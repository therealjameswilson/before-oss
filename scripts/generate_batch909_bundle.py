#!/usr/bin/env python3
"""Generate the reviewed Batch 909 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "research/evidence-page445-starr-to-stauski-review_batch-909_2026-10-25.json"

INDEX = "nara-index-b909"
ARMY = "army-bulk-b909"
TECH = "army-tech-b909"
CODES = "army-codes-b909"
STARZ_SWJ = "army-swj-starz-b909"
STATHAKOS_GREECE = "elia-oss-greece-stathakos-b909"
STATHAKOS_GO = "war-department-go54-stathakos-b909"
STATHAKOS_TEXAS = "ut-athletics-stathakos-b909"
STATHAKOS_OBIT = "nyt-obit-stathakos-b909"
STATHIS_OBIT = "brooklyn-eagle-stathis-transcript-b909"
NPS_STARRETT = "nps-starrett-training-b909"
ARMY_STAUB = "army-review-staub-varsity-b909"


PEOPLE = {
    1: ("b1685cc0-d3cf-54d2-a9c7-3b92852ac8f8", "Roy C Starr"),
    2: ("9563b55e-8c83-5f50-b973-487895c64674", "Deane W Starret"),
    3: ("86100598-9e66-5137-8559-5c852307cc51", "Dean W Starrett"),
    4: ("3ff1fc9b-5a54-5f9c-9eaa-ef99ea9e38a8", "Mason B Starring"),
    5: ("62d18c8f-69b7-5962-8666-6aef2daaf3ab", "William T Starry"),
    6: ("aab8d590-c457-5db9-91e7-a6ca3c505597", "Kenneth E Startin"),
    7: ("9109e767-6ce5-5178-bd4d-baf402786df2", "William T Starube"),
    8: ("ab3758cd-057e-5e6c-8409-3ede780bfad4", "John G Stary"),
    9: ("5dbb75e0-b230-582d-b728-792e44598543", "Edward Starz"),
    10: ("a5228d9e-ffe2-5b64-915b-f8a6f4f686e2", "Edward A Starz"),
    11: ("20a2b661-e75a-5fd1-b0ff-ff13b891fae4", "Albert E Stasik"),
    12: ("6314c9c2-b677-51a6-96b2-4fa806ab07fc", "Ernest A Stasik"),
    13: ("4a522807-5f4b-5e86-8f9d-65517629ada0", "Marion F Staszewski"),
    14: ("7c036c19-c382-5e31-90bb-96db7e27f6e1", "James F Stathakos"),
    15: ("476f017e-56e5-5bb9-9f73-c8cc70d84be4", "George J Stathis"),
    16: ("de0f3b3e-b86f-5da3-b4c4-8b1656610639", "Joseph M Staub"),
    17: ("62cf1bb0-6d6e-5819-9d76-649968d9fc1f", "Robert Staub"),
    18: ("f6ea5939-6163-59f6-a9b3-3fe7e848fc26", "Robert Staub"),
    19: ("18006384-c6a7-5e5f-b4b0-a38c3c5d91c1", "Robert W Stauder"),
    20: ("e1b3b47a-313f-561c-854a-dbc208ebe40b", "Harold D Stauffer"),
    21: ("2644026f-3e34-5d35-81a6-d9416b6d1fe5", "John R Stauffer"),
    22: ("c70de78a-8c12-559d-b5d3-83fddb11f3d7", "Theodore R Stauffer"),
    23: ("b06886da-6567-55a5-a875-762ed33b51d3", "Joe F Stauski"),
}


ARMY_OCCUPATIONS = [
    {"row": 1, "date": "1943-01-20", "code": "126", "occupation": "Paymasters, payroll clerks, and timekeepers", "locator": "PDF physical page 171; category 1-26", "army_name": "STARR ROY C JR"},
    {"row": 5, "date": "1941-02-17", "code": "002", "occupation": "Actors and actresses", "locator": "PDF physical page 170; category 0-02"},
    {"row": 8, "date": "1944-01-18", "code": "992", "occupation": "Students", "locator": "PDF physical page 304; amended category 9-92"},
    {"row": 15, "date": "1943-03-11", "code": "071", "occupation": "Hotel and restaurant managers", "locator": "PDF physical page 171; category 0-71"},
    {"row": 17, "date": "1942-07-31", "code": "144", "occupation": "Ticket, station, and express agents, transportation", "locator": "PDF physical page 171; category 1-44"},
    {"row": 22, "date": "1943-02-11", "code": "340", "occupation": "Gardeners and grounds keepers, parks, cemeteries, etc.", "locator": "PDF physical page 172; category 3-40", "army_name": "STAUFFER THEODORE R JR"},
    {"row": 23, "date": "1942-12-07", "code": "922", "occupation": "Occupations in extraction of minerals, n.e.c.", "locator": "PDF physical page 174; category 9-22"},
]


RANK_CLASSIFICATION = {
    3: ("enlisted_army_personnel", False),
    4: ("commissioned_army_officer", True),
    10: ("enlisted_army_personnel", False),
    11: ("enlisted_army_personnel", False),
    12: ("enlisted_army_personnel", False),
    14: ("commissioned_army_officer", True),
    15: ("enlisted_army_personnel", False),
    16: ("enlisted_army_personnel", False),
    18: ("commissioned_army_officer", True),
}


UNRESOLVED = {
    2: "The adjacent Deane W. Starret and Dean W. Starrett rows combine the exact spelling used by a postwar CIA archival citation; neither row can receive that biography without personnel-file evidence.",
    3: "The adjacent Deane W. Starret and Dean W. Starrett rows combine the exact spelling used by a postwar CIA archival citation; neither row can receive that biography without personnel-file evidence.",
    4: "Financial and business references for a same-name person lack an OSS, rank, officer-number, age or other person-specific bridge.",
    6: "A cemetery lead for a career Air Force man of this name supplies no protected identifier, OSS assignment or compatible chronology.",
    7: "The unusual printed surname produced no person-specific official, institutional, newspaper, directory or obituary result.",
    9: "This no-initial row remains separate from the adjacent Edward A. Starz row, whose protected identifier, rank and official OSS role are more specific.",
    11: "A same-name Chicago obituary supplies no protected identifier or OSS bridge and is not assigned to this technician-third-grade row.",
    12: "Exact-name and rank searches produced no defensible identity bridge or dated pre-OSS affiliation.",
    13: "Exact-name, occupation, employer, obituary and archival searches produced no defensible person-specific result.",
    16: "The common name and technical-sergeant rank produced no source with a compatible identifier or person-specific OSS assignment.",
    18: "An official Army history names an OSS operative Robert Staub but supplies no rank or identifier capable of distinguishing this lieutenant row from the adjacent enlisted row.",
    19: "The officer-format number is not treated as proof of rank, and searched sources supplied no person-specific identity or employment bridge.",
    20: "The officer-format number is not treated as proof of rank, and common-name searches supplied no corroborating OSS assignment or employment chronology.",
    21: "The officer-format number is not treated as proof of rank, and searched sources supplied no corroborating OSS assignment or employment chronology.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 739, 740 and 752",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 445, rows 1-23; checked against layout-preserving text and a rendered page image",
            "access_date": "2026-10-25",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain immutable. Full protected identifiers remain private; the Starret/Starrett, Starz and Staub clusters remain separate.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; seven accepted reviewed identity bridges",
            "access_date": "2026-10-25",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "No raw Army row or full protected identifier is retained in public assets. Coded occupations identify no employer.",
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
            "access_date": "2026-10-25",
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
            "locator": "PDF physical pages 170-174 and 304; all seven Batch 909 codes visually and textually checked",
            "access_date": "2026-10-25",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical labels identify neither employers nor workplaces. The amended table on physical page 304 maps code 992 to Students.",
        },
        {
            "key": STARZ_SWJ,
            "stable_url": "https://www.swcs.mil/Special-Warfare-Journal/Article/4222259/drop-improvise-win-the-oss-in-china/",
            "title": "Drop, Improvise, Win: The OSS in China",
            "author_creator": "Lt. Col. Zachary Griffiths",
            "repository_publisher": "U.S. Army John F. Kennedy Special Warfare Center and School",
            "publication_record_date": "2025-06-20",
            "locator": "Special Warfare Journal 38, no. 1, pages 34-39; Operation Cardinal team description",
            "access_date": "2026-10-25",
            "source_quality": "A_direct_official",
            "collection_name": "Special Warfare Journal",
            "rights_notes": "Used for a concise identity and wartime-role claim; it provides no pre-OSS employer.",
        },
        {
            "key": STATHAKOS_GREECE,
            "stable_url": "https://www.elia.org.gr/userfiles/pdf_archieve/1945%201-1845%20OSS%20Base%2C%20OSS%20Agents%2C%20%5B7%20pgs%5D%20226-211%20WN22856%20%28Admin%29.pdf",
            "archival_identifier": "RG 226-211, WN 22856; declassified OSS base personnel report",
            "title": "OSS Base and OSS Agents personnel report",
            "author_creator": "Office of Strategic Services",
            "repository_publisher": "Hellenic Literary and Historical Archive (ELIA)",
            "publication_record_date": "1945",
            "locator": "Seven-page declassified record, roster entry for James F. Stathakos, First Lieutenant, operative, Greece",
            "access_date": "2026-10-25",
            "source_quality": "A_direct_official",
            "collection_name": "Declassified OSS records",
            "rights_notes": "The scan's OCR renders the surname imperfectly; the page image and search transcription were checked in context.",
        },
        {
            "key": STATHAKOS_GO,
            "stable_url": "https://www.6thinfantry.com/wp-content/uploads/2020/06/medal-of-honor-awards-posthumously-WWII_Part1.pdf",
            "archival_identifier": "War Department General Orders No. 54 (1946)",
            "title": "War Department General Orders No. 54",
            "author_creator": "United States War Department",
            "repository_publisher": "U.S. Government Printing Office; digitized mirror hosted by 6th Infantry",
            "publication_record_date": "1946",
            "locator": "Bronze Star Medal list for Captain James F. Stathakos, Infantry, Army of the United States, July-October 1944; officer number withheld",
            "access_date": "2026-10-25",
            "source_quality": "A_direct_official",
            "collection_name": "War Department General Orders",
            "document_number": "General Orders No. 54",
            "rights_notes": "Official government text on a third-party mirror. Its protected officer number conflicts with the index and is not silently reconciled or exposed.",
        },
        {
            "key": STATHAKOS_TEXAS,
            "stable_url": "https://texaslonghorns.com/documents/download/2018/4/23/Texas_Baseball_Honors.pdf",
            "title": "Texas Baseball Honors and Awards",
            "author_creator": "University of Texas Athletics",
            "repository_publisher": "University of Texas at Austin",
            "publication_record_date": "2018",
            "locator": "PDF page 19, T-Association/letterwinners: Stathakos, James F. (1939)",
            "access_date": "2026-10-25",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Texas Baseball historical records",
            "rights_notes": "The institutional list establishes documented student-athlete status, not employment.",
        },
        {
            "key": STATHAKOS_OBIT,
            "stable_url": "https://www.legacy.com/us/obituaries/nytimes/name/james-stathakos-obituary?id=24566320",
            "title": "James F. Stathakos obituary",
            "repository_publisher": "The New York Times via Legacy.com",
            "publication_record_date": "2013-03-03",
            "locator": "Biographical notice: University of Texas law degree; U.S. Army officer; wartime service in occupied Greece",
            "access_date": "2026-10-25",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "rights_notes": "The family notice says Office of Special Services; the project does not silently quote that as the agency's formal name. Postwar employment is not republished.",
        },
        {
            "key": STATHIS_OBIT,
            "stable_url": "https://www.508pir.org/obits/obit_text/s/stathis_gj.htm",
            "title": "George J. Stathis contemporary obituary transcriptions",
            "repository_publisher": "508th Parachute Infantry Regiment historical archive",
            "publication_record_date": "1954-09-17 and 1954-09-23",
            "locator": "Brooklyn Daily Eagle, 23 September 1954, page 15; Portsmouth Herald, 17 September 1954, page 3",
            "access_date": "2026-10-25",
            "source_quality": "D_correlative_or_secondary",
            "collection_name": "508th PIR obituary archive",
            "rights_notes": "A secondary transcription of named contemporary newspapers. It supports a qualified earlier association, not a settled employer claim.",
        },
        {
            "key": NPS_STARRETT,
            "stable_url": "https://www.nps.gov/articles/summary-and-conclusion.htm",
            "archival_identifier": "RG 226, Entry 161, Box 2, Folder 32",
            "title": "Summary and Conclusion: OSS Training in the National Parks and Service Abroad in World War II",
            "author_creator": "John Whiteclay Chambers II",
            "repository_publisher": "National Park Service",
            "publication_record_date": "2008; web edition updated 2017",
            "locator": "Note citing Deane W. Starrett, Chief, CIA Training Materials and Research Section, memorandum of 16 May 1949",
            "access_date": "2026-10-25",
            "source_quality": "B_authoritative_institutional",
            "rights_notes": "Private identity lead only: its spelling combines features of two adjacent index rows and supplies no protected identifier.",
        },
        {
            "key": ARMY_STAUB,
            "stable_url": "https://www.armyupress.army.mil/Journals/Military-Review/Online-Exclusive/2024-OLE/Glorious-Amateurs/",
            "title": "Glorious Amateurs at War: Measuring the Effectiveness and Performance of the Office of Strategic Services",
            "author_creator": "Maj. Benjamin J. Lyman, U.S. Army",
            "repository_publisher": "Army University Press, Military Review",
            "publication_record_date": "2024",
            "locator": "Operation Varsity case study naming OSS subordinate Robert Staub",
            "access_date": "2026-10-25",
            "source_quality": "A_direct_official",
            "collection_name": "Military Review Online Exclusive",
            "rights_notes": "Private identity lead only because the article supplies no rank or identifier to distinguish the two adjacent Robert Staub rows.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": "university-texas-austin-b909",
            "organization_id": "b32bddda-c39e-5948-a605-0a2b0a1d3a97",
            "canonical_name": "University of Texas at Austin",
            "historical_name": "University of Texas",
            "aliases": ["The University of Texas", "UT Austin"],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "Austin",
            "state_or_region": "Texas",
            "country": "United States",
            "normalization_notes": "The 1939 institutional athletics record uses the University of Texas context. Student status is not employment.",
        },
        {
            "key": "seaford-restaurant-b909",
            "canonical_name": "Seaford Restaurant",
            "historical_name": "Seaford Restaurant",
            "aliases": [],
            "organization_type": "restaurant",
            "sector": "business_and_industry",
            "city": "Brooklyn",
            "state_or_region": "New York",
            "country": "United States",
            "normalization_notes": "Preserves the historical name in the 1954 obituary transcription; no modern successor is asserted.",
        },
    ]


def army_affiliation(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    person_id, name = PEOPLE[row]
    return {
        "key": f"{slug(name)}-row{row}-occupation-b909",
        "person_id": person_id,
        "relationship_type": "student" if item["occupation"] == "Students" else "employment",
        "occupation": item["occupation"],
        "end_date": item["date"],
        "date_precision": f"Historical civilian-occupation code {item['code']} was recorded at Army entry on {item['date']}; no employer or OSS-transfer date is named.",
        "country": "United States",
        "immediate_pre_oss": False,
        "last_civilian_pre_service": False,
        "pre_oss_temporal_basis": "strongly_date_bounded",
        "identity_confidence": "high_confidence",
        "claim_confidence": "medium",
        "source_quality": "A_direct_official",
        "publication_status": "publish_qualified",
        "research_notes": "The historical category is not converted into a named employer, workplace or exact title.",
    }


def army_claims(item: dict[str, object]) -> list[dict[str, object]]:
    row = int(item["row"])
    person_id, name = PEOPLE[row]
    name_note = " The Army record adds Jr.; the index wording remains unchanged." if row in {1, 22} else ""
    return [
        {
            "key": f"identity-{slug(name)}-row{row}-b909",
            "person_id": person_id,
            "claim_type": "identity",
            "claim_text": f"The indexed {name} row is a high-confidence match to the reviewed official Army record.",
            "evidence_paraphrase": f"A nonshared protected identifier and compatible name connect the visually verified index row to the official Army record.{name_note}",
            "identity_match_assessment": "High confidence from the nonshared protected-identifier bridge and compatible name.",
            "temporal_assessment": "The Army record supports identity and a dated occupation category; it does not establish the OSS transfer sequence.",
            "source_quality": "A_direct_official",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "No protected identifier is exposed, and the coded occupation is kept separate from employer claims.",
            "sources": [
                {"source_key": INDEX, "locator_override": f"PDF page 445 row {row}; protected identifier withheld"},
                {"source_key": ARMY, "locator_override": f"Accepted reviewed identity bridge; Army name {item.get('army_name', name)}; protected identifier withheld"},
            ],
        },
        {
            "key": f"occupation-{slug(name)}-row{row}-b909",
            "person_id": person_id,
            "affiliation_key": f"{slug(name)}-row{row}-occupation-b909",
            "claim_type": "occupation",
            "claim_text": f"At Army entry on {item['date']}, the official record assigned {name} the historical civilian-occupation category '{item['occupation']}'; no employer is identified.",
            "evidence_paraphrase": f"The Army entry field carries code {item['code']}, which the visually checked NARA code list maps to the stated category.",
            "identity_match_assessment": "High confidence from a nonshared protected-identifier bridge and compatible name.",
            "temporal_assessment": "Strongly date-bounded at Army entry, but neither immediate pre-OSS status nor a named employer is established.",
            "source_quality": "A_direct_official",
            "claim_confidence": "medium",
            "publication_status": "publish_qualified",
            "match_notes": "Historical code-language is retained and excluded from default confirmed/high-confidence employer analytics.",
            "sources": [
                {"source_key": ARMY, "locator_override": f"Army-entry date {item['date']}; occupation code {item['code']}; protected identifier withheld"},
                {"source_key": TECH, "support_type": "context_only", "locator_override": "Civilian-occupation field definition"},
                {"source_key": CODES, "locator_override": item["locator"]},
            ],
        },
    ]


def additional_affiliations() -> list[dict[str, object]]:
    return [
        {
            "key": "james-f-stathakos-ut-student-b909",
            "person_id": PEOPLE[14][0],
            "organization_key": "university-texas-austin-b909",
            "organization_name_as_found": "University of Texas",
            "role_title": "baseball letterwinner",
            "occupation": "student",
            "relationship_type": "student",
            "end_date": "1939",
            "date_precision": "The institutional record lists James F. Stathakos as a 1939 baseball letterwinner; an obituary reports a law degree but gives no graduation year.",
            "city": "Austin",
            "state_or_region": "Texas",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "conflicting",
            "claim_confidence": "medium",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "publish_qualified",
            "research_notes": "Published as student status, not employment. The index and War Department officer numbers conflict, so the identity is visibly qualified.",
        },
        {
            "key": "george-j-stathis-seaford-association-b909",
            "person_id": PEOPLE[15][0],
            "organization_key": "seaford-restaurant-b909",
            "organization_name_as_found": "Seaford Restaurant",
            "relationship_type": "professional_affiliation",
            "date_precision": "A 1954 obituary says Stathis renewed this association after the war, establishing an earlier association without specifying its role, dates or whether it was the final pre-service affiliation.",
            "city": "Brooklyn",
            "state_or_region": "New York",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "high_confidence",
            "claim_confidence": "medium",
            "source_quality": "D_correlative_or_secondary",
            "publication_status": "publish_qualified",
            "research_notes": "The protected-identifier bridge and matching 1943 restaurant-manager category support identity. Association is not silently converted into employment.",
        },
    ]


def substantive_claims() -> list[dict[str, object]]:
    claims: list[dict[str, object]] = [
        {
            "key": "identity-edward-a-starz-cardinal-b909",
            "person_id": PEOPLE[10][0],
            "claim_type": "identity",
            "claim_text": "The indexed Technician Fourth Grade Edward A. Starz is a high-confidence match to the OSS radio operator on Operation Cardinal in Manchuria.",
            "evidence_excerpt": "Sgt. Edward A. Starz served as the radio operator",
            "evidence_paraphrase": "An official Army Special Warfare account names the exact person and his OSS communications role on the August 1945 mission.",
            "identity_match_assessment": "High confidence from the uncommon exact name, compatible enlisted rank and person-specific OSS assignment; the adjacent no-initial row remains separate.",
            "temporal_assessment": "The source establishes wartime OSS service, not the immediate pre-OSS affiliation or a civilian employer.",
            "source_quality": "A_direct_official",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "No pre-OSS employer is inferred from communications duty. The adjacent Edward Starz record is not merged.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 445 row 10; T/4; protected identifier withheld"},
                {"source_key": STARZ_SWJ, "locator_override": "Special Warfare Journal 38, no. 1, Operation Cardinal team description"},
            ],
        },
        {
            "key": "identity-james-f-stathakos-conflict-b909",
            "person_id": PEOPLE[14][0],
            "claim_type": "identity",
            "claim_text": "The indexed Captain James F. Stathakos is a probable match to the Army officer and OSS operative in Greece, but the printed officer number conflicts with the War Department order.",
            "evidence_paraphrase": "The rare exact name, compatible rank, OSS Greece roster and biographical notice align, but the protected officer numbers in the index and 1946 order do not agree.",
            "identity_match_assessment": "Probable, with a material identifier conflict preserved for personnel-file review.",
            "temporal_assessment": "The sources establish wartime Army and OSS service but do not document the transfer into OSS or an immediate pre-OSS affiliation.",
            "source_quality": "A_direct_official",
            "claim_confidence": "medium",
            "publication_status": "publish_qualified",
            "match_notes": "The project neither corrects nor normalizes away the conflicting officer numbers.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 445 row 14; Captain; protected officer number withheld"},
                {"source_key": STATHAKOS_GO, "locator_override": "General Orders No. 54: Captain James F. Stathakos; protected officer number withheld"},
                {"source_key": STATHAKOS_GREECE, "locator_override": "Roster: James F. Stathakos, First Lieutenant, operative, Greece"},
                {"source_key": STATHAKOS_OBIT, "support_type": "context_only", "locator_override": "Biographical notice: Army officer, occupied Greece"},
            ],
        },
        {
            "key": "student-james-f-stathakos-ut-b909",
            "person_id": PEOPLE[14][0],
            "affiliation_key": "james-f-stathakos-ut-student-b909",
            "claim_type": "other_pre_oss_affiliation",
            "claim_text": "James F. Stathakos was a University of Texas student and 1939 baseball letterwinner; the university is not classified as his employer.",
            "evidence_excerpt": "Stathakos, James F. (1939)",
            "evidence_paraphrase": "The university's athletics history lists him among 1939 letterwinners, while the obituary reports that he earned a law degree there.",
            "identity_match_assessment": "Medium confidence because the distinctive biographical pattern aligns but the wartime officer-number conflict remains unresolved.",
            "temporal_assessment": "Documented prewar student status; it is not shown to be the immediately prior affiliation and is not employment.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "medium",
            "publication_status": "publish_qualified",
            "match_notes": "Excluded from employer analytics and visibly qualified on the profile.",
            "sources": [
                {"source_key": STATHAKOS_TEXAS, "locator_override": "PDF page 19, T-Association/letterwinners"},
                {"source_key": STATHAKOS_OBIT, "support_type": "context_only", "locator_override": "University of Texas law degree"},
            ],
        },
        {
            "key": "affiliation-george-j-stathis-seaford-b909",
            "person_id": PEOPLE[15][0],
            "affiliation_key": "george-j-stathis-seaford-association-b909",
            "claim_type": "other_pre_oss_affiliation",
            "claim_text": "George J. Stathis had a documented prewar association with the Seaford Restaurant, but the accessible source does not identify his earlier role or prove that it was his final pre-service employer.",
            "evidence_excerpt": "renewed his association with the Seaford Restaurant",
            "evidence_paraphrase": "A transcribed 1954 Brooklyn Daily Eagle obituary states that he resumed the association after the war; his Army entry record independently coded him as a hotel and restaurant manager.",
            "identity_match_assessment": "High confidence from the protected-identifier Army bridge, exact name, compatible enlisted rank and matching restaurant occupation context.",
            "temporal_assessment": "The word renewed establishes an earlier association but not its precise dates, role, immediacy or legal employment relationship.",
            "source_quality": "D_correlative_or_secondary",
            "claim_confidence": "medium",
            "publication_status": "publish_qualified",
            "match_notes": "Modeled as professional affiliation and excluded from settled-employer counts.",
            "sources": [
                {"source_key": STATHIS_OBIT, "locator_override": "Brooklyn Daily Eagle transcription, 23 September 1954, page 15"},
                {"source_key": ARMY, "support_type": "context_only", "locator_override": "Army-entry date 1943-03-11; occupation code 071; protected identifier withheld"},
                {"source_key": CODES, "support_type": "context_only", "locator_override": "PDF physical page 171; category 0-71"},
            ],
        },
    ]

    for row in (2, 3):
        claims.append(
            {
                "key": f"candidate-{slug(PEOPLE[row][1])}-row{row}-starrett-b909",
                "person_id": PEOPLE[row][0],
                "claim_type": "identity",
                "claim_text": "Deane W. Starrett, later a CIA training-research chief, is a candidate spanning two adjacent index spellings rather than a resolved identity.",
                "evidence_paraphrase": "An NPS study cites a 1949 CIA memorandum by Deane W. Starrett, but the two index rows divide the given-name and surname spellings and provide different record details.",
                "identity_match_assessment": "Ambiguous; neither name agreement nor adjacency can establish which row, if either, represents the memo author.",
                "temporal_assessment": "The citation is postwar and does not identify a pre-OSS employer.",
                "source_quality": "B_authoritative_institutional",
                "claim_confidence": "low",
                "publication_status": "needs_review",
                "match_notes": "Private candidate only; both printed rows remain separate pending joint personnel-file review.",
                "sources": [
                    {"source_key": INDEX, "locator_override": f"PDF page 445 row {row}; Box 740"},
                    {"source_key": NPS_STARRETT, "locator_override": "Citation to Deane W. Starrett memorandum, 16 May 1949"},
                ],
            }
        )
    for row in (17, 18):
        claims.append(
            {
                "key": f"candidate-robert-staub-row{row}-varsity-b909",
                "person_id": PEOPLE[row][0],
                "claim_type": "identity",
                "claim_text": "An OSS operative Robert Staub in Operation Varsity is a candidate for one of two adjacent index rows, not a resolved assignment.",
                "evidence_paraphrase": "An official Army history names Robert Staub but supplies no rank, middle name or identifier distinguishing the enlisted and lieutenant rows.",
                "identity_match_assessment": "Ambiguous across two separately preserved source records with different protected identifiers.",
                "temporal_assessment": "The source establishes an OSS wartime role for a namesake but no pre-OSS chronology.",
                "source_quality": "A_direct_official",
                "claim_confidence": "low",
                "publication_status": "needs_review",
                "match_notes": "Private candidate only; no Operation Varsity role is published on either profile until the personnel files distinguish them.",
                "sources": [
                    {"source_key": INDEX, "locator_override": f"PDF page 445 row {row}; protected identifier withheld"},
                    {"source_key": ARMY_STAUB, "locator_override": "Operation Varsity case study naming Robert Staub"},
                ],
            }
        )
    claims.append(
        {
            "key": "candidate-edward-starz-no-initial-b909",
            "person_id": PEOPLE[9][0],
            "claim_type": "identity",
            "claim_text": "The Operation Cardinal radio operator Edward A. Starz is a candidate for the no-initial Edward Starz row, not a resolved identity.",
            "evidence_paraphrase": "The adjacent row has the exact middle initial, rank and protected identifier, so transferring the official biography to this less specific row would risk duplication.",
            "identity_match_assessment": "Ambiguous; adjacency and surname agreement do not establish duplication.",
            "temporal_assessment": "The official source establishes wartime service only.",
            "source_quality": "A_direct_official",
            "claim_confidence": "low",
            "publication_status": "needs_review",
            "match_notes": "Private candidate only; both printed rows remain separate.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 445 rows 9-10; separate printed entries"},
                {"source_key": STARZ_SWJ, "locator_override": "Operation Cardinal team description"},
            ],
        }
    )
    return claims


def army_person_update(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    person_id, _name = PEOPLE[row]
    update: dict[str, object] = {
        "person_id": person_id,
        "identity_status": "high_confidence",
        "identity_evidence": "A nonshared protected identifier and compatible name connect the visually verified index row to the reviewed official Army record. The historical occupation field remains separate from employer and immediate-affiliation claims.",
        "personnel_category": "enlisted_army_personnel",
        "commissioned_officer": False,
        "allied_or_foreign_personnel": False,
        "manual_review_required": True,
        "research_status": "occupation_only_found",
        "next_action": "Review the indexed personnel file to identify the immediate pre-OSS affiliation and last civilian employer; do not convert the Army occupation category into a named employer.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }
    if row == 17:
        update["possible_duplicate_group"] = "same-name:robert-staub-page445"
        update["archival_review_priority"] = "critical"
        update["next_action"] = "Review both Robert Staub personnel files together. Preserve the accepted Army occupation bridge for this enlisted row, but do not assign the unranked Operation Varsity biography to either row without distinguishing evidence."
    return update


def unresolved_update(row: int) -> dict[str, object]:
    person_id, name = PEOPLE[row]
    category, commissioned = RANK_CLASSIFICATION.get(row, ("unknown_or_indeterminate", None))
    update: dict[str, object] = {
        "person_id": person_id,
        "identity_status": "ambiguous" if row in {2, 3, 9, 18} else "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, rank when printed, box and archive location, but staged official-context, CIA Reading Room, exact-name, occupation, employer, obituary, institutional, newspaper, directory, Library of Congress and archival searches found no defensible identity bridge. {UNRESOLVED[row]}",
        "personnel_category": category,
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": "Review the indexed personnel file for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "critical" if row in {2, 3, 4, 9, 18, 19, 20, 21} else "high",
    }
    if commissioned is not None:
        update["commissioned_officer"] = commissioned
        update["allied_or_foreign_personnel"] = False
    if row in {2, 3}:
        update["possible_duplicate_group"] = "name-variant:deane-starret-dean-starrett-page445"
        update["next_action"] = "Review both adjacent Box 740 files together before assigning the Deane W. Starrett CIA biography or merging either source record."
    elif row == 9:
        update["possible_duplicate_group"] = "same-name:edward-starz-page445"
        update["next_action"] = "Review both adjacent Edward Starz files together; do not transfer the Edward A. Starz Operation Cardinal evidence to this no-initial row without a direct bridge."
    elif row == 18:
        update["possible_duplicate_group"] = "same-name:robert-staub-page445"
        update["next_action"] = "Review both Robert Staub personnel files together before assigning the unranked Operation Varsity biography or merging either source record."
    return update


def person_updates() -> list[dict[str, object]]:
    updates = [army_person_update(item) for item in ARMY_OCCUPATIONS]
    updates.extend(unresolved_update(row) for row in UNRESOLVED)
    updates.extend(
        [
            {
                "person_id": PEOPLE[10][0],
                "identity_status": "high_confidence",
                "identity_evidence": "The uncommon exact name, compatible enlisted rank and official person-specific Operation Cardinal radio assignment support a high-confidence match; the adjacent no-initial row remains separate.",
                "personnel_category": "enlisted_army_personnel",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "possible_duplicate_group": "same-name:edward-starz-page445",
                "research_status": "requires_archival_review",
                "next_action": "Review both Edward Starz personnel files together and identify Edward A. Starz's immediate pre-OSS affiliation and last civilian employer.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[14][0],
                "identity_status": "conflicting",
                "identity_evidence": "The distinctive exact name, compatible commissioned ranks, OSS Greece roster and biographical notice support a probable match, but the protected officer number printed in the index differs from the one in War Department General Orders No. 54. The conflict is not silently corrected or exposed.",
                "personnel_category": "commissioned_army_officer",
                "commissioned_officer": True,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "possible_duplicate_group": "identifier-conflict:james-f-stathakos-page445-war-department",
                "research_status": "conflicting_sources",
                "next_action": "Review Box 740 and the original War Department order to resolve the officer-number conflict and identify the immediate pre-OSS military assignment and last civilian employer.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
        ]
    )
    return updates


def research_attempts() -> list[dict[str, object]]:
    sourced_rows = {1, 5, 8, 10, 14, 15, 17, 22, 23}
    candidate_rows = {2, 3, 9, 18}
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        if row in candidate_rows:
            outcome = "candidate_found"
            detail = "A specific candidate source remains private because it cannot distinguish this row from an adjacent name variant or same-name record."
        elif row in sourced_rows:
            outcome = "source_reviewed"
            detail = "Reviewed evidence established an official identity and occupation bridge, a qualified institutional affiliation, or a person-specific wartime identity context."
        else:
            outcome = "candidate_rejected"
            detail = UNRESOLVED[row]
        attempts.append(
            {
                "key": f"page445-row{row}-{slug(name)}-b909",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA/index and public Catalog context; CIA Reading Room exact-name check; OSS and rank variants; employer and occupation; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Box {'739' if row == 1 else ('752' if row == 7 else '740')}; protected-identifier Army crosswalk where available",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_909",
                "started_at": "2026-10-25T21:00:00Z",
                "completed_at": "2026-10-25T23:40:00Z",
                "outcome": outcome,
                "sources_reviewed": 11 if row in {10, 14, 15} else (8 if row in sourced_rows else 6),
                "candidate_sources_rejected": 5 if row in sourced_rows else 7,
                "rejection_reasons": "Unbridged namesakes, discovery-only results, chronologically irrelevant records, postwar-only employment and adjacent-row ambiguity were not assigned." if row in sourced_rows else UNRESOLVED.get(row, detail),
                "research_notes": f"{detail} The LoC and CIA adapters failed closed on transport errors and were preserved as errors rather than negative results; equivalent public-source checks were completed manually. Search-result snippets were discovery aids only, no access control was bypassed, and no exposed NARA API credential was used.",
                "next_action": "Review the indexed personnel file for corroborating identifiers and the last documented pre-OSS affiliation.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b909-v1",
            }
        )
    return attempts


def main() -> None:
    affiliations = [army_affiliation(item) for item in ARMY_OCCUPATIONS]
    affiliations.extend(additional_affiliations())
    claims: list[dict[str, object]] = []
    for item in ARMY_OCCUPATIONS:
        claims.extend(army_claims(item))
    claims.extend(substantive_claims())
    bundle = {
        "bundle_version": "batch-909-v1",
        "reviewer": "Before OSS Batch 909 evidence review",
        "sources": sources(),
        "organizations": organizations(),
        "affiliations": affiliations,
        "claims": claims,
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }
    OUTPUT.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
