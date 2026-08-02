#!/usr/bin/env python3
"""Audit generated public artifacts for full private service identifiers.

The scanner sends private identifier patterns to ripgrep over stdin and parses
its JSON stream in memory. It reports aggregate counts only: identifiers,
artifacts, candidate substring matches, and boundary-delimited matches. No
identifier value or matching line is written to stdout or stderr.
"""

from __future__ import annotations

import argparse
import json
import sqlite3
import subprocess
import sys
from pathlib import Path


ASCII_ALNUM = frozenset(
    b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
)


def identifier_sets(database: Path) -> tuple[set[str], set[str]]:
    with sqlite3.connect(database) as connection:
        normalized = {
            row[0]
            for row in connection.execute(
                """
                SELECT DISTINCT serial_number_normalized
                FROM source_records
                WHERE serial_number_normalized IS NOT NULL
                  AND length(serial_number_normalized) >= 5
                """
            )
        }
        formatted = {
            row[0].strip()
            for row in connection.execute(
                """
                SELECT DISTINCT serial_number_raw
                FROM source_records
                WHERE serial_number_normalized IS NOT NULL
                  AND length(serial_number_normalized) >= 5
                  AND trim(serial_number_raw) <> serial_number_normalized
                """
            )
        }
    return normalized, formatted


def public_artifact_count(public_root: Path) -> int:
    return sum(1 for path in public_root.rglob("*") if path.is_file())


def scan(
    public_root: Path,
    normalized: set[str],
    formatted: set[str],
) -> tuple[int, int]:
    patterns = sorted(normalized | formatted, key=lambda value: (-len(value), value))
    command = [
        "rg",
        "--json",
        "--search-zip",
        "--text",
        "--fixed-strings",
        "--file",
        "-",
        str(public_root),
    ]
    completed = subprocess.run(
        command,
        input="\n".join(patterns) + "\n",
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    # ripgrep returns 1 when no match exists; either 0 or 1 is a valid audit.
    if completed.returncode not in (0, 1):
        raise RuntimeError(
            f"ripgrep privacy scan failed with exit code {completed.returncode}"
        )

    candidate_matches = 0
    boundary_matches = 0
    for raw_event in completed.stdout.splitlines():
        event = json.loads(raw_event)
        if event.get("type") != "match":
            continue
        data = event["data"]
        line_block = data["lines"]
        if "text" not in line_block:
            # Binary/base64 records cannot contain an inspectable public text
            # claim. ripgrep is invoked with --text, so this is defensive.
            continue
        line = line_block["text"].encode("utf-8")
        for match in data["submatches"]:
            candidate_matches += 1
            start = match["start"]
            end = match["end"]
            before = line[start - 1] if start else None
            after = line[end] if end < len(line) else None
            if (
                (before is None or before not in ASCII_ALNUM)
                and (after is None or after not in ASCII_ALNUM)
            ):
                boundary_matches += 1
    return candidate_matches, boundary_matches


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--database", type=Path, default=Path("research/research.sqlite")
    )
    parser.add_argument("--public-root", type=Path, default=Path("site/dist"))
    args = parser.parse_args()

    normalized, formatted = identifier_sets(args.database)
    artifact_count = public_artifact_count(args.public_root)
    candidates, boundary_matches = scan(args.public_root, normalized, formatted)
    print(
        "normalized_identifiers={} formatted_variants={} artifacts={} "
        "candidate_substrings={} unexpected_boundary_matches={}".format(
            len(normalized),
            len(formatted),
            artifact_count,
            candidates,
            boundary_matches,
        )
    )
    return 1 if boundary_matches else 0


if __name__ == "__main__":
    sys.exit(main())
