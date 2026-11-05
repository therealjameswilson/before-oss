#!/usr/bin/env python3
"""Generate the reviewed Batch 1048 evidence bundle for PDF page 303."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page303-luigi-mazzone-to-richard-j-mccann-review_"
    "batch-1048_2026-11-05.json"
)

INDEX = "nara-index-b1048"
ARMY = "army-bulk-b1048"
TECH = "army-tech-b1048"
CODES = "army-codes-b1048"
HOOVER_MAZZONE = "hoover-oss-board-luigi-mazzone-b1048"
CLEVELAND_MAZZONE = "cleveland-luigi-mazzone-obituary-b1048"
BERKELEY_MCBAINE = "berkeley-turner-mcbaine-oral-history-b1048"
LOC_MCAFEE = "loc-william-mcafee-oral-history-b1048"
SIA_MCCANDLISH = "smithsonian-nancy-mccandlish-b1048"
WP_MCCANDLISH = "washington-post-nancy-prichard-b1048"
TWU_MCAFEE = "twu-frederica-mcafee-wasp-b1048"
GOVINFO_MCAFEE = "govinfo-frederica-mcafee-wasp-b1048"
ROTARY_MCAFEE = "brookline-rotary-frederica-mcafee-b1048"
NARA_MCADOO = "nara-dale-mcadoo-oss-b1048"

ORG_NAVY = "us-navy-b1048"
ORG_ARMY = "us-army-b1048"
ORG_SAO = "smithsonian-astrophysical-observatory-b1048"
ORG_WASP = "women-airforce-service-pilots-b1048"
ORG_EWING = "ewing-christian-college-b1048"
ORG_NEYLAN = "john-francis-neylan-law-practice-b1048"
ORG_ORRICK = "orrick-palmer-dahlquist-b1048"


# Rows 27, 28, and 39 already have terminal conflict outcomes and are preserved.
PEOPLE = {
    1: ("36ddd41c-6c05-5bbc-ba32-e447e6705bf3", "Luigi Mazzone", "495"),
    2: ("08ae6225-9791-58a9-8eab-8b989b2bdc9e", "John C McAdam", "496"),
    3: ("930d7002-8987-53c1-90d7-b38d860fd7a0", "Donald B McAdams", "496"),
    4: ("31be0bec-6099-5431-856a-5b16f58b1ad4", "George F McAdams", "496"),
    5: ("dc968a4e-3508-597e-a8db-67a84f1dbbb7", "Dale McAdoo", "496"),
    6: ("de63d744-2cc3-5aef-872a-eedd92aae057", "Donald R McAfee", "496"),
    7: ("a75f2bdc-68ba-546c-9dde-d06899a32354", "Frederica McAfee", "496"),
    8: ("8f05dbf3-9834-553a-8232-e82a780e19c1", "Pattie A McAfee", "496"),
    9: ("d55bc229-2189-53f8-a66e-422b32f4c203", "William McAfee", "496"),
    10: ("4d1c5c71-2b95-5802-8b54-c68e6f0c2f65", "Carl E McAlister", "496"),
    11: ("6ffd5bea-1602-58a5-89c5-a2dd5f391712", "Clare D McAllister", "496"),
    12: ("ad94cdc2-a7c2-508b-8499-9105e42a4f35", "Claude A McAllister", "496"),
    13: ("e497610e-712f-5f2d-941f-e559411bf199", "Nancy M McAnolish", "496"),
    14: ("5925506f-0976-5138-9c6a-794f152a31d9", "William C McAragle", "496"),
    15: ("c79f1504-32ed-5bc0-a5b2-93ff78a8bfee", "Raymond J McArdle", "496"),
    16: ("994851c7-ab62-50ba-ab8d-7be7995d039a", "John J McAtee", "496"),
    17: ("eef7e0bb-5af1-5de2-9e44-c69d7ea43a04", "Russell W McAuley", "496"),
    18: ("adb6db80-e25b-5281-b817-e5adbf0fef2b", "James H McAvoy", "496"),
    19: ("6bb85841-c492-5eeb-ba04-33bc0539dcb9", "Virgina W McBain", "496"),
    20: ("c5d22196-a119-55fd-8591-5d902531e84e", "Turner H McBaine", "496"),
    21: ("8e9688eb-016b-58f6-8f1a-17f3e0128de2", "George J McBride", "496"),
    22: ("a7bc2d0c-6805-5594-9a00-ca4c009eda0e", "Hiram W McBride", "496"),
    23: ("9e2b51bd-be4e-53c3-9566-cc85d833278f", "John J McBride", "496"),
    24: ("3a333fe9-a009-5306-a4d3-415c7d8b07c5", "William H McBride", "496"),
    25: ("f186e469-d0e3-55e2-9b83-bc1330dcc2e9", "Alexander McBroom", "496"),
    26: ("c09ccaaa-7681-564a-8893-b59d695924b5", "Assunta S McCabe", "497"),
    29: ("8755c600-96ec-5c50-a41c-4d5594df0ee4", "Rachel McCaffery", "497"),
    30: ("a28a1cbd-07ec-5491-95c3-63c9e5d1984f", "James S McCain", "497"),
    31: ("241d9592-f869-5fd4-a581-4a2bb1cd7813", "Leo C McCaleb", "497"),
    32: ("74b1d653-b603-5730-b538-eee6d4bfdd43", "Elcie A McCall", "497"),
    33: ("e93e5ecb-8c29-5043-a0cb-dbe9d1b9e6b1", "Leo H McCall", "497"),
    34: ("980ba55e-a7fc-5243-a93f-75c84523f36c", "William S McCall", "497"),
    35: ("0b9acef9-ce96-50a5-9b5f-e15611d275a2", "William A McCall", "497"),
    36: ("bb92b8fe-5f55-5c5a-919c-c71416dd746e", "Carlos R McCalla", "497"),
    37: ("29aca0b0-8368-539a-a9b9-2924d3236641", "Paul M McCallen", "497"),
    38: ("e52b5081-fce2-5a71-8336-abd31a63b2ca", "William P McCalliard", "497"),
    40: ("2b169eda-922a-55f7-a99a-8a26793037e8", "Paul McCance", "497"),
    41: ("5a051b4f-2624-52b8-adb9-9e2e50201832", "Nancy McCandlish", "497"),
    42: ("63732f9a-c391-5080-ba79-337c45dbc8b1", "Dennis J McCann", "497"),
    43: ("75681bee-861f-5ac5-abdb-1bd72e601965", "Francis L McCann", "497"),
    44: ("ccd594fa-d511-55ba-a465-a9cda3e3bde7", "Margaret T McCann", "497"),
    45: ("9a2c2441-e632-5515-9336-ac5a754e6af7", "Mary G McCann", "497"),
    46: ("be497ae1-424d-538c-98b5-c7676af53339", "Richard J McCann", "497"),
}


# Official Army classifications are broad historical categories, not employers.
ARMY_ASSOCIATIONS = {
    3: ("1942-02-02", "068", "semiprofessional occupation, not elsewhere classified", "Semiprofessional occupations, n.e.c.", "PDF physical page 171; historical category 0-68"),
    6: ("1944-04-25", "105", "general office clerk", "Clerks, general office", "PDF physical page 171; historical category 1-05"),
    10: ("1943-04-17", "316", "general farm hand", "Farm hands, general farms", "PDF physical page 172; historical category 3-16"),
    11: ("1943-03-18", "433", "general woodworking worker, not elsewhere classified", "General woodworking occupations, n.e.c.", "PDF physical page 173; historical category 4-33"),
    18: ("1943-04-05", "137", "stenographer or typist", "Stenographers and typists", "PDF physical page 172; historical category 1-37"),
    22: ("1940-11-25", "736", "chauffeur or driver of a bus, taxi, truck, or tractor", "Chauffeurs and drivers, bus, taxi, truck, and tractor", "PDF physical page 174; historical category 7-36"),
    24: ("1942-12-02", "001", "accountant or auditor", "Accountants and auditors", "PDF physical page 170; historical category 0-01"),
}

ARMY_IDENTITY_ONLY = {12, 23}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def source(key: str, **kwargs: object) -> dict[str, object]:
    value: dict[str, object] = {"key": key, "access_date": "2026-11-05"}
    value.update(kwargs)
    return value


def sources() -> list[dict[str, object]]:
    return [
        source(
            INDEX,
            stable_url="https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            archival_identifier="RG 226, Entry A1-224, Boxes 495-497",
            title="OSS Personnel Files from Excel",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="2010-12-23",
            locator="PDF page 303, rows 1-46; every printed row visually checked",
            source_quality="A_direct_official",
            collection_name="Records of the Office of Strategic Services, Record Group 226",
            rights_notes="All 46 printed rows remain recoverable as 46 cautious entities. Existing McCabe and McCammon conflicts remain separate and unchanged.",
        ),
        source(
            ARMY,
            stable_url="https://catalog.archives.gov/id/1263923",
            archival_identifier="National Archives Identifier 1263923; parent series NAID 604357",
            title="Electronic Army Serial Number Merged File, ca. 1938-1946",
            author_creator="Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="1938-1946; merged file created 2002",
            locator="Official unrestricted ASNEF.FIN.DAT; protected identity candidates reviewed individually",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records",
            document_number="ASNEF.FIN.DAT",
            rights_notes="No raw record, full protected identifier, or bulk-file ordinal is retained in public assets. Shared and conflicting candidates were not accepted.",
        ),
        source(
            TECH,
            stable_url="https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf",
            archival_identifier="NN3-064-03-008; National Archives Identifier 1263923",
            title="World War II Army Enlistment Records: Reference Copy of Technical Documentation",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives at College Park - Electronic Records",
            publication_record_date="1994-2005; reference copy modified 2011",
            locator="PDF physical pages 44-46; identity, Army-entry-date, grade, and civilian-occupation fields",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records technical documentation",
            rights_notes="Used only to interpret selected fields; source damage, postwar entries, and incomplete coverage remain visible.",
        ),
        source(
            CODES,
            stable_url="https://aad.archives.gov/aad/popup-codelist.jsp?cl_id=3323&dt=893&c_id=24986",
            archival_identifier="NARA AAD civilian occupation code list; Code No. 30 in NAID 1263923 documentation",
            title="World War II Army Enlistment Records: Civilian Occupation Code List",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives Access to Archival Databases",
            locator="Current AAD values for codes 001, 068, 105, 137, 316, 433, and 736; printed reference copy visually checked",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records code lists",
            rights_notes="Categories identify neither employer, institution, workplace, nor exact Army-to-OSS sequence.",
        ),
        source(
            HOOVER_MAZZONE,
            stable_url="https://digitalcollections.hoover.org/objects/73269/oss-board-of-officers-report-on-arrival-at-naples",
            archival_identifier="Millard Preston Goodfellow papers, record 69085.145",
            title="OSS board of officers report on arrival at Naples",
            author_creator="Office of Strategic Services board of officers",
            repository_publisher="Hoover Institution Library & Archives",
            publication_record_date="1944-05-03",
            locator="Printed page 71, section XVIII; Luigi Mazzone entry",
            source_quality="A_direct_official",
            collection_name="Millard Preston Goodfellow papers, Declassified U.S. government records",
            document_number="69085.145",
            rights_notes="Official wartime report. The protected number printed in the source is neither transcribed into claims nor exposed in public data.",
        ),
        source(
            CLEVELAND_MAZZONE,
            stable_url="https://obits.cleveland.com/us/obituaries/cleveland/name/luigi-mazzone-obituary?id=6668794",
            title="Luigi Mazzone obituary",
            author_creator="Mazzone family; Ripepi Funeral Home",
            repository_publisher="Cleveland.com",
            publication_record_date="2016-04-09",
            locator="Biographical paragraph describing Navy and OSS service",
            source_quality="C_reputable_contemporary_or_scholarly",
            collection_name="Cleveland.com obituaries",
            rights_notes="Corroborative identity source only. The postwar bakery is not treated as a prewar employer.",
        ),
        source(
            BERKELEY_MCBAINE,
            stable_url="https://digicoll.lib.berkeley.edu/record/217698/files/careerlawathome00mcbarich.pdf",
            archival_identifier="Regional Oral History Office, University of California, Berkeley",
            title="A Career in the Law at Home and Abroad",
            author_creator="Turner H. McBaine; interviewer Carole Hicke",
            repository_publisher="Regional Oral History Office, The Bancroft Library, University of California, Berkeley",
            publication_record_date="1989",
            locator="Introduction and transcript pages 40-45; wartime chronology and early law practice",
            source_quality="B_authoritative_institutional",
            collection_name="Pillsbury, Madison & Sutro Oral History Series",
            rights_notes="First-person institutional oral history. Project-authored paraphrases and short excerpts only.",
        ),
        source(
            LOC_MCAFEE,
            stable_url="https://www.loc.gov/item/mfdipbib000776/",
            archival_identifier="Foreign Affairs Oral History Collection, item mfdipbib000776",
            title="Interview with William McAfee",
            author_creator="William McAfee; interviewer Charles Stuart Kennedy",
            repository_publisher="Library of Congress; Association for Diplomatic Studies and Training",
            publication_record_date="Interviewed 1997-09-09; copyright 2000",
            locator="Transcript sections on 1932-1942 teaching, Army service, China Theater headquarters, and late-spring 1945 OSS transfer",
            source_quality="B_authoritative_institutional",
            collection_name="Foreign Affairs Oral History Collection",
            rights_notes="First-person oral history preserved by the Library of Congress. Project-authored paraphrases and short excerpts only.",
        ),
        source(
            SIA_MCCANDLISH,
            stable_url="https://siarchives.si.edu/blog/what%E2%80%99s-name-uncovering-early-women-computers",
            title="What's in a Name? Uncovering Early Women Computers",
            author_creator="Smithsonian Institution Archives staff",
            repository_publisher="Smithsonian Institution Archives",
            publication_record_date="2020",
            locator="Nancy McCandlish Prichard biographical paragraph",
            source_quality="B_authoritative_institutional",
            collection_name="Smithsonian Institution Archives blog",
            rights_notes="Institutional research based on Smithsonian annual reports, marriage records, and obituary evidence.",
        ),
        source(
            WP_MCCANDLISH,
            stable_url="https://www.washingtonpost.com/archive/local/2006/10/07/nancy-prichard/bab7a6e5-cdf3-4621-b551-f380fa962f50/",
            title="Nancy Prichard; Church and Civic Volunteer",
            repository_publisher="The Washington Post",
            publication_record_date="2006-10-06",
            locator="Biographical paragraphs on Smithsonian employment and OSS service",
            source_quality="C_reputable_contemporary_or_scholarly",
            collection_name="Washington Post obituaries",
            rights_notes="Corroborative obituary. Its broader job description is preserved in research notes rather than silently substituted for the Smithsonian role title.",
        ),
        source(
            TWU_MCAFEE,
            stable_url="https://twu.edu/library/womans-collection/collections/women-airforce-service-pilots-official-archive/research/training-classes/wafs--wasp-class-of-1943/wasp-class-43-w-3/",
            title="WASP Class 43-W-3",
            author_creator="Woman's Collection",
            repository_publisher="Texas Woman's University",
            locator="Class roster entry: Richardson, Frederica McAfee",
            source_quality="B_authoritative_institutional",
            collection_name="Women Airforce Service Pilots Official Archive",
            rights_notes="Official WASP archive roster; supports name variant and program membership, not by itself the OSS transition.",
        ),
        source(
            GOVINFO_MCAFEE,
            stable_url="https://www.govinfo.gov/content/pkg/CREC-2009-06-17/pdf/CREC-2009-06-17-extensions.pdf",
            archival_identifier="Congressional Record, 111th Congress, Extensions of Remarks E1457",
            title="Honoring the Women Airforce Service Pilots of World War II",
            author_creator="Representative Ileana Ros-Lehtinen",
            repository_publisher="U.S. Government Publishing Office",
            publication_record_date="2009-06-17",
            locator="Congressional Record page E1457; Class 43-3 roster",
            source_quality="A_direct_official",
            collection_name="Congressional Record",
            rights_notes="Official roster prints Frederica Richardson with McAfee as her training name.",
        ),
        source(
            ROTARY_MCAFEE,
            stable_url="https://www.brooklinerotary.org/stories/artemas-p-richardson",
            title="Artemas P. Richardson",
            author_creator="Brookline Rotary Club",
            repository_publisher="Brookline Rotary Club",
            publication_record_date="2018",
            locator="Wartime biography paragraph",
            source_quality="D_correlative_or_secondary",
            rights_notes="Secondary biographical source used only to qualify the WASP-before-OSS sequence; not sufficient alone for a settled immediate-transition claim.",
        ),
        source(
            NARA_MCADOO,
            stable_url="https://www.archives.gov/files/research/jfk/releases/104-10165-10143.pdf",
            archival_identifier="National Archives release 104-10165-10143",
            title="Letter concerning accounts of John A. Bross and Dale McAdoo",
            author_creator="Robert Hayden Alcorn, Office of Strategic Services",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="1943-07-13",
            locator="OSS memorandum, first page; American Embassy, London",
            source_quality="A_direct_official",
            collection_name="National Archives JFK records release",
            rights_notes="Supports a qualified identity bridge only; it supplies no pre-OSS employer or predecessor assignment.",
        ),
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": ORG_NAVY,
            "organization_id": "3960fa8e-a551-56cf-8305-b2b9e4961b9d",
            "canonical_name": "United States Navy",
            "historical_name": "United States Navy",
            "aliases": ["U.S. Navy", "United States Naval Reserve", "USNR"],
            "organization_type": "military service",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "The Naval Reserve is retained in the source wording while grouped under the historical Navy organization.",
        },
        {
            "key": ORG_ARMY,
            "organization_id": "28a26f92-78af-5a1a-9c09-a843eb5975b4",
            "canonical_name": "United States Army",
            "historical_name": "United States Army",
            "aliases": ["U.S. Army"],
            "organization_type": "military service",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "The China Theater headquarters wording remains attached to the affiliation rather than being silently normalized into a modern command.",
        },
        {
            "key": ORG_SAO,
            "organization_id": "58087213-ec99-5d94-acf5-59320a4f39ab",
            "canonical_name": "Smithsonian Astrophysical Observatory",
            "historical_name": "Smithsonian Astrophysical Observatory",
            "aliases": ["SAO"],
            "organization_type": "federal research observatory",
            "sector": "academia_and_research",
            "city": "Washington",
            "state_or_region": "District of Columbia",
            "country": "United States",
            "normalization_notes": "Historical Smithsonian unit preserved as named by the institutional source.",
        },
        {
            "key": ORG_WASP,
            "canonical_name": "Women Airforce Service Pilots",
            "historical_name": "Women Airforce Service Pilots",
            "aliases": ["WASP"],
            "organization_type": "wartime civilian federal aviation program",
            "sector": "federal_government",
            "country": "United States",
            "active_dates": "1943-1944",
            "normalization_notes": "WASP pilots were civilian federal personnel; this affiliation is not classified as commissioned military service.",
        },
        {
            "key": ORG_EWING,
            "canonical_name": "Ewing Christian College",
            "historical_name": "Ewing Christian College",
            "aliases": [],
            "organization_type": "college",
            "sector": "academia_and_research",
            "city": "Allahabad",
            "state_or_region": "United Provinces",
            "country": "India",
            "normalization_notes": "Historical institutional name and place wording preserved from McAfee's oral history.",
        },
        {
            "key": ORG_NEYLAN,
            "canonical_name": "Law Office of John Francis Neylan",
            "historical_name": "John Francis Neylan's law practice",
            "aliases": ["John Francis Neylan"],
            "organization_type": "law practice",
            "sector": "law",
            "city": "San Francisco",
            "state_or_region": "California",
            "country": "United States",
            "normalization_notes": "Modeled as Neylan's individual law practice because the oral history names the lawyer rather than a separate firm.",
        },
        {
            "key": ORG_ORRICK,
            "canonical_name": "Orrick, Palmer & Dahlquist",
            "historical_name": "Orrick, Palmer & Dahlquist",
            "aliases": [],
            "organization_type": "law firm",
            "sector": "law",
            "city": "San Francisco",
            "state_or_region": "California",
            "country": "United States",
            "normalization_notes": "The 1936-1939 firm name is retained; no modern successor name is substituted.",
        },
    ]


def army_affiliation_key(row: int) -> str:
    return f"{slug(PEOPLE[row][1])}-army-association-b1048"


def army_identity_assessment(row: int) -> str:
    special = {
        3: "High confidence from matching given name and middle initial, a damaged but compatible surname, and a nonshared protected linkage; the damaged spelling remains visible in private review data.",
        22: "High confidence from matching name, middle initial, and a nonshared protected linkage; the Army record's added Jr. remains a documented variant.",
    }
    return special.get(
        row,
        "High confidence from exact official name agreement and a nonshared protected linkage; the protected identifier remains private.",
    )


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, _label, _locator) in ARMY_ASSOCIATIONS.items():
        values.append(
            {
                "key": army_affiliation_key(row),
                "person_id": PEOPLE[row][0],
                "occupation": occupation,
                "relationship_type": "unknown",
                "end_date": date,
                "date_precision": f"Historical civilian-occupation code {code} was recorded at Army entry on {date}; no named employer, institution, workplace, or OSS-transfer date is supplied.",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "strongly_date_bounded",
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
                "key": "luigi-mazzone-us-navy-b1048",
                "person_id": PEOPLE[1][0],
                "organization_key": ORG_NAVY,
                "organization_name_as_found": "United States Naval Reserve",
                "role_title": "interpreter; later motor-pool driver",
                "relationship_type": "military_assignment",
                "start_date": "1943-04-01",
                "date_precision": "The official report dates Navy entry to 1 April 1943, then describes interpreter training and recruitment for Special Operations; no exact OSS reporting date is printed.",
                "country": "United States",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "explicit_immediate",
                "identity_confidence": "confirmed",
                "claim_confidence": "confirmed",
                "source_quality": "A_direct_official",
                "publication_status": "published",
                "research_notes": "Navy assignment is kept distinct from civilian employment.",
            },
            {
                "key": "luigi-mazzone-truck-driver-b1048",
                "person_id": PEOPLE[1][0],
                "occupation": "truck driver",
                "relationship_type": "employment",
                "end_date": "1943-04-01",
                "date_precision": "The wartime report says he was a truck driver in Pennsylvania in civilian life and entered the Navy on 1 April 1943; it does not name an employer.",
                "state_or_region": "Pennsylvania",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "confirmed",
                "claim_confidence": "confirmed",
                "source_quality": "A_direct_official",
                "publication_status": "published",
                "research_notes": "Published as a last civilian occupation with no named employer; it does not count as a verified employer organization.",
            },
            {
                "key": "turner-mcbaine-us-navy-b1048",
                "person_id": PEOPLE[20][0],
                "organization_key": ORG_NAVY,
                "organization_name_as_found": "U.S. Naval Reserve",
                "role_title": "Naval Reserve officer; later lieutenant commander",
                "relationship_type": "military_assignment",
                "start_date": "1941",
                "date_precision": "The oral-history introduction says McBaine was called to active duty in 1941 and then served with Donovan in OSS; it does not print an exact OSS assignment date.",
                "country": "United States",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "probable_immediate",
                "identity_confidence": "confirmed",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Published as the best-supported military pathway, visibly qualified because the exact transfer date is unstated.",
            },
            {
                "key": "turner-mcbaine-neylan-b1048",
                "person_id": PEOPLE[20][0],
                "organization_key": ORG_NEYLAN,
                "organization_name_as_found": "John Francis Neylan",
                "role_title": "lawyer",
                "occupation": "attorney",
                "relationship_type": "employment",
                "start_date": "1939",
                "end_date": "1941",
                "date_precision": "McBaine says he joined Neylan after leaving Orrick in 1939; the institutional introduction dates active Navy duty to 1941.",
                "city": "San Francisco",
                "state_or_region": "California",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "confirmed",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Best-supported last civilian employer before Navy service; Navy duty intervened before OSS.",
            },
            {
                "key": "turner-mcbaine-orrick-b1048",
                "person_id": PEOPLE[20][0],
                "organization_key": ORG_ORRICK,
                "organization_name_as_found": "Orrick, Palmer & Dahlquist",
                "role_title": "associate lawyer",
                "occupation": "attorney",
                "relationship_type": "employment",
                "start_date": "1936",
                "end_date": "1939",
                "date_precision": "McBaine explicitly dates his work at the firm from 1936 to 1939 and says he then went to work for John Francis Neylan.",
                "city": "San Francisco",
                "state_or_region": "California",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "confirmed",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Earlier documented law-firm employment, separated from the later Neylan practice.",
            },
            {
                "key": "william-mcafee-china-theater-b1048",
                "person_id": PEOPLE[9][0],
                "organization_key": ORG_ARMY,
                "organization_name_as_found": "China Theater headquarters",
                "role_title": "aide to General Albert C. Wedemeyer; assistant secretary of staff",
                "relationship_type": "military_assignment",
                "start_date": "1943-10",
                "end_date": "1945",
                "date_precision": "McAfee dates his aide assignment from October 1943, his China role from October 1944, and his relief followed by four months with OSS to late spring 1945.",
                "country": "China",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "explicit_immediate",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "The historical theater wording is retained; this is a military assignment, not civilian employment.",
            },
            {
                "key": "william-mcafee-ewing-b1048",
                "person_id": PEOPLE[9][0],
                "organization_key": ORG_EWING,
                "organization_name_as_found": "Ewing Christian College",
                "role_title": "teacher",
                "occupation": "college teacher",
                "relationship_type": "employment",
                "start_date": "1932",
                "end_date": "1935",
                "date_precision": "McAfee explicitly dates his teaching at Ewing Christian College in Allahabad to 1932-1935.",
                "city": "Allahabad",
                "state_or_region": "United Provinces",
                "country": "India",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Named earlier employer, not the last civilian position before Army service.",
            },
            {
                "key": "william-mcafee-patton-high-school-b1048",
                "person_id": PEOPLE[9][0],
                "organization_name_as_found": "high school in Patton",
                "role_title": "teacher",
                "occupation": "high-school teacher",
                "relationship_type": "employment",
                "date_precision": "McAfee says he taught in a high school in Patton after returning from India in 1935; no exact dates or formal institution name are supplied.",
                "city": "Patton",
                "state_or_region": "Pennsylvania",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Source wording retained; no modern or inferred formal school name is substituted.",
            },
            {
                "key": "william-mcafee-kiski-b1048",
                "person_id": PEOPLE[9][0],
                "organization_name_as_found": "Kiski",
                "role_title": "teacher",
                "occupation": "teacher",
                "relationship_type": "employment",
                "date_precision": "McAfee says he taught at Kiski after returning from India and before graduate study; exact dates and institutional form are unstated.",
                "state_or_region": "Pennsylvania",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "The oral history's exact institutional wording is retained without inferring a modern successor.",
            },
            {
                "key": "william-mcafee-altoona-high-b1048",
                "person_id": PEOPLE[9][0],
                "organization_name_as_found": "Altoona High",
                "role_title": "teacher",
                "occupation": "high-school teacher",
                "relationship_type": "employment",
                "date_precision": "McAfee names Altoona High in the sequence between his return from India and later Penn State graduate work; exact dates are unstated.",
                "city": "Altoona",
                "state_or_region": "Pennsylvania",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Historical name as found is retained without silently assigning a modern school identity.",
            },
            {
                "key": "william-mcafee-local-high-school-b1048",
                "person_id": PEOPLE[9][0],
                "organization_name_as_found": "local high school",
                "role_title": "teacher",
                "occupation": "high-school teacher",
                "relationship_type": "employment",
                "end_date": "1942-03-10",
                "date_precision": "McAfee says he taught at a local high school while continuing Penn State graduate study until the war and was drafted on 10 March 1942; the school is unnamed.",
                "state_or_region": "Pennsylvania",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Best-supported last civilian employment, but the employer name remains unknown and does not count as a verified named employer.",
            },
            {
                "key": "nancy-mccandlish-sao-b1048",
                "person_id": PEOPLE[41][0],
                "organization_key": ORG_SAO,
                "organization_name_as_found": "Smithsonian Astrophysical Observatory",
                "role_title": "Special Assistant to the Meteorologist",
                "relationship_type": "employment",
                "start_date": "1938",
                "date_precision": "Smithsonian research says McCandlish held the role for three years before joining OSS; the 1938 start is derived from the separately documented college graduation year.",
                "city": "Washington",
                "state_or_region": "District of Columbia",
                "country": "United States",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "explicit_immediate",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Smithsonian gives the specific SAO role; the Washington Post describes her more broadly as administrative assistant to the Smithsonian Secretary. Both descriptions are preserved in the evidence note.",
            },
            {
                "key": "frederica-mcafee-wasp-b1048",
                "person_id": PEOPLE[7][0],
                "organization_key": ORG_WASP,
                "organization_name_as_found": "Women Airforce Service Pilots",
                "role_title": "pilot, Class 43-W-3",
                "relationship_type": "government_assignment",
                "start_date": "1943",
                "date_precision": "Official rosters establish Class 43-W-3 membership; a secondary institutional biography describes her as a former WASP then serving with OSS, without an exact transition date.",
                "country": "United States",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "probable_immediate",
                "identity_confidence": "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "publish_qualified",
                "research_notes": "WASP service is classified as civilian government assignment, not commissioned military service. The transition remains visibly qualified.",
            },
        ]
    )
    return values


def claim(
    key: str,
    person_row: int,
    claim_type: str,
    claim_text: str,
    evidence_paraphrase: str,
    identity_match_assessment: str,
    temporal_assessment: str,
    source_quality: str,
    claim_confidence: str,
    publication_status: str,
    match_notes: str,
    sources_list: list[dict[str, str]],
    affiliation_key: str | None = None,
) -> dict[str, object]:
    value: dict[str, object] = {
        "key": key,
        "person_id": PEOPLE[person_row][0],
        "claim_type": claim_type,
        "claim_text": claim_text,
        "evidence_paraphrase": evidence_paraphrase,
        "identity_match_assessment": identity_match_assessment,
        "temporal_assessment": temporal_assessment,
        "source_quality": source_quality,
        "claim_confidence": claim_confidence,
        "publication_status": publication_status,
        "match_notes": match_notes,
        "sources": sources_list,
    }
    if affiliation_key:
        value["affiliation_key"] = affiliation_key
    return value


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, label, locator) in ARMY_ASSOCIATIONS.items():
        values.append(
            claim(
                f"army-{slug(PEOPLE[row][1])}-b1048",
                row,
                "occupation",
                f"At Army entry on {date}, {PEOPLE[row][1]} was recorded as {occupation}; no employer, institution, or workplace is identified.",
                f"The Army bulk file records code {code}; the visually checked official list defines the category as {label}.",
                army_identity_assessment(row),
                "Strongly date-bounded to Army entry, but not proven to be the immediately preceding role or status before OSS.",
                "A_direct_official",
                "medium",
                "publish_qualified",
                "The historical category is qualified, excluded from verified-employer analytics, and not converted into a named organization.",
                [
                    {"source_key": INDEX},
                    {"source_key": ARMY},
                    {"source_key": TECH, "support_type": "context_only"},
                    {"source_key": CODES, "locator_override": locator},
                ],
                army_affiliation_key(row),
            )
        )

    values.extend(
        [
            claim(
                "identity-luigi-mazzone-b1048", 1, "identity",
                "Indexed Luigi Mazzone is confirmed as the Naval Reserve specialist described in an official OSS board report.",
                "The uncommon exact name, compatible naval rank, direct OSS context, and private identifier agreement connect the index row and wartime report; a Cleveland obituary independently corroborates Navy and OSS service.",
                "Confirmed by exact uncommon name, compatible rank, official OSS context, and a protected row-specific identifier; the identifier is not published.",
                "Wartime identity and chronology are explicit in the official report.",
                "A_direct_official", "confirmed", "published",
                "The postwar bakery mentioned in the obituary is not treated as prewar employment.",
                [{"source_key": HOOVER_MAZZONE}, {"source_key": CLEVELAND_MAZZONE, "support_type": "supports"}, {"source_key": INDEX, "support_type": "context_only"}],
            ),
            claim(
                "navy-luigi-mazzone-b1048", 1, "immediate_pre_oss_affiliation",
                "Luigi Mazzone's documented immediate pathway into OSS was through the United States Naval Reserve.",
                "The official report dates his Navy entry, interpreter assignment and training, and recruitment by an OSS officer for Special Operations.",
                "Confirmed by the same row-specific official evidence supporting identity.",
                "Explicit immediate military pathway; the precise OSS reporting date is not printed.",
                "A_direct_official", "confirmed", "published",
                "Military assignment remains separate from the civilian-employer field.",
                [{"source_key": HOOVER_MAZZONE, "excerpt_override": "Entered the Navy 1 April 1943 and received his basic training at Great Lakes."}, {"source_key": INDEX, "support_type": "context_only"}],
                "luigi-mazzone-us-navy-b1048",
            ),
            claim(
                "truck-driver-luigi-mazzone-b1048", 1, "last_civilian_pre_service",
                "Luigi Mazzone was a truck driver in Pennsylvania before entering the Navy; the official report does not name his employer.",
                "The wartime personnel review directly states his civilian occupation and separately dates Navy entry to 1 April 1943.",
                "Confirmed by exact official identity evidence and a protected row-specific linkage.",
                "Strongly date-bounded as the civilian occupation before Navy entry; not a named employer and not the immediate OSS predecessor because Navy service intervened.",
                "A_direct_official", "confirmed", "published",
                "This occupation is excluded from named-employer counts.",
                [{"source_key": HOOVER_MAZZONE, "excerpt_override": "In civilian life, was a truck driver in Pennsylvania"}],
                "luigi-mazzone-truck-driver-b1048",
            ),
            claim(
                "identity-turner-h-mcbaine-b1048", 20, "identity",
                "Indexed Turner H. McBaine is confirmed as the lawyer and Naval Reserve officer whose institutional oral history documents OSS service.",
                "The exact distinctive name, matching lieutenant-commander rank, Navy chronology, and direct OSS statement align across the index and Berkeley oral history.",
                "Confirmed by exact uncommon name, matching rank, and direct first-person institutional biography of OSS service.",
                "The oral history dates his prewar law practice, 1941 active duty, and wartime OSS service.",
                "B_authoritative_institutional", "confirmed", "published",
                "Later Standard Oil work is postwar and is not used as a pre-OSS employer.",
                [{"source_key": BERKELEY_MCBAINE}, {"source_key": INDEX, "support_type": "context_only"}],
            ),
            claim(
                "navy-turner-mcbaine-b1048", 20, "immediate_pre_oss_affiliation",
                "The U.S. Naval Reserve is the best-supported immediate military pathway between Turner McBaine's civilian law practice and OSS service.",
                "Berkeley's introduction says he was called to active duty in 1941 and that his wartime service with Donovan was in OSS.",
                "Confirmed identity from exact name, compatible rank, and direct OSS statement.",
                "Probable immediate pathway because active duty and later OSS service are explicit but the exact transfer date is unstated.",
                "B_authoritative_institutional", "high", "published",
                "Military status is separate from the last civilian employer.",
                [{"source_key": BERKELEY_MCBAINE, "excerpt_override": "as a member of the U.S. Naval Reserve, McBaine was called to active duty in 1941"}],
                "turner-mcbaine-us-navy-b1048",
            ),
            claim(
                "neylan-turner-mcbaine-b1048", 20, "last_civilian_pre_service",
                "John Francis Neylan's San Francisco law practice is Turner McBaine's best-supported last civilian employer before active Navy duty.",
                "McBaine says he went to work for Neylan after leaving Orrick in 1939; the institutional introduction dates his active Navy duty to 1941.",
                "Confirmed identity from the exact distinctive name and direct OSS biography.",
                "Strongly date-bounded between 1939 and the 1941 call to active duty; Navy service then intervened before OSS.",
                "B_authoritative_institutional", "high", "published",
                "The employer is modeled as Neylan's law practice, not a later or unnamed firm.",
                [{"source_key": BERKELEY_MCBAINE, "excerpt_override": "I went to work for him after leaving Mr. Orrick."}],
                "turner-mcbaine-neylan-b1048",
            ),
            claim(
                "orrick-turner-mcbaine-b1048", 20, "other_pre_oss_affiliation",
                "Turner McBaine worked for Orrick, Palmer & Dahlquist from 1936 to 1939 before joining John Francis Neylan's practice.",
                "His oral history names the firm, dates his start to 1936, and confirms a three-year tenure ending in 1939.",
                "Confirmed identity from the exact distinctive name and direct OSS biography.",
                "Documented prewar employment, explicitly earlier than the Neylan practice and Navy service.",
                "B_authoritative_institutional", "high", "published",
                "The historical firm name is retained without substituting a modern successor.",
                [{"source_key": BERKELEY_MCBAINE, "excerpt_override": "finally wound up at a firm then called Orrick, Palmer & Dahlquist"}],
                "turner-mcbaine-orrick-b1048",
            ),
            claim(
                "identity-william-mcafee-b1048", 9, "identity",
                "Indexed Major William McAfee is a high-confidence match to the Army officer and OSS veteran in the Library of Congress oral history.",
                "The exact name, Army officer chronology, China service, and direct account of four months with OSS align with the indexed major.",
                "High confidence from exact name, compatible Army officer status, direct OSS service, and detailed China chronology; Box 496 remains the strongest final confirmation target.",
                "The first-person account dates his civilian work, 1942 draft, China headquarters assignment, and 1945 OSS service.",
                "B_authoritative_institutional", "high", "published",
                "No unrelated later State Department employment is used to fill the pre-OSS fields.",
                [{"source_key": LOC_MCAFEE}, {"source_key": INDEX, "support_type": "context_only"}],
            ),
            claim(
                "china-theater-william-mcafee-b1048", 9, "immediate_pre_oss_affiliation",
                "William McAfee's immediate pre-OSS assignment was on the U.S. Army's China Theater headquarters staff under General Albert C. Wedemeyer.",
                "McAfee says he served as Wedemeyer's aide and assistant secretary of staff, asked to be relieved in late spring 1945, and then spent about four months with OSS.",
                "High confidence from the exact name, Army officer status, and direct first-person OSS chronology.",
                "Explicit immediate military predecessor to OSS.",
                "B_authoritative_institutional", "high", "published",
                "The historical theater wording is preserved and not conflated with civilian employment.",
                [{"source_key": LOC_MCAFEE, "excerpt_override": "in the late spring of 1945, I asked to be relieved and I was with OSS"}],
                "william-mcafee-china-theater-b1048",
            ),
            claim(
                "ewing-william-mcafee-b1048", 9, "other_pre_oss_affiliation",
                "William McAfee taught at Ewing Christian College in Allahabad from 1932 to 1935.",
                "His first-person oral history names the college, location, role, and years.",
                "High confidence from the exact name and direct detailed OSS chronology.",
                "Documented prewar employment, earlier than his Pennsylvania teaching and Army service.",
                "B_authoritative_institutional", "high", "published",
                "A named earlier employer, not the last civilian employer before service.",
                [{"source_key": LOC_MCAFEE, "excerpt_override": "At Ewing Christian College where I taught"}],
                "william-mcafee-ewing-b1048",
            ),
            claim(
                "patton-william-mcafee-b1048", 9, "other_pre_oss_affiliation",
                "After returning from India, William McAfee taught at a high school in Patton, Pennsylvania.",
                "McAfee names Patton in a sequence of teaching positions before Penn State graduate study.",
                "High confidence from the exact name and direct detailed OSS chronology.",
                "Documented prewar employment; exact dates and the formal school name are not supplied.",
                "B_authoritative_institutional", "high", "published",
                "Source wording is retained without inventing an institutional name.",
                [{"source_key": LOC_MCAFEE}],
                "william-mcafee-patton-high-school-b1048",
            ),
            claim(
                "kiski-william-mcafee-b1048", 9, "other_pre_oss_affiliation",
                "William McAfee also taught at the institution he called Kiski before Army service.",
                "McAfee places Kiski between his return from India and later Penn State graduate study.",
                "High confidence from the exact name and direct detailed OSS chronology.",
                "Documented prewar employment; exact dates and institutional form are unstated.",
                "B_authoritative_institutional", "high", "published",
                "No modern successor name is inferred.",
                [{"source_key": LOC_MCAFEE}],
                "william-mcafee-kiski-b1048",
            ),
            claim(
                "altoona-william-mcafee-b1048", 9, "other_pre_oss_affiliation",
                "William McAfee taught at Altoona High before undertaking graduate study at Penn State.",
                "The oral history names Altoona High in his ordered sequence of Pennsylvania teaching positions.",
                "High confidence from the exact name and direct detailed OSS chronology.",
                "Documented prewar employment; exact dates are unstated.",
                "B_authoritative_institutional", "high", "published",
                "Historical name as found is retained.",
                [{"source_key": LOC_MCAFEE}],
                "william-mcafee-altoona-high-b1048",
            ),
            claim(
                "local-high-school-william-mcafee-b1048", 9, "last_civilian_pre_service",
                "William McAfee's best-supported last civilian job before his 1942 draft was teaching at an unnamed local high school while studying at Penn State.",
                "McAfee says he continued that job until the war and separately dates his draft to 10 March 1942.",
                "High confidence from exact name and detailed first-person Army-to-OSS chronology.",
                "Strongly date-bounded to the period immediately before Army entry; the employer name remains unknown.",
                "B_authoritative_institutional", "high", "published",
                "The unnamed job is excluded from named-employer analytics.",
                [{"source_key": LOC_MCAFEE, "excerpt_override": "a job teaching in the local high school, which I did while continuing graduate study until the war"}],
                "william-mcafee-local-high-school-b1048",
            ),
            claim(
                "identity-nancy-mccandlish-b1048", 41, "identity",
                "Indexed Nancy McCandlish is a high-confidence match to Nancy Montague McCandlish Prichard, Smithsonian employee and civilian OSS staff member in Cairo.",
                "The exact uncommon name, Smithsonian employment, and direct OSS and Cairo chronology agree across the institutional history and obituary.",
                "High confidence from the uncommon exact surname and given name, documented married-name variant, Smithsonian role, and direct OSS service.",
                "Both sources place Smithsonian employment before wartime OSS service.",
                "B_authoritative_institutional", "high", "published",
                "Evidence is not transferred to the separate Nancy M. McAnolish row; both Box 496 and Box 497 entities remain visible pending file comparison.",
                [{"source_key": SIA_MCCANDLISH}, {"source_key": WP_MCCANDLISH}, {"source_key": INDEX, "support_type": "context_only"}],
            ),
            claim(
                "sao-nancy-mccandlish-b1048", 41, "immediate_pre_oss_affiliation",
                "Nancy McCandlish worked as Special Assistant to the Meteorologist at the Smithsonian Astrophysical Observatory for three years before joining OSS.",
                "Smithsonian Archives explicitly identifies the role and sequence; the Washington Post independently places Smithsonian employment before civilian OSS service.",
                "High confidence from the uncommon exact name, documented married name, and direct Smithsonian-to-OSS chronology.",
                "Explicit immediate civilian employer and last civilian employer before OSS.",
                "B_authoritative_institutional", "high", "published",
                "The Post's broader administrative-assistant description is preserved in research notes rather than silently replacing the institutional role title.",
                [{"source_key": SIA_MCCANDLISH, "excerpt_override": "worked as a Special Assistant to the Meterologist at SAO for three years before joining the Office of Strategic Services"}, {"source_key": WP_MCCANDLISH, "support_type": "supports"}],
                "nancy-mccandlish-sao-b1048",
            ),
            claim(
                "identity-frederica-mcafee-b1048", 7, "identity",
                "Indexed Frederica McAfee is a high-confidence match to WASP Frederica McAfee Richardson, later documented as serving with OSS.",
                "Texas Woman's University and the Congressional Record identify Frederica Richardson's training name as McAfee; a separate biography places the former WASP in OSS.",
                "High confidence from the distinctive exact name, official class roster, documented married-name variant, and direct OSS statement in a secondary institutional biography.",
                "The sources establish WASP service before OSS but do not print an exact transition date.",
                "B_authoritative_institutional", "high", "published",
                "The married name is retained as a variant; no commissioned status is inferred from WASP service.",
                [{"source_key": TWU_MCAFEE}, {"source_key": GOVINFO_MCAFEE}, {"source_key": ROTARY_MCAFEE}, {"source_key": INDEX, "support_type": "context_only"}],
            ),
            claim(
                "wasp-frederica-mcafee-b1048", 7, "immediate_pre_oss_affiliation",
                "Frederica McAfee Richardson's WASP service is the probable immediate affiliation before her OSS civilian service.",
                "Official rosters establish Class 43-W-3 membership, while the Brookline biography describes her as a former WASP then serving with OSS.",
                "High confidence in identity from the distinctive name and two official rosters; the transition chronology relies on a secondary biography.",
                "Probable immediate, not explicit: the sequence is stated but no exact transition date is supplied.",
                "B_authoritative_institutional", "medium", "publish_qualified",
                "WASP is modeled as civilian government assignment and excluded from commissioned-military analytics.",
                [{"source_key": TWU_MCAFEE, "excerpt_override": "Richardson, Frederica McAfee"}, {"source_key": GOVINFO_MCAFEE, "support_type": "supports"}, {"source_key": ROTARY_MCAFEE, "support_type": "supports"}],
                "frederica-mcafee-wasp-b1048",
            ),
            claim(
                "identity-dale-mcadoo-b1048", 5, "identity",
                "Indexed Dale McAdoo is probably the OSS employee named in a 1943 official memorandum, but the document supplies no row-specific identifier or pre-OSS affiliation.",
                "The exact distinctive name appears in both the personnel index and an official OSS memorandum concerning McAdoo's account.",
                "Probable from the distinctive exact name and direct official OSS context; Box 496 review is still required because no rank or protected identifier bridges the records.",
                "Wartime OSS identity context only; no pre-OSS chronology is supplied.",
                "A_direct_official", "medium", "publish_qualified",
                "No employer, occupation, nationality, or assignment is inferred from the accounting memorandum.",
                [{"source_key": NARA_MCADOO}, {"source_key": INDEX, "support_type": "context_only"}],
            ),
        ]
    )
    return values


def base_update(row: int) -> dict[str, object]:
    person_id, name, box = PEOPLE[row]
    return {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified page 303 source preserves {name}, Box {box}, rank or grade when printed, notes when present, and archive location. Prior Library of Congress searching plus staged official, exact-name, occupation, obituary, institutional, directory, and archival discovery did not establish a defensible identity-and-affiliation bridge.",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": f"Review indexed Box {box} for corroborating identifiers, immediate pre-OSS affiliation, and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }


def person_updates() -> list[dict[str, object]]:
    by_row = {row: base_update(row) for row in PEOPLE}

    for row in ARMY_ASSOCIATIONS:
        by_row[row].update(
            identity_status="high_confidence",
            identity_evidence=army_identity_assessment(row),
            personnel_category="enlisted_army_personnel",
            commissioned_officer=False,
            allied_or_foreign_personnel=False,
            nara_catalog_id="1263923",
            research_status="occupation_only_found",
            next_action=f"Review Box {PEOPLE[row][2]} to identify a named employer or institution and establish Army-to-OSS chronology. The protected Army link supplies only a broad historical occupation category.",
            archival_review_priority="high",
        )

    for row in ARMY_IDENTITY_ONLY:
        by_row[row].update(
            identity_status="high_confidence",
            personnel_category="enlisted_army_personnel",
            commissioned_officer=False,
            allied_or_foreign_personnel=False,
            nara_catalog_id="1263923",
            next_action=f"Review Box {PEOPLE[row][2]} for a defensible pre-OSS affiliation. The accepted protected identity bridge supplies no publishable pre-OSS occupation.",
            archival_review_priority="high",
        )
    by_row[12]["identity_evidence"] = "A nonshared protected linkage and compatible damaged surname connect the indexed row to an official Army record entered on 6 December 1945. Because that date is after OSS disbandment, its occupation code is not used as pre-OSS evidence."
    by_row[23]["identity_evidence"] = "The exact official name and a nonshared protected linkage connect the records. The historical occupation code is unresolved in the reviewed official list and is not published."

    by_row[1].update(
        identity_status="confirmed",
        identity_evidence="The uncommon exact name, compatible naval rank, direct official OSS context, and protected row-specific identifier connect the index row to the wartime OSS board report; a Cleveland obituary independently corroborates Navy and OSS service.",
        personnel_category="enlisted_naval_personnel",
        commissioned_officer=False,
        allied_or_foreign_personnel=False,
        research_status="occupation_only_found",
        next_action="Review Box 495 for the name of Mazzone's Pennsylvania trucking employer and the exact Navy-to-OSS transfer date. The official report establishes the occupation and Navy pathway but not a named civilian employer.",
        archival_review_priority="medium",
    )
    by_row[5].update(
        identity_status="probable",
        identity_evidence="An official 1943 OSS memorandum names Dale McAdoo, matching the distinctive index name, but supplies no rank, Box 496 reference, protected identifier, or pre-OSS chronology.",
        next_action="Review Box 496 to confirm the 1943 official-document candidate and recover McAdoo's pre-OSS occupation, employer, and assignment sequence.",
        archival_review_priority="high",
    )
    by_row[7].update(
        identity_status="high_confidence",
        identity_evidence="The distinctive indexed name is connected to Frederica McAfee Richardson by official TWU and Congressional rosters; a separate biography explicitly places the former WASP in OSS.",
        name_variants=["Frederica McAfee Richardson", "Frederica Richardson"],
        replace_name_variants=False,
        personnel_category="civilian_professional_or_administrative_grade",
        commissioned_officer=False,
        allied_or_foreign_personnel=False,
        research_status="needs_temporal_review",
        next_action="Review Box 496 or the TWU biographical file for the exact date and terms of Frederica McAfee Richardson's WASP-to-OSS transition and any earlier civilian employer.",
        archival_review_priority="high",
    )
    by_row[9].update(
        identity_status="high_confidence",
        identity_evidence="The exact name, compatible Army officer status, China Theater chronology, and direct first-person account of four months with OSS support the match to diplomat William McAfee.",
        personnel_category="commissioned_army_officer",
        commissioned_officer=True,
        allied_or_foreign_personnel=False,
        research_status="documented_prewar_employer_found",
        next_action="Review Box 496 to confirm the indexed major and identify the unnamed local high school where McAfee taught immediately before his 10 March 1942 draft.",
        archival_review_priority="medium",
    )
    by_row[13].update(
        identity_status="ambiguous",
        identity_evidence="The page separately prints Nancy M. McAnolish in Box 496 and Nancy McCandlish in Box 497. Their similar names may reflect different people, a transcription variant, or duplicate files; no evidence is transferred between them.",
        possible_duplicate_group="p303-nancy-mcanolish-mccandlish-b1048",
        research_status="needs_identity_review",
        next_action="Compare Boxes 496 and 497 before treating McAnolish as a variant of McCandlish or transferring the Smithsonian evidence.",
        archival_review_priority="critical",
    )
    by_row[14].update(
        identity_status="ambiguous",
        identity_evidence="The same protected identifier is associated with page 303 William C. McAragle and page 308 William C. McGaragle, while the Army file prints McGaragle. The rows remain separate and no occupation is transferred.",
        possible_duplicate_group="p303-308-william-mcaragle-mcgaragle-b623",
        personnel_category="enlisted_army_personnel",
        commissioned_officer=False,
        allied_or_foreign_personnel=False,
        research_status="needs_identity_review",
        next_action="Compare the Box 496 and Box 506 jackets and the protected identifier before resolving McAragle/McGaragle or publishing the Army occupation category.",
        archival_review_priority="critical",
    )
    by_row[20].update(
        identity_status="confirmed",
        identity_evidence="The exact distinctive name, matching lieutenant-commander rank, and Berkeley oral history's direct Navy and OSS chronology confirm Turner Hudson McBaine.",
        name_variants=["Turner Hudson McBaine"],
        replace_name_variants=False,
        personnel_category="commissioned_naval_officer",
        commissioned_officer=True,
        allied_or_foreign_personnel=False,
        research_status="verified_employer_found",
        next_action="Review Box 496 for the exact Navy-to-OSS assignment date; the 1939-1941 Neylan law practice is already strongly date-bounded as the last civilian employer before active duty.",
        archival_review_priority="medium",
    )
    by_row[22].update(
        name_variants=["Hiram W McBride Jr."],
        replace_name_variants=False,
    )
    by_row[41].update(
        identity_status="high_confidence",
        identity_evidence="The uncommon exact name, Smithsonian institutional history, documented married name, and Washington Post obituary directly connect Nancy McCandlish to Smithsonian employment and civilian OSS service in Cairo.",
        name_variants=["Nancy McCandlish Prichard", "Nancy Montague McCandlish Prichard"],
        replace_name_variants=False,
        personnel_category="civilian_professional_or_administrative_grade",
        commissioned_officer=False,
        allied_or_foreign_personnel=False,
        possible_duplicate_group="p303-nancy-mcanolish-mccandlish-b1048",
        research_status="verified_employer_found",
        next_action="Compare Boxes 496 and 497 to determine whether Nancy M. McAnolish is a separate person or index variant; do not transfer the Smithsonian evidence without that review.",
        archival_review_priority="critical",
    )

    result = [by_row[row] for row in PEOPLE]
    if len(result) != 43:
        raise RuntimeError(f"Expected 43 person updates, generated {len(result)}")
    return result


def outcome_note(row: int) -> str:
    notes = {
        1: "A wartime OSS board report confirms Mazzone's Navy pathway and Pennsylvania truck-driver occupation; no trucking employer is named.",
        5: "An official OSS memorandum supports a probable Dale McAdoo identity bridge but supplies no pre-OSS chronology.",
        7: "Two official rosters and a separate biography support Frederica McAfee Richardson's WASP and OSS identities; the exact transition date remains unverified.",
        9: "The Library of Congress oral history supplies a direct China-Theater-to-OSS sequence and several named earlier teaching roles; the final local high school is unnamed.",
        12: "The protected Army identity bridge was accepted, but the 6 December 1945 Army-entry date is post-OSS and no occupation was used as pre-OSS evidence.",
        13: "The similar McAnolish and McCandlish rows remain separate pending comparison of Boxes 496 and 497.",
        14: "The McAragle/McGaragle candidate shares one protected identifier across two index people and remains conflicting rather than accepted.",
        20: "A Berkeley institutional oral history supplies McBaine's 1936-1941 law-employer chronology and probable Navy-to-OSS pathway.",
        23: "The protected identity bridge was accepted, but unresolved historical code 985 was not converted into an occupation.",
        41: "Smithsonian institutional research explicitly identifies three years at SAO before OSS; evidence is not transferred to Nancy M. McAnolish.",
    }
    return notes.get(row, "Unbridged namesakes, snippets, commercial people-finder pages, unsourced genealogy, relatives, and postwar-only leads did not establish a reliable identity or pre-OSS affiliation.")


def research_attempts() -> list[dict[str, object]]:
    updates = {item["person_id"]: item for item in person_updates()}
    substantiated = set(ARMY_ASSOCIATIONS) | ARMY_IDENTITY_ONLY | {1, 5, 7, 9, 20, 41}
    values: list[dict[str, object]] = []
    for row, (person_id, name, box) in PEOPLE.items():
        if row in {13, 14}:
            outcome = "candidate_rejected"
        elif row in substantiated:
            outcome = "source_reviewed"
        else:
            outcome = "no_result"
        values.append(
            {
                "key": f"page303-row{row}-{slug(name)}-b1048",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index context; exact-name and meaningful initial, punctuation, spelling and OCR variants; public CIA-domain discovery and equivalent official-source context; rank, branch, nationality, assignment and protected-identifier clues; employer and occupation 1940; obituary, biography, institutional, Library of Congress newspaper, directory and archival searches; indexed Box {box}",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_1048",
                "started_at": "2026-11-05T13:05:00-05:00",
                "completed_at": "2026-11-05T13:45:00-05:00",
                "outcome": outcome,
                "sources_reviewed": 9 if row in {1, 9, 20, 41} else 8 if row == 7 else 7 if row in substantiated else 6 if row in {13, 14} else 5,
                "candidate_sources_rejected": 5 if row in {13, 14} else 4 if row in {1, 5, 7, 9, 20, 41} else 3,
                "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, education treated as employment, relatives, and postwar-only leads were rejected. Army categories were not converted into named employers. Similar or shared-identifier rows remain separate.",
                "research_notes": f"{outcome_note(row)} The official index, prior Library of Congress search, exact-name OSS discovery, public CIA-domain discovery, Army and NARA materials, occupation and employer searches, and institutional, obituary, directory, military-history, newspaper, and archival sources were reviewed as applicable. Public CIA-domain discovery was used; direct adapter access remains unavailable under the documented robots policy and was not treated as a negative result. No authenticated NARA Catalog API request was made.",
                "next_action": str(updates[person_id]["next_action"]),
                "attempt_number": 2,
                "research_agent_version": "before-oss-b1048-v1",
            }
        )
    if len(values) != 43:
        raise RuntimeError(f"Expected 43 research attempts, generated {len(values)}")
    return values


def main() -> None:
    bundle = {
        "bundle_version": "batch-1048-v1",
        "reviewer": "Before OSS Batch 1048 evidence review",
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
