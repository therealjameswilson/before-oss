from __future__ import annotations

import csv
import json
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path

from oss_research.db import connect, migrate
from oss_research.exports import coverage_report
from oss_research.review import import_review_decisions


class ReviewDecisionTests(unittest.TestCase):
    def _display_correction(self, expected="Example Person", replacement="Example A. Person"):
        path = Path(self.temp_dir.name) / "display_review.csv"
        with path.open("w", newline="", encoding="utf-8") as stream:
            writer = csv.writer(stream)
            writer.writerow(["target_type", "target_id", "decision", "rationale", "reviewer", "decision_version"])
            writer.writerow(["person_entity", "person-1", "display_name:" + json.dumps({
                "expected": expected, "replacement": replacement,
            }), "Reviewed name presentation; raw source unchanged.", "Unit test", "display-v1"])
        return path

    def test_guarded_display_correction_preserves_sources_identity_and_audit(self):
        source_before = [tuple(row) for row in self.connection.execute("SELECT * FROM source_records")]
        links_before = [tuple(row) for row in self.connection.execute("SELECT * FROM person_source_links")]
        path = self._display_correction()
        first = import_review_decisions(self.connection, path)
        self.assertEqual(first["state_changes_applied"], 1)
        second = import_review_decisions(self.connection, path)
        self.assertEqual(second["duplicates_skipped"], 1)
        self.assertEqual(second["state_changes_applied"], 0)
        row = self.connection.execute("SELECT * FROM person_entities WHERE person_id='person-1'").fetchone()
        self.assertEqual(row["display_name"], "Example A. Person")
        self.assertEqual(row["normalized_name"], "EXAMPLE A PERSON")
        self.assertEqual(row["identity_status"], "unresolved")
        self.assertEqual(json.loads(row["name_variants_json"]), ["Example A. Person", "Example Person"])
        self.assertEqual(source_before, [tuple(row) for row in self.connection.execute("SELECT * FROM source_records")])
        self.assertEqual(links_before, [tuple(row) for row in self.connection.execute("SELECT * FROM person_source_links")])
        self.assertEqual(self.connection.execute("SELECT COUNT(*) FROM review_decisions").fetchone()[0], 1)

    def test_display_correction_rejects_stale_or_empty_values_without_writes(self):
        for expected, replacement in [("Another Name", "Example A. Person"), ("Example Person", " ")]:
            with self.subTest(expected=expected, replacement=replacement):
                with self.assertRaises(ValueError):
                    import_review_decisions(self.connection, self._display_correction(expected, replacement))
                self.assertEqual(self.connection.execute("SELECT COUNT(*) FROM review_decisions").fetchone()[0], 0)
                self.assertEqual(self.connection.execute("SELECT display_name FROM person_entities WHERE person_id='person-1'").fetchone()[0], "Example Person")

    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.database = Path(self.temp_dir.name) / "test.sqlite"
        self.connection = connect(self.database)
        migrate(self.connection)
        now = "2026-07-30T00:00:00+00:00"
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
                    'person-1', 'Example Person', 'EXAMPLE PERSON', 'unresolved',
                    '[]', 'unknown_or_indeterminate', 1, 1, 'candidate_found',
                    1, 1, 0, 'unassessed', ?, ?
                )
                """,
                (now, now),
            )
            self.connection.execute(
                """
                INSERT INTO person_entities(
                    person_id, display_name, normalized_name, identity_status,
                    name_variants_json, personnel_category, difficulty_tier,
                    manual_review_required, possible_duplicate_group,
                    research_status, research_attempt_number,
                    personnel_file_indexed, personnel_file_reviewed,
                    archive_box, archive_location, archival_review_priority,
                    created_at, updated_at
                ) VALUES (
                    'person-2', 'Example Alias', 'EXAMPLE ALIAS', 'unresolved',
                    '["Alias, Example"]', 'enlisted_army_personnel', 2, 1,
                    'serial-conflict:test', 'not_started', 0, 1, 0,
                    '20', 'shelf-b', 'unassessed', ?, ?
                )
                """,
                (now, now),
            )
            for source_id, page in (("source-1", 1), ("source-2", 2)):
                self.connection.execute(
                    """
                    INSERT INTO source_records(
                        source_record_id, source_pdf, source_pdf_sha256,
                        source_page, source_row_number, raw_row_text,
                        last_name_raw, display_name, normalized_name, last_name,
                        personnel_category, name_variants_json,
                        parser_confidence, requires_visual_review,
                        entity_resolution_status, ingested_at, parser_version
                    ) VALUES (
                        ?, 'test.pdf', 'sha', ?, 1, 'row', 'Example',
                        'Example Person', 'EXAMPLE PERSON', 'Example',
                        'unknown_or_indeterminate', '[]', 1.0, 0,
                        'linked', ?, 'test-v1'
                    )
                    """,
                    (source_id, page, now),
                )
            self.connection.execute(
                """
                INSERT INTO person_source_links(
                    person_id, source_record_id, link_status, evidence,
                    algorithm_version, manual_review_required, created_at
                ) VALUES ('person-1', 'source-1', 'unresolved', 'initial',
                          'test-v1', 1, ?)
                """,
                (now,),
            )
            self.connection.execute(
                """
                INSERT INTO person_source_links(
                    person_id, source_record_id, link_status, evidence,
                    algorithm_version, manual_review_required, created_at
                ) VALUES ('person-2', 'source-2', 'unresolved', 'initial',
                          'test-v1', 1, ?)
                """,
                (now,),
            )
            self.connection.execute(
                """
                INSERT INTO research_queue(
                    person_id, difficulty_tier, priority, research_status,
                    attempts, protocol_version, updated_at
                ) VALUES ('person-1', 1, 10, 'candidate_found', 1, 'test-v1', ?)
                """,
                (now,),
            )
            self.connection.execute(
                """
                INSERT INTO research_queue(
                    person_id, difficulty_tier, priority, research_status,
                    attempts, protocol_version, updated_at
                ) VALUES ('person-2', 2, 20, 'not_started', 0, 'test-v1', ?)
                """,
                (now,),
            )
            self.connection.execute(
                """
                INSERT INTO candidate_matches(
                    candidate_match_id, person_id, candidate_type,
                    candidate_label, evidence_json, match_assessment,
                    created_at, updated_at
                ) VALUES (
                    'candidate-1', 'person-1', 'source', 'Example candidate',
                    '{}', 'unreviewed', ?, ?
                )
                """,
                (now, now),
            )

    def tearDown(self) -> None:
        self.connection.close()
        self.temp_dir.cleanup()

    def test_existing_decisions_reapply_authoritative_state(self) -> None:
        decisions = Path(self.temp_dir.name) / "decisions.csv"
        decisions.write_text(
            "target_type,target_id,decision,rationale,reviewer,decision_version\n"
            "candidate_match,candidate-1,rejected,Wrong person,Unit test,test-v1\n"
            "research_status,person-1,in_progress,Continue research,Unit test,test-v1\n",
            encoding="utf-8",
        )
        first = import_review_decisions(self.connection, decisions)
        self.assertEqual(first["decisions_imported"], 2)
        with self.connection:
            self.connection.execute(
                """
                UPDATE candidate_matches
                SET match_assessment = 'unreviewed', rejection_reason = NULL
                WHERE candidate_match_id = 'candidate-1'
                """
            )
            self.connection.execute(
                """
                UPDATE person_entities
                SET research_status = 'candidate_found', next_action = NULL
                WHERE person_id = 'person-1'
                """
            )
            self.connection.execute(
                """
                UPDATE research_queue
                SET research_status = 'candidate_found', next_action = NULL
                WHERE person_id = 'person-1'
                """
            )

        second = import_review_decisions(self.connection, decisions)

        self.assertEqual(second["decisions_imported"], 0)
        self.assertEqual(second["duplicates_skipped"], 2)
        self.assertEqual(second["state_changes_applied"], 2)
        candidate = self.connection.execute(
            """
            SELECT match_assessment, rejection_reason FROM candidate_matches
            WHERE candidate_match_id = 'candidate-1'
            """
        ).fetchone()
        self.assertEqual(candidate["match_assessment"], "rejected")
        self.assertEqual(candidate["rejection_reason"], "Wrong person")
        person = self.connection.execute(
            """
            SELECT research_status, next_action FROM person_entities
            WHERE person_id = 'person-1'
            """
        ).fetchone()
        self.assertEqual(person["research_status"], "in_progress")
        self.assertEqual(person["next_action"], "Continue research")

    def test_entity_merge_preserves_rows_and_excludes_superseded_from_coverage(self) -> None:
        decisions = Path(self.temp_dir.name) / "entity_decisions.csv"
        decisions.write_text(
            "target_type,target_id,decision,rationale,reviewer,decision_version\n"
            "person_entity,person-2,merge_into:person-1,Exact private identifier matches,Unit test,test-v1\n",
            encoding="utf-8",
        )

        first = import_review_decisions(self.connection, decisions)
        second = import_review_decisions(self.connection, decisions)

        self.assertEqual(first["decisions_imported"], 1)
        self.assertEqual(first["state_changes_applied"], 1)
        self.assertEqual(second["duplicates_skipped"], 1)
        links = self.connection.execute(
            "SELECT person_id, COUNT(*) AS count FROM person_source_links GROUP BY person_id"
        ).fetchall()
        self.assertEqual([(row["person_id"], row["count"]) for row in links], [("person-1", 2)])
        supersession = self.connection.execute(
            "SELECT canonical_person_id FROM entity_supersessions WHERE superseded_person_id='person-2'"
        ).fetchone()
        self.assertEqual(supersession["canonical_person_id"], "person-1")
        self.assertIsNone(
            self.connection.execute(
                "SELECT 1 FROM research_queue WHERE person_id='person-2'"
            ).fetchone()
        )
        canonical = self.connection.execute(
            """
            SELECT name_variants_json, archive_box, archive_location,
                   personnel_category, possible_duplicate_group
            FROM person_entities WHERE person_id='person-1'
            """
        ).fetchone()
        self.assertIn("Example Alias", canonical["name_variants_json"])
        self.assertEqual(canonical["archive_box"], "20")
        self.assertEqual(canonical["archive_location"], "shelf-b")
        self.assertEqual(canonical["personnel_category"], "enlisted_army_personnel")
        self.assertIsNone(canonical["possible_duplicate_group"])
        with patch("oss_research.exports.REPORTS_DIR", Path(self.temp_dir.name)):
            report = coverage_report(self.connection)
        self.assertEqual(report["research_attempt_coverage"]["person_entities"], 1)
