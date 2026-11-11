#!/usr/bin/env python3
"""Generate the reviewed Batch 1053 evidence bundle for PDF page 308."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page308-robert-h-mcdowell-to-william-m-mcghee-review_"
    "batch-1053_2026-11-11.json"
)

INDEX = "nara-index-b1053"
ARMY = "army-bulk-b1053"
TECH = "army-tech-b1053"
CODES = "army-codes-b1053"
SHIELD = "phi-kappa-psi-shield-b1053"
NEBRASKA = "nebraska-education-directory-b1053"
OBITUARY = "kathleen-mcferren-obituary-b1053"
HASTINGS = "hastings-college-alumni-b1053"


# Rows 19/20 and 21/22 are two pairs of printed rows linked to one cautiously
# resolved person each. Every source row remains preserved in source_records.
PEOPLE = {
    1: ("1cb3c8c2-0bb8-5965-9501-3b434a8f3abb", "Robert H McDowell", "503"),
    2: ("87967ad6-aa66-522a-ac55-31358b684ed6", "Richard W McEachern", "504"),
    3: ("b66de25f-cb93-5205-a36c-c8649c6a6ad8", "Virgina S McEachern", "504"),
    4: ("65432428-1a0a-55da-816c-f2251cf8ef5a", "Nelson C McEdward", "504"),
    5: ("a4bba57b-2235-5848-ac27-c9012ea69fd8", "Albert B McElhoe", "504"),
    6: ("7ab9338b-1ec0-5e60-88e6-d9d123907b4d", "Edward C McElroy", "504"),
    7: ("94d28ca4-f11b-59f3-8691-3ff347ee1603", "Madeline C McElroy", "504"),
    8: ("a05711f3-9996-5452-852c-efb0ef9807e1", "Roland H McElroy", "504"),
    9: ("a72babc9-ce39-532e-97ce-888a1f71768d", "William J McElroy", "504"),
    10: ("38c8f27f-a524-597c-9460-78e430a04d9d", "William P McEneaney", "504"),
    11: ("5b6fffc3-d4a0-5ac6-98d1-5a0571177a1d", "Leroy McEntire", "504"),
    12: ("9b0ab9f5-a7eb-5871-9dd6-acf23188aae3", "Hoeph E McEvan", "504"),
    13: ("68436ed6-79ed-5d42-b9c3-7fe532e447a5", "Arthur M McEvay", "504"),
    14: ("33e11ddf-f7b7-588d-8282-66296e3a9df7", "Dennis McEvoy", "504"),
    15: ("25fb8370-9e09-5739-80e0-b931202edacf", "Joseph E McEwan", "504"),
    16: ("43e65fcd-5b93-58f7-b693-51f0f5541fcc", "Charles W McFadden", "504"),
    17: ("ff56088c-b8cd-512b-88e7-a69a681808c3", "Elizabeth T McFadden", "504"),
    18: ("b4da83c6-ae04-5434-a232-cab6c3ddc305", "George H McFadden", "504"),
    19: ("b2850942-a685-52d7-bb47-43a368d1b665", "Robert D McFadden", "504"),
    20: ("b2850942-a685-52d7-bb47-43a368d1b665", "Robert D McFadden", "504"),
    21: ("bc76141a-950f-5e91-8578-a9b74be39d47", "Stuart P McFadden", "504"),
    22: ("bc76141a-950f-5e91-8578-a9b74be39d47", "Stuart P McFadden", "504"),
    23: ("6617d4ef-b5b4-537d-a389-c1c80909e4d1", "Thomas J McFadden", "504"),
    24: ("c7305cd7-23c2-54f5-989e-7a2156333733", "Lawerence B McFaddin", "504"),
    25: ("10aeb551-a334-5bf2-966a-44b1188202ff", "Neil McFadyen", "504"),
    26: ("6b8e782a-5b29-5d33-a730-501bf048dbc7", "Dallas A McFarland", "504"),
    27: ("33aa76dc-133f-5548-b257-1af31badcdfa", "Frank A McFarland", "505"),
    28: ("835bb837-5b5f-5ccd-a6a5-68108180ebb5", "Jack McFarland", "505"),
    29: ("0ae71579-ad1a-559a-99f1-44b79aaa47d7", "Kenneth R McFarland", "505"),
    30: ("bd9a40e8-7409-547d-a706-5e0449bc4698", "Maynard McFarlane", "505"),
    31: ("aa8c1b8c-452c-5633-8e9a-b708b6f385cd", "Phyllis M McFarlane", "505"),
    32: ("1aee67a4-b38b-5ebd-84ec-086909f10cad", "Darel D McFerren", "505"),
    33: ("4d6eb7f9-83b2-567a-aa76-25683a32d761", "William C McGaragle", "505"),
    34: ("42986f6e-6650-55bc-8600-c28ba3928a8a", "William D McGarry", "505"),
    35: ("806e928a-6bb1-5935-a8cc-258cb69cbdf6", "Edward A McGaughy", "505"),
    36: ("73bc3437-460f-5c09-9903-82b581914e1e", "Edward McGaughy", "505"),
    37: ("c731cbb9-43ca-55d2-840e-98d9265dd4c9", "Frank McGavock", "505"),
    38: ("80460459-4d0f-5e93-996f-7d5c203d9cfe", "James A McGay", "505"),
    39: ("74bf9c95-6e09-5abd-91f7-030c8f9a73ef", "James M McGee", "505"),
    40: ("6c35b80e-0504-545c-985a-97bffa274e55", "John R McGee", "505"),
    41: ("2eddcd14-4226-55e9-9e42-22e3f23d0bdb", "Mary E McGee", "505"),
    42: ("faca659d-eb88-5a89-9191-53fa2c00fc12", "Meredith C McGee", "505"),
    43: ("f134f978-8244-5d89-9ccb-156d80d0bcb6", "Charles B McGehee", "505"),
    44: ("aee6f423-0fe3-5673-acf7-828279715655", "Philip McGevna", "505"),
    45: ("2173b96f-f737-577e-a6ec-2aa37a333e42", "Harvey D McGhee", "505"),
    46: ("88d785e5-31e0-5452-bfd1-8ea5e71cd9ac", "William M McGhee", "505"),
}

UNIQUE_ROWS = [row for row in PEOPLE if row not in {20, 22}]

# Nonshared, wartime-dated Army links with a defined occupation code. Codes
# 993 and 999 are absent from the reviewed official list and are not interpreted.
ARMY_OCCUPATIONS = {
    16: ("1942-11-04", "185", "sales agent, except to consumers", "Agents, sales, except to consumers", "unknown", "PDF physical page 175; historical code 1-85"),
    21: ("1941-02-10", "081", "advertising agent", "Advertising agents", "unknown", "PDF physical page 171; historical code 0-81"),
    25: ("1943-05-27", "992", "student", "Students", "student", "PDF physical page 304; corrected historical code 9-92"),
    28: ("1944-06-16", "579", "railroad or car-shop mechanic or repairman", "Mechanics and repairmen, railroad and carshop", "unknown", "PDF physical page 175; historical code 5-79"),
    37: ("1943-12-13", "992", "student", "Students", "student", "PDF physical page 304; corrected historical code 9-92"),
    38: ("1942-12-04", "105", "general office clerk", "Clerks, general office", "unknown", "PDF physical page 171; historical code 1-05"),
    40: ("1942-09-19", "644", "compositor or typesetter", "Compositors and typesetters", "unknown", "PDF physical page 173; historical code 6-44"),
    44: ("1942-11-16", "148", "agent or appraiser, not elsewhere classified", "Agents and appraisers, n.e.c.", "unknown", "PDF physical page 171; historical code 1-48"),
    45: ("1943-05-15", "636", "furniture-manufacturing occupation, not elsewhere classified", "Occupations in manufacture of furniture, n.e.c.", "unknown", "PDF physical page 173; historical code 6-36"),
    46: ("1942-12-14", "118", "general industry clerk", "General industry clerks", "unknown", "PDF physical page 171; historical code 1-18"),
}

ARMY_IDENTITY_ONLY = {24, 26}
CONFLICT_ROWS = {6}
AMBIGUOUS_ROWS = {33, 35, 36}

ATTEMPT_NUMBERS = {
    1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 3, 7: 2, 8: 2, 9: 3,
    10: 2, 11: 2, 12: 2, 13: 2, 14: 2, 15: 2, 16: 4, 17: 2,
    18: 3, 19: 2, 21: 3, 23: 2, 24: 3, 25: 3, 26: 4, 27: 2,
    28: 4, 29: 2, 30: 2, 31: 2, 32: 2, 33: 3, 34: 3, 35: 3,
    36: 3, 37: 3, 38: 3, 39: 3, 40: 4, 41: 3, 42: 2, 43: 3,
    44: 3, 45: 4, 46: 4,
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
            archival_identifier="RG 226, Entry A1-224, Boxes 503-505",
            title="OSS Personnel Files from Excel",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="2010-12-23",
            locator="PDF page 308, rows 1-46; every printed row visually checked against the official PDF",
            source_quality="A_direct_official",
            collection_name="Records of the Office of Strategic Services, Record Group 226",
            rights_notes="All 46 printed rows remain preserved; rows 19/20 and 21/22 each link to one person entity. Full protected identifiers remain private.",
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
            rights_notes="No raw record, protected identifier, or bulk ordinal is retained in public assets. Shared, conflicting, and undefined-code links are withheld from occupation claims.",
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
            locator="PDF physical pages 171, 173, 175, and 304; all ten published Batch 1053 categories visually checked",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records technical documentation",
            rights_notes="Categories identify neither employer nor exact Army-to-OSS sequence. Codes 993 and 999 are absent and remain uninterpreted.",
        ),
        source(
            SHIELD,
            stable_url="https://www.phikappapsi.com/wp-content/uploads/2019/06/1941-42_vol62_no1-4.pdf",
            archival_identifier="The Shield of Phi Kappa Psi, volume 62",
            title="The Shield of Phi Kappa Psi, Volume LXII, 1941-1942",
            author_creator="Phi Kappa Psi",
            repository_publisher="Phi Kappa Psi",
            publication_record_date="1941-11",
            locator="PDF physical page 57, printed page 55, Indiana Beta—Indiana University newsletter",
            source_quality="B_authoritative_institutional",
            collection_name="The Shield of Phi Kappa Psi",
            rights_notes="Only a short paraphrase and citation are retained; the source documents a student and fraternity affiliation, not employment.",
        ),
        source(
            NEBRASKA,
            stable_url="https://govdocs.nebraska.gov/epubs/E2200/D001-193233.pdf",
            archival_identifier="Nebraska Department of Public Instruction, 1932-1933 educational directory",
            title="Nebraska Educational Directory, 1932-1933",
            author_creator="Nebraska Department of Public Instruction",
            repository_publisher="Nebraska State Government Publications Online",
            publication_record_date="1932",
            locator="PDF physical page 53, printed page 52; Gordon, Sheridan County continuation; abbreviation key on printed page 8",
            source_quality="A_direct_official",
            collection_name="Nebraska educational directories",
            rights_notes="The official directory defines H as History and Ec as Economics and lists two years in the position including 1932-33.",
        ),
        source(
            OBITUARY,
            stable_url="https://www.genealogybuff.com/ne/adams/webbbs_config.pl/noframes/read/23",
            archival_identifier="Adams County, Nebraska obituary collection, Kathleen McFerren",
            title="Kathleen McFerren obituary",
            author_creator="Creator not stated; obituary collection from area funeral homes",
            repository_publisher="GenealogyBuff.com",
            publication_record_date="1997-01",
            locator="Kathleen McFerren obituary, paragraphs describing marriage and 1937-42 mission-school service",
            source_quality="D_correlative_or_secondary",
            collection_name="Adams County, Nebraska Obituary and Death Notice Collection",
            rights_notes="The short project-authored paraphrase is qualified because the accessible page republishes an obituary and does not state an original newspaper title.",
        ),
        source(
            HASTINGS,
            stable_url="https://www.hastings.edu/alumni/alumni-connections/outstanding-alumni-and-young-alumni/",
            archival_identifier="Hastings College Outstanding Alumni, 1977",
            title="Outstanding Alumni and Young Alumni",
            author_creator="Hastings College",
            repository_publisher="Hastings College",
            publication_record_date="current institutional page; 1977 award entry",
            locator="1977: Darel D. McFerren '31",
            source_quality="B_authoritative_institutional",
            collection_name="Hastings College alumni records",
            rights_notes="Used to corroborate the distinctive full name and prewar Nebraska educational context; it does not by itself establish OSS identity or employment.",
        ),
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": "indiana-university-b1053",
            "canonical_name": "Indiana University",
            "historical_name": "Indiana University",
            "aliases": ["Indiana University Bloomington"],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "Bloomington",
            "state_or_region": "Indiana",
            "country": "United States",
            "active_dates": "1820-present",
            "normalization_notes": "The 1941 source heading reads Indiana Beta—Indiana University; the modern campus qualifier is retained only as an alias.",
        },
        {
            "key": "phi-kappa-psi-indiana-beta-b1053",
            "canonical_name": "Phi Kappa Psi, Indiana Beta chapter",
            "historical_name": "Indiana Beta of Phi Kappa Psi",
            "aliases": ["Indiana Beta", "Phi Psi at Indiana University"],
            "organization_type": "student fraternity chapter",
            "sector": "labor_nonprofit_and_religion",
            "city": "Bloomington",
            "state_or_region": "Indiana",
            "country": "United States",
            "normalization_notes": "Kept separate from Indiana University because a fraternity affiliation is not the same relationship as university attendance.",
        },
        {
            "key": "gordon-high-school-nebraska-b1053",
            "canonical_name": "Gordon High School",
            "historical_name": "Gordon High School",
            "organization_type": "public high school",
            "sector": "academia_and_research",
            "city": "Gordon",
            "state_or_region": "Nebraska",
            "country": "United States",
            "active_dates": "active in 1932-1933",
            "normalization_notes": "The directory lists the school under Gordon, Sheridan County; no modern successor is asserted.",
        },
        {
            "key": "methodist-mission-school-medan-b1053",
            "canonical_name": "Methodist Mission School, Medan",
            "historical_name": "Methodist Mission School in Medan, Sumatra, Indonesia",
            "aliases": [],
            "organization_type": "mission school",
            "sector": "academia_and_research",
            "city": "Medan",
            "state_or_region": "Sumatra",
            "country": "Indonesia",
            "active_dates": "documented in 1937-1942",
            "normalization_notes": "The source wording is preserved; no modern successor, parent denomination, or legal entity is inferred.",
        },
    ]


def army_affiliation_key(row: int) -> str:
    return f"{slug(PEOPLE[row][1])}-army-entry-occupation-b1053"


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
    values.extend(
        [
            {
                "key": "lawrence-b-mcfaddin-indiana-university-b1053",
                "person_id": PEOPLE[24][0],
                "organization_key": "indiana-university-b1053",
                "organization_name_as_found": "Indiana University",
                "role_title": "student",
                "occupation": "student",
                "relationship_type": "student",
                "end_date": "1941-11",
                "date_precision": "The November 1941 chapter newsletter lists Lawrence McFaddin in the Indiana University pledge class.",
                "city": "Bloomington",
                "state_or_region": "Indiana",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "This is an institutional student affiliation, not an employer claim. The source spells Lawrence correctly while the index prints Lawerence.",
            },
            {
                "key": "lawrence-b-mcfaddin-phi-kappa-psi-b1053",
                "person_id": PEOPLE[24][0],
                "organization_key": "phi-kappa-psi-indiana-beta-b1053",
                "organization_name_as_found": "Indiana Beta",
                "role_title": "pledgee",
                "relationship_type": "professional_affiliation",
                "end_date": "1941-11",
                "date_precision": "Documented in the November 1941 issue; no initiation date is asserted.",
                "city": "Bloomington",
                "state_or_region": "Indiana",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Fraternity affiliation is modeled separately from university attendance and is not counted as employment.",
            },
            {
                "key": "darel-d-mcferren-gordon-high-school-b1053",
                "person_id": PEOPLE[32][0],
                "organization_key": "gordon-high-school-nebraska-b1053",
                "organization_name_as_found": "Gordon High School",
                "role_title": "history and economics teacher",
                "occupation": "teacher",
                "relationship_type": "employment",
                "start_date": "1932",
                "end_date": "1933",
                "date_precision": "The 1932-33 directory lists two years in the position including that school year; exact appointment and departure dates are not stated.",
                "city": "Gordon",
                "state_or_region": "Nebraska",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "A_direct_official",
                "publication_status": "published",
                "research_notes": "The directory abbreviation key defines H as History and Ec as Economics. This earlier job is not represented as the immediate pre-OSS role.",
            },
            {
                "key": "darel-d-mcferren-methodist-mission-school-b1053",
                "person_id": PEOPLE[32][0],
                "organization_key": "methodist-mission-school-medan-b1053",
                "organization_name_as_found": "Methodist Mission School in Medan, Sumatra, Indonesia",
                "role_title": "teacher and administrator",
                "occupation": "teacher and school administrator",
                "relationship_type": "employment",
                "start_date": "1937",
                "end_date": "1942",
                "date_precision": "A later obituary reports the 1937-42 range; exact dates and an OSS-entry date are not supplied.",
                "city": "Medan",
                "state_or_region": "Sumatra",
                "country": "Indonesia",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "D_correlative_or_secondary",
                "publication_status": "publish_qualified",
                "research_notes": "This is the best-supported last civilian role currently found, but it is qualified because the accessible source is a later spouse obituary and does not state when OSS service began.",
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
        values.append(
            claim(
                f"army-entry-{slug(PEOPLE[row][1])}-b1053",
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
    values.extend(
        [
            claim(
                "lawrence-b-mcfaddin-indiana-university-student-b1053",
                24,
                "other_pre_oss_affiliation",
                "Lawrence B. McFaddin was documented as a student at Indiana University in November 1941.",
                "The Indiana Beta newsletter is headed Indiana University and includes Lawrence McFaddin among its pledge class.",
                "The distinctive full name and middle initial agree with the indexed row after correcting the index's Lawerence spelling, and an existing official Army linkage independently uses Lawrence B. McFaddin.",
                "The November 1941 issue is prewar and predates his December 1942 Army entry, but it does not establish the immediate pre-OSS sequence.",
                "B_authoritative_institutional",
                "high",
                "published",
                "Modeled as student status, never as employment; Lawrence is retained as a documented name variant rather than silently overwriting the index.",
                [{"source_key": SHIELD}, {"source_key": INDEX, "support_type": "context_only"}, {"source_key": ARMY, "support_type": "context_only"}],
                "lawrence-b-mcfaddin-indiana-university-b1053",
                "Our twenty-eight pledgees are: Lawrence McFaddin",
            ),
            claim(
                "lawrence-b-mcfaddin-phi-kappa-psi-b1053",
                24,
                "other_pre_oss_affiliation",
                "Lawrence B. McFaddin was an Indiana Beta pledge of Phi Kappa Psi in November 1941.",
                "The Indiana University chapter newsletter explicitly names Lawrence McFaddin in its pledge class.",
                "The distinctive full name and initial agree with the official Army-linked variant of the indexed person.",
                "The issue fixes the affiliation to November 1941 but does not establish how long it continued.",
                "B_authoritative_institutional",
                "high",
                "published",
                "Fraternity affiliation is kept separate from university attendance and from employment.",
                [{"source_key": SHIELD}, {"source_key": INDEX, "support_type": "context_only"}],
                "lawrence-b-mcfaddin-phi-kappa-psi-b1053",
            ),
            claim(
                "identity-darel-d-mcferren-b1053",
                32,
                "identity",
                "The indexed Darel D. McFerren has a high-confidence identity match to the Nebraska educator and later Hastings College alumnus documented in the reviewed sources.",
                "The exact uncommon full name appears in the OSS index and Hastings College record; the official directory independently places Darel McFerren in the same Nebraska educational career before the war.",
                "High confidence from the uncommon exact full name with middle initial and a coherent Nebraska and Southeast Asia chronology across independent official and institutional sources.",
                "The sources document identity and prewar chronology but do not state an OSS entry date.",
                "B_authoritative_institutional",
                "high",
                "published",
                "No protected identifier or relative is used as the principal match; the spouse obituary is corroborative and supports the mission-school role.",
                [{"source_key": INDEX}, {"source_key": HASTINGS}, {"source_key": NEBRASKA, "support_type": "context_only"}],
            ),
            claim(
                "darel-d-mcferren-gordon-high-school-b1053",
                32,
                "other_pre_oss_affiliation",
                "Darel D. McFerren taught history and economics at Gordon High School in Nebraska during the 1932-33 school year.",
                "Nebraska's official directory lists Darel McFerren under Gordon High School with H and Ec subjects, two years in position, and a salary.",
                "The unusual name and Nebraska educator chronology agree with the indexed Darel D. McFerren and Hastings College's exact-name alumni record.",
                "This is explicitly documented prewar employment, but later employment intervened before OSS service.",
                "A_direct_official",
                "high",
                "published",
                "The source abbreviation key defines H as History and Ec as Economics; the job is not labeled immediate pre-OSS or last civilian employment.",
                [{"source_key": NEBRASKA}, {"source_key": HASTINGS, "support_type": "context_only"}, {"source_key": INDEX, "support_type": "context_only"}],
                "darel-d-mcferren-gordon-high-school-b1053",
            ),
            claim(
                "darel-d-mcferren-methodist-mission-school-b1053",
                32,
                "last_civilian_pre_service",
                "The best current evidence indicates that Darel D. McFerren taught and administered the Methodist Mission School in Medan from 1937 to 1942, his last documented civilian role before wartime service.",
                "A later obituary reports that Darel and Kathleen McFerren taught and administered the Medan mission school from 1937 until their 1942 evacuation.",
                "The exact full name, spouse, Hastings context, Southeast Asia chronology, and independent institutional record support the match; the employment statement is nevertheless from a later obituary.",
                "The role ends in 1942 and is strongly date-bounded before wartime service, but no reviewed source explicitly says he left it to join OSS.",
                "D_correlative_or_secondary",
                "medium",
                "publish_qualified",
                "Published with visible qualification; it is not marked immediate pre-OSS and remains eligible for upgrade after personnel-file or contemporary mission-record review.",
                [{"source_key": OBITUARY}, {"source_key": HASTINGS, "support_type": "context_only"}, {"source_key": INDEX, "support_type": "context_only"}],
                "darel-d-mcferren-methodist-mission-school-b1053",
                "They taught and administered the Methodist Mission School in Medan, Sumatra, Indonesia from 1937-42.",
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
    for row in UNIQUE_ROWS:
        person_id, name, box = PEOPLE[row]
        update: dict[str, object] = {
            "person_id": person_id,
            "manual_review_required": True,
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
        }
        if row in ARMY_OCCUPATIONS:
            update.update(
                identity_status="high_confidence",
                identity_evidence="The official index and Army entry agree in name and a reviewed nonshared private identifier. The identifier remains private; the dated broad occupation does not establish an employer or OSS sequence.",
                nara_catalog_id="1263923",
                research_status="occupation_only_found",
                next_action=f"Review Box {box} for a named employer or institution and establish the Army-to-OSS chronology.",
                archival_review_priority="high",
            )
        elif row == 24:
            update.update(
                identity_status="high_confidence",
                identity_evidence="The official Army entry uses Lawrence B. McFaddin, and a contemporary Indiana University chapter source independently names Lawrence McFaddin. The OSS index's Lawerence spelling is preserved as printed.",
                name_variants=["Lawrence B McFaddin", "Lawrence McFaddin"],
                nara_catalog_id="1263923",
                research_status="occupation_only_found",
                next_action="Review Box 504 to identify a named employer or later civilian role and establish the Indiana University-to-Army-to-OSS chronology; Army occupation code 993 remains undefined.",
                archival_review_priority="high",
            )
        elif row == 26:
            update.update(
                identity_status="high_confidence",
                identity_evidence="The official index and Army entry agree in name and a reviewed nonshared private identifier. Historical occupation code 999 is absent from the reviewed official list and is not interpreted.",
                nara_catalog_id="1263923",
                research_status="requires_archival_review",
                next_action="Review Box 504 to identify Dallas A. McFarland's civilian occupation, employer, and Army-to-OSS chronology; undefined code 999 supplies no defensible occupation.",
                archival_review_priority="high",
            )
        elif row == 32:
            update.update(
                identity_status="high_confidence",
                identity_evidence="The uncommon exact full name and coherent Nebraska educator and Southeast Asia chronology across independent official and institutional sources support a high-confidence match.",
                research_status="documented_prewar_employer_found",
                next_action="Review Box 505 and contemporary Methodist mission records to confirm whether the Medan school was the immediate pre-OSS affiliation and refine the 1942 transition chronology.",
                archival_review_priority="high",
            )
        elif row == 6:
            update.update(
                identity_status="conflicting",
                identity_evidence="The protected identifier printed in the index resolves in the official Army bulk file to a wholly different name. No Army identity or occupation is transferred to Edward C. McElroy.",
                research_status="conflicting_sources",
                next_action="Review Box 504 and the original index documentation to resolve the protected-identifier conflict before making identity or employment claims.",
                archival_review_priority="critical",
            )
        elif row == 33:
            update.update(
                identity_status="ambiguous",
                identity_evidence="The Army entry favors the McGaragle spelling, but the same protected identifier is printed for William C. McAragle on page 303. No occupation is transferred pending file comparison.",
                possible_duplicate_group="p303-308-william-mcaragle-mcgaragle-b623",
                research_status="needs_identity_review",
                next_action="Compare the William C. McAragle and William C. McGaragle files in Boxes 496 and 505 before merging, correcting, or transferring occupation evidence.",
                archival_review_priority="critical",
            )
        elif row in {35, 36}:
            update.update(
                identity_status="ambiguous",
                identity_evidence="Page 308's Edward A. McGaughy and Edward McGaughy rows conflict in identifier length and overlap with Edward A. McCaughy on page 304. All remain separate pending file review.",
                possible_duplicate_group="p304-308-edward-mccaughy-mcgaughy-b623",
                research_status="needs_identity_review",
                next_action="Compare the Edward McCaughy/McGaughy personnel files in Boxes 497 and 505 before any merge, correction, or employment assignment.",
                archival_review_priority="critical",
            )
        elif row == 19:
            update.update(
                identity_status="high_confidence",
                identity_evidence="Two printed rows share the exact indexed name and the same nonempty private identifier, so both source rows remain preserved and linked to one cautiously resolved person entity.",
                possible_duplicate_group="auto:b2850942-a685-52d7-bb47-43a368d1b665",
                research_status="requires_archival_review",
                next_action="Review both Robert D. McFadden entries in Box 504 to confirm duplicate-file structure and identify the pre-OSS affiliation.",
                archival_review_priority="high",
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
    if len(values) != 44 or len({item["person_id"] for item in values}) != 44:
        raise RuntimeError("Expected 44 unique page-308 person updates")
    return values


def outcome_note(row: int) -> str:
    if row in ARMY_OCCUPATIONS:
        return "An accepted official Army identity link supports a qualified dated occupation or student category but no named employer or OSS-transfer sequence."
    if row == 24:
        return "A contemporary institutional source supports Lawrence B. McFaddin's Indiana University student and fraternity affiliations; undefined Army code 993 remains uninterpreted."
    if row == 26:
        return "An accepted official Army link supports identity, but undefined occupation code 999 is not interpreted."
    if row == 32:
        return "Official and institutional sources establish an earlier school job, while a qualified later obituary supports the 1937-42 Medan mission-school role."
    if row == 6:
        return "A protected-identifier conflict remains visible; no Army identity or occupation was transferred."
    if row in AMBIGUOUS_ROWS:
        return "A cross-page spelling or protected-identifier conflict remains separate for direct personnel-file comparison."
    if row == 19:
        return "Two source rows remain preserved and linked to one high-confidence duplicate entity; no employer was established."
    return "No reliable identity or pre-OSS affiliation was established; unbridged namesakes and chronologically irrelevant results were rejected."


def research_attempts() -> list[dict[str, object]]:
    updates = {item["person_id"]: item for item in person_updates()}
    values: list[dict[str, object]] = []
    for row in UNIQUE_ROWS:
        person_id, name, box = PEOPLE[row]
        if row in set(ARMY_OCCUPATIONS) | ARMY_IDENTITY_ONLY | {32}:
            outcome, reviewed, rejected = "source_reviewed", 5, 2
        elif row in CONFLICT_ROWS | AMBIGUOUS_ROWS:
            outcome, reviewed, rejected = "candidate_rejected", 3, 4
        else:
            outcome, reviewed, rejected = "no_result", 2, 3
        values.append(
            {
                "key": f"page308-row{row}-{slug(name)}-b1053",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index context; exact-name and meaningful initial, punctuation, spacing, spelling and OCR variants; CIA-domain discovery; OSS, rank, branch, assignment and private-identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory and archival searches; indexed Box {box}",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_1053",
                "started_at": "2026-11-11T14:05:00-05:00",
                "completed_at": "2026-11-11T15:20:00-05:00",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, postwar-only leads, and sources without an OSS, rank, private-identifier, unit, or personnel-file bridge were rejected. Shared identifiers and duplicate rows remain visible. Army categories were not converted into named employers, and undefined codes 993 and 999 were not interpreted.",
                "research_notes": f"{outcome_note(row)} Page 308 was visually checked against a fresh official NARA download matching the preserved SHA-256. The official index, existing Library of Congress item-level attempts, exact-name OSS and meaningful-variant web discovery, CIA-domain discovery, employment and occupation checks, and obituary, institutional, directory, newspaper, and archival searches were reviewed as applicable. CIA-domain searches returned no person-specific result and were not treated as proof of absence. No search-result snippet was used as final evidence and no authenticated NARA Catalog API request was made.",
                "next_action": str(updates[person_id]["next_action"]),
                "attempt_number": ATTEMPT_NUMBERS[row],
                "research_agent_version": "before-oss-b1053-v1",
            }
        )
    if len(values) != 44 or len({item["person_id"] for item in values}) != 44:
        raise RuntimeError("Expected 44 unique page-308 research attempts")
    return values


def build_bundle() -> dict[str, object]:
    return {
        "bundle_version": "batch-1053-v1",
        "reviewer": "Before OSS Batch 1053 evidence review",
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
