from __future__ import annotations

import sqlite3
import unittest

from oss_research.classification import refresh_unknown_classifications


class RefreshClassificationsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.db = sqlite3.connect(":memory:")
        self.db.row_factory = sqlite3.Row
        self.db.executescript(
            """
            CREATE TABLE source_records (
                source_record_id TEXT PRIMARY KEY, source_page INTEGER,
                source_row_number INTEGER, rank_raw TEXT, notes_raw TEXT,
                personnel_category TEXT, commissioned_officer INTEGER,
                allied_or_foreign_personnel INTEGER, normalization_notes TEXT,
                rank_normalized TEXT
            );
            CREATE TABLE person_entities (
                person_id TEXT PRIMARY KEY, personnel_category TEXT,
                commissioned_officer INTEGER,
                allied_or_foreign_personnel INTEGER, updated_at TEXT
            );
            CREATE TABLE person_source_links (
                person_id TEXT, source_record_id TEXT
            );
            """
        )
        for number, person_category in ((1, "unknown_or_indeterminate"),
                                        (2, "commissioned_naval_officer")):
            self.db.execute(
                "INSERT INTO source_records VALUES (?, 150, ?, 'Cmdr', NULL, ?, NULL, NULL, ?, 'CMDR')",
                (
                    f"source-{number}", number, "unknown_or_indeterminate",
                    "Printed rank or grade is preserved but not classified by the current rule set.",
                ),
            )
            self.db.execute(
                "INSERT INTO person_entities VALUES (?, ?, NULL, NULL, NULL)",
                (f"person-{number}", person_category),
            )
            self.db.execute(
                "INSERT INTO person_source_links VALUES (?, ?)",
                (f"person-{number}", f"source-{number}"),
            )
        self.db.commit()

    def tearDown(self) -> None:
        self.db.close()

    def test_monotonic_refresh_and_idempotence(self) -> None:
        planned = refresh_unknown_classifications(self.db, dry_run=True)
        self.assertEqual(planned["source_rows_reclassified"], 2)
        self.assertEqual(planned["person_entities_reclassified"], 1)
        self.assertEqual(
            self.db.execute("SELECT personnel_category FROM source_records LIMIT 1").fetchone()[0],
            "unknown_or_indeterminate",
        )

        result = refresh_unknown_classifications(self.db)
        self.assertEqual(result["source_rows_reclassified"], 2)
        self.assertEqual(result["person_entities_reclassified"], 1)
        source = self.db.execute(
            "SELECT * FROM source_records WHERE source_record_id = 'source-1'"
        ).fetchone()
        self.assertEqual(source["rank_raw"], "Cmdr")
        self.assertEqual(source["personnel_category"], "commissioned_naval_officer")
        self.assertEqual(source["commissioned_officer"], 1)
        self.assertNotIn("not classified", source["normalization_notes"])
        self.assertEqual(
            self.db.execute(
                "SELECT personnel_category FROM person_entities WHERE person_id = 'person-2'"
            ).fetchone()[0],
            "commissioned_naval_officer",
        )
        self.assertEqual(refresh_unknown_classifications(self.db)["source_rows_reclassified"], 0)


if __name__ == "__main__":
    unittest.main()
