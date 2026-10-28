#!/usr/bin/env python3
"""Generate the reviewed Batch 940 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / (
    "research/evidence-page460-jefferson-m-tancil-to-mary-b-tarbet-"
    "review_batch-940_2026-10-28.json"
)

INDEX = "nara-index-b940"
ARMY = "army-bulk-b940"
TECH = "army-tech-b940"
CODES = "army-codes-b940"
OSS_ORDER = "oss-travel-orders-existing-b940"
PACIFIC_TANI = "pacific-citizen-saburo-tani-b940"
JAVA_TANI = "java-mis-registry-saburo-tani-b940"
ARMY_NISEI = "army-nisei-linguists-b940"
MANZANAR_1943 = "manzanar-free-press-1943-tanisaki-b940"
MANZANAR_1944 = "manzanar-free-press-1944-tanisaki-b940"
ALBA_TANZ = "alba-alfred-tanz-b940"
LOC_TANZ = "loc-evening-star-alfred-tanz-b940"
RUBY_TAPE = "cathay-ruby-tape-b940"
WP_TAQUEY = "washington-post-charles-taquey-b940"
FIELD_TAQUEY = "field-artillery-charles-taquey-b940"
FIELD_TAQUEY_1943 = "field-artillery-charles-taquey-us-army-b940"
GOVINFO_TARASOV = "govinfo-helen-tarasov-b940"
LEGACY_TARBERT = "legacy-william-tarbert-b940"


PEOPLE = {
    24: ("29fb89c8-10fa-52be-9da2-7748a0478530", "Jefferson M Tancil"),
    25: ("2ac17d28-008f-56c7-a245-8eb7acd5f46d", "Ernest O Tancous"),
    26: ("0d6072d9-fb0f-5179-8be6-00f7b0f405be", "Jeanne C Taneyhill"),
    27: ("0273cc24-59e4-5976-9d06-b1c190308d1e", "Louis L Tang"),
    28: ("4f134170-2f6e-5f2f-aa6d-4ee3bde139a7", "T Y Tang"),
    29: ("5223864f-7d5d-5c58-ac61-bdebbaa9e35b", "Wen Shun Tang"),
    30: ("fb3d4db7-0878-5374-aafa-83fbc9f13c3e", "Corrine M Tanguay"),
    31: ("ddd7f9db-7681-59b6-90ae-3209bd1890af", "Saburo Tani"),
    32: ("3230157d-3a4d-5ba4-b86b-0b48c378c0a8", "Noboru M Tanimoto"),
    33: ("31d4b2c1-44f0-580e-8ed3-21900f6a8046", "Bob F Tanisaki"),
    34: ("6cc20403-47c9-5e63-a2a1-2af7fd280aae", "Jane M Tanner"),
    35: ("24e84169-6067-57d5-9df3-ad8326ae318e", "Joe W Tanner"),
    36: ("13e4cf5e-73fe-5a20-ba99-6749a1fb52d3", "Walter J Tanner"),
    37: ("87cd2c5b-73f9-5b42-8704-0f8b8afa679c", "Alfred L Tanz"),
    38: ("8d7b2266-af60-530c-ba8a-46858edc3524", "Ruby K Tape"),
    39: ("157f8db0-165e-5bdc-86c4-975a11168127", "Charles H Taquey"),
    40: ("49a969e2-6e4d-555e-ae93-fc81ad342152", "Antielle Taralle"),
    41: ("ec3a44af-1e99-5769-a770-d75c00cea911", "Carmine Tarallo"),
    42: ("ca5a6b22-278f-59f3-865f-a007f7ac9e33", "Frank J Tarallo"),
    43: ("f7f4f0ef-ddbd-5a7a-9355-21fb72882c9a", "Mario Tarantino"),
    44: ("1227c3d3-25e9-53f2-87d6-1a4db7f9f39d", "Helen Tarasov"),
    45: ("7d615a84-e4da-511e-b83f-da22dd97b4bd", "William L Tarbert"),
    46: ("1d8e292c-4ac8-5fcb-abbf-cfb5ec0ff89d", "Mary B Tarbet"),
}


UNRESOLVED = {
    24: "A postwar federal cryptologic-career lead and a 1944 marriage notice do not establish the indexed Jefferson M Tancil's pre-OSS identity or employer.",
    25: "Exact-name and variant OSS, employer, occupation, obituary, institutional and archival searches produced no defensible identity bridge.",
    26: "Exact-name and spelling-variant searches produced no source connecting the indexed row to a dated pre-OSS affiliation.",
    27: "Common-name OSS, military, employer, occupation, obituary and institutional searches produced no defensible Box 765 identity bridge.",
    28: "Initial-only and transliteration searches produced no source that safely distinguishes the indexed person from namesakes.",
    29: "A Yale-associated Wen Shun Tang language-teacher lead lacks a person-specific OSS or protected-identifier bridge and was not assigned.",
    30: "Exact-name and spelling-variant searches produced no defensible OSS identity or pre-OSS employment source.",
    34: "Common-name exact and middle-initial searches produced no defensible Box 765 identity bridge.",
    36: "Common-name exact and middle-initial searches produced no defensible Box 765 identity bridge.",
    40: "Exact-name and likely spelling-variant searches produced no reliable identity, occupation or employer source.",
    42: "Exact-name OSS, Army, employer, obituary, directory and archival searches produced no defensible identity bridge.",
    46: "Exact-name OSS, employer, occupation, obituary, institutional and archival searches produced no defensible identity bridge.",
}


ARMY_OCCUPATIONS = [
    {
        "row": 35,
        "slug": "joe-w-tanner",
        "date": "1942-12-12",
        "code": "316",
        "occupation": "Farm hands, general farms",
        "relationship_type": "employment",
        "locator": "PDF physical page 172; category 3-16",
    },
    {
        "row": 41,
        "slug": "carmine-tarallo",
        "date": "1944-07-09",
        "code": "992",
        "occupation": "Students",
        "relationship_type": "student",
        "locator": "PDF physical page 304; corrected Code No. 30 category 9-92",
    },
]


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Box 765",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 460, rows 24-46; checked against layout-preserving text and a 300 dpi page render",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. Full protected identifiers remain private. Ray L Tarbox on page 461 row 1 was checked as the next boundary.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; accepted Joe W Tanner, Carmine Tarallo and Mario Tarantino identity bridges; Ruby K Tape candidate retained as conflicting",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "No raw row or full protected identifier is retained in public assets. Coded occupations identify no employer, and an uninterpreted code is not published.",
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
            "locator": "PDF physical pages 172 and 304; categories 316 and corrected 992 visually checked",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical occupation labels identify neither employers nor workplaces.",
        },
        {
            "key": OSS_ORDER,
            "source_id": "2469c7e5-2353-5b68-b581-a174bab565d2",
            "stable_url": "https://www.historyofjapaneseinny.org/wp-content/uploads/2024/05/OFFICE-OF-STRATEGIC-SERVICES-1.pdf",
            "archival_identifier": "OSS Headquarters corrected Invitational Travel Orders, shipment IJ-B857-HY",
            "title": "Invitational Travel Orders, Shipment IJ-B857-HY",
            "author_creator": "Office of Strategic Services",
            "repository_publisher": "History of Japanese in New York",
            "publication_record_date": "1945-04-30",
            "locator": "PDF physical page 11; Chuzo Tamotzu, Fujiwo Bob Tanisaki and Noboru Mori Tanimoto among named civilian OSS employees",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "Office of Strategic Services records",
            "rights_notes": "The scanned order page was rendered at high resolution and visually inspected. It cannot determine which of the two near-duplicate Tanimoto/Tamimoto index rows it represents.",
        },
        {
            "key": PACIFIC_TANI,
            "stable_url": "https://pacificcitizen.org/wp-content/uploads/archives-menu/Vol.134_%2309_May_17_2002.pdf",
            "title": "University Seeks Former U.S. Navy Japanese Language School Instructors",
            "repository_publisher": "Pacific Citizen",
            "publication_record_date": "2002-05-17",
            "locator": "PDF physical page 5; Saburo Tani in the list of University of Colorado Navy Japanese/Oriental Language School teachers, 1942-1946",
            "access_date": "2026-10-28",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Pacific Citizen archive, volume 134, number 9",
            "rights_notes": "The full page was rendered and visually inspected; only a project-authored paraphrase is retained.",
        },
        {
            "key": JAVA_TANI,
            "stable_url": "https://java-us.org/wp-content/uploads/2023/09/8.pdf",
            "title": "Military Intelligence Service Registry Merged (alphabetical)",
            "author_creator": "Japanese American Veterans Association",
            "repository_publisher": "Japanese American Veterans Association",
            "locator": "Registry row 8826; Tani, Saburo; Faculty; Civilian",
            "access_date": "2026-10-28",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Military Intelligence Service Registry",
            "rights_notes": "Used to corroborate the civilian faculty role; it does not by itself establish the OSS transition date.",
        },
        {
            "key": ARMY_NISEI,
            "stable_url": "https://history.army.mil/portals/143/Images/Publications/catalog/70-99-1.pdf",
            "archival_identifier": "CMH Pub 70-99-1",
            "title": "Nisei Linguists: Japanese Americans in the Military Intelligence Service During World War II",
            "author_creator": "James C. McNaughton",
            "repository_publisher": "U.S. Army Center of Military History",
            "publication_record_date": "2006",
            "locator": "Printed page 150; Navy Japanese Language School instructors were employees of the University of Colorado",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "U.S. Army Center of Military History publications",
            "rights_notes": "Used for the institutional employment relationship, not as a person-specific roster.",
        },
        {
            "key": MANZANAR_1943,
            "stable_url": "https://tile.loc.gov/storage-services/service/sgp/sgpbatches/batch_dlc_anacostia_ver01/data/sn84025948/0023728866A/1943122201/0966.pdf",
            "archival_identifier": "sn84025948, 1943-12-22, page 4",
            "title": "Manzanar Free Press",
            "author_creator": "Manzanar Relocation Center Administration and Manzanar Cooperative Enterprises",
            "repository_publisher": "Library of Congress",
            "publication_record_date": "1943-12-22",
            "locator": "Page 4 staff box; Fujiwo Tanisaki, Japanese Section staff member",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "Japanese-American Internment Camp Newspapers, 1942-1946",
            "rights_notes": "The direct scan was rendered and visually inspected.",
        },
        {
            "key": MANZANAR_1944,
            "stable_url": "https://tile.loc.gov/storage-services/service/sgp/sgpbatches/batch_dlc_anacostia_ver01/data/sn84025948/0023728866A/1944061701/1428.pdf",
            "archival_identifier": "sn84025948, 1944-06-17, page 2",
            "title": "Manzanar Free Press",
            "author_creator": "Manzanar Relocation Center Administration and Manzanar Cooperative Enterprises",
            "repository_publisher": "Library of Congress",
            "publication_record_date": "1944-06-17",
            "locator": "Page 2 staff box; Fujiwo Tanisaki, Japanese Section chairman",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "Japanese-American Internment Camp Newspapers, 1942-1946",
            "rights_notes": "The direct scan was rendered and visually inspected.",
        },
        {
            "key": ALBA_TANZ,
            "stable_url": "https://alba-valb.org/wp-content/uploads/2020/01/vol23n05_winter2001.pdf",
            "title": "Alfred L. Tanz (1906-2000)",
            "author_creator": "Veterans of the Abraham Lincoln Brigade",
            "repository_publisher": "The Volunteer, an ALBA publication",
            "publication_record_date": "2001",
            "locator": "PDF physical page 20; legal work, Lincoln Battalion service, Army enlistment and Donovan recruitment into OSS",
            "access_date": "2026-10-28",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "The Volunteer, volume XXIII, number 5",
            "rights_notes": "The page was rendered and visually inspected; only concise project-authored paraphrases are retained.",
        },
        {
            "key": LOC_TANZ,
            "stable_url": "https://tile.loc.gov/storage-services/service/ndnp/dlc/batch_dlc_1lichtenstein_ver02/data/sn83045462/0028060169A/1938020901/0661.pdf",
            "archival_identifier": "The Evening Star, 1938-02-09, page A-5",
            "title": "New York Attorney Back From Spanish Front",
            "repository_publisher": "The Evening Star; Library of Congress",
            "publication_record_date": "1938-02-09",
            "locator": "Page A-5; Alfred L. Tanz described as a New York attorney and Lincoln Brigade lieutenant",
            "access_date": "2026-10-28",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Chronicling America",
            "rights_notes": "Contemporary corroboration of occupation and Spanish Civil War role.",
        },
        {
            "key": RUBY_TAPE,
            "stable_url": "https://www.sfcathaypost384.org/uploads/1/0/5/6/105640191/1301_cd__ruby_tape.pdf",
            "title": "Who Was Ruby Kim Tape?",
            "author_creator": "Roger S. Dong",
            "repository_publisher": "Cathay Chronicle, American Legion Cathay Post 384",
            "publication_record_date": "2013-01",
            "locator": "PDF physical pages 10-11; Women's Army Corps intelligence and Camp Ritchie account",
            "access_date": "2026-10-28",
            "source_quality": "D_correlative_or_secondary",
            "collection_name": "Cathay Chronicle",
            "rights_notes": "The exact-name biography is retained only as one side of an unresolved identity conflict; the pages were rendered and visually inspected.",
        },
        {
            "key": WP_TAQUEY,
            "stable_url": "https://www.washingtonpost.com/archive/local/1999/04/07/obituaries/d13adf97-9ddf-4776-bb99-8302ead53868/",
            "title": "Charles Henri Taquey: Diplomat",
            "repository_publisher": "The Washington Post",
            "publication_record_date": "1999-04-06",
            "locator": "Obituary section for Charles Henri Taquey; French foreign service, French Army, U.S. Army and OSS chronology",
            "access_date": "2026-10-28",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Washington Post obituaries",
            "rights_notes": "Only project-authored paraphrases are retained.",
        },
        {
            "key": FIELD_TAQUEY,
            "stable_url": "https://tradocfcoeccafcoepfwprod.blob.core.usgovcloudapi.net/fires-bulletin-archive/1942/FEB_1942/FEB_1942_FULL_EDITION.pdf",
            "title": "Mountain Guns in Today's War",
            "author_creator": "Lieutenant Charles Taquey",
            "repository_publisher": "The Field Artillery Journal; U.S. Army Fires Bulletin archive",
            "publication_record_date": "1942-02",
            "locator": "Printed page 89; Lieutenant Charles Taquey, 93d Regiment of French Mountain Artillery",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "The Field Artillery Journal",
            "rights_notes": "Contemporary person-authored account of the 1940 French Army assignment.",
        },
        {
            "key": FIELD_TAQUEY_1943,
            "stable_url": "https://tradocfcoeccafcoepfwprod.blob.core.usgovcloudapi.net/fires-bulletin-archive/1943/APR_1943/APR_1943_FULL_EDITION.pdf",
            "title": "A 'Frog' at Fort Sill",
            "author_creator": "Lieutenant Charles H. Taquey",
            "repository_publisher": "The Field Artillery Journal; U.S. Army Fires Bulletin archive",
            "publication_record_date": "1943-04",
            "locator": "Printed page 255; U.S. Army enlistment, parachute training, Officer Candidate School commission and parachute field artillery service",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "The Field Artillery Journal",
            "rights_notes": "Contemporary person-authored article with an editorial note identifying Taquey's U.S. Army sequence.",
        },
        {
            "key": GOVINFO_TARASOV,
            "stable_url": "https://www.govinfo.gov/content/pkg/CPRT-76SPRT299968/pdf/CPRT-76SPRT299968.pdf",
            "archival_identifier": "76th Congress Senate Committee Print 299968",
            "title": "Description of Hearings and Monographs of the Temporary National Economic Committee",
            "author_creator": "Temporary National Economic Committee",
            "repository_publisher": "U.S. Government Printing Office; GovInfo",
            "publication_record_date": "1941",
            "locator": "PDF physical page 19, printed page 13; Helen Tarasov, Industrial Economics Division, Department of Commerce",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "Investigation of Concentration of Economic Power",
            "rights_notes": "The page was rendered and visually inspected.",
        },
        {
            "key": LEGACY_TARBERT,
            "stable_url": "https://www.legacy.com/us/obituaries/york/name/william-tarbert-obituary?id=14149832",
            "title": "William L. Tarbert obituary",
            "repository_publisher": "York Daily Record via Legacy",
            "publication_record_date": "2015-02-15",
            "locator": "Obituary; 1943 University of Maryland graduation and World War II Army/OSS service",
            "access_date": "2026-10-28",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "York Daily Record obituaries",
            "rights_notes": "Only concise project-authored paraphrases are retained; postwar employment is excluded from the claim.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": "us-army-existing-b940",
            "organization_id": "28a26f92-78af-5a1a-9c09-a843eb5975b4",
            "canonical_name": "United States Army",
            "historical_name": "Army of the United States",
            "aliases": ["U.S. Army"],
            "organization_type": "military service",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "Existing canonical organization reused.",
        },
        {
            "key": "university-colorado-existing-b940",
            "organization_id": "a8b04832-946d-527b-9c16-854d9052f157",
            "canonical_name": "University of Colorado",
            "historical_name": "University of Colorado at Boulder",
            "aliases": ["University of Colorado at Boulder", "CU Boulder"],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "Boulder",
            "state_or_region": "Colorado",
            "country": "United States",
            "normalization_notes": "Existing canonical organization reused; the Navy school is preserved in the role, not silently merged with the university.",
        },
        {
            "key": "university-maryland-existing-b940",
            "organization_id": "57b220a8-e7c0-53d8-8565-a287d3bc6bd7",
            "canonical_name": "University of Maryland",
            "historical_name": "University of Maryland",
            "aliases": [],
            "organization_type": "university",
            "sector": "academia_and_research",
            "state_or_region": "Maryland",
            "country": "United States",
            "normalization_notes": "Existing canonical organization reused; student status is not employment.",
        },
        {
            "key": "commerce-existing-b940",
            "organization_id": "2c144ed0-23ad-5a5f-aefe-cb0473b68357",
            "canonical_name": "United States Department of Commerce",
            "historical_name": "Department of Commerce, Industrial Economics Division",
            "aliases": ["Commerce Department"],
            "organization_type": "federal department",
            "sector": "federal_government",
            "country": "United States",
            "normalization_notes": "Existing canonical organization reused; the historical division remains explicit in source wording.",
        },
        {
            "key": "french-army-existing-b940",
            "organization_id": "f61aed47-47ad-5e11-82be-3835d1bc4365",
            "canonical_name": "French Army",
            "historical_name": "French Army",
            "aliases": ["Armée française"],
            "organization_type": "military service",
            "sector": "military",
            "country": "France",
            "normalization_notes": "Existing canonical organization reused; the 93d mountain-artillery regiment remains explicit in the role.",
        },
        {
            "key": "manzanar-free-press-b940",
            "canonical_name": "Manzanar Free Press",
            "historical_name": "Manzanar Free Press",
            "aliases": [],
            "organization_type": "wartime relocation-center newspaper",
            "sector": "journalism_and_media",
            "city": "Manzanar",
            "state_or_region": "California",
            "country": "United States",
            "active_dates": "1942-1945",
            "normalization_notes": "The historical newspaper and Japanese Section are preserved; no paid-employment relationship is inferred from a staff box.",
        },
        {
            "key": "lincoln-battalion-b940",
            "canonical_name": "Abraham Lincoln Battalion",
            "historical_name": "Abraham Lincoln Battalion, International Brigades",
            "aliases": ["Lincoln Battalion", "Abraham Lincoln Brigade"],
            "organization_type": "Spanish Civil War volunteer military unit",
            "sector": "military",
            "country": "Spain",
            "active_dates": "1936-1938",
            "normalization_notes": "Historical unit retained separately from later U.S. Army and OSS service.",
        },
        {
            "key": "french-foreign-service-b940",
            "canonical_name": "French Ministry of Foreign Affairs",
            "historical_name": "French foreign service",
            "aliases": ["French Foreign Service"],
            "organization_type": "national diplomatic service",
            "sector": "federal_government",
            "country": "France",
            "normalization_notes": "The source's historical wording is preserved; no modern organizational substitution is made.",
        },
    ]


def army_affiliation(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    person_id, _ = PEOPLE[row]
    student = item["relationship_type"] == "student"
    return {
        "key": f"{item['slug']}-occupation-b940",
        "person_id": person_id,
        "relationship_type": item["relationship_type"],
        "occupation": "Student; institution not recorded" if student else item["occupation"],
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
        "research_notes": "The historical category is not converted into a named employer, institution, workplace or exact title.",
    }


def substantive_affiliations() -> list[dict[str, object]]:
    return [
        {
            "key": "saburo-tani-university-colorado-b940",
            "person_id": PEOPLE[31][0],
            "organization_key": "university-colorado-existing-b940",
            "organization_name_as_found": "University of Colorado, U.S. Navy Japanese/Oriental Language School",
            "role_title": "Japanese language instructor",
            "occupation": "language instructor",
            "relationship_type": "employment",
            "start_date": "1942",
            "end_date": "1946",
            "date_precision": "The roster covers the school's 1942-1946 operation; it does not give Saburo Tani's individual start and end dates.",
            "city": "Boulder",
            "state_or_region": "Colorado",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "temporal_relation_uncertain",
            "identity_confidence": "probable",
            "claim_confidence": "medium",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "publish_qualified",
            "research_notes": "The uncommon exact name and corroborating civilian-faculty registry support a probable match. Box 765 is needed to establish the OSS sequence.",
        },
        {
            "key": "bob-tanisaki-manzanar-free-press-b940",
            "person_id": PEOPLE[33][0],
            "organization_key": "manzanar-free-press-b940",
            "organization_name_as_found": "Manzanar Free Press, Japanese Section",
            "role_title": "Staff member; later chairman of the Japanese Section",
            "occupation": "newspaper staff",
            "relationship_type": "professional_affiliation",
            "start_date": "1943-12-22",
            "end_date": "1944-06-17",
            "date_precision": "Contemporary staff boxes establish these two dated points; pay status and the exact departure date are not stated.",
            "city": "Manzanar",
            "state_or_region": "California",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "high_confidence",
            "claim_confidence": "medium",
            "source_quality": "A_direct_official",
            "publication_status": "publish_qualified",
            "research_notes": "The role is a documented pre-OSS professional affiliation, not a named employer or proof of an immediate transition.",
        },
        {
            "key": "alfred-tanz-us-army-b940",
            "person_id": PEOPLE[37][0],
            "organization_key": "us-army-existing-b940",
            "organization_name_as_found": "the army",
            "role_title": "Soldier; later captain",
            "occupation": "Army officer",
            "relationship_type": "military_assignment",
            "start_date": "1942",
            "end_date": "1942-1943",
            "date_precision": "The institutional obituary directly sequences Army enlistment and Donovan recruitment for OSS; the exact transfer date is not stated.",
            "country": "United States",
            "immediate_pre_oss": True,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "explicit_immediate",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "published",
            "research_notes": "Army service is the explicit immediate predecessor to OSS recruitment; no civilian-employer label is applied.",
        },
        {
            "key": "alfred-tanz-law-practice-b940",
            "person_id": PEOPLE[37][0],
            "role_title": "Attorney; pro bono veterans' lawyer",
            "occupation": "attorney",
            "relationship_type": "self_employment",
            "start_date": "1930s",
            "end_date": "1942",
            "date_precision": "A contemporary report identifies his New York law practice before Spain; the later institutional obituary records pro bono legal work after his 1938 return and before Army enlistment.",
            "city": "New York City",
            "state_or_region": "New York",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": True,
            "pre_oss_temporal_basis": "probable_immediate",
            "identity_confidence": "high_confidence",
            "claim_confidence": "medium",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "publish_qualified",
            "research_notes": "Modeled as self-employment/professional practice, not a named employer. The exact resumption and end dates are not documented.",
        },
        {
            "key": "alfred-tanz-lincoln-battalion-b940",
            "person_id": PEOPLE[37][0],
            "organization_key": "lincoln-battalion-b940",
            "organization_name_as_found": "Lincoln Battalion",
            "role_title": "Lieutenant; quartermaster; machine-gun company member",
            "occupation": "international volunteer",
            "relationship_type": "military_assignment",
            "start_date": "1936-12",
            "end_date": "1938-12",
            "date_precision": "The institutional obituary dates departure in December 1936, two tours in Spain and return in December 1938.",
            "country": "Spain",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "published",
            "research_notes": "Earlier pre-OSS foreign volunteer military service; kept separate from U.S. Army and OSS service.",
        },
        {
            "key": "charles-taquey-us-army-b940",
            "person_id": PEOPLE[39][0],
            "organization_key": "us-army-existing-b940",
            "organization_name_as_found": "U.S. Army",
            "role_title": "Parachute field artillery officer",
            "occupation": "Army officer",
            "relationship_type": "military_assignment",
            "start_date": "1942",
            "end_date": "1943-1945",
            "date_precision": "A 1943 Field Artillery Journal account places him in U.S. Army parachute artillery; the obituary later pairs U.S. Army and OSS service without an exact transfer date.",
            "country": "United States",
            "immediate_pre_oss": True,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "probable_immediate",
            "identity_confidence": "high_confidence",
            "claim_confidence": "medium",
            "source_quality": "A_direct_official",
            "publication_status": "publish_qualified",
            "research_notes": "A qualified U.S. Army-to-OSS pathway; the personnel file is needed for the exact transition.",
        },
        {
            "key": "charles-taquey-french-army-b940",
            "person_id": PEOPLE[39][0],
            "organization_key": "french-army-existing-b940",
            "organization_name_as_found": "5th Battalion, 93d Regiment of French Mountain Artillery",
            "role_title": "Lieutenant and liaison officer",
            "occupation": "artillery officer",
            "relationship_type": "military_assignment",
            "start_date": "1940",
            "end_date": "1940",
            "date_precision": "Taquey's contemporary article describes his headquarters liaison role in the June 1940 Alpine operations.",
            "country": "France",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "A_direct_official",
            "publication_status": "published",
            "research_notes": "Earlier documented military service, distinct from later U.S. Army and OSS assignments.",
        },
        {
            "key": "charles-taquey-french-foreign-service-b940",
            "person_id": PEOPLE[39][0],
            "organization_key": "french-foreign-service-b940",
            "organization_name_as_found": "French foreign service",
            "role_title": "Financial attaché in New York",
            "occupation": "diplomat and international economist",
            "relationship_type": "government_assignment",
            "start_date": "1937",
            "end_date": "1940",
            "date_precision": "The obituary explicitly dates the New York financial-attaché assignment to 1937-1940 and then sequences French Army service.",
            "city": "New York City",
            "state_or_region": "New York",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": True,
            "pre_oss_temporal_basis": "explicit_immediate",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "published",
            "research_notes": "Last identified civilian government employer before French Army service; kept separate from the immediate U.S. Army-to-OSS path.",
        },
        {
            "key": "helen-tarasov-commerce-b940",
            "person_id": PEOPLE[44][0],
            "organization_key": "commerce-existing-b940",
            "organization_name_as_found": "Industrial Economics Division, Department of Commerce",
            "role_title": "Industrial economist and coauthor",
            "occupation": "economist",
            "relationship_type": "government_assignment",
            "end_date": "1941",
            "date_precision": "The 1941 official committee print identifies the division and coauthorship; no exact employment dates or OSS transition are stated.",
            "city": "Washington",
            "state_or_region": "District of Columbia",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "probable",
            "claim_confidence": "medium",
            "source_quality": "A_direct_official",
            "publication_status": "publish_qualified",
            "research_notes": "Rare exact-name and wartime-economics alignment support a probable match, but Box 765 is needed for a direct OSS identity bridge.",
        },
        {
            "key": "william-tarbert-maryland-student-b940",
            "person_id": PEOPLE[45][0],
            "organization_key": "university-maryland-existing-b940",
            "organization_name_as_found": "University of Maryland",
            "role_title": "B.S. student",
            "occupation": "student",
            "relationship_type": "student",
            "end_date": "1943",
            "date_precision": "The obituary dates graduation to 1943 and identifies subsequent World War II Army/OSS service, but it does not state the exact entry date.",
            "state_or_region": "Maryland",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "high_confidence",
            "claim_confidence": "medium",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "publish_qualified",
            "research_notes": "Last documented pre-OSS student affiliation; the university is not labeled an employer.",
        },
    ]


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
    result: dict[str, object] = {
        "key": key,
        "person_id": PEOPLE[row][0],
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
    if affiliation_key:
        result["affiliation_key"] = affiliation_key
    return result


def army_identity_claim(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    _, name = PEOPLE[row]
    return claim(
        row,
        f"identity-{item['slug']}-b940",
        "identity",
        f"The indexed {name} row is a high-confidence match to the reviewed official Army record.",
        "A nonshared protected identifier connects the visually verified index row to the official Army record.",
        "High confidence from the protected-identifier bridge and exact full-name agreement.",
        "The Army record supports identity and a dated occupation category; it does not establish the OSS transfer sequence.",
        "A_direct_official",
        "high",
        [
            {"source_key": INDEX, "locator_override": f"PDF page 460 row {row}; protected identifier withheld"},
            {"source_key": ARMY, "locator_override": "Accepted reviewed identity bridge; protected identifier withheld"},
        ],
        "No protected identifier is exposed, and no employer or workplace is inferred.",
    )


def army_occupation_claim(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    _, name = PEOPLE[row]
    category = (
        "student category"
        if item["relationship_type"] == "student"
        else f"historical {str(item['occupation']).lower()} category"
    )
    return claim(
        row,
        f"occupation-{item['slug']}-b940",
        "occupation",
        f"At Army entry on {item['date']}, {name} was recorded in the {category}; no employer is identified.",
        f"The accepted Army record carries civilian-occupation code {item['code']}, decoded from NARA's official code list.",
        "The occupation belongs only to the reviewed protected-identifier match; the identifier itself is not public.",
        "Strongly date-bounded to Army entry; it does not establish the immediate pre-OSS affiliation or a named employer.",
        "A_direct_official",
        "medium",
        [
            {"source_key": ARMY, "locator_override": f"Accepted reviewed identity record; civilian occupation code {item['code']}; protected identifier withheld"},
            {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46; Army-entry-date and civilian-occupation fields"},
            {"source_key": CODES, "locator_override": item["locator"], "excerpt_override": item["occupation"]},
        ],
        "The historical category remains a qualified occupation lead, not an employer, workplace, institution or exact title.",
        f"{item['slug']}-occupation-b940",
    )


def substantive_claims() -> list[dict[str, object]]:
    return [
        claim(31, "identity-saburo-tani-b940", "identity", "Indexed Saburo Tani is a probable match to the civilian Japanese-language instructor listed at the University of Colorado wartime Navy school.", "Two institutional rosters carry the uncommon exact name and identify a civilian faculty role.", "Probable from the uncommon exact name, civilian-faculty designation and aligned wartime language work; Box 765 remains the direct OSS bridge.", "The teacher list covers 1942-1946, but the exact OSS sequence is unknown.", "B_authoritative_institutional", "medium", [{"source_key": INDEX, "locator_override": "PDF page 460 row 31; Box 765"}, {"source_key": PACIFIC_TANI, "locator_override": "PDF physical page 5"}, {"source_key": JAVA_TANI, "locator_override": "Registry row 8826"}], "Published as a qualified probable identity, excluded from default high-confidence employer analytics."),
        claim(31, "employment-saburo-tani-colorado-b940", "other_pre_oss_affiliation", "Saburo Tani is listed as a civilian teacher at the University of Colorado's U.S. Navy Japanese/Oriental Language School during 1942-1946.", "Pacific Citizen lists him among the teachers; the Army history states that the school's instructors were university employees.", "Probable identity from the uncommon exact name and corroborating civilian-faculty registry.", "Documented wartime employment, but its precise relationship to OSS service is unresolved.", "B_authoritative_institutional", "medium", [{"source_key": PACIFIC_TANI, "locator_override": "PDF physical page 5; list of teachers"}, {"source_key": JAVA_TANI, "locator_override": "Registry row 8826; Faculty; Civilian"}, {"source_key": ARMY_NISEI, "locator_override": "Printed page 150; university employment relationship"}], "The named employer is qualified because the Box 765 personnel file has not yet linked the teaching dates to OSS chronology.", "saburo-tani-university-colorado-b940"),
        claim(32, "conflict-noboru-tanimoto-tamimoto-b940", "identity", "Indexed Noboru M. Tanimoto may be the Noboru Mori Tanimoto named in a 1945 OSS order, but a separate Noboru Tamimoto row remains a competing candidate.", "The index preserves both near-identical rows; the direct OSS order supplies one expanded name but no box-level identifier.", "Ambiguous: row 32 aligns more closely with the middle initial, but no source assigns the order to either row.", "Both index rows and the OSS order are wartime records; their exact relationship is unresolved.", "A_direct_official", "conflicting", [{"source_key": INDEX, "locator_override": "PDF page 460 rows 14 and 32"}, {"source_key": OSS_ORDER, "locator_override": "PDF physical page 11; Noboru Mori Tanimoto"}], "Both source rows remain separate in one possible-duplicate group pending joint Box 764-765 review.", publication_status="conflicting"),
        claim(33, "identity-bob-fujiwo-tanisaki-b940", "identity", "Indexed Bob F. Tanisaki is a high-confidence match to Fujiwo Bob Tanisaki, named as a civilian OSS employee in April 1945.", "The index's Bob and middle F align with Fujiwo Bob in the direct OSS order; contemporary staff boxes use Fujiwo Tanisaki.", "High confidence from the unusual surname, reciprocal Bob/Fujiwo name alignment and direct wartime OSS record.", "The newspaper roles are dated December 1943 and June 1944; the OSS order is dated April 1945.", "A_direct_official", "high", [{"source_key": INDEX, "locator_override": "PDF page 460 row 33; Box 765"}, {"source_key": OSS_ORDER, "locator_override": "PDF physical page 11; Fujiwo Bob Tanisaki"}, {"source_key": MANZANAR_1943}, {"source_key": MANZANAR_1944}], "Bob F. remains the indexed display name; Fujiwo Bob and Fujiwo are documented variants."),
        claim(33, "pre-oss-bob-tanisaki-manzanar-b940", "other_pre_oss_affiliation", "Fujiwo Bob Tanisaki served on the Manzanar Free Press Japanese Section before the 1945 OSS travel order.", "Contemporary staff boxes name Fujiwo Tanisaki as a staff member in 1943 and section chairman in 1944.", "High-confidence identity from the direct OSS name expansion and the uncommon matching surname.", "Strongly date-bounded before the April 1945 OSS order, but pay status and the exact transition are not stated.", "A_direct_official", "medium", [{"source_key": MANZANAR_1943, "locator_override": "Page 4 staff box"}, {"source_key": MANZANAR_1944, "locator_override": "Page 2 staff box"}, {"source_key": OSS_ORDER, "support_type": "context_only", "locator_override": "PDF physical page 11"}], "Modeled as a professional affiliation, not a named employer or an explicitly immediate predecessor.", "bob-tanisaki-manzanar-free-press-b940"),
        claim(37, "identity-alfred-tanz-b940", "identity", "Indexed Alfred L. Tanz is a high-confidence match to the New York lawyer, Lincoln Battalion veteran, U.S. Army captain and OSS member.", "The rare exact name and middle initial align with an institutional biography that explicitly sequences Army enlistment and Donovan recruitment into OSS.", "High confidence from the rare exact name, direct OSS chronology and corroborating legal and military history.", "The sources distinguish 1930s law, 1936-1938 Spain service, 1942 Army entry and subsequent OSS recruitment.", "B_authoritative_institutional", "high", [{"source_key": INDEX, "locator_override": "PDF page 460 row 37; Box 765"}, {"source_key": ALBA_TANZ, "locator_override": "PDF physical page 20"}, {"source_key": LOC_TANZ, "support_type": "context_only"}], "The commissioned-officer classification rests on the documented U.S. Army promotion to captain, not the OSS index alone."),
        claim(37, "immediate-alfred-tanz-army-b940", "immediate_pre_oss_affiliation", "The United States Army is Alfred L. Tanz's documented immediate pre-OSS affiliation.", "The institutional obituary states that he enlisted in the Army and was recruited by William Donovan for OSS service.", "High-confidence identity from the rare exact name and explicit OSS chronology.", "Explicit immediate sequence; the exact transfer date is not stated.", "B_authoritative_institutional", "high", [{"source_key": ALBA_TANZ, "locator_override": "PDF physical page 20; Army and Donovan paragraph"}], "Modeled as a military assignment, not a civilian employer.", "alfred-tanz-us-army-b940"),
        claim(37, "last-civilian-alfred-tanz-law-b940", "last_civilian_pre_service", "Alfred L. Tanz's last identified civilian occupation before Army service was legal practice in New York, including pro bono work for veterans.", "A contemporary report calls him a New York attorney; the institutional biography records post-Spain pro bono legal work before Army enlistment.", "High-confidence identity from the rare exact name and aligned life chronology.", "Probably the last civilian occupation before Army service, but the exact practice-resumption and end dates are not documented.", "B_authoritative_institutional", "medium", [{"source_key": LOC_TANZ, "locator_override": "Page A-5; New York attorney"}, {"source_key": ALBA_TANZ, "locator_override": "PDF physical page 20; post-Spain legal work"}], "Published as self-employment/professional practice; no law firm is invented.", "alfred-tanz-law-practice-b940"),
        claim(37, "prewar-alfred-tanz-lincoln-b940", "other_pre_oss_affiliation", "Alfred L. Tanz served as a lieutenant in the Abraham Lincoln Battalion during the Spanish Civil War.", "The institutional biography dates two Spain tours from 1936 to 1938 and documents his lieutenant and unit roles.", "High-confidence identity from the rare exact name and corroborating contemporary legal/military description.", "Documented prewar military affiliation, not immediate to OSS because later legal and U.S. Army service intervened.", "B_authoritative_institutional", "high", [{"source_key": ALBA_TANZ, "locator_override": "PDF physical page 20"}, {"source_key": LOC_TANZ, "support_type": "context_only", "locator_override": "Page A-5"}], "Kept separate from later U.S. Army and OSS service.", "alfred-tanz-lincoln-battalion-b940"),
        claim(38, "conflict-ruby-tape-joseph-army-b940", "identity", "Ruby K. Tape's indexed row has conflicting identity evidence: an exact-name military-intelligence biography aligns contextually, but the protected identifier points to a different Army name.", "A Cathay Post account describes Ruby Kim Tape in WAC intelligence; the official Army candidate carries a materially different full name.", "Conflicting. Exact rare-name context cannot override a substantive protected-identifier name conflict.", "No Army occupation, date or assignment is transferred while identity remains conflicting.", "A_direct_official", "conflicting", [{"source_key": INDEX, "locator_override": "PDF page 460 row 38; protected identifier withheld"}, {"source_key": ARMY, "support_type": "contradicts", "locator_override": "Conflicting official candidate; protected identifier withheld"}, {"source_key": RUBY_TAPE, "support_type": "context_only", "locator_override": "PDF physical pages 10-11"}], "Review Box 765 before correcting an identifier or assigning the WAC biography to this row.", publication_status="conflicting"),
        claim(39, "identity-charles-henri-taquey-b940", "identity", "Indexed Charles H. Taquey is a high-confidence match to Charles Henri Taquey, the French and U.S. Army officer who served with OSS.", "The exact surname, middle-name expansion, French artillery article and obituary's direct Army/OSS chronology align.", "High confidence from the unusual exact name, matching middle initial, first-person military source and explicit OSS obituary.", "The sources sequence 1937-1940 diplomacy, 1940 French Army service and later U.S. Army/OSS service.", "A_direct_official", "high", [{"source_key": INDEX, "locator_override": "PDF page 460 row 39; Box 765"}, {"source_key": FIELD_TAQUEY, "locator_override": "Printed page 89"}, {"source_key": WP_TAQUEY, "locator_override": "Charles Henri Taquey obituary section"}], "Henri is retained as a documented middle-name expansion."),
        claim(39, "immediate-charles-taquey-us-army-b940", "immediate_pre_oss_affiliation", "Charles H. Taquey's best-supported immediate pre-OSS affiliation is the United States Army, where he served in parachute field artillery.", "A contemporary Army journal identifies his U.S. enlistment and commission; the obituary pairs U.S. Army and OSS service.", "High-confidence identity from the rare exact name and aligned French/U.S. military chronology.", "Probable immediate sequence; the accessible sources do not give an exact Army-to-OSS transfer date.", "A_direct_official", "medium", [{"source_key": FIELD_TAQUEY_1943, "locator_override": "Printed page 255"}, {"source_key": WP_TAQUEY}], "Published as a qualified military pathway, not a settled transfer date.", "charles-taquey-us-army-b940"),
        claim(39, "prewar-charles-taquey-french-army-b940", "other_pre_oss_affiliation", "Charles Taquey served as a French Army lieutenant and liaison officer with the 93d Regiment of Mountain Artillery in 1940.", "His contemporary article identifies his rank, regiment and headquarters liaison role during the Alpine operations.", "High-confidence identity from the exact name, matching middle initial and first-person military account.", "Explicitly dated to the June 1940 Alpine campaign, before later U.S. Army and OSS service.", "A_direct_official", "high", [{"source_key": FIELD_TAQUEY, "locator_override": "Printed page 89"}, {"source_key": WP_TAQUEY, "support_type": "context_only"}], "Earlier foreign military assignment, kept separate from the U.S. Army-to-OSS pathway.", "charles-taquey-french-army-b940"),
        claim(39, "last-civilian-charles-taquey-french-service-b940", "last_civilian_pre_service", "The French foreign service was Charles Henri Taquey's last identified civilian employer before military service.", "The obituary dates his New York financial-attaché assignment to 1937-1940 and directly sequences French Army service.", "High-confidence identity from the rare exact name and explicit French/U.S. Army and OSS chronology.", "Explicit last civilian government assignment before French Army service in 1940.", "C_reputable_contemporary_or_scholarly", "high", [{"source_key": WP_TAQUEY, "locator_override": "Charles Henri Taquey obituary section"}], "Government assignment is kept distinct from military service and from the later OSS role.", "charles-taquey-french-foreign-service-b940"),
        claim(43, "identity-mario-tarantino-army-b940", "identity", "The indexed Mario Tarantino row is a high-confidence match to the reviewed official Army record.", "A nonshared protected identifier and exact full name connect the index row to the Army record.", "High confidence from the protected-identifier bridge and exact name agreement.", "The official record dates Army entry to 1943-12-05; its occupation code is not interpreted or published.", "A_direct_official", "high", [{"source_key": INDEX, "locator_override": "PDF page 460 row 43; protected identifier withheld"}, {"source_key": ARMY, "locator_override": "Accepted reviewed identity bridge; protected identifier withheld"}], "No employer, workplace or occupation is inferred from the uninterpreted code."),
        claim(44, "identity-helen-tarasov-b940", "identity", "Indexed Helen Tarasov is a probable match to the Department of Commerce economist named in a 1941 federal committee print.", "The rare exact name and wartime federal economics role align with the index, but no second person-specific OSS identifier is accessible.", "Probable, not high confidence; Box 765 remains necessary for the direct identity bridge.", "The Department of Commerce affiliation is documented in 1941, but its sequence relative to OSS is unknown.", "A_direct_official", "medium", [{"source_key": INDEX, "locator_override": "PDF page 460 row 44; Box 765"}, {"source_key": GOVINFO_TARASOV, "locator_override": "PDF physical page 19, printed page 13"}], "Visibly qualified and excluded from default high-confidence employer analytics."),
        claim(44, "prewar-helen-tarasov-commerce-b940", "other_pre_oss_affiliation", "A 1941 federal committee print identifies Helen Tarasov with the Industrial Economics Division of the Department of Commerce.", "The official publication credits her by exact name and division on the tax-distribution monograph.", "Probable identity from a rare exact name and compatible wartime federal role; the personnel file remains unreviewed.", "Documented in 1941, but not shown to be the immediate predecessor to OSS service.", "A_direct_official", "medium", [{"source_key": GOVINFO_TARASOV, "locator_override": "PDF physical page 19, printed page 13"}], "Published as a qualified documented prewar government affiliation, not an immediate-employer claim.", "helen-tarasov-commerce-b940"),
        claim(45, "identity-william-tarbert-b940", "identity", "Indexed William L. Tarbert is a high-confidence match to the University of Maryland graduate and World War II Army/OSS veteran.", "The exact full name and middle initial, age-compatible 1943 graduation and explicit Army/OSS service align.", "High confidence from the uncommon exact name and direct OSS chronology; Box 765 remains unreviewed.", "The obituary places graduation in 1943 and Army/OSS service during World War II without an exact entry date.", "C_reputable_contemporary_or_scholarly", "high", [{"source_key": INDEX, "locator_override": "PDF page 460 row 45; Box 765"}, {"source_key": LEGACY_TARBERT}], "Postwar employment details are not used to reconstruct the pre-OSS period."),
        claim(45, "pre-oss-william-tarbert-maryland-b940", "other_pre_oss_affiliation", "University of Maryland student status is William L. Tarbert's last documented affiliation before his Army/OSS service.", "The obituary dates his B.S. graduation to 1943 and identifies World War II Army/OSS service.", "High-confidence identity from the exact name and direct OSS chronology.", "Strongly date-bounded, but not explicitly stated as the immediate predecessor to service.", "C_reputable_contemporary_or_scholarly", "medium", [{"source_key": LEGACY_TARBERT}], "Student status is not employment, and the university is not counted as an employer.", "william-tarbert-maryland-student-b940"),
    ]


def archival_update(row: int, reason: str) -> dict[str, object]:
    person_id, name = PEOPLE[row]
    return {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, Box 765 and archive location 230/86/41/07. {reason}",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": "Review Box 765 for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }


def person_updates() -> list[dict[str, object]]:
    updates = [archival_update(row, reason) for row, reason in UNRESOLVED.items()]
    for item in ARMY_OCCUPATIONS:
        row = int(item["row"])
        updates.append(
            {
                "person_id": PEOPLE[row][0],
                "identity_status": "high_confidence",
                "identity_evidence": "A nonshared protected identifier and exact name connect the visually verified index row to the reviewed official Army record. The historical occupation field remains separate from employer and immediate-affiliation claims.",
                "personnel_category": "enlisted_army_personnel",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "occupation_only_found",
                "next_action": "Review Box 765 to identify the immediate pre-OSS affiliation and last civilian employer; do not convert the Army category into a named employer or institution.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            }
        )
    updates.extend(
        [
            {"person_id": PEOPLE[31][0], "identity_status": "probable", "identity_evidence": "The uncommon exact name appears in two institutional wartime language-school rosters, including a civilian-faculty designation. No direct Box 765 or OSS order yet proves the match.", "personnel_category": "civilian_professional_or_administrative_grade", "commissioned_officer": False, "allied_or_foreign_personnel": False, "manual_review_required": True, "research_status": "documented_prewar_employer_found", "next_action": "Review Box 765 for a direct identity bridge, individual University of Colorado employment dates and the sequence into OSS service.", "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "high"},
            {"person_id": PEOPLE[32][0], "identity_status": "ambiguous", "identity_evidence": "The index separately prints Noboru M Tanimoto and Noboru Tamimoto, while a direct OSS order names Noboru Mori Tanimoto. The order cannot determine which row it represents.", "manual_review_required": True, "possible_duplicate_group": "page460-noboru-tamimoto-tanimoto-rows14-32", "research_status": "conflicting_sources", "next_action": "Review the Noboru Tamimoto Box 764 file and Noboru M Tanimoto Box 765 file together. Keep both rows separate unless direct evidence proves duplication.", "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "critical"},
            {"person_id": PEOPLE[33][0], "identity_status": "high_confidence", "identity_evidence": "The index's Bob and middle F align with Fujiwo Bob Tanisaki in a direct 1945 OSS order; contemporary Manzanar Free Press staff boxes use Fujiwo Tanisaki.", "name_variants": ["Fujiwo Bob Tanisaki", "Fujiwo Tanisaki"], "personnel_category": "civilian_professional_or_administrative_grade", "commissioned_officer": False, "allied_or_foreign_personnel": False, "manual_review_required": True, "research_status": "completed", "next_action": "Review Box 765 for the exact Manzanar-to-OSS chronology, employment status and any intervening affiliation.", "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "medium"},
            {"person_id": PEOPLE[37][0], "identity_status": "high_confidence", "identity_evidence": "The rare exact name and middle initial align with an institutional biography that explicitly sequences New York legal work, Lincoln Battalion service, Army enlistment and Donovan recruitment into OSS.", "name_variants": ["Al Tanz"], "personnel_category": "commissioned_army_officer", "commissioned_officer": True, "allied_or_foreign_personnel": False, "manual_review_required": True, "research_status": "completed", "next_action": "Review Box 765 for the exact Army-to-OSS transfer date and the administrative status of his OSS service; seek a dated law-practice record if available.", "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "medium"},
            {"person_id": PEOPLE[38][0], "identity_status": "conflicting", "identity_evidence": "An exact-name WAC intelligence biography plausibly fits the index context, but the row's protected identifier points to an official Army record under the materially different name Joseph Joseph W.", "name_variants": ["Ruby Kim Tape"], "manual_review_required": True, "possible_duplicate_group": "identifier-conflict:ruby-k-tape-joseph-joseph-w", "research_status": "conflicting_sources", "next_action": "Review Box 765 before correcting the index identifier, accepting the Army record or assigning the Ruby Kim Tape biography.", "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "critical"},
            {"person_id": PEOPLE[39][0], "identity_status": "high_confidence", "identity_evidence": "The rare exact surname and middle-name expansion align with a first-person French artillery article and an obituary that explicitly sequences French service, U.S. Army service and OSS work.", "name_variants": ["Charles Henri Taquey"], "personnel_category": "commissioned_army_officer", "commissioned_officer": True, "allied_or_foreign_personnel": False, "manual_review_required": True, "research_status": "documented_prewar_employer_found", "next_action": "Review Box 765 for the exact U.S. Army-to-OSS transfer date and assignment; seek French diplomatic personnel records for precise attaché dates.", "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "medium"},
            {"person_id": PEOPLE[43][0], "identity_status": "high_confidence", "identity_evidence": "A nonshared protected identifier and exact name connect the visually verified index row to the reviewed official Army record. Its occupation code remains uninterpreted and unpublished.", "personnel_category": "enlisted_army_personnel", "commissioned_officer": False, "allied_or_foreign_personnel": False, "manual_review_required": True, "research_status": "completed", "next_action": "Review Box 765 for the immediate pre-OSS affiliation, last civilian employer and meaning of the disputed or undocumented occupation code.", "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "high"},
            {"person_id": PEOPLE[44][0], "identity_status": "probable", "identity_evidence": "A 1941 federal committee print identifies the rare exact name Helen Tarasov with the Department of Commerce Industrial Economics Division, but no second identifier links that economist directly to Box 765.", "personnel_category": "civilian_professional_or_administrative_grade", "commissioned_officer": False, "allied_or_foreign_personnel": False, "manual_review_required": True, "research_status": "documented_prewar_employer_found", "next_action": "Review Box 765 for a direct identity bridge, Commerce employment dates and the transition to OSS.", "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "high"},
            {"person_id": PEOPLE[45][0], "identity_status": "high_confidence", "identity_evidence": "The exact full name and middle initial, age-compatible 1943 University of Maryland graduation and explicit World War II Army/OSS service form a coherent identity bridge.", "name_variants": ["William L. 'Bill' Tarbert", "Bill Tarbert"], "manual_review_required": True, "research_status": "completed", "next_action": "Review Box 765 for Army rank, the exact service-entry date and whether University of Maryland immediately preceded OSS or an intervening Army assignment.", "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "medium"},
        ]
    )
    return updates


def research_attempts() -> list[dict[str, object]]:
    substantive = {
        31: ("source_reviewed", 9, 4, "Institutional rosters support a probable civilian University of Colorado language-school employment match; the OSS sequence remains unresolved."),
        32: ("candidate_found", 9, 5, "The direct OSS order creates a visible possible-duplicate conflict with the separately indexed Noboru Tamimoto row; no merge was made."),
        33: ("source_reviewed", 10, 4, "A direct OSS order and two contemporary Manzanar Free Press staff boxes support the Fujiwo Bob Tanisaki identity and pre-OSS professional affiliation."),
        35: ("source_reviewed", 8, 4, "An accepted protected-identifier Army bridge supports identity and a dated general-farm-hand occupation category, not an employer."),
        37: ("source_reviewed", 12, 4, "Institutional and contemporary sources support a high-confidence lawyer, Lincoln Battalion, Army and OSS chronology."),
        38: ("candidate_found", 9, 6, "An exact-name WAC intelligence biography remains unassigned because the protected identifier points to a materially different Army name."),
        39: ("source_reviewed", 12, 4, "A first-person military article and a reputable obituary support the French diplomatic, French Army, U.S. Army and OSS chronology."),
        41: ("source_reviewed", 8, 4, "An accepted protected-identifier Army bridge supports identity and student status at Army entry, not a school or employer."),
        43: ("source_reviewed", 7, 4, "An accepted protected-identifier Army bridge supports identity; the uninterpreted occupation code was withheld."),
        44: ("source_reviewed", 9, 5, "An official 1941 source supports a probable Department of Commerce affiliation; Box 765 remains the direct identity bridge."),
        45: ("source_reviewed", 9, 4, "A reputable obituary supports a high-confidence University of Maryland student-to-Army/OSS chronology without treating the university as an employer."),
    }
    attempts: list[dict[str, object]] = []
    for row in sorted(PEOPLE):
        person_id, name = PEOPLE[row]
        if row in UNRESOLVED:
            outcome, reviewed, rejected, detail = "no_result", 7, 5, UNRESOLVED[row]
        else:
            outcome, reviewed, rejected, detail = substantive[row]
        attempts.append(
            {
                "key": f"page460-row{row}-{slug(name)}-b940",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA index and public Archives context; CIA Reading Room and CIA exact-name discovery; OSS, rank and spelling variants; employer and occupation 1940; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Box 765; protected identifiers used privately only when defensible",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_940",
                "started_at": "2026-10-28T05:45:00Z",
                "completed_at": "2026-10-28T08:15:00Z",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search snippets, family-tree assertions, modern people-finder pages, postwar-only leads and sources without an OSS, protected-identifier or Box-file bridge were not assigned.",
                "research_notes": f"{detail} The index page and admitted PDF pages were visually checked. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": "Review Box 765 for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before military service.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b940-v1",
            }
        )
    return attempts


def main() -> None:
    affiliations = [army_affiliation(item) for item in ARMY_OCCUPATIONS]
    affiliations += substantive_affiliations()
    claims = [army_identity_claim(item) for item in ARMY_OCCUPATIONS]
    claims += [army_occupation_claim(item) for item in ARMY_OCCUPATIONS]
    claims += substantive_claims()
    bundle = {
        "bundle_version": "batch-940-v1",
        "reviewer": "Before OSS Batch 940 evidence review",
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
