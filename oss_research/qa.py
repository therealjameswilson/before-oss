from __future__ import annotations

import json
import hashlib
import random
import sqlite3
import statistics
import subprocess
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Callable

from .constants import (
    EXPECTED_SOURCE_ROWS,
    REPORTS_DIR,
    SOURCE_PDF_PAGES,
    TMP_DIR,
)
from .db import integrity_report, utc_now

QA_RANDOM_SEED = 226_224

COMMISSIONED_COMPATIBLE_CATEGORIES = frozenset(
    {
        "commissioned_army_officer",
        "commissioned_coast_guard_officer",
        "commissioned_marine_corps_officer",
        "commissioned_naval_officer",
        "foreign_or_allied_military_personnel",
        "unknown_or_indeterminate",
    }
)


def commissioned_category_is_consistent(
    commissioned_officer: object,
    personnel_category: object,
) -> bool:
    """Allow sourced Allied officers without erasing their foreign category."""
    return (
        commissioned_officer != 1
        or personnel_category in COMMISSIONED_COMPATIBLE_CATEGORIES
    )


def selected_pages(
    page_counts: dict[int, int],
    warning_pages: set[int],
) -> dict[int, list[str]]:
    reasons: dict[int, list[str]] = {}

    def add(page: int, reason: str) -> None:
        reasons.setdefault(page, []).append(reason)

    for page in range(1, 6):
        add(page, "first_five")
    for page in range(260, 265):
        add(page, "middle_five")
    for page in range(SOURCE_PDF_PAGES - 4, SOURCE_PDF_PAGES + 1):
        add(page, "final_five")

    fixed = set(reasons)
    candidates = [page for page in range(1, SOURCE_PDF_PAGES + 1) if page not in fixed]
    rng = random.Random(QA_RANDOM_SEED)
    for page in sorted(rng.sample(candidates, 50)):
        add(page, "deterministic_random_50")

    for page in sorted(warning_pages):
        add(page, "parser_warning")

    counts = list(page_counts.values())
    median = statistics.median(counts)
    deviations = [abs(count - median) for count in counts]
    mad = statistics.median(deviations)
    lower = median - max(3 * mad, 3)
    upper = median + max(3 * mad, 3)
    for page, count in page_counts.items():
        if count < lower or count > upper:
            add(page, f"row_count_anomaly:{count}")
    # The short final page is structurally expected but still selected.
    return reasons


def render_pages(pdf_path: Path, pages: list[int], output_dir: Path) -> list[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)

    def render_one(page: int) -> Path:
        prefix = output_dir / f"page-{page:03d}"
        output = prefix.with_suffix(".png")
        if output.exists() and output.stat().st_size > 0:
            return output
        command = [
            "pdftoppm",
            "-f",
            str(page),
            "-l",
            str(page),
            "-singlefile",
            "-png",
            "-r",
            "110",
            str(pdf_path),
            str(prefix),
        ]
        subprocess.run(command, check=True, capture_output=True)
        return output

    # Four local Poppler workers keep the validation run short while remaining
    # bounded and deterministic. Existing page images are valid checkpoints.
    with ThreadPoolExecutor(max_workers=4) as executor:
        return list(executor.map(render_one, pages))


def validate_ingest(
    connection: sqlite3.Connection,
    pdf_path: Path,
    *,
    render_selected: bool = False,
) -> dict[str, object]:
    total = connection.execute("SELECT COUNT(*) FROM source_records").fetchone()[0]
    page_rows = list(
        connection.execute(
            """
            SELECT source_page, COUNT(*) AS row_count,
                   SUM(requires_visual_review) AS warning_rows
            FROM source_records
            GROUP BY source_page
            ORDER BY source_page
            """
        )
    )
    page_counts = {row["source_page"]: row["row_count"] for row in page_rows}
    warning_pages = {
        row["source_page"] for row in page_rows if row["warning_rows"]
    }
    warnings = list(
        connection.execute(
            """
            SELECT source_page, source_row_number, source_record_id,
                   raw_row_text, parser_confidence
            FROM source_records
            WHERE requires_visual_review = 1
            ORDER BY source_page, source_row_number
            """
        )
    )
    reasons = selected_pages(page_counts, warning_pages)
    render_dir = TMP_DIR / "pdfs" / "parser-qa"
    rendered: list[Path] = []
    if render_selected:
        rendered = render_pages(pdf_path, sorted(reasons), render_dir)

    with connection:
        for page, selection_reasons in reasons.items():
            image_path = (
                str(render_dir / f"page-{page:03d}.png")
                if render_selected
                else None
            )
            connection.execute(
                """
                UPDATE page_qa
                SET selection_reason = ?,
                    rendered_image_path = COALESCE(?, rendered_image_path),
                    visual_review_status = CASE
                        WHEN visual_review_status = 'not_selected' THEN 'selected'
                        ELSE visual_review_status
                    END
                WHERE source_page = ?
                """,
                (";".join(selection_reasons), image_path, page),
            )

    initials = Counter()
    for row in connection.execute("SELECT last_name_raw FROM source_records"):
        initial = (row["last_name_raw"][:1] or "?").upper()
        initials[initial] += 1
    category_counts = {
        row["personnel_category"]: row["count"]
        for row in connection.execute(
            """
            SELECT personnel_category, COUNT(*) AS count
            FROM source_records
            GROUP BY personnel_category
            ORDER BY personnel_category
            """
        )
    }
    integrity = integrity_report(connection)
    review_status_counts = {
        row["visual_review_status"]: row["count"]
        for row in connection.execute(
            """
            SELECT visual_review_status, COUNT(*) AS count
            FROM page_qa
            GROUP BY visual_review_status
            ORDER BY visual_review_status
            """
        )
    }
    source_review_status_counts = {
        row["visual_review_status"]: row["count"]
        for row in connection.execute(
            """
            SELECT visual_review_status, COUNT(*) AS count
            FROM source_records
            GROUP BY visual_review_status
            ORDER BY visual_review_status
            """
        )
    }
    checks = {
        "exact_source_row_count": total == EXPECTED_SOURCE_ROWS,
        "all_pdf_pages_represented": len(page_counts) == SOURCE_PDF_PAGES,
        "all_rows_have_location": connection.execute(
            "SELECT COUNT(*) FROM source_records WHERE archive_location IS NULL OR archive_location = ''"
        ).fetchone()[0]
        == 0,
        "unique_page_row_coordinates": connection.execute(
            """
            SELECT COUNT(*) FROM (
                SELECT source_page, source_row_number, COUNT(*) AS n
                FROM source_records
                GROUP BY source_page, source_row_number
                HAVING n > 1
            )
            """
        ).fetchone()[0]
        == 0,
        "sqlite_integrity": integrity["quick_check"] == "ok"
        and integrity["foreign_key_error_count"] == 0,
        "all_selected_pages_visually_reviewed": connection.execute(
            """
            SELECT COUNT(*) FROM page_qa
            WHERE selection_reason IS NOT NULL
              AND visual_review_status NOT IN (
                  'reviewed_matches', 'reviewed_after_correction'
              )
            """
        ).fetchone()[0]
        == 0,
        "all_warning_rows_visually_resolved": connection.execute(
            """
            SELECT COUNT(*) FROM source_records
            WHERE requires_visual_review = 1
              AND visual_review_status NOT IN (
                  'reviewed_matches', 'reviewed_corrected'
              )
            """
        ).fetchone()[0]
        == 0,
    }
    audit = {
        "generated_at": utc_now(),
        "expected_source_rows": EXPECTED_SOURCE_ROWS,
        "actual_source_rows": total,
        "expected_pages": SOURCE_PDF_PAGES,
        "pages_represented": len(page_counts),
        "page_row_counts": page_counts,
        "initial_counts": dict(sorted(initials.items())),
        "category_counts": category_counts,
        "warning_row_count": len(warnings),
        "warning_rows": [dict(row) for row in warnings],
        "selected_visual_qa_page_count": len(reasons),
        "selected_visual_qa_pages": {
            str(page): page_reasons for page, page_reasons in sorted(reasons.items())
        },
        "rendered_page_count": len(rendered),
        "visual_review_status_counts": review_status_counts,
        "source_record_visual_review_status_counts": source_review_status_counts,
        "checks": checks,
        "integrity": integrity,
    }
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    (REPORTS_DIR / "parser_qa.json").write_text(
        json.dumps(audit, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    lines = [
        "# Parser QA",
        "",
        f"Generated: {audit['generated_at']}",
        "",
        "## Gate summary",
        "",
        f"- Source rows: **{total:,}** of **{EXPECTED_SOURCE_ROWS:,}** expected.",
        f"- PDF pages represented: **{len(page_counts)}** of **{SOURCE_PDF_PAGES}**.",
        f"- Parser-warning rows: **{len(warnings):,}**.",
        f"- Pages selected for visual QA: **{len(reasons):,}**.",
        f"- Page images rendered in this run: **{len(rendered):,}**.",
        f"- Pages visually reviewed as matching: "
        f"**{review_status_counts.get('reviewed_matches', 0):,}**.",
        f"- Pages visually reviewed after a normalized-field correction: "
        f"**{review_status_counts.get('reviewed_after_correction', 0):,}**.",
        f"- Parser-warning rows visually reviewed and corrected: "
        f"**{source_review_status_counts.get('reviewed_corrected', 0):,}**.",
        "",
        "## Automated checks",
        "",
    ]
    lines.extend(
        f"- {'PASS' if passed else 'FAIL'} - `{name}`"
        for name, passed in checks.items()
    )
    lines.extend(
        [
            "",
            "## Page row-count distribution",
            "",
            f"- Minimum: {min(page_counts.values())}",
            f"- Median: {statistics.median(page_counts.values())}",
            f"- Maximum: {max(page_counts.values())}",
            "",
            "The final page contains 12 rows and is expected to be shorter. "
            "Visual selection does not itself mark a page as reviewed.",
            "",
            "## Visual QA selection",
            "",
            ", ".join(str(page) for page in sorted(reasons)),
            "",
        ]
    )
    (REPORTS_DIR / "parser_qa.md").write_text(
        "\n".join(lines), encoding="utf-8"
    )
    return audit


def audit_profiles(
    connection: sqlite3.Connection,
    *,
    sample_size: int = 200,
) -> dict[str, object]:
    """Run a deterministic, stratified data-integrity audit of public profiles."""
    if sample_size < 200:
        raise ValueError("The publication audit requires at least 200 profiles.")
    people = [
        dict(row)
        for row in connection.execute(
            """
            SELECT pe.*, q.research_status AS queue_status,
                   COUNT(psl.source_record_id) AS source_record_count,
                   MIN(sr.first_name_raw) AS indexed_first_name,
                   SUM(CASE
                       WHEN sr.first_name_raw IS NULL
                         OR length(replace(sr.first_name_raw, '.', '')) <= 1
                       THEN 1 ELSE 0 END) AS incomplete_name_rows
            FROM person_entities pe
            JOIN research_queue q USING(person_id)
            JOIN person_source_links psl USING(person_id)
            JOIN source_records sr USING(source_record_id)
            GROUP BY pe.person_id
            ORDER BY pe.person_id
            """
        )
    ]
    for person in people:
        person["_order"] = hashlib.sha256(
            f"profile-audit-v2:{person['person_id']}".encode()
        ).hexdigest()

    published_claim_rows = list(
        connection.execute(
            """
            SELECT DISTINCT person_id, claim_confidence
            FROM claims
            WHERE publication_status IN (
                'publish_qualified', 'published', 'conflicting'
            )
            """
        )
    )
    claim_people_by_confidence = {
        confidence: {
            str(row["person_id"])
            for row in published_claim_rows
            if row["claim_confidence"] == confidence
        }
        for confidence in (
            "confirmed",
            "high",
            "medium",
            "low",
            "unresolved",
            "conflicting",
        )
    }
    confirmed_or_high_claim_people = (
        claim_people_by_confidence["confirmed"]
        | claim_people_by_confidence["high"]
    )
    medium_claim_people = claim_people_by_confidence["medium"]
    conflicting_claim_people = claim_people_by_confidence["conflicting"]

    selected: dict[str, dict[str, object]] = {}

    def take(
        predicate: Callable[[dict[str, object]], bool], target: int
    ) -> None:
        candidates = sorted(
            (person for person in people if predicate(person)),
            key=lambda item: str(item["_order"]),
        )
        for person in candidates:
            if len([item for item in selected.values() if predicate(item)]) >= target:
                break
            selected[str(person["person_id"])] = person

    for category in sorted({str(person["personnel_category"]) for person in people}):
        take(lambda person, category=category: person["personnel_category"] == category, 4)
    for tier in range(1, 5):
        take(lambda person, tier=tier: int(person["difficulty_tier"]) == tier, 25)
    take(lambda person: person["commissioned_officer"] == 1, 25)
    take(
        lambda person: person["personnel_category"]
        == "civilian_professional_or_administrative_grade",
        20,
    )
    take(
        lambda person: str(person["personnel_category"]).startswith("enlisted_"),
        20,
    )
    take(lambda person: person["allied_or_foreign_personnel"] == 1, 20)
    take(lambda person: int(person["incomplete_name_rows"]) > 0, 20)
    take(lambda person: person["possible_duplicate_group"] is not None, 30)
    take(lambda person: person["identity_status"] == "high_confidence", 20)
    take(
        lambda person: str(person["person_id"])
        in confirmed_or_high_claim_people,
        min(10, len(confirmed_or_high_claim_people)),
    )
    take(
        lambda person: str(person["person_id"]) in medium_claim_people,
        min(10, len(medium_claim_people)),
    )
    take(
        lambda person: str(person["person_id"]) in conflicting_claim_people,
        min(10, len(conflicting_claim_people)),
    )
    take(lambda person: person["identity_status"] == "unresolved", 25)
    for person in sorted(people, key=lambda item: str(item["_order"])):
        if len(selected) >= sample_size:
            break
        selected[str(person["person_id"])] = person
    selected_rows = list(selected.values())[:sample_size]

    public_ids = {
        row["person_id"]
        for row in connection.execute(
            """
            SELECT person_id FROM person_entities
            WHERE person_id NOT IN (
                SELECT superseded_person_id FROM entity_supersessions
            )
            """
        )
    }
    checks = {
        "sample_size_at_least_200": len(selected_rows) >= 200,
        "every_profile_has_source_row": all(
            int(person["source_record_count"]) >= 1 for person in selected_rows
        ),
        "every_profile_in_public_projection": all(
            person["person_id"] in public_ids for person in selected_rows
        ),
        "identity_evidence_present": all(
            bool(person["identity_evidence"]) for person in selected_rows
        ),
        "queue_status_synchronized": all(
            person["research_status"] == person["queue_status"]
            for person in selected_rows
        ),
        "duplicate_groups_require_manual_review": all(
            person["possible_duplicate_group"] is None
            or person["manual_review_required"] == 1
            for person in selected_rows
        ),
        "commissioned_categories_consistent": all(
            commissioned_category_is_consistent(
                person["commissioned_officer"],
                person["personnel_category"],
            )
            for person in selected_rows
        ),
    }
    category_counts = Counter(
        str(person["personnel_category"]) for person in selected_rows
    )
    tier_counts = Counter(int(person["difficulty_tier"]) for person in selected_rows)
    identity_counts = Counter(str(person["identity_status"]) for person in selected_rows)
    research_counts = Counter(str(person["research_status"]) for person in selected_rows)
    special_counts = {
        "commissioned": sum(
            person["commissioned_officer"] == 1 for person in selected_rows
        ),
        "civilian": sum(
            person["personnel_category"]
            == "civilian_professional_or_administrative_grade"
            for person in selected_rows
        ),
        "enlisted": sum(
            str(person["personnel_category"]).startswith("enlisted_")
            for person in selected_rows
        ),
        "allied_or_foreign": sum(
            person["allied_or_foreign_personnel"] == 1
            for person in selected_rows
        ),
        "incomplete_or_initial_only_name": sum(
            int(person["incomplete_name_rows"]) > 0 for person in selected_rows
        ),
        "possible_duplicate_group": sum(
            person["possible_duplicate_group"] is not None
            for person in selected_rows
        ),
        "confirmed_or_high_published_claim": sum(
            str(person["person_id"]) in confirmed_or_high_claim_people
            for person in selected_rows
        ),
        "medium_published_claim": sum(
            str(person["person_id"]) in medium_claim_people
            for person in selected_rows
        ),
        "conflicting_published_claim": sum(
            str(person["person_id"]) in conflicting_claim_people
            for person in selected_rows
        ),
        "unresolved_identity": sum(
            person["identity_status"] == "unresolved"
            for person in selected_rows
        ),
    }
    unavailable_strata = {
        "women": (
            "The index has no sex/gender field; the project does not infer gender "
            "from names. This stratum requires sourced identity research."
        ),
    }
    if not confirmed_or_high_claim_people:
        unavailable_strata["confirmed_or_high_claims"] = (
            "No confirmed or high-confidence published claim currently exists."
        )
    if not medium_claim_people:
        unavailable_strata["medium_claims"] = (
            "No medium-confidence published claim currently exists."
        )
    if not conflicting_claim_people:
        unavailable_strata["conflicting_claims"] = (
            "No conflicting published claim currently exists."
        )
    audit = {
        "generated_at": utc_now(),
        "selection_version": "profile-audit-v2",
        "sample_size": len(selected_rows),
        "checks": checks,
        "personnel_category_counts": dict(sorted(category_counts.items())),
        "difficulty_tier_counts": dict(sorted(tier_counts.items())),
        "identity_status_counts": dict(sorted(identity_counts.items())),
        "research_status_counts": dict(sorted(research_counts.items())),
        "special_strata_counts": special_counts,
        "unavailable_strata": unavailable_strata,
        "sample_person_ids": [person["person_id"] for person in selected_rows],
    }
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    (REPORTS_DIR / "profile_audit.json").write_text(
        json.dumps(audit, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    lines = [
        "# Stratified profile audit",
        "",
        f"Generated: {audit['generated_at']}",
        "",
        f"Deterministic profiles audited: **{len(selected_rows):,}**.",
        "",
        "## Checks",
        "",
    ]
    lines.extend(
        f"- {'PASS' if passed else 'FAIL'} - `{name}`"
        for name, passed in checks.items()
    )
    lines.extend(["", "## Special strata represented", ""])
    lines.extend(
        f"- {label.replace('_', ' ')}: {count:,}"
        for label, count in special_counts.items()
    )
    lines.extend(["", "## Evidence-limited strata", ""])
    lines.extend(f"- {label}: {note}" for label, note in unavailable_strata.items())
    lines.extend(
        [
            "",
            "This is a data-integrity and publication-boundary audit, not a claim "
            "that the sampled people have completed historical research.",
            "",
        ]
    )
    (REPORTS_DIR / "profile_audit.md").write_text(
        "\n".join(lines), encoding="utf-8"
    )
    return audit
