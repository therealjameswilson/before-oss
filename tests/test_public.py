from __future__ import annotations

import unittest

from oss_research.public import mask_serial, public_source_row


class FakeRow(dict):
    def __getitem__(self, key: str) -> object:
        return super().__getitem__(key)


class PublicProjectionTests(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
