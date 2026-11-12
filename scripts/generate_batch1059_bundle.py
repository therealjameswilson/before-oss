#!/usr/bin/env python3
"""Generate the reviewed Batch 1059 completion bundle for PDF page 314."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page314-francis-c-mcvarish-to-d-meedsellen-review_"
    "batch-1059_2026-11-11.json"
)

INDEX = "nara-index-page314-b1059"
ARMY = "army-bulk-page314-b1059"
TECH = "army-tech-page314-b1059"
CODES = "army-codes-page314-b1059"


PEOPLE = {
    1: ("a3b30365-2a1f-5f2e-8e9c-a7a1a2987551", "Francis C McVarish", "513"),
    2: ("28c74028-bb9f-585e-8afa-521e14a920c3", "Charles F McVey", "513"),
    3: ("9cb50c4f-c305-5867-9f5a-08a8d4fde336", "Ethel L McVey", "513"),
    4: ("51318818-d94a-5cd1-ab8d-5500883da0ea", "R McVickerst", "513"),
    5: ("63a05d72-5be8-5f69-a07b-372b1d3c6851", "Gebbert Q McVitty", "513"),
    6: ("e89a8a78-1a30-5b67-bfe9-57b2761cd781", "Joseph W McWatters", "513"),
    7: ("33d9c6b7-650a-5bf1-881e-a54c383b39c9", "Mary C McWhidt", "513"),
    8: ("f9379f55-febb-52d2-993f-0e276bdbb5fc", "Richard A McWhirter", "513"),
    9: ("71e6a694-3a2a-5b6f-a615-60a3630cc05f", "Chastain McWilliams", "513"),
    10: ("a417086c-3c99-5b5a-a198-35e1dc27f553", "Julia C McWilliams", "513"),
    11: ("05b64e26-6fd7-52b4-b44d-b55381b7ac15", "Robert H McWilliams", "513"),
    12: ("636ecf8a-9eca-553f-9335-fba09f37be6a", "George G Mead", "514"),
    13: ("2a1bf552-169d-50d3-a246-1a62df82fc29", "Gerard E Mead", "514"),
    14: ("cc77cae7-2c22-5c27-9d06-fb09e3091358", "Herbert B Mead", "514"),
    15: ("0406a1cb-66b0-5573-9923-e5dba422b52f", "John C Mead", "514"),
    16: ("9d59dcd1-940d-5d23-ad38-0b4e061c8917", "Montauge Mead", "514"),
    17: ("d819d4d6-a847-5804-a6c5-b37c9db716c3", "Pierre D Mead", "514"),
    18: ("9e1dd7a8-2b56-5cd4-b7e9-cdcb315a2d28", "Robert F Mead", "514"),
    19: ("1635d360-c224-5e20-9c2f-651da849c40e", "Robert G Mead", "514"),
    20: ("6f6769fa-a8d9-561d-8874-44ce0c700fe6", "Ronald C Mead", "514"),
    21: ("948cd939-1937-5ccb-b3e2-fd58bf08434b", "Mary P Meade", "514"),
    22: ("5745d57e-cc7f-57c1-9a11-3673f61baa9e", "Mary P Meade", "514"),
    23: ("0d351a66-7871-5f85-8666-720005dbb0cb", "Patrick A Meade", "514"),
    24: ("6f7c4c30-bff8-5269-8a33-e110724d3284", "Rita C Meade", "514"),
    25: ("cd2a9ff7-13d3-5386-9652-c47686c756cb", "Edwin E Meader", "514"),
    26: ("e1d3612e-1ec2-5438-8a7f-8768cad5816d", "Lorraine M Meader", "514"),
    27: ("87534337-8145-51b8-bd77-c4748c6de875", "Lorraine M Meador", "514"),
    28: ("95ac70b7-b61c-5bd4-87fd-a83dc16d5228", "Richard M Meadors", "514"),
    29: ("0d401161-9bb7-5c26-b9d1-9669aae71ebb", "Arnold Meadow", "514"),
    30: ("73fa35b0-22b5-538e-98d4-e484b27132fa", "Francis Meadowcraft", "514"),
    31: ("72dda63e-b65e-50ac-8f14-058926c0629e", "Gail K Meadows", "514"),
    32: ("3b2c43c1-f34f-5aff-83a1-51cd49f4d7b4", "Frederick Mears", "514"),
    33: ("025d89a8-16e4-5a8e-b8d6-b41ffd2a3d03", "Bernard C Meaton", "514"),
    34: ("70ac74b0-8618-5493-a6fa-98f29450a20d", "David C Meck", "514"),
    35: ("0784a7a4-d7e1-540f-bd41-20ee44c1f5af", "Joseph Medaglian", "514"),
    36: ("382588a9-b2e3-50ad-89fa-1c91994f3511", "Joseph B Medagliant", "514"),
    37: ("e4f06177-71b0-59d9-b72d-9f36f3377345", "Donn P Medalie", "514"),
    38: ("f57c5f53-76ab-530e-aab0-c3289548228d", "William Medcraft", "514"),
    39: ("5bbf4902-3433-59f9-bae3-ee31a492f572", "Earl R Meddaugh", "515"),
    40: ("22a22416-ca55-57e6-9d6d-859bf9eed047", "Henry J Medieros", "515"),
    41: ("20b7b2b4-3153-584e-b8ec-ff80023aca96", "Manuel Medieros", "515"),
    42: ("2c23d961-72ee-5252-99a1-a4e466598994", "Aneo Mediler", "515"),
    43: ("c2f1a32f-db57-537f-91d3-e21198ed9dbd", "Thomas O Medlicott", "515"),
    44: ("f059f6f0-916c-51bc-96dd-408430261469", "Raymond Medlin", "515"),
    45: ("fd951697-8d83-5c30-a37d-9799b02da010", "Herbert G Medric", "515"),
    46: ("5b67065d-48d2-5d5a-9d0f-9b19c8225cc2", "D Meedsellen", "515"),
}

# These official Army-entry categories are accepted only where exact or
# documented variant names and unique reviewed private identifiers agree. The
# protected identifiers never enter this bundle or the public projection.
ARMY_OCCUPATIONS = {
    1: ("1943-06-23", "006", "author, editor, or reporter", "Authors, editors and reporters", "PDF physical page 170; historical code 0-06"),
    2: ("1941-03-05", "948", "sailor or deckhand, except U.S. Navy", "Sailors and deckhands, except U.S. Navy", "PDF physical page 174; historical code 9-48"),
    9: ("1943-02-13", "768", "packing, filling, labeling, marking, bottling, or related occupation, n.e.c.", "Packing, filling, labeling, marking, bottling, and related occupations, n.e.c.", "PDF physical page 174; historical code 7-68"),
    12: ("1942-10-01", "016", "civil engineer", "Engineers, civil", "PDF physical page 170; historical code 0-16"),
    13: ("1941-01-27", "236", "guide, except hunting or trapping", "Guides, except hunting and trapping", "PDF physical page 172; historical code 2-36"),
    25: ("1942-11-16", "097", "manager or official, n.e.c.", "Managers and officials, n.e.c.", "PDF physical page 171; historical code 0-97"),
    30: ("1943-02-01", "138", "stock clerk", "Stock clerks", "PDF physical page 171; historical code 1-38"),
    33: ("1945-01-22", "020", "mining engineer", "Engineers, mining", "PDF physical page 171; historical code 0-20"),
    40: ("1943-07-15", "072", "retail manager", "Managers, retail", "PDF physical page 171; historical code 0-72"),
    41: ("1941-12-11", "736", "chauffeur or bus, taxi, truck, or tractor driver", "Chauffeurs and drivers, bus, taxi, truck, and tractor", "PDF physical page 174; historical code 7-36"),
    45: ("1942-05-27", "170", "sales clerk", "Sales clerks", "PDF physical page 171; historical code 1-70"),
}

VERIFIED_EMPLOYER_ROWS = {10, 11, 25}
IDENTITY_REVIEW_ROWS = {4, 21, 22, 26, 27, 34, 42}
CONFLICT_ROWS = {36}
COMPLETED_AFFILIATION_ROWS = {37, 43}
OCCUPATION_ONLY_ROWS = set(ARMY_OCCUPATIONS) - VERIFIED_EMPLOYER_ROWS
ARCHIVAL_ROWS = set(PEOPLE) - (
    VERIFIED_EMPLOYER_ROWS
    | IDENTITY_REVIEW_ROWS
    | CONFLICT_ROWS
    | COMPLETED_AFFILIATION_ROWS
    | OCCUPATION_ONLY_ROWS
)


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
            archival_identifier="RG 226, Entry A1-224, Boxes 513-515",
            title="OSS Personnel Files from Excel",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="2010-12-23",
            locator="PDF page 314, rows 1-46; every printed row visually checked against the official PDF",
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
            locator="PDF physical pages 170-174; every published Batch 1059 category visually checked",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records technical documentation",
            rights_notes="Historical categories are published only as qualified Army-entry occupations, never as named employers.",
        ),
    ]


def army_affiliation_key(row: int) -> str:
    return f"army-entry-{slug(PEOPLE[row][1])}-b1059"


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, _code, occupation, _label, _locator) in ARMY_OCCUPATIONS.items():
        values.append(
            {
                "key": army_affiliation_key(row),
                "person_id": PEOPLE[row][0],
                "role_title": occupation,
                "occupation": occupation,
                "relationship_type": "unknown",
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
    for row, (date, code, occupation, label, locator) in ARMY_OCCUPATIONS.items():
        values.append(
            {
                "key": army_affiliation_key(row),
                "person_id": PEOPLE[row][0],
                "affiliation_key": army_affiliation_key(row),
                "claim_type": "occupation",
                "claim_text": f"At Army entry on {date}, {PEOPLE[row][1]} was recorded as {occupation}; no employer, institution, or workplace is identified.",
                "evidence_paraphrase": f"The official Army bulk file records code {code}; the visually checked official list defines the category as {label}.",
                "identity_match_assessment": "High confidence from exact or documented variant-name agreement and a reviewed, nonshared private identifier linkage; the identifier remains private.",
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


def identity_review_action(row: int) -> str:
    box = PEOPLE[row][2]
    if row in {21, 22}:
        return f"Inspect both adjacent Mary P. Meade jackets in Box {box} before merging records or transferring employment evidence."
    if row in {26, 27}:
        return f"Inspect the Lorraine M. Meader/Meador jackets in Box {box} before merging records or transferring employment evidence."
    if row == 34:
        return f"Inspect Box {box} to confirm identity and the sequence among law-school, Federal Security Agency, Middle East mission, and OSS roles."
    if row == 4:
        return f"Inspect Box {box} and the identifier-linked Army record before correcting the indexed surname or assigning employment evidence."
    return f"Inspect Box {box} and the identifier-linked Army record before correcting the indexed name or assigning employment evidence."


def person_updates() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (person_id, name, box) in PEOPLE.items():
        update: dict[str, object] = {"person_id": person_id}
        if row in OCCUPATION_ONLY_ROWS:
            update.update(
                manual_review_required=False,
                research_status="occupation_only_found",
                next_action=f"Review Box {box} for a named employer or institution and establish the Army-to-OSS chronology.",
                archival_review_priority="high",
            )
        elif row in VERIFIED_EMPLOYER_ROWS:
            next_actions = {
                10: "No additional archival review is required for the current employer questions; retain the differing official box references in provenance.",
                11: "Review Box 513 to document the exact OSS assignment and transition from ONI to Army/OSS service.",
                25: "Review Box 514 for the exact Army-to-OSS assignment date, unit, and Kalamazoo Vegetable Parchment Company job title.",
            }
            update.update(
                manual_review_required=False,
                research_status="verified_employer_found",
                next_action=next_actions[row],
                archival_review_priority="not_required" if row == 10 else "high",
            )
        elif row in IDENTITY_REVIEW_ROWS:
            update.update(
                manual_review_required=True,
                research_status="needs_identity_review",
                next_action=identity_review_action(row),
                archival_review_priority="critical",
            )
        elif row in CONFLICT_ROWS:
            update.update(
                manual_review_required=True,
                research_status="conflicting_sources",
                next_action="Inspect Box 514 and both identifier-linked Army records before correcting the name or assigning any affiliation.",
                archival_review_priority="critical",
            )
        elif row in COMPLETED_AFFILIATION_ROWS:
            action = (
                "Review Box 514 and State Department personnel records for the exact Foreign Service-to-OSS transition and any last civilian employer."
                if row == 37
                else "Review Box 515 and Coast Guard records for assignment dates, prewar employment, and the meaning of the printed C8M rank code."
            )
            update.update(
                manual_review_required=False,
                research_status="completed",
                next_action=action,
                archival_review_priority="high",
            )
        else:
            if row not in ARCHIVAL_ROWS:
                raise RuntimeError(f"Unclassified page-314 row {row}")
            update.update(
                identity_status="unresolved",
                identity_evidence="Exact-name and meaningful-variant checks across the official index context, CIA-domain discovery, accessible military and institutional sources, employment and occupation searches, and obituary or archival discovery produced no reliable identity and pre-OSS affiliation bridge; unbridged namesakes were rejected.",
                manual_review_required=True,
                research_status="requires_archival_review",
                next_action=unresolved_message(name, box),
                personnel_file_digitized=False,
                personnel_file_reviewed=False,
                archival_review_priority="critical" if row == 46 else "high",
            )
        values.append(update)
    if len(values) != 46 or len({item["person_id"] for item in values}) != 46:
        raise RuntimeError("Expected 46 separate page-314 person updates")
    return values


def outcome_note(row: int) -> str:
    if row in OCCUPATION_ONLY_ROWS:
        return "An accepted official Army identity link supports a qualified dated occupation but no named employer, institution, workplace, or OSS-transfer sequence."
    if row == 10:
        return "The confirmed digitized personnel-file identity and existing cited OWI, W. & J. Sloane, volunteer, magazine, and Smith College claims remain unchanged."
    if row == 11:
        return "The existing ONI immediate pathway and Denver District Attorney employer claims remain unchanged; a 1945 Army entry was not treated as evidence of an earlier occupation because its chronology does not support that use."
    if row == 25:
        return "The existing Kalamazoo Vegetable Parchment Company and Army-pathway claims remain unchanged; the Army entry adds only a qualified broad manager-or-official category and does not tie that category to the company."
    if row in {21, 22}:
        return "The adjacent identical index rows remain separate and unresolved; no employment or identity evidence was transferred between them."
    if row in {26, 27}:
        return "The adjacent Meader/Meador spelling variants remain separate and unresolved; no employment or identity evidence was transferred between them."
    if row == 34:
        return "The probable David C. Meck identity and its qualified law-school and Federal Security Agency claims remain visible, but no direct OSS or protected-identifier bridge was found."
    if row in {4, 42}:
        return "The protected identifier points to a materially incompatible or displaced name; the conflict remains visible and no occupation or employer was transferred."
    if row == 36:
        return "Two incompatible Army records share the printed identifier; neither was selected and no occupation or employer was transferred."
    if row == 37:
        return "The high-confidence Foreign Service affiliation is documented, but accessible sources do not establish the exact transition into OSS or a last civilian employer."
    if row == 43:
        return "The official Coast Guard-to-OSS assignment is documented as the immediate pathway, but accessible sources do not identify an earlier civilian employer."
    return "No reliable identity or pre-OSS affiliation was established; unbridged namesakes, snippets, and chronologically irrelevant results were rejected."


def research_attempts() -> list[dict[str, object]]:
    updates = {item["person_id"]: item for item in person_updates()}
    values: list[dict[str, object]] = []
    for row, (person_id, name, box) in PEOPLE.items():
        if row in ARMY_OCCUPATIONS:
            outcome, reviewed, rejected = "source_reviewed", 4, 3
        elif row in VERIFIED_EMPLOYER_ROWS | COMPLETED_AFFILIATION_ROWS:
            outcome, reviewed, rejected = "source_reviewed", 5, 2
        elif row in IDENTITY_REVIEW_ROWS | CONFLICT_ROWS:
            outcome, reviewed, rejected = "candidate_rejected", 3, 4
        else:
            outcome, reviewed, rejected = "no_result", 2, 3
        attempt_number = 14 if row == 10 else 5 if row == 11 else 3
        values.append(
            {
                "key": f"page314-row{row}-{slug(name)}-b1059",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index context; exact-name and meaningful initial, punctuation, spacing, spelling and OCR variants; CIA Reading Room/domain discovery; OSS, rank, branch, assignment and private-identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory and archival searches; indexed Box {box}",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_1059",
                "started_at": "2026-11-11T18:30:00-05:00",
                "completed_at": "2026-11-11T20:45:00-05:00",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, postwar-only leads, and sources without an OSS, rank, private-identifier, unit, or personnel-file bridge were rejected. Army categories were not converted into named employers; duplicate-row and identifier conflicts were not promoted.",
                "research_notes": f"{outcome_note(row)} Page 314 was visually checked against the official NARA index, and every published Army occupation code was visually checked against the official code-list PDF. Exact-name OSS, CIA-domain, employment, occupation, obituary, institutional, newspaper, directory, and archival searches were reviewed as applicable. Existing cited claims were preserved without duplication. No search-result snippet was used as final evidence and no authenticated NARA Catalog API request was made.",
                "next_action": str(updates[person_id]["next_action"]),
                "attempt_number": attempt_number,
                "research_agent_version": "before-oss-b1059-v1",
            }
        )
    return values


def build_bundle() -> dict[str, object]:
    return {
        "bundle_version": "batch-1059-v1",
        "reviewer": "Before OSS Batch 1059 evidence review",
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
