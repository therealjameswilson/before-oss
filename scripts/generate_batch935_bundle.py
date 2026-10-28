#!/usr/bin/env python3
"""Generate the reviewed Batch 935 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / (
    "research/evidence-page458-paul-m-sweezy-to-ardeth-g-swoyer-"
    "review_batch-935_2026-10-27.json"
)

INDEX = "nara-index-b935"
ARMY_SOURCE = "army-bulk-b935"
TECH = "army-tech-b935"
CODES = "army-codes-b935"
SWEEZY_INTERVIEW = "sweezy-interview-b935"
HARVARD_CRIMSON = "harvard-crimson-sweezy-b935"
SWIFT_REVIEW = "cia-swift-review-b935"
SWIFT_ANTHOLOGY = "cia-swift-anthology-b935"
SWIFT_MEMORIAL = "swift-memorial-b935"

PEOPLE = {
    1: ("ead0d460-6fcd-51cd-a6d4-01862ecc82f8", "Paul M Sweezy"),
    2: ("8686bb8e-3b16-5aa2-bb72-bdd2e6a6f3aa", "Paul M Sweezy"),
    3: ("c9b7d9f5-98f1-59a1-8e0a-8d643f54c836", "William H Sweezy"),
    4: ("42e969fc-831d-5694-8def-3fa1ae9bc063", "Thomas T Sweigart"),
    5: ("a2761d25-38eb-5bb3-adb5-888b7e86b976", "Mildred M Sweiven"),
    6: ("b32bda9e-0f87-5349-8295-5eed630cf55e", "James J Swensen"),
    7: ("5e771570-d7a2-5818-bc1b-d11f552dd40a", "John W Swensen"),
    8: ("47405c7a-b8cb-518d-9c10-efe83bc67588", "Sigurd M Swenson"),
    9: ("8754c3cd-4deb-59a1-bb64-a27660fc132c", "Judith Swerdloff"),
    10: ("1f497093-a7d0-52a4-8850-62bacd564f87", "John W Swetish"),
    11: ("2ce271ea-ff12-53f1-b078-e4641e595135", "Andrew L Swider"),
    12: ("a3672823-a79c-5c58-b74e-71f94571ecf2", "Gertrude T Swidler"),
    13: ("4c018d36-d9e1-54dc-8b94-79ff9bf1636d", "Henry R Swierat"),
    14: ("e9dc5d67-dbf5-51a9-8805-17111ba5b93e", "Carleton B Swift"),
    15: ("f9095d98-30c0-5d33-8bc6-480b69fee15c", "Frank R Swift"),
    16: ("b37cbcdc-c931-5136-902f-636a7dcd3881", "Helen G Swift"),
    17: ("d28f5516-3542-5fb6-a6b9-6931d7b69c2d", "John L Swift"),
    18: ("706ed1af-148d-5ea7-bd31-1cc6468955c5", "Robert S Swift"),
    19: ("6edd27e8-41b1-5b78-a5b9-71ad5f4e0b5b", "Walter S Swift"),
    20: ("c8d7ec94-a521-5ca1-85c8-1908acdddb91", "Richard M Swinhart"),
    21: ("c92f224b-0f73-57c8-918a-b93ffe1fac0b", "Marion A Swiss"),
    22: ("b47f4bff-6090-505d-88d0-c4a89900d368", "Alfred R Switgall"),
    23: ("f77f5aea-ea0d-5cc6-8c5b-dc8c29ac1b4d", "Ardeth G Swoyer"),
}

PAUL_DUPLICATE_GROUP = "possible-same-person-paul-m-sweezy-box-761"

ARMY = {
    1: {
        "entry": "1942-12-16",
        "code": "011",
        "occupation": "College presidents, professors, and instructors",
        "relationship": "employment",
        "locator": "PDF physical page 170; historical category 0-11",
    },
    4: {
        "entry": "1943-03-01",
        "code": "992",
        "occupation": "Students",
        "relationship": "student",
        "locator": "PDF physical page 304; amended historical category 9-92",
    },
    7: {
        "entry": "1942-06-12",
        "code": "935",
        "occupation": "Routemen",
        "relationship": "employment",
        "locator": "PDF physical page 174; historical category 7,9-35",
    },
    8: {
        "entry": "1942-10-12",
        "code": "992",
        "occupation": "Students",
        "relationship": "student",
        "locator": "PDF physical page 304; amended historical category 9-92",
    },
    11: {
        "entry": "1943-02-13",
        "code": "699",
        "occupation": "Occupations in manufacture of radios and phonographs",
        "relationship": "employment",
        "locator": "PDF physical page 174; historical category 4,6,8-99",
    },
    13: {
        "entry": "1943-11-17",
        "code": "513",
        "occupation": "Occupations in manufacture of miscellaneous products",
        "relationship": "employment",
        "locator": "PDF physical page 174; historical category 5,7,9-13",
    },
}

UNRESOLVED = {
    2: "This separately printed Paul M Sweezy row carries a different protected identifier from row 1; the Harvard and Army evidence is not transferred.",
    3: "Exact-name OSS, military, employment and obituary searches supplied no Box 761 identity bridge.",
    5: "Exact-name and spelling-variant searches supplied no defensible OSS or Box 761 identity bridge.",
    6: "Exact-name and military searches supplied no two-identifier match for James J Swensen.",
    9: "Genealogy-style Judith Swerdloff leads lacked an OSS, Box 761 or employment bridge and were not assigned.",
    10: "A 501st Parachute Infantry roster lead remains unassigned because no authoritative source establishes its relation to the Box 761 file or an OSS transition.",
    12: "Exact-name and employment searches supplied no defensible OSS or Box 761 identity bridge.",
    15: "Exact-name searches produced unrelated and unbridged namesakes; no Box 762 identity bridge was found.",
    16: "Multiple Helen G Swift namesakes could not be distinguished from the indexed person.",
    17: "The short protected identifier and common name did not yield a defensible official-record match.",
    18: "The reviewed Army candidate was rejected because its surname and given name differ completely from Robert S Swift.",
    19: "Exact-name, military and obituary searches supplied no two-identifier match for Walter S Swift.",
    20: "Exact-name and spelling-variant searches supplied no defensible OSS or Box 762 identity bridge.",
    21: "Searches for the exact indexed name returned unrelated uses of Swiss as a nationality and no person-specific bridge.",
    22: "A Ritchie Boys roster supplies the rare exact name but no protected identifier, OSS transition, employer or Box 762 bridge.",
    23: "Exact-name, obituary, institutional and archival searches supplied no defensible identity bridge.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 761-762",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 458, rows 1-23; checked against layout-preserving text and a rendered page image",
            "access_date": "2026-10-27",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. Full identifiers remain private. The two Paul M Sweezy rows have different protected identifiers and are not merged.",
        },
        {
            "key": ARMY_SOURCE,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; six accepted and one rejected Batch 935 identity candidates",
            "access_date": "2026-10-27",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "Accepted rows use nonshared protected-identifier matches. No raw bulk row or full identifier is public.",
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
            "locator": "PDF physical pages 170, 174 and 304; categories 011, 513, 699, 935 and amended 992 visually checked",
            "access_date": "2026-10-27",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical labels identify neither a named employer nor workplace. Students is status, not employment.",
        },
        {
            "key": SWEEZY_INTERVIEW,
            "stable_url": "https://www.devrimcimarksizm.net/sites/default/files/sungur_savran_and_e._ahmet_tonak_an_interview_with_paul_sweezy.pdf",
            "archival_identifier": "Interview conducted 1986-03-20; republished in Revolutionary Marxism 2025",
            "title": "An Interview with Paul Sweezy",
            "author_creator": "Sungur Savran and E. Ahmet Tonak; interviewee Paul M. Sweezy",
            "repository_publisher": "Revolutionary Marxism; originally translated in Onbirinci Tez and later published in Monthly Review",
            "publication_record_date": "1986 interview; 2025 republication",
            "locator": "PDF pages 1-2, printed pages 287-290; footnote and first-person Harvard-Army-OSS chronology",
            "access_date": "2026-10-27",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "rights_notes": "Only short excerpts and project-authored paraphrases are retained.",
        },
        {
            "key": HARVARD_CRIMSON,
            "stable_url": "https://www.thecrimson.com/article/1940/12/4/dunster-forum-discusses-economics-of-defense/",
            "archival_identifier": "Harvard Crimson article, 1940-12-04",
            "title": "Dunster Forum Discusses Economics of Defense Before Large Crowd",
            "repository_publisher": "The Harvard Crimson",
            "publication_record_date": "1940-12-04",
            "locator": "Article text; Paul M. Sweezy '32 identified as instructor in Economics",
            "access_date": "2026-10-27",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "The Harvard Crimson archive",
            "rights_notes": "Contemporary institutional newspaper used to corroborate the named Harvard role.",
        },
        {
            "key": SWIFT_REVIEW,
            "stable_url": "https://www.cia.gov/resources/csi/static/675d915ae21817e698dfb5f08240f6a7/Swift-WhyVietnam.pdf",
            "archival_identifier": "Studies in Intelligence 25, no. 2 (1981)",
            "title": "Intelligence in Recent Public Literature: Why Vietnam? Prelude to America's Albatross",
            "author_creator": "Carleton A. Swift",
            "repository_publisher": "Center for the Study of Intelligence, Central Intelligence Agency",
            "publication_record_date": "1981",
            "locator": "PDF page 1, printed page 99; first-person November 1944 OSS entry and wartime assignments; PDF page 9 signature",
            "access_date": "2026-10-27",
            "source_quality": "A_direct_official",
            "collection_name": "Studies in Intelligence",
            "rights_notes": "The author line uses middle initial A while the index and family memorial use B/Byron. The discrepancy remains explicit.",
        },
        {
            "key": SWIFT_ANTHOLOGY,
            "stable_url": "https://www.cia.gov/resources/csi/static/CIA-Wars-Southeast-Asia.pdf",
            "archival_identifier": "Studies in Intelligence anthology, August 2016",
            "title": "CIA and the Wars in Southeast Asia, 1947-75",
            "author_creator": "Clayton D. Laurie and Andres Vaart",
            "repository_publisher": "Center for the Study of Intelligence, Central Intelligence Agency",
            "publication_record_date": "2016-08",
            "locator": "PDF page 45, printed page 29; Carleton Swift identified as Patti's successor as chief of Hanoi Station",
            "access_date": "2026-10-27",
            "source_quality": "A_direct_official",
            "collection_name": "Studies in Intelligence anthology",
            "rights_notes": "Official institutional corroboration of the OSS identity and Hanoi assignment.",
        },
        {
            "key": SWIFT_MEMORIAL,
            "stable_url": "https://remembered.com/biography/cbs",
            "archival_identifier": "Carleton Byron Swift memorial biography",
            "title": "Carleton Byron Swift's Biography",
            "repository_publisher": "Remembered.com",
            "publication_record_date": "2012",
            "locator": "Memorial biography paragraphs 1-2; Harvard, Swift and Co., Navy and OSS chronology",
            "access_date": "2026-10-27",
            "source_quality": "D_correlative_or_secondary",
            "rights_notes": "Family memorial used with official CIA sources. The Swift and Co. employer claim remains medium-confidence and qualified.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": "harvard-existing-b935",
            "organization_id": "45ddf347-21c6-59f5-a8ae-517418adf941",
            "canonical_name": "Harvard University",
            "historical_name": "Harvard University",
            "aliases": ["Harvard"],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "Cambridge",
            "state_or_region": "Massachusetts",
            "country": "United States",
            "normalization_notes": "Existing canonical organization reused.",
        },
        {
            "key": "army-existing-b935",
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
            "key": "navy-existing-b935",
            "organization_id": "3960fa8e-a551-56cf-8305-b2b9e4961b9d",
            "canonical_name": "United States Navy",
            "historical_name": "United States Navy",
            "aliases": ["U.S. Navy", "Navy"],
            "organization_type": "military service",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "Existing canonical organization reused.",
        },
        {
            "key": "swift-company-b935",
            "canonical_name": "Swift & Company",
            "historical_name": "Swift and Co.",
            "aliases": ["Swift and Company", "Swift & Co.", "Swift and Co."],
            "organization_type": "meatpacking company",
            "sector": "business_and_industry",
            "city": "Chicago",
            "state_or_region": "Illinois",
            "country": "United States",
            "normalization_notes": "The family memorial's historical wording is preserved. No modern successor is substituted.",
        },
    ]


def army_affiliations() -> list[dict[str, object]]:
    result: list[dict[str, object]] = []
    for row, data in ARMY.items():
        person_id, name = PEOPLE[row]
        result.append(
            {
                "key": f"{slug(name)}-row{row}-occupation-b935",
                "person_id": person_id,
                "occupation": data["occupation"],
                "relationship_type": data["relationship"],
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
            "key": "paul-sweezy-harvard-b935",
            "person_id": PEOPLE[1][0],
            "organization_key": "harvard-existing-b935",
            "organization_name_as_found": "Harvard",
            "role_title": "Assistant Professor of Economics",
            "occupation": "economist and university teacher",
            "relationship_type": "employment",
            "end_date": "1942",
            "date_precision": "Sweezy says he left Harvard in 1942 while on a five-year contract; exact day not stated",
            "city": "Cambridge",
            "state_or_region": "Massachusetts",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": True,
            "pre_oss_temporal_basis": "explicit_immediate",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "published",
            "research_notes": "Sweezy's first-person account explicitly places Harvard immediately before Army service; the Army then intervened before OSS.",
        },
        {
            "key": "paul-sweezy-army-b935",
            "person_id": PEOPLE[1][0],
            "organization_key": "army-existing-b935",
            "organization_name_as_found": "U.S. Army",
            "role_title": "Private at entry; later taken into the intelligence apparatus",
            "occupation": "military service",
            "relationship_type": "military_assignment",
            "start_date": "1942-12-16",
            "date_precision": "Army entry date is exact; transfer into OSS is explicit but undated",
            "country": "United States",
            "immediate_pre_oss": True,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "explicit_immediate",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "A_direct_official",
            "publication_status": "published",
            "research_notes": "The official Army entry and Sweezy's first-person statement establish the Army-to-OSS pathway without inferring a transfer date.",
        },
        {
            "key": "carleton-swift-navy-b935",
            "person_id": PEOPLE[14][0],
            "organization_key": "navy-existing-b935",
            "organization_name_as_found": "US Navy",
            "role_title": "PT boat service in the South Pacific; later Lieutenant Commander",
            "occupation": "naval officer",
            "relationship_type": "military_assignment",
            "end_date": "1944-11",
            "date_precision": "Swift's first-person account dates OSS entry to November 1944; exact Navy dates are not stated",
            "country": "United States",
            "immediate_pre_oss": True,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "explicit_immediate",
            "identity_confidence": "high_confidence",
            "claim_confidence": "medium",
            "source_quality": "D_correlative_or_secondary",
            "publication_status": "publish_qualified",
            "research_notes": "The family memorial supplies the Navy-before-OSS sequence; Swift's CIA-hosted first-person review dates OSS entry and official CIA sources document his OSS rank and assignments.",
        },
        {
            "key": "carleton-swift-company-b935",
            "person_id": PEOPLE[14][0],
            "organization_key": "swift-company-b935",
            "organization_name_as_found": "Swift and Co.",
            "role_title": "Role not stated",
            "occupation": "meatpacking-company employee",
            "relationship_type": "employment",
            "date_precision": "Brief employment after Harvard graduation in 1941 and before Navy service; exact dates not stated",
            "city": "Chicago",
            "state_or_region": "Illinois",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": True,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "high_confidence",
            "claim_confidence": "medium",
            "source_quality": "D_correlative_or_secondary",
            "publication_status": "publish_qualified",
            "research_notes": "Best-supported last civilian employer before Navy service, but currently supported by a family memorial rather than a personnel or company record.",
        },
    ]


def affiliations() -> list[dict[str, object]]:
    return [*army_affiliations(), *named_affiliations()]


def army_claims() -> list[dict[str, object]]:
    result: list[dict[str, object]] = []
    for row, data in ARMY.items():
        person_id, name = PEOPLE[row]
        variant_note = ""
        if row == 7:
            variant_note = " The Army file spells the surname Swenson; the indexed Swensen spelling remains primary."
        result.extend(
            [
                {
                    "key": f"identity-{slug(name)}-row{row}-b935",
                    "person_id": person_id,
                    "claim_type": "identity",
                    "claim_text": f"The indexed {name} row {row} is a high-confidence match to an official Army record dated {data['entry']}.",
                    "evidence_paraphrase": f"The reviewed Army row agrees through a nonshared protected identifier and the full name or a preserved one-letter surname variant.{variant_note}",
                    "identity_match_assessment": "High confidence from a nonshared protected identifier; the identifier itself is withheld.",
                    "temporal_assessment": f"The Army record documents entry on {data['entry']}; it does not establish the OSS transfer date.",
                    "source_quality": "A_direct_official",
                    "claim_confidence": "high",
                    "publication_status": "published",
                    "match_notes": "No employer or workplace is inferred from the coded occupation field.",
                    "sources": [
                        {"source_key": INDEX, "locator_override": f"PDF page 458 row {row}; Box 761"},
                        {"source_key": ARMY_SOURCE, "locator_override": f"Accepted reviewed identity record; Army entry {data['entry']}; protected identifier withheld"},
                        {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46; field definitions"},
                    ],
                },
                {
                    "key": f"occupation-{slug(name)}-row{row}-b935",
                    "person_id": person_id,
                    "affiliation_key": f"{slug(name)}-row{row}-occupation-b935",
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
            "key": "last-civilian-paul-sweezy-harvard-b935",
            "person_id": PEOPLE[1][0],
            "affiliation_key": "paul-sweezy-harvard-b935",
            "claim_type": "last_civilian_pre_service",
            "claim_text": "Paul M. Sweezy's last civilian employer before Army service was Harvard University, where he taught economics.",
            "evidence_excerpt": "on military leave from Harvard ... an Assistant Professor",
            "evidence_paraphrase": "Sweezy said he left Harvard in 1942 for the Army while holding a five-year academic contract; a 1940 Crimson article identifies him as an economics instructor.",
            "identity_match_assessment": "High confidence from the rare full name, exact protected-identifier Army bridge, 1942 entry date and matching professor category.",
            "temporal_assessment": "Explicit civilian-to-Army sequence. Harvard is the last civilian employer, not the immediate pre-OSS affiliation because Army service intervened.",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "The separately printed second Paul M Sweezy row receives no copied claim.",
            "sources": [
                {"source_key": SWEEZY_INTERVIEW, "locator_override": "PDF page 2, printed page 290; first-person Harvard-Army chronology"},
                {"source_key": HARVARD_CRIMSON, "support_type": "supports", "locator_override": "Article text; instructor in Economics"},
                {"source_key": ARMY_SOURCE, "support_type": "supports", "locator_override": "Accepted Army identity record; 1942-12-16 entry; protected identifier withheld"},
            ],
        },
        {
            "key": "immediate-paul-sweezy-army-b935",
            "person_id": PEOPLE[1][0],
            "affiliation_key": "paul-sweezy-army-b935",
            "claim_type": "immediate_pre_oss_affiliation",
            "claim_text": "Paul M. Sweezy entered OSS from the U.S. Army.",
            "evidence_excerpt": "taken from the Army into the intelligence apparatus",
            "evidence_paraphrase": "Sweezy explicitly described moving from the Army into OSS; the official Army file dates entry to 16 December 1942.",
            "identity_match_assessment": "High confidence from the exact name, nonshared protected identifier and matching academic occupation.",
            "temporal_assessment": "Explicit immediate Army-to-OSS transition; the exact transfer date is not stated.",
            "source_quality": "A_direct_official",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "Army is modeled as a military assignment, not a civilian employer.",
            "sources": [
                {"source_key": SWEEZY_INTERVIEW, "locator_override": "PDF page 2, printed page 290; first-person Army-to-OSS statement"},
                {"source_key": ARMY_SOURCE, "support_type": "supports", "locator_override": "Accepted Army identity record; entry date and private grade; protected identifier withheld"},
            ],
        },
        {
            "key": "identity-carleton-swift-b935",
            "person_id": PEOPLE[14][0],
            "claim_type": "identity",
            "claim_text": "The indexed Carleton B Swift is a high-confidence match to Carleton Byron Swift Jr., the naval officer who joined OSS in 1944 and served in China and Hanoi.",
            "evidence_paraphrase": "The rare exact given and surname, Byron middle name, 1944 OSS entry, China service and Hanoi role align the index, family memorial, Swift's CIA-hosted first-person review and the CIA anthology.",
            "identity_match_assessment": "High confidence, not confirmed: official CIA sources document the rare-name OSS officer, while the review author line uses middle initial A rather than indexed B/Byron.",
            "temporal_assessment": "Swift's first-person review dates OSS entry to November 1944; the memorial places Navy service immediately before it.",
            "source_quality": "A_direct_official",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "The middle-initial disagreement remains visible and requires Box 761 confirmation.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 458 row 14; Box 761"},
                {"source_key": SWIFT_REVIEW, "locator_override": "PDF page 1 and signature on page 9; first-person OSS chronology"},
                {"source_key": SWIFT_ANTHOLOGY, "locator_override": "PDF page 45, printed page 29; Hanoi station role"},
                {"source_key": SWIFT_MEMORIAL, "support_type": "supports", "locator_override": "Memorial biography paragraphs 1-2"},
            ],
        },
        {
            "key": "immediate-carleton-swift-navy-b935",
            "person_id": PEOPLE[14][0],
            "affiliation_key": "carleton-swift-navy-b935",
            "claim_type": "immediate_pre_oss_affiliation",
            "claim_text": "Carleton B. Swift Jr.'s immediate pre-OSS affiliation was the United States Navy.",
            "evidence_excerpt": "then joined the US Navy ... In 1944, he joined the Office of Strategic Services",
            "evidence_paraphrase": "The memorial explicitly sequences PT boat-related Navy service before OSS, while Swift's first-person CIA-hosted review dates OSS entry to November 1944 and identifies his subsequent assignments.",
            "identity_match_assessment": "High confidence from the rare name and mutually consistent official OSS chronology, with the middle-initial discrepancy retained.",
            "temporal_assessment": "Explicit Navy-to-OSS sequence; exact Navy dates are not stated.",
            "source_quality": "D_correlative_or_secondary",
            "claim_confidence": "medium",
            "publication_status": "publish_qualified",
            "match_notes": "The explicit transition is currently supplied by a family memorial; the Navy is not labeled a civilian employer, and the claim is excluded from default high-confidence analytics pending direct personnel or naval evidence.",
            "sources": [
                {"source_key": SWIFT_MEMORIAL, "locator_override": "Memorial biography paragraph 2; Navy-to-OSS sequence"},
                {"source_key": SWIFT_REVIEW, "support_type": "supports", "locator_override": "PDF page 1; November 1944 OSS entry and maritime assignment"},
                {"source_key": SWIFT_ANTHOLOGY, "support_type": "supports", "locator_override": "PDF page 45; OSS Hanoi role"},
            ],
        },
        {
            "key": "last-civilian-carleton-swift-company-b935",
            "person_id": PEOPLE[14][0],
            "affiliation_key": "carleton-swift-company-b935",
            "claim_type": "last_civilian_pre_service",
            "claim_text": "Carleton B. Swift Jr.'s best-supported last civilian employer before Navy service is Swift and Co., the family meatpacking business.",
            "evidence_excerpt": "worked briefly for Swift and Co. ... and then joined the US Navy",
            "evidence_paraphrase": "The family memorial explicitly places brief Swift and Co. employment between Harvard graduation and Navy service.",
            "identity_match_assessment": "High-confidence identity through official OSS evidence and the rare full-name chronology.",
            "temporal_assessment": "Strongly date-bounded as the last identified civilian employer before Navy service; exact employment dates are not stated.",
            "source_quality": "D_correlative_or_secondary",
            "claim_confidence": "medium",
            "publication_status": "publish_qualified",
            "match_notes": "Qualified pending a personnel, company or contemporary directory record. Excluded from default high-confidence employer analytics.",
            "sources": [
                {"source_key": SWIFT_MEMORIAL, "locator_override": "Memorial biography paragraph 2; employer-to-Navy chronology"},
                {"source_key": SWIFT_REVIEW, "support_type": "supports", "locator_override": "PDF page 1; first-person 1944 OSS chronology"},
            ],
        },
    ]


def claims() -> list[dict[str, object]]:
    return [*army_claims(), *named_claims()]


def archival_update(row: int, reason: str) -> dict[str, object]:
    person_id, name = PEOPLE[row]
    box = "761" if row <= 14 else "762"
    update: dict[str, object] = {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, Box {box} and archive location, but staged official-register, CIA-site, OSS, employment, occupation, obituary, institutional, newspaper, Library of Congress and archival searches found no defensible identity bridge. {reason}",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": f"Review Box {box} for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }
    if row == 2:
        update["identity_status"] = "ambiguous"
        update["possible_duplicate_group"] = PAUL_DUPLICATE_GROUP
        update["archival_review_priority"] = "critical"
        update["next_action"] = "Review both Box 761 Paul M Sweezy files together. The printed rows have different protected identifiers and must not be merged or share Harvard claims without direct file evidence."
    if row == 18:
        update["archival_review_priority"] = "critical"
        update["next_action"] = "Review Box 762 to resolve Robert S Swift's identity. The different-name Army candidate was rejected and supplies no usable occupation evidence."
    return update


def person_updates() -> list[dict[str, object]]:
    updates = [archival_update(row, reason) for row, reason in UNRESOLVED.items()]
    for row in ARMY:
        box = "761"
        status = "verified_employer_found" if row == 1 else "occupation_only_found"
        next_action = f"Review Box {box} for the immediate pre-OSS affiliation and a named employer or institution."
        update: dict[str, object] = {
            "person_id": PEOPLE[row][0],
            "identity_status": "high_confidence",
            "identity_evidence": "A nonshared protected identifier connects the visually verified index row to the reviewed official Army record. The historical occupation field remains separate from employer and immediate-affiliation claims.",
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
        if row == 1:
            update["name_variants"] = ["Paul M. Sweezy", "Paul Marlor Sweezy"]
            update["possible_duplicate_group"] = PAUL_DUPLICATE_GROUP
            update["next_action"] = "Review both Box 761 Paul M Sweezy files to confirm the exact Army-to-OSS transfer and explain the separately printed second identifier."
        if row == 7:
            update["name_variants"] = ["John W Swenson", "John W. Swensen"]
            update["identity_evidence"] = "A nonshared protected identifier links indexed John W Swensen to the Army record spelling John W Swenson. The one-letter surname difference remains visible and requires Box 761 confirmation."
        updates.append(update)
    updates.append(
        {
            "person_id": PEOPLE[14][0],
            "identity_status": "high_confidence",
            "identity_evidence": "Official CIA publications, Swift's first-person review and a family memorial align the rare Carleton Swift name, 1944 OSS entry, China and Hanoi assignments and Lieutenant Commander rank. The review author line's A middle initial differs from indexed B/Byron and remains explicit.",
            "name_variants": ["Carleton Byron Swift Jr.", "Carleton B. Swift Jr.", "Carleton A. Swift"],
            "personnel_category": "commissioned_naval_officer",
            "commissioned_officer": True,
            "allied_or_foreign_personnel": False,
            "manual_review_required": True,
            "research_status": "documented_prewar_employer_found",
            "next_action": "Review Box 761 and a Swift & Company personnel or contemporary directory source to confirm the middle initial, Navy transition and qualified company employment.",
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
            "archival_review_priority": "high",
        }
    )
    return updates


def research_attempts() -> list[dict[str, object]]:
    attempts: list[dict[str, object]] = []
    for row in sorted(PEOPLE):
        person_id, name = PEOPLE[row]
        box = "761" if row <= 14 else "762"
        if row == 1:
            outcome, reviewed, rejected = "source_reviewed", 12, 4
            detail = "The official Army bridge, a first-person interview and a contemporary Harvard article establish a high-confidence identity, Harvard employment and an explicit Army-to-OSS pathway."
        elif row == 14:
            outcome, reviewed, rejected = "source_reviewed", 12, 4
            detail = "Official CIA sources and a family memorial establish a high-confidence identity and Navy pathway; Swift and Co. remains a qualified medium-confidence last civilian employer."
        elif row in ARMY:
            outcome, reviewed, rejected = "source_reviewed", 9, 3
            detail = "A nonshared protected identifier supports a high-confidence Army identity bridge and dated occupation-only evidence."
        else:
            outcome, reviewed, rejected = "no_result", 7, 4
            detail = UNRESOLVED[row]
        attempts.append(
            {
                "key": f"page458-row{row}-{slug(name)}-b935",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA index and public Archives context; CIA Reading Room site-restricted exact-name discovery; OSS and spelling variants; employer and occupation 1940; obituary, institutional, newspaper, Library of Congress and archival searches; Box {box}; protected-identifier Army crosswalk where defensible",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_935",
                "started_at": "2026-10-27T22:45:00Z",
                "completed_at": "2026-10-28T03:15:00Z",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search snippets, genealogy-only assertions, modern people-finder pages, postwar-only leads and sources without an OSS, protected-identifier or Box-file bridge were not assigned. Grouped CIA Reading Room and Library of Congress site-restricted exact-name checks produced no additional defensible person-specific result.",
                "research_notes": f"{detail} The index page and official Army code-list pages were visually checked. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA API call was made.",
                "next_action": f"Review Box {box} for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before military service.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b935-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-935-v1",
        "reviewer": "Before OSS Batch 935 evidence review",
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
