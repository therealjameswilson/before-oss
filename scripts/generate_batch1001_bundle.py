#!/usr/bin/env python3
"""Generate the reviewed Batch 1001 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page491-wargo-to-waters-"
    "review_batch-1001_2026-11-03.json"
)

INDEX = "nara-index-b1001"
ARMY = "army-bulk-b1001"
TECH = "army-tech-b1001"
CODES = "army-codes-b1001"
HOOVER = "hoover-eugene-warner-b1001"
CIA = "cia-fifty-years-law-b1001"
JOHN_OBIT = "washpost-john-warner-b1001"
COPYRIGHT = "copyright-sam-warner-b1001"
UCHICAGO = "uchicago-w-lloyd-warner-b1001"
PRINCETON = "princeton-northam-warren-b1001"
EISENHOWER = "eisenhower-abbott-washburn-b1001"
ABBOTT_OBIT = "washpost-abbott-washburn-b1001"

ORG_HARVARD = "harvard-university-b1001"
ORG_WPB = "war-production-board-b1001"
ORG_UCHICAGO = "university-chicago-b1001"
ORG_ARMY = "us-army-b1001"
ORG_NAVY = "us-navy-b1001"
ORG_UNION_TRUST = "union-trust-company-b1001"
ORG_390BG = "390-bombardment-group-b1001"
ORG_GENERAL_MILLS = "general-mills-b1001"


PEOPLE = {
    1: ("a8016077-f892-598d-b293-e7f46dcdecfd", "Stephen J Wargo"),
    2: ("d9572d34-1f9d-5650-821a-412223e6f362", "Waldo W Waring"),
    3: ("0be00d1d-21ca-569c-a32d-90e74fea3836", "Joseph J Warman"),
    4: ("33c4d214-2cad-5297-a566-5c3580dfc49b", "Adolphe J Warner"),
    5: ("34fe30da-78f4-5535-9b36-55267c69e1ef", "Arthur C Warner"),
    6: ("1f8b79b4-0d38-558f-b3cb-d8f8bfb97aeb", "Edwin E Warner"),
    7: ("404b95d9-57bb-5ec7-9e32-b7467e75c600", "Eugene P Warner"),
    8: ("cc98d8f8-ae18-52be-8f96-c560af5dae31", "J C Warner"),
    9: ("911ff8bb-d5d9-5a83-a676-83444e861b60", "John S Warner"),
    10: ("98e1a775-897d-5d07-a044-83624f91a0de", "Margaret Warner"),
    11: ("8f9d31f3-56d5-5838-9bf5-019c35ab5e9f", "Marion A Warner"),
    12: ("ff8d47e4-635f-59e1-b5e7-b2e4fa11a179", "Ralph P Warner"),
    13: ("efb61a4e-cf44-5022-8b4e-7cb7fb995f0c", "Sam B Warner"),
    14: ("813dbe56-56ea-511f-a41c-1a3d9169874c", "W. Lloyd Warner"),
    15: ("ad9ae311-9c12-544f-bb91-f230050d9e74", "Aaron D Warnock"),
    16: ("c858e5fe-1609-5798-8f79-53eca3937c9c", "John C Warnock"),
    17: ("8b775eea-a03b-543d-98ed-40be4c602792", "* Warren"),
    18: ("b326361e-4098-553d-8f5b-d5b4b490ecb7", "Charles H Warren"),
    19: ("eb5f4e5d-9208-589c-b4f5-02e4274b7711", "Charlie J Warren"),
    20: ("57a43dbf-1a33-534b-955a-aab3b7633fbc", "Darrell F Warren"),
    21: ("dcf0b482-ab8e-5a0e-b0cb-df66645a1504", "Frank Miles Warren"),
    22: ("c2438c9f-b1b8-592d-9468-747d3ed002cb", "George E Warren"),
    23: ("c13d0727-a63f-52e1-89f1-d573971dfa58", "Janet Carolyn Warren"),
    24: ("5ae50702-aae8-56a9-afe3-db1f3ebe690d", "Northam Warren Jr."),
    25: ("a1319427-adda-50e6-bbb4-73717cd45432", "Paul L Warren"),
    26: ("c798347f-5ddf-5442-a80c-caf48cff5455", "Ralph F Warren"),
    27: ("537beed5-76d8-5bd9-ad54-040e0cc3290b", "Helga Rose Warrens"),
    28: ("e9faa646-d4ac-5adc-9c01-4d15da7dec68", "Salomon J Warszawski"),
    29: ("c87c2938-ead3-58f7-8a78-932704b681bb", "George Wartenbert"),
    30: ("1e5c0e34-d68a-52e6-b1f9-cb644b8cccc4", "Anna M Warters"),
    31: ("f4890abc-e000-5bdf-9eb6-e197ced081ab", "John William Waser"),
    32: ("8c491ced-1cd9-5e63-9fd0-0cb81588e02b", "Abbott Washburn"),
    33: ("ec3a1750-f61f-56c5-9742-98c9f2326e0e", "Emlen D Washburn"),
    34: ("88c0e9e9-dd30-521c-beb1-92e5c862f92d", "Arthur Washington"),
    35: ("f6bb3b94-048f-531c-a0c1-f62134849fe8", "Bushrod C Washington"),
    36: ("00b472e6-1caf-594b-bbed-29b903030aea", "Wilbert Washington"),
    37: ("8ac64ad3-5cea-574e-aaca-aa290ad404f8", "John J Wask"),
    38: ("8bb70dd9-0143-5ab0-bbe3-a5cf1c9766d6", "Frank S Watanabe"),
    39: ("1c940876-93a6-5e82-a6f7-0efe4c7a8d92", "Howard T Watanabe"),
    40: ("5d1a383f-2578-5076-9e92-0452cbfa5e5a", "Kazumi Watanabe"),
    41: ("84b75ea2-9eac-5961-887c-1a3f41470449", "Lucy E Waterman"),
    42: ("9f2c0364-363a-56a9-b48c-9c977039b1a5", "Richard E Waterman"),
    43: ("88879c6b-b450-5195-9c97-37ff0c25779c", "Robert W Waterman"),
    44: ("41976ddf-1fc5-5600-95eb-52fcfc4dd71b", "Robert P Waterman"),
    45: ("6be568c2-1fab-5868-be5f-6e11b6d3bf03", "Alexander Waters"),
    46: ("b36e432f-89da-55ae-931d-211f2cd4f2d1", "Arthur R Waters"),
}


ARMY_OCCUPATIONS = {
    3: {"date": "1943-05-05", "code": "471", "occupation": "jeweler, watchmaker, goldsmith, or silversmith", "label": "Jewelers, watchmakers, goldsmiths, and silversmiths", "locator": "PDF physical page 173; historical category 4-71"},
    4: {"date": "1943-02-24", "code": "185", "occupation": "salesman or sales agent, except to consumers", "label": "Salesmen and sales agents, except to consumers", "locator": "PDF physical page 172; historical category 1-85"},
    12: {"date": "1942-10-26", "code": "686", "occupation": "blacksmith, forgerman, or hammerman", "label": "Blacksmiths, forgemen, and hammermen", "locator": "PDF physical page 174; historical category 6-86"},
    16: {"date": "1944-06-30", "code": "992", "occupation": "student", "label": "Student", "locator": "PDF physical page 304; historical civilian-occupation code 992"},
    19: {"date": "1942-11-29", "code": "306", "occupation": "general farmer", "label": "General farmers", "locator": "PDF physical page 172; historical category 3-06"},
    20: {"date": "1943-03-16", "code": "497", "occupation": "electrician", "label": "Electricians", "locator": "PDF physical page 173; historical category 4-97"},
    38: {"date": "1941-10-23", "code": "170", "occupation": "sales clerk", "label": "Sales clerks", "locator": "PDF physical page 171; historical category 1-70"},
    39: {"date": "1943-03-24", "code": "104", "occupation": "general clerk", "label": "Clerks, general", "locator": "PDF physical page 171; historical category 1-04"},
    42: {"date": "1944-11-03", "code": "992", "occupation": "student", "label": "Student", "locator": "PDF physical page 304; historical civilian-occupation code 992"},
}


UNRESOLVED = {
    2: "Rank-aware common-name searches produced no source with an OSS assignment, indexed identifier, employer chronology, or Box 816 bridge.",
    5: "Common-name and middle-initial searches produced only unbridged namesakes and no reliable OSS, employment, or personnel-file identity bridge.",
    6: "Exact-name and meaningful-variant searches produced no source with an OSS assignment, indexed identifier, employer chronology, or Box 817 bridge.",
    8: "Initial-only searches were too ambiguous to support an external identity, occupation, employer, or OSS-assignment claim.",
    10: "Exact-name, obituary, directory, institutional, newspaper, and archival searches yielded only unbridged namesakes.",
    11: "Exact-name and middle-initial searches produced no reliable OSS, employment, institutional, or archival identity bridge.",
    15: "The distinctive full name produced no source with an OSS, protected-identifier, employer, occupation, or personnel-file bridge.",
    17: "The index explicitly prints no first name; surname-only searches cannot identify a unique person without the Box 817 personnel file.",
    18: "The printed Captain and USNR note establish naval officer status, but exact-name searches produced no reliable external identity or employer bridge.",
    21: "Exact-name and meaningful-variant searches produced no source with an OSS, indexed-identifier, employer, occupation, or personnel-file bridge.",
    22: "The printed Private First Class rank establishes Army status, but common-name searches produced no reliable external identity or employment bridge.",
    23: "Exact-name searches yielded no source with an OSS assignment, indexed identifier, employer chronology, or Box 817 bridge.",
    25: "Common-name searches produced no source with the middle initial, indexed identifier, employer chronology, or direct OSS assignment bridge.",
    26: "Common-name searches produced no source with the middle initial, indexed identifier, employer chronology, or direct OSS assignment bridge.",
    27: "Exact-name and spelling-variant searches produced no source with an OSS, employer, occupation, or personnel-file bridge.",
    28: "Exact-name and transliteration-aware searches produced no source with an OSS, employer, occupation, or personnel-file bridge.",
    29: "The distinctive printed spelling produced no source with an OSS, employer, occupation, or personnel-file bridge; no spelling correction is inferred.",
    30: "Exact-name, occupation, obituary, institutional, directory, and archival searches produced no reliable identity bridge.",
    31: "The printed Corporal rank establishes Army status, but exact-name searches produced no reliable external identity or employment bridge.",
    33: "Exact-name and middle-initial searches produced no source with an OSS assignment, indexed identifier, employer chronology, or Box 818 bridge.",
    34: "Common-name searches produced no source with an OSS assignment, protected identifier, employer chronology, or Box 818 bridge.",
    35: "The distinctive full name produced no source that reliably bridges the indexed person to an employer, occupation, or OSS assignment.",
    36: "Common-name searches produced no source with an OSS assignment, indexed identifier, employer chronology, or Box 818 bridge.",
    37: "The printed Radioman second class and Navy note establish enlisted naval status, but searches produced no reliable employer or external identity bridge.",
    40: "Exact-name and meaningful-variant searches produced no reliable OSS, employer, occupation, obituary, institutional, or archival identity bridge.",
    41: "Exact-name and middle-initial searches produced no source with an OSS assignment, indexed identifier, employer chronology, or Box 818 bridge.",
    43: "Common-name searches produced only unbridged namesakes and no source with an indexed identifier or direct OSS assignment bridge.",
    44: "The printed Captain rank establishes Army officer status, but common-name searches produced no reliable external identity or employer bridge.",
    45: "Common-name and archival searches produced only unbridged namesakes and no reliable OSS, occupation, or employer bridge.",
    46: "The printed First Lieutenant rank establishes Army officer status, but exact-name searches produced no reliable external identity or employer bridge.",
}


PRINTED_CATEGORIES = {
    2: ("commissioned_army_officer", True),
    18: ("commissioned_naval_officer", True),
    22: ("enlisted_army_personnel", False),
    31: ("enlisted_army_personnel", False),
    37: ("enlisted_naval_personnel", False),
    44: ("commissioned_army_officer", True),
    46: ("commissioned_army_officer", True),
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 816-818",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 491, rows 1-46; checked against layout-preserving text and an original-detail page render",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 46 printed rows remain separate. The asterisk and 'no first n' note at row 17 are preserved literally. Protected identifiers remain private.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; nine accepted and one conflicting protected-identifier comparison; identifiers and record ordinals withheld",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "Nine exact-name identity bridges were accepted after private review. Stephen J. Wargo remains conflicting because the Army given name is Stephan; no occupation was transferred.",
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
            "locator": "PDF physical pages 171-174 and 304; historical civilian-occupation categories 1-04, 1-70, 1-85, 3-06, 4-71, 4-97, 6-86, and 992",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical labels identify broad occupations or student status, not named employers, workplaces, schools, or exact OSS-transfer dates.",
        },
        {
            "key": HOOVER,
            "stable_url": "https://digitalcollections.hoover.org/internal/media/dispatcher/331573/full",
            "archival_identifier": "Hoover Digital Collections internal media 331573",
            "title": "Office of Strategic Services board proceedings at Caserta",
            "author_creator": "Office of Strategic Services",
            "repository_publisher": "Hoover Institution Library & Archives",
            "publication_record_date": "1944-05-04",
            "locator": "Board proceedings, Eugene P. Warner testimony; civilian status and entry into OSS in January 1942",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "Office of Strategic Services records",
            "rights_notes": "The direct record identifies Warner as a reporter and writer in civilian life but names no employer or newspaper.",
        },
        {
            "key": CIA,
            "stable_url": "https://www.cia.gov/readingroom/docs/FIFTY%20YEARS%20UNDER%20LAW%5B16059810%5D.pdf",
            "archival_identifier": "CIA FOIA release C06863740",
            "title": "Fifty Years Under Law",
            "author_creator": "Central Intelligence Agency",
            "repository_publisher": "CIA Freedom of Information Act Electronic Reading Room",
            "publication_record_date": "2022-04-28 release",
            "locator": "PDF page 152; John S. Warner identified in the SSU/CIG legal-office chronology",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "CIA FOIA Electronic Reading Room",
        },
        {
            "key": JOHN_OBIT,
            "stable_url": "https://www.legacy.com/us/obituaries/washingtonpost/name/john-warner-obituary?id=5562689",
            "title": "John Stanley Warner Sr. obituary",
            "author_creator": "The Washington Post obituary",
            "repository_publisher": "The Washington Post via Legacy.com",
            "publication_record_date": "2006-05-02",
            "locator": "Biographical chronology: Union Trust Company, active Army service, 390th Bombardment Group, and December 1944 OSS detail",
            "access_date": "2026-11-03",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "rights_notes": "Used with the CIA institutional history to corroborate identity and chronology; excerpts are limited to the minimum necessary.",
        },
        {
            "key": COPYRIGHT,
            "stable_url": "https://copyright.gov/about/registers/warner/warner.html",
            "title": "Sam Bass Warner, Register of Copyrights",
            "author_creator": "United States Copyright Office",
            "repository_publisher": "United States Copyright Office, Library of Congress",
            "publication_record_date": "undated institutional biography",
            "locator": "Career biography; Harvard leave in 1942 and wartime War Production Board service",
            "access_date": "2026-11-03",
            "source_quality": "B_authoritative_institutional",
            "rights_notes": "The biography documents wartime affiliations but does not state the exact sequence between the War Production Board and OSS.",
        },
        {
            "key": UCHICAGO,
            "stable_url": "https://photoarchive.lib.uchicago.edu/db.xqy?one=apf1-08578.xml",
            "archival_identifier": "University of Chicago Photographic Archive apf1-08578",
            "title": "Warner, W. Lloyd",
            "author_creator": "University of Chicago Library",
            "repository_publisher": "University of Chicago Photographic Archive",
            "publication_record_date": "undated collection record",
            "locator": "Biographical note: professor of anthropology and sociology, University of Chicago, 1935-1959",
            "access_date": "2026-11-03",
            "source_quality": "B_authoritative_institutional",
            "rights_notes": "The institutional record documents employment, but not the precise transition into or out of indexed OSS service.",
        },
        {
            "key": PRINCETON,
            "stable_url": "https://paw.princeton.edu/memorial/northam-warren-jr-37",
            "title": "Northam Warren Jr. '37",
            "author_creator": "Princeton Alumni Weekly",
            "repository_publisher": "Princeton Alumni Weekly; Princeton University",
            "publication_record_date": "2013-12-04",
            "locator": "Memorial biography; Army service at Fort Sill and Fort Benning, rising to major",
            "access_date": "2026-11-03",
            "source_quality": "B_authoritative_institutional",
            "rights_notes": "The memorial documents Army service but supplies no dates or direct OSS transition. Postwar employment is not presented as pre-OSS work.",
        },
        {
            "key": EISENHOWER,
            "stable_url": "https://www.eisenhowerlibrary.gov/sites/default/files/finding-aids/pdf/washburn-abbott-papers.pdf",
            "archival_identifier": "Dwight D. Eisenhower Library, Abbott Washburn Papers, accessions 04-16, 07-3 and 07-3/1",
            "title": "Washburn, Abbott: Papers, 1938-2003",
            "author_creator": "Dwight D. Eisenhower Presidential Library",
            "repository_publisher": "Dwight D. Eisenhower Presidential Library, National Archives and Records Administration",
            "publication_record_date": "2008-06",
            "locator": "Scope and Content Note, PDF physical page 2; General Mills employment beginning in 1937 with a World War II interruption",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "Abbott Washburn Papers, 1938-2003",
        },
        {
            "key": ABBOTT_OBIT,
            "stable_url": "https://www.washingtonpost.com/archive/local/2003/12/19/abbott-washburn-88-dies/d2dd2e4f-b4ef-4e0a-b9c7-a055c4c14f30/",
            "title": "Abbott Washburn, 88, Dies",
            "author_creator": "The Washington Post",
            "repository_publisher": "The Washington Post",
            "publication_record_date": "2003-12-19",
            "locator": "Obituary paragraphs identifying Navy service, OSS assignment in Europe, and General Mills public-relations work",
            "access_date": "2026-11-03",
            "source_quality": "C_reputable_contemporary_or_scholarly",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": ORG_HARVARD,
            "organization_id": "45ddf347-21c6-59f5-a8ae-517418adf941",
            "canonical_name": "Harvard University",
            "historical_name": "Harvard University",
            "aliases": [],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "Cambridge",
            "state_or_region": "Massachusetts",
            "country": "United States",
            "normalization_notes": "Canonical existing university entity; the historical name is unchanged.",
        },
        {
            "key": ORG_WPB,
            "organization_id": "92be7d87-ebc8-5b56-b469-380867bdafe1",
            "canonical_name": "War Production Board",
            "historical_name": "War Production Board",
            "aliases": ["WPB"],
            "organization_type": "federal agency",
            "sector": "federal_government",
            "city": "Washington",
            "state_or_region": "District of Columbia",
            "country": "United States",
            "active_dates": "1942-1945",
            "normalization_notes": "Preserved as the wartime federal agency, not merged into a modern successor.",
        },
        {
            "key": ORG_UCHICAGO,
            "organization_id": "f2c878b0-ee44-573d-ab30-7e4282bc85e5",
            "canonical_name": "University of Chicago",
            "historical_name": "University of Chicago",
            "aliases": [],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "Chicago",
            "state_or_region": "Illinois",
            "country": "United States",
            "normalization_notes": "Canonical existing university entity; the historical name is unchanged.",
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
            "normalization_notes": "Service-level entity used because the accessible biography names no narrower wartime unit chronology.",
        },
        {
            "key": ORG_NAVY,
            "organization_id": "3960fa8e-a551-56cf-9a81-a468deaa2e2f",
            "canonical_name": "United States Navy",
            "historical_name": "United States Navy",
            "aliases": ["U.S. Navy"],
            "organization_type": "military service",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "Service-level entity; no narrower Navy unit is inferred from the obituary.",
        },
        {
            "key": ORG_UNION_TRUST,
            "canonical_name": "Union Trust Company",
            "historical_name": "Union Trust Company",
            "aliases": ["Union Trust Company, Washington, D.C."],
            "organization_type": "bank and trust company",
            "sector": "finance_and_banking",
            "city": "Washington",
            "state_or_region": "District of Columbia",
            "country": "United States",
            "normalization_notes": "The 1935-1943 employer name is preserved; no modern successor is substituted.",
        },
        {
            "key": ORG_390BG,
            "canonical_name": "390th Bombardment Group (Heavy)",
            "historical_name": "390th Bombardment Group (H)",
            "aliases": ["390th Bomb Group", "390th Bombardment Group"],
            "organization_type": "Army Air Forces bombardment group",
            "sector": "military",
            "country": "United States",
            "active_dates": "1943-1945",
            "normalization_notes": "The wartime unit is kept distinct from its memorial foundation and later successor organizations.",
        },
        {
            "key": ORG_GENERAL_MILLS,
            "canonical_name": "General Mills, Inc.",
            "historical_name": "General Mills",
            "aliases": ["General Mills Inc."],
            "organization_type": "food manufacturing company",
            "sector": "business_and_industry",
            "city": "Minneapolis",
            "state_or_region": "Minnesota",
            "country": "United States",
            "normalization_notes": "The historical corporate name is preserved; no successor or subsidiary is substituted.",
        },
    ]


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, item in ARMY_OCCUPATIONS.items():
        values.append({
            "key": f"{slug(PEOPLE[row][1])}-army-occupation-b1001",
            "person_id": PEOPLE[row][0],
            "occupation": item["occupation"],
            "relationship_type": "student" if item["code"] == "992" else "unknown",
            "end_date": item["date"],
            "date_precision": f"Historical civilian-occupation code {item['code']} was recorded at Army entry on {item['date']}; no named employer, workplace, school, or exact OSS-transfer date is supplied.",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "confirmed",
            "claim_confidence": "medium",
            "source_quality": "A_direct_official",
            "publication_status": "publish_qualified",
            "research_notes": "Broad historical occupation or student category only; no named employer, workplace, or school is inferred.",
        })
    values.extend([
        {
            "key": "eugene-warner-reporter-writer-b1001",
            "person_id": PEOPLE[7][0],
            "occupation": "reporter and writer",
            "relationship_type": "unknown",
            "end_date": "1942-01",
            "date_precision": "The May 1944 OSS testimony says Warner entered OSS in January 1942 and had been a reporter and writer in civilian life; it names no employer.",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "probable_immediate",
            "identity_confidence": "high_confidence",
            "claim_confidence": "medium",
            "source_quality": "A_direct_official",
            "publication_status": "publish_qualified",
            "research_notes": "Occupation only. The record does not establish a named employer, newspaper, exact end date, or absence of an intervening affiliation.",
        },
        {
            "key": "john-warner-390-bomb-group-b1001",
            "person_id": PEOPLE[9][0],
            "organization_key": ORG_390BG,
            "organization_name_as_found": "390th Bombardment Group (H)",
            "role_title": "B-17 pilot",
            "occupation": "Army Air Forces officer and bomber pilot",
            "relationship_type": "military_assignment",
            "start_date": "1944-05",
            "end_date": "1944-12",
            "date_precision": "The obituary dates arrival in England to May 1944, 35 missions with the group, and the OSS detail to December 1944.",
            "country": "United Kingdom",
            "immediate_pre_oss": True,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "explicit_immediate",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "published",
            "research_notes": "The explicit December 1944 detail connects the wartime unit chronology to OSS; the CIA history independently corroborates the exact legal-officer identity.",
        },
        {
            "key": "john-warner-union-trust-b1001",
            "person_id": PEOPLE[9][0],
            "organization_key": ORG_UNION_TRUST,
            "organization_name_as_found": "Union Trust Company",
            "role_title": "Assistant Trust Investment Officer",
            "occupation": "bank trust investment officer",
            "relationship_type": "employment",
            "start_date": "1935",
            "end_date": "1943-03",
            "date_precision": "The obituary states employment from 1935 until entrance on active military service in March 1943.",
            "city": "Washington",
            "state_or_region": "District of Columbia",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": True,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "published",
            "research_notes": "Explicitly the last civilian employment before active military service, not the immediate institutional predecessor to OSS.",
        },
        {
            "key": "sam-warner-harvard-b1001",
            "person_id": PEOPLE[13][0],
            "organization_key": ORG_HARVARD,
            "organization_name_as_found": "Harvard University",
            "role_title": "professor",
            "occupation": "law professor",
            "relationship_type": "employment",
            "end_date": "1942",
            "date_precision": "The Copyright Office biography says Warner took leave from Harvard in 1942 for wartime service; the exact OSS transition is not stated.",
            "city": "Cambridge",
            "state_or_region": "Massachusetts",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "high_confidence",
            "claim_confidence": "medium",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "publish_qualified",
            "research_notes": "Documented prewar employment only. The available biography does not prove whether Harvard was the last civilian employer before indexed OSS service.",
        },
        {
            "key": "sam-warner-wpb-b1001",
            "person_id": PEOPLE[13][0],
            "organization_key": ORG_WPB,
            "organization_name_as_found": "War Production Board",
            "role_title": "head attorney for compliance",
            "occupation": "government attorney",
            "relationship_type": "government_assignment",
            "start_date": "1942",
            "end_date": "1945",
            "date_precision": "The institutional biography places the role during World War II but does not give exact dates or its sequence relative to OSS.",
            "city": "Washington",
            "state_or_region": "District of Columbia",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "temporal_relation_uncertain",
            "identity_confidence": "high_confidence",
            "claim_confidence": "medium",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "publish_qualified",
            "research_notes": "The wartime government assignment is documented, but its relationship to indexed OSS service requires the personnel file.",
        },
        {
            "key": "w-lloyd-warner-uchicago-b1001",
            "person_id": PEOPLE[14][0],
            "organization_key": ORG_UCHICAGO,
            "organization_name_as_found": "University of Chicago",
            "role_title": "professor of anthropology and sociology",
            "occupation": "anthropologist and sociologist",
            "relationship_type": "employment",
            "start_date": "1935",
            "end_date": "1959",
            "date_precision": "University archival metadata dates the professorship 1935-1959; the exact OSS-service interval is not stated.",
            "city": "Chicago",
            "state_or_region": "Illinois",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "high_confidence",
            "claim_confidence": "medium",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "publish_qualified",
            "research_notes": "The institutional employment spans the prewar and wartime years, but no accessible source establishes the precise transition to OSS.",
        },
        {
            "key": "northam-warren-army-b1001",
            "person_id": PEOPLE[24][0],
            "organization_key": ORG_ARMY,
            "organization_name_as_found": "Army",
            "role_title": "officer, rising to major",
            "occupation": "Army officer",
            "relationship_type": "military_assignment",
            "date_precision": "The Princeton memorial identifies Army service at Fort Sill and Fort Benning and the rank of major, but gives no dates or direct OSS transition.",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "temporal_relation_uncertain",
            "identity_confidence": "high_confidence",
            "claim_confidence": "medium",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "publish_qualified",
            "research_notes": "Military service only. The memorial's postwar employer is not treated as pre-OSS employment.",
        },
        {
            "key": "abbott-washburn-navy-b1001",
            "person_id": PEOPLE[32][0],
            "organization_key": ORG_NAVY,
            "organization_name_as_found": "Navy",
            "role_title": "Navy servicemember assigned to OSS in Europe",
            "occupation": "Navy servicemember",
            "relationship_type": "military_assignment",
            "date_precision": "The obituary states Navy service during World War II and assignment to OSS in Europe; exact dates and unit are not supplied.",
            "country": "United States",
            "immediate_pre_oss": True,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "explicit_immediate",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "published",
            "research_notes": "The obituary explicitly presents OSS as a Navy assignment; no rank or narrower unit is inferred.",
        },
        {
            "key": "abbott-washburn-general-mills-b1001",
            "person_id": PEOPLE[32][0],
            "organization_key": ORG_GENERAL_MILLS,
            "organization_name_as_found": "General Mills",
            "role_title": "public services office employee",
            "occupation": "public relations specialist",
            "relationship_type": "employment",
            "start_date": "1937",
            "date_precision": "The official finding aid dates employment from 1937, interrupted only by World War II service, and continuing after the war until 1950.",
            "city": "Minneapolis",
            "state_or_region": "Minnesota",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": True,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "A_direct_official",
            "publication_status": "published",
            "research_notes": "The wartime service interruption establishes General Mills as the last documented civilian employer before military service; the finding aid gives no exact interruption date.",
        },
    ])
    return values


def make_claim(
    *,
    key: str,
    row: int,
    claim_type: str,
    text: str,
    paraphrase: str,
    identity: str,
    temporal: str,
    quality: str,
    confidence: str,
    publication: str,
    notes: str,
    source_links: list[dict[str, str]],
    affiliation_key: str | None = None,
) -> dict[str, object]:
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
    for row, item in ARMY_OCCUPATIONS.items():
        name = PEOPLE[row][1]
        values.extend([
            make_claim(
                key=f"identity-{slug(name)}-b1001",
                row=row,
                claim_type="identity",
                text=f"Indexed {name} is confirmed as the reviewed official Army entry record.",
                paraphrase="The exact indexed and Army names agree, and a nonshared protected identifier connects the records.",
                identity="Confirmed by exact name and a nonshared protected-identifier agreement; the identifier and record ordinal remain private.",
                temporal=f"The Army record dates entry to {item['date']} and supplies only historical civilian code {item['code']}.",
                quality="A_direct_official",
                confidence="confirmed",
                publication="published",
                notes="Identity only; no named employer, workplace, school, or exact OSS-transfer date is inferred.",
                source_links=[
                    {"source_key": INDEX, "locator_override": f"PDF page 491 row {row}; protected identifier withheld"},
                    {"source_key": ARMY, "locator_override": "Accepted reviewed identity bridge; protected identifier withheld"},
                ],
            ),
            make_claim(
                key=f"occupation-{slug(name)}-b1001",
                row=row,
                claim_type="occupation",
                text=f"At Army entry on {item['date']}, {name} was recorded in the historical {item['occupation']} category; no named employer or institution is identified.",
                paraphrase=f"The accepted Army record carries civilian-occupation code {item['code']}, decoded from NARA's official code list.",
                identity="The category belongs only to the confirmed protected-identifier match; the identifier itself is not public.",
                temporal="Strongly date-bounded to Army entry; it does not establish the immediate pre-OSS affiliation or a named employer or school.",
                quality="A_direct_official",
                confidence="medium",
                publication="publish_qualified",
                notes="Published with its limits and excluded from verified-employer analytics.",
                source_links=[
                    {"source_key": ARMY, "locator_override": f"Army entry {item['date']}; civilian occupation code {item['code']}; protected identifier withheld"},
                    {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46"},
                    {"source_key": CODES, "locator_override": item["locator"], "excerpt_override": item["label"]},
                ],
                affiliation_key=f"{slug(name)}-army-occupation-b1001",
            ),
        ])

    values.extend([
        make_claim(
            key="conflict-stephen-wargo-b1001",
            row=1,
            claim_type="identity",
            text="Stephen J Wargo's reviewed Army candidate remains conflicting because the official Army given name is Stephan rather than Stephen.",
            paraphrase="A protected identifier connects the rows, but the material given-name difference is preserved pending personnel-file review.",
            identity="Conflicting: the protected identifier aligns, while the given-name spellings materially differ.",
            temporal="No occupation, grade, or chronology is transferred from the Army candidate until the conflict is resolved.",
            quality="A_direct_official",
            confidence="conflicting",
            publication="conflicting",
            notes="The conflict remains visible without exposing the protected identifier.",
            source_links=[
                {"source_key": INDEX, "locator_override": "PDF page 491 row 1; protected identifier withheld"},
                {"source_key": ARMY, "locator_override": "Conflicting reviewed candidate; Army given name Stephan; protected identifier withheld"},
            ],
        ),
        make_claim(
            key="identity-eugene-p-warner-b1001",
            row=7,
            claim_type="identity",
            text="The indexed civilian Eugene P Warner is a high-confidence match to Eugene P. Warner in the May 1944 OSS board proceedings.",
            paraphrase="The exact name, civilian status, and direct OSS chronology align between the index and official board record.",
            identity="High confidence from exact full name, matching civilian status, and direct OSS service context.",
            temporal="The record says he entered OSS in January 1942; it does not identify his civilian employer.",
            quality="A_direct_official",
            confidence="high",
            publication="published",
            notes="Direct official identity bridge; the Box 817 file remains the target for a named employer.",
            source_links=[
                {"source_key": INDEX, "locator_override": "PDF page 491 row 7; Civilian; Box 817"},
                {"source_key": HOOVER, "excerpt_override": "Entered OSS January 1942 (then COI) to do propaganda work."},
            ],
        ),
        make_claim(
            key="occupation-eugene-p-warner-b1001",
            row=7,
            claim_type="occupation",
            text="Before entering OSS in January 1942, Eugene P Warner had been a reporter and writer; no named employer is identified.",
            paraphrase="His May 1944 OSS testimony describes his civilian occupation as reporter and writer and dates entry into OSS to January 1942.",
            identity="High confidence from the direct official identity bridge.",
            temporal="Probably immediate from the testimony's compressed career narrative, but the record does not exclude an intervening affiliation.",
            quality="A_direct_official",
            confidence="medium",
            publication="publish_qualified",
            notes="Occupation only; not counted as a verified employer or settled immediate affiliation.",
            source_links=[
                {"source_key": HOOVER, "excerpt_override": "Was reporter and writer in civilian life."},
            ],
            affiliation_key="eugene-warner-reporter-writer-b1001",
        ),
        make_claim(
            key="identity-john-s-warner-b1001",
            row=9,
            claim_type="identity",
            text="The indexed John S Warner is a high-confidence match to John Stanley Warner, the wartime bomber pilot detailed to OSS in December 1944.",
            paraphrase="The full middle-name expansion, OSS detail, later SSU/CIG legal role, and bomber-pilot chronology align across institutional and biographical sources.",
            identity="High confidence from exact indexed initials plus a specific OSS-to-SSU/CIG career chronology corroborated by an official CIA history.",
            temporal="The obituary provides an explicit 1935-1944 employment and military chronology ending in an OSS detail.",
            quality="A_direct_official",
            confidence="high",
            publication="published",
            notes="The CIA source corroborates identity and later institutional continuity; the obituary supplies the detailed pre-OSS chronology.",
            source_links=[
                {"source_key": INDEX, "locator_override": "PDF page 491 row 9; Box 817"},
                {"source_key": CIA, "locator_override": "PDF page 152"},
                {"source_key": JOHN_OBIT, "locator_override": "Biographical chronology, paragraphs 3-5"},
            ],
        ),
        make_claim(
            key="immediate-john-warner-390-bomb-group-b1001",
            row=9,
            claim_type="immediate_pre_oss_affiliation",
            text="John S Warner's immediate documented pre-OSS assignment was as a B-17 pilot with the 390th Bombardment Group (Heavy).",
            paraphrase="The obituary places 35 missions with the 390th Bombardment Group immediately before his December 1944 detail to OSS.",
            identity="High confidence from the corroborated full biography and OSS legal-career continuity.",
            temporal="Explicitly immediate: the source narrates the group assignment and then the December 1944 OSS detail.",
            quality="C_reputable_contemporary_or_scholarly",
            confidence="high",
            publication="published",
            notes="Military assignment, not civilian employment.",
            source_links=[
                {"source_key": JOHN_OBIT, "excerpt_override": "was detailed to the Office of Strategic Services (OSS) in December 1944"},
                {"source_key": CIA, "support_type": "context_only", "locator_override": "PDF page 152"},
            ],
            affiliation_key="john-warner-390-bomb-group-b1001",
        ),
        make_claim(
            key="last-civilian-john-warner-union-trust-b1001",
            row=9,
            claim_type="last_civilian_pre_service",
            text="John S Warner's last documented civilian employer before active military service was Union Trust Company in Washington, D.C.",
            paraphrase="The obituary states that he worked there from 1935 until entering active service in March 1943.",
            identity="High confidence from the corroborated full biography and OSS legal-career continuity.",
            temporal="Explicitly bounded as civilian employment ending when active military service began.",
            quality="C_reputable_contemporary_or_scholarly",
            confidence="high",
            publication="published",
            notes="Distinguished from the later 390th Bombardment Group immediate pre-OSS military assignment.",
            source_links=[
                {"source_key": JOHN_OBIT, "excerpt_override": "Was employed from 1935 to March 1943 at the Union Trust Company, Washington, DC, as an Assistant Trust Investment Officer."},
            ],
            affiliation_key="john-warner-union-trust-b1001",
        ),
        make_claim(
            key="identity-sam-b-warner-b1001",
            row=13,
            claim_type="identity",
            text="The indexed Sam B Warner is a high-confidence match to Sam Bass Warner, the Harvard professor documented in wartime government service.",
            paraphrase="The distinctive name and middle initial align with an official institutional biography spanning Harvard and wartime federal work.",
            identity="High confidence from the distinctive exact name and relevant wartime chronology; direct Box 817 confirmation is still required.",
            temporal="The biography documents a 1942 Harvard leave and wartime assignments but does not state the exact OSS sequence.",
            quality="B_authoritative_institutional",
            confidence="high",
            publication="published",
            notes="The identity is published; the affiliation chronology remains qualified.",
            source_links=[
                {"source_key": INDEX, "locator_override": "PDF page 491 row 13; Box 817"},
                {"source_key": COPYRIGHT, "locator_override": "Career biography"},
            ],
        ),
        make_claim(
            key="employment-sam-warner-harvard-b1001",
            row=13,
            claim_type="other_pre_oss_affiliation",
            text="Sam B Warner was a Harvard University professor and took leave in 1942 for wartime service.",
            paraphrase="The Copyright Office biography identifies Harvard employment and a 1942 wartime leave.",
            identity="High confidence from the distinctive name and institutional biography.",
            temporal="Documented prewar employment, but not proven to be the last civilian employer or immediate predecessor to OSS.",
            quality="B_authoritative_institutional",
            confidence="medium",
            publication="publish_qualified",
            notes="Published as documented prewar employment while the exact OSS transition remains an archival question.",
            source_links=[
                {"source_key": COPYRIGHT, "locator_override": "Career biography; 1942 Harvard leave"},
            ],
            affiliation_key="sam-warner-harvard-b1001",
        ),
        make_claim(
            key="assignment-sam-warner-wpb-b1001",
            row=13,
            claim_type="other_pre_oss_affiliation",
            text="During World War II, Sam B Warner served as head attorney for compliance at the War Production Board.",
            paraphrase="The Copyright Office biography identifies the wartime federal legal role.",
            identity="High confidence from the distinctive name and institutional biography.",
            temporal="Documented wartime assignment; its sequence relative to OSS is not established by the accessible source.",
            quality="B_authoritative_institutional",
            confidence="medium",
            publication="publish_qualified",
            notes="Government assignment, not civilian employment; excluded from immediate-affiliation analytics until chronology is resolved.",
            source_links=[
                {"source_key": COPYRIGHT, "excerpt_override": "held the position of head attorney for compliance of the War Production Board"},
            ],
            affiliation_key="sam-warner-wpb-b1001",
        ),
        make_claim(
            key="identity-w-lloyd-warner-b1001",
            row=14,
            claim_type="identity",
            text="The indexed W. Lloyd Warner is a high-confidence match to the University of Chicago anthropologist and sociologist.",
            paraphrase="The uncommon indexed form aligns exactly with the university's archival name and a 1935-1959 professorial chronology.",
            identity="High confidence from the distinctive exact name and institutionally documented wartime-era career; direct Box 817 confirmation remains desirable.",
            temporal="The professorship spans the prewar and wartime years, but the OSS-service interval is not stated.",
            quality="B_authoritative_institutional",
            confidence="high",
            publication="published",
            notes="Identity is published while the employment-to-OSS sequence is qualified.",
            source_links=[
                {"source_key": INDEX, "locator_override": "PDF page 491 row 14; Box 817"},
                {"source_key": UCHICAGO, "locator_override": "Biographical note"},
            ],
        ),
        make_claim(
            key="employment-w-lloyd-warner-uchicago-b1001",
            row=14,
            claim_type="other_pre_oss_affiliation",
            text="W. Lloyd Warner was a University of Chicago professor of anthropology and sociology from 1935 to 1959.",
            paraphrase="The university archival record identifies his departments and dates his professorship.",
            identity="High confidence from the distinctive exact name and university archival record.",
            temporal="Documented before and across the wartime period, but not proven to be the immediate pre-OSS affiliation or last civilian employer.",
            quality="B_authoritative_institutional",
            confidence="medium",
            publication="publish_qualified",
            notes="Published as documented prewar employment with the transition limitation visible.",
            source_links=[
                {"source_key": UCHICAGO, "locator_override": "Biographical note; professor, 1935-1959"},
            ],
            affiliation_key="w-lloyd-warner-uchicago-b1001",
        ),
        make_claim(
            key="identity-northam-warren-jr-b1001",
            row=24,
            claim_type="identity",
            text="The indexed Northam Warren Jr. is a high-confidence match to the Princeton alumnus who served in the Army and rose to major.",
            paraphrase="The distinctive exact name and suffix align with an institutional memorial describing relevant wartime Army service.",
            identity="High confidence from the rare exact name, suffix, and wartime Army service; direct Box 817 confirmation is still required.",
            temporal="The memorial supplies no service dates or direct OSS-transition statement.",
            quality="B_authoritative_institutional",
            confidence="high",
            publication="published",
            notes="The memorial's postwar employment is not used as pre-OSS evidence.",
            source_links=[
                {"source_key": INDEX, "locator_override": "PDF page 491 row 24; Box 817"},
                {"source_key": PRINCETON, "locator_override": "Memorial biography"},
            ],
        ),
        make_claim(
            key="assignment-northam-warren-army-b1001",
            row=24,
            claim_type="other_pre_oss_affiliation",
            text="Northam Warren Jr. served in the United States Army at Fort Sill and Fort Benning and rose to major.",
            paraphrase="The Princeton memorial documents the Army locations and rank.",
            identity="High confidence from the rare exact name, suffix, and relevant wartime service.",
            temporal="The relation to OSS is uncertain because the source provides no dates or transfer chronology.",
            quality="B_authoritative_institutional",
            confidence="medium",
            publication="publish_qualified",
            notes="Military assignment only; not labeled immediate pre-OSS.",
            source_links=[
                {"source_key": PRINCETON, "excerpt_override": "He served in the Army at Fort Sill, Okla., and Fort Benning, Ga., rising to the rank of major."},
            ],
            affiliation_key="northam-warren-army-b1001",
        ),
        make_claim(
            key="identity-abbott-washburn-b1001",
            row=32,
            claim_type="identity",
            text="The indexed Abbott Washburn is a high-confidence match to Abbott McConnell Washburn, the Navy servicemember assigned to OSS in Europe.",
            paraphrase="The distinctive exact name, Navy-to-OSS chronology, and General Mills career align across a NARA presidential-library finding aid and a reputable obituary.",
            identity="High confidence from the distinctive name plus an explicit Navy, OSS, and employer chronology in independent reputable sources.",
            temporal="The sources distinguish prewar General Mills employment from Navy service and OSS assignment.",
            quality="A_direct_official",
            confidence="high",
            publication="published",
            notes="The Box 818 file remains the direct personnel-file confirmation target.",
            source_links=[
                {"source_key": INDEX, "locator_override": "PDF page 491 row 32; Box 818"},
                {"source_key": EISENHOWER, "locator_override": "Scope and Content Note, PDF physical page 2"},
                {"source_key": ABBOTT_OBIT, "locator_override": "Obituary paragraph 3"},
            ],
        ),
        make_claim(
            key="immediate-abbott-washburn-navy-b1001",
            row=32,
            claim_type="immediate_pre_oss_affiliation",
            text="Abbott Washburn's immediate documented institutional pathway into OSS was through United States Navy service.",
            paraphrase="The obituary states that he served in the Navy during World War II and was assigned to OSS in Europe.",
            identity="High confidence from the distinctive exact name and corroborated General Mills chronology.",
            temporal="Explicitly immediate at the institutional level because OSS is described as a Navy assignment; no narrower unit or date is supplied.",
            quality="C_reputable_contemporary_or_scholarly",
            confidence="high",
            publication="published",
            notes="Military service, not civilian employment.",
            source_links=[
                {"source_key": ABBOTT_OBIT, "excerpt_override": "He served in the Navy during World War II and was assigned to the Office of Strategic Services in Europe."},
            ],
            affiliation_key="abbott-washburn-navy-b1001",
        ),
        make_claim(
            key="last-civilian-abbott-washburn-general-mills-b1001",
            row=32,
            claim_type="last_civilian_pre_service",
            text="Abbott Washburn's last documented civilian employer before World War II service was General Mills in Minneapolis.",
            paraphrase="The Eisenhower Library finding aid dates his General Mills work from 1937 and describes World War II service as the sole interruption before 1950.",
            identity="High confidence from the distinctive exact name and corroborating Navy-to-OSS obituary chronology.",
            temporal="Strongly date-bounded as employment immediately before and after the wartime interruption.",
            quality="A_direct_official",
            confidence="high",
            publication="published",
            notes="Distinguished from the immediate pre-OSS Navy assignment.",
            source_links=[
                {"source_key": EISENHOWER, "excerpt_override": "Except for a brief service in World War II he worked at General Mills until 1950"},
                {"source_key": ABBOTT_OBIT, "support_type": "context_only", "locator_override": "Obituary paragraphs 3-4"},
            ],
            affiliation_key="abbott-washburn-general-mills-b1001",
        ),
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
    value.update(overrides)
    return value


def person_updates() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, reason in UNRESOLVED.items():
        category: dict[str, object] = {}
        if row in PRINTED_CATEGORIES:
            category_name, officer = PRINTED_CATEGORIES[row]
            category = {
                "personnel_category": category_name,
                "commissioned_officer": officer,
                "allied_or_foreign_personnel": False,
            }
        values.append(base_update(
            row,
            identity_status="unresolved",
            identity_evidence=f"The visually verified page 491 row preserves {PEOPLE[row][1]}, its printed rank or note, and archival context. {reason}",
            research_status="requires_archival_review",
            next_action=f"Review the indexed Box {816 if row <= 2 else 817 if row <= 30 else 818} personnel file for corroborating identifiers, the immediate pre-OSS affiliation, and the last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}",
            **category,
        ))
    for row, item in ARMY_OCCUPATIONS.items():
        values.append(base_update(
            row,
            identity_status="confirmed",
            identity_evidence="The exact indexed name and a nonshared protected identifier connect the row to the reviewed official Army record.",
            personnel_category="enlisted_army_personnel",
            commissioned_officer=False,
            allied_or_foreign_personnel=False,
            research_status="occupation_only_found",
            next_action=f"Review the indexed Box {817 if row <= 20 else 818} personnel file to identify any named employer or school behind the broad {item['occupation']} category and establish the Army-to-OSS chronology.",
            nara_catalog_id="1263923",
        ))
    values.extend([
        base_update(
            1,
            identity_status="conflicting",
            identity_evidence="A protected identifier connects the index row to an Army record for Stephan J. Wargo, but the materially different given-name spelling remains unresolved.",
            research_status="conflicting_sources",
            next_action="Review the indexed Box 816 personnel file to resolve Stephen versus Stephan before transferring Army occupation, grade, or chronology evidence.",
            nara_catalog_id="1263923",
        ),
        base_update(
            7,
            identity_status="high_confidence",
            identity_evidence="The exact name, civilian status, and direct OSS chronology align between the index and May 1944 official board proceedings.",
            personnel_category="civilian_professional_or_administrative_grade",
            commissioned_officer=False,
            allied_or_foreign_personnel=False,
            research_status="occupation_only_found",
            next_action="Review the indexed Box 817 personnel file to identify the employer or publication behind the reporter-and-writer occupation and confirm whether it was immediately pre-OSS.",
        ),
        base_update(
            9,
            identity_status="high_confidence",
            identity_evidence="The full middle-name expansion, 390th Bombardment Group service, December 1944 OSS detail, and later SSU/CIG legal role align across an official CIA history and obituary.",
            personnel_category="commissioned_army_officer",
            commissioned_officer=True,
            allied_or_foreign_personnel=False,
            research_status="verified_employer_found",
            next_action="Review the indexed Box 817 personnel file to confirm the published Union Trust and 390th Bombardment Group chronology and capture any more precise OSS assignment dates.",
        ),
        base_update(
            13,
            identity_status="high_confidence",
            identity_evidence="The distinctive exact name aligns with an official Copyright Office biography documenting Harvard and War Production Board service.",
            research_status="requires_archival_review",
            next_action="Review the indexed Box 817 personnel file to determine whether Harvard was the last civilian employer and where the War Production Board role falls relative to OSS service.",
        ),
        base_update(
            14,
            identity_status="high_confidence",
            identity_evidence="The uncommon indexed form aligns exactly with the University of Chicago archival name and a 1935-1959 professorial chronology.",
            research_status="documented_prewar_employer_found",
            next_action="Review the indexed Box 817 personnel file to determine whether University of Chicago was the immediate predecessor or last civilian employer before OSS service.",
        ),
        base_update(
            24,
            identity_status="high_confidence",
            identity_evidence="The rare exact name and suffix align with a Princeton institutional memorial documenting relevant Army service and the rank of major.",
            personnel_category="commissioned_army_officer",
            commissioned_officer=True,
            allied_or_foreign_personnel=False,
            research_status="requires_archival_review",
            next_action="Review the indexed Box 817 personnel file to date Northam Warren Jr.'s Army assignments, establish the OSS transition, and identify his last civilian employer before service.",
        ),
        base_update(
            32,
            identity_status="high_confidence",
            identity_evidence="The distinctive exact name, General Mills chronology, Navy service, and OSS assignment in Europe align across a NARA presidential-library finding aid and a reputable obituary.",
            research_status="verified_employer_found",
            next_action="Review the indexed Box 818 personnel file to confirm the General Mills-to-Navy-to-OSS chronology, Navy unit, rank, and more precise dates.",
        ),
    ])
    if len(values) != len(PEOPLE):
        raise RuntimeError(f"Expected {len(PEOPLE)} person updates, generated {len(values)}")
    return values


def research_attempts() -> list[dict[str, object]]:
    attempts: list[dict[str, object]] = []
    strong_rows = {7, 9, 13, 14, 24, 32}
    candidate_rejected = {5, 10, 18, 21, 23, 35, 43, 44, 45}
    for row, (person_id, name) in PEOPLE.items():
        if row in ARMY_OCCUPATIONS:
            outcome, reviewed, rejected = "source_reviewed", 9, 5
            note = f"A reviewed protected-identifier Army bridge supports identity and a qualified {ARMY_OCCUPATIONS[row]['occupation']} category at Army entry; no named employer, workplace, school, or OSS-transfer date is supplied."
        elif row == 1:
            outcome, reviewed, rejected = "candidate_rejected", 9, 6
            note = "The protected identifier aligns, but the Army given name Stephan materially differs from indexed Stephen; no Army occupation or chronology was transferred."
        elif row in strong_rows:
            outcome, reviewed, rejected = "source_reviewed", 12, 6
            note = {
                7: "Official OSS board proceedings support a high-confidence identity and reporter-and-writer occupation, but no named employer.",
                9: "An official CIA history and detailed obituary support Union Trust Company as the last civilian employer and the 390th Bombardment Group as the immediate pre-OSS assignment.",
                13: "An official Copyright Office biography supports Harvard and War Production Board affiliations, but their exact sequence relative to OSS remains unresolved.",
                14: "A University of Chicago archival record supports documented prewar university employment; immediate-predecessor status remains unproven.",
                24: "A Princeton memorial supports high-confidence Army service identity, but supplies no dates or direct OSS transition.",
                32: "A NARA presidential-library finding aid and obituary support General Mills as the last civilian employer and Navy service as the immediate OSS pathway.",
            }[row]
        elif row in candidate_rejected:
            outcome, reviewed, rejected = "candidate_rejected", 8, 7
            note = UNRESOLVED[row]
        else:
            outcome, reviewed, rejected = "no_result", 7, 6
            note = UNRESOLVED[row]
        box = 816 if row <= 2 else 817 if row <= 30 else 818
        attempts.append({
            "key": f"page491-row{row}-{slug(name)}-b1001",
            "person_id": person_id,
            "source_adapter": "manual_staged_protocol",
            "query_text": f"{name}; NARA OSS index context; CIA Reading Room exact-name domain check; Library of Congress collection check; exact-name and meaningful spelling, initial, suffix, punctuation, and transliteration variants; OSS, rank, branch, assignment and identifier clues; employer and occupation 1940; obituary, institutional, newspaper, directory and archival searches; indexed Box {box}; protected identifiers used only in private official-record comparison",
            "query_variant_type": "staged_identity_employment_archival_protocol_batch_1001",
            "started_at": "2026-11-03T18:10:00Z",
            "completed_at": "2026-11-03T19:05:00Z",
            "outcome": outcome,
            "sources_reviewed": reviewed,
            "candidate_sources_rejected": rejected,
            "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, postwar-only leads, and sources without an OSS, protected-identifier, rank, unit, or personnel-file bridge were rejected. Northam Warren's postwar Chesebrough-Ponds role was not recast as prewar work. Historical Army categories were not converted into named employers or schools.",
            "research_notes": f"{note} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain, and archival searches were checked as applicable. Official CIA Reading Room and Library of Congress collection discovery checks produced no additional publishable employer source for the unresolved rows. The NARA index page was text-extracted, rendered, and visually checked. Official Army bulk data, technical documentation, and code documentation were inspected locally. Hoover and CIA document interfaces were reviewed without bypassing blocked direct-download behavior. No search-result snippet was used as sole final evidence, and no authenticated NARA Catalog API call was made.",
            "next_action": f"Review the indexed Box {box} personnel file for corroborating identifiers, the immediate pre-OSS affiliation, and the last civilian employer before wartime service.",
            "attempt_number": 1,
            "research_agent_version": "before-oss-b1001-v1",
        })
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-1001-v1",
        "reviewer": "Before OSS Batch 1001 evidence review",
        "sources": sources(),
        "organizations": organizations(),
        "affiliations": affiliations(),
        "claims": claims(),
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }
    EvidenceBundle.model_validate(bundle)
    OUTPUT.write_text(
        json.dumps(bundle, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
