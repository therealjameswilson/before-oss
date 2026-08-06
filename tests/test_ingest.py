from __future__ import annotations

import unittest

from oss_research.ingest import (
    Word,
    _normalization_name_middle_and_rank,
    _normalization_rank_and_serial,
    _parse_bbox_row,
)


class BboxParserTests(unittest.TestCase):
    def test_complete_row_columns(self) -> None:
        words = [
            Word("Adrian", 72.8, 290.7),
            Word("Leonard", 141.1, 290.7),
            Word("Sgt", 239.4, 290.7),
            Word("4", 361.1, 290.7),
            Word("Polish", 368.4, 290.7),
            Word("Ar", 398.4, 290.7),
            Word("230/86/26/03", 410.4, 290.7),
        ]
        fields, warnings = _parse_bbox_row(words)
        self.assertEqual(fields["last_name_raw"], "Adrian")
        self.assertEqual(fields["first_name_raw"], "Leonard")
        self.assertEqual(fields["rank_raw"], "Sgt")
        self.assertEqual(fields["box_raw"], "4")
        self.assertEqual(fields["notes_raw"], "Polish Ar")
        self.assertEqual(fields["archive_location_raw"], "230/86/26/03")
        self.assertEqual(warnings, [])

    def test_missing_first_name_is_preserved_without_column_shift(self) -> None:
        words = [
            Word("Testi", 72.8, 100.0),
            Word("*", 141.1, 100.0),
            Word("770", 349.9, 100.0),
            Word("review", 368.4, 100.0),
            Word("230/86/41/07", 410.4, 100.0),
        ]
        fields, warnings = _parse_bbox_row(words)
        self.assertEqual(fields["first_name_raw"], "*")
        self.assertEqual(fields["notes_raw"], "review")
        self.assertEqual(warnings, [])

    def test_nonnumeric_box_is_flagged(self) -> None:
        words = [
            Word("Example", 72.8, 100.0),
            Word("Person", 141.1, 100.0),
            Word("ABC", 349.9, 100.0),
            Word("230/86/41/07", 410.4, 100.0),
        ]
        _, warnings = _parse_bbox_row(words)
        self.assertIn("nonnumeric_box", warnings)

    def test_civilian_grade_printed_in_middle_column_is_normalized_separately(
        self,
    ) -> None:
        words = [
            Word("Adelson", 72.8, 100.0),
            Word("Sonia", 141.1, 100.0),
            Word("P-2", 210.0, 100.0),
            Word("4", 361.1, 100.0),
            Word("230/86/26/03", 410.4, 100.0),
        ]
        fields, warnings = _parse_bbox_row(words)
        middle, rank, note = _normalization_name_middle_and_rank(fields)
        self.assertEqual(fields["middle_initial_raw"], "P-2")
        self.assertIsNone(fields["rank_raw"])
        self.assertIsNone(middle)
        self.assertEqual(rank, "P-2")
        self.assertIn("raw cells are preserved", note or "")
        self.assertIn("civilian_grade_printed_in_middle_column", warnings)

    def test_military_rank_printed_in_middle_column_is_normalized_separately(
        self,
    ) -> None:
        words = [
            Word("Allen", 72.8, 100.0),
            Word("Keith", 141.1, 100.0),
            Word("Col", 210.0, 100.0),
            Word("10", 361.1, 100.0),
            Word("230/86/26/04", 410.4, 100.0),
        ]
        fields, warnings = _parse_bbox_row(words)
        middle, rank, note = _normalization_name_middle_and_rank(fields)
        self.assertEqual(fields["middle_initial_raw"], "Col")
        self.assertIsNone(fields["rank_raw"])
        self.assertIsNone(middle)
        self.assertEqual(rank, "Col")
        self.assertIn("raw cells are preserved", note or "")
        self.assertIn("military_rank_printed_in_middle_column", warnings)

    def test_numeric_identifier_printed_in_rank_column_is_normalized_separately(
        self,
    ) -> None:
        words = [
            Word("Berg", 72.8, 100.0),
            Word("John,", 141.1, 100.0),
            Word("III", 174.0, 100.0),
            Word("W", 210.0, 100.0),
            Word("4302568", 239.4, 100.0),
            Word("51", 361.1, 100.0),
            Word("230/86/27/03", 410.4, 100.0),
        ]
        fields, warnings = _parse_bbox_row(words)
        _, classification_rank, _ = _normalization_name_middle_and_rank(fields)
        rank, serial, note = _normalization_rank_and_serial(
            fields, classification_rank
        )
        self.assertEqual(fields["rank_raw"], "4302568")
        self.assertIsNone(fields["serial_number_raw"])
        self.assertIsNone(rank)
        self.assertEqual(serial, "4302568")
        self.assertIn("raw cells are preserved", note or "")
        self.assertIn("serial_number_printed_in_rank_column", warnings)


if __name__ == "__main__":
    unittest.main()
