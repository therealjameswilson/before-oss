from __future__ import annotations

import json
import sqlite3
import unittest
from pathlib import Path

from oss_research.config import Settings
from oss_research.db import connect, migrate
from oss_research.sources.common import ResponseData
from oss_research.sources.nara import (
    NaraAdapter,
    NaraConfigurationError,
)


def settings(**changes: object) -> Settings:
    values: dict[str, object] = {
        "research_scope": "all_personnel",
        "contact_email": "historian@example.org",
        "nara_api_base_url": "https://catalog.archives.gov/api/v2",
        "nara_api_key": "TEST_ONLY_NOT_LIVE",
        "nara_api_enabled": True,
        "nara_monthly_hard_limit": 10000,
        "nara_monthly_soft_limit": 9000,
        "nara_timeout_seconds": 30.0,
        "nara_max_retries": 2,
        "nara_max_concurrency": 2,
        "nara_per_run_query_budget": 500,
        "loc_api_base_url": "https://www.loc.gov",
        "cia_base_url": "https://www.cia.gov/readingroom",
        "site_title": "Before OSS",
        "site_subtitle": "Test",
        "public_base_path": "/before-oss",
    }
    values.update(changes)
    return Settings(**values)


class NaraAdapterTests(unittest.TestCase):
    def setUp(self) -> None:
        self.connection = connect(Path(":memory:"))
        migrate(self.connection)

    def tearDown(self) -> None:
        self.connection.close()

    def test_dry_run_needs_no_key_and_makes_no_request(self) -> None:
        called = False

        def transport(_request: object, _timeout: float) -> ResponseData:
            nonlocal called
            called = True
            raise AssertionError("transport should not be called")

        adapter = NaraAdapter(
            self.connection,
            settings(nara_api_key=None, contact_email=""),
            transport=transport,
        )
        result = adapter.search('"Jane Example" OSS', dry_run=True)
        self.assertTrue(result.planned)
        self.assertFalse(called)
        self.assertEqual(
            self.connection.execute("SELECT COUNT(*) FROM request_audit").fetchone()[0],
            0,
        )

    def test_dry_run_resume_skips_an_existing_plan(self) -> None:
        adapter = NaraAdapter(
            self.connection,
            settings(nara_api_key=None, contact_email=""),
        )
        first = adapter.search('"Jane Example" OSS', dry_run=True)
        now = "2026-07-29T00:00:00+00:00"
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
                ) VALUES (
                    'person-1', 'Jane Example', 'JANE EXAMPLE', 'unresolved',
                    '[]', 'unknown_or_indeterminate', 1, 1, 'not_started',
                    0, 1, 0, 'unassessed', ?, ?
                )
                """,
                (now, now),
            )
            self.connection.execute(
                """
                INSERT INTO research_attempts(
                    research_attempt_id, person_id, source_adapter, query_text,
                    query_variant_type, request_fingerprint, started_at,
                    completed_at, outcome, attempt_number,
                    research_agent_version
                ) VALUES (
                    'attempt-1', 'person-1', 'nara', '"Jane Example" OSS',
                    'official', ?, ?, ?, 'planned', 1, 'test'
                )
                """,
                (first.fingerprint, now, now),
            )
        resumed = adapter.search('"Jane Example" OSS', dry_run=True)
        self.assertTrue(resumed.duplicate_request)
        self.assertFalse(resumed.planned)

    def test_live_request_fails_closed_without_key(self) -> None:
        adapter = NaraAdapter(
            self.connection, settings(nara_api_key=None)
        )
        with self.assertRaises(NaraConfigurationError):
            adapter.search('"Jane Example" OSS')

    def test_minimizes_response_to_naid_and_never_stores_body(self) -> None:
        fixture = (
            Path(__file__).parent / "fixtures" / "nara_search_minimal.json"
        ).read_bytes()
        seen_headers: dict[str, str] = {}

        def transport(request: object, _timeout: float) -> ResponseData:
            nonlocal seen_headers
            seen_headers = dict(request.header_items())
            return ResponseData(200, {}, fixture)

        adapter = NaraAdapter(
            self.connection, settings(), transport=transport
        )
        result = adapter.search('"Jane Example" OSS')
        self.assertEqual(result.candidate_naids, ("123456789",))
        self.assertIn("X-api-key", seen_headers)
        dump = "\n".join(
            str(value)
            for row in self.connection.iterdump()
            for value in [row]
        )
        self.assertNotIn("Synthetic test record", dump)
        self.assertNotIn("TEST_ONLY_NOT_LIVE", dump)

    def test_retries_429_then_succeeds(self) -> None:
        fixture = (
            Path(__file__).parent / "fixtures" / "nara_search_minimal.json"
        ).read_bytes()
        responses = [
            ResponseData(429, {"retry-after": "0"}, b"{}"),
            ResponseData(200, {}, fixture),
        ]
        sleeps: list[float] = []

        def transport(_request: object, _timeout: float) -> ResponseData:
            return responses.pop(0)

        adapter = NaraAdapter(
            self.connection,
            settings(),
            transport=transport,
            sleep=sleeps.append,
        )
        result = adapter.search('"Retry Example" OSS')
        self.assertEqual(result.http_status, 200)
        self.assertEqual(len(sleeps), 1)


if __name__ == "__main__":
    unittest.main()
