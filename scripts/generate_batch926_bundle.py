#!/usr/bin/env python3
"""Generate the reviewed Batch 926 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import uuid
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / (
    "research/evidence-page453-harry-strozer-to-jack-r-stubbs-"
    "review_batch-926_2026-10-27.json"
)

INDEX = "nara-index-b926"
ARMY = "army-bulk-b926"
TECH = "army-tech-b926"
CODES = "army-codes-b926"
GOULD = "gould-walter-struewe-b926"
CHOJN = "chojniczanin-zbigniew-strzelinski-b926"
DVIDS = "dvids-richard-stuart-b926"
SF_DIR = "sf-directory-harry-strozer-b926"
FRANCE_DISCOVERY = "geneafrance-francois-strub-b926"

PEOPLE = {
    24: ("4071581a-cf4d-5465-b9ab-b048a4834ede", "Harry Strozer", "754"),
    25: ("2f89d8a4-08ae-5572-9bc6-95c714f7037a", "Francois Strub", "754"),
    26: ("df309945-6593-580e-8f3f-9242add28fde", "Byron T Strubbs", "754"),
    27: ("5b7b3a9e-8a78-50d8-82c7-d677b1b8df42", "James M Strueber", "755"),
    28: ("6e123cf0-88ad-5b80-ac87-ac64de77b32c", "Benjamin Strunk", "754"),
    29: ("e305ccad-b2e5-5551-ba96-491d5ca24185", "Benjamin F Strunk", "754"),
    30: ("411691a6-cd6a-5734-be55-2be3fd0d4167", "Norman W Strunk", "754"),
    31: ("776ee0ec-ca66-5acc-a913-8ed07ab3bf81", "Joseph L Strup", "754"),
    32: ("b0ace79b-87fe-5a71-9521-5d08a66166e3", "Walter Struwe", "754"),
    33: ("7a9b6b86-a4e2-5b08-b7ed-e5db13b82978", "Melvin Struz", "756"),
    34: ("a4d4ab5b-b85c-558d-acc2-21cbade2c2f9", "Zbigniew Strzelinski", "754"),
    35: ("674ad910-1f5d-5e79-9b9a-ea7395c80bd0", "Arthur W Stuart", "754"),
    36: ("f2c0fcde-197d-5083-b523-54ae075d8ba8", "Arthur W Stuart", "754"),
    37: ("f87ee060-f3bd-561e-a5ba-c8fd61c6ad2a", "Charles E Stuart", "754"),
    38: ("25e677b9-c89f-59d8-9c21-4ba95cfed7fa", "Chester J Stuart", "754"),
    39: ("915da674-6281-5950-a3c3-29674e8a86ae", "Ernest A Stuart", "754"),
    40: ("55d5598b-ec0e-5d2a-b11e-2d509c338a7c", "James Stuart", "754"),
    41: ("15857283-ee80-5e7d-a09c-0bef619e304f", "Jean F Stuart", "754"),
    42: ("4b99de9f-5faf-5673-9031-62f48d4a995f", "Kimberly Stuart", "754"),
    43: ("13a10b6e-1455-576d-9c9f-7140afcc35f9", "Richard Stuart", "754"),
    44: ("933f1373-855a-53df-9249-4e2e66351513", "Richard Stuart", "754"),
    45: ("81653b6f-53e2-5fcf-8a2a-046707041c34", "Roger M Stuart", "754"),
    46: ("80266adb-1261-5f48-be76-99878dcdacb7", "Jack R Stubbs", "754"),
}

# Batch 915 already preserved James M. Strueber as a cross-page conflict.
PRESERVED_ROWS = {27}

ARMY_IDENTITIES = {
    26: {"entry": "1943-03-12", "grade": "PVT", "variant": "Byron T Stubbs"},
    29: {"entry": "1942-10-30", "grade": "PVT"},
    31: {"entry": "1942-10-17", "grade": "PVT"},
    33: {"entry": "1943-07-19", "grade": "PVT", "variant": "Melvin Sturz"},
    35: {"entry": "1943-08-16", "grade": "PVT"},
    46: {"entry": "1944-11-03", "grade": "PVT"},
}

ARMY_OCCUPATIONS = {
    26: {
        "code": "983",
        "occupation": "Mechanics and repairmen, n.e.c.",
        "relationship": "employment",
        "locator": "PDF physical page 175; historical category 9-83",
    },
    29: {
        "code": "688",
        "occupation": "Stamping occupations in mechanical treatment of metals",
        "relationship": "employment",
        "locator": "PDF physical page 304; amended historical category 6-88",
    },
    31: {
        "code": "056",
        "occupation": "Photographers",
        "relationship": "employment",
        "locator": "PDF physical page 171; historical category 0-56",
    },
    33: {
        "code": "992",
        "occupation": "Students",
        "relationship": "student",
        "locator": "PDF physical page 304; amended historical category 9-92",
    },
    35: {
        "code": "097",
        "occupation": "Managers and officials, n.e.c.",
        "relationship": "employment",
        "locator": "PDF physical page 171; historical category 0-97",
    },
    46: {
        "code": "992",
        "occupation": "Students",
        "relationship": "student",
        "locator": "PDF physical page 304; amended historical category 9-92",
    },
}

UNRESOLVED = {
    28: "The adjacent Benjamin F. Strunk row has a protected-identifier Army match, but no evidence establishes that the two printed rows represent one person.",
    30: "Exact-name and middle-initial searches found no corroborating identifier or defensible pre-OSS affiliation.",
    36: "The adjacent Arthur W. Stuart row has a distinct protected identifier; the two printed rows remain separate pending Box 754 review.",
    37: "Common-name searches produced no two-identifier bridge to the Box 754 person.",
    38: "Exact-name and middle-initial searches found no person-specific source tied to OSS or Box 754.",
    39: "Common-name and middle-initial searches produced no defensible OSS identity bridge or pre-OSS affiliation.",
    40: "A missionary-priest namesake associated with OSS work in Burma lacks a second identifier and was not assigned to this unranked row.",
    41: "Exact-name and middle-initial searches found no corroborating identifier or reliable pre-OSS affiliation.",
    42: "The incomplete, potentially anachronistic-looking name remains exactly as printed; searches found no reliable identity bridge.",
    45: "Exact-name and middle-initial searches found no corroborating identifier or reliable employment evidence.",
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
            "archival_identifier": "RG 226, Entry A1-224, Boxes 754-756",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 453, rows 24-46; checked against layout-preserving text and the rendered page image",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. Full identifiers remain private. James M Strueber's earlier conflicting outcome is preserved unchanged.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; six accepted Batch 926 protected-identifier candidates",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "No raw record or full protected identifier is retained in public assets. Coded occupations identify neither employer nor workplace.",
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
            "locator": "PDF physical pages 171, 174-175 and 304; Batch 926 categories visually checked",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical categories identify neither employer, institution nor workplace. Amended labels on physical page 304 are retained.",
        },
        {
            "key": GOULD,
            "stable_url": "https://api.pageplace.de/preview/DT0400.9780429879197_A36424273/preview-9780429879197_A36424273.pdf",
            "archival_identifier": "ISBN 978-0-429-87919-7",
            "title": "German Anti-Nazi Espionage in the Second World War: The OSS and the Men of the TOOL Missions",
            "author_creator": "Jonathan S. Gould",
            "repository_publisher": "Routledge",
            "publication_record_date": "2019",
            "locator": "Preview PDF physical pages 18-19, printed pages xvii-xviii; visual and text review",
            "access_date": "2026-10-26",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "rights_notes": "The preview identifies Walter Strüwe among the exiled German trade unionists selected for the OSS TOOL missions in late August 1944.",
        },
        {
            "key": CHOJN,
            "stable_url": "https://chojniczanin.pl/pdf/Chojniczanin03-2023.pdf",
            "title": "Chojnicki Orzeł",
            "author_creator": "Andrzej Lorbiecki; republishing research by Ewelina Tyborska with permission",
            "repository_publisher": "Chojniczanin.pl",
            "publication_record_date": "2023-03",
            "locator": "Issue 03/2023 (127), PDF physical page 19, printed page 19",
            "access_date": "2026-10-26",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "rights_notes": "The article draws on John S. Micgiel's Project Eagle archival research, identifies Zbigniew Strzeliński as Zbigniew Paprzycki, and reproduces his OSS personnel-file card.",
        },
        {
            "key": DVIDS,
            "stable_url": "https://www.dvidshub.net/news/370910/104-year-old-michigan-world-war-ii-veteran-honored-with-birthday-parade",
            "title": "104 year-old Michigan World War II veteran honored with birthday parade",
            "author_creator": "Sgt. James R. Bennett",
            "repository_publisher": "Defense Visual Information Distribution Service; Michigan National Guard",
            "publication_record_date": "2020-05-28",
            "locator": "Story 370910, paragraphs 1-3",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "rights_notes": "The official story identifies Richard Kingsley Stuart and his prewar school-principal role. Two identical Richard Stuart index rows prevent assignment without another identifier.",
        },
        {
            "key": SF_DIR,
            "stable_url": "https://library.sfgenealogy.org/directory/san-francisco-county-directory/1930/1930_1367.pdf",
            "title": "Polk's Crocker-Langley San Francisco City Directory, 1930",
            "author_creator": "R. L. Polk & Co.",
            "repository_publisher": "San Francisco Genealogy; original directory published by R. L. Polk & Co.",
            "publication_record_date": "1930",
            "locator": "Directory page 1367; Harry Strozer entry",
            "access_date": "2026-10-26",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "rights_notes": "The rare exact-name directory lead lists a telegraph operator at Dutro & Co.; the unranked index row supplies no second identifier or OSS bridge.",
        },
        {
            "key": FRANCE_DISCOVERY,
            "stable_url": "https://www.geneafrance.com/france/mplf/?mplf=441529",
            "title": "STRUB François: Titres, homologations et services pour faits de résistance",
            "repository_publisher": "GénéaFrance, citing Mémoire des hommes",
            "publication_record_date": "record accessed 2026",
            "locator": "Discovery record for François Strub, born 18 January 1908 at Maidières",
            "access_date": "2026-10-26",
            "source_quality": "E_discovery_only",
            "rights_notes": "Discovery-only pointer to a French official resistance record. It supplies no OSS, Box 754 or employment bridge and is not published as the indexed identity.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": "polish-armed-forces-west-b926",
            "organization_id": "8043a812-1527-5eab-af0c-08670108993d",
            "canonical_name": "Polish Armed Forces in the West",
            "historical_name": "Polish Army",
            "aliases": ["Polish Armed Forces", "Polskie Siły Zbrojne"],
            "organization_type": "allied armed forces",
            "sector": "military",
            "country": "Poland",
            "normalization_notes": "Existing canonical organization reused. The reviewed source supports the broad Polish Armed Forces relationship, not a specific unit.",
        },
        {
            "key": "german-army-wehrmacht-b926",
            "organization_id": "a577f889-8052-5c7d-aefc-6345820d8ac1",
            "canonical_name": "German Army (Wehrmacht)",
            "historical_name": "Heer der Wehrmacht",
            "aliases": ["Wehrmacht"],
            "organization_type": "army",
            "sector": "military",
            "country": "Germany",
            "active_dates": "1935-1945",
            "normalization_notes": "Existing historical organization reused. This records a wartime conscripted assignment, not political affiliation or voluntary support.",
        },
    ]


def affiliations() -> list[dict[str, object]]:
    result: list[dict[str, object]] = []
    for row, data in ARMY_OCCUPATIONS.items():
        result.append(
            {
                "key": f"{slug(PEOPLE[row][1])}-occupation-b926",
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
                "key": "walter-struewe-exiled-trade-unionist-b926",
                "person_id": PEOPLE[32][0],
                "role_title": "exiled German trade unionist selected for a TOOL mission",
                "occupation": "trade unionist",
                "relationship_type": "professional_affiliation",
                "start_date": "1944-08",
                "end_date": "1944-08",
                "date_precision": "Introduced to OSS recruiter Joseph Gould in late August 1944 and selected from the proposed group for a TOOL mission.",
                "city": "London",
                "country": "United Kingdom",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "explicit_immediate",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "published",
                "research_notes": "This is a documented professional and political-exile pathway, not a named employer. A separate inaccessible biographical lead was not used to publish a bricklayer occupation.",
            },
            {
                "key": "zbigniew-strzelinski-polish-armed-forces-b926",
                "person_id": PEOPLE[34][0],
                "organization_key": "polish-armed-forces-west-b926",
                "organization_name_as_found": "Polish Armed Forces",
                "role_title": "corporal; Project Eagle trainee",
                "relationship_type": "military_assignment",
                "start_date": "1943-11",
                "end_date": "1944-09",
                "date_precision": "After surrender at Cassino on 1943-11-09, he entered Polish military custody; the Polish ministry delegated Project Eagle soldiers to the OSS section in mid-1944, with parachute training in September.",
                "country": "United Kingdom",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "probable_immediate",
                "identity_confidence": "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "publish_qualified",
                "research_notes": "The source supports the broad Polish Armed Forces pathway but not a specific regiment or exact transfer date.",
            },
            {
                "key": "zbigniew-strzelinski-wehrmacht-b926",
                "person_id": PEOPLE[34][0],
                "organization_key": "german-army-wehrmacht-b926",
                "organization_name_as_found": "Wehrmacht",
                "role_title": "conscripted soldier",
                "relationship_type": "military_assignment",
                "start_date": "1942",
                "end_date": "1943-11-09",
                "date_precision": "The article places Project Eagle members' German conscription in 1942-1943 and specifically dates Strzeliński's surrender at Cassino to 1943-11-09.",
                "country": "Germany",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "publish_qualified",
                "research_notes": "Recorded as a conscripted enemy-army assignment in the pathway to Allied service; not treated as employment or ideological affiliation.",
            },
        ]
    )
    return result


def claims() -> list[dict[str, object]]:
    result: list[dict[str, object]] = []
    for row, data in ARMY_OCCUPATIONS.items():
        result.append(
            {
                "key": f"occupation-{slug(PEOPLE[row][1])}-b926",
                "person_id": PEOPLE[row][0],
                "affiliation_key": f"{slug(PEOPLE[row][1])}-occupation-b926",
                "claim_type": "occupation",
                "claim_text": f"At Army entry on {ARMY_IDENTITIES[row]['entry']}, the official record coded the civilian category as {data['occupation']}; no employer or institution is named.",
                "evidence_paraphrase": f"The protected identifier links the index row to the Army record, whose category {data['code']} is decoded in the official NARA code list.",
                "identity_match_assessment": "High confidence from a nonshared protected identifier and exact or compatible full name; the identifier is not published.",
                "temporal_assessment": "Strongly date-bounded to Army entry, but not shown to be the immediate pre-OSS affiliation.",
                "source_quality": "A_direct_official",
                "claim_confidence": "medium",
                "publication_status": "publish_qualified",
                "match_notes": "The code is published only as a historical category and is excluded from named-employer analytics.",
                "sources": [
                    {"source_key": INDEX, "locator_override": f"PDF page 453 row {row}; Box {PEOPLE[row][2]}; protected value withheld"},
                    {"source_key": ARMY, "locator_override": f"Accepted protected-identifier record; Army entry {ARMY_IDENTITIES[row]['entry']}; grade {ARMY_IDENTITIES[row]['grade']}; category {data['code']}"},
                    {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46; field definitions"},
                    {"source_key": CODES, "locator_override": data["locator"]},
                ],
            }
        )
    result.extend(
        [
            {
                "key": "identity-walter-struewe-b926",
                "person_id": PEOPLE[32][0],
                "claim_type": "identity",
                "claim_text": "Walter Struwe in the OSS index is a high-confidence match to Walter Strüwe, the German exile selected for the OSS PICKAXE mission.",
                "evidence_excerpt": "Walter Strüwe and Emil Konhäuser",
                "evidence_paraphrase": "Gould names Walter Strüwe among seven exiled German trade unionists selected for TOOL missions and identifies him as a PICKAXE mission participant.",
                "identity_match_assessment": "High confidence from the rare name, diacritic variant, exact OSS context and named mission; Box 754 remains unreviewed.",
                "temporal_assessment": "The selection occurred in late August 1944 before OSS mission training.",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "The index spelling without an umlaut is preserved; the documented Strüwe variant is added separately.",
                "sources": [
                    {"source_key": INDEX, "locator_override": "PDF page 453 row 32; Box 754"},
                    {"source_key": GOULD, "locator_override": "Preview PDF physical page 19, printed page xviii; selection for TOOL missions"},
                ],
            },
            {
                "key": "immediate-walter-struewe-b926",
                "person_id": PEOPLE[32][0],
                "affiliation_key": "walter-struewe-exiled-trade-unionist-b926",
                "claim_type": "immediate_pre_oss_affiliation",
                "claim_text": "Immediately before OSS selection in late August 1944, Walter Strüwe was part of the exiled German trade-unionist group presented to Joseph Gould in London.",
                "evidence_excerpt": "group of exiled German trade unionists",
                "evidence_paraphrase": "The scholarly account describes the group presented for recruitment and then names Strüwe among those selected for TOOL missions.",
                "identity_match_assessment": "High-confidence rare-name match in explicit OSS recruitment context.",
                "temporal_assessment": "Explicitly immediate: presentation to the recruiter and selection occur in the same late-August 1944 sequence.",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "This is a professional/political-exile affiliation, not a named employer; no employer is inferred.",
                "sources": [{"source_key": GOULD, "locator_override": "Preview PDF physical page 19, printed page xviii"}],
            },
            {
                "key": "identity-zbigniew-strzelinski-b926",
                "person_id": PEOPLE[34][0],
                "claim_type": "identity",
                "claim_text": "Zbigniew Strzelinski in the index is a high-confidence match to Project Eagle corporal Zbigniew Strzeliński, whose real name was Zbigniew Paprzycki.",
                "evidence_excerpt": "Zbigniew Strzeliński (real name: Zbigniew Paprzycki)",
                "evidence_paraphrase": "The article identifies the Project Eagle alias and real name, home region, rank, mission and OSS personnel-file card.",
                "identity_match_assessment": "High confidence from the rare exact alias, OSS personnel-file context and named Project Eagle mission.",
                "temporal_assessment": "The source sequences German military service, surrender, Polish military service, OSS training and the 1945 mission.",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "The index spelling remains primary; the diacritic form and real name are documented variants.",
                "sources": [
                    {"source_key": INDEX, "locator_override": "PDF page 453 row 34; Box 754"},
                    {"source_key": CHOJN, "locator_override": "PDF physical page 19, printed page 19; identity and Hot Punch paragraphs"},
                ],
            },
            {
                "key": "immediate-zbigniew-strzelinski-polish-forces-b926",
                "person_id": PEOPLE[34][0],
                "affiliation_key": "zbigniew-strzelinski-polish-armed-forces-b926",
                "claim_type": "immediate_pre_oss_affiliation",
                "claim_text": "The best-supported immediate pre-OSS pathway is a Polish Armed Forces assignment before delegation to the Polish OSS section for Project Eagle.",
                "evidence_excerpt": "soldiers of the Polish Armed Forces",
                "evidence_paraphrase": "The article says the Polish ministry delegated German-speaking Polish soldiers to the OSS section and identifies Strzeliński among Project Eagle participants.",
                "identity_match_assessment": "High-confidence alias match; exact unit remains unverified.",
                "temporal_assessment": "Probable immediate: Polish service is the documented intervening assignment before OSS training, but no exact transfer date is given.",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "claim_confidence": "medium",
                "publication_status": "publish_qualified",
                "match_notes": "The broad Polish Armed Forces relationship is published with qualification; no specific regiment is inferred.",
                "sources": [{"source_key": CHOJN, "locator_override": "PDF physical page 19, printed page 19; Polish delegation and training chronology"}],
            },
            {
                "key": "preoss-zbigniew-strzelinski-wehrmacht-b926",
                "person_id": PEOPLE[34][0],
                "affiliation_key": "zbigniew-strzelinski-wehrmacht-b926",
                "claim_type": "other_pre_oss_affiliation",
                "claim_text": "Before entering Polish service, Zbigniew Strzeliński had been conscripted into the Wehrmacht and surrendered to the Allies at Cassino on November 9, 1943.",
                "evidence_excerpt": "surrendered to the Allies on 09.11.1943",
                "evidence_paraphrase": "The article dates his surrender and explains the conscripted German-service pathway shared by Project Eagle participants.",
                "identity_match_assessment": "High-confidence alias match in a person-specific biographical passage.",
                "temporal_assessment": "Documented pre-OSS military assignment ending before Polish service and OSS training.",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "claim_confidence": "medium",
                "publication_status": "publish_qualified",
                "match_notes": "Recorded as conscription, not employment or voluntary political alignment.",
                "sources": [{"source_key": CHOJN, "locator_override": "PDF physical page 19, printed page 19; conscription and surrender chronology"}],
            },
            {
                "key": "identity-harry-strozer-candidate-b926",
                "person_id": PEOPLE[24][0],
                "claim_type": "identity",
                "claim_text": "A 1930 San Francisco directory entry for telegraph operator Harry Strozer is an unassigned namesake candidate for the index row.",
                "evidence_excerpt": "Strozer Harry (Lillian) teleg opr Dutro & Co",
                "evidence_paraphrase": "The contemporary directory provides a rare exact-name occupation and employer lead.",
                "identity_match_assessment": "Low: exact rare name only; the index supplies no rank, identifier, residence or other bridge.",
                "temporal_assessment": "The 1930 role predates OSS, but no sequence to OSS is established.",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "claim_confidence": "low",
                "publication_status": "withheld_low_confidence",
                "match_notes": "Private candidate only; Dutro & Co. is not published as the indexed person's employer.",
                "sources": [{"source_key": SF_DIR, "locator_override": "Directory page 1367; Harry Strozer entry"}],
            },
            {
                "key": "identity-francois-strub-candidate-b926",
                "person_id": PEOPLE[25][0],
                "claim_type": "identity",
                "claim_text": "A French resistance record for François Strub is an unassigned discovery lead for the index row.",
                "evidence_paraphrase": "The discovery record points to an official resistance file for a François Strub born in 1908 at Maidières.",
                "identity_match_assessment": "Low: name and wartime resistance context only; no OSS, Box 754, birth or employment bridge is present in the index.",
                "temporal_assessment": "Wartime resistance service is plausible context, but its relationship to OSS is unverified.",
                "source_quality": "E_discovery_only",
                "claim_confidence": "low",
                "publication_status": "withheld_low_confidence",
                "match_notes": "Private discovery lead only; no biographical fact is transferred to the public profile.",
                "sources": [{"source_key": FRANCE_DISCOVERY, "locator_override": "Discovery record citing Mémoire des hommes"}],
            },
        ]
    )
    for row in (43, 44):
        result.append(
            {
                "key": f"identity-richard-k-stuart-candidate-row{row}-b926",
                "person_id": PEOPLE[row][0],
                "claim_type": "identity",
                "claim_text": "Richard Kingsley Stuart, an OSS lieutenant and prewar school principal, is an unassigned candidate for this Richard Stuart index row.",
                "evidence_excerpt": "Stuart had been a school principal prior to the war.",
                "evidence_paraphrase": "The official Defense Department story identifies Richard Kingsley Stuart, his prewar role, OSS service and Pacific assignments.",
                "identity_match_assessment": "Low for this row: two identical Richard Stuart index rows exist, and neither can be selected from the public evidence.",
                "temporal_assessment": "The school-principal role is explicitly prewar for the candidate, but cannot be assigned to either index row.",
                "source_quality": "A_direct_official",
                "claim_confidence": "low",
                "publication_status": "withheld_low_confidence",
                "match_notes": "Private candidate attached to both rows; no employer, school or occupation is published until Box 754 distinguishes them.",
                "sources": [
                    {"source_key": INDEX, "locator_override": f"PDF page 453 row {row}; Box 754"},
                    {"source_key": DVIDS, "locator_override": "Story 370910, paragraphs 1-3"},
                ],
            }
        )
    return result


def archival_update(row: int, reason: str) -> dict[str, object]:
    person_id, name, box = PEOPLE[row]
    return {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, Box {box} and archive location, but staged official, CIA, OSS, employment, occupation, obituary, institutional, newspaper, directory and archival searches found no defensible identity bridge. {reason}",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": f"Review Box {box} for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "critical",
    }


def person_updates() -> list[dict[str, object]]:
    updates = [archival_update(row, reason) for row, reason in UNRESOLVED.items()]
    benjamin_group = duplicate_group("benjamin-strunk-page453-b926")
    arthur_group = duplicate_group("arthur-w-stuart-page453-b926")
    richard_group = duplicate_group("richard-stuart-page453-b926")
    for update in updates:
        if update["person_id"] == PEOPLE[28][0]:
            update["identity_status"] = "ambiguous"
            update["possible_duplicate_group"] = benjamin_group
        if update["person_id"] == PEOPLE[36][0]:
            update["identity_status"] = "ambiguous"
            update["possible_duplicate_group"] = arthur_group

    updates.extend(
        [
            {
                **archival_update(24, "A rare exact-name 1930 directory candidate has no second identifier or OSS bridge."),
                "identity_status": "ambiguous",
                "identity_evidence": "The visually verified index row supplies only Harry Strozer and Box 754. A rare exact-name 1930 San Francisco directory candidate was found, but no source bridges that telegraph operator to OSS.",
            },
            {
                **archival_update(25, "A French resistance namesake remains a discovery-only lead without an OSS bridge."),
                "identity_status": "ambiguous",
                "identity_evidence": "The visually verified index row supplies only Francois Strub and Box 754. A French resistance namesake remains a discovery lead; no birth date, OSS link or other identifier selects him.",
            },
        ]
    )

    for row, data in ARMY_IDENTITIES.items():
        name = PEOPLE[row][1]
        occupation = ARMY_OCCUPATIONS[row]["occupation"]
        if row == 26:
            evidence = "A nonshared protected identifier links the indexed Byron T Strubbs row to an official Army record spelling the name Byron T Stubbs. The surname discrepancy remains visible."
        elif row == 33:
            evidence = "A nonshared protected identifier links the indexed Melvin Struz row to an official Army record spelling the name Melvin Sturz. The letter transposition remains visible."
        else:
            evidence = "An exact full name and nonshared protected identifier connect the index row to the official Army record."
        update: dict[str, object] = {
            "person_id": PEOPLE[row][0],
            "identity_status": "high_confidence",
            "identity_evidence": evidence,
            "personnel_category": "enlisted_army_personnel",
            "commissioned_officer": False,
            "allied_or_foreign_personnel": False,
            "manual_review_required": True,
            "research_status": "occupation_only_found",
            "next_action": f"Review Box {PEOPLE[row][2]} for the immediate pre-OSS affiliation and named employer or institution; do not convert the historical category '{occupation}' into one.",
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
            "archival_review_priority": "high",
        }
        if data.get("variant"):
            update["name_variants"] = [str(data["variant"])]
        if row == 29:
            update["possible_duplicate_group"] = benjamin_group
        if row == 35:
            update["possible_duplicate_group"] = arthur_group
        updates.append(update)

    updates.extend(
        [
            {
                "person_id": PEOPLE[32][0],
                "identity_status": "high_confidence",
                "identity_evidence": "The rare indexed name, documented Strüwe variant, explicit OSS selection and named PICKAXE mission establish a high-confidence identity match.",
                "name_variants": ["Walter Strüwe"],
                "personnel_category": "temporary_contract_or_special_personnel",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": True,
                "manual_review_required": True,
                "research_status": "occupation_only_found",
                "next_action": "Review Box 754 for the named civilian employer, formal status, training dates and exact OSS assignment documents. The immediate trade-unionist recruitment pathway is established.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[34][0],
                "identity_status": "high_confidence",
                "identity_evidence": "The rare exact alias, real-name disclosure, OSS personnel-card reproduction and named Project Eagle Hot Punch mission establish a high-confidence match.",
                "name_variants": ["Zbigniew Strzeliński", "Zbigniew Paprzycki"],
                "personnel_category": "foreign_or_allied_military_personnel",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": True,
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Review Box 754 for the named civilian employer, exact Polish unit and transfer order. The Wehrmacht-to-Polish-Armed-Forces-to-OSS pathway is documented with qualifications.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
        ]
    )
    for row in (43, 44):
        updates.append(
            {
                "person_id": PEOPLE[row][0],
                "identity_status": "ambiguous",
                "identity_evidence": "An official Defense Department story identifies Richard Kingsley Stuart as an OSS lieutenant and prewar school principal, but two identical Richard Stuart index rows exist and the public evidence selects neither.",
                "manual_review_required": True,
                "possible_duplicate_group": richard_group,
                "research_status": "requires_archival_review",
                "next_action": "Review both Box 754 files together for middle name, birth date, rank, service number and Pacific assignment before assigning the Richard Kingsley Stuart candidate or his school-principal role.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            }
        )
    return updates


def research_attempts() -> list[dict[str, object]]:
    attempts: list[dict[str, object]] = []
    for row, (person_id, name, box) in PEOPLE.items():
        if row in PRESERVED_ROWS:
            continue
        if row in ARMY_IDENTITIES:
            outcome = "source_reviewed"
            detail = f"An accepted protected-identifier Army bridge establishes high-confidence identity and the dated historical category {ARMY_OCCUPATIONS[row]['occupation']}, but no named employer or institution."
            reviewed, rejected = 7, 3
        elif row == 32:
            outcome = "source_reviewed"
            detail = "A scholarly OSS study establishes high-confidence identity and the immediate late-August 1944 recruitment pathway from a group of exiled German trade unionists; no named employer was established."
            reviewed, rejected = 9, 3
        elif row == 34:
            outcome = "source_reviewed"
            detail = "A regional historical article based on Project Eagle archival research establishes the alias, real name, German and Polish military pathway, OSS training and mission; no named civilian employer was established."
            reviewed, rejected = 9, 3
        elif row == 24:
            outcome = "candidate_found"
            detail = "A contemporary San Francisco directory provides a rare exact-name telegraph-operator and Dutro & Co. lead, but no second identifier or OSS bridge permits assignment."
            reviewed, rejected = 7, 3
        elif row == 25:
            outcome = "candidate_found"
            detail = "A French resistance namesake was found through a discovery pointer to Mémoire des hommes, but no OSS, Box 754, birth or employment bridge permits assignment."
            reviewed, rejected = 7, 3
        elif row in {43, 44}:
            outcome = "candidate_found"
            detail = "An official Defense Department story identifies Richard Kingsley Stuart and a prewar school-principal role, but two identical index rows prevent assignment to either person."
            reviewed, rejected = 8, 3
        else:
            outcome = "no_result"
            detail = UNRESOLVED[row]
            reviewed, rejected = 6, 3
        attempts.append(
            {
                "key": f"page453-row{row}-{slug(name)}-b926",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA index and public Archives context; CIA Reading Room site-restricted exact-name check; OSS and spelling variants; employer and occupation 1940; obituary, institutional, newspaper, directory and archival searches; Box {box}; protected-identifier Army crosswalk where defensible",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_926",
                "started_at": "2026-10-26T22:00:00Z",
                "completed_at": "2026-10-27T02:26:00Z",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, discovery-only genealogy, wrong initials, postwar-only leads and sources without an OSS or Box-file bridge were not assigned. Grouped CIA Reading Room and Library of Congress exact-name checks returned no person-specific result.",
                "research_notes": f"{detail} The index page and Army code pages were visually checked. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA API call was made.",
                "next_action": f"Review Box {box} for corroborating identifiers and the immediate pre-OSS affiliation or last civilian employer.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b926-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-926-v1",
        "reviewer": "Before OSS Batch 926 evidence review",
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
