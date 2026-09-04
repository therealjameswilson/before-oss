from __future__ import annotations

import csv
import json
import sqlite3
from pathlib import Path

from .constants import DERIVED_DIR, REPORTS_DIR
from .db import utc_now
from .analytics import VERIFIED_SQL


def _write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=fieldnames,
            extrasaction="ignore",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def _write_jsonl(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def _query_dicts(connection: sqlite3.Connection, sql: str) -> list[dict[str, object]]:
    return [dict(row) for row in connection.execute(sql)]


def export_derived(connection: sqlite3.Connection) -> dict[str, int]:
    source_rows = _query_dicts(
        connection,
        "SELECT * FROM source_records ORDER BY source_page, source_row_number",
    )
    source_fields = list(source_rows[0]) if source_rows else []
    _write_csv(DERIVED_DIR / "personnel_source_rows.csv", source_fields, source_rows)
    _write_jsonl(DERIVED_DIR / "personnel_source_rows.jsonl", source_rows)

    people = _query_dicts(
        connection,
        "SELECT * FROM person_entities ORDER BY normalized_name, person_id",
    )
    _write_csv(
        DERIVED_DIR / "person_entities.csv",
        list(people[0]) if people else [
            "person_id", "display_name", "identity_status", "research_status"
        ],
        people,
    )
    supersessions = _query_dicts(
        connection,
        """
        SELECT * FROM entity_supersessions
        ORDER BY canonical_person_id, superseded_person_id
        """,
    )
    _write_csv(
        DERIVED_DIR / "entity_supersessions.csv",
        list(supersessions[0]) if supersessions else [
            "superseded_person_id", "canonical_person_id", "decision_id",
            "reason", "created_at"
        ],
        supersessions,
    )
    organizations = _query_dicts(
        connection,
        "SELECT * FROM organizations ORDER BY canonical_name, organization_id",
    )
    _write_csv(
        DERIVED_DIR / "organizations.csv",
        list(organizations[0]) if organizations else [
            "organization_id", "canonical_name", "historical_name", "sector"
        ],
        organizations,
    )
    affiliations = _query_dicts(
        connection,
        "SELECT * FROM affiliations ORDER BY person_id, affiliation_id",
    )
    _write_csv(
        DERIVED_DIR / "affiliations.csv",
        list(affiliations[0]) if affiliations else [
            "affiliation_id", "person_id", "organization_id",
            "relationship_type", "immediate_pre_oss",
            "last_civilian_pre_service", "claim_confidence"
        ],
        affiliations,
    )
    sources = _query_dicts(
        connection,
        "SELECT * FROM sources ORDER BY repository_publisher, title, source_id",
    )
    _write_csv(
        DERIVED_DIR / "sources.csv",
        list(sources[0]) if sources else [
            "source_id", "stable_url", "archival_identifier", "title",
            "repository_publisher", "access_date", "source_quality"
        ],
        sources,
    )
    unresolved = _query_dicts(
        connection,
        """
        SELECT person_id, display_name, normalized_name, identity_status,
               research_status, next_action, archival_review_priority,
               archive_box, archive_location
        FROM person_entities
        WHERE person_id NOT IN (
              SELECT superseded_person_id FROM entity_supersessions
          )
          AND (
            identity_status IN ('ambiguous', 'conflicting', 'unresolved')
            OR research_status IN (
               'not_started', 'in_progress', 'needs_identity_review',
               'needs_temporal_review', 'conflicting_sources',
               'no_reliable_result_after_protocol', 'blocked_by_source_access',
               'requires_archival_review'
            )
          )
        ORDER BY normalized_name, person_id
        """,
    )
    _write_csv(
        DERIVED_DIR / "unresolved.csv",
        list(unresolved[0]) if unresolved else [
            "person_id", "display_name", "identity_status", "research_status"
        ],
        unresolved,
    )
    pull_list = _query_dicts(
        connection,
        """
        SELECT sr.source_record_id,
               pe.person_id,
               sr.display_name AS indexed_name,
               sr.name_variants_json AS name_variants,
               sr.source_page,
               sr.box_raw AS box,
               sr.archive_location,
               CASE
                   WHEN pe.research_status = 'not_started'
                       THEN 'No documented research protocol has yet been completed.'
                   WHEN pe.research_status = 'no_reliable_result_after_protocol'
                       THEN 'No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.'
                   ELSE COALESCE(pe.next_action, 'Identity or temporal evidence requires review.')
               END AS unresolved_research_question,
               'The indexed personnel file may contain recruitment or prior-affiliation evidence unavailable online.'
                   AS why_physical_file_is_needed,
               pe.research_status,
               pe.archival_review_priority AS priority
        FROM source_records sr
        JOIN person_source_links psl ON psl.source_record_id = sr.source_record_id
        JOIN person_entities pe ON pe.person_id = psl.person_id
        WHERE pe.personnel_file_reviewed = 0
          AND pe.research_status NOT IN ('verified_employer_found')
        ORDER BY sr.archive_location, CAST(sr.box_raw AS INTEGER),
                 sr.last_name_raw, sr.first_name_raw, sr.source_page, sr.source_row_number
        """,
    )
    _write_csv(
        DERIVED_DIR / "nara_pull_list.csv",
        list(pull_list[0]) if pull_list else [
            "source_record_id", "person_id", "indexed_name", "source_page",
            "box", "archive_location", "unresolved_research_question",
            "why_physical_file_is_needed", "research_status", "priority"
        ],
        pull_list,
    )
    review_queue = _query_dicts(
        connection,
        """
        SELECT q.person_id, pe.display_name, pe.identity_status,
               pe.personnel_category, pe.commissioned_officer,
               q.difficulty_tier, q.priority, q.research_status,
               q.protocol_version, q.next_action
        FROM research_queue q
        JOIN person_entities pe USING(person_id)
        ORDER BY q.research_status, q.priority, pe.normalized_name, q.person_id
        """,
    )
    _write_csv(
        Path("research/review_queue.csv"),
        list(review_queue[0]) if review_queue else [
            "person_id", "display_name", "identity_status", "research_status"
        ],
        review_queue,
    )
    attempts = _query_dicts(
        connection,
        "SELECT * FROM research_attempts ORDER BY started_at, research_attempt_id",
    )
    _write_csv(
        Path("research/research_attempts.csv"),
        list(attempts[0]) if attempts else [
            "research_attempt_id", "person_id", "source_adapter", "query_text",
            "started_at", "completed_at", "outcome", "rejection_reasons"
        ],
        attempts,
    )
    return {
        "source_rows": len(source_rows),
        "person_entities": len(people),
        "active_person_entities": len(people) - len(supersessions),
        "superseded_person_entities": len(supersessions),
        "organizations": len(organizations),
        "affiliations": len(affiliations),
        "sources": len(sources),
        "unresolved": len(unresolved),
        "nara_pull_list_rows": len(pull_list),
        "review_queue_rows": len(review_queue),
        "research_attempts": len(attempts),
    }


def coverage_report(connection: sqlite3.Connection) -> dict[str, object]:
    scalar = lambda sql: connection.execute(sql).fetchone()[0]
    source_rows = scalar("SELECT COUNT(*) FROM source_records")
    stored_people = scalar("SELECT COUNT(*) FROM person_entities")
    superseded_people = scalar("SELECT COUNT(*) FROM entity_supersessions")
    people = scalar(
        """
        SELECT COUNT(*) FROM person_entities pe
        WHERE NOT EXISTS (
            SELECT 1 FROM entity_supersessions es
            WHERE es.superseded_person_id = pe.person_id
        )
        """
    )
    linked_rows = scalar(
        "SELECT COUNT(DISTINCT source_record_id) FROM person_source_links"
    )
    attempted_people = scalar(
        """
        SELECT COUNT(DISTINCT ra.person_id)
        FROM research_attempts ra
        JOIN person_entities pe ON pe.person_id = ra.person_id
        WHERE ra.outcome NOT IN ('planned', 'skipped_budget')
          AND NOT EXISTS (
              SELECT 1 FROM entity_supersessions es
              WHERE es.superseded_person_id = pe.person_id
          )
        """
    )
    verified_affiliation_people = scalar(
        f"""
        SELECT COUNT(DISTINCT a.person_id)
        FROM affiliations a
        JOIN person_entities pe ON pe.person_id = a.person_id
        WHERE {VERIFIED_SQL}
          AND NOT EXISTS (
              SELECT 1 FROM entity_supersessions es
              WHERE es.superseded_person_id = pe.person_id
          )
        """
    )
    verified_employer_people = scalar(
        f"""
        SELECT COUNT(DISTINCT a.person_id)
        FROM affiliations a
        JOIN person_entities pe ON pe.person_id = a.person_id
        WHERE {VERIFIED_SQL}
          AND a.relationship_type IN ('employment', 'self_employment')
          AND NOT EXISTS (
              SELECT 1 FROM entity_supersessions es
              WHERE es.superseded_person_id = pe.person_id
          )
        """
    )
    archival_assessed = scalar(
        """
        SELECT COUNT(*) FROM person_entities pe
        WHERE (
              pe.archival_review_priority <> 'unassessed'
              OR pe.personnel_file_digitized IS NOT NULL
              OR pe.personnel_file_reviewed = 1
          )
          AND NOT EXISTS (
              SELECT 1 FROM entity_supersessions es
              WHERE es.superseded_person_id = pe.person_id
          )
        """
    )
    status_counts = {
        row["research_status"]: row["count"]
        for row in connection.execute(
            """
            SELECT research_status, COUNT(*) AS count
            FROM person_entities pe
            WHERE NOT EXISTS (
                SELECT 1 FROM entity_supersessions es
                WHERE es.superseded_person_id = pe.person_id
            )
            GROUP BY research_status
            ORDER BY research_status
            """
        )
    }
    claim_counts = {
        row["claim_confidence"]: row["count"]
        for row in connection.execute(
            """
            SELECT claim_confidence, COUNT(*) AS count
            FROM claims c
            JOIN person_entities pe ON pe.person_id = c.person_id
            WHERE NOT EXISTS (
                SELECT 1 FROM entity_supersessions es
                WHERE es.superseded_person_id = pe.person_id
            )
            GROUP BY claim_confidence
            ORDER BY claim_confidence
            """
        )
    }
    category_counts = {
        row["personnel_category"]: row["count"]
        for row in connection.execute(
            """
            SELECT personnel_category, COUNT(*) AS count
            FROM person_entities pe
            WHERE NOT EXISTS (
                SELECT 1 FROM entity_supersessions es
                WHERE es.superseded_person_id = pe.person_id
            )
            GROUP BY personnel_category
            ORDER BY personnel_category
            """
        )
    }
    report = {
        "generated_at": utc_now(),
        "index_coverage": {
            "source_rows": source_rows,
            "source_rows_linked": linked_rows,
            "percent_linked": round(100 * linked_rows / source_rows, 4)
            if source_rows
            else 0,
        },
        "research_attempt_coverage": {
            "person_entities": people,
            "stored_person_entities": stored_people,
            "superseded_person_entities": superseded_people,
            "people_with_nonplanned_attempts": attempted_people,
            "percent": round(100 * attempted_people / people, 4) if people else 0,
        },
        "verified_affiliation_coverage": {
            "person_entities": people,
            "people_with_confirmed_or_high_published_affiliation":
                verified_affiliation_people,
            "percent": round(
                100 * verified_affiliation_people / people, 4
            ) if people else 0,
        },
        "verified_employer_coverage": {
            "person_entities": people,
            "people_with_confirmed_or_high_published_employer":
                verified_employer_people,
            "percent": round(
                100 * verified_employer_people / people, 4
            ) if people else 0,
        },
        "archival_review_coverage": {
            "person_entities": people,
            "people_assessed": archival_assessed,
            "percent": round(100 * archival_assessed / people, 4) if people else 0,
        },
        "research_status_counts": status_counts,
        "claim_confidence_counts": claim_counts,
        "personnel_category_counts": category_counts,
        "possible_duplicate_groups": scalar(
            """
            SELECT COUNT(DISTINCT possible_duplicate_group)
            FROM person_entities pe
            WHERE pe.possible_duplicate_group IS NOT NULL
              AND NOT EXISTS (
                  SELECT 1 FROM entity_supersessions es
                  WHERE es.superseded_person_id = pe.person_id
              )
            """
        ),
        "conflict_count": scalar(
            """
            SELECT COUNT(*) FROM person_entities pe
            WHERE (
                  pe.identity_status = 'conflicting'
                  OR pe.research_status = 'conflicting_sources'
              )
              AND NOT EXISTS (
                  SELECT 1 FROM entity_supersessions es
                  WHERE es.superseded_person_id = pe.person_id
              )
            """
        ),
        "citations": scalar("SELECT COUNT(*) FROM sources"),
        "unique_source_documents": scalar(
            """
            SELECT COUNT(*) FROM (
                SELECT COALESCE(archival_identifier, stable_url) AS document_key
                FROM sources
                GROUP BY document_key
            )
            """
        ),
    }
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    (REPORTS_DIR / "research_coverage.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    lines = [
        "# Research coverage",
        "",
        f"Generated: {report['generated_at']}",
        "",
        "## Distinct coverage measures",
        "",
        f"- Index coverage: **{linked_rows:,} / {source_rows:,}** source rows linked "
        f"({report['index_coverage']['percent_linked']:.4f}%).",
        f"- Research-attempt coverage: **{attempted_people:,} / {people:,}** people "
        f"({report['research_attempt_coverage']['percent']:.4f}%).",
        f"- Verified-affiliation coverage: "
        f"**{verified_affiliation_people:,} / {people:,}** people "
        f"({report['verified_affiliation_coverage']['percent']:.4f}%).",
        f"- Verified-employer coverage: "
        f"**{verified_employer_people:,} / {people:,}** people "
        f"({report['verified_employer_coverage']['percent']:.4f}%).",
        f"- Archival-review coverage: **{archival_assessed:,} / {people:,}** people "
        f"({report['archival_review_coverage']['percent']:.4f}%).",
        "",
        "Automated extraction and identity-queue creation do not count as a "
        "historical research attempt.",
        "",
        "## Research statuses",
        "",
    ]
    lines.extend(f"- `{key}`: {value:,}" for key, value in status_counts.items())
    lines.extend(["", "## Claim confidence", ""])
    if claim_counts:
        lines.extend(f"- `{key}`: {value:,}" for key, value in claim_counts.items())
    else:
        lines.append("- No affiliation claims have yet passed into the claims table.")
    lines.append("")
    (REPORTS_DIR / "research_coverage.md").write_text(
        "\n".join(lines), encoding="utf-8"
    )
    identity_status_counts = {
        row["identity_status"]: row["count"]
        for row in connection.execute(
            """
            SELECT identity_status, COUNT(*) AS count
            FROM person_entities pe
            WHERE NOT EXISTS (
                SELECT 1 FROM entity_supersessions es
                WHERE es.superseded_person_id = pe.person_id
            )
            GROUP BY identity_status
            ORDER BY identity_status
            """
        )
    }
    link_status_counts = {
        row["link_status"]: row["count"]
        for row in connection.execute(
            """
            SELECT link_status, COUNT(*) AS count
            FROM person_source_links
            GROUP BY link_status
            ORDER BY link_status
            """
        )
    }
    entity_audit = {
        "generated_at": report["generated_at"],
        "source_rows": source_rows,
        "person_entities": people,
        "stored_person_entities": stored_people,
        "superseded_person_entities": superseded_people,
        "source_rows_linked": linked_rows,
        "identity_status_counts": identity_status_counts,
        "link_status_counts": link_status_counts,
        "automatic_same_name_same_service_number_groups": scalar(
            """
            SELECT COUNT(*) FROM person_entities
            WHERE identity_status = 'high_confidence'
              AND identity_evidence LIKE 'Automatically linked%'
              AND person_id NOT IN (
                  SELECT superseded_person_id FROM entity_supersessions
              )
            """
        ),
        "possible_duplicate_groups": report["possible_duplicate_groups"],
        "same_service_number_different_name_groups": scalar(
            """
            SELECT COUNT(DISTINCT candidate_label)
            FROM candidate_matches cm
            WHERE cm.candidate_type = 'duplicate_person'
              AND cm.candidate_label LIKE 'serial-conflict:%'
              AND cm.match_assessment IN (
                  'unreviewed', 'plausible', 'probable', 'conflicting'
              )
              AND cm.person_id NOT IN (
                  SELECT superseded_person_id FROM entity_supersessions
              )
            """
        ),
        "entities_requiring_manual_review": scalar(
            """
            SELECT COUNT(*) FROM person_entities
            WHERE manual_review_required = 1
              AND person_id NOT IN (
                  SELECT superseded_person_id FROM entity_supersessions
              )
            """
        ),
        "checks": {
            "all_source_rows_linked": linked_rows == source_rows,
            "no_name_only_automatic_merges": scalar(
                """
                SELECT COUNT(*) FROM person_entities
                WHERE identity_status = 'high_confidence'
                  AND identity_evidence LIKE 'Automatically linked%'
                  AND identity_evidence NOT LIKE
                      '%same non-empty service number%'
                  AND person_id NOT IN (
                      SELECT superseded_person_id FROM entity_supersessions
                  )
                """
            )
            == 0,
            "all_duplicate_groups_require_review": scalar(
                """
                SELECT COUNT(*) FROM person_entities
                WHERE possible_duplicate_group IS NOT NULL
                  AND manual_review_required <> 1
                  AND person_id NOT IN (
                      SELECT superseded_person_id FROM entity_supersessions
                  )
                """
            )
            == 0,
        },
    }
    (REPORTS_DIR / "entity_resolution_qa.json").write_text(
        json.dumps(entity_audit, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    entity_lines = [
        "# Entity-resolution QA",
        "",
        f"Generated: {entity_audit['generated_at']}",
        "",
        f"- Source rows: **{source_rows:,}**.",
        f"- Cautious person entities: **{people:,}**.",
        f"- Superseded person entities retained for audit: "
        f"**{superseded_people:,}** of **{stored_people:,}** stored rows.",
        f"- Source rows linked: **{linked_rows:,}**.",
        f"- Narrow automatic same-name/same-service-number groups: "
        f"**{entity_audit['automatic_same_name_same_service_number_groups']:,}**.",
        f"- Possible duplicate groups: **{entity_audit['possible_duplicate_groups']:,}**.",
        f"- Same-service-number/different-name groups: "
        f"**{entity_audit['same_service_number_different_name_groups']:,}**.",
        f"- Entities requiring manual review: "
        f"**{entity_audit['entities_requiring_manual_review']:,}**.",
        "",
        "## Checks",
        "",
    ]
    entity_lines.extend(
        f"- {'PASS' if passed else 'FAIL'} - `{name}`"
        for name, passed in entity_audit["checks"].items()
    )
    entity_lines.extend(
        [
            "",
            "Exact normalized names alone never trigger an automatic merge. "
            "Identical printed service numbers attached to different names remain "
            "separate review candidates.",
            "",
        ]
    )
    (REPORTS_DIR / "entity_resolution_qa.md").write_text(
        "\n".join(entity_lines), encoding="utf-8"
    )
    return report
