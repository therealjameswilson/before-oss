#!/usr/bin/env python3
"""Generate the reviewed Batch 929 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import uuid
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / (
    "research/evidence-page455-mitsue-m-sugimachi-to-john-l-sullivan-"
    "review_batch-929_2026-10-27.json"
)

INDEX = "nara-index-b929"
ARMY = "army-bulk-b929"
TECH = "army-tech-b929"
CODES = "army-codes-b929"
VMI_CATALOG = "vmi-register-catalog-b929"
VMI_REGISTER = "vmi-register-transcription-b929"
CIA_SUHLING = "cia-suhling-b929"
CIA_SUHLING_ROLE = "cia-suhling-role-b929"
ABQ_ROSTER = "abq-sugimachi-roster-b929"
DISCOVER_NIKKEI = "discover-nikkei-yaemitsu-b929"
ENEMY_ALIEN = "enemy-alien-mitsue-b929"
SUISSA_CERT = "suissa-ffc-certificate-b929"
OCS_ROSTER = "artillery-ocs-roster-b929"
SUKER_STUDY = "orman-suker-scholarly-study-b929"

PEOPLE = {
    1: ("4b9ee9ae-406e-5052-acfb-3342458b1a0e", "Mitsue M Sugimachi", "756"),
    2: ("c3272091-5088-51b8-a22a-ed9686c963db", "Yaemitsu Sugimachi", "756"),
    3: ("e7f51c31-fef5-5a95-861a-2b216f1d62b1", "David M Sugimoto", "756"),
    4: ("faf7bbe1-a238-51b8-83fc-2728936d170c", "Sang P Suh", "756"),
    5: ("9d148818-62e7-5f99-a98f-96829d17b157", "Young Wan Suh", "756"),
    6: ("f4f5e550-d483-542b-877a-c29ead135b2b", "William G Suhling", "756"),
    7: ("656be164-41d6-5db8-b90b-5a5800c8d62a", "Joseph Suhovich", "756"),
    8: ("949dff8a-61ee-59cc-908b-cc72c2a066ab", "Jacques Suissa", "756"),
    9: ("ecad2fa4-9c31-5190-81ba-dd5ec303143d", "Albert F Suitor", "756"),
    10: ("a9d32691-f8c4-5f45-b96d-6dc02418f59d", "Orman Suker", "757"),
    11: ("c27ef2e8-8fb2-5d4a-aa2e-29fc47eca4e2", "Awat B Sulaiman", "757"),
    12: ("8173b048-fdfc-5637-b358-26f402110775", "Boyd Sullivan", "757"),
    13: ("566d31ed-9087-5e94-bf31-54c481724905", "Charles C Sullivan", "757"),
    14: ("e1667c65-fa29-50f2-91a1-cfe51fd86368", "Dorothy F Sullivan", "757"),
    15: ("5ca8a9e4-b2a3-5b59-9eb6-60bf037ea1f9", "Edmund F Sullivan", "757"),
    16: ("c0ec7141-053c-5395-82bc-23cf3f2b0f4f", "Eileen B Sullivan", "757"),
    17: ("3a75805e-7d9a-5d41-a472-37ecfd6c91c4", "Francis Sullivan", "757"),
    18: ("90c20580-29f1-5c8e-bfa6-3602da404576", "Herbert M Sullivan", "757"),
    19: ("b11e3f9d-a49a-5692-9b93-42677d73b9ca", "James A Sullivan", "757"),
    20: ("537b148b-dded-55a5-9efb-cbe45ae0d5e7", "James M Sullivan", "757"),
    21: ("5403327d-921c-523c-aaff-84ee6645e0e2", "John A Sullivan", "757"),
    22: ("143102f8-5932-59ae-b577-9005ebbe6c99", "John E Sullivan", "757"),
    23: ("8aaf8dbf-7222-50a3-87a3-229778ac91d5", "John L Sullivan", "757"),
}

ARMY_IDENTITIES = {
    7: {"entry": "1942-05-28", "grade": "PVT", "code": "736"},
    9: {"entry": "1941-02-18", "grade": "PVT", "code": "304"},
    12: {"entry": "1946-01-21", "grade": "PVT", "code": "201", "variant": "Boyd S Sullivan"},
    15: {"entry": "1942-09-30", "grade": "PVT", "code": "136"},
    17: {"entry": "1942-05-04", "grade": "PVT", "code": "736", "variant": "Francis L Sullivan"},
    18: {"entry": "1944-01-18", "grade": "PVT", "code": "992"},
}

ARMY_OCCUPATIONS = {
    7: ("Chauffeurs and drivers, bus, taxi, truck, and tractor", "employment", "PDF physical page 174; historical category 7-36"),
    9: ("Dairy farmers", "employment", "PDF physical page 172; historical category 3-04"),
    15: ("Statistical clerks and compilers", "employment", "PDF physical pages 171 and 304; historical category 1-36"),
    17: ("Chauffeurs and drivers, bus, taxi, truck, and tractor", "employment", "PDF physical page 174; historical category 7-36"),
    18: ("Students", "student", "PDF physical page 304; amended historical category 9-92"),
}

UNRESOLVED = {
    3: "A wartime David Sugimoto associated with Agar Company and the 442nd/522nd lacks a middle-initial, protected-identifier or Box 756 bridge and was rejected.",
    4: "Exact-name, transliteration and institutional searches found no corroborating identifier or reliable pre-OSS affiliation.",
    5: "Exact-name and transliteration searches found no source connecting the indexed person to a pre-OSS employer or institution.",
    11: "Exact-name and spelling-variant searches found no defensible OSS identity bridge or pre-OSS affiliation.",
    13: "Common-name searches and the printed identifier produced no independently corroborated identity or reliable pre-OSS affiliation.",
    14: "Common-name searches produced multiple namesakes and no two-identifier bridge to the Box 757 person.",
    16: "Common-name searches produced multiple namesakes and no two-identifier bridge to the Box 757 person.",
    19: "Common-name searches produced multiple namesakes and no two-identifier bridge to the Box 757 person.",
    20: "Common-name searches produced multiple namesakes and no two-identifier bridge to the Box 757 person.",
    21: "Common-name searches produced multiple namesakes and no two-identifier bridge to the Box 757 person.",
    22: "Common-name and printed-identifier searches produced no independently corroborated identity or reliable pre-OSS affiliation.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def duplicate_group(key: str) -> str:
    return str(uuid.uuid5(uuid.NAMESPACE_URL, f"before-oss:{key}"))


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 756-757",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 455, rows 1-23; checked against layout-preserving text and the rendered page image",
            "access_date": "2026-10-27",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. Full identifiers remain private. The first John L Sullivan row is not merged with two adjacent identical printed rows.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; six accepted Batch 929 protected-identifier candidates",
            "access_date": "2026-10-27",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "No raw record or full protected identifier is retained in public assets. Boyd Sullivan's 1946 entry is post-OSS and is used only for identity classification.",
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
            "access_date": "2026-10-27",
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
            "locator": "PDF physical pages 171, 172, 174 and 304; Batch 929 categories visually checked",
            "access_date": "2026-10-27",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical categories identify neither employer nor workplace. The 1946 Boyd Sullivan category is not published as pre-OSS evidence.",
        },
        {
            "key": VMI_CATALOG,
            "stable_url": "https://www.familysearch.org/search/catalog/2538363",
            "title": "Register of former cadets: 1939",
            "author_creator": "Virginia Military Institute",
            "repository_publisher": "FamilySearch Library catalog",
            "publication_record_date": "1939",
            "locator": "Centennial edition; Class of 1918 register source description",
            "access_date": "2026-10-27",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Virginia Military Institute former-cadet registers",
            "rights_notes": "Catalog context for the 1939 institutional register; the linked transcription supplies the reviewed entry text.",
        },
        {
            "key": VMI_REGISTER,
            "stable_url": "https://genealogytrails.com/vir/rockbridge/vmi/cadet_class_registers/cadets_1918.html",
            "title": "Register of Former Cadets, 1939: Class of 1918",
            "author_creator": "Virginia Military Institute; transcribed by Genealogy Trails",
            "repository_publisher": "Genealogy Trails History Group",
            "publication_record_date": "1939 register; transcription accessed 2026",
            "locator": "Suhling, William Gerhard, Jr. entry",
            "access_date": "2026-10-27",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "VMI cadet class registers",
            "rights_notes": "The historical register names a 1939 company and presidency but does not state that it was immediately prior to OSS service.",
        },
        {
            "key": CIA_SUHLING,
            "stable_url": "https://www.cia.gov/resources/csi/static/Conein-Contrasts-and-Controversy.pdf",
            "title": "No Boy Scout: D. G. 'Dewey' Clarridge and the Early History of CIA",
            "author_creator": "Thomas A. Boghardt",
            "repository_publisher": "Central Intelligence Agency, Center for the Study of Intelligence",
            "publication_record_date": "Studies in Intelligence, Vol. 67, No. 3 (September 2023)",
            "locator": "Footnote citing William G. Suhling Jr. to John Magruder, 18 December 1945",
            "access_date": "2026-10-27",
            "source_quality": "A_direct_official",
            "collection_name": "Studies in Intelligence",
            "rights_notes": "Official OSS-era name corroboration; it does not document the 1939 company.",
        },
        {
            "key": CIA_SUHLING_ROLE,
            "stable_url": "https://www.cia.gov/readingroom/docs/CIA%20AND%20NAZI%20WAR%20CRIM.%20AND%20COL.%20CHAP.%201-10%2C%20DRAFT%20WORKING%20PAPER_0004.pdf",
            "title": "CIA and Nazi War Criminals: Draft Working Paper, chapters 1-10",
            "author_creator": "Central Intelligence Agency History Staff",
            "repository_publisher": "Central Intelligence Agency Reading Room",
            "publication_record_date": "Draft working paper released through CIA Reading Room",
            "locator": "September 1945 discussion naming Lt. Col. William G. Suhling Jr. as deputy of the German Mission",
            "access_date": "2026-10-27",
            "source_quality": "A_direct_official",
            "collection_name": "CIA Nazi War Crimes Disclosure Act records",
            "rights_notes": "Used to support commissioned Army classification and OSS-era identity; it does not document the 1939 company.",
        },
        {
            "key": ABQ_ROSTER,
            "stable_url": "https://www.cabq.gov/artsculture/albuquerque-museum/documents/prisoner-rosters-for-confinement-sites-in-nm.pdf",
            "title": "Prisoner Rosters for Confinement Sites in New Mexico",
            "author_creator": "Albuquerque Museum",
            "repository_publisher": "City of Albuquerque",
            "publication_record_date": "Compilation accessed 2026",
            "locator": "Yaemitsu Sugimachi roster entry; occupation Teacher; arrested 28 April 1942",
            "access_date": "2026-10-27",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Japanese American wartime confinement research materials",
            "rights_notes": "Home address and next-of-kin details are excluded from public evidence. The occupation names no school or employer.",
        },
        {
            "key": DISCOVER_NIKKEI,
            "stable_url": "https://discovernikkei.org/en/journal/2023/1/9/nihon-jikan-la-3/",
            "title": "The Japanese Hour Radio Show in Los Angeles (Part 3)",
            "author_creator": "Tetsuya Hirahara",
            "repository_publisher": "Discover Nikkei, Japanese American National Museum",
            "publication_record_date": "2023-01-09",
            "locator": "Discussion of the September 1932 Los Angeles Japanese-language broadcast and Sugimachi Yaemitsu",
            "access_date": "2026-10-27",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Discover Nikkei Journal",
            "rights_notes": "The article documents reporting work in 1932, not an immediate transition to OSS or continued employment through 1942.",
        },
        {
            "key": ENEMY_ALIEN,
            "stable_url": "https://gaic.info/wp-content/uploads/2016/02/1949-1947-TunaCanyon-intern-listrevised.pdf",
            "archival_identifier": "Enemy Alien Control Unit case list, file 15942/2374, box 151",
            "title": "Department of Justice Enemy Alien Case Files list",
            "author_creator": "German American Internee Coalition; compiled from National Archives case-file listings",
            "repository_publisher": "German American Internee Coalition",
            "publication_record_date": "Revised list accessed 2026",
            "locator": "Sugimachi, Mitsue Marie entry",
            "access_date": "2026-10-27",
            "source_quality": "D_correlative_or_secondary",
            "collection_name": "World War II enemy alien case-file reference list",
            "rights_notes": "Used only as a probable name expansion. It supplies no employer and does not establish an OSS role.",
        },
        {
            "key": SUISSA_CERT,
            "stable_url": "https://www.plan-sussex-1944.net/en/biographies/pdf/suissa_attestation_FFC.pdf",
            "archival_identifier": "French War Ministry certificate no. 77.262",
            "title": "Attestation d'appartenance aux Forces Françaises Combattantes: Jacques Suissa",
            "author_creator": "Ministère de la Guerre, Direction du personnel militaire de l'armée de terre",
            "repository_publisher": "Plan Sussex 1944 historical project",
            "publication_record_date": "1949-08-06",
            "locator": "Single-page certificate; Sussex (Proust) network; 11 July-30 September 1944",
            "access_date": "2026-10-27",
            "source_quality": "A_direct_official",
            "collection_name": "Plan Sussex participant records",
            "document_number": "77.262",
            "rights_notes": "The certificate documents wartime service and a mission-duration corresponding grade; it supplies no pre-OSS employer.",
        },
        {
            "key": OCS_ROSTER,
            "stable_url": "https://artilleryocshistory.org/uploads/1/4/5/9/145902858/ocs_class_rosters_1940s__updated_7-21-2025_.pdf",
            "title": "1940s Field Artillery Officer Candidate School Class Rosters",
            "author_creator": "Field Artillery OCS Alumni Association historical project; Penny Dunham",
            "repository_publisher": "Field Artillery OCS Alumni Association",
            "publication_record_date": "Updated 2025-07-21",
            "locator": "PDF physical page 119; Orman Suker in the continuation of class 72-43, which began 15 April and graduated 7 July 1943",
            "access_date": "2026-10-27",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Field Artillery OCS class rosters",
            "rights_notes": "The page was visually inspected because a new class begins mid-page. Suker belongs to class 72-43, not 73-43.",
        },
        {
            "key": SUKER_STUDY,
            "stable_url": "https://hrcak.srce.hr/file/280840",
            "title": "Neuspjeh jedne misije: Britanska vojna misija kod četničkog vojvode Pavla Đurišića u Crnoj Gori 1944. godine",
            "author_creator": "Davor Marijan",
            "repository_publisher": "Croatian Institute of History / Hrčak",
            "publication_record_date": "Scholarly article accessed 2026",
            "locator": "Discussion of Lt. Orman Suker, OSS Yugoslav section in Bari, 6 October 1944",
            "access_date": "2026-10-27",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Croatian scholarly journals portal",
            "rights_notes": "Used to establish a later dated OSS assignment and commissioned rank; it does not identify civilian employment.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": "suhling-company-b929",
            "canonical_name": "Suhling & Co., Inc.",
            "historical_name": "Suhling & Co., Inc.",
            "aliases": [],
            "organization_type": "leaf tobacco packing, dealing and exporting company",
            "sector": "business_and_industry",
            "city": "Lynchburg",
            "state_or_region": "Virginia",
            "country": "United States",
            "active_dates": "Documented in the 1939 VMI register; broader dates not established in the reviewed sources",
            "normalization_notes": "Historical name preserved. No successor or modern equivalent is inferred.",
        },
        {
            "key": "rafu-shimpo-b929",
            "canonical_name": "Rafu Shimpo",
            "historical_name": "Rafu Shimpo",
            "aliases": ["Rafu Shimpo newspaper"],
            "organization_type": "Japanese-language newspaper",
            "sector": "journalism_and_media",
            "city": "Los Angeles",
            "state_or_region": "California",
            "country": "United States",
            "active_dates": "Sugimachi employment documented in 1932; exact tenure not established",
            "normalization_notes": "Historical newspaper name preserved. No uninterrupted tenure through 1942 is inferred.",
        },
        {
            "key": "field-artillery-ocs-b929",
            "canonical_name": "U.S. Army Field Artillery Officer Candidate School",
            "historical_name": "Field Artillery Officer Candidate School",
            "aliases": ["Field Artillery OCS"],
            "organization_type": "military officer training school",
            "sector": "military",
            "country": "United States",
            "active_dates": "World War II",
            "normalization_notes": "Normalized as a U.S. Army military training institution; it is not a civilian employer.",
        },
    ]


def affiliations() -> list[dict[str, object]]:
    result: list[dict[str, object]] = []
    for row, (occupation, relationship, _locator) in ARMY_OCCUPATIONS.items():
        data = ARMY_IDENTITIES[row]
        result.append({
            "key": f"{slug(PEOPLE[row][1])}-occupation-b929",
            "person_id": PEOPLE[row][0],
            "occupation": occupation,
            "relationship_type": relationship,
            "end_date": data["entry"],
            "date_precision": f"Historical civilian-occupation code {data['code']} was recorded at Army entry on {data['entry']}; no employer, school or workplace is named.",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "high_confidence",
            "claim_confidence": "medium",
            "source_quality": "A_direct_official",
            "publication_status": "publish_qualified",
            "research_notes": "The historical category is not converted into a named employer, institution, workplace or exact job title.",
        })
    result.extend([
        {
            "key": "william-suhling-company-b929",
            "person_id": PEOPLE[6][0],
            "organization_key": "suhling-company-b929",
            "organization_name_as_found": "Suhling & Co., Inc.",
            "role_title": "president",
            "occupation": "leaf tobacco packer, dealer and exporter",
            "relationship_type": "employment",
            "start_date": "1939",
            "end_date": "1939",
            "date_precision": "The 1939 VMI register identifies the company and presidency; it does not supply start or separation dates.",
            "city": "Lynchburg",
            "state_or_region": "Virginia",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "high_confidence",
            "claim_confidence": "medium",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "publish_qualified",
            "research_notes": "A named 1939 employer and role, but not established as the immediate predecessor or last civilian employer before OSS service.",
        },
        {
            "key": "yaemitsu-sugimachi-rafu-shimpo-b929",
            "person_id": PEOPLE[2][0],
            "organization_key": "rafu-shimpo-b929",
            "organization_name_as_found": "Rafu Shimpo",
            "role_title": "reporter",
            "occupation": "newspaper reporter",
            "relationship_type": "employment",
            "start_date": "1932",
            "end_date": "1932",
            "date_precision": "The reviewed article identifies him as a Rafu Shimpo reporter in connection with broadcasts beginning in September 1932; exact tenure is not stated.",
            "city": "Los Angeles",
            "state_or_region": "California",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "probable",
            "claim_confidence": "medium",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "publish_qualified",
            "research_notes": "Distinctive exact name and compatible chronology support a probable match; no source proves employment continued through 1942 or immediately preceded the indexed file.",
        },
        {
            "key": "yaemitsu-sugimachi-teacher-b929",
            "person_id": PEOPLE[2][0],
            "occupation": "teacher",
            "relationship_type": "employment",
            "end_date": "1942-04-28",
            "date_precision": "The confinement-site roster records occupation as Teacher when it records arrest on 28 April 1942; no school or employer is named.",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "probable",
            "claim_confidence": "medium",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "publish_qualified",
            "research_notes": "A dated occupation category, not a named school, employer or evidence of OSS service.",
        },
        {
            "key": "orman-suker-field-artillery-ocs-b929",
            "person_id": PEOPLE[10][0],
            "organization_key": "field-artillery-ocs-b929",
            "organization_name_as_found": "72-43 Class Roster",
            "role_title": "officer candidate",
            "occupation": "military officer training",
            "relationship_type": "military_assignment",
            "start_date": "1943-04-15",
            "end_date": "1943-07-07",
            "date_precision": "The roster dates class 72-43 from 15 April to 7 July 1943; a scholarly study identifies Suker as an OSS lieutenant in Bari by 6 October 1944.",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "high_confidence",
            "claim_confidence": "medium",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "publish_qualified",
            "research_notes": "Documented military training before the dated OSS assignment; not a civilian employer and not established as the immediate transfer source.",
        },
    ])
    return result


def army_identity_claim(row: int) -> dict[str, object]:
    name = PEOPLE[row][1]
    data = ARMY_IDENTITIES[row]
    variant = data.get("variant")
    assessment = "High confidence from a nonshared protected identifier and exact full name."
    if variant:
        assessment = "High confidence from a nonshared protected identifier; the expanded middle initial remains visible as a name variant."
    temporal = f"The Army record documents entry on {data['entry']}; it does not by itself establish the OSS transfer date."
    note = "The protected identifier is withheld from public data; no employer is inferred from the Army row."
    if row == 12:
        temporal = "The record dates Army entry to 21 January 1946, after OSS dissolution; it is used for identity classification only and not as pre-OSS evidence."
        note = "The protected identifier is withheld. The post-OSS occupation code is not published as a pre-OSS affiliation."
    return {
        "key": f"identity-{slug(name)}-row{row}-b929",
        "person_id": PEOPLE[row][0],
        "claim_type": "identity",
        "claim_text": f"The indexed {name} row is a high-confidence match to an official Army record dated {data['entry']}.",
        "evidence_paraphrase": "The reviewed Army row agrees through a nonshared protected identifier and an exact or explicitly preserved name variant.",
        "identity_match_assessment": assessment,
        "temporal_assessment": temporal,
        "source_quality": "A_direct_official",
        "claim_confidence": "high",
        "publication_status": "published",
        "match_notes": note,
        "sources": [
            {"source_key": INDEX, "locator_override": f"PDF page 455 row {row}; Box {PEOPLE[row][2]}"},
            {"source_key": ARMY, "locator_override": f"Accepted reviewed identity record; Army entry {data['entry']}; protected identifier withheld"},
            {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46; field definitions"},
        ],
    }


def army_occupation_claim(row: int) -> dict[str, object]:
    name = PEOPLE[row][1]
    data = ARMY_IDENTITIES[row]
    occupation, _relationship, locator = ARMY_OCCUPATIONS[row]
    noun = "historical occupation category"
    qualifier = "no employer or workplace is identified"
    if occupation == "Students":
        noun = "historical status group"
        qualifier = "no school or employer is identified"
    return {
        "key": f"occupation-{slug(name)}-b929",
        "person_id": PEOPLE[row][0],
        "affiliation_key": f"{slug(name)}-occupation-b929",
        "claim_type": "occupation",
        "claim_text": f"At Army entry on {data['entry']}, {name} was recorded in the {noun} {occupation}; {qualifier}.",
        "evidence_excerpt": occupation,
        "evidence_paraphrase": f"The accepted Army record carries civilian-occupation code {data['code']}, decoded from NARA's official code list.",
        "identity_match_assessment": "The category belongs only to the reviewed protected-identifier match; the identifier itself is not public.",
        "temporal_assessment": "Dated to Army entry; it does not establish an immediate pre-OSS affiliation or named employer.",
        "source_quality": "A_direct_official",
        "claim_confidence": "medium",
        "publication_status": "publish_qualified",
        "match_notes": "The historical category is a qualified lead, not a named employer, school, institution, workplace or exact title.",
        "sources": [
            {"source_key": ARMY, "locator_override": f"Accepted reviewed identity record; civilian occupation code {data['code']}; protected identifier withheld"},
            {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46; Army-entry-date and civilian-occupation fields"},
            {"source_key": CODES, "locator_override": locator, "excerpt_override": occupation},
        ],
    }


def claims() -> list[dict[str, object]]:
    result = [army_identity_claim(row) for row in ARMY_IDENTITIES]
    result.extend(army_occupation_claim(row) for row in ARMY_OCCUPATIONS)
    result.extend([
        {
            "key": "identity-mitsue-marie-sugimachi-b929",
            "person_id": PEOPLE[1][0],
            "claim_type": "identity",
            "claim_text": "Mitsue Marie Sugimachi is a probable name expansion for the indexed Mitsue M Sugimachi row.",
            "evidence_excerpt": "Sugimachi, Mitsue Marie",
            "evidence_paraphrase": "A NARA-derived enemy-alien case-file list supplies the same rare name and expands the middle initial to Marie.",
            "identity_match_assessment": "Probable from the rare exact surname and given name plus matching middle initial; no protected identifier or personnel-file bridge was located.",
            "temporal_assessment": "The case-list entry is wartime context, not evidence of an OSS role or pre-OSS employment.",
            "source_quality": "D_correlative_or_secondary",
            "claim_confidence": "medium",
            "publication_status": "publish_qualified",
            "match_notes": "Published only as a qualified name variant. No employer, family relationship or OSS function is inferred.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 455 row 1; Box 756"},
                {"source_key": ENEMY_ALIEN, "locator_override": "Sugimachi, Mitsue Marie; file 15942/2374, box 151"},
            ],
        },
        {
            "key": "identity-yaemitsu-sugimachi-b929",
            "person_id": PEOPLE[2][0],
            "claim_type": "identity",
            "claim_text": "The distinctive indexed Yaemitsu Sugimachi is a probable match to the teacher and former Rafu Shimpo reporter documented in reviewed sources.",
            "evidence_paraphrase": "A municipal-museum confinement roster and a Japanese American National Museum article independently use the rare exact name with compatible prewar chronology.",
            "identity_match_assessment": "Probable, not confirmed: two reputable sources agree on a distinctive exact name, but neither cites the Box 756 personnel file or a protected identifier.",
            "temporal_assessment": "The sources document 1932 reporting and a 1942 teacher occupation; they do not establish an OSS role or entry date.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "medium",
            "publication_status": "publish_qualified",
            "match_notes": "The index establishes only that this name appears in the personnel-file index. Wartime detention evidence prevents any automatic inference that he served as an operative.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 455 row 2; Box 756"},
                {"source_key": ABQ_ROSTER, "locator_override": "Yaemitsu Sugimachi entry; occupation Teacher; arrested 28 April 1942"},
                {"source_key": DISCOVER_NIKKEI, "locator_override": "September 1932 Los Angeles broadcast discussion"},
            ],
        },
        {
            "key": "yaemitsu-rafu-shimpo-b929",
            "person_id": PEOPLE[2][0],
            "affiliation_key": "yaemitsu-sugimachi-rafu-shimpo-b929",
            "claim_type": "other_pre_oss_affiliation",
            "claim_text": "Yaemitsu Sugimachi was a reporter for Rafu Shimpo in connection with a Los Angeles Japanese-language broadcast beginning in September 1932.",
            "evidence_excerpt": "reporter for the Rafu Shimpo",
            "evidence_paraphrase": "The reviewed historical article names Sugimachi Yaemitsu as a Rafu Shimpo reporter and co-host of the 1932 broadcast.",
            "identity_match_assessment": "Probable from the rare exact name and compatible chronology, qualified because no Box-file or protected-identifier bridge was found.",
            "temporal_assessment": "Explicitly documented in 1932; not shown to be the immediate predecessor or last civilian employment before the indexed file.",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "claim_confidence": "medium",
            "publication_status": "publish_qualified",
            "match_notes": "Published as earlier documented employment. Continued employment through 1942 is not inferred.",
            "sources": [{"source_key": DISCOVER_NIKKEI, "locator_override": "September 1932 Los Angeles broadcast discussion"}],
        },
        {
            "key": "yaemitsu-teacher-b929",
            "person_id": PEOPLE[2][0],
            "affiliation_key": "yaemitsu-sugimachi-teacher-b929",
            "claim_type": "occupation",
            "claim_text": "A wartime confinement roster recorded Yaemitsu Sugimachi's occupation as teacher on 28 April 1942; no school or employer is identified.",
            "evidence_excerpt": "Teacher",
            "evidence_paraphrase": "The municipal-museum roster provides a dated occupation field and a rare exact-name match.",
            "identity_match_assessment": "Probable from the distinctive exact name; no protected identifier or Box-file bridge was found.",
            "temporal_assessment": "Dated to 28 April 1942, but no OSS relationship or transition is established.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "medium",
            "publication_status": "publish_qualified",
            "match_notes": "A qualified occupation lead, not a named school, employer or evidence of OSS service.",
            "sources": [{"source_key": ABQ_ROSTER, "locator_override": "Yaemitsu Sugimachi entry; occupation Teacher; arrested 28 April 1942"}],
        },
        {
            "key": "identity-william-gerhard-suhling-jr-b929",
            "person_id": PEOPLE[6][0],
            "claim_type": "identity",
            "claim_text": "The indexed William G Suhling is a high-confidence match to William Gerhard Suhling Jr., documented in a 1939 VMI register and OSS-era official records.",
            "evidence_paraphrase": "The distinctive full-name expansion, VMI class details and an official CIA historical citation to William G. Suhling Jr. align with the indexed name.",
            "identity_match_assessment": "High confidence from a distinctive name, expanded middle name and independent institutional and official wartime sources.",
            "temporal_assessment": "The VMI entry is dated 1939 and the official citation is OSS-era in December 1945.",
            "source_quality": "A_direct_official",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "The VMI company claim remains temporally qualified; neither source proves it was the immediate predecessor to OSS service.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 455 row 6; Box 756"},
                {"source_key": VMI_CATALOG, "locator_override": "1939 institutional register catalog record"},
                {"source_key": VMI_REGISTER, "locator_override": "William Gerhard Suhling, Jr. entry"},
                {"source_key": CIA_SUHLING, "locator_override": "Footnote citing William G. Suhling Jr. to John Magruder, 18 December 1945"},
                {"source_key": CIA_SUHLING_ROLE, "locator_override": "September 1945: Lt. Col. William G. Suhling Jr., deputy of the German Mission"},
            ],
        },
        {
            "key": "william-suhling-company-b929",
            "person_id": PEOPLE[6][0],
            "affiliation_key": "william-suhling-company-b929",
            "claim_type": "other_pre_oss_affiliation",
            "claim_text": "The 1939 VMI register identified William Gerhard Suhling Jr. as president of Suhling & Co., Inc., a Lynchburg leaf-tobacco packing, dealing and exporting company.",
            "evidence_excerpt": "Pres., Suhling & Co., Inc., Leaf Tobacco Packers-Dealers-Exporters",
            "evidence_paraphrase": "The VMI former-cadet entry supplies the company, presidency, trade and city in 1939.",
            "identity_match_assessment": "High-confidence person match from the distinctive expanded name and independent official OSS-era citation.",
            "temporal_assessment": "Explicitly documented in 1939, but no separation date or immediate transition to OSS is stated.",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "claim_confidence": "medium",
            "publication_status": "publish_qualified",
            "match_notes": "Published as other documented pre-OSS employment, not immediate affiliation and not last civilian employment before service.",
            "sources": [
                {"source_key": VMI_REGISTER, "locator_override": "William Gerhard Suhling, Jr. entry"},
                {"source_key": VMI_CATALOG, "support_type": "context_only", "locator_override": "1939 institutional register catalog record"},
                {"source_key": CIA_SUHLING, "support_type": "context_only", "locator_override": "OSS-era name corroboration"},
            ],
        },
        {
            "key": "identity-jacques-suissa-b929",
            "person_id": PEOPLE[8][0],
            "claim_type": "identity",
            "claim_text": "The indexed Jacques Suissa is a high-confidence match to the French Sussex (Proust) network participant documented by a French War Ministry certificate.",
            "evidence_excerpt": "Réseau SUSSEX (PROUST)",
            "evidence_paraphrase": "Certificate no. 77.262 names Jacques Suissa, gives his birth date, mission dates and Sussex network, and records a mission-duration corresponding rank of sous-lieutenant.",
            "identity_match_assessment": "High confidence from the distinctive exact name, official wartime network record and compatible index context.",
            "temporal_assessment": "The certificate documents service from 11 July through 30 September 1944; it does not supply a pre-OSS employer.",
            "source_quality": "A_direct_official",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "Classified as foreign or Allied military personnel and commissioned for the documented mission period; no civilian employment is inferred.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 455 row 8; Box 756"},
                {"source_key": SUISSA_CERT, "locator_override": "Certificate no. 77.262; single page"},
            ],
        },
        {
            "key": "identity-orman-suker-b929",
            "person_id": PEOPLE[10][0],
            "claim_type": "identity",
            "claim_text": "The indexed Orman Suker is a high-confidence match to the Field Artillery OCS graduate later documented as an OSS lieutenant in Bari.",
            "evidence_paraphrase": "A visually checked institutional roster places the rare exact name in class 72-43, while a scholarly study identifies Lt. Orman Suker with the OSS Yugoslav section in 1944.",
            "identity_match_assessment": "High confidence from the rare exact name, dated military chronology and later explicit OSS identification.",
            "temporal_assessment": "OCS ended 7 July 1943; the study documents an OSS assignment by 6 October 1944.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "The sources establish commissioned Army/OSS status but do not identify a civilian employer.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 455 row 10; Box 757"},
                {"source_key": OCS_ROSTER, "locator_override": "PDF physical page 119; continuation of class 72-43"},
                {"source_key": SUKER_STUDY, "locator_override": "Lt. Orman Suker, OSS Yugoslav section in Bari, 6 October 1944"},
            ],
        },
        {
            "key": "orman-suker-field-artillery-ocs-b929",
            "person_id": PEOPLE[10][0],
            "affiliation_key": "orman-suker-field-artillery-ocs-b929",
            "claim_type": "other_pre_oss_affiliation",
            "claim_text": "Orman Suker attended U.S. Army Field Artillery Officer Candidate School class 72-43 from 15 April to 7 July 1943, before his documented 1944 OSS assignment.",
            "evidence_excerpt": "72-43 Class Roster Started April 15, 1943 Graduated July 7, 1943",
            "evidence_paraphrase": "The roster's three-column layout was visually checked: Suker appears in the continuation of class 72-43, not the class 73-43 block beginning mid-page.",
            "identity_match_assessment": "High confidence from the rare exact name and later explicit OSS lieutenant identification.",
            "temporal_assessment": "Documented before the 6 October 1944 OSS assignment, but not shown to be the immediately prior military post.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "medium",
            "publication_status": "publish_qualified",
            "match_notes": "Military training, not civilian employment. The class-number discrepancy was resolved by visual page inspection.",
            "sources": [
                {"source_key": OCS_ROSTER, "locator_override": "PDF physical page 119; continuation of class 72-43"},
                {"source_key": SUKER_STUDY, "support_type": "context_only", "locator_override": "Dated 1944 OSS assignment"},
            ],
        },
    ])
    return result


def archival_update(row: int, reason: str) -> dict[str, object]:
    person_id, name, box = PEOPLE[row]
    return {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, Box {box} and archive location, but staged official, CIA-site, OSS, employment, occupation, obituary, institutional, newspaper, directory and archival searches found no defensible identity bridge. {reason}",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": f"Review Box {box} for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }


def person_updates() -> list[dict[str, object]]:
    updates = [archival_update(row, reason) for row, reason in UNRESOLVED.items()]
    for row, data in ARMY_IDENTITIES.items():
        status = "occupation_only_found" if row in ARMY_OCCUPATIONS else "requires_archival_review"
        evidence = "An exact full name and nonshared protected identifier connect the index row to the official Army record."
        if data.get("variant"):
            evidence = "A nonshared protected identifier connects the index row to an official Army record with the preserved expanded-middle-initial name variant."
        if row == 12:
            evidence += " The 1946 entry is post-OSS and therefore supports identity and personnel classification only."
        update: dict[str, object] = {
            "person_id": PEOPLE[row][0],
            "identity_status": "high_confidence",
            "identity_evidence": evidence,
            "personnel_category": "enlisted_army_personnel",
            "commissioned_officer": False,
            "allied_or_foreign_personnel": False,
            "manual_review_required": True,
            "research_status": status,
            "next_action": f"Review Box {PEOPLE[row][2]} for the immediate pre-OSS affiliation and a named employer, school or institution.",
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
            "archival_review_priority": "high",
        }
        if data.get("variant"):
            update["name_variants"] = [str(data["variant"])]
        updates.append(update)
    updates.extend([
        {
            "person_id": PEOPLE[1][0],
            "identity_status": "probable",
            "identity_evidence": "A NARA-derived enemy-alien case-file list expands the rare exact indexed form to Mitsue Marie Sugimachi, but no protected identifier or personnel-file bridge confirms the match.",
            "name_variants": ["Mitsue Marie Sugimachi"],
            "manual_review_required": True,
            "research_status": "requires_archival_review",
            "next_action": "Review Box 756 to confirm the middle-name expansion, determine why the file was indexed and identify any reliable pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
            "archival_review_priority": "high",
        },
        {
            "person_id": PEOPLE[2][0],
            "identity_status": "probable",
            "identity_evidence": "A municipal-museum roster and Japanese American National Museum article independently document the rare exact name with compatible prewar chronology, but no Box-file or protected-identifier bridge confirms the match.",
            "manual_review_required": True,
            "research_status": "documented_prewar_employer_found",
            "next_action": "Review Box 756 to confirm identity, explain the indexed file and determine whether the 1942 teacher occupation or another affiliation immediately preceded it.",
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
            "archival_review_priority": "critical",
        },
        {
            "person_id": PEOPLE[6][0],
            "identity_status": "high_confidence",
            "identity_evidence": "The distinctive indexed name aligns with William Gerhard Suhling Jr. in a 1939 VMI register and an official CIA historical citation to OSS-era correspondence.",
            "name_variants": ["William Gerhard Suhling Jr."],
            "personnel_category": "commissioned_army_officer",
            "commissioned_officer": True,
            "allied_or_foreign_personnel": False,
            "manual_review_required": True,
            "research_status": "documented_prewar_employer_found",
            "next_action": "Review Box 756 to confirm the exact transition from Suhling & Co., Inc. or any intervening affiliation into wartime service.",
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
            "archival_review_priority": "high",
        },
        {
            "person_id": PEOPLE[8][0],
            "identity_status": "high_confidence",
            "identity_evidence": "A French War Ministry certificate names Jacques Suissa, documents the Sussex (Proust) network and gives detailed 1944 mission dates and rank.",
            "personnel_category": "foreign_or_allied_military_personnel",
            "commissioned_officer": True,
            "allied_or_foreign_personnel": True,
            "manual_review_required": True,
            "research_status": "requires_archival_review",
            "next_action": "Review Box 756 for the immediate pre-mission affiliation and any named civilian employer; the official certificate documents wartime service only.",
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
            "archival_review_priority": "high",
        },
        {
            "person_id": PEOPLE[10][0],
            "identity_status": "high_confidence",
            "identity_evidence": "The rare exact name appears in a visually checked Field Artillery OCS roster and a scholarly source explicitly identifying Lt. Orman Suker with the OSS Yugoslav section in Bari.",
            "personnel_category": "commissioned_army_officer",
            "commissioned_officer": True,
            "allied_or_foreign_personnel": False,
            "manual_review_required": True,
            "research_status": "requires_archival_review",
            "next_action": "Review Box 757 for any intervening Army assignments and the last civilian employer before military service.",
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
            "archival_review_priority": "high",
        },
        {
            **archival_update(23, "Two additional identical John L Sullivan rows immediately follow on the same page; the three source rows remain separate."),
            "identity_status": "ambiguous",
            "identity_evidence": "Three separately printed John L Sullivan rows occur consecutively on page 455 with the same box and no visible identifier. Name and adjacency alone cannot establish duplication.",
            "possible_duplicate_group": duplicate_group("john-l-sullivan-page455-rows23-25"),
            "archival_review_priority": "critical",
            "next_action": "Review all three Box 757 John L Sullivan files together for identifiers, cross-references and duplicate-file evidence before merging or assigning any external biography.",
        },
    ])
    return updates


def research_attempts() -> list[dict[str, object]]:
    attempts: list[dict[str, object]] = []
    source_rows = {row for row in PEOPLE}
    for row in sorted(source_rows):
        person_id, name, box = PEOPLE[row]
        if row in ARMY_IDENTITIES:
            outcome, reviewed, rejected = "source_reviewed", 7, 3
            detail = "A nonshared protected identifier supports a high-confidence Army identity bridge."
            if row in ARMY_OCCUPATIONS:
                detail += " The dated occupation or student category names no employer, school or workplace."
            else:
                detail += " The 1946 record is post-OSS and was not converted into pre-OSS evidence."
        elif row == 1:
            outcome, reviewed, rejected = "candidate_found", 8, 4
            detail = "A probable middle-name expansion was retained, but no employer or personnel-file bridge was found."
        elif row == 2:
            outcome, reviewed, rejected = "source_reviewed", 11, 4
            detail = "Two reputable sources support a probable identity, a 1932 Rafu Shimpo reporting role and a dated 1942 teacher occupation; neither establishes an OSS role or immediate predecessor."
        elif row == 6:
            outcome, reviewed, rejected = "source_reviewed", 10, 3
            detail = "A high-confidence identity and 1939 Suhling & Co. presidency were documented, but no separation date or immediate transition to OSS was found."
        elif row == 8:
            outcome, reviewed, rejected = "source_reviewed", 9, 3
            detail = "A French War Ministry certificate establishes the Sussex network, mission dates and mission-duration rank, but no pre-OSS employer."
        elif row == 10:
            outcome, reviewed, rejected = "source_reviewed", 10, 3
            detail = "Visual review resolved OCS class 72-43 and a scholarly source establishes a later OSS lieutenant assignment; no civilian employer was found."
        elif row == 23:
            outcome, reviewed, rejected = "candidate_found", 7, 5
            detail = "Three identical adjacent rows remain separate and cannot receive a namesake biography until the Box 757 files are jointly reviewed."
        else:
            outcome, reviewed, rejected = "no_result", 6, 4
            detail = UNRESOLVED[row]
        attempts.append({
            "key": f"page455-row{row}-{slug(name)}-b929",
            "person_id": person_id,
            "source_adapter": "manual_staged_protocol",
            "query_text": f"{name}; NARA index and public Archives context; CIA Reading Room site-restricted exact-name discovery; OSS and spelling/transliteration variants; employer and occupation 1940; obituary, institutional, newspaper, Library of Congress and archival searches; Box {box}; protected-identifier Army crosswalk where defensible",
            "query_variant_type": "staged_identity_employment_archival_protocol_batch_929",
            "started_at": "2026-10-27T04:15:00Z",
            "completed_at": "2026-10-27T08:15:00Z",
            "outcome": outcome,
            "sources_reviewed": reviewed,
            "candidate_sources_rejected": rejected,
            "rejection_reasons": "Unbridged namesakes, search snippets, family-only assertions, modern profiles, postwar-only leads and sources without an OSS or Box-file bridge were not assigned. Grouped CIA Reading Room and Library of Congress site-restricted exact-name discovery checks returned no additional person-specific pre-OSS result.",
            "research_notes": f"{detail} The index page and relevant Army or roster pages were visually checked. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA API call was made.",
            "next_action": f"Review Box {box} for corroborating identifiers and the immediate pre-OSS affiliation or last civilian employer.",
            "attempt_number": 1,
            "research_agent_version": "before-oss-b929-v1",
        })
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-929-v1",
        "reviewer": "Before OSS Batch 929 evidence review",
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
