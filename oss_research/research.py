from __future__ import annotations

import hashlib
import json
import sqlite3
import uuid
from collections import Counter, defaultdict
from dataclasses import dataclass

from . import __version__
from .config import Settings
from .constants import NAMESPACE_GENERIC, RESEARCH_PROTOCOL_VERSION
from .db import utc_now
from .sources.loc import LocAdapter
from .sources.nara import NaraAdapter
from .sources.cia import CiaAdapter
from .sources.web import WebDiscoveryAdapter

GENERIC_NAMESPACE = uuid.UUID(NAMESPACE_GENERIC)
PILOT_SEED = "before-oss-pilot-v1"


def _order_key(person_id: str) -> str:
    return hashlib.sha256(f"{PILOT_SEED}:{person_id}".encode()).hexdigest()


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


def _attempt(
    connection: sqlite3.Connection,
    *,
    person_id: str,
    source: str,
    query: str,
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
            request_fingerprint, started_at, completed_at, outcome,
            sources_reviewed, candidate_sources_rejected, research_notes,
            attempt_number, research_agent_version
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, 0, 0, ?, ?, ?)
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

    planned = searched = duplicates = candidates = errors = 0
    processed_people: set[str] = set()
    for person in people:
        if planned + searched >= max_queries:
            break
        person_id_value = person["person_id"]
        families = query_families(person)
        query = (
            families["official"][0]
            if source in {"nara", "cia"}
            else families["employment"][0]
        )
        try:
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
            outcome = "planned" if is_planned else (
                "candidate_found" if candidate_count else "no_result"
            )
            notes = (
                "Dry-run query plan; no request was made."
                if is_planned
                else f"HTTP {status}; {candidate_count} unreviewed discovery candidates."
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
                    fingerprint=fingerprint,
                    outcome=outcome,
                    notes=notes,
                    attempt_number=attempt_number,
                )
                if not is_planned:
                    connection.execute(
                        """
                        UPDATE person_entities
                        SET research_status = ?,
                            research_started_at = COALESCE(research_started_at, ?),
                            research_attempt_number = research_attempt_number + 1,
                            next_action = ?,
                            research_agent_version = ?,
                            updated_at = ?
                        WHERE person_id = ?
                        """,
                        (
                            "candidate_found" if candidate_count else "in_progress",
                            utc_now(),
                            (
                                "Review discovery candidates for identity and temporal relevance."
                                if candidate_count
                                else "Continue the minimum research protocol with the next source family."
                            ),
                            f"before-oss/{__version__}",
                            utc_now(),
                            person_id_value,
                        ),
                    )
                    connection.execute(
                        """
                        UPDATE research_queue
                        SET research_status = ?, attempts = attempts + 1,
                            next_action = ?, updated_at = ?
                        WHERE person_id = ?
                        """,
                        (
                            "candidate_found" if candidate_count else "in_progress",
                            (
                                "Review source candidates."
                                if candidate_count
                                else "Continue staged research."
                            ),
                            utc_now(),
                            person_id_value,
                        ),
                    )
            if is_planned:
                planned += 1
            else:
                searched += 1
                processed_people.add(person_id_value)
                candidates += candidate_count
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
        "duplicate_queries_skipped": duplicates,
        "candidate_matches_created_or_seen": candidates,
        "people_with_live_attempts_this_run": len(processed_people),
        "errors": errors,
    }
