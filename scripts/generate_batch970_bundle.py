#!/usr/bin/env python3
"""Generate the reviewed Batch 970 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page475-joseph-turcotte-to-mildred-turner-"
    "review_batch-970_2026-10-30.json"
)

INDEX = "nara-index-b970"
ARMY = "army-bulk-b970"
TECH = "army-tech-b970"
CODES = "army-codes-b970"
FSJ_1938 = "fsj-campbell-turner-1938-b970"
FSJ_1942 = "fsj-campbell-turner-1942-b970"
SCHOOL = "turners-diplomatic-school-b970"


PEOPLE = {
    24: ("a2f22323-2d3a-50fe-a2b2-b67b8d3a6253", "Joseph E Turcotte"),
    25: ("5029cf18-6843-58b3-a9d5-bd89a2ffccf4", "John Turean"),
    26: ("cae8ee63-77b7-5b6f-933c-577360d0a0fb", "Leonard S Turkowski"),
    27: ("98c38d68-3fee-5c00-9cb7-fb7dc7a48249", "August A Turlano"),
    28: ("43d20da9-2ff9-5732-8e6c-126abbcb0b40", "Carl W Turley"),
    29: ("2f9c3116-ab53-51b0-8618-b04abf056627", "Grady V Turley"),
    30: ("4ff7bce1-cef9-5c40-b79a-fc4493625ec3", "Dennis H Turnbull"),
    31: ("f59b7664-3c11-533c-827f-6cc6f742efc4", "Douglas H Turnbull"),
    32: ("cb434056-7a1e-54c1-8239-a141caa85f96", "Fredrick Turnbull"),
    33: ("e406630e-c5da-5d8e-826d-463e8c577e6b", "Robert L Turnbull"),
    34: ("415f3a77-a884-51c3-b9fa-05d7b0575d5e", "Robert T Turnbull"),
    35: ("3fe00325-5ead-586f-8f25-337bd56c685f", "Ronald B Turnbull"),
    36: ("cb43dd8f-a17c-50ea-8ddb-0bddefb6f932", "William Turnbull"),
    37: ("d20803ab-67c1-5afe-bde2-f11ea7cb0a02", "Campbell Turner"),
    38: ("8f4710f2-9061-58c3-b539-b794eb783096", "Charles N Turner"),
    39: ("e87a0151-6edd-5cf4-8686-0937b4e0ae80", "Dora Turner"),
    40: ("aa8a566b-5fb0-5694-a270-f56909e7e083", "Gladys Turner"),
    41: ("e2aea350-195f-5aab-b91f-eecee44b996f", "Hugh W Turner"),
    42: ("9a83dca7-ea84-5abb-9139-fb7448ee5dde", "John L Turner"),
    43: ("e695bb1b-ee87-56e8-af3b-5cf51377eed3", "John M Turner"),
    44: ("c7fed2e6-f649-5059-98cc-56d7be89ccdc", "Marden S Turner"),
    45: ("cea7eb07-203b-5308-acc3-8f074a9c52be", "Margaret H Turner"),
    46: ("6e04f465-6968-56dc-8252-26dbf33beec3", "Mildred M Turner"),
}


ARMY_OCCUPATIONS = [
    {
        "row": 24,
        "date": "1942-01-26",
        "code": "678",
        "occupation": "Machine shop and related occupations, not elsewhere classified",
        "public_occupation": "semiskilled machine-shop or related worker, not elsewhere classified",
        "locator": "Historical category 6-78; machine-shop and related occupations, n.e.c.",
        "temporal_basis": "documented_prewar",
    },
    {
        "row": 25,
        "date": "1942-11-03",
        "code": "992",
        "occupation": "Students",
        "public_occupation": "student",
        "locator": "Corrected historical category 9-92; students",
        "temporal_basis": "documented_prewar",
    },
    {
        "row": 27,
        "date": "1942-11-13",
        "code": "022",
        "occupation": "Lawyers and judges",
        "public_occupation": "lawyer or judge",
        "locator": "Historical category 0-22; lawyers and judges",
        "temporal_basis": "documented_prewar",
        "variants": ["August A Iurlano"],
        "identity_note": (
            "The exact protected identifier connects indexed August A Turlano to the official Army spelling "
            "August A Iurlano. The surname conflict remains visible as a variant; the index rank Cpl. and Army-entry "
            "grade PVT describe different moments and are not treated as a contradiction."
        ),
    },
    {
        "row": 31,
        "date": "1942-02-13",
        "code": "736",
        "occupation": "Chauffeurs and drivers, bus, taxi, truck, and tractor",
        "public_occupation": "chauffeur or driver of a bus, taxi, truck or tractor",
        "locator": "Historical category 7-36; chauffeurs and drivers, bus, taxi, truck and tractor",
        "temporal_basis": "documented_prewar",
    },
    {
        "row": 34,
        "date": "1941-02-10",
        "code": "240",
        "occupation": "Attendants, recreation and amusement, not elsewhere classified",
        "public_occupation": "recreation or amusement attendant, not elsewhere classified",
        "locator": "Historical category 2-40; attendants, recreation and amusement, n.e.c.",
        "temporal_basis": "documented_prewar",
    },
    {
        "row": 41,
        "date": "1943-04-17",
        "code": "118",
        "occupation": "Clerks, general industry",
        "public_occupation": "general-industry clerk",
        "locator": "Corrected historical category 1-18; clerks, general industry",
        "temporal_basis": "documented_prewar",
    },
    {
        "row": 42,
        "date": "1945-06-28",
        "code": "992",
        "occupation": "Students",
        "public_occupation": "student",
        "locator": "Corrected historical category 9-92; students",
        "temporal_basis": "temporal_relation_uncertain",
    },
    {
        "row": 43,
        "date": "1942-12-12",
        "code": "992",
        "occupation": "Students",
        "public_occupation": "student",
        "locator": "Corrected historical category 9-92; students",
        "temporal_basis": "documented_prewar",
        "variants": ["John M Turner Jr"],
        "identity_note": (
            "The protected identifier connects indexed John M Turner to the official Army spelling John M Turner Jr. "
            "The suffix remains visible as a variant and is not silently added to the indexed name."
        ),
    },
    {
        "row": 44,
        "date": "1943-05-19",
        "code": "592",
        "occupation": "Foremen, manufacturing",
        "public_occupation": "manufacturing foreman",
        "locator": "Historical category 5-92; foremen, manufacturing",
        "temporal_basis": "documented_prewar",
    },
]


IDENTITY_ONLY = {
    28: {
        "date": "1946-01-29",
        "note": (
            "An exact full name and nonshared protected identifier connect the index row to the reviewed official Army "
            "row. The Army-entry date is after OSS dissolution and code 345 is not safely decoded, so no pre-OSS "
            "occupation is projected backward."
        ),
    },
    29: {
        "date": "1941-03-10",
        "note": (
            "An exact full name and nonshared protected identifier connect the index row to the reviewed official Army "
            "row. Historical code 999 supplies no safely decoded civilian occupation."
        ),
    },
}


UNRESOLVED = {
    26: "A specialist Ritchie Boys roster lead was not admitted because the accessible result did not provide a second person-specific identifier or inspectable pre-OSS chronology.",
    30: "Exact-name, initial, OSS, employer, occupation, obituary and archival searches produced no defensible identity bridge.",
    32: "The index spelling Fredrick and Frederick variants produced multiple namesakes without two corroborating identifiers beyond the name.",
    33: "The common name produced multiple namesakes and no source supplied two corroborating identifiers beyond the name.",
    35: "Exact-name, initial, OSS, employer, occupation, obituary and archival searches produced no defensible identity bridge.",
    36: "The common name produced multiple namesakes and no source supplied two corroborating identifiers beyond the name.",
    38: "Exact-name, middle-initial, OSS, employer, occupation, obituary and archival searches produced no defensible identity bridge.",
    39: "Name-only searches produced multiple plausible namesakes without a second identifier or dated OSS context.",
    40: "Name-only searches produced multiple plausible namesakes without a second identifier or dated OSS context.",
    45: "The common name and middle initial produced multiple namesakes without a source linking one to Box 790 or OSS.",
    46: "The common name and middle initial produced multiple namesakes without a source linking one to Box 790 or OSS.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def army_identity_note(row: int) -> str:
    item = next((entry for entry in ARMY_OCCUPATIONS if entry["row"] == row), None)
    if item and item.get("identity_note"):
        return str(item["identity_note"])
    if row in IDENTITY_ONLY:
        return str(IDENTITY_ONLY[row]["note"])
    return (
        "An exact full name and nonshared protected identifier connect the indexed person to the reviewed official "
        "Army row."
    )


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 365 and 789-790",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 475, rows 24-46; checked against layout-preserving text and a 200 dpi page render",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. Protected identifiers remain private.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; eleven accepted Batch 970 identity comparisons; protected identifiers and record ordinals withheld",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "No raw bulk row, record ordinal or full protected identifier enters the evidence bundle or public assets.",
        },
        {
            "key": TECH,
            "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf",
            "archival_identifier": "NN3-064-03-008; National Archives Identifier 1263923",
            "title": "World War II Army Enlistment Records: Reference Copy of Technical Documentation",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives at College Park - Electronic Records",
            "publication_record_date": "1994-2005; reference copy modified 2011",
            "locator": "PDF physical pages 44-46; name, Army-entry-date, grade and civilian-occupation fields",
            "access_date": "2026-10-30",
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
            "locator": "PDF physical pages 171-174 and corrected page 304; nine Batch 970 categories visually and textually checked",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical categories identify neither employers nor workplaces and are retained only where needed for auditability.",
        },
        {
            "key": FSJ_1938,
            "stable_url": "https://www.afsa.org/sites/default/files/fsj-1938-05-may_0.pdf",
            "title": "The American Foreign Service Journal, May 1938",
            "author_creator": "American Foreign Service Association",
            "repository_publisher": "American Foreign Service Association",
            "publication_record_date": "1938-05",
            "locator": "PDF page 64 (viewer page 63); Turner’s Diplomatic School advertisement and Colonel Campbell Turner contact",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "The Foreign Service Journal archive",
            "rights_notes": "Only a short excerpt and project-authored paraphrase are retained.",
        },
        {
            "key": FSJ_1942,
            "stable_url": "https://afsa.org/sites/default/files/fsj-1942-02-february_0.pdf",
            "title": "The American Foreign Service Journal, February 1942",
            "author_creator": "American Foreign Service Association",
            "repository_publisher": "American Foreign Service Association",
            "publication_record_date": "1942-02",
            "locator": "PDF page 62 (viewer page 61); Turner’s Diplomatic School advertisement naming Colonel Campbell Turner as director",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "The Foreign Service Journal archive",
            "rights_notes": "Only a short excerpt and project-authored paraphrase are retained.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": SCHOOL,
            "organization_id": "f24ecbc7-450d-5c41-8fdf-a2e2286b41f2",
            "canonical_name": "Turner's Diplomatic School",
            "historical_name": "Mr. Turner's Diplomatic School",
            "aliases": ["TURNER'S DIPLOMATIC SCHOOL", "Turner’s Diplomatic School"],
            "organization_type": "Foreign Service examination school",
            "sector": "academia_and_research",
            "country": "United States",
            "active_dates": "Documented 1938-1942",
            "normalization_notes": "The existing 'Mr. Turner's Diplomatic School' record and contemporary advertisements headed 'TURNER'S DIPLOMATIC SCHOOL' describe the same Foreign Service examination school. It advertised a Washington, D.C. address in 1938 and an Alexandria, Virginia address in February 1942; no modern successor is assigned.",
        }
    ]


def occupation_affiliation(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    name = PEOPLE[row][1]
    relation = "student" if item["code"] == "992" else "unknown"
    return {
        "key": f"{slug(name)}-occupation-b970",
        "person_id": PEOPLE[row][0],
        "occupation": item["public_occupation"],
        "relationship_type": relation,
        "end_date": item["date"],
        "date_precision": f"Historical civilian-status code {item['code']} was recorded at Army entry on {item['date']}; no employer, school, workplace or OSS-transfer date is named.",
        "country": "United States",
        "immediate_pre_oss": False,
        "last_civilian_pre_service": False,
        "pre_oss_temporal_basis": item["temporal_basis"],
        "identity_confidence": "high_confidence",
        "claim_confidence": "medium",
        "source_quality": "A_direct_official",
        "publication_status": "publish_qualified",
        "research_notes": "Occupation or student status only. The historical category is not a named employer or institution and is excluded from verified-employer analytics.",
    }


def affiliations() -> list[dict[str, object]]:
    values = [occupation_affiliation(item) for item in ARMY_OCCUPATIONS]
    values.append(
        {
            "key": "campbell-turner-diplomatic-school-b970",
            "person_id": PEOPLE[37][0],
            "organization_key": SCHOOL,
            "organization_name_as_found": "TURNER'S DIPLOMATIC SCHOOL",
            "role_title": "director",
            "relationship_type": "professional_affiliation",
            "start_date": "1938-05",
            "end_date": "1942-02",
            "date_precision": "Foreign Service Journal advertisements name Colonel Campbell Turner in May 1938 and as director in February 1942. They do not identify the indexed OSS file or the date of OSS entry.",
            "city": "Alexandria",
            "state_or_region": "Virginia",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "probable",
            "claim_confidence": "medium",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "publish_qualified",
            "research_notes": "Qualified institutional affiliation. The exact-name chronology is strong, but Box 789 must bridge the school director to the indexed person before the relationship can enter default analytics.",
        }
    )
    return values


def claim(
    row: int,
    key: str,
    claim_type: str,
    claim_text: str,
    evidence_paraphrase: str,
    identity_assessment: str,
    temporal_assessment: str,
    source_quality: str,
    confidence: str,
    source_links: list[dict[str, str]],
    notes: str,
    affiliation_key: str | None = None,
    publication_status: str = "published",
) -> dict[str, object]:
    value: dict[str, object] = {
        "key": key,
        "person_id": PEOPLE[row][0],
        "claim_type": claim_type,
        "claim_text": claim_text,
        "evidence_paraphrase": evidence_paraphrase,
        "identity_match_assessment": identity_assessment,
        "temporal_assessment": temporal_assessment,
        "source_quality": source_quality,
        "claim_confidence": confidence,
        "publication_status": publication_status,
        "match_notes": notes,
        "sources": source_links,
    }
    if affiliation_key:
        value["affiliation_key"] = affiliation_key
    return value


def army_claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    rows = [int(item["row"]) for item in ARMY_OCCUPATIONS] + list(IDENTITY_ONLY)
    for row in rows:
        name = PEOPLE[row][1]
        note = army_identity_note(row)
        date = next(
            (str(item["date"]) for item in ARMY_OCCUPATIONS if item["row"] == row),
            str(IDENTITY_ONLY.get(row, {}).get("date", "")),
        )
        values.append(
            claim(
                row,
                f"identity-{slug(name)}-b970",
                "identity",
                f"Indexed {name} is high-confidence matched to a reviewed official Army record.",
                note,
                note,
                f"The official Army entry date is {date}; it establishes military-entry chronology but not the exact OSS transfer date.",
                "A_direct_official",
                "high",
                [{"source_key": INDEX}, {"source_key": ARMY}, {"source_key": TECH}],
                "Protected identifiers were used only for private resolution and remain absent from the evidence bundle and public output.",
            )
        )

    for item in ARMY_OCCUPATIONS:
        row = int(item["row"])
        name = PEOPLE[row][1]
        relation = "other_pre_oss_affiliation" if item["code"] == "992" else "occupation"
        temporal = (
            "The 1945 Army-entry date falls within the final months of OSS and its relation to this person's OSS service is uncertain; no institution or employer is named."
            if item["temporal_basis"] == "temporal_relation_uncertain"
            else "Dated at Army entry before the later OSS-index context; no employer, school, workplace or exact OSS-transfer date is named."
        )
        values.append(
            claim(
                row,
                f"occupation-{slug(name)}-b970",
                relation,
                f"At Army entry on {item['date']}, {name}'s historical civilian-status category was {str(item['occupation']).lower()}.",
                f"The official Army field carries historical code {item['code']}; NARA's code list defines it as {item['occupation']}.",
                army_identity_note(row),
                temporal,
                "A_direct_official",
                "medium",
                [
                    {"source_key": ARMY, "locator_override": "Accepted identity bridge; protected identifier and raw record withheld"},
                    {"source_key": TECH, "locator_override": "PDF physical pages 44-46; civilian-occupation field"},
                    {"source_key": CODES, "locator_override": str(item["locator"])},
                ],
                "Published as qualified occupation or student status only; excluded from verified-employer analytics.",
                f"{slug(name)}-occupation-b970",
                "publish_qualified",
            )
        )
    return values


def campbell_claims() -> list[dict[str, object]]:
    return [
        claim(
            37,
            "identity-campbell-turner-b970",
            "identity",
            "Indexed Campbell Turner is a probable match to Colonel Campbell Turner, director of Turner's Diplomatic School.",
            "Contemporary advertisements use the exact name in 1938 and again in February 1942, but neither identifies OSS service or Box 789.",
            "Probable exact-name match across a continuous, unusually specific prewar institutional record; the personnel file is still needed for a direct identity bridge.",
            "The advertisements document activity through February 1942 but do not establish when the indexed person entered OSS.",
            "C_reputable_contemporary_or_scholarly",
            "medium",
            [
                {"source_key": INDEX},
                {"source_key": FSJ_1938, "excerpt_override": "COLONEL CAMPBELL TURNER"},
                {"source_key": FSJ_1942, "excerpt_override": "COLONEL CAMPBELL TURNER, Director"},
            ],
            "Published only as a qualified identity lead and excluded from default analytics until Box 789 confirms the match.",
            publication_status="publish_qualified",
        ),
        claim(
            37,
            "affiliation-campbell-turner-school-b970",
            "other_pre_oss_affiliation",
            "A probable Campbell Turner served as director of Turner's Diplomatic School from at least 1938 through February 1942.",
            "Foreign Service Journal advertisements identify Colonel Campbell Turner with the school in 1938 and as its director in February 1942.",
            "Probable identity; exact name and continuous institution-specific chronology, without a direct OSS or Box 789 bridge.",
            "Documented before OSS was established, but neither immediate pre-OSS status nor a last civilian employer is established.",
            "C_reputable_contemporary_or_scholarly",
            "medium",
            [
                {"source_key": FSJ_1938, "excerpt_override": "COLONEL CAMPBELL TURNER"},
                {"source_key": FSJ_1942, "excerpt_override": "COLONEL CAMPBELL TURNER, Director"},
            ],
            "Modeled as a professional affiliation rather than employment because the advertisements state the role but not the employment arrangement.",
            "campbell-turner-diplomatic-school-b970",
            "publish_qualified",
        ),
    ]


def claims() -> list[dict[str, object]]:
    return army_claims() + campbell_claims()


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
    values = [
        base_update(
            row,
            identity_status="unresolved",
            identity_evidence=f"The visually verified index row supplies {PEOPLE[row][1]}, Box {'790' if row >= 45 else '789'} and archive location 230/86/42/03. {reason}",
            personnel_category="unknown_or_indeterminate",
            commissioned_officer=None,
            allied_or_foreign_personnel=None,
            research_status="requires_archival_review",
            next_action=f"Review the indexed personnel file for corroborating identifiers, immediate pre-OSS affiliation and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}",
        )
        for row, reason in UNRESOLVED.items()
    ]

    for item in ARMY_OCCUPATIONS:
        row = int(item["row"])
        values.append(
            base_update(
                row,
                identity_status="high_confidence",
                identity_evidence=army_identity_note(row),
                name_variants=item.get("variants"),
                personnel_category="enlisted_army_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                research_status="occupation_only_found",
                next_action=(
                    "Review Box 365 at archive location 230/86/33/06 to resolve the Turlano/Iurlano surname discrepancy and establish the immediate pre-OSS affiliation and named last civilian employer."
                    if row == 27
                    else "Review the indexed personnel file to establish the immediate pre-OSS affiliation and named last civilian employer; do not convert the Army occupation category into a workplace."
                ),
            )
        )

    for row, item in IDENTITY_ONLY.items():
        values.append(
            base_update(
                row,
                identity_status="high_confidence",
                identity_evidence=item["note"],
                personnel_category="enlisted_army_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                research_status="requires_archival_review",
                next_action="Review the indexed personnel file to establish the immediate pre-OSS affiliation and last civilian employer; no usable historical occupation category was established.",
            )
        )

    values.append(
        base_update(
            37,
            identity_status="probable",
            identity_evidence="Contemporary Foreign Service Journal advertisements use the exact name Colonel Campbell Turner with Turner's Diplomatic School from 1938 through February 1942, but neither source identifies OSS service or Box 789.",
            name_variants=["Colonel Campbell Turner"],
            personnel_category="unknown_or_indeterminate",
            commissioned_officer=None,
            allied_or_foreign_personnel=None,
            research_status="requires_archival_review",
            next_action="Review Box 789 to confirm whether the indexed person directed Turner's Diplomatic School and determine whether that affiliation was immediate before OSS entry or a last civilian employer.",
        )
    )
    return values


def research_attempts() -> list[dict[str, object]]:
    source_review_rows = set([int(item["row"]) for item in ARMY_OCCUPATIONS]) | set(IDENTITY_ONLY) | {37}
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        if row in source_review_rows:
            outcome = "source_reviewed"
            reviewed = 7 if row in {27, 37, 44} else 5
            rejected = 5
            detail = "Reviewed official, institutional, contemporary or archival evidence produced the identity, occupation, student, institutional-affiliation or identity-only outcome recorded in the evidence bundle."
        else:
            outcome = "no_result"
            reviewed = 6
            rejected = 6
            detail = UNRESOLVED[row]
        special_rejection = ""
        if row == 44:
            special_rejection = " Contemporary Utah newspaper references to another Marden Turner were rejected because their National Guard/Air Corps chronology conflicts with the protected-identifier-linked Army-entry chronology."
        if row == 26:
            special_rejection = " A Ritchie Boys roster search result was retained only as a lead and rejected as final evidence because no inspectable source or second identifier bridged it to the index row."
        attempts.append(
            {
                "key": f"page475-row{row}-{slug(name)}-b970",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index and official Archives context; CIA Reading Room or equivalent official-source check; exact-name and meaningful variants; OSS, Army, rank and unit clues; employer and occupation 1940; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Boxes 365 and 789-790; protected identifiers used only when defensible",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_970",
                "started_at": "2026-10-30T12:30:00Z",
                "completed_at": "2026-10-30T16:15:00Z",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search snippets, unsourced genealogy, people-finder pages, postwar-only employment leads and sources without an OSS, protected-identifier or personnel-file bridge were rejected. Historical occupation codes, military service and student status were not silently converted into employers." + special_rejection,
                "research_notes": f"{detail} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain, CIA Reading Room-equivalent and Library of Congress searches were checked as applicable. The index page, Army bulk file, technical documentation and occupation-code pages were inspected directly. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": f"Review the indexed Box {'365' if row == 27 else ('790' if row >= 45 else '789')} personnel file for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before wartime service.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b970-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-970-v1",
        "reviewer": "Before OSS Batch 970 evidence review",
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
