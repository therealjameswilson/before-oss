from __future__ import annotations

import csv
import json
import sqlite3
import uuid
from pathlib import Path

from .constants import NAMESPACE_GENERIC
from .db import utc_now
from .normalize import clean, name_key

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

RESEARCH_STATUS_PRIORITY = {
    "not_started": 0,
    "in_progress": 1,
    "candidate_found": 2,
    "needs_identity_review": 3,
    "needs_temporal_review": 3,
    "blocked_by_source_access": 4,
    "requires_archival_review": 5,
    "no_reliable_result_after_protocol": 6,
    "occupation_only_found": 7,
    "documented_prewar_employer_found": 8,
    "verified_employer_found": 9,
    "conflicting_sources": 10,
    "completed": 11,
}

IDENTITY_STATUS_PRIORITY = {
    "unresolved": 0,
    "ambiguous": 1,
    "probable": 2,
    "high_confidence": 3,
    "confirmed": 4,
    "conflicting": 5,
}

ARCHIVAL_PRIORITY = {
    "unassessed": 0,
    "not_required": 1,
    "low": 2,
    "medium": 3,
    "high": 4,
    "critical": 5,
}


def _stronger_value(first: str, second: str, weights: dict[str, int]) -> str:
    return max((first, second), key=lambda value: weights[value])


def _merge_values(*values: str | None) -> str | None:
    unique = sorted(
        {part.strip() for value in values if value for part in value.split(";") if part.strip()},
        key=lambda value: (value.casefold(), value),
    )
    return "; ".join(unique) or None


def _merge_person_entity(
    connection: sqlite3.Connection,
    *,
    superseded_person_id: str,
    canonical_person_id: str,
    decision_id: str,
    rationale: str,
    reviewer: str,
    decision_version: str,
) -> int:
    if superseded_person_id == canonical_person_id:
        raise ValueError("A person entity cannot be merged into itself.")
    people = {
        row["person_id"]: row
        for row in connection.execute(
            "SELECT * FROM person_entities WHERE person_id IN (?, ?)",
            (superseded_person_id, canonical_person_id),
        )
    }
    missing = {
        superseded_person_id,
        canonical_person_id,
    } - set(people)
    if missing:
        raise ValueError(f"Unknown person IDs in entity merge: {sorted(missing)}")

    canonical_supersession = connection.execute(
        "SELECT canonical_person_id FROM entity_supersessions WHERE superseded_person_id=?",
        (canonical_person_id,),
    ).fetchone()
    if canonical_supersession:
        raise ValueError(
            "The selected canonical person is already superseded by "
            f"{canonical_supersession['canonical_person_id']}."
        )
    existing = connection.execute(
        "SELECT canonical_person_id FROM entity_supersessions WHERE superseded_person_id=?",
        (superseded_person_id,),
    ).fetchone()
    if existing and existing["canonical_person_id"] != canonical_person_id:
        raise ValueError(
            "The person is already superseded by a different canonical entity."
        )

    superseded = people[superseded_person_id]
    canonical = people[canonical_person_id]
    now = utc_now()
    audit_note = (
        f"Human-reviewed entity merge ({decision_version}; {reviewer}): {rationale}"
    )
    variants = {
        *json.loads(superseded["name_variants_json"] or "[]"),
        *json.loads(canonical["name_variants_json"] or "[]"),
        superseded["display_name"],
        canonical["display_name"],
    }
    personnel_category = canonical["personnel_category"]
    if personnel_category == "unknown_or_indeterminate":
        personnel_category = superseded["personnel_category"]
    research_status = _stronger_value(
        canonical["research_status"],
        superseded["research_status"],
        RESEARCH_STATUS_PRIORITY,
    )
    identity_status = _stronger_value(
        canonical["identity_status"],
        superseded["identity_status"],
        IDENTITY_STATUS_PRIORITY,
    )
    archival_priority = _stronger_value(
        canonical["archival_review_priority"],
        superseded["archival_review_priority"],
        ARCHIVAL_PRIORITY,
    )

    connection.execute(
        """
        INSERT INTO entity_supersessions(
            superseded_person_id, canonical_person_id, decision_id,
            reason, created_at
        ) VALUES (?, ?, ?, ?, ?)
        ON CONFLICT(superseded_person_id) DO UPDATE SET
            canonical_person_id=excluded.canonical_person_id,
            decision_id=excluded.decision_id,
            reason=excluded.reason
        """,
        (
            superseded_person_id,
            canonical_person_id,
            decision_id,
            rationale,
            now,
        ),
    )

    # Preserve each immutable PDF row while making its person link canonical.
    connection.execute(
        """
        DELETE FROM person_source_links
        WHERE person_id=?
          AND source_record_id IN (
              SELECT source_record_id FROM person_source_links WHERE person_id=?
          )
        """,
        (superseded_person_id, canonical_person_id),
    )
    connection.execute(
        """
        UPDATE person_source_links
        SET person_id=?, link_status='confirmed', evidence=?,
            algorithm_version=?, manual_review_required=0
        WHERE person_id=?
        """,
        (
            canonical_person_id,
            audit_note,
            f"human-review:{decision_version}",
            superseded_person_id,
        ),
    )
    connection.execute(
        """
        UPDATE person_source_links
        SET link_status='confirmed', evidence=?, algorithm_version=?,
            manual_review_required=0
        WHERE person_id=?
        """,
        (
            audit_note,
            f"human-review:{decision_version}",
            canonical_person_id,
        ),
    )
    connection.execute(
        """
        UPDATE source_records
        SET entity_resolution_status='linked', entity_resolution_evidence=?
        WHERE source_record_id IN (
            SELECT source_record_id FROM person_source_links WHERE person_id=?
        )
        """,
        (audit_note, canonical_person_id),
    )

    for table in (
        "affiliations",
        "claims",
        "research_attempts",
        "candidate_matches",
        "request_audit",
    ):
        connection.execute(
            f"UPDATE {table} SET person_id=? WHERE person_id=?",
            (canonical_person_id, superseded_person_id),
        )
    connection.execute(
        """
        UPDATE candidate_matches
        SET match_assessment='accepted', rejection_reason=NULL, updated_at=?
        WHERE person_id=? AND candidate_type='duplicate_person'
          AND candidate_label IN (?, ?)
        """,
        (
            now,
            canonical_person_id,
            canonical["possible_duplicate_group"],
            superseded["possible_duplicate_group"],
        ),
    )

    canonical_queue = connection.execute(
        "SELECT * FROM research_queue WHERE person_id=?",
        (canonical_person_id,),
    ).fetchone()
    superseded_queue = connection.execute(
        "SELECT * FROM research_queue WHERE person_id=?",
        (superseded_person_id,),
    ).fetchone()
    if canonical_queue and superseded_queue:
        connection.execute(
            """
            UPDATE research_queue
            SET priority=?, difficulty_tier=?, research_status=?,
                assigned_batch=COALESCE(assigned_batch, ?),
                next_action=COALESCE(next_action, ?), updated_at=?
            WHERE person_id=?
            """,
            (
                min(canonical_queue["priority"], superseded_queue["priority"]),
                max(
                    canonical_queue["difficulty_tier"],
                    superseded_queue["difficulty_tier"],
                ),
                research_status,
                superseded_queue["assigned_batch"],
                superseded_queue["next_action"],
                now,
                canonical_person_id,
            ),
        )
        connection.execute(
            "DELETE FROM research_queue WHERE person_id=?",
            (superseded_person_id,),
        )
    elif superseded_queue:
        connection.execute(
            "UPDATE research_queue SET person_id=?, updated_at=? WHERE person_id=?",
            (canonical_person_id, now, superseded_person_id),
        )

    attempt_count = connection.execute(
        "SELECT COUNT(*) FROM research_attempts WHERE person_id=?",
        (canonical_person_id,),
    ).fetchone()[0]
    commissioned_officer = canonical["commissioned_officer"]
    if commissioned_officer is None:
        commissioned_officer = superseded["commissioned_officer"]
    allied_or_foreign = canonical["allied_or_foreign_personnel"]
    if allied_or_foreign is None:
        allied_or_foreign = superseded["allied_or_foreign_personnel"]
    connection.execute(
        """
        UPDATE person_entities
        SET identity_status=?, identity_evidence=?, name_variants_json=?,
            personnel_category=?, commissioned_officer=?,
            allied_or_foreign_personnel=?, difficulty_tier=?,
            manual_review_required=0, possible_duplicate_group=NULL,
            research_status=?, research_started_at=COALESCE(research_started_at, ?),
            research_completed_at=COALESCE(research_completed_at, ?),
            research_attempt_number=?, next_action=COALESCE(next_action, ?),
            personnel_file_digitized=COALESCE(personnel_file_digitized, ?),
            personnel_file_reviewed=MAX(personnel_file_reviewed, ?),
            archive_box=?, archive_location=?,
            nara_catalog_id=COALESCE(nara_catalog_id, ?),
            archival_review_priority=?, updated_at=?
        WHERE person_id=?
        """,
        (
            identity_status,
            audit_note,
            json.dumps(
                sorted(variants, key=lambda value: (value.casefold(), value)),
                ensure_ascii=False,
            ),
            personnel_category,
            commissioned_officer,
            allied_or_foreign,
            max(canonical["difficulty_tier"], superseded["difficulty_tier"]),
            research_status,
            superseded["research_started_at"],
            superseded["research_completed_at"],
            attempt_count,
            superseded["next_action"],
            superseded["personnel_file_digitized"],
            superseded["personnel_file_reviewed"],
            _merge_values(canonical["archive_box"], superseded["archive_box"]),
            _merge_values(
                canonical["archive_location"], superseded["archive_location"]
            ),
            superseded["nara_catalog_id"],
            archival_priority,
            now,
            canonical_person_id,
        ),
    )
    connection.execute(
        "UPDATE research_queue SET attempts=?, updated_at=? WHERE person_id=?",
        (attempt_count, now, canonical_person_id),
    )
    return 1


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
        with connection:
            if exists:
                skipped_existing += 1
            else:
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
            elif values["target_type"] == "person_entity":
                if values["decision"].startswith("display_name:"):
                    # A guarded editorial correction changes only the entity's
                    # presentation. Printed source fields and identity stay put.
                    correction = json.loads(values["decision"][len("display_name:"):])
                    if not isinstance(correction, dict) or set(correction) != {
                        "expected", "replacement"
                    } or any(
                        not isinstance(value, str) or not clean(value)
                        for value in correction.values()
                    ):
                        raise ValueError("Display correction needs expected and replacement names.")
                    replacement = clean(correction["replacement"])
                    current = connection.execute(
                        "SELECT display_name, name_variants_json FROM person_entities WHERE person_id=?",
                        (values["target_id"],),
                    ).fetchone()
                    if current is None or current["display_name"] not in {
                        correction["expected"], replacement
                    }:
                        raise ValueError("Display correction target does not match its expected name.")
                    variants = sorted(
                        {*json.loads(current["name_variants_json"] or "[]"),
                         correction["expected"], replacement},
                        key=lambda value: (value.casefold(), value),
                    )
                    if current["display_name"] != replacement:
                        connection.execute(
                            """UPDATE person_entities SET display_name=?, normalized_name=?,
                               name_variants_json=?, updated_at=? WHERE person_id=?""",
                            (replacement, name_key(replacement), json.dumps(variants, ensure_ascii=False),
                             utc_now(), values["target_id"]),
                        )
                        applied += 1
                    continue
                prefix = "merge_into:"
                if not values["decision"].startswith(prefix):
                    raise ValueError(
                        f"Unsupported person-entity decision on row {row_number}."
                    )
                applied += _merge_person_entity(
                    connection,
                    superseded_person_id=values["target_id"],
                    canonical_person_id=values["decision"][len(prefix):],
                    decision_id=decision_id,
                    rationale=values["rationale"],
                    reviewer=values["reviewer"],
                    decision_version=values["decision_version"],
                )
    return {
        "rows_read": len(rows),
        "decisions_imported": imported,
        "state_changes_applied": applied,
        "duplicates_skipped": skipped_existing,
    }
