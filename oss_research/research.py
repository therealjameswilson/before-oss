from __future__ import annotations

import hashlib
import json
import re
import sqlite3
import uuid
from collections import Counter, defaultdict
from dataclasses import dataclass

from . import __version__
from .config import Settings
from .constants import NAMESPACE_GENERIC, RESEARCH_PROTOCOL_VERSION
from .db import utc_now
from .sources.army_bulk import ARMY_BULK_URL
from .sources.loc import LocAdapter
from .sources.nara import NaraAdapter
from .sources.cia import CiaAdapter
from .sources.web import WebDiscoveryAdapter

GENERIC_NAMESPACE = uuid.UUID(NAMESPACE_GENERIC)
PILOT_SEED = "before-oss-pilot-v1"


def _order_key(person_id: str) -> str:
    return hashlib.sha256(f"{PILOT_SEED}:{person_id}".encode()).hexdigest()


def assign_page_batch(
    connection: sqlite3.Connection,
    *,
    batch_name: str,
    source_page: int,
    first_row: int,
    last_row: int,
) -> dict[str, object]:
    """Assign a complete printed row range to a resumable research batch.

    A source row may link to a superseded entity, so research its reviewed
    canonical person. Existing assignments outside this exact cohort are not
    displaced. Repeating the same command is idempotent.
    """
    if not re.fullmatch(r"[a-z][a-z0-9_-]{0,63}", batch_name):
        raise ValueError("Batch name must be a short lowercase slug.")
    if source_page < 1 or first_row < 1 or last_row < first_row:
        raise ValueError("Page and row numbers must be positive and ordered.")
    if last_row - first_row + 1 > 100:
        raise ValueError("Page batches are bounded to at most 100 printed rows.")

    rows = list(
        connection.execute(
            """
            SELECT s.source_row_number,
                   COALESCE(es.canonical_person_id, l.person_id) AS person_id
            FROM source_records s
            LEFT JOIN person_source_links l USING(source_record_id)
            LEFT JOIN entity_supersessions es
              ON es.superseded_person_id = l.person_id
            WHERE s.source_page = ? AND s.source_row_number BETWEEN ? AND ?
            ORDER BY s.source_row_number, person_id
            """,
            (source_page, first_row, last_row),
        )
    )
    found_rows = {row["source_row_number"] for row in rows}
    missing_rows = sorted(set(range(first_row, last_row + 1)) - found_rows)
    if missing_rows:
        raise ValueError(
            f"Page {source_page} has no printed source row(s) {missing_rows}."
        )
    unlinked_rows = sorted(
        {row["source_row_number"] for row in rows if row["person_id"] is None}
    )
    if unlinked_rows:
        raise ValueError(
            f"Page {source_page} has unlinked source row(s) {unlinked_rows}."
        )
    person_ids = sorted({row["person_id"] for row in rows})
    assigned = {
        row["person_id"]: row["assigned_batch"]
        for row in connection.execute(
            "SELECT person_id, assigned_batch FROM research_queue"
        )
    }
    missing_people = sorted(set(person_ids) - set(assigned))
    if missing_people:
        raise ValueError(f"Person(s) missing from research queue: {missing_people}.")
    conflicting_people = [
        person_id
        for person_id in person_ids
        if assigned[person_id] not in (None, batch_name)
    ]
    if conflicting_people:
        raise ValueError(
            f"Person(s) already assigned to another batch: {conflicting_people}."
        )
    other_members = sorted(
        person_id
        for person_id, assigned_batch in assigned.items()
        if assigned_batch == batch_name and person_id not in person_ids
    )
    if other_members:
        raise ValueError(
            f"Batch name already contains person(s) outside this row range: {other_members}."
        )

    now = utc_now()
    with connection:
        connection.executemany(
            """
            UPDATE research_queue
            SET assigned_batch = ?, protocol_version = ?, updated_at = ?
            WHERE person_id = ? AND assigned_batch IS NULL
            """,
            (
                (batch_name, RESEARCH_PROTOCOL_VERSION, now, person_id)
                for person_id in person_ids
            ),
        )
    return {
        "batch_name": batch_name,
        "source_page": source_page,
        "first_row": first_row,
        "last_row": last_row,
        "source_rows": len(found_rows),
        "person_entities": len(person_ids),
        "newly_assigned_people": sum(assigned[person_id] is None for person_id in person_ids),
        "person_ids": person_ids,
    }


def create_stratified_pilot(
    connection: sqlite3.Connection,
    *,
    size: int = 75,
    batch_name: str = "pilot-v1",
) -> dict[str, object]:
    if size < 8:
        raise ValueError("Pilot size must be at least 8 to cover categories and tiers.")
    people = [dict(row) for row in connection.execute(
        """
        SELECT person_id, display_name, personnel_category, difficulty_tier,
               commissioned_officer
        FROM person_entities
        ORDER BY person_id
        """
    )]
    for person in people:
        person["_order"] = _order_key(str(person["person_id"]))
    by_category: dict[str, list[dict[str, object]]] = defaultdict(list)
    by_tier: dict[int, list[dict[str, object]]] = defaultdict(list)
    for person in people:
        by_category[str(person["personnel_category"])].append(person)
        by_tier[int(person["difficulty_tier"])].append(person)
    for values in (*by_category.values(), *by_tier.values()):
        values.sort(key=lambda item: str(item["_order"]))

    selected: dict[str, dict[str, object]] = {}
    # Guarantee representation for every populated personnel category.
    for category in sorted(by_category):
        for person in by_category[category][: min(2, len(by_category[category]))]:
            selected[str(person["person_id"])] = person
    # Guarantee meaningful representation from every difficulty tier.
    tier_target = max(8, size // 5)
    for tier in range(1, 5):
        for person in by_tier[tier]:
            if len([p for p in selected.values() if p["difficulty_tier"] == tier]) >= tier_target:
                break
            selected[str(person["person_id"])] = person
    # Fill deterministically across the full population.
    for person in sorted(people, key=lambda item: str(item["_order"])):
        if len(selected) >= size:
            break
        selected[str(person["person_id"])] = person
    if len(selected) != size:
        raise ValueError(f"Could select only {len(selected)} of {size} pilot people.")

    now = utc_now()
    with connection:
        connection.execute(
            "UPDATE research_queue SET assigned_batch = NULL WHERE assigned_batch = ?",
            (batch_name,),
        )
        for person_id in selected:
            connection.execute(
                """
                UPDATE research_queue
                SET assigned_batch = ?, priority = MIN(priority, 10),
                    protocol_version = ?, updated_at = ?
                WHERE person_id = ?
                """,
                (batch_name, RESEARCH_PROTOCOL_VERSION, now, person_id),
            )
    category_counts = Counter(
        str(person["personnel_category"]) for person in selected.values()
    )
    tier_counts = Counter(int(person["difficulty_tier"]) for person in selected.values())
    return {
        "batch_name": batch_name,
        "size": len(selected),
        "personnel_category_counts": dict(sorted(category_counts.items())),
        "difficulty_tier_counts": dict(sorted(tier_counts.items())),
        "selection_seed": PILOT_SEED,
    }


def query_families(person: sqlite3.Row) -> dict[str, list[str]]:
    name = person["display_name"]
    rank = person["rank_normalized"]
    serial = person["serial_number_normalized"]
    exact = [
        f'"{name}" "Office of Strategic Services"',
        f'"{name}" OSS',
    ]
    employment = [
        f'"{name}" employer 1940',
        f'"{name}" occupation 1940',
    ]
    official = [
        f'"{name}" "Office of Strategic Services"',
    ]
    if rank:
        exact.append(f'"{name}" "{rank}" OSS')
    if serial:
        official.append(f'"{name}" "{serial}"')
    return {
        "official": official,
        "exact_oss": exact,
        "employment": employment,
        "institutional": [f'"{name}" obituary', f'"{name}" biography'],
    }


def source_query_options(
    source: str,
    families: dict[str, list[str]],
) -> list[tuple[str, str]]:
    family_order = {
        "nara": ["official"],
        "cia": ["exact_oss"],
        "loc": ["employment", "institutional"],
        "web": ["exact_oss", "employment", "institutional"],
    }[source]
    options: list[tuple[str, str]] = []
    seen: set[str] = set()
    for family in family_order:
        for query in families[family]:
            if query in seen:
                continue
            seen.add(query)
            options.append((family, query))
    return options


def candidate_aware_status(
    candidate_count: int,
    has_unreviewed_candidates: bool,
) -> tuple[str, str, str]:
    if candidate_count or has_unreviewed_candidates:
        return (
            "candidate_found",
            "Review discovery candidates for identity and temporal relevance.",
            "Review source candidates.",
        )
    return (
        "in_progress",
        "Continue the minimum research protocol with the next source family.",
        "Continue staged research.",
    )


def discovery_outcome(
    *, planned: bool, http_status: int | None, candidate_count: int
) -> str:
    if planned:
        return "planned"
    if http_status != 200:
        return "blocked"
    return "candidate_found" if candidate_count else "no_result"


def has_unreviewed_research_candidate(
    connection: sqlite3.Connection,
    person_id: str,
) -> bool:
    return bool(
        connection.execute(
            """
            SELECT 1
            FROM candidate_matches
            WHERE person_id = ?
              AND candidate_type <> 'duplicate_person'
              AND NOT (candidate_type = 'identity' AND candidate_url = ?)
              AND match_assessment = 'unreviewed'
            LIMIT 1
            """,
            (person_id, ARMY_BULK_URL),
        ).fetchone()
    )


def record_discovery_progress(
    connection: sqlite3.Connection,
    *,
    person_id: str,
    candidate_count: int,
    has_unreviewed_candidates: bool,
) -> None:
    """Count a source check without replacing a reviewed research disposition.

    Only the three automatically managed discovery states may move to another
    discovery state. A later search is supplementary evidence, not a reason
    to erase a human-reviewed employer, archival, conflict, or access outcome.
    """
    next_status, person_action, queue_action = candidate_aware_status(
        candidate_count, has_unreviewed_candidates
    )
    now = utc_now()
    connection.execute(
        """
        UPDATE person_entities
        SET research_started_at = COALESCE(research_started_at, ?),
            research_attempt_number = research_attempt_number + 1,
            updated_at = ?
        WHERE person_id = ?
        """,
        (now, now, person_id),
    )
    connection.execute(
        """
        UPDATE person_entities
        SET research_status = ?, next_action = ?, research_agent_version = ?
        WHERE person_id = ?
          AND research_status IN ('not_started', 'in_progress', 'candidate_found')
        """,
        (next_status, person_action, f"before-oss/{__version__}", person_id),
    )
    connection.execute(
        """
        UPDATE research_queue
        SET attempts = attempts + 1, updated_at = ?
        WHERE person_id = ?
        """,
        (now, person_id),
    )
    connection.execute(
        """
        UPDATE research_queue
        SET research_status = ?, next_action = ?
        WHERE person_id = ?
          AND research_status IN ('not_started', 'in_progress', 'candidate_found')
        """,
        (next_status, queue_action, person_id),
    )


def _attempt(
    connection: sqlite3.Connection,
    *,
    person_id: str,
    source: str,
    query: str,
    query_variant_type: str,
    fingerprint: str,
    outcome: str,
    notes: str,
    attempt_number: int,
) -> None:
    attempt_id = str(
        uuid.uuid5(
            GENERIC_NAMESPACE,
            f"attempt:{source}:{person_id}:{fingerprint}",
        )
    )
    now = utc_now()
    connection.execute(
        """
        INSERT INTO research_attempts(
            research_attempt_id, person_id, source_adapter, query_text,
            query_variant_type, request_fingerprint, started_at, completed_at, outcome,
            sources_reviewed, candidate_sources_rejected, research_notes,
            attempt_number, research_agent_version
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 0, 0, ?, ?, ?)
        ON CONFLICT(research_attempt_id) DO UPDATE SET
            completed_at=excluded.completed_at,
            outcome=excluded.outcome,
            research_notes=excluded.research_notes
        """,
        (
            attempt_id,
            person_id,
            source,
            query,
            query_variant_type,
            fingerprint,
            now,
            now,
            outcome,
            notes,
            attempt_number,
            f"before-oss/{__version__}",
        ),
    )


def run_research(
    connection: sqlite3.Connection,
    settings: Settings,
    *,
    source: str,
    max_queries: int,
    person_id: str | None = None,
    batch: str | None = None,
    dry_run: bool = False,
) -> dict[str, object]:
    if max_queries <= 0:
        raise ValueError("--max-queries must be positive")
    where = ["1=1"]
    params: list[object] = []
    if person_id:
        where.append("pe.person_id = ?")
        params.append(person_id)
    if batch:
        where.append("q.assigned_batch = ?")
        params.append(batch)
    if settings.research_scope == "commissioned_officers":
        where.append("pe.commissioned_officer = 1")
    people = list(
        connection.execute(
            f"""
            SELECT pe.*, sr.rank_normalized, sr.serial_number_normalized,
                   q.assigned_batch
            FROM person_entities pe
            JOIN research_queue q USING(person_id)
            JOIN person_source_links psl USING(person_id)
            JOIN source_records sr USING(source_record_id)
            WHERE {' AND '.join(where)}
            GROUP BY pe.person_id
            ORDER BY q.priority, pe.difficulty_tier, pe.normalized_name, pe.person_id
            """,
            params,
        )
    )
    adapter: object
    if source == "nara":
        adapter = NaraAdapter(connection, settings)
    elif source == "cia":
        adapter = CiaAdapter(connection, settings)
    elif source == "loc":
        adapter = LocAdapter(connection, settings)
    elif source == "web":
        adapter = WebDiscoveryAdapter(connection, settings)
    else:
        raise ValueError(f"Unsupported research source: {source}")

    planned = searched = blocked = duplicates = candidates = errors = 0
    processed_people: set[str] = set()
    for person in people:
        if planned + searched >= max_queries:
            break
        person_id_value = person["person_id"]
        families = query_families(person)
        try:
            selected: tuple[
                str, str, bool, int, str, int | None
            ] | None = None
            for query_variant_type, query in source_query_options(source, families):
                if source == "nara":
                    result = adapter.search(
                        query, person_id=person_id_value, dry_run=dry_run
                    )
                    is_planned = result.planned
                    is_duplicate = result.duplicate_request
                    candidate_count = len(result.candidate_naids)
                    fingerprint = result.fingerprint
                    status = result.http_status
                else:
                    result = adapter.search(
                        query, person_id=person_id_value, dry_run=dry_run
                    )
                    is_planned = bool(result["planned"])
                    is_duplicate = bool(result["duplicate_request"])
                    candidate_count = int(result["candidate_count"])
                    fingerprint = str(result["fingerprint"])
                    status = result["http_status"]
                if is_duplicate:
                    duplicates += 1
                    continue
                selected = (
                    query_variant_type,
                    query,
                    is_planned,
                    candidate_count,
                    fingerprint,
                    status,
                )
                break
            if selected is None:
                continue
            (
                query_variant_type,
                query,
                is_planned,
                candidate_count,
                fingerprint,
                status,
            ) = selected
            outcome = discovery_outcome(
                planned=is_planned,
                http_status=status,
                candidate_count=candidate_count,
            )
            notes = (
                "Dry-run query plan; no request was made."
                if is_planned
                else (
                    f"HTTP {status}; {candidate_count} unreviewed discovery candidates."
                    if status == 200
                    else f"HTTP {status}; no usable source response, so this is not a negative search result."
                )
            )
            attempt_number = connection.execute(
                "SELECT COUNT(*) + 1 FROM research_attempts WHERE person_id = ?",
                (person_id_value,),
            ).fetchone()[0]
            with connection:
                _attempt(
                    connection,
                    person_id=person_id_value,
                    source=source,
                    query=query,
                    query_variant_type=query_variant_type,
                    fingerprint=fingerprint,
                    outcome=outcome,
                    notes=notes,
                    attempt_number=attempt_number,
                )
                if not is_planned:
                    has_unreviewed_candidates = has_unreviewed_research_candidate(
                        connection,
                        person_id_value,
                    )
                    record_discovery_progress(
                        connection,
                        person_id=person_id_value,
                        candidate_count=candidate_count,
                        has_unreviewed_candidates=has_unreviewed_candidates,
                    )
            if is_planned:
                planned += 1
            else:
                searched += 1
                processed_people.add(person_id_value)
                candidates += candidate_count
                if outcome == "blocked":
                    blocked += 1
                    # A restricted or unavailable source must not be probed
                    # for every subsequent person in the same batch.
                    break
        except Exception:
            errors += 1
            raise
    return {
        "source": source,
        "scope": settings.research_scope,
        "batch": batch,
        "dry_run": dry_run,
        "max_queries": max_queries,
        "queries_planned": planned,
        "queries_searched": searched,
        "queries_blocked": blocked,
        "duplicate_queries_skipped": duplicates,
        "candidate_matches_created_or_seen": candidates,
        "people_with_live_attempts_this_run": len(processed_people),
        "errors": errors,
    }
