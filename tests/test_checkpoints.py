from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from oss_research.checkpoints import (
    ATTEMPT_COLUMNS,
    CANDIDATE_COLUMNS,
    PERSON_UPDATE_COLUMNS,
    export_adapter_checkpoints,
    import_adapter_checkpoints,
)
from oss_research.db import connect, migrate


class AdapterCheckpointTests(unittest.TestCase):
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
                    '[]', 'unknown_or_indeterminate', 1, 1, 'not_started',
                    0, 1, 0, 'unassessed', ?, ?
                )
                """,
                (now, now),
            )
            self.connection.execute(
                """
                INSERT INTO research_queue(
                    person_id, difficulty_tier, priority, research_status,
                    attempts, protocol_version, updated_at
                ) VALUES ('person-1', 1, 10, 'not_started', 0, 'test-v1', ?)
                """,
                (now,),
            )

    def tearDown(self) -> None:
        self.connection.close()
        self.temp_dir.cleanup()

    def test_checkpoint_replays_sanitized_state_idempotently(self) -> None:
        payload = {
            "checkpoint_version": "1.0",
            "description": "Unit-test checkpoint without query text.",
            "attempt_columns": ATTEMPT_COLUMNS,
            "attempts": [
                [
                    "attempt-1",
                    "person-1",
                    "loc",
                    "employment",
                    "fingerprint-1",
                    "2026-07-30T00:00:00+00:00",
                    "2026-07-30T00:01:00+00:00",
                    "candidate_found",
                    0,
                    0,
                    1,
                    "before-oss/test",
                ]
            ],
            "person_update_columns": PERSON_UPDATE_COLUMNS,
            "person_updates": [
                [
                    "person-1",
                    "candidate_found",
                    "Review the discovery candidate.",
                ]
            ],
            "candidate_columns": CANDIDATE_COLUMNS,
            "candidates": [
                [
                    "candidate-1",
                    "person-1",
                    "source",
                    "Example candidate",
                    "https://example.test/candidate",
                    "example-id",
                    json.dumps({"project_note": "Discovery metadata only."}),
                    "2026-07-30T00:00:00+00:00",
                    "2026-07-30T00:00:00+00:00",
                ]
            ],
        }
        path = Path(self.temp_dir.name) / "checkpoint.json"
        path.write_text(json.dumps(payload), encoding="utf-8")

        first = import_adapter_checkpoints(self.connection, path)
        self.assertEqual(
            first,
            {
                "research_attempts": 1,
                "person_updates": 1,
                "candidate_matches": 1,
            },
        )
        with self.connection:
            self.connection.execute(
                """
                UPDATE research_attempts
                SET query_text = 'private local query',
                    research_notes = 'private local note'
                WHERE research_attempt_id = 'attempt-1'
                """
            )
            self.connection.execute(
                """
                UPDATE candidate_matches
                SET match_assessment = 'rejected',
                    rejection_reason = 'Reviewed and rejected.'
                WHERE candidate_match_id = 'candidate-1'
                """
            )

        second = import_adapter_checkpoints(self.connection, path)

        self.assertEqual(first, second)
        attempt = self.connection.execute(
            """
            SELECT query_text, research_notes FROM research_attempts
            WHERE research_attempt_id = 'attempt-1'
            """
        ).fetchone()
        self.assertEqual(attempt["query_text"], "private local query")
        self.assertEqual(attempt["research_notes"], "private local note")
        candidate = self.connection.execute(
            """
            SELECT match_assessment, rejection_reason FROM candidate_matches
            WHERE candidate_match_id = 'candidate-1'
            """
        ).fetchone()
        self.assertEqual(candidate["match_assessment"], "rejected")
        self.assertEqual(candidate["rejection_reason"], "Reviewed and rejected.")
        person = self.connection.execute(
            """
            SELECT research_status, research_attempt_number
            FROM person_entities WHERE person_id = 'person-1'
            """
        ).fetchone()
        self.assertEqual(person["research_status"], "candidate_found")
        self.assertEqual(person["research_attempt_number"], 1)

    def test_checkpoint_export_is_deterministic_and_sanitized(self) -> None:
        now = "2026-07-30T00:00:00+00:00"
        with self.connection:
            self.connection.execute(
                """
                INSERT INTO research_attempts(
                    research_attempt_id, person_id, source_adapter, query_text,
                    query_variant_type, request_fingerprint, started_at,
                    completed_at, outcome, sources_reviewed,
                    candidate_sources_rejected, research_notes, attempt_number,
                    research_agent_version
                ) VALUES (
                    'attempt-1', 'person-1', 'loc', 'private search terms',
                    'employment', 'fingerprint-1', ?, ?, 'candidate_found',
                    1, 0, 'private local note', 1, 'before-oss/test'
                )
                """,
                (now, now),
            )
            self.connection.execute(
                """
                INSERT INTO candidate_matches(
                    candidate_match_id, person_id, candidate_type,
                    candidate_label, candidate_url, candidate_identifier,
                    evidence_json, match_assessment, rejection_reason,
                    created_at, updated_at
                ) VALUES (
                    'candidate-1', 'person-1', 'source', 'Example candidate',
                    'https://example.test/item', NULL, ?, 'rejected',
                    'Wrong namesake.', ?, ?
                )
                """,
                (
                    json.dumps(
                        {
                            "project_note": "Discovery metadata only.",
                            "request_fingerprint": "fingerprint-1",
                        }
                    ),
                    now,
                    now,
                ),
            )
            self.connection.execute(
                """
                INSERT INTO research_attempts(
                    research_attempt_id, person_id, source_adapter, query_text,
                    query_variant_type, request_fingerprint, started_at,
                    completed_at, outcome, sources_reviewed,
                    candidate_sources_rejected, attempt_number,
                    research_agent_version
                ) VALUES (
                    'reviewed-attempt', 'person-1', 'reviewed_web',
                    'reviewed evidence query', 'reviewed',
                    'reviewed-fingerprint', ?, ?, 'source_reviewed',
                    1, 0, 2, 'before-oss/test'
                )
                """,
                (now, now),
            )
            self.connection.execute(
                """
                UPDATE person_entities
                SET research_status = 'candidate_found',
                    next_action = 'Review the candidate.'
                WHERE person_id = 'person-1'
                """
            )

        first_path = Path(self.temp_dir.name) / "checkpoint-1.json"
        second_path = Path(self.temp_dir.name) / "checkpoint-2.json"
        first = export_adapter_checkpoints(self.connection, first_path)
        second = export_adapter_checkpoints(self.connection, second_path)

        self.assertEqual(first, second)
        self.assertEqual(first_path.read_bytes(), second_path.read_bytes())
        text = first_path.read_text(encoding="utf-8")
        self.assertNotIn("private search terms", text)
        self.assertNotIn("private local note", text)
        self.assertNotIn("Wrong namesake", text)
        payload = json.loads(text)
        self.assertEqual(len(payload["attempts"]), 1)
        self.assertEqual(payload["attempts"][0][0], "attempt-1")
        self.assertEqual(payload["candidates"][0][0], "candidate-1")
        self.assertEqual(payload["person_updates"][0][0], "person-1")
