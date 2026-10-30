#!/usr/bin/env python3
"""Generate the reviewed Batch 988 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page484-ovito-vlasic-to-lou-bernard-voigt-"
    "review_batch-988_2026-10-30.json"
)

INDEX = "nara-index-b988"
ARMY = "army-bulk-b988"
TECH = "army-tech-b988"
CODES = "army-codes-b988"
NPS_VOIGT = "nps-hollin-hills-voigt-b988"
BMC_1943 = "black-mountain-announcements-1943-b988"

ORG_SOM = "skidmore-owings-merrill-b988"
ORG_BMC = "black-mountain-college-b988"

EDGAR_VOGES_DUPLICATE_GROUP = "page484-edgar-voges-b988"
VANCE_VOGAL_VOGEL_DUPLICATE_GROUP = "page484-vance-vogal-vogel-b988"


PEOPLE = {
    24: ("b75eda33-b0e4-563e-abf0-a49867f93cf0", "Ovito T Vlasic"),
    25: ("faa6c43f-2007-5a7d-a45b-a47eb5e47d23", "Charlie Vlkojan Jr."),
    26: ("5e7446c1-b779-56bd-aba6-52dab666613a", "Stephen F Vlodek"),
    27: ("84e8bec8-11d8-5218-88e1-5137c23f35db", "John C Vlossak"),
    28: ("449eed30-cb35-5c10-ba63-0768a85eaa71", "Sylvester J Vodde"),
    29: ("3dec0c62-6dbb-58b3-ac01-7efa2beb3ee2", "Josephine G Vodika"),
    30: ("78470cf4-0695-53b5-ac63-0c09fa824a38", "Oliver B Vodrey"),
    31: ("ebae0b04-b7a7-5139-887e-b226723176ec", "Vance V Vogal"),
    32: ("0f604abf-fcad-532b-ac0e-716cadbca4c8", "Emmett Vogan Jr."),
    33: ("e9ff643a-98e9-5c57-a6f2-98cfbbaf4ed3", "Noel A Voge"),
    34: ("09afd35f-18d3-5e71-a594-635bc5f9bd43", "Edward F Vogel"),
    35: ("2930308b-327f-59b2-9a3a-3f93ec9d3623", "Frank S Vogel"),
    36: ("b27073b5-6d3a-5e5f-ae33-76aa7bd959d4", "Robert F Vogel"),
    37: ("aa961d2a-055b-546e-9ec4-e49f5a22ab40", "Vance V Vogel"),
    38: ("d3ad13a4-8e99-51d0-9333-d7b67dd0d847", "Edgar Voges"),
    39: ("a6682a72-96bc-5cae-927f-2f1f8c742c36", "Edgar Voges"),
    40: ("4560d7c3-f72b-5ffd-be8c-e00d2ab655b8", "Bert D Vogt"),
    41: ("56518591-c05b-5bd1-8d71-00382943dda8", "George R Vogt"),
    42: ("60985369-08f8-58e4-9568-20d77cfb57b1", "Lawrence R Vogt"),
    43: ("0c543385-954c-5510-8e6c-b73d0f990c1b", "Robert J Vogt"),
    44: ("d9d8ebc6-c7f6-57ea-b344-5a47578fc492", "Edgar H Voight"),
    45: ("1186b7ea-8636-5337-8d06-89c74a5ae929", "John P Voight"),
    46: ("01f9144e-eb54-5b9e-877e-5b452a804ee7", "Lou Bernard Voigt"),
}


ARMY_FINDINGS = {
    27: {
        "date": "1941-02-06",
        "code": "002",
        "occupation": "Actors and actresses",
        "public_occupation": "actor or actress",
        "relationship": "employment",
    },
    28: {
        "date": "1942-12-29",
        "code": "753",
        "occupation": "Linemen and servicemen, telegraph, telephone, and power",
        "public_occupation": "lineman or serviceman in telegraph, telephone, or power work",
        "relationship": "employment",
    },
    33: {
        "date": "1942-11-12",
        "code": "588",
        "occupation": "Warehousing, storekeeping, handling, loading, unloading, and related occupations, n.e.c.",
        "public_occupation": "warehousing, storekeeping, handling, loading, unloading, or related occupation",
        "relationship": "employment",
    },
    34: {
        "date": "1943-07-15",
        "code": "992",
        "occupation": "Students",
        "public_occupation": "student",
        "relationship": "student",
    },
    35: {
        "date": "1942-04-03",
        "code": "072",
        "occupation": "Retail managers",
        "public_occupation": "retail manager",
        "relationship": "employment",
    },
    36: {
        "date": "1940-08-28",
        "code": "226",
        "occupation": "Cooks, except private family",
        "public_occupation": "cook, except for a private family",
        "relationship": "employment",
    },
    38: {
        "date": "1942-04-24",
        "code": "736",
        "occupation": "Chauffeurs and drivers, bus, taxi, truck, and tractor",
        "public_occupation": "chauffeur or driver of a bus, taxi, truck, or tractor",
        "relationship": "employment",
    },
    42: {
        "date": "1942-03-06",
        "code": "043",
        "occupation": "Decorators and window dressers",
        "public_occupation": "decorator or window dresser",
        "relationship": "employment",
    },
    43: {
        "date": "1942-09-19",
        "code": "295",
        "occupation": "Elevator operators",
        "public_occupation": "elevator operator",
        "relationship": "employment",
    },
}


UNRESOLVED = {
    24: "Exact-name, spelling-variant, OSS, occupation, obituary, institutional and archival searches produced no reliable identity or pre-OSS affiliation bridge.",
    26: "A same-name veteran-burial lead records Army service, but no protected identifier, OSS assignment or employer connects it to the indexed person.",
    29: "A county enlistment-list lead repeats the exact name but supplies no pre-OSS employer or personnel-file bridge.",
    30: "An exact-name Army Air Forces officer lead has incompatible identifier evidence and cannot be assigned without review of the indexed file.",
    31: "The adjacent Vance V Vogel row may be a spelling variant, but name similarity and proximity do not establish duplication or an employer.",
    32: "Exact-name, suffix, OSS, employer, occupation, obituary and archival searches produced no reliable identity or pre-OSS affiliation bridge.",
    37: "The adjacent Vance V Vogal row may be a spelling variant, but no source bridges the two rows or establishes a pre-OSS affiliation.",
    39: "This unnumbered Edgar Voges row may duplicate the adjacent numbered row, but the official Army record is assigned only to the numbered source row.",
    41: "Exact-name, middle-initial, OSS, employer, occupation, obituary and archival searches produced no reliable identity or pre-OSS affiliation bridge.",
    44: "Exact-name, middle-initial, identifier, OSS, employer and archival searches produced no reliable identity or pre-OSS affiliation bridge.",
    45: "Exact-name, middle-initial, OSS, employer, occupation, obituary and archival searches produced no reliable identity or pre-OSS affiliation bridge.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 806-807",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 484, rows 24-46; checked against layout-preserving text and an original-detail page render",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. The two Edgar Voges rows and the Vogal/Vogel rows are grouped only for possible-duplicate review; no people are merged.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; eleven protected-identifier comparisons; identifiers and record ordinals withheld",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "Ten nonshared-identifier identity bridges were accepted. The Bert D Vogt candidate is conflicting because the index prints the same identifier for Bert D Voot. No raw bulk row, record ordinal or full identifier enters public assets.",
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
            "locator": "PDF physical pages 170-175 and amended page 304; codes 002, 043, 072, 226, 295, 588, 736, 753 and 992 visually checked",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical categories identify broad occupation or student status, not a named employer, workplace or exact job. Code 590 is absent from the reviewed three-digit lists and remains uninterpreted.",
        },
        {
            "key": NPS_VOIGT,
            "stable_url": "https://www.dhr.virginia.gov/wp-content/uploads/2018/04/029-5471-Hollin_Hills_HD_2013_NRHP_Final.pdf",
            "archival_identifier": "Virginia DHR 029-5471; National Register of Historic Places Registration Form",
            "title": "Hollin Hills Historic District",
            "author_creator": "National Park Service; Virginia Department of Historic Resources",
            "repository_publisher": "United States Department of the Interior, National Park Service; Virginia Department of Historic Resources",
            "publication_record_date": "2013",
            "locator": "PDF physical page 98, Section 8 page 97; Lou Bernard Voigt biography",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "National Register of Historic Places",
            "rights_notes": "The official registration narrative directly sequences Black Mountain College, Skidmore, Owings and Merrill wartime work, and OSS design work begun in Washington in 1944.",
        },
        {
            "key": BMC_1943,
            "stable_url": "https://collection.ashevilleart.org/objects-1/info/6589?sort=0",
            "archival_identifier": "Asheville Art Museum accession 2017.40.021",
            "title": "Black Mountain College Announcements 1943-4",
            "author_creator": "Black Mountain College",
            "repository_publisher": "Asheville Art Museum",
            "publication_record_date": "1943",
            "locator": "Faculty roster; Lou Bernard Voigt, Botany and Landscape Architecture, Black Mountain College since 1942",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Black Mountain College Collection, Theodore Dreier Sr. Document Collection",
            "rights_notes": "Contemporary 14-page announcements booklet; the project stores citation metadata and a short paraphrase, not the copyrighted booklet.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": ORG_SOM,
            "canonical_name": "Skidmore, Owings & Merrill",
            "historical_name": "Skidmore, Owings and Merrill (SOM)",
            "aliases": ["SOM", "Skidmore, Owings and Merrill"],
            "organization_type": "architecture and engineering firm",
            "sector": "engineering_science_and_technology",
            "country": "United States",
            "active_dates": "Founded 1936",
            "normalization_notes": "Historical firm name retained. No modern successor or office location is inferred from the Voigt biography.",
        },
        {
            "key": ORG_BMC,
            "canonical_name": "Black Mountain College",
            "historical_name": "Black Mountain College",
            "organization_type": "college",
            "sector": "academia_and_research",
            "city": "Black Mountain",
            "state_or_region": "North Carolina",
            "country": "United States",
            "active_dates": "1933-1957",
            "normalization_notes": "Defunct historical college preserved under its contemporary name.",
        },
    ]


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, item in ARMY_FINDINGS.items():
        name = PEOPLE[row][1]
        values.append(
            {
                "key": f"{slug(name)}-army-category-b988-row{row}",
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
    values.extend(
        [
            {
                "key": "lou-bernard-voigt-som-b988",
                "person_id": PEOPLE[46][0],
                "organization_key": ORG_SOM,
                "organization_name_as_found": "Skidmore, Owings and Merrill (SOM)",
                "role_title": "site-planning designer for atomic plant installations at Oak Ridge",
                "occupation": "landscape architect and site planner",
                "relationship_type": "employment",
                "start_date": "1943",
                "end_date": "1944",
                "date_precision": "The official chronology places this engagement after Black Mountain College ended in September 1943 and before OSS design work began in Washington in 1944; exact employment dates are not supplied",
                "city": "Oak Ridge",
                "state_or_region": "Tennessee",
                "country": "United States",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Best-supported immediate pre-OSS affiliation and last civilian employer. The source directly sequences SOM's Oak Ridge work before OSS employment in Washington; it does not supply an exact transfer date.",
            },
            {
                "key": "lou-bernard-voigt-black-mountain-b988",
                "person_id": PEOPLE[46][0],
                "organization_key": ORG_BMC,
                "organization_name_as_found": "Black Mountain College",
                "role_title": "instructor in botany and landscape architecture",
                "occupation": "landscape architect and educator",
                "relationship_type": "employment",
                "start_date": "1942-09",
                "end_date": "1943-09",
                "date_precision": "The National Register biography gives September 1942 to September 1943; a contemporary 1943 college announcement lists his faculty fields and service since 1942",
                "city": "Black Mountain",
                "state_or_region": "North Carolina",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Earlier documented employment, kept separate from the later SOM role that best fits the immediate and last-civilian categories.",
            },
        ]
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
        values.append(
            claim(
                row,
                f"identity-{slug(name)}-army-b988-row{row}",
                "identity",
                f"Indexed {name} is high-confidence matched to the official Army entry reviewed for Batch 988.",
                "The exact official name and a nonshared protected identifier directly link the printed row to the reviewed Army record.",
                "High confidence from exact name and a nonshared protected identifier; the protected value and raw bulk record are withheld.",
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
                f"occupation-{slug(name)}-b988-row{row}",
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
                f"{slug(name)}-army-category-b988-row{row}",
                "publish_qualified",
            )
        )

    values.extend(
        [
            claim(
                25,
                "identity-charlie-vlkojan-army-b988-row25",
                "identity",
                "Indexed Charlie Vlkojan Jr. is high-confidence matched to the official Army entry reviewed for Batch 988.",
                "The exact official name, suffix and nonshared protected identifier directly link the printed row to the Army record.",
                "High confidence from exact name, suffix and a nonshared protected identifier; the protected value and raw bulk record are withheld.",
                "The Army-entry date is after OSS dissolution and code 590 is undefined in the reviewed code list, so the record supports identity only.",
                "A_direct_official",
                "high",
                [{"source_key": INDEX}, {"source_key": ARMY, "locator_override": "Accepted identity bridge; protected identifier and raw record withheld"}],
                "No occupation, employer or pre-OSS chronology is inferred from an undefined code or a post-OSS Army-entry date.",
            ),
            claim(
                46,
                "identity-lou-bernard-voigt-nps-b988",
                "identity",
                "Indexed Lou Bernard Voigt is high-confidence identified as the landscape architect and wartime OSS designer documented by the National Park Service.",
                "The official National Register biography gives the exact distinctive name and explicitly states that he began OSS design work in Washington in 1944.",
                "High confidence from an exact distinctive full name and an authoritative official biography that directly links the person to OSS.",
                "The biography supplies a dated employment sequence from Black Mountain College to SOM and then OSS.",
                "B_authoritative_institutional",
                "high",
                [{"source_key": INDEX}, {"source_key": NPS_VOIGT}],
                "The match is not upgraded to confirmed because the indexed personnel file has not been reviewed.",
            ),
            claim(
                46,
                "immediate-lou-bernard-voigt-som-b988",
                "immediate_pre_oss_affiliation",
                "Skidmore, Owings & Merrill is the best-supported immediate pre-OSS affiliation for Lou Bernard Voigt.",
                "The official biography places Voigt's SOM site-planning work for Oak Ridge after his September 1943 college tenure and before he began OSS design work in Washington in 1944.",
                "High-confidence identity from the exact distinctive name and direct OSS link.",
                "Strongly date-bounded sequence with no known intervening affiliation; exact transfer date is not supplied.",
                "B_authoritative_institutional",
                "high",
                [{"source_key": NPS_VOIGT}],
                "The firm is named as an employer; Oak Ridge is the documented worksite, not a separate employer.",
                "lou-bernard-voigt-som-b988",
            ),
            claim(
                46,
                "last-civilian-lou-bernard-voigt-som-b988",
                "last_civilian_pre_service",
                "Skidmore, Owings & Merrill is also the best-supported last civilian employer before Lou Bernard Voigt's OSS service.",
                "The official chronology moves from SOM's wartime Oak Ridge site-planning engagement to OSS design employment begun in Washington in 1944.",
                "High-confidence identity from the exact distinctive name and direct OSS link.",
                "Strongly date-bounded; the same civilian job legitimately satisfies both categories, which remain separately modeled.",
                "B_authoritative_institutional",
                "high",
                [{"source_key": NPS_VOIGT}],
                "Immediate affiliation and last civilian employer are stored as distinct claims even though the same documented job answers both questions.",
                "lou-bernard-voigt-som-b988",
            ),
            claim(
                46,
                "earlier-lou-bernard-voigt-black-mountain-b988",
                "other_pre_oss_affiliation",
                "Lou Bernard Voigt taught botany and landscape architecture at Black Mountain College from September 1942 to September 1943.",
                "The National Register biography gives the date range and teaching fields; a contemporary 1943 college announcement lists Voigt on the faculty in botany and landscape architecture and notes service since 1942.",
                "High-confidence identity from the exact distinctive name and consistent education and professional chronology.",
                "Explicitly dated before the later SOM and OSS roles; not labeled immediate.",
                "B_authoritative_institutional",
                "high",
                [{"source_key": NPS_VOIGT}, {"source_key": BMC_1943}],
                "Earlier documented employment, kept separate from the immediate SOM role.",
                "lou-bernard-voigt-black-mountain-b988",
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
        duplicate = None
        identity_status = "unresolved"
        priority = "high"
        if row in {31, 37}:
            duplicate = VANCE_VOGAL_VOGEL_DUPLICATE_GROUP
            identity_status = "ambiguous"
            priority = "critical"
        elif row == 39:
            duplicate = EDGAR_VOGES_DUPLICATE_GROUP
            identity_status = "ambiguous"
            priority = "critical"
        values.append(
            base_update(
                row,
                identity_status=identity_status,
                identity_evidence=f"The visually verified page 484 row preserves {PEOPLE[row][1]} and its indexed Box 806 or 807 context. {reason}",
                personnel_category="unknown_or_indeterminate",
                commissioned_officer=None,
                allied_or_foreign_personnel=False,
                possible_duplicate_group=duplicate,
                research_status="requires_archival_review",
                next_action=f"Review the indexed personnel file for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}",
                archival_review_priority=priority,
            )
        )

    for row, item in ARMY_FINDINGS.items():
        values.append(
            base_update(
                row,
                identity_status="high_confidence",
                identity_evidence="The exact official name and a nonshared protected-identifier agreement support the Army identity match; the protected value remains private.",
                personnel_category="enlisted_army_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                possible_duplicate_group=EDGAR_VOGES_DUPLICATE_GROUP if row == 38 else None,
                research_status="occupation_only_found",
                next_action=f"Review the indexed personnel file to identify any named employer behind historical code {item['code']} and establish the Army-to-OSS chronology. The code supplies only a broad occupation or student category.",
                nara_catalog_id="1263923",
            )
        )

    values.extend(
        [
            base_update(
                25,
                identity_status="high_confidence",
                identity_evidence="The exact official name, suffix and a nonshared protected-identifier agreement support the Army identity match; the protected value remains private.",
                personnel_category="enlisted_army_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                research_status="requires_archival_review",
                next_action="Review Box 806 to establish the pre-OSS chronology. The accepted Army identity record entered after OSS dissolution and code 590 is absent from the reviewed official code list, so it supplies no publishable occupation.",
                nara_catalog_id="1263923",
            ),
            base_update(
                40,
                identity_status="conflicting",
                identity_evidence="The printed protected identifier is shared by separately indexed Bert D Vogt and Bert D Voot. The Army record uses the Vogt spelling, but the identifier conflict prevents transfer of its machinist category or biography.",
                personnel_category="unknown_or_indeterminate",
                commissioned_officer=None,
                allied_or_foreign_personnel=False,
                research_status="conflicting_sources",
                next_action="Review the Bert D Vogt Box 807 file together with the separately indexed Bert D Voot file before assigning the Army identity, occupation or any employer.",
                archival_review_priority="critical",
            ),
            base_update(
                46,
                identity_status="high_confidence",
                identity_evidence="The exact distinctive full name and an official National Register biography directly link Lou Bernard Voigt to OSS design work begun in Washington in 1944 and provide the preceding employment chronology.",
                name_variants=["Lou Bernard “Barney” Voigt", "Lou “Barney” Voigt"],
                personnel_category="civilian_professional_or_administrative_grade",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                research_status="verified_employer_found",
                next_action="Skidmore, Owings & Merrill is documented as the strongly date-bounded immediate and last civilian employer, with Black Mountain College as earlier employment. Review Box 807 to refine the exact 1944 transfer date and OSS grade.",
                archival_review_priority="medium",
            ),
        ]
    )
    return values


def research_attempts() -> list[dict[str, object]]:
    sourced = set(ARMY_FINDINGS) | {25, 30, 31, 37, 39, 40, 46}
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        if row == 46:
            outcome = "source_reviewed"
            sources_reviewed = 8
            rejected = 4
            detail = "Official and contemporary institutional sources established the exact OSS identity, SOM immediate and last civilian employer, and earlier Black Mountain College employment."
        elif row in ARMY_FINDINGS or row == 25:
            outcome = "source_reviewed"
            sources_reviewed = 6
            rejected = 4
            detail = "Reviewed official index, Army bulk, technical and code-list evidence produced the identity and qualified occupation, student-status or identity-only outcome recorded in the bundle."
        elif row == 40:
            outcome = "source_reviewed"
            sources_reviewed = 6
            rejected = 5
            detail = "The shared protected identifier creates a direct index conflict with Bert D Voot; the Army identity and machinist code were withheld."
        elif row in {31, 37, 39}:
            outcome = "source_reviewed"
            sources_reviewed = 5
            rejected = 5
            detail = "The immutable adjacent index rows support possible-duplicate review only; no external source justified a merge or employer claim."
        else:
            outcome = "no_result"
            sources_reviewed = 5
            rejected = 5
            detail = UNRESOLVED[row]
        attempts.append(
            {
                "key": f"page484-row{row}-{slug(name)}-b988",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index context; CIA Reading Room or equivalent official-source check; exact-name and meaningful variants; OSS, rank, branch, identifier and assignment clues; employer and occupation 1940; obituary, institutional, newspaper, directory and archival searches; indexed Box 806 or 807; protected identifiers used only in private official-record comparison",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_988",
                "started_at": "2026-10-30T14:45:00Z",
                "completed_at": "2026-10-30T15:22:00Z",
                "outcome": outcome,
                "sources_reviewed": sources_reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, snippets, commercial people-finder pages, relatives, unsourced genealogy, postwar-only leads and sources without an OSS, protected-identifier, rank, unit or personnel-file bridge were rejected. Historical occupation categories, student status, military assignments and OSS-period duties were not converted into employers. The Oliver B Vodrey military lead was not assigned because its identifier evidence conflicts; Bert D Vogt's Army lead was withheld because the identifier is shared with Bert D Voot.",
                "research_notes": f"{detail} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain and archival searches were checked as applicable. The NARA index page, official Army technical documentation and code-list pages were inspected directly. No search-result snippet was used as sole final evidence, no paywall or access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": "Review the indexed personnel file for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before wartime service.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b988-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-988-v1",
        "reviewer": "Before OSS Batch 988 evidence review",
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
