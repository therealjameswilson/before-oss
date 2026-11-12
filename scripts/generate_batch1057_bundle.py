#!/usr/bin/env python3
"""Generate the reviewed Batch 1057 completion bundle for PDF page 312."""

from __future__ import annotations

import json
import re
import sys
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page312-arthur-b-mclaughlin-to-george-t-mcnamara-review_"
    "batch-1057_2026-11-11.json"
)

INDEX = "nara-index-page312-b1057"
ARMY = "army-bulk-page312-b1057"
TECH = "army-tech-page312-b1057"
CODES = "army-codes-page312-b1057"
NPS = "nps-emmett-mcnamara-b1057"
SIGNAL_CORPS = "signal-corps-b1057"


# Rows 6 and 8 are separately preserved printed rows linked to one person because
# the normalized name and reviewed private identifier agree exactly.
PEOPLE = {
    1: ("b05b8495-345b-590f-bd85-87eb7ac517cb", "Arthur B McLaughlin", "510"),
    2: ("b716d0a6-b18c-55c9-addd-721ae710f134", "Donal McLaughlin", "510"),
    3: ("ab5edd1f-ad17-5d3f-b982-7dc1a0b4f1cc", "Frank W McLaughlin", "510"),
    4: ("169b969d-d244-5b28-bf73-4452b6bc2b35", "Gene J McLaughlin", "510"),
    5: ("116fc97e-96d1-5f5c-b97d-6e282c1e01d8", "James A McLaughlin", "510"),
    6: ("c3e47113-2f34-5958-8f4f-2915a2e0ee16", "John J McLaughlin", "510"),
    7: ("62b7e7a2-1c64-540b-94cf-1819c5e5ce61", "John P McLaughlin", "510"),
    8: ("c3e47113-2f34-5958-8f4f-2915a2e0ee16", "John J McLaughlin", "510"),
    9: ("e1b5046d-d09c-5945-bfba-ea16480faa84", "Juliet B McLaughlin", "510"),
    10: ("a94eff10-05c8-5e45-8b41-a693348eb20e", "Ruth M/S McLaughlin", "510"),
    11: ("90056aaa-8075-5a9e-b919-643b09768d06", "Virgina McLaughlin", "510"),
    12: ("ea3f0762-ee75-5ae6-ba35-60f66a152374", "Jane M McLean", "510"),
    13: ("a14fd49a-979e-5c9d-bac9-0b5390474c04", "Donald B McLennan", "510"),
    14: ("bb31e319-1344-5907-9f92-f6b72ab50caf", "Cyril McLeod", "510"),
    15: ("4f1b0b55-f38c-5dd0-a0d1-4ad44a3b2268", "Francis B McLeod", "510"),
    16: ("08ea0735-7c82-5864-8187-d3d32070c393", "Nancy I McLeod", "510"),
    17: ("e8a4cafb-51dd-580a-bdfe-c90beddbac6e", "John T McLoughlin", "510"),
    18: ("0f00812f-801f-5820-bc02-a7ca47e9931f", "Ellis R McLuckie", "510"),
    19: ("f69ec40e-d619-5c5d-bb6e-ec35e0240443", "James A McLuskey", "510"),
    20: ("19b2ffb9-b2ce-5495-9c2b-15f1494884cf", "Caroline B McMahon", "510"),
    21: ("c9553620-b2b3-52a7-87e7-6164444e79b6", "Eugene F McMahon", "510"),
    22: ("a6013069-83e6-58ba-bb6d-712e6c46f9a8", "Manning McMahon", "510"),
    23: ("151f290a-b097-5a8f-b7cf-c7faf214b293", "Robert F McMahon", "510"),
    24: ("53feb570-be38-5565-a47e-9791da63cbb3", "Virgina A McMahon", "510"),
    25: ("8453c16a-1c36-5cbc-8433-8f30fd990e50", "William J McMahon", "510"),
    26: ("0f222fe3-db20-59bf-b347-07392f886149", "Robert C McManamy", "510"),
    27: ("9fc27241-8b17-543c-a354-e5037fc09a4e", "Mary A McManus", "510"),
    28: ("39d7d890-0d36-5ab1-898f-ca0d2229b1bd", "Alfred D McMaster", "510"),
    29: ("f1f356b9-266d-5af2-a2ac-594d72bdf098", "Albert J McMenamin", "510"),
    30: ("9f25ccf6-1d83-5749-acd1-9bfe6406844d", "Elizabeth L McMillan", "510"),
    31: ("6850de4c-7e91-5bfd-91e7-ec0b7468e61e", "James D McMillan", "510"),
    32: ("6f81d270-10fe-5cb4-ae38-304d848a6699", "Walter F McMillan", "510"),
    33: ("c0478222-d055-5c2a-92bd-ea1c09ae7e7f", "Francis B McMohigal", "510"),
    34: ("1aabe396-b652-5c7b-9390-8dccadc36612", "Lewis H McMorris", "510"),
    35: ("56d7dc89-779e-54d6-883c-5bcd6fe437d5", "Harry W McMullen", "510"),
    36: ("cb14be75-ce0e-5a12-b1d8-e9dd7d7208e8", "John J McMullen", "511"),
    37: ("7261099a-9fd6-5445-b305-2c5f536d8522", "Frank D McMurray", "510"),
    38: ("f69fca86-79c3-55a0-845b-5f706ee4c6d5", "Jack A McMurtrie", "510"),
    39: ("89546f8e-9b61-5e5c-b66d-bcbd09c80d64", "Edward F McNair", "510"),
    40: ("19d26b79-9ae5-5b19-b43d-83cd71a0d7ab", "George E McNally", "511"),
    41: ("94ddb860-0807-58d2-8a20-1e7ebb0c0116", "Hubert A McNally", "511"),
    42: ("d928cf3d-2d0e-5905-b0f2-4e93d57c20fd", "John E McNally", "511"),
    43: ("228becf6-8f84-5dc3-97bb-25ebc221d819", "Lawerence D McNally", "511"),
    44: ("6c8575fb-21bd-5fbb-9f18-0a91042040ac", "Mayme O McNally", "511"),
    45: ("6422367f-34a3-5c72-9130-5af24fd15e02", "Emmett F McNamara", "511"),
    46: ("1c956fdc-ddf9-5d13-b528-23c32fb51fea", "George T McNamara", "511"),
}

UNIQUE_PEOPLE = OrderedDict()
for row, value in PEOPLE.items():
    UNIQUE_PEOPLE.setdefault(value[0], (row, *value))

ARMY_OCCUPATIONS = {
    5: ("1942-09-08", "992", "student", "Students", "student", "PDF physical page 304; corrected historical code 9-92"),
    18: ("1944-02-21", "992", "student", "Students", "student", "PDF physical page 304; corrected historical code 9-92"),
    23: ("1943-03-02", "002", "actor or actress", "Actors and actresses", "unknown", "PDF physical page 170; historical code 0-02"),
    25: ("1943-04-02", "266", "policeman or detective in public service", "Policemen and detectives, public service", "unknown", "PDF physical page 172; historical code 2-66"),
    40: ("1943-08-16", "992", "student", "Students", "student", "PDF physical page 304; corrected historical code 9-92"),
    43: ("1943-03-18", "238", "midwife or practical nurse", "Midwives and practical nurses", "unknown", "PDF physical page 172; historical code 2-38"),
    45: ("1943-04-13", "072", "retail manager", "Retail managers", "unknown", "PDF physical page 171; historical code 0-72"),
    46: ("1942-06-11", "225", "housekeeper, steward, or hostess", "Housekeepers, stewards, and hostesses", "unknown", "PDF physical page 172; historical code 2-25"),
}

IDENTITY_ONLY_ARMY = {19}
IDENTIFIER_CONFLICT_ROWS = {4, 26, 29, 31, 38}
MIDDLE_INITIAL_CONFLICT_ROWS = {32, 39}
ATTEMPT_NUMBERS = {
    1: 3, 2: 3, 3: 3, 4: 3, 5: 3, 6: 4, 7: 3,
    9: 2, 10: 2, 11: 2, 12: 2, 13: 3, 14: 2, 15: 3, 16: 2,
    17: 2, 18: 3, 19: 3, 20: 2, 21: 2, 22: 2, 23: 3,
    **{row: 1 for row in range(24, 47)},
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
            archival_identifier="RG 226, Entry A1-224, Boxes 510-511",
            title="OSS Personnel Files from Excel",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="2010-12-23",
            locator="PDF page 312, rows 1-46; every printed row visually checked against the official PDF",
            source_quality="A_direct_official",
            collection_name="Records of the Office of Strategic Services, Record Group 226",
            rights_notes="All 46 printed rows remain preserved. Full protected identifiers remain private. The printed PFC placement on Cyril McLeod's row remains flagged for visual review.",
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
            locator="PDF physical pages 170-172 and 304; every published Batch 1057 category visually checked",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records technical documentation",
            rights_notes="Historical categories are published only as qualified Army-entry occupations, never as named employers.",
        ),
        source(
            NPS,
            stable_url="https://home.nps.gov/articles/oss-in-action-the-mediterranean-and-european-theaters.htm",
            archival_identifier="National Park Service article; OSS Training in the National Parks and Service Abroad in World War II",
            title="OSS in Action The Mediterranean and European Theaters",
            repository_publisher="U.S. National Park Service",
            publication_record_date="2017-08-07",
            locator="Emmett F. McNamara discussion and note 182",
            source_quality="B_authoritative_institutional",
            collection_name="OSS Training in the National Parks and Service Abroad in World War II",
            rights_notes="The article identifies McNamara by exact name, age, Boston neighborhood, radio role, Signal Corps school, OSS recruitment year, and French Operational Group service.",
        ),
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": SIGNAL_CORPS,
            "organization_id": "37fe0e48-9745-5a0a-8e04-6be9bc7c5c91",
            "canonical_name": "United States Army Signal Corps",
            "historical_name": "Army Signal Corps",
            "aliases": ["Signal Corps", "U.S. Army Signal Corps"],
            "organization_type": "military branch",
            "sector": "military",
            "city": None,
            "state_or_region": None,
            "country": "United States",
            "active_dates": None,
            "normalization_notes": "Existing military organization reused. Fort Monmouth training is modeled as a military assignment, not a civilian employer.",
        }
    ]


def army_affiliation_key(row: int) -> str:
    return f"army-entry-{slug(PEOPLE[row][1])}-b1057"


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
    values.append(
        {
            "key": "emmett-mcnamara-signal-corps-b1057",
            "person_id": PEOPLE[45][0],
            "organization_key": SIGNAL_CORPS,
            "organization_name_as_found": "Army's Signal Corps school at Fort Monmouth",
            "role_title": "Signal Corps school graduate and radio operator",
            "occupation": "radio operator",
            "relationship_type": "military_assignment",
            "start_date": "1943",
            "end_date": "1943",
            "date_precision": "The National Park Service says OSS recruited him in 1943 after graduation from the Signal Corps school; exact dates are not stated.",
            "city": "Fort Monmouth",
            "state_or_region": "New Jersey",
            "country": "United States",
            "immediate_pre_oss": True,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "explicit_immediate",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "published",
            "research_notes": "This is an immediate military training assignment, not a civilian employer. The Army-entry retail-manager category remains a separate qualified claim.",
        }
    )
    return values


def claim(
    key: str,
    row: int,
    claim_type: str,
    claim_text: str,
    evidence_paraphrase: str,
    identity_match_assessment: str,
    temporal_assessment: str,
    source_quality: str,
    claim_confidence: str,
    publication_status: str,
    match_notes: str,
    source_links: list[dict[str, str]],
    affiliation_key: str | None = None,
    evidence_excerpt: str | None = None,
) -> dict[str, object]:
    value: dict[str, object] = {
        "key": key,
        "person_id": PEOPLE[row][0],
        "claim_type": claim_type,
        "claim_text": claim_text,
        "evidence_paraphrase": evidence_paraphrase,
        "identity_match_assessment": identity_match_assessment,
        "temporal_assessment": temporal_assessment,
        "source_quality": source_quality,
        "claim_confidence": claim_confidence,
        "publication_status": publication_status,
        "match_notes": match_notes,
        "sources": source_links,
    }
    if affiliation_key:
        value["affiliation_key"] = affiliation_key
    if evidence_excerpt:
        value["evidence_excerpt"] = evidence_excerpt
    return value


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, label, _relationship, locator) in ARMY_OCCUPATIONS.items():
        identity_sources = [
            {"source_key": INDEX, "support_type": "context_only"},
            {"source_key": ARMY},
        ]
        identity_assessment = "High confidence from exact normalized full-name agreement and a unique protected-identifier match."
        identity_paraphrase = "The official index and Army entry agree in normalized full name and a reviewed nonshared protected identifier; the identifier remains private."
        if row == 45:
            identity_sources.append({"source_key": NPS})
            identity_assessment = "High confidence from the protected-identifier crosswalk plus the National Park Service's exact name, Boston location, radio role, Signal Corps chronology, and OSS assignment."
            identity_paraphrase = "Official Army and National Park Service evidence independently converge on the indexed Emmett F. McNamara."
        values.append(
            claim(
                f"identity-{slug(PEOPLE[row][1])}-army-b1057",
                row,
                "identity",
                f"The indexed {PEOPLE[row][1]} has a high-confidence match to an official Army entry.",
                identity_paraphrase,
                identity_assessment,
                "The Army entry establishes dated identity context but does not by itself establish the Army-to-OSS sequence.",
                "A_direct_official",
                "high",
                "published",
                "Identity crosswalk only; the Army category is assessed separately and is not a named employer.",
                identity_sources,
            )
        )
        values.append(
            claim(
                f"army-entry-{slug(PEOPLE[row][1])}-b1057",
                row,
                "occupation",
                f"At Army entry on {date}, {PEOPLE[row][1]} was recorded as {occupation}; no employer, institution, or workplace is identified.",
                f"The official Army bulk file records code {code}; the visually checked official list defines the category as {label}.",
                "High confidence from matching official name evidence and a reviewed, nonshared private identifier linkage; the identifier remains private.",
                "The category is fixed to the Army-entry date, but its sequence relative to OSS service is not established.",
                "A_direct_official",
                "medium",
                "publish_qualified",
                "The historical category remains qualified, excluded from verified-employer analytics, and is not converted into a named organization.",
                [
                    {"source_key": INDEX, "support_type": "context_only"},
                    {"source_key": ARMY},
                    {"source_key": TECH, "support_type": "context_only"},
                    {"source_key": CODES, "locator_override": locator},
                ],
                army_affiliation_key(row),
            )
        )
    # Row 19 already has a reviewed, published 1946 identity-only claim from the
    # Army checkpoint workflow. Do not create a second claim under a batch key.
    values.append(
        claim(
            "identity-john-j-mclaughlin-duplicate-b1057",
            6,
            "identity",
            "The two separately preserved John J. McLaughlin rows on page 312 are linked to one high-confidence person entity.",
            "The adjacent official index rows repeat the same normalized name and reviewed protected identifier; both printed rows remain preserved.",
            "High confidence for the duplicate-row linkage; no external biographical identity is asserted.",
            "The index supports source-row resolution only and supplies no pre-OSS affiliation.",
            "A_direct_official",
            "high",
            "published",
            "The protected value is not public, and the linkage does not create an employer claim.",
            [{"source_key": INDEX}],
        )
    )
    values.append(
        claim(
            "emmett-mcnamara-signal-corps-b1057",
            45,
            "immediate_pre_oss_affiliation",
            "Emmett F. McNamara graduated from the Army Signal Corps school at Fort Monmouth immediately before OSS recruited him in 1943.",
            "The National Park Service explicitly says OSS recruited the 22-year-old Boston radio operator after his Signal Corps school graduation.",
            "High confidence from exact name, age, Boston neighborhood, radio specialty, Signal Corps chronology, OSS recruitment year, and later operational assignment.",
            "Explicit immediate military-training-to-OSS recruitment sequence in 1943.",
            "B_authoritative_institutional",
            "high",
            "published",
            "This is a military assignment, not a civilian employer. The source also identifies later OSS Areas B and F and Section Lindsay service.",
            [{"source_key": NPS}],
            "emmett-mcnamara-signal-corps-b1057",
            "recruited him in 1943 after he graduated from the Army's Signal Corps school",
        )
    )
    return values


def unresolved_message(name: str, box: str) -> str:
    return (
        f"Review the indexed Box {box} personnel file for corroborating identifiers, the immediate pre-OSS affiliation, and the last civilian employer. "
        "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed."
    )


def person_updates() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for person_id, (row, _person_id, name, box) in UNIQUE_PEOPLE.items():
        update: dict[str, object] = {
            "person_id": person_id,
            "manual_review_required": True,
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
        }
        if row in ARMY_OCCUPATIONS and row != 45:
            update.update(
                identity_status="high_confidence",
                identity_evidence="The official index and Army entry agree in normalized full name and a reviewed nonshared private identifier. The dated broad category does not establish a named employer or OSS sequence.",
                nara_catalog_id="1263923",
                research_status="occupation_only_found",
                next_action=f"Review Box {box} for a named employer or institution and establish the Army-to-OSS chronology.",
                archival_review_priority="high",
            )
        elif row == 45:
            update.update(
                manual_review_required=False,
                identity_status="high_confidence",
                identity_evidence="The private official Army crosswalk and National Park Service history converge on the exact name, Boston background, radio role, Signal Corps training, OSS recruitment year, and operational assignment.",
                nara_catalog_id="1263923",
                research_status="completed",
                next_action="Review Box 511 for a named last civilian employer before Signal Corps service and the exact Fort Monmouth training dates.",
                archival_review_priority="medium",
            )
        elif row in IDENTITY_ONLY_ARMY:
            update.update(
                identity_status="high_confidence",
                identity_evidence="The official index and Army entry agree in normalized full name and a reviewed nonshared private identifier; the 1946 occupation is not treated as pre-OSS evidence.",
                nara_catalog_id="1263923",
                research_status="requires_archival_review",
                next_action=f"Review Box {box} for a genuinely pre-OSS employer or affiliation; do not back-project the post-OSS Army occupation.",
                archival_review_priority="high",
            )
        elif row == 2:
            update.update(
                manual_review_required=False,
                identity_status="high_confidence",
                identity_evidence="Existing reviewed evidence links this distinctive exact name to Donal McLaughlin's documented design and federal-government career and preserves five cited pre-OSS affiliations.",
                research_status="verified_employer_found",
                next_action="Review Box 510 to confirm the exact OSS recruitment date and whether Loewy's office was the final civilian employer.",
                archival_review_priority="medium",
            )
        elif row == 6:
            update.update(
                identity_status="high_confidence",
                identity_evidence="Two separately preserved page-312 rows share the exact normalized name and reviewed private identifier and are linked to one entity; no external biographical identity is asserted.",
                possible_duplicate_group="p312-john-j-mclaughlin-identical-private-identifier-b1057",
                research_status="requires_archival_review",
                next_action="Review both John J. McLaughlin entries in Box 510 to confirm the duplicate-row relationship and identify a pre-OSS affiliation.",
                archival_review_priority="high",
            )
        elif row == 15:
            update.update(
                identity_status="probable",
                identity_evidence="The indexed Francis B. McLeod and official Army MC LEOD FRANCIS B entry share the reviewed private identifier and normalized name, but the Army transcription suffix requires personnel-file confirmation before publication.",
                research_status="needs_identity_review",
                next_action="Review Box 510 to confirm whether the official Army transcription belongs to Francis B. McLeod before transferring any occupation or chronology.",
                archival_review_priority="critical",
            )
        elif row in IDENTIFIER_CONFLICT_ROWS:
            update.update(
                identity_status="conflicting",
                identity_evidence="The protected identifier associated with the index row maps to an official Army entry bearing a materially different name. No occupation or biography is transferred across the conflict.",
                research_status="conflicting_sources",
                next_action=f"Review Box {box} and the original index documentation to resolve the protected-identifier/name conflict before accepting any external identity.",
                archival_review_priority="critical",
            )
        elif row in MIDDLE_INITIAL_CONFLICT_ROWS:
            update.update(
                identity_status="ambiguous",
                identity_evidence="An official Army candidate agrees in first and last name but conflicts in middle initial. The candidate was rejected for claim promotion pending direct personnel-file evidence.",
                research_status="needs_identity_review",
                next_action=f"Review Box {box} to resolve the middle-initial conflict before transferring any Army occupation or outside biography.",
                archival_review_priority="critical",
            )
        elif row == 14:
            update.update(
                identity_status="unresolved",
                identity_evidence="The page image places PFC in the printed middle-initial column while the rank column is blank. The raw row is preserved and flagged; no silent rank or middle-name correction is made.",
                research_status="requires_archival_review",
                next_action="Review Box 510 and the original page layout to determine whether PFC is a displaced rank before normalizing the row or researching namesakes.",
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
    if len(values) != 45 or len({item["person_id"] for item in values}) != 45:
        raise RuntimeError("Expected 45 unique page-312 person updates")
    return values


def outcome_note(row: int) -> str:
    if row == 45:
        return "Institutional evidence explicitly establishes Emmett F. McNamara's immediate Signal Corps training-to-OSS recruitment sequence; the separate Army-entry occupation remains qualified."
    if row in ARMY_OCCUPATIONS:
        return "An accepted official Army identity link supports a qualified dated occupation or student category but no named employer or OSS-transfer sequence."
    if row in IDENTITY_ONLY_ARMY:
        return "The existing accepted official Army identity link supports identity only; the 1946 occupation remains excluded from pre-OSS claims."
    if row == 2:
        return "Existing reviewed citations already establish five pre-OSS affiliations for Donal McLaughlin; this attempt checked for stronger immediate-transition evidence without duplicating claims."
    if row == 6:
        return "The two printed John J. McLaughlin rows remain separately preserved and linked to one entity by exact name and private identifier; no employer was inferred."
    if row == 15 or row in MIDDLE_INITIAL_CONFLICT_ROWS:
        return "A plausible military-record candidate remains unpromoted because a transcription or middle-initial conflict requires the personnel file."
    if row in IDENTIFIER_CONFLICT_ROWS:
        return "The protected-identifier/name conflict remains visible; no occupation or employer was transferred."
    if row == 14:
        return "The PFC column-placement warning was visually confirmed and preserved without silently changing the indexed name or rank."
    return "No reliable identity or pre-OSS affiliation was established; unbridged namesakes and chronologically irrelevant results were rejected."


def research_attempts() -> list[dict[str, object]]:
    updates = {item["person_id"]: item for item in person_updates()}
    positive_rows = set(ARMY_OCCUPATIONS) | IDENTITY_ONLY_ARMY | {2, 6}
    review_rows = IDENTIFIER_CONFLICT_ROWS | MIDDLE_INITIAL_CONFLICT_ROWS | {14, 15}
    values: list[dict[str, object]] = []
    for person_id, (row, _person_id, name, box) in UNIQUE_PEOPLE.items():
        if row in positive_rows:
            outcome, reviewed, rejected = "source_reviewed", 5, 3
        elif row in review_rows:
            outcome, reviewed, rejected = "candidate_rejected", 3, 4
        else:
            outcome, reviewed, rejected = "no_result", 2, 3
        values.append(
            {
                "key": f"page312-row{row}-{slug(name)}-b1057",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index context; exact-name and meaningful initial, punctuation, spacing, spelling and OCR variants; CIA Reading Room/domain discovery; OSS, rank, branch, assignment and private-identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory and archival searches; indexed Box {box}",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_1057",
                "started_at": "2026-11-11T19:10:00-05:00",
                "completed_at": "2026-11-11T21:35:00-05:00",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, postwar-only leads, and sources without an OSS, rank, protected-identifier, unit, or personnel-file bridge were rejected. Army categories were not converted into named employers; middle-initial and identifier conflicts were not promoted.",
                "research_notes": f"{outcome_note(row)} Page 312 was visually checked against the official NARA index, and the published Army occupation codes were visually checked against the official code-list PDF. Exact-name OSS, CIA-domain, employment, occupation, obituary, institutional, newspaper, directory, and archival searches were reviewed as applicable. No search-result snippet was used as final evidence and no authenticated NARA Catalog API request was made.",
                "next_action": str(updates[person_id]["next_action"]),
                "attempt_number": ATTEMPT_NUMBERS[row],
                "research_agent_version": "before-oss-b1057-v1",
            }
        )
    if len(values) != 45 or len({item["person_id"] for item in values}) != 45:
        raise RuntimeError("Expected 45 unique page-312 research attempts")
    return values


def build_bundle() -> dict[str, object]:
    return {
        "bundle_version": "batch-1057-v1",
        "reviewer": "Before OSS Batch 1057 evidence review",
        "sources": sources(),
        "organizations": organizations(),
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
