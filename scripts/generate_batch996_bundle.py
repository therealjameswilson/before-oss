#!/usr/bin/env python3
"""Generate the reviewed Batch 996 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page488-walker-to-wallace-"
    "review_batch-996_2026-11-03.json"
)

INDEX = "nara-index-b996"
ARMY = "army-bulk-b996"
TECH = "army-tech-b996"
CODES = "army-codes-b996"


PEOPLE = {
    24: ("466b5612-1274-5490-a2db-e8df9e243b13", "Mary Virginia Walker"),
    25: ("f1ee22dc-e66e-5954-bb75-ffffe5d1f7c0", "Morley Walker"),
    26: ("45ff3de0-3a9b-50a3-8f19-1c53b6a649bf", "Nora Walker"),
    27: ("9ee3948c-3dee-5078-9bd0-e5595bede27e", "Philip G Walker"),
    28: ("c1845772-6df0-53bb-84b0-60fb88d41b80", "Raymond E Walker"),
    29: ("084a2157-d631-51ee-bd61-ec09efb64202", "Reinhold Walker"),
    30: ("36343c8d-ea8b-54bf-b6f2-555f9506b595", "Richard J Walker"),
    31: ("5c303c26-d46d-5481-bdac-f9cbcc737083", "Robert N Walker"),
    32: ("ba8c8f52-f4be-5af6-a3c5-2683ee52cd80", "Robert M Walker"),
    33: ("40b7f95c-8c3e-5b7e-bc55-9dff49bf847f", "Robert M Walker"),
    34: ("2e8b3586-7976-57f5-a9ce-5f1ee04e7917", "Roy L Walker"),
    35: ("ba6c677b-1da9-569c-9561-91b6ed996182", "Sinclair C Walker"),
    36: ("3fdb6199-8323-5e87-a7b1-85d23ac514ba", "T.E. Walker"),
    37: ("32855ded-c355-56f8-98bb-e140410da6cf", "Vincent Walker"),
    38: ("b55b188c-7264-50b4-9295-9174ebd72054", "Wesley E Walker"),
    39: ("252a6f06-c8e6-5184-9f1b-6ac4f9428ebd", "William E Walker"),
    40: ("08b751b5-8153-5b80-aba2-234d85a7e1af", "Philip Walkley"),
    41: ("a1174b10-b91a-5ce6-8796-75d331c2d091", "Fred Wall Jr."),
    42: ("b9ef16f7-ea2c-5a27-a95a-1df21e528219", "Robert B Wall"),
    43: ("8bd20855-5dac-5616-bdc6-be3c48394139", "Temple A Wall Jr."),
    44: ("3b7644de-050b-5216-ab0c-44e83b010f92", "Curt M Wallace"),
    45: ("c1d97c2b-84f9-5b2f-9f80-b4eb06948d33", "Dudley R Wallace"),
    46: ("dfb5ff48-b259-575b-bea2-e4f319b3da68", "Elery P Wallace"),
}

OFFICERS = {27, 39}

UNRESOLVED = {
    24: "A 1951 nursing-faculty lead and other modern or genealogical namesakes supplied no OSS, indexed-identifier, or personnel-file bridge and were rejected.",
    26: "The common exact name produced multiple namesakes but no corroborating OSS, identifier, rank, unit, employer, or personnel-file evidence.",
    27: "A British war-memorial namesake supplied no indexed officer-number or OSS bridge and was rejected; rank-aware searches produced no reliable alternative.",
    29: "Exact-name, identifier, OSS, employer, occupation, obituary, institutional, and archival searches produced no reliable identity bridge.",
    30: "Common-name searches produced no source with the middle initial, indexed identifier, unit, or direct OSS assignment bridge.",
    32: "This first of two adjacent Robert M Walker rows remains separate; name identity alone cannot merge it with row 33, whose different protected identifier has an Army match.",
    36: "The initials-only form and common surname produced no source with enough corroborating identifiers to resolve the person.",
    37: "The common exact name produced multiple namesakes but no source with an indexed identifier, OSS assignment, unit, or personnel-file bridge.",
    38: "Exact-name and middle-initial searches produced no source with an indexed identifier, OSS assignment, unit, employer, or personnel-file bridge.",
    39: "Rank-aware and exact-name searches produced no source with the indexed officer number or a direct OSS assignment bridge.",
    40: "A modern nonprofit executive with the same distinctive name is chronologically incompatible and was rejected; no wartime identity bridge was found.",
    41: "Common-name and suffix-aware searches produced no source with an OSS, protected-identifier, rank, unit, or personnel-file bridge.",
    43: "Modern and deceased namesakes supplied no OSS, indexed-identifier, employer, or personnel-file bridge and were rejected.",
    45: "Exact-name, OSS, employer, occupation, obituary, institutional, newspaper, and archival searches produced no reliable result.",
    46: "The distinctive full name produced no source with an OSS, protected-identifier, employer, or personnel-file bridge.",
}

ARMY_OCCUPATIONS = {
    25: {
        "date": "1942-11-10",
        "code": "992",
        "occupation": "student",
        "label": "Students",
        "locator": "PDF physical page 304; amended historical category 9-92",
        "identity": "confirmed",
        "confidence": "confirmed",
        "relationship": "student",
        "category": "enlisted_army_personnel",
        "officer": False,
        "variant": "The official Army and indexed names agree exactly.",
    },
    33: {
        "date": "1943-11-15",
        "code": "031",
        "occupation": "secondary-school teacher or principal",
        "label": "Teachers (secondary school) and principals",
        "locator": "PDF physical page 171; historical category 0-31",
        "identity": "confirmed",
        "confidence": "confirmed",
        "relationship": "employment",
        "category": "enlisted_army_personnel",
        "officer": False,
        "variant": "The official Army and indexed names agree exactly.",
    },
    34: {
        "date": "1942-04-28",
        "code": "316",
        "occupation": "farm hand on a general farm",
        "label": "Farm hands, general farms",
        "locator": "PDF physical page 172; historical category 3-16",
        "identity": "confirmed",
        "confidence": "confirmed",
        "relationship": "employment",
        "category": "enlisted_army_personnel",
        "officer": False,
        "variant": "The official Army and indexed names agree exactly.",
    },
    35: {
        "date": "1940-11-25",
        "code": "002",
        "occupation": "actor",
        "label": "Actors and actresses",
        "locator": "PDF physical page 171; historical category 0-02",
        "identity": "high_confidence",
        "confidence": "high",
        "relationship": "employment",
        "category": "unknown_or_indeterminate",
        "officer": None,
        "variant": "The official Army form omits the indexed middle initial C; the nonshared protected identifier, surname, and distinctive given name agree. Its malformed grade code is withheld.",
    },
    42: {
        "date": "1944-01-18",
        "code": "992",
        "occupation": "student",
        "label": "Students",
        "locator": "PDF physical page 304; amended historical category 9-92",
        "identity": "confirmed",
        "confidence": "confirmed",
        "relationship": "student",
        "category": "enlisted_army_personnel",
        "officer": False,
        "variant": "The official Army and indexed names agree exactly.",
    },
    44: {
        "date": "1943-07-27",
        "code": "056",
        "occupation": "photographer",
        "label": "Photographers",
        "locator": "PDF physical page 171; historical category 0-56",
        "identity": "high_confidence",
        "confidence": "high",
        "relationship": "employment",
        "category": "enlisted_army_personnel",
        "officer": False,
        "variant": "The official Army middle initial W conflicts with indexed M; the nonshared protected identifier, surname, given name, and private rank agree.",
    },
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Box 813",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 488, rows 24-46; checked against layout-preserving text and an original-detail page render",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. Protected identifiers remain private. PDF page 489 row 1, Inovar A Wallace in Box 813, is outside this cohort and begins the next batch.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; six accepted and one rejected protected-identifier comparison; identifiers and record ordinals withheld",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "Six identity bridges were accepted after private comparison. Raymond E Walker's identifier points to a wholly different Army name; no Army fields were transferred to him.",
        },
        {
            "key": TECH,
            "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf",
            "archival_identifier": "NN3-064-03-008; National Archives Identifier 1263923",
            "title": "World War II Army Enlistment Records: Reference Copy of Technical Documentation",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives at College Park - Electronic Records",
            "publication_record_date": "1994-2005; reference copy modified 2011",
            "locator": "PDF physical pages 44-46; name, Army-entry-date, grade, and civilian-occupation fields",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
        },
        {
            "key": CODES,
            "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1CL_SD.pdf",
            "archival_identifier": "National Archives Identifier 1263923; Code No. 30",
            "title": "NARA Compiled Code Lists for the Electronic Army Serial Number Merged File",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives at College Park - Electronic Records",
            "publication_record_date": "2011-01-12; modified 2011-03-17",
            "locator": "PDF physical pages 171, 172, and 304; historical civilian-occupation or student categories 0-02, 0-31, 0-56, 3-16, and amended 9-92",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "All cited code pages were checked in extracted text and original-detail renders. Historical labels identify broad occupations or student status, not named employers, schools, workplaces, or exact OSS-transfer dates.",
        },
    ]


def affiliations() -> list[dict[str, object]]:
    values = []
    for row, item in ARMY_OCCUPATIONS.items():
        values.append(
            {
                "key": f"{slug(PEOPLE[row][1])}-army-occupation-b996",
                "person_id": PEOPLE[row][0],
                "occupation": item["occupation"],
                "relationship_type": item["relationship"],
                "end_date": item["date"],
                "date_precision": f"Historical civilian-occupation code {item['code']} was recorded at Army entry on {item['date']}; no named employer, school, workplace, or exact OSS-transfer date is supplied.",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": item["identity"],
                "claim_confidence": "medium",
                "source_quality": "A_direct_official",
                "publication_status": "publish_qualified",
                "research_notes": "Broad historical occupation or student category only; no named employer, school, or workplace is inferred.",
            }
        )
    return values


def claim(
    key: str,
    row: int,
    claim_type: str,
    text: str,
    paraphrase: str,
    identity: str,
    temporal: str,
    quality: str,
    confidence: str,
    publication: str,
    notes: str,
    source_links: list[dict[str, str]],
    affiliation_key: str | None = None,
) -> dict[str, object]:
    value: dict[str, object] = {
        "key": key,
        "person_id": PEOPLE[row][0],
        "claim_type": claim_type,
        "claim_text": text,
        "evidence_paraphrase": paraphrase,
        "identity_match_assessment": identity,
        "temporal_assessment": temporal,
        "source_quality": quality,
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
    for row, item in ARMY_OCCUPATIONS.items():
        name = PEOPLE[row][1]
        category = str(item["occupation"]).lower()
        values.extend(
            [
                claim(
                    f"identity-{slug(name)}-b996",
                    row,
                    "identity",
                    f"Indexed {name} is a {str(item['confidence']).replace('_', ' ')} match to the reviewed official Army entry record.",
                    f"A nonshared protected identifier connects the visually verified index row to the Army record. {item['variant']}",
                    f"{str(item['confidence']).replace('_', ' ').capitalize()} from the protected-identifier bridge and documented name comparison; the identifier and record ordinal remain private.",
                    f"The Army record dates entry to {item['date']} and supplies only historical civilian code {item['code']}.",
                    "A_direct_official",
                    str(item["confidence"]),
                    "published",
                    "Identity only; no named employer, school, or exact OSS-transfer date is inferred.",
                    [
                        {"source_key": INDEX, "locator_override": f"PDF page 488 row {row}; protected identifier withheld"},
                        {"source_key": ARMY, "locator_override": "Accepted reviewed identity bridge; protected identifier withheld"},
                    ],
                ),
                claim(
                    f"occupation-{slug(name)}-b996",
                    row,
                    "occupation",
                    f"At Army entry on {item['date']}, {name} was recorded in the historical {category} category; no named employer or institution is identified.",
                    f"The accepted Army record carries civilian-occupation code {item['code']}, decoded from NARA's official code list.",
                    "The category belongs only to the reviewed protected-identifier match; the identifier itself is not public.",
                    "Strongly date-bounded to Army entry; it does not establish the immediate pre-OSS affiliation, a named employer, or a named school.",
                    "A_direct_official",
                    "medium",
                    "publish_qualified",
                    "Published with its limits and excluded from verified-employer analytics.",
                    [
                        {"source_key": ARMY, "locator_override": f"Army entry {item['date']}; civilian occupation code {item['code']}; protected identifier withheld"},
                        {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46"},
                        {"source_key": CODES, "locator_override": str(item["locator"]), "excerpt_override": str(item["label"])},
                    ],
                    f"{slug(name)}-army-occupation-b996",
                ),
            ]
        )
    values.append(
        claim(
            "conflict-raymond-walker-b996",
            28,
            "identity",
            "Raymond E Walker's indexed protected identifier points to an official Army record under a wholly different name.",
            "The visually verified index row and official Army bulk row conflict materially in both surname and given name.",
            "Conflicting source data: the Army candidate is rejected, and its identity, chronology, grade, and occupation are not transferred.",
            "No temporal conclusion is possible until the indexed Box 813 personnel file is reviewed.",
            "A_direct_official",
            "conflicting",
            "conflicting",
            "The conflict remains visible without exposing either protected identifier or the unrelated Army biography.",
            [
                {"source_key": INDEX, "locator_override": "PDF page 488 row 28; protected identifier withheld"},
                {"source_key": ARMY, "locator_override": "Rejected material name collision; protected identifier and unrelated name withheld"},
            ],
        )
    )
    return values


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
    values = []
    for row, reason in UNRESOLVED.items():
        category = "commissioned_army_officer" if row in OFFICERS else "unknown_or_indeterminate"
        officer: bool | None = True if row in OFFICERS else None
        values.append(
            base_update(
                row,
                identity_status="unresolved",
                identity_evidence=f"The visually verified page 488 row preserves {PEOPLE[row][1]} and its archival context. {reason}",
                personnel_category=category,
                commissioned_officer=officer,
                research_status="requires_archival_review",
                next_action=f"Review the indexed Box 813 personnel file for corroborating identifiers, the immediate pre-OSS affiliation, and the last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}",
            )
        )

    for row, item in ARMY_OCCUPATIONS.items():
        identity_note = "Exact indexed name and a nonshared protected identifier connect the row to the reviewed official Army record."
        if row == 35:
            identity_note = "A nonshared protected identifier, surname, and distinctive given name connect the records; the Army form omits indexed middle initial C and its malformed grade code is withheld."
        elif row == 44:
            identity_note = "A nonshared protected identifier, surname, given name, and private rank connect the records; the Army middle initial W conflicts with indexed M, so identity remains high-confidence rather than confirmed."
        values.append(
            base_update(
                row,
                identity_status=item["identity"],
                identity_evidence=identity_note,
                personnel_category=item["category"],
                commissioned_officer=item["officer"],
                allied_or_foreign_personnel=False,
                research_status="occupation_only_found",
                next_action=f"Review the indexed Box 813 personnel file to identify any named employer or institution behind the broad {str(item['occupation']).lower()} category and establish the Army-to-OSS chronology.",
                nara_catalog_id="1263923",
            )
        )

    values.extend(
        [
            base_update(
                28,
                identity_status="conflicting",
                identity_evidence="The protected identifier printed for Raymond E Walker points to an official Army row under a wholly different full name. The candidate is rejected and none of its fields are transferred.",
                personnel_category="unknown_or_indeterminate",
                commissioned_officer=None,
                research_status="conflicting_sources",
                next_action="Review the indexed Box 813 personnel file to resolve the protected-identifier conflict before assigning any Army identity, chronology, occupation, immediate affiliation, or employer.",
                archival_review_priority="critical",
            ),
            base_update(
                31,
                identity_status="unresolved",
                identity_evidence="An official NSA search index exposes a Robert N. Walker correspondence file with a matching protected officer-number candidate and a detailed prewar chronology, but the source PDF returned Access Denied and could not be inspected. Search-result text is not accepted as final identity or employment evidence.",
                personnel_category="unknown_or_indeterminate",
                commissioned_officer=None,
                research_status="blocked_by_source_access",
                next_action="Revisit NSA document A69841 through an authorized public path or inspect the indexed Box 813 personnel file. Verify the source pages before accepting the candidate identity, Wilson College employment, earlier teaching, or military-intelligence chronology.",
                archival_review_priority="critical",
            ),
        ]
    )
    return values


def research_attempts() -> list[dict[str, object]]:
    attempts = []
    sourced = set(ARMY_OCCUPATIONS)
    for row, (person_id, name) in PEOPLE.items():
        if row in sourced:
            outcome, reviewed, rejected_count = "source_reviewed", 8, 5
            note = f"A reviewed protected-identifier Army bridge supports identity and a qualified {ARMY_OCCUPATIONS[row]['occupation']} category at Army entry; it supplies no named employer, school, workplace, or OSS-transfer date."
        elif row == 28:
            outcome, reviewed, rejected_count = "candidate_rejected", 8, 7
            note = "The protected identifier points to a wholly different official Army name. The candidate was rejected and its date, grade, occupation, and biography were withheld."
        elif row == 31:
            outcome, reviewed, rejected_count = "blocked", 7, 6
            note = "Official NSA document A69841 is a strong discovery lead because indexed OCR presents the same name and protected officer-number candidate plus prewar employment chronology. Direct retrieval returned an Access Denied HTML page, browser access was unavailable, and the search snippet was not used as final evidence."
        elif row in {24, 27, 40, 43}:
            outcome, reviewed, rejected_count = "candidate_rejected", 7, 7
            note = UNRESOLVED[row]
        else:
            outcome, reviewed, rejected_count = "no_result", 6, 6
            note = UNRESOLVED[row]

        attempts.append(
            {
                "key": f"page488-row{row}-{slug(name)}-b996",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index context; CIA Reading Room exact-name domain check; Library of Congress exact-name collection check; exact-name and meaningful variants; OSS, rank, branch, identifier and assignment clues; employer and occupation 1940; obituary, institutional, newspaper, directory and archival searches; indexed Box 813; protected identifiers used only in private official-record comparison",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_996",
                "started_at": "2026-11-03T15:05:00Z",
                "completed_at": "2026-11-03T16:20:00Z",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected_count,
                "rejection_reasons": "Unbridged namesakes, snippets, commercial people-finder pages, relatives, unsourced genealogy, postwar-only leads, and sources without an OSS, protected-identifier, rank, unit, or personnel-file bridge were rejected. The two Robert M Walker rows were not merged. Raymond E Walker's material Army-name collision was rejected. The inaccessible NSA Robert N. Walker lead was deferred rather than published from indexed OCR. Historical occupations and student status were not converted into named employers or schools.",
                "research_notes": f"{note} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain, and archival searches were checked as applicable. Grouped CIA Reading Room and Library of Congress discovery checks produced no additional publishable employer source for the cohort. The NARA index page was text-extracted, rendered, and visually checked; official Army bulk data, technical documentation, and code documentation were inspected locally. All cited code pages were also visually checked. No search-result snippet was used as sole final evidence, no paywall or access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": "Review the indexed Box 813 personnel file for corroborating identifiers, the immediate pre-OSS affiliation, and the last civilian employer before wartime service.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b996-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-996-v1",
        "reviewer": "Before OSS Batch 996 evidence review",
        "sources": sources(),
        "organizations": [],
        "affiliations": affiliations(),
        "claims": claims(),
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }
    EvidenceBundle.model_validate(bundle)
    OUTPUT.write_text(
        json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
