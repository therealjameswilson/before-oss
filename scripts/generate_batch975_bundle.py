#!/usr/bin/env python3
"""Generate the reviewed Batch 975 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page478-henry-untermeyer-to-robert-vacasovich-"
    "review_batch-975_2026-10-30.json"
)

INDEX = "nara-index-b975"
ARMY = "army-bulk-b975"
TECH = "army-tech-b975"
CODES = "army-codes-b975"
UNTERMEYER_PROFILE = "broadcasting-henry-untermeyer-b975"
UPDIKE_GAO = "gao-furman-updike-b975"
URSIN_OBIT = "washington-post-paul-ursin-b975"
URSIN_FSJ = "foreign-service-journal-paul-ursin-b975"
USSACHEVSKY_FINDING_AID = "columbia-ussachevsky-finding-aid-b975"
USSACHEVSKY_PAPER = "unt-ussachevsky-paper-b975"
USUDA_ORDER = "jhcny-oss-usuda-travel-order-b975"

WABC = "wabc-cbs-b975"
US_ARMY = "us-army-b975"
STATE = "state-department-b975"
PASADENA_JC = "pasadena-junior-college-b975"
ROOSEVELT_HIGH = "roosevelt-high-los-angeles-b975"


PEOPLE = {
    1: ("ba2f4d84-a0f3-5e25-922f-6877669645d2", "Henry Untermeyer"),
    2: ("2f876bbf-66eb-53c1-b830-87ffd9323af3", "Furman H Updike"),
    3: ("7a1139da-0ce0-5bc6-9a3f-5d20b8981ee0", "George A Upperman"),
    4: ("6c54eb25-eb8c-5993-8f79-5c681eb61cf9", "Thomas G Upton"),
    5: ("60d6aa53-3a02-56ed-ad54-3347b4918ae9", "George S Ura"),
    6: ("f03fb629-1dc6-5031-a484-160ec8130861", "John W Urban"),
    7: ("ddbdf47a-b4e6-5fdf-a90e-ec5c9ae69a0c", "Louis Urbano"),
    8: ("7c0c0f78-8e5d-533b-9278-6d0e9e03984e", "Louis J Urbanski"),
    9: ("753f57cf-1935-5b71-bd36-8a892f15b678", "Sigfried Urdal"),
    10: ("5ad6dc81-8af9-5abb-a229-3345b8e3d942", "Maurice Urdang"),
    11: ("e41ca66f-b26c-59c2-a168-ea4a2bc02c2d", "Paul M Ursin"),
    12: ("b4895c56-bf22-58af-b1e7-c2cc6787a4d0", "Joseph Ursiny"),
    13: ("af9b0355-8b6f-5c2a-90d4-648a982e909e", "George H Usher"),
    14: ("a527f98e-c2c8-51d2-863a-85c811a4a9e2", "Martha E Usher"),
    15: ("da946194-40b9-5bc7-be24-023ceb6646bb", "Richard E Usher"),
    16: ("0fc49d3a-dfbe-57d3-8152-475b9cecb1aa", "Richard E Usher"),
    17: ("a33336a7-5b2a-513d-a5c2-ed3499ee4ad6", "Vladimir Ussachevsky"),
    18: ("f48526a4-8ee2-5232-8d00-2930b2ec3f57", "Yoshisada Usuda"),
    19: ("caacaa5f-df72-57df-95ad-e93ad5c58f0f", "James C Utrecht"),
    20: ("8e55df97-f557-53d9-bd5f-14c8778f208a", "Anton S Utz"),
    21: ("128fcc95-79fa-5d1f-8893-90ba9c5defb6", "Stella T Uzdawinis"),
    22: ("a8306d70-3613-59d0-b9f2-0abc9384ab1c", "E V Uzes"),
    23: ("e10018a7-307f-5664-aae2-46b50fc9576c", "Robert Vacasovich"),
}


ARMY_OCCUPATIONS = [
    {
        "row": 3,
        "date": "1945-04-27",
        "code": "137",
        "occupation": "Stenographers and typists",
        "public_occupation": "stenographer or typist",
        "relationship_type": "unknown",
        "temporal_basis": "temporal_relation_uncertain",
        "locator": "PDF physical page 171; category 1-37 Stenographers and typists",
    },
    {
        "row": 7,
        "date": "1942-11-30",
        "code": "134",
        "occupation": "Shipping and receiving clerks",
        "public_occupation": "shipping or receiving clerk",
        "relationship_type": "unknown",
        "temporal_basis": "documented_prewar",
        "locator": "PDF physical page 171; category 1-34 Shipping and receiving clerks",
    },
    {
        "row": 9,
        "date": "1941-01-27",
        "code": "948",
        "occupation": "Sailors and deckhands, except U.S. Navy",
        "public_occupation": "sailor or deckhand outside the U.S. Navy",
        "relationship_type": "unknown",
        "temporal_basis": "documented_prewar",
        "locator": "PDF physical page 172; category 9-48 Sailors and deckhands, except U.S. Navy",
    },
    {
        "row": 10,
        "date": "1943-07-14",
        "code": "097",
        "occupation": "Managers and officials, not elsewhere classified",
        "public_occupation": "manager or official, not elsewhere classified",
        "relationship_type": "unknown",
        "temporal_basis": "documented_prewar",
        "locator": "PDF physical page 171; category 0-97 Managers and officials, n.e.c.",
    },
    {
        "row": 19,
        "date": "1942-09-09",
        "code": "992",
        "occupation": "Students",
        "public_occupation": "student",
        "relationship_type": "student",
        "temporal_basis": "documented_prewar",
        "locator": "Corrected Code No. 30, PDF physical page 304; category 9-92 Students",
    },
]


UNRESOLVED = {
    4: "A short officer-style identifier did not yield an eligible exact Army bulk match, and exact-name military, obituary, institutional and archival searches did not bridge Thomas G Upton to a pre-OSS affiliation.",
    5: "A pre-evacuation California directory names George S Ura, while separate Japanese American veteran and relocation records use George Ura or George Masaru Ura; none links the indexed person to Box 795 or an employer, and the middle-name evidence conflicts.",
    6: "The short identifier was outside the eligible Army bulk pattern, and the common name John W Urban produced no source with two corroborating identifiers beyond the name.",
    12: "Exact-name and surname-variant OSS, military, occupation, obituary, newspaper and archival searches produced no defensible identity bridge for Joseph Ursiny.",
    13: "The common name George H Usher produced unrelated namesakes and no two corroborating identifiers beyond the name.",
    14: "Exact-name, military, employment, obituary, institutional and archival searches did not establish Martha E Usher's identity or pre-OSS affiliation.",
    16: "This is the second of two separately printed Richard E Usher rows. Its different protected identifier produced no Army bulk candidate, so the two rows remain separate pending Box 795 review.",
    20: "Exact-name and variant military, employment, obituary, newspaper and archival searches produced no defensible identity bridge for Anton S Utz.",
    22: "The initials-only name E V Uzes produced geographic false positives and no defensible OSS identity, occupation or employer evidence.",
    23: "Exact-name and Vacasovich/Vakasovich/Vukasovich variant searches produced no defensible OSS, military, occupation, obituary or institutional identity bridge for Robert Vacasovich.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 794-796",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 478, rows 1-23; checked against layout-preserving text and an original-detail page render",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. The two Richard E Usher rows have different protected identifiers and are not merged.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; eight Batch 975 identity comparisons; protected identifiers and record ordinals withheld",
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
            "locator": "PDF physical pages 171-172 and corrected page 304; Batch 975 categories visually and textually checked",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical categories identify neither employers nor workplaces and are retained only where needed for auditability.",
        },
        {
            "key": UNTERMEYER_PROFILE,
            "stable_url": "https://www.worldradiohistory.com/Archive-All-BC/Broadcasting-Magazine/BC-1957/1957-09-23-BC.pdf",
            "title": "Our Respects to Henry Untermeyer",
            "author_creator": "Broadcasting-Telecasting staff",
            "repository_publisher": "Broadcasting Publications; preserved by World Radio History",
            "publication_record_date": "1957-09-23",
            "locator": "Page 22; education, 1937-1941 WABC/CBS work and 1941-1946 Army chronology",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Broadcasting-Telecasting magazine archive",
            "rights_notes": "Contemporary trade profile; only concise paraphrases and short excerpts are retained.",
        },
        {
            "key": UPDIKE_GAO,
            "stable_url": "https://www.gao.gov/products/b-121663",
            "archival_identifier": "B-121663; 36 Comp. Gen. 210",
            "title": "B-121663, September 14, 1956, 36 Comp. Gen. 210",
            "author_creator": "Comptroller General of the United States",
            "repository_publisher": "U.S. Government Accountability Office",
            "publication_record_date": "1956-09-14",
            "locator": "Decision paragraphs naming Furman H. Updike as an Army officer and later major",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "Comptroller General decisions",
            "document_number": "B-121663",
        },
        {
            "key": URSIN_OBIT,
            "stable_url": "https://www.washingtonpost.com/archive/local/1990/12/14/house-committee-director-david-c-sharman-67-dies/8ee21bdf-3d3f-43aa-9bb1-d3d5577bb009/",
            "title": "Paul M. Ursin: Defense Intelligence Agency Specialist",
            "author_creator": "The Washington Post obituary staff",
            "repository_publisher": "The Washington Post",
            "publication_record_date": "1990-12-14",
            "locator": "Paul M. Ursin obituary section; Prague diplomatic work and OSS London service",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Washington Post local obituaries",
        },
        {
            "key": URSIN_FSJ,
            "stable_url": "https://afsa.org/sites/default/files/fsj-1941-01-january_0.pdf",
            "title": "The Foreign Service Journal, January 1941",
            "author_creator": "American Foreign Service Association",
            "repository_publisher": "American Foreign Service Association",
            "publication_record_date": "1941-01",
            "locator": "Page 59, Department visitors: Paul M. Ursin, Jr., Prague",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Foreign Service Journal archive",
        },
        {
            "key": USSACHEVSKY_FINDING_AID,
            "stable_url": "https://findingaids.library.columbia.edu/pdf/cul-7583223.pdf",
            "archival_identifier": "Columbia University Libraries collection 7583223",
            "title": "Vladimir Ussachevsky papers, 1932-1969",
            "author_creator": "Jude Webre",
            "repository_publisher": "Rare Book and Manuscript Library, Columbia University Libraries",
            "publication_record_date": "2010-02; revised 2019-05-20",
            "locator": "Biographical note, page 4; Box 3, Folder 6, Pasadena Junior College and Roosevelt High, 1940-1942",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Vladimir Ussachevsky papers",
        },
        {
            "key": USSACHEVSKY_PAPER,
            "stable_url": "https://digital.library.unt.edu/ark:/67531/metadc801972/m2/1/high_res_d/SmokingGun%20evidence%20paper.pdf",
            "archival_identifier": "UNT Digital Library metadc801972",
            "title": "The Smoking Gun: Evidence that Vladimir Ussachevsky used Chinese Timbres as the Basis for his Electronic Music, Expanded Edition",
            "author_creator": "Carl Rahkonen and Ralph Hartsock",
            "repository_publisher": "University of North Texas Digital Library",
            "publication_record_date": "2015",
            "locator": "PDF pages 4-5; Los Angeles and Pasadena teaching, Army induction and August 1944 assignment to OSS",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "UNT Digital Library",
        },
        {
            "key": USUDA_ORDER,
            "stable_url": "https://www.historyofjapaneseinny.org/wp-content/uploads/2024/05/OFFICE-OF-STRATEGIC-SERVICES-1.pdf",
            "archival_identifier": "OSS Headquarters travel order 370.5 (27 Apr 45), corrected copy",
            "title": "Invitational Travel Orders, Shipment IJ-B857-HY",
            "author_creator": "Headquarters and Headquarters Detachment, Office of Strategic Services",
            "repository_publisher": "Japan History Council of New York",
            "publication_record_date": "1945-04-30",
            "locator": "Corrected travel order, paragraph 1; Yoshisada Katoi Usuda among named civilian OSS employees",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "History of Japanese in New York research documents",
            "document_number": "Shipment IJ-B857-HY",
            "rights_notes": "Digitized reproduction of an OSS travel order; used for identity and personnel status, not a pre-OSS employer.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": WABC,
            "canonical_name": "WABC (CBS-owned New York radio station)",
            "historical_name": "WABC",
            "aliases": ["CBS-owned WABC", "WCBS"],
            "organization_type": "radio station",
            "sector": "journalism_and_media",
            "city": "New York",
            "state_or_region": "New York",
            "country": "United States",
            "active_dates": "1928-1946 under the WABC call sign",
            "normalization_notes": "The 1937-1941 historical station name is preserved. The station became WCBS in 1946; the later name is an alias, not substituted into the prewar claim.",
        },
        {
            "key": US_ARMY,
            "organization_id": "24facf23-e75a-54f2-a37a-0ef1509bc18a",
            "canonical_name": "United States Army",
            "historical_name": "U.S. Army",
            "aliases": ["Army of the United States"],
            "organization_type": "military_service",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "Reuses the reviewed canonical organization; modeled separately from civilian employment and from OSS duty.",
        },
        {
            "key": STATE,
            "organization_id": "4d2fbb5f-218d-5445-b7b3-4c2fd22f0286",
            "canonical_name": "United States Department of State",
            "historical_name": "Department of State",
            "aliases": ["U.S. Department of State"],
            "organization_type": "federal executive department",
            "sector": "federal_government",
            "country": "United States",
            "normalization_notes": "Reuses the reviewed canonical organization. Embassy and consular work is a government assignment, not a private employer.",
        },
        {
            "key": PASADENA_JC,
            "canonical_name": "Pasadena Junior College",
            "historical_name": "Pasadena Junior College",
            "aliases": ["PJC"],
            "organization_type": "public junior college",
            "sector": "academia_and_research",
            "city": "Pasadena",
            "state_or_region": "California",
            "country": "United States",
            "normalization_notes": "The historical employer name is preserved; no modern institution name is substituted.",
        },
        {
            "key": ROOSEVELT_HIGH,
            "canonical_name": "Roosevelt High School (Los Angeles)",
            "historical_name": "Roosevelt High",
            "aliases": ["Theodore Roosevelt High School"],
            "organization_type": "public high school",
            "sector": "academia_and_research",
            "city": "Los Angeles",
            "state_or_region": "California",
            "country": "United States",
            "normalization_notes": "The Columbia finding aid names Roosevelt High; the UNT paper independently places Ussachevsky in the Los Angeles public schools.",
        },
    ]


def occupation_affiliation(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    name = PEOPLE[row][1]
    return {
        "key": f"{slug(name)}-occupation-b975",
        "person_id": PEOPLE[row][0],
        "organization_name_as_found": None,
        "role_title": None,
        "occupation": str(item["public_occupation"]),
        "relationship_type": str(item["relationship_type"]),
        "end_date": str(item["date"]),
        "date_precision": "Army entry date; the historical occupation field names no employer or workplace",
        "country": "United States",
        "immediate_pre_oss": False,
        "last_civilian_pre_service": False,
        "pre_oss_temporal_basis": str(item["temporal_basis"]),
        "identity_confidence": "high_confidence",
        "claim_confidence": "medium",
        "source_quality": "A_direct_official",
        "publication_status": "publish_qualified",
        "research_notes": "Historical Army-entry occupation only; excluded from verified-employer analytics.",
    }


def affiliations() -> list[dict[str, object]]:
    values = [occupation_affiliation(item) for item in ARMY_OCCUPATIONS]
    values.extend(
        [
            {
                "key": "henry-untermeyer-wabc-b975",
                "person_id": PEOPLE[1][0],
                "organization_key": WABC,
                "organization_name_as_found": "CBS-owned WABC (later WCBS)",
                "role_title": "writer, reporter, editor, producer and program operations manager",
                "occupation": "radio writer and program employee",
                "relationship_type": "employment",
                "start_date": "1937",
                "end_date": "1941",
                "date_precision": "The contemporary trade profile says he joined the station in 1937 and was called to active Army duty in 1941",
                "city": "New York",
                "state_or_region": "New York",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "published",
                "research_notes": "Last documented civilian employer before active Army duty. The source does not state the exact OSS accession date.",
            },
            {
                "key": "henry-untermeyer-army-b975",
                "person_id": PEOPLE[1][0],
                "organization_key": US_ARMY,
                "organization_name_as_found": "U.S. Army Reserve",
                "role_title": "officer; Second Corps Area aide and later Army radio public-relations liaison",
                "occupation": "Army officer",
                "relationship_type": "military_assignment",
                "start_date": "1941",
                "end_date": "1946",
                "date_precision": "The profile describes a 1941-1946 military hiatus from CBS and several assignments, but not the exact OSS duty",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "temporal_relation_uncertain",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "published",
                "research_notes": "Military pathway is separate from civilian WABC employment. Box 794 must establish how Army and OSS assignments intersected.",
            },
            {
                "key": "paul-ursin-prague-state-b975",
                "person_id": PEOPLE[11][0],
                "organization_key": STATE,
                "organization_name_as_found": "U.S. Embassy in Prague and later the American consulate",
                "role_title": None,
                "occupation": "diplomatic-post employee",
                "relationship_type": "government_assignment",
                "end_date": "1940-10",
                "date_precision": "The obituary says he began work while a graduate student and moved to Washington after the consulate closed in October 1940",
                "city": "Prague",
                "country": "Czechoslovakia",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "published",
                "research_notes": "Named prewar government affiliation. The accessible sources do not identify his Washington role between October 1940 and OSS London service.",
            },
            {
                "key": "ussachevsky-pasadena-jc-b975",
                "person_id": PEOPLE[17][0],
                "organization_key": PASADENA_JC,
                "organization_name_as_found": "Pasadena Junior College",
                "role_title": "evening music instructor",
                "occupation": "music teacher",
                "relationship_type": "employment",
                "start_date": "1940",
                "end_date": "1942-09",
                "date_precision": "The finding aid dates Pasadena Junior College and Roosevelt High materials 1940-1942; the scholarly paper says he taught evening classes before September 1942 induction",
                "city": "Pasadena",
                "state_or_region": "California",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Concurrent with Los Angeles public-school teaching and immediately before Army induction, not immediately before OSS assignment.",
            },
            {
                "key": "ussachevsky-roosevelt-high-b975",
                "person_id": PEOPLE[17][0],
                "organization_key": ROOSEVELT_HIGH,
                "organization_name_as_found": "Roosevelt High",
                "role_title": "music teacher",
                "occupation": "music teacher",
                "relationship_type": "employment",
                "start_date": "1940",
                "end_date": "1942-09",
                "date_precision": "The finding aid dates Roosevelt High materials 1940-1942; the scholarly paper independently describes Los Angeles public-school music teaching before induction",
                "city": "Los Angeles",
                "state_or_region": "California",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Concurrent with Pasadena Junior College evening teaching and immediately before Army induction.",
            },
            {
                "key": "ussachevsky-us-army-b975",
                "person_id": PEOPLE[17][0],
                "organization_key": US_ARMY,
                "organization_name_as_found": "U.S. Army",
                "role_title": "servicemember assigned to OSS as a Far East research analyst",
                "occupation": "military research analyst",
                "relationship_type": "military_assignment",
                "start_date": "1942-09-28",
                "end_date": "1945-11-07",
                "date_precision": "Exact induction and discharge dates are supplied; the Army assignment to OSS began in August 1944",
                "city": "Washington",
                "state_or_region": "District of Columbia",
                "country": "United States",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "explicit_immediate",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "published",
                "research_notes": "The Army is the immediate pre-OSS affiliation because the source explicitly says the Army assigned him to OSS. It is not a civilian employer.",
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
    evidence_excerpt: str | None = None,
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
    if evidence_excerpt:
        value["evidence_excerpt"] = evidence_excerpt
    return value


def army_identity_note(row: int) -> str:
    name = PEOPLE[row][1]
    if row == 9:
        return (
            "The official Army row agrees on the uncommon surname and a nonshared protected identifier; "
            "Sigfred differs from indexed Sigfried by one omitted vowel and is retained as a variant."
        )
    return (
        f"The official Army bulk row has the exact indexed full name {name} and an exact, "
        "nonshared protected-identifier agreement. The identifier and raw record ordinal remain private."
    )


def army_claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for item in ARMY_OCCUPATIONS:
        row = int(item["row"])
        name = PEOPLE[row][1]
        values.append(
            claim(
                row,
                f"identity-{slug(name)}-army-b975",
                "identity",
                f"Indexed {name} is high-confidence matched to the official Army entry used for the dated occupation finding.",
                "The official Army name comparison and a nonshared protected identifier support the match; the private identifier is not published.",
                army_identity_note(row),
                "The Army entry date is preserved separately from the later OSS-index context.",
                "A_direct_official",
                "high",
                [{"source_key": INDEX}, {"source_key": ARMY, "locator_override": "Accepted identity bridge; protected identifier and raw record withheld"}],
                "Protected identifiers were used only for private resolution and remain absent from the evidence bundle and public output.",
            )
        )
        values.append(
            claim(
                row,
                f"occupation-{slug(name)}-b975",
                "occupation",
                f"At Army entry on {item['date']}, {name}'s historical civilian-occupation category was {str(item['occupation']).lower()}.",
                f"The official Army field carries historical code {item['code']}; NARA's code list defines it as {item['occupation']}.",
                army_identity_note(row),
                (
                    "Dated at Army entry before the later OSS-index context; no named employer, workplace or exact OSS-transfer date is supplied."
                    if item["temporal_basis"] == "documented_prewar"
                    else "Dated at Army entry in 1945; the evidence does not establish whether this status preceded or overlapped OSS service."
                ),
                "A_direct_official",
                "medium",
                [
                    {"source_key": ARMY, "locator_override": "Accepted identity bridge; protected identifier and raw record withheld"},
                    {"source_key": TECH, "locator_override": "PDF physical pages 44-46; civilian-occupation field"},
                    {"source_key": CODES, "locator_override": str(item["locator"])},
                ],
                "Published as qualified occupation or student status only; excluded from verified-employer analytics.",
                f"{slug(name)}-occupation-b975",
                "publish_qualified",
            )
        )

    values.append(
        claim(
            8,
            "identity-louis-j-urbanski-army-b975",
            "identity",
            "Indexed Louis J Urbanski is high-confidence matched to an official Army entry with the same full name and a nonshared protected identifier.",
            "The official Army name and protected identifier agree; the row records a 1946 Army entry and technical-sergeant grade.",
            army_identity_note(8),
            "The 1946 entry is postwar and is used only for identity and enlisted classification; it does not establish a pre-OSS affiliation.",
            "A_direct_official",
            "high",
            [{"source_key": INDEX}, {"source_key": ARMY, "locator_override": "Accepted identity bridge; protected identifier and raw record withheld"}],
            "Historical code 177 was not found in the inspected NARA occupation list and is not interpreted or published.",
        )
    )
    return values


def special_claims() -> list[dict[str, object]]:
    return [
        claim(
            1,
            "identity-henry-untermeyer-b975",
            "identity",
            "Indexed Henry Untermeyer is high-confidence matched to the Cornell graduate, CBS radio employee and Army officer profiled in Broadcasting-Telecasting.",
            "The uncommon exact name, 1936 Cornell education and 1941-1946 Army hiatus provide a coherent identity and wartime chronology.",
            "High confidence from the rare exact name and a detailed contemporary occupational and military profile consistent with the OSS personnel-file context.",
            "The profile dates WABC employment before Army duty but does not state the exact OSS assignment.",
            "C_reputable_contemporary_or_scholarly",
            "high",
            [{"source_key": INDEX}, {"source_key": UNTERMEYER_PROFILE}],
            "The later WCBS and KCBS career is used for identity context only, not projected backward.",
        ),
        claim(
            1,
            "last-civilian-henry-untermeyer-wabc-b975",
            "last_civilian_pre_service",
            "CBS-owned WABC was Henry Untermeyer's last documented civilian employer before active Army duty in 1941.",
            "The trade profile says he joined WABC in 1937, served in several program roles for nearly four years, and entered active Army duty in 1941.",
            "High-confidence uncommon-name match with a continuous education, employment, service and postwar-return chronology.",
            "Strongly date-bounded immediately before military service; the source does not claim direct recruitment from WABC into OSS.",
            "C_reputable_contemporary_or_scholarly",
            "high",
            [{"source_key": UNTERMEYER_PROFILE, "excerpt_override": "For nearly four years he served in the WCBS program department as reporter, editor, producer and, finally, program operations manager."}],
            "Historical WABC is preserved even though the retrospective profile uses the later WCBS name parenthetically.",
            "henry-untermeyer-wabc-b975",
        ),
        claim(
            1,
            "wartime-henry-untermeyer-army-b975",
            "other_pre_oss_affiliation",
            "Henry Untermeyer's wartime pathway was commissioned U.S. Army service beginning in 1941; the exact relationship between his Army assignments and OSS remains unresolved.",
            "The profile says Lieutenant Untermeyer entered active duty in 1941, later served as a major and left active wartime service in 1946 as a lieutenant colonel in the Army Reserve.",
            "High-confidence uncommon-name match supported by a detailed contemporary profile.",
            "The Army interval spans the OSS years, but no reviewed source establishes whether it preceded or overlapped a specific OSS assignment.",
            "C_reputable_contemporary_or_scholarly",
            "medium",
            [{"source_key": UNTERMEYER_PROFILE}],
            "Published with explicit temporal qualification and excluded from immediate-affiliation analytics.",
            "henry-untermeyer-army-b975",
            "publish_qualified",
        ),
        claim(
            2,
            "identity-furman-h-updike-b975",
            "identity",
            "Indexed Furman H Updike is high-confidence matched to the Army officer and later major named in a U.S. Comptroller General decision.",
            "The uncommon exact full name and matching Army-officer context support the identity; the official decision documents active-duty release in 1948.",
            "High confidence from the rare exact name, matching middle initial and authoritative Army-officer context.",
            "The decision is postwar and supplies no pre-OSS employer or assignment sequence.",
            "A_direct_official",
            "high",
            [{"source_key": INDEX}, {"source_key": UPDIKE_GAO}],
            "The decision supports identity and commissioned status only; disability details are neither relevant nor reproduced on the profile.",
        ),
        claim(
            11,
            "identity-paul-m-ursin-b975",
            "identity",
            "Indexed Paul M Ursin is high-confidence matched to the Prague diplomatic-post employee who later served with OSS in London.",
            "The exact uncommon name and middle initial, Prague chronology and explicit OSS London service align; a contemporary Foreign Service Journal entry corroborates the Prague connection.",
            "High confidence from the rare exact name, middle initial, Charles University and Prague diplomatic-post chronology, and explicit OSS London service.",
            "The sources establish prewar Prague work and later OSS service but leave his October 1940-to-OSS Washington chronology incomplete.",
            "C_reputable_contemporary_or_scholarly",
            "high",
            [{"source_key": INDEX}, {"source_key": URSIN_OBIT}, {"source_key": URSIN_FSJ, "support_type": "context_only"}],
            "No later Army Map Service or Defense Intelligence Agency role is projected backward.",
        ),
        claim(
            11,
            "other-paul-ursin-prague-b975",
            "other_pre_oss_affiliation",
            "Paul M. Ursin worked at the U.S. Embassy in Prague and later the American consulate before moving to Washington after the consulate closed in October 1940.",
            "The obituary supplies the work sequence; the January 1941 Foreign Service Journal independently lists Paul M. Ursin, Jr., with Prague.",
            "High-confidence exact-name and Prague/OSS chronology match.",
            "Documented prewar government assignment; not marked immediate because the Washington interval before OSS is unknown.",
            "C_reputable_contemporary_or_scholarly",
            "high",
            [{"source_key": URSIN_OBIT, "excerpt_override": "he began working at the U.S. Embassy there and later at the American consulate"}, {"source_key": URSIN_FSJ, "support_type": "context_only"}],
            "Government assignment remains distinct from private civilian employment.",
            "paul-ursin-prague-state-b975",
        ),
        claim(
            17,
            "identity-vladimir-ussachevsky-b975",
            "identity",
            "Indexed Vladimir Ussachevsky is high-confidence matched to the composer whom the U.S. Army assigned to OSS as a Far East research analyst in August 1944.",
            "The exceptionally distinctive exact name, education and teaching history align with a scholarly chronology that explicitly states his Army-to-OSS assignment.",
            "High confidence from the rare exact name, complete chronological fit, institutional finding aid and explicit Army assignment to OSS.",
            "Teaching ended before September 1942 induction; the Army assigned him to OSS in August 1944.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": INDEX}, {"source_key": USSACHEVSKY_FINDING_AID}, {"source_key": USSACHEVSKY_PAPER}],
            "Postwar State Department, Putney School and Columbia work is not used as pre-OSS evidence.",
        ),
        claim(
            17,
            "last-civilian-ussachevsky-pasadena-b975",
            "last_civilian_pre_service",
            "Pasadena Junior College was one of Vladimir Ussachevsky's two concurrent last civilian employers before Army induction.",
            "The scholarly paper says he taught evening classes there; the finding aid dates the relevant teaching materials 1940-1942.",
            "High-confidence rare-name match with independent institutional and scholarly corroboration.",
            "Strongly date-bounded before September 1942 induction; Army service intervened before OSS assignment.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": USSACHEVSKY_FINDING_AID}, {"source_key": USSACHEVSKY_PAPER, "excerpt_override": "teaching evening classes at Pasadena Junior College"}],
            "Teaching is employment, not student status; concurrent Los Angeles public-school work remains separate.",
            "ussachevsky-pasadena-jc-b975",
        ),
        claim(
            17,
            "last-civilian-ussachevsky-roosevelt-b975",
            "last_civilian_pre_service",
            "Roosevelt High in the Los Angeles public schools was one of Vladimir Ussachevsky's two concurrent last civilian employers before Army induction.",
            "The finding aid names Roosevelt High and dates the materials 1940-1942; the scholarly paper independently says he taught music in Los Angeles public schools.",
            "High-confidence rare-name match with independent institutional and scholarly corroboration.",
            "Strongly date-bounded before September 1942 induction; Army service intervened before OSS assignment.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": USSACHEVSKY_FINDING_AID, "excerpt_override": "Pasadena Junior College and Roosevelt High, 1940-1942"}, {"source_key": USSACHEVSKY_PAPER}],
            "The historical school is retained separately from the district and from Pasadena Junior College.",
            "ussachevsky-roosevelt-high-b975",
        ),
        claim(
            17,
            "immediate-ussachevsky-army-b975",
            "immediate_pre_oss_affiliation",
            "The U.S. Army was Vladimir Ussachevsky's immediate affiliation before his August 1944 assignment to OSS as a Far East research analyst.",
            "The scholarly chronology gives his 1942 induction, subsequent Army training and the Army's August 1944 assignment to OSS.",
            "High-confidence rare-name and complete wartime-chronology match.",
            "Explicitly immediate: the source says the Army assigned him to OSS.",
            "C_reputable_contemporary_or_scholarly",
            "high",
            [{"source_key": USSACHEVSKY_PAPER, "excerpt_override": "the Army assigned Ussachevsky to the Office of Strategic Services in Washington D.C."}],
            "Military assignment is not labeled a civilian employer.",
            "ussachevsky-us-army-b975",
        ),
        claim(
            18,
            "identity-yoshisada-katoi-usuda-b975",
            "identity",
            "Indexed Yoshisada Usuda is high-confidence matched to Yoshisada Katoi Usuda, a civilian OSS employee named in an April 1945 travel order.",
            "The rare exact first and last name align with an OSS travel order that adds the middle name Katoi and explicitly classifies the listed people as civilian employees.",
            "High confidence from the exceptionally rare exact name and specific contemporary OSS order; Box 795 should confirm the middle-name spelling.",
            "The order establishes OSS employment in April 1945 but supplies no pre-OSS employer.",
            "C_reputable_contemporary_or_scholarly",
            "high",
            [{"source_key": INDEX}, {"source_key": USUDA_ORDER, "excerpt_override": "Yoshisada Katoi Usuda"}],
            "A different Yoshisada Karlo Usuda embassy lead was rejected because its wartime internment chronology conflicts with this civilian OSS order.",
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
    values = []
    for row, reason in UNRESOLVED.items():
        box = "796" if row == 23 else "795"
        possible_group = "duplicate-b975-richard-e-usher" if row == 16 else None
        values.append(
            base_update(
                row,
                identity_status="ambiguous" if row in {5, 16} else "unresolved",
                identity_evidence=f"The visually verified index row supplies {PEOPLE[row][1]}, Box {box} and archive location 230/86/42/04. {reason}",
                personnel_category="unknown_or_indeterminate",
                commissioned_officer=None,
                allied_or_foreign_personnel=None,
                possible_duplicate_group=possible_group,
                research_status="requires_archival_review",
                next_action=f"Review Box {box} for corroborating identifiers, immediate pre-OSS affiliation and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}",
                archival_review_priority="critical" if row in {5, 16} else "high",
            )
        )

    for row in [3, 7, 9, 10, 19]:
        temporal_note = " The 1945 Army-entry date does not establish whether the occupation preceded or overlapped OSS service." if row == 3 else ""
        values.append(
            base_update(
                row,
                identity_status="high_confidence",
                identity_evidence=army_identity_note(row),
                name_variants=["Sigfred Urdal"] if row == 9 else None,
                personnel_category="enlisted_army_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                research_status="occupation_only_found",
                next_action=f"Review Box 795 to establish the immediate pre-OSS affiliation and named last civilian employer; do not convert the Army occupation category into a workplace.{temporal_note}",
            )
        )

    values.extend(
        [
            base_update(
                1,
                identity_status="high_confidence",
                identity_evidence="The uncommon exact name matches a detailed contemporary profile of the 1936 Cornell graduate, 1937-1941 CBS radio employee and 1941-1946 commissioned Army officer.",
                personnel_category="commissioned_army_officer",
                commissioned_officer=True,
                allied_or_foreign_personnel=False,
                research_status="documented_prewar_employer_found",
                next_action="Review Box 794 to establish the exact OSS assignment and whether Army service preceded or overlapped that duty; WABC remains the last documented civilian employer before active service.",
                archival_review_priority="medium",
            ),
            base_update(
                2,
                identity_status="high_confidence",
                identity_evidence="The rare exact full name and matching Army-officer context align with the authoritative Comptroller General decision naming Furman H. Updike and his later grade of major.",
                personnel_category="commissioned_army_officer",
                commissioned_officer=True,
                allied_or_foreign_personnel=False,
                research_status="requires_archival_review",
                next_action="Review Box 795 for Furman H. Updike's pre-OSS civilian employer, wartime Army assignments and exact OSS duty. The postwar GAO decision supports identity and officer status only.",
            ),
            base_update(
                8,
                identity_status="high_confidence",
                identity_evidence=army_identity_note(8),
                personnel_category="enlisted_army_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                research_status="requires_archival_review",
                next_action="Review Box 795 to establish Louis J Urbanski's pre-OSS employer and service chronology. The 1946 Army entry supports identity only, and unlisted code 177 remains uninterpreted.",
            ),
            base_update(
                11,
                identity_status="high_confidence",
                identity_evidence="The rare exact name and middle initial align with a Prague diplomatic-post chronology and explicit OSS London service, corroborated by a contemporary Foreign Service Journal Prague entry.",
                personnel_category="unknown_or_indeterminate",
                commissioned_officer=None,
                allied_or_foreign_personnel=False,
                research_status="completed",
                next_action="Review Box 795 to identify Paul M. Ursin's Washington role after October 1940 and determine whether it was the immediate predecessor to OSS London service.",
                archival_review_priority="medium",
            ),
            base_update(
                15,
                identity_status="conflicting",
                identity_evidence="This is the first of two separately printed Richard E Usher rows. Its protected identifier produced two Army candidates with substantively different corrupted names; both were rejected and no candidate field was transferred.",
                personnel_category="unknown_or_indeterminate",
                commissioned_officer=None,
                allied_or_foreign_personnel=None,
                possible_duplicate_group="duplicate-b975-richard-e-usher",
                research_status="conflicting_sources",
                next_action="Review both Box 795 Richard E Usher files together to resolve the conflicting identifier, determine whether the two printed rows are different people and establish each person's pre-OSS affiliation.",
                archival_review_priority="critical",
            ),
            base_update(
                17,
                identity_status="high_confidence",
                identity_evidence="The exceptionally distinctive exact name, 1940-1942 teaching chronology and explicit August 1944 Army assignment to OSS align across Columbia's finding aid and a scholarly archival study.",
                name_variants=["Vladimir Alexis Ussachevsky"],
                personnel_category="enlisted_army_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                research_status="verified_employer_found",
                next_action="Review Box 795 to confirm exact employment dates at Roosevelt High and Pasadena Junior College and document his Army/OSS personnel sequence.",
                archival_review_priority="medium",
            ),
            base_update(
                18,
                identity_status="high_confidence",
                identity_evidence="The rare exact name aligns with an April 1945 OSS travel order naming Yoshisada Katoi Usuda among civilian employees; the middle name is retained as a documented variant pending file confirmation.",
                name_variants=["Yoshisada Katoi Usuda"],
                personnel_category="civilian_professional_or_administrative_grade",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                research_status="requires_archival_review",
                next_action="Review Box 795 for Yoshisada Usuda's pre-OSS occupation and employer. The April 1945 order establishes civilian OSS status but not the prior affiliation.",
                archival_review_priority="high",
            ),
            base_update(
                21,
                research_status="requires_archival_review",
                next_action="Review Box 795 for recruitment forms, résumé, education, language history and pre-OSS employment. A fresh official and institutional search found no reliable pre-OSS employer beyond the already published CIA identity evidence.",
                archival_review_priority="high",
            ),
        ]
    )
    return values


def research_attempts() -> list[dict[str, object]]:
    reviewed_rows = {1, 2, 3, 7, 8, 9, 10, 11, 17, 18, 19, 21}
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        box = "794" if row == 1 else ("796" if row == 23 else "795")
        if row in reviewed_rows:
            outcome = "source_reviewed"
            reviewed = 10 if row in {1, 11, 17} else 7
            rejected = 5
            detail = "Reviewed official, institutional, contemporary or scholarly evidence produced the identity, occupation, military-pathway or employer outcome recorded in the bundle."
        else:
            outcome = "candidate_rejected" if row == 15 else "no_result"
            reviewed = 6
            rejected = 6
            detail = (
                "Two corrupted Army-name conflicts were rejected without transferring any candidate field."
                if row == 15
                else UNRESOLVED[row]
            )

        special_rejection = ""
        if row == 1:
            special_rejection = " Later WCBS and KCBS roles were used only to corroborate identity and were not projected backward."
        elif row == 5:
            special_rejection = " George Masaru Ura and a no-middle-initial veteran listing were retained as leads only because neither bridges George S Ura to OSS or Box 795."
        elif row == 8:
            special_rejection = " Historical code 177 was absent from the inspected occupation list and was not interpreted."
        elif row == 9:
            special_rejection = " Sigfred is retained as an official-record variant of indexed Sigfried rather than silently corrected."
        elif row == 10:
            special_rejection = " A 1965 Maurice Urdang & Associates property record is postwar and was not projected backward."
        elif row == 15:
            special_rejection = " Both Army candidates disagreed substantively on the name and were rejected; the two printed Richard E Usher rows remain separate."
        elif row == 18:
            special_rejection = " Yoshisada Karlo Usuda, associated with the Japanese Embassy and wartime internment, was rejected because that chronology conflicts with the 1945 civilian OSS employee order."
        elif row == 21:
            special_rejection = " CIA Museum and official pocket-history evidence continues to support OSS identity only; language ability and postwar Army employment were not converted into pre-OSS occupation or employment."

        attempts.append(
            {
                "key": f"page478-row{row}-{slug(name)}-b975",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index and official Archives context; permitted CIA official-source context or documented robots-policy limitation; exact-name and meaningful variants; OSS, Army, Navy, rank and unit clues; employer and occupation 1940; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Box {box}; protected identifiers used only in private official-record comparison",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_975",
                "started_at": "2026-10-30T06:45:00Z",
                "completed_at": "2026-10-30T08:28:00Z",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search snippets, unsourced genealogy, people-finder pages, relatives, postwar-only employment leads and sources without an OSS, protected-identifier or personnel-file bridge were rejected. Historical occupation codes and military service were not silently converted into employers." + special_rejection,
                "research_notes": f"{detail} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain and archival searches were checked as applicable. The automated CIA Reading Room route remains disallowed by the site's robots policy, so it was not queried and is not described as a negative result; permitted official or equivalent institutional sources and the physical-file route were used instead. The index page, Army bulk file, technical documentation and relevant occupation-code pages were inspected directly; code pages 171-172 and corrected page 304 were checked. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": f"Review Box {box} for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before wartime service.",
                "attempt_number": 2 if row == 21 else 1,
                "research_agent_version": "before-oss-b975-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-975-v1",
        "reviewer": "Before OSS Batch 975 evidence review",
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
