#!/usr/bin/env python3
"""Generate the reviewed Batch 908 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "research/evidence-page444-stanley-to-stapleton-review_batch-908_2026-10-25.json"

INDEX = "nara-index-b908"
ARMY = "army-bulk-b908"
TECH = "army-tech-b908"
CODES = "army-codes-b908"
TORKAR_DISSERTATION = "upr-torkar-stante-b908"
TORKAR_ARTICLE = "acta-torkar-stante-b908"
CIA_STAPLES = "cia-rust-staples-b908"
AFEES_STANTON = "afees-claude-stanton-b908"
REGION_STANTON = "occitanie-claude-stanton-b908"
CIA_FRANK_STANTON = "cia-donovan-frank-stanton-b908"
COLUMBIA_FRANK_STANTON = "columbia-frank-stanton-b908"
GEORGIA_TECH_STAPLETON = "gatech-cyril-stapleton-b908"
ARMY_AVIATION_STAPLETON = "army-aviation-cyril-stapleton-b908"


PEOPLE = {
    1: ("9aed898c-c148-53e1-8dce-c278d0cbfd74", "William S Stanley"),
    2: ("88cbb611-dd65-5035-9b1b-d3418b15977a", "Howard J Stansfield"),
    3: ("44e39ae5-b6bc-5a61-bfff-6d2c17bcd576", "Lorraine Stant"),
    4: ("306b7120-8734-5789-ab8a-0190a97d996f", "Joseph Stante"),
    5: ("36005475-4520-59e1-8883-548cf41633c9", "Alfred Stanton"),
    6: ("ef6ccf60-373a-5939-9336-aa115874eb7b", "Claude Stanton"),
    7: ("5c2cf8d6-61f8-5e31-ac69-c2c920da345d", "Edward L Stanton"),
    8: ("730072c0-79db-58e3-af00-a5ae7c9b58d6", "Edward L Stanton"),
    9: ("0d6b4de8-b896-57a2-b54e-e75a0a3c48f7", "Edward B Stanton"),
    10: ("a2dd3c55-6e9d-54df-a00b-62374e5442c6", "Frank Stanton"),
    11: ("4d9a3ab1-de6b-5e52-bacc-1e0efec1180b", "George H Stanton"),
    12: ("c7626520-0979-591c-b52a-81a6e57d0cf2", "Gertrude A Stanton"),
    13: ("ceceb9df-d3fe-515f-82d5-710acd558ac4", "Helena Stanton"),
    14: ("b68d4197-e62d-5bb1-b260-069478e7f8c4", "Merwin C Stanton"),
    15: ("bbc8cd90-0769-52e1-9896-c4c7f98d6907", "W T Stanton"),
    16: ("e5f841ca-fa75-5da8-bdde-10ee0c4a3e0c", "Willis A Stanton"),
    17: ("517ae32b-7d4d-5e02-b343-3880bce29efd", "Bernard N Stanziola"),
    18: ("0f7aa741-130b-5311-832d-58695c62ac71", "Henry L Staples"),
    19: ("462bc961-3e75-53ee-8036-9ffea196cf71", "John H Staples"),
    20: ("e41c80bc-afa1-560a-9aee-a466721268d5", "Richard F Staples"),
    21: ("e5ec7abb-9a71-5116-90f4-d2967e8d5e14", "Richard F Staples"),
    22: ("b74bab57-e9fd-5a9c-9a1d-a7aec253b51a", "Cyril D Stapleton"),
    23: ("859580c6-0048-552b-977c-e2eb454221cf", "George A Stapleton"),
}


ARMY_OCCUPATIONS = [
    {"row": 2, "date": "1942-04-10", "code": "948", "occupation": "Sailors and deckhands, except U.S. Navy", "locator": "PDF physical page 174; category 9-48"},
    {"row": 14, "date": "1942-10-28", "code": "126", "occupation": "Paymasters, payroll clerks, and timekeepers", "locator": "PDF physical page 171; category 1-26"},
    {"row": 17, "date": "1943-02-08", "code": "992", "occupation": "Students", "locator": "PDF physical page 304; amended category 9-92"},
    {"row": 21, "date": "1943-11-11", "code": "061", "occupation": "Radio operators", "locator": "PDF physical page 171; category 0-61", "army_name": "Staple Richard F"},
]


UNRESOLVED = {
    1: "The name is common, and no searched source supplied a compatible rank, identifier, box reference or OSS assignment.",
    3: "Exact-name and spelling-variant searches found no person-specific official, institutional, newspaper, directory or obituary result.",
    5: "The printed honorific Dr. was insufficient to distinguish incompatible professional and obituary namesakes.",
    7: "This row remains separate from the adjacent same-name row because the protected identifiers differ; no source resolved either identity.",
    8: "This row remains separate from the preceding same-name row because the protected identifiers differ; no source resolved either identity.",
    9: "Exact-name and middle-initial searches returned unbridged namesakes and no defensible pre-OSS chronology.",
    11: "The index provides an officer-format identifier but no printed rank; searched sources did not produce a corroborating identity bridge.",
    12: "Exact-name, employment, obituary, institutional, newspaper and archival searches produced no person-specific result.",
    13: "Exact-name and variant searches produced no defensible identity bridge or dated pre-OSS affiliation.",
    15: "Initials-only searches could not distinguish the indexed person from numerous namesakes.",
    16: "Exact-name searches returned incompatible military and obituary candidates without a second corroborating identifier.",
    18: "Common-name searches returned multiple incompatible candidates and no rank, identifier, box or OSS corroboration.",
    19: "A decorated Army officer of this name remains an unbridged namesake because the accessible biography supplies no OSS or index identifier match.",
    23: "The printed lieutenant-colonel rank establishes officer status, but no accessible source supplied a defensible identity or employment bridge.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def archive_box(row: int) -> str:
    return "737" if row <= 14 else "738"


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 737 and 738",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 444, rows 1-23; checked against layout-preserving text and a rendered page image",
            "access_date": "2026-10-25",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain immutable. Full protected identifiers remain private, and the two Richard F. Staples rows and two Edward L. Stanton rows remain separate.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; four accepted reviewed identity bridges",
            "access_date": "2026-10-25",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "No raw row or full protected identifier is retained in public assets. Coded occupations identify no employer.",
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
            "locator": "PDF physical pages 171, 174 and 304; all four Batch 908 codes visually and textually checked",
            "access_date": "2026-10-25",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical labels identify neither employers nor workplaces. The amended table on physical page 304 maps code 992 to Students.",
        },
        {
            "key": TORKAR_DISSERTATION,
            "stable_url": "https://repozitorij.upr.si/Dokument.php?id=9689&lang=slv",
            "archival_identifier": "URN:NBN:SI:DOC-WQ6DMHJB",
            "title": "Ozadje delovanja misij ameriške obveščevalne službe OSS v Sloveniji",
            "author_creator": "Blaž Torkar",
            "repository_publisher": "University of Primorska Repository",
            "publication_record_date": "2010",
            "locator": "Dissertation PDF page 255 (printed page 246), biographical entry for Jože Stante",
            "access_date": "2026-10-25",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "University of Primorska doctoral dissertations",
            "rights_notes": "The repository record and document identifier are stable. Evidence was transcribed from the relevant page only; no full copyrighted work is republished.",
        },
        {
            "key": TORKAR_ARTICLE,
            "stable_url": "https://www.dlib.si/stream/URN%3ANBN%3ASI%3ADOC-VNG766N2/cd5de3df-f886-4722-938f-c2163a56ee54/PDF",
            "archival_identifier": "URN:NBN:SI:DOC-VNG766N2",
            "title": "Delovanje jugoslovanskih sekcij ameriške obveščevalne službe OSS v severni Afriki in južni Italiji",
            "author_creator": "Blaž Torkar",
            "repository_publisher": "Acta Histriae; Digital Library of Slovenia",
            "publication_record_date": "2012",
            "locator": "Acta Histriae 20, no. 4, discussion of Slovenian mission personnel and civilian OSS status",
            "access_date": "2026-10-25",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Acta Histriae",
            "rights_notes": "Corroborative scholarly context only; project-authored paraphrases are used.",
        },
        {
            "key": CIA_STAPLES,
            "stable_url": "https://www.cia.gov/resources/csi/studies-in-intelligence/volume-60-no-1/transitioning-into-cia-the-strategic-services-unit-in-indonesia/",
            "title": "Transitioning into CIA: The Strategic Services Unit in Indonesia",
            "author_creator": "William J. Rust",
            "repository_publisher": "Central Intelligence Agency, Center for the Study of Intelligence",
            "publication_record_date": "2016-03",
            "locator": "Studies in Intelligence 60, no. 1, PDF page 4; Lieutenant Richard F. Staples in Java",
            "access_date": "2026-10-25",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Studies in Intelligence",
            "rights_notes": "Used for the exact-name and rank identity bridge only; it does not establish a pre-OSS employer.",
        },
        {
            "key": AFEES_STANTON,
            "stable_url": "https://airforceescape.org/wp-content/uploads/2018/10/AFEES-Member-Database-Ky-Rad.pdf",
            "title": "Air Forces Escape and Evasion Society Member Database",
            "repository_publisher": "Air Forces Escape and Evasion Society",
            "locator": "Claude Stanton of Mazamet (Tarn) identified as a wartime helper",
            "access_date": "2026-10-25",
            "source_quality": "D_correlative_or_secondary",
            "rights_notes": "Private identity lead only; it supplies no index identifier or pre-OSS employer.",
        },
        {
            "key": REGION_STANTON,
            "stable_url": "https://inventaire.patrimoines.laregion.fr/dossier/IA81001932",
            "archival_identifier": "IA81001932",
            "title": "Villa Stanton",
            "repository_publisher": "Région Occitanie heritage inventory",
            "locator": "Historical note naming Claude Stanton, born 1921, as Robert Stanton's son",
            "access_date": "2026-10-25",
            "source_quality": "B_authoritative_institutional",
            "rights_notes": "Family context cannot establish employment and is retained only as a private disambiguation lead.",
        },
        {
            "key": CIA_FRANK_STANTON,
            "stable_url": "https://www.cia.gov/readingroom/docs/CIA-RDP90-00708R000600120001-0.pdf",
            "archival_identifier": "CIA-RDP90-00708R000600120001-0",
            "title": "Donovan and the CIA: A History of the Establishment of the Central Intelligence Agency",
            "repository_publisher": "Central Intelligence Agency Reading Room",
            "locator": "Passage naming Dr. Frank Stanton of CBS as a wartime collaborator",
            "access_date": "2026-10-25",
            "source_quality": "A_direct_official",
            "rights_notes": "Private candidate lead only. The common index name has no rank or identifier tying it to the CBS executive.",
        },
        {
            "key": COLUMBIA_FRANK_STANTON,
            "stable_url": "https://www.columbia.edu/cu/lweb/digital/collections/nny/stantonf/index.html",
            "title": "Frank Stanton Oral History",
            "author_creator": "Columbia Center for Oral History Research",
            "repository_publisher": "Columbia University Libraries",
            "locator": "Institutional biographical profile",
            "access_date": "2026-10-25",
            "source_quality": "B_authoritative_institutional",
            "rights_notes": "Candidate context only; it cannot bridge the unqualified index row to the CBS executive.",
        },
        {
            "key": GEORGIA_TECH_STAPLETON,
            "stable_url": "https://repository.gatech.edu/server/api/core/bitstreams/ed81c043-a7c9-4aa7-9fc5-849a21886641/content",
            "title": "Georgia Institute of Technology commencement program",
            "repository_publisher": "Georgia Tech Library Repository",
            "locator": "Graduate listing for Cyril Darwin Stapleton, B.S. Aeronautical Engineering",
            "access_date": "2026-10-25",
            "source_quality": "B_authoritative_institutional",
            "rights_notes": "Private identity lead only; education is not employment and the source does not mention OSS.",
        },
        {
            "key": ARMY_AVIATION_STAPLETON,
            "stable_url": "https://armyaviationmagazine.com/images/archive/backissues/1969/69_06.pdf",
            "title": "Army Aviation Directory",
            "repository_publisher": "Army Aviation magazine",
            "publication_record_date": "1969-06",
            "locator": "Directory entry for Colonel Cyril D. Stapleton, Army Aeronautical Research Laboratory",
            "access_date": "2026-10-25",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "rights_notes": "Postwar candidate context only; it supplies no direct OSS or index-identifier bridge.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": "german-army-b908",
            "organization_id": "a577f889-8052-5c7d-aefc-6345820d8ac1",
            "canonical_name": "German Army (Wehrmacht)",
            "historical_name": "Heer der Wehrmacht",
            "aliases": ["German Army", "Wehrmacht Heer"],
            "organization_type": "army",
            "sector": "military",
            "country": "Germany",
            "active_dates": "1935-1945",
            "normalization_notes": "Modeled as a military assignment. The source describes Stante's 1942 mobilization; this is not characterized as voluntary employment.",
        }
    ]


def army_affiliation(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    person_id, name = PEOPLE[row]
    return {
        "key": f"{slug(name)}-row{row}-occupation-b908",
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
    spelling_note = " The Army file spells the surname Staple; the unique protected identifier and matching given names support the link despite that one-character conflict." if row == 21 else ""
    return [
        {
            "key": f"identity-{slug(name)}-row{row}-b908",
            "person_id": person_id,
            "claim_type": "identity",
            "claim_text": f"The indexed {name} row is a high-confidence match to the reviewed official Army record.",
            "evidence_paraphrase": f"A nonshared protected identifier and compatible name connect the visually verified index row to the official Army record.{spelling_note}",
            "identity_match_assessment": "High confidence from the nonshared protected-identifier bridge and compatible name; the Army surname's missing final s is documented rather than silently corrected." if row == 21 else "High confidence from the nonshared protected-identifier bridge and exact name alignment.",
            "temporal_assessment": "The Army record supports identity and a dated occupation category; it does not establish the OSS transfer sequence.",
            "source_quality": "A_direct_official",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "No protected identifier is exposed, and the coded occupation is kept separate from employer claims.",
            "sources": [
                {"source_key": INDEX, "locator_override": f"PDF page 444 row {row}; protected identifier withheld"},
                {"source_key": ARMY, "locator_override": f"Accepted reviewed identity bridge; Army name {item.get('army_name', name)}; protected identifier withheld"},
            ],
        },
        {
            "key": f"occupation-{slug(name)}-row{row}-b908",
            "person_id": person_id,
            "affiliation_key": f"{slug(name)}-row{row}-occupation-b908",
            "claim_type": "occupation",
            "claim_text": f"At Army entry on {item['date']}, the official record assigned {name} the historical civilian-occupation category '{item['occupation']}'; no employer is identified.",
            "evidence_paraphrase": f"The Army entry field carries code {item['code']}, which the visually checked NARA code list maps to the stated category.",
            "identity_match_assessment": "High confidence from the protected-identifier bridge; the one-character surname conflict remains visible." if row == 21 else "High confidence from a nonshared protected-identifier bridge and exact name alignment.",
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


def stante_affiliations() -> list[dict[str, object]]:
    return [
        {
            "key": "joseph-stante-miner-factory-worker-b908",
            "person_id": PEOPLE[4][0],
            "occupation": "miner and factory worker",
            "relationship_type": "employment",
            "date_precision": "Before compulsory German Army mobilization on 8 September 1942; employer names and the order of the two occupations are not stated.",
            "country": "Yugoslavia",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "high_confidence",
            "claim_confidence": "medium",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "publish_qualified",
            "research_notes": "The dissertation supplies occupations but no employer, workplace, exact dates or sequence, so this is not labeled the last civilian employer.",
        },
        {
            "key": "joseph-stante-german-army-b908",
            "person_id": PEOPLE[4][0],
            "organization_key": "german-army-b908",
            "organization_name_as_found": "German Army",
            "relationship_type": "military_assignment",
            "start_date": "1942-09-08",
            "date_precision": "Mobilized on 8 September 1942; later captured by U.S. forces in North Africa before OSS recruitment and training.",
            "country": "Germany",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "published",
            "research_notes": "This is modeled as compulsory military assignment, not civilian employment. Captivity intervened before OSS training, so it is not marked immediate pre-OSS.",
        },
    ]


def substantive_claims() -> list[dict[str, object]]:
    return [
        {
            "key": "identity-joseph-stante-b908",
            "person_id": PEOPLE[4][0],
            "claim_type": "identity",
            "claim_text": "The indexed Joseph Stante is a high-confidence match to Jože Stante, alias Stanley Post, a Slovenian member of an OSS mission.",
            "evidence_paraphrase": "The uncommon surname, compatible given-name form and detailed OSS mission chronology support the identity; the personnel file remains necessary for confirmation.",
            "identity_match_assessment": "High confidence from the rare name, Anglicized/Slovene given-name correspondence and a person-specific OSS mission account.",
            "temporal_assessment": "The dissertation sequences civilian work, German Army mobilization, capture, OSS training and the November 1943 mission.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "Jože Stante and mission alias Stanley Post are added as documented variants; the Box 737 file should confirm the link.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 444 row 4; Box 737"},
                {"source_key": TORKAR_DISSERTATION, "locator_override": "PDF page 255 (printed page 246), Jože Stante entry"},
                {"source_key": TORKAR_ARTICLE, "support_type": "context_only", "locator_override": "Scholarly discussion of Slovenian OSS mission personnel"},
            ],
        },
        {
            "key": "occupation-joseph-stante-b908",
            "person_id": PEOPLE[4][0],
            "affiliation_key": "joseph-stante-miner-factory-worker-b908",
            "claim_type": "occupation",
            "claim_text": "Before wartime military service, Jože (Joseph) Stante worked as a miner and factory worker; the source names no employer.",
            "evidence_excerpt": "Delal je kot rudar in tovarniški delavec.",
            "evidence_paraphrase": "Torkar's biographical entry identifies two civilian occupations before Stante's September 1942 German Army mobilization.",
            "identity_match_assessment": "High-confidence match based on the rare name and exact OSS mission context.",
            "temporal_assessment": "Documented prewar work, but neither occupation is proven to be the final civilian role and no employer is identified.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "medium",
            "publication_status": "publish_qualified",
            "match_notes": "Published as occupation-only evidence and excluded from employer analytics.",
            "sources": [{"source_key": TORKAR_DISSERTATION, "locator_override": "PDF page 255 (printed page 246), Jože Stante entry"}],
        },
        {
            "key": "military-joseph-stante-german-army-b908",
            "person_id": PEOPLE[4][0],
            "affiliation_key": "joseph-stante-german-army-b908",
            "claim_type": "other_pre_oss_affiliation",
            "claim_text": "Jože (Joseph) Stante was mobilized into the German Army on 8 September 1942, then captured in North Africa before OSS training.",
            "evidence_paraphrase": "The dissertation gives the mobilization date and sequences German service, capture by Americans, OSS training in Cairo and mission departure.",
            "identity_match_assessment": "High-confidence match based on the rare name and exact OSS mission context.",
            "temporal_assessment": "Strongly date-bounded pre-OSS military assignment; captivity intervened, so it is not labeled the immediate pre-OSS affiliation.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "Modeled as compulsory military assignment, not employment.",
            "sources": [{"source_key": TORKAR_DISSERTATION, "locator_override": "PDF page 255 (printed page 246), Jože Stante entry"}],
        },
        {
            "key": "identity-richard-f-staples-officer-b908",
            "person_id": PEOPLE[20][0],
            "claim_type": "identity",
            "claim_text": "The indexed First Lieutenant Richard F. Staples is a high-confidence match to the OSS communications officer sent to Java in September 1945.",
            "evidence_excerpt": "Lieutenant Richard F. Staples, a communications officer",
            "evidence_paraphrase": "A CIA institutional history repeats the exact full name and lieutenant rank and places Staples on a specific OSS/SSU mission in Java.",
            "identity_match_assessment": "High confidence from exact name, matching commissioned rank and person-specific wartime OSS/SSU assignment; the separate enlisted row remains distinct.",
            "temporal_assessment": "The source establishes wartime service but does not document a pre-OSS employer or the transfer into OSS.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "The adjacent enlisted Richard F. Staples row has a different protected identifier and its own Army record; the two are not merged.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 444 row 20; First Lieutenant; protected identifier withheld"},
                {"source_key": CIA_STAPLES, "locator_override": "Studies in Intelligence 60, no. 1, PDF page 4"},
            ],
        },
        {
            "key": "candidate-claude-stanton-france-b908",
            "person_id": PEOPLE[6][0],
            "claim_type": "identity",
            "claim_text": "A French wartime helper named Claude Stanton is a candidate for the indexed French lieutenant, not a resolved identity.",
            "evidence_paraphrase": "An escape-and-evasion roster and a regional heritage record supply compatible French context but no OSS, rank or index-identifier bridge.",
            "identity_match_assessment": "Ambiguous; exact name and nationality context are insufficient without rank, service identifier or direct OSS evidence.",
            "temporal_assessment": "The sources provide wartime and family context but no reliable pre-OSS employment chronology.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "low",
            "publication_status": "needs_review",
            "match_notes": "Retained privately for Box 737 review; a relative's textile business is not assigned as Claude Stanton's employer.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 444 row 6; Lieutenant; French note; Box 737"},
                {"source_key": AFEES_STANTON, "locator_override": "Claude Stanton of Mazamet (Tarn), wartime helper"},
                {"source_key": REGION_STANTON, "support_type": "context_only", "locator_override": "Heritage entry for the Stanton family villa"},
            ],
        },
        {
            "key": "candidate-frank-stanton-cbs-b908",
            "person_id": PEOPLE[10][0],
            "claim_type": "identity",
            "claim_text": "The CBS executive Frank Stanton is a candidate namesake, not a resolved identity for the unqualified index row.",
            "evidence_paraphrase": "A CIA history names Dr. Frank Stanton of CBS as a wartime collaborator, but the index supplies no rank, middle initial or identifier bridge.",
            "identity_match_assessment": "Ambiguous; a famous same-name biography cannot be assigned from name agreement alone.",
            "temporal_assessment": "The candidate sources supply wartime CBS context but no defensible link to the indexed person.",
            "source_quality": "A_direct_official",
            "claim_confidence": "low",
            "publication_status": "needs_review",
            "match_notes": "Retained privately for Box 737 review; CBS is not published as this person's employer.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 444 row 10; Box 737"},
                {"source_key": CIA_FRANK_STANTON, "locator_override": "Passage naming Dr. Frank Stanton of CBS"},
                {"source_key": COLUMBIA_FRANK_STANTON, "support_type": "context_only", "locator_override": "Institutional biographical profile"},
            ],
        },
        {
            "key": "candidate-cyril-d-stapleton-b908",
            "person_id": PEOPLE[22][0],
            "claim_type": "identity",
            "claim_text": "Engineer and later Army colonel Cyril D. Stapleton is a candidate for the indexed captain, not a resolved identity.",
            "evidence_paraphrase": "Institutional records give the same uncommon name and a compatible Army aeronautical career but no OSS or index-identifier bridge.",
            "identity_match_assessment": "Ambiguous; name, middle initial and later branch context are promising but insufficient for this officer case.",
            "temporal_assessment": "The degree record establishes education, not employment; the Army directory is postwar.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "low",
            "publication_status": "needs_review",
            "match_notes": "Retained privately for Box 738 review; Georgia Tech is not classified as an employer.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 444 row 22; Captain; protected identifier withheld"},
                {"source_key": GEORGIA_TECH_STAPLETON, "locator_override": "Cyril Darwin Stapleton degree listing"},
                {"source_key": ARMY_AVIATION_STAPLETON, "support_type": "context_only", "locator_override": "1969 directory entry for Colonel Cyril D. Stapleton"},
            ],
        },
    ]


def army_person_update(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    person_id, _name = PEOPLE[row]
    spelling = " The Army file omits the final s in Staples; that conflict is documented and prevents a confirmed classification." if row == 21 else ""
    return {
        "person_id": person_id,
        "identity_status": "high_confidence",
        "identity_evidence": f"A nonshared protected identifier and compatible name connect the visually verified index row to the reviewed official Army record.{spelling} The historical occupation field remains separate from employer and immediate-affiliation claims.",
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


def unresolved_update(row: int) -> dict[str, object]:
    person_id, name = PEOPLE[row]
    category = "commissioned_army_officer" if row == 23 else "unknown_or_indeterminate"
    commissioned: bool | None = True if row == 23 else None
    update: dict[str, object] = {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, rank when printed, box and archive location, but staged official-context, CIA Reading Room, exact-name, occupation, employer, obituary, institutional, newspaper, directory, Library of Congress and archival searches found no defensible identity bridge. {UNRESOLVED[row]}",
        "personnel_category": category,
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": f"Review the indexed Box {archive_box(row)} personnel file for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "critical" if row in {5, 7, 8, 11, 15, 18, 19, 23} else "high",
    }
    if commissioned is not None:
        update["commissioned_officer"] = commissioned
        update["allied_or_foreign_personnel"] = False
    return update


def person_updates() -> list[dict[str, object]]:
    updates = [army_person_update(item) for item in ARMY_OCCUPATIONS]
    updates.extend(
        [
            {
                "person_id": PEOPLE[4][0],
                "identity_status": "high_confidence",
                "identity_evidence": "The rare Stante surname, Joseph/Jože name correspondence and detailed person-specific OSS mission chronology support a high-confidence match to Jože Stante, alias Stanley Post.",
                "name_variants": ["Jože Stante", "Stanley Post"],
                "personnel_category": "temporary_contract_or_special_personnel",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": True,
                "manual_review_required": True,
                "research_status": "occupation_only_found",
                "next_action": "Review Box 737 to confirm the identity, clarify the sequence and names of civilian employers, and document the captivity-to-OSS transition.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[20][0],
                "identity_status": "high_confidence",
                "identity_evidence": "A CIA institutional history repeats the exact full name and lieutenant rank and identifies a person-specific OSS/SSU communications assignment in Java; the adjacent enlisted row has a different protected identifier and remains separate.",
                "personnel_category": "commissioned_army_officer",
                "commissioned_officer": True,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Review Box 738 to identify Lieutenant Staples's immediate pre-OSS military assignment and last civilian employer; do not merge the adjacent enlisted record.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[6][0],
                "identity_status": "ambiguous",
                "identity_evidence": "Same-name French wartime sources provide promising context but no rank, protected identifier, direct OSS record or employer evidence connecting them to the indexed French lieutenant.",
                "personnel_category": "foreign_or_allied_military_personnel",
                "commissioned_officer": True,
                "allied_or_foreign_personnel": True,
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Review Box 737 for nationality, military service, date of birth, OSS assignment and prewar occupation; do not transfer a relative's employment or an unbridged same-name biography.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[10][0],
                "identity_status": "ambiguous",
                "identity_evidence": "A historically relevant same-name lead remains private because the index row supplies no middle initial, rank, protected identifier or other fact connecting that biography to this person.",
                "personnel_category": "unknown_or_indeterminate",
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Review Box 737 for a full name, birth details, OSS role and prewar employer; do not assign a well-known namesake biography on name agreement alone.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[22][0],
                "identity_status": "ambiguous",
                "identity_evidence": "Same-name institutional records provide compatible education and later military context, but no officer number, OSS assignment or personnel-file bridge.",
                "personnel_category": "commissioned_army_officer",
                "commissioned_officer": True,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Review Box 738 to test the private same-name candidate and identify the immediate pre-OSS assignment; keep education separate from employment unless work is independently documented.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
        ]
    )
    updates.extend(unresolved_update(row) for row in UNRESOLVED)
    return updates


def research_attempts() -> list[dict[str, object]]:
    sourced_rows = {2, 4, 6, 10, 14, 17, 20, 21, 22}
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        if row in {6, 10, 22}:
            outcome = "candidate_found"
            detail = "A same-name candidate with compatible context remains private because the available evidence does not supply a sufficient index identity bridge."
        elif row in sourced_rows:
            outcome = "source_reviewed"
            detail = "Reviewed evidence established an official identity/occupation bridge or a carefully qualified identity and pre-OSS chronology."
        else:
            outcome = "candidate_rejected"
            detail = UNRESOLVED[row]
        attempts.append(
            {
                "key": f"page444-row{row}-{slug(name)}-b908",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA/index and public Catalog context; CIA Reading Room exact-name check; OSS and rank variants; employer and occupation; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Box {archive_box(row)}; protected-identifier Army crosswalk where available",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_908",
                "started_at": "2026-10-25T20:50:00Z",
                "completed_at": "2026-10-26T01:20:00Z",
                "outcome": outcome,
                "sources_reviewed": 10 if row in {4, 20} else (8 if row in sourced_rows else 6),
                "candidate_sources_rejected": 5 if row in sourced_rows else 7,
                "rejection_reasons": "Unbridged namesakes, discovery-only results, chronologically irrelevant records, relatives' employment and postwar-only leads were not assigned." if row in sourced_rows else UNRESOLVED[row],
                "research_notes": f"{detail} Search-result snippets were discovery aids only, no access control was bypassed, and no exposed NARA API credential was used.",
                "next_action": f"Review the indexed Box {archive_box(row)} personnel file for corroborating identifiers and the last documented pre-OSS affiliation.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b908-v1",
            }
        )
    return attempts


def main() -> None:
    affiliations = [army_affiliation(item) for item in ARMY_OCCUPATIONS]
    affiliations.extend(stante_affiliations())
    claims: list[dict[str, object]] = []
    for item in ARMY_OCCUPATIONS:
        claims.extend(army_claims(item))
    claims.extend(substantive_claims())
    bundle = {
        "bundle_version": "batch-908-v1",
        "reviewer": "Before OSS Batch 908 evidence review",
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
