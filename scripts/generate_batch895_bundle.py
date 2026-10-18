#!/usr/bin/env python3
"""Generate the reviewed Batch 895 evidence bundle from audited constants."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "research/evidence-page437-snyder-to-soha-review_batch-895_2026-10-18.json"

INDEX = "nara-index-b895"
ARMY = "army-bulk-b895"
TECH = "army-tech-b895"
CODES = "army-codes-b895"
NPS_SNYDER = "nps-jacques-snyder-b895"
NARA_AWARDS = "nara-oss-awards-104-10165-10120-b895"
GAZETTE_1925 = "london-gazette-sofiano-1925-b895"
GAZETTE_1946 = "london-gazette-sofiano-1946-b895"
WAPO_SUTTON = "washington-post-henry-sutton-b895"
CIA_SUTTON = "cia-reading-room-henry-sutton-b895"


PEOPLE = {
    24: ("a0eb56fc-94e0-5d7a-94d0-620cb727a61b", "Edwin N Snyder"),
    25: ("3de98a54-5732-59c6-b6b5-675e49475a74", "Fred R Snyder"),
    26: ("81846ed3-29e1-5a6a-9b7d-c91bff9e6105", "Horace Snyder"),
    27: ("c688e6ed-7a90-5040-b025-a560d83f814a", "Jacques F Snyder"),
    28: ("0d52f2fb-07cb-5351-9fef-b17b9f36a125", "John C Snyder"),
    29: ("79f26601-d2c7-587f-9751-674bd8810456", "John T Snyder"),
    30: ("b4bafedb-05f7-5804-9d4b-d55b5a88eb20", "Kinsley D Snyder"),
    31: ("0a9138af-4eeb-535f-a40f-27356379b953", "Mary J Snyder"),
    32: ("fc6928ae-ec6f-5fc8-92ae-158bbcedca2d", "Robert P Snyder"),
    33: ("dd583670-17a6-5fa3-9b22-9b61a0d1c0c5", "Robert M Snyder"),
    34: ("66ba5ebe-29d9-5d0e-b96d-0f32d9a03012", "William T Snyder"),
    35: ("e9ecdc74-486b-5081-b7e8-6f733753c4c8", "John N Soares"),
    36: ("725f8e08-fc9a-53ee-a009-1a103df5cf27", "Leonard F Soares"),
    37: ("64973a5c-cdd2-5fb4-bb7c-2580a953bcbb", "Franciszek Sobecki"),
    38: ("5cee0934-c05e-52df-afa4-1a7b4462b635", "Julian Sobiechowski"),
    39: ("f5db58ba-c46b-57dc-b190-6b3d79769c5c", "Amato D Soccorsy"),
    40: ("57200a17-49a2-506a-98b8-c979c6f8ae0f", "Gloria H Soderberg"),
    41: ("75b19183-870f-57e8-bf4e-9375b3d0825c", "M Soegihadji"),
    42: ("8d32f609-60a0-5dce-a87f-158e9509f57a", "Louis T Sofa"),
    43: ("09426597-aa08-5f50-8bae-68a0a068d0fb", "Heinrich C Soffner"),
    44: ("00262806-355a-5598-bce4-f1b49140ed5b", "Heirich C Soffner"),
    45: ("d014b325-de84-5e57-9b29-5be897a3f4b8", "Vincent J Sofiano"),
    46: ("56563af8-16d1-5c82-9893-320aaa316b5b", "John Soha"),
}


ARMY_MATCHES = [
    {
        "row": 24,
        "slug": "edwin-n-snyder",
        "date": "1942-06-17",
        "code": "735",
        "occupation": "Routemen",
        "code_locator": "PDF physical page 174; transportation category 7-35",
    },
    {
        "row": 25,
        "slug": "fred-r-snyder",
        "date": "1943-07-08",
        "code": "521",
        "occupation": "Miners and mining-machine operators",
        "code_locator": "PDF physical page 174; extraction-of-minerals category 5-21",
    },
    {
        "row": 27,
        "slug": "jacques-f-snyder",
        "date": "1942-09-18",
        "code": "031",
        "occupation": "Teachers (secondary school) and principals",
        "code_locator": "PDF physical page 171; professional category 0-31",
    },
    {
        "row": 36,
        "slug": "leonard-f-soares",
        "date": "1943-05-15",
        "code": "072",
        "occupation": "Retail managers",
        "code_locator": "PDF physical page 171; managerial category 0-72",
    },
    {
        "row": 43,
        "slug": "heinrich-soffner-henry-sutton",
        "date": "1943-12-06",
        "code": "105",
        "occupation": "Clerks, general office",
        "code_locator": "PDF physical page 171; clerical category 1-05",
    },
]


UNRESOLVED = {
    26: "The common name produced no official OSS, Box 727 or prewar-employment bridge with corroborating identifiers.",
    28: "Multiple namesakes remained unbridged; none supplied two corroborating identifiers beyond the indexed name.",
    29: "The only protected-identifier Army candidate names Carmon Donald F and is formally rejected; no alias evidence resolves the conflict.",
    30: "Exact-name, occupation, obituary, institutional and archival searches produced no defensible identity bridge.",
    31: "Common-name results lacked a protected identifier, OSS assignment or Box 727 bridge.",
    32: "Earlier newspaper candidates carried incompatible middle initials M or W and remain rejected; no supported P-initial identity was found.",
    33: "Common-name results did not distinguish this Robert M Snyder from unrelated namesakes.",
    34: "Exact-name OSS, occupation, obituary and institutional searches produced no defensible identity bridge.",
    35: "Exact-name and Portuguese-name variants produced no reliable OSS or prewar-affiliation bridge.",
    38: "A Project Eagle alias lead remains discovery-only and lacks an inspectable item-level source tying it to this indexed Polish Army row.",
    39: "Modern property and memorial name matches are chronologically irrelevant or uncorroborated and were rejected.",
    40: "Exact-name official-domain, occupation, obituary and institutional searches returned only the index or unbridged namesakes.",
    41: "The initials-only foreign-name row remains highly ambiguous; transliteration and institutional searches produced no corroborating identifiers.",
    42: "A paywalled Navy muster-roll name lead could not be inspected or bridged to OSS, Box 727 or a prewar affiliation.",
    44: "The adjacent Heirich spelling may duplicate Heinrich C Soffner, but this row lacks the protected identifier that independently links Heinrich to Henry Sutton, so it remains separate.",
    46: "Exact-name OSS, occupation, obituary, directory and archival searches produced no defensible identity bridge.",
}


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 727-728 and 759",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 437 rows 24-46; PDF page 456 rows 32-33 for the separately indexed Henry C Sutton records; checked against layout-preserving text and rendered page images",
            "access_date": "2026-10-18",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All printed rows remain immutable. A matching protected identifier resolves one Soffner/Sutton alias pair; the identifier is withheld from public data, and the other same-name rows remain separate.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; protected-identifier fields checked; six identity candidates accepted and one rejected after review",
            "access_date": "2026-10-18",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "No raw row or full private identifier is retained in public assets. The file is incomplete and a non-hit is not negative proof.",
        },
        {
            "key": TECH,
            "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf",
            "archival_identifier": "NN3-064-03-008; National Archives Identifier 1263923",
            "title": "World War II Army Enlistment Records: Reference Copy of Technical Documentation",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives at College Park - Electronic Records",
            "publication_record_date": "1994-2005; reference copy modified 2011",
            "locator": "PDF physical pages 44-46; fixed-width identifier, name, DD/MM/YY Army-entry-date, grade and civilian-occupation fields visually checked",
            "access_date": "2026-10-18",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Used to interpret selected fields only; source damage, alternate layouts, coding limits and incomplete coverage remain applicable.",
        },
        {
            "key": CODES,
            "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1CL_SD.pdf",
            "archival_identifier": "National Archives Identifier 1263923; Code No. 30",
            "title": "NARA Compiled Code Lists for the Electronic Army Serial Number Merged File",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives at College Park - Electronic Records",
            "publication_record_date": "2011-01-12; modified 2011-03-17",
            "locator": "PDF physical pages 171 and 174; categories 031, 072, 105, 521 and 735 visually checked",
            "access_date": "2026-10-18",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical labels name neither employers nor workplaces and are published only as qualified occupation evidence.",
        },
        {
            "key": NPS_SNYDER,
            "stable_url": "https://home.nps.gov/articles/daily-life-in-camp-park-and-town.htm",
            "title": "Daily Life in Camp Park and Town",
            "repository_publisher": "U.S. National Park Service",
            "publication_record_date": "2017-07-27",
            "locator": "Jacques F. Snyder biographical passage in the recruitment discussion",
            "access_date": "2026-10-18",
            "source_quality": "A_direct_official",
            "collection_name": "OSS Training in the National Parks and Service Abroad in World War II",
            "rights_notes": "Only two concise excerpts totaling fewer than 25 words are retained; postwar details are not reconstructed.",
        },
        {
            "key": NARA_AWARDS,
            "stable_url": "https://www.archives.gov/files/research/jfk/releases/104-10165-10120.pdf",
            "archival_identifier": "104-10165-10120",
            "title": "OSS awards and decorations records",
            "author_creator": "Office of Strategic Services, U.S. Forces European Theater",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1945-07-19 and 1945-08-22",
            "locator": "PDF physical page 79, Award of Unit Certificate of Merit; pages 130 and 132-133, Awards and Decorations Board minutes and SI Branch survey",
            "access_date": "2026-10-18",
            "source_quality": "A_direct_official",
            "collection_name": "John F. Kennedy Assassination Records Collection; declassified OSS records",
            "document_number": "104-10165-10120",
            "rights_notes": "Target pages were rendered and visually checked. Full record images are not republished in public data.",
        },
        {
            "key": GAZETTE_1925,
            "stable_url": "https://www.thegazette.co.uk/London/issue/33080/page/5770/data.pdf",
            "archival_identifier": "London Gazette Issue 33080, page 5770",
            "title": "The London Gazette, Issue 33080",
            "author_creator": "Air Ministry",
            "repository_publisher": "The Gazette, United Kingdom",
            "publication_record_date": "1925-09-01",
            "locator": "Page 5770; permanent commissions effective 31 July 1925",
            "access_date": "2026-10-18",
            "source_quality": "A_direct_official",
            "collection_name": "The London Gazette",
            "rights_notes": "Used for Vincent John Sofiano's full name and RAF commission chronology.",
        },
        {
            "key": GAZETTE_1946,
            "stable_url": "https://www.thegazette.co.uk/London/issue/37827/supplement/6245/data.pdf",
            "archival_identifier": "London Gazette Issue 37827, supplement page 6245",
            "title": "Supplement to The London Gazette, Issue 37827",
            "author_creator": "Air Ministry",
            "repository_publisher": "The Gazette, United Kingdom",
            "publication_record_date": "1946-12-24",
            "locator": "Supplement page 6245; entry records 26 May 1940 reserve transfer and wartime call-up",
            "access_date": "2026-10-18",
            "source_quality": "A_direct_official",
            "collection_name": "The London Gazette",
            "rights_notes": "The notice was published after the war but explicitly records the 1940 RAF event.",
        },
        {
            "key": WAPO_SUTTON,
            "stable_url": "https://www.washingtonpost.com/archive/local/1977/05/25/henry-sutton-retired-cia-aide-fled-austria-paris-before-nazis/249b9437-0e88-45f5-bc63-1db2f3054a36/",
            "title": "Henry Sutton, Retired CIA Aide, Fled Austria, Paris Before Nazis",
            "repository_publisher": "The Washington Post",
            "publication_record_date": "1977-05-25",
            "locator": "Biographical paragraphs on Austrian union activity, refugee work, Army enlistment and OSS assignment",
            "access_date": "2026-10-18",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "rights_notes": "The obituary supplies explicit chronology but not an exact OSS assignment date. Excerpts total fewer than 25 words; unrelated family and medical details are excluded.",
        },
        {
            "key": CIA_SUTTON,
            "stable_url": "https://www.cia.gov/readingroom/docs/CIA-RDP88-01350R000200230019-9.pdf",
            "archival_identifier": "CIA-RDP88-01350R000200230019-9",
            "title": "Article Appeared: profile of OSS veterans including Henry Sutton",
            "repository_publisher": "CIA Freedom of Information Act Electronic Reading Room",
            "locator": "Profile passage identifying Henry Sutton's birth name and Austrian union background",
            "access_date": "2026-10-18",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "CIA FOIA Electronic Reading Room",
            "document_number": "CIA-RDP88-01350R000200230019-9",
            "rights_notes": "The Reading Room holds a periodical clipping rather than a CIA-authored biography. It is used with the index identifier crosswalk and not as sole evidence.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": "army-air-corps-b895",
            "organization_id": "27378252-f855-504f-b916-d3fb6fb40fd0",
            "canonical_name": "United States Army Air Corps",
            "historical_name": "U.S. Army Air Corps",
            "aliases": ["Army Air Corps"],
            "organization_type": "military air arm",
            "sector": "military",
            "country": "United States",
            "active_dates": "1926-1941; name retained colloquially after reorganization",
            "normalization_notes": "The National Park Service uses the historical wording Army Air Corps; it is not silently modernized to the U.S. Air Force.",
        },
        {
            "key": "us-army-b895",
            "organization_id": "0c4e35ec-7297-5e38-a871-3742b6eac546",
            "canonical_name": "United States Army",
            "historical_name": "United States Army",
            "aliases": ["U.S. Army"],
            "organization_type": "military service",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "Army service is modeled as a military assignment, never as civilian employment.",
        },
        {
            "key": "royal-air-force-b895",
            "organization_id": "48ee5835-b4bd-58f5-8be5-99e6928decea",
            "canonical_name": "Royal Air Force",
            "historical_name": "Royal Air Force",
            "aliases": ["RAF"],
            "organization_type": "military air force",
            "sector": "military",
            "country": "United Kingdom",
            "active_dates": "1918-present",
            "normalization_notes": "The Gazette and OSS board both identify Sofiano with the RAF; no civilian-employer inference is made.",
        },
        {
            "key": "carinthia-white-collar-union-b895",
            "canonical_name": "White Collar Workers Union in Carinthia province",
            "historical_name": "White Collar Workers Union in Corinthia province",
            "aliases": ["Austrian white-collar workers' union"],
            "organization_type": "trade union",
            "sector": "labor_nonprofit_and_religion",
            "state_or_region": "Carinthia",
            "country": "Austria",
            "normalization_notes": "The Washington Post spells the province 'Corinthia.' The source wording is preserved in the historical field; the organization is not silently equated with a broader national union.",
        },
    ]


def army_occupation_affiliation(item: dict[str, object]) -> dict[str, object]:
    person_id, _name = PEOPLE[int(item["row"])]
    return {
        "key": f"{item['slug']}-occupation-b895",
        "person_id": person_id,
        "relationship_type": "unknown",
        "occupation": item["occupation"],
        "end_date": item["date"],
        "date_precision": f"Historical civilian-occupation code {item['code']} was recorded at Army entry on {item['date']}; no employer or OSS-transfer date is named.",
        "country": "United States",
        "immediate_pre_oss": False,
        "last_civilian_pre_service": False,
        "pre_oss_temporal_basis": "strongly_date_bounded",
        "identity_confidence": "confirmed" if int(item["row"]) == 43 else "high_confidence",
        "claim_confidence": "medium",
        "source_quality": "A_direct_official",
        "publication_status": "publish_qualified",
        "research_notes": "The historical occupation category is not converted into a named employer, workplace or exact job title.",
    }


def army_occupation_claim(item: dict[str, object]) -> dict[str, object]:
    person_id, name = PEOPLE[int(item["row"])]
    return {
        "key": f"occupation-{item['slug']}-b895",
        "person_id": person_id,
        "affiliation_key": f"{item['slug']}-occupation-b895",
        "claim_type": "occupation",
        "claim_text": f"At Army entry on {item['date']}, {name} was recorded in the historical {str(item['occupation']).lower()} category; no employer is identified.",
        "evidence_paraphrase": f"The accepted Army record carries civilian-occupation code {item['code']}, decoded from NARA's official code list.",
        "identity_match_assessment": "The occupation belongs only to the reviewed protected-identifier match; the identifier itself is not public.",
        "temporal_assessment": "Strongly date-bounded to Army entry; it does not establish the immediate pre-OSS affiliation or a named employer.",
        "source_quality": "A_direct_official",
        "claim_confidence": "medium",
        "publication_status": "publish_qualified",
        "match_notes": "The historical category is a qualified lead, not an employer, workplace or exact title.",
        "sources": [
            {"source_key": ARMY, "locator_override": f"Accepted reviewed identity record; civilian occupation code {item['code']}; protected identifier withheld"},
            {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46; Army-entry-date and civilian-occupation fields"},
            {"source_key": CODES, "locator_override": item["code_locator"], "excerpt_override": item["occupation"]},
        ],
    }


def generic_army_identity_claim(row: int) -> dict[str, object]:
    person_id, name = PEOPLE[row]
    return {
        "key": f"identity-page437-row{row}-b895",
        "person_id": person_id,
        "claim_type": "identity",
        "claim_text": f"The indexed {name} row on PDF page 437 is a high-confidence match to the reviewed official Army record.",
        "evidence_paraphrase": "The exact indexed name and a nonshared protected identifier agree with the reviewed Army record.",
        "identity_match_assessment": "High confidence from exact-name agreement and a nonshared protected-identifier bridge.",
        "temporal_assessment": "The Army-entry record supports identity and a dated occupation category; it does not establish the OSS transfer sequence.",
        "source_quality": "A_direct_official",
        "claim_confidence": "high",
        "publication_status": "published",
        "match_notes": "No protected identifier is exposed, and no same-name entity is merged by name alone.",
        "sources": [
            {"source_key": INDEX, "locator_override": f"PDF page 437 row {row}; protected identifier withheld"},
            {"source_key": ARMY, "locator_override": "Accepted reviewed identity bridge; protected identifier withheld"},
        ],
    }


def substantive_affiliations() -> list[dict[str, object]]:
    return [
        {
            "key": "jacques-snyder-army-air-corps-language-school-b895",
            "person_id": PEOPLE[27][0],
            "organization_key": "army-air-corps-b895",
            "organization_name_as_found": "U.S. Army Air Corps language training school in Tennessee",
            "role_title": "French-language trainee",
            "occupation": "military language trainee",
            "relationship_type": "military_assignment",
            "start_date": "1942",
            "end_date": "1943",
            "date_precision": "The NPS account places Army Air Corps enlistment and Tennessee language training after U.S. entry into the war and immediately before an OSS recruiter approached Snyder in the hospital; exact dates are not supplied.",
            "state_or_region": "Tennessee",
            "country": "United States",
            "immediate_pre_oss": True,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "explicit_immediate",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "A_direct_official",
            "publication_status": "published",
            "research_notes": "This is a military training assignment, not a civilian employer or identified school.",
        },
        {
            "key": "jacques-snyder-canadian-forces-b895",
            "person_id": PEOPLE[27][0],
            "organization_name_as_found": "Canadian armed forces",
            "role_title": "service member",
            "relationship_type": "military_assignment",
            "end_date": "1942",
            "date_precision": "The NPS account places this before Snyder enlisted in the U.S. Army Air Corps after U.S. entry into the war; the branch and exact dates are not named.",
            "country": "Canada",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "A_direct_official",
            "publication_status": "published",
            "research_notes": "The institution is preserved exactly as described because the source does not identify a Canadian service branch.",
        },
        {
            "key": "heinrich-soffner-us-army-b895",
            "person_id": PEOPLE[43][0],
            "organization_key": "us-army-b895",
            "organization_name_as_found": "U.S. Army",
            "role_title": "private",
            "relationship_type": "military_assignment",
            "start_date": "1943-12-06",
            "date_precision": "The Army record dates entry to 6 December 1943; the obituary explicitly sequences Army enlistment before assignment to OSS but supplies no transfer date.",
            "country": "United States",
            "immediate_pre_oss": True,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "explicit_immediate",
            "identity_confidence": "confirmed",
            "claim_confidence": "high",
            "source_quality": "A_direct_official",
            "publication_status": "published",
            "research_notes": "Army service is the explicit immediate OSS pathway. It is not civilian employment.",
        },
        {
            "key": "heinrich-soffner-white-collar-union-b895",
            "person_id": PEOPLE[43][0],
            "organization_key": "carinthia-white-collar-union-b895",
            "organization_name_as_found": "White Collar Workers Union in Corinthia province",
            "role_title": "head",
            "occupation": "trade-union official",
            "relationship_type": "professional_affiliation",
            "start_date": "1928",
            "end_date": "1933",
            "date_precision": "The obituary says late 1920s and early 1930s; year bounds are approximate and do not imply continuous service for the entire range.",
            "state_or_region": "Carinthia",
            "country": "Austria",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "confirmed",
            "claim_confidence": "medium",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "publish_qualified",
            "research_notes": "The source establishes union leadership but does not establish salaried employment, so the relationship is not counted as an employer.",
        },
        {
            "key": "heinrich-soffner-austrian-refugee-organization-b895",
            "person_id": PEOPLE[43][0],
            "organization_name_as_found": "an Austrian refugee organization in Paris",
            "role_title": "head",
            "relationship_type": "professional_affiliation",
            "start_date": "1938",
            "end_date": "1940",
            "date_precision": "The obituary places the Paris role after flight from Austria in the late 1930s and before flight to Portugal ahead of the German invasion of France; the organization and exact dates are unnamed.",
            "city": "Paris",
            "country": "France",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "confirmed",
            "claim_confidence": "medium",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "publish_qualified",
            "research_notes": "The organization remains unnamed; no canonical institution or employer is invented.",
        },
        {
            "key": "vincent-sofiano-royal-air-force-b895",
            "person_id": PEOPLE[45][0],
            "organization_key": "royal-air-force-b895",
            "organization_name_as_found": "Royal Air Force",
            "role_title": "Group Captain",
            "relationship_type": "military_assignment",
            "start_date": "1925-07-31",
            "end_date": "1945-08-21",
            "date_precision": "The Gazette confirms the 1925 permanent commission and 26 May 1940 wartime call-up; an OSS SI Branch awards survey identifies Group Captain V. J. Sofiano as RAF on 21 August 1945. The exact OSS attachment date is not supplied.",
            "country": "United Kingdom",
            "immediate_pre_oss": True,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "A_direct_official",
            "publication_status": "published",
            "research_notes": "The evidence supports an RAF pathway or attachment into OSS, not civilian employment or an exact transfer date.",
        },
    ]


def substantive_claims() -> list[dict[str, object]]:
    return [
        {
            "key": "identity-jacques-f-snyder-b895",
            "person_id": PEOPLE[27][0],
            "claim_type": "identity",
            "claim_text": "The indexed Jacques F Snyder is a high-confidence match to the Army Air Corps serviceman whom an OSS recruiter approached during hospitalization.",
            "evidence_paraphrase": "The rare exact name, index rank, reviewed Army identifier and NPS account of Army Air Corps and OSS service align.",
            "identity_match_assessment": "High confidence from an exact protected-identifier Army bridge plus an independent official biography using the rare full name and documenting OSS recruitment.",
            "temporal_assessment": "The NPS account explicitly sequences Canadian service, U.S. Army Air Corps language training and OSS recruitment.",
            "source_quality": "A_direct_official",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "The Army record shows private at entry and the index later shows first lieutenant; the ranks are chronologically compatible rather than conflicting.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 437 row 27; First Lieutenant; protected identifier withheld"},
                {"source_key": ARMY, "locator_override": "Accepted reviewed identity bridge; Army entry 18 September 1942; protected identifier withheld"},
                {"source_key": NPS_SNYDER, "locator_override": "Jacques F. Snyder biographical passage"},
            ],
        },
        {
            "key": "military-jacques-snyder-air-corps-b895",
            "person_id": PEOPLE[27][0],
            "affiliation_key": "jacques-snyder-army-air-corps-language-school-b895",
            "claim_type": "immediate_pre_oss_affiliation",
            "claim_text": "Jacques F. Snyder was in an Army Air Corps language-training school in Tennessee immediately before an OSS recruiter approached him in the hospital.",
            "evidence_paraphrase": "The NPS biography explicitly connects Snyder's fluent French, Tennessee military language training, hospitalization and OSS recruitment.",
            "identity_match_assessment": "High confidence from the rare exact name, accepted Army bridge and OSS-specific official biography.",
            "temporal_assessment": "Explicitly immediate in the source sequence; exact school, course and recruitment dates are not given.",
            "source_quality": "A_direct_official",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "The school is not named, and neither it nor the Army Air Corps is described as a civilian employer.",
            "sources": [
                {"source_key": NPS_SNYDER, "locator_override": "Jacques F. Snyder biographical passage", "excerpt_override": "because of his fluent French, he was put in a language training school in Tennessee"},
                {"source_key": ARMY, "support_type": "context_only", "locator_override": "Army entry 18 September 1942; protected identifier withheld"},
            ],
        },
        {
            "key": "military-jacques-snyder-canadian-forces-b895",
            "person_id": PEOPLE[27][0],
            "affiliation_key": "jacques-snyder-canadian-forces-b895",
            "claim_type": "other_pre_oss_affiliation",
            "claim_text": "Before U.S. Army Air Corps service, Jacques F. Snyder served in the Canadian armed forces; the source does not name a branch.",
            "evidence_paraphrase": "The NPS account explicitly places Canadian military service before U.S. entry into the war and Snyder's later U.S. enlistment.",
            "identity_match_assessment": "High confidence from the same rare-name, Army and OSS evidence.",
            "temporal_assessment": "Documented pre-OSS military service, but not the immediate affiliation and not a civilian employer.",
            "source_quality": "A_direct_official",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "The generic source wording is preserved; no Canadian branch is inferred.",
            "sources": [
                {"source_key": NPS_SNYDER, "locator_override": "Jacques F. Snyder biographical passage", "excerpt_override": "He joined the Canadian armed forces"},
            ],
        },
        {
            "key": "identity-franciszek-sobecki-b895",
            "person_id": PEOPLE[37][0],
            "claim_type": "identity",
            "claim_text": "The indexed Major Franciszek Sobecki is confirmed in a contemporaneous OSS record as a Polish Army major who contributed to OSS operations.",
            "evidence_paraphrase": "A 19 July 1945 OSS Mission to France award record names Major Franciszek Sobecki, Polish Army, and describes his contribution to OSS operations.",
            "identity_match_assessment": "Confirmed by the rare exact full name, matching major rank and Polish Army note in both the index and a contemporaneous OSS record.",
            "temporal_assessment": "The record establishes wartime identity and Allied military status in July 1945; it does not establish the pre-OSS sequence.",
            "source_quality": "A_direct_official",
            "claim_confidence": "confirmed",
            "publication_status": "published",
            "match_notes": "No immediate pre-OSS affiliation or civilian employer is inferred from the award record.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 437 row 37; Major; note 'Polish Ar'"},
                {"source_key": NARA_AWARDS, "locator_override": "PDF physical page 79; 19 July 1945 Unit Certificate of Merit", "excerpt_override": "his invaluable contribution to the successful operations of the Office of Strategic Services"},
            ],
        },
        {
            "key": "identity-heinrich-soffner-henry-sutton-b895",
            "person_id": PEOPLE[43][0],
            "claim_type": "identity",
            "claim_text": "Heinrich C. Soffner and the separately indexed Henry C. Sutton record with the same protected identifier represent one confirmed person.",
            "evidence_paraphrase": "The official index repeats one protected identifier under both names; the CIA-held article independently says Henry Sutton was born Heinrich Sofner, and the Army record uses Henry C Sutton.",
            "identity_match_assessment": "Confirmed by the unique protected-identifier crosswalk across two immutable index rows plus independent explicit alias evidence.",
            "temporal_assessment": "The alias evidence and Army entry are wartime identity evidence; they do not by themselves establish civilian employment chronology.",
            "source_quality": "A_direct_official",
            "claim_confidence": "confirmed",
            "publication_status": "published",
            "match_notes": "Both index rows remain preserved. The other Henry C Sutton row with a different identifier and the adjacent Heirich C Soffner row remain separate.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 437 row 43 and page 456 row 33; matching protected identifier withheld"},
                {"source_key": CIA_SUTTON, "locator_override": "Henry Sutton profile passage", "excerpt_override": "he was born Heinrich Sofner"},
                {"source_key": ARMY, "locator_override": "Accepted Henry C Sutton Army record; protected identifier withheld"},
            ],
        },
        {
            "key": "military-heinrich-soffner-us-army-b895",
            "person_id": PEOPLE[43][0],
            "affiliation_key": "heinrich-soffner-us-army-b895",
            "claim_type": "immediate_pre_oss_affiliation",
            "claim_text": "Henry C. Sutton, born Heinrich Soffner, entered the U.S. Army and was then assigned to OSS and sent to London.",
            "evidence_paraphrase": "The Washington Post explicitly sequences Army enlistment before OSS assignment; the reviewed Army record dates entry and records private grade.",
            "identity_match_assessment": "Confirmed through the protected-identifier alias crosswalk and explicit independent alias evidence.",
            "temporal_assessment": "Explicit immediate military pathway, although the exact OSS assignment date is not supplied.",
            "source_quality": "A_direct_official",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "U.S. Army service is a military assignment, not civilian employment.",
            "sources": [
                {"source_key": WAPO_SUTTON, "locator_override": "Wartime chronology paragraph", "excerpt_override": "He enlisted in the U.S. Army ... and was assigned to the OSS"},
                {"source_key": ARMY, "locator_override": "Army entry 6 December 1943; private grade; protected identifier withheld"},
                {"source_key": INDEX, "support_type": "context_only", "locator_override": "Matching Soffner and Sutton protected identifiers withheld"},
            ],
        },
        {
            "key": "union-heinrich-soffner-b895",
            "person_id": PEOPLE[43][0],
            "affiliation_key": "heinrich-soffner-white-collar-union-b895",
            "claim_type": "other_pre_oss_affiliation",
            "claim_text": "In the late 1920s and early 1930s, Henry Sutton was head of a white-collar workers' union in Carinthia province, Austria.",
            "evidence_paraphrase": "The Washington Post obituary explicitly identifies Sutton as an Austrian Social Democrat and provincial white-collar union leader.",
            "identity_match_assessment": "Confirmed identity from the independent alias bridge and matching protected identifier.",
            "temporal_assessment": "Documented prewar professional affiliation; the source does not establish salaried employment or immediacy before OSS.",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "claim_confidence": "medium",
            "publication_status": "publish_qualified",
            "match_notes": "The source's 'Corinthia' spelling is preserved; the relationship is not counted as an employer.",
            "sources": [
                {"source_key": WAPO_SUTTON, "locator_override": "Austrian political and union biography", "excerpt_override": "head of the White Collar Workers Union in Corinthia province"},
                {"source_key": CIA_SUTTON, "support_type": "context_only", "locator_override": "Austrian union-background passage"},
            ],
        },
        {
            "key": "refugee-organization-heinrich-soffner-b895",
            "person_id": PEOPLE[43][0],
            "affiliation_key": "heinrich-soffner-austrian-refugee-organization-b895",
            "claim_type": "other_pre_oss_affiliation",
            "claim_text": "In the late 1930s, Henry Sutton headed an unnamed Austrian refugee organization in Paris before fleeing to Portugal.",
            "evidence_paraphrase": "The obituary places the Paris refugee-organization role between flight from Austria and flight to Portugal before the German invasion of France.",
            "identity_match_assessment": "Confirmed identity from the protected-identifier alias crosswalk and explicit alias evidence.",
            "temporal_assessment": "Strongly date-bounded pre-OSS professional affiliation; it is not shown to be employment or the immediate predecessor.",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "claim_confidence": "medium",
            "publication_status": "publish_qualified",
            "match_notes": "The organization remains unnamed and is not normalized to an invented institution.",
            "sources": [
                {"source_key": WAPO_SUTTON, "locator_override": "Late-1930s refugee chronology paragraph"},
            ],
        },
        {
            "key": "identity-vincent-john-sofiano-b895",
            "person_id": PEOPLE[45][0],
            "claim_type": "identity",
            "claim_text": "The indexed Captain Vincent J Sofiano is a high-confidence match to RAF officer Vincent John Sofiano, listed by an OSS SI Branch awards board.",
            "evidence_paraphrase": "Official Gazette notices establish the exact full name and RAF chronology; the contemporaneous OSS board lists Gp Capt V. J. Sofiano (RAF) in its SI Branch survey.",
            "identity_match_assessment": "High confidence from rare surname, matching initials, compatible officer ranks and independent official RAF and OSS records.",
            "temporal_assessment": "The official records span the 1925 commission, 1940 wartime call-up and August 1945 OSS SI Branch award action.",
            "source_quality": "A_direct_official",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "The index's captain rank and the 1945 group-captain rank are chronologically compatible; no civilian career is inferred.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 437 row 45; Captain"},
                {"source_key": GAZETTE_1925, "locator_override": "Page 5770; RAF permanent commission list", "excerpt_override": "Vincent John SOFIANO"},
                {"source_key": NARA_AWARDS, "locator_override": "PDF physical pages 130 and 132-133; SI Branch survey approved 21 August 1945", "excerpt_override": "Gp Capt V. J. Sofiano (RAF)"},
            ],
        },
        {
            "key": "military-vincent-sofiano-royal-air-force-b895",
            "person_id": PEOPLE[45][0],
            "affiliation_key": "vincent-sofiano-royal-air-force-b895",
            "claim_type": "immediate_pre_oss_affiliation",
            "claim_text": "Vincent John Sofiano's documented wartime pathway into OSS was through the Royal Air Force; the exact attachment date is not available.",
            "evidence_paraphrase": "The Gazette records wartime RAF call-up on 26 May 1940, while the OSS SI Branch survey identifies him as an RAF group captain in August 1945.",
            "identity_match_assessment": "High confidence from the rare full name, initials, officer ranks and direct official records.",
            "temporal_assessment": "Strongly date-bounded military continuity into the OSS context, but the precise recruitment or attachment sequence remains unproven.",
            "source_quality": "A_direct_official",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "The RAF is modeled as a military assignment, not a civilian employer.",
            "sources": [
                {"source_key": GAZETTE_1925, "support_type": "context_only", "locator_override": "Page 5770; permanent commission"},
                {"source_key": GAZETTE_1946, "locator_override": "Supplement page 6245; event dated 26 May 1940", "excerpt_override": "and called up for Air Force service"},
                {"source_key": NARA_AWARDS, "locator_override": "PDF physical pages 130 and 132-133; OSS SI Branch survey"},
            ],
        },
    ]


def person_updates() -> list[dict[str, object]]:
    updates: list[dict[str, object]] = []

    for row in (24, 25, 36):
        person_id, _name = PEOPLE[row]
        updates.append({
            "person_id": person_id,
            "identity_status": "high_confidence",
            "identity_evidence": "Exact-name agreement plus a nonshared protected identifier connects the visually verified index row to the reviewed official Army record.",
            "personnel_category": "enlisted_army_personnel",
            "commissioned_officer": False,
            "allied_or_foreign_personnel": False,
            "manual_review_required": True,
            "research_status": "occupation_only_found",
            "next_action": "Review the indexed Box 727 personnel file to identify the immediate pre-OSS affiliation and last civilian employer; do not convert the Army occupation category into a named employer.",
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
            "archival_review_priority": "high",
        })

    updates.extend([
        {
            "person_id": PEOPLE[27][0],
            "identity_status": "high_confidence",
            "identity_evidence": "The rare exact name, a nonshared protected Army identifier and an official National Park Service biography explicitly documenting Army Air Corps and OSS service identify Jacques F. Snyder.",
            "personnel_category": "commissioned_army_officer",
            "commissioned_officer": True,
            "allied_or_foreign_personnel": False,
            "manual_review_required": True,
            "research_status": "requires_archival_review",
            "next_action": "Review Box 727 for the exact Army-Air-Corps-to-OSS transfer date, the Tennessee school and the last civilian employer before Canadian or U.S. military service.",
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
            "archival_review_priority": "high",
        },
        {
            "person_id": PEOPLE[37][0],
            "identity_status": "confirmed",
            "identity_evidence": "A contemporaneous OSS Mission to France record names Major Franciszek Sobecki, Polish Army, exactly matching the rare indexed name, rank and Polish Army note.",
            "personnel_category": "foreign_or_allied_military_personnel",
            "commissioned_officer": True,
            "allied_or_foreign_personnel": True,
            "manual_review_required": True,
            "research_status": "requires_archival_review",
            "next_action": "Review Box 727 and Polish military records for Sobecki's pre-OSS assignment, civilian occupation and exact OSS relationship; the 1945 award does not establish chronology before OSS.",
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
            "archival_review_priority": "high",
        },
        {
            "person_id": PEOPLE[43][0],
            "identity_status": "confirmed",
            "identity_evidence": "The same nonshared protected identifier appears under Heinrich C Soffner and Henry C Sutton in separate immutable index rows; a CIA Reading Room-held article explicitly says Sutton was born Heinrich Sofner, and the official Army record uses Henry C Sutton.",
            "name_variants": ["Henry C. Sutton", "Henry Sutton", "Heinz Soffner", "Heinrich Sofner"],
            "personnel_category": "enlisted_army_personnel",
            "commissioned_officer": False,
            "allied_or_foreign_personnel": False,
            "manual_review_required": True,
            "possible_duplicate_group": "p437-heinrich-heirich-soffner-b895",
            "research_status": "requires_archival_review",
            "next_action": "Review Boxes 728 and 759 together for the exact OSS assignment date, Austrian union records and any last civilian employer. The adjacent Heirich row remains a separate possible duplicate.",
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
            "archival_review_priority": "high",
        },
        {
            "person_id": PEOPLE[45][0],
            "identity_status": "high_confidence",
            "identity_evidence": "The rare surname, matching initials, compatible officer ranks, official Gazette notices for Vincent John Sofiano and a contemporaneous OSS SI Branch awards survey identify the indexed person.",
            "name_variants": ["Vincent John Sofiano", "V. J. Sofiano"],
            "personnel_category": "foreign_or_allied_military_personnel",
            "commissioned_officer": True,
            "allied_or_foreign_personnel": True,
            "manual_review_required": True,
            "research_status": "requires_archival_review",
            "next_action": "Review Box 728 and RAF service records for the exact attachment or recruitment date and any last civilian employer before wartime RAF service.",
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
            "archival_review_priority": "high",
        },
    ])

    for row, rejection in UNRESOLVED.items():
        person_id, name = PEOPLE[row]
        update: dict[str, object] = {
            "person_id": person_id,
            "identity_status": "ambiguous" if row == 38 else "unresolved",
            "identity_evidence": f"The visually verified index row supplies {name}, Box 727 or 728 and archive location, but staged official-context, exact-name, employment, occupation, obituary, institutional, directory and archival searches found no defensible identity bridge. {rejection}",
            "manual_review_required": True,
            "research_status": "requires_archival_review",
            "next_action": "Review the indexed personnel file for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
            "archival_review_priority": "critical",
        }
        if row in (43, 44):
            update["possible_duplicate_group"] = "p437-heinrich-heirich-soffner-b895"
        if row == 38:
            update["next_action"] = "Review Box 727 and the NARA Project Eagle/OLD FASHIONED files for an item-level alias bridge and pre-OSS Polish military chronology. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed."
        updates.append(update)
    return updates


def research_attempts() -> list[dict[str, object]]:
    attempts = []
    evidence_rows = {24, 25, 27, 36, 37, 43, 45}
    for row, (person_id, name) in PEOPLE.items():
        has_evidence = row in evidence_rows
        notes = UNRESOLVED.get(row, "Reviewed evidence established an identity bridge and, where supported, a carefully bounded military affiliation or occupation claim.")
        box = "727" if row <= 42 else "728"
        attempts.append({
            "key": f"page437-row{row}-{name.lower().replace(' ', '-').replace("'", '')}-b895",
            "person_id": person_id,
            "source_adapter": "manual_staged_protocol",
            "query_text": f"{name}; NARA/index context; CIA Reading Room or equivalent official-source check; exact-name OSS variants; employer and occupation; obituary, institutional, newspaper, directory and archival searches; Box {box}; protected-identifier Army crosswalk where available",
            "query_variant_type": "staged_identity_employment_archival_protocol_batch_895",
            "started_at": "2026-10-18T19:30:00Z",
            "completed_at": "2026-10-18T22:30:00Z",
            "outcome": "source_reviewed" if has_evidence else "candidate_rejected",
            "sources_reviewed": 9 if has_evidence else 5,
            "candidate_sources_rejected": 5 if has_evidence else 7,
            "rejection_reasons": "Unbridged namesakes, chronologically irrelevant results and materially conflicting candidates were not assigned." if has_evidence else notes,
            "research_notes": ("Reviewed evidence established a supported identity; public affiliation claims are limited to what the cited sources prove. " if has_evidence else "No reliable identity or pre-OSS employer was established after the staged search and namesake-rejection protocol. ") + notes + " Search-result snippets were discovery aids only, no paywall or access control was bypassed, and no exposed NARA API credential was used.",
            "next_action": f"Review the indexed Box {box} personnel file.",
            "attempt_number": 1,
            "research_agent_version": "before-oss-b895-v1",
        })
    return attempts


def main() -> None:
    affiliations = [army_occupation_affiliation(item) for item in ARMY_MATCHES]
    affiliations.extend(substantive_affiliations())

    claims = [generic_army_identity_claim(row) for row in (24, 25, 36)]
    claims.extend(army_occupation_claim(item) for item in ARMY_MATCHES)
    claims.extend(substantive_claims())

    bundle = {
        "bundle_version": "batch-895-v1",
        "reviewer": "Before OSS Batch 895 evidence review",
        "sources": sources(),
        "organizations": organizations(),
        "affiliations": affiliations,
        "claims": claims,
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }
    OUTPUT.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
