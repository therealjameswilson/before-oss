#!/usr/bin/env python3
"""Generate the reviewed Batch 925 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import uuid
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / (
    "research/evidence-page453-charlie-e-stringer-to-bernard-e-strozenski-"
    "review_batch-925_2026-10-26.json"
)

INDEX = "nara-index-b925"
ARMY = "army-bulk-b925"
TECH = "army-tech-b925"
CODES = "army-codes-b925"
ART_BIN = "art-bin-tony-strobl-b925"
NIA = "nia-birger-stromsheim-b925"
PRAIRIE = "prairie-flier-harry-strouse-b925"
SCOTTISH_RITE = "scottish-rite-harry-strouse-jr-b925"
ARMY_REGISTER = "army-register-sherman-strong-b925"
ARMY_REVIEW = "army-review-ray-stroupe-b925"
AFSA = "afsa-harry-stritman-b925"
QUANTICO = "quantico-harry-stritman-b925"

PEOPLE = {
    1: ("76e80fa6-1a97-5b8d-87fd-a41f1f124314", "Charlie E Stringer", "753"),
    2: ("5ceda236-9a1e-5c3f-91c5-b3117ec25989", "James A Stringer", "753"),
    3: ("5fda078e-0385-586a-9257-c3b99737a8a7", "Elden R Stringfellow", "753"),
    4: ("323aa721-0234-53d2-9da8-5f5cb06229fc", "Horace Stringfellow", "753"),
    5: ("3f6fef6c-0374-52f3-8e35-bc44710d72a1", "Harry R Stritman", "753"),
    6: ("9e1f8844-880f-5c12-a8bc-7874a97eaff7", "Anthony J Strobl", "753"),
    7: ("598a0f40-31e6-5acc-8807-c30ffca57c47", "Sylvia S Strohman", "753"),
    8: ("b3919726-c363-5da4-9258-156e6e8e6ba7", "Lester A Stromberg", "753"),
    9: ("638047fa-fbbe-53c7-96d4-77c794b814c2", "Edmund I Stromholt", "753"),
    10: ("87031931-cac0-53eb-829a-03e87dc4b2d0", "Birger Stromsheim", "753"),
    11: ("04292e37-b226-552b-860c-336b8b48b126", "David F Strong", "753"),
    12: ("dcbc6a3f-534d-5681-aba3-43064e772089", "Joan M Strong", "754"),
    13: ("d3c854f7-60c5-5d4a-bf28-428146db4061", "Philip D Strong", "754"),
    14: ("15a35f9d-2de5-5c55-9cc5-0fd3b3ff5394", "Sherman I Strong", "754"),
    15: ("88a9dda3-01d2-5385-b121-ba17ca341dd8", "Philip Strongin", "754"),
    16: ("0a7e8099-31d5-504e-b3bb-8e1f990130e6", "Edward K Stropp", "754"),
    17: ("e763e441-1516-5f89-8f03-3def28d07a81", "Jaunita H Strosnider", "754"),
    18: ("2404a3bd-01c7-552e-ab1d-0c07adc3c20d", "Jeanne H Stroud", "754"),
    19: ("2551c9c8-3307-5ca3-b498-f1b9348bc45e", "Robert L Stroud", "754"),
    20: ("8264951b-a33e-5155-9a62-996388c1acf2", "Ray M Stroupe", "754"),
    21: ("5bca5a08-f53d-5f02-8a4c-c75e3c0781cd", "Harry D Strouse", "754"),
    22: ("ee569abe-319c-567c-a922-49ff72153677", "Bernard B Strozenski", "754"),
    23: ("ce77c56f-052f-511b-a375-ae9b026f1492", "Bernard E Strozenski", "754"),
}

# Edmund I. Stromholt already has a completed, high-confidence, sourced outcome.
# Batch 925 deliberately leaves that record untouched.
PRESERVED_ROWS = {9}

ARMY_IDENTITIES = {
    1: {"entry": "1943-01-29", "grade": "PVT", "variant": "Charlie E Stringer Jr."},
    2: {"entry": "1946-03-13", "grade": "TEC5", "undefined_code": "055"},
    4: {"entry": "1941-07-10", "grade": "PVT"},
    6: {"entry": "1941-12-05", "grade": "PVT", "variant": "Anthony J Strobl Jr."},
    13: {"entry": "1942-11-11", "grade": "PVT"},
    15: {"entry": "1942-04-27", "grade": "PVT"},
    22: {"entry": "1944-07-03", "grade": "P0T", "variant": "Bernard B Strozeski"},
}

ARMY_OCCUPATIONS = {
    1: {
        "code": "794",
        "occupation": "Machinists' apprentices",
        "relationship": "employment",
        "locator": "PDF physical page 175; historical category 7-94",
    },
    4: {
        "code": "753",
        "occupation": "Servicemen and linemen, telegraph, telephone, and power",
        "relationship": "employment",
        "locator": "PDF physical pages 174 and 304; historical category 7-53",
    },
    6: {
        "code": "044",
        "occupation": "Commercial artists",
        "relationship": "employment",
        "locator": "PDF physical page 171; historical category 0-44",
    },
    13: {
        "code": "992",
        "occupation": "Students",
        "relationship": "student",
        "locator": "PDF physical page 304; amended historical category 9-92",
    },
    15: {
        "code": "044",
        "occupation": "Commercial artists",
        "relationship": "employment",
        "locator": "PDF physical page 171; historical category 0-44",
    },
    22: {
        "code": "992",
        "occupation": "Students",
        "relationship": "student",
        "locator": "PDF physical page 304; amended historical category 9-92",
    },
}

UNRESOLVED = {
    3: "Exact-name, OSS, occupation, obituary, institutional, newspaper, directory and archival searches found no corroborating identifier or defensible pre-OSS affiliation.",
    7: "Exact-name and variant searches found no reliable OSS identity bridge, employer, occupation or institution.",
    8: "Exact-name and middle-initial searches found no person-specific source tied to OSS or Box 753.",
    11: "Common-name searches produced no two-identifier bridge to the Box 753 person and no defensible pre-OSS affiliation.",
    12: "Common-name and middle-initial searches produced no person-specific source tied to OSS or Box 754.",
    16: "Exact-name searches produced no corroborating identifier or reliable employment evidence for the Box 754 person.",
    17: "The rendered index page confirms the printed spelling Jaunita; searches of Jaunita, Juanita and initials found no defensible identity bridge.",
    18: "Common-name and middle-initial searches produced no second identifier or Box 754 bridge.",
    19: "The protected index value did not produce a defensible public identity bridge; common-name searches were insufficient.",
    23: "No external source distinguishes Bernard E. Strozenski from the adjacent Bernard B. Strozenski row; the two source records remain separate.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def duplicate_group(key: str) -> str:
    return str(uuid.uuid5(uuid.NAMESPACE_URL, f"before-oss:{key}"))


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 753-754",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 453, rows 1-23; checked against layout-preserving text and rendered page images",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. Full identifiers remain private. The printed row reads Jaunita H Strosnider. Edmund I Stromholt's earlier reviewed outcome is preserved unchanged.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; seven accepted Batch 925 protected-identifier candidates",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "No raw row or full protected identifier is retained in public assets. Code 055 is not assigned a label; damaged grade P0T is not normalized. Coded occupations identify no employer.",
        },
        {
            "key": TECH,
            "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf",
            "archival_identifier": "NN3-064-03-008; National Archives Identifier 1263923",
            "title": "World War II Army Enlistment Records: Reference Copy of Technical Documentation",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives at College Park - Electronic Records",
            "publication_record_date": "1994-2005; reference copy modified 2011",
            "locator": "PDF physical pages 44-46; identifier, name, Army-entry-date, grade and civilian-occupation fields",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Used to interpret selected fields only; source damage, coding limits and incomplete coverage remain applicable.",
        },
        {
            "key": CODES,
            "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1CL_SD.pdf",
            "archival_identifier": "National Archives Identifier 1263923; Code No. 30",
            "title": "NARA Compiled Code Lists for the Electronic Army Serial Number Merged File",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives at College Park - Electronic Records",
            "publication_record_date": "2011-01-12; modified 2011-03-17",
            "locator": "PDF physical pages 171-175 and 304; Batch 925 categories visually checked",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical categories identify neither employer nor workplace. Code 055 is absent from the reviewed list and remains uninterpreted.",
        },
        {
            "key": ART_BIN,
            "stable_url": "https://www.art-bin.com/art/strobleng.html",
            "title": "The classic Donald Duck of Tony Strobl",
            "author_creator": "Anders Berglund; translated by Henrik Nordström",
            "repository_publisher": "The Art Bin",
            "publication_record_date": "Based on 1983 article and 1988 published interview",
            "locator": "Biographical paragraphs 4-6; references list",
            "access_date": "2026-10-26",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "rights_notes": "The article identifies Anthony Joseph Strobl, his December 1938 Disney start, specific film work and draft into the Army; it cites a published interview with Strobl.",
        },
        {
            "key": NIA,
            "source_id": "cb35d744-a689-5c7e-8cb2-e9e9adbeee02",
            "stable_url": "https://www.nia.no/en/the-saboteurs/",
            "title": "The heroes of Telemark",
            "author_creator": "Norsk Industriarbeidermuseum",
            "repository_publisher": "Norsk Industriarbeidermuseum",
            "locator": "Biographical entries for Jens-Anton Poulsson and Birger Strømsheim",
            "access_date": "2026-10-26",
            "source_quality": "B_authoritative_institutional",
            "rights_notes": "The museum identifies Strømsheim's prewar construction-contracting work, 1941 flight with his wife, and enlistment in Norwegian Independent Company 1. Public excerpts remain below 25 words.",
        },
        {
            "key": PRAIRIE,
            "stable_url": "https://www.cchsm.com/resources/newspapers/1940/pf_sf_v1_1943_44.pdf",
            "title": "Officer Profiles: Major Harry D. Strouse",
            "author_creator": "Prairie Flier staff",
            "repository_publisher": "Prairie Flier, Strother Army Air Field; digitized by Cowley County Historical Society Museum",
            "publication_record_date": "1943-09-10",
            "locator": "PDF physical page 93, printed page 3",
            "access_date": "2026-10-26",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "rights_notes": "Contemporary profile of Major Harry D. Strouse. It describes prewar self-employment and sales work but cannot be assigned to the unranked index row without another identifier.",
        },
        {
            "key": SCOTTISH_RITE,
            "stable_url": "https://scottishritechicago.org/wp-content/uploads/2018/12/2008-Summer.pdf",
            "title": "In Memoriam: Harry Dunlap Strouse, Jr.",
            "author_creator": "Valley of Chicago",
            "repository_publisher": "Scottish Rite Valley of Chicago",
            "publication_record_date": "2008",
            "locator": "Summer 2008 issue; memorial for Harry Dunlap Strouse, Jr.",
            "access_date": "2026-10-26",
            "source_quality": "B_authoritative_institutional",
            "rights_notes": "The memorial identifies a distinct Harry D. Strouse Jr., born 1923, who served as a wartime cryptographer. The unranked index row does not distinguish father from son.",
        },
        {
            "key": ARMY_REGISTER,
            "stable_url": "https://www.archives.gov/files/foia/pdf/nprc-crg-part4-508.pdf",
            "title": "Official Army Register, 1942",
            "author_creator": "Adjutant General's Office, War Department",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1942",
            "locator": "Printed page 976; retirement list",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "rights_notes": "The register lists Lieutenant Colonel Sherman I. Strong, Quartermaster Corps, retired June 30, 1942. The index row has no rank or identifier, so the candidate is not assigned.",
        },
        {
            "key": ARMY_REVIEW,
            "stable_url": "https://www.armyupress.army.mil/Portals/7/military-review/Archives/English/100-Landing/Topics-Interest/Deployments/docs/World-War-II-1945.pdf",
            "title": "Rescue by the Rangers",
            "author_creator": "Captain Ray M. Stroupe, Infantry",
            "repository_publisher": "Military Review; U.S. Army University Press",
            "publication_record_date": "1945",
            "locator": "Author byline and staff-and-faculty identification",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "rights_notes": "The official publication identifies an exact-name Army captain, but the unranked index row supplies no second identifier. The candidate remains unassigned.",
        },
        {
            "key": AFSA,
            "stable_url": "https://afsa.org/sites/default/files/fsj-1953-06-june_0.pdf",
            "title": "The Foreign Service Journal, June 1953",
            "author_creator": "American Foreign Service Association",
            "repository_publisher": "American Foreign Service Association",
            "publication_record_date": "1953-06",
            "locator": "PDF physical page 61; Foreign Service changes",
            "access_date": "2026-10-26",
            "source_quality": "B_authoritative_institutional",
            "rights_notes": "The postwar roster places Harry R. Stritman at Rome and then the Department. It supports a namesake lead, not a pre-OSS employer.",
        },
        {
            "key": QUANTICO,
            "stable_url": "https://www.interment.net/united-states/virginia/prince-william-county/triangle/national-memorial-cemetery-at-quantico/transcription/955.php?page=364",
            "title": "National Memorial Cemetery at Quantico transcription",
            "author_creator": "Interment.net contributors",
            "repository_publisher": "Interment.net",
            "publication_record_date": "database entry accessed 2026",
            "locator": "Harry R. Stritman entry; Section 23, Site 1300",
            "access_date": "2026-10-26",
            "source_quality": "D_correlative_or_secondary",
            "rights_notes": "The transcription identifies a Harry R. Stritman as a World War II Army major. It is corroborative only and does not establish the indexed identity.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": "walt-disney-studios-b925",
            "organization_id": "2ea94105-71c7-5971-9d2e-23dfe8097e3f",
            "canonical_name": "Walt Disney Studios",
            "historical_name": "Walt Disney Studios",
            "aliases": ["Disney"],
            "organization_type": "film studio",
            "sector": "arts_and_culture",
            "city": "Burbank",
            "state_or_region": "California",
            "country": "United States",
            "normalization_notes": "Existing canonical organization reused. Historical employer wording is preserved; no modern successor substitution is implied.",
        },
        {
            "key": "norwegian-independent-company-1-b925",
            "organization_id": "0ad15737-f33c-5d8c-b93d-c9a96833563e",
            "canonical_name": "Norwegian Independent Company 1",
            "historical_name": "Norwegian Independent Company 1",
            "aliases": ["Kompani Linge", "Norwegian Independent Company No. 1"],
            "organization_type": "Norwegian special operations unit",
            "sector": "military",
            "country": "United Kingdom",
            "active_dates": "1941-1945",
            "normalization_notes": "Existing canonical organization reused. Historical aliases are preserved; separate source evidence controls each person's dates and relationship.",
        },
    ]


def affiliations() -> list[dict[str, object]]:
    result: list[dict[str, object]] = []
    for row, data in ARMY_OCCUPATIONS.items():
        result.append(
            {
                "key": f"{slug(PEOPLE[row][1])}-occupation-b925",
                "person_id": PEOPLE[row][0],
                "occupation": data["occupation"],
                "relationship_type": data["relationship"],
                "end_date": ARMY_IDENTITIES[row]["entry"],
                "date_precision": f"Historical civilian-occupation code {data['code']} was recorded at Army entry on {ARMY_IDENTITIES[row]['entry']}; no employer, school, workplace or OSS-transfer date is named.",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "A_direct_official",
                "publication_status": "publish_qualified",
                "research_notes": "The historical category is not converted into a named employer, school, institution, workplace or exact job title.",
            }
        )
    result.extend(
        [
            {
                "key": "anthony-strobl-disney-b925",
                "person_id": PEOPLE[6][0],
                "organization_key": "walt-disney-studios-b925",
                "organization_name_as_found": "Disney studio",
                "role_title": "in-betweener and animator",
                "occupation": "commercial artist and animator",
                "relationship_type": "employment",
                "start_date": "1938-12",
                "end_date": "1941-12-05",
                "date_precision": "The biography dates his first Disney assignment to December 1938 and says Disney film work preceded his Army draft; the official Army row dates entry to 1941-12-05.",
                "city": "Burbank",
                "state_or_region": "California",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "published",
                "research_notes": "This is the last documented civilian employer before Army service. It is not labeled the immediate OSS predecessor because Army service intervened.",
            },
            {
                "key": "birger-stromsheim-contractor-b925",
                "person_id": PEOPLE[10][0],
                "organization_name_as_found": "self-employed construction contractor",
                "role_title": "construction contractor",
                "occupation": "construction contractor",
                "relationship_type": "self_employment",
                "end_date": "1941",
                "date_precision": "The museum says he worked as a construction contractor before the war and fled Norway in 1941; no start or exact end date is supplied.",
                "city": "Ålesund",
                "country": "Norway",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "probable",
                "claim_confidence": "medium",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "publish_qualified",
                "research_notes": "Qualified as the last identifiable civilian role before wartime service, not an explicitly immediate predecessor to OSS. The person match remains probable pending Box 753 review.",
            },
            {
                "key": "birger-stromsheim-nic1-b925",
                "person_id": PEOPLE[10][0],
                "organization_key": "norwegian-independent-company-1-b925",
                "organization_name_as_found": "Norwegian Independent Company 1",
                "role_title": "sergeant and saboteur",
                "relationship_type": "military_assignment",
                "start_date": "1941",
                "end_date": "1944",
                "date_precision": "The museum dates flight to Shetland and joining the unit to 1941 and documents operations through March 1944; it does not give an OSS transfer date.",
                "country": "United Kingdom",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "temporal_relation_uncertain",
                "identity_confidence": "probable",
                "claim_confidence": "medium",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "publish_qualified",
                "research_notes": "Documented wartime military affiliation. It is not labeled immediate to OSS because no reviewed source states the OSS relationship or transfer sequence.",
            },
        ]
    )
    return result


def army_identity_claim(row: int) -> dict[str, object]:
    name = PEOPLE[row][1]
    data = ARMY_IDENTITIES[row]
    if row == 22:
        assessment = "High confidence: the protected identifier is nonshared and exact; the one-letter Strozenski/Strozeski spelling discrepancy is preserved."
        notes = "The damaged grade code P0T is not normalized, and the adjacent Bernard E. Strozenski remains a separate person."
    else:
        assessment = "High confidence from the exact or compatible full name and a nonshared protected identifier."
        notes = "The protected identifier is withheld from public data; no employer or OSS assignment is inferred from the Army row."
    return {
        "key": f"identity-{slug(name)}-b925",
        "person_id": PEOPLE[row][0],
        "claim_type": "identity",
        "claim_text": f"The indexed {name} is a high-confidence match to an official Army record dated {data['entry']}; the protected identifier is withheld.",
        "evidence_paraphrase": f"The reviewed Army row agrees in name and a nonshared protected identifier and records grade {data['grade']} at Army entry.",
        "identity_match_assessment": assessment,
        "temporal_assessment": "The date is Army entry, not an OSS assignment date or proof of an immediate pre-OSS affiliation.",
        "source_quality": "A_direct_official",
        "claim_confidence": "high",
        "publication_status": "published",
        "match_notes": notes,
        "sources": [
            {"source_key": INDEX, "locator_override": f"PDF page 453 row {row}; Box {PEOPLE[row][2]}; protected value withheld"},
            {"source_key": ARMY, "locator_override": "Accepted reviewed identity record; protected identifier withheld"},
            {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46; identifier, name, date and grade fields"},
        ],
    }


def army_occupation_claim(row: int) -> dict[str, object]:
    name = PEOPLE[row][1]
    data = ARMY_OCCUPATIONS[row]
    occupation = data["occupation"]
    if occupation == "Students":
        text = f"At Army entry on {ARMY_IDENTITIES[row]['entry']}, {name} was recorded in the historical occupation group Students; no school or employer is identified."
    else:
        text = f"At Army entry on {ARMY_IDENTITIES[row]['entry']}, {name} was recorded in the historical occupation category {occupation}; no employer is identified."
    return {
        "key": f"occupation-{slug(name)}-b925",
        "person_id": PEOPLE[row][0],
        "affiliation_key": f"{slug(name)}-occupation-b925",
        "claim_type": "occupation",
        "claim_text": text,
        "evidence_excerpt": occupation,
        "evidence_paraphrase": f"The accepted Army record carries civilian-occupation code {data['code']}, decoded from NARA's official code list.",
        "identity_match_assessment": "The category belongs only to the reviewed protected-identifier match; the identifier itself is not public.",
        "temporal_assessment": "Dated to Army entry; it does not establish an immediate pre-OSS affiliation or named employer.",
        "source_quality": "A_direct_official",
        "claim_confidence": "medium",
        "publication_status": "publish_qualified",
        "match_notes": "The historical category is a qualified lead, not a named employer, school, institution, workplace or exact title.",
        "sources": [
            {"source_key": ARMY, "locator_override": f"Accepted reviewed identity record; civilian occupation code {data['code']}; protected identifier withheld"},
            {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46; Army-entry-date and civilian-occupation fields"},
            {"source_key": CODES, "locator_override": data["locator"], "excerpt_override": occupation},
        ],
    }


def claims() -> list[dict[str, object]]:
    result = [army_identity_claim(row) for row in ARMY_IDENTITIES]
    result.extend(army_occupation_claim(row) for row in ARMY_OCCUPATIONS)
    result.extend(
        [
            {
                "key": "last-civilian-anthony-strobl-disney-b925",
                "person_id": PEOPLE[6][0],
                "affiliation_key": "anthony-strobl-disney-b925",
                "claim_type": "last_civilian_pre_service",
                "claim_text": "Anthony J. Strobl worked at Walt Disney Studios as an in-betweener and animator from December 1938 until Army service in December 1941, making Disney his last documented civilian employer before service.",
                "evidence_excerpt": "In December 1938 he began his first assignment",
                "evidence_paraphrase": "The biography identifies Anthony Joseph Strobl, dates his Disney start, names film work, and says he was then drafted; the Army row independently dates entry and codes commercial artist.",
                "identity_match_assessment": "High confidence from the exact protected-identifier Army bridge, matching full name, Jr. variant, dated transition and matching commercial-artist occupation.",
                "temporal_assessment": "Strongly date-bounded from December 1938 to Army entry on 1941-12-05. Army service intervened before OSS, so this is not an immediate OSS affiliation.",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "The historical studio name is preserved. The claim is included in last-civilian-employer analytics, not immediate-affiliation analytics.",
                "sources": [
                    {"source_key": ART_BIN, "locator_override": "Biographical paragraphs 4-6 and references"},
                    {"source_key": ARMY, "support_type": "context_only", "locator_override": "Accepted reviewed identity record; Army entry 1941-12-05; occupation code 044"},
                    {"source_key": CODES, "support_type": "context_only", "locator_override": "PDF physical page 171; category 0-44", "excerpt_override": "Commercial artists"},
                ],
            },
            {
                "key": "identity-birger-stromsheim-b925",
                "person_id": PEOPLE[10][0],
                "claim_type": "identity",
                "claim_text": "The indexed Birger Stromsheim is a probable match to Norwegian resistance member Birger Strømsheim, but Box 753 has not been reviewed for a second biographical identifier.",
                "evidence_excerpt": "Birger Strømsheim is from Ålesund",
                "evidence_paraphrase": "The museum gives the distinctive diacritic spelling, Ålesund origin, wartime Norwegian Independent Company 1 service and Gunnerside chronology.",
                "identity_match_assessment": "Probable from the rare exact name, index context and highly specific wartime special-operations biography; not high confidence because the index supplies no rank, nationality or service number.",
                "temporal_assessment": "The museum documents prewar work and 1941-1944 wartime service; it does not state an OSS assignment or transfer.",
                "source_quality": "B_authoritative_institutional",
                "claim_confidence": "medium",
                "publication_status": "publish_qualified",
                "match_notes": "The famous biography is not treated as settled solely on the name. Box 753 review remains required.",
                "sources": [
                    {"source_key": INDEX, "locator_override": "PDF page 453 row 10; Box 753"},
                    {"source_key": NIA, "locator_override": "Birger Strømsheim biographical entry"},
                ],
            },
            {
                "key": "prewar-birger-stromsheim-contractor-b925",
                "person_id": PEOPLE[10][0],
                "affiliation_key": "birger-stromsheim-contractor-b925",
                "claim_type": "last_civilian_pre_service",
                "claim_text": "On the probable identity match, Birger Strømsheim worked as a construction contractor before the war; this is his last identifiable civilian role before wartime service, not a proven immediate OSS predecessor.",
                "evidence_excerpt": "works as a construction contractor before the war",
                "evidence_paraphrase": "The museum explicitly names the prewar occupation and then dates his flight to Shetland and wartime unit membership to 1941.",
                "identity_match_assessment": "Probable, not settled, for the reasons stated in the identity claim.",
                "temporal_assessment": "Documented prewar. The source does not establish exact dates or exclude an intervening civilian role before 1941.",
                "source_quality": "B_authoritative_institutional",
                "claim_confidence": "medium",
                "publication_status": "publish_qualified",
                "match_notes": "Self-employment is not normalized into an invented company. Excluded from default confirmed/high employer analytics.",
                "sources": [{"source_key": NIA, "locator_override": "Birger Strømsheim biographical entry"}],
            },
            {
                "key": "wartime-birger-stromsheim-nic1-b925",
                "person_id": PEOPLE[10][0],
                "affiliation_key": "birger-stromsheim-nic1-b925",
                "claim_type": "other_pre_oss_affiliation",
                "claim_text": "On the probable identity match, Strømsheim joined Norwegian Independent Company 1 after reaching England in 1941; its temporal relationship to OSS is unverified.",
                "evidence_excerpt": "he joins Norwegian Independent Company 1",
                "evidence_paraphrase": "The museum sequences the 1941 escape, arrival in England, unit membership and later Gunnerside and Fjeldfare operations.",
                "identity_match_assessment": "Probable and qualified pending Box 753 review.",
                "temporal_assessment": "Documented wartime military affiliation; no reviewed source states an OSS transfer date or immediate predecessor relationship.",
                "source_quality": "B_authoritative_institutional",
                "claim_confidence": "medium",
                "publication_status": "publish_qualified",
                "match_notes": "Military affiliation, not civilian employment; excluded from immediate-affiliation analytics.",
                "sources": [{"source_key": NIA, "locator_override": "Birger Strømsheim biographical entry"}],
            },
            {
                "key": "identity-harry-d-strouse-conflict-b925",
                "person_id": PEOPLE[21][0],
                "claim_type": "identity",
                "claim_text": "The unranked Harry D. Strouse index row cannot yet be assigned between Major Harry D. Strouse and his son, wartime cryptographer Harry Dunlap Strouse Jr.",
                "evidence_paraphrase": "A contemporary Army newspaper profiles the father as a major with prewar business experience; a later institutional memorial identifies the same-named son as a 1944-1945 cryptographer.",
                "identity_match_assessment": "Conflicting: both candidates match the indexed initials, and the index supplies no rank, suffix, service number, birth year or unit.",
                "temporal_assessment": "Both candidates have wartime service, but neither may transfer employment or education facts to the index profile without Box 754 evidence.",
                "source_quality": "B_authoritative_institutional",
                "claim_confidence": "conflicting",
                "publication_status": "conflicting",
                "match_notes": "Both alternatives remain visible; the father's oil-burner and self-employment history is not published as the indexed person's prehistory.",
                "sources": [
                    {"source_key": INDEX, "locator_override": "PDF page 453 row 21; Box 754"},
                    {"source_key": PRAIRIE, "locator_override": "PDF physical page 93, printed page 3; Major Harry D. Strouse"},
                    {"source_key": SCOTTISH_RITE, "support_type": "contradicts", "locator_override": "Harry Dunlap Strouse Jr. memorial"},
                ],
            },
            {
                "key": "identity-sherman-i-strong-candidate-b925",
                "person_id": PEOPLE[14][0],
                "claim_type": "identity",
                "claim_text": "A 1942 Army Register entry for Lieutenant Colonel Sherman I. Strong is an unassigned namesake candidate for the index row.",
                "evidence_paraphrase": "The official register identifies an exact-name Quartermaster Corps lieutenant colonel and a June 30, 1942 retirement date.",
                "identity_match_assessment": "Low: exact name only. The index supplies no rank, service number, branch or other corroborating identifier.",
                "temporal_assessment": "The retirement date may precede OSS service, but no sequence is established.",
                "source_quality": "A_direct_official",
                "claim_confidence": "low",
                "publication_status": "withheld_low_confidence",
                "match_notes": "Preserved as a private candidate lead; no military assignment or employer is transferred.",
                "sources": [{"source_key": ARMY_REGISTER, "locator_override": "Printed page 976; June 30, 1942 retirement list"}],
            },
            {
                "key": "identity-ray-m-stroupe-candidate-b925",
                "person_id": PEOPLE[20][0],
                "claim_type": "identity",
                "claim_text": "An official 1945 article by Captain Ray M. Stroupe, Infantry, is an unassigned namesake candidate for the index row.",
                "evidence_paraphrase": "Military Review identifies the author as an Infantry captain on the Command and General Staff School staff and faculty.",
                "identity_match_assessment": "Low: exact name and wartime Army context, but the index supplies no rank, branch, service number or other corroborating identifier.",
                "temporal_assessment": "The 1945 role's sequence relative to OSS is unknown.",
                "source_quality": "A_direct_official",
                "claim_confidence": "low",
                "publication_status": "withheld_low_confidence",
                "match_notes": "Preserved as a private lead only; no assignment is transferred.",
                "sources": [{"source_key": ARMY_REVIEW, "locator_override": "Author byline and staff-and-faculty identification"}],
            },
            {
                "key": "identity-harry-r-stritman-candidate-b925",
                "person_id": PEOPLE[5][0],
                "claim_type": "identity",
                "claim_text": "Postwar Foreign Service and cemetery records provide a probable Harry R. Stritman namesake, but do not yet bridge the index captain to pre-OSS employment.",
                "evidence_paraphrase": "The index gives Captain; the cemetery transcription gives a World War II Army major; the Foreign Service Journal gives a postwar Rome-to-Department transfer.",
                "identity_match_assessment": "Probable from the rare exact name and compatible wartime rank progression, but no service number or direct personnel-file bridge was reviewed.",
                "temporal_assessment": "The Foreign Service evidence is postwar and cannot establish pre-OSS employment.",
                "source_quality": "B_authoritative_institutional",
                "claim_confidence": "low",
                "publication_status": "withheld_low_confidence",
                "match_notes": "The candidate remains private pending Box 753 review; no postwar role is presented as prewar employment.",
                "sources": [
                    {"source_key": INDEX, "locator_override": "PDF page 453 row 5; Captain; Box 753; protected value withheld"},
                    {"source_key": QUANTICO, "support_type": "context_only", "locator_override": "Harry R. Stritman; World War II Army major"},
                    {"source_key": AFSA, "support_type": "context_only", "locator_override": "PDF physical page 61; 1953 Rome-to-Department transfer"},
                ],
            },
        ]
    )
    return result


def archival_update(row: int, reason: str) -> dict[str, object]:
    person_id, name, box = PEOPLE[row]
    update: dict[str, object] = {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, Box {box} and archive location, but staged official, OSS, employment, occupation, obituary, institutional, newspaper, directory and archival searches found no defensible identity bridge. {reason}",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": f"Review Box {box} for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "critical",
    }
    return update


def person_updates() -> list[dict[str, object]]:
    updates = [archival_update(row, reason) for row, reason in UNRESOLVED.items()]
    bernard_group = duplicate_group("bernard-b-e-strozenski-b925")
    for update in updates:
        if update["person_id"] == PEOPLE[23][0]:
            update["identity_status"] = "ambiguous"
            update["possible_duplicate_group"] = bernard_group

    for row, data in ARMY_IDENTITIES.items():
        name = PEOPLE[row][1]
        occupation = ARMY_OCCUPATIONS.get(row, {}).get("occupation")
        if row == 22:
            evidence = "A nonshared protected identifier links the indexed Bernard B Strozenski to an official Army row spelling the surname Strozeski. The one-letter discrepancy and damaged grade P0T remain visible."
        else:
            evidence = "An exact or compatible full name and nonshared protected identifier connect the index row to the official Army record."
        next_action = (
            f"Review Box {PEOPLE[row][2]} for the immediate pre-OSS affiliation and last civilian employer; official code 055 is not interpreted, and the 1946 Army-entry date does not establish pre-OSS chronology."
            if row == 2
            else f"Review Box {PEOPLE[row][2]} for the immediate pre-OSS affiliation and named employer; do not convert the historical category '{occupation}' into an employer or institution."
        )
        update: dict[str, object] = {
            "person_id": PEOPLE[row][0],
            "identity_status": "high_confidence",
            "identity_evidence": evidence,
            "personnel_category": "enlisted_army_personnel",
            "commissioned_officer": False,
            "allied_or_foreign_personnel": False,
            "manual_review_required": True,
            "research_status": "verified_employer_found" if row == 6 else ("occupation_only_found" if row in ARMY_OCCUPATIONS else "requires_archival_review"),
            "next_action": next_action if row != 6 else "The last civilian Walt Disney Studios employment is established. Review Box 753 for the Army-to-OSS transfer and exact OSS assignment.",
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
            "archival_review_priority": "medium" if row == 6 else "high",
        }
        if data.get("variant"):
            update["name_variants"] = [str(data["variant"])]
        if row == 6:
            update["name_variants"] = ["Anthony Joseph Strobl", "Tony Strobl", str(data["variant"])]
        if row == 22:
            update["possible_duplicate_group"] = bernard_group
        updates.append(update)

    updates.extend(
        [
            {
                "person_id": PEOPLE[5][0],
                "identity_status": "probable",
                "identity_evidence": "The rare exact name, index rank Captain, a World War II Army-major cemetery transcription and postwar Foreign Service record are compatible, but no direct service-number or Box 753 bridge was reviewed.",
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Review Box 753 for service number, birth date, unit, Army-to-OSS sequence and any prewar occupation. Do not infer prewar employment from the postwar Foreign Service record.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[10][0],
                "identity_status": "probable",
                "identity_evidence": "The rare exact name, OSS-index context and museum-documented Norwegian special-operations chronology support a probable match to Birger Strømsheim; the index supplies no second biographical identifier.",
                "name_variants": ["Birger Strømsheim", "Birger Edvin Martin Strømsheim"],
                "personnel_category": "foreign_or_allied_military_personnel",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": True,
                "manual_review_required": True,
                "research_status": "documented_prewar_employer_found",
                "next_action": "Review Box 753 for a second identifier, exact OSS relationship and transfer chronology. The construction-contracting role remains qualified until that identity bridge is confirmed.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[14][0],
                "identity_status": "ambiguous",
                "identity_evidence": "The official Army Register exact-name lieutenant-colonel is plausible, but the index row supplies no rank, service number, branch or second identifier. No facts were transferred.",
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Review Box 754 for rank, branch, service number or birth data before assigning the Quartermaster Corps lieutenant-colonel candidate or any pre-OSS military pathway.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[20][0],
                "identity_status": "ambiguous",
                "identity_evidence": "An official 1945 article identifies an exact-name Infantry captain on the Command and General Staff School staff, but the index row supplies no rank or corroborating identifier.",
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Review Box 754 for rank, branch, service number and OSS chronology before assigning the Captain Ray M. Stroupe candidate or any military affiliation.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[21][0],
                "identity_status": "conflicting",
                "identity_evidence": "The unranked index row could refer to Major Harry D. Strouse or his son Harry Dunlap Strouse Jr., a wartime cryptographer. Both match the initials and neither has a second index identifier.",
                "manual_review_required": True,
                "research_status": "conflicting_sources",
                "next_action": "Review Box 754 for rank, suffix, birth year, service number or unit. Do not transfer the father's business career or the son's education and cryptography service until the person is resolved.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
        ]
    )
    return updates


def research_attempts() -> list[dict[str, object]]:
    attempts: list[dict[str, object]] = []
    for row, (person_id, name, box) in PEOPLE.items():
        if row in PRESERVED_ROWS:
            continue
        if row == 6:
            outcome = "source_reviewed"
            detail = "An accepted Army identity bridge and a published interview-based biography establish high-confidence identity, Walt Disney Studios employment from 1938 to Army entry, and commercial-artist occupation."
            reviewed, rejected = 9, 3
        elif row == 10:
            outcome = "source_reviewed"
            detail = "A museum biography establishes construction-contracting work and Norwegian Independent Company 1 service for a probable rare-name match; the identity remains qualified pending Box 753 review."
            reviewed, rejected = 8, 3
        elif row == 21:
            outcome = "candidate_found"
            detail = "A contemporary Army profile of Major Harry D. Strouse and an institutional memorial for Harry Dunlap Strouse Jr. create a two-candidate conflict that the unranked index row cannot resolve."
            reviewed, rejected = 8, 2
        elif row in {5, 14, 20}:
            outcome = "candidate_found"
            detail = {
                5: "Compatible wartime-rank and postwar Foreign Service records support a probable namesake, but no direct service-number or Box 753 bridge establishes pre-OSS employment.",
                14: "An official Army Register exact-name candidate lacks a second identifier and remains unassigned.",
                20: "An official 1945 exact-name Army captain candidate lacks a second identifier and remains unassigned.",
            }[row]
            reviewed, rejected = 7, 4
        elif row in ARMY_IDENTITIES:
            outcome = "source_reviewed"
            if row == 2:
                detail = "An accepted protected-identifier Army bridge establishes identity and a 1946 Army entry, but official code 055 is undefined and no occupation or employer was inferred."
            else:
                detail = f"An accepted protected-identifier Army bridge establishes identity and the dated historical category {ARMY_OCCUPATIONS[row]['occupation']}, but no named employer or institution."
            reviewed, rejected = 6, 3
        else:
            outcome = "no_result"
            detail = UNRESOLVED[row]
            reviewed, rejected = 5, 3
        attempts.append(
            {
                "key": f"page453-row{row}-{slug(name)}-b925",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA/index and public Archives context; CIA Reading Room site-restricted exact-name check; OSS and rank variants; employer and occupation; obituary, institutional, newspaper, directory and archival searches; Box {box}; protected-identifier Army crosswalk where defensible",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_925",
                "started_at": "2026-10-26T11:45:00Z",
                "completed_at": "2026-10-27T02:12:00Z",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, discovery-only genealogy or people-finder results, wrong initials, postwar-only leads and sources without an OSS or Box-file bridge were not assigned.",
                "research_notes": f"{detail} Official Army code pages and the index page were visually checked. No search snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA API call was made.",
                "next_action": f"Review Box {box} for corroborating identifiers and the immediate pre-OSS affiliation or last civilian employer.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b925-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-925-v1",
        "reviewer": "Before OSS Batch 925 evidence review",
        "sources": sources(),
        "organizations": organizations(),
        "affiliations": affiliations(),
        "claims": claims(),
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }
    OUTPUT.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
