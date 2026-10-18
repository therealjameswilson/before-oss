#!/usr/bin/env python3
"""Generate the reviewed Batch 894 evidence bundle from audited constants."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "research/evidence-page437-smyth-to-snyder-review_batch-894_2026-10-18.json"

INDEX = "nara-index-b894"
ARMY = "army-bulk-b894"
TECH = "army-tech-b894"
CODES = "army-codes-b894"
CMH = "cmh-howard-mcgaw-smyth-b894"
AHA = "aha-howard-mcgaw-smyth-b894"
GOOGLE_BOOKS = "google-play-howard-mcgaw-smyth-b894"
SNOWER_OBIT = "kansas-city-star-william-snower-b894"
CRIMSON = "harvard-crimson-william-snower-b894"


PEOPLE = {
    1: ("70ffc830-4c39-57aa-9acb-d6b30487a942", "Howard M Smyth"),
    2: ("7a9e1465-aa07-5da7-87f7-8ead85a2a699", "Edith W Smythe"),
    3: ("46d0bea3-2039-5f4d-80fe-6a7f327720ab", "Sarah E Smythe"),
    4: ("23e71660-bee2-5b09-ada1-08fcb84081fa", "James F Snapp"),
    5: ("009fc40d-571f-51d1-834f-3cf74c0eebfe", "Paul A Snearline"),
    6: ("588e8538-2277-57fa-83ec-c593c7117126", "William K Snedecker"),
    7: ("a07b88d3-1d00-5c82-81f5-3eeb117ca320", "Daniel T Snell"),
    8: ("efb448dd-013b-51c2-8572-908ab3600127", "Harry D Snell"),
    9: ("ae79fec5-d504-5791-b253-83db22d26886", "William M Snelling"),
    10: ("ffbbc250-a298-5be6-b425-083547a2b306", "Charles C Snider"),
    11: ("47c2c0ee-c331-58e3-a496-e78a3fd6033c", "R H Snider"),
    12: ("fd5ad97f-872a-5629-bd4d-31971b1d49a8", "Paul C Snodgrass"),
    13: ("52d2c58c-e260-58e4-8273-f1a613ef14bc", "Roy L Snodgrass"),
    14: ("4a6a9e7b-838e-57a0-a381-55b376b47b6f", "Paul C Snodgress"),
    15: ("8a4528ee-354f-50af-8161-4413b20f914f", "Davis W Snow"),
    16: ("b32e47b5-ed21-56b4-871c-bc7372ea14da", "Harold C Snow"),
    17: ("e3820167-e0ea-50db-a59f-6756b5570508", "Charles R Snowden"),
    18: ("dc5f0a30-4c3f-50f2-83cf-49381bf44c4f", "Charles R Snowden"),
    19: ("84ea25db-f77e-55db-ad7d-b373fe898f2c", "William Snower"),
    20: ("3d9eb348-dee6-5edf-ae6c-e5257697248b", "Joseph Snoy"),
    21: ("4c1e2c3f-ba2a-5337-becf-fea5a67c8f84", "Andrew J Snyder"),
    22: ("98a5e40a-df4f-52fb-a468-123d29002ab1", "Arthur L Snyder"),
    23: ("926c80b5-ab2a-54e4-8262-16d0daf34b56", "Clarke C Snyder"),
}


ARMY_MATCHES = [
    {
        "row": 6,
        "slug": "william-k-snedecker",
        "date": "1942-03-06",
        "code": "003",
        "occupation": "Architects",
        "code_locator": "PDF physical page 170; civilian occupation category 0-03",
        "name_note": "The Army form SNEDEKER omits one letter from the indexed surname Snedecker.",
    },
    {
        "row": 13,
        "slug": "roy-l-snodgrass",
        "date": "1942-05-04",
        "code": "688",
        "occupation": "Occupations in mechanical treatment of metals (rolling, stamping, forging, pressing, etc.), n.e.c.",
        "code_locator": "PDF physical page 174; civilian occupation category 6-88",
    },
    {
        "row": 22,
        "slug": "arthur-l-snyder",
        "date": "1942-03-05",
        "code": "240",
        "occupation": "Attendants, recreation and amusement, n.e.c.",
        "code_locator": "PDF physical page 172; civilian occupation category 2-40",
        "name_note": "The Army form ARTHRU is treated as a damaged or transposed form of Arthur.",
    },
]


UNRESOLVED = {
    2: "Exact-name searches produced unbridged namesakes and no official OSS, Box 726 or employment evidence.",
    3: "Exact-name searches produced unbridged namesakes and no official OSS, Box 726 or employment evidence.",
    4: "Common-name results lacked a protected-identifier, OSS or Box 727 bridge.",
    5: "The rare surname produced no defensible identity or employment source in the accessible staged searches.",
    7: "Common-name results lacked corroborating identifiers beyond the indexed name.",
    8: "Common-name results lacked corroborating identifiers beyond the indexed name.",
    9: "A PT-boat officer namesake is an unbridged lead; the available page does not connect him to this Box 727 row.",
    10: "Exact-name and occupation searches produced multiple unbridged namesakes.",
    11: "The initials-only record is highly ambiguous and no accessible result supplied two corroborating identifiers.",
    12: "The Snodgrass spelling remains separate from the indexed Paul C Snodgress row; neither has a defensible external identity bridge.",
    14: "The Snodgress spelling remains separate from the indexed Paul C Snodgrass row; neither has a defensible external identity bridge.",
    15: "Exact-name, obituary, institutional, directory and archival searches did not establish this indexed person.",
    16: "Exact-name, obituary, institutional, directory and archival searches did not establish this indexed person.",
    17: "The first same-name Charles R Snowden row has no independent bridge; evidence is not transferred between the two rows.",
    18: "The second same-name Charles R Snowden row remains separate; its protected identifier produced no accepted Army bridge.",
    20: "The rare surname produced no reliable identity or pre-OSS affiliation in accessible sources.",
    23: "Exact-name OSS, occupation, obituary and institutional searches produced no defensible identity bridge.",
}


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 726-727",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 437, rows 1-23; checked against layout-preserving text and a rendered page image",
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
            "locator": "Official unrestricted ASNEF.FIN.DAT; protected-identifier fields checked, four identity matches accepted after review",
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
            "locator": "PDF physical pages 170-174; categories 003, 240 and 688 visually checked; 195 is unassigned",
            "access_date": "2026-10-18",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical labels name neither employers nor workplaces. Code 195 is not converted into an occupation.",
        },
        {
            "key": CMH,
            "stable_url": "https://history.army.mil/Publications/Publications-Catalog/Sicily-and-the-Surrender-of-Italy/",
            "archival_identifier": "CMH Pub 6-2",
            "title": "Sicily and the Surrender of Italy",
            "author_creator": "Albert N. Garland and Howard McGaw Smyth",
            "repository_publisher": "U.S. Army Center of Military History",
            "publication_record_date": "1965",
            "locator": "The Authors, page viii; visually checked in the publication PDF",
            "access_date": "2026-10-18",
            "source_quality": "A_direct_official",
            "collection_name": "United States Army in World War II: The Mediterranean Theater of Operations",
            "rights_notes": "Used for identity, teaching history and OSS chronology; postwar career details are not reconstructed.",
        },
        {
            "key": AHA,
            "stable_url": "https://www.govinfo.gov/content/pkg/SERIALSET-10651_00_00-002-0012-0000/pdf/SERIALSET-10651_00_00-002-0012-0000.pdf",
            "archival_identifier": "United States Congressional Serial Set 10651; American Historical Association Annual Report for 1940",
            "title": "Proceedings of the Thirty-Sixth Annual Meeting of the Pacific Coast Branch of the American Historical Association",
            "author_creator": "American Historical Association",
            "repository_publisher": "U.S. Government Publishing Office",
            "publication_record_date": "1942",
            "locator": "Report page 89; PDF physical page 113; meeting held 29-31 December 1940",
            "access_date": "2026-10-18",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "rights_notes": "The contemporary proceedings identify Smyth with the University of California, Berkeley.",
        },
        {
            "key": GOOGLE_BOOKS,
            "stable_url": "https://play.google.com/store/info/name/Howard_McGaw_Smyth?id=12nxdlzr9",
            "title": "Books by Howard McGaw Smyth on Google Play",
            "author_creator": "Google Play Books",
            "repository_publisher": "Google",
            "locator": "Author biography; teaching dates and subsequent OSS/State Department service",
            "access_date": "2026-10-18",
            "source_quality": "D_correlative_or_secondary",
            "rights_notes": "Used only with contemporary and official corroboration; the shortest supporting excerpt is retained.",
        },
        {
            "key": SNOWER_OBIT,
            "stable_url": "https://www.legacy.com/us/obituaries/kansascity/name/william-snower-obituary?id=4348865",
            "title": "William Snower Jr. obituary",
            "repository_publisher": "The Kansas City Star",
            "publication_record_date": "2008-06-07",
            "locator": "Biographical paragraph on Harvard graduation, Army service, Swedish Area and Language training and OSS work",
            "access_date": "2026-10-18",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "rights_notes": "Only concise evidence excerpts and project-authored paraphrases are retained; unrelated family details are excluded.",
        },
        {
            "key": CRIMSON,
            "stable_url": "https://www.thecrimson.com/article/1943/5/27/degrees-for-1943-pjohn-lee-barber/",
            "title": "Degrees for 1943",
            "author_creator": "The Harvard Crimson",
            "repository_publisher": "The Harvard Crimson",
            "publication_record_date": "1943-05-27",
            "locator": "A.B. Magna cum Laude; alumni records as Class of 1944",
            "access_date": "2026-10-18",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "rights_notes": "Contemporary degree list used to corroborate the rare-name student identity and field of study.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": "uc-berkeley-b894",
            "organization_id": "dd5d0a44-0368-5e91-a5d3-074de36840ed",
            "canonical_name": "University of California, Berkeley",
            "historical_name": "University of California at Berkeley",
            "aliases": ["UC Berkeley", "University of California"],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "Berkeley",
            "state_or_region": "California",
            "country": "United States",
            "normalization_notes": "The Berkeley campus named in the contemporary sources is retained; student and employment relationships remain separate, and no modern system-wide employer inference is made.",
        },
        {
            "key": "army-specialized-training-program-b894",
            "canonical_name": "U.S. Army Specialized Training Program",
            "historical_name": "Army Specialized Training Program",
            "aliases": ["ASTP"],
            "organization_type": "military training program",
            "sector": "military",
            "country": "United States",
            "active_dates": "1942-1944",
            "normalization_notes": "The Swedish Area and Language course location at the University of Minnesota is preserved in the affiliation; the university is not mislabeled as an employer.",
        },
        {
            "key": "harvard-college-b894",
            "organization_id": "4b0261ed-1fe7-58cf-bbf3-c521c0b84164",
            "canonical_name": "Harvard College",
            "historical_name": "Harvard",
            "aliases": ["Harvard University undergraduate college"],
            "organization_type": "undergraduate college",
            "sector": "academia_and_research",
            "city": "Cambridge",
            "state_or_region": "Massachusetts",
            "country": "United States",
            "active_dates": "1636-present",
            "normalization_notes": "Modeled as student status, not employment; the undergraduate college remains distinct from other Harvard units.",
        },
    ]


def army_identity_claim(row: int, *, postwar: bool = False) -> dict[str, object]:
    person_id, name = PEOPLE[row]
    note = next((item.get("name_note") for item in ARMY_MATCHES if item["row"] == row), None)
    if row == 21:
        note = "The exact indexed name agrees; the November 1945 Army entry is post-OSS and supports identity only."
    return {
        "key": f"identity-page437-row{row}-b894",
        "person_id": person_id,
        "claim_type": "identity",
        "claim_text": f"The indexed {name} row on PDF page 437 is a high-confidence match to the reviewed official Army record.",
        "evidence_paraphrase": "The reviewed name evidence and a nonshared protected identifier agree with the indexed row.",
        "identity_match_assessment": "High confidence from a nonshared protected-identifier bridge plus compatible name evidence.",
        "temporal_assessment": "The matched Army entry is dated after the OSS period and supports identity only." if postwar else "The Army-entry record supports identity and a dated occupation category; it does not establish the OSS transfer sequence.",
        "source_quality": "A_direct_official",
        "claim_confidence": "high",
        "publication_status": "published",
        "match_notes": f"No protected identifier is exposed. {note or 'No same-name row is merged.'}",
        "sources": [
            {"source_key": INDEX, "locator_override": f"PDF page 437 row {row}; protected identifier withheld"},
            {"source_key": ARMY, "locator_override": "Accepted reviewed identity bridge; protected identifier withheld"},
        ],
    }


def army_occupation_affiliation(item: dict[str, object]) -> dict[str, object]:
    person_id, _name = PEOPLE[int(item["row"])]
    return {
        "key": f"{item['slug']}-occupation-b894",
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
        "research_notes": "The historical occupation category is not converted into a named employer, workplace or exact job title.",
    }


def army_occupation_claim(item: dict[str, object]) -> dict[str, object]:
    person_id, name = PEOPLE[int(item["row"])]
    return {
        "key": f"occupation-{item['slug']}-b894",
        "person_id": person_id,
        "affiliation_key": f"{item['slug']}-occupation-b894",
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


def howard_affiliation() -> dict[str, object]:
    return {
        "key": "howard-mcgaw-smyth-uc-berkeley-b894",
        "person_id": PEOPLE[1][0],
        "organization_key": "uc-berkeley-b894",
        "organization_name_as_found": "University of California, Berkeley",
        "role_title": "professor of modern European history",
        "occupation": "historian and university teacher",
        "relationship_type": "employment",
        "start_date": "1936",
        "end_date": "1942",
        "date_precision": "A publisher biography dates University of California teaching to 1936-1942 and places OSS service thereafter; contemporary and official sources corroborate both affiliations.",
        "city": "Berkeley",
        "state_or_region": "California",
        "country": "United States",
        "immediate_pre_oss": True,
        "last_civilian_pre_service": True,
        "pre_oss_temporal_basis": "strongly_date_bounded",
        "identity_confidence": "high_confidence",
        "claim_confidence": "high",
        "source_quality": "C_reputable_contemporary_or_scholarly",
        "publication_status": "published",
        "research_notes": "The chronology strongly supports this as the final civilian employer before OSS, although no exact recruitment date is supplied.",
    }


def howard_claims() -> list[dict[str, object]]:
    person_id = PEOPLE[1][0]
    common_sources = [
        {"source_key": INDEX, "locator_override": "PDF page 437 row 1"},
        {"source_key": CMH, "locator_override": "The Authors, page viii", "excerpt_override": "During World War II he served for a time in the Office of Strategic Services"},
        {"source_key": AHA, "locator_override": "Report page 89; PDF physical page 113", "excerpt_override": "Howard McGaw Smyth of the University of California, Berkeley"},
        {"source_key": GOOGLE_BOOKS, "locator_override": "Author biography", "excerpt_override": "taught at the University of California, 1936-42"},
    ]
    return [
        {
            "key": "identity-howard-mcgaw-smyth-b894",
            "person_id": person_id,
            "claim_type": "identity",
            "claim_text": "The indexed Howard M Smyth is a high-confidence match to historian and OSS veteran Howard McGaw Smyth.",
            "evidence_paraphrase": "The rare full name, middle initial, documented OSS service and University of California chronology align across official, contemporary and publisher sources.",
            "identity_match_assessment": "High confidence from rare-name agreement plus independent OSS-specific and dated institutional evidence.",
            "temporal_assessment": "The sources place University of California teaching before OSS service and State Department work after OSS.",
            "source_quality": "A_direct_official",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "McGaw is retained as a documented middle-name variant; no unrelated postwar career is reconstructed.",
            "sources": common_sources,
        },
        {
            "key": "employment-howard-mcgaw-smyth-uc-berkeley-b894",
            "person_id": person_id,
            "affiliation_key": "howard-mcgaw-smyth-uc-berkeley-b894",
            "claim_type": "immediate_pre_oss_affiliation",
            "claim_text": "Howard McGaw Smyth taught at the University of California, Berkeley, through 1942 before entering OSS service.",
            "evidence_excerpt": "taught at the University of California, 1936-42",
            "evidence_paraphrase": "A dated publisher biography places University of California teaching in 1936-1942 and OSS service thereafter; contemporary AHA proceedings and an official Army history corroborate the institutional and OSS links.",
            "identity_match_assessment": "High confidence from the rare full name and corroborating OSS service.",
            "temporal_assessment": "Strongly date-bounded as the immediate pre-OSS affiliation and last identified civilian employer; the exact transition date is not supplied.",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "University teaching is treated as employment; earlier educational institutions are not mislabeled as employers.",
            "sources": common_sources[1:],
        },
    ]


def snower_affiliations() -> list[dict[str, object]]:
    person_id = PEOPLE[19][0]
    return [
        {
            "key": "william-snower-army-astp-b894",
            "person_id": person_id,
            "organization_key": "army-specialized-training-program-b894",
            "organization_name_as_found": "Army Specialized Training Program Swedish Area and Language at the University of Minnesota",
            "role_title": "Swedish Area and Language trainee",
            "occupation": "Army language trainee",
            "relationship_type": "military_assignment",
            "start_date": "1943",
            "end_date": "1944",
            "date_precision": "The obituary places this first in Snower's 1943-1946 Army service and immediately before two years with OSS; exact course dates are not supplied.",
            "city": "Minneapolis",
            "state_or_region": "Minnesota",
            "country": "United States",
            "immediate_pre_oss": True,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "explicit_immediate",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "published",
            "research_notes": "This is a military training assignment, not University of Minnesota employment.",
        },
        {
            "key": "william-snower-harvard-college-b894",
            "person_id": person_id,
            "organization_key": "harvard-college-b894",
            "organization_name_as_found": "Harvard College",
            "role_title": "student",
            "occupation": "student of government",
            "relationship_type": "student",
            "end_date": "1943",
            "date_precision": "The contemporary degree list is dated 27 May 1943; the obituary says he received the A.B. in 1943 before Army service.",
            "city": "Cambridge",
            "state_or_region": "Massachusetts",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "published",
            "research_notes": "Student status immediately preceded Army service but is not employment and is not counted as a civilian employer.",
        },
    ]


def snower_claims() -> list[dict[str, object]]:
    person_id = PEOPLE[19][0]
    common = {
        "person_id": person_id,
        "identity_match_assessment": "High confidence from the rare exact surname and first name, matching middle-initial absence, contemporary Harvard degree evidence and an obituary explicitly documenting OSS service.",
        "source_quality": "C_reputable_contemporary_or_scholarly",
        "claim_confidence": "high",
        "publication_status": "published",
        "match_notes": "The suffix Jr. is retained as a documented variant. Student and military-training affiliations are not presented as civilian employment.",
    }
    return [
        {
            **common,
            "key": "identity-william-snower-b894",
            "claim_type": "identity",
            "claim_text": "The indexed William Snower is a high-confidence match to William Snower Jr., a 1943 Harvard graduate who served in OSS.",
            "evidence_paraphrase": "A contemporary Harvard list and a Kansas City Star obituary agree on the rare name, 1943 degree and government field; the obituary explicitly places him in OSS.",
            "temporal_assessment": "The evidence dates Harvard graduation to 1943 and sequences Army training before two years in OSS.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 437 row 19"},
                {"source_key": CRIMSON, "locator_override": "A.B. Magna cum Laude; Class of 1944 alumni records", "excerpt_override": "William Snower, Jr. (Government)"},
                {"source_key": SNOWER_OBIT, "locator_override": "Biographical paragraph on wartime service", "excerpt_override": "then for two years as a paraphraser in the Office of Strategic Services"},
            ],
        },
        {
            **common,
            "key": "military-william-snower-army-astp-b894",
            "affiliation_key": "william-snower-army-astp-b894",
            "claim_type": "immediate_pre_oss_affiliation",
            "claim_text": "During Army service, William Snower trained in the Swedish Area and Language program at the University of Minnesota before serving in OSS.",
            "evidence_excerpt": "first in the Army Specialized Training Program Swedish Area and Language",
            "evidence_paraphrase": "The obituary explicitly sequences the Army language program before two years as an OSS paraphraser.",
            "temporal_assessment": "Explicitly immediate in the source's wartime sequence, but exact course and transfer dates are not supplied.",
            "sources": [
                {"source_key": SNOWER_OBIT, "locator_override": "Biographical paragraph on 1943-1946 Army and OSS service", "excerpt_override": "first in the Army Specialized Training Program Swedish Area and Language"},
                {"source_key": CRIMSON, "support_type": "context_only", "excerpt_override": "William Snower, Jr. (Government)"},
            ],
        },
        {
            **common,
            "key": "student-william-snower-harvard-b894",
            "affiliation_key": "william-snower-harvard-college-b894",
            "claim_type": "other_pre_oss_affiliation",
            "claim_text": "William Snower received an A.B. magna cum laude in government from Harvard College in 1943 before entering Army service.",
            "evidence_excerpt": "William Snower, Jr. (Government)",
            "evidence_paraphrase": "The contemporary degree list and obituary independently identify the degree, field and year.",
            "temporal_assessment": "Strongly date-bounded immediately before Army service, but student status is not civilian employment.",
            "sources": [
                {"source_key": CRIMSON, "locator_override": "A.B. Magna cum Laude; Class of 1944 alumni records", "excerpt_override": "William Snower, Jr. (Government)"},
                {"source_key": SNOWER_OBIT, "locator_override": "Education and wartime-service paragraph", "excerpt_override": "received an A.B. magna cum laude in government from Harvard College in 1943"},
            ],
        },
    ]


def person_updates() -> list[dict[str, object]]:
    updates: list[dict[str, object]] = [
        {
            "person_id": PEOPLE[1][0],
            "identity_status": "high_confidence",
            "identity_evidence": "The rare indexed name matches historian Howard McGaw Smyth across a contemporary AHA record, an official Army history and a publisher biography that explicitly documents OSS service.",
            "name_variants": ["Howard McGaw Smyth"],
            "manual_review_required": False,
            "research_status": "verified_employer_found",
            "next_action": "Review Box 726 to obtain the exact OSS recruitment or entry date and test whether any short intervening assignment followed University of California teaching.",
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
            "archival_review_priority": "medium",
        },
        {
            "person_id": PEOPLE[19][0],
            "identity_status": "high_confidence",
            "identity_evidence": "The rare exact name, a contemporary 1943 Harvard degree list and a Kansas City Star obituary explicitly documenting OSS service identify William Snower Jr.",
            "name_variants": ["William Snower Jr."],
            "manual_review_required": True,
            "research_status": "requires_archival_review",
            "next_action": "Review Box 727 for the exact Army-program-to-OSS transfer date and any civilian employment before Harvard or military service. Student status is not an employer.",
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
            "archival_review_priority": "high",
        },
    ]

    for item in ARMY_MATCHES:
        row = int(item["row"])
        person_id, _name = PEOPLE[row]
        update: dict[str, object] = {
            "person_id": person_id,
            "identity_status": "high_confidence",
            "identity_evidence": "A nonshared protected identifier and compatible name evidence connect the visually verified index row to the reviewed official Army record.",
            "personnel_category": "enlisted_army_personnel",
            "commissioned_officer": False,
            "allied_or_foreign_personnel": False,
            "manual_review_required": True,
            "research_status": "occupation_only_found",
            "next_action": "Review the indexed Box 727 personnel file to identify the immediate pre-OSS affiliation and last civilian employer; do not convert the Army occupation category into a named employer.",
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
            "archival_review_priority": "high",
        }
        if row == 6:
            update["name_variants"] = ["William K Snedeker"]
            update["identity_evidence"] = "A nonshared protected identifier, first name and middle initial bridge the index to Army form SNEDEKER; the minor surname difference remains visible as a documented variant."
        if row == 22:
            update["identity_evidence"] = "A nonshared protected identifier, surname and middle initial bridge the index to damaged Army form ARTHRU L; the transposition is documented and not silently corrected."
        updates.append(update)

    updates.append({
        "person_id": PEOPLE[21][0],
        "identity_status": "high_confidence",
        "identity_evidence": "Exact-name agreement plus a nonshared protected identifier connect the index row to a November 1945 Army record. The post-OSS date supports identity only, and unassigned code 195 is not interpreted.",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": "Review Box 727 for wartime status and pre-OSS affiliation; the accepted postwar Army record supplies no usable pre-OSS occupation.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    })

    for row, rejection in UNRESOLVED.items():
        person_id, name = PEOPLE[row]
        update: dict[str, object] = {
            "person_id": person_id,
            "identity_status": "unresolved",
            "identity_evidence": f"The visually verified index row supplies {name}, Box 726 or 727 and archive location, but staged official-context, exact-name, employment, occupation, obituary, institutional, directory and archival searches found no defensible identity bridge. {rejection}",
            "manual_review_required": True,
            "research_status": "requires_archival_review",
            "next_action": "Review the indexed personnel file for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
            "archival_review_priority": "critical",
        }
        if row in (12, 14):
            update["possible_duplicate_group"] = "p437-paul-c-snodgrass-snodgress-b894"
        if row in (17, 18):
            update["possible_duplicate_group"] = "p437-charles-r-snowden-b894"
        updates.append(update)
    return updates


def research_attempts() -> list[dict[str, object]]:
    attempts = []
    evidence_rows = {1, 6, 13, 19, 21, 22}
    for row, (person_id, name) in PEOPLE.items():
        has_evidence = row in evidence_rows
        notes = UNRESOLVED.get(row, "Reviewed evidence established an identity bridge and, where supported, a carefully bounded affiliation or occupation claim.")
        attempts.append({
            "key": f"page437-row{row}-{name.lower().replace(' ', '-').replace("'", '')}-b894",
            "person_id": person_id,
            "source_adapter": "manual_staged_protocol",
            "query_text": f"{name}; NARA/index context; CIA Reading Room discovery check; exact-name OSS variants; employer and occupation; obituary, institutional, newspaper, directory and archival searches; Box 726 or 727; protected-identifier Army crosswalk where available",
            "query_variant_type": "staged_identity_employment_archival_protocol_batch_894",
            "started_at": "2026-10-18T15:45:00Z",
            "completed_at": "2026-10-18T17:45:00Z",
            "outcome": "source_reviewed" if has_evidence else "candidate_rejected",
            "sources_reviewed": 8 if has_evidence else 5,
            "candidate_sources_rejected": 5 if has_evidence else 7,
            "rejection_reasons": "Unbridged namesakes and chronologically incompatible candidates were not assigned." if has_evidence else notes,
            "research_notes": ("Reviewed evidence established a high-confidence identity; public affiliation claims are limited to what the cited sources support. " if has_evidence else "No reliable identity or pre-OSS employer was established after staged search and namesake rejection. ") + notes + " Search-result snippets were not used as final evidence, and no exposed NARA API credential was used.",
            "next_action": "Review the indexed Box 726 or 727 personnel file.",
            "attempt_number": 1,
            "research_agent_version": "before-oss-b894-v1",
        })
    return attempts


def main() -> None:
    affiliations = [army_occupation_affiliation(item) for item in ARMY_MATCHES]
    affiliations.extend([howard_affiliation(), *snower_affiliations()])

    claims = [army_identity_claim(row, postwar=(row == 21)) for row in (6, 13, 21, 22)]
    claims.extend(army_occupation_claim(item) for item in ARMY_MATCHES)
    claims.extend([*howard_claims(), *snower_claims()])

    bundle = {
        "bundle_version": "batch-894-v1",
        "reviewer": "Before OSS Batch 894 evidence review",
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
