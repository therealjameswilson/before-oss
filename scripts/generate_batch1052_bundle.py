#!/usr/bin/env python3
"""Generate the reviewed Batch 1052 evidence bundle for PDF page 307."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page307-charles-w-mcdaniel-to-michael-v-mcdowell-review_"
    "batch-1052_2026-11-11.json"
)

INDEX = "nara-index-b1052"
ARMY = "army-bulk-b1052"
TECH = "army-tech-b1052"
CODES = "army-codes-b1052"


PEOPLE = {
    1: ("8b72e51f-1234-5627-ad40-344365214db0", "Charles W McDaniel", "502"),
    2: ("718ff7d4-e469-544e-993c-1f77cc15c5ab", "Gene A McDaniel", "502"),
    3: ("3942be6c-1665-515a-969e-be5b1754c952", "Hazel M McDaniel", "502"),
    4: ("38ffc93e-398c-5040-839b-16e2d30592d7", "James E McDaniel", "502"),
    5: ("37829384-256a-51ca-94a6-f82e4bdd34c2", "Florence I McDanile", "502"),
    6: ("681baa6d-acb2-5e6e-8f5f-d6a3613cbe66", "Arlene E McDermott", "502"),
    7: ("27a18023-4ff5-564a-8ad7-e6bea4480b1b", "Charles J McDermott", "502"),
    8: ("1d531444-256f-5612-af7b-8cd7c19874ed", "Francis L McDermott", "502"),
    9: ("02b6cee9-6581-5f2f-a595-10776c924af0", "Francis M McDermott", "502"),
    10: ("bef15c26-b61f-5ec1-a109-3e44af4a6b02", "Mary L McDermott", "502"),
    11: ("940fe6f7-a36b-54fd-97e7-11e5ecd89586", "Hugh A McDevitt", "502"),
    12: ("b9838bf7-f5ed-58b7-8d9d-03d4bcc6d38a", "Dale J McDonald", "502"),
    13: ("24c85fe3-ff5a-5a8d-a9fd-14eeac196896", "Dervey A McDonald", "502"),
    14: ("646b8baa-726e-5da5-9373-5d3515172cad", "Dewey E McDonald", "502"),
    15: ("70f72e56-1f98-574a-82ab-862d51a4c570", "Garreth M McDonald", "502"),
    16: ("f90d6015-81a6-5a84-9aa7-cdd915fd85d8", "George S McDonald", "502"),
    17: ("71d34770-f8fd-58ce-af88-2e1ec03f3cdb", "Georgie R McDonald", "502"),
    18: ("7498979d-3069-5bd2-8ab0-748855fec83d", "Hervey A McDonald", "502"),
    19: ("d93acb14-2836-5e89-83f7-747da5251273", "Hoke S McDonald", "503"),
    20: ("3a39a26c-73bb-57c3-bdef-a51432ef2aea", "James E McDonald", "503"),
    21: ("37afadbd-0cb9-57cf-bd84-3226c1cec7c6", "Jasper N McDonald", "503"),
    22: ("6b65de24-e2b7-542c-a082-6c955d02ddf2", "Joseph E McDonald", "503"),
    23: ("7f41f9f1-d563-5643-be44-6ad148cfabb6", "Kenneth C McDonald", "503"),
    24: ("702b036c-dd0d-5d3d-8758-1eb30ea210ff", "Mary B McDonald", "503"),
    25: ("137cb269-2c16-5257-b4a3-32b930306826", "Patricia A McDonald", "503"),
    26: ("c9f2ee69-91f5-5e10-a206-2ddef07ccf37", "Raymond W McDonald", "503"),
    27: ("53e08adb-c626-5a51-8ed8-3e8111c37709", "Roy W McDonald", "503"),
    28: ("35e3e5e2-6d43-52c1-9fe5-49d8ed0cd1cd", "Wilmer J McDonald", "503"),
    29: ("49191b6a-4ee0-5c00-a5aa-98c59c538356", "Catherine F McDonnell", "503"),
    30: ("f16edcd0-5911-5ef9-ac2f-10dfad67236f", "James L McDonnell", "503"),
    31: ("a12d47d9-3357-5ba2-ad3f-46192ba7f21f", "Mary E McDonnell", "503"),
    32: ("280e3886-14b8-571b-8a70-92bbf4333411", "Paul J McDonnell", "503"),
    33: ("5884a9a9-afed-5ed1-91b5-d56d73936604", "Robert E McDonnell", "503"),
    34: ("229b4fa8-5af4-5b8a-9980-4b643adfa6f9", "Thomas F McDonnell", "503"),
    35: ("511d1a1e-b956-5466-8f29-fe66b79245c7", "Francis J McDonough", "503"),
    36: ("1046b337-77db-5a64-b2e1-58a65ef3eb1a", "John J McDonough", "503"),
    37: ("0c0eff9f-6cff-5af4-8ee9-ff79c6460590", "Margie McDonough", "503"),
    38: ("f61af583-dd89-50b4-be44-c4c4d2d8e13c", "Rita C McDonough", "503"),
    39: ("140aaec5-d714-5803-b14c-9ca1269eb1f0", "William P McDonough", "503"),
    40: ("966fb129-379e-5de2-b856-016ee0d2a0e6", "Claire H McDougal", "503"),
    41: ("7db9f7df-bf95-5c1f-a059-f03c440c517c", "Robert L McDougal", "503"),
    42: ("c6a74455-3ace-5b0a-9c9a-ddc2c70770c5", "Robert L McDougal", "503"),
    43: ("93a587a3-5e94-5c72-a349-009778e2cfe8", "Paul J McDougall", "503"),
    44: ("d4cf87a9-e29b-57c0-af46-d2dd01c90c0b", "John D McDowell", "503"),
    45: ("de94b79b-ee77-5e6d-8b93-299a9ff202b3", "Mary A McDowell", "503"),
    46: ("43fafdd6-80a4-5d5d-9d08-bbca38e8a96f", "Michael V McDowell", "503"),
}


# Only nonshared, wartime-dated identity links with a defined occupation code
# become public, qualified occupation evidence. Code 993 is absent from the
# reviewed official list and remains uninterpreted.
ARMY_OCCUPATIONS = {
    2: ("1943-03-19", "992", "student", "Students", "student", "PDF physical page 304; corrected historical code 9-92"),
    14: ("1942-09-17", "992", "student", "Students", "student", "PDF physical page 304; corrected historical code 9-92"),
    16: ("1943-09-10", "480", "sheet-metal worker, coppersmith, or tinsmith", "Tinsmiths, coppersmiths, and sheet metal workers", "unknown", "PDF physical page 174; historical code 4-80"),
    17: ("1943-07-01", "599", "foreman, not elsewhere classified", "Foremen, n.e.c.", "unknown", "PDF physical page 175; historical code 5-99"),
    21: ("1942-05-19", "831", "sawmill occupation, not elsewhere classified", "Sawmill occupations, n.e.c.", "unknown", "PDF physical page 173; historical code 8-31"),
    34: ("1942-11-10", "789", "miscellaneous occupation, not elsewhere classified", "Miscellaneous occupations, n.e.c.", "unknown", "PDF physical page 175; historical code 7-89"),
    39: ("1942-04-21", "727", "construction or maintenance painter", "Painters, construction and maintenance", "unknown", "PDF physical page 174; historical code 7-27"),
    46: ("1941-07-03", "578", "millwright", "Millwrights", "unknown", "PDF physical page 175; historical code 5-78"),
}

ARMY_IDENTITY_ROWS = set(ARMY_OCCUPATIONS) | {43}
CONFLICT_ROWS = {4, 26, 27}
AMBIGUOUS_ROWS = {13, 18, 41, 42}
DUPLICATE_GROUPS = {
    13: "p307-dervey-hervey-mcdonald-b623",
    18: "p307-dervey-hervey-mcdonald-b623",
    41: "p307-robert-l-mcdougal-two-rows-b623",
    42: "p307-robert-l-mcdougal-two-rows-b623",
}

ATTEMPT_NUMBERS = {
    1: 2, 2: 3, 3: 2, 4: 3, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2,
    10: 2, 11: 2, 12: 2, 13: 3, 14: 3, 15: 2, 16: 3, 17: 3,
    18: 3, 19: 2, 20: 2, 21: 3, 22: 2, 23: 2, 24: 3, 25: 2,
    26: 4, 27: 4, 28: 2, 29: 2, 30: 3, 31: 2, 32: 2, 33: 3,
    34: 4, 35: 2, 36: 3, 37: 2, 38: 2, 39: 4, 40: 2, 41: 3,
    42: 4, 43: 3, 44: 3, 45: 3, 46: 3,
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
            archival_identifier="RG 226, Entry A1-224, Boxes 502-503",
            title="OSS Personnel Files from Excel",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="2010-12-23",
            locator="PDF page 307, rows 1-46; every printed row visually checked against the official PDF",
            source_quality="A_direct_official",
            collection_name="Records of the Office of Strategic Services, Record Group 226",
            rights_notes="All 46 printed rows remain separate. Full protected identifiers remain private.",
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
            rights_notes="No raw record, protected identifier, or bulk ordinal is retained in public assets. Shared or conflicting links are withheld.",
        ),
        source(
            TECH,
            stable_url="https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf",
            archival_identifier="NN3-064-03-008; National Archives Identifier 1263923",
            title="World War II Army Enlistment Records: Reference Copy of Technical Documentation",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives at College Park - Electronic Records",
            publication_record_date="1994-2005; reference copy modified 2011",
            locator="PDF physical pages 44-46; Army-entry date, grade, and civilian-occupation fields",
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
            locator="PDF physical pages 173-175 and 304; all eight published Batch 1052 categories visually checked",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records technical documentation",
            rights_notes="Historical categories identify neither employer, institution, workplace, nor exact Army-to-OSS sequence. Undefined code 993 is not interpreted.",
        ),
    ]


def army_affiliation_key(row: int) -> str:
    return f"{slug(PEOPLE[row][1])}-army-entry-occupation-b1052"


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, _label, relationship, _locator) in ARMY_OCCUPATIONS.items():
        values.append(
            {
                "key": army_affiliation_key(row),
                "person_id": PEOPLE[row][0],
                "occupation": occupation,
                "relationship_type": relationship,
                "end_date": date,
                "date_precision": f"Historical civilian-occupation code {code} was recorded at Army entry on {date}; no named employer, institution, workplace, or OSS-transfer date is supplied.",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "temporal_relation_uncertain",
                "identity_confidence": "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "A_direct_official",
                "publication_status": "publish_qualified",
                "research_notes": "The broad historical category is excluded from verified-employer analytics and is not converted into a named organization.",
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
    return value


def identity_claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row in sorted(ARMY_IDENTITY_ROWS):
        undefined = row == 43
        values.append(
            claim(
                f"identity-{slug(PEOPLE[row][1])}-army-b1052",
                row,
                "identity",
                f"The indexed {PEOPLE[row][1]} row has a high-confidence identity link to an official Army enlistment record.",
                "The official index and Army names agree after historical fixed-width surname spacing is normalized, and the reviewed private identifier is nonshared for this row.",
                "High confidence from matching official name evidence and a reviewed, nonshared private identifier link; the identifier remains private.",
                "The Army-entry date supports identity, not by itself the chronology of OSS service.",
                "A_direct_official",
                "high",
                "published",
                "Historical occupation code 993 is undefined and is not interpreted."
                if undefined
                else "The identity link supports only a qualified Army-entry occupation or student category.",
                [
                    {"source_key": ARMY},
                    {"source_key": INDEX, "support_type": "context_only"},
                ],
            )
        )
    return values


def claims() -> list[dict[str, object]]:
    values = identity_claims()
    for row, (date, code, occupation, label, _relationship, locator) in ARMY_OCCUPATIONS.items():
        values.append(
            claim(
                f"army-entry-{slug(PEOPLE[row][1])}-b1052",
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
    return values


def unresolved_message(name: str, box: str) -> str:
    return (
        f"Review the indexed Box {box} personnel file for corroborating identifiers, the immediate pre-OSS affiliation, and the last civilian employer. "
        "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed."
    )


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
                identity_evidence="The official index and Army entry agree after historical fixed-width surname spacing is normalized, and a reviewed nonshared private identifier connects the records. The identifier remains private.",
                nara_catalog_id="1263923",
                research_status="occupation_only_found",
                next_action=f"Review Box {box} for a named employer or institution and establish the Army-to-OSS chronology; the official record supplies only a broad category at Army entry.",
                archival_review_priority="high",
            )
        elif row == 43:
            update.update(
                identity_status="high_confidence",
                identity_evidence="The official index and Army entry agree after historical fixed-width surname spacing is normalized, and a reviewed nonshared private identifier connects the records. Historical occupation code 993 is undefined and is not interpreted.",
                nara_catalog_id="1263923",
                research_status="requires_archival_review",
                next_action="Review Box 503 to identify Paul J. McDougall's civilian occupation, employer, and Army-to-OSS chronology; undefined code 993 supplies no defensible occupation.",
                archival_review_priority="high",
            )
        elif row == 4:
            update.update(
                identity_status="conflicting",
                identity_evidence="The protected identifier printed in the index resolves in the official Army bulk file to a wholly different name. The Army identity and occupation are not assigned to James E. McDaniel.",
                research_status="conflicting_sources",
                next_action="Review Box 502 and the original index documentation to resolve the protected-identifier conflict before making identity or employment claims.",
                archival_review_priority="critical",
            )
        elif row == 26:
            update.update(
                identity_status="conflicting",
                identity_evidence="The protected identifier printed in the index resolves in the official Army bulk file to a severely corrupted or conflicting name. The Army identity and occupation are not assigned to Raymond W. McDonald.",
                research_status="conflicting_sources",
                next_action="Review Box 503 and the original index documentation to resolve the protected-identifier conflict before making identity or employment claims.",
                archival_review_priority="critical",
            )
        elif row == 27:
            update.update(
                identity_status="conflicting",
                identity_evidence="The protected identifier printed in the index resolves in the official Army bulk file to a wholly different name. Neither that Army identity nor an unbridged university namesake is assigned to Roy W. McDonald.",
                research_status="conflicting_sources",
                next_action="Review Box 503 and the original index documentation before making identity or employment claims.",
                archival_review_priority="critical",
            )
        elif row in {13, 18}:
            update.update(
                identity_status="ambiguous",
                identity_evidence="The same protected identifier is printed for separate Dervey A. McDonald and Hervey A. McDonald rows with different ranks. The two source rows remain separate entities pending file review.",
                possible_duplicate_group=DUPLICATE_GROUPS[row],
                research_status="requires_archival_review",
                next_action="Compare the Dervey and Hervey personnel files in Box 502 before merging, correcting, or assigning employment evidence.",
                archival_review_priority="critical",
            )
        elif row == 41:
            update.update(
                identity_status="ambiguous",
                identity_evidence="This Robert L. McDougal row has a T/5 grade but no protected identifier, while the adjacent same-name row has an identifier but no grade. The rows remain separate pending file review.",
                possible_duplicate_group=DUPLICATE_GROUPS[row],
                research_status="requires_archival_review",
                next_action="Compare both Robert L. McDougal personnel files in Box 503 before any merge, correction, or employment assignment.",
                archival_review_priority="critical",
            )
        elif row == 42:
            update.update(
                identity_status="ambiguous",
                identity_evidence="This Robert L. McDougal row has a protected identifier but no grade, while the adjacent same-name row has a T/5 grade but no identifier. The rows remain separate pending file review.",
                possible_duplicate_group=DUPLICATE_GROUPS[row],
                research_status="requires_archival_review",
                next_action="Compare both Robert L. McDougal personnel files in Box 503 before any merge, correction, or employment assignment.",
                archival_review_priority="critical",
            )
        else:
            update.update(
                identity_status="unresolved",
                identity_evidence="Exact-name and meaningful-variant checks across the official index context, CIA-domain discovery, accessible military and institutional sources, Library of Congress newspaper discovery, obituary, directory, and archival searches produced no reliable identity and pre-OSS affiliation bridge; unbridged namesakes were rejected.",
                research_status="requires_archival_review",
                next_action=unresolved_message(name, box),
                archival_review_priority="high",
            )
        values.append(update)
    if len(values) != 46:
        raise RuntimeError(f"Expected 46 person updates, generated {len(values)}")
    return values


def outcome_note(row: int) -> str:
    if row in ARMY_OCCUPATIONS:
        return "An accepted official Army identity link supports a qualified dated occupation or student category but no named employer or OSS-transfer sequence."
    if row == 43:
        return "An accepted official Army link supports identity, but undefined occupation code 993 is not interpreted."
    if row in CONFLICT_ROWS:
        return "A protected-identifier conflict remains visible; no Army identity, occupation, or namesake biography was transferred."
    if row in AMBIGUOUS_ROWS:
        return "A shared identifier or adjacent same-name row remains a separate, ambiguous entity for direct personnel-file comparison."
    return "No reliable identity or pre-OSS affiliation was established; unbridged namesakes and chronologically irrelevant results were rejected."


def research_attempts() -> list[dict[str, object]]:
    updates = {item["person_id"]: item for item in person_updates()}
    values: list[dict[str, object]] = []
    for row, (person_id, name, box) in PEOPLE.items():
        if row in ARMY_IDENTITY_ROWS:
            outcome, reviewed, rejected = "source_reviewed", 4, 2
        elif row in CONFLICT_ROWS | AMBIGUOUS_ROWS:
            outcome, reviewed, rejected = "candidate_rejected", 3, 4
        else:
            outcome, reviewed, rejected = "no_result", 2, 3
        values.append(
            {
                "key": f"page307-row{row}-{slug(name)}-b1052",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index context; exact-name and meaningful initial, punctuation, spacing, spelling and OCR variants; CIA-domain discovery; OSS, rank, branch, assignment and private-identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory and archival searches; indexed Box {box}",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_1052",
                "started_at": "2026-11-11T13:35:00-05:00",
                "completed_at": "2026-11-11T14:00:00-05:00",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, postwar-only leads, and sources without an OSS, rank, private-identifier, unit, or personnel-file bridge were rejected. Shared identifiers and duplicate rows remain separate. Army categories were not converted into named employers, and undefined code 993 was not interpreted.",
                "research_notes": f"{outcome_note(row)} Page 307 was visually checked against a fresh official NARA download matching the preserved SHA-256. The official index, existing Library of Congress item-level attempts, exact-name OSS and meaningful-variant web discovery, CIA-domain discovery, employment and occupation checks, and obituary, institutional, directory, newspaper, and archival searches were reviewed as applicable. CIA-domain searches returned no person-specific result and were not treated as proof of absence. No search-result snippet was used as final evidence and no authenticated NARA Catalog API request was made.",
                "next_action": str(updates[person_id]["next_action"]),
                "attempt_number": ATTEMPT_NUMBERS[row],
                "research_agent_version": "before-oss-b1052-v1",
            }
        )
    if len(values) != 46:
        raise RuntimeError(f"Expected 46 research attempts, generated {len(values)}")
    return values


def build_bundle() -> dict[str, object]:
    return {
        "bundle_version": "batch-1052-v1",
        "reviewer": "Before OSS Batch 1052 evidence review",
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
