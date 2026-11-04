#!/usr/bin/env python3
"""Generate the reviewed Batch 1035 evidence bundle for PDF page 290."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page290-nelle-maertens-to-robert-maisonpierre-review_"
    "batch-1035_2026-11-04.json"
)

INDEX = "nara-index-b1035"
ARMY = "army-bulk-b1035"
TECH = "army-tech-b1035"
CODES = "army-codes-b1035"
DET101 = "oss-detachment-101-maharg-b1035"


PEOPLE = {
    1: ("dcd4522c-b303-5f32-b0aa-243ff21ce246", "Nelle E Maertens", "474"),
    2: ("0222f773-9e95-5dfe-afb3-5ec4cac228cf", "Clyde M Maffin", "474"),
    3: ("ade234fb-950f-5379-9e64-0fb78d937ce1", "Matthew P Magdic", "474"),
    4: ("0d513ebe-1061-57ad-8aa4-af1c3c4fa320", "Charles A Magee", "474"),
    5: ("112e97dd-adb7-5495-816d-bec8f04125ea", "Sam Maggio", "474"),
    6: ("89e8fa33-cadf-5a12-be13-ad13793b647b", "Ted W Magier", "474"),
    7: ("1afa37c1-a18f-5c24-8a9d-f1774124983b", "Annel Magill", "474"),
    8: ("8d86d6c9-b62e-5370-8fe6-f3ce9c0cce6a", "Charles W Magill", "474"),
    9: ("248b53bd-d4e9-5241-ae97-2cee6e0e61e4", "Orrin R Magill Jr.", "474"),
    10: ("8761c610-a85a-577c-b62b-9cc1aa39cc66", "Robert N Magill", "474"),
    11: ("6abf47e5-2b1e-52a6-9b9b-32e37670fc40", "William L Magistretti", "475"),
    12: ("4f5d1141-e64c-5fd1-b030-72e40352dc4f", "Henry F Magliocchetti", "475"),
    13: ("a70a133f-5c2e-5b94-b19a-f51410cd34e2", "Louis J Magnani", "475"),
    14: ("67f89379-4e9a-5e11-9762-15d185f4a9d3", "Andre W Magnus", "475"),
    15: ("88a65acc-5385-598b-850a-e998e0fa0169", "Erik M Magnussen", "475"),
    16: ("b2b098d0-36b9-5306-b4e7-c810a4bfc90f", "Alfred Magone", "475"),
    17: ("b6636f80-d453-5c21-94a5-31c9e0e5c97b", "Peter M Magras", "475"),
    18: ("c8e1b865-5f79-59ab-840a-a77ed34fbc67", "Christine F Magriel", "475"),
    19: ("d18c2c5d-2343-5f27-8b3b-c51d72f866aa", "Barbara Magruder", "475"),
    20: ("a93ac760-896e-50b9-9746-754d434a1200", "John Magruder", "475"),
    21: ("8fc3d83c-8fae-50d7-9ddc-725cf1c1da3b", "Elizabeth Maguire", "475"),
    22: ("95254387-be95-5481-b8b5-42a7d6c889e6", "Nancy E Maguire", "475"),
    23: ("e6cdeeba-47e3-5782-9cff-da5eb2f628b8", "Julius Magyar", "475"),
    24: ("35b3a07f-0e20-5ae8-b906-cc757de9d6e0", "Joseph W Mahala", "475"),
    25: ("eb006d56-b602-5c13-82cc-df92c7b8bb95", "James E Mahan", "475"),
    26: ("972d2cdb-c882-5eb7-92bb-5317612f9a4c", "John D Maharg", "475"),
    27: ("0de0a7b0-0891-5a17-a231-7aaa440c9bdb", "Charles A Maher", "475"),
    28: ("c6c3f2d9-a638-5af0-9068-bb18e52f05a1", "John R Maher Jr.", "475"),
    29: ("fb49c573-6519-5512-809c-c51710cbf391", "Joseph A Maher", "475"),
    30: ("ed75f311-c190-594c-936e-3c754ce54c03", "Lincoln E Maher Jr.", "475"),
    31: ("ce0ab96d-98bf-59e9-a796-80f630cefb01", "Peter J Maher", "475"),
    32: ("03912762-331f-5ea3-87cc-d87bb817fdf3", "Robert F Mahon", "475"),
    33: ("35553743-9fc8-5e73-8efa-896f72eee092", "Francis A Mahoney", "476"),
    34: ("c65f7cad-bc5f-5877-8537-67ef78a9109a", "George J Mahoney", "476"),
    35: ("eaf93ed7-95b9-522e-80a7-1fb0f360f204", "Georgie W Mahoney", "476"),
    36: ("0a8cfae8-2036-5131-a2fe-87f07ae97ed4", "Marie A Mahoney", "476"),
    37: ("71adf8ed-dbcc-51a8-b0ad-8fc4e8c11c7b", "William F Mahoney", "476"),
    38: ("68d9b57c-d1ab-57eb-800e-bc813215bd1a", "Frank C Mahood", "476"),
    39: ("7689dd9e-87ef-5351-acd1-c9575161c358", "Natalie C Maiden", "476"),
    40: ("43e275e8-d612-5b8a-99df-3ff09eca6aae", "Mary B Maiers", "476"),
    41: ("f9e24d65-c1fd-520a-8b48-098f4434f3e9", "J L J Mailuku", "476"),
    42: ("57e0f633-3022-52bc-ba7b-3d13a9ab5829", "Shirley K Mains", "476"),
    43: ("7ffc9c71-90c1-5264-88f5-96e4f1bb2165", "James Maiorino", "476"),
    44: ("fac49dd1-8556-57ea-9b59-262d8c10086a", "Raymond E Maisel", "476"),
    45: ("4936b594-ac32-581d-8610-8eea343243c4", "Reginald V Maisey", "476"),
    46: ("62bdae40-7c17-59a6-bf36-824653811f9c", "Robert J Maisonpierre", "476"),
}

# John Magruder already has a confirmed, completed profile. Batch 1035 leaves
# it untouched and updates the other 45 rows printed on page 290.
ACTIVE_ROWS = tuple(row for row in PEOPLE if row != 20)

ARMY_ASSOCIATIONS = {
    3: ("1942-05-06", "732", "semiskilled construction occupation, not elsewhere classified", "Construction occupations, n.e.c.", "unknown", "PDF physical page 174; historical category 7-32"),
    4: ("1944-03-29", "736", "chauffeur or driver of a bus, taxi, truck, or tractor", "Chauffeurs and drivers, bus, taxi, truck, and tractor", "unknown", "PDF physical page 174; historical category 7-36"),
    8: ("1942-04-03", "505", "semiskilled transportation-equipment-building occupation", "Occupations in building transportation equipment except automobiles and aircraft, n.e.c.", "unknown", "PDF physical page 174; historical category 5-05"),
    9: ("1943-04-16", "992", "student", "Students", "student", "PDF physical page 304; corrected historical category 9-92"),
    12: ("1943-02-15", "682", "semiskilled foundry occupation, not elsewhere classified", "Foundry occupations, n.e.c.", "unknown", "PDF physical page 174; historical category 6-82"),
    13: ("1943-02-25", "123", "messenger, errand, or office-worker occupation", "Messengers, errand boys, and office boys and girls", "unknown", "PDF physical page 171; historical category 1-23"),
    14: ("1944-06-30", "081", "advertising agent", "Advertising agents", "unknown", "PDF physical page 171; historical category 0-81"),
    16: ("1942-03-16", "006", "author, editor, or reporter", "Authors, editors, and reporters", "unknown", "PDF physical page 170; historical category 0-06"),
    17: ("1941-03-01", "475", "machinist", "Machinists", "unknown", "PDF physical page 173; historical category 4-75"),
    23: ("1943-04-27", "992", "student", "Students", "student", "PDF physical page 304; corrected historical category 9-92"),
    24: ("1943-08-27", "316", "general farm hand", "Farm hands, general farms", "unknown", "PDF physical page 172; historical category 3-16"),
    31: ("1943-04-01", "732", "semiskilled construction occupation, not elsewhere classified", "Construction occupations, n.e.c.", "unknown", "PDF physical page 174; historical category 7-32"),
    37: ("1942-11-19", "105", "general office clerk", "Clerks, general office", "unknown", "PDF physical page 171; historical category 1-05"),
    43: ("1943-02-26", "627", "semiskilled textile-products-fabrication occupation, not elsewhere classified", "Occupations in fabrication of textile products, n.e.c.", "unknown", "PDF physical page 173; historical category 6-27"),
    46: ("1943-02-13", "011", "college president, professor, or instructor", "College presidents, professors, and instructors", "unknown", "PDF physical page 170; historical category 0-11"),
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def source(key: str, **kwargs: object) -> dict[str, object]:
    value: dict[str, object] = {"key": key, "access_date": "2026-11-04"}
    value.update(kwargs)
    return value


def sources() -> list[dict[str, object]]:
    return [
        source(
            INDEX,
            stable_url="https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            archival_identifier="RG 226, Entry A1-224, Boxes 474-476",
            title="OSS Personnel Files from Excel",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="2010-12-23",
            locator="PDF page 290, rows 1-46; page and all rows visually checked at 180 dpi",
            source_quality="A_direct_official",
            collection_name="Records of the Office of Strategic Services, Record Group 226",
            rights_notes="All 46 printed rows remain separate. Full protected identifiers remain private. Batch 1035 updates 45 rows and preserves John Magruder's completed profile.",
        ),
        source(
            ARMY,
            stable_url="https://catalog.archives.gov/id/1263923",
            archival_identifier="National Archives Identifier 1263923; parent series NAID 604357",
            title="Electronic Army Serial Number Merged File, ca. 1938-1946",
            author_creator="Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="1938-1946; merged file created 2002",
            locator="Official unrestricted ASNEF.FIN.DAT; sixteen Batch 1035 identity candidates explicitly reviewed; fifteen accepted and one rejected",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records",
            document_number="ASNEF.FIN.DAT",
            rights_notes="No raw record, full protected identifier, or bulk-record ordinal is retained in public assets.",
        ),
        source(
            TECH,
            stable_url="https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf",
            archival_identifier="NN3-064-03-008; National Archives Identifier 1263923",
            title="World War II Army Enlistment Records: Reference Copy of Technical Documentation",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives at College Park - Electronic Records",
            publication_record_date="1994-2005; reference copy modified 2011",
            locator="PDF physical pages 44-46; identifier, name, Army-entry-date, grade and civilian-occupation fields",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records technical documentation",
            rights_notes="Used to interpret selected fields only; source damage, coding limits, and incomplete coverage remain applicable.",
        ),
        source(
            CODES,
            stable_url="https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1CL_SD.pdf",
            archival_identifier="National Archives Identifier 1263923; Code No. 30",
            title="NARA Compiled Code Lists for the Electronic Army Serial Number Merged File",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives at College Park - Electronic Records",
            publication_record_date="2011-01-12; modified 2011-03-17",
            locator="PDF physical pages 170-175 and 304; all fifteen published Batch 1035 categories visually checked",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records technical documentation",
            rights_notes="Historical categories identify neither employer, institution, workplace, nor exact Army-to-OSS sequence.",
        ),
        source(
            DET101,
            stable_url="https://www.javadc.org/java/docs/1945-03-15%20OSSSU%20Detachment%20101%20Promotions%20and%20Citations%20OCR%20P11_MA.pdf",
            archival_identifier="OSS SU Detachment 101 Promotions & Citations Report, 15 May 1945",
            title="Promotions & Citations Report, OSS SU Detachment 101",
            author_creator="Headquarters, OSS SU Detachment 101",
            repository_publisher="OSS Detachment 101 Association / JAVA",
            publication_record_date="1945-05-15",
            locator="PDF pages 1-4; John D. Maharg entries under the 29 April and 21 April 1945 promotion boards",
            source_quality="A_direct_official",
            collection_name="OSS Detachment 101 historical records",
            rights_notes="The direct wartime record confirms OSS Detachment 101 service and captain rank; it supplies no pre-OSS employer or civilian occupation.",
        ),
    ]


def affiliation_key(row: int) -> str:
    return f"{slug(PEOPLE[row][1])}-army-association-b1035"


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, _label, relationship, _locator) in ARMY_ASSOCIATIONS.items():
        item: dict[str, object] = {
            "key": affiliation_key(row),
            "person_id": PEOPLE[row][0],
            "relationship_type": relationship,
            "end_date": date,
            "date_precision": f"Historical civilian-occupation code {code} was recorded at Army entry on {date}; no named employer, institution, or workplace is supplied.",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "confirmed",
            "claim_confidence": "medium",
            "source_quality": "A_direct_official",
            "publication_status": "publish_qualified",
            "research_notes": "The broad historical category is not converted into a named employer and is excluded from verified-employer analytics.",
        }
        if relationship == "student":
            item["role_title"] = "student"
        else:
            item["occupation"] = occupation
        values.append(item)
    return values


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, label, relationship, locator) in ARMY_ASSOCIATIONS.items():
        values.append(
            {
                "key": f"army-{slug(PEOPLE[row][1])}-b1035",
                "person_id": PEOPLE[row][0],
                "affiliation_key": affiliation_key(row),
                "claim_type": "other_pre_oss_affiliation" if relationship == "student" else "occupation",
                "claim_text": f"At Army entry on {date}, {PEOPLE[row][1]} was recorded as {occupation}; no employer, institution, or workplace is identified.",
                "evidence_paraphrase": f"The Army bulk file records code {code}, and the visually checked official code list defines the category as {label}.",
                "identity_match_assessment": "Confirmed by exact official name agreement and a nonshared protected linkage; the protected identifier is not published.",
                "temporal_assessment": "Strongly date-bounded to Army entry, but not proven to be the immediately preceding role or status before OSS.",
                "source_quality": "A_direct_official",
                "claim_confidence": "medium",
                "publication_status": "publish_qualified",
                "match_notes": "The historical category is qualified, excluded from verified-employer analytics, and not converted into a named organization.",
                "sources": [
                    {"source_key": INDEX},
                    {"source_key": ARMY},
                    {"source_key": TECH, "support_type": "context_only"},
                    {"source_key": CODES, "locator_override": locator},
                ],
            }
        )
    values.append(
        {
            "key": "identity-john-maharg-detachment-101-b1035",
            "person_id": PEOPLE[26][0],
            "claim_type": "identity",
            "claim_text": "The indexed Captain John D. Maharg served with OSS SU Detachment 101 in 1945.",
            "evidence_paraphrase": "A direct Detachment 101 report records Capt. John D. Maharg's promotion recommendation and approval to major in April 1945.",
            "identity_match_assessment": "High confidence from the exact full name, matching captain rank, and direct wartime OSS unit context.",
            "temporal_assessment": "Direct wartime OSS identity evidence; the report does not identify a pre-OSS employer or occupation.",
            "source_quality": "A_direct_official",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "Later legal-career namesakes were not used to infer prewar employment. Box 475 remains necessary for that chronology.",
            "sources": [
                {"source_key": DET101},
                {"source_key": INDEX, "support_type": "context_only"},
            ],
        }
    )
    return values


def base_update(row: int) -> dict[str, object]:
    name = PEOPLE[row][1]
    box = PEOPLE[row][2]
    return {
        "person_id": PEOPLE[row][0],
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified page 290 source preserves {name}, Box {box}, rank or grade when printed, notes when present, and archive location. Staged official, exact-name, employment, occupation, obituary, institutional, newspaper, directory, and archival searches did not establish a defensible identity-and-affiliation bridge.",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": f"Review indexed Box {box} for corroborating identifiers, immediate pre-OSS affiliation, and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }


def person_updates() -> list[dict[str, object]]:
    updates = [base_update(row) for row in ACTIVE_ROWS]
    by_row = {row: update for row, update in zip(ACTIVE_ROWS, updates, strict=True)}

    for row in ARMY_ASSOCIATIONS:
        by_row[row].update(
            identity_status="confirmed",
            identity_evidence="Exact official name agreement and a nonshared protected linkage connect the index and Army records; the protected identifier remains private.",
            personnel_category="enlisted_army_personnel",
            commissioned_officer=False,
            allied_or_foreign_personnel=False,
            research_status="occupation_only_found",
            nara_catalog_id="1263923",
            archival_review_priority="high",
            next_action=f"Review Box {PEOPLE[row][2]} to identify a named employer or institution and establish Army-to-OSS chronology. The protected Army link supplies only a broad historical occupation or student-status category.",
        )

    by_row[2].update(
        identity_evidence="The indexed row was visually verified, but a protected Army candidate was rejected because its substantially damaged name field conflicts with Clyde M. Maffin. No occupation was transferred.",
        archival_review_priority="critical",
        next_action="Review Box 474 to resolve the damaged Army candidate and identify the immediate pre-OSS affiliation and last civilian employer. No candidate occupation is published.",
    )
    by_row[9].update(
        name_variants=["Orrin F Magill Jr."],
        replace_name_variants=False,
        archival_review_priority="critical",
        next_action="Review Box 474 to identify the educational institution and reconcile the indexed middle initial R with an OSS Detachment 101 report rendered as F before using that report for further identity claims.",
    )
    by_row[11].update(
        name_variants=["William Louis Magistretti"],
        replace_name_variants=False,
        next_action="Review Box 475 and the American Council of Learned Societies file for William Louis Magistretti (1937-1941) to determine the nature of the prewar relationship; a finding-aid file title alone is not treated as employment evidence.",
    )
    by_row[26].update(
        identity_status="high_confidence",
        identity_evidence="A direct wartime OSS Detachment 101 report names Capt. John D. Maharg and records his April 1945 promotion recommendation and approval to major, matching the indexed full name and captain rank.",
        personnel_category="commissioned_army_officer",
        commissioned_officer=True,
        allied_or_foreign_personnel=False,
        next_action="Review Box 475 for John D. Maharg's pre-OSS legal or military chronology. Later Los Angeles County legal work and an unsourced biographical lead were not used to infer a prewar employer.",
        archival_review_priority="critical",
    )
    by_row[42].update(
        name_variants=["Shirley K Ray"],
        replace_name_variants=False,
        next_action="Review Box 476 under both Shirley K. Mains and the indexed note 'Aka Ray' to establish identity, immediate pre-OSS affiliation, and last civilian employer.",
        archival_review_priority="critical",
    )

    if len(updates) != 45:
        raise RuntimeError(f"Expected 45 person updates, generated {len(updates)}")
    return updates


def unresolved_reason(row: int) -> str:
    special = {
        2: "A damaged-name Army candidate was rejected, so no occupation was transferred.",
        9: "A direct Detachment 101 report appears to name Orrin F. Magill Jr.; the middle-initial conflict with the indexed and Army-linked R remains unresolved.",
        11: "An ACLS finding aid contains a William Louis Magistretti file dated 1937-1941, but it does not state the relationship and cannot establish employment.",
        26: "A direct OSS record confirms John D. Maharg's Detachment 101 identity, but accessible sources did not establish his pre-OSS legal or military chronology.",
        28: "The source note '1 or 7 at' was preserved exactly as parsed and requires personnel-file review; it was not used to infer an identity or assignment.",
        41: "Initials-only J L J Mailuku remains unresolved after exact and variant searches; no biography was assigned by name resemblance.",
        42: "The indexed alias note 'Aka Ray' was retained as a search variant but did not produce a defensible identity bridge.",
    }
    return special.get(
        row,
        "Unbridged namesakes, snippets, commercial people-finder pages, unsourced genealogy, relatives, and postwar-only leads did not establish this indexed person's identity or pre-OSS affiliation.",
    )


def research_attempts() -> list[dict[str, object]]:
    updates = {item["person_id"]: item for item in person_updates()}
    substantiated = set(ARMY_ASSOCIATIONS) | {26}
    values: list[dict[str, object]] = []
    for row in ACTIVE_ROWS:
        person_id, name, box = PEOPLE[row]
        values.append(
            {
                "key": f"page290-row{row}-{slug(name)}-b1035",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index context; exact-name and meaningful initial, suffix, alias, punctuation and OCR variants; OSS and CIA Reading Room; rank, branch, assignment and protected-identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory and archival searches; indexed Box {box}",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_1035",
                "started_at": "2026-11-04T18:55:00-05:00",
                "completed_at": "2026-11-04T20:35:00-05:00",
                "outcome": "source_reviewed" if row in substantiated else "candidate_rejected",
                "sources_reviewed": 6 if row in substantiated else 5,
                "candidate_sources_rejected": 2 if row in substantiated else 4,
                "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, and postwar-only leads were rejected. Army categories were not converted into named employers; finding-aid file titles were not treated as affiliations; and discovery-only material was not published as evidence.",
                "research_notes": f"{unresolved_reason(row)} The official index, exact-name OSS searches, targeted CIA context, employment and occupation searches, and institutional, newspaper, obituary, directory, and archival searches were reviewed as applicable. Page 290 and all cited code-list pages were visually checked. No authenticated NARA Catalog API request was made.",
                "next_action": str(updates[person_id]["next_action"]),
                "attempt_number": 1,
                "research_agent_version": "before-oss-b1035-v1",
            }
        )
    if len(values) != 45:
        raise RuntimeError(f"Expected 45 research attempts, generated {len(values)}")
    return values


def main() -> None:
    bundle = {
        "bundle_version": "batch-1035-v1",
        "reviewer": "Before OSS Batch 1035 evidence review",
        "sources": sources(),
        "affiliations": affiliations(),
        "claims": claims(),
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }
    EvidenceBundle.model_validate(bundle)
    OUTPUT.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
