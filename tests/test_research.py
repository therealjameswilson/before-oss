from __future__ import annotations

import sqlite3
import unittest

from oss_research.research import (
    assign_page_batch,
    candidate_aware_status,
    discovery_outcome,
    has_unreviewed_research_candidate,
    record_discovery_progress,
    source_query_options,
)


class PageBatchAssignmentTests(unittest.TestCase):
    def setUp(self) -> None:
        self.connection = sqlite3.connect(":memory:")
        self.connection.row_factory = sqlite3.Row
        self.connection.executescript(
            """
            CREATE TABLE source_records(
                source_record_id TEXT PRIMARY KEY,
                source_page INTEGER NOT NULL,
                source_row_number INTEGER NOT NULL
            );
            CREATE TABLE person_source_links(
                source_record_id TEXT NOT NULL,
                person_id TEXT NOT NULL
            );
            CREATE TABLE entity_supersessions(
                superseded_person_id TEXT PRIMARY KEY,
                canonical_person_id TEXT NOT NULL
            );
            CREATE TABLE research_queue(
                person_id TEXT PRIMARY KEY,
                assigned_batch TEXT,
                protocol_version TEXT NOT NULL,
                updated_at TEXT NOT NULL
            );
            INSERT INTO source_records VALUES ('row-1', 117, 1), ('row-2', 117, 2);
            INSERT INTO person_source_links VALUES
                ('row-1', 'person-1'), ('row-2', 'person-2');
            INSERT INTO research_queue VALUES
                ('person-1', NULL, 'old', 'old-time'),
                ('person-2', NULL, 'old', 'old-time'),
                ('person-3', NULL, 'old', 'old-time');
            """
        )

    def tearDown(self) -> None:
        self.connection.close()

    def test_assigns_exact_range_and_repeat_is_idempotent(self) -> None:
        first = assign_page_batch(
            self.connection,
            batch_name="batch-580",
            source_page=117,
            first_row=1,
            last_row=2,
        )
        self.assertEqual(first["source_rows"], 2)
        self.assertEqual(first["person_entities"], 2)
        self.assertEqual(first["newly_assigned_people"], 2)
        self.assertEqual(first["person_ids"], ["person-1", "person-2"])
        before = self.connection.execute(
            "SELECT updated_at FROM research_queue WHERE person_id='person-1'"
        ).fetchone()[0]
        second = assign_page_batch(
            self.connection,
            batch_name="batch-580",
            source_page=117,
            first_row=1,
            last_row=2,
        )
        after = self.connection.execute(
            "SELECT updated_at FROM research_queue WHERE person_id='person-1'"
        ).fetchone()[0]
        self.assertEqual(second["newly_assigned_people"], 0)
        self.assertEqual(before, after)

    def test_missing_or_unlinked_row_fails_without_partial_assignment(self) -> None:
        with self.assertRaisesRegex(ValueError, "no printed source row"):
            assign_page_batch(
                self.connection,
                batch_name="batch-580",
                source_page=117,
                first_row=1,
                last_row=3,
            )
        self.connection.execute(
            "DELETE FROM person_source_links WHERE source_record_id='row-2'"
        )
        with self.assertRaisesRegex(ValueError, "unlinked source row"):
            assign_page_batch(
                self.connection,
                batch_name="batch-580",
                source_page=117,
                first_row=1,
                last_row=2,
            )
        self.assertEqual(
            self.connection.execute(
                "SELECT COUNT(*) FROM research_queue WHERE assigned_batch IS NOT NULL"
            ).fetchone()[0],
            0,
        )

    def test_conflicting_assignment_or_batch_name_fails(self) -> None:
        self.connection.execute(
            "UPDATE research_queue SET assigned_batch='other' WHERE person_id='person-2'"
        )
        with self.assertRaisesRegex(ValueError, "another batch"):
            assign_page_batch(
                self.connection,
                batch_name="batch-580",
                source_page=117,
                first_row=1,
                last_row=2,
            )
        self.connection.execute(
            "UPDATE research_queue SET assigned_batch=NULL WHERE person_id='person-2'"
        )
        self.connection.execute(
            "UPDATE research_queue SET assigned_batch='batch-580' WHERE person_id='person-3'"
        )
        with self.assertRaisesRegex(ValueError, "outside this row range"):
            assign_page_batch(
                self.connection,
                batch_name="batch-580",
                source_page=117,
                first_row=1,
                last_row=2,
            )

    def test_superseded_row_routes_to_canonical_person(self) -> None:
        self.connection.execute(
            "INSERT INTO entity_supersessions VALUES ('person-2', 'person-1')"
        )
        result = assign_page_batch(
            self.connection,
            batch_name="batch-580",
            source_page=117,
            first_row=1,
            last_row=2,
        )
        self.assertEqual(result["source_rows"], 2)
        self.assertEqual(result["person_ids"], ["person-1"])
        self.assertEqual(result["newly_assigned_people"], 1)

    def test_batch_name_and_range_are_bounded(self) -> None:
        for name in ("Batch580", "../batch", "", "a" * 65):
            with self.subTest(name=name), self.assertRaisesRegex(ValueError, "slug"):
                assign_page_batch(
                    self.connection,
                    batch_name=name,
                    source_page=117,
                    first_row=1,
                    last_row=2,
                )
        with self.assertRaisesRegex(ValueError, "at most 100"):
            assign_page_batch(
                self.connection,
                batch_name="batch-580",
                source_page=117,
                first_row=1,
                last_row=101,
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

    def test_unavailable_source_is_never_a_negative_search_result(self) -> None:
        self.assertEqual(
            discovery_outcome(planned=False, http_status=200, candidate_count=0),
            "no_result",
        )
        self.assertEqual(
            discovery_outcome(planned=False, http_status=200, candidate_count=1),
            "candidate_found",
        )
        for status in (None, 401, 403, 429, 503):
            with self.subTest(status=status):
                self.assertEqual(
                    discovery_outcome(
                        planned=False, http_status=status, candidate_count=0
                    ),
                    "blocked",
                )
        self.assertEqual(
            discovery_outcome(planned=True, http_status=None, candidate_count=0),
            "planned",
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
                candidate_url TEXT,
                match_assessment TEXT
            )
            """
        )
        connection.execute(
            """
            INSERT INTO candidate_matches
            VALUES ('person-1', 'duplicate_person', NULL, 'unreviewed')
            """
        )
        self.assertFalse(
            has_unreviewed_research_candidate(connection, "person-1")
        )
        connection.execute(
            """
            INSERT INTO candidate_matches
            VALUES ('person-1', 'identity',
                    'https://catalog.archives.gov/id/1263923', 'unreviewed')
            """
        )
        self.assertFalse(
            has_unreviewed_research_candidate(connection, "person-1")
        )
        connection.execute(
            """
            INSERT INTO candidate_matches
            VALUES ('person-1', 'source', NULL, 'unreviewed')
            """
        )
        self.assertTrue(
            has_unreviewed_research_candidate(connection, "person-1")
        )


class DiscoveryStatusPreservationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.connection = sqlite3.connect(":memory:")
        self.connection.row_factory = sqlite3.Row
        self.connection.executescript(
            """
            CREATE TABLE person_entities(
                person_id TEXT PRIMARY KEY,
                research_status TEXT NOT NULL,
                research_started_at TEXT,
                research_attempt_number INTEGER NOT NULL,
                next_action TEXT,
                research_agent_version TEXT,
                updated_at TEXT
            );
            CREATE TABLE research_queue(
                person_id TEXT PRIMARY KEY,
                research_status TEXT NOT NULL,
                attempts INTEGER NOT NULL,
                next_action TEXT,
                updated_at TEXT
            );
            INSERT INTO person_entities VALUES
                ('person-1', 'not_started', NULL, 0,
                 'Keep reviewed action', 'manual-review', 'old-time');
            INSERT INTO research_queue VALUES
                ('person-1', 'not_started', 0,
                 'Keep reviewed action', 'old-time');
            """
        )

    def tearDown(self) -> None:
        self.connection.close()

    def test_new_candidate_advances_only_an_automatic_discovery_status(self) -> None:
        record_discovery_progress(
            self.connection,
            person_id="person-1",
            candidate_count=1,
            has_unreviewed_candidates=True,
        )
        person = self.connection.execute(
            "SELECT * FROM person_entities WHERE person_id='person-1'"
        ).fetchone()
        queue = self.connection.execute(
            "SELECT * FROM research_queue WHERE person_id='person-1'"
        ).fetchone()
        self.assertEqual(person["research_status"], "candidate_found")
        self.assertIn("Review discovery candidates", person["next_action"])
        self.assertEqual(queue["research_status"], "candidate_found")
        self.assertEqual(person["research_attempt_number"], 1)
        self.assertEqual(queue["attempts"], 1)

    def test_supplemental_search_preserves_reviewed_status_and_next_action(self) -> None:
        reviewed_statuses = (
            "requires_archival_review",
            "verified_employer_found",
            "documented_prewar_employer_found",
            "occupation_only_found",
            "no_reliable_result_after_protocol",
            "conflicting_sources",
            "needs_identity_review",
            "needs_temporal_review",
            "blocked_by_source_access",
            "completed",
        )
        for status in reviewed_statuses:
            with self.subTest(status=status):
                self.connection.execute(
                    """
                    UPDATE person_entities
                    SET research_status=?, research_attempt_number=4,
                        next_action='Keep reviewed action',
                        research_agent_version='manual-review'
                    WHERE person_id='person-1'
                    """,
                    (status,),
                )
                self.connection.execute(
                    """
                    UPDATE research_queue
                    SET research_status=?, attempts=4,
                        next_action='Keep reviewed action'
                    WHERE person_id='person-1'
                    """,
                    (status,),
                )
                record_discovery_progress(
                    self.connection,
                    person_id="person-1",
                    candidate_count=1,
                    has_unreviewed_candidates=True,
                )
                person = self.connection.execute(
                    "SELECT * FROM person_entities WHERE person_id='person-1'"
                ).fetchone()
                queue = self.connection.execute(
                    "SELECT * FROM research_queue WHERE person_id='person-1'"
                ).fetchone()
                self.assertEqual(person["research_status"], status)
                self.assertEqual(queue["research_status"], status)
                self.assertEqual(person["next_action"], "Keep reviewed action")
                self.assertEqual(queue["next_action"], "Keep reviewed action")
                self.assertEqual(person["research_agent_version"], "manual-review")
                self.assertEqual(person["research_attempt_number"], 5)
                self.assertEqual(queue["attempts"], 5)


if __name__ == "__main__":
    unittest.main()
