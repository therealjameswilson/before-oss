from __future__ import annotations

import json
import sqlite3
import tempfile
import unittest
from pathlib import Path
from subprocess import CompletedProcess
from unittest.mock import patch

from scripts.audit_public_identifiers import (
    _integer_values,
    identifier_sets,
    public_aggregate_values,
    public_manifest_sizes,
    scan,
)


class PublicIdentifierAuditTests(unittest.TestCase):
    def test_formatted_variants_exclude_shifted_date_annotations(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            database = Path(directory) / "research.sqlite"
            with sqlite3.connect(database) as connection:
                connection.execute(
                    """
                    CREATE TABLE source_records (
                        serial_number_raw TEXT,
                        serial_number_normalized TEXT
                    )
                    """
                )
                connection.executemany(
                    "INSERT INTO source_records VALUES (?, ?)",
                    [
                        ("A 12-3456", "A123456"),
                        ("Jun-43", "7654321"),
                    ],
                )

            normalized, formatted = identifier_sets(database)

            self.assertEqual(normalized, {"A123456", "7654321"})
            self.assertEqual(formatted, {"A 12-3456"})

    def test_integer_values_collects_counts_without_booleans(self) -> None:
        self.assertEqual(
            _integer_values({"count": 12, "nested": [34, True, 5.5, "67"]}),
            {12, 34},
        )

    def test_aggregate_coincidence_is_allowed_only_in_stats_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            public_root = Path(directory)
            stats_path = public_root / "data" / "stats.json"
            stats_path.parent.mkdir(parents=True)
            stats_path.write_text(json.dumps({"unresolved": 12345}), encoding="utf-8")
            (public_root / "profile.html").write_text(
                "Leaked identifier: 12345",
                encoding="utf-8",
            )

            events = []
            for path, line in (
                (stats_path, '{"unresolved": 12345}'),
                (public_root / "profile.html", "Leaked identifier: 12345"),
            ):
                start = len(line[: line.index("12345")].encode("utf-8"))
                events.append(
                    json.dumps(
                        {
                            "type": "match",
                            "data": {
                                "path": {"text": str(path)},
                                "lines": {"text": line},
                                "submatches": [
                                    {"start": start, "end": start + len("12345")}
                                ],
                            },
                        }
                    )
                )

            with patch(
                "scripts.audit_public_identifiers.subprocess.run",
                return_value=CompletedProcess(
                    args=["rg"],
                    returncode=0,
                    stdout="\n".join(events),
                    stderr="",
                ),
            ):
                (
                    candidates,
                    boundary_matches,
                    aggregate_false_positives,
                    manifest_size_false_positives,
                ) = scan(
                    public_root,
                    {"12345"},
                    set(),
                    public_aggregate_values(public_root),
                    set(),
                )

            self.assertEqual(candidates, 2)
            self.assertEqual(aggregate_false_positives, 1)
            self.assertEqual(manifest_size_false_positives, 0)
            self.assertEqual(boundary_matches, 1)

    def test_manifest_size_coincidence_is_allowed_only_in_size_field(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            public_root = Path(directory)
            data_root = public_root / "data"
            data_root.mkdir(parents=True)
            (data_root / "stats.json").write_text("{}", encoding="utf-8")
            manifest_path = data_root / "public_build_manifest.json"
            manifest_path.write_text(
                json.dumps(
                    {"files": [{"path": "data/example.json", "size_bytes": 12345}]}
                ),
                encoding="utf-8",
            )
            profile_path = public_root / "profile.html"
            profile_path.write_text("Leaked identifier: 12345", encoding="utf-8")

            events = []
            for path, line in (
                (manifest_path, manifest_path.read_text(encoding="utf-8")),
                (profile_path, "Leaked identifier: 12345"),
            ):
                start = len(line[: line.index("12345")].encode("utf-8"))
                events.append(
                    json.dumps(
                        {
                            "type": "match",
                            "data": {
                                "path": {"text": str(path)},
                                "lines": {"text": line},
                                "submatches": [
                                    {"start": start, "end": start + len("12345")}
                                ],
                            },
                        }
                    )
                )

            with patch(
                "scripts.audit_public_identifiers.subprocess.run",
                return_value=CompletedProcess(
                    args=["rg"],
                    returncode=0,
                    stdout="\n".join(events),
                    stderr="",
                ),
            ):
                (
                    candidates,
                    boundary_matches,
                    aggregate_false_positives,
                    manifest_size_false_positives,
                ) = scan(
                    public_root,
                    {"12345"},
                    set(),
                    public_aggregate_values(public_root),
                    public_manifest_sizes(public_root),
                )

            self.assertEqual(candidates, 2)
            self.assertEqual(aggregate_false_positives, 0)
            self.assertEqual(manifest_size_false_positives, 1)
            self.assertEqual(boundary_matches, 1)
