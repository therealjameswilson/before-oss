#!/usr/bin/env python3
"""Generate the reviewed Batch 1025 evidence bundle for PDF page 515."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page515-mundy-wright-to-hans-wyner-review_"
    "batch-1025_2026-11-04.json"
)

INDEX = "nara-index-b1025"
ARMY = "army-bulk-b1025"
TECH = "army-tech-b1025"
CODES = "army-codes-b1025"
TUFTS_WRISTON = "tufts-wriston-timeline-b1025"
COLUMBIA_WUORINEN = "columbia-annual-report-1944-b1025"
CTPOST_WURTMANN = "ctpost-wurtmann-obituary-b1025"
STARTRIB_WYLIE = "startrib-betty-wylie-obituary-b1025"
USMC_WYLLY = "usmc-marines-oss-b1025"
CEN_WYNBERG = "cen-hans-wynberg-obituary-b1025"
RUG_WYNBERG = "rug-hans-wijnberg-b1025"

ORG_US_ARMY = "us-army-existing-b1025"
ORG_STATE = "state-department-existing-b1025"
ORG_COLUMBIA = "columbia-existing-b1025"
ORG_US_NAVY = "us-navy-existing-b1025"
ORG_USMC = "usmc-existing-b1025"
ORG_GENERAL_MILLS = "general-mills-existing-b1025"
ORG_PFIZER = "charles-pfizer-b1025"

PEOPLE = {
    1: ("f6ca38c7-939c-594b-bbba-096cef3844f6", "Mundy P Wright", "854"),
    2: ("498b354f-cff2-5199-88d7-2fe4ab11389a", "Penelope Wright", "854"),
    3: ("5c341a43-ac3e-5e33-8871-eb14467ea055", "Phyllis M Wright", "854"),
    4: ("464c71c4-d5bf-54c3-96ae-cf9f07a050a4", "Rexford E Wright", "854"),
    5: ("a0e81896-7bc3-511f-af63-1574ce2df2a7", "Robert B Wright", "854"),
    6: ("266a1510-87a8-5103-bdc8-52ded6feeeb8", "Robert C Wright", "854"),
    7: ("fcf1b637-9c4f-5931-9042-ff01317c31fb", "Robert G Wright", "854"),
    8: ("590d5f15-a9ee-5e9c-885e-18139ccffb3d", "Robert G Wright", "854"),
    9: ("c58f8056-0d02-5660-98c0-bdce70fe4317", "Rosalind Wright", "855"),
    10: ("9ee4e652-09cc-56a2-8628-24565ab0e165", "Walter L Wright Jr.", "855"),
    11: ("a4cc65e3-dcb1-5f69-9179-248250d8e0d3", "Walter B Wriston", "855"),
    12: ("0977a3b5-f4d2-5fe8-9237-86e0b6f92bbe", "Charles S Wrobel", "855"),
    13: ("1e8cafa0-b2e1-5c4d-8178-f82a4feaf04d", "Stanley J Wrobel Jr.", "855"),
    14: ("6218e551-9e03-56ea-a15e-747a6240bd7a", "Conrad Wronski", "855"),
    15: ("26211f84-f80c-522b-ad2c-35ee335acfac", "Margaret M Wronski", "855"),
    16: ("c679d76f-b583-570d-91a4-bb3574961e0f", "Margaret O Wronski", "855"),
    17: ("e0a20e71-20db-5345-b554-e968a4b82b0d", "Bing K Wu", "855"),
    18: ("44eabc25-461f-5fd3-bb47-a889da19b58d", "James Wu", "855"),
    19: ("521c80ee-c975-552a-b41f-d565c60a921b", "George S Wuchinich", "855"),
    20: ("4b01db98-4e1c-54aa-880e-d801864cfd52", "Ferdinand Wuenschel", "855"),
    21: ("42aa2bdf-59a8-595c-ad29-12a60f188ac2", "William E Wuertenberg", "855"),
    22: ("8a7f2cc2-edbd-5193-b4ed-b6efbacae9d9", "Edward C Wuinee", "855"),
    23: ("aca25142-7a3a-5940-9e63-0ae3d53bb6bf", "Marilyn M Wunder", "855"),
    24: ("cb25c890-b435-588a-ae34-5bf5a0fc1e3f", "Frederic L Wunderlich", "855"),
    25: ("2e867ac7-8629-5831-bd81-825bec1cceb6", "Henry Wunsch", "855"),
    26: ("93dd2d8f-507f-57d5-b146-2e78f31275d3", "John H Wuorinen", "855"),
    27: ("cf53c258-0e02-581a-9a5f-77a80eb56165", "Suzanne Wurdeman", "855"),
    28: ("b3908766-14f9-5138-b106-bbe667298ff3", "Arthur O Wurtmann", "855"),
    29: ("8e12fb72-4e50-569d-b57c-d8aa2b223b37", "Walter Wusza", "855"),
    30: ("2ee50555-1e6f-56e2-876e-7f2a68153311", "Paul Wyamura", "855"),
    31: ("8d12681d-c67c-5c61-bec4-144eceb1f3f8", "Adam M Wyant Jr.", "855"),
    32: ("32feba01-fb07-52f9-89c0-3e38496a9ccd", "Harold W Wyatt", "855"),
    33: ("49a6b0cb-a5f9-5520-9c64-29e0792d438e", "William M Wyatt", "855"),
    34: ("ed4521e9-f90c-5109-9569-3130eef1913e", "Francis B Wyeth", "855"),
    35: ("5d034721-2ca7-5ca4-a3aa-d205efe0c255", "Vera Wygod", "855"),
    36: ("ae184ae4-4d5c-5d81-b319-ca11b61a9b27", "Stanley A Wyka", "855"),
    37: ("2d394ae9-4bfe-56e3-abff-5736520f1b23", "C P Wykeham-Mar", "855"),
    38: ("9be104b7-6150-5a79-b6cd-0a0cecd22446", "Allen C Wylie", "855"),
    39: ("3890f008-d6f6-5903-9921-31034b37902b", "Betty Jane Wylie", "855"),
    40: ("089b013f-4e02-5082-837f-64a14fd52908", "Glenn J Wylie", "856"),
    41: ("d49bd67f-a30d-57e0-b88a-1388abb1373c", "Glenn T Wylie", "856"),
    42: ("d2cf9c26-f78f-5999-9cd0-e97592fb167d", "Richard D Wylly", "856"),
    43: ("b164e6b5-74f0-56c9-bda4-d271418f2081", "Cecil F Wynatt Jr.", "856"),
    44: ("5d6efed7-0465-5d86-bf92-bfa923623d5b", "Hans Wynberg", "856"),
    45: ("36f7f5cb-3edf-532a-9912-23c7b968d25e", "James O Wynder", "856"),
    46: ("5b89f70b-2c13-5ced-9cdf-1ea9daba55a4", "Hans Wyner", "856"),
}

ARMY_OCCUPATIONS = {
    1: ("1943-05-11", "949", "transportation occupation, not elsewhere classified", "Transportation occupations, n.e.c.", "PDF physical page 174; historical category 9-49", "unknown"),
    14: ("1943-01-18", "048", "draftsman", "Draftsmen", "PDF physical page 171; historical category 0-48", "unknown"),
    17: ("1943-05-05", "019", "mechanical engineer", "Engineers, mechanical", "PDF physical page 170; historical category 0-19", "unknown"),
    21: ("1941-09-16", "480", "sheet-metal worker, coppersmith, or tinsmith", "Tinsmiths, coppersmiths, and sheet metal workers", "PDF physical page 174; historical category 4-80", "unknown"),
    22: ("1942-01-08", "678", "machine-shop or related occupation, not elsewhere classified", "Machine shop and related occupations, n.e.c.", "PDF physical page 174; historical category 6-78", "unknown"),
    24: ("1942-12-14", "992", "student", "Students", "PDF physical page 304; amended category 9-92", "student"),
    36: ("1942-09-25", "992", "student", "Students", "PDF physical page 304; amended category 9-92", "student"),
    41: ("1942-09-05", "965", "nonprocessing occupation in manufacturing, not elsewhere classified", "Nonprocessing occupations in manufacturing, n.e.c.", "PDF physical page 174; historical category 9-65", "unknown"),
    44: ("1943-07-14", "050", "laboratory technician or assistant", "Laboratory technicians and assistants", "PDF physical page 171; historical category 0-50", "unknown"),
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def source(key: str, **kwargs: object) -> dict[str, object]:
    value: dict[str, object] = {"key": key, "access_date": "2026-11-04"}
    value.update(kwargs)
    return value


def sources() -> list[dict[str, object]]:
    return [
        source(INDEX, stable_url="https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf", archival_identifier="RG 226, Entry A1-224, Boxes 854-856", title="OSS Personnel Files from Excel", author_creator="National Archives and Records Administration", repository_publisher="National Archives and Records Administration", publication_record_date="2010-12-23", locator="PDF page 515, rows 1-46; page 516 boundary and all page 515 rows visually checked at 180 dpi", source_quality="A_direct_official", collection_name="Records of the Office of Strategic Services, Record Group 226", rights_notes="All 46 printed rows remain separate. Full protected identifiers remain private."),
        source(ARMY, source_id="cf280d3e-1262-5963-90d7-40ffa66c53a3", stable_url="https://catalog.archives.gov/id/1263923", archival_identifier="National Archives Identifier 1263923; parent series NAID 604357", title="Electronic Army Serial Number Merged File, ca. 1938-1946", author_creator="Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration", repository_publisher="National Archives and Records Administration", publication_record_date="1938-1946; merged file created 2002", locator="Official unrestricted ASNEF.FIN.DAT; eleven Batch 1025 protected-identifier identity candidates reviewed", source_quality="A_direct_official", collection_name="World War II Army Enlistment Records", document_number="ASNEF.FIN.DAT", rights_notes="No raw record or full protected identifier is retained in public assets. Coded occupations identify neither employer nor workplace."),
        source(TECH, source_id="f24044fe-5fcd-5d78-96d4-25d577e90703", stable_url="https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf", archival_identifier="NN3-064-03-008; National Archives Identifier 1263923", title="World War II Army Enlistment Records: Reference Copy of Technical Documentation", author_creator="National Archives and Records Administration", repository_publisher="National Archives at College Park - Electronic Records", publication_record_date="1994-2005; reference copy modified 2011", locator="PDF physical pages 44-46; identifier, name, Army-entry-date, grade and civilian-occupation fields", source_quality="A_direct_official", collection_name="World War II Army Enlistment Records technical documentation", rights_notes="Used to interpret selected fields only; source damage, coding limits and incomplete coverage remain applicable."),
        source(CODES, source_id="ace136c1-722a-5af0-a43b-bab53792ae6a", stable_url="https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1CL_SD.pdf", archival_identifier="National Archives Identifier 1263923; Code No. 30", title="NARA Compiled Code Lists for the Electronic Army Serial Number Merged File", author_creator="National Archives and Records Administration", repository_publisher="National Archives at College Park - Electronic Records", publication_record_date="2011-01-12; modified 2011-03-17", locator="PDF physical pages 170-175 and 304; Batch 1025 categories visually checked", source_quality="A_direct_official", collection_name="World War II Army Enlistment Records technical documentation", rights_notes="Historical categories identify neither employer, institution nor workplace. Code 999 remains uninterpreted."),
        source(TUFTS_WRISTON, stable_url="https://exhibits.tufts.edu/spotlight/wriston-archives/feature/timeline-1888-1974", archival_identifier="Walter B. Wriston Archives timeline, 1888-1974", title="Timeline, 1888-1974", author_creator="Tufts Archival Research Center", repository_publisher="Tufts University", locator="Entries for 1919 and 1937-1946, including Department of State and U.S. Army service", source_quality="B_authoritative_institutional", collection_name="Walter B. Wriston Archives", rights_notes="Institutional chronology; the exact OSS transfer date is not supplied."),
        source(COLUMBIA_WUORINEN, stable_url="https://upload.wikimedia.org/wikipedia/commons/e/e3/Annual_report_%28IA_annualreport1944colu%29.pdf", archival_identifier="Columbia University Annual Report 1944, printed page 8", title="Annual Report of Columbia University for 1944", author_creator="Columbia University Office of the President", repository_publisher="Columbia University", publication_record_date="1944", locator="PDF physical page 18, printed page 8; John H. Wuorinen entry visually checked at 180 dpi", source_quality="B_authoritative_institutional", collection_name="Columbia University annual reports", rights_notes="Contemporaneous institutional report digitized by the Internet Archive; stable public mirror used for access."),
        source(CTPOST_WURTMANN, stable_url="https://www.ctpost.com/past_obituaries/article/Arthur-O-Wurtmann-92-13973403.php", title="Arthur O. Wurtmann, 92", author_creator="Wilton Bulletin", repository_publisher="Connecticut Post", publication_record_date="2013-11-04", locator="Obituary chronology from Nichols College through State Department, Office of Naval Attache, U.S. Navy and OSS selection", source_quality="C_reputable_contemporary_or_scholarly", rights_notes="Obituary evidence is published with qualification; it does not replace the personnel file."),
        source(STARTRIB_WYLIE, stable_url="https://obituaries.startribune.com/obituary/betty-jane-wylie-myhre-1090561590", title="Betty Jane (Wylie) Myhre Obituary", repository_publisher="Minnesota Star Tribune", publication_record_date="2007-08-05", locator="Obituary paragraph covering Carleton graduation, General Mills employment and civilian OSS service in London", source_quality="C_reputable_contemporary_or_scholarly", rights_notes="Obituary evidence is published with qualification; unrelated living-family details are not reproduced."),
        source(USMC_WYLLY, stable_url="https://www.usmcu.edu/Portals/218/Herringbone%20Cloak%20-%20GI%20Dagger%20Marines%20Of%20The%20OSS.pdf", archival_identifier="D 214.14/3:H 43; LCCN 89602625", title="Herringbone Cloak - GI Dagger: Marines of the OSS", author_creator="Major Robert E. Mattingly, United States Marine Corps", repository_publisher="History and Museums Division, Headquarters, U.S. Marine Corps", publication_record_date="1989", locator="PDF physical page 342, printed page 314; Reprise list under First Lieutenants; visually checked at 180 dpi", source_quality="A_direct_official", collection_name="United States Marine Corps Occasional Papers", rights_notes="The official list identifies rank and OSS theater, not a civilian employer."),
        source(CEN_WYNBERG, stable_url="https://cen.acs.org/articles/89/i39/Hans-Wynberg.html", title="Hans Wynberg", repository_publisher="Chemical & Engineering News, American Chemical Society", publication_record_date="2011-09-26", locator="Obituary paragraphs covering New York schooling, Charles Pfizer & Co. summer work and subsequent OSS service", source_quality="C_reputable_contemporary_or_scholarly", rights_notes="Professional-society obituary; only the shortest necessary paraphrase is retained."),
        source(RUG_WYNBERG, stable_url="https://www.rug.nl/alumni/magazines-and-newsletters/broerstraat-5/pdf/broerstraat5-2016-no-afraid-of-anyone.pdf", title="Not afraid of anyone", author_creator="Kirsten Otten", repository_publisher="University of Groningen", publication_record_date="2016-12", locator="PDF physical page 1, printed page 14; Hans Wijnberg's New York schooling, U.S. military service, OSS training and Operation Greenup; visually checked at 180 dpi", source_quality="B_authoritative_institutional", collection_name="Broerstraat 5", rights_notes="Institutional alumni article supplies the Wijnberg spelling and OSS chronology; it does not name Pfizer."),
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {"key": ORG_US_ARMY, "organization_id": "28a26f92-78af-5a1a-9c09-a843eb5975b4", "canonical_name": "United States Army", "historical_name": "United States Army", "aliases": ["U.S. Army", "Army", "AUS"], "organization_type": "military service", "sector": "military", "country": "United States", "normalization_notes": "Military assignment is modeled separately from civilian employment."},
        {"key": ORG_STATE, "organization_id": "4d2fbb5f-218d-5445-b7b3-4c2fd22f0286", "canonical_name": "United States Department of State", "historical_name": "Department of State", "aliases": ["U.S. Department of State"], "organization_type": "federal executive department", "sector": "federal_government", "city": "Washington", "state_or_region": "District of Columbia", "country": "United States", "normalization_notes": "Government assignments remain distinct from private employment."},
        {"key": ORG_COLUMBIA, "organization_id": "87e3d52a-9ace-512a-9677-e966b7fbd5e5", "canonical_name": "Columbia University", "historical_name": "Columbia University", "organization_type": "university", "sector": "academia_and_research", "city": "New York", "state_or_region": "New York", "country": "United States", "normalization_notes": "Existing historical institution reused."},
        {"key": ORG_US_NAVY, "organization_id": "3960fa8e-a551-56cf-8305-b2b9e4961b9d", "canonical_name": "United States Navy", "historical_name": "United States Navy", "aliases": ["U.S. Navy"], "organization_type": "military service", "sector": "military", "country": "United States", "normalization_notes": "The Office of Naval Attache posting is preserved in the affiliation wording."},
        {"key": ORG_USMC, "organization_id": "48217a0d-8af9-5502-b0ed-f24d49f634f9", "canonical_name": "United States Marine Corps", "historical_name": "United States Marine Corps", "aliases": ["U.S. Marine Corps", "USMC"], "organization_type": "military service", "sector": "military", "country": "United States", "normalization_notes": "Marine Corps commission is modeled separately from civilian employment."},
        {"key": ORG_GENERAL_MILLS, "organization_id": "510706df-406b-55b7-bb96-9a18bd7ceaee", "canonical_name": "General Mills, Inc.", "historical_name": "General Mills", "aliases": ["General Mills"], "organization_type": "food manufacturer", "sector": "business_and_industry", "city": "Minneapolis", "state_or_region": "Minnesota", "country": "United States", "normalization_notes": "The obituary's historical General Mills wording is preserved."},
        {"key": ORG_PFIZER, "canonical_name": "Charles Pfizer & Co.", "historical_name": "Charles Pfizer & Co.", "aliases": ["Charles Pfizer and Company"], "organization_type": "chemical and pharmaceutical manufacturer", "sector": "business_and_industry", "city": "New York", "state_or_region": "New York", "country": "United States", "normalization_notes": "The wartime historical company name is preserved; no modern corporate name is substituted."},
    ]


def affiliation(key: str, row: int, relationship: str, temporal: str, identity: str, confidence: str, quality: str, status: str = "published", **kwargs: object) -> dict[str, object]:
    value: dict[str, object] = {
        "key": key,
        "person_id": PEOPLE[row][0],
        "relationship_type": relationship,
        "pre_oss_temporal_basis": temporal,
        "identity_confidence": identity,
        "claim_confidence": confidence,
        "source_quality": quality,
        "publication_status": status,
    }
    value.update(kwargs)
    return value


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, _label, _locator, relationship) in ARMY_OCCUPATIONS.items():
        values.append(affiliation(
            f"{slug(PEOPLE[row][1])}-army-occupation-b1025", row, relationship,
            "strongly_date_bounded", "confirmed", "medium", "A_direct_official", "publish_qualified",
            occupation=occupation, end_date=date,
            date_precision=f"Historical civilian-occupation code {code} was recorded at Army entry on {date}; no named employer or institution is supplied.",
            country="United States", immediate_pre_oss=False, last_civilian_pre_service=False,
            research_notes="Broad historical category only; excluded from verified-employer analytics and not narrowed beyond the official wording.",
        ))
    values.extend([
        affiliation("walter-wriston-state-b1025", 11, "government_assignment", "strongly_date_bounded", "high_confidence", "medium", "B_authoritative_institutional", "publish_qualified", organization_key=ORG_STATE, organization_name_as_found="Special Division, Dept. of State", role_title="officer", start_date="1942-05", end_date="1943-01", date_precision="The Tufts timeline dates the Special Division assignment from May 1942 through January 1943; it overlaps Army service by about one month.", city="Washington", state_or_region="District of Columbia", country="United States", immediate_pre_oss=False, last_civilian_pre_service=True, research_notes="Best-supported last civilian government assignment before and briefly overlapping Army service; not labeled a private employer."),
        affiliation("walter-wriston-army-b1025", 11, "military_assignment", "probable_immediate", "high_confidence", "medium", "B_authoritative_institutional", "publish_qualified", organization_key=ORG_US_ARMY, organization_name_as_found="U.S. Army", role_title="lieutenant", start_date="1942-12", end_date="1946-04", date_precision="The Tufts timeline dates Army service but does not state the exact OSS transfer date.", country="United States", immediate_pre_oss=True, last_civilian_pre_service=False, research_notes="The Army is the best-supported military pathway into the indexed OSS personnel record; exact assignment chronology still requires Box 855."),
        affiliation("john-wuorinen-columbia-b1025", 26, "employment", "strongly_date_bounded", "high_confidence", "high", "B_authoritative_institutional", organization_key=ORG_COLUMBIA, organization_name_as_found="Columbia University", role_title="Associate Professor of History", occupation="historian and university professor", date_precision="Columbia's contemporaneous 1944 report identifies Wuorinen simultaneously by academic title and as an OSS section chief.", city="New York", state_or_region="New York", country="United States", immediate_pre_oss=True, last_civilian_pre_service=True, research_notes="The report directly connects the exact academic identity and OSS role; no military intermediary is documented."),
        affiliation("arthur-wurtmann-state-b1025", 28, "government_assignment", "strongly_date_bounded", "high_confidence", "medium", "C_reputable_contemporary_or_scholarly", "publish_qualified", organization_key=ORG_STATE, organization_name_as_found="State Department", start_date="1943", date_precision="The obituary says Wurtmann went to work for the State Department in 1943 before his London posting and Navy commission.", city="Washington", state_or_region="District of Columbia", country="United States", immediate_pre_oss=False, last_civilian_pre_service=True, research_notes="Government assignment, not private employment; the personnel file remains necessary for exact dates."),
        affiliation("arthur-wurtmann-navy-b1025", 28, "military_assignment", "explicit_immediate", "high_confidence", "medium", "C_reputable_contemporary_or_scholarly", "publish_qualified", organization_key=ORG_US_NAVY, organization_name_as_found="Office of Naval Attache in London", role_title="lieutenant", start_date="1943", date_precision="The obituary orders the London Naval Attache commission immediately before selection by William J. Donovan for OSS.", city="London", country="United Kingdom", immediate_pre_oss=True, last_civilian_pre_service=False, research_notes="Best-supported immediate military affiliation; published with qualification because the evidence is an obituary."),
        affiliation("betty-wylie-general-mills-b1025", 39, "employment", "explicit_immediate", "high_confidence", "medium", "C_reputable_contemporary_or_scholarly", "publish_qualified", organization_key=ORG_GENERAL_MILLS, organization_name_as_found="General Mills", date_precision="The obituary explicitly says she left her General Mills job and moved to London as a civilian OSS employee.", state_or_region="Minnesota", country="United States", immediate_pre_oss=True, last_civilian_pre_service=True, research_notes="Explicitly sequenced civilian employer; retained at medium confidence pending a direct personnel or employer record."),
        affiliation("richard-wylly-usmc-b1025", 42, "military_assignment", "explicit_immediate", "high_confidence", "high", "A_direct_official", organization_key=ORG_USMC, organization_name_as_found="United States Marine Corps", role_title="first lieutenant", country="United States", immediate_pre_oss=True, last_civilian_pre_service=False, date_precision="The official Marine Corps history lists Richard D. Wylly under First Lieutenants among Marines of the OSS and gives France as theater.", research_notes="This establishes the military pathway and OSS theater, not a civilian employer."),
        affiliation("hans-wynberg-pfizer-b1025", 44, "employment", "strongly_date_bounded", "confirmed", "high", "C_reputable_contemporary_or_scholarly", organization_key=ORG_PFIZER, organization_name_as_found="Charles Pfizer & Co.", role_title="summer production-site worker", occupation="production-site worker", date_precision="The C&EN obituary places the summer job after New York high school and before U.S. military and OSS service; no exact year is supplied.", city="New York", state_or_region="New York", country="United States", immediate_pre_oss=False, last_civilian_pre_service=True, research_notes="Best-supported last civilian employer before military service; the historical company name is preserved."),
        affiliation("hans-wynberg-army-b1025", 44, "military_assignment", "explicit_immediate", "confirmed", "high", "B_authoritative_institutional", organization_key=ORG_US_ARMY, organization_name_as_found="U.S. military service", role_title="soldier; later indexed as second lieutenant", start_date="1943-07-14", date_precision="The official Army record dates entry; the Groningen article says he enlisted and then trained with OSS before Operation Greenup.", country="United States", immediate_pre_oss=True, last_civilian_pre_service=False, research_notes="The Army pathway is separate from the Pfizer civilian-employer claim. Entry grade is not treated as his later indexed rank."),
    ])
    return values


def claim(key: str, row: int, claim_type: str, text: str, paraphrase: str, identity: str, temporal: str, quality: str, confidence: str, source_links: list[dict[str, str]], notes: str, status: str = "published", affiliation_key: str | None = None) -> dict[str, object]:
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
        "publication_status": status,
        "match_notes": notes,
        "sources": source_links,
    }
    if affiliation_key:
        value["affiliation_key"] = affiliation_key
    return value


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, label, locator, _relationship) in ARMY_OCCUPATIONS.items():
        identity_links = [{"source_key": INDEX}, {"source_key": ARMY}, {"source_key": TECH}]
        if row == 44:
            identity_links.extend([{"source_key": RUG_WYNBERG, "support_type": "context_only"}, {"source_key": CEN_WYNBERG, "support_type": "context_only"}])
        values.append(claim(
            f"identity-{slug(PEOPLE[row][1])}-b1025", row, "identity",
            f"The indexed {PEOPLE[row][1]} and the reviewed Army entry represent the same person.",
            "Exact official name agreement and a nonshared protected identifier connect the records; the identifier remains private.",
            "Confirmed by exact name and a nonshared protected identifier.",
            f"The Army entry is dated {date}; it supports identity and entry chronology, not an OSS transfer date.",
            "A_direct_official", "confirmed", identity_links,
            "No full identifier or raw Army record is published.",
        ))
        values.append(claim(
            f"occupation-{slug(PEOPLE[row][1])}-b1025", row, "occupation",
            f"At Army entry, {PEOPLE[row][1]} was recorded in the historical category '{label}'.",
            f"The Army occupation field contains code {code}; the reviewed code list renders it as {occupation}.",
            "Confirmed identity from exact name and nonshared protected identifier.",
            f"Recorded at Army entry on {date}; this does not prove the immediate pre-OSS role.",
            "A_direct_official", "medium", [{"source_key": ARMY}, {"source_key": TECH}, {"source_key": CODES, "locator_override": locator}],
            "Historical category only; no employer, institution, workplace, or exact job title is inferred.", "publish_qualified",
            f"{slug(PEOPLE[row][1])}-army-occupation-b1025",
        ))
    values.append(claim(
        "identity-francis-wyeth-b1025", 34, "identity",
        "The indexed Francis B Wyeth and the reviewed Army entry represent the same person.",
        "Exact official name agreement and a nonshared protected identifier connect the records; code 999 remains uninterpreted.",
        "Confirmed by exact name and a nonshared protected identifier.",
        "The Army entry is dated 1940-08-20; no occupation or OSS transfer date is inferred.",
        "A_direct_official", "confirmed", [{"source_key": INDEX}, {"source_key": ARMY}, {"source_key": TECH}, {"source_key": CODES, "support_type": "context_only"}],
        "Identity only. Code 999 remains uninterpreted and has no public occupation label.",
    ))
    values.extend([
        claim("identity-walter-wriston-b1025", 11, "identity", "Indexed Walter B Wriston is the Walter Bigelow Wriston documented by Tufts University.", "The rare exact name and middle initial align with Tufts' full middle name, education, State Department service and wartime Army commission.", "High confidence from the rare exact name, middle initial and compatible wartime chronology.", "The institutional timeline covers the prewar and wartime period.", "B_authoritative_institutional", "high", [{"source_key": INDEX}, {"source_key": TUFTS_WRISTON}], "No claim is made that postwar Citibank employment preceded OSS."),
        claim("state-walter-wriston-b1025", 11, "last_civilian_pre_service", "Walter B. Wriston's last documented civilian government assignment before Army service was the Department of State Special Division.", "Tufts dates the State Department assignment from May 1942 through January 1943 and Army service from December 1942.", "High-confidence identity from rare exact name and compatible chronology.", "Strongly date-bounded, with a one-month overlap that remains explicit.", "B_authoritative_institutional", "medium", [{"source_key": TUFTS_WRISTON}], "Government assignment, not private employment; exact OSS transfer still requires Box 855.", "publish_qualified", "walter-wriston-state-b1025"),
        claim("army-walter-wriston-b1025", 11, "immediate_pre_oss_affiliation", "The U.S. Army is Walter B. Wriston's best-supported military pathway into the indexed OSS record.", "Tufts dates his lieutenant service from December 1942 to April 1946, overlapping the wartime OSS period.", "High-confidence identity from rare exact name and compatible State Department-to-Army chronology.", "Probable immediate affiliation; the exact Army-to-OSS assignment date is not supplied.", "B_authoritative_institutional", "medium", [{"source_key": INDEX}, {"source_key": TUFTS_WRISTON}], "Published with qualification and excluded from any claim of a precise OSS transfer date.", "publish_qualified", "walter-wriston-army-b1025"),
        claim("identity-john-wuorinen-b1025", 26, "identity", "Indexed John H Wuorinen is Columbia historian John H. Wuorinen, chief of the OSS Scandinavian-Baltic Section.", "Columbia's contemporaneous report gives the exact name, middle initial, academic title and specific OSS section-chief role.", "High confidence from an exceptionally specific contemporaneous institutional source.", "The 1944 report directly covers his wartime Columbia and OSS roles.", "B_authoritative_institutional", "high", [{"source_key": INDEX}, {"source_key": COLUMBIA_WUORINEN}], "A direct institutional identity-and-role bridge supports publication."),
        claim("immediate-john-wuorinen-b1025", 26, "immediate_pre_oss_affiliation", "John H. Wuorinen's best-supported immediate pre-OSS affiliation was Columbia University, where he was an associate professor of history.", "The 1944 Columbia report identifies him by academic title while naming his OSS section-chief assignment.", "High-confidence exact identity and OSS role from a contemporaneous institutional report.", "Strongly date-bounded and contemporaneous; no intervening organization is documented.", "B_authoritative_institutional", "high", [{"source_key": COLUMBIA_WUORINEN}], "Columbia is treated as an employer because the source supplies a faculty title, not merely attendance.", "published", "john-wuorinen-columbia-b1025"),
        claim("civilian-john-wuorinen-b1025", 26, "last_civilian_pre_service", "Columbia University is John H. Wuorinen's last documented civilian employer before or concurrent with OSS service.", "The university's 1944 report directly joins his associate-professor title and OSS section-chief role.", "High-confidence exact identity and specific OSS role.", "Strongly date-bounded; no military intermediary is documented.", "B_authoritative_institutional", "high", [{"source_key": COLUMBIA_WUORINEN}], "The chronology is reported without inventing a resignation or transfer date.", "published", "john-wuorinen-columbia-b1025"),
        claim("identity-arthur-wurtmann-b1025", 28, "identity", "Indexed Arthur O Wurtmann is Arthur Otto Wurtmann, the State Department and Navy officer selected for OSS.", "The rare exact name and middle initial align with an obituary that gives a detailed State Department, Navy and OSS chronology.", "High confidence from the rare exact name and direct OSS narrative; personnel-file confirmation remains desirable.", "The obituary explicitly covers 1943 entry into wartime service.", "C_reputable_contemporary_or_scholarly", "high", [{"source_key": INDEX}, {"source_key": CTPOST_WURTMANN}], "The expanded middle name is retained as a documented variant."),
        claim("state-arthur-wurtmann-b1025", 28, "last_civilian_pre_service", "Arthur O. Wurtmann's last documented civilian government assignment before Navy service was with the U.S. Department of State.", "The obituary says he began State Department work in Washington in 1943 before the London Naval Attache posting.", "High-confidence identity from the rare exact name and direct OSS chronology.", "Strongly date-bounded; exact appointment dates are not supplied.", "C_reputable_contemporary_or_scholarly", "medium", [{"source_key": CTPOST_WURTMANN}], "Government assignment is not recast as private employment.", "publish_qualified", "arthur-wurtmann-state-b1025"),
        claim("navy-arthur-wurtmann-b1025", 28, "immediate_pre_oss_affiliation", "Arthur O. Wurtmann's best-supported immediate pre-OSS affiliation was the U.S. Navy Office of Naval Attache in London.", "The obituary orders his London Navy commission immediately before William J. Donovan selected him for OSS.", "High-confidence identity from the rare exact name and direct OSS narrative.", "Explicit immediate sequence, but exact dates require the personnel file.", "C_reputable_contemporary_or_scholarly", "medium", [{"source_key": CTPOST_WURTMANN}], "Published with qualification because the source is a reputable obituary, not the personnel file.", "publish_qualified", "arthur-wurtmann-navy-b1025"),
        claim("identity-betty-wylie-b1025", 39, "identity", "Indexed Betty Jane Wylie is Betty Jane Wylie Myhre, the civilian OSS employee documented by the Star Tribune.", "The distinctive full name, 1940 Carleton graduation, General Mills employment and civilian OSS service in London form a specific identity bridge.", "High confidence from the distinctive full name and direct OSS narrative.", "The obituary explicitly covers the transition into wartime OSS service.", "C_reputable_contemporary_or_scholarly", "high", [{"source_key": INDEX}, {"source_key": STARTRIB_WYLIE}], "The unrelated Canadian writer of the same name is rejected as a later-born namesake."),
        claim("immediate-betty-wylie-b1025", 39, "immediate_pre_oss_affiliation", "Betty Jane Wylie's immediate pre-OSS employer was General Mills.", "The obituary explicitly states that she left her General Mills job and moved to London as a civilian OSS employee.", "High-confidence identity from the distinctive full name and detailed OSS role.", "Explicit immediate sequence; no exact departure date is supplied.", "C_reputable_contemporary_or_scholarly", "medium", [{"source_key": STARTRIB_WYLIE}], "Published with qualification pending an employer or personnel record.", "publish_qualified", "betty-wylie-general-mills-b1025"),
        claim("civilian-betty-wylie-b1025", 39, "last_civilian_pre_service", "General Mills is Betty Jane Wylie's last documented civilian employer before OSS service.", "The obituary directly sequences General Mills employment before civilian OSS service in London.", "High-confidence identity from the distinctive full name and detailed OSS narrative.", "Explicitly the job she left for OSS; no intervening affiliation is named.", "C_reputable_contemporary_or_scholarly", "medium", [{"source_key": STARTRIB_WYLIE}], "The claim remains qualified because it rests on one reputable obituary.", "publish_qualified", "betty-wylie-general-mills-b1025"),
        claim("identity-richard-wylly-b1025", 42, "identity", "Indexed Richard D Wylly is the U.S. Marine Corps first lieutenant listed among Marines of the OSS.", "The official Marine Corps history supplies the exact name and middle initial, first-lieutenant rank, OSS context and France theater.", "High confidence from exact name, middle initial, rank and direct official OSS listing.", "The official list concerns wartime OSS service.", "A_direct_official", "high", [{"source_key": INDEX}, {"source_key": USMC_WYLLY}], "The list does not supply a civilian employer and none is inferred."),
        claim("usmc-richard-wylly-b1025", 42, "immediate_pre_oss_affiliation", "Richard D. Wylly's documented institutional pathway into OSS was as a U.S. Marine Corps first lieutenant.", "The official Marine Corps history lists Wylly under First Lieutenants among Marines who served with OSS, with France as theater.", "High-confidence exact identity from the official listing.", "Explicit institutional relationship to OSS; no civilian predecessor is supplied.", "A_direct_official", "high", [{"source_key": USMC_WYLLY}], "Military assignment is not labeled civilian employment.", "published", "richard-wylly-usmc-b1025"),
        claim("pfizer-hans-wynberg-b1025", 44, "last_civilian_pre_service", "Charles Pfizer & Co. is Hans Wynberg's last documented civilian employer before U.S. military and OSS service.", "C&EN places a summer job at the Pfizer production site after high school and immediately before describing OSS service; Army records corroborate laboratory work.", "Confirmed identity from a nonshared protected identifier, rare name and independent OSS accounts using Wynberg and Wijnberg.", "Strongly date-bounded before military service; the exact summer is not supplied.", "C_reputable_contemporary_or_scholarly", "high", [{"source_key": CEN_WYNBERG}, {"source_key": ARMY, "support_type": "context_only"}, {"source_key": CODES, "support_type": "context_only"}], "The official occupation code corroborates laboratory work but is not treated as proof of the employer.", "published", "hans-wynberg-pfizer-b1025"),
        claim("army-hans-wynberg-b1025", 44, "immediate_pre_oss_affiliation", "Hans Wynberg's immediate institutional pathway into OSS was U.S. Army service beginning in July 1943.", "The Army record dates entry; Groningen says he enlisted, trained with OSS and deployed on Operation Greenup.", "Confirmed by exact name, nonshared protected identifier and independent Wynberg/Wijnberg OSS narratives.", "Explicit military-to-OSS sequence; the exact training start date is not supplied.", "B_authoritative_institutional", "high", [{"source_key": ARMY}, {"source_key": TECH}, {"source_key": RUG_WYNBERG}, {"source_key": CEN_WYNBERG, "support_type": "context_only"}], "The Army pathway remains separate from the Pfizer civilian-employer claim.", "published", "hans-wynberg-army-b1025"),
    ])
    return values


def unresolved_reason(row: int) -> str:
    reasons = {
        6: "A protected identifier is shared with the separately printed Robert G Wright row, so neither identity can absorb the other or any Army evidence.",
        7: "A protected identifier is shared with the separately printed Robert C Wright row, so neither identity can absorb the other or any Army evidence.",
        8: "This second Robert G Wright row carries a different protected identifier from the adjacent conflict pair and remains a separate common-name person.",
        18: "The index prints only the common name James Wu and the word Chinese in the rank column; no unique external identity bridge was found.",
        20: "The printed second-lieutenant rank does not distinguish this person from namesakes, and no reliable OSS-to-employment bridge was found.",
        27: "A Washington Post obituary for a postwar CIA secretary supplies no pre-OSS employer or secure bridge to the indexed person and is rejected for this claim.",
        29: "A Project Eagle discovery lead mentions a Lieutenant Wusza without enough identifiers to establish Walter Wusza or a pre-OSS affiliation.",
        35: "Yearbook and literary-archive leads for Vera Wygod do not establish an OSS, personnel-file, or pre-OSS employment bridge.",
        37: "The printed surname is visibly truncated as Wykeham-Mar; Major and British A are preserved, but no full-name resolution was found.",
        40: "This Glenn J Wylie remains separate from the confirmed Glenn T Wylie Army record; middle initials are not interchangeable.",
        45: "A 1965 criminal-case namesake is postwar, unrelated and rejected; no reliable OSS or pre-OSS affiliation bridge was found.",
    }
    return reasons.get(row, "Accessible exact-name, official, CIA, OSS, employer, occupation, obituary, institutional, newspaper, directory and archival searches produced no reliable identity-and-affiliation bridge; unbridged namesakes and postwar-only leads were rejected.")


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
    special = set(ARMY_OCCUPATIONS) | {11, 19, 26, 28, 34, 39, 42, 44}
    values: list[dict[str, object]] = []
    for row in sorted(set(PEOPLE) - special):
        reason = unresolved_reason(row)
        if row in {6, 7}:
            values.append(base_update(row, identity_status="conflicting", identity_evidence=f"The visually verified page 515 source preserves {PEOPLE[row][1]}, but its protected identifier is shared by a differently initialed source row. {reason}", research_status="conflicting_sources", possible_duplicate_group="batch1025-robert-wright-identifier-conflict", archival_review_priority="critical", next_action=f"Jointly review both indexed Box 854 files before resolving either person. {reason}"))
            continue
        updates: dict[str, object] = {
            "identity_status": "unresolved",
            "identity_evidence": f"The visually verified page 515 source preserves {PEOPLE[row][1]} and Box {PEOPLE[row][2]}. {reason}",
            "research_status": "requires_archival_review",
            "archival_review_priority": "critical" if row in {8, 18, 20, 27, 29, 35, 37, 40, 45} else "high",
            "next_action": f"Review indexed Box {PEOPLE[row][2]} for corroborating identifiers, immediate pre-OSS affiliation and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}",
        }
        if row == 18:
            updates.update({"personnel_category": "foreign_or_allied_military_personnel", "allied_or_foreign_personnel": True})
        elif row in {20, 31, 43}:
            updates.update({"personnel_category": "commissioned_army_officer", "commissioned_officer": True})
        elif row == 37:
            updates.update({"personnel_category": "foreign_or_allied_military_personnel", "commissioned_officer": True, "allied_or_foreign_personnel": True})
        values.append(base_update(row, **updates))
    for row in sorted(set(ARMY_OCCUPATIONS) - {44}):
        values.append(base_update(row, identity_status="confirmed", identity_evidence="A nonshared protected identifier and exact official name agreement connect the index and Army records; the identifier remains private.", personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="occupation_only_found", nara_catalog_id="1263923", next_action=f"Review indexed Box {PEOPLE[row][2]} to identify a named employer or institution and establish Army-to-OSS chronology; the bulk record supplies only a historical occupation category."))
    values.extend([
        base_update(34, identity_status="confirmed", identity_evidence="A nonshared protected identifier and exact official name agreement connect the records; code 999 remains uninterpreted and the identifier remains private.", personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="requires_archival_review", nara_catalog_id="1263923", archival_review_priority="high", next_action="Review Box 855 for Francis B Wyeth's named employer, occupation and Army-to-OSS chronology. The historical code 999 is preserved without interpretation."),
        base_update(11, identity_status="high_confidence", identity_evidence="The rare exact name and middle initial align with Tufts' Walter Bigelow Wriston chronology of education, Department of State service and wartime Army commission.", name_variants=["Walter Bigelow Wriston", "Walter B. Wriston"], replace_name_variants=False, personnel_category="commissioned_army_officer", commissioned_officer=True, allied_or_foreign_personnel=False, research_status="completed", archival_review_priority="high", next_action="Review Box 855 for the exact State Department-to-Army-to-OSS transfer chronology; the one-month State/Army overlap remains explicit."),
        base_update(26, identity_status="high_confidence", identity_evidence="Columbia's contemporaneous annual report gives the exact name, middle initial, associate-professor title and specific OSS Scandinavian-Baltic Section leadership role.", name_variants=["John H. Wuorinen"], replace_name_variants=False, personnel_category="civilian_professional_or_administrative_grade", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="verified_employer_found", archival_review_priority="medium", next_action="Review Box 855 for exact Columbia leave and OSS appointment dates; the employer and role are already strongly documented."),
        base_update(28, identity_status="high_confidence", identity_evidence="The rare exact name and middle initial align with a detailed obituary chronology from the State Department through the Navy and OSS.", name_variants=["Arthur Otto Wurtmann"], replace_name_variants=False, personnel_category="commissioned_naval_officer", commissioned_officer=True, allied_or_foreign_personnel=False, research_status="completed", archival_review_priority="high", next_action="Review Box 855 to confirm State Department appointment, London Naval Attache posting and OSS selection dates."),
        base_update(39, identity_status="high_confidence", identity_evidence="The distinctive full name, Carleton chronology, General Mills employment and detailed civilian OSS London role align in a reputable obituary.", name_variants=["Betty Jane Wylie Myhre", "Betty Jane Myhre"], replace_name_variants=False, personnel_category="civilian_professional_or_administrative_grade", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="documented_prewar_employer_found", archival_review_priority="high", next_action="Review Box 855 or General Mills records to confirm employment dates and the OSS London appointment; the employer sequence is explicit but currently medium confidence."),
        base_update(42, identity_status="high_confidence", identity_evidence="An official Marine Corps history lists the exact Richard D. Wylly name and middle initial as a first lieutenant among Marines of the OSS in France.", personnel_category="commissioned_marine_corps_officer", commissioned_officer=True, allied_or_foreign_personnel=False, research_status="completed", archival_review_priority="high", next_action="Review Box 856 to identify Wylly's last civilian employer and exact Marine-to-OSS assignment dates."),
        base_update(44, identity_status="confirmed", identity_evidence="A nonshared protected identifier and exact Army name confirm Hans Wynberg; University of Groningen's Hans Wijnberg spelling and two independent OSS narratives establish the documented variant and wartime identity.", name_variants=["Hans Wijnberg"], replace_name_variants=False, personnel_category="commissioned_army_officer", commissioned_officer=True, allied_or_foreign_personnel=False, research_status="verified_employer_found", nara_catalog_id="1263923", archival_review_priority="medium", next_action="Review Box 856 to confirm the Pfizer employment dates, Army promotion and OSS training chronology; the employer and military pathway are already strongly supported."),
    ])
    if len(values) != 45:
        raise RuntimeError(f"Expected 45 person updates after preserving prior row 19 research, generated {len(values)}")
    if any(item["person_id"] == PEOPLE[19][0] for item in values):
        raise RuntimeError("Batch 1025 must preserve George S Wuchinich's prior reviewed record")
    return values


def research_attempts() -> list[dict[str, object]]:
    substantiated = set(ARMY_OCCUPATIONS) | {11, 26, 28, 34, 39, 42, 44}
    attempts: list[dict[str, object]] = []
    for row, (person_id, name, box) in PEOPLE.items():
        if row == 19:
            continue
        if row in substantiated:
            outcome = "source_reviewed"
            reviewed = 9 if row in {11, 26, 28, 39, 42, 44} else 6
            rejected = 3
            note = "At least one identity, occupation, employer or institutional-pathway outcome is preserved with claim-level citations; remaining employer or temporal questions remain explicit."
        else:
            outcome = "candidate_rejected"
            reviewed = 5
            rejected = 4
            note = unresolved_reason(row)
        attempts.append({
            "key": f"page515-row{row}-{slug(name)}-b1025",
            "person_id": person_id,
            "source_adapter": "manual_staged_protocol",
            "query_text": f"{name}; NARA OSS index context; exact-name and meaningful initial, suffix, punctuation, transliteration and OCR variants; OSS, CIA Reading Room, rank, branch, assignment and protected-identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory and archival searches; indexed Box {box}",
            "query_variant_type": "staged_identity_employment_archival_protocol_batch_1025",
            "started_at": "2026-11-04T15:35:00Z",
            "completed_at": "2026-11-04T18:30:00Z",
            "outcome": outcome,
            "sources_reviewed": reviewed,
            "candidate_sources_rejected": rejected,
            "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, postwar-only leads and sources without an OSS, protected-identifier, rank, unit or personnel-file bridge were rejected. Army categories were not converted into named employers. Shared identifiers never triggered a merge.",
            "research_notes": f"{note} The official index, exact-name OSS searches, grouped CIA Reading Room checks, and employer, occupation, obituary, institutional, newspaper, directory and archival searches were reviewed as applicable. Page 515, the page 516 boundary, every cited NARA code-list page, Columbia's printed page 8, Groningen's printed page 14 and the Marine Corps printed page 314 were visually checked. No authenticated NARA Catalog API request was made.",
            "next_action": f"Review indexed Box {box} for corroborating identifiers, immediate pre-OSS affiliation and last civilian employer before wartime service.",
            "attempt_number": 1,
            "research_agent_version": "before-oss-b1025-v1",
        })
    if len(attempts) != 45:
        raise RuntimeError(f"Expected 45 new research attempts, generated {len(attempts)}")
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-1025-v1",
        "reviewer": "Before OSS Batch 1025 evidence review",
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
