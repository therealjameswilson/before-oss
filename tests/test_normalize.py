from __future__ import annotations

import unittest

from oss_research.normalize import (
    classify_personnel,
    normalize_name,
    normalize_serial,
)


class NormalizeTests(unittest.TestCase):
    def test_suffix_in_first_name_column(self) -> None:
        result = normalize_name("Young", "Gerald, Jr.", "S")
        self.assertEqual(result.display_name, "Gerald S Young Jr.")
        self.assertEqual(result.suffix, "Jr.")

    def test_suffix_in_last_name_column(self) -> None:
        result = normalize_name("Kruse, Jr.", "John", "H")
        self.assertEqual(result.display_name, "John H Kruse Jr.")
        self.assertEqual(result.last_name, "Kruse")

    def test_suffix_in_middle_column(self) -> None:
        result = normalize_name("Maxson", "Raymond", "J Jr")
        self.assertEqual(result.display_name, "Raymond J Maxson Jr.")
        self.assertEqual(result.middle, "J")

    def test_apostrophe_and_hyphen_are_searchable(self) -> None:
        result = normalize_name("O'Neil-Smith", "Anne-Marie", "E")
        self.assertEqual(result.normalized_name, "ANNE MARIE E O NEIL SMITH")

    def test_civilian_grade_is_not_an_officer(self) -> None:
        result = classify_personnel("Caf-11", None)
        self.assertEqual(
            result.category, "civilian_professional_or_administrative_grade"
        )
        self.assertFalse(result.commissioned_officer)

    def test_unknown_rank_stays_unknown(self) -> None:
        result = classify_personnel("WAE", None)
        self.assertEqual(result.category, "unknown_or_indeterminate")
        self.assertIsNone(result.commissioned_officer)
        self.assertIn("preserved", result.note or "")

    def test_foreign_note_does_not_silently_disappear(self) -> None:
        result = classify_personnel("S/Lt", "French")
        self.assertEqual(result.category, "foreign_or_allied_military_personnel")
        self.assertTrue(result.allied_or_foreign)

    def test_coast_guard_note_overrides_generic_lieutenant_category(self) -> None:
        result = classify_personnel("Lt", "Coast G")
        self.assertEqual(result.category, "commissioned_coast_guard_officer")
        self.assertTrue(result.commissioned_officer)
        self.assertFalse(result.allied_or_foreign)

    def test_usn_suffix_classifies_lieutenant_as_naval_officer(self) -> None:
        result = classify_personnel("LT USN", None)
        self.assertEqual(result.rank_normalized, "LT USN")
        self.assertEqual(result.category, "commissioned_naval_officer")
        self.assertTrue(result.commissioned_officer)
        self.assertIn("USN", result.note or "")

    def test_usnr_suffix_classifies_lieutenant_as_naval_officer(self) -> None:
        result = classify_personnel("Lt USNR", None)
        self.assertEqual(result.rank_normalized, "LT USNR")
        self.assertEqual(result.category, "commissioned_naval_officer")
        self.assertTrue(result.commissioned_officer)

    def test_spaced_seaman_second_class_variant_is_naval_enlisted(self) -> None:
        result = classify_personnel("S2 C", None)
        self.assertEqual(result.rank_normalized, "S 2/C")
        self.assertEqual(result.category, "enlisted_naval_personnel")
        self.assertFalse(result.commissioned_officer)

    def test_first_sergeant_is_army_enlisted(self) -> None:
        result = classify_personnel("1st Sgt", None)
        self.assertEqual(result.rank_normalized, "1ST SGT")
        self.assertEqual(result.category, "enlisted_army_personnel")
        self.assertFalse(result.commissioned_officer)

    def test_lieutenant_commander_variants_are_naval_officers(self) -> None:
        for printed_rank, normalized_rank in (
            ("Lt CMD", "LT CMD"),
            ("Lt Cmdr", "LT CMDR"),
        ):
            with self.subTest(printed_rank=printed_rank):
                result = classify_personnel(printed_rank, None)
                self.assertEqual(result.rank_normalized, normalized_rank)
                self.assertEqual(result.category, "commissioned_naval_officer")
                self.assertTrue(result.commissioned_officer)

    def test_serial_normalization_preserves_prefix(self) -> None:
        self.assertEqual(normalize_serial("RA 3389449"), "RA3389449")


if __name__ == "__main__":
    unittest.main()
