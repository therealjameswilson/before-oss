from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from oss_research.db import connect, migrate
from oss_research.identity import build_identities


class IdentityBuildTests(unittest.TestCase):
    def test_rebuild_refreshes_parser_derived_name_variants(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            connection = connect(Path(temp_dir) / "test.sqlite")
            try:
                migrate(connection)
                with connection:
                    connection.execute(
                        """
                        INSERT INTO source_records(
                            source_record_id, source_pdf, source_pdf_sha256,
                            source_page, source_row_number, raw_row_text,
                            last_name_raw, first_name_raw, middle_initial_raw,
                            display_name, normalized_name, last_name, first_name,
                            personnel_category, name_variants_json,
                            parser_confidence, requires_visual_review,
                            visual_review_status, entity_resolution_status,
                            ingested_at, parser_version
                        ) VALUES (
                            'record-1', 'fixture.pdf', 'fixture-sha256',
                            1, 1, 'Shift Sonia P-2', 'Shift', 'Sonia', 'P-2',
                            'Sonia Shift', 'SONIA SHIFT', 'Shift', 'Sonia',
                            'civilian_professional_or_administrative_grade',
                            ?, 0.88, 1, 'reviewed_corrected', 'unresolved',
                            '2026-07-30T00:00:00+00:00', 'test-v1'
                        )
                        """,
                        (json.dumps(["Shift, Sonia P-2"]),),
                    )

                build_identities(connection)
                with connection:
                    connection.execute(
                        """
                        UPDATE source_records
                        SET name_variants_json = ?
                        WHERE source_record_id = 'record-1'
                        """,
                        (json.dumps(["Shift, Sonia"]),),
                    )

                build_identities(connection)

                variants = connection.execute(
                    "SELECT name_variants_json FROM person_entities"
                ).fetchone()[0]
                self.assertEqual(json.loads(variants), ["Shift, Sonia"])
            finally:
                connection.close()


if __name__ == "__main__":
    unittest.main()
