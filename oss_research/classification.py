from __future__ import annotations

import sqlite3

from .db import utc_now
from .normalize import classify_personnel


UNKNOWN = "unknown_or_indeterminate"
OBSOLETE_NOTE = (
    "Printed rank or grade is preserved but not classified by the current rule set."
)
REFRESHED_NOTE = "Printed rank or grade classified by a later explicit normalization rule."


def refresh_unknown_classifications(
    connection: sqlite3.Connection, *, dry_run: bool = False
) -> dict[str, int | bool]:
    """Upgrade only newly recognizable ranks; never overwrite reviewed categories.

    Printed cells, source IDs, identity statuses, and manually assigned person
    categories are unchanged. This is safe to rerun after a rank-rule update.
    """
    source_updates: list[tuple[str, str, int | None, int | None, str | None, str]] = []
    person_updates: dict[str, tuple[str, int | None, int | None]] = {}
    for row in connection.execute(
        """
        SELECT source_record_id, rank_raw, notes_raw, personnel_category,
               normalization_notes
        FROM source_records
        WHERE personnel_category = ? AND rank_raw IS NOT NULL
        ORDER BY source_page, source_row_number
        """,
        (UNKNOWN,),
    ):
        classification = classify_personnel(row["rank_raw"], row["notes_raw"])
        if classification.category == UNKNOWN:
            continue
        note = row["normalization_notes"] or ""
        if OBSOLETE_NOTE in note:
            note = note.replace(OBSOLETE_NOTE, REFRESHED_NOTE)
        elif REFRESHED_NOTE not in note:
            note = f"{note} {REFRESHED_NOTE}".strip()
        source_updates.append(
            (
                row["source_record_id"],
                classification.category,
                classification.commissioned_officer,
                classification.allied_or_foreign,
                note,
                classification.rank_normalized,
            )
        )
        links = list(
            connection.execute(
                "SELECT person_id FROM person_source_links WHERE source_record_id = ?",
                (row["source_record_id"],),
            )
        )
        if len(links) != 1:
            continue
        person_id = str(links[0]["person_id"])
        person = connection.execute(
            """
            SELECT personnel_category,
                   (SELECT COUNT(*) FROM person_source_links WHERE person_id = ?) AS linked_rows
            FROM person_entities WHERE person_id = ?
            """,
            (person_id, person_id),
        ).fetchone()
        if person and person["personnel_category"] == UNKNOWN and person["linked_rows"] == 1:
            person_updates[person_id] = (
                classification.category,
                classification.commissioned_officer,
                classification.allied_or_foreign,
            )

    if not dry_run:
        with connection:
            connection.executemany(
                """
                UPDATE source_records
                SET personnel_category = ?, commissioned_officer = ?,
                    allied_or_foreign_personnel = ?, normalization_notes = ?,
                    rank_normalized = ?
                WHERE source_record_id = ? AND personnel_category = ?
                """,
                [
                    (category, officer, foreign, note, rank, record_id, UNKNOWN)
                    for record_id, category, officer, foreign, note, rank in source_updates
                ],
            )
            now = utc_now()
            connection.executemany(
                """
                UPDATE person_entities
                SET personnel_category = ?, commissioned_officer = ?,
                    allied_or_foreign_personnel = ?, updated_at = ?
                WHERE person_id = ? AND personnel_category = ?
                """,
                [
                    (category, officer, foreign, now, person_id, UNKNOWN)
                    for person_id, (category, officer, foreign) in person_updates.items()
                ],
            )
    return {
        "dry_run": dry_run,
        "source_rows_reclassified": len(source_updates),
        "person_entities_reclassified": len(person_updates),
    }
