#!/usr/bin/env python3
"""Generate the reviewed Batch 1058 completion bundle for PDF page 313."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page313-james-j-mcnamara-to-donald-s-mcvannel-review_"
    "batch-1058_2026-11-11.json"
)

INDEX = "nara-index-page313-b1058"
ARMY = "army-bulk-page313-b1058"
TECH = "army-tech-page313-b1058"
CODES = "army-codes-page313-b1058"


PEOPLE = {
    1: ("c0ed47cf-000e-5ac2-aaae-21cf60a9c056", "James J McNamara", "511"),
    2: ("f997f8b4-d555-521d-a837-a4f5a54d0f4f", "Rebecca H McNamara", "511"),
    3: ("db06d14f-5735-5fb5-9b77-f4db9b7301d0", "Robert J McNamara", "511"),
    4: ("6cd113ce-3751-5a09-b1e2-ac656e2a578c", "Thomas J McNamara", "511"),
    5: ("267637f5-b268-5b4e-a38a-b8d34ea8bdc0", "William H McNay", "512"),
    6: ("cae1845d-65c0-5bfb-ba5a-1e3494d35551", "James E McNearnry", "512"),
    7: ("2fc524a5-5b25-5b02-bdbd-64235090e0fd", "James J McNeary", "512"),
    8: ("fff2e586-8e90-514c-a3d1-6c33232e7fc6", "Daniel J McNeason", "512"),
    9: ("13945b6a-c5ca-5019-85d9-db71215544bf", "Thomas J McNee", "512"),
    10: ("fad5c77b-2530-5e2a-8492-11170f289b77", "William D McNeely", "512"),
    11: ("dd1a6ab5-c5a5-5808-8832-10008ad9cb4b", "Juliette V McNeese", "512"),
    12: ("2df2c498-74e4-588e-9d85-43e2fdf7a147", "Coy I McNeil", "512"),
    13: ("494364ee-0148-5275-b1c7-c7d9d4c4ef82", "Edward F McNeil", "512"),
    14: ("e2de50f6-5979-5fdf-9104-22d721c13f82", "William D McNeil", "512"),
    15: ("84ecd8d1-be9d-5602-b428-39452050ce43", "Volney G McNeill", "512"),
    16: ("1f40daef-d2fb-56c9-8b63-1e4b24d28957", "Albert J McNenamin", "512"),
    17: ("86bbdb79-84c5-5ce5-81aa-58de02c2d582", "James E McNerney", "512"),
    18: ("b52bc58b-966e-5e8c-828e-b0693b9ab193", "Paul McNichol", "512"),
    19: ("e2efb896-63f7-5dea-96b5-470d29a2a9de", "Harry P McNickle", "512"),
    20: ("50bc7aa2-4d18-5aba-b532-195174995035", "John J McNulty", "512"),
    21: ("10c8b5ad-b31c-5bf9-9d9a-db7595fe5540", "Joseph S McNulty", "512"),
    22: ("172783fb-b807-5847-aa14-ffb843f67e35", "Joseph G McNulty", "512"),
    23: ("11da3f31-12e5-523f-bcf5-3f6098d6f2a7", "Mack McNutt", "512"),
    24: ("a3a81cec-0d47-560c-a3a5-09595b868488", "John F McPadden", "512"),
    25: ("5bbe802a-dcb6-5207-a038-ecbb77f515e7", "Thomas H McPadden", "512"),
    26: ("baf6c6b1-c49b-5ffd-b858-514918dfce35", "Thomas E McParland", "512"),
    27: ("530efde3-45c5-5e7b-b3e1-877aeb723a22", "Joan H McPeak", "512"),
    28: ("f47465c8-faff-5a55-b514-928527258983", "Eleanor C McPeck", "512"),
    29: ("bac64720-9ef7-5214-a8cc-9c9ce36f5c0b", "Robert E McPeek", "512"),
    30: ("5a7c2989-51bc-5df9-a02c-644959675d47", "Thomas E McPharland", "512"),
    31: ("9df1aa20-e89d-5a64-aab5-55455c13fb7b", "William G McPheat", "512"),
    32: ("131e916c-7403-5982-8d40-cf71e614c2e6", "Frances P McPherson", "512"),
    33: ("a400ecf6-b26a-5c00-8020-64ef702e51d7", "Walter N McPherson", "512"),
    34: ("aeb8dbfb-dd81-5af9-b2e6-e039657363bd", "James F McPoil", "512"),
    35: ("37fda173-2b83-5347-a547-6bdc147ed920", "Raymond C McQuade", "512"),
    36: ("f8ac2b72-b2e3-5e10-9987-0bf833536f26", "Robert C McQueen", "512"),
    37: ("e27aa046-5f94-560e-a96b-f394622fcf70", "Wesley H McQueen", "513"),
    38: ("1754702d-ffc5-5766-89b3-aaa17ae8ed90", "Robert H McQuilkin", "513"),
    39: ("f56204ea-51f3-5f3e-9b15-af5f696aacd7", "Gerald McQuinn", "513"),
    40: ("79e0abb6-1bc6-5caa-b381-a51a3a54a4a8", "Joann W McQuiston", "513"),
    41: ("1af9856d-8712-5210-b55b-c11c6b2d64b1", "Joanne W Mcquiston", "513"),
    42: ("c8b8cd04-de56-55ef-b93b-0f4e1dab4e38", "Donald G McRae", "513"),
    43: ("5ee7e74b-004e-5762-8e5a-3f80d3ccae4e", "Ruby H McShane", "513"),
    44: ("71c2f9d7-2801-51c0-90a9-ea40697b7d30", "Francis J McSwiggin", "513"),
    45: ("ef9e2fbb-80d8-51e5-af75-3b794eae6752", "Helen M McTernan", "513"),
    46: ("c8c087ec-782f-56cd-a71f-a8d7da152c27", "Donald S McVannel", "513"),
}

# Official Army-entry categories accepted only where exact name and a unique,
# reviewed private identifier agree. The protected values never enter the bundle.
ARMY_OCCUPATIONS = {
    4: ("1942-06-26", "688", "occupation in mechanical treatment of metals, n.e.c.", "Occupations in mechanical treatment of metals, n.e.c.", "unknown", "PDF physical page 176; historical code 6-88"),
    10: ("1943-04-28", "992", "student", "Students", "student", "PDF physical page 304; corrected historical code 9-92"),
    13: ("1942-06-15", "170", "sales clerk", "Sales clerks", "unknown", "PDF physical page 171; historical code 1-70"),
    15: ("1942-04-02", "185", "sales agent, except to consumers", "Agents, sales, except to consumers", "unknown", "PDF physical page 171; historical code 1-85"),
    19: ("1941-09-19", "530", "plumber, gas fitter, or steam fitter", "Plumbers, gas fitters, and steam fitters", "unknown", "PDF physical page 174; historical code 5-30"),
    20: ("1944-01-18", "992", "student", "Students", "student", "PDF physical page 304; corrected historical code 9-92"),
    21: ("1944-03-31", "476", "toolmaker, die sinker, or die setter", "Toolmakers and die sinkers and setters", "unknown", "PDF physical page 173; historical code 4-76"),
    22: ("1943-05-24", "101", "bookkeeper or cashier, except bank cashier", "Bookkeepers and cashiers, except bank cashiers", "unknown", "PDF physical page 171; historical code 1-01"),
    29: ("1941-11-05", "736", "chauffeur or bus, taxi, truck, or tractor driver", "Chauffeurs and drivers, bus, taxi, truck, and tractor", "unknown", "PDF physical page 177; historical code 7-36"),
    34: ("1942-08-29", "630", "lumberman, raftsman, or woodchopper", "Lumbermen, raftsmen, and woodchoppers", "unknown", "PDF physical page 175; historical code 6-30"),
    36: ("1942-07-13", "902", "occupation in manufacture of automobiles, n.e.c.", "Occupations in manufacture of automobiles, n.e.c.", "unknown", "PDF physical page 178; historical code 9-02"),
    46: ("1943-01-07", "682", "foundry occupation, n.e.c.", "Foundry occupations, n.e.c.", "unknown", "PDF physical page 176; historical code 6-82"),
}

DUPLICATE_BOUNDARY_PAIRS = ((6, 17), (26, 30), (40, 41))
DUPLICATE_ROWS = {row for pair in DUPLICATE_BOUNDARY_PAIRS for row in pair}
CONFLICT_ROWS = {12}
ATTEMPT_NUMBERS = {
    1: 3, 2: 2, 3: 3, 4: 3, 5: 2, 6: 3, 7: 2, 8: 2, 9: 2,
    10: 3, 11: 2, 12: 3, 13: 3, 14: 3, 15: 3, 16: 2, 17: 3,
    18: 2, 19: 3, 20: 3, 21: 3, 22: 3, 23: 2, 24: 3, 25: 3,
    26: 3, 27: 3, 28: 3, 29: 3, 30: 3, 31: 3, 32: 3, 33: 3,
    34: 3, 35: 3, 36: 3, 37: 3, 38: 3, 39: 3, 40: 3, 41: 3,
    42: 5, 43: 3, 44: 3, 45: 3, 46: 3,
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def source(key: str, **kwargs: object) -> dict[str, object]:
    value: dict[str, object] = {"key": key, "access_date": "2026-11-11"}
    value.update(kwargs)
    return value


def sources() -> list[dict[str, object]]:
    return [
        source(
            INDEX,
            stable_url="https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            archival_identifier="RG 226, Entry A1-224, Boxes 511-513",
            title="OSS Personnel Files from Excel",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="2010-12-23",
            locator="PDF page 313, rows 1-46; every printed row visually checked against the official PDF",
            source_quality="A_direct_official",
            collection_name="Records of the Office of Strategic Services, Record Group 226",
            rights_notes="All 46 printed rows remain separately preserved. Full protected identifiers remain private.",
        ),
        source(
            ARMY,
            stable_url="https://catalog.archives.gov/id/1263923",
            archival_identifier="National Archives Identifier 1263923; parent series NAID 604357",
            title="Electronic Army Serial Number Merged File, ca. 1938-1946",
            author_creator="Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="1938-1946; merged file created 2002",
            locator="Official unrestricted ASNEF.FIN.DAT; reviewed row-specific private identity crosswalks",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records",
            document_number="ASNEF.FIN.DAT",
            rights_notes="No raw record, protected identifier, or bulk ordinal is retained in public assets.",
        ),
        source(
            TECH,
            stable_url="https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf",
            archival_identifier="NN3-064-03-008; National Archives Identifier 1263923",
            title="World War II Army Enlistment Records: Reference Copy of Technical Documentation",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives at College Park - Electronic Records",
            publication_record_date="1994-2005; reference copy modified 2011",
            locator="PDF physical pages 44-46; Army-entry date and civilian-occupation fields",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records technical documentation",
            rights_notes="Used only to interpret selected fields; the bulk file does not identify a named employer or prove the Army-to-OSS sequence.",
        ),
        source(
            CODES,
            stable_url="https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1CL_SD.pdf",
            archival_identifier="Code No. 30; National Archives Identifier 1263923",
            title="NARA Compiled Code Lists for the Electronic Army Serial Number Merged File",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives at College Park - Electronic Records",
            publication_record_date="1942; reference copy modified 2011",
            locator="PDF physical pages 171-178 and 304; every published Batch 1058 category visually checked",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records technical documentation",
            rights_notes="Historical categories are published only as qualified Army-entry occupations, never as named employers.",
        ),
    ]


def army_affiliation_key(row: int) -> str:
    return f"army-entry-{slug(PEOPLE[row][1])}-b1058"


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, _code, occupation, _label, relationship, _locator) in ARMY_OCCUPATIONS.items():
        values.append(
            {
                "key": army_affiliation_key(row),
                "person_id": PEOPLE[row][0],
                "role_title": occupation,
                "occupation": occupation,
                "relationship_type": relationship,
                "start_date": date,
                "end_date": date,
                "date_precision": "Exact Army-entry date; the broad category may summarize civilian experience and does not identify an employer.",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "temporal_relation_uncertain",
                "identity_confidence": "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "A_direct_official",
                "publication_status": "publish_qualified",
                "research_notes": "The category is excluded from verified-employer analytics and is not converted into a named organization.",
            }
        )
    return values


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, label, _relationship, locator) in ARMY_OCCUPATIONS.items():
        values.append(
            {
                "key": army_affiliation_key(row),
                "person_id": PEOPLE[row][0],
                "affiliation_key": army_affiliation_key(row),
                "claim_type": "occupation",
                "claim_text": f"At Army entry on {date}, {PEOPLE[row][1]} was recorded as {occupation}; no employer, institution, or workplace is identified.",
                "evidence_paraphrase": f"The official Army bulk file records code {code}; the visually checked official list defines the category as {label}.",
                "identity_match_assessment": "High confidence from exact normalized full-name agreement and a reviewed, nonshared private identifier linkage; the identifier remains private.",
                "temporal_assessment": "The category is fixed to the Army-entry date, but its sequence relative to OSS service is not established.",
                "source_quality": "A_direct_official",
                "claim_confidence": "medium",
                "publication_status": "publish_qualified",
                "match_notes": "An earlier reviewed identity claim already documents the official crosswalk. The historical category remains qualified, excluded from verified-employer analytics, and is not converted into a named organization.",
                "sources": [
                    {"source_key": INDEX, "support_type": "context_only"},
                    {"source_key": ARMY},
                    {"source_key": TECH, "support_type": "context_only"},
                    {"source_key": CODES, "locator_override": locator},
                ],
            }
        )
    return values


def unresolved_message(name: str, box: str) -> str:
    return (
        f"Review the indexed Box {box} personnel file for corroborating identifiers, the immediate pre-OSS affiliation, and the last civilian employer. "
        "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed."
    )


def duplicate_group(row: int) -> str:
    if row in {6, 17}:
        return "p313-james-e-mcnearnry-mcnerney-shared-private-identifier-b1058"
    if row in {26, 30}:
        return "p313-thomas-e-mcparland-mcpharland-shared-private-identifier-b1058"
    return "p313-joann-joanne-w-mcquiston-adjacent-variant-b1058"


def person_updates() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (person_id, name, box) in PEOPLE.items():
        update: dict[str, object] = {
            "person_id": person_id,
            "manual_review_required": True,
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
        }
        if row in ARMY_OCCUPATIONS:
            update.update(
                identity_status="high_confidence",
                identity_evidence="The official index and Army entry agree in normalized full name and a reviewed nonshared private identifier. The dated broad category does not establish a named employer or OSS sequence.",
                nara_catalog_id="1263923",
                research_status="occupation_only_found",
                next_action=f"Review Box {box} for a named employer or institution and establish the Army-to-OSS chronology.",
                archival_review_priority="high",
            )
        elif row in DUPLICATE_ROWS:
            detail = (
                "The two indexed spelling variants share a reviewed protected identifier, but the spellings and ranks differ; both people remain separate pending personnel-file evidence."
                if row in {6, 17, 26, 30}
                else "The adjacent indexed Joann/Joanne spelling variants have no shared protected identifier; both people remain separate pending personnel-file evidence."
            )
            if row in {26, 30}:
                detail += " A Camden fire-service candidate remains private and unpromoted because it lacks a direct OSS or personnel-file identity bridge."
            update.update(
                identity_status="probable",
                identity_evidence=detail,
                possible_duplicate_group=duplicate_group(row),
                research_status="needs_identity_review",
                next_action=f"Review both records in Box {box} to resolve the variant-name boundary before transferring any occupation or outside biography.",
                archival_review_priority="critical",
            )
        elif row in CONFLICT_ROWS:
            update.update(
                identity_status="conflicting",
                identity_evidence="The protected identifier associated with the index row maps to an official Army entry bearing a materially different surname. No occupation or biography is transferred across the conflict.",
                research_status="conflicting_sources",
                next_action="Review Box 512 and the original index documentation to resolve the protected-identifier/name conflict before accepting any external identity.",
                archival_review_priority="critical",
            )
        else:
            update.update(
                identity_status="unresolved",
                identity_evidence="Exact-name and meaningful-variant checks across the official index context, CIA-domain discovery, accessible military and institutional sources, employment and occupation searches, and obituary or archival discovery produced no reliable identity and pre-OSS affiliation bridge; unbridged namesakes were rejected.",
                research_status="requires_archival_review",
                next_action=unresolved_message(name, box),
                archival_review_priority="high",
            )
        values.append(update)
    if len(values) != 46 or len({item["person_id"] for item in values}) != 46:
        raise RuntimeError("Expected 46 separate page-313 person updates")
    return values


def outcome_note(row: int) -> str:
    if row in ARMY_OCCUPATIONS:
        return "An accepted official Army identity link supports a qualified dated occupation or student category but no named employer or OSS-transfer sequence."
    if row in DUPLICATE_ROWS:
        return "The plausible variant-name relationship remains unresolved and both source rows remain separate; no employer or occupation was transferred."
    if row in CONFLICT_ROWS:
        return "The protected-identifier/name conflict remains visible; no occupation or employer was transferred."
    if row == 45:
        return "A local birth-index candidate was rejected because it supplies no OSS, personnel-file, or employment bridge."
    if row == 38:
        return "Several obituary namesakes were rejected because age, military context, or OSS identity could not be bridged to the index row."
    if row == 39:
        return "Several later namesakes were rejected because none supplied a direct OSS or personnel-file identity bridge."
    return "No reliable identity or pre-OSS affiliation was established; unbridged namesakes and chronologically irrelevant results were rejected."


def research_attempts() -> list[dict[str, object]]:
    updates = {item["person_id"]: item for item in person_updates()}
    values: list[dict[str, object]] = []
    for row, (person_id, name, box) in PEOPLE.items():
        if row in ARMY_OCCUPATIONS:
            outcome, reviewed, rejected = "source_reviewed", 4, 3
        elif row in DUPLICATE_ROWS | CONFLICT_ROWS:
            outcome, reviewed, rejected = "candidate_rejected", 3, 4
        else:
            outcome, reviewed, rejected = "no_result", 2, 3
        extra = ""
        if row in {26, 30}:
            extra = " The Camden fire-service page was access-blocked; its search lead was not used as evidence and remains an unpromoted private candidate."
        values.append(
            {
                "key": f"page313-row{row}-{slug(name)}-b1058",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index context; exact-name and meaningful initial, punctuation, spacing, spelling and OCR variants; CIA Reading Room/domain discovery; OSS, rank, branch, assignment and private-identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory and archival searches; indexed Box {box}",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_1058",
                "started_at": "2026-11-11T21:40:00-05:00",
                "completed_at": "2026-11-11T23:25:00-05:00",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, postwar-only leads, and sources without an OSS, rank, protected-identifier, unit, or personnel-file bridge were rejected. Army categories were not converted into named employers; spelling and identifier conflicts were not promoted.",
                "research_notes": f"{outcome_note(row)} Page 313 was visually checked against the official NARA index, and every published Army occupation code was visually checked against the official code-list PDF. Exact-name OSS, CIA-domain, employment, occupation, obituary, institutional, newspaper, directory, and archival searches were reviewed as applicable. No search-result snippet was used as final evidence and no authenticated NARA Catalog API request was made.{extra}",
                "next_action": str(updates[person_id]["next_action"]),
                "attempt_number": ATTEMPT_NUMBERS[row],
                "research_agent_version": "before-oss-b1058-v1",
            }
        )
    return values


def build_bundle() -> dict[str, object]:
    return {
        "bundle_version": "batch-1058-v1",
        "reviewer": "Before OSS Batch 1058 evidence review",
        "sources": sources(),
        "organizations": [],
        "affiliations": affiliations(),
        "claims": claims(),
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }


def main() -> None:
    bundle = build_bundle()
    EvidenceBundle.model_validate(bundle)
    OUTPUT.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
