#!/usr/bin/env python3
"""Generate the reviewed Batch 998 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page489-walsh-to-walters-"
    "review_batch-998_2026-11-03.json"
)

INDEX = "nara-index-b998"
ARMY = "army-bulk-b998"
TECH = "army-tech-b998"
CODES = "army-codes-b998"

PEOPLE = {
    24: ("7cd40e3d-ac07-53f3-8b80-fdb080abceaa", "James B Walsh"),
    25: ("772b3d25-d931-5153-98fe-a1ee4520f0ab", "James D Walsh"),
    26: ("f638258e-9f5c-5f06-99b3-74ef48e97b12", "John P Walsh"),
    27: ("6b456d9c-a880-5fd9-9e5d-da6b29010d3a", "Louis A Walsh Jr."),
    28: ("d15a6330-2faf-5646-89b2-5d920fbca282", "Lucille B Walsh"),
    29: ("64fe3e00-3f9e-5099-bbd1-9dabcbf2927f", "Margaret E Walsh"),
    30: ("e797ac78-524c-56b1-b3b6-112cdc16ec6e", "Matilda R Walsh"),
    31: ("14cc594d-8688-582b-a27c-15abc92eb2e4", "Richard L Walsh"),
    32: ("43acb70c-ea97-50c1-99c2-a601293edf7f", "Richard T Walsh"),
    33: ("dd9f8589-bfab-5ccf-b508-b50229125541", "Rutherford T Walsh"),
    34: ("2e043a99-db2d-5b34-83f7-37b9ae5caef8", "Thomas J Walsh Jr."),
    35: ("642c272e-ce42-5107-af8b-10083c4c9895", "William B Walsh"),
    36: ("669746fa-822a-5727-8db0-712f2e89e03e", "William F Walsh"),
    37: ("5fc300b8-b79a-51a9-847e-374fb4c46b27", "Edmond S Walstrum"),
    38: ("79f14b4c-3d29-58a8-b3eb-2359bc3ce576", "Austin Walter"),
    39: ("36cb5e40-f961-5f47-88fe-d15c8415e92a", "Billy H Walter"),
    40: ("8dc18e64-594e-5505-9aef-86095e0fb0e1", "Hugh T Walter"),
    41: ("bf349e30-514b-547c-96fd-1a4d749e796f", "Martin J Walter"),
    42: ("a8aa7172-f03d-5a7b-94a3-8a220bbcf319", "Robert B Walter"),
    43: ("c0daf938-ecef-569c-88d2-562f9ac19b7d", "Carroll R Walters"),
    44: ("31ef38be-bae9-5e4b-a588-efe6b04a895e", "George T Walters"),
    45: ("4ab6b5e5-c100-5b80-b0fa-6ed51d0f6b96", "Lawrence T Walters"),
    46: ("441b8ec5-2fc8-537d-aa45-072503acc264", "Lenore B Walters"),
}

UNRESOLVED = {
    24: "Common-name searches produced no source with an OSS assignment, indexed identifier, employer, occupation, or personnel-file bridge.",
    25: "Common-name and middle-initial searches produced no source with an OSS assignment, indexed identifier, employer, occupation, or personnel-file bridge.",
    27: "A postwar Army-order namesake supplied no indexed officer-number, Box 814, or OSS bridge and was not assigned.",
    28: "Genealogical and modern namesakes supplied no OSS, indexed-identifier, employer, or personnel-file bridge and were rejected.",
    29: "Exact-name and meaningful-variant searches produced no source with an OSS, indexed-identifier, employer, occupation, or personnel-file bridge.",
    30: "The exact name produced no reliable external identity, occupation, employer, or OSS-assignment source.",
    31: "A wartime casualty namesake carries a different service identifier and no OSS bridge; that candidate was rejected.",
    32: "Exact-name, OSS, employer, occupation, obituary, institutional, newspaper, directory, and archival searches produced no reliable identity bridge.",
    33: "Rank-aware, exact-name, officer-number, OSS, employer, and archival searches produced no reliable identity or employment bridge.",
    34: "Modern and chronologically incompatible namesakes supplied no OSS, indexed-identifier, employer, or personnel-file bridge and were rejected.",
    35: "A prominent postwar physician with the same name lacks an OSS, indexed-identifier, Box 814, or personnel-file bridge and was not assigned.",
    36: "A NARA Army prominence-list lead supplies no identifier or biography linking it to this index row; the common-name candidate remains unassigned.",
    37: "An exact-name search and a surname-only Maryland death-index lead supplied no OSS, indexed-identifier, employer, or personnel-file bridge.",
    38: "Name-order variants and modern results supplied no OSS, indexed-identifier, employer, or personnel-file bridge.",
    40: "A historical city-directory hit and other namesakes supplied no OSS, indexed-identifier, employer, or personnel-file bridge.",
    41: "A historical city-directory painter with the reversed name order lacks an OSS, indexed-identifier, Box 814, or personnel-file bridge and was not assigned.",
    42: "The printed Pharmacist's Mate first class, USNR rate establishes personnel category but not a distinct external identity, employer, or OSS assignment.",
    44: "A 1945 Canadian fair listing and modern professional namesakes supplied no OSS, indexed-identifier, employer, or personnel-file bridge.",
    45: "Modern employment and genealogy namesakes supplied no OSS, indexed-identifier, employer, or personnel-file bridge.",
    46: "Exact-name, OSS, employer, occupation, obituary, institutional, newspaper, directory, and archival searches produced no reliable identity bridge.",
}

ARMY_OCCUPATIONS = {
    26: {
        "date": "1942-06-25",
        "code": "475",
        "occupation": "machinist",
        "label": "Machinists",
        "locator": "PDF physical page 173; historical category 4-75",
    },
    39: {
        "date": "1943-03-30",
        "code": "736",
        "occupation": "chauffeur or driver of a bus, taxi, truck, or tractor",
        "label": "Chauffeurs and drivers, bus, taxi, truck, and tractor",
        "locator": "PDF physical page 174; historical category 7-36",
    },
    43: {
        "date": "1942-11-18",
        "code": "316",
        "occupation": "farm hand on a general farm",
        "label": "Farm hands, general farms",
        "locator": "PDF physical page 172; historical category 3-16",
    },
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 814-815",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 489, rows 24-46; checked against layout-preserving text and an original-detail page render",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. Protected identifiers remain private. PDF page 490 row 1, Robert E Walters in Box 815, is outside this cohort and begins the next batch.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; three accepted and one nonmatching protected-identifier comparison; identifiers and record ordinals withheld",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "Three exact-name identity bridges were accepted after private review. The nonmatching row supplied no transferable Army evidence.",
        },
        {
            "key": TECH,
            "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf",
            "archival_identifier": "NN3-064-03-008; National Archives Identifier 1263923",
            "title": "World War II Army Enlistment Records: Reference Copy of Technical Documentation",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives at College Park - Electronic Records",
            "publication_record_date": "1994-2005; reference copy modified 2011",
            "locator": "PDF physical pages 44-46; name, Army-entry-date, grade, and civilian-occupation fields",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
        },
        {
            "key": CODES,
            "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1CL_SD.pdf",
            "archival_identifier": "National Archives Identifier 1263923; Code No. 30",
            "title": "NARA Compiled Code Lists for the Electronic Army Serial Number Merged File",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives at College Park - Electronic Records",
            "publication_record_date": "2011-01-12; modified 2011-03-17",
            "locator": "PDF physical pages 172-174; historical civilian-occupation categories 3-16, 4-75, and 7-36",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "The historical labels identify broad occupations, not named employers, workplaces, or exact OSS-transfer dates.",
        },
    ]


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, item in ARMY_OCCUPATIONS.items():
        values.append({
            "key": f"{slug(PEOPLE[row][1])}-army-occupation-b998",
            "person_id": PEOPLE[row][0],
            "occupation": item["occupation"],
            "relationship_type": "employment",
            "end_date": item["date"],
            "date_precision": f"Historical civilian-occupation code {item['code']} was recorded at Army entry on {item['date']}; no named employer, workplace, or exact OSS-transfer date is supplied.",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "confirmed",
            "claim_confidence": "medium",
            "source_quality": "A_direct_official",
            "publication_status": "publish_qualified",
            "research_notes": "Broad historical occupation category only; no named employer or workplace is inferred.",
        })
    return values


def claim(
    key: str,
    row: int,
    claim_type: str,
    text: str,
    paraphrase: str,
    temporal: str,
    confidence: str,
    publication: str,
    notes: str,
    source_links: list[dict[str, str]],
    affiliation_key: str | None = None,
) -> dict[str, object]:
    value: dict[str, object] = {
        "key": key,
        "person_id": PEOPLE[row][0],
        "claim_type": claim_type,
        "claim_text": text,
        "evidence_paraphrase": paraphrase,
        "identity_match_assessment": "Confirmed by exact name and a nonshared protected-identifier agreement; the identifier and record ordinal remain private.",
        "temporal_assessment": temporal,
        "source_quality": "A_direct_official",
        "claim_confidence": confidence,
        "publication_status": publication,
        "match_notes": notes,
        "sources": source_links,
    }
    if affiliation_key:
        value["affiliation_key"] = affiliation_key
    return value


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, item in ARMY_OCCUPATIONS.items():
        name = PEOPLE[row][1]
        values.extend([
            claim(
                f"identity-{slug(name)}-b998",
                row,
                "identity",
                f"Indexed {name} is confirmed as the reviewed official Army entry record.",
                "The exact indexed and Army names agree, and a nonshared protected identifier connects the records.",
                f"The Army record dates entry to {item['date']} and supplies only historical civilian code {item['code']}.",
                "confirmed",
                "published",
                "Identity only; no named employer or exact OSS-transfer date is inferred.",
                [
                    {"source_key": INDEX, "locator_override": f"PDF page 489 row {row}; protected identifier withheld"},
                    {"source_key": ARMY, "locator_override": "Accepted reviewed identity bridge; protected identifier withheld"},
                ],
            ),
            claim(
                f"occupation-{slug(name)}-b998",
                row,
                "occupation",
                f"At Army entry on {item['date']}, {name} was recorded in the historical {item['occupation']} category; no named employer is identified.",
                f"The accepted Army record carries civilian-occupation code {item['code']}, decoded from NARA's official code list.",
                "Strongly date-bounded to Army entry; it does not establish the immediate pre-OSS affiliation or a named employer.",
                "medium",
                "publish_qualified",
                "Published with its limits and excluded from verified-employer analytics.",
                [
                    {"source_key": ARMY, "locator_override": f"Army entry {item['date']}; civilian occupation code {item['code']}; protected identifier withheld"},
                    {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46"},
                    {"source_key": CODES, "locator_override": item["locator"], "excerpt_override": item["label"]},
                ],
                f"{slug(name)}-army-occupation-b998",
            ),
        ])
    return values


def base_update(row: int, **overrides: object) -> dict[str, object]:
    value: dict[str, object] = {
        "person_id": PEOPLE[row][0],
        "manual_review_required": True,
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }
    value.update(overrides)
    return value


def person_updates() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, reason in UNRESOLVED.items():
        special: dict[str, object] = {}
        if row in {27, 33}:
            special = {
                "personnel_category": "commissioned_army_officer",
                "commissioned_officer": True,
                "allied_or_foreign_personnel": False,
            }
        elif row == 42:
            special = {
                "personnel_category": "enlisted_naval_personnel",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": False,
            }
        values.append(base_update(
            row,
            identity_status="unresolved",
            identity_evidence=f"The visually verified page 489 row preserves {PEOPLE[row][1]} and its archival context. {reason}",
            research_status="requires_archival_review",
            next_action=f"Review the indexed Box {'815' if row >= 43 else '814'} personnel file for corroborating identifiers, the immediate pre-OSS affiliation, and the last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}",
            **special,
        ))
    for row, item in ARMY_OCCUPATIONS.items():
        values.append(base_update(
            row,
            identity_status="confirmed",
            identity_evidence="The exact indexed name and a nonshared protected identifier connect the row to the reviewed official Army record.",
            personnel_category="enlisted_army_personnel",
            commissioned_officer=False,
            allied_or_foreign_personnel=False,
            research_status="occupation_only_found",
            next_action=f"Review the indexed Box {'815' if row >= 43 else '814'} personnel file to identify any named employer behind the broad {item['occupation']} category and establish the Army-to-OSS chronology.",
            nara_catalog_id="1263923",
        ))
    return values


def research_attempts() -> list[dict[str, object]]:
    attempts: list[dict[str, object]] = []
    candidate_rejected = {27, 28, 31, 34, 35, 36, 37, 40, 41, 44, 45}
    for row, (person_id, name) in PEOPLE.items():
        if row in ARMY_OCCUPATIONS:
            outcome, reviewed, rejected_count = "source_reviewed", 8, 5
            note = f"A reviewed protected-identifier Army bridge supports identity and a qualified {ARMY_OCCUPATIONS[row]['occupation']} category at Army entry; it supplies no named employer, workplace, or OSS-transfer date."
        elif row in candidate_rejected:
            outcome, reviewed, rejected_count = "candidate_rejected", 7, 7
            note = UNRESOLVED[row]
        else:
            outcome, reviewed, rejected_count = "no_result", 6, 6
            note = UNRESOLVED[row]
        attempts.append({
            "key": f"page489-row{row}-{slug(name)}-b998",
            "person_id": person_id,
            "source_adapter": "manual_staged_protocol",
            "query_text": f"{name}; NARA OSS index context; CIA Reading Room exact-name domain check; Library of Congress exact-name collection check; exact-name and meaningful variants; OSS, rank, branch, identifier and assignment clues; employer and occupation 1940; obituary, institutional, newspaper, directory and archival searches; indexed Box {'815' if row >= 43 else '814'}; protected identifiers used only in private official-record comparison",
            "query_variant_type": "staged_identity_employment_archival_protocol_batch_998",
            "started_at": "2026-11-03T17:10:00Z",
            "completed_at": "2026-11-03T18:25:00Z",
            "outcome": outcome,
            "sources_reviewed": reviewed,
            "candidate_sources_rejected": rejected_count,
            "rejection_reasons": "Unbridged namesakes, snippets, commercial people-finder pages, relatives, unsourced genealogy, postwar-only leads, and sources without an OSS, protected-identifier, rank, unit, or personnel-file bridge were rejected. The postwar Louis A Walsh Jr. officer lead, Richard L Walsh casualty, William B Walsh physician, William F Walsh prominence-list entry, and directory or modern Walter/Walters leads were not assigned. Historical occupations were not converted into named employers.",
            "research_notes": f"{note} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain, and archival searches were checked as applicable. Exact-name CIA Reading Room checks produced no additional publishable employer source. Library of Congress collection discovery checks produced no reliable identity bridge. The NARA index page was text-extracted, rendered, and visually checked; official Army bulk data, technical documentation, and code documentation were inspected locally. No search-result snippet was used as sole final evidence, no paywall or access control was bypassed, and no authenticated NARA Catalog API call was made.",
            "next_action": f"Review the indexed Box {'815' if row >= 43 else '814'} personnel file for corroborating identifiers, the immediate pre-OSS affiliation, and the last civilian employer before wartime service.",
            "attempt_number": 1,
            "research_agent_version": "before-oss-b998-v1",
        })
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-998-v1",
        "reviewer": "Before OSS Batch 998 evidence review",
        "sources": sources(),
        "organizations": [],
        "affiliations": affiliations(),
        "claims": claims(),
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }
    EvidenceBundle.model_validate(bundle)
    OUTPUT.write_text(
        json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
