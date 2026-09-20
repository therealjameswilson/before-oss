from __future__ import annotations

import json
import unittest
import urllib.error
from pathlib import Path

from oss_research.config import Settings
from oss_research.db import connect, migrate
from oss_research.sources.common import ResponseData
from oss_research.sources.common import audit_request, request_fingerprint
from oss_research.sources.loc import (
    LOC_MIN_INTERVAL_SECONDS,
    LocAdapter,
    LocRateLimitCooldown,
)


def settings() -> Settings:
    return Settings(
        research_scope="all_personnel",
        contact_email="historian@example.org",
        nara_api_base_url="https://catalog.archives.gov/api/v2",
        nara_api_key=None,
        nara_api_enabled=False,
        nara_monthly_hard_limit=10000,
        nara_monthly_soft_limit=9000,
        nara_timeout_seconds=30.0,
        nara_max_retries=2,
        nara_max_concurrency=2,
        nara_per_run_query_budget=500,
        loc_api_base_url="https://www.loc.gov",
        loc_timeout_seconds=30.0,
        loc_max_retries=3,
        cia_base_url="https://www.cia.gov/readingroom",
        site_title="Before OSS",
        site_subtitle="Test",
        public_base_path="/before-oss",
    )


class LocAdapterTests(unittest.TestCase):
    def setUp(self) -> None:
        self.connection = connect(Path(":memory:"))
        migrate(self.connection)
        now = "2026-08-03T00:00:00+00:00"
        with self.connection:
            for index in range(1, 4):
                self.connection.execute(
                    """
                    INSERT INTO person_entities(
                        person_id, display_name, normalized_name, identity_status,
                        name_variants_json, personnel_category, difficulty_tier,
                        manual_review_required, research_status,
                        research_attempt_number, personnel_file_indexed,
                        personnel_file_reviewed, archival_review_priority,
                        created_at, updated_at
                    ) VALUES (?, ?, ?, 'unresolved', '[]',
                              'unknown_or_indeterminate', 1, 1, 'not_started',
                              0, 1, 0, 'unassessed', ?, ?)
                    """,
                    (
                        f"person-{index}",
                        f"Example Person {index}",
                        f"EXAMPLE PERSON {index}",
                        now,
                        now,
                    ),
                )

    def tearDown(self) -> None:
        self.connection.close()

    def test_retries_timeout_then_succeeds_and_audits_retry(self) -> None:
        responses: list[object] = [
            TimeoutError("synthetic timeout"),
            ResponseData(
                200,
                {},
                json.dumps(
                    {
                        "results": [
                            {
                                "id": "https://www.loc.gov/resource/example/",
                                "title": "Synthetic newspaper page",
                                "date": "1942-01-01",
                            }
                        ]
                    }
                ).encode("utf-8"),
            ),
        ]
        sleeps: list[float] = []

        def transport(_request: object, _timeout: float) -> ResponseData:
            response = responses.pop(0)
            if isinstance(response, Exception):
                raise response
            return response

        adapter = LocAdapter(
            self.connection,
            settings(),
            transport=transport,
            sleep=sleeps.append,
        )
        result = adapter.search("Jane Example", person_id="person-1")
        self.assertEqual(result["http_status"], 200)
        self.assertEqual(result["candidate_count"], 1)
        self.assertEqual(len(sleeps), 1)
        audit = self.connection.execute(
            "SELECT retry_count, error_class FROM request_audit WHERE adapter = 'loc'"
        ).fetchone()
        self.assertEqual(audit["retry_count"], 1)
        self.assertIsNone(audit["error_class"])

    def test_429_stops_without_retry_and_enforces_project_cooldown(self) -> None:
        responses = [
            ResponseData(429, {"retry-after": "0"}, b"{}"),
            ResponseData(200, {}, b'{"results": []}'),
        ]
        sleeps: list[float] = []

        def transport(_request: object, _timeout: float) -> ResponseData:
            return responses.pop(0)

        result = LocAdapter(
            self.connection,
            settings(),
            transport=transport,
            sleep=sleeps.append,
        ).search("Retry Example", person_id="person-2")
        self.assertEqual(result["http_status"], 429)
        self.assertEqual(sleeps, [])
        self.assertEqual(len(responses), 1)
        with self.assertRaisesRegex(LocRateLimitCooldown, "no request was sent"):
            LocAdapter(
                self.connection,
                settings(),
                transport=transport,
                sleep=sleeps.append,
            ).search("Another query", person_id="person-2")
        self.assertEqual(len(responses), 1)

    def test_default_spacing_stays_below_published_twenty_per_minute(self) -> None:
        adapter = LocAdapter(self.connection, settings())
        self.assertGreaterEqual(adapter.limiter.minimum_interval_seconds, 3.0)
        self.assertEqual(adapter.limiter.minimum_interval_seconds, LOC_MIN_INTERVAL_SECONDS)

    def test_reuses_successful_query_from_prior_adapter_version(self) -> None:
        query = '"Example Person 1" employer 1940'
        old_fingerprint = request_fingerprint(
            "loc-chronicling-america-v2",
            "GET",
            "/collections/chronicling-america/",
            {"q": query, "fo": "json", "c": 5, "at": "results,pagination"},
        )
        with self.connection:
            audit_request(
                self.connection,
                adapter="loc",
                fingerprint=old_fingerprint,
                query_text=query,
                status=200,
                adapter_version="loc-chronicling-america-v2",
                person_id="person-1",
            )
        calls = []

        def transport(request: object, _timeout: float) -> ResponseData:
            calls.append(request)
            return ResponseData(200, {}, b'{"results": []}')

        result = LocAdapter(
            self.connection,
            settings(),
            transport=transport,
        ).search(query, person_id="person-2")
        self.assertTrue(result["duplicate_request"])
        self.assertEqual(result["fingerprint"], old_fingerprint)
        self.assertEqual(calls, [])

    def test_rebuilt_database_reuses_sanitized_successful_attempt(self) -> None:
        query = '"Example Person 1" occupation 1940'
        old_fingerprint = request_fingerprint(
            "loc-chronicling-america-v2",
            "GET",
            "/collections/chronicling-america/",
            {"q": query, "fo": "json", "c": 5, "at": "results,pagination"},
        )
        with self.connection:
            self.connection.execute(
                """
                INSERT INTO research_attempts(
                    research_attempt_id, person_id, source_adapter,
                    request_fingerprint, started_at, completed_at,
                    outcome, attempt_number, research_agent_version
                ) VALUES ('rebuilt-attempt', 'person-1', 'loc', ?,
                          '2026-08-03T00:00:00Z', '2026-08-03T00:00:01Z',
                          'no_result', 1, 'checkpoint-test')
                """,
                (old_fingerprint,),
            )

        def forbidden(_request: object, _timeout: float) -> ResponseData:
            self.fail("Completed checkpoint was unexpectedly searched again")

        result = LocAdapter(
            self.connection,
            settings(),
            transport=forbidden,
        ).search(query, person_id="person-2")
        self.assertTrue(result["duplicate_request"])
        self.assertEqual(result["fingerprint"], old_fingerprint)
        self.assertEqual(
            self.connection.execute("SELECT COUNT(*) FROM request_audit").fetchone()[0],
            0,
        )

    def test_final_transport_error_is_durably_audited(self) -> None:
        def transport(_request: object, _timeout: float) -> ResponseData:
            raise urllib.error.URLError("synthetic outage")

        with self.assertRaises(urllib.error.URLError):
            LocAdapter(
                self.connection,
                settings(),
                transport=transport,
                sleep=lambda _delay: None,
            ).search("Unavailable Example", person_id="person-3")
        audit = self.connection.execute(
            "SELECT http_status, error_class, retry_count FROM request_audit "
            "WHERE adapter = 'loc'"
        ).fetchone()
        self.assertIsNone(audit["http_status"])
        self.assertEqual(audit["error_class"], "URLError")
        self.assertEqual(audit["retry_count"], 3)

        recovered = LocAdapter(
            self.connection,
            settings(),
            transport=lambda _request, _timeout: ResponseData(
                200,
                {},
                b'{"results": []}',
            ),
            sleep=lambda _delay: None,
        ).search("Unavailable Example", person_id="person-3")
        self.assertFalse(recovered["duplicate_request"])
        self.assertEqual(recovered["http_status"], 200)
        recovered_audit = self.connection.execute(
            "SELECT http_status, error_class FROM request_audit WHERE adapter = 'loc'"
        ).fetchone()
        self.assertEqual(recovered_audit["http_status"], 200)
        self.assertIsNone(recovered_audit["error_class"])


if __name__ == "__main__":
    unittest.main()
