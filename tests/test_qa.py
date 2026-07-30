from __future__ import annotations

import unittest

from oss_research.qa import commissioned_category_is_consistent


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


if __name__ == "__main__":
    unittest.main()
