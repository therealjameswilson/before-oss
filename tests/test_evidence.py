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
                    "identity_status": "confirmed",
                    "identity_evidence": "Exact full name and archival context.",
                    "name_variants": ["Example A. Person"],
                    "personnel_category": "civilian_professional_or_administrative_grade",
                    "commissioned_officer": False,
                    "allied_or_foreign_personnel": False,
                    "manual_review_required": False,
                    "possible_duplicate_group": "test-duplicate-group",
                    "research_status": "verified_employer_found",
                    "next_action": "No additional action is currently required.",
                    "personnel_file_digitized": True,
                    "personnel_file_reviewed": True,
                    "nara_catalog_id": "12345",
                    "archival_review_priority": "not_required",
                }
            ],
            "research_attempts": [
                {
                    "key": "attempt-1",
                    "person_id": "person-1",
                    "source_adapter": "reviewed_archive",
                    "query_text": "https://example.test/source",
                    "query_variant_type": "direct_archival_file_review",
                    "started_at": "2026-07-29T00:00:00+00:00",
                    "completed_at": "2026-07-29T01:00:00+00:00",
                    "outcome": "source_reviewed",
                    "sources_reviewed": 1,
                    "research_notes": "The complete file was reviewed.",
                    "next_action": "No additional action is currently required.",
                    "attempt_number": 1,
                    "research_agent_version": "before-oss/test",
                }
            ],
        }

    def test_import_is_idempotent(self) -> None:
        path = Path(self.temp_dir.name) / "bundle.json"
        path.write_text(json.dumps(self._bundle()), encoding="utf-8")
        first = import_reviewed_evidence(self.connection, path)
        first_completed_at = self.connection.execute(
            "SELECT research_completed_at FROM person_entities"
        ).fetchone()[0]
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
        self.assertEqual(
            self.connection.execute(
                "SELECT COUNT(*) FROM research_attempts"
            ).fetchone()[0],
            1,
        )
        attempt = self.connection.execute(
            """
            SELECT outcome, sources_reviewed, request_fingerprint
            FROM research_attempts
            """
        ).fetchone()
        self.assertEqual(attempt["outcome"], "source_reviewed")
        self.assertEqual(attempt["sources_reviewed"], 1)
        self.assertTrue(attempt["request_fingerprint"])
        person = self.connection.execute(
            """
            SELECT identity_status, identity_evidence, name_variants_json,
                   personnel_category, commissioned_officer,
                   allied_or_foreign_personnel, manual_review_required,
                   possible_duplicate_group,
                   research_status, research_started_at, research_completed_at,
                   personnel_file_digitized, personnel_file_reviewed,
                   nara_catalog_id, archival_review_priority
            FROM person_entities
            """
        ).fetchone()
        self.assertEqual(person["identity_status"], "confirmed")
        self.assertEqual(
            json.loads(person["name_variants_json"]),
            ["Example A. Person"],
        )
        self.assertEqual(
            person["personnel_category"],
            "civilian_professional_or_administrative_grade",
        )
        self.assertEqual(person["commissioned_officer"], 0)
        self.assertEqual(person["allied_or_foreign_personnel"], 0)
        self.assertEqual(person["manual_review_required"], 0)
        self.assertEqual(
            person["possible_duplicate_group"],
            "test-duplicate-group",
        )
        self.assertEqual(person["research_status"], "verified_employer_found")
        self.assertIsNotNone(person["research_started_at"])
        self.assertIsNotNone(person["research_completed_at"])
        self.assertEqual(person["research_completed_at"], first_completed_at)
        self.assertEqual(person["personnel_file_digitized"], 1)
        self.assertEqual(person["personnel_file_reviewed"], 1)
        self.assertEqual(person["nara_catalog_id"], "12345")
        self.assertEqual(person["archival_review_priority"], "not_required")
        self.assertEqual(
            self.connection.execute(
                "SELECT research_attempt_number FROM person_entities"
            ).fetchone()[0],
            1,
        )
        self.assertEqual(
            self.connection.execute(
                "SELECT attempts FROM research_queue"
            ).fetchone()[0],
            1,
        )

        link = self.connection.execute(
            "SELECT link_status, evidence, manual_review_required FROM person_source_links"
        ).fetchone()
        # This unit fixture does not create a person/source link, so no link is
        # expected; the assertion protects the import from inventing one.
        self.assertIsNone(link)

    def test_sanitized_attempt_checkpoint_preserves_richer_local_fields(self) -> None:
        attempt_id = "checkpoint-attempt-id"
        fingerprint = "checkpoint-fingerprint"
        self.connection.execute(
            """
            INSERT INTO research_attempts(
                research_attempt_id, person_id, source_adapter, query_text,
                query_variant_type, request_fingerprint, started_at,
                completed_at, outcome, sources_reviewed,
                candidate_sources_rejected, research_notes, attempt_number,
                research_agent_version
            ) VALUES (?, 'person-1', 'loc', 'private local query',
                      'employment', ?, '2026-07-29T00:00:00+00:00',
                      '2026-07-29T00:01:00+00:00', 'no_result', 0, 0,
                      'Private local audit detail.', 1, 'before-oss/test')
            """,
            (attempt_id, fingerprint),
        )
        bundle = self._bundle()
        bundle["research_attempts"] = [
            {
                "key": "sanitized-checkpoint",
                "research_attempt_id": attempt_id,
                "person_id": "person-1",
                "source_adapter": "loc",
                "query_variant_type": "employment",
                "request_fingerprint": fingerprint,
                "started_at": "2026-07-29T00:00:00+00:00",
                "completed_at": "2026-07-29T00:01:00+00:00",
                "outcome": "no_result",
                "attempt_number": 1,
                "research_agent_version": "before-oss/test",
            }
        ]
        path = Path(self.temp_dir.name) / "checkpoint.json"
        path.write_text(json.dumps(bundle), encoding="utf-8")

        import_reviewed_evidence(self.connection, path)

        attempt = self.connection.execute(
            """
            SELECT research_attempt_id, request_fingerprint, query_text,
                   research_notes
            FROM research_attempts
            """
        ).fetchone()
        self.assertEqual(attempt["research_attempt_id"], attempt_id)
        self.assertEqual(attempt["request_fingerprint"], fingerprint)
        self.assertEqual(attempt["query_text"], "private local query")
        self.assertEqual(attempt["research_notes"], "Private local audit detail.")

    def test_name_variant_order_has_a_deterministic_case_tiebreaker(self) -> None:
        bundle = self._bundle()
        bundle["person_updates"][0]["name_variants"] = [
            "Dewitt Clinton Poole",
            "DeWitt Clinton Poole",
        ]
        path = Path(self.temp_dir.name) / "variant-order-bundle.json"
        path.write_text(json.dumps(bundle), encoding="utf-8")

        import_reviewed_evidence(self.connection, path)

        variants = json.loads(
            self.connection.execute(
                "SELECT name_variants_json FROM person_entities"
            ).fetchone()[0]
        )
        self.assertEqual(
            variants,
            ["DeWitt Clinton Poole", "Dewitt Clinton Poole"],
        )

    def test_name_variants_can_replace_rejected_namesake_aliases(self) -> None:
        original = self._bundle()
        original["person_updates"][0]["name_variants"] = [
            "Example A. Person",
            "Rejected Namesake",
        ]
        original_path = Path(self.temp_dir.name) / "variant-original-bundle.json"
        original_path.write_text(json.dumps(original), encoding="utf-8")
        import_reviewed_evidence(self.connection, original_path)

        correction = self._bundle()
        correction["person_updates"][0]["name_variants"] = [
            "Example A. Person",
            "Example Person",
        ]
        correction["person_updates"][0]["replace_name_variants"] = True
        correction_path = Path(self.temp_dir.name) / "variant-correction-bundle.json"
        correction_path.write_text(json.dumps(correction), encoding="utf-8")
        import_reviewed_evidence(self.connection, correction_path)

        variants = json.loads(
            self.connection.execute(
                "SELECT name_variants_json FROM person_entities"
            ).fetchone()[0]
        )
        self.assertEqual(
            variants,
            ["Example A. Person", "Example Person"],
        )

    def test_nara_catalog_id_omission_preserves_and_null_clears(self) -> None:
        original_path = Path(self.temp_dir.name) / "catalog-id-original.json"
        original_path.write_text(json.dumps(self._bundle()), encoding="utf-8")
        import_reviewed_evidence(self.connection, original_path)
        self.assertEqual(
            self.connection.execute(
                "SELECT nara_catalog_id FROM person_entities"
            ).fetchone()[0],
            "12345",
        )

        omitted_bundle = self._bundle()
        del omitted_bundle["person_updates"][0]["nara_catalog_id"]
        omitted_path = Path(self.temp_dir.name) / "catalog-id-omitted.json"
        omitted_path.write_text(json.dumps(omitted_bundle), encoding="utf-8")
        import_reviewed_evidence(self.connection, omitted_path)
        self.assertEqual(
            self.connection.execute(
                "SELECT nara_catalog_id FROM person_entities"
            ).fetchone()[0],
            "12345",
        )

        cleared_bundle = self._bundle()
        cleared_bundle["person_updates"][0]["nara_catalog_id"] = None
        cleared_path = Path(self.temp_dir.name) / "catalog-id-cleared.json"
        cleared_path.write_text(json.dumps(cleared_bundle), encoding="utf-8")
        import_reviewed_evidence(self.connection, cleared_path)
        self.assertIsNone(
            self.connection.execute(
                "SELECT nara_catalog_id FROM person_entities"
            ).fetchone()[0]
        )

    def test_review_can_correct_generic_rank_to_marine_corps_officer(self) -> None:
        bundle = self._bundle()
        bundle["person_updates"][0]["personnel_category"] = (
            "commissioned_marine_corps_officer"
        )
        bundle["person_updates"][0]["commissioned_officer"] = True
        path = Path(self.temp_dir.name) / "marine-officer-bundle.json"
        path.write_text(json.dumps(bundle), encoding="utf-8")

        import_reviewed_evidence(self.connection, path)

        person = self.connection.execute(
            """
            SELECT personnel_category, commissioned_officer
            FROM person_entities
            WHERE person_id = 'person-1'
            """
        ).fetchone()
        self.assertEqual(
            person["personnel_category"],
            "commissioned_marine_corps_officer",
        )
        self.assertEqual(person["commissioned_officer"], 1)

    def test_review_can_correct_generic_rank_to_enlisted_marine(self) -> None:
        bundle = self._bundle()
        bundle["person_updates"][0]["personnel_category"] = (
            "enlisted_marine_corps_personnel"
        )
        bundle["person_updates"][0]["commissioned_officer"] = False
        path = Path(self.temp_dir.name) / "enlisted-marine-bundle.json"
        path.write_text(json.dumps(bundle), encoding="utf-8")

        import_reviewed_evidence(self.connection, path)

        person = self.connection.execute(
            """
            SELECT personnel_category, commissioned_officer
            FROM person_entities
            WHERE person_id = 'person-1'
            """
        ).fetchone()
        self.assertEqual(
            person["personnel_category"],
            "enlisted_marine_corps_personnel",
        )
        self.assertEqual(person["commissioned_officer"], 0)

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
