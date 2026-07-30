from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from oss_research.db import connect, migrate
from oss_research.page_reviews import import_page_reviews


class PageReviewTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.database = Path(self.temp_dir.name) / "test.sqlite"
        self.connection = connect(self.database)
        migrate(self.connection)
        self.pdf_hash = "a" * 64
        now = "2026-07-30T00:00:00Z"
        with self.connection:
            for page in (1, 2):
                self.connection.execute(
                    """
                    INSERT INTO page_qa(
                        source_pdf_sha256, source_page, extracted_row_count,
                        warning_count, anomaly_flags_json, selection_reason
                    ) VALUES (?, ?, 1, ?, ?, 'test_selection')
                    """,
                    (
                        self.pdf_hash,
                        page,
                        1 if page == 2 else 0,
                        '["civilian_grade_printed_in_middle_column"]'
                        if page == 2
                        else "[]",
                    ),
                )
                self.connection.execute(
                    """
                    INSERT INTO source_records(
                        source_record_id, source_pdf, source_pdf_sha256,
                        source_page, source_row_number, raw_row_text,
                        last_name_raw, first_name_raw, middle_initial_raw,
                        rank_raw, archive_location_raw, display_name,
                        normalized_name, last_name, first_name,
                        middle_name_or_initial, rank_normalized, box_number,
                        archive_location, personnel_category,
                        commissioned_officer, allied_or_foreign_personnel,
                        name_variants_json, parser_confidence,
                        requires_visual_review, ingested_at, parser_version
                    ) VALUES (
                        ?, 'test.pdf', ?, ?, 1, ?, ?, ?, ?, NULL,
                        '230/86/26/03', ?, ?, ?, ?, ?, ?, 4,
                        '230/86/26/03', ?, 0, 0, '[]', ?, ?, ?, 'test-v1'
                    )
                    """,
                    (
                        f"record-{page}",
                        self.pdf_hash,
                        page,
                        "MATCH Jane J Lt 4 230/86/26/03"
                        if page == 1
                        else "SHIFT Sonia P-2 4 230/86/26/03",
                        "Match" if page == 1 else "Shift",
                        "Jane" if page == 1 else "Sonia",
                        "J" if page == 1 else "P-2",
                        "Jane J Match" if page == 1 else "Sonia Shift",
                        "JANE J MATCH" if page == 1 else "SONIA SHIFT",
                        "Match" if page == 1 else "Shift",
                        "Jane" if page == 1 else "Sonia",
                        "J" if page == 1 else None,
                        "Lt" if page == 1 else "P-2",
                        "commissioned_army_officer"
                        if page == 1
                        else "civilian_professional_or_administrative_grade",
                        0.88 if page == 2 else 1.0,
                        1 if page == 2 else 0,
                        now,
                    ),
                )

    def tearDown(self) -> None:
        self.connection.close()
        self.temp_dir.cleanup()

    def test_import_page_reviews_replays_page_and_row_decisions(self) -> None:
        review_file = Path(self.temp_dir.name) / "reviews.json"
        review_file.write_text(
            json.dumps(
                {
                    "bundle_version": "test-v1",
                    "source_pdf_sha256": self.pdf_hash,
                    "reviewer": "Unit test",
                    "matching_pages_reviewed_at": "2026-07-30T00:01:00Z",
                    "matching_pages_notes": "Matched the source.",
                    "reviewed_matching_pages": [1],
                    "corrections_reviewed_at": "2026-07-30T00:02:00Z",
                    "correction_rows": [
                        {
                            "source_page": 2,
                            "source_row_number": 1,
                            "expected_last_name_raw": "Shift",
                            "expected_first_name_raw": "Sonia",
                            "expected_middle_initial_raw": "P-2",
                            "expected_rank_raw": None,
                            "decision": "reviewed_corrected",
                            "notes": "Raw grade cell preserved.",
                        }
                    ],
                }
            ),
            encoding="utf-8",
        )

        result = import_page_reviews(self.connection, review_file)

        self.assertEqual(result["reviewed_pages"], 2)
        pages = list(
            self.connection.execute(
                """
                SELECT source_page, visual_review_status FROM page_qa
                ORDER BY source_page
                """
            )
        )
        self.assertEqual(
            [(row["source_page"], row["visual_review_status"]) for row in pages],
            [(1, "reviewed_matches"), (2, "reviewed_after_correction")],
        )
        rows = list(
            self.connection.execute(
                """
                SELECT source_page, visual_review_status FROM source_records
                ORDER BY source_page
                """
            )
        )
        self.assertEqual(
            [(row["source_page"], row["visual_review_status"]) for row in rows],
            [(1, "reviewed_matches"), (2, "reviewed_corrected")],
        )

    def test_import_page_reviews_rejects_changed_raw_cells(self) -> None:
        review_file = Path(self.temp_dir.name) / "reviews.json"
        review_file.write_text(
            json.dumps(
                {
                    "bundle_version": "test-v1",
                    "source_pdf_sha256": self.pdf_hash,
                    "reviewer": "Unit test",
                    "matching_pages_reviewed_at": "2026-07-30T00:01:00Z",
                    "matching_pages_notes": "Matched the source.",
                    "reviewed_matching_pages": [1],
                    "corrections_reviewed_at": "2026-07-30T00:02:00Z",
                    "correction_rows": [
                        {
                            "source_page": 2,
                            "source_row_number": 1,
                            "expected_last_name_raw": "Wrong",
                            "expected_first_name_raw": "Sonia",
                            "expected_middle_initial_raw": "P-2",
                            "expected_rank_raw": None,
                            "decision": "reviewed_corrected",
                            "notes": "Raw grade cell preserved.",
                        }
                    ],
                }
            ),
            encoding="utf-8",
        )

        with self.assertRaisesRegex(ValueError, "expected raw cells"):
            import_page_reviews(self.connection, review_file)
