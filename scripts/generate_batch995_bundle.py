#!/usr/bin/env python3
"""Generate the reviewed Batch 995 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page488-walk-to-walker-"
    "review_batch-995_2026-11-03.json"
)

INDEX = "nara-index-b995"
ARMY = "army-bulk-b995"
TECH = "army-tech-b995"
CODES = "army-codes-b995"


PEOPLE = {
    1: ("fab5ef20-f001-5dea-ada9-27184f1b7f86", "Richard D Walk"),
    2: ("e9cdf34e-9e6b-5fbe-91da-bbaf5cb9a283", "Albert Walker"),
    3: ("c4f2769f-aeec-59d5-ba0f-f94f88af5ec2", "Alvin Walker"),
    4: ("a5b7d8d3-810d-517e-bc61-87a0359a0dfa", "Ann C Walker"),
    5: ("e642b0c8-a5fa-533d-b208-cfe63fecbf54", "Ann Walker"),
    6: ("2842489c-2541-56bf-9ba2-be9594be05c9", "Anna G Walker"),
    7: ("f752f636-d84d-58ca-aae7-578d4a7ea918", "Bette B Walker"),
    8: ("7cef39d0-6022-5e0d-957b-d2ff21b82978", "Burdeau Walker"),
    9: ("bbb69569-76d8-53dd-95df-4110d86d285a", "Charles S Walker Jr."),
    10: ("5380b9b7-7cc7-5ed7-9ee4-e5a6eb58dc23", "Charlotte F Walker"),
    11: ("606124e8-7690-5a13-b93c-8e4994173bfd", "Doyle E Walker"),
    12: ("79bdb544-7b3d-51bb-bab0-dd3ee917fe0f", "Earl E Walker"),
    13: ("afa5978b-65fc-53cb-97f2-eaa95400c45a", "Eleanor Louise Walker"),
    14: ("e4b38c8f-5816-57e6-bb45-ab6e99af193d", "Fred W Walker"),
    15: ("25de06bd-bc37-5d02-8963-df108cbd026a", "Fred L Walker Jr."),
    16: ("bc6c83a9-6eda-5135-ac73-e2ee63bc9a42", "Gordon A Walker"),
    17: ("82d9e346-f0d1-50d8-926a-18aeadc153bc", "Herman Walker Jr."),
    18: ("629282c2-60ad-5e4f-a80d-e446f35ec92e", "James Edward Walker"),
    19: ("3b209b39-4b2e-5d5f-85aa-446afa5b1a07", "John C Walker"),
    20: ("02336424-ef94-5ca7-8e83-31d3f52e1983", "John W Walker"),
    21: ("76b5fb40-2b7d-57c0-906b-7ce0b78350f6", "Joseph W Walker"),
    22: ("66f9c5f9-2f77-5dcf-a5a5-97920f0e17dd", "Lucy B Walker"),
    23: ("44e05623-d961-5aa5-87e9-1ccbfce38cc8", "Marjorie K Walker"),
}

OFFICERS = {9, 12, 15}

UNRESOLVED = {
    2: "The common exact name produced multiple namesakes but no source with an indexed identifier, OSS assignment, rank, unit, or personnel-file bridge.",
    3: "Exact-name, OSS, employer, occupation, obituary, institutional, newspaper, and archival searches produced no reliable identity bridge.",
    4: "Exact-name and initial-variant searches produced no source with an OSS, protected-identifier, employer, or personnel-file bridge.",
    5: "The common exact name produced multiple namesakes but no corroborating identifiers beyond the name.",
    6: "Exact-name and initial-variant searches produced no source with an OSS, protected-identifier, employer, or personnel-file bridge.",
    7: "Exact-name, OSS, occupation, obituary, institutional, and archival searches produced no reliable result.",
    8: "A Newberry Library family-history finding-aid name and an unsourced genealogy lead supplied no OSS, indexed-identifier, or employment bridge and were rejected.",
    9: "Rank-aware and exact-name searches produced no source with the indexed identifier or a direct OSS assignment bridge.",
    10: "Exact-name and initial-variant searches produced no source with an OSS, protected-identifier, employer, or personnel-file bridge.",
    12: "Rank-aware and exact-name searches produced no source with the indexed identifier or a direct OSS assignment bridge.",
    13: "The distinctive full name produced no source with an OSS, protected-identifier, employer, or personnel-file bridge.",
    15: "Texas Military Forces Museum material documents a 36th Division officer with the exact name and compatible rank progression, but supplies no OSS, indexed-identifier, or personnel-file bridge; the lead remains unassigned.",
    18: "The distinctive full name produced no source with an OSS, protected-identifier, employer, or personnel-file bridge.",
    19: "Common-name and rank-aware searches produced no source with the middle initial, indexed identifier, unit, or a direct OSS assignment bridge.",
    20: "Common-name searches produced no source with the middle initial, indexed identifier, rank, unit, or direct OSS bridge.",
    21: "Common-name searches produced no source with the middle initial, indexed identifier, rank, unit, or direct OSS bridge.",
    22: "Exact-name and initial-variant searches produced no source with an OSS, protected-identifier, employer, or personnel-file bridge.",
    23: "Exact-name and initial-variant searches produced no source with an OSS, protected-identifier, employer, or personnel-file bridge.",
}

ARMY_OCCUPATIONS = {
    1: {
        "date": "1942-12-11",
        "code": "000",
        "occupation": "architect",
        "label": "Architects",
        "locator": "PDF physical pages 170 and 175; historical category 0-00",
        "identity": "high_confidence",
        "confidence": "high",
        "variant": "The official Army name differs by one apparent transcription character in the given name.",
    },
    11: {
        "date": "1942-11-07",
        "code": "787",
        "occupation": "chainman, rodman, or axman in surveying",
        "label": "Chainmen, rodmen, and axmen, surveying",
        "locator": "PDF physical page 175; historical category 7-87",
        "identity": "confirmed",
        "confidence": "confirmed",
        "variant": "The official Army and indexed names agree exactly.",
    },
    14: {
        "date": "1943-05-08",
        "code": "316",
        "occupation": "farm hand on a general farm",
        "label": "Farm hands, general farms",
        "locator": "PDF physical page 172; historical category 3-16",
        "identity": "confirmed",
        "confidence": "confirmed",
        "variant": "The official Army and indexed names agree exactly.",
    },
    17: {
        "date": "1943-03-31",
        "code": "039",
        "occupation": "professional occupation, not elsewhere classified",
        "label": "Professional occupations, not elsewhere classified",
        "locator": "PDF physical page 171; historical category 0-39",
        "identity": "confirmed",
        "confidence": "confirmed",
        "variant": "The official Army name and Jr. suffix agree with the indexed form.",
    },
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Box 812",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 488, rows 1-23; checked against layout-preserving text and an original-detail page render",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. Protected identifiers remain private. PDF page 488 row 24, Mary Virginia Walker in Box 813, is outside this cohort and begins the next batch.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; four accepted protected-identifier comparisons and one rejected material name collision; identifiers and record ordinals withheld",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "Four identity bridges were accepted after private comparison. Gordon A Walker's identifier points to a wholly different Army name; no Army fields were transferred to him.",
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
            "locator": "PDF physical pages 170-175; historical civilian-occupation categories 0-00, 0-39, 3-16, and 7-87",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "The page-175 category 7-87 was checked in extracted text and an original-detail render. Historical labels identify broad occupations, not employers or exact OSS-transfer dates.",
        },
    ]


def affiliations() -> list[dict[str, object]]:
    values = []
    for row, item in ARMY_OCCUPATIONS.items():
        values.append(
            {
                "key": f"{slug(PEOPLE[row][1])}-army-occupation-b995",
                "person_id": PEOPLE[row][0],
                "occupation": item["occupation"],
                "relationship_type": "employment",
                "end_date": item["date"],
                "date_precision": f"Historical civilian-occupation code {item['code']} was recorded at Army entry on {item['date']}; no named employer, workplace, or exact OSS-transfer date is supplied.",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": item["identity"],
                "claim_confidence": "medium",
                "source_quality": "A_direct_official",
                "publication_status": "publish_qualified",
                "research_notes": "Broad historical occupation category only; no named employer or workplace is inferred.",
            }
        )
    return values


def claim(
    key: str,
    row: int,
    claim_type: str,
    text: str,
    paraphrase: str,
    identity: str,
    temporal: str,
    quality: str,
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
        "identity_match_assessment": identity,
        "temporal_assessment": temporal,
        "source_quality": quality,
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
        values.extend(
            [
                claim(
                    f"identity-{slug(name)}-b995",
                    row,
                    "identity",
                    f"Indexed {name} is a {item['confidence'].replace('_', ' ')} match to the reviewed official Army entry record.",
                    f"A nonshared protected identifier connects the visually verified index row to the Army record. {item['variant']}",
                    f"{item['confidence'].replace('_', ' ').capitalize()} from the protected-identifier bridge and documented name comparison; the identifier and record ordinal remain private.",
                    f"The Army record dates entry to {item['date']} and supplies only historical civilian code {item['code']}.",
                    "A_direct_official",
                    item["confidence"],
                    "published",
                    "Identity only; no named employer or exact OSS-transfer date is inferred.",
                    [
                        {"source_key": INDEX, "locator_override": f"PDF page 488 row {row}; protected identifier withheld"},
                        {"source_key": ARMY, "locator_override": "Accepted reviewed identity bridge; protected identifier withheld"},
                    ],
                ),
                claim(
                    f"occupation-{slug(name)}-b995",
                    row,
                    "occupation",
                    f"At Army entry on {item['date']}, {name} was recorded in the historical {str(item['occupation']).lower()} category; no named employer is identified.",
                    f"The accepted Army record carries civilian-occupation code {item['code']}, decoded from NARA's official code list.",
                    "The occupation belongs only to the reviewed protected-identifier match; the identifier itself is not public.",
                    "Strongly date-bounded to Army entry; it does not establish the immediate pre-OSS affiliation or a named employer.",
                    "A_direct_official",
                    "medium",
                    "publish_qualified",
                    "Published with its limits and excluded from verified-employer analytics.",
                    [
                        {"source_key": ARMY, "locator_override": f"Army entry {item['date']}; civilian occupation code {item['code']}; protected identifier withheld"},
                        {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46"},
                        {"source_key": CODES, "locator_override": item["locator"], "excerpt_override": item["label"]},
                    ],
                    f"{slug(name)}-army-occupation-b995",
                ),
            ]
        )
    values.append(
        claim(
            "conflict-gordon-walker-b995",
            16,
            "identity",
            "Gordon A Walker's indexed protected identifier points to an official Army record under a wholly different name.",
            "The visually verified index row and official Army bulk row conflict materially in both surname and given name.",
            "Conflicting source data: the Army candidate is rejected, and its identity, chronology, grade, and occupation are not transferred.",
            "No temporal conclusion is possible until the indexed Box 812 personnel file is reviewed.",
            "A_direct_official",
            "conflicting",
            "conflicting",
            "The conflict remains visible without exposing either protected identifier or the unrelated Army biography.",
            [
                {"source_key": INDEX, "locator_override": "PDF page 488 row 16; protected identifier withheld"},
                {"source_key": ARMY, "locator_override": "Rejected material name collision; protected identifier and unrelated name withheld"},
            ],
        )
    )
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
    values = []
    for row, reason in UNRESOLVED.items():
        category = "commissioned_army_officer" if row in OFFICERS else "unknown_or_indeterminate"
        officer: bool | None = True if row in OFFICERS else None
        values.append(
            base_update(
                row,
                identity_status="unresolved",
                identity_evidence=f"The visually verified page 488 row preserves {PEOPLE[row][1]} and its archival context. {reason}",
                personnel_category=category,
                commissioned_officer=officer,
                research_status="requires_archival_review",
                next_action=f"Review the indexed Box 812 personnel file for corroborating identifiers, the immediate pre-OSS affiliation, and the last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}",
            )
        )

    for row, item in ARMY_OCCUPATIONS.items():
        name = PEOPLE[row][1]
        identity_note = "Exact indexed name and a nonshared protected identifier connect the row to the reviewed official Army record."
        if row == 1:
            identity_note = "A nonshared protected identifier and matching surname, given-name structure, middle initial, and chronology connect the row to the official Army record despite one apparent transcription character in the given name."
        elif row == 17:
            identity_note = "The indexed name and Jr. suffix agree with the official Army form, and a nonshared protected identifier connects the records."
        values.append(
            base_update(
                row,
                identity_status=item["identity"],
                identity_evidence=identity_note,
                personnel_category="enlisted_army_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                research_status="occupation_only_found",
                next_action=f"Review the indexed Box 812 personnel file to identify any named employer behind the broad {str(item['occupation']).lower()} category and establish the Army-to-OSS chronology.",
                nara_catalog_id="1263923",
            )
        )

    values.append(
        base_update(
            16,
            identity_status="conflicting",
            identity_evidence="The protected identifier printed for Gordon A Walker points to an official Army row under a wholly different full name. The candidate is rejected and none of its fields are transferred.",
            personnel_category="unknown_or_indeterminate",
            commissioned_officer=None,
            research_status="conflicting_sources",
            next_action="Review the indexed Box 812 personnel file to resolve the protected-identifier conflict before assigning any Army identity, chronology, occupation, immediate affiliation, or employer.",
            archival_review_priority="critical",
        )
    )
    return values


def research_attempts() -> list[dict[str, object]]:
    attempts = []
    sourced = set(ARMY_OCCUPATIONS)
    rejected = {8, 15, 16}
    for row, (person_id, name) in PEOPLE.items():
        if row in sourced:
            outcome, reviewed, rejected_count = "source_reviewed", 8, 5
            note = f"A reviewed protected-identifier Army bridge supports identity and a qualified {ARMY_OCCUPATIONS[row]['occupation']} category at Army entry; it supplies no named employer or OSS-transfer date."
            if row == 1:
                note += " A postwar contractor-license namesake was not used as a wartime identity or employment bridge."
        elif row == 16:
            outcome, reviewed, rejected_count = "candidate_rejected", 8, 7
            note = "The protected identifier points to a wholly different official Army name. The candidate was rejected and its date, grade, occupation, and biography were withheld."
        elif row == 15:
            outcome, reviewed, rejected_count = "candidate_rejected", 8, 7
            note = "Texas Military Forces Museum sources document a Fred L. Walker Jr. as a 36th Division operations officer and later 143rd Infantry battalion commander, but no OSS, indexed-identifier, or personnel-file bridge links that officer to this common-name row."
        elif row == 8:
            outcome, reviewed, rejected_count = "candidate_rejected", 7, 7
            note = UNRESOLVED[row]
        else:
            outcome, reviewed, rejected_count = "no_result", 6, 6
            note = UNRESOLVED[row]

        attempts.append(
            {
                "key": f"page488-row{row}-{slug(name)}-b995",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index context; CIA Reading Room exact-name domain check; Library of Congress exact-name collection check; exact-name and meaningful variants; OSS, rank, branch, identifier and assignment clues; employer and occupation 1940; obituary, institutional, newspaper, directory and archival searches; indexed Box 812; protected identifiers used only in private official-record comparison",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_995",
                "started_at": "2026-11-03T13:30:00Z",
                "completed_at": "2026-11-03T14:25:00Z",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected_count,
                "rejection_reasons": "Unbridged namesakes, snippets, commercial people-finder pages, relatives, unsourced genealogy, postwar-only leads, and sources without an OSS, protected-identifier, rank, unit, or personnel-file bridge were rejected. Fred L. Walker Jr.'s compatible 36th Division lead was not assigned without a second corroborating identifier beyond name and rank. Gordon A Walker's material Army-name collision was rejected. Historical occupations were not converted into named employers.",
                "research_notes": f"{note} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain, and archival searches were checked as applicable. Grouped CIA Reading Room and Library of Congress discovery checks produced no additional publishable employer source for the cohort. The NARA index page was text-extracted, rendered, and visually checked; official Army bulk data, technical documentation, and code documentation were inspected locally. The code-787 page was also visually checked. No search-result snippet was used as sole final evidence, no paywall or access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": "Review the indexed Box 812 personnel file for corroborating identifiers, the immediate pre-OSS affiliation, and the last civilian employer before wartime service.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b995-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-995-v1",
        "reviewer": "Before OSS Batch 995 evidence review",
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
