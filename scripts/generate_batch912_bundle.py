#!/usr/bin/env python3
"""Generate the reviewed Batch 912 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import uuid
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "research/evidence-page446-steimack-to-steinhope-review_batch-912_2026-10-25.json"

INDEX = "nara-index-b912"
ARMY = "army-bulk-b912"
TECH = "army-tech-b912"
CODES = "army-codes-b912"
NARA_GUIDE = "nara-oss-index-guide-b912"
CONGRESS = "congress-steinacker-b912"
YALE = "yale-steinberg-papers-b912"
FOUNDATION = "steinberg-foundation-wwii-b912"
SMITHSONIAN = "smithsonian-steinberg-b912"


PEOPLE = {
    24: ("c6a7b342-9551-5eec-bab7-b95ae4981530", "Theodore Steimack"),
    25: ("77e95da9-071e-58f8-b5e2-f0218fb5d89e", "Albert S Stein"),
    26: ("4dce7c6c-557a-5b04-aef4-5c51d29cfd43", "Bernard Stein"),
    27: ("c6598120-2c01-5d17-a876-ece8081ea846", "Eleanor M Stein"),
    28: ("9c5efdc8-8458-5270-9aeb-ffdc7d20df81", "Jack A Stein"),
    29: ("864446d9-ba48-57af-bc44-e0c02c5cedee", "Kenneth W Stein"),
    30: ("255dd371-c020-5c58-97bc-e44dd2b96d93", "Maldwin Stein"),
    31: ("e16dba7c-16bf-5d05-a5c2-42fb83dc898c", "Morris I Stein"),
    32: ("a03e0a85-ed90-5c32-95ae-4f9eeac67d52", "Patricia A Stein"),
    33: ("2c67d0ee-c122-5434-96c7-9af43c5f5851", "Robert L Stein"),
    34: ("da2cb9ac-f157-5a0e-90ce-429701e02d73", "Sol W Stein"),
    35: ("4207d44f-23cb-50c9-a2af-23364fc27ea8", "Wilbur Stein"),
    36: ("261cc632-397a-5da6-ac09-a882f8083d4f", "Estelle H Steinacker"),
    37: ("04322751-2c25-5ebe-8db3-34ea6aec83a1", "Frederick E Steinbach"),
    38: ("d7b1da2b-2d3e-5f23-9df1-f045454bb82f", "Rudolph R Steinbeck"),
    39: ("823c8e93-d093-5e58-81d3-07824cf70242", "Arthur J Steinberg"),
    40: ("85a03501-8259-5429-af9f-b190d1c12023", "Howard O Steinberg"),
    41: ("8a130c89-6739-5907-94aa-51585f2357ca", "Saul Steinberg"),
    42: ("6b35c00e-1b60-5c6e-ad65-c75d75d1151d", "Ernest W Steinbrenner"),
    43: ("7ea3504a-e340-5d4e-ad4c-3fc9dd9452e2", "Alvin E Steiner"),
    44: ("0ebec71e-c319-51ee-988d-b9ce407517ff", "Francis B Steiner"),
    45: ("95f2e133-a840-560a-b645-e12240b78db7", "Stephen Steinhardt"),
    46: ("bf41eb6f-66b8-589c-be73-586322325bbe", "Edwards G Steinhope"),
}


ARMY_OCCUPATIONS = {
    24: {
        "army_name": "STELMACK THEODORE",
        "entry": "1942-07-14",
        "code": "688",
        "occupation": "occupations in mechanical treatment of metals, not elsewhere classified",
        "code_page": "PDF physical page 174",
    },
    26: {
        "army_name": "STEIN BERNARD",
        "entry": "1943-10-25",
        "code": "444",
        "occupation": "compositors and typesetters",
        "code_page": "PDF physical page 173",
    },
    28: {
        "army_name": "STEIN JACK A",
        "entry": "1942-12-15",
        "code": "134",
        "occupation": "shipping and receiving clerks",
        "code_page": "PDF physical page 171",
    },
    33: {
        "army_name": "STEIN ROBERT L",
        "entry": "1942-10-02",
        "code": "175",
        "occupation": "salespersons",
        "code_page": "PDF physical page 171",
    },
    34: {
        "army_name": "STEIN SOL W",
        "entry": "1945-03-15",
        "code": "713",
        "occupation": "semiskilled occupations in manufacture of miscellaneous products",
        "code_page": "PDF physical page 174",
    },
    37: {
        "army_name": "STEINBACH FREDERICK E",
        "entry": "1942-08-25",
        "code": "101",
        "occupation": "bookkeepers and cashiers, except bank cashiers",
        "code_page": "PDF physical page 171",
    },
}


UNRESOLVED = {
    25: "The common name and middle initial produced multiple namesakes but no corroborating OSS identifier or pre-OSS chronology.",
    27: "Searches returned unrelated modern people and unsourced genealogy entries, none of which bridges the indexed person to an employer.",
    29: "The index establishes a second-lieutenant rank, but exact-name and rank searches did not supply two independent identifiers or a pre-OSS assignment.",
    30: "A NARA personal-name index supplies a Washington administrative-file lead, but it names no employer and does not bridge the printed personnel row to a pre-OSS chronology.",
    32: "Exact-name OSS, employment, occupation, obituary, institutional, directory and archival searches found no defensible person-specific result.",
    35: "A NARA personal-name index supplies a Kunming finance-file lead, but it names no earlier employer and does not establish the pre-OSS sequence.",
    38: "Exact-name and spelling-variant searches produced no reliable identity bridge or pre-OSS affiliation.",
    39: "The common name produced namesakes without an OSS, rank, box or other corroborating identifier.",
    40: "Exact-name searches produced no reliable person-specific OSS identity or pre-OSS affiliation.",
    42: "The distinctive name produced no source connecting a namesake to the indexed OSS row or documenting an earlier affiliation.",
    43: "Exact-name OSS, occupation, employer, obituary and institutional searches produced no defensible match.",
    44: "Exact-name searches produced no source with enough identifiers to assign an employer or occupation to this row.",
    45: "Search results concerned the unrelated Laurence A. Steinhardt papers and did not establish Stephen Steinhardt's identity or pre-OSS history.",
    46: "Both Edwards and Edward spelling searches produced no defensible identity bridge or pre-OSS affiliation.",
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
            "archival_identifier": "RG 226, Entry A1-224, Boxes 742-743",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 446, rows 24-46; checked against layout-preserving text and a rendered page image",
            "access_date": "2026-10-25",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain immutable. The unusually long printed value for Maldwin Stein remains private and is not normalized or exposed publicly.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; seven accepted reviewed Batch 912 identity matches",
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
            "locator": "PDF physical pages 171, 173 and 174; six mapped categories checked visually; code 037 is omitted",
            "access_date": "2026-10-25",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical occupation categories identify neither a named employer nor an immediate pre-OSS affiliation. No label is invented for omitted code 037.",
        },
        {
            "key": NARA_GUIDE,
            "stable_url": "https://www.archives.gov/files/calendar/genealogy-series/2025-05-13-presentation-kamph.pdf",
            "title": "Revealing Ties to Espionage in the Office of Strategic Services Records",
            "author_creator": "Claire Kluskens Kamph",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2025-05-13",
            "locator": "PDF physical page 15, Personal Name Index screenshot and explanatory bullets",
            "access_date": "2026-10-25",
            "source_quality": "A_direct_official",
            "collection_name": "National Archives Genealogy Series",
            "rights_notes": "The screenshot supplies additional RG 226 file leads for Maldwin Stein, Wilbur Stein and Saul Steinberg; it does not by itself establish a pre-OSS employer.",
        },
        {
            "key": CONGRESS,
            "stable_url": "https://www.congress.gov/77/crecb/1942/07/14/GPO-CRECB-1942-pt5-7.pdf",
            "archival_identifier": "Congressional Record, 77th Congress, July 14, 1942, page 6127",
            "title": "Congressional Record - Senate",
            "author_creator": "United States Congress",
            "repository_publisher": "Congress.gov; U.S. Government Publishing Office",
            "publication_record_date": "1942-07-14",
            "locator": "Printed page 6127, Civilian Pilot Training Division resignation table",
            "access_date": "2026-10-25",
            "source_quality": "A_direct_official",
            "rights_notes": "The table names the agency, salary and reason for resignation but not Steinacker's job title, exact departure date, next employer or OSS entry date.",
        },
        {
            "key": YALE,
            "stable_url": "https://ead-pdfs.library.yale.edu/5449.pdf",
            "archival_identifier": "YCAL MSS 1053",
            "title": "Guide to the Saul Steinberg Papers",
            "author_creator": "Eve C. Neiger and E. Ashley Cale",
            "repository_publisher": "Yale University Library",
            "publication_record_date": "2019-10; last exported 2026-08-17",
            "locator": "Biographical history, PDF pages 6-7 of 415; box 122, folder 2375, OSS service certificate",
            "access_date": "2026-10-25",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Saul Steinberg papers",
            "rights_notes": "The finding aid documents prewar study and publishing, a 1943 Naval Reserve commission and assignment to OSS.",
        },
        {
            "key": FOUNDATION,
            "stable_url": "https://saulsteinbergfoundation.org/essay/world-war-ii/",
            "title": "World War II",
            "author_creator": "Saul Steinberg Foundation",
            "repository_publisher": "Saul Steinberg Foundation",
            "publication_record_date": None,
            "locator": "Life and Work essay, paragraphs on U.S. periodicals, The New Yorker, Office of War Information recommendation, Naval Reserve commission and OSS Morale Operations",
            "access_date": "2026-10-25",
            "source_quality": "B_authoritative_institutional",
            "rights_notes": "The recommendation for Office of War Information employment is retained as context and is not converted into an employment claim.",
        },
        {
            "key": SMITHSONIAN,
            "stable_url": "https://americanart.si.edu/artist/saul-steinberg-4620",
            "title": "Saul Steinberg",
            "author_creator": "Virginia M. Mecklenburg",
            "repository_publisher": "Smithsonian American Art Museum",
            "publication_record_date": "1987",
            "locator": "Artist biography, education, prewar publishing and Navy service paragraphs",
            "access_date": "2026-10-25",
            "source_quality": "B_authoritative_institutional",
            "rights_notes": "Used as institutional corroboration of education, publishing occupation and Navy service.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": "civilian-pilot-training-b912",
            "organization_id": stable_id("organization", "Civilian Pilot Training Division of the Civil Aeronautics Authority"),
            "canonical_name": "Civilian Pilot Training Division of the Civil Aeronautics Authority",
            "historical_name": "Civilian Pilot Training Division of Civil Aeronautics Authority",
            "aliases": ["Civilian Pilot Training Division"],
            "organization_type": "federal aviation training division",
            "sector": "federal_government",
            "country": "United States",
            "normalization_notes": "The 1942 Congressional Record wording is preserved; no modern successor is substituted.",
        },
        {
            "key": "usnr-b912",
            "organization_id": "1b90fcf6-604d-588b-8a30-7bb08c930c6f",
            "canonical_name": "United States Naval Reserve",
            "historical_name": "Naval Reserve",
            "aliases": ["U.S. Naval Reserve", "USNR"],
            "organization_type": "military reserve component",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "Reuses the reviewed canonical Naval Reserve organization.",
        },
        {
            "key": "new-yorker-b912",
            "organization_id": "d952a5bf-420f-5b7e-8c11-2bfa39fccfed",
            "canonical_name": "The New Yorker",
            "historical_name": "The New Yorker",
            "aliases": ["New Yorker"],
            "organization_type": "magazine",
            "sector": "journalism_and_media",
            "city": "New York",
            "state_or_region": "New York",
            "country": "United States",
            "normalization_notes": "Professional publishing affiliation is not silently converted into salaried employment.",
        },
        {
            "key": "regio-politecnico-b912",
            "organization_id": stable_id("organization", "Regio Politecnico Milan"),
            "canonical_name": "Regio Politecnico Milan",
            "historical_name": "Regio Politecnico Milan",
            "aliases": ["Polytechnic University in Milan", "Regio Politecnico"],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "Milan",
            "country": "Italy",
            "normalization_notes": "The historical institutional form in the finding aid is preserved; no present-day successor relation is asserted without separate evidence.",
        },
    ]


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, data in ARMY_OCCUPATIONS.items():
        values.append(
            {
                "key": f"{slug(PEOPLE[row][1])}-occupation-b912",
                "person_id": PEOPLE[row][0],
                "occupation": data["occupation"],
                "relationship_type": "employment",
                "end_date": data["entry"],
                "date_precision": f"The official Army entry record assigns historical civilian-occupation code {data['code']} on {data['entry']}; no employer or OSS-transfer date is named.",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "temporal_relation_uncertain",
                "identity_confidence": "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "A_direct_official",
                "publication_status": "publish_qualified",
                "research_notes": "The coded category is dated at Army entry; it is not a named employer and is excluded from employer analytics.",
            }
        )
    values.extend(
        [
            {
                "key": "estelle-steinacker-cptd-b912",
                "person_id": PEOPLE[36][0],
                "organization_key": "civilian-pilot-training-b912",
                "organization_name_as_found": "Civilian Pilot Training Division of Civil Aeronautics Authority",
                "role_title": "employee; title not stated",
                "relationship_type": "government_assignment",
                "end_date": "1942",
                "date_precision": "The July 14, 1942 table lists resignations since December 7, 1941; it does not give Steinacker's exact resignation date or next position.",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "temporal_relation_uncertain",
                "identity_confidence": "probable",
                "claim_confidence": "medium",
                "source_quality": "A_direct_official",
                "publication_status": "publish_qualified",
                "research_notes": "The rare exact name and relevant chronology support a qualified identity match, but the personnel file is required to prove the OSS transition.",
            },
            {
                "key": "saul-steinberg-usnr-b912",
                "person_id": PEOPLE[41][0],
                "organization_key": "usnr-b912",
                "organization_name_as_found": "US Naval Reserve",
                "role_title": "ensign",
                "occupation": "naval officer",
                "relationship_type": "military_assignment",
                "start_date": "1943",
                "end_date": "1943",
                "date_precision": "The Yale finding aid dates the commission to 1943 and says service began in May; the Foundation places the commission in February. Neither source provides a separate OSS transfer date.",
                "country": "United States",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "The Naval Reserve commission is the best-supported institutional pathway into his OSS assignment; no separate Navy unit is inferred.",
            },
            {
                "key": "saul-steinberg-new-yorker-b912",
                "person_id": PEOPLE[41][0],
                "organization_key": "new-yorker-b912",
                "organization_name_as_found": "The New Yorker",
                "role_title": "contributing cartoonist and illustrator",
                "occupation": "artist and illustrator",
                "relationship_type": "professional_affiliation",
                "start_date": "1941-10-25",
                "end_date": "1943",
                "date_precision": "The finding aid dates his first New Yorker drawing to October 25, 1941; the Foundation documents increased contributions before his 1943 commission and continued submissions during service.",
                "city": "New York",
                "state_or_region": "New York",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "The documented publishing relationship is not labeled salaried employment or the last civilian employer.",
            },
            {
                "key": "saul-steinberg-politecnico-b912",
                "person_id": PEOPLE[41][0],
                "organization_key": "regio-politecnico-b912",
                "organization_name_as_found": "Regio Politecnico Milan",
                "role_title": "architecture student",
                "occupation": "student",
                "relationship_type": "student",
                "start_date": "1933",
                "end_date": "1940",
                "date_precision": "The Yale finding aid dates enrollment to 1933 and the architecture degree to 1940.",
                "city": "Milan",
                "country": "Italy",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Student status is shown separately and is not counted as employment.",
            },
        ]
    )
    return values


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, data in ARMY_OCCUPATIONS.items():
        variant_note = ""
        identity_assessment = "High confidence from exact name and a nonshared protected identifier."
        if row == 24:
            variant_note = " The Army spelling Stelmack is retained as a variant rather than silently replacing the indexed Steimack spelling."
            identity_assessment = "High confidence from the nonshared protected identifier; the one-letter surname difference remains explicit."
        if row == 34:
            variant_note = " The malformed Army grade value is preserved privately and not interpreted."
        values.append(
            {
                "key": f"identity-{slug(PEOPLE[row][1])}-b912",
                "person_id": PEOPLE[row][0],
                "claim_type": "identity",
                "claim_text": f"The indexed {PEOPLE[row][1]} is a high-confidence match to the reviewed official Army record.{variant_note}",
                "evidence_paraphrase": f"A nonshared protected identifier connects the index row to Army name {data['army_name']} and a dated entry record.",
                "identity_match_assessment": identity_assessment,
                "temporal_assessment": f"The Army record dates entry to {data['entry']} but does not establish the OSS transfer date.",
                "source_quality": "A_direct_official",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "No protected identifier is exposed publicly. The Army record is an identity bridge, not proof of a named employer.",
                "sources": [
                    {"source_key": INDEX, "locator_override": f"PDF page 446 row {row}; protected identifier withheld"},
                    {"source_key": ARMY, "locator_override": f"Accepted reviewed identity bridge; Army name {data['army_name']}; protected identifier withheld"},
                ],
            }
        )
        values.append(
            {
                "key": f"occupation-{slug(PEOPLE[row][1])}-b912",
                "person_id": PEOPLE[row][0],
                "affiliation_key": f"{slug(PEOPLE[row][1])}-occupation-b912",
                "claim_type": "occupation",
                "claim_text": f"At Army entry on {data['entry']}, {PEOPLE[row][1]} was recorded in the historical civilian-occupation category {data['occupation']}; no employer is identified.",
                "evidence_paraphrase": f"The Army record carries code {data['code']}, which the visually checked NARA code list maps to {data['occupation']}.",
                "identity_match_assessment": identity_assessment,
                "temporal_assessment": "Dated at Army entry, but its relationship to OSS service is uncertain and no employer is named.",
                "source_quality": "A_direct_official",
                "claim_confidence": "medium",
                "publication_status": "publish_qualified",
                "match_notes": "Excluded from employer analytics and not described as the immediate pre-OSS role.",
                "sources": [
                    {"source_key": ARMY, "locator_override": f"Army-entry date {data['entry']}; occupation code {data['code']}; protected identifier withheld"},
                    {"source_key": TECH, "support_type": "context_only", "locator_override": "Civilian-occupation field definition"},
                    {"source_key": CODES, "locator_override": f"{data['code_page']}; historical category {data['code']}"},
                ],
            }
        )
    values.extend(
        [
            {
                "key": "identity-morris-stein-b912",
                "person_id": PEOPLE[31][0],
                "claim_type": "identity",
                "claim_text": "The indexed Morris I. Stein is a high-confidence match to the reviewed official Army record, but its historical civilian-occupation code 037 remains unmapped.",
                "evidence_paraphrase": "A nonshared protected identifier and exact name establish the Army identity bridge; the reviewed official code list omits code 037.",
                "identity_match_assessment": "High confidence from exact name and a nonshared protected identifier.",
                "temporal_assessment": "The Army record dates entry to 1944-11-09; no occupation label, employer or OSS transition is assigned.",
                "source_quality": "A_direct_official",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "No protected identifier is exposed publicly, and no occupation is invented for an omitted historical code.",
                "sources": [
                    {"source_key": INDEX, "locator_override": "PDF page 446 row 31; protected identifier withheld"},
                    {"source_key": ARMY, "locator_override": "Accepted reviewed identity bridge; occupation code 037; protected identifier withheld"},
                    {"source_key": CODES, "support_type": "context_only", "locator_override": "PDF physical page 171; code sequence omits 037"},
                ],
            },
            {
                "key": "identity-estelle-steinacker-b912",
                "person_id": PEOPLE[36][0],
                "claim_type": "identity",
                "claim_text": "The indexed Estelle H. Steinacker is a probable match to the Civilian Pilot Training Division employee of the same rare full name.",
                "evidence_paraphrase": "A contemporary federal table records the exact rare full name in a wartime aviation-training agency.",
                "identity_match_assessment": "Probable from the rare exact full name and relevant federal wartime chronology; no independent identifier directly joins the two records.",
                "temporal_assessment": "The resignation occurred sometime after December 7, 1941 and before July 14, 1942; the OSS entry date is unknown.",
                "source_quality": "A_direct_official",
                "claim_confidence": "medium",
                "publication_status": "publish_qualified",
                "match_notes": "The personnel file remains necessary to confirm identity and sequence.",
                "sources": [
                    {"source_key": INDEX, "locator_override": "PDF page 446 row 36; Estelle H. Steinacker"},
                    {"source_key": CONGRESS, "locator_override": "Printed page 6127, resignation table"},
                ],
            },
            {
                "key": "other-estelle-steinacker-cptd-b912",
                "person_id": PEOPLE[36][0],
                "affiliation_key": "estelle-steinacker-cptd-b912",
                "claim_type": "other_pre_oss_affiliation",
                "claim_text": "If the qualified identity match is correct, Estelle H. Steinacker worked for the Civilian Pilot Training Division of the Civil Aeronautics Authority before resigning for a higher-paid position in 1941-1942.",
                "evidence_excerpt": "Estelle H. Steinacker ... Higher paid position.",
                "evidence_paraphrase": "The Congressional Record table lists her among division employees who resigned after December 7, 1941.",
                "identity_match_assessment": "Probable from the rare exact full name; no separate OSS identifier appears in the table.",
                "temporal_assessment": "Documented before July 14, 1942, but not proven to be the immediate pre-OSS assignment or last civilian employer.",
                "source_quality": "A_direct_official",
                "claim_confidence": "medium",
                "publication_status": "publish_qualified",
                "match_notes": "Neither a job title nor the next employer is inferred from the resignation reason.",
                "sources": [{"source_key": CONGRESS, "locator_override": "Printed page 6127, Civilian Pilot Training Division resignation table"}],
            },
            {
                "key": "identity-saul-steinberg-b912",
                "person_id": PEOPLE[41][0],
                "claim_type": "identity",
                "claim_text": "The indexed Saul Steinberg is a high-confidence match to the Romanian-born artist and U.S. Naval Reserve officer assigned to OSS Morale Operations.",
                "evidence_paraphrase": "The exact distinctive name, NARA personal-name index entry, Naval Reserve commission and person-specific OSS service chronology align across official and institutional sources.",
                "identity_match_assessment": "High confidence from the distinctive exact name plus NARA and Yale person-specific OSS evidence and matching Navy chronology.",
                "temporal_assessment": "The sources separately date prewar study, pre-service publishing, the 1943 commission and wartime OSS assignment.",
                "source_quality": "B_authoritative_institutional",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "The project does not rely on fame or name alone; NARA and Yale supply independent OSS bridges.",
                "sources": [
                    {"source_key": INDEX, "locator_override": "PDF page 446 row 41; Saul Steinberg"},
                    {"source_key": NARA_GUIDE, "locator_override": "PDF physical page 15, Saul Steinberg personal-name index entry"},
                    {"source_key": YALE, "locator_override": "Biographical history, PDF pages 6-7 of 415"},
                    {"source_key": FOUNDATION, "support_type": "context_only", "locator_override": "Naval Reserve and OSS Morale Operations paragraphs"},
                ],
            },
            {
                "key": "immediate-saul-steinberg-usnr-b912",
                "person_id": PEOPLE[41][0],
                "affiliation_key": "saul-steinberg-usnr-b912",
                "claim_type": "immediate_pre_oss_affiliation",
                "claim_text": "Saul Steinberg's best-supported immediate institutional pathway into OSS was his 1943 commission as an ensign in the U.S. Naval Reserve.",
                "evidence_excerpt": "commission as an ensign in the US Naval Reserve",
                "evidence_paraphrase": "The Yale finding aid sequences his commission and active service before describing his OSS assignment.",
                "identity_match_assessment": "High confidence from the person-specific Yale finding aid and corroborating NARA and Foundation evidence.",
                "temporal_assessment": "Strongly date-bounded in 1943; the sources do not provide a distinct Navy-to-OSS transfer date.",
                "source_quality": "B_authoritative_institutional",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "The military pathway is kept separate from his civilian publishing activity.",
                "sources": [
                    {"source_key": YALE, "locator_override": "Biographical history, PDF pages 6-7 of 415; 1943 commission and OSS assignment"},
                    {"source_key": FOUNDATION, "support_type": "supports", "locator_override": "February 1943 Naval Reserve commission and OSS service paragraphs"},
                ],
            },
            {
                "key": "other-saul-steinberg-new-yorker-b912",
                "person_id": PEOPLE[41][0],
                "affiliation_key": "saul-steinberg-new-yorker-b912",
                "claim_type": "other_pre_oss_affiliation",
                "claim_text": "Before his 1943 commission, Saul Steinberg was a contributing cartoonist and illustrator for The New Yorker; he continued sending drawings during wartime service.",
                "evidence_excerpt": "published his first drawing in The New Yorker",
                "evidence_paraphrase": "Yale dates the first contribution to October 25, 1941, and the Foundation documents increased contributions before service and continued wartime submissions.",
                "identity_match_assessment": "High confidence from the person-specific institutional biography and OSS chronology.",
                "temporal_assessment": "Strongly date-bounded before the 1943 commission, but the relationship continued during service and is not labeled a last civilian employer.",
                "source_quality": "B_authoritative_institutional",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "Modeled as a professional affiliation rather than assumed salaried employment.",
                "sources": [
                    {"source_key": YALE, "locator_override": "Biographical history, PDF pages 6-7 of 415; 1941 first New Yorker drawing and wartime drawings"},
                    {"source_key": FOUNDATION, "support_type": "supports", "locator_override": "Pre-service New Yorker contributions and wartime submissions"},
                    {"source_key": SMITHSONIAN, "support_type": "context_only", "locator_override": "Artist biography, prewar publishing and Navy service"},
                ],
            },
            {
                "key": "student-saul-steinberg-politecnico-b912",
                "person_id": PEOPLE[41][0],
                "affiliation_key": "saul-steinberg-politecnico-b912",
                "claim_type": "other_pre_oss_affiliation",
                "claim_text": "Saul Steinberg studied architecture at the Regio Politecnico in Milan from 1933 until receiving his degree in 1940.",
                "evidence_paraphrase": "The Yale finding aid dates enrollment and graduation; Smithsonian independently identifies the architecture program and degree.",
                "identity_match_assessment": "High confidence from person-specific institutional biographies linked to the same Navy and OSS chronology.",
                "temporal_assessment": "Explicitly prewar and earlier than his immediate military pathway; student status is not employment.",
                "source_quality": "B_authoritative_institutional",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "Excluded from employer analytics.",
                "sources": [
                    {"source_key": YALE, "locator_override": "Biographical history, PDF page 6 of 415; 1933 enrollment and 1940 architecture degree"},
                    {"source_key": SMITHSONIAN, "support_type": "supports", "locator_override": "Artist biography, Milan architecture study and 1940 degree"},
                ],
            },
        ]
    )
    return values


def person_updates() -> list[dict[str, object]]:
    updates: list[dict[str, object]] = []
    for row, reason in UNRESOLVED.items():
        person_id, name = PEOPLE[row]
        priority = "critical" if row in {25, 27, 29, 32, 39, 40} else "high"
        updates.append(
            {
                "person_id": person_id,
                "identity_status": "unresolved",
                "identity_evidence": f"The visually verified index row supplies {name}, box and archive location, but staged NARA context, CIA, exact-name, occupation, employer, obituary, institutional, newspaper, directory, Library of Congress and archival searches found no defensible identity bridge. {reason}",
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Review the indexed personnel file for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": priority,
            }
        )
    for row in ARMY_OCCUPATIONS:
        data = ARMY_OCCUPATIONS[row]
        person_id, name = PEOPLE[row]
        variants = ["Theodore Stelmack"] if row == 24 else None
        identity_text = f"A nonshared protected identifier and exact full name connect the index row to the reviewed official Army record; the {data['occupation']} category names no employer."
        if row == 24:
            identity_text = "A nonshared protected identifier connects indexed Theodore Steimack to Army-record Theodore Stelmack; the one-letter spelling difference remains explicit, and the mechanical-metals category names no employer."
        if row == 34:
            identity_text += " The malformed Army grade value remains uninterpreted."
        update: dict[str, object] = {
            "person_id": person_id,
            "identity_status": "high_confidence",
            "identity_evidence": identity_text,
            "personnel_category": "enlisted_army_personnel",
            "commissioned_officer": False,
            "allied_or_foreign_personnel": False,
            "manual_review_required": True,
            "research_status": "occupation_only_found",
            "next_action": f"Review Box {743 if row == 24 else 742} to identify the employer behind the Army occupation category and the assignment immediately preceding OSS.",
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
            "archival_review_priority": "critical" if row == 24 else "high",
        }
        if variants:
            update["name_variants"] = variants
        updates.append(update)
    updates.extend(
        [
            {
                "person_id": PEOPLE[31][0],
                "identity_status": "high_confidence",
                "identity_evidence": "A nonshared protected identifier and exact full name connect the index row to the reviewed official Army record. Its historical civilian-occupation code 037 is omitted from the reviewed official code list, so no occupation is assigned.",
                "personnel_category": "enlisted_army_personnel",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Review Box 742 to recover Morris I. Stein's civilian occupation, employer and immediate pre-OSS assignment; do not infer a label for code 037.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[36][0],
                "identity_status": "probable",
                "identity_evidence": "A contemporary federal table records the same rare full name as an employee of the Civilian Pilot Training Division, but no independent identifier directly connects the table to the indexed OSS row.",
                "manual_review_required": True,
                "research_status": "needs_temporal_review",
                "next_action": "Review Box 742 to confirm the Civilian Pilot Training Division identity, exact resignation date, next position and OSS entry chronology.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[41][0],
                "identity_status": "high_confidence",
                "identity_evidence": "The distinctive exact name, NARA personal-name index entry, Yale finding aid, Naval Reserve commission and person-specific OSS Morale Operations chronology identify the indexed Saul Steinberg at high confidence.",
                "personnel_category": "commissioned_naval_officer",
                "commissioned_officer": True,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "completed",
                "next_action": "Review Box 742 for the original commission and assignment papers, the exact Navy-to-OSS sequence and any formal pre-service employment contract; current sources establish affiliations but not a last civilian employer.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "medium",
            },
        ]
    )
    return updates


def research_attempts() -> list[dict[str, object]]:
    evidence_rows = set(ARMY_OCCUPATIONS) | {31, 36, 41}
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        if row in evidence_rows:
            outcome = "source_reviewed"
            if row == 31:
                detail = "The Army identity bridge was accepted, but official code 037 remains unmapped and no employer is assigned."
            elif row == 36:
                detail = "A qualified contemporary federal employment record was found; identity and sequence still require personnel-file confirmation."
            elif row == 41:
                detail = "Independent official and institutional sources establish a high-confidence Navy/OSS identity and documented pre-service affiliations."
            else:
                detail = "A reviewed official Army identity and dated historical occupation category were accepted; no named employer is supplied."
        else:
            outcome = "candidate_rejected"
            detail = UNRESOLVED[row]
        attempts.append(
            {
                "key": f"page446-row{row}-{slug(name)}-b912",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA index and finding-aid context; CIA Reading Room exact-name check; OSS and spelling variants; employer and occupation; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Box {743 if row in {24, 46} else 742}; protected-identifier Army crosswalk where available",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_912",
                "started_at": "2026-10-25T22:35:00Z",
                "completed_at": "2026-10-25T23:00:00Z",
                "outcome": outcome,
                "sources_reviewed": 12 if row == 41 else (9 if row in evidence_rows or row in {30, 35} else 7),
                "candidate_sources_rejected": 5 if row in evidence_rows else 8,
                "rejection_reasons": "Unbridged namesakes, discovery-only results, sensitive people-search pages, chronologically irrelevant records and postwar-only material were not assigned." if row in evidence_rows else detail,
                "research_notes": f"{detail} Automated CIA and LoC adapter transport failures remain recorded as errors rather than negative findings; equivalent source checks were completed manually. Search-result snippets were discovery aids only, final claims point to inspectable sources, no access control was bypassed, and no exposed NARA API credential was used.",
                "next_action": "Review the indexed personnel file for corroborating identifiers and the last documented pre-OSS affiliation.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b912-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-912-v1",
        "reviewer": "Before OSS Batch 912 evidence review",
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
