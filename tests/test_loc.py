from __future__ import annotations

import json
import unittest
import urllib.error
from pathlib import Path

from oss_research.config import Settings
from oss_research.db import connect, migrate
from oss_research.sources.common import ResponseData
from oss_research.sources.loc import LocAdapter


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

    def test_respects_retry_after_for_429(self) -> None:
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
        self.assertEqual(result["http_status"], 200)
        self.assertEqual(sleeps, [0.0])

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
