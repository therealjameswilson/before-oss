#!/usr/bin/env python3
"""Generate the reviewed Batch 1022 evidence bundle for PDF page 512."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page512-william-wolverton-to-william-wood-review_"
    "batch-1022_2026-11-04.json"
)

INDEX = "nara-index-b1022"
ARMY = "army-bulk-b1022"
TECH = "army-tech-b1022"
CODES = "army-codes-b1022"
DUPLICATE_GROUP = "page512-shen-shew-wong-protected-name-conflict"

PEOPLE = {
    1: ("9cf0dcb6-b7d8-5c57-bc2c-9b2c07604fcc", "William H Wolverton Jr.", "850"),
    2: ("df2280f0-1f4d-5ab7-adf8-ba5e76082bf6", "Thomas F Wombacher", "850"),
    3: ("12902f59-4ff1-5834-bd59-fb1662dac126", "William H Womble Jr.", "850"),
    4: ("58b0b6e2-57c3-5f33-9403-579ad73fd5ec", "Benjamin Y.W. Wong", "850"),
    5: ("3e5ad5ac-7a83-58ed-b92c-63e80409a53f", "Fook L Wong", "850"),
    6: ("193cc3c8-3199-5460-a266-11acfbe9fb0e", "Hans J.W. Wong", "850"),
    7: ("eb7cb732-3d2f-5797-8121-5b42ada8d1f4", "Henry P Wong", "850"),
    8: ("52eadd18-6063-5dd3-aaf1-82fbde9d6243", "Pak Hoy Wong", "850"),
    9: ("b112c13f-722d-55c6-ad0f-1eb40e8962d4", "Paul Wong", "850"),
    10: ("72ec1228-3474-592a-9bdd-fc5cb677ce33", "Ping K Wong", "850"),
    11: ("a0f8c55f-c8c4-5e3b-8b45-33cb34318f30", "Raymond T Wong", "850"),
    12: ("a3ac93f1-0d1a-577a-a943-51a44c4b0a2a", "Sam Q Wong", "850"),
    13: ("59e7eeb9-6bc4-516d-b4f2-4e98bee6508e", "Shen T Wong", "850"),
    14: ("51f077a2-c1d2-5504-9917-8b4448140944", "Shew T Wong", "850"),
    15: ("5ed7bc84-4dd0-53cd-8fb1-fc979d7c1338", "Si G Wong", "850"),
    16: ("1bc527a6-46a9-5789-818b-1103bf58eba6", "Yack-tuk Wong", "850"),
    17: ("83d2b7aa-b27c-5c3c-b862-4eff3fb1a440", "David Woo", "850"),
    18: ("3e33786d-9dcc-5f54-bf46-d369454195d7", "Simon P Wooby", "850"),
    19: ("3231314c-5883-55eb-8109-19cf0f9ed908", "Andrew M Wood", "850"),
    20: ("05009f19-3350-5513-bf4c-11a40c140fc4", "Betty H.P. Wood", "850"),
    21: ("050ba9c9-40d4-5aac-8179-dd4ad2e20dbf", "Charles M Wood", "850"),
    22: ("aa641498-37c7-5f21-a4f2-fc112451e049", "Charles R Wood", "850"),
    23: ("ac211295-d5c4-5c85-b784-8c29bf171534", "Eric F Wood", "850"),
    24: ("6532fd47-ac27-5c69-8a79-abf560b72b6f", "G F Wood", "850"),
    25: ("a83ab0a8-523f-5b2b-84ca-34d8d38c0c1f", "Garfield A Wood Jr.", "850"),
    26: ("ef02a95c-4ae7-5363-ac95-e44bea581186", "Helen O Wood", "850"),
    27: ("1f688b42-b13d-5b5c-9e7f-fbb8e243dca8", "Jack G Wood", "850"),
    28: ("1d0d6a8d-ae51-5dab-b4e4-8a47d7d1d74b", "James E Wood", "850"),
    29: ("a2e44d8b-721d-5150-9852-ba85ada1ce12", "James J Wood", "850"),
    30: ("8afa4af6-7fb5-52c3-a1b9-b73466fd0460", "Jeruska S Wood", "850"),
    31: ("d050b758-a141-51c0-8e51-a4806026aac6", "John L Wood", "850"),
    32: ("67adaa44-43a4-5fc3-9a9a-fb3835d1b128", "John S Wood Jr.", "850"),
    33: ("da71f9b2-ad7f-55cd-a204-54c240a3e838", "Leona Wood", "851"),
    34: ("847d16f3-1419-51ea-bc0e-a8ab463a4834", "Louise B Wood", "851"),
    35: ("eaa72e2a-2df7-510c-965c-9f8d923b8372", "Myrtle B Wood", "851"),
    36: ("e29282e1-dd8c-5282-a288-b61bb1d09be0", "Percy S Wood", "851"),
    37: ("233b3b68-abaf-5dfc-b600-66d4430aa0fb", "Philip H Wood", "851"),
    38: ("911121ce-d93f-5b85-aea1-ffed2903b497", "Reuben E Wood", "851"),
    39: ("a877411d-ffbb-5c60-b721-7cb133964279", "Richard Wood", "851"),
    40: ("b804840c-2aaf-5a80-bf47-6eaebdb5c913", "Richard H Wood", "851"),
    41: ("16f5f26d-20ed-555c-a76a-ed0badd42c34", "Richardson K Wood", "851"),
    42: ("9024551d-8067-5e01-b949-2bd19b012acd", "Robert L Wood", "851"),
    43: ("ef392d70-b074-56a3-8d53-6420bffbc7d2", "Thomas M Wood", "851"),
    44: ("4a085c67-97e0-5935-96b3-f944fe1f51ca", "Wallace W Wood", "851"),
    45: ("474608cd-0dc5-55fb-b3aa-d994cb9be7c0", "William B Wood", "851"),
    46: ("a699fb3f-fdb2-5f46-b13f-787bda39291e", "William D Wood", "851"),
}

# Official three-digit categories visually checked in NARA's compiled code list.
# They describe civilian occupation at Army entry, never a named employer.
ARMY_OCCUPATIONS = {
    8: ("1944-02-04", "992", "student", "Students", "PDF physical page 304; amended category 9-92", "student"),
    11: ("1943-02-12", "134", "shipping and receiving clerk", "Shipping and receiving clerks", "PDF physical page 171; historical category 1-34", "unknown"),
    15: ("1943-07-01", "583", "mechanic or repairman, not elsewhere classified", "Repairmen and mechanics, n.e.c.", "PDF physical page 178; historical category 5-83", "unknown"),
    17: ("1941-03-14", "757", "laundering, cleaning, dyeing or apparel-pressing worker", "Cleaning occupations, apparel and other articles", "PDF physical page 176; historical category 7-57", "unknown"),
    18: ("1942-09-23", "530", "steam fitter, gas fitter, or plumber", "Steam fitters, gas fitters, and plumbers", "PDF physical page 178; historical category 5-30", "unknown"),
    37: ("1942-10-06", "105", "general office clerk", "Clerks, general office", "PDF physical page 171; historical category 1-05", "unknown"),
    40: ("1942-12-29", "992", "student", "Students", "PDF physical page 304; amended category 9-92", "student"),
    44: ("1943-11-09", "316", "general farm hand", "Farm hands, general farms", "PDF physical page 172; historical category 3-16", "unknown"),
    46: ("1943-09-09", "180", "salesman to consumers", "Salesmen, to consumers", "PDF physical pages 171 and 247; historical category 1-80", "unknown"),
}

HIGH_CONFIDENCE = {8, 18, 37}
CONFLICT_ROWS = {13, 14}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def source(key: str, source_id: str | None, url: str, title: str, locator: str) -> dict[str, object]:
    value: dict[str, object] = {
        "key": key,
        "stable_url": url,
        "title": title,
        "author_creator": "National Archives and Records Administration",
        "repository_publisher": "National Archives and Records Administration",
        "access_date": "2026-11-04",
        "source_quality": "A_direct_official",
        "locator": locator,
        "collection_name": "Records of the Office of Strategic Services" if key == INDEX else "World War II Army Enlistment Records",
    }
    if source_id:
        value["source_id"] = source_id
    return value


def sources() -> list[dict[str, object]]:
    return [
        source(INDEX, None, "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf", "OSS Personnel Files from Excel", "PDF page 512, rows 1-46; visually checked at 180 dpi; RG 226, Entry A1-224, Boxes 850-851"),
        {
            "key": ARMY,
            "source_id": "cf280d3e-1262-5963-90d7-40ffa66c53a3",
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; six accepted Batch 926 protected-identifier candidates",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "No raw record or full protected identifier is retained in public assets. Coded occupations identify neither employer nor workplace.",
        },
        {
            "key": TECH,
            "source_id": "f24044fe-5fcd-5d78-96d4-25d577e90703",
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
            "source_id": "ace136c1-722a-5af0-a43b-bab53792ae6a",
            "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1CL_SD.pdf",
            "archival_identifier": "National Archives Identifier 1263923; Code No. 30",
            "title": "NARA Compiled Code Lists for the Electronic Army Serial Number Merged File",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives at College Park - Electronic Records",
            "publication_record_date": "2011-01-12; modified 2011-03-17",
            "locator": "PDF physical pages 171, 174-175 and 304; Batch 926 categories visually checked",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical categories identify neither employer, institution nor workplace. Amended labels on physical page 304 are retained.",
        },
    ]


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, _label, _locator, relationship) in ARMY_OCCUPATIONS.items():
        values.append({
            "key": f"{slug(PEOPLE[row][1])}-army-occupation-row{row}-b1022",
            "person_id": PEOPLE[row][0],
            "occupation": occupation,
            "relationship_type": relationship,
            "end_date": date,
            "date_precision": f"Historical civilian-occupation code {code} was recorded at Army entry on {date}; no named employer or institution is supplied.",
            "country": "United States",
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "high_confidence" if row in HIGH_CONFIDENCE else "confirmed",
            "claim_confidence": "medium",
            "source_quality": "A_direct_official",
            "publication_status": "publish_qualified",
            "research_notes": "A broad historical category only. It is not converted into a named employer, school, workplace, or exact OSS-transition date.",
        })
    return values


def make_claim(*, key: str, row: int, claim_type: str, text: str, paraphrase: str, identity: str, temporal: str, confidence: str, publication: str, notes: str, source_links: list[dict[str, str]], affiliation_key: str | None = None) -> dict[str, object]:
    value: dict[str, object] = {
        "key": key,
        "person_id": PEOPLE[row][0],
        "claim_type": claim_type,
        "claim_text": text,
        "evidence_paraphrase": paraphrase,
        "identity_match_assessment": identity,
        "temporal_assessment": temporal,
        "source_quality": "A_direct_official",
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
    for row, (date, code, occupation, label, locator, _relationship) in ARMY_OCCUPATIONS.items():
        name = PEOPLE[row][1]
        high = row in HIGH_CONFIDENCE
        identity_key = f"identity-{slug(name)}-row{row}-b1022"
        affiliation_key = f"{slug(name)}-army-occupation-row{row}-b1022"
        values.append(make_claim(
            key=identity_key,
            row=row,
            claim_type="identity",
            text=f"Indexed {name} is {'a high-confidence match to' if high else 'confirmed as'} the matching Army record.",
            paraphrase="The official index and Army record agree through a nonshared protected identifier and compatible name evidence.",
            identity=("High confidence from a nonshared protected identifier plus distinctive compatible name evidence; the identifier remains private." if high else "Confirmed by a nonshared protected identifier and exact official name agreement; the identifier remains private."),
            temporal="Identity evidence only; Army entry is not treated as an OSS-transition date.",
            confidence="high" if high else "confirmed",
            publication="published",
            notes="The accepted review withholds the full identifier and does not convert Army fields into a named employer.",
            source_links=[
                {"source_key": INDEX, "support_type": "supports", "locator_override": f"PDF page 512, row {row}; Box {PEOPLE[row][2]}"},
                {"source_key": ARMY, "support_type": "supports"},
                {"source_key": TECH, "support_type": "context_only"},
            ],
        ))
        values.append(make_claim(
            key=f"occupation-{slug(name)}-row{row}-b1022",
            row=row,
            affiliation_key=affiliation_key,
            claim_type="occupation",
            text=f"At Army entry on {date}, {name}'s record carried historical civilian-occupation category {code}: {occupation}.",
            paraphrase=f"The official bulk record carries code {code}; NARA's compiled list labels that category '{label}'.",
            identity=("High confidence from protected-identifier agreement and distinctive compatible name evidence." if high else "Confirmed by protected-identifier agreement and exact official name evidence."),
            temporal="Strongly date-bounded at Army entry, but not proof of an immediate predecessor affiliation or an exact OSS start date.",
            confidence="medium",
            publication="publish_qualified",
            notes="A historical category only. It is excluded from verified-employer analytics and never converted into a named employer or institution.",
            source_links=[
                {"source_key": ARMY, "support_type": "supports"},
                {"source_key": TECH, "support_type": "context_only"},
                {"source_key": CODES, "support_type": "supports", "locator_override": locator},
            ],
        ))
    conflict_text = "A protected identifier printed on the Shen T Wong index row leads to an Army name that instead matches the adjacent, separately preserved Shew T Wong row."
    for row in sorted(CONFLICT_ROWS):
        values.append(make_claim(
            key=f"identity-conflict-{slug(PEOPLE[row][1])}-row{row}-b1022",
            row=row,
            claim_type="identity",
            text=f"{PEOPLE[row][1]}'s identity remains conflicting because the protected identifier and Army name point to different adjacent index rows.",
            paraphrase=conflict_text,
            identity="Conflicting: the identifier belongs to the Shen row, while the Army spelling agrees with the separate Shew row. Neither record is merged or assigned the Army occupation.",
            temporal="No chronology or occupation is transferred while identity is unresolved.",
            confidence="conflicting",
            publication="conflicting",
            notes="Both printed rows remain separate and are grouped only for joint archival review of Box 850.",
            source_links=[
                {"source_key": INDEX, "support_type": "supports", "locator_override": f"PDF page 512, row {row}; Box 850"},
                {"source_key": ARMY, "support_type": "contradicts"},
                {"source_key": TECH, "support_type": "context_only"},
            ],
        ))
    return values


def unresolved_reason(row: int) -> str:
    reasons = {
        2: "The protected-identifier Army candidate has a materially different damaged name and is rejected.",
        3: "A 1926-born Navy enlisted namesake conflicts with the indexed captain and is rejected.",
        5: "The official Army bulk comparison produced no identifier match; that nonhit is not evidence against other service.",
        21: "A civilian-pilot-instructor biography lacks a bridge to this OSS index row and remains a rejected lead.",
        25: "The famous Garfield Wood Jr. biography lacks a direct index or personnel-file bridge and is not assigned to this row.",
        28: "A 459th Bomb Group namesake lacks corroborating index identifiers and is rejected.",
        33: "An artist biography lacks an OSS or protected-identifier bridge and is rejected.",
        34: "Competing directory and teaching records cannot be assigned to this common name without Box 851 evidence.",
    }
    if row == 19:
        return "The protected-identifier Army candidate contains an incompatible name and impossible date code; it is rejected entirely."
    return reasons.get(row, "Accessible exact-name, official, OSS, employer, occupation, obituary, institutional, newspaper, directory and archival searches produced no reliable identity-and-affiliation bridge; unbridged namesakes and postwar-only leads were rejected.")


def base_update(row: int, **overrides: object) -> dict[str, object]:
    value: dict[str, object] = {
        "person_id": PEOPLE[row][0],
        "manual_review_required": True,
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }
    value.update(overrides)
    return value


def person_updates() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    special = set(ARMY_OCCUPATIONS) | CONFLICT_ROWS
    for row in sorted(set(PEOPLE) - special):
        reason = unresolved_reason(row)
        values.append(base_update(
            row,
            identity_status="unresolved",
            identity_evidence=f"The visually verified page 512 source preserves {PEOPLE[row][1]} and Box {PEOPLE[row][2]}. {reason}",
            research_status="requires_archival_review",
            archival_review_priority="critical" if row in {2, 3, 19, 25, 34} else "high",
            next_action=f"Review indexed Box {PEOPLE[row][2]} for corroborating identifiers, immediate pre-OSS affiliation and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}",
        ))
    for row in ARMY_OCCUPATIONS:
        values.append(base_update(
            row,
            identity_status="high_confidence" if row in HIGH_CONFIDENCE else "confirmed",
            identity_evidence=("A nonshared protected identifier and distinctive compatible name evidence connect the records; the Army name has a minor spelling or transcription variation and the identifier remains private." if row in HIGH_CONFIDENCE else "A nonshared protected identifier and exact official name agreement connect the index and Army records; the identifier remains private."),
            name_variants=({8: ["Pak Hoy Won", "Wong Pak Hoy"], 18: ["Simon P Wooby", "Simom P Wooby"], 37: ["Philip H Wood", "Phillip H Wood"]}.get(row)),
            replace_name_variants=False,
            personnel_category="enlisted_army_personnel",
            commissioned_officer=False,
            allied_or_foreign_personnel=False,
            research_status="occupation_only_found",
            nara_catalog_id="1263923",
            next_action=f"Review indexed Box {PEOPLE[row][2]} to identify a named employer or institution and establish Army-to-OSS chronology; the bulk record supplies only a historical category at Army entry.",
        ))
    for row in sorted(CONFLICT_ROWS):
        values.append(base_update(
            row,
            identity_status="conflicting",
            identity_evidence="The protected identifier appears on the Shen T Wong row, but the associated Army name instead agrees with the adjacent Shew T Wong row. The two source rows remain separate and neither receives Army occupation evidence.",
            possible_duplicate_group=DUPLICATE_GROUP,
            research_status="conflicting_sources",
            archival_review_priority="critical",
            next_action="Review the Shen T Wong and Shew T Wong folders together in Box 850 to resolve the protected-identifier/name conflict; do not merge them or transfer the Army occupation meanwhile.",
        ))
    if len(values) != 46:
        raise RuntimeError(f"Expected 46 person updates, generated {len(values)}")
    return values


def research_attempts() -> list[dict[str, object]]:
    attempts: list[dict[str, object]] = []
    for row, (person_id, name, box) in PEOPLE.items():
        if row in ARMY_OCCUPATIONS:
            outcome, reviewed, rejected = "source_reviewed", 9, 5
            note = "An accepted official Army bridge supports identity and one qualified historical occupation category at Army entry; it supplies no named employer or exact OSS-transfer date."
        elif row in CONFLICT_ROWS:
            outcome, reviewed, rejected = "source_reviewed", 9, 7
            note = "The protected identifier and Army name point to different adjacent index rows; the conflict remains visible and neither row receives occupation evidence."
        else:
            outcome, reviewed, rejected = "candidate_rejected", 6, 5
            note = unresolved_reason(row)
        attempts.append({
            "key": f"page512-row{row}-{slug(name)}-b1022",
            "person_id": person_id,
            "source_adapter": "manual_staged_protocol",
            "query_text": f"{name}; NARA OSS index context; exact-name and meaningful initial, suffix, punctuation, transliteration and OCR variants; OSS, rank, branch, assignment and protected-identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory and archival searches; indexed Box {box}",
            "query_variant_type": "staged_identity_employment_archival_protocol_batch_1022",
            "started_at": "2026-11-04T12:45:00Z",
            "completed_at": "2026-11-04T18:15:00Z",
            "outcome": outcome,
            "sources_reviewed": reviewed,
            "candidate_sources_rejected": rejected,
            "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, postwar-only leads, famous biographies and sources without an OSS, protected-identifier, rank, unit or personnel-file bridge were rejected. Army categories were not converted into named employers or institutions.",
            "research_notes": f"{note} The official index, exact-name searches, official OSS context and available employer, occupation, obituary, institutional, newspaper, directory and archival leads were reviewed as applicable. Page 512 and every cited NARA code-list page were visually checked. No authenticated NARA Catalog API request was made.",
            "next_action": f"Review indexed Box {box} for corroborating identifiers, immediate pre-OSS affiliation and last civilian employer before wartime service.",
            "attempt_number": 1,
            "research_agent_version": "before-oss-b1022-v1",
        })
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-1022-v1",
        "reviewer": "Before OSS Batch 1022 evidence review",
        "sources": sources(),
        "organizations": [],
        "affiliations": affiliations(),
        "claims": claims(),
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }
    EvidenceBundle.model_validate(bundle)
    OUTPUT.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
