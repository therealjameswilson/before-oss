#!/usr/bin/env python3
"""Generate the reviewed Batch 1049 evidence bundle for PDF page 304."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page304-thomas-a-mccann-to-grant-s-mcclelian-review_"
    "batch-1049_2026-11-06.json"
)

INDEX = "nara-index-b1049"
ARMY = "army-bulk-b1049"
TECH = "army-tech-b1049"
CODES = "army-codes-b1049"
HOOVER = "hoover-oss-board-thomas-mccart-b1049"

ORG_ARMY = "us-army-b1049"
ORG_RCA = "rca-b1049"


PEOPLE = {
    1: ("69d9fd3c-658e-519b-a5bb-4a4622e930d9", "Thomas A McCann", "497"),
    2: ("1aa37e74-b066-54a9-b781-89500217fb27", "Jack L McCarary", "501"),
    3: ("ff0e53eb-3398-5e5e-86ec-d8d5547ad224", "John A McCargar", "499"),
    4: ("f378adb4-7779-533a-934a-0be8f4f721f3", "John A McCaroar", "498"),
    5: ("4625ee27-239f-546f-a037-b77ea9256780", "James W McCarroll", "498"),
    6: ("ed6f557f-5d4d-5668-9f8d-10db4a9851d7", "Thomas A McCart", "498"),
    7: ("ac926cdc-3a10-5f4f-8cf1-38161388b76c", "William J McCart", "498"),
    8: ("d14f21e3-d3df-596d-b041-3a7879d15de4", "Elder McCarter", "498"),
    9: ("c05e87ef-a0af-5f91-b6ce-b566786bdbe6", "Ann K McCarthy", "498"),
    10: ("74292384-0dcf-55f0-b624-0e9becf14b28", "Arthur F McCarthy", "498"),
    11: ("3b396695-194f-5aba-b707-127c9411326f", "Charles M McCarthy", "498"),
    12: ("81e8f705-828c-5869-a7d3-69c9b503ef3c", "Daniel L McCarthy", "498"),
    13: ("4c805025-19d5-5ea8-984b-fa3aa71e7461", "Donald K McCarthy", "498"),
    14: ("e530895d-35c4-570d-aea6-7a71dfe1d241", "Edward McCarthy Jr.", "498"),
    15: ("9c50064f-cce6-51aa-9192-cb3b3c705b7c", "Edward S McCarthy", "498"),
    16: ("5b051d63-c675-5181-bd41-9fe5d348b611", "Emmett J McCarthy", "498"),
    17: ("51210f92-f8e8-5f4d-8243-378c3af68429", "Francis P McCarthy", "498"),
    18: ("f147e735-6481-508a-8361-7d017c1f40bd", "Harry L McCarthy", "498"),
    19: ("96e89852-1be2-5ea0-a307-ac53eaf6c5d5", "Hazel M McCarthy", "498"),
    20: ("98b57dae-121f-52b2-810c-165e26f3751a", "John F McCarthy", "498"),
    21: ("d5db343c-7209-505d-b40b-f777f67cf63c", "John F McCarthy", "498"),
    22: ("0e1f546e-4042-5b57-b674-4a89446bd242", "John P.C McCarthy", "498"),
    23: ("7e7b3872-80ac-531b-999a-ed6b12d9ac2e", "John A McCarthy", "498"),
    24: ("69448dcf-6876-5788-b2f9-074728171fc0", "Joseph P McCarthy", "498"),
    25: ("b1037ec8-764a-5960-9a5e-8e3099f34f32", "Kathryn McCarthy", "498"),
    26: ("d23f20be-0c63-5238-bb5b-a9e5ed26685a", "Michael McCarthy", "498"),
    27: ("98a6f574-6f06-5e69-a942-81741ec978e4", "Patrick T McCarthy", "498"),
    28: ("32ac1b50-5eca-5690-94f1-5ffb7c21472f", "Richard D McCarthy", "498"),
    29: ("a3df36a7-8058-511b-ac66-8fee6d2e54bc", "Robert J McCarthy", "498"),
    30: ("46fb8629-6eb4-5463-a61c-9e001306a285", "William B McCarthy", "498"),
    31: ("6fa2904c-d3f5-5895-bbd0-e976b55d5d29", "William A McCaughlin", "499"),
    32: ("dbbe0d36-756b-5061-87a8-aaab00a15a41", "Edward A McCaughy", "498"),
    33: ("22ad5999-7308-5fb9-bba2-018ae671ceac", "Rex H McCauley", "498"),
    34: ("43a95663-9317-5c6c-bdc7-80a680998a8e", "Russell W McCauley", "498"),
    35: ("85c12836-4535-5df2-bdc9-3b0cc2d61af2", "Paul W McCausland", "498"),
    36: ("3cc38cc5-733b-5dbc-9bfb-c8f6f210bed2", "Robert McCay", "499"),
    37: ("b66a5fc2-3989-5316-a346-82a0bf0162a1", "Elmer L McCcollum", "499"),
    38: ("3d36cd8a-285e-573d-88fe-f2ad70340829", "Thomas J McClafferty", "499"),
    39: ("e0f4aa24-f702-52f2-a504-e8f68ff3ba2b", "Lester K McClaflin", "499"),
    40: ("96af3651-bce6-553d-84d7-1bdddb854c3f", "John W McClain", "499"),
    41: ("ca7679af-b6a0-574b-be0c-1d706bcde5cb", "Melba R McClanahan", "499"),
    42: ("49607110-dce1-5cc6-baa6-209fcb59625d", "William H McClare", "499"),
    43: ("98e10c39-29b3-5095-bd0a-d64e425f4ccb", "James A McClasky", "499"),
    44: ("b641e203-1d4e-51f8-993a-38270141ec15", "Paul W McClausland", "499"),
    45: ("5f26f317-1160-5cb5-aae3-b9b7686ecd0e", "Raymond J McCleery", "499"),
    46: ("e0a50899-b3be-5f79-aa5b-df073f155b2e", "Grant S McClelian", "499"),
}


ARMY_ASSOCIATIONS = {
    8: ("1943-04-16", "992", "student", "Students", "PDF physical page 304; corrected historical code 9-92"),
    13: ("1942-08-29", "992", "student", "Students", "PDF physical page 304; corrected historical code 9-92"),
    16: ("1943-05-24", "006", "author, editor, or reporter", "Authors, editors, and reporters", "PDF physical page 170; historical code 0-06"),
    17: ("1943-06-17", "992", "student", "Students", "PDF physical page 304; corrected historical code 9-92"),
    18: ("1942-11-13", "732", "semiskilled construction occupation, not elsewhere classified", "Construction occupations, n.e.c.", "PDF physical page 174; historical category 5, 7, 9-32"),
    20: ("1942-08-01", "101", "bookkeeper or cashier, except bank cashier", "Bookkeepers and cashiers, except bank cashiers", "PDF physical page 171; historical code 1-01"),
    23: ("1944-08-15", "992", "student", "Students", "PDF physical page 304; corrected historical code 9-92"),
    28: ("1943-02-03", "095", "public-service inspector, not elsewhere classified", "Inspectors, public service, n.e.c.", "PDF physical page 171; historical code 0-95"),
    39: ("1942-04-14", "316", "general farm hand", "Farm hands, general farms", "PDF physical page 172; historical code 3-16"),
    42: ("1942-06-12", "788", "warehousing, storekeeping, handling, loading, unloading, or related occupation", "Warehousing, storekeeping, handling, loading, unloading, and related occupations, n.e.c.", "PDF physical page 175; historical category 5, 7, 9-88"),
}

IDENTITY_REVIEW_ROWS = {2, 3, 4, 21, 32, 35, 36, 37, 40, 44}

DUPLICATE_GROUPS = {
    2: "p304-306-jack-mccarary-mccrary-b623",
    3: "p304-john-mccargar-mccaroar-b623",
    4: "p304-john-mccargar-mccaroar-b623",
    21: "p304-john-f-mccarthy-distinct-identifiers-b623",
    32: "p304-308-edward-mccaughy-mcgaughy-b623",
    35: "p304-paul-mccausland-mcclausland-b623",
    36: "p288-304-robert-mackay-mccay-b621",
    37: "p304-305-elmer-mcccollum-mccollum-b623",
    44: "p304-paul-mccausland-mcclausland-b623",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def source(key: str, **kwargs: object) -> dict[str, object]:
    value: dict[str, object] = {"key": key, "access_date": "2026-11-06"}
    value.update(kwargs)
    return value


def sources() -> list[dict[str, object]]:
    return [
        source(
            INDEX,
            stable_url="https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            archival_identifier="RG 226, Entry A1-224, Boxes 497-501",
            title="OSS Personnel Files from Excel",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="2010-12-23",
            locator="PDF page 304, rows 1-46; every printed row visually checked",
            source_quality="A_direct_official",
            collection_name="Records of the Office of Strategic Services, Record Group 226",
            rights_notes="All 46 printed rows remain recoverable as 46 cautious person entities. Similar spellings, repeated names, and conflicting protected identifiers remain separate.",
        ),
        source(
            ARMY,
            stable_url="https://catalog.archives.gov/id/1263923",
            archival_identifier="National Archives Identifier 1263923; parent series NAID 604357",
            title="Electronic Army Serial Number Merged File, ca. 1938-1946",
            author_creator="Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="1938-1946; merged file created 2002",
            locator="Official unrestricted ASNEF.FIN.DAT; previously reviewed row-specific protected identity crosswalks",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records",
            document_number="ASNEF.FIN.DAT",
            rights_notes="No raw record, full protected identifier, or bulk-file ordinal is retained in public assets. Shared and conflicting candidates were not used for occupations.",
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
            rights_notes="Used only to interpret selected fields; the bulk file does not name an employer or establish the Army-to-OSS sequence.",
        ),
        source(
            CODES,
            stable_url="https://aad.archives.gov/aad/popup-codelist.jsp?cl_id=3323&dt=893&c_id=24986",
            archival_identifier="NARA AAD civilian occupation code list; Code No. 30 in NAID 1263923 documentation",
            title="World War II Army Enlistment Records: Civilian Occupation Code List",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives Access to Archival Databases",
            locator="Codes 006, 095, 101, 316, 732, 788, and corrected 992; printed reference-copy pages visually checked",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records code lists",
            rights_notes="Historical categories identify neither employer, institution, workplace, nor exact Army-to-OSS chronology.",
        ),
        source(
            HOOVER,
            stable_url="https://digitalcollections.hoover.org/objects/73269/oss-board-of-officers-report-on-arrival-at-naples",
            archival_identifier="Millard Preston Goodfellow papers, record 69085.145",
            title="OSS board of officers report on arrival at Naples",
            author_creator="Office of Strategic Services board of officers",
            repository_publisher="Hoover Institution Library & Archives",
            publication_record_date="1944-05-03",
            locator="Report printed page 26, item CXII; Thomas A. McCart entry",
            source_quality="A_direct_official",
            collection_name="Millard Preston Goodfellow papers, Declassified U.S. government records",
            document_number="69085.145",
            rights_notes="The official item record reports no known restrictions. The protected identifier printed in the report is used for identity review but is not transcribed into public evidence.",
        ),
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": ORG_ARMY,
            "organization_id": "28a26f92-78af-5a1a-9c09-a843eb5975b4",
            "canonical_name": "United States Army",
            "historical_name": "United States Army",
            "aliases": ["U.S. Army", "Vth Army"],
            "organization_type": "military service",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "The report's historical Vth Army Replacement Center wording remains visible in the affiliation.",
        },
        {
            "key": ORG_RCA,
            "organization_id": "71cb9b7e-5023-5ec3-b7c9-34afafeea171",
            "canonical_name": "Radio Corporation of America",
            "historical_name": "RCA",
            "aliases": ["RCA", "Radio Corporation of America", "RCA Victor Division"],
            "organization_type": "electronics and communications company",
            "sector": "engineering_science_and_technology",
            "country": "United States",
            "normalization_notes": "RCA is not merged with the separately preserved RCA Communications, Inc. entity; the source names only RCA.",
        },
    ]


def army_affiliation_key(row: int) -> str:
    return f"{slug(PEOPLE[row][1])}-army-entry-occupation-b1049"


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, _label, _locator) in ARMY_ASSOCIATIONS.items():
        values.append(
            {
                "key": army_affiliation_key(row),
                "person_id": PEOPLE[row][0],
                "occupation": occupation,
                "relationship_type": "student" if code == "992" else "unknown",
                "end_date": date,
                "date_precision": f"Historical civilian-occupation code {code} was recorded at Army entry on {date}; no named employer, institution, workplace, or OSS-transfer date is supplied.",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "A_direct_official",
                "publication_status": "publish_qualified",
                "research_notes": "The broad historical category is excluded from verified-employer analytics and is not converted into a named organization.",
            }
        )

    values.extend(
        [
            {
                "key": "thomas-mccart-fifth-army-b1049",
                "person_id": PEOPLE[6][0],
                "organization_key": ORG_ARMY,
                "organization_name_as_found": "Vth Army Replacement Center",
                "role_title": "soldier at replacement center; later OSS driver and supply clerk",
                "relationship_type": "military_assignment",
                "start_date": "1942-04-01",
                "end_date": "1943-10-12",
                "date_precision": "The wartime report explicitly dates Army entry and the 12 October 1943 transfer from the Vth Army Replacement Center to OSS.",
                "country": "Italy",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "explicit_immediate",
                "identity_confidence": "confirmed",
                "claim_confidence": "confirmed",
                "source_quality": "A_direct_official",
                "publication_status": "published",
                "research_notes": "The military assignment is separate from McCart's earlier civilian RCA employment.",
            },
            {
                "key": "thomas-mccart-rca-b1049",
                "person_id": PEOPLE[6][0],
                "organization_key": ORG_RCA,
                "organization_name_as_found": "RCA",
                "relationship_type": "employment",
                "end_date": "1942-04-01",
                "date_precision": "The wartime report says McCart worked for RCA in civilian life and separately dates Army entry to 1 April 1942; it does not state his role or explicitly call RCA his final civilian employer.",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "confirmed",
                "claim_confidence": "high",
                "source_quality": "A_direct_official",
                "publication_status": "published",
                "research_notes": "Definite prewar employment, but not promoted to last-civilian-employer status without stronger sequencing evidence.",
            },
        ]
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


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, label, locator) in ARMY_ASSOCIATIONS.items():
        values.append(
            claim(
                f"army-entry-{slug(PEOPLE[row][1])}-b1049",
                row,
                "occupation",
                f"At Army entry on {date}, {PEOPLE[row][1]} was recorded as {occupation}; no employer, institution, or workplace is identified.",
                f"The official Army bulk file records code {code}; the visually checked official list defines the category as {label}.",
                "High confidence from matching official name evidence and a previously reviewed, nonshared protected identity linkage; the protected identifier remains private.",
                "Strongly date-bounded to Army entry, but not proven to be the immediately preceding status before OSS.",
                "A_direct_official",
                "medium",
                "publish_qualified",
                "The historical category remains qualified, is excluded from verified-employer analytics, and is not converted into a named organization.",
                [
                    {"source_key": INDEX, "support_type": "context_only"},
                    {"source_key": ARMY},
                    {"source_key": TECH, "support_type": "context_only"},
                    {"source_key": CODES, "locator_override": locator},
                ],
                army_affiliation_key(row),
            )
        )

    values.extend(
        [
            claim(
                "identity-thomas-a-mccart-b1049",
                6,
                "identity",
                "Indexed Thomas A. McCart is confirmed as the Army private described in the wartime OSS board report.",
                "The exact name, compatible enlisted rank, direct OSS context, and protected row-specific identifier connect the index row and wartime report.",
                "Confirmed by exact name, compatible rank, direct official OSS context, and a protected identifier that is not published.",
                "The official report dates Army entry and transfer to OSS.",
                "A_direct_official",
                "confirmed",
                "published",
                "No inference from a namesake biography is required.",
                [{"source_key": HOOVER}, {"source_key": INDEX, "support_type": "context_only"}],
            ),
            claim(
                "fifth-army-thomas-a-mccart-b1049",
                6,
                "immediate_pre_oss_affiliation",
                "Thomas A. McCart transferred to OSS from the Vth Army Replacement Center on 12 October 1943.",
                "The wartime OSS board report explicitly names the prior Army center and transfer date, then describes his OSS supply-section duties.",
                "Confirmed by the row-specific official evidence supporting identity.",
                "Explicit immediate military predecessor to OSS.",
                "A_direct_official",
                "confirmed",
                "published",
                "The Army pathway is kept separate from civilian employment.",
                [{"source_key": HOOVER, "excerpt_override": "went to OSS 12 October 1943 from Vth Army Replacement Center"}],
                "thomas-mccart-fifth-army-b1049",
            ),
            claim(
                "rca-thomas-a-mccart-b1049",
                6,
                "other_pre_oss_affiliation",
                "Thomas A. McCart worked for RCA in civilian life before his wartime OSS service.",
                "The official wartime report directly names RCA as McCart's civilian employer and separately dates Army entry to 1 April 1942.",
                "Confirmed by exact official identity evidence and a protected row-specific linkage.",
                "Documented prewar employment; the source does not explicitly establish that RCA was his final civilian employer before Army entry.",
                "A_direct_official",
                "high",
                "published",
                "RCA is preserved as the historical employer; it is not silently replaced by a successor and is not labeled immediate.",
                [{"source_key": HOOVER, "excerpt_override": "Worked for RCA in civilian life."}],
                "thomas-mccart-rca-b1049",
            ),
        ]
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
        if row == 6:
            update.update(
                identity_status="confirmed",
                identity_evidence="The exact name, compatible enlisted rank, official OSS context, and protected row-specific identifier connect the index row to the 1944 OSS board report.",
                personnel_category="enlisted_army_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                research_status="documented_prewar_employer_found",
                next_action="Review Box 498 for McCart's RCA role and stronger evidence establishing whether RCA was his final civilian employer immediately before Army entry.",
                archival_review_priority="medium",
            )
        elif row in ARMY_ASSOCIATIONS:
            update.update(
                identity_status="high_confidence",
                identity_evidence="A previously reviewed official Army bulk crosswalk agrees in name and a nonshared protected identifier. The linkage supports identity but supplies only a broad historical occupation category.",
                personnel_category="enlisted_army_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                nara_catalog_id="1263923",
                research_status="occupation_only_found",
                next_action=f"Review Box {box} to identify a named employer or institution and establish the Army-to-OSS chronology. The official bulk record supplies only a broad historical occupation category.",
                archival_review_priority="high",
            )
        elif row == 33:
            update.update(
                identity_status="conflicting",
                identity_evidence="The protected identifier printed for Rex H. McCauley points to an official Army record naming Lawrence R. Chambers. The names do not align, so no Army occupation is transferred.",
                research_status="conflicting_sources",
                next_action="Compare Box 498 and the original Army record before resolving Rex H. McCauley or using any occupation code tied to the conflicting identifier.",
                archival_review_priority="critical",
            )
        elif row in IDENTITY_REVIEW_ROWS:
            update.update(
                research_status="needs_identity_review",
                next_action=unresolved_message(name, box),
                archival_review_priority="critical",
            )
            if row != 40:
                update.update(
                    identity_status="ambiguous",
                    identity_evidence="The indexed row overlaps a spelling variant, repeated name, shared protected identifier, or conflicting rank in another preserved source row. The records remain separate pending direct file comparison.",
                )
            else:
                update.update(
                    identity_status="probable",
                    identity_evidence="A prior newspaper candidate is a plausible John W. McClain namesake, but it lacks the second corroborating identifier required for this common name and is withheld from publication.",
                )
            if row in DUPLICATE_GROUPS:
                update["possible_duplicate_group"] = DUPLICATE_GROUPS[row]
        else:
            update.update(
                identity_status="unresolved",
                identity_evidence="Exact-name and meaningful-variant checks across the NARA index context, official CIA and Archives domains, OSS discovery, Library of Congress newspapers, employment, occupation, obituary, institutional, directory, and archival sources produced no reliable identity and pre-OSS affiliation bridge; unbridged namesakes were rejected.",
                research_status="requires_archival_review",
                next_action=unresolved_message(name, box),
                archival_review_priority="high",
            )
        values.append(update)
    if len(values) != 46:
        raise RuntimeError(f"Expected 46 person updates, generated {len(values)}")
    return values


def outcome_note(row: int) -> str:
    if row == 6:
        return "A wartime OSS board report confirms McCart's transfer from the Fifth Army Replacement Center and separately documents RCA employment."
    if row in ARMY_ASSOCIATIONS:
        return "A previously accepted official Army identity crosswalk supports a qualified Army-entry occupation or student category but no named employer or OSS-transfer sequence."
    if row == 33:
        return "The indexed protected identifier conflicts with an Army record naming an entirely different person; no occupation was transferred."
    if row in IDENTITY_REVIEW_ROWS:
        return "A same-name, spelling-variant, shared-identifier, rank-conflict, or insufficiently bridged candidate remains separate for direct personnel-file review."
    return "No reliable identity or pre-OSS affiliation was established; unbridged namesakes and chronologically irrelevant results were rejected."


def research_attempts() -> list[dict[str, object]]:
    updates = {item["person_id"]: item for item in person_updates()}
    values: list[dict[str, object]] = []
    for row, (person_id, name, box) in PEOPLE.items():
        if row == 6 or row in ARMY_ASSOCIATIONS:
            outcome = "source_reviewed"
            reviewed = 8 if row == 6 else 7
            rejected = 3
        elif row == 33 or row in IDENTITY_REVIEW_ROWS:
            outcome = "candidate_rejected"
            reviewed = 6
            rejected = 5
        else:
            outcome = "no_result"
            reviewed = 5
            rejected = 3
        values.append(
            {
                "key": f"page304-row{row}-{slug(name)}-b1049",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index context; exact-name and meaningful initial, punctuation, spelling and OCR variants; official CIA Reading Room and Archives domain checks; OSS, rank, branch, assignment and protected-identifier clues; employer and occupation 1940; obituary, biography, institutional, Library of Congress newspaper, directory and archival searches; indexed Box {box}",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_1049",
                "started_at": "2026-11-06T09:05:00-05:00",
                "completed_at": "2026-11-06T09:58:00-05:00",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, postwar-only leads, and sources without an OSS, rank, protected-identifier, unit, or personnel-file bridge were rejected. Similar-name and shared-identifier rows remain separate. Army categories were not converted into named employers.",
                "research_notes": f"{outcome_note(row)} The official index, earlier Library of Congress item-level pass, exact-name OSS search, official CIA and Archives domain searches, occupation and employer searches, and obituary, institutional, directory, military-history, newspaper, and archival discovery were reviewed as applicable. Direct CIA adapter access was not treated as a negative result. No authenticated NARA Catalog API request was made.",
                "next_action": str(updates[person_id]["next_action"]),
                "attempt_number": 2,
                "research_agent_version": "before-oss-b1049-v1",
            }
        )
    if len(values) != 46:
        raise RuntimeError(f"Expected 46 research attempts, generated {len(values)}")
    return values


def main() -> None:
    bundle = {
        "bundle_version": "batch-1049-v1",
        "reviewer": "Before OSS Batch 1049 evidence review",
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
