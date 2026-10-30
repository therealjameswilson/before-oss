#!/usr/bin/env python3
"""Generate the reviewed Batch 989 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page485-voiles-to-von-meyerfeld-"
    "review_batch-989_2026-10-30.json"
)

INDEX = "nara-index-b989"
ARMY = "army-bulk-b989"
TECH = "army-tech-b989"
CODES = "army-codes-b989"
USDA_1945 = "usda-graduate-school-bulletin-1945-b989"
IAS = "ias-maxim-von-brevern-b989"
LBG_FRITSCH = "lbg-gunther-von-fritsch-b989"
AFMAG_LIETH = "air-force-magazine-john-von-der-lieth-b989"
TIME_HOF = "time-raimund-von-hofmannsthal-b989"

ORG_NATIONAL_PARK = "national-park-junior-college-b989"
ORG_IAS = "institute-for-advanced-study-b989"
ORG_INTERIOR = "us-department-interior-b989"

VOLOSEN_DUPLICATE_GROUP = "p261-p485-kuznecoff-volosen-b619"


PEOPLE = {
    1: ("2f4efe76-ace1-5e51-b6c1-37bea40965ac", "Alice Voiles"),
    2: ("1544624a-b9ba-549b-968a-433233d49a7c", "John F Vokestaitis"),
    3: ("aa1ebeca-8f75-538f-8771-d00f31025d41", "Joseph C Vokoun Jr."),
    4: ("2cef112d-9b1c-59ae-af29-c585cc49a415", "Arthur W Volck"),
    5: ("0ee623a9-7af4-5d84-89f0-6dce00e8a775", "Harold F Volk"),
    6: ("2cde1c52-ca14-52a3-b9b8-bc3a61fdbe18", "William J Volk"),
    7: ("168bb5fb-3e0e-543b-92a4-b80c8ada3acd", "Ernest W Volkmar"),
    8: ("9086c36c-96b5-5a72-a132-d139935f13d3", "Daniel E Volm"),
    9: ("1895dfcb-a588-5581-a5dc-6b56b86546a7", "Gerald Volm"),
    10: ("752029e7-cc27-5f1c-b486-30108e4126ee", "James Volosen"),
    11: ("b5fe08c4-ccf3-55e9-875c-13318f603d38", "Mario H Volpe"),
    12: ("b0b9a0cb-dc8e-59b8-bf41-49cf90f41b8f", "William Volpe"),
    13: ("113ffbf7-df79-5f44-a033-9f4e9560b928", "Elmer Volton"),
    14: ("2b7a4536-0cc9-54ad-b7d2-8447faa16939", "Frederick G Voltz"),
    15: ("2afa5f16-eb5c-539b-947e-0db82255d630", "Joseph Voltz"),
    16: ("43ea8eb6-e45b-554e-96da-f05b7bcb038f", "Nathalie A Von Bretzel"),
    17: ("42bb66fb-49e7-5501-a166-4451abefae0d", "Maxim C Von Brevern"),
    18: ("e6eb81b4-b503-5a3e-a5cd-c32139ddcb27", "John Von Der Lieth"),
    19: ("b365dd9c-3759-5b54-8365-b0662c9c7aa4", "Gunther Von Fritsch"),
    20: ("2216a8ab-92ec-5871-a82a-2e80d7ce470d", "Gerhard E Von Glahn"),
    21: ("bbc9de8f-66d7-52ef-a825-cd04a55cfba4", "Gert Hans Von Gontard"),
    22: ("52b56726-abdc-51af-aefe-6557f1c579ee", "Wilhelm-Viggo E.F. Von Hoffmanst"),
    23: ("7dfe6372-13f7-5ee8-8fb2-4dab6bdf03df", "Herman W Von Meyerfeld"),
}


UNRESOLVED = {
    1: "Exact-name, OSS, employer, occupation, obituary, directory, institutional and archival searches produced no reliable identity or pre-OSS affiliation bridge.",
    2: "Exact-name and spelling-variant searches produced no reliable identity or pre-OSS affiliation bridge.",
    4: "Exact-name, middle-initial, OSS, employer, occupation and archival searches produced no reliable identity or pre-OSS affiliation bridge.",
    5: "A 1941 Dallas directory names a Harold F. Volk as a company president, but no OSS or protected-identifier evidence connects that namesake to this row.",
    7: "Exact-name, OSS, employer, occupation, obituary and archival searches produced no reliable identity or pre-OSS affiliation bridge.",
    8: "Exact-name, OSS, employer, occupation, obituary and archival searches produced no reliable identity or pre-OSS affiliation bridge.",
    9: "A company history begins Gerald Volm's business career in 1954, which is postwar and cannot establish a pre-OSS affiliation.",
    13: "Exact-name, OSS, employer, occupation, obituary and archival searches produced no reliable identity or pre-OSS affiliation bridge.",
    14: "Exact-name, middle-initial, OSS, employer, occupation and archival searches produced no reliable identity or pre-OSS affiliation bridge.",
    15: "Exact-name searches produced multiple namesakes but no corroborating OSS identity or pre-OSS affiliation bridge.",
    20: "Exact-name and spelling-variant searches produced no reliable OSS identity or pre-OSS affiliation bridge.",
    21: "Exact-name and spelling-variant searches produced no reliable OSS identity or pre-OSS affiliation bridge.",
    23: "Exact-name and spelling-variant searches produced no reliable OSS identity or pre-OSS affiliation bridge.",
}


ARMY_OCCUPATIONS = {
    3: {
        "date": "1942-08-31",
        "code": "105",
        "official": "Clerks, general office",
        "public": "general office clerk",
    },
    11: {
        "date": "1942-09-14",
        "code": "022",
        "official": "Lawyers and judges",
        "public": "lawyer or judge",
    },
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 807-808",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 485, rows 1-23; checked against layout-preserving text and an original-detail page render",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. Protected identifiers remain private. The James Volosen conflict and truncated Wilhelm-Viggo E.F. Von Hoffmanst name are preserved rather than silently corrected or merged.",
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
            "rights_notes": "Four exact name-and-identifier bridges were accepted. The Wilhelm-Viggo/Raimund name mismatch and James Volosen/Walter Kuznecoff shared identifier remain conflicts. No raw bulk row, record ordinal or full identifier enters public assets.",
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
            "locator": "PDF physical pages 171 and 174, with amended page 304; codes 022, 105 and 480 visually checked; code 999 absent from the reviewed three-digit list",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical categories identify broad occupations, not a named employer, workplace or exact job. Code 480 is not used because its Army entry postdates OSS dissolution; code 999 remains uninterpreted.",
        },
        {
            "key": USDA_1945,
            "stable_url": "https://archive.org/details/CAT31332222003",
            "archival_identifier": "CAT31332222003",
            "title": "Graduate School, United States Department of Agriculture: Spring Semester 1945",
            "author_creator": "Graduate School, United States Department of Agriculture",
            "repository_publisher": "United States Department of Agriculture; digitized by the National Agricultural Library and Internet Archive",
            "publication_record_date": "1945-01",
            "locator": "PDF physical page 89, printed page 85; Nathalie Von Bretzel faculty biography",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "United States Department of Agriculture Graduate School bulletins",
            "rights_notes": "The contemporary government bulletin identifies Von Bretzel's current OSS role and earlier teaching at National Park Junior College. Her concurrent 1945 Graduate School teaching is not recast as pre-OSS employment.",
        },
        {
            "key": IAS,
            "stable_url": "https://www.ias.edu/scholars/maxim-von-brevern",
            "archival_identifier": "Institute for Advanced Study scholar profile: Maxim von Brevern",
            "title": "Maxim von Brevern",
            "author_creator": "Institute for Advanced Study",
            "repository_publisher": "Institute for Advanced Study",
            "publication_record_date": None,
            "locator": "Scholar profile; School of Economics and Politics, member, September-December 1941",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Institute for Advanced Study scholar records",
            "rights_notes": "The exact-name institutional record supports a qualified pre-OSS professional affiliation, not employment. It does not mention OSS or the middle initial, so identity remains probable pending personnel-file review.",
        },
        {
            "key": LBG_FRITSCH,
            "stable_url": "https://austriansoldiers.lbg.ac.at/bio/gunther-von-fritsch/?lang=en",
            "archival_identifier": "Austrian Soldiers in the US Army biography: Gunther von Fritsch",
            "title": "Gunther von Fritsch",
            "author_creator": "Ludwig Boltzmann Institute for Research on Consequences of War",
            "repository_publisher": "Ludwig Boltzmann Gesellschaft",
            "publication_record_date": None,
            "locator": "Biography section on emigration and employment; October 1940 draft-card employment at the U.S. Department of the Interior",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Austrian Soldiers in the US Army",
            "rights_notes": "Institutional research biography citing underlying NARA records. It supports a qualified 1940 government assignment but does not directly link the person to OSS.",
        },
        {
            "key": AFMAG_LIETH,
            "stable_url": "https://www.airandspaceforces.com/app/uploads/2024/08/AFmag_1980_11.pdf",
            "archival_identifier": "Air Force Magazine, November 1980",
            "title": "Raids on Schweinfurt",
            "author_creator": "Col. Stone Christopher, USAF (Ret.)",
            "repository_publisher": "Air Force Association",
            "publication_record_date": "1980-11",
            "locator": "PDF physical page 18, printed page 16; letter to the editor",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Air Force Magazine",
            "rights_notes": "The retrospective letter places exact-name John Von der Lieth as U.S. Vice Consul in Gothenburg on 1 January 1944. It supplies wartime context but neither a pre-OSS employer nor a direct OSS link.",
        },
        {
            "key": TIME_HOF,
            "stable_url": "https://time.com/archive/6760841/milestones-jun-19-1939/",
            "archival_identifier": "TIME archive, June 19, 1939",
            "title": "Milestones, Jun. 19, 1939",
            "author_creator": "TIME",
            "repository_publisher": "TIME",
            "publication_record_date": "1939-06-19",
            "locator": "Milestones notice for Raimund von Hofmannsthal",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "TIME archive",
            "rights_notes": "This contemporary source documents Raimund von Hofmannsthal's London staff role at Time Inc. It is conflict context only and is not assigned to the differently named indexed Wilhelm-Viggo E.F. Von Hoffmanst.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": ORG_NATIONAL_PARK,
            "canonical_name": "National Park Junior College",
            "historical_name": "National Park Junior College",
            "aliases": ["National Park Seminary and Junior College"],
            "organization_type": "junior college",
            "sector": "academia_and_research",
            "city": "Forest Glen",
            "state_or_region": "Maryland",
            "country": "United States",
            "active_dates": "Historical institution; exact name preserved from the 1945 source",
            "normalization_notes": "The historical employer name is preserved. No modern successor institution is substituted.",
        },
        {
            "key": ORG_IAS,
            "canonical_name": "Institute for Advanced Study",
            "historical_name": "Institute for Advanced Study",
            "aliases": ["IAS"],
            "organization_type": "independent research institute",
            "sector": "academia_and_research",
            "city": "Princeton",
            "state_or_region": "New Jersey",
            "country": "United States",
            "active_dates": "Founded 1930",
            "normalization_notes": "The School of Economics and Politics is retained in the role field rather than treated as a separate employer.",
        },
        {
            "key": ORG_INTERIOR,
            "canonical_name": "United States Department of the Interior",
            "historical_name": "U.S. Department of the Interior",
            "aliases": ["Department of the Interior", "Interior Department"],
            "organization_type": "federal executive department",
            "sector": "federal_government",
            "country": "United States",
            "normalization_notes": "The department is retained as the named 1940 government organization; no unidentified subordinate bureau is inferred.",
        },
    ]


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, item in ARMY_OCCUPATIONS.items():
        name = PEOPLE[row][1]
        values.append(
            {
                "key": f"{slug(name)}-army-category-b989-row{row}",
                "person_id": PEOPLE[row][0],
                "occupation": item["public"],
                "relationship_type": "employment",
                "end_date": item["date"],
                "date_precision": "Historical civilian-occupation category recorded at Army entry; employer, workplace, duration and exact job are not supplied",
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
                "key": "nathalie-von-bretzel-national-park-b989",
                "person_id": PEOPLE[16][0],
                "organization_key": ORG_NATIONAL_PARK,
                "organization_name_as_found": "National Park Junior College",
                "role_title": "teacher",
                "occupation": "teacher",
                "relationship_type": "employment",
                "date_precision": "A January 1945 government bulletin describes this teaching in the past tense while listing Von Bretzel's current OSS role; exact dates and immediacy are not supplied",
                "city": "Forest Glen",
                "state_or_region": "Maryland",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Earlier documented employment. The source directly names both the prior college teaching and her current OSS role, but it does not prove this was the immediate predecessor or last civilian employer.",
            },
            {
                "key": "maxim-von-brevern-ias-b989",
                "person_id": PEOPLE[17][0],
                "organization_key": ORG_IAS,
                "organization_name_as_found": "Institute for Advanced Study",
                "role_title": "member, School of Economics and Politics",
                "relationship_type": "professional_affiliation",
                "start_date": "1941-09",
                "end_date": "1941-12",
                "date_precision": "Institute profile gives September through December 1941",
                "city": "Princeton",
                "state_or_region": "New Jersey",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "probable",
                "claim_confidence": "medium",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "publish_qualified",
                "research_notes": "Qualified professional affiliation, not employment. Exact-name institutional evidence is strong, but the profile has no middle initial or OSS link.",
            },
            {
                "key": "gunther-von-fritsch-interior-b989",
                "person_id": PEOPLE[19][0],
                "organization_key": ORG_INTERIOR,
                "organization_name_as_found": "U.S. Department of the Interior",
                "role_title": "director of short documentary films",
                "occupation": "film director",
                "relationship_type": "government_assignment",
                "start_date": "1940-10",
                "date_precision": "An October 1940 draft-card record cited by the institutional biography gives the employer and activity; beginning and ending dates are unknown",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "probable",
                "claim_confidence": "medium",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "publish_qualified",
                "research_notes": "Qualified earlier government assignment. The source does not link the biography directly to the OSS index or establish the immediate pre-OSS sequence.",
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
    for row, item in ARMY_OCCUPATIONS.items():
        name = PEOPLE[row][1]
        affiliation_key = f"{slug(name)}-army-category-b989-row{row}"
        values.extend(
            [
                claim(
                    row,
                    f"identity-{slug(name)}-army-b989-row{row}",
                    "identity",
                    f"Indexed {name} is high-confidence matched to the official Army entry reviewed for Batch 989.",
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
                ),
                claim(
                    row,
                    f"occupation-{slug(name)}-b989-row{row}",
                    "occupation",
                    f"At Army entry on {item['date']}, {name}'s historical civilian category was {str(item['official']).lower()}.",
                    f"The official Army field carries historical code {item['code']}; NARA's code list defines it as {item['official']}.",
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
                    affiliation_key,
                    "publish_qualified",
                ),
            ]
        )

    values.extend(
        [
            claim(
                6,
                "identity-william-j-volk-army-b989-row6",
                "identity",
                "Indexed William J Volk is high-confidence matched to the official Army entry reviewed for Batch 989.",
                "The exact official name and a nonshared protected identifier directly link the printed row to the reviewed Army record.",
                "High confidence from exact name and a nonshared protected identifier; the protected value and raw bulk record are withheld.",
                "The Army-entry date is 16 July 1946, after OSS dissolution, so the record supports identity but no pre-OSS occupation or affiliation.",
                "A_direct_official",
                "high",
                [{"source_key": INDEX}, {"source_key": ARMY, "locator_override": "Accepted identity bridge; protected identifier and raw record withheld"}],
                "Historical code 480 is not transferred because the dated Army entry is post-OSS.",
            ),
            claim(
                12,
                "identity-william-volpe-army-b989-row12",
                "identity",
                "Indexed William Volpe is high-confidence matched to the official Army entry reviewed for Batch 989.",
                "The exact official name and a nonshared protected identifier directly link the printed row to the reviewed Army record.",
                "High confidence from exact name and a nonshared protected identifier; the protected value and raw bulk record are withheld.",
                "The Army record supports identity; historical code 999 is undefined in the reviewed official code list and supplies no occupation.",
                "A_direct_official",
                "high",
                [{"source_key": INDEX}, {"source_key": ARMY, "locator_override": "Accepted identity bridge; protected identifier and raw record withheld"}],
                "No occupation, employer or chronology is inferred from undefined code 999.",
            ),
            claim(
                16,
                "identity-nathalie-von-bretzel-usda-b989",
                "identity",
                "Indexed Nathalie A Von Bretzel is high-confidence identified as the OSS research assistant described in a contemporary U.S. government bulletin.",
                "The distinctive exact name appears with a current senior research-assistant role in the USSR Section of OSS and an earlier teaching role.",
                "High confidence from the distinctive exact name and a contemporary government source that directly names her OSS section and role.",
                "The January 1945 bulletin explicitly distinguishes her current OSS role from earlier teaching, but gives no exact transition date.",
                "B_authoritative_institutional",
                "high",
                [{"source_key": INDEX}, {"source_key": USDA_1945}],
                "The indexed file remains necessary for a confirmed identifier match and complete transfer chronology.",
            ),
            claim(
                16,
                "earlier-nathalie-von-bretzel-national-park-b989",
                "other_pre_oss_affiliation",
                "Nathalie Von Bretzel taught at National Park Junior College before the January 1945 bulletin described her current OSS role.",
                "The contemporary government faculty biography says she taught at National Park Junior College and currently served as an OSS senior research assistant.",
                "High-confidence identity from the distinctive exact name and direct OSS role in the same source.",
                "Documented before the dated current OSS role, but exact dates, immediacy and last-civilian status are not supplied.",
                "B_authoritative_institutional",
                "high",
                [{"source_key": USDA_1945}],
                "Published as earlier employment only; not counted as immediate pre-OSS or last civilian employer.",
                "nathalie-von-bretzel-national-park-b989",
            ),
            claim(
                17,
                "identity-maxim-von-brevern-ias-b989",
                "identity",
                "The indexed Maxim C Von Brevern is probably the Maxim von Brevern documented at the Institute for Advanced Study in late 1941.",
                "The exact distinctive name appears in the Institute's scholar record as a member of the School of Economics and Politics.",
                "Probable: the exact rare name and prewar timing agree, but the institutional profile omits the middle initial and does not mention OSS.",
                "The affiliation is explicitly dated September through December 1941; its relation to OSS recruitment is unknown.",
                "B_authoritative_institutional",
                "medium",
                [{"source_key": INDEX}, {"source_key": IAS}],
                "Qualified identity pending review of Box 807; not included in default confirmed/high identity analytics.",
                publication_status="publish_qualified",
            ),
            claim(
                17,
                "earlier-maxim-von-brevern-ias-b989",
                "other_pre_oss_affiliation",
                "Maxim von Brevern was a member of the Institute for Advanced Study's School of Economics and Politics from September through December 1941.",
                "The Institute's scholar record directly supplies the name, school, member status and date range.",
                "Probable identity from the exact rare name; personnel-file corroboration is still required.",
                "Explicitly dated prewar professional affiliation; no source shows it was employment, immediate pre-OSS or the last civilian role.",
                "B_authoritative_institutional",
                "medium",
                [{"source_key": IAS}],
                "Published as a qualified professional affiliation, never as an employer.",
                "maxim-von-brevern-ias-b989",
                "publish_qualified",
            ),
            claim(
                18,
                "identity-context-john-von-der-lieth-b989",
                "identity",
                "The indexed John Von Der Lieth is probably the U.S. vice consul documented in Gothenburg on 1 January 1944.",
                "A military-history journal letter names John Von der Lieth as U.S. Vice Consul in Gothenburg during a documented wartime bearing transaction.",
                "Probable from the distinctive exact name and wartime European context; the source gives no protected identifier or direct OSS link.",
                "The source establishes a 1 January 1944 diplomatic role, not a pre-OSS employer or recruitment sequence.",
                "C_reputable_contemporary_or_scholarly",
                "medium",
                [{"source_key": INDEX}, {"source_key": AFMAG_LIETH}],
                "Published as qualified identity and wartime context only; no affiliation record is created.",
                publication_status="publish_qualified",
            ),
            claim(
                19,
                "identity-gunther-von-fritsch-lbg-b989",
                "identity",
                "The indexed Gunther Von Fritsch is probably the Austrian-born filmmaker documented by an institutional military-history project.",
                "The exact distinctive name and compatible wartime Army chronology appear in a research biography based on archival records.",
                "Probable from the exact rare name and compatible Army chronology; the biography does not directly link the person to OSS.",
                "The biography dates a Department of the Interior assignment to October 1940 and Army induction to December 1943.",
                "C_reputable_contemporary_or_scholarly",
                "medium",
                [{"source_key": INDEX}, {"source_key": LBG_FRITSCH}],
                "Qualified identity pending personnel-file review; not included in default confirmed/high identity analytics.",
                publication_status="publish_qualified",
            ),
            claim(
                19,
                "earlier-gunther-von-fritsch-interior-b989",
                "other_pre_oss_affiliation",
                "Gunther von Fritsch worked for the U.S. Department of the Interior directing short documentary films in October 1940.",
                "The institutional biography reports that his October 1940 draft card recorded this department and documentary-directing activity.",
                "Probable identity from the distinctive exact name and compatible wartime chronology; direct OSS corroboration remains absent.",
                "Documented in October 1940, but neither dates of service nor its relation to OSS recruitment are established.",
                "C_reputable_contemporary_or_scholarly",
                "medium",
                [{"source_key": LBG_FRITSCH}],
                "Published as a qualified earlier government assignment, not as immediate pre-OSS or last civilian employment.",
                "gunther-von-fritsch-interior-b989",
                "publish_qualified",
            ),
            claim(
                10,
                "identity-conflict-james-volosen-b989",
                "identity",
                "James Volosen remains a conflicting identity because his printed protected identifier is also assigned to Walter M Kuznecoff in the OSS index.",
                "Two separately printed index people share the same protected identifier, preventing a defensible identity or occupation transfer.",
                "Conflicting: a shared identifier is strong evidence of an index or filing problem, not permission to merge differently named people.",
                "No reliable pre-OSS sequence can be assigned until both indexed files are compared.",
                "A_direct_official",
                "conflicting",
                [{"source_key": INDEX}, {"source_key": ARMY, "support_type": "context_only", "locator_override": "Candidate comparison withheld because the index identifier is shared"}],
                "The source rows stay separate in the existing conflict group; no Army identity, occupation or employer is transferred.",
                publication_status="conflicting",
            ),
            claim(
                22,
                "identity-conflict-wilhelm-viggo-von-hoffmanst-b989",
                "identity",
                "The indexed Wilhelm-Viggo E.F. Von Hoffmanst conflicts with an Army record for Raimund Von Hofmannsthal carrying the same protected identifier.",
                "The protected identifier resolves to a wholly different full name in the official Army file; a contemporary source separately documents Raimund's 1939 employment.",
                "Conflicting: identifier agreement is outweighed by the wholly different full name, and the truncated index spelling cannot be silently expanded.",
                "Neither the Army occupation nor Raimund's Time Inc. employment can be assigned to the indexed person without personnel-file review.",
                "A_direct_official",
                "conflicting",
                [
                    {"source_key": INDEX},
                    {"source_key": ARMY, "support_type": "contradicts", "locator_override": "Army candidate name: Raimund Von Hofmannsthal; protected identifier withheld"},
                    {"source_key": TIME_HOF, "support_type": "context_only"},
                ],
                "Conflict is public and excluded from default analytics. The Time employment belongs only to the separate Raimund candidate unless the indexed file proves otherwise.",
                publication_status="conflicting",
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
        values.append(
            base_update(
                row,
                identity_status="unresolved",
                identity_evidence=f"The visually verified page 485 row preserves {PEOPLE[row][1]} and its indexed Box 807 or 808 context. {reason}",
                research_status="requires_archival_review",
                next_action=f"Review the indexed personnel file for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}",
            )
        )

    for row, item in ARMY_OCCUPATIONS.items():
        values.append(
            base_update(
                row,
                identity_status="high_confidence",
                identity_evidence="The exact official name and a nonshared protected-identifier agreement support the Army identity match; the protected value remains private.",
                personnel_category=("commissioned_army_officer" if row == 11 else "enlisted_army_personnel"),
                commissioned_officer=(row == 11),
                allied_or_foreign_personnel=False,
                research_status="occupation_only_found",
                next_action=f"Review the indexed personnel file to identify any named employer behind historical code {item['code']} and establish the Army-to-OSS chronology. The code supplies only a broad occupation category.",
                nara_catalog_id="1263923",
            )
        )

    values.extend(
        [
            base_update(
                6,
                identity_status="high_confidence",
                identity_evidence="The exact official name and a nonshared protected-identifier agreement support the Army identity match; the protected value remains private.",
                personnel_category="enlisted_army_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                research_status="requires_archival_review",
                next_action="Review Box 807 to establish the pre-OSS chronology. The accepted Army identity record entered after OSS dissolution, so its occupation code supplies no pre-OSS evidence.",
                nara_catalog_id="1263923",
            ),
            base_update(
                10,
                identity_status="conflicting",
                identity_evidence="The printed protected identifier is shared by separately indexed James Volosen and Walter M Kuznecoff. The source rows remain separate and no Army identity, occupation or employer is transferred.",
                possible_duplicate_group=VOLOSEN_DUPLICATE_GROUP,
                research_status="conflicting_sources",
                next_action="Review the James Volosen and Walter M Kuznecoff personnel files together before assigning an identity, occupation or pre-OSS affiliation.",
                archival_review_priority="critical",
            ),
            base_update(
                12,
                identity_status="high_confidence",
                identity_evidence="The exact official name and a nonshared protected-identifier agreement support the Army identity match; the protected value remains private.",
                personnel_category="enlisted_army_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                research_status="requires_archival_review",
                next_action="Review Box 807 to establish pre-OSS employment and the Army-to-OSS chronology. Historical code 999 is undefined in the reviewed official code list.",
                nara_catalog_id="1263923",
            ),
            base_update(
                16,
                identity_status="high_confidence",
                identity_evidence="A contemporary U.S. government bulletin gives the distinctive exact name, a current OSS senior research-assistant role and the earlier National Park Junior College teaching role.",
                personnel_category="civilian_professional_or_administrative_grade",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                research_status="documented_prewar_employer_found",
                next_action="National Park Junior College is documented as earlier employment, but Box 807 should be reviewed to establish dates, the immediate predecessor affiliation and the last civilian employer.",
                archival_review_priority="medium",
            ),
            base_update(
                17,
                identity_status="probable",
                identity_evidence="The exact rare name and prewar timing agree with the Institute for Advanced Study scholar record, but the profile omits the middle initial and does not mention OSS.",
                research_status="requires_archival_review",
                next_action="Review Box 807 for an identifier and OSS chronology. The September-December 1941 Institute for Advanced Study membership is published only as a qualified professional affiliation, not employment.",
            ),
            base_update(
                18,
                identity_status="probable",
                identity_evidence="A military-history journal gives the distinctive exact name and a wartime U.S. vice-consul role in Gothenburg, but no protected identifier or direct OSS link.",
                research_status="requires_archival_review",
                next_action="Review Box 807 for an identity bridge and pre-OSS chronology. The 1 January 1944 vice-consul context does not establish a pre-OSS employer.",
            ),
            base_update(
                19,
                identity_status="probable",
                identity_evidence="An institutional research biography gives the distinctive exact name and compatible wartime Army chronology, but it does not directly link the person to the OSS index.",
                personnel_category="enlisted_army_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                research_status="requires_archival_review",
                next_action="Review Box 808 for an identifier and transfer chronology. The October 1940 Department of the Interior assignment is published only as qualified earlier evidence.",
            ),
            base_update(
                22,
                identity_status="conflicting",
                identity_evidence="The protected identifier resolves in the Army file to Raimund Von Hofmannsthal, a wholly different full name from the indexed Wilhelm-Viggo E.F. Von Hoffmanst. No identity, occupation or employment is transferred.",
                research_status="conflicting_sources",
                next_action="Review Box 808 and the neighboring von-name files to resolve whether the printed name or identifier is displaced. Do not assign Raimund von Hofmannsthal's Army record or Time Inc. employment before that review.",
                archival_review_priority="critical",
            ),
        ]
    )
    return values


def research_attempts() -> list[dict[str, object]]:
    sourced = {3, 6, 10, 11, 12, 16, 17, 18, 19, 22}
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        if row == 16:
            outcome = "source_reviewed"
            sources_reviewed = 9
            rejected = 5
            detail = "A contemporary USDA Graduate School bulletin directly linked the exact name to OSS and documented earlier National Park Junior College teaching."
        elif row in {17, 18, 19}:
            outcome = "source_reviewed"
            sources_reviewed = 8
            rejected = 6
            detail = "An institutional or military-history source supplied a qualified identity and dated context, but no direct personnel-file bridge or reliable immediate pre-OSS employer."
        elif row in {3, 6, 11, 12}:
            outcome = "source_reviewed"
            sources_reviewed = 7
            rejected = 5
            detail = "Reviewed official index, Army bulk, technical and code-list evidence produced the accepted identity and qualified occupation or identity-only outcome recorded in the bundle."
        elif row in {10, 22}:
            outcome = "source_reviewed"
            sources_reviewed = 7
            rejected = 6
            detail = "Official identifier comparison exposed a conflicting name or shared-identifier problem, so identity, occupation and employer transfer were withheld."
        else:
            outcome = "no_result"
            sources_reviewed = 6
            rejected = 6
            detail = UNRESOLVED[row]
        attempts.append(
            {
                "key": f"page485-row{row}-{slug(name)}-b989",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index context; CIA Reading Room or equivalent official-source check; Library of Congress collection check; exact-name and meaningful variants; OSS, rank, branch, identifier and assignment clues; employer and occupation 1940; obituary, institutional, newspaper, directory and archival searches; indexed Box 807 or 808; protected identifiers used only in private official-record comparison",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_989",
                "started_at": "2026-10-30T15:45:00Z",
                "completed_at": "2026-10-30T17:00:00Z",
                "outcome": outcome,
                "sources_reviewed": sources_reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, snippets, commercial people-finder pages, relatives, unsourced genealogy, postwar-only leads and sources without an OSS, protected-identifier, rank, unit or personnel-file bridge were rejected. Historical occupation categories, wartime diplomatic roles and government assignments were not converted into employers. Harold F. Volk's Dallas directory namesake and Gerald Volm's postwar company history were rejected. Raimund von Hofmannsthal's Time Inc. employment was not transferred to the differently named indexed person.",
                "research_notes": f"{detail} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain and archival searches were checked as applicable. The CIA Reading Room adapter recorded its robots restriction without bypass; grouped official-domain discovery searches returned no candidate. The LoC.gov adapter or current collection check produced no publishable source for this review. The NARA index page, official Army technical documentation and relevant code-list pages were inspected directly. No search-result snippet was used as sole final evidence, no paywall or access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": "Review the indexed personnel file for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before wartime service.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b989-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-989-v1",
        "reviewer": "Before OSS Batch 989 evidence review",
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
