from __future__ import annotations

import inspect
import unittest

from oss_research.qa import commissioned_category_is_consistent, validate_ingest


class ProfileQaTests(unittest.TestCase):
    def test_foreign_lieutenant_can_remain_in_allied_category(self) -> None:
        self.assertTrue(
            commissioned_category_is_consistent(
                1,
                "foreign_or_allied_military_personnel",
            )
        )

    def test_commissioned_flag_still_rejects_enlisted_category(self) -> None:
        self.assertFalse(
            commissioned_category_is_consistent(
                1,
                "enlisted_army_personnel",
            )
        )

    def test_noncommissioned_rows_are_not_restricted_to_officer_categories(
        self,
    ) -> None:
        self.assertTrue(
            commissioned_category_is_consistent(
                0,
                "enlisted_naval_personnel",
            )
        )

    def test_parser_warning_report_does_not_select_raw_source_rows(self) -> None:
        source = inspect.getsource(validate_ingest)
        warning_query = source.split("warnings = list(", maxsplit=1)[1].split(
            "reasons = selected_pages",
            maxsplit=1,
        )[0]
        self.assertNotIn("raw_row_text", warning_query)
        self.assertIn("source_record_id", warning_query)


if __name__ == "__main__":
    unittest.main()
