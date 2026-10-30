#!/usr/bin/env python3
"""Generate the reviewed Batch 986 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page483-joseph-viggiani-to-edward-virant-"
    "review_batch-986_2026-10-30.json"
)

INDEX = "nara-index-b986"
ARMY = "army-bulk-b986"
TECH = "army-tech-b986"
CODES = "army-codes-b986"
VIGNERAS = "army-history-vigneras-b986"
VILLERE = "nara-x2-villere-b986"
VILM = "medford-mail-tribune-vilm-b986"
CORNELL_1944 = "cornell-alumni-news-1944-vinciguerra-b986"
CORNELL_1993 = "cornell-alumni-news-1993-vinciguerra-b986"
VINGERS = "lacrosse-library-vingers-b986"

ORG_SMITH = "smith-college-b986"
ORG_FRENCH_ARMY = "french-army-b986"
ORG_NPS = "national-park-service-b986"
ORG_WAC = "womens-army-corps-b986"
ORG_CORNELL = "cornell-university-b986"
ORG_STUKINS = "stukins-distributing-b986"
ORG_KRAFT = "kraft-cheese-b986"


PEOPLE = {
    1: ("6f9085ff-c2a2-54f6-8ec2-217a88dcb1f7", "Joseph P Viggiani"),
    2: ("5f61bbe9-a98c-5670-8453-1de5c265b51e", "Joseph L Vigilante"),
    3: ("df1f0485-567f-5833-b0b0-2f67080c323c", "Marcel Vigneras"),
    4: ("c218bf1d-efe0-513b-bb68-ff2c95c2728c", "Edward Vignone"),
    5: ("56df289c-e56f-5592-95f3-b0b4be5c13d1", "Nick F Vigorito"),
    6: ("deec61f3-edad-5fb1-b317-eef2184557ed", "Joseph L Vigue"),
    7: ("3b20f467-2628-5548-a3c9-831fb8c122bd", "Gilberto M Vilante"),
    8: ("3e21b5fe-181b-5571-867d-0ae43c03e963", "William H Vilas"),
    9: ("71c7fd47-40ae-57e3-b04e-0fd529039894", "Joe S Villareal"),
    10: ("5f8a4e41-bba6-55fc-b3a0-232b36f135e1", "Andre L Villere"),
    11: ("d8849782-5880-557c-83eb-2d4182ae32ed", "Elizabeth E Vilm"),
    12: ("da7e8a80-a205-589c-b224-df0100bb220f", "Irving Vincent"),
    13: ("bdf2750a-14af-52c4-a95a-e2485245339d", "Stephen P Vinciguerra"),
    14: ("f870aed7-663c-5ec1-8fcd-7370ad1babeb", "Sterling N Vines"),
    15: ("438e4aaf-2eb4-5250-84d3-8f89e7df6d6d", "Noel E Vinette"),
    16: ("c9b4252e-240c-5cfc-b115-7a0cae99d101", "Harold O Vingers"),
    17: ("5342a233-a053-5580-a0ad-88c4a8dc85a4", "Jack Vinik"),
    18: ("a540b58a-56b0-5707-89c5-398a6a8fc1da", "Igor Vinner"),
    19: ("ca4f9532-b0d9-5591-8dbc-d9b78ff91aa7", "Paul Vinski"),
    20: ("5723612f-36ad-5320-8894-e6e7b7ad4bbd", "Hal D Vinson"),
    21: ("81f5edf0-f2fe-5edc-b672-e81cee13e4c2", "John H Vinson"),
    22: ("41606285-b3f2-5bb5-9589-6aff42ebb110", "Joseph E Viola"),
    23: ("721e0cdf-3b83-5a07-9096-cfa1be8acd89", "Edward J Virant"),
}


ARMY_FINDINGS = {
    1: {
        "date": "1941-08-23",
        "code": "819",
        "occupation": "Unskilled occupations in manufacture of textiles, n.e.c.",
        "public_occupation": "unskilled textile-manufacturing occupation",
        "relationship": "employment",
    },
    5: {
        "date": "1942-10-21",
        "code": "642",
        "occupation": "Semiskilled occupations in manufacture of paper goods",
        "public_occupation": "semiskilled paper-goods manufacturing occupation",
        "relationship": "employment",
    },
    6: {
        "date": "1942-10-13",
        "code": "071",
        "occupation": "Hotel and restaurant managers",
        "public_occupation": "hotel or restaurant manager",
        "relationship": "employment",
    },
    9: {
        "date": "1940-10-30",
        "code": "999",
        "occupation": None,
        "public_occupation": None,
        "relationship": "unknown",
    },
    15: {
        "date": "1944-01-18",
        "code": "992",
        "occupation": "Students (occupations not classified elsewhere)",
        "public_occupation": "student",
        "relationship": "student",
    },
    16: {
        "date": "1941-04-14",
        "code": "175",
        "occupation": "Salespersons",
        "public_occupation": "salesperson",
        "relationship": "employment",
    },
    17: {
        "date": "1941-06-26",
        "code": "105",
        "occupation": "Clerks, general office",
        "public_occupation": "general office clerk",
        "relationship": "employment",
    },
    19: {
        "date": "1942-02-22",
        "code": "475",
        "occupation": "Machinists",
        "public_occupation": "machinist",
        "relationship": "employment",
    },
    22: {
        "date": "1946-06-14",
        "code": "345",
        "occupation": None,
        "public_occupation": None,
        "relationship": "unknown",
    },
    23: {
        "date": "1943-04-03",
        "code": "892",
        "occupation": "Unskilled occupations in production of ferrous and nonferrous metals, n.e.c.",
        "public_occupation": "unskilled metal-production occupation",
        "relationship": "employment",
    },
}


UNRESOLVED = {
    2: "Exact-name, serial, OSS, occupation, obituary, social-work and institutional searches produced no reliable pre-OSS identity bridge; the later Adelphi social-worker lead remains an unbridged namesake.",
    4: "Exact-name and initial-variant searches produced an unbridged Edward L. Vignone student lead and no direct OSS or protected-identifier connection.",
    7: "Exact-name, military, obituary, employer and archival searches supplied no reliable identity or pre-OSS affiliation bridge.",
    8: "Exact-name, military, institutional, obituary and archival searches supplied no reliable identity or pre-OSS affiliation bridge.",
    12: "Baseball, motorcycle and directory namesakes could not be connected to the indexed record by rank, identifier, OSS assignment or personnel file.",
    14: "Exact-name, military, obituary, employer and archival searches supplied no reliable identity or pre-OSS affiliation bridge.",
    18: "Exact-name, transliteration, military, institutional and obituary searches supplied no reliable identity or pre-OSS affiliation bridge.",
    20: "Exact-name, rank, serial, employer, obituary and archival searches supplied no reliable identity or pre-OSS affiliation bridge.",
    21: "Exact-name, rank, serial, employer, obituary and archival searches supplied no reliable identity or pre-OSS affiliation bridge.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Box 805",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 483, rows 24-46; checked against layout-preserving text and an original-detail page render",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate; original spelling and archival context are recoverable while public identifiers are masked.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; ten protected-identifier comparisons; identifiers and record ordinals withheld",
            "access_date": "2026-10-30",
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
            "locator": "PDF physical pages 44-46; name, Army-entry-date, grade and civilian-occupation fields",
            "access_date": "2026-10-30",
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
            "locator": "PDF physical pages 171-174 and amended code-list page 304; Batch 986 categories visually and textually checked",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Codes 999 and 345 remain uninterpreted. Other historical categories identify status or broad occupation, not a named employer or exact job title.",
        },
        {
            "key": VIGNERAS,
            "stable_url": "https://www.govinfo.gov/content/pkg/GOVPUB-D114-PURL-gpo84825/pdf/GOVPUB-D114-PURL-gpo84825.pdf",
            "archival_identifier": "CMH Pub 11-6; GOVPUB-D114-PURL-gpo84825",
            "title": "Rearming the French",
            "author_creator": "Marcel Vigneras; introductory note by Hugh M. Cole",
            "repository_publisher": "Office of the Chief of Military History, Department of the Army; GovInfo",
            "publication_record_date": "1957",
            "locator": "PDF physical page 11, printed page x, Introductory Note",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "United States Army in World War II: Special Studies",
        },
        {
            "key": VILLERE,
            "stable_url": "https://www.archives.gov/files/research/jfk/releases/104-10165-10120.pdf",
            "archival_identifier": "JFK release 104-10165-10120",
            "title": "Awards and Decorations: 201 Personnel Concerned",
            "author_creator": "Office of Strategic Services, European Theater of Operations",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1945",
            "locator": "PDF physical page 123, printed page 66, X-2 Branch - 3; Unit Commander's Certificate of Merit roster",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "John F. Kennedy Assassination Records Collection",
            "document_number": "104-10165-10120",
        },
        {
            "key": VILM,
            "stable_url": "https://oregonnews.uoregon.edu/lccn/sn97071090/1944-07-18/ed-1/seq-6/ocr/",
            "archival_identifier": "Medford Mail Tribune, July 18, 1944, page 6, image 6",
            "title": "Lt. Elizabeth Vilm in Overseas Sector",
            "author_creator": "Medford Mail Tribune",
            "repository_publisher": "Medford Mail Tribune; Historic Oregon Newspapers, University of Oregon Libraries",
            "publication_record_date": "1944-07-18",
            "locator": "Page 6, image 6; article and photo caption",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Historic Oregon Newspapers",
        },
        {
            "key": CORNELL_1944,
            "stable_url": "https://hdl.handle.net/1813/27444",
            "archival_identifier": "Cornell Alumni News, volume 47, number 3",
            "title": "Cornell Alumni News",
            "author_creator": "Cornell Alumni News",
            "repository_publisher": "Cornell University",
            "publication_record_date": "1944-08-01",
            "locator": "PDF physical page 19, printed page 57; class notes naming Lieutenant Stephen P. Vinciguerra '40 in London",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Cornell University eCommons",
        },
        {
            "key": CORNELL_1993,
            "stable_url": "https://hdl.handle.net/1813/28090",
            "archival_identifier": "Cornell Alumni News, April 1993",
            "title": "Cornell Alumni News",
            "author_creator": "Cornell Alumni News",
            "repository_publisher": "Cornell University",
            "publication_record_date": "1993-04",
            "locator": "PDF physical and printed page 69; alumni family directory identifying Stephen P. Vinciguerra '40, JD '42, LLM '46",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Cornell University eCommons",
        },
        {
            "key": VINGERS,
            "stable_url": "https://archives.lacrosselibrary.org/files/2916/3914/9972/38-Cloak__Dagger_Soldier.pdf",
            "title": "Cloak & Dagger Soldier",
            "author_creator": "Jeff Rand",
            "repository_publisher": "La Crosse Public Library Archives",
            "publication_record_date": "2020",
            "locator": "PDF pages 1, 3, 5 and 7; OSS identity, 1940 employer, Army chronology, previous Kraft job and source notes",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "La Crosse Public Library Archives",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": ORG_SMITH,
            "organization_id": "8c458c45-c94a-5e4a-b1a9-693a91d9cb0c",
            "canonical_name": "Smith College",
            "historical_name": "Smith College",
            "organization_type": "college",
            "sector": "academia_and_research",
            "city": "Northampton",
            "state_or_region": "Massachusetts",
            "country": "United States",
            "normalization_notes": "Existing canonical organization reused; faculty employment remains distinct from student status.",
        },
        {
            "key": ORG_FRENCH_ARMY,
            "organization_id": "f61aed47-47ad-5e11-82be-3835d1bc4365",
            "canonical_name": "French Army",
            "historical_name": "French Army",
            "organization_type": "military service",
            "sector": "military",
            "country": "France",
            "normalization_notes": "Military assignment is not civilian employment.",
        },
        {
            "key": ORG_NPS,
            "organization_id": "46c9e5c6-dd04-5ab8-ba4d-b4c9f4aa6165",
            "canonical_name": "National Park Service",
            "historical_name": "National Park Service",
            "aliases": ["Crater Lake National Park Service"],
            "organization_type": "federal agency",
            "sector": "federal_government",
            "country": "United States",
            "normalization_notes": "The source's Crater Lake unit wording is preserved on the affiliation; the existing federal-agency organization is reused.",
        },
        {
            "key": ORG_WAC,
            "organization_id": "6de4acc9-1159-53e0-b9aa-887ba656b902",
            "canonical_name": "Women's Army Corps",
            "historical_name": "Women's Army Corps",
            "aliases": ["WAC"],
            "organization_type": "military service",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "Military assignment is not civilian employment; its exact temporal relation to OSS remains unresolved.",
        },
        {
            "key": ORG_CORNELL,
            "organization_id": "e1357e85-f9f9-5409-b56d-a75b4c3326fa",
            "canonical_name": "Cornell University",
            "historical_name": "Cornell University",
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "Ithaca",
            "state_or_region": "New York",
            "country": "United States",
            "normalization_notes": "Student status is not employment.",
        },
        {
            "key": ORG_STUKINS,
            "canonical_name": "Stukins Distributing Company",
            "historical_name": "Stukins Distributing Company",
            "organization_type": "distributor",
            "sector": "business_and_industry",
            "city": "La Crosse",
            "state_or_region": "Wisconsin",
            "country": "United States",
            "active_dates": "Active by 1940",
            "normalization_notes": "Historical name retained; no successor organization is inferred.",
        },
        {
            "key": ORG_KRAFT,
            "canonical_name": "Kraft Cheese Company",
            "historical_name": "Kraft Cheese Co.",
            "aliases": ["Kraft Cheese Co."],
            "organization_type": "food manufacturer",
            "sector": "business_and_industry",
            "country": "United States",
            "active_dates": "World War II era",
            "normalization_notes": "Historical employer wording retained; no modern corporate successor is substituted.",
        },
    ]


def occupation_affiliations() -> list[dict[str, object]]:
    values = []
    for row, item in ARMY_FINDINGS.items():
        if not item["occupation"]:
            continue
        name = PEOPLE[row][1]
        values.append(
            {
                "key": f"{slug(name)}-army-category-b986-row{row}",
                "person_id": PEOPLE[row][0],
                "occupation": item["public_occupation"],
                "relationship_type": item["relationship"],
                "end_date": item["date"],
                "date_precision": "Historical civilian-occupation category recorded at Army entry; employer, workplace and duration are not supplied",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "A_direct_official",
                "publication_status": "publish_qualified",
                "research_notes": "Official historical category only; excluded from verified-employer analytics and not narrowed beyond the code-list wording.",
            }
        )
    return values


def affiliations() -> list[dict[str, object]]:
    values = occupation_affiliations()
    values.extend(
        [
            {
                "key": "marcel-vigneras-smith-b986",
                "person_id": PEOPLE[3][0],
                "organization_key": ORG_SMITH,
                "organization_name_as_found": "Smith College",
                "role_title": "faculty member",
                "occupation": "historian and faculty member",
                "relationship_type": "employment",
                "date_precision": "Army history states that Vigneras was on the Smith faculty before World War II; exact dates are not supplied",
                "city": "Northampton",
                "state_or_region": "Massachusetts",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "A_direct_official",
                "publication_status": "published",
                "research_notes": "Best-supported last civilian employer before wartime military service; not labeled the immediate predecessor to OSS.",
            },
            {
                "key": "marcel-vigneras-french-army-b986",
                "person_id": PEOPLE[3][0],
                "organization_key": ORG_FRENCH_ARMY,
                "organization_name_as_found": "French Army",
                "role_title": "wartime service; seconded to OSS",
                "relationship_type": "military_assignment",
                "end_date": "1943",
                "date_precision": "The Army history states that he served in the French Army in both world wars and was seconded to OSS duty in 1943",
                "country": "France",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "explicit_immediate",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "A_direct_official",
                "publication_status": "published",
                "research_notes": "Military pathway, not civilian employment.",
            },
            {
                "key": "elizabeth-vilm-nps-b986",
                "person_id": PEOPLE[11][0],
                "organization_key": ORG_NPS,
                "organization_name_as_found": "Crater Lake National Park Service",
                "role_title": "assistant clerk",
                "occupation": "assistant clerk",
                "relationship_type": "employment",
                "end_date": "before WAC entry",
                "date_precision": "The contemporary article explicitly places this employment before entry into the Women's Army Corps; exact dates are not supplied",
                "city": "Crater Lake",
                "state_or_region": "Oregon",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "published",
                "research_notes": "Explicit last civilian employer before wartime service; the article does not establish when she entered OSS.",
            },
            {
                "key": "elizabeth-vilm-wac-b986",
                "person_id": PEOPLE[11][0],
                "organization_key": ORG_WAC,
                "organization_name_as_found": "WAC",
                "role_title": "second lieutenant",
                "relationship_type": "military_assignment",
                "end_date": "1944-07-18",
                "date_precision": "Contemporary article reports overseas WAC service as of publication; relation to later OSS-index context is not stated",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "temporal_relation_uncertain",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "published",
                "research_notes": "Military assignment, not civilian employment; not promoted to immediate pre-OSS status.",
            },
            {
                "key": "stephen-vinciguerra-cornell-b986",
                "person_id": PEOPLE[13][0],
                "organization_key": ORG_CORNELL,
                "organization_name_as_found": "Cornell",
                "role_title": "student; AB 1940 and JD 1942",
                "relationship_type": "student",
                "end_date": "1942",
                "date_precision": "Cornell alumni records identify the 1940 undergraduate class and 1942 law degree; no employer is supplied",
                "city": "Ithaca",
                "state_or_region": "New York",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "probable",
                "claim_confidence": "medium",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "publish_qualified",
                "research_notes": "Student status is not employment; Box 805 remains necessary to close the OSS identity bridge.",
            },
            {
                "key": "harold-vingers-stukins-b986",
                "person_id": PEOPLE[16][0],
                "organization_key": ORG_STUKINS,
                "organization_name_as_found": "Stukins Distributing Company",
                "role_title": "truck driver",
                "occupation": "truck driver",
                "relationship_type": "employment",
                "end_date": "1940",
                "date_precision": "The library history cites the 1940 census and a 1940 draft card; a later Kraft role is better supported as the final pre-service job",
                "city": "La Crosse",
                "state_or_region": "Wisconsin",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "published",
                "research_notes": "Earlier documented prewar employer; not labeled the last civilian employer because later evidence supports Kraft sales work.",
            },
            {
                "key": "harold-vingers-kraft-b986",
                "person_id": PEOPLE[16][0],
                "organization_key": ORG_KRAFT,
                "organization_name_as_found": "Kraft Cheese Co.",
                "role_title": "salesman",
                "occupation": "salesperson",
                "relationship_type": "employment",
                "end_date": "1941",
                "date_precision": "The library history reports that he returned after the war to his previous Kraft sales job; his official 1941 Army category independently records salesperson",
                "city": "La Crosse",
                "state_or_region": "Wisconsin",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "published",
                "research_notes": "Best-supported last civilian employer before Army service; the Army remained the intervening wartime pathway to OSS.",
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
    identity_assessment: str,
    temporal_assessment: str,
    source_quality: str,
    confidence: str,
    source_links: list[dict[str, str]],
    notes: str,
    affiliation_key: str | None = None,
    publication_status: str = "published",
) -> dict[str, object]:
    value: dict[str, object] = {
        "key": key,
        "person_id": PEOPLE[row][0],
        "claim_type": claim_type,
        "claim_text": claim_text,
        "evidence_paraphrase": evidence_paraphrase,
        "identity_match_assessment": identity_assessment,
        "temporal_assessment": temporal_assessment,
        "source_quality": source_quality,
        "claim_confidence": confidence,
        "publication_status": publication_status,
        "match_notes": notes,
        "sources": source_links,
    }
    if affiliation_key:
        value["affiliation_key"] = affiliation_key
    return value


def army_claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, item in ARMY_FINDINGS.items():
        name = PEOPLE[row][1]
        values.append(
            claim(
                row,
                f"identity-{slug(name)}-army-b986-row{row}",
                "identity",
                f"Indexed {name} is high-confidence matched to the official Army entry reviewed for Batch 986.",
                "The exact official name and a nonshared protected-identifier agreement support the match.",
                "High confidence from exact name and a nonshared protected identifier; the protected value and raw record are withheld.",
                "The dated Army entry precedes the later OSS-index context; the personnel file remains necessary to document the transfer sequence.",
                "A_direct_official",
                "high",
                [
                    {"source_key": INDEX},
                    {"source_key": ARMY, "locator_override": "Accepted identity bridge; protected identifier and raw record withheld"},
                ],
                "Private identifiers and raw bulk records remain absent from the evidence bundle and public output.",
            )
        )
        if not item["occupation"]:
            continue
        values.append(
            claim(
                row,
                f"occupation-{slug(name)}-b986-row{row}",
                "other_pre_oss_affiliation" if item["relationship"] == "student" else "occupation",
                f"At Army entry on {item['date']}, {name}'s historical civilian category was {str(item['occupation']).lower()}.",
                f"The official Army field carries historical code {item['code']}; NARA's code list defines it as {item['occupation']}.",
                "High confidence from the reviewed official identity bridge.",
                "Dated at Army entry before the later OSS-index context; no named employer, workplace, duration or exact OSS-transfer date is supplied.",
                "A_direct_official",
                "medium",
                [
                    {"source_key": ARMY, "locator_override": "Reviewed Army entry; raw record and identifier withheld"},
                    {"source_key": TECH, "locator_override": "PDF physical pages 44-46; civilian-occupation field"},
                    {"source_key": CODES, "locator_override": f"Historical code {item['code']}; reviewed code-list pages"},
                ],
                "Published as a qualified historical category only; excluded from verified-employer analytics.",
                f"{slug(name)}-army-category-b986-row{row}",
                "publish_qualified",
            )
        )
    return values


def special_claims() -> list[dict[str, object]]:
    return [
        claim(
            3,
            "identity-marcel-vigneras-b986",
            "identity",
            "Indexed Marcel Vigneras is high-confidence matched to the historian whom the official Army history explicitly places with OSS in 1943.",
            "The exact rare name, French Army background and explicit 1943 OSS duty align.",
            "High confidence from an exact rare name and an official biographical note explicitly naming OSS.",
            "The same note supplies the prewar faculty and wartime military sequence.",
            "A_direct_official",
            "high",
            [{"source_key": INDEX}, {"source_key": VIGNERAS}],
            "No postwar role is used to infer the pre-OSS chronology.",
        ),
        claim(
            3,
            "last-civilian-marcel-vigneras-smith-b986",
            "last_civilian_pre_service",
            "Marcel Vigneras was a Smith College faculty member before World War II.",
            "The official Army history names Smith College immediately after describing his prewar qualifications and before its wartime chronology.",
            "High-confidence exact identity from the official OSS-linked biography.",
            "Best-supported last civilian employer before wartime military service; exact employment dates are not supplied.",
            "A_direct_official",
            "high",
            [{"source_key": VIGNERAS, "locator_override": "PDF physical page 11, printed page x"}],
            "Not promoted to immediate pre-OSS employment because French Army service intervened.",
            "marcel-vigneras-smith-b986",
        ),
        claim(
            3,
            "immediate-marcel-vigneras-french-army-b986",
            "immediate_pre_oss_affiliation",
            "Marcel Vigneras's wartime French Army service was the military pathway from which he was seconded to OSS duty in 1943.",
            "The Army history states that he served in the French Army in both world wars and was seconded to OSS duty in 1943.",
            "High-confidence exact identity from the official biography.",
            "Explicit immediate military pathway; not a civilian employer.",
            "A_direct_official",
            "high",
            [{"source_key": VIGNERAS, "locator_override": "PDF physical page 11, printed page x"}],
            "Military assignment remains distinct from Smith College employment.",
            "marcel-vigneras-french-army-b986",
        ),
        claim(
            10,
            "identity-andre-villere-b986",
            "identity",
            "Indexed Pfc Andre L Villere is confirmed in an official OSS X-2 Branch merit roster.",
            "The official roster lists Pfc André L. Villere under approved Unit Commander's Certificates of Merit for X-2 Branch.",
            "Confirmed from exact full name, matching Pfc rank and direct official OSS branch context.",
            "The source establishes OSS identity but supplies no pre-OSS employer or assignment chronology.",
            "A_direct_official",
            "confirmed",
            [{"source_key": INDEX}, {"source_key": VILLERE, "locator_override": "PDF physical page 123, printed page 66"}],
            "No civilian employer is inferred from merit-award service.",
        ),
        claim(
            11,
            "identity-elizabeth-vilm-b986",
            "identity",
            "Indexed Elizabeth E Vilm is high-confidence matched to Second Lieutenant Elizabeth E. Vilm of the Women's Army Corps.",
            "The exact uncommon name and middle initial align with a contemporary article giving rank, wartime service and a pre-service employer.",
            "High confidence from the uncommon exact name, middle initial and coherent wartime chronology.",
            "The article documents pre-WAC employment and 1944 overseas service but does not state the later OSS sequence.",
            "C_reputable_contemporary_or_scholarly",
            "high",
            [{"source_key": INDEX}, {"source_key": VILM}],
            "Box 805 remains necessary to document the WAC-to-OSS chronology.",
        ),
        claim(
            11,
            "last-civilian-elizabeth-vilm-nps-b986",
            "last_civilian_pre_service",
            "Elizabeth E. Vilm was an assistant clerk for the Crater Lake National Park Service before entering the Women's Army Corps.",
            "The contemporary article explicitly names the organization, assistant-clerk role and sequence before corps entry.",
            "High-confidence uncommon-name match.",
            "Explicit last civilian employer before wartime service; not claimed as immediately pre-OSS.",
            "C_reputable_contemporary_or_scholarly",
            "high",
            [{"source_key": VILM, "locator_override": "Page 6, image 6"}],
            "The National Park Service employment and WAC assignment remain separate relationships.",
            "elizabeth-vilm-nps-b986",
        ),
        claim(
            11,
            "other-pre-oss-elizabeth-vilm-wac-b986",
            "other_pre_oss_affiliation",
            "By July 1944, Elizabeth E. Vilm was a second lieutenant serving overseas in the Women's Army Corps.",
            "The article and photo caption identify her rank, corps and overseas status.",
            "High-confidence uncommon-name match.",
            "Documented wartime military assignment; exact temporal relation to OSS remains uncertain.",
            "C_reputable_contemporary_or_scholarly",
            "high",
            [{"source_key": VILM, "locator_override": "Page 6, image 6"}],
            "Military assignment, not civilian employment.",
            "elizabeth-vilm-wac-b986",
        ),
        claim(
            13,
            "identity-stephen-vinciguerra-b986",
            "identity",
            "Indexed Captain Stephen P Vinciguerra is probably the Cornell alumnus reported as a lieutenant in London in 1944.",
            "The exact uncommon name and middle initial, officer status, Cornell chronology and London service align.",
            "Probable rather than high confidence because the alumni source does not state OSS and the rank predates the indexed captain grade.",
            "Cornell dates education through 1942 and military presence in London by 1944; no civilian employer is supplied.",
            "B_authoritative_institutional",
            "medium",
            [{"source_key": INDEX}, {"source_key": CORNELL_1944}, {"source_key": CORNELL_1993}],
            "Box 805 is required to close the identity bridge.",
            publication_status="publish_qualified",
        ),
        claim(
            13,
            "other-pre-oss-stephen-vinciguerra-cornell-b986",
            "other_pre_oss_affiliation",
            "The probable Stephen P. Vinciguerra match graduated from Cornell in 1940 and earned a Cornell law degree in 1942.",
            "Cornell alumni records identify Stephen P. Vinciguerra '40 and JD '42.",
            "Probable identity from the exact uncommon name and officer chronology.",
            "Documented prewar student status; not shown to be immediately pre-OSS and not treated as employment.",
            "B_authoritative_institutional",
            "medium",
            [{"source_key": CORNELL_1944}, {"source_key": CORNELL_1993}],
            "Student status is excluded from verified-employer analytics.",
            "stephen-vinciguerra-cornell-b986",
            "publish_qualified",
        ),
        claim(
            16,
            "other-pre-oss-harold-vingers-stukins-b986",
            "other_pre_oss_affiliation",
            "In 1940, Harold O. Vingers worked as a truck driver for Stukins Distributing Company.",
            "The library history cites the 1940 census for the occupation and a 1940 draft card for the named employer.",
            "High-confidence identity from exact name, official Army bridge and explicit OSS personnel-file context.",
            "Documented prewar employment, but later evidence supports Kraft as the final pre-service role.",
            "C_reputable_contemporary_or_scholarly",
            "high",
            [{"source_key": VINGERS, "locator_override": "PDF page 3 and source notes 12-13"}],
            "Earlier employer preserved separately from the last civilian employer.",
            "harold-vingers-stukins-b986",
        ),
        claim(
            16,
            "last-civilian-harold-vingers-kraft-b986",
            "last_civilian_pre_service",
            "Harold O. Vingers's best-supported last civilian employer before Army service was Kraft Cheese Co., where he worked as a salesman.",
            "The library history reports his postwar return to a previous Kraft sales job; the official 1941 Army category independently records salesperson.",
            "High-confidence identity from the accepted official Army bridge and the library's exact-name OSS account.",
            "Strongly date-bounded before Army service, although the source does not give the exact hiring or departure date.",
            "C_reputable_contemporary_or_scholarly",
            "high",
            [
                {"source_key": VINGERS, "locator_override": "PDF page 5 and source note 30"},
                {"source_key": ARMY, "locator_override": "Reviewed 1941 Army entry; raw record and identifier withheld"},
                {"source_key": CODES, "locator_override": "Historical code 175: Salespersons"},
            ],
            "Stukins remains visible as earlier employment; neither employer is labeled an OSS organization.",
            "harold-vingers-kraft-b986",
        ),
    ]


def claims() -> list[dict[str, object]]:
    return army_claims() + special_claims()


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
        values.append(
            base_update(
                row,
                identity_status="unresolved",
                identity_evidence=f"The visually verified page 483 row supplies {PEOPLE[row][1]}, its indexed archival context and location 230/86/42/05. {reason}",
                personnel_category="unknown_or_indeterminate",
                commissioned_officer=None,
                allied_or_foreign_personnel=False,
                research_status="requires_archival_review",
                next_action=f"Review the indexed personnel file for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}",
            )
        )

    status_by_row = {
        1: "occupation_only_found",
        5: "occupation_only_found",
        6: "occupation_only_found",
        9: "requires_archival_review",
        15: "requires_archival_review",
        16: "verified_employer_found",
        17: "occupation_only_found",
        19: "occupation_only_found",
        22: "requires_archival_review",
        23: "occupation_only_found",
    }
    for row, item in ARMY_FINDINGS.items():
        undefined = item["occupation"] is None
        values.append(
            base_update(
                row,
                identity_status="high_confidence",
                identity_evidence="The exact official name and a nonshared protected-identifier agreement support the Army identity match; the protected value remains private.",
                personnel_category="enlisted_army_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                research_status=status_by_row[row],
                next_action=(
                    f"Review the indexed personnel file to establish the Army-to-OSS chronology and interpret historical code {item['code']}; the reviewed code list does not define that value."
                    if undefined
                    else f"Review the indexed personnel file to identify any named employer behind historical code {item['code']} and establish the Army-to-OSS chronology."
                ),
                nara_catalog_id="1263923",
                archival_review_priority="medium" if row == 16 else "high",
            )
        )

    values.extend(
        [
            base_update(
                3,
                identity_status="high_confidence",
                identity_evidence="The exact rare name, French Army background and official Army history's explicit 1943 OSS duty establish a high-confidence identity.",
                personnel_category="foreign_or_allied_military_personnel",
                commissioned_officer=None,
                allied_or_foreign_personnel=True,
                research_status="verified_employer_found",
                next_action="Smith College and the French Army-to-OSS pathway are documented. Review Box 805 to refine dates and any intervening assignment.",
                archival_review_priority="medium",
            ),
            base_update(
                10,
                identity_status="confirmed",
                identity_evidence="An official OSS X-2 Branch roster lists Pfc André L. Villere with an approved Unit Commander's Certificate of Merit; exact name and rank match the index.",
                name_variants=["André L. Villere"],
                personnel_category="enlisted_army_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                research_status="requires_archival_review",
                next_action="The X-2 identity is confirmed. Review Box 805 to identify the immediate pre-OSS affiliation and last civilian employer.",
                archival_review_priority="high",
            ),
            base_update(
                11,
                identity_status="high_confidence",
                identity_evidence="The uncommon exact name and middle initial align with a contemporary article naming Second Lieutenant Elizabeth E. Vilm, her WAC service and pre-service employer.",
                personnel_category="commissioned_army_officer",
                commissioned_officer=True,
                allied_or_foreign_personnel=False,
                research_status="verified_employer_found",
                next_action="Crater Lake National Park Service is documented as the last civilian employer before WAC service. Review Box 805 to establish the WAC-to-OSS chronology.",
                archival_review_priority="medium",
            ),
            base_update(
                13,
                identity_status="probable",
                identity_evidence="The exact uncommon name and middle initial, commissioned status, Cornell chronology and London service align, but the alumni source does not explicitly state OSS.",
                personnel_category="commissioned_army_officer",
                commissioned_officer=True,
                allied_or_foreign_personnel=False,
                research_status="requires_archival_review",
                next_action="Cornell student status is documented. Review Box 805 to confirm the identity bridge and identify the immediate pre-OSS affiliation and last civilian employer after the 1942 law degree.",
                archival_review_priority="high",
            ),
        ]
    )
    return values


def research_attempts() -> list[dict[str, object]]:
    sourced = set(ARMY_FINDINGS) | {3, 10, 11, 13}
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        if row in sourced:
            outcome = "source_reviewed"
            sources_reviewed = 8 if row in {3, 10, 11, 13, 16} else 6
            rejected = 4
            detail = "Reviewed official, contemporary and institutional sources produced the identity, occupation, student, named-employer or military-pathway outcome recorded in the bundle."
        else:
            outcome = "no_result"
            sources_reviewed = 5
            rejected = 5
            detail = UNRESOLVED[row]
        attempts.append(
            {
                "key": f"page483-row{row + 23}-{slug(name)}-b986",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index context; CIA Reading Room or equivalent official-source check; exact-name and meaningful variants; OSS, rank, branch, serial and assignment clues; employer and occupation 1940; obituary, institutional, newspaper, directory and archival searches; indexed Box 805; protected identifiers used only in private official-record comparison",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_986",
                "started_at": "2026-10-30T13:30:00Z",
                "completed_at": "2026-10-30T14:55:00Z",
                "outcome": outcome,
                "sources_reviewed": sources_reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, snippets, commercial people-finder pages, relatives, unsourced genealogy, postwar-only leads and sources without an OSS, protected-identifier, rank, unit or personnel-file bridge were rejected. Historical occupation categories, student status and military assignments were not converted into employers.",
                "research_notes": f"{detail} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain and archival searches were checked as applicable. The index page, official Army comparison, technical field definitions and cited code-list pages were inspected directly. Relevant Army-history, NARA X-2, Cornell Alumni News and La Crosse Library PDF pages were checked against rendered images. No search-result snippet was used as sole final evidence, no paywall or access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": "Review the indexed personnel file for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before wartime service.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b986-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-986-v1",
        "reviewer": "Before OSS Batch 986 evidence review",
        "sources": sources(),
        "organizations": organizations(),
        "affiliations": affiliations(),
        "claims": claims(),
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }
    EvidenceBundle.model_validate(bundle)
    OUTPUT.write_text(
        json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
