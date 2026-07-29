from __future__ import annotations

import json
import sqlite3
import uuid
from collections import Counter, defaultdict

from .constants import (
    IDENTITY_VERSION,
    NAMESPACE_PERSON,
    RESEARCH_PROTOCOL_VERSION,
)
from .db import utc_now

PERSON_NAMESPACE = uuid.UUID(NAMESPACE_PERSON)
COMMON_SURNAMES = {
    "ADAMS", "ALLEN", "ANDERSON", "BAKER", "BROWN", "CAMPBELL", "CARTER",
    "CLARK", "DAVIS", "EVANS", "GARCIA", "GREEN", "HALL", "HARRIS",
    "HILL", "JACKSON", "JOHNSON", "JONES", "KING", "LEE", "LEWIS",
    "MARTIN", "MILLER", "MOORE", "MORGAN", "MORRIS", "MURPHY", "NELSON",
    "PARKER", "ROBINSON", "ROGERS", "ROSS", "SCOTT", "SMITH", "STEWART",
    "TAYLOR", "THOMAS", "THOMPSON", "TURNER", "WALKER", "WHITE",
    "WILLIAMS", "WILSON", "WRIGHT", "YOUNG",
}


def _difficulty(row: sqlite3.Row, name_frequency: int) -> int:
    first = (row["first_name"] or "").strip()
    last_key = (row["last_name"] or "").upper()
    if not first or len(first.replace(".", "")) <= 1:
        return 4
    if row["allied_or_foreign_personnel"]:
        return 4
    if last_key in COMMON_SURNAMES or name_frequency >= 4:
        return 3
    if row["serial_number_normalized"]:
        return 1 if name_frequency == 1 else 2
    return 2


def build_identities(connection: sqlite3.Connection) -> dict[str, int]:
    rows = list(
        connection.execute(
            """
            SELECT * FROM source_records
            ORDER BY source_page, source_row_number
            """
        )
    )
    name_counts = Counter(row["normalized_name"] for row in rows)

    # The only automatic merge rule requires both an exact normalized indexed
    # name and the same non-empty service number.
    groups: dict[tuple[str, ...], list[sqlite3.Row]] = defaultdict(list)
    for row in rows:
        serial = row["serial_number_normalized"]
        if serial:
            key = ("name_serial", row["normalized_name"], serial)
        else:
            key = ("source_row", row["source_record_id"])
        groups[key].append(row)

    now = utc_now()
    people_created = 0
    rows_linked = 0
    auto_merged_rows = 0
    duplicate_groups = 0
    with connection:
        for key, members in sorted(groups.items(), key=lambda item: item[0]):
            seed = min(member["source_record_id"] for member in members)
            person_id = str(uuid.uuid5(PERSON_NAMESPACE, seed))
            exemplar = members[0]
            is_merge = len(members) > 1
            if is_merge:
                duplicate_groups += 1
                auto_merged_rows += len(members) - 1
            difficulty = _difficulty(
                exemplar, name_counts[exemplar["normalized_name"]]
            )
            identity_status = "high_confidence" if is_merge else "unresolved"
            identity_evidence = (
                "Automatically linked because the printed rows share an exact "
                "normalized indexed name and the same non-empty service number."
                if is_merge
                else "Initial one-row entity; no external identity resolution has been accepted."
            )
            categories = {member["personnel_category"] for member in members}
            category = (
                next(iter(categories))
                if len(categories) == 1
                else "unknown_or_indeterminate"
            )
            officer_values = {
                member["commissioned_officer"]
                for member in members
                if member["commissioned_officer"] is not None
            }
            commissioned = (
                next(iter(officer_values)) if len(officer_values) == 1 else None
            )
            allied_values = {
                member["allied_or_foreign_personnel"]
                for member in members
                if member["allied_or_foreign_personnel"] is not None
            }
            allied = next(iter(allied_values)) if len(allied_values) == 1 else None
            duplicate_group = f"auto:{person_id}" if is_merge else None
            connection.execute(
                """
                INSERT INTO person_entities(
                    person_id, display_name, normalized_name, identity_status,
                    identity_evidence, name_variants_json, personnel_category,
                    commissioned_officer, allied_or_foreign_personnel,
                    difficulty_tier, manual_review_required,
                    possible_duplicate_group, research_status,
                    personnel_file_indexed, archive_box, archive_location,
                    archival_review_priority, created_at, updated_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'not_started',
                          1, ?, ?, 'unassessed', ?, ?)
                ON CONFLICT(person_id) DO UPDATE SET
                    display_name=excluded.display_name,
                    normalized_name=excluded.normalized_name,
                    identity_status=excluded.identity_status,
                    identity_evidence=excluded.identity_evidence,
                    personnel_category=excluded.personnel_category,
                    commissioned_officer=excluded.commissioned_officer,
                    allied_or_foreign_personnel=excluded.allied_or_foreign_personnel,
                    difficulty_tier=excluded.difficulty_tier,
                    possible_duplicate_group=excluded.possible_duplicate_group,
                    archive_box=excluded.archive_box,
                    archive_location=excluded.archive_location,
                    updated_at=excluded.updated_at
                """,
                (
                    person_id,
                    exemplar["display_name"],
                    exemplar["normalized_name"],
                    identity_status,
                    identity_evidence,
                    exemplar["name_variants_json"],
                    category,
                    commissioned,
                    allied,
                    difficulty,
                    1,
                    duplicate_group,
                    exemplar["box_raw"],
                    exemplar["archive_location"],
                    now,
                    now,
                ),
            )
            people_created += 1
            connection.execute(
                """
                INSERT INTO research_queue(
                    person_id, priority, difficulty_tier, research_status,
                    protocol_version, updated_at
                ) VALUES (?, ?, ?, 'not_started', ?, ?)
                ON CONFLICT(person_id) DO UPDATE SET
                    priority=excluded.priority,
                    difficulty_tier=excluded.difficulty_tier,
                    protocol_version=excluded.protocol_version,
                    updated_at=excluded.updated_at
                """,
                (person_id, difficulty * 100, difficulty, RESEARCH_PROTOCOL_VERSION, now),
            )
            for member in members:
                link_status = "high_confidence" if is_merge else "unresolved"
                connection.execute(
                    """
                    INSERT INTO person_source_links(
                        person_id, source_record_id, link_status, evidence,
                        algorithm_version, manual_review_required, created_at
                    ) VALUES (?, ?, ?, ?, ?, 1, ?)
                    ON CONFLICT(person_id, source_record_id) DO UPDATE SET
                        link_status=excluded.link_status,
                        evidence=excluded.evidence,
                        algorithm_version=excluded.algorithm_version
                    """,
                    (
                        person_id,
                        member["source_record_id"],
                        link_status,
                        identity_evidence,
                        IDENTITY_VERSION,
                        now,
                    ),
                )
                connection.execute(
                    """
                    UPDATE source_records
                    SET entity_resolution_status = ?,
                        entity_resolution_evidence = ?
                    WHERE source_record_id = ?
                    """,
                    (
                        "linked" if is_merge else "manual_review_required",
                        identity_evidence,
                        member["source_record_id"],
                    ),
                )
                rows_linked += 1

        # Similar rows with the same service number but different normalized
        # names are candidates only; they are never automatically merged.
        serial_groups: dict[str, list[sqlite3.Row]] = defaultdict(list)
        for row in rows:
            if row["serial_number_normalized"]:
                serial_groups[row["serial_number_normalized"]].append(row)
        for serial, members in serial_groups.items():
            names = {member["normalized_name"] for member in members}
            if len(names) <= 1:
                continue
            candidate_group = f"serial-conflict:{serial}"
            person_ids = []
            for member in members:
                link = connection.execute(
                    "SELECT person_id FROM person_source_links WHERE source_record_id = ?",
                    (member["source_record_id"],),
                ).fetchone()
                if link:
                    person_ids.append(link["person_id"])
                    connection.execute(
                        """
                        UPDATE person_entities
                        SET possible_duplicate_group = ?,
                            manual_review_required = 1,
                            updated_at = ?
                        WHERE person_id = ?
                        """,
                        (candidate_group, now, link["person_id"]),
                    )
                    connection.execute(
                        """
                        UPDATE source_records
                        SET entity_resolution_status = 'possible_duplicate_group',
                            entity_resolution_evidence = ?
                        WHERE source_record_id = ?
                        """,
                        (
                            "Same printed service number appears with a different "
                            "normalized name; manual review is required.",
                            member["source_record_id"],
                        ),
                    )
            for person_id in sorted(set(person_ids)):
                candidate_id = str(
                    uuid.uuid5(
                        PERSON_NAMESPACE,
                        f"candidate:{candidate_group}:{person_id}",
                    )
                )
                connection.execute(
                    """
                    INSERT INTO candidate_matches(
                        candidate_match_id, person_id, candidate_type,
                        candidate_label, candidate_identifier, evidence_json,
                        match_assessment, created_at, updated_at
                    ) VALUES (?, ?, 'duplicate_person', ?, ?, ?, 'unreviewed', ?, ?)
                    ON CONFLICT(candidate_match_id) DO UPDATE SET
                        evidence_json=excluded.evidence_json,
                        updated_at=excluded.updated_at
                    """,
                    (
                        candidate_id,
                        person_id,
                        candidate_group,
                        serial,
                        json.dumps(
                            {
                                "service_number": serial,
                                "indexed_names": sorted(names),
                                "rule": "same_serial_different_name_never_auto_merge",
                            }
                        ),
                        now,
                        now,
                    ),
                )

    return {
        "source_rows": len(rows),
        "person_entities": people_created,
        "source_rows_linked": rows_linked,
        "automatic_duplicate_groups": duplicate_groups,
        "automatic_merged_rows": auto_merged_rows,
    }
