#!/usr/bin/env python3
"""Generate the reviewed Batch 917 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import uuid
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "research/evidence-page449-stewart-to-stiefel-review_batch-917_2026-10-26.json"

INDEX = "nara-index-b917"
ARMY = "army-bulk-b917"
TECH = "army-tech-b917"
CODES = "army-codes-b917"
OSWALD_OBIT = "express-times-oswald-stewart-b917"
MIT_OSWALD = "mit-alumni-oswald-stewart-b917"
NDU_STEWEN = "finland-ndu-stewen-b917"
LUND_STEWEN = "lund-stewen-b917"
STIAKAKIS_MEMORIAL = "war-memorials-stiakakis-b917"
OSSOG_STIANSEN = "ossog-stiansen-b917"
VESTERHEIM_STIANSEN = "vesterheim-stiansen-b917"
NPU_STIASSNI = "npu-karel-stiassni-b917"
USCOURT_STIEFEL = "us-court-ernst-stiefel-b917"
DB_STIEFEL = "deutsche-biographie-stiefel-b917"
WP_STIEFEL = "washington-post-stiefel-b917"

PEOPLE = {
    1: ("c9617d96-7e59-5dfb-becb-b56e55966fe9", "Jack S Stewart"),
    2: ("424de3fa-57da-5422-a92a-550d3d3cab89", "James R Stewart"),
    3: ("0ca29a30-7007-5330-b5ca-771fe271362c", "John H Stewart"),
    4: ("0f68bdcb-c062-5641-904b-740da9e3a3c3", "Joseph C Stewart"),
    5: ("b4d722ee-4bc5-5c6e-b4d5-e15241c446c2", "Joseph E Stewart"),
    6: ("01c7dcd8-d894-539c-89d9-dac9c047a162", "Margaret M Stewart"),
    7: ("55972627-d528-57a7-970f-fbd22d908154", "Mary Stewart"),
    8: ("b5b5b7f7-19d2-58cd-a62d-d307daa17538", "Oswald Stewart"),
    9: ("a216ee02-5f8d-59f2-87e2-de5f415e7395", "Susan S Stewart"),
    10: ("1b7afa81-e3d0-5dde-995a-88d889a470cd", "William D Stewart"),
    11: ("a174e1da-0c19-511d-8077-713c025c4a44", "William R Stewart"),
    12: ("4cf845da-4243-52c6-a37e-e59ea3e03ed0", "Martin K Stewen"),
    13: ("4ff0a066-312a-565a-9c00-89411b79e4e5", "Constantine Stiakakis"),
    14: ("22a1cfab-ac86-558e-87c6-31fc98b6174c", "Oddberg P Stiansen"),
    15: ("eaf13bea-cd19-5e19-8433-f2d51325d53d", "Karel C Stiassni"),
    16: ("97a168bb-761a-5998-b82d-3814fc261154", "Karel C Stiassni"),
    17: ("ea33c2c9-c603-5fc8-b072-fdff25ca39f2", "Betty A Stich"),
    18: ("d11d21d0-a731-5b46-9e9b-83d0f950c77b", "Shirlene J Stich"),
    19: ("581f6054-c633-54e8-a250-b8648f881a73", "Howard L Stickney"),
    20: ("69267441-cc57-5de4-b128-7cbf3fbb193e", "Ernest C Stiefel"),
    21: ("8ca1e52d-f2f9-5479-ac6d-74cfd3e4ee59", "Ernest C Stiefel"),
    22: ("ca0f3cc1-cd83-5041-be1b-9386d6b5592b", "Rudolph C Stiefel"),
    23: ("5503f49d-9886-520b-b7eb-7b696ab2aedf", "Sidney G Stiefel"),
}

ARMY_OCCUPATIONS = [
    {
        "row": 5,
        "date": "1943-03-12",
        "code": "105",
        "occupation": "Clerks, general office",
        "locator": "PDF physical page 171; category 1-05",
    },
    {
        "row": 10,
        "date": "1942-04-28",
        "code": "306",
        "occupation": "General farmers",
        "locator": "PDF physical page 172; category 3-06",
    },
]

UNRESOLVED = {
    1: "Exact-name, middle-initial, occupation, obituary, institutional, newspaper, directory and archival searches produced no defensible identity bridge.",
    2: "The protected index identifier produced no compatible official Army candidate, while exact-name searches returned unbridged namesakes.",
    3: "A Navy-lieutenant memorial candidate lacks an OSS, protected-identifier or Box 746 bridge and was rejected as an unassigned namesake.",
    4: "Common-name results did not supply two corroborating identifiers beyond the name or a reliable pre-OSS chronology.",
    6: "Exact-name and institutional searches produced no source with a defensible OSS identity bridge or pre-OSS employer chronology.",
    7: "The no-middle-name index row could not be distinguished from numerous namesakes through accessible official, obituary and institutional sources.",
    9: "Exact-name, occupation, obituary, institutional and archival searches produced no reliable person-specific match.",
    11: "Exact-name and middle-initial variants returned incompatible namesakes without an OSS assignment or protected-identifier bridge.",
    17: "Exact-name, occupation, obituary and archival searches found no reliable pre-OSS identity or employer evidence.",
    18: "The distinctive indexed name produced no reliable official, institutional, obituary, directory or archival result beyond the index.",
    19: "A Howard Loren Stickney Marine casualty record lacks an OSS, index-identifier or Box 747 bridge and was rejected as an unassigned namesake.",
    22: "A biographical note for engineer Rudolf Stiefel depends principally on family relationship and supplies no direct OSS or protected-identifier bridge to this row.",
    23: "A Honolulu obituary for Sidney Stiefel supplies no middle initial, OSS link, wartime chronology or protected-identifier bridge and was not assigned.",
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
            "archival_identifier": "RG 226, Entry A1-224, Boxes 746-747",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 449, rows 1-23; checked against layout-preserving text and a rendered page image",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All separately printed rows remain separate. Full protected identifiers remain private.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; two accepted reviewed Batch 917 identity bridges",
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
            "locator": "PDF physical pages 171-172; Batch 917 categories 1-05 and 3-06 visually checked",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical occupation labels identify neither employers nor workplaces.",
        },
        {
            "key": OSWALD_OBIT,
            "stable_url": "https://obits.lehighvalleylive.com/us/obituaries/etpa/name/oswald-stewart-obituary?id=14953246",
            "title": "Oswald Stewart Obituary",
            "repository_publisher": "The Express-Times",
            "publication_record_date": "2009-01-14",
            "locator": "Biographical paragraph on MIT, Army anti-aircraft service and 1945 transfer to OSS",
            "access_date": "2026-10-26",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "The Express-Times obituaries",
            "rights_notes": "Only short evidence excerpts and project-authored paraphrases are retained.",
        },
        {
            "key": MIT_OSWALD,
            "stable_url": "https://alum.mit.edu/sites/default/files/2017-05/FY04_Report.pdf",
            "title": "Association of Alumni and Alumnae of MIT Fiscal Year 2004 Report",
            "author_creator": "MIT Alumni Association",
            "repository_publisher": "Massachusetts Institute of Technology",
            "publication_record_date": "2004",
            "locator": "PDF pages 24-25; Oswald Stewart '39 among Harold E. Lobdell Distinguished Service Award recipients",
            "access_date": "2026-10-26",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "MIT Alumni Association reports",
            "rights_notes": "Institutional corroboration supports class-year identity; student status is not employment.",
        },
        {
            "key": NDU_STEWEN,
            "stable_url": "https://www.doria.fi/bitstream/handle/10024/125274/FDS_Palokangas_netpdf.pdf?sequence=2",
            "title": "Exploding Wilderness: Guerrilla-type activities in the Finnish art of war",
            "author_creator": "Marko Palokangas",
            "repository_publisher": "National Defence University of Finland",
            "publication_record_date": "2016",
            "locator": "PDF physical page 86 and note 266; Martin Stewen identified as Finland's military attaché in Stockholm",
            "access_date": "2026-10-26",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Finnish Defence Studies 20",
            "rights_notes": "Used for the documented wartime role; it does not establish an OSS employment relationship.",
        },
        {
            "key": LUND_STEWEN,
            "stable_url": "https://lup.lub.lu.se/luur/download?fileOId=9218237&func=downloadFile&recordOId=9218235",
            "title": "Keep Quiet and Nobody Gets Hurt: Investigating the Decline of the Swedish-Finnish Intelligence Sharing Relationship 1943-1948",
            "author_creator": "Luukas Lilover and Wilmer Filen",
            "repository_publisher": "Lund University, Department of Political Science",
            "publication_record_date": "2025",
            "locator": "PDF physical page 6; Martin Kasimir Stewen identified as Finland's military attaché to Stockholm, 1942-1944",
            "access_date": "2026-10-26",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Lund University student papers",
            "rights_notes": "Corroborates the full name and dated military assignment; temporal relation to the indexed OSS file remains uncertain.",
        },
        {
            "key": STIAKAKIS_MEMORIAL,
            "stable_url": "https://uswarmemorials.org/html/monument_details.php?MemID=1865&SiteID=1414&file=monument_details.php&page=4",
            "title": "Greek Operational Group (OSS) Soldier Monument",
            "author_creator": "American War Memorials Overseas, Inc.",
            "repository_publisher": "American War Memorials Overseas, Inc.",
            "publication_record_date": "Monument dedicated 2005-05-26",
            "locator": "People list and unit fields naming Constantine Stiakakis, Company C, 2671st Special Reconnaissance Battalion and OSS Greek Operational Group",
            "access_date": "2026-10-26",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "American War Memorials Overseas database",
            "rights_notes": "Supports an identity and OSS-unit bridge only; it names no pre-OSS employer.",
        },
        {
            "key": OSSOG_STIANSEN,
            "stable_url": "https://ossog.info/norway/norso_01.html",
            "title": "Office of Strategic Services Operational Groups: Operation Rype",
            "author_creator": "Art Frizzell",
            "repository_publisher": "Office of Strategic Services Operational Groups",
            "locator": "Norwegian OG personnel roster; T/5 Oddberg P. Stiansen marked as part of the initial RYPE deployment",
            "access_date": "2026-10-26",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Norwegian Operational Group histories",
            "rights_notes": "The compiler identifies NARA records and Colby reports as sources. No pre-OSS employer is supplied.",
        },
        {
            "key": VESTERHEIM_STIANSEN,
            "stable_url": "https://vesterheim.org/norwegian-special-operations-group-percy-red/",
            "title": "Rieder Grunseth and the Norwegian Special Operations Group - Operation Percy Red",
            "author_creator": "Jon Grunseth",
            "repository_publisher": "Vesterheim Norwegian-American Museum",
            "publication_record_date": "2025",
            "locator": "Percy Red roster naming T/5 Oddberg Stiansen",
            "access_date": "2026-10-26",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Vesterheim Blog",
            "rights_notes": "Museum-hosted family history corroborates the OSS operational-group roster; it names no pre-OSS employer.",
        },
        {
            "key": NPU_STIASSNI,
            "stable_url": "https://www.npu.cz/uop/brno/akce/2022/MCMA_CS_stopa/sbornik_web.pdf",
            "title": "Czechoslovak Traces in Subcarpathian Ruthenia, Monuments at Risk, and Heritage Preservation",
            "author_creator": "Vlasta Loutocka and Hana Urbaskova, editors",
            "repository_publisher": "National Heritage Institute, Brno Methodological Centre of Modern Architecture",
            "publication_record_date": "2022",
            "locator": "PDF physical page 116; Karel Stiassni described as a U.S. Army first lieutenant during Czechoslovakia's liberation",
            "access_date": "2026-10-26",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "National Heritage Institute publications",
            "rights_notes": "A low-confidence identity candidate for two separately printed same-name rows; not published as settled fact.",
        },
        {
            "key": USCOURT_STIEFEL,
            "stable_url": "https://www.rid.uscourts.gov/sites/rid/files/historical/documents/20150908-LawyersWithoutRightsExhibit-Book2.pdf",
            "title": "Lawyers Without Rights",
            "author_creator": "German Federal Bar and American Bar Association Section of International Law",
            "repository_publisher": "United States District Court for the District of Rhode Island",
            "locator": "PDF physical page 17; Ernst Stiefel panel describing Board of Economic Warfare work, Army draft and OSS deployment",
            "access_date": "2026-10-26",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Lawyers Without Rights exhibit",
            "rights_notes": "The biography is retained as a low-confidence candidate for two separate Ernest C. Stiefel index rows.",
        },
        {
            "key": DB_STIEFEL,
            "stable_url": "https://www.deutsche-biographie.de/gnd118829386.html",
            "archival_identifier": "GND 118829386",
            "title": "Stiefel, Ernst (Ernest) Carl",
            "author_creator": "Kurt Biedenkopf",
            "repository_publisher": "Deutsche Biographie / Neue Deutsche Biographie",
            "publication_record_date": "2013",
            "locator": "Name variants and biography; consultant in the Office of Economic Warfare before Army service",
            "access_date": "2026-10-26",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Neue Deutsche Biographie 25",
            "rights_notes": "Supports the Ernest/Ernst name variants but does not identify which printed index row is intended.",
        },
        {
            "key": WP_STIEFEL,
            "stable_url": "https://www.washingtonpost.com/archive/politics/2000/10/29/oss-unit-used-insurance-data-as-weapons-of-war/98a387c0-dce3-4d7f-bf46-f1cc2eb915ba/",
            "title": "OSS Unit Used Insurance Data as Weapons of War",
            "author_creator": "Mark Fritz",
            "repository_publisher": "The Washington Post",
            "publication_record_date": "2000-10-28",
            "locator": "Paragraph identifying Ernest Stiefel as a member of the OSS Insurance Intelligence Unit",
            "access_date": "2026-10-26",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "The Washington Post archive",
            "rights_notes": "Contextual corroboration only; duplicate index rows prevent assignment to a single entity.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": "us-army-b917",
            "organization_id": "28a26f92-78af-5a1a-9c09-a843eb5975b4",
            "canonical_name": "United States Army",
            "historical_name": "Army of the United States",
            "aliases": ["U.S. Army"],
            "organization_type": "military service",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "Existing canonical organization reused. Specific units remain in affiliation wording; Army service is not civilian employment.",
        },
        {
            "key": "mit-b917",
            "organization_id": "c254b90a-52af-5598-a9f9-9ac1d4406f16",
            "canonical_name": "Massachusetts Institute of Technology",
            "historical_name": "Massachusetts Institute of Technology",
            "aliases": ["MIT"],
            "organization_type": "university and research institute",
            "sector": "academia_and_research",
            "city": "Cambridge",
            "state_or_region": "Massachusetts",
            "country": "United States",
            "normalization_notes": "Student relationships are modeled separately from employment.",
        },
        {
            "key": "finnish-defence-forces-b917",
            "organization_id": stable_id("organization", "Finnish Defence Forces wartime military attache"),
            "canonical_name": "Finnish Defence Forces",
            "historical_name": "Finnish Defence Forces",
            "aliases": ["Defence Forces of Finland"],
            "organization_type": "national military service",
            "sector": "military",
            "country": "Finland",
            "normalization_notes": "The source wording is preserved as Finland's military attache to Stockholm; no civilian employer relationship is inferred.",
        },
        {
            "key": "board-economic-warfare-b917",
            "organization_id": "c560e197-f162-5279-b2f2-b75de9c71872",
            "canonical_name": "Board of Economic Warfare",
            "historical_name": "Board of Economic Warfare",
            "aliases": ["BEW"],
            "organization_type": "federal wartime agency",
            "sector": "federal_government",
            "city": "Washington",
            "state_or_region": "District of Columbia",
            "country": "United States",
            "active_dates": "1941-1943",
            "normalization_notes": "Existing organization reused. Government assignment is kept distinct from civilian employment.",
        },
    ]


def army_affiliation(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    person_id, name = PEOPLE[row]
    return {
        "key": f"{slug(name)}-occupation-b917",
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
        "research_notes": "The historical category is not converted into a named employer, workplace or exact job title.",
    }


def affiliations() -> list[dict[str, object]]:
    values = [army_affiliation(item) for item in ARMY_OCCUPATIONS]
    values.extend(
        [
            {
                "key": "oswald-stewart-army-anti-aircraft-b917",
                "person_id": PEOPLE[8][0],
                "organization_key": "us-army-b917",
                "organization_name_as_found": "Army anti-aircraft units in the China-Burma-India theater",
                "role_title": "second lieutenant to major",
                "relationship_type": "military_assignment",
                "start_date": "1940",
                "end_date": "1945",
                "date_precision": "The obituary states Army service began in 1940 and that he transferred from anti-aircraft units to OSS in 1945.",
                "country": "United States",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "explicit_immediate",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "published",
                "research_notes": "The military assignment is not labeled a civilian employer. The indexed personnel file is still needed for exact unit and transfer dates.",
            },
            {
                "key": "oswald-stewart-mit-student-b917",
                "person_id": PEOPLE[8][0],
                "organization_key": "mit-b917",
                "organization_name_as_found": "MIT",
                "role_title": "mechanical-engineering student",
                "relationship_type": "student",
                "end_date": "1939",
                "date_precision": "The obituary states that he graduated in 1939; the MIT alumni report independently identifies Oswald Stewart as class of 1939.",
                "city": "Cambridge",
                "state_or_region": "Massachusetts",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "MIT is a documented educational affiliation, not an employer.",
            },
            {
                "key": "martin-stewen-finland-attache-b917",
                "person_id": PEOPLE[12][0],
                "organization_key": "finnish-defence-forces-b917",
                "organization_name_as_found": "Finland's military attache to Stockholm",
                "role_title": "military attache",
                "relationship_type": "military_assignment",
                "start_date": "1942",
                "end_date": "1944",
                "date_precision": "Two scholarly institutional sources identify the role; neither fixes its temporal relation to the indexed OSS personnel file.",
                "city": "Stockholm",
                "country": "Sweden",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "temporal_relation_uncertain",
                "identity_confidence": "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "publish_qualified",
                "research_notes": "The assignment is documented, but the accessible sources do not establish that it immediately preceded an OSS recruitment, employment or transfer.",
            },
        ]
    )
    for row in (20, 21):
        values.append(
            {
                "key": f"ernest-c-stiefel-board-economic-warfare-row{row}-b917",
                "person_id": PEOPLE[row][0],
                "organization_key": "board-economic-warfare-b917",
                "organization_name_as_found": "Board of Economic Warfare",
                "role_title": "researcher and writer on insurance questions",
                "relationship_type": "government_assignment",
                "end_date": "1943",
                "date_precision": "The biography explicitly places this work before a December 1943 Army draft and OSS deployment, but the duplicate index rows cannot be distinguished.",
                "city": "Washington",
                "state_or_region": "District of Columbia",
                "country": "United States",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "explicit_immediate",
                "identity_confidence": "ambiguous",
                "claim_confidence": "low",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "withheld_low_confidence",
                "research_notes": "Private candidate only. Two separately printed Ernest C. Stiefel rows remain distinct pending Box 747 review.",
            }
        )
    return values


def army_claims(item: dict[str, object]) -> list[dict[str, object]]:
    row = int(item["row"])
    person_id, name = PEOPLE[row]
    return [
        {
            "key": f"identity-{slug(name)}-b917",
            "person_id": person_id,
            "claim_type": "identity",
            "claim_text": f"The indexed {name} row is a high-confidence match to the reviewed official Army record.",
            "evidence_paraphrase": "A nonshared protected identifier and compatible name connect the visually verified index row to the official Army record.",
            "identity_match_assessment": "High confidence from the nonshared protected-identifier bridge and compatible name.",
            "temporal_assessment": "The Army record supports identity and a dated occupation category; it does not establish the OSS transfer sequence.",
            "source_quality": "A_direct_official",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "No protected identifier is exposed, and the coded occupation remains separate from employer claims.",
            "sources": [
                {"source_key": INDEX, "locator_override": f"PDF page 449 row {row}; protected identifier withheld"},
                {"source_key": ARMY, "locator_override": "Accepted reviewed identity bridge; protected identifier withheld"},
            ],
        },
        {
            "key": f"occupation-{slug(name)}-b917",
            "person_id": person_id,
            "affiliation_key": f"{slug(name)}-occupation-b917",
            "claim_type": "occupation",
            "claim_text": f"At Army entry on {item['date']}, the official record assigned {name} the historical civilian-occupation category '{item['occupation']}'; no employer is identified.",
            "evidence_paraphrase": f"The Army entry field carries code {item['code']}, which the visually checked NARA code list maps to the stated category.",
            "identity_match_assessment": "High confidence from a nonshared protected-identifier bridge between the index and official Army record.",
            "temporal_assessment": "Strongly date-bounded at Army entry, but neither immediate pre-OSS status nor a named employer is established.",
            "source_quality": "A_direct_official",
            "claim_confidence": "medium",
            "publication_status": "publish_qualified",
            "match_notes": "Historical code-language is retained and excluded from default confirmed/high-confidence employer analytics.",
            "sources": [
                {"source_key": ARMY, "locator_override": f"Army-entry date {item['date']}; occupation code {item['code']}; protected identifier withheld"},
                {"source_key": TECH, "support_type": "context_only", "locator_override": "Civilian-occupation field definition"},
                {"source_key": CODES, "locator_override": item["locator"], "excerpt_override": item["occupation"]},
            ],
        },
    ]


def historical_claims() -> list[dict[str, object]]:
    claims = [
        {
            "key": "identity-oswald-stewart-ii-b917",
            "person_id": PEOPLE[8][0],
            "claim_type": "identity",
            "claim_text": "The indexed Oswald Stewart is a high-confidence match to Oswald Stewart II, MIT class of 1939 and a U.S. Army officer transferred to OSS in 1945.",
            "evidence_paraphrase": "A detailed obituary supplies the distinctive name, education, Army chronology and explicit OSS transfer; MIT independently corroborates the class-year identity.",
            "identity_match_assessment": "High confidence from a distinctive exact name, explicit OSS service, compatible Army chronology and independent MIT class-year corroboration.",
            "temporal_assessment": "The obituary explicitly dates Army service to 1940-1946 and transfer to OSS to 1945.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "The high-confidence identity does not establish a civilian employer; the indexed file remains necessary for exact unit and transfer dates.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 449 row 8; protected identifier withheld"},
                {"source_key": OSWALD_OBIT},
                {"source_key": MIT_OSWALD, "support_type": "context_only"},
            ],
        },
        {
            "key": "immediate-oswald-stewart-army-b917",
            "person_id": PEOPLE[8][0],
            "affiliation_key": "oswald-stewart-army-anti-aircraft-b917",
            "claim_type": "immediate_pre_oss_affiliation",
            "claim_text": "Oswald Stewart served in U.S. Army anti-aircraft units in the China-Burma-India theater immediately before transferring to OSS in 1945.",
            "evidence_excerpt": "transferring to the OSS in 1945",
            "evidence_paraphrase": "The obituary places his anti-aircraft service before and his OSS transfer in 1945.",
            "identity_match_assessment": "High-confidence Oswald Stewart II identity supported by the explicit OSS obituary and MIT corroboration.",
            "temporal_assessment": "Explicit immediate sequence: Army anti-aircraft units followed by transfer to OSS in 1945.",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "A military assignment is published, not a civilian employer. Exact unit and transfer-day details await the personnel file.",
            "sources": [{"source_key": OSWALD_OBIT, "excerpt_override": "transferring to the OSS in 1945"}],
        },
        {
            "key": "prewar-oswald-stewart-mit-b917",
            "person_id": PEOPLE[8][0],
            "affiliation_key": "oswald-stewart-mit-student-b917",
            "claim_type": "other_pre_oss_affiliation",
            "claim_text": "Oswald Stewart graduated from MIT in 1939 with a degree in mechanical engineering.",
            "evidence_excerpt": "graduated from MIT in 1939 with a degree in mechanical engineering",
            "evidence_paraphrase": "The obituary provides the degree and year; the MIT alumni report identifies Oswald Stewart as class of 1939.",
            "identity_match_assessment": "High-confidence identity from the explicit OSS obituary and matching MIT class-year record.",
            "temporal_assessment": "Documented prewar student status ending in 1939, before Army service began in 1940.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "MIT is correctly labeled as an educational institution rather than an employer.",
            "sources": [
                {"source_key": OSWALD_OBIT, "excerpt_override": "graduated from MIT in 1939 with a degree in mechanical engineering"},
                {"source_key": MIT_OSWALD, "excerpt_override": "Oswald Stewart '39"},
            ],
        },
        {
            "key": "identity-martin-kasimir-stewen-b917",
            "person_id": PEOPLE[12][0],
            "claim_type": "identity",
            "claim_text": "The indexed Martin K. Stewen is a high-confidence match to Finnish Colonel Martin Kasimir Stewen.",
            "evidence_paraphrase": "Two institutional studies independently identify the distinctive full name and wartime military-attache role in Stockholm.",
            "identity_match_assessment": "High confidence from the distinctive exact surname and initial, full-name expansion and mutually compatible Finnish military chronology.",
            "temporal_assessment": "The dated 1942-1944 role supports wartime identity but does not define the precise relationship to the indexed OSS file.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "The sources document a Finnish officer and intelligence liaison context; they do not convert him into a U.S. OSS employee.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 449 row 12"},
                {"source_key": NDU_STEWEN, "excerpt_override": "Martin Stewen, Finland's military attache in Stockholm"},
                {"source_key": LUND_STEWEN, "excerpt_override": "Stewen, Martin Kasimir - Finland's Military attache to Stockholm 1942-1944"},
            ],
        },
        {
            "key": "wartime-martin-stewen-attache-b917",
            "person_id": PEOPLE[12][0],
            "affiliation_key": "martin-stewen-finland-attache-b917",
            "claim_type": "other_pre_oss_affiliation",
            "claim_text": "Martin Kasimir Stewen served as Finland's military attache to Stockholm from 1942 to 1944.",
            "evidence_paraphrase": "The Lund study dates the assignment to 1942-1944, while the Finnish National Defence University independently identifies the same role.",
            "identity_match_assessment": "High-confidence match to the distinctive indexed name Martin K. Stewen.",
            "temporal_assessment": "The military assignment is dated, but its sequence relative to the indexed OSS relationship remains uncertain.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "medium",
            "publication_status": "publish_qualified",
            "match_notes": "The profile visibly qualifies the temporal relation and does not call the Finnish military assignment a civilian employer.",
            "sources": [
                {"source_key": NDU_STEWEN, "excerpt_override": "Martin Stewen, Finland's military attache in Stockholm"},
                {"source_key": LUND_STEWEN, "excerpt_override": "Stewen, Martin Kasimir - Finland's Military attache to Stockholm 1942-1944"},
            ],
        },
        {
            "key": "identity-constantine-stiakakis-b917",
            "person_id": PEOPLE[13][0],
            "claim_type": "identity",
            "claim_text": "The indexed T/5 Constantine Stiakakis is a high-confidence match to the OSS Greek Operational Group servicemember commemorated by name in Athens.",
            "evidence_paraphrase": "The distinctive exact name appears in both the official index and the Greek Operational Group monument database, which supplies the OSS unit context.",
            "identity_match_assessment": "High confidence from the distinctive exact name, compatible T/5 Army status and specific OSS Greek Operational Group context.",
            "temporal_assessment": "The sources establish wartime OSS-unit identity but supply no earlier employer or predecessor assignment.",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "No claim is made that the unit-level 122nd Infantry recruitment narrative proves this person's immediate pre-OSS assignment.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 449 row 13; rank T/5"},
                {"source_key": STIAKAKIS_MEMORIAL, "excerpt_override": "Constantine Stiakakis"},
            ],
        },
        {
            "key": "identity-oddberg-p-stiansen-b917",
            "person_id": PEOPLE[14][0],
            "claim_type": "identity",
            "claim_text": "The indexed Oddberg P. Stiansen is a high-confidence match to T/5 Oddberg P. Stiansen of the OSS Norwegian Operational Group.",
            "evidence_paraphrase": "An archive-informed operational-group roster and a Norwegian-American museum history independently name the distinctive servicemember and rank.",
            "identity_match_assessment": "High confidence from the distinctive full name, matching middle initial, rank and two mutually compatible OSS operational-group sources.",
            "temporal_assessment": "The sources establish OSS service and deployment context but identify no pre-OSS employer.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "No civilian occupation or employer is inferred from Norwegian-American operational-group service.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 449 row 14; protected identifier withheld"},
                {"source_key": OSSOG_STIANSEN, "excerpt_override": "T/5 Oddberg P. Stiansen"},
                {"source_key": VESTERHEIM_STIANSEN, "excerpt_override": "T/5 Oddberg Stiansen"},
            ],
        },
    ]
    for row in (15, 16):
        claims.append(
            {
                "key": f"candidate-karel-c-stiassni-row{row}-b917",
                "person_id": PEOPLE[row][0],
                "claim_type": "identity",
                "claim_text": "An institutional history documents a Karel Stiassni who served as a U.S. Army first lieutenant, but it cannot yet be assigned to this separately printed index row.",
                "evidence_paraphrase": "The rare exact name and U.S. Army service are compatible, but page 449 contains two Karel C. Stiassni rows with different protected identifiers.",
                "identity_match_assessment": "Ambiguous. Direct personnel-file evidence is required before assigning the external biography to either source row.",
                "temporal_assessment": "The source documents wartime Army service but supplies no proven OSS entry sequence for this index row.",
                "source_quality": "B_authoritative_institutional",
                "claim_confidence": "low",
                "publication_status": "withheld_low_confidence",
                "match_notes": "Private review candidate only. The two rows remain separate and no famous or convenient biography is selected by name alone.",
                "sources": [
                    {"source_key": INDEX, "locator_override": f"PDF page 449 row {row}; protected identifier withheld"},
                    {"source_key": NPU_STIASSNI, "excerpt_override": "Karel Stiassni"},
                ],
            }
        )
    for row in (20, 21):
        claims.extend(
            [
                {
                    "key": f"candidate-ernest-c-stiefel-row{row}-b917",
                    "person_id": PEOPLE[row][0],
                    "claim_type": "identity",
                    "claim_text": "The Ernst Carl Stiefel biography is a strong name-and-OSS candidate, but it cannot yet be assigned to this separately printed Ernest C. Stiefel row.",
                    "evidence_paraphrase": "Institutional and newspaper sources connect the Ernest/Ernst C. name variants to OSS insurance work, while page 449 contains two separate same-name rows.",
                    "identity_match_assessment": "Ambiguous. The external biography cannot distinguish the row with a protected identifier from the row without one.",
                    "temporal_assessment": "The biography supplies an explicit Board of Economic Warfare-to-Army/OSS chronology for the candidate, not a resolved row assignment.",
                    "source_quality": "B_authoritative_institutional",
                    "claim_confidence": "low",
                    "publication_status": "withheld_low_confidence",
                    "match_notes": "Private candidate only. Both index rows remain visible and require Box 747 review.",
                    "sources": [
                        {"source_key": INDEX, "locator_override": f"PDF page 449 row {row}; protected identifier withheld when present"},
                        {"source_key": USCOURT_STIEFEL, "excerpt_override": "deployed with the Office of Strategic Services"},
                        {"source_key": DB_STIEFEL, "excerpt_override": "Stiefel, Ernest C."},
                        {"source_key": WP_STIEFEL, "support_type": "context_only", "excerpt_override": "Ernest Stiefel, a member of the intelligence unit"},
                    ],
                },
                {
                    "key": f"candidate-immediate-ernest-c-stiefel-row{row}-b917",
                    "person_id": PEOPLE[row][0],
                    "affiliation_key": f"ernest-c-stiefel-board-economic-warfare-row{row}-b917",
                    "claim_type": "immediate_pre_oss_affiliation",
                    "claim_text": "A candidate biography places Ernst Carl Stiefel with the Board of Economic Warfare before his December 1943 Army draft and OSS deployment.",
                    "evidence_paraphrase": "The institutional exhibit explicitly gives the sequence, but the duplicate source rows make person-level assignment unresolved.",
                    "identity_match_assessment": "Low for this row because two separately printed Ernest C. Stiefel records cannot yet be distinguished.",
                    "temporal_assessment": "Explicit immediate sequence for the external candidate; unverified row assignment.",
                    "source_quality": "B_authoritative_institutional",
                    "claim_confidence": "low",
                    "publication_status": "withheld_low_confidence",
                    "match_notes": "Not published as fact and excluded from default analytics until the indexed personnel files resolve the duplicate rows.",
                    "sources": [
                        {"source_key": USCOURT_STIEFEL, "excerpt_override": "involved with the Board of Economic Warfare"},
                        {"source_key": DB_STIEFEL, "support_type": "context_only"},
                    ],
                },
            ]
        )
    return claims


def accepted_army_update(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    person_id, _name = PEOPLE[row]
    return {
        "person_id": person_id,
        "identity_status": "high_confidence",
        "identity_evidence": "A nonshared protected identifier and compatible name connect the visually verified index row to the reviewed official Army record. The historical occupation field remains separate from employer and immediate-affiliation claims.",
        "personnel_category": "enlisted_army_personnel",
        "commissioned_officer": False,
        "allied_or_foreign_personnel": False,
        "manual_review_required": True,
        "research_status": "occupation_only_found",
        "next_action": f"Review the indexed Box {'746' if row == 5 else '747'} personnel file to identify the immediate pre-OSS affiliation and last civilian employer; do not convert the Army occupation category into a named employer.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }


def unresolved_update(row: int) -> dict[str, object]:
    person_id, name = PEOPLE[row]
    box = "746" if row <= 6 else "747"
    return {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, Box {box} and archive location, but staged NARA context, CIA Reading Room, exact-name, occupation, employer, obituary, institutional, newspaper, directory, Library of Congress and archival searches found no defensible identity bridge. {UNRESOLVED[row]}",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": f"Review the indexed Box {box} personnel file for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "critical" if row in {2, 19, 22, 23} else "high",
    }


def person_updates() -> list[dict[str, object]]:
    updates = [accepted_army_update(item) for item in ARMY_OCCUPATIONS]
    updates.extend(unresolved_update(row) for row in UNRESOLVED)
    updates.extend(
        [
            {
                "person_id": PEOPLE[8][0],
                "identity_status": "high_confidence",
                "identity_evidence": "The distinctive indexed name is explicitly connected to OSS in a detailed obituary that dates Army anti-aircraft service and a 1945 OSS transfer. MIT independently corroborates Oswald Stewart's 1939 class year.",
                "name_variants": ["Oswald Stewart II"],
                "personnel_category": "commissioned_army_officer",
                "commissioned_officer": True,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Review the indexed Box 747 personnel file for exact Army unit and OSS transfer dates and any last civilian employer. MIT is student status, not employment.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "medium",
            },
            {
                "person_id": PEOPLE[12][0],
                "identity_status": "high_confidence",
                "identity_evidence": "Two institutional studies independently expand the distinctive indexed name to Martin Kasimir Stewen and identify his wartime Finnish military-attache role in Stockholm. The precise temporal relation to the indexed OSS file remains unproven.",
                "name_variants": ["Martin Kasimir Stewen", "Colonel Martin Stewen"],
                "personnel_category": "foreign_or_allied_military_personnel",
                "commissioned_officer": True,
                "allied_or_foreign_personnel": True,
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Review the indexed Box 747 file to determine Martin Stewen's precise OSS relationship and whether the 1942-1944 Finnish military-attache assignment immediately preceded it.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[13][0],
                "identity_status": "high_confidence",
                "identity_evidence": "The distinctive exact name, indexed T/5 rank and specific OSS Greek Operational Group monument context support a high-confidence identity. The unit-level recruitment narrative is not assigned as this person's immediate pre-OSS pathway.",
                "personnel_category": "enlisted_army_personnel",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Review the indexed Box 747 file for Constantine Stiakakis's pre-OSS assignment or employer; do not infer an individual transfer from the unit history alone.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[14][0],
                "identity_status": "high_confidence",
                "identity_evidence": "The distinctive full name and middle initial are independently corroborated by an archive-informed OSS Norwegian Operational Group roster and a Vesterheim museum history, both identifying T/5 Oddberg Stiansen.",
                "name_variants": ["T/5 Oddberg P Stiansen", "T/5 Oddberg Stiansen"],
                "personnel_category": "enlisted_army_personnel",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Review the indexed Box 747 file for Oddberg Stiansen's immediate pre-OSS assignment and last civilian employer; operational-group service supplies neither.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
        ]
    )
    for row in (15, 16):
        updates.append(
            {
                "person_id": PEOPLE[row][0],
                "identity_status": "ambiguous",
                "identity_evidence": "PDF page 449 contains two separately printed Karel C. Stiassni rows with different protected identifiers. Accessible external candidates cannot distinguish the rows, remain withheld at low confidence and are assigned to neither.",
                "possible_duplicate_group": "same-name:karel-c-stiassni-page449",
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Compare both indexed Box 747 personnel files and protected identifiers before merging either row or publishing any external biography for a specific entity.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            }
        )
    for row in (20, 21):
        updates.append(
            {
                "person_id": PEOPLE[row][0],
                "identity_status": "ambiguous",
                "identity_evidence": "PDF page 449 contains two separately printed Ernest C. Stiefel rows. One carries a protected identifier and one does not. Accessible external candidates cannot distinguish the rows, remain withheld at low confidence and are assigned to neither.",
                "possible_duplicate_group": "same-name:ernest-c-stiefel-page449",
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Compare both indexed Box 747 personnel files before merging either row or publishing any external employment chronology for a specific entity.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            }
        )
    return updates


def research_attempts() -> list[dict[str, object]]:
    army_rows = {5, 10}
    rich_rows = {8, 12, 13, 14}
    ambiguous_rows = {15, 16, 20, 21}
    attempts = []
    for row, (person_id, name) in PEOPLE.items():
        if row in army_rows:
            outcome = "source_reviewed"
            detail = "A reviewed official Army identity and dated historical occupation category were accepted; no named employer is supplied."
            reviewed, rejected = 8, 5
        elif row in rich_rows:
            outcome = "source_reviewed"
            detail = {
                8: "A high-confidence identity and explicit Army anti-aircraft-to-OSS transfer were accepted; MIT student status is documented separately from employment.",
                12: "A high-confidence identity and dated Finnish military-attache assignment were accepted with an explicit temporal qualification relative to OSS.",
                13: "A high-confidence OSS Greek Operational Group identity was accepted; the unit history does not establish an individual pre-OSS pathway.",
                14: "A high-confidence OSS Norwegian Operational Group identity was accepted from two compatible sources; no pre-OSS employer was found.",
            }[row]
            reviewed, rejected = 10, 6
        elif row in ambiguous_rows:
            outcome = "candidate_found"
            detail = "A specific external biography was retained as a private low-confidence candidate, but same-name duplicate source rows prevent a defensible assignment without the personnel files."
            reviewed, rejected = 9, 6
        else:
            outcome = "candidate_rejected"
            detail = UNRESOLVED[row]
            reviewed, rejected = 7, 7
        box = "746" if row <= 6 else "747"
        attempts.append(
            {
                "key": f"page449-row{row}-{slug(name)}-b917",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA/index context; CIA Reading Room and Library of Congress official-domain exact-name checks; OSS, rank and spelling variants; employer and occupation; obituary, institutional, newspaper, directory and archival searches; Box {box}; protected-identifier Army crosswalk where available",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_917",
                "started_at": "2026-10-26T03:08:00Z",
                "completed_at": "2026-10-26T04:24:00Z",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, discovery-only results, chronologically incompatible records, relatives-only matches and postwar-only material were not assigned." if row not in UNRESOLVED else detail,
                "research_notes": f"{detail} Search-result snippets were discovery aids only; public claims point to inspectable sources. The CIA Reading Room was temporarily in maintenance during a recheck. No access control was bypassed, and no exposed NARA API credential was used.",
                "next_action": f"Review the indexed Box {box} personnel file for corroborating identifiers, exact transition dates and the last documented pre-OSS affiliation.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b917-v1",
            }
        )
    return attempts


def main() -> None:
    claims: list[dict[str, object]] = []
    for item in ARMY_OCCUPATIONS:
        claims.extend(army_claims(item))
    claims.extend(historical_claims())
    bundle = {
        "bundle_version": "batch-917-v1",
        "reviewer": "Before OSS Batch 917 evidence review",
        "sources": sources(),
        "organizations": organizations(),
        "affiliations": affiliations(),
        "claims": claims,
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }
    OUTPUT.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
