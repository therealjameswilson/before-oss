#!/usr/bin/env python3
"""Generate the reviewed Batch 1007 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page497-wells-to-werner-"
    "review_batch-1007_2026-11-03.json"
)

INDEX = "nara-index-b1007"
ARMY = "army-bulk-b1007"
TECH = "army-tech-b1007"
CODES = "army-codes-b1007"
WERBELL_HISTORY = "nara-werbell-history-b1007"
WERBELL_OSS = "nara-werbell-oss-b1007"
NAS_WELLS = "nas-john-west-wells-b1007"

ORG_ARMY = "us-army-b1007"
ORG_OHIO_STATE = "ohio-state-b1007"
ORG_PALMER = "palmer-radar-b1007"
ORG_STRAWBRIDGE = "strawbridge-clothier-b1007"
ORG_LARTISAN = "lartisan-b1007"
ORG_PRICE = "charles-morris-price-school-b1007"


PEOPLE = {
    1: ("7660dc05-b932-5947-8a11-bd697c70fdb1", "Dorson S Wells"),
    2: ("666ce936-2052-5880-b3ae-6df492bbfe7c", "Edward O Wells"),
    3: ("198c0f14-b3bc-5e5a-9d52-9503cef85ef7", "Frances J Wells"),
    4: ("fbe6bb8d-88c5-59b7-84ec-da59a00725d5", "George K Wells Jr."),
    5: ("d0c82f62-3687-5630-aa68-08193eb7274d", "John W Wells"),
    6: ("f2e7ae70-cdd8-5aa6-bae4-24a99269358d", "Kenneth E Wells"),
    7: ("b8ded288-581c-5deb-8de8-c14e6e6d2ed3", "Lydia F Wells"),
    8: ("b89754a9-ed43-53ef-94c7-5c00b8a957de", "Lyman C Wells"),
    9: ("c3e5d490-25f2-52af-8dba-3a6744bd3e4c", "Marion O Wells"),
    10: ("c06be51c-8294-5d38-90a0-c321153fb607", "Ralph J Wells"),
    11: ("8b6b5d22-c121-58d5-bcb4-f317b3c88152", "Richard S Wells"),
    12: ("5e06c406-a711-5604-8aa9-eb36eb919c8d", "Robert J Wells"),
    13: ("98e8f4ad-841a-54b3-9d00-b2eddfcd3bd5", "Staring Wells"),
    14: ("7659df98-b645-504b-a2f8-cf32fcd507f3", "Warren R Wells"),
    15: ("9f6be017-c897-5886-84f7-ee7531110081", "Winifred G Wells"),
    16: ("3373c334-5112-519f-9cd5-da94b1e2537e", "Vivian Wellwood"),
    17: ("9e224a36-2f9d-552d-8844-e1b6aa782205", "Jerome H Welo"),
    18: ("99d9d8a5-9f99-50b7-bc4a-fd3b31d1b3ad", "Eva B Wels"),
    19: ("45dc201b-9b7c-5f57-82df-23bb7cc2dacd", "Paul J Welsh"),
    20: ("1558bf32-3a55-5c16-b9a6-cf22fa86183a", "Luida Wendell"),
    21: ("65d263fe-859d-5e0a-9cf5-fb398582510c", "Saly Wengel"),
    22: ("87a69f19-f285-558a-bc27-9c155a08a89b", "Irving Wenger"),
    23: ("c6b9e65d-b194-57ee-9ee2-32313dd628c2", "John H Wennberg"),
    24: ("4b69a7f5-b17b-5ed8-92f7-95af6a06e777", "Carl G Wenner"),
    25: ("1ff415e5-57da-50e7-8af1-e6fb6bbb52e9", "Luther J.G. Wenner"),
    26: ("35310cb1-996d-5dbd-92c2-09d33e4ad6bc", "Robert K Wensley"),
    27: ("9db7a686-99df-58d6-855a-b07dff245bdf", "George Wentler"),
    28: ("82c94e31-3810-5a88-8723-86fe24f3cf6a", "Dorothy E Wentworth"),
    29: ("96cfe5ac-0557-5a09-b35f-0cb206603f38", "Nathan H Wentworth"),
    30: ("1650d9e8-4f2d-5f5c-802f-1e4189fd5a94", "Paul T Wentworth"),
    31: ("d3ea8fb7-808e-5b83-8c05-9098f6244f2a", "Robert J Wentworth"),
    32: ("ae4af2b2-505b-5913-afd3-9161ba7d93a3", "Robert J Wentworth"),
    33: ("0f6a0e59-a521-5f32-8902-8dadd70e872f", "Russell A Wentworth"),
    34: ("f0aed3c5-2440-5e45-b8ec-38d607586214", "Donald B Wentzel"),
    35: ("58e485fe-9fcd-5b1c-b229-be0b27d10570", "Francis G Wenzel"),
    36: ("2a3e9061-b725-5382-8361-57923cbb4ae8", "Peter Wenzel"),
    37: ("2627680a-afa9-509d-9332-a0f2fa29213c", "Charlotte L Wepf"),
    38: ("86661c77-6a2f-59b8-9a2e-ce1b3797d9e8", "Mitchell L Wer-Bell"),
    39: ("8289cc71-1234-5008-936d-c0fcc9565a41", "Wilford J Werber"),
    40: ("935fbe7a-3882-5ad8-972f-da066a935ea9", "Leon I Werbin"),
    41: ("a3400fd4-a057-5ebf-84d6-f0d217e4aab6", "Wallace Werble Sr."),
    42: ("727ff070-594f-562a-820b-2f288f921782", "Thomas F Werkich"),
    43: ("44094644-6fc0-5896-8ddd-1436b103b431", "Frank W Werley"),
    44: ("1aa11e0f-bcaa-589e-85ea-6ee3d9a08143", "Daniel S Werner"),
    45: ("7dba3b2a-5e3f-53b9-a387-cfe55fef0581", "Louis B Werner"),
    46: ("3ae20377-34d3-5050-8225-bb4b217b5087", "Louis Werner Jr."),
}


ARMY_MATCHES = {
    9: {"date": "1942-09-22", "code": "553", "occupation": "telegraph, telephone, or power lineman or serviceman", "label": "Linemen and servicemen, telegraph, telephone, and power", "locator": "PDF physical page 174; historical category 5, 7-53", "identity": "confirmed", "publish": True, "detail": "The indexed and Army names agree exactly."},
    11: {"date": "1942-10-22", "code": "106", "occupation": "financial institution clerk", "label": "Financial institution clerks, n.e.c.", "locator": "PDF physical page 171; historical category 1-06", "identity": "confirmed", "publish": True, "detail": "The indexed and Army names agree exactly."},
    22: {"date": "1942-12-14", "code": "992", "occupation": "student", "label": "Students", "locator": "PDF physical page 304; amended historical category 9-92", "identity": "confirmed", "publish": True, "detail": "The indexed and Army names agree exactly."},
    23: {"date": "1942-08-06", "code": "783", "occupation": "mechanic or repairman, not elsewhere classified", "label": "Mechanics and repairmen, n.e.c.", "locator": "PDF physical page 175; historical category 7-83", "identity": "high_confidence", "publish": True, "detail": "The protected identifier agrees, but the Army record gives Henry rather than indexed John H."},
    24: {"date": "1943-08-13", "code": "031", "occupation": "secondary-school teacher or principal", "label": "Teachers (secondary school) and principals", "locator": "PDF physical page 171; historical category 0-31", "identity": "confirmed", "publish": True, "detail": "The indexed and Army names agree exactly."},
    25: {"date": "1942-12-12", "code": "990", "occupation": None, "label": None, "locator": None, "identity": "high_confidence", "publish": False, "detail": "The protected identifier agrees, but the Army name WEVNEI LUTHER is visibly damaged and conflicts with indexed Luther J.G. Wenner."},
    39: {"date": "1940-09-16", "code": "999", "occupation": None, "label": None, "locator": None, "identity": "confirmed", "publish": False, "detail": "The indexed and Army names agree exactly; the reviewed official code material did not provide a reliable public label for code 999."},
    40: {"date": "1942-02-02", "code": "044", "occupation": "commercial artist", "label": "Commercial artists", "locator": "PDF physical page 171; historical category 0-44", "identity": "confirmed", "publish": True, "detail": "The indexed and Army names agree exactly."},
    41: {"date": "1943-12-14", "code": "006", "occupation": "author, editor, or reporter", "label": "Authors, editors, and reporters", "locator": "PDF physical page 170; historical category 0-06", "identity": "confirmed", "publish": True, "detail": "The indexed and Army names agree exactly, including the senior suffix."},
    42: {"date": "1943-04-19", "code": "839", "occupation": "worker in manufacture of miscellaneous finished lumber products", "label": "Occupations in manufacture of miscellaneous finished lumber products, n.e.c.", "locator": "PDF physical page 173; historical categories 4, 6, 8-39", "identity": "confirmed", "publish": True, "detail": "The indexed and Army names agree exactly."},
    43: {"date": "1943-10-09", "code": "736", "occupation": "chauffeur or driver", "label": "Chauffeurs and drivers, bus, taxi, truck, and tractor", "locator": "PDF physical page 174; historical categories 5, 7-36", "identity": "confirmed", "publish": True, "detail": "The indexed and Army names agree exactly."},
}


PRINTED_CATEGORY = {
    2: ("enlisted_army_personnel", False),
    8: ("enlisted_coast_guard_personnel", False),
    44: ("commissioned_army_officer", True),
    46: ("commissioned_army_officer", True),
}

DUPLICATE_GROUPS = {
    31: "name-only:robert-j-wentworth-page497",
    32: "name-only:robert-j-wentworth-page497",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def box_for(row: int) -> str:
    if row <= 12:
        return "825"
    if row <= 40:
        return "826"
    return "827"


def unresolved_reason(row: int) -> str:
    base = (
        "Exact-name and meaningful-variant searches across the NARA index context, "
        "CIA Reading Room, Library of Congress, OSS, employment, occupation, obituary, "
        "institutional, newspaper, directory, and archival sources produced no reliable "
        "identity and pre-OSS affiliation bridge; unbridged namesakes were rejected."
    )
    special = {
        1: "A cemetery-style discovery lead for a Dorson S. Wells supplied no OSS, Box 825, or employer bridge and was rejected. ",
        31: "This separately printed Robert J. Wentworth row is not merged with the identical row 32 without distinguishing evidence. ",
        32: "This separately printed Robert J. Wentworth row is not merged with the identical row 31 without distinguishing evidence. ",
        45: "A prominent radiochemist named Louis B. Werner has no OSS or Box 827 bridge and was rejected as an unconfirmed namesake. ",
        46: "Postwar E. Louis Werner Jr. material is chronologically incompatible and supplies no Box 827 bridge. ",
    }
    return special.get(row, "") + base


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 825-827",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 497, rows 1-46",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 46 printed rows remain separately preserved; full protected identifiers remain private.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; 11 eligible protected-identifier comparisons; identifiers and record ordinals withheld",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "Eleven identity bridges were accepted. No Army record is treated as a named employer, institution, or exact OSS-transfer record.",
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
            "stable_url": "https://catalog.archives.gov/medialz/electronic-records/rg-064/asnf/100.1CL_SD.pdf",
            "archival_identifier": "National Archives Identifier 1263923; Code No. 30",
            "title": "NARA Compiled Code Lists for the Electronic Army Serial Number Merged File",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives at College Park - Electronic Records",
            "publication_record_date": "2011-01-12; modified 2011-03-17",
            "locator": "PDF physical pages 170-175 and 304; reviewed historical civilian-occupation categories",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical labels identify broad occupations or student status, not named employers, institutions, workplaces, or exact OSS-transfer dates.",
        },
        {
            "key": WERBELL_HISTORY,
            "stable_url": "https://www.archives.gov/files/research/jfk/releases/2022/104-10182-10136.pdf",
            "archival_identifier": "JFK release 104-10182-10136",
            "title": "Personnel history memorandum regarding Mitchell Livingston WerBell III",
            "author_creator": "Central Intelligence Agency",
            "repository_publisher": "National Archives and Records Administration",
            "locator": "PDF physical page 1; education and employment sections",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "John F. Kennedy Assassination Records Collection",
            "document_number": "104-10182-10136",
            "rights_notes": "The page was rendered from the original file and visually inspected. Unrelated sensitive personal details are excluded.",
        },
        {
            "key": WERBELL_OSS,
            "stable_url": "https://www.archives.gov/files/research/jfk/releases/104-10112-10321.pdf",
            "archival_identifier": "JFK release 104-10112-10321",
            "title": "Memorandum mentioning Mitchell Livingston WerBell III's OSS service",
            "author_creator": "John F. Meehan, Acting Chief, EAB",
            "repository_publisher": "National Archives and Records Administration",
            "locator": "PDF physical page 2, paragraph 5",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "John F. Kennedy Assassination Records Collection",
            "document_number": "104-10112-10321",
            "rights_notes": "The page was rendered from the original file and visually inspected. The public citation omits the OSS personnel number.",
        },
        {
            "key": NAS_WELLS,
            "stable_url": "https://www.nationalacademies.org/read/5406/chapter/21",
            "archival_identifier": "DOI 10.17226/5406; Biographical Memoirs, volume 70",
            "title": "John West Wells",
            "author_creator": "William R. Brice",
            "repository_publisher": "National Academy of Sciences; National Academies Press",
            "publication_record_date": "1996",
            "locator": "Original page 425 and career chronology on following pages",
            "access_date": "2026-11-03",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Biographical Memoirs, Volume 70",
            "rights_notes": "Supports a qualified common-name identity lead; the index supplies no second independent identifier beyond the name and direct OSS context.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {"key": ORG_ARMY, "organization_id": "24facf23-e75a-54f2-a37a-0ef1509bc18a", "canonical_name": "United States Army", "historical_name": "U.S. Army", "aliases": ["Army of the United States"], "organization_type": "military_service", "sector": "military", "country": "United States", "normalization_notes": "Modeled as a military assignment, never a civilian employer."},
        {"key": ORG_OHIO_STATE, "organization_id": "de52c90c-62bc-532e-a99e-a7d9ca019c09", "canonical_name": "The Ohio State University", "historical_name": "Ohio State University", "aliases": ["Ohio State"], "organization_type": "university", "sector": "academia_and_research", "city": "Columbus", "state_or_region": "Ohio", "country": "United States", "normalization_notes": "Preserves the historical source wording while reusing the reviewed canonical university organization."},
        {"key": ORG_PALMER, "canonical_name": "Palmer Radar Development Laboratories", "historical_name": "Palmer Radar Dev. Laboratories", "aliases": ["Palmer Radar Development Laboratory"], "organization_type": "research laboratory", "sector": "engineering_science_and_technology", "city": "Belmar", "state_or_region": "New Jersey", "country": "United States", "active_dates": "1942-1943 documented for this claim", "normalization_notes": "Preserves the laboratory name and Camp Evans location in the official personnel history; no successor is inferred."},
        {"key": ORG_STRAWBRIDGE, "canonical_name": "Strawbridge & Clothier", "historical_name": "Strawbridge & Clothier Dept. Store", "aliases": ["Strawbridge and Clothier"], "organization_type": "department_store", "sector": "business_and_industry", "city": "Philadelphia", "state_or_region": "Pennsylvania", "country": "United States", "normalization_notes": "Historical department-store employer; no modern successor is substituted."},
        {"key": ORG_LARTISAN, "canonical_name": "L'Artisan", "historical_name": "L'Artisan", "aliases": [], "organization_type": "dress_manufacturer", "sector": "business_and_industry", "city": "Philadelphia", "state_or_region": "Pennsylvania", "country": "United States", "normalization_notes": "The official personnel history describes the organization only as a Philadelphia dress manufacturer; no similarly named firm is inferred."},
        {"key": ORG_PRICE, "canonical_name": "Charles Morris Price School", "historical_name": "Chas. Morris Price School", "aliases": [], "organization_type": "school", "sector": "academia_and_research", "city": "Philadelphia", "state_or_region": "Pennsylvania", "country": "United States", "normalization_notes": "Modeled only as a journalism and advertising student affiliation, not employment."},
    ]


def occupation_key(row: int) -> str:
    return f"{slug(PEOPLE[row][1])}-army-occupation-row{row}-b1007"


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, item in ARMY_MATCHES.items():
        if not item["publish"]:
            continue
        values.append({
            "key": occupation_key(row),
            "person_id": PEOPLE[row][0],
            "occupation": item["occupation"],
            "relationship_type": "student" if item["code"] == "992" else "unknown",
            "end_date": item["date"],
            "date_precision": f"Historical civilian-occupation code {item['code']} was recorded at Army entry on {item['date']}; no named employer, workplace, institution, or exact OSS-transfer date is supplied.",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": item["identity"],
            "claim_confidence": "medium",
            "source_quality": "A_direct_official",
            "publication_status": "publish_qualified",
            "research_notes": "Broad historical category only; no named employer, institution, workplace, or OSS transition is inferred.",
        })

    values.extend([
        {"key": "john-west-wells-ohio-state-b1007", "person_id": PEOPLE[5][0], "organization_key": ORG_OHIO_STATE, "organization_name_as_found": "Ohio State University", "role_title": "Faculty member; professor by 1948", "occupation": "paleontologist and university teacher", "relationship_type": "employment", "start_date": "1938", "end_date": "1948", "date_precision": "The memoir gives the 1938-1948 Ohio State faculty span and says he served with OSS during World War II; exact wartime leave and OSS-entry dates are not stated.", "city": "Columbus", "state_or_region": "Ohio", "country": "United States", "immediate_pre_oss": True, "last_civilian_pre_service": True, "pre_oss_temporal_basis": "probable_immediate", "identity_confidence": "probable", "claim_confidence": "medium", "source_quality": "B_authoritative_institutional", "publication_status": "publish_qualified", "research_notes": "Qualified common-name identity lead. The exact middle initial and direct OSS biography align, but the index lacks the second corroborating identifier required for confirmation."},
        {"key": "werbell-army-b1007", "person_id": PEOPLE[38][0], "organization_key": ORG_ARMY, "organization_name_as_found": "U.S. Army", "role_title": "Army service member", "relationship_type": "military_assignment", "start_date": "1943-04", "end_date": "1945-07", "date_precision": "The personnel history says he left Palmer to enter the Army in April 1943; a separate official memo dates OSS service to July-December 1945. Continuous Army affiliation is probable but not explicitly stated.", "country": "United States", "immediate_pre_oss": True, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "probable_immediate", "identity_confidence": "confirmed", "claim_confidence": "medium", "source_quality": "A_direct_official", "publication_status": "publish_qualified", "research_notes": "Best-supported military pathway, visibly qualified because the exact Army unit and OSS transfer are not stated."},
        {"key": "werbell-palmer-b1007", "person_id": PEOPLE[38][0], "organization_key": ORG_PALMER, "organization_name_as_found": "Palmer Radar Dev. Laboratories", "role_title": "Employee", "relationship_type": "employment", "start_date": "1942-04", "end_date": "1943-04", "date_precision": "The official personnel history gives April 1942-April 1943 and explicitly says he left to enter the U.S. Army.", "city": "Belmar", "state_or_region": "New Jersey", "country": "United States", "immediate_pre_oss": False, "last_civilian_pre_service": True, "pre_oss_temporal_basis": "explicit_immediate", "identity_confidence": "confirmed", "claim_confidence": "confirmed", "source_quality": "A_direct_official", "publication_status": "published", "research_notes": "Direct last-civilian-employer evidence before Army service; no occupational title is inferred."},
        {"key": "werbell-strawbridge-b1007", "person_id": PEOPLE[38][0], "organization_key": ORG_STRAWBRIDGE, "organization_name_as_found": "Strawbridge & Clothier Dept. Store", "role_title": "Assistant advertising manager", "occupation": "advertising manager", "relationship_type": "employment", "start_date": "1939-11", "end_date": "1942-04", "date_precision": "The official personnel history gives November 1939-April 1942.", "city": "Philadelphia", "state_or_region": "Pennsylvania", "country": "United States", "immediate_pre_oss": False, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "confirmed", "claim_confidence": "confirmed", "source_quality": "A_direct_official", "publication_status": "published", "research_notes": "Earlier documented employment, kept separate from the subsequent Palmer laboratory job."},
        {"key": "werbell-lartisan-b1007", "person_id": PEOPLE[38][0], "organization_key": ORG_LARTISAN, "organization_name_as_found": "L'Artisan", "role_title": "Employee", "relationship_type": "employment", "start_date": "1939-02", "end_date": "1939-11", "date_precision": "The official personnel history gives February-November 1939 and describes the employer as a Philadelphia dress manufacturer.", "city": "Philadelphia", "state_or_region": "Pennsylvania", "country": "United States", "immediate_pre_oss": False, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "confirmed", "claim_confidence": "confirmed", "source_quality": "A_direct_official", "publication_status": "published", "research_notes": "Earlier documented employment; no occupational title is inferred."},
        {"key": "werbell-price-school-b1007", "person_id": PEOPLE[38][0], "organization_key": ORG_PRICE, "organization_name_as_found": "Chas. Morris Price School", "role_title": "Night student in journalism and advertising", "occupation": "student", "relationship_type": "student", "start_date": "1939", "end_date": "1941", "date_precision": "The official personnel history gives 1939-1941 and identifies night-school journalism and advertising study.", "city": "Philadelphia", "state_or_region": "Pennsylvania", "country": "United States", "immediate_pre_oss": False, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "confirmed", "claim_confidence": "confirmed", "source_quality": "A_direct_official", "publication_status": "published", "research_notes": "Student affiliation only; the school is not treated as an employer."},
    ])
    return values


def make_claim(*, key: str, row: int, claim_type: str, text: str, paraphrase: str, identity: str, temporal: str, quality: str, confidence: str, publication: str, notes: str, source_links: list[dict[str, str]], affiliation_key: str | None = None) -> dict[str, object]:
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
    for row, item in ARMY_MATCHES.items():
        if not item["publish"]:
            continue
        name = PEOPLE[row][1]
        values.append(make_claim(
            key=f"occupation-{slug(name)}-row{row}-b1007",
            row=row,
            claim_type="occupation",
            text=f"At Army entry on {item['date']}, {name} was recorded in the historical {item['occupation']} category; no named employer or institution is identified.",
            paraphrase=f"The accepted Army record carries civilian-occupation code {item['code']}, decoded from NARA's official code list.",
            identity="The category belongs only to the accepted protected-identifier match; the identifier itself is not public.",
            temporal="Strongly date-bounded to Army entry; it does not establish the immediate pre-OSS affiliation or a named employer, workplace, or institution.",
            quality="A_direct_official",
            confidence="medium",
            publication="publish_qualified",
            notes="Published with its limits and excluded from verified-employer analytics.",
            source_links=[
                {"source_key": ARMY, "locator_override": f"Army entry {item['date']}; civilian occupation code {item['code']}; protected identifier withheld"},
                {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46"},
                {"source_key": CODES, "locator_override": item["locator"], "excerpt_override": item["label"]},
            ],
            affiliation_key=occupation_key(row),
        ))

    values.extend([
        make_claim(key="identity-john-west-wells-b1007", row=5, claim_type="identity", text="Indexed John W. Wells is a probable match to paleontologist John West Wells, an Ohio State faculty member who served with OSS in Europe.", paraphrase="A National Academy of Sciences memoir supplies the full middle name, 1938-1948 Ohio State faculty span, and direct OSS wartime service.", identity="Probable common-name match: exact name and middle initial plus direct OSS context align, but the index provides no second independent identifier for confirmation.", temporal="The memoir places Ohio State employment across 1938-1948 and OSS service during World War II.", quality="B_authoritative_institutional", confidence="medium", publication="publish_qualified", notes="Qualified and excluded from default confirmed/high identity analytics pending Box 825 review.", source_links=[{"source_key": INDEX, "locator_override": "PDF page 497 row 5"}, {"source_key": NAS_WELLS, "locator_override": "Original page 425", "excerpt_override": "at Ohio State University (1938-48). During World War II he served with the Office of Strategic Services"}]),
        make_claim(key="immediate-john-west-wells-ohio-state-b1007", row=5, claim_type="immediate_pre_oss_affiliation", text="If the probable identity is confirmed, Ohio State University is John West Wells's best-supported immediate pre-OSS institutional affiliation.", paraphrase="The memoir dates his Ohio State faculty tenure to 1938-1948 and states that he served with OSS during World War II.", identity="Probable common-name match pending the Box 825 personnel file.", temporal="Probable immediate affiliation; wartime leave and OSS-entry dates are not supplied.", quality="B_authoritative_institutional", confidence="medium", publication="publish_qualified", notes="Visibly qualified and excluded from default employer analytics.", source_links=[{"source_key": NAS_WELLS, "locator_override": "Original page 425 and Ohio State career paragraph", "excerpt_override": "served on the faculty ... at Ohio State University (1938-48)"}], affiliation_key="john-west-wells-ohio-state-b1007"),
        make_claim(key="last-civilian-john-west-wells-ohio-state-b1007", row=5, claim_type="last_civilian_pre_service", text="If the probable identity is confirmed, Ohio State University is John West Wells's last documented civilian employer before OSS service.", paraphrase="The memoir presents Ohio State faculty employment and wartime OSS service within the same 1938-1948 career span.", identity="Probable common-name match pending the Box 825 personnel file.", temporal="Probable last civilian employment; exact leave and return dates are not stated.", quality="B_authoritative_institutional", confidence="medium", publication="publish_qualified", notes="Presented as a qualified lead, not a settled fact.", source_links=[{"source_key": NAS_WELLS, "locator_override": "Original page 425 and Ohio State career paragraph", "excerpt_override": "at Ohio State University (1938-48)"}], affiliation_key="john-west-wells-ohio-state-b1007"),
        make_claim(key="identity-mitchell-werbell-b1007", row=38, claim_type="identity", text="Indexed Mitchell L. Wer-Bell is Mitchell Livingston WerBell III, whose official personnel history and OSS memorandum document the same rare full name and wartime service.", paraphrase="The index spelling, exact middle initial, official full-name expansion, personnel history, and direct July-December 1945 OSS statement align.", identity="Confirmed by two official records plus the rare indexed name; the public claim omits protected service identifiers.", temporal="The records date Army entry to April 1943 and OSS service to July-December 1945.", quality="A_direct_official", confidence="confirmed", publication="published", notes="Name variants remain visible; unrelated sensitive details are not published.", source_links=[{"source_key": INDEX, "locator_override": "PDF page 497 row 38; protected identifier masked"}, {"source_key": WERBELL_HISTORY, "locator_override": "PDF physical page 1", "excerpt_override": "FULL NAME Mitchell Livingston WerBell III"}, {"source_key": WERBELL_OSS, "locator_override": "PDF physical page 2, paragraph 5", "excerpt_override": "was in the OSS briefly (7/45-12/45) during WW II"}]),
        make_claim(key="immediate-werbell-army-b1007", row=38, claim_type="immediate_pre_oss_affiliation", text="The U.S. Army is Mitchell Livingston WerBell III's best-supported immediate pre-OSS affiliation, though the exact unit and transfer date remain undocumented.", paraphrase="One official record says he left Palmer to enter the Army in April 1943; another dates OSS service to July-December 1945.", identity="Confirmed exact-person official source chain.", temporal="Probable immediate military pathway; the records leave a two-year interval and do not state continuous service or an exact transfer.", quality="A_direct_official", confidence="medium", publication="publish_qualified", notes="Military assignment is not counted as a civilian employer.", source_links=[{"source_key": WERBELL_HISTORY, "locator_override": "PDF physical page 1, Palmer employment entry", "excerpt_override": "Left to enter U.S. Army"}, {"source_key": WERBELL_OSS, "locator_override": "PDF physical page 2, paragraph 5", "excerpt_override": "was in the OSS briefly (7/45-12/45) during WW II"}], affiliation_key="werbell-army-b1007"),
        make_claim(key="last-civilian-werbell-palmer-b1007", row=38, claim_type="last_civilian_pre_service", text="Palmer Radar Development Laboratories was Mitchell Livingston WerBell III's last civilian employer before he entered the U.S. Army in April 1943.", paraphrase="The official personnel history gives the employer, April 1942-April 1943 dates, Camp Evans location, and explicit departure for the Army.", identity="Confirmed exact-person official personnel history and separate official OSS record.", temporal="Explicit last civilian employment before Army service.", quality="A_direct_official", confidence="confirmed", publication="published", notes="No occupational title beyond employee is inferred from the source.", source_links=[{"source_key": WERBELL_HISTORY, "locator_override": "PDF physical page 1, employment section", "excerpt_override": "Palmer Radar Dev. Laboratories ... Left to enter U.S. Army"}], affiliation_key="werbell-palmer-b1007"),
        make_claim(key="earlier-werbell-strawbridge-b1007", row=38, claim_type="other_pre_oss_affiliation", text="Mitchell Livingston WerBell III worked as assistant advertising manager for Strawbridge & Clothier from November 1939 to April 1942.", paraphrase="The official personnel history explicitly supplies the employer, role, Philadelphia location, and dates.", identity="Confirmed exact-person official source chain.", temporal="Documented prewar employment preceding the Palmer laboratory job.", quality="A_direct_official", confidence="confirmed", publication="published", notes="Kept separate from the later last-civilian employer.", source_links=[{"source_key": WERBELL_HISTORY, "locator_override": "PDF physical page 1, employment section", "excerpt_override": "Assistant advertising manager for Strawbridge & Clothier Dept. Store"}], affiliation_key="werbell-strawbridge-b1007"),
        make_claim(key="earlier-werbell-lartisan-b1007", row=38, claim_type="other_pre_oss_affiliation", text="Mitchell Livingston WerBell III worked for the Philadelphia dress manufacturer L'Artisan from February to November 1939.", paraphrase="The official personnel history explicitly supplies the employer description, city, and dates.", identity="Confirmed exact-person official source chain.", temporal="Documented prewar employment preceding Strawbridge & Clothier.", quality="A_direct_official", confidence="confirmed", publication="published", notes="No job title is inferred.", source_links=[{"source_key": WERBELL_HISTORY, "locator_override": "PDF physical page 1, employment section", "excerpt_override": "Worked for 'L'Artisan', dress manufacturer in Philadelphia"}], affiliation_key="werbell-lartisan-b1007"),
        make_claim(key="student-werbell-price-school-b1007", row=38, claim_type="other_pre_oss_affiliation", text="Mitchell Livingston WerBell III attended the Charles Morris Price School at night for journalism and advertising from 1939 to 1941.", paraphrase="The official personnel history identifies the school, subjects, night-study status, and years.", identity="Confirmed exact-person official source chain.", temporal="Documented prewar student affiliation.", quality="A_direct_official", confidence="confirmed", publication="published", notes="Student status is not employment.", source_links=[{"source_key": WERBELL_HISTORY, "locator_override": "PDF physical page 1, education section", "excerpt_override": "Chas. Morris Price School (Journalism & Advertising - night school)"}], affiliation_key="werbell-price-school-b1007"),
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
    if row in PRINTED_CATEGORY:
        value["personnel_category"], value["commissioned_officer"] = PRINTED_CATEGORY[row]
    if row in DUPLICATE_GROUPS:
        value["possible_duplicate_group"] = DUPLICATE_GROUPS[row]
    value.update(overrides)
    return value


def person_updates() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    special = set(ARMY_MATCHES) | {5, 38}
    for row in sorted(set(PEOPLE) - special):
        reason = unresolved_reason(row)
        values.append(base_update(
            row,
            identity_status="unresolved",
            identity_evidence=f"The visually verified page 497 source preserves {PEOPLE[row][1]}, its printed rank or notation, archival box, and location. {reason}",
            research_status="requires_archival_review",
            next_action=f"Review the indexed Box {box_for(row)} personnel file for corroborating identifiers, the immediate pre-OSS affiliation, and the last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}",
        ))
    for row, item in ARMY_MATCHES.items():
        status = "occupation_only_found" if item["publish"] else "requires_archival_review"
        next_action = (
            f"Review the indexed Box {box_for(row)} personnel file to identify any named employer or institution behind the broad {item['occupation']} category and establish the Army-to-OSS chronology."
            if item["publish"]
            else f"Review the indexed Box {box_for(row)} personnel file to resolve the damaged or undefined Army occupation code and establish the Army-to-OSS chronology."
        )
        values.append(base_update(row, identity_status=item["identity"], identity_evidence=item["detail"] + " A nonshared protected identifier supports the match and remains private.", personnel_category="enlisted_army_personnel", commissioned_officer=False, research_status=status, next_action=next_action, nara_catalog_id="1263923"))
    values.extend([
        base_update(5, identity_status="probable", identity_evidence="The National Academy of Sciences memoir supplies the full name John West Wells, exact middle initial, Ohio State chronology, and direct OSS service, but the common-name index row lacks a second independent identifier for confirmation.", research_status="requires_archival_review", archival_review_priority="critical", next_action="Review the Box 825 personnel file to confirm whether the indexed John W. Wells is paleontologist John West Wells and to establish the exact Ohio State leave and OSS-entry dates."),
        base_update(38, identity_status="confirmed", identity_evidence="Two official NARA-released records expand the rare indexed name to Mitchell Livingston WerBell III, supply a direct personnel history, and date his OSS service to July-December 1945. The reviewed records establish Army service but do not establish an enlisted or commissioned grade.", name_variants=["Mitchell L Wer-Bell", "Mitchell Livingston WerBell III"], replace_name_variants=True, personnel_category="unknown_or_indeterminate", commissioned_officer=None, research_status="verified_employer_found", archival_review_priority="medium", next_action="Review the Box 826 personnel file to identify the exact Army unit, grade, and OSS transfer date; Palmer Radar Development Laboratories is directly established as the last civilian employer before Army service."),
    ])
    if len(values) != len(PEOPLE):
        raise RuntimeError(f"Expected {len(PEOPLE)} person updates, generated {len(values)}")
    return values


def research_attempts() -> list[dict[str, object]]:
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        if row == 38:
            outcome, reviewed, rejected = "source_reviewed", 14, 5
            note = "Two visually inspected official NARA documents confirm identity, direct OSS service, Palmer as the last civilian employer before Army service, earlier Strawbridge & Clothier and L'Artisan jobs, and night study at the Charles Morris Price School."
        elif row == 5:
            outcome, reviewed, rejected = "source_reviewed", 10, 6
            note = "A National Academy of Sciences memoir supports a probable John West Wells identity and qualified Ohio State employment lead; the common-name match still requires Box 825 confirmation."
        elif row in ARMY_MATCHES:
            item = ARMY_MATCHES[row]
            outcome, reviewed, rejected = "source_reviewed", 9, 5
            note = (f"A reviewed protected-identifier Army bridge supports identity and a qualified {item['occupation']} category at Army entry; no named employer, institution, workplace, or OSS-transfer date is supplied." if item["publish"] else "The protected-identifier match is retained privately, but the damaged or undefined historical occupation code is not published as a pre-OSS occupation.")
        else:
            outcome, reviewed, rejected = "candidate_rejected", 7, 6
            note = unresolved_reason(row)
        attempts.append({
            "key": f"page497-row{row}-{slug(name)}-b1007",
            "person_id": person_id,
            "source_adapter": "manual_staged_protocol",
            "query_text": f"{name}; NARA OSS index context; CIA Reading Room, National Archives, and Library of Congress exact-name domain checks; exact-name and meaningful spelling, initial, suffix, punctuation, transliteration, and OCR variants; OSS, rank, branch, assignment, and identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory, and archival searches; indexed Box {box_for(row)}; protected identifiers used only in private official-record comparison",
            "query_variant_type": "staged_identity_employment_archival_protocol_batch_1007",
            "started_at": "2026-11-04T01:15:00Z",
            "completed_at": "2026-11-04T02:35:00Z",
            "outcome": outcome,
            "sources_reviewed": reviewed,
            "candidate_sources_rejected": rejected,
            "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, postwar-only leads, discovery-only biographies, and sources without an OSS, protected-identifier, rank, unit, or personnel-file bridge were rejected. Historical Army categories were not converted into named employers, workplaces, or institutions. Student status was not converted into employment.",
            "research_notes": f"{note} Exact-name official-domain, OSS, employer, occupation, obituary, biography, institutional, newspaper, directory, and archival searches were checked as applicable. NARA index page 497 was rendered and visually checked. Relevant Army code pages and both WerBell official-document pages were rendered and visually inspected. No authenticated NARA Catalog API call was made.",
            "next_action": f"Review the indexed Box {box_for(row)} personnel file for corroborating identifiers, the immediate pre-OSS affiliation, and the last civilian employer before wartime service.",
            "attempt_number": 1,
            "research_agent_version": "before-oss-b1007-v1",
        })
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-1007-v1",
        "reviewer": "Before OSS Batch 1007 evidence review",
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
