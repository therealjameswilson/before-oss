#!/usr/bin/env python3
"""Generate the reviewed Batch 1046 evidence bundle for PDF page 301."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page301-josef-matuszowicz-to-lewis-l-may-review_"
    "batch-1046_2026-11-05.json"
)

INDEX = "nara-index-b1046"
ARMY = "army-bulk-b1046"
TECH = "army-tech-b1046"
CODES = "army-codes-b1046"
DET101 = "oss-detachment-101-promotions-b1046"


# Row 19 is the second immutable source row for the same Joseph P. Mauro entity.
PEOPLE = {
    1: ("fd2cc206-3286-56f2-a7f2-f338b7dc2898", "Josef Matuszowicz", "492"),
    2: ("d9ef67dd-d79c-5adf-8565-8146fa7225dd", "John A Matuzsa", "492"),
    3: ("2cfe71e7-66c3-5081-b32c-a92e34139e09", "Alvin H Matz", "492"),
    4: ("90d03d3a-dba1-5886-b612-b39efed74330", "Lewis M Maudsley", "492"),
    5: ("50a8b427-21e6-511d-a21f-c924b6124d2a", "Joseph J Maugeri", "492"),
    6: ("76f4ed04-d71e-51b7-865b-573955bf7c77", "Richard F Mauksch", "492"),
    7: ("a13eb496-af35-544d-8c3a-066edc2f56e6", "Paul M Maulis", "492"),
    8: ("b537425c-055d-516f-b61d-b2e7464018e8", "Ko Maung", "492"),
    9: ("7db9341c-9705-54b8-8314-c1e4a382f23f", "Frank Mauran Jr.", "492"),
    10: ("b001208c-f2a2-5b05-94e1-f568d4057371", "Georges Maurel", "492"),
    11: ("03f27616-b31e-5c6a-8927-eabc194d802c", "Charlotte Maurer", "492"),
    12: ("bfe0137d-1126-5be1-b24a-f662bd03cdae", "Maurietta J Maurer", "492"),
    13: ("c91c1189-4736-5fb9-93e4-06990d352976", "Norman F Maurer", "492"),
    14: ("c516c4e3-dc96-5e9e-84a3-67277e5ef6f2", "Raymond J Maurer", "492"),
    15: ("a894ff08-c339-5462-9bfc-be17e3ff6908", "Anthony Mauro", "492"),
    16: ("4547df27-17c8-586b-a93f-a142b84ec7d9", "Dominick C Mauro", "492"),
    17: ("98254b52-cb7b-518a-ae69-58e318dbb8b5", "James V Mauro", "492"),
    18: ("afb2ef1d-8661-50fc-8e0a-27938f5d56b7", "Joseph P Mauro", "492-493"),
    20: ("1957decc-aa4c-52de-9c4b-7d610c328081", "Jean Maury", "492"),
    21: ("cf4f6e85-c132-53a0-9a94-c4160772b5e4", "Richard P Maury", "492"),
    22: ("4b97ed0c-9c0b-5f68-a7a1-c49471df5b6b", "Erwin Mauss", "492"),
    23: ("dc92c3c1-dd07-53b9-befd-b2e4f8ba018c", "Joseph P Mautner", "492"),
    24: ("64ba13a9-502e-5e08-8a9f-f753ddb6f93d", "Floyd E Maves", "493"),
    25: ("de9c3430-3063-5043-88fc-7c2221164e29", "Arthur B Mavis", "493"),
    26: ("51028b1e-5c4c-5549-9726-2ea57824bfe5", "Sam Mavromihales", "493"),
    27: ("c6ecd827-6f61-5917-966c-1facf5bce4c4", "John H Maxson", "493"),
    28: ("422f9595-566c-5c1b-80c9-2a182af1b14c", "Carlton Maxwell", "493"),
    29: ("bbdeca8e-84d8-571c-aa35-91064cd2dc10", "Charles Maxwell", "493"),
    30: ("55c24843-0cd5-57b7-90fe-f00f73427c20", "Howard Maxwell", "493"),
    31: ("bf7b573d-3118-55fe-b61e-f6d284d10163", "Raymond J Maxwell Jr.", "493"),
    32: ("9a838d2e-e71b-533a-82f3-07a519001f44", "Anthony B May", "493"),
    33: ("45245c34-6211-5e87-96af-34a8b95a1869", "Catherine H May", "493"),
    34: ("998260a2-da9c-5e4e-b7e5-e03b73ad0969", "Ernest R May", "493"),
    35: ("7f270962-a2f6-5652-ba53-f91fcc9ddcba", "Erwin May", "493"),
    36: ("b39c237a-1c75-5dd0-a2be-01b88172e126", "Georges May", "493"),
    37: ("96d23cce-ea21-58ca-a626-4e13d8243f04", "Georges May", "493"),
    38: ("9e518533-f0cd-51c7-bca3-458141224101", "Gerald May", "493"),
    39: ("5a9d35c6-967b-58de-8ed0-a4e55cdc8d4d", "Harold M May", "493"),
    40: ("2a8de0e1-363e-5aa4-9810-2789b834f1cb", "Henry T May", "493"),
    41: ("17b990f2-97e4-5298-a39a-628f140f3df6", "Iris F May", "493"),
    42: ("0982cbc4-221f-509c-b88b-953f26d89127", "Jacques G May", "493"),
    43: ("ce1a6a3c-c5be-5f8e-86c7-7e353aabbab9", "James Q May", "493"),
    44: ("8e6ab224-5d8d-5288-83d7-a65caa0dd44b", "Katherine H May", "493"),
    45: ("a61567ad-0471-53b2-b45f-e5b5da16086f", "Lester H May", "493"),
    46: ("eaf1cbb0-30ed-51a6-89b4-39ea1a7d3819", "Lewis L May", "493"),
}


# Official Army classifications are broad historical categories, not employers.
ARMY_ASSOCIATIONS = {
    2: ("1943-06-02", "316", "general farm hand", "Farm hands, general farms", "unknown"),
    4: ("1944-03-24", "170", "sales clerk", "Sales clerks", "unknown"),
    5: ("1943-04-22", "583", "skilled mechanic or repairman, not elsewhere classified", "Mechanics and repairmen, n.e.c.", "unknown"),
    14: ("1943-09-02", "478", "skilled machine-shop or related worker, not elsewhere classified", "Skilled machine shop and related occupations, n.e.c.", "unknown"),
    16: ("1942-12-01", "839", "unskilled worker in manufacture of miscellaneous finished lumber products, not elsewhere classified", "Occupations in manufacture of miscellaneous finished lumber products, n.e.c.", "unknown"),
    17: ("1943-07-05", "959", "worker in trades or services, not elsewhere classified", "Occupations in trades and services, n.e.c.", "unknown"),
    18: ("1943-03-19", "157", "insurance salesman", "Insurance salesmen", "unknown"),
    24: ("1943-01-07", "783", "semiskilled mechanic or repairman, not elsewhere classified", "Semiskilled mechanics and repairmen, n.e.c.", "unknown"),
    26: ("1942-11-25", "227", "waiter, except private-family service", "Waiters and waitresses, except private family", "unknown"),
    31: ("1942-11-18", "992", "student", "Students", "student"),
    32: ("1942-11-20", "316", "general farm hand", "Farm hands, general farms", "unknown"),
    37: ("1943-04-08", "031", "secondary-school teacher or principal", "Teachers (secondary school) and principals", "unknown"),
    39: ("1942-08-04", "175", "salesperson", "Salesmen, general", "unknown"),
    42: ("1943-04-08", "134", "shipping or receiving clerk", "Shipping and receiving clerks", "unknown"),
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def source(key: str, **kwargs: object) -> dict[str, object]:
    value: dict[str, object] = {"key": key, "access_date": "2026-11-05"}
    value.update(kwargs)
    return value


def sources() -> list[dict[str, object]]:
    return [
        source(
            INDEX,
            stable_url="https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            archival_identifier="RG 226, Entry A1-224, Boxes 492-493",
            title="OSS Personnel Files from Excel",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="2010-12-23",
            locator="PDF page 301, rows 1-46; every printed row visually checked",
            source_quality="A_direct_official",
            collection_name="Records of the Office of Strategic Services, Record Group 226",
            rights_notes="All 46 printed rows remain recoverable. The two Joseph P. Mauro rows remain separate source records linked cautiously to one person entity.",
        ),
        source(
            ARMY,
            stable_url="https://catalog.archives.gov/id/1263923",
            archival_identifier="National Archives Identifier 1263923; parent series NAID 604357",
            title="Electronic Army Serial Number Merged File, ca. 1938-1946",
            author_creator="Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="1938-1946; merged file created 2002",
            locator="Official unrestricted ASNEF.FIN.DAT; 17 protected candidates explicitly reviewed, including one conflict and one spelling-variant candidate",
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
            locator="PDF physical pages 44-46; identity, Army-entry-date, grade, and civilian-occupation fields",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records technical documentation",
            rights_notes="Used only to interpret selected fields; source damage and incomplete coverage remain visible.",
        ),
        source(
            CODES,
            stable_url="https://aad.archives.gov/aad/popup-codelist.jsp?cl_id=3323&dt=893&c_id=24986",
            archival_identifier="NARA AAD civilian occupation code list; Code No. 30 in NAID 1263923 documentation",
            title="World War II Army Enlistment Records: Civilian Occupation Code List",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives Access to Archival Databases",
            locator="Current AAD values for codes 031, 134, 157, 170, 175, 227, 316, 478, 583, 783, 839, 959, and 992; printed reference copy visually checked",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records code lists",
            rights_notes="Every published value was visually checked. Code 993 was not published because no sufficiently reliable definition was found in the reviewed list.",
        ),
        source(
            DET101,
            stable_url="https://www.javadc.org/java/docs/1945-03-15%20OSSSU%20Detachment%20101%20Promotions%20and%20Citations%20OCR%20P11_MA.pdf",
            archival_identifier="RG 226, Entry UD190, Stack 190, Row 9, Compartment 24, Shelf 6, Box 35, Folder 4; NND 877190",
            title="OSS Special Operations Detachment 101 Promotions and Citations",
            author_creator="Office of Strategic Services, Detachment 101 Promotion and Citation Board",
            repository_publisher="Japanese American Veterans Association digital document library",
            publication_record_date="1945-04-16 to 1945-04-25",
            locator="Promotion and Citation Board proceedings; Floyd E. Maves promotion list and roster context",
            source_quality="A_direct_official",
            collection_name="Records of the Office of Strategic Services, Record Group 226",
            rights_notes="Digitized official RG 226 document hosted by JAVA. Only project-authored notes and a short supporting excerpt are retained.",
        ),
    ]


def army_affiliation_key(row: int) -> str:
    return f"{slug(PEOPLE[row][1])}-army-association-b1046"


def army_identity_assessment(row: int) -> str:
    if row == 18:
        return "High confidence from exact official name agreement, the same nonshared protected linkage across both immutable index rows, and the matching Army entry; the identifier remains private."
    if row == 31:
        return "High confidence from exact official name and suffix agreement and a nonshared protected linkage; the protected identifier remains private."
    if row == 37:
        return "High confidence from a nonshared protected linkage and matching name fields; the Army entry's middle initial C remains a visible variant, and a separate officer row remains unmerged."
    if row == 24:
        return "Confirmed by the exact uncommon name, compatible rank progression, nonshared protected linkage, and the official Detachment 101 promotion record."
    return "High confidence from exact official name agreement and a nonshared protected linkage; the protected identifier remains private."


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, _label, relationship) in ARMY_ASSOCIATIONS.items():
        item: dict[str, object] = {
            "key": army_affiliation_key(row),
            "person_id": PEOPLE[row][0],
            "relationship_type": relationship,
            "end_date": date,
            "date_precision": f"Historical civilian-occupation code {code} was recorded at Army entry on {date}; no named employer, institution, workplace, or OSS-transfer date is supplied.",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "confirmed" if row == 24 else "high_confidence",
            "claim_confidence": "medium",
            "source_quality": "A_direct_official",
            "publication_status": "publish_qualified",
            "research_notes": "The broad historical category is excluded from verified-employer analytics and is not converted into a named organization.",
        }
        if relationship == "student":
            item["role_title"] = "student"
        else:
            item["occupation"] = occupation
        values.append(item)
    return values


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, label, relationship) in ARMY_ASSOCIATIONS.items():
        values.append(
            {
                "key": f"army-{slug(PEOPLE[row][1])}-b1046",
                "person_id": PEOPLE[row][0],
                "affiliation_key": army_affiliation_key(row),
                "claim_type": "other_pre_oss_affiliation" if relationship == "student" else "occupation",
                "claim_text": f"At Army entry on {date}, {PEOPLE[row][1]} was recorded as {occupation}; no employer, institution, or workplace is identified.",
                "evidence_paraphrase": f"The Army bulk file records code {code}; the visually checked official list defines the category as {label}.",
                "identity_match_assessment": army_identity_assessment(row),
                "temporal_assessment": "Strongly date-bounded to Army entry, but not proven to be the immediately preceding role or status before OSS.",
                "source_quality": "A_direct_official",
                "claim_confidence": "medium",
                "publication_status": "publish_qualified",
                "match_notes": "The historical category is qualified, excluded from verified-employer analytics, and not converted into a named organization.",
                "sources": [
                    {"source_key": INDEX},
                    {"source_key": ARMY},
                    {"source_key": TECH, "support_type": "context_only"},
                    {"source_key": CODES, "locator_override": f"Current AAD civilian occupation code {code}"},
                ],
            }
        )

    values.extend(
        [
            {
                "key": "identity-floyd-e-maves-detachment-101-b1046",
                "person_id": PEOPLE[24][0],
                "claim_type": "identity",
                "claim_text": "Indexed Sergeant Floyd E. Maves is confirmed as the Detachment 101 soldier promoted from corporal to sergeant in April 1945.",
                "evidence_paraphrase": "An official RG 226 promotion-board record prints the exact uncommon name and the corporal-to-sergeant promotion; the protected record bridge independently agrees.",
                "identity_match_assessment": "Confirmed by exact uncommon name agreement, compatible index rank, the official Detachment 101 context, and a nonshared protected Army linkage.",
                "temporal_assessment": "Wartime OSS identity and rank progression only; the document does not identify a pre-OSS employer or immediate predecessor affiliation.",
                "source_quality": "A_direct_official",
                "claim_confidence": "confirmed",
                "publication_status": "published",
                "match_notes": "The archival document's roster context is retained without publishing the protected identifier. The Army-entry occupation remains a separate qualified claim.",
                "sources": [
                    {"source_key": DET101, "excerpt_override": "Maves, Floyd E | Cpl | Sgt"},
                    {"source_key": INDEX, "support_type": "context_only"},
                    {"source_key": ARMY, "support_type": "context_only"},
                ],
            },
            {
                "key": "identity-joseph-p-mauro-two-rows-b1046",
                "person_id": PEOPLE[18][0],
                "claim_type": "identity",
                "claim_text": "Two printed Joseph P. Mauro index rows remain preserved and are cautiously linked to one person entity.",
                "evidence_paraphrase": "Both immutable index rows print the same name and protected identifier, while the Army entry independently agrees in full name and identifier.",
                "identity_match_assessment": "High confidence from the exact name and same nonshared protected identifier across both source rows and the official Army entry.",
                "temporal_assessment": "Identity-resolution evidence only; the differing ranks and boxes are preserved and do not establish employment chronology.",
                "source_quality": "A_direct_official",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "The two source rows are never deduplicated. No protected number appears in public data.",
                "sources": [
                    {"source_key": INDEX},
                    {"source_key": ARMY, "support_type": "context_only"},
                ],
            },
            {
                "key": "identity-erwin-mauss-protected-conflict-b1046",
                "person_id": PEOPLE[22][0],
                "claim_type": "identity",
                "claim_text": "Erwin Mauss remains unresolved because the protected index identifier points to an Army record for a materially different full name.",
                "evidence_paraphrase": "The private crosswalk connects the printed identifier to an Army entry for Stephen Z. Krzyzaniak; no fields are transferred between the names.",
                "identity_match_assessment": "Conflicting: the materially different names outweigh the shared protected identifier until the original jackets are compared.",
                "temporal_assessment": "No Army occupation or chronology is assigned to Erwin Mauss pending archival review.",
                "source_quality": "A_direct_official",
                "claim_confidence": "conflicting",
                "publication_status": "conflicting",
                "match_notes": "The conflict is visible without exposing the protected identifier or attaching another person's occupation.",
                "sources": [
                    {"source_key": INDEX},
                    {"source_key": ARMY, "support_type": "context_only"},
                ],
            },
            {
                "key": "identity-charles-maxwell-maxwelc-candidate-b1046",
                "person_id": PEOPLE[29][0],
                "claim_type": "identity",
                "claim_text": "A likely Army spelling variant for Charles Maxwell remains a private candidate pending file review.",
                "evidence_paraphrase": "The protected crosswalk points to MAXWELC CHARLES R, but the surname difference and added middle initial require confirmation in the original file.",
                "identity_match_assessment": "Probable but unconfirmed; no occupation or chronology is published from the candidate.",
                "temporal_assessment": "Candidate identity evidence only; the 1946 Army-entry date is not treated as pre-OSS chronology.",
                "source_quality": "A_direct_official",
                "claim_confidence": "low",
                "publication_status": "withheld_low_confidence",
                "match_notes": "The candidate remains in the review system and is excluded from public factual claims and analytics.",
                "sources": [
                    {"source_key": INDEX},
                    {"source_key": ARMY, "support_type": "context_only"},
                ],
            },
            {
                "key": "identity-georges-may-two-entities-b1046",
                "person_id": PEOPLE[36][0],
                "claim_type": "identity",
                "claim_text": "The two Georges May rows remain separate because the officer and enlisted records have different protected identifiers.",
                "evidence_paraphrase": "Page 301 prints a second lieutenant and a private first class as separate rows; only the enlisted identifier has an accepted Army bridge.",
                "identity_match_assessment": "Ambiguous same-name case: rank and protected-identifier differences require separate entities pending review of both Box 493 files.",
                "temporal_assessment": "Identity-resolution evidence only; the enlisted occupation is not transferred to the officer.",
                "source_quality": "A_direct_official",
                "claim_confidence": "conflicting",
                "publication_status": "conflicting",
                "match_notes": "Both source rows and both person entities remain visible; no silent merge was made.",
                "sources": [
                    {"source_key": INDEX},
                    {"source_key": ARMY, "support_type": "context_only"},
                ],
            },
        ]
    )
    return values


def base_update(row: int) -> dict[str, object]:
    person_id, name, box = PEOPLE[row]
    return {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified page 301 source preserves {name}, Box {box}, rank or grade when printed, notes when present, and archive location. Prior Library of Congress searching plus staged official, exact-name, occupation, obituary, institutional, directory, and archival discovery did not establish a defensible identity-and-affiliation bridge.",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": f"Review indexed Box {box} for corroborating identifiers, immediate pre-OSS affiliation, and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }


def person_updates() -> list[dict[str, object]]:
    by_row = {row: base_update(row) for row in PEOPLE}

    for row in ARMY_ASSOCIATIONS:
        by_row[row].update(
            identity_status="confirmed" if row == 24 else "high_confidence",
            identity_evidence=army_identity_assessment(row),
            personnel_category="enlisted_army_personnel",
            commissioned_officer=False,
            allied_or_foreign_personnel=False,
            nara_catalog_id="1263923",
            research_status="occupation_only_found",
            next_action=f"Review Box {PEOPLE[row][2]} to identify a named employer or institution and establish Army-to-OSS chronology. The protected Army link supplies only a broad historical occupation or student-status category.",
            archival_review_priority="medium" if row == 24 else "high",
        )

    by_row[18].update(
        identity_status="high_confidence",
        identity_evidence=army_identity_assessment(18),
        possible_duplicate_group="page301-joseph-p-mauro-two-source-rows",
        archival_review_priority="critical",
    )
    by_row[22].update(
        identity_status="conflicting",
        identity_evidence="The protected identifier printed for indexed Erwin Mauss points to an Army bulk entry for Stephen Z. Krzyzaniak. The materially different full names create an identifier conflict and are not merged.",
        research_status="conflicting_sources",
        next_action="Inspect Box 492 and both original records to determine which person owns the repeated protected identifier. No Army occupation is transferred to Erwin Mauss.",
        archival_review_priority="critical",
    )
    by_row[23].update(
        identity_status="high_confidence",
        identity_evidence="The index and official Army bulk entry agree in full name and a nonshared protected identifier. Occupation code 993 remains unpublished because its meaning was not established reliably in the reviewed code list.",
        personnel_category="enlisted_army_personnel",
        commissioned_officer=False,
        allied_or_foreign_personnel=False,
        nara_catalog_id="1263923",
        next_action="Review Box 492 and the underlying Army record to identify Joseph P. Mautner's pre-service occupation or status and immediate pre-OSS affiliation. Code 993 is not interpreted without a reliable definition.",
        archival_review_priority="high",
    )
    by_row[24].update(
        name_variants=["Floyd E. Maves"],
        replace_name_variants=False,
    )
    by_row[29].update(
        identity_status="probable",
        identity_evidence="A nonshared protected identifier links indexed Charles Maxwell to an Army bulk name printed MAXWELC CHARLES R. The likely surname transcription error and added middle initial require file confirmation.",
        research_status="needs_identity_review",
        next_action="Inspect Box 493 and the original jacket to confirm the Army bulk surname spelling and middle initial before relying on this identity crosswalk. No candidate occupation is published.",
        archival_review_priority="critical",
    )
    by_row[36].update(
        identity_status="ambiguous",
        identity_evidence="Page 301 prints a second Georges May as a second lieutenant with a protected identifier different from the enlisted Georges May row. The officer remains a separate same-name entity pending file review.",
        possible_duplicate_group="page301-georges-may-two-entities",
        research_status="needs_identity_review",
        next_action="Compare both Box 493 files to confirm that the officer and enlisted rows are distinct namesakes. Do not transfer the enlisted Army occupation to the officer.",
        archival_review_priority="critical",
    )
    by_row[37].update(
        name_variants=["Georges C May"],
        replace_name_variants=False,
        possible_duplicate_group="page301-georges-may-two-entities",
        next_action="Review both Box 493 Georges May files to confirm separation and identify the enlisted person's school or other named employer. The Army record supplies only a secondary-school teacher or principal category.",
        archival_review_priority="critical",
    )

    result = [by_row[row] for row in PEOPLE]
    if len(result) != 45:
        raise RuntimeError(f"Expected 45 person updates, generated {len(result)}")
    return result


def outcome_note(row: int) -> str:
    notes = {
        9: "An official Rhode Island survey and a Yale finding-aid hit for people named Frank Mauran Jr. lacked an OSS bridge and were rejected rather than attached to this row.",
        18: "Two immutable Joseph P. Mauro rows are linked cautiously through the same protected identifier; both rows and their differing ranks and boxes remain recoverable.",
        22: "The protected identifier conflict with Stephen Z. Krzyzaniak remains visible; no Army fields were transferred to Erwin Mauss.",
        24: "An official RG 226 Detachment 101 promotion record confirms Floyd E. Maves's wartime identity and rank progression, but not his pre-OSS employer.",
        29: "The MAXWELC CHARLES R candidate remains probable and private; no occupation or chronology is published pending Box 493 review.",
        36: "The officer remains separate from the enlisted Georges C. May because their ranks and protected identifiers differ.",
        37: "The enlisted Georges May has an accepted Army bridge adding middle initial C; the separate officer row remains unmerged.",
        42: "A postwar Nebraska optometry-license result for Jacques G. May lacked a wartime identity bridge and was rejected.",
        45: "Commercial genealogy and directory namesakes for Lester H. May lacked an OSS bridge and were rejected.",
    }
    return notes.get(row, "Unbridged namesakes, snippets, commercial people-finder pages, unsourced genealogy, relatives, and postwar-only leads did not establish a reliable identity or pre-OSS affiliation.")


def research_attempts() -> list[dict[str, object]]:
    updates = {item["person_id"]: item for item in person_updates()}
    substantiated = set(ARMY_ASSOCIATIONS) | {23}
    values: list[dict[str, object]] = []
    for row, (person_id, name, box) in PEOPLE.items():
        if row in {22, 29, 36}:
            outcome = "candidate_rejected"
        elif row in substantiated:
            outcome = "source_reviewed"
        else:
            outcome = "no_result"
        values.append(
            {
                "key": f"page301-row{row}-{slug(name)}-b1046",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index context; exact-name and meaningful initial, suffix, punctuation, spelling and OCR variants; public CIA Reading Room discovery and equivalent official-source context; rank, branch, nationality, assignment and protected-identifier clues; employer and occupation 1940; obituary, biography, institutional, Library of Congress newspaper, directory and archival searches; indexed Box {box}",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_1046",
                "started_at": "2026-11-05T16:40:00-05:00",
                "completed_at": "2026-11-05T20:05:00-05:00",
                "outcome": outcome,
                "sources_reviewed": 7 if row == 24 else 6 if row in substantiated or row in {22, 29, 36} else 5,
                "candidate_sources_rejected": 4 if row in {9, 22, 29, 36, 42, 45} else 3,
                "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, education treated as employment, relatives, and postwar-only leads were rejected. Army categories were not converted into named employers. Protected conflicts and spelling variants remain visible.",
                "research_notes": f"{outcome_note(row)} The official index, prior Library of Congress search, exact-name OSS discovery, public CIA Reading Room discovery, Army and NARA materials, occupation and employer searches, and institutional, obituary, directory, military-history, and archival sources were reviewed as applicable. Direct CIA adapter access failed closed under robots policy and was not treated as a negative biographical result. No authenticated NARA Catalog API request was made.",
                "next_action": str(updates[person_id]["next_action"]),
                "attempt_number": 4 if row == 3 else 3,
                "research_agent_version": "before-oss-b1046-v1",
            }
        )
    if len(values) != 45:
        raise RuntimeError(f"Expected 45 research attempts, generated {len(values)}")
    return values


def main() -> None:
    bundle = {
        "bundle_version": "batch-1046-v1",
        "reviewer": "Before OSS Batch 1046 evidence review",
        "sources": sources(),
        "organizations": [],
        "affiliations": affiliations(),
        "claims": claims(),
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }
    EvidenceBundle.model_validate(bundle)
    OUTPUT.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
