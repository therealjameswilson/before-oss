#!/usr/bin/env python3
"""Generate the reviewed Batch 893 evidence bundle from audited constants."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "research/evidence-page436-smith-to-smyser-review_batch-893_2026-10-18.json"

INDEX = "nara-index-b893"
ARMY = "army-bulk-b893"
TECH = "army-tech-b893"
CODES = "army-codes-b893"
WAS_BIO = "william-arthur-smith-biography-b893"
MDTA = "mdta-william-arthur-smith-b893"
UAA = "uaa-richard-d-smyser-b893"
GAZETTE_1936 = "london-gazette-smith-ross-1936-b893"
GAZETTE_1946 = "london-gazette-smith-ross-1946-b893"
HOOVER = "hoover-oss-smolianinoff-b893"
GEORGETOWN = "georgetown-jane-smith-hutton-b893"


PEOPLE = {
    24: ("da91124a-89fd-5e93-a846-e2411303eca1", "William M Smith"),
    25: ("3dbc5bde-2890-5e97-89d1-6ce225b533bf", "William H Smith"),
    26: ("c1c4e791-d7db-5424-a3c2-9f9b15a14021", "William C Smith"),
    27: ("157e35dc-5ebf-54d0-ab54-17c138da29c4", "William A Smith"),
    28: ("52f1f635-8b61-5c8f-8d7c-4db2864c48f1", "William Smith"),
    29: ("a44e8306-6b97-56bb-b79b-daaf4bec5f55", "William J Smith"),
    30: ("6b5293b4-d121-50da-85bf-9384db948774", "Williard E Smith"),
    31: ("432ee618-a5b0-5ed8-90c0-de392c13a3f0", "Wilma D Smith"),
    32: ("b5dcf046-1647-5a06-9d4f-04427707332f", "Wingate Smith"),
    33: ("a790cb51-5723-5a1e-b72f-e4dbd5c91c50", "Wylie D Smith"),
    34: ("c2381c10-0242-5f17-9bcb-c2b9537a8d73", "F E Smither"),
    35: ("a5740231-e0d5-5cb4-a5a6-549184194458", "Jane Smith-Hutton"),
    36: ("0b2ae5c2-e6e1-57c2-a479-734c39218e2a", "Frank R Smithka"),
    37: ("eee04cc0-07ae-5122-a7b3-737c40d5efb7", "Edward C Smith-Ross"),
    38: ("c619eabc-8dd2-55d2-9ced-4b785735f98b", "Andre V Smolianinoff"),
    39: ("588469b6-d7eb-51ba-97fe-739fa48a9e66", "Frank G Smolinski"),
    40: ("f836650c-0c21-5ee1-97fd-d61286a7a704", "Carl A Smollar"),
    41: ("2d2f5d8d-dbd9-5be0-baa0-3e2276a8de58", "Carl A Smollar"),
    42: ("81d58579-038d-598b-ba59-f7f8ced3e994", "Nick Smoltz"),
    43: ("19132dd2-ba41-554f-80cd-be5a2293ec28", "Roy W Smurr"),
    44: ("b13c4730-5346-509d-9509-2d15545b04e2", "Laura Z Smusz"),
    45: ("6d81be1b-1aa6-5a9c-b710-6201005ad163", "Rost R Smylie"),
    46: ("de95bdf0-f67e-5e8c-9216-481a3b5e322f", "Richard D Smyser"),
}


ARMY_MATCHES = [
    {
        "row": 26,
        "slug": "william-c-smith",
        "date": "1943-04-13",
        "code": "736",
        "occupation": "Chauffeurs and drivers, bus, taxi, truck, and tractor",
        "code_locator": "PDF physical page 174; civilian occupation category 7-36",
    },
    {
        "row": 27,
        "slug": "william-a-smith",
        "date": "1944-05-29",
        "code": "044",
        "occupation": "Commercial artists",
        "code_locator": "PDF physical page 171; civilian occupation category 0-44",
    },
    {
        "row": 39,
        "slug": "frank-g-smolinski",
        "date": "1943-04-20",
        "code": "316",
        "occupation": "Farm hands, general farms",
        "code_locator": "PDF physical page 172; civilian occupation category 3-16",
    },
    {
        "row": 41,
        "slug": "carl-a-smollar-row41",
        "date": "1942-01-30",
        "code": "721",
        "occupation": "Miners and mining-machine operators",
        "code_locator": "PDF physical page 174; civilian occupation category 7-21",
    },
    {
        "row": 45,
        "slug": "rost-r-smylie",
        "date": "1943-02-11",
        "code": "592",
        "occupation": "Foremen, manufacturing",
        "code_locator": "PDF physical page 175; civilian occupation category 5-92",
    },
]


UNRESOLVED = {
    24: "The protected identifier produced no Army candidate, and common-name results lacked an OSS or Box 726 bridge. A non-hit is not negative proof.",
    28: "The no-initial name is exceptionally ambiguous; exact-name and occupation searches produced numerous unbridged namesakes.",
    29: "The protected identifier also appears on indexed Alexander J Soto. The conflicting rows remain separate, and no Army evidence is transferred.",
    30: "The index spelling Williard is preserved. Directory and other exact-name results lacked an OSS or Box 726 bridge.",
    31: "Genealogical and contemporary namesakes lacked an OSS, protected-identifier or Box 726 bridge.",
    32: "An American Film Institute assistant-director namesake is a lead only; no source connects that career to the indexed captain or Box 726 file.",
    33: "Public-record namesakes were unbridged or chronologically incompatible with the indexed row.",
    34: "The initials-only record is highly ambiguous, and staged employment and archival searches found no defensible identity bridge.",
    36: "The protected identifier produced no Army candidate, and exact-name searches found no independent OSS or Box 726 bridge. A non-hit is not negative proof.",
    40: "This first Carl A Smollar row has no protected identifier. Evidence accepted for the second same-name row is not transferred.",
    42: "Obituary-family and aircraft-name results did not establish that Nicholas or Nick Smoltz was the indexed person.",
    43: "A burial-record namesake supplied possible dates but no OSS, protected-identifier or Box 726 bridge.",
    44: "Exact-name, employment, obituary, institutional and archival searches produced no usable identity bridge.",
}


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Box 726",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 436, rows 24-46; checked against layout-preserving text and a rendered page image",
            "access_date": "2026-10-18",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain preserved. Full protected identifiers remain private and are masked from public data.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; protected-identifier fields checked, seven matches accepted and two conflicts rejected after review",
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
            "locator": "PDF physical pages 171-175 and 304; categories 044, 316, 592, 721, 736 and 992 visually checked; 345 is unassigned",
            "access_date": "2026-10-18",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical labels name neither employers nor workplaces. Code 345 is not converted into an occupation.",
        },
        {
            "key": WAS_BIO,
            "stable_url": "https://www.weihsien-paintings.org/StanleyFairchild/Sketches/text/WilliamSmith.htm",
            "title": "William A. Smith Biography",
            "author_creator": "David Leopold",
            "repository_publisher": "Weihsien Paintings; biography prepared for the Studio of Ben Solowey",
            "publication_record_date": "1996",
            "locator": "Biographical essay; paragraphs on newspaper work, Manhattan freelance illustration and OSS recruitment",
            "access_date": "2026-10-18",
            "source_quality": "D_correlative_or_secondary",
            "collection_name": "Stanley Fairchild Sketches",
            "rights_notes": "Only short evidence excerpts and project-authored paraphrases are retained.",
        },
        {
            "key": MDTA,
            "stable_url": "https://www.mdta.maryland.gov/FormerMarylandHouseMurals",
            "title": "Former Maryland House Murals",
            "author_creator": "Maryland Transportation Authority",
            "repository_publisher": "Maryland Transportation Authority",
            "locator": "Section identifying mural artist William Arthur Smith (1918-1989)",
            "access_date": "2026-10-18",
            "source_quality": "B_authoritative_institutional",
            "rights_notes": "Used to corroborate the full name and illustrator identity; it does not establish pre-OSS employment.",
        },
        {
            "key": UAA,
            "stable_url": "https://www.uaa.alaska.edu/academics/college-of-arts-and-sciences/departments/journalism-and-communication/atwood-chair-of-journalism/our-past-chairs.cshtml",
            "title": "Our Past Chairs: Richard D. 'Dick' Smyser",
            "author_creator": "University of Alaska Anchorage",
            "repository_publisher": "University of Alaska Anchorage",
            "locator": "Richard D. Smyser biographical entry; identifies 1944 Pennsylvania State University graduation",
            "access_date": "2026-10-18",
            "source_quality": "B_authoritative_institutional",
            "rights_notes": "Used with the official Army student record to identify the institution; postwar career details are not reconstructed.",
        },
        {
            "key": GAZETTE_1936,
            "stable_url": "https://www.thegazette.co.uk/London/issue/34281/page/2899/data.pdf",
            "archival_identifier": "The London Gazette, issue 34281, page 2899",
            "title": "The London Gazette, 5 May 1936",
            "author_creator": "Air Ministry",
            "repository_publisher": "The Gazette",
            "publication_record_date": "1936-05-05",
            "locator": "Page 2899; Royal Air Force promotion effective 1 April 1936",
            "access_date": "2026-10-18",
            "source_quality": "A_direct_official",
            "rights_notes": "Official notice used to establish the full name, RAF affiliation and dated rank.",
        },
        {
            "key": GAZETTE_1946,
            "stable_url": "https://www.thegazette.co.uk/London/issue/37534/supplement/1903/data.pdf",
            "archival_identifier": "The London Gazette, issue 37534, supplement page 1903",
            "title": "The London Gazette, 16 April 1946",
            "author_creator": "Central Chancery of the Orders of Knighthood",
            "repository_publisher": "The Gazette",
            "publication_record_date": "1946-04-16",
            "locator": "Supplement page 1903; Wing Commander Edward Charles Smith-Ross, OBE, RAFO, listed with the United States Legion of Merit",
            "access_date": "2026-10-18",
            "source_quality": "A_direct_official",
            "rights_notes": "Used as identity and rank-continuity corroboration, not as pre-OSS employment evidence.",
        },
        {
            "key": HOOVER,
            "stable_url": "https://digitalcollections.hoover.org/internal/media/dispatcher/266796/full",
            "title": "By Oct., 127 agents trained and landed in occupied countries",
            "author_creator": "Office of Strategic Services",
            "repository_publisher": "Hoover Institution Library & Archives",
            "locator": "PDF page 47; Special Operations recruiting desk for Yugoslavia, Albania and Greece",
            "access_date": "2026-10-18",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Hoover Institution Digital Collections",
            "rights_notes": "Used only to corroborate identity and wartime U.S. Navy lieutenant status; it does not establish a pre-OSS affiliation.",
        },
        {
            "key": GEORGETOWN,
            "stable_url": "https://findingaids.library.georgetown.edu/repositories/15/archival_objects/1453338",
            "archival_identifier": "GTM-220705, Box 1, Folder 13",
            "title": "Miscellaneous: OSS Oral History Project, 1945-1996",
            "author_creator": "OSS Oral History Project",
            "repository_publisher": "Georgetown University Manuscripts, Booth Family Center for Special Collections",
            "publication_record_date": "1945-1996",
            "locator": "Box 1, Folder 13; finding-aid description names biographical information on Jane Smith-Hutton",
            "access_date": "2026-10-18",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "OSS Oral History Project Records",
            "rights_notes": "The finding aid corroborates identity and OSS research context but does not establish an assignment or pre-OSS employer.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": "scripps-howard-b893",
            "canonical_name": "Scripps-Howard Newspapers",
            "historical_name": "Scripps-Howard Newspapers",
            "aliases": ["Scripps-Howard"],
            "organization_type": "newspaper chain",
            "sector": "journalism_and_media",
            "country": "United States",
            "normalization_notes": "The historical name in the source is preserved; no modern successor is substituted.",
        },
        {
            "key": "san-francisco-examiner-b893",
            "canonical_name": "San Francisco Examiner",
            "historical_name": "San Francisco Examiner",
            "aliases": [],
            "organization_type": "newspaper",
            "sector": "journalism_and_media",
            "city": "San Francisco",
            "state_or_region": "California",
            "country": "United States",
            "normalization_notes": "The newspaper named by the biographical source is retained without corporate-parent inference.",
        },
        {
            "key": "self-employed-illustrator-b893",
            "canonical_name": "Self-employed illustrator",
            "historical_name": "Freelance illustrator",
            "aliases": ["Freelance artist"],
            "organization_type": "self-employment",
            "sector": "self_employed",
            "city": "New York City",
            "state_or_region": "New York",
            "country": "United States",
            "normalization_notes": "A separate self-employment entity prevents magazine clients from being mislabeled as employers.",
        },
        {
            "key": "royal-air-force-b893",
            "canonical_name": "Royal Air Force",
            "historical_name": "Royal Air Force",
            "aliases": ["RAF"],
            "organization_type": "military service",
            "sector": "military",
            "country": "United Kingdom",
            "normalization_notes": "The official historical service name is preserved.",
        },
        {
            "key": "penn-state-b893",
            "canonical_name": "Pennsylvania State University",
            "historical_name": "Pennsylvania State University",
            "aliases": ["Penn State"],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "State College",
            "state_or_region": "Pennsylvania",
            "country": "United States",
            "normalization_notes": "Student status is kept distinct from employment.",
        },
    ]


def army_identity_claim(row: int, postwar: bool = False) -> dict[str, object]:
    person_id, name = PEOPLE[row]
    temporal = (
        "The matched Army entry is dated 1946, after the OSS period, and supports identity only."
        if postwar
        else "The Army-entry record supports identity and a dated occupation category; it does not establish the OSS transfer sequence."
    )
    return {
        "key": f"identity-page436-row{row}-b893",
        "person_id": person_id,
        "claim_type": "identity",
        "claim_text": f"The indexed {name} row on PDF page 436 is a high-confidence match to the official Army bulk record.",
        "evidence_paraphrase": "The exact indexed name and a nonshared protected identifier agree with the reviewed official Army record.",
        "identity_match_assessment": "High confidence from exact-name agreement plus a nonshared protected-identifier bridge.",
        "temporal_assessment": temporal,
        "source_quality": "A_direct_official",
        "claim_confidence": "high",
        "publication_status": "published",
        "match_notes": "No protected identifier is exposed, and same-name source rows are not merged.",
        "sources": [
            {"source_key": INDEX, "locator_override": f"PDF page 436 row {row}; protected identifier withheld"},
            {"source_key": ARMY, "locator_override": "Accepted reviewed identity bridge; protected identifier withheld"},
        ],
    }


def army_occupation_affiliation(item: dict[str, object]) -> dict[str, object]:
    person_id, _name = PEOPLE[int(item["row"])]
    return {
        "key": f"{item['slug']}-occupation-b893",
        "person_id": person_id,
        "relationship_type": "unknown",
        "occupation": item["occupation"],
        "end_date": item["date"],
        "date_precision": f"Historical civilian-occupation code {item['code']} was recorded at Army entry on {item['date']}; no employer or OSS-transfer date is named.",
        "country": "United States",
        "immediate_pre_oss": False,
        "last_civilian_pre_service": False,
        "pre_oss_temporal_basis": "strongly_date_bounded",
        "identity_confidence": "high_confidence",
        "claim_confidence": "medium",
        "source_quality": "A_direct_official",
        "publication_status": "publish_qualified",
        "research_notes": "The historical occupation category is not converted into a named employer or exact job title.",
    }


def army_occupation_claim(item: dict[str, object]) -> dict[str, object]:
    person_id, name = PEOPLE[int(item["row"])]
    return {
        "key": f"occupation-{item['slug']}-b893",
        "person_id": person_id,
        "affiliation_key": f"{item['slug']}-occupation-b893",
        "claim_type": "occupation",
        "claim_text": f"At Army entry on {item['date']}, {name} was recorded in the historical {str(item['occupation']).lower()} category; no employer is identified.",
        "evidence_excerpt": item["occupation"],
        "evidence_paraphrase": f"The accepted Army record carries civilian-occupation code {item['code']}, decoded from NARA's official code list.",
        "identity_match_assessment": "The occupation category belongs only to the accepted protected-identifier match for this index row.",
        "temporal_assessment": "Strongly date-bounded to Army entry; it does not establish the immediate pre-OSS affiliation or a named employer.",
        "source_quality": "A_direct_official",
        "claim_confidence": "medium",
        "publication_status": "publish_qualified",
        "match_notes": "The historical occupation category is reported as a qualified lead, not as an employer or exact title.",
        "sources": [
            {"source_key": ARMY, "locator_override": f"Accepted reviewed identity record; civilian occupation code {item['code']}; protected identifier withheld"},
            {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46; Army-entry-date and civilian-occupation fields"},
            {"source_key": CODES, "locator_override": item["code_locator"], "excerpt_override": item["occupation"]},
        ],
    }


def william_a_affiliations() -> list[dict[str, object]]:
    person_id = PEOPLE[27][0]
    base = {
        "person_id": person_id,
        "country": "United States",
        "immediate_pre_oss": False,
        "last_civilian_pre_service": False,
        "pre_oss_temporal_basis": "documented_prewar",
        "identity_confidence": "high_confidence",
        "claim_confidence": "medium",
        "source_quality": "D_correlative_or_secondary",
        "publication_status": "publish_qualified",
    }
    return [
        {
            **base,
            "key": "william-a-smith-scripps-howard-b893",
            "organization_key": "scripps-howard-b893",
            "organization_name_as_found": "Scripps-Howard Newspapers",
            "role_title": "sketch artist",
            "occupation": "commercial artist",
            "relationship_type": "employment",
            "start_date": "1932",
            "end_date": "1932",
            "date_precision": "The biography places the work at the 1932 Los Angeles Olympics; it does not supply exact employment dates.",
            "city": "Los Angeles",
            "state_or_region": "California",
            "research_notes": "Earlier documented prewar work; not shown to be the immediate pre-OSS affiliation.",
        },
        {
            **base,
            "key": "william-a-smith-examiner-b893",
            "organization_key": "san-francisco-examiner-b893",
            "organization_name_as_found": "San Francisco Examiner",
            "role_title": "sketch artist",
            "occupation": "commercial artist",
            "relationship_type": "employment",
            "end_date": "1937",
            "date_precision": "The biography places this work before Smith moved to Manhattan at age nineteen, approximately 1937.",
            "city": "San Francisco",
            "state_or_region": "California",
            "research_notes": "Earlier documented prewar work; not shown to be the immediate pre-OSS affiliation.",
        },
        {
            **base,
            "key": "william-a-smith-freelance-b893",
            "organization_key": "self-employed-illustrator-b893",
            "organization_name_as_found": "freelance illustrator",
            "role_title": "freelance illustrator",
            "occupation": "commercial artist",
            "relationship_type": "self_employment",
            "start_date": "1937",
            "date_precision": "The biography places the start when Smith moved to Manhattan at age nineteen; no end date or direct OSS transition is stated.",
            "city": "New York City",
            "state_or_region": "New York",
            "research_notes": "Documented prewar self-employment; magazine clients are not mislabeled as employers, and immediacy before OSS remains unproven.",
        },
    ]


def william_a_claims() -> list[dict[str, object]]:
    person_id = PEOPLE[27][0]
    common = {
        "person_id": person_id,
        "claim_type": "other_pre_oss_affiliation",
        "identity_match_assessment": "The biography's full name, artist career and OSS-China account align with the indexed row and the official Army commercial-artist match; Maryland institutional evidence corroborates the full name and profession.",
        "temporal_assessment": "Documented as prewar, but the source does not establish that this was the immediate pre-OSS affiliation or last civilian employer.",
        "source_quality": "D_correlative_or_secondary",
        "claim_confidence": "medium",
        "publication_status": "publish_qualified",
        "match_notes": "Presented as qualified earlier employment; no employer sequence is inferred beyond the source chronology.",
    }
    return [
        {
            **common,
            "key": "employment-william-a-smith-scripps-howard-b893",
            "affiliation_key": "william-a-smith-scripps-howard-b893",
            "claim_text": "A biographical source reports that William Arthur Smith worked as a sketch artist for Scripps-Howard Newspapers at the 1932 Los Angeles Olympics.",
            "evidence_excerpt": "Scripps-Howard Newspapers to cover the 1932 Los Angeles Olympics",
            "evidence_paraphrase": "The essay dates this named newspaper-chain employment to the 1932 Olympics.",
            "sources": [
                {"source_key": WAS_BIO, "locator_override": "Biographical paragraph on Smith's work beginning at age fourteen", "excerpt_override": "Scripps-Howard Newspapers to cover the 1932 Los Angeles Olympics"},
                {"source_key": MDTA, "support_type": "context_only", "excerpt_override": "William Arthur Smith (1918-1989), a renowned portraitist and illustrator"},
            ],
        },
        {
            **common,
            "key": "employment-william-a-smith-examiner-b893",
            "affiliation_key": "william-a-smith-examiner-b893",
            "claim_text": "The same biography reports that William Arthur Smith later worked for the San Francisco Examiner sketching murder trials.",
            "evidence_excerpt": "worked for the San Francisco Examiner sketching murder trials",
            "evidence_paraphrase": "The essay names the newspaper and describes Smith's sketch-artist work before his move to Manhattan.",
            "sources": [
                {"source_key": WAS_BIO, "locator_override": "Biographical paragraph preceding Smith's move to Manhattan", "excerpt_override": "worked for the San Francisco Examiner sketching murder trials"},
                {"source_key": MDTA, "support_type": "context_only", "excerpt_override": "William Arthur Smith (1918-1989), a renowned portraitist and illustrator"},
            ],
        },
        {
            **common,
            "key": "self-employment-william-a-smith-b893",
            "affiliation_key": "william-a-smith-freelance-b893",
            "claim_text": "The biography describes William Arthur Smith as a successful freelance illustrator in Manhattan before his wartime OSS service.",
            "evidence_excerpt": "found success as a freelance illustrator",
            "evidence_paraphrase": "The chronology places freelance illustration after his move to Manhattan and before the essay's account of OSS recruitment.",
            "sources": [
                {"source_key": WAS_BIO, "locator_override": "Biographical paragraphs on Manhattan illustration and later OSS recruitment", "excerpt_override": "found success as a freelance illustrator"},
                {"source_key": MDTA, "support_type": "context_only", "excerpt_override": "William Arthur Smith (1918-1989), a renowned portraitist and illustrator"},
            ],
        },
    ]


def richard_smyser_affiliation() -> dict[str, object]:
    return {
        "key": "richard-d-smyser-penn-state-b893",
        "person_id": PEOPLE[46][0],
        "organization_key": "penn-state-b893",
        "organization_name_as_found": "Pennsylvania State University",
        "role_title": "student",
        "occupation": "student",
        "relationship_type": "student",
        "end_date": "1944",
        "date_precision": "Army entry recorded student status on 1942-12-15; the University of Alaska Anchorage biography identifies 1944 graduation from Pennsylvania State University.",
        "state_or_region": "Pennsylvania",
        "country": "United States",
        "immediate_pre_oss": False,
        "last_civilian_pre_service": False,
        "pre_oss_temporal_basis": "strongly_date_bounded",
        "identity_confidence": "high_confidence",
        "claim_confidence": "high",
        "source_quality": "B_authoritative_institutional",
        "publication_status": "published",
        "research_notes": "Student status is not employment and does not establish the immediate pre-OSS affiliation.",
    }


def richard_smyser_claim() -> dict[str, object]:
    return {
        "key": "student-richard-d-smyser-penn-state-b893",
        "person_id": PEOPLE[46][0],
        "affiliation_key": "richard-d-smyser-penn-state-b893",
        "claim_type": "other_pre_oss_affiliation",
        "claim_text": "Richard D Smyser was recorded as a student at Army entry in December 1942, and an institutional biography identifies Pennsylvania State University and a 1944 graduation.",
        "evidence_excerpt": "a 1944 graduate of Pennsylvania State University",
        "evidence_paraphrase": "The official Army student category and UAA's rare-name biography independently support the dated institutional affiliation.",
        "identity_match_assessment": "High confidence from exact rare-name agreement, a nonshared protected identifier and an institutional biography using his documented nickname.",
        "temporal_assessment": "Strongly date-bounded to 1942-1944, but not shown to be employment or the immediate pre-OSS predecessor.",
        "source_quality": "B_authoritative_institutional",
        "claim_confidence": "high",
        "publication_status": "published",
        "match_notes": "Pennsylvania State University is classified as an educational institution, not an employer.",
        "sources": [
            {"source_key": ARMY, "locator_override": "Accepted reviewed identity record; student code 992 at Army entry 1942-12-15; protected identifier withheld"},
            {"source_key": CODES, "locator_override": "PDF physical page 304; corrected civilian occupation category 9-92", "excerpt_override": "Students"},
            {"source_key": UAA, "excerpt_override": "a 1944 graduate of Pennsylvania State University"},
        ],
    }


def edward_affiliation() -> dict[str, object]:
    return {
        "key": "edward-c-smith-ross-raf-b893",
        "person_id": PEOPLE[37][0],
        "organization_key": "royal-air-force-b893",
        "organization_name_as_found": "Royal Air Force",
        "role_title": "Flight Lieutenant",
        "relationship_type": "military_assignment",
        "start_date": "1936-04-01",
        "end_date": "1936-04-01",
        "date_precision": "Official promotion effective 1 April 1936; service before and after that date is corroborated but not fully bounded here.",
        "country": "United Kingdom",
        "immediate_pre_oss": False,
        "last_civilian_pre_service": False,
        "pre_oss_temporal_basis": "documented_prewar",
        "identity_confidence": "high_confidence",
        "claim_confidence": "high",
        "source_quality": "A_direct_official",
        "publication_status": "published",
        "research_notes": "The dated RAF affiliation is documented prewar service; the transfer sequence into OSS remains unestablished.",
    }


def edward_claims() -> list[dict[str, object]]:
    person_id = PEOPLE[37][0]
    common_sources = [
        {"source_key": INDEX, "locator_override": "PDF page 436 row 37; indexed as Edward C Smith-Ross, Wing C"},
        {"source_key": GAZETTE_1936, "locator_override": "Page 2899; promotion effective 1 April 1936"},
        {"source_key": GAZETTE_1946, "support_type": "context_only", "locator_override": "Supplement page 1903; full name and Wing Commander rank"},
    ]
    return [
        {
            "key": "identity-edward-c-smith-ross-b893",
            "person_id": person_id,
            "claim_type": "identity",
            "claim_text": "The indexed Edward C Smith-Ross is a high-confidence match to Royal Air Force officer Edward Charles Smith-Ross.",
            "evidence_paraphrase": "Two official Gazette notices preserve the rare hyphenated name, expand the middle name and document RAF officer ranks consistent with the index.",
            "identity_match_assessment": "High confidence from the rare exact surname, first name, middle initial and compatible Wing Commander rank.",
            "temporal_assessment": "The 1936 notice is prewar; the 1946 notice corroborates identity and rank continuity only.",
            "source_quality": "A_direct_official",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "The full middle name is retained as a documented variant; no civilian employer is inferred.",
            "sources": common_sources,
        },
        {
            "key": "military-edward-c-smith-ross-raf-b893",
            "person_id": person_id,
            "affiliation_key": "edward-c-smith-ross-raf-b893",
            "claim_type": "other_pre_oss_affiliation",
            "claim_text": "Edward Charles Smith-Ross was a Royal Air Force officer promoted to Flight Lieutenant effective 1 April 1936.",
            "evidence_excerpt": "promoted to the rank of Flight Lieutenant",
            "evidence_paraphrase": "The official Air Ministry notice names Smith-Ross and provides the effective promotion date.",
            "identity_match_assessment": "The rare name and compatible indexed Wing Commander abbreviation make the affiliation a high-confidence match.",
            "temporal_assessment": "Documented prewar military service; the immediate pre-OSS transfer sequence is not established.",
            "source_quality": "A_direct_official",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "Royal Air Force service is classified as a military assignment, not a civilian employer.",
            "sources": [
                {"source_key": GAZETTE_1936, "locator_override": "Page 2899; promotion effective 1 April 1936", "excerpt_override": "promoted to the rank of Flight Lieutenant"},
                {"source_key": GAZETTE_1946, "support_type": "context_only", "locator_override": "Supplement page 1903; full name and Wing Commander rank"},
            ],
        },
    ]


def contextual_identity_claims() -> list[dict[str, object]]:
    jane_id, _ = PEOPLE[35]
    andre_id, _ = PEOPLE[38]
    return [
        {
            "key": "identity-jane-smith-hutton-b893",
            "person_id": jane_id,
            "claim_type": "identity",
            "claim_text": "A Georgetown University OSS Oral History Project finding aid independently corroborates the rare indexed name Jane Smith-Hutton.",
            "evidence_excerpt": "biographical information on Jane Smith-Hutton",
            "evidence_paraphrase": "The institutional finding aid names Jane Smith-Hutton in an OSS oral-history research folder.",
            "identity_match_assessment": "High confidence from the rare exact hyphenated name and independent OSS-specific archival context.",
            "temporal_assessment": "Identity and OSS research context only; the finding aid does not establish an assignment or pre-OSS affiliation.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "No role, employer or personnel detail beyond the finding-aid description is inferred.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 436 row 35"},
                {"source_key": GEORGETOWN, "locator_override": "GTM-220705, Box 1, Folder 13", "excerpt_override": "biographical information on Jane Smith-Hutton"},
            ],
        },
        {
            "key": "identity-andre-v-smolianinoff-b893",
            "person_id": andre_id,
            "claim_type": "identity",
            "claim_text": "An OSS historical narrative preserved by the Hoover Institution corroborates Andre Smolianinoff as a U.S. Navy lieutenant working in OSS Special Operations.",
            "evidence_excerpt": "Lt. Andre Smolianinoff, USN, was in charge of this desk",
            "evidence_paraphrase": "The narrative places Lieutenant Smolianinoff at the recruiting desk for Special Operations personnel for Yugoslavia, Albania and Greece.",
            "identity_match_assessment": "High confidence from the rare surname and first name in an OSS-specific institutional document.",
            "temporal_assessment": "This documents wartime OSS status, not a pre-OSS military assignment or civilian employer.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "The wartime Navy rank informs personnel classification only; it is not presented as the immediate pre-OSS affiliation.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 436 row 38"},
                {"source_key": HOOVER, "locator_override": "PDF page 47; Special Operations recruiting desk", "excerpt_override": "Lt. Andre Smolianinoff, USN, was in charge of this desk"},
            ],
        },
    ]


def person_updates() -> list[dict[str, object]]:
    updates: list[dict[str, object]] = []
    for row in (25, 26, 27, 39, 41, 45, 46):
        person_id, name = PEOPLE[row]
        status = "requires_archival_review" if row == 25 else "occupation_only_found"
        if row == 27:
            status = "documented_prewar_employer_found"
        update: dict[str, object] = {
            "person_id": person_id,
            "identity_status": "high_confidence",
            "identity_evidence": "Exact-name agreement plus a nonshared protected identifier connect the visually verified index row to the reviewed official Army record.",
            "personnel_category": "enlisted_army_personnel",
            "commissioned_officer": False,
            "allied_or_foreign_personnel": False,
            "manual_review_required": True,
            "research_status": status,
            "next_action": "Review the indexed Box 726 personnel file to identify the immediate pre-OSS affiliation and last civilian employer; do not convert the Army occupation category into a named employer.",
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
            "archival_review_priority": "high",
        }
        if row == 25:
            update["identity_evidence"] = "Exact-name agreement plus a nonshared protected identifier connect the index row to a 1946 Army record. The post-OSS date supports identity only, and unassigned code 345 is not interpreted."
            update["next_action"] = "Review the indexed Box 726 personnel file for wartime status and pre-OSS affiliation; the accepted 1946 Army record supplies no usable pre-OSS occupation."
        if row == 27:
            update["identity_evidence"] = "The official Army bridge, rare commercial-artist category, OSS artist biography and Maryland institutional biography jointly support William Arthur Smith as a high-confidence identity."
            update["name_variants"] = ["William Arthur Smith"]
            update["next_action"] = "Review Box 726 to determine whether Manhattan freelance illustration was the immediate pre-OSS affiliation or whether an intervening assignment existed."
        if row == 41:
            update["possible_duplicate_group"] = "p436-carl-a-smollar-b893"
            update["identity_evidence"] = "The second Carl A Smollar row has an exact-name Army match through its nonshared protected identifier. The first same-name row remains separate and unresolved."
        if row == 46:
            update["name_variants"] = ["Dick Smyser"]
            update["identity_evidence"] = "The official Army bridge and an institutional rare-name biography jointly identify Richard D. 'Dick' Smyser and his Pennsylvania State University student affiliation."
            update["next_action"] = "Review Box 726 to establish the sequence between Pennsylvania State University, Army entry and OSS service and to identify any civilian employer."
        updates.append(update)

    jane_id, _ = PEOPLE[35]
    updates.append({
        "person_id": jane_id,
        "identity_status": "high_confidence",
        "identity_evidence": "The rare exact hyphenated name appears independently in a Georgetown University OSS Oral History Project finding aid.",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": "Review Box 726 and Georgetown GTM-220705, Box 1, Folder 13, for identity details and a documented pre-OSS affiliation.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    })
    edward_id, _ = PEOPLE[37]
    updates.append({
        "person_id": edward_id,
        "identity_status": "high_confidence",
        "identity_evidence": "Official Gazette notices expand the rare indexed name to Edward Charles Smith-Ross and document RAF officer ranks compatible with Wing Commander.",
        "name_variants": ["Edward Charles Smith-Ross"],
        "personnel_category": "foreign_or_allied_military_personnel",
        "commissioned_officer": True,
        "allied_or_foreign_personnel": True,
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": "Review Box 726 to establish the RAF-to-OSS sequence and determine whether a later immediate pre-OSS assignment intervened.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    })
    andre_id, _ = PEOPLE[38]
    updates.append({
        "person_id": andre_id,
        "identity_status": "high_confidence",
        "identity_evidence": "An OSS narrative preserved by the Hoover Institution identifies the rare-name Andre Smolianinoff as a U.S. Navy lieutenant in Special Operations.",
        "personnel_category": "commissioned_naval_officer",
        "commissioned_officer": True,
        "allied_or_foreign_personnel": False,
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": "Review Box 726 to establish Smolianinoff's pre-OSS Navy or civilian chronology; the wartime OSS narrative does not answer that question.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    })

    for row, rejection in UNRESOLVED.items():
        person_id, name = PEOPLE[row]
        update = {
            "person_id": person_id,
            "identity_status": "unresolved",
            "identity_evidence": f"The visually verified index row supplies {name}, Box 726 and archive location, but staged official-domain, exact-name, employment, occupation, obituary, institutional, directory and archival searches found no defensible identity bridge. {rejection}",
            "manual_review_required": True,
            "research_status": "requires_archival_review",
            "next_action": "Review the indexed Box 726 personnel file for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
            "archival_review_priority": "critical",
        }
        if row == 40:
            update["possible_duplicate_group"] = "p436-carl-a-smollar-b893"
        updates.append(update)
    return updates


def research_attempts() -> list[dict[str, object]]:
    attempts = []
    high_rows = {25, 26, 27, 35, 37, 38, 39, 41, 45, 46}
    for row, (person_id, name) in PEOPLE.items():
        is_high = row in high_rows
        notes = UNRESOLVED.get(row, "Reviewed evidence established an identity bridge and, where supported, a carefully bounded affiliation or occupation claim.")
        attempts.append({
            "key": f"page436-row{row}-{name.lower().replace(' ', '-').replace("'", '')}-b893",
            "person_id": person_id,
            "source_adapter": "manual_staged_protocol",
            "query_text": f"{name}; NARA/index context; CIA Reading Room attempt; exact-name OSS variants; employer and occupation; obituary, institutional, newspaper, directory and archival searches; Box 726; protected-identifier Army crosswalk where available",
            "query_variant_type": "staged_identity_employment_archival_protocol_batch_893",
            "started_at": "2026-10-18T13:00:00Z",
            "completed_at": "2026-10-18T15:40:00Z",
            "outcome": "source_reviewed" if is_high else "candidate_rejected",
            "sources_reviewed": 8 if is_high else 5,
            "candidate_sources_rejected": 5 if is_high else 7,
            "rejection_reasons": "Unbridged namesakes and chronologically incompatible candidates were not assigned." if is_high else notes,
            "research_notes": ("Reviewed evidence established a high-confidence identity; public affiliation claims are limited to what the cited sources support. " if is_high else "No reliable identity or pre-OSS employer was established after staged search and namesake rejection. ") + notes + " The CIA adapter stopped at robots restrictions and the current Library of Congress request timed out; both are access limitations, not negative findings. No exposed NARA API credential was used.",
            "next_action": "Review Box 726.",
            "last_error_redacted": "CIA robots restriction; Library of Congress request timeout",
            "attempt_number": 2 if row == 39 else 1,
            "research_agent_version": "before-oss-b893-v1",
        })
    return attempts


def main() -> None:
    affiliations = [army_occupation_affiliation(item) for item in ARMY_MATCHES]
    affiliations.extend(william_a_affiliations())
    affiliations.extend([richard_smyser_affiliation(), edward_affiliation()])

    claims = [army_identity_claim(row, postwar=(row == 25)) for row in (25, 26, 27, 39, 41, 45, 46)]
    claims.extend(army_occupation_claim(item) for item in ARMY_MATCHES)
    claims.extend(william_a_claims())
    claims.extend([richard_smyser_claim(), *edward_claims(), *contextual_identity_claims()])

    bundle = {
        "bundle_version": "batch-893-v1",
        "reviewer": "Before OSS Batch 893 evidence review",
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
