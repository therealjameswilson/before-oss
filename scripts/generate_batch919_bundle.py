#!/usr/bin/env python3
"""Generate the reviewed Batch 919 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "research/evidence-page450-stites-to-henry-stokes-review_batch-919_2026-10-26.json"

INDEX = "nara-index-b919"
ARMY = "army-bulk-b919"
TECH = "army-tech-b919"
CODES = "army-codes-b919"
HRC = "hrc-grattan-stiver-b919"
NARA_TIMELINE = "nara-oss-timeline-b919"
OHIO_STIX = "ohiolink-stix-b919"
ELIA_STIX = "elia-oss-stix-b919"
OBIT_STOCKWITZ = "omps-stockwitz-b919"


PEOPLE = {
    1: ("1225ef83-5bed-5c7f-b230-cc8db024471f", "Louis E Stites", "748"),
    2: ("e76a74b1-2a05-5dfb-bfb2-c15893dc5238", "Michael L Stiver", "748"),
    3: ("6e2df8db-7754-5854-bc73-f0063ba9bc5a", "Frederick Stix", "748"),
    4: ("6f5a6c85-9821-5226-a925-69fe6ae2bc22", "Tom Stix", "748"),
    5: ("bbe9712d-6c59-574f-b72a-7ebd960c6587", "Albert B Stock", "748"),
    6: ("e021e1ca-fe8a-55e7-b3cb-192fee4fd9bd", "Grace K Stock", "748"),
    7: ("f0ca1cba-263b-517e-8f0d-2ab49e8747b8", "George J Stocker", "748"),
    8: ("91d19978-8e48-5131-9827-abe34b8f7be3", "Louise T Stockly", "748"),
    9: ("4491ad4a-2a29-5085-b9d8-710c98a1e2ed", "Robert A Stockton", "748"),
    10: ("240b615e-7100-59fa-9ce8-818859b653b2", "Stanley Stockwitz", "749"),
    11: ("b711ede2-6b15-5517-a69e-8761c4e9f479", "Gertrude Stoddard", "748"),
    12: ("37fb3056-d41f-5837-b028-2a66df481322", "Louis Stoddard", "748"),
    13: ("78e79875-9404-5857-8c86-3e67a5e4d999", "Janie E Stodghill", "748"),
    14: ("6df27dbc-aa29-5425-9493-4d692ab3246f", "Clemence F Stodolka", "749"),
    15: ("84be9c37-cc0a-549e-9008-0c046112b1bb", "Graham D Stoessel", "749"),
    16: ("fc0375ab-d463-51fd-be42-d2a7cbfc7c74", "Joan M Stoffel", "749"),
    17: ("241e2792-2f46-5e38-b648-722518ac7dd5", "Margaret B Stoffle", "749"),
    18: ("a3c55561-db1d-5f3c-b1ea-e9dbc06cff0e", "Lloyd K Stogdill", "749"),
    19: ("a46f0afb-ff51-5246-b412-84c462915d9d", "Andrew W Stohl", "749"),
    20: ("1f87fe7e-8d81-5ddf-9a3d-35c608729e35", "Adolph Stojak", "749"),
    21: ("7ab32b46-1116-5cca-9e4f-0af79b160a28", "Alexander C Stokes", "749"),
    22: ("7905888a-9ace-5607-a756-d56d0ee75653", "Fraser R Stokes", "749"),
    23: ("9c0927d4-6279-52fd-9e0e-2a8afe47203b", "Henry C Stokes", "749"),
}


UNRESOLVED = {
    1: "The official Army bulk crosswalk found no exact protected-identifier record; the source is damaged and incomplete, so the nonhit is not negative service evidence.",
    3: "Exact-name searches produced unbridged Stix namesakes and no person-specific pre-OSS employment evidence.",
    5: "The common name produced no result with a protected identifier, Box 748 reference, or documented OSS assignment.",
    6: "The Library of Congress candidate was an 1876 OCR false positive and no reliable identity or employment bridge was found.",
    7: "Five Library of Congress candidates were wrong-initial, postwar, or OCR/token false positives; no reliable identity bridge remained.",
    8: "Exact-name, occupation, obituary, institutional, newspaper, and archival searches produced no defensible match.",
    9: "The printed protected identifier is outside the Army bulk adapter's defensible enlisted-number scope, and common-name results supplied no corroborating bridge.",
    11: "Common-name results supplied no middle name, protected identifier, OSS assignment, or Box 748 bridge.",
    12: "The 1938 newspaper candidate concerned a junior namesake's racehorse, and the printed protected identifier is outside the Army bulk adapter's defensible scope.",
    13: "Exact-name and institutional searches produced no person-specific result with an OSS or Box 748 bridge.",
    14: "The official Army bulk crosswalk found no exact protected-identifier record; the source is damaged and incomplete, so the nonhit is not negative service evidence.",
    15: "Exact-name and archival searches found only the index row and no reliable employer, occupation, or identity bridge.",
    16: "Exact-name, occupation, obituary, institutional, newspaper, and archival searches produced no defensible match.",
    17: "Exact-name and spelling-variant searches returned no reliable identity or employment evidence.",
    18: "Exact-name and institutional searches produced no person-specific result with an OSS or Box 749 bridge.",
    19: "Exact-name and occupation searches produced no person-specific source with a reliable OSS connection.",
    20: "The printed identifier is outside the Army bulk adapter's defensible scope, the CIA adapter failed closed, and exact-name searches found no reliable bridge.",
    21: "The short printed identifier is outside the Army bulk adapter's defensible scope, and common-name results lacked corroborating identifiers.",
    23: "Two Library of Congress candidates were OCR/token false positives, and common-name searches produced no corroborating OSS or Box 749 bridge.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 748-749",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 450, rows 1-23; checked against layout-preserving text and a rendered page image",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 separately printed rows remain separate. Full protected identifiers remain private.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; one accepted Batch 919 protected-identifier identity bridge",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "No raw row or full protected identifier is retained in public assets. The coded occupation identifies no employer.",
        },
        {
            "key": TECH,
            "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf",
            "archival_identifier": "NN3-064-03-008; National Archives Identifier 1263923",
            "title": "World War II Army Enlistment Records: Reference Copy of Technical Documentation",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives at College Park - Electronic Records",
            "publication_record_date": "1994-2005; reference copy modified 2011",
            "locator": "PDF physical pages 44-46; identifier, name, entry-date, grade and civilian-occupation fields",
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
            "locator": "PDF physical page 171; category 1-01 visually checked",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical occupation labels identify neither employers nor workplaces.",
        },
        {
            "key": HRC,
            "stable_url": "https://norman.hrc.utexas.edu/fasearch/pdf/01097.pdf",
            "archival_identifier": "Manuscript Collection MS-1700, container 6.11",
            "title": "C. Hartley Grattan: An Inventory of His Papers at the Harry Ransom Center",
            "author_creator": "Jane McGee; Joan Sibley; Kevin O'Sullivan",
            "repository_publisher": "Harry Ransom Center, The University of Texas at Austin",
            "publication_record_date": "1993-2010 processing revisions",
            "locator": "PDF physical page 82, index of correspondents: Michael L. Stiver (Coordinator of Information)--6.11",
            "access_date": "2026-10-26",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "C. Hartley Grattan Papers",
            "rights_notes": "The finding aid identifies an organizational affiliation but does not state Stiver's role, dates, or later OSS sequence.",
        },
        {
            "key": NARA_TIMELINE,
            "stable_url": "https://www.archives.gov/research/military/ww2/oss/timeline",
            "title": "Timeline of the Office of Strategic Services (Record Group 226)",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "last reviewed 2018-12-20",
            "locator": "1940-1941 and 1942-1943 sections; COI created 1941-07-11 and OSS created 1942-06-13",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "Used for agency chronology only, not as person-specific evidence.",
        },
        {
            "key": OHIO_STIX,
            "stable_url": "https://etd.ohiolink.edu/acprod/odb_etd/ws/send_file/send?accession=kent1271704826&disposition=inline",
            "archival_identifier": "Kent State University dissertation, OhioLINK accession kent1271704826",
            "title": "Time on the Mountain: The Office of Strategic Services in Axis-Occupied Greece, 1943-1944",
            "author_creator": "Kyriakos Nalmpantis",
            "repository_publisher": "Kent State University; OhioLINK Electronic Theses and Dissertations Center",
            "publication_record_date": "2010-05",
            "locator": "PDF physical page 159, dissertation page 146; footnote 227 cites NARA RG 226/210, 283/1, Stygia Mission",
            "access_date": "2026-10-26",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "OhioLINK Electronic Theses and Dissertations Center",
            "rights_notes": "Used with the official index and the scanned OSS report to assess identity; it supplies no pre-OSS employment evidence.",
        },
        {
            "key": ELIA_STIX,
            "stable_url": "https://www.elia.org.gr/userfiles/pdf_archieve/1945%201-2745%20Peloponnesus%2C%20Thessaly%2C%20Macedonia%2C%20German%20Atrocities%2C%20Food%20Shortages%2C%20Skouras%2C%20%5B27%20pgs%5D%20226-210-WN17661%2C%20226-140-Folder%20164%20%28Admin%29.pdf",
            "archival_identifier": "NARA RG 226, Entry 210, WN 17661; RG 226, Entry 140, folder 164",
            "title": "East Central Greece, Thessaly and Western Macedonia",
            "author_creator": "Office of Strategic Services",
            "repository_publisher": "Hellenic Literary and Historical Archive (ELIA-MIET), scan of NARA record",
            "publication_record_date": "1944-11 or later",
            "locator": "PDF physical page 12; journey beginning 1944-11-17 names Lt. Tom Stix",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services",
            "rights_notes": "Official-document scan used for identity and rank context only; it supplies no pre-OSS affiliation.",
        },
        {
            "key": OBIT_STOCKWITZ,
            "stable_url": "https://ompsfuneralhome.com/obituary/stanley-stephen-stockwitz/",
            "title": "Stanley Stephen Stockwitz",
            "repository_publisher": "Omps Funeral Home",
            "publication_record_date": "2012-04",
            "locator": "Biographical paragraph; Stanley Stephen Stokwitz, born Stokwisz, Army and OSS service",
            "access_date": "2026-10-26",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Omps Funeral Home obituaries",
            "rights_notes": "The obituary's statement that OSS membership began in 1940 conflicts with the official 1942 creation date; it is used only as qualified identity context.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": "coordinator-information-b919",
            "canonical_name": "Office of the Coordinator of Information",
            "historical_name": "Coordinator of Information",
            "aliases": ["COI", "Office of Coordinator of Information"],
            "organization_type": "federal intelligence and information office",
            "sector": "federal_government",
            "country": "United States",
            "active_dates": "1941-07-11 to 1942-06-13",
            "normalization_notes": "NARA records COI as the predecessor whose functions were divided between OSS and OWI in June 1942. No individual transfer is inferred from agency succession alone.",
        }
    ]


def affiliations() -> list[dict[str, object]]:
    return [
        {
            "key": "michael-l-stiver-coi-b919",
            "person_id": PEOPLE[2][0],
            "organization_key": "coordinator-information-b919",
            "organization_name_as_found": "Coordinator of Information",
            "relationship_type": "government_assignment",
            "date_precision": "The institutional finding aid identifies the affiliation but not Stiver's role or individual dates; COI existed from July 1941 to June 1942.",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "probable",
            "claim_confidence": "medium",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "publish_qualified",
            "research_notes": "The exact uncommon name and predecessor-agency context support a probable match, but Box 748 is required to prove identity and whether this was immediate before the indexed OSS service.",
        },
        {
            "key": "fraser-r-stokes-occupation-b919",
            "person_id": PEOPLE[22][0],
            "relationship_type": "employment",
            "occupation": "Bookkeepers and cashiers, except bank cashiers",
            "end_date": "1943-06-07",
            "date_precision": "Historical civilian-occupation code 101 was recorded at Army entry on 1943-06-07; no employer or OSS-transfer date is named.",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "high_confidence",
            "claim_confidence": "medium",
            "source_quality": "A_direct_official",
            "publication_status": "publish_qualified",
            "research_notes": "The historical category is not converted into a named employer, workplace, bank role, or exact title.",
        },
    ]


def claims() -> list[dict[str, object]]:
    return [
        {
            "key": "coi-michael-l-stiver-b919",
            "person_id": PEOPLE[2][0],
            "affiliation_key": "michael-l-stiver-coi-b919",
            "claim_type": "other_pre_oss_affiliation",
            "claim_text": "A Harry Ransom Center finding aid probably identifies the indexed Michael L. Stiver with the Office of the Coordinator of Information, the 1941-1942 predecessor context for OSS and OWI.",
            "evidence_excerpt": "Stiver, Michael L. (Coordinator of Information)--6.11",
            "evidence_paraphrase": "The institutional correspondent index attaches the exact uncommon name to COI; NARA dates COI before OSS but the item-level letter and Box 748 file remain unreviewed.",
            "identity_match_assessment": "Probable from the exact uncommon full name and the exceptionally specific predecessor-agency context, without a protected identifier or item-level OSS bridge.",
            "temporal_assessment": "Documented in the 1941-1942 COI period, but neither individual dates nor immediate transition into OSS are established.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "medium",
            "publication_status": "publish_qualified",
            "match_notes": "Published with qualification as a government affiliation, not as a civilian employer or proven immediate predecessor.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 450 row 2; Box 748"},
                {"source_key": HRC, "locator_override": "PDF physical page 82; correspondent index; container 6.11"},
                {"source_key": NARA_TIMELINE, "support_type": "context_only", "locator_override": "COI and OSS creation dates"},
            ],
        },
        {
            "key": "identity-tom-stix-b919",
            "person_id": PEOPLE[4][0],
            "claim_type": "identity",
            "claim_text": "The indexed 1st Lt. Tom Stix is a high-confidence match to the OSS lieutenant documented in Greece and identified as commander of Secret Intelligence mission Stygia.",
            "evidence_excerpt": "Lt. Tom Stix, commander of the SI mission Operation Stygia",
            "evidence_paraphrase": "The index rank and exact name align with an official OSS report naming Lt. Tom Stix and a scholarly account tied to NARA mission records.",
            "identity_match_assessment": "High confidence from exact name, matching lieutenant rank, OSS context, Greece documentation, and a NARA-cited mission record.",
            "temporal_assessment": "The sources establish wartime OSS identity and assignment, but provide no pre-OSS employer or predecessor affiliation.",
            "source_quality": "A_direct_official",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "The identity bridge does not transfer unbridged radio-work namesake evidence or create a pre-OSS affiliation claim.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 450 row 4; rank 1ST LT; protected identifier withheld"},
                {"source_key": ELIA_STIX, "locator_override": "PDF physical page 12; journey beginning 1944-11-17"},
                {"source_key": OHIO_STIX, "locator_override": "PDF physical page 159, dissertation page 146; footnote 227"},
            ],
        },
        {
            "key": "identity-stanley-stockwitz-b919",
            "person_id": PEOPLE[10][0],
            "claim_type": "identity",
            "claim_text": "A 2012 obituary for Stanley Stephen Stokwitz, born Stokwisz, is a probable match to the indexed Stanley Stockwitz, but its claim of OSS membership in 1940 is chronologically inconsistent.",
            "evidence_excerpt": "He joined the United States Army in 1940 as a member of the Office of Strategic Services",
            "evidence_paraphrase": "The unusual surname variants and OSS/Army context support a probable identity lead; NARA dates OSS creation to June 1942, so the obituary cannot establish service chronology.",
            "identity_match_assessment": "Probable from the distinctive near-exact surname, first name, Army service, and explicit OSS reference, but without a protected identifier or Box 749 linkage.",
            "temporal_assessment": "Conflicting: the obituary assigns OSS membership to 1940, two years before the official creation date. No pre-OSS employer is stated.",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "claim_confidence": "medium",
            "publication_status": "publish_qualified",
            "match_notes": "The chronology is visibly qualified and excluded from affiliation and employer analytics; Box 749 must resolve identity and dates.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 450 row 10; Box 749"},
                {"source_key": OBIT_STOCKWITZ, "locator_override": "Biographical paragraph"},
                {"source_key": NARA_TIMELINE, "support_type": "contradicts", "locator_override": "OSS created 1942-06-13"},
            ],
        },
        {
            "key": "identity-fraser-r-stokes-b919",
            "person_id": PEOPLE[22][0],
            "claim_type": "identity",
            "claim_text": "The indexed Fraser R. Stokes row is a high-confidence match to the reviewed official Army record.",
            "evidence_paraphrase": "A nonshared protected identifier and exact name connect the visually verified index row to the official Army record.",
            "identity_match_assessment": "High confidence from the nonshared protected-identifier bridge and exact name alignment.",
            "temporal_assessment": "The Army record supports identity and a dated occupation category; it does not establish the OSS transfer sequence.",
            "source_quality": "A_direct_official",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "No protected identifier is exposed, and the coded occupation is kept separate from employer claims.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 450 row 22; protected identifier withheld"},
                {"source_key": ARMY, "locator_override": "Accepted reviewed identity bridge; protected identifier withheld"},
            ],
        },
        {
            "key": "occupation-fraser-r-stokes-b919",
            "person_id": PEOPLE[22][0],
            "affiliation_key": "fraser-r-stokes-occupation-b919",
            "claim_type": "occupation",
            "claim_text": "At Army entry on 1943-06-07, the official record assigned Fraser R. Stokes the historical civilian-occupation category 'Bookkeepers and cashiers, except bank cashiers'; no employer is identified.",
            "evidence_paraphrase": "The Army entry field carries code 101, which the visually checked NARA code list maps to the stated category.",
            "identity_match_assessment": "High confidence from a nonshared protected-identifier bridge and exact name alignment.",
            "temporal_assessment": "Strongly date-bounded at Army entry, but neither immediate pre-OSS status nor a named employer is established.",
            "source_quality": "A_direct_official",
            "claim_confidence": "medium",
            "publication_status": "publish_qualified",
            "match_notes": "Historical code-language is retained and excluded from default confirmed/high-confidence employer analytics.",
            "sources": [
                {"source_key": ARMY, "locator_override": "Army-entry date 1943-06-07; occupation code 101; protected identifier withheld"},
                {"source_key": TECH, "support_type": "context_only", "locator_override": "Civilian-occupation field definition"},
                {"source_key": CODES, "locator_override": "PDF physical page 171; category 1-01"},
            ],
        },
    ]


def unresolved_update(row: int) -> dict[str, object]:
    person_id, name, box = PEOPLE[row]
    return {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, Box {box} and archive location, but staged official-context, CIA Reading Room, exact-name OSS, occupation, employer, obituary, institutional, newspaper, Library of Congress and archival searches found no defensible identity bridge. {UNRESOLVED[row]}",
        "personnel_category": "unknown_or_indeterminate",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": f"Review the indexed Box {box} personnel file for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "critical",
    }


def person_updates() -> list[dict[str, object]]:
    updates = [unresolved_update(row) for row in UNRESOLVED]
    updates.extend(
        [
            {
                "person_id": PEOPLE[2][0],
                "identity_status": "probable",
                "identity_evidence": "The exact uncommon full name and a Harry Ransom Center correspondent index connect Michael L. Stiver to the Office of the Coordinator of Information, but no protected identifier, item-level letter, or direct Box 748 bridge has been reviewed.",
                "personnel_category": "unknown_or_indeterminate",
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Review Box 748 and HRC container 6.11 to confirm identity, role, dates, the transition from COI, and the last civilian employer before wartime government service.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[4][0],
                "identity_status": "high_confidence",
                "identity_evidence": "The visually verified index prints Tom Stix as a first lieutenant. An official OSS report names Lt. Tom Stix in Greece, and a NARA-cited dissertation identifies him as commander of SI mission Stygia.",
                "personnel_category": "commissioned_army_officer",
                "commissioned_officer": True,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Review Box 748 and the Stygia mission file to establish a full name, corroborating identifiers, immediate pre-OSS affiliation, and last civilian employer; do not transfer unbridged radio-work namesake evidence.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[10][0],
                "identity_status": "probable",
                "identity_evidence": "A funeral-home obituary identifies Stanley Stephen Stokwitz, born Stokwisz, with Army and OSS service. The distinctive name supports a probable match, but no Box 749 or protected-identifier bridge is available and its 1940 OSS date conflicts with NARA's 1942 creation date.",
                "name_variants": ["Stanley Stephen Stokwitz", "Stanley Stephen Stokwisz"],
                "personnel_category": "unknown_or_indeterminate",
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Review Box 749 for full name, birth details, Army entry, OSS chronology, and pre-service occupation. Treat the obituary's 1940 OSS wording as an anachronism unless the file explains it.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[22][0],
                "identity_status": "high_confidence",
                "identity_evidence": "A nonshared protected identifier and exact name connect the visually verified index row to the reviewed official Army record. The historical occupation field remains separate from employer and immediate-affiliation claims.",
                "personnel_category": "enlisted_army_personnel",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "occupation_only_found",
                "next_action": "Review the indexed Box 749 personnel file to identify the immediate pre-OSS affiliation and last civilian employer; do not convert the Army occupation category into a named employer.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
        ]
    )
    return updates


def research_attempts() -> list[dict[str, object]]:
    sourced_rows = {2, 4, 10, 22}
    attempts: list[dict[str, object]] = []
    for row, (person_id, name, box) in PEOPLE.items():
        if row in sourced_rows:
            outcome = "source_reviewed"
            if row == 2:
                detail = "A qualified COI affiliation was documented, but immediate sequence and any civilian employer remain unresolved."
            elif row == 4:
                detail = "Official and scholarly OSS records established a high-confidence lieutenant/mission identity bridge but no pre-OSS employment."
            elif row == 10:
                detail = "A distinctive obituary lead supports a probable identity while its 1940 OSS chronology was rejected as anachronistic."
            else:
                detail = "An accepted protected-identifier Army bridge established identity and a dated historical occupation category, not an employer."
        else:
            outcome = "candidate_rejected"
            detail = UNRESOLVED[row]
        attempts.append(
            {
                "key": f"page450-row{row}-{slug(name)}-b919",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA/index and public Catalog context; CIA Reading Room exact-name check; OSS and rank variants; employer and occupation; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Box {box}; protected-identifier Army crosswalk where defensible",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_919",
                "started_at": "2026-10-26T05:40:00Z",
                "completed_at": "2026-10-26T07:25:00Z",
                "outcome": outcome,
                "sources_reviewed": 10 if row in sourced_rows else 6,
                "candidate_sources_rejected": 5 if row in sourced_rows else (9 if row in {6, 7, 12, 23} else 7),
                "rejection_reasons": "Unbridged namesakes, discovery-only results, chronologically impossible wording, OCR/token false positives, and postwar-only leads were not assigned." if row in sourced_rows else detail,
                "research_notes": f"{detail} The CIA adapter failed closed when its robots endpoint was unavailable. The current Library of Congress API pass completed for all 23 people; nine returned discovery candidates were inspected and rejected where unsupported. No search snippet was used as evidence, no access control was bypassed, and no exposed NARA API credential was used.",
                "next_action": f"Review the indexed Box {box} personnel file for corroborating identifiers and the last documented pre-OSS affiliation.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b919-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-919-v1",
        "reviewer": "Before OSS Batch 919 evidence review",
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
