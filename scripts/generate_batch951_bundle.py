#!/usr/bin/env python3
"""Generate the reviewed Batch 951 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page466-austin-h-thompson-to-james-l-thompson-"
    "review_batch-951_2026-10-28.json"
)

INDEX = "nara-index-b951"
ARMY = "army-bulk-b951"
TECH = "army-tech-b951"
CODES = "army-codes-b951"
NEW_YORKER = "new-yorker-benjamin-thompson-b951"


PEOPLE = {
    1: ("f55c9fe2-2777-5fc4-be9e-66b2879bb6fb", "Austin H Thompson"),
    2: ("6afbec90-7296-5481-87e1-da8b070b1b0a", "Benjamin C Thompson"),
    3: ("a0e9c855-9fee-5c71-a947-e1d0695fb408", "Charles D Thompson"),
    4: ("e03b71e1-6c88-59a1-9c07-b256281029e4", "Charles F Thompson"),
    5: ("81c0c7d6-e51d-562c-8c38-9972623903d4", "Charles L Thompson"),
    6: ("db6bea42-64d8-585e-8a86-f8903b4e82b4", "Charles W Thompson"),
    7: ("ccf7ae6b-eb61-513b-9de4-ca9277c7d0de", "Cynthia N Thompson"),
    8: ("7a4b4ec6-23bc-5b2a-8e51-5d65b4d1acc6", "Cyril S Thompson"),
    9: ("fded3f72-83b3-5b17-ab28-8a73540cf94b", "Delwyn D Thompson"),
    10: ("14bfb168-2e53-533d-8a22-a8175b17242a", "Edward A Thompson"),
    11: ("0cdac249-9664-588b-813d-68ea1649b099", "Edwin E Thompson"),
    12: ("9608cf06-262b-5edf-aea2-89da1577571c", "Elise E Thompson"),
    13: ("4d8a352b-6619-5971-98c1-f6b1c07e01e7", "Esther V Thompson"),
    14: ("4a3cde62-0215-518b-80e2-9420cf1389c4", "Eugene K Thompson"),
    15: ("fce5601f-6e15-5c10-b409-54e8cc056310", "Frances K Thompson"),
    16: ("c5512256-75fe-57f8-9813-8ef2c96962f2", "Frances M Thompson"),
    17: ("da533eb3-42a9-5d6a-b1ba-d3d357b795f0", "Genevieve Thompson"),
    18: ("e6a733b8-2d8b-5c24-8633-ec3eb1f0e966", "Granville K Thompson"),
    19: ("d5a4614e-85b1-5e40-8585-00ab8fefbb92", "Harry N Thompson"),
    20: ("901fbd46-4d5b-5a72-92c8-3a10d537d05e", "James W Thompson"),
    21: ("f0db9336-3497-5723-94f6-92133e1dc79d", "James C Thompson"),
    22: ("90ee0049-4953-5278-b942-fc960e8cf0c0", "James H Thompson"),
    23: ("f0cccd89-8310-5e42-82ba-e2427ca4433a", "James L Thompson"),
}


ARMY_RECORDS = [
    {
        "row": 1,
        "date": "1942-09-01",
        "code": "698",
        "occupation": "radio or phonograph manufacturing occupation",
        "label": "Occupations in manufacture of radios and phonographs",
        "locator": "PDF physical page 174; historical category 6-98",
        "relationship": "employment",
    },
    {
        "row": 11,
        "date": "1943-01-05",
        "code": "963",
        "occupation": "nonprocess manufacturing occupation, not elsewhere classified",
        "label": "Nonprocess occupations in manufacturing, n.e.c.",
        "locator": "PDF physical page 174; historical category 9-63",
        "relationship": "employment",
    },
    {
        "row": 18,
        "date": "1942-10-03",
        "code": "001",
        "occupation": "accountant or auditor",
        "label": "Accountants and auditors",
        "locator": "PDF physical page 170; historical category 0-01",
        "relationship": "employment",
    },
    {
        "row": 19,
        "date": "1943-05-12",
        "code": "105",
        "occupation": "general office clerk",
        "label": "Clerks, general office",
        "locator": "PDF physical page 171; historical category 1-05",
        "relationship": "employment",
    },
    {
        "row": 21,
        "date": "1942-07-20",
        "code": "721",
        "occupation": "miner or mining-machine operator",
        "label": "Miners and mining-machine operators",
        "locator": "PDF physical page 174; historical category 7-21",
        "relationship": "employment",
    },
    {
        "row": 23,
        "date": "1944-10-20",
        "code": "992",
        "occupation": "student",
        "label": "Students",
        "locator": "PDF physical page 304; amended historical category 9-92",
        "relationship": "student",
    },
]


UNRESOLVED = {
    3: "The common name produced no OSS, Box 774 or corroborating identity bridge and no reliable pre-OSS affiliation.",
    4: "Exact-name, military, obituary and institutional searches produced multiple namesakes but no defensible OSS identity or pre-OSS chronology.",
    5: "Common-name results lacked a protected-identifier, Box-file or dated OSS bridge and were not assigned.",
    6: "Exact-name and meaningful-variant searches produced unbridged namesakes but no reliable pre-OSS affiliation.",
    7: "Exact-name, official-domain, obituary and institutional searches did not identify the indexed person or a dated pre-OSS role.",
    8: "The distinctive initialed name produced no defensible OSS identity or employment result in the accessible sources reviewed.",
    9: "Exact-name and variant searches produced no reliable identity, occupation or employer bridge.",
    10: "Common-name military, obituary and directory candidates lacked two corroborating identifiers beyond the name.",
    12: "Exact-name, official-domain and institutional searches produced no reliable OSS identity or pre-OSS affiliation.",
    13: "Exact-name, obituary, directory and archival searches did not distinguish the indexed person from namesakes.",
    14: "Exact-name and employment-focused searches produced no defensible OSS identity or dated pre-OSS employer evidence.",
    16: "Exact-name and meaningful-variant searches produced namesakes without an OSS, Box-file or protected-identifier bridge.",
    17: "The initial-free common name produced historical namesakes but no corroborating OSS identity or pre-OSS chronology.",
    20: "Common-name exact and variant searches did not establish a unique indexed person or reliable pre-OSS affiliation.",
    22: "Common-name military, obituary and institutional candidates lacked an OSS, Box-file or corroborating identity bridge.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Box 774",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 466, rows 1-23; checked against layout-preserving text and a 220 dpi page render",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. Austin H Thompson and James L Thompson were visually checked as the cohort boundaries; Janet F Thompson is the next row. Full protected identifiers remain private.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; seven reviewed Batch 951 candidates; protected identifiers withheld",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "No raw bulk row or full protected identifier is retained in public assets. Six identities were accepted; the Frances K./Frank K. Thompson first-name conflict transfers no Army fields.",
        },
        {
            "key": TECH,
            "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf",
            "archival_identifier": "NN3-064-03-008; National Archives Identifier 1263923",
            "title": "World War II Army Enlistment Records: Reference Copy of Technical Documentation",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives at College Park - Electronic Records",
            "publication_record_date": "1994-2005; reference copy modified 2011",
            "locator": "PDF physical pages 44-46; identifier, name, Army-entry-date, grade and civilian-occupation fields",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Used to interpret selected fields only; source damage, coding limits and incomplete coverage remain applicable.",
        },
        {
            "key": CODES,
            "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1CL_SD.pdf",
            "archival_identifier": "National Archives Identifier 1263923; Code No. 30",
            "title": "NARA Compiled Code Lists for the Electronic Army Serial Number Merged File",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives at College Park - Electronic Records",
            "publication_record_date": "2011-01-12; modified 2011-03-17",
            "locator": "PDF physical pages 170-174 and 304; reviewed historical categories 0-01, 1-05, 6-98, 7-21, 9-63 and amended 9-92",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical occupation labels are qualified and never converted into named employers. Students is modeled as status, not employment.",
        },
        {
            "key": NEW_YORKER,
            "stable_url": "https://www.newyorker.com/magazine/1963/12/28/new-store-2",
            "archival_identifier": "The New Yorker, Talk of the Town, December 28, 1963",
            "title": "New Store",
            "author_creator": "Geoffrey T. Hellman",
            "repository_publisher": "The New Yorker",
            "publication_record_date": "1963-12-21",
            "locator": "Profile of architect Benjamin Thompson; wartime chronology and postwar Architects Collaborative discussion",
            "access_date": "2026-10-28",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "The Talk of the Town",
            "rights_notes": "Retained as a withheld identity lead only. The article describes architect Benjamin Thompson's wartime work but does not connect him to this Box 774 index row.",
        },
    ]


def affiliation(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    return {
        "key": f"{slug(PEOPLE[row][1])}-occupation-b951",
        "person_id": PEOPLE[row][0],
        "occupation": item["occupation"],
        "relationship_type": item["relationship"],
        "end_date": item["date"],
        "date_precision": f"Historical category {item['code']} was recorded at Army entry on {item['date']}; no employer, workplace, school or OSS-transfer date is named.",
        "country": "United States",
        "immediate_pre_oss": False,
        "last_civilian_pre_service": False,
        "pre_oss_temporal_basis": "strongly_date_bounded",
        "identity_confidence": "high_confidence",
        "claim_confidence": "medium",
        "source_quality": "A_direct_official",
        "publication_status": "publish_qualified",
        "research_notes": "The historical category is not converted into a named employer, workplace, school, immediate affiliation or exact modern job title.",
    }


def claim(
    row: int,
    key: str,
    claim_type: str,
    text: str,
    paraphrase: str,
    identity: str,
    temporal: str,
    quality: str,
    confidence: str,
    source_links: list[dict[str, object]],
    notes: str,
    affiliation_key: str | None = None,
    publication_status: str | None = None,
) -> dict[str, object]:
    return {
        "key": key,
        "person_id": PEOPLE[row][0],
        "affiliation_key": affiliation_key,
        "claim_type": claim_type,
        "claim_text": text,
        "evidence_paraphrase": paraphrase,
        "identity_match_assessment": identity,
        "temporal_assessment": temporal,
        "source_quality": quality,
        "claim_confidence": confidence,
        "publication_status": publication_status
        or ("published" if confidence in {"confirmed", "high"} else "publish_qualified"),
        "match_notes": notes,
        "sources": source_links,
    }


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for item in ARMY_RECORDS:
        row = int(item["row"])
        name = PEOPLE[row][1]
        values.append(
            claim(
                row,
                f"identity-{slug(name)}-b951",
                "identity",
                f"The indexed {name} is a high-confidence match to the reviewed official Army record.",
                "A nonshared protected identifier connects the visually verified index row to the official Army record, and the name is exact or suffix-compatible.",
                "High confidence from a private nonshared identifier plus name agreement.",
                "The Army record dates entry into service but does not establish the exact OSS transfer date.",
                "A_direct_official",
                "high",
                [
                    {"source_key": INDEX, "locator_override": f"PDF page 466 row {row}; protected identifier withheld"},
                    {"source_key": ARMY, "locator_override": "Reviewed name record; protected identifier withheld"},
                    {"source_key": TECH, "support_type": "context_only", "locator_override": "Field definitions, PDF physical pages 44-46"},
                ],
                "This identity decision does not establish a named employer or immediate OSS predecessor.",
            )
        )
        if item["relationship"] == "student":
            text = f"At Army entry on {item['date']}, {name} was recorded in the historical Students category; no school or employer is identified."
        else:
            text = f"At Army entry on {item['date']}, {name}'s record carried the historical civilian-occupation category {item['label']}; no employer is named."
        values.append(
            claim(
                row,
                f"occupation-{slug(name)}-b951",
                "occupation" if item["relationship"] == "employment" else "other_pre_oss_affiliation",
                text,
                f"The official bulk record supplies code {item['code']}; the visually reviewed NARA code list expands it as {item['label']}.",
                "High confidence from the accepted protected-identifier bridge and name agreement.",
                "Strongly date-bounded at Army entry, but not shown to be the immediate pre-OSS affiliation.",
                "A_direct_official",
                "medium",
                [
                    {"source_key": ARMY, "locator_override": f"Army entry {item['date']}; code {item['code']}; identifier withheld"},
                    {"source_key": CODES, "locator_override": item["locator"]},
                ],
                "Published only as a qualified historical category. No workplace, employer or school is inferred.",
                f"{slug(name)}-occupation-b951",
                "publish_qualified",
            )
        )
    values.extend(
        [
            claim(
                15,
                "conflict-frances-k-thompson-army-b951",
                "identity",
                "The indexed Frances K. Thompson row is not assigned to the reviewed Frank K. Thompson Army record despite the private identifier collision.",
                "The protected identifier points to an Army record whose first name materially differs, so no Army field is transferred.",
                "Conflicting: the private identifier agrees but Frances and Frank materially disagree.",
                "No Army occupation, grade or affiliation is transferred until the Box 774 file resolves the collision.",
                "A_direct_official",
                "conflicting",
                [
                    {"source_key": INDEX, "locator_override": "PDF page 466 row 15; protected identifier withheld"},
                    {"source_key": ARMY, "support_type": "contradicts", "locator_override": "Reviewed candidate prints Frank K Thompson; protected identifier withheld"},
                ],
                "The conflict remains visible and is not silently corrected or used as biographical evidence.",
                publication_status="conflicting",
            ),
            claim(
                2,
                "candidate-benjamin-c-thompson-architect-b951",
                "identity",
                "Architect Benjamin C. Thompson is a plausible but unconfirmed candidate for the indexed Benjamin C. Thompson.",
                "A contemporary profile describes the architect's Navy and OSS service, construction work and Corps of Engineers camouflage work, but supplies no Box 774 or protected-identifier bridge.",
                "Ambiguous: exact name and OSS context agree, but the common name and index row lack two corroborating identifiers.",
                "The candidate biography has a wartime chronology, but none may be transferred to the indexed person until identity is resolved.",
                "C_reputable_contemporary_or_scholarly",
                "low",
                [{"source_key": NEW_YORKER, "locator_override": "1963 profile of architect Benjamin Thompson"}],
                "Withheld from public facts and analytics; review Box 774 for birth, education, branch or assignment evidence.",
                publication_status="withheld_low_confidence",
            ),
        ]
    )
    return values


def archival_update(row: int, reason: str) -> dict[str, object]:
    person_id, name = PEOPLE[row]
    return {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, Box 774 and archive location 230/86/42/01. {reason}",
        "personnel_category": "unknown_or_indeterminate",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": "Review Box 774 for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }


def army_update(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    person_id, name = PEOPLE[row]
    update: dict[str, object] = {
        "person_id": person_id,
        "identity_status": "high_confidence",
        "identity_evidence": f"A nonshared protected identifier and name agreement connect the visually verified {name} index row to the reviewed official Army record.",
        "personnel_category": "enlisted_army_personnel",
        "commissioned_officer": False,
        "allied_or_foreign_personnel": False,
        "manual_review_required": True,
        "research_status": "occupation_only_found",
        "next_action": "Review Box 774 to establish the immediate pre-OSS affiliation and named last civilian employer; do not convert the Army category into a workplace or school.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }
    if row == 19:
        update["name_variants"] = ["Harry N Thompson Jr"]
    return update


def person_updates() -> list[dict[str, object]]:
    values = [archival_update(row, reason) for row, reason in UNRESOLVED.items()]
    values.extend(army_update(item) for item in ARMY_RECORDS)
    values.extend(
        [
            {
                "person_id": PEOPLE[2][0],
                "identity_status": "ambiguous",
                "identity_evidence": "Architect Benjamin C. Thompson is a plausible exact-name OSS candidate, but the index supplies no rank or public identifier and the contemporary profile supplies no Box 774 bridge.",
                "personnel_category": "unknown_or_indeterminate",
                "manual_review_required": True,
                "research_status": "needs_identity_review",
                "next_action": "Review Box 774 for birth date, education, naval assignment or OSS Presentation Branch evidence before transferring the architect's construction or Corps of Engineers chronology.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[15][0],
                "identity_status": "conflicting",
                "identity_evidence": "The index prints Frances K. Thompson, while the reviewed Army row linked by the private identifier prints Frank K. Thompson. The first-name collision is preserved and no Army fields are transferred.",
                "personnel_category": "unknown_or_indeterminate",
                "manual_review_required": True,
                "research_status": "conflicting_sources",
                "next_action": "Review the Box 774 personnel file and original Army source together to resolve the identifier/name collision before assigning any occupation or affiliation.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
        ]
    )
    return values


def research_attempts() -> list[dict[str, object]]:
    army_rows = {int(item["row"]) for item in ARMY_RECORDS}
    attempts: list[dict[str, object]] = []
    for row in sorted(PEOPLE):
        person_id, name = PEOPLE[row]
        if row in UNRESOLVED:
            outcome, reviewed, rejected, detail = "no_result", 7, 7, UNRESOLVED[row]
        elif row in army_rows:
            outcome, reviewed, rejected = "source_reviewed", 8, 5
            detail = "An accepted protected-identifier Army bridge supports identity and a dated historical occupation or student-status category without naming an employer or school."
        elif row == 2:
            outcome, reviewed, rejected, detail = "candidate_found", 9, 7, "Architect Benjamin C. Thompson is an exact-name OSS candidate whose contemporary profile supplies a detailed wartime chronology, but no second indexed identifier or Box 774 bridge supports assignment."
        elif row == 15:
            outcome, reviewed, rejected, detail = "candidate_found", 8, 6, "The protected identifier points to Frank K. Thompson while the index prints Frances K. Thompson; the first-name conflict is preserved and no Army field is transferred."
        else:
            raise AssertionError(f"Missing Batch 951 outcome for row {row}")
        attempts.append(
            {
                "key": f"page466-row{row}-{slug(name)}-b951",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index and public Archives context; CIA Reading Room or equivalent official-source check; exact-name and meaningful variants; OSS and military clues; employer and occupation 1940; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Box 774; protected identifiers used privately only when defensible",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_951",
                "started_at": "2026-10-28T12:00:00Z",
                "completed_at": "2026-10-28T15:15:00Z",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search snippets, family-tree assertions, people-finder pages, modern records, postwar-only leads and sources without an OSS, protected-identifier or Box-file bridge were not assigned. A Granville Kirby Thompson who died in 1935 was rejected as chronologically impossible. The Benjamin Thompson architect biography remains a withheld lead only.",
                "research_notes": f"{detail} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain, CIA Reading Room and Library of Congress searches were checked as applicable. The index and admitted Army and code-list sources were visually reviewed. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": "Review Box 774 for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before wartime service.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b951-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-951-v1",
        "reviewer": "Before OSS Batch 951 evidence review",
        "sources": sources(),
        "organizations": [],
        "affiliations": [affiliation(item) for item in ARMY_RECORDS],
        "claims": claims(),
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }
    EvidenceBundle.model_validate(bundle)
    OUTPUT.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
