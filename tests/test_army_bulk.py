from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from oss_research.db import connect, migrate
from oss_research.identity import build_identities
from oss_research.sources import army_bulk


def _record(identifier: str, name: str, occupation: str = "098") -> bytes:
    row = bytearray(b" " * 89 + b"\r\n")
    row[0:8] = identifier.encode("ascii")
    row[8 : 8 + len(name)] = name.encode("ascii")
    row[41:47] = b"420630"
    row[47:51] = b"PVT "
    row[69:72] = occupation.encode("ascii")
    return bytes(row)


class ArmyBulkTests(unittest.TestCase):
    def test_bounded_checkpoint_keeps_name_conflicts_private_and_status_unchanged(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            connection = connect(root / "research.sqlite")
            try:
                migrate(connection)
                names = [
                    ("row-john", 1, "Deull", "John", "B", "12345678"),
                    ("row-sol", 2, "Deull", "Sol", "NMI", "12345678"),
                    ("row-jane", 3, "Smith", "Jane", "", "87654321"),
                ]
                with connection:
                    for source_id, row_number, surname, given, middle, identifier in names:
                        connection.execute(
                            """
                            INSERT INTO source_records(
                                source_record_id, source_pdf, source_pdf_sha256,
                                source_page, source_row_number, raw_row_text,
                                last_name_raw, first_name_raw, middle_initial_raw,
                                serial_number_raw, display_name, normalized_name,
                                last_name, first_name, middle_name_or_initial,
                                serial_number_normalized, personnel_category,
                                parser_confidence, ingested_at, parser_version
                            ) VALUES (?, 'fixture.pdf', 'fixture-sha256', 1, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                                      'unknown_or_indeterminate', 1.0, '2026-09-19T00:00:00Z', 'fixture')
                            """,
                            (
                                source_id,
                                row_number,
                                f"{surname} {given} {middle}",
                                surname,
                                given,
                                middle,
                                identifier,
                                f"{given} {middle} {surname}".replace("  ", " ").strip(),
                                f"{surname} {given} {middle}".strip().upper(),
                                surname,
                                given,
                                middle,
                                identifier,
                            ),
                        )
                build_identities(connection)
                payload = _record("12345678", "DEULL JOHN B") + _record("87654321", "SMITH JANE")
                path = root / "ASNEF.FIN.DAT"
                path.write_bytes(payload)
                expected_hash = hashlib.sha256(payload).hexdigest()
                with patch.object(army_bulk, "ARMY_BULK_BYTES", len(payload)), patch.object(
                    army_bulk, "ARMY_BULK_RECORDS", 2
                ):
                    preview = army_bulk.match_army_bulk(
                        connection, path, max_candidates=1, dry_run=True,
                        expected_sha256=expected_hash,
                    )
                    self.assertEqual(preview["identity_candidates_total"], 3)
                    self.assertEqual(preview["name_agreement_candidates"], 2)
                    self.assertEqual(preview["name_conflict_candidates"], 1)
                    self.assertEqual(preview["candidates_checkpointed_this_run"], 0)
                    self.assertEqual(connection.execute("SELECT COUNT(*) FROM candidate_matches WHERE candidate_url = ?", (army_bulk.ARMY_BULK_URL,)).fetchone()[0], 0)

                    for remaining in (2, 1, 0):
                        result = army_bulk.match_army_bulk(
                            connection, path, max_candidates=1,
                            expected_sha256=expected_hash,
                        )
                        self.assertEqual(result["candidates_remaining"], remaining)
                        self.assertEqual(result["candidates_checkpointed_this_run"], 1)

                    rows = list(connection.execute(
                        "SELECT evidence_json, candidate_identifier FROM candidate_matches WHERE candidate_url = ?",
                        (army_bulk.ARMY_BULK_URL,),
                    ))
                    self.assertEqual(len(rows), 3)
                    self.assertTrue(any(json.loads(row[0])["name_alignment"] == "name_conflict" for row in rows))
                    for row in rows:
                        self.assertNotIn("12345678", row[0] + row[1])
                        self.assertNotIn("87654321", row[0] + row[1])
                        self.assertIn("neither a named employer", row[0])

                    candidate_id = connection.execute(
                        "SELECT candidate_match_id FROM candidate_matches WHERE candidate_url = ? LIMIT 1",
                        (army_bulk.ARMY_BULK_URL,),
                    ).fetchone()[0]
                    with connection:
                        connection.execute(
                            "UPDATE candidate_matches SET match_assessment = 'rejected' WHERE candidate_match_id = ?",
                            (candidate_id,),
                        )
                    rerun = army_bulk.match_army_bulk(
                        connection, path, expected_sha256=expected_hash,
                    )
                    self.assertEqual(rerun["candidates_checkpointed_this_run"], 0)
                    self.assertEqual(connection.execute(
                        "SELECT match_assessment FROM candidate_matches WHERE candidate_match_id = ?",
                        (candidate_id,),
                    ).fetchone()[0], "rejected")

                self.assertEqual(connection.execute(
                    "SELECT COUNT(*) FROM person_entities WHERE research_status = 'not_started'"
                ).fetchone()[0], 3)
                self.assertEqual(connection.execute("SELECT COUNT(*) FROM affiliations").fetchone()[0], 0)
                self.assertEqual(connection.execute("SELECT COUNT(*) FROM research_attempts").fetchone()[0], 0)
            finally:
                connection.close()

    def test_wrong_checksum_fails_before_any_candidate_write(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            connection = connect(root / "research.sqlite")
            try:
                migrate(connection)
                payload = _record("12345678", "DEULL JOHN B")
                path = root / "ASNEF.FIN.DAT"
                path.write_bytes(payload)
                with patch.object(army_bulk, "ARMY_BULK_BYTES", len(payload)):
                    with self.assertRaisesRegex(ValueError, "SHA-256 mismatch"):
                        army_bulk.match_army_bulk(connection, path, expected_sha256="0" * 64)
                self.assertEqual(connection.execute("SELECT COUNT(*) FROM candidate_matches").fetchone()[0], 0)
            finally:
                connection.close()


if __name__ == "__main__":
    unittest.main()
