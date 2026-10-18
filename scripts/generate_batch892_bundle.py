#!/usr/bin/env python3
"""Generate the reviewed Batch 892 evidence bundle from audited constants."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "research/evidence-page436-smith-review_batch-892_2026-10-18.json"

INDEX_KEY = "nara-index-b892"
ARMY_KEY = "army-bulk-b892"
TECH_KEY = "army-tech-b892"
CODES_KEY = "army-codes-b892"
ORDER_KEY = "oss-order-warren-j-smith-b892"


HIGH = [
    {
        "slug": "thomas-j-smith-row2",
        "row": 2,
        "person_id": "05476034-b73b-50ef-a221-b97837fb5fca",
        "name": "Thomas J Smith",
        "source_form": "Thomas J Smith",
        "date": "1942-05-19",
        "code": "736",
        "occupation": "Chauffeurs and drivers, bus, taxi, truck, and tractor",
        "relationship": "unknown",
        "code_locator": "PDF physical page 174; civilian occupation category 7-36",
        "variant": None,
        "duplicate_group": None,
        "identity_note": "Exact-name agreement plus a nonshared protected identifier connect the index row to the official Army bulk record.",
        "research_note": "The historical driver category is not converted into a named employer or exact job title.",
        "order_support": False,
    },
    {
        "slug": "thomas-r-smith-row3",
        "row": 3,
        "person_id": "3c9ff555-1615-5324-b1b6-e25c40aa0e17",
        "name": "Thomas R Smith",
        "source_form": "Thomas R Smith",
        "date": "1943-07-26",
        "code": "031",
        "occupation": "Teachers (secondary school) and principals",
        "relationship": "unknown",
        "code_locator": "PDF physical page 171; civilian occupation category 0-31",
        "variant": None,
        "duplicate_group": "p436-thomas-r-smith-b892",
        "identity_note": "Exact-name agreement plus a nonshared protected identifier connect the first Thomas R Smith row to the official Army bulk record; the other two same-name rows remain separate.",
        "research_note": "The broad historical teacher/principal category names neither an employer nor a school and is not treated as proof of a specific role.",
        "order_support": False,
    },
    {
        "slug": "thomas-r-smith-row4",
        "row": 4,
        "person_id": "e794dbca-f53d-5846-ac82-69643cd2de0f",
        "name": "Thomas R Smith",
        "source_form": "Homas R Smith Jr",
        "date": "1943-04-16",
        "code": "447",
        "occupation": "Photoengravers",
        "relationship": "unknown",
        "code_locator": "PDF physical page 173; civilian occupation category 4-47",
        "variant": "Thomas R Smith Jr",
        "duplicate_group": "p436-thomas-r-smith-b892",
        "identity_note": "A nonshared protected identifier agrees exactly. The damaged Army source form omits the initial T and adds Jr; both discrepancies are documented, and the other two Thomas R Smith rows remain separate.",
        "research_note": "The damaged name is not silently substituted for the indexed spelling, and the historical photoengraver category does not identify an employer.",
        "order_support": False,
    },
    {
        "slug": "thomas-f-smith-row6",
        "row": 6,
        "person_id": "8c2623b6-d26a-52c0-878a-b9194386cff9",
        "name": "Thomas F Smith",
        "source_form": "Thomas F Smith",
        "date": "1943-06-18",
        "code": "992",
        "occupation": "Students",
        "relationship": "student",
        "code_locator": "PDF physical page 304; corrected civilian occupation category 9-92",
        "variant": None,
        "duplicate_group": None,
        "identity_note": "Exact-name agreement plus a nonshared protected identifier connect the index row to the official Army bulk record.",
        "research_note": "Student status is distinct from employment, and no school, course or employer is inferred.",
        "order_support": False,
    },
    {
        "slug": "warren-j-smith-row17",
        "row": 17,
        "person_id": "b4c7ef21-37da-55d7-9fdc-90d0299ce416",
        "name": "Warren J Smith",
        "source_form": "Warren J Smith",
        "date": "1943-08-11",
        "code": "992",
        "occupation": "Students",
        "relationship": "student",
        "code_locator": "PDF physical page 304; corrected civilian occupation category 9-92",
        "variant": None,
        "duplicate_group": None,
        "identity_note": "Exact-name agreement and a nonshared protected identifier connect the index row to the official Army record; an independently released OSS order repeats that identifier and names him as a sergeant in Company B, Special Reconnaissance Battalion, on 9 May 1945.",
        "research_note": "The 1945 order corroborates identity and wartime assignment only. Army-entry student status names no school or employer and is not treated as the immediate OSS predecessor.",
        "order_support": True,
    },
    {
        "slug": "willard-a-smith-row21",
        "row": 21,
        "person_id": "033ce195-83cd-5c62-bd5d-645268a735fc",
        "name": "Willard A Smith",
        "source_form": "Willard A Smith",
        "date": "1942-01-03",
        "code": "031",
        "occupation": "Teachers (secondary school) and principals",
        "relationship": "unknown",
        "code_locator": "PDF physical page 171; civilian occupation category 0-31",
        "variant": None,
        "duplicate_group": None,
        "identity_note": "Exact-name agreement plus a nonshared protected identifier connect the index row to the official Army bulk record.",
        "research_note": "The broad historical teacher/principal category names neither an employer nor a school and is not treated as proof of a specific role.",
        "order_support": False,
    },
    {
        "slug": "william-w-smith-row23",
        "row": 23,
        "person_id": "4cae9929-a8d0-59b7-8f7b-3f2c39f55d74",
        "name": "William W Smith",
        "source_form": "William W Smith",
        "date": "1942-02-10",
        "code": "736",
        "occupation": "Chauffeurs and drivers, bus, taxi, truck, and tractor",
        "relationship": "unknown",
        "code_locator": "PDF physical page 174; civilian occupation category 7-36",
        "variant": None,
        "duplicate_group": None,
        "identity_note": "Exact-name agreement plus a nonshared protected identifier connect the index row to the official Army bulk record.",
        "research_note": "The historical driver category is not converted into a named employer or exact job title. An unbridged Library of Congress oral-history namesake is not used.",
        "order_support": False,
    },
]


UNRESOLVED = [
    (1, "dcc93d54-a060-5bf7-b1c0-1d9124ad7299", "Susan Smith", None, 3, "An official Congressional Record biography of Susan (Smith) Rodriguez describes an OSS Tangier veteran and prewar teaching, but this common-name index row supplies no alias, identifier or assignment bridge; the lead is not assigned."),
    (5, "d5d13d64-00b2-536c-94f6-f00935cc36b7", "Thomas M Smith", None, 1, "The index retains a protected identifier, but the Army bulk file produced no candidate and exact-name searches found no independent OSS or Box 725 bridge. A non-hit is not negative proof."),
    (7, "94c002a2-0d19-505f-8996-46462ad2a93a", "Thomas A Smith", None, 1, "Military, obituary, institutional and employment namesakes lacked an OSS or Box 725 bridge."),
    (8, "bb64788e-1247-50a2-8f5a-c0496897f046", "Thomas R Smith", "p436-thomas-r-smith-b892", 1, "This third same-name row has a different protected identifier and no accepted Army candidate. Evidence from the other two Thomas R Smith rows is not transferred."),
    (9, "b1c65d73-fc8f-519e-a938-918d5a3ccc51", "Turner T Smith", None, 1, "The printed Lieutenant rank supports commissioned-Army classification, but exact-name, obituary, institutional and archival searches did not establish a unique identity or pre-OSS affiliation."),
    (10, "44551848-8a85-5be0-a0a2-6e5f4efbd218", "Vera M Smith", None, 1, "Exact-name, employment, obituary, institutional and archival searches produced only unbridged namesakes."),
    (11, "47bd39c3-4f1c-5acd-a478-23d0bc4cd564", "Vincent R Smith", None, 1, "Military and obituary namesakes, including people with differing middle names or assignments, lacked an OSS or Box 725 bridge."),
    (12, "0492bc5a-30e7-55e6-8fa7-367b195c7cf4", "Vincent P Smith", None, 1, "The protected identifier produced no Army candidate, and exact-name, employment and archival searches found no defensible identity bridge. A non-hit is not negative proof."),
    (13, "7afe8d58-0e2b-5b1e-a59d-b53bd37d49e1", "Virginia K Smith", None, 1, "Exact-name, institutional, obituary, newspaper and archival searches produced only unbridged namesakes."),
    (14, "4ba2b47a-19da-5df3-9d36-4957f151c2af", "Walter Smith", None, 1, "The no-initial name is highly ambiguous; results about General Walter Bedell Smith and numerous other namesakes do not bridge to this Box 725 row."),
    (15, "851304d8-5106-5a3f-a7de-5a92c0a7487d", "Walter M Smith", None, 1, "The printed Captain rank supports commissioned-Army classification. The protected identifier produced no Army candidate, and namesakes lacked an OSS or Box 725 bridge."),
    (16, "c846f651-e6d8-5f65-a725-b1fcb019c602", "Warren D Smith", None, 1, "The sole Army candidate was rejected because its materially different name conflicts with the index despite identifier agreement. No occupation or grade is transferred."),
    (18, "eec8967f-b662-59ad-9979-3eed5928a476", "Warren O Smith", None, 1, "Newspaper, obituary, directory and institutional results lacked an OSS or Box 725 bridge."),
    (19, "4230e29d-43a8-55ce-80c7-159e3cce96d3", "Wilfred A Smith", None, 1, "Directory and historic-property namesakes predated the relevant generation or lacked an OSS and Box 726 bridge."),
    (20, "2b45880b-4e22-5d6a-b043-798f5842b44f", "Wilfred J Smith", None, 1, "The printed Lieutenant Colonel rank supports commissioned-Army classification. The protected identifier produced no Army candidate, and military and obituary namesakes lacked an OSS or Box 726 bridge."),
    (22, "c95a4d6c-44b9-5016-8cec-7d0d75452f98", "William F Smith", None, 1, "The common name returned numerous military, obituary and directory namesakes, none tied to the Box 726 personnel file."),
]


def source_inputs() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX_KEY,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 725-726",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 436, rows 1-23; checked against layout-preserving text and a rendered page image",
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
            "locator": "Official unrestricted ASNEF.FIN.DAT; 13 protected-identifier fields checked, seven candidates accepted and one conflicting-name candidate rejected after review",
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
            "locator": "PDF physical pages 171, 173, 174 and 304; civilian-occupation categories 031, 447, 736 and 992 visually checked",
            "access_date": "2026-10-18",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical occupation labels name neither employers nor workplaces. The corrected 992 entry is preserved; no employer or institution is inferred.",
        },
        {
            "key": ORDER_KEY,
            "stable_url": "https://www.archives.gov/files/research/jfk/releases/2022/104-10165-10121.pdf",
            "archival_identifier": "104-10165-10121",
            "title": "Headquarters, Operational Group Command, Office of Strategic Services, Special Orders Number 9",
            "author_creator": "Headquarters, Operational Group Command, Office of Strategic Services",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1945-05-09",
            "locator": "PDF image 8, original page 2, item 4; Warren J Smith listed among enlisted men assigned to Company B, Special Reconnaissance Battalion",
            "access_date": "2026-10-18",
            "source_quality": "A_direct_official",
            "collection_name": "John F. Kennedy Assassination Records Collection",
            "document_number": "Special Orders Number 9",
            "rights_notes": "Used only to corroborate identity and wartime assignment. The full protected identifier is retained privately and omitted from public text and downloads.",
        },
    ]


def make_affiliation(item: dict[str, object]) -> dict[str, object]:
    return {
        "key": f"{item['slug']}-occupation-b892",
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
    identity_sources = [
        {"source_key": INDEX_KEY, "locator_override": f"PDF page 436 row {item['row']}; protected identifier withheld"},
        {"source_key": ARMY_KEY, "locator_override": "Accepted reviewed identity bridge; protected identifier withheld"},
    ]
    if item["order_support"]:
        identity_sources.append({
            "source_key": ORDER_KEY,
            "locator_override": "PDF image 8, original page 2, item 4; protected identifier withheld",
            "excerpt_override": "Sgt Warren J Smith",
        })
    suffix_note = (
        f" The normalized search variant {item['variant']} preserves the source suffix; the damaged Army spelling itself is documented in the evidence note."
        if item["variant"]
        else ""
    )
    occupation_label = "student" if item["relationship"] == "student" else str(item["occupation"]).lower()
    identity = {
        "key": f"identity-{item['slug']}-b892",
        "person_id": item["person_id"],
        "claim_type": "identity",
        "claim_text": f"The indexed {item['name']} row on PDF page 436 is a high-confidence match to the official Army bulk record.",
        "evidence_paraphrase": item["identity_note"],
        "identity_match_assessment": "High confidence from a nonshared protected-identifier bridge, with name agreement or explicitly reviewed source damage.",
        "temporal_assessment": "The Army-entry record supports identity and a dated occupation category; it does not establish a named employer or the OSS transfer sequence.",
        "source_quality": "A_direct_official",
        "claim_confidence": "high",
        "publication_status": "published",
        "match_notes": f"No protected identifier is exposed and same-name source rows are not merged.{suffix_note}",
        "sources": identity_sources,
    }
    occupation = {
        "key": f"occupation-{item['slug']}-b892",
        "person_id": item["person_id"],
        "affiliation_key": f"{item['slug']}-occupation-b892",
        "claim_type": "occupation",
        "claim_text": f"At Army entry on {item['date']}, {item['name']} was recorded in the historical {occupation_label} category; no employer is identified.",
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
        "next_action": "Review the indexed personnel file in Box 725 or 726 to identify the last civilian employer and establish the Army-to-OSS sequence; the Army occupation category is not an employer.",
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
    box = "725" if row <= 18 else "726"
    update: dict[str, object] = {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, Box {box} and archive location, but staged official-domain, exact-name, employment, occupation, obituary, institutional, directory and archival searches found no defensible identity bridge. {rejection}",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": f"Review the indexed Box {box} personnel file for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "critical",
    }
    if duplicate_group:
        update["possible_duplicate_group"] = duplicate_group
    return update


def make_attempt(row: int, person_id: str, name: str, outcome: str, attempt_number: int, notes: str, high: bool = False) -> dict[str, object]:
    box = "725" if row <= 18 else "726"
    return {
        "key": f"page436-row{row}-{name.lower().replace(' ', '-')}-b892",
        "person_id": person_id,
        "source_adapter": "manual_staged_protocol",
        "query_text": f"{name}; NARA/index context; CIA Reading Room attempt; exact-name OSS variants; employer and occupation; obituary, institutional, newspaper, directory and archival searches; Box {box}; protected-identifier Army crosswalk where available",
        "query_variant_type": "staged_identity_employment_archival_protocol_batch_892",
        "started_at": "2026-10-18T18:00:00Z",
        "completed_at": "2026-10-18T19:10:00Z",
        "outcome": outcome,
        "sources_reviewed": 6 if high else 4,
        "candidate_sources_rejected": 5 if high else 7,
        "rejection_reasons": notes if not high else "External namesakes lacked the protected identifier or Box 725/726 bridge; no named employer source was established.",
        "research_notes": (f"High-confidence official Army identity and qualified occupation or student-status evidence established. {notes}" if high else f"No reliable identity or pre-OSS employer found after staged search and namesake rejection. {notes}") + " The CIA adapter stopped at robots restrictions and the current Library of Congress request timed out; both are access limitations, not negative findings. No exposed NARA API credential was used.",
        "next_action": f"Review Box {box}.",
        "last_error_redacted": "CIA robots restriction; Library of Congress request timeout" if not high else None,
        "attempt_number": attempt_number,
        "research_agent_version": "before-oss-b892-v1",
    }


def main() -> None:
    affiliations = [make_affiliation(item) for item in HIGH]
    claims = [claim for item in HIGH for claim in make_claims(item)]
    person_updates = [high_update(item) for item in HIGH]
    person_updates.extend(unresolved_update(*item) for item in UNRESOLVED)
    research_attempts = [
        make_attempt(
            int(item["row"]),
            str(item["person_id"]),
            str(item["name"]),
            "source_reviewed",
            1,
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
        "bundle_version": "batch-892-v1",
        "reviewer": "Before OSS Batch 892 evidence review",
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
