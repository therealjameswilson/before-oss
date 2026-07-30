from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from oss_research.constants import PERSONNEL_CATEGORIES
from oss_research.db import connect, migrate


class DatabaseMigrationTests(unittest.TestCase):
    def test_source_records_accept_every_normalized_personnel_category(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            connection = connect(Path(temp_dir) / "test.sqlite")
            try:
                migrate(connection)
                for row_number, category in enumerate(
                    sorted(PERSONNEL_CATEGORIES), start=1
                ):
                    connection.execute(
                        """
                        INSERT INTO source_records(
                            source_record_id, source_pdf, source_pdf_sha256,
                            source_page, source_row_number, raw_row_text,
                            last_name_raw, display_name, normalized_name,
                            last_name, personnel_category, name_variants_json,
                            parser_confidence, requires_visual_review,
                            visual_review_status, entity_resolution_status,
                            ingested_at, parser_version
                        ) VALUES (?, ?, ?, 1, ?, ?, ?, ?, ?, ?, ?, '[]',
                                  1.0, 0, 'not_reviewed', 'unresolved', ?, ?)
                        """,
                        (
                            f"record-{row_number}",
                            "fixture.pdf",
                            "fixture-sha256",
                            row_number,
                            category,
                            category,
                            category,
                            category.upper(),
                            category,
                            category,
                            "2026-07-30T00:00:00+00:00",
                            "test-v1",
                        ),
                    )
                connection.commit()
                self.assertEqual(
                    connection.execute(
                        "SELECT COUNT(*) FROM source_records"
                    ).fetchone()[0],
                    len(PERSONNEL_CATEGORIES),
                )
            finally:
                connection.close()


if __name__ == "__main__":
    unittest.main()
