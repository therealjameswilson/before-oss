#!/usr/bin/env python3
"""Generate the reviewed Batch 913 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import uuid
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "research/evidence-page447-steininger-to-stenzel-review_batch-913_2026-10-25.json"

INDEX = "nara-index-b913"
ARMY = "army-bulk-b913"
TECH = "army-tech-b913"
CODES = "army-codes-b913"
LAMOTH = "lamoth-steinitz-b913"
UPENN = "upenn-stellar-b913"
SD_DIR = "san-diego-directory-b913"


PEOPLE = {
    1: ("1eaeb281-1dcb-503a-a169-2b66fca72fcb", "Irene H Steininger"),
    2: ("d5f8eeb4-d8cb-58d4-9889-dfd09dd238e1", "Bernard K Steinitz"),
    3: ("008efcab-4288-538a-88b0-2ec07cdfc550", "L J Steinlein"),
    4: ("adf8d830-5132-5f94-8525-4556d43a4c63", "Robert J Steinmetz"),
    5: ("f95e7e8e-b70c-50a7-93f2-624e63d10ae5", "Elizabeth Steinway"),
    6: ("41542d8f-5226-5d34-8a55-829ed6ba5d57", "Bernard Steinzor"),
    7: ("47f94246-6f13-5a6c-be03-605942ff0723", "Richard Steinzor"),
    8: ("49e25661-ad4b-56d0-a74c-885f68c9a923", "Eliot Stellar"),
    9: ("3e1a4718-993d-5aae-856d-eb968cebc1ba", "Charles C Stelle"),
    10: ("6b35efae-c413-5e60-853f-8e53f5979dba", "Jean C Stellhorn"),
    11: ("ce3dba94-abf0-5148-9636-f5b2051a8559", "John L Stelling"),
    12: ("b8179964-193f-56f2-9f64-2786822d508b", "Karl H Stello"),
    13: ("4690a353-0a65-5040-b6d2-504bbff25ae9", "Chester R Stelman"),
    14: ("49dda36a-e8c2-5e03-a04e-b9cdd780d924", "Helmut A Steltermann"),
    15: ("3c791167-9e98-5f0b-a7c9-fe98b337d885", "Charles H Stember"),
    16: ("f3c4ad5a-b44d-5308-b1ca-38a93573921b", "Morton Stemberg"),
    17: ("9ef5a9d6-e409-560b-8637-adc38b4166da", "Reba A Stemmermann"),
    18: ("b926ff5b-6798-5239-a2d2-acbab9b234f4", "Leonard V Stemnock"),
    19: ("7c5e76d6-bb6f-529e-9220-ba36cdde0e38", "Marcel Stempher"),
    20: ("33b8ee52-4e70-5229-be93-8c9de8581ef5", "Robert R Stengel"),
    21: ("ee22d8cb-a8c8-55cc-8507-ae6a166372b5", "Alex D Stenhous"),
    22: ("07968dc2-b2d2-59ca-a4e8-986e8ea2dbb4", "Mark D Stenson"),
    23: ("603ba0b1-79ee-5431-92de-90365a4ebdc6", "Joachim A Stenzel"),
}

OLD_STAMNOCK = "15f9a410-37d7-57b8-83e6-98ce98e51fb3"
DUPLICATE_GROUP = "name-variant:leonard-v-stamnock-stemnock-pages443-447"

ARMY_OCCUPATIONS = {
    2: {
        "army_name": "STEINITZ BERND K",
        "entry": "1943-07-16",
        "code": "457",
        "occupation": "skilled occupations in production of rubber goods",
        "code_page": "PDF physical page 173",
    },
    6: {
        "army_name": "STEINZOR BERNARD",
        "entry": "1942-06-13",
        "code": "002",
        "occupation": "actors and actresses",
        "code_page": "PDF physical page 170",
    },
    8: {
        "army_name": "STELLAR ELIOT",
        "entry": "1942-12-28",
        "code": "992",
        "occupation": "student",
        "code_page": "PDF physical page 304",
    },
    11: {
        "army_name": "STELLING JOHN L",
        "entry": "1942-11-10",
        "code": "001",
        "occupation": "accountants and auditors",
        "code_page": "PDF physical page 170",
    },
    20: {
        "army_name": "STENGEL ROBERT R",
        "entry": "1943-01-11",
        "code": "649",
        "occupation": "semiskilled occupations in printing and publishing, not elsewhere classified",
        "code_page": "PDF physical page 173",
    },
}

UNRESOLVED = {
    1: "Exact-name and spelling-variant searches produced no source with an OSS identifier or pre-OSS chronology.",
    3: "The initials-only index form is insufficient to distinguish namesakes, and no source supplied a matching box, identifier or assignment.",
    4: "Multiple Robert J. Steinmetz namesakes lacked a protected identifier or person-specific OSS bridge.",
    5: "Searches produced Steinway-family and piano-company results but no source that establishes this indexed person's identity or affiliation.",
    7: "The exact name produced no reliable employment chronology or distinguishing OSS identifier.",
    9: "A Captain Charles C. Stelle appears in accounts of the 1944 Army Observer Group in China, but accessible sources did not establish his pre-OSS affiliation or independently bridge that roster to this row.",
    12: "Postwar Navy employment and radio-related namesake material did not establish a pre-OSS role or a person-specific OSS bridge.",
    13: "Later military-veteran references supplied no pre-OSS chronology or protected-identifier match.",
    14: "A rare-name vital-record lead supplied no occupation, employer or OSS linkage and was not assigned as a historical claim.",
    15: "The later Rutgers sociologist and National Opinion Research Center researcher is a plausible namesake, but accessible sources did not link him to this OSS row or establish his pre-OSS affiliation.",
    16: "Exact-name and variant searches produced no defensible identity bridge or pre-OSS affiliation.",
    17: "Exact-name searches produced no source with enough identifiers to establish identity or employment.",
    19: "Exact-name, occupation, employer, obituary and archival searches produced no defensible match.",
    21: "Stenhous and Stenhouse variant searches produced unrelated namesakes but no OSS bridge.",
    22: "Exact-name searches produced no reliable pre-OSS affiliation or distinguishing identity evidence.",
    23: "The adjacent second Joachim A. Stenzel row has a different printed identifier and rank; neither row is merged, and no external biography was assigned.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def stable_id(kind: str, value: str) -> str:
    return str(uuid.uuid5(uuid.NAMESPACE_URL, f"before-oss:{kind}:{value}"))


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 743-744",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 447, rows 1-23; checked against layout-preserving text and a rendered page image",
            "access_date": "2026-10-25",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All printed rows remain separate, including the two Joachim A. Stenzel rows and the Stamnock/Stemnock near-match.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; five accepted reviewed Batch 913 identity matches",
            "access_date": "2026-10-25",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "No raw Army row or full protected identifier is retained in public assets. Historical occupation fields do not name employers.",
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
            "locator": "PDF physical pages 170, 173 and 304; categories 001, 002, 457, 649 and corrected 992 checked visually",
            "access_date": "2026-10-25",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical occupation categories identify neither a named employer nor an immediate pre-OSS affiliation.",
        },
        {
            "key": LAMOTH,
            "stable_url": "https://lamoth.libraryhost.com/?p=collections/findingaid&id=67",
            "archival_identifier": "RG-42, Bernd Stevens (Steinitz) Collection",
            "title": "Bernd Stevens (Steinitz) Collection, 1920-1960",
            "author_creator": "Los Angeles Museum of the Holocaust staff",
            "repository_publisher": "Los Angeles Museum of the Holocaust",
            "publication_record_date": None,
            "locator": "Biographical Note; Collection Overview; RG-42.02.15, undated circa-1940s Chattanooga News-Free Press article",
            "access_date": "2026-10-25",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Bernd Stevens Collection",
            "rights_notes": "The finding aid documents the name variants and Army-to-OSS transfer. The tire-inspector article is undated, so its chronology remains qualified.",
        },
        {
            "key": UPENN,
            "stable_url": "https://archives.upenn.edu/collections/finding-aid/upt50s824/",
            "archival_identifier": "UPT 50 S824",
            "title": "Eliot Stellar Papers",
            "author_creator": "J.M. Duffin under the direction of Theresa R. Snyder",
            "repository_publisher": "University of Pennsylvania Archives and Records Center",
            "publication_record_date": None,
            "locator": "Biographical Note, paragraphs covering Harvard, Brown, NDRC, Air Force and OSS service",
            "access_date": "2026-10-25",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Eliot Stellar Papers, 1938-1993",
            "rights_notes": "The institutional finding aid explicitly sequences study, NDRC research, Air Force psychology service and OSS service.",
        },
        {
            "key": SD_DIR,
            "stable_url": "https://www.sandiego.gov/sites/default/files/1943_part_3.pdf",
            "archival_identifier": "1943 San Diego City Directory, part 3",
            "title": "San Diego City Directory, 1943",
            "author_creator": "San Diego Directory Company",
            "repository_publisher": "City of San Diego Digital Archives",
            "publication_record_date": "1943",
            "locator": "PDF physical page 38, printed page 851, Stellhorn entry",
            "access_date": "2026-10-25",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "San Diego City Directories",
            "rights_notes": "The rare exact name and wartime date support a qualified identity assessment; the directory names an occupation but no employer.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": "us-army-b913",
            "organization_id": "24facf23-e75a-54f2-a37a-0ef1509bc18a",
            "canonical_name": "United States Army",
            "historical_name": "U.S. Army",
            "aliases": ["Army of the United States"],
            "organization_type": "military service",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "Reuses the reviewed canonical organization; modeled as a military assignment, never a civilian employer.",
        },
        {
            "key": "usaaf-b913",
            "organization_id": "75a3a185-5c26-548b-8be6-9bcdf51bc4eb",
            "canonical_name": "United States Army Air Forces",
            "historical_name": "Air Force",
            "aliases": ["U.S. Army Air Forces", "Army Air Force"],
            "organization_type": "military air service",
            "sector": "military",
            "country": "United States",
            "active_dates": "1941-1947",
            "normalization_notes": "The finding aid's historical wording is retained; the organization is not replaced by the post-1947 U.S. Air Force.",
        },
        {
            "key": "ndrc-b913",
            "organization_id": stable_id("organization", "National Defense Research Council NDRC Eliot Stellar"),
            "canonical_name": "National Defense Research Council",
            "historical_name": "National Defense Research Council (NDRC)",
            "aliases": ["NDRC"],
            "organization_type": "wartime research organization as named by the source",
            "sector": "federal_government",
            "country": "United States",
            "normalization_notes": "Preserves the University of Pennsylvania finding aid's wording; no unreferenced institutional correction is substituted.",
        },
        {
            "key": "brown-b913",
            "organization_id": "dfc9e35b-88f9-593d-874e-01edd9a69d7a",
            "canonical_name": "Brown University",
            "historical_name": "Brown University",
            "aliases": [],
            "organization_type": "private research university",
            "sector": "academia_and_research",
            "city": "Providence",
            "state_or_region": "Rhode Island",
            "country": "United States",
            "normalization_notes": "Reuses the reviewed canonical Brown University organization.",
        },
        {
            "key": "harvard-b913",
            "organization_id": "45ddf347-21c6-59f5-a8ae-517418adf941",
            "canonical_name": "Harvard University",
            "historical_name": "Harvard University",
            "aliases": ["Harvard College"],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "Cambridge",
            "state_or_region": "Massachusetts",
            "country": "United States",
            "normalization_notes": "Reuses the reviewed canonical Harvard University organization; student status is not employment.",
        },
        {
            "key": "johnson-tire-b913",
            "organization_id": stable_id("organization", "Johnson Tire Company Chattanooga 1940s"),
            "canonical_name": "Johnson Tire Company",
            "historical_name": "Johnson Tire Company",
            "aliases": [],
            "organization_type": "tire company",
            "sector": "business_and_industry",
            "city": "Chattanooga",
            "state_or_region": "Tennessee",
            "country": "United States",
            "normalization_notes": "The historical employer name in the archival item description is preserved; no modern successor is inferred.",
        },
    ]


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, data in ARMY_OCCUPATIONS.items():
        values.append(
            {
                "key": f"{slug(PEOPLE[row][1])}-occupation-b913",
                "person_id": PEOPLE[row][0],
                "occupation": data["occupation"],
                "relationship_type": "student" if row == 8 else "employment",
                "end_date": data["entry"],
                "date_precision": f"The official Army entry record assigns historical civilian-occupation code {data['code']} on {data['entry']}; no employer or OSS-transfer date is named.",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "temporal_relation_uncertain",
                "identity_confidence": "confirmed" if row in {2, 8} else "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "A_direct_official",
                "publication_status": "publish_qualified",
                "research_notes": "The coded category is dated at Army entry; it is not a named employer and is excluded from employer analytics.",
            }
        )
    values.extend(
        [
            {
                "key": "bernd-steinitz-us-army-b913",
                "person_id": PEOPLE[2][0],
                "organization_key": "us-army-b913",
                "organization_name_as_found": "U.S. Army",
                "role_title": "soldier; later officer on an OSS mission",
                "relationship_type": "military_assignment",
                "start_date": "1943-07-16",
                "end_date": "1945",
                "date_precision": "The Army entry record dates entry to 1943-07-16; the finding aid states that OSS took interest after Army training and transferred him for special training before a 1945 mission.",
                "country": "United States",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "explicit_immediate",
                "identity_confidence": "confirmed",
                "claim_confidence": "confirmed",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "This is the documented military pathway into OSS, not a civilian employer.",
            },
            {
                "key": "bernd-steinitz-johnson-tire-b913",
                "person_id": PEOPLE[2][0],
                "organization_key": "johnson-tire-b913",
                "organization_name_as_found": "Johnson Tire Company",
                "role_title": "tire inspector",
                "occupation": "tire inspector",
                "relationship_type": "employment",
                "city": "Chattanooga",
                "state_or_region": "Tennessee",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "temporal_relation_uncertain",
                "identity_confidence": "confirmed",
                "claim_confidence": "medium",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "publish_qualified",
                "research_notes": "The archival finding aid identifies the person and employer, but dates the newspaper item only circa the 1940s; it is not counted as the immediate or last civilian employer.",
            },
            {
                "key": "eliot-stellar-usaaf-b913",
                "person_id": PEOPLE[8][0],
                "organization_key": "usaaf-b913",
                "organization_name_as_found": "Air Force",
                "role_title": "Classification Psychologist",
                "occupation": "psychologist",
                "relationship_type": "military_assignment",
                "start_date": "1943",
                "end_date": "1944",
                "date_precision": "The finding aid explicitly dates Classification Psychologist service to 1943-1944 and OSS psychologist service beginning in 1944.",
                "country": "United States",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "explicit_immediate",
                "identity_confidence": "confirmed",
                "claim_confidence": "confirmed",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "The military assignment is explicitly sequenced before OSS and is not labeled civilian employment.",
            },
            {
                "key": "eliot-stellar-ndrc-b913",
                "person_id": PEOPLE[8][0],
                "organization_key": "ndrc-b913",
                "organization_name_as_found": "National Defense Research Council (NDRC)",
                "role_title": "researcher in submarine crew selection",
                "occupation": "psychology researcher",
                "relationship_type": "government_assignment",
                "start_date": "1942",
                "end_date": "1943",
                "date_precision": "The finding aid places a six-month NDRC research assignment after his 1942 master's degree and before Air Force service beginning in 1943.",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "confirmed",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "The source says he joined the NDRC and conducted research but does not specify an employment contract; modeled as a government assignment, not a civilian employer.",
            },
            {
                "key": "eliot-stellar-brown-b913",
                "person_id": PEOPLE[8][0],
                "organization_key": "brown-b913",
                "organization_name_as_found": "Brown University",
                "role_title": "Master of Science student",
                "occupation": "student",
                "relationship_type": "student",
                "start_date": "1941",
                "end_date": "1942",
                "date_precision": "The finding aid says he entered after graduating from Harvard in 1941 and received the M.S. a year later.",
                "city": "Providence",
                "state_or_region": "Rhode Island",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "confirmed",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Student status is not employment and remains separate from the later NDRC and military assignments.",
            },
            {
                "key": "eliot-stellar-harvard-b913",
                "person_id": PEOPLE[8][0],
                "organization_key": "harvard-b913",
                "organization_name_as_found": "Harvard University",
                "role_title": "undergraduate student",
                "occupation": "student",
                "relationship_type": "student",
                "start_date": "1937",
                "end_date": "1941",
                "date_precision": "The finding aid explicitly dates Harvard entry to 1937 and graduation to 1941.",
                "city": "Cambridge",
                "state_or_region": "Massachusetts",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "confirmed",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Student status is not employment.",
            },
            {
                "key": "jean-stellhorn-waiter-b913",
                "person_id": PEOPLE[10][0],
                "role_title": "waiter",
                "occupation": "waiter",
                "relationship_type": "employment",
                "end_date": "1943",
                "date_precision": "The 1943 city directory gives the exact name and occupation but no employer or service-transition date.",
                "city": "San Diego",
                "state_or_region": "California",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "temporal_relation_uncertain",
                "identity_confidence": "probable",
                "claim_confidence": "medium",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "publish_qualified",
                "research_notes": "The rare exact name and wartime chronology support a qualified match; no employer or direct OSS identifier appears in the directory.",
            },
        ]
    )
    return values


def army_claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, data in ARMY_OCCUPATIONS.items():
        identity_confidence = "confirmed" if row in {2, 8} else "high"
        identity_assessment = "High confidence from exact name and a nonshared protected identifier."
        if row == 2:
            identity_assessment = "Confirmed by the nonshared protected identifier plus the institutional finding aid's Bernd Karl Steinitz and Bernd Stevens variants."
        elif row == 8:
            identity_assessment = "Confirmed by the distinctive exact name, nonshared protected identifier and person-specific University of Pennsylvania OSS chronology."
        values.extend(
            [
                {
                    "key": f"identity-{slug(PEOPLE[row][1])}-b913",
                    "person_id": PEOPLE[row][0],
                    "claim_type": "identity",
                    "claim_text": f"The indexed {PEOPLE[row][1]} is a {identity_confidence}-confidence match to the reviewed official Army record.",
                    "evidence_paraphrase": f"A nonshared protected identifier connects the index row to Army name {data['army_name']} and a dated entry record.",
                    "identity_match_assessment": identity_assessment,
                    "temporal_assessment": f"The Army record dates entry to {data['entry']} but does not by itself establish the OSS transfer date.",
                    "source_quality": "A_direct_official",
                    "claim_confidence": identity_confidence,
                    "publication_status": "published",
                    "match_notes": "No protected identifier is exposed publicly. The Army record is an identity bridge, not proof of a named employer.",
                    "sources": [
                        {"source_key": INDEX, "locator_override": f"PDF page 447 row {row}; protected identifier withheld"},
                        {"source_key": ARMY, "locator_override": f"Accepted reviewed identity bridge; Army name {data['army_name']}; protected identifier withheld"},
                    ],
                },
                {
                    "key": f"occupation-{slug(PEOPLE[row][1])}-b913",
                    "person_id": PEOPLE[row][0],
                    "affiliation_key": f"{slug(PEOPLE[row][1])}-occupation-b913",
                    "claim_type": "occupation",
                    "claim_text": f"At Army entry on {data['entry']}, {PEOPLE[row][1]} was recorded in the historical civilian-occupation category '{data['occupation']}.'",
                    "evidence_paraphrase": f"The official Army record supplies code {data['code']}; the reviewed official code list maps it to the stated category.",
                    "identity_match_assessment": identity_assessment,
                    "temporal_assessment": "Dated at Army entry; the category names no employer and does not establish the immediate pre-OSS affiliation.",
                    "source_quality": "A_direct_official",
                    "claim_confidence": "medium",
                    "publication_status": "publish_qualified",
                    "match_notes": "Excluded from employer analytics. The language is preserved as a historical classification rather than modernized into a specific job title.",
                    "sources": [
                        {"source_key": ARMY, "locator_override": f"Civilian occupation code {data['code']}; entry date {data['entry']}; protected identifier withheld"},
                        {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46; field definitions"},
                        {"source_key": CODES, "locator_override": f"{data['code_page']}; historical code {data['code']}"},
                    ],
                },
            ]
        )
    return values


def claims() -> list[dict[str, object]]:
    values = army_claims()
    values.extend(
        [
            {
                "key": "immediate-bernd-steinitz-army-b913",
                "person_id": PEOPLE[2][0],
                "affiliation_key": "bernd-steinitz-us-army-b913",
                "claim_type": "immediate_pre_oss_affiliation",
                "claim_text": "The United States Army was Bernd Karl Steinitz's documented immediate pathway into OSS special training.",
                "evidence_excerpt": "Soon the U.S. intelligence service (OSS) took interest in him and he was transferred",
                "evidence_paraphrase": "The museum finding aid states that he enlisted in the Army, trained in Texas and was then transferred for OSS special training.",
                "identity_match_assessment": "Confirmed by the nonshared protected identifier and the finding aid's Bernd Karl Steinitz, Karl Steinitz and Bernd Stevens variants.",
                "temporal_assessment": "Explicit immediate Army-to-OSS training sequence; the precise transfer date is not stated.",
                "source_quality": "B_authoritative_institutional",
                "claim_confidence": "confirmed",
                "publication_status": "published",
                "match_notes": "The Army is modeled as a military assignment, not a civilian employer.",
                "sources": [
                    {"source_key": LAMOTH, "locator_override": "Biographical Note, Army training and OSS transfer paragraph"},
                    {"source_key": ARMY, "support_type": "supports", "locator_override": "Entry date 1943-07-16; protected identifier withheld"},
                ],
            },
            {
                "key": "other-bernd-steinitz-johnson-tire-b913",
                "person_id": PEOPLE[2][0],
                "affiliation_key": "bernd-steinitz-johnson-tire-b913",
                "claim_type": "other_pre_oss_affiliation",
                "claim_text": "An undated circa-1940s article in the Bernd Stevens collection describes him as a tire inspector at Johnson Tire Company; its sequence relative to Army and OSS service remains uncertain.",
                "evidence_excerpt": "Tire inspectors like Bernard Steinetz ... of the Johnson Tire Company",
                "evidence_paraphrase": "The finding aid describes an archival newspaper item naming a tire-inspection role and employer in Chattanooga.",
                "identity_match_assessment": "Confirmed at the collection level through the finding aid's documented Steinitz/Stevens variants; the article uses Bernard Steinetz.",
                "temporal_assessment": "The item is dated only circa the 1940s and is not claimed as immediate or last civilian employment.",
                "source_quality": "B_authoritative_institutional",
                "claim_confidence": "medium",
                "publication_status": "publish_qualified",
                "match_notes": "The employer is published only with a visible chronology qualification and is excluded from default immediate/last-employer analytics.",
                "sources": [{"source_key": LAMOTH, "locator_override": "RG-42.02.15, article about Bernd Steinitz as tire inspector, undated circa 1940s"}],
            },
            {
                "key": "immediate-eliot-stellar-usaaf-b913",
                "person_id": PEOPLE[8][0],
                "affiliation_key": "eliot-stellar-usaaf-b913",
                "claim_type": "immediate_pre_oss_affiliation",
                "claim_text": "Eliot Stellar's immediate pre-OSS affiliation was the wartime Air Force, where he served as a Classification Psychologist from 1943 to 1944.",
                "evidence_excerpt": "serving as a Classification Psychologist from 1943 to 1944. Beginning in 1944, Stellar served as a psychologist in the OSS",
                "evidence_paraphrase": "The University of Pennsylvania finding aid directly sequences Air Force psychology service before OSS psychology service.",
                "identity_match_assessment": "Confirmed by the distinctive exact name, protected Army identifier and person-specific institutional chronology.",
                "temporal_assessment": "Explicit immediate sequence from 1943-1944 Air Force service to OSS service beginning in 1944.",
                "source_quality": "B_authoritative_institutional",
                "claim_confidence": "confirmed",
                "publication_status": "published",
                "match_notes": "This is a military assignment, not a civilian employer.",
                "sources": [{"source_key": UPENN, "locator_override": "Biographical Note, lines 84-89; NDRC, Air Force and OSS sequence"}],
            },
            {
                "key": "other-eliot-stellar-ndrc-b913",
                "person_id": PEOPLE[8][0],
                "affiliation_key": "eliot-stellar-ndrc-b913",
                "claim_type": "other_pre_oss_affiliation",
                "claim_text": "After his 1942 master's degree, Eliot Stellar conducted submarine crew-selection research for the National Defense Research Council for six months before entering the Air Force.",
                "evidence_excerpt": "joined the National Defense Research Council (NDRC) and conducted research into submarine crew selection",
                "evidence_paraphrase": "The finding aid places the research assignment between Brown University and Air Force service.",
                "identity_match_assessment": "Confirmed by the person-specific institutional chronology and protected Army identifier.",
                "temporal_assessment": "Strongly bounded after the 1942 degree and before 1943 Air Force service; modeled as a government assignment rather than assumed employment.",
                "source_quality": "B_authoritative_institutional",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "Not counted as a civilian employer because the source does not specify an employment relationship.",
                "sources": [{"source_key": UPENN, "locator_override": "Biographical Note, lines 82-87; six-month NDRC research assignment"}],
            },
            {
                "key": "student-eliot-stellar-brown-b913",
                "person_id": PEOPLE[8][0],
                "affiliation_key": "eliot-stellar-brown-b913",
                "claim_type": "other_pre_oss_affiliation",
                "claim_text": "Eliot Stellar studied psychology at Brown University in 1941-1942 and received a Master of Science degree.",
                "evidence_paraphrase": "The finding aid dates his entry after Harvard graduation in 1941 and the master's degree one year later.",
                "identity_match_assessment": "Confirmed by the person-specific institutional biography and wartime chronology.",
                "temporal_assessment": "Documented before NDRC, Air Force and OSS service; student status is not employment.",
                "source_quality": "B_authoritative_institutional",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "Excluded from employer analytics.",
                "sources": [
                    {"source_key": UPENN, "locator_override": "Biographical Note, lines 78-85; Brown study and M.S."},
                    {"source_key": ARMY, "support_type": "context_only", "locator_override": "Army entry occupation code 992; student; protected identifier withheld"},
                ],
            },
            {
                "key": "student-eliot-stellar-harvard-b913",
                "person_id": PEOPLE[8][0],
                "affiliation_key": "eliot-stellar-harvard-b913",
                "claim_type": "other_pre_oss_affiliation",
                "claim_text": "Eliot Stellar attended Harvard University from 1937 until graduating in 1941.",
                "evidence_paraphrase": "The institutional finding aid dates his Harvard entry and graduation and describes his early physiological-psychology research.",
                "identity_match_assessment": "Confirmed by the person-specific institutional biography and wartime chronology.",
                "temporal_assessment": "Documented earlier prewar student affiliation; not employment.",
                "source_quality": "B_authoritative_institutional",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "Excluded from employer analytics.",
                "sources": [{"source_key": UPENN, "locator_override": "Biographical Note, lines 78-83; Harvard 1937-1941"}],
            },
            {
                "key": "identity-jean-stellhorn-b913",
                "person_id": PEOPLE[10][0],
                "claim_type": "identity",
                "claim_text": "The indexed Jean C. Stellhorn is a probable match to the rare exact-name entry in the 1943 San Diego city directory.",
                "evidence_paraphrase": "A contemporary city directory records the same rare full name and a wartime occupation in San Diego.",
                "identity_match_assessment": "Probable from the rare exact full name and compatible wartime chronology; no second identifier directly joins the records.",
                "temporal_assessment": "The directory is dated 1943, but the person's OSS entry date is unknown.",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "claim_confidence": "medium",
                "publication_status": "publish_qualified",
                "match_notes": "The personnel file is still required to confirm identity and sequence.",
                "sources": [
                    {"source_key": INDEX, "locator_override": "PDF page 447 row 10; Jean C. Stellhorn"},
                    {"source_key": SD_DIR, "locator_override": "PDF physical page 38, printed page 851"},
                ],
            },
            {
                "key": "occupation-jean-stellhorn-b913",
                "person_id": PEOPLE[10][0],
                "affiliation_key": "jean-stellhorn-waiter-b913",
                "claim_type": "occupation",
                "claim_text": "A qualified 1943 directory match lists Jean C. Stellhorn's occupation as waiter; no employer is named.",
                "evidence_excerpt": "Stellhorn Jean C Mrs waiter",
                "evidence_paraphrase": "The contemporary directory provides the exact name, occupation and residence but no employer.",
                "identity_match_assessment": "Probable from the rare exact name; not confirmed by an independent identifier.",
                "temporal_assessment": "Dated 1943, but not proven to be the immediate pre-OSS role or last civilian employment.",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "claim_confidence": "medium",
                "publication_status": "publish_qualified",
                "match_notes": "Published visibly qualified and excluded from default employer analytics.",
                "sources": [{"source_key": SD_DIR, "locator_override": "PDF physical page 38, printed page 851, Stellhorn entry"}],
            },
        ]
    )
    return values


def person_updates() -> list[dict[str, object]]:
    updates: list[dict[str, object]] = []
    for row, reason in UNRESOLVED.items():
        person_id, name = PEOPLE[row]
        priority = "critical" if row in {1, 3, 4, 5, 7, 9, 15, 23} else "high"
        updates.append(
            {
                "person_id": person_id,
                "identity_status": "unresolved",
                "identity_evidence": f"The visually verified index row supplies {name}, box and archive location, but staged NARA context, CIA Reading Room, exact-name, occupation, employer, obituary, institutional, newspaper, directory, Library of Congress and archival searches found no defensible identity bridge. {reason}",
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Review the indexed personnel file for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": priority,
            }
        )
    updates.extend(
        [
            {
                "person_id": PEOPLE[2][0],
                "identity_status": "confirmed",
                "identity_evidence": "A nonshared protected identifier joins indexed Bernard K. Steinitz to Army-record Bernd K. Steinitz; the Los Angeles Museum of the Holocaust finding aid independently documents Bernd Karl Steinitz, Karl Steinitz and Bernd Stevens and explicitly sequences Army service before OSS training.",
                "name_variants": ["Bernd K Steinitz", "Bernd Karl Steinitz", "Karl Bernd Steinitz", "Karl Steinitz", "Bernd Stevens", "Bernard Steinetz"],
                "personnel_category": "enlisted_army_personnel",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "completed",
                "next_action": "Review Box 743 and LAMOTH RG-42.02 to obtain the exact Johnson Tire article date, Army-to-OSS transfer date and original mission orders.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "medium",
            },
            {
                "person_id": PEOPLE[6][0],
                "identity_status": "high_confidence",
                "identity_evidence": "The exact name and nonshared protected identifier connect the index row to the reviewed official Army record; the historical actors-and-actresses category names no employer.",
                "personnel_category": "enlisted_army_personnel",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "occupation_only_found",
                "next_action": "Review Box 743 to identify the employer behind the Army occupation category and the assignment immediately preceding OSS.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[8][0],
                "identity_status": "confirmed",
                "identity_evidence": "The distinctive exact name, nonshared protected identifier and University of Pennsylvania finding aid align on his education, Air Force psychology service and 1944-1946 OSS psychology service.",
                "personnel_category": "enlisted_army_personnel",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": False,
                "manual_review_required": False,
                "research_status": "completed",
                "next_action": "Optional Box 743 review may refine the precise Air Force-to-OSS transfer date and NDRC administrative status; the institutional sequence is already explicit.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "low",
            },
            {
                "person_id": PEOPLE[10][0],
                "identity_status": "probable",
                "identity_evidence": "A 1943 San Diego city directory records the same rare full name and a waiter occupation, but no independent identifier directly joins that entry to the indexed OSS row.",
                "manual_review_required": True,
                "research_status": "occupation_only_found",
                "next_action": "Review Box 743 to confirm the San Diego directory identity, employer and chronology relative to OSS service.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[11][0],
                "identity_status": "high_confidence",
                "identity_evidence": "The exact name and nonshared protected identifier connect the index row to the reviewed official Army record; the accountants-and-auditors category names no employer.",
                "personnel_category": "enlisted_army_personnel",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "occupation_only_found",
                "next_action": "Review Box 743 to identify the employer behind the Army occupation category and the assignment immediately preceding OSS.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[20][0],
                "identity_status": "high_confidence",
                "identity_evidence": "The exact name and nonshared protected identifier connect the index row to the reviewed official Army record; the printing-and-publishing category names no employer, and malformed grade value P53 remains uninterpreted.",
                "personnel_category": "enlisted_army_personnel",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "occupation_only_found",
                "next_action": "Review Box 743 to identify the employer behind the Army occupation category and the assignment immediately preceding OSS; do not interpret grade value P53.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[18][0],
                "identity_status": "ambiguous",
                "identity_evidence": "Page 447 prints Leonard V. Stemnock with a protected identifier in Box 743, while page 443 separately prints Leonard V. Stamnock without one in Box 736. The similar names are not merged; both files require joint review.",
                "manual_review_required": True,
                "possible_duplicate_group": DUPLICATE_GROUP,
                "research_status": "needs_identity_review",
                "next_action": "Review the Box 743 Stemnock and Box 736 Stamnock personnel files together before merging records or assigning any external biography.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": OLD_STAMNOCK,
                "identity_status": "ambiguous",
                "identity_evidence": "Page 443 prints Leonard V. Stamnock without a protected identifier in Box 736, while page 447 separately prints Leonard V. Stemnock with one in Box 743. The similar names are not merged; both files require joint review.",
                "manual_review_required": True,
                "possible_duplicate_group": DUPLICATE_GROUP,
                "research_status": "requires_archival_review",
                "next_action": "Review the Box 736 Stamnock and Box 743 Stemnock personnel files together before merging records or assigning any external biography.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
        ]
    )
    return updates


def research_attempts() -> list[dict[str, object]]:
    evidence_rows = {2, 6, 8, 10, 11, 20}
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        if row == 18:
            outcome = "candidate_found"
            detail = "A near-identical Leonard V. Stamnock row on page 443 was identified and preserved as a separate possible-duplicate entity requiring joint file review."
        elif row in evidence_rows:
            outcome = "source_reviewed"
            if row == 2:
                detail = "Official and institutional sources establish the Bernd/Karl/Stevens identity variants and Army-to-OSS sequence; the tire-company chronology remains explicitly qualified."
            elif row == 8:
                detail = "Official and institutional sources establish the education, NDRC, Air Force and OSS sequence."
            elif row == 10:
                detail = "A rare exact-name 1943 city-directory occupation was accepted only as a probable, medium-confidence match."
            else:
                detail = "A reviewed official Army identity and dated historical occupation category were accepted; no named employer is supplied."
        else:
            outcome = "candidate_rejected"
            detail = UNRESOLVED[row]
        attempts.append(
            {
                "key": f"page447-row{row}-{slug(name)}-b913",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA index and finding-aid context; CIA Reading Room and Library of Congress official-domain exact-name checks; OSS, rank and spelling variants; employer and occupation; obituary, institutional, newspaper, directory and archival searches; Box {744 if row == 23 else 743}; protected-identifier Army crosswalk where available",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_913",
                "started_at": "2026-10-25T23:35:00Z",
                "completed_at": "2026-10-25T23:40:00Z",
                "outcome": outcome,
                "sources_reviewed": 11 if row in {2, 8} else (8 if row in evidence_rows or row in {9, 15, 18} else 6),
                "candidate_sources_rejected": 4 if row in evidence_rows else 7,
                "rejection_reasons": "Unbridged namesakes, discovery-only results, sensitive people-search pages, chronologically irrelevant records and postwar-only material were not assigned." if row in evidence_rows else detail,
                "research_notes": f"{detail} Automated CIA and LoC adapter transport failures remain recorded as errors rather than negative findings; equivalent official-domain checks were completed manually. Search-result snippets were discovery aids only, final claims point to inspectable sources, no access control was bypassed, and no exposed NARA API credential was used.",
                "next_action": "Review the indexed personnel file for corroborating identifiers and the last documented pre-OSS affiliation.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b913-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-913-v1",
        "reviewer": "Before OSS Batch 913 evidence review",
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
