#!/usr/bin/env python3
"""Generate the reviewed Batch 905 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "research/evidence-page442-squillacioti-to-st-sauveur-review_batch-905_2026-10-25.json"

INDEX = "nara-index-b905"
ARMY = "army-bulk-b905"
TECH = "army-tech-b905"
CODES = "army-codes-b905"
APUS = "apus-aaron-squires-b905"
NPS = "nps-aaron-squires-b905"
CMU = "cmu-anonda-srivardhana-b905"
CAMBRIDGE = "cambridge-free-thai-b905"
CIA_THAI = "cia-free-thai-b905"


PEOPLE = {
    24: ("bc08ab60-1f86-5122-81dd-eeb3c5ec4cc7", "Phillip I Squillacioti"),
    25: ("20b2395a-763a-5af4-b883-a3706d91ec7f", "Emerson T Squire"),
    26: ("5f455f1d-7dda-53a6-9752-6321d305ed9f", "Loren D Squire"),
    27: ("329e3c54-16ab-5811-bbe7-968bc959039b", "Aaron Squires"),
    28: ("ca2acceb-bbbd-5a88-b6ab-e634031ffeac", "Emerson Squires"),
    29: ("8d5414b6-2613-5a7f-a186-7b99db380802", "Roy W Squires"),
    30: ("ac5a7cd5-3bd0-52ca-940f-f8a3a082e2da", "Joseph T Sranova"),
    31: ("ee345694-fb4f-514b-948c-ce155de19d9f", "Anonda Srivardhana"),
    32: ("09b75d60-426c-5791-b9ff-6da5e5c15729", "Karawek Srivicharn"),
    33: ("91af211a-42ce-51ff-a200-80a2851aea05", "Philemon A St. Amant"),
    34: ("522e731e-4043-5cf9-9ad9-9f6047976f8d", "Alice E St. Clair"),
    35: ("613d537b-f9a6-5dae-9a5c-baf52c014968", "James T St. Clair"),
    36: ("15ee567b-7398-5018-9ef6-71101a57e7cd", "Rodman A St. Clair"),
    37: ("cd7dcd2b-b166-5ce2-97f0-b36f09585d73", "Joseph R St. Gelais"),
    38: ("d85572a8-0a71-50f4-a847-8602b3463c55", "Laurent M St. Georges"),
    39: ("f36e01b2-1d6c-5814-b067-103f9ea9512a", "Lawrence S St. Jean"),
    40: ("09f2177d-1c37-5d8b-b236-1dc3ba175b1a", "Wilfred T St. Laurence"),
    41: ("d1a8fa3a-f5e3-57db-a76b-31c97f044a17", "Antonio L St. Laurent"),
    42: ("e56f66cd-9fe3-5322-926b-a103a02141cf", "Ramond P St. Laurent"),
    43: ("1c21abe6-b6e6-599c-ba12-57d6d0e007ae", "Albert J St. Michel"),
    44: ("50dc58a1-51f3-5532-a8ef-c7b0d6f85894", "Ivan B St. Onge"),
    45: ("51dd54e1-a3d7-5976-acf5-4e9d09e836c5", "Wallace J St. Pierre"),
    46: ("7e87391c-bc9d-5311-9151-a0a31793b7ba", "Pierre G St. Sauveur"),
}


ARMY_OCCUPATIONS = [
    {"row": 24, "date": "1942-09-04", "code": "091", "occupation": "Purchasing agents and buyers, not elsewhere classified", "locator": "PDF physical pages 170-173; category 0-91"},
    {"row": 25, "date": "1942-04-09", "code": "027", "occupation": "Social and welfare workers", "locator": "PDF physical pages 170-173; category 0-27"},
    {"row": 27, "date": "1941-01-13", "code": "056", "occupation": "Photographers", "locator": "PDF physical pages 170-173; category 0-56"},
    {"row": 30, "date": "1942-01-20", "code": "819", "occupation": "Unskilled occupations in manufacture of textiles, not elsewhere classified", "locator": "PDF physical pages 170-173; category 8-19"},
    {"row": 41, "date": "1942-11-03", "code": "678", "occupation": "Semiskilled machine-shop and related occupations, not elsewhere classified", "locator": "PDF physical pages 170-173; category 6-78"},
    {"row": 43, "date": "1941-02-24", "code": "819", "occupation": "Unskilled occupations in manufacture of textiles, not elsewhere classified", "locator": "PDF physical pages 170-173; category 8-19"},
    {"row": 46, "date": "1943-04-23", "code": "819", "occupation": "Unskilled occupations in manufacture of textiles, not elsewhere classified", "locator": "PDF physical pages 170-173; category 8-19"},
]

ARMY_IDENTITY_ONLY = [
    {"row": 40, "army_name": "St Lawrence Wilfred T", "date": "1946-03-20", "note": "The Army spelling Lawrence differs from the index spelling Laurence, and the 1946 record is post-OSS; no occupation is transferred."},
    {"row": 44, "army_name": "Ivan B St. Onge", "date": "1941-05-07", "note": "The historical occupation value is not safely decoded in the applicable NARA table; no occupation or employer is published."},
    {"row": 45, "army_name": "St IERRE Wallace J", "date": "1945-11-20", "note": "The source name is visibly damaged and the Army-entry date is after OSS dissolution; no occupation is transferred."},
]

UNRESOLVED = {
    26: "Exact-name and variant searches did not establish a defensible identity bridge or pre-OSS affiliation for Loren D Squire.",
    28: "The M/Sgt Emerson Squires row cannot be merged with Emerson T Squire: the name form and rank differ, and only the latter has a nonshared official identifier bridge.",
    29: "Common-name results did not supply two corroborating identifiers for Lieutenant Roy W Squires.",
    33: "Exact-name, obituary, institutional, newspaper and archival searches did not identify Philemon A St. Amant or a dated pre-OSS affiliation.",
    35: "Common-name results did not establish which Captain James T St. Clair is represented.",
    36: "Exact-name and rank-focused searches did not produce a defensible identity bridge for Lieutenant Colonel Rodman A St. Clair.",
    37: "Exact-name and spelling-variant searches did not identify Joseph R St. Gelais or a dated pre-OSS affiliation.",
    38: "Exact-name, institutional and archival searches did not establish Laurent M St. Georges' identity or chronology.",
    39: "Exact-name and occupation/employer searches did not distinguish the indexed Lawrence S St. Jean from namesakes.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 734, 735 and 752",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 442, rows 24-46; checked against layout-preserving text and a rendered page image",
            "access_date": "2026-10-25",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain immutable. Full protected identifiers remain private.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; ten accepted and two conflicting reviewed identity bridges",
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
            "locator": "PDF physical pages 170-173; categories 027, 056, 091, 678 and 819 visually checked",
            "access_date": "2026-10-25",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical labels identify neither employers nor workplaces; uninterpretable or post-OSS values are not used as public occupation claims.",
        },
        {
            "key": APUS,
            "stable_url": "https://www.apus.edu/docs/apus/-/journals/saber-and-scroll-historical-journal/sands-09-03.pdf",
            "title": "The Saber and Scroll Journal, Volume 9, Number 3",
            "author_creator": "Policy Studies Organization and American Public University System",
            "repository_publisher": "American Public University System",
            "publication_record_date": "Winter 2020",
            "locator": "Article 'Into the Maelstrom: America and Vietnam, 1945-1956,' PDF printed page 153; Deer Team photograph caption",
            "access_date": "2026-10-25",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "rights_notes": "Project-authored paraphrase only; the exact-name caption is used as identity context, not pre-OSS employment evidence.",
        },
        {
            "key": NPS,
            "stable_url": "https://home.nps.gov/articles/oss-in-action-the-pacific-and-the-far-east.htm",
            "title": "OSS in Action: The Pacific and the Far East",
            "author_creator": "John Whiteclay Chambers II",
            "repository_publisher": "National Park Service",
            "locator": "Ho Chi Minh and the OSS section; Deer Team roster",
            "access_date": "2026-10-25",
            "source_quality": "A_direct_official",
            "rights_notes": "The page calls the photographer Alan Squires; that discrepancy is preserved rather than silently corrected.",
        },
        {
            "key": CMU,
            "stable_url": "https://iiif.library.cmu.edu/file/TAR_1944_38_24_07251944/TAR_1944_38_24_07251944.pdf",
            "archival_identifier": "The Carnegie Tartan, volume 38, number 24",
            "title": "The Carnegie Tartan",
            "author_creator": "The Carnegie Tartan staff",
            "repository_publisher": "Carnegie Institute of Technology; Carnegie Mellon University Libraries",
            "publication_record_date": "1944-07-25",
            "locator": "Page 2, 'Salute in Khaki' column; list of independent Tech men serving their country",
            "access_date": "2026-10-25",
            "source_quality": "B_authoritative_institutional",
            "rights_notes": "Contemporary campus-newspaper evidence; no employer is inferred from student affiliation.",
        },
        {
            "key": CAMBRIDGE,
            "stable_url": "https://assets.cambridge.org/97805218/36012/frontmatter/9780521836012_frontmatter.pdf",
            "archival_identifier": "ISBN 0-521-83601-8",
            "title": "Thailand's Secret War: The Free Thai, OSS, and SOE during World War II",
            "author_creator": "E. Bruce Reynolds",
            "repository_publisher": "Cambridge University Press",
            "publication_record_date": "2004",
            "locator": "Frontmatter illustrations 2 and 7; acknowledgments; notes on Thai-name transliteration",
            "access_date": "2026-10-25",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "rights_notes": "Project-authored paraphrases only. Variant transliterations are preserved as found.",
        },
        {
            "key": CIA_THAI,
            "stable_url": "https://www.cia.gov/resources/csi/static/OSS-and-Free-Thai.pdf",
            "title": "War of a Different Kind: OSS and Free Thai Operations in World War II",
            "author_creator": "Bob Bergin",
            "repository_publisher": "Central Intelligence Agency, Studies in Intelligence",
            "publication_record_date": "December 2011",
            "locator": "Studies in Intelligence 55(4), pages 11-22; overview of Thai student volunteers and OSS training",
            "access_date": "2026-10-25",
            "source_quality": "A_direct_official",
            "rights_notes": "Used for group context only; no group statement substitutes for a person-specific identity bridge.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": "carnegie-tech-b905",
            "canonical_name": "Carnegie Institute of Technology",
            "historical_name": "Carnegie Institute of Technology",
            "aliases": ["Carnegie Tech", "C.I.T."],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "Pittsburgh",
            "state_or_region": "Pennsylvania",
            "country": "United States",
            "active_dates": "1912-1967 under this name",
            "normalization_notes": "The 1944 historical name is preserved. Student status is modeled separately from employment.",
        }
    ]


def army_affiliation(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    person_id, name = PEOPLE[row]
    return {
        "key": f"{slug(name)}-occupation-b905",
        "person_id": person_id,
        "relationship_type": "employment",
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


def carnegie_affiliation() -> dict[str, object]:
    return {
        "key": "anonda-srivardhana-carnegie-tech-b905",
        "person_id": PEOPLE[31][0],
        "organization_key": "carnegie-tech-b905",
        "organization_name_as_found": "Carnegie Tech",
        "role_title": "student",
        "relationship_type": "student",
        "date_precision": "Attended Carnegie Tech before wartime service; the July 25, 1944 campus paper lists him among independent Tech men serving their country.",
        "city": "Pittsburgh",
        "state_or_region": "Pennsylvania",
        "country": "United States",
        "immediate_pre_oss": False,
        "last_civilian_pre_service": False,
        "pre_oss_temporal_basis": "documented_prewar",
        "identity_confidence": "high_confidence",
        "claim_confidence": "high",
        "source_quality": "B_authoritative_institutional",
        "publication_status": "published",
        "research_notes": "The contemporary institutional source establishes a student connection, not employment by Carnegie Tech.",
    }


def army_identity_claim(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    person_id, name = PEOPLE[row]
    variants = {
        24: "The official Army spelling uses Philip with one l; that spelling is retained as a documented variant.",
        30: "The official Army surname is Stranova; that spelling is retained as a documented variant.",
    }
    return {
        "key": f"identity-{slug(name)}-b905",
        "person_id": person_id,
        "claim_type": "identity",
        "claim_text": f"The indexed {name} row is a high-confidence match to the reviewed official Army record.",
        "evidence_paraphrase": "A nonshared protected identifier connects the visually verified index row to the official Army record.",
        "identity_match_assessment": "High confidence from the protected-identifier bridge and compatible name; any spelling variant is preserved rather than replacing the index form.",
        "temporal_assessment": "The Army record supports identity and a dated occupation category; it does not establish the OSS transfer sequence.",
        "source_quality": "A_direct_official",
        "claim_confidence": "high",
        "publication_status": "published",
        "match_notes": variants.get(row, "No protected identifier is exposed, and no employer or workplace is inferred from the coded field."),
        "sources": [
            {"source_key": INDEX, "locator_override": f"PDF page 442 row {row}; protected identifier withheld"},
            {"source_key": ARMY, "locator_override": "Accepted reviewed identity bridge; protected identifier withheld"},
        ],
    }


def army_occupation_claim(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    person_id, name = PEOPLE[row]
    return {
        "key": f"occupation-{slug(name)}-b905",
        "person_id": person_id,
        "affiliation_key": f"{slug(name)}-occupation-b905",
        "claim_type": "occupation",
        "claim_text": f"At Army entry on {item['date']}, the official record assigned {name} the historical civilian-occupation category '{item['occupation']}'; no employer is identified.",
        "evidence_paraphrase": f"The Army entry field carries code {item['code']}, which the visually checked NARA code list maps to the stated category.",
        "identity_match_assessment": "High confidence from a nonshared protected-identifier bridge between the index and official Army record.",
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
    }


def identity_only_army_claim(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    person_id, name = PEOPLE[row]
    return {
        "key": f"identity-{slug(name)}-b905",
        "person_id": person_id,
        "claim_type": "identity",
        "claim_text": f"The indexed {name} row is a high-confidence match to the reviewed official Army record, but that record does not support a publishable pre-OSS occupation claim.",
        "evidence_paraphrase": "A nonshared protected identifier connects the index row and official Army record; unusable or post-OSS occupational data are withheld.",
        "identity_match_assessment": "High confidence from the protected-identifier bridge, with source spelling damage or variation recorded where applicable.",
        "temporal_assessment": item["note"],
        "source_quality": "A_direct_official",
        "claim_confidence": "high",
        "publication_status": "published",
        "match_notes": "Identity evidence is separated from the unanswered pre-OSS employer and affiliation questions.",
        "sources": [
            {"source_key": INDEX, "locator_override": f"PDF page 442 row {row}; protected identifier withheld"},
            {"source_key": ARMY, "locator_override": f"Accepted identity bridge; Army entry {item['date']}; protected identifier withheld"},
            {"source_key": TECH, "support_type": "context_only", "locator_override": "Name, entry-date and occupation-field definitions"},
        ],
    }


def substantive_claims() -> list[dict[str, object]]:
    return [
        {
            "key": "aaron-squires-deer-team-conflict-b905",
            "person_id": PEOPLE[27][0],
            "claim_type": "identity",
            "claim_text": "Scholarly and magazine captions identify Aaron Squires with the OSS Deer Team, while a National Park Service history calls the team's photographer Alan Squires.",
            "evidence_paraphrase": "The exact-name photograph caption agrees with the index and Army bridge; the official NPS roster differs on the first name but agrees on surname, rank, role and team.",
            "identity_match_assessment": "High confidence that the indexed Aaron Squires served as the Deer Team photographer, with a visible source-level first-name discrepancy.",
            "temporal_assessment": "The evidence concerns OSS service in 1945 and supports identity, not a pre-OSS employer.",
            "source_quality": "A_direct_official",
            "claim_confidence": "conflicting",
            "publication_status": "conflicting",
            "match_notes": "The NPS wording is not silently corrected; Box 735 should be consulted for the authoritative name form.",
            "sources": [
                {"source_key": APUS, "locator_override": "PDF printed page 153; Deer Team photograph caption naming Aaron Squires"},
                {"source_key": NPS, "locator_override": "Deer Team roster naming Sergeant Alan Squires, photographer"},
                {"source_key": INDEX, "support_type": "supports", "locator_override": "PDF page 442 row 27; Aaron Squires"},
            ],
        },
        {
            "key": "identity-anonda-srivardhana-b905",
            "person_id": PEOPLE[31][0],
            "claim_type": "identity",
            "claim_text": "The indexed Anonda Srivardhana is a high-confidence match to Free Thai participant Anond Siwatthana (Srivardhana).",
            "evidence_paraphrase": "A contemporary Carnegie Tech paper names Anonda Srivardhana in military intelligence, while Reynolds identifies Anond Siwattana (Srivardhana) in OSS DURIAN training and acknowledges him as a wartime participant.",
            "identity_match_assessment": "High confidence from the distinctive name, documented transliteration variant, contemporary military-intelligence context and person-specific OSS training photograph.",
            "temporal_assessment": "The sources document pre-service student status and wartime OSS/Free Thai participation; they do not name a civilian employer.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "Anond Siwatthana and Anond Siwattana are retained as transliteration variants; no employer is inferred from Carnegie attendance.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 442 row 31; Box 735"},
                {"source_key": CMU, "locator_override": "Page 2, 'Salute in Khaki' column"},
                {"source_key": CAMBRIDGE, "locator_override": "Illustration 7 and acknowledgments"},
                {"source_key": CIA_THAI, "support_type": "context_only", "locator_override": "Thai student volunteers trained in America by OSS"},
            ],
        },
        {
            "key": "student-anonda-srivardhana-carnegie-b905",
            "person_id": PEOPLE[31][0],
            "affiliation_key": "anonda-srivardhana-carnegie-tech-b905",
            "claim_type": "other_pre_oss_affiliation",
            "claim_text": "Before wartime service, Anonda Srivardhana was affiliated with Carnegie Institute of Technology as a student; Carnegie was not his employer.",
            "evidence_paraphrase": "The July 1944 campus paper lists Srivardhana among independent Tech men serving their country and identifies his wartime field as military intelligence.",
            "identity_match_assessment": "High confidence from the distinctive exact name and compatible Free Thai/OSS wartime record.",
            "temporal_assessment": "Documented prewar student affiliation; the accessible source does not prove it was the immediate predecessor to OSS.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "Student status is modeled separately and excluded from employer analytics.",
            "sources": [{"source_key": CMU, "locator_override": "Page 2, 'Salute in Khaki' column"}],
        },
        {
            "key": "identity-karawek-srivicharn-b905",
            "person_id": PEOPLE[32][0],
            "claim_type": "identity",
            "claim_text": "The indexed Karawek Srivicharn is a high-confidence match to Karawek Siwichan (Srivicharn), one of the first Thai volunteers commissioned as Free Thai officers in December 1942.",
            "evidence_paraphrase": "Reynolds' caption names Karawek Siwichan (Srivicharn) among the first Thai volunteers immediately after their Free Thai commissions.",
            "identity_match_assessment": "High confidence from the distinctive name, explicit variant and compatible OSS/Free Thai chronology.",
            "temporal_assessment": "The December 1942 commission establishes wartime Free Thai officer status but does not identify a pre-OSS employer or prove the exact recruitment sequence.",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "The variant Karawek Siwichan is preserved. The commission is not relabeled as civilian employment.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 442 row 32; Box 735"},
                {"source_key": CAMBRIDGE, "locator_override": "Illustration 2 caption; first Thai volunteers commissioned in December 1942"},
                {"source_key": CIA_THAI, "support_type": "context_only", "locator_override": "Thai volunteers in America trained by OSS"},
            ],
        },
        {
            "key": "identity-alice-e-st-clair-conflict-b905",
            "person_id": PEOPLE[34][0],
            "claim_type": "identity",
            "claim_text": "Alice E St. Clair shares a protected identifier with the separately indexed Alice E Gibson; the conflict remains unresolved.",
            "evidence_paraphrase": "Two materially different index names in different boxes carry the same protected identifier.",
            "identity_match_assessment": "Conflicting until the Box 735 and Box 271 personnel files establish whether the identifier is a transcription error.",
            "temporal_assessment": "Identity conflict only; no Army evidence, occupation or affiliation is transferred.",
            "source_quality": "A_direct_official",
            "claim_confidence": "conflicting",
            "publication_status": "conflicting",
            "match_notes": "The rows remain separate, and the protected identifier is not exposed.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 442 row 34 and page 168 row 7; protected identifier withheld"},
                {"source_key": ARMY, "support_type": "context_only", "locator_override": "Conflicting shared-identifier candidate; protected identifier withheld"},
            ],
        },
        {
            "key": "identity-ramond-p-st-laurent-conflict-b905",
            "person_id": PEOPLE[42][0],
            "claim_type": "identity",
            "claim_text": "Ramond P St. Laurent shares a protected identifier with the separately indexed Eugene K Matthews; the conflict remains unresolved.",
            "evidence_paraphrase": "Materially different index names in different boxes carry the same protected identifier.",
            "identity_match_assessment": "Conflicting until the Box 735 and Box 492 personnel files establish whether the identifier is a transcription error.",
            "temporal_assessment": "Identity conflict only; no Army evidence, occupation or affiliation is transferred.",
            "source_quality": "A_direct_official",
            "claim_confidence": "conflicting",
            "publication_status": "conflicting",
            "match_notes": "The records remain separate, and the protected identifier is not exposed.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 442 row 42 and page 300 rows 29-30; protected identifier withheld"},
                {"source_key": ARMY, "support_type": "context_only", "locator_override": "Conflicting shared-identifier candidate; protected identifier withheld"},
            ],
        },
    ]


def unresolved_update(row: int) -> dict[str, object]:
    person_id, name = PEOPLE[row]
    category = "unknown_or_indeterminate"
    commissioned: bool | None = None
    if row in {26, 28}:
        category, commissioned = "enlisted_army_personnel", False
    elif row in {29, 35, 36}:
        category, commissioned = "commissioned_army_officer", True
    update: dict[str, object] = {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, its rank when printed, box and archive location, but staged official-context, CIA Reading Room, exact-name, occupation, employer, obituary, institutional, newspaper, directory, Library of Congress and archival searches found no defensible identity bridge. {UNRESOLVED[row]}",
        "personnel_category": category,
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": "Review the indexed Box 735 personnel file for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "critical",
    }
    if commissioned is not None:
        update["commissioned_officer"] = commissioned
    if row == 26:
        update["next_action"] = "Review Loren D Squire's Box 734 personnel file for corroborating identifiers and the last documented pre-OSS affiliation."
    if row in {25, 28}:
        update["possible_duplicate_group"] = "name-variant:emerson-t-squire-emerson-squires-page442"
    return update


def person_updates() -> list[dict[str, object]]:
    updates: list[dict[str, object]] = []
    for item in ARMY_OCCUPATIONS:
        row = int(item["row"])
        person_id, _name = PEOPLE[row]
        update: dict[str, object] = {
            "person_id": person_id,
            "identity_status": "high_confidence",
            "identity_evidence": "A nonshared protected identifier connects the visually verified index row to the reviewed official Army record. The historical occupation field is kept separate from employer and immediate-affiliation claims.",
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
        if row == 24:
            update["identity_evidence"] = "A nonshared protected identifier connects the index spelling Phillip to the official Army spelling Philip I Squillacioti. The one-letter variant is preserved."
            update["name_variants"] = ["Philip I Squillacioti"]
        elif row == 25:
            update["possible_duplicate_group"] = "name-variant:emerson-t-squire-emerson-squires-page442"
        elif row == 27:
            update["identity_evidence"] = "A nonshared protected identifier and exact-name scholarly Deer Team caption support Aaron Squires at high confidence. A National Park Service history calls the photographer Alan Squires, and that discrepancy remains public."
            update["research_status"] = "conflicting_sources"
            update["archival_review_priority"] = "critical"
            update["next_action"] = "Review Box 735 to resolve the Aaron/Alan Deer Team first-name discrepancy and identify the immediate pre-OSS affiliation and last civilian employer."
        elif row == 30:
            update["identity_evidence"] = "A nonshared protected identifier connects index spelling Sranova to official Army spelling Stranova. The surname variant is preserved without overwriting the index form."
            update["name_variants"] = ["Joseph T Stranova"]
        updates.append(update)

    for item in ARMY_IDENTITY_ONLY:
        row = int(item["row"])
        person_id, _name = PEOPLE[row]
        variants = {40: ["Wilfred T St. Lawrence"], 45: ["St IERRE Wallace J"]}
        update: dict[str, object] = {
            "person_id": person_id,
            "identity_status": "high_confidence",
            "identity_evidence": f"A nonshared protected identifier connects the index row to an official Army record. {item['note']}",
            "personnel_category": "enlisted_army_personnel",
            "commissioned_officer": False,
            "allied_or_foreign_personnel": False,
            "manual_review_required": True,
            "research_status": "requires_archival_review",
            "next_action": "Review the indexed Box 735 personnel file for the immediate pre-OSS affiliation and last civilian employer; do not use the withheld Army occupation field.",
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
            "archival_review_priority": "high",
        }
        if row in variants:
            update["name_variants"] = variants[row]
        updates.append(update)

    updates.extend(
        [
            {
                "person_id": PEOPLE[31][0],
                "identity_status": "high_confidence",
                "identity_evidence": "A distinctive-name contemporary Carnegie Tech record and Reynolds' person-specific OSS DURIAN photograph identify Anond Siwatthana/Siwattana (Srivardhana) at high confidence.",
                "name_variants": ["Anond Srivardhana", "Anond Siwatthana", "Anond Siwattana"],
                "personnel_category": "foreign_or_allied_military_personnel",
                "allied_or_foreign_personnel": True,
                "manual_review_required": True,
                "research_status": "completed",
                "next_action": "Review Box 735 for exact Free Thai/OSS dates and any civilian employer; retain Carnegie Institute of Technology as student affiliation only.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[32][0],
                "identity_status": "high_confidence",
                "identity_evidence": "Reynolds' distinctive-name caption explicitly identifies Karawek Siwichan (Srivicharn) among the first Thai volunteers commissioned as Free Thai officers in December 1942.",
                "name_variants": ["Karawek Siwichan"],
                "personnel_category": "foreign_or_allied_military_personnel",
                "commissioned_officer": True,
                "allied_or_foreign_personnel": True,
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Review Box 735 for Karawek Srivicharn's pre-service education or employment and the exact sequence between the Free Thai commission and OSS training.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[34][0],
                "identity_status": "conflicting",
                "identity_evidence": "Alice E St. Clair shares a protected identifier with the separately indexed Alice E Gibson in Box 271. The conflict prevents any identity, occupation or affiliation transfer.",
                "manual_review_required": True,
                "possible_duplicate_group": "shared-identifier:alice-e-st-clair-alice-e-gibson",
                "research_status": "conflicting_sources",
                "next_action": "Review the Alice E St. Clair Box 735 file and Alice E Gibson Box 271 file together before correcting either record or transferring evidence.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[42][0],
                "identity_status": "conflicting",
                "identity_evidence": "Ramond P St. Laurent shares a protected identifier with the separately indexed Eugene K Matthews entries in Box 492. The conflict prevents any identity, occupation or affiliation transfer.",
                "personnel_category": "commissioned_army_officer",
                "commissioned_officer": True,
                "manual_review_required": True,
                "possible_duplicate_group": "p299-300-442-eugene-mathews-stlaurent-b622",
                "research_status": "conflicting_sources",
                "next_action": "Review the Ramond P St. Laurent Box 735 file and Eugene K Matthews Box 492 files together before correcting either record or transferring evidence.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
        ]
    )

    # Replace a legacy private identifier-bearing group label on the already
    # indexed Alice E Gibson counterpart with the same descriptive, public-safe
    # group used for Alice E St. Clair. This changes no research status.
    updates.append(
        {
            "person_id": "ae0d28dd-c027-5799-829c-280f30240ddb",
            "possible_duplicate_group": "shared-identifier:alice-e-st-clair-alice-e-gibson",
        }
    )

    for row in UNRESOLVED:
        updates.append(unresolved_update(row))
    return updates


def research_attempts() -> list[dict[str, object]]:
    evidence_rows = {24, 25, 27, 30, 31, 32, 34, 40, 41, 42, 43, 44, 45, 46}
    notes = {
        24: "The protected-identifier bridge supports identity and a dated purchasing-agent/buyer category, but not a named employer.",
        25: "The protected-identifier bridge supports identity and a dated social/welfare-worker category; Emerson Squires remains a separate possible duplicate.",
        27: "Army evidence supports a dated photographer category, while Deer Team sources disagree between Aaron and Alan Squires.",
        30: "The protected-identifier bridge supports the Sranova/Stranova variant and a dated textile-manufacturing category, but not a named employer.",
        31: "Contemporary Carnegie Tech evidence and Reynolds' OSS DURIAN caption establish the identity, transliteration variants and student affiliation.",
        32: "Reynolds establishes the Srivicharn/Siwichan variant and December 1942 Free Thai officer commission, but not a pre-service employer.",
        34: "The protected identifier is shared with Alice E Gibson; no evidence is transferred until both files are reviewed.",
        40: "The protected-identifier bridge supports identity, but the 1946 Army entry is post-OSS and no occupation is transferred.",
        41: "The protected-identifier bridge supports identity and a dated semiskilled machine-shop category, but not a named employer.",
        42: "The protected identifier is shared with Eugene K Matthews; no evidence is transferred until both file groups are reviewed.",
        43: "The protected-identifier bridge supports identity and a dated textile-manufacturing category, but not a named employer.",
        44: "The protected-identifier bridge supports identity, but the occupation value is not safely interpreted and remains withheld.",
        45: "The protected-identifier bridge supports identity despite a damaged source name, but the late-1945 entry is post-OSS and no occupation is transferred.",
        46: "The protected-identifier bridge supports identity and a dated textile-manufacturing category, but not a named employer.",
    }
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        evidence = row in evidence_rows
        note = notes[row] if evidence else UNRESOLVED[row]
        box = "Box 734" if row in {24, 25, 26} else ("Box 752" if row == 30 else "Box 735")
        attempts.append(
            {
                "key": f"page442-row{row}-{slug(name)}-b905",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA/index context; CIA Reading Room exact-name check; OSS and rank variants; employer and occupation; obituary, institutional, newspaper, directory, Library of Congress and archival searches; {box}; protected-identifier Army crosswalk where available",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_905",
                "started_at": "2026-10-25T16:05:00Z",
                "completed_at": "2026-10-25T17:25:00Z",
                "outcome": "source_reviewed" if evidence else "candidate_rejected",
                "sources_reviewed": 9 if row in {27, 31, 32} else (7 if evidence else 6),
                "candidate_sources_rejected": 5 if evidence else 7,
                "rejection_reasons": "Unbridged namesakes, discovery-only results, chronologically irrelevant records and postwar-only leads were not assigned." if evidence else note,
                "research_notes": ("Reviewed evidence established a supported, qualified or explicitly conflicting outcome. " if evidence else "No reliable identity or pre-OSS employer was established after the staged search and namesake-rejection protocol. ") + note + " Search-result snippets were discovery aids only, no access control was bypassed, and no exposed NARA API credential was used.",
                "next_action": f"Review the indexed {box} personnel file for corroborating identifiers and the last documented pre-OSS affiliation.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b905-v1",
            }
        )
    return attempts


def main() -> None:
    affiliations = [army_affiliation(item) for item in ARMY_OCCUPATIONS]
    affiliations.append(carnegie_affiliation())
    claims = [army_identity_claim(item) for item in ARMY_OCCUPATIONS]
    claims.extend(army_occupation_claim(item) for item in ARMY_OCCUPATIONS)
    claims.extend(identity_only_army_claim(item) for item in ARMY_IDENTITY_ONLY)
    claims.extend(substantive_claims())
    bundle = {
        "bundle_version": "batch-905-v1",
        "reviewer": "Before OSS Batch 905 evidence review",
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
