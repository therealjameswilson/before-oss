#!/usr/bin/env python3
"""Generate the reviewed Batch 1003 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page493-watterson-to-weber-"
    "review_batch-1003_2026-11-03.json"
)

INDEX = "nara-index-b1003"
ARMY = "army-bulk-b1003"
TECH = "army-tech-b1003"
CODES = "army-codes-b1003"
WAUCHOPE = "wauchope-obituary-b1003"
FSJ = "foreign-service-journal-weatherby-b1003"
KKG = "kappa-key-frances-webb-b1003"
ERWIN = "nolte-shear-yelvington-erwin-watts-b1003"
CLINTON = "nara-jfk-clinton-webb-b1003"
CIA_WEBER = "cia-frank-weber-b1003"

ORG_TULANE = "tulane-university-b1003"
ORG_STATE = "state-department-b1003"


PEOPLE = {
    1: ("e1b78199-e6d3-533b-8552-2255721a5953", "Arthur W Watterson"),
    2: ("f3555281-6063-59bf-a7d3-c8d71fa1603d", "Robert Silas Wattles"),
    3: ("cbbfe8eb-44c8-5e2f-b7b3-c193a4d876e7", "Arthur P Watts"),
    4: ("01cbb21a-3e2b-51be-a075-ff2657d3000b", "Dallas H Watts"),
    5: ("573e5b0b-4dc2-553f-9011-3df911f332d0", "Erwin H Watts"),
    6: ("8d384416-1380-5563-b7ae-344fec95e4d5", "Eve Watts"),
    7: ("092eaffe-127e-593c-a910-b1ea9131f365", "James P Watts Jr."),
    8: ("143b8109-28ac-5e56-bcf3-2bba6d0440cc", "Richard Watts Jr."),
    9: ("c02e9cd9-56fe-588c-a152-a1df5e4dbf7a", "Robert T Watts"),
    10: ("eb3bc431-05f0-56b9-8bb4-4a90a383937a", "Shirley L Watts"),
    11: ("8ee1dda8-b9c6-5b2f-a0a8-52cdcea29e13", "Robert Wauchope"),
    12: ("6ca54963-6dcb-587a-8b68-e9e0cfa85548", "Frederick J Waugh Jr."),
    13: ("d4111205-bd60-505c-a3fe-2dee3a692fce", "Jeanne Wax"),
    14: ("43dc6fea-d61b-53c3-ac8a-adbea7cb479e", "Edrie C Way"),
    15: ("dbbb76cf-ebfc-5b76-ac55-42d83baf8e16", "Helen P Weary"),
    16: ("7ece89f4-dadb-5891-acb7-d9d20b5b5291", "Meredith Weatherby"),
    17: ("5473d13c-e63d-52f4-8942-6e8a249c1842", "Paul Weatherill"),
    18: ("605f5941-8b11-55ab-8af7-ef6ee46da3c1", "Gerald Weathers"),
    19: ("6c363f8a-ce24-527e-843c-44e417d00d81", "Anthony J Weaver Jr."),
    20: ("eafde514-22ea-5b57-a140-2f4aa0892cb6", "Charlotte E Weaver"),
    21: ("1b72519d-6f46-54c5-bd6a-e134d752277a", "Charlton A Weaver"),
    22: ("7205097b-3f94-513e-a4d9-2ac9f9d57707", "Edward L Weaver"),
    23: ("2a7d64b6-a329-530c-a595-78be22aff0a0", "Helen K Weaver"),
    24: ("0c9af132-45fd-5c87-b6a0-a73b19d8b014", "Jim R Weaver"),
    25: ("aecbaf59-4b19-5bb6-8d94-5b5ddc978f0b", "John F Weaver"),
    26: ("94053f47-2df3-5250-b5d7-8fcfeba9208b", "John O Weaver"),
    27: ("bacca2df-f44b-5179-92af-48e4a0180c39", "John C Weaver"),
    28: ("00ee89a6-edf2-59fd-89d3-90b6eb612292", "Leon H Weaver"),
    29: ("277dbab4-641c-584c-946f-772732a329ef", "Margaret L Weaver"),
    30: ("f1441a91-0830-510c-9df8-5ce7a2e14da0", "Robert G Weaver"),
    31: ("299ebc54-2409-518e-9dd5-1c88ac3385a8", "William Weaver"),
    32: ("496804e3-6a41-539e-a265-dd50394f28c6", "* Weaver and C"),
    33: ("fd6448d5-ff98-510f-82b2-2547470b8a77", "Clinton Webb"),
    34: ("1199e6b9-f016-516e-be71-fb979b8b3d82", "Dorothy J Webb"),
    35: ("b70198e8-4541-59be-bccb-89ad23ba7be0", "Frances Webb"),
    36: ("d4b9090a-7ac4-5640-8035-4798f553d40a", "Guy E Webb"),
    37: ("4db5be91-fcef-5ca1-88cd-a3784c3bef0b", "James H Webb Jr."),
    38: ("071a99c2-27f8-53de-97eb-5d1a9ff9ab7f", "John A Webb"),
    39: ("fbd6811e-0c76-551f-8050-5112f4815e4c", "Kenneth W Webb"),
    40: ("317c293c-265a-5818-b150-939d35022f8c", "Thomas B Webb Jr."),
    41: ("2ee5f8b5-7394-5254-9798-896d7b600678", "Wesley D Webb"),
    42: ("1d96e15f-6b50-51ec-8c29-6c7a0acc31fe", "M. V Webbert"),
    43: ("10f7202d-9ee4-5a88-bf10-988b60dd88ec", "Dean Weber"),
    44: ("0ec2d8ef-d908-5564-b4be-53bd47fa07b7", "Frank R Weber"),
    45: ("c64303f5-5b04-5d67-b46f-8eefa17e9908", "Harry Weber"),
    46: ("4a8ea418-6dd5-5412-9eeb-8ec49190142b", "Jacob H Weber"),
}

BOX_BY_ROW = {
    **{row: 820 for row in range(1, 24)},
    24: 821,
    25: 820,
    26: 820,
    27: 820,
    **{row: 821 for row in range(28, 47)},
    32: 820,
}

ARMY_MATCHES = {
    1: {
        "date": "1943-08-14", "code": "031",
        "occupation": "secondary-school teacher or principal",
        "label": "Teachers (secondary school) and principals",
        "locator": "PDF physical page 171; historical category 0-31",
        "publish_occupation": True,
    },
    4: {
        "date": "1943-05-03", "code": "992", "occupation": "student",
        "label": "Students",
        "locator": "PDF physical page 304; amended historical category 9-92",
        "publish_occupation": True,
    },
    7: {
        "date": "1940-09-16", "code": "862",
        "occupation": "unskilled leather-products manufacturing worker",
        "label": "Occupations in manufacture of leather and leather products",
        "locator": "PDF physical page 174; historical category 8-62",
        "publish_occupation": True,
    },
    10: {
        "date": "1942-12-18", "code": "117", "occupation": "file clerk",
        "label": "File clerks",
        "locator": "PDF physical page 171; historical category 1-17",
        "publish_occupation": True,
    },
    18: {
        "date": "1940-12-23", "code": "002", "occupation": "actor",
        "label": "Actors and actresses",
        "locator": "PDF physical page 170; historical category 0-02",
        "publish_occupation": True,
    },
    21: {
        "date": "1945-11-03", "code": "499",
        "occupation": "electrical-machinery manufacturing worker",
        "label": "Electrical machinery and accessories manufacturing occupations, not elsewhere classified",
        "locator": "PDF physical pages 174 and 176; historical category 4-99",
        "publish_occupation": False,
    },
    30: {
        "date": "1942-06-16", "code": "002", "occupation": "actor",
        "label": "Actors and actresses",
        "locator": "PDF physical page 170; historical category 0-02",
        "publish_occupation": True,
    },
    36: {
        "date": "1943-04-29", "code": "992", "occupation": "student",
        "label": "Students",
        "locator": "PDF physical page 304; amended historical category 9-92",
        "publish_occupation": True,
    },
    39: {
        "date": "1942-09-15", "code": "446", "occupation": "lithographer",
        "label": "Lithographers",
        "locator": "PDF physical page 174; historical category 4-46",
        "publish_occupation": True,
    },
    44: {
        "date": "1941-04-23", "code": "050",
        "occupation": "laboratory technician or assistant",
        "label": "Laboratory technicians and assistants",
        "locator": "PDF physical page 171; historical category 0-50",
        "publish_occupation": True,
    },
    45: {
        "date": "1943-11-03", "code": "022", "occupation": "lawyer or judge",
        "label": "Lawyers and judges",
        "locator": "PDF physical page 171; historical category 0-22",
        "publish_occupation": True,
    },
}

PRINTED_CATEGORY = {
    11: ("commissioned_naval_officer", True),
    12: ("commissioned_army_officer", True),
    26: ("commissioned_army_officer", True),
    27: ("enlisted_naval_personnel", False),
    36: ("enlisted_army_personnel", False),
    37: ("commissioned_army_officer", True),
    44: ("enlisted_army_personnel", False),
}

LEADS = {
    5: "A scholarly article documents an OSS officer named Erwin H. Watts in wartime Africa, but it supplies no indexed identifier or personnel-file linkage and no pre-OSS affiliation.",
    33: "Official OSS-London records name a Clinton Webb, including Clinton W. Webb, but the common name and absence of the indexed identifier leave the page-493 identity unconfirmed.",
    35: "A Kappa Kappa Gamma institutional magazine states that a Frances Webb served with OSS in England, but the common name and absence of an indexed identifier leave the page-493 identity unconfirmed.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def box_for(row: int) -> int:
    return BOX_BY_ROW[row]


def unresolved_reason(row: int) -> str:
    name = PEOPLE[row][1]
    base = (
        "Exact-name and meaningful-variant searches across the NARA index context, "
        "CIA Reading Room, Library of Congress, OSS, employment, occupation, obituary, "
        "institutional, newspaper, directory, and archival sources produced no reliable "
        "identity and pre-OSS affiliation bridge; unbridged namesakes were rejected."
    )
    if row == 8:
        return (
            "Published theater-history leads for a Richard Watts Jr. did not supply an indexed "
            "identifier, Box 820, rank, or direct personnel-file bridge. " + base
        )
    if row == 17:
        return (
            "A CIA search lead for a T/Sgt. Paul Weatherill could not be inspected because the "
            "Reading Room file returned a maintenance page; a snippet was not used as final evidence. "
            + base
        )
    if row == 24:
        return "The page itself flags a possible move in the notes column. " + base
    if row == 32:
        return (
            "The unusual printed form '* Weaver and C' and note 'review' are preserved exactly; "
            "no person or company name is inferred from the fragment. " + base
        )
    if row in PRINTED_CATEGORY:
        return f"The printed rank for {name} establishes personnel category only. " + base
    return base


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 820-821",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 493, rows 1-46",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 46 printed rows remain separate. Page 493 was checked against layout-preserving text and an original-detail render. Full protected identifiers remain private.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; eleven accepted protected-identifier comparisons; identifiers and record ordinals withheld",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "Eleven exact-name identity bridges were accepted after private review. The November 3, 1945 entry is retained as identity-only evidence because it postdates OSS dissolution. No Army record is treated as a named employer or direct OSS-transfer record.",
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
            "locator": "PDF physical pages 170-176 and 304; categories 0-02, 0-22, 0-31, 0-50, 1-17, 4-46, 4-99, 8-62, and 9-92",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical labels identify broad occupations or student status, not named employers, institutions, workplaces, or exact OSS-transfer dates.",
        },
        {
            "key": WAUCHOPE,
            "stable_url": "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/B46488AE02F872074BF0B6A1B6CA5958/S0002731600079476a.pdf/obituary_robert_wauchope_19091979.pdf",
            "archival_identifier": "DOI 10.1017/S0002731600079476",
            "title": "Robert Wauchope, 1909-1979",
            "author_creator": "E. Wyllys Andrews V and Margaret A. L. Harrison",
            "repository_publisher": "American Antiquity; Cambridge University Press",
            "publication_record_date": "1981",
            "locator": "American Antiquity 46(1), pages 113-127; printed page 118",
            "access_date": "2026-11-03",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "American Antiquity obituaries",
            "rights_notes": "The chronology explicitly states that Wauchope took leave from Tulane in mid-1943 for a USNR commission and OSS assignment.",
        },
        {
            "key": FSJ,
            "stable_url": "https://afsa.org/sites/default/files/fsj-1946-08-august_0.pdf",
            "title": "The Foreign Service Journal, August 1946",
            "author_creator": "American Foreign Service Association; News from the Department by Jane Wilson",
            "repository_publisher": "American Foreign Service Association",
            "publication_record_date": "1946-08",
            "locator": "PDF physical page 25; printed page 23",
            "access_date": "2026-11-03",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "The Foreign Service Journal",
            "rights_notes": "The item prints the surname as Weathherby in its heading and Weatherby in the prose. It documents resignation from the Foreign Service in early 1943 to enter the Army, not an immediate transfer to OSS.",
        },
        {
            "key": KKG,
            "stable_url": "https://wiki.kkg.org/images/a/ab/THE_KEY_VOL_70_NO_3_OCT_1953.pdf",
            "title": "The Key, volume 70, number 3",
            "author_creator": "Kappa Kappa Gamma; article by Frances Webb Leishman",
            "repository_publisher": "Kappa Kappa Gamma",
            "publication_record_date": "1953-10",
            "locator": "PDF physical page 9; printed page 183; editor's note",
            "access_date": "2026-11-03",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "The Key",
            "rights_notes": "The editor's note documents an OSS Frances Webb in England but supplies no index identifier or Box 821 linkage.",
        },
        {
            "key": ERWIN,
            "stable_url": "https://pure-oai.bham.ac.uk/ws/files/40535063/Nolte_Shear_and_Yelvington.From_Ethnographic_Knowledge_to_Anthropological_Intelligence.Revised_version_resubmitted_12_April_2017_.pdf",
            "title": "From ethnographic knowledge to anthropological intelligence: An anthropologist in the Office of Strategic Services in Second World War Africa",
            "author_creator": "Insa Nolte, Keith Shear, and Kevin A. Yelvington",
            "repository_publisher": "University of Birmingham Research Portal",
            "publication_record_date": "2018",
            "locator": "Discussion of Erwin H. Watts's COI and OSS Special Operations service in Lagos",
            "access_date": "2026-11-03",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "History and Anthropology",
            "rights_notes": "The article supplies a strong OSS namesake lead but no protected identifier, Box 820 link, or pre-OSS affiliation.",
        },
        {
            "key": CLINTON,
            "stable_url": "https://www.archives.gov/files/research/jfk/releases/104-10165-10143.pdf",
            "archival_identifier": "JFK release 104-10165-10143",
            "title": "London Correspondence #1 (CINEM, L.), 1943-1945",
            "author_creator": "Office of Strategic Services",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1943-1945; released JFK collection copy",
            "locator": "OSS Main UK Base records naming Lt. Clinton Webb and Clinton W. Webb in 1945",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "John F. Kennedy Assassination Records Collection",
            "rights_notes": "Direct OSS evidence for a namesake; no protected identifier or Box 821 link establishes that he is the indexed Clinton Webb.",
        },
        {
            "key": CIA_WEBER,
            "source_id": "edf80daf-da47-5703-9d87-41df6d6fff5b",
            "stable_url": "https://www.cia.gov/readingroom/docs/BISHOP%2C%20ROBERT_0060.pdf",
            "archival_identifier": "CIA FOIA document BISHOP, ROBERT_0060",
            "title": "Assignment of Qualified Personnel to OSS-ME Parachute Unit",
            "author_creator": "Office of Strategic Services, U.S. Army Forces in the Middle East",
            "repository_publisher": "Central Intelligence Agency Freedom of Information Act Electronic Reading Room",
            "publication_record_date": "1944-07-01",
            "locator": "PDF page 1; official order includes Cpl. Frank R. Weber with protected identifier withheld",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "CIA FOIA OSS Collection",
            "document_number": "BISHOP, ROBERT_0060",
            "rights_notes": "The public claim omits the full protected identifier. The document establishes OSS identity and assignment, not pre-OSS employment.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": ORG_TULANE,
            "canonical_name": "Tulane University",
            "historical_name": "Tulane University of Louisiana",
            "aliases": ["Tulane"],
            "organization_type": "private research university",
            "sector": "academia_and_research",
            "city": "New Orleans",
            "state_or_region": "Louisiana",
            "country": "United States",
            "active_dates": "1884-present",
            "normalization_notes": "The historical employer name is preserved separately; the Middle American Research Institute was Wauchope's university unit.",
        },
        {
            "key": ORG_STATE,
            "organization_id": "4d2fbb5f-218d-5445-b7b3-4c2fd22f0286",
            "canonical_name": "United States Department of State",
            "historical_name": "Department of State",
            "aliases": ["U.S. Department of State", "Foreign Service of the United States"],
            "organization_type": "federal executive department",
            "sector": "federal_government",
            "city": "Washington",
            "state_or_region": "District of Columbia",
            "country": "United States",
            "normalization_notes": "Existing canonical department reused. Foreign Service work is modeled as a government assignment, not private employment.",
        },
    ]


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, item in ARMY_MATCHES.items():
        if not item["publish_occupation"]:
            continue
        values.append({
            "key": f"{slug(PEOPLE[row][1])}-army-occupation-b1003",
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
    values.extend([
        {
            "key": "robert-wauchope-tulane-b1003",
            "person_id": PEOPLE[11][0],
            "organization_key": ORG_TULANE,
            "organization_name_as_found": "Tulane University",
            "role_title": "Director, Middle American Research Institute, and associate professor of anthropology",
            "occupation": "anthropologist and university professor",
            "relationship_type": "employment",
            "start_date": "1942-07",
            "end_date": "1943",
            "date_precision": "The source dates the Tulane appointment to July 1942 and the leave for a USNR commission and OSS assignment to mid-1943.",
            "city": "New Orleans",
            "state_or_region": "Louisiana",
            "country": "United States",
            "immediate_pre_oss": True,
            "last_civilian_pre_service": True,
            "pre_oss_temporal_basis": "explicit_immediate",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "published",
            "research_notes": "The scholarly obituary explicitly states that Wauchope left Tulane on leave to accept his USNR commission and was assigned to OSS.",
        },
        {
            "key": "meredith-weatherby-state-b1003",
            "person_id": PEOPLE[16][0],
            "organization_key": ORG_STATE,
            "organization_name_as_found": "Foreign Service",
            "role_title": "Foreign Service officer",
            "occupation": "diplomat",
            "relationship_type": "government_assignment",
            "end_date": "1943",
            "date_precision": "The institutional journal says Weatherby resigned from the Foreign Service in early 1943 to enter the Army; it does not date an OSS transition.",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": True,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "published",
            "research_notes": "This is the last documented civilian government affiliation before Army service, not an immediate pre-OSS affiliation.",
        },
    ])
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
        links = [
            {"source_key": INDEX, "locator_override": f"PDF page 493 row {row}; protected identifier withheld"},
            {"source_key": ARMY, "locator_override": "Accepted reviewed identity bridge; protected identifier withheld"},
        ]
        if row == 44:
            links.append({
                "source_key": CIA_WEBER,
                "locator_override": "Official July 1, 1944 OSS assignment order; protected identifier withheld",
                "excerpt_override": "Cpl Frank R Weber",
            })
        values.append(make_claim(
            key=f"identity-{slug(name)}-b1003",
            row=row,
            claim_type="identity",
            text=f"Indexed {name} is confirmed as the reviewed official Army entry record.",
            paraphrase="The exact indexed and Army names agree, and a nonshared protected identifier connects the records.",
            identity="Confirmed by exact name and a nonshared protected-identifier agreement; the identifier and record ordinal remain private.",
            temporal=f"The Army record dates entry to {item['date']} and carries historical civilian code {item['code']}.",
            quality="A_direct_official",
            confidence="confirmed",
            publication="published",
            notes=(
                "Identity only. The Army entry postdates OSS dissolution, so its civilian code is not published as pre-OSS evidence."
                if not item["publish_occupation"]
                else "Identity only; no named employer, workplace, school, or exact OSS-transfer date is inferred."
            ),
            source_links=links,
        ))
        if not item["publish_occupation"]:
            continue
        values.append(make_claim(
            key=f"occupation-{slug(name)}-b1003",
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
            affiliation_key=f"{slug(name)}-army-occupation-b1003",
        ))

    values.extend([
        make_claim(
            key="identity-robert-wauchope-b1003",
            row=11,
            claim_type="identity",
            text="The indexed Lt. Robert Wauchope, marked USNR, is a high-confidence match to the anthropologist assigned to OSS.",
            paraphrase="The distinctive exact name, naval rank and reserve branch agree, and the scholarly chronology explicitly states his OSS assignment.",
            identity="High confidence from a distinctive exact name plus matching lieutenant junior grade, U.S. Naval Reserve, and direct OSS chronology.",
            temporal="The source dates his move to Tulane in July 1942 and his USNR commission and OSS assignment to mid-1943.",
            quality="C_reputable_contemporary_or_scholarly",
            confidence="high",
            publication="published",
            notes="The indexed personnel file remains useful, but the identity and employer chronology are well supported.",
            source_links=[
                {"source_key": INDEX, "locator_override": "PDF page 493 row 11; Lt.; USNR; Box 820"},
                {"source_key": WAUCHOPE, "locator_override": "Printed page 118", "excerpt_override": "He was assigned to the Office of Strategic Services"},
            ],
        ),
        make_claim(
            key="immediate-robert-wauchope-tulane-b1003",
            row=11,
            claim_type="immediate_pre_oss_affiliation",
            text="Robert Wauchope's immediate pre-OSS civilian affiliation was Tulane University, where he directed the Middle American Research Institute and was associate professor of anthropology.",
            paraphrase="The obituary states that he joined Tulane in July 1942 and took leave in mid-1943 for a USNR commission and OSS assignment.",
            identity="High-confidence match from distinctive name, matching naval status, and explicit OSS assignment.",
            temporal="Explicit immediate sequence: leave from Tulane to accept the commission followed by OSS assignment.",
            quality="C_reputable_contemporary_or_scholarly",
            confidence="high",
            publication="published",
            notes="The same affiliation is also the last documented civilian employer before wartime service.",
            source_links=[
                {"source_key": WAUCHOPE, "locator_override": "Printed page 118", "excerpt_override": "In mid-1943 Wauchope was granted a leave-of-absence from Tulane to accept a commission"},
            ],
            affiliation_key="robert-wauchope-tulane-b1003",
        ),
        make_claim(
            key="last-civilian-robert-wauchope-tulane-b1003",
            row=11,
            claim_type="last_civilian_pre_service",
            text="Tulane University was Robert Wauchope's last documented civilian employer before his USNR commission and OSS assignment.",
            paraphrase="The source gives an unbroken sequence from the July 1942 Tulane appointment to his mid-1943 leave for naval and OSS service.",
            identity="High-confidence match from distinctive name, matching naval status, and explicit OSS assignment.",
            temporal="Explicitly the last civilian employment before military service.",
            quality="C_reputable_contemporary_or_scholarly",
            confidence="high",
            publication="published",
            notes="This claim is not inferred from education; the source documents employment and the transition.",
            source_links=[
                {"source_key": WAUCHOPE, "locator_override": "Printed page 118", "excerpt_override": "In July 1942, when Wauchope moved to Tulane University as director"},
            ],
            affiliation_key="robert-wauchope-tulane-b1003",
        ),
        make_claim(
            key="identity-meredith-weatherby-b1003",
            row=16,
            claim_type="identity",
            text="The indexed Meredith Weatherby is a high-confidence match to the Foreign Service officer who resigned in early 1943 to enter the Army.",
            paraphrase="The distinctive exact personal name and wartime Army transition align; the journal contains a heading typographical variant, Weathherby.",
            identity="High confidence from a distinctive exact name, the same wartime sequence, and an authoritative Foreign Service institutional source.",
            temporal="The source dates resignation from the Foreign Service to early 1943 and identifies Army service as the next step.",
            quality="B_authoritative_institutional",
            confidence="high",
            publication="published",
            notes="The source does not state the Army-to-OSS chronology, so no immediate pre-OSS claim is made.",
            source_links=[
                {"source_key": INDEX, "locator_override": "PDF page 493 row 16; Box 820"},
                {"source_key": FSJ, "locator_override": "Printed page 23", "excerpt_override": "resigned in early 1943 in order to enter the Army"},
            ],
        ),
        make_claim(
            key="last-civilian-meredith-weatherby-state-b1003",
            row=16,
            claim_type="last_civilian_pre_service",
            text="Meredith Weatherby's last documented civilian government affiliation before Army service was the Foreign Service of the United States.",
            paraphrase="The Foreign Service Journal states that Weatherby resigned from the Foreign Service in early 1943 in order to enter the Army.",
            identity="High confidence from the distinctive exact name and authoritative institutional chronology.",
            temporal="Strongly date-bounded as the affiliation immediately before Army entry; the later Army-to-OSS sequence remains unresolved.",
            quality="B_authoritative_institutional",
            confidence="high",
            publication="published",
            notes="Modeled as a government assignment, not a private employer and not an immediate pre-OSS affiliation.",
            source_links=[
                {"source_key": FSJ, "locator_override": "Printed page 23", "excerpt_override": "resigned in early 1943 in order to enter the Army"},
            ],
            affiliation_key="meredith-weatherby-state-b1003",
        ),
        make_claim(
            key="lead-erwin-h-watts-b1003",
            row=5,
            claim_type="identity",
            text="Erwin H. Watts is a plausible OSS namesake lead, but the indexed identity is not confirmed.",
            paraphrase="A scholarly article documents an OSS officer with the exact uncommon name in wartime Africa but supplies no index identifier or Box 820 linkage.",
            identity="Probable lead only; the exact name is distinctive, but no protected identifier or personnel-file link has been found.",
            temporal="The source documents OSS service, not a pre-OSS employer or transfer chronology.",
            quality="C_reputable_contemporary_or_scholarly",
            confidence="low",
            publication="withheld_low_confidence",
            notes="Retained for archival follow-up and excluded from public facts and analytics.",
            source_links=[{"source_key": ERWIN, "locator_override": "Discussion of Erwin H. Watts in Lagos"}],
        ),
        make_claim(
            key="lead-clinton-webb-b1003",
            row=33,
            claim_type="identity",
            text="Clinton Webb is a plausible OSS-London namesake lead, but the indexed identity is not confirmed.",
            paraphrase="Official OSS records name Lt. Clinton Webb and Clinton W. Webb in London, but the common name lacks an indexed identifier or Box 821 linkage.",
            identity="Probable lead only; name and OSS context agree, but the common name requires additional corroboration.",
            temporal="The source documents OSS service in 1945 and supplies no pre-OSS affiliation.",
            quality="A_direct_official",
            confidence="low",
            publication="withheld_low_confidence",
            notes="Retained for archival follow-up and excluded from public facts and analytics.",
            source_links=[{"source_key": CLINTON, "locator_override": "OSS Main UK Base records, January-March 1945"}],
        ),
        make_claim(
            key="lead-frances-webb-b1003",
            row=35,
            claim_type="identity",
            text="Frances Webb Leishman is a plausible OSS namesake lead, but the indexed Frances Webb identity is not confirmed.",
            paraphrase="An institutional magazine states that Frances Webb went to England with OSS, but the common name lacks an index identifier or Box 821 linkage.",
            identity="Probable lead only; name and OSS context agree, but the common name requires additional corroboration.",
            temporal="The source documents OSS service in England and supplies no pre-OSS affiliation.",
            quality="B_authoritative_institutional",
            confidence="low",
            publication="withheld_low_confidence",
            notes="Retained for archival follow-up and excluded from public facts and analytics.",
            source_links=[
                {"source_key": KKG, "locator_override": "Printed page 183; editor's note", "excerpt_override": "Frances Webb went to England during World War II with the office of Strategic Services"},
            ],
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
    if row in PRINTED_CATEGORY:
        value["personnel_category"], value["commissioned_officer"] = PRINTED_CATEGORY[row]
    value.update(overrides)
    return value


def person_updates() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    special_rows = set(ARMY_MATCHES) | {11, 16} | set(LEADS)
    for row in sorted(set(PEOPLE) - special_rows):
        reason = unresolved_reason(row)
        values.append(base_update(
            row,
            identity_status="unresolved",
            identity_evidence=f"The visually verified page 493 row preserves {PEOPLE[row][1]}, its printed rank or blank rank cell, notes, and archival context. {reason}",
            research_status="requires_archival_review",
            next_action=f"Review the indexed Box {box_for(row)} personnel file for corroborating identifiers, the immediate pre-OSS affiliation, and the last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}",
        ))
    for row, item in ARMY_MATCHES.items():
        if item["publish_occupation"]:
            status = "occupation_only_found"
            action = f"Review the indexed Box {box_for(row)} personnel file to identify any named employer or school behind the broad {item['occupation']} category and establish the Army-to-OSS chronology."
        else:
            status = "requires_archival_review"
            action = f"Review the indexed Box {box_for(row)} personnel file because the Army entry postdates OSS dissolution; establish an earlier occupation, immediate affiliation, and OSS chronology from contemporaneous evidence."
        values.append(base_update(
            row,
            identity_status="confirmed",
            identity_evidence="The exact indexed name and a nonshared protected identifier connect the row to the reviewed official Army record.",
            personnel_category="enlisted_army_personnel",
            commissioned_officer=False,
            allied_or_foreign_personnel=False,
            research_status=status,
            next_action=action,
            nara_catalog_id="1263923",
        ))
    values.extend([
        base_update(
            11,
            identity_status="high_confidence",
            identity_evidence="The distinctive exact name, lieutenant junior grade, U.S. Naval Reserve notation, and scholarly OSS chronology agree.",
            personnel_category="commissioned_naval_officer",
            commissioned_officer=True,
            research_status="verified_employer_found",
            archival_review_priority="medium",
            next_action="Review the indexed Box 820 personnel file to corroborate the already well-supported Tulane-to-USNR-to-OSS chronology and capture any additional pre-OSS roles.",
        ),
        base_update(
            16,
            identity_status="high_confidence",
            identity_evidence="The distinctive exact personal name and early-1943 Foreign Service-to-Army chronology align in an authoritative institutional source; the article heading contains the typographical form Weathherby.",
            name_variants=["Meredith Weathherby"],
            research_status="verified_employer_found",
            archival_review_priority="medium",
            next_action="Review the indexed Box 820 personnel file to establish Meredith Weatherby's Army-to-OSS sequence and determine whether another immediate affiliation intervened.",
        ),
        base_update(
            5,
            identity_status="probable",
            identity_evidence=LEADS[5],
            research_status="requires_archival_review",
            next_action="Review the indexed Box 820 personnel file for a protected identifier, assignment evidence, and any pre-OSS employer before accepting the scholarly Erwin H. Watts OSS namesake.",
        ),
        base_update(
            33,
            identity_status="probable",
            identity_evidence=LEADS[33],
            research_status="requires_archival_review",
            next_action="Review the indexed Box 821 personnel file for a middle initial, protected identifier, or London assignment evidence before accepting the official OSS-London Clinton Webb namesake.",
        ),
        base_update(
            35,
            identity_status="probable",
            identity_evidence=LEADS[35],
            research_status="requires_archival_review",
            next_action="Review the indexed Box 821 personnel file for identifiers, English assignment evidence, or the later Leishman surname before accepting the Frances Webb namesake.",
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
            if item["publish_occupation"]:
                note = f"A reviewed protected-identifier Army bridge supports identity and a qualified {item['occupation']} category at Army entry; no named employer, workplace, school, or OSS-transfer date is supplied."
            else:
                note = "A reviewed protected-identifier Army bridge confirms identity, but the November 3, 1945 entry postdates OSS dissolution and is not published as pre-OSS occupation evidence."
        elif row == 11:
            outcome, reviewed, rejected = "source_reviewed", 10, 5
            note = "A scholarly obituary provides a high-confidence identity bridge and explicit Tulane-to-USNR-to-OSS chronology, supporting both immediate affiliation and last civilian employer claims."
        elif row == 16:
            outcome, reviewed, rejected = "source_reviewed", 9, 5
            note = "An authoritative Foreign Service Journal item supports a high-confidence identity and the Foreign Service as the last documented civilian government affiliation before Army service; the later OSS sequence remains unresolved."
        elif row in LEADS:
            outcome, reviewed, rejected = "candidate_found", 8, 6
            note = LEADS[row] + " The candidate remains withheld from public facts pending personnel-file corroboration."
        else:
            outcome, reviewed, rejected = "candidate_rejected", 7, 6
            note = unresolved_reason(row)
        attempts.append({
            "key": f"page493-row{row}-{slug(name)}-b1003",
            "person_id": person_id,
            "source_adapter": "manual_staged_protocol",
            "query_text": f"{name}; NARA OSS index context; CIA Reading Room, National Archives, and Library of Congress exact-name domain checks; exact-name and meaningful spelling, initial, suffix, punctuation, and OCR variants; OSS, rank, branch, assignment, and identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory, and archival searches; indexed Box {box_for(row)}; protected identifiers used only in private official-record comparison",
            "query_variant_type": "staged_identity_employment_archival_protocol_batch_1003",
            "started_at": "2026-11-03T20:22:00Z",
            "completed_at": "2026-11-03T20:32:00Z",
            "outcome": outcome,
            "sources_reviewed": reviewed,
            "candidate_sources_rejected": rejected,
            "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, postwar-only leads, and sources without an OSS, protected-identifier, rank, unit, or personnel-file bridge were rejected. Historical Army categories were not converted into named employers, workplaces, or schools. A famous theater critic was not assigned to Richard Watts Jr. on name alone.",
            "research_notes": f"{note} Exact-name official-domain, OSS, employer, occupation, obituary, biography, institutional, newspaper, directory, and archival searches were checked as applicable. The NARA index page was text-extracted, rendered, and visually checked. Official Army bulk data, technical documentation, and code documentation were inspected locally. The CIA Special Funds Branch file returned a maintenance page, so the Paul Weatherill search snippet was not used as evidence. No authenticated NARA Catalog API call was made.",
            "next_action": f"Review the indexed Box {box_for(row)} personnel file for corroborating identifiers, the immediate pre-OSS affiliation, and the last civilian employer before wartime service.",
            "attempt_number": 1,
            "research_agent_version": "before-oss-b1003-v1",
        })
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-1003-v1",
        "reviewer": "Before OSS Batch 1003 evidence review",
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
