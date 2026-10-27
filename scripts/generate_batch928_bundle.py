#!/usr/bin/env python3
"""Generate the reviewed Batch 928 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import uuid
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / (
    "research/evidence-page454-donald-b-sturtevant-to-pearl-e-sugerman-"
    "review_batch-928_2026-10-27.json"
)

INDEX = "nara-index-b928"
ARMY = "army-bulk-b928"
TECH = "army-tech-b928"
CODES = "army-codes-b928"
STYMA_CITATION = "nara-styma-citation-b928"
ADST = "adst-styma-b928"
STYMFAL_ROSTER = "elia-stymfal-b928"
UCLA = "ucla-kay-sugahara-b928"
ARLINGTON = "arlington-kay-sugahara-b928"

PEOPLE = {
    24: ("05f86065-b7d2-59da-a5df-e5585608b028", "Donald B Sturtevant", "755"),
    25: ("87a79df2-11c7-5a7a-b694-c3ce1e6b6f49", "Warren B Sturtevant", "755"),
    26: ("90d1c4fb-99b4-54b6-b0a6-1f348a055535", "Warren Stutler", "756"),
    27: ("04f65c85-7d87-513c-ae7d-91942da15d9c", "Carl A Stutz", "756"),
    28: ("bd4e5dd6-6147-54e2-a7f3-a10f9bc086fd", "Sherwood S Stutz", "756"),
    29: ("e2e0804f-ed19-57d7-a501-39422a01e10a", "Duane H Stutzman", "756"),
    30: ("b45dfb7f-0ee5-5197-9577-89ade3f34693", "Alan R Stuyvesant", "756"),
    31: ("b1065589-d21a-50cb-ade6-ff326413ff71", "John H Styer", "756"),
    32: ("26f6008b-fb70-500b-89b3-0a51aa7e9cf6", "Mitchell Styma", "756"),
    33: ("39a5e6cf-0a32-5641-b2df-4c895e8ef402", "Peter A Stymfal", "756"),
    34: ("8d36048e-55b5-54fb-8a1f-9f04f64a1583", "Lauritz E Styve", "756"),
    35: ("8bb20ea2-0b9f-5b23-9bf3-2823930fcb1e", "Ju Sung Su", "756"),
    36: ("c9aa82ba-73de-5616-8645-4df4c4f39a2e", "Alfred M Suarez", "756"),
    37: ("b3b31bb1-f477-5a28-96eb-1d69a1df1201", "Robert Suarez", "756"),
    38: ("ade8798b-d25b-57f6-b47c-49c026f0ed97", "Nicholas M Suban", "756"),
    39: ("936f8c8c-5b71-5892-b0e3-964fe595412b", "Sukontha B Subhats", "756"),
    40: ("395cf2ec-41c3-516e-989b-6a49e983543c", "Vivian B. Suchards", "756"),
    41: ("670c1d13-5f3f-5cf5-a261-9de3acb32552", "Carlos V Sucre", "756"),
    42: ("5a43db91-5b7d-513e-b8a2-5df17c517288", "Piscot Sudasna", "756"),
    43: ("0b2bf8f8-0fd8-51f8-8723-aa2c6b37111a", "Kay K Sugahara", "756"),
    44: ("630c03c4-c927-5520-986c-07339921cf4d", "Kelichi K Sugahara", "756"),
    45: ("c4cad75d-0f5e-5d9a-9898-879ded80aad3", "Tomio Sugano", "756"),
    46: ("1a4e3c57-6db8-504c-aad9-e93363f1925b", "Pearl E Sugerman", "756"),
}

ARMY_IDENTITIES = {
    27: {"entry": "1943-06-12", "grade": "PVT", "undefined_code": "047"},
    32: {"entry": "1942-01-06", "grade": "PVT"},
    33: {"entry": "1943-05-24", "grade": "PVT"},
    41: {"entry": "1943-05-17", "grade": "PVT", "variant": "Carlos U Sucre"},
}

ARMY_OCCUPATIONS = {
    32: ("678", "Machine shop and related occupations, n.e.c.", "employment", "PDF physical page 174; historical category 6-78"),
    33: ("992", "Students", "student", "PDF physical page 304; amended historical category 9-92"),
    41: ("073", "Wholesale managers", "employment", "PDF physical page 171; historical category 0-73"),
}

UNRESOLVED = {
    24: "Exact-name and middle-initial searches found no person-specific OSS identity bridge or reliable pre-OSS affiliation.",
    25: "Exact-name searches returned unrelated historical namesakes and no Box 755 or OSS bridge.",
    26: "A 1950 CIA daily-log result and a Warren H. Stutler military lead are postwar or insufficiently identified and were not assigned.",
    28: "Exact-name and middle-initial searches found no corroborating identifier or reliable pre-OSS affiliation.",
    29: "A 1940 census lead lacks a protected identifier, Box 756 reference or OSS link and was not assigned.",
    30: "A namesake in a memorial-dog record supplies no OSS or prewar-employment bridge and was rejected.",
    31: "Banking and obituary namesakes lack the protected identifier and OSS linkage needed for this common-name case.",
    34: "Exact-name searches found only unverified genealogy leads and no defensible OSS or employment bridge.",
    35: "Transliteration-sensitive searches found no source with corroborating identifiers or a reliable pre-OSS affiliation.",
    36: "Common-name searches produced multiple namesakes and no two-identifier bridge to the Box 756 person.",
    37: "Common-name searches produced multiple namesakes and no two-identifier bridge to the Box 756 person.",
    38: "Exact-name searches found no person-specific source tied to OSS, Box 756 or a pre-OSS affiliation.",
    39: "Name and transliteration variants produced no reliable OSS identity bridge or pre-OSS affiliation.",
    40: "Exact-name and punctuation-variant searches found no corroborating identifier or reliable affiliation.",
    42: "A much later international-industry record is postwar and does not identify the Box 756 person or a pre-OSS affiliation.",
    45: "Wartime relocation records name a Tomio Sugano, but no reviewed source links that person to the Box 756 file or OSS service.",
    46: "Exact-name and middle-initial searches found no reliable identity bridge or pre-OSS affiliation.",
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
            "archival_identifier": "RG 226, Entry A1-224, Boxes 755-756",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 454, rows 24-46; checked against layout-preserving text and the rendered page image",
            "access_date": "2026-10-27",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. Full identifiers remain private. Kay and Kelichi Sugahara are linked for review but not merged.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; four accepted Batch 928 protected-identifier candidates",
            "access_date": "2026-10-27",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "No raw record or full protected identifier is retained in public assets. Code 047 remains uninterpreted; other coded occupations name neither employer nor workplace.",
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
            "locator": "PDF physical pages 171, 174 and 304; Batch 928 categories visually checked",
            "access_date": "2026-10-27",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical categories identify neither employer nor workplace. Code 047 is absent from the reviewed list and remains uninterpreted.",
        },
        {
            "key": STYMA_CITATION,
            "stable_url": "https://www.archives.gov/files/research/jfk/releases/104-10165-10120.pdf",
            "archival_identifier": "104-10165-10120",
            "title": "OSS citations and related records (file 104-10165-10120)",
            "author_creator": "Office of Strategic Services",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "World War II; released 2017",
            "locator": "PDF physical page 81; internal restricted page 3; Tec 3 Mitchell Styma citation",
            "access_date": "2026-10-27",
            "source_quality": "A_direct_official",
            "collection_name": "John F. Kennedy Assassination Records Collection",
            "document_number": "104-10165-10120",
            "rights_notes": "The citation prints the same protected identifier as the index. Public excerpts and notes omit that value.",
        },
        {
            "key": ADST,
            "stable_url": "https://adst.org/Readers/Yugoslavia-1.pdf",
            "title": "Yugoslavia Country Reader",
            "author_creator": "Joseph Walter Neubert; Association for Diplomatic Studies and Training",
            "repository_publisher": "Association for Diplomatic Studies and Training",
            "publication_record_date": "Neubert self-interview, 2007",
            "locator": "PDF physical page 26, internal page 26; Joseph Walter Neubert self-interview",
            "access_date": "2026-10-27",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Foreign Affairs Oral History Collection country readers",
            "rights_notes": "The account names no employer or sponsoring organization for the prewar courier runs.",
        },
        {
            "key": STYMFAL_ROSTER,
            "stable_url": "https://www.elia.org.gr/userfiles/pdf_archieve/1945%201-1845%20OSS%20Base,%20OSS%20Agents,%20%5B7%20pgs%5D%20226-211%20WN22856%20(Admin).pdf",
            "archival_identifier": "226-211 WN22856; memorandum 600/3",
            "title": "Athens personnel list of 1 January 1945",
            "author_creator": "Lewis Leary, Chief, SI, Office of Strategic Services, Cairo",
            "repository_publisher": "Hellenic Literary and Historical Archive (ELIA-MIET)",
            "publication_record_date": "1945-01-18",
            "locator": "PDF physical page 7; personnel transferred or discharged from Athens office",
            "access_date": "2026-10-27",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "OSS Base and OSS Agents records",
            "document_number": "226-211 WN22856",
            "rights_notes": "The wartime roster identifies Peter A. Stymfal as a Pfc. operative in Greece and records return to Cairo; it supplies no pre-OSS employer.",
        },
        {
            "key": UCLA,
            "stable_url": "https://learn.aasc.ucla.edu/sugahara/about/",
            "title": "About – Sugahara Project",
            "author_creator": "UCLA Asian American Studies Center",
            "repository_publisher": "UCLA Asian American Studies Center",
            "publication_record_date": "Page copyright 2022; note based on 1982 profile and 1988 curriculum vitae",
            "locator": "Kay Keiichi Sugahara biographical note, paragraphs 1-4",
            "access_date": "2026-10-27",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Sugahara Project",
            "rights_notes": "The note distinguishes the 1932 customs-brokerage firm, forced removal and 1942 OSS service. Postwar oil activity is not treated as pre-OSS employment.",
        },
        {
            "key": ARLINGTON,
            "stable_url": "https://www.arlingtoncemetery.mil/Explore/Notable-Graves/Minorities/Japanese-American-Service-Members",
            "title": "Japanese-American Service Members",
            "author_creator": "Arlington National Cemetery",
            "repository_publisher": "Office of Army Cemeteries, United States Army",
            "publication_record_date": "Page accessed 2026",
            "locator": "Columbarium table, I-15-3: Sugahara, Kay K.; served: OSS",
            "access_date": "2026-10-27",
            "source_quality": "A_direct_official",
            "collection_name": "Arlington National Cemetery notable graves",
            "rights_notes": "Official exact-name OSS corroboration. The page does not document prewar employment.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [{
        "key": "universal-foreign-service-company-b928",
        "canonical_name": "Universal Foreign Service Company",
        "historical_name": "Universal Foreign Service Company",
        "aliases": [],
        "organization_type": "customs brokerage",
        "sector": "business_and_industry",
        "city": "Los Angeles",
        "state_or_region": "California",
        "country": "United States",
        "active_dates": "Founded after Kay Sugahara's 1932 UCLA graduation; later history not established in the reviewed sources",
        "normalization_notes": "Historical name preserved. No successor, merger or modern equivalent is inferred.",
    }]


def affiliations() -> list[dict[str, object]]:
    result: list[dict[str, object]] = []
    for row, (code, occupation, relationship, _locator) in ARMY_OCCUPATIONS.items():
        result.append({
            "key": f"{slug(PEOPLE[row][1])}-occupation-b928",
            "person_id": PEOPLE[row][0],
            "occupation": occupation,
            "relationship_type": relationship,
            "end_date": ARMY_IDENTITIES[row]["entry"],
            "date_precision": f"Historical civilian-occupation code {code} was recorded at Army entry on {ARMY_IDENTITIES[row]['entry']}; no employer, school, workplace or OSS-transfer date is named.",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "confirmed" if row == 32 else "high_confidence",
            "claim_confidence": "medium",
            "source_quality": "A_direct_official",
            "publication_status": "publish_qualified",
            "research_notes": "The historical category is not converted into a named employer, school, institution, workplace or exact job title.",
        })
    result.extend([
        {
            "key": "mitchell-styma-courier-b928",
            "person_id": PEOPLE[32][0],
            "role_title": "courier",
            "occupation": "courier",
            "relationship_type": "unknown",
            "end_date": "1939",
            "date_precision": "A 2007 oral-history recollection says he made courier runs to Lisbon until the fall of Poland; no employer, sponsoring organization, start date or precise end date is named.",
            "country": "Portugal",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "confirmed",
            "claim_confidence": "medium",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "publish_qualified",
            "research_notes": "Documented prewar activity, not a named employer and not established as the immediate predecessor to OSS service.",
        },
        {
            "key": "kay-sugahara-universal-foreign-service-b928",
            "person_id": PEOPLE[43][0],
            "organization_key": "universal-foreign-service-company-b928",
            "organization_name_as_found": "Universal Foreign Service Company",
            "role_title": "founder and owner",
            "occupation": "customs broker",
            "relationship_type": "self_employment",
            "start_date": "1932",
            "end_date": "1942",
            "date_precision": "The UCLA note says he opened the firm after graduating in 1932, then separately describes forced removal and joining OSS in 1942; the exact separation date is not stated.",
            "city": "Los Angeles",
            "state_or_region": "California",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": True,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "published",
            "research_notes": "Last documented civilian enterprise before wartime displacement and OSS service. The intervening forced removal means the firm is not labeled the immediate pre-OSS affiliation.",
        },
    ])
    return result


def army_identity_claim(row: int) -> dict[str, object]:
    name = PEOPLE[row][1]
    data = ARMY_IDENTITIES[row]
    assessment = "High confidence from the exact full name and a nonshared protected identifier."
    if row == 32:
        assessment = "Confirmed by the exact name, a nonshared protected identifier and a NARA OSS citation carrying the same protected value."
    elif row == 41:
        assessment = "High confidence from the nonshared protected identifier; the Carlos V/Carlos U middle-initial disagreement remains visible as a variant."
    links: list[dict[str, object]] = [
        {"source_key": INDEX, "locator_override": f"PDF page 454 row {row}; Box {PEOPLE[row][2]}"},
        {"source_key": ARMY, "locator_override": f"Accepted reviewed identity record; Army entry {data['entry']}; protected identifier withheld"},
        {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46; field definitions"},
    ]
    if row == 32:
        links.append({"source_key": STYMA_CITATION, "locator_override": "PDF physical page 81; internal restricted page 3; protected identifier withheld"})
    elif row == 33:
        links.append({"source_key": STYMFAL_ROSTER, "locator_override": "PDF physical page 7; Peter A. Stymfal, Pfc., operative, Greece"})
    note = "The protected identifier is withheld from public data; no employer is inferred from the Army row."
    if row == 27:
        note += " Occupation code 047 remains uninterpreted because it is absent from the reviewed official code list."
    return {
        "key": f"identity-{slug(name)}-row{row}-b928",
        "person_id": PEOPLE[row][0],
        "claim_type": "identity",
        "claim_text": f"The indexed {name} row is a {'confirmed' if row == 32 else 'high-confidence'} match to an official Army record dated {data['entry']}.",
        "evidence_paraphrase": "The reviewed Army row agrees through a nonshared protected identifier and an exact or explicitly preserved name variant.",
        "identity_match_assessment": assessment,
        "temporal_assessment": f"The Army record documents entry on {data['entry']}; it does not by itself establish the OSS transfer date.",
        "source_quality": "A_direct_official",
        "claim_confidence": "confirmed" if row == 32 else "high",
        "publication_status": "published",
        "match_notes": note,
        "sources": links,
    }


def army_occupation_claim(row: int) -> dict[str, object]:
    code, occupation, _relationship, locator = ARMY_OCCUPATIONS[row]
    name = PEOPLE[row][1]
    text = f"At Army entry on {ARMY_IDENTITIES[row]['entry']}, {name} was recorded in the historical occupation category {occupation}; no employer is identified."
    if occupation == "Students":
        text = f"At Army entry on {ARMY_IDENTITIES[row]['entry']}, {name} was recorded in the historical occupation group Students; no school or employer is identified."
    return {
        "key": f"occupation-{slug(name)}-b928",
        "person_id": PEOPLE[row][0],
        "affiliation_key": f"{slug(name)}-occupation-b928",
        "claim_type": "occupation",
        "claim_text": text,
        "evidence_excerpt": occupation,
        "evidence_paraphrase": f"The accepted Army record carries civilian-occupation code {code}, decoded from NARA's official code list.",
        "identity_match_assessment": "The category belongs only to the reviewed protected-identifier match; the identifier itself is not public.",
        "temporal_assessment": "Dated to Army entry; it does not establish an immediate pre-OSS affiliation or named employer.",
        "source_quality": "A_direct_official",
        "claim_confidence": "medium",
        "publication_status": "publish_qualified",
        "match_notes": "The historical category is a qualified lead, not a named employer, school, institution, workplace or exact title.",
        "sources": [
            {"source_key": ARMY, "locator_override": f"Accepted reviewed identity record; civilian occupation code {code}; protected identifier withheld"},
            {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46; Army-entry-date and civilian-occupation fields"},
            {"source_key": CODES, "locator_override": locator, "excerpt_override": occupation},
        ],
    }


def claims() -> list[dict[str, object]]:
    result = [army_identity_claim(row) for row in ARMY_IDENTITIES]
    result.extend(army_occupation_claim(row) for row in ARMY_OCCUPATIONS)
    result.extend([
        {
            "key": "prewar-courier-mitchell-styma-b928",
            "person_id": PEOPLE[32][0],
            "affiliation_key": "mitchell-styma-courier-b928",
            "claim_type": "other_pre_oss_affiliation",
            "claim_text": "Mitchell Styma performed courier runs to Lisbon before returning to the United States and later serving in OSS; the employer or sponsoring organization is not named.",
            "evidence_excerpt": "did courier runs to Lisbon until the fall of Poland. Then he returned to the U.S. and served in the OSS",
            "evidence_paraphrase": "Joseph Walter Neubert's oral-history account places Styma's courier activity before his return to the United States and subsequent OSS service.",
            "identity_match_assessment": "Confirmed by the NARA OSS citation and protected-identifier bridge; the oral history adds birthplace, Polish education and OSS details.",
            "temporal_assessment": "Explicitly pre-OSS, but not shown to be immediately prior; the fall of Poland predates OSS service and an interval remains undocumented.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "medium",
            "publication_status": "publish_qualified",
            "match_notes": "Published as documented prewar activity, not a named employer and not an immediate affiliation.",
            "sources": [
                {"source_key": ADST, "locator_override": "PDF physical page 26, internal page 26; Joseph Walter Neubert self-interview"},
                {"source_key": STYMA_CITATION, "support_type": "context_only", "locator_override": "PDF physical page 81; protected identifier withheld"},
            ],
        },
        {
            "key": "identity-kay-keiichi-sugahara-b928",
            "person_id": PEOPLE[43][0],
            "claim_type": "identity",
            "claim_text": "The indexed Kay K Sugahara is a high-confidence match to Kay Keiichi Sugahara, whose UCLA biography and Arlington record both identify OSS service.",
            "evidence_excerpt": "In 1942 Sugahara joined the Office of Strategic Services",
            "evidence_paraphrase": "UCLA supplies the full name and chronology; Arlington independently lists Kay K. Sugahara with OSS service.",
            "identity_match_assessment": "High confidence from the rare exact indexed form, expanded middle name, two authoritative institutional sources and explicit OSS references.",
            "temporal_assessment": "Both sources identify wartime OSS service; UCLA dates entry to 1942.",
            "source_quality": "A_direct_official",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "The adjacent Kelichi K Sugahara row remains separate and is linked only as a possible variant/duplicate requiring the personnel files.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 454 row 43; Box 756"},
                {"source_key": UCLA, "locator_override": "Kay Keiichi Sugahara biographical note, paragraphs 1-4"},
                {"source_key": ARLINGTON, "locator_override": "Columbarium table, I-15-3"},
            ],
        },
        {
            "key": "last-civilian-kay-sugahara-universal-b928",
            "person_id": PEOPLE[43][0],
            "affiliation_key": "kay-sugahara-universal-foreign-service-b928",
            "claim_type": "last_civilian_pre_service",
            "claim_text": "Kay Keiichi Sugahara founded Universal Foreign Service Company after graduating in 1932 and worked as a customs broker before forced removal and OSS service in 1942.",
            "evidence_excerpt": "he opened his own firm, Universal Foreign Service Company",
            "evidence_paraphrase": "The UCLA institutional biography names the firm, the 1932 starting point, Sugahara's customs-broker occupation, wartime forced removal and 1942 OSS entry.",
            "identity_match_assessment": "High confidence from the distinctive name and independent UCLA and Arlington OSS identifications.",
            "temporal_assessment": "Strongly date-bounded as the last documented civilian enterprise before wartime displacement and service; not labeled immediate because forced removal intervened.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "Self-employment and named company are preserved separately. UCLA's postwar oil activity is excluded from this pre-OSS claim and the site's oil-company category.",
            "sources": [
                {"source_key": UCLA, "locator_override": "Kay Keiichi Sugahara biographical note, paragraphs 2-4"},
                {"source_key": ARLINGTON, "support_type": "context_only", "locator_override": "Columbarium table, I-15-3"},
            ],
        },
        {
            "key": "identity-kelichi-k-sugahara-candidate-b928",
            "person_id": PEOPLE[44][0],
            "claim_type": "identity",
            "claim_text": "Kay Keiichi Sugahara is a possible identity candidate for the separate Kelichi K Sugahara index row.",
            "evidence_paraphrase": "The adjacent rows share surname, box and similar given-name letters, while UCLA expands Kay's middle name to Keiichi; no source proves that the two rows represent one person.",
            "identity_match_assessment": "Low for this row because the index preserves Kay K and Kelichi K as separate entries and no personnel-file or protected-identifier linkage establishes duplication.",
            "temporal_assessment": "The candidate biography covers prewar employment and 1942 OSS service, but neither may be assigned to this row without direct linkage.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "low",
            "publication_status": "withheld_low_confidence",
            "match_notes": "Private candidate only. The entities remain separate; the Universal Foreign Service Company affiliation is published only for Kay K Sugahara.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 454 rows 43-44; Box 756; rows preserved separately"},
                {"source_key": UCLA, "locator_override": "Kay Keiichi Sugahara biographical note"},
                {"source_key": ARLINGTON, "support_type": "context_only", "locator_override": "Columbarium table, I-15-3: Kay K. Sugahara"},
            ],
        },
    ])
    return result


def archival_update(row: int, reason: str) -> dict[str, object]:
    person_id, name, box = PEOPLE[row]
    return {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, Box {box} and archive location, but staged official, CIA-site, OSS, employment, occupation, obituary, institutional, newspaper, directory and archival searches found no defensible identity bridge. {reason}",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": f"Review Box {box} for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }


def person_updates() -> list[dict[str, object]]:
    updates = [archival_update(row, reason) for row, reason in UNRESOLVED.items()]
    for row, data in ARMY_IDENTITIES.items():
        evidence = "An exact full name and nonshared protected identifier connect the index row to the official Army record."
        status = "occupation_only_found" if row in ARMY_OCCUPATIONS else "requires_archival_review"
        identity = "high_confidence"
        next_action = f"Review Box {PEOPLE[row][2]} for the immediate pre-OSS affiliation and named employer or institution."
        if row == 27:
            next_action += " Historical occupation code 047 remains uninterpreted."
        elif row == 32:
            identity = "confirmed"
            evidence = "The exact name, nonshared protected identifier and a NARA OSS citation carrying the same protected value establish the indexed entity; an ADST oral history adds a documented prewar courier role."
            next_action = "Review Box 756 to identify the employer or sponsoring organization for the prewar courier runs and to establish the Army-to-OSS chronology."
        elif row == 33:
            evidence += " A January 1945 OSS Athens roster independently names Peter A. Stymfal as a Pfc. operative in Greece."
            next_action = "Review Box 756 to identify the school represented by the 1943 student code and establish the Army-to-OSS chronology."
        elif row == 41:
            evidence = "A nonshared protected identifier links the indexed Carlos V Sucre row to an official Army record spelling the middle initial U. The disagreement remains visible."
        update: dict[str, object] = {
            "person_id": PEOPLE[row][0],
            "identity_status": identity,
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
        if row == 32:
            update["name_variants"] = ["Mitch Styma"]
        if data.get("variant"):
            update["name_variants"] = [str(data["variant"])]
        updates.append(update)
    group = duplicate_group("kay-kelichi-sugahara-page454-b928")
    updates.append({
        "person_id": PEOPLE[43][0],
        "identity_status": "high_confidence",
        "identity_evidence": "The distinctive indexed form Kay K Sugahara aligns with UCLA's Kay Keiichi Sugahara biography and Arlington's official Kay K. Sugahara OSS listing.",
        "name_variants": ["Kay Keiichi Sugahara"],
        "manual_review_required": True,
        "possible_duplicate_group": group,
        "research_status": "verified_employer_found",
        "next_action": "Review both Box 756 Sugahara files to determine whether the adjacent Kelichi row is a duplicate or a different person, and to document the exact Universal Foreign Service Company separation date.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "critical",
    })
    updates.append({
        **archival_update(44, "Kay Keiichi Sugahara is a plausible spelling/duplication candidate, but no direct evidence links that biography to this separate row."),
        "identity_status": "ambiguous",
        "possible_duplicate_group": group,
        "archival_review_priority": "critical",
        "identity_evidence": "Kay K Sugahara and Kelichi K Sugahara are adjacent Box 756 rows and UCLA gives Kay's full name as Kay Keiichi Sugahara. The source rows remain separate because no personnel-file or protected-identifier evidence proves duplication.",
        "next_action": "Review both Box 756 files together for identifiers, cross-references and duplicate-file evidence before assigning Kay Keiichi Sugahara's biography or employer to this row.",
    })
    return updates


def research_attempts() -> list[dict[str, object]]:
    attempts: list[dict[str, object]] = []
    for row, (person_id, name, box) in PEOPLE.items():
        if row == 43:
            outcome, reviewed, rejected = "source_reviewed", 9, 3
            detail = "UCLA and Arlington independently establish the Kay Keiichi/Kay K identity and OSS service; UCLA names Universal Foreign Service Company and the customs-broker role before wartime displacement."
        elif row == 44:
            outcome, reviewed, rejected = "candidate_found", 8, 4
            detail = "Kay Keiichi Sugahara is a strong spelling/duplication candidate, but the two printed index rows remain separate and only the personnel files can resolve them."
        elif row == 32:
            outcome, reviewed, rejected = "source_reviewed", 10, 3
            detail = "The protected-identifier Army bridge, NARA OSS citation and ADST oral history establish identity, a dated occupation category and a qualified prewar courier role without naming an employer."
        elif row == 33:
            outcome, reviewed, rejected = "source_reviewed", 8, 3
            detail = "The protected-identifier Army bridge and OSS Athens roster establish identity; the Army code records student status but names no school or employer."
        elif row == 41:
            outcome, reviewed, rejected = "source_reviewed", 7, 3
            detail = "A nonshared protected identifier establishes a high-confidence Army bridge despite the V/U middle-initial disagreement; the wholesale-manager category names no enterprise."
        elif row == 27:
            outcome, reviewed, rejected = "source_reviewed", 7, 3
            detail = "A protected-identifier Army bridge establishes high-confidence identity, but occupation code 047 remains uninterpreted and no named employer was found."
        elif row in {26, 45}:
            outcome, reviewed, rejected = "candidate_found", 7, 4
            detail = UNRESOLVED[row]
        else:
            outcome, reviewed, rejected = "no_result", 6, 3
            detail = UNRESOLVED[row]
        attempts.append({
            "key": f"page454-row{row}-{slug(name)}-b928",
            "person_id": person_id,
            "source_adapter": "manual_staged_protocol",
            "query_text": f"{name}; NARA index and public Archives context; CIA Reading Room site-restricted exact-name discovery; OSS and spelling/transliteration variants; employer and occupation 1940; obituary, institutional, newspaper, Library of Congress and archival searches; Box {box}; protected-identifier Army crosswalk where defensible",
            "query_variant_type": "staged_identity_employment_archival_protocol_batch_928",
            "started_at": "2026-10-27T01:30:00Z",
            "completed_at": "2026-10-27T04:00:00Z",
            "outcome": outcome,
            "sources_reviewed": reviewed,
            "candidate_sources_rejected": rejected,
            "rejection_reasons": "Unbridged namesakes, search snippets, family-only assertions, modern profiles, postwar-only leads and sources without an OSS or Box-file bridge were not assigned. Grouped CIA Reading Room and Library of Congress site-restricted exact-name discovery checks returned no person-specific pre-OSS result.",
            "research_notes": f"{detail} The index page and relevant Army code pages were visually checked. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA API call was made.",
            "next_action": f"Review Box {box} for corroborating identifiers and the immediate pre-OSS affiliation or last civilian employer.",
            "attempt_number": 1,
            "research_agent_version": "before-oss-b928-v1",
        })
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-928-v1",
        "reviewer": "Before OSS Batch 928 evidence review",
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
