#!/usr/bin/env python3
"""Generate the reviewed Batch 1054 evidence bundle for PDF page 309."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page309-barry-mcgill-to-ernest-f-mcguire-review_"
    "batch-1054_2026-11-11.json"
)

INDEX = "nara-index-b1054"
ARMY = "army-bulk-b1054"
TECH = "army-tech-b1054"
CODES = "army-codes-b1054"
COURTS = "ny-courts-owen-mcgivern-b1054"
NORTHWESTERN = "northwestern-william-mcgovern-b1054"
CRIMSON = "harvard-crimson-donald-mcgranahan-b1054"
HARVARD = "harvard-psychology-donald-mcgranahan-b1054"
STREET = "street-radio-luxembourg-mcgranahan-b1054"


# Every printed row is a distinct person entity on this page. Exact-name pairs
# at rows 8/9 and 26/27 remain separate because their boxes or identifiers differ.
PEOPLE = {
    1: ("a574c48c-ad3b-57a1-ae43-c985d9c94364", "Barry McGill", "505"),
    2: ("05f65963-c3d4-55cc-9de3-b6ce4d6904b8", "John H McGill", "505"),
    3: ("4f730acf-788d-5f0f-b340-fae1209bf8ca", "William L McGill", "505"),
    4: ("d6d56580-d0ae-5cc5-91bb-9e52e746ba4f", "William H McGill", "505"),
    5: ("19933c86-d3c0-5d70-a61a-a2decbaa88f1", "Morgan McGilvray", "505"),
    6: ("8a2055db-b8a6-519b-abd4-95a5fb0a767c", "Margaret McGinley", "505"),
    7: ("3ecc51f1-f0bc-5847-9ab7-1d77b4fc5d29", "Vincent P McGinn", "505"),
    8: ("19527627-c8ef-5beb-9c82-4eb2b082fed0", "David K McGinnis", "505"),
    9: ("4d925235-45a5-5159-a7a5-a62ecfa8f571", "David K McGinnis", "506"),
    10: ("46b3e995-3c27-5791-a165-d171b3cce7d7", "Donald F McGinnis", "506"),
    11: ("f2ba7ece-afb3-59e6-8667-ba0d1d64a3cd", "Edward F McGinnis", "506"),
    12: ("00711a15-d463-54d9-b64e-1774dcbb8b40", "Edward M McGinnis", "506"),
    13: ("f466bb16-1781-5ad5-b65f-d35f17033d3c", "Leon A McGinnis", "506"),
    14: ("8c545524-a2bf-51a0-a47b-6fa703c1d0a0", "Owen McGivern", "506"),
    15: ("e8d03935-3728-53a5-81fe-223e327de47f", "Grady C McGlassen", "506"),
    16: ("5e66c7f7-38aa-567d-99cd-9c9c826932b8", "Edward J McGlynn", "506"),
    17: ("1ded0ad9-a341-5cf8-9517-3027537e7578", "Irene M McGlynn", "506"),
    18: ("5124d908-2dcc-51e3-8357-fc1f746e7945", "James G McGoldrick", "506"),
    19: ("46f824d1-5a14-57ae-88d3-edcc9bb87e04", "Harlan McGonigal", "506"),
    20: ("968ba99c-f60f-51d5-a7a0-f7e4dba3c44d", "John J McGourty", "506"),
    21: ("4154128c-4ca7-5725-bdcc-7c84cc0b4ace", "Terrence J McGovern", "506"),
    22: ("770cf847-09bb-50f8-a57c-0e03d10e8a68", "William C McGovern", "506"),
    23: ("80e851c4-c1ae-5bd5-b591-9ec4c92a351a", "William M McGovern", "506"),
    24: ("7e6b3058-a30c-5328-bec0-1deb39bcae80", "Arthur P McGowan", "506"),
    25: ("32ab45a5-822e-5015-973c-f81f40d74361", "James J McGowan", "506"),
    26: ("8cb882e2-137b-5126-96c5-c3415e716d7f", "John E McGowan", "506"),
    27: ("5b3f8268-a841-5291-8096-84d6bdc48b8d", "John E McGowan", "506"),
    28: ("f5e7c846-718d-5e75-8160-1750a31f9742", "Justin J McGowan", "506"),
    29: ("5d2de7a8-da80-571f-983d-2fa44ca7935e", "Terrence P McGowan", "506"),
    30: ("7beb9f96-3fa1-509a-9ac4-c62cfd9e9eec", "William H McGowan", "506"),
    31: ("d9809e99-bfb1-5734-adb6-649244d89738", "John McGrail", "506"),
    32: ("e0c472fb-5a66-50c4-8436-bce3dd919130", "Frank McGrann", "506"),
    33: ("bbe4a616-0be8-5952-a230-1be0c8365dfa", "Donald V McGrannahan", "506"),
    34: ("aff7f748-6f2f-5903-9959-115b25b02d53", "Charles E McGrath", "506"),
    35: ("6e93d495-cfc8-5141-bf74-3e353987b326", "John E McGrath", "506"),
    36: ("d50fd0c5-3253-51e6-bba3-9fb30512e2a8", "Thomas H McGrath", "506"),
    37: ("3bb3ab9d-4e83-5cd7-840a-8681229a6f70", "William McGrath", "506"),
    38: ("de3debe5-89c6-5e05-a483-75e466eeb259", "Doris J McGraw", "506"),
    39: ("27f39146-e428-51f5-aa6a-9c35af400941", "James F McGraw", "506"),
    40: ("0ec32606-6b8d-5dc3-b88c-7a3467df01ee", "Robert V McGraw", "506"),
    41: ("045ac283-2b08-5872-bb8d-fb1f6eea91a3", "William A McGregor", "506"),
    42: ("3e1cb4fd-405f-53ca-972a-c1d2b13f70a9", "John J McGrew", "507"),
    43: ("24a8dd4c-bb08-528b-9dc5-4c9f0d86118d", "Stanley F McGrnahan", "507"),
    44: ("22234c9b-9eae-54af-8246-4bcc0e16b0f9", "David M McGuigan", "507"),
    45: ("83cd6e0c-36d4-571f-9a99-fa7c96c24cb3", "Edward J McGuire", "507"),
    46: ("011e990f-67a9-531a-9659-42ea37883393", "Ernest F McGuire", "507"),
}


# These are nonshared official Army links with wartime entry dates and defined
# occupation codes. They identify broad occupations, never named employers.
ARMY_OCCUPATIONS = {
    1: ("1943-03-19", "992", "student", "Students", "student", "PDF physical page 304; corrected historical code 9-92"),
    3: ("1943-06-03", "480", "sheet metal worker, coppersmith, or tinsmith", "Sheet metal workers, coppersmiths, and tinsmiths", "unknown", "PDF physical page 174; historical code 4-80"),
    4: ("1942-09-03", "992", "student", "Students", "student", "PDF physical page 304; corrected historical code 9-92"),
    12: ("1943-03-09", "316", "general-farm hand", "Farm hands, general farms", "unknown", "PDF physical page 172; historical code 3-16"),
    16: ("1943-03-10", "992", "student", "Students", "student", "PDF physical page 304; corrected historical code 9-92"),
    19: ("1944-01-18", "992", "student", "Students", "student", "PDF physical page 304; corrected historical code 9-92"),
    20: ("1943-06-02", "992", "student", "Students", "student", "PDF physical page 304; corrected historical code 9-92"),
    22: ("1942-11-05", "627", "textile-product fabrication worker, not elsewhere classified", "Occupations in fabrication of textile products, n.e.c.", "unknown", "PDF physical page 173; historical code 6-27"),
    24: ("1943-02-12", "101", "bookkeeper or cashier, except bank cashier", "Bookkeepers and cashiers, except bank cashiers", "unknown", "PDF physical page 171; historical code 1-01"),
    34: ("1942-11-30", "263", "fire-department fireman", "Firemen, fire department", "unknown", "PDF physical page 172; historical code 2-63"),
    45: ("1943-02-13", "641", "paper- or pulp-manufacturing worker", "Occupations in manufacture of paper and pulp", "unknown", "PDF physical page 173; historical code 6-41"),
}

ARMY_IDENTITY_ONLY = {30, 37}
CONFLICT_ROWS = {13}
AMBIGUOUS_ROWS = {8, 9, 26, 27}

ATTEMPT_NUMBERS = {
    1: 3, 2: 2, 3: 3, 4: 3, 5: 2, 6: 2, 7: 2, 8: 2, 9: 3,
    10: 2, 11: 3, 12: 3, 13: 3, 14: 2, 15: 2, 16: 3, 17: 2,
    18: 2, 19: 3, 20: 3, 21: 2, 22: 3, 23: 3, 24: 3, 25: 3,
    26: 3, 27: 3, 28: 2, 29: 2, 30: 3, 31: 3, 32: 2, 33: 2,
    34: 3, 35: 3, 36: 2, 37: 3, 38: 2, 39: 3, 40: 2, 41: 2,
    42: 3, 43: 2, 44: 2, 45: 3, 46: 2,
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
            archival_identifier="RG 226, Entry A1-224, Boxes 505-507",
            title="OSS Personnel Files from Excel",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="2010-12-23",
            locator="PDF page 309, rows 1-46; every printed row visually checked against the official PDF",
            source_quality="A_direct_official",
            collection_name="Records of the Office of Strategic Services, Record Group 226",
            rights_notes="All 46 printed rows remain separate. Full protected identifiers remain private.",
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
            rights_notes="No raw record, protected identifier, or bulk ordinal is retained in public assets. Conflicting, undefined, and post-OSS links are withheld from occupation claims.",
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
            locator="PDF physical pages 171-175 and 304; all eleven published Batch 1054 categories visually checked",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records technical documentation",
            rights_notes="Categories identify neither employer nor exact Army-to-OSS sequence. Code 590 is absent and remains uninterpreted.",
        ),
        source(
            COURTS,
            stable_url="https://history.nycourts.gov/biography/owen-mcgivern/",
            archival_identifier="Historical Society of the New York Courts biography: Owen McGivern",
            title="Owen McGivern",
            author_creator="Historical Society of the New York Courts",
            repository_publisher="Historical Society of the New York Courts",
            publication_record_date="current institutional biography; accessed 2026-11-11",
            locator="Biographical paragraphs covering education, legal practice, Assembly service, Navy service, and OSS Naval Liaison duty",
            source_quality="B_authoritative_institutional",
            collection_name="New York Legal History biographies",
            rights_notes="Only project-authored paraphrases and the shortest necessary excerpt are retained.",
        ),
        source(
            NORTHWESTERN,
            stable_url="https://findingaids.library.northwestern.edu/agents/people/1731",
            archival_identifier="William Montgomery McGovern (1897-1964); related papers 11/3/22/3",
            title="McGovern, William Montgomery, 1897-1964",
            author_creator="Northwestern University Archives",
            repository_publisher="Northwestern University Archives",
            publication_record_date="current archival authority record; accessed 2026-11-11",
            locator="Biography: faculty appointment, Chicago Times, Harvard, and United States Naval Reserve chronology",
            source_quality="B_authoritative_institutional",
            collection_name="Archival and Manuscript Collections",
            rights_notes="The authority record supplies a precise institutional chronology but does not itself state OSS service.",
        ),
        source(
            CRIMSON,
            stable_url="https://www.thecrimson.com/article/1932/4/1/whitaker-scholarship-is-awarded-to-mcgranahan/",
            archival_identifier="Harvard Crimson, 1932-04-01",
            title="Whitaker Scholarship Is Awarded to McGranahan",
            author_creator="No writer attributed",
            repository_publisher="The Harvard Crimson",
            publication_record_date="1932-04-01",
            locator="Opening two paragraphs",
            source_quality="C_reputable_contemporary_or_scholarly",
            collection_name="The Harvard Crimson archive",
            rights_notes="The article documents Donald Vincent McGranahan as a Harvard student; it does not establish an OSS identity by itself.",
        ),
        source(
            HARVARD,
            stable_url="https://psychology.fas.harvard.edu/doctoral-alumni",
            archival_identifier="Harvard Department of Psychology doctoral alumni, 1940",
            title="Doctoral Alumni",
            author_creator="Harvard University Department of Psychology",
            repository_publisher="Harvard University",
            publication_record_date="current institutional page; 1940 alumni entry",
            locator="20th Century list, 1940: Donald McGranahan",
            source_quality="B_authoritative_institutional",
            collection_name="Harvard Psychology doctoral alumni",
            rights_notes="The institutional list documents the doctorate year but does not establish an OSS identity by itself.",
        ),
        source(
            STREET,
            stable_url="https://eprints.bournemouth.ac.uk/393/1/Street%2C_Sean_Ph.D._2003.pdf",
            archival_identifier="Bournemouth University PhD thesis, Sean Street, 2003",
            title="The Development of British Radio Broadcasting to Germany during the Second World War",
            author_creator="Sean Street",
            repository_publisher="Bournemouth University",
            publication_record_date="2003",
            locator="PDF page 381; Capt. Donald V. McGranahan, Intelligence Section, PWD, SHAEF, 30 October 1944",
            source_quality="C_reputable_contemporary_or_scholarly",
            collection_name="Bournemouth University Research Online",
            rights_notes="Used as a scholarly wartime identity bridge. It documents SHAEF psychological-warfare service, not an OSS assignment or prewar employer.",
        ),
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": "united-states-navy-b1054",
            "organization_id": "3960fa8e-a551-56cf-8305-b2b9e4961b9d",
            "canonical_name": "United States Navy",
            "historical_name": "United States Navy",
            "aliases": ["U.S. Navy", "Navy"],
            "organization_type": "military service",
            "sector": "military",
            "country": "United States",
            "active_dates": "1794-present",
            "normalization_notes": "Existing canonical organization reused; the source wording Navy is preserved on the affiliation.",
        },
        {
            "key": "new-york-state-assembly-b1054",
            "canonical_name": "New York State Assembly",
            "historical_name": "New York State Assembly",
            "aliases": ["New York State Assemblyman"],
            "organization_type": "state legislature",
            "sector": "state_or_local_government",
            "city": "Albany",
            "state_or_region": "New York",
            "country": "United States",
            "normalization_notes": "Legislative service is a government assignment, not converted into private employment.",
        },
        {
            "key": "donovan-leisure-newton-lumbard-b1054",
            "organization_id": "41d7a107-a9e1-5b19-92ac-ddef680f8c45",
            "canonical_name": "Donovan, Leisure, Newton & Lumbard",
            "historical_name": "Donovan, Leisure, Newton & Lumbard",
            "aliases": ["Donovan, Leisure, Newton and Lumbard"],
            "organization_type": "law firm",
            "sector": "law",
            "city": "New York City",
            "state_or_region": "New York",
            "country": "United States",
            "normalization_notes": "Historical firm name retained exactly; no postwar successor is substituted.",
        },
        {
            "key": "james-dooling-law-office-b1054",
            "canonical_name": "James J. Dooling law office",
            "historical_name": "James J. Dooling's law office",
            "aliases": ["Law office of James J. Dooling"],
            "organization_type": "law office",
            "sector": "law",
            "city": "New York City",
            "state_or_region": "New York",
            "country": "United States",
            "normalization_notes": "Normalized only to the named office described by the source; no modern successor is asserted.",
        },
        {
            "key": "harvard-university-b1054",
            "organization_id": "45ddf347-21c6-59f5-a8ae-517418adf941",
            "canonical_name": "Harvard University",
            "historical_name": "Harvard University",
            "aliases": [],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "Cambridge",
            "state_or_region": "Massachusetts",
            "country": "United States",
            "normalization_notes": "Existing canonical organization reused; student and employment relationships remain separate.",
        },
        {
            "key": "northwestern-university-b1054",
            "organization_id": "010d3e98-f501-58c2-a2ad-ba0dc45aaf81",
            "canonical_name": "Northwestern University",
            "historical_name": "Northwestern University",
            "aliases": [],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "Evanston",
            "state_or_region": "Illinois",
            "country": "United States",
            "normalization_notes": "Existing canonical organization reused.",
        },
        {
            "key": "chicago-daily-times-b1054",
            "organization_id": "65769ebf-479d-5caa-96a9-65826d4aec6a",
            "canonical_name": "Chicago Daily Times",
            "historical_name": "Chicago Times",
            "aliases": ["Chicago Daily Times"],
            "organization_type": "newspaper",
            "sector": "journalism_and_media",
            "city": "Chicago",
            "state_or_region": "Illinois",
            "country": "United States",
            "normalization_notes": "The Northwestern authority record's Chicago Times wording is preserved on the affiliation.",
        },
    ]


def army_affiliation_key(row: int) -> str:
    return f"{slug(PEOPLE[row][1])}-army-entry-occupation-b1054"


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
                "key": "owen-mcgivern-united-states-navy-b1054",
                "person_id": PEOPLE[14][0],
                "organization_key": "united-states-navy-b1054",
                "organization_name_as_found": "Navy",
                "role_title": "naval officer; subsequently OSS Naval Liaison Officer",
                "occupation": "naval officer",
                "relationship_type": "military_assignment",
                "date_precision": "The institutional biography says McGivern joined the Navy during World War II and subsequently served as the OSS Naval Liaison Officer; exact dates are not stated.",
                "country": "United States",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "explicit_immediate",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "The source explicitly supplies the Navy-to-OSS sequence. Navy service is modeled as a military assignment, not a civilian employer.",
            },
            {
                "key": "owen-mcgivern-new-york-state-assembly-b1054",
                "person_id": PEOPLE[14][0],
                "organization_key": "new-york-state-assembly-b1054",
                "organization_name_as_found": "New York State Assembly",
                "role_title": "Assemblyman",
                "occupation": "state legislator",
                "relationship_type": "government_assignment",
                "start_date": "1939",
                "end_date": "1950",
                "date_precision": "The source gives a 1939 election and service through 1950 and says he entered the Navy while deferred as an Assemblyman.",
                "city": "Albany",
                "state_or_region": "New York",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "explicit_immediate",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "This is the last documented civilian government role before Navy service. It continued through wartime and is not mislabeled as private employment.",
            },
            {
                "key": "owen-mcgivern-donovan-leisure-newton-lumbard-b1054",
                "person_id": PEOPLE[14][0],
                "organization_key": "donovan-leisure-newton-lumbard-b1054",
                "organization_name_as_found": "Donovan, Leisure, Newton & Lumbard",
                "role_title": "lawyer",
                "occupation": "attorney",
                "relationship_type": "employment",
                "start_date": "1937",
                "end_date": "1939",
                "date_precision": "The source says he joined the firm in 1937 and was elected to the Assembly two years later; an exact departure date is not stated.",
                "city": "New York City",
                "state_or_region": "New York",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Earlier documented private employment; the later Assembly and Navy roles prevent treating it as immediate pre-OSS or last civilian before service.",
            },
            {
                "key": "owen-mcgivern-james-dooling-law-office-b1054",
                "person_id": PEOPLE[14][0],
                "organization_key": "james-dooling-law-office-b1054",
                "organization_name_as_found": "James J. Dooling's law office",
                "role_title": "associate",
                "occupation": "attorney",
                "relationship_type": "employment",
                "end_date": "1937",
                "date_precision": "The source places this association after 1934 admission to the bar and before McGivern joined Donovan, Leisure, Newton & Lumbard in 1937.",
                "city": "New York City",
                "state_or_region": "New York",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Earlier documented legal employment; no exact start date is asserted.",
            },
            {
                "key": "william-m-mcgovern-harvard-university-b1054",
                "person_id": PEOPLE[23][0],
                "organization_key": "harvard-university-b1054",
                "organization_name_as_found": "Harvard University",
                "role_title": "visiting lecturer in government",
                "occupation": "university lecturer",
                "relationship_type": "employment",
                "start_date": "1940",
                "end_date": "1941",
                "date_precision": "Northwestern's authority record gives the visiting appointment as 1940-41 and places Naval Reserve service from 1941 through 1945.",
                "city": "Cambridge",
                "state_or_region": "Massachusetts",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Best-supported last civilian employer before Naval Reserve service. The source does not establish the exact later Navy-to-OSS sequence.",
            },
            {
                "key": "william-m-mcgovern-northwestern-university-b1054",
                "person_id": PEOPLE[23][0],
                "organization_key": "northwestern-university-b1054",
                "organization_name_as_found": "Northwestern University",
                "role_title": "associate professor and later professor of political science",
                "occupation": "political science professor",
                "relationship_type": "employment",
                "start_date": "1929",
                "date_precision": "The source says McGovern joined in 1929, became a full professor in 1936, and retained the appointment through documented interruptions.",
                "city": "Evanston",
                "state_or_region": "Illinois",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Earlier and continuing academic employment; the intervening 1940-41 Harvard appointment is separately modeled as last civilian before service.",
            },
            {
                "key": "william-m-mcgovern-chicago-times-b1054",
                "person_id": PEOPLE[23][0],
                "organization_key": "chicago-daily-times-b1054",
                "organization_name_as_found": "Chicago Times",
                "role_title": "Far East correspondent",
                "occupation": "foreign correspondent",
                "relationship_type": "employment",
                "start_date": "1937",
                "end_date": "1938",
                "date_precision": "Northwestern's authority record explicitly dates the correspondent role to 1937-38.",
                "city": "Chicago",
                "state_or_region": "Illinois",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Earlier documented employment, not the last civilian role before wartime service.",
            },
            {
                "key": "donald-v-mcgranahan-harvard-university-b1054",
                "person_id": PEOPLE[33][0],
                "organization_key": "harvard-university-b1054",
                "organization_name_as_found": "Harvard University",
                "role_title": "undergraduate and psychology doctoral student",
                "occupation": "student",
                "relationship_type": "student",
                "start_date": "1931",
                "end_date": "1940",
                "date_precision": "A 1932 contemporary article identifies class year 1935; Harvard's official doctoral list places Donald McGranahan in 1940.",
                "city": "Cambridge",
                "state_or_region": "Massachusetts",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "probable",
                "claim_confidence": "medium",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "publish_qualified",
                "research_notes": "Qualified student affiliation, never an employer claim. The index spelling McGrannahan and the source spelling McGranahan remain visible pending personnel-file confirmation.",
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
                f"army-entry-{slug(PEOPLE[row][1])}-b1054",
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

    owen_identity = (
        "The unusual exact name, the index's Navy lieutenant context, and the institutional biography's explicit Navy and OSS Naval Liaison service support a high-confidence identity match."
    )
    values.extend(
        [
            claim(
                "identity-owen-mcgivern-b1054",
                14,
                "identity",
                "The indexed Owen McGivern is a high-confidence match to the New York lawyer, Assemblyman, Navy officer, and OSS Naval Liaison Officer.",
                "The court-history biography supplies the rare exact name and an explicit Navy-to-OSS liaison sequence consistent with the indexed lieutenant row.",
                owen_identity,
                "The source describes the wartime sequence but gives no exact Navy or OSS start date.",
                "B_authoritative_institutional",
                "high",
                "published",
                "No famous-name transfer is made from name alone; the source independently supplies both Navy and OSS roles.",
                [{"source_key": INDEX, "support_type": "context_only"}, {"source_key": COURTS}],
            ),
            claim(
                "owen-mcgivern-united-states-navy-b1054",
                14,
                "immediate_pre_oss_affiliation",
                "Owen McGivern's immediate documented pathway into OSS was through the United States Navy, where he subsequently served as the OSS Naval Liaison Officer.",
                "The institutional biography explicitly says he joined the Navy during World War II and subsequently served as the OSS Naval Liaison Officer.",
                owen_identity,
                "Explicit immediate sequence; exact dates remain unstated.",
                "B_authoritative_institutional",
                "high",
                "published",
                "Navy service is a military assignment, not a civilian employer.",
                [{"source_key": COURTS}, {"source_key": INDEX, "support_type": "context_only"}],
                "owen-mcgivern-united-states-navy-b1054",
                "McGivern joined the Navy during World War II to subsequently serve as Office of Strategic Services' Naval Liaison Officer.",
            ),
            claim(
                "owen-mcgivern-new-york-state-assembly-b1054",
                14,
                "last_civilian_pre_service",
                "Owen McGivern was serving in the New York State Assembly when he entered the Navy, making the Assembly his last documented civilian government affiliation before service.",
                "The biography dates his Assembly service to 1939-50 and says he joined the Navy despite being militarily deferred as an Assemblyman.",
                owen_identity,
                "The source directly connects Assembly status with entry into Navy service, while showing that legislative service continued.",
                "B_authoritative_institutional",
                "high",
                "published",
                "The relationship is government assignment, not private employment.",
                [{"source_key": COURTS}],
                "owen-mcgivern-new-york-state-assembly-b1054",
            ),
            claim(
                "owen-mcgivern-donovan-leisure-newton-lumbard-b1054",
                14,
                "other_pre_oss_affiliation",
                "Owen McGivern joined Donovan, Leisure, Newton & Lumbard in 1937, before his 1939 election to the New York State Assembly.",
                "The institutional biography gives the firm name and 1937 start, followed by the Assembly election two years later.",
                owen_identity,
                "Definitely prewar and before Assembly and Navy service; not immediate pre-OSS.",
                "B_authoritative_institutional",
                "high",
                "published",
                "Earlier legal employment is not conflated with the later civilian government and military pathway.",
                [{"source_key": COURTS}],
                "owen-mcgivern-donovan-leisure-newton-lumbard-b1054",
            ),
            claim(
                "owen-mcgivern-james-dooling-law-office-b1054",
                14,
                "other_pre_oss_affiliation",
                "Before joining Donovan, Leisure, Newton & Lumbard, Owen McGivern was an associate in James J. Dooling's law office.",
                "The biography names Dooling's law office and then dates McGivern's move to Donovan, Leisure, Newton & Lumbard in 1937.",
                owen_identity,
                "Definitely prewar and earlier than the 1937 law-firm role; exact start date unknown.",
                "B_authoritative_institutional",
                "high",
                "published",
                "The historical office name is preserved without inferring a modern successor.",
                [{"source_key": COURTS}],
                "owen-mcgivern-james-dooling-law-office-b1054",
            ),
            claim(
                "identity-william-m-mcgovern-b1054",
                23,
                "identity",
                "The indexed Commander William M. McGovern is a high-confidence match to William Montgomery McGovern, Northwestern professor and 1941-45 Naval Reserve officer.",
                "The uncommon full name and middle initial, the indexed commander rank, and Northwestern's exact wartime Naval Reserve chronology form a coherent match.",
                "High confidence from the uncommon exact name with middle initial and independently documented 1941-45 United States Naval Reserve service consistent with the indexed commander rank.",
                "The source establishes wartime Navy service but does not state an OSS assignment or entry date.",
                "B_authoritative_institutional",
                "high",
                "published",
                "The Navy chronology supports identity; the precise Navy-to-OSS sequence remains for personnel-file review.",
                [{"source_key": INDEX, "support_type": "context_only"}, {"source_key": NORTHWESTERN}],
            ),
            claim(
                "william-m-mcgovern-harvard-university-b1054",
                23,
                "last_civilian_pre_service",
                "William Montgomery McGovern's last documented civilian employer before Naval Reserve service was Harvard University, where he was a visiting lecturer in government in 1940-41.",
                "Northwestern's authority record places the 1940-41 Harvard appointment immediately before Naval Reserve service beginning in 1941.",
                "High confidence from the uncommon name, middle initial, indexed commander rank, and matching Naval Reserve chronology.",
                "Strongly date-bounded before military service; the exact OSS sequence is not established.",
                "B_authoritative_institutional",
                "high",
                "published",
                "Harvard employment is kept separate from Northwestern's continuing appointment and from later military service.",
                [{"source_key": NORTHWESTERN}, {"source_key": INDEX, "support_type": "context_only"}],
                "william-m-mcgovern-harvard-university-b1054",
            ),
            claim(
                "william-m-mcgovern-northwestern-university-b1054",
                23,
                "other_pre_oss_affiliation",
                "William Montgomery McGovern joined Northwestern University's political science faculty in 1929 and became a full professor in 1936.",
                "Northwestern's archival authority record documents the faculty appointment, promotion, and later interruptions.",
                "High confidence from the distinctive identity and matching Naval Reserve chronology.",
                "Documented prewar employment, but the 1940-41 Harvard appointment intervened before service.",
                "B_authoritative_institutional",
                "high",
                "published",
                "The continuing appointment is not mislabeled as the last civilian employer before service.",
                [{"source_key": NORTHWESTERN}],
                "william-m-mcgovern-northwestern-university-b1054",
            ),
            claim(
                "william-m-mcgovern-chicago-times-b1054",
                23,
                "other_pre_oss_affiliation",
                "William Montgomery McGovern worked as Far East correspondent for the Chicago Times in 1937-38.",
                "Northwestern's authority record explicitly names the newspaper, role, and dates.",
                "High confidence from the distinctive identity and matching Naval Reserve chronology.",
                "Documented prewar employment; later Harvard employment intervened before military service.",
                "B_authoritative_institutional",
                "high",
                "published",
                "The source wording Chicago Times is preserved even though the organization is normalized separately.",
                [{"source_key": NORTHWESTERN}],
                "william-m-mcgovern-chicago-times-b1054",
            ),
            claim(
                "identity-donald-v-mcgranahan-b1054",
                33,
                "identity",
                "The indexed Donald V. McGrannahan is a probable, not confirmed, match to Donald Vincent McGranahan, the Harvard-trained psychologist who served in SHAEF psychological warfare.",
                "The rare name and middle initial align after a one-letter spelling difference, while a scholarly source places Donald V. McGranahan in wartime PWD, SHAEF intelligence work.",
                "Probable from a rare near-exact name, matching middle initial, and a contemporaneous wartime intelligence role; the index's P-5 grade and protected identifier still require file confirmation.",
                "The sources establish prewar Harvard study and wartime SHAEF service but do not explicitly connect him to OSS.",
                "C_reputable_contemporary_or_scholarly",
                "medium",
                "publish_qualified",
                "The spelling variance remains visible, and the identity is not promoted to high confidence without the indexed personnel file.",
                [
                    {"source_key": INDEX, "support_type": "context_only"},
                    {"source_key": STREET},
                    {"source_key": CRIMSON, "support_type": "context_only"},
                    {"source_key": HARVARD, "support_type": "context_only"},
                ],
            ),
            claim(
                "donald-v-mcgranahan-harvard-university-b1054",
                33,
                "other_pre_oss_affiliation",
                "A probable identity match documents Donald Vincent McGranahan as a Harvard student and 1940 psychology doctoral alumnus.",
                "A contemporary Harvard newspaper names Donald Vincent McGranahan in the class of 1935, and Harvard's official alumni list records Donald McGranahan in 1940.",
                "Probable, not confirmed, because the rare name and initial align with the indexed spelling variant and wartime intelligence role, but no personnel file was reviewed.",
                "Documented prewar student status; neither source establishes employment or an immediate OSS sequence.",
                "B_authoritative_institutional",
                "medium",
                "publish_qualified",
                "Harvard is modeled only as a student institution. This claim is excluded from employer analytics.",
                [{"source_key": CRIMSON}, {"source_key": HARVARD}, {"source_key": STREET, "support_type": "context_only"}],
                "donald-v-mcgranahan-harvard-university-b1054",
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
    for row, (person_id, name, box) in PEOPLE.items():
        update: dict[str, object] = {
            "person_id": person_id,
            "manual_review_required": True,
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
        }
        if row in ARMY_OCCUPATIONS:
            update.update(
                identity_status="high_confidence",
                identity_evidence="The official index and Army entry agree in name and a reviewed nonshared private identifier. The identifier remains private; the dated broad occupation does not establish an employer or OSS sequence.",
                nara_catalog_id="1263923",
                research_status="occupation_only_found",
                next_action=f"Review Box {box} for a named employer or institution and establish the Army-to-OSS chronology.",
                archival_review_priority="high",
            )
        elif row == 14:
            update.update(
                identity_status="high_confidence",
                identity_evidence="The rare exact name, indexed Navy lieutenant context, and institutional biography's explicit Navy and OSS Naval Liaison service support a high-confidence match.",
                research_status="verified_employer_found",
                next_action="Review Box 506 to determine exact Navy and OSS entry dates and confirm whether New York State Assembly service formally continued through the liaison assignment.",
                archival_review_priority="medium",
            )
        elif row == 23:
            update.update(
                identity_status="high_confidence",
                identity_evidence="The uncommon full name and middle initial, indexed commander rank, and Northwestern's independently documented 1941-45 Naval Reserve chronology support a high-confidence match.",
                name_variants=["William Montgomery McGovern"],
                research_status="verified_employer_found",
                next_action="Review Box 506 to establish the exact Naval Reserve-to-OSS sequence and test whether any affiliation intervened after the 1940-41 Harvard appointment.",
                archival_review_priority="high",
            )
        elif row == 33:
            update.update(
                identity_status="probable",
                identity_evidence="The rare near-exact name, matching middle initial, and documented wartime PWD, SHAEF intelligence role support a probable match, but the index's McGrannahan spelling and P-5 record still require file confirmation.",
                name_variants=["Donald V McGranahan", "Donald Vincent McGranahan"],
                research_status="occupation_only_found",
                next_action="Review Box 506 to confirm the McGrannahan/McGranahan spelling variant, protected identifier, P-5 grade, and whether the documented SHAEF psychologist is the indexed person.",
                archival_review_priority="critical",
            )
        elif row == 13:
            update.update(
                identity_status="conflicting",
                identity_evidence="The official Army record linked by the private identifier uses Leon D. McGinnis, conflicting with the index's Leon A. McGinnis. No Army occupation is transferred.",
                research_status="conflicting_sources",
                next_action="Review Box 506 and the original index documentation to resolve the middle-initial conflict before making identity or employment claims.",
                archival_review_priority="critical",
            )
        elif row in {8, 9}:
            update.update(
                identity_status="ambiguous",
                identity_evidence="Two printed rows share the exact indexed name David K. McGinnis but are filed in different boxes. They remain separate without direct duplicate evidence.",
                possible_duplicate_group="p309-david-k-mcginnis-two-boxes-b623",
                research_status="needs_identity_review",
                next_action="Compare the David K. McGinnis personnel files in Boxes 505 and 506 before merging, transferring evidence, or assigning an employer.",
                archival_review_priority="critical",
            )
        elif row in {26, 27}:
            update.update(
                identity_status="ambiguous",
                identity_evidence="Two printed John E. McGowan rows have distinct rank and private identifier evidence. They remain separate pending direct file comparison.",
                possible_duplicate_group="p309-john-e-mcgowan-distinct-identifiers-b623",
                research_status="needs_identity_review",
                next_action="Compare both John E. McGowan personnel files in Box 506 before any merge or transfer of identity and employment evidence.",
                archival_review_priority="critical",
            )
        elif row == 30:
            update.update(
                identity_status="high_confidence",
                identity_evidence="The official index and Army entry agree in name and a reviewed nonshared private identifier, but the Army-entry date is 1945-12-28 and therefore cannot support a pre-OSS occupation claim.",
                nara_catalog_id="1263923",
                research_status="requires_archival_review",
                next_action="Review Box 506 for William H. McGowan's actual pre-OSS affiliation; do not project the post-OSS 1945-12-28 Army occupation backward.",
                archival_review_priority="high",
            )
        elif row == 37:
            update.update(
                identity_status="high_confidence",
                identity_evidence="The official index and Army entry agree in name and a reviewed nonshared private identifier. Historical occupation code 590 is absent from the reviewed official list and is not interpreted.",
                nara_catalog_id="1263923",
                research_status="requires_archival_review",
                next_action="Review Box 506 to identify William McGrath's civilian occupation, employer, and Army-to-OSS chronology; undefined code 590 supplies no defensible occupation.",
                archival_review_priority="high",
            )
        else:
            update.update(
                identity_status="unresolved",
                identity_evidence="Exact-name and meaningful-variant checks across the official index context, CIA-domain discovery, accessible military and institutional sources, Library of Congress newspaper discovery, obituary, directory, and archival searches produced no reliable identity and pre-OSS affiliation bridge; unbridged namesakes were rejected.",
                research_status="requires_archival_review",
                next_action=unresolved_message(name, box),
                archival_review_priority="high",
            )
        values.append(update)
    if len(values) != 46 or len({item["person_id"] for item in values}) != 46:
        raise RuntimeError("Expected 46 separate page-309 person updates")
    return values


def outcome_note(row: int) -> str:
    if row in ARMY_OCCUPATIONS:
        return "An accepted official Army identity link supports a qualified dated occupation or student category but no named employer or OSS-transfer sequence."
    if row == 14:
        return "An institutional legal-history source establishes the Navy-to-OSS pathway, last civilian government affiliation, and two earlier legal employers."
    if row == 23:
        return "Northwestern's archival authority record establishes Harvard as the last documented civilian employer before Naval Reserve service and two earlier employers."
    if row == 33:
        return "A qualified probable identity supports Harvard student status; the spelling variant and indexed P-5 record still require personnel-file confirmation."
    if row == 13:
        return "A middle-initial conflict remains visible; no Army occupation or identity was transferred."
    if row in AMBIGUOUS_ROWS:
        return "An exact-name duplicate cluster remains separated for direct personnel-file comparison."
    if row == 30:
        return "An accepted official Army identity link is dated after OSS ended, so no pre-OSS occupation is projected backward."
    if row == 37:
        return "An accepted official Army identity link uses undefined occupation code 590, which is not interpreted."
    return "No reliable identity or pre-OSS affiliation was established; unbridged namesakes and chronologically irrelevant results were rejected."


def research_attempts() -> list[dict[str, object]]:
    updates = {item["person_id"]: item for item in person_updates()}
    values: list[dict[str, object]] = []
    strong_rows = set(ARMY_OCCUPATIONS) | ARMY_IDENTITY_ONLY | {14, 23, 33}
    for row, (person_id, name, box) in PEOPLE.items():
        if row in strong_rows:
            outcome, reviewed, rejected = "source_reviewed", 5, 2
        elif row in CONFLICT_ROWS | AMBIGUOUS_ROWS:
            outcome, reviewed, rejected = "candidate_rejected", 3, 4
        else:
            outcome, reviewed, rejected = "no_result", 2, 3
        values.append(
            {
                "key": f"page309-row{row}-{slug(name)}-b1054",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index context; exact-name and meaningful initial, punctuation, spacing, spelling and OCR variants; CIA-domain discovery; OSS, rank, branch, assignment and private-identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory and archival searches; indexed Box {box}",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_1054",
                "started_at": "2026-11-11T15:25:00-05:00",
                "completed_at": "2026-11-11T16:20:00-05:00",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, postwar-only leads, and sources without an OSS, rank, private-identifier, unit, or personnel-file bridge were rejected. Exact-name duplicate rows remain separate. Army categories were not converted into named employers; the post-OSS 1945-12-28 entry and undefined code 590 were not published as pre-OSS claims.",
                "research_notes": f"{outcome_note(row)} Page 309 was visually checked against a fresh official NARA download matching the preserved SHA-256. The official index, existing Library of Congress item-level attempts, exact-name OSS and meaningful-variant web discovery, CIA-domain discovery, employment and occupation checks, and obituary, institutional, directory, newspaper, and archival searches were reviewed as applicable. CIA-domain searches returned no person-specific result and were not treated as proof of absence. No search-result snippet was used as final evidence and no authenticated NARA Catalog API request was made.",
                "next_action": str(updates[person_id]["next_action"]),
                "attempt_number": ATTEMPT_NUMBERS[row],
                "research_agent_version": "before-oss-b1054-v1",
            }
        )
    if len(values) != 46 or len({item["person_id"] for item in values}) != 46:
        raise RuntimeError("Expected 46 separate page-309 research attempts")
    return values


def build_bundle() -> dict[str, object]:
    return {
        "bundle_version": "batch-1054-v1",
        "reviewer": "Before OSS Batch 1054 evidence review",
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
