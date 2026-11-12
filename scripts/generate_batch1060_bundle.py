#!/usr/bin/env python3
"""Generate the reviewed Batch 1060 completion bundle for PDF page 315."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page315-joseph-meegan-to-bert-e-mellgren-review_"
    "batch-1060_2026-11-11.json"
)

INDEX = "nara-index-page315-b1060"
ARMY = "army-bulk-page315-b1060"
TECH = "army-tech-page315-b1060"
CODES = "army-codes-page315-b1060"


# Page 315 has 46 printed rows but 45 cautious entities. The two adjacent
# Michael Melkonian rows share one identifier and are already linked to one
# entity; both immutable source rows remain separately recoverable.
PEOPLE = {
    1: ("fc2b05f3-2436-5ae9-b88b-01b7b6080717", "Joseph Meegan", "515"),
    2: ("e719f2d2-4835-58e8-93d8-ab100bd90a77", "Arthur J Meehan", "515"),
    3: ("1e06c56a-6808-58f4-abb1-d7a729d5c810", "Donald J Meehan", "515"),
    4: ("bad285ac-33c7-533d-b231-f8457734785a", "Ruth L Meehan", "515"),
    5: ("88b14f2c-a7f1-573b-bcc4-d95b8f2acce9", "Charles R Meek", "515"),
    6: ("f44ab699-af7c-5b2d-9d83-440c6e958da5", "William R Meek", "515"),
    7: ("a5ef50b1-f406-5e62-a829-2be84a182538", "Leonard C Meeker", "515"),
    8: ("fd12a334-6091-5c70-ae46-fe4b89f38b18", "Donald J Meeks", "515"),
    9: ("ca050c6b-e20a-5e8e-bc73-4e88853d585f", "A Meeksdelbert?", "515"),
    10: ("7650b2d2-f90b-5d00-810f-a50369169b96", "Richard C Meelar", "515"),
    11: ("5d5163d4-87c1-53ed-b29f-854b6314d64d", "Peter M Meenan", "515"),
    12: ("d163e1ef-2d9c-5a0f-8058-fe032bd1e07e", "Mary E Meenehan", "515"),
    13: ("fd22f40f-6b02-56ac-9d71-af6fbda36e27", "John Megan", "515"),
    14: ("7f5823b9-e766-5a55-9e6e-05ec39b5ad1e", "Gaudens Megaro", "515"),
    15: ("661658e7-cddd-55cc-8252-da52c0a3491a", "Joseph C Megaro", "515"),
    16: ("fe92904e-0079-5b27-87e4-782be9c55301", "William T Megill", "515"),
    17: ("45dd460f-d1d6-5053-ae37-e7246f5bc02f", "William G Mehillos", "515"),
    18: ("e7928084-3eb3-5b1c-998e-c2c6c2e6fd2c", "Eugene W Mehner", "515"),
    19: ("aabc6afc-6a05-5342-b1c2-4ff5d7b48f55", "Lincoln Mei", "515"),
    20: ("8ff12694-57c3-5592-9bc0-91e8462a35a9", "Walter E Meier", "515"),
    21: ("203ca089-cf20-53cc-8364-7847b336f171", "Henry H Meigs", "515"),
    22: ("be3a7372-3777-543f-ae83-aaa2dee1b0db", "Richard L Meigs", "516"),
    23: ("08962f8b-b560-5ce7-a3fc-ed9817e8f99c", "John J Meily", "516"),
    24: ("a00970fa-cadb-56d7-8d87-73f22771a320", "Harvey H Meir", "515"),
    25: ("9f4d39d2-8975-5dd6-9ae5-58d479f3d0c8", "Nancy H Meirr", "515"),
    26: ("664ccf5c-d214-5170-934e-2b802372e457", "Frederick A Meiser", "516"),
    27: ("8b67db4e-ab10-54ef-ba38-974c36669054", "Beny J Meitoff", "516"),
    28: ("33ac230d-0524-5c61-92da-d087da50f79b", "Michael S Meixner", "516"),
    29: ("959b49ad-0879-52a8-a5a1-9c7a555d1e48", "Donald F Mela", "516"),
    30: ("24a68ddd-d4f3-5d05-a9fb-7f3b382b52a9", "Leif E Meland", "516"),
    31: ("2ec41bfb-73fd-5e8b-900b-819ecb628654", "George A Melanson", "516"),
    32: ("be740a24-8451-5af9-8c41-5d1ac6bfb2ad", "Patrick J Melanson", "516"),
    33: ("adfbfd38-473f-5099-9e7a-3b8515c84c00", "Leon C Melas", "516"),
    34: ("b3624f10-4e5e-537f-a72c-1e4670ff7de7", "Robert L Melberg", "516"),
    35: ("09119446-f015-5b6e-b512-e2ad4104d5dc", "I J Melchior", "516"),
    36: ("828d8e69-0aff-5cf3-b128-0187b00e93e2", "Valeriano Melchiori", "516"),
    37: ("0941bebf-43dd-5cfa-b669-1fdfa3c6e161", "Charles S Meledonis", "516"),
    38: ("0b87149d-b1f9-542d-b53d-dbd99d2772bd", "Michael Melehes", "516"),
    39: ("a92c2143-79dc-5238-9772-9e5ba3082cb5", "Angelo Meli", "516"),
    40: ("7db39dcf-751d-5747-a82e-60e38cfffb33", "Gustave Meligonis", "516"),
    41: ("e81bf272-edef-5a3a-94f7-87ac7a542d9c", "Kosta Melinkoff", "516"),
    42: ("7bd6f68b-0801-5068-93e8-7b56f4f8dfb6", "Nicholas J Melito", "516"),
    43: ("2c99f3a1-3b85-543b-b2e0-0cb69b197ded", "Michael Melkonian", "516"),
    44: ("2c99f3a1-3b85-543b-b2e0-0cb69b197ded", "Michael Melkonian", "516"),
    45: ("b6a814ed-479e-5e1f-83a6-e0b6cb48de16", "Constance L Mellen", "516"),
    46: ("1ae517c5-847f-5f78-a4c8-8dba7635158a", "Bert E Mellgren", "516"),
}

# The accepted categories below require an accepted, nonshared Army identity
# bridge and a code legible in the visually checked official code list. Codes
# tied to conflicting identities, and code 992 (not defined in the reviewed
# code list), are deliberately not published.
ARMY_OCCUPATIONS = {
    3: ("1942-11-30", "117", "file clerk", "File clerks", "PDF physical page 171; historical code 1-17"),
    6: ("1942-10-23", "732", "construction occupation, n.e.c.", "Construction occupations, n.e.c.", "PDF physical page 174; historical code 7-32"),
    15: ("1942-09-05", "022", "lawyer or judge", "Lawyers and judges", "PDF physical page 171; historical code 0-22"),
    16: ("1943-06-29", "736", "chauffeur or bus, taxi, truck, or tractor driver", "Chauffeurs and drivers, bus, taxi, truck, and tractor", "PDF physical page 174; historical code 7-36"),
    20: ("1945-02-01", "068", "semiprofessional occupation, n.e.c.", "Semiprofessional occupations, n.e.c.", "PDF physical page 171; historical code 0-68"),
    28: ("1945-02-06", "448", "pressman or plate printer in printing", "Pressmen and plate printers, printing", "PDF physical page 173; historical code 4-48"),
    30: ("1943-03-20", "748", "sailor or deckhand, except U.S. Navy", "Sailors and deckhands, except U.S. Navy", "PDF physical page 174; historical code 7-48"),
    31: ("1943-06-08", "685", "welder or flame cutter", "Welders and flame cutters", "PDF physical page 174; historical code 6-85"),
    34: ("1943-06-22", "266", "policeman or detective in public service", "Policemen and detectives, public service", "PDF physical page 172; historical code 2-66"),
    36: ("1943-02-08", "227", "waiter, except private family", "Waiters and waitresses, except private family", "PDF physical page 172; historical code 2-27"),
    37: ("1942-06-25", "017", "electrical engineer", "Engineers, electrical", "PDF physical page 170; historical code 0-17"),
    40: ("1941-03-13", "125", "office machine operator", "Office machine operators", "PDF physical page 171; historical code 1-25"),
    46: ("1943-01-18", "062", "showman", "Showmen", "PDF physical page 171; historical code 0-62"),
}

VERIFIED_EMPLOYER_ROWS = {7, 14, 35}
DOCUMENTED_PREWAR_ROWS = {30}
IDENTITY_REVIEW_ROWS = {19}
CONFLICT_ROWS = {17, 18, 23, 32, 41, 43}
PRESERVE_HIGH_IDENTITY_ARCHIVAL_ROWS = {21, 22, 38}
OCCUPATION_ONLY_ROWS = set(ARMY_OCCUPATIONS) - DOCUMENTED_PREWAR_ROWS


def unique_rows() -> list[int]:
    seen: set[str] = set()
    rows: list[int] = []
    for row, (person_id, _name, _box) in PEOPLE.items():
        if person_id not in seen:
            seen.add(person_id)
            rows.append(row)
    return rows


UNIQUE_ROWS = set(unique_rows())
ARCHIVAL_ROWS = UNIQUE_ROWS - (
    VERIFIED_EMPLOYER_ROWS
    | DOCUMENTED_PREWAR_ROWS
    | IDENTITY_REVIEW_ROWS
    | CONFLICT_ROWS
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
            archival_identifier="RG 226, Entry A1-224, Boxes 515-516",
            title="OSS Personnel Files from Excel",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="2010-12-23",
            locator="PDF page 315, rows 1-46; every printed row visually checked against the official PDF",
            source_quality="A_direct_official",
            collection_name="Records of the Office of Strategic Services, Record Group 226",
            rights_notes="All 46 printed rows remain separately preserved. The rendered first row reads Joseph Meegan; the embedded text transposition remains in immutable raw fields. Full protected identifiers remain private.",
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
            locator="PDF physical pages 170-174; every published Batch 1060 category visually checked",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records technical documentation",
            rights_notes="Historical categories are published only as qualified Army-entry occupations, never as named employers. Unlisted and identity-conflict codes remain unpublished.",
        ),
    ]


def army_affiliation_key(row: int) -> str:
    return f"army-entry-{slug(PEOPLE[row][1])}-b1060"


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


def conflict_action(row: int) -> str:
    actions = {
        17: "Inspect Box 515 before accepting the Mehillos/Mehilos spelling or transferring any Army occupation.",
        18: "Inspect Box 515 before accepting the Mehner/Mohner spelling or transferring any Army occupation.",
        23: "Inspect Box 516 for suffix, branch, birth date, and identifiers before choosing between the two John J. Meily candidates.",
        32: "Inspect Box 516 to resolve why the printed identifier maps to William G. Wood; do not transfer that Army occupation.",
        41: "Inspect Box 516 before accepting the Melinkoff/Melnikoff spelling or transferring any Army occupation.",
        43: "Inspect both Michael Melkonian entries in Box 516 before accepting the Melkonian/Milkonian spelling or transferring any Army occupation.",
    }
    return actions[row]


def person_updates() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row in unique_rows():
        person_id, name, box = PEOPLE[row]
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
                7: "Review Box 515 for the exact Army-to-OSS selection date and any narrower Army assignment.",
                14: "Review Box 515 and the Gaudens Megaro papers for exact Queens College leave and COI-to-OSS appointment dates.",
                35: "Review Box 516 for exact Army and OSS assignment dates while retaining Radio City Music Hall as the last documented civilian employer.",
            }
            update.update(
                manual_review_required=False,
                research_status="verified_employer_found",
                next_action=next_actions[row],
                archival_review_priority="high",
            )
        elif row in DOCUMENTED_PREWAR_ROWS:
            update.update(
                manual_review_required=False,
                research_status="documented_prewar_employer_found",
                next_action="Review Box 516 and Norwegian seamen's records to identify any 1940-1942 civilian work and document the exact 99th Infantry Battalion-to-OSS transfer.",
                archival_review_priority="high",
            )
        elif row in IDENTITY_REVIEW_ROWS:
            update.update(
                manual_review_required=True,
                research_status="needs_identity_review",
                next_action="Inspect Box 515 for a direct bridge to the probable Lincoln Mei Army officer identity before researching pre-Army employment.",
                archival_review_priority="critical",
            )
        elif row in CONFLICT_ROWS:
            update.update(
                manual_review_required=True,
                research_status="conflicting_sources",
                next_action=conflict_action(row),
                archival_review_priority="critical",
            )
        else:
            if row not in ARCHIVAL_ROWS:
                raise RuntimeError(f"Unclassified page-315 row {row}")
            if row not in PRESERVE_HIGH_IDENTITY_ARCHIVAL_ROWS:
                update.update(
                    identity_status="unresolved",
                    identity_evidence=(
                        "The official index context and saved staged exact-name, meaningful-variant, OSS, CIA-domain, employment, occupation, institutional, newspaper, obituary, directory, and archival checks produced no reliable identity and pre-OSS affiliation bridge; unbridged namesakes were rejected."
                    ),
                )
            update.update(
                manual_review_required=True,
                research_status="requires_archival_review",
                next_action=unresolved_message(name, box),
                personnel_file_digitized=False,
                personnel_file_reviewed=False,
                archival_review_priority="high",
            )
            if row in {21, 22}:
                update["next_action"] = (
                    f"Review Box {box} for a named pre-OSS employer and the Army-to-OSS sequence. "
                    "The accepted Army identity bridge records an occupation code that was not defined in the visually reviewed official list and is not published as an occupation."
                )
            elif row == 38:
                update["next_action"] = (
                    "Review Box 516 and Greenville-area prewar sources for Michael Melehes's employer or occupation; the direct OSS Detachment 101 identity remains high confidence."
                )
            elif row == 1:
                update["identity_evidence"] = (
                    "Visual inspection of the official page shows Joseph Meegan; the immutable embedded-text extraction transposed the first name as Jospeh. Saved exact-name and spelling-variant searches did not establish an external identity or pre-OSS affiliation."
                )
                update["next_action"] = unresolved_message("Joseph Meegan", box)
        values.append(update)
    if len(values) != 45 or len({item["person_id"] for item in values}) != 45:
        raise RuntimeError("Expected 45 page-315 person updates for 46 source rows")
    return values


def outcome_note(row: int) -> str:
    if row in OCCUPATION_ONLY_ROWS:
        return "An accepted official Army identity link supports a qualified dated occupation but no named employer, institution, workplace, or OSS-transfer sequence."
    if row == 30:
        return "The documented D/S Cate B merchant-sea work and 99th Infantry Battalion-to-OSS pathway remain unchanged; the Army category is qualified and does not fill the 1940-1942 chronology gap."
    if row == 7:
        return "The existing Treasury, Solicitor General, and Army-to-OSS chronology remains unchanged and distinct from private employment."
    if row == 14:
        return "The existing Queens College last-civilian-employer and COI immediate-predecessor claims remain unchanged."
    if row == 35:
        return "The existing Radio City Music Hall last-employer and Army pathway claims remain unchanged."
    if row in CONFLICT_ROWS:
        return "The saved identity conflict remains visible; no employer or Army occupation crossed the unresolved name, identifier, suffix, or duplicate boundary."
    if row == 19:
        return "The probable Lincoln Mei officer identity remains qualified; its postwar employer was excluded and no pre-OSS affiliation was assigned."
    if row in {21, 22}:
        return "The accepted official Army identity bridge remains high confidence, but undefined code 992 was not converted into an occupation or employer."
    if row == 38:
        return "A direct OSS Detachment 101 record establishes the wartime identity, but accessible sources do not identify a reliable pre-OSS employer."
    if row == 1:
        return "The normalized display was corrected to the visually printed Joseph Meegan while the raw embedded-text transposition remains preserved; no external identity or affiliation was established."
    return "No reliable identity or pre-OSS affiliation was established; unbridged namesakes, snippets, and chronologically irrelevant results were rejected."


def research_attempts() -> list[dict[str, object]]:
    updates = {item["person_id"]: item for item in person_updates()}
    values: list[dict[str, object]] = []
    for row in unique_rows():
        person_id, name, box = PEOPLE[row]
        if row in ARMY_OCCUPATIONS:
            outcome, reviewed, rejected = "source_reviewed", 4, 3
        elif row in VERIFIED_EMPLOYER_ROWS | DOCUMENTED_PREWAR_ROWS:
            outcome, reviewed, rejected = "source_reviewed", 5, 2
        elif row in IDENTITY_REVIEW_ROWS | CONFLICT_ROWS:
            outcome, reviewed, rejected = "candidate_rejected", 3, 4
        elif row in PRESERVE_HIGH_IDENTITY_ARCHIVAL_ROWS | {1}:
            outcome, reviewed, rejected = "source_reviewed", 3, 3
        else:
            outcome, reviewed, rejected = "no_result", 2, 3
        values.append(
            {
                "key": f"page315-row{row}-{slug(name)}-b1060",
                "person_id": person_id,
                "source_adapter": "manual_saved_protocol_completion",
                "query_text": f"{name}; NARA OSS index context; exact-name and meaningful initial, punctuation, spacing, spelling and OCR variants; CIA Reading Room/domain discovery; OSS, rank, branch, assignment and private-identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory and archival searches; indexed Box {box}",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_1060",
                "started_at": "2026-11-11T20:45:00-05:00",
                "completed_at": "2026-11-11T21:30:00-05:00",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, postwar-only leads, and sources without an OSS, rank, private-identifier, unit, or personnel-file bridge were rejected. Army categories were not converted into named employers; duplicate-row, identifier, and spelling conflicts were not promoted.",
                "research_notes": f"{outcome_note(row)} Page 315 was visually checked against the official NARA index, and every published Army occupation code was visually checked against the official code-list PDF. Saved exact-name OSS, CIA-domain, employment, occupation, obituary, institutional, newspaper, directory, and archival outcomes from earlier staged passes were re-reviewed as applicable. Existing cited claims were preserved without duplication. No search-result snippet was used as final evidence and no authenticated NARA Catalog API request was made.",
                "next_action": str(updates[person_id]["next_action"]),
                "attempt_number": 6,
                "research_agent_version": "before-oss-b1060-v1",
            }
        )
    return values


def build_bundle() -> dict[str, object]:
    return {
        "bundle_version": "batch-1060-v1",
        "reviewer": "Before OSS Batch 1060 evidence review",
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
    OUTPUT.write_text(
        json.dumps(bundle, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
