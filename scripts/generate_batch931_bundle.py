#!/usr/bin/env python3
"""Generate the reviewed Batch 931 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import uuid
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / (
    "research/evidence-page456-erwin-summers-to-stanley-sussman-"
    "review_batch-931_2026-10-27.json"
)

INDEX = "nara-index-b931"
ARMY_SOURCE = "army-bulk-b931"
TECH = "army-tech-b931"
CODES = "army-codes-b931"
UN_BIO = "un-ilc-biographical-statement-b931"
SIAM_REVIEW = "siam-society-review-b931"

PEOPLE = {
    1: ("4daa22b0-e89a-584f-9fdd-d6f0844ce444", "Erwin Summers", "758"),
    2: ("ea50bf7f-1db6-5a7c-a3d4-d995fa57cb38", "Homer B Summers", "758"),
    3: ("2df6b26f-bc5c-5425-b7eb-6eea2867abbd", "James Summers", "758"),
    4: ("d3903566-15af-5cb0-b5ab-12173aa55d82", "John W Summers", "758"),
    5: ("865a5f77-6cd7-53cd-8dbc-13d3f250c0d7", "John W Summers", "758"),
    6: ("35f0de37-8be4-52a9-897a-31b605d67dcc", "John B Summers", "758"),
    7: ("2a15173f-ca36-5c22-b8cd-71478bb2ee3e", "Edna J Sumner", "758"),
    8: ("4cdd937a-61a3-5c56-9d6f-35351acc2f81", "H Y Sun", "758"),
    9: ("30736fc0-734c-5937-9365-8f8e5bd4d109", "Robert G Sunday", "758"),
    10: ("2ccc5346-c6be-5483-902c-76e746d56d9a", "John Sunde", "758"),
    11: ("b1f9485b-168d-5690-adeb-05394faba3dd", "Jane Sunderland", "758"),
    12: ("49316a03-2fd8-5f57-a31f-eec022045a15", "Jeanne M Sunderland", "758"),
    13: ("af893820-db8e-5698-8228-4f385cce5203", "Ragnor N Sundstrom", "758"),
    14: ("b2fb9b93-9d75-5200-93c9-a6e034e5a076", "Edward S Sununu", "758"),
    15: ("4b65b46a-0828-5e7a-ba12-68b42aeb27b5", "Konthi Suphamonkol", "758"),
    16: ("96b42951-d1f0-551c-8efb-ba2d5c28c4f6", "Joan Supple", "758"),
    17: ("3f4b84e9-9d41-564d-adc6-d1f6e015496a", "Dorothy E Suratt", "758"),
    18: ("1a4c02a6-5f44-5ebd-9661-a3f511e2cbb3", "Sang P Surh", "758"),
    19: ("3bad49d2-d74d-5ddf-95cd-b5d687259a50", "Harold A Surle", "759"),
    20: ("afe4fe93-57d8-55aa-af8d-9e11aeeee672", "Julian C Suso", "759"),
    21: ("997be5df-41cb-5785-9204-6f44face8b6e", "Carl L Sussman", "759"),
    22: ("e1c0bc96-2d4b-5e13-a131-d4bec64fa6d3", "Harvey S Sussman", "759"),
    23: ("0661f296-5917-572d-abc3-c2673294b974", "Stanley Sussman", "759"),
}

ARMY = {
    2: {"entry": "1942-07-21", "code": "553", "occupation": "Linemen and servicemen, telegraph, telephone, and power", "locator": "PDF physical page 174; historical category 5-53", "variant": "Homer B Summers Jr"},
    3: {"entry": "1943-09-18", "code": "770", "occupation": "Firemen, other than process firemen", "locator": "PDF physical page 174; historical category 7-70", "variant": "James W Summers"},
    6: {"entry": "1943-07-06", "code": "001", "occupation": "Accountants and auditors", "locator": "PDF physical page 170; historical category 0-01"},
    9: {"entry": "1943-05-21", "code": "878", "occupation": "Machine-shop and related occupations, not elsewhere classified", "locator": "PDF physical page 174; historical category 8-78"},
    10: {"entry": "1942-09-07", "code": "893", "occupation": "Occupations in fabrication of metal products, not elsewhere classified", "locator": "PDF physical page 174; historical category 8-93"},
    21: {"entry": "1942-12-08", "code": "056", "occupation": "Photographers", "locator": "PDF physical page 171; historical category 0-56"},
    22: {"entry": "1943-02-09", "code": "097", "occupation": "Managers and officials, not elsewhere classified", "locator": "PDF physical page 171; historical category 0-97"},
}

UNRESOLVED = {
    1: "Exact-name searches produced no source tying an Erwin Summers namesake to OSS or Box 758.",
    7: "Exact-name and occupation searches produced no corroborated identity bridge for Edna J Sumner.",
    8: "The abbreviated indexed name is insufficient to distinguish H Y Sun from numerous namesakes.",
    11: "Common-name and institutional results did not provide two corroborating identifiers for Jane Sunderland.",
    12: "Exact-name and spelling-variant searches found no OSS or Box 758 bridge for Jeanne M Sunderland.",
    13: "Ragnor, Ragnar and Sundstrom variants produced no defensible person-specific OSS or employment source.",
    14: "A genealogical namesake lead lacked OSS, identifier and Box 758 evidence and was rejected.",
    16: "Exact-name and institutional searches produced only unrelated or modern namesakes for Joan Supple.",
    17: "Exact-name, obituary and archival searches found no person-specific bridge for Dorothy E Suratt.",
    19: "The printed identifier has no accepted Army bulk match, and exact-name searches did not establish the Box 759 person.",
    20: "The printed SI note is preserved but not expanded or treated as identity evidence; searches produced modern namesakes only.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def duplicate_group(key: str) -> str:
    return str(uuid.uuid5(uuid.NAMESPACE_URL, f"before-oss:{key}"))


JOHN_W_GROUP = duplicate_group("john-w-summers-page456-rows4-5")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 758-759",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 456, rows 1-23; checked against layout-preserving text and the rendered page image",
            "access_date": "2026-10-27",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. Full identifiers remain private. The box changes from 758 to 759 at row 19, and Julian C Suso's SI note is preserved without expansion.",
        },
        {
            "key": ARMY_SOURCE,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; nine reviewed Batch 931 identity candidates",
            "access_date": "2026-10-27",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "Seven nonshared, name-compatible identity bridges are accepted. Sang P Surh's identifier is shared with a different indexed name, and Stanley Sussman's Army name is damaged; both remain conflicts. No raw record or full identifier is public.",
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
            "locator": "PDF physical pages 170-171 and 174; Batch 931 categories visually checked",
            "access_date": "2026-10-27",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical categories identify neither employer nor workplace. Conflicting candidates are not assigned an occupation.",
        },
        {
            "key": UN_BIO,
            "stable_url": "https://digitallibrary.un.org/record/841304/files/A_4780-EN.pdf?version=1",
            "archival_identifier": "United Nations General Assembly document A/4780",
            "title": "Election of Members of the International Law Commission: Statements of Qualifications of Candidates",
            "author_creator": "United Nations Secretary-General",
            "repository_publisher": "United Nations Digital Library",
            "publication_record_date": "1961-06-28",
            "locator": "PDF physical page 61, printed page 61; Konthi Suphamongkhon statement visually checked",
            "access_date": "2026-10-27",
            "source_quality": "A_direct_official",
            "collection_name": "United Nations General Assembly, sixteenth session",
            "document_number": "A/4780",
            "rights_notes": "The official qualification statement supplies dated education, Foreign Ministry, embassy and university roles. It does not state an OSS entry date, so no immediate-predecessor claim is made.",
        },
        {
            "key": SIAM_REVIEW,
            "stable_url": "https://thesiamsociety.org/wp-content/uploads/1985/03/JSS_073_0s_Reviews.pdf",
            "archival_identifier": "Journal of the Siam Society, volume 73",
            "title": "Reviews: Thai Foreign Policy and Thai Foreign Policy 1932-1946",
            "author_creator": "S. Sivaraksa",
            "repository_publisher": "The Siam Society Under Royal Patronage",
            "publication_record_date": "1985",
            "locator": "PDF physical page 10, printed page 262; visually checked",
            "access_date": "2026-10-27",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Journal of the Siam Society",
            "rights_notes": "The review preserves the indexed Suphamonkol spelling and connects the author to Foreign Ministry work and the Free Thai Movement. It is used as corroboration, not to infer an OSS entry date.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": "siam-foreign-ministry-b931",
            "canonical_name": "Ministry of Foreign Affairs, Siam",
            "historical_name": "Ministry of Foreign Affairs",
            "aliases": ["Foreign Ministry", "Ministry of Foreign Affairs, Thailand"],
            "organization_type": "national foreign ministry",
            "sector": "federal_government",
            "city": "Bangkok",
            "country": "Siam (Thailand)",
            "active_dates": "Historical ministry; wartime name preserved",
            "normalization_notes": "The wartime country name and ministry wording are preserved. The modern successor name is listed only as an alias, not substituted for the historical affiliation.",
        },
        {
            "key": "thai-embassy-tokyo-b931",
            "canonical_name": "Embassy of Thailand, Tokyo",
            "historical_name": "Embassy of Thailand, Tokyo",
            "aliases": ["Thai Embassy in Tokyo"],
            "organization_type": "embassy",
            "sector": "federal_government",
            "city": "Tokyo",
            "country": "Japan",
            "active_dates": "Active during 1942-1944",
            "normalization_notes": "Kept separate from the Foreign Ministry headquarters role because the official biography names an embassy assignment. Its parent organization was the Ministry of Foreign Affairs, Siam.",
        },
        {
            "key": "moral-political-sciences-university-b931",
            "canonical_name": "University of Moral and Political Sciences",
            "historical_name": "University of Moral and Political Sciences",
            "aliases": ["University of Moral and Political Sciences, Bangkok"],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "Bangkok",
            "country": "Siam (Thailand)",
            "normalization_notes": "The historical institutional name in the UN statement is retained; its successor is Thammasat University. Student and lecturer relationships remain distinct, and neither is converted into an employer claim without separate evidence.",
        },
        {
            "key": "university-of-paris-b931",
            "canonical_name": "University of Paris",
            "historical_name": "University of Paris",
            "aliases": [],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "Paris",
            "country": "France",
            "active_dates": "Historical university before its 1970 reorganization",
            "normalization_notes": "The historical university is not silently merged with any modern successor campus. The relationship is student, not employment.",
        },
    ]


def affiliations() -> list[dict[str, object]]:
    result: list[dict[str, object]] = []
    for row, data in ARMY.items():
        result.append({
            "key": f"{slug(PEOPLE[row][1])}-occupation-b931",
            "person_id": PEOPLE[row][0],
            "occupation": data["occupation"],
            "relationship_type": "employment",
            "end_date": data["entry"],
            "date_precision": f"Historical civilian-occupation code {data['code']} was recorded at Army entry on {data['entry']}; no employer or workplace is named.",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "high_confidence",
            "claim_confidence": "medium",
            "source_quality": "A_direct_official",
            "publication_status": "publish_qualified",
            "research_notes": "The historical category is not converted into a named employer, workplace or exact job title.",
        })
    konthi = PEOPLE[15][0]
    result.extend([
        {
            "key": "konthi-umps-student-b931",
            "person_id": konthi,
            "organization_key": "moral-political-sciences-university-b931",
            "organization_name_as_found": "University of Moral and Political Sciences, Bangkok, Thailand",
            "role_title": "LL.B. student",
            "occupation": "student",
            "relationship_type": "student",
            "end_date": "1935",
            "date_precision": "Degree year; attendance start date not stated",
            "city": "Bangkok",
            "country": "Siam (Thailand)",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "A_direct_official",
            "publication_status": "published",
            "research_notes": "A student affiliation, not employment and not shown to be immediate before OSS-related service.",
        },
        {
            "key": "konthi-paris-student-b931",
            "person_id": konthi,
            "organization_key": "university-of-paris-b931",
            "organization_name_as_found": "University of Paris",
            "role_title": "Docteur en droit student",
            "occupation": "student",
            "relationship_type": "student",
            "end_date": "1940",
            "date_precision": "Degree year; attendance start date not stated",
            "city": "Paris",
            "country": "France",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "A_direct_official",
            "publication_status": "published",
            "research_notes": "A student affiliation, not employment and not shown to be immediate before OSS-related service.",
        },
        {
            "key": "konthi-foreign-ministry-1940-b931",
            "person_id": konthi,
            "organization_key": "siam-foreign-ministry-b931",
            "organization_name_as_found": "Political Division, Ministry of Foreign Affairs",
            "role_title": "Chief of Section, Political Division",
            "occupation": "diplomat",
            "relationship_type": "government_assignment",
            "start_date": "1940",
            "end_date": "1942",
            "date_precision": "Calendar-year range in the UN qualification statement; exact appointment dates are not stated",
            "city": "Bangkok",
            "country": "Siam (Thailand)",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "A_direct_official",
            "publication_status": "published",
            "research_notes": "A documented government assignment. The source does not establish an OSS entry date or prove that this was the immediate predecessor.",
        },
        {
            "key": "konthi-tokyo-embassy-b931",
            "person_id": konthi,
            "organization_key": "thai-embassy-tokyo-b931",
            "organization_name_as_found": "Embassy of Thailand, Tokyo",
            "role_title": "Second Secretary",
            "occupation": "diplomat",
            "relationship_type": "government_assignment",
            "start_date": "1942",
            "end_date": "1944",
            "date_precision": "Calendar-year range in the UN qualification statement; exact appointment dates are not stated",
            "city": "Tokyo",
            "country": "Japan",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "temporal_relation_uncertain",
            "identity_confidence": "high_confidence",
            "claim_confidence": "medium",
            "source_quality": "A_direct_official",
            "publication_status": "publish_qualified",
            "research_notes": "The assignment is documented, but its sequence or overlap with Free Thai and OSS-related activity is not fixed by the reviewed sources.",
        },
        {
            "key": "konthi-umps-lecturer-b931",
            "person_id": konthi,
            "organization_key": "moral-political-sciences-university-b931",
            "organization_name_as_found": "University of Moral and Political Sciences, Bangkok, Thailand",
            "role_title": "Lecturer on public finance",
            "occupation": "lecturer",
            "relationship_type": "employment",
            "start_date": "1944",
            "end_date": "1944",
            "date_precision": "Year only; the UN statement describes the lectureship as part-time",
            "city": "Bangkok",
            "country": "Siam (Thailand)",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "temporal_relation_uncertain",
            "identity_confidence": "high_confidence",
            "claim_confidence": "medium",
            "source_quality": "A_direct_official",
            "publication_status": "publish_qualified",
            "research_notes": "The part-time employment is documented for 1944, but the reviewed sources do not establish whether it preceded, overlapped or followed the relevant OSS relationship.",
        },
    ])
    return result


def army_identity_claim(row: int) -> dict[str, object]:
    name = PEOPLE[row][1]
    data = ARMY[row]
    variant = data.get("variant")
    variant_note = f" The Army spelling expands the name as {variant}." if variant else ""
    return {
        "key": f"identity-{slug(name)}-row{row}-b931",
        "person_id": PEOPLE[row][0],
        "claim_type": "identity",
        "claim_text": f"The indexed {name} row is a high-confidence match to an official Army record dated {data['entry']}.{variant_note}",
        "evidence_paraphrase": "The reviewed Army row agrees through a nonshared protected identifier and an exact or explicitly preserved name variant.",
        "identity_match_assessment": "High confidence from a nonshared protected identifier and compatible full name.",
        "temporal_assessment": f"The Army record documents entry on {data['entry']}; it does not establish the OSS transfer date.",
        "source_quality": "A_direct_official",
        "claim_confidence": "high",
        "publication_status": "published",
        "match_notes": "The protected identifier is withheld from public data; no employer is inferred from the Army row.",
        "sources": [
            {"source_key": INDEX, "locator_override": f"PDF page 456 row {row}; Box {PEOPLE[row][2]}"},
            {"source_key": ARMY_SOURCE, "locator_override": f"Accepted reviewed identity record; Army entry {data['entry']}; protected identifier withheld"},
            {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46; field definitions"},
        ],
    }


def army_occupation_claim(row: int) -> dict[str, object]:
    name = PEOPLE[row][1]
    data = ARMY[row]
    return {
        "key": f"occupation-{slug(name)}-row{row}-b931",
        "person_id": PEOPLE[row][0],
        "affiliation_key": f"{slug(name)}-occupation-b931",
        "claim_type": "occupation",
        "claim_text": f"At Army entry on {data['entry']}, {name} was recorded in the historical occupation category {data['occupation']}; no employer or workplace is identified.",
        "evidence_excerpt": data["occupation"],
        "evidence_paraphrase": f"The accepted Army record carries civilian-occupation code {data['code']}, decoded from NARA's official code list.",
        "identity_match_assessment": "The occupation is assigned only to the accepted protected-identifier match; the identifier itself is not public.",
        "temporal_assessment": "Strongly date-bounded to Army entry, but not proven to be the immediate pre-OSS affiliation.",
        "source_quality": "A_direct_official",
        "claim_confidence": "medium",
        "publication_status": "publish_qualified",
        "match_notes": "Historical occupation language is preserved and is not converted into a company, workplace or exact job title.",
        "sources": [
            {"source_key": ARMY_SOURCE, "locator_override": f"Army entry {data['entry']}; civilian-occupation code {data['code']}; protected identifier withheld"},
            {"source_key": CODES, "locator_override": data["locator"]},
        ],
    }


def konthi_claims() -> list[dict[str, object]]:
    person_id = PEOPLE[15][0]
    items = [
        ("student-umps", "konthi-umps-student-b931", "Konthi Suphamongkhon earned an LL.B. from the University of Moral and Political Sciences in 1935.", "LL.B. University of Moral and Political Sciences", "Documented prewar student affiliation; not employment or an immediate predecessor to OSS-related activity.", "high", "published"),
        ("student-paris", "konthi-paris-student-b931", "Konthi Suphamongkhon earned a doctorate in law from the University of Paris in 1940.", "Docteur en droit, University of Paris, 1940", "Documented prewar student affiliation; not employment or an immediate predecessor to OSS-related activity.", "high", "published"),
        ("foreign-ministry", "konthi-foreign-ministry-1940-b931", "Konthi Suphamongkhon served as Chief of Section in the Political Division of Siam's Ministry of Foreign Affairs from 1940 to 1942.", "Chief of Section, Political Division", "Documented prewar government assignment; the reviewed sources do not establish an exact OSS entry date.", "high", "published"),
        ("tokyo-embassy", "konthi-tokyo-embassy-b931", "Konthi Suphamongkhon served as Second Secretary at the Embassy of Thailand in Tokyo from 1942 to 1944.", "Second Secretary, Embassy of Thailand, Tokyo", "Documented wartime assignment with uncertain sequence or overlap relative to Free Thai and OSS-related activity.", "medium", "publish_qualified"),
        ("lecturer", "konthi-umps-lecturer-b931", "Konthi Suphamongkhon held a part-time public-finance lectureship at the University of Moral and Political Sciences in 1944.", "Lecturer on public finance", "Documented 1944 employment; its exact sequence relative to OSS-related activity remains uncertain.", "medium", "publish_qualified"),
    ]
    result = [{
        "key": "identity-konthi-suphamonkol-b931",
        "person_id": person_id,
        "claim_type": "identity",
        "claim_text": "The indexed Konthi Suphamonkol is a high-confidence match to Thai diplomat Konthi Suphamongkhon.",
        "evidence_excerpt": "His own involvement in the Free Thai Movement",
        "evidence_paraphrase": "The Siam Society review uses the indexed surname spelling and describes his Foreign Ministry and Free Thai experience; the UN statement supplies the corresponding alternate spelling and dated career.",
        "identity_match_assessment": "High confidence from the exceptionally distinctive given name and near-identical surname spellings, matched profession, wartime chronology and Free Thai context across independent institutional sources.",
        "temporal_assessment": "The sources document 1935-1944 education and assignments but do not supply an OSS entry date.",
        "source_quality": "A_direct_official",
        "claim_confidence": "high",
        "publication_status": "published",
        "match_notes": "The Suphamongkhon spelling is preserved as a documented variant rather than silently replacing the index form.",
        "sources": [
            {"source_key": INDEX, "locator_override": "PDF page 456 row 15; Box 758"},
            {"source_key": UN_BIO, "locator_override": "PDF physical and printed page 61"},
            {"source_key": SIAM_REVIEW, "locator_override": "PDF physical page 10, printed page 262"},
        ],
    }]
    for suffix, affiliation_key, text, excerpt, temporal, confidence, publication in items:
        result.append({
            "key": f"other-konthi-{suffix}-b931",
            "person_id": person_id,
            "affiliation_key": affiliation_key,
            "claim_type": "other_pre_oss_affiliation",
            "claim_text": text,
            "evidence_excerpt": excerpt,
            "evidence_paraphrase": "The United Nations qualification statement lists the institution, role or degree and the stated year or year range.",
            "identity_match_assessment": "High confidence from the rare-name bridge and corroborating Free Thai and diplomatic context.",
            "temporal_assessment": temporal,
            "source_quality": "A_direct_official",
            "claim_confidence": confidence,
            "publication_status": publication,
            "match_notes": "Published as an earlier or temporally qualified affiliation only. It is not labeled immediate, and no last civilian employer is inferred.",
            "sources": [{"source_key": UN_BIO, "locator_override": "PDF physical and printed page 61; visually checked"}],
        })
    return result


def claims() -> list[dict[str, object]]:
    result: list[dict[str, object]] = []
    for row in ARMY:
        result.extend([army_identity_claim(row), army_occupation_claim(row)])
    result.extend([
        {
            "key": "conflict-sang-p-surh-army-b931",
            "person_id": PEOPLE[18][0],
            "claim_type": "identity",
            "claim_text": "An Army record names Sang P Surh and agrees with the index, but its protected identifier is also printed for a different indexed person; the identity bridge remains conflicting.",
            "evidence_paraphrase": "The Army name agrees, but the same protected identifier appears in the index for Sang P Surh and Charles M Joe.",
            "identity_match_assessment": "Conflicting. Name agreement cannot overcome the shared-identifier collision between two differently named source rows.",
            "temporal_assessment": "The Army record is dated 1945-02-15, but neither identity nor the occupation field is accepted while the conflict remains unresolved.",
            "source_quality": "A_direct_official",
            "claim_confidence": "conflicting",
            "publication_status": "conflicting",
            "match_notes": "The identifier is not reproduced. Both people remain separate and require joint file and original-index review.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 456 row 18 and separate Charles M Joe row; protected identifier withheld"},
                {"source_key": ARMY_SOURCE, "locator_override": "Conflicting reviewed candidate; protected identifier withheld"},
            ],
        },
        {
            "key": "conflict-stanley-sussman-army-b931",
            "person_id": PEOPLE[23][0],
            "claim_type": "identity",
            "claim_text": "Stanley Sussman's nonshared protected identifier points to an Army row whose damaged name does not agree; the identity and occupation remain unassigned.",
            "evidence_paraphrase": "The protected value agrees, but the Army name field is damaged and cannot be reconciled safely with Stanley Sussman from the accessible record.",
            "identity_match_assessment": "Conflicting. A protected-identifier agreement is strong, but the substantive name-field damage requires manual source review before acceptance.",
            "temporal_assessment": "The candidate is dated 1942-09-20. No occupation or employer is published from the unresolved row.",
            "source_quality": "A_direct_official",
            "claim_confidence": "conflicting",
            "publication_status": "conflicting",
            "match_notes": "The protected identifier and damaged raw name are not exposed. Box 759 and original bulk-record review are required.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 456 row 23; Box 759; protected identifier withheld"},
                {"source_key": ARMY_SOURCE, "locator_override": "Conflicting name-field candidate dated 1942-09-20; protected identifier withheld"},
            ],
        },
    ])
    result.extend(konthi_claims())
    return result


def archival_update(row: int, reason: str, *, priority: str = "high") -> dict[str, object]:
    person_id, name, box = PEOPLE[row]
    return {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, Box {box} and archive location, but staged official-register, CIA-site, OSS, employment, occupation, obituary, institutional, newspaper, Library of Congress and archival searches found no defensible identity bridge. {reason}",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": f"Review Box {box} for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": priority,
    }


def person_updates() -> list[dict[str, object]]:
    updates = [archival_update(row, reason) for row, reason in UNRESOLVED.items()]
    for row, data in ARMY.items():
        variants = [data["variant"]] if data.get("variant") else None
        update: dict[str, object] = {
            "person_id": PEOPLE[row][0],
            "identity_status": "high_confidence",
            "identity_evidence": "An exact or compatible full name and nonshared protected identifier connect the visually verified index row to the reviewed official Army record. The occupation field remains separate from employer and immediate-affiliation claims.",
            "personnel_category": "enlisted_army_personnel",
            "commissioned_officer": False,
            "allied_or_foreign_personnel": False,
            "manual_review_required": True,
            "research_status": "occupation_only_found",
            "next_action": f"Review Box {PEOPLE[row][2]} for the immediate pre-OSS affiliation and a named employer or institution.",
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
            "archival_review_priority": "high",
        }
        if variants:
            update["name_variants"] = variants
        updates.append(update)
    updates.extend([
        {
            **archival_update(4, "Two separately printed John W Summers rows share Box 758 but differ because only the second row carries a protected identifier.", priority="critical"),
            "identity_status": "ambiguous",
            "identity_evidence": "Two separately printed John W Summers rows share Box 758, but only the second has a protected identifier. Name and adjacency alone cannot establish duplication.",
            "possible_duplicate_group": JOHN_W_GROUP,
            "next_action": "Review both Box 758 John W Summers files together for identifiers, cross-references and duplicate-file evidence before merging or assigning any common-name biography.",
        },
        {
            **archival_update(5, "Two separately printed John W Summers rows share Box 758; the second row's protected identifier has no accepted Army bulk match.", priority="critical"),
            "identity_status": "ambiguous",
            "identity_evidence": "Two separately printed John W Summers rows share Box 758, but only this row has a protected identifier. No accepted external match establishes whether they are duplicates.",
            "possible_duplicate_group": JOHN_W_GROUP,
            "next_action": "Review both Box 758 John W Summers files together for identifiers, cross-references and duplicate-file evidence before merging or assigning any common-name biography.",
        },
        {
            "person_id": PEOPLE[15][0],
            "identity_status": "high_confidence",
            "identity_evidence": "The exceptionally distinctive indexed Konthi Suphamonkol aligns with Konthi Suphamongkhon through near-identical spellings, a dated official diplomatic biography and an independent Siam Society review describing his Foreign Ministry and Free Thai experience.",
            "name_variants": ["Konthi Suphamongkhon", "Konthi Souphamongkon", "Konthī Suphamongkhon"],
            "personnel_category": "unknown_or_indeterminate",
            "allied_or_foreign_personnel": True,
            "manual_review_required": True,
            "research_status": "requires_archival_review",
            "next_action": "Review Box 758 and the Thai-language memoir to establish the exact Free Thai/OSS chronology and determine which documented assignment, if any, immediately preceded the indexed relationship.",
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
            "archival_review_priority": "high",
        },
        {
            "person_id": PEOPLE[18][0],
            "identity_status": "conflicting",
            "identity_evidence": "An official Army row prints the exact Sang P Surh name, but the protected identifier is shared by a separate index row named Charles M Joe. The Army identity and occupation are not accepted while the collision remains unresolved.",
            "manual_review_required": True,
            "research_status": "conflicting_sources",
            "next_action": "Review both personnel files and the original index and Army source records together; do not assign the Army occupation to either person until the shared-identifier conflict is resolved.",
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
            "archival_review_priority": "critical",
        },
        {
            "person_id": PEOPLE[23][0],
            "identity_status": "conflicting",
            "identity_evidence": "A nonshared protected identifier points to an official Army row, but that row's name field is substantively damaged and does not safely resolve to Stanley Sussman. The identity and occupation remain unaccepted.",
            "manual_review_required": True,
            "research_status": "conflicting_sources",
            "next_action": "Review Box 759 and the original Army bulk record before accepting the identity or interpreting occupation code 992.",
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
            "archival_review_priority": "critical",
        },
    ])
    return updates


def research_attempts() -> list[dict[str, object]]:
    attempts: list[dict[str, object]] = []
    for row in sorted(PEOPLE):
        person_id, name, box = PEOPLE[row]
        if row in ARMY:
            outcome, reviewed, rejected = "source_reviewed", 8, 3
            detail = "A nonshared protected identifier and compatible name support a high-confidence official Army identity bridge. The dated occupation category names no employer or workplace."
        elif row == 15:
            outcome, reviewed, rejected = "source_reviewed", 12, 4
            detail = "An official UN biographical statement and independent Siam Society review establish a high-confidence identity, two educational affiliations, Foreign Ministry and Tokyo embassy assignments, and a 1944 part-time lectureship; the immediate OSS chronology remains unresolved."
        elif row in {4, 5}:
            outcome, reviewed, rejected = "candidate_found", 7, 5
            detail = "Two separately printed John W Summers rows remain distinct because only one carries an identifier and no source proves duplication."
        elif row == 18:
            outcome, reviewed, rejected = "source_reviewed", 9, 5
            detail = "The Army name agrees, but the protected identifier is shared with Charles M Joe; the candidate and occupation remain conflicting."
        elif row == 23:
            outcome, reviewed, rejected = "source_reviewed", 8, 4
            detail = "The protected identifier is nonshared, but substantive name-field damage prevents acceptance of the Army identity or occupation."
        else:
            outcome, reviewed, rejected = "no_result", 6, 4
            detail = UNRESOLVED[row]
        attempts.append({
            "key": f"page456-row{row}-{slug(name)}-b931",
            "person_id": person_id,
            "source_adapter": "manual_staged_protocol",
            "query_text": f"{name}; NARA index and public Archives context; 1943 Official Register; CIA Reading Room site-restricted exact-name discovery; OSS and spelling variants; employer and occupation 1940; obituary, institutional, newspaper, Library of Congress and archival searches; Box {box}; protected-identifier Army crosswalk where defensible",
            "query_variant_type": "staged_identity_employment_archival_protocol_batch_931",
            "started_at": "2026-10-28T00:55:00Z",
            "completed_at": "2026-10-28T01:35:00Z",
            "outcome": outcome,
            "sources_reviewed": reviewed,
            "candidate_sources_rejected": rejected,
            "rejection_reasons": "Unbridged namesakes, search snippets, genealogy-only assertions, modern profiles, postwar-only leads and sources without an OSS or Box-file bridge were not assigned. Grouped CIA Reading Room exact-name checks returned no person-specific pre-OSS result; Library of Congress checks added only a postwar Konthi spelling lead and unrelated namesakes.",
            "research_notes": f"{detail} The index, UN biography, Siam Society review and relevant Army code-list pages were visually checked where applicable. The 1943 Official Register contains no exact-name Batch 931 hit. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA API call was made.",
            "next_action": f"Review Box {box} for corroborating identifiers and the immediate pre-OSS affiliation or last civilian employer.",
            "attempt_number": 1,
            "research_agent_version": "before-oss-b931-v1",
        })
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-931-v1",
        "reviewer": "Before OSS Batch 931 evidence review",
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
