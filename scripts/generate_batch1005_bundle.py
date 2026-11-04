#!/usr/bin/env python3
"""Generate the reviewed Batch 1005 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page495-weichbrodt-to-weisberg-"
    "review_batch-1005_2026-11-03.json"
)

INDEX = "nara-index-b1005"
ARMY = "army-bulk-b1005"
TECH = "army-tech-b1005"
CODES = "army-codes-b1005"
ASU_WEIGEND = "asu-guido-weigend-b1005"
SUMMIT_WEIL = "summit-herald-richard-weil-b1005"
NARA_WEISBERG_SERVICE = "nara-harold-weisberg-service-b1005"
NARA_WEISBERG_HISTORY = "nara-harold-weisberg-history-b1005"

ORG_UCHICAGO = "university-chicago-b1005"
ORG_BAMBERGER = "bamberger-company-b1005"
ORG_MACY = "macy-company-b1005"
ORG_ARMY = "us-army-b1005"
ORG_SELF = "self-employed-b1005"
ORG_CLICK = "click-magazine-b1005"
ORG_SENATE = "senate-civil-liberties-b1005"


PEOPLE = {
    1: ("96380515-34a4-54d4-af42-67d1c36f8f95", "Ray J Weichbrodt"),
    2: ("9a974e19-d4d8-5c62-9ffd-eef3784e8378", "William H Weick"),
    3: ("ee26e0c9-77a6-57d0-8e1c-6b5fa6f2010c", "Edward R Weickel Jr."),
    4: ("dc0d35bf-f811-5d25-8494-35d79874ae66", "Frederick P Weidner"),
    5: ("7a47aa95-93d7-5d35-adfc-e8027664a58d", "Ernest G Weidul"),
    6: ("99a8c9da-698d-5daa-a64b-3b780fd8a59b", "Guido G Weigend"),
    7: ("adcb2aa1-2d70-5fae-9f1b-aa49b37f4567", "Mary E Weikel"),
    8: ("bfbba608-2723-546a-9bf6-fbd7e4f64c12", "Billie A Weil"),
    9: ("d456d2fa-5d89-56a8-9aa0-ef15876c2ea0", "Morris Weil"),
    10: ("cf879662-102b-560d-8c1c-d106412d43ec", "Morris Weil"),
    11: ("a627a7ef-519a-5052-bc41-e799915a1463", "Richard Weil Jr."),
    12: ("d8ad01d0-cf9e-50c5-9184-db58ae03d50d", "Charles H Weilamann Jr."),
    13: ("dc480af6-f4b6-5bf7-b0c8-d132d047d293", "Robert J Weiler"),
    14: ("27184007-d820-53a0-a4c4-1773857b839f", "Otto Weill"),
    15: ("e56df687-2d94-56c2-a934-7e448d5b7637", "Ruth Weiller"),
    16: ("0c21257e-626d-5259-b0bc-e2f0771e49da", "Robert P Weimann"),
    17: ("215294cb-acef-55a3-8c29-8bcf65344475", "Marian E Weimer"),
    18: ("38069ad6-69b5-55af-9be5-751947e67f45", "Albert K Weinberg"),
    19: ("bcbb680f-0b79-5d7f-b1c1-d64110b2fe7b", "Edgar Weinberg"),
    20: ("990bfb96-b0cd-5897-acd9-f4b799b6604b", "Irving Weinberg"),
    21: ("95ea5da4-9589-5f3e-bfd8-add668877113", "Abraham Weiner"),
    22: ("3e4d54bc-f5e0-5681-9494-bb05129eceb6", "Daniel J Weiner"),
    23: ("47cb41f9-98c7-5168-b8a7-fa3978bbd857", "Daniel J Weiner"),
    24: ("1ef133ec-c826-5a17-b9c1-b7b17e5de822", "George Weiner"),
    25: ("200f7993-0eb6-50d9-8bcf-6645ec74fadc", "George Weiner"),
    26: ("82e0b6ac-d40d-5815-8fe3-e4046e26d65a", "Gerald I Weiner"),
    27: ("757ea55f-be27-5da0-b167-ebb5638ae950", "Irving R Weiner"),
    28: ("6a500891-e969-5f82-8795-d873bbcb657b", "Louis L Weiner"),
    29: ("9527f68e-1811-5aa6-bace-aca9f0a83183", "Martin J Weiner"),
    30: ("8eefdaba-3e61-5954-b660-81f3a8645fd5", "Samuel S Weinfeld"),
    31: ("1a500550-8c9f-5a45-9d21-e22a2387ded9", "Robert F Weingartner"),
    32: ("f76ffe3b-f960-583e-872a-2ae345aa0f0b", "Louis Weinman"),
    33: ("b22480d2-e3e4-5b91-94a1-31f9cb0db9b4", "Walter E Weinmann"),
    34: ("90eb1d9b-d9f1-5f23-a785-278f645eacd6", "Marcel I Weinrich"),
    35: ("2216ca28-872d-5b1e-92b0-7f5a623825e7", "Leo Weinstein"),
    36: ("7c899093-f52d-5a67-b610-462e891d463d", "Lionel I Weinstock"),
    37: ("a62731cd-5f4b-5aa1-b67c-16412413ee2e", "Monroe Weinstock"),
    38: ("ad99cb59-4129-596d-b7d2-0f8eb860030b", "Lewis R Weintraub"),
    39: ("73f3649a-d598-5791-bac4-e72405339859", "R E Weinzettel"),
    40: ("a402fdf7-1059-5522-aeb8-4cdde5ec31b7", "Donald E Weir"),
    41: ("cb767798-9c5d-580c-a957-a421c97b3030", "Marjorie Q Weir"),
    42: ("99a0375c-4912-5478-bf66-8bd3e433fa23", "Siegfried H Weir"),
    43: ("4dad4fa3-09da-5d34-bc46-f7e1027d8caf", "Thomas A Weir"),
    44: ("a7105a68-9492-5d7f-89aa-030a3ecdfab7", "George B Weisback"),
    45: ("e57be43b-4812-5e91-8a90-9c73c62b7484", "Walter G Weisbecker"),
    46: ("d0bdcbdd-a1da-5f4c-adea-c5dfde35ed77", "Harold Weisberg"),
}


ARMY_MATCHES = {
    3: {"date": "1943-05-25", "code": "992", "occupation": "student", "label": "students", "locator": "PDF physical page 304; amended historical category 9-92", "identity": "high_confidence", "publish": True},
    12: {"date": "1945-02-13", "code": "476", "occupation": "toolmaker or die sinker and setter", "label": "Toolmakers and die sinkers and setters", "locator": "PDF physical page 173; historical category 4-76", "identity": "confirmed", "publish": True},
    16: {"date": "1946-06-28", "code": "992", "occupation": "student", "label": "students", "locator": "PDF physical page 304; amended historical category 9-92", "identity": "high_confidence", "publish": False},
    21: {"date": "1943-03-26", "code": "592", "occupation": "manufacturing foreman", "label": "Foremen, manufacturing", "locator": "PDF physical page 175; historical category 5-92", "identity": "confirmed", "publish": True},
    22: {"date": "1944-08-25", "code": "992", "occupation": "student", "label": "students", "locator": "PDF physical page 304; amended historical category 9-92", "identity": "high_confidence", "publish": True},
    24: {"date": "1940-11-27", "code": "001", "occupation": "accountant or auditor", "label": "Accountants and auditors", "locator": "PDF physical page 170; historical category 0-01", "identity": "confirmed", "publish": True},
    29: {"date": "1942-09-14", "code": "992", "occupation": "student", "label": "students", "locator": "PDF physical page 304; amended historical category 9-92", "identity": "confirmed", "publish": True},
    30: {"date": "1942-06-16", "code": "134", "occupation": "shipping and receiving clerk", "label": "Shipping and receiving clerks", "locator": "PDF physical page 171; historical category 1-34", "identity": "confirmed", "publish": True},
    31: {"date": "1943-05-20", "code": "022", "occupation": "lawyer or judge", "label": "Lawyers and judges", "locator": "PDF physical page 171; historical category 0-22", "identity": "confirmed", "publish": True},
    32: {"date": "1941-03-19", "code": "525", "occupation": "carpenter", "label": "Carpenters", "locator": "PDF physical page 174; historical category 5-25", "identity": "confirmed", "publish": True},
    35: {"date": "1943-07-24", "code": "992", "occupation": "student", "label": "students", "locator": "PDF physical page 304; amended historical category 9-92", "identity": "confirmed", "publish": True},
    36: {"date": "1943-04-29", "code": "992", "occupation": "student", "label": "students", "locator": "PDF physical page 304; amended historical category 9-92", "identity": "confirmed", "publish": True},
    37: {"date": "1942-12-08", "code": "992", "occupation": "student", "label": "students", "locator": "PDF physical page 304; amended historical category 9-92", "identity": "confirmed", "publish": True},
    38: {"date": "1943-03-09", "code": "002", "occupation": "actor", "label": "Actors and actresses", "locator": "PDF physical page 170; historical category 0-02", "identity": "confirmed", "publish": True},
    40: {"date": "1942-12-15", "code": "048", "occupation": "draftsman", "label": "Draftsmen", "locator": "PDF physical page 171; historical category 0-48", "identity": "confirmed", "publish": True},
    44: {"date": "1945-09-26", "code": "992", "occupation": "student", "label": "students", "locator": "PDF physical page 304; amended historical category 9-92", "identity": "high_confidence", "publish": False},
    45: {"date": "1941-07-22", "code": "006", "occupation": "author, editor, or reporter", "label": "Authors, editors, and reporters", "locator": "PDF physical page 170; historical category 0-06", "identity": "confirmed", "publish": True},
    46: {"date": "1942-12-18", "code": "940", "occupation": "unresolved Army code", "label": "Code 940", "locator": "Official detailed code documentation; code not published as a pre-OSS occupation", "identity": "confirmed", "publish": False},
}

PRINTED_CATEGORY = {
    11: ("commissioned_army_officer", True),
    28: ("commissioned_army_officer", True),
    36: ("enlisted_army_personnel", False),
    39: ("civilian_professional_or_administrative_grade", False),
    43: ("civilian_professional_or_administrative_grade", False),
}

DUPLICATE_GROUPS = {
    9: "name-only:morris-weil-page495",
    10: "name-only:morris-weil-page495",
    22: "name-only:daniel-j-weiner-page495",
    23: "name-only:daniel-j-weiner-page495",
    24: "name-only:george-weiner-page495",
    25: "name-only:george-weiner-page495",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def box_for(row: int) -> str:
    if row <= 2:
        return "822"
    if row <= 36:
        return "823"
    if row == 42:
        return "829"
    return "824"


def unresolved_reason(row: int) -> str:
    base = (
        "Exact-name and meaningful-variant searches across the NARA index context, "
        "CIA Reading Room, Library of Congress, OSS, employment, occupation, obituary, "
        "institutional, newspaper, directory, and archival sources produced no reliable "
        "identity and pre-OSS affiliation bridge; unbridged namesakes were rejected."
    )
    if row in {9, 10}:
        return "Two separately printed Morris Weil rows lack distinguishing identifiers and remain separate. " + base
    if row == 18:
        return "Albert Katz Weinberg academic leads lack a protected identifier, Box 823 reference, or direct OSS-personnel bridge. " + base
    if row == 23:
        return "A second Daniel J. Weiner row lacks a protected identifier and is not merged with the separately printed Army-linked row. " + base
    if row == 28:
        return "The printed Major rank is preserved, but common-name results did not establish a Box 823 or direct OSS-personnel bridge. " + base
    if row == 33:
        return "The Walter E. Weinmann spelling was preserved; results for similar Weinman and Weimann names were rejected. " + base
    if row == 42:
        return "The distinct Box 829 and archival location are preserved, but no reliable identity or employment bridge was found. " + base
    return base


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 822-824 and 829",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 495, rows 1-46",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 46 page-495 rows remain separately recoverable. The page was checked against an original-detail render; full protected identifiers remain private.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; 19 protected-identifier comparisons; identifiers and record ordinals withheld",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "Eighteen identity bridges were accepted and one materially different name remains conflicting. No Army record is treated as a named employer or exact OSS-transfer record.",
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
            "locator": "PDF physical pages 170-175 and 304; reviewed categories 0-01, 0-02, 0-06, 0-22, 0-48, 1-34, 4-76, 5-25, 5-92, and 9-92",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical labels identify broad occupations or student status, not named employers, institutions, workplaces, or exact OSS-transfer dates.",
        },
        {
            "key": ASU_WEIGEND,
            "stable_url": "https://news.asu.edu/20160517-memoriam-guido-g-weigend-asu-geography-professor-and-dean",
            "title": "In memoriam: Guido G. Weigend, ASU geography professor and dean",
            "author_creator": "Malcolm Comeaux and Martin J. Pasqualetti",
            "repository_publisher": "Arizona State University",
            "publication_record_date": "2016-05-17",
            "locator": "Biographical paragraphs on University of Chicago graduation and March 1943-December 1945 Army service in OSS",
            "access_date": "2026-11-03",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "ASU News",
            "rights_notes": "The biography supports student status and Army/OSS chronology; it does not name a civilian employer immediately before service.",
        },
        {
            "key": SUMMIT_WEIL,
            "stable_url": "https://www.digifind-it.com/summit/DATA/newspapers/herald/1943/1943-03-18.pdf",
            "title": "The Summit Herald, Thursday, March 18, 1943",
            "repository_publisher": "The Summit Herald",
            "publication_record_date": "1943-03-18",
            "locator": "PDF page 15, 'President of Bamberger Granted Military Leave'",
            "access_date": "2026-11-03",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Summit Historical Society newspaper archive",
            "rights_notes": "The full page was rendered and visually checked. Public excerpts are limited to the shortest text needed to support the claim.",
        },
        {
            "key": NARA_WEISBERG_SERVICE,
            "stable_url": "https://www.archives.gov/files/research/jfk/releases/104-10336-10010.pdf",
            "archival_identifier": "JFK release 104-10336-10010; OSS Form 1003a",
            "title": "Harold Weisberg OSS Service History",
            "author_creator": "Office of Strategic Services",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1945",
            "locator": "PDF physical page 4, OSS Form 1003a; physical page 15 summary",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "John F. Kennedy Assassination Records Collection",
            "document_number": "104-10336-10010",
            "rights_notes": "The service-history page was locally rendered and visually inspected. Home-address and telephone fields are not reproduced.",
        },
        {
            "key": NARA_WEISBERG_HISTORY,
            "stable_url": "https://www.archives.gov/files/research/rfk/releases/2025/0612/00440177_security_file_weisberg_h_104-10129-10412.pdf",
            "archival_identifier": "Document 104-10305-10002; memorandum dated 1968-01-11",
            "title": "Weisberg Extracts: Subject Harold Weisberg",
            "author_creator": "Central Intelligence Agency, Office of Security",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1968-01-11",
            "locator": "Opening memorandum, employment-history paragraphs",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "Robert F. Kennedy Assassination Records release",
            "document_number": "104-10305-10002",
            "rights_notes": "The memorandum summarizes a December 1946 employment statement. Irrelevant security allegations and sensitive personal details are not reproduced.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {"key": ORG_UCHICAGO, "organization_id": "f2c878b0-ee44-573d-ab30-7e4282bc85e5", "canonical_name": "University of Chicago", "historical_name": "University of Chicago", "aliases": ["The University of Chicago"], "organization_type": "university", "sector": "academia_and_research", "city": "Chicago", "state_or_region": "Illinois", "country": "United States", "normalization_notes": "Reuses the reviewed canonical university; student status is not employment."},
        {"key": ORG_BAMBERGER, "organization_id": "9928549e-0ca7-5864-ae91-58c00195bd1c", "canonical_name": "L. Bamberger & Company", "historical_name": "L. Bamberger & Company", "aliases": ["Bamberger's"], "organization_type": "department store", "sector": "business_and_industry", "city": "Newark", "state_or_region": "New Jersey", "country": "United States", "active_dates": "1892-1986", "normalization_notes": "Preserves the wartime company name; it is not silently replaced by a parent or successor."},
        {"key": ORG_MACY, "organization_id": "478afb16-55ec-5281-8176-c51953a05355", "canonical_name": "R. H. Macy & Company", "historical_name": "Macy's", "aliases": ["Macy's New York"], "organization_type": "department store company", "sector": "business_and_industry", "city": "New York", "state_or_region": "New York", "country": "United States", "normalization_notes": "Preserves the name as printed in the 1943 source and remains separate from L. Bamberger & Company."},
        {"key": ORG_ARMY, "organization_id": "24facf23-e75a-54f2-a37a-0ef1509bc18a", "canonical_name": "United States Army", "historical_name": "U.S. Army", "aliases": ["Army of the United States"], "organization_type": "military_service", "sector": "military", "country": "United States", "normalization_notes": "Reuses the reviewed canonical Army organization; modeled as a military assignment, never a civilian employer."},
        {"key": ORG_SELF, "organization_id": "aa51c76b-2edd-5ca3-a14b-e40ca752af59", "canonical_name": "Self-employed", "historical_name": "Self-employed", "aliases": ["Freelance"], "organization_type": "self-employment", "sector": "self_employed", "normalization_notes": "Person-specific freelance work is not treated as a shared company."},
        {"key": ORG_CLICK, "organization_id": "985711f4-cf24-55c2-a1a7-499fc9cc147c", "canonical_name": "Click magazine", "historical_name": "CLICK magazine", "aliases": ["Click"], "organization_type": "magazine", "sector": "journalism_and_media", "country": "United States", "normalization_notes": "The source says Washington representative while describing freelance work; modeled as a professional affiliation, not silently as employment."},
        {"key": ORG_SENATE, "organization_id": "1df4b3a3-6cfb-537e-801a-7d5590a05f0d", "canonical_name": "U.S. Senate Civil Liberties Committee", "historical_name": "U.S. Senate Subcommittee on Education and Labor", "aliases": ["Senate Civil Liberties Committee", "La Follette Civil Liberties Committee"], "organization_type": "congressional subcommittee", "sector": "federal_government", "city": "Washington", "state_or_region": "District of Columbia", "country": "United States", "active_dates": "1936-1940", "normalization_notes": "Preserves both names used in the official employment-history memorandum."},
    ]


def occupation_key(row: int) -> str:
    return f"{slug(PEOPLE[row][1])}-army-occupation-b1005"


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, item in ARMY_MATCHES.items():
        if not item["publish"]:
            continue
        relationship = "student" if item["code"] == "992" else "unknown"
        values.append({
            "key": occupation_key(row),
            "person_id": PEOPLE[row][0],
            "occupation": item["occupation"],
            "relationship_type": relationship,
            "end_date": item["date"],
            "date_precision": f"Historical civilian-occupation code {item['code']} was recorded at Army entry on {item['date']}; no named employer, workplace, institution, or exact OSS-transfer date is supplied.",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": item["identity"],
            "claim_confidence": "medium",
            "source_quality": "A_direct_official",
            "publication_status": "publish_qualified",
            "research_notes": "Broad historical category only; no named employer, institution, workplace, or OSS transition is inferred.",
        })
    values.extend([
        {"key": "guido-weigend-uchicago-student-b1005", "person_id": PEOPLE[6][0], "organization_key": ORG_UCHICAGO, "organization_name_as_found": "University of Chicago", "role_title": "Student", "occupation": "student", "relationship_type": "student", "end_date": "1942", "date_precision": "Institutional biography says he graduated in 1942 and began Army service in the office of OSS in March 1943; an intervening affiliation is not excluded.", "city": "Chicago", "state_or_region": "Illinois", "country": "United States", "immediate_pre_oss": False, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "high_confidence", "claim_confidence": "high", "source_quality": "B_authoritative_institutional", "publication_status": "published", "research_notes": "Student status is a verified pre-OSS institutional affiliation, not an employer finding."},
        {"key": "richard-weil-bamberger-b1005", "person_id": PEOPLE[11][0], "organization_key": ORG_BAMBERGER, "organization_name_as_found": "L. Bamberger & Company", "role_title": "President", "occupation": "department-store executive", "relationship_type": "employment", "end_date": "1943-03-15", "date_precision": "Contemporary report says the military leave became effective March 15 and that Weil left immediately for OSS duties.", "city": "Newark", "state_or_region": "New Jersey", "country": "United States", "immediate_pre_oss": True, "last_civilian_pre_service": True, "pre_oss_temporal_basis": "explicit_immediate", "identity_confidence": "confirmed", "claim_confidence": "confirmed", "source_quality": "C_reputable_contemporary_or_scholarly", "publication_status": "published", "research_notes": "The employer and transition are explicit in a contemporary newspaper report."},
        {"key": "richard-weil-macy-b1005", "person_id": PEOPLE[11][0], "organization_key": ORG_MACY, "organization_name_as_found": "Macy's", "role_title": "Training Squad member; later administrative roles", "occupation": "department-store executive", "relationship_type": "employment", "start_date": "1928", "date_precision": "The contemporary report dates his Macy's start to 1928 but does not state the end date or exact transfer to Bamberger.", "city": "New York", "state_or_region": "New York", "country": "United States", "immediate_pre_oss": False, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "confirmed", "claim_confidence": "high", "source_quality": "C_reputable_contemporary_or_scholarly", "publication_status": "published", "research_notes": "Earlier employment is kept separate from the explicit immediate Bamberger affiliation."},
        {"key": "harold-weisberg-army-b1005", "person_id": PEOPLE[46][0], "organization_key": ORG_ARMY, "organization_name_as_found": "U.S. Army", "role_title": "Corporal at discharge", "relationship_type": "military_assignment", "start_date": "1942", "end_date": "1944-11", "date_precision": "The official history says he entered the Army in 1942, was discharged in November 1944, and began OSS civilian service in January 1945.", "country": "United States", "immediate_pre_oss": True, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "strongly_date_bounded", "identity_confidence": "confirmed", "claim_confidence": "high", "source_quality": "A_direct_official", "publication_status": "published", "research_notes": "Modeled as the immediate military pathway; it is not a civilian employer."},
        {"key": "harold-weisberg-freelance-b1005", "person_id": PEOPLE[46][0], "organization_key": ORG_SELF, "organization_name_as_found": "free lance writer", "role_title": "Freelance writer", "occupation": "journalist and writer", "relationship_type": "self_employment", "start_date": "1939", "end_date": "1942", "date_precision": "The official employment-history memorandum dates freelance writing from 1939 to 1942, immediately before Army entry.", "country": "United States", "immediate_pre_oss": False, "last_civilian_pre_service": True, "pre_oss_temporal_basis": "strongly_date_bounded", "identity_confidence": "confirmed", "claim_confidence": "high", "source_quality": "A_direct_official", "publication_status": "published", "research_notes": "Self-employment is supported; Click magazine is modeled separately as a professional affiliation."},
        {"key": "harold-weisberg-click-b1005", "person_id": PEOPLE[46][0], "organization_key": ORG_CLICK, "organization_name_as_found": "CLICK magazine", "role_title": "Washington representative", "occupation": "journalist and writer", "relationship_type": "professional_affiliation", "start_date": "1939", "end_date": "1942", "date_precision": "The memorandum places the Click representative role within the 1939-1942 freelance-writing period.", "city": "Washington", "state_or_region": "District of Columbia", "country": "United States", "immediate_pre_oss": False, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "confirmed", "claim_confidence": "high", "source_quality": "A_direct_official", "publication_status": "published", "research_notes": "Professional affiliation is not silently converted into salaried employment."},
        {"key": "harold-weisberg-senate-b1005", "person_id": PEOPLE[46][0], "organization_key": ORG_SENATE, "organization_name_as_found": "U.S. Senate Subcommittee on Education and Labor", "role_title": "Editor, investigator, and assistant secretary", "relationship_type": "employment", "start_date": "1936", "end_date": "1939", "date_precision": "The official memorandum supplies the 1936-1939 dates and says the work ended because the assignment terminated.", "city": "Washington", "state_or_region": "District of Columbia", "country": "United States", "immediate_pre_oss": False, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "confirmed", "claim_confidence": "high", "source_quality": "A_direct_official", "publication_status": "published", "research_notes": "Earlier federal employment is distinct from the later freelance period and Army pathway."},
    ])
    return values


def make_claim(*, key: str, row: int, claim_type: str, text: str, paraphrase: str, identity: str, temporal: str, quality: str, confidence: str, publication: str, notes: str, source_links: list[dict[str, str]], affiliation_key: str | None = None) -> dict[str, object]:
    value: dict[str, object] = {"key": key, "person_id": PEOPLE[row][0], "claim_type": claim_type, "claim_text": text, "evidence_paraphrase": paraphrase, "identity_match_assessment": identity, "temporal_assessment": temporal, "source_quality": quality, "claim_confidence": confidence, "publication_status": publication, "match_notes": notes, "sources": source_links}
    if affiliation_key:
        value["affiliation_key"] = affiliation_key
    return value


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, item in ARMY_MATCHES.items():
        name = PEOPLE[row][1]
        identity_text = "The exact indexed and Army names agree, and a nonshared protected identifier connects the records."
        if row == 3:
            identity_text = "The nonshared protected identifier, surname, given name and suffix agree; the Army record omits the indexed middle initial R."
        elif row == 16:
            identity_text = "The nonshared protected identifier, surname, given name and middle initial agree; the Army record adds Jr."
        elif row == 22:
            identity_text = "The nonshared protected identifier and given name Daniel J agree; the Army surname field is visibly damaged as EI ER."
        elif row == 44:
            identity_text = "The nonshared protected identifier and full name are compatible despite the Army record's transposed given name and WEISBECK spelling."
        elif row == 46:
            identity_text = "The nonshared protected identifier and given name Harold align despite a limited Army surname corruption; an official OSS service-history form independently confirms Harold Weisberg."
        links = [
            {"source_key": INDEX, "locator_override": f"PDF page 495 row {row}; protected identifier withheld"},
            {"source_key": ARMY, "locator_override": "Accepted reviewed identity bridge; protected identifier withheld"},
        ]
        if row == 46:
            links.append({"source_key": NARA_WEISBERG_SERVICE, "locator_override": "PDF physical page 4, OSS Form 1003a", "excerpt_override": "Weisberg, Harold"})
        values.append(make_claim(
            key=f"identity-{slug(name)}-row{row}-b1005",
            row=row,
            claim_type="identity",
            text=f"Indexed {name} is {('confirmed' if item['identity'] == 'confirmed' else 'a high-confidence match')} to the reviewed official Army entry record.",
            paraphrase=identity_text,
            identity=("Confirmed by official sources and a nonshared protected-identifier agreement; the identifier remains private." if item["identity"] == "confirmed" else "High confidence from a nonshared protected identifier plus compatible name fields; the limited discrepancy remains visible."),
            temporal=f"The Army record dates entry to {item['date']}.",
            quality="A_direct_official",
            confidence=("confirmed" if item["identity"] == "confirmed" else "high"),
            publication="published",
            notes="Identity only; no named employer, workplace, institution, or exact OSS-transfer date is inferred from the Army record.",
            source_links=links,
        ))
        if item["publish"]:
            values.append(make_claim(
                key=f"occupation-{slug(name)}-row{row}-b1005",
                row=row,
                claim_type="occupation",
                text=f"At Army entry on {item['date']}, {name} was recorded in the historical {item['occupation']} category; no named employer or institution is identified.",
                paraphrase=f"The accepted Army record carries civilian-occupation code {item['code']}, decoded from NARA's official code list.",
                identity="The category belongs only to the accepted protected-identifier match; the identifier itself is not public.",
                temporal="Strongly date-bounded to Army entry; it does not establish the immediate pre-OSS affiliation or a named employer, workplace, or institution.",
                quality="A_direct_official",
                confidence="medium",
                publication="publish_qualified",
                notes="Published with its limits and excluded from verified-employer analytics.",
                source_links=[
                    {"source_key": ARMY, "locator_override": f"Army entry {item['date']}; civilian occupation code {item['code']}; protected identifier withheld"},
                    {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46"},
                    {"source_key": CODES, "locator_override": item["locator"], "excerpt_override": item["label"]},
                ],
                affiliation_key=occupation_key(row),
            ))

    values.extend([
        make_claim(key="identity-guido-weigend-b1005", row=6, claim_type="identity", text="The indexed Guido G. Weigend is a high-confidence match to the Arizona State University biography of the University of Chicago graduate who served in the Army office of OSS.", paraphrase="The uncommon full name, 1942 Chicago graduation, March 1943 Army/OSS start, and indexed wartime identifier align.", identity="High confidence from a distinctive full name, compatible chronology, direct institutional OSS statement, and indexed Army identifier; the personnel file remains the final bridge.", temporal="The biography dates University of Chicago graduation to 1942 and Army service in OSS from March 1943 through December 1945.", quality="B_authoritative_institutional", confidence="high", publication="published", notes="No civilian employer immediately before service is inferred.", source_links=[{"source_key": INDEX, "locator_override": "PDF page 495 row 6; protected identifier withheld"}, {"source_key": ASU_WEIGEND, "locator_override": "Biographical paragraphs on education and Army/OSS service", "excerpt_override": "enrolling at the University of Chicago, graduating in 1942"}]),
        make_claim(key="preoss-guido-weigend-chicago-b1005", row=6, claim_type="other_pre_oss_affiliation", text="Guido G. Weigend graduated from the University of Chicago in 1942 before beginning Army service in the office of OSS in March 1943.", paraphrase="Arizona State University's institutional biography supplies both dates and distinguishes education from employment.", identity="High-confidence distinctive-name and chronology match to the indexed person.", temporal="Documented pre-OSS student affiliation; the source does not exclude an intervening affiliation or name a civilian employer.", quality="B_authoritative_institutional", confidence="high", publication="published", notes="University attendance is not classified as employment or as the last civilian employer.", source_links=[{"source_key": ASU_WEIGEND, "locator_override": "Biographical paragraphs on education and Army/OSS service", "excerpt_override": "graduating in 1942"}], affiliation_key="guido-weigend-uchicago-student-b1005"),
        make_claim(key="identity-richard-weil-b1005", row=11, claim_type="identity", text="The indexed Lieutenant Colonel Richard Weil Jr. is confirmed as the L. Bamberger & Company president who entered OSS as an Army captain in March 1943.", paraphrase="A contemporary report names Richard Weil Jr., his company presidency, Army captain's commission, and immediate departure for OSS; the later indexed rank is compatible.", identity="Confirmed by the exact uncommon name and suffix, company role, Army/OSS transition, and compatible officer progression to the indexed lieutenant-colonel rank.", temporal="The military leave became effective March 15, 1943, and the report says he left immediately for OSS duties.", quality="C_reputable_contemporary_or_scholarly", confidence="confirmed", publication="published", notes="The contemporary article was visually checked on the full newspaper page.", source_links=[{"source_key": INDEX, "locator_override": "PDF page 495 row 11; protected officer identifier withheld"}, {"source_key": SUMMIT_WEIL, "locator_override": "PDF page 15, 'President of Bamberger Granted Military Leave'", "excerpt_override": "commissioned as Captain in the U.S. Army, office of Strategic Services"}]),
        make_claim(key="immediate-richard-weil-bamberger-b1005", row=11, claim_type="immediate_pre_oss_affiliation", text="Richard Weil Jr.'s immediate pre-OSS employer was L. Bamberger & Company in Newark, where he was president.", paraphrase="The contemporary newspaper says Bamberger granted its president military leave effective March 15, 1943, and that he left immediately for OSS duties.", identity="Confirmed by the exact name, suffix, officer chronology, and direct OSS statement.", temporal="Explicit immediate transition from the employer to OSS.", quality="C_reputable_contemporary_or_scholarly", confidence="confirmed", publication="published", notes="Also qualifies as the last civilian employer before wartime service.", source_links=[{"source_key": SUMMIT_WEIL, "locator_override": "PDF page 15", "excerpt_override": "Richard Weil, Jr., president was granted a military leave of absence"}], affiliation_key="richard-weil-bamberger-b1005"),
        make_claim(key="last-civilian-richard-weil-bamberger-b1005", row=11, claim_type="last_civilian_pre_service", text="L. Bamberger & Company was Richard Weil Jr.'s last documented civilian employer before Army and OSS service.", paraphrase="The same contemporary report identifies the company, his presidency, the effective leave date, and his immediate OSS departure.", identity="Confirmed exact-person match.", temporal="Explicitly date-bounded to March 15, 1943, immediately before OSS duties.", quality="C_reputable_contemporary_or_scholarly", confidence="confirmed", publication="published", notes="Kept separate from his earlier Macy's employment.", source_links=[{"source_key": SUMMIT_WEIL, "locator_override": "PDF page 15", "excerpt_override": "This leave became effective March 15 and continues for the duration."}], affiliation_key="richard-weil-bamberger-b1005"),
        make_claim(key="earlier-richard-weil-macy-b1005", row=11, claim_type="other_pre_oss_affiliation", text="Richard Weil Jr. joined Macy's training squad in 1928 and later held administrative roles there.", paraphrase="The contemporary report describes this earlier department-store career but does not give the date he moved to Bamberger.", identity="Confirmed by the same exact-person contemporary article.", temporal="Documented prewar employment; not the immediate pre-OSS employer.", quality="C_reputable_contemporary_or_scholarly", confidence="high", publication="published", notes="Modeled separately from L. Bamberger & Company and excluded from immediate-employer counts.", source_links=[{"source_key": SUMMIT_WEIL, "locator_override": "PDF page 15", "excerpt_override": "In 1928 he joined Macy's on the Training Squad"}], affiliation_key="richard-weil-macy-b1005"),
        make_claim(key="conflict-george-weiner-row25-b1005", row=25, claim_type="identity", text="The protected identifier on the second page-495 George Weiner row resolves to an official Army record under the materially different name Funk Yoward C.", paraphrase="The visually checked index and official Army bulk file conflict; the two George Weiner rows remain separate.", identity="Conflicting; no identity, occupation, or employer evidence is transferred from the Army candidate.", temporal="The Army entry date does not resolve the name conflict.", quality="A_direct_official", confidence="conflicting", publication="conflicting", notes="Box 823 must be reviewed before any merge or attribution.", source_links=[{"source_key": INDEX, "locator_override": "PDF page 495 row 25; protected identifier withheld"}, {"source_key": ARMY, "locator_override": "Conflicting candidate; protected identifier and record ordinal withheld"}]),
        make_claim(key="immediate-harold-weisberg-army-b1005", row=46, claim_type="immediate_pre_oss_affiliation", text="Harold Weisberg's best-supported immediate pre-OSS affiliation was the U.S. Army, from which he was discharged in November 1944 before beginning OSS civilian service in January 1945.", paraphrase="Official NARA records date Army service from 1942 to November 1944 and OSS appointment from January 15, 1945.", identity="Confirmed by the indexed protected identifier plus official OSS service-history records.", temporal="Strongly date-bounded military pathway with a short documented interval; no intervening employer is identified.", quality="A_direct_official", confidence="high", publication="published", notes="Military assignment is not a civilian employer.", source_links=[{"source_key": NARA_WEISBERG_HISTORY, "locator_override": "Opening memorandum, employment-history paragraphs", "excerpt_override": "In 1942 Subject entered the Army"}, {"source_key": NARA_WEISBERG_SERVICE, "locator_override": "PDF physical page 4", "excerpt_override": "1/15/45"}], affiliation_key="harold-weisberg-army-b1005"),
        make_claim(key="last-civilian-harold-weisberg-freelance-b1005", row=46, claim_type="last_civilian_pre_service", text="Harold Weisberg's last documented civilian work before Army service was self-employed freelance writing from 1939 to 1942.", paraphrase="An official employment-history memorandum records freelance writing, including work as Click magazine's Washington representative, immediately before Army entry.", identity="Confirmed by the protected Army bridge and exact official OSS service history.", temporal="Strongly date-bounded as the last documented civilian work before Army service.", quality="A_direct_official", confidence="high", publication="published", notes="Click magazine is modeled as a professional affiliation because the source describes him as freelance.", source_links=[{"source_key": NARA_WEISBERG_HISTORY, "locator_override": "Opening memorandum, employment-history paragraphs", "excerpt_override": "From 1939 to 1942 he worked as a free lance writer"}], affiliation_key="harold-weisberg-freelance-b1005"),
        make_claim(key="preoss-harold-weisberg-click-b1005", row=46, claim_type="other_pre_oss_affiliation", text="During his 1939-1942 freelance period, Harold Weisberg was Click magazine's Washington representative.", paraphrase="The official employment-history memorandum places this representative role within freelance work.", identity="Confirmed exact-person official record.", temporal="Documented before Army and OSS service; not classified as salaried employment.", quality="A_direct_official", confidence="high", publication="published", notes="Professional affiliation only and excluded from employer analytics.", source_links=[{"source_key": NARA_WEISBERG_HISTORY, "locator_override": "Opening memorandum, employment-history paragraphs", "excerpt_override": "Washington representative with CLICK magazine"}], affiliation_key="harold-weisberg-click-b1005"),
        make_claim(key="preoss-harold-weisberg-senate-b1005", row=46, claim_type="other_pre_oss_affiliation", text="Harold Weisberg worked for the U.S. Senate Subcommittee on Education and Labor from 1936 to 1939 as an editor, investigator, and assistant secretary.", paraphrase="The official employment-history memorandum supplies the organization, roles, dates, and reason the work ended.", identity="Confirmed exact-person official record.", temporal="Earlier documented prewar employment, preceding the freelance period.", quality="A_direct_official", confidence="high", publication="published", notes="Not the immediate pre-OSS affiliation or last civilian work before Army service.", source_links=[{"source_key": NARA_WEISBERG_HISTORY, "locator_override": "Opening memorandum, employment-history paragraphs", "excerpt_override": "from 1936 to 1939 as an editor, investigator and Asst. Secretary"}], affiliation_key="harold-weisberg-senate-b1005"),
    ])
    return values


def base_update(row: int, **overrides: object) -> dict[str, object]:
    value: dict[str, object] = {"person_id": PEOPLE[row][0], "manual_review_required": True, "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "high"}
    if row in PRINTED_CATEGORY:
        value["personnel_category"], value["commissioned_officer"] = PRINTED_CATEGORY[row]
    if row in DUPLICATE_GROUPS:
        value["possible_duplicate_group"] = DUPLICATE_GROUPS[row]
    value.update(overrides)
    return value


def person_updates() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    special = set(ARMY_MATCHES) | {6, 11, 25}
    for row in sorted(set(PEOPLE) - special):
        reason = unresolved_reason(row)
        values.append(base_update(row, identity_status="unresolved", identity_evidence=f"The visually verified page 495 source preserves {PEOPLE[row][1]}, its printed rank or notation, archival box, and location. {reason}", research_status="requires_archival_review", next_action=f"Review the indexed Box {box_for(row)} personnel file for corroborating identifiers, the immediate pre-OSS affiliation, and the last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}"))
    for row, item in ARMY_MATCHES.items():
        if row == 46:
            continue
        if row in {16, 44}:
            values.append(base_update(row, identity_status=item["identity"], identity_evidence="A nonshared protected identifier and compatible name fields support the reviewed Army identity bridge, but the Army-entry date postdates the OSS period.", personnel_category="enlisted_army_personnel", commissioned_officer=False, research_status="requires_archival_review", next_action=f"Review the indexed Box {box_for(row)} personnel file for pre-OSS history; the {item['date']} Army record cannot establish a pre-OSS occupation.", nara_catalog_id="1263923"))
        else:
            values.append(base_update(row, identity_status=item["identity"], identity_evidence="A nonshared protected identifier and reviewed compatible name fields connect the index row to the official Army record.", personnel_category="enlisted_army_personnel", commissioned_officer=False, research_status="occupation_only_found", next_action=f"Review the indexed Box {box_for(row)} personnel file to identify any named employer or institution behind the broad {item['occupation']} category and establish the Army-to-OSS chronology.", nara_catalog_id="1263923"))
    values.extend([
        base_update(6, identity_status="high_confidence", identity_evidence="The uncommon full name, indexed Army identifier, 1942 University of Chicago graduation, and Arizona State University biography placing him in Army service with OSS from March 1943 align.", personnel_category="enlisted_army_personnel", commissioned_officer=False, research_status="completed", archival_review_priority="medium", next_action="Review the indexed Box 823 personnel file for an exact Army/OSS assignment date and any intervening civilian employer after University of Chicago graduation."),
        base_update(11, identity_status="confirmed", identity_evidence="A contemporary newspaper names Richard Weil Jr., his L. Bamberger presidency, his Army captain's commission, and his immediate OSS departure; the later lieutenant-colonel rank matches the index.", personnel_category="commissioned_army_officer", commissioned_officer=True, research_status="verified_employer_found", archival_review_priority="medium", next_action="Review the indexed Box 823 personnel file for exact OSS assignments and the date of transition from Macy's to L. Bamberger & Company."),
        base_update(25, identity_status="conflicting", identity_evidence="The printed protected identifier resolves to an official Army record under the materially different name Funk Yoward C. The separate page-495 George Weiner entities are not merged.", possible_duplicate_group=DUPLICATE_GROUPS[25], research_status="conflicting_sources", archival_review_priority="critical", next_action="Review the Box 823 personnel file and compare both page-495 George Weiner rows before attributing identity, occupation, or employer evidence."),
        base_update(46, identity_status="confirmed", identity_evidence="The protected Army bridge and official NARA OSS service-history form confirm Harold Weisberg despite a limited surname corruption in the Army bulk record.", name_variants=["Harold Weisserg"], personnel_category="enlisted_army_personnel", commissioned_officer=False, research_status="verified_employer_found", archival_review_priority="medium", next_action="Review the indexed Box 824 personnel file for the exact Army-to-OSS transition and original December 1946 employment statement; code 940 remains unpublished as occupation evidence.", nara_catalog_id="1263923"),
    ])
    if len(values) != len(PEOPLE):
        raise RuntimeError(f"Expected {len(PEOPLE)} person updates, generated {len(values)}")
    return values


def research_attempts() -> list[dict[str, object]]:
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        if row == 11:
            outcome, reviewed, rejected = "source_reviewed", 11, 6
            note = "A visually checked contemporary newspaper explicitly identifies L. Bamberger & Company as the employer Richard Weil Jr. left for OSS and documents earlier Macy's work."
        elif row == 46:
            outcome, reviewed, rejected = "source_reviewed", 14, 6
            note = "Official NARA Army and OSS records distinguish Weisberg's immediate Army pathway, last civilian freelance work, Click affiliation, and earlier Senate employment."
        elif row == 6:
            outcome, reviewed, rejected = "source_reviewed", 10, 6
            note = "Arizona State University's institutional biography supports a high-confidence identity and documented University of Chicago student affiliation before Army/OSS service; no civilian employer is named."
        elif row == 25:
            outcome, reviewed, rejected = "candidate_found", 8, 6
            note = "The protected identifier points to an unrelated Army name. The conflict is preserved and no Army-coded field is transferred."
        elif row in ARMY_MATCHES:
            item = ARMY_MATCHES[row]
            outcome, reviewed, rejected = "source_reviewed", 9, 5
            note = (f"A reviewed protected-identifier Army bridge supports identity and a qualified {item['occupation']} category at Army entry; no named employer, institution, workplace, or OSS-transfer date is supplied." if item["publish"] else f"A reviewed protected-identifier Army bridge supports identity, but the {item['date']} Army entry postdates the OSS period and supplies no pre-OSS occupation.")
        else:
            outcome, reviewed, rejected = "candidate_rejected", 7, 6
            note = unresolved_reason(row)
        attempts.append({
            "key": f"page495-row{row}-{slug(name)}-b1005",
            "person_id": person_id,
            "source_adapter": "manual_staged_protocol",
            "query_text": f"{name}; NARA OSS index context; CIA Reading Room, National Archives, and Library of Congress exact-name domain checks; exact-name and meaningful spelling, initial, suffix, punctuation, transliteration, and OCR variants; OSS, rank, branch, assignment, and identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory, and archival searches; indexed Box {box_for(row)}; protected identifiers used only in private official-record comparison",
            "query_variant_type": "staged_identity_employment_archival_protocol_batch_1005",
            "started_at": "2026-11-03T23:05:00Z",
            "completed_at": "2026-11-04T00:15:00Z",
            "outcome": outcome,
            "sources_reviewed": reviewed,
            "candidate_sources_rejected": rejected,
            "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, postwar-only leads, discovery-only biographies, and sources without an OSS, protected-identifier, rank, unit, or personnel-file bridge were rejected. Historical Army categories were not converted into named employers, workplaces, or institutions. Student status was not converted into employment, and post-OSS Army-entry records were not used as pre-OSS occupation evidence.",
            "research_notes": f"{note} Exact-name official-domain, OSS, employer, occupation, obituary, biography, institutional, newspaper, directory, and archival searches were checked as applicable. NARA index page 495 was rendered and visually checked. Official Army bulk data and code documentation, the Richard Weil newspaper page, and Harold Weisberg's service-history form were visually inspected. No authenticated NARA Catalog API call was made.",
            "next_action": f"Review the indexed Box {box_for(row)} personnel file for corroborating identifiers, the immediate pre-OSS affiliation, and the last civilian employer before wartime service.",
            "attempt_number": 1,
            "research_agent_version": "before-oss-b1005-v1",
        })
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-1005-v1",
        "reviewer": "Before OSS Batch 1005 evidence review",
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
