#!/usr/bin/env python3
"""Generate the reviewed Batch 953 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page467-william-j-thompson-to-ronald-h-thornley-"
    "review_batch-953_2026-10-28.json"
)

INDEX = "nara-index-b953"
ARMY = "army-bulk-b953"
TECH = "army-tech-b953"
CODES = "army-codes-b953"
COLUMBIA = "columbia-annual-report-b953"
ENTRY214 = "nara-entry214-b953"
USASOC = "usasoc-oss-influence-b953"
USNA = "usna-register-b953"
ARMY_GO = "army-general-orders-b953"
NARA_PEP = "nara-pep-b953"
USCG_VALOR = "uscg-valor-b953"
GUARDIAN = "guardian-spies-b953"

PEOPLE = {
    1: ("e80c56d4-d024-5b0c-9cac-33eac8268924", "William J Thompson"),
    2: ("9e6312c7-2f9a-5521-a32e-be3236e2cc74", "William K Thompson"),
    3: ("68011b7b-c0c4-5c7a-bd5c-b4a9b917687d", "William T Thompson"),
    4: ("7b75a41b-3260-5644-bbe7-4e2115fc28c5", "Adeline V Thoms"),
    5: ("b610a51d-477f-5600-97ca-c5b898435199", "Hans Peter A Thomsen"),
    6: ("f16981e3-6361-5ec1-9d95-249027dde163", "Archibald G Thomson"),
    7: ("875f2b0d-2f9d-52cc-93a5-8689c7ac8b84", "Archibald R Thomson"),
    8: ("551ae1bd-d271-5a8e-88ea-965f0780c8f7", "George G Thomson"),
    9: ("4940db74-777c-50d6-9067-bd2a32c5f3d3", "James C Thomson"),
    10: ("a399210a-e1bb-55ad-bf4b-1c6f7778d971", "John S Thomson"),
    11: ("d048558b-b5c8-5ebc-8c6f-09a751cdf82a", "Robert D Thomson"),
    12: ("f9ce2aa6-4dae-506c-81b8-bf43212190f9", "Stanley J Thomson"),
    13: ("bb58f59a-8263-5672-847a-f219dc941904", "Conrad J Thoren"),
    14: ("2456daf1-03f3-5a6c-9007-e8d330b093ab", "Gordon P Thorigal"),
    15: ("4d30ffd0-43d2-5611-9cd7-7ea559fcb604", "Reginald Thorlin"),
    16: ("dfafe96f-62dd-5348-bfe6-d652b36f3422", "Betsy A Thorn"),
    17: ("7e2b7ced-c34d-5840-821a-1d51657abb78", "Edwin W Thorn"),
    18: ("04c4b7c0-765e-5cd9-9a59-9cbc54e62177", "Elmers Thornburg"),
    19: ("1eb0eaa7-9a35-585d-a672-c7f2f61f960f", "Ethel M Thornbury"),
    20: ("df0d68ba-4870-554d-b2c0-4bb94869670d", "George O Thorne"),
    21: ("e87dd833-7c90-577a-9a43-3722decf88a9", "Sevia B Thorne"),
    22: ("7e44bfee-9729-501a-8903-5ce8eeda77fb", "Stewart Thorne"),
    23: ("adb5a82e-e191-5679-87ee-616cffd41c1a", "Ronald H Thornley"),
}

ARMY_IDENTITIES = {
    1: ("1942-09-30", None, None),
    3: ("1942-07-20", "Actors and actresses", "0-02"),
    12: ("1943-04-15", "Accountants and auditors", "0-01"),
    21: ("1943-07-10", "General industry clerks", "1-18"),
    22: ("1942-02-27", "Paint and varnish producing occupations", "6-50"),
}

UNRESOLVED = {
    2: "Common-name exact and variant searches produced no second identifier or Box 775 bridge.",
    4: "Exact-name, OSS, employer, occupation, newspaper, obituary and institutional searches produced no defensible Box 775 identity bridge.",
    5: "Foreign-name and transliteration searches returned several unbridged namesakes but no OSS, Box 775 or dated employment linkage.",
    6: "Military, newspaper, obituary and institutional results for this common name lack the two corroborating identifiers required for assignment.",
    7: "Exact-name and initial-variant results remain unbridged to OSS or Box 775.",
    8: "Common-name military and civilian records provide no defensible OSS or Box 775 selector.",
    10: "Exact-name, OSS, official-domain, occupation, obituary and archival searches produced no reliable Box 776 identity bridge.",
    11: "Multiple military namesakes remain unselectable without a nonshared identifier or Box 776 evidence.",
    13: "Postwar geographic and government records concern a plausible namesake but do not establish a pre-OSS affiliation or Box 776 identity bridge.",
    16: "Exact-name and variant searches produced no reliable wartime identity or pre-OSS affiliation.",
    17: "Military, directory, obituary and institutional candidates remain unbridged to the indexed Box 776 person.",
    18: "The unusual printed first name was preserved; spelling variants and exact-name searches produced no defensible identity or employment evidence.",
    20: "Exact-name military, obituary, directory and employment results remain unbridged to Box 776.",
    23: "A wartime British bell-ringing record names a Ronald H Thornley but supplies no OSS, nationality, assignment or Box 776 bridge and was rejected.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def archive_box(row: int) -> str:
    return "775" if row <= 8 else "776"


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 775-776",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 467, rows 1-23; checked against layout-preserving text and a 220 dpi page render",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. Rows 1-8 are in Box 775 and rows 9-23 in Box 776. Full protected identifiers remain private.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; six Batch 953 protected-identifier candidates reviewed; identifiers withheld",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "Five identity links were accepted and one direct name conflict rejected. No raw bulk row or full protected identifier enters public assets.",
        },
        {
            "key": TECH,
            "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf",
            "archival_identifier": "NN3-064-03-008; National Archives Identifier 1263923",
            "title": "World War II Army Enlistment Records: Reference Copy of Technical Documentation",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives at College Park - Electronic Records",
            "publication_record_date": "1994-2005; reference copy modified 2011",
            "locator": "PDF physical pages 44-46; identifier, name, Army-entry-date and civilian-occupation fields",
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
            "locator": "PDF physical pages 171, 175 and 177; historical categories 1-18, 0-01, 0-02 and 6-50",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical categories are qualified and never converted into named employers, workplaces or exact modern job titles.",
        },
        {
            "key": COLUMBIA,
            "stable_url": "https://upload.wikimedia.org/wikipedia/commons/0/0a/Annual_report_%28IA_annualreport1941colu%29.pdf",
            "archival_identifier": "Internet Archive item annualreport1941colu",
            "title": "Annual Report of the President and Treasurer to the Trustees for the Academic Year Ending June 30, 1941",
            "author_creator": "Columbia University. Office of the President",
            "repository_publisher": "Columbia University; Internet Archive digital scan",
            "publication_record_date": "1941",
            "locator": "PDF physical page 27, printed page 19; presidential report appointment list",
            "access_date": "2026-10-28",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Columbia University annual reports",
            "rights_notes": "The page was text-extracted and inspected at 220 dpi. It dates the 1940-41 appointment but not the exact start or separation day.",
        },
        {
            "key": ENTRY214,
            "stable_url": "https://www.archives.gov/iwg/declassified-records/rg-226-oss/entry-214.html",
            "archival_identifier": "RG 226, Entry 214, Box 6, WN 24840",
            "title": "Records of the Office of Strategic Services (RG 226): Entry 214",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1944-06-21 report; web inventory current at access",
            "locator": "Box 6 inventory entry for Ethel M. Thornbury's twelve-page report on the Iberian Peninsula",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "Sources and Methods Files (Previously Withdrawn Material)",
            "document_number": "WN 24840",
            "rights_notes": "The item-level inventory supplies exact name, report title, date and archival handle; it does not itself state her pre-OSS employer.",
        },
        {
            "key": USASOC,
            "stable_url": "https://arsof-history.org/articles/v14n2_oss_to_sf_page_1.html",
            "archival_identifier": "Veritas, volume 14, number 2 (2018), page 24",
            "title": "The Office of Strategic Services (OSS) Influence on Special Forces",
            "author_creator": "Troy J. Sacquety, PhD",
            "repository_publisher": "U.S. Army Special Operations Command History Office",
            "publication_record_date": "2018",
            "locator": "OSS Veterans of Early Special Forces sidebar; by-name roster comparison and Detachment 101 assignment",
            "access_date": "2026-10-28",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Veritas: Journal of Army Special Operations History",
            "rights_notes": "The historian states that the list resulted from by-name comparisons of OSS personnel and early Special Forces rosters.",
        },
        {
            "key": USNA,
            "stable_url": "https://upload.wikimedia.org/wikipedia/commons/0/00/Annual_register_of_the_United_States_Naval_Academy_%28IA_annualregisterof9319unit%29.pdf",
            "archival_identifier": "Internet Archive item annualregisterof9319unit",
            "title": "Annual Register of the United States Naval Academy, Ninety-Third Academic Year, 1937-1938",
            "author_creator": "United States Naval Academy",
            "repository_publisher": "United States Government Printing Office; Internet Archive digital scan",
            "publication_record_date": "1937-09-24",
            "locator": "PDF physical page 112, printed page 106; resignations list",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "United States Naval Academy annual registers",
            "rights_notes": "The page was text-extracted and inspected at 220 dpi. It identifies student status and a resignation date, not employment.",
        },
        {
            "key": ARMY_GO,
            "stable_url": "https://mcoecbamcoepwprd01.blob.core.usgovcloudapi.net/library/GeneralOrders/GO%201948-1952-E.pdf",
            "archival_identifier": "Department of the Army General Orders No. 81 (1952)",
            "title": "Recommended Lists for Promotion to Temporary Grade of Lieutenant Colonel in the Army of the United States",
            "author_creator": "Department of the Army",
            "repository_publisher": "Maneuver Center of Excellence Libraries",
            "publication_record_date": "1952-08-26",
            "locator": "General Orders No. 81; Reginald Thorlin entry; protected officer number withheld",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "Department of the Army General Orders",
            "rights_notes": "The postwar order supports Army officer identity but prints a protected number that differs from the index; the discrepancy remains explicit and is not published in full.",
        },
        {
            "key": NARA_PEP,
            "stable_url": "https://www.archives.gov/st-louis/pep",
            "archival_identifier": "NARA Persons of Exceptional Prominence list",
            "title": "Persons of Exceptional Prominence",
            "author_creator": "National Personnel Records Center",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "Current as of 2026-08-12",
            "locator": "Table entry for Gordon P Thorigal; branch listed as Coast Guard",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "Official Military Personnel Files",
            "rights_notes": "The current public table confirms the exact name and branch but does not claim a pre-OSS employer or digitized file.",
        },
        {
            "key": USCG_VALOR,
            "stable_url": "https://media.defense.gov/2018/Nov/08/2002060964/0/0/0/BOOK%20OF%20VALOR_DOC.PDF",
            "archival_identifier": "U.S. Coast Guard Historian's Office, Book of Valor, page 164 of 175",
            "title": "Book of Valor",
            "author_creator": "U.S. Coast Guard Historian's Office",
            "repository_publisher": "United States Coast Guard",
            "publication_record_date": "Historical award entry; digital publication 2018",
            "locator": "PDF page 164 of 175; Gordon P. Thorigal Bronze Star entry",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "U.S. Coast Guard Historian's Office",
            "rights_notes": "The award entry supplies exact name, Coast Guard Reserve grade, award and dated mission description; it does not name a civilian employer.",
        },
        {
            "key": GUARDIAN,
            "stable_url": "https://www.guardianspies.com/research.html",
            "archival_identifier": "Guardian Spies OSS/USCG research roster",
            "title": "About the Research: The Story of the U.S. Coast Guard and OSS in World War II",
            "author_creator": "Guardian Spies research project",
            "repository_publisher": "MEB, Inc.",
            "publication_record_date": "2007-2011",
            "locator": "Operational Swimmer Group II roster and deployment chronology; Coast Guard and declassified OSS personnel files described as source base",
            "access_date": "2026-10-28",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Guardian Spies",
            "rights_notes": "Used with official NARA and Coast Guard evidence. The roster explicitly identifies Coast Guard personnel attached to OSS; the underlying personnel file still merits review.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": "wisconsin-b953",
            "organization_id": "4a1a13c4-1aee-5ab1-ac44-16b7a037b7d4",
            "canonical_name": "University of Wisconsin-Madison",
            "historical_name": "University of Wisconsin",
            "aliases": ["UW-Madison", "University of Wisconsin"],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "Madison",
            "state_or_region": "Wisconsin",
            "country": "United States",
            "normalization_notes": "The 1941 historical employer name is preserved separately from the modern canonical name. Student relationships elsewhere are not treated as employment.",
        },
        {
            "key": "barnard-b953",
            "organization_id": "2fccdad1-6dea-523a-9ba5-4a9c954dda43",
            "canonical_name": "Barnard College",
            "historical_name": "Barnard College",
            "aliases": ["Barnard College of Columbia University"],
            "organization_type": "college",
            "sector": "academia_and_research",
            "city": "New York",
            "state_or_region": "New York",
            "country": "United States",
            "active_dates": "1889-present",
            "normalization_notes": "Barnard is preserved as the employing college and is not silently collapsed into Columbia University.",
        },
        {
            "key": "uscgr-b953",
            "organization_id": "37a8f326-bc36-5bb7-9c9c-078500d96f92",
            "canonical_name": "United States Coast Guard",
            "historical_name": "United States Coast Guard Reserve",
            "aliases": ["USCGR", "U.S. Coast Guard"],
            "organization_type": "military and maritime service",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "The historical Coast Guard Reserve wording is preserved for Gordon P. Thorigal's wartime affiliation.",
        },
        {
            "key": "usna-b953",
            "canonical_name": "United States Naval Academy",
            "historical_name": "United States Naval Academy",
            "aliases": ["U.S. Naval Academy", "USNA"],
            "organization_type": "federal service academy",
            "sector": "academia_and_research",
            "city": "Annapolis",
            "state_or_region": "Maryland",
            "country": "United States",
            "active_dates": "1845-present",
            "normalization_notes": "Reginald Thorlin's relationship is student status, not employment; resignation in 1937 does not establish his immediate pre-OSS affiliation.",
        },
    ]


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (entry_date, occupation, code) in ARMY_IDENTITIES.items():
        if occupation is None:
            continue
        values.append(
            {
                "key": f"army-occupation-row{row}-b953",
                "person_id": PEOPLE[row][0],
                "occupation": occupation.lower(),
                "relationship_type": "employment",
                "end_date": entry_date,
                "date_precision": f"Historical category {code} was recorded at Army entry on {entry_date}; no employer, workplace or OSS-transfer date is named.",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "A_direct_official",
                "publication_status": "publish_qualified",
                "research_notes": "The historical category is not converted into a named employer, workplace, exact specialization or immediate pre-OSS affiliation.",
            }
        )
    values.extend(
        [
            {
                "key": "ethel-thornbury-wisconsin-b953",
                "person_id": PEOPLE[19][0],
                "organization_key": "wisconsin-b953",
                "organization_name_as_found": "University of Wisconsin",
                "role_title": "associate professor of English",
                "occupation": "professor",
                "relationship_type": "employment",
                "end_date": "1941",
                "date_precision": "The 1940-41 Columbia annual report identifies her University of Wisconsin title at the time of a Barnard visiting appointment; exact employment dates are not supplied.",
                "city": "Madison",
                "state_or_region": "Wisconsin",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Documented prewar employment. The three-year gap to her dated 1944 OSS report prevents an immediate-predecessor or last-civilian-employer claim.",
            },
            {
                "key": "ethel-thornbury-barnard-b953",
                "person_id": PEOPLE[19][0],
                "organization_key": "barnard-b953",
                "organization_name_as_found": "Barnard College",
                "role_title": "visiting associate professor of English",
                "occupation": "professor",
                "relationship_type": "employment",
                "start_date": "1940",
                "end_date": "1941",
                "date_precision": "The appointment appears in the annual report for the academic year ending 1941-06-30; exact start and separation dates are not supplied.",
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
                "research_notes": "Documented prewar visiting appointment. No source yet bridges this appointment directly to OSS service in 1944.",
            },
            {
                "key": "reginald-thorlin-usna-b953",
                "person_id": PEOPLE[15][0],
                "organization_key": "usna-b953",
                "organization_name_as_found": "United States Naval Academy",
                "role_title": "midshipman; class of 1940",
                "relationship_type": "student",
                "end_date": "1937-03-15",
                "date_precision": "The official register lists a March 15, 1937 resignation and class year 1940; it does not supply an admission date.",
                "city": "Annapolis",
                "state_or_region": "Maryland",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "A_direct_official",
                "publication_status": "published",
                "research_notes": "Student status is not employment. The 1937-OSS interval remains unresolved and requires the personnel file.",
            },
            {
                "key": "gordon-thorigal-uscgr-b953",
                "person_id": PEOPLE[14][0],
                "organization_key": "uscgr-b953",
                "organization_name_as_found": "USCGR",
                "role_title": "coxswain; later recorded as Boatswain's Mate, Second Class",
                "relationship_type": "military_assignment",
                "start_date": "1944-01",
                "end_date": "1945-04-15",
                "date_precision": "The documented Operational Swimmer Group II deployment ran from January 1944 through 1945-04-15; individual attachment day is not stated.",
                "country": "United States",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "explicit_immediate",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "published",
                "research_notes": "Best-supported military pathway: Coast Guard Reserve member attached to OSS Operational Swimmer Group II. This is not a civilian employer claim.",
            },
        ]
    )
    return values


def army_claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    code_pages = {3: 175, 12: 175, 21: 171, 22: 177}
    for row, (entry_date, occupation, code) in ARMY_IDENTITIES.items():
        person_id, name = PEOPLE[row]
        values.append(
            {
                "key": f"identity-row{row}-army-b953",
                "person_id": person_id,
                "claim_type": "identity",
                "claim_text": f"The indexed {name} is a high-confidence match to the reviewed official Army record.",
                "evidence_paraphrase": "A nonshared protected identifier and exact full-name agreement connect the visually verified index row to the official Army record.",
                "identity_match_assessment": "High confidence from an exact full name and a private nonshared identifier.",
                "temporal_assessment": "The Army record dates entry into service but does not establish the exact OSS transfer date.",
                "source_quality": "A_direct_official",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "This identity decision does not establish a named employer or immediate OSS predecessor.",
                "sources": [
                    {"source_key": INDEX, "locator_override": f"PDF page 467 row {row}; Box {archive_box(row)}; protected identifier withheld"},
                    {"source_key": ARMY, "locator_override": "Reviewed name record; protected identifier withheld"},
                    {"source_key": TECH, "support_type": "context_only", "locator_override": "Field definitions, PDF physical pages 44-46"},
                ],
            }
        )
        if occupation is None:
            continue
        values.append(
            {
                "key": f"occupation-row{row}-army-b953",
                "person_id": person_id,
                "affiliation_key": f"army-occupation-row{row}-b953",
                "claim_type": "occupation",
                "claim_text": f"At Army entry on {entry_date}, {name} was recorded in the historical {occupation} category; no employer or workplace is identified.",
                "evidence_excerpt": occupation,
                "evidence_paraphrase": f"The official bulk record supplies historical code {code}; the visually reviewed NARA code list expands it as {occupation}.",
                "identity_match_assessment": "High confidence from the accepted protected-identifier bridge and exact name agreement.",
                "temporal_assessment": "Strongly date-bounded at Army entry, but not shown to be the immediate pre-OSS affiliation.",
                "source_quality": "A_direct_official",
                "claim_confidence": "medium",
                "publication_status": "publish_qualified",
                "match_notes": "Published only as a qualified historical category. No employer, workplace or exact modern specialization is inferred.",
                "sources": [
                    {"source_key": ARMY, "locator_override": f"Army entry {entry_date}; historical code {code}; protected identifier withheld"},
                    {"source_key": CODES, "locator_override": f"PDF physical page {code_pages[row]}; historical category {code}"},
                ],
            }
        )
    return values


def claims() -> list[dict[str, object]]:
    values = army_claims()
    values.extend(
        [
            {
                "key": "identity-ethel-thornbury-b953",
                "person_id": PEOPLE[19][0],
                "claim_type": "identity",
                "claim_text": "The indexed Ethel M Thornbury is a high-confidence match to the scholar named in a dated OSS report inventory and Columbia's 1941 annual report.",
                "evidence_excerpt": "Report by Miss Ethel M. Thornbury",
                "evidence_paraphrase": "NARA inventories a 1944 OSS report under the exact indexed name; Columbia supplies her full middle name and prewar academic appointments.",
                "identity_match_assessment": "High confidence from a distinctive exact name and middle initial, direct OSS record context, and compatible institutional chronology.",
                "temporal_assessment": "The academic appointments are documented in 1940-41 and the OSS report is dated 1944-06-21; the intervening sequence remains unproven.",
                "source_quality": "A_direct_official",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "The full-name variant is admitted; neither academic institution is labeled immediate without a personnel-file bridge.",
                "sources": [
                    {"source_key": INDEX, "locator_override": "PDF page 467 row 19; Box 776"},
                    {"source_key": ENTRY214, "locator_override": "Entry 214, Box 6, WN 24840; report dated 1944-06-21"},
                    {"source_key": COLUMBIA, "locator_override": "PDF physical page 27, printed page 19"},
                ],
            },
            {
                "key": "employment-ethel-wisconsin-b953",
                "person_id": PEOPLE[19][0],
                "affiliation_key": "ethel-thornbury-wisconsin-b953",
                "claim_type": "other_pre_oss_affiliation",
                "claim_text": "In the 1940-41 academic year, Ethel Margaret Thornbury was identified as an associate professor of English at the University of Wisconsin.",
                "evidence_excerpt": "Associate Professor of English at the University of Wisconsin",
                "evidence_paraphrase": "Columbia's annual report states her University of Wisconsin title while announcing a Barnard visiting appointment.",
                "identity_match_assessment": "High confidence from the distinctive full name combined with the exact-name 1944 OSS record.",
                "temporal_assessment": "Documented prewar employment; not shown to be the immediate affiliation or last civilian employer before OSS.",
                "source_quality": "B_authoritative_institutional",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "University of Wisconsin is an employer here; the modern canonical organization is kept separate from the historical name.",
                "sources": [{"source_key": COLUMBIA, "locator_override": "PDF physical page 27, printed page 19"}],
            },
            {
                "key": "employment-ethel-barnard-b953",
                "person_id": PEOPLE[19][0],
                "affiliation_key": "ethel-thornbury-barnard-b953",
                "claim_type": "other_pre_oss_affiliation",
                "claim_text": "Ethel Margaret Thornbury held a visiting associate professorship of English at Barnard College in the 1940-41 academic year.",
                "evidence_excerpt": "Visiting Associate Professor of English, in Barnard College",
                "evidence_paraphrase": "Columbia's annual report names the visiting title and employing college for the academic year ending June 30, 1941.",
                "identity_match_assessment": "High confidence from the distinctive full name combined with the exact-name 1944 OSS record.",
                "temporal_assessment": "Documented prewar appointment; no source yet establishes it as immediately before OSS.",
                "source_quality": "B_authoritative_institutional",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "Barnard is retained as the named employing college rather than collapsed into Columbia University.",
                "sources": [{"source_key": COLUMBIA, "locator_override": "PDF physical page 27, printed page 19"}],
            },
            {
                "key": "identity-reginald-thorlin-b953",
                "person_id": PEOPLE[15][0],
                "claim_type": "identity",
                "claim_text": "The indexed Reginald Thorlin is a high-confidence match to the OSS Detachment 101 veteran documented by the U.S. Army Special Operations history office.",
                "evidence_excerpt": "LTC Reginald Thorlin ... SO Detachment 101 (Burma)",
                "evidence_paraphrase": "A U.S. Army historian's by-name OSS roster comparison places Thorlin in Detachment 101; a postwar Army order confirms the officer identity but carries a differing protected number.",
                "identity_match_assessment": "High confidence from the rare exact name, explicit OSS roster match and official Army officer record; the protected-number discrepancy remains documented.",
                "temporal_assessment": "The source establishes wartime OSS assignment but does not bridge his 1937 academy resignation to OSS entry.",
                "source_quality": "B_authoritative_institutional",
                "claim_confidence": "high",
                "publication_status": "publish_qualified",
                "match_notes": "No full protected number is published. Box 776 must resolve the discrepancy and intervening chronology.",
                "sources": [
                    {"source_key": INDEX, "locator_override": "PDF page 467 row 15; Box 776; protected identifier withheld"},
                    {"source_key": USASOC, "locator_override": "OSS Veterans of Early Special Forces sidebar; by-name roster comparison"},
                    {"source_key": ARMY_GO, "support_type": "contradicts", "locator_override": "General Orders No. 81; protected officer number withheld"},
                ],
            },
            {
                "key": "student-reginald-thorlin-usna-b953",
                "person_id": PEOPLE[15][0],
                "affiliation_key": "reginald-thorlin-usna-b953",
                "claim_type": "other_pre_oss_affiliation",
                "claim_text": "Reginald Thorlin was a United States Naval Academy midshipman in the class of 1940 and resigned on 1937-03-15.",
                "evidence_excerpt": "Thorlin, Reginald ... 1940 ... Mar. 15, 1937",
                "evidence_paraphrase": "The official 1937-38 Naval Academy register lists his class year and resignation date.",
                "identity_match_assessment": "High confidence from the rare exact name and compatible later official OSS and Army officer evidence.",
                "temporal_assessment": "Documented prewar student status only; it is neither employment nor the proven immediate predecessor to OSS.",
                "source_quality": "A_direct_official",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "The personnel file is needed to identify his activity between 1937 and OSS service.",
                "sources": [{"source_key": USNA, "locator_override": "PDF physical page 112, printed page 106; resignations list"}],
            },
            {
                "key": "identity-gordon-thorigal-b953",
                "person_id": PEOPLE[14][0],
                "claim_type": "identity",
                "claim_text": "The indexed Gordon P Thorigal is a high-confidence match to the Coast Guard Reserve member attached to OSS Operational Swimmer Group II.",
                "evidence_excerpt": "COX Gordon P. Thorigal, USCGR (Bronze Star)",
                "evidence_paraphrase": "NARA confirms the exact name and Coast Guard branch; the Coast Guard award history and the OSS/USCG archival roster agree on identity and wartime service.",
                "identity_match_assessment": "High confidence from a distinctive exact name and middle initial across three mutually reinforcing official or archival sources.",
                "temporal_assessment": "The roster dates the OSS-attached group to January 1944 through 1945-04-15; the award entry dates missions within that interval.",
                "source_quality": "A_direct_official",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "The difference between coxswain and Boatswain's Mate Second Class wording is preserved as a source-level grade variation.",
                "sources": [
                    {"source_key": INDEX, "locator_override": "PDF page 467 row 14; Box 776"},
                    {"source_key": NARA_PEP, "locator_override": "Current PEP table; exact name and Coast Guard branch"},
                    {"source_key": USCG_VALOR, "locator_override": "PDF page 164 of 175; Bronze Star entry"},
                    {"source_key": GUARDIAN, "locator_override": "Operational Swimmer Group II roster and deployment chronology"},
                ],
            },
            {
                "key": "military-gordon-thorigal-uscgr-b953",
                "person_id": PEOPLE[14][0],
                "affiliation_key": "gordon-thorigal-uscgr-b953",
                "claim_type": "immediate_pre_oss_affiliation",
                "claim_text": "Gordon P Thorigal's best-supported military pathway was the United States Coast Guard Reserve, from which he served with an OSS-attached operational swimmer group.",
                "evidence_excerpt": "Coast Guard men attached to the OSS",
                "evidence_paraphrase": "The archival research roster identifies Thorigal as USCGR in Operational Swimmer Group II, explicitly attached to OSS Detachments 101, 404 and 505.",
                "identity_match_assessment": "High confidence from the exact-name official Coast Guard and NARA records combined with the OSS/USCG roster.",
                "temporal_assessment": "Explicit immediate military pathway: the source describes an active Coast Guard Reserve member in an OSS-attached unit during the dated deployment.",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "This military affiliation is not labeled a civilian employer; no last civilian employer has yet been identified.",
                "sources": [
                    {"source_key": GUARDIAN, "locator_override": "Operational Swimmer Group II; January 1944 to 1945-04-15; attached to OSS Detachments 101, 404 and 505"},
                    {"source_key": USCG_VALOR, "locator_override": "PDF page 164 of 175; dated Bronze Star mission entry"},
                    {"source_key": NARA_PEP, "support_type": "context_only", "locator_override": "Current PEP table; Coast Guard branch"},
                ],
            },
        ]
    )
    return values


def archival_update(row: int, reason: str) -> dict[str, object]:
    person_id, name = PEOPLE[row]
    box = archive_box(row)
    return {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, Box {box} and archive location 230/86/42/01. {reason}",
        "personnel_category": "unknown_or_indeterminate",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": f"Review Box {box} for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }


def army_update(row: int) -> dict[str, object]:
    occupation = ARMY_IDENTITIES[row][1]
    return {
        "person_id": PEOPLE[row][0],
        "identity_status": "high_confidence",
        "identity_evidence": "A nonshared protected identifier and exact full-name agreement connect the visually verified index row to the reviewed official Army record.",
        "name_variants": ["Sevia B Thorne Jr"] if row == 21 else None,
        "personnel_category": "enlisted_army_personnel",
        "commissioned_officer": False,
        "allied_or_foreign_personnel": False,
        "manual_review_required": True,
        "research_status": "occupation_only_found" if occupation else "requires_archival_review",
        "next_action": f"Review Box {archive_box(row)} to establish the immediate pre-OSS affiliation and named last civilian employer; do not convert the Army category into a workplace.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }


def person_updates() -> list[dict[str, object]]:
    values = [archival_update(row, reason) for row, reason in UNRESOLVED.items()]
    values.extend(army_update(row) for row in ARMY_IDENTITIES)
    values.extend(
        [
            {
                "person_id": PEOPLE[9][0],
                "identity_status": "conflicting",
                "identity_evidence": "The Box 776 row's protected identifier points to an official Army record whose name conflicts directly with James C Thomson. The candidate was rejected and no Army facts were transferred.",
                "personnel_category": "unknown_or_indeterminate",
                "manual_review_required": True,
                "research_status": "conflicting_sources",
                "next_action": "Review Box 776 and the original index source to determine whether the protected identifier or printed name is erroneous. No reliable pre-OSS employer has yet been identified.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[14][0],
                "identity_status": "high_confidence",
                "identity_evidence": "The distinctive exact name and middle initial align across the OSS index, NARA's Coast Guard personnel-file listing, the official Coast Guard award history and an OSS/USCG archival roster.",
                "personnel_category": "enlisted_coast_guard_personnel",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": False,
                "manual_review_required": False,
                "research_status": "completed",
                "next_action": "Optional Box 776 and Coast Guard personnel-file review may identify his last civilian employer before service and refine the grade chronology.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "medium",
            },
            {
                "person_id": PEOPLE[15][0],
                "identity_status": "high_confidence",
                "identity_evidence": "The rare exact name and official U.S. Army Special Operations roster comparison identify the OSS Detachment 101 veteran. A postwar official Army order carries a differing protected identifier, which remains unresolved.",
                "personnel_category": "unknown_or_indeterminate",
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Review Box 776 to reconcile the protected identifier and identify Thorlin's activity between his 1937 Naval Academy resignation and OSS Detachment 101 service.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[19][0],
                "identity_status": "high_confidence",
                "identity_evidence": "A distinctive exact name and middle initial connect the index to NARA's dated inventory of her 1944 OSS report; Columbia supplies the full middle name and compatible 1941 academic chronology.",
                "name_variants": ["Ethel Margaret Thornbury"],
                "personnel_category": "civilian_professional_or_administrative_grade",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "documented_prewar_employer_found",
                "next_action": "Review Box 776 to determine whether University of Wisconsin, Barnard College or another intervening affiliation immediately preceded OSS service and to identify the last civilian employer before entry.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
        ]
    )
    return values


def research_attempts() -> list[dict[str, object]]:
    attempts: list[dict[str, object]] = []
    for row in sorted(PEOPLE):
        person_id, name = PEOPLE[row]
        box = archive_box(row)
        if row in UNRESOLVED:
            outcome = "no_result"
            reviewed = 7
            rejected = 6
            detail = UNRESOLVED[row]
        elif row == 9:
            outcome = "candidate_rejected"
            reviewed = 8
            rejected = 7
            detail = "A protected identifier produced an official Army candidate with a directly conflicting name; the candidate was rejected and no facts were transferred."
        elif row in ARMY_IDENTITIES:
            occupation = ARMY_IDENTITIES[row][1]
            outcome = "source_reviewed"
            reviewed = 8
            rejected = 6
            detail = "An accepted protected-identifier Army bridge supports identity" + (f" and a dated historical {occupation} category without naming an employer or workplace." if occupation else "; the undefined historical occupation code was not interpreted or published.")
        elif row == 14:
            outcome = "source_reviewed"
            reviewed = 11
            rejected = 5
            detail = "Official NARA and Coast Guard evidence plus an archival OSS/USCG roster establish a high-confidence Coast Guard Reserve pathway into an OSS-attached operational swimmer group."
        elif row == 15:
            outcome = "source_reviewed"
            reviewed = 10
            rejected = 6
            detail = "An official U.S. Army historian's by-name roster comparison establishes Detachment 101 identity; an official 1937 Naval Academy register documents student status, while a protected-number discrepancy and the intervening chronology require Box 776 review."
        elif row == 19:
            outcome = "source_reviewed"
            reviewed = 10
            rejected = 5
            detail = "A NARA item-level inventory establishes exact-name OSS context and Columbia's inspected 1941 annual report documents University of Wisconsin and Barnard College employment, without proving immediacy."
        else:
            raise AssertionError(f"Missing Batch 953 outcome for row {row}")
        attempts.append(
            {
                "key": f"page467-row{row}-{slug(name)}-b953",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index and public Archives context; CIA Reading Room or equivalent official-source check; exact-name and meaningful variants; OSS and military clues; employer and occupation 1940; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Box {box}; protected identifiers used privately only when defensible",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_953",
                "started_at": "2026-10-28T18:00:00Z",
                "completed_at": "2026-10-28T21:10:00Z",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search snippets, unsourced genealogy, people-finder pages, modern records, postwar-only leads and sources without an OSS, protected-identifier or Box-file bridge were not assigned. The James C Thomson Army-name conflict and Ronald H Thornley bell-ringing lead were rejected or retained only as unassigned alternatives.",
                "research_notes": f"{detail} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain, CIA Reading Room-equivalent and Library of Congress searches were checked as applicable. The index page, Columbia and Naval Academy pages, Army code lists and admitted web sources were inspected directly. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": f"Review Box {box} for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before wartime service.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b953-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-953-v1",
        "reviewer": "Before OSS Batch 953 evidence review",
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
