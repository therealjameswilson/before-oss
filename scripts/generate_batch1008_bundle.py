#!/usr/bin/env python3
"""Generate the reviewed Batch 1008 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page498-werner-to-weston-"
    "review_batch-1008_2026-11-03.json"
)

INDEX = "nara-index-b1008"
ARMY = "army-bulk-b1008"
TECH = "army-tech-b1008"
CODES = "army-codes-b1008"
AKRON = "akron-directory-b1008"
WAPO = "washington-post-wertime-b1008"
GREECE = "oss-greece-west-b1008"
GAZETTE = "london-gazette-westmacott-b1008"
AMEDD = "army-history-weston-b1008"
OSSOG = "oss-operational-groups-westgard-b1008"

ORG_FIRESTONE = "firestone-b1008"
ORG_GRENADIER_GUARDS = "grenadier-guards-b1008"
WECHSBERG_ID = "f50fca9a-eeec-5f59-afcf-f2b2970a04b2"


PEOPLE = {
    1: ("06eb2019-df98-55f3-aa79-2ec688eab677", "Marjorie J Werner"),
    2: ("b5fef31b-68d9-5199-af8f-1ece8d6a0f5b", "Naomi R Werner"),
    3: ("fbb08b7b-d19b-5400-9e4f-03f08ede11d5", "Neale L Werner"),
    4: ("25dfc434-480e-5828-a485-a25b303984fa", "Joseph Wernersbach"),
    5: ("2fc3b6d4-ca0d-5cbb-a150-dcc31255fd67", "Doris M Werntz"),
    6: ("d82b4b8c-1f51-5901-bd59-abcbf59772f1", "Harold J Wersinger"),
    7: ("2cfb89ab-e239-5461-9fa9-9fe35fa58836", "Jean B Wertheimer"),
    8: ("84898965-8e48-52a4-a528-1b7b74b2d676", "Sidney S Wertheimer"),
    9: ("5eedf409-6844-5209-a463-3f7f24836574", "Theodore A Wertime"),
    10: ("d100f26a-d14b-5e39-83a2-6fd17154f02a", "Louis M Wertley"),
    11: ("7de3fdd4-3c90-5e28-81c5-4a92a13ff3aa", "Roland E Weschler"),
    12: ("187e527d-e0cc-54a5-85d6-c503905ed584", "Frank A Wesley Jr."),
    13: ("a59e997b-0f4f-5378-98ca-648e324c2369", "Harry N Wessel Jr."),
    14: ("96ae5806-fdb9-5cf9-a63c-bfba23349722", "Arthur H West"),
    15: ("5bf2b9ee-8cf1-5500-80cf-9c3d6f018d0d", "Carlin J West"),
    16: ("90da1136-c456-5f1f-9d02-9c1078a03a7d", "David E West"),
    17: ("5b4795c9-4006-5d02-944d-e0783803feab", "Edythe M West"),
    18: ("494eb3fc-5608-56f4-bcea-d248f7d0bb2e", "Eleanor West"),
    19: ("1f3d2471-f0b0-5cc6-8b57-7e6db06f0841", "Jane V West"),
    20: ("0925e9ca-9c59-5e23-8fa3-a2f319db53d8", "Joe R West"),
    21: ("435d0e64-ffb0-50a0-9092-7e5419c40968", "Lee E West"),
    22: ("856cfba7-fca0-5e24-a272-57c38ed15423", "Marjorie West"),
    23: ("4bf3fa80-e205-511d-9e23-8ae140993a81", "Mary E West"),
    24: ("9766cd11-b267-5d63-93f5-ba648aeb1396", "Max E West"),
    25: ("4d549971-32b4-5f39-9b80-9748d59a9613", "Owen A West"),
    26: ("b5ae9703-e77e-545b-aaa3-38c7f16b9eeb", "Paul West"),
    27: ("73d2675c-996f-5eae-96c5-f5e081ecfcd7", "Robert C West"),
    28: ("e95606dd-9394-51b4-bf17-e25ee9a01c73", "Robert C West"),
    29: ("5e382a0f-0115-5b66-8dcb-2270cedd78c2", "Thomas M West"),
    30: ("46722351-0394-5a6e-92fd-97f60c1a6ee1", "William West"),
    31: ("b31a55fc-175a-52c1-9606-77161626f526", "Richard M Westberry"),
    32: ("4f0c7e11-dc4c-5127-8690-9b0730267753", "Edwin P Westbrook"),
    33: ("38e97fef-f6c7-52bc-bbb1-cb64a2cae5a7", "Alwood I Westerdahl"),
    34: ("5b2245c4-c5e7-5c28-8741-07493c31eba9", "Beatrice H Westerlind"),
    35: ("164f6285-fe64-5b94-9d7e-8c76ef4c46a2", "Raymond J Western"),
    36: ("06de1f97-0890-5c94-9fc9-ff6b374c9b94", "Tipton M Westfall"),
    37: ("6cbe576e-2e56-5ac3-acbd-321b488b1201", "Wallace D Westfall"),
    38: ("e3f52756-4d35-5387-a8f3-08a015d88f88", "Arthur J Westgard"),
    39: ("146c2e04-0774-51b4-abef-736949c59f2c", "F K Westlake"),
    40: ("35befa3e-bc07-553f-ad1f-b1e375f6f44f", "Margaret A Westlake"),
    41: ("fc9f7331-4067-55f8-ab58-f9f3ac4f96e3", "Guy Westmacott"),
    42: ("eb846920-1abd-5562-85cc-db31dca30df2", "Cecil R Weston"),
    43: ("2fc54647-b18e-5c77-943d-0acd3f117498", "Joseph H Weston"),
    44: ("40729d31-4e16-578b-98f9-ec82a0e38b30", "Logan E Weston"),
    45: ("dc5a290b-412d-5503-bdc1-7b24532d8d58", "Oscar C Weston"),
    46: ("b2d63e4c-a599-50df-af87-6865b7b1d247", "T B Weston"),
}


ARMY_MATCHES = {
    3: {"date": "1943-09-06", "code": "992", "occupation": "student", "label": "Students", "locator": "PDF physical page 304; amended historical category 9-92"},
    4: {"date": "1943-02-06", "code": "134", "occupation": "shipping and receiving clerk", "label": "Shipping and receiving clerks", "locator": "PDF physical page 171; historical category 1-34"},
    8: {"date": "1943-02-27", "code": "935", "occupation": "routeman", "label": "Routemen", "locator": "PDF physical page 174; historical category 9-35"},
    9: {"date": "1944-10-23", "code": "039", "occupation": "professional occupation, not elsewhere classified", "label": "Professional occupations, n.e.c.", "locator": "PDF physical page 171; historical category 0-39"},
    13: {"date": "1943-02-23", "code": "992", "occupation": "student", "label": "Students", "locator": "PDF physical page 304; amended historical category 9-92"},
    15: {"date": "1943-04-03", "code": "878", "occupation": "machine-shop and related occupation, not elsewhere classified", "label": "Machine shop and related occupations, n.e.c.", "locator": "PDF physical page 174; historical category 8-78"},
    16: {"date": "1943-03-19", "code": "992", "occupation": "student", "label": "Students", "locator": "PDF physical page 304; amended historical category 9-92"},
    24: {"date": "1942-05-13", "code": "266", "occupation": "police officer or detective, public service", "label": "Policemen and detectives, public service", "locator": "PDF physical page 172; historical category 2-66"},
    31: {"date": "1943-01-14", "code": "103", "occupation": "checker", "label": "Checkers", "locator": "PDF physical page 171; historical category 1-03"},
    32: {"date": "1943-03-02", "code": "002", "occupation": "actor or actress", "label": "Actors and actresses", "locator": "PDF physical page 170; historical category 0-02"},
    33: {"date": "1942-10-22", "code": "783", "occupation": "mechanic or repairman, not elsewhere classified", "label": "Mechanics and repairmen, n.e.c.", "locator": "PDF physical page 175; historical category 7-83"},
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def box_for(row: int) -> str:
    return "827" if row <= 25 else "828"


def occupation_key(row: int) -> str:
    return f"{slug(PEOPLE[row][1])}-army-occupation-row{row}-b1008"


def unresolved_reason(row: int) -> str:
    base = (
        "Exact-name and meaningful-variant searches across the NARA index context, CIA Reading Room, "
        "Library of Congress, OSS, employment, occupation, obituary, institutional, newspaper, "
        "directory, and archival sources produced no reliable identity and pre-OSS affiliation bridge; "
        "unbridged namesakes were rejected."
    )
    special = {
        17: "A 1939-1940 Iowa educational-directory result for an Edythe M. West lacks an OSS or Box 827 bridge and was rejected. ",
        22: "An Arlington Hall and OSS biography for a Marjorie West lacks a distinguishing identifier for this common-name row and was rejected. ",
        27: "This separately printed Robert C. West row is not merged with identical row 28 without distinguishing evidence. ",
        28: "This separately printed Robert C. West row is not merged with identical row 27 without distinguishing evidence. ",
        36: "Discovery-only records identify different men named Tipton M. Westfall and cannot be assigned to this row. ",
    }
    return special.get(row, "") + base


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 827-828",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 498, rows 1-46",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 46 printed rows remain separately preserved; full protected identifiers remain private.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; 11 accepted protected-identifier comparisons; identifiers and record ordinals withheld",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "Eleven exact-name identity bridges were accepted. No Army record is treated as a named employer, institution, or exact OSS-transfer record.",
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
            "locator": "PDF physical pages 170-175 and 304; reviewed historical civilian-occupation categories",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical labels identify broad occupations or student status, not named employers, institutions, workplaces, or exact OSS-transfer dates.",
        },
        {
            "key": AKRON,
            "stable_url": "https://www.akronlibrary.org/images/SpecCol/akroncitydir1941-2.pdf",
            "title": "Akron 1941 City Directory",
            "author_creator": "Burch Directory Company",
            "repository_publisher": "Akron-Summit County Public Library",
            "publication_record_date": "1941",
            "locator": "PDF physical page 417; Barberton directory printed page 1617",
            "access_date": "2026-11-03",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Akron city directories",
            "rights_notes": "The original page was rendered and visually inspected. The abbreviated employer name is preserved and not silently expanded.",
        },
        {
            "key": WAPO,
            "stable_url": "https://www.washingtonpost.com/archive/local/1982/04/16/theodore-wertime/ece2bb7e-6993-49d1-bc3d-38e936e67e18/",
            "title": "Theodore Wertime",
            "repository_publisher": "The Washington Post",
            "publication_record_date": "1982-04-15",
            "locator": "Obituary; wartime-service paragraph",
            "access_date": "2026-11-03",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "rights_notes": "Used to bridge the exact full name to OSS service; it does not supply a pre-OSS employer.",
        },
        {
            "key": GREECE,
            "stable_url": "https://www.elia.org.gr/userfiles/pdf_archieve/1944%2011-1744%20OSS%20Missions%2C%20SOE%2C%20Georgiades%2C%20Pericles%2C%20Helios%20%5B25%20pgs%5D%20226-210-WN15277%20%28Admin%29.pdf",
            "archival_identifier": "RG 226; 226-210-WN15277 (Admin)",
            "title": "Strategic Services Operations report concerning Greece",
            "author_creator": "Office of Strategic Services",
            "repository_publisher": "National Archives reproduction hosted by Hellenic Literary and Historical Archive (ELIA)",
            "publication_record_date": "1944-10-15",
            "locator": "PDF physical page 15",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "The original page was rendered and visually inspected. It documents wartime identity and assignment context, not pre-OSS employment.",
        },
        {
            "key": GAZETTE,
            "stable_url": "https://www.thegazette.co.uk/London/issue/37961/supplement/2287/data.pdf",
            "archival_identifier": "London Gazette issue 37961, supplement page 2287",
            "title": "The London Gazette, Supplement",
            "author_creator": "The War Office",
            "repository_publisher": "The London Gazette",
            "publication_record_date": "1947-05-23",
            "locator": "Supplement page 2287; Legion of Merit list",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "rights_notes": "The original page was rendered and visually inspected. The postwar notice confirms the full name, temporary lieutenant-colonel rank, and Grenadier Guards affiliation but not OSS-entry chronology.",
        },
        {
            "key": AMEDD,
            "stable_url": "https://achh.army.mil/history/book-wwii-woundblstcs-chapter4/",
            "title": "Casualty Survey-New Georgia and Burma Campaigns",
            "author_creator": "James E. T. Hopkins, M.D.",
            "repository_publisher": "U.S. Army Medical Department Center of History and Heritage",
            "publication_record_date": "World War II historical study; web edition accessed 2026",
            "locator": "Chapter IV, Burma section; original page approximately 247",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "rights_notes": "Supports only a qualified identity lead and 1944 Army assignment; no OSS or pre-OSS chronology is stated.",
        },
        {
            "key": OSSOG,
            "stable_url": "https://ossog.info/personnel.html",
            "title": "Office of Strategic Services Operational Groups personnel roster",
            "repository_publisher": "OSS Operational Groups historical project",
            "locator": "Norwegian operations personnel list",
            "access_date": "2026-11-03",
            "source_quality": "D_correlative_or_secondary",
            "rights_notes": "The roster and index share a protected identifier privately, but their printed grades conflict; the site says its list remains under construction.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": ORG_FIRESTONE,
            "canonical_name": "Firestone",
            "historical_name": "Firestone",
            "aliases": [],
            "organization_type": "industrial employer",
            "sector": "business_and_industry",
            "state_or_region": "Ohio",
            "country": "United States",
            "active_dates": "Documented in the 1941 directory",
            "normalization_notes": "The directory's abbreviated employer wording is preserved. A more specific Firestone corporate entity is not inferred.",
        },
        {
            "key": ORG_GRENADIER_GUARDS,
            "canonical_name": "Grenadier Guards",
            "historical_name": "Grenadier Guards",
            "aliases": [],
            "organization_type": "military unit",
            "sector": "military",
            "country": "United Kingdom",
            "normalization_notes": "Preserves the official London Gazette unit name; no predecessor or successor is inferred.",
        },
    ]


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, item in ARMY_MATCHES.items():
        values.append({
            "key": occupation_key(row),
            "person_id": PEOPLE[row][0],
            "occupation": item["occupation"],
            "relationship_type": "student" if item["code"] == "992" else "unknown",
            "end_date": item["date"],
            "date_precision": f"Historical civilian-occupation code {item['code']} was recorded at Army entry on {item['date']}; no named employer, workplace, institution, or exact OSS-transfer date is supplied.",
            "country": "United States",
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "confirmed",
            "claim_confidence": "medium",
            "source_quality": "A_direct_official",
            "publication_status": "publish_qualified",
            "research_notes": "Broad historical category only; no named employer, institution, workplace, or OSS transition is inferred.",
        })
    values.extend([
        {
            "key": "doris-werntz-firestone-b1008",
            "person_id": PEOPLE[5][0],
            "organization_key": ORG_FIRESTONE,
            "organization_name_as_found": "Firestone",
            "role_title": "Accountant",
            "occupation": "accountant",
            "relationship_type": "employment",
            "end_date": "1941",
            "date_precision": "A 1941 directory lists the exact rare name as an accountant at Firestone; the index supplies no independent identifier or exact OSS-entry date.",
            "state_or_region": "Ohio",
            "country": "United States",
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "probable",
            "claim_confidence": "medium",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "publish_qualified",
            "research_notes": "Qualified rare-name lead. It is neither immediate-pre-OSS nor last-civilian employment without personnel-file confirmation.",
        },
        {
            "key": "guy-westmacott-grenadier-guards-b1008",
            "person_id": PEOPLE[41][0],
            "organization_key": ORG_GRENADIER_GUARDS,
            "organization_name_as_found": "Grenadier Guards",
            "role_title": "Temporary lieutenant-colonel",
            "relationship_type": "military_assignment",
            "end_date": "1947-05-23",
            "date_precision": "The Gazette notice is postwar and confirms the affiliation but does not give its start date or relation to OSS entry.",
            "country": "United Kingdom",
            "pre_oss_temporal_basis": "temporal_relation_uncertain",
            "identity_confidence": "high_confidence",
            "claim_confidence": "medium",
            "source_quality": "A_direct_official",
            "publication_status": "publish_qualified",
            "research_notes": "Military affiliation only; not classified as an employer or immediate pre-OSS assignment.",
        },
    ])
    return values


def make_claim(*, key: str, row: int, claim_type: str, text: str, paraphrase: str,
               identity: str, temporal: str, quality: str, confidence: str,
               publication: str, notes: str, source_links: list[dict[str, str]],
               affiliation_key: str | None = None) -> dict[str, object]:
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
            key=f"occupation-{slug(name)}-row{row}-b1008",
            row=row,
            claim_type="occupation",
            text=f"At Army entry on {item['date']}, {name} was recorded in the historical {item['occupation']} category; no named employer or institution is identified.",
            paraphrase=f"The accepted Army record carries civilian-occupation code {item['code']}, decoded from NARA's official code list.",
            identity="The category belongs only to the accepted exact-name, protected-identifier match; the identifier itself is not public.",
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
        make_claim(key="identity-doris-werntz-b1008", row=5, claim_type="identity", text="Indexed Doris M. Werntz is a probable match to the exact rare name in the 1941 Barberton directory.", paraphrase="The directory and index agree on the full name and middle initial, but no independent service, hometown, or OSS identifier bridges them.", identity="Probable rare-name match pending the Box 827 personnel file.", temporal="The directory is securely prewar, but its relation to OSS entry is not established.", quality="B_authoritative_institutional", confidence="medium", publication="publish_qualified", notes="Visible qualification prevents a name-only directory hit from becoming a confirmed identity.", source_links=[{"source_key": INDEX, "locator_override": "PDF page 498 row 5"}, {"source_key": AKRON, "locator_override": "PDF physical page 417; printed page 1617", "excerpt_override": "Werntz Doris M acct Firestone"}]),
        make_claim(key="earlier-doris-werntz-firestone-b1008", row=5, claim_type="other_pre_oss_affiliation", text="If the probable identity is confirmed, Doris M. Werntz worked as an accountant at Firestone in 1941.", paraphrase="The 1941 directory lists the exact rare name with the abbreviation for accountant and the employer name Firestone.", identity="Probable rare-name match; no second distinguishing identifier is available online.", temporal="Documented prewar employment only; neither immediacy nor last-civilian status is established.", quality="B_authoritative_institutional", confidence="medium", publication="publish_qualified", notes="Qualified and excluded from default confirmed/high employer analytics.", source_links=[{"source_key": AKRON, "locator_override": "PDF physical page 417; printed page 1617", "excerpt_override": "Werntz Doris M acct Firestone"}], affiliation_key="doris-werntz-firestone-b1008"),
        make_claim(key="identity-theodore-wertime-b1008", row=9, claim_type="identity", text="Indexed Theodore A. Wertime is confirmed as the Theodore A. Wertime whose obituary states that he served with OSS in China during World War II.", paraphrase="The exact uncommon full name, official Army bridge, age-compatible wartime chronology, and direct obituary statement align.", identity="Confirmed through the index, accepted protected Army identifier, and direct OSS obituary context.", temporal="The obituary places OSS service during World War II; the Army record dates entry to October 1944.", quality="A_direct_official", confidence="confirmed", publication="published", notes="The obituary supports identity and OSS service, not a pre-OSS employer.", source_links=[{"source_key": INDEX, "locator_override": "PDF page 498 row 9; protected identifier masked"}, {"source_key": ARMY, "locator_override": "Army entry 1944-10-23; protected identifier withheld"}, {"source_key": WAPO, "locator_override": "Wartime-service paragraph", "excerpt_override": "During World War II, he served in China with the Office of Strategic Services"}]),
        make_claim(key="identity-roland-weschler-conflict-b1008", row=11, claim_type="identity", text="Roland E. Weschler remains in identity conflict because the same protected service number is also printed for a differently named index person.", paraphrase="The page-498 row and a page-494 row for Roland E. Wechsberg share a private identifier despite different surnames.", identity="Conflicting; the two source rows remain separate entities pending review of both personnel files.", temporal="No temporal or employment conclusion can be drawn from the identifier conflict.", quality="A_direct_official", confidence="conflicting", publication="conflicting", notes="The full protected number is omitted from the public claim.", source_links=[{"source_key": INDEX, "locator_override": "PDF page 498 row 11 and page 494 row 16; protected identifier withheld"}]),
        make_claim(key="identity-paul-west-b1008", row=26, claim_type="identity", text="Indexed Colonel Paul West is a high-confidence match to the OSS report naming Colonel Paul West as the senior U.S. officer in Greece.", paraphrase="The exact name, exact colonel rank, U.S. Army designation, and direct OSS operational context align.", identity="High confidence despite the common name because rank and contemporaneous OSS assignment context corroborate it.", temporal="The report documents an OSS-era assignment on 15 October 1944, not the preceding employer or unit.", quality="A_direct_official", confidence="high", publication="published", notes="No pre-OSS affiliation is inferred from an OSS-era operational report.", source_links=[{"source_key": INDEX, "locator_override": "PDF page 498 row 26"}, {"source_key": GREECE, "locator_override": "PDF physical page 15", "excerpt_override": "Colonel Paul West, AUS, senior U.S. officer in Greece"}]),
        make_claim(key="identity-arthur-westgard-rank-conflict-b1008", row=38, claim_type="identity", text="Arthur J. Westgard is linked to the Norwegian operational-groups roster by a private identifier, but the sources disagree on grade.", paraphrase="The index prints Captain Arthur J. Westgard; the roster prints T/5 A. J. Westgard with the same protected identifier.", identity="Confirmed person-level bridge with an unresolved Captain-versus-T/5 grade conflict.", temporal="Both sources concern wartime service; neither establishes a pre-OSS employer or immediate predecessor assignment.", quality="D_correlative_or_secondary", confidence="conflicting", publication="conflicting", notes="The full protected identifier is not published, and the grade conflict remains explicit.", source_links=[{"source_key": INDEX, "locator_override": "PDF page 498 row 38; protected identifier withheld"}, {"source_key": OSSOG, "locator_override": "Norwegian operations personnel list", "excerpt_override": "T/5 A. J. Westgard"}]),
        make_claim(key="identity-guy-westmacott-b1008", row=41, claim_type="identity", text="Indexed British Colonel Guy Westmacott is a high-confidence match to Lieutenant-Colonel Guy Randolph Westmacott of the Grenadier Guards.", paraphrase="The unique name, colonel-level rank, British note, and official Gazette record align and supply the middle name Randolph.", identity="High confidence from distinctive name, nationality, rank, and official military record.", temporal="The 1947 notice confirms wartime distinction but does not establish the timing of Grenadier Guards service relative to OSS.", quality="A_direct_official", confidence="high", publication="published", notes="The full name is added as a documented variant; no OSS chronology is inferred.", source_links=[{"source_key": INDEX, "locator_override": "PDF page 498 row 41"}, {"source_key": GAZETTE, "locator_override": "Supplement page 2287", "excerpt_override": "Lieutenant-Colonel (temporary) Guy Randolph WESTMACOTT, D.S.O. ... Grenadier Guards"}]),
        make_claim(key="military-guy-westmacott-grenadiers-b1008", row=41, claim_type="other_pre_oss_affiliation", text="Guy Randolph Westmacott is documented as a temporary lieutenant-colonel in the Grenadier Guards, but the affiliation's relation to OSS is unresolved.", paraphrase="The official Gazette gives his full name, temporary rank, and Grenadier Guards unit.", identity="High-confidence distinctive-name, rank, and nationality match.", temporal="Temporal relation uncertain: the postwar notice does not give the assignment's start date or OSS chronology.", quality="A_direct_official", confidence="medium", publication="publish_qualified", notes="Military affiliation only; excluded from employer analytics and not labeled immediate pre-OSS.", source_links=[{"source_key": GAZETTE, "locator_override": "Supplement page 2287", "excerpt_override": "Lieutenant-Colonel (temporary) Guy Randolph WESTMACOTT ... Grenadier Guards"}], affiliation_key="guy-westmacott-grenadier-guards-b1008"),
        make_claim(key="identity-logan-weston-b1008", row=44, claim_type="identity", text="Indexed Logan E. Weston is a probable match to First Lieutenant Logan E. Weston, who led an I&R platoon in Burma in 1944.", paraphrase="An official Army history gives the exact uncommon full name and wartime assignment in the 5307th Composite Unit.", identity="Probable exact-name match; the index supplies no rank or private identifier for a second independent bridge.", temporal="The source documents a 1944 Army assignment but does not establish its sequence relative to OSS service.", quality="A_direct_official", confidence="medium", publication="publish_qualified", notes="Qualified identity context only; no pre-OSS affiliation claim is made.", source_links=[{"source_key": INDEX, "locator_override": "PDF page 498 row 44"}, {"source_key": AMEDD, "locator_override": "Chapter IV, Burma section; original page approximately 247", "excerpt_override": "1st Lt. Logan E. Weston, Inf."}]),
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
    if row in {27, 28}:
        value["possible_duplicate_group"] = "name-only:robert-c-west-page498"
    value.update(overrides)
    return value


def person_updates() -> list[dict[str, object]]:
    special = set(ARMY_MATCHES) | {5, 11, 26, 38, 41, 44}
    values: list[dict[str, object]] = []
    for row in sorted(set(PEOPLE) - special):
        reason = unresolved_reason(row)
        values.append(base_update(
            row,
            identity_status="unresolved",
            identity_evidence=f"The visually verified page 498 source preserves {PEOPLE[row][1]}, its printed rank or notation, archival box, and location. {reason}",
            research_status="requires_archival_review",
            next_action=f"Review the indexed Box {box_for(row)} personnel file for corroborating identifiers, the immediate pre-OSS affiliation, and the last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}",
        ))
    for row in ARMY_MATCHES:
        item = ARMY_MATCHES[row]
        values.append(base_update(
            row,
            identity_status="confirmed",
            identity_evidence="The exact indexed and Army names agree, and a nonshared protected identifier connects the records. The identifier remains private.",
            personnel_category="enlisted_army_personnel",
            commissioned_officer=False,
            research_status="occupation_only_found",
            next_action=f"Review the indexed Box {box_for(row)} personnel file to identify any named employer or institution behind the broad {item['occupation']} category and establish the Army-to-OSS chronology.",
            nara_catalog_id="1263923",
        ))
    values.extend([
        base_update(5, identity_status="probable", identity_evidence="The exact rare name Doris M. Werntz appears in both the index and a visually inspected 1941 Barberton directory, but no independent identifier connects the records.", research_status="documented_prewar_employer_found", archival_review_priority="critical", next_action="Review the Box 827 personnel file to confirm the rare-name Firestone accountant lead and determine whether it was immediate or the last civilian employment before service."),
        base_update(11, identity_status="conflicting", identity_evidence="The same protected service number is printed for Roland E. Weschler and the separately indexed Roland E. Wechsberg. Both entities remain separate pending file review.", possible_duplicate_group="serial-conflict:roland-weschler-wechsberg", research_status="conflicting_sources", archival_review_priority="critical", next_action="Review both indexed personnel files to resolve the shared protected service number without merging the differently named rows."),
        base_update(26, identity_status="high_confidence", identity_evidence="A contemporary official OSS report names Colonel Paul West, AUS, as the senior U.S. officer in Greece, matching both the indexed name and colonel rank.", personnel_category="commissioned_army_officer", commissioned_officer=True, research_status="requires_archival_review", archival_review_priority="critical", next_action="Review the Box 828 personnel file to establish Colonel Paul West's immediate pre-OSS unit or institution and last civilian employer."),
        base_update(38, identity_status="confirmed", identity_evidence="A private protected-identifier match connects the index and Norwegian operational-groups roster, but Captain in the index conflicts with T/5 in the roster.", research_status="conflicting_sources", archival_review_priority="critical", next_action="Review the Box 828 personnel file to resolve the Captain-versus-T/5 grade conflict and establish Arthur J. Westgard's pre-OSS affiliation."),
        base_update(41, identity_status="high_confidence", identity_evidence="The distinctive name, British note, colonel-level rank, and official Gazette entry for Guy Randolph Westmacott of the Grenadier Guards align.", name_variants=["Guy Westmacott", "Guy Randolph Westmacott"], replace_name_variants=True, personnel_category="foreign_or_allied_military_personnel", commissioned_officer=True, allied_or_foreign_personnel=True, research_status="occupation_only_found", archival_review_priority="critical", next_action="Review the Box 828 personnel file to establish the Grenadier Guards assignment's chronology relative to OSS and identify any last civilian employer."),
        base_update(44, identity_status="probable", identity_evidence="An official Army history gives the exact uncommon name First Lieutenant Logan E. Weston and a 1944 Burma assignment, but the index lacks a second distinguishing identifier.", research_status="requires_archival_review", archival_review_priority="critical", next_action="Review the Box 828 personnel file to confirm the Merrill's Marauders identity lead and establish the assignment's sequence relative to OSS service."),
        {
            "person_id": WECHSBERG_ID,
            "identity_status": "conflicting",
            "identity_evidence": "The same protected service number is printed for Roland E. Wechsberg and the separately indexed Roland E. Weschler. Both entities remain separate pending file review.",
            "manual_review_required": True,
            "possible_duplicate_group": "serial-conflict:roland-weschler-wechsberg",
            "research_status": "conflicting_sources",
            "next_action": "Review both indexed personnel files to resolve the shared protected service number without merging the differently named rows.",
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
            "archival_review_priority": "critical",
        },
    ])
    if len(values) != len(PEOPLE) + 1:
        raise RuntimeError(f"Expected {len(PEOPLE) + 1} person updates, generated {len(values)}")
    return values


def research_attempts() -> list[dict[str, object]]:
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        if row == 5:
            outcome, reviewed, rejected = "source_reviewed", 11, 6
            note = "A visually inspected 1941 directory supplies a qualified rare-name Firestone accountant lead; the Box 827 file is still required for identity and chronology."
        elif row == 11:
            outcome, reviewed, rejected = "source_reviewed", 9, 6
            note = "A duplicate protected service number conflicts with the separately indexed Roland E. Wechsberg; both entities remain separate."
        elif row == 26:
            outcome, reviewed, rejected = "source_reviewed", 10, 6
            note = "A visually inspected contemporary OSS report supports a high-confidence Colonel Paul West identity in Greece but no pre-OSS affiliation."
        elif row == 38:
            outcome, reviewed, rejected = "source_reviewed", 9, 5
            note = "A protected-identifier bridge to a Norwegian operational-groups roster confirms the person but exposes an unresolved Captain-versus-T/5 grade conflict."
        elif row == 41:
            outcome, reviewed, rejected = "source_reviewed", 10, 5
            note = "A visually inspected London Gazette notice supports the full name Guy Randolph Westmacott and Grenadier Guards affiliation; OSS chronology remains unresolved."
        elif row == 44:
            outcome, reviewed, rejected = "source_reviewed", 9, 6
            note = "An official Army history supports a probable First Lieutenant Logan E. Weston identity and 1944 Burma assignment; no independent index identifier or OSS chronology is available."
        elif row in ARMY_MATCHES:
            item = ARMY_MATCHES[row]
            outcome, reviewed, rejected = "source_reviewed", 9, 5
            note = f"A reviewed exact-name, protected-identifier Army bridge supports identity and a qualified {item['occupation']} category at Army entry; no named employer, institution, workplace, or OSS-transfer date is supplied."
        else:
            outcome, reviewed, rejected = "candidate_rejected", 7, 6
            note = unresolved_reason(row)
        attempts.append({
            "key": f"page498-row{row}-{slug(name)}-b1008",
            "person_id": person_id,
            "source_adapter": "manual_staged_protocol",
            "query_text": f"{name}; NARA OSS index context; CIA Reading Room, National Archives, and Library of Congress exact-name domain checks; exact-name and meaningful spelling, initial, suffix, punctuation, transliteration, and OCR variants; OSS, rank, branch, assignment, and identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory, and archival searches; indexed Box {box_for(row)}; protected identifiers used only in private official-record comparison",
            "query_variant_type": "staged_identity_employment_archival_protocol_batch_1008",
            "started_at": "2026-11-04T02:50:00Z",
            "completed_at": "2026-11-04T03:30:00Z",
            "outcome": outcome,
            "sources_reviewed": reviewed,
            "candidate_sources_rejected": rejected,
            "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, postwar-only leads, discovery-only biographies, and sources without an OSS, protected-identifier, rank, unit, or personnel-file bridge were rejected. Historical Army categories were not converted into named employers, workplaces, or institutions. Student status was not converted into employment.",
            "research_notes": f"{note} Exact-name official-domain, OSS, employer, occupation, obituary, biography, institutional, newspaper, directory, and archival searches were checked as applicable. NARA index page 498 and relevant evidence pages were rendered and visually checked. No authenticated NARA Catalog API call was made.",
            "next_action": f"Review the indexed Box {box_for(row)} personnel file for corroborating identifiers, the immediate pre-OSS affiliation, and the last civilian employer before wartime service.",
            "attempt_number": 1,
            "research_agent_version": "before-oss-b1008-v1",
        })
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-1008-v1",
        "reviewer": "Before OSS Batch 1008 evidence review",
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
