#!/usr/bin/env python3
"""Generate the reviewed Batch 921 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "research/evidence-page451-franz-stone-to-william-stoppe-review_batch-921_2026-10-26.json"

INDEX = "nara-index-b921"
ARMY = "army-bulk-b921"
TECH = "army-tech-b921"
CODES = "army-codes-b921"
LOC_OPM = "loc-opm-franz-stone-b921"
NARA_OPM = "nara-opm-history-b921"
LOC_OSRD = "loc-osrd-franz-stone-b921"
BARNES = "barnes-crampton-kirk-stone-b921"
AAG = "sedaag-kirk-stone-b921"
GHI = "ghi-oscar-stonorov-b921"
UWYO = "uwyo-oscar-stonorov-b921"


PEOPLE = {
    1: ("2ae9e581-728c-5e63-b11c-055e82208b3e", "Franz T Stone", "750"),
    2: ("7c9621d7-a086-501f-83e4-ec804eee8eed", "Franz T Stone", "750"),
    3: ("4a034e0a-7e12-513f-b9e2-e8c3ea45a895", "George Stone", "750"),
    4: ("4d430faa-718d-5966-b521-1a5e70d1f0a6", "Harry L Stone", "750"),
    5: ("ce673b69-e635-5dd6-9623-2cc544325084", "Jack W Stone", "750"),
    6: ("985f4849-5045-5cfe-982a-c01a8bed3f02", "Katherine T Stone", "750"),
    7: ("773a3e2c-7d01-542e-93f0-35fc0fa85890", "Katherine D Stone", "750"),
    8: ("f8d4679d-40c3-59c8-8c09-211c0697dbc5", "Kenneth S Stone", "750"),
    9: ("b941d58f-625d-555c-931e-62a49ed11c7c", "Kirk H Stone", "750"),
    10: ("e24c44f9-d71c-5ec5-a45e-f42fdd335e3a", "Martin R Stone", "750"),
    11: ("c149ac40-bafc-5f8b-952b-fd452a6862b2", "Norman Stone", "750"),
    12: ("9bd8988a-fa3d-56df-ba0b-ca751a1f93f5", "Orville C Stone", "750"),
    13: ("b7d45841-06f9-574d-b6a3-ba9808c72a4f", "Stone Stone", "750"),
    14: ("b7a5d36a-ff2f-5c50-b6de-784bafe5d61c", "Ward S Stone", "750"),
    15: ("6b0d1d2e-39c7-5e6d-b3e7-db24178335e1", "William M Stone", "750"),
    16: ("8c317a37-92de-5056-9cf1-44c6fa6fa777", "Donna M Stoner", "750"),
    17: ("c8c78b53-71ac-532d-ad2e-6925c1953574", "James B Stoner", "750"),
    18: ("aa4e8983-ee9c-5e01-b227-f5d98c82a648", "Edna F Stonesifer", "750"),
    19: ("d710a222-4b39-55df-9ab5-81c8eee836ce", "Catherine J Stonitsch", "750"),
    20: ("807f6052-1c82-5804-9077-59d534add06f", "Oscar Stonorov", "750"),
    21: ("e2597159-a1af-52ae-a691-db27fff06410", "David K Stookey", "751"),
    22: ("a9a77b30-9fd3-5c38-9998-5aa3970c67a7", "Berthold J Stoos", "751"),
    23: ("b0e72372-abb5-5173-8b87-0655201869ac", "William R Stoppe", "751"),
}


UNRESOLVED = {
    3: "Five Library of Congress candidates were uninitialed, postwar, too early, or OCR-derived common-name collisions; none supplied an OSS or Box 750 bridge.",
    4: "Five Library of Congress candidates had the wrong middle initial, described namesakes, or were OCR token collisions; none established the indexed person.",
    5: "The Library of Congress candidate referred to Mrs Jack L Stone, not Jack W Stone, and no other reviewed source supplied an identity bridge.",
    6: "Exact-name, employer, occupation, institutional, obituary, newspaper and archival searches produced no person-specific result with an OSS or Box 750 bridge.",
    7: "Exact-name, employer, occupation, institutional, obituary, newspaper and archival searches produced no person-specific result with an OSS or Box 750 bridge.",
    8: "Exact-name, employer, occupation, institutional, obituary, newspaper and archival searches produced no person-specific result with an OSS or Box 750 bridge.",
    10: "The sole Library of Congress candidate was an OCR collision involving Stonewall and a different Martin; no identity or employment bridge was found.",
    11: "The protected identifier points to an official Army row named Edmund J De Lorenzo, a complete name conflict. Five Library of Congress candidates were also unbridged or false positives.",
    12: "Exact-name, employer, occupation, institutional, obituary, newspaper and archival searches produced no person-specific result with an OSS or Box 750 bridge.",
    13: "The unusual printed name was preserved exactly. Five Library of Congress candidates merely repeated the material noun stone or referred to I. F. Stone.",
    14: "The Library of Congress candidate named Edward C Stone, not Ward S Stone, and no corroborating OSS or employment evidence was found.",
    15: "Five Library of Congress candidates concerned other initials, OCR collisions, or unrelated namesakes; none established William M Stone.",
    16: "Exact-name, employer, occupation, institutional, obituary, newspaper and archival searches produced no person-specific result with an OSS or Box 750 bridge.",
    17: "Five Library of Congress candidates were OCR collisions or wrong-name results. The printed Captain rank alone does not identify an external namesake or employer.",
    18: "A 1945 Supreme Court journal entry names Edna F Stonesifer but supplies no occupation, employer, OSS context, or identifier bridge and was not assigned.",
    19: "Exact-name, employer, occupation, institutional, obituary, newspaper and archival searches produced no reliable identity or employment evidence.",
    21: "A Foreign Service Journal lead actually concerned Robert W Stookey, not David K Stookey; genealogy results were discovery-only and supplied no employer.",
    22: "A 1911 Chicago directory lists a Berthold J Stoos as a clerk but is too early and lacks an OSS or Box 751 bridge; it remains an unassigned namesake lead.",
}


LOC_REJECTIONS = {1: 1, 3: 5, 4: 5, 5: 1, 10: 1, 11: 5, 13: 5, 14: 1, 15: 5, 17: 5}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 750-751",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 451, rows 1-23; checked against layout-preserving text and a rendered page image",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. The two adjacent Franz T Stone rows remain separate unresolved entities in one possible-duplicate group. Full identifiers remain private.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; one accepted and one rejected Batch 921 protected-identifier candidate",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "No raw row or full protected identifier is retained in public assets. The Norman Stone name conflict was rejected. A coded occupation identifies no employer.",
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
            "access_date": "2026-10-26",
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
            "locator": "PDF physical page 173, printed pages XIV-XV; category 8-02 visually checked",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "The historical occupation label identifies neither an employer nor a workplace.",
        },
        {
            "key": LOC_OPM,
            "stable_url": "https://www.loc.gov/item/2017689998/",
            "archival_identifier": "Library of Congress Control Number 2017689998; LC-USE6-D-001062",
            "title": "Mr. Franz T. Stone. Special adviser, Industrial Supply Section, Tools Section, Office of Production Management (OPM)",
            "author_creator": "United States Office for Emergency Management",
            "repository_publisher": "Library of Congress Prints and Photographs Division",
            "publication_record_date": "between 1940 and 1946; OPM caption context limits the role to 1941-January 1942",
            "locator": "Item caption card and catalog record; LC-USE6-D-001062",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "collection_name": "Farm Security Administration/Office of War Information Photograph Collection",
            "rights_notes": "Government photograph catalog metadata. The exact name is a candidate for the adjacent index rows, but neither row can yet be selected.",
        },
        {
            "key": NARA_OPM,
            "stable_url": "https://www.archives.gov/research/guide-fed-records/groups/179.html",
            "archival_identifier": "Record Group 179",
            "title": "Records of the War Production Board",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "current federal records guide",
            "locator": "Sections 179.1 and 179.2; OPM established January 7, 1941 and superseded in January 1942",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "collection_name": "Guide to Federal Records",
            "rights_notes": "Context source used only to date the historical agency; it does not identify Franz Stone.",
        },
        {
            "key": LOC_OSRD,
            "stable_url": "https://tile.loc.gov/storage-services/service/gdc/gdcosrdmicrofilmpublic/2020673190/2020673190.pdf",
            "archival_identifier": "OSRD Report No. 6023; Section 16.1 Report No. 125; Library of Congress item 2020673190",
            "title": "A Practical Application of the Schmidt Camera to Night Photography",
            "author_creator": "Harvard University Optical Research Laboratory; Office of Scientific Research and Development",
            "repository_publisher": "Library of Congress",
            "publication_record_date": "1945-12-31",
            "locator": "PDF physical pages 2 and 4; title page and visually checked distribution list",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "collection_name": "Office of Scientific Research and Development reports",
            "document_number": "OEMsr-474; OSRD 6023",
            "rights_notes": "The distribution list names Dr. Franz Stone at OSS but does not distinguish the two adjacent index rows.",
        },
        {
            "key": BARNES,
            "stable_url": "https://blogs.ubc.ca/trevorbarnes/files/2015/09/proofs.pdf",
            "archival_identifier": "Chapter 11, proof copy, pages 228-251",
            "title": "Mapping Intelligence, American Geographers and the Office of Strategic Services and GHQ/SCAP (Tokyo)",
            "author_creator": "Trevor Barnes and Jeremy Crampton",
            "repository_publisher": "University of British Columbia",
            "locator": "PDF page 2, printed page 229 and footnote 2; citation to Kirk H. Stone letter in RG 226, Entry 1, Box 7, Folder 14",
            "access_date": "2026-10-26",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "rights_notes": "A scholarly chapter hosted by the author's university. Only a short excerpt and project-authored paraphrase are retained.",
        },
        {
            "key": AAG,
            "stable_url": "https://higherlogicdownload.s3.amazonaws.com/AAG/84c8f118-b8f0-4f1f-b48c-c0c0b8e1105f/UploadedImages/spring1998.pdf",
            "archival_identifier": "Southeastern Division, Association of American Geographers Newsletter, volume 17, number 1",
            "title": "In Memoriam: Kirk H. Stone",
            "author_creator": "James O. Wheeler",
            "repository_publisher": "Southeastern Division, Association of American Geographers",
            "publication_record_date": "Spring 1998",
            "locator": "PDF physical page 3; degree years and University of Georgia career summary",
            "access_date": "2026-10-26",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "SEDAAG Newsletter",
            "rights_notes": "Professional-association obituary used for degree institutions and years; postwar employment is not modeled as pre-OSS evidence.",
        },
        {
            "key": GHI,
            "stable_url": "https://www.transatlanticperspectives.org/entries/oscar-stonorov/",
            "archival_identifier": "Transatlantic Perspectives biographical entry",
            "title": "Oscar Stonorov",
            "author_creator": "Andreas Joch",
            "repository_publisher": "German Historical Institute",
            "publication_record_date": "2018-04-11; updated 2018-07-29",
            "locator": "Biography paragraphs describing the Philadelphia office with Louis Kahn and early-1940s staff",
            "access_date": "2026-10-26",
            "source_quality": "B_authoritative_institutional",
            "rights_notes": "The biography is retained as a low-confidence identity lead only because no independent OSS or Box 750 bridge was found.",
        },
        {
            "key": UWYO,
            "stable_url": "https://www.wyominghistoryday.org/theme-topics/collections/oscar-stonorov",
            "archival_identifier": "Oscar Stonorov papers, Collection No. 4375",
            "title": "Oscar Stonorov",
            "author_creator": "American Heritage Center",
            "repository_publisher": "University of Wyoming American Heritage Center",
            "locator": "Collection biography and linked inventory; architectural office and 1940s Louis Kahn partnership",
            "access_date": "2026-10-26",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Oscar Stonorov papers",
            "rights_notes": "Institutional collection context corroborates the architect's career but does not bridge him to the OSS index row.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": "opm-b921",
            "organization_id": "68d72760-88d8-5d06-a8b2-598b571bb6a8",
            "canonical_name": "U.S. Office of Production Management",
            "historical_name": "Office of Production Management",
            "aliases": ["OPM"],
            "organization_type": "federal wartime agency",
            "sector": "federal_government",
            "city": "Washington",
            "state_or_region": "District of Columbia",
            "country": "United States",
            "active_dates": "1941-1942",
            "normalization_notes": "Reuses the existing historical agency. It was superseded by the War Production Board in January 1942.",
        },
        {
            "key": "michigan-b921",
            "organization_id": "4ee8a858-3cd1-5a2d-94a7-0d3c7a3fdb3a",
            "canonical_name": "University of Michigan",
            "historical_name": "University of Michigan",
            "aliases": [],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "Ann Arbor",
            "state_or_region": "Michigan",
            "country": "United States",
            "normalization_notes": "Reuses the most-linked existing canonical organization record.",
        },
        {
            "key": "syracuse-b921",
            "canonical_name": "Syracuse University",
            "historical_name": "Syracuse University",
            "aliases": [],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "Syracuse",
            "state_or_region": "New York",
            "country": "United States",
            "normalization_notes": "Historical institution name preserved; the relationship is student, not employment.",
        },
        {
            "key": "stonorov-kahn-b921",
            "canonical_name": "Stonorov & Kahn",
            "historical_name": "Stonorov & Kahn",
            "aliases": ["office of Stonorov & Kahn"],
            "organization_type": "architectural practice",
            "sector": "self_employed",
            "city": "Philadelphia",
            "state_or_region": "Pennsylvania",
            "country": "United States",
            "active_dates": "early 1940s",
            "normalization_notes": "Retained only for a withheld low-confidence candidate. No link to the indexed Oscar Stonorov row is published as fact.",
        },
    ]


def affiliations() -> list[dict[str, object]]:
    result: list[dict[str, object]] = []
    for row in (1, 2):
        result.append(
            {
                "key": f"franz-stone-row{row}-opm-b921",
                "person_id": PEOPLE[row][0],
                "organization_key": "opm-b921",
                "organization_name_as_found": "Office of Production Management",
                "role_title": "Special adviser, Industrial Supply Section, Tools Section",
                "relationship_type": "government_assignment",
                "end_date": "1942-01",
                "date_precision": "The caption names OPM, an agency active from January 1941 until January 1942; neither exact dates nor the OSS transition are established.",
                "city": "Washington",
                "state_or_region": "District of Columbia",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "ambiguous",
                "claim_confidence": "low",
                "source_quality": "A_direct_official",
                "publication_status": "withheld_low_confidence",
                "research_notes": "The exact external name may describe one person duplicated in the index or one of two different people. The same claim is withheld on both rows to prevent public double-counting.",
            }
        )
    result.extend(
        [
            {
                "key": "kirk-stone-michigan-student-b921",
                "person_id": PEOPLE[9][0],
                "organization_key": "michigan-b921",
                "organization_name_as_found": "University of Michigan",
                "role_title": "B.A. student",
                "occupation": "student",
                "relationship_type": "student",
                "end_date": "1935",
                "date_precision": "Bachelor's degree year; attendance start date not stated",
                "city": "Ann Arbor",
                "state_or_region": "Michigan",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "A student affiliation, not employment and not shown to be immediate before OSS service.",
            },
            {
                "key": "kirk-stone-syracuse-student-b921",
                "person_id": PEOPLE[9][0],
                "organization_key": "syracuse-b921",
                "organization_name_as_found": "Syracuse University",
                "role_title": "M.A. student",
                "occupation": "student",
                "relationship_type": "student",
                "end_date": "1937",
                "date_precision": "Master's degree year; attendance start date not stated",
                "city": "Syracuse",
                "state_or_region": "New York",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "A student affiliation, not employment and not shown to be immediate before OSS service.",
            },
            {
                "key": "oscar-stonorov-kahn-candidate-b921",
                "person_id": PEOPLE[20][0],
                "organization_key": "stonorov-kahn-b921",
                "organization_name_as_found": "office of Stonorov & Kahn",
                "role_title": "architect and partner",
                "occupation": "architect",
                "relationship_type": "self_employment",
                "date_precision": "The institutional biographies place the practice in the early 1940s; its relation to OSS service is unestablished.",
                "city": "Philadelphia",
                "state_or_region": "Pennsylvania",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "temporal_relation_uncertain",
                "identity_confidence": "ambiguous",
                "claim_confidence": "low",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "withheld_low_confidence",
                "research_notes": "The spelling is distinctive, but no source reviewed bridges the architect directly to OSS or Box 750. The candidate is not a public fact.",
            },
            {
                "key": "william-stoppe-occupation-b921",
                "person_id": PEOPLE[23][0],
                "occupation": "Occupations in production of bakery products, not elsewhere classified, unskilled level",
                "relationship_type": "employment",
                "end_date": "1943-05-12",
                "date_precision": "Historical civilian-occupation code 802 was recorded at Army entry on 1943-05-12; no employer, workplace or OSS-transfer date is named.",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "A_direct_official",
                "publication_status": "publish_qualified",
                "research_notes": "The historical category is not converted into a named employer, bakery, product, workplace or exact job title.",
            },
        ]
    )
    return result


def claims() -> list[dict[str, object]]:
    result: list[dict[str, object]] = []
    for row in (1, 2):
        result.extend(
            [
                {
                    "key": f"identity-franz-stone-row{row}-b921",
                    "person_id": PEOPLE[row][0],
                    "claim_type": "identity",
                    "claim_text": "This Franz T Stone row is a possible match to Dr. Franz Stone at OSS in 1945, but the adjacent identical row prevents a row-level identity resolution.",
                    "evidence_excerpt": "Office of Strategic Services ... (Dr. Franz Stone, Ensign W. H. White)",
                    "evidence_paraphrase": "A visually checked 1945 official distribution list names Dr. Franz Stone at OSS; it does not distinguish the adjacent index rows.",
                    "identity_match_assessment": "Ambiguous. The distinctive name and direct OSS context are strong person-level evidence, but two adjacent, otherwise identical source rows cannot be allocated to one external identity.",
                    "temporal_assessment": "The official report is dated December 31, 1945. It establishes OSS context, not the pre-OSS chronology.",
                    "source_quality": "A_direct_official",
                    "claim_confidence": "low",
                    "publication_status": "withheld_low_confidence",
                    "match_notes": "The candidate is withheld from public facts and analytics until both Box 750 files are reviewed together.",
                    "sources": [
                        {"source_key": INDEX, "locator_override": f"PDF page 451 row {row}; one of two adjacent identical Franz T Stone rows"},
                        {"source_key": LOC_OSRD, "locator_override": "PDF physical page 4; distribution list visually checked"},
                    ],
                },
                {
                    "key": f"prewar-franz-stone-row{row}-opm-b921",
                    "person_id": PEOPLE[row][0],
                    "affiliation_key": f"franz-stone-row{row}-opm-b921",
                    "claim_type": "other_pre_oss_affiliation",
                    "claim_text": "A Franz T. Stone served as a special adviser in the Office of Production Management in 1941-1942, but the role cannot yet be assigned to this specific duplicate index row.",
                    "evidence_excerpt": "Special adviser, Industrial Supply Section, Tools Section, Office of Production Management",
                    "evidence_paraphrase": "The Library of Congress caption gives an exact middle-initial name and OPM role; NARA's agency history dates OPM to 1941-January 1942.",
                    "identity_match_assessment": "Low at row level because two adjacent Franz T Stone rows lack differentiating identifiers. The external source may describe one person duplicated in the index.",
                    "temporal_assessment": "Documented pre-OSS government assignment at the person-name level; not shown to be the immediate predecessor to OSS.",
                    "source_quality": "A_direct_official",
                    "claim_confidence": "low",
                    "publication_status": "withheld_low_confidence",
                    "match_notes": "Stored for duplicate review only; not published or counted in analytics.",
                    "sources": [
                        {"source_key": LOC_OPM, "locator_override": "Item caption card; LC-USE6-D-001062"},
                        {"source_key": NARA_OPM, "support_type": "context_only", "locator_override": "Sections 179.1-179.2; OPM active 1941-January 1942"},
                    ],
                },
            ]
        )
    result.extend(
        [
            {
                "key": "identity-kirk-stone-b921",
                "person_id": PEOPLE[9][0],
                "claim_type": "identity",
                "claim_text": "The indexed Kirk H Stone is a high-confidence match to geographer Kirk H. Stone documented in COI/OSS archival research.",
                "evidence_excerpt": "Kirk H. Stone to William J. Donovan, July 1 1942, RG 226 Entry 1 Box 7, Folder 14, NARA.",
                "evidence_paraphrase": "A scholarly archival study cites Stone's dated letter to Donovan and describes his July 1942 geographic research trip for COI/OSS.",
                "identity_match_assessment": "High confidence from the exact full name and middle initial, direct RG 226 letter citation, OSS context, and the professional geographer identity corroborated by the AAG obituary.",
                "temporal_assessment": "The cited letter and trip are dated July 1942; they establish wartime identity, not the immediate pre-OSS employer.",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "Box 750 remains necessary to establish recruitment chronology and the last civilian employer.",
                "sources": [
                    {"source_key": INDEX, "locator_override": "PDF page 451 row 9; Box 750"},
                    {"source_key": BARNES, "locator_override": "PDF page 2, printed page 229 and footnote 2"},
                    {"source_key": AAG, "support_type": "context_only", "locator_override": "PDF physical page 3; exact name and geography career"},
                ],
            },
            {
                "key": "prewar-kirk-stone-michigan-b921",
                "person_id": PEOPLE[9][0],
                "affiliation_key": "kirk-stone-michigan-student-b921",
                "claim_type": "other_pre_oss_affiliation",
                "claim_text": "Kirk H. Stone received a B.A. from the University of Michigan in 1935.",
                "evidence_excerpt": "Dr. Kirk Stone, B.A. University of Michigan 1935",
                "evidence_paraphrase": "The professional association obituary explicitly gives the institution, degree and year.",
                "identity_match_assessment": "High confidence when combined with the exact name, geographer profession and direct RG 226 OSS evidence.",
                "temporal_assessment": "Explicitly pre-OSS; this is a student affiliation, not employment and not shown to be immediate.",
                "source_quality": "B_authoritative_institutional",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "University attendance is not counted as an employer.",
                "sources": [{"source_key": AAG, "locator_override": "PDF physical page 3; In Memoriam"}],
            },
            {
                "key": "prewar-kirk-stone-syracuse-b921",
                "person_id": PEOPLE[9][0],
                "affiliation_key": "kirk-stone-syracuse-student-b921",
                "claim_type": "other_pre_oss_affiliation",
                "claim_text": "Kirk H. Stone received an M.A. from Syracuse University in 1937.",
                "evidence_excerpt": "M.A. Syracuse University 1937",
                "evidence_paraphrase": "The professional association obituary explicitly gives the institution, degree and year.",
                "identity_match_assessment": "High confidence when combined with the exact name, geographer profession and direct RG 226 OSS evidence.",
                "temporal_assessment": "Explicitly pre-OSS; this is a student affiliation, not employment and not shown to be immediate.",
                "source_quality": "B_authoritative_institutional",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "University attendance is not counted as an employer.",
                "sources": [{"source_key": AAG, "locator_override": "PDF physical page 3; In Memoriam"}],
            },
            {
                "key": "identity-oscar-stonorov-candidate-b921",
                "person_id": PEOPLE[20][0],
                "claim_type": "identity",
                "claim_text": "The indexed Oscar Stonorov may be the German-American architect of that distinctive name, but no reviewed source directly bridges the biography to OSS or Box 750.",
                "evidence_paraphrase": "Two institutional biographies describe the architect's Philadelphia practice and 1940s partnership, but neither mentions OSS service.",
                "identity_match_assessment": "Ambiguous. Distinctive spelling is useful discovery evidence but cannot by itself assign a biography to an index record.",
                "temporal_assessment": "The practice is documented before and during the wartime period, but its relation to OSS entry is unknown.",
                "source_quality": "B_authoritative_institutional",
                "claim_confidence": "low",
                "publication_status": "withheld_low_confidence",
                "match_notes": "The candidate is preserved for Box 750 comparison and excluded from public facts and analytics.",
                "sources": [
                    {"source_key": INDEX, "locator_override": "PDF page 451 row 20; Box 750"},
                    {"source_key": GHI, "locator_override": "Institutional biography"},
                    {"source_key": UWYO, "locator_override": "American Heritage Center collection biography"},
                ],
            },
            {
                "key": "prewar-oscar-stonorov-kahn-candidate-b921",
                "person_id": PEOPLE[20][0],
                "affiliation_key": "oscar-stonorov-kahn-candidate-b921",
                "claim_type": "other_pre_oss_affiliation",
                "claim_text": "The architect Oscar Stonorov operated a Philadelphia architectural office with Louis Kahn in the early 1940s, but this candidate is not yet linked to the index row.",
                "evidence_excerpt": "opened his own architectural office in Philadelphia together with modernist architect Louis Kahn",
                "evidence_paraphrase": "The German Historical Institute and American Heritage Center document the practice and partnership.",
                "identity_match_assessment": "Low because no independent OSS, identifier or Box 750 bridge was found.",
                "temporal_assessment": "Documented in the early 1940s for the biographical subject; relation to OSS entry remains uncertain.",
                "source_quality": "B_authoritative_institutional",
                "claim_confidence": "low",
                "publication_status": "withheld_low_confidence",
                "match_notes": "Stored only as a candidate and excluded from public facts and analytics.",
                "sources": [
                    {"source_key": GHI, "locator_override": "Biography paragraphs 3-5"},
                    {"source_key": UWYO, "locator_override": "Collection biography; 1940s partnership"},
                ],
            },
            {
                "key": "identity-william-stoppe-b921",
                "person_id": PEOPLE[23][0],
                "claim_type": "identity",
                "claim_text": "The indexed William R Stoppe row is a high-confidence match to the reviewed official Army record.",
                "evidence_paraphrase": "A nonshared protected identifier connects the visually verified index row to an exact-name official Army record.",
                "identity_match_assessment": "High confidence from exact full-name agreement and a nonshared protected-identifier bridge.",
                "temporal_assessment": "The Army entry is dated May 12, 1943; the record does not establish an OSS transfer date.",
                "source_quality": "A_direct_official",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "No protected identifier is exposed, and the coded occupation is kept separate from employer claims.",
                "sources": [
                    {"source_key": INDEX, "locator_override": "PDF page 451 row 23; protected identifier withheld"},
                    {"source_key": ARMY, "locator_override": "Accepted reviewed identity bridge; protected identifier withheld"},
                ],
            },
            {
                "key": "occupation-william-stoppe-b921",
                "person_id": PEOPLE[23][0],
                "affiliation_key": "william-stoppe-occupation-b921",
                "claim_type": "occupation",
                "claim_text": "At Army entry on May 12, 1943, William R Stoppe was recorded in the unskilled level of occupations producing bakery products, not elsewhere classified; no employer is identified.",
                "evidence_paraphrase": "The accepted Army record carries civilian-occupation code 802, decoded from NARA's official code list.",
                "identity_match_assessment": "The category belongs only to the reviewed protected-identifier match; the identifier itself is not public.",
                "temporal_assessment": "Strongly date-bounded to Army entry; it does not establish the immediate pre-OSS affiliation or a named employer.",
                "source_quality": "A_direct_official",
                "claim_confidence": "medium",
                "publication_status": "publish_qualified",
                "match_notes": "The historical category is a qualified lead, not an employer, bakery, product, workplace or exact title.",
                "sources": [
                    {"source_key": ARMY, "locator_override": "Accepted reviewed identity record; civilian occupation code 802; protected identifier withheld"},
                    {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46; Army-entry-date and civilian-occupation fields"},
                    {"source_key": CODES, "locator_override": "PDF physical page 173, printed pages XIV-XV; category 8-02", "excerpt_override": "Occupations in production of bakery products, n.e.c."},
                ],
            },
        ]
    )
    return result


def unresolved_update(row: int) -> dict[str, object]:
    person_id, name, box = PEOPLE[row]
    update: dict[str, object] = {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, Box {box} and archive location, but staged NARA/index, CIA Reading Room, exact-name OSS, occupation, employer, obituary, institutional, newspaper, Library of Congress and archival searches found no defensible identity bridge. {UNRESOLVED[row]}",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": f"Review the indexed Box {box} personnel file for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "critical",
    }
    if row == 17:
        update["personnel_category"] = "commissioned_army_officer"
        update["commissioned_officer"] = True
    else:
        update["personnel_category"] = "unknown_or_indeterminate"
    return update


def person_updates() -> list[dict[str, object]]:
    updates = [unresolved_update(row) for row in UNRESOLVED]
    for row in (1, 2):
        updates.append(
            {
                "person_id": PEOPLE[row][0],
                "identity_status": "ambiguous",
                "identity_evidence": "A 1945 official distribution list names Dr. Franz Stone at OSS, and a Library of Congress caption names Franz T. Stone at OPM in 1941-1942. Two adjacent identical index rows lack differentiating rank or public identifiers, so neither external record is assigned to one row.",
                "personnel_category": "unknown_or_indeterminate",
                "manual_review_required": True,
                "possible_duplicate_group": "same-name:franz-t-stone-page451",
                "research_status": "needs_identity_review",
                "next_action": "Review both adjacent Box 750 Franz T Stone files together to determine whether the index duplicated one person or represents two people; then allocate the OPM and OSS evidence only if supported.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            }
        )
    updates.extend(
        [
            {
                "person_id": PEOPLE[9][0],
                "identity_status": "high_confidence",
                "identity_evidence": "A scholarly archival study cites a July 1, 1942 Kirk H. Stone letter to William J. Donovan in RG 226 and describes the geographer's COI/OSS research trip. An AAG obituary corroborates the exact name and geography profession.",
                "personnel_category": "civilian_professional_or_administrative_grade",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Review Box 750 for recruitment chronology and the last civilian employer. The documented Michigan and Syracuse student affiliations are not employers.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[20][0],
                "identity_status": "ambiguous",
                "identity_evidence": "The distinctive indexed name matches a documented German-American architect, but the reviewed institutional biographies do not mention OSS service or Box 750. The architectural practice remains a withheld candidate, not a public fact.",
                "personnel_category": "unknown_or_indeterminate",
                "manual_review_required": True,
                "research_status": "needs_identity_review",
                "next_action": "Review the Box 750 personnel file for a Philadelphia, architecture, Louis Kahn or date-of-birth bridge before accepting or rejecting the Oscar Stonorov biography.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[23][0],
                "identity_status": "high_confidence",
                "identity_evidence": "An exact full name and nonshared protected identifier connect the index row to the official Army record. The record gives a private-at-entry grade, date and historical civilian-occupation code but no employer.",
                "personnel_category": "enlisted_army_personnel",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "occupation_only_found",
                "next_action": "Review Box 751 to identify the immediate pre-OSS affiliation and last civilian employer; do not convert the Army occupation category into a named bakery or employer.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
        ]
    )
    return updates


def research_attempts() -> list[dict[str, object]]:
    attempts: list[dict[str, object]] = []
    for row, (person_id, name, box) in PEOPLE.items():
        if row == 9:
            outcome = "source_reviewed"
            detail = "Archival scholarship established the geographer's COI/OSS identity; the professional-association obituary documented two prewar student affiliations but no pre-OSS employer."
        elif row == 23:
            outcome = "source_reviewed"
            detail = "An accepted protected-identifier Army bridge established identity and a dated historical civilian-occupation category, not an employer or immediate OSS predecessor."
        elif row in (1, 2):
            outcome = "candidate_found"
            detail = "Direct official sources document Dr. Franz Stone at OSS in 1945 and Franz T. Stone at OPM in 1941-1942, but two adjacent identical index rows prevent row-level allocation."
        elif row == 20:
            outcome = "candidate_found"
            detail = "Institutional biographies document the distinctive-name architect's early-1940s practice, but no reviewed source bridges that biography to OSS or Box 750."
        else:
            outcome = "candidate_rejected"
            detail = UNRESOLVED[row]
        loc_rejected = LOC_REJECTIONS.get(row, 0)
        sources_reviewed = 13 if row in (1, 2, 9, 20, 23) else 8
        attempts.append(
            {
                "key": f"page451-row{row}-{slug(name)}-b921",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA/index and public Archives context; CIA Reading Room exact-name check; OSS and rank variants; employer and occupation; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Box {box}; protected-identifier Army crosswalk where defensible",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_921",
                "started_at": "2026-10-26T08:05:00Z",
                "completed_at": "2026-10-26T08:56:00Z",
                "outcome": outcome,
                "sources_reviewed": sources_reviewed,
                "candidate_sources_rejected": (5 + loc_rejected) if row not in (1, 2, 9, 20, 23) else (3 + loc_rejected),
                "rejection_reasons": "Unbridged namesakes, discovery-only genealogy, wrong initials, OCR/token false positives, postwar-only leads and sources without an OSS or Box-file bridge were not assigned." if outcome != "candidate_rejected" else detail,
                "research_notes": f"{detail} The CIA adapter failed closed on its robots check; separate site-restricted public Reading Room searches returned no exact-name result. The Library of Congress API pass completed for all 23 people, producing 34 candidates across ten people; every candidate was individually inspected and rejected. No search snippet was used as final evidence, no access control was bypassed, and no authenticated NARA API call was made.",
                "next_action": f"Review the indexed Box {box} personnel file for corroborating identifiers and the immediate pre-OSS affiliation or last civilian employer.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b921-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-921-v1",
        "reviewer": "Before OSS Batch 921 evidence review",
        "sources": sources(),
        "organizations": organizations(),
        "affiliations": affiliations(),
        "claims": claims(),
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }
    OUTPUT.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
