from __future__ import annotations

import unittest
import urllib.error
from pathlib import Path

from oss_research.config import Settings
from oss_research.db import connect, migrate
from oss_research.sources.cia import (
    CiaAdapter,
    CiaRobotsDisallowed,
    CiaRobotsUnavailable,
)
from oss_research.sources.common import (
    DomainRateLimiter,
    ResponseData,
    audit_request,
    request_fingerprint,
)


ALLOW_ROBOTS = b"User-agent: *\nAllow: /readingroom/search/\nCrawl-delay: 10\n"
DENY_ROBOTS = b"User-agent: *\nDisallow: /readingroom/search/\nCrawl-delay: 10\n"


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


class CiaAdapterTests(unittest.TestCase):
    def setUp(self) -> None:
        self.connection = connect(Path(":memory:"))
        migrate(self.connection)
        now = "2026-09-12T00:00:00+00:00"
        with self.connection:
            self.connection.execute(
                """
                INSERT INTO person_entities(
                    person_id, display_name, normalized_name, identity_status,
                    name_variants_json, personnel_category, difficulty_tier,
                    manual_review_required, research_status,
                    research_attempt_number, personnel_file_indexed,
                    personnel_file_reviewed, archival_review_priority,
                    created_at, updated_at
                ) VALUES ('person-1', 'Example Person', 'EXAMPLE PERSON',
                          'unresolved', '[]', 'unknown_or_indeterminate', 1,
                          1, 'not_started', 0, 1, 0, 'unassessed', ?, ?)
                """,
                (now, now),
            )

    def tearDown(self) -> None:
        self.connection.close()

    def test_transient_transport_failure_can_be_resumed(self) -> None:
        def unavailable(request: object, _timeout: float) -> ResponseData:
            if request.full_url.endswith("/robots.txt"):
                return ResponseData(200, {}, ALLOW_ROBOTS)
            raise urllib.error.URLError("synthetic outage")

        with self.assertRaises(urllib.error.URLError):
            CiaAdapter(
                self.connection,
                settings(),
                transport=unavailable,
                sleep=lambda _delay: None,
            ).search("Example Person", person_id="person-1")

        failed = self.connection.execute(
            "SELECT http_status, error_class FROM request_audit WHERE adapter = 'cia'"
        ).fetchone()
        self.assertIsNone(failed["http_status"])
        self.assertEqual(failed["error_class"], "URLError")

        def available(request: object, _timeout: float) -> ResponseData:
            if request.full_url.endswith("/robots.txt"):
                return ResponseData(200, {}, ALLOW_ROBOTS)
            return ResponseData(200, {}, b"")

        recovered = CiaAdapter(
            self.connection,
            settings(),
            transport=available,
            sleep=lambda _delay: None,
        ).search("Example Person", person_id="person-1")
        self.assertFalse(recovered["duplicate_request"])
        self.assertEqual(recovered["http_status"], 200)
        self.assertEqual(recovered["candidate_count"], 0)

        audit = self.connection.execute(
            "SELECT http_status, error_class FROM request_audit WHERE adapter = 'cia'"
        ).fetchone()
        self.assertEqual(audit["http_status"], 200)
        self.assertIsNone(audit["error_class"])

    def test_disallowed_path_is_never_requested_or_counted_as_research(self) -> None:
        requested: list[str] = []

        def deny(request: object, _timeout: float) -> ResponseData:
            requested.append(request.full_url)
            return ResponseData(200, {}, DENY_ROBOTS)

        adapter = CiaAdapter(self.connection, settings(), transport=deny)
        with self.assertRaisesRegex(CiaRobotsDisallowed, "no CIA search was sent"):
            adapter.search("Example Person", person_id="person-1")
        self.assertEqual(requested, ["https://www.cia.gov/robots.txt"])
        self.assertEqual(
            self.connection.execute("SELECT COUNT(*) FROM request_audit").fetchone()[0],
            0,
        )

    def test_unavailable_robots_policy_fails_closed(self) -> None:
        requested: list[str] = []

        def unavailable(request: object, _timeout: float) -> ResponseData:
            requested.append(request.full_url)
            return ResponseData(503, {}, b"")

        with self.assertRaisesRegex(CiaRobotsUnavailable, "CIA discovery was not sent"):
            CiaAdapter(self.connection, settings(), transport=unavailable).search(
                "Example Person", person_id="person-1"
            )
        self.assertEqual(requested, ["https://www.cia.gov/robots.txt"])

    def test_changed_robots_policy_preserves_failed_retry_audit(self) -> None:
        query = "Example Person"
        path = "/search/site/Example%20Person"
        fingerprint = request_fingerprint(
            "cia-reading-room-html-v2-robots", "GET", path, {}
        )
        with self.connection:
            audit_request(
                self.connection,
                adapter="cia",
                fingerprint=fingerprint,
                query_text=query,
                status=None,
                adapter_version="cia-reading-room-html-v2-robots",
                person_id="person-1",
                error_class="URLError",
            )
        requested: list[str] = []

        def deny(request: object, _timeout: float) -> ResponseData:
            requested.append(request.full_url)
            return ResponseData(200, {}, DENY_ROBOTS)

        with self.assertRaises(CiaRobotsDisallowed):
            CiaAdapter(self.connection, settings(), transport=deny).search(
                query, person_id="person-1"
            )
        self.assertEqual(requested, ["https://www.cia.gov/robots.txt"])
        self.assertEqual(
            self.connection.execute(
                "SELECT COUNT(*) FROM request_audit WHERE adapter='cia'"
            ).fetchone()[0],
            1,
        )

    def test_allowed_policy_applies_crawl_delay(self) -> None:
        requested: list[str] = []

        def allow(request: object, _timeout: float) -> ResponseData:
            requested.append(request.full_url)
            if request.full_url.endswith("/robots.txt"):
                return ResponseData(200, {}, ALLOW_ROBOTS)
            return ResponseData(200, {}, b"")

        limiter = DomainRateLimiter(1.0)
        adapter = CiaAdapter(
            self.connection, settings(), transport=allow, limiter=limiter
        )
        result = adapter.search("Example Person", person_id="person-1")
        self.assertEqual(result["http_status"], 200)
        self.assertEqual(len(requested), 2)
        self.assertEqual(limiter.minimum_interval_seconds, 10.0)

    def test_dry_run_never_requests_robots_or_search(self) -> None:
        def forbidden(_request: object, _timeout: float) -> ResponseData:
            self.fail("Dry-run unexpectedly made a network request")

        result = CiaAdapter(
            self.connection, settings(), transport=forbidden
        ).search("Example Person", person_id="person-1", dry_run=True)
        self.assertTrue(result["planned"])


if __name__ == "__main__":
    unittest.main()
