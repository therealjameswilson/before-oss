from __future__ import annotations

import unittest
import urllib.error
from pathlib import Path

from oss_research.config import Settings
from oss_research.db import connect, migrate
from oss_research.sources.cia import CiaAdapter
from oss_research.sources.common import ResponseData


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
        def unavailable(_request: object, _timeout: float) -> ResponseData:
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

        recovered = CiaAdapter(
            self.connection,
            settings(),
            transport=lambda _request, _timeout: ResponseData(200, {}, b""),
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


if __name__ == "__main__":
    unittest.main()
