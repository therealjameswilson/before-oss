#!/usr/bin/env python3
"""Generate the reviewed Batch 907 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "research/evidence-page443-stamoulis-to-stanley-review_batch-907_2026-10-25.json"

INDEX = "nara-index-b907"
ARMY = "army-bulk-b907"
TECH = "army-tech-b907"
CODES = "army-codes-b907"
HOOVER_STAMPADOS = "hoover-oss-stampados-b907"
HAF_HISTORY = "haf-history-b907"
ARSOF_STANFORD = "arsof-clarence-stanford-b907"
WATERFRONT_STANFORD = "mppdc-clarence-stanford-b907"


PEOPLE = {
    24: ("5c4f081c-0157-54b4-8601-ffb36c851ea4", "Thomas S Stamoulis"),
    25: ("12a33d31-8539-54fc-8778-9604cd57e62e", "Demetrius G Stampados"),
    26: ("e7d8cb18-535b-5006-8c3c-6d511a997b97", "Susan C Stampados"),
    27: ("81951af4-37ca-55b8-9ec5-66e80209aff8", "James D Stamper"),
    28: ("9b9b1467-e3fa-5399-8138-d790378ea4e3", "Vincent C Stampone"),
    29: ("596a3916-bb44-5955-8e60-4aee9eaf7788", "Basil J Stanberg"),
    30: ("00c92df5-fea7-5cb8-9f7b-3f5f94634951", "Charles R Standen"),
    31: ("4275343b-5f88-5dce-80fa-fd3a8d970449", "Victor L Stanek"),
    32: ("9fa1606f-115c-5344-bed3-f553167530ee", "Phoebe E Stanfield"),
    33: ("369d4b4a-b7c7-5a5a-af00-a5da9f338583", "Clarence Stanford"),
    34: ("ce18c2b1-9bd4-5cd7-b957-41a784785cf0", "Dorothy M Stanford"),
    35: ("49375915-35a5-5c97-a7bf-8b06cfb46a2c", "Ferdinand F Stanford"),
    36: ("3435d3c4-40df-5661-88fb-e70feb26401a", "George W Stanford"),
    37: ("1a2b8b12-8b9d-599c-8c3f-6cb21b4ce088", "Marie Stanhope"),
    38: ("6ca6bc3e-6112-5adf-b829-8a07e27aa133", "William Stanko"),
    39: ("dc853cf2-d6bb-5d21-921d-09f9a54e953f", "George Stankula"),
    40: ("6c2ebb81-da8b-50ce-9c20-4f1ce56da92f", "Carl T Stanley"),
    41: ("340e3e1b-c7b6-52a5-b985-e9c92e8959eb", "Eugene R Stanley"),
    42: ("e3761d01-ebe3-5fa6-b945-29564cd67251", "Hippolyte L Stanley"),
    43: ("767d1ad9-6711-5917-95c3-1234d6f003c3", "Joseph W Stanley"),
    44: ("5b1ac0d8-9131-5113-8d00-8844c26fe9ee", "Katherine J Stanley"),
    45: ("4c794cd9-83c8-5c28-b2fa-9358d1c739d7", "Leo F Stanley"),
    46: ("801e5aca-5e7e-5de7-b37b-f8485e333c49", "Robert W Stanley"),
}


ARMY_OCCUPATIONS = [
    {"row": 28, "date": "1941-07-14", "code": "081", "occupation": "Advertising agents", "locator": "PDF physical pages 170-171; category 0-81"},
    {"row": 29, "date": "1943-02-05", "code": "866", "occupation": "Unskilled occupations in production of clay products", "locator": "PDF physical page 173; category 8-66"},
    {"row": 31, "date": "1942-09-19", "code": "558", "occupation": "Meatcutters, except in slaughtering and packing houses", "locator": "PDF physical page 174; category 5-58"},
    {"row": 35, "date": "1940-08-26", "code": "525", "occupation": "Carpenters", "locator": "PDF physical page 174; category 5-25"},
    {"row": 38, "date": "1941-07-02", "code": "221", "occupation": "Bartenders", "locator": "PDF physical page 172; category 2-21"},
    {"row": 40, "date": "1942-12-12", "code": "771", "occupation": "Oilers of machinery", "locator": "PDF physical page 177; category 7-71"},
    {"row": 41, "date": "1943-03-02", "code": "048", "occupation": "Draftsmen", "locator": "PDF physical pages 170-171; category 0-48"},
]


UNRESOLVED = {
    26: "Postwar material identifying a family relationship does not establish employment or an independent identity bridge and was excluded.",
    27: "Common-name and genealogy results could not be tied to the indexed R-prefixed identifier or OSS service.",
    30: "Exact-name and spelling-variant searches produced no defensible identity bridge or dated pre-OSS affiliation.",
    32: "Exact-name, obituary, institutional and archival searches produced no person-specific result.",
    34: "Multiple same-name vital-record candidates lacked rank, service, box or OSS corroboration.",
    36: "The printed T/SGT rank establishes enlisted status, but searches found no reliable identity bridge or pre-OSS affiliation.",
    37: "Modern professional and obituary results were chronologically incompatible or lacked an OSS bridge.",
    39: "The NARA index remained the only person-specific result; no reliable employer or occupation source was found.",
    42: "The distinctive full name produced no reliable official, institutional, newspaper or obituary match.",
    43: "Common-name searches returned incompatible candidates, including a 1944 Pennsylvania death entry, without an OSS bridge.",
    44: "Exact-name and variant searches produced no defensible identity or employment evidence.",
    45: "The indexed middle initial F does not support assigning biographies of better-known Leo Stanleys with different initials; no corroborating identifier was found.",
    46: "Numerous same-name military and obituary records could not be connected to the index row, which prints no rank or service identifier.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def archive_box(row: int) -> str:
    return "736" if row <= 36 else "737"


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 736 and 737",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 443, rows 24-46; checked against layout-preserving text and a rendered page image",
            "access_date": "2026-10-25",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain immutable. Full protected identifiers remain private.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; seven accepted identity bridges and one rejected middle-initial conflict",
            "access_date": "2026-10-25",
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
            "access_date": "2026-10-25",
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
            "locator": "PDF physical pages 170-174 and 177; all seven Batch 907 occupation codes visually and textually checked",
            "access_date": "2026-10-25",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical occupation labels identify neither employers nor workplaces.",
        },
        {
            "key": HOOVER_STAMPADOS,
            "stable_url": "https://digitalcollections.hoover.org/internal/media/dispatcher/331573/full",
            "archival_identifier": "Hoover Digital Collections media 331573",
            "title": "Office of Strategic Services [Board proceedings, Caserta and Bari]",
            "author_creator": "Office of Strategic Services",
            "repository_publisher": "Hoover Institution Library & Archives",
            "publication_record_date": "1944-05-04",
            "locator": "PDF viewer pages 48-49, entry XIV; exact name, officer number, chronology and Greek Air Force service",
            "access_date": "2026-10-25",
            "source_quality": "A_direct_official",
            "collection_name": "Office of Strategic Services records in Hoover Digital Collections",
            "rights_notes": "A browser challenge blocked direct download, but the indexed PDF text and complete relevant pages were reviewed through an accessible search rendering. No access control was bypassed.",
        },
        {
            "key": HAF_HISTORY,
            "stable_url": "https://hafa.haf.gr/en/hafa/history/",
            "title": "History",
            "author_creator": "Hellenic Air Force Academy",
            "repository_publisher": "Hellenic Air Force",
            "locator": "Official institutional history, 1931-1951 and World War II sections",
            "access_date": "2026-10-25",
            "source_quality": "B_authoritative_institutional",
            "rights_notes": "Used only to normalize the historical Greek military organization; it does not identify Stampados.",
        },
        {
            "key": ARSOF_STANFORD,
            "stable_url": "https://arsof-history.org/articles/pdf/v5n1_operation_boston.pdf",
            "title": "Operation BOSTON: An OSS Combined Operation in the Indian Ocean",
            "author_creator": "Troy J. Sacquety",
            "repository_publisher": "United States Army Special Operations Command History Office",
            "publication_record_date": "2009",
            "locator": "Acknowledgments identifying Clarence Stanford as a P-101 veteran",
            "access_date": "2026-10-25",
            "source_quality": "B_authoritative_institutional",
            "rights_notes": "Identity lead only. Name agreement without an index identifier is insufficient for publication as the indexed person.",
        },
        {
            "key": WATERFRONT_STANFORD,
            "stable_url": "https://www.mppdc.com/articles/reports/FINAL_MPPDC_WWF_PLAN-RED.pdf",
            "title": "Virginia Working Waterfront Master Plan",
            "author_creator": "Middle Peninsula Planning District Commission",
            "repository_publisher": "Middle Peninsula Planning District Commission",
            "publication_record_date": "2015",
            "locator": "Page 27; postwar profile of Colonial Beach boatbuilder Clarence Stanford",
            "access_date": "2026-10-25",
            "source_quality": "B_authoritative_institutional",
            "rights_notes": "Postwar candidate context only; it is not evidence of pre-OSS employment or an index identity bridge.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": "hellenic-royal-air-force-b907",
            "organization_id": "915b3fa9-f21c-5fb8-85ae-46f98b727af4",
            "canonical_name": "Hellenic Royal Air Force",
            "historical_name": "Air Force [of Greece]",
            "aliases": ["Greek Air Force", "Royal Hellenic Air Force"],
            "organization_type": "air force",
            "sector": "military",
            "country": "Greece",
            "active_dates": "Historical designation during the Second World War",
            "normalization_notes": "The OSS source says only that Stampados was a staff officer of the Air Force in Greece. The historical organization is normalized separately without altering that wording.",
        }
    ]


def army_affiliation(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    person_id, name = PEOPLE[row]
    return {
        "key": f"{slug(name)}-occupation-b907",
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


def stampados_affiliation() -> dict[str, object]:
    return {
        "key": "demetrius-stampados-greek-air-force-b907",
        "person_id": PEOPLE[25][0],
        "organization_key": "hellenic-royal-air-force-b907",
        "organization_name_as_found": "Air Force [in Greece]",
        "role_title": "staff officer",
        "relationship_type": "military_assignment",
        "date_precision": "Before coming to the United States and before entering OSS as a civilian on 11 December 1941; exact start and end dates are not stated.",
        "country": "Greece",
        "immediate_pre_oss": False,
        "last_civilian_pre_service": False,
        "pre_oss_temporal_basis": "documented_prewar",
        "identity_confidence": "confirmed",
        "claim_confidence": "confirmed",
        "source_quality": "A_direct_official",
        "publication_status": "published",
        "research_notes": "The direct OSS report establishes earlier Greek Air Force staff service but does not prove that it immediately preceded OSS or identify a civilian employer.",
    }


def army_claims(item: dict[str, object]) -> list[dict[str, object]]:
    row = int(item["row"])
    person_id, name = PEOPLE[row]
    return [
        {
            "key": f"identity-{slug(name)}-b907",
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
                {"source_key": INDEX, "locator_override": f"PDF page 443 row {row}; protected identifier withheld"},
                {"source_key": ARMY, "locator_override": "Accepted reviewed identity bridge; protected identifier withheld"},
            ],
        },
        {
            "key": f"occupation-{slug(name)}-b907",
            "person_id": person_id,
            "affiliation_key": f"{slug(name)}-occupation-b907",
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


def substantive_claims() -> list[dict[str, object]]:
    return [
        {
            "key": "identity-demetrius-stampados-b907",
            "person_id": PEOPLE[25][0],
            "claim_type": "identity",
            "claim_text": "The indexed Captain Demetrius G. Stampados is confirmed as the OSS officer described in the 4 May 1944 board proceedings.",
            "evidence_paraphrase": "The direct OSS report repeats his exact name, captain rank and officer number, adding a precise entry and commissioning chronology.",
            "identity_match_assessment": "Confirmed by exact full name, rank and the same officer number with a leading-zero formatting difference.",
            "temporal_assessment": "The report states OSS entry as a civilian on 11 December 1941 and commission from civilian life in July 1943.",
            "source_quality": "A_direct_official",
            "claim_confidence": "confirmed",
            "publication_status": "published",
            "match_notes": "The full officer number remains private; the report supplies a direct, person-specific identity bridge.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 443 row 25; Captain; officer number withheld"},
                {"source_key": HOOVER_STAMPADOS, "locator_override": "PDF viewer page 48, entry XIV"},
            ],
        },
        {
            "key": "prewar-demetrius-stampados-greek-air-force-b907",
            "person_id": PEOPLE[25][0],
            "affiliation_key": "demetrius-stampados-greek-air-force-b907",
            "claim_type": "other_pre_oss_affiliation",
            "claim_text": "Before coming to the United States and entering OSS, Demetrius G. Stampados had served as an Air Force staff officer in Greece.",
            "evidence_excerpt": "where he was a staff officer of the Air Force",
            "evidence_paraphrase": "The OSS report describes Greek Air Force staff service and reconnaissance, photo-interpretation, topography and operations training before his U.S. arrival.",
            "identity_match_assessment": "Confirmed by exact name, rank and officer number in the same direct OSS report.",
            "temporal_assessment": "Documented prewar military affiliation; the report does not prove it was immediately before OSS and names no civilian employer.",
            "source_quality": "A_direct_official",
            "claim_confidence": "confirmed",
            "publication_status": "published",
            "match_notes": "Published as an earlier military affiliation, not as a civilian employer or an explicit immediate predecessor.",
            "sources": [
                {"source_key": HOOVER_STAMPADOS, "locator_override": "PDF viewer pages 48-49, entry XIV"},
                {"source_key": HAF_HISTORY, "support_type": "context_only", "locator_override": "Official institutional history, 1931-1951"},
            ],
        },
        {
            "key": "candidate-clarence-stanford-p101-b907",
            "person_id": PEOPLE[33][0],
            "claim_type": "identity",
            "claim_text": "A P-101 veteran named Clarence Stanford is a candidate for the indexed Clarence Stanford, not a resolved identity.",
            "evidence_paraphrase": "A USASOC history thanks the widow of P-101 veteran Clarence Stanford; a regional plan profiles a postwar boatbuilder of that name.",
            "identity_match_assessment": "Ambiguous: the index provides no middle initial, rank or identifier, and relatives cannot serve as the principal identity bridge.",
            "temporal_assessment": "The sources provide OSS and postwar context but no defensible pre-OSS affiliation or transition chronology.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "low",
            "publication_status": "needs_review",
            "match_notes": "Retained privately for Box 736 review; no public affiliation or employer is assigned.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 443 row 33; Box 736"},
                {"source_key": ARSOF_STANFORD, "locator_override": "Acknowledgments; P-101 veteran Clarence Stanford"},
                {"source_key": WATERFRONT_STANFORD, "support_type": "context_only", "locator_override": "Page 27; postwar Colonial Beach boatbuilder"},
            ],
        },
    ]


def army_person_update(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    person_id, _name = PEOPLE[row]
    return {
        "person_id": person_id,
        "identity_status": "high_confidence",
        "identity_evidence": "A nonshared protected identifier and exact name connect the visually verified index row to the reviewed official Army record. The historical occupation field remains separate from employer and immediate-affiliation claims.",
        "personnel_category": "enlisted_army_personnel",
        "commissioned_officer": False,
        "allied_or_foreign_personnel": False,
        "manual_review_required": True,
        "research_status": "occupation_only_found",
        "next_action": "Review the indexed personnel file to identify the immediate pre-OSS affiliation and last civilian employer; do not convert the Army occupation category into a named employer.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }


def unresolved_update(row: int) -> dict[str, object]:
    person_id, name = PEOPLE[row]
    category = "enlisted_army_personnel" if row == 36 else "unknown_or_indeterminate"
    commissioned: bool | None = False if row == 36 else None
    update: dict[str, object] = {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, rank when printed, box and archive location, but staged official-context, CIA Reading Room, exact-name, occupation, employer, obituary, institutional, newspaper, directory, Library of Congress and archival searches found no defensible identity bridge. {UNRESOLVED[row]}",
        "personnel_category": category,
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": f"Review the indexed Box {archive_box(row)} personnel file for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "critical" if row in {27, 32, 34, 37, 42, 43, 44, 45, 46} else "high",
    }
    if commissioned is not None:
        update["commissioned_officer"] = commissioned
        update["allied_or_foreign_personnel"] = False
    return update


def person_updates() -> list[dict[str, object]]:
    updates = [army_person_update(item) for item in ARMY_OCCUPATIONS]
    updates.extend(
        [
            {
                "person_id": PEOPLE[24][0],
                "identity_status": "conflicting",
                "identity_evidence": "The protected identifier agrees with an Army record for Thomas G Stamoulis, but the index prints Thomas S Stamoulis. The middle-initial conflict prevents transferring Army identity or occupation evidence.",
                "personnel_category": "unknown_or_indeterminate",
                "manual_review_required": True,
                "research_status": "conflicting_sources",
                "next_action": "Review Box 736 to resolve the S/G middle-initial conflict; do not transfer the Army occupation code or classify the indexed person from the disputed record.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[25][0],
                "identity_status": "confirmed",
                "identity_evidence": "A direct OSS report repeats Demetrius G. Stampados's exact name, Captain rank and officer number and supplies a precise OSS-entry chronology.",
                "personnel_category": "commissioned_army_officer",
                "commissioned_officer": True,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "completed",
                "next_action": "Review Box 736 to identify any civilian employer immediately before his 11 December 1941 OSS entry and to refine the timing of his earlier Greek Air Force staff service.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[33][0],
                "identity_status": "ambiguous",
                "identity_evidence": "Accessible same-name official and regional sources do not supply a corroborating middle initial, rank, identifier or chronology. The indexed identity therefore remains ambiguous and no candidate is accepted.",
                "personnel_category": "unknown_or_indeterminate",
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Review Box 736 for a full name, middle initial, personnel status, prewar occupation, employer and OSS assignment; do not accept a namesake without independent identifiers.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
        ]
    )
    updates.extend(unresolved_update(row) for row in UNRESOLVED)
    return updates


def research_attempts() -> list[dict[str, object]]:
    sourced_rows = {25, 28, 29, 31, 33, 35, 38, 40, 41}
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        if row == 24:
            outcome = "candidate_rejected"
            detail = "The official Army candidate was rejected as a resolved identity because the middle initial conflicts; no occupation was transferred."
        elif row in sourced_rows:
            outcome = "source_reviewed" if row != 33 else "candidate_found"
            detail = "Reviewed evidence established a direct identity/affiliation bridge, an official identity/occupation bridge, or a private candidate requiring the personnel file."
        else:
            outcome = "candidate_rejected"
            detail = UNRESOLVED[row]
        attempts.append(
            {
                "key": f"page443-row{row}-{slug(name)}-b907",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA/index and public Catalog context; CIA Reading Room exact-name check; OSS and rank variants; employer and occupation; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Box {archive_box(row)}; protected-identifier Army crosswalk where available",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_907",
                "started_at": "2026-10-25T19:05:00Z",
                "completed_at": "2026-10-25T20:05:00Z",
                "outcome": outcome,
                "sources_reviewed": 10 if row in {25, 33} else (8 if row in sourced_rows or row == 24 else 6),
                "candidate_sources_rejected": 4 if row in sourced_rows else 7,
                "rejection_reasons": "Unbridged namesakes, discovery-only results, chronologically irrelevant records and postwar-only leads were not assigned." if row in sourced_rows else detail,
                "research_notes": f"{detail} The dedicated CIA and Library of Congress adapters failed closed after access errors; indexed site-specific discovery checks were completed without treating snippets as evidence. No access control was bypassed, and no exposed NARA API credential was used.",
                "next_action": f"Review the indexed Box {archive_box(row)} personnel file for corroborating identifiers and the last documented pre-OSS affiliation.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b907-v1",
            }
        )
    return attempts


def main() -> None:
    affiliations = [army_affiliation(item) for item in ARMY_OCCUPATIONS]
    affiliations.append(stampados_affiliation())
    claims: list[dict[str, object]] = []
    for item in ARMY_OCCUPATIONS:
        claims.extend(army_claims(item))
    claims.extend(substantive_claims())
    bundle = {
        "bundle_version": "batch-907-v1",
        "reviewer": "Before OSS Batch 907 evidence review",
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
