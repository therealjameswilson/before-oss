#!/usr/bin/env python3
"""Generate the reviewed Batch 1006 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page496-weisch-to-wellman-"
    "review_batch-1006_2026-11-03.json"
)

INDEX = "nara-index-b1006"
ARMY = "army-bulk-b1006"
TECH = "army-tech-b1006"
CODES = "army-codes-b1006"
NARA_AWARDS = "nara-oss-awards-b1006"
WEISMILLER_OBIT = "monticello-weismiller-b1006"
CORNELL_WEISMILLER = "cornell-weismiller-b1006"
SENTINEL_WEISGAL = "sentinel-weisgal-b1006"
WAPO_BENJAMIN = "wapo-benjamin-welles-b1006"
WAPO_EDWARD = "wapo-edward-welles-b1006"
CRIMSON_WELD = "crimson-philip-weld-b1006"
MATHER_WELLEMEYER = "mather-wellemeyer-b1006"

ORG_HARVARD = "harvard-b1006"
ORG_RANDOM_HOUSE = "random-house-b1006"
ORG_CORNELL_COLLEGE = "cornell-college-b1006"
ORG_OXFORD = "oxford-b1006"
ORG_NYT = "new-york-times-b1006"
ORG_ARMY = "us-army-b1006"
ORG_YALE = "yale-b1006"
ORG_BRITISH_INTELLIGENCE = "british-intelligence-unspecified-b1006"
ORG_BRYN_MAWR = "bryn-mawr-b1006"


# Rows 7 and 8 were manually resolved to one person entity. Row 7 is the
# canonical key below, and both immutable source rows remain linked in SQLite.
PEOPLE = {
    1: ("9637eb7f-fd8b-591d-961c-07b57e8d9096", "William S Weisch"),
    2: ("a3862cc4-56d0-509d-af6e-6cbb352f2da0", "Willis Weisenborn"),
    3: ("e14df31e-236d-53f3-a4e3-626965df7a95", "Paul R Weisenford"),
    4: ("1e7f7717-f628-5999-bded-cbf57a761ec1", "Emanuel Weisgal"),
    5: ("a93ce7da-b421-5fcf-bfee-efafad927472", "Jacob Weisman"),
    6: ("c77ecc8d-345c-5189-9ed8-a8027272b351", "Edwin Weismantel"),
    7: ("22fa4603-6ad9-5a98-be2b-c2f3a3a88a14", "Edward Ronald Weismiller"),
    9: ("ca18d8c7-089b-5ff5-91b5-7f63233923ed", "Edward E Weiss"),
    10: ("a7945de2-80cd-5d70-aae0-9eaf866bd91d", "Harry Weiss"),
    11: ("eeb310fa-1944-5a96-9212-027020f49ad7", "Karl Weiss"),
    12: ("7c1acf69-cc93-521c-93b3-e43a4aa6232e", "Rudi Weiss"),
    13: ("2ee57559-2ce6-5e46-8848-c2a67d85a93d", "Sendor Weiss"),
    14: ("1d342508-e680-5225-8071-2c75faa82694", "William P Weiss"),
    15: ("246f2907-7acd-5948-a63e-9e4e99c5b0cc", "Russell G Weissinger"),
    16: ("c6f635c3-896e-5df3-b150-1e24386ffdfd", "Russell G Weissinger"),
    17: ("93a1ba96-127b-54e6-a363-ef67b0ae534a", "Aaron Weissman"),
    18: ("a300df26-e40b-5e5e-b31b-ac36c2be6432", "Bessie Weissman"),
    19: ("4f4025b2-b66b-57aa-94b6-93fbea65a5c2", "Ferdinand Weiszmann"),
    20: ("3797df38-fe99-52d2-9e81-f59e67d3f3d0", "Helen C Weitzel"),
    21: ("9f0fbc25-551e-58f5-ac40-e90147bd5176", "Benjamin Weitzner"),
    22: ("ffb9bbf5-6ce0-5baf-ab96-104e73a398fc", "Richard A Wejmar"),
    23: ("80ca1776-8667-5939-8f3a-5712c5126776", "Charles P Welbon"),
    24: ("10e1db43-0ff5-5dd5-8220-a3059c6d6d68", "Emily Welborn"),
    25: ("7a004eec-ed3f-553d-a6e4-45780ae6e50d", "Caroline H Welch"),
    26: ("808a46e0-d844-5437-89a3-6449c92cd14a", "Edward J Welch"),
    27: ("7d07895d-cd12-54db-83f7-65f4c22824b7", "James S Welch"),
    28: ("01467b07-f41e-5452-863d-8114b52a1184", "John F Welch"),
    29: ("3ceb7696-7c1a-5f4c-8ad2-7f7d2f5ee07b", "John F Welch"),
    30: ("7a2a94d6-06f0-555b-81b6-efaf7b6a00f1", "Joseph H Welch"),
    31: ("08383c20-3c71-5753-b56a-0679d25be7b6", "Richard E Welch"),
    32: ("c1e94569-7096-530f-b753-811f6d009022", "Wallace C Welch"),
    33: ("8eed9943-03da-5666-a317-f9daf372b463", "John D Welchel"),
    34: ("f81ffd12-2b4e-5bfc-b7ca-97b74f583dcf", "Marie F Welcome"),
    35: ("933646ec-234f-5c2e-ac61-7abc2f7657c1", "Jerome H Weld"),
    36: ("3c8d0cb6-6673-54f8-bdf9-4f4b4b6438c9", "Philip S Weld"),
    37: ("c522721c-6d0c-51d8-b0d4-72eb9101bb01", "Henry H Weldon"),
    38: ("dbb89959-c2c2-5271-bb69-cf37c1670a93", "Ella Welker"),
    39: ("d4cd2777-53b5-5d78-be57-a445464317a3", "David M Well"),
    40: ("423b1e4a-f36c-5191-a377-f99b529f5979", "Clement F Wellein"),
    41: ("1b059e1e-f463-5175-90a2-efa55e940ffc", "Marilyn R Wellemeyer"),
    42: ("fe98259e-0671-5ebb-a1a1-e3b6f7c06e47", "Benjamin Welles"),
    43: ("3441c9db-b396-5d18-a62a-2f9b27c10975", "Charles B Welles"),
    44: ("6ec0023a-4cae-53a3-bc69-7a3b3891f415", "Edward O Welles"),
    45: ("64a3024e-c2cd-5209-8af7-8b968218d485", "Walter C Wellman"),
    46: ("13d07abd-6746-5708-923d-b56d63621f34", "Walter J Wellman"),
}


ARMY_MATCHES = {
    3: {"date": "1942-01-06", "code": "736", "occupation": "chauffeur or driver", "label": "Chauffeurs and drivers, bus, taxi, truck, and tractor", "locator": "PDF physical page 177; historical category 7-36", "identity": "high_confidence", "publish": True, "detail": "The Army name field is damaged as WEISENFORD P UL R."},
    10: {"date": "1943-05-07", "code": "170", "occupation": "sales clerk", "label": "Sales clerks", "locator": "PDF physical page 172; historical category 1-70", "identity": "confirmed", "publish": True, "detail": "The indexed and Army names agree exactly."},
    12: {"date": "1943-03-18", "code": "459", "occupation": "leather-manufacturing occupation", "label": "Skilled occupations in manufacture of leather and leather products, n.e.c.", "locator": "PDF physical page 173; historical category 4-59", "identity": "confirmed", "publish": True, "detail": "The exact name, corporal rank, and nonshared protected identifier agree; an OSS citation independently confirms the same combination."},
    13: {"date": "1942-07-18", "code": "072", "occupation": "retail manager", "label": "Managers and officials, n.e.c. - retail trade", "locator": "PDF physical page 171; historical category 0-72", "identity": "high_confidence", "publish": True, "detail": "The protected identifier agrees; the Army record uses Sandor rather than indexed Sendor."},
    16: {"date": "1942-12-29", "code": "586", "occupation": "photographic-process occupation", "label": "Skilled occupations in production of photographic apparatus, n.e.c.", "locator": "PDF physical page 175; historical category 5-86", "identity": "confirmed", "publish": True, "detail": "The indexed and Army names agree exactly."},
    17: {"date": "1942-12-12", "code": "056", "occupation": "photographer", "label": "Photographers", "locator": "PDF physical page 171; historical category 0-56", "identity": "confirmed", "publish": True, "detail": "The indexed and Army names agree exactly."},
    23: {"date": "1943-01-05", "code": "133", "occupation": "secretary", "label": "Secretaries", "locator": "PDF physical page 172; historical category 1-33", "identity": "confirmed", "publish": True, "detail": "The indexed and Army names agree exactly."},
    27: {"date": "1943-07-01", "code": "992", "occupation": "student", "label": "Students", "locator": "PDF physical page 304; amended historical category 9-92", "identity": "confirmed", "publish": True, "detail": "The indexed and Army names agree exactly."},
    29: {"date": "1942-07-29", "code": "221", "occupation": "bartender", "label": "Bartenders", "locator": "PDF physical page 172; historical category 2-21", "identity": "confirmed", "publish": True, "detail": "The protected identifier distinguishes this John F Welch row from the separately printed row 28."},
    30: {"date": "1945-03-12", "code": "097", "occupation": "manager or official, n.e.c.", "label": "Managers and officials, n.e.c.", "locator": "PDF physical page 171; historical category 0-97", "identity": "high_confidence", "publish": False, "detail": "The protected identifier agrees but the Army surname field is damaged; the chronology to OSS is unresolved."},
    31: {"date": "1942-12-04", "code": "992", "occupation": "student", "label": "Students", "locator": "PDF physical page 304; amended historical category 9-92", "identity": "high_confidence", "publish": True, "detail": "The protected identifier and surname agree; the Army given name is damaged and adds Jr."},
    33: {"date": "1942-05-04", "code": "581", "occupation": "motor-vehicle mechanic", "label": "Mechanics and repairmen, motor vehicle", "locator": "PDF physical page 175; historical category 5-81", "identity": "confirmed", "publish": True, "detail": "The indexed and Army names agree exactly."},
    40: {"date": "1942-11-13", "code": "170", "occupation": "sales clerk", "label": "Sales clerks", "locator": "PDF physical page 172; historical category 1-70", "identity": "confirmed", "publish": True, "detail": "The indexed and Army names agree exactly."},
}


PRINTED_CATEGORY = {
    7: ("commissioned_marine_corps_officer", True),
    12: ("enlisted_army_personnel", False),
    21: ("civilian_professional_or_administrative_grade", False),
    32: ("commissioned_army_officer", True),
    35: ("enlisted_naval_personnel", False),
    37: ("commissioned_army_officer", True),
    42: ("commissioned_army_officer", True),
}

DUPLICATE_GROUPS = {
    15: "name-only:russell-g-weissinger-page496",
    16: "name-only:russell-g-weissinger-page496",
    28: "name-only:john-f-welch-page496",
    29: "name-only:john-f-welch-page496",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def box_for(row: int) -> str:
    return "824" if row <= 31 else "825"


def row_locator(row: int) -> str:
    return "PDF page 496 rows 7-8" if row == 7 else f"PDF page 496 row {row}"


def unresolved_reason(row: int) -> str:
    base = (
        "Exact-name and meaningful-variant searches across the NARA index context, "
        "CIA Reading Room, Library of Congress, OSS, employment, occupation, obituary, "
        "institutional, newspaper, directory, and archival sources produced no reliable "
        "identity and pre-OSS affiliation bridge; unbridged namesakes were rejected."
    )
    special = {
        14: "Two Library of Congress newspaper candidates concern attorney and author William S. Weiss, not indexed William P. Weiss; both were rejected. ",
        15: "This separately printed Russell G. Weissinger row has no protected identifier and is not merged with row 16. ",
        28: "This separately printed John F. Welch row has a different protected identifier from row 29 and remains distinct. ",
        38: "Multiple incompatible Ella Welker biographies were found, including a Mormon mission clerk and a Ryan Aircraft worker; neither has an OSS or Box 825 bridge. ",
        43: "A Charles B. Welles aviator died in 1928 and is not the indexed wartime person. ",
        45: "Walter C. Wellman namesakes include a man who died in 1940; no Box 825 bridge identifies the indexed person. ",
        46: "A postwar Lieutenant Colonel Walter J. Wellman lead lacks the protected identifier, OSS context, or Box 825 bridge needed for attribution. ",
    }
    return special.get(row, "") + base


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 824-825",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 496, rows 1-46",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 46 printed rows remain recoverable. Rows 7 and 8 are explicitly linked to one reviewed person entity; full protected identifiers remain private.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; 16 eligible protected-identifier comparisons; identifiers and record ordinals withheld",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "Thirteen identity bridges were accepted. No Army record is treated as a named employer, institution, or exact OSS-transfer record.",
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
            "locator": "PDF physical pages 171-177 and 304; reviewed historical civilian-occupation categories",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical labels identify broad occupations or student status, not named employers, institutions, workplaces, or exact OSS-transfer dates.",
        },
        {
            "key": NARA_AWARDS,
            "stable_url": "https://www.archives.gov/files/research/jfk/releases/104-10165-10120.pdf",
            "archival_identifier": "JFK release 104-10165-10120",
            "title": "Office of Strategic Services Award Recommendations and Citations",
            "author_creator": "Office of Strategic Services",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1945",
            "locator": "PDF physical page 82, Rudi Weiss citation; physical page 109, Benjamin Welles and Edward R. Weismiller entries",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "John F. Kennedy Assassination Records Collection",
            "document_number": "104-10165-10120",
            "rights_notes": "The relevant pages were OCR-located, rendered from the original scan, and visually inspected. Protected service numbers are not reproduced.",
        },
        {
            "key": WEISMILLER_OBIT,
            "stable_url": "https://www.monticellohistoricalsociety.org/obituaries/Weismiller%2C%20Edward%20R.pdf",
            "title": "Edward Ronald Weismiller, Aug. 3, 1915-Aug. 25, 2010",
            "repository_publisher": "Monticello Historical Society",
            "publication_record_date": "2010",
            "locator": "Single-page biographical obituary; Harvard teaching, Random House translation, and OSS recruitment paragraphs",
            "access_date": "2026-11-03",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Monticello-area obituaries",
            "rights_notes": "The locally downloaded page was rendered and visually inspected. Public excerpts remain under 25 words.",
        },
        {
            "key": CORNELL_WEISMILLER,
            "stable_url": "https://news.cornellcollege.edu/2010/Fall/edward-r-weismiller-38.html",
            "title": "Edward R. Weismiller '38",
            "author_creator": "Dee Ann Rexroat",
            "repository_publisher": "Cornell College",
            "publication_record_date": "2010-10-30",
            "locator": "In Memoriam biography, paragraphs on education and OSS counterespionage",
            "access_date": "2026-11-03",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Cornell College News",
        },
        {
            "key": SENTINEL_WEISGAL,
            "stable_url": "https://www.idaillinois.org/digital/api/collection/p16614coll14/id/64947/download",
            "archival_identifier": "Illinois Digital Archives item 64947",
            "title": "The Sentinel, December 10, 1942",
            "repository_publisher": "The Sentinel; Illinois Digital Archives",
            "publication_record_date": "1942-12-10",
            "locator": "PDF page 10, 'Stage and Screen' column",
            "access_date": "2026-11-03",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "The Sentinel",
            "rights_notes": "The page was downloaded, rendered, and visually checked. The article establishes a Harvard student lead, not an employer or direct OSS identity bridge.",
        },
        {
            "key": WAPO_BENJAMIN,
            "stable_url": "https://www.washingtonpost.com/archive/local/2002/01/03/benjamin-welles-85/ae3de8be-ade6-4155-b20d-7dcf3029140b/",
            "title": "Benjamin Welles, 85",
            "repository_publisher": "The Washington Post",
            "publication_record_date": "2002-01-03",
            "locator": "Obituary paragraphs on Harvard, The New York Times, Army, and OSS service",
            "access_date": "2026-11-03",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Washington Post archive",
        },
        {
            "key": WAPO_EDWARD,
            "stable_url": "https://www.washingtonpost.com/archive/local/2006/10/20/gun-control-advocate-edward-welles-85/3c53858a-ae3f-4d8d-8406-8d08fdbbfc70/",
            "title": "Gun-Control Advocate Edward Welles, 85",
            "author_creator": "Matt Schudel",
            "repository_publisher": "The Washington Post",
            "publication_record_date": "2006-10-19",
            "locator": "Biographical paragraphs on Yale, ambulance driving, British intelligence, and OSS service",
            "access_date": "2026-11-03",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Washington Post archive",
        },
        {
            "key": CRIMSON_WELD,
            "stable_url": "https://www.thecrimson.com/article/1984/11/8/famed-sailor-philip-s-weld-dies/",
            "title": "Famed Sailor Philip S. Weld Dies at 69",
            "author_creator": "Nicholas P. Caros",
            "repository_publisher": "The Harvard Crimson",
            "publication_record_date": "1984-11-08",
            "locator": "Opening and career paragraphs",
            "access_date": "2026-11-03",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "The Harvard Crimson archive",
            "rights_notes": "Supports a qualified Harvard and wartime-service lead; it does not independently establish OSS service.",
        },
        {
            "key": MATHER_WELLEMEYER,
            "stable_url": "https://www.matherhodge.com/obituaries/Marilyn-Ruth-Wellemeyer?obId=27304483",
            "title": "Marilyn Ruth Wellemeyer Obituary",
            "repository_publisher": "The Mather-Hodge Funeral Home",
            "publication_record_date": "2019-12-01",
            "locator": "Biographical paragraphs on Bryn Mawr, the Sorbonne, and 1947 central-intelligence work",
            "access_date": "2026-11-03",
            "source_quality": "D_correlative_or_secondary",
            "collection_name": "Obituary archive",
            "rights_notes": "The exact rare name and central-intelligence chronology are strong identity clues, but the indexed file's relationship to the OSS period still requires archival review.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {"key": ORG_HARVARD, "organization_id": "45ddf347-21c6-59f5-a8ae-517418adf941", "canonical_name": "Harvard University", "historical_name": "Harvard University", "aliases": ["Harvard"], "organization_type": "university", "sector": "academia_and_research", "city": "Cambridge", "state_or_region": "Massachusetts", "country": "United States", "normalization_notes": "Employment and student relationships are modeled separately."},
        {"key": ORG_RANDOM_HOUSE, "canonical_name": "Random House", "historical_name": "Random House", "aliases": [], "organization_type": "publisher", "sector": "journalism_and_media", "city": "New York", "state_or_region": "New York", "country": "United States", "normalization_notes": "Preserves the publisher name used in the biographical source; no modern parent is substituted."},
        {"key": ORG_CORNELL_COLLEGE, "canonical_name": "Cornell College", "historical_name": "Cornell College", "aliases": [], "organization_type": "college", "sector": "academia_and_research", "city": "Mount Vernon", "state_or_region": "Iowa", "country": "United States", "normalization_notes": "Distinct from Cornell University; modeled only as student affiliation."},
        {"key": ORG_OXFORD, "organization_id": "2541747c-7e73-57f7-9369-83da5b0abfac", "canonical_name": "University of Oxford", "historical_name": "Oxford University", "aliases": ["Oxford"], "organization_type": "university", "sector": "academia_and_research", "city": "Oxford", "country": "United Kingdom", "normalization_notes": "Student status is not employment."},
        {"key": ORG_NYT, "organization_id": "9904e836-9d45-5ba0-ba26-035a375d8d6f", "canonical_name": "The New York Times", "historical_name": "The New York Times", "aliases": ["New York Times", "the Times"], "organization_type": "newspaper", "sector": "journalism_and_media", "city": "New York", "state_or_region": "New York", "country": "United States", "normalization_notes": "Reuses the reviewed historical newspaper organization."},
        {"key": ORG_ARMY, "organization_id": "24facf23-e75a-54f2-a37a-0ef1509bc18a", "canonical_name": "United States Army", "historical_name": "U.S. Army", "aliases": ["Army of the United States"], "organization_type": "military_service", "sector": "military", "country": "United States", "normalization_notes": "Modeled as a military assignment, never a civilian employer."},
        {"key": ORG_YALE, "organization_id": "918dedde-f9d1-5db1-8304-5c218a06b9b5", "canonical_name": "Yale University", "historical_name": "Yale University", "aliases": ["Yale"], "organization_type": "university", "sector": "academia_and_research", "city": "New Haven", "state_or_region": "Connecticut", "country": "United States", "normalization_notes": "Student status is not employment."},
        {"key": ORG_BRITISH_INTELLIGENCE, "canonical_name": "British intelligence service (unspecified)", "historical_name": "a British intelligence service", "aliases": [], "organization_type": "government intelligence service", "sector": "federal_government", "country": "United Kingdom", "normalization_notes": "The source does not name the service, so it is not normalized to MI5, MI6, SOE, or another specific organization."},
        {"key": ORG_BRYN_MAWR, "organization_id": "242079a5-4289-5105-83e6-51898d6cb032", "canonical_name": "Bryn Mawr College", "historical_name": "Bryn Mawr College", "aliases": ["Bryn Mawr"], "organization_type": "college", "sector": "academia_and_research", "city": "Bryn Mawr", "state_or_region": "Pennsylvania", "country": "United States", "normalization_notes": "Student status is not employment; chronology is presented as pre-intelligence-service, not proven pre-OSS."},
    ]


def occupation_key(row: int) -> str:
    return f"{slug(PEOPLE[row][1])}-army-occupation-row{row}-b1006"


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, item in ARMY_MATCHES.items():
        if not item["publish"]:
            continue
        values.append({
            "key": occupation_key(row),
            "person_id": PEOPLE[row][0],
            "occupation": item["occupation"],
            "relationship_type": "student" if item["code"] == "992" else "unknown",
            "end_date": item["date"],
            "date_precision": f"Historical civilian-occupation code {item['code']} was recorded at Army entry on {item['date']}; no named employer, workplace, institution, or exact OSS-transfer date is supplied.",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": item["identity"],
            "claim_confidence": "medium",
            "source_quality": "A_direct_official",
            "publication_status": "publish_qualified",
            "research_notes": "Broad historical category only; no named employer, institution, workplace, or OSS transition is inferred.",
        })

    values.extend([
        {"key": "weismiller-harvard-employment-b1006", "person_id": PEOPLE[7][0], "organization_key": ORG_HARVARD, "organization_name_as_found": "Harvard", "role_title": "Teacher", "occupation": "teacher and graduate student", "relationship_type": "employment", "end_date": "1942", "date_precision": "The obituary says he earned a master's degree and taught at Harvard before a midnight OSS recruitment call; the exact dates of teaching and recruitment are not supplied.", "city": "Cambridge", "state_or_region": "Massachusetts", "country": "United States", "immediate_pre_oss": True, "last_civilian_pre_service": True, "pre_oss_temporal_basis": "probable_immediate", "identity_confidence": "confirmed", "claim_confidence": "medium", "source_quality": "C_reputable_contemporary_or_scholarly", "publication_status": "publish_qualified", "research_notes": "Best-supported immediate and last civilian affiliation, visibly qualified because the chronology lacks exact dates."},
        {"key": "weismiller-random-house-b1006", "person_id": PEOPLE[7][0], "organization_key": ORG_RANDOM_HOUSE, "organization_name_as_found": "Random House", "role_title": "Translator", "occupation": "literary translator", "relationship_type": "employment", "start_date": "1941", "end_date": "1942", "date_precision": "The obituary says Random House hired him in 1941 while he was a student and published the translation in 1942.", "city": "New York", "state_or_region": "New York", "country": "United States", "immediate_pre_oss": False, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "confirmed", "claim_confidence": "high", "source_quality": "C_reputable_contemporary_or_scholarly", "publication_status": "published", "research_notes": "Earlier project employment; not presented as the immediate pre-OSS employer."},
        {"key": "weismiller-cornell-student-b1006", "person_id": PEOPLE[7][0], "organization_key": ORG_CORNELL_COLLEGE, "organization_name_as_found": "Cornell College", "role_title": "Student", "occupation": "student", "relationship_type": "student", "end_date": "1938", "date_precision": "Both biographies identify the 1938 Cornell College graduation.", "city": "Mount Vernon", "state_or_region": "Iowa", "country": "United States", "immediate_pre_oss": False, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "confirmed", "claim_confidence": "high", "source_quality": "B_authoritative_institutional", "publication_status": "published", "research_notes": "Student status is not employment."},
        {"key": "weismiller-oxford-student-b1006", "person_id": PEOPLE[7][0], "organization_key": ORG_OXFORD, "organization_name_as_found": "Oxford University", "role_title": "Rhodes Scholar", "occupation": "student", "relationship_type": "student", "start_date": "1936", "date_precision": "The obituary says his Rhodes Scholarship study was interrupted by war and later completed after wartime service.", "city": "Oxford", "country": "United Kingdom", "immediate_pre_oss": False, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "confirmed", "claim_confidence": "high", "source_quality": "C_reputable_contemporary_or_scholarly", "publication_status": "published", "research_notes": "Prewar student affiliation only; the postwar return is not modeled as pre-OSS."},
        {"key": "weisgal-harvard-student-b1006", "person_id": PEOPLE[4][0], "organization_key": ORG_HARVARD, "organization_name_as_found": "Harvard", "role_title": "Student and actor in a university production", "occupation": "student", "relationship_type": "student", "end_date": "1942-12-10", "date_precision": "A contemporary item dated December 10, 1942 calls Meyer W. Weisgal's son Emanuel a Harvard student; the index lacks a direct identifier bridge.", "city": "Cambridge", "state_or_region": "Massachusetts", "country": "United States", "immediate_pre_oss": False, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "temporal_relation_uncertain", "identity_confidence": "probable", "claim_confidence": "medium", "source_quality": "C_reputable_contemporary_or_scholarly", "publication_status": "publish_qualified", "research_notes": "Qualified rare-name lead; Harvard is not classified as an employer and the Box 824 file must establish identity and sequence."},
        {"key": "benjamin-welles-nyt-b1006", "person_id": PEOPLE[42][0], "organization_key": ORG_NYT, "organization_name_as_found": "the Times", "role_title": "News clerk", "occupation": "journalist", "relationship_type": "employment", "start_date": "1938", "end_date": "1942", "date_precision": "The obituary says he joined after Harvard graduation in 1938 and enlisted in the Army during World War II; a biographical book note dates enlistment to 1942.", "city": "New York", "state_or_region": "New York", "country": "United States", "immediate_pre_oss": False, "last_civilian_pre_service": True, "pre_oss_temporal_basis": "strongly_date_bounded", "identity_confidence": "confirmed", "claim_confidence": "high", "source_quality": "C_reputable_contemporary_or_scholarly", "publication_status": "published", "research_notes": "Last civilian employer before the documented Army-to-OSS pathway."},
        {"key": "benjamin-welles-army-b1006", "person_id": PEOPLE[42][0], "organization_key": ORG_ARMY, "organization_name_as_found": "Army", "role_title": "Major; Executive Officer to the commanding officer, SCI France", "relationship_type": "military_assignment", "start_date": "1942", "date_precision": "The obituary dates Army entry to wartime service; the official OSS award file confirms his Major rank and SCI France role.", "country": "United States", "immediate_pre_oss": True, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "probable_immediate", "identity_confidence": "confirmed", "claim_confidence": "high", "source_quality": "A_direct_official", "publication_status": "published", "research_notes": "Military pathway, not a civilian employer. The source does not state a separate pre-OSS Army unit or transfer date."},
        {"key": "benjamin-welles-harvard-b1006", "person_id": PEOPLE[42][0], "organization_key": ORG_HARVARD, "organization_name_as_found": "Harvard", "role_title": "Student", "occupation": "student", "relationship_type": "student", "end_date": "1938", "date_precision": "The obituary says he graduated in 1938 and then joined The New York Times.", "city": "Cambridge", "state_or_region": "Massachusetts", "country": "United States", "immediate_pre_oss": False, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "confirmed", "claim_confidence": "high", "source_quality": "C_reputable_contemporary_or_scholarly", "publication_status": "published", "research_notes": "Student status is not employment."},
        {"key": "edward-welles-british-intelligence-b1006", "person_id": PEOPLE[44][0], "organization_key": ORG_BRITISH_INTELLIGENCE, "organization_name_as_found": "a British intelligence service", "role_title": "Volunteer intelligence worker", "relationship_type": "government_assignment", "start_date": "1943", "end_date": "1944", "date_precision": "The obituary says he volunteered in 1943 and joined OSS the next year.", "country": "United Kingdom", "immediate_pre_oss": True, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "explicit_immediate", "identity_confidence": "high_confidence", "claim_confidence": "high", "source_quality": "C_reputable_contemporary_or_scholarly", "publication_status": "published", "research_notes": "The service is deliberately left unspecified; it is not normalized to a named British agency."},
        {"key": "edward-welles-yale-b1006", "person_id": PEOPLE[44][0], "organization_key": ORG_YALE, "organization_name_as_found": "Yale University", "role_title": "Student", "occupation": "student", "relationship_type": "student", "end_date": "1942", "date_precision": "The obituary says he interrupted Yale studies to drive an ambulance in North Africa; an exact interruption date is not stated.", "city": "New Haven", "state_or_region": "Connecticut", "country": "United States", "immediate_pre_oss": False, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "high_confidence", "claim_confidence": "high", "source_quality": "C_reputable_contemporary_or_scholarly", "publication_status": "published", "research_notes": "Earlier student affiliation, not employment."},
        {"key": "philip-weld-harvard-b1006", "person_id": PEOPLE[36][0], "organization_key": ORG_HARVARD, "organization_name_as_found": "Harvard", "role_title": "Student", "occupation": "student", "relationship_type": "student", "end_date": "1936", "date_precision": "The Crimson identifies Philip Saltonstall Weld as Harvard class of 1936 and a Silver Star recipient in World War II, but does not mention OSS.", "city": "Cambridge", "state_or_region": "Massachusetts", "country": "United States", "immediate_pre_oss": False, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "probable", "claim_confidence": "medium", "source_quality": "C_reputable_contemporary_or_scholarly", "publication_status": "publish_qualified", "research_notes": "Qualified uncommon-name and wartime-service lead; the Box 825 file remains necessary for an OSS identity bridge."},
        {"key": "wellemeyer-bryn-mawr-b1006", "person_id": PEOPLE[41][0], "organization_key": ORG_BRYN_MAWR, "organization_name_as_found": "Bryn Mawr College", "role_title": "Student", "occupation": "student", "relationship_type": "student", "start_date": "1942", "end_date": "1946", "date_precision": "The obituary dates Bryn Mawr study to 1942-1946 and central-intelligence work to 1947; it does not establish OSS-period service.", "city": "Bryn Mawr", "state_or_region": "Pennsylvania", "country": "United States", "immediate_pre_oss": False, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "temporal_relation_uncertain", "identity_confidence": "high_confidence", "claim_confidence": "medium", "source_quality": "D_correlative_or_secondary", "publication_status": "publish_qualified", "research_notes": "Presented as pre-intelligence-service student history, not as proof of pre-OSS employment or OSS-period service."},
    ])
    return values


def make_claim(*, key: str, row: int, claim_type: str, text: str, paraphrase: str, identity: str, temporal: str, quality: str, confidence: str, publication: str, notes: str, source_links: list[dict[str, str]], affiliation_key: str | None = None) -> dict[str, object]:
    value: dict[str, object] = {
        "key": key,
        "person_id": PEOPLE[row][0],
        "claim_type": claim_type,
        "claim_text": text,
        "evidence_paraphrase": paraphrase,
        "identity_match_assessment": identity,
        "temporal_assessment": temporal,
        "source_quality": quality,
        "claim_confidence": confidence,
        "publication_status": publication,
        "match_notes": notes,
        "sources": source_links,
    }
    if affiliation_key:
        value["affiliation_key"] = affiliation_key
    return value


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, item in ARMY_MATCHES.items():
        name = PEOPLE[row][1]
        links: list[dict[str, str]] = [
            {"source_key": INDEX, "locator_override": f"{row_locator(row)}; protected identifier withheld"},
            {"source_key": ARMY, "locator_override": "Accepted reviewed identity bridge; protected identifier withheld"},
        ]
        if row == 12:
            links.append({"source_key": NARA_AWARDS, "locator_override": "PDF physical page 82", "excerpt_override": "Cpl Rudi Weiss"})
        values.append(make_claim(
            key=f"identity-{slug(name)}-row{row}-b1006",
            row=row,
            claim_type="identity",
            text=f"Indexed {name} is {('confirmed' if item['identity'] == 'confirmed' else 'a high-confidence match')} to the reviewed official Army entry record.",
            paraphrase=item["detail"],
            identity=("Confirmed by official sources and a nonshared protected-identifier agreement; the identifier remains private." if item["identity"] == "confirmed" else "High confidence from a nonshared protected identifier plus compatible name fields; the limited discrepancy remains visible."),
            temporal=f"The Army record dates entry to {item['date']}.",
            quality="A_direct_official",
            confidence=("confirmed" if item["identity"] == "confirmed" else "high"),
            publication="published",
            notes="Identity only; no named employer, workplace, institution, or exact OSS-transfer date is inferred from the Army record.",
            source_links=links,
        ))
        if item["publish"]:
            values.append(make_claim(
                key=f"occupation-{slug(name)}-row{row}-b1006",
                row=row,
                claim_type="occupation",
                text=f"At Army entry on {item['date']}, {name} was recorded in the historical {item['occupation']} category; no named employer or institution is identified.",
                paraphrase=f"The accepted Army record carries civilian-occupation code {item['code']}, decoded from NARA's official code list.",
                identity="The category belongs only to the accepted protected-identifier match; the identifier itself is not public.",
                temporal="Strongly date-bounded to Army entry; it does not establish the immediate pre-OSS affiliation or a named employer, workplace, or institution.",
                quality="A_direct_official",
                confidence="medium",
                publication="publish_qualified",
                notes="Published with its limits and excluded from verified-employer analytics.",
                source_links=[
                    {"source_key": ARMY, "locator_override": f"Army entry {item['date']}; civilian occupation code {item['code']}; protected identifier withheld"},
                    {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46"},
                    {"source_key": CODES, "locator_override": item["locator"], "excerpt_override": item["label"]},
                ],
                affiliation_key=occupation_key(row),
            ))

    values.extend([
        make_claim(key="identity-edward-weismiller-b1006", row=7, claim_type="identity", text="The two indexed Edward Weismiller rows represent Edward Ronald Weismiller, the Marine first lieutenant and OSS X-2 officer documented in official and institutional sources.", paraphrase="The name variants, USMCR note, first-lieutenant rank, Cornell biography, and official OSS award entry align.", identity="Confirmed by two complementary index rows, an official OSS record, and an authoritative institutional biography.", temporal="The official record documents wartime OSS X-2 service; the biography supplies the education and recruitment chronology.", quality="A_direct_official", confidence="confirmed", publication="published", notes="The source rows remain separately preserved and visibly linked to one cautious entity.", source_links=[{"source_key": INDEX, "locator_override": "PDF page 496 rows 7-8"}, {"source_key": NARA_AWARDS, "locator_override": "PDF physical page 109", "excerpt_override": "1st Lt Edward R. Weismiller"}, {"source_key": CORNELL_WEISMILLER, "locator_override": "Education and OSS paragraph", "excerpt_override": "served with the Office of Strategic Services in counterespionage"}]),
        make_claim(key="immediate-weismiller-harvard-b1006", row=7, claim_type="immediate_pre_oss_affiliation", text="Edward Ronald Weismiller's best-supported immediate pre-OSS affiliation was Harvard University, where he completed a master's degree and taught before OSS recruitment.", paraphrase="The detailed obituary places Harvard teaching directly before a midnight OSS recruitment call, but gives no exact teaching or recruitment date.", identity="Confirmed by the official OSS entry, the indexed USMCR first-lieutenant row, and independent biographies.", temporal="Probable immediate affiliation; the sequence is direct but the source does not explicitly say he left Harvard for OSS on a stated date.", quality="C_reputable_contemporary_or_scholarly", confidence="medium", publication="publish_qualified", notes="Visibly qualified and excluded from default high-confidence employer analytics.", source_links=[{"source_key": WEISMILLER_OBIT, "locator_override": "Harvard and OSS recruitment paragraphs", "excerpt_override": "earned his master's degree and taught at Harvard"}], affiliation_key="weismiller-harvard-employment-b1006"),
        make_claim(key="last-civilian-weismiller-harvard-b1006", row=7, claim_type="last_civilian_pre_service", text="Harvard University is the last documented civilian employer before Edward Ronald Weismiller's wartime service, subject to the same chronology qualification.", paraphrase="The obituary sequences Harvard teaching immediately before OSS recruitment and Marine commissioning.", identity="Confirmed exact-person record chain.", temporal="Probable last civilian employment; an exact end date and intervening-gap statement are absent.", quality="C_reputable_contemporary_or_scholarly", confidence="medium", publication="publish_qualified", notes="Random House translation work is modeled separately as earlier employment.", source_links=[{"source_key": WEISMILLER_OBIT, "locator_override": "Harvard and OSS recruitment paragraphs", "excerpt_override": "taught at Harvard"}], affiliation_key="weismiller-harvard-employment-b1006"),
        make_claim(key="earlier-weismiller-random-house-b1006", row=7, claim_type="other_pre_oss_affiliation", text="Random House hired Edward Ronald Weismiller in 1941 to translate a French novel that it published in 1942.", paraphrase="The obituary explicitly identifies the publisher, year hired, project, and publication year.", identity="Confirmed exact-person biography supported by official OSS identity evidence.", temporal="Documented prewar employment, but not shown to be the immediate predecessor to OSS service.", quality="C_reputable_contemporary_or_scholarly", confidence="high", publication="published", notes="Kept separate from Harvard teaching and not marked immediate.", source_links=[{"source_key": WEISMILLER_OBIT, "locator_override": "Closing Random House paragraph", "excerpt_override": "In 1941, Random House hired Weismiller"}], affiliation_key="weismiller-random-house-b1006"),
        make_claim(key="student-weismiller-cornell-b1006", row=7, claim_type="other_pre_oss_affiliation", text="Edward Ronald Weismiller graduated from Cornell College in 1938.", paraphrase="Cornell College's institutional memorial identifies him as class of 1938.", identity="Confirmed exact-person institutional biography and official OSS record.", temporal="Earlier documented prewar student affiliation.", quality="B_authoritative_institutional", confidence="high", publication="published", notes="Education is not classified as employment.", source_links=[{"source_key": CORNELL_WEISMILLER, "locator_override": "Title and opening biography", "excerpt_override": "Edward R. Weismiller '38"}], affiliation_key="weismiller-cornell-student-b1006"),
        make_claim(key="student-weismiller-oxford-b1006", row=7, claim_type="other_pre_oss_affiliation", text="Edward Ronald Weismiller was a Rhodes Scholar at the University of Oxford before wartime service interrupted his studies.", paraphrase="The obituary supplies the scholarship and wartime interruption; he returned after the war to finish the doctorate.", identity="Confirmed exact-person source chain.", temporal="Documented prewar student affiliation; the postwar return is excluded from the pre-OSS claim.", quality="C_reputable_contemporary_or_scholarly", confidence="high", publication="published", notes="Education is not classified as employment.", source_links=[{"source_key": WEISMILLER_OBIT, "locator_override": "Education and wartime-interruption paragraphs", "excerpt_override": "In 1936 he was awarded a Rhodes Scholarship to Oxford"}], affiliation_key="weismiller-oxford-student-b1006"),
        make_claim(key="student-emanuel-weisgal-harvard-b1006", row=4, claim_type="other_pre_oss_affiliation", text="A contemporary December 1942 item identifies an Emanuel Weisgal, son of Meyer W. Weisgal, as a Harvard student and university actor; the OSS-index identity remains probable.", paraphrase="The unusual exact name and wartime date make this a useful lead, but neither the article nor the index supplies a second corroborating identifier.", identity="Probable uncommon-name match; Box 824 remains necessary for confirmation.", temporal="Documented in December 1942, but its relation to OSS entry is uncertain.", quality="C_reputable_contemporary_or_scholarly", confidence="medium", publication="publish_qualified", notes="Harvard is modeled as student affiliation, never as employer.", source_links=[{"source_key": SENTINEL_WEISGAL, "locator_override": "PDF page 10, 'Stage and Screen'", "excerpt_override": "His son Emanuel, a student at Harvard"}], affiliation_key="weisgal-harvard-student-b1006"),
        make_claim(key="identity-benjamin-welles-b1006", row=42, claim_type="identity", text="Indexed Major Benjamin Welles is confirmed as the New York Times journalist who served in Army OSS and as executive officer to the commanding officer, SCI France.", paraphrase="The exact distinctive name and Major rank appear in the index and official OSS award file; the obituary independently documents Army and OSS service.", identity="Confirmed by exact name, officer rank, official OSS role, and an independent reputable biography.", temporal="The sources consistently place Army and OSS service during World War II.", quality="A_direct_official", confidence="confirmed", publication="published", notes="The biography's employer chronology is modeled separately.", source_links=[{"source_key": INDEX, "locator_override": "PDF page 496 row 42"}, {"source_key": NARA_AWARDS, "locator_override": "PDF physical page 109", "excerpt_override": "Major Benjamin Welles"}, {"source_key": WAPO_BENJAMIN, "locator_override": "Army and OSS paragraph", "excerpt_override": "enlisted in the Army and served in the Office of Strategic Services"}]),
        make_claim(key="last-civilian-benjamin-welles-nyt-b1006", row=42, claim_type="last_civilian_pre_service", text="The New York Times was Benjamin Welles's last documented civilian employer before Army and OSS service; he joined in 1938 as a news clerk.", paraphrase="The obituary sequences Harvard graduation, Times employment, and wartime Army/OSS service.", identity="Confirmed by exact name and rank in official OSS evidence plus the independent obituary.", temporal="Strongly date-bounded; available biographies date Army entry to 1942, with no intervening civilian employer identified.", quality="C_reputable_contemporary_or_scholarly", confidence="high", publication="published", notes="The Army pathway remains the immediate military affiliation and is not labeled a civilian employer.", source_links=[{"source_key": WAPO_BENJAMIN, "locator_override": "Education, employment, and wartime-service paragraphs", "excerpt_override": "graduated from Harvard and joined the Times as a news clerk"}], affiliation_key="benjamin-welles-nyt-b1006"),
        make_claim(key="immediate-benjamin-welles-army-b1006", row=42, claim_type="immediate_pre_oss_affiliation", text="Benjamin Welles entered OSS through U.S. Army service and ended the war as a major.", paraphrase="The obituary states that he enlisted in the Army and served in OSS; the official award file confirms the Major rank and SCI France assignment.", identity="Confirmed exact-person official and biographical sources.", temporal="Probable immediate military pathway; no separate pre-OSS Army unit or transfer date is stated.", quality="A_direct_official", confidence="high", publication="published", notes="Military assignment is not counted as a civilian employer.", source_links=[{"source_key": WAPO_BENJAMIN, "locator_override": "Army and OSS paragraph", "excerpt_override": "enlisted in the Army and served in the Office of Strategic Services"}, {"source_key": NARA_AWARDS, "locator_override": "PDF physical page 109", "excerpt_override": "Was Executive Officer to CO, SCI France"}], affiliation_key="benjamin-welles-army-b1006"),
        make_claim(key="student-benjamin-welles-harvard-b1006", row=42, claim_type="other_pre_oss_affiliation", text="Benjamin Welles graduated from Harvard University in 1938 before joining The New York Times.", paraphrase="The obituary gives the institution, graduation year, and next employment.", identity="Confirmed exact-person source chain.", temporal="Earlier documented prewar student affiliation.", quality="C_reputable_contemporary_or_scholarly", confidence="high", publication="published", notes="Student status is not employment.", source_links=[{"source_key": WAPO_BENJAMIN, "locator_override": "Education and employment paragraph", "excerpt_override": "In 1938, he graduated from Harvard"}], affiliation_key="benjamin-welles-harvard-b1006"),
        make_claim(key="identity-edward-welles-b1006", row=44, claim_type="identity", text="Indexed Edward O. Welles is a high-confidence match to Edward O'Malley Welles, whose obituary documents Yale, British intelligence, OSS, and Army service.", paraphrase="The distinctive full name, middle-name expansion, wartime intelligence chronology, and direct OSS statement align.", identity="High confidence from a distinctive name and specific direct OSS biography; the protected index identifier still requires archival confirmation.", temporal="The obituary dates British intelligence work to 1943 and OSS entry to 1944.", quality="C_reputable_contemporary_or_scholarly", confidence="high", publication="published", notes="No protected identifier was disclosed or sent to an external service.", source_links=[{"source_key": INDEX, "locator_override": "PDF page 496 row 44; protected identifier withheld"}, {"source_key": WAPO_EDWARD, "locator_override": "Wartime biography paragraphs", "excerpt_override": "The next year, he joined the OSS"}]),
        make_claim(key="immediate-edward-welles-british-intelligence-b1006", row=44, claim_type="immediate_pre_oss_affiliation", text="Edward O'Malley Welles's immediate pre-OSS affiliation was an unspecified British intelligence service, for which he volunteered in 1943.", paraphrase="The obituary says he volunteered in 1943, gathered intelligence in Greece, and joined OSS the next year.", identity="High-confidence exact-person match from distinctive name and direct OSS chronology.", temporal="Explicit immediate sequence from 1943 British intelligence work to 1944 OSS entry.", quality="C_reputable_contemporary_or_scholarly", confidence="high", publication="published", notes="The service is not silently normalized to MI5, MI6, SOE, or another named agency.", source_links=[{"source_key": WAPO_EDWARD, "locator_override": "Lines describing 1943-1944 intelligence service", "excerpt_override": "In 1943, he volunteered for a British intelligence service"}], affiliation_key="edward-welles-british-intelligence-b1006"),
        make_claim(key="student-edward-welles-yale-b1006", row=44, claim_type="other_pre_oss_affiliation", text="Edward O'Malley Welles attended Yale University before interrupting his studies to drive an ambulance in North Africa.", paraphrase="The obituary explicitly sequences Yale study before his wartime ambulance and intelligence work.", identity="High-confidence exact-person match.", temporal="Earlier documented prewar student affiliation; not the immediate pre-OSS role.", quality="C_reputable_contemporary_or_scholarly", confidence="high", publication="published", notes="Student status is not employment; the ambulance organization is not named and is not inferred.", source_links=[{"source_key": WAPO_EDWARD, "locator_override": "Education and ambulance paragraph", "excerpt_override": "interrupted his studies at Yale University to be an ambulance driver"}], affiliation_key="edward-welles-yale-b1006"),
        make_claim(key="student-philip-weld-harvard-b1006", row=36, claim_type="other_pre_oss_affiliation", text="The indexed Philip S. Weld is a probable match to Philip Saltonstall Weld, Harvard class of 1936 and a World War II Silver Star recipient.", paraphrase="The uncommon full-name expansion and wartime service support the lead, but the biography does not mention OSS and no second index identifier is available publicly.", identity="Probable pending Box 825 review.", temporal="Harvard class year establishes an earlier prewar student affiliation if the identity is confirmed.", quality="C_reputable_contemporary_or_scholarly", confidence="medium", publication="publish_qualified", notes="Excluded from default high-confidence analytics; Harvard is not an employer.", source_links=[{"source_key": CRIMSON_WELD, "locator_override": "Opening and career paragraphs", "excerpt_override": "Philip Saltonstall Weld 36"}], affiliation_key="philip-weld-harvard-b1006"),
        make_claim(key="student-wellemeyer-bryn-mawr-b1006", row=41, claim_type="other_pre_oss_affiliation", text="A strong identity lead places Marilyn Ruth Wellemeyer at Bryn Mawr College from 1942 to 1946 before documented central-intelligence work in 1947; OSS-period service remains unresolved.", paraphrase="The rare exact name and intelligence chronology align with the indexed file, but the obituary describes post-OSS successor work rather than OSS service.", identity="High-confidence lead, not confirmed; the Box 825 personnel file must establish why the name appears in the index.", temporal="Documented pre-intelligence-service study, but its relationship to the OSS period is uncertain.", quality="D_correlative_or_secondary", confidence="medium", publication="publish_qualified", notes="Presented with explicit chronology limits and excluded from employer analytics.", source_links=[{"source_key": MATHER_WELLEMEYER, "locator_override": "Education and 1947 intelligence-work paragraphs", "excerpt_override": "graduated Cum Laude in 1946"}], affiliation_key="wellemeyer-bryn-mawr-b1006"),
    ])
    return values


def base_update(row: int, **overrides: object) -> dict[str, object]:
    value: dict[str, object] = {
        "person_id": PEOPLE[row][0],
        "manual_review_required": True,
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }
    if row in PRINTED_CATEGORY:
        value["personnel_category"], value["commissioned_officer"] = PRINTED_CATEGORY[row]
    if row in DUPLICATE_GROUPS:
        value["possible_duplicate_group"] = DUPLICATE_GROUPS[row]
    value.update(overrides)
    return value


def person_updates() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    special = set(ARMY_MATCHES) | {4, 7, 36, 41, 42, 44}
    for row in sorted(set(PEOPLE) - special):
        reason = unresolved_reason(row)
        values.append(base_update(
            row,
            identity_status="unresolved",
            identity_evidence=f"The visually verified page 496 source preserves {PEOPLE[row][1]}, its printed rank or notation, archival box, and location. {reason}",
            research_status="requires_archival_review",
            next_action=f"Review the indexed Box {box_for(row)} personnel file for corroborating identifiers, the immediate pre-OSS affiliation, and the last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}",
        ))
    for row, item in ARMY_MATCHES.items():
        if row == 30:
            values.append(base_update(row, identity_status=item["identity"], identity_evidence=item["detail"] + " A nonshared protected identifier supports the match, but the late entry date does not establish the relation to OSS.", personnel_category="enlisted_army_personnel", commissioned_officer=False, research_status="requires_archival_review", next_action="Review the Box 824 personnel file to establish the Army-to-OSS chronology before publishing occupation code 097 or any employer claim.", nara_catalog_id="1263923"))
        else:
            values.append(base_update(row, identity_status=item["identity"], identity_evidence=item["detail"] + " The protected identifier remains private.", personnel_category="enlisted_army_personnel", commissioned_officer=False, research_status="occupation_only_found", next_action=f"Review the indexed Box {box_for(row)} personnel file to identify any named employer or institution behind the broad {item['occupation']} category and establish the Army-to-OSS chronology.", nara_catalog_id="1263923"))
    values.extend([
        base_update(4, identity_status="probable", identity_evidence="The rare exact name and a contemporary December 1942 Harvard student item support a probable identity lead, but no second identifier or direct OSS bridge was found.", research_status="requires_archival_review", next_action="Review the Box 824 personnel file to confirm whether the indexed Emanuel Weisgal is Meyer W. Weisgal's son and establish the OSS entry sequence."),
        base_update(7, identity_status="confirmed", identity_evidence="Rows 7 and 8 supply complementary name forms, first-lieutenant rank, and USMCR note; an official OSS award record and Cornell biography confirm Edward R. Weismiller's counterespionage service.", name_variants=["Edward R Weismiller", "Edward Ronal Weismiller"], replace_name_variants=True, personnel_category="commissioned_marine_corps_officer", commissioned_officer=True, research_status="documented_prewar_employer_found", archival_review_priority="medium", next_action="Review the Box 824 personnel file for exact Harvard employment and OSS recruitment dates; Harvard remains a medium-confidence probable-immediate employer."),
        base_update(36, identity_status="probable", identity_evidence="The uncommon Philip S. Weld name, Philip Saltonstall expansion, Harvard 1936 class year, and World War II Silver Star support a probable lead; the biography does not mention OSS.", research_status="requires_archival_review", next_action="Review the Box 825 personnel file to confirm the Philip Saltonstall Weld identity and determine the immediate pre-OSS affiliation."),
        base_update(41, identity_status="high_confidence", identity_evidence="The exceptionally rare exact name and obituary chronology place Marilyn Ruth Wellemeyer in central-intelligence work in 1947, but do not establish OSS-period service or why her file appears in the index.", research_status="requires_archival_review", archival_review_priority="critical", next_action="Review the Box 825 file to resolve whether it is an OSS, SSU, CIG, or successor-service personnel file and establish the relevant predecessor affiliation."),
        base_update(42, identity_status="confirmed", identity_evidence="The exact distinctive name and Major rank agree between the index and official OSS award file; the Washington Post obituary independently documents Army OSS service and the pre-service New York Times job.", personnel_category="commissioned_army_officer", commissioned_officer=True, research_status="verified_employer_found", archival_review_priority="medium", next_action="Review the Box 825 personnel file for the exact 1942 Army entry and OSS assignment dates."),
        base_update(44, identity_status="high_confidence", identity_evidence="The distinctive Edward O. Welles name expands to Edward O'Malley Welles in a reputable obituary that directly dates British intelligence and OSS service; the protected index identifier remains unconfirmed externally.", research_status="completed", archival_review_priority="medium", next_action="Review the Box 825 personnel file to confirm the protected identifier and exact OSS appointment, branch, and rank."),
    ])
    if len(values) != len(PEOPLE):
        raise RuntimeError(f"Expected {len(PEOPLE)} person updates, generated {len(values)}")
    return values


def research_attempts() -> list[dict[str, object]]:
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        if row == 7:
            outcome, reviewed, rejected = "source_reviewed", 13, 5
            note = "Official OSS evidence confirms the merged identity; a detailed obituary and Cornell biography support qualified Harvard employment, earlier Random House work, and student affiliations."
        elif row == 42:
            outcome, reviewed, rejected = "source_reviewed", 12, 5
            note = "Official OSS evidence confirms Major Benjamin Welles; a reputable obituary supports The New York Times as the last civilian employer and Army as the immediate military pathway."
        elif row == 44:
            outcome, reviewed, rejected = "source_reviewed", 10, 5
            note = "A reputable obituary supplies a distinctive full-name expansion, direct OSS service, immediate British intelligence work, and earlier Yale study."
        elif row == 4:
            outcome, reviewed, rejected = "source_reviewed", 9, 6
            note = "A visually checked contemporary newspaper provides a probable Harvard student lead; identity and OSS chronology remain archival-review questions."
        elif row == 36:
            outcome, reviewed, rejected = "source_reviewed", 9, 6
            note = "The Harvard Crimson supports a probable Philip Saltonstall Weld identity and prewar Harvard study but does not establish OSS service."
        elif row == 41:
            outcome, reviewed, rejected = "source_reviewed", 9, 5
            note = "The rare exact name and 1947 central-intelligence chronology support a strong identity lead; the source contradicts any unqualified assumption of OSS-period service."
        elif row in ARMY_MATCHES:
            item = ARMY_MATCHES[row]
            outcome, reviewed, rejected = "source_reviewed", 9, 5
            note = (f"A reviewed protected-identifier Army bridge supports identity and a qualified {item['occupation']} category at Army entry; no named employer, institution, workplace, or OSS-transfer date is supplied." if item["publish"] else "The protected-identifier match is retained privately, but chronology is insufficient to publish the historical occupation category as pre-OSS evidence.")
        else:
            outcome, reviewed, rejected = "candidate_rejected", 7, 6
            note = unresolved_reason(row)
        attempts.append({
            "key": f"page496-row{row}-{slug(name)}-b1006",
            "person_id": person_id,
            "source_adapter": "manual_staged_protocol",
            "query_text": f"{name}; NARA OSS index context; CIA Reading Room, National Archives, and Library of Congress exact-name domain checks; exact-name and meaningful spelling, initial, suffix, punctuation, transliteration, and OCR variants; OSS, rank, branch, assignment, and identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory, and archival searches; indexed Box {box_for(row)}; protected identifiers used only in private official-record comparison",
            "query_variant_type": "staged_identity_employment_archival_protocol_batch_1006",
            "started_at": "2026-11-03T23:45:00Z",
            "completed_at": "2026-11-04T01:10:00Z",
            "outcome": outcome,
            "sources_reviewed": reviewed,
            "candidate_sources_rejected": rejected,
            "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, postwar-only leads, discovery-only biographies, and sources without an OSS, protected-identifier, rank, unit, or personnel-file bridge were rejected. Historical Army categories were not converted into named employers, workplaces, or institutions. Student status was not converted into employment.",
            "research_notes": f"{note} Exact-name official-domain, OSS, employer, occupation, obituary, biography, institutional, newspaper, directory, and archival searches were checked as applicable. NARA index page 496 was rendered and visually checked. Relevant Army code pages, the OSS award pages, the Weismiller obituary, and The Sentinel page were visually inspected. No authenticated NARA Catalog API call was made.",
            "next_action": f"Review the indexed Box {box_for(row)} personnel file for corroborating identifiers, the immediate pre-OSS affiliation, and the last civilian employer before wartime service.",
            "attempt_number": 1,
            "research_agent_version": "before-oss-b1006-v1",
        })
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-1006-v1",
        "reviewer": "Before OSS Batch 1006 evidence review",
        "sources": sources(),
        "organizations": organizations(),
        "affiliations": affiliations(),
        "claims": claims(),
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }
    EvidenceBundle.model_validate(bundle)
    OUTPUT.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
