#!/usr/bin/env python3
"""Generate the reviewed Batch 915 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import uuid
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "research/evidence-page448-stern-to-stevens-review_batch-915_2026-10-25.json"

INDEX = "nara-index-b915"
ARMY = "army-bulk-b915"
TECH = "army-tech-b915"
CODES = "army-codes-b915"
CIA_HARLEY = "cia-harley-stevens-b915"
AUB_HARLEY = "aub-harley-stevens-b915"
SFGATE_HARLEY = "sfgate-harley-stevens-b915"

PEOPLE = {
    1: ("3f7f9e19-f869-5e70-a564-020dc20ef000", "Samuel Stern"),
    2: ("c6431844-8e4d-557e-b04c-716b91b62574", "Louis Stern II"),
    3: ("3cd66e21-0ede-57f6-8ff1-024d079d6b16", "Ann Sterrett"),
    4: ("5afe2046-fe34-5561-8681-4dcc3ef0095a", "Robert E Stettler"),
    5: ("892b24cb-ca39-5186-97ba-6f84a016e1f7", "Henry L Steuben"),
    6: ("e8c7d51a-405a-5c6f-a7ee-cab51cc37ac8", "James M Steuber"),
    7: ("61cad98d-40a2-5194-b6c1-40b98534dd19", "Julian Steuer"),
    8: ("8e3ad75e-d90e-5d5e-a81a-16fb05bf4b58", "Eugene A Steuert"),
    9: ("6bb9642b-7be4-5724-9919-7d414ec5815a", "Robert G Steuert"),
    10: ("2d365fc2-da2c-53fe-b2f5-b9dc98986790", "Anthony Stevens"),
    11: ("23438d88-83f0-5667-9fe3-053023cbec0d", "Charles R Stevens"),
    12: ("a94b6c77-e585-5017-8403-1cc185e2975b", "Dorothy Stevens"),
    13: ("6c69c02c-9785-5468-849a-ba65c52486da", "Edmund Stevens"),
    14: ("05de92f2-8874-5824-8f2e-f20fbd59adc9", "Eldora K Stevens"),
    15: ("aaab3951-f2b4-538a-ab05-07c7418b8469", "Elinor N Stevens"),
    16: ("9832a83e-ae77-54e0-bb3a-a2bea584a4fe", "Evelyn M Stevens"),
    17: ("481dcee9-df77-599c-8d17-5c98e48049ab", "Frances W Stevens"),
    18: ("66a93bda-db9a-54dd-8e37-bec5c85a78c7", "Frank E Stevens"),
    19: ("a66e64a5-9747-528f-9fd4-9c8765da3cf7", "George Stevens"),
    20: ("87f86752-2ab4-5fc9-bc9f-36b343a8ddff", "Harley C Stevens"),
    21: ("ad2adb6a-4846-5fc2-959e-9ba25d198d8c", "John A Stevens"),
    22: ("26117ce0-c1d9-5bf3-a036-63c23c6b868e", "Lawrence N Stevens"),
    23: ("c086e4e0-577e-5b04-937c-7968e5e74186", "Mary E Stevens"),
}

JAMES_STRUEBER = "5b7b3a9e-8a78-50d8-82c7-d677b1b8df42"
JAMES_GROUP = "protected-conflict-b915-steuber-strueber"

ARMY_OCCUPATIONS = [
    {
        "row": 2,
        "date": "1943-03-22",
        "code": "099",
        "occupation": "Managers and officials, not elsewhere classified",
        "locator": "PDF physical page 171; category 0-99",
    },
    {
        "row": 5,
        "date": "1943-01-12",
        "code": "050",
        "occupation": "Laboratory technicians and assistants",
        "locator": "PDF physical page 171; category 0-50",
    },
    {
        "row": 7,
        "date": "1943-02-22",
        "code": "992",
        "occupation": "Students",
        "locator": "PDF physical page 304; amended category 9-92",
    },
    {
        "row": 21,
        "date": "1942-02-04",
        "code": "316",
        "occupation": "Farm hands, general farms",
        "locator": "PDF physical page 172; category 3-16",
    },
]

UNRESOLVED = {
    1: "The common name and protected index identifier produced no compatible official Army row or second person-specific OSS bridge.",
    3: "Exact-name, obituary, institutional, employment and archival searches produced no defensible identity bridge.",
    4: "The seven-digit protected identifier did not yield an official Army candidate, and exact-name searches did not establish the person's identity or chronology.",
    8: "The protected index identifier produced no compatible official Army row, and spelling-variant searches did not establish a reliable external identity.",
    9: "An exact-name Arlington cemetery lead lacks an OSS, protected-identifier or employment bridge and was not assigned.",
    10: "Searches returned numerous chronologically incompatible namesakes, including a postwar British psychiatrist, but no evidence tied one to this index row.",
    11: "Common-name military and obituary results lacked the protected identifier, OSS assignment or two corroborating identifiers required for assignment.",
    12: "A 1944 Camp Adair service-club hostess is a possible namesake only; the article supplies no OSS or person-specific bridge.",
    13: "Biographies of a well-known foreign correspondent named Edmund Stevens lack a protected identifier or source linking that biography to this row.",
    14: "Exact-name and variant searches produced no reliable identity, occupation or pre-OSS employer evidence.",
    15: "Exact-name and middle-initial searches produced no source with a defensible OSS identity bridge or employment chronology.",
    16: "The common name returned many incompatible vital-record candidates and no person-specific OSS or employment bridge.",
    17: "Exact-name searches returned unrelated directory and legal records but no reliable OSS identity or pre-OSS chronology.",
    18: "Common-name obituary and genealogy results did not provide an OSS assignment, protected identifier or other corroborating evidence.",
    19: "Official sources document film director George Stevens in OSS, but this no-initial index row has a different unresolved protected identifier and no Army bridge; the famous biography was not assigned on name alone.",
    23: "Exact-name, occupation, employer, obituary and archival searches produced no reliable person-specific match.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def stable_id(kind: str, value: str) -> str:
    return str(uuid.uuid5(uuid.NAMESPACE_URL, f"before-oss:{kind}:{value}"))


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 745-746; related Box 755 conflict row",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 448, rows 1-23; related James M Strueber conflict at page 453, row 27; checked against layout-preserving text and a rendered page image",
            "access_date": "2026-10-25",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All printed rows remain separate. Full protected identifiers remain private.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; four accepted reviewed Batch 915 identity bridges and one shared-identifier/name conflict",
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
            "locator": "PDF physical pages 171-172 and 304; categories 050, 099, 316 and amended 992 visually checked",
            "access_date": "2026-10-25",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical labels identify neither employers nor workplaces. The amended table on physical page 304 maps code 992 to Students.",
        },
        {
            "key": CIA_HARLEY,
            "stable_url": "https://www.cia.gov/resources/csi/static/Review-of-OSS.pdf",
            "archival_identifier": "CIA-RDP84-00499R000500080003-1",
            "title": "Book review of OSS: The Secret History of America's First Central Intelligence Agency",
            "author_creator": "Sherman Kent",
            "repository_publisher": "Central Intelligence Agency, Center for the Study of Intelligence",
            "publication_record_date": "Posted 2007-05-08; historical review released in full",
            "locator": "PDF physical page 6; discussion of the Harley Stevens papers",
            "access_date": "2026-10-25",
            "source_quality": "A_direct_official",
            "collection_name": "CIA Historical Review Program",
            "document_number": "CIA-RDP84-00499R000500080003-1",
            "rights_notes": "Official CIA publication used only to corroborate the distinctive OSS identity and Chungking command assignment.",
        },
        {
            "key": AUB_HARLEY,
            "stable_url": "https://www.aub.edu.lb/maingate/Documents/v2_no3-4_2003-2004.pdf",
            "archival_identifier": "MainGate, Summer 2004, Vol. II, Nos. 3 and 4",
            "title": "Georgiana Stevens (In Memoriam)",
            "author_creator": "MainGate editors",
            "repository_publisher": "American University of Beirut",
            "publication_record_date": "Summer 2004",
            "locator": "PDF physical page 66, In Memoriam II",
            "access_date": "2026-10-25",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "MainGate",
            "rights_notes": "Institutional memorial used for the concise prewar-to-OSS chronology; postwar employment is context only.",
        },
        {
            "key": SFGATE_HARLEY,
            "stable_url": "https://www.sfgate.com/bayarea/article/georgiana-gerlinger-stevens-writer-expert-on-2762337.php",
            "title": "Georgiana Gerlinger Stevens -- writer, expert on Mideast",
            "author_creator": "Michael Taylor",
            "repository_publisher": "San Francisco Chronicle / SFGATE",
            "publication_record_date": "2004-05-03",
            "locator": "Paragraphs describing Harley Stevens's law practice, Standard Oil assignment, OSS service and 1947 departure from Standard Oil",
            "access_date": "2026-10-25",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "rights_notes": "Reputable obituary corroboration; only short excerpts and project-authored paraphrases are retained.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": "standard-oil-california-b915",
            "organization_id": stable_id("organization", "Standard Oil Company of California historical"),
            "canonical_name": "Standard Oil Company of California",
            "historical_name": "Standard Oil Co. of California",
            "aliases": ["Standard Oil Company of California"],
            "organization_type": "oil and refining company",
            "sector": "business_and_industry",
            "country": "United States",
            "normalization_notes": "The historical company name in both sources is preserved; no modern successor name is substituted.",
        },
        {
            "key": "pillsbury-madison-sutro-b915",
            "organization_id": stable_id("organization", "Pillsbury Madison & Sutro historical law firm"),
            "canonical_name": "Pillsbury Madison & Sutro",
            "historical_name": "Pillsbury Madison & Sutro",
            "aliases": [],
            "organization_type": "law firm",
            "sector": "law",
            "city": "San Francisco",
            "state_or_region": "California",
            "country": "United States",
            "normalization_notes": "The historical firm name is preserved; the sources' modern successor reference is not substituted as Harley Stevens's employer.",
        },
    ]


def army_affiliation(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    person_id, name = PEOPLE[row]
    is_student = item["code"] == "992"
    return {
        "key": f"{slug(name)}-occupation-b915",
        "person_id": person_id,
        "relationship_type": "student" if is_student else "employment",
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


def affiliations() -> list[dict[str, object]]:
    values = [army_affiliation(item) for item in ARMY_OCCUPATIONS]
    values.extend(
        [
            {
                "key": "harley-stevens-standard-oil-b915",
                "person_id": PEOPLE[20][0],
                "organization_key": "standard-oil-california-b915",
                "organization_name_as_found": "Standard Oil Company of California",
                "role_title": "legal or company assignment; exact title not stated",
                "occupation": "attorney or company representative",
                "relationship_type": "employment",
                "country": "United States",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "The sources describe an assignment to Standard Oil, wartime OSS service and a 1947 departure from Standard Oil. They do not state an exact title, employment start date or leave arrangement.",
            },
            {
                "key": "harley-stevens-pillsbury-b915",
                "person_id": PEOPLE[20][0],
                "organization_key": "pillsbury-madison-sutro-b915",
                "organization_name_as_found": "Pillsbury Madison & Sutro",
                "role_title": "attorney",
                "occupation": "attorney",
                "relationship_type": "employment",
                "city": "San Francisco",
                "state_or_region": "California",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Documented earlier legal employment before the firm's Standard Oil assignment; not collapsed into the later oil-company affiliation.",
            },
        ]
    )
    return values


def army_claims(item: dict[str, object]) -> list[dict[str, object]]:
    row = int(item["row"])
    person_id, name = PEOPLE[row]
    return [
        {
            "key": f"identity-{slug(name)}-b915",
            "person_id": person_id,
            "claim_type": "identity",
            "claim_text": f"The indexed {name} row is a high-confidence match to the reviewed official Army record.",
            "evidence_paraphrase": "A nonshared protected identifier and compatible name connect the visually verified index row to the official Army record.",
            "identity_match_assessment": "High confidence from the nonshared protected-identifier bridge and compatible name.",
            "temporal_assessment": "The Army record supports identity and a dated occupation category; it does not establish the OSS transfer sequence.",
            "source_quality": "A_direct_official",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "No protected identifier is exposed, and the coded occupation is kept separate from employer claims.",
            "sources": [
                {"source_key": INDEX, "locator_override": f"PDF page 448 row {row}; protected identifier withheld"},
                {"source_key": ARMY, "locator_override": "Accepted reviewed identity bridge; protected identifier withheld"},
            ],
        },
        {
            "key": f"occupation-{slug(name)}-b915",
            "person_id": person_id,
            "affiliation_key": f"{slug(name)}-occupation-b915",
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
                {"source_key": CODES, "locator_override": item["locator"], "excerpt_override": item["occupation"]},
            ],
        },
    ]


def conflict_claims() -> list[dict[str, object]]:
    values = []
    for person_id, name, locator in [
        (PEOPLE[6][0], PEOPLE[6][1], "PDF page 448 row 6"),
        (JAMES_STRUEBER, "James M Strueber", "PDF page 453 row 27"),
    ]:
        values.append(
            {
                "key": f"identity-conflict-{slug(name)}-b915",
                "person_id": person_id,
                "claim_type": "identity",
                "claim_text": f"The official Army row cannot yet be assigned to {name}: the protected identifier is shared across two differently spelled index rows and the Army spelling agrees with neither exactly.",
                "evidence_paraphrase": "The index preserves separate Steuber and Strueber rows with one protected identifier; the Army record spells the surname Stueber.",
                "identity_match_assessment": "Conflicting. Name variation is plausible, but the shared identifier and three spellings require joint personnel-file review.",
                "temporal_assessment": "No Army occupation or chronology is transferred to either person while identity remains conflicting.",
                "source_quality": "A_direct_official",
                "claim_confidence": "conflicting",
                "publication_status": "conflicting",
                "match_notes": "Both person entities and source rows remain separate in one visible conflict group; no merger is performed.",
                "sources": [
                    {"source_key": INDEX, "locator_override": f"{locator}; protected identifier withheld"},
                    {"source_key": ARMY, "locator_override": "Conflicting Army name STUEBER JAMES M; protected identifier withheld"},
                ],
            }
        )
    return values


def harley_claims() -> list[dict[str, object]]:
    person_id = PEOPLE[20][0]
    identity_assessment = "High confidence from the distinctive Harley Stevens name, the index's lieutenant-colonel rank, and independent sources explicitly placing him in OSS Chungking command."
    return [
        {
            "key": "identity-harley-c-stevens-b915",
            "person_id": person_id,
            "claim_type": "identity",
            "claim_text": "The indexed Lieutenant Colonel Harley C. Stevens is a high-confidence match to Harley Stevens, OSS detachment commander in Chungking.",
            "evidence_excerpt": "was commander of the OSS detachment in Chungking",
            "evidence_paraphrase": "The CIA review names Harley Stevens as the Chungking detachment commander; institutional and newspaper chronologies independently place him in OSS.",
            "identity_match_assessment": identity_assessment,
            "temporal_assessment": "The sources establish wartime OSS service and provide the sequence from prewar work into OSS, but do not cite the index box or protected identifier.",
            "source_quality": "A_direct_official",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "The middle initial does not appear in the external sources, so the identity is high-confidence rather than confirmed from a direct personnel-file link.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 448 row 20; Lieutenant Colonel; protected identifier withheld"},
                {"source_key": CIA_HARLEY, "excerpt_override": "was commander of the OSS detachment in Chungking"},
                {"source_key": AUB_HARLEY},
                {"source_key": SFGATE_HARLEY},
            ],
        },
        {
            "key": "immediate-harley-stevens-standard-oil-b915",
            "person_id": person_id,
            "affiliation_key": "harley-stevens-standard-oil-b915",
            "claim_type": "immediate_pre_oss_affiliation",
            "claim_text": "Standard Oil Company of California is Harley C. Stevens's best-supported immediate civilian affiliation before his wartime OSS service.",
            "evidence_excerpt": "The firm assigned Stevens to Standard Oil Company of California",
            "evidence_paraphrase": "Both accounts place his Standard Oil assignment after law-firm practice and immediately before describing his wartime entry into OSS.",
            "identity_match_assessment": identity_assessment,
            "temporal_assessment": "Strongly date-bounded, but neither source states an exact OSS entry date or whether Standard Oil employment formally paused during service.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "The exact corporate title is not inferred. Postwar American Independent Oil employment is excluded from the pre-OSS claim.",
            "sources": [
                {"source_key": AUB_HARLEY, "excerpt_override": "The firm assigned Stevens to Standard Oil Company of California"},
                {"source_key": SFGATE_HARLEY, "locator_override": "Paragraphs 112-114 and 122"},
            ],
        },
        {
            "key": "last-civilian-harley-stevens-standard-oil-b915",
            "person_id": person_id,
            "affiliation_key": "harley-stevens-standard-oil-b915",
            "claim_type": "last_civilian_pre_service",
            "claim_text": "Standard Oil Company of California is Harley C. Stevens's best-supported last civilian employer before wartime OSS service.",
            "evidence_paraphrase": "The same two chronologies place Standard Oil between his law-firm work and OSS service; SFGATE states that he left Standard Oil in 1947.",
            "identity_match_assessment": identity_assessment,
            "temporal_assessment": "The last-civilian sequence is strong, although an exact separation or wartime leave date is not given.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "The classification is separate from the immediate-affiliation claim and does not imply that Standard Oil was a military or OSS assignment.",
            "sources": [
                {"source_key": AUB_HARLEY, "locator_override": "PDF physical page 66, Harley Stevens chronology"},
                {"source_key": SFGATE_HARLEY, "locator_override": "Paragraphs 112-114 and 122"},
            ],
        },
        {
            "key": "earlier-harley-stevens-pillsbury-b915",
            "person_id": person_id,
            "affiliation_key": "harley-stevens-pillsbury-b915",
            "claim_type": "other_pre_oss_affiliation",
            "claim_text": "Before his Standard Oil assignment, Harley C. Stevens practiced law at Pillsbury Madison & Sutro in San Francisco.",
            "evidence_excerpt": "was practicing law with the firm of Pillsbury Madison & Sutro",
            "evidence_paraphrase": "The institutional memorial and newspaper obituary independently describe his law practice before the Standard Oil assignment.",
            "identity_match_assessment": identity_assessment,
            "temporal_assessment": "Documented prewar employment; it is earlier than the Standard Oil affiliation and is not labeled immediate.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "The historical law-firm name is preserved and not replaced by a successor firm.",
            "sources": [
                {"source_key": AUB_HARLEY, "excerpt_override": "was practicing law with the firm of Pillsbury Madison & Sutro"},
                {"source_key": SFGATE_HARLEY, "locator_override": "Paragraph 112"},
            ],
        },
    ]


def accepted_update(item: dict[str, object]) -> dict[str, object]:
    person_id, _name = PEOPLE[int(item["row"])]
    return {
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


def unresolved_update(row: int) -> dict[str, object]:
    person_id, name = PEOPLE[row]
    box = 745 if row <= 22 else 746
    return {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, rank when printed, box and archive location, but staged NARA context, CIA Reading Room, exact-name, occupation, employer, obituary, institutional, newspaper, directory, Library of Congress and archival searches found no defensible identity bridge. {UNRESOLVED[row]}",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": f"Review the indexed Box {box} personnel file for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "critical" if row in {1, 4, 8, 9, 10, 11, 12, 13, 19, 23} else "high",
    }


def person_updates() -> list[dict[str, object]]:
    updates = [accepted_update(item) for item in ARMY_OCCUPATIONS]
    updates.extend(unresolved_update(row) for row in UNRESOLVED)
    updates.extend(
        [
            {
                "person_id": PEOPLE[6][0],
                "identity_status": "conflicting",
                "identity_evidence": "The protected identifier printed for James M Steuber is also printed for James M Strueber on page 453. The official Army row spells the surname Stueber; neither person receives the Army record or its occupation code pending joint file review.",
                "manual_review_required": True,
                "possible_duplicate_group": JAMES_GROUP,
                "research_status": "conflicting_sources",
                "next_action": "Review the Box 745 James M Steuber and Box 755 James M Strueber personnel files together; do not merge the people or transfer the Army record before the conflict is resolved.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": JAMES_STRUEBER,
                "identity_status": "conflicting",
                "identity_evidence": "The protected identifier printed for James M Strueber is also printed for James M Steuber on page 448. The official Army row spells the surname Stueber; neither person receives the Army record or its occupation code pending joint file review.",
                "manual_review_required": True,
                "possible_duplicate_group": JAMES_GROUP,
                "research_status": "conflicting_sources",
                "next_action": "Review the Box 745 James M Steuber and Box 755 James M Strueber personnel files together; do not merge the people or transfer the Army record before the conflict is resolved.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[20][0],
                "identity_status": "high_confidence",
                "identity_evidence": "The distinctive Harley Stevens name, the index's lieutenant-colonel rank, an official CIA reference to OSS Chungking command and two independent prewar-to-OSS chronologies support a high-confidence identity. The external sources do not provide the middle initial or protected identifier, so the match is not labeled confirmed.",
                "personnel_category": "commissioned_army_officer",
                "commissioned_officer": True,
                "allied_or_foreign_personnel": False,
                "manual_review_required": False,
                "research_status": "verified_employer_found",
                "next_action": "Review the indexed Box 745 personnel file to confirm exact Standard Oil dates and Harley Stevens's formal employment or leave status during wartime OSS service.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "medium",
            },
            {
                "person_id": PEOPLE[22][0],
                "identity_status": "unresolved",
                "identity_evidence": "The visually verified index identifies Lawrence N Stevens as an ensign in Box 745. Seventeen recorded attempts, including the renewed Batch 915 check, found no source with two corroborating identifiers beyond the common name and naval rank.",
                "personnel_category": "commissioned_naval_officer",
                "commissioned_officer": True,
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Review the indexed Box 745 personnel file for a service identifier, naval assignment, hometown and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
        ]
    )
    return updates


def research_attempts() -> list[dict[str, object]]:
    accepted_rows = {int(item["row"]) for item in ARMY_OCCUPATIONS}
    attempts = []
    for row, (person_id, name) in PEOPLE.items():
        box = 745 if row <= 22 else 746
        if row in accepted_rows:
            outcome = "source_reviewed"
            detail = "A reviewed official Army identity and dated historical occupation or student category were accepted; no named employer is supplied."
        elif row == 6:
            outcome = "candidate_found"
            detail = "The official Army candidate remains conflicting because the protected identifier is shared with James M Strueber and the Army surname is Stueber."
        elif row == 20:
            outcome = "source_reviewed"
            detail = "CIA, American University of Beirut and SFGATE sources support a high-confidence identity, Standard Oil as the best-supported immediate and last civilian affiliation, and earlier Pillsbury Madison & Sutro employment."
        elif row == 22:
            outcome = "candidate_rejected"
            detail = "A renewed exact-name, occupation, obituary and official-context check did not improve the sixteen previously recorded attempts; the common-name ensign remains unresolved."
        else:
            outcome = "candidate_rejected"
            detail = UNRESOLVED[row]
        attempts.append(
            {
                "key": f"page448-row{row}-{slug(name)}-b915",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA/index context; CIA Reading Room and Library of Congress official-domain exact-name checks; OSS, rank and spelling variants; employer and occupation; obituary, institutional, newspaper, directory and archival searches; Box {box}; protected-identifier Army crosswalk where available",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_915",
                "started_at": "2026-10-26T01:20:00Z",
                "completed_at": "2026-10-26T01:41:00Z",
                "outcome": outcome,
                "sources_reviewed": 10 if row == 20 else (8 if row in accepted_rows or row in {6, 12, 13, 19, 22} else 6),
                "candidate_sources_rejected": 3 if row == 20 else (5 if row in accepted_rows else 7),
                "rejection_reasons": "Unbridged namesakes, discovery-only results, chronologically incompatible records and postwar-only material were not assigned." if row in accepted_rows or row == 20 else detail,
                "research_notes": f"{detail} Search-result snippets were discovery aids only; public claims point to inspectable sources. No access control was bypassed, and no exposed NARA API credential was used.",
                "next_action": "Review the indexed personnel file for exact employment dates and the documented wartime transition." if row == 20 else f"Review the indexed Box {box} personnel file for corroborating identifiers and the last documented pre-OSS affiliation.",
                "attempt_number": 17 if row == 22 else 1,
                "research_agent_version": "before-oss-b915-v1",
            }
        )
    attempts.append(
        {
            "key": "page453-row27-james-m-strueber-linked-conflict-b915",
            "person_id": JAMES_STRUEBER,
            "source_adapter": "manual_staged_protocol",
            "query_text": "James M Strueber; James M Steuber; James M Stueber; NARA/index context; protected-identifier Army crosswalk; joint Box 745 and Box 755 conflict review",
            "query_variant_type": "linked_shared_identifier_conflict_protocol_batch_915",
            "started_at": "2026-10-26T01:20:00Z",
            "completed_at": "2026-10-26T01:41:00Z",
            "outcome": "candidate_found",
            "sources_reviewed": 4,
            "candidate_sources_rejected": 1,
            "rejection_reasons": "The official Army row cannot be assigned while two separately preserved index rows share the protected identifier and use different surname spellings.",
            "research_notes": "The page 453 Strueber row was reviewed with the page 448 Steuber row. Both entities remain separate; no Army occupation or employer evidence is transferred.",
            "next_action": "Review the Box 745 James M Steuber and Box 755 James M Strueber personnel files together before resolving the identity conflict.",
            "attempt_number": 1,
            "research_agent_version": "before-oss-b915-v1",
        }
    )
    return attempts


def main() -> None:
    claims: list[dict[str, object]] = []
    for item in ARMY_OCCUPATIONS:
        claims.extend(army_claims(item))
    claims.extend(conflict_claims())
    claims.extend(harley_claims())
    bundle = {
        "bundle_version": "batch-915-v1",
        "reviewer": "Before OSS Batch 915 evidence review",
        "sources": sources(),
        "organizations": organizations(),
        "affiliations": affiliations(),
        "claims": claims,
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }
    OUTPUT.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
