#!/usr/bin/env python3
"""Generate the reviewed Batch 945 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page463-kenneth-s-templeton-to-william-b-terrell-"
    "review_batch-945_2026-10-28.json"
)

INDEX = "nara-index-b945"
ARMY = "army-bulk-b945"
TECH = "army-tech-b945"
CODES = "army-codes-b945"
TRUMAN_TENENBAUM = "truman-library-tenenbaum-b945"
CAMBRIDGE_TENENBAUM = "cambridge-tenenbaum-excerpt-b945"
HSOZ_TENENBAUM = "hsozkult-tenenbaum-review-b945"
FBI_TENNEY = "fbi-donovan-tenney-b945"
CIA_TENNEY = "cia-shameful-years-tenney-b945"
YALE_VENONA = "yale-venona-tenney-b945"
CORNELL_ILGWU = "cornell-ilgwu-research-b945"
UMN_1938 = "umn-regents-1938-terhaar-b945"
UMN_1939 = "umn-regents-1939-terhaar-b945"

YALE = "yale-university-b945"
ARMY_AIR_FORCES = "army-air-forces-b945"
ILGWU = "ilgwu-b945"
SHORT_WAVE = "short-wave-research-b945"
UNIVERSITY_MINNESOTA = "university-minnesota-b945"


PEOPLE = {
    1: ("38fea3f1-6703-5843-a83a-e9c248895241", "Kenneth S Templeton"),
    2: ("10858a8f-fd6f-5c5d-92ad-fe20908f14c0", "Richard Temposky"),
    3: ("acb250e2-712f-5117-b4e7-6e89a2978fa2", "Edward A Tenenbaum"),
    4: ("800216a6-97b8-593d-b6ea-f339050a035c", "Gerritt J TenHoor"),
    5: ("c07e7248-2a98-5259-8bd3-469c0015de5f", "Calvin Tenne"),
    6: ("136f7d9d-c513-5977-bd5b-81d03c93f2b9", "George E Tenny"),
    7: ("9c06eb20-7990-5b72-bc6c-4b65c48a9c2b", "Helen B Tenny"),
    8: ("7cb36e99-9fc4-5677-9211-6250c6e69a2e", "Lloyd S Tenny"),
    9: ("d8d95892-3f69-510d-aec4-432a43575061", "William W Tennyson"),
    10: ("265712f9-7f19-5589-8d6b-ceadd8044671", "Bertha H Teper"),
    11: ("fc4e3ffe-f90f-54c1-bd2d-8a12346960df", "Lazare Teper"),
    12: ("44a21b4e-d171-557b-bab6-252f31ce8f6e", "Lazare Teper"),
    13: ("ff8e4a0a-f694-50e0-be9f-98a722feae73", "Douglas Tepper"),
    14: ("e8090daa-f5cd-53ad-9efb-4d5b3c5b0af6", "Gabriel R Terek"),
    15: ("23f7873e-68ac-5360-992b-988999c9e6c4", "Ethel M Terhaar"),
    16: ("22eb9e85-2d7a-53d9-94a0-63b762e5a63f", "Frank J Terhorst"),
    17: ("3063897d-55a8-59e6-a61a-216167e64d9a", "Virginia H Terhune"),
    18: ("9f4ca781-6b4d-5eba-b165-b1e7c1cc4612", "Dorothy N Terney"),
    19: ("6de3f649-54a5-5737-87b9-2f0a1bcf5e20", "Anneilo A Terracciano"),
    20: ("43bd4912-1519-56ad-93b0-5d990d61e757", "Edwin M Terrell"),
    21: ("b008145c-0a58-5d63-8cb2-b26439f13726", "Virgil E Terrell"),
    22: ("f238d457-78c8-5960-985c-b84c7b7586e0", "Walter L Terrell"),
    23: ("72386b20-f9db-5aa6-80f2-48aad95e24ce", "William B Terrell"),
}


ARMY_OCCUPATIONS = [
    {
        "row": 11,
        "date": "1943-10-21",
        "code": "039",
        "occupation": "Professional occupations, n.e.c.",
        "public_occupation": "professional occupation, not elsewhere classified",
        "locator": "PDF physical page 171; historical category 0-39",
    },
    {
        "row": 14,
        "date": "1943-10-04",
        "code": "513",
        "occupation": "Occupations in the manufacture of miscellaneous products",
        "public_occupation": "skilled occupation in the manufacture of miscellaneous products",
        "locator": "PDF physical page 174; historical category 5-13",
    },
    {
        "row": 19,
        "date": "1943-09-03",
        "code": "688",
        "occupation": "Occupations in mechanical treatment of metals, n.e.c.",
        "public_occupation": "semiskilled occupation in mechanical treatment of metals",
        "locator": "PDF physical page 174; historical category 6-88",
    },
    {
        "row": 23,
        "date": "1942-09-22",
        "code": "031",
        "occupation": "Teachers (secondary school) and principals",
        "public_occupation": "secondary-school teacher or principal",
        "locator": "PDF physical page 171; historical category 0-31",
    },
]


UNRESOLVED = {
    1: "The common name and middle initial did not yield a defensible OSS, employer, occupation or Box 768 identity bridge.",
    2: "A distinctive surname produced genealogy and yearbook leads only; none established OSS service or a pre-OSS employer.",
    4: "Exact-name and spacing variants found no reliable wartime, employer, institutional or OSS bridge.",
    5: "Exact-name searches found no reliable employer, occupation, institutional or wartime identity bridge.",
    6: "Same-name public records lacked the middle initial, OSS context and a Box 769 or protected-identifier bridge.",
    8: "Exact-name searches found no reliable OSS, employer, occupation or archival identity bridge.",
    9: "The common name and middle initial produced unbridged namesakes but no reliable OSS or pre-OSS affiliation evidence.",
    10: "Exact-name searches found no reliable wartime identity, employer, occupation or institutional bridge.",
    13: "Exact-name searches found no defensible OSS, employer, occupation or archival identity bridge.",
    16: "Same-name public records lacked a corroborating middle initial, OSS assignment or Box 769 bridge.",
    17: "Exact-name searches found no reliable pre-OSS employer, occupation, institution or OSS identity bridge.",
    18: "Exact-name and variant searches found no reliable wartime identity or pre-OSS affiliation evidence.",
    20: "The common name and middle initial produced unbridged namesakes but no defensible OSS or employer match.",
    21: "Exact-name searches found no reliable employer, occupation, institution or wartime identity bridge.",
    22: "The common name and middle initial produced unbridged namesakes but no reliable OSS or pre-OSS affiliation evidence.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 768-769",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 463, rows 1-23; checked against layout-preserving text and a 300 dpi page render",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. The two Lazare Teper rows remain separate entities. Full protected identifiers remain private. Henry W. Terrett at row 24 was checked as the next boundary.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; four reviewed Batch 945 candidates; protected identifiers withheld",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "No raw bulk row or full protected identifier is retained in public assets. Four exact-name identities were accepted; historical occupation codes identify neither employers nor workplaces.",
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
            "locator": "PDF physical pages 171 and 174; reviewed historical categories 0-31, 0-39, 5-13 and 6-88",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Both relevant pages were rendered at 220 dpi and visually inspected. Historical occupation labels are qualified and never converted into named employers.",
        },
        {
            "key": TRUMAN_TENENBAUM,
            "stable_url": "https://www.trumanlibrary.gov/library/personal-papers/edward-tenenbaum-papers",
            "archival_identifier": "Edward A. Tenenbaum Papers, Harry S. Truman Presidential Library",
            "title": "Tenenbaum, Edward A. Papers",
            "author_creator": "Harry S. Truman Presidential Library and Museum",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "updated 2019",
            "locator": "Biographical Sketch, entries for 1921 and 1942-1947",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "Edward A. Tenenbaum Papers, 1941-1959",
            "rights_notes": "The official sketch supplies Edward Adam Tenenbaum, Yale B.A. in 1942 and U.S. Army Air Forces service from 1942 to 1947.",
        },
        {
            "key": CAMBRIDGE_TENENBAUM,
            "stable_url": "https://assets.cambridge.org/97810094/92812/excerpt/9781009492812_excerpt.pdf",
            "archival_identifier": "ISBN 978-1-009-49281-2",
            "title": "Edward A. Tenenbaum and the Deutschmark: How an American Jew Became the Father of Germany's Postwar Economic Revival",
            "author_creator": "Carl-Ludwig Holtfrerich",
            "repository_publisher": "Cambridge University Press & Assessment",
            "publication_record_date": "2024",
            "locator": "Official excerpt, introduction, printed page 2; PDF physical page 2",
            "access_date": "2026-10-28",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Studies in New Economic Thinking",
            "rights_notes": "The official publisher excerpt was rendered at 220 dpi and visually inspected; it explicitly dates Tenenbaum's OSS employment from June 1942.",
        },
        {
            "key": HSOZ_TENENBAUM,
            "stable_url": "https://www.hsozkult.de/publicationreview/id/reb-144904",
            "archival_identifier": "H-Soz-Kult review reb-144904",
            "title": "Review of C.-L. Holtfrerich: Edward A. Tenenbaum and the Deutschmark",
            "author_creator": "Stefan Grüner",
            "repository_publisher": "H-Soz-Kult",
            "publication_record_date": "2026-02-12",
            "locator": "Review discussion of education, Army and OSS chronology",
            "access_date": "2026-10-28",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "H-Soz-Kult publication reviews",
            "rights_notes": "The scholarly review identifies Tenenbaum as a U.S. officer and later lieutenant, but it is used only to classify documented military status, not to infer an exact OSS transfer path.",
        },
        {
            "key": FBI_TENNEY,
            "stable_url": "https://vault.fbi.gov/William%20J%20Donovan%20/William%20J%20Donovan%20Part%2002",
            "archival_identifier": "William J. Donovan FBI file, Part 2 of 7",
            "title": "William J. Donovan Part 2 of 7",
            "author_creator": "Federal Bureau of Investigation",
            "repository_publisher": "Federal Bureau of Investigation Vault",
            "publication_record_date": "records compiled 1946; later released under FOIA",
            "locator": "PDF page 15; Helen B. Tenney paragraph",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "William J. Donovan FBI file",
            "rights_notes": "Used only for the exact Helen B. Tenney name and documented OSS Spanish Division and Balkans assignments. Unrelated allegations and sensitive personal material are excluded.",
        },
        {
            "key": CIA_TENNEY,
            "stable_url": "https://www.cia.gov/readingroom/docs/CIA-RDP60-00442R000100050013-5.pdf",
            "archival_identifier": "CIA-RDP60-00442R000100050013-5",
            "title": "The Shameful Years: Thirty Years of Soviet Espionage in the United States",
            "author_creator": "United States Congress; released by Central Intelligence Agency",
            "repository_publisher": "Central Intelligence Agency Reading Room",
            "publication_record_date": "approved for release 2003-03-25",
            "locator": "Printed page 60; list entry for Helen Tenney",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "CIA Freedom of Information Act Electronic Reading Room",
            "rights_notes": "Used only to corroborate Helen Tenney's documented OSS Spanish Division assignment; allegations outside project scope are not republished.",
        },
        {
            "key": YALE_VENONA,
            "stable_url": "https://yalebooks.yale.edu/book/9780300084627/venona/",
            "archival_identifier": "ISBN 978-0-300-08462-7",
            "title": "Venona: Decoding Soviet Espionage in America",
            "author_creator": "John Earl Haynes and Harvey Klehr",
            "repository_publisher": "Yale University Press",
            "publication_record_date": "1999; paperback 2000",
            "locator": "The Golos-Bentley Network, printed page 112",
            "access_date": "2026-10-28",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Yale University Press books",
            "rights_notes": "The scholarly source documents 1942 employment at Short Wave Research, its Office of War Information contract and the subsequent move into OSS. Only a short supporting excerpt is retained.",
        },
        {
            "key": CORNELL_ILGWU,
            "stable_url": "https://archives.library.cornell.edu/repositories/4/resources/10667",
            "archival_identifier": "ILGWU Research Department Records, 5780/168",
            "title": "ILGWU Research Department Records",
            "author_creator": "Kheel Center for Labor-Management Documentation & Archives",
            "repository_publisher": "Cornell University Library",
            "publication_record_date": "collection dates 1890-1995",
            "locator": "Biographical / Historical note; Lazare Teper paragraph",
            "access_date": "2026-10-28",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "International Ladies' Garment Workers' Union records",
            "rights_notes": "The current Cornell finding aid identifies Teper as founding director from 1937 to 1980. It does not establish whether wartime military or OSS service interrupted active union duties.",
        },
        {
            "key": UMN_1938,
            "stable_url": "https://conservancy.umn.edu/server/api/core/bitstreams/cd9a8cf0-84e0-4f48-a668-8bff8da82ee0/content",
            "archival_identifier": "University of Minnesota Board of Regents, Year 1937-38, No. 13",
            "title": "Board of Regents Agricultural Committee Minutes, January 28, 1938",
            "author_creator": "University of Minnesota Board of Regents",
            "repository_publisher": "University of Minnesota Libraries",
            "publication_record_date": "1938-01-28",
            "locator": "Printed page 138; PDF physical page 2; appointment list",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "University of Minnesota Board of Regents minutes",
            "rights_notes": "The page was rendered at 220 dpi and visually inspected. It gives Ethel M. Terhaar's exact name, role, unit and appointment dates.",
        },
        {
            "key": UMN_1939,
            "stable_url": "https://conservancy.umn.edu/server/api/core/bitstreams/67f82e9b-0041-4bfc-b923-b6b750a9d669/content",
            "archival_identifier": "University of Minnesota Board of Regents, Year 1938-39, No. 62",
            "title": "Board of Regents Budget Committee Minutes, June 16, 1939",
            "author_creator": "University of Minnesota Board of Regents",
            "repository_publisher": "University of Minnesota Libraries",
            "publication_record_date": "1939-06-16",
            "locator": "1939-40 budget, printed page 681; PDF physical page 21; Department of Agriculture administration",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "University of Minnesota Board of Regents minutes",
            "rights_notes": "The page was rendered at 220 dpi and visually inspected. It confirms Ethel Terhaar's continuing clerk-stenographer listing in the 1939-40 budget.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": YALE,
            "organization_id": "918dedde-f9d1-5db1-8304-5c218a06b9b5",
            "canonical_name": "Yale University",
            "historical_name": "Yale University",
            "aliases": ["Yale"],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "New Haven",
            "state_or_region": "Connecticut",
            "country": "United States",
            "normalization_notes": "Existing canonical employer organization reused; distinct from the separate historical Yale College row in the database.",
        },
        {
            "key": ARMY_AIR_FORCES,
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
            "key": ILGWU,
            "organization_id": "b8b51bae-7552-5eff-986b-85c69667730f",
            "canonical_name": "International Ladies' Garment Workers' Union",
            "historical_name": "International Ladies' Garment Workers' Union",
            "aliases": ["ILGWU"],
            "organization_type": "labor union",
            "sector": "labor_nonprofit_and_religion",
            "city": "New York",
            "state_or_region": "New York",
            "country": "United States",
            "active_dates": "1900-1995",
            "normalization_notes": "The historical union name is retained; no successor union is substituted in the employment claim.",
        },
        {
            "key": SHORT_WAVE,
            "canonical_name": "Short Wave Research, Inc.",
            "historical_name": "Short Wave Research",
            "aliases": ["Short Wave Research"],
            "organization_type": "wartime communications contractor",
            "sector": "journalism_and_media",
            "city": "New York",
            "state_or_region": "New York",
            "country": "United States",
            "active_dates": "active in 1942; closure date not specified in the admitted source",
            "normalization_notes": "The scholarly source describes a firm under contract to the Office of War Information; no modern successor is assigned.",
        },
        {
            "key": UNIVERSITY_MINNESOTA,
            "organization_id": "a7d41a87-9f88-51a4-9eb3-fb8de0ce10a1",
            "canonical_name": "University of Minnesota",
            "historical_name": "University of Minnesota",
            "aliases": [],
            "organization_type": "public university",
            "sector": "academia_and_research",
            "city": "Minneapolis and Saint Paul",
            "state_or_region": "Minnesota",
            "country": "United States",
            "normalization_notes": "Golda Stegner's staff role is distinct from her later student listing.",
        },
    ]


def army_affiliation(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    name = PEOPLE[row][1]
    return {
        "key": f"{slug(name)}-occupation-b945",
        "person_id": PEOPLE[row][0],
        "occupation": item["public_occupation"],
        "relationship_type": "employment",
        "end_date": item["date"],
        "date_precision": f"Historical civilian-occupation code {item['code']} was recorded at Army entry on {item['date']}; no employer, workplace or OSS-transfer date is named.",
        "country": "United States",
        "immediate_pre_oss": False,
        "last_civilian_pre_service": False,
        "pre_oss_temporal_basis": "strongly_date_bounded",
        "identity_confidence": "high_confidence",
        "claim_confidence": "medium",
        "source_quality": "A_direct_official",
        "publication_status": "publish_qualified",
        "research_notes": "The historical category is not converted into a named employer, workplace, immediate affiliation or exact modern job title.",
    }


def affiliations() -> list[dict[str, object]]:
    values = [army_affiliation(item) for item in ARMY_OCCUPATIONS]
    values.extend(
        [
            {
                "key": "edward-tenenbaum-yale-student-b945",
                "person_id": PEOPLE[3][0],
                "organization_key": YALE,
                "organization_name_as_found": "Yale University",
                "role_title": "B.A. student",
                "relationship_type": "student",
                "end_date": "1942",
                "date_precision": "The Truman Library dates the B.A. to 1942; the Cambridge excerpt dates OSS employment from June 1942, but neither source gives the graduation day or excludes an intervening Army assignment.",
                "city": "New Haven",
                "state_or_region": "Connecticut",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "A_direct_official",
                "publication_status": "published",
                "research_notes": "Yale is a documented student institution, not an employer. The exact Army-to-OSS transfer sequence remains unresolved.",
            },
            {
                "key": "edward-tenenbaum-army-air-forces-b945",
                "person_id": PEOPLE[3][0],
                "organization_key": ARMY_AIR_FORCES,
                "organization_name_as_found": "U.S. Army Air Forces",
                "role_title": "military service; later documented as a lieutenant",
                "relationship_type": "military_assignment",
                "start_date": "1942",
                "end_date": "1947",
                "date_precision": "The Truman Library gives 1942-1947 Army Air Forces service; the scholarly review documents commissioned status, but the exact date and unit immediately before June 1942 OSS employment are not stated.",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "temporal_relation_uncertain",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "A_direct_official",
                "publication_status": "published",
                "research_notes": "Military service overlaps the documented OSS period; it is not labeled the immediate predecessor without a direct transfer record.",
            },
            {
                "key": "helen-tenney-short-wave-research-b945",
                "person_id": PEOPLE[7][0],
                "organization_key": SHORT_WAVE,
                "organization_name_as_found": "Short Wave Research",
                "role_title": "foreign-language recruitment and related wartime communications work",
                "relationship_type": "employment",
                "start_date": "1942",
                "end_date": "1942",
                "date_precision": "The scholarly account places Tenney at the firm in 1942, states that it disbanded, and then places her in the OSS Spanish section later that year.",
                "city": "New York",
                "state_or_region": "New York",
                "country": "United States",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "explicit_immediate",
                "identity_confidence": "probable",
                "claim_confidence": "medium",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "publish_qualified",
                "research_notes": "The claim is visibly qualified because the index spells the surname Tenny and no protected identifier or personnel-file bridge has yet confirmed the one-letter correction.",
            },
            {
                "key": "lazare-teper-ilgwu-b945",
                "person_id": PEOPLE[11][0],
                "organization_key": ILGWU,
                "organization_name_as_found": "ILGWU's Research Department",
                "role_title": "founding director of the Research Department",
                "relationship_type": "employment",
                "start_date": "1937",
                "end_date": "1980",
                "date_precision": "Cornell's finding aid gives the directorship as 1937-1980; it does not identify leave periods or the precise relationship to 1943 Army entry and OSS service.",
                "city": "New York",
                "state_or_region": "New York",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "The protected Army identity bridge applies only to page 463 row 11. The duplicate-name row 12 remains separate and receives none of this evidence.",
            },
            {
                "key": "ethel-terhaar-university-minnesota-b945",
                "person_id": PEOPLE[15][0],
                "organization_key": UNIVERSITY_MINNESOTA,
                "organization_name_as_found": "University Farm; Department of Agriculture",
                "role_title": "clerk-stenographer",
                "relationship_type": "employment",
                "start_date": "1937-12-16",
                "end_date": "1940",
                "date_precision": "The appointment runs through June 30, 1938 and the name and role recur in the approved 1939-40 budget; the exact separation date is not stated.",
                "city": "Saint Paul",
                "state_or_region": "Minnesota",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "probable",
                "claim_confidence": "medium",
                "source_quality": "A_direct_official",
                "publication_status": "publish_qualified",
                "research_notes": "The rare exact name and middle initial support a probable match, but no OSS or Box 769 source yet supplies a second identifier or proves immediate chronology.",
            },
        ]
    )
    return values


def claim(
    row: int,
    key: str,
    claim_type: str,
    claim_text: str,
    evidence_paraphrase: str,
    identity: str,
    temporal: str,
    source_quality: str,
    confidence: str,
    source_links: list[dict[str, str]],
    notes: str,
    affiliation_key: str | None = None,
    publication_status: str | None = None,
) -> dict[str, object]:
    return {
        "key": key,
        "person_id": PEOPLE[row][0],
        "affiliation_key": affiliation_key,
        "claim_type": claim_type,
        "claim_text": claim_text,
        "evidence_paraphrase": evidence_paraphrase,
        "identity_match_assessment": identity,
        "temporal_assessment": temporal,
        "source_quality": source_quality,
        "claim_confidence": confidence,
        "publication_status": publication_status
        or ("published" if confidence in {"confirmed", "high"} else "publish_qualified"),
        "match_notes": notes,
        "sources": source_links,
    }


def army_claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for item in ARMY_OCCUPATIONS:
        row = int(item["row"])
        name = PEOPLE[row][1]
        values.append(
            claim(
                row,
                f"identity-{slug(name)}-army-b945",
                "identity",
                f"Indexed {name} is a high-confidence match to the reviewed official Army entry.",
                "A nonshared protected identifier and exact full-name agreement connect the visually checked index row to the official Army bulk record.",
                "High confidence from a private unique identifier plus exact name agreement; the full identifier remains private.",
                "Identity evidence only; the Army entry does not itself establish an OSS transfer date.",
                "A_direct_official",
                "high",
                [
                    {"source_key": INDEX, "locator_override": f"PDF page 463 row {row}"},
                    {"source_key": ARMY, "locator_override": "Reviewed bulk row; protected identifier withheld"},
                    {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46"},
                ],
                "The review accepts identity only for the matching source row and does not expose the protected identifier.",
            )
        )
        values.append(
            claim(
                row,
                f"occupation-{slug(name)}-army-b945",
                "occupation",
                f"At Army entry on {item['date']}, the record coded {name}'s civilian occupation as {item['occupation']}",
                f"The official Army record contains civilian-occupation code {item['code']}; NARA's historical code list expands it to {item['occupation']}",
                "High-confidence identity from the accepted protected-identifier bridge and exact name agreement.",
                "The code was recorded at Army entry and is date-bounded, but it identifies no employer, workplace or immediate OSS predecessor.",
                "A_direct_official",
                "medium",
                [
                    {"source_key": ARMY, "locator_override": "Reviewed bulk row; protected identifier withheld"},
                    {"source_key": CODES, "locator_override": str(item["locator"]), "excerpt_override": str(item["occupation"])},
                    {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46"},
                ],
                "The historical category is published as qualified occupation-only evidence and is excluded from named-employer analytics.",
                f"{slug(name)}-occupation-b945",
                "publish_qualified",
            )
        )
    return values


def substantive_claims() -> list[dict[str, object]]:
    return [
        claim(
            3,
            "identity-edward-tenenbaum-b945",
            "identity",
            "Indexed Edward A. Tenenbaum is a high-confidence match to economist and OSS officer Edward Adam Tenenbaum.",
            "The rare exact indexed name aligns with the Truman Library biography and the Cambridge scholarly account that dates his OSS employment from June 1942.",
            "High confidence from a distinctive exact name, documented 1942 Yale and military chronology, and an explicit scholarly OSS statement.",
            "Identity is established; the exact sequence between Yale, Army Air Forces and OSS still requires the indexed file.",
            "A_direct_official",
            "high",
            [
                {"source_key": INDEX, "locator_override": "PDF page 463 row 3"},
                {"source_key": TRUMAN_TENENBAUM, "locator_override": "Biographical Sketch"},
                {"source_key": CAMBRIDGE_TENENBAUM, "locator_override": "Introduction, printed page 2", "excerpt_override": "Tenenbaum was employed from June 1942"},
            ],
            "Edward Adam Tenenbaum is preserved as a documented full-name variant; no postwar employer is substituted for the pre-OSS question.",
        ),
        claim(
            3,
            "prewar-edward-tenenbaum-yale-b945",
            "other_pre_oss_affiliation",
            "Edward A. Tenenbaum received a B.A. from Yale University in 1942 before his documented June 1942 OSS employment.",
            "The Truman Library dates the Yale B.A. to 1942, and the Cambridge excerpt independently dates OSS employment from June 1942.",
            "High-confidence identity from the distinctive exact name and direct OSS chronology.",
            "Strongly date-bounded student status, not employment; the sources do not prove that Yale was the immediate predecessor rather than an Army assignment.",
            "A_direct_official",
            "high",
            [
                {"source_key": TRUMAN_TENENBAUM, "locator_override": "Biographical Sketch, 1942", "excerpt_override": "B.A., Yale University"},
                {"source_key": CAMBRIDGE_TENENBAUM, "locator_override": "Introduction, printed page 2", "excerpt_override": "Tenenbaum was employed from June 1942"},
            ],
            "Yale is classified as a student institution and is excluded from employer analytics.",
            "edward-tenenbaum-yale-student-b945",
        ),
        claim(
            3,
            "wartime-edward-tenenbaum-army-air-forces-b945",
            "other_pre_oss_affiliation",
            "Edward A. Tenenbaum served in the U.S. Army Air Forces from 1942 to 1947 while his OSS employment began in June 1942.",
            "The Truman Library supplies the Army Air Forces dates, Cambridge supplies the OSS start month, and the scholarly review documents commissioned status.",
            "High-confidence identity from the distinctive exact name and mutually reinforcing official and scholarly chronology.",
            "The military and OSS periods overlap; the sources do not identify the exact unit or transfer immediately before OSS.",
            "A_direct_official",
            "high",
            [
                {"source_key": TRUMAN_TENENBAUM, "locator_override": "Biographical Sketch, 1942-1947", "excerpt_override": "Served in U.S. Army Air Forces, U.S. and Europe"},
                {"source_key": CAMBRIDGE_TENENBAUM, "locator_override": "Introduction, printed page 2"},
                {"source_key": HSOZ_TENENBAUM, "support_type": "context_only", "locator_override": "Review discussion of wartime service and lieutenant status"},
            ],
            "The assignment is not labeled immediate pre-OSS until the personnel file resolves the 1942 sequence.",
            "edward-tenenbaum-army-air-forces-b945",
        ),
        claim(
            7,
            "identity-helen-tenney-b945",
            "identity",
            "Indexed Helen B. Tenny is a probable match to Helen B. Tenney of the OSS Spanish Division and Balkans work.",
            "The FBI gives the exact first name and middle initial with a one-letter surname variant and direct OSS assignments; a CIA document independently lists Helen Tenney in the Spanish Division.",
            "Probable identity from the rare near-exact name and two official OSS references, but no protected identifier or personnel-file bridge.",
            "Identity only; the indexed file is still required to confirm that Tenny is a misspelling of Tenney.",
            "A_direct_official",
            "medium",
            [
                {"source_key": INDEX, "locator_override": "PDF page 463 row 7"},
                {"source_key": FBI_TENNEY, "locator_override": "PDF page 15; Helen B. Tenney paragraph", "excerpt_override": "HELEN B. TENNEY was first employed at the OSS, Spanish Division"},
                {"source_key": CIA_TENNEY, "locator_override": "Printed page 60", "excerpt_override": "Helen Tenney, Office of Strategic Services, Spanish Division"},
            ],
            "The one-letter surname difference remains visible. Unrelated allegations and sensitive personal details are excluded.",
            publication_status="publish_qualified",
        ),
        claim(
            7,
            "immediate-helen-tenney-short-wave-b945",
            "immediate_pre_oss_affiliation",
            "If the Tenny/Tenney identity is confirmed, Helen Tenney's immediate civilian employer before OSS was Short Wave Research in 1942.",
            "The Yale scholarly account states that she worked for the Office of War Information contractor in 1942, the firm disbanded, and she then entered the OSS Spanish section.",
            "Probable identity from the rare near-exact name and two official OSS references; the surname spelling still requires Box 769 confirmation.",
            "The scholarly source explicitly gives the employer-to-OSS sequence, but the identity link remains probable rather than confirmed.",
            "C_reputable_contemporary_or_scholarly",
            "medium",
            [
                {"source_key": YALE_VENONA, "locator_override": "The Golos-Bentley Network, printed page 112", "excerpt_override": "worked for Short Wave Research, a firm on contract for the Office of War Information"},
                {"source_key": FBI_TENNEY, "support_type": "context_only", "locator_override": "PDF page 15; OSS Spanish Division and Balkans work"},
                {"source_key": CIA_TENNEY, "support_type": "context_only", "locator_override": "Printed page 60"},
            ],
            "Published only as a qualified finding and excluded from default employer analytics because identity is probable, not high-confidence.",
            "helen-tenney-short-wave-research-b945",
            "publish_qualified",
        ),
        claim(
            11,
            "prewar-lazare-teper-ilgwu-b945",
            "other_pre_oss_affiliation",
            "Page 463 row 11 Lazare Teper was founding director of the ILGWU Research Department beginning in 1937.",
            "Cornell's current finding aid identifies Lazare Teper as founding director from 1937 to 1980; an accepted protected Army identifier bridges only row 11 to the exact-name wartime record.",
            "High-confidence identity for row 11 from a nonshared protected identifier and exact name agreement; row 12 remains separate.",
            "Documented prewar employment, but the long tenure statement does not establish wartime leave or the immediate sequence before OSS.",
            "B_authoritative_institutional",
            "high",
            [
                {"source_key": CORNELL_ILGWU, "locator_override": "Biographical / Historical note", "excerpt_override": "Lazare Teper was the founding director of the ILGWU's Research Department"},
                {"source_key": ARMY, "support_type": "context_only", "locator_override": "Reviewed row-11 bulk identity; protected identifier withheld"},
                {"source_key": INDEX, "support_type": "context_only", "locator_override": "PDF page 463 row 11"},
            ],
            "The employment evidence is not transferred to the separate row 12 entity and is not labeled immediate or last civilian before service.",
            "lazare-teper-ilgwu-b945",
        ),
        claim(
            15,
            "identity-ethel-terhaar-b945",
            "identity",
            "Indexed Ethel M. Terhaar is a probable match to the University of Minnesota clerk-stenographer documented from 1937 into the 1939-40 budget.",
            "The rare exact full name appears in the 1938 appointment record, and the same surname and role recur in the university's 1939-40 budget.",
            "Probable identity from the rare exact name and middle initial plus a consistent institutional chronology, but no OSS or protected-identifier bridge.",
            "Identity only; Box 769 is needed to confirm the Minnesota employee is the indexed person.",
            "A_direct_official",
            "medium",
            [
                {"source_key": INDEX, "locator_override": "PDF page 463 row 15"},
                {"source_key": UMN_1938, "locator_override": "Printed page 138; PDF physical page 2", "excerpt_override": "Ethel M Terhaar as Clerk Stenographer 1 Publications University Farm"},
                {"source_key": UMN_1939, "locator_override": "Printed page 681; PDF physical page 21", "excerpt_override": "Ethel Terhaar, Clerk-Steno"},
            ],
            "The claim remains qualified and the exact indexed spelling is preserved.",
            publication_status="publish_qualified",
        ),
        claim(
            15,
            "prewar-ethel-terhaar-minnesota-b945",
            "other_pre_oss_affiliation",
            "A probable identity match places Ethel M. Terhaar as a University of Minnesota clerk-stenographer from December 1937 into the 1939-40 budget.",
            "Two official Regents records document the appointment dates, Publications at University Farm role and later Department of Agriculture administration listing.",
            "Probable identity from the rare exact full name and consistent role; no direct OSS or Box 769 bridge has been found.",
            "Documented prewar employment only; the sources do not establish that Minnesota was the immediate or last civilian employer before OSS.",
            "A_direct_official",
            "medium",
            [
                {"source_key": UMN_1938, "locator_override": "Printed page 138; PDF physical page 2", "excerpt_override": "December 16, 1937 to June 30, 1938"},
                {"source_key": UMN_1939, "locator_override": "1939-40 budget, printed page 681; PDF physical page 21", "excerpt_override": "Ethel Terhaar, Clerk-Steno"},
            ],
            "Published only as a qualified earlier job and excluded from default employer analytics until identity reaches high confidence.",
            "ethel-terhaar-university-minnesota-b945",
            "publish_qualified",
        ),
    ]


def archival_update(row: int, reason: str) -> dict[str, object]:
    person_id, name = PEOPLE[row]
    box = "768" if row in {1, 2} else "769"
    return {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, Box {box} and archive location 230/86/41/07. {reason}",
        "personnel_category": "unknown_or_indeterminate",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": f"Review Box {box} for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }


def army_update(row: int, status: str = "occupation_only_found") -> dict[str, object]:
    person_id, name = PEOPLE[row]
    return {
        "person_id": person_id,
        "identity_status": "high_confidence",
        "identity_evidence": f"A nonshared protected identifier connects the visually verified {name} index row to the reviewed official Army record, and the full name agrees exactly.",
        "personnel_category": "enlisted_army_personnel",
        "commissioned_officer": False,
        "allied_or_foreign_personnel": False,
        "manual_review_required": True,
        "research_status": status,
        "next_action": "Review Box 769 to establish the immediate pre-OSS affiliation and named last civilian employer; do not convert the Army occupation category into a workplace.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }


def person_updates() -> list[dict[str, object]]:
    updates = [archival_update(row, reason) for row, reason in UNRESOLVED.items()]
    updates.extend(army_update(row) for row in (14, 19, 23))
    lazare = army_update(11, "documented_prewar_employer_found")
    lazare["possible_duplicate_group"] = "lazare-teper-page463-rows11-12-b945"
    lazare["next_action"] = "Review both Box 769 files together to determine whether the two Lazare Teper rows are duplicate references or different people, and to establish the immediate pre-OSS sequence without merging them by name."
    updates.append(lazare)
    updates.extend(
        [
            {
                "person_id": PEOPLE[12][0],
                "identity_status": "ambiguous",
                "identity_evidence": "Page 463 contains two separate Lazare Teper rows with different protected identifiers. The accepted Army bridge applies only to row 11, so row 12 remains a distinct ambiguous entity.",
                "personnel_category": "unknown_or_indeterminate",
                "manual_review_required": True,
                "possible_duplicate_group": "lazare-teper-page463-rows11-12-b945",
                "research_status": "needs_identity_review",
                "next_action": "Review both Box 769 files together and compare their protected identifiers, birth details and assignments. Do not transfer row 11's Army or ILGWU evidence to row 12.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[3][0],
                "identity_status": "high_confidence",
                "identity_evidence": "The distinctive exact name aligns across the index, the official Truman Library biography and Cambridge's explicit June 1942 OSS chronology.",
                "name_variants": ["Edward Adam Tenenbaum"],
                "personnel_category": "commissioned_army_officer",
                "commissioned_officer": True,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "occupation_only_found",
                "next_action": "Review Box 769 to resolve the exact 1942 sequence among Yale graduation, Army Air Forces service and OSS employment, and to determine whether a civilian employer intervened.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[7][0],
                "identity_status": "probable",
                "identity_evidence": "Two official records document rare near-exact Helen B. Tenney in OSS Spanish Division work, while the index prints Helen B. Tenny. No protected identifier or personnel-file bridge yet confirms the one-letter surname correction.",
                "name_variants": ["Helen B. Tenney"],
                "personnel_category": "civilian_professional_or_administrative_grade",
                "commissioned_officer": False,
                "manual_review_required": True,
                "research_status": "documented_prewar_employer_found",
                "next_action": "Review Box 769 to confirm the Tenny/Tenney spelling and the 1942 transition from Short Wave Research into the OSS Spanish Division.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[15][0],
                "identity_status": "probable",
                "identity_evidence": "Official University of Minnesota records document the rare exact Ethel M. Terhaar name and a consistent clerk-stenographer role from December 1937 into the 1939-40 budget, but no source yet bridges that employee directly to OSS or Box 769.",
                "personnel_category": "civilian_professional_or_administrative_grade",
                "commissioned_officer": False,
                "manual_review_required": True,
                "research_status": "documented_prewar_employer_found",
                "next_action": "Review Box 769 for a Minnesota address, birth date or employment history that confirms identity and establishes whether the university was the immediate or last civilian employer.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
        ]
    )
    return updates


def research_attempts() -> list[dict[str, object]]:
    army_rows = {int(item["row"]) for item in ARMY_OCCUPATIONS}
    attempts: list[dict[str, object]] = []
    for row in sorted(PEOPLE):
        person_id, name = PEOPLE[row]
        if row in UNRESOLVED:
            outcome, reviewed, rejected, detail = "no_result", 5, 5, UNRESOLVED[row]
        elif row == 12:
            outcome, reviewed, rejected, detail = (
                "candidate_found",
                6,
                5,
                "The duplicate exact name is a candidate relationship only. Its different protected identifier prevents transfer of the row 11 Army and ILGWU evidence.",
            )
        elif row == 3:
            outcome, reviewed, rejected, detail = (
                "source_reviewed",
                9,
                4,
                "Official and scholarly sources establish Edward Adam Tenenbaum's Yale, Army Air Forces and June 1942 OSS chronology, while the exact immediate predecessor remains unresolved.",
            )
        elif row == 7:
            outcome, reviewed, rejected, detail = (
                "source_reviewed",
                9,
                5,
                "Two official sources support the Helen B. Tenney OSS identity candidate and a scholarly source documents Short Wave Research immediately before OSS; the surname correction remains probable.",
            )
        elif row == 15:
            outcome, reviewed, rejected, detail = (
                "source_reviewed",
                7,
                4,
                "Two official University of Minnesota pages document Ethel M. Terhaar's prewar clerk-stenographer employment, but no second OSS identifier confirms the person match or immediate chronology.",
            )
        elif row == 11:
            outcome, reviewed, rejected, detail = (
                "source_reviewed",
                8,
                4,
                "An accepted protected Army bridge identifies row 11; Cornell documents Lazare Teper's 1937-1980 ILGWU Research Department directorship, while wartime leave and immediate chronology remain unknown.",
            )
        elif row in army_rows:
            outcome, reviewed, rejected, detail = (
                "source_reviewed",
                6,
                4,
                "An accepted protected-identifier Army bridge supports identity and a dated historical occupation category, not a named employer or immediate OSS affiliation.",
            )
        else:
            raise AssertionError(f"Missing Batch 945 outcome for row {row}")
        attempts.append(
            {
                "key": f"page463-row{row}-{slug(name)}-b945",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA index and public Archives context; CIA Reading Room; exact-name and meaningful variants; OSS and military clues; employer and occupation 1940; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Boxes 768-769; protected identifiers used privately only when defensible",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_945",
                "started_at": "2026-10-29T00:20:00Z",
                "completed_at": "2026-10-29T01:05:00Z",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search snippets, family-tree assertions, modern people-finder pages, postwar-only leads and sources without an OSS, protected-identifier or Box-file bridge were not assigned.",
                "research_notes": f"{detail} The index page and admitted Army or institutional PDF pages were visually checked where applicable. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": "Review the indexed personnel file for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before wartime service.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b945-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-945-v1",
        "reviewer": "Before OSS Batch 945 evidence review",
        "sources": sources(),
        "organizations": organizations(),
        "affiliations": affiliations(),
        "claims": army_claims() + substantive_claims(),
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }
    EvidenceBundle.model_validate(bundle)
    OUTPUT.write_text(
        json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
