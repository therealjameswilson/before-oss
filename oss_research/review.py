from __future__ import annotations

import csv
import sqlite3
import uuid
from pathlib import Path

from .constants import NAMESPACE_GENERIC
from .db import utc_now

GENERIC_NAMESPACE = uuid.UUID(NAMESPACE_GENERIC)
RESEARCH_STATUSES = {
    "not_started",
    "in_progress",
    "candidate_found",
    "needs_identity_review",
    "needs_temporal_review",
    "verified_employer_found",
    "documented_prewar_employer_found",
    "occupation_only_found",
    "conflicting_sources",
    "no_reliable_result_after_protocol",
    "blocked_by_source_access",
    "requires_archival_review",
    "completed",
}


def import_review_decisions(
    connection: sqlite3.Connection, path: Path
) -> dict[str, int]:
    required = {
        "target_type",
        "target_id",
        "decision",
        "rationale",
        "reviewer",
        "decision_version",
    }
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        missing = required - set(reader.fieldnames or [])
        if missing:
            raise ValueError(f"Review CSV is missing columns: {sorted(missing)}")
        rows = list(reader)

    imported = applied = skipped_existing = 0
    for row_number, row in enumerate(rows, start=2):
        values = {key: (row.get(key) or "").strip() for key in required}
        if any(not value for value in values.values()):
            raise ValueError(f"Review CSV row {row_number} has blank required values.")
        decision_id = str(
            uuid.uuid5(
                GENERIC_NAMESPACE,
                "review:"
                + ":".join(
                    [
                        values["target_type"],
                        values["target_id"],
                        values["decision"],
                        values["reviewer"],
                        values["decision_version"],
                    ]
                ),
            )
        )
        exists = connection.execute(
            "SELECT 1 FROM review_decisions WHERE review_decision_id = ?",
            (decision_id,),
        ).fetchone()
        if exists:
            skipped_existing += 1
            continue
        with connection:
            connection.execute(
                """
                INSERT INTO review_decisions(
                    review_decision_id, target_type, target_id, decision,
                    rationale, reviewer, decision_version, created_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    decision_id,
                    values["target_type"],
                    values["target_id"],
                    values["decision"],
                    values["rationale"],
                    values["reviewer"],
                    values["decision_version"],
                    utc_now(),
                ),
            )
            imported += 1
            if values["target_type"] == "candidate_match":
                if values["decision"] not in {
                    "unreviewed",
                    "plausible",
                    "probable",
                    "accepted",
                    "rejected",
                    "conflicting",
                }:
                    raise ValueError(
                        f"Invalid candidate decision on row {row_number}."
                    )
                cursor = connection.execute(
                    """
                    UPDATE candidate_matches
                    SET match_assessment = ?,
                        rejection_reason = CASE
                            WHEN ? = 'rejected' THEN ? ELSE rejection_reason END,
                        updated_at = ?
                    WHERE candidate_match_id = ?
                    """,
                    (
                        values["decision"],
                        values["decision"],
                        values["rationale"],
                        utc_now(),
                        values["target_id"],
                    ),
                )
                applied += cursor.rowcount
            elif values["target_type"] == "research_status":
                if values["decision"] not in RESEARCH_STATUSES:
                    raise ValueError(
                        f"Invalid research status on row {row_number}."
                    )
                cursor = connection.execute(
                    """
                    UPDATE person_entities
                    SET research_status = ?, next_action = ?, updated_at = ?
                    WHERE person_id = ?
                    """,
                    (
                        values["decision"],
                        values["rationale"],
                        utc_now(),
                        values["target_id"],
                    ),
                )
                connection.execute(
                    """
                    UPDATE research_queue
                    SET research_status = ?, next_action = ?, updated_at = ?
                    WHERE person_id = ?
                    """,
                    (
                        values["decision"],
                        values["rationale"],
                        utc_now(),
                        values["target_id"],
                    ),
                )
                applied += cursor.rowcount
    return {
        "rows_read": len(rows),
        "decisions_imported": imported,
        "state_changes_applied": applied,
        "duplicates_skipped": skipped_existing,
    }
