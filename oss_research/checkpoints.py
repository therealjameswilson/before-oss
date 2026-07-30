from __future__ import annotations

import json
import sqlite3
from pathlib import Path

from .constants import RESEARCH_STATUSES
from .db import utc_now

ATTEMPT_COLUMNS = [
    "research_attempt_id",
    "person_id",
    "source_adapter",
    "query_variant_type",
    "request_fingerprint",
    "started_at",
    "completed_at",
    "outcome",
    "sources_reviewed",
    "candidate_sources_rejected",
    "attempt_number",
    "research_agent_version",
]
PERSON_UPDATE_COLUMNS = ["person_id", "research_status", "next_action"]
CANDIDATE_COLUMNS = [
    "candidate_match_id",
    "person_id",
    "candidate_type",
    "candidate_label",
    "candidate_url",
    "candidate_identifier",
    "evidence_json",
    "created_at",
    "updated_at",
]
ATTEMPT_OUTCOMES = {
    "planned",
    "searched",
    "candidate_found",
    "source_reviewed",
    "candidate_rejected",
    "no_result",
    "blocked",
    "error",
    "skipped_budget",
}
CANDIDATE_TYPES = {
    "identity",
    "source",
    "organization",
    "affiliation",
    "duplicate_person",
}


def _table_rows(
    payload: dict[str, object],
    *,
    columns_key: str,
    rows_key: str,
    expected_columns: list[str],
) -> list[dict[str, object]]:
    columns = payload.get(columns_key)
    if columns != expected_columns:
        raise ValueError(
            f"{columns_key} must exactly match the documented checkpoint schema."
        )
    rows = payload.get(rows_key)
    if not isinstance(rows, list):
        raise ValueError(f"{rows_key} must be a list.")
    normalized: list[dict[str, object]] = []
    for number, row in enumerate(rows, start=1):
        if not isinstance(row, list) or len(row) != len(expected_columns):
            raise ValueError(f"{rows_key} row {number} has the wrong width.")
        normalized.append(dict(zip(expected_columns, row, strict=True)))
    return normalized


def import_adapter_checkpoints(
    connection: sqlite3.Connection,
    path: Path,
) -> dict[str, int]:
    """Replay sanitized adapter audit state without storing query text or payloads."""
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("checkpoint_version") != "1.0":
        raise ValueError("Unsupported adapter checkpoint version.")
    attempts = _table_rows(
        payload,
        columns_key="attempt_columns",
        rows_key="attempts",
        expected_columns=ATTEMPT_COLUMNS,
    )
    person_updates = _table_rows(
        payload,
        columns_key="person_update_columns",
        rows_key="person_updates",
        expected_columns=PERSON_UPDATE_COLUMNS,
    )
    candidates = _table_rows(
        payload,
        columns_key="candidate_columns",
        rows_key="candidates",
        expected_columns=CANDIDATE_COLUMNS,
    )
    referenced_people = {
        str(row["person_id"]) for row in [*attempts, *person_updates, *candidates]
    }
    if referenced_people:
        placeholders = ",".join("?" for _ in referenced_people)
        known_people = {
            str(row[0])
            for row in connection.execute(
                f"SELECT person_id FROM person_entities "
                f"WHERE person_id IN ({placeholders})",
                tuple(sorted(referenced_people)),
            )
        }
        missing_people = sorted(referenced_people - known_people)
        if missing_people:
            raise ValueError(
                f"Checkpoint references {len(missing_people)} unknown people."
            )

    for row in attempts:
        if row["outcome"] not in ATTEMPT_OUTCOMES:
            raise ValueError(f"Invalid checkpoint outcome: {row['outcome']}")
        if int(row["attempt_number"]) <= 0:
            raise ValueError("Checkpoint attempt numbers must be positive.")
    for row in person_updates:
        if row["research_status"] not in RESEARCH_STATUSES:
            raise ValueError(
                f"Invalid checkpoint research status: {row['research_status']}"
            )
    for row in candidates:
        if row["candidate_type"] not in CANDIDATE_TYPES:
            raise ValueError(
                f"Invalid checkpoint candidate type: {row['candidate_type']}"
            )
        json.loads(str(row["evidence_json"]))

    now = utc_now()
    with connection:
        for row in attempts:
            connection.execute(
                """
                INSERT INTO research_attempts(
                    research_attempt_id, person_id, pipeline_run_id,
                    source_adapter, query_text, query_variant_type,
                    request_fingerprint, started_at, completed_at, outcome,
                    sources_reviewed, candidate_sources_rejected,
                    rejection_reasons, research_notes, next_action,
                    last_error_redacted, attempt_number, research_agent_version
                ) VALUES (?, ?, NULL, ?, NULL, ?, ?, ?, ?, ?, ?, ?,
                          NULL, NULL, NULL, NULL, ?, ?)
                ON CONFLICT(research_attempt_id) DO UPDATE SET
                    source_adapter=excluded.source_adapter,
                    query_variant_type=COALESCE(
                        excluded.query_variant_type,
                        research_attempts.query_variant_type
                    ),
                    request_fingerprint=COALESCE(
                        excluded.request_fingerprint,
                        research_attempts.request_fingerprint
                    ),
                    started_at=excluded.started_at,
                    completed_at=excluded.completed_at,
                    outcome=excluded.outcome,
                    sources_reviewed=excluded.sources_reviewed,
                    candidate_sources_rejected=excluded.candidate_sources_rejected,
                    attempt_number=excluded.attempt_number,
                    research_agent_version=excluded.research_agent_version
                """,
                tuple(row[column] for column in ATTEMPT_COLUMNS),
            )
        for row in candidates:
            connection.execute(
                """
                INSERT INTO candidate_matches(
                    candidate_match_id, person_id, candidate_type,
                    candidate_label, candidate_url, candidate_identifier,
                    evidence_json, match_assessment, rejection_reason,
                    created_at, updated_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, 'unreviewed', NULL, ?, ?)
                ON CONFLICT(candidate_match_id) DO UPDATE SET
                    candidate_type=excluded.candidate_type,
                    candidate_label=excluded.candidate_label,
                    candidate_url=excluded.candidate_url,
                    candidate_identifier=excluded.candidate_identifier,
                    evidence_json=excluded.evidence_json
                """,
                tuple(row[column] for column in CANDIDATE_COLUMNS),
            )
        for row in person_updates:
            first_attempt = connection.execute(
                """
                SELECT MIN(started_at) FROM research_attempts
                WHERE person_id = ?
                  AND outcome NOT IN ('planned', 'skipped_budget')
                """,
                (row["person_id"],),
            ).fetchone()[0]
            connection.execute(
                """
                UPDATE person_entities
                SET research_status = ?,
                    research_started_at = COALESCE(research_started_at, ?),
                    next_action = ?,
                    updated_at = ?
                WHERE person_id = ?
                """,
                (
                    row["research_status"],
                    first_attempt,
                    row["next_action"],
                    now,
                    row["person_id"],
                ),
            )
            connection.execute(
                """
                UPDATE research_queue
                SET research_status = ?, next_action = ?, updated_at = ?
                WHERE person_id = ?
                """,
                (
                    row["research_status"],
                    row["next_action"],
                    now,
                    row["person_id"],
                ),
            )
        for person_id in sorted(referenced_people):
            attempt_count = connection.execute(
                "SELECT COUNT(*) FROM research_attempts WHERE person_id = ?",
                (person_id,),
            ).fetchone()[0]
            connection.execute(
                """
                UPDATE person_entities
                SET research_attempt_number = ?, updated_at = ?
                WHERE person_id = ?
                """,
                (attempt_count, now, person_id),
            )
            connection.execute(
                """
                UPDATE research_queue
                SET attempts = ?, updated_at = ?
                WHERE person_id = ?
                """,
                (attempt_count, now, person_id),
            )
    return {
        "research_attempts": len(attempts),
        "person_updates": len(person_updates),
        "candidate_matches": len(candidates),
    }
