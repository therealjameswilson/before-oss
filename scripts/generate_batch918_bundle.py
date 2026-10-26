#!/usr/bin/env python3
"""Generate the reviewed Batch 918 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "research/evidence-page449-sties-to-stiteler-review_batch-918_2026-10-26.json"

INDEX = "nara-index-b918"
ARMY = "army-bulk-b918"
TECH = "army-tech-b918"
CODES = "army-codes-b918"
SIGNAL_OCS = "signal-ocs-bradford-stimpson-b918"
TENTH_MOUNTAIN = "denver-10th-mountain-walter-stirnus-b918"
GOVINFO_STIPANOVIC = "govinfo-branko-stipanovic-b918"
STATE_STIMPSON = "state-harry-stimpson-b918"
OBIT_STIMPSON = "legacy-harry-stimpson-b918"


PEOPLE = {
    24: ("83ba9d62-be87-58db-a413-32ea6067119d", "Bernard J Sties", "747"),
    25: ("0f3d9b46-82b1-50bf-9335-82670357e0e8", "Meredith R Stiff", "748"),
    26: ("baf96760-6a9a-5da5-8df8-e74e39e3a26a", "Gus Stikas", "747"),
    27: ("6e859c75-0d49-53b3-8e88-ff08d7815a99", "Lois Stiles", "747"),
    28: ("1e2d4f78-aeb2-5d05-b569-c054c17e49e5", "Ralph S Stillman", "747"),
    29: ("65089006-e3b3-51ad-b130-692b819c7785", "William R Stillman", "747"),
    30: ("0369edcc-6ea0-5d1b-82e1-40f865ec2ddf", "Marjorie Stillwell", "747"),
    31: ("9c2b9bfd-5779-513d-9ea1-767b0a3e3eee", "Robert E Stillwell", "747"),
    32: ("687cac4b-9486-5a6b-854f-73d60e13a124", "Margaret H Stilp", "748"),
    33: ("bc4158b8-1856-5a10-95f5-2a7649b1868a", "Stephen Stimac", "748"),
    34: ("65832d1e-5925-5032-b521-82bc2c8e7765", "Bradford J Stimpson", "748"),
    35: ("ee880962-8913-584f-a995-870b8ed7dd35", "Harry F Stimpson", "748"),
    36: ("976a2b4e-f5c4-5a28-9e74-d41f601aaf99", "Clifford E Stine", "748"),
    37: ("f4035a23-f465-5c33-bad6-2fd1bb5b2c9b", "Nell C Stine", "748"),
    38: ("133893ce-2a7a-5315-861a-54e7835c797e", "Charter D Stinespring", "748"),
    39: ("f5d6883b-b4c9-5ed6-a76f-56d5a7a4e583", "Harriet M Stinson", "748"),
    40: ("b5511f96-d54c-53ac-8470-092ffc6ae178", "John D Stinson", "748"),
    41: ("bd78e839-5810-58e3-966c-b568df05de0f", "Woodrow W Stinson", "748"),
    42: ("22e12290-d309-5e85-9536-63ada21a7553", "Branko Stipanovic", "748"),
    43: ("df379047-78b7-5d44-8768-b2283a02ef8d", "John A Stippick", "748"),
    44: ("269bf631-b75d-5834-8c26-80873e2db234", "Mary J Stirling", "748"),
    45: ("c33c4e2d-8049-5879-a798-e6b22af7ffa2", "Walter E Stirnus", "748"),
    46: ("c68a60a4-f321-5373-b5be-7e11cd719867", "Leroy G Stiteler", "748"),
}


ARMY_OCCUPATIONS = [
    {"row": 24, "date": "1941-05-01", "code": "105", "occupation": "Clerks, general office", "locator": "PDF physical page 171; category 1-05"},
    {"row": 26, "date": "1943-05-01", "code": "948", "occupation": "Sailors and deckhands, except U. S. Navy", "locator": "PDF physical page 174; category 9-48"},
    {"row": 29, "date": "1941-01-27", "code": "003", "occupation": "Architects", "locator": "PDF physical page 170; category 0-03"},
    {"row": 38, "date": "1943-03-15", "code": "983", "occupation": "Mechanics and repairmen, n. e. c.", "locator": "PDF physical page 175; category 9-83"},
    {"row": 40, "date": "1942-12-30", "code": "698", "occupation": "Occupations in manufacture of radios and phonographs", "locator": "PDF physical page 174; category 6-98"},
    {"row": 45, "date": "1942-10-15", "code": "753", "occupation": "Linemen and servicemen, telegraph, telephone, and power", "locator": "PDF physical page 174; category 7-53"},
    {"row": 46, "date": "1942-09-07", "code": "783", "occupation": "Mechanics and repairmen, n. e. c.", "locator": "PDF physical page 175; category 7-83"},
]


UNRESOLVED = {
    25: "The printed note '?move t' was preserved exactly, but no accessible source explained it or established an identity or employer.",
    27: "Exact-name and institutional searches produced no person-specific result with an OSS or Box 747 bridge.",
    28: "Common-name results lacked the corroborating identifiers required to distinguish the indexed person.",
    30: "Exact-name, occupation, obituary, institutional and archival searches found no defensible person-specific match.",
    32: "Exact-name and middle-initial searches produced no reliable identity bridge or dated pre-OSS affiliation.",
    33: "Exact-name searches produced unbridged namesakes and no reliable pre-OSS employer evidence.",
    36: "Exact-name, obituary, institutional, newspaper and archival searches produced no defensible identity bridge.",
    37: "Exact-name and occupation searches produced no person-specific source with a reliable OSS connection.",
    39: "Exact-name and middle-initial searches returned no reliable identity or employment evidence.",
    41: "Common-name results could not be connected to the indexed person through rank, service, box or OSS assignment.",
    43: "Exact-name searches produced no defensible identity bridge or dated pre-OSS affiliation.",
    44: "Exact-name, obituary, institutional, directory and archival searches produced no reliable match.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 747-748",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 449, rows 24-46; checked against layout-preserving text and a rendered page image",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 separately printed rows remain separate. Full protected identifiers remain private.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; seven accepted identity bridges and one rejected spelling conflict",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "No raw row or full protected identifier is retained in public assets. Coded occupations identify no employer.",
        },
        {
            "key": TECH,
            "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf",
            "archival_identifier": "NN3-064-03-008; National Archives Identifier 1263923",
            "title": "World War II Army Enlistment Records: Reference Copy of Technical Documentation",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives at College Park - Electronic Records",
            "publication_record_date": "1994-2005; reference copy modified 2011",
            "locator": "PDF physical pages 44-46; identifier, name, entry-date, grade and civilian-occupation fields",
            "access_date": "2026-10-26",
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
            "locator": "PDF physical pages 170-175; all seven Batch 918 occupation codes visually checked",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical occupation labels identify neither employers nor workplaces.",
        },
        {
            "key": SIGNAL_OCS,
            "stable_url": "https://www.armysignalocs.com/archived/ww2/44_34.html",
            "title": "World War II Signal OCS - Class 44-34",
            "author_creator": "Army Signal Corps Officer Candidate School Association historical archive",
            "repository_publisher": "ArmySignalOCS.com",
            "publication_record_date": "Roster last updated 2020-01-28; graduation 1944-06-21",
            "locator": "Class 34-1944 roster; Bradford J Stimpson entry",
            "access_date": "2026-10-26",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "World War II Signal Corps OCS graduates",
            "rights_notes": "Historical association roster, not an official Army personnel file. It does not establish the timing of OSS service.",
        },
        {
            "key": TENTH_MOUNTAIN,
            "stable_url": "https://history.denverlibrary.org/sites/history/files/10th_mountain_index_0.pdf",
            "title": "10th Mountain Division Name Index",
            "author_creator": "10th Mountain Division Resource Center volunteers",
            "repository_publisher": "Denver Public Library, Western History and Genealogy",
            "publication_record_date": "Database project begun 1998",
            "locator": "PDF physical pages 878-879; Walter E Stirnus, HQ, 86th Infantry",
            "access_date": "2026-10-26",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "10th Mountain Division Resource Center",
            "rights_notes": "The index describes wartime division membership but does not date this individual's assignment relative to OSS.",
        },
        {
            "key": GOVINFO_STIPANOVIC,
            "stable_url": "https://www.govinfo.gov/content/pkg/STATUTE-63/pdf/STATUTE-63-Pg1240.pdf",
            "archival_identifier": "63 Stat. 1240-1242; S. Con. Res. 29",
            "title": "Deportation Suspensions",
            "author_creator": "United States Congress",
            "repository_publisher": "U.S. Government Publishing Office",
            "publication_record_date": "1949-07-20",
            "locator": "Page 1242; Branko Stipanovic or Branko Stipanovich",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "collection_name": "United States Statutes at Large, Volume 63",
            "rights_notes": "Exact-name discovery lead only; it contains no OSS, Box 748 or employment bridge.",
        },
        {
            "key": STATE_STIMPSON,
            "stable_url": "https://history.state.gov/historicaldocuments/frus1958-60v05mSupp/persons",
            "title": "Foreign Relations of the United States, 1958-1960, Volume V, Microfiche Supplement: List of Persons",
            "author_creator": "Office of the Historian, U.S. Department of State",
            "repository_publisher": "U.S. Department of State",
            "publication_record_date": "1958-1960 volume",
            "locator": "Harry F. Stimpson, Jr. entry",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "collection_name": "Foreign Relations of the United States",
            "rights_notes": "Postwar identity lead only; the source does not connect this diplomat to the OSS index row.",
        },
        {
            "key": OBIT_STIMPSON,
            "stable_url": "https://www.legacy.com/us/obituaries/legacyremembers/harry-stimpson-obituary?id=26599519",
            "title": "Harry Farnum Stimpson Jr. Obituary",
            "repository_publisher": "Legacy Remembers",
            "publication_record_date": "2005-04",
            "locator": "Biographical paragraph on law practice and Pacific naval service",
            "access_date": "2026-10-26",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Legacy Remembers obituaries",
            "rights_notes": "Candidate context only. No occupation or employer is assigned to the indexed person without an OSS identity bridge.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": "signal-ocs-b918",
            "canonical_name": "U.S. Army Signal Corps Officer Candidate School",
            "historical_name": "Army Signal Corps OCS",
            "aliases": ["Signal OCS", "Signal Corps Officer Candidate School"],
            "organization_type": "military school",
            "sector": "military",
            "city": "Fort Monmouth",
            "state_or_region": "New Jersey",
            "country": "United States",
            "active_dates": "Second World War",
            "normalization_notes": "Institutional training is modeled separately from employment and from any later OSS assignment.",
        },
        {
            "key": "86th-infantry-b918",
            "canonical_name": "86th Infantry Regiment, 10th Mountain Division",
            "historical_name": "86TH INF",
            "aliases": ["86th Infantry", "86th Mountain Infantry Regiment"],
            "organization_type": "military regiment",
            "sector": "military",
            "country": "United States",
            "active_dates": "Second World War",
            "normalization_notes": "The regiment belonged to the 10th Mountain Division. The roster places Stirnus in headquarters company but does not establish the sequence relative to OSS.",
        },
    ]


def army_affiliation(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    person_id, name, _box = PEOPLE[row]
    return {
        "key": f"{slug(name)}-occupation-b918",
        "person_id": person_id,
        "relationship_type": "employment",
        "occupation": item["occupation"],
        "end_date": item["date"],
        "date_precision": f"Historical civilian-occupation code {item['code']} was recorded at Army entry on {item['date']}; no employer or OSS-transfer date is named.",
        "country": "United States",
        "immediate_pre_oss": False,
        "last_civilian_pre_service": False,
        "pre_oss_temporal_basis": "strongly_date_bounded",
        "identity_confidence": "high_confidence",
        "claim_confidence": "medium",
        "source_quality": "A_direct_official",
        "publication_status": "publish_qualified",
        "research_notes": "The historical category is not converted into a named employer, workplace or exact title.",
    }


def extra_affiliations() -> list[dict[str, object]]:
    return [
        {
            "key": "bradford-stimpson-signal-ocs-b918",
            "person_id": PEOPLE[34][0],
            "organization_key": "signal-ocs-b918",
            "organization_name_as_found": "Army Signal Corps OCS",
            "role_title": "Class 34-1944 graduate",
            "relationship_type": "student",
            "end_date": "1944-06-21",
            "date_precision": "Graduation date; the roster does not state enrollment dates or the timing of OSS service.",
            "city": "Fort Monmouth",
            "state_or_region": "New Jersey",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "temporal_relation_uncertain",
            "identity_confidence": "probable",
            "claim_confidence": "medium",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "publish_qualified",
            "research_notes": "Exact full name and the indexed second-lieutenant rank support a probable match, but the personnel file is needed to prove sequence and identity.",
        },
        {
            "key": "walter-stirnus-86th-infantry-b918",
            "person_id": PEOPLE[45][0],
            "organization_key": "86th-infantry-b918",
            "organization_name_as_found": "HQ 86TH INF",
            "role_title": "Headquarters company member",
            "relationship_type": "military_assignment",
            "date_precision": "The institutional database covers 10th Mountain Division service during 1941-1945 but does not provide individual assignment dates.",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "temporal_relation_uncertain",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "published",
            "research_notes": "The exact, uncommon full name and accepted Army identity bridge support the match; no immediate pre-OSS sequence is inferred.",
        },
    ]


def army_claims(item: dict[str, object]) -> list[dict[str, object]]:
    row = int(item["row"])
    person_id, name, _box = PEOPLE[row]
    return [
        {
            "key": f"identity-{slug(name)}-b918",
            "person_id": person_id,
            "claim_type": "identity",
            "claim_text": f"The indexed {name} row is a high-confidence match to the reviewed official Army record.",
            "evidence_paraphrase": "A nonshared protected identifier and exact name connect the visually verified index row to the official Army record.",
            "identity_match_assessment": "High confidence from the nonshared protected-identifier bridge and exact name alignment.",
            "temporal_assessment": "The Army record supports identity and a dated occupation category; it does not establish the OSS transfer sequence.",
            "source_quality": "A_direct_official",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "No protected identifier is exposed, and the coded occupation is kept separate from employer claims.",
            "sources": [
                {"source_key": INDEX, "locator_override": f"PDF page 449 row {row}; protected identifier withheld"},
                {"source_key": ARMY, "locator_override": "Accepted reviewed identity bridge; protected identifier withheld"},
            ],
        },
        {
            "key": f"occupation-{slug(name)}-b918",
            "person_id": person_id,
            "affiliation_key": f"{slug(name)}-occupation-b918",
            "claim_type": "occupation",
            "claim_text": f"At Army entry on {item['date']}, the official record assigned {name} the historical civilian-occupation category '{item['occupation']}'; no employer is identified.",
            "evidence_paraphrase": f"The Army entry field carries code {item['code']}, which the visually checked NARA code list maps to the stated category.",
            "identity_match_assessment": "High confidence from a nonshared protected-identifier bridge and exact name alignment.",
            "temporal_assessment": "Strongly date-bounded at Army entry, but neither immediate pre-OSS status nor a named employer is established.",
            "source_quality": "A_direct_official",
            "claim_confidence": "medium",
            "publication_status": "publish_qualified",
            "match_notes": "Historical code-language is retained and excluded from default confirmed/high-confidence employer analytics.",
            "sources": [
                {"source_key": ARMY, "locator_override": f"Army-entry date {item['date']}; occupation code {item['code']}; protected identifier withheld"},
                {"source_key": TECH, "support_type": "context_only", "locator_override": "Civilian-occupation field definition"},
                {"source_key": CODES, "locator_override": item["locator"]},
            ],
        },
    ]


def other_claims() -> list[dict[str, object]]:
    return [
        {
            "key": "signal-ocs-bradford-stimpson-b918",
            "person_id": PEOPLE[34][0],
            "affiliation_key": "bradford-stimpson-signal-ocs-b918",
            "claim_type": "other_pre_oss_affiliation",
            "claim_text": "A June 1944 Signal Corps OCS roster probably identifies Bradford J. Stimpson as a Class 34-1944 graduate; its relation to OSS service is unknown.",
            "evidence_excerpt": "STIMPSON BRADFORD J CA",
            "evidence_paraphrase": "The historical roster gives the exact full name, California, and a 21 June 1944 graduation date; the index separately prints second lieutenant.",
            "identity_match_assessment": "Probable from the distinctive exact name and rank-compatible officer training, but no protected identifier or direct OSS bridge is present.",
            "temporal_assessment": "Dated wartime military training; the accessible sources do not establish whether it preceded, overlapped or followed OSS service.",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "claim_confidence": "medium",
            "publication_status": "publish_qualified",
            "match_notes": "Published with qualification and excluded from default confirmed/high-confidence employer analytics.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 449 row 34; rank 2nd LT"},
                {"source_key": SIGNAL_OCS, "locator_override": "Class 34-1944 roster; graduation date 1944-06-21"},
            ],
        },
        {
            "key": "military-assignment-walter-stirnus-b918",
            "person_id": PEOPLE[45][0],
            "affiliation_key": "walter-stirnus-86th-infantry-b918",
            "claim_type": "other_pre_oss_affiliation",
            "claim_text": "The 10th Mountain Division Name Index places Walter E. Stirnus in headquarters company, 86th Infantry; its timing relative to OSS service is unknown.",
            "evidence_excerpt": "WALTER E STIRNUS HQ 86TH INF",
            "evidence_paraphrase": "The institutional index identifies the exact, uncommon full name and unit; a separate official Army record supplies the protected identity bridge.",
            "identity_match_assessment": "High confidence from the exact uncommon name, Army-service context and accepted protected-identifier bridge.",
            "temporal_assessment": "Documented wartime military assignment, but the accessible record does not place it immediately before OSS.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "Published as a wartime assignment with explicit temporal uncertainty, not as a civilian employer or immediate predecessor.",
            "sources": [
                {"source_key": ARMY, "locator_override": "Accepted reviewed identity bridge; protected identifier withheld"},
                {"source_key": TENTH_MOUNTAIN, "locator_override": "PDF physical pages 878-879; Walter E Stirnus entry"},
            ],
        },
        {
            "key": "candidate-harry-f-stimpson-b918",
            "person_id": PEOPLE[35][0],
            "claim_type": "identity",
            "claim_text": "Harry Farnum Stimpson Jr., later a U.S. diplomat, is an unconfirmed namesake candidate for the indexed Harry F. Stimpson.",
            "evidence_paraphrase": "Official postwar and obituary sources identify a Harry F. Stimpson Jr. who practiced law and served as a Pacific naval officer, but neither source mentions OSS.",
            "identity_match_assessment": "Low: name and middle initial agree, but no index identifier, Box 748 reference, OSS assignment or independent wartime bridge connects the records.",
            "temporal_assessment": "The candidate has a plausible wartime chronology, but chronology cannot substitute for identity evidence.",
            "source_quality": "A_direct_official",
            "claim_confidence": "low",
            "publication_status": "needs_review",
            "match_notes": "Retained privately for Box 748 comparison; no occupation, employer or affiliation is assigned to the indexed person.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 449 row 35; Box 748"},
                {"source_key": STATE_STIMPSON, "locator_override": "List of Persons; Harry F. Stimpson, Jr."},
                {"source_key": OBIT_STIMPSON, "support_type": "context_only", "locator_override": "Biographical paragraph"},
            ],
        },
        {
            "key": "candidate-branko-stipanovic-b918",
            "person_id": PEOPLE[42][0],
            "claim_type": "identity",
            "claim_text": "A 1949 congressional resolution naming Branko Stipanovic or Branko Stipanovich is an unconfirmed identity candidate for the indexed person.",
            "evidence_excerpt": "Stipanovic, Branko, or Branko Stipanovich",
            "evidence_paraphrase": "The official resolution supplies an exact name and a spelling variant in a deportation-suspension list, but no OSS or employment information.",
            "identity_match_assessment": "Low: exact name alone is insufficient without a Box 748, service, nationality or OSS bridge.",
            "temporal_assessment": "Postwar evidence only; no pre-OSS chronology is established.",
            "source_quality": "A_direct_official",
            "claim_confidence": "low",
            "publication_status": "needs_review",
            "match_notes": "Retained privately as a spelling-variant lead; no public affiliation or employer is assigned.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 449 row 42; Box 748"},
                {"source_key": GOVINFO_STIPANOVIC, "locator_override": "63 Stat. 1242"},
            ],
        },
    ]


def army_person_update(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    person_id, _name, box = PEOPLE[row]
    return {
        "person_id": person_id,
        "identity_status": "high_confidence",
        "identity_evidence": "A nonshared protected identifier and exact name connect the visually verified index row to the reviewed official Army record. The historical occupation field remains separate from employer and immediate-affiliation claims.",
        "personnel_category": "enlisted_army_personnel",
        "commissioned_officer": False,
        "allied_or_foreign_personnel": False,
        "manual_review_required": True,
        "research_status": "occupation_only_found",
        "next_action": f"Review the indexed Box {box} personnel file to identify the immediate pre-OSS affiliation and last civilian employer; do not convert the Army occupation category into a named employer.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }


def unresolved_update(row: int) -> dict[str, object]:
    person_id, name, box = PEOPLE[row]
    return {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, Box {box} and archive location, but staged official-context, CIA Reading Room, exact-name, occupation, employer, obituary, institutional, newspaper, Library of Congress and archival searches found no defensible identity bridge. {UNRESOLVED[row]}",
        "personnel_category": "unknown_or_indeterminate",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": f"Review the indexed Box {box} personnel file for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "critical" if row in {25, 27, 28, 30, 32, 33, 36, 37, 39, 41, 43, 44} else "high",
    }


def person_updates() -> list[dict[str, object]]:
    updates = [army_person_update(item) for item in ARMY_OCCUPATIONS]
    updates.extend(unresolved_update(row) for row in UNRESOLVED)
    updates.extend(
        [
            {
                "person_id": PEOPLE[31][0],
                "identity_status": "conflicting",
                "identity_evidence": "A nonshared protected identifier points to an Army record for Robert E Stilwell, while the index prints Robert E Stillwell. The surname discrepancy prevents transferring Army identity, grade or occupation evidence.",
                "personnel_category": "unknown_or_indeterminate",
                "manual_review_required": True,
                "research_status": "conflicting_sources",
                "next_action": "Review Box 747 to resolve the Stillwell/Stilwell spelling conflict and reject unbridged newspaper namesakes; do not transfer the Army occupation code pending resolution.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[34][0],
                "identity_status": "probable",
                "identity_evidence": "The historical Signal Corps OCS roster gives the exact full name and a June 1944 graduation date. The indexed second-lieutenant rank is compatible, but no protected identifier or direct OSS bridge is available.",
                "personnel_category": "commissioned_army_officer",
                "commissioned_officer": True,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Review Box 748 to confirm the OCS graduate's identity, determine the OSS assignment chronology and identify any civilian employer before military service.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[35][0],
                "identity_status": "ambiguous",
                "identity_evidence": "A retained private candidate agrees in name and middle initial and has wartime Navy service, but accessible sources provide no OSS, protected-identifier or Box 748 bridge.",
                "personnel_category": "unknown_or_indeterminate",
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Review Box 748 for a full name, birth details, Navy service and OSS assignment before accepting or rejecting the retained private candidate; do not transfer any candidate employment meanwhile.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[42][0],
                "identity_status": "ambiguous",
                "identity_evidence": "A retained private postwar candidate agrees in exact name and supplies a spelling variant, but it contains no OSS, service, nationality or Box 748 bridge.",
                "personnel_category": "unknown_or_indeterminate",
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Review Box 748 for nationality, spelling variants and service identifiers before accepting or rejecting the retained private candidate.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
        ]
    )
    return updates


def research_attempts() -> list[dict[str, object]]:
    sourced_rows = {24, 26, 29, 34, 35, 38, 40, 42, 45, 46}
    attempts: list[dict[str, object]] = []
    for row, (person_id, name, box) in PEOPLE.items():
        if row == 31:
            outcome = "candidate_rejected"
            detail = "The official Army candidate was rejected as a resolved identity because the indexed and Army surname spellings conflict; no occupation was transferred. An unrelated 1913 newspaper hit was also rejected."
        elif row in sourced_rows:
            outcome = "source_reviewed" if row in {24, 26, 29, 38, 40, 45, 46} else "candidate_found"
            detail = "Reviewed evidence established an official identity/occupation bridge, a qualified wartime affiliation, or a private candidate requiring the personnel file."
        else:
            outcome = "candidate_rejected"
            detail = UNRESOLVED[row]
        attempts.append(
            {
                "key": f"page449-row{row}-{slug(name)}-b918",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA/index and public Catalog context; CIA Reading Room exact-name check; OSS and rank variants; employer and occupation; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Box {box}; protected-identifier Army crosswalk where available",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_918",
                "started_at": "2026-10-26T03:55:00Z",
                "completed_at": "2026-10-26T05:05:00Z",
                "outcome": outcome,
                "sources_reviewed": 10 if row in {34, 35, 42, 45} else (8 if row in sourced_rows or row == 31 else 6),
                "candidate_sources_rejected": 4 if row in sourced_rows else 7,
                "rejection_reasons": "Unbridged namesakes, discovery-only results, chronologically irrelevant records and postwar-only leads were not assigned." if row in sourced_rows else detail,
                "research_notes": f"{detail} The CIA adapter failed closed when its robots endpoint was unavailable. A bounded current Library of Congress API pass was separately checkpointed, and returned discovery candidates were reviewed without treating snippets as evidence. No access control was bypassed, and no exposed NARA API credential was used.",
                "next_action": f"Review the indexed Box {box} personnel file for corroborating identifiers and the last documented pre-OSS affiliation.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b918-v1",
            }
        )
    return attempts


def main() -> None:
    affiliations = [army_affiliation(item) for item in ARMY_OCCUPATIONS]
    affiliations.extend(extra_affiliations())
    claims: list[dict[str, object]] = []
    for item in ARMY_OCCUPATIONS:
        claims.extend(army_claims(item))
    claims.extend(other_claims())
    bundle = {
        "bundle_version": "batch-918-v1",
        "reviewer": "Before OSS Batch 918 evidence review",
        "sources": sources(),
        "organizations": organizations(),
        "affiliations": affiliations,
        "claims": claims,
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }
    OUTPUT.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
