from __future__ import annotations

import sqlite3
import unittest

from oss_research.research import (
    candidate_aware_status,
    has_unreviewed_research_candidate,
    source_query_options,
)


class ResearchQuerySchedulerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.families = {
            "official": ["official one", "official two"],
            "exact_oss": ["exact one", "exact two"],
            "employment": ["employer", "occupation"],
            "institutional": ["obituary", "biography"],
        }

    def test_loc_advances_through_employment_and_institutional_queries(self) -> None:
        self.assertEqual(
            source_query_options("loc", self.families),
            [
                ("employment", "employer"),
                ("employment", "occupation"),
                ("institutional", "obituary"),
                ("institutional", "biography"),
            ],
        )

    def test_web_options_are_staged_and_deduplicated(self) -> None:
        families = dict(self.families)
        families["employment"] = ["exact two", "employer"]
        self.assertEqual(
            source_query_options("web", families),
            [
                ("exact_oss", "exact one"),
                ("exact_oss", "exact two"),
                ("employment", "employer"),
                ("institutional", "obituary"),
                ("institutional", "biography"),
            ],
        )

    def test_unreviewed_candidate_survives_a_later_no_result(self) -> None:
        status, person_action, queue_action = candidate_aware_status(0, True)
        self.assertEqual(status, "candidate_found")
        self.assertIn("Review discovery candidates", person_action)
        self.assertEqual(queue_action, "Review source candidates.")

    def test_duplicate_resolution_candidate_does_not_change_research_status(
        self,
    ) -> None:
        connection = sqlite3.connect(":memory:")
        connection.execute(
            """
            CREATE TABLE candidate_matches(
                person_id TEXT,
                candidate_type TEXT,
                match_assessment TEXT
            )
            """
        )
        connection.execute(
            """
            INSERT INTO candidate_matches
            VALUES ('person-1', 'duplicate_person', 'unreviewed')
            """
        )
        self.assertFalse(
            has_unreviewed_research_candidate(connection, "person-1")
        )
        connection.execute(
            """
            INSERT INTO candidate_matches
            VALUES ('person-1', 'source', 'unreviewed')
            """
        )
        self.assertTrue(
            has_unreviewed_research_candidate(connection, "person-1")
        )


if __name__ == "__main__":
    unittest.main()
