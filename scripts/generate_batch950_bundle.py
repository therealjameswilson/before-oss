#!/usr/bin/env python3
"""Generate the reviewed Batch 950 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page465-lewis-v-thomas-to-allen-j-thompson-"
    "review_batch-950_2026-10-28.json"
)

INDEX = "nara-index-b950"
ARMY = "army-bulk-b950"
TECH = "army-tech-b950"
CODES = "army-codes-b950"
REGISTER = "army-register-1947-b950"
CASUALTY = "nara-wisconsin-casualty-b950"
US_ARMY = "us-army-existing-b950"
USMA = "usma-existing-b950"


PEOPLE = {
    24: ("e44e7ee4-3e3c-56c0-b0e2-9f4f360fa3d7", "Lewis V Thomas"),
    25: ("f1bcfc60-59c3-5091-99ca-a5c81b13f6b6", "Lloyd T Thomas"),
    26: ("101cde46-ba70-5bb4-9dbb-04dd02c75096", "Lorres C Thomas"),
    27: ("2cc7cf60-0256-5442-9eb9-4b452b20f8a6", "Margaret Thomas"),
    28: ("54c9e6d9-fac7-559b-a6b4-6a1d1970383b", "Martha E Thomas"),
    29: ("e2dd9b24-eeaf-5765-83cc-afd7f2938449", "Mary C Thomas"),
    30: ("b9b8b015-4796-5137-b9bd-8bcc7228e6c3", "Melen E Thomas"),
    31: ("0763cce9-6235-5eff-8672-c82aa0ee7bc9", "Otaway M Thomas"),
    32: ("ca4335f3-d926-5d2d-8129-a26267b033c8", "Richard A Thomas"),
    33: ("0c6563ee-519e-5ee1-a7cf-949ac6ef1d01", "Richard B Thomas"),
    34: ("3cc76513-1dd0-5b56-bb1c-38f7bac4503d", "Roosevelt Thomas"),
    35: ("75d7d142-63ec-5319-ab54-44b9a9bc3ff9", "Rudolph Thomas"),
    36: ("72f771c2-2f4f-5853-811e-9b4c6fb439c0", "Ruth E Thomas"),
    37: ("560a03c8-5f9a-54f9-bcce-1637871a09f8", "Sidney S Thomas"),
    38: ("ee1f713c-aaf1-5b26-82c2-57718bd18007", "Thomas H Thomas"),
    39: ("f33765df-f93d-5ca9-8630-6d0cc2f32d71", "Wilfred Thomas"),
    40: ("c7fca1a6-69e9-5194-b841-f58a7ab6b688", "William H Thomas"),
    41: ("370c487f-8c13-5bf4-ad54-04b2a4a2996a", "William J Thomason"),
    42: ("d37e4799-3e65-5298-8a88-305db958013c", "Harvey W Thomasson"),
    43: ("7b9a42c7-87aa-5133-a3ab-60dd72458c8d", "Stefan A Thomasson"),
    44: ("544f416b-ca58-5f26-b2d2-f68cd03c7bdd", "Paul P Thomle"),
    45: ("c90e461d-215c-5e44-aa88-77a5cc478f58", "Allen R Thompson"),
    46: ("756e5e56-0715-500f-98fd-aa07095efe1f", "Allen J Thompson"),
}


ARMY_RECORDS = [
    {
        "row": 35,
        "date": "1943-05-19",
        "code": "316",
        "occupation": "farm hand on a general farm",
        "label": "Farm hands, general farms",
        "locator": "PDF physical page 172; historical category 3-16",
    },
    {
        "row": 39,
        "date": "1942-03-02",
        "code": "768",
        "occupation": "packing, filling, labeling, marking, bottling, or related work, not elsewhere classified",
        "label": "Packing, filling, labeling, marking, bottling, and related occupations, n.e.c.",
        "locator": "PDF physical page 175; historical category 7-68",
    },
    {
        "row": 42,
        "date": "1942-10-26",
        "code": "157",
        "occupation": "insurance salesman",
        "label": "Salesmen, insurance",
        "locator": "PDF physical page 171; historical category 1-57",
    },
]


UNRESOLVED = {
    24: "The common name produced no OSS, Box 773 or corroborating identity bridge and no reliable pre-OSS affiliation.",
    25: "Exact-name and meaningful-variant searches produced namesakes but no OSS, Box 773 or prewar-employment bridge.",
    27: "The initial-free common name could not be linked to a unique identity, occupation or employer without the personnel file.",
    28: "Exact-name results identified multiple unrelated women and did not establish an OSS identity or pre-OSS chronology.",
    29: "Exact-name, obituary, directory and archival searches did not distinguish the indexed person from common-name alternatives.",
    30: "The unusual printed first name was preserved exactly; no reliable external identity, spelling correction or employer bridge was found.",
    31: "A rare-name World War II Army officer is a plausible lead, but the protected index number is not bridged by an accessible official record. Modern Otaway Thomas and Otaway Thomas III records were rejected as later namesakes.",
    32: "Common-name military, obituary and directory candidates lacked two corroborating identifiers beyond the name.",
    33: "Common-name results lacked a protected-identifier, Box-file or dated OSS bridge and were not assigned.",
    34: "Exact-name searches produced no defensible OSS identity or dated pre-OSS employer evidence.",
    36: "Exact-name and institutional searches produced several namesakes without a corroborating OSS or Box-file identifier.",
    37: "Exact-name, military and obituary searches did not establish a unique OSS identity or pre-OSS affiliation.",
    38: "The repeated first and last name produced ambiguous results and no corroborating identifier or employer chronology.",
    40: "The short protected number was absent from the reviewed official Army registers, and common-name results did not identify the indexed person.",
    41: "The short protected number and exact name did not yield a defensible official identity or pre-OSS employer bridge.",
    43: "A 1963 Washington court record and unverified memorial candidates were retained as namesake leads only; neither bridges the protected index record to OSS or pre-OSS work.",
    45: "Common-name obituary and employment results lacked an OSS, Box 774 or corroborating identity bridge.",
    46: "The short protected number was absent from the reviewed official Army registers, and exact-name results remained ambiguous.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def box_for(row: int) -> str:
    return "773" if row <= 40 else "774"


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 773-774",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 465, rows 24-46; checked against layout-preserving text and a 220 dpi page render",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. Lewis V. Thomas and Allen J. Thompson were visually checked as the cohort boundaries. Full protected identifiers remain private.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; three reviewed Batch 950 candidates; protected identifiers withheld",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "No raw bulk row or full protected identifier is retained in public assets. The three historical occupation categories name no employer or workplace.",
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
            "locator": "PDF physical pages 171, 172 and 175; reviewed historical categories 1-57, 3-16 and 7-68",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical occupation labels are qualified and never converted into named employers or immediate OSS predecessors.",
        },
        {
            "key": REGISTER,
            "stable_url": "https://archive.org/details/officialarmyregi1947unit",
            "archival_identifier": "War Department, Official Army Register, Volume I, 1 January 1947",
            "title": "Official Army Register, Volume I, 1 January 1947",
            "author_creator": "United States War Department, Adjutant General's Office",
            "repository_publisher": "United States Government Printing Office; digitized copy hosted by Internet Archive",
            "publication_record_date": "1947-01-01",
            "locator": "Volume I, printed page 1112, entry for Thomas, Lorres C.; protected officer identifier withheld",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "Official Army Register",
            "rights_notes": "The government register was inspected locally from the public-domain scan and OCR. The public citation omits the full officer identifier.",
        },
        {
            "key": CASUALTY,
            "stable_url": "https://nara-media-001.s3.amazonaws.com/arcmedia/media/images/29/21/29-2067a.gif",
            "archival_identifier": "National Archives Identifier 305324",
            "title": "World War II Honor List of Dead and Missing Army and Army Air Forces Personnel from Wisconsin, 1946",
            "author_creator": "War Department, Adjutant General's Office, Strength Accounting Branch",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1946",
            "locator": "Wisconsin page 22, Milwaukee County, final entry; protected identifier withheld; page image visually inspected",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army casualties: Wisconsin",
            "rights_notes": "The image identifies Paul P. Thomle as a private who died of wounds. It supports identity and wartime Army status, not a pre-OSS employer or exact OSS sequence.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": US_ARMY,
            "organization_id": "28a26f92-78af-5a1a-9c09-a843eb5975b4",
            "canonical_name": "United States Army",
            "historical_name": "Army of the United States",
            "aliases": ["U.S. Army"],
            "organization_type": "military service",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "Existing canonical organization reused. Army service is modeled as military assignment, not civilian employment.",
        },
        {
            "key": USMA,
            "organization_id": "a6458663-2447-50ce-aa34-4a72ffa79348",
            "canonical_name": "United States Military Academy",
            "historical_name": "United States Military Academy at West Point",
            "aliases": ["U.S.M.A.", "West Point"],
            "organization_type": "military academy",
            "sector": "academia_and_research",
            "city": "West Point",
            "state_or_region": "New York",
            "country": "United States",
            "normalization_notes": "Existing canonical organization reused. Cadet status is classified as student, not employment.",
        },
    ]


def occupation_affiliation(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    return {
        "key": f"{slug(PEOPLE[row][1])}-occupation-b950",
        "person_id": PEOPLE[row][0],
        "occupation": item["occupation"],
        "relationship_type": "employment",
        "end_date": item["date"],
        "date_precision": f"Historical civilian-occupation code {item['code']} was recorded at Army entry on {item['date']}; no employer, workplace or OSS-transfer date is named.",
        "country": "United States",
        "immediate_pre_oss": False,
        "last_civilian_pre_service": False,
        "pre_oss_temporal_basis": "strongly_date_bounded",
        "identity_confidence": "high_confidence",
        "claim_confidence": "medium",
        "source_quality": "A_direct_official",
        "publication_status": "publish_qualified",
        "research_notes": "The historical category is not converted into a named employer, workplace, immediate affiliation or exact modern job title.",
    }


def affiliations() -> list[dict[str, object]]:
    values = [occupation_affiliation(item) for item in ARMY_RECORDS]
    values.extend(
        [
            {
                "key": "lorres-thomas-usma-b950",
                "person_id": PEOPLE[26][0],
                "organization_key": USMA,
                "organization_name_as_found": "U. S. M. A.",
                "role_title": "cadet",
                "relationship_type": "student",
                "start_date": "1940-07-01",
                "end_date": "1943-06-01",
                "date_precision": "The 1947 Official Army Register gives cadet status from 1 July 1940 and a 1943 U.S.M.A. B.S.; it records his Corps of Engineers commission on 1 June 1943.",
                "city": "West Point",
                "state_or_region": "New York",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "temporal_relation_uncertain",
                "identity_confidence": "confirmed",
                "claim_confidence": "confirmed",
                "source_quality": "A_direct_official",
                "publication_status": "published",
                "research_notes": "Cadet status is a student affiliation, not employment. The accessible sources do not establish its exact relationship to the indexed OSS personnel file.",
            },
            {
                "key": "lorres-thomas-army-b950",
                "person_id": PEOPLE[26][0],
                "organization_key": US_ARMY,
                "organization_name_as_found": "Corps of Engineers",
                "role_title": "second lieutenant, Corps of Engineers",
                "relationship_type": "military_assignment",
                "start_date": "1943-06-01",
                "date_precision": "The 1947 Official Army Register records commissioning as second lieutenant, Corps of Engineers, on 1 June 1943; it does not supply the OSS transfer date.",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "temporal_relation_uncertain",
                "identity_confidence": "confirmed",
                "claim_confidence": "confirmed",
                "source_quality": "A_direct_official",
                "publication_status": "published",
                "research_notes": "Army service is not labeled a civilian employer. Box 773 is needed to establish whether it was the immediate predecessor to OSS service.",
            },
        ]
    )
    return values


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


def army_claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for item in ARMY_RECORDS:
        row = int(item["row"])
        name = PEOPLE[row][1]
        values.append(
            claim(
                row,
                f"identity-{slug(name)}-b950",
                "identity",
                f"The indexed {name} is a high-confidence match to the reviewed official Army record.",
                "A nonshared protected identifier connects the visually verified index row to the official Army record, and the indexed name agrees with the Army form.",
                "High confidence from a private nonshared identifier plus name agreement.",
                "The Army record dates entry into service but does not establish the exact OSS transfer date.",
                "A_direct_official",
                "high",
                [
                    {"source_key": INDEX, "locator_override": f"PDF page 465 row {row}; protected identifier withheld"},
                    {"source_key": ARMY, "locator_override": "Reviewed name record; protected identifier withheld"},
                    {"source_key": TECH, "support_type": "context_only", "locator_override": "Field definitions, PDF physical pages 44-46"},
                ],
                "This identity decision does not itself establish a named employer or immediate OSS predecessor.",
            )
        )
        values.append(
            claim(
                row,
                f"occupation-{slug(name)}-b950",
                "occupation",
                f"At Army entry on {item['date']}, {name}'s record carried the historical civilian-occupation category {item['label']}; no employer is named.",
                f"The official bulk record supplies code {item['code']}; the visually reviewed NARA code list expands it as {item['label']}.",
                "High confidence from the accepted protected-identifier bridge and name agreement.",
                "Strongly date-bounded at Army entry, but not shown to be the immediate pre-OSS affiliation.",
                "A_direct_official",
                "medium",
                [
                    {"source_key": ARMY, "locator_override": f"Army entry {item['date']}; code {item['code']}; identifier withheld"},
                    {"source_key": CODES, "locator_override": item["locator"]},
                ],
                "Published only as a qualified historical occupation category. No workplace or named employer is inferred.",
                f"{slug(name)}-occupation-b950",
                "publish_qualified",
            )
        )
    return values


def lorres_claims() -> list[dict[str, object]]:
    return [
        claim(
            26,
            "identity-lorres-thomas-b950",
            "identity",
            "Indexed Lorres C. Thomas is confirmed as Army officer Lorres Charles Thomas.",
            "The visually verified OSS index and the 1947 Official Army Register agree in the distinctive name, middle initial and protected officer identifier.",
            "Confirmed by exact protected-identifier agreement between two direct official records plus the distinctive name.",
            "The Army register supplies a service chronology but not the OSS file's entry or transfer date.",
            "A_direct_official",
            "confirmed",
            [
                {"source_key": INDEX, "locator_override": "PDF page 465 row 26; protected officer identifier withheld"},
                {"source_key": REGISTER, "locator_override": "Volume I, printed page 1112; protected officer identifier withheld"},
            ],
            "The public claim expands the middle initial from the official register while withholding the full officer identifier.",
        ),
        claim(
            26,
            "student-lorres-thomas-usma-b950",
            "other_pre_oss_affiliation",
            "Lorres C. Thomas was a United States Military Academy cadet from July 1940 until his June 1943 commissioning.",
            "The Official Army Register records cadet status from 1 July 1940, a 1943 U.S.M.A. B.S., and commissioning on 1 June 1943.",
            "Confirmed exact identity from protected-identifier agreement.",
            "The dated cadet period precedes commissioning, but the source does not date his OSS personnel-file relationship.",
            "A_direct_official",
            "confirmed",
            [{"source_key": REGISTER, "locator_override": "Volume I, printed page 1112; education and appointment chronology"}],
            "Published as student status, never as employment. Excluded from employer analytics.",
            "lorres-thomas-usma-b950",
        ),
        claim(
            26,
            "army-lorres-thomas-b950",
            "other_pre_oss_affiliation",
            "Lorres C. Thomas was commissioned a second lieutenant in the U.S. Army Corps of Engineers on June 1, 1943.",
            "The Official Army Register records the Corps of Engineers commission and later Army ranks.",
            "Confirmed exact identity from protected-identifier agreement.",
            "The military appointment is explicit; whether it immediately preceded OSS service requires the personnel file.",
            "A_direct_official",
            "confirmed",
            [{"source_key": REGISTER, "locator_override": "Volume I, printed page 1112; Corps of Engineers chronology"}],
            "Modeled as military assignment, not civilian employment, and excluded from immediate-affiliation analytics until Box 773 resolves the sequence.",
            "lorres-thomas-army-b950",
        ),
    ]


def paul_claims() -> list[dict[str, object]]:
    return [
        claim(
            44,
            "identity-paul-thomle-b950",
            "identity",
            "Indexed Paul P. Thomle is confirmed as the Army private listed in the 1946 Wisconsin casualty honor list.",
            "The visually verified OSS index and the NARA casualty image agree in the exact uncommon name and protected service identifier; the casualty list records rank private and died of wounds.",
            "Confirmed by exact protected-identifier agreement and the uncommon full name across two direct official records.",
            "The 1944 casualty status does not establish when or how the indexed OSS personnel relationship occurred.",
            "A_direct_official",
            "confirmed",
            [
                {"source_key": INDEX, "locator_override": "PDF page 465 row 44; protected service identifier withheld"},
                {"source_key": CASUALTY, "locator_override": "Wisconsin page 22, Milwaukee County, final entry; protected identifier withheld"},
            ],
            "This identity claim does not infer a pre-OSS employer, wartime unit or sequence. Box 774 remains necessary.",
        )
    ]


def archival_update(row: int, reason: str) -> dict[str, object]:
    person_id, name = PEOPLE[row]
    box = box_for(row)
    return {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, Box {box} and archive location 230/86/42/01. {reason}",
        "personnel_category": "unknown_or_indeterminate",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": f"Review Box {box} for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
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
        "next_action": f"Review Box {box_for(row)} to establish the immediate pre-OSS affiliation and named last civilian employer; do not convert the Army category into a workplace.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }
    if row == 39:
        update["name_variants"] = ["Wilfred J Thomas"]
    return update


def person_updates() -> list[dict[str, object]]:
    values = [archival_update(row, reason) for row, reason in UNRESOLVED.items()]
    values.extend(army_update(item) for item in ARMY_RECORDS)
    values.extend(
        [
            {
                "person_id": PEOPLE[26][0],
                "identity_status": "confirmed",
                "identity_evidence": "The distinctive name, middle initial and protected officer identifier agree exactly between the visually verified OSS index and the 1947 Official Army Register.",
                "name_variants": ["Lorres Charles Thomas", "Captain Lorres C Thomas"],
                "personnel_category": "commissioned_army_officer",
                "commissioned_officer": True,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Review Box 773 to date the OSS relationship and determine whether the Corps of Engineers assignment immediately preceded it and whether any civilian employer preceded West Point or Army service.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[44][0],
                "identity_status": "confirmed",
                "identity_evidence": "The uncommon full name and protected service identifier agree exactly between the visually verified OSS index and the NARA Wisconsin casualty honor list.",
                "personnel_category": "enlisted_army_personnel",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Review Box 774 to establish Paul P. Thomle's OSS relationship, wartime chronology and last civilian employer; the casualty list supplies identity and status only.",
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
            detail = "An accepted protected-identifier Army bridge supports identity and a dated historical occupation category without naming an employer."
        elif row == 26:
            outcome, reviewed, rejected, detail = "source_reviewed", 10, 5, "The 1947 Official Army Register exactly matches the protected officer identifier and documents West Point cadet status and Corps of Engineers commissioning; the OSS transition date and civilian employer remain unresolved."
        elif row == 44:
            outcome, reviewed, rejected, detail = "source_reviewed", 9, 5, "The visually reviewed NARA Wisconsin casualty image exactly matches the protected service identifier and uncommon name; it supports identity and Army status only."
        else:
            raise AssertionError(f"Missing Batch 950 outcome for row {row}")
        attempts.append(
            {
                "key": f"page465-row{row}-{slug(name)}-b950",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index and public Archives context; CIA Reading Room or equivalent official-source check; exact-name and meaningful variants; OSS and military clues; employer and occupation 1940; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Boxes 773-774; protected identifiers used privately only when defensible",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_950",
                "started_at": "2026-10-28T17:30:00Z",
                "completed_at": "2026-10-28T20:10:00Z",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search snippets, family-tree assertions, people-finder pages, current Otaway Thomas/Arkham Technology records, postwar-only leads and sources without an OSS, protected-identifier or Box-file bridge were not assigned. Stefan A. Thomasson's 1963 court record was not treated as an identity bridge.",
                "research_notes": f"{detail} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain, CIA Reading Room and Library of Congress searches were checked as applicable. The index and admitted Army, code-list, register or casualty sources were visually reviewed. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": f"Review Box {box_for(row)} for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before wartime service.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b950-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-950-v1",
        "reviewer": "Before OSS Batch 950 evidence review",
        "sources": sources(),
        "organizations": organizations(),
        "affiliations": affiliations(),
        "claims": army_claims() + lorres_claims() + paul_claims(),
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }
    EvidenceBundle.model_validate(bundle)
    OUTPUT.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
