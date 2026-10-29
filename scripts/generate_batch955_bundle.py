#!/usr/bin/env python3
"""Generate the reviewed Batch 955 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page468-arthur-m-thurston-to-aaron-l-tietelbaum-"
    "review_batch-955_2026-10-29.json"
)

INDEX = "nara-index-b955"
ARMY = "army-bulk-b955"
TECH = "army-tech-b955"
CODES = "army-codes-b955"
FBI = "fbi-ostrich-b955"
KOREA = "korean-history-db-b955"
FBI_ORG = "fbi-existing-b955"

PEOPLE = {
    1: ("db997c8d-1ca3-5c5d-9485-3df1941a3be8", "Arthur M Thurston"),
    2: ("dc28e0fc-012a-52a2-a3ea-321137395080", "Charles A Thurston"),
    3: ("bac0f088-6372-5119-9a5d-dc481b57e921", "Lois L Tibben"),
    4: ("134dccdb-07cf-53ba-8a6a-5cedb980acee", "Margaret J Tibbetts"),
    5: ("5d5d1a61-c567-5008-b42b-1ed44a218043", "Ralph F Tibbetts"),
    6: ("78238042-cac6-5e6a-8949-e4b89019e48c", "Robert W Tibbetts"),
    7: ("24d45a3d-d48e-55ee-bdab-8e4e7ff516ae", "Richard H Tibbs"),
    8: ("63cf9ad7-a959-57d3-a916-1979f689fb0c", "Stafford Tibbs"),
    9: ("baa17585-db77-5852-a52e-64a0368bddcb", "Edward T Tiche"),
    10: ("01bc7836-0bd1-5168-835a-401413775729", "Kenneth H Tichnell"),
    11: ("e0365f40-d2e7-5b3d-8852-b1b7e56f1831", "William D Ticknor"),
    12: ("07920f04-56ab-5277-9a33-9c27d3edc616", "James M Tidwell"),
    13: ("dc9b365c-a6fb-58dc-9b91-570b391e9e71", "Jane V Tidwell"),
    14: ("6382cde3-d93d-5fee-a566-98fb1e218cfe", "Jane W Tidwell"),
    15: ("21fe8de2-5aab-578c-b21a-2fcdf5f76d02", "William A Tidwell"),
    16: ("70acabb2-5e46-5e5f-8411-0b079ec974e2", "Loren A Tiegland"),
    17: ("5ea910b5-24b0-5df0-b538-d7e10cff8fe7", "Herman F Tierney"),
    18: ("1b15da94-c712-5b6a-ba31-1eb8546aa499", "Joseph E Tierney"),
    # Printed rows 19 and 20 are preserved separately in source_records but
    # cautiously linked to one person because they are exact duplicate rows.
    19: ("a054c154-cd1d-5aa1-97c3-1ead473286d6", "Philip D Tierney"),
    21: ("2c4e7a1c-f734-5b75-8bd0-8aeb2ec0bf4a", "Francis R Tierno"),
    22: ("5aa4fd50-2bbe-5b56-95fc-461ab9766544", "Cornelius Tiers"),
    23: ("c6de9c88-1717-5bcb-891f-8e1706713f00", "Aaron L Tietelbaum"),
}

# The NARA technical documentation defines the six-character entry date as
# DD/MM/YY. These categories describe status or occupation at Army entry and
# do not identify an employer, workplace, or immediate OSS predecessor.
ARMY_IDENTITIES = {
    2: ("1941-05-02", "Architects", "0-03", 170),
    5: ("1944-03-31", "Radio operators", "0-61", 171),
    7: ("1943-05-04", "Lithographers", "4-46", 173),
    12: ("1943-05-29", "Managers and officials, n. e. c.", "0-97", 171),
    18: ("1942-10-16", "Elevator operators", "2-95", 172),
    19: ("1942-09-08", "Salesmen, insurance", "1-57", 171),
    21: ("1940-09-16", "Clerks, general", "1-04", 171),
    22: ("1942-04-13", "Aviators", "0-41", 171),
    23: ("1942-08-10", "Lawyers and judges", "0-22", 171),
}

UNRESOLVED = {
    3: "Exact-name, OSS, employer, occupation, obituary, newspaper and institutional searches produced no defensible Box 777 identity bridge.",
    4: "Exact-name and variant searches produced multiple Margaret Tibbetts namesakes but no second identifier or Box 777 bridge.",
    6: "The common exact name produced several military and obituary namesakes; none supplied two corroborating identifiers beyond the name.",
    8: "Exact-name and initials searches produced no reliable OSS, Box 777, employer or wartime-assignment bridge.",
    9: "The printed Tiche spelling was preserved; Tice variants produced namesakes but no defensible Box 778 linkage.",
    10: "Exact-name, initials, obituary, directory, official-domain and employment searches produced no defensible Box 777 bridge.",
    11: "A postwar trade notice links a William D. Ticknor to OSS and later Commercial Solvents employment, but it does not establish the indexed identity or a pre-OSS employer and was not promoted.",
    13: "Exact-name, middle-initial, obituary, institutional, directory and OSS searches produced no defensible Box 778 identity bridge.",
    14: "Exact-name, middle-initial, obituary, institutional, directory and OSS searches produced no defensible Box 778 identity bridge.",
    15: "A later Army and CIA intelligence officer and historian has the same name, but the accessible sources do not bridge him to Box 778 or establish his immediate pre-OSS affiliation.",
    16: "Exact-name, spelling-variant, obituary, newspaper and institutional searches produced no defensible Box 778 identity bridge.",
    17: "The only protected-identifier Army candidate names Daniel W Summers, a substantive conflict; it was rejected and no facts were transferred to Herman F Tierney.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def archive_box(row: int) -> str:
    return "777" if row <= 8 or row in {10, 11} else "778"


def archive_location(row: int) -> str:
    return "230/86/42/01" if archive_box(row) == "777" else "230/86/42/02"


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 777-778",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 468, rows 1-23; checked against layout-preserving text and a 220 dpi page render",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. Rows 19 and 20 are exact duplicates cautiously linked to one person; full protected identifiers remain private.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; eleven Batch 955 source-row candidates reviewed; identifiers withheld",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "Ten source-row identity leads representing nine people were accepted; one substantive name conflict was rejected. No raw bulk row or full protected identifier enters public assets.",
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
            "access_date": "2026-10-29",
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
            "locator": "PDF physical pages 170-173; nine reviewed historical categories",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical categories are qualified and never converted into named employers, workplaces or exact modern job titles.",
        },
        {
            "key": FBI,
            "stable_url": "https://fbistudies.com/wp-content/uploads/2018/02/OSTRICH-1.pdf",
            "archival_identifier": "FBI file 65-49714-1; OSTRICH; Communication No. 1295",
            "title": "OSTRICH file: Arthur M. Thurston to J. Edgar Hoover",
            "author_creator": "Arthur M. Thurston, Federal Bureau of Investigation",
            "repository_publisher": "Federal Bureau of Investigation document; public scan hosted by FBI Studies",
            "publication_record_date": "1943-08-18",
            "locator": "PDF physical page 76; signed letterhead from the American Embassy, London",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "Declassified Federal Bureau of Investigation records",
            "document_number": "Communication No. 1295",
            "rights_notes": "Only document metadata, a short excerpt and a project-authored paraphrase are retained. The complete scan is not republished.",
        },
        {
            "key": KOREA,
            "stable_url": "https://db.history.go.kr/modern/level.do?levelId=ij_013_$1exp",
            "archival_identifier": "HOI ij_013_$1exp",
            "title": "Korean Liberation Army IV: Explanatory Note",
            "author_creator": "National Institute of Korean History",
            "repository_publisher": "Korean History Database, National Institute of Korean History",
            "locator": "Section 3, 1944-45 OSS China organization; Arthur M Thurston named as lieutenant colonel and X-2 chief",
            "access_date": "2026-10-29",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Documents of the Provisional Government of the Republic of Korea",
            "rights_notes": "The institutional explanatory note identifies its underlying OSS materials as selections from NARA Record Group 226.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": FBI_ORG,
            "organization_id": "e88a4c18-5e0d-58aa-9ed4-787529fac74f",
            "canonical_name": "Federal Bureau of Investigation",
            "historical_name": "Federal Bureau of Investigation",
            "aliases": ["FBI"],
            "organization_type": "federal law-enforcement agency",
            "sector": "federal_government",
            "country": "United States",
            "normalization_notes": "Existing canonical organization reused for documented historical FBI government assignments; it is not classified as a civilian-company employer.",
        }
    ]


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = [
        {
            "key": "fbi-legal-attache-arthur-thurston-b955",
            "person_id": PEOPLE[1][0],
            "organization_key": FBI_ORG,
            "organization_name_as_found": "Federal Bureau of Investigation",
            "role_title": "Legal Attaché, American Embassy, London",
            "relationship_type": "government_assignment",
            "end_date": "1943-08-18",
            "date_precision": "Documented in this assignment on 1943-08-18; beginning and end dates are not established.",
            "city": "London",
            "country": "United Kingdom",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "A_direct_official",
            "publication_status": "publish_qualified",
            "research_notes": "The signed FBI letter establishes a point-in-time government assignment. A separate institutional source places the same distinctive name in OSS/China by July 1945; no source reviewed establishes that the FBI role was the immediate predecessor.",
        }
    ]
    for row, (entry_date, category, code, _page) in ARMY_IDENTITIES.items():
        values.append(
            {
                "key": f"army-category-row{row}-b955",
                "person_id": PEOPLE[row][0],
                "occupation": category.lower(),
                "relationship_type": "employment",
                "end_date": entry_date,
                "date_precision": f"Historical category {code} was recorded at Army entry on {entry_date}; no employer, workplace or OSS-transfer date is named.",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "A_direct_official",
                "publication_status": "publish_qualified",
                "research_notes": "The historical category is not converted into a named employer, workplace, exact specialization or immediate pre-OSS affiliation.",
            }
        )
    return values


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = [
        {
            "key": "identity-arthur-thurston-b955",
            "person_id": PEOPLE[1][0],
            "claim_type": "identity",
            "claim_text": "The indexed Arthur M Thurston is a high-confidence match to Lieutenant Colonel Arthur M. Thurston, X-2 chief in OSS/China by July 1945.",
            "evidence_excerpt": "X-2: Lieutenant Colonel Arthur M Thurston",
            "evidence_paraphrase": "An authoritative institutional account based on NARA RG 226 identifies the distinctive exact-name person as OSS/China's X-2 chief.",
            "identity_match_assessment": "High confidence from distinctive exact full name, middle initial, OSS service and compatible wartime chronology.",
            "temporal_assessment": "The institutional account places Thurston in the OSS/China leadership structure by July 1945.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "The identity bridge supports the documented 1943 FBI assignment but does not establish the date or mechanism of transfer into OSS.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 468 row 1; Box 777; archive location 230/86/42/01; protected identifier withheld"},
                {"source_key": KOREA, "locator_override": "Section 3, OSS/China leadership structure in July 1945"},
            ],
        },
        {
            "key": "fbi-legal-attache-arthur-thurston-claim-b955",
            "person_id": PEOPLE[1][0],
            "affiliation_key": "fbi-legal-attache-arthur-thurston-b955",
            "claim_type": "other_pre_oss_affiliation",
            "claim_text": "Arthur M. Thurston was serving as the FBI legal attaché at the American Embassy in London on August 18, 1943.",
            "evidence_excerpt": "Arthur M. Thurston — Legal Attaché",
            "evidence_paraphrase": "A signed FBI letter on American Embassy London letterhead identifies Thurston as legal attaché on August 18, 1943.",
            "identity_match_assessment": "High confidence from the exact distinctive name, signed official document and independently documented later OSS/China role.",
            "temporal_assessment": "Explicitly dated before the July 1945 OSS/China leadership snapshot; immediacy before OSS is not established.",
            "source_quality": "A_direct_official",
            "claim_confidence": "high",
            "publication_status": "publish_qualified",
            "match_notes": "Published as a documented earlier government assignment, not as a civilian employer or proven immediate OSS predecessor.",
            "sources": [
                {"source_key": FBI, "locator_override": "PDF physical page 76; signed letter dated 1943-08-18"},
                {"source_key": KOREA, "support_type": "context_only", "locator_override": "Section 3, OSS/China leadership structure in July 1945"},
            ],
        },
    ]
    for row, (entry_date, category, code, page) in ARMY_IDENTITIES.items():
        person_id, name = PEOPLE[row]
        identity_note = "A nonshared protected identifier and name agreement connect the visually verified index row to the official Army record."
        identity_assessment = "High confidence from private nonshared identifier agreement and compatible name evidence."
        if row == 22:
            identity_note = "A nonshared protected identifier, exact surname and the fixed-width Army form CORNELI S support the indexed Cornelius spelling; the damaged form remains documented."
            identity_assessment = "High confidence from private nonshared identifier agreement and a transparent one-character split in the fixed-width given-name field."
        values.append(
            {
                "key": f"identity-row{row}-army-b955",
                "person_id": person_id,
                "claim_type": "identity",
                "claim_text": f"The indexed {name} is a high-confidence match to the reviewed official Army record.",
                "evidence_paraphrase": identity_note,
                "identity_match_assessment": identity_assessment,
                "temporal_assessment": "The Army record dates entry into service but does not establish the exact OSS transfer date.",
                "source_quality": "A_direct_official",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "This identity decision does not establish a named employer or immediate OSS predecessor.",
                "sources": [
                    {"source_key": INDEX, "locator_override": f"PDF page 468 row {row}; Box {archive_box(row)}; protected identifier withheld"},
                    {"source_key": ARMY, "locator_override": "Reviewed name record; protected identifier withheld"},
                    {"source_key": TECH, "support_type": "context_only", "locator_override": "Field definitions and DD/MM/YY date format, PDF physical pages 44-46"},
                ],
            }
        )
        values.append(
            {
                "key": f"category-row{row}-army-b955",
                "person_id": person_id,
                "affiliation_key": f"army-category-row{row}-b955",
                "claim_type": "occupation",
                "claim_text": f"At Army entry on {entry_date}, {name} was recorded in the historical {category} category; no employer or workplace is identified.",
                "evidence_excerpt": category,
                "evidence_paraphrase": f"The official bulk record supplies historical code {code}; the visually reviewed NARA code list expands it as {category}.",
                "identity_match_assessment": identity_assessment,
                "temporal_assessment": "Strongly date-bounded at Army entry, but not shown to be the immediate pre-OSS affiliation.",
                "source_quality": "A_direct_official",
                "claim_confidence": "medium",
                "publication_status": "publish_qualified",
                "match_notes": "Published only as a qualified historical category. No employer, workplace or exact modern specialization is inferred.",
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
    priority = "critical" if row == 17 else "high"
    return {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, Box {box} and archive location {archive_location(row)}. {reason}",
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
    evidence = "A nonshared protected identifier and compatible name agreement connect the visually verified index row to the reviewed official Army record."
    if row == 18:
        variants = ["Joseph E Tierney Jr"]
    if row == 22:
        evidence = "A nonshared protected identifier, exact surname and the fixed-width Army form CORNELI S support a high-confidence match; the source-damaged form is not silently normalized into an employer claim."
    return {
        "person_id": PEOPLE[row][0],
        "identity_status": "high_confidence",
        "identity_evidence": evidence,
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
    values.append(
        {
            "person_id": PEOPLE[1][0],
            "identity_status": "high_confidence",
            "identity_evidence": "The distinctive exact name in the index matches a lieutenant colonel documented as OSS/China X-2 chief; a signed 1943 FBI letter supplies compatible earlier chronology.",
            "name_variants": ["Arthur M. Thurston"],
            "personnel_category": "commissioned_army_officer",
            "commissioned_officer": True,
            "allied_or_foreign_personnel": False,
            "manual_review_required": True,
            "research_status": "completed",
            "next_action": "Review Box 777 to establish the exact date and mechanism of transfer from the FBI or any intervening assignment into OSS; do not label the FBI role immediate without direct evidence.",
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
            "archival_review_priority": "high",
        }
    )
    return values


def research_attempts() -> list[dict[str, object]]:
    attempts: list[dict[str, object]] = []
    for row in sorted(PEOPLE):
        person_id, name = PEOPLE[row]
        box = archive_box(row)
        if row == 1:
            outcome = "source_reviewed"
            reviewed = 10
            rejected = 5
            detail = "A signed 1943 FBI legal-attaché letter and an authoritative NARA-RG-226-based account of the July 1945 OSS/China leadership were inspected directly. The earlier government assignment is documented, but immediacy is not."
        elif row in UNRESOLVED:
            outcome = "candidate_rejected" if row in {11, 15, 17} else "no_result"
            reviewed = 7
            rejected = 6
            detail = UNRESOLVED[row]
        elif row in ARMY_IDENTITIES:
            entry_date, category, _code, _page = ARMY_IDENTITIES[row]
            outcome = "source_reviewed"
            reviewed = 8
            rejected = 5
            detail = f"An accepted protected-identifier Army bridge supports identity and a dated historical {category} category at Army entry on {entry_date}, without naming an employer or workplace."
            if row == 22:
                detail += " The fixed-width Army form CORNELI S was retained as source damage and reviewed against the indexed Cornelius spelling."
            if row == 23:
                detail += " A 1945 congressional exhibit also names Aaron L. Tietelbaum as a U.S. Army CIOS investigator, but that wartime assignment was not treated as pre-OSS employment."
        else:
            raise AssertionError(f"Missing Batch 955 outcome for row {row}")
        attempts.append(
            {
                "key": f"page468-row{row}-{slug(name)}-b955",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index and public Archives context; CIA Reading Room or equivalent official-source check; exact-name and meaningful variants; OSS and military clues; employer and occupation 1940; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Box {box}; protected identifiers used privately only when defensible",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_955",
                "started_at": "2026-10-29T02:10:00Z",
                "completed_at": "2026-10-29T04:45:00Z",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search snippets, unsourced genealogy, people-finder pages, modern records, postwar-only leads and sources without an OSS, protected-identifier or Box-file bridge were not assigned. Spelling variants were search aliases only. Differing protected identifiers and substantive name conflicts were rejected.",
                "research_notes": f"{detail} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain, CIA Reading Room-equivalent and Library of Congress searches were checked as applicable. The index page, Army technical documentation and occupation-code pages were inspected directly. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": f"Review Box {box} for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before wartime service.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b955-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-955-v1",
        "reviewer": "Before OSS Batch 955 evidence review",
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
