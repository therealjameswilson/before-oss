#!/usr/bin/env python3
"""Generate the reviewed Batch 922 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "research/evidence-page451-robert-storey-to-eli-strahinic-review_batch-922_2026-10-26.json"

INDEX = "nara-index-b922"
ARMY = "army-bulk-b922"
TECH = "army-tech-b922"
CODES = "army-codes-b922"
USREPORTS = "usreports-robert-storey-b922"
CAIL = "cail-robert-storey-b922"
SMU = "smu-robert-storey-b922"
NIA = "nia-hans-storhaug-b922"
NPS = "nps-john-stoyka-b922"


PEOPLE = {
    24: ("6d05a8b2-fead-50bf-a2f9-71a472244f3d", "Robert G Storey"),
    25: ("9d98cb3f-f72f-58d9-b62e-7e2668e868d3", "Hans Storhaug"),
    26: ("1154eca1-e910-5060-b0d9-14a36d684008", "Lee Storm"),
    27: ("6a5e9ce8-f1c7-5727-8bb7-f7db5458b21f", "Eileen R Stormberg"),
    28: ("ed72d56b-f275-521a-bc48-ec9a88b3022e", "William H Stormont"),
    29: ("a0c69ffc-9476-5212-aede-5950930c3c49", "Leroy W Storms"),
    30: ("d2d7f85e-cda2-5155-bf64-5b3ce5e178ba", "William W Storms"),
    31: ("255b1730-c44c-5917-99b4-a2e0040dcc88", "Cleveland H Storrs"),
    32: ("5343e021-48ae-5751-9df1-36f7b7f961e4", "Charles D Story"),
    33: ("07b8976a-685d-5b4b-ab92-fd9c6b0c99c1", "Willard E Stott"),
    34: ("18624c6d-6695-5c15-a649-623169ed816e", "Bernard C Stough"),
    35: ("8d6aeb36-d988-5efe-8242-b2504bb103f2", "Charles Stout"),
    36: ("2c154491-3bb2-5e5b-8b28-4966d01e088f", "David B Stout"),
    37: ("f2b9f64b-7639-5471-9a46-2ea1376df006", "Junius J Stout"),
    38: ("70ff768d-d6d7-5d80-b88d-6c90e869aae6", "Robert Stout"),
    39: ("7b5272b6-b369-5bd4-afa7-55c87f51a72e", "Ruth E Stout"),
    40: ("e445044d-5dbf-51bc-ab0c-d29cf96a87f4", "Cecil C Stovall"),
    41: ("19d969f1-a213-5b05-9165-c78a8b6d516e", "Dean M Stover"),
    42: ("9c8ad805-f7ef-524a-9a3c-1d1240188386", "Harris Stover"),
    43: ("8710270f-c604-54ce-b2ee-81931b138886", "Deborah L Stowe"),
    44: ("9447dc24-7a05-52af-b5a2-fdb2f02abb42", "John L Stoyka"),
    45: ("4e31d976-918e-5aa0-b07f-54aed36fbc40", "Lelah M Strader"),
    46: ("49431e62-6925-5e68-862b-bcf66ec4c5e8", "Eli Strahinic"),
}


UNRESOLVED = {
    26: "A Laun Lee Storm naval biography and other uninitialed namesakes did not match the printed name or provide an OSS or Box 751 bridge.",
    27: "Only discovery-only people-finder results appeared; none was retained as identity or employment evidence.",
    28: "Genealogy and military-roster search results concerned other Stormont names and supplied no corroborating identifier.",
    29: "Exact-name, occupation, employer, obituary, institutional, newspaper and archival searches produced no defensible identity bridge.",
    30: "A nineteenth-century directory and modern physician results were wrong-period or wrong-person namesakes and were rejected.",
    31: "Exact-name and variant searches produced no person-specific result with an OSS or Box 751 bridge.",
    32: "A cemetery entry for a Charles D Story who died in 1942 lacked an OSS bridge and was not assigned to the index row.",
    35: "A 1970 CIA document and several wartime biographies concerned uninitialed or differently identified Charles Stout namesakes.",
    36: "Exact-name and variant searches produced no defensible wartime identity or employment evidence.",
    37: "The distinctive exact-name searches returned no defensible identity, employment or institutional result.",
    38: "Several wartime Robert Stout military biographies had different full names or service contexts and no Box 751 bridge.",
    39: "A 1970 Air Force list and directory fragments were postwar or wrong-initial namesakes and were not assigned.",
    41: "Exact-name and variant searches produced no defensible wartime identity or employment evidence.",
    43: "Only discovery-only modern people-finder results appeared; none was retained as evidence.",
    45: "Only discovery-only modern people-finder and relative-name results appeared; none was retained as evidence.",
    46: "Exact-name, transliteration-aware and institutional searches produced no defensible identity or employment result.",
}


ARMY_OCCUPATIONS = {
    33: {
        "code": "316",
        "occupation": "Farm hands, general farms",
        "entry_date": "1941-12-29",
        "code_locator": "PDF physical page 172; historical category 3-16",
    },
    34: {
        "code": "475",
        "occupation": "Machinists",
        "entry_date": "1944-01-27",
        "code_locator": "PDF physical page 173; historical category 4-75",
    },
    42: {
        "code": "992",
        "occupation": "Students",
        "entry_date": "1943-07-08",
        "code_locator": "PDF physical page 304; corrected historical category 9-92",
    },
    44: {
        "code": "032",
        "occupation": "Teachers and instructors, not elsewhere classified",
        "entry_date": "1942-12-01",
        "code_locator": "PDF physical page 171; historical category 0-32",
    },
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Box 751",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 451, rows 24-46; checked against layout-preserving text and a rendered page image",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. Full identifiers remain private. The printed Hans Storhaug note and rank were visually verified.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; four accepted and one rejected Batch 922 protected-identifier candidates",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "No raw row or full protected identifier is retained in public assets. The Cecil C/O Stovall conflict was rejected. Coded occupations identify no employer.",
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
            "locator": "PDF physical pages 171-173 and 304; historical categories 0-32, 3-16, 4-75 and corrected 9-92 visually checked",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "The historical occupation categories identify neither an employer nor a workplace. Bernard Stough's damaged grade is not normalized.",
        },
        {
            "key": USREPORTS,
            "stable_url": "https://www.govinfo.gov/content/pkg/USREPORTS-313/pdf/USREPORTS-313-BackMatter-7.pdf",
            "archival_identifier": "313 U.S. 581; October Term 1940, Decisions Denying Certiorari",
            "title": "Decisions Denying Certiorari, From April 1, 1941, Through June 2, 1941",
            "author_creator": "Supreme Court of the United States",
            "repository_publisher": "U.S. Government Publishing Office",
            "publication_record_date": "1941",
            "locator": "PDF physical page 24, printed page 581; visually checked counsel listing immediately above the May 26, 1941 entries",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "collection_name": "United States Reports, volume 313",
            "rights_notes": "The official court record names Robert Gerald Storey as counsel. It documents active legal practice, not a law-firm employer.",
        },
        {
            "key": CAIL,
            "stable_url": "https://www.cailaw.org/Southwestern-Institute-for-International-and-Comparative-Law/About-Us/storey-award.html",
            "title": "Storey Award",
            "author_creator": "The Center for American and International Law",
            "repository_publisher": "The Center for American and International Law",
            "locator": "Robert Gerald Storey biographical paragraph",
            "access_date": "2026-10-26",
            "source_quality": "B_authoritative_institutional",
            "rights_notes": "The institutional biography identifies Storey's Dallas legal practice and later Nuremberg role. A short excerpt is retained.",
        },
        {
            "key": SMU,
            "stable_url": "https://blog.smu.edu/smumagazine/2025/10/27/dean-storey-journals/",
            "title": "SMU Law Dean Storey's journals chronicle Nuremberg trial",
            "author_creator": "Sarah Bennett",
            "repository_publisher": "Southern Methodist University Magazine",
            "publication_record_date": "2025-10-27",
            "locator": "Paragraph describing Storey's World War II Army Air Corps service and Mediterranean intelligence work",
            "access_date": "2026-10-26",
            "source_quality": "B_authoritative_institutional",
            "rights_notes": "The university account is used for identity and military chronology, not to infer a named OSS assignment or employer.",
        },
        {
            "key": NIA,
            "stable_url": "https://www.nia.no/en/the-saboteurs/",
            "title": "The heroes of Telemark",
            "author_creator": "Norwegian Industrial Workers Museum",
            "repository_publisher": "Norwegian Industrial Workers Museum",
            "locator": "Hans Storhaug biographical section and Gunnerside roster",
            "access_date": "2026-10-26",
            "source_quality": "B_authoritative_institutional",
            "rights_notes": "The museum account dates Storhaug's December 1940 entry into Norwegian Independent Company 1 and gives his sergeant role. No civilian employer is named.",
        },
        {
            "key": NPS,
            "stable_url": "https://home.nps.gov/articles/oss-in-action-the-pacific-and-the-far-east.htm",
            "archival_identifier": "National Park Service article, Ho Chi Minh and the OSS section",
            "title": "OSS in Action: The Pacific and the Far East",
            "author_creator": "National Park Service",
            "repository_publisher": "U.S. National Park Service",
            "locator": "Ho Chi Minh and the OSS section; Cat Team paragraph naming John L. Stoyka",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "rights_notes": "The official history directly names Stoyka as an OSS sergeant and radio operator. It does not identify his civilian employer.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": "norwegian-independent-company-1-b922",
            "organization_id": "0ad15737-f33c-5d8c-b93d-c9a96833563e",
            "canonical_name": "Norwegian Independent Company 1",
            "historical_name": "Norwegian Independent Company 1",
            "aliases": ["Kompani Linge", "Norwegian Independent Company No. 1"],
            "organization_type": "Norwegian special operations unit",
            "sector": "military",
            "country": "United Kingdom",
            "active_dates": "1941-1945",
            "normalization_notes": "Existing canonical organization reused. The museum dates Storhaug's joining to December 1940; the unit's formal organization chronology remains separately documented.",
        }
    ]


def affiliations() -> list[dict[str, object]]:
    result: list[dict[str, object]] = [
        {
            "key": "robert-storey-dallas-law-b922",
            "person_id": PEOPLE[24][0],
            "organization_name_as_found": "private law practice in Dallas",
            "role_title": "attorney and counsel",
            "occupation": "lawyer",
            "relationship_type": "self_employment",
            "date_precision": "An official court record names him as counsel on May 26, 1941; Army service began in 1941, but the exact transition date is not stated.",
            "city": "Dallas",
            "state_or_region": "Texas",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": True,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "high_confidence",
            "claim_confidence": "medium",
            "source_quality": "A_direct_official",
            "publication_status": "publish_qualified",
            "research_notes": "This is the last documented civilian practice before his 1941-1945 Army service. No firm name or explicit OSS recruitment transition is claimed.",
        },
        {
            "key": "hans-storhaug-nic1-b922",
            "person_id": PEOPLE[25][0],
            "organization_key": "norwegian-independent-company-1-b922",
            "organization_name_as_found": "Norwegian Independent Company 1",
            "role_title": "sergeant",
            "relationship_type": "military_assignment",
            "start_date": "1940-12",
            "date_precision": "The museum states that Storhaug left for Scotland and joined the unit in December 1940; exact day and end date are not supplied.",
            "country": "United Kingdom",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "published",
            "research_notes": "Allied military assignment, not a civilian employer. The public source does not establish the route by which his file entered the OSS index.",
        },
    ]
    for row, data in ARMY_OCCUPATIONS.items():
        relationship = "student" if row == 42 else "employment"
        result.append(
            {
                "key": f"{slug(PEOPLE[row][1])}-occupation-b922",
                "person_id": PEOPLE[row][0],
                "occupation": data["occupation"],
                "relationship_type": relationship,
                "end_date": data["entry_date"],
                "date_precision": f"Historical civilian-occupation code {data['code']} was recorded at Army entry on {data['entry_date']}; no employer, school, workplace or OSS-transfer date is named.",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "A_direct_official",
                "publication_status": "publish_qualified",
                "research_notes": "The historical category is not converted into a named employer, school, farm, shop, institution, workplace or exact job title.",
            }
        )
    return result


def claims() -> list[dict[str, object]]:
    result: list[dict[str, object]] = [
        {
            "key": "identity-robert-storey-b922",
            "person_id": PEOPLE[24][0],
            "claim_type": "identity",
            "claim_text": "The indexed Robert G Storey is a high-confidence match to Dallas lawyer and Army Air Corps Colonel Robert Gerald Storey.",
            "evidence_excerpt": "Robert Gerald Storey (1893-1981) practiced law in Dallas",
            "evidence_paraphrase": "Institutional sources document the exact full name, Dallas legal career, World War II Army colonel service and Mediterranean intelligence work.",
            "identity_match_assessment": "High confidence from the exact first name, middle initial, surname, nonpublic Army-format officer identifier and institutional documentation of Robert Gerald Storey Sr.'s World War II Army colonel service. The suffix-free index row and Army context distinguish the senior lawyer from his Navy-veteran son.",
            "temporal_assessment": "The court record documents active legal practice in May 1941; SMU documents World War II Army service beginning in 1941. Neither source supplies an OSS transfer date.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "The protected index identifier is not exposed. The identity finding does not turn Mediterranean intelligence work into a specifically named OSS assignment.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 451 row 24; Box 751; protected identifier withheld"},
                {"source_key": CAIL, "locator_override": "Robert Gerald Storey biographical paragraph"},
                {"source_key": SMU, "locator_override": "World War II service paragraph"},
            ],
        },
        {
            "key": "last-civilian-robert-storey-b922",
            "person_id": PEOPLE[24][0],
            "affiliation_key": "robert-storey-dallas-law-b922",
            "claim_type": "last_civilian_pre_service",
            "claim_text": "Robert Gerald Storey's last documented civilian practice before his 1941 Army service was law practice in Dallas; the reviewed sources do not name his 1941 firm.",
            "evidence_excerpt": "Mr. Robert Gerald Storey for respondent.",
            "evidence_paraphrase": "The U.S. Reports page identifies Storey as counsel in a May 1941 matter, while institutional sources document his Dallas practice and Army service beginning in 1941.",
            "identity_match_assessment": "High-confidence identity based on the exact full name and documented World War II Army colonel chronology.",
            "temporal_assessment": "Strongly date-bounded: active counsel on May 26, 1941, and Army service began in 1941. The exact transition date and firm are not stated.",
            "source_quality": "A_direct_official",
            "claim_confidence": "medium",
            "publication_status": "publish_qualified",
            "match_notes": "The finding is presented as private legal practice, not a named employer and not an explicit immediate-pre-OSS transition.",
            "sources": [
                {"source_key": USREPORTS, "locator_override": "PDF physical page 24, printed page 581; visually checked counsel listing"},
                {"source_key": CAIL, "locator_override": "Robert Gerald Storey biographical paragraph"},
                {"source_key": SMU, "support_type": "context_only", "locator_override": "World War II service paragraph"},
            ],
        },
        {
            "key": "identity-hans-storhaug-b922",
            "person_id": PEOPLE[25][0],
            "claim_type": "identity",
            "claim_text": "The indexed Hans Storhaug is a high-confidence match to the Norwegian sergeant in the Gunnerside sabotage group.",
            "evidence_excerpt": "sergeant Hans Storhaug (27)",
            "evidence_paraphrase": "The museum identifies the exact distinctive name, sergeant rank, Norwegian origin and wartime special-operations chronology.",
            "identity_match_assessment": "High confidence from the distinctive exact name, the index's SGT rank and Norwegian note, and the museum's matching sergeant rank, nationality and wartime chronology.",
            "temporal_assessment": "The museum dates his Norwegian Independent Company 1 service from December 1940; the OSS-index relationship is not explained online.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "This identity does not establish a civilian employer or imply that the British-led unit was itself an OSS organization.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 451 row 25; SGT; Norwegian note; Box 751"},
                {"source_key": NIA, "locator_override": "Hans Storhaug biographical section and Gunnerside roster"},
            ],
        },
        {
            "key": "prewar-hans-storhaug-nic1-b922",
            "person_id": PEOPLE[25][0],
            "affiliation_key": "hans-storhaug-nic1-b922",
            "claim_type": "other_pre_oss_affiliation",
            "claim_text": "In December 1940 Hans Storhaug joined Norwegian Independent Company 1 in Scotland and served as a sergeant.",
            "evidence_excerpt": "In December 1940 he leaves Ålesund for Scotland, where he joins Norwegian Independent Company 1.",
            "evidence_paraphrase": "The museum explicitly dates the Allied military assignment and separately identifies Storhaug as a Gunnerside sergeant.",
            "identity_match_assessment": "High-confidence match from the distinctive name, nationality note, sergeant rank and matching operational chronology.",
            "temporal_assessment": "Documented before the OSS existed, but not shown to be the immediate predecessor to any OSS assignment.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "Military assignment, not civilian employment. No route into the OSS index is inferred.",
            "sources": [{"source_key": NIA, "locator_override": "Hans Storhaug biographical section"}],
        },
    ]

    for row, data in ARMY_OCCUPATIONS.items():
        name = PEOPLE[row][1]
        identity_sources = [
            {"source_key": INDEX, "locator_override": f"PDF page 451 row {row}; Box 751; protected identifier withheld"},
            {"source_key": ARMY, "locator_override": "Accepted reviewed identity bridge; protected identifier withheld"},
        ]
        identity_text = f"The indexed {name} row is a high-confidence match to the reviewed official Army record."
        identity_paraphrase = "A nonshared protected identifier and compatible name connect the visually verified index row to the official Army record."
        identity_assessment = "High confidence from exact full-name agreement and a nonshared protected-identifier bridge."
        if row == 42:
            identity_assessment = "High confidence from given-name and surname agreement plus a nonshared protected identifier; the Army row adds middle initial A without contradicting the index."
        if row == 44:
            identity_text = "The indexed John L Stoyka is a high-confidence match to the official Army record and the OSS Cat Team radio operator documented by the National Park Service."
            identity_paraphrase = "The exact name and protected Army identifier are reinforced by an official history naming Sergeant John L. Stoyka in OSS Special Operations."
            identity_assessment = "High confidence from exact full-name agreement, a nonshared protected identifier and an independent official OSS history identifying the same sergeant."
            identity_sources.append({"source_key": NPS, "locator_override": "Ho Chi Minh and the OSS; Cat Team paragraph"})
        result.append(
            {
                "key": f"identity-{slug(name)}-b922",
                "person_id": PEOPLE[row][0],
                "claim_type": "identity",
                "claim_text": identity_text,
                "evidence_paraphrase": identity_paraphrase,
                "identity_match_assessment": identity_assessment,
                "temporal_assessment": f"The Army entry is dated {data['entry_date']}; it does not establish an OSS transfer date.",
                "source_quality": "A_direct_official",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "No protected identifier is exposed, and the historical occupation is kept separate from employer claims.",
                "sources": identity_sources,
            }
        )
        article = "an" if data["occupation"].lower().startswith(tuple("aeiou")) else "a"
        if row == 42:
            claim_text = f"At Army entry on {data['entry_date']}, Harris Stover was recorded in the historical occupation group Students; no school or employer is identified."
        else:
            claim_text = f"At Army entry on {data['entry_date']}, {name} was recorded in {article} historical occupation category, {data['occupation']}; no employer is identified."
        result.append(
            {
                "key": f"occupation-{slug(name)}-b922",
                "person_id": PEOPLE[row][0],
                "affiliation_key": f"{slug(name)}-occupation-b922",
                "claim_type": "occupation",
                "claim_text": claim_text,
                "evidence_excerpt": data["occupation"],
                "evidence_paraphrase": f"The accepted Army record carries civilian-occupation code {data['code']}, decoded from NARA's official code list.",
                "identity_match_assessment": "The category belongs only to the reviewed protected-identifier match; the identifier itself is not public.",
                "temporal_assessment": "Strongly date-bounded to Army entry; it does not establish the immediate pre-OSS affiliation or a named employer.",
                "source_quality": "A_direct_official",
                "claim_confidence": "medium",
                "publication_status": "publish_qualified",
                "match_notes": "The historical category is a qualified lead, not a named employer, school, farm, shop, institution, workplace or exact title.",
                "sources": [
                    {"source_key": ARMY, "locator_override": f"Accepted reviewed identity record; civilian occupation code {data['code']}; protected identifier withheld"},
                    {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46; Army-entry-date and civilian-occupation fields"},
                    {"source_key": CODES, "locator_override": data["code_locator"], "excerpt_override": data["occupation"]},
                ],
            }
        )
    return result


def unresolved_update(row: int) -> dict[str, object]:
    person_id, name = PEOPLE[row]
    return {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, Box 751 and archive location, but staged NARA/index, CIA Reading Room, exact-name OSS, occupation, employer, obituary, institutional, newspaper and archival searches found no defensible identity bridge. {UNRESOLVED[row]}",
        "personnel_category": "unknown_or_indeterminate",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": "Review the indexed Box 751 personnel file for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "critical",
    }


def person_updates() -> list[dict[str, object]]:
    updates = [unresolved_update(row) for row in UNRESOLVED]
    updates.extend(
        [
            {
                "person_id": PEOPLE[24][0],
                "identity_status": "high_confidence",
                "identity_evidence": "The exact name, nonpublic Army-format officer identifier and institutional histories connect the index row to Robert Gerald Storey Sr., a Dallas lawyer and World War II Army Air Corps colonel who conducted Mediterranean intelligence work.",
                "name_variants": ["Robert Gerald Storey", "Robert G. Storey Sr."],
                "personnel_category": "commissioned_army_officer",
                "commissioned_officer": True,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "documented_prewar_employer_found",
                "next_action": "Review Box 751 for the OSS recruitment or transfer chronology and the 1941 law-practice firm. The current last-civilian finding is private Dallas legal practice, not a named employer.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[25][0],
                "identity_status": "high_confidence",
                "identity_evidence": "The exact distinctive name, index rank SGT and Norwegian note match the museum's Hans Storhaug, a Norwegian sergeant who joined Norwegian Independent Company 1 in Scotland in December 1940 and served in Gunnerside.",
                "name_variants": ["Hans 'Kyllingen' Storhaug"],
                "personnel_category": "foreign_or_allied_military_personnel",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": True,
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Review Box 751 for the basis of the OSS index linkage and for any civilian occupation before December 1940. The documented Norwegian unit is an Allied military assignment, not a civilian employer.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[40][0],
                "identity_status": "conflicting",
                "identity_evidence": "The protected identifier selects an official Army row named Cecil O Stovall, while the visually verified index prints Cecil C Stovall. The middle-initial conflict is unresolved, so no Army field is transferred.",
                "personnel_category": "unknown_or_indeterminate",
                "manual_review_required": True,
                "research_status": "conflicting_sources",
                "next_action": "Review Box 751 for the full name and compare it with the official Army row before accepting or rejecting the protected-identifier match. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
        ]
    )
    for row in ARMY_OCCUPATIONS:
        name = PEOPLE[row][1]
        evidence = "An exact full name and nonshared protected identifier connect the index row to the official Army record."
        if row == 42:
            evidence = "Given-name and surname agreement plus a nonshared protected identifier connect the index row to the official Army record; the record adds middle initial A without contradicting the index."
        if row == 44:
            evidence += " An independent National Park Service history names Sergeant John L. Stoyka as an OSS Cat Team radio operator."
        updates.append(
            {
                "person_id": PEOPLE[row][0],
                "identity_status": "high_confidence",
                "identity_evidence": evidence,
                "personnel_category": "enlisted_army_personnel",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "occupation_only_found",
                "next_action": f"Review Box 751 to identify the immediate pre-OSS affiliation and last civilian employer; do not convert the Army category '{ARMY_OCCUPATIONS[row]['occupation']}' into a named employer or institution.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            }
        )
    return updates


def research_attempts() -> list[dict[str, object]]:
    attempts: list[dict[str, object]] = []
    strong_rows = {24, 25, 33, 34, 42, 44}
    rejected_rows = {26, 30, 32, 35, 38, 39, 40}
    for row, (person_id, name) in PEOPLE.items():
        if row == 24:
            outcome = "source_reviewed"
            detail = "A contemporaneous U.S. Reports page, CAIL biography and SMU history established high-confidence identity and strongly date-bounded Dallas legal practice before 1941 Army service."
            sources_reviewed = 9
            rejected = 4
        elif row == 25:
            outcome = "source_reviewed"
            detail = "The Norwegian Industrial Workers Museum established high-confidence identity and a December 1940 Allied military assignment, but no civilian employer."
            sources_reviewed = 7
            rejected = 3
        elif row in ARMY_OCCUPATIONS:
            outcome = "source_reviewed"
            detail = f"An accepted protected-identifier Army bridge established identity and a dated historical category, {ARMY_OCCUPATIONS[row]['occupation']}, but no named employer or institution."
            if row == 44:
                detail += " The National Park Service independently documented Stoyka's OSS service."
            sources_reviewed = 8 if row == 44 else 6
            rejected = 3
        elif row == 40:
            outcome = "candidate_rejected"
            detail = "The protected identifier selects Cecil O Stovall while the index prints Cecil C Stovall. The conflict prevents transfer of all Army fields."
            sources_reviewed = 6
            rejected = 5
        elif row in rejected_rows:
            outcome = "candidate_rejected"
            detail = UNRESOLVED[row]
            sources_reviewed = 5
            rejected = 5
        else:
            outcome = "no_result"
            detail = UNRESOLVED[row]
            sources_reviewed = 5
            rejected = 3
        attempts.append(
            {
                "key": f"page451-row{row}-{slug(name)}-b922",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA/index and public Archives context; CIA Reading Room site-restricted exact-name check; OSS and rank variants; employer and occupation; obituary, institutional, newspaper, directory and archival searches; Box 751; protected-identifier Army crosswalk where defensible",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_922",
                "started_at": "2026-10-26T09:22:00Z",
                "completed_at": "2026-10-26T09:48:00Z",
                "outcome": outcome,
                "sources_reviewed": sources_reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, discovery-only genealogy or people-finder results, wrong initials, postwar-only leads and sources without an OSS or Box-file bridge were not assigned." if outcome in strong_rows or outcome == "source_reviewed" else detail,
                "research_notes": f"{detail} The CIA adapter failed closed on its robots check; separate site-restricted public Reading Room searches returned no exact-name result, except an unrelated 1970 Charles Stout namesake that was rejected. The Library of Congress adapter failed before returning results, so institutional, obituary, newspaper, directory and archival web searches supplied the alternative protocol step. No search snippet was used as final evidence, no access control was bypassed, and no authenticated NARA API call was made.",
                "next_action": "Review the indexed Box 751 personnel file for corroborating identifiers and the immediate pre-OSS affiliation or last civilian employer.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b922-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-922-v1",
        "reviewer": "Before OSS Batch 922 evidence review",
        "sources": sources(),
        "organizations": organizations(),
        "affiliations": affiliations(),
        "claims": claims(),
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }
    OUTPUT.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
