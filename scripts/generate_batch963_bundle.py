#!/usr/bin/env python3
"""Generate the reviewed Batch 963 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page472-harry-trainosky-to-william-treat-"
    "review_batch-963_2026-10-29.json"
)

INDEX = "nara-index-b963"
ARMY = "army-bulk-b963"
TECH = "army-tech-b963"
CODES = "army-codes-b963"
OSS_BOARD_INDEX = "hoover-oss-board-index-b963"


PEOPLE = {
    3: ("b1cfbbc5-6503-554d-a4a0-ce2de319f5b5", "Harry Trainosky"),
    4: ("d4d935e2-f749-585e-a087-6195e37b7cd9", "Athenesios P Traintos"),
    5: ("c4049a48-3c09-5c37-a934-14fc0b2104a1", "Fannie M Tramantano"),
    6: ("f9e08d73-0e00-5ab2-b46f-0ee7aa4e5c63", "Albert Tramonti"),
    7: ("9211fdc5-2eed-5089-b58f-267735773d09", "Kurt E Trampel"),
    8: ("ca5871a0-fa0d-5074-b8fd-479ab1d94a32", "Anthony Tramuta"),
    9: ("95f03c8b-794a-5d5d-a27d-78745588690d", "Jack Tranes"),
    10: ("83412f4c-4834-50aa-8a36-6eadd50cc2a5", "Lillian Trangott"),
    11: ("5443535b-811d-52b5-b22a-c1ecebf95ac7", "F W Trapwell"),
    12: ("ca9be871-b625-5062-b435-0b2bca887810", "George M Trate"),
    13: ("2f3399a1-d162-51b3-967f-d04e5db13d51", "Alvin W Traub"),
    14: ("fd434428-30e6-5a00-8110-22429c5aa2dd", "Lillian Traugott"),
    15: ("3aae401a-368a-54f0-99b0-94054a258037", "Ralph C Traunecker"),
    16: ("f1c861af-67f0-58e3-9723-ecf7bb570960", "Marcella M Traut"),
    17: ("627fe0bd-a41b-577c-bbe2-da49b5dc3b46", "Vincent D Travaglini"),
    18: ("3aa9d2e9-6ce3-5dd7-9b59-87a7fff7e36d", "Helen E Travers"),
    19: ("6816b766-c089-5688-8d1e-e06141ba4af1", "Thomas J Travers"),
    20: ("e9ec8843-c86e-551d-95a7-4f4d33ccc4ed", "George Travis"),
    21: ("802721f2-ad68-56db-acd3-6c7cc6c0b545", "James Travis"),
    22: ("461c6ca0-13b8-573a-a1b3-b3769821399e", "Leo M Traynor"),
    23: ("5f06d6a6-99ce-50f5-a14f-58bf750abe74", "Emerson Treacy"),
    24: ("0e9f2d7d-8b3f-54bd-ab7d-c08dabebf820", "Owen E Treanor"),
    25: ("34047313-8092-56ca-a1a2-f2963e964eb3", "William W Treat"),
}


ARMY_OCCUPATIONS = [
    {
        "row": 4,
        "date": "1943-01-27",
        "code": "992",
        "occupation": "Students",
        "public_occupation": "student",
        "relationship": "student",
        "locator": "PDF physical page 304; amended historical category 9-92",
        "variant": "Athenesios P Triantos",
    },
    {
        "row": 8,
        "date": "1941-01-27",
        "code": "105",
        "occupation": "Clerks, general office",
        "public_occupation": "general office clerk",
        "relationship": "employment",
        "locator": "PDF physical page 171; historical category 1-05",
    },
    {
        "row": 12,
        "date": "1942-10-14",
        "code": "108",
        "occupation": "Insurance clerks, n.e.c.",
        "public_occupation": "insurance clerk, not elsewhere classified",
        "relationship": "employment",
        "locator": "PDF physical page 171; historical category 1-08",
        "variant": "George M Trate Jr",
    },
    {
        "row": 13,
        "date": "1942-09-28",
        "code": "992",
        "occupation": "Students",
        "public_occupation": "student",
        "relationship": "student",
        "locator": "PDF physical page 304; amended historical category 9-92",
    },
    {
        "row": 15,
        "date": "1943-04-16",
        "code": "773",
        "occupation": "Cranemen, derrickmen, hoistmen, and shovelmen",
        "public_occupation": "craneman, derrickman, hoistman, or shovelman",
        "relationship": "employment",
        "locator": "PDF physical page 175; historical category 7-73",
    },
    {
        "row": 20,
        "date": "1942-03-20",
        "code": "175",
        "occupation": "Salespersons",
        "public_occupation": "salesperson",
        "relationship": "employment",
        "locator": "PDF physical page 171; historical category 1-75",
        "variant": "George Travis Jr",
    },
]


UNRESOLVED = {
    3: "The protected identifier produced no defensible Army bulk candidate, and exact-name searches produced no reliable identity or employment bridge.",
    5: "Exact-name, OSS, occupation, obituary, institutional, newspaper and archival searches produced no defensible identity bridge.",
    6: "The name is insufficiently distinctive and public searches did not supply corroborating identifiers tying a namesake to Box 783.",
    7: "The protected identifier produced no Army bulk candidate, and exact-name and spelling-variant searches did not establish a reliable namesake.",
    9: "The protected identifier produced no Army bulk candidate; an unrelated modern document hit and unbridged namesakes were rejected.",
    10: "The index also prints Lillian Traugott four rows later in the same box, but no direct source establishes duplication or either woman's identity.",
    11: "The initials-only name and lack of a protected identifier produced no reliable identity or pre-OSS affiliation bridge.",
    14: "The index also prints Lillian Trangott four rows earlier in the same box, but no direct source establishes duplication or either woman's identity.",
    16: "Exact-name, occupation, obituary, institutional, newspaper and archival searches produced no reliable identity bridge.",
    17: "A rare-name postwar Commerce official is a plausible lead, but no independent source connects that biography to OSS or Box 784, so it was rejected as final evidence.",
    18: "The common name and middle initial produced no corroborating identifier beyond the index row.",
    19: "The common name and middle initial produced no corroborating identifier beyond the index row.",
    21: "The common name produced no corroborating identifier beyond the index row.",
    22: "Exact-name searches produced family and obituary leads but no source connecting a namesake to OSS, Box 784 or a pre-OSS affiliation.",
    23: "The actor and wartime Office of War Information writer is a plausible exact-name lead, but no independent source connects that biography to OSS or Box 784, so it was not assigned.",
    25: "The later New Hampshire judge and banker is a plausible exact-name lead, but no independent source connects that biography to OSS or Box 784, so it was not assigned.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 783-785",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 472, rows 3-25; checked against layout-preserving text and the 300 dpi page render",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. Lillian Trangott and Lillian Traugott remain an unresolved possible-duplicate pair. Protected identifiers remain private.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; six accepted Batch 963 identity candidates; protected identifiers withheld",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "No raw bulk row, record ordinal or full protected identifier enters the evidence bundle or public assets. Historical occupation codes identify neither employers nor workplaces.",
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
            "access_date": "2026-10-29",
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
            "locator": "PDF physical pages 171, 175 and 304; categories 1-05, 1-08, 1-75, 7-73 and amended 9-92 visually checked",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Students is status, not employment. Other historical labels are qualified and never converted into named employers or exact workplaces.",
        },
        {
            "key": OSS_BOARD_INDEX,
            "stable_url": "https://digitalcollections.hoover.org/internal/media/dispatcher/331574/full",
            "title": "Index of Personnel Interviewed in the North African and Italian Theater",
            "author_creator": "Office of Strategic Services review board",
            "repository_publisher": "Hoover Institution Library & Archives",
            "publication_record_date": "1944",
            "locator": "PDF page 19, entry 555; Owen E. Treanor, first lieutenant, Algiers, report page 37",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "Hoover Institution Digital Collections",
            "rights_notes": "The review-board index confirms wartime OSS rank and station but does not identify a pre-OSS employer or prior military assignment.",
        },
    ]


def army_affiliation(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    return {
        "key": f"{slug(PEOPLE[row][1])}-occupation-b963",
        "person_id": PEOPLE[row][0],
        "occupation": item["public_occupation"],
        "relationship_type": item["relationship"],
        "end_date": item["date"],
        "date_precision": f"Historical civilian-occupation code {item['code']} was recorded at Army entry on {item['date']}; no employer, school, workplace or OSS-transfer date is named.",
        "country": "United States",
        "immediate_pre_oss": False,
        "last_civilian_pre_service": False,
        "pre_oss_temporal_basis": "strongly_date_bounded",
        "identity_confidence": "high_confidence",
        "claim_confidence": "medium",
        "source_quality": "A_direct_official",
        "publication_status": "publish_qualified",
        "research_notes": "The historical category is not converted into a named employer, workplace, school, immediate affiliation or exact modern job title.",
    }


def claim(
    row: int,
    key: str,
    claim_type: str,
    claim_text: str,
    evidence_paraphrase: str,
    identity: str,
    temporal: str,
    source_quality: str,
    confidence: str,
    source_links: list[dict[str, object]],
    notes: str,
    affiliation_key: str | None = None,
    publication_status: str | None = None,
) -> dict[str, object]:
    return {
        "key": key,
        "person_id": PEOPLE[row][0],
        "affiliation_key": affiliation_key,
        "claim_type": claim_type,
        "claim_text": claim_text,
        "evidence_paraphrase": evidence_paraphrase,
        "identity_match_assessment": identity,
        "temporal_assessment": temporal,
        "source_quality": source_quality,
        "claim_confidence": confidence,
        "publication_status": publication_status
        or ("published" if confidence in {"confirmed", "high"} else "publish_qualified"),
        "match_notes": notes,
        "sources": source_links,
    }


def army_claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for item in ARMY_OCCUPATIONS:
        row = int(item["row"])
        name = PEOPLE[row][1]
        variant = item.get("variant")
        identity_paraphrase = "A nonshared protected identifier connects the visually verified index row to the official Army record."
        identity_assessment = "High confidence from exact protected-identifier agreement plus compatible full-name evidence."
        if variant:
            identity_paraphrase += f" The Army record prints the preserved variant {variant}."
            identity_assessment = "High confidence from exact protected-identifier agreement, rare or compatible given names and a minor spelling or suffix variation."
        values.append(
            claim(
                row,
                f"identity-{slug(name)}-army-b963",
                "identity",
                f"Indexed {name} is a high-confidence match to the reviewed official Army entry.",
                identity_paraphrase,
                identity_assessment,
                "Identity evidence only; the Army entry does not itself establish an OSS transfer date.",
                "A_direct_official",
                "high",
                [
                    {"source_key": INDEX, "locator_override": f"PDF page 472 row {row}; protected identifier withheld"},
                    {"source_key": ARMY, "locator_override": "Accepted reviewed identity bridge; protected identifier withheld"},
                ],
                "The review accepts identity only for this source row, preserves source spellings and does not expose the protected identifier.",
            )
        )
        category = str(item["occupation"])
        if item["relationship"] == "student":
            text = f"At Army entry on {item['date']}, {name} was recorded in the historical Students category; no school or employer is identified."
        else:
            text = f"At Army entry on {item['date']}, the record coded {name}'s civilian occupation as {category}."
        values.append(
            claim(
                row,
                f"occupation-{slug(name)}-army-b963",
                "occupation",
                text,
                f"The official Army record contains civilian-occupation code {item['code']}; NARA's historical code list expands it to {category}.",
                "High-confidence identity from the accepted protected-identifier bridge and compatible exact or preserved-variant name evidence.",
                "The code was recorded at Army entry and is date-bounded, but it identifies no employer, workplace, school or immediate OSS predecessor.",
                "A_direct_official",
                "medium",
                [
                    {"source_key": ARMY, "locator_override": f"Accepted identity record; civilian occupation code {item['code']}; protected identifier withheld"},
                    {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46; Army-entry-date and civilian-occupation fields"},
                    {"source_key": CODES, "locator_override": str(item["locator"]), "excerpt_override": category},
                ],
                "The historical category is published as qualified occupation or status evidence and is excluded from named-employer analytics.",
                f"{slug(name)}-occupation-b963",
                "publish_qualified",
            )
        )
    return values


def claims() -> list[dict[str, object]]:
    values = army_claims()
    values.append(
        claim(
            24,
            "identity-owen-treanor-board-b963",
            "identity",
            "The indexed Owen E. Treanor is a high-confidence match to the first lieutenant interviewed by the OSS review board in Algiers.",
            "A direct wartime OSS index supplies the rare exact full name, first-lieutenant rank, Algiers station and its detailed-report locator.",
            "High confidence from a rare exact full name in two direct OSS record series plus compatible wartime context.",
            "The source confirms wartime rank and station but does not identify the preceding employer or military assignment.",
            "A_direct_official",
            "high",
            [
                {"source_key": INDEX, "locator_override": "PDF page 472 row 24; Box 784; protected identifier withheld"},
                {"source_key": OSS_BOARD_INDEX, "locator_override": "PDF page 19, entry 555; report page 37", "excerpt_override": "Treanor, Owen E. 1st Lt. Algiers"},
            ],
            "The protected identifier remains private. The Box 784 personnel file and detailed board report are still required for the pre-OSS question.",
        )
    )
    return values


def unresolved_update(row: int, reason: str) -> dict[str, object]:
    person_id, name = PEOPLE[row]
    duplicate = "batch963-lillian-trangott-traugott" if row in {10, 14} else None
    return {
        "person_id": person_id,
        "identity_status": "ambiguous" if duplicate else "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, Box 784 and archive location 230/86/42/02. {reason}",
        "personnel_category": "unknown_or_indeterminate",
        "commissioned_officer": None,
        "allied_or_foreign_personnel": False,
        "manual_review_required": True,
        "possible_duplicate_group": duplicate,
        "research_status": "requires_archival_review",
        "next_action": "Review the indexed personnel file for corroborating identifiers, immediate pre-OSS affiliation and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "critical" if duplicate else "high",
    }


def army_update(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    person_id, name = PEOPLE[row]
    evidence = f"A nonshared protected identifier connects the visually verified {name} index row to the reviewed official Army record."
    update: dict[str, object] = {
        "person_id": person_id,
        "identity_status": "high_confidence",
        "identity_evidence": evidence,
        "personnel_category": "enlisted_army_personnel",
        "commissioned_officer": False,
        "allied_or_foreign_personnel": False,
        "manual_review_required": True,
        "research_status": "occupation_only_found",
        "next_action": "Review Box 784 or 785 to establish the immediate pre-OSS affiliation and named last civilian employer; do not convert the Army occupation category into a workplace.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }
    if item.get("variant"):
        update["name_variants"] = [item["variant"]]
        update["identity_evidence"] = f"{evidence} The Army record preserves the compatible variant {item['variant']}."
    return update


def person_updates() -> list[dict[str, object]]:
    values = [unresolved_update(row, reason) for row, reason in UNRESOLVED.items()]
    values.extend(army_update(item) for item in ARMY_OCCUPATIONS)
    values.append(
        {
            "person_id": PEOPLE[24][0],
            "identity_status": "high_confidence",
            "identity_evidence": "A direct wartime OSS review-board index independently prints the rare exact name Owen E. Treanor as a first lieutenant stationed at Algiers.",
            "personnel_category": "commissioned_army_officer",
            "commissioned_officer": True,
            "allied_or_foreign_personnel": False,
            "manual_review_required": True,
            "research_status": "requires_archival_review",
            "next_action": "Review Box 784 and the detailed review-board report page 37 to identify Owen Treanor's immediate pre-OSS assignment and last civilian employer.",
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
            "archival_review_priority": "high",
        }
    )
    return values


def research_attempts() -> list[dict[str, object]]:
    army_rows = {int(item["row"]) for item in ARMY_OCCUPATIONS}
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        if row in army_rows:
            outcome, reviewed, rejected = "source_reviewed", 8, 4
            detail = "Accepted an exact nonshared protected-identifier Army bridge and verified the dated historical civilian-occupation code against NARA technical documentation."
        elif row == 24:
            outcome, reviewed, rejected = "source_reviewed", 8, 5
            detail = "A direct wartime OSS review-board index confirmed the rare exact full name, first-lieutenant rank and Algiers station, but not a pre-OSS employer."
        else:
            outcome, reviewed, rejected = "no_result", 7, 6
            detail = UNRESOLVED[row]
        attempts.append(
            {
                "key": f"page472-row{row}-{slug(name)}-b963",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index and official Archives context; CIA Reading Room or equivalent official-source check; exact-name and meaningful variants; OSS, Army and rank clues; employer and occupation 1940; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Boxes 783-785; protected identifiers used only when defensible",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_963",
                "started_at": "2026-10-30T01:40:00Z",
                "completed_at": "2026-10-30T04:30:00Z",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search snippets, unsourced genealogy, people-finder pages, postwar-only leads and sources without an OSS, protected-identifier or Box-file bridge were rejected. Education and occupation categories were not converted into named employers. Search aliases were not treated as silent corrections.",
                "research_notes": f"{detail} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain, CIA Reading Room-equivalent and Library of Congress searches were checked as applicable. The index page, Army bulk file, technical documentation and occupation-code pages were inspected directly. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": "Review the indexed personnel file for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before wartime service.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b963-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-963-v1",
        "reviewer": "Before OSS Batch 963 evidence review",
        "sources": sources(),
        "organizations": [],
        "affiliations": [army_affiliation(item) for item in ARMY_OCCUPATIONS],
        "claims": claims(),
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }
    EvidenceBundle.model_validate(bundle)
    OUTPUT.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
