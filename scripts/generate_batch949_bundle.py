#!/usr/bin/env python3
"""Generate the reviewed Batch 949 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page465-robert-thomale-to-josephine-thomas-"
    "review_batch-949_2026-10-28.json"
)

INDEX = "nara-index-b949"
ARMY = "army-bulk-b949"
TECH = "army-tech-b949"
CODES = "army-codes-b949"
NPS_THOMAS = "nps-allison-thomas-b949"
MSU_THOMAS = "msu-allison-thomas-b949"
US_ARMY = "us-army-existing-b949"


PEOPLE = {
    1: ("a2237c45-cf09-5527-93f5-e8a28fa480b1", "Robert Thomale"),
    2: ("eb722592-1737-570a-8c5d-d53d223cc31d", "Anthony Thomann"),
    3: ("9ec3b452-168a-58d2-bf07-717405f8432f", "Anton C Thomann"),
    4: ("848cbc0c-de59-53c2-971f-59d1550b4bf0", "Albert Thomas"),
    5: ("b7f0c3a4-816e-5d51-9ae4-ca5de1cea3a7", "Alfred B Thomas"),
    6: ("4b6ce778-ca66-5bab-bead-6092f597e135", "Allison K Thomas"),
    7: ("327b7145-da3a-5e1c-8f03-97cfb7d52c43", "Annie B Thomas"),
    8: ("1f065e09-e3b8-5832-8b92-150d3fa2ecb6", "Christopher G Thomas"),
    9: ("fea54bf1-c0f0-5a5c-8efb-d804746fedbd", "Clinton F Thomas"),
    10: ("8012bd97-b9ab-5104-b534-426bc75adab4", "Cynthia M Thomas"),
    11: ("21853702-bc6d-500c-a4ae-739c01fc2c85", "Edward G Thomas"),
    12: ("e398bf65-febf-5a08-95a2-03748594a270", "Francis L Thomas"),
    13: ("3da7dfb8-29bf-5862-8f30-8a94ebf2a33a", "G W Thomas"),
    14: ("53563a1b-63ec-514a-812d-8772c3303a50", "George W Thomas"),
    15: ("19247a68-3dd0-5808-b4de-18a98415f82a", "Gertrude M Thomas"),
    16: ("71805a05-515c-50ed-88e8-96d6c8bc7b2b", "Gregory Thomas"),
    17: ("abd10a7f-9aa1-5912-8227-287c708d7e6a", "Helen E Thomas"),
    18: ("82a29dd8-abaf-597a-95ca-a3ebcf4bd01e", "Hugh R Thomas"),
    19: ("6351a088-3a21-5bd4-9386-c23593aef8fb", "James A Thomas"),
    20: ("f1d18087-0244-5533-af39-2747203f7117", "Jean Thomas"),
    21: ("77cd18a4-d48a-5460-bc8b-ee359f58b1fc", "John L Thomas"),
    22: ("80feec29-4005-5aea-af35-fef831dbc9cc", "Joseph E Thomas"),
    23: ("2111bd68-1f04-59f8-9753-708774f5be42", "Josephine Thomas"),
}


ARMY_RECORDS = [
    {"row": 2, "date": "1942-07-17", "code": "101", "occupation": "bookkeepers and cashiers, except bank cashiers", "label": "Bookkeepers and cashiers, except bank cashiers", "locator": "PDF physical page 171; historical category 1-01"},
    {"row": 3, "date": "1941-12-19", "code": "781", "occupation": "motor-vehicle mechanic or repairman", "label": "Mechanics and repairmen, motor vehicle", "locator": "PDF physical page 175; historical category 7-81"},
    {"row": 4, "date": "1945-10-31", "code": "345", "occupation": None, "label": None, "locator": None},
    {"row": 8, "date": "1942-06-01", "code": "072", "occupation": "retail manager", "label": "Retail managers", "locator": "PDF physical page 171; historical category 0-72"},
    {"row": 11, "date": "1945-03-16", "code": "525", "occupation": "carpenter", "label": "Carpenters", "locator": "PDF physical page 174; historical category 5-25"},
    {"row": 12, "date": "1945-11-07", "code": "070", "occupation": None, "label": None, "locator": None},
    {"row": 19, "date": "1942-11-18", "code": "226", "occupation": "cook, except private family", "label": "Cooks, except private family", "locator": "PDF physical page 172; historical category 2-26"},
]


UNRESOLVED = {
    1: "The indexed protected identifier produced no Army bulk match, and exact-name searches did not establish a defensible OSS identity or pre-OSS affiliation.",
    5: "Common-name results lacked an OSS, Box 773 or protected-identifier bridge and did not establish a pre-OSS employer.",
    7: "Exact-name, institutional, obituary, newspaper and archival searches produced no reliable identity or employer bridge.",
    9: "Exact-name and military searches produced namesakes without a second corroborating identifier or pre-OSS chronology.",
    10: "Exact-name and meaningful-variant searches produced no reliable OSS identity or pre-OSS affiliation.",
    13: "The initial-only indexed name is insufficient to assign any G. W. Thomas biography or employer without the personnel file.",
    14: "The indexed protected identifier produced no Army bulk match, and common-name results could not be bridged to Box 773.",
    15: "Exact-name, institutional, obituary and archival searches produced no defensible identity or pre-OSS affiliation.",
    16: "H. Gregory Thomas OSS records were retained as a rejected namesake lead because the index omits H and supplies no corroborating identifier.",
    17: "The short protected number and common name did not support a unique online identity or employer match.",
    18: "Exact-name and rank-free searches produced multiple namesakes without an OSS or Box-file bridge.",
    20: "The common name produced several unrelated candidates and no corroborating OSS identifier or prewar employer chronology.",
    21: "Common-name military, obituary and directory candidates lacked a protected-identifier or Box 773 bridge.",
    22: "Common-name results did not supply two corroborating identifiers beyond the name or a defensible pre-OSS chronology.",
    23: "Exact-name, obituary, institutional and archival searches produced no reliable identity or employer bridge.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 772-773",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 465, rows 1-23; checked against layout-preserving text and a 220 dpi page render",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. Robert Thomale and Josephine Thomas were visually checked as the cohort boundaries. Full protected identifiers remain private.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; seven reviewed Batch 949 candidates; protected identifiers withheld",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "No raw bulk row or full protected identifier is retained in public assets. Five interpretable categories identify occupations, not employers. Codes 345 and 070 are not assigned in the reviewed official list and are not published as occupations.",
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
            "locator": "PDF physical pages 171-175; reviewed historical categories 0-72, 1-01, 2-26, 5-25 and 7-81",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical occupation labels are qualified and never converted into named employers. Codes 345 and 070 are unassigned in the reviewed official three-digit list and remain uninterpreted.",
        },
        {
            "key": NPS_THOMAS,
            "stable_url": "https://www.nps.gov/articles/oss-in-action-the-pacific-and-the-far-east.htm",
            "title": "OSS in Action: The Pacific and the Far East",
            "author_creator": "National Park Service",
            "repository_publisher": "National Park Service, U.S. Department of the Interior",
            "publication_record_date": "Last updated 2017-08-08",
            "locator": "Section on the Deer Team; paragraph beginning 'The commander was Major Allison K. Thomas'",
            "access_date": "2026-10-28",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "OSS training and operations history",
            "rights_notes": "The institutional history explicitly describes Michigan legal work, Army service and recruitment from the Army by OSS. It names no law firm or employer.",
        },
        {
            "key": MSU_THOMAS,
            "stable_url": "https://archive.lib.msu.edu/uahc/FindingAids/222.html",
            "archival_identifier": "Collection 00222",
            "title": "Major Allison K. Thomas Collection",
            "author_creator": "Michigan State University Archives and Historical Collections",
            "repository_publisher": "Michigan State University Archives and Historical Collections",
            "publication_record_date": "2012-08",
            "locator": "Summary information, biographical note and Box 1 inventory",
            "access_date": "2026-10-28",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Major Allison K. Thomas collection",
            "rights_notes": "Used to corroborate the exact identity, full name, dates and Deer Team role. Its brief biographical note describes the postwar return to law and is not used as proof of a named prewar employer.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [{
        "key": US_ARMY,
        "organization_id": "28a26f92-78af-5a1a-9c09-a843eb5975b4",
        "canonical_name": "United States Army",
        "historical_name": "Army of the United States",
        "aliases": ["U.S. Army"],
        "organization_type": "military service",
        "sector": "military",
        "country": "United States",
        "normalization_notes": "Existing canonical organization reused. Army service is modeled as military assignment, not civilian employment.",
    }]


def occupation_affiliation(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    return {
        "key": f"{slug(PEOPLE[row][1])}-occupation-b949",
        "person_id": PEOPLE[row][0],
        "occupation": item["occupation"],
        "relationship_type": "employment",
        "end_date": item["date"],
        "date_precision": f"Historical civilian-occupation code {item['code']} was recorded at Army entry on {item['date']}; no employer, workplace or OSS-transfer date is named.",
        "country": "United States",
        "immediate_pre_oss": False,
        "last_civilian_pre_service": False,
        "pre_oss_temporal_basis": "strongly_date_bounded",
        "identity_confidence": "high_confidence",
        "claim_confidence": "medium",
        "source_quality": "A_direct_official",
        "publication_status": "publish_qualified",
        "research_notes": "The historical category is not converted into a named employer, workplace, immediate affiliation or exact modern job title.",
    }


def affiliations() -> list[dict[str, object]]:
    values = [occupation_affiliation(item) for item in ARMY_RECORDS if item["occupation"]]
    values.extend([
        {
            "key": "allison-thomas-army-b949",
            "person_id": PEOPLE[6][0],
            "organization_key": US_ARMY,
            "organization_name_as_found": "Army",
            "role_title": "officer; later major",
            "relationship_type": "military_assignment",
            "date_precision": "The National Park Service history states that Thomas joined the Army, became an officer and was recruited from the Army by OSS; exact dates are not supplied.",
            "country": "United States",
            "immediate_pre_oss": True,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "explicit_immediate",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "published",
            "research_notes": "The Army is an explicit predecessor affiliation and is not labeled a civilian employer.",
        },
        {
            "key": "allison-thomas-lawyer-b949",
            "person_id": PEOPLE[6][0],
            "occupation": "lawyer",
            "relationship_type": "employment",
            "date_precision": "The National Park Service history places Michigan legal work before Army entry; no firm, employer or exact dates are named.",
            "state_or_region": "Michigan",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": True,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "high_confidence",
            "claim_confidence": "medium",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "publish_qualified",
            "research_notes": "Published as the best-supported last civilian occupation before Army service. No law firm, employer or self-employment status is inferred.",
        },
    ])
    return values


def claim(row: int, key: str, claim_type: str, text: str, paraphrase: str, identity: str, temporal: str, quality: str, confidence: str, source_links: list[dict[str, object]], notes: str, affiliation_key: str | None = None, publication_status: str | None = None) -> dict[str, object]:
    return {
        "key": key,
        "person_id": PEOPLE[row][0],
        "affiliation_key": affiliation_key,
        "claim_type": claim_type,
        "claim_text": text,
        "evidence_paraphrase": paraphrase,
        "identity_match_assessment": identity,
        "temporal_assessment": temporal,
        "source_quality": quality,
        "claim_confidence": confidence,
        "publication_status": publication_status or ("published" if confidence in {"confirmed", "high"} else "publish_qualified"),
        "match_notes": notes,
        "sources": source_links,
    }


def army_claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for item in ARMY_RECORDS:
        row = int(item["row"])
        name = PEOPLE[row][1]
        post_oss = item["date"] > "1945-09-20"
        values.append(claim(
            row,
            f"identity-{slug(name)}-b949",
            "identity",
            f"The indexed {name} is a high-confidence match to the reviewed official Army record.",
            "A nonshared protected identifier connects the visually verified index row to the official Army record, and the indexed name agrees with the Army form.",
            "High confidence from a private nonshared identifier plus full-name agreement.",
            "The Army record dates entry into service" + (" after OSS dissolution and therefore supports identity only." if post_oss else "; it does not establish the exact OSS transfer date."),
            "A_direct_official",
            "high",
            [
                {"source_key": INDEX, "locator_override": f"PDF page 465 row {row}; protected identifier withheld"},
                {"source_key": ARMY, "locator_override": "Reviewed name record; protected identifier withheld"},
                {"source_key": TECH, "support_type": "context_only", "locator_override": "Field definitions, PDF physical pages 44-46"},
            ],
            "This identity decision does not by itself establish a named employer or immediate OSS predecessor.",
        ))
        if item["occupation"]:
            values.append(claim(
                row,
                f"occupation-{slug(name)}-b949",
                "occupation",
                f"At Army entry on {item['date']}, {name}'s record carried the historical civilian-occupation category {item['label']}; no employer is named.",
                f"The official bulk record supplies code {item['code']}; the visually reviewed NARA code list expands it as {item['label']}.",
                "High confidence from the accepted protected-identifier bridge and name agreement.",
                "Strongly date-bounded at Army entry, but not shown to be the immediate pre-OSS affiliation.",
                "A_direct_official",
                "medium",
                [
                    {"source_key": ARMY, "locator_override": f"Army entry {item['date']}; code {item['code']}; identifier withheld"},
                    {"source_key": CODES, "locator_override": item["locator"]},
                ],
                "Published only as a qualified historical occupation category. No workplace or named employer is inferred.",
                f"{slug(name)}-occupation-b949",
                "publish_qualified",
            ))
    return values


def allison_claims() -> list[dict[str, object]]:
    return [
        claim(6, "identity-allison-thomas-b949", "identity", "Indexed Allison K. Thomas is a high-confidence match to Major Allison Kent Thomas, commander of the OSS Deer Team.", "The exact full name, compatible officer identifier and two institutional histories align with the Deer Team commander.", "High confidence from the distinctive full name, compatible officer context and independent NPS and MSU institutional histories.", "Both institutional histories place him in OSS wartime service; neither source exposes the index identifier.", "B_authoritative_institutional", "high", [{"source_key": INDEX, "locator_override": "PDF page 465 row 6; protected identifier withheld"}, {"source_key": NPS_THOMAS, "locator_override": "Deer Team commander paragraph"}, {"source_key": MSU_THOMAS, "locator_override": "Biographical note and Collection 00222 inventory"}], "The public identity claim masks the indexed officer identifier."),
        claim(6, "immediate-allison-thomas-army-b949", "immediate_pre_oss_affiliation", "Allison K. Thomas's documented immediate pre-OSS affiliation was the United States Army.", "The National Park Service history says that Thomas joined the Army, became an officer and was recruited from the Army by OSS.", "High-confidence distinctive-name identity corroborated by NPS and MSU institutional histories.", "Explicit recruitment-from-Army statement; exact dates are absent.", "B_authoritative_institutional", "high", [{"source_key": NPS_THOMAS, "locator_override": "Deer Team commander paragraph", "excerpt_override": "He joined the Army, became an officer, and ... had been recruited from the Army by OSS."}], "Modeled as a military assignment, not a civilian employer.", "allison-thomas-army-b949"),
        claim(6, "occupation-allison-thomas-lawyer-b949", "last_civilian_pre_service", "Before Army service, Allison K. Thomas worked as a lawyer in Michigan; no employer or firm is named.", "The National Park Service history places his Michigan legal work before Army entry and Army-to-OSS recruitment.", "High-confidence distinctive-name identity corroborated by institutional archives.", "Strongly date-bounded before Army service, but no firm, exact dates or self-employment status are supplied.", "B_authoritative_institutional", "medium", [{"source_key": NPS_THOMAS, "locator_override": "Deer Team commander paragraph", "excerpt_override": "had become a lawyer in Michigan"}, {"source_key": MSU_THOMAS, "support_type": "context_only", "locator_override": "Biographical note; postwar return to Lansing and law"}], "Published as a qualified last civilian occupation, not as a named employer. The MSU summary confirms identity but does not independently settle the prewar legal chronology.", "allison-thomas-lawyer-b949", "publish_qualified"),
    ]


def archival_update(row: int, reason: str) -> dict[str, object]:
    person_id, name = PEOPLE[row]
    box = "772" if row <= 3 else "773"
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
        "archival_review_priority": "high",
    }


def army_update(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    person_id, name = PEOPLE[row]
    update: dict[str, object] = {
        "person_id": person_id,
        "identity_status": "high_confidence",
        "identity_evidence": f"A nonshared protected identifier and name agreement connect the visually verified {name} index row to the reviewed official Army record.",
        "personnel_category": "enlisted_army_personnel",
        "commissioned_officer": False,
        "allied_or_foreign_personnel": False,
        "manual_review_required": True,
        "research_status": "occupation_only_found" if item["occupation"] else "requires_archival_review",
        "next_action": "Review Box 773 to establish the immediate pre-OSS affiliation and named last civilian employer; do not convert the Army category into a workplace." if item["occupation"] else f"Review Box 773 for the pre-OSS affiliation and last civilian employer. The {item['date']} Army record supports identity only, and code {item['code']} remains uninterpreted.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }
    if row == 2:
        update["name_variants"] = ["Anthony W Thomann Jr"]
    return update


def person_updates() -> list[dict[str, object]]:
    values = [archival_update(row, reason) for row, reason in UNRESOLVED.items()]
    values.extend(army_update(item) for item in ARMY_RECORDS)
    values.append({
        "person_id": PEOPLE[6][0],
        "identity_status": "high_confidence",
        "identity_evidence": "The exact full name, compatible officer context and independent National Park Service and Michigan State University archival histories identify Major Allison Kent Thomas of the OSS Deer Team.",
        "name_variants": ["Allison Kent Thomas", "Major Allison K Thomas"],
        "personnel_category": "commissioned_army_officer",
        "commissioned_officer": True,
        "allied_or_foreign_personnel": False,
        "manual_review_required": True,
        "research_status": "occupation_only_found",
        "next_action": "Review Box 773 and contemporary Michigan legal records for a named pre-Army law employer or practice and exact dates. Do not infer self-employment from the occupation alone.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "medium",
    })
    return values


def research_attempts() -> list[dict[str, object]]:
    army_rows = {int(item["row"]) for item in ARMY_RECORDS}
    attempts: list[dict[str, object]] = []
    for row in sorted(PEOPLE):
        person_id, name = PEOPLE[row]
        if row in UNRESOLVED:
            outcome, reviewed, rejected, detail = "no_result", 6, 6, UNRESOLVED[row]
        elif row in army_rows:
            item = next(value for value in ARMY_RECORDS if int(value["row"]) == row)
            outcome, reviewed, rejected = "source_reviewed", 7, 5
            detail = "An accepted protected-identifier Army bridge supports identity" + (" and a dated historical occupation category." if item["occupation"] else "; the post-OSS Army-entry date and unassigned code support no pre-OSS occupation.")
        elif row == 6:
            outcome, reviewed, rejected, detail = "source_reviewed", 10, 5, "NPS and MSU institutional histories establish the Deer Team identity; NPS explicitly documents recruitment from the Army and qualified pre-Army Michigan legal work without naming an employer."
        else:
            raise AssertionError(f"Missing Batch 949 outcome for row {row}")
        attempts.append({
            "key": f"page465-row{row}-{slug(name)}-b949",
            "person_id": person_id,
            "source_adapter": "manual_staged_protocol",
            "query_text": f"{name}; NARA OSS index and public Archives context; CIA Reading Room or equivalent official-source check; exact-name and meaningful variants; OSS and military clues; employer and occupation 1940; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Boxes 772-773; protected identifiers used privately only when defensible",
            "query_variant_type": "staged_identity_employment_archival_protocol_batch_949",
            "started_at": "2026-10-28T15:00:00Z",
            "completed_at": "2026-10-28T17:15:00Z",
            "outcome": outcome,
            "sources_reviewed": reviewed,
            "candidate_sources_rejected": rejected,
            "rejection_reasons": "Unbridged namesakes, search snippets, family-tree assertions, discovery-only pages, modern people-finder results, postwar-only leads and sources without an OSS, protected-identifier or Box-file bridge were not assigned. H. Gregory Thomas was not assigned to the initial-free Gregory Thomas row.",
            "research_notes": f"{detail} The index page and admitted Army, code-list, official or institutional sources were checked where applicable. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA Catalog API call was made.",
            "next_action": "Review the indexed personnel file for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before wartime service.",
            "attempt_number": 1,
            "research_agent_version": "before-oss-b949-v1",
        })
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-949-v1",
        "reviewer": "Before OSS Batch 949 evidence review",
        "sources": sources(),
        "organizations": organizations(),
        "affiliations": affiliations(),
        "claims": army_claims() + allison_claims(),
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }
    EvidenceBundle.model_validate(bundle)
    OUTPUT.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
