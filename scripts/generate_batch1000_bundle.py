#!/usr/bin/env python3
"""Generate the reviewed Batch 1000 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / "research/evidence-page490-ward-to-warfield-review_batch-1000_2026-11-03.json"

INDEX = "nara-index-b1000"
ARMY = "army-bulk-b1000"
TECH = "army-tech-b1000"
CODES = "army-codes-b1000"
LIVING_CHURCH = "living-church-paul-ward-b1000"
VAUMC = "vaumc-warfield-b1000"
CIA_FOIA = "cia-foia-wardrop-b1000"
PRINCETON = "princeton-wardrop-b1000"
EDGEWORTH = "edgeworth-wardrop-b1000"

PEOPLE = {
    24: ("8dbec3ac-780d-537e-b275-15eb457ebb1a", "Betty Lou Ward"),
    25: ("acf77d4c-cdde-5187-8840-c018ac689b1d", "Charles D Ward"),
    26: ("b5f31ff9-2798-59f1-aa28-1999599622cc", "Francis R Ward"),
    27: ("3bb338fc-74b8-5158-85cb-446b5997af69", "Hugh C Ward Jr."),
    28: ("00d4faca-822d-50e9-a3be-749c7bf0370a", "James R Ward"),
    29: ("9687c2b9-417a-5123-adb8-3a1f90046c95", "Jean E Ward"),
    30: ("733e8b24-040a-5e54-8d01-7c63ec5c1bed", "Kathryn Ward"),
    31: ("e6847ed1-5bf3-510d-8713-3f67c0025b77", "Luther B Ward"),
    32: ("1fc82c30-5734-5011-83e3-04d47578ec25", "M. Eugene Ward"),
    33: ("5dcf386e-3a45-5ba9-97aa-76eaf81a9a43", "Mabel T Ward"),
    34: ("0047c86d-d525-502b-b9af-dfd5ce252870", "Malcolm C Ward"),
    35: ("7b7a2502-afcd-5d38-919e-f14455be282e", "Mary B Ward"),
    36: ("b9fc6164-4765-52dc-bd65-9422318bca73", "Paul L Ward"),
    37: ("4cdfb92a-831d-51d6-a6e3-c0223f07ed5b", "Philip S Ward"),
    38: ("778665c4-757e-598a-bbe3-e4bc98ddadf2", "Robert L Ward"),
    39: ("03030a9c-ebef-5dd2-8ddd-a9f7709d36e6", "Thomas N Ward"),
    40: ("7ab1af89-8ef5-58b1-a40f-437f78e56126", "Edythe C Warden"),
    41: ("c808443d-d646-5233-8851-7017c717ed80", "Philip Wardner"),
    42: ("2ce5dcd0-29f7-52f6-ada6-fae6349d8d6b", "Edmund D Wardrop"),
    43: ("0c292d66-d569-56d6-981a-02988e793fe5", "Tom Karr Ware Jr."),
    44: ("b88028d0-754f-5590-8a00-bb9a9aab0f70", "Roscoe H Wareham"),
    45: ("c945176d-c547-5ce4-8c54-c397ce14b890", "Peter P Warenzak"),
    46: ("3d88483a-88a7-5d92-b263-b8a0ee44cf0d", "Gaither P Warfield"),
}

ARMY_OCCUPATIONS = {
    25: {
        "date": "1942-07-29", "grade": "Private", "code": "902",
        "occupation": "automobile-manufacturing occupation, not elsewhere classified",
        "label": "Occupations in manufacture of automobiles, n.e.c.",
        "locator": "PDF physical page 174; historical category 9-02",
        "relationship": "unknown",
    },
    27: {
        "date": "1943-02-25", "grade": "Private", "code": "002",
        "occupation": "actor",
        "label": "Actors and actresses",
        "locator": "PDF physical page 170; historical category 0-02",
        "relationship": "unknown",
    },
    31: {
        "date": "1944-07-24", "grade": "Private", "code": "992",
        "occupation": "student",
        "label": "Students",
        "locator": "PDF physical page 304; historical category 9-92",
        "relationship": "student",
    },
    37: {
        "date": "1942-11-07", "grade": "Private", "code": "992",
        "occupation": "student",
        "label": "Students",
        "locator": "PDF physical page 304; historical category 9-92",
        "relationship": "student",
    },
    38: {
        "date": "1942-08-07", "grade": "damaged grade text", "code": "145",
        "occupation": "weigher",
        "label": "Weighers",
        "locator": "PDF physical page 171; historical category 1-45",
        "relationship": "unknown",
    },
    44: {
        "date": "1942-04-15", "grade": "Private", "code": "497",
        "occupation": "electrician",
        "label": "Electricians",
        "locator": "PDF physical page 174; historical category 4-97",
        "relationship": "unknown",
    },
    45: {
        "date": "1943-05-07", "grade": "Private", "code": "963",
        "occupation": "nonprocess manufacturing occupation, not elsewhere classified",
        "label": "Unskilled and nonprocess occupations in manufacturing, n.e.c.",
        "locator": "PDF physical page 174; historical category 9-63",
        "relationship": "unknown",
    },
}

UNRESOLVED = {
    24: "Exact-name, OSS, employer, occupation, obituary, newspaper, institutional, and archival searches produced no reliable identity bridge.",
    26: "Common-name results supplied no protected identifier, OSS assignment, employer chronology, or Box 816 personnel-file bridge.",
    28: "A later article citation names a James R. Ward as author of a Detachment 101 history, but it supplies no middle name, rank, service identifier, hometown, or other bridge to the indexed lieutenant.",
    30: "Exact-name and variant searches produced only unbridged namesakes and no reliable employment chronology.",
    32: "Initial, expanded-name, OSS, employer, occupation, obituary, and archival searches produced no reliable identity bridge.",
    33: "Exact-name, newspaper, obituary, institutional, and archival searches produced no source tied to the indexed Box 816 record.",
    34: "Common-name results supplied no corroborating OSS assignment, service identifier, employer chronology, or Box 816 bridge.",
    35: "Common-name results supplied no corroborating OSS assignment, service identifier, employer chronology, or Box 816 bridge.",
    39: "Common-name results supplied no corroborating OSS assignment, service identifier, employer chronology, or Box 816 bridge.",
    40: "Exact-name and meaningful-variant searches produced no reliable OSS, employer, occupation, or personnel-file bridge.",
    41: "Postwar Garden City High School references identify a teacher with this name but supply no prewar date, OSS assignment, or Box 816 bridge, so they were rejected for pre-OSS claims.",
    43: "Exact-name, suffix-variant, OSS, employer, occupation, obituary, institutional, and archival searches produced no reliable identity bridge.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Box 816",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 490, rows 24-46; checked against layout-preserving text and an original-detail page render",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. Printed ranks and blank rank cells are preserved literally. Protected identifiers remain private.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; seven accepted and one conflicting protected-identifier comparison; identifiers and record ordinals withheld",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "Seven exact-name bridges were accepted after private review. The Jean E Ward candidate is withheld because the Army record says John Ward. No Army record is treated as a named employer or direct OSS-transfer record.",
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
            "locator": "PDF physical pages 170-171, 174, and 304; historical civilian-occupation categories 0-02, 1-45, 4-97, 9-02, 9-63, and 9-92",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical categories identify broad occupations or student status, not named employers, institutions, workplaces, or exact OSS-transfer dates.",
        },
        {
            "key": LIVING_CHURCH,
            "stable_url": "https://d7u3dh9x9blzp.cloudfront.net/1945/6.24.1945.pdf",
            "archival_identifier": "The Living Church, volume CX, number 25",
            "title": "Paul L. Ward to Serve in China",
            "author_creator": "The Living Church",
            "repository_publisher": "Morehouse-Gorham Co.",
            "publication_record_date": "1945-06-24",
            "locator": "PDF physical pages 5-6",
            "access_date": "2026-11-03",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "The Living Church",
            "rights_notes": "The contemporary notice explicitly places Ward with OSS in Washington and lists earlier teaching experience, but gives no dates or exact sequence among the three institutions.",
        },
        {
            "key": VAUMC,
            "stable_url": "https://doc.vaumc.org/Memoirs/UMCPastorMemoirs_1987-2017_2Sep17.pdf",
            "archival_identifier": "1987 Annual Conference memoir, pages 7-8",
            "title": "Gaither P. Warfield, 1896-1986",
            "author_creator": "Kenneth E. Colton",
            "repository_publisher": "Virginia United Methodist Conference",
            "publication_record_date": "1987",
            "locator": "PDF physical pages 7-8",
            "access_date": "2026-11-03",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Virginia Conference clergy memoirs",
            "rights_notes": "The institutional memoir supplies a distinctive full-name biography and dated church-service chronology but does not explain how that chronology intersects the indexed OSS file.",
        },
        {
            "key": CIA_FOIA,
            "stable_url": "https://www.cia.gov/readingroom/docs/FOIA%20CASE%20LOG%20CALENDER%20YE%5B16111550%5D.pdf",
            "archival_identifier": "CIA FOIA case log, calendar years 2001-2003; release C06935701",
            "title": "FOIA Case Log, Calendar Years 2001-2003",
            "author_creator": "Central Intelligence Agency",
            "repository_publisher": "CIA FOIA Electronic Reading Room",
            "publication_record_date": "Approved for release 2022-08-23",
            "locator": "Entry naming Edmund Donnan Wardrop; request context only",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "CIA FOIA case logs",
            "rights_notes": "A FOIA request subject is not evidence of CIA or OSS employment, a responsive record, or the request's disposition. It is used only as name context.",
        },
        {
            "key": PRINCETON,
            "stable_url": "https://paw.princeton.edu/memorial/robert-wardrop-ii-35",
            "title": "Robert Wardrop II '35",
            "author_creator": "The Class of 1935",
            "repository_publisher": "Princeton Alumni Weekly",
            "locator": "Memorial identifies brother Edmund D. Wardrop '34 and his 1963 death",
            "access_date": "2026-11-03",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Princeton Alumni Weekly memorials",
            "rights_notes": "Used for a qualified student-affiliation and identity lead only; it does not mention OSS or employment for Edmund Wardrop.",
        },
        {
            "key": EDGEWORTH,
            "stable_url": "https://www.hmdb.org/m.asp?m=247062",
            "archival_identifier": "Edgeworth World War II Honor Roll, erected 1946",
            "title": "Edgeworth World War II Honor Roll",
            "author_creator": "Citizens of Edgeworth, Pennsylvania",
            "repository_publisher": "Historical Marker Database",
            "publication_record_date": "1946; photographed 2024-05-19",
            "locator": "Honor-roll inscription naming Edmund D. Wardrop",
            "access_date": "2026-11-03",
            "source_quality": "D_correlative_or_secondary",
            "rights_notes": "A modern photographic transcription of a 1946 civic honor roll. It supports World War II service context but supplies no rank, unit, employer, or OSS assignment.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": "harvard-b1000",
            "organization_id": "45ddf347-21c6-59f5-a8ae-517418adf941",
            "canonical_name": "Harvard University", "historical_name": "Harvard University",
            "organization_type": "university", "sector": "academia_and_research",
            "city": "Cambridge", "state_or_region": "Massachusetts", "country": "United States",
            "normalization_notes": "Existing canonical organization reused; Ward's Society of Fellows research is noted in the evidence but not converted into a separate employer claim.",
        },
        {
            "key": "radcliffe-b1000",
            "organization_id": "8b718239-988a-55f0-a231-decd01eb0642",
            "canonical_name": "Radcliffe College", "historical_name": "Radcliffe College",
            "organization_type": "college", "sector": "academia_and_research",
            "city": "Cambridge", "state_or_region": "Massachusetts", "country": "United States",
            "normalization_notes": "Preserved separately from Harvard because the contemporary source names both institutions.",
        },
        {
            "key": "russell-sage-b1000",
            "canonical_name": "Russell Sage College", "historical_name": "Russell Sage College",
            "organization_type": "college", "sector": "academia_and_research",
            "city": "Troy", "state_or_region": "New York", "country": "United States",
            "normalization_notes": "Historical institutional name preserved as printed in the 1945 source.",
        },
        {
            "key": "methodist-mission-poland-b1000",
            "canonical_name": "Methodist mission in Poland", "historical_name": "Methodist mission in Poland",
            "aliases": ["Methodist work in Poland"],
            "organization_type": "religious mission", "sector": "labor_nonprofit_and_religion",
            "country": "Poland", "active_dates": "1924-1942",
            "normalization_notes": "A descriptive historical entity is used because the memoir says Warfield was appointed to Poland but does not name a single employing corporation.",
        },
        {
            "key": "methodist-board-missions-b1000",
            "canonical_name": "Board of Missions of the Methodist Church",
            "historical_name": "Board of Missions of the Methodist Church",
            "organization_type": "church mission board", "sector": "labor_nonprofit_and_religion",
            "country": "United States", "active_dates": "1939-1968",
            "normalization_notes": "Historical name preserved exactly; no modern successor is substituted.",
        },
        {
            "key": "princeton-b1000",
            "organization_id": "ad6bb38c-850a-50e4-b092-d33163c93875",
            "canonical_name": "Princeton University", "historical_name": "Princeton University",
            "organization_type": "university", "sector": "academia_and_research",
            "city": "Princeton", "state_or_region": "New Jersey", "country": "United States",
            "normalization_notes": "Existing canonical organization reused. Class-year evidence is modeled as student status, never employment.",
        },
    ]


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, item in ARMY_OCCUPATIONS.items():
        values.append({
            "key": f"{slug(PEOPLE[row][1])}-army-occupation-b1000",
            "person_id": PEOPLE[row][0], "occupation": item["occupation"],
            "relationship_type": item["relationship"], "end_date": item["date"],
            "date_precision": f"Historical civilian-occupation code {item['code']} was recorded at Army entry on {item['date']}; no named employer, institution, workplace, or exact OSS-transfer date is supplied.",
            "country": "United States", "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "confirmed", "claim_confidence": "medium",
            "source_quality": "A_direct_official", "publication_status": "publish_qualified",
            "research_notes": "Broad historical occupation category or student status only; no named employer, school, or workplace is inferred.",
        })
    values.extend([
        {
            "key": "paul-l-ward-harvard-b1000", "person_id": PEOPLE[36][0],
            "organization_key": "harvard-b1000", "organization_name_as_found": "Harvard",
            "role_title": "instructor and tutor in history", "occupation": "history teacher",
            "relationship_type": "employment", "date_precision": "The 24 June 1945 source lists this among Ward's prior experience but supplies no dates or order.",
            "city": "Cambridge", "state_or_region": "Massachusetts", "country": "United States",
            "immediate_pre_oss": False, "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "high_confidence",
            "claim_confidence": "medium", "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "publish_qualified", "research_notes": "Documented earlier employment; not proven immediate and not designated the last civilian employer.",
        },
        {
            "key": "paul-l-ward-radcliffe-b1000", "person_id": PEOPLE[36][0],
            "organization_key": "radcliffe-b1000", "organization_name_as_found": "Radcliffe",
            "role_title": "instructor and tutor in history", "occupation": "history teacher",
            "relationship_type": "employment", "date_precision": "The 24 June 1945 source lists this among Ward's prior experience but supplies no dates or order.",
            "city": "Cambridge", "state_or_region": "Massachusetts", "country": "United States",
            "immediate_pre_oss": False, "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "high_confidence",
            "claim_confidence": "medium", "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "publish_qualified", "research_notes": "Documented earlier employment; not proven immediate and not designated the last civilian employer.",
        },
        {
            "key": "paul-l-ward-russell-sage-b1000", "person_id": PEOPLE[36][0],
            "organization_key": "russell-sage-b1000", "organization_name_as_found": "Russell Sage College",
            "role_title": "assistant professor of history", "occupation": "history professor",
            "relationship_type": "employment", "date_precision": "The 24 June 1945 source lists this among Ward's prior experience but supplies no dates or order.",
            "city": "Troy", "state_or_region": "New York", "country": "United States",
            "immediate_pre_oss": False, "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "high_confidence",
            "claim_confidence": "medium", "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "publish_qualified", "research_notes": "Documented earlier employment; not proven immediate and not designated the last civilian employer.",
        },
        {
            "key": "edmund-d-wardrop-princeton-b1000", "person_id": PEOPLE[42][0],
            "organization_key": "princeton-b1000", "organization_name_as_found": "Princeton",
            "role_title": "Class of 1934", "relationship_type": "student", "end_date": "1934",
            "date_precision": "Class year only; degree completion is not separately established in the accessible source.",
            "city": "Princeton", "state_or_region": "New Jersey", "country": "United States",
            "immediate_pre_oss": False, "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "probable",
            "claim_confidence": "medium", "source_quality": "B_authoritative_institutional",
            "publication_status": "publish_qualified", "research_notes": "Student affiliation only, never an employer claim. The Box 816 file is still needed for direct identity confirmation.",
        },
        {
            "key": "gaither-warfield-poland-b1000", "person_id": PEOPLE[46][0],
            "organization_key": "methodist-mission-poland-b1000", "organization_name_as_found": "appointed to Poland",
            "role_title": "Methodist missionary", "occupation": "minister and missionary",
            "relationship_type": "professional_affiliation", "start_date": "1924", "end_date": "1942",
            "date_precision": "The institutional memoir dates the appointment to 1924, describes eighteen years of service, and dates repatriation to 1942.",
            "country": "Poland", "immediate_pre_oss": False, "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "high_confidence",
            "claim_confidence": "high", "source_quality": "B_authoritative_institutional",
            "publication_status": "published", "research_notes": "Documented prewar professional affiliation; the source does not establish an OSS transition or a conventional employer relationship.",
        },
        {
            "key": "gaither-warfield-board-missions-b1000", "person_id": PEOPLE[46][0],
            "organization_key": "methodist-board-missions-b1000", "organization_name_as_found": "Board of Missions of the Methodist Church",
            "role_title": "served the Board of Missions", "occupation": "minister and mission-board worker",
            "relationship_type": "professional_affiliation", "start_date": "1942", "end_date": "1946",
            "date_precision": "The memoir says he served the Board after returning to the United States in 1942 and until 1946.",
            "country": "United States", "immediate_pre_oss": False, "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "temporal_relation_uncertain", "identity_confidence": "high_confidence",
            "claim_confidence": "medium", "source_quality": "B_authoritative_institutional",
            "publication_status": "publish_qualified", "research_notes": "Wartime affiliation overlaps the likely indexed period, but the accessible source does not explain whether, when, or how OSS service intersected it.",
        },
    ])
    return values


def make_claim(*, key: str, row: int, claim_type: str, text: str, paraphrase: str,
               identity: str, temporal: str, quality: str, confidence: str,
               publication: str, notes: str, source_links: list[dict[str, str]],
               affiliation_key: str | None = None) -> dict[str, object]:
    value: dict[str, object] = {
        "key": key, "person_id": PEOPLE[row][0], "claim_type": claim_type,
        "claim_text": text, "evidence_paraphrase": paraphrase,
        "identity_match_assessment": identity, "temporal_assessment": temporal,
        "source_quality": quality, "claim_confidence": confidence,
        "publication_status": publication, "match_notes": notes, "sources": source_links,
    }
    if affiliation_key:
        value["affiliation_key"] = affiliation_key
    return value


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, item in ARMY_OCCUPATIONS.items():
        name = PEOPLE[row][1]
        values.extend([
            make_claim(
                key=f"identity-{slug(name)}-b1000", row=row, claim_type="identity",
                text=f"Indexed {name} is confirmed as the reviewed official Army entry record.",
                paraphrase="The exact names agree, and a nonshared protected identifier connects the records.",
                identity="Confirmed by exact name and a nonshared protected-identifier agreement; the identifier and record ordinal remain private.",
                temporal=f"The Army record dates entry to {item['date']} and records grade as {item['grade']}.",
                quality="A_direct_official", confidence="confirmed", publication="published",
                notes="Identity only; no named employer or direct Army-to-OSS sequence is inferred.",
                source_links=[
                    {"source_key": INDEX, "locator_override": f"PDF page 490 row {row}; protected identifier withheld"},
                    {"source_key": ARMY, "locator_override": "Accepted reviewed identity bridge; protected identifier withheld"},
                ],
            ),
            make_claim(
                key=f"occupation-{slug(name)}-b1000", row=row, claim_type="occupation",
                text=f"At Army entry on {item['date']}, {name} was recorded in the historical {item['occupation']} category; no named employer or institution is identified.",
                paraphrase=f"The accepted Army record carries civilian-occupation code {item['code']}, decoded from NARA's official code list.",
                identity="The category belongs only to the confirmed protected-identifier match; the identifier itself is not public.",
                temporal="Strongly date-bounded to Army entry; it does not establish the immediate pre-OSS affiliation or a named employer.",
                quality="A_direct_official", confidence="medium", publication="publish_qualified",
                notes="Published with its limits and excluded from verified-employer analytics.",
                source_links=[
                    {"source_key": ARMY, "locator_override": f"Army entry {item['date']}; civilian occupation code {item['code']}; protected identifier withheld"},
                    {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46"},
                    {"source_key": CODES, "locator_override": item["locator"], "excerpt_override": item["label"]},
                ], affiliation_key=f"{slug(name)}-army-occupation-b1000",
            ),
        ])
    values.extend([
        make_claim(
            key="conflict-jean-e-ward-b1000", row=29, claim_type="identity",
            text="The protected identifier candidate for Jean E Ward names John Ward in the official Army record, so the candidate is conflicting and no evidence is transferred.",
            paraphrase="Private comparison found a protected-identifier collision with a materially different given name.",
            identity="Conflicting: Jean and John are materially different indexed and Army names, and no direct personnel-file evidence establishes that they are the same person.",
            temporal="No chronology, grade, or occupation is transferred while identity remains conflicting.",
            quality="A_direct_official", confidence="conflicting", publication="conflicting",
            notes="The conflict remains visible without exposing the protected identifier, Army record ordinal, or unrelated biography.",
            source_links=[
                {"source_key": INDEX, "locator_override": "PDF page 490 row 29; protected identifier withheld"},
                {"source_key": ARMY, "locator_override": "Conflicting reviewed candidate naming John Ward; protected identifier withheld"},
            ],
        ),
        make_claim(
            key="identity-paul-l-ward-b1000", row=36, claim_type="identity",
            text="The indexed Paul L Ward is a high-confidence match to the historian whom a June 1945 contemporary notice places with OSS in Washington.",
            paraphrase="The exact name and middle initial, current OSS affiliation, Washington location, academic field, and Ph.D. profile align.",
            identity="High confidence from exact name and middle initial plus explicit current OSS service, location, profession, age, and educational profile.",
            temporal="The source is dated 24 June 1945 and distinguishes current OSS service from earlier teaching experience.",
            quality="C_reputable_contemporary_or_scholarly", confidence="high", publication="published",
            notes="The exact Box 816 personnel file remains the direct archival confirmation target.",
            source_links=[
                {"source_key": INDEX, "locator_override": "PDF page 490 row 36; Box 816"},
                {"source_key": LIVING_CHURCH, "locator_override": "PDF physical page 5", "excerpt_override": "At present Dr. Ward is with the Office of Strategic Services in Washington"},
            ],
        ),
        make_claim(
            key="employment-paul-l-ward-harvard-b1000", row=36, claim_type="other_pre_oss_affiliation",
            text="Paul L Ward had earlier worked as an instructor and tutor in history at Harvard University.",
            paraphrase="The contemporary notice lists Harvard instruction and tutoring among Ward's experience before describing his current OSS role.",
            identity="High-confidence identity from the same exact-name contemporary profile that explicitly places him with OSS.",
            temporal="Documented earlier than the 24 June 1945 notice, but no dates, ordering, or immediate-predecessor status are supplied.",
            quality="C_reputable_contemporary_or_scholarly", confidence="medium", publication="publish_qualified",
            notes="Earlier employment only; not marked immediate or last civilian employer.",
            source_links=[{"source_key": LIVING_CHURCH, "locator_override": "PDF physical pages 5-6", "excerpt_override": "instructor and tutor in history at Harvard and Radcliffe"}],
            affiliation_key="paul-l-ward-harvard-b1000",
        ),
        make_claim(
            key="employment-paul-l-ward-radcliffe-b1000", row=36, claim_type="other_pre_oss_affiliation",
            text="Paul L Ward had earlier worked as an instructor and tutor in history at Radcliffe College.",
            paraphrase="The contemporary notice lists Radcliffe instruction and tutoring among Ward's experience before describing his current OSS role.",
            identity="High-confidence identity from the same exact-name contemporary profile that explicitly places him with OSS.",
            temporal="Documented earlier than the 24 June 1945 notice, but no dates, ordering, or immediate-predecessor status are supplied.",
            quality="C_reputable_contemporary_or_scholarly", confidence="medium", publication="publish_qualified",
            notes="Earlier employment only; not marked immediate or last civilian employer.",
            source_links=[{"source_key": LIVING_CHURCH, "locator_override": "PDF physical pages 5-6", "excerpt_override": "instructor and tutor in history at Harvard and Radcliffe"}],
            affiliation_key="paul-l-ward-radcliffe-b1000",
        ),
        make_claim(
            key="employment-paul-l-ward-russell-sage-b1000", row=36, claim_type="other_pre_oss_affiliation",
            text="Paul L Ward had earlier served as assistant professor of history at Russell Sage College in Troy, New York.",
            paraphrase="The contemporary notice lists the college, role, and city among Ward's experience before describing his current OSS role.",
            identity="High-confidence identity from the same exact-name contemporary profile that explicitly places him with OSS.",
            temporal="Documented earlier than the 24 June 1945 notice, but no dates, ordering, or immediate-predecessor status are supplied.",
            quality="C_reputable_contemporary_or_scholarly", confidence="medium", publication="publish_qualified",
            notes="Earlier employment only; not marked immediate or last civilian employer.",
            source_links=[{"source_key": LIVING_CHURCH, "locator_override": "PDF physical page 6", "excerpt_override": "assistant professor of history at Russell Sage College, Troy, N. Y."}],
            affiliation_key="paul-l-ward-russell-sage-b1000",
        ),
        make_claim(
            key="identity-edmund-d-wardrop-b1000", row=42, claim_type="identity",
            text="The indexed First Lieutenant Edmund D Wardrop is probably the Princeton Class of 1934 alumnus named on Edgeworth's 1946 World War II honor roll.",
            paraphrase="The uncommon exact name, institutional class-year reference, contemporary-era civic honor roll, and CIA FOIA request subject converge, but no direct OSS bridge was accessible.",
            identity="Probable from the distinctive exact first name, middle initial, surname, prewar class year, and World War II service context; the Box 816 file is still required.",
            temporal="The Princeton class year predates the war and the 1946 honor roll establishes World War II service context, but neither supplies an OSS assignment or employer.",
            quality="B_authoritative_institutional", confidence="medium", publication="publish_qualified",
            notes="The CIA item is only a FOIA request subject and is not treated as agency employment evidence. Rank remains supported only by the OSS index.",
            source_links=[
                {"source_key": INDEX, "locator_override": "PDF page 490 row 42; printed rank 1st Lt.; Box 816"},
                {"source_key": PRINCETON, "locator_override": "Memorial body", "excerpt_override": "A brother, Edmund D. Wardrop '34, died in 1963."},
                {"source_key": EDGEWORTH, "locator_override": "1946 World War II honor-roll inscription", "excerpt_override": "Edmund D. Wardrop"},
                {"source_key": CIA_FOIA, "support_type": "context_only", "locator_override": "FOIA case-log entry", "excerpt_override": "EDMUND DONNAN WARDROP"},
            ],
        ),
        make_claim(
            key="student-edmund-d-wardrop-princeton-b1000", row=42, claim_type="other_pre_oss_affiliation",
            text="A probable Edmund D Wardrop identity was associated with Princeton's Class of 1934 as a student, not as an employee.",
            paraphrase="Princeton Alumni Weekly identifies Edmund D. Wardrop with the Class of 1934 in a memorial for his brother.",
            identity="Probable, not confirmed, from the distinctive exact name and corroborating World War II service context.",
            temporal="The 1934 class year is documented prewar, but degree completion and its relation to later service are not established.",
            quality="B_authoritative_institutional", confidence="medium", publication="publish_qualified",
            notes="Student status is explicitly separated from employment and excluded from employer analytics.",
            source_links=[{"source_key": PRINCETON, "locator_override": "Memorial body", "excerpt_override": "A brother, Edmund D. Wardrop '34, died in 1963."}],
            affiliation_key="edmund-d-wardrop-princeton-b1000",
        ),
        make_claim(
            key="identity-gaither-p-warfield-b1000", row=46, claim_type="identity",
            text="The indexed Gaither P Warfield is a high-confidence match to Methodist missionary Gaither Postley Warfield.",
            paraphrase="The distinctive exact name and middle initial align with an institutional full-name biography and a detailed wartime chronology.",
            identity="High confidence from the highly distinctive exact name and middle initial plus a continuous 1896-1986 institutional biography covering the wartime years.",
            temporal="The memoir documents prewar, wartime, and postwar church service but does not explicitly mention OSS or explain the indexed-file sequence.",
            quality="B_authoritative_institutional", confidence="high", publication="published",
            notes="The Box 816 file remains necessary for direct confirmation and the OSS-service chronology.",
            source_links=[
                {"source_key": INDEX, "locator_override": "PDF page 490 row 46; Box 816"},
                {"source_key": VAUMC, "locator_override": "PDF physical pages 7-8", "excerpt_override": "Gaither Postley Warfield was born February 13, 1896, Rockville, Maryland"},
            ],
        ),
        make_claim(
            key="affiliation-gaither-warfield-poland-b1000", row=46, claim_type="other_pre_oss_affiliation",
            text="Gaither P Warfield served as a Methodist missionary in Poland from his 1924 appointment until repatriation in 1942.",
            paraphrase="The institutional memoir dates his appointment, describes eighteen years of service, and dates repatriation after the occupation.",
            identity="High confidence from the distinctive exact-name institutional biography.",
            temporal="Explicitly dated 1924-1942 and therefore documented prewar and wartime; no immediate OSS transition is stated.",
            quality="B_authoritative_institutional", confidence="high", publication="published",
            notes="Professional religious affiliation, not silently converted into a conventional named employer.",
            source_links=[{"source_key": VAUMC, "locator_override": "PDF physical page 8", "excerpt_override": "appointed to Poland where he began his eventful, dramatic 18 years of service"}],
            affiliation_key="gaither-warfield-poland-b1000",
        ),
        make_claim(
            key="affiliation-gaither-warfield-board-missions-b1000", row=46, claim_type="other_pre_oss_affiliation",
            text="After returning to the United States in 1942, Gaither P Warfield served the Board of Missions of the Methodist Church until 1946.",
            paraphrase="The institutional memoir explicitly names the Board and dates the service from his 1942 return through 1946.",
            identity="High confidence from the distinctive exact-name institutional biography.",
            temporal="Strong wartime bounds, but the source does not explain whether, when, or how this affiliation intersected indexed OSS service.",
            quality="B_authoritative_institutional", confidence="medium", publication="publish_qualified",
            notes="Not labeled immediate pre-OSS and not treated as a last civilian employer pending the personnel file.",
            source_links=[{"source_key": VAUMC, "locator_override": "PDF physical page 8", "excerpt_override": "served the Board of Missions of the Methodist Church until 1946"}],
            affiliation_key="gaither-warfield-board-missions-b1000",
        ),
    ])
    return values


def base_update(row: int, **overrides: object) -> dict[str, object]:
    value: dict[str, object] = {
        "person_id": PEOPLE[row][0], "manual_review_required": True,
        "personnel_file_digitized": False, "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }
    value.update(overrides)
    return value


def person_updates() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, reason in UNRESOLVED.items():
        values.append(base_update(
            row, identity_status="unresolved",
            identity_evidence=f"The visually verified page 490 row preserves {PEOPLE[row][1]} and its Box 816 context. {reason}",
            research_status="requires_archival_review",
            next_action=f"Review the indexed Box 816 personnel file for corroborating identifiers, the immediate pre-OSS affiliation, and the last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}",
        ))
    for row, item in ARMY_OCCUPATIONS.items():
        category = "civilian_professional_or_administrative_grade" if row == 27 else "enlisted_army_personnel"
        values.append(base_update(
            row, identity_status="confirmed",
            identity_evidence="The exact indexed name and a nonshared protected identifier connect the row to the reviewed official Army record.",
            personnel_category=category, commissioned_officer=False,
            allied_or_foreign_personnel=False, research_status="occupation_only_found",
            next_action=f"Review the indexed Box 816 personnel file to identify any named employer or institution behind the broad {item['occupation']} category and establish the Army-to-OSS chronology. The printed OSS index status remains authoritative for public personnel classification.",
            nara_catalog_id="1263923",
        ))
    values.extend([
        base_update(
            29, identity_status="conflicting",
            identity_evidence="The protected-identifier candidate names John Ward in the official Army record, materially conflicting with indexed Jean E Ward; no Army evidence is transferred.",
            research_status="conflicting_sources",
            next_action="Review Jean E Ward's Box 816 personnel file and the conflicting Army candidate before transferring any identity, grade, or occupation evidence.",
        ),
        base_update(
            36, identity_status="high_confidence",
            identity_evidence="A June 1945 contemporary profile gives the exact name and middle initial, explicitly places Paul L Ward with OSS in Washington, and supplies a distinctive historian and Ph.D. profile.",
            personnel_category="civilian_professional_or_administrative_grade", commissioned_officer=False,
            allied_or_foreign_personnel=False, research_status="documented_prewar_employer_found",
            next_action="Review the indexed Box 816 personnel file to determine which teaching role, if any, was the immediate predecessor or last civilian employer and to date the transition into OSS.",
        ),
        base_update(
            42, identity_status="probable",
            identity_evidence="The uncommon exact name, Princeton Class of 1934 reference, 1946 World War II honor roll, and CIA FOIA request subject converge, but no direct OSS or protected-identifier bridge was accessible.",
            personnel_category="commissioned_army_officer", commissioned_officer=True,
            allied_or_foreign_personnel=False, research_status="requires_archival_review",
            next_action="Review the indexed Box 816 personnel file to confirm the probable identity and establish Edmund D Wardrop's immediate pre-OSS assignment and last civilian employer. The CIA FOIA log is only a request subject, not employment evidence.",
        ),
        base_update(
            46, identity_status="high_confidence",
            identity_evidence="The highly distinctive exact name and middle initial align with an institutional full-name biography and detailed 1924-1946 wartime chronology.",
            research_status="requires_archival_review",
            next_action="Review the indexed Box 816 personnel file to confirm the identity and determine how the Methodist Board of Missions service intersected OSS service; do not label either affiliation immediate without that sequence evidence.",
        ),
    ])
    return values


def research_attempts() -> list[dict[str, object]]:
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        reviewed = 1
        rejected = 0
        outcome = "no_result"
        note = UNRESOLVED.get(row, "")
        if row in ARMY_OCCUPATIONS:
            reviewed, outcome = 4, "source_reviewed"
            note = f"A reviewed Army bridge supports confirmed identity and a qualified {ARMY_OCCUPATIONS[row]['occupation']} category at Army entry; no named employer, institution, or direct OSS-transfer sequence is supplied."
            if row == 45:
                rejected = 2
                note += " Genealogy and postwar namesake leads were rejected as unbridged."
        elif row == 29:
            reviewed, rejected, outcome = 2, 1, "candidate_rejected"
            note = "The Army candidate says John Ward rather than Jean E Ward; no identity, occupation, or grade evidence was transferred."
        elif row == 36:
            reviewed, outcome = 2, "source_reviewed"
            note = "A contemporary notice explicitly places the exact-name historian with OSS in Washington and documents earlier teaching at Harvard, Radcliffe, and Russell Sage without proving their order or immediacy."
        elif row == 42:
            reviewed, outcome = 4, "source_reviewed"
            note = "Princeton, a 1946 honor roll, and a CIA FOIA request subject support a probable identity and prewar student affiliation; none establishes employment or a direct OSS bridge."
        elif row == 46:
            reviewed, outcome = 2, "source_reviewed"
            note = "An institutional memoir supports the distinctive identity and dated Methodist affiliations in Poland and the United States; the OSS overlap remains unresolved."
        elif row == 28:
            reviewed, rejected, outcome = 2, 1, "candidate_rejected"
            note = UNRESOLVED[row]
        elif row == 41:
            reviewed, rejected, outcome = 2, 1, "candidate_rejected"
            note = UNRESOLVED[row]
        attempts.append({
            "key": f"page490-row{row}-{slug(name)}-b1000",
            "person_id": person_id, "source_adapter": "manual_staged_protocol",
            "query_text": f"{name}; NARA OSS index context; CIA Reading Room exact-name domain check; Library of Congress collection check; exact-name and meaningful variants; OSS, rank, branch, assignment and identifier clues; employer and occupation 1940; obituary, institutional, newspaper, directory and archival searches; indexed Box 816; protected identifiers used only in private official-record comparison",
            "query_variant_type": "staged_identity_employment_archival_protocol_batch_1000",
            "started_at": "2026-11-03T15:10:00Z", "completed_at": "2026-11-03T17:58:00Z",
            "outcome": outcome, "sources_reviewed": reviewed,
            "candidate_sources_rejected": rejected,
            "rejection_reasons": "Unbridged common-name results, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives' employers, postwar-only leads, and sources without an OSS, protected-identifier, rank, unit, or personnel-file bridge were rejected. The James R. Ward Detachment 101 authorship lead and Philip Wardner postwar teaching references were not assigned. Historical occupation categories and student status were not converted into named employers.",
            "research_notes": f"{note} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain, and archival searches were checked as applicable. CIA Reading Room domain results were checked; no access restriction was bypassed. Library of Congress domain checks supplied no accepted identity or employment source. The NARA index page was text-extracted, rendered, and visually checked; official Army bulk data, technical documentation, and code documentation were inspected locally. No authenticated NARA Catalog API call was made.",
            "next_action": "Review the indexed Box 816 personnel file for corroborating identifiers, the immediate pre-OSS affiliation, and the last civilian employer before wartime service.",
            "attempt_number": 1, "research_agent_version": "before-oss-b1000-v1",
        })
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-1000-v1",
        "reviewer": "Before OSS Batch 1000 evidence review",
        "sources": sources(), "organizations": organizations(),
        "affiliations": affiliations(), "claims": claims(),
        "person_updates": person_updates(), "research_attempts": research_attempts(),
    }
    EvidenceBundle.model_validate(bundle)
    OUTPUT.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
