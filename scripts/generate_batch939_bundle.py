#!/usr/bin/env python3
"""Generate the reviewed Batch 939 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / (
    "research/evidence-page460-will-s-talbot-to-yasuo-tanaka-"
    "review_batch-939_2026-10-28.json"
)

INDEX = "nara-index-b939"
DENVER = "denver-10th-mountain-b939"
CIA_HALE = "cia-camp-hale-b939"
ASCSA_HISTORY = "ascsa-history-b939"
ASCSA_PROFILE = "ascsa-lucy-talcott-b939"
PENN = "penn-gazette-lucy-talcott-b939"
TALEVI = "all-otsego-bruno-talevi-b939"
GUARDIAN = "guardian-spies-talmadge-b939"
IOWA = "iowa-talmadge-brothers-b939"
TAMARGO = "eldiario-jack-tamargo-b939"
OSS_TRAVEL = "oss-travel-orders-b939"
SMITHSONIAN = "smithsonian-chuzo-tamotzu-b939"
PRIDI = "pridi-bunliang-tamthai-b939"

PEOPLE = {
    1: ("29a23254-9b59-561f-9400-5cbe0bca2311", "Will S Talbot", "764"),
    2: ("af44fc9e-1e5a-552c-86af-5fc9575bf2cf", "William F Talbot", "764"),
    3: ("aeb197ac-2b0e-564a-9544-4df1d1bffed9", "Lucy Talcott", "764"),
    4: ("92cd223b-91a3-5797-acc1-f644a5f3ec4b", "Bruno A Talevi", "764"),
    5: ("c4df08e3-22a7-554d-9f32-7504b16e9f21", "Edward H Taliaferro", "764"),
    6: ("762bb7a8-295a-50db-aed3-697065eec185", "Jaunita L Talkington", "764"),
    7: ("e9ae672d-a6a5-57f1-8e79-6a451f2b6eea", "Bernard W Tallaksen", "764"),
    8: ("c06a1cb0-fca1-5268-ad2a-19acb1c103fe", "Vangie Tallent", "764"),
    9: ("6c509447-7d74-5d6f-8b5f-0567d7927226", "David Talley", "764"),
    10: ("988d1d54-de83-5e95-a882-e5d474a0c9b9", "Bob Talmadge", "764"),
    11: ("d9674002-4998-5c5e-a4cf-b19e59311b83", "James Talmadge", "764"),
    12: ("bdedb53a-ba1e-5716-900e-5618287b8cfb", "Jack Tamargo", "764"),
    13: ("75eb871d-5eb6-59f4-bfeb-ff27594b9fba", "George L Tambakos", "764"),
    14: ("559e5784-b401-5c6b-bee4-62c912bb44a9", "Noboru Tamimoto", "764"),
    15: ("17baa547-fbe8-5ee4-9a4c-590fbebad012", "Ernest D Tamminga", "764"),
    16: ("d9828313-3399-5ffb-8706-05564b29b5c7", "Chuzo Tamotsu", "764"),
    17: ("4adbd14d-83c6-59c5-bcd5-230cef23fb48", "Bunliang Tamthai", "764"),
    18: ("f4d36700-40f6-5e16-88a8-69ce8b2b3933", "Takeo Tanabe", "764"),
    19: ("ac4881e6-6585-5ef0-a1e5-dbfc6cd6f637", "Hajime W Tanaka", "765"),
    20: ("eea3292c-810c-5802-9e90-2c1c41cda07e", "Linda Y Tanaka", "765"),
    21: ("f147656a-bf77-5fb4-8acd-5e886754c7c1", "Paul H Tanaka", "765"),
    22: ("ceb349c5-6fcd-5943-9511-ca3811bbe6ea", "Sugumu Tanaka", "765"),
    23: ("6f02d6b8-2686-5a95-a1bc-27b82c27862b", "Yasuo Tanaka", "765"),
}

UNRESOLVED = {
    1: "Exact-name OSS, Army, employment, obituary and archival searches supplied no defensible Box 764 identity bridge.",
    2: "Common-name OSS, military, employment, obituary and archival searches supplied no defensible Box 764 identity bridge.",
    5: "Exact-name searches and the private protected identifier supplied no accessible source establishing the indexed person's identity or pre-OSS work.",
    6: "Searches of the printed Jaunita spelling and the Juanita variant supplied no OSS or Box 764 identity bridge.",
    8: "A Mary Vangie Tallent namesake obituary lacks an OSS bridge and was rejected rather than assigned.",
    9: "Common-name military, employment, obituary and archival searches supplied no defensible Box 764 identity bridge.",
    13: "Family-tree and modern-directory leads supplied no authoritative OSS or protected-identifier bridge.",
    15: "An Ernest Dorsey Tamminga genealogy lead supplied no authoritative OSS bridge and was rejected.",
    18: "A Military Intelligence registry and other wartime leads did not match the exact name and protected identifier and were not assigned.",
    19: "Common-name OSS, military, institutional and obituary searches supplied no defensible Box 765 identity bridge.",
    20: "Exact-name and variant searches supplied only modern or unbridged namesakes.",
    21: "Common-name OSS, military, institutional and obituary searches supplied no defensible Box 765 identity bridge.",
    22: "Exact-name and transliteration searches supplied no source connecting the indexed row to a pre-OSS affiliation.",
    23: "A same-name MIS Language School registry entry lacks the index row's corroborating identifiers and remains an unassigned candidate.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 764-765",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 460, rows 1-23; checked against layout-preserving text and a high-resolution page render",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. Full protected identifiers remain private. Row 24 was checked as the next boundary.",
        },
        {
            "key": DENVER,
            "stable_url": "https://history.denverlibrary.org/sites/history/files/10th_mountain_index_0.pdf",
            "title": "Members of the 10th Mountain Division",
            "author_creator": "Denver Public Library Western History and Genealogy Department",
            "repository_publisher": "Denver Public Library",
            "locator": "PDF physical page 898; Bernard W Tallaksen, Headquarters, 99th Infantry",
            "access_date": "2026-10-28",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "10th Mountain Division Resource Center name index",
            "rights_notes": "The exact roster line was rendered and visually inspected.",
        },
        {
            "key": CIA_HALE,
            "stable_url": "https://www.cia.gov/stories/story/spy-sites-camp-hale/",
            "title": "Spy Sites: Skis, Spies, and America's Newest National Monument Camp Hale",
            "author_creator": "Central Intelligence Agency",
            "repository_publisher": "Central Intelligence Agency",
            "publication_record_date": "2023-03-20",
            "locator": "Spies on Skis section; recruitment and transfer of 99th Infantry Battalion volunteers",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "CIA history stories",
            "rights_notes": "Used for unit-level recruitment context, not as a person-specific roster.",
        },
        {
            "key": ASCSA_HISTORY,
            "stable_url": "https://www.ascsa.edu.gr/uploads/media/ASCSA_HISTORY_MERITT_1939_1980_reduced.pdf",
            "title": "A History of the American School of Classical Studies at Athens, 1939-1980",
            "author_creator": "Lucy Shoe Meritt",
            "repository_publisher": "American School of Classical Studies at Athens",
            "publication_record_date": "1984",
            "locator": "PDF physical page 96, printed page 176; Lucy Talcott among six prewar Agora staff authorized to resume in 1946",
            "access_date": "2026-10-28",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "American School institutional history",
            "rights_notes": "The relevant page was rendered and visually inspected.",
        },
        {
            "key": ASCSA_PROFILE,
            "stable_url": "https://www.ascsa.edu.gr/news/newsDetails/lucy-talcott-honored-with-room-in-loring-hall",
            "title": "Lucy Talcott Honored With Room in Loring Hall",
            "author_creator": "American School of Classical Studies at Athens",
            "repository_publisher": "American School of Classical Studies at Athens",
            "publication_record_date": "2024-02-22",
            "locator": "Institutional biography; Secretary of the Agora Excavations, 1931-1958",
            "access_date": "2026-10-28",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "American School news",
            "rights_notes": "Used for employment title and dates.",
        },
        {
            "key": PENN,
            "stable_url": "https://thepenngazette.com/trowel-cloak-and-dagger/",
            "title": "Trowel, Cloak and Dagger",
            "author_creator": "Melissa Jacobs",
            "repository_publisher": "The Pennsylvania Gazette, University of Pennsylvania",
            "publication_record_date": "2012-11-01",
            "locator": "Article discussion of Rodney Young's OSS Greek Desk and named archaeological assistants",
            "access_date": "2026-10-28",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Pennsylvania Gazette",
            "rights_notes": "The article is based on NARA-declassified records and Susan Heuck Allen's scholarly history; only a project-authored paraphrase is retained.",
        },
        {
            "key": TALEVI,
            "stable_url": "https://www.allotsego.com/bruno-a-talevi-96-wwii-veteran-accountant-civic-leader-in-oneonta-cooperstown/",
            "title": "Bruno A. Talevi, 96; WWII Veteran, Accountant, Civic Leader In Oneonta, Cooperstown",
            "repository_publisher": "The Freeman's Journal and Hometown Oneonta / All Otsego",
            "publication_record_date": "2021-04-08",
            "locator": "Obituary paragraphs 2-4; birth, Benjamin Franklin High School, OSS and Navy sequence",
            "access_date": "2026-10-28",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "In Memoriam",
            "rights_notes": "The direct chronology is retained as a short paraphrase; postwar career details are excluded from the claim.",
        },
        {
            "key": GUARDIAN,
            "stable_url": "https://www.guardianspies.com/research.html",
            "title": "Guardian Spies: The Story of the U.S. Coast Guard and OSS in World War II - About the Research",
            "author_creator": "MEB, Inc.",
            "repository_publisher": "Guardian Spies",
            "locator": "Operational Swimmer Group III roster; James and Robert Talmadge, USCGR",
            "access_date": "2026-10-28",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Coast Guard and OSS Maritime Unit research",
            "rights_notes": "The project describes its use of declassified OSS and Coast Guard personnel files and rosters. The roster was checked directly.",
        },
        {
            "key": IOWA,
            "stable_url": "https://aspace.lib.uiowa.edu/repositories/2/archival_objects/1064492",
            "archival_identifier": "MsC0512, Box 3",
            "title": "James 'Jimmy' and Robert 'Bobby' Talmadge",
            "author_creator": "Marion Meade",
            "repository_publisher": "University of Iowa Special Collections",
            "publication_record_date": "Collection dates 1895-1997",
            "locator": "Marion Meade Buster Keaton Research Files, file-level description",
            "access_date": "2026-10-28",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Marion Meade Buster Keaton Research Files",
            "rights_notes": "Used only to establish the James/Jimmy and Robert/Bobby name variants as a paired family record.",
        },
        {
            "key": TAMARGO,
            "stable_url": "https://www.eldiario.es/euskadi/blogs/fighting-basques-ecos-de-dos-guerras-1936-1945/espanoles-hitler-servicio-ejercito-estados-unidos_132_6216218.html",
            "title": "Españoles contra Hitler. Al servicio del Ejército de Estados Unidos",
            "author_creator": "Asociación Sancho de Beurko",
            "repository_publisher": "elDiario.es",
            "publication_record_date": "2020-09-11",
            "locator": "Caption for Joaquín 'Jack' Tamargo Montoto; Army enlistment, Algeria and OSS counterintelligence sequence",
            "access_date": "2026-10-28",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Fighting Basques: Ecos de dos guerras 1936-1945",
            "rights_notes": "The association describes its NARA-based military-history research; only a concise paraphrase is retained.",
        },
        {
            "key": OSS_TRAVEL,
            "stable_url": "https://www.historyofjapaneseinny.org/wp-content/uploads/2024/05/OFFICE-OF-STRATEGIC-SERVICES-1.pdf",
            "archival_identifier": "OSS Headquarters corrected Invitational Travel Orders, shipment IJ-B857-HY",
            "title": "Invitational Travel Orders, Shipment IJ-B857-HY",
            "author_creator": "Office of Strategic Services",
            "repository_publisher": "History of Japanese in New York",
            "publication_record_date": "1945-04-30",
            "locator": "PDF physical page 11; Chuzo Tamotzu among named civilian OSS employees",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "Office of Strategic Services records",
            "rights_notes": "The scanned order page was rendered at high resolution and visually inspected.",
        },
        {
            "key": SMITHSONIAN,
            "stable_url": "https://www.aaa.si.edu/collections/interviews/oral-history-interview-chuzo-tamotzu-11756",
            "archival_identifier": "AAA_collcode_tamots64; DSI-AAA_CollID 11756",
            "title": "Oral history interview with Chuzo Tamotzu, 1964 September 3",
            "author_creator": "Sylvia Glidden Loomis, interviewer; Chuzo Tamotzu, interviewee",
            "repository_publisher": "Archives of American Art, Smithsonian Institution",
            "publication_record_date": "1964-09-03",
            "locator": "Interview overview and transcript; Federal Art Project and WPA discussion",
            "access_date": "2026-10-28",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "New Deal and the Arts Oral History Project",
            "rights_notes": "The Smithsonian record documents Tamotzu/Tamotsu variants and his Federal Art Project work. Only project-authored paraphrases are retained.",
        },
        {
            "key": PRIDI,
            "stable_url": "https://pridi.or.th/th/content/2022/08/1210",
            "title": "ขบวนการเสรีไทย : พันธกิจที่ใหญ่ยิ่ง (The Free Thai Movement: A Great Mission)",
            "author_creator": "Pusadee Tamthai",
            "repository_publisher": "Pridi Banomyong Institute",
            "publication_record_date": "2022-08",
            "locator": "Family-authored institutional account; Bunliang Tamthai joined the first U.S. Free Thai volunteers while a scholarship student",
            "access_date": "2026-10-28",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Pridi Banomyong Institute historical articles",
            "rights_notes": "The account identifies the family relationship and training chronology. The unnamed school is not invented.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": "army-existing-b939",
            "organization_id": "28a26f92-78af-5a1a-9c09-a843eb5975b4",
            "canonical_name": "United States Army",
            "historical_name": "Army of the United States",
            "aliases": ["U.S. Army"],
            "organization_type": "military service",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "Existing canonical organization reused.",
        },
        {
            "key": "army-99th-existing-b939",
            "organization_id": "a520c0e7-81d8-5aea-90d7-ddb0b2ce5eff",
            "canonical_name": "United States Army, 99th Infantry Battalion (Separate)",
            "historical_name": "99th Infantry Battalion (Separate)",
            "aliases": ["99th Infantry", "Viking Battalion"],
            "organization_type": "U.S. Army infantry battalion",
            "sector": "military",
            "country": "United States",
            "active_dates": "1942-1945",
            "normalization_notes": "Existing canonical organization reused; the roster abbreviation HQ 99TH INF is preserved in evidence.",
        },
        {
            "key": "coast-guard-existing-b939",
            "organization_id": "37a8f326-bc36-5bb7-9c9c-078500d96f92",
            "canonical_name": "United States Coast Guard",
            "historical_name": "United States Coast Guard Reserve",
            "aliases": ["USCGR", "U.S. Coast Guard"],
            "organization_type": "military and maritime service",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "Existing canonical organization reused.",
        },
        {
            "key": "ascsa-existing-b939",
            "organization_id": "29abce5d-fe96-5ed8-beb4-93560d4604cb",
            "canonical_name": "American School of Classical Studies at Athens",
            "historical_name": "American School of Classical Studies at Athens",
            "aliases": ["American School", "ASCSA", "Athenian Agora Excavations"],
            "organization_type": "research institution",
            "sector": "academia_and_research",
            "city": "Athens",
            "country": "Greece",
            "normalization_notes": "Existing canonical organization reused; the Agora Excavations unit remains explicit in the role and source wording.",
        },
        {
            "key": "benjamin-franklin-high-b939",
            "canonical_name": "Benjamin Franklin High School",
            "historical_name": "Benjamin Franklin High School",
            "aliases": [],
            "organization_type": "public high school",
            "sector": "student",
            "city": "New York City",
            "state_or_region": "New York",
            "country": "United States",
            "normalization_notes": "Modeled only as student status, not as an employer.",
        },
        {
            "key": "federal-art-project-b939",
            "canonical_name": "Federal Art Project",
            "historical_name": "Federal Art Project of the Works Progress Administration",
            "aliases": ["WPA Federal Art Project", "Federal Art Project division of the WPA"],
            "organization_type": "federal arts employment program",
            "sector": "federal_government",
            "country": "United States",
            "active_dates": "1935-1943",
            "normalization_notes": "Historical program name preserved. No modern successor is substituted.",
        },
    ]


def affiliations() -> list[dict[str, object]]:
    return [
        {
            "key": "lucy-talcott-ascsa-b939", "person_id": PEOPLE[3][0],
            "organization_key": "ascsa-existing-b939", "organization_name_as_found": "Agora Excavations",
            "role_title": "Secretary of the Agora Excavations", "occupation": "archaeologist and records administrator",
            "relationship_type": "employment", "start_date": "1931", "end_date": "1942",
            "date_precision": "Institutional tenure ran 1931-1958 with a wartime interruption; the exact OSS transition date is not stated",
            "city": "Athens", "country": "Greece", "immediate_pre_oss": False,
            "last_civilian_pre_service": True, "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "high_confidence", "claim_confidence": "medium",
            "source_quality": "B_authoritative_institutional", "publication_status": "publish_qualified",
            "research_notes": "The institutional history identifies her as prewar staff, and the Penn account independently places her with the OSS Greek Desk. The exact recruitment date remains unproved.",
        },
        {
            "key": "bruno-talevi-benjamin-franklin-b939", "person_id": PEOPLE[4][0],
            "organization_key": "benjamin-franklin-high-b939", "organization_name_as_found": "Benjamin Franklin High School",
            "role_title": "Student", "occupation": "student", "relationship_type": "student",
            "end_date": "1941-1942", "date_precision": "Graduated at age 16 and then worked for OSS; exact graduation date is not stated",
            "city": "New York City", "state_or_region": "New York", "country": "United States",
            "immediate_pre_oss": True, "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "explicit_immediate", "identity_confidence": "high_confidence",
            "claim_confidence": "high", "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "published", "research_notes": "Student status immediately preceded OSS work; the school is not labeled an employer.",
        },
        {
            "key": "bernard-tallaksen-99th-b939", "person_id": PEOPLE[7][0],
            "organization_key": "army-99th-existing-b939", "organization_name_as_found": "HQ, 99TH INF",
            "role_title": "Headquarters soldier", "occupation": "soldier", "relationship_type": "military_assignment",
            "end_date": "1943", "date_precision": "Roster identifies Headquarters, 99th Infantry; CIA dates unit recruitment to summer 1943",
            "country": "United States", "immediate_pre_oss": True, "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "strongly_date_bounded", "identity_confidence": "high_confidence",
            "claim_confidence": "high", "source_quality": "B_authoritative_institutional",
            "publication_status": "published", "research_notes": "The exact roster name and index row align; the CIA source supplies unit-level recruitment context. No civilian employer is inferred.",
        },
        {
            "key": "bob-talmadge-coast-guard-b939", "person_id": PEOPLE[10][0],
            "organization_key": "coast-guard-existing-b939", "organization_name_as_found": "Robert Talmadge, USCGR",
            "role_title": "Motor Machinist's Mate Second Class; Operational Swimmer Group III", "occupation": "Coast Guardsman",
            "relationship_type": "military_assignment", "end_date": "1944-10",
            "date_precision": "Roster places the group in OSS Detachment 101 from October 1944 to January 1945",
            "country": "United States", "immediate_pre_oss": True, "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "explicit_immediate", "identity_confidence": "high_confidence",
            "claim_confidence": "high", "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "published", "research_notes": "The adjacent Bob and James index rows align with the paired Robert/Bobby and James/Jimmy archival file and the OSS roster. No civilian employer is inferred.",
        },
        {
            "key": "james-talmadge-coast-guard-b939", "person_id": PEOPLE[11][0],
            "organization_key": "coast-guard-existing-b939", "organization_name_as_found": "James Talmadge, USCGR",
            "role_title": "Boatswain's Mate Second Class; Operational Swimmer Group III", "occupation": "Coast Guardsman",
            "relationship_type": "military_assignment", "end_date": "1944-10",
            "date_precision": "Roster places the group in OSS Detachment 101 from October 1944 to January 1945",
            "country": "United States", "immediate_pre_oss": True, "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "explicit_immediate", "identity_confidence": "high_confidence",
            "claim_confidence": "high", "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "published", "research_notes": "The adjacent Bob and James index rows align with the paired Robert/Bobby and James/Jimmy archival file and the OSS roster. No civilian employer is inferred.",
        },
        {
            "key": "jack-tamargo-army-b939", "person_id": PEOPLE[12][0],
            "organization_key": "army-existing-b939", "organization_name_as_found": "U.S. Army",
            "role_title": "Soldier assigned to Canastel, Algeria", "occupation": "soldier",
            "relationship_type": "military_assignment", "start_date": "1942", "end_date": "1943-1945",
            "date_precision": "Drafted in 1942; in Algeria by 1943; later joined OSS counterintelligence, exact transfer date not stated",
            "city": "Canastel", "country": "Algeria", "immediate_pre_oss": True,
            "last_civilian_pre_service": False, "pre_oss_temporal_basis": "explicit_immediate",
            "identity_confidence": "high_confidence", "claim_confidence": "medium",
            "source_quality": "C_reputable_contemporary_or_scholarly", "publication_status": "publish_qualified",
            "research_notes": "Modeled as an Army-to-OSS pathway. The source does not identify a civilian employer before Army service.",
        },
        {
            "key": "chuzo-tamotsu-federal-art-b939", "person_id": PEOPLE[16][0],
            "organization_key": "federal-art-project-b939", "organization_name_as_found": "Federal Art Project",
            "role_title": "Easel and graphic artist", "occupation": "painter and printmaker",
            "relationship_type": "employment", "start_date": "1935", "end_date": "1937",
            "date_precision": "Institutional sources date Federal Art Project work to 1935-1937; later Army and OSS chronology is not fully dated",
            "city": "New York City", "state_or_region": "New York", "country": "United States",
            "immediate_pre_oss": False, "last_civilian_pre_service": True,
            "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "high_confidence",
            "claim_confidence": "medium", "source_quality": "B_authoritative_institutional",
            "publication_status": "publish_qualified", "research_notes": "This is the last named civilian employer found before wartime service, not proof that no intervening independent art work occurred.",
        },
        {
            "key": "bunliang-tamthai-student-b939", "person_id": PEOPLE[17][0],
            "role_title": "Scholarship student in the United States", "occupation": "student",
            "relationship_type": "student", "end_date": "1942-06",
            "date_precision": "The account says he joined the first U.S. Free Thai volunteers while studying on scholarship; the institution is not named",
            "country": "United States", "immediate_pre_oss": True, "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "explicit_immediate", "identity_confidence": "high_confidence",
            "claim_confidence": "high", "source_quality": "B_authoritative_institutional",
            "publication_status": "published", "research_notes": "Student status is not employment. The unnamed institution is intentionally not inferred.",
        },
    ]


def claim(
    row: int,
    key: str,
    claim_type: str,
    text: str,
    paraphrase: str,
    assessment: str,
    temporal: str,
    quality: str,
    confidence: str,
    source_keys: list[dict[str, object]],
    notes: str,
    affiliation_key: str | None = None,
    publication_status: str | None = None,
) -> dict[str, object]:
    result: dict[str, object] = {
        "key": key,
        "person_id": PEOPLE[row][0],
        "claim_type": claim_type,
        "claim_text": text,
        "evidence_paraphrase": paraphrase,
        "identity_match_assessment": assessment,
        "temporal_assessment": temporal,
        "source_quality": quality,
        "claim_confidence": confidence,
        "publication_status": publication_status or ("published" if confidence in {"confirmed", "high"} else "publish_qualified"),
        "match_notes": notes,
        "sources": source_keys,
    }
    if affiliation_key:
        result["affiliation_key"] = affiliation_key
    return result


def claims() -> list[dict[str, object]]:
    result = [
        claim(3, "identity-lucy-talcott-b939", "identity", "Indexed Lucy Talcott is a high-confidence match to the American School archaeologist who assisted the OSS Greek Desk.", "The rare exact name, continuous Agora career and named Greek Desk role align.", "High confidence from the rare exact name and two independent institutional sources; the Box 764 file remains unreviewed.", "The sources place the Agora career before and after the war and the OSS role by 1942.", "B_authoritative_institutional", "high", [{"source_key": INDEX, "locator_override": "PDF page 460 row 3; Box 764"}, {"source_key": ASCSA_PROFILE}, {"source_key": PENN}], "The employer and OSS role are independently documented; exact recruitment chronology still requires the personnel file."),
        claim(3, "last-civilian-lucy-talcott-ascsa-b939", "last_civilian_pre_service", "Lucy Talcott served as Secretary of the Athenian Agora Excavations before her wartime OSS Greek Desk work.", "American School records identify her as prewar Agora staff and secretary; the Penn account names her among the Greek Desk assistants.", "High-confidence identity from the rare exact name and aligned archaeological role.", "Strongly date-bounded, but the exact date she left or paused Agora work for OSS is not stated.", "B_authoritative_institutional", "medium", [{"source_key": ASCSA_HISTORY, "locator_override": "PDF physical page 96, printed page 176"}, {"source_key": ASCSA_PROFILE}, {"source_key": PENN}], "Published as the last documented civilian employer, not as an explicitly immediate recruitment source.", "lucy-talcott-ascsa-b939"),
        claim(4, "identity-bruno-talevi-b939", "identity", "Indexed Bruno A. Talevi is a high-confidence match to the New York-born OSS civilian and later Navy veteran.", "The exact full name, age-compatible chronology and explicit OSS service align with the index.", "High confidence from the unusual exact name and direct life chronology; no protected identifier is published.", "The obituary places OSS work after high school and before Navy service at age 18.", "C_reputable_contemporary_or_scholarly", "high", [{"source_key": INDEX, "locator_override": "PDF page 460 row 4; Box 764"}, {"source_key": TALEVI}], "The source distinguishes his civilian OSS work from later Navy service."),
        claim(4, "immediate-bruno-talevi-student-b939", "immediate_pre_oss_affiliation", "Bruno A. Talevi was a Benjamin Franklin High School student immediately before his OSS employment.", "His obituary directly sequences graduation at age 16 and OSS work.", "High-confidence identity from the exact full name and compatible wartime chronology.", "Explicitly immediate; the school is student status, not employment.", "C_reputable_contemporary_or_scholarly", "high", [{"source_key": TALEVI, "locator_override": "Obituary paragraphs 2-4"}], "No civilian employer before OSS is named, and none is invented.", "bruno-talevi-benjamin-franklin-b939"),
        claim(7, "identity-bernard-tallaksen-b939", "identity", "Indexed Bernard W. Tallaksen is a high-confidence match to the Headquarters soldier listed with the 99th Infantry Battalion.", "The exact full name and middle initial align between the OSS index and Denver Public Library roster.", "High confidence from the rare exact name, initial, military roster and known unit-level OSS recruitment.", "The roster and CIA history place the unit at Camp Hale before its 1943 OSS transfers.", "B_authoritative_institutional", "high", [{"source_key": INDEX, "locator_override": "PDF page 460 row 7; Box 764"}, {"source_key": DENVER, "locator_override": "PDF physical page 898"}, {"source_key": CIA_HALE}], "The exact roster line was visually inspected."),
        claim(7, "immediate-bernard-tallaksen-99th-b939", "immediate_pre_oss_affiliation", "Bernard W. Tallaksen served in Headquarters, 99th Infantry Battalion, immediately before the unit's OSS Norwegian Operational Group pathway.", "The roster names him in the 99th; CIA documents the OSS recruitment and transfer of 99th Battalion volunteers.", "High-confidence identity from the exact name and middle initial in the unit roster.", "Strongly date-bounded at unit level; the individual transfer order is not accessible.", "B_authoritative_institutional", "high", [{"source_key": DENVER, "locator_override": "PDF physical page 898; HQ, 99TH INF"}, {"source_key": CIA_HALE, "locator_override": "Spies on Skis section"}], "Modeled as a military assignment, not a civilian employer.", "bernard-tallaksen-99th-b939"),
        claim(10, "identity-bob-talmadge-b939", "identity", "Indexed Bob Talmadge is a high-confidence match to Robert 'Bobby' Talmadge of the Coast Guard OSS Operational Swimmer Group III.", "The adjacent Bob and James rows align with an institutional paired-sibling file and the paired OSS roster entries.", "High confidence from the unusual adjacent pair, Bobby/Robert variant and person-specific Coast Guard OSS roster.", "The roster places Robert in OSS Detachment 101 during 1944-1945.", "C_reputable_contemporary_or_scholarly", "high", [{"source_key": INDEX, "locator_override": "PDF page 460 rows 10-11; Box 764"}, {"source_key": IOWA}, {"source_key": GUARDIAN, "locator_override": "Operational Swimmer Group III roster"}], "Bob is preserved as indexed; Robert and Bobby are documented variants."),
        claim(10, "immediate-bob-talmadge-coast-guard-b939", "immediate_pre_oss_affiliation", "Robert 'Bob' Talmadge entered the OSS Maritime Unit through the United States Coast Guard Reserve.", "The roster names Robert Talmadge, USCGR, in OSS Operational Swimmer Group III.", "High-confidence paired identity; the Box 764 file remains the final direct bridge.", "Explicit Coast Guard attachment to an OSS group deployed October 1944-January 1945.", "C_reputable_contemporary_or_scholarly", "high", [{"source_key": GUARDIAN, "locator_override": "Operational Swimmer Group III roster"}, {"source_key": IOWA, "support_type": "context_only"}], "Modeled as a military assignment, not a civilian employer.", "bob-talmadge-coast-guard-b939"),
        claim(11, "identity-james-talmadge-b939", "identity", "Indexed James Talmadge is a high-confidence match to James 'Jimmy' Talmadge of the Coast Guard OSS Operational Swimmer Group III.", "The adjacent James and Bob rows align with an institutional paired-sibling file and the paired OSS roster entries.", "High confidence from the unusual adjacent pair, Jimmy/James variant and person-specific Coast Guard OSS roster.", "The roster places James in OSS Detachment 101 during 1944-1945.", "C_reputable_contemporary_or_scholarly", "high", [{"source_key": INDEX, "locator_override": "PDF page 460 rows 10-11; Box 764"}, {"source_key": IOWA}, {"source_key": GUARDIAN, "locator_override": "Operational Swimmer Group III roster"}], "James is preserved as indexed; Jimmy is a documented variant."),
        claim(11, "immediate-james-talmadge-coast-guard-b939", "immediate_pre_oss_affiliation", "James 'Jimmy' Talmadge entered the OSS Maritime Unit through the United States Coast Guard Reserve.", "The roster names James Talmadge, USCGR, in OSS Operational Swimmer Group III.", "High-confidence paired identity; the Box 764 file remains the final direct bridge.", "Explicit Coast Guard attachment to an OSS group deployed October 1944-January 1945.", "C_reputable_contemporary_or_scholarly", "high", [{"source_key": GUARDIAN, "locator_override": "Operational Swimmer Group III roster"}, {"source_key": IOWA, "support_type": "context_only"}], "Modeled as a military assignment, not a civilian employer.", "james-talmadge-coast-guard-b939"),
        claim(12, "identity-jack-tamargo-b939", "identity", "Indexed Jack Tamargo is a high-confidence match to Joaquín 'Jack' Tamargo Montoto, the Spanish-born Army and OSS counterintelligence veteran.", "The distinctive name, Jack variant, Army chronology and explicit OSS service align.", "High confidence from the unusual exact name and compatible NARA-based military chronology.", "The source dates Army entry to 1942 and OSS counterintelligence service after assignment in Algeria.", "C_reputable_contemporary_or_scholarly", "high", [{"source_key": INDEX, "locator_override": "PDF page 460 row 12; Box 764"}, {"source_key": TAMARGO}], "The full Spanish name is retained as a documented variant."),
        claim(12, "immediate-jack-tamargo-army-b939", "immediate_pre_oss_affiliation", "Joaquín 'Jack' Tamargo Montoto moved from a U.S. Army assignment in Algeria into OSS counterintelligence.", "The NARA-based military-history article directly sequences 1942 Army recruitment, Algeria and OSS counterintelligence.", "High-confidence identity from the rare name and aligned Army/OSS history.", "Explicit sequence, but the exact OSS transfer date is not stated.", "C_reputable_contemporary_or_scholarly", "medium", [{"source_key": TAMARGO, "locator_override": "Tamargo photograph caption and research note"}], "Published as a qualified military pathway; no civilian employer is identified.", "jack-tamargo-army-b939"),
        claim(14, "conflict-noboru-tamimoto-tanimoto-b939", "identity", "Indexed Noboru Tamimoto may be a spelling-variant duplicate of separately indexed Noboru M. Tanimoto, but the rows remain unmerged.", "Page 460 contains both rows, while a direct OSS order names Noboru Mori Tanimoto.", "Ambiguous: the near-identical names and middle-name expansion suggest duplication, but no source assigns the travel order to row 14.", "Both index rows and the 1945 order are wartime records; their exact relationship is unresolved.", "A_direct_official", "conflicting", [{"source_key": INDEX, "locator_override": "PDF page 460 rows 14 and 32"}, {"source_key": OSS_TRAVEL, "locator_override": "PDF physical page 11; Noboru Mori Tanimoto"}], "The rows are intentionally kept separate pending Box 764-765 review.", publication_status="conflicting"),
        claim(16, "identity-chuzo-tamotsu-b939", "identity", "Indexed Chuzo Tamotsu is a high-confidence match to artist Chuzo Tamotzu, named as a civilian OSS employee in April 1945.", "The rare name, Smithsonian Tamotzu/Tamotsu variants and direct OSS order align.", "High confidence from the explicit institutional name variants and direct wartime OSS record.", "The order confirms OSS employment in April 1945; the oral history documents earlier Federal Art Project work.", "A_direct_official", "high", [{"source_key": INDEX, "locator_override": "PDF page 460 row 16; Box 764"}, {"source_key": SMITHSONIAN}, {"source_key": OSS_TRAVEL, "locator_override": "PDF physical page 11"}], "The order page and Smithsonian guide page were visually inspected."),
        claim(16, "last-civilian-chuzo-tamotsu-federal-art-b939", "last_civilian_pre_service", "Chuzo Tamotzu's last identified named civilian employer before wartime service was the Federal Art Project.", "His Smithsonian oral history documents easel and graphic work for the Federal Art Project and WPA before his wartime service.", "High-confidence identity from the distinctive name variants and direct OSS order.", "Documented prewar employment ending about 1937; later independent work or an intervening employer cannot be excluded.", "B_authoritative_institutional", "medium", [{"source_key": SMITHSONIAN, "locator_override": "Interview overview and Federal Art Project transcript section"}], "Qualified as the last identified named civilian employer, not as explicitly immediate.", "chuzo-tamotsu-federal-art-b939"),
        claim(17, "identity-bunliang-tamthai-b939", "identity", "Indexed Bunliang Tamthai is a high-confidence match to the scholarship student who joined the first U.S. Free Thai volunteers trained by OSS.", "The rare exact name and explicit U.S. OSS/Free Thai chronology align with the index.", "High confidence from the distinctive exact name and family-authored institutional account.", "The account dates volunteer training from June 1942 into 1943.", "B_authoritative_institutional", "high", [{"source_key": INDEX, "locator_override": "PDF page 460 row 17; Box 764"}, {"source_key": PRIDI}], "The source names no school, so none is inferred."),
        claim(17, "immediate-bunliang-tamthai-student-b939", "immediate_pre_oss_affiliation", "Bunliang Tamthai was a scholarship student in the United States immediately before joining the first Free Thai volunteers trained by OSS.", "The family-authored institutional account directly states that he joined while studying in the United States on scholarship.", "High-confidence identity from the rare exact name and explicit OSS chronology.", "Explicitly immediate; the institution is unnamed and student status is not employment.", "B_authoritative_institutional", "high", [{"source_key": PRIDI, "locator_override": "Family recollection and volunteer-training discussion"}], "The institution and degree are not invented.", "bunliang-tamthai-student-b939"),
    ]
    return result


def archival_update(row: int, reason: str) -> dict[str, object]:
    person_id, name, box = PEOPLE[row]
    return {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, Box {box} and archive location 230/86/41/07. {reason}",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": f"Review Box {box} for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }


def person_updates() -> list[dict[str, object]]:
    updates = [archival_update(row, reason) for row, reason in UNRESOLVED.items()]
    updates.extend([
        {"person_id": PEOPLE[3][0], "identity_status": "high_confidence", "identity_evidence": "The rare exact name, American School prewar employment and independent Penn account of her OSS Greek Desk role form a coherent identity bridge.", "name_variants": ["Lucy Talcott"], "personnel_category": "civilian_professional_or_administrative_grade", "commissioned_officer": False, "allied_or_foreign_personnel": False, "manual_review_required": True, "research_status": "documented_prewar_employer_found", "next_action": "Review Box 764 for her exact Agora-to-OSS recruitment date and whether the employment relationship formally continued during wartime service.", "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "medium"},
        {"person_id": PEOPLE[4][0], "identity_status": "high_confidence", "identity_evidence": "The exact full name and obituary's age-compatible high-school, OSS and Navy chronology align with the index.", "personnel_category": "civilian_professional_or_administrative_grade", "commissioned_officer": False, "allied_or_foreign_personnel": False, "manual_review_required": True, "research_status": "completed", "next_action": "Review Box 764 for his civilian OSS duties and exact service dates; no pre-OSS civilian employer is named.", "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "medium"},
        {"person_id": PEOPLE[7][0], "identity_status": "high_confidence", "identity_evidence": "The exact name and middle initial match a visually inspected Denver Public Library roster placing him in Headquarters, 99th Infantry Battalion; CIA documents the unit's 1943 OSS recruitment pathway.", "personnel_category": "enlisted_army_personnel", "commissioned_officer": False, "allied_or_foreign_personnel": False, "manual_review_required": True, "research_status": "completed", "next_action": "Review Box 764 for the individual transfer order, OSS operational group and last civilian employer before Army service.", "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "medium"},
        {"person_id": PEOPLE[10][0], "identity_status": "high_confidence", "identity_evidence": "The adjacent Bob and James index rows align with the University of Iowa's paired Robert/Bobby and James/Jimmy file and the paired Coast Guard OSS roster entries.", "name_variants": ["Robert Talmadge", "Robert 'Bobby' Talmadge"], "personnel_category": "enlisted_coast_guard_personnel", "commissioned_officer": False, "allied_or_foreign_personnel": False, "manual_review_required": True, "research_status": "completed", "next_action": "Review Box 764 and the cited Coast Guard personnel file for enlistment date and the last civilian employer before service.", "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "medium"},
        {"person_id": PEOPLE[11][0], "identity_status": "high_confidence", "identity_evidence": "The adjacent James and Bob index rows align with the University of Iowa's paired James/Jimmy and Robert/Bobby file and the paired Coast Guard OSS roster entries.", "name_variants": ["James 'Jimmy' Talmadge"], "personnel_category": "enlisted_coast_guard_personnel", "commissioned_officer": False, "allied_or_foreign_personnel": False, "manual_review_required": True, "research_status": "completed", "next_action": "Review Box 764 and the cited Coast Guard personnel file for enlistment date and the last civilian employer before service.", "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "medium"},
        {"person_id": PEOPLE[12][0], "identity_status": "high_confidence", "identity_evidence": "The distinctive Jack Tamargo name and the NARA-based Spanish military-history project's Army, Algeria and OSS counterintelligence chronology align with the index.", "name_variants": ["Joaquín Tamargo Montoto", "Joaquín 'Jack' Tamargo Montoto"], "personnel_category": "enlisted_army_personnel", "commissioned_officer": False, "allied_or_foreign_personnel": False, "manual_review_required": True, "research_status": "completed", "next_action": "Review Box 764 for the exact Army-to-OSS transfer date, counterintelligence assignment and civilian employment before the 1942 draft.", "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "medium"},
        {"person_id": PEOPLE[14][0], "identity_status": "ambiguous", "identity_evidence": "The visually verified page also contains a separate Noboru M. Tanimoto row, while a direct 1945 OSS order names Noboru Mori Tanimoto. No evidence assigns that order to the Tamimoto row.", "manual_review_required": True, "possible_duplicate_group": "page460-noboru-tamimoto-tanimoto-rows14-32", "research_status": "conflicting_sources", "next_action": "Review the Noboru Tamimoto Box 764 file and Noboru M. Tanimoto Box 765 file together. Keep both source rows separate unless direct evidence proves duplication.", "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "critical"},
        {"person_id": PEOPLE[16][0], "identity_status": "high_confidence", "identity_evidence": "Smithsonian records explicitly preserve the Tamotzu/Tamotsu variants, and a visually inspected 1945 OSS order names Chuzo Tamotzu as a civilian employee.", "name_variants": ["Chuzo Tamotzu", "Chūzō Tamotsu", "Chūzō Tamotzu"], "personnel_category": "civilian_professional_or_administrative_grade", "commissioned_officer": False, "allied_or_foreign_personnel": False, "manual_review_required": True, "research_status": "documented_prewar_employer_found", "next_action": "Review Box 764 for his Army and OSS chronology and any named civilian work between the 1937 Federal Art Project exit and wartime service.", "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "medium"},
        {"person_id": PEOPLE[17][0], "identity_status": "high_confidence", "identity_evidence": "The rare exact name and family-authored Pridi Banomyong Institute account explicitly align a U.S. scholarship student with the first Free Thai volunteers trained by OSS.", "name_variants": ["Professor Dr. Bunliang Tamthai"], "commissioned_officer": False, "allied_or_foreign_personnel": True, "manual_review_required": True, "research_status": "completed", "next_action": "Review Box 764 for the unnamed U.S. institution, degree program, Free Thai training dates and any civilian employer before study.", "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "medium"},
    ])
    return updates


def research_attempts() -> list[dict[str, object]]:
    substantive = {
        3: ("source_reviewed", 11, 4, "Institutional and scholarly sources support a high-confidence identity and a qualified prewar American School employer."),
        4: ("source_reviewed", 8, 3, "A reputable obituary directly sequences Benjamin Franklin High School, civilian OSS work and later Navy service."),
        7: ("source_reviewed", 10, 3, "An institutional roster and official CIA unit history support the high-confidence 99th Infantry-to-OSS pathway."),
        10: ("source_reviewed", 10, 4, "An OSS/Coast Guard roster and University of Iowa paired-name file support the Robert/Bobby Talmadge identity and military pathway."),
        11: ("source_reviewed", 10, 4, "An OSS/Coast Guard roster and University of Iowa paired-name file support the James/Jimmy Talmadge identity and military pathway."),
        12: ("source_reviewed", 9, 4, "A NARA-based Spanish military-history project supports the Army-to-OSS counterintelligence pathway."),
        14: ("candidate_found", 9, 5, "The nearby Noboru M. Tanimoto row and direct OSS order create a visible possible-duplicate conflict; no merge was made."),
        16: ("source_reviewed", 12, 4, "A direct OSS order confirms Chuzo Tamotzu, while Smithsonian sources document the name variants and Federal Art Project work."),
        17: ("source_reviewed", 10, 4, "A family-authored institutional history supports student status immediately before Free Thai/OSS training; the school remains unnamed."),
    }
    attempts = []
    for row in sorted(PEOPLE):
        person_id, name, box = PEOPLE[row]
        if row in UNRESOLVED:
            outcome, reviewed, rejected, detail = "no_result", 7, 4, UNRESOLVED[row]
        else:
            outcome, reviewed, rejected, detail = substantive[row]
        attempts.append({
            "key": f"page460-row{row}-{slug(name)}-b939",
            "person_id": person_id,
            "source_adapter": "manual_staged_protocol",
            "query_text": f"{name}; NARA index and public Archives context; CIA Reading Room and CIA site-restricted exact-name discovery; OSS and spelling variants; employer and occupation 1940; obituary, institutional, newspaper and archival searches; Box {box}; protected identifiers used privately only when defensible",
            "query_variant_type": "staged_identity_employment_archival_protocol_batch_939",
            "started_at": "2026-10-28T03:35:00Z",
            "completed_at": "2026-10-28T05:18:00Z",
            "outcome": outcome,
            "sources_reviewed": reviewed,
            "candidate_sources_rejected": rejected,
            "rejection_reasons": "Unbridged namesakes, search snippets, family-tree assertions, modern people-finder pages, postwar-only leads and sources without an OSS, protected-identifier or Box-file bridge were not assigned. Grouped CIA Reading Room exact-name checks produced no additional defensible person-specific result.",
            "research_notes": f"{detail} The index page and every admitted PDF page were visually checked. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA Catalog API call was made.",
            "next_action": f"Review Box {box} for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before military service.",
            "attempt_number": 1,
            "research_agent_version": "before-oss-b939-v1",
        })
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-939-v1",
        "reviewer": "Before OSS Batch 939 evidence review",
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
