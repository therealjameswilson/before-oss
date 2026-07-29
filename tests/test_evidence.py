from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from pydantic import ValidationError

from oss_research.db import connect, migrate
from oss_research.evidence import EvidenceBundle, import_reviewed_evidence


class ReviewedEvidenceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.database = Path(self.temp_dir.name) / "test.sqlite"
        self.connection = connect(self.database)
        migrate(self.connection)
        now = "2026-07-29T00:00:00+00:00"
        with self.connection:
            self.connection.execute(
                """
                INSERT INTO person_entities(
                    person_id, display_name, normalized_name, identity_status,
                    identity_evidence, name_variants_json, personnel_category,
                    commissioned_officer, allied_or_foreign_personnel,
                    difficulty_tier, manual_review_required, research_status,
                    research_attempt_number, personnel_file_indexed,
                    personnel_file_reviewed, archival_review_priority,
                    created_at, updated_at
                ) VALUES (
                    'person-1', 'Example Person', 'EXAMPLE PERSON', 'unresolved',
                    NULL, '[]', 'unknown_or_indeterminate', NULL, NULL,
                    1, 1, 'in_progress', 1, 1, 0, 'unassessed', ?, ?
                )
                """,
                (now, now),
            )
            self.connection.execute(
                """
                INSERT INTO research_queue(
                    person_id, difficulty_tier, priority, research_status,
                    attempts, protocol_version, updated_at
                ) VALUES ('person-1', 1, 10, 'in_progress', 1, 'test-v1', ?)
                """,
                (now,),
            )

    def tearDown(self) -> None:
        self.connection.close()
        self.temp_dir.cleanup()

    def _bundle(self) -> dict[str, object]:
        return {
            "bundle_version": "test-v1",
            "reviewer": "Unit test",
            "sources": [
                {
                    "key": "source-1",
                    "stable_url": "https://example.test/source",
                    "title": "Example source",
                    "repository_publisher": "Example archive",
                    "access_date": "2026-07-29",
                    "source_quality": "B_authoritative_institutional",
                }
            ],
            "organizations": [
                {
                    "key": "organization-1",
                    "canonical_name": "Example Organization",
                    "sector": "federal_government",
                }
            ],
            "affiliations": [
                {
                    "key": "affiliation-1",
                    "person_id": "person-1",
                    "organization_key": "organization-1",
                    "organization_name_as_found": "Example Organization",
                    "relationship_type": "government_assignment",
                    "immediate_pre_oss": True,
                    "pre_oss_temporal_basis": "explicit_immediate",
                    "identity_confidence": "high_confidence",
                    "claim_confidence": "high",
                    "source_quality": "B_authoritative_institutional",
                    "publication_status": "publish_qualified",
                }
            ],
            "claims": [
                {
                    "key": "claim-1",
                    "person_id": "person-1",
                    "affiliation_key": "affiliation-1",
                    "claim_type": "immediate_pre_oss_affiliation",
                    "claim_text": "Example Person transferred from Example Organization.",
                    "evidence_excerpt": "Transferred from Example Organization.",
                    "evidence_paraphrase": "The source explicitly documents the transfer.",
                    "identity_match_assessment": "Exact full name and archival context.",
                    "temporal_assessment": "Explicitly immediate.",
                    "source_quality": "B_authoritative_institutional",
                    "claim_confidence": "high",
                    "publication_status": "publish_qualified",
                    "match_notes": "Reviewed against the indexed record.",
                    "sources": [{"source_key": "source-1"}],
                }
            ],
            "person_updates": [
                {
                    "person_id": "person-1",
                    "identity_status": "high_confidence",
                    "identity_evidence": "Exact full name and archival context.",
                    "research_status": "verified_employer_found",
                    "next_action": "Continue review for earlier affiliations.",
                }
            ],
        }

    def test_import_is_idempotent(self) -> None:
        path = Path(self.temp_dir.name) / "bundle.json"
        path.write_text(json.dumps(self._bundle()), encoding="utf-8")
        first = import_reviewed_evidence(self.connection, path)
        second = import_reviewed_evidence(self.connection, path)
        self.assertEqual(first, second)
        self.assertEqual(
            self.connection.execute("SELECT COUNT(*) FROM sources").fetchone()[0],
            1,
        )
        self.assertEqual(
            self.connection.execute("SELECT COUNT(*) FROM affiliations").fetchone()[0],
            1,
        )
        self.assertEqual(
            self.connection.execute("SELECT COUNT(*) FROM claims").fetchone()[0],
            1,
        )
        person = self.connection.execute(
            "SELECT identity_status, research_status FROM person_entities"
        ).fetchone()
        self.assertEqual(person["identity_status"], "high_confidence")
        self.assertEqual(person["research_status"], "verified_employer_found")

    def test_public_claim_requires_source(self) -> None:
        bundle = self._bundle()
        bundle["claims"][0]["sources"] = []
        with self.assertRaises(ValidationError):
            EvidenceBundle.model_validate(bundle)

    def test_excerpt_limit_is_enforced(self) -> None:
        bundle = self._bundle()
        bundle["claims"][0]["evidence_excerpt"] = "word " * 26
        with self.assertRaises(ValidationError):
            EvidenceBundle.model_validate(bundle)


if __name__ == "__main__":
    unittest.main()
