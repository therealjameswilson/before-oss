#!/usr/bin/env python3
"""Generate the reviewed Batch 993 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page487-waffle-to-waite-"
    "review_batch-993_2026-11-03.json"
)

INDEX = "nara-index-b993"
ARMY = "army-bulk-b993"
TECH = "army-tech-b993"
CODES = "army-codes-b993"
BOULDER = "boulder-county-wagener-b993"
HOUSE = "house-stuyvesant-wainwright-b993"
HARVEY_OBIT = "harvey-wainright-obituary-b993"
GRAZ = "graz-ludwig-wagner-b993"

ORG_CHICAGO = "chicago-daily-times-b993"
ORG_KFEL = "kfel-radio-b993"
ORG_ARMY = "us-army-canonical-b993"
ORG_YALE_LAW = "yale-law-school-canonical-b993"
ORG_ASSEMBLY = "assembly-democratic-austrian-republic-b993"
ORG_KLEINE = "das-kleine-blatt-b993"


PEOPLE = {
    1: ("c9d24217-4daf-54c1-a360-7bbf1130d951", "Albert H Waffle"),
    2: ("aaf02551-6b0f-5358-ac5b-09d04eb45d59", "Siegfried Wagener"),
    3: ("f823b41c-13ff-5735-8b5c-21117a39475e", "Stanley S Wager"),
    4: ("74f95699-9431-5381-bd4f-f58c95d8e856", "David E Waggoner"),
    5: ("1ff34c99-84d5-539b-a946-635ee8d7b323", "Albert Wagner"),
    6: ("a83ac3b9-2f7f-59b1-a87b-9800dc64f475", "Allan Wagner"),
    7: ("c902112c-4321-5c6d-bfc8-e1d5f69fd0db", "Allen Oscar Wagner"),
    8: ("4c8b55c7-eb17-5490-893c-32f05e62e8de", "Bernard G Wagner"),
    9: ("e05bbae5-7976-5f5e-90df-21c66096b8da", "Charles B Wagner"),
    10: ("614f3952-4274-5c62-8bc4-a44b1b82abe3", "Harry Eugene Wagner"),
    11: ("f38438b9-058a-5208-95c5-616f37265236", "Herta Gloria Wagner"),
    12: ("8663f075-bcc3-50b2-9de0-e9fdfac8a682", "Lloyd A Wagner"),
    13: ("8e2548e9-16a4-5e4d-ac17-2d14a40834ae", "Ludwig Anton Wagner"),
    14: ("02ed2ba0-c9e3-56cf-81c7-8142e8da4f2a", "Paul A Wagner"),
    15: ("66344d4e-7120-5bca-9cdb-259bab783be8", "Richard D Wagner"),
    16: ("917d8c7a-0983-5730-934e-314ff181e146", "Shirley Carol Wagner"),
    17: ("44f08118-cc69-5e8c-85b5-d0555cd2ae14", "William E Wagner"),
    18: ("146c48fa-7fb8-5a02-adfe-4938e195d561", "Joseph Wago Jr."),
    19: ("80c9aa4f-6fe5-5fe4-b790-12ed4fb6f446", "Florence E Wagoner"),
    20: ("1485beb4-f02c-5159-9abe-7b10a9fdae8c", "David R Wahl"),
    21: ("7717ded8-388f-5cf9-8dea-cbc41c69f1c7", "Harvey W Wainwright"),
    22: ("55ab49e4-7b19-5746-9576-de7f1c8cc8d4", "Stuyvesant Wainwright"),
    23: ("f26f02bd-08ba-58d2-b7a7-13c6b1f7f485", "James P Waite"),
}


UNRESOLVED = {
    1: "Exact-name, OSS, employer, occupation, obituary, institutional, newspaper and archival searches produced no reliable identity bridge.",
    4: "A cemetery transcription names a World War II Army technician fifth grade with the exact name, but it supplies no indexed identifier, OSS link or pre-service chronology.",
    6: "Common-name and spelling-variant searches produced no source with the indexed identifier or a direct OSS assignment bridge.",
    7: "The distinctive full name produced no source with an OSS, protected-identifier, employer or personnel-file bridge.",
    8: "Multiple genealogy and cemetery namesakes lacked the indexed identifier and an OSS or employment bridge.",
    9: "Common-name results lacked the indexed identifier, OSS assignment and corroborating identifiers required for assignment.",
    10: "A modern namesake and a local veterans list were rejected because their chronology is incompatible with World War II service.",
    11: "The distinctive exact name produced no reliable biographical, institutional, military or employment source.",
    16: "Exact-name, OSS, occupation, obituary, directory, institutional and archival searches produced no reliable result.",
    18: "Exact-name and suffix searches produced no source with an OSS, protected-identifier or personnel-file bridge.",
    19: "People-finder and genealogy results exposed multiple namesakes and sensitive personal data but no defensible OSS identity; they were rejected and not retained.",
    20: "Common-name results produced no source with the middle initial, indexed identifier or direct OSS bridge.",
    23: "Common-name results produced no source with the middle initial, indexed identifier, rank, unit or direct OSS bridge.",
}


ARMY_PREOSS = {
    3: {
        "date": "1943-03-03",
        "code": "992",
        "occupation": "student",
        "relationship": "student",
        "code_locator": "PDF physical page 304; amended historical category 9-92",
    },
    5: {
        "date": "1942-02-05",
        "code": "316",
        "occupation": "farm hands, general farms",
        "relationship": "employment",
        "code_locator": "PDF physical page 172; historical category 3-16",
    },
    12: {
        "date": "1942-03-05",
        "code": "678",
        "occupation": "machine shop and related occupations, n.e.c.",
        "relationship": "employment",
        "code_locator": "PDF physical page 174; historical category 6-78",
    },
    14: {
        "date": "1942-02-13",
        "code": "340",
        "occupation": "gardeners and grounds keepers, parks, cemeteries, etc.",
        "relationship": "employment",
        "code_locator": "PDF physical page 172; historical category 3-40",
    },
    21: {
        "date": "1942-10-03",
        "code": "992",
        "occupation": "student",
        "relationship": "student",
        "code_locator": "PDF physical page 304; amended historical category 9-92",
    },
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 810-811",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 487, rows 1-23; checked against layout-preserving text and an original-detail page render",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. Protected identifiers remain private. PDF page 487 row 24, Wilma Isabel Waite, is outside this cohort and begins the next batch.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; seven accepted protected-identifier comparisons; identifiers and record ordinals withheld",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "Five exact-name records and two documented spelling variants were accepted with nonshared protected identifiers. The 1945-11-16 and 1946-05-28 Army entries postdate OSS dissolution and are identity evidence only.",
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
            "locator": "PDF physical pages 172, 174 and 304; categories 3-16, 3-40, 6-78 and amended 9-92",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical labels identify broad occupations or student status, not named employers, schools, workplaces or exact OSS-transfer dates. The amended page 304 maps code 992 to Students.",
        },
        {
            "key": BOULDER,
            "stable_url": "https://assets.bouldercounty.gov/wp-content/uploads/2018/02/hpab-agenda-and-meeting-packet-20180301.pdf",
            "archival_identifier": "Boulder County Historic Preservation Advisory Board packet, HP-17-0005",
            "title": "Historic Preservation Advisory Board Agenda and Meeting Packet",
            "author_creator": "Boulder County Land Use Department, Historic Preservation Program",
            "repository_publisher": "Boulder County, Colorado",
            "publication_record_date": "2018-03-01",
            "locator": "PDF physical page 5, Tahosa Valley Land Office history and significance; visually inspected",
            "access_date": "2026-11-03",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Boulder County Historic Preservation Advisory Board records",
            "rights_notes": "The county record directly links Siegfried Wagener to OSS and documents Chicago Times and KFEL work. Employment form and exact OSS entry remain qualified.",
        },
        {
            "key": HOUSE,
            "stable_url": "https://history.house.gov/People/Detail/23247",
            "archival_identifier": "Biographical Directory identifier W000024",
            "title": "WAINWRIGHT, Stuyvesant, II",
            "author_creator": "Office of the Historian and Office of Art and Archives",
            "repository_publisher": "U.S. House of Representatives",
            "publication_record_date": "updated 2026-09-01",
            "locator": "Concise Biography",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "History, Art & Archives, U.S. House of Representatives",
            "rights_notes": "The official biography supplies a direct Yale-to-Army chronology and explicitly identifies command of OSS units of the First Army.",
        },
        {
            "key": HARVEY_OBIT,
            "stable_url": "https://owenspavlotrogers.com/tribute/details/106/Harvey-Wainright/obituary.html",
            "title": "Obituary of Harvey W. Wainright",
            "author_creator": "Harvey W. Wainright; family and funeral-home publication",
            "repository_publisher": "Owens-Pavlot & Rogers Funeral Service",
            "publication_record_date": "2010-11",
            "locator": "Self-authored biographical section",
            "access_date": "2026-11-03",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Owens-Pavlot & Rogers obituaries",
            "rights_notes": "Used for the Wainright spelling and explicit OSS service context. Postwar General Electric work is excluded from pre-OSS claims.",
        },
        {
            "key": GRAZ,
            "stable_url": "https://agso.uni-graz.at/archive/marienthal/biografien/wagner_ludwig.htm",
            "title": "Ludwig Wagner",
            "author_creator": "Reinhard Müller; based on biographical work by Herbert Exenberger and Eckart Früh",
            "repository_publisher": "Archive for the History of Sociology in Austria, University of Graz",
            "publication_record_date": "updated 2012-08",
            "locator": "Biographical chronology and bibliography",
            "access_date": "2026-11-03",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Marienthal study biographical archive",
            "rights_notes": "The rare exact name and compatible U.S. wartime chronology support a probable identity only; the biography does not itself mention OSS.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": ORG_CHICAGO,
            "canonical_name": "Chicago Daily Times",
            "historical_name": "Chicago Times",
            "aliases": ["Chicago Daily Times", "Chicago Times"],
            "organization_type": "newspaper",
            "sector": "journalism_and_media",
            "city": "Chicago",
            "state_or_region": "Illinois",
            "country": "United States",
            "active_dates": "1929-1948 under the Chicago Daily Times name",
            "normalization_notes": "The source's Chicago Times wording is preserved. The later Chicago Sun-Times is a successor, not substituted as the wartime employer.",
        },
        {
            "key": ORG_KFEL,
            "canonical_name": "KFEL",
            "historical_name": "KFEL",
            "aliases": ["KFEL Denver"],
            "organization_type": "radio station",
            "sector": "journalism_and_media",
            "city": "Denver",
            "state_or_region": "Colorado",
            "country": "United States",
            "normalization_notes": "Historical call sign preserved; no modern successor is silently substituted.",
        },
        {
            "key": ORG_ARMY,
            "organization_id": "28a26f92-78af-5a1a-9c09-a843eb5975b4",
            "canonical_name": "United States Army",
            "historical_name": "United States Army",
            "aliases": ["U.S. Army", "Army of the United States"],
            "organization_type": "armed service",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "Existing canonical military organization reused; Stuyvesant Wainwright's First Army OSS command remains a role, not a separate employer.",
        },
        {
            "key": ORG_YALE_LAW,
            "organization_id": "779938ea-1d26-5c1f-81a8-9155c71c0a64",
            "canonical_name": "Yale Law School",
            "historical_name": "Yale University Law School",
            "aliases": ["Yale law faculty", "Yale Law"],
            "organization_type": "university law school",
            "sector": "academia_and_research",
            "city": "New Haven",
            "state_or_region": "Connecticut",
            "country": "United States",
            "normalization_notes": "Existing organization reused. Student status is not employment.",
        },
        {
            "key": ORG_ASSEMBLY,
            "canonical_name": "Assembly for a Democratic Austrian Republic",
            "historical_name": "Assembly for a Democratic Austrian Republic",
            "aliases": [],
            "organization_type": "political exile organization",
            "sector": "labor_nonprofit_and_religion",
            "city": "New York",
            "state_or_region": "New York",
            "country": "United States",
            "active_dates": "1942-1943",
            "normalization_notes": "Preserved as a professional or political affiliation, not employment.",
        },
        {
            "key": ORG_KLEINE,
            "canonical_name": "Das Kleine Blatt",
            "historical_name": "Das Kleine Blatt",
            "aliases": [],
            "organization_type": "newspaper",
            "sector": "journalism_and_media",
            "city": "Vienna",
            "country": "Austria",
            "normalization_notes": "Historical newspaper title preserved.",
        },
    ]


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, item in ARMY_PREOSS.items():
        values.append(
            {
                "key": f"{slug(PEOPLE[row][1])}-army-category-b993",
                "person_id": PEOPLE[row][0],
                "occupation": item["occupation"],
                "relationship_type": item["relationship"],
                "end_date": item["date"],
                "date_precision": f"Historical civilian-occupation code {item['code']} was recorded at Army entry on {item['date']}; no named employer, school, workplace or OSS-transfer date is supplied.",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "confirmed",
                "claim_confidence": "medium",
                "source_quality": "A_direct_official",
                "publication_status": "publish_qualified",
                "research_notes": "Broad historical category or student status only; no named employer or school is inferred.",
            }
        )

    values.extend(
        [
            {
                "key": "siegfried-wagener-chicago-times-b993",
                "person_id": PEOPLE[2][0],
                "organization_key": ORG_CHICAGO,
                "organization_name_as_found": "Chicago Times",
                "role_title": "journalist, propaganda analyst and columnist",
                "relationship_type": "employment",
                "start_date": "1942-01",
                "date_precision": "Boulder County reports that one month after U.S. entry into World War II, Wagener's We're Listening column was picked up by the Chicago Times; the exact contract and end date are not stated.",
                "city": "Chicago",
                "state_or_region": "Illinois",
                "country": "United States",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "probable_immediate",
                "identity_confidence": "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "publish_qualified",
                "research_notes": "The county chronology places this work before a brief OSS position, but does not prove there was no intervening affiliation or define his employment contract.",
            },
            {
                "key": "siegfried-wagener-kfel-b993",
                "person_id": PEOPLE[2][0],
                "organization_key": ORG_KFEL,
                "organization_name_as_found": "KFEL",
                "role_title": "twice-weekly radio broadcaster",
                "relationship_type": "professional_affiliation",
                "start_date": "1941",
                "date_precision": "The county record dates the beginning of twice-weekly KFEL broadcasts to 1941; the end date and employment form are not stated.",
                "city": "Denver and Tahosa Valley",
                "state_or_region": "Colorado",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "publish_qualified",
                "research_notes": "Documented broadcasting affiliation; not silently converted into salaried employment.",
            },
            {
                "key": "ludwig-wagner-assembly-b993",
                "person_id": PEOPLE[13][0],
                "organization_key": ORG_ASSEMBLY,
                "organization_name_as_found": "Assembly for a Democratic Austrian Republic",
                "role_title": "leading figure",
                "relationship_type": "professional_affiliation",
                "start_date": "1942-04",
                "end_date": "1943-07",
                "date_precision": "The institutional biography dates the Assembly's formation to April 1942 and its merger into the Austro American Association to July 1943.",
                "city": "New York",
                "state_or_region": "New York",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "temporal_relation_uncertain",
                "identity_confidence": "probable",
                "claim_confidence": "medium",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "publish_qualified",
                "research_notes": "Rare-name probable identity. The affiliation is not employment and its sequence relative to OSS is not established.",
            },
            {
                "key": "ludwig-wagner-kleine-blatt-b993",
                "person_id": PEOPLE[13][0],
                "organization_key": ORG_KLEINE,
                "organization_name_as_found": "Das Kleine Blatt",
                "role_title": "editor",
                "relationship_type": "employment",
                "start_date": "1932-10",
                "end_date": "1933-04",
                "date_precision": "The University of Graz biography explicitly dates his editorial tenure from October 1932 through April 1933.",
                "city": "Vienna",
                "country": "Austria",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "probable",
                "claim_confidence": "medium",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "publish_qualified",
                "research_notes": "Documented earlier employment for the probable rare-name identity; not presented as immediate or the last civilian employer.",
            },
            {
                "key": "stuyvesant-wainwright-army-b993",
                "person_id": PEOPLE[22][0],
                "organization_key": ORG_ARMY,
                "organization_name_as_found": "United States Army",
                "role_title": "private; later commanding officer of OSS units of the First Army",
                "relationship_type": "military_assignment",
                "start_date": "1942-01-30",
                "date_precision": "The official House biography dates enlistment to 30 January 1942 and states that he later commanded OSS units of the First Army; the exact OSS transfer date is not given.",
                "country": "United States",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "A_direct_official",
                "publication_status": "published",
                "research_notes": "The Army pathway is a military assignment, not a civilian employer.",
            },
            {
                "key": "stuyvesant-wainwright-yale-b993",
                "person_id": PEOPLE[22][0],
                "organization_key": ORG_YALE_LAW,
                "organization_name_as_found": "Yale University",
                "role_title": "law student",
                "relationship_type": "student",
                "end_date": "1942-01-30",
                "date_precision": "The official biography says his legal studies were interrupted when he enlisted on 30 January 1942.",
                "city": "New Haven",
                "state_or_region": "Connecticut",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "A_direct_official",
                "publication_status": "published",
                "research_notes": "Student status immediately before Army enlistment; Yale is not classified as an employer.",
            },
        ]
    )
    return values


def links(*keys: str) -> list[dict[str, str]]:
    return [{"source_key": key} for key in keys]


def claim(
    key: str,
    row: int,
    claim_type: str,
    text: str,
    paraphrase: str,
    identity: str,
    temporal: str,
    quality: str,
    confidence: str,
    publication_status: str,
    notes: str,
    source_links: list[dict[str, str]],
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
        "publication_status": publication_status,
        "match_notes": notes,
        "sources": source_links,
    }
    if affiliation_key:
        value["affiliation_key"] = affiliation_key
    return value


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, item in ARMY_PREOSS.items():
        name = PEOPLE[row][1]
        if row == 21:
            identity_paraphrase = "A nonshared protected identifier links the index to the Army record, while the self-authored obituary independently uses Wainright and explicitly names OSS service."
            identity_assessment = "Confirmed by the protected identifier, compatible middle name and independent Wainright/OSS biography; the identifier remains private."
            identity_links = links(INDEX, ARMY, HARVEY_OBIT)
            identity_notes = "The index spelling Wainwright and documented spelling Wainright remain visible variants."
        else:
            identity_paraphrase = "The official index and Army bulk record agree in exact name and a nonshared protected identifier."
            identity_assessment = "Confirmed by direct protected-identifier agreement; the identifier and bulk ordinal remain private."
            identity_links = links(INDEX, ARMY)
            identity_notes = "Identity only; no employer, school or exact OSS-transfer date is inferred."
        values.append(
            claim(
                f"identity-{slug(name)}-b993",
                row,
                "identity",
                f"Indexed {name} is confirmed as the reviewed official Army entry record.",
                identity_paraphrase,
                identity_assessment,
                f"The Army record dates entry to {item['date']} and supplies only historical civilian code {item['code']}.",
                "A_direct_official",
                "confirmed",
                "published",
                identity_notes,
                identity_links,
            )
        )
        status_label = "student" if item["relationship"] == "student" else item["occupation"]
        claim_type = "other_pre_oss_affiliation" if item["relationship"] == "student" else "occupation"
        values.append(
            claim(
                f"army-category-{slug(name)}-b993",
                row,
                claim_type,
                f"At Army entry on {item['date']}, {name} was recorded as {status_label}; no named employer or school is identified.",
                f"The accepted Army record carries civilian-occupation code {item['code']}, decoded from NARA's official amended code list.",
                "The category belongs only to the confirmed protected-identifier match.",
                "Strongly date-bounded to Army entry; it does not establish a named employer, school or immediate OSS affiliation.",
                "A_direct_official",
                "medium",
                "publish_qualified",
                "The historical category is published with its limits and excluded from verified-employer analytics.",
                [
                    {"source_key": ARMY, "locator_override": f"Army entry {item['date']}; civilian occupation code {item['code']}; protected identifier withheld"},
                    {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46; Army-entry-date and civilian-occupation fields"},
                    {"source_key": CODES, "locator_override": item["code_locator"], "excerpt_override": "Students" if item["relationship"] == "student" else item["occupation"].capitalize()},
                ],
                f"{slug(name)}-army-category-b993",
            )
        )

    values.extend(
        [
            claim(
                "identity-siegfried-wagener-b993",
                2,
                "identity",
                "Indexed Siegfried Wagener is a high-confidence match to the Boulder County journalist and OSS staff member.",
                "The official county history uses the exact distinctive name, documents his Chicago and Colorado work, and explicitly states that he held an OSS position.",
                "High confidence from the rare exact name, compatible chronology and direct OSS statement in an authoritative county record.",
                "The county chronology places his journalism and broadcasting before a brief OSS position.",
                "B_authoritative_institutional",
                "high",
                "published",
                "The personnel file is still needed for the exact employment contract and OSS entry date.",
                links(INDEX, BOULDER),
            ),
            claim(
                "immediate-siegfried-wagener-chicago-times-b993",
                2,
                "immediate_pre_oss_affiliation",
                "Siegfried Wagener's Chicago Times journalism is the best-supported probable immediate civilian affiliation before his brief OSS position.",
                "Boulder County dates the newspaper column to one month after U.S. entry into the war and places the later OSS position after this work.",
                "High-confidence identity from the same exact-name county chronology that explicitly names OSS.",
                "Probable immediate: the sequence is strong, but the source gives neither an exact OSS entry date nor proof that no affiliation intervened.",
                "B_authoritative_institutional",
                "medium",
                "publish_qualified",
                "Published as qualified employment; excluded from default high/confirmed employer analytics.",
                [{"source_key": BOULDER, "locator_override": "PDF physical page 5", "excerpt_override": "his column ‘We're Listening’ ... was picked up by the Chicago Times"}],
                "siegfried-wagener-chicago-times-b993",
            ),
            claim(
                "last-civilian-siegfried-wagener-chicago-times-b993",
                2,
                "last_civilian_pre_service",
                "Chicago Times is the best-supported probable last civilian employer or publishing affiliation before Siegfried Wagener's OSS position.",
                "The county record describes reporter work, a newspaper column and later OSS service, but does not define whether he was staff, contract or syndicated.",
                "High-confidence identity from the exact-name direct OSS biography.",
                "Probable rather than settled because employment form and the exact transition date are unstated.",
                "B_authoritative_institutional",
                "medium",
                "publish_qualified",
                "The historical newspaper name is preserved; the modern successor is not substituted.",
                links(BOULDER),
                "siegfried-wagener-chicago-times-b993",
            ),
            claim(
                "kfel-siegfried-wagener-b993",
                2,
                "other_pre_oss_affiliation",
                "Siegfried Wagener began twice-weekly broadcasts on KFEL in 1941 while analyzing foreign propaganda.",
                "Boulder County documents the 1941 broadcasts and the Tahosa Valley listening post before describing his later OSS position.",
                "High-confidence identity from the exact-name direct OSS biography.",
                "Definitely wartime and pre-OSS in the county chronology; the employment form and end date remain unknown.",
                "B_authoritative_institutional",
                "medium",
                "publish_qualified",
                "Recorded as a professional affiliation, not assumed salaried employment.",
                [{"source_key": BOULDER, "locator_override": "PDF physical page 5", "excerpt_override": "in 1941, Wagener started broadcasting twice weekly from KFEL in Denver"}],
                "siegfried-wagener-kfel-b993",
            ),
            claim(
                "identity-ludwig-anton-wagner-b993",
                13,
                "identity",
                "Indexed Ludwig Anton Wagner is probably the Austrian journalist and economist documented by the University of Graz archive.",
                "The institutional biography uses the exact rare three-part name and supplies a compatible emigration and New York wartime chronology.",
                "Probable from the exceptionally distinctive exact name and compatible U.S. wartime context; the biography does not mention OSS or the personnel file.",
                "The biography documents employment and affiliations before and during the war but does not establish their sequence relative to OSS.",
                "B_authoritative_institutional",
                "medium",
                "publish_qualified",
                "Box 811 is required before upgrading identity or treating any role as immediate.",
                links(INDEX, GRAZ),
            ),
            claim(
                "assembly-ludwig-wagner-b993",
                13,
                "other_pre_oss_affiliation",
                "Ludwig Anton Wagner was a leading figure in New York's Assembly for a Democratic Austrian Republic from its 1942 formation until its 1943 merger.",
                "The University of Graz biography identifies him and dates the organization's formation and merger.",
                "Probable identity from the rare exact name and compatible wartime U.S. chronology.",
                "Documented wartime affiliation; its relation to OSS entry is unknown.",
                "B_authoritative_institutional",
                "medium",
                "publish_qualified",
                "Professional or political affiliation only, not employment.",
                links(GRAZ),
                "ludwig-wagner-assembly-b993",
            ),
            claim(
                "employment-ludwig-wagner-kleine-blatt-b993",
                13,
                "other_pre_oss_affiliation",
                "Ludwig Anton Wagner worked as an editor for Vienna's Das Kleine Blatt from October 1932 through April 1933.",
                "The institutional biography explicitly gives the newspaper, role and date range.",
                "Probable identity from the rare exact name; direct personnel-file confirmation remains absent.",
                "Explicitly dated earlier employment, not shown to be immediate or the last civilian job before OSS.",
                "B_authoritative_institutional",
                "medium",
                "publish_qualified",
                "Published as qualified earlier employment only.",
                links(GRAZ),
                "ludwig-wagner-kleine-blatt-b993",
            ),
            claim(
                "identity-richard-d-wagner-b993",
                15,
                "identity",
                "Indexed Richard D Wagner is confirmed as the official Army record printed as Agner Richard D.",
                "The records share a nonshared protected identifier, and the Army spelling differs only by the loss of the initial W.",
                "Confirmed by direct protected-identifier agreement and a narrowly explained one-letter loss; the identifier remains private.",
                "The Army entry date is 28 May 1946, after OSS dissolution, so its student code supplies no pre-OSS evidence.",
                "A_direct_official",
                "confirmed",
                "published",
                "Identity only; no post-OSS occupation code is transferred into the pre-OSS history.",
                links(INDEX, ARMY, TECH),
            ),
            claim(
                "identity-william-e-wagner-b993",
                17,
                "identity",
                "Indexed William E Wagner is confirmed as the reviewed official Army entry record.",
                "The index and Army bulk record agree in exact name and a nonshared protected identifier.",
                "Confirmed by direct protected-identifier agreement; the identifier and bulk ordinal remain private.",
                "The Army entry date is 16 November 1945, after OSS dissolution, so the civil-engineer code supplies no pre-OSS evidence.",
                "A_direct_official",
                "confirmed",
                "published",
                "Identity only; the post-OSS occupation code is deliberately withheld from the pre-OSS affiliation model.",
                links(INDEX, ARMY, TECH),
            ),
            claim(
                "identity-stuyvesant-wainwright-b993",
                22,
                "identity",
                "Indexed Stuyvesant Wainwright is a high-confidence match to the U.S. Representative and wartime OSS unit commander.",
                "The official House biography uses the distinctive exact name and explicitly states that he commanded OSS units of the First Army.",
                "High confidence from an exact distinctive name and direct official OSS biography.",
                "The same biography supplies the Yale-to-Army-to-OSS chronology.",
                "A_direct_official",
                "high",
                "published",
                "No famous-name assignment was made from name alone; the direct OSS statement is the identity bridge.",
                links(INDEX, HOUSE),
            ),
            claim(
                "army-stuyvesant-wainwright-b993",
                22,
                "immediate_pre_oss_affiliation",
                "The United States Army was Stuyvesant Wainwright's immediate institutional pathway into OSS command.",
                "The official biography dates Army enlistment and later identifies him as commanding officer of OSS units of the First Army.",
                "High-confidence identity from the distinctive exact name and direct official OSS statement.",
                "Strongly date-bounded military pathway; the exact transfer date is not given.",
                "A_direct_official",
                "high",
                "published",
                "Military assignment, never mislabeled as a civilian employer.",
                [{"source_key": HOUSE, "locator_override": "Concise Biography", "excerpt_override": "was commanding officer of O.S.S. units of the First Army"}],
                "stuyvesant-wainwright-army-b993",
            ),
            claim(
                "student-stuyvesant-wainwright-yale-b993",
                22,
                "other_pre_oss_affiliation",
                "Stuyvesant Wainwright was a Yale law student immediately before enlisting in the Army on 30 January 1942.",
                "The official House biography says his legal studies at Yale were interrupted by that dated enlistment.",
                "High-confidence identity from the distinctive exact name and direct official OSS biography.",
                "Explicitly bounded to the day of Army enlistment; student status is not employment.",
                "A_direct_official",
                "high",
                "published",
                "Yale is excluded from employer analytics.",
                links(HOUSE),
                "stuyvesant-wainwright-yale-b993",
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
    values = [
        base_update(
            row,
            identity_status="unresolved",
            identity_evidence=f"The visually verified page 487 row preserves {PEOPLE[row][1]} and its Box 810 or 811 context. {reason}",
            research_status="requires_archival_review",
            next_action=f"Review the indexed personnel file for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}",
        )
        for row, reason in UNRESOLVED.items()
    ]
    for row, item in ARMY_PREOSS.items():
        variants = ["Harvey W Wainright"] if row == 21 else None
        values.append(
            base_update(
                row,
                identity_status="confirmed",
                identity_evidence=(
                    "A nonshared protected identifier connects the index to the official Army record. The documented Wainright spelling and self-authored OSS biography independently resolve the index spelling variant."
                    if row == 21
                    else "The exact official name and a nonshared protected identifier connect the visually verified index row to the Army record."
                ),
                name_variants=variants,
                personnel_category="enlisted_army_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                research_status="occupation_only_found",
                next_action=f"Review Box {810 if row == 3 else 811} to identify any named employer or school behind historical code {item['code']} and establish the Army-to-OSS chronology.",
                nara_catalog_id="1263923",
            )
        )
    values.extend(
        [
            base_update(
                2,
                identity_status="high_confidence",
                identity_evidence="An authoritative Boulder County history uses the distinctive exact name, documents wartime journalism and broadcasting, and explicitly states that Wagener briefly held an OSS position.",
                personnel_category="civilian_professional_or_administrative_grade",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                research_status="documented_prewar_employer_found",
                next_action="Review Box 810 to confirm the Chicago Times employment form, determine whether Chicago Times or KFEL was the exact immediate predecessor, and establish the OSS entry date.",
                archival_review_priority="medium",
            ),
            base_update(
                13,
                identity_status="probable",
                identity_evidence="The University of Graz archive documents an exceptionally distinctive exact name and a compatible Austrian-emigre and New York wartime chronology, but does not itself mention OSS or the indexed file.",
                personnel_category="civilian_professional_or_administrative_grade",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                research_status="documented_prewar_employer_found",
                next_action="Review Box 811 to confirm the rare-name identity and determine whether the 1942-1943 Austrian exile organization preceded OSS service; Das Kleine Blatt remains qualified earlier employment only.",
            ),
            base_update(
                15,
                identity_status="confirmed",
                identity_evidence="A nonshared protected identifier connects the index to the Army record printed as Agner Richard D; the one-letter loss is retained as a documented source variant.",
                name_variants=["Agner Richard D"],
                personnel_category="enlisted_army_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                research_status="requires_archival_review",
                next_action="Review Box 811 for the pre-OSS history. The accepted Army entry is dated 28 May 1946, so its student code is not pre-OSS evidence.",
                nara_catalog_id="1263923",
            ),
            base_update(
                17,
                identity_status="confirmed",
                identity_evidence="The exact official name and a nonshared protected identifier connect the visually verified index row to the Army record.",
                personnel_category="enlisted_army_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                research_status="requires_archival_review",
                next_action="Review Box 811 for the pre-OSS history. The accepted Army entry is dated 16 November 1945, so its civil-engineer code is not pre-OSS evidence.",
                nara_catalog_id="1263923",
            ),
            base_update(
                22,
                identity_status="high_confidence",
                identity_evidence="The official House biography uses the distinctive exact name, supplies the Yale-to-Army chronology and explicitly states that Wainwright commanded OSS units of the First Army.",
                name_variants=["Stuyvesant Wainwright II"],
                personnel_category="commissioned_army_officer",
                commissioned_officer=True,
                allied_or_foreign_personnel=False,
                research_status="completed",
                next_action="No online research action is required. The indexed file may still refine the exact Army-to-OSS transfer date.",
                archival_review_priority="low",
            ),
        ]
    )
    return values


def research_attempts() -> list[dict[str, object]]:
    sourced = {2, 3, 5, 12, 13, 14, 15, 17, 21, 22}
    rejected = {4, 8, 10, 19}
    detail = {
        2: "A Boulder County preservation record directly linked the exact name to OSS and documented qualified Chicago Times and KFEL work.",
        3: "The accepted protected-identifier Army bridge produced a confirmed identity and qualified generic student status at 1943 Army entry.",
        5: "The accepted protected-identifier Army bridge produced a confirmed identity and qualified historical general-farm-hand category.",
        12: "The accepted protected-identifier Army bridge produced a confirmed identity and qualified historical machine-shop category.",
        13: "A University of Graz biography produced a probable rare-name identity, qualified Das Kleine Blatt employment and a wartime Austrian exile affiliation.",
        14: "The accepted protected-identifier Army bridge produced a confirmed identity and qualified historical gardener and groundskeeper category.",
        15: "A nonshared identifier resolved the Army file's one-letter name loss; the post-OSS entry was used for identity only.",
        17: "The accepted protected-identifier Army record dates after OSS dissolution and was used for identity only, not for its engineering code.",
        21: "The protected-identifier bridge, documented Wainright spelling and self-authored OSS obituary confirmed identity and qualified generic student status at Army entry.",
        22: "An official House biography directly documented Yale study, dated Army enlistment and command of OSS units of the First Army.",
    }
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        if row in sourced:
            outcome = "source_reviewed"
            reviewed = 8
            rejected_count = 5
            note = detail[row]
        elif row in rejected:
            outcome = "candidate_rejected"
            reviewed = 7
            rejected_count = 7
            note = UNRESOLVED[row]
        else:
            outcome = "no_result"
            reviewed = 6
            rejected_count = 6
            note = UNRESOLVED.get(row, "No reliable identity or pre-OSS affiliation bridge was found.")
        attempts.append(
            {
                "key": f"page487-row{row}-{slug(name)}-b993",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index context; CIA Reading Room exact-name domain check; Library of Congress exact-name collection check; exact-name and meaningful variants; OSS, rank, branch, identifier and assignment clues; employer and occupation 1940; obituary, institutional, newspaper, directory and archival searches; indexed Box 810 or 811; protected identifiers used only in private official-record comparison",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_993",
                "started_at": "2026-11-03T12:45:00Z",
                "completed_at": "2026-11-03T13:25:00Z",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected_count,
                "rejection_reasons": "Unbridged namesakes, snippets, commercial people-finder pages, relatives, unsourced genealogy, postwar-only leads and sources without an OSS, protected-identifier, rank, unit or personnel-file bridge were rejected. Modern Harry Eugene Wagner results, multiple Florence E. Wagoner people-finder records, an incompatible Albert Wagner military casualty and ambiguous Bernard G. Wagner records were not assigned. Historical Army categories, student status and military service were not silently converted into named employers.",
                "research_notes": f"{note} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain and archival searches were checked as applicable. Grouped CIA Reading Room and Library of Congress discovery checks produced no additional publishable source for the cohort. The NARA index, official Army bulk data, technical documentation and code-list pages were inspected directly; Boulder County packet physical page 5 was downloaded, text-extracted and visually checked. The official House biography and University of Graz institutional biography were inspected in context. No search-result snippet was used as sole final evidence, no paywall or access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": "Review the indexed personnel file for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before wartime service.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b993-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-993-v1",
        "reviewer": "Before OSS Batch 993 evidence review",
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
