#!/usr/bin/env python3
"""Generate the reviewed Batch 914 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "research/evidence-page447-stenzel-to-stern-review_batch-914_2026-10-25.json"

INDEX = "nara-index-b914"
ARMY = "army-bulk-b914"
TECH = "army-tech-b914"
CODES = "army-codes-b914"

PEOPLE = {
    24: ("e0290893-9d54-54b3-93a0-5ad26c83bab0", "Joachim A Stenzel"),
    25: ("fb1fc5c2-4ba6-59a4-9261-e8e07be58310", "Joseph J Stepaniak"),
    26: ("dc76e348-18c1-5c94-a065-3ba63d564fac", "Chica M Stephens"),
    27: ("56b53769-7e4b-531c-b0e1-086eb15dcd1a", "Edward J Stephens"),
    28: ("4b841b5a-a7a7-58a2-b892-309858539786", "John Stephens"),
    29: ("43b8e4e5-d436-57ed-ad05-5ad83c93a5e6", "Lillian S Stephens"),
    30: ("e37fa599-a281-51c5-800f-c769fc428c08", "Raymond R Stephens"),
    31: ("fd7da39e-45f2-57f4-8dc7-4c680d450f55", "Robert G Stephens"),
    32: ("6ef6c3ce-1283-5548-8023-4f5b3678f5c8", "William R Stephens"),
    33: ("65972bde-7b36-5004-a0f4-c878f0a7e725", "Bernice T Stephenson"),
    34: ("e41f4957-18c0-5c32-ab88-4a772031ba15", "Eleanor F Stephenson"),
    35: ("fe86dc5a-4569-5932-b300-d9a4f1f30b0d", "John H Stephenson"),
    36: ("70eccb43-d69c-52d3-8ef0-baca5b8c1af0", "Otis V Stephenson"),
    37: ("627229bf-03ee-5f9c-b167-c18a0650edc2", "William S Stephenson"),
    38: ("b0ade786-4c0a-50b3-a43a-4d8326d31d23", "Harry J Steppenbacke"),
    39: ("45d40362-ad03-5e1f-bfaf-4e293ea4ea3e", "Henry S Sterling"),
    40: ("e7fbbf6c-9892-5eb8-bb18-603aa8d3a4fc", "Aaron R Stern"),
    41: ("2d895519-5853-52a6-9dcd-0f813e695e6a", "Alfred Stern"),
    42: ("dc4da7b2-2f52-52bc-8094-0645afe65ee5", "Barry Stern"),
    43: ("c19e4bf4-14ed-59fe-8dfd-61fe8affae2c", "David S Stern"),
    44: ("523f18b9-69f4-5186-b64e-4b52ff68343e", "Floyd L Stern"),
    45: ("020c0d6f-48a7-5fcb-8808-4f984d44292a", "Ludwig S Stern"),
    46: ("1002cc50-504e-5d26-a5cd-a09e4b8cd0f0", "Michael F Stern"),
}

OLD_JOACHIM = "603ba0b1-79ee-5431-92de-90365a4ebdc6"
JOACHIM_GROUP = "possible-duplicate:joachim-a-stenzel-page447-rows23-24"
BARRY_GROUP = "shared-identifier:barry-steen-stern"

ARMY_OCCUPATIONS = [
    {"row": 30, "date": "1943-03-09", "code": "232", "occupation": "Barbers, beauticians, and manicurists", "locator": "PDF physical page 172; category 2-32"},
    {"row": 35, "date": "1943-05-13", "code": "402", "occupation": "Skilled occupations in production of bakery products, not elsewhere classified", "locator": "PDF physical page 173; category 4-02"},
    {"row": 40, "date": "1942-08-27", "code": "592", "occupation": "Foremen, manufacturing", "locator": "PDF physical page 175; category 5-92"},
    {"row": 41, "date": "1943-05-12", "code": "736", "occupation": "Semiskilled chauffeurs and drivers, bus, taxi, truck, and tractor", "locator": "PDF physical page 174; category 7-36"},
    {"row": 43, "date": "1942-12-13", "code": "992", "occupation": "Students", "locator": "PDF physical page 304; amended category 9-92"},
    {"row": 44, "date": "1941-04-25", "code": "494", "occupation": "Skilled occupations in fabrication of metal products, not elsewhere classified", "locator": "PDF physical page 174; category 4-94"},
    {"row": 46, "date": "1943-05-03", "code": "137", "occupation": "Stenographers and typists", "locator": "PDF physical pages 171 and 304; category 1-37"},
]

UNRESOLVED = {
    25: "A Smithsonian American Art Museum artist record for a Joseph J. Stepaniak is a plausible namesake lead, but it supplies no OSS identifier, military detail or second person-specific bridge and was not assigned.",
    26: "Exact-name and spelling-variant searches produced no source with a person-specific OSS bridge or dated employment chronology.",
    27: "Common-name results lacked the protected identifier, rank, hometown or another corroborating identifier required for assignment.",
    28: "The incomplete common name could not be distinguished from numerous wartime namesakes.",
    29: "Exact-name, occupation, obituary, directory and archival searches produced no defensible identity bridge.",
    31: "Common-name searches returned incompatible candidates and no source with two corroborating identifiers beyond the name.",
    32: "Exact-name and middle-initial searches produced no reliable pre-OSS affiliation or distinguishing OSS evidence.",
    33: "Exact-name and institutional searches produced no source that established identity or a pre-OSS chronology.",
    34: "Exact-name and employment searches produced no reliable person-specific match.",
    36: "The principal exact-name result described a person born in 1928 and was chronologically incompatible with adult World War II OSS service.",
    37: "Search results were dominated by unrelated Sir William Stephenson material and supplied no bridge to the indexed William S. Stephenson.",
    38: "The rare exact name produced no inspectable source establishing identity, occupation or employer.",
    39: "Common-name searches produced multiple incompatible candidates and no protected-identifier or OSS-assignment bridge.",
    45: "Exact-name, rank, occupation, obituary and archival searches produced no defensible match for the indexed lieutenant.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 744-745",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 447, rows 24-46; checked against layout-preserving text and a rendered page image",
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
            "locator": "Official unrestricted ASNEF.FIN.DAT; seven accepted reviewed Batch 914 identity bridges and one shared-identifier conflict",
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
            "locator": "PDF physical pages 171-175 and 304; categories 137, 232, 402, 494, 592, 736 and amended 992 visually checked",
            "access_date": "2026-10-25",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical labels identify neither employers nor workplaces. The amended table on physical page 304 maps code 992 to Students.",
        },
    ]


def army_affiliation(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    person_id, name = PEOPLE[row]
    is_student = item["code"] == "992"
    return {
        "key": f"{slug(name)}-occupation-b914",
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


def army_claims(item: dict[str, object]) -> list[dict[str, object]]:
    row = int(item["row"])
    person_id, name = PEOPLE[row]
    identity_note = (
        "The Army record adds a Jr suffix absent from the index; the protected identifier and otherwise compatible name support the bridge while both forms remain visible."
        if row == 35
        else "A nonshared protected identifier and compatible name connect the visually verified index row to the official Army record."
    )
    return [
        {
            "key": f"identity-{slug(name)}-b914",
            "person_id": person_id,
            "claim_type": "identity",
            "claim_text": f"The indexed {name} row is a high-confidence match to the reviewed official Army record.",
            "evidence_paraphrase": identity_note,
            "identity_match_assessment": "High confidence from the nonshared protected-identifier bridge and compatible name.",
            "temporal_assessment": "The Army record supports identity and a dated occupation category; it does not establish the OSS transfer sequence.",
            "source_quality": "A_direct_official",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "No protected identifier is exposed, and the coded occupation is kept separate from employer claims.",
            "sources": [
                {"source_key": INDEX, "locator_override": f"PDF page 447 row {row}; protected identifier withheld"},
                {"source_key": ARMY, "locator_override": "Accepted reviewed identity bridge; protected identifier withheld"},
            ],
        },
        {
            "key": f"occupation-{slug(name)}-b914",
            "person_id": person_id,
            "affiliation_key": f"{slug(name)}-occupation-b914",
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
        },
    ]


def accepted_update(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    person_id, _name = PEOPLE[row]
    update: dict[str, object] = {
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
    if row == 35:
        update["identity_evidence"] = "A nonshared protected identifier and otherwise compatible name connect the index row to an Army record that adds Jr; the suffix remains a documented variant rather than a silent correction."
        update["name_variants"] = ["John H Stephenson Jr"]
    return update


def unresolved_update(row: int) -> dict[str, object]:
    person_id, name = PEOPLE[row]
    box = 744 if row <= 42 else 745
    return {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, rank when printed, box and archive location, but staged NARA context, CIA Reading Room, exact-name, occupation, employer, obituary, institutional, newspaper, directory, Library of Congress and archival searches found no defensible identity bridge. {UNRESOLVED[row]}",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": f"Review the indexed Box {box} personnel file for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "critical" if row in {25, 28, 31, 37, 39, 45} else "high",
    }


def person_updates() -> list[dict[str, object]]:
    updates = [accepted_update(item) for item in ARMY_OCCUPATIONS]
    updates.extend(unresolved_update(row) for row in UNRESOLVED)
    updates.extend(
        [
            {
                "person_id": PEOPLE[24][0],
                "identity_status": "ambiguous",
                "identity_evidence": "Page 447 separately prints two Joachim A. Stenzel rows: row 23 has lieutenant rank and one protected identifier, while row 24 has no rank and a different protected identifier. Official interpreter references align more closely with the lieutenant row but do not bridge the second row; neither entity is merged.",
                "manual_review_required": True,
                "possible_duplicate_group": JOACHIM_GROUP,
                "research_status": "needs_identity_review",
                "next_action": "Review both Box 744 Joachim A. Stenzel personnel files together before merging records or assigning the official 1st Lieutenant interpreter material to row 24.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": OLD_JOACHIM,
                "identity_status": "ambiguous",
                "identity_evidence": "Page 447 separately prints two Joachim A. Stenzel rows with different protected identifiers; row 23 is a lieutenant and row 24 has no rank. Official interpreter references are compatible with the lieutenant row but do not establish that the rows represent one person.",
                "manual_review_required": True,
                "possible_duplicate_group": JOACHIM_GROUP,
                "research_status": "requires_archival_review",
                "next_action": "Review both Box 744 Joachim A. Stenzel personnel files together before any merger or transfer of external evidence.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[42][0],
                "identity_status": "conflicting",
                "identity_evidence": "The protected identifier printed for Barry Stern is also printed for the separately preserved Barry Steen row. The official Army record agrees with Stern, but the shared identifier prevents assignment to either entity without joint file review.",
                "manual_review_required": True,
                "possible_duplicate_group": BARRY_GROUP,
                "research_status": "conflicting_sources",
                "next_action": "Review the Barry Stern Box 744 and Barry Steen Box 743 personnel files together; do not transfer Army occupation code 108 or merge the people before the conflict is resolved.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
        ]
    )
    return updates


def research_attempts() -> list[dict[str, object]]:
    accepted_rows = {int(item["row"]) for item in ARMY_OCCUPATIONS}
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        box = 744 if row <= 42 else 745
        if row in accepted_rows:
            outcome = "source_reviewed"
            detail = "A reviewed official Army identity and dated historical occupation category were accepted; no named employer is supplied."
        elif row == 24:
            outcome = "candidate_found"
            detail = "The adjacent lieutenant row and official interpreter references are preserved as a possible-duplicate lead, but different printed identifiers prevent a merger."
        elif row == 42:
            outcome = "candidate_found"
            detail = "The official Army candidate remains conflicting because the protected identifier is shared with separately preserved Barry Steen."
        else:
            outcome = "candidate_rejected"
            detail = UNRESOLVED[row]
        attempts.append(
            {
                "key": f"page447-row{row}-{slug(name)}-b914",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA/index context; CIA Reading Room and Library of Congress official-domain exact-name checks; OSS, rank and spelling variants; employer and occupation; obituary, institutional, newspaper, directory and archival searches; Box {box}; protected-identifier Army crosswalk where available",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_914",
                "started_at": "2026-10-26T00:45:00Z",
                "completed_at": "2026-10-26T01:20:00Z",
                "outcome": outcome,
                "sources_reviewed": 8 if row in accepted_rows or row in {24, 25, 42} else 6,
                "candidate_sources_rejected": 5 if row in accepted_rows else 7,
                "rejection_reasons": "Unbridged namesakes, discovery-only results, chronologically incompatible records and postwar-only material were not assigned." if row in accepted_rows else detail,
                "research_notes": f"{detail} Automated CIA and LoC adapter transport failures remain recorded as errors rather than negative findings; equivalent official-domain checks were completed manually. Search-result snippets were discovery aids only, final claims point to inspectable sources, no access control was bypassed, and no exposed NARA API credential was used.",
                "next_action": f"Review the indexed Box {box} personnel file for corroborating identifiers and the last documented pre-OSS affiliation.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b914-v1",
            }
        )
    return attempts


def main() -> None:
    affiliations = [army_affiliation(item) for item in ARMY_OCCUPATIONS]
    claims: list[dict[str, object]] = []
    for item in ARMY_OCCUPATIONS:
        claims.extend(army_claims(item))
    bundle = {
        "bundle_version": "batch-914-v1",
        "reviewer": "Before OSS Batch 914 evidence review",
        "sources": sources(),
        "organizations": [],
        "affiliations": affiliations,
        "claims": claims,
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }
    OUTPUT.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
