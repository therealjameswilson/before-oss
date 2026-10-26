#!/usr/bin/env python3
"""Generate the reviewed Batch 924 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import uuid
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / (
    "research/evidence-page452-william-s-strauss-to-theophanes-g-strimenos-"
    "review_batch-924_2026-10-26.json"
)

INDEX = "nara-index-b924"
ARMY = "army-bulk-b924"
TECH = "army-tech-b924"
CODES = "army-codes-b924"
PRINCETON = "princeton-george-strawbridge-b924"
ST_PAUL = "st-paul-george-strawbridge-b924"
BETEKINTO = "betekinto-stephen-streeter-b924"
DESERET = "deseret-nicholas-strike-b924"
AHEPA = "ahepa-nicholas-strike-b924"
HOOVER = "hoover-theophanes-strimenos-b924"

PEOPLE = {
    24: ("c1d42fce-baf7-5259-978e-1360e936b29b", "William S Strauss"),
    25: ("e00eb3c2-d676-526a-89c2-e6829a91046a", "George Strawbridge"),
    26: ("dbe6304d-6bb1-5483-93b6-eb41572f0668", "Ernest H Streed"),
    27: ("a83e8685-38a2-598b-bc91-42598bd5232d", "Elmer E Streeter"),
    28: ("e46e59df-3e9d-5073-93f5-e72c7616ac24", "Elmer S Streeter"),
    29: ("802cbb13-1a4d-5078-a233-6fefbc226de0", "Norman E Streeter"),
    30: ("3ec9d787-c0ca-5d3b-9bf6-8266543a29d6", "Stephen Streeter"),
    31: ("2abae00d-4604-50eb-a84d-23049d23c7c0", "Thomas W Streeter"),
    32: ("803ea5df-1954-5848-829c-a5af19f134d2", "Robert E Streif"),
    33: ("873441b6-b61b-5cd4-988e-64204693367a", "Walter H Streilein"),
    34: ("515e65a9-5d06-5f79-b585-4a2cd23eb528", "Kathleen Streissguth"),
    35: ("8e39dd9b-d723-5ced-9d44-ab0d7dfd42d9", "Pierre D Streit"),
    36: ("543bc104-fac6-5352-84ca-e0d1a66b38e7", "J E Strick"),
    37: ("ebdb36f9-54a2-5972-b030-0fef7dd7b5c8", "Bessie Strickland"),
    38: ("684a6676-6e1a-527a-89a3-22d9f12957ed", "Irene Strickland"),
    39: ("c7b71ec2-a3bb-5508-acb1-3749dea49018", "Mary W Strickland"),
    40: ("1466bcf3-31c9-5381-9c42-223d086dd20c", "Robert E Strickland"),
    41: ("1cd1e7c4-8c21-5d0a-86e1-788915338430", "William C Strickland"),
    42: ("d8dbe549-c4b2-5dfe-9070-ab83a98b79f8", "William C Strickland"),
    43: ("d36a49ed-dd13-552b-9509-6477fe43872a", "Robert A Stricklin"),
    44: ("9e24f3ef-d1e6-5f00-9661-33583be17f01", "Robert E Strief"),
    45: ("526fc414-2a93-566a-9f5e-1246122f61f5", "Nicholas L Strike"),
    46: ("2b92e253-f5d1-5fb0-93d1-662da49b084d", "Theophanes G Strimenos"),
}

UNRESOLVED = {
    24: "Exact-name and variant searches produced no person-specific result with an OSS or Box 752 identity bridge.",
    28: "The protected identifier produced no Army bulk match; the adjacent Elmer E. Streeter has a different middle initial and protected identifier and remains separate.",
    34: "Exact-name, institutional, obituary, newspaper and archival searches produced no defensible identity or employment evidence.",
    36: "Initials-only searches were too ambiguous to support a person match, employer or institution.",
    37: "Common-name searches produced no corroborating identifier or Box 753 bridge.",
    38: "Common-name and occupation searches produced no defensible identity bridge.",
    39: "Common-name and middle-initial searches produced no person-specific result tied to OSS or Box 753.",
    40: "Common-name searches produced no second corroborating identifier or defensible pre-OSS affiliation.",
    42: "This row has a different protected identifier from the adjacent William C. Strickland row and remains separate; no defensible external match was found.",
}

ARMY_OCCUPATIONS = {
    27: {
        "code": "794",
        "occupation": "Machinists' apprentices",
        "entry_date": "1943-06-03",
        "temporal_basis": "strongly_date_bounded",
        "locator": "PDF physical pages 175 and 304; historical category 7-94",
    },
    29: {
        "code": "736",
        "occupation": "Chauffeurs and drivers, bus, taxi, truck, and tractor",
        "entry_date": "1945-03-20",
        "temporal_basis": "temporal_relation_uncertain",
        "locator": "PDF physical page 174; historical category 7-36",
    },
    35: {
        "code": "992",
        "occupation": "Students",
        "entry_date": "1943-06-03",
        "temporal_basis": "strongly_date_bounded",
        "locator": "PDF physical page 304; historical category 9-92",
    },
    41: {
        "code": "138",
        "occupation": "Stock clerks",
        "entry_date": "1941-04-09",
        "temporal_basis": "strongly_date_bounded",
        "locator": "PDF physical pages 171 and 304; historical category 1-38",
    },
    43: {
        "code": "068",
        "occupation": "Semiprofessional occupations, not elsewhere classified",
        "entry_date": "1943-08-12",
        "temporal_basis": "strongly_date_bounded",
        "locator": "PDF physical pages 171 and 304; historical category 0-68",
    },
}

DUPLICATE_GROUPS = {
    "elmer-streeter-b924": (27, 28),
    "robert-streif-strief-b924": (32, 44),
    "william-c-strickland-b924": (41, 42),
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
            "archival_identifier": "RG 226, Entry A1-224, Boxes 752-753",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 452, rows 24-46; checked against layout-preserving text and a rendered page image",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. Full identifiers remain private. Two Elmer Streeter rows, two William C. Strickland rows, and the Streif/Strief spellings were visually verified.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; six accepted and two rejected Batch 924 protected-identifier candidates",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "No raw row or full protected identifier is retained in public assets. The Ernest H. Streed and Thomas W. Streeter candidates were rejected. Coded occupations identify no employer.",
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
            "locator": "PDF physical pages 171-175 and 304; Batch 924 categories visually checked",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical occupation categories identify neither an employer nor a workplace. The category wording is retained without modernization.",
        },
        {
            "key": PRINCETON,
            "stable_url": "https://paw.princeton.edu/memorial/george-strawbridge-sr-33",
            "title": "George Strawbridge Sr. '33",
            "author_creator": "Princeton Class of 1933",
            "repository_publisher": "Princeton Alumni Weekly, Princeton University",
            "publication_record_date": "2013-12-04",
            "locator": "Memorial paragraphs 2-4",
            "access_date": "2026-10-26",
            "source_quality": "B_authoritative_institutional",
            "rights_notes": "The memorial says he worked for Campbell Soup before and after World War II, but does not date the prewar job or call it the immediate predecessor to OSS.",
        },
        {
            "key": ST_PAUL,
            "stable_url": "https://www.sps70.org/AlumniHorae/20thAH.pdf",
            "title": "Twentieth Century Alumni Horae, 1906-1930",
            "author_creator": "St. Paul's School Alumni Association",
            "repository_publisher": "St. Paul's School",
            "publication_record_date": "2012",
            "locator": "PDF physical page 62, printed page 103; George Strawbridge entry",
            "access_date": "2026-10-26",
            "source_quality": "B_authoritative_institutional",
            "rights_notes": "The institutional obituary gives exact family, education, February 1941-October 1945 Army and OSS service, and rank at separation. It says Campbell Soup employment after the war only.",
        },
        {
            "key": BETEKINTO,
            "stable_url": "https://www.betekinto.hu/en/2_2016",
            "title": "Angleton's Hungarians: A Case Study of Central European Counterintelligence in Rome 1945-1946",
            "author_creator": "Duncan Bare",
            "repository_publisher": "Betekintő, Historical Archives of the Hungarian State Security",
            "publication_record_date": "2016",
            "locator": "Issue 2/2016 English abstract; article PDF caption and note cite NARA II, RG 226, Entry 224, Box 752",
            "access_date": "2026-10-26",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "rights_notes": "The scholarly article names Stephen Streeter in OSS X-2 Balkans, but its Box 752 citation conflicts with the index's Box 753. The identity is therefore qualified and no pre-OSS affiliation is inferred.",
        },
        {
            "key": DESERET,
            "stable_url": "https://www.deseret.com/1997/1/1/19287025/death-nicholas-louis-strike/",
            "title": "Death: Nicholas Louis Strike",
            "author_creator": "Deseret News",
            "repository_publisher": "Deseret News",
            "publication_record_date": "1997-01-01",
            "locator": "Biographical paragraphs 1-5",
            "access_date": "2026-10-26",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "rights_notes": "The obituary gives the exact full name, education, 1939-1940 Sons of Pericles presidency and wartime Navy service. It does not mention OSS; the identity remains probable.",
        },
        {
            "key": AHEPA,
            "stable_url": "https://ahepahistory.org/AHEPA-Magazines/1962-Ahepa-Magazines-Opt.pdf",
            "title": "The Ahepan, 1962 issues",
            "author_creator": "Order of AHEPA",
            "repository_publisher": "AHEPA History",
            "publication_record_date": "1962",
            "locator": "PDF physical page 40, printed page 20, Strike Follows Dad's Footsteps; physical page 50, Sons report",
            "access_date": "2026-10-26",
            "source_quality": "B_authoritative_institutional",
            "rights_notes": "The organization's magazine identifies Nick Strike as a former Sons of Pericles Supreme President before World War II and confirms the Salt Lake City family context.",
        },
        {
            "key": HOOVER,
            "stable_url": "https://digitalcollections.hoover.org/objects/73291/goodfellow-memo-regarding-supplementary-interim-report-of-os",
            "archival_identifier": "Hoover ID 69085.167; HIA-GOODFELLOW-4-A-9-5-3",
            "title": "Goodfellow memo regarding supplementary interim report of OSS board",
            "author_creator": "Millard Preston Goodfellow",
            "repository_publisher": "Hoover Institution Library & Archives",
            "publication_record_date": "1944-05-13",
            "locator": "Section XV, First Sergeant Theophanes G. Strimenos",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "collection_name": "Millard Preston Goodfellow papers; declassified U.S. government records",
            "document_number": "69085.167",
            "rights_notes": "The declassified official report gives the exact protected identifier, civilian occupation, Army entry and September 1943 OSS assignment. The protected identifier is not public.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": "campbell-soup-b924",
            "canonical_name": "Campbell Soup Company",
            "historical_name": "Campbell Soup",
            "aliases": ["Campbell Soup Company"],
            "organization_type": "food manufacturing company",
            "sector": "business_and_industry",
            "city": "Camden",
            "state_or_region": "New Jersey",
            "country": "United States",
            "normalization_notes": "The institutional memorial's historical employer wording is preserved. No modern corporate restructuring is implied.",
        },
        {
            "key": "alabama-national-guard-b924",
            "canonical_name": "Alabama National Guard",
            "historical_name": "Alabama National Guard",
            "aliases": [],
            "organization_type": "state National Guard",
            "sector": "military",
            "state_or_region": "Alabama",
            "country": "United States",
            "normalization_notes": "The organization is preserved exactly as named in the 1944 OSS interview; no unit is inferred.",
        },
        {
            "key": "sons-of-pericles-b924",
            "organization_id": "a120746f-204d-533e-926f-edd93e9f8ac3",
            "canonical_name": "Sons of Pericles",
            "historical_name": "Sons of Pericles",
            "aliases": ["Order of Sons of Pericles"],
            "organization_type": "youth fraternal organization",
            "sector": "labor_nonprofit_and_religion",
            "country": "United States",
            "normalization_notes": "Existing organization reused. Leadership is a professional or volunteer affiliation, not employment.",
        },
    ]


def affiliations() -> list[dict[str, object]]:
    result: list[dict[str, object]] = [
        {
            "key": "george-strawbridge-campbell-b924",
            "person_id": PEOPLE[25][0],
            "organization_key": "campbell-soup-b924",
            "organization_name_as_found": "Campbell Soup",
            "role_title": "public relations and assistant treasurer",
            "occupation": "public relations and corporate administration",
            "relationship_type": "employment",
            "end_date": "1941-02",
            "date_precision": "Princeton says he worked for Campbell Soup before and after World War II; St. Paul's dates Army service from February 1941. The exact prewar start and end dates are not stated.",
            "city": "Camden",
            "state_or_region": "New Jersey",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": True,
            "pre_oss_temporal_basis": "probable_immediate",
            "identity_confidence": "high_confidence",
            "claim_confidence": "medium",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "publish_qualified",
            "research_notes": "A named prewar employer and probable last civilian employer before Army service. Neither memorial explicitly calls it the immediate OSS predecessor.",
        },
        {
            "key": "nicholas-strike-sons-pericles-b924",
            "person_id": PEOPLE[45][0],
            "organization_key": "sons-of-pericles-b924",
            "organization_name_as_found": "Sons of Pericles",
            "role_title": "national president",
            "relationship_type": "professional_affiliation",
            "start_date": "1939",
            "end_date": "1940",
            "date_precision": "The obituary gives 1939 and 1940; the AHEPA magazine independently describes his national leadership before World War II.",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "probable",
            "claim_confidence": "medium",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "publish_qualified",
            "research_notes": "Documented prewar organizational leadership, not employment. The exact-name wartime Navy officer lacks an independent OSS bridge, so the person match remains probable.",
        },
        {
            "key": "theophanes-strimenos-alabama-guard-b924",
            "person_id": PEOPLE[46][0],
            "organization_key": "alabama-national-guard-b924",
            "organization_name_as_found": "Alabama National Guard",
            "role_title": "soldier; later first sergeant",
            "relationship_type": "military_assignment",
            "start_date": "1940-11",
            "end_date": "1943-09",
            "date_precision": "The OSS report says he entered the Army with the Alabama National Guard in November 1940 and was assigned to OSS in September 1943.",
            "state_or_region": "Alabama",
            "country": "United States",
            "immediate_pre_oss": True,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "explicit_immediate",
            "identity_confidence": "confirmed",
            "claim_confidence": "confirmed",
            "source_quality": "A_direct_official",
            "publication_status": "published",
            "research_notes": "Military assignment, not civilian employment. The official report supplies the entry-to-OSS chronology directly.",
        },
        {
            "key": "theophanes-strimenos-cafe-b924",
            "person_id": PEOPLE[46][0],
            "role_title": "cafe worker",
            "occupation": "cafe worker; historical Army category: waiters and waitresses except private family",
            "relationship_type": "employment",
            "end_date": "1940-11-25",
            "date_precision": "The OSS report says he worked in a Mobile cafe in civilian life; the Army record dates entry to 1940-11-25 and codes the occupation as 227. No cafe name is supplied.",
            "city": "Mobile",
            "state_or_region": "Alabama",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": True,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "confirmed",
            "claim_confidence": "confirmed",
            "source_quality": "A_direct_official",
            "publication_status": "published",
            "research_notes": "The last civilian occupation is explicit, but the employer is unnamed and is not normalized into an invented organization.",
        },
    ]
    for row, data in ARMY_OCCUPATIONS.items():
        result.append(
            {
                "key": f"{slug(PEOPLE[row][1])}-occupation-b924",
                "person_id": PEOPLE[row][0],
                "occupation": data["occupation"],
                "relationship_type": "student" if data["occupation"] == "Students" else "employment",
                "end_date": data["entry_date"],
                "date_precision": f"Historical civilian-occupation code {data['code']} was recorded at Army entry on {data['entry_date']}; no employer, school, workplace or OSS-transfer date is named.",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": data["temporal_basis"],
                "identity_confidence": "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "A_direct_official",
                "publication_status": "publish_qualified",
                "research_notes": "The historical category is not converted into a named employer, school, institution, workplace or exact job title.",
            }
        )
    return result


def claims() -> list[dict[str, object]]:
    result: list[dict[str, object]] = [
        {
            "key": "identity-george-strawbridge-b924",
            "person_id": PEOPLE[25][0],
            "claim_type": "identity",
            "claim_text": "The indexed George Strawbridge is a high-confidence match to Princeton alumnus and Army major George Strawbridge, who served in the Quartermaster Corps and OSS.",
            "evidence_excerpt": "Quartermaster Corps of the U.S. Army and in the Office of Strategic Services",
            "evidence_paraphrase": "Two institutional memorials agree on his education, wartime Army service, major rank and distinctive identity; St. Paul's explicitly names OSS.",
            "identity_match_assessment": "High confidence from the exact uncommon name, consistent Philadelphia and Princeton context, dated Army service and direct institutional OSS statement.",
            "temporal_assessment": "St. Paul's dates service from February 1941 to October 1945; the exact OSS assignment dates are not supplied.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "The protected index value is not published. No sequence between Quartermaster Corps and OSS is invented.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 452 row 25; Box 752; protected value withheld"},
                {"source_key": ST_PAUL, "locator_override": "PDF physical page 62, printed page 103; George Strawbridge entry"},
                {"source_key": PRINCETON, "support_type": "context_only", "locator_override": "Memorial paragraphs 2-4"},
            ],
        },
        {
            "key": "prewar-george-strawbridge-campbell-b924",
            "person_id": PEOPLE[25][0],
            "affiliation_key": "george-strawbridge-campbell-b924",
            "claim_type": "last_civilian_pre_service",
            "claim_text": "George Strawbridge worked for Campbell Soup in public relations and as assistant treasurer before and after World War II; it is his probable last civilian employer before February 1941 Army service, not a proven immediate OSS predecessor.",
            "evidence_excerpt": "Before and after WWII, George spent some years with Campbell Soup",
            "evidence_paraphrase": "Princeton's memorial names the employer and roles; St. Paul's independently dates his Army and OSS service from February 1941.",
            "identity_match_assessment": "High-confidence person match from two institutional memorials and direct OSS context.",
            "temporal_assessment": "Prewar employment is explicit, but its exact end date and any intervening role before OSS are not stated.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "medium",
            "publication_status": "publish_qualified",
            "match_notes": "The employer is published with a probable-immediate temporal label and excluded from default confirmed/high employer analytics.",
            "sources": [
                {"source_key": PRINCETON, "locator_override": "Memorial paragraph 4"},
                {"source_key": ST_PAUL, "support_type": "context_only", "locator_override": "PDF physical page 62; service dated February 1941-October 1945"},
            ],
        },
        {
            "key": "identity-ernest-streed-conflict-b924",
            "person_id": PEOPLE[26][0],
            "claim_type": "identity",
            "claim_text": "The Army candidate for Ernest H Streed was rejected because the official row reads Ernest H Steed and the protected identifier is shared by separate index records.",
            "evidence_paraphrase": "The name spelling and nonunique protected identifier do not support transferring the Army row to this index person.",
            "identity_match_assessment": "Conflicting: the protected value is not unique within the index and the Army surname omits the indexed r.",
            "temporal_assessment": "No Army date or occupation is transferred; Box 752 review is required.",
            "source_quality": "A_direct_official",
            "claim_confidence": "conflicting",
            "publication_status": "conflicting",
            "match_notes": "The rejected candidate remains auditable. A second generated candidate also remains unaccepted; neither supplies a public fact.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 452 row 26; Box 752; protected identifier withheld"},
                {"source_key": ARMY, "support_type": "contradicts", "locator_override": "Rejected reviewed candidate; Army surname Steed; protected identifier withheld"},
            ],
        },
        {
            "key": "identity-stephen-streeter-b924",
            "person_id": PEOPLE[30][0],
            "claim_type": "identity",
            "claim_text": "The indexed Stephen Streeter is a probable match to the OSS X-2 Balkans officer described by Duncan Bare, but the article's Box 752 citation conflicts with the index's Box 753.",
            "evidence_excerpt": "chief of Counterintelligence Balkans ... and his lieutenant, Stephen Streeter",
            "evidence_paraphrase": "A scholarly archival study gives the exact distinctive name, OSS X-2 role and a personnel-file citation one box away from the index row.",
            "identity_match_assessment": "Probable from the distinctive exact name and direct OSS context; the box discrepancy prevents a high-confidence match.",
            "temporal_assessment": "The article documents OSS and postwar intelligence work, not a pre-OSS employer.",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "claim_confidence": "medium",
            "publication_status": "publish_qualified",
            "match_notes": "No employer, nationality or language background is inferred from the article for the index row pending Box 753 review.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 452 row 30; Box 753"},
                {"source_key": BETEKINTO, "locator_override": "Issue 2/2016 English abstract; article note cites Box 752"},
            ],
        },
        {
            "key": "identity-thomas-streeter-conflict-b924",
            "person_id": PEOPLE[31][0],
            "claim_type": "identity",
            "claim_text": "The Army candidate for Thomas W Streeter was rejected because the protected identifier selects an official Army row named James E OConnell.",
            "evidence_paraphrase": "The official Army name conflicts completely with the indexed name, so none of its fields belongs to this person.",
            "identity_match_assessment": "Conflicting protected-identifier result; no name agreement.",
            "temporal_assessment": "No Army date, grade or occupation is transferred; Box 753 review is required.",
            "source_quality": "A_direct_official",
            "claim_confidence": "conflicting",
            "publication_status": "conflicting",
            "match_notes": "The conflict is displayed rather than resolved by convenience.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 452 row 31; Box 753; protected identifier withheld"},
                {"source_key": ARMY, "support_type": "contradicts", "locator_override": "Rejected reviewed candidate; Army row names James E OConnell; protected identifier withheld"},
            ],
        },
        {
            "key": "identity-nicholas-strike-b924",
            "person_id": PEOPLE[45][0],
            "claim_type": "identity",
            "claim_text": "The indexed Nicholas L Strike is a probable match to Nicholas Louis Strike, the prewar Sons of Pericles president and wartime Navy officer.",
            "evidence_excerpt": "In 1939 and 1940 ... National President of the Sons of Pericles",
            "evidence_paraphrase": "The exact distinctive full name, prewar national role and World War II Navy service align, but neither reviewed source mentions OSS.",
            "identity_match_assessment": "Probable, not high confidence, because the rare exact name and wartime military chronology agree but an independent OSS or Box 753 bridge is missing.",
            "temporal_assessment": "The 1939-1940 affiliation is explicitly prewar; the obituary does not date OSS service.",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "claim_confidence": "medium",
            "publication_status": "publish_qualified",
            "match_notes": "Postwar Ajax employment is excluded. The profile remains marked for archival review.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 452 row 45; Box 753"},
                {"source_key": DESERET, "locator_override": "Biographical paragraphs 1-5"},
                {"source_key": AHEPA, "support_type": "context_only", "locator_override": "PDF physical pages 40 and 50; former Supreme President before World War II"},
            ],
        },
        {
            "key": "prewar-nicholas-strike-sons-b924",
            "person_id": PEOPLE[45][0],
            "affiliation_key": "nicholas-strike-sons-pericles-b924",
            "claim_type": "other_pre_oss_affiliation",
            "claim_text": "Nicholas Louis Strike served as national president of the Sons of Pericles in 1939 and 1940; this is a qualified professional or volunteer affiliation, not employment.",
            "evidence_excerpt": "traveled the country as National President of the Sons of Pericles",
            "evidence_paraphrase": "A contemporary organizational retrospective corroborates the obituary's prewar national leadership account.",
            "identity_match_assessment": "The person match remains probable because no reviewed source independently connects this Navy officer to OSS.",
            "temporal_assessment": "Explicitly dated 1939-1940 and therefore documented prewar; immediacy to OSS is not established.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "medium",
            "publication_status": "publish_qualified",
            "match_notes": "The organization is not described as an employer and is excluded from employer analytics.",
            "sources": [
                {"source_key": DESERET, "locator_override": "Biographical paragraph 2"},
                {"source_key": AHEPA, "locator_override": "PDF physical page 50; prewar Supreme Presidency retrospective"},
            ],
        },
        {
            "key": "identity-theophanes-strimenos-b924",
            "person_id": PEOPLE[46][0],
            "claim_type": "identity",
            "claim_text": "The indexed Theophanes G Strimenos is confirmed as the first sergeant interviewed in the May 1944 OSS board report.",
            "evidence_excerpt": "First Sergeant Theophanes G. Strimenos",
            "evidence_paraphrase": "The declassified official report and index agree on the exact name and protected identifier and give a direct OSS service chronology.",
            "identity_match_assessment": "Confirmed by exact name, protected identifier and direct OSS record. The identifier remains private.",
            "temporal_assessment": "The report says he entered the Army in November 1940 and was assigned to OSS in September 1943.",
            "source_quality": "A_direct_official",
            "claim_confidence": "confirmed",
            "publication_status": "published",
            "match_notes": "The direct official record supports the identity without reliance on a namesake biography.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 452 row 46; Box 753; protected identifier withheld"},
                {"source_key": HOOVER, "locator_override": "Section XV; protected identifier withheld"},
            ],
        },
        {
            "key": "immediate-theophanes-strimenos-guard-b924",
            "person_id": PEOPLE[46][0],
            "affiliation_key": "theophanes-strimenos-alabama-guard-b924",
            "claim_type": "immediate_pre_oss_affiliation",
            "claim_text": "Theophanes G. Strimenos entered the Army with the Alabama National Guard in November 1940 and was assigned to OSS in September 1943.",
            "evidence_excerpt": "Entered the Army with the Alabama National Guard in November 1940",
            "evidence_paraphrase": "The official OSS interview gives the predecessor military affiliation and the month of his OSS assignment in one chronology.",
            "identity_match_assessment": "Confirmed exact-person official record.",
            "temporal_assessment": "Explicit immediate military pathway to the September 1943 OSS assignment.",
            "source_quality": "A_direct_official",
            "claim_confidence": "confirmed",
            "publication_status": "published",
            "match_notes": "Military assignment, not civilian employment.",
            "sources": [{"source_key": HOOVER, "locator_override": "Section XV, First Sergeant Theophanes G. Strimenos"}],
        },
        {
            "key": "civilian-theophanes-strimenos-cafe-b924",
            "person_id": PEOPLE[46][0],
            "affiliation_key": "theophanes-strimenos-cafe-b924",
            "claim_type": "last_civilian_pre_service",
            "claim_text": "Before Army service, Theophanes G. Strimenos worked in an unnamed cafe in Mobile, Alabama; the employer's name is not given.",
            "evidence_excerpt": "in civilian life, worked in a cafe in Mobile, Alabama",
            "evidence_paraphrase": "The official OSS report states the civilian occupation and city; the accepted Army row dates entry and supplies a compatible waiter category.",
            "identity_match_assessment": "Confirmed exact-person official records linked by a protected identifier.",
            "temporal_assessment": "Explicitly civilian life before November 1940 Army entry; definitely last civilian work before service, but not immediately before OSS.",
            "source_quality": "A_direct_official",
            "claim_confidence": "confirmed",
            "publication_status": "published",
            "match_notes": "No cafe, proprietor or corporate employer is invented.",
            "sources": [
                {"source_key": HOOVER, "locator_override": "Section XV; civilian-life sentence"},
                {"source_key": ARMY, "support_type": "context_only", "locator_override": "Accepted reviewed identity record; Army entry 1940-11-25 and occupation code 227; protected identifier withheld"},
                {"source_key": CODES, "support_type": "context_only", "locator_override": "PDF physical page 172; historical category 2-27"},
            ],
        },
    ]

    for row, data in ARMY_OCCUPATIONS.items():
        name = PEOPLE[row][1]
        result.append(
            {
                "key": f"identity-{slug(name)}-b924",
                "person_id": PEOPLE[row][0],
                "claim_type": "identity",
                "claim_text": f"The indexed {name} row is a high-confidence match to the reviewed official Army record.",
                "evidence_paraphrase": "An exact compatible name and nonshared protected identifier connect the visually verified index row to the official Army record.",
                "identity_match_assessment": "High confidence from exact or compatible full-name agreement and a nonshared protected-identifier bridge.",
                "temporal_assessment": f"The Army entry is dated {data['entry_date']}; it does not establish an OSS transfer date.",
                "source_quality": "A_direct_official",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "No protected identifier is exposed, and the historical occupation is kept separate from employer claims.",
                "sources": [
                    {"source_key": INDEX, "locator_override": f"PDF page 452 row {row}; Box {'752' if row < 30 else '753'}; protected identifier withheld"},
                    {"source_key": ARMY, "locator_override": "Accepted reviewed identity bridge; protected identifier withheld"},
                ],
            }
        )
        article = "an" if data["occupation"].lower().startswith(tuple("aeiou")) else "a"
        if data["occupation"] == "Students":
            claim_text = f"At Army entry on {data['entry_date']}, {name} was recorded in the historical occupation group Students; no school or employer is identified."
        else:
            claim_text = f"At Army entry on {data['entry_date']}, {name} was recorded in {article} historical occupation category, {data['occupation']}; no employer is identified."
        if row == 29:
            claim_text += " Because this entry date is in 1945, its relation to OSS service is uncertain."
        result.append(
            {
                "key": f"occupation-{slug(name)}-b924",
                "person_id": PEOPLE[row][0],
                "affiliation_key": f"{slug(name)}-occupation-b924",
                "claim_type": "occupation",
                "claim_text": claim_text,
                "evidence_excerpt": data["occupation"],
                "evidence_paraphrase": f"The accepted Army record carries civilian-occupation code {data['code']}, decoded from NARA's official code list.",
                "identity_match_assessment": "The category belongs only to the reviewed protected-identifier match; the identifier itself is not public.",
                "temporal_assessment": "Dated to Army entry; it does not establish the immediate pre-OSS affiliation or a named employer." if row != 29 else "Dated to March 1945; chronology relative to OSS is unresolved.",
                "source_quality": "A_direct_official",
                "claim_confidence": "medium",
                "publication_status": "publish_qualified",
                "match_notes": "The historical category is a qualified lead, not a named employer, school, institution, workplace or exact title.",
                "sources": [
                    {"source_key": ARMY, "locator_override": f"Accepted reviewed identity record; civilian occupation code {data['code']}; protected identifier withheld"},
                    {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46; Army-entry-date and civilian-occupation fields"},
                    {"source_key": CODES, "locator_override": data["locator"], "excerpt_override": data["occupation"]},
                ],
            }
        )
    return result


def base_archival_update(row: int, identity_evidence: str) -> dict[str, object]:
    return {
        "person_id": PEOPLE[row][0],
        "identity_status": "unresolved",
        "identity_evidence": identity_evidence,
        "personnel_category": "unknown_or_indeterminate",
        "commissioned_officer": None,
        "allied_or_foreign_personnel": None,
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": "Review the indexed personnel file for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "critical",
    }


def person_updates() -> list[dict[str, object]]:
    updates = [
        base_archival_update(
            row,
            f"The visually verified index row supplies {PEOPLE[row][1]}, Box {'752' if row < 30 else '753'} and archive location, but staged NARA/index, CIA Reading Room, exact-name OSS, occupation, employer, obituary, institutional, newspaper and archival searches found no defensible identity bridge. {reason}",
        )
        for row, reason in UNRESOLVED.items()
    ]

    group_by_row = {
        row: duplicate_group(key)
        for key, rows in DUPLICATE_GROUPS.items()
        for row in rows
    }
    for update in updates:
        row = next(row for row, person in PEOPLE.items() if person[0] == update["person_id"])
        if row in group_by_row:
            update["possible_duplicate_group"] = group_by_row[row]

    updates.extend(
        [
            {
                "person_id": PEOPLE[25][0],
                "identity_status": "high_confidence",
                "identity_evidence": "St. Paul's and Princeton institutional memorials identify the uncommon exact-name Army major, Quartermaster Corps and OSS veteran and his Campbell Soup work before and after World War II.",
                "name_variants": ["George Strawbridge Sr."],
                "personnel_category": "commissioned_army_officer",
                "commissioned_officer": True,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "documented_prewar_employer_found",
                "next_action": "Review Box 752 for exact Campbell Soup dates and the sequence between civilian work, Quartermaster Corps and OSS. The employer is probable last civilian pre-service, not proven immediate to OSS.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[26][0],
                "identity_status": "conflicting",
                "identity_evidence": "The official Army candidate spells the surname Steed and the protected identifier is shared by separate index records. The candidate and all attached fields were rejected.",
                "personnel_category": "unknown_or_indeterminate",
                "commissioned_officer": None,
                "allied_or_foreign_personnel": None,
                "manual_review_required": True,
                "research_status": "conflicting_sources",
                "next_action": "Review Box 752 to establish the correct identifier and pre-OSS affiliation. Do not transfer any field from the rejected Ernest H Steed Army row.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[30][0],
                "identity_status": "probable",
                "identity_evidence": "A scholarly archival study identifies an exact-name Stephen Streeter in OSS X-2 Balkans but cites Box 752, while the index row is Box 753.",
                "personnel_category": "unknown_or_indeterminate",
                "commissioned_officer": None,
                "allied_or_foreign_personnel": None,
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Review Box 753 and the article's cited Box 752 personnel file to resolve the box discrepancy and identify any pre-OSS employer.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[31][0],
                "identity_status": "conflicting",
                "identity_evidence": "The protected identifier selects an official Army row named James E OConnell, not Thomas W Streeter. The candidate and every attached field were rejected.",
                "personnel_category": "unknown_or_indeterminate",
                "commissioned_officer": None,
                "allied_or_foreign_personnel": None,
                "manual_review_required": True,
                "research_status": "conflicting_sources",
                "next_action": "Review Box 753 to establish the correct identifier and pre-OSS affiliation. Do not transfer any field from the rejected Army row.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[32][0],
                "identity_status": "ambiguous",
                "identity_evidence": "The adjacent Robert E Streif and Robert E Strief rows may represent a spelling variant or different people. A Dallas lawyer named Robert Edwin Strief lacks an OSS or Box 753 bridge and was not assigned.",
                "possible_duplicate_group": group_by_row[32],
                "personnel_category": "unknown_or_indeterminate",
                "commissioned_officer": None,
                "allied_or_foreign_personnel": None,
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Review both adjacent Box 753 files to determine whether Streif and Strief are spelling variants or different people; do not assign the Dallas lawyer without a direct bridge.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[33][0],
                "identity_status": "ambiguous",
                "identity_evidence": "Public records contain at least two Walter H Streilein namesakes with different military and death histories; neither has a defensible OSS or Box 753 bridge.",
                "personnel_category": "unknown_or_indeterminate",
                "commissioned_officer": None,
                "allied_or_foreign_personnel": None,
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Review Box 753 for rank, service branch, birth year or other disambiguators before assigning either Walter H Streilein namesake.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[44][0],
                "identity_status": "ambiguous",
                "identity_evidence": "The adjacent Robert E Strief and Robert E Streif rows may represent a spelling variant or different people. A Dallas lawyer named Robert Edwin Strief lacks an OSS or Box 753 bridge and was not assigned.",
                "possible_duplicate_group": group_by_row[44],
                "personnel_category": "unknown_or_indeterminate",
                "commissioned_officer": None,
                "allied_or_foreign_personnel": None,
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Review both adjacent Box 753 files to determine whether Streif and Strief are spelling variants or different people; do not assign the Dallas lawyer without a direct bridge.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[45][0],
                "identity_status": "probable",
                "identity_evidence": "The uncommon exact name Nicholas Louis Strike, documented 1939-1940 national leadership and wartime Navy service align, but no reviewed source independently mentions OSS or Box 753.",
                "name_variants": ["Nicholas Louis Strike", "Nick Strike"],
                "personnel_category": "unknown_or_indeterminate",
                "commissioned_officer": None,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Review Box 753 to confirm the Navy officer identity, OSS assignment and any civilian employment before service. The Sons of Pericles role is not employment.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[46][0],
                "identity_status": "confirmed",
                "identity_evidence": "The index, accepted Army row and declassified May 1944 OSS board report agree on the exact name and protected identifier and give a direct November 1940 Army to September 1943 OSS chronology.",
                "personnel_category": "enlisted_army_personnel",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": False,
                "manual_review_required": False,
                "research_status": "occupation_only_found",
                "next_action": "The immediate Alabama National Guard pathway and last civilian cafe work are established. Review Box 753 only to identify the cafe, if recorded, and refine unit chronology.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "not_required",
            },
        ]
    )

    for row, data in ARMY_OCCUPATIONS.items():
        variants = ["William C Strickland Jr."] if row == 41 else None
        update = {
            "person_id": PEOPLE[row][0],
            "identity_status": "high_confidence",
            "identity_evidence": "An exact or compatible full name and nonshared protected identifier connect the index row to the official Army record.",
            "personnel_category": "enlisted_army_personnel",
            "commissioned_officer": False,
            "allied_or_foreign_personnel": False,
            "manual_review_required": True,
            "research_status": "occupation_only_found",
            "next_action": f"Review Box {'752' if row < 30 else '753'} to identify the immediate pre-OSS affiliation and last civilian employer; do not convert the Army category '{data['occupation']}' into a named employer or institution.",
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
            "archival_review_priority": "high",
        }
        if variants:
            update["name_variants"] = variants
        if row in group_by_row:
            update["possible_duplicate_group"] = group_by_row[row]
        updates.append(update)
    return updates


def research_attempts() -> list[dict[str, object]]:
    attempts: list[dict[str, object]] = []
    reviewed_rows = {25, 30, 45, 46}
    conflict_rows = {26, 31}
    ambiguous_rows = {32, 33, 44}
    for row, (person_id, name) in PEOPLE.items():
        if row == 25:
            outcome = "source_reviewed"
            detail = "Two institutional memorials established high-confidence identity and qualified prewar Campbell Soup employment, but not an explicit immediate OSS predecessor."
            sources_reviewed, rejected = 8, 3
        elif row == 30:
            outcome = "source_reviewed"
            detail = "A scholarly archival study established a probable OSS X-2 identity; its Box 752 citation conflicts with the index's Box 753, so no employer was assigned."
            sources_reviewed, rejected = 7, 4
        elif row == 45:
            outcome = "source_reviewed"
            detail = "An obituary and AHEPA magazine established probable identity and a 1939-1940 Sons of Pericles role, but no independent OSS bridge or prewar employer."
            sources_reviewed, rejected = 8, 4
        elif row == 46:
            outcome = "source_reviewed"
            detail = "A direct declassified OSS report and accepted Army bridge confirmed identity, the Alabama National Guard-to-OSS path and unnamed Mobile cafe work before Army service."
            sources_reviewed, rejected = 8, 2
        elif row in conflict_rows:
            outcome = "candidate_rejected"
            detail = "The protected-identifier Army candidate conflicted with the indexed name or was nonunique; every attached field was rejected."
            sources_reviewed, rejected = 6, 5
        elif row in ARMY_OCCUPATIONS:
            outcome = "source_reviewed"
            detail = f"An accepted protected-identifier Army bridge established identity and a dated historical category, {ARMY_OCCUPATIONS[row]['occupation']}, but no named employer or institution."
            sources_reviewed, rejected = 6, 3
        elif row in ambiguous_rows:
            outcome = "candidate_rejected"
            detail = "Plausible namesakes or spelling variants lacked a second identifier or Box 753 bridge and were not assigned."
            sources_reviewed, rejected = 6, 5
        else:
            outcome = "no_result"
            detail = UNRESOLVED[row]
            sources_reviewed, rejected = 5, 3
        attempts.append(
            {
                "key": f"page452-row{row}-{slug(name)}-b924",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA/index and public Archives context; CIA Reading Room site-restricted exact-name check; OSS and rank variants; employer and occupation; obituary, institutional, newspaper, directory and archival searches; Boxes 752-753; protected-identifier Army crosswalk where defensible",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_924",
                "started_at": "2026-10-26T10:28:00Z",
                "completed_at": "2026-10-26T10:41:00Z",
                "outcome": outcome,
                "sources_reviewed": sources_reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, discovery-only genealogy or people-finder results, wrong identifiers, wrong initials, postwar-only leads and sources without an OSS or Box-file bridge were not assigned." if outcome == "source_reviewed" else detail,
                "research_notes": f"{detail} The CIA and Library of Congress adapters failed closed before returning results; institutional, obituary, newspaper, directory and archival web searches supplied the alternative protocol step. No search snippet was used as final evidence, no access control was bypassed, and no authenticated NARA API call was made.",
                "next_action": "Review the indexed personnel file for corroborating identifiers and the immediate pre-OSS affiliation or last civilian employer.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b924-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-924-v1",
        "reviewer": "Before OSS Batch 924 evidence review",
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
