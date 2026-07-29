from __future__ import annotations

import csv
import gzip
import hashlib
import json
import re
import sqlite3
from collections import Counter, defaultdict
from pathlib import Path

from .config import Settings
from .constants import (
    NAMESPACE_GENERIC,
    PUBLIC_DATA_VERSION,
    SOURCE_PDF_URL,
)
from .db import utc_now

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SITE_ROOT = PROJECT_ROOT / "site"
PUBLIC_ROOT = SITE_ROOT / "public"
GENERATED_ROOT = SITE_ROOT / "src" / "data" / "generated"
FULL_SERIAL_RE = re.compile(r"^[A-Z]{0,3}\d{5,10}$")


def mask_serial(value: str | None) -> str | None:
    if not value:
        return None
    suffix = value[-4:] if len(value) >= 4 else value
    return f"••••{suffix}"


def public_source_row(row: sqlite3.Row) -> dict[str, object]:
    return {
        "source_record_id": row["source_record_id"],
        "indexed_last_name": row["last_name_raw"],
        "indexed_first_name": row["first_name_raw"],
        "indexed_middle": row["middle_initial_raw"],
        "rank_as_indexed": row["rank_raw"],
        "serial_masked": mask_serial(row["serial_number_normalized"]),
        "box": row["box_raw"],
        "notes_as_indexed": row["notes_raw"],
        "archive_location": row["archive_location"],
        "pdf_page": row["source_page"],
        "pdf_url": f"{SOURCE_PDF_URL}#page={row['source_page']}",
    }


def _initial(value: str) -> str:
    initial = value[:1].upper()
    return initial if "A" <= initial <= "Z" else "other"


def _write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(value, ensure_ascii=False, separators=(",", ":")) + "\n"
    path.write_text(payload, encoding="utf-8")
    with gzip.open(path.with_suffix(path.suffix + ".gz"), "wb", compresslevel=9) as handle:
        handle.write(payload.encode("utf-8"))


def _write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=fields,
            extrasaction="ignore",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def _write_jsonl(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(
                json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n"
            )


def _published_affiliations(
    connection: sqlite3.Connection,
) -> dict[str, list[dict[str, object]]]:
    result: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in connection.execute(
        """
        SELECT a.*, o.canonical_name, o.historical_name, o.sector,
               o.organization_type, o.country AS organization_country
        FROM affiliations a
        LEFT JOIN organizations o USING(organization_id)
        WHERE a.publication_status IN ('published', 'publish_qualified', 'conflicting')
          AND a.claim_confidence IN ('confirmed', 'high', 'medium', 'conflicting')
        ORDER BY a.person_id, a.immediate_pre_oss DESC,
                 a.last_civilian_pre_service DESC, a.start_date, a.affiliation_id
        """
    ):
        item = {
            "affiliation_id": row["affiliation_id"],
            "organization_id": row["organization_id"],
            "organization_name_as_found": row["organization_name_as_found"],
            "canonical_organization": row["canonical_name"],
            "historical_organization": row["historical_name"],
            "role_title": row["role_title"],
            "occupation": row["occupation"],
            "relationship_type": row["relationship_type"],
            "start_date": row["start_date"],
            "end_date": row["end_date"],
            "date_precision": row["date_precision"],
            "city": row["city"],
            "state_or_region": row["state_or_region"],
            "country": row["country"],
            "immediate_pre_oss": bool(row["immediate_pre_oss"]),
            "last_civilian_pre_service": bool(row["last_civilian_pre_service"]),
            "temporal_basis": row["pre_oss_temporal_basis"],
            "identity_confidence": row["identity_confidence"],
            "claim_confidence": row["claim_confidence"],
            "source_quality": row["source_quality"],
            "publication_status": row["publication_status"],
            "sector": row["sector"],
            "organization_country": row["organization_country"],
        }
        result[row["person_id"]].append(item)
    return result


def _claims_and_sources(
    connection: sqlite3.Connection,
) -> tuple[dict[str, list[dict[str, object]]], list[dict[str, object]]]:
    sources = {
        row["source_id"]: {
            "source_id": row["source_id"],
            "stable_url": row["stable_url"],
            "archival_identifier": row["archival_identifier"],
            "title": row["title"],
            "author_creator": row["author_creator"],
            "repository_publisher": row["repository_publisher"],
            "publication_record_date": row["publication_record_date"],
            "locator": row["locator"],
            "access_date": row["access_date"],
            "source_quality": row["source_quality"],
            "collection_name": row["collection_name"],
            "document_number": row["document_number"],
            "rights_notes": row["rights_notes"],
        }
        for row in connection.execute("SELECT * FROM sources ORDER BY source_id")
    }
    claims: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in connection.execute(
        """
        SELECT * FROM claims
        WHERE publication_status IN ('published', 'publish_qualified', 'conflicting')
          AND claim_confidence IN ('confirmed', 'high', 'medium', 'conflicting')
        ORDER BY person_id, claim_id
        """
    ):
        linked = [
            {
                "source_id": link["source_id"],
                "support_type": link["support_type"],
                "locator_override": link["locator_override"],
                "excerpt_override": link["excerpt_override"],
            }
            for link in connection.execute(
                "SELECT * FROM claim_sources WHERE claim_id = ? ORDER BY source_id",
                (row["claim_id"],),
            )
        ]
        claims[row["person_id"]].append(
            {
                "claim_id": row["claim_id"],
                "affiliation_id": row["affiliation_id"],
                "claim_type": row["claim_type"],
                "claim_text": row["claim_text"],
                "evidence_excerpt": row["evidence_excerpt"],
                "evidence_paraphrase": row["evidence_paraphrase"],
                "identity_match_assessment": row["identity_match_assessment"],
                "temporal_assessment": row["temporal_assessment"],
                "source_quality": row["source_quality"],
                "claim_confidence": row["claim_confidence"],
                "publication_status": row["publication_status"],
                "match_notes": row["match_notes"],
                "sources": linked,
            }
        )
    used_source_ids = {
        link["source_id"]
        for person_claims in claims.values()
        for claim in person_claims
        for link in claim["sources"]
    }
    return claims, [sources[source_id] for source_id in sorted(used_source_ids)]


def build_public_data(
    connection: sqlite3.Connection,
    settings: Settings,
) -> dict[str, object]:
    PUBLIC_ROOT.mkdir(parents=True, exist_ok=True)
    GENERATED_ROOT.mkdir(parents=True, exist_ok=True)
    affiliations = _published_affiliations(connection)
    claims, public_sources = _claims_and_sources(connection)
    source_rows: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in connection.execute(
        """
        SELECT sr.*, psl.person_id
        FROM source_records sr
        JOIN person_source_links psl USING(source_record_id)
        ORDER BY sr.source_page, sr.source_row_number
        """
    ):
        source_rows[row["person_id"]].append(public_source_row(row))

    profiles: list[dict[str, object]] = []
    search_index: list[dict[str, object]] = []
    download_people: list[dict[str, object]] = []
    status_counts: Counter[str] = Counter()
    category_counts: Counter[str] = Counter()
    identity_counts: Counter[str] = Counter()
    officer_counts: Counter[str] = Counter()
    archival_counts: Counter[str] = Counter()
    for person in connection.execute(
        """
        SELECT * FROM person_entities
        WHERE person_id NOT IN (SELECT superseded_person_id FROM entity_supersessions)
        ORDER BY normalized_name, person_id
        """
    ):
        person_affiliations = affiliations.get(person["person_id"], [])
        immediate = [
            item for item in person_affiliations if item["immediate_pre_oss"]
        ]
        last_civilian = [
            item for item in person_affiliations if item["last_civilian_pre_service"]
        ]
        earlier = [
            item
            for item in person_affiliations
            if not item["immediate_pre_oss"] and not item["last_civilian_pre_service"]
        ]
        rows = source_rows.get(person["person_id"], [])
        research_status = person["research_status"]
        if research_status == "not_started":
            status_message = (
                "The documented minimum research protocol has not yet been completed "
                "for this indexed person."
            )
        elif research_status == "no_reliable_result_after_protocol":
            status_message = (
                "No reliable pre-OSS employer has yet been identified in the "
                "accessible sources reviewed."
            )
        elif research_status in {"in_progress", "candidate_found"}:
            status_message = (
                "Research is in progress. Discovery candidates are not presented "
                "as established facts until identity and chronology are reviewed."
            )
        else:
            status_message = person["next_action"] or (
                "This profile remains under documented review."
            )
        profile = {
            "person_id": person["person_id"],
            "display_name": person["display_name"],
            "normalized_name": person["normalized_name"],
            "name_variants": json.loads(person["name_variants_json"] or "[]"),
            "identity_status": person["identity_status"],
            "identity_evidence": person["identity_evidence"],
            "personnel_category": person["personnel_category"],
            "commissioned_officer": (
                None
                if person["commissioned_officer"] is None
                else bool(person["commissioned_officer"])
            ),
            "allied_or_foreign_personnel": (
                None
                if person["allied_or_foreign_personnel"] is None
                else bool(person["allied_or_foreign_personnel"])
            ),
            "possible_duplicate_group": (
                "duplicate-"
                + hashlib.sha256(
                    str(person["possible_duplicate_group"]).encode("utf-8")
                ).hexdigest()[:12]
                if person["possible_duplicate_group"]
                else None
            ),
            "manual_review_required": bool(person["manual_review_required"]),
            "research_status": research_status,
            "research_status_message": status_message,
            "research_attempt_count": person["research_attempt_number"],
            "next_action": person["next_action"],
            "source_records": rows,
            "immediate_pre_oss_affiliations": immediate,
            "last_civilian_pre_service": last_civilian,
            "other_pre_oss_affiliations": earlier,
            "claims": claims.get(person["person_id"], []),
            "archival_file": {
                "indexed": bool(person["personnel_file_indexed"]),
                "digitized": (
                    None
                    if person["personnel_file_digitized"] is None
                    else bool(person["personnel_file_digitized"])
                ),
                "reviewed": bool(person["personnel_file_reviewed"]),
                "box": person["archive_box"],
                "location": person["archive_location"],
                "nara_catalog_id": person["nara_catalog_id"],
                "review_priority": person["archival_review_priority"],
            },
        }
        profiles.append(profile)
        employer_names = sorted(
            {
                str(
                    item["canonical_organization"]
                    or item["organization_name_as_found"]
                    or ""
                )
                for item in person_affiliations
                if item["canonical_organization"]
                or item["organization_name_as_found"]
            }
        )
        sectors = sorted(
            {str(item["sector"]) for item in person_affiliations if item["sector"]}
        )
        countries = sorted(
            {
                str(item["organization_country"] or item["country"])
                for item in person_affiliations
                if item["organization_country"] or item["country"]
            }
        )
        ranks = sorted(
            {
                str(row["rank_as_indexed"])
                for row in rows
                if row["rank_as_indexed"]
            }
        )
        search_index.append(
            {
                "id": person["person_id"],
                "n": person["display_name"],
                "nn": person["normalized_name"],
                "v": profile["name_variants"],
                "e": employer_names,
                "r": ranks,
                "c": person["personnel_category"],
                "o": profile["commissioned_officer"],
                "s": sectors,
                "g": countries,
                "i": person["identity_status"],
                "rs": research_status,
                "ar": person["archival_review_priority"],
                "b": sorted({str(row["box"]) for row in rows if row["box"]}),
            }
        )
        first_source = rows[0] if rows else {}
        download_people.append(
            {
                "person_id": person["person_id"],
                "display_name": person["display_name"],
                "indexed_last_name": first_source.get("indexed_last_name"),
                "indexed_first_name": first_source.get("indexed_first_name"),
                "identity_status": person["identity_status"],
                "personnel_category": person["personnel_category"],
                "commissioned_officer": profile["commissioned_officer"],
                "research_status": research_status,
                "source_record_count": len(rows),
                "source_pdf_page": first_source.get("pdf_page"),
                "box": first_source.get("box"),
                "archive_location": first_source.get("archive_location"),
                "serial_masked": first_source.get("serial_masked"),
            }
        )
        status_counts[research_status] += 1
        category_counts[person["personnel_category"]] += 1
        identity_counts[person["identity_status"]] += 1
        officer_key = (
            "unknown"
            if profile["commissioned_officer"] is None
            else ("commissioned" if profile["commissioned_officer"] else "not_commissioned")
        )
        officer_counts[officer_key] += 1
        archival_counts[person["archival_review_priority"]] += 1

    people_count = len(profiles)
    attempted_people = sum(
        1
        for profile in profiles
        if profile["research_attempt_count"] > 0
    )
    verified_people = sum(
        1
        for profile in profiles
        if profile["immediate_pre_oss_affiliations"]
        or profile["last_civilian_pre_service"]
    )
    archival_assessed = sum(
        1
        for profile in profiles
        if profile["archival_file"]["review_priority"] != "unassessed"
        or profile["archival_file"]["digitized"] is not None
        or profile["archival_file"]["reviewed"]
    )
    source_row_count = sum(len(value) for value in source_rows.values())
    stats = {
        "data_version": PUBLIC_DATA_VERSION,
        "generated_at": utc_now(),
        "title": settings.site_title,
        "subtitle": settings.site_subtitle,
        "source_rows": source_row_count,
        "person_entities": people_count,
        "possible_duplicate_groups": len(
            {
                profile["possible_duplicate_group"]
                for profile in profiles
                if profile["possible_duplicate_group"]
            }
        ),
        "research_attempted_people": attempted_people,
        "research_attempt_percent": round(
            100 * attempted_people / people_count, 4
        ) if people_count else 0,
        "verified_employer_people": verified_people,
        "verified_employer_percent": round(
            100 * verified_people / people_count, 4
        ) if people_count else 0,
        "archival_review_assessed_people": archival_assessed,
        "archival_review_percent": round(
            100 * archival_assessed / people_count, 4
        ) if people_count else 0,
        "research_status_counts": dict(sorted(status_counts.items())),
        "personnel_category_counts": dict(sorted(category_counts.items())),
        "identity_status_counts": dict(sorted(identity_counts.items())),
        "commissioned_status_counts": dict(sorted(officer_counts.items())),
        "archival_review_counts": dict(sorted(archival_counts.items())),
        "published_claims": sum(len(profile["claims"]) for profile in profiles),
        "public_sources": len(public_sources),
        "nara_api_attribution_required": bool(public_sources),
        "analytics_policy": (
            "Default employer analytics count unique person entities with "
            "confirmed or high-confidence published affiliations only."
        ),
    }

    shards: dict[str, list[dict[str, object]]] = defaultdict(list)
    for profile in profiles:
        shards[_initial(str(profile["display_name"]))].append(profile)
    data_root = PUBLIC_ROOT / "data"
    people_root = data_root / "people"
    for key, shard in sorted(shards.items()):
        _write_json(people_root / f"{key.lower()}.json", shard)
    _write_json(data_root / "search-index.json", search_index)
    _write_json(data_root / "stats.json", stats)
    _write_json(data_root / "sources.json", public_sources)

    # Astro's static profile generator reads this build-only copy. It is not a
    # database and is regenerated from SQLite before every production build.
    _write_json(GENERATED_ROOT / "people.json", profiles)
    _write_json(GENERATED_ROOT / "stats.json", stats)
    _write_json(GENERATED_ROOT / "sources.json", public_sources)

    organizations = [
        dict(row)
        for row in connection.execute(
            """
            SELECT o.*,
                   COUNT(DISTINCT a.person_id) AS documented_person_count
            FROM organizations o
            JOIN affiliations a USING(organization_id)
            WHERE a.publication_status IN ('published', 'publish_qualified')
              AND a.claim_confidence IN ('confirmed', 'high', 'medium')
            GROUP BY o.organization_id
            ORDER BY o.canonical_name
            """
        )
    ]
    _write_json(GENERATED_ROOT / "organizations.json", organizations)
    _write_json(data_root / "organizations.json", organizations)

    downloads = PUBLIC_ROOT / "downloads"
    personnel_fields = [
        "person_id", "display_name", "indexed_last_name", "indexed_first_name",
        "identity_status", "personnel_category", "commissioned_officer",
        "research_status", "source_record_count", "source_pdf_page", "box",
        "archive_location", "serial_masked",
    ]
    _write_csv(downloads / "personnel_public.csv", download_people, personnel_fields)
    _write_jsonl(downloads / "personnel_public.jsonl", download_people)
    public_org_rows = [
        {
            key: row.get(key)
            for key in (
                "organization_id", "canonical_name", "historical_name",
                "organization_type", "sector", "city", "state_or_region",
                "country", "active_dates", "normalization_notes",
                "documented_person_count",
            )
        }
        for row in organizations
    ]
    _write_csv(
        downloads / "organizations_public.csv",
        public_org_rows,
        [
            "organization_id", "canonical_name", "historical_name",
            "organization_type", "sector", "city", "state_or_region",
            "country", "active_dates", "normalization_notes",
            "documented_person_count",
        ],
    )
    public_affiliation_rows = [
        {"person_id": person_id, **item}
        for person_id, items in affiliations.items()
        for item in items
    ]
    _write_csv(
        downloads / "affiliations_public.csv",
        public_affiliation_rows,
        [
            "affiliation_id", "person_id", "organization_id",
            "organization_name_as_found", "canonical_organization",
            "role_title", "occupation", "relationship_type", "start_date",
            "end_date", "date_precision", "city", "state_or_region", "country",
            "immediate_pre_oss", "last_civilian_pre_service",
            "temporal_basis", "identity_confidence", "claim_confidence",
            "source_quality", "publication_status", "sector",
        ],
    )
    _write_csv(
        downloads / "sources_public.csv",
        public_sources,
        [
            "source_id", "stable_url", "archival_identifier", "title",
            "author_creator", "repository_publisher",
            "publication_record_date", "locator", "access_date",
            "source_quality", "collection_name", "document_number",
            "rights_notes",
        ],
    )

    # Scan the public projection, not the source database, for forbidden field
    # names and obvious unmasked service-number values.
    serialized = json.dumps(
        {
            "profiles": profiles,
            "search_index": search_index,
            "downloads": download_people,
        },
        ensure_ascii=False,
    )
    forbidden_tokens = [
        "serial_number_raw",
        "serial_number_normalized",
        "raw_row_text",
        "research_notes",
        "last_error",
        "NARA_API_KEY",
        "x-api-key",
    ]
    leaked_tokens = [token for token in forbidden_tokens if token in serialized]
    if leaked_tokens:
        raise ValueError(f"Forbidden public fields detected: {leaked_tokens}")

    manifest_entries = []
    for path in sorted((data_root).rglob("*")) + sorted(downloads.rglob("*")):
        if path.is_file():
            manifest_entries.append(
                {
                    "path": str(path.relative_to(PUBLIC_ROOT)),
                    "size_bytes": path.stat().st_size,
                    "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                }
            )
    manifest = {
        "data_version": PUBLIC_DATA_VERSION,
        "generated_at": stats["generated_at"],
        "source_of_truth": "research/research.sqlite",
        "files": manifest_entries,
        "redaction_checks": {
            "forbidden_field_tokens": leaked_tokens,
            "passed": not leaked_tokens,
        },
    }
    _write_json(data_root / "public_build_manifest.json", manifest)
    return {
        "source_rows": source_row_count,
        "person_entities": people_count,
        "profile_shards": len(shards),
        "search_index_rows": len(search_index),
        "organizations": len(organizations),
        "published_affiliations": len(public_affiliation_rows),
        "published_claims": stats["published_claims"],
        "public_sources": len(public_sources),
        "research_attempted_people": attempted_people,
        "verified_employer_people": verified_people,
        "archival_review_assessed_people": archival_assessed,
        "redaction_checks_passed": not leaked_tokens,
    }
