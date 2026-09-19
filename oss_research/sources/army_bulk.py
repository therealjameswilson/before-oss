"""Conservative, resumable identity triage against NARA's Army bulk file.

The Electronic Army Serial Number Merged File is an official, separately
downloaded bulk-data source, not a Catalog API response. A matching private
identifier is only a candidate until the name and archival context are
reviewed. In particular, its civilian-occupation field is not an employer.
"""

from __future__ import annotations

import hashlib
import json
import re
import sqlite3
import unicodedata
import uuid
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

from ..constants import NAMESPACE_GENERIC
from ..db import utc_now

ARMY_BULK_URL = "https://catalog.archives.gov/id/1263923"
ARMY_BULK_NAID = "1263923"
ARMY_BULK_SHA256 = "db10dbf90f0ef95dc327b0e8f8f0489923941b65399cf79bba71ac4b45d07e5b"
ARMY_BULK_BYTES = 837_221_112
ARMY_BULK_RECORDS = 9_200_232
ARMY_RECORD_LENGTH = 91
ADAPTER_VERSION = "army-bulk-identity-v1"


@dataclass(frozen=True)
class IndexedRow:
    person_id: str
    source_record_id: str
    surname: str
    given: str
    middle: str
    identifier: bytes
    shared_identifier: bool


@dataclass(frozen=True)
class Candidate:
    person_id: str
    source_record_id: str
    ordinal: int
    indexed_name: str
    army_name: str
    alignment: str
    shared_identifier: bool
    entry_date_code: str
    grade_code: str
    occupation_code: str

    @property
    def candidate_id(self) -> str:
        # The stable ID contains no service number and survives a display-name edit.
        value = f"{ADAPTER_VERSION}:{self.person_id}:{self.source_record_id}:{self.ordinal}"
        return str(uuid.uuid5(uuid.UUID(NAMESPACE_GENERIC), value))


def _tokens(value: str) -> list[str]:
    ascii_value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    return re.findall(r"[A-Z0-9]+", ascii_value.upper())


def conflict_triage(indexed_name: str, army_name: str, alignment: str) -> str:
    """Explain a stored name conflict for *private review*, never identity promotion.

    The index and Army file often differ only in surname spacing (for example,
    DE VICO/DEVICO). Collapsing punctuation and whitespace helps route those
    leads, but is insufficient to establish that the two people are identical.
    The original name-alignment assessment and both source spellings are kept.
    """
    if alignment != "name_conflict":
        return "not_a_name_conflict"
    indexed = "".join(_tokens(indexed_name))
    army = "".join(_tokens(army_name))
    if indexed and army and indexed == army:
        return "spacing_or_punctuation_only"
    return "substantive_name_difference"


def _alignment(indexed: IndexedRow, army_name: str) -> str:
    army = _tokens(army_name)
    surname = _tokens(indexed.surname)
    given = _tokens(indexed.given)
    if not surname or not given or army[: len(surname)] != surname:
        return "name_conflict"
    remaining = army[len(surname) :]
    if not remaining or remaining[0] != given[0]:
        return "name_conflict"
    middle = _tokens(indexed.middle)
    if middle and middle != ["NMI"]:
        army_middle = remaining[1:]
        if not army_middle:
            return "surname_given_only"
        if army_middle[0][0] != middle[0][0]:
            return "middle_disagreement"
    return "name_agrees"


def _eligible_rows(connection: sqlite3.Connection) -> tuple[dict[bytes, list[IndexedRow]], int]:
    rows = list(
        connection.execute(
            """
            SELECT l.person_id, s.source_record_id, s.last_name, s.first_name,
                   s.middle_name_or_initial, s.serial_number_normalized
            FROM source_records s
            JOIN person_source_links l ON l.source_record_id = s.source_record_id
            ORDER BY s.source_page, s.source_row_number, l.person_id
            """
        )
    )
    raw: dict[bytes, list[sqlite3.Row]] = defaultdict(list)
    for row in rows:
        identifier = (row["serial_number_normalized"] or "").strip()
        if len(identifier) == 8 and identifier.isascii() and identifier.isdigit():
            raw[identifier.encode("ascii")].append(row)
    eligible: dict[bytes, list[IndexedRow]] = {}
    for identifier, members in raw.items():
        shared = len({row["person_id"] for row in members}) > 1
        eligible[identifier] = [
            IndexedRow(
                person_id=row["person_id"],
                source_record_id=row["source_record_id"],
                surname=row["last_name"] or "",
                given=row["first_name"] or "",
                middle=row["middle_name_or_initial"] or "",
                identifier=identifier,
                shared_identifier=shared,
            )
            for row in members
        ]
    return eligible, sum(map(len, eligible.values()))


def _file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def _field(row: bytes, start: int, end: int) -> str:
    return row[start:end].decode("ascii", "replace").strip()


def scan_army_bulk(path: Path, indexed: dict[bytes, list[IndexedRow]]) -> tuple[list[Candidate], int]:
    candidates: list[Candidate] = []
    records = 0
    with path.open("rb", buffering=1024 * 1024) as handle:
        for record in handle:
            records += 1
            if len(record) != ARMY_RECORD_LENGTH or record[-2:] != b"\r\n":
                raise ValueError(f"Army bulk file has an invalid 91-byte record at ordinal {records}")
            members = indexed.get(record[:8])
            if not members:
                continue
            army_name = " ".join(_field(record, 8, 32).split())
            erc = record[79:80] == b"3"
            for member in members:
                candidates.append(
                    Candidate(
                        person_id=member.person_id,
                        source_record_id=member.source_record_id,
                        ordinal=records,
                        indexed_name=" ".join(filter(None, (member.surname, member.given, member.middle))),
                        army_name=army_name,
                        alignment=_alignment(member, army_name),
                        shared_identifier=member.shared_identifier,
                        entry_date_code=_field(record, 41, 47),
                        grade_code=_field(record, 47, 51),
                        occupation_code=_field(record, 70 if erc else 69, 73 if erc else 72),
                    )
                )
    return candidates, records


def match_army_bulk(
    connection: sqlite3.Connection,
    path: Path,
    *,
    max_candidates: int = 500,
    dry_run: bool = False,
    expected_sha256: str = ARMY_BULK_SHA256,
) -> dict[str, object]:
    """Scan once, checkpoint candidates in bounded idempotent batches.

    Existing candidate rows are never overwritten: a reviewer may already
    have accepted or rejected them. A repeat run scans the file again but
    inserts only the next uncheckpointed candidate rows.
    """
    if max_candidates < 1:
        raise ValueError("max_candidates must be at least one")
    if not path.is_file():
        raise FileNotFoundError(f"Army bulk file not found: {path}")
    actual_size = path.stat().st_size
    if actual_size != ARMY_BULK_BYTES:
        raise ValueError(f"Army bulk file size mismatch: {actual_size} bytes")
    actual_hash = _file_sha256(path)
    if actual_hash != expected_sha256:
        raise ValueError("Army bulk file SHA-256 mismatch; no candidates were stored")
    indexed, eligible_row_count = _eligible_rows(connection)
    candidates, records = scan_army_bulk(path, indexed)
    if records != ARMY_BULK_RECORDS:
        raise ValueError(f"Army bulk record-count mismatch: {records}")
    existing_ids = {
        row[0]
        for row in connection.execute(
            "SELECT candidate_match_id FROM candidate_matches WHERE candidate_url = ?",
            (ARMY_BULK_URL,),
        )
    }
    remaining = [candidate for candidate in candidates if candidate.candidate_id not in existing_ids]
    selected = remaining[:max_candidates]
    if not dry_run:
        now = utc_now()
        with connection:
            for candidate in selected:
                evidence = {
                    "adapter_version": ADAPTER_VERSION,
                    "source_record_id": candidate.source_record_id,
                    "bulk_file_naid": ARMY_BULK_NAID,
                    "bulk_record_ordinal": candidate.ordinal,
                    "indexed_name": candidate.indexed_name,
                    "army_name": candidate.army_name,
                    "name_alignment": candidate.alignment,
                    "private_identifier_agreement": True,
                    "identifier_shared_by_multiple_index_people": candidate.shared_identifier,
                    "army_entry_date_code": candidate.entry_date_code,
                    "army_grade_code": candidate.grade_code,
                    "civilian_occupation_code": candidate.occupation_code,
                    "limitation": (
                        "Identity review required. Army-entry civilian occupation "
                        "is neither a named employer nor an immediate pre-OSS affiliation."
                    ),
                }
                connection.execute(
                    """
                    INSERT INTO candidate_matches(
                        candidate_match_id, person_id, candidate_type,
                        candidate_label, candidate_url, candidate_identifier,
                        evidence_json, match_assessment, created_at, updated_at
                    ) VALUES (?, ?, 'identity', ?, ?, ?, ?, 'unreviewed', ?, ?)
                    ON CONFLICT(candidate_match_id) DO NOTHING
                    """,
                    (
                        candidate.candidate_id,
                        candidate.person_id,
                        "Army bulk identity lead — name/number review required"
                        if candidate.alignment != "name_conflict"
                        else "Army bulk identifier conflict — name differs",
                        ARMY_BULK_URL,
                        f"NAID {ARMY_BULK_NAID}; bulk record ordinal {candidate.ordinal}",
                        json.dumps(evidence, sort_keys=True),
                        now,
                        now,
                    ),
                )
    matched_source_record_ids = {candidate.source_record_id for candidate in candidates}
    matched_identifiers = {
        row.identifier
        for members in indexed.values()
        for row in members
        if row.source_record_id in matched_source_record_ids
    }
    return {
        "bulk_source_url": ARMY_BULK_URL,
        "bulk_file_sha256": actual_hash,
        "bulk_file_bytes": actual_size,
        "bulk_records_scanned": records,
        "eligible_index_rows": eligible_row_count,
        "eligible_index_people": len({row.person_id for members in indexed.values() for row in members}),
        "matched_private_identifiers": len(matched_identifiers),
        "identifier_nonhits": len(indexed) - len(matched_identifiers),
        "identity_candidates_total": len(candidates),
        "name_agreement_candidates": sum(c.alignment == "name_agrees" for c in candidates),
        "surname_given_only_candidates": sum(c.alignment == "surname_given_only" for c in candidates),
        "middle_disagreement_candidates": sum(c.alignment == "middle_disagreement" for c in candidates),
        "name_conflict_candidates": sum(c.alignment == "name_conflict" for c in candidates),
        "shared_index_identifier_candidates": sum(c.shared_identifier for c in candidates),
        "already_checkpointed": len(candidates) - len(remaining),
        "candidates_checkpointed_this_run": 0 if dry_run else len(selected),
        "candidates_remaining": len(remaining) if dry_run else len(remaining) - len(selected),
        "dry_run": dry_run,
        "research_status_changes": 0,
        "employer_claims_created": 0,
    }
