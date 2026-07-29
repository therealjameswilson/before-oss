from __future__ import annotations

import unittest

from oss_research.ingest import Word, _parse_bbox_row


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


if __name__ == "__main__":
    unittest.main()
