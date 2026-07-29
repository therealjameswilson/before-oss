from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from oss_research.public import (
    _write_json,
    mask_serial,
    public_source_row,
    verified_affiliation_person_count,
    verified_employer_person_count,
)


class FakeRow(dict):
    def __getitem__(self, key: str) -> object:
        return super().__getitem__(key)


class PublicProjectionTests(unittest.TestCase):
    def test_json_gzip_is_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "example.json"
            _write_json(path, {"example": "value"})
            first = path.with_suffix(".json.gz").read_bytes()
            _write_json(path, {"example": "value"})
            second = path.with_suffix(".json.gz").read_bytes()
            self.assertEqual(first, second)
            self.assertEqual(first[4:8], b"\x00\x00\x00\x00")

    def test_masks_service_number(self) -> None:
        self.assertEqual(mask_serial("RA3389449"), "••••9449")
        self.assertIsNone(mask_serial(None))

    def test_source_projection_excludes_raw_serial_and_raw_line(self) -> None:
        row = FakeRow(
            source_record_id="row-1",
            last_name_raw="Example",
            first_name_raw="Jane",
            middle_initial_raw="A",
            rank_raw="Capt",
            serial_number_normalized="12345678",
            box_raw="1",
            notes_raw=None,
            archive_location="230/86/26/03",
            source_page=1,
            raw_row_text="Example Jane A Capt 12345678",
        )
        public = public_source_row(row)
        self.assertEqual(public["serial_masked"], "••••5678")
        self.assertNotIn("serial_number_normalized", public)
        self.assertNotIn("raw_row_text", public)
        self.assertNotIn("12345678", str(public))

    def test_medium_affiliation_does_not_count_as_verified(self) -> None:
        profiles = [
            {
                "immediate_pre_oss_affiliations": [
                    {
                        "claim_confidence": "medium",
                        "publication_status": "publish_qualified",
                        "relationship_type": "student",
                    }
                ],
                "last_civilian_pre_service": [],
                "other_pre_oss_affiliations": [],
            },
            {
                "immediate_pre_oss_affiliations": [],
                "last_civilian_pre_service": [
                    {
                        "claim_confidence": "high",
                        "publication_status": "publish_qualified",
                        "relationship_type": "military_assignment",
                    }
                ],
                "other_pre_oss_affiliations": [],
            },
        ]
        self.assertEqual(verified_affiliation_person_count(profiles), 1)

    def test_nonemployment_affiliation_does_not_count_as_verified_employer(
        self,
    ) -> None:
        profiles = [
            {
                "immediate_pre_oss_affiliations": [
                    {
                        "claim_confidence": "high",
                        "publication_status": "published",
                        "relationship_type": "student",
                    }
                ],
                "last_civilian_pre_service": [],
                "other_pre_oss_affiliations": [],
            },
            {
                "immediate_pre_oss_affiliations": [],
                "last_civilian_pre_service": [
                    {
                        "claim_confidence": "confirmed",
                        "publication_status": "published",
                        "relationship_type": "employment",
                    }
                ],
                "other_pre_oss_affiliations": [],
            },
            {
                "immediate_pre_oss_affiliations": [],
                "last_civilian_pre_service": [],
                "other_pre_oss_affiliations": [
                    {
                        "claim_confidence": "high",
                        "publication_status": "publish_qualified",
                        "relationship_type": "self_employment",
                    }
                ],
            },
        ]
        self.assertEqual(verified_affiliation_person_count(profiles), 3)
        self.assertEqual(verified_employer_person_count(profiles), 2)


if __name__ == "__main__":
    unittest.main()
