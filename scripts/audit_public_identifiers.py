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
import re
import sqlite3
import subprocess
import sys
from pathlib import Path


ASCII_ALNUM = frozenset(
    b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
)
SERIAL_FORMAT_RE = re.compile(r"[^A-Z0-9]")


def _normalize_raw_identifier(value: str) -> str | None:
    normalized = SERIAL_FORMAT_RE.sub("", value.upper())
    return normalized or None


def identifier_sets(database: Path) -> tuple[set[str], set[str]]:
    if not database.is_file():
        raise FileNotFoundError(
            f"Private audit database is missing: {database}. Run the ingest stage first."
        )
    with sqlite3.connect(database) as connection:
        try:
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
                raw_value.strip()
                for raw_value, normalized_value in connection.execute(
                    """
                    SELECT DISTINCT serial_number_raw, serial_number_normalized
                    FROM source_records
                    WHERE serial_number_normalized IS NOT NULL
                      AND length(serial_number_normalized) >= 5
                      AND trim(serial_number_raw) <> serial_number_normalized
                    """
                )
                if _normalize_raw_identifier(raw_value) == normalized_value
            }
        except sqlite3.OperationalError as error:
            raise RuntimeError(
                f"Private audit database is not ingested: {database}"
            ) from error
    return normalized, formatted


def public_artifact_count(public_root: Path) -> int:
    return sum(1 for path in public_root.rglob("*") if path.is_file())


def _integer_values(value: object) -> set[int]:
    if isinstance(value, bool):
        return set()
    if isinstance(value, int):
        return {value}
    if isinstance(value, list):
        return set().union(*(_integer_values(item) for item in value), set())
    if isinstance(value, dict):
        return set().union(*(_integer_values(item) for item in value.values()), set())
    return set()


def public_aggregate_values(public_root: Path) -> set[int]:
    stats_path = public_root / "data" / "stats.json"
    if not stats_path.is_file():
        raise FileNotFoundError(
            f"Public aggregate statistics are missing: {stats_path}. Build the site first."
        )
    return _integer_values(json.loads(stats_path.read_text(encoding="utf-8")))


def public_manifest_sizes(public_root: Path) -> set[int]:
    manifest_path = public_root / "data" / "public_build_manifest.json"
    if not manifest_path.is_file():
        raise FileNotFoundError(
            f"Public build manifest is missing: {manifest_path}. Build the site first."
        )
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    return {
        item["size_bytes"]
        for item in manifest.get("files", [])
        if isinstance(item, dict)
        and isinstance(item.get("size_bytes"), int)
        and not isinstance(item.get("size_bytes"), bool)
    }


def scan(
    public_root: Path,
    normalized: set[str],
    formatted: set[str],
    aggregate_values: set[int],
    manifest_sizes: set[int],
) -> tuple[int, int, int, int]:
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
    aggregate_false_positives = 0
    manifest_size_false_positives = 0
    for raw_event in completed.stdout.splitlines():
        event = json.loads(raw_event)
        if event.get("type") != "match":
            continue
        data = event["data"]
        artifact_path = data["path"]["text"]
        aggregate_artifact = artifact_path.endswith(
            "/data/stats.json"
        ) or artifact_path.endswith("/data/stats.json.gz")
        manifest_artifact = artifact_path.endswith(
            "/data/public_build_manifest.json"
        ) or artifact_path.endswith("/data/public_build_manifest.json.gz")
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
                matched_text = line[start:end].decode("utf-8", errors="strict")
                if (
                    aggregate_artifact
                    and matched_text.isdigit()
                    and int(matched_text) in aggregate_values
                ):
                    aggregate_false_positives += 1
                    continue
                if (
                    manifest_artifact
                    and matched_text.isdigit()
                    and int(matched_text) in manifest_sizes
                    and line[max(0, start - 32) : start]
                    .rstrip()
                    .endswith(b'"size_bytes":')
                ):
                    manifest_size_false_positives += 1
                    continue
                boundary_matches += 1
    return (
        candidate_matches,
        boundary_matches,
        aggregate_false_positives,
        manifest_size_false_positives,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--database", type=Path, default=Path("research/research.sqlite")
    )
    parser.add_argument("--public-root", type=Path, default=Path("site/dist"))
    args = parser.parse_args()

    normalized, formatted = identifier_sets(args.database)
    artifact_count = public_artifact_count(args.public_root)
    aggregate_values = public_aggregate_values(args.public_root)
    manifest_sizes = public_manifest_sizes(args.public_root)
    (
        candidates,
        boundary_matches,
        aggregate_false_positives,
        manifest_size_false_positives,
    ) = scan(
        args.public_root,
        normalized,
        formatted,
        aggregate_values,
        manifest_sizes,
    )
    print(
        "normalized_identifiers={} formatted_variants={} artifacts={} "
        "candidate_substrings={} aggregate_false_positives={} "
        "manifest_size_false_positives={} unexpected_boundary_matches={}".format(
            len(normalized),
            len(formatted),
            artifact_count,
            candidates,
            aggregate_false_positives,
            manifest_size_false_positives,
            boundary_matches,
        )
    )
    return 1 if boundary_matches else 0


if __name__ == "__main__":
    sys.exit(main())
