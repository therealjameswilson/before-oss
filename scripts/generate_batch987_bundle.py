#!/usr/bin/env python3
"""Generate the reviewed Batch 987 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page484-domonic-virdo-to-floyd-tomas-vlasic-"
    "review_batch-987_2026-10-30.json"
)

INDEX = "nara-index-b987"
ARMY = "army-bulk-b987"
TECH = "army-tech-b987"
CODES = "army-codes-b987"
HOOVER_VISINI = "hoover-visini-b987"
GAZETTE_1940 = "london-gazette-vivian-1940-b987"
GAZETTE_1947 = "london-gazette-vivian-1947-b987"

ORG_BRITISH_ARMY = "british-army-b987"

VISINI_DUPLICATE_GROUP = "page484-anthony-antonio-visini-b987"
VIVEQUIN_DUPLICATE_GROUP = "page484-emile-vivequin-viviquin-b987"


PEOPLE = {
    1: ("c986edb4-91c5-53df-aa84-a04979f76455", "Domonic Virdo"),
    2: ("5a5ebcb8-87d3-5419-8da4-e205e973af8a", "Robert Viret"),
    3: ("832da0f2-62c5-52f4-ad61-2c2bf0e6f873", "Russell E Virgils"),
    4: ("fe075865-c28d-5ac1-bb0a-f940d75c5d3e", "Anthony Visini"),
    5: ("473f8b49-bf87-5cf5-b4ff-d92ff3fc6e4f", "Antonio Visini"),
    6: ("256326f1-90d9-578a-939a-a56eda91e1e0", "C R Vislocky"),
    7: ("f8cab5da-5946-5c38-9da1-1666fdd03e42", "Theodore Visser"),
    8: ("b4622aeb-4202-531e-8793-8dadd714cba3", "William G Visser"),
    9: ("a2cfec37-7bba-5459-ba97-0505bae9aa8d", "Steve Vitak Jr."),
    10: ("89a44246-6c0f-5d8f-9fc3-e28d254d4d1b", "Charles J Vitale"),
    11: ("9b76b69f-fc08-5c07-acea-22eb719b6b64", "Samuel Vitale"),
    12: ("f9a41038-73a4-58de-b790-244e10a28354", "Domenick P Viterisi"),
    13: ("abb41258-4f42-5160-bc07-58eda7573820", "Philip B Vito"),
    14: ("6e1925d1-7da1-5f7d-9fd8-3604d9577331", "Angelo Vitti"),
    15: ("b451a6c1-53c5-5e02-8f48-6ed0ca6f3803", "Aniceto Vitti"),
    16: ("bac268dd-0fce-5194-973b-0cf0b5909894", "Emile Vivequin"),
    17: ("ad5f4b1c-11ea-5da7-9665-c044e9fc75fa", "Neal B Vivian"),
    18: ("d083cf01-0633-5619-a6bc-13aa1c97805e", "Valentine P.T. Viviani"),
    19: ("7e952688-bb4b-514b-8718-5af15091729d", "William F Viviani"),
    20: ("6cef9a04-a514-502e-a9a2-c59defaa7c09", "Emile Viviquin"),
    21: ("effb65bc-b499-5652-8262-98f9eacce1cc", "Peter L Vlahakes"),
    22: ("9fa853a2-a40f-58ff-bed4-4576bd9dedb9", "Steve P Vlahovich"),
    23: ("e6d791d1-e3ef-5232-a6e9-9a96daa89bef", "Floyd Tomas Vlasic"),
}


ARMY_FINDINGS = {
    1: {
        "date": "1942-08-20",
        "code": "678",
        "occupation": "Machine shop and related occupations, n.e.c.",
        "public_occupation": "machine-shop or related occupation, not elsewhere classified",
        "relationship": "employment",
    },
    5: {
        "date": "1943-08-06",
        "code": "497",
        "occupation": "Electricians",
        "public_occupation": "electrician",
        "relationship": "employment",
    },
    11: {
        "date": "1942-05-20",
        "code": "736",
        "occupation": "Chauffeurs and drivers, bus, taxi, truck, and tractor",
        "public_occupation": "chauffeur or driver of a bus, taxi, truck, or tractor",
        "relationship": "employment",
    },
    12: {
        "date": "1945-08-13",
        "code": "992",
        "occupation": "Students",
        "public_occupation": "student",
        "relationship": "student",
    },
    15: {
        "date": "1942-11-11",
        "code": "316",
        "occupation": "Farm hands, general farms",
        "public_occupation": "general farm hand",
        "relationship": "employment",
    },
}


UNRESOLVED = {
    2: "The index note 'French' supplies nationality context, but exact-name French, OSS, occupation, obituary and archival searches produced multiple namesakes and no Box 805 bridge.",
    3: "A same-name veteran-burial lead records Army Air Corps service, but no protected identifier, OSS assignment, personnel-file link or employer connects it to the indexed person.",
    6: "The initials-only entry is not safely distinguishable from namesakes; exact-initial, surname, OSS, employer and archival searches produced no corroborating identifier.",
    7: "Exact-name, serial, Army, OSS, occupation, obituary and archival searches produced no reliable identity or employer bridge.",
    8: "The printed rank and truncated note 'Netherla' support an Allied-service research lead, but no exact unit, biographical bridge or pre-OSS employer was established.",
    9: "Exact-name, suffix, serial, Army, OSS, occupation, obituary and archival searches produced no reliable identity or employer bridge.",
    10: "The common name generated several unbridged candidates; none supplied the middle initial, Box 806 context, OSS assignment or a defensible pre-OSS chronology.",
    13: "Exact-name, middle-initial, military, OSS, occupation, obituary and archival searches supplied no reliable identity or pre-OSS affiliation bridge.",
    14: "Numerous same-name candidates could not be connected to Box 806, an OSS assignment, military identifier or pre-OSS chronology.",
    16: "Veteran-grave and military leads for Emile Vivequin do not establish the Box 806 identity or prove whether this row duplicates the separately printed Viviquin row.",
    17: "Exact-name, middle-initial, serial, Army, OSS, occupation and obituary searches supplied no reliable identity or employer bridge.",
    19: "A specialist mission roster contains a 1st Lt. W. F. Viviani lead, but it does not establish the full identity, protected identifier or any pre-OSS employer.",
    20: "Searches on the printed Viviquin spelling point back to the index; the adjacent Vivequin row is a possible variant, but name similarity alone cannot establish duplication.",
    21: "An official 1943 service-journal list contains Peter L. Vlahakes, but it does not provide an OSS or Box 806 bridge, occupation or pre-OSS employer.",
    22: "A District of Columbia war memorial contains the exact name, but it supplies no OSS assignment, employer or identifiers sufficient to connect the indexed person.",
    23: "Exact-name, identifier, spelling-variant, military, OSS, occupation, obituary and archival searches supplied no reliable identity or pre-OSS affiliation bridge.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 805-806",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 484, rows 1-23; checked against layout-preserving text and an original-detail page render",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. The page render prints Domonic Virdo; Dominic G Virdo is retained only as an Army-supported variant.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; five protected-identifier comparisons; identifiers and record ordinals withheld",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "The restored local source was verified at 837,221,112 bytes and SHA-256 db10dbf90f0ef95dc327b0e8f8f0489923941b65399cf79bba71ac4b45d07e5b. No raw bulk row, record ordinal or full protected identifier enters public assets.",
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
            "locator": "PDF physical pages 172, 174 and amended page 304; codes 316, 497, 678, 736 and 992 visually checked",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical categories identify broad occupation or student status, not a named employer, workplace or exact job title.",
        },
        {
            "key": HOOVER_VISINI,
            "stable_url": "https://digitalcollections.hoover.org/objects/73269/oss-board-of-officers-report-on-arrival-at-naples",
            "archival_identifier": "Hoover ID 69085.145; object 73269",
            "title": "OSS board of officers report on arrival at Naples",
            "author_creator": "United States. Office of Strategic Services; collected by Millard Preston Goodfellow",
            "repository_publisher": "Hoover Institution Library & Archives",
            "publication_record_date": "1944-05-03",
            "locator": "77-page digital copy, PDF physical page 70, printed page 72; Cpl. Anthony Visini entry",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "Millard Preston Goodfellow papers, declassified U.S. government records",
            "document_number": "69085.145",
            "rights_notes": "The item page states on-site viewing restrictions. The project stores no downloaded copy or verbatim excerpt, only citation metadata and a concise project-authored paraphrase.",
        },
        {
            "key": GAZETTE_1940,
            "stable_url": "https://www.thegazette.co.uk/London/issue/34789/supplement/848/data.pdf",
            "archival_identifier": "London Gazette issue 34789, supplement page 848",
            "title": "Supplement to the London Gazette, 13 February 1940",
            "author_creator": "The War Office",
            "repository_publisher": "The Gazette, United Kingdom",
            "publication_record_date": "1940-02-13",
            "locator": "Page 848; substituted notification for 3 September 1939 commission, Valentine Patrick Terrel Vivian",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "The London Gazette",
        },
        {
            "key": GAZETTE_1947,
            "stable_url": "https://www.thegazette.co.uk/London/issue/37909/supplement/1312/data.pdf",
            "archival_identifier": "London Gazette issue 37909, supplement page 1312",
            "title": "Supplement to the London Gazette, 20 March 1947",
            "author_creator": "The War Office",
            "repository_publisher": "The Gazette, United Kingdom",
            "publication_record_date": "1947-03-20",
            "locator": "Page 1312; temporary Lieutenant-Colonel Valentine Patrick Terrel Vivian, General List",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "The London Gazette",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": ORG_BRITISH_ARMY,
            "organization_id": "865faf71-f9b5-558b-97a3-0b9d4332d29d",
            "canonical_name": "British Army",
            "historical_name": "British Army",
            "aliases": ["Indian Army Reserve of Officers", "General List"],
            "organization_type": "national army",
            "sector": "military",
            "country": "United Kingdom",
            "normalization_notes": "Existing canonical organization reused. Indian Army Reserve of Officers and General List wording remains on the affiliation; no Secret Intelligence Service assignment is inferred from the Gazette notices.",
        }
    ]


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, item in ARMY_FINDINGS.items():
        name = PEOPLE[row][1]
        values.append(
            {
                "key": f"{slug(name)}-army-category-b987-row{row}",
                "person_id": PEOPLE[row][0],
                "occupation": item["public_occupation"],
                "relationship_type": item["relationship"],
                "end_date": item["date"],
                "date_precision": "Historical civilian-occupation category recorded at Army entry; employer, workplace and duration are not supplied",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "A_direct_official",
                "publication_status": "publish_qualified",
                "research_notes": "Official historical category only; excluded from verified-employer analytics and not narrowed beyond the code-list wording.",
            }
        )
    values.append(
        {
            "key": "valentine-vivian-british-army-b987",
            "person_id": PEOPLE[18][0],
            "organization_key": ORG_BRITISH_ARMY,
            "organization_name_as_found": "Indian Army Reserve of Officers; later General List",
            "role_title": "major; later temporary lieutenant-colonel",
            "relationship_type": "military_assignment",
            "start_date": "1939-09-03",
            "date_precision": "The Gazette records a commission effective 3 September 1939 and a temporary lieutenant-colonel listing in 1947; it does not establish continuous service or the exact relation to the OSS-index file",
            "country": "United Kingdom",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "probable",
            "claim_confidence": "medium",
            "source_quality": "A_direct_official",
            "publication_status": "publish_qualified",
            "research_notes": "Qualified military-affiliation lead. The index spelling Viviani is preserved; Vivian is a documented variant candidate. No SIS role or immediate OSS transfer is inferred.",
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


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, item in ARMY_FINDINGS.items():
        name = PEOPLE[row][1]
        identity_note = (
            "A nonshared protected identifier directly links the printed row to the official Army record; the rare Domonic/Dominic spelling difference and added middle initial remain visible."
            if row == 1
            else "The exact official name and a nonshared protected identifier directly link the printed row to the reviewed Army record."
        )
        values.append(
            claim(
                row,
                f"identity-{slug(name)}-army-b987-row{row}",
                "identity",
                f"Indexed {name} is high-confidence matched to the official Army entry reviewed for Batch 987.",
                identity_note,
                "High confidence from a nonshared protected identifier; the protected value and raw bulk record are withheld.",
                "The dated Army entry precedes the later OSS-index context; the personnel file remains necessary to document the transfer sequence.",
                "A_direct_official",
                "high",
                [
                    {"source_key": INDEX},
                    {"source_key": ARMY, "locator_override": "Accepted identity bridge; protected identifier and raw record withheld"},
                ],
                "The identity bridge does not by itself establish an employer or immediate pre-OSS affiliation.",
            )
        )
        values.append(
            claim(
                row,
                f"occupation-{slug(name)}-b987-row{row}",
                "other_pre_oss_affiliation" if item["relationship"] == "student" else "occupation",
                f"At Army entry on {item['date']}, {name}'s historical civilian category was {str(item['occupation']).lower()}.",
                f"The official Army field carries historical code {item['code']}; NARA's code list defines it as {item['occupation']}.",
                "High confidence from the reviewed official identity bridge.",
                "Dated at Army entry before the later OSS-index context; no named employer, workplace, duration or exact OSS-transfer date is supplied.",
                "A_direct_official",
                "medium",
                [
                    {"source_key": ARMY, "locator_override": "Reviewed Army entry; raw record and identifier withheld"},
                    {"source_key": TECH, "locator_override": "PDF physical pages 44-46; civilian-occupation field"},
                    {"source_key": CODES, "locator_override": f"Historical code {item['code']}; visually reviewed code-list page"},
                ],
                "Published as a qualified historical category only; excluded from verified-employer analytics.",
                f"{slug(name)}-army-category-b987-row{row}",
                "publish_qualified",
            )
        )

    values.extend(
        [
            claim(
                4,
                "identity-anthony-visini-hoover-b987",
                "identity",
                "Indexed Anthony Visini is probably the corporal named in a 1944 OSS personnel survey in Italy.",
                "The direct OSS report names Cpl. Anthony Visini, records an Army-entry date matching the adjacent Antonio Visini Army record, and describes OSS training and installation duties.",
                "Probable from the exact rare name and direct OSS context, but the index row has no printed identifier and may duplicate the separately preserved Antonio row.",
                "The report documents OSS-period duties, not a pre-OSS employer; the personnel file is required to resolve the two index rows.",
                "A_direct_official",
                "medium",
                [{"source_key": INDEX}, {"source_key": HOOVER_VISINI}],
                "No wartime OSS duty is converted into a pre-OSS employer. The Anthony and Antonio rows remain separate and visibly grouped for duplicate review.",
                publication_status="publish_qualified",
            ),
            claim(
                18,
                "identity-valentine-viviani-vivian-b987",
                "identity",
                "Indexed Colonel Valentine P.T. Viviani is probably the British officer Valentine Patrick Terrel Vivian.",
                "The rare given name and initials, colonel-level rank and British Army note align with official Gazette notices for Valentine Patrick Terrel Vivian.",
                "Probable rather than high confidence because the surname differs by a final i and neither Gazette notice names OSS or Box 806.",
                "The 1939 notice establishes a prewar British military commission; the exact relation to the OSS-index file remains unresolved.",
                "A_direct_official",
                "medium",
                [{"source_key": INDEX}, {"source_key": GAZETTE_1940}, {"source_key": GAZETTE_1947}],
                "The original Viviani spelling is preserved. No Secret Intelligence Service role is inferred from these notices.",
                publication_status="publish_qualified",
            ),
            claim(
                18,
                "other-pre-oss-valentine-vivian-british-army-b987",
                "other_pre_oss_affiliation",
                "The probable Valentine Patrick Terrel Vivian match held a British Army commission effective 3 September 1939 and later appeared as a temporary lieutenant-colonel on the General List.",
                "The 1940 Gazette identifies him as a major, late Indian Army Reserve of Officers, commissioned without pay and allowances; the 1947 Gazette lists him as a temporary lieutenant-colonel, General List.",
                "Probable identity from the rare full name reconstructed from initials, rank and British Army note.",
                "The 1939 commission is definitely pre-OSS; continuity and immediate predecessor status are not established.",
                "A_direct_official",
                "medium",
                [{"source_key": GAZETTE_1940}, {"source_key": GAZETTE_1947}],
                "Military assignment, not civilian employment; excluded from verified-employer analytics.",
                "valentine-vivian-british-army-b987",
                "publish_qualified",
            ),
        ]
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
    values: list[dict[str, object]] = []
    for row, reason in UNRESOLVED.items():
        category = "unknown_or_indeterminate"
        commissioned = None
        allied = False
        if row == 2:
            allied = True
        elif row == 8:
            category = "foreign_or_allied_military_personnel"
            commissioned = False
            allied = True
        elif row == 19:
            category = "commissioned_army_officer"
            commissioned = True
        duplicate = VIVEQUIN_DUPLICATE_GROUP if row in {16, 20} else None
        values.append(
            base_update(
                row,
                identity_status="ambiguous" if row in {16, 20} else "unresolved",
                identity_evidence=f"The visually verified page 484 row preserves {PEOPLE[row][1]} and its indexed Box 805 or 806 context. {reason}",
                personnel_category=category,
                commissioned_officer=commissioned,
                allied_or_foreign_personnel=allied,
                possible_duplicate_group=duplicate,
                research_status="requires_archival_review",
                next_action=f"Review the indexed personnel file for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}",
                archival_review_priority="critical" if row in {16, 20} else "high",
            )
        )

    for row, item in ARMY_FINDINGS.items():
        variants = ["Dominic G Virdo"] if row == 1 else None
        evidence = (
            "A nonshared protected identifier connects the printed Domonic Virdo row to the official Army record for Dominic G Virdo. The printed spelling remains unchanged and the Army form is retained as a variant."
            if row == 1
            else "The exact official name and a nonshared protected-identifier agreement support the Army identity match; the protected value remains private."
        )
        values.append(
            base_update(
                row,
                identity_status="high_confidence",
                identity_evidence=evidence,
                name_variants=variants,
                personnel_category="enlisted_army_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                possible_duplicate_group=VISINI_DUPLICATE_GROUP if row == 5 else None,
                research_status="occupation_only_found",
                next_action=f"Review the indexed personnel file to identify any named employer behind historical code {item['code']} and establish the Army-to-OSS chronology. The code supplies only a broad occupation or student category.",
                nara_catalog_id="1263923",
            )
        )

    values.extend(
        [
            base_update(
                4,
                identity_status="probable",
                identity_evidence="A direct 1944 OSS survey names Cpl. Anthony Visini and records an Army-entry date matching the adjacent Antonio Visini Army record. The Anthony index row lacks a printed identifier, so the rows remain separate pending Box 805 review.",
                personnel_category="enlisted_army_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                possible_duplicate_group=VISINI_DUPLICATE_GROUP,
                research_status="requires_archival_review",
                next_action="Review both Box 805 Visini files together to determine whether Anthony and Antonio are name variants for one person and to identify any civilian employer before Army or OSS service.",
                archival_review_priority="critical",
            ),
            base_update(
                18,
                identity_status="probable",
                identity_evidence="The rare given name and initials, colonel-level rank and British Army note align with official Gazette notices for Valentine Patrick Terrel Vivian; the surname difference and absent Box 806 bridge prevent a high-confidence match.",
                name_variants=["Valentine Patrick Terrel Vivian"],
                personnel_category="foreign_or_allied_military_personnel",
                commissioned_officer=True,
                allied_or_foreign_personnel=True,
                research_status="requires_archival_review",
                next_action="Review Box 806 to confirm the Viviani/Vivian spelling bridge, the person's exact Allied relationship to OSS, and any civilian affiliation before British military service.",
                archival_review_priority="critical",
            ),
        ]
    )
    return values


def research_attempts() -> list[dict[str, object]]:
    sourced = set(ARMY_FINDINGS) | {4, 18}
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        if row in sourced:
            outcome = "source_reviewed"
            sources_reviewed = 7 if row in {4, 18} else 6
            rejected = 4
            detail = "Reviewed official index, Army, institutional or government sources produced the identity, historical occupation, student-status, duplicate-review or British military-affiliation outcome recorded in the bundle."
        else:
            outcome = "no_result"
            sources_reviewed = 5
            rejected = 5
            detail = UNRESOLVED[row]
        attempts.append(
            {
                "key": f"page484-row{row}-{slug(name)}-b987",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index context; CIA Reading Room or equivalent official-source check; exact-name and meaningful variants; OSS, rank, branch, identifier and assignment clues; employer and occupation 1940; obituary, institutional, newspaper, directory and archival searches; indexed Box 805 or 806; protected identifiers used only in private official-record comparison",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_987",
                "started_at": "2026-10-30T13:50:00Z",
                "completed_at": "2026-10-30T14:48:00Z",
                "outcome": outcome,
                "sources_reviewed": sources_reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, snippets, commercial people-finder pages, relatives, unsourced genealogy, postwar-only leads and sources without an OSS, protected-identifier, rank, unit or personnel-file bridge were rejected. Historical occupation categories, student status, military assignments and OSS-period duties were not converted into employers.",
                "research_notes": f"{detail} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain and archival searches were checked as applicable. The NARA index page and official Army code-list pages were inspected directly. The Hoover item was used only through its stable institutional record and a concise paraphrase; no restricted file was retained or republished. No search-result snippet was used as sole final evidence, no paywall or access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": "Review the indexed personnel file for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before wartime service.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b987-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-987-v1",
        "reviewer": "Before OSS Batch 987 evidence review",
        "sources": sources(),
        "organizations": organizations(),
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
