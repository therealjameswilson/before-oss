#!/usr/bin/env python3
"""Generate the reviewed Batch 965 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page473-edward-trevaskis-to-barry-trivers-"
    "review_batch-965_2026-10-29.json"
)

INDEX = "nara-index-b965"
ARMY = "army-bulk-b965"
TECH = "army-tech-b965"
CODES = "army-codes-b965"
TREVETT_OBIT = "times-union-trevett-b965"
TREVOR_NARA = "nara-trevor-wilson-b965"
TREVOR_WARWICK = "warwick-trevor-wilson-b965"
TREWARTHA_WISCONSIN = "wisconsin-trewartha-b965"
TREZISE_TRUMAN = "truman-trezise-b965"
TRIFLETTI_NARA = "nara-detachment-101-trifletti-b965"
TRIPCONY_GUARD = "indiana-guard-tripcony-b965"
TRITSCH_OBIT = "washington-post-tritsch-b965"
TRIVANOVITCH_NICB = "free-library-trivanovitch-b965"
TRIVANOVITCH_AAA = "smithsonian-trivanovitch-b965"
TRIVERS_AFI = "afi-trivers-b965"


PEOPLE = {
    1: ("a86f8f5e-1b90-507d-8b07-156121038784", "Edward M Trevaskis"),
    2: ("cc6c821b-f2dd-5a1c-aea7-7075d9ed9f75", "Curtis D Trevathan"),
    3: ("01d9f8cd-245b-5f1d-931a-1bfde4a8846e", "Richard S Trevett"),
    4: ("849c7517-d88a-5db9-87e5-eb8d45592c13", "Arthur G Trevor Wilson"),
    5: ("53fea1d3-d777-5d70-b6e1-44d86bb73fab", "Glenn T Trewartha"),
    6: ("3805afc8-7986-5daf-9a0b-deca137f4390", "Leonard G Trexler"),
    7: ("e9ee2cd1-b2bf-5f49-9cf9-5b4e9dc92b29", "Philip Trezise"),
    8: ("a03f9a5e-c228-5651-bba5-20e98ad00c52", "Andre Tricard"),
    9: ("342ecd8d-85bb-5c7c-ab27-709c7bc95573", "Arthur Triebwasser"),
    10: ("e674cc03-2add-5526-b953-d389e2093d5e", "John E Triesner"),
    11: ("5cbcdd94-4fee-5e50-9bc2-51c4031de526", "Samuel L Trifiletti"),
    12: ("6bfa53b8-ca2d-5f76-9b0e-fbcdbb2d8e00", "Vincent J Trifletti"),
    13: ("01afa479-d58b-5c99-bc78-26a7f5b6f897", "Norman M Trigalet"),
    14: ("3d0e3029-78ca-510c-ae1f-32aafa4c5d0d", "Harold R Trimble"),
    15: ("3a2f3978-8978-58b2-a5c7-52df9fea8dbd", "Bonnell L Tripcony"),
    16: ("ab62ea6f-75de-567e-9524-8af26054a8d8", "Cecil L Triplett"),
    17: ("df5f7faa-df5d-5f9c-8a72-9587c69299a1", "Raymond E Triplett"),
    18: ("d2e3f6f2-942f-5d3e-b850-0913d39ba058", "Louis C Trippel"),
    19: ("04a73096-7a1f-5c3a-8aec-36b2a1320ab3", "George R Triska"),
    20: ("6eec0862-b778-5316-8dac-ac5a78be8dec", "Arthur A Tritsch"),
    21: ("a4007d7c-1236-5e83-b91b-9714712011e1", "Madeline E Tritsch"),
    22: ("3b46fb9d-a240-5366-856c-4db2e7c9fbf8", "Vaso Trivanovitch"),
    23: ("36192a2e-94fe-54fb-88bf-2b5d14d3c1b4", "Barry Trivers"),
}


ARMY_OCCUPATIONS = [
    {
        "row": 2,
        "date": "1943-01-07",
        "code": "799",
        "occupation": "Apprentices to other trades",
        "public_occupation": "apprentice to another trade",
        "locator": "PDF physical page 175; historical category 7-99",
    },
    {
        "row": 3,
        "date": "1942-11-09",
        "code": "105",
        "occupation": "Clerks, general office",
        "public_occupation": "general office clerk",
        "locator": "PDF physical page 171; historical category 1-05",
    },
    {
        "row": 6,
        "date": "1943-01-07",
        "code": "866",
        "occupation": "Unskilled occupations in production of clay products",
        "public_occupation": "unskilled clay-products production occupation",
        "locator": "PDF physical page 173; historical category 8-66",
    },
    {
        "row": 10,
        "date": "1944-01-04",
        "code": "017",
        "occupation": "Engineers, electrical",
        "public_occupation": "electrical engineer",
        "locator": "PDF physical page 170; historical category 0-17",
    },
    {
        "row": 13,
        "date": "1941-02-04",
        "code": "221",
        "occupation": "Bartenders",
        "public_occupation": "bartender",
        "locator": "PDF physical page 172; historical category 2-21",
    },
    {
        "row": 17,
        "date": "1943-10-25",
        "code": "056",
        "occupation": "Photographers",
        "public_occupation": "photographer",
        "locator": "PDF physical page 171; historical category 0-56",
    },
]


UNRESOLVED = {
    8: "Exact-name, spelling-variant, official-domain, occupation, obituary, institutional, newspaper and archival searches produced no defensible identity bridge.",
    9: "A later accounting lead and regional namesakes lack an OSS, Box 785 or protected-identifier bridge and cannot support a pre-OSS claim.",
    14: "The common name produced multiple military and civilian namesakes without two corroborating identifiers beyond the name.",
    16: "Exact-name and rank-variant searches produced no reliable OSS identity or pre-OSS affiliation source for the Box 786 row.",
    18: "Accessible exact-name, occupation, obituary and archival results did not establish the indexed person's identity or chronology.",
    19: "Exact-name and variant searches produced no reliable identity bridge, dated occupation or employing organization.",
    21: "The adjacent Arthur Tritsch record does not establish kinship or shared biography; no independent source identifies Madeline E Tritsch.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 785-786",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 473, rows 1-23; checked against layout-preserving text and a 200 dpi page render",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. Protected identifiers remain private.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; six accepted and two rejected Batch 965 candidates; protected identifiers withheld",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "No raw bulk row, record ordinal or full protected identifier enters the evidence bundle or public assets.",
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
            "access_date": "2026-10-29",
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
            "locator": "PDF physical pages 170-173 and 175; six Batch 965 historical civilian-occupation categories visually and textually checked",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical occupation groups identify neither employers nor workplaces.",
        },
        {
            "key": TREVETT_OBIT,
            "stable_url": "https://www.legacy.com/us/obituaries/timesunion-albany/name/richard-trevett-obituary?id=5007718",
            "title": "Richard S. Trevett Obituary",
            "author_creator": "Albany Times Union obituary",
            "repository_publisher": "Albany Times Union; Legacy.com",
            "publication_record_date": "2016-10-26",
            "locator": "Obituary paragraphs identifying 1940 graduation, 1942 Army enlistment and OSS radio-operator service",
            "access_date": "2026-10-29",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Albany Times Union obituaries",
            "rights_notes": "The postwar General Electric career is not presented as pre-OSS employment.",
        },
        {
            "key": TREVOR_NARA,
            "stable_url": "https://www.archives.gov/files/research/jfk/releases/104-10165-10120.pdf",
            "archival_identifier": "JFK release 104-10165-10120; X-2 Branch award recommendations",
            "title": "X-2 Branch: Survey of Board Recommendations",
            "author_creator": "Office of Strategic Services, X-2 Branch",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1945",
            "locator": "PDF physical page 182; Major Arthur G. Trevor-Wilson, British Army, Legion of Merit recommendation; visually inspected",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "JFK Assassination Records Collection",
            "document_number": "104-10165-10120",
        },
        {
            "key": TREVOR_WARWICK,
            "stable_url": "https://wrap.warwick.ac.uk/id/eprint/81565/1/WRAP_Theses_Shah_2016.pdf",
            "archival_identifier": "University of Warwick WRAP 81565",
            "title": "Secret Towns: British Intelligence in Asia during the Cold War",
            "author_creator": "Nikita Shah",
            "repository_publisher": "University of Warwick",
            "publication_record_date": "2016-03",
            "locator": "Thesis page 184; PDF physical page 199; Arthur Trevor-Wilson biographical paragraph",
            "access_date": "2026-10-29",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Warwick Research Archive Portal",
            "rights_notes": "Only a concise paraphrase and short excerpt are retained.",
        },
        {
            "key": TREWARTHA_WISCONSIN,
            "stable_url": "https://wisconsingeography.wordpress.com/wp-content/uploads/2013/05/1978-cover-pg.pdf",
            "title": "The Wisconsin Geographer, Volume 16",
            "author_creator": "Clarence U. Olmstead, compiler",
            "repository_publisher": "Department of Geography, University of Wisconsin-Madison",
            "publication_record_date": "1978",
            "locator": "Printed page 3; PDF physical page 6; dedication and career chronology for Glenn T. Trewartha",
            "access_date": "2026-10-29",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "The Wisconsin Geographer",
        },
        {
            "key": TREZISE_TRUMAN,
            "stable_url": "https://www.trumanlibrary.gov/library/oral-histories/trezise",
            "title": "Philip Trezise Oral History Interview",
            "author_creator": "Philip Trezise; interviewed by Richard D. McKinzie",
            "repository_publisher": "Harry S. Truman Presidential Library and Museum",
            "publication_record_date": "1975-05-27; opened 1979-06",
            "locator": "Transcript pages 2-3; Navy-to-OSS transfer and rejected St. John's University offer",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "Harry S. Truman Library Oral Histories",
            "rights_notes": "The interview explicitly says Trezise did not take the St. John's University job; it is not modeled as employment.",
        },
        {
            "key": TRIFLETTI_NARA,
            "archival_identifier": "RG 226, Entry UD140, Box 35, Folder 4; Promotions & Citations Report, Detachment 101, 15 May 1945; declassification authority NND 87790",
            "title": "Promotions & Citations Report, OSS SU Detachment 101, May report",
            "author_creator": "Office of Strategic Services, Special Unit Detachment 101",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1945-05-15",
            "locator": "Enlisted men's recommendations approved; Vincent J. Trifletti, staff sergeant to technical sergeant",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "The exact archival identifier is retained because the former third-party scan URL no longer resolves safely.",
        },
        {
            "key": TRIPCONY_GUARD,
            "stable_url": "https://worldwartwoveterans.org/wp-content/uploads/2020/10/National-Guard-of-the-State-of-Indiana-1938-Part-1-of-2-wm.pdf",
            "title": "Historical Annual, National Guard of the State of Indiana, 1938",
            "author_creator": "Indiana National Guard, Adjutant General's Office",
            "repository_publisher": "Indiana National Guard; digital reproduction by World War II Veterans",
            "publication_record_date": "1938; digital reproduction 2020",
            "locator": "PDF physical pages 158-159; Medical Department Detachment, Columbia City; Bonnell L. Tripcony listed among privates",
            "access_date": "2026-10-29",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Indiana National Guard historical annuals",
        },
        {
            "key": TRITSCH_OBIT,
            "stable_url": "https://www.legacy.com/us/obituaries/washingtonpost/name/arthur-tritsch-obituary?id=5601765",
            "title": "Arthur Albert Tritsch Jr. Obituary",
            "author_creator": "Washington Post obituary",
            "repository_publisher": "The Washington Post; Legacy.com",
            "publication_record_date": "2007-11-08",
            "locator": "Obituary paragraph identifying 1941 Army enlistment, OSS service and photographic-reconnaissance specialty",
            "access_date": "2026-10-29",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Washington Post obituaries",
        },
        {
            "key": TRIVANOVITCH_NICB,
            "stable_url": "https://catalog.freelibrary.org/Record/767932",
            "archival_identifier": "Free Library of Philadelphia catalog record ocm00522705",
            "title": "International Transactions of the United States: An Audit and Interpretation of Balance-of-Payments Estimates",
            "author_creator": "National Industrial Conference Board; Ray Ovid Hall; Vaso Trivanovitch, editor",
            "repository_publisher": "Free Library of Philadelphia catalog",
            "publication_record_date": "1936",
            "locator": "Catalog item description and MARC note identifying Trivanovitch as a member of the Board's staff",
            "access_date": "2026-10-29",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Free Library of Philadelphia catalog",
        },
        {
            "key": TRIVANOVITCH_AAA,
            "stable_url": "https://www.aaa.si.edu/collections/interviews/oral-history-interview-miriam-hapgood-dewitt-12941",
            "archival_identifier": "Archives of American Art oral-history record edanmdm-AAADCD_oh_215739",
            "title": "Oral History Interview with Miriam Hapgood DeWitt, 1987-1988",
            "author_creator": "Miriam Hapgood DeWitt; interviewed by Robert F. Brown",
            "repository_publisher": "Archives of American Art, Smithsonian Institution",
            "publication_record_date": "1987-1988",
            "locator": "Transcript around 00:26:24-00:30:05; Vaso Trivanovitch identified as an economist met at a wartime government agency",
            "access_date": "2026-10-29",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Archives of American Art Oral History Program",
            "rights_notes": "The interview does not name OSS and is used only as corroborating identity and occupation context.",
        },
        {
            "key": TRIVERS_AFI,
            "stable_url": "https://catalog.afi.com/Catalog/MovieDetails/26698?cxt=filmography",
            "archival_identifier": "AFI Catalog movie record 26698",
            "title": "Flight from Destiny",
            "author_creator": "American Film Institute Catalog of Feature Films",
            "repository_publisher": "American Film Institute",
            "publication_record_date": "1941-02-08",
            "locator": "Full credits, Writers; Barry Trivers credited for screenplay; release details",
            "access_date": "2026-10-29",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "AFI Catalog of Feature Films",
            "rights_notes": "A film credit establishes professional writing activity, not employment by the studio.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": "us-army-b965",
            "organization_id": "28a26f92-78af-5a1a-9c09-a843eb5975b4",
            "canonical_name": "United States Army",
            "historical_name": "Army of the United States",
            "aliases": ["U.S. Army", "US Army"],
            "organization_type": "military service",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "Existing canonical organization reused; exact component and unit remain unresolved where the source does not identify them.",
        },
        {
            "key": "us-navy-b965",
            "organization_id": "3960fa8e-a551-56cf-8305-b2b9e4961b9d",
            "canonical_name": "United States Navy",
            "historical_name": "United States Navy",
            "aliases": ["U.S. Navy", "Navy", "USN"],
            "organization_type": "military service",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "Existing canonical organization reused; Trezise's rank and component remain unresolved.",
        },
        {
            "key": "wisconsin-b965",
            "organization_id": "4a1a13c4-1aee-5ab1-ac44-16b7a037b7d4",
            "canonical_name": "University of Wisconsin-Madison",
            "historical_name": "University of Wisconsin",
            "aliases": ["University of Wisconsin", "UW-Madison"],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "Madison",
            "state_or_region": "Wisconsin",
            "country": "United States",
            "normalization_notes": "The historical employer wording is preserved separately from the modern canonical name.",
        },
        {
            "key": "indiana-guard-b965",
            "organization_id": "f500e532-8599-537c-8c0b-cf11a8c1ee6b",
            "canonical_name": "Indiana National Guard",
            "historical_name": "Indiana National Guard",
            "aliases": ["National Guard of the State of Indiana"],
            "organization_type": "state military organization",
            "sector": "military",
            "state_or_region": "Indiana",
            "country": "United States",
            "normalization_notes": "The 1938 Medical Department Detachment is preserved as a unit detail, not silently merged into a later federal Army assignment.",
        },
        {
            "key": "broadalbin-high-b965",
            "canonical_name": "Broadalbin High School",
            "historical_name": "Broadalbin High School",
            "organization_type": "secondary school",
            "sector": "academia_and_research",
            "city": "Broadalbin",
            "state_or_region": "New York",
            "country": "United States",
            "normalization_notes": "Trevett's relationship is student status and is not counted as employment.",
        },
        {
            "key": "nicb-b965",
            "canonical_name": "National Industrial Conference Board",
            "historical_name": "National Industrial Conference Board, Inc.",
            "aliases": ["Conference Board", "NICB"],
            "organization_type": "business research organization",
            "sector": "business_and_industry",
            "city": "New York",
            "state_or_region": "New York",
            "country": "United States",
            "active_dates": "1916-1970",
            "normalization_notes": "The historical organization is not silently replaced by a modern successor name.",
        },
    ]


def army_affiliation(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    return {
        "key": f"{slug(PEOPLE[row][1])}-occupation-b965",
        "person_id": PEOPLE[row][0],
        "occupation": item["public_occupation"],
        "relationship_type": "employment",
        "end_date": item["date"],
        "date_precision": f"Historical civilian-occupation code {item['code']} was recorded at Army entry on {item['date']}; no employer, workplace or OSS-transfer date is named.",
        "country": "United States",
        "immediate_pre_oss": False,
        "last_civilian_pre_service": False,
        "pre_oss_temporal_basis": "strongly_date_bounded",
        "identity_confidence": "confirmed" if row == 3 else "high_confidence",
        "claim_confidence": "medium",
        "source_quality": "A_direct_official",
        "publication_status": "publish_qualified",
        "research_notes": "The historical category is not converted into a named employer, workplace, exact specialization or immediate pre-OSS affiliation.",
    }


def specialist_affiliations() -> list[dict[str, object]]:
    return [
        {
            "key": "richard-trevett-broadalbin-b965",
            "person_id": PEOPLE[3][0],
            "organization_key": "broadalbin-high-b965",
            "organization_name_as_found": "Broadalbin High School",
            "role_title": "student",
            "relationship_type": "student",
            "end_date": "1940",
            "date_precision": "The obituary states that Trevett graduated in 1940; it does not identify later civilian employment before his 1942 Army enlistment.",
            "city": "Broadalbin",
            "state_or_region": "New York",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "confirmed",
            "claim_confidence": "medium",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "publish_qualified",
            "research_notes": "Education is preserved as student status and not treated as an employer.",
        },
        {
            "key": "arthur-trevor-wilson-perfume-b965",
            "person_id": PEOPLE[4][0],
            "organization_name_as_found": "unnamed French perfume house",
            "role_title": "employee",
            "occupation": "perfume-house employee",
            "relationship_type": "employment",
            "end_date": "1942",
            "date_precision": "The scholarly source says he spent the interwar years at a French perfume house and was MI6 station chief in Algiers by 1942; the employer is not named.",
            "country": "France",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "confirmed",
            "claim_confidence": "medium",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "publish_qualified",
            "research_notes": "The unnamed historical employer is not normalized to a modern company and is not claimed as the immediate OSS predecessor.",
        },
        {
            "key": "glenn-trewartha-wisconsin-b965",
            "person_id": PEOPLE[5][0],
            "organization_key": "wisconsin-b965",
            "organization_name_as_found": "University of Wisconsin",
            "role_title": "instructor and professor of geography",
            "occupation": "geography professor",
            "relationship_type": "employment",
            "start_date": "1922",
            "date_precision": "The institutional history dates instructor service to 1922, assistant-professor service to 1926 and a 59-year Wisconsin geography career; 1942 marks the pre-OSS research boundary, not termination.",
            "city": "Madison",
            "state_or_region": "Wisconsin",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "probable",
            "claim_confidence": "medium",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "publish_qualified",
            "research_notes": "The employer is explicit, but the Box 785 file must confirm the rare-name identity and exact OSS chronology.",
        },
        {
            "key": "philip-trezise-navy-b965",
            "person_id": PEOPLE[7][0],
            "organization_key": "us-navy-b965",
            "organization_name_as_found": "Navy",
            "relationship_type": "military_assignment",
            "end_date": "1945",
            "date_precision": "Trezise explicitly recalled being co-opted from the Navy to OSS during World War II; exact transfer date, component and rank are not supplied.",
            "country": "United States",
            "immediate_pre_oss": True,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "explicit_immediate",
            "identity_confidence": "confirmed",
            "claim_confidence": "confirmed",
            "source_quality": "A_direct_official",
            "publication_status": "published",
            "research_notes": "The unaccepted St. John's University offer is explicitly excluded from employment claims.",
        },
        {
            "key": "bonnell-tripcony-indiana-guard-b965",
            "person_id": PEOPLE[15][0],
            "organization_key": "indiana-guard-b965",
            "organization_name_as_found": "National Guard of the State of Indiana",
            "role_title": "private, Medical Department Detachment",
            "relationship_type": "military_assignment",
            "end_date": "1938",
            "date_precision": "The 1938 annual lists the exact rare name among the detachment's privates; it does not document later federal service or an OSS transfer date.",
            "city": "Columbia City",
            "state_or_region": "Indiana",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "probable",
            "claim_confidence": "medium",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "publish_qualified",
            "research_notes": "Published as a qualified earlier military affiliation pending Box 786 review.",
        },
        {
            "key": "arthur-tritsch-army-b965",
            "person_id": PEOPLE[20][0],
            "organization_key": "us-army-b965",
            "organization_name_as_found": "U.S. Army",
            "relationship_type": "military_assignment",
            "start_date": "1941",
            "end_date": "1945",
            "date_precision": "The obituary states that Tritsch enlisted in 1941 and then served with OSS throughout World War II; exact unit, transfer date and commissioning chronology are not supplied.",
            "country": "United States",
            "immediate_pre_oss": True,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "probable_immediate",
            "identity_confidence": "high_confidence",
            "claim_confidence": "medium",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "publish_qualified",
            "research_notes": "The source supports an Army-to-OSS pathway but not the exact administrative transfer or a civilian employer.",
        },
        {
            "key": "vaso-trivanovitch-nicb-b965",
            "person_id": PEOPLE[22][0],
            "organization_key": "nicb-b965",
            "organization_name_as_found": "National Industrial Conference Board",
            "role_title": "research staff member and editor",
            "occupation": "economist",
            "relationship_type": "employment",
            "start_date": "1933",
            "end_date": "1936",
            "date_precision": "Catalog records document his economic investigation in 1933 and explicitly identify him as a Board staff member and editor in 1936.",
            "city": "New York",
            "state_or_region": "New York",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "probable",
            "claim_confidence": "medium",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "publish_qualified",
            "research_notes": "The rare name and economist occupation support a probable identity; the wartime agency is not identified as OSS in the corroborating oral history.",
        },
        {
            "key": "barry-trivers-screenwriter-b965",
            "person_id": PEOPLE[23][0],
            "role_title": "screenplay writer",
            "occupation": "screenwriter",
            "relationship_type": "professional_affiliation",
            "end_date": "1941-02-08",
            "date_precision": "AFI credits Trivers for the screenplay of a film released on 8 February 1941; the credit does not establish an employment contract or OSS chronology.",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "probable",
            "claim_confidence": "medium",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "publish_qualified",
            "research_notes": "Warner Bros. is not inferred to be his employer from a film credit alone.",
        },
    ]


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
    source_links: list[dict[str, object]],
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
        confirmed = row == 3
        links: list[dict[str, object]] = [
            {"source_key": INDEX, "locator_override": f"PDF page 473 row {row}; protected identifier withheld"},
            {"source_key": ARMY, "locator_override": "Accepted reviewed identity bridge; protected identifier withheld"},
        ]
        if confirmed:
            links.append(
                {
                    "source_key": TREVETT_OBIT,
                    "locator_override": "Obituary paragraphs on 1940 graduation, 1942 enlistment and OSS radio service",
                    "excerpt_override": "served as a radio operator for the O.S.S.",
                }
            )
        values.append(
            claim(
                row,
                f"identity-{slug(name)}-army-b965",
                "identity",
                f"Indexed {name} is a {'confirmed' if confirmed else 'high-confidence'} match to the reviewed official Army entry.",
                "A nonshared protected identifier connects the visually verified index row to the official Army record."
                + (" An independent obituary repeats his exact name, Army chronology and OSS radio service." if confirmed else ""),
                "Confirmed by exact identifier agreement plus an independent exact-name OSS obituary." if confirmed else "High confidence from exact protected-identifier agreement plus compatible full-name evidence.",
                "Identity evidence only; the Army entry does not itself establish an OSS transfer date.",
                "A_direct_official",
                "confirmed" if confirmed else "high",
                links,
                "The review accepts identity only for this source row and does not expose the protected identifier.",
            )
        )
        category = str(item["occupation"])
        values.append(
            claim(
                row,
                f"occupation-{slug(name)}-army-b965",
                "occupation",
                f"At Army entry on {item['date']}, the record coded {name}'s civilian occupation as {category}.",
                f"The official Army record contains civilian-occupation code {item['code']}; NARA's historical code list expands it to {category}.",
                "Confirmed identity from independent exact-name OSS evidence and the accepted identifier bridge." if confirmed else "High-confidence identity from the accepted protected-identifier bridge and compatible full-name evidence.",
                "The code was recorded at Army entry and is date-bounded, but it identifies no employer, workplace or immediate OSS predecessor.",
                "A_direct_official",
                "medium",
                [
                    {"source_key": ARMY, "locator_override": f"Accepted identity record; civilian occupation code {item['code']}; protected identifier withheld"},
                    {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46; Army-entry-date and civilian-occupation fields"},
                    {"source_key": CODES, "locator_override": str(item["locator"]), "excerpt_override": category},
                ],
                "The historical category is published as qualified occupation evidence and excluded from named-employer analytics.",
                f"{slug(name)}-occupation-b965",
                "publish_qualified",
            )
        )
    return values


def conflict_claims() -> list[dict[str, object]]:
    return [
        claim(
            1,
            "conflict-edward-trevaskis-army-b965",
            "identity",
            "Edward M Trevaskis has a rejected Army candidate whose protected identifier agrees but whose printed name is incompatible and corrupt.",
            "The private identifier selects an Army row with a name that does not match Trevaskis; no occupation, date or grade is transferred.",
            "Conflicting source selectors. Identifier agreement alone cannot overcome a materially incompatible name.",
            "Identity conflict only; all candidate biographical fields are withheld.",
            "A_direct_official",
            "conflicting",
            [
                {"source_key": INDEX, "locator_override": "PDF page 473 row 1; protected identifier withheld"},
                {"source_key": ARMY, "support_type": "contradicts", "locator_override": "Rejected incompatible-name candidate; protected identifier withheld"},
            ],
            "The candidate remains reviewable in the private decision ledger; the public claim exposes no identifier or raw Army row.",
            publication_status="conflicting",
        ),
        claim(
            11,
            "conflict-samuel-trifiletti-army-b965",
            "identity",
            "Samuel L Trifiletti has a rejected Army candidate that prints Samuel F Trifiletti despite protected-identifier agreement.",
            "The middle-initial disagreement is preserved and the candidate's occupation, date and grade are not transferred.",
            "Conflicting. The exact surname and first name plus identifier are strong, but the middle initial differs and no independent bridge resolves it.",
            "Identity conflict only; the dated occupation remains withheld.",
            "A_direct_official",
            "conflicting",
            [
                {"source_key": INDEX, "locator_override": "PDF page 473 row 11; Samuel L Trifiletti; protected identifier withheld"},
                {"source_key": ARMY, "support_type": "contradicts", "locator_override": "Rejected Samuel F Trifiletti candidate; protected identifier withheld"},
            ],
            "Do not merge the initials or publish the candidate occupation until Box 785 or another direct source resolves the discrepancy.",
            publication_status="conflicting",
        ),
    ]


def specialist_claims() -> list[dict[str, object]]:
    return [
        claim(
            3,
            "student-richard-trevett-broadalbin-b965",
            "other_pre_oss_affiliation",
            "Richard S. Trevett graduated from Broadalbin High School in 1940 before entering the Army in 1942.",
            "The obituary supplies the school, graduation year, Army-entry year and OSS radio-operator service.",
            "Confirmed by the exact protected-identifier Army bridge and independent exact-name obituary.",
            "Documented prewar education; the two-year interval means it is not labeled the immediate OSS predecessor or an employer.",
            "C_reputable_contemporary_or_scholarly",
            "medium",
            [{"source_key": TREVETT_OBIT, "locator_override": "Obituary paragraph on 1940 graduation and 1942 Army enlistment"}],
            "Student status is explicitly separated from employment.",
            "richard-trevett-broadalbin-b965",
            "publish_qualified",
        ),
        claim(
            4,
            "identity-arthur-trevor-wilson-b965",
            "identity",
            "Indexed Arthur G Trevor Wilson is confirmed as British Army Major Arthur G. Trevor-Wilson, an Allied counterintelligence officer who cooperated with OSS.",
            "An original OSS X-2 award sheet supplies the exact name variant, middle initial, British Army rank and detailed counterintelligence cooperation.",
            "Confirmed by the uncommon exact name and middle initial, British Army status and direct original OSS record.",
            "The source documents wartime Allied cooperation, not a transfer into U.S. OSS employment.",
            "A_direct_official",
            "confirmed",
            [
                {"source_key": INDEX, "locator_override": "PDF page 473 row 4; Box 785"},
                {"source_key": TREVOR_NARA, "locator_override": "PDF physical page 182; first Legion of Merit entry", "excerpt_override": "(Major) Arthur G. Trevor-Wilson (Brit Army)"},
            ],
            "The hyphenated surname and expanded full name are preserved as documented variants.",
        ),
        claim(
            4,
            "prewar-arthur-trevor-wilson-perfume-b965",
            "other_pre_oss_affiliation",
            "Before wartime intelligence service, Arthur Trevor-Wilson worked for an unnamed French perfume house during the interwar years.",
            "A scholarly history states that he spent the interwar years at a French perfume house before becoming MI6 station chief in Algiers in 1942.",
            "Confirmed identity from the original OSS award sheet; the scholarly source uses the same rare hyphenated name and intelligence chronology.",
            "Documented prewar employment. The employer is unnamed and immediacy relative to OSS cooperation is not established.",
            "C_reputable_contemporary_or_scholarly",
            "medium",
            [{"source_key": TREVOR_WARWICK, "locator_override": "Thesis page 184; PDF physical page 199", "excerpt_override": "spent the inter-war years working for a French perfume house"}],
            "No company name or modern successor is inferred.",
            "arthur-trevor-wilson-perfume-b965",
            "publish_qualified",
        ),
        claim(
            5,
            "identity-glenn-trewartha-b965",
            "identity",
            "The indexed Glenn T Trewartha is a probable match to University of Wisconsin geographer Glenn Thomas Trewartha.",
            "The institutional history supplies the rare exact name, expanded middle name, continuous Wisconsin geography career and extensive Japan expertise.",
            "Probable from the rare exact name and compatible specialist background; no independent public OSS, Box 785 or protected-identifier bridge was found.",
            "The career chronology begins in 1920 and spans the wartime period, but the exact OSS relationship is unresolved.",
            "B_authoritative_institutional",
            "medium",
            [
                {"source_key": INDEX, "locator_override": "PDF page 473 row 5; Box 785"},
                {"source_key": TREWARTHA_WISCONSIN, "locator_override": "Printed page 3; PDF physical page 6"},
            ],
            "The identity and employer remain visibly qualified pending personnel-file review.",
            publication_status="publish_qualified",
        ),
        claim(
            5,
            "prewar-glenn-trewartha-wisconsin-b965",
            "other_pre_oss_affiliation",
            "A probable identity match indicates that Glenn T. Trewartha taught geography at the University of Wisconsin from the 1920s through the pre-OSS period.",
            "The departmental history dates assistant service to 1920-1921, instructor service to 1922 and assistant-professor service to 1926 within a long Wisconsin career.",
            "Probable identity only; the rare name and specialist field are strong but do not independently prove the OSS index match.",
            "Documented prewar employment, but the exact OSS start and any wartime leave or transfer are not established.",
            "B_authoritative_institutional",
            "medium",
            [{"source_key": TREWARTHA_WISCONSIN, "locator_override": "Printed page 3; PDF physical page 6"}],
            "Published as qualified employment and excluded from confirmed/high default employer analytics.",
            "glenn-trewartha-wisconsin-b965",
            "publish_qualified",
        ),
        claim(
            7,
            "identity-philip-trezise-b965",
            "identity",
            "Indexed Philip Trezise is confirmed as the U.S. Navy serviceman who recalled being transferred to OSS and sent to China.",
            "In a presidential-library oral history, Trezise directly describes his Navy-to-OSS transfer and subsequent China assignment.",
            "Confirmed by the uncommon exact name and first-person account explicitly naming Navy, OSS and China.",
            "The first-person chronology explicitly places Navy service immediately before OSS.",
            "A_direct_official",
            "confirmed",
            [
                {"source_key": INDEX, "locator_override": "PDF page 473 row 7; Box 785"},
                {"source_key": TREZISE_TRUMAN, "locator_override": "Transcript page 2", "excerpt_override": "I was co-opted from the Navy to OSS"},
            ],
            "The rejected St. John's University offer is not an affiliation or employer.",
        ),
        claim(
            7,
            "immediate-philip-trezise-navy-b965",
            "immediate_pre_oss_affiliation",
            "Philip Trezise's immediate pre-OSS affiliation was service in the United States Navy.",
            "Trezise explicitly states that OSS co-opted him from the Navy during World War II.",
            "Confirmed by a first-person presidential-library oral history and the uncommon exact index name.",
            "Explicit immediate: the interview directly describes movement from Navy to OSS.",
            "A_direct_official",
            "confirmed",
            [{"source_key": TREZISE_TRUMAN, "locator_override": "Transcript page 2", "excerpt_override": "co-opted from the Navy to OSS"}],
            "Rank, component, exact date and last civilian employer remain unresolved.",
            "philip-trezise-navy-b965",
        ),
        claim(
            12,
            "identity-vincent-trifletti-b965",
            "identity",
            "Indexed Vincent J Trifletti is confirmed as the enlisted OSS Detachment 101 member recommended for promotion in May 1945.",
            "An original OSS promotion report names Vincent J. Trifletti and records an approved staff-sergeant-to-technical-sergeant recommendation.",
            "Confirmed by the rare exact full name and middle initial in both the index and a direct original OSS unit record.",
            "The source documents OSS service in May 1945 but supplies no pre-OSS employer or transfer chronology.",
            "A_direct_official",
            "confirmed",
            [
                {"source_key": INDEX, "locator_override": "PDF page 473 row 12; Box 785"},
                {"source_key": TRIFLETTI_NARA, "locator_override": "Enlisted men's recommendations approved", "excerpt_override": "Trifletti, Vincent J"},
            ],
            "The public record identifies enlisted status without exposing the index identifier.",
        ),
        claim(
            15,
            "identity-bonnell-tripcony-b965",
            "identity",
            "The indexed Bonnell L Tripcony is a probable match to the Indiana National Guard private listed in a 1938 unit roster.",
            "The contemporary state military annual supplies the rare exact full name and middle initial in a Columbia City medical detachment.",
            "Probable from the rare exact name and compatible prewar military context; no independent OSS, Box 786 or protected-identifier bridge was found.",
            "The 1938 record predates OSS but does not establish a later transfer.",
            "C_reputable_contemporary_or_scholarly",
            "medium",
            [
                {"source_key": INDEX, "locator_override": "PDF page 473 row 15; Box 786"},
                {"source_key": TRIPCONY_GUARD, "locator_override": "PDF physical pages 158-159; Medical Department Detachment roster"},
            ],
            "The identity remains qualified pending Box 786 review.",
            publication_status="publish_qualified",
        ),
        claim(
            15,
            "prewar-bonnell-tripcony-guard-b965",
            "other_pre_oss_affiliation",
            "A probable identity match indicates that Bonnell L. Tripcony served as a private in an Indiana National Guard medical detachment in 1938.",
            "The 1938 annual lists Bonnell L. Tripcony among the detachment's privates and places the unit in Columbia City, Indiana.",
            "Probable identity from the rare exact name; the personnel file has not yet supplied an OSS bridge.",
            "Documented prewar military affiliation, not proven to be the immediate OSS predecessor.",
            "C_reputable_contemporary_or_scholarly",
            "medium",
            [{"source_key": TRIPCONY_GUARD, "locator_override": "PDF physical pages 158-159; Medical Department Detachment roster", "excerpt_override": "TRIPCONY, BONNELL L."}],
            "Published as a qualified earlier military affiliation and excluded from confirmed/high default analytics.",
            "bonnell-tripcony-indiana-guard-b965",
            "publish_qualified",
        ),
        claim(
            20,
            "identity-arthur-tritsch-b965",
            "identity",
            "Indexed Arthur A Tritsch is a high-confidence match to Arthur Albert Tritsch Jr., who served with OSS after entering the U.S. Army.",
            "The Washington Post obituary supplies the exact uncommon name, expanded middle name, 1941 Army entry, direct OSS service and photographic-reconnaissance specialty.",
            "High confidence from the uncommon exact name, middle initial, explicit OSS service and compatible wartime Army chronology.",
            "The chronology establishes wartime service but not the exact OSS transfer or commissioning date.",
            "C_reputable_contemporary_or_scholarly",
            "high",
            [
                {"source_key": INDEX, "locator_override": "PDF page 473 row 20; Box 786"},
                {"source_key": TRITSCH_OBIT, "locator_override": "Opening obituary paragraph", "excerpt_override": "served with the OSS in southern Europe, Panama and North Africa"},
            ],
            "Later rank and postwar employment are not projected backward into the OSS period.",
        ),
        claim(
            20,
            "immediate-arthur-tritsch-army-b965",
            "immediate_pre_oss_affiliation",
            "Arthur A. Tritsch's best-supported pathway into OSS was U.S. Army service beginning in 1941.",
            "The obituary states that Tritsch enlisted in the Army in 1941 and then served with OSS throughout World War II.",
            "High-confidence identity from the uncommon exact name and explicit OSS biography.",
            "Probable immediate: the ordered chronology supports an Army-to-OSS pathway, but no transfer order or exact date was found.",
            "C_reputable_contemporary_or_scholarly",
            "medium",
            [{"source_key": TRITSCH_OBIT, "locator_override": "Opening obituary paragraph"}],
            "The claim is visibly qualified and does not establish commissioned status or a civilian employer.",
            "arthur-tritsch-army-b965",
            "publish_qualified",
        ),
        claim(
            22,
            "identity-vaso-trivanovitch-b965",
            "identity",
            "The indexed Vaso Trivanovitch is a probable match to the economist who worked for the National Industrial Conference Board and later at a wartime government agency.",
            "Institutional catalog and oral-history sources independently supply the rare exact name, economist occupation and prewar-to-wartime chronology.",
            "Probable from a highly distinctive exact name and consistent economist role; the oral history does not identify the wartime agency as OSS.",
            "The 1933-1936 employment clearly predates OSS; the wartime agency sequence remains incomplete.",
            "B_authoritative_institutional",
            "medium",
            [
                {"source_key": INDEX, "locator_override": "PDF page 473 row 22; Box 786"},
                {"source_key": TRIVANOVITCH_NICB, "locator_override": "Catalog item description and MARC note"},
                {"source_key": TRIVANOVITCH_AAA, "support_type": "context_only", "locator_override": "Transcript around 00:26:24-00:30:05"},
            ],
            "The identity remains qualified and the physical file is needed to name the wartime agency and OSS entry path.",
            publication_status="publish_qualified",
        ),
        claim(
            22,
            "prewar-vaso-trivanovitch-nicb-b965",
            "other_pre_oss_affiliation",
            "A probable identity match documents Vaso Trivanovitch as a National Industrial Conference Board staff economist and editor by 1936.",
            "The library catalog quotes the publication note identifying Trivanovitch as a member of the Board's staff and editor of the report.",
            "Probable identity from the rare exact name, economist occupation and corroborating wartime oral-history context.",
            "Documented prewar employment in 1933-1936; it is not shown to be the immediate predecessor to OSS.",
            "B_authoritative_institutional",
            "medium",
            [{"source_key": TRIVANOVITCH_NICB, "locator_override": "Catalog item description and MARC note", "excerpt_override": "Vaso Trivanovitch, also of the Board's staff"}],
            "Published as qualified earlier employment and excluded from confirmed/high default employer analytics.",
            "vaso-trivanovitch-nicb-b965",
            "publish_qualified",
        ),
        claim(
            23,
            "identity-barry-trivers-b965",
            "identity",
            "The indexed Barry Trivers is a probable match to the screenwriter credited by the American Film Institute in 1941.",
            "AFI supplies the rare exact name and a dated prewar screenplay credit.",
            "Probable from the rare exact name and compatible chronology; no independent OSS, Box 786 or protected-identifier bridge was found.",
            "The film credit predates OSS but does not establish the timing of any OSS association.",
            "B_authoritative_institutional",
            "medium",
            [
                {"source_key": INDEX, "locator_override": "PDF page 473 row 23; Box 786"},
                {"source_key": TRIVERS_AFI, "locator_override": "Full credits, Writers; release details"},
            ],
            "The identity remains qualified pending personnel-file review.",
            publication_status="publish_qualified",
        ),
        claim(
            23,
            "prewar-barry-trivers-screenwriter-b965",
            "occupation",
            "A probable identity match indicates that Barry Trivers was working as a screenwriter before the wartime OSS period.",
            "The AFI Catalog credits Barry Trivers for the screenplay of Flight from Destiny, released in February 1941.",
            "Probable identity from the rare exact name; no independent OSS bridge was found.",
            "Documented prewar professional activity, but neither a studio employment relationship nor immediacy is established.",
            "B_authoritative_institutional",
            "medium",
            [{"source_key": TRIVERS_AFI, "locator_override": "Full credits, Writers; release date", "excerpt_override": "Barry Trivers — Scr"}],
            "The film credit is not converted into employment by Warner Bros. or another production company.",
            "barry-trivers-screenwriter-b965",
            "publish_qualified",
        ),
    ]


def claims() -> list[dict[str, object]]:
    return army_claims() + conflict_claims() + specialist_claims()


def unresolved_update(row: int, reason: str) -> dict[str, object]:
    person_id, name = PEOPLE[row]
    box = "785" if row <= 13 else "786"
    return {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, Box {box} and archive location 230/86/42/03. {reason}",
        "personnel_category": "unknown_or_indeterminate",
        "commissioned_officer": None,
        "allied_or_foreign_personnel": False,
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": f"Review Box {box} for corroborating identifiers, immediate pre-OSS affiliation and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }


def army_update(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    person_id, name = PEOPLE[row]
    confirmed = row == 3
    evidence = f"A nonshared protected identifier connects the visually verified {name} index row to the reviewed official Army record."
    if confirmed:
        evidence += " An independent exact-name obituary also supplies compatible Army chronology and direct OSS radio service."
    update: dict[str, object] = {
        "person_id": person_id,
        "identity_status": "confirmed" if confirmed else "high_confidence",
        "identity_evidence": evidence,
        "personnel_category": "enlisted_army_personnel",
        "commissioned_officer": False,
        "allied_or_foreign_personnel": False,
        "manual_review_required": True,
        "research_status": "occupation_only_found",
        "next_action": "Review Box 785 or 786 to establish the immediate pre-OSS affiliation and named last civilian employer; do not convert the Army occupation category into a workplace.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }
    if confirmed:
        update["name_variants"] = ['Richard S. "Dick" Trevett']
    return update


def conflict_update(row: int, evidence: str) -> dict[str, object]:
    box = "785" if row <= 13 else "786"
    return {
        "person_id": PEOPLE[row][0],
        "identity_status": "conflicting",
        "identity_evidence": evidence,
        "personnel_category": "unknown_or_indeterminate",
        "commissioned_officer": None,
        "allied_or_foreign_personnel": False,
        "manual_review_required": True,
        "research_status": "conflicting_sources",
        "next_action": f"Review Box {box} and an original service record to resolve the protected-identifier conflict. No candidate occupation or employer has been transferred.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "critical",
    }


def person_updates() -> list[dict[str, object]]:
    values = [unresolved_update(row, reason) for row, reason in UNRESOLVED.items()]
    values.extend(army_update(item) for item in ARMY_OCCUPATIONS)
    values.extend(
        [
            conflict_update(1, "A protected identifier selects an official Army candidate whose printed name is materially incompatible and corrupt. The candidate was rejected and no biographical field was transferred."),
            conflict_update(11, "A protected identifier selects Samuel F Trifiletti, while the index prints Samuel L Trifiletti. The middle-initial conflict is unresolved, so the candidate was rejected and its occupation withheld."),
            {
                "person_id": PEOPLE[4][0],
                "identity_status": "confirmed",
                "identity_evidence": "An original OSS X-2 award sheet identifies British Army Major Arthur G. Trevor-Wilson by exact name and middle initial and documents extensive counterintelligence cooperation with OSS.",
                "name_variants": ["Arthur G. Trevor-Wilson", "Arthur Geoffrey Trevor-Wilson"],
                "personnel_category": "foreign_or_allied_military_personnel",
                "commissioned_officer": True,
                "allied_or_foreign_personnel": True,
                "manual_review_required": True,
                "research_status": "occupation_only_found",
                "next_action": "Review Box 785 and British service records to confirm the exact relationship between his British assignments and the OSS file and to identify the unnamed French perfume house.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[5][0],
                "identity_status": "probable",
                "identity_evidence": "The rare exact name, expanded middle name, continuous University of Wisconsin geography career and Japan expertise support a probable match, but no independent OSS or protected-identifier bridge was found.",
                "name_variants": ["Glenn Thomas Trewartha"],
                "personnel_category": "civilian_professional_or_administrative_grade",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "documented_prewar_employer_found",
                "next_action": "Review Box 785 to confirm identity, exact OSS chronology and whether University of Wisconsin employment was the immediate civilian predecessor.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[7][0],
                "identity_status": "confirmed",
                "identity_evidence": "In a presidential-library oral history, Philip Trezise directly states that he was co-opted from the Navy to OSS and sent to China.",
                "personnel_category": "unknown_or_indeterminate",
                "commissioned_officer": None,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Review Box 785 for Navy rank and component, exact transfer date and last civilian employer. Do not treat the rejected St. John's University offer as employment.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[12][0],
                "identity_status": "confirmed",
                "identity_evidence": "An original OSS Detachment 101 promotion report repeats the rare exact full name and middle initial and identifies enlisted wartime service.",
                "personnel_category": "enlisted_army_personnel",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Review Box 785 for pre-OSS Army unit, civilian occupation and named employer; the 1945 Detachment 101 record establishes OSS service only.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[15][0],
                "identity_status": "probable",
                "identity_evidence": "A 1938 Indiana National Guard annual lists the rare exact Bonnell L Tripcony name as a private in a Columbia City medical detachment, but supplies no OSS bridge.",
                "personnel_category": "unknown_or_indeterminate",
                "commissioned_officer": None,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "occupation_only_found",
                "next_action": "Review Box 786 to confirm the rare-name identity, later military chronology, immediate pre-OSS affiliation and last civilian employer.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[20][0],
                "identity_status": "high_confidence",
                "identity_evidence": "A Washington Post obituary supplies the uncommon exact name, expanded middle name, 1941 Army entry, explicit OSS service and photographic-reconnaissance specialty.",
                "name_variants": ["Arthur Albert Tritsch Jr."],
                "personnel_category": "unknown_or_indeterminate",
                "commissioned_officer": None,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Review Box 786 for the exact Army-to-OSS transfer, wartime grade and last civilian employer; do not project the later Major rank backward.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[22][0],
                "identity_status": "probable",
                "identity_evidence": "Institutional catalog and oral-history sources independently supply the highly distinctive exact name, economist occupation and compatible prewar-to-wartime government chronology, but the wartime agency is not identified as OSS.",
                "personnel_category": "civilian_professional_or_administrative_grade",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "documented_prewar_employer_found",
                "next_action": "Review Box 786 to confirm the identity, name the wartime government agency and determine whether the 1936 Conference Board role was followed by another employer.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[23][0],
                "identity_status": "probable",
                "identity_evidence": "The AFI Catalog supplies the rare exact name and a dated 1941 screenplay credit, but no independent OSS, Box 786 or protected-identifier bridge.",
                "personnel_category": "unknown_or_indeterminate",
                "commissioned_officer": None,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "occupation_only_found",
                "next_action": "Review Box 786 to confirm the identity, employment arrangement, immediate pre-OSS affiliation and last civilian employer.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
        ]
    )
    return values


def research_attempts() -> list[dict[str, object]]:
    army_rows = {int(item["row"]) for item in ARMY_OCCUPATIONS}
    conflicts = {1, 11}
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        if row in army_rows:
            outcome, reviewed, rejected = "source_reviewed", 8, 4
            detail = "Accepted an exact nonshared protected-identifier Army bridge and verified the dated historical civilian-occupation code against NARA technical documentation."
            if row == 3:
                reviewed, rejected = 10, 4
                detail += " An independent obituary confirmed Richard Trevett's exact identity, school chronology, Army entry and OSS radio service."
        elif row in conflicts:
            outcome, reviewed, rejected = "candidate_rejected", 7, 7
            detail = "Rejected the Army candidate because its printed name conflicts with the indexed identity despite private identifier agreement; no candidate field was transferred."
        elif row == 4:
            outcome, reviewed, rejected = "source_reviewed", 10, 5
            detail = "An original OSS award sheet confirmed the British officer's identity; a scholarly history documented only an unnamed interwar French perfume-house employer."
        elif row == 5:
            outcome, reviewed, rejected = "source_reviewed", 9, 6
            detail = "An institutional departmental history supports a probable rare-name identity and explicit University of Wisconsin employment; exact OSS chronology remains unproved."
        elif row == 7:
            outcome, reviewed, rejected = "source_reviewed", 9, 5
            detail = "A first-person presidential-library oral history explicitly documented transfer from the Navy to OSS and rejection of the St. John's University job offer."
        elif row == 12:
            outcome, reviewed, rejected = "source_reviewed", 8, 5
            detail = "An original OSS Detachment 101 promotion report confirmed the exact identity and enlisted service but supplied no pre-OSS occupation or employer."
        elif row == 15:
            outcome, reviewed, rejected = "source_reviewed", 8, 6
            detail = "A contemporary Indiana National Guard annual supports a probable rare-name match and 1938 private's assignment; no independent OSS bridge was found."
        elif row == 20:
            outcome, reviewed, rejected = "source_reviewed", 9, 5
            detail = "A reputable obituary supports a high-confidence exact-name OSS identity and probable Army-to-OSS pathway, while commissioning chronology and civilian employer remain unresolved."
        elif row == 22:
            outcome, reviewed, rejected = "source_reviewed", 10, 6
            detail = "Independent institutional sources support a probable rare-name economist identity and explicit 1930s Conference Board employment; the wartime agency is unnamed."
        elif row == 23:
            outcome, reviewed, rejected = "source_reviewed", 8, 6
            detail = "AFI documents a 1941 screenplay credit for the rare exact name, but no independent OSS bridge or studio employment relationship was found."
        else:
            outcome, reviewed, rejected = "no_result", 7, 6
            detail = UNRESOLVED[row]
        attempts.append(
            {
                "key": f"page473-row{row}-{slug(name)}-b965",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index and official Archives context; CIA Reading Room or equivalent official-source check; exact-name and meaningful variants; OSS, Army, Navy and rank clues; employer and occupation 1940; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Boxes 785-786; protected identifiers used only when defensible",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_965",
                "started_at": "2026-10-30T01:45:00Z",
                "completed_at": "2026-10-30T03:05:00Z",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search snippets, unsourced genealogy, people-finder pages, postwar-only leads and sources without an OSS, protected-identifier or Box-file bridge were rejected. Education, occupation categories, family adjacency and film credits were not converted into named employers. Search aliases were not treated as silent corrections.",
                "research_notes": f"{detail} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain, CIA Reading Room-equivalent and Library of Congress searches were checked as applicable. The index page, Army bulk file, technical documentation, occupation-code pages and cited original or institutional sources were inspected directly. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": "Review the indexed personnel file for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before wartime service.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b965-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-965-v1",
        "reviewer": "Before OSS Batch 965 evidence review",
        "sources": sources(),
        "organizations": organizations(),
        "affiliations": [army_affiliation(item) for item in ARMY_OCCUPATIONS]
        + specialist_affiliations(),
        "claims": claims(),
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }
    EvidenceBundle.model_validate(bundle)
    OUTPUT.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
