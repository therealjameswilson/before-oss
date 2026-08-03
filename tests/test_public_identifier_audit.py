from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from subprocess import CompletedProcess
from unittest.mock import patch

from scripts.audit_public_identifiers import (
    _integer_values,
    public_aggregate_values,
    scan,
)


class PublicIdentifierAuditTests(unittest.TestCase):
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
                candidates, boundary_matches, aggregate_false_positives = scan(
                    public_root,
                    {"12345"},
                    set(),
                    public_aggregate_values(public_root),
                )

            self.assertEqual(candidates, 2)
            self.assertEqual(aggregate_false_positives, 1)
            self.assertEqual(boundary_matches, 1)
