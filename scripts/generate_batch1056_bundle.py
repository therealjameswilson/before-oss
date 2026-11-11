#!/usr/bin/env python3
"""Generate the reviewed Batch 1056 completion bundle for PDF page 311."""

from __future__ import annotations

import json
import re
import sys
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page311-eugene-f-mckee-to-richard-v-mclallen-review_"
    "batch-1056_2026-11-11.json"
)

INDEX = "nara-index-page311-b1056"
ARMY = "army-bulk-page311-b1056"
TECH = "army-tech-page311-b1056"
CODES = "army-codes-page311-b1056"
CSPAN = "cspan-porter-mckeever-b1056"
FDR = "nara-fdr-holdings-porter-mckeever-b1056"
AFSA = "afsa-emmerson-porter-mckeever-b1056"
BERKELEY = "berkeley-donald-mackinnon-b1056"
MCLALLEN = "nara-oss-awards-mclallen-b1056"
MCKILLOP = "senate-affidavit-marjorie-mckillop-b1056"


# Row 40 and row 41 are two separately preserved printed rows linked to one active
# person because the exact normalized name and private identifier agree. Row 42
# has a different identifier and remains a separate unresolved person.
PEOPLE = {
    1: ("9f0cf797-a233-554e-aa08-198e74bb117d", "Eugene F McKee", "508"),
    2: ("89b2aba3-fb16-54e8-9bff-50d0583671f5", "Howard R McKee", "508"),
    3: ("87540427-e043-5313-87cf-d48c48ed3dd8", "Samuel R McKee", "508"),
    4: ("71c45aa8-a318-5ab1-b904-5bd862741e6d", "Charles B McKeel", "508"),
    5: ("9b287c86-d2a1-527e-b073-4d5fec8f73d2", "John B McKeenan", "508"),
    6: ("163d87f3-8435-591b-a4fb-52e2881a2af6", "Alton H McKeethan", "508"),
    7: ("2b0fbee8-d22b-5382-80d0-bbe878feee01", "Porter H McKeever", "508"),
    8: ("9cc4c4de-efb8-50d0-aab4-e641d479105b", "Francis J McKenna", "508"),
    9: ("08675ecb-5983-5f64-adbd-124d80901356", "Michael M McKenney", "508"),
    10: ("e7a2e42a-3dbe-59b6-8280-ef258ea7f6c1", "Stewart L McKenney", "508"),
    11: ("bfb5330a-d471-5fd6-8edc-be0f506d26e0", "Stewart L McKenney", "508"),
    12: ("dd60dccf-c3e9-531a-98fe-2e3f2a33dc09", "James A McKenskey", "509"),
    13: ("caf52600-59af-5780-b723-63a8a5bb316f", "A.Q. McKenzie", "508"),
    14: ("7a8902f5-3e2e-5d0a-a294-fe4fd28c68c9", "Francis W McKenzie", "508"),
    15: ("93a69e26-7b3d-55cf-8c92-83ef9bf49226", "Gordon G McKenzie", "508"),
    16: ("b7ded7ef-a3c0-5436-9575-c4dfba76b4a8", "Louis F McKenzie", "508"),
    17: ("1703d005-2673-5502-b76b-31223619e190", "Marcella D McKenzie", "509"),
    18: ("f42515e7-f2a0-5cb9-bd6c-71095461cf08", "William H McKenzie", "509"),
    19: ("f0f67f98-825e-5a38-8f84-5daedafd5fed", "William S McKenzie", "509"),
    20: ("a7c00d21-8729-53b4-9bed-302b19c45902", "John B McKeon", "509"),
    21: ("9d28417e-32c4-5ae9-b270-4dc21330f042", "Thomas E McKeown", "509"),
    22: ("24678b19-3dbf-5e3d-8917-13b012e6f87f", "Ellsworth B McKie", "509"),
    23: ("5fe8a0f7-d926-599d-b4d1-f8af52ddeff9", "William F McKiernan", "509"),
    24: ("96e5b8b1-21ba-51ae-a587-6f961a2b29dd", "James L McKillop", "509"),
    25: ("6200df0a-f592-52d0-a420-3a1dd16d0c2e", "Marjorie L McKillop", "509"),
    26: ("bb11447b-ae92-5207-b794-2e42af450a5f", "Frederick H McKinley", "509"),
    27: ("02588cbd-f852-5812-8267-e238d3a6137a", "Gordon S McKinley", "509"),
    28: ("a9a77fb0-f11d-5533-b474-a357000ab7ec", "James S McKinley", "509"),
    29: ("f6819278-5872-5ed3-8998-03880e7a112a", "Charles C McKinney", "509"),
    30: ("dd992a00-8cac-53a1-9175-021afec9bf7c", "Ira D McKinney", "509"),
    31: ("3beaa14d-4b70-5eb7-9e6e-1a3fc197a45d", "James M McKinney", "509"),
    32: ("c5022888-7a6b-5d00-92ea-d8b775d78199", "James S McKinney", "509"),
    33: ("078e65b2-d22a-50dd-aea6-be1761cdf3be", "Joe H McKinney", "509"),
    34: ("a33da211-1814-57c4-ab40-4272effafdd5", "Maurice E McKinney", "509"),
    35: ("d5ef7413-3d25-5bbb-b99f-80c6ba91d775", "Donald W McKinnon", "509"),
    36: ("7497e2af-b1a8-52aa-9e4c-4cb3203ba238", "Hazel M McKinnon", "509"),
    37: ("0773213e-0a12-55e9-9041-68e9bfb48616", "Lloyd L McKinnon", "509"),
    38: ("079f8ba8-1571-5713-b6e9-dd50f8564f6e", "Roderick W McKinnon", "509"),
    39: ("04105a4d-7388-5991-b7fd-7e917e3e477c", "Ethel D McKnew", "509"),
    40: ("512518ac-900f-5640-93cb-5da5cc084103", "Kenneth L McKown", "508/509"),
    41: ("512518ac-900f-5640-93cb-5da5cc084103", "Kenneth L McKown", "508/509"),
    42: ("e3c44fcb-5b5e-5fef-b2cb-8c529acf5fa9", "Kenneth L McKown", "509"),
    43: ("b047f078-c17e-5c82-9967-0ad0a3139409", "Arthur McLain", "509"),
    44: ("3b39b7e5-2902-5024-8cd9-66459f56cf06", "John P McLain", "509"),
    45: ("40805905-b3b3-5009-9b13-29974636ca9d", "Robert E McLain", "510"),
    46: ("395c1942-d8b8-5871-99bc-98edd53c8b80", "Richard V McLallen", "510"),
}

UNIQUE_PEOPLE = OrderedDict()
for row, value in PEOPLE.items():
    UNIQUE_PEOPLE.setdefault(value[0], (row, *value))

ARMY_OCCUPATIONS = {
    2: ("1942-10-20", "118", "general industry clerk", "General industry clerks", "unknown", "PDF physical page 171; historical code 1-18"),
    3: ("1942-05-06", "685", "welder or flame cutter", "Welders and flame cutters", "unknown", "PDF physical page 173; historical code 6-85"),
    16: ("1941-02-06", "736", "chauffeur or driver", "Chauffeurs and drivers, bus, taxi, truck, and tractor", "unknown", "PDF physical page 174; historical code 7-36"),
    27: ("1944-09-08", "992", "student", "Students", "student", "PDF physical page 304; corrected historical code 9-92"),
    32: ("1942-12-11", "992", "student", "Students", "student", "PDF physical page 304; corrected historical code 9-92"),
    40: ("1943-08-02", "101", "bookkeeper or cashier, except bank cashier", "Bookkeepers and cashiers, except bank cashiers", "unknown", "PDF physical page 171; historical code 1-01"),
    37: ("1943-04-17", "576", "inspector, not elsewhere classified", "Inspectors, n.e.c.", "unknown", "PDF physical page 175; historical code 5-76"),
    45: ("1942-08-15", "583", "mechanic or repairman, not elsewhere classified", "Mechanics and repairmen, n.e.c.", "unknown", "PDF physical page 175; historical code 5-83"),
}

IDENTITY_ONLY_ARMY = {13, 14}
ATTEMPT_NUMBERS = {
    1: 2, 2: 3, 3: 3, 4: 2, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2,
    10: 3, 11: 3, 12: 3, 13: 3, 14: 3, 15: 2, 16: 3, 17: 2,
    18: 3, 19: 3, 20: 3, 21: 2, 22: 2, 23: 2, 24: 1, 25: 1,
    26: 1, 27: 1, 28: 1, 29: 1, 30: 1, 31: 1, 32: 1, 33: 1,
    34: 1, 35: 1, 36: 1, 37: 1, 38: 1, 39: 1, 40: 1, 42: 1,
    43: 1, 44: 1, 45: 1, 46: 1,
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def source(key: str, **kwargs: object) -> dict[str, object]:
    value: dict[str, object] = {"key": key, "access_date": "2026-11-11"}
    value.update(kwargs)
    return value


def sources() -> list[dict[str, object]]:
    return [
        source(
            INDEX,
            stable_url="https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            archival_identifier="RG 226, Entry A1-224, Boxes 508-510",
            title="OSS Personnel Files from Excel",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="2010-12-23",
            locator="PDF page 311, rows 1-46; every printed row visually checked against the official PDF",
            source_quality="A_direct_official",
            collection_name="Records of the Office of Strategic Services, Record Group 226",
            rights_notes="All 46 printed rows remain preserved. Full protected identifiers remain private.",
        ),
        source(
            ARMY,
            stable_url="https://catalog.archives.gov/id/1263923",
            archival_identifier="National Archives Identifier 1263923; parent series NAID 604357",
            title="Electronic Army Serial Number Merged File, ca. 1938-1946",
            author_creator="Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="1938-1946; merged file created 2002",
            locator="Official unrestricted ASNEF.FIN.DAT; reviewed row-specific private identity crosswalks",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records",
            document_number="ASNEF.FIN.DAT",
            rights_notes="No raw record, protected identifier, or bulk ordinal is retained in public assets.",
        ),
        source(
            TECH,
            stable_url="https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf",
            archival_identifier="NN3-064-03-008; National Archives Identifier 1263923",
            title="World War II Army Enlistment Records: Reference Copy of Technical Documentation",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives at College Park - Electronic Records",
            publication_record_date="1994-2005; reference copy modified 2011",
            locator="PDF physical pages 44-46; Army-entry date and civilian-occupation fields",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records technical documentation",
            rights_notes="Used only to interpret selected fields; the bulk file does not identify a named employer or prove the Army-to-OSS sequence.",
        ),
        source(
            CODES,
            stable_url="https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1CL_SD.pdf",
            archival_identifier="Code No. 30; National Archives Identifier 1263923",
            title="NARA Compiled Code Lists for the Electronic Army Serial Number Merged File",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives at College Park - Electronic Records",
            publication_record_date="1942; reference copy modified 2011",
            locator="PDF physical pages 171, 173-175, and 304; every published Batch 1056 category visually checked",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records technical documentation",
            rights_notes="Codes 515 and 999 were not published because no defensible definition was verified.",
        ),
        source(
            CSPAN,
            stable_url="https://booknotes.c-span.org/Watch/8609-1",
            archival_identifier="Booknotes program 8609-1",
            title="Adlai Stevenson: His Life and Legacy",
            author_creator="Brian Lamb, interviewer; Porter McKeever, interviewee",
            repository_publisher="C-SPAN Booknotes",
            publication_record_date="1989-08-06",
            locator="Transcript, Porter McKeever background discussion",
            source_quality="B_authoritative_institutional",
            collection_name="Booknotes",
            rights_notes="The interviewee directly names both newspapers he represented. Only short excerpts and project-authored paraphrases are retained.",
        ),
        source(
            FDR,
            stable_url="https://nara-media.s3.amazonaws.com/presidential-libraries/clinton/foia/2006-0469-F-Seg-2/2006-0469-F-Seg-2-PDF/Box_033/42-t-7763296-20060469F-Seg2-033-010-2015.pdf",
            archival_identifier="Franklin D. Roosevelt Library, Historical Materials, oral-history transcript list",
            title="Historical Materials in the Franklin D. Roosevelt Library",
            author_creator="Franklin D. Roosevelt Library",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="1996-03",
            locator="PDF page 25, Porter McKeever oral-history entry",
            source_quality="A_direct_official",
            collection_name="Franklin D. Roosevelt Library holdings guide",
            rights_notes="The finding aid dates McKeever's White House correspondent work to 1937-1942.",
        ),
        source(
            AFSA,
            stable_url="https://afsa.org/sites/default/files/fsj-1977-10-october_0.pdf",
            archival_identifier="Foreign Service Journal, volume 54, number 10",
            title="China-Burma-India",
            author_creator="John K. Emmerson",
            repository_publisher="American Foreign Service Association",
            publication_record_date="1977-10",
            locator="PDF page 35, Office of War Information Psychological Warfare Team discussion",
            source_quality="C_reputable_contemporary_or_scholarly",
            collection_name="Foreign Service Journal",
            rights_notes="The author distinguishes OWI's overt work from OSS and identifies Porter McKeever among the OWI team.",
        ),
        source(
            BERKELEY,
            stable_url="https://psychology.berkeley.edu/about/history/memoriam",
            archival_identifier="University of California In Memoriam, 1987",
            title="Donald Wallace MacKinnon, Psychology: Berkeley, 1903-1987",
            author_creator="Kenneth H. Craik, Harrison G. Gough, Wallace B. Hall, and Ravenna Helson",
            repository_publisher="University of California, Berkeley Department of Psychology",
            publication_record_date="1987",
            locator="Donald Wallace MacKinnon memorial; career chronology paragraph",
            source_quality="B_authoritative_institutional",
            collection_name="In Memoriam",
            rights_notes="The memorial explicitly dates the Bryn Mawr professorship and leave to direct OSS Station S.",
        ),
        source(
            MCLALLEN,
            stable_url="https://www.archives.gov/files/research/jfk/releases/104-10165-10120.pdf",
            archival_identifier="JFK release 104-10165-10120; OSS European Theater awards board minutes",
            title="Minutes of Meeting of Awards and Decorations Board",
            author_creator="Office of Strategic Services, United States Forces European Theater",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="1945-08-14",
            locator="Document page 77, Special Operations Branch list; Major Richard V. McLallen",
            source_quality="A_direct_official",
            collection_name="John F. Kennedy Assassination Records Collection",
            document_number="104-10165-10120",
            rights_notes="The official record confirms OSS context, exact name, and major rank; it does not identify a pre-OSS affiliation.",
        ),
        source(
            MCKILLOP,
            stable_url="https://www.ggarchives.com/MIL/HelloGirls/Docs/AffidavitOfMarjorieLMcKillop-1977.html",
            archival_identifier="U.S. Senate Committee on Veterans' Affairs hearing, 95th Congress, 1st session, Appendix B, page 357",
            title="Affidavit of Marjorie L. McKillop",
            author_creator="Marjorie L. McKillop",
            repository_publisher="Gjenvick-Gjonvik Archives reproduction of U.S. Senate hearing material",
            publication_record_date="1977-05-07",
            locator="Affidavit paragraphs 1-7",
            source_quality="C_reputable_contemporary_or_scholarly",
            collection_name="Recognition for Purposes of VA Benefits hearing exhibits",
            rights_notes="A probable rare-name identity only; the affidavit does not independently establish OSS service.",
        ),
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": "news-observer-b1056",
            "canonical_name": "The News & Observer",
            "historical_name": "Raleigh News and Observer",
            "aliases": ["News and Observer", "Raleigh News & Observer"],
            "organization_type": "newspaper",
            "sector": "journalism_and_media",
            "city": "Raleigh",
            "state_or_region": "North Carolina",
            "country": "United States",
            "normalization_notes": "McKeever's historical wording is preserved; the publication is not merged with another Daniels family property.",
        },
        {
            "key": "greenville-news-b1056",
            "canonical_name": "The Greenville News",
            "historical_name": "Greenville News",
            "aliases": [],
            "organization_type": "newspaper",
            "sector": "journalism_and_media",
            "city": "Greenville",
            "state_or_region": "South Carolina",
            "country": "United States",
            "normalization_notes": "Historical newspaper title retained; no modern corporate owner is substituted.",
        },
        {
            "key": "owi-b1056",
            "organization_id": "d907505c-05ff-502a-810c-e6189e186543",
            "canonical_name": "United States Office of War Information",
            "historical_name": "Office of War Information",
            "aliases": ["OWI"],
            "organization_type": "federal wartime information agency",
            "sector": "federal_government",
            "country": "United States",
            "active_dates": "1942-1945",
            "normalization_notes": "Existing canonical agency reused. OWI is explicitly kept distinct from OSS.",
        },
        {
            "key": "bryn-mawr-b1056",
            "organization_id": "242079a5-4289-5105-83e6-51898d6cb032",
            "canonical_name": "Bryn Mawr College",
            "historical_name": "Bryn Mawr College",
            "aliases": [],
            "organization_type": "college",
            "sector": "academia_and_research",
            "city": "Bryn Mawr",
            "state_or_region": "Pennsylvania",
            "country": "United States",
            "normalization_notes": "Existing canonical college reused; the documented professorship is employment, not education.",
        },
        {
            "key": "uw-b1056",
            "organization_id": "594f9bda-f97b-5210-9d92-b622487fbf34",
            "canonical_name": "University of Washington",
            "historical_name": "University of Washington",
            "aliases": ["UW"],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "Seattle",
            "state_or_region": "Washington",
            "country": "United States",
            "normalization_notes": "Existing organization reused; McKillop's status is student, never employment.",
        },
        {
            "key": "signal-corps-b1056",
            "organization_id": "37fe0e48-9745-5a0a-8e04-6be9bc7c5c91",
            "canonical_name": "United States Army Signal Corps",
            "historical_name": "Signal Corps",
            "aliases": ["U.S. Army Signal Corps"],
            "organization_type": "military branch",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "Existing military organization reused; the 1918-1919 assignment is not a civilian employer.",
        },
    ]


def army_affiliation_key(row: int) -> str:
    return f"{slug(PEOPLE[row][1])}-army-entry-occupation-b1056"


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, _label, relationship, _locator) in ARMY_OCCUPATIONS.items():
        values.append(
            {
                "key": army_affiliation_key(row),
                "person_id": PEOPLE[row][0],
                "occupation": occupation,
                "relationship_type": relationship,
                "end_date": date,
                "date_precision": f"Historical civilian-occupation code {code} was recorded at Army entry on {date}; no named employer, institution, workplace, or OSS-transfer date is supplied.",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "temporal_relation_uncertain",
                "identity_confidence": "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "A_direct_official",
                "publication_status": "publish_qualified",
                "research_notes": "The broad historical category is excluded from verified-employer analytics and is not converted into a named organization.",
            }
        )
    values.extend(
        [
            {
                "key": "porter-mckeever-news-observer-b1056",
                "person_id": PEOPLE[7][0],
                "organization_key": "news-observer-b1056",
                "organization_name_as_found": "Raleigh News and Observer",
                "role_title": "Washington and White House correspondent",
                "occupation": "newspaper correspondent",
                "relationship_type": "employment",
                "start_date": "1937",
                "end_date": "1942",
                "date_precision": "NARA's holdings guide dates White House correspondent work to 1937-1942; McKeever's first-person interview names the newspaper he represented.",
                "city": "Washington",
                "state_or_region": "District of Columbia",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "A_direct_official",
                "publication_status": "published",
                "research_notes": "The two newspaper clients are preserved as separate concurrent employers. The exact OSS entry date remains unknown.",
            },
            {
                "key": "porter-mckeever-greenville-news-b1056",
                "person_id": PEOPLE[7][0],
                "organization_key": "greenville-news-b1056",
                "organization_name_as_found": "Greenville News",
                "role_title": "Washington correspondent",
                "occupation": "newspaper correspondent",
                "relationship_type": "employment",
                "start_date": "1937",
                "end_date": "1942",
                "date_precision": "NARA dates McKeever's correspondent work to 1937-1942; his first-person interview names the Greenville News as another paper he represented.",
                "city": "Washington",
                "state_or_region": "District of Columbia",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "A_direct_official",
                "publication_status": "published",
                "research_notes": "Concurrent newspaper representation is allowed; this is not collapsed into the Raleigh paper.",
            },
            {
                "key": "porter-mckeever-owi-b1056",
                "person_id": PEOPLE[7][0],
                "organization_key": "owi-b1056",
                "organization_name_as_found": "Office of War Information Psychological Warfare Team",
                "role_title": "Psychological Warfare Team member",
                "occupation": "wartime information and psychological-warfare work",
                "relationship_type": "government_assignment",
                "date_precision": "Emmerson places McKeever on the wartime North Burma OWI team but does not establish its sequence relative to any OSS assignment.",
                "state_or_region": "North Burma",
                "country": "Burma",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "temporal_relation_uncertain",
                "identity_confidence": "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "publish_qualified",
                "research_notes": "OWI is explicitly not labeled OSS. The reviewed article distinguishes OWI's overt propaganda from OSS work.",
            },
            {
                "key": "donald-mackinnon-bryn-mawr-b1056",
                "person_id": PEOPLE[35][0],
                "organization_key": "bryn-mawr-b1056",
                "organization_name_as_found": "Bryn Mawr College",
                "role_title": "professor of psychology",
                "occupation": "psychologist and professor",
                "relationship_type": "employment",
                "start_date": "1933",
                "end_date": "1947",
                "date_precision": "The institutional memorial dates the professorship to 1933-1947 and says he was on leave in 1944-1946 to direct OSS Station S.",
                "city": "Bryn Mawr",
                "state_or_region": "Pennsylvania",
                "country": "United States",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "explicit_immediate",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "The continuing professorship and wartime leave are represented accurately; no resignation is inferred.",
            },
            {
                "key": "marjorie-mckillop-uw-b1056",
                "person_id": PEOPLE[25][0],
                "organization_key": "uw-b1056",
                "organization_name_as_found": "University of Washington",
                "role_title": "student",
                "occupation": "student of French",
                "relationship_type": "student",
                "start_date": "1917",
                "end_date": "1918",
                "date_precision": "The 1977 affidavit states that Marjorie L. McKillop was a University of Washington senior in French during 1917-1918.",
                "city": "Seattle",
                "state_or_region": "Washington",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "probable",
                "claim_confidence": "medium",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "publish_qualified",
                "research_notes": "Student status is not employment. The rare-name match remains probable pending Box 509 confirmation.",
            },
            {
                "key": "marjorie-mckillop-signal-corps-b1056",
                "person_id": PEOPLE[25][0],
                "organization_key": "signal-corps-b1056",
                "organization_name_as_found": "United States Army Signal Corps",
                "role_title": "telephone operator, Unit Four",
                "occupation": "telephone operator",
                "relationship_type": "military_assignment",
                "start_date": "1918-02",
                "end_date": "1919",
                "date_precision": "The affidavit dates sworn service from February 1918 through 1919 and describes assignments in France; the exact discharge date is not stated.",
                "country": "United States / France",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "probable",
                "claim_confidence": "medium",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "publish_qualified",
                "research_notes": "This is a much earlier military assignment, not an OSS predecessor and not a civilian employer.",
            },
        ]
    )
    return values


def claim(
    key: str,
    row: int,
    claim_type: str,
    claim_text: str,
    evidence_paraphrase: str,
    identity_match_assessment: str,
    temporal_assessment: str,
    source_quality: str,
    claim_confidence: str,
    publication_status: str,
    match_notes: str,
    source_links: list[dict[str, str]],
    affiliation_key: str | None = None,
    evidence_excerpt: str | None = None,
) -> dict[str, object]:
    value: dict[str, object] = {
        "key": key,
        "person_id": PEOPLE[row][0],
        "claim_type": claim_type,
        "claim_text": claim_text,
        "evidence_paraphrase": evidence_paraphrase,
        "identity_match_assessment": identity_match_assessment,
        "temporal_assessment": temporal_assessment,
        "source_quality": source_quality,
        "claim_confidence": claim_confidence,
        "publication_status": publication_status,
        "match_notes": match_notes,
        "sources": source_links,
    }
    if affiliation_key:
        value["affiliation_key"] = affiliation_key
    if evidence_excerpt:
        value["evidence_excerpt"] = evidence_excerpt
    return value


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, label, _relationship, locator) in ARMY_OCCUPATIONS.items():
        values.append(
            claim(
                f"identity-{slug(PEOPLE[row][1])}-army-b1056",
                row,
                "identity",
                f"The indexed {PEOPLE[row][1]} has a high-confidence match to an official Army entry.",
                "The normalized full name and a reviewed nonshared protected identifier agree; the identifier remains private.",
                "High confidence from exact normalized full-name agreement and a unique protected-identifier match.",
                "The Army entry establishes wartime identity context but not the exact OSS sequence.",
                "A_direct_official",
                "high",
                "published",
                "Identity crosswalk only; the Army category is assessed separately and is not a named employer.",
                [{"source_key": INDEX, "support_type": "context_only"}, {"source_key": ARMY}],
            )
        )
        values.append(
            claim(
                f"army-entry-{slug(PEOPLE[row][1])}-b1056",
                row,
                "occupation",
                f"At Army entry on {date}, {PEOPLE[row][1]} was recorded as {occupation}; no employer, institution, or workplace is identified.",
                f"The official Army bulk file records code {code}; the visually checked official list defines the category as {label}.",
                "High confidence from matching official name evidence and a reviewed, nonshared private identifier linkage; the identifier remains private.",
                "The category is fixed to the Army-entry date, but its sequence relative to OSS service is not established.",
                "A_direct_official",
                "medium",
                "publish_qualified",
                "The historical category remains qualified, excluded from verified-employer analytics, and is not converted into a named organization.",
                [
                    {"source_key": INDEX, "support_type": "context_only"},
                    {"source_key": ARMY},
                    {"source_key": TECH, "support_type": "context_only"},
                    {"source_key": CODES, "locator_override": locator},
                ],
                army_affiliation_key(row),
            )
        )
    for row in sorted(IDENTITY_ONLY_ARMY):
        values.append(
            claim(
                f"identity-{slug(PEOPLE[row][1])}-army-b1056",
                row,
                "identity",
                f"The indexed {PEOPLE[row][1]} has a high-confidence match to an official Army entry.",
                "The normalized full name and a reviewed nonshared protected identifier agree; the identifier remains private.",
                "High confidence from exact normalized full-name agreement and a unique protected-identifier match.",
                "The Army entry establishes identity context but its unverified code is not interpreted.",
                "A_direct_official",
                "high",
                "published",
                "Code 515 or 999 is not converted into an occupation because the reviewed official code list did not yield a defensible definition.",
                [{"source_key": INDEX, "support_type": "context_only"}, {"source_key": ARMY}],
            )
        )
    porter_identity = "High confidence from the rare exact name, first-person newspaper history, a NARA-dated White House correspondent entry, and an independent wartime OWI team identification."
    values.extend(
        [
            claim(
                "identity-porter-mckeever-b1056", 7, "identity",
                "The indexed Porter H. McKeever is a high-confidence match to journalist and wartime Office of War Information team member Porter McKeever.",
                "First-person, official finding-aid, and professional-journal sources converge on the same rare-named journalist and wartime information officer.",
                porter_identity,
                "The sources cover 1937-1942 journalism and wartime OWI work; the exact OSS sequence remains unverified.",
                "A_direct_official", "high", "published",
                "The OWI and OSS organizations remain distinct, and the middle initial is not expanded without direct evidence.",
                [{"source_key": INDEX, "support_type": "context_only"}, {"source_key": CSPAN}, {"source_key": FDR}, {"source_key": AFSA}],
            ),
            claim(
                "porter-mckeever-news-observer-b1056", 7, "last_civilian_pre_service",
                "Porter McKeever represented the Raleigh News and Observer in Washington during his 1937-1942 White House correspondent career.",
                "McKeever directly named the newspaper; NARA independently dates his White House correspondent work to 1937-1942.",
                porter_identity,
                "Strongly date-bounded civilian work ending in 1942 before the documented wartime OWI assignment; the exact OSS entry date is unknown.",
                "A_direct_official", "high", "published",
                "Published as a last documented civilian employer before wartime government work, not as an explicitly immediate OSS predecessor.",
                [{"source_key": CSPAN}, {"source_key": FDR}],
                "porter-mckeever-news-observer-b1056",
                "the Raleigh News and Observer which I represented",
            ),
            claim(
                "porter-mckeever-greenville-news-b1056", 7, "last_civilian_pre_service",
                "Porter McKeever also represented the Greenville News as a Washington correspondent during the same prewar reporting career.",
                "McKeever directly identified the Greenville News as his South Carolina paper; NARA dates the broader correspondent period to 1937-1942.",
                porter_identity,
                "Strongly date-bounded concurrent civilian work before wartime OWI service; the exact end date for this newspaper alone is not separately stated.",
                "A_direct_official", "high", "published",
                "Concurrent newspaper employers remain separate and confidence-aware.",
                [{"source_key": CSPAN}, {"source_key": FDR}],
                "porter-mckeever-greenville-news-b1056",
                "my paper in South Carolina, the Greenville News",
            ),
            claim(
                "porter-mckeever-owi-b1056", 7, "occupation",
                "Porter McKeever served on an Office of War Information Psychological Warfare Team in North Burma during the war.",
                "John K. Emmerson identifies McKeever among the OWI team and explicitly distinguishes OWI's overt propaganda from OSS.",
                porter_identity,
                "Documented wartime government assignment; the sequence relative to any OSS assignment is uncertain.",
                "C_reputable_contemporary_or_scholarly", "medium", "publish_qualified",
                "OWI is not relabeled as OSS and is excluded from immediate-predecessor analytics.",
                [{"source_key": AFSA}],
                "porter-mckeever-owi-b1056",
            ),
            claim(
                "identity-donald-wallace-mackinnon-b1056", 35, "identity",
                "The indexed Donald W. McKinnon is a high-confidence match to psychologist Donald Wallace MacKinnon, director of OSS Station S.",
                "The Berkeley memorial supplies the full middle name, matching initial, professorial chronology, and explicit OSS Station S directorship.",
                "High confidence from exact first name and middle initial, a documented spelling variant, distinctive profession, and explicit OSS assignment.",
                "The institutional chronology directly covers the transition into OSS.",
                "B_authoritative_institutional", "high", "published",
                "MacKinnon is preserved as a documented name variant; the index spelling remains visible.",
                [{"source_key": INDEX, "support_type": "context_only"}, {"source_key": BERKELEY}],
            ),
            claim(
                "donald-mackinnon-bryn-mawr-b1056", 35, "immediate_pre_oss_affiliation",
                "Donald Wallace MacKinnon was a Bryn Mawr College professor and went on leave in 1944 to direct OSS Station S.",
                "The Berkeley memorial dates the professorship to 1933-1947 and the OSS leave to 1944-1946.",
                "High confidence from the institutional memorial's name, middle initial, profession, dates, and explicit Station S assignment.",
                "Explicit immediate civilian-employment-to-OSS sequence; the professorship continued while he was on leave.",
                "B_authoritative_institutional", "high", "published",
                "The claim does not imply he resigned from Bryn Mawr or that the college employed him for OSS work.",
                [{"source_key": BERKELEY}],
                "donald-mackinnon-bryn-mawr-b1056",
                "on leave in 1944-46 to serve as director of Station S",
            ),
            claim(
                "identity-richard-v-mclallen-b1056", 46, "identity",
                "The indexed Major Richard V. McLallen is a high-confidence match to the OSS major named in European Theater awards-board minutes.",
                "An official OSS record gives the exact name and major rank under the Special Operations Branch awards list.",
                "High confidence from exact full name, middle initial, matching major rank, and direct OSS document context.",
                "The 1945 record confirms wartime OSS service but supplies no predecessor affiliation.",
                "A_direct_official", "high", "published",
                "No employer or earlier military assignment is inferred from the award listing.",
                [{"source_key": INDEX, "support_type": "context_only"}, {"source_key": MCLALLEN}],
                evidence_excerpt="Major Richard V. McLallen Approved",
            ),
            claim(
                "identity-marjorie-leslie-mckillop-b1056", 25, "identity",
                "The indexed Marjorie L. McKillop is a probable match to Marjorie Leslie McKillop, the University of Washington student and World War I Signal Corps operator.",
                "A sworn affidavit expands the rare exact name and gives a detailed institutional and military chronology, but does not independently mention OSS.",
                "Probable from the rare exact first name, middle initial, surname, and historically compatible age; Box 509 is still required for a direct OSS bridge.",
                "The documented roles predate OSS by more than two decades and are not treated as immediate predecessors.",
                "C_reputable_contemporary_or_scholarly", "medium", "publish_qualified",
                "The identity and both affiliations remain visibly qualified and are excluded from default analytics.",
                [{"source_key": INDEX, "support_type": "context_only"}, {"source_key": MCKILLOP}],
            ),
            claim(
                "marjorie-mckillop-uw-b1056", 25, "other_pre_oss_affiliation",
                "Probable identity Marjorie Leslie McKillop was a University of Washington senior studying French in 1917-1918.",
                "Her 1977 affidavit directly states the institution, dates, class standing, and field of study.",
                "Probable identity pending direct personnel-file corroboration.",
                "Documented prewar student status, not employment and not an immediate OSS predecessor.",
                "C_reputable_contemporary_or_scholarly", "medium", "publish_qualified",
                "Student status is kept separate from employer analytics.",
                [{"source_key": MCKILLOP}],
                "marjorie-mckillop-uw-b1056",
            ),
            claim(
                "marjorie-mckillop-signal-corps-b1056", 25, "other_pre_oss_affiliation",
                "Probable identity Marjorie Leslie McKillop served as a Signal Corps telephone operator in France from 1918 to 1919.",
                "The sworn affidavit describes enlistment, training, overseas orders, Le Havre duty, Paris and Brest assignments, and return in 1919.",
                "Probable identity pending direct personnel-file corroboration.",
                "Documented World War I military assignment, not a civilian employer and not an immediate OSS predecessor.",
                "C_reputable_contemporary_or_scholarly", "medium", "publish_qualified",
                "The later legal-status dispute surrounding the operators does not change the project's relationship classification.",
                [{"source_key": MCKILLOP}],
                "marjorie-mckillop-signal-corps-b1056",
            ),
        ]
    )
    return values


def unresolved_message(name: str, box: str) -> str:
    return (
        f"Review the indexed Box {box} personnel file for corroborating identifiers, the immediate pre-OSS affiliation, and the last civilian employer. "
        "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed."
    )


def person_updates() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for person_id, (row, _person_id, name, box) in UNIQUE_PEOPLE.items():
        update: dict[str, object] = {
            "person_id": person_id,
            "manual_review_required": True,
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
        }
        if row in ARMY_OCCUPATIONS:
            update.update(
                identity_status="high_confidence",
                identity_evidence="The official index and Army entry agree in normalized full name and a reviewed nonshared private identifier. The identifier remains private; the dated broad category does not establish a named employer or OSS sequence.",
                nara_catalog_id="1263923",
                research_status="occupation_only_found",
                next_action=f"Review Box {box} for a named employer or institution and establish the Army-to-OSS chronology.",
                archival_review_priority="high",
            )
        elif row in IDENTITY_ONLY_ARMY:
            update.update(
                identity_status="high_confidence",
                identity_evidence="The official index and Army entry agree in normalized full name and a reviewed nonshared private identifier. The unidentified historical code is not interpreted or published.",
                nara_catalog_id="1263923",
                research_status="requires_archival_review",
                next_action=f"Review Box {box} for a named affiliation and resolve the Army-entry code before making an occupation claim.",
                archival_review_priority="high",
            )
        elif row == 7:
            update.update(
                manual_review_required=False,
                identity_status="high_confidence",
                identity_evidence="The rare exact name, first-person newspaper history, NARA-dated correspondent entry, and independent wartime OWI team identification converge on one person.",
                research_status="verified_employer_found",
                next_action="Review Box 508 to establish the exact OWI-to-OSS sequence and whether either newspaper was the immediate OSS predecessor.",
                archival_review_priority="medium",
            )
        elif row == 35:
            update.update(
                manual_review_required=False,
                identity_status="high_confidence",
                identity_evidence="The exact first name and middle initial, documented MacKinnon spelling variant, psychology profession, and explicit OSS Station S directorship support a high-confidence match.",
                name_variants=["Donald Wallace MacKinnon", "Donald W MacKinnon"],
                research_status="verified_employer_found",
                next_action="Review Box 509 for the personnel-file appointment date and any predecessor affiliation before the Bryn Mawr professorship.",
                archival_review_priority="medium",
            )
        elif row == 46:
            update.update(
                identity_status="high_confidence",
                identity_evidence="An official OSS European Theater record gives the exact Richard V. McLallen name and matching major rank under a Special Operations Branch award list.",
                research_status="requires_archival_review",
                next_action="Review Box 510 to identify McLallen's pre-OSS employer or military assignment and the meaning of the index note 'also AS'.",
                archival_review_priority="high",
            )
        elif row == 25:
            update.update(
                identity_status="probable",
                identity_evidence="A sworn affidavit expands the rare exact indexed name to Marjorie Leslie McKillop and supplies an age-compatible institutional and military history, but no source independently bridges her to OSS.",
                name_variants=["Marjorie Leslie McKillop"],
                research_status="needs_identity_review",
                next_action="Review Box 509 to confirm the Marjorie Leslie McKillop identity and establish her immediate pre-OSS affiliation and last civilian employer.",
                archival_review_priority="critical",
            )
        elif row == 6:
            update.update(
                identity_status="ambiguous",
                identity_evidence="The rare exact name has an age-compatible wartime candidate, but accessible cemetery evidence describes U.S. Navy service while the index prints PFC. No direct OSS or private-identifier bridge was found.",
                research_status="needs_identity_review",
                next_action="Review Box 508 to resolve the Army-rank versus Navy-service conflict before transferring any directory occupation or military chronology.",
                archival_review_priority="critical",
            )
        elif row in {10, 11}:
            update.update(
                identity_status="ambiguous",
                identity_evidence="Adjacent rows share the same indexed name, lieutenant-colonel rank, box, and location but carry different protected identifiers. They remain separate without direct duplicate evidence.",
                possible_duplicate_group="p311-stewart-l-mckenney-adjacent-distinct-identifiers-b1056",
                research_status="needs_identity_review",
                next_action="Compare both Stewart L. McKenney personnel files in Box 508 before merging or transferring any affiliation evidence.",
                archival_review_priority="critical",
            )
        elif row == 12:
            update.update(
                identity_status="conflicting",
                identity_evidence="The indexed James A. McKenskey protected identifier maps to an official Army entry for Philip Cappella. The name conflict remains unresolved and no Army occupation is transferred.",
                research_status="conflicting_sources",
                next_action="Review Box 509 and the original index documentation to resolve the James A. McKenskey / Philip Cappella identifier conflict.",
                archival_review_priority="critical",
            )
        elif row == 42:
            update.update(
                identity_status="ambiguous",
                identity_evidence="A separate Technician Fifth Grade Kenneth L. McKown row carries a different protected identifier from the two linked unranked rows. Name alone is insufficient to merge them.",
                possible_duplicate_group="p311-kenneth-l-mckown-distinct-identifiers-b1056",
                research_status="needs_identity_review",
                next_action="Compare the Kenneth L. McKown personnel files in Boxes 508-509 before any merge or transfer of the accepted Army occupation.",
                archival_review_priority="critical",
            )
        else:
            update.update(
                identity_status="unresolved",
                identity_evidence="Exact-name and meaningful-variant checks across the official index context, CIA-domain discovery, accessible military and institutional sources, newspaper or obituary discovery, and archival searches produced no reliable identity and pre-OSS affiliation bridge; unbridged namesakes were rejected.",
                research_status="requires_archival_review",
                next_action=unresolved_message(name, box),
                archival_review_priority="high",
            )
        values.append(update)
    if len(values) != 45 or len({item["person_id"] for item in values}) != 45:
        raise RuntimeError("Expected 45 unique page-311 person updates")
    return values


def outcome_note(row: int) -> str:
    if row in ARMY_OCCUPATIONS:
        return "An accepted official Army identity link supports a qualified dated occupation or student category but no named employer or OSS-transfer sequence."
    if row in IDENTITY_ONLY_ARMY:
        return "An accepted official Army identity link supports identity only; code 515 or 999 was not interpreted or published."
    if row == 7:
        return "First-person, NARA, and professional-journal evidence establishes Porter McKeever's newspaper employment and wartime OWI assignment while preserving the OWI/OSS distinction."
    if row == 35:
        return "Berkeley's institutional memorial explicitly establishes Donald Wallace MacKinnon's Bryn Mawr professorship and 1944 leave to direct OSS Station S."
    if row == 46:
        return "An official OSS awards-board record confirms Richard V. McLallen's identity and rank but does not identify a predecessor affiliation."
    if row == 25:
        return "A rare-name affidavit supports a probable identity and qualified early student and Signal Corps history; Box 509 remains necessary for the OSS bridge."
    if row in {6, 10, 11, 42}:
        return "A duplicate or military-branch conflict remains visible; no occupation or employer was transferred across unresolved identities."
    if row == 12:
        return "The protected-identifier conflict remains visible; no occupation or employer was transferred."
    return "No reliable identity or pre-OSS affiliation was established; unbridged namesakes and chronologically irrelevant results were rejected."


def research_attempts() -> list[dict[str, object]]:
    updates = {item["person_id"]: item for item in person_updates()}
    positive_rows = set(ARMY_OCCUPATIONS) | IDENTITY_ONLY_ARMY | {7, 25, 35, 46}
    review_rows = {6, 10, 11, 12, 42}
    values: list[dict[str, object]] = []
    for person_id, (row, _person_id, name, box) in UNIQUE_PEOPLE.items():
        if row in positive_rows:
            outcome, reviewed, rejected = "source_reviewed", 5, 3
        elif row in review_rows:
            outcome, reviewed, rejected = "candidate_rejected", 3, 4
        else:
            outcome, reviewed, rejected = "no_result", 2, 3
        values.append(
            {
                "key": f"page311-row{row}-{slug(name)}-b1056",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index context; exact-name and meaningful initial, punctuation, spacing, spelling and OCR variants; CIA Reading Room/domain discovery; OSS, rank, branch, assignment and private-identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory and archival searches; indexed Box {box}",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_1056",
                "started_at": "2026-11-11T18:15:00-05:00",
                "completed_at": "2026-11-11T20:10:00-05:00",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, postwar-only leads, and sources without an OSS, rank, private-identifier, unit, or personnel-file bridge were rejected. Army categories were not converted into named employers; codes 515 and 999 were not interpreted; the separate Kenneth L. McKown identifiers were not merged; and OWI was not relabeled as OSS.",
                "research_notes": f"{outcome_note(row)} Page 311 was visually checked against a fresh official NARA download matching the preserved SHA-256. The official index, existing Library of Congress attempts where present, exact-name OSS and meaningful-variant discovery, CIA-domain checks, employment and occupation checks, and obituary, institutional, directory, newspaper, and archival searches were reviewed as applicable. CIA-domain searches returned no additional person-specific evidence and were not treated as proof of absence. No search-result snippet was used as final evidence and no authenticated NARA Catalog API request was made.",
                "next_action": str(updates[person_id]["next_action"]),
                "attempt_number": ATTEMPT_NUMBERS[row],
                "research_agent_version": "before-oss-b1056-v1",
            }
        )
    if len(values) != 45 or len({item["person_id"] for item in values}) != 45:
        raise RuntimeError("Expected 45 unique page-311 research attempts")
    return values


def build_bundle() -> dict[str, object]:
    return {
        "bundle_version": "batch-1056-v1",
        "reviewer": "Before OSS Batch 1056 evidence review",
        "sources": sources(),
        "organizations": organizations(),
        "affiliations": affiliations(),
        "claims": claims(),
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }


def main() -> None:
    bundle = build_bundle()
    EvidenceBundle.model_validate(bundle)
    OUTPUT.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
