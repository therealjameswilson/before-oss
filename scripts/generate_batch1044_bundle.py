#!/usr/bin/env python3
"""Generate the reviewed Batch 1044 evidence bundle for PDF page 299."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page299-nicholas-g-maslikosa-to-william-a-mathewson-review_"
    "batch-1044_2026-11-05.json"
)

INDEX = "nara-index-b1044"
ARMY = "army-bulk-b1044"
TECH = "army-tech-b1044"
CODES = "army-codes-b1044"
MATERAZZI_ISRAL = "isral-materazzi-b1044"
MATERAZZI_NPS = "nps-materazzi-b1044"
MATERAZZI_NPS_DAILY = "nps-materazzi-daily-life-b1044"
MASLIKOSA_VALOR = "military-times-maslikosa-b1044"
MASLOWSKY_101 = "detachment101-maslowsky-b1044"
MASTROS_ROSTER = "hellenic-news-mastros-b1044"

ORG_ARMY_ENGINEERS = "org-army-engineers-b1044"
ORG_ARMY_MAP_SERVICE = "org-army-map-service-b1044"


PEOPLE = {
    1: ("29c9d876-b149-5a52-8a77-8704e9398b73", "Nicholas G Maslikosa", "489"),
    2: ("2bd2124f-a3c2-541e-be6d-1ce03721b3f1", "Edward S Maslowsky", "489"),
    3: ("e6aaa1ce-31ca-5603-9321-0946e71ffaee", "Raymond K Masnaghetti", "489"),
    4: ("9fdf5f8f-1950-515d-a7d6-c5b1ad6879d0", "Clyde E Mason", "490"),
    5: ("f473f7bd-c530-50c6-89a7-44b5eb38f42f", "Dorothy Mason", "490"),
    6: ("e3b15c03-9d62-5a59-8ac0-117fe8e68bef", "Edward S Mason", "490"),
    7: ("c24691c1-7f8c-5930-b203-acdc527bd259", "Elizabeth P Mason", "490"),
    8: ("b393f4c3-c720-5772-abc1-1bcd2e018784", "Harry W Mason", "490"),
    9: ("8febcfb0-f2be-58ed-9b97-bb3ad6e9e036", "Julien J Mason", "490"),
    10: ("1a474d45-a908-59a1-a23e-2270edd839a5", "Leonard E Mason", "490"),
    11: ("6e049fa8-805f-561f-835f-359e045dc037", "Marie Mason", "490"),
    12: ("639c6b4e-9a76-5b54-9b2d-5e2cef0df533", "George H Masselman", "490"),
    13: ("440f2217-af5a-53af-b7a4-601376126c07", "Gene Massett", "490"),
    14: ("1d6d7b1a-39e9-55ce-a2ec-c9f9aa102b70", "John A Massey", "490"),
    15: ("fe71fade-aaca-517f-a7c9-0ca2fa88dabb", "Virginia E Massey", "490"),
    16: ("d1d8c434-bc7a-5a83-a8f3-06de7960583a", "Alex B Massie Jr.", "490"),
    17: ("c0b1c0eb-c70a-5f9a-a6e1-136cd6c7586f", "Charles W Massie Jr.", "490"),
    18: ("62709823-a3bf-5ed9-a0f4-3ff9188c53e4", "Evelyn D Massie Jr.", "490"),
    19: ("58c7a4e3-16a0-5317-ad51-38db20dbfb75", "Hedwig I Massing", "490"),
    20: ("35af5e6e-7e92-531f-97ef-ed060d012c2f", "Paul W Massing", "490"),
    21: ("21ac50fe-047a-5640-a78c-51f9ddfe35d4", "Fred M Mast Jr.", "490"),
    22: ("6484739b-d244-5fd1-bd1c-5fcbfb14b387", "Elroy P Master", "490"),
    23: ("b5c14ab5-4c10-58d5-8f44-62df33e55d12", "Alvin M Masterson", "490"),
    24: ("8ef8b29f-91ce-5013-b0e0-d91dbe3fb2dc", "Clayton O Masterson", "490"),
    25: ("7397a953-4a4a-567d-a47d-f4f4ee82696f", "Leo J Masterson", "490"),
    26: ("23028d53-546b-582a-a116-443d36e28393", "Louis V Mastrangelo", "490"),
    27: ("13372639-5c1a-5c52-a0bf-973c8479bcca", "Francesco Mastrocola", "490"),
    28: ("699dc478-5ee2-5d00-a097-83b0b547ca48", "Steve J Mastros", "490"),
    29: ("ce2bbe26-4df1-5f19-88cd-be706289f2a6", "Felix S Masucci", "490"),
    30: ("2809c292-d795-57e1-9fa7-86f30c016108", "Joe Y Masuda", "490"),
    31: ("12186952-87d5-5b15-ab27-d16fbdb6494a", "Thomas Masuda", "490"),
    32: ("42900e5c-30b7-5a7f-927e-18799b2428bf", "Albert M Matakonis", "491"),
    33: ("1c51a5e9-b1f8-527e-8416-2f4ecb1c926a", "Brunislaw J Matejcak", "491"),
    34: ("87f52b08-72d7-5e63-a651-dd26bc0865e2", "Raymond A Matejcek", "491"),
    35: ("94583f40-5aa1-5ff8-89cc-69b0a1cd96e2", "Albert R Materazzi", "491"),
    36: ("d147cbfe-7201-5e9e-b7d9-ff45b955e249", "Dimitrious Matheos", "491"),
    37: ("91f28590-f119-517b-80e9-b9f7b4702ebd", "Lester E Mather", "491"),
    38: ("5659d019-f9b9-5387-abbc-2f1632925bed", "Robert L Mathes", "491"),
    39: ("861a2a63-0874-5bc2-b893-0e997ace063d", "Frederick Matheson", "491"),
    40: ("c3274913-07c3-5cc6-a9a3-6403f409e81c", "Andrew J Mathews", "491"),
    41: ("0b1b7345-f31f-5c45-b270-9d9a6f27e151", "Elwood K Mathews", "491"),
    42: ("5ae134b6-03a7-56fa-9a37-a6077ed848fe", "Eugene K Mathews", "491"),
    43: ("bcf9c6da-3902-5f9f-b1ef-8a06c6863111", "Martha E Mathews", "491"),
    44: ("f3f910a4-e024-5979-9c24-6a881d72bc6a", "Marthiel D Mathews", "491"),
    45: ("a27caeba-b3ec-554e-ac05-2ad01dfec307", "Yvonne M Mathews", "491"),
    46: ("e1ffea33-f916-55b6-8b69-bc583218f990", "William A Mathewson", "491"),
}


# Every category below was checked against the current official NARA AAD code list.
# The list supplies broad historical categories, never a named employer or workplace.
ARMY_ASSOCIATIONS = {
    3: ("1942-11-18", "702", "semiskilled automobile-manufacturing worker, not elsewhere classified", "Semiskilled occupations in manufacture of automobiles, n.e.c.", "unknown", "confirmed"),
    8: ("1943-06-26", "665", "semiskilled glass-products manufacturing worker", "Semiskilled occupations in production of glass and glass products", "unknown", "confirmed"),
    9: ("1943-06-09", "006", "author, editor, or reporter", "Authors, editors, and reporters", "unknown", "confirmed"),
    14: ("1942-10-15", "187", "salesman or sales agent, except to consumers", "Salesmen and sales agents, except to consumers", "unknown", "confirmed"),
    16: ("1942-10-16", "716", "semiskilled painter, except construction and maintenance", "Semiskilled painters, except construction and maintenance", "unknown", "confirmed"),
    21: ("1943-04-15", "992", "student", "Students", "student", "high_confidence"),
    26: ("1943-02-18", "736", "semiskilled chauffeur or driver of a bus, taxi, truck, or tractor", "Semiskilled chauffeurs and drivers, bus, taxi, truck, and tractor", "unknown", "confirmed"),
    27: ("1943-05-20", "768", "packing, filling, labeling, marking, or bottling worker", "Packing, filling, labeling, marking, bottling, and related occupations, n.e.c.", "unknown", "confirmed"),
    29: ("1942-11-25", "105", "general office clerk", "Clerks, general office", "unknown", "confirmed"),
    32: ("1943-07-21", "521", "skilled miner or mining-machine operator", "Skilled miners and mining-machine operators", "unknown", "confirmed"),
    33: ("1942-03-02", "678", "semiskilled machine-shop or related worker, not elsewhere classified", "Semiskilled machine shop and related occupations, n.e.c.", "unknown", "high_confidence"),
    36: ("1943-02-11", "226", "cook, except in a private family", "Cooks, except private family", "unknown", "high_confidence"),
    39: ("1944-07-03", "031", "secondary-school teacher or principal", "Teachers (secondary school) and principals", "unknown", "high_confidence"),
    41: ("1945-05-16", "992", "student", "Students", "student", "high_confidence"),
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
            archival_identifier="RG 226, Entry A1-224, Boxes 489-491",
            title="OSS Personnel Files from Excel",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="2010-12-23",
            locator="PDF page 299, rows 1-46; every printed row visually checked",
            source_quality="A_direct_official",
            collection_name="Records of the Office of Strategic Services, Record Group 226",
            rights_notes="All rows remain separate. The odd Evelyn D. Massie Jr. suffix, variant grades, damaged Steve Mastros identifier, and exact printed spellings remain recoverable.",
        ),
        source(
            ARMY,
            stable_url="https://catalog.archives.gov/id/1263923",
            archival_identifier="National Archives Identifier 1263923; parent series NAID 604357",
            title="Electronic Army Serial Number Merged File, ca. 1938-1946",
            author_creator="Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="1938-1946; merged file created 2002",
            locator="Official unrestricted ASNEF.FIN.DAT; 15 protected candidates explicitly reviewed; 14 accepted and one rejected",
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
            locator="Current AAD values for codes 006, 031, 105, 187, 226, 521, 665, 678, 702, 716, 736, 768, and 992; printed reference-copy pages 170-176 and 304",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records code lists",
            rights_notes="Every used value was visually checked. Categories identify neither employer, institution, workplace, nor exact Army-to-OSS sequence.",
        ),
        source(
            MATERAZZI_ISRAL,
            stable_url="https://www.isral.it/wp-content/uploads/2018/12/QSC20_lunati.pdf",
            archival_identifier="Fondo Albert Materazzi; Quaderno di storia contemporanea no. 20",
            title="L'Archivio del Fondo Materazzi",
            author_creator="Gabriele Lunati",
            repository_publisher="Istituto per la storia della resistenza e della società contemporanea in provincia di Alessandria (ISRAL)",
            publication_record_date="1996; web copy 2018",
            locator="PDF physical page 7, note 1",
            source_quality="B_authoritative_institutional",
            collection_name="Fondo Albert Materazzi",
            rights_notes="The archival finding-aid essay provides a compact chronology and points to original OSS records in RG 226, Entry 143, Boxes 11-12.",
        ),
        source(
            MATERAZZI_NPS,
            stable_url="https://www.nps.gov/parkhistory/online_books/oss/chap8.pdf",
            archival_identifier="OSS Training in the National Parks and Service Abroad in World War II, chapter 8",
            title="OSS in Action: The Mediterranean and European Theaters",
            author_creator="John W. Chambers II",
            repository_publisher="National Park Service",
            publication_record_date="2008",
            locator="PDF page 305; notes 61-62",
            source_quality="A_direct_official",
            collection_name="OSS Training in the National Parks and Service Abroad in World War II",
            rights_notes="The official history identifies Materazzi as the first Italian Operational Group's operations officer and documents recruitment of that group from U.S. Army units.",
        ),
        source(
            MATERAZZI_NPS_DAILY,
            stable_url="https://www.nps.gov/articles/daily-life-in-camp-park-and-town.htm",
            archival_identifier="National Park Service OSS training history, Daily Life in Camp, Park, and Town",
            title="Daily Life in Camp, Park, and Town",
            author_creator="National Park Service",
            repository_publisher="National Park Service",
            locator="Security investigations and Espionage and Sabotage Exercises sections",
            source_quality="A_direct_official",
            collection_name="OSS Training in the National Parks and Service Abroad in World War II",
            rights_notes="The official history identifies Materazzi as an engineering officer from Hershey who volunteered for the Italian Operational Group.",
        ),
        source(
            MASLIKOSA_VALOR,
            stable_url="https://valor.militarytimes.com/recipient/recipient-85343/",
            archival_identifier="35th Infantry Division General Orders No. 13 (1944)",
            title="Nicholas G. Maslikosa: Silver Star",
            author_creator="Military Times Hall of Valor",
            repository_publisher="Military Times",
            publication_record_date="1944-08-04 order; online compilation",
            locator="Award record for action on 1944-07-14",
            source_quality="C_reputable_contemporary_or_scholarly",
            collection_name="Hall of Valor",
            rights_notes="Used only for a rank-and-name identity bridge and wartime Army context; no pre-OSS employer or transfer chronology is inferred.",
        ),
        source(
            MASLOWSKY_101,
            stable_url="https://www.javadc.org/java/docs/1945-03-15%20OSSSU%20Detachment%20101%20Promotions%20and%20Citations%20OCR%20P11_MA.pdf",
            archival_identifier="OSS Detachment 101 promotions and citations, 1945",
            title="OSS Detachment 101 Promotions and Citations",
            author_creator="Office of Strategic Services Detachment 101",
            repository_publisher="Jungle Aviation and Radio Service / JAVA Research Archive",
            publication_record_date="1945",
            locator="Promotions and citations report; Edward S. Maslowsky entry, staff sergeant to technical sergeant",
            source_quality="C_reputable_contemporary_or_scholarly",
            collection_name="OSS Detachment 101 records",
            rights_notes="The hosted archival document confirms wartime identity and rank only; it supplies no pre-OSS employer.",
        ),
        source(
            MASTROS_ROSTER,
            stable_url="https://hellenicnews.com/2020/01/23/the-us-greek-battalion-wwii/",
            archival_identifier="Greek Operational Group rosters, Groups III and VII",
            title="The Greek-American Volunteers of the Greek Battalion, WWII",
            author_creator="Hellenic News of America",
            repository_publisher="Hellenic News of America",
            publication_record_date="2020-01-23",
            locator="Greek Operational Groups III and VII rosters",
            source_quality="C_reputable_contemporary_or_scholarly",
            collection_name="Greek-American wartime history",
            rights_notes="The uncommon exact name appears in two OSS Greek Operational Group rosters. The later staff-sergeant rank is treated as compatible context, not a correction to the index.",
        ),
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": ORG_ARMY_ENGINEERS,
            "organization_id": "f2367526-082d-5cad-8156-c405c426f2e1",
            "canonical_name": "United States Army Corps of Engineers",
            "historical_name": "Army Corps of Engineers",
            "aliases": ["Engineer Corps", "U.S. Army Corps of Engineers", "Army Engineering Corps"],
            "organization_type": "military branch",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "The Italian institutional source's 'genio' wording is normalized to the Corps of Engineers while preserving the source wording in the claim. Military service is not civilian employment.",
        },
        {
            "key": ORG_ARMY_MAP_SERVICE,
            "organization_id": "6ccf6e60-2936-5b97-b21e-c629128391a7",
            "canonical_name": "United States Army Map Service",
            "historical_name": "Army Map Service",
            "aliases": ["U.S. Army Map Service", "ARMY Map Service"],
            "organization_type": "federal mapping agency",
            "sector": "federal_government",
            "city": "Washington",
            "state_or_region": "District of Columbia",
            "country": "United States",
            "normalization_notes": "The historical source wording is retained exactly even though it predates the agency's formal 1942 naming. No modern successor agency is substituted.",
        },
    ]


def army_affiliation_key(row: int) -> str:
    return f"{slug(PEOPLE[row][1])}-army-association-b1044"


def army_identity_assessment(row: int) -> str:
    if row == 21:
        return "High confidence from a nonshared protected linkage and a damaged Army rendering that preserves Fred, M, Jr., and the surviving surname letters; the damage remains explicit."
    if row == 32:
        return "Confirmed by exact name agreement and a nonshared protected linkage; the damaged Army grade is not used to alter the index."
    if row == 33:
        return "High confidence from the rare Matejcak/Matejczak and Brunislaw/Bronislaw variants plus a nonshared protected linkage; every spelling remains visible."
    if row == 36:
        return "High confidence from the uncommon surname, Dimitrious/Dimtrious letter transposition, and a nonshared protected linkage; the source typo remains visible."
    if row == 39:
        return "High confidence from exact first name and surname plus a nonshared protected linkage; the Army record's added middle initial is retained only as a variant."
    if row == 41:
        return "High confidence from the uncommon full name, Mathews/Mathew surname variant, and a nonshared protected linkage; both spellings remain visible."
    return "Confirmed by exact official name agreement and a nonshared protected linkage; the protected identifier remains private."


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, _label, relationship, identity) in ARMY_ASSOCIATIONS.items():
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
            "identity_confidence": identity,
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

    values.extend(
        [
            {
                "key": "albert-r-materazzi-army-engineers-b1044",
                "person_id": PEOPLE[35][0],
                "organization_key": ORG_ARMY_ENGINEERS,
                "organization_name_as_found": "genio",
                "role_title": "second lieutenant; engineering officer",
                "relationship_type": "military_assignment",
                "start_date": "1942",
                "end_date": "1943-early",
                "date_precision": "ISRAL places Materazzi in the engineers as a second lieutenant in 1942 and in contact with OSS recruiters at the beginning of 1943; NPS independently calls him an engineering officer who volunteered for the Italian Operational Group.",
                "country": "United States",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "confirmed",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Best-supported immediate military pathway into OSS. The sources do not supply an exact transfer date or unit below the Corps of Engineers.",
            },
            {
                "key": "albert-r-materazzi-army-map-service-b1044",
                "person_id": PEOPLE[35][0],
                "organization_key": ORG_ARMY_MAP_SERVICE,
                "organization_name_as_found": "ARMY Map Service",
                "role_title": "chemist",
                "occupation": "chemist",
                "relationship_type": "employment",
                "start_date": "1940",
                "end_date": "1942 or earlier",
                "date_precision": "ISRAL explicitly places Materazzi as an Army Map Service chemist in 1940 and next identifies him as an Army engineering second lieutenant in 1942; the exact employment end date is not stated.",
                "city": "Washington",
                "state_or_region": "District of Columbia",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "confirmed",
                "claim_confidence": "medium",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "publish_qualified",
                "research_notes": "Best-supported last identified civilian employer before military service. A 1940 role is documented, but continuity through the 1942 commission is not assumed.",
            },
        ]
    )
    return values


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, label, relationship, _identity) in ARMY_ASSOCIATIONS.items():
        values.append(
            {
                "key": f"army-{slug(PEOPLE[row][1])}-b1044",
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
                "key": "identity-nicholas-g-maslikosa-b1044",
                "person_id": PEOPLE[1][0],
                "claim_type": "identity",
                "claim_text": "Indexed Second Lieutenant Nicholas G. Maslikosa is strongly supported as the Army officer decorated for action in Normandy in July 1944.",
                "evidence_paraphrase": "The award record supplies the exact uncommon name, middle initial, second-lieutenant rank, Army service, division, and dated action.",
                "identity_match_assessment": "High confidence from the rare exact name, matching middle initial and second-lieutenant rank, and compatible wartime Army chronology; Box 489 remains unreviewed.",
                "temporal_assessment": "Wartime Army identity only; the award record does not establish a pre-OSS employer or transfer sequence.",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "claim_confidence": "high",
                "publication_status": "publish_qualified",
                "match_notes": "The award and division are identity context, not evidence that the 35th Infantry Division immediately preceded OSS.",
                "sources": [{"source_key": MASLIKOSA_VALOR}, {"source_key": INDEX, "support_type": "context_only"}],
            },
            {
                "key": "identity-edward-s-maslowsky-b1044",
                "person_id": PEOPLE[2][0],
                "claim_type": "identity",
                "claim_text": "Indexed Technical Sergeant Edward S. Maslowsky is strongly supported as the OSS Detachment 101 member promoted from staff sergeant to technical sergeant.",
                "evidence_paraphrase": "The wartime Detachment 101 report gives the uncommon exact name and the promotion to the rank printed in the index.",
                "identity_match_assessment": "High confidence from the rare exact name, middle initial, explicit OSS Detachment 101 context, and matching technical-sergeant rank.",
                "temporal_assessment": "Wartime OSS identity and promotion context only; no pre-OSS employer or predecessor assignment is supplied.",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "claim_confidence": "high",
                "publication_status": "publish_qualified",
                "match_notes": "No occupation or employer is inferred from a promotion report.",
                "sources": [{"source_key": MASLOWSKY_101}, {"source_key": INDEX, "support_type": "context_only"}],
            },
            {
                "key": "identity-steve-j-mastros-b1044",
                "person_id": PEOPLE[28][0],
                "claim_type": "identity",
                "claim_text": "Indexed Steve J. Mastros is strongly supported as the OSS Greek Operational Group member listed in Groups III and VII.",
                "evidence_paraphrase": "Two rosters reproduce the uncommon exact name in Greek Operational Groups III and VII and show a later staff-sergeant rank.",
                "identity_match_assessment": "High confidence from the uncommon exact full name, explicit OSS Greek Operational Group context, and compatible enlisted-rank progression; the damaged index identifier is not used.",
                "temporal_assessment": "Wartime OSS assignment context only; the rosters do not identify a pre-OSS employer or earlier Army unit.",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "claim_confidence": "high",
                "publication_status": "publish_qualified",
                "match_notes": "The index's private rank is preserved; the roster rank is treated as later context rather than a silent correction.",
                "sources": [{"source_key": MASTROS_ROSTER}, {"source_key": INDEX, "support_type": "context_only"}],
            },
            {
                "key": "identity-albert-r-materazzi-b1044",
                "person_id": PEOPLE[35][0],
                "claim_type": "identity",
                "claim_text": "Indexed Captain Albert R. Materazzi is confirmed as the first Italian Operational Group's operations officer.",
                "evidence_paraphrase": "The official NPS history gives the exact name, captain rank, operations-officer role, Italian Operational Group, and first-person interview source.",
                "identity_match_assessment": "Confirmed by the rare exact name and middle initial, matching captain rank, direct OSS role, NPS oral-history attribution, and independent ISRAL chronology.",
                "temporal_assessment": "The sources document a 1940 civilian role, 1942 Army commission, and early-1943 OSS recruitment sequence.",
                "source_quality": "A_direct_official",
                "claim_confidence": "confirmed",
                "publication_status": "published",
                "match_notes": "Education remains identity context and is not converted into employment.",
                "sources": [{"source_key": MATERAZZI_NPS}, {"source_key": MATERAZZI_ISRAL}, {"source_key": INDEX, "support_type": "context_only"}],
            },
            {
                "key": "immediate-albert-r-materazzi-army-engineers-b1044",
                "person_id": PEOPLE[35][0],
                "affiliation_key": "albert-r-materazzi-army-engineers-b1044",
                "claim_type": "immediate_pre_oss_affiliation",
                "claim_text": "Albert R. Materazzi's best-supported immediate pre-OSS affiliation was as a U.S. Army engineering officer.",
                "evidence_paraphrase": "ISRAL places him as an engineers second lieutenant in 1942 and with OSS recruiters in early 1943; NPS calls him an engineering officer.",
                "identity_match_assessment": "Confirmed by the exact uncommon name, captain index entry, official NPS role, and independent institutional chronology.",
                "temporal_assessment": "Strongly date-bounded: the 1942 Army engineering commission directly precedes documented early-1943 OSS recruitment, though no exact transfer day is supplied.",
                "source_quality": "B_authoritative_institutional",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "The military pathway is kept distinct from civilian employment and is not narrowed to an unsupported unit.",
                "sources": [
                    {"source_key": MATERAZZI_ISRAL, "locator_override": "PDF physical page 7, note 1", "excerpt_override": "Sottotenente del genio nel 1942, all'inizio del 1943 è in contatto con Livermore e Max Corvo"},
                    {"source_key": MATERAZZI_NPS_DAILY, "support_type": "context_only"},
                    {"source_key": MATERAZZI_NPS, "support_type": "context_only"},
                ],
            },
            {
                "key": "last-civilian-albert-r-materazzi-army-map-service-b1044",
                "person_id": PEOPLE[35][0],
                "affiliation_key": "albert-r-materazzi-army-map-service-b1044",
                "claim_type": "last_civilian_pre_service",
                "claim_text": "The Army Map Service is Albert R. Materazzi's last identified civilian employer before military service.",
                "evidence_paraphrase": "ISRAL identifies him as an Army Map Service chemist in 1940 and next as an Army engineering second lieutenant in 1942.",
                "identity_match_assessment": "Confirmed by the exact uncommon name and the same institutional chronology independently linked to his OSS role by NPS.",
                "temporal_assessment": "Documented prewar employment and the last civilian employer identified in the reviewed sequence; the source does not state that employment continued until commission.",
                "source_quality": "B_authoritative_institutional",
                "claim_confidence": "medium",
                "publication_status": "publish_qualified",
                "match_notes": "Published as qualified last-civilian employment. The exact end date and continuity from 1940 to 1942 remain unresolved.",
                "sources": [
                    {"source_key": MATERAZZI_ISRAL, "locator_override": "PDF physical page 7, note 1", "excerpt_override": "Chimico presso la ARMY Map Service nel 1940 e Sottotenente del genio nel 1942"},
                    {"source_key": MATERAZZI_NPS, "support_type": "context_only"},
                ],
            },
            {
                "key": "identity-eugene-k-mathews-conflict-b1044",
                "person_id": PEOPLE[42][0],
                "claim_type": "identity",
                "claim_text": "An automated Army candidate for Eugene K. Mathews was rejected because the protected identifiers conflict.",
                "evidence_paraphrase": "The candidate supplied no defensible protected linkage to the indexed captain, so no Army name, date, grade, or occupation was transferred.",
                "identity_match_assessment": "Ambiguous: a name-based candidate cannot overcome conflicting private identifiers and the common surname without corroborating evidence.",
                "temporal_assessment": "No candidate Army chronology is published pending review of Box 491.",
                "source_quality": "A_direct_official",
                "claim_confidence": "conflicting",
                "publication_status": "conflicting",
                "match_notes": "The conflict is reported without exposing either protected identifier or attaching another person's Army data.",
                "sources": [{"source_key": INDEX}, {"source_key": ARMY, "support_type": "contradicts"}],
            },
        ]
    )
    return values


def base_update(row: int) -> dict[str, object]:
    person_id, name, box = PEOPLE[row]
    detail = " The printed suffix Jr. after Evelyn D. Massie remains recoverable and is not silently removed." if row == 18 else ""
    return {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified page 299 source preserves {name}, Box {box}, rank or grade when printed, notes when present, and archive location.{detail} Staged official, exact-name, employment, occupation, obituary, institutional, newspaper, directory, and archival searches did not establish a defensible identity-and-affiliation bridge.",
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
        identity = ARMY_ASSOCIATIONS[row][5]
        by_row[row].update(
            identity_status=identity,
            identity_evidence=army_identity_assessment(row),
            personnel_category="enlisted_army_personnel",
            commissioned_officer=False,
            allied_or_foreign_personnel=False,
            nara_catalog_id="1263923",
            research_status="occupation_only_found",
            next_action=f"Review Box {PEOPLE[row][2]} to identify a named employer or institution and establish Army-to-OSS chronology. The protected Army link supplies only a broad historical occupation or student-status category.",
        )

    by_row[1].update(
        identity_status="high_confidence",
        identity_evidence="The rare exact name and middle initial, matching second-lieutenant rank, Army context, and dated 35th Infantry Division award record strongly identify Nicholas G. Maslikosa.",
        personnel_category="commissioned_army_officer",
        commissioned_officer=True,
        allied_or_foreign_personnel=False,
        next_action="Review Box 489 to identify Nicholas G. Maslikosa's civilian employer or military assignment immediately before OSS and establish the 35th Infantry Division-to-OSS sequence.",
        archival_review_priority="critical",
    )
    by_row[2].update(
        identity_status="high_confidence",
        identity_evidence="A wartime OSS Detachment 101 promotions report supplies the uncommon exact name, middle initial, and promotion to the technical-sergeant rank printed in the index.",
        personnel_category="enlisted_army_personnel",
        commissioned_officer=False,
        allied_or_foreign_personnel=False,
        next_action="Review Box 489 and Detachment 101 personnel records for Edward S. Maslowsky's pre-OSS civilian occupation and earlier Army unit; the promotion report supplies no predecessor affiliation.",
        archival_review_priority="critical",
    )
    by_row[6].update(
        identity_status="high_confidence",
        identity_evidence="Exact name and initial, NARA Box 490 entry, Harvard professorship, and Edward S. Mason's first-person account of his 1941 OSS recruitment align.",
        manual_review_required=False,
        research_status="verified_employer_found",
        next_action="Review Box 490 to interpret the indexed PD grade and document exact OSS appointment dates; existing first-person employer evidence remains verified and was not duplicated.",
        archival_review_priority="medium",
    )
    by_row[21].update(archival_review_priority="critical")
    by_row[28].update(
        identity_status="high_confidence",
        identity_evidence="The uncommon exact name appears in two OSS Greek Operational Group rosters. The later staff-sergeant rank is compatible with the printed private rank and is not used as a correction.",
        personnel_category="enlisted_army_personnel",
        commissioned_officer=False,
        allied_or_foreign_personnel=False,
        next_action="Review Box 490 and Greek Operational Group records for Steve J. Mastros's pre-OSS occupation, employer, and earlier Army unit; wartime rosters establish identity only.",
        archival_review_priority="critical",
    )
    by_row[31].update(
        identity_status="ambiguous",
        identity_evidence="A contemporary Thomas Masuda was a Seattle attorney, entered Camp Savage in 1943, and later practiced in Chicago, but the common name, rankless index row, and absence of a protected or direct OSS bridge make the match insufficient.",
        research_status="needs_identity_review",
        next_action="Review Box 490 for hometown, education, profession, or Japanese-language-service evidence before linking the indexed Thomas Masuda to the contemporary Seattle and Chicago attorney.",
        archival_review_priority="critical",
    )
    by_row[32].update(archival_review_priority="critical")
    by_row[33].update(
        name_variants=["Bronislaw J Matejczak"],
        replace_name_variants=False,
        archival_review_priority="critical",
    )
    by_row[35].update(
        identity_status="confirmed",
        identity_evidence="The exact uncommon name and middle initial, matching captain rank, official NPS Italian Operational Group role, oral-history attribution, and independent ISRAL chronology confirm Albert R. Materazzi.",
        name_variants=["Albert R. Materazzi", "Albert 'Al' Materazzi"],
        replace_name_variants=False,
        personnel_category="commissioned_army_officer",
        commissioned_officer=True,
        allied_or_foreign_personnel=False,
        research_status="verified_employer_found",
        next_action="Review Box 491 and Army Map Service records to establish the exact end date of civilian employment and the precise 1943 Corps of Engineers-to-OSS transfer.",
        archival_review_priority="medium",
    )
    by_row[36].update(
        name_variants=["Dimtrious Matheos"],
        replace_name_variants=False,
        personnel_category="enlisted_army_personnel",
        commissioned_officer=False,
        allied_or_foreign_personnel=False,
        archival_review_priority="critical",
    )
    by_row[39].update(
        name_variants=["Frederick G Matheson"],
        replace_name_variants=False,
        archival_review_priority="critical",
    )
    by_row[41].update(
        name_variants=["Elwood K Mathew"],
        replace_name_variants=False,
        personnel_category="enlisted_army_personnel",
        commissioned_officer=False,
        allied_or_foreign_personnel=False,
        archival_review_priority="critical",
    )
    by_row[42].update(
        identity_status="ambiguous",
        identity_evidence="The automated Army candidate was rejected because the protected identifiers conflict and its evidence supplied no defensible link to the indexed captain. No Army fields were transferred.",
        research_status="needs_identity_review",
        next_action="Review Box 491 and protected Army evidence for Eugene K. Mathews before accepting any candidate or transferring Army chronology, occupation, or name data.",
        archival_review_priority="critical",
    )

    result = [by_row[row] for row in PEOPLE]
    if len(result) != 46:
        raise RuntimeError(f"Expected 46 person updates, generated {len(result)}")
    return result


def outcome_note(row: int) -> str:
    notes = {
        1: "A specific wartime award record establishes a strong Army identity but not a pre-OSS employer or transfer sequence.",
        2: "A Detachment 101 promotion report establishes a strong wartime OSS identity but supplies no earlier employer or unit.",
        6: "Existing Truman Library first-person evidence for Edward S. Mason was re-reviewed and remains verified without duplicate claims.",
        19: "Hede or Hedwig Massing discovery leads were not linked to this index row without the personnel file; sensitive and later espionage narratives were not substituted for employment evidence.",
        20: "Paul Massing and Institute for Social Research leads were not published because the index-file relationship and OSS sequence remain unestablished.",
        28: "Two Greek Operational Group rosters establish a strong wartime identity but no pre-OSS affiliation.",
        31: "A contemporary attorney and Camp Savage lead remains a plausible namesake requiring Box 490; no profession was transferred.",
        35: "Official and institutional histories establish Materazzi's Army engineering pathway and a qualified last civilian employer at the Army Map Service.",
        42: "The Army candidate was rejected because protected identifiers conflict; no candidate fields were transferred.",
    }
    return notes.get(row, "Unbridged namesakes, snippets, commercial people-finder pages, unsourced genealogy, relatives, and postwar-only leads did not establish a reliable identity or pre-OSS affiliation.")


def research_attempts() -> list[dict[str, object]]:
    updates = {item["person_id"]: item for item in person_updates()}
    substantiated = set(ARMY_ASSOCIATIONS) | {1, 2, 6, 28, 35}
    values: list[dict[str, object]] = []
    for row, (person_id, name, box) in PEOPLE.items():
        if row in {31, 42}:
            outcome = "candidate_rejected"
        elif row in substantiated:
            outcome = "source_reviewed"
        else:
            outcome = "no_result"
        values.append(
            {
                "key": f"page299-row{row}-{slug(name)}-b1044",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index context; exact-name and meaningful initial, suffix, punctuation, spelling and OCR variants; OSS and permitted CIA or equivalent official-source context; rank, branch, nationality, assignment and protected-identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory and archival searches; indexed Box {box}",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_1044",
                "started_at": "2026-11-05T13:15:00-05:00",
                "completed_at": "2026-11-05T15:45:00-05:00",
                "outcome": outcome,
                "sources_reviewed": 10 if row in {1, 2, 6, 28, 35} else 7 if row in substantiated or row in {31, 42} else 6,
                "candidate_sources_rejected": 3 if row in substantiated else 5,
                "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, education without employment, sensitive but irrelevant personal narratives, and postwar-only leads were rejected. Army categories were not converted into named employers. Protected conflicts and spelling variants remain visible.",
                "research_notes": f"{outcome_note(row)} The official index, exact-name OSS searches, permitted official-source context, Army and NARA materials, employment and occupation searches, and institutional, newspaper, obituary, directory, award, military-history, and archival sources were reviewed as applicable. Page 299 and every used Army code were visually checked. No authenticated NARA Catalog API request was made.",
                "next_action": str(updates[person_id]["next_action"]),
                "attempt_number": 1,
                "research_agent_version": "before-oss-b1044-v1",
            }
        )
    if len(values) != 46:
        raise RuntimeError(f"Expected 46 research attempts, generated {len(values)}")
    return values


def main() -> None:
    bundle = {
        "bundle_version": "batch-1044-v1",
        "reviewer": "Before OSS Batch 1044 evidence review",
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
