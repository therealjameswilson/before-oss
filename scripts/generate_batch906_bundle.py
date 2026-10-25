#!/usr/bin/env python3
"""Generate the reviewed Batch 906 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "research/evidence-page443-st-thomas-to-stamnock-review_batch-906_2026-10-25.json"

INDEX = "nara-index-b906"
ARMY = "army-bulk-b906"
TECH = "army-tech-b906"
CODES = "army-codes-b906"
NARA_STAIGER = "nara-duck-staiger-b906"
SMITHSONIAN_STAIGER = "smithsonian-staiger-b906"
AP_STAIGER = "ap-staiger-oregon-b906"
NCPEDIA_STALLINGS = "ncpedia-stallings-b906"
BROADCASTING_STADLER = "broadcasting-stadler-b906"
WARTIME_STAHL = "wartime-stahl-b906"


PEOPLE = {
    1: ("c75c56b5-e909-5af5-b768-b60db5609e5e", "Jean St. Thomas"),
    2: ("8661ce76-3af7-5bf1-992e-1d4a89a7ac37", "Jacov Staal"),
    3: ("c6a4198d-cfeb-5558-9e8a-1850dd75f225", "J R Staats"),
    4: ("051d8378-29bf-583c-9b60-41c923cc41a0", "Ryneer A Staats"),
    5: ("fac95fd7-1393-51ed-8df0-cea97facbd3b", "Clifford D Stack"),
    6: ("56c59499-289a-5b81-8083-36f6499be217", "James F Stacy"),
    7: ("c589c231-cb5a-518e-9cdd-114484bc119c", "John A Stacy"),
    8: ("ac36f6a3-16e0-5fb1-9e6a-6e1b6f8c20db", "Howard A Stadermann"),
    9: ("aae82823-6bc7-5f01-9c3d-0535d99e052f", "Frederick J Stadler"),
    10: ("4338c90d-460f-56b0-9367-ad0ceb83c52f", "Glen M Stadler"),
    11: ("97695d0a-6fdd-5dda-8a75-ccb0d7252e77", "Jimmie Stafford"),
    12: ("edd7eae3-d9cd-5725-8945-a80b4e28b090", "Walter E Stafford"),
    13: ("2ca0c4ef-6c8c-5640-b2b3-1758b090ea95", "Ella M Stagg"),
    14: ("e64fd301-0183-5535-bf7b-3c9e885902e9", "Donald C Stahl"),
    15: ("41c6eca3-ac25-595c-ab12-fcdcc6b7c8e6", "Martin Stahl"),
    16: ("d4e11632-c367-5d3b-ab4d-e583cf8fa7ce", "Ferdinando Stahly"),
    17: ("2b671e64-23bb-5753-8582-b91a7729c6e5", "Eugene L Staiger"),
    18: ("727a6826-b4c7-5d0f-ad18-5a48b6696605", "Stanley A Staiger"),
    19: ("2cc57327-5011-58e7-8122-145adacf288d", "Richard D Stainbrook"),
    20: ("1448fa2a-a922-56e4-a160-6a3bc1478b29", "Laurence T Stallings"),
    21: ("f852edf0-d68f-56b8-9f54-5910ec700d23", "Peter Stamates"),
    22: ("9b7207d9-0de2-5210-9397-ca4acfcf8c32", "Max Stamler"),
    23: ("15f9a410-37d7-57b8-83e6-98ce98e51fb3", "Leonard V Stamnock"),
}


ARMY_OCCUPATIONS = [
    {"row": 1, "date": "1943-02-13", "code": "056", "occupation": "Photographers", "locator": "PDF physical pages 170-173; category 0-56"},
    {"row": 6, "date": "1943-07-03", "code": "105", "occupation": "Clerks, general office", "locator": "PDF physical pages 170-173; category 1-05"},
    {"row": 12, "date": "1943-03-16", "code": "736", "occupation": "Semiskilled chauffeurs and drivers, bus, taxi, truck, and tractor", "locator": "PDF physical pages 170-173; category 7-36"},
    {"row": 14, "date": "1943-04-20", "code": "736", "occupation": "Semiskilled chauffeurs and drivers, bus, taxi, truck, and tractor", "locator": "PDF physical pages 170-173; category 7-36"},
    {"row": 17, "date": "1942-03-07", "code": "494", "occupation": "Skilled occupations in fabrication of metal products, not elsewhere classified", "locator": "PDF physical pages 170-173; category 4-94"},
    {"row": 19, "date": "1942-09-10", "code": "992", "occupation": "Students", "locator": "PDF physical page 304; amended category 9-92"},
    {"row": 21, "date": "1943-04-09", "code": "484", "occupation": "Skilled structural and ornamental-metal workers", "locator": "PDF physical pages 170-173; category 4-84"},
]


UNRESOLVED = {
    2: "The Dutch Army captain cannot be connected to a person-specific official or institutional record; a similarly named Holocaust victim is a rejected namesake.",
    3: "Initials-only searches could not distinguish the indexed person from numerous namesakes.",
    4: "Exact-name and spelling-variant searches produced no defensible identity bridge or dated pre-OSS affiliation.",
    5: "Obituary and genealogy candidates lacked two corroborating identifiers and were not assigned.",
    7: "A 1936-1937 directory employment lead lacked identifiers connecting that John A Stacy to the index row and was rejected.",
    8: "A 1940 amateur-radio listing and later vital-record leads did not establish OSS identity or employment.",
    9: "The principal exact-name result concerned a contemporary property holder and was chronologically inapplicable.",
    11: "Common-name searches returned multiple incompatible candidates and no corroborating identifiers.",
    13: "Real-estate and association results were chronologically or biographically incompatible and were rejected.",
    15: "A same-name wartime lead lacked a second identifier and remains confined to the private review system.",
    16: "Searches chiefly returned a nineteenth-century namesake and no plausible wartime identity bridge.",
    22: "Multiple incompatible records for Max Stamler lacked rank, service, box, or OSS corroboration.",
    23: "Exact-name, variant, occupation, obituary and archival searches produced no defensible match.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 735 and 736",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 443, rows 1-23; checked against layout-preserving text and a rendered page image",
            "access_date": "2026-10-25",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain immutable. Full protected identifiers remain private.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; seven accepted reviewed identity bridges",
            "access_date": "2026-10-25",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "No raw row or full protected identifier is retained in public assets. Coded occupations identify no employer.",
        },
        {
            "key": TECH,
            "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf",
            "archival_identifier": "NN3-064-03-008; National Archives Identifier 1263923",
            "title": "World War II Army Enlistment Records: Reference Copy of Technical Documentation",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives at College Park - Electronic Records",
            "publication_record_date": "1994-2005; reference copy modified 2011",
            "locator": "PDF physical pages 44-46; identifier, name, entry-date, grade and civilian-occupation fields",
            "access_date": "2026-10-25",
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
            "locator": "PDF physical pages 170-175 and 304; categories 056, 105, 484, 494, 736 and amended category 992 visually checked",
            "access_date": "2026-10-25",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical labels identify neither employers nor workplaces. The amended table on physical page 304 supersedes the earlier 9-92 label and maps code 992 to Students.",
        },
        {
            "key": NARA_STAIGER,
            "stable_url": "https://catalog.archives.gov/id/102069",
            "archival_identifier": "National Archives Identifier 102069",
            "title": "DUCK MISSION, THE: INTERVIEW WITH MAJ. STANLEY A. STAIGER, 09/1945",
            "author_creator": "Office of Strategic Services, Morale Operations Branch",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1945-09",
            "locator": "Catalog item title and archival description",
            "access_date": "2026-10-25",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "The item establishes an exact-name, exact-rank OSS identity context; it does not document pre-service employment.",
        },
        {
            "key": SMITHSONIAN_STAIGER,
            "stable_url": "https://americanhistory.si.edu/explore/exhibitions/price-of-freedom/online/world-war-ii/pacific-theater/final-blows",
            "title": "Final Blows: The Pacific Theater",
            "author_creator": "National Museum of American History",
            "repository_publisher": "Smithsonian Institution",
            "locator": "Weihsien liberation section identifying Major Stanley A. Staiger",
            "access_date": "2026-10-25",
            "source_quality": "B_authoritative_institutional",
            "rights_notes": "Institutional identity and wartime-context evidence only.",
        },
        {
            "key": AP_STAIGER,
            "stable_url": "https://lasvegassun.com/news/1999/feb/15/new-jersey-assemblywoman-seeks-soldiers-who-freed-/",
            "title": "New Jersey assemblywoman seeks soldiers who freed internment camp",
            "author_creator": "Associated Press",
            "repository_publisher": "Las Vegas Sun",
            "publication_record_date": "1999-02-15",
            "locator": "Profile of Major Stanley A. Staiger and his pre-service University of Oregon status",
            "access_date": "2026-10-25",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "rights_notes": "Project-authored paraphrase only; University attendance is modeled as student status, not employment.",
        },
        {
            "key": NCPEDIA_STALLINGS,
            "stable_url": "https://www.ncpedia.org/biography/stallings-laurence-tucker",
            "archival_identifier": "Dictionary of North Carolina Biography",
            "title": "Stallings, Laurence Tucker",
            "author_creator": "Erma Williams Glover",
            "repository_publisher": "University of North Carolina Press; NCpedia",
            "publication_record_date": "1994",
            "locator": "Biographical chronology covering the 1937 MGM contract and 1942 return to military service",
            "access_date": "2026-10-25",
            "source_quality": "B_authoritative_institutional",
            "rights_notes": "Project-authored paraphrases only. The index-to-biography identity remains qualified pending personnel-file review.",
        },
        {
            "key": BROADCASTING_STADLER,
            "stable_url": "https://www.worldradiohistory.com/Archive-All-BC/Broadcasting-Magazine/BC-1942/1942-06-08-BC.pdf",
            "archival_identifier": "Broadcasting, June 8, 1942",
            "title": "Returned Correspondents Describe Foreign Radio Listening",
            "author_creator": "Broadcasting magazine staff",
            "repository_publisher": "Broadcasting",
            "publication_record_date": "1942-06-08",
            "locator": "Contemporary report naming Glen Stadler of the United Press Paris bureau",
            "access_date": "2026-10-25",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "rights_notes": "Project-authored paraphrase only. The source establishes United Press work but not an OSS identity bridge.",
        },
        {
            "key": WARTIME_STAHL,
            "stable_url": "https://wartimearchive.com/document/oss-internal-memoranda-on-critiques-of-office-practices",
            "archival_identifier": "OSS memorandum, Martin Stahl to Captain William D. Rantack, 1945-06-28",
            "title": "OSS Internal Memoranda on Critiques of Office Practices",
            "author_creator": "Martin Stahl and Office of Strategic Services",
            "repository_publisher": "The Wartime Archive",
            "publication_record_date": "1945-06-28",
            "locator": "Preview page 6; Overseas Report on Central European Section and Westfield Mission work",
            "access_date": "2026-10-25",
            "source_quality": "D_correlative_or_secondary",
            "rights_notes": "A public-domain scan is hosted by a secondary commercial archive. The common-name identity remains unconfirmed and is not published as fact.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": "university-oregon-b906",
            "organization_id": "e21c0239-53db-582a-b036-1ec043c0e8b2",
            "canonical_name": "University of Oregon",
            "historical_name": "University of Oregon",
            "aliases": ["Oregon", "University of Oregon, Eugene"],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "Eugene",
            "state_or_region": "Oregon",
            "country": "United States",
            "normalization_notes": "Student status is modeled separately from employment.",
        },
        {
            "key": "mgm-b906",
            "organization_id": "f40d460a-3c35-5d71-91f1-b2b1c5ea53bd",
            "canonical_name": "Metro-Goldwyn-Mayer",
            "historical_name": "Metro-Goldwyn-Mayer",
            "aliases": ["MGM"],
            "organization_type": "film studio",
            "sector": "arts_and_culture",
            "city": "Culver City",
            "state_or_region": "California",
            "country": "United States",
            "normalization_notes": "The historical employer name is retained; no modern successor is substituted.",
        },
        {
            "key": "united-press-b906",
            "organization_id": "ea6250da-ba89-5ae0-8c8c-d3d2897c6a21",
            "canonical_name": "United Press",
            "historical_name": "United Press",
            "aliases": [],
            "organization_type": "news agency",
            "sector": "journalism_and_media",
            "city": "New York",
            "state_or_region": "New York",
            "country": "United States",
            "active_dates": "1907-1958 under this name",
            "normalization_notes": "The 1942 agency name is preserved and not silently replaced by United Press International.",
        },
    ]


def army_affiliation(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    person_id, name = PEOPLE[row]
    return {
        "key": f"{slug(name)}-occupation-b906",
        "person_id": person_id,
        "relationship_type": "employment",
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
        "research_notes": "The historical category is not converted into a named employer, workplace or exact title.",
    }


def substantive_affiliations() -> list[dict[str, object]]:
    return [
        {
            "key": "stanley-staiger-oregon-student-b906",
            "person_id": PEOPLE[18][0],
            "organization_key": "university-oregon-b906",
            "organization_name_as_found": "University of Oregon",
            "role_title": "student; ROTC class member",
            "relationship_type": "student",
            "date_precision": "Immediately before being called to active duty during World War II; the source says he remained 23 credits short of an economics degree.",
            "city": "Eugene",
            "state_or_region": "Oregon",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "published",
            "research_notes": "This is a pre-service student affiliation, not employment and not proof of the immediate pre-OSS predecessor.",
        },
        {
            "key": "laurence-stallings-mgm-b906",
            "person_id": PEOPLE[20][0],
            "organization_key": "mgm-b906",
            "organization_name_as_found": "MGM",
            "role_title": "contract screenwriter",
            "occupation": "writer and screenwriter",
            "relationship_type": "employment",
            "start_date": "1937",
            "end_date": "1942",
            "date_precision": "The biography places a new MGM contract and move to California in 1937, followed by return to Washington as a Marine officer in 1942.",
            "city": "Culver City",
            "state_or_region": "California",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": True,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "probable",
            "claim_confidence": "medium",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "publish_qualified",
            "research_notes": "The distinctive full name and compatible wartime chronology support a probable identity, but no external source yet links this biography directly to the index row or OSS transfer.",
        },
        {
            "key": "glen-stadler-united-press-b906",
            "person_id": PEOPLE[10][0],
            "organization_key": "united-press-b906",
            "organization_name_as_found": "United Press",
            "role_title": "Paris bureau correspondent",
            "occupation": "journalist",
            "relationship_type": "employment",
            "end_date": "1942",
            "date_precision": "A June 1942 contemporary account says Glen Stadler served in the Paris bureau for 13 months after the German occupation and was later interned in Germany.",
            "city": "Paris",
            "country": "France",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "probable",
            "claim_confidence": "medium",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "publish_qualified",
            "research_notes": "United Press employment is documented, but the accessible source does not prove that this was the indexed person or the immediate predecessor to OSS.",
        },
    ]


def army_claims(item: dict[str, object]) -> list[dict[str, object]]:
    row = int(item["row"])
    person_id, name = PEOPLE[row]
    identity = {
        "key": f"identity-{slug(name)}-b906",
        "person_id": person_id,
        "claim_type": "identity",
        "claim_text": f"The indexed {name} row is a high-confidence match to the reviewed official Army record.",
        "evidence_paraphrase": "A nonshared protected identifier and compatible name connect the visually verified index row to the official Army record.",
        "identity_match_assessment": "High confidence from the nonshared protected-identifier bridge and name alignment.",
        "temporal_assessment": "The Army record supports identity and a dated occupation category; it does not establish the OSS transfer sequence.",
        "source_quality": "A_direct_official",
        "claim_confidence": "high",
        "publication_status": "published",
        "match_notes": "No protected identifier is exposed, and the coded occupation is kept separate from employer claims.",
        "sources": [
            {"source_key": INDEX, "locator_override": f"PDF page 443 row {row}; protected identifier withheld"},
            {"source_key": ARMY, "locator_override": "Accepted reviewed identity bridge; protected identifier withheld"},
        ],
    }
    occupation = {
        "key": f"occupation-{slug(name)}-b906",
        "person_id": person_id,
        "affiliation_key": f"{slug(name)}-occupation-b906",
        "claim_type": "occupation",
        "claim_text": f"At Army entry on {item['date']}, the official record assigned {name} the historical civilian-occupation category '{item['occupation']}'; no employer is identified.",
        "evidence_paraphrase": f"The Army entry field carries code {item['code']}, which the visually checked NARA code list maps to the stated category.",
        "identity_match_assessment": "High confidence from a nonshared protected-identifier bridge between the index and official Army record.",
        "temporal_assessment": "Strongly date-bounded at Army entry, but neither immediate pre-OSS status nor a named employer is established.",
        "source_quality": "A_direct_official",
        "claim_confidence": "medium",
        "publication_status": "publish_qualified",
        "match_notes": "Historical code-language is retained and excluded from default confirmed/high-confidence employer analytics.",
        "sources": [
            {"source_key": ARMY, "locator_override": f"Army-entry date {item['date']}; occupation code {item['code']}; protected identifier withheld"},
            {"source_key": TECH, "support_type": "context_only", "locator_override": "Civilian-occupation field definition"},
            {"source_key": CODES, "locator_override": item["locator"]},
        ],
    }
    return [identity, occupation]


def substantive_claims() -> list[dict[str, object]]:
    return [
        {
            "key": "identity-stanley-a-staiger-b906",
            "person_id": PEOPLE[18][0],
            "claim_type": "identity",
            "claim_text": "The indexed Major Stanley A. Staiger is a high-confidence match to the OSS officer interviewed about the DUCK Mission and identified with the Weihsien liberation team.",
            "evidence_paraphrase": "An official NARA item repeats the exact full name and rank in an OSS interview; Smithsonian and Associated Press accounts supply compatible mission context.",
            "identity_match_assessment": "High confidence from exact full name, exact rank and two specific, mutually compatible wartime contexts.",
            "temporal_assessment": "The sources establish 1945 OSS service and earlier student-to-military chronology, but not the exact Army-to-OSS transfer date.",
            "source_quality": "A_direct_official",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "The personnel file remains necessary to establish the immediate pre-OSS assignment.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 443 row 18; Major; officer identifier withheld"},
                {"source_key": NARA_STAIGER, "locator_override": "Catalog item title; September 1945 interview"},
                {"source_key": SMITHSONIAN_STAIGER, "locator_override": "Weihsien liberation-team context"},
            ],
        },
        {
            "key": "student-stanley-staiger-oregon-b906",
            "person_id": PEOPLE[18][0],
            "affiliation_key": "stanley-staiger-oregon-student-b906",
            "claim_type": "other_pre_oss_affiliation",
            "claim_text": "Immediately before being called to active military duty, Stanley A. Staiger was an economics student and ROTC class member at the University of Oregon; the university was not his employer.",
            "evidence_paraphrase": "An Associated Press retrospective reports that his ROTC class was called to active duty while he remained 23 credits short of an economics degree.",
            "identity_match_assessment": "High confidence through exact name and the same specific Weihsien liberation mission documented by institutional and official sources.",
            "temporal_assessment": "Strongly date-bounded immediately before military service, but not proven to be immediately before OSS assignment.",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "Student status is modeled separately and excluded from employer analytics.",
            "sources": [{"source_key": AP_STAIGER, "locator_override": "Pre-service biography and University of Oregon chronology"}],
        },
        {
            "key": "identity-laurence-t-stallings-b906",
            "person_id": PEOPLE[20][0],
            "claim_type": "identity",
            "claim_text": "Laurence T. Stallings is a probable match to the writer and Marine officer Laurence Tucker Stallings.",
            "evidence_paraphrase": "The distinctive full name and compatible 1942 Washington military chronology support the candidate, but the biography does not mention OSS or the index box.",
            "identity_match_assessment": "Probable, not confirmed; no direct personnel-file, identifier or OSS-unit bridge is available online.",
            "temporal_assessment": "The biography directly sequences MGM work before renewed military service, not before a documented OSS transfer.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "medium",
            "publication_status": "publish_qualified",
            "match_notes": "The qualified identity is excluded from default employer analytics until the Box 736 file is reviewed.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 443 row 20; Box 736"},
                {"source_key": NCPEDIA_STALLINGS, "locator_override": "Biographical chronology, 1937-1943"},
            ],
        },
        {
            "key": "last-civilian-laurence-stallings-mgm-b906",
            "person_id": PEOPLE[20][0],
            "affiliation_key": "laurence-stallings-mgm-b906",
            "claim_type": "last_civilian_pre_service",
            "claim_text": "If the indexed person is Laurence Tucker Stallings, Metro-Goldwyn-Mayer was his last documented civilian employer before he returned to military service in 1942.",
            "evidence_paraphrase": "The institutional biography places a new MGM contract in 1937 and his return to Washington as a Marine officer in 1942.",
            "identity_match_assessment": "Probable index-to-biography match based on the distinctive full name and compatible wartime chronology.",
            "temporal_assessment": "Strongly date-bounded as last civilian employment before military service; it is not labeled the immediate pre-OSS affiliation.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "medium",
            "publication_status": "publish_qualified",
            "match_notes": "The conditional wording and qualified badge must remain until the personnel file supplies a direct bridge.",
            "sources": [{"source_key": NCPEDIA_STALLINGS, "locator_override": "Biographical chronology, 1937 MGM contract and 1942 military service"}],
        },
        {
            "key": "identity-glen-m-stadler-b906",
            "person_id": PEOPLE[10][0],
            "claim_type": "identity",
            "claim_text": "Glen M. Stadler is a probable match to United Press correspondent Glen Stadler, but the accessible source does not independently establish OSS service.",
            "evidence_paraphrase": "A contemporary trade-journal report places Glen Stadler in United Press's Paris bureau and records his wartime internment in Germany.",
            "identity_match_assessment": "Probable from the uncommon name and compatible wartime chronology; the missing middle initial and OSS bridge prevent a high-confidence identification.",
            "temporal_assessment": "The source documents wartime journalism before possible OSS service but does not establish the transition.",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "claim_confidence": "medium",
            "publication_status": "publish_qualified",
            "match_notes": "Box 735 review is required before the identity or chronology is upgraded.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 443 row 10; Box 735"},
                {"source_key": BROADCASTING_STADLER, "locator_override": "June 8, 1942 report on repatriated United Press correspondents"},
            ],
        },
        {
            "key": "prewar-glen-stadler-united-press-b906",
            "person_id": PEOPLE[10][0],
            "affiliation_key": "glen-stadler-united-press-b906",
            "claim_type": "other_pre_oss_affiliation",
            "claim_text": "A probable match worked for United Press in its Paris bureau before returning from wartime internment in 1942; the evidence does not prove this was his immediate pre-OSS affiliation.",
            "evidence_paraphrase": "The June 1942 account identifies Glen Stadler among repatriated United Press correspondents and describes his 13 months in the Paris bureau after occupation.",
            "identity_match_assessment": "Probable, with the uncommon name and chronology supporting but not conclusively proving the index match.",
            "temporal_assessment": "Documented prewar/wartime employment; immediate sequence and later service transition remain unknown.",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "claim_confidence": "medium",
            "publication_status": "publish_qualified",
            "match_notes": "Excluded from default employer analytics because identity remains probable.",
            "sources": [{"source_key": BROADCASTING_STADLER, "locator_override": "June 8, 1942 report on United Press Paris bureau work"}],
        },
        {
            "key": "candidate-martin-stahl-westfield-b906",
            "person_id": PEOPLE[15][0],
            "claim_type": "identity",
            "claim_text": "A 1945 OSS memorandum by a Martin Stahl is a candidate lead for the indexed Martin Stahl, not a confirmed identity.",
            "evidence_paraphrase": "The memo's author reports work in the Central European Section, SO Branch, London and the Westfield Mission in Stockholm during 1944-1945.",
            "identity_match_assessment": "Ambiguous: the exact name is insufficient for a common-name case, and no service identifier, rank, birth detail or box reference corroborates it.",
            "temporal_assessment": "The memorandum documents OSS assignments for its author, but no pre-OSS affiliation and no bridge to the indexed person.",
            "source_quality": "D_correlative_or_secondary",
            "claim_confidence": "low",
            "publication_status": "needs_review",
            "match_notes": "Retained in the private review system only; the public profile must not present it as a fact.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 443 row 15; Box 736"},
                {"source_key": WARTIME_STAHL, "locator_override": "Preview page 6; June 28, 1945 Overseas Report"},
            ],
        },
    ]


def unresolved_update(row: int) -> dict[str, object]:
    person_id, name = PEOPLE[row]
    category = "unknown_or_indeterminate"
    commissioned: bool | None = None
    foreign: bool | None = None
    if row == 2:
        category, commissioned, foreign = "foreign_or_allied_military_personnel", True, True
    elif row == 22:
        category, commissioned = "commissioned_army_officer", True
    elif row == 15:
        identity_status = "ambiguous"
    else:
        identity_status = "unresolved"
    update: dict[str, object] = {
        "person_id": person_id,
        "identity_status": "ambiguous" if row == 15 else "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, rank when printed, box and archive location, but staged official-context, CIA Reading Room, exact-name, occupation, employer, obituary, institutional, newspaper, directory, Library of Congress and archival searches found no defensible identity bridge. {UNRESOLVED[row]}",
        "personnel_category": category,
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": f"Review the indexed Box {'735' if row < 15 else '736'} personnel file for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "critical" if row in {2, 3, 15, 22} else "high",
    }
    if commissioned is not None:
        update["commissioned_officer"] = commissioned
    if foreign is not None:
        update["allied_or_foreign_personnel"] = foreign
    if row == 15:
        update["next_action"] = "Review Martin Stahl's Box 736 file for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer; private same-name candidates must not be transferred without a second identifier."
    return update


def person_updates() -> list[dict[str, object]]:
    updates: list[dict[str, object]] = []
    for item in ARMY_OCCUPATIONS:
        row = int(item["row"])
        person_id, _name = PEOPLE[row]
        updates.append(
            {
                "person_id": person_id,
                "identity_status": "high_confidence",
                "identity_evidence": "A nonshared protected identifier and compatible name connect the visually verified index row to the reviewed official Army record. The historical occupation field remains separate from employer and immediate-affiliation claims.",
                "personnel_category": "enlisted_army_personnel",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "occupation_only_found",
                "next_action": "Review the indexed personnel file to identify the immediate pre-OSS affiliation and last civilian employer; do not convert the Army occupation category into a named employer.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            }
        )
    updates.extend(
        [
            {
                "person_id": PEOPLE[18][0],
                "identity_status": "high_confidence",
                "identity_evidence": "The exact full name and Major rank align between the index and an official NARA OSS interview; Smithsonian and Associated Press accounts independently supply the same specific Weihsien liberation context.",
                "personnel_category": "commissioned_army_officer",
                "commissioned_officer": True,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "completed",
                "next_action": "Review Box 736 to identify Major Staiger's immediate Army assignment before OSS and any last civilian employer; retain University of Oregon as student status only.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "nara_catalog_id": "102069",
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[20][0],
                "identity_status": "probable",
                "identity_evidence": "The distinctive full name and compatible 1942 Washington military chronology support Laurence Tucker Stallings as a probable match, but no direct identifier or OSS-unit bridge is available online.",
                "manual_review_required": True,
                "research_status": "documented_prewar_employer_found",
                "next_action": "Review Box 736 to confirm the identity, OSS relationship and transfer chronology before upgrading the qualified MGM finding.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[10][0],
                "identity_status": "probable",
                "identity_evidence": "The uncommon name and compatible wartime chronology support the United Press correspondent as a probable match, but the contemporary source omits the middle initial and does not mention OSS.",
                "manual_review_required": True,
                "research_status": "documented_prewar_employer_found",
                "next_action": "Review Box 735 to confirm the United Press identity and determine whether that work immediately preceded military or OSS service.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
        ]
    )
    for row in UNRESOLVED:
        updates.append(unresolved_update(row))
    return updates


def research_attempts() -> list[dict[str, object]]:
    source_rows = {1, 6, 10, 12, 14, 15, 17, 18, 19, 20, 21}
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        reviewed = row in source_rows
        if row in {10, 15, 20}:
            outcome = "candidate_found"
        elif reviewed:
            outcome = "source_reviewed"
        else:
            outcome = "candidate_rejected"
        detail = (
            "Reviewed evidence established an official identity/occupation bridge or a carefully qualified institutional candidate."
            if reviewed
            else UNRESOLVED[row]
        )
        attempts.append(
            {
                "key": f"page443-row{row}-{slug(name)}-b906",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA/index context; CIA Reading Room exact-name check; OSS and rank variants; employer and occupation; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Box {'735' if row < 15 else '736'}; protected-identifier Army crosswalk where available",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_906",
                "started_at": "2026-10-25T19:15:00Z",
                "completed_at": "2026-10-25T23:30:00Z",
                "outcome": outcome,
                "sources_reviewed": 9 if row in {18, 20} else (7 if reviewed else 6),
                "candidate_sources_rejected": 5 if reviewed else 7,
                "rejection_reasons": "Unbridged namesakes, discovery-only results, chronologically irrelevant records and postwar-only leads were not assigned." if reviewed else UNRESOLVED[row],
                "research_notes": f"{detail} Search-result snippets were discovery aids only, no access control was bypassed, and no exposed NARA API credential was used.",
                "next_action": f"Review the indexed Box {'735' if row < 15 else '736'} personnel file for corroborating identifiers and the last documented pre-OSS affiliation.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b906-v1",
            }
        )
    return attempts


def main() -> None:
    affiliations = [army_affiliation(item) for item in ARMY_OCCUPATIONS]
    affiliations.extend(substantive_affiliations())
    claims: list[dict[str, object]] = []
    for item in ARMY_OCCUPATIONS:
        claims.extend(army_claims(item))
    claims.extend(substantive_claims())
    bundle = {
        "bundle_version": "batch-906-v1",
        "reviewer": "Before OSS Batch 906 evidence review",
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
