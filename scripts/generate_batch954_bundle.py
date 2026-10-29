#!/usr/bin/env python3
"""Generate the reviewed Batch 954 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page467-george-thornton-to-walter-h-thurn-"
    "review_batch-954_2026-10-28.json"
)

INDEX = "nara-index-b954"
ARMY = "army-bulk-b954"
TECH = "army-tech-b954"
CODES = "army-codes-b954"

PEOPLE = {
    24: ("3eaee07c-ad1f-5aac-9067-80b288358223", "George Thornton"),
    25: ("9813058e-948f-54a1-b531-830fd57520f7", "George D Thornton"),
    26: ("28de3ad1-ac3d-5166-9252-718f74ee763d", "Homer A Thornton"),
    27: ("13adbaaa-c9f4-5a34-9dc7-bec1b035473f", "J R Thornton"),
    28: ("ff67f7bb-616f-595b-aa02-b384b2b07b34", "Steve W Thornton"),
    29: ("6aca7beb-46ce-5804-b46e-fba2731d0582", "Claude G Thorpe"),
    30: ("1329c519-a0c3-5f86-9c7c-77f6d1aaa0f9", "George H Thorpe"),
    31: ("c0ad88ce-8efc-5642-94aa-0b737b50eb48", "Wilbur Thorpe"),
    32: ("50c61c2d-b77b-59c9-b09a-bdb215f5c10b", "Arthur C Thorsen"),
    33: ("3f226327-04e9-5dfd-812d-b00883aabbae", "Randell A Thorsen"),
    34: ("a0872503-1a26-598e-b496-20a238fb327d", "Kent D Thorup"),
    35: ("4313fff7-d9d1-5ac0-9683-f1669e8e4509", "Martin C Thraikill"),
    36: ("997e7660-49ed-5566-988a-aff5457c1624", "Donald S Thrall"),
    37: ("a0498cde-de76-5b25-94b3-c1bfabac856a", "Rastus W Thrasher"),
    38: ("c80601a9-cc7c-5c78-9e4d-e97621314899", "John E Throwbridge"),
    39: ("a943f5da-0fbb-5f23-98ff-3731251fdf9b", "Clellan C Thrower"),
    40: ("8b4a9cd3-97aa-5dc7-92ff-719ace44183c", "Fredrick M Thrower"),
    41: ("6b3ee250-ca60-58ce-8990-e481afd8c743", "Robert Thrun"),
    42: ("73b4c7d4-b77b-50de-aec6-08bea9efcd3d", "Paul H Thunnissen"),
    43: ("eca8027a-3642-5f8f-a3d5-34d14d72805c", "Francis B Thurber"),
    44: ("59151c96-04d4-50f4-ae2e-c8830d29ef03", "John W Thurlow"),
    45: ("3b177db3-fa9f-5558-ac1f-32ed57cf2f2a", "Edwin B Thurman"),
    46: ("ab0cb3f1-9652-57c4-9768-bc6d0d95e43a", "Walter H Thurn"),
}

# The NARA technical documentation defines the six-character entry date as
# DD/MM/YY. These categories describe status or occupation at Army entry and
# do not identify an employer, workplace, or immediate OSS predecessor.
ARMY_IDENTITIES = {
    24: ("1942-12-10", "Students", "9-92", 304, "student"),
    25: ("1945-02-16", "Purchasing agents and buyers, n. e. c.", "0-91", 171, "employment"),
    26: ("1943-10-05", "Architects", "0-03", 170, "employment"),
    30: ("1942-11-21", "Occupations in manufacture of boots and shoes", "6-61", 173, "employment"),
    31: ("1942-09-21", "Construction occupations, n. e. c.", "7-32", 174, "employment"),
    32: ("1941-03-11", "Machine shop and related occupations, n. e. c.", "6-78", 174, "employment"),
    36: ("1942-12-03", "Construction occupations, n. e. c.", "7-32", 174, "employment"),
    37: ("1942-12-16", "General farmers", "3-06", 172, "employment"),
    41: ("1943-06-15", "Lawyers and judges", "0-22", 171, "employment"),
    45: ("1942-09-28", "Salesmen, insurance", "1-57", 171, "employment"),
    46: ("1942-07-01", "Mechanics and repairmen, motor vehicle", "7-81", 175, "employment"),
}

UNRESOLVED = {
    27: "Initials-only exact and variant searches produced no second identifier or Box 776 bridge.",
    28: "The printed six-digit protected number is too short for an exact Army bulk bridge; exact-name searches found only unassignable Steven and Stephen namesakes.",
    29: "Exact-name, OSS, employer, occupation, obituary, newspaper and institutional searches produced no defensible Box 776 identity bridge.",
    33: "The printed Randell spelling was preserved; Randall variants and exact-name searches produced no defensible OSS or Box 776 linkage.",
    34: "Postwar Marine and legal records concern a plausible exact-name person but do not bridge that person to Box 776 or establish a pre-OSS affiliation.",
    35: "The printed Thraikill spelling was preserved; Thrailkill was used only as a search alias and produced no defensible identity or employment evidence.",
    38: "The printed Throwbridge spelling was preserved; Trowbridge variants produced multiple namesakes but no OSS, Box 776 or employment bridge.",
    39: "The printed seven-digit protected number is not eligible for an exact Army bulk bridge; an exact-name Army row carried a different full identifier and was not assigned by name alone.",
    40: "The printed Fredrick spelling was preserved; Frederick variants and official-domain, obituary, directory and employment searches produced no reliable Box 777 bridge.",
    42: "Exact-name, foreign-name, OSS, archival, obituary and institutional searches produced no defensible Box 777 identity bridge.",
    43: "Results were dominated by the nineteenth-century Francis B. Thurber and other namesakes; none bridges the indexed Box 777 person to OSS or pre-OSS employment.",
    44: "A postwar obituary for an Army veteran named John W. Thurlow lacks an OSS, protected-identifier or Box 777 bridge and was rejected as an unassigned namesake.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def archive_box(row: int) -> str:
    return "776" if row <= 38 else "777"


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 776-777",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 467, rows 24-46; checked against layout-preserving text and a 220 dpi page render",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. Rows 24-38 are in Box 776 and rows 39-46 in Box 777. Full protected identifiers remain private.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; eleven Batch 954 protected-identifier candidates reviewed; identifiers withheld",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "Eleven identity links were accepted after exact protected-identifier and name review. No raw bulk row or full protected identifier enters public assets.",
        },
        {
            "key": TECH,
            "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf",
            "archival_identifier": "NN3-064-03-008; National Archives Identifier 1263923",
            "title": "World War II Army Enlistment Records: Reference Copy of Technical Documentation",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives at College Park - Electronic Records",
            "publication_record_date": "1994-2005; reference copy modified 2011",
            "locator": "PDF physical pages 44-46; identifier, name, DD/MM/YY Army-entry-date and civilian-occupation fields",
            "access_date": "2026-10-28",
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
            "locator": "PDF physical pages 170-175 and 304; eleven reviewed historical categories",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical categories are qualified and never converted into named employers, workplaces or exact modern job titles.",
        },
    ]


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (entry_date, category, code, _page, relationship) in ARMY_IDENTITIES.items():
        values.append(
            {
                "key": f"army-category-row{row}-b954",
                "person_id": PEOPLE[row][0],
                "occupation": "student" if relationship == "student" else category.lower(),
                "relationship_type": relationship,
                "end_date": entry_date,
                "date_precision": f"Historical category {code} was recorded at Army entry on {entry_date}; no employer, workplace, school or OSS-transfer date is named.",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "A_direct_official",
                "publication_status": "publish_qualified",
                "research_notes": "The historical category is not converted into a named employer, workplace, school, exact specialization or immediate pre-OSS affiliation.",
            }
        )
    return values


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (entry_date, category, code, page, relationship) in ARMY_IDENTITIES.items():
        person_id, name = PEOPLE[row]
        values.append(
            {
                "key": f"identity-row{row}-army-b954",
                "person_id": person_id,
                "claim_type": "identity",
                "claim_text": f"The indexed {name} is a high-confidence match to the reviewed official Army record.",
                "evidence_paraphrase": "A nonshared protected identifier and name agreement connect the visually verified index row to the official Army record.",
                "identity_match_assessment": "High confidence from private nonshared identifier agreement and compatible name evidence.",
                "temporal_assessment": "The Army record dates entry into service but does not establish the exact OSS transfer date.",
                "source_quality": "A_direct_official",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "This identity decision does not establish a named employer or immediate OSS predecessor.",
                "sources": [
                    {"source_key": INDEX, "locator_override": f"PDF page 467 row {row}; Box {archive_box(row)}; protected identifier withheld"},
                    {"source_key": ARMY, "locator_override": "Reviewed name record; protected identifier withheld"},
                    {"source_key": TECH, "support_type": "context_only", "locator_override": "Field definitions and DD/MM/YY date format, PDF physical pages 44-46"},
                ],
            }
        )
        student = relationship == "student"
        values.append(
            {
                "key": f"category-row{row}-army-b954",
                "person_id": person_id,
                "affiliation_key": f"army-category-row{row}-b954",
                "claim_type": "other_pre_oss_affiliation" if student else "occupation",
                "claim_text": (
                    f"At Army entry on {entry_date}, {name} was recorded in the historical student category; no school or employer is identified."
                    if student
                    else f"At Army entry on {entry_date}, {name} was recorded in the historical {category} category; no employer or workplace is identified."
                ),
                "evidence_excerpt": category,
                "evidence_paraphrase": f"The official bulk record supplies historical code {code}; the visually reviewed NARA code list expands it as {category}.",
                "identity_match_assessment": "High confidence from the accepted protected-identifier bridge and compatible name evidence.",
                "temporal_assessment": "Strongly date-bounded at Army entry, but not shown to be the immediate pre-OSS affiliation.",
                "source_quality": "A_direct_official",
                "claim_confidence": "medium",
                "publication_status": "publish_qualified",
                "match_notes": "Published only as a qualified historical category. No employer, workplace, school or exact modern specialization is inferred.",
                "sources": [
                    {"source_key": ARMY, "locator_override": f"Army entry {entry_date}; historical code {code}; protected identifier withheld"},
                    {"source_key": CODES, "locator_override": f"PDF physical page {page}; historical category {code}"},
                ],
            }
        )
    return values


def archival_update(row: int, reason: str) -> dict[str, object]:
    person_id, name = PEOPLE[row]
    box = archive_box(row)
    priority = "critical" if row == 39 else "high"
    return {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, Box {box} and archive location 230/86/42/01. {reason}",
        "personnel_category": "unknown_or_indeterminate",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": f"Review Box {box} for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": priority,
    }


def army_update(row: int) -> dict[str, object]:
    variants: list[str] | None = None
    if row == 24:
        variants = ["George C Thornton"]
    elif row == 46:
        variants = ["Walter H Thurn Jr"]
    return {
        "person_id": PEOPLE[row][0],
        "identity_status": "high_confidence",
        "identity_evidence": "A nonshared protected identifier and compatible name agreement connect the visually verified index row to the reviewed official Army record.",
        "name_variants": variants,
        "personnel_category": "enlisted_army_personnel",
        "commissioned_officer": False,
        "allied_or_foreign_personnel": False,
        "manual_review_required": True,
        "research_status": "occupation_only_found",
        "next_action": f"Review Box {archive_box(row)} to establish the immediate pre-OSS affiliation and named last civilian employer; do not convert the Army category into a workplace.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }


def person_updates() -> list[dict[str, object]]:
    values = [archival_update(row, reason) for row, reason in UNRESOLVED.items()]
    values.extend(army_update(row) for row in ARMY_IDENTITIES)
    return values


def research_attempts() -> list[dict[str, object]]:
    attempts: list[dict[str, object]] = []
    for row in sorted(PEOPLE):
        person_id, name = PEOPLE[row]
        box = archive_box(row)
        if row in UNRESOLVED:
            outcome = "candidate_rejected" if row in {39, 44} else "no_result"
            reviewed = 7
            rejected = 6
            detail = UNRESOLVED[row]
        elif row in ARMY_IDENTITIES:
            entry_date, category, _code, _page, relationship = ARMY_IDENTITIES[row]
            outcome = "source_reviewed"
            reviewed = 8
            rejected = 5
            if relationship == "student":
                detail = f"An accepted protected-identifier Army bridge supports identity and dated student status at Army entry on {entry_date}, without naming a school or employer."
            else:
                detail = f"An accepted protected-identifier Army bridge supports identity and a dated historical {category} category at Army entry on {entry_date}, without naming an employer or workplace."
            if row == 41:
                detail += " A CIA Reading Room search exposed a specific wartime document naming Robert Thrun, but the direct page redirected to system maintenance during review and was not used as final claim evidence."
        else:
            raise AssertionError(f"Missing Batch 954 outcome for row {row}")
        attempts.append(
            {
                "key": f"page467-row{row}-{slug(name)}-b954",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index and public Archives context; CIA Reading Room or equivalent official-source check; exact-name and meaningful variants; OSS and military clues; employer and occupation 1940; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Box {box}; protected identifiers used privately only when defensible",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_954",
                "started_at": "2026-10-28T22:55:00Z",
                "completed_at": "2026-10-29T04:05:00Z",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search snippets, unsourced genealogy, people-finder pages, modern records, postwar-only leads and sources without an OSS, protected-identifier or Box-file bridge were not assigned. Spelling variants were search aliases only. Short or differing protected numbers were not bridged by name alone.",
                "research_notes": f"{detail} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain, CIA Reading Room-equivalent and Library of Congress searches were checked as applicable. The index page, Army technical documentation and occupation-code pages were inspected directly. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": f"Review Box {box} for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before wartime service.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b954-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-954-v1",
        "reviewer": "Before OSS Batch 954 evidence review",
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
