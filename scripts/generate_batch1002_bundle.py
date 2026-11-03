#!/usr/bin/env python3
"""Generate the reviewed Batch 1002 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page492-waters-to-watters-"
    "review_batch-1002_2026-11-03.json"
)

INDEX = "nara-index-b1002"
ARMY = "army-bulk-b1002"
TECH = "army-tech-b1002"
CODES = "army-codes-b1002"
CONGRESS = "congressional-record-armitage-watkins-b1002"
COLUMBIA = "columbia-armitage-watkins-b1002"
ORG_OWI = "office-war-information-b1002"


PEOPLE = {
    1: ("f8df6b7e-af94-5c45-978f-ada828df39e5", "Donald O Waters"),
    2: ("9a74397d-2341-5bcf-91d2-201d42927823", "Freeman Waters"),
    3: ("97d07707-aee0-522e-8033-6bd6d46fe267", "John R Waters"),
    4: ("666bafff-6b58-5301-b0a9-21b399578c13", "Lee W Waters"),
    5: ("9c35ecd1-a1b0-5ea8-aec2-a80d48214d1b", "Louise V Waters"),
    6: ("38ae5342-7ef4-57d7-b904-1f143d37c273", "Martin J Waters Jr."),
    7: ("8d427d07-8902-57dd-bbd0-632afc4e9dcb", "William J Waters"),
    8: ("60b2620c-5001-55af-8dbc-005ad86bdce1", "John J Wathey"),
    9: ("dfd06350-8ca2-5188-909d-6913e7c43ea1", "Agnes M Wathley"),
    10: ("d433152f-6f0b-50af-a9da-f0032526ec4b", "Ann Watkins"),
    11: ("c8800e05-3bf6-561d-ba74-377a56e4b00e", "Armitage Watkins"),
    12: ("fe8d97f1-79ec-5c69-93eb-1dd8faeb673b", "Arthur W Watkins"),
    13: ("0eed28b7-cb28-5aa8-8a91-f8f644689e5e", "Caryl J Watkins"),
    14: ("6b615233-75aa-5b02-8c54-b98e6530ef7b", "Charles R Watkins"),
    15: ("2811a6e9-abc3-58fb-ae3c-9719b4ab3b92", "Elizabeth L Watkins"),
    16: ("fcbc3bb1-285e-5b1a-bafa-ec8d035ba34d", "Ervine C Watkins"),
    17: ("2f061908-5ea8-5ef8-8088-18d9e93ffecd", "Fitch Watkins"),
    18: ("3d4c6a52-a771-5ecb-a408-fc20a473d7fc", "Frederick M Watkins"),
    19: ("01aa76df-a5f9-538c-b6fa-5a18aaecb692", "George E Watkins"),
    20: ("10238e5a-1e22-5c9d-b686-41f1c535b1d7", "George L Watkins"),
    21: ("765c1a83-c5e6-5f3c-b441-367f5fe7f6fc", "Gladys M Watkins"),
    22: ("615ed00a-a4af-501c-812f-e45747d99033", "Thomas H Watkins"),
    23: ("1d9badfa-9791-57de-a7f1-769b472a57d3", "William H Watkins"),
    24: ("1b35027b-8402-5142-941e-0c10d412c680", "Allyn R Watson"),
    25: ("bddef72e-36a0-53e1-aa57-4c4df4542871", "Eldon D Watson"),
    26: ("eb26f905-3ac1-562f-b6df-d3b617b95212", "Fred S Watson Jr."),
    27: ("78717d07-eb68-59e7-97cc-77212c315841", "George W Watson"),
    28: ("fe23b5c2-4712-5698-902f-29e24c1d2779", "George L Watson"),
    29: ("3af47aef-c75e-5715-96d3-4dea77fc01da", "George H Watson"),
    30: ("343fe3d3-84f2-5fbf-8bfe-12f83b795d2a", "Henry P Watson"),
    31: ("28b7e7bc-199d-5e84-bbe9-279640218279", "Hermine G Watson"),
    32: ("9483b242-0e98-58dc-9c80-b5fbbea61e03", "John T Watson"),
    33: ("38165f9e-2618-5a47-9210-72e51e484ebb", "Lee V Watson"),
    34: ("dd31dd6e-f2bb-553d-9bdb-d25b870b791f", "Mary A Watson"),
    35: ("696bde5d-8ca8-5d32-93f4-37a8fac0275d", "Mary S Watson"),
    36: ("f289cd20-68bf-51b2-98d0-ed9d86b5573c", "Minerva Louis Watson"),
    37: ("1f801a64-198c-5626-a9a1-11232a926f1c", "Minnie L Watson"),
    38: ("4dda1e45-8d25-52b1-b1f6-170809e98986", "Oscar L Watson"),
    39: ("01b2c3e2-a0f3-569f-951b-87c0f773c550", "Tom J Watson"),
    40: ("a8951ad7-b713-530a-addd-982a01302364", "William K Watson"),
    41: ("c193282a-c021-59d2-a48b-e6f14e484b9c", "Richard F Watt"),
    42: ("37bf5363-2d97-5d28-b725-e64aa3015e0e", "Edwin E Watte"),
    43: ("7f5ae83b-05f3-5636-810a-d3ee71103f6c", "Frederick Watteins"),
    44: ("3f2b3006-da89-526d-86c7-ca41b1b6c36b", "Joseph A Wattenhofer"),
    45: ("c8e51e6a-ee01-5f04-afd7-37705450a087", "Katharine Watters"),
    46: ("8a956e47-3a04-5155-9267-9ba42647c5c3", "Lee J Watters"),
}


ARMY_MATCHES = {
    1: {
        "date": "1943-03-29", "code": "295", "occupation": "elevator operator",
        "label": "Elevator operators", "locator": "PDF physical page 172; historical category 2-95",
    },
    3: {
        "date": "1943-06-24", "code": "992", "occupation": "student",
        "label": "Students", "locator": "PDF physical page 304; amended historical category 9-92",
    },
    8: {
        "date": "1943-08-12", "code": "126", "occupation": "paymaster, payroll clerk, or timekeeper",
        "label": "Paymasters, payroll clerks, and timekeepers", "locator": "PDF physical page 171; historical category 1-26",
    },
    12: {
        "date": "1942-06-24", "code": "602", "occupation": "semiskilled bakery-products production worker",
        "label": "Occupations in production of bakery products, n. e. c.", "locator": "PDF physical page 173; historical category 6-02",
    },
    13: {
        "date": "1943-06-18", "code": "073", "occupation": "wholesale manager",
        "label": "Wholesale managers", "locator": "PDF physical page 171; historical category 0-73",
    },
    17: {
        "date": "1941-11-13", "code": "736", "occupation": "chauffeur or driver",
        "label": "Chauffeurs and drivers, bus, taxi, truck, and tractor", "locator": "PDF physical page 174; historical category 7-36",
    },
    24: {
        "date": "1943-02-13", "code": "992", "occupation": "student",
        "label": "Students", "locator": "PDF physical page 304; amended historical category 9-92",
    },
    25: {
        "date": "1941-03-07", "code": "525", "occupation": "carpenter",
        "label": "Carpenters", "locator": "PDF physical page 174; historical category 5-25",
    },
    38: {
        "date": "1940-11-07", "code": "999", "occupation": None,
        "label": None, "locator": "Historical code 999; no publishable civilian occupation decoded",
    },
    46: {
        "date": "1942-12-09", "code": "799", "occupation": "apprentice to another trade",
        "label": "Apprentices to other trades", "locator": "PDF physical page 175; historical category 7-99",
    },
}


PRINTED_OFFICERS = {6, 30, 41, 42}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def box_for(row: int) -> int:
    return 818 if row <= 16 else 819 if row <= 40 else 820


def unresolved_reason(row: int) -> str:
    name = PEOPLE[row][1]
    base = (
        "Exact-name and meaningful-variant searches across the NARA index context, "
        "CIA Reading Room, Library of Congress, OSS, employment, occupation, obituary, "
        "institutional, newspaper, directory, and archival sources produced no reliable "
        "identity and pre-OSS affiliation bridge; unbridged namesakes were rejected."
    )
    if row in PRINTED_OFFICERS:
        return (
            f"The printed officer rank for {name} establishes personnel category only. "
            + base
        )
    if row == 36:
        return (
            "The printed form 'Minerva Louis' is preserved without silently changing Louis "
            "to Louise. " + base
        )
    if row == 43:
        return (
            "The printed surname Watteins is preserved without a spelling correction. " + base
        )
    return base


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 818-820",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 492, rows 1-46; conflict comparison also uses page 457 row 16",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 46 printed rows remain separate. Page 492 was checked against layout-preserving text and an original-detail render. Full protected identifiers remain private.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; ten accepted protected-identifier comparisons; identifiers and record ordinals withheld",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "Ten exact-name identity bridges were accepted after private review. Code 999 was retained as identity-only evidence. No Army record is treated as a named employer or direct OSS-transfer record.",
        },
        {
            "key": TECH,
            "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf",
            "archival_identifier": "NN3-064-03-008; National Archives Identifier 1263923",
            "title": "World War II Army Enlistment Records: Reference Copy of Technical Documentation",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives at College Park - Electronic Records",
            "publication_record_date": "1994-2005; reference copy modified 2011",
            "locator": "PDF physical pages 44-46; name, Army-entry-date, grade, and civilian-occupation fields",
            "access_date": "2026-11-03",
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
            "locator": "PDF physical pages 171-175 and 304; categories 0-73, 1-26, 2-95, 5-25, 6-02, 7-36, 7-99, and 9-92",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical labels identify broad occupations or student status, not named employers, institutions, workplaces, or exact OSS-transfer dates.",
        },
        {
            "key": CONGRESS,
            "stable_url": "https://www.govinfo.gov/content/pkg/GPO-CRECB-1943-pt1/pdf/GPO-CRECB-1943-pt1-21-1.pdf",
            "archival_identifier": "78th Congress, 1st session, Congressional Record, volume 89, part 1",
            "title": "Congressional Record - Senate",
            "author_creator": "United States Congress",
            "repository_publisher": "U.S. Government Publishing Office",
            "publication_record_date": "1943-02-08",
            "locator": "Congressional Record page 675",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "Congressional Record",
            "rights_notes": "The record identifies Armitage Watkins with Overseas Publications, Office of War Information. It does not state when or whether he entered OSS.",
        },
        {
            "key": COLUMBIA,
            "stable_url": "https://findingaids.library.columbia.edu/archives/cul-4079450",
            "archival_identifier": "Columbia University Libraries collection cul-4079450",
            "title": "Armitage Watkins papers on the Office of War Information, 1941-1948",
            "author_creator": "Armitage Watkins",
            "repository_publisher": "Rare Book & Manuscript Library, Columbia University Libraries",
            "publication_record_date": "1941-1948",
            "locator": "Collection-level archival description",
            "access_date": "2026-11-03",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Armitage Watkins papers on the Office of War Information",
            "rights_notes": "Collection-level identity and institutional context only; the finding aid does not establish a pre-OSS employer chronology.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": ORG_OWI,
            "organization_id": "d907505c-05ff-502a-810c-e6189e186543",
            "canonical_name": "United States Office of War Information",
            "historical_name": "Office of War Information",
            "aliases": ["OWI", "U.S. Office of War Information"],
            "organization_type": "federal wartime information agency",
            "sector": "federal_government",
            "city": "Washington",
            "state_or_region": "District of Columbia",
            "country": "United States",
            "active_dates": "1942-1945",
            "normalization_notes": "Canonical existing wartime agency entity; preserved separately from OSS and postwar successor bodies.",
        }
    ]


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, item in ARMY_MATCHES.items():
        if item["occupation"] is None:
            continue
        values.append({
            "key": f"{slug(PEOPLE[row][1])}-army-occupation-b1002",
            "person_id": PEOPLE[row][0],
            "occupation": item["occupation"],
            "relationship_type": "student" if item["code"] == "992" else "unknown",
            "end_date": item["date"],
            "date_precision": f"Historical civilian-occupation code {item['code']} was recorded at Army entry on {item['date']}; no named employer, workplace, school, or exact OSS-transfer date is supplied.",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "confirmed",
            "claim_confidence": "medium",
            "source_quality": "A_direct_official",
            "publication_status": "publish_qualified",
            "research_notes": "Broad historical occupation or student category only; no named employer, workplace, school, or OSS transition is inferred.",
        })
    values.append({
        "key": "armitage-watkins-owi-b1002",
        "person_id": PEOPLE[11][0],
        "organization_key": ORG_OWI,
        "organization_name_as_found": "Office of War Information",
        "role_title": "Overseas Publications",
        "occupation": "wartime information work",
        "relationship_type": "government_assignment",
        "date_precision": "A February 8, 1943 Congressional Record passage identifies Watkins with Overseas Publications, Office of War Information; no start or end date is supplied.",
        "city": "Washington",
        "state_or_region": "District of Columbia",
        "country": "United States",
        "immediate_pre_oss": False,
        "last_civilian_pre_service": False,
        "pre_oss_temporal_basis": "temporal_relation_uncertain",
        "identity_confidence": "high_confidence",
        "claim_confidence": "medium",
        "source_quality": "A_direct_official",
        "publication_status": "publish_qualified",
        "research_notes": "The wartime federal affiliation is documented, but the accessible sources do not establish its sequence relative to the indexed OSS personnel file.",
    })
    return values


def make_claim(
    *, key: str, row: int, claim_type: str, text: str, paraphrase: str,
    identity: str, temporal: str, quality: str, confidence: str,
    publication: str, notes: str, source_links: list[dict[str, str]],
    affiliation_key: str | None = None,
) -> dict[str, object]:
    value: dict[str, object] = {
        "key": key,
        "person_id": PEOPLE[row][0],
        "claim_type": claim_type,
        "claim_text": text,
        "evidence_paraphrase": paraphrase,
        "identity_match_assessment": identity,
        "temporal_assessment": temporal,
        "source_quality": quality,
        "claim_confidence": confidence,
        "publication_status": publication,
        "match_notes": notes,
        "sources": source_links,
    }
    if affiliation_key:
        value["affiliation_key"] = affiliation_key
    return value


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, item in ARMY_MATCHES.items():
        name = PEOPLE[row][1]
        values.append(make_claim(
            key=f"identity-{slug(name)}-b1002",
            row=row,
            claim_type="identity",
            text=f"Indexed {name} is confirmed as the reviewed official Army entry record.",
            paraphrase="The exact indexed and Army names agree, and a nonshared protected identifier connects the records.",
            identity="Confirmed by exact name and a nonshared protected-identifier agreement; the identifier and record ordinal remain private.",
            temporal=f"The Army record dates entry to {item['date']} and carries historical civilian code {item['code']}.",
            quality="A_direct_official",
            confidence="confirmed",
            publication="published",
            notes="Identity only; no named employer, workplace, school, or exact OSS-transfer date is inferred.",
            source_links=[
                {"source_key": INDEX, "locator_override": f"PDF page 492 row {row}; protected identifier withheld"},
                {"source_key": ARMY, "locator_override": "Accepted reviewed identity bridge; protected identifier withheld"},
            ],
        ))
        if item["occupation"] is None:
            continue
        values.append(make_claim(
            key=f"occupation-{slug(name)}-b1002",
            row=row,
            claim_type="occupation",
            text=f"At Army entry on {item['date']}, {name} was recorded in the historical {item['occupation']} category; no named employer or institution is identified.",
            paraphrase=f"The accepted Army record carries civilian-occupation code {item['code']}, decoded from NARA's official code list.",
            identity="The category belongs only to the confirmed protected-identifier match; the identifier itself is not public.",
            temporal="Strongly date-bounded to Army entry; it does not establish the immediate pre-OSS affiliation or a named employer or school.",
            quality="A_direct_official",
            confidence="medium",
            publication="publish_qualified",
            notes="Published with its limits and excluded from verified-employer analytics.",
            source_links=[
                {"source_key": ARMY, "locator_override": f"Army entry {item['date']}; civilian occupation code {item['code']}; protected identifier withheld"},
                {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46"},
                {"source_key": CODES, "locator_override": item["locator"], "excerpt_override": item["label"]},
            ],
            affiliation_key=f"{slug(name)}-army-occupation-b1002",
        ))

    values.extend([
        make_claim(
            key="conflict-fred-watson-b1002",
            row=26,
            claim_type="identity",
            text="Fred S Watson Jr. remains in an unresolved protected-identifier conflict with the separately indexed Harvey R Swarts.",
            paraphrase="The NARA index prints the same protected identifier on two materially different names, so neither source row is silently merged.",
            identity="Conflicting: the protected identifier is shared while the names differ materially.",
            temporal="No identity, occupation, employer, or chronology is transferred across the conflicting rows.",
            quality="A_direct_official",
            confidence="conflicting",
            publication="conflicting",
            notes="Both source rows remain separate and the full identifier stays private pending archival review.",
            source_links=[
                {"source_key": INDEX, "locator_override": "PDF page 492 row 26 and page 457 row 16; shared protected identifier withheld"},
            ],
        ),
        make_claim(
            key="identity-armitage-watkins-b1002",
            row=11,
            claim_type="identity",
            text="The indexed Armitage Watkins is a high-confidence match to the Office of War Information official documented in 1943.",
            paraphrase="The uncommon exact name aligns across the OSS index, a contemporary Congressional Record passage, and Columbia's dedicated Watkins OWI papers.",
            identity="High confidence from an uncommon exact name and two independent official or institutional sources in the same wartime information context.",
            temporal="The external evidence documents an OWI role in 1943 but does not date indexed OSS service.",
            quality="A_direct_official",
            confidence="high",
            publication="published",
            notes="The identity bridge is strong; the Box 818 personnel file remains necessary for the OSS chronology and prewar employer.",
            source_links=[
                {"source_key": INDEX, "locator_override": "PDF page 492 row 11; Box 818"},
                {"source_key": CONGRESS, "locator_override": "Congressional Record page 675", "excerpt_override": "Armitage Watkins, Overseas Publications, Office of War Information"},
                {"source_key": COLUMBIA, "locator_override": "Collection cul-4079450"},
            ],
        ),
        make_claim(
            key="affiliation-armitage-watkins-owi-b1002",
            row=11,
            claim_type="other_pre_oss_affiliation",
            text="On February 8, 1943, Armitage Watkins was identified with Overseas Publications in the Office of War Information.",
            paraphrase="A contemporary Congressional Record passage gives his name and OWI unit; Columbia preserves his OWI papers from 1941-1948.",
            identity="High confidence from the distinctive exact-name and wartime institutional match.",
            temporal="The role is securely wartime but its sequence relative to indexed OSS service is uncertain; it is not labeled immediate pre-OSS.",
            quality="A_direct_official",
            confidence="medium",
            publication="publish_qualified",
            notes="A documented government affiliation, not a settled previous employer or immediate OSS predecessor.",
            source_links=[
                {"source_key": CONGRESS, "locator_override": "Congressional Record page 675", "excerpt_override": "Armitage Watkins, Overseas Publications, Office of War Information"},
                {"source_key": COLUMBIA, "support_type": "context_only", "locator_override": "Collection cul-4079450"},
            ],
            affiliation_key="armitage-watkins-owi-b1002",
        ),
    ])
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
    special_rows = set(ARMY_MATCHES) | {11, 26}
    for row in sorted(set(PEOPLE) - special_rows):
        reason = unresolved_reason(row)
        values.append(base_update(
            row,
            identity_status="unresolved",
            identity_evidence=f"The visually verified page 492 row preserves {PEOPLE[row][1]}, its printed rank or blank rank cell, and archival context. {reason}",
            research_status="requires_archival_review",
            next_action=f"Review the indexed Box {box_for(row)} personnel file for corroborating identifiers, the immediate pre-OSS affiliation, and the last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}",
        ))
    for row, item in ARMY_MATCHES.items():
        status = "occupation_only_found" if item["occupation"] else "requires_archival_review"
        next_action = (
            f"Review the indexed Box {box_for(row)} personnel file to identify any named employer or school behind the broad {item['occupation']} category and establish the Army-to-OSS chronology."
            if item["occupation"]
            else f"Review the indexed Box {box_for(row)} personnel file because historical code 999 supplies no publishable occupation, employer, or Army-to-OSS chronology."
        )
        values.append(base_update(
            row,
            identity_status="confirmed",
            identity_evidence="The exact indexed name and a nonshared protected identifier connect the row to the reviewed official Army record.",
            personnel_category="enlisted_army_personnel",
            commissioned_officer=False,
            allied_or_foreign_personnel=False,
            research_status=status,
            next_action=next_action,
            nara_catalog_id="1263923",
        ))
    values.extend([
        base_update(
            11,
            identity_status="high_confidence",
            identity_evidence="The uncommon exact name aligns across the index, a contemporary Congressional Record passage, and Columbia's dedicated Armitage Watkins OWI papers.",
            research_status="requires_archival_review",
            next_action="Review the indexed Box 818 personnel file to establish the sequence between Armitage Watkins's documented Office of War Information role and indexed OSS service, and to identify his last civilian employer before wartime government service.",
        ),
        base_update(
            26,
            identity_status="conflicting",
            identity_evidence="The same protected identifier is printed for Fred S. Watson Jr. on page 492 and Harvey R. Swarts on page 457; materially different names prevent a merge or identity transfer.",
            research_status="conflicting_sources",
            next_action="Review both indexed personnel files in Boxes 819 and 760 to resolve the shared protected identifier before assigning identity, occupation, employer, or chronology evidence.",
        ),
    ])
    if len(values) != len(PEOPLE):
        raise RuntimeError(f"Expected {len(PEOPLE)} person updates, generated {len(values)}")
    return values


def research_attempts() -> list[dict[str, object]]:
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        if row in ARMY_MATCHES:
            item = ARMY_MATCHES[row]
            outcome, reviewed, rejected = "source_reviewed", 8, 5
            if item["occupation"]:
                note = f"A reviewed protected-identifier Army bridge supports identity and a qualified {item['occupation']} category at Army entry; no named employer, workplace, school, or OSS-transfer date is supplied."
            else:
                note = "A reviewed protected-identifier Army bridge confirms identity, but historical code 999 supplies no publishable occupation, employer, or OSS-transfer chronology."
        elif row == 26:
            outcome, reviewed, rejected = "candidate_rejected", 8, 6
            note = "The same protected identifier appears on the Fred S. Watson Jr. and Harvey R. Swarts index rows; no identity or occupation evidence was transferred across the conflict."
        elif row == 11:
            outcome, reviewed, rejected = "source_reviewed", 11, 6
            note = "A contemporary Congressional Record passage and Columbia archival collection support a high-confidence Armitage Watkins identity and a qualified Office of War Information affiliation; the OSS sequence and previous civilian employer remain unresolved."
        else:
            outcome, reviewed, rejected = "candidate_rejected", 7, 6
            note = unresolved_reason(row)
        attempts.append({
            "key": f"page492-row{row}-{slug(name)}-b1002",
            "person_id": person_id,
            "source_adapter": "manual_staged_protocol",
            "query_text": f"{name}; NARA OSS index context; CIA Reading Room, National Archives, and Library of Congress exact-name domain checks; exact-name and meaningful spelling, initial, suffix, and punctuation variants; OSS, rank, branch, assignment, and identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory, and archival searches; indexed Box {box_for(row)}; protected identifiers used only in private official-record comparison",
            "query_variant_type": "staged_identity_employment_archival_protocol_batch_1002",
            "started_at": "2026-11-03T19:50:00Z",
            "completed_at": "2026-11-03T20:00:00Z",
            "outcome": outcome,
            "sources_reviewed": reviewed,
            "candidate_sources_rejected": rejected,
            "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, postwar-only leads, and sources without an OSS, protected-identifier, rank, unit, or personnel-file bridge were rejected. Historical Army categories were not converted into named employers, workplaces, or schools. The Martin Joseph Waters Jr. naval-officer result with a different officer identifier was not assigned to indexed Martin J. Waters Jr.",
            "research_notes": f"{note} Exact-name official-domain, OSS, employer, occupation, obituary, biography, institutional, newspaper, directory, and archival searches were checked as applicable. The NARA index page was text-extracted, rendered, and visually checked. Official Army bulk data, technical documentation, and code documentation were inspected locally. The Columbia finding-aid endpoint was access-restricted, so only its stable collection identifier and independently indexed collection-level description were retained; no access restriction was bypassed. No search-result snippet was used as sole final employer evidence, and no authenticated NARA Catalog API call was made.",
            "next_action": f"Review the indexed Box {box_for(row)} personnel file for corroborating identifiers, the immediate pre-OSS affiliation, and the last civilian employer before wartime service.",
            "attempt_number": 1,
            "research_agent_version": "before-oss-b1002-v1",
        })
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-1002-v1",
        "reviewer": "Before OSS Batch 1002 evidence review",
        "sources": sources(),
        "organizations": organizations(),
        "affiliations": affiliations(),
        "claims": claims(),
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }
    EvidenceBundle.model_validate(bundle)
    OUTPUT.write_text(
        json.dumps(bundle, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
