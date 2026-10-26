#!/usr/bin/env python3
"""Generate the reviewed Batch 920 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "research/evidence-page450-isabel-stokes-to-franklin-stone-review_batch-920_2026-10-26.json"

INDEX = "nara-index-b920"
ARMY = "army-bulk-b920"
TECH = "army-tech-b920"
CODES = "army-codes-b920"
AWARDS = "nara-oss-awards-stolin-b920"
HOOVER = "hoover-oss-board-stonborough-b920"


PEOPLE = {
    24: ("bf4437e8-a3fb-5387-b289-c9e27e117b4e", "Isabel Stokes", "749"),
    25: ("12343f77-a18b-559d-864b-71cc57d115c4", "James W Stokes", "749"),
    26: ("33413cb8-c61e-56e2-81e7-5e2e8a613240", "James K Stokes", "749"),
    27: ("1d94cda6-a735-5a4a-9047-27a27013cc61", "James R Stokes", "749"),
    28: ("3e179fd6-e6a9-5bf2-b1ca-5997e5df0300", "Robert Stokes", "749"),
    29: ("b98dfab5-e0d0-51d7-b9ce-3696abcc8827", "Alice O Stolb", "749"),
    30: ("041c3b88-ce0b-5a7c-bbac-bfbc68000c0a", "Robert F Stolb", "749"),
    31: ("f47a9347-c428-512a-8421-04b72a6e8fc2", "John A Stolba", "749"),
    32: ("3f95a78f-89c6-59d5-8120-f97cef7d50c2", "Samuel J Stolin", "749"),
    33: ("1e2adc0f-26d5-5033-992f-828b60315c18", "Carrol J Stoll", "749"),
    34: ("fd99bf74-21d1-5158-87bf-5f1f007d2ac1", "Carl Stolle", "749"),
    35: ("ef6b0129-32d4-5866-90f7-0758bc48a640", "Norman E Stoller", "749"),
    36: ("b97f6b08-7810-5cd3-b4e3-b6c0138ac4c6", "Edwin R Stolp", "749"),
    37: ("67c66b5e-b4f4-59cd-bab9-62be1163b616", "George W Stolte", "749"),
    38: ("3988ba42-de0b-58ed-9d67-87122d344b2d", "William J Stolte", "749"),
    39: ("acf22eae-f5a0-50fd-b211-edbcccb657f7", "Thomas Stonborough", "749"),
    40: ("5dc90dbe-8b7b-5fa5-8a11-96e0f50480b3", "Bruce D Stone", "749"),
    41: ("f3851d6e-3d61-5083-9420-e249e5569012", "Charlotte B Stone", "749"),
    42: ("92e75949-e907-5931-b0c7-1dfe8c5141cc", "Edward A Stone", "749"),
    43: ("c1173b12-5447-565c-b347-429b4d680b14", "Everett L Stone", "750"),
    44: ("ae7a9be2-be83-544b-853c-7e8b43b6272e", "Frank D Stone", "750"),
    45: ("368971b6-e196-56dc-be2d-d22ae72978a6", "Frank D Stone", "750"),
    46: ("18c19532-d243-5e0a-982e-6a79be33cce2", "Franklin M Stone", "750"),
}


ARMY_OCCUPATIONS = [
    {"row": 25, "slug": "james-w-stokes", "date": "1942-05-18", "code": "002", "occupation": "Actors and actresses", "locator": "PDF physical page 175; alphabetical listing for Actors and actresses"},
    {"row": 27, "slug": "james-r-stokes", "date": "1941-09-15", "code": "105", "occupation": "Clerks, general office", "locator": "PDF physical page 171; category 1-05"},
    {"row": 30, "slug": "robert-f-stolb", "date": "1942-05-05", "code": "653", "occupation": "Chemical products producing occupations, not elsewhere classified", "locator": "PDF physical page 176; category 6-53"},
    {"row": 32, "slug": "samuel-j-stolin", "date": "1942-10-23", "code": "138", "occupation": "Stock clerks", "locator": "PDF physical pages 171 and 176; category 1-38"},
    {"row": 34, "slug": "carl-stolle", "date": "1942-10-12", "code": "497", "occupation": "Electricians", "locator": "PDF physical pages 174 and 176; category 4-97"},
    {"row": 35, "slug": "norman-e-stoller", "date": "1942-12-11", "code": "175", "occupation": "Salespersons", "locator": "PDF physical page 171; category 1-75"},
    {"row": 40, "slug": "bruce-d-stone", "date": "1943-02-11", "code": "499", "occupation": "Electrical machinery and accessories manufacturing occupations, not elsewhere classified", "locator": "PDF physical pages 174 and 176; category 4-99"},
]


UNRESOLVED = {
    24: "Exact-name results concerned unbridged namesakes, including a modern organizer and an Australian serviceman's spouse; no OSS or Box 749 bridge was found.",
    28: "Two Library of Congress candidates lacked a middle name, protected-identifier link, OSS context or Box 749 bridge; a common-name match alone is insufficient.",
    29: "Exact-name, occupation, obituary, institutional, newspaper and archival searches produced no person-specific result with an OSS or Box 749 bridge.",
    31: "Searches produced older and unrelated Stolba namesakes but no matching middle initial, OSS context, employer or Box 749 bridge.",
    33: "Exact-name and variant searches produced no reliable identity or employment evidence for the indexed spelling Carrol J Stoll.",
    36: "The official Army bulk crosswalk found no exact protected-identifier record; because that source is damaged and incomplete, the nonhit is not negative service evidence.",
    37: "The official Army bulk crosswalk found no exact protected-identifier record, and an early city-directory namesake could not be bridged to the index row.",
    38: "The official Army bulk crosswalk found no exact protected-identifier record; later banking and obituary namesakes lacked a wartime identity bridge.",
    41: "Exact-name results were postwar or unbridged namesakes and supplied no OSS, protected-identifier or Box 749 connection.",
    42: "Five Library of Congress candidates concerned Edward C. Stone or were unsupported OCR results; none established Edward A. Stone's identity or employment.",
    43: "Three Library of Congress candidates were too early, wrong-initial or OCR false positives; no source established the indexed Everett L Stone.",
    46: "The short printed identifier lies outside the Army adapter's defensible scope, and exact-name results were later or unbridged namesakes.",
}


LOC_REJECTIONS = {25: 3, 26: 3, 27: 3, 28: 2, 42: 5, 43: 3, 44: 5, 45: 5}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 749-750",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 450, rows 24-46; checked against layout-preserving text and a rendered page image",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. The two Frank D Stone rows carry different protected identifiers and are not merged. Full identifiers remain private.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; eight accepted Batch 920 identity bridges, one rejected middle-initial conflict and three identifier nonhits",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "No raw row or full protected identifier is retained in public assets. Coded occupations identify no employer, and a nonhit is not negative service evidence.",
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
            "locator": "PDF physical pages 171 and 174-176; categories 002, 105, 138, 175, 497, 499 and 653 visually checked",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical occupation labels identify neither employers nor workplaces. Code 993 is absent from the reviewed list and is not interpreted.",
        },
        {
            "key": AWARDS,
            "stable_url": "https://www.archives.gov/files/research/jfk/releases/104-10165-10120.pdf",
            "archival_identifier": "NARA JFK release 104-10165-10120",
            "title": "OSS awards and decorations board records",
            "author_creator": "Office of Strategic Services",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1945",
            "locator": "PDF physical page 183, internal page 8; SO Branch 2 Unit Commander's Certificate of Merit list",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "collection_name": "John F. Kennedy Assassination Records Collection",
            "document_number": "104-10165-10120",
            "rights_notes": "The scan was OCR-located and visually inspected. It confirms Samuel J. Stolin's OSS master-sergeant identity but supplies no pre-OSS employer.",
        },
        {
            "key": HOOVER,
            "stable_url": "https://digitalcollections.hoover.org/internal/media/dispatcher/331570/full",
            "archival_identifier": "Hoover Institution internal media 331570",
            "title": "Report of OSS Board of Officers examination at Bastia, Corsica",
            "author_creator": "Office of Strategic Services Board of Officers",
            "repository_publisher": "Hoover Institution Library & Archives",
            "publication_record_date": "1944-05-02",
            "locator": "PDF physical page 7; examination of Thomas H. W. Stonborough",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "rights_notes": "The declassified official record was reviewed through Hoover's indexed transcription and stable document reference; only short excerpts and project-authored paraphrases are retained.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": "opa-b920",
            "organization_id": "a37403a5-5878-511c-9413-dd7054848aa0",
            "canonical_name": "United States Office of Price Administration",
            "historical_name": "Office of Price Administration",
            "aliases": ["OPA"],
            "organization_type": "federal wartime agency",
            "sector": "federal_government",
            "city": "Washington",
            "state_or_region": "District of Columbia",
            "country": "United States",
            "active_dates": "1941-1947",
            "normalization_notes": "Reuses the existing canonical organization. The Cleveland area office remains a location of the historical agency, not a separate employer.",
        },
        {
            "key": "stonborough-market-research-b920",
            "canonical_name": "Thomas H. W. Stonborough's market research business",
            "historical_name": "his own market research business",
            "aliases": [],
            "organization_type": "self-employed market research practice",
            "sector": "self_employed",
            "country": "United States",
            "normalization_notes": "The official source does not name the business. The project label preserves ownership and does not invent a firm name.",
        },
    ]


def army_affiliation(item: dict[str, object]) -> dict[str, object]:
    person_id, _, _ = PEOPLE[int(item["row"])]
    return {
        "key": f"{item['slug']}-occupation-b920",
        "person_id": person_id,
        "relationship_type": "employment",
        "occupation": item["occupation"],
        "end_date": item["date"],
        "date_precision": f"Historical civilian-occupation code {item['code']} was recorded at Army entry on {item['date']}; no employer or OSS-transfer date is named.",
        "country": "United States",
        "immediate_pre_oss": False,
        "last_civilian_pre_service": False,
        "pre_oss_temporal_basis": "strongly_date_bounded",
        "identity_confidence": "confirmed" if int(item["row"]) == 32 else "high_confidence",
        "claim_confidence": "medium",
        "source_quality": "A_direct_official",
        "publication_status": "publish_qualified",
        "research_notes": "The historical category is not converted into a named employer, workplace, institution or exact title.",
    }


def affiliations() -> list[dict[str, object]]:
    result = [army_affiliation(item) for item in ARMY_OCCUPATIONS]
    result.extend(
        [
            {
                "key": "thomas-stonborough-opa-b920",
                "person_id": PEOPLE[39][0],
                "organization_key": "opa-b920",
                "organization_name_as_found": "Office of Price Administration",
                "role_title": "Research Director, Cleveland area",
                "occupation": "research director",
                "relationship_type": "government_assignment",
                "end_date": "1943-07",
                "date_precision": "The OSS board says this was his previous position when he entered OSS in July 1943; no exact day or start date is stated.",
                "city": "Cleveland",
                "state_or_region": "Ohio",
                "country": "United States",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "explicit_immediate",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "A_direct_official",
                "publication_status": "published",
                "research_notes": "Modeled as a federal government assignment, not a civilian employer.",
            },
            {
                "key": "thomas-stonborough-market-research-b920",
                "person_id": PEOPLE[39][0],
                "organization_key": "stonborough-market-research-b920",
                "organization_name_as_found": "his own market research business",
                "occupation": "market researcher",
                "relationship_type": "self_employment",
                "date_precision": "The OSS board places this work before his Cleveland-area OPA position; it gives no business name or exact dates.",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "A_direct_official",
                "publication_status": "published",
                "research_notes": "Published as the last documented civilian work before the intervening federal assignment, not as the immediate pre-OSS affiliation.",
            },
        ]
    )
    return result


def army_identity_claim(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    person_id, name, _ = PEOPLE[row]
    confirmed = row == 32
    claim = {
        "key": f"identity-{item['slug']}-b920",
        "person_id": person_id,
        "claim_type": "identity",
        "claim_text": f"The indexed {name} row is {'confirmed as the OSS master sergeant named in a direct official record and matched to' if confirmed else 'a high-confidence match to'} the reviewed official Army record.",
        "evidence_paraphrase": "A nonshared protected identifier connects the visually verified index row to the official Army record." + (" A separate OSS award record names M/Sgt Samuel J. Stolin." if confirmed else ""),
        "identity_match_assessment": "Confirmed by exact distinctive name, a nonshared protected identifier and a separate direct OSS master-sergeant record." if confirmed else "High confidence from a nonshared protected-identifier bridge and the reviewed name alignment.",
        "temporal_assessment": "The records support identity and a dated Army-entry occupation category; they do not establish the OSS transfer sequence or a named employer.",
        "source_quality": "A_direct_official",
        "claim_confidence": "confirmed" if confirmed else "high",
        "publication_status": "published",
        "match_notes": "No protected identifier is exposed, and no employer or workplace is inferred from the coded field.",
        "sources": [
            {"source_key": INDEX, "locator_override": f"PDF page 450 row {row}; protected identifier withheld"},
            {"source_key": ARMY, "locator_override": "Accepted reviewed identity bridge; protected identifier withheld"},
        ],
    }
    if confirmed:
        claim["evidence_excerpt"] = "M/Sgt Samuel J. Stolin — Approved"
        claim["sources"].append({"source_key": AWARDS, "locator_override": "PDF physical page 183, internal page 8"})
    return claim


def army_occupation_claim(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    person_id, name, _ = PEOPLE[row]
    return {
        "key": f"occupation-{item['slug']}-b920",
        "person_id": person_id,
        "affiliation_key": f"{item['slug']}-occupation-b920",
        "claim_type": "occupation",
        "claim_text": f"At Army entry on {item['date']}, {name} was recorded in the historical {str(item['occupation']).lower()} category; no employer is identified.",
        "evidence_paraphrase": f"The accepted Army record carries civilian-occupation code {item['code']}, decoded from NARA's official code list.",
        "identity_match_assessment": "The category belongs only to the reviewed protected-identifier match; the identifier itself is not public.",
        "temporal_assessment": "Strongly date-bounded to Army entry; it does not establish the immediate pre-OSS affiliation or a named employer.",
        "source_quality": "A_direct_official",
        "claim_confidence": "medium",
        "publication_status": "publish_qualified",
        "match_notes": "The historical category is a qualified lead, not an employer, workplace, institution or exact title.",
        "sources": [
            {"source_key": ARMY, "locator_override": f"Accepted reviewed identity record; civilian occupation code {item['code']}; protected identifier withheld"},
            {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46; Army-entry-date and civilian-occupation fields"},
            {"source_key": CODES, "locator_override": item["locator"], "excerpt_override": item["occupation"]},
        ],
    }


def claims() -> list[dict[str, object]]:
    result: list[dict[str, object]] = []
    for item in ARMY_OCCUPATIONS:
        result.append(army_identity_claim(item))
        result.append(army_occupation_claim(item))
    result.append(
        {
            "key": "identity-frank-d-stone-row45-b920",
            "person_id": PEOPLE[45][0],
            "claim_type": "identity",
            "claim_text": "The second indexed Frank D Stone row is a high-confidence match to the reviewed official Army record and remains separate from the adjacent same-name row.",
            "evidence_paraphrase": "A nonshared protected identifier selects an exact-name Army record; the adjacent Frank D Stone row carries a different protected identifier.",
            "identity_match_assessment": "High confidence for this row only from exact name and a nonshared protected identifier; no merge with the adjacent row is permitted.",
            "temporal_assessment": "The Army entry is dated 1943-01-06. Its occupation code 993 is undefined in the reviewed NARA list and is not interpreted.",
            "source_quality": "A_direct_official",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "The damaged grade field and undefined occupation code are withheld. Full identifiers are not exposed.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 450 rows 44-45; two separate Frank D Stone rows; protected identifiers withheld"},
                {"source_key": ARMY, "locator_override": "Accepted exact-name row-45 identity bridge; protected identifier withheld"},
                {"source_key": CODES, "support_type": "context_only", "locator_override": "Reviewed occupation list; code 993 absent and not interpreted"},
            ],
        }
    )
    result.extend(
        [
            {
                "key": "conflict-james-k-stokes-b920",
                "person_id": PEOPLE[26][0],
                "claim_type": "identity",
                "claim_text": "James K Stokes's protected identifier points to an official Army record under the materially different middle initial E.",
                "evidence_paraphrase": "The protected identifier agrees, but the Army row names James E Stokes; no grade, date or occupation is transferred.",
                "identity_match_assessment": "Conflicting. A protected identifier cannot override a substantive middle-initial disagreement without the personnel file.",
                "temporal_assessment": "No Army chronology or occupation is assigned while identity remains conflicting.",
                "source_quality": "A_direct_official",
                "claim_confidence": "conflicting",
                "publication_status": "conflicting",
                "match_notes": "Review Box 749 before correcting an identifier or accepting the Army candidate.",
                "sources": [
                    {"source_key": INDEX, "locator_override": "PDF page 450 row 26; protected identifier withheld"},
                    {"source_key": ARMY, "support_type": "context_only", "locator_override": "Rejected middle-initial-conflict candidate; protected identifier withheld"},
                ],
            },
            {
                "key": "identity-thomas-stonborough-b920",
                "person_id": PEOPLE[39][0],
                "claim_type": "identity",
                "claim_text": "The indexed Thomas Stonborough is a high-confidence match to civilian OSS member Thomas H. W. Stonborough examined at Bastia in 1944.",
                "evidence_excerpt": "Thomas H. W. Stonborough, civilian. Entered the OSS July 1943 in New York.",
                "evidence_paraphrase": "A direct OSS board record supplies the distinctive full name, civilian status, entry month and wartime assignment.",
                "identity_match_assessment": "High confidence from the distinctive exact first and surname plus direct OSS context; Box 749 remains needed to confirm the omitted middle names.",
                "temporal_assessment": "The record dates OSS entry to July 1943 and explicitly describes the two preceding work stages.",
                "source_quality": "A_direct_official",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "The index form remains primary display text; Thomas H. W. Stonborough is preserved as a documented variant.",
                "sources": [
                    {"source_key": INDEX, "locator_override": "PDF page 450 row 39; Box 749"},
                    {"source_key": HOOVER, "locator_override": "PDF physical page 7; first examination"},
                ],
            },
            {
                "key": "immediate-thomas-stonborough-opa-b920",
                "person_id": PEOPLE[39][0],
                "affiliation_key": "thomas-stonborough-opa-b920",
                "claim_type": "immediate_pre_oss_affiliation",
                "claim_text": "Thomas H. W. Stonborough's immediate pre-OSS affiliation was the Cleveland-area Office of Price Administration, where he was Research Director.",
                "evidence_excerpt": "Previous position was Research Director, Cleveland area, Office of Price Administration",
                "evidence_paraphrase": "The OSS board explicitly identifies this as his previous position when recording his July 1943 OSS entry.",
                "identity_match_assessment": "High confidence from the distinctive name and direct official OSS personnel examination.",
                "temporal_assessment": "Explicit immediate predecessor to OSS entry in July 1943.",
                "source_quality": "A_direct_official",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "The OPA is modeled as a federal government assignment, not a civilian employer.",
                "sources": [{"source_key": HOOVER, "locator_override": "PDF physical page 7; first examination"}],
            },
            {
                "key": "last-civilian-thomas-stonborough-market-research-b920",
                "person_id": PEOPLE[39][0],
                "affiliation_key": "thomas-stonborough-market-research-b920",
                "claim_type": "last_civilian_pre_service",
                "claim_text": "Before his OPA government assignment, Thomas H. W. Stonborough conducted his own market research business.",
                "evidence_excerpt": "prior to that time, he conducted his own market research business",
                "evidence_paraphrase": "The official OSS board sequences self-employed market research before the Cleveland-area OPA role and July 1943 OSS entry.",
                "identity_match_assessment": "High confidence from the distinctive name and direct official OSS personnel examination.",
                "temporal_assessment": "Strongly date-bounded as the last documented civilian work before the intervening OPA government assignment; exact dates are unstated.",
                "source_quality": "A_direct_official",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "The unnamed business is not given an invented firm name and is not mislabeled as the immediate pre-OSS affiliation.",
                "sources": [{"source_key": HOOVER, "locator_override": "PDF physical page 7; first examination"}],
            },
        ]
    )
    return result


def unresolved_update(row: int) -> dict[str, object]:
    person_id, name, box = PEOPLE[row]
    return {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, Box {box} and archive location, but staged NARA/index, CIA Reading Room, exact-name OSS, occupation, employer, obituary, institutional, newspaper, Library of Congress and archival searches found no defensible identity bridge. {UNRESOLVED[row]}",
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
    for item in ARMY_OCCUPATIONS:
        row = int(item["row"])
        person_id, _, box = PEOPLE[row]
        confirmed = row == 32
        updates.append(
            {
                "person_id": person_id,
                "identity_status": "confirmed" if confirmed else "high_confidence",
                "identity_evidence": "A nonshared protected identifier and exact name connect the index row to the official Army record." + (" A separate direct OSS award record names M/Sgt Samuel J. Stolin." if confirmed else " The historical occupation field remains separate from employer and immediate-affiliation claims."),
                "personnel_category": "enlisted_army_personnel",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "occupation_only_found",
                "next_action": f"Review the indexed Box {box} personnel file to identify the immediate pre-OSS affiliation and last civilian employer; do not convert the Army occupation category into a named employer.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            }
        )
    updates.extend(
        [
            {
                "person_id": PEOPLE[26][0],
                "identity_status": "conflicting",
                "identity_evidence": "The protected identifier points to an official Army record named James E Stokes, not indexed James K Stokes. The middle-initial conflict prevents identity, grade, date or occupation transfer.",
                "personnel_category": "unknown_or_indeterminate",
                "manual_review_required": True,
                "research_status": "conflicting_sources",
                "next_action": "Review Box 749 before correcting the identifier or accepting the Army candidate; no reliable pre-OSS employer has yet been identified.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[39][0],
                "identity_status": "high_confidence",
                "identity_evidence": "A direct official OSS board examination names civilian Thomas H. W. Stonborough, dates his OSS entry to July 1943 and supplies the two preceding work stages. The distinctive first and surname match the index; Box 749 should confirm the omitted middle names.",
                "name_variants": ["Thomas H. W. Stonborough"],
                "personnel_category": "civilian_professional_or_administrative_grade",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "verified_employer_found",
                "next_action": "Review Box 749 to confirm the full name and seek the market-research business name and dates; the immediate OPA assignment is already explicit.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "medium",
            },
            {
                "person_id": PEOPLE[44][0],
                "identity_status": "ambiguous",
                "identity_evidence": "This is the first of two adjacent, separately printed Frank D Stone rows. It carries a different protected identifier from the accepted Army-linked second row and remains a separate unresolved person.",
                "personnel_category": "unknown_or_indeterminate",
                "manual_review_required": True,
                "possible_duplicate_group": "same-name:frank-d-stone-page450",
                "research_status": "requires_archival_review",
                "next_action": "Review both Box 750 Frank D Stone files together before merging records or assigning external evidence. No reliable pre-OSS employer has yet been identified for this row.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[45][0],
                "identity_status": "high_confidence",
                "identity_evidence": "A nonshared protected identifier and exact name connect this second Frank D Stone row to the reviewed Army record. The first same-name row carries a different identifier and is not merged. The damaged grade and undefined occupation code are withheld.",
                "personnel_category": "enlisted_army_personnel",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "possible_duplicate_group": "same-name:frank-d-stone-page450",
                "research_status": "requires_archival_review",
                "next_action": "Review both Box 750 Frank D Stone files together to establish distinct full identities and this row's immediate pre-OSS affiliation and last civilian employer.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
        ]
    )
    return updates


def research_attempts() -> list[dict[str, object]]:
    sourced_rows = {25, 26, 27, 30, 32, 34, 35, 39, 40, 45}
    attempts: list[dict[str, object]] = []
    for row, (person_id, name, box) in PEOPLE.items():
        if row in sourced_rows:
            outcome = "source_reviewed"
            if row == 26:
                detail = "The protected-identifier Army candidate was rejected as an identity resolution because its middle initial E conflicts with indexed K."
            elif row == 39:
                detail = "A direct OSS board examination explicitly documented the immediate Cleveland-area OPA assignment and earlier self-employed market research."
            elif row == 45:
                detail = "The second Frank D Stone row has an accepted exact-name Army identity bridge, but its damaged grade and undefined occupation code were not interpreted."
            elif row == 32:
                detail = "The protected-identifier Army bridge and a separate OSS awards-board master-sergeant entry confirm identity; the Army occupation remains qualified and names no employer."
            else:
                detail = "An accepted protected-identifier Army bridge established identity and a dated historical occupation category, not an employer or immediate OSS predecessor."
        elif row == 44:
            outcome = "candidate_rejected"
            detail = "The first Frank D Stone row remains separate because its protected identifier differs from the adjacent Army-linked row; name-only sources cannot be assigned."
        else:
            outcome = "candidate_rejected"
            detail = UNRESOLVED[row]
        loc_rejected = LOC_REJECTIONS.get(row, 0)
        attempts.append(
            {
                "key": f"page450-row{row}-{slug(name)}-b920",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA/index and public Catalog context; CIA Reading Room exact-name check; OSS and rank variants; employer and occupation; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Box {box}; protected-identifier Army crosswalk where defensible",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_920",
                "started_at": "2026-10-26T06:45:00Z",
                "completed_at": "2026-10-26T07:18:00Z",
                "outcome": outcome,
                "sources_reviewed": 13 if row in sourced_rows else 8,
                "candidate_sources_rejected": 5 + loc_rejected,
                "rejection_reasons": "Unbridged namesakes, discovery-only results, wrong initials, OCR/token false positives, postwar-only leads and inaccessible item pages were not assigned." if row in sourced_rows else detail,
                "research_notes": f"{detail} The CIA adapter failed closed on its robots check; separate site-restricted public Reading Room searches covered all 23 names. The current Library of Congress API pass completed for all 23 people, producing 29 candidate pages across eight people; every candidate was individually inspected and rejected. No search snippet was used as final evidence, no access control was bypassed, and no authenticated NARA API call was made.",
                "next_action": f"Review the indexed Box {box} personnel file for corroborating identifiers and the last documented pre-OSS affiliation.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b920-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-920-v1",
        "reviewer": "Before OSS Batch 920 evidence review",
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
