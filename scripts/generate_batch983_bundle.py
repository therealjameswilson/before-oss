#!/usr/bin/env python3
"""Generate the reviewed Batch 983 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page482-edward-c-veigel-to-m-p-veran-"
    "review_batch-983_2026-10-30.json"
)

INDEX = "nara-index-b983"
ARMY = "army-bulk-b983"
TECH = "army-tech-b983"
CODES = "army-codes-b983"
CAMBRIDGE_VELLA = "cambridge-walter-vella-b983"
OSS_SOCIETY_VELLIS = "oss-society-alex-vellis-b983"
USWM_VELLIS = "us-war-memorials-alex-vellis-b983"
USWM_MONUMENT = "us-war-memorials-greek-og-b983"

ORG_BERKELEY = "uc-berkeley-b983"
ORG_ASTP = "army-astp-b983"
ORG_GREEK_OG = "oss-greek-og-b983"


PEOPLE = {
    1: ("25b4ded1-d287-5680-9e77-072ccadf2f03", "Edward C Veigel"),
    2: ("3b8b4299-8dc4-5b1e-aff3-d8abe1363965", "Rock G Veilleux"),
    3: ("033b3adc-b3f2-525a-802f-6d438bcf8bc9", "Evelyn M Veith"),
    4: ("1124fde4-d031-5cc1-8b89-217722a1e6cc", "Paul Velay"),
    5: ("45dc42eb-8c1c-52ba-91a1-1ac1da7909e4", "Hermes Velez"),
    6: ("8b6fe7b1-ce53-5cc3-895f-724988f74fcd", "Anthony J Vella"),
    7: ("404f2fd6-b353-581f-8ba8-57b953916e94", "Anthony J Vella"),
    8: ("ca775866-fb72-5226-8b75-71447d09d156", "Walter F Vella"),
    9: ("9a81eee3-9800-507c-b604-ef49aafc3da3", "Arthur H Velleman"),
    10: ("833cab1f-839d-5766-baf2-4bebff78cada", "Moritz Velleman"),
    11: ("899455b1-64c6-5a77-8c65-29b2447b86a9", "Guss Vellios"),
    12: ("5a0538fa-0b0c-5f45-bbbc-4094c81f9736", "Alex L Vellis"),
    13: ("28d4ca4f-e3c6-5322-a519-d2f03ee5c6fd", "Lawson R Venable"),
    14: ("73d65c5b-56b8-5e0d-bf76-055753173f4a", "Theodore Venard"),
    15: ("982f70ae-b035-5658-9369-decacad2e92b", "Malcolm Vendrick"),
    16: ("5cd94b1a-0c3b-5fbc-8750-5946f8b482d8", "Anthony A Veneruso"),
    17: ("ba6f0b53-a64c-567b-a673-b02fc77e71b0", "Irene A Venit"),
    18: ("2f8a9780-0748-5d48-92f7-de31c48cba54", "Claude H Venon"),
    19: ("7f0f46d5-0bad-5d45-92a6-5bbe9bfd9057", "Atta B Venson"),
    20: ("3a7fc3e4-e455-57dc-b944-8b992a31a505", "Annina Ventrella"),
    21: ("bdd660b0-ca6b-54fa-81a7-cd22b108476e", "Jose Ventura"),
    22: ("bf74d86c-94cf-5191-92d5-f60b97c64d37", "Lauro Venturi"),
    23: ("432ad6dd-0b72-5c7c-b104-2ea7721abd74", "M P Veran"),
}


ARMY_FINDINGS = {
    2: {
        "date": "1943-07-23",
        "code": "642",
        "occupation": "Occupations in manufacture of paper goods",
        "public_occupation": "paper-goods manufacturing occupation",
        "relationship": "employment",
        "locator": "PDF physical page 173; historical category 6-42",
    },
    6: {
        "date": "1942-11-28",
        "code": "788",
        "occupation": "Warehousing, storekeeping, handling, loading, unloading, and related occupations, not elsewhere classified",
        "public_occupation": "warehousing, storekeeping, handling, loading or unloading occupation, not elsewhere classified",
        "relationship": "employment",
        "locator": "PDF physical page 175; historical category 7-88",
    },
    8: {
        "date": "1943-04-03",
        "code": "992",
        "occupation": "Students",
        "public_occupation": "student",
        "relationship": "student",
        "locator": "PDF physical page 304; corrected historical category 9-92",
    },
    10: {
        "date": "1942-01-12",
        "code": "072",
        "occupation": "Retail managers",
        "public_occupation": "retail manager",
        "relationship": "employment",
        "locator": "PDF physical page 171; historical category 0-72",
    },
    11: {
        "date": "1942-11-04",
        "code": "043",
        "occupation": "Decorators and window dressers",
        "public_occupation": "decorator or window dresser",
        "relationship": "employment",
        "locator": "PDF physical page 171; historical category 0-43",
    },
    13: {
        "date": "1945-12-22",
        "code": "050",
        "occupation": "Laboratory technicians and assistants",
        "public_occupation": "laboratory technician or assistant",
        "relationship": "employment",
        "locator": "PDF physical page 171; historical category 0-50",
    },
    16: {
        "date": "1943-03-10",
        "code": "702",
        "occupation": "Occupations in manufacture of automobiles, not elsewhere classified (semiskilled level)",
        "public_occupation": "semiskilled automobile-manufacturing occupation, not elsewhere classified",
        "relationship": "employment",
        "locator": "PDF physical page 174; historical category 7-02",
    },
    18: {
        "date": "1943-04-14",
        "code": "992",
        "occupation": "Students",
        "public_occupation": "student",
        "relationship": "student",
        "locator": "PDF physical page 304; corrected historical category 9-92",
    },
    21: {
        "date": "1941-01-27",
        "code": "229",
        "occupation": "Kitchen workers in hotels, restaurants, railroads, steamships, and related establishments, not elsewhere classified",
        "public_occupation": "kitchen worker in a hotel, restaurant, railroad, steamship or related establishment, not elsewhere classified",
        "relationship": "employment",
        "locator": "PDF physical page 172; historical category 2-29",
    },
    22: {
        "date": "1943-05-14",
        "code": "992",
        "occupation": "Students",
        "public_occupation": "student",
        "relationship": "student",
        "locator": "PDF physical page 304; corrected historical category 9-92",
    },
}


UNRESOLVED = {
    1: "The protected identifier is shared by a separately printed Edward C Viegel row on page 483. The spelling variant may represent one person, but the rows remain separate pending Box 802 and Box 804 review.",
    3: "A 1940-census discovery lead for a stenographer and a later obituary naming an OSS veteran's wife supply no protected identifier, Box 802 or direct OSS bridge to this row.",
    4: "French military and casualty results for namesakes do not establish the indexed French sergeant's identity, unit or pre-OSS chronology.",
    5: "Puerto Rican military, obituary and genealogy results produced multiple namesakes and no Box 802 or direct OSS bridge.",
    7: "This second printed Anthony J Vella row has no identifier and remains separate from the adjacent identifier-bearing row; name and box alone do not justify a merge or claim transfer.",
    14: "Common-name officer and obituary results did not connect the indexed first lieutenant's officer number and Box 802 to a defensible biography or employer.",
    15: "An airborne roster supports a same-name Army service lead, but it does not establish the sequence into OSS or a prewar employer.",
    17: "Exact-name, OSS, employer, occupation, obituary, institutional and archival searches produced no reliable identity or pre-OSS affiliation bridge.",
    19: "Exact-name and spelling-variant searches produced no reliable wartime identity or pre-OSS affiliation bridge.",
    20: "Exact-name, Italian-name, employer, obituary and archival searches produced no reliable identity or pre-OSS affiliation bridge.",
    23: "The initials-only name is insufficient to distinguish candidates, and reviewed OSS, military, directory and archival searches supplied no corroborating identifier.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Box 802",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 482, rows 1-23; checked against layout-preserving text and an original-detail page render",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate; original spelling and archival context are recoverable while public identifiers are masked.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; twelve Batch 983 identity comparisons; protected identifiers and record ordinals withheld",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "No raw bulk row, record ordinal or full protected identifier enters the evidence bundle or public assets.",
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
            "locator": "PDF physical pages 171-175 and 304; every published Batch 983 category visually and textually checked",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical categories identify status or broad occupation, not a named employer, workplace or exact job title.",
        },
        {
            "key": CAMBRIDGE_VELLA,
            "stable_url": "https://doi.org/10.1017/S002191180008013X",
            "title": "Walter Francis Vella (1924-1980)",
            "author_creator": "Robert Van Niel",
            "repository_publisher": "The Journal of Asian Studies; Cambridge University Press",
            "publication_record_date": "1981-05",
            "locator": "Volume 40, issue 3, page 660; first biographical paragraph; source PDF visually and textually checked",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "The Journal of Asian Studies",
            "document_number": "DOI 10.1017/S002191180008013X",
            "rights_notes": "The obituary explicitly sequences Berkeley enrollment, military service, Army language training and OSS CBI assignment.",
        },
        {
            "key": OSS_SOCIETY_VELLIS,
            "stable_url": "https://www.ossreborn.com/files/OSS_Sum10_Final.pdf",
            "title": "Help Wanted: Alex L. Vellis",
            "author_creator": "Nick Vellis",
            "repository_publisher": "The OSS Society Journal",
            "publication_record_date": "2010",
            "locator": "Summer/Fall 2010, page 77; family research request",
            "access_date": "2026-10-30",
            "source_quality": "D_correlative_or_secondary",
            "collection_name": "The OSS Society Journal",
            "rights_notes": "First-person family testimony is corroborative, not direct personnel-file proof; the transition claim remains qualified.",
        },
        {
            "key": USWM_VELLIS,
            "stable_url": "https://uswarmemorials.org/html/people_details.php?PeopleID=24839",
            "title": "Vellis, Alex L.",
            "author_creator": "U.S. War Memorials",
            "repository_publisher": "U.S. War Memorials",
            "publication_record_date": "Database current at access",
            "locator": "Person record; Greek Operational Group monument linkage and service summary",
            "access_date": "2026-10-30",
            "source_quality": "D_correlative_or_secondary",
            "collection_name": "Greek Operational Group (OSS) Soldier Monument database",
        },
        {
            "key": USWM_MONUMENT,
            "stable_url": "https://www.uswarmemorials.org/html/monument_details.php?MemID=1865&SiteID=1414&file=monument_details.php&page=5",
            "title": "Greek Operational Group (OSS) Soldier Monument",
            "author_creator": "U.S. War Memorials",
            "repository_publisher": "U.S. War Memorials",
            "publication_record_date": "Monument dedicated 2005-05-26; database current at access",
            "locator": "Company C, 2671st Special Reconnaissance Battalion roster; Gus Vellios and Alex Vellis entries",
            "access_date": "2026-10-30",
            "source_quality": "D_correlative_or_secondary",
            "collection_name": "Athens Hellenic Army ALSOS Park memorials",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": ORG_BERKELEY,
            "organization_id": "dd5d0a44-0368-5e91-a5d3-074de36840ed",
            "canonical_name": "University of California, Berkeley",
            "historical_name": "University of California at Berkeley",
            "aliases": ["UC Berkeley", "University of California at Berkeley"],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "Berkeley",
            "state_or_region": "California",
            "country": "United States",
            "normalization_notes": "Student status remains distinct from employment.",
        },
        {
            "key": ORG_ASTP,
            "organization_id": "fca60c0c-b288-54f2-b3a9-5ab0370f00eb",
            "canonical_name": "Army Specialized Training Program",
            "historical_name": "Army Specialized Training Program",
            "aliases": ["ASTP"],
            "organization_type": "military training program",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "An Army training assignment, not a civilian employer or university affiliation unless separately documented.",
        },
        {
            "key": ORG_GREEK_OG,
            "organization_id": "5672671e-db84-554a-aefd-469d60722262",
            "canonical_name": "OSS Greek Operational Group",
            "historical_name": "Company C, 2671st Special Reconnaissance Battalion",
            "aliases": ["Greek Battalion", "Greek/US Operational Group", "Operational Group III"],
            "organization_type": "military and OSS operational unit",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "The wartime designation is preserved; this assignment is not a civilian employer.",
        },
    ]


def army_identity_note(row: int) -> str:
    if row == 11:
        return "The nonshared protected identifier agrees exactly; the official Army form prints Gus while the index prints Guss, and the rare-name monument entry independently supports Gus Vellios."
    return "The official Army and indexed full names agree and the protected identifier is nonshared."


def occupation_affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, item in ARMY_FINDINGS.items():
        values.append(
            {
                "key": f"{slug(PEOPLE[row][1])}-occupation-b983-row{row}",
                "person_id": PEOPLE[row][0],
                "occupation": item["public_occupation"],
                "relationship_type": item["relationship"],
                "start_date": item["date"],
                "end_date": item["date"],
                "date_precision": "Dated at Army entry; the historical category names no employer, school, workplace, duration or precise OSS-transfer date",
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
    return values


def affiliations() -> list[dict[str, object]]:
    values = occupation_affiliations()
    values.extend(
        [
            {
                "key": "walter-vella-berkeley-student-b983",
                "person_id": PEOPLE[8][0],
                "organization_key": ORG_BERKELEY,
                "organization_name_as_found": "University of California at Berkeley",
                "role_title": "student",
                "relationship_type": "student",
                "start_date": "1942",
                "end_date": "1942",
                "date_precision": "Entered in 1942 and was soon drawn into military service; exact dates are not supplied",
                "city": "Berkeley",
                "state_or_region": "California",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "confirmed",
                "claim_confidence": "high",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "published",
                "research_notes": "Last documented civilian status before military service. Berkeley is not labeled an employer.",
            },
            {
                "key": "walter-vella-astp-b983",
                "person_id": PEOPLE[8][0],
                "organization_key": ORG_ASTP,
                "organization_name_as_found": "ASTP program",
                "role_title": "Thai-language trainee",
                "relationship_type": "military_assignment",
                "start_date": "1942 or later",
                "end_date": "Before OSS CBI assignment",
                "date_precision": "The obituary gives the explicit ASTP-to-OSS sequence but not exact transfer dates",
                "country": "United States",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "explicit_immediate",
                "identity_confidence": "confirmed",
                "claim_confidence": "high",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "published",
                "research_notes": "Immediate documented military training assignment before OSS CBI service; not a civilian employer.",
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


def army_claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, item in ARMY_FINDINGS.items():
        name = PEOPLE[row][1]
        identity_sources = [
            {"source_key": INDEX},
            {"source_key": ARMY, "locator_override": "Accepted identity bridge; protected identifier and raw record withheld"},
        ]
        if row == 11:
            identity_sources.append(
                {"source_key": USWM_MONUMENT, "locator_override": "Company C roster; Gus Vellios entry"}
            )
        values.append(
            claim(
                row,
                f"identity-{slug(name)}-army-b983-row{row}",
                "identity",
                f"Indexed {name} is high-confidence matched to the official Army entry used for the dated occupation finding.",
                "The official name comparison and a nonshared protected-identifier agreement support the match.",
                army_identity_note(row),
                "The Army entry date is preserved separately from later OSS-index context.",
                "A_direct_official",
                "high",
                identity_sources,
                "Protected identifiers were used only for private resolution and remain absent from the evidence bundle and public output.",
            )
        )
        claim_type = "other_pre_oss_affiliation" if item["relationship"] == "student" else "occupation"
        values.append(
            claim(
                row,
                f"occupation-{slug(name)}-b983-row{row}",
                claim_type,
                f"At Army entry on {item['date']}, {name}'s historical civilian category was {str(item['occupation']).lower()}.",
                f"The official Army field carries historical code {item['code']}; NARA's code list defines it as {item['occupation']}.",
                army_identity_note(row),
                "Dated at Army entry before the later OSS-index context; no named employer, workplace, duration or exact OSS-transfer date is supplied.",
                "A_direct_official",
                "medium",
                [
                    {"source_key": ARMY, "locator_override": "Accepted identity bridge; protected identifier and raw record withheld"},
                    {"source_key": TECH, "locator_override": "PDF physical pages 44-46; civilian-occupation field"},
                    {"source_key": CODES, "locator_override": str(item["locator"])},
                ],
                "Published as a qualified historical category only; excluded from verified-employer analytics.",
                f"{slug(name)}-occupation-b983-row{row}",
                "publish_qualified",
            )
        )
    return values


def special_claims() -> list[dict[str, object]]:
    return [
        claim(
            8,
            "identity-walter-francis-vella-b983",
            "identity",
            "Indexed Walter F Vella is confirmed as historian Walter Francis Vella, who served with the OSS in the China-Burma-India theater.",
            "A scholarly obituary supplies his full name and explicit Berkeley-to-military-to-OSS chronology; the index and Army files add exact-name and protected-identifier agreement.",
            "Confirmed by the exact indexed and Army name, nonshared protected identifier, expanded middle name, student chronology and explicit OSS CBI service.",
            "The obituary places Berkeley and Army language training before the OSS assignment.",
            "C_reputable_contemporary_or_scholarly",
            "confirmed",
            [
                {"source_key": INDEX},
                {"source_key": ARMY, "locator_override": "Exact nonshared protected-identifier comparison; raw value withheld"},
                {"source_key": CAMBRIDGE_VELLA, "locator_override": "Page 660; first biographical paragraph"},
            ],
            "The source sequence is explicit and independently anchored by the official protected-identifier crosswalk.",
        ),
        claim(
            8,
            "last-civilian-walter-vella-berkeley-b983",
            "other_pre_oss_affiliation",
            "Walter Francis Vella was a student at the University of California at Berkeley immediately before entering military service in 1942.",
            "The obituary says he entered Berkeley in 1942 and was soon drawn into military service.",
            "Confirmed Walter Francis Vella identity.",
            "Strongly date-bounded as the last documented civilian status before military service; Berkeley is not an employer.",
            "C_reputable_contemporary_or_scholarly",
            "high",
            [
                {
                    "source_key": CAMBRIDGE_VELLA,
                    "excerpt_override": "entered the University of California at Berkeley in 1942 but was soon drawn into military service",
                }
            ],
            "Published as student status, not employment, and excluded from verified-employer counts.",
            "walter-vella-berkeley-student-b983",
        ),
        claim(
            8,
            "immediate-walter-vella-astp-b983",
            "immediate_pre_oss_affiliation",
            "Walter Francis Vella's immediate documented pre-OSS assignment was Thai-language training in the Army Specialized Training Program.",
            "The obituary explicitly sequences ASTP Thai-language study and then assignment to OSS service in the China-Burma-India theater.",
            "Confirmed Walter Francis Vella identity.",
            "Explicit immediate sequence, although exact transfer dates are not supplied.",
            "C_reputable_contemporary_or_scholarly",
            "high",
            [
                {
                    "source_key": CAMBRIDGE_VELLA,
                    "excerpt_override": "Placed in an ASTP program, he began his study of Thai language and was then assigned to serve with the OSS",
                }
            ],
            "Military training assignment, not a civilian employer.",
            "walter-vella-astp-b983",
        ),
        claim(
            12,
            "identity-alex-vellis-greek-og-b983",
            "identity",
            "Indexed Alex L Vellis is high-confidence matched to the Greek Operational Group veteran recorded by the Athens memorial project.",
            "The rare exact name and nonshared protected identifier agree with the Army record; memorial and family sources independently place Alex L. Vellis in the Greek operational unit.",
            "High confidence from rare exact name, nonshared protected identifier and two concordant Greek Operational Group sources.",
            "The sources document wartime service but do not establish a civilian employer or a fully audited pre-OSS transfer date.",
            "D_correlative_or_secondary",
            "high",
            [
                {"source_key": INDEX},
                {"source_key": ARMY, "locator_override": "Exact nonshared protected-identifier comparison; code 993 left uninterpreted"},
                {"source_key": USWM_VELLIS},
                {
                    "source_key": OSS_SOCIETY_VELLIS,
                    "excerpt_override": "served in Company C ... was later assigned to the OSS and served in Operational Group III",
                },
            ],
            "The family transition account remains corroborative. Box 802 is required before publishing a settled immediate-predecessor claim.",
        ),
    ]


def claims() -> list[dict[str, object]]:
    return army_claims() + special_claims()


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
    categories = {
        1: "unknown_or_indeterminate",
        3: "unknown_or_indeterminate",
        4: "foreign_or_allied_military_personnel",
        5: "unknown_or_indeterminate",
        7: "unknown_or_indeterminate",
        14: "commissioned_army_officer",
        15: "enlisted_army_personnel",
        17: "unknown_or_indeterminate",
        19: "unknown_or_indeterminate",
        20: "unknown_or_indeterminate",
        23: "unknown_or_indeterminate",
    }
    for row, reason in UNRESOLVED.items():
        values.append(
            base_update(
                row,
                identity_status="ambiguous" if row in {1, 7} else "unresolved",
                identity_evidence=f"The visually verified page 482 row supplies {PEOPLE[row][1]}, Box 802 and archive location 230/86/42/05. {reason}",
                personnel_category=categories[row],
                commissioned_officer=True if row == 14 else False,
                allied_or_foreign_personnel=True if row == 4 else False,
                possible_duplicate_group=(
                    "p482-anthony-j-vella-rows6-7-b983" if row == 7 else None
                ),
                research_status="requires_archival_review",
                next_action=f"Review Box 802 for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}",
            )
        )

    for row in ARMY_FINDINGS:
        if row == 10:
            continue
        item = ARMY_FINDINGS[row]
        status = "completed" if row == 8 else "occupation_only_found"
        identity_status = "confirmed" if row == 8 else "high_confidence"
        values.append(
            base_update(
                row,
                identity_status=identity_status,
                identity_evidence=(
                    "The exact indexed and Army name, nonshared protected identifier, scholarly expanded name and explicit Berkeley-to-ASTP-to-OSS chronology confirm Walter Francis Vella."
                    if row == 8
                    else army_identity_note(row)
                ),
                name_variants=(
                    ["Walter Francis Vella"]
                    if row == 8
                    else (["Gus Vellios"] if row == 11 else None)
                ),
                personnel_category="enlisted_army_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                possible_duplicate_group=(
                    "p482-anthony-j-vella-rows6-7-b983" if row == 6 else None
                ),
                research_status=status,
                next_action=(
                    "Research protocol completed: Berkeley student status and the ASTP-to-OSS sequence are documented. Review Box 802 only to refine exact dates or identify any separate civilian employment."
                    if row == 8
                    else f"Review Box 802 to identify the named employer or institution behind historical category {item['code']} and establish the precise Army-to-OSS chronology."
                ),
                nara_catalog_id="1263923",
                archival_review_priority="medium" if row == 8 else "high",
            )
        )

    values.append(
        base_update(
            12,
            identity_status="high_confidence",
            identity_evidence="The rare exact indexed and Army name and nonshared protected identifier agree; two independent memorial/family sources identify Alex L. Vellis with the Greek Operational Group.",
            personnel_category="enlisted_army_personnel",
            commissioned_officer=False,
            allied_or_foreign_personnel=False,
            research_status="requires_archival_review",
            next_action="Review Box 802 to verify the Company C-to-Operational Group III chronology and identify the last civilian employer or status; code 993 remains uninterpreted.",
            nara_catalog_id="1263923",
        )
    )
    return values


def research_attempts() -> list[dict[str, object]]:
    reviewed = set(ARMY_FINDINGS) | {12}
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        if row == 9:
            continue
        if row in reviewed:
            outcome = "source_reviewed"
            sources_reviewed = 8 if row in {8, 11, 12} else 6
            rejected = 3
            detail = "Reviewed official and corroborating sources produced the identity, dated occupation, student or military-training outcome recorded in the bundle."
        elif row in UNRESOLVED:
            outcome = "no_result"
            sources_reviewed = 5
            rejected = 5
            detail = UNRESOLVED[row]
        else:
            # Moritz Velleman's prior public identity and pathway remain intact;
            # this attempt records only the newly reviewed Army occupation field.
            outcome = "source_reviewed"
            sources_reviewed = 4
            rejected = 0
            detail = "Supplemental official Army review adds a dated retail-manager category without changing the existing documented U.S. Army, French Army and Lisbon-office pathway."

        attempts.append(
            {
                "key": f"page482-row{row}-{slug(name)}-b983",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index and official Archives context; CIA Reading Room or equivalent official-source check; exact-name and meaningful variants; OSS, Army, rank, branch and assignment clues; employer and occupation 1940; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Box 802; protected identifiers used only in private official-record comparison",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_983",
                "started_at": "2026-10-30T22:10:00Z",
                "completed_at": "2026-10-31T00:05:00Z",
                "outcome": outcome,
                "sources_reviewed": sources_reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, snippets, commercial people-finder pages, relatives, unsourced genealogy, postwar-only leads and sources without an OSS, protected-identifier, rank, unit or personnel-file bridge were rejected. Historical occupation categories and military assignments were not converted into employers.",
                "research_notes": f"{detail} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain and archival searches were checked as applicable. The index page, official Army bulk comparison, technical field definitions and code-list pages were inspected directly. The Walter Francis Vella obituary was visually and textually checked; Alex Vellis and Gus Vellios unit sources were reviewed in context. No search-result snippet was used as sole final evidence, no paywall or access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": "Review the indexed Box 802 personnel file for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before wartime service.",
                "attempt_number": 2 if row == 10 else 1,
                "research_agent_version": "before-oss-b983-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-983-v1",
        "reviewer": "Before OSS Batch 983 evidence review",
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
