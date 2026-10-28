#!/usr/bin/env python3
"""Generate the reviewed Batch 936 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / (
    "research/evidence-page458-edward-d-sybesma-to-stanley-f-szalamacha-"
    "review_batch-936_2026-10-27.json"
)

INDEX = "nara-index-b936"
ARMY_SOURCE = "army-bulk-b936"
TECH = "army-tech-b936"
CODES = "army-codes-b936"
SYPESTEYN_COMMENDATION = "sypesteyn-oss-commendation-b936"
SYPHAX_OBITUARY = "syphax-washington-post-b936"
SYRO_TREASURY = "syro-boiarsky-treasury-memo-b936"
SYRSTAD_ND = "syrstad-north-dakota-register-b936"
SYRSTAD_DPL = "syrstad-denver-roster-b936"
SYRSTAD_NORSO = "syrstad-norso-ii-b936"

PEOPLE = {
    24: ("418b8496-43ce-5d57-ba83-66846184d412", "Edward D Sybesma"),
    25: ("2a52849b-107a-5323-8ac2-cd904d10d7d7", "George M Sylvester"),
    26: ("1ba6a73b-384d-529d-b0be-98ffaa474216", "Loren H Sylvester"),
    27: ("d51e9ca8-2451-55db-9884-0a4087d89e78", "Richard C Sylvester"),
    28: ("f344b7eb-15cf-5e29-be0b-560a0944bbd2", "Stephen J Symanski"),
    29: ("16ec2597-787b-5430-bb98-b83c28508d64", "Louise Syminyon"),
    30: ("edb4cff2-1aef-52ac-bb58-a19115af6e2c", "Percival M Symonds"),
    31: ("0faa01df-72cc-5ec9-9ba0-73347161a55a", "Sidney L Symons"),
    32: ("125350a5-bab1-5917-81c2-7a28a22f794d", "Fryderyk Synowiec"),
    33: ("102b2653-669a-5c85-8d6f-b90832a06d73", "Willem K Sypesteyn"),
    34: ("74c91ced-6cbb-50e5-a9e8-a907707b21ec", "William K Sypesteyn"),
    35: ("100e38c5-bc8e-5fca-80b6-be988adcb44a", "John W Syphax"),
    36: ("04556319-8777-5a62-b9d7-7fe2ef158c19", "Ganna M Syro-Boiarsky"),
    37: ("75c7db38-481e-593b-a784-d054ebc68582", "Morris A Syrstad"),
    38: ("7a11d7e0-ee8f-5199-86e9-e5f4c99c5dc9", "Stephen J Sysko"),
    39: ("fcfea34a-7168-5376-b507-a09d9df29740", "Stevan J Sysko"),
    40: ("2273a4dd-11de-509c-9631-b3498cad2756", "Bertha B Syverud"),
    41: ("c38713db-05d0-5cf2-a5bd-6f1e7c5d50a8", "Kie Syzdek"),
    42: ("6e48695f-4e86-52d8-b1ae-2e754ca0bef5", "George M Szabad"),
    43: ("33908893-ab7a-5d9e-b705-c78866ae3f4e", "Kalman L Szabo"),
    44: ("1b13a8d4-f5f2-5bf6-8cc1-d144b498659e", "Kazmer J Szabo"),
    45: ("2dc317c8-8b94-56e3-9778-08d8d1c2e254", "Edward M Szachowicz"),
    46: ("3709a6cd-b7d5-5701-b630-8996171e1bf9", "Stanley F Szalamacha"),
}

SYPESTEYN_DUPLICATE_GROUP = "possible-same-person-willem-william-k-sypesteyn-box-762"
SYSKO_DUPLICATE_GROUP = "possible-same-person-stephen-stevan-j-sysko-box-762"

ARMY = {
    26: {
        "entry": "1941-03-27",
        "code": "138",
        "occupation": "Stock clerks",
        "locator": "PDF physical page 171; historical category 1-38",
    },
    33: {
        "entry": "1942-04-08",
        "code": "068",
        "occupation": "Semiprofessional occupations, n.e.c.",
        "locator": "PDF physical page 304; amended historical category 0-68",
    },
    39: {
        "entry": "1943-04-20",
        "code": "642",
        "occupation": "Occupations in manufacture of paper goods",
        "locator": "PDF physical page 173; historical category 4,6,8-42",
    },
    41: {
        "entry": "1942-04-25",
        "code": "401",
        "occupation": "Bakers",
        "locator": "PDF physical page 173; historical category 4-01",
    },
    42: {
        "entry": "1945-04-24",
        "code": "022",
        "occupation": "Lawyers and judges",
        "locator": "PDF physical page 171; historical category 0-22",
    },
}

UNRESOLVED = {
    24: "Search results concern a later Edward D. Sybesma Jr. and do not identify the indexed person.",
    25: "Exact-name military, employment, obituary and institutional searches supplied no Box 762 identity bridge.",
    27: "Exact-name military, employment, obituary and archival searches supplied no Box 762 identity bridge.",
    28: "A 44th Infantry Division roster lead matches the name but lacks a protected identifier, OSS transition or Box 762 bridge.",
    29: "Exact-name and spelling-variant searches supplied no defensible identity or pre-OSS affiliation evidence.",
    30: "Exact-name, occupation and archival searches supplied no defensible Box 762 identity bridge.",
    31: "Exact-name, OSS, obituary and institutional searches supplied no defensible Box 762 identity bridge.",
    32: "Exact-name, transliteration-variant and foreign-language searches supplied no defensible identity bridge.",
    34: "The similar Willem K Sypesteyn evidence is not transferred to this separately printed William K Sypesteyn row.",
    38: "The accepted Stevan/Steven J Sysko Army evidence is not transferred to this separately printed Stephen J Sysko row.",
    40: "Exact-name, military, employer, obituary and archival searches supplied no defensible identity bridge.",
    43: "A same-name obituary documents wartime Army service but lacks a protected identifier, OSS transition or Box 762 bridge.",
    44: "Exact-name and spelling-variant searches supplied no defensible Box 762 identity bridge.",
    45: "A 1940 amateur-radio directory lead supplies the exact name but no OSS, protected-identifier or Box 762 bridge.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Box 762",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 458, rows 24-46; checked against layout-preserving text and a rendered page image",
            "access_date": "2026-10-27",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. Full protected identifiers remain private. The printed note fragment on row 36 is preserved as printed.",
        },
        {
            "key": ARMY_SOURCE,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; six accepted and two conflicting Batch 936 identity candidates",
            "access_date": "2026-10-27",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "Accepted matches use nonshared protected identifiers. The Stanley F Szalamacha candidate is withheld because the identifier is shared by a differently named index row. No raw bulk row or full identifier is public.",
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
            "access_date": "2026-10-27",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Used to interpret selected fields only.",
        },
        {
            "key": CODES,
            "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1CL_SD.pdf",
            "archival_identifier": "National Archives Identifier 1263923; Code No. 30",
            "title": "NARA Compiled Code Lists for the Electronic Army Serial Number Merged File",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives at College Park - Electronic Records",
            "publication_record_date": "2011-01-12; modified 2011-03-17",
            "locator": "PDF physical pages 171, 173 and 304; categories 022, 068, 138, 401 and 642 visually checked",
            "access_date": "2026-10-27",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical labels identify neither a named employer nor a workplace. Undefined code 999 is not interpreted.",
        },
        {
            "key": SYPESTEYN_COMMENDATION,
            "stable_url": "https://www.archives.gov/files/research/jfk/releases/104-10165-10120.pdf",
            "archival_identifier": "NARA release 104-10165-10120",
            "title": "Recommendations for Awards and Decorations, OSS European Theater of Operations",
            "author_creator": "Headquarters and Headquarters Detachment, Office of Strategic Services, European Theater of Operations",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1945",
            "locator": "PDF physical page 82, printed page 4; corporal entry for Willem K. Sypesteyn and OSS citation",
            "access_date": "2026-10-27",
            "source_quality": "A_direct_official",
            "collection_name": "Office of Strategic Services records",
            "document_number": "104-10165-10120",
            "rights_notes": "The scanned page was visually inspected. The full protected identifier is not repeated in public evidence text.",
        },
        {
            "key": SYPHAX_OBITUARY,
            "stable_url": "https://www.washingtonpost.com/archive/local/1979/10/12/john-w-syphax-dies/717a3033-7bd9-4e35-9b4e-032f272ddb26/",
            "archival_identifier": "Washington Post obituary, 1979-10-12",
            "title": "John W. Syphax Dies: Retired Intelligence Officer at State",
            "repository_publisher": "The Washington Post",
            "publication_record_date": "1979-10-12",
            "locator": "Obituary paragraphs 2-3; Howard teaching dates and 1943-45 OSS biographic-analyst service",
            "access_date": "2026-10-27",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Washington Post archive",
            "rights_notes": "Only a short excerpt and project-authored paraphrase are retained. Education is not treated as employment.",
        },
        {
            "key": SYRO_TREASURY,
            "stable_url": "https://fraser.stlouisfed.org/archival-collection/diaries-henry-morgenthau-jr-6880/volume-397-634976/content/fulltext/morgenthau-diaries-0533",
            "archival_identifier": "Diaries of Henry Morgenthau, Jr., Volume 397, Part 1",
            "title": "Diaries of Henry Morgenthau, Jr.: Volume 397, Part 1",
            "author_creator": "United States Department of the Treasury; Henry Morgenthau Jr. papers",
            "repository_publisher": "FRASER, Federal Reserve Bank of St. Louis",
            "publication_record_date": "1941-05-14 memorandum",
            "locator": "Full-text lines 13993-14000; Treasury memorandum describing the 1940 Far East trip",
            "access_date": "2026-10-27",
            "source_quality": "A_direct_official",
            "collection_name": "Diaries of Henry Morgenthau, Jr.",
            "rights_notes": "Only the employment-relevant statement is retained. Unrelated investigative allegations and sensitive personal details are excluded.",
        },
        {
            "key": SYRSTAD_ND,
            "stable_url": "https://www.veterans.nd.gov/sites/www/files/documents/resource/S.pdf",
            "archival_identifier": "Register of North Dakota Veterans, S entries",
            "title": "Register of North Dakota Veterans: S",
            "author_creator": "State of North Dakota",
            "repository_publisher": "North Dakota Department of Veterans Affairs",
            "locator": "PDF physical page 188, printed page 1463; Morris A. Syrstad entry",
            "access_date": "2026-10-27",
            "source_quality": "A_direct_official",
            "collection_name": "Register of North Dakota Veterans",
            "rights_notes": "The official entry independently aligns the exact name, protected identifier, Army entry, theater and T/5 grade. The identifier is not public.",
        },
        {
            "key": SYRSTAD_DPL,
            "stable_url": "https://history.denverlibrary.org/sites/history/files/10th_mountain_index_0.pdf",
            "archival_identifier": "10th Mountain Division Name Index",
            "title": "Members of the 10th Mountain Division",
            "author_creator": "Denver Public Library Western History Department",
            "repository_publisher": "Denver Public Library",
            "publication_record_date": "database project begun 1998",
            "locator": "PDF physical page 896; Morris A Syrstad, Headquarters, 99th Infantry",
            "access_date": "2026-10-27",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "10th Mountain Division Resource Center",
            "rights_notes": "The index documents the unit assignment, not the individual transfer date to OSS or a civilian employer.",
        },
        {
            "key": SYRSTAD_NORSO,
            "stable_url": "https://ossog.info/norway/norso_02.html",
            "archival_identifier": "OSS Operational Groups NORSO II personnel roster",
            "title": "Office of Strategic Services Operational Groups: NORSO II",
            "author_creator": "Art Frizzell",
            "repository_publisher": "OSS Operational Groups",
            "locator": "NORSO II summary and personnel roster; T/5 Morris Syrstad",
            "access_date": "2026-10-27",
            "source_quality": "D_correlative_or_secondary",
            "collection_name": "OSS Operational Groups histories",
            "rights_notes": "The page states that its summary was compiled from National Archives records and Colby and Skabo reports. It corroborates OSS service but does not name a civilian employer.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": "army-existing-b936",
            "organization_id": "28a26f92-78af-5a1a-9c09-a843eb5975b4",
            "canonical_name": "United States Army",
            "historical_name": "Army of the United States",
            "aliases": ["U.S. Army", "Army"],
            "organization_type": "military service",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "Existing canonical organization reused.",
        },
        {
            "key": "howard-existing-b936",
            "organization_id": "58c9dd45-df41-5582-95ad-93d33663b259",
            "canonical_name": "Howard University",
            "historical_name": "Howard University",
            "aliases": ["Howard"],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "Washington",
            "state_or_region": "District of Columbia",
            "country": "United States",
            "normalization_notes": "Existing canonical organization reused.",
        },
        {
            "key": "ninety-ninth-existing-b936",
            "organization_id": "a520c0e7-81d8-5aea-90d7-ddb0b2ce5eff",
            "canonical_name": "United States Army, 99th Infantry Battalion (Separate)",
            "historical_name": "99th Infantry Battalion (Separate)",
            "aliases": ["99th Infantry", "99TH INF"],
            "organization_type": "U.S. Army infantry battalion",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "Existing canonical organization reused; Denver's headquarters and 99TH INF wording remains visible in the affiliation.",
        },
    ]


def army_affiliations() -> list[dict[str, object]]:
    result: list[dict[str, object]] = []
    for row, data in ARMY.items():
        person_id, name = PEOPLE[row]
        result.append(
            {
                "key": f"{slug(name)}-row{row}-occupation-b936",
                "person_id": person_id,
                "occupation": data["occupation"],
                "relationship_type": "employment",
                "end_date": data["entry"],
                "date_precision": "Army entry date; beginning and duration are not stated",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "A_direct_official",
                "publication_status": "publish_qualified",
                "research_notes": "The official historical category is tied to Army entry. It identifies no employer or workplace and is not promoted to an immediate pre-OSS affiliation.",
            }
        )
    return result


def named_affiliations() -> list[dict[str, object]]:
    return [
        {
            "key": "john-syphax-howard-b936",
            "person_id": PEOPLE[35][0],
            "organization_key": "howard-existing-b936",
            "organization_name_as_found": "Howard",
            "role_title": "Political science teacher",
            "occupation": "political science teacher",
            "relationship_type": "employment",
            "start_date": "1936",
            "end_date": "1938",
            "date_precision": "Years stated in obituary; exact dates not stated",
            "city": "Washington",
            "state_or_region": "District of Columbia",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "high_confidence",
            "claim_confidence": "medium",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "publish_qualified",
            "research_notes": "The obituary explicitly documents 1936-38 teaching and 1943-45 OSS service, but the five-year gap prevents treating Howard as immediate or last civilian before OSS.",
        },
        {
            "key": "ganna-syro-boiarsky-secretary-b936",
            "person_id": PEOPLE[36][0],
            "role_title": "Secretary to General John F. O'Ryan during a Far East survey trip",
            "occupation": "secretary",
            "relationship_type": "employment",
            "end_date": "1940",
            "date_precision": "The government memorandum dates the trip to 1940; exact employment dates are not stated",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "probable",
            "claim_confidence": "medium",
            "source_quality": "A_direct_official",
            "publication_status": "publish_qualified",
            "research_notes": "The rare exact full name and prewar timing support a probable match. The source names an individual principal, not a company or institution, and does not establish the immediate OSS predecessor.",
        },
        {
            "key": "morris-syrstad-99th-b936",
            "person_id": PEOPLE[37][0],
            "organization_key": "ninety-ninth-existing-b936",
            "organization_name_as_found": "HQ, 99TH INF",
            "role_title": "Headquarters company member; later T/5 in OSS NORSO II",
            "occupation": "military service",
            "relationship_type": "military_assignment",
            "date_precision": "World War II assignment; individual transfer date to OSS is not stated",
            "country": "United States",
            "immediate_pre_oss": True,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "probable_immediate",
            "identity_confidence": "confirmed",
            "claim_confidence": "medium",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "publish_qualified",
            "research_notes": "The official protected-identifier bridge confirms the person; Denver documents his 99th Infantry assignment and the NORSO roster documents later OSS service. The individual transfer date is unlocated, so the immediate pathway remains qualified.",
        },
    ]


def affiliations() -> list[dict[str, object]]:
    return [*army_affiliations(), *named_affiliations()]


def army_claims() -> list[dict[str, object]]:
    result: list[dict[str, object]] = []
    for row, data in ARMY.items():
        person_id, name = PEOPLE[row]
        variant_note = ""
        identity_sources = [
            {"source_key": INDEX, "locator_override": f"PDF page 458 row {row}; Box 762"},
            {"source_key": ARMY_SOURCE, "locator_override": f"Accepted reviewed identity record; Army entry {data['entry']}; protected identifier withheld"},
            {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46; field definitions"},
        ]
        if row == 33:
            variant_note = " An official OSS commendation independently supplies the full indexed name and corroborates OSS service."
            identity_sources.append(
                {"source_key": SYPESTEYN_COMMENDATION, "locator_override": "PDF physical page 82, printed page 4; corporal entry and OSS citation; protected identifier withheld"}
            )
        elif row == 39:
            variant_note = " The Army record spells the given name Steven; indexed Stevan remains primary."
        elif row == 41:
            variant_note = " The Army record adds middle initials K L, retained only as a variant."
        result.extend(
            [
                {
                    "key": f"identity-{slug(name)}-row{row}-b936",
                    "person_id": person_id,
                    "claim_type": "identity",
                    "claim_text": f"The indexed {name} row {row} is a high-confidence match to an official Army record dated {data['entry']}.",
                    "evidence_paraphrase": f"The reviewed Army row agrees through a nonshared protected identifier and the full name or a preserved name variant.{variant_note}",
                    "identity_match_assessment": "High confidence from a nonshared protected identifier; the identifier itself is withheld.",
                    "temporal_assessment": f"The Army record documents entry on {data['entry']}; it does not establish the OSS transfer date.",
                    "source_quality": "A_direct_official",
                    "claim_confidence": "high",
                    "publication_status": "published",
                    "match_notes": "No employer or workplace is inferred from the coded occupation field.",
                    "sources": identity_sources,
                },
                {
                    "key": f"occupation-{slug(name)}-row{row}-b936",
                    "person_id": person_id,
                    "affiliation_key": f"{slug(name)}-row{row}-occupation-b936",
                    "claim_type": "occupation",
                    "claim_text": f"At Army entry on {data['entry']}, {name} was recorded in the historical category {data['occupation']}; no employer or workplace is identified.",
                    "evidence_excerpt": data["occupation"],
                    "evidence_paraphrase": f"The accepted Army record carries civilian-occupation code {data['code']}, decoded from NARA's official code list.",
                    "identity_match_assessment": "The category is assigned only to the accepted protected-identifier match; the identifier itself is not public.",
                    "temporal_assessment": "Strongly date-bounded to Army entry, but not proven to be the immediate pre-OSS affiliation.",
                    "source_quality": "A_direct_official",
                    "claim_confidence": "medium",
                    "publication_status": "publish_qualified",
                    "match_notes": "Historical language is preserved and is not converted into a company, school, workplace or modern job title.",
                    "sources": [
                        {"source_key": ARMY_SOURCE, "locator_override": f"Army entry {data['entry']}; civilian-occupation code {data['code']}; protected identifier withheld"},
                        {"source_key": CODES, "locator_override": data["locator"]},
                    ],
                },
            ]
        )
    return result


def named_claims() -> list[dict[str, object]]:
    return [
        {
            "key": "identity-john-syphax-b936",
            "person_id": PEOPLE[35][0],
            "claim_type": "identity",
            "claim_text": "The indexed John W Syphax is a high-confidence match to the Howard political science teacher who served as an OSS biographic analyst from 1943 to 1945.",
            "evidence_paraphrase": "The uncommon exact name and explicit OSS organization, role and dates align the index with the obituary.",
            "identity_match_assessment": "High confidence from the uncommon exact full name and the source's explicit OSS role and dates; Box 762 remains the final direct-file check.",
            "temporal_assessment": "The obituary dates Howard teaching to 1936-38 and OSS service to 1943-45.",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "The education history is retained only for identity context and is not converted into employment.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 458 row 35; Box 762"},
                {"source_key": SYPHAX_OBITUARY, "locator_override": "Obituary paragraphs 2-3; Howard teaching and OSS service"},
            ],
        },
        {
            "key": "prewar-john-syphax-howard-b936",
            "person_id": PEOPLE[35][0],
            "affiliation_key": "john-syphax-howard-b936",
            "claim_type": "other_pre_oss_affiliation",
            "claim_text": "John W. Syphax taught political science at Howard University from 1936 to 1938.",
            "evidence_excerpt": "He taught political science at Howard from 1936 to 1938.",
            "evidence_paraphrase": "The obituary explicitly identifies the institution, teaching field and years.",
            "identity_match_assessment": "High confidence from the uncommon exact name and explicit 1943-45 OSS biographic-analyst service in the same source.",
            "temporal_assessment": "Documented prewar employment, but not immediate or last civilian because the source leaves 1938-43 unaccounted for.",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "claim_confidence": "medium",
            "publication_status": "publish_qualified",
            "match_notes": "Howard is not promoted to immediate pre-OSS affiliation or last civilian employer.",
            "sources": [
                {"source_key": SYPHAX_OBITUARY, "locator_override": "Obituary paragraph 2; Howard teaching dates"},
            ],
        },
        {
            "key": "identity-ganna-syro-boiarsky-b936",
            "person_id": PEOPLE[36][0],
            "claim_type": "identity",
            "claim_text": "The indexed Ganna M Syro-Boiarsky is a probable match to Ganna Mahrt Syro-Boiarsky named in a 1941 Treasury memorandum.",
            "evidence_paraphrase": "The rare exact compound surname, given name and compatible middle name align the index with the contemporary federal memorandum.",
            "identity_match_assessment": "Probable rather than high confidence because the accessible memorandum does not mention OSS or the Box 762 file.",
            "temporal_assessment": "The memorandum discusses a trip made in 1940, before OSS existed.",
            "source_quality": "A_direct_official",
            "claim_confidence": "medium",
            "publication_status": "publish_qualified",
            "match_notes": "Unrelated investigative allegations and personal details in the memorandum are excluded.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 458 row 36; Box 762; printed note fragment preserved"},
                {"source_key": SYRO_TREASURY, "locator_override": "Full-text lines 13993-14000; rare exact name and 1940 secretary role"},
            ],
        },
        {
            "key": "prewar-ganna-syro-boiarsky-secretary-b936",
            "person_id": PEOPLE[36][0],
            "affiliation_key": "ganna-syro-boiarsky-secretary-b936",
            "claim_type": "other_pre_oss_affiliation",
            "claim_text": "A 1941 Treasury memorandum says Ganna Mahrt Syro-Boiarsky accompanied General John F. O'Ryan as his secretary on a 1940 Far East trip.",
            "evidence_excerpt": "went with the General on the trip as his secretary",
            "evidence_paraphrase": "The federal memorandum explicitly identifies the individual, role and prewar trip.",
            "identity_match_assessment": "Probable match from the rare exact compound surname, given name and compatible middle name; no direct OSS bridge is present in the source.",
            "temporal_assessment": "Documented prewar work in 1940; not shown to be immediate before OSS or the last civilian position.",
            "source_quality": "A_direct_official",
            "claim_confidence": "medium",
            "publication_status": "publish_qualified",
            "match_notes": "The principal is preserved as named; no employing organization is invented.",
            "sources": [
                {"source_key": SYRO_TREASURY, "locator_override": "Full-text lines 13993-14000; 1940 trip and secretary role"},
            ],
        },
        {
            "key": "identity-morris-syrstad-b936",
            "person_id": PEOPLE[37][0],
            "claim_type": "identity",
            "claim_text": "The indexed Morris A Syrstad is confirmed as the North Dakota Army entrant later listed in Headquarters, 99th Infantry and as a T/5 in OSS NORSO II.",
            "evidence_paraphrase": "Official index, Army and North Dakota records align by exact name and protected identifier; institutional and OSS rosters align the 99th Infantry and NORSO II assignments.",
            "identity_match_assessment": "Confirmed from an exact nonshared protected identifier in official records, with exact-name unit and OSS corroboration; the identifier is withheld.",
            "temporal_assessment": "Army entry is dated 1940; the two wartime rosters establish the 99th Infantry and later NORSO II sequence but not the transfer date.",
            "source_quality": "A_direct_official",
            "claim_confidence": "confirmed",
            "publication_status": "published",
            "match_notes": "Undefined occupation code 999 is not interpreted, and no civilian employer is inferred.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 458 row 37; Box 762"},
                {"source_key": ARMY_SOURCE, "locator_override": "Accepted reviewed identity record; 1940 Army entry; protected identifier withheld"},
                {"source_key": SYRSTAD_ND, "locator_override": "PDF physical page 188, printed page 1463; exact identity and service chronology; protected identifier withheld"},
                {"source_key": SYRSTAD_DPL, "support_type": "supports", "locator_override": "PDF physical page 896; Headquarters, 99th Infantry"},
                {"source_key": SYRSTAD_NORSO, "support_type": "supports", "locator_override": "NORSO II personnel roster; T/5 Morris Syrstad"},
            ],
        },
        {
            "key": "immediate-morris-syrstad-99th-b936",
            "person_id": PEOPLE[37][0],
            "affiliation_key": "morris-syrstad-99th-b936",
            "claim_type": "immediate_pre_oss_affiliation",
            "claim_text": "Morris A. Syrstad's best-supported immediate pre-OSS assignment is Headquarters, 99th Infantry Battalion (Separate), before his service with OSS NORSO II.",
            "evidence_excerpt": "MORRIS A SYRSTAD HQ 99TH INF",
            "evidence_paraphrase": "The Denver roster places Syrstad in Headquarters, 99th Infantry; the NORSO II roster then lists T/5 Morris Syrstad.",
            "identity_match_assessment": "Confirmed identity from official protected-identifier evidence, with uncommon exact-name agreement across the unit and OSS rosters.",
            "temporal_assessment": "Probable immediate military pathway. The sequence is supported, but no accessible source states Syrstad's individual transfer date.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "medium",
            "publication_status": "publish_qualified",
            "match_notes": "The 99th Infantry is modeled as a military assignment, not a civilian employer, and the qualified claim is excluded from default high-confidence analytics.",
            "sources": [
                {"source_key": SYRSTAD_DPL, "locator_override": "PDF physical page 896; Headquarters, 99th Infantry"},
                {"source_key": SYRSTAD_NORSO, "locator_override": "NORSO II personnel roster; T/5 Morris Syrstad"},
                {"source_key": SYRSTAD_ND, "support_type": "supports", "locator_override": "PDF physical page 188; official identity and Army chronology; protected identifier withheld"},
            ],
        },
    ]


def claims() -> list[dict[str, object]]:
    return [*army_claims(), *named_claims()]


def archival_update(row: int, reason: str) -> dict[str, object]:
    person_id, name = PEOPLE[row]
    update: dict[str, object] = {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, Box 762 and archive location, but staged official-register, CIA-site, OSS, employment, occupation, obituary, institutional, newspaper, Library of Congress and archival searches found no defensible identity bridge. {reason}",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": "Review Box 762 for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }
    if row == 34:
        update["identity_status"] = "ambiguous"
        update["possible_duplicate_group"] = SYPESTEYN_DUPLICATE_GROUP
        update["archival_review_priority"] = "critical"
        update["next_action"] = "Review the Willem K and William K Sypesteyn Box 762 files together. They remain separate people, and the official Willem evidence must not be transferred without direct file proof."
    if row == 38:
        update["identity_status"] = "ambiguous"
        update["possible_duplicate_group"] = SYSKO_DUPLICATE_GROUP
        update["archival_review_priority"] = "critical"
        update["next_action"] = "Review the Stephen J and Stevan J Sysko Box 762 files together. They remain separate people, and the accepted Stevan/Steven Army evidence must not be transferred to Stephen."
    return update


def person_updates() -> list[dict[str, object]]:
    updates = [archival_update(row, reason) for row, reason in UNRESOLVED.items()]
    for row in [26, 33, 37, 39, 41, 42]:
        person_id, _ = PEOPLE[row]
        identity_status = "confirmed" if row == 37 else "high_confidence"
        evidence = "A nonshared protected identifier connects the visually verified index row to the reviewed official Army record. Historical occupation fields remain separate from employer and immediate-affiliation claims."
        status = "completed" if row == 37 else "occupation_only_found"
        next_action = "Review Box 762 for the immediate pre-OSS affiliation and a named civilian employer or institution."
        update: dict[str, object] = {
            "person_id": person_id,
            "identity_status": identity_status,
            "identity_evidence": evidence,
            "personnel_category": "enlisted_army_personnel",
            "commissioned_officer": False,
            "allied_or_foreign_personnel": False,
            "manual_review_required": True,
            "research_status": status,
            "next_action": next_action,
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
            "archival_review_priority": "high",
        }
        if row == 33:
            update["name_variants"] = ["Willem K. Sypesteyn"]
            update["possible_duplicate_group"] = SYPESTEYN_DUPLICATE_GROUP
            update["identity_evidence"] = "A nonshared protected identifier connects the index and Army record; a visually inspected official OSS commendation independently gives the full name and OSS service. The similar William K row remains separate."
            update["next_action"] = "Review the Willem K and William K Sypesteyn Box 762 files together to resolve the possible spelling variant without merging the printed rows."
        elif row == 37:
            update["identity_evidence"] = "Exact nonshared protected-identifier agreement across official records confirms the person; the Denver roster and NORSO II roster independently align the 99th Infantry and OSS assignments."
            update["next_action"] = "Review Box 762 for the precise 99th Infantry-to-OSS transfer and the last civilian employer before Army service."
        elif row == 39:
            update["name_variants"] = ["Steven J Sysko"]
            update["possible_duplicate_group"] = SYSKO_DUPLICATE_GROUP
            update["identity_evidence"] = "A nonshared protected identifier links indexed Stevan J Sysko to the Army record spelling Steven J Sysko. The separately printed Stephen J Sysko row remains distinct and requires joint file review."
            update["next_action"] = "Review the Stephen J and Stevan J Sysko Box 762 files together; do not transfer the accepted Army evidence to Stephen without direct proof."
        elif row == 41:
            update["name_variants"] = ["Kie K L Syzdek"]
        updates.append(update)
    updates.extend(
        [
            {
                "person_id": PEOPLE[35][0],
                "identity_status": "high_confidence",
                "identity_evidence": "A Washington Post obituary aligns the uncommon exact name with explicit 1943-45 OSS biographic-analyst service and documents 1936-38 Howard University teaching.",
                "personnel_category": "civilian_professional_or_administrative_grade",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "documented_prewar_employer_found",
                "next_action": "Review Box 762 and 1938-43 directories or personnel records to identify the immediate pre-OSS affiliation and last civilian employer.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[36][0],
                "identity_status": "probable",
                "identity_evidence": "A contemporary Treasury memorandum supplies the rare exact compound surname, given name, compatible middle name and a 1940 secretary role, but no direct OSS or Box 762 bridge.",
                "name_variants": ["Ganna Mahrt Syro-Boiarsky"],
                "personnel_category": "civilian_professional_or_administrative_grade",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "documented_prewar_employer_found",
                "next_action": "Review Box 762 to confirm the identity and determine whether the 1940 secretary assignment preceded OSS directly or whether later employment intervened.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[46][0],
                "identity_status": "conflicting",
                "identity_evidence": "The official Army candidate agrees by name but its protected identifier is also printed for a differently named source row. This is a source conflict, not proof of a duplicate person.",
                "manual_review_required": True,
                "research_status": "conflicting_sources",
                "next_action": "Review the Box 672 Louis Salamacha and Box 762 Stanley F Szalamacha files together and compare the original Army source before assigning identity, occupation or employment evidence.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
        ]
    )
    return updates


def research_attempts() -> list[dict[str, object]]:
    attempts: list[dict[str, object]] = []
    for row in sorted(PEOPLE):
        person_id, name = PEOPLE[row]
        if row in UNRESOLVED:
            outcome, reviewed, rejected = "no_result", 7, 4
            detail = UNRESOLVED[row]
        elif row == 35:
            outcome, reviewed, rejected = "source_reviewed", 9, 3
            detail = "A reputable obituary supplies an explicit OSS role and dates plus qualified documented-prewar Howard University employment."
        elif row == 36:
            outcome, reviewed, rejected = "source_reviewed", 9, 4
            detail = "A contemporary Treasury memorandum supplies a qualified probable identity and documented 1940 secretary role; unrelated sensitive allegations were excluded."
        elif row == 37:
            outcome, reviewed, rejected = "source_reviewed", 12, 3
            detail = "Official protected-identifier evidence confirms the identity; official and institutional records support a qualified 99th Infantry-to-NORSO II pathway."
        elif row == 46:
            outcome, reviewed, rejected = "candidate_rejected", 8, 4
            detail = "The Army candidate was withheld because one protected identifier is printed for two different index names; neither person receives the occupation evidence."
        elif row in ARMY:
            outcome, reviewed, rejected = "source_reviewed", 10 if row == 33 else 9, 3
            detail = "A nonshared protected identifier supports a high-confidence Army identity bridge and dated occupation-only evidence."
        else:
            raise AssertionError(f"No outcome configured for row {row}")
        attempts.append(
            {
                "key": f"page458-row{row}-{slug(name)}-b936",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA index and public Archives context; CIA Reading Room site-restricted exact-name discovery; OSS and spelling variants; employer and occupation 1940; obituary, institutional, newspaper, Library of Congress and archival searches; Box 762; protected-identifier Army crosswalk where defensible",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_936",
                "started_at": "2026-10-28T03:16:00Z",
                "completed_at": "2026-10-28T03:36:00Z",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search snippets, genealogy-only assertions, modern people-finder pages, postwar-only leads and sources without an OSS, protected-identifier or Box-file bridge were not assigned. Grouped CIA Reading Room exact-name checks produced no additional defensible person-specific result.",
                "research_notes": f"{detail} The index page and official Army code-list pages were visually checked. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA API call was made.",
                "next_action": "Review Box 762 for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before military service.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b936-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-936-v1",
        "reviewer": "Before OSS Batch 936 evidence review",
        "sources": sources(),
        "organizations": organizations(),
        "affiliations": affiliations(),
        "claims": claims(),
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }
    OUTPUT.write_text(
        json.dumps(bundle, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
