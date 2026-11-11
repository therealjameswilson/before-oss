#!/usr/bin/env python3
"""Generate the reviewed Batch 1055 completion bundle for PDF page 310."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page310-james-a-mcguire-to-emmy-r-mckee-review_"
    "batch-1055_2026-11-11.json"
)

INDEX = "nara-index-page310-b1055"
ARMY = "army-bulk-page310-b1055"
TECH = "army-tech-page310-b1055"
CODES = "army-codes-page310-b1055"
ACC = "acc-henry-mcintosh-b1055"
NPS = "nps-henry-deane-mcintosh-b1055"
GAZETTE = "london-gazette-peter-mckeand-b1055"
FETTES = "fettes-peter-mckeand-b1055"
OKMHOF = "oklahoma-military-hall-calvin-mckee-b1055"
FITZGERALD = "fitzgerald-calvin-mckee-b1055"


PEOPLE = {
    1: ("b3075200-83c5-5e59-995c-e36fcaf8969b", "James A McGuire", "507"),
    2: ("78aabdc6-8193-5711-8a13-d5a184de37bd", "Joseph T McGuire", "507"),
    3: ("5b292952-6dac-5457-b87a-2810d512c6ec", "Kathleen McGuire", "507"),
    4: ("4fd7fa9f-d0c4-5d3d-85d8-6bbdc0218ee9", "Lucy J McGuire", "507"),
    5: ("335ea3d6-5fe4-5973-8c55-224935fa4826", "Martin E McGuire", "507"),
    6: ("e59a8582-deef-5697-b08f-c5db9df369d6", "Melvin T McGuire", "507"),
    7: ("74bcb75d-d0b9-54c5-9404-33d108056164", "Thomas F McGuire", "507"),
    8: ("cab5a497-9f2c-5f8e-ac99-557fc564d797", "William T McGuire", "507"),
    9: ("c4351070-8273-53b7-9de5-8e3dd2fbdc64", "Francis McGurk", "507"),
    10: ("bfa34ef5-18cc-5422-9e3b-8bc14a31ff3b", "Andrew D McHendrie", "507"),
    11: ("1b5e143f-8a83-59c3-813e-4390d6f04e10", "Janet H McHendrie", "507"),
    12: ("348b62ba-10cb-58a3-8862-711b6c6ba7fb", "James H McHugh", "507"),
    13: ("8d673f1d-952a-59df-8197-8404206eb0b8", "Loughlin G McHugh", "507"),
    14: ("042c24c0-ea25-5c04-a1ab-7bcde3b0e180", "Martin I McHugh", "507"),
    15: ("b200530a-db10-5858-b7dc-a9643c3ed8bd", "Erie McIlhenny", "507"),
    16: ("23ea1fcb-b040-556d-bc2c-8c36777043db", "Opal E McIlhenny", "507"),
    17: ("dd982cc7-df0d-5b87-9041-b6edf50509e7", "William McIlraith", "507"),
    18: ("a53654fc-2e95-5d4b-914b-9836d8c9f546", "Perry E McIlvaine", "507"),
    19: ("6832ec68-a67a-5570-97c1-a340d9adb9bf", "George O McIninch", "507"),
    20: ("e9ded329-c58c-5637-8bcf-26783ffe2149", "Donald E McInnis", "507"),
    21: ("ae5d6a79-fad8-57c1-9076-6d7ba2e0d892", "Carolyn S McIntosh", "508"),
    22: ("e440e796-473a-51d5-97a9-fdbcdc42b986", "Carolyn McIntosh", "507"),
    23: ("c9a01212-57dd-51e7-a539-0fcd48426344", "Henry D McIntosh", "507"),
    24: ("586f051e-49c1-52c3-a60f-eb2f5955767e", "Jean McIntosh", "507"),
    25: ("33c5cc44-3fde-5b06-95f4-bfc6b64a208f", "Norma C McIntosh", "507"),
    26: ("7c53e363-a224-512d-aa0f-c60c7cdb3e80", "Robert McIntosh", "507"),
    27: ("89945a25-8f2d-59ab-93b8-de14ffc73dda", "Adelle McIntyre", "507"),
    28: ("c9b19741-c01e-5d4a-bd66-b1cc454c6847", "Ann C McIntyre", "507"),
    29: ("5c1050cd-c559-5cef-81a5-5168325d66d1", "John W McIntyre", "507"),
    30: ("a94433d8-0eec-58a3-8b08-9178c171230d", "Katherine McIntyre", "507"),
    31: ("926aceed-b77a-5944-bafb-fa06897b0e21", "Marshall W McIntyre", "507"),
    32: ("c4e77b7d-e470-5a79-98b2-210d9d2e8266", "Ann C McKay", "507"),
    33: ("424a424a-9dbb-5ed8-a29c-69aa4c2e9831", "Donald C McKay", "508"),
    34: ("cbbd07bc-674f-53ed-be70-e03a4e81a4f9", "Grace M McKay", "508"),
    35: ("8ec3696f-e2a2-5b70-93cc-86dece9b91cb", "Herman McKay", "508"),
    36: ("43f38d64-93bd-5c37-be74-feba88c9c67f", "Lawerence I McKay", "508"),
    37: ("01414f99-a8d1-5ec1-b188-4ca1a30127af", "Thomas A McKay", "508"),
    38: ("b47656af-0036-5003-a976-0e5d604be4ab", "William J McKay", "508"),
    39: ("83707c1a-7daf-58c1-a89e-148fcdf7f9d5", "William M McKay", "508"),
    40: ("20a66cdc-f78b-5023-b6f6-1211443f1f64", "Gertrude L McKean", "508"),
    41: ("f634b404-7d17-5e3b-a77d-91211c565ba1", "Peter A.H. McKeand", "508"),
    42: ("985ad762-bd86-5d93-a99b-c2db86b41f28", "Calvin C McKee", "508"),
    43: ("66c4779b-2e27-555c-8157-0522ea46def5", "Charles T McKee", "508"),
    44: ("68ff85e6-97a8-56f6-be0f-0d98b8998911", "Dan M McKee", "508"),
    45: ("fa3db986-79fb-502a-b154-920f3493290a", "David R McKee", "508"),
    46: ("d33532a4-c781-5a73-a03e-807efe81bcad", "Emmy R McKee", "508"),
}


ARMY_OCCUPATIONS = {
    20: ("1942-09-18", "661", "shoe and boot manufacturing worker", "Shoe and boot manufacturing occupations", "unknown", "PDF physical pages 173 and 304; historical code 6-61"),
    26: ("1943-05-20", "106", "financial institution clerk, not elsewhere classified", "Financial institution clerks, n.e.c.", "unknown", "PDF physical page 171; historical code 1-06"),
    43: ("1942-12-07", "992", "student", "Students", "student", "PDF physical page 304; corrected historical code 9-92"),
}

ATTEMPT_NUMBERS = {
    1: 3, 2: 3, 3: 2, 4: 2, 5: 2, 6: 2, 7: 4, 8: 4, 9: 2,
    10: 2, 11: 2, 12: 3, 13: 3, 14: 2, 15: 2, 16: 2, 17: 2,
    18: 2, 19: 2, 20: 3, 21: 2, 22: 2, 23: 3, 24: 1, 25: 1,
    26: 1, 27: 1, 28: 1, 29: 1, 30: 1, 31: 1, 32: 1, 33: 2,
    34: 1, 35: 1, 36: 1, 37: 1, 38: 1, 39: 1, 40: 1, 41: 1,
    42: 1, 43: 1, 44: 1, 45: 1, 46: 1,
}

CONFLICT_ROWS = {7, 13}
DUPLICATE_ROWS = {21, 22}
POSITIVE_ROWS = set(ARMY_OCCUPATIONS) | {23, 33, 41, 42}


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
            archival_identifier="RG 226, Entry A1-224, Boxes 507-508",
            title="OSS Personnel Files from Excel",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="2010-12-23",
            locator="PDF page 310, rows 1-46; every printed row visually checked against the official PDF",
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
            locator="PDF physical pages 171, 173, and 304; all three Batch 1055 categories visually checked",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records technical documentation",
            rights_notes="Categories identify neither employer nor exact Army-to-OSS sequence.",
        ),
        source(
            ACC,
            stable_url="https://www.acc.org/-/media/Non-Clinical/Files-PDFs-Excel-MS-Word-etc/Membership/Publications/Cardiology-Magazine/2009/2009-03-Cardiology-Magazine.pdf",
            archival_identifier="Cardiology, March 2009, volume 38, number 3",
            title="Remembering Henry McIntosh, M.D., M.A.C.C.",
            author_creator="Richard A. Chazal",
            repository_publisher="American College of Cardiology",
            publication_record_date="2009-03",
            locator="PDF page 23, profile paragraphs 1-3",
            source_quality="B_authoritative_institutional",
            collection_name="Cardiology magazine",
            rights_notes="Only project-authored paraphrases and a short supporting excerpt are retained.",
        ),
        source(
            NPS,
            stable_url="https://home.nps.gov/articles/postwar-period-end-of-the-oss-and-return-to-the-park-service.htm",
            archival_identifier="National Park Service OSS history study, postwar period",
            title="Postwar Period: End of the OSS and Return to the Park Service",
            author_creator="John Whiteclay Chambers II",
            repository_publisher="United States National Park Service",
            publication_record_date="current official historical article; accessed 2026-11-11",
            locator="Postwar careers section; Lieutenant Henry Deane McIntosh paragraph",
            source_quality="B_authoritative_institutional",
            collection_name="OSS Training in the National Parks and Service Abroad in World War II",
            rights_notes="Used to corroborate the full middle name, lieutenant rank, Jedburgh service, and medical chronology.",
        ),
        source(
            GAZETTE,
            stable_url="https://www.thegazette.co.uk/London/issue/38628/supplement/2824/data.pdf",
            archival_identifier="The London Gazette, issue 38628, supplement 2824",
            title="Appointments to commissions in the Royal Air Force Volunteer Reserve",
            author_creator="Air Ministry",
            repository_publisher="The London Gazette",
            publication_record_date="1949-06-07",
            locator="Supplement page 2824; Peter Andrew Hannay McKeand entry",
            source_quality="A_direct_official",
            collection_name="The London Gazette",
            rights_notes="This postwar official record supports name expansion and RAF identity only, not an OSS chronology.",
        ),
        source(
            FETTES,
            stable_url="https://www.fettes.com/uploaded/PDF/Sadly_Departed_List_-_Last_Updated_09.09.2025.pdf",
            archival_identifier="Fettes College sadly departed list, updated 2025-09-09",
            title="Sadly Departed List",
            author_creator="Fettes College",
            repository_publisher="Fettes College",
            publication_record_date="2025-09-09",
            locator="McKeand, Wing Commander Peter A H; death 1960-10-27",
            source_quality="B_authoritative_institutional",
            collection_name="Fettes College historical records",
            rights_notes="Supports the rare initials and RAF rank; it does not establish OSS service or a pre-OSS affiliation.",
        ),
        source(
            OKMHOF,
            stable_url="https://okmhf.org/citations-2025-1",
            archival_identifier="Oklahoma Military Hall of Fame, Memorial Day 2025 citation",
            title="Calvin McKee",
            author_creator="Oklahoma Military Hall of Fame",
            repository_publisher="Oklahoma Military Hall of Fame",
            publication_record_date="2025",
            locator="Memorial Day 2025 section, Calvin McKee",
            source_quality="B_authoritative_institutional",
            collection_name="Citations 2025",
            rights_notes="Used for exact-name OSS and Army service context; later careers are excluded from pre-OSS claims.",
        ),
        source(
            FITZGERALD,
            stable_url="https://www.fitzgeraldfuneralservice.com/obituaries/calvin-mckee",
            archival_identifier="Fitzgerald Funeral Service obituary, Calvin Charles McKee",
            title="Calvin Charles McKee",
            author_creator="Family-placed obituary",
            repository_publisher="Fitzgerald Funeral Service",
            publication_record_date="2019-12",
            locator="Military-service paragraphs",
            source_quality="C_reputable_contemporary_or_scholarly",
            collection_name="Obituaries",
            rights_notes="Used to corroborate the 1942 Army entry, Master Sergeant promotion, and wartime chronology; postwar employment is not projected backward.",
        ),
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": "united-states-army-b1055",
            "organization_id": "28a26f92-78af-5a1a-9c09-a843eb5975b4",
            "canonical_name": "United States Army",
            "historical_name": "U.S. Army",
            "aliases": ["Army", "Army Airborne"],
            "organization_type": "military service",
            "sector": "military",
            "country": "United States",
            "active_dates": "1775-present",
            "normalization_notes": "Existing primary Army organization reused; Army Airborne and paratrooper wording remains on the individual affiliations.",
        },
        {
            "key": "davidson-college-b1055",
            "organization_id": "c575d000-7066-5975-89cd-b282792ec7f6",
            "canonical_name": "Davidson College",
            "historical_name": "Davidson College",
            "aliases": [],
            "organization_type": "college",
            "sector": "academia_and_research",
            "city": "Davidson",
            "state_or_region": "North Carolina",
            "country": "United States",
            "normalization_notes": "Existing canonical organization reused; student status is never classified as employment.",
        },
    ]


def army_affiliation_key(row: int) -> str:
    return f"{slug(PEOPLE[row][1])}-army-entry-occupation-b1055"


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
                "key": "henry-d-mcintosh-army-airborne-b1055",
                "person_id": PEOPLE[23][0],
                "organization_key": "united-states-army-b1055",
                "organization_name_as_found": "Army Airborne",
                "role_title": "Army Airborne officer",
                "occupation": "military officer",
                "relationship_type": "military_assignment",
                "start_date": "1943",
                "date_precision": "The ACC profile says McIntosh entered Army Airborne after graduating in 1943 and was quickly transferred to OSS; no exact dates or unit are stated.",
                "country": "United States",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "explicit_immediate",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Army Airborne is the explicitly documented predecessor assignment and is not a civilian employer.",
            },
            {
                "key": "henry-d-mcintosh-davidson-college-b1055",
                "person_id": PEOPLE[23][0],
                "organization_key": "davidson-college-b1055",
                "organization_name_as_found": "Davidson College",
                "role_title": "student",
                "occupation": "student",
                "relationship_type": "student",
                "end_date": "1943",
                "date_precision": "The ACC profile says McIntosh graduated in 1943 immediately before entering Army Airborne.",
                "city": "Davidson",
                "state_or_region": "North Carolina",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "This is a student affiliation, not an employer. It is therefore excluded from last-civilian-employer analytics.",
            },
            {
                "key": "calvin-c-mckee-united-states-army-b1055",
                "person_id": PEOPLE[42][0],
                "organization_key": "united-states-army-b1055",
                "organization_name_as_found": "U.S. Army",
                "role_title": "paratrooper and combat-intelligence soldier",
                "occupation": "soldier",
                "relationship_type": "military_assignment",
                "start_date": "1942-10-31",
                "end_date": "1945-10",
                "date_precision": "The obituary dates Army service from 1942-10-31 through October 1945; institutional history documents OSS service but not the exact transfer date.",
                "country": "United States",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "probable_immediate",
                "identity_confidence": "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "publish_qualified",
                "research_notes": "The Army is the best-supported wartime institutional pathway, but the exact Army-to-OSS transfer remains for Box 508 review.",
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
        if row in {26, 43}:
            values.append(
                claim(
                    f"identity-{slug(PEOPLE[row][1])}-army-b1055",
                    row,
                    "identity",
                    f"The indexed {PEOPLE[row][1]} has a high-confidence match to an official Army entry.",
                    "The normalized full name and a reviewed nonshared protected identifier agree; the identifier remains private.",
                    "High confidence from exact normalized full-name agreement and a unique protected-identifier match.",
                    "The Army entry establishes wartime identity context but not the exact OSS sequence.",
                    "A_direct_official",
                    "high",
                    "published",
                    "Identity crosswalk only; the Army category is assessed separately and is not a named employer.",
                    [{"source_key": INDEX, "support_type": "context_only"}, {"source_key": ARMY}],
                )
            )
        values.append(
            claim(
                f"army-entry-{slug(PEOPLE[row][1])}-b1055",
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

    henry_identity = "High confidence from the exact indexed first name and middle initial, indexed captain rank, official NPS full-name and lieutenant evidence, and the ACC's explicit Army Airborne-to-OSS chronology."
    calvin_identity = "High confidence from the exact name and middle initial, indexed Master Sergeant rank, institutional OSS history, and an obituary documenting promotion to Master Sergeant during wartime Army service."
    values.extend(
        [
            claim(
                "identity-henry-deane-mcintosh-b1055",
                23,
                "identity",
                "The indexed Captain Henry D. McIntosh is a high-confidence match to Lieutenant Henry Deane McIntosh, the Davidson graduate, Army Airborne officer, OSS Jedburgh, and physician.",
                "The ACC gives the Davidson-Army-OSS sequence; the National Park Service supplies the full middle name, lieutenant rank, Jedburgh service, and matching medical career.",
                henry_identity,
                "Both sources describe wartime service and the sequence into OSS.",
                "B_authoritative_institutional",
                "high",
                "published",
                "The identity rests on converging name, middle initial, rank, OSS assignment, education, and postwar profession rather than name alone.",
                [{"source_key": INDEX, "support_type": "context_only"}, {"source_key": ACC}, {"source_key": NPS}],
            ),
            claim(
                "henry-d-mcintosh-army-airborne-b1055",
                23,
                "immediate_pre_oss_affiliation",
                "Henry Deane McIntosh entered Army Airborne after graduating from Davidson College in 1943 and was quickly transferred to OSS.",
                "The ACC profile directly states the Davidson-to-Army Airborne-to-OSS sequence.",
                henry_identity,
                "Explicit immediate sequence; exact transfer date and Army unit are not stated.",
                "B_authoritative_institutional",
                "high",
                "published",
                "Army Airborne is a military assignment, not a civilian employer.",
                [{"source_key": ACC}, {"source_key": NPS, "support_type": "context_only"}],
                "henry-d-mcintosh-army-airborne-b1055",
                "graduated from Davidson College in 1943. He then entered the Army Airborne but was quickly transferred to the OSS",
            ),
            claim(
                "henry-d-mcintosh-davidson-college-b1055",
                23,
                "other_pre_oss_affiliation",
                "Henry Deane McIntosh graduated from Davidson College in 1943 immediately before entering Army Airborne.",
                "The ACC profile names Davidson College, gives the graduation year, and directly follows it with Army entry.",
                henry_identity,
                "Strongly date-bounded student status before military and OSS service.",
                "B_authoritative_institutional",
                "high",
                "published",
                "Davidson is modeled as a student institution, never as an employer.",
                [{"source_key": ACC}],
                "henry-d-mcintosh-davidson-college-b1055",
            ),
            claim(
                "identity-peter-andrew-hannay-mckeand-b1055",
                41,
                "identity",
                "The indexed Peter A.H. McKeand is a probable match to Royal Air Force officer Peter Andrew Hannay McKeand.",
                "The official London Gazette expands the rare A.H. initials to Andrew Hannay, and Fettes College independently records Wing Commander Peter A. H. McKeand.",
                "Probable from a highly distinctive exact surname and four-part initial pattern corroborated by official and institutional RAF records; neither source independently states OSS service.",
                "The reviewed records are postwar and cannot establish a pre-OSS affiliation or transfer sequence.",
                "A_direct_official",
                "medium",
                "publish_qualified",
                "Personnel-file review remains mandatory before promoting the identity or transferring any RAF chronology into pre-OSS claims.",
                [{"source_key": INDEX, "support_type": "context_only"}, {"source_key": GAZETTE}, {"source_key": FETTES}],
            ),
            claim(
                "identity-calvin-charles-mckee-b1055",
                42,
                "identity",
                "The indexed Master Sergeant Calvin C. McKee is a high-confidence match to Calvin Charles McKee, the Army paratrooper and OSS veteran.",
                "Oklahoma's military hall gives the exact full name and OSS service; the obituary documents wartime Army service and promotion to Master Sergeant.",
                calvin_identity,
                "The sources establish Army service beginning in 1942 and OSS service during the war but do not give an exact transfer date.",
                "B_authoritative_institutional",
                "high",
                "published",
                "The rank, middle initial, exact name, and explicit OSS history provide multiple identifiers beyond the name.",
                [{"source_key": INDEX, "support_type": "context_only"}, {"source_key": OKMHOF}, {"source_key": FITZGERALD}],
            ),
            claim(
                "calvin-c-mckee-united-states-army-b1055",
                42,
                "immediate_pre_oss_affiliation",
                "Calvin Charles McKee's best-supported immediate institutional pathway to OSS was through wartime United States Army service, beginning in 1942.",
                "The obituary dates Army entry and describes paratrooper and combat-intelligence service; Oklahoma's military hall independently documents his OSS service.",
                calvin_identity,
                "Probable immediate pathway; the exact Army-to-OSS transfer date and unit remain unverified.",
                "B_authoritative_institutional",
                "medium",
                "publish_qualified",
                "This is visibly qualified military-assignment evidence, not a civilian employer claim.",
                [{"source_key": FITZGERALD}, {"source_key": OKMHOF}],
                "calvin-c-mckee-united-states-army-b1055",
                "Calvin voluntarily enlisted in the U.S. Army on October 31, 1942, at the age of 19 years old.",
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
        if row in ARMY_OCCUPATIONS:
            update.update(
                identity_status="high_confidence",
                identity_evidence="The official index and Army entry agree in normalized full name and a reviewed nonshared private identifier. The identifier remains private; the dated broad category does not establish an employer or OSS sequence.",
                nara_catalog_id="1263923",
                research_status="occupation_only_found",
                next_action=f"Review Box {box} for a named employer or institution and establish the Army-to-OSS chronology.",
                archival_review_priority="high",
            )
        elif row == 23:
            update.update(
                identity_status="high_confidence",
                identity_evidence="The exact first name and middle initial, indexed captain rank, official NPS full-name and lieutenant evidence, and ACC Army Airborne-to-OSS chronology support a high-confidence match.",
                name_variants=["Henry Deane McIntosh"],
                research_status="occupation_only_found",
                next_action="Review Box 507 for exact Army Airborne and OSS transfer dates and for any civilian employment distinct from Davidson student status.",
                archival_review_priority="medium",
            )
        elif row == 33:
            update.update(
                manual_review_required=False,
                research_status="verified_employer_found",
                next_action="Review Box 508 for McKay's Harvard leave, COI appointment, and OSS transfer documentation.",
                archival_review_priority="medium",
            )
        elif row == 41:
            update.update(
                identity_status="probable",
                identity_evidence="The rare Peter A.H. McKeand index form aligns with official Peter Andrew Hannay McKeand and Fettes College's Wing Commander Peter A. H. McKeand, but neither reviewed source independently establishes OSS service.",
                name_variants=["Peter Andrew Hannay McKeand", "Peter A H McKeand"],
                research_status="needs_identity_review",
                next_action="Review Box 508 to confirm the Peter Andrew Hannay McKeand identity and establish the RAF-to-OSS sequence and any pre-service civilian role.",
                archival_review_priority="critical",
            )
        elif row == 42:
            update.update(
                identity_status="high_confidence",
                identity_evidence="Exact name and middle initial, indexed Master Sergeant rank, institutional OSS history, and an obituary documenting wartime promotion to Master Sergeant support a high-confidence match.",
                name_variants=["Calvin Charles McKee"],
                research_status="occupation_only_found",
                next_action="Review Box 508 for the exact Army-to-OSS transfer, wartime unit, and any civilian affiliation before Army entry in 1942.",
                archival_review_priority="medium",
            )
        elif row in CONFLICT_ROWS:
            update.update(
                identity_status="conflicting",
                research_status="conflicting_sources",
                next_action=(
                    "Review Box 507 and the original index documentation to resolve the protected-identifier and full-name conflict before making identity or employment claims."
                    if row == 7
                    else "Review Box 507 and the original index documentation to resolve the G/F middle-initial conflict before making identity or employment claims."
                ),
                archival_review_priority="critical",
            )
        elif row == 8:
            update.update(
                identity_status="high_confidence",
                identity_evidence="The official index and Army entry agree in normalized full name and a reviewed nonshared private identifier, but the Army-entry date is 1946-07-25 and cannot support a pre-OSS occupation claim.",
                nara_catalog_id="1263923",
                research_status="requires_archival_review",
                next_action="Review Box 507 for William T. McGuire's actual pre-OSS affiliation; do not project the post-OSS 1946-07-25 Army category backward.",
                archival_review_priority="high",
            )
        elif row in DUPLICATE_ROWS:
            update.update(
                identity_status="ambiguous",
                identity_evidence="Adjacent printed rows share the Carolyn McIntosh name but differ in middle initial, civilian grade, and box. They remain separate without direct duplicate evidence.",
                possible_duplicate_group="p310-carolyn-mcintosh-adjacent-distinct-rows-b1055",
                research_status="needs_identity_review",
                next_action="Compare the Carolyn McIntosh personnel files in Boxes 507 and 508 before merging, transferring evidence, or assigning an employer.",
                archival_review_priority="critical",
            )
        else:
            update.update(
                identity_status="unresolved",
                identity_evidence="Exact-name and meaningful-variant checks across the official index context, CIA-domain discovery, accessible military and institutional sources, newspaper or obituary discovery, and archival searches produced no reliable identity and pre-OSS affiliation bridge; unbridged namesakes were rejected.",
                research_status="requires_archival_review",
                next_action=unresolved_message(name, box),
                archival_review_priority="high",
            )
        values.append(update)
    if len(values) != 46 or len({item["person_id"] for item in values}) != 46:
        raise RuntimeError("Expected 46 separate page-310 person updates")
    return values


def outcome_note(row: int) -> str:
    if row in ARMY_OCCUPATIONS:
        return "An accepted official Army identity link supports a qualified dated occupation or student category but no named employer or OSS-transfer sequence."
    if row == 23:
        return "Institutional and official historical sources establish Davidson student status and an explicit Army Airborne-to-OSS pathway for Henry Deane McIntosh."
    if row == 33:
        return "Existing reviewed evidence for Donald C. McKay's Harvard employment and COI-to-OSS pathway was preserved; this pass added a terminal protocol attempt without duplicating claims."
    if row == 41:
        return "Official and institutional RAF records support a probable rare-name identity, but Box 508 is required to confirm the OSS linkage and pre-OSS chronology."
    if row == 42:
        return "Institutional and obituary evidence establish Calvin Charles McKee's Army and OSS service; the exact transfer and any pre-Army affiliation remain unresolved."
    if row in CONFLICT_ROWS:
        return "The existing protected-identifier conflict remains visible; no occupation or employer was transferred."
    if row in DUPLICATE_ROWS:
        return "The adjacent Carolyn McIntosh rows remain separate pending direct personnel-file comparison."
    if row == 8:
        return "An accepted Army identity link is dated after OSS ended, so no pre-OSS occupation is projected backward."
    return "No reliable identity or pre-OSS affiliation was established; unbridged namesakes and chronologically irrelevant results were rejected."


def research_attempts() -> list[dict[str, object]]:
    updates = {item["person_id"]: item for item in person_updates()}
    values: list[dict[str, object]] = []
    for row, (person_id, name, box) in PEOPLE.items():
        if row in POSITIVE_ROWS:
            outcome, reviewed, rejected = "source_reviewed", 5, 2
        elif row in CONFLICT_ROWS | DUPLICATE_ROWS:
            outcome, reviewed, rejected = "candidate_rejected", 3, 4
        elif row == 8:
            outcome, reviewed, rejected = "source_reviewed", 3, 2
        else:
            outcome, reviewed, rejected = "no_result", 2, 3
        values.append(
            {
                "key": f"page310-row{row}-{slug(name)}-b1055",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index context; exact-name and meaningful initial, punctuation, spacing, spelling and OCR variants; CIA-domain discovery; OSS, rank, branch, assignment and private-identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory and archival searches; indexed Box {box}",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_1055",
                "started_at": "2026-11-11T16:35:00-05:00",
                "completed_at": "2026-11-11T18:05:00-05:00",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, postwar-only leads, and sources without an OSS, rank, private-identifier, unit, or personnel-file bridge were rejected. The common-name William McKay OSS veteran was not transferred to William M. McKay without two corroborating identifiers. Army categories were not converted into named employers, and postwar careers were not projected backward.",
                "research_notes": f"{outcome_note(row)} Page 310 was visually checked against a fresh official NARA download matching the preserved SHA-256. The official index, existing Library of Congress attempts where present, exact-name OSS and meaningful-variant discovery, CIA-domain checks, employment and occupation checks, and obituary, institutional, directory, newspaper, and archival searches were reviewed as applicable. CIA-domain searches returned no person-specific result and were not treated as proof of absence. No search-result snippet was used as final evidence and no authenticated NARA Catalog API request was made.",
                "next_action": str(updates[person_id]["next_action"]),
                "attempt_number": ATTEMPT_NUMBERS[row],
                "research_agent_version": "before-oss-b1055-v1",
            }
        )
    if len(values) != 46 or len({item["person_id"] for item in values}) != 46:
        raise RuntimeError("Expected 46 separate page-310 research attempts")
    return values


def build_bundle() -> dict[str, object]:
    return {
        "bundle_version": "batch-1055-v1",
        "reviewer": "Before OSS Batch 1055 evidence review",
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
