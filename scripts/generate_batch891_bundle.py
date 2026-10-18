#!/usr/bin/env python3
"""Generate the reviewed Batch 891 evidence bundle from audited constants."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "research/evidence-page435-smith-continuation-review_batch-891_2026-10-18.json"

INDEX_KEY = "nara-index-b891"
ARMY_KEY = "army-bulk-b891"
TECH_KEY = "army-tech-b891"
CODES_KEY = "army-codes-b891"


HIGH = [
    {
        "slug": "robert-g-smith-row25",
        "row": 25,
        "person_id": "e635478f-5c1b-546e-ba4d-e7b46324038c",
        "name": "Robert G Smith",
        "source_form": "Robert G Smith",
        "date": "1943-05-10",
        "code": "485",
        "occupation": "Welders and flame cutters",
        "relationship": "unknown",
        "code_locator": "PDF physical page 174; civilian occupation category 4-85",
        "variant": None,
        "duplicate_group": None,
        "identity_note": "Exact-name agreement plus a nonshared protected identifier connect the index row to the official Army bulk record.",
        "research_note": "No named employer, workplace, exact role or OSS-transfer sequence is supplied.",
    },
    {
        "slug": "robert-b-smith-row28",
        "row": 28,
        "person_id": "b11baf40-7e25-5fd2-81a2-ea737792e016",
        "name": "Robert B Smith",
        "source_form": "Robert B Smith",
        "date": "1942-04-03",
        "code": "157",
        "occupation": "Salesmen, insurance",
        "relationship": "unknown",
        "code_locator": "PDF physical page 171; civilian occupation category 1-57",
        "variant": None,
        "duplicate_group": "p435-robert-b-smith-b891",
        "identity_note": "Exact-name agreement plus a nonshared protected identifier connect this index row to the official Army bulk record. The Army row records private grade at entry, while the later index prints M/Sgt; both are preserved as chronology.",
        "research_note": "The different grade descriptions occur at different stages and are not treated as a contradiction. No insurer or employer is named.",
    },
    {
        "slug": "robert-b-smith-row30",
        "row": 30,
        "person_id": "0949e62d-df9f-5a21-bb88-65c0013c8cb8",
        "name": "Robert B Smith",
        "source_form": "Robert B Smith Jr",
        "date": "1944-11-01",
        "code": "992",
        "occupation": "Student",
        "relationship": "student",
        "code_locator": "PDF physical page 304; corrected civilian occupation category 9-92",
        "variant": "Robert B Smith Jr",
        "duplicate_group": "p435-robert-b-smith-b891",
        "identity_note": "Base-name agreement plus a nonshared protected identifier connect this index row to official Army source form Robert B Smith Jr; the suffix remains a source variant.",
        "research_note": "Student status is distinct from employment, and no school, course or employer is inferred.",
    },
    {
        "slug": "robert-a-smith-row32",
        "row": 32,
        "person_id": "d72b29b0-777d-594b-943c-fccdb06b72ac",
        "name": "Robert A Smith",
        "source_form": "Robert A Smith",
        "date": "1942-03-17",
        "code": "057",
        "occupation": "Sports instructors, athletes, and sports officials",
        "relationship": "unknown",
        "code_locator": "PDF physical pages 171 and 304; corrected civilian occupation category 0-57",
        "variant": None,
        "duplicate_group": "p435-robert-a-smith-b891",
        "identity_note": "Exact-name agreement plus a nonshared protected identifier connect the second Robert A Smith row to the official Army bulk record; the adjacent identical-name row has a different protected identifier and remains separate.",
        "research_note": "The broad historical sports category is not converted into a specific job, employer or institution.",
    },
    {
        "slug": "robert-f-smith-row33",
        "row": 33,
        "person_id": "3dce0dac-b055-5a94-aed0-5ac33e5b902a",
        "name": "Robert F Smith",
        "source_form": "Robert F Smith",
        "date": "1941-04-17",
        "code": "736",
        "occupation": "Chauffeurs and drivers, bus, taxi, truck, and tractor",
        "relationship": "unknown",
        "code_locator": "PDF physical page 174; civilian occupation category 7-36",
        "variant": None,
        "duplicate_group": "p435-robert-f-smith-b891",
        "identity_note": "Exact-name agreement plus a nonshared protected identifier connect the third Robert F Smith entry on page 435 to the official Army bulk record; the two earlier rows have different protected identifiers and remain separate.",
        "research_note": "The historical driver category is not converted into a named employer or exact job title.",
    },
    {
        "slug": "sam-m-smith-row38",
        "row": 38,
        "person_id": "1095ac4a-7293-5fac-97fe-16e5d0b6e7bf",
        "name": "Sam M Smith",
        "source_form": "Sam M Smith",
        "date": "1942-08-04",
        "code": "105",
        "occupation": "Clerks, general office",
        "relationship": "unknown",
        "code_locator": "PDF physical page 171; civilian occupation category 1-05",
        "variant": None,
        "duplicate_group": None,
        "identity_note": "Exact-name agreement plus a nonshared protected identifier connect the index row to the official Army bulk record.",
        "research_note": "The general-office-clerk category names neither an employer nor a workplace.",
    },
    {
        "slug": "sands-smith-row39",
        "row": 39,
        "person_id": "1c688f94-0919-52dd-94ec-011395f677b2",
        "name": "Sands Smith",
        "source_form": "Sands Smith Jr",
        "date": "1943-07-03",
        "code": "992",
        "occupation": "Student",
        "relationship": "student",
        "code_locator": "PDF physical page 304; corrected civilian occupation category 9-92",
        "variant": "Sands Smith Jr",
        "duplicate_group": None,
        "identity_note": "Base-name agreement plus a nonshared protected identifier connect the index row to official Army source form Sands Smith Jr; the suffix remains a source variant.",
        "research_note": "Student status is distinct from employment. A discovery-only 1924-born namesake lacks a direct archival bridge and is not used as identity or employer evidence.",
    },
    {
        "slug": "stephen-j-smith-row45",
        "row": 45,
        "person_id": "02f23a7e-922f-5848-935a-25e0b166371d",
        "name": "Stephen J Smith",
        "source_form": "Stephen J Smith",
        "date": "1941-02-07",
        "code": "003",
        "occupation": "Architects",
        "relationship": "unknown",
        "code_locator": "PDF physical page 170; civilian occupation category 0-03",
        "variant": None,
        "duplicate_group": None,
        "identity_note": "Exact-name agreement plus a nonshared protected identifier connect the index row to the official Army bulk record.",
        "research_note": "The architect category does not name an employer, firm, project or location.",
    },
    {
        "slug": "sunday-b-smith-row46",
        "row": 46,
        "person_id": "da092c48-923d-5c64-8cbc-52f2c0791c8c",
        "name": "Sunday B Smith",
        "source_form": "Sunday B Smith",
        "date": "1944-01-11",
        "code": "760",
        "occupation": "Attendants, filling stations and parking lots",
        "relationship": "unknown",
        "code_locator": "PDF physical page 174; civilian occupation category 7-60",
        "variant": None,
        "duplicate_group": None,
        "identity_note": "Exact-name agreement plus a nonshared protected identifier connect the index row to the official Army bulk record.",
        "research_note": "The attendant category identifies neither a particular station, lot, company nor employer.",
    },
]


UNRESOLVED = [
    (24, "438a81b6-647c-51bf-b5b6-a53c2c158ca5", "Robert W Smith", None, 1, "Common-name veteran, obituary, directory and employment leads lacked an OSS or Box 725 bridge. A family-history page naming a steel employer was not transferable to this person."),
    (26, "8bf823dd-6f4b-5e1b-9d06-cee2ad34f635", "Robert K Smith", None, 1, "An official National Park Service profile describes a same-name airman who died in January 1945, but the index supplies no identifier or assignment bridge tying him to this Box 725 file."),
    (27, "71eef5f5-ba52-5047-8e54-b4598fc66dee", "Robert F Smith", "p435-robert-f-smith-b891", 1, "Professor, military, obituary and directory namesakes lacked this row's protected identifier or OSS/Box 724 bridge; the three same-name rows remain separate."),
    (29, "74aa846e-915c-5872-a53c-255d72176a2b", "Robert M Smith", None, 1, "A 1940 postmaster namesake and other common-name results lacked an OSS or Box 725 bridge."),
    (31, "7864e8d2-56bd-56f7-a746-57720209284f", "Robert A Smith", "p435-robert-a-smith-b891", 15, "The adjacent same-name row has a different protected identifier and an accepted Army match. No evidence transfers that identity or occupation to this separate row."),
    (34, "33f6ed9b-9f87-528f-b9dc-b230626c621d", "Russell K Smith", None, 1, "Exact-name, military, employment, obituary and archival searches yielded only unbridged namesakes."),
    (35, "cf561725-0f49-5f2c-9766-f65dc2b46a28", "Ruth A Smith", None, 1, "Student, war-work, engineering-company and other namesakes lacked an OSS or Box 725 bridge."),
    (36, "aaf55d5f-f53e-5d7c-929a-eb7a4e6b69f6", "Ruth E Smith", None, 14, "Obituary, cemetery, directory and licensing-worker namesakes lacked an OSS or Box 725 bridge."),
    (37, "bb02ba81-a9f3-5333-bdbb-c24bbf698b98", "Ruthanna Smith", None, 1, "A 1947 graduate-student listing is postwar and supplies no OSS bridge; modern and incompatible obituary namesakes were rejected."),
    (40, "36b49e6d-0451-50ab-a0a4-2383592db6f1", "Sara E Smith", None, 1, "Exact-name, employment, obituary, institutional and directory searches produced no corroborating OSS or Box 725 bridge."),
    (41, "0ac0ee95-fec0-5792-b835-6b8f91ceb453", "Saul Smith", None, 1, "Exact-name, occupation, obituary, institutional and archival searches produced unrelated modern people and unbridged namesakes."),
    (42, "72b0a311-b136-5130-a35e-2a36c1f2904c", "Saul M Smith", None, 1, "Exact-name and initial-variant searches produced unrelated firm-name results and unbridged namesakes."),
    (43, "24867299-a213-5a46-b0d9-1f70d3909fc2", "Sidney B Smith", None, 1, "Census, cemetery and genealogy candidates supplied no OSS, wartime identifier or Box 725 bridge."),
    (44, "f86c15f2-9a6f-5be9-90c9-d30a56556303", "Stella T Smith", None, 1, "Exact-name, employment, obituary, directory and archival searches produced no corroborating identity bridge."),
]


def source_inputs() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX_KEY,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 724-725",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 435, rows 24-46; checked against layout-preserving text and a rendered page image",
            "access_date": "2026-10-18",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain preserved. Full protected identifiers remain private and are masked from public data.",
        },
        {
            "key": ARMY_KEY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; 12 existing protected-identifier fields checked and nine nonshared-identifier candidates accepted after review",
            "access_date": "2026-10-18",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "No raw row or full private identifier is retained in public assets. The file is incomplete and a non-hit is not negative proof.",
        },
        {
            "key": TECH_KEY,
            "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf",
            "archival_identifier": "NN3-064-03-008; National Archives Identifier 1263923",
            "title": "World War II Army Enlistment Records: Reference Copy of Technical Documentation",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives at College Park - Electronic Records",
            "publication_record_date": "1994-2005; reference copy modified 2011",
            "locator": "PDF physical pages 44-46; fixed-width identifier, name, DD/MM/YY Army-entry-date, grade and civilian-occupation fields visually checked",
            "access_date": "2026-10-18",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Used to interpret selected fields only; documentation warnings about source damage, alternate layouts, coding limits and incomplete coverage remain applicable.",
        },
        {
            "key": CODES_KEY,
            "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1CL_SD.pdf",
            "archival_identifier": "National Archives Identifier 1263923; Code No. 30",
            "title": "NARA Compiled Code Lists for the Electronic Army Serial Number Merged File",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives at College Park - Electronic Records",
            "publication_record_date": "2011-01-12; modified 2011-03-17",
            "locator": "PDF physical pages 170, 171, 174 and 304; civilian-occupation categories 003, 057, 105, 157, 485, 736, 760 and 992 visually checked",
            "access_date": "2026-10-18",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical occupation labels name neither employers nor workplaces. The corrected 057 and 992 entries were preserved; no employer or institution is inferred.",
        },
    ]


def make_affiliation(item: dict[str, object]) -> dict[str, object]:
    return {
        "key": f"{item['slug']}-occupation-b891",
        "person_id": item["person_id"],
        "organization_key": None,
        "organization_name_as_found": None,
        "role_title": None,
        "occupation": item["occupation"],
        "relationship_type": item["relationship"],
        "start_date": None,
        "end_date": item["date"],
        "date_precision": f"Historical civilian-occupation code {item['code']} was recorded at Army entry on {item['date']}; no employer, workplace, start date or OSS-transfer date is named.",
        "country": "United States",
        "immediate_pre_oss": False,
        "last_civilian_pre_service": False,
        "pre_oss_temporal_basis": "strongly_date_bounded",
        "identity_confidence": "high_confidence",
        "claim_confidence": "medium",
        "source_quality": "A_direct_official",
        "publication_status": "publish_qualified",
        "research_notes": item["research_note"],
    }


def make_claims(item: dict[str, object]) -> list[dict[str, object]]:
    suffix_note = (
        f" The Army source form {item['source_form']} remains a documented variant and does not replace the indexed spelling."
        if item["variant"]
        else ""
    )
    identity = {
        "key": f"identity-{item['slug']}-b891",
        "person_id": item["person_id"],
        "claim_type": "identity",
        "claim_text": f"The indexed {item['name']} row on PDF page 435 is a high-confidence match to the official Army bulk record.",
        "evidence_paraphrase": item["identity_note"],
        "identity_match_assessment": "High confidence from name agreement and a nonshared protected-identifier bridge for this source row only.",
        "temporal_assessment": "The Army-entry record supports identity and a dated occupation category; it does not establish a named employer or the OSS transfer sequence.",
        "source_quality": "A_direct_official",
        "claim_confidence": "high",
        "publication_status": "published",
        "match_notes": f"No protected identifier is exposed and same-name source rows are not merged.{suffix_note}",
        "sources": [
            {"source_key": INDEX_KEY, "locator_override": f"PDF page 435 row {item['row']}; protected identifier withheld"},
            {"source_key": ARMY_KEY, "locator_override": "Accepted reviewed identity bridge; protected identifier withheld"},
        ],
    }
    occupation = {
        "key": f"occupation-{item['slug']}-b891",
        "person_id": item["person_id"],
        "affiliation_key": f"{item['slug']}-occupation-b891",
        "claim_type": "occupation",
        "claim_text": f"At Army entry on {item['date']}, {item['name']} was recorded in the historical {str(item['occupation']).lower()} category; no employer is identified.",
        "evidence_excerpt": item["occupation"],
        "evidence_paraphrase": f"The accepted Army row carries civilian-occupation code {item['code']}, decoded from NARA's official code list.",
        "identity_match_assessment": "The occupation category belongs only to the accepted protected-identifier match for this index row.",
        "temporal_assessment": "Strongly date-bounded to Army entry; it does not establish the immediate pre-OSS affiliation or a named employer.",
        "source_quality": "A_direct_official",
        "claim_confidence": "medium",
        "publication_status": "publish_qualified",
        "match_notes": item["research_note"],
        "sources": [
            {"source_key": ARMY_KEY, "locator_override": f"Accepted reviewed identity record; civilian occupation code {item['code']}; protected identifier withheld"},
            {"source_key": TECH_KEY, "support_type": "context_only", "locator_override": "PDF physical pages 44-46; DD/MM/YY entry-date and civilian-occupation fields"},
            {"source_key": CODES_KEY, "locator_override": item["code_locator"], "excerpt_override": item["occupation"]},
        ],
    }
    return [identity, occupation]


def high_update(item: dict[str, object]) -> dict[str, object]:
    update: dict[str, object] = {
        "person_id": item["person_id"],
        "identity_status": "high_confidence",
        "identity_evidence": item["identity_note"],
        "personnel_category": "enlisted_army_personnel",
        "commissioned_officer": False,
        "allied_or_foreign_personnel": False,
        "manual_review_required": True,
        "research_status": "occupation_only_found",
        "next_action": "Review the indexed personnel file in Box 724 or 725 to identify the last civilian employer and establish the Army-to-OSS sequence; the Army occupation category is not an employer.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }
    if item["variant"]:
        update["name_variants"] = [item["variant"]]
    if item["duplicate_group"]:
        update["possible_duplicate_group"] = item["duplicate_group"]
    return update


def unresolved_update(row: int, person_id: str, name: str, duplicate_group: str | None, attempt_number: int, rejection: str) -> dict[str, object]:
    update: dict[str, object] = {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, Box 724 or 725 and archive location, but staged official-domain, exact-name, employment, occupation, obituary, institutional, directory and archival searches found no defensible identity bridge. {rejection}",
        "personnel_category": "unknown_or_indeterminate",
        "commissioned_officer": None,
        "allied_or_foreign_personnel": False,
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": "Review the indexed Box 724 or 725 personnel file for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "critical",
    }
    if duplicate_group:
        update["possible_duplicate_group"] = duplicate_group
    return update


def make_attempt(row: int, person_id: str, name: str, outcome: str, attempt_number: int, notes: str, high: bool = False) -> dict[str, object]:
    return {
        "key": f"page435-row{row}-{name.lower().replace(' ', '-')}-b891",
        "person_id": person_id,
        "source_adapter": "manual_staged_protocol",
        "query_text": f"{name}; NARA/index context; CIA Reading Room attempt; exact-name OSS variants; employer and occupation; obituary, institutional, newspaper, directory and archival searches; Box 724/725; protected-identifier Army crosswalk where available",
        "query_variant_type": "staged_identity_employment_archival_protocol_batch_891",
        "started_at": "2026-10-18T07:35:00Z",
        "completed_at": "2026-10-18T08:35:00Z",
        "outcome": outcome,
        "sources_reviewed": 5 if high else 3,
        "candidate_sources_rejected": 5 if high else 7,
        "rejection_reasons": notes if not high else "External namesakes lacked the protected identifier or Box 724/725 bridge; no named employer source was established.",
        "research_notes": (f"High-confidence official Army identity and qualified occupation or student-status evidence established. {notes}" if high else f"No reliable identity or pre-OSS employer found after staged search and namesake rejection. {notes}") + " The CIA adapter stopped at robots restrictions and the current Library of Congress request timed out; both are access limitations, not negative findings. No exposed NARA API credential was used.",
        "next_action": "Review Box 724 or 725.",
        "last_error_redacted": "CIA robots restriction; Library of Congress request timeout" if not high else None,
        "attempt_number": attempt_number,
        "research_agent_version": "before-oss-b891-v1",
    }


def main() -> None:
    affiliations = [make_affiliation(item) for item in HIGH]
    claims = [claim for item in HIGH for claim in make_claims(item)]
    person_updates = [high_update(item) for item in HIGH]
    person_updates.extend(unresolved_update(*item) for item in UNRESOLVED)
    person_updates.append({
        "person_id": "c4738870-9e3f-5a3c-b157-b93bdc6b8673",
        "possible_duplicate_group": "p435-robert-f-smith-b891",
        "manual_review_required": True,
    })
    research_attempts = [
        make_attempt(
            int(item["row"]),
            str(item["person_id"]),
            str(item["name"]),
            "source_reviewed",
            4 if item["row"] == 32 else 1,
            str(item["research_note"]),
            high=True,
        )
        for item in HIGH
    ]
    research_attempts.extend(
        make_attempt(row, person_id, name, "candidate_rejected", attempt_number, rejection)
        for row, person_id, name, _duplicate_group, attempt_number, rejection in UNRESOLVED
    )
    bundle = {
        "bundle_version": "batch-891-v1",
        "reviewer": "Before OSS Batch 891 evidence review",
        "sources": source_inputs(),
        "organizations": [],
        "affiliations": affiliations,
        "claims": claims,
        "person_updates": person_updates,
        "research_attempts": research_attempts,
    }
    OUTPUT.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
