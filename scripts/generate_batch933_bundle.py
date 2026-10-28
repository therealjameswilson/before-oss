#!/usr/bin/env python3
"""Generate the reviewed Batch 933 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / (
    "research/evidence-page457-fred-g-swafford-to-victor-h-swearingen-"
    "review_batch-933_2026-10-27.json"
)

INDEX = "nara-index-b933"
ARMY_SOURCE = "army-bulk-b933"
TECH = "army-tech-b933"
CODES = "army-codes-b933"
NPS = "nps-oss-europe-b933"
SINGLAUB = "singlaub-interview-b933"
MEMORIAL = "awmo-paul-swank-b933"

PEOPLE = {
    1: ("c64a56f3-6fc6-52a5-968c-29f3cf050365", "Fred G Swafford"),
    2: ("f8868ded-ef9e-5573-a291-990bd6d38ff5", "John E Swain"),
    3: ("ac6f5af1-3a00-56d4-858e-cff941235d2a", "Robert A Swain"),
    4: ("62a7c1a6-98d2-5b5d-be9d-4fa3515c8441", "George L Swan"),
    5: ("7a42a7ad-813b-5603-bf41-4a983d5bb0e4", "George E Swan"),
    6: ("69a6f0c3-d2cc-5083-8699-c20a004aca7c", "Fletcher B Swank"),
    7: ("0bf5a230-67ef-5df0-ba1b-8cd327338508", "Lawrence E Swank"),
    8: ("427ff312-d569-53c2-a7d7-2eb8dbf41b37", "Paul A Swank"),
    9: ("5d27bd4f-fb95-5364-88f0-4aef6bdc2422", "William A Swank"),
    10: ("044b7354-3fee-595a-9bd7-708c4870e94e", "David E Swanson"),
    11: ("d3ba048a-e197-5f90-8f14-f44837eba600", "Helen C Swanson"),
    12: ("bfea9036-7f70-5511-b915-9a9a5bd5c136", "John C Swanson"),
    13: ("787c4af9-a4c3-5820-831f-4f79cb549a3e", "Joseph E Swanson"),
    14: ("a81f7f88-2c1a-5303-af3c-dee96deebc96", "Raymond W Swanson"),
    15: ("40bfd075-e0ce-54f0-821f-c41d599f57f8", "Anthony I Swarowsky"),
    16: ("cffcba38-a8cf-5fe1-ae21-9a88f06ee1fd", "Harvey R Swarts"),
    17: ("ad45604e-a553-582c-b770-f8b1b5cc9bfc", "Anthony P Swartz"),
    18: ("5c4f6716-7192-5fcd-9a61-a39859e05756", "Jacobs R Swartz"),
    19: ("d39ac391-f0e5-516b-a120-4bffed927329", "Robert C Swartz"),
    20: ("1c765e0e-e385-5464-aa5c-c36787644da3", "Thomas J Swartz"),
    21: ("96fd44f3-f0c1-5f97-863b-248fa3f75a2f", "William E Swartzenburg"),
    22: ("a58739d6-74a7-5c8f-a055-267bf3c8c90c", "John A Swayze"),
    23: ("2ce81670-f2ec-5178-bf58-36cfa5c16e2a", "Victor H Swearingen"),
}

FRED_S_WATSON_JR = "eb26f905-3ac1-562f-b6df-d3b617b95212"
DUPLICATE_GROUP = "p457-harvey-r-swarts-fred-s-watson-jr-b933"

ARMY = {
    9: {
        "entry": "1944-08-16",
        "code": "992",
        "occupation": "Students",
        "relationship": "student",
        "locator": "PDF physical page 304; corrected historical category 9-92",
        "grade": "PVT",
    },
    20: {
        "entry": "1942-11-02",
        "code": "788",
        "occupation": "Warehousing, storekeeping, handling, loading, unloading, and related occupations, n.e.c.",
        "relationship": "employment",
        "locator": "PDF physical page 175; historical category 7-88",
        "grade": "uninterpreted value PV0",
    },
    21: {
        "entry": "1942-11-18",
        "code": "992",
        "occupation": "Students",
        "relationship": "student",
        "locator": "PDF physical page 304; corrected historical category 9-92",
        "grade": "PVT",
    },
    23: {
        "entry": "1942-12-28",
        "code": "736",
        "occupation": "Chauffeurs and drivers, bus, taxi, truck, tractor",
        "relationship": "employment",
        "locator": "PDF physical page 174; historical category 7-36",
        "grade": "PVT",
    },
}

UNRESOLVED = {
    1: "Exact-name Army, obituary and archival leads supplied no OSS, protected-identifier or Box 760 bridge.",
    2: "Exact-name and variant searches did not distinguish the indexed John E Swain from namesakes.",
    3: "The short protected identifier and common name produced no defensible official-record identity bridge.",
    4: "Exact-name military, employment and obituary searches produced no two-identifier match.",
    5: "Exact-name military, employment and obituary searches produced no two-identifier match.",
    6: "A former judge and congressman namesake was rejected because no OSS or Box 760 evidence connects him to this row.",
    10: "Exact-name and occupation searches did not identify the indexed David E Swanson among common-name results.",
    11: "Exact-name, institutional and newspaper searches supplied no OSS or Box 760 identity bridge for Helen C Swanson.",
    12: "Exact-name and military searches supplied no two-identifier match for John C Swanson.",
    13: "Exact-name and military searches supplied no two-identifier match for Joseph E Swanson.",
    14: "The short protected identifier and common name did not yield a defensible official-record match.",
    17: "Exact-name and spelling-variant searches did not establish which Anthony P Swartz is indexed.",
    18: "Exact-name and variant searches produced no corroborated identity bridge for the unusual indexed form Jacobs R Swartz.",
    19: "Exact-name military, obituary and archival searches did not distinguish Robert C Swartz from namesakes.",
    22: "Exact-name and military searches did not provide two corroborating identifiers for John A Swayze.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Box 760",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 457, rows 1-23; checked against layout-preserving text and the rendered page image",
            "access_date": "2026-10-27",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. Full identifiers remain private. A shared-identifier conflict is represented by an opaque duplicate-group label.",
        },
        {
            "key": ARMY_SOURCE,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; five reviewed Batch 933 identity candidates",
            "access_date": "2026-10-27",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "Four exact-name, nonshared protected-identifier matches are accepted. One materially different-name record is rejected. No raw row or full identifier is public.",
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
            "access_date": "2026-10-27",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Used to interpret selected fields only. The damaged grade value PV0 is preserved as uninterpreted.",
        },
        {
            "key": CODES,
            "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1CL_SD.pdf",
            "archival_identifier": "National Archives Identifier 1263923; Code No. 30",
            "title": "NARA Compiled Code Lists for the Electronic Army Serial Number Merged File",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives at College Park - Electronic Records",
            "publication_record_date": "2011-01-12; modified 2011-03-17",
            "locator": "PDF physical pages 174, 175 and 304; categories 736, 788 and corrected 992 visually checked",
            "access_date": "2026-10-27",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical categories identify neither a named employer nor workplace. Student status is not classified as employment.",
        },
        {
            "key": NPS,
            "stable_url": "https://www.nps.gov/articles/oss-in-action-the-mediterranean-and-european-theaters.htm",
            "archival_identifier": "National Park Service OSS history article",
            "title": "OSS in Action: The Mediterranean and European Theaters",
            "author_creator": "National Park Service",
            "repository_publisher": "United States National Park Service",
            "publication_record_date": "2017-08-07",
            "locator": "Sections discussing Lawrence E. Swank and Paul A. Swank; page text reviewed",
            "access_date": "2026-10-27",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Office of Strategic Services histories",
            "rights_notes": "The official historical article distinguishes the two Swanks and documents their ranks, training and OSS missions. It is not a personnel file.",
        },
        {
            "key": SINGLAUB,
            "stable_url": "https://www.defensemedianetwork.com/stories/interview-with-maj-gen-john-k-singlaub-u-s-army-ret/2/",
            "archival_identifier": "Defense Media Network oral-history interview, page 2",
            "title": "Interview with Maj. Gen. John K. Singlaub, (U.S. Army, Ret.)",
            "author_creator": "Dwight Jon Zimmerman",
            "repository_publisher": "Defense Media Network",
            "publication_record_date": "2012-07-20",
            "locator": "Page 2, discussion of Lawrence Swank's West Point, engineer and OSS chronology",
            "access_date": "2026-10-27",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Defense Media Network interviews",
            "rights_notes": "Singlaub's interview corroborates the West Point class, engineer branch, demolitions background and direct OSS recruitment sequence.",
        },
        {
            "key": MEMORIAL,
            "stable_url": "https://www.uswarmemorials.org/html/people_details.php?PeopleID=2746",
            "archival_identifier": "American War Memorials Overseas PeopleID 2746",
            "title": "Swank Paul A.",
            "author_creator": "American War Memorials Overseas, Inc.",
            "repository_publisher": "American War Memorials Overseas, Inc.",
            "publication_record_date": None,
            "locator": "Biographical comments and military-service fields; page reviewed",
            "access_date": "2026-10-27",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "American War Memorials Overseas person profiles",
            "rights_notes": "The profile's protected officer number agrees with the private index value but is omitted from evidence, exports and public text. The chronology is corroborated by the NPS mission account.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": "usma-existing-b933",
            "organization_id": "a6458663-2447-50ce-aa34-4a72ffa79348",
            "canonical_name": "United States Military Academy",
            "historical_name": "United States Military Academy at West Point",
            "aliases": ["West Point", "Military Academy"],
            "organization_type": "military academy",
            "sector": "academia_and_research",
            "city": "West Point",
            "state_or_region": "New York",
            "country": "United States",
            "active_dates": "1802-present",
            "normalization_notes": "Existing canonical organization reused. Cadet or student status is modeled separately and is not employment.",
        },
        {
            "key": "usace-existing-b933",
            "organization_id": "f2367526-082d-5cad-8156-c405c426f2e1",
            "canonical_name": "United States Army Corps of Engineers",
            "historical_name": "Army Corps of Engineers",
            "aliases": ["Engineer Corps", "U.S. Army Corps of Engineers"],
            "organization_type": "military branch",
            "sector": "military",
            "country": "United States",
            "active_dates": "Active during World War II",
            "normalization_notes": "Existing canonical organization reused. Corps of Engineers service is a military assignment, not civilian employment.",
        },
        {
            "key": "us-army-existing-b933",
            "organization_id": "28a26f92-78af-5a1a-9c09-a843eb5975b4",
            "canonical_name": "United States Army",
            "historical_name": "Army of the United States",
            "aliases": ["U.S. Army"],
            "organization_type": "military service",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "Existing canonical organization reused. Specific units remain in affiliation wording; Army service is not civilian employment.",
        },
    ]


def army_affiliations() -> list[dict[str, object]]:
    result: list[dict[str, object]] = []
    for row, data in ARMY.items():
        person_id, name = PEOPLE[row]
        result.append(
            {
                "key": f"{slug(name)}-occupation-b933",
                "person_id": person_id,
                "occupation": data["occupation"],
                "relationship_type": data["relationship"],
                "end_date": data["entry"],
                "date_precision": "Army entry date; beginning and duration are not stated",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "A_direct_official",
                "publication_status": "publish_qualified",
                "research_notes": "The official historical category is tied to Army entry. It identifies no employer or workplace and is not promoted to an immediate pre-OSS affiliation.",
            }
        )
    return result


def named_affiliations() -> list[dict[str, object]]:
    lawrence = PEOPLE[7][0]
    paul = PEOPLE[8][0]
    return [
        {
            "key": "lawrence-e-swank-usma-b933",
            "person_id": lawrence,
            "organization_key": "usma-existing-b933",
            "organization_name_as_found": "West Point",
            "role_title": "Cadet; 1943 graduate",
            "occupation": "student",
            "relationship_type": "student",
            "end_date": "1943",
            "date_precision": "Graduation year stated by both reviewed sources; month and entry year not used",
            "city": "West Point",
            "state_or_region": "New York",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "published",
            "research_notes": "Student status, not employment. The sources identify him as a 1943 graduate before the engineer and OSS sequence.",
        },
        {
            "key": "lawrence-e-swank-usace-b933",
            "person_id": lawrence,
            "organization_key": "usace-existing-b933",
            "organization_name_as_found": "engineer branch",
            "role_title": "Army engineer and demolitions officer",
            "occupation": "commissioned Army officer",
            "relationship_type": "military_assignment",
            "start_date": "1943",
            "date_precision": "Post-graduation 1943 sequence; exact transfer date not stated",
            "country": "United States",
            "immediate_pre_oss": True,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "explicit_immediate",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "published",
            "research_notes": "Singlaub describes engineer/demolitions service followed by recruitment as an OSS instructor; this is a military pathway, not a civilian employer.",
        },
        {
            "key": "paul-a-swank-us-army-b933",
            "person_id": paul,
            "organization_key": "us-army-existing-b933",
            "organization_name_as_found": "U.S. Army at Camp Claiborne",
            "role_title": "First Lieutenant; Army training at Camp Claiborne",
            "occupation": "commissioned Army officer",
            "relationship_type": "military_assignment",
            "start_date": "1942-08-18",
            "end_date": "1943-08-18",
            "date_precision": "Entry and end-of-Camp-Claiborne dates stated in the memorial profile",
            "city": "Camp Claiborne",
            "state_or_region": "Louisiana",
            "country": "United States",
            "immediate_pre_oss": True,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "explicit_immediate",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "published",
            "research_notes": "The profile says he volunteered for OSS after Camp Claiborne; NPS independently documents the same first lieutenant and OSS mission. No civilian employer is inferred.",
        },
    ]


def affiliations() -> list[dict[str, object]]:
    return [*army_affiliations(), *named_affiliations()]


def army_claims() -> list[dict[str, object]]:
    result: list[dict[str, object]] = []
    for row, data in ARMY.items():
        person_id, name = PEOPLE[row]
        result.extend(
            [
                {
                    "key": f"identity-{slug(name)}-row{row}-b933",
                    "person_id": person_id,
                    "claim_type": "identity",
                    "claim_text": f"The indexed {name} row is a high-confidence match to an official Army record dated {data['entry']}.",
                    "evidence_paraphrase": "The reviewed Army row agrees through the exact full name and a nonshared protected identifier.",
                    "identity_match_assessment": "High confidence from an exact full name and a nonshared protected identifier.",
                    "temporal_assessment": f"The Army record documents entry on {data['entry']}; it does not establish the OSS transfer date.",
                    "source_quality": "A_direct_official",
                    "claim_confidence": "high",
                    "publication_status": "published",
                    "match_notes": f"The protected identifier is withheld. The grade field is {data['grade']}; no employer is inferred.",
                    "sources": [
                        {"source_key": INDEX, "locator_override": f"PDF page 457 row {row}; Box 760"},
                        {"source_key": ARMY_SOURCE, "locator_override": f"Accepted reviewed identity record; Army entry {data['entry']}; protected identifier withheld"},
                        {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46; field definitions"},
                    ],
                },
                {
                    "key": f"occupation-{slug(name)}-row{row}-b933",
                    "person_id": person_id,
                    "affiliation_key": f"{slug(name)}-occupation-b933",
                    "claim_type": "occupation",
                    "claim_text": f"At Army entry on {data['entry']}, {name} was recorded in the historical category {data['occupation']}; no employer or workplace is identified.",
                    "evidence_excerpt": data["occupation"],
                    "evidence_paraphrase": f"The accepted Army record carries civilian-occupation code {data['code']}, decoded from NARA's official code list.",
                    "identity_match_assessment": "The category is assigned only to the accepted protected-identifier match; the identifier itself is not public.",
                    "temporal_assessment": "Strongly date-bounded to Army entry, but not proven to be the immediate pre-OSS affiliation.",
                    "source_quality": "A_direct_official",
                    "claim_confidence": "medium",
                    "publication_status": "publish_qualified",
                    "match_notes": "Historical language is preserved and is not converted into a company, workplace or more specific modern job title.",
                    "sources": [
                        {"source_key": ARMY_SOURCE, "locator_override": f"Army entry {data['entry']}; civilian-occupation code {data['code']}; protected identifier withheld"},
                        {"source_key": CODES, "locator_override": data["locator"]},
                    ],
                },
            ]
        )
    return result


def named_claims() -> list[dict[str, object]]:
    lawrence = PEOPLE[7][0]
    paul = PEOPLE[8][0]
    return [
        {
            "key": "identity-lawrence-e-swank-b933",
            "person_id": lawrence,
            "claim_type": "identity",
            "claim_text": "The indexed Lawrence E Swank is a high-confidence match to Lawrence E. 'Larry' Swank, a 1943 West Point graduate, Army engineer and OSS Jedburgh officer.",
            "evidence_paraphrase": "The NPS and Singlaub interview independently align the exact name, West Point class, engineer background, OSS training role and wartime mission.",
            "identity_match_assessment": "High confidence from a distinctive exact full name and a mutually consistent, highly specific career sequence in two reputable sources.",
            "temporal_assessment": "The sources document the 1943 academy-to-engineer-to-OSS sequence but do not state the exact OSS transfer date.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "The NPS article distinguishes Lawrence from Paul A. Swank. Box 760 review remains necessary for the personnel-file chronology and any civilian employer.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 457 row 7; Box 760"},
                {"source_key": NPS, "locator_override": "Lawrence E. Swank discussion"},
                {"source_key": SINGLAUB, "locator_override": "Page 2, Lawrence Swank discussion"},
            ],
        },
        {
            "key": "other-lawrence-e-swank-usma-b933",
            "person_id": lawrence,
            "affiliation_key": "lawrence-e-swank-usma-b933",
            "claim_type": "other_pre_oss_affiliation",
            "claim_text": "Lawrence E. Swank graduated from the United States Military Academy at West Point in 1943.",
            "evidence_excerpt": "a 1943 graduate of West Point",
            "evidence_paraphrase": "Both reviewed sources identify Swank as a 1943 West Point graduate.",
            "identity_match_assessment": "High confidence from the distinctive exact-name and career-sequence identity bridge.",
            "temporal_assessment": "Documented pre-OSS student affiliation; not employment.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "The academy is not labeled an employer.",
            "sources": [
                {"source_key": NPS, "locator_override": "Lawrence E. Swank discussion"},
                {"source_key": SINGLAUB, "locator_override": "Page 2, Lawrence Swank discussion"},
            ],
        },
        {
            "key": "immediate-lawrence-e-swank-usace-b933",
            "person_id": lawrence,
            "affiliation_key": "lawrence-e-swank-usace-b933",
            "claim_type": "immediate_pre_oss_affiliation",
            "claim_text": "Lawrence E. Swank entered the Army engineer branch after West Point and was recruited from his engineer and demolitions work into an OSS instructor role.",
            "evidence_excerpt": "He was in the engineers and went through demolitions training",
            "evidence_paraphrase": "Singlaub describes Swank's engineer branch and demolitions background immediately before OSS recruitment; NPS corroborates his OSS demolitions-instructor role.",
            "identity_match_assessment": "High confidence from the distinctive exact name and matching West Point, engineering, demolitions and OSS chronology.",
            "temporal_assessment": "Explicit immediate military pathway into OSS; the precise transfer date is not stated.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "The Corps of Engineers is a military assignment, not a civilian employer.",
            "sources": [
                {"source_key": SINGLAUB, "locator_override": "Page 2, Lawrence Swank discussion"},
                {"source_key": NPS, "locator_override": "Lawrence E. Swank discussion"},
            ],
        },
        {
            "key": "identity-paul-a-swank-b933",
            "person_id": paul,
            "claim_type": "identity",
            "claim_text": "The indexed Paul A Swank is a high-confidence match to First Lieutenant Paul A. Swank of Houston, an OSS Operational Group officer killed in France in August 1944.",
            "evidence_paraphrase": "NPS supplies the exact name, rank, hometown, OSS unit and mission; the memorial profile independently aligns the full name, chronology and private protected identifier.",
            "identity_match_assessment": "High confidence from multiple specific identifiers in two independent sources, including a protected value withheld from public evidence.",
            "temporal_assessment": "The sources document Army entry in 1942, OSS volunteering after Camp Claiborne in 1943 and the August 1944 mission.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "The NPS article explicitly says Paul was not related to Lawrence Swank. The protected officer number is not reproduced.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 457 row 8; Box 760"},
                {"source_key": NPS, "locator_override": "Paul A. Swank discussion"},
                {"source_key": MEMORIAL, "locator_override": "Military-service fields and biographical comments; protected identifier omitted"},
            ],
        },
        {
            "key": "immediate-paul-a-swank-us-army-b933",
            "person_id": paul,
            "affiliation_key": "paul-a-swank-us-army-b933",
            "claim_type": "immediate_pre_oss_affiliation",
            "claim_text": "Paul A. Swank's immediate documented pre-OSS pathway was United States Army service and training at Camp Claiborne before he volunteered for OSS.",
            "evidence_excerpt": "He volunteered to join the Office of Strategic Services (OSS)",
            "evidence_paraphrase": "The memorial profile gives dated Army and Camp Claiborne service followed by OSS volunteering; NPS corroborates his first-lieutenant OSS role.",
            "identity_match_assessment": "High confidence from the exact-name, rank, hometown, protected-identifier and OSS-mission alignment.",
            "temporal_assessment": "Explicit immediate military pathway. No civilian employer is named or inferred.",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "United States Army service is modeled as a military assignment, not civilian employment.",
            "sources": [
                {"source_key": MEMORIAL, "locator_override": "Biographical comments; Camp Claiborne and OSS-volunteering sequence"},
                {"source_key": NPS, "locator_override": "Paul A. Swank discussion"},
            ],
        },
    ]


def conflict_claims() -> list[dict[str, object]]:
    return [
        {
            "key": "conflict-anthony-i-swarowsky-b933",
            "person_id": PEOPLE[15][0],
            "claim_type": "identity",
            "claim_text": "The protected identifier on the Anthony I Swarowsky index row maps to a materially different full name in the reviewed official Army record; no identity, occupation or assignment is transferred.",
            "evidence_paraphrase": "The official Army candidate agrees on the protected identifier but conflicts materially on the person's name.",
            "identity_match_assessment": "Conflicting. A protected-number match cannot override a materially different official name without the personnel file.",
            "temporal_assessment": "No employment or assignment chronology is accepted from the rejected candidate.",
            "source_quality": "A_direct_official",
            "claim_confidence": "conflicting",
            "publication_status": "conflicting",
            "match_notes": "The candidate is rejected and the unrelated name and protected identifier are omitted from public text.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 457 row 15; Box 760; protected identifier withheld"},
                {"source_key": ARMY_SOURCE, "locator_override": "Rejected materially different-name candidate; protected identifier withheld"},
            ],
        },
        {
            "key": "conflict-harvey-r-swarts-b933",
            "person_id": PEOPLE[16][0],
            "claim_type": "identity",
            "claim_text": "Harvey R Swarts shares a protected index identifier with the separately printed Fred S Watson Jr row; both entities remain separate and no affiliation is transferred.",
            "evidence_paraphrase": "Two differently named printed rows carry the same protected value in the official index.",
            "identity_match_assessment": "Conflicting. The shared identifier may reflect an index error or file relationship, but it does not justify merging two different names.",
            "temporal_assessment": "No employment or military assignment is transferred between the rows.",
            "source_quality": "A_direct_official",
            "claim_confidence": "conflicting",
            "publication_status": "conflicting",
            "match_notes": "The duplicate group is opaque, and the full protected value remains private.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 457 row 16 and page 492 row 26; protected identifier withheld"}
            ],
        },
    ]


def claims() -> list[dict[str, object]]:
    return [*army_claims(), *named_claims(), *conflict_claims()]


def archival_update(row: int, reason: str) -> dict[str, object]:
    person_id, name = PEOPLE[row]
    return {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, Box 760 and archive location, but staged official-register, CIA-site, OSS, employment, occupation, obituary, institutional, newspaper, Library of Congress and archival searches found no defensible identity bridge. {reason}",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": "Review Box 760 for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }


def person_updates() -> list[dict[str, object]]:
    updates = [archival_update(row, reason) for row, reason in UNRESOLVED.items()]
    for row in ARMY:
        update: dict[str, object] = {
            "person_id": PEOPLE[row][0],
            "identity_status": "high_confidence",
            "identity_evidence": "An exact full name and nonshared protected identifier connect the visually verified index row to the reviewed official Army record. The historical occupation field remains separate from employer and immediate-affiliation claims.",
            "manual_review_required": True,
            "research_status": "occupation_only_found",
            "next_action": "Review Box 760 for the immediate pre-OSS affiliation and a named employer or institution.",
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
            "archival_review_priority": "high",
        }
        if row in {9, 21, 23}:
            update.update(
                personnel_category="enlisted_army_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
            )
        else:
            update.update(
                personnel_category="unknown_or_indeterminate",
                commissioned_officer=None,
                allied_or_foreign_personnel=False,
                identity_evidence="An exact full name and nonshared protected identifier connect the index row to the reviewed official Army record. Its damaged grade value PV0 is not interpreted; only the dated historical occupation category is retained.",
            )
        updates.append(update)
    updates.extend(
        [
            {
                "person_id": PEOPLE[7][0],
                "identity_status": "high_confidence",
                "identity_evidence": "The distinctive exact name and the specific West Point, Army engineer, demolitions-instructor and OSS Jedburgh chronology align across an official NPS history and Singlaub interview.",
                "name_variants": ["Lawrence E. Swank", "Lawrence Edwin Swank", "Larry Swank"],
                "personnel_category": "commissioned_army_officer",
                "commissioned_officer": True,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Review Box 760 for the exact Corps of Engineers-to-OSS transfer date and any last civilian employer before military service.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[8][0],
                "identity_status": "high_confidence",
                "identity_evidence": "NPS and the memorial profile align the exact name, first-lieutenant rank, Houston association, OSS mission, wartime chronology and a private protected identifier that is withheld from public data.",
                "name_variants": ["Paul A. Swank"],
                "personnel_category": "commissioned_army_officer",
                "commissioned_officer": True,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Review Box 760 for the exact Army-to-OSS transfer date and any last civilian employer before Army entry.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[15][0],
                "identity_status": "conflicting",
                "identity_evidence": "The index row's protected identifier maps to a materially different full name in the official Army data. The candidate is rejected and no occupation or assignment is transferred.",
                "personnel_category": "unknown_or_indeterminate",
                "commissioned_officer": None,
                "allied_or_foreign_personnel": None,
                "manual_review_required": True,
                "research_status": "conflicting_sources",
                "next_action": "Review Box 760 and the underlying Army record to resolve the protected-identifier/name conflict. Do not use rare-name or unit-roster leads without a second bridge.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[16][0],
                "identity_status": "conflicting",
                "identity_evidence": "The Harvey R Swarts index row shares a protected identifier with a separately printed Fred S Watson Jr row. They remain separate entities and no assignment is transferred.",
                "personnel_category": "unknown_or_indeterminate",
                "commissioned_officer": None,
                "allied_or_foreign_personnel": None,
                "manual_review_required": True,
                "possible_duplicate_group": DUPLICATE_GROUP,
                "research_status": "conflicting_sources",
                "next_action": "Review the Box 760 Swarts file together with the Box 768 Watson file to determine whether the shared identifier is an index error or cross-file relationship.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": FRED_S_WATSON_JR,
                "possible_duplicate_group": DUPLICATE_GROUP,
            },
        ]
    )
    return updates


def research_attempts() -> list[dict[str, object]]:
    attempts: list[dict[str, object]] = []
    for row in sorted(PEOPLE):
        person_id, name = PEOPLE[row]
        if row in ARMY:
            outcome, reviewed, rejected = "source_reviewed", 9, 3
            detail = "An exact name and nonshared protected identifier support a high-confidence official Army identity bridge and dated occupation-only evidence."
        elif row in {7, 8}:
            outcome, reviewed, rejected = "source_reviewed", 11, 4
            detail = "Two independent sources support a high-confidence OSS identity and a documented military pathway; the last civilian employer remains unresolved."
        elif row == 15:
            outcome, reviewed, rejected = "candidate_rejected", 10, 5
            detail = "The official Army candidate was rejected because its protected identifier maps to a materially different full name. Rare-name leads do not resolve the conflict."
        elif row == 16:
            outcome, reviewed, rejected = "source_reviewed", 9, 5
            detail = "The index shares this row's protected identifier with a separately printed Fred S Watson Jr row; an exact-name cavalry-roster lead is not transferred without a file bridge."
        else:
            outcome, reviewed, rejected = "no_result", 7, 4
            detail = UNRESOLVED[row]
        attempts.append(
            {
                "key": f"page457-row{row}-{slug(name)}-b933",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA index and public Archives context; CIA Reading Room site-restricted exact-name discovery; OSS and spelling variants; employer and occupation 1940; obituary, institutional, newspaper, Library of Congress and archival searches; Box 760; protected-identifier Army crosswalk where defensible",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_933",
                "started_at": "2026-10-27T21:00:00Z",
                "completed_at": "2026-10-27T22:12:00Z",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search snippets, genealogy-only assertions, modern profiles, postwar-only leads and sources without an OSS, protected-identifier or Box-file bridge were not assigned. Grouped CIA Reading Room and Library of Congress exact-name checks returned no person-specific Batch 933 result.",
                "research_notes": f"{detail} Relevant index and Army code-list pages were visually checked. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA API call was made.",
                "next_action": "Review Box 760 for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before military service.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b933-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-933-v1",
        "reviewer": "Before OSS Batch 933 evidence review",
        "sources": sources(),
        "organizations": organizations(),
        "affiliations": affiliations(),
        "claims": claims(),
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }
    OUTPUT.write_text(
        json.dumps(bundle, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
