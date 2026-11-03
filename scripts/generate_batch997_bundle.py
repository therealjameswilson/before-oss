#!/usr/bin/env python3
"""Generate the reviewed Batch 997 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page489-wallace-to-walsh-"
    "review_batch-997_2026-11-03.json"
)

INDEX = "nara-index-b997"
ARMY = "army-bulk-b997"
TECH = "army-tech-b997"
CODES = "army-codes-b997"
WALLER = "cia-waller-interview-b997"
SHIELD = "phi-kappa-psi-wallace-b997"

ORG_STATE = "state-department-b997"
ORG_BAKER = "baker-daniels-b997"
ORG_STANDARD = "standard-oil-unspecified-b997"

PEOPLE = {
    1: ("8bc4b395-0a4a-533d-a735-d52e8feed49e", "Inovar A Wallace"),
    2: ("f5761189-b996-54ad-a6de-dad011c891d2", "Jean Browne Wallace"),
    3: ("e8ffff68-cbe1-5f73-b56c-790384467c03", "John G Wallace"),
    4: ("495edc87-1bf8-5311-86e9-3908355b8a27", "Lynn de G Wallace"),
    5: ("edb65626-5c15-5103-9fea-0e6439eefff6", "Marcel H Wallace"),
    6: ("4dad3b4c-bd4c-5cf6-9c6b-ee05d6bcec26", "Neville M Wallace"),
    7: ("fbe9b621-0b06-5e77-9a74-25a7d6bd1462", "Owen M Wallace"),
    8: ("8347189c-b6e2-5bc4-bf45-479125cc7fa4", "Paul J Wallace"),
    9: ("37fbed5a-c775-5986-8537-5d3426ea809a", "Paul Kimball Wallace"),
    10: ("3ac25756-5223-543a-80f8-91c0dbe55656", "Robert E Wallace"),
    11: ("c5fd2f1d-f46c-5c5c-a684-66cfc89a8368", "Sherman L Wallace"),
    12: ("801f3a93-552c-5231-8fe6-68720b866029", "Warrack Wallace"),
    13: ("f9a11234-9f48-57d3-a7b2-620e8a6f3dd7", "Maurice Gene Wallen"),
    14: ("66448181-04d2-5eed-a887-261a5208c333", "Victor Wallen"),
    15: ("35e24273-0c50-5564-a61d-092f6cc2ff3e", "Clarence V Wallenberg"),
    16: ("c1248ae4-8088-5b8c-bbb4-a0dccc020cc9", "John Henry Waller"),
    17: ("4143ff42-e3f0-5646-a2fd-093f584ed0ef", "Mabel Aclydia Waller"),
    18: ("1142a070-a82f-5a46-8dde-491655534c2e", "Helen Wallin"),
    19: ("535c2746-7a1a-5209-83f2-8c950010965c", "Jack H Wallin"),
    20: ("7deac770-4360-589a-9cae-fbaafc42479d", "Sophia A Wallon"),
    21: ("cc075c6c-f5c1-570a-948a-b6d54e62621b", "Michel Walon"),
    22: ("a50ca661-582d-5197-a6c7-9720e25ab021", "Ingrid Walot"),
    23: ("0fd0b591-736e-5627-91d3-5ad3ea455852", "Emily A.T. Walsh"),
}

UNRESOLVED = {
    2: "A Henry A. Wallace family candidate has the exact distinctive name, but available sources supply no OSS, Box 813, identifier, assignment, or employment bridge; the famous-name lead was not assigned.",
    3: "Exact-name, identifier, OSS, employer, occupation, obituary, institutional, newspaper, directory, and archival searches produced no reliable identity bridge.",
    4: "Exact-name and punctuation-variant searches produced no source with an OSS, indexed-identifier, employer, unit, or personnel-file bridge.",
    5: "A commercial death-index namesake and other modern results supplied no OSS, indexed-identifier, employer, or personnel-file bridge and were rejected.",
    9: "A reputable obituary identifies a Paul Kimball Wallace born in 1920, but it supplies no OSS, Box 814, wartime assignment, identifier, or employment bridge; the candidate remains unassigned.",
    11: "A 1946 university employment record for a Sherman L Wallace lacks an OSS, indexed-identifier, rank, unit, or personnel-file bridge and was not assigned.",
    13: "Exact-name, identifier, OSS, employer, occupation, obituary, institutional, newspaper, directory, and archival searches produced no reliable identity bridge.",
    14: "Common-name and spelling-variant searches produced modern namesakes but no OSS, Box 814, employer, unit, or personnel-file bridge.",
    15: "Exact-name and Wallenberg-family searches produced no source with an OSS, indexed-identifier, employer, assignment, or personnel-file bridge.",
    17: "The exceptionally distinctive indexed name produced no reliable external identity, occupation, employer, or OSS assignment source.",
    18: "An obituary-derived alumni page describes a Helen Wallin in OSS, but supplies no Box 814, identifier, assignment, or other direct bridge to this common-name row; it remains a lead only.",
    20: "Exact-name, initial, OSS, employer, occupation, obituary, institutional, newspaper, directory, and archival searches produced no reliable identity bridge.",
    21: "French-rank and exact-name searches produced no source with an OSS assignment, service detail, employer, or personnel-file bridge beyond the index.",
    22: "Exact-name and spelling-variant searches produced only the NARA index and irrelevant modern results; no reliable identity or employer source was found.",
    23: "Exact-name, punctuation-variant, OSS, employer, occupation, obituary, institutional, newspaper, directory, and archival searches produced no reliable identity bridge.",
}

ARMY_OCCUPATIONS = {
    6: ("1943-10-05", "170", "sales clerk", "Sales clerks", "PDF physical page 171; historical category 1-70"),
    7: ("1943-07-12", "591", "manufacturing foreman", "Foremen, manufacturing", "PDF physical page 175; historical category 5-91"),
    8: ("1941-10-06", "105", "general office clerk", "Clerks, general office", "PDF physical page 171; historical category 1-05"),
    10: ("1942-02-18", "579", "railroad or carshop mechanic or repairman", "Mechanics and repairmen, railroad and carshop", "PDF physical page 175; historical category 5,7-79"),
    19: ("1942-08-04", "118", "general industry clerk", "General industry clerks", "PDF physical page 171; historical category 1-18"),
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 812-814",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 489, rows 1-23; checked against layout-preserving text and an original-detail page render",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. Protected identifiers remain private. PDF page 489 row 24, James B Walsh, is outside this cohort and begins the next batch.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; six accepted protected-identifier comparisons; identifiers and record ordinals withheld",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "Five exact-name identity bridges and one high-confidence Inovar/Ingvar spelling bridge were accepted. The post-OSS Inovar/Ingvar occupation field was not published as pre-OSS evidence.",
        },
        {
            "key": TECH,
            "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf",
            "archival_identifier": "NN3-064-03-008; National Archives Identifier 1263923",
            "title": "World War II Army Enlistment Records: Reference Copy of Technical Documentation",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives at College Park - Electronic Records",
            "publication_record_date": "1994-2005; reference copy modified 2011",
            "locator": "PDF physical pages 44-46; name, Army-entry-date, grade, and civilian-occupation fields",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
        },
        {
            "key": CODES,
            "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1CL_SD.pdf",
            "archival_identifier": "National Archives Identifier 1263923; Code No. 30",
            "title": "NARA Compiled Code Lists for the Electronic Army Serial Number Merged File",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives at College Park - Electronic Records",
            "publication_record_date": "2011-01-12; modified 2011-03-17",
            "locator": "PDF physical pages 171 and 175; historical civilian-occupation categories 1-05, 1-18, 1-70, 5-91, and 5,7-79",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "The cited pages were checked in extracted text and original-detail renders. Historical labels identify broad occupations, not named employers, workplaces, or exact OSS-transfer dates.",
        },
        {
            "key": WALLER,
            "stable_url": "https://commons.wikimedia.org/wiki/File:Studies_in_Intelligence_-_An_Interview_With_John_H._Waller.pdf",
            "archival_identifier": "CIA release C06122540",
            "title": "An Interview With John H. Waller",
            "author_creator": "Central Intelligence Agency, Studies in Intelligence",
            "repository_publisher": "Central Intelligence Agency; public scan hosted by Wikimedia Commons",
            "publication_record_date": "Interviewed 1999-05-24; approved for release 2014-09-03",
            "locator": "PDF physical page 1, printed page 43, introductory biography",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "Studies in Intelligence",
            "document_number": "C06122540",
            "rights_notes": "The original CIA release page was visually inspected. Only a short supporting excerpt is republished.",
        },
        {
            "key": SHIELD,
            "stable_url": "https://phikappapsiarchive.com/wp-content/uploads/2012/03/1969-70_vol90_no1-4.pdf",
            "archival_identifier": "The Shield of Phi Kappa Psi, volume 90, 1969-1970",
            "title": "W. Warrack Wallace, Purdue '11",
            "author_creator": "The Shield of Phi Kappa Psi",
            "repository_publisher": "Phi Kappa Psi Fraternity archive",
            "publication_record_date": "Fall 1969",
            "locator": "PDF physical page 59, printed page 57, obituary in chapter eternal section",
            "access_date": "2026-11-03",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "The Shield of Phi Kappa Psi",
            "rights_notes": "The institutional obituary page was checked in extracted text and an original-detail render. Excerpts are limited to the shortest text needed for each claim.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": ORG_STATE,
            "organization_id": "4d2fbb5f-218d-5445-b7b3-4c2fd22f0286",
            "canonical_name": "United States Department of State",
            "historical_name": "Department of State",
            "aliases": ["U.S. Department of State"],
            "organization_type": "federal executive department",
            "sector": "federal_government",
            "country": "United States",
            "normalization_notes": "Existing canonical department reused. The relationship is a government assignment, not private employment.",
        },
        {
            "key": ORG_BAKER,
            "canonical_name": "Baker & Daniels",
            "historical_name": "Baker & Daniels",
            "aliases": [],
            "organization_type": "law firm",
            "sector": "law",
            "city": "Indianapolis",
            "state_or_region": "Indiana",
            "country": "United States",
            "normalization_notes": "The employer name printed in the institutional obituary is preserved; no modern successor firm is substituted.",
        },
        {
            "key": ORG_STANDARD,
            "canonical_name": "Standard Oil Company (entity unspecified)",
            "historical_name": "Standard Oil Company",
            "aliases": [],
            "organization_type": "petroleum company",
            "sector": "business_and_industry",
            "country": "China",
            "normalization_notes": "The source does not identify the Standard Oil corporate entity or subsidiary. This broad historical record is not merged with any named Standard Oil successor or regional company.",
        },
    ]


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, _label, _locator) in ARMY_OCCUPATIONS.items():
        values.append({
            "key": f"{slug(PEOPLE[row][1])}-army-occupation-b997",
            "person_id": PEOPLE[row][0],
            "occupation": occupation,
            "relationship_type": "employment",
            "end_date": date,
            "date_precision": f"Historical civilian-occupation code {code} was recorded at Army entry on {date}; no named employer, workplace, or exact OSS-transfer date is supplied.",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "confirmed",
            "claim_confidence": "medium",
            "source_quality": "A_direct_official",
            "publication_status": "publish_qualified",
            "research_notes": "Broad historical occupation category only; no named employer or workplace is inferred.",
        })
    values.extend([
        {
            "key": "john-henry-waller-state-b997",
            "person_id": PEOPLE[16][0],
            "organization_key": ORG_STATE,
            "organization_name_as_found": "State Department",
            "relationship_type": "government_assignment",
            "end_date": "1944",
            "date_precision": "The CIA biography explicitly says Waller joined OSS from the State Department in 1944; no month or job title is supplied.",
            "country": "United States",
            "immediate_pre_oss": True,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "explicit_immediate",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "A_direct_official",
            "publication_status": "published",
            "research_notes": "Direct government-to-OSS transition; not labeled a private civilian employer.",
        },
        {
            "key": "warrack-wallace-baker-daniels-b997",
            "person_id": PEOPLE[12][0],
            "organization_key": ORG_BAKER,
            "organization_name_as_found": "Baker & Daniels",
            "role_title": "senior partner",
            "occupation": "corporate lawyer",
            "relationship_type": "employment",
            "start_date": "1923",
            "date_precision": "The institutional obituary says he joined in 1923, became a senior partner, served in military intelligence during World War II, and left the firm in 1953; an exact military-leave date is not supplied.",
            "city": "Indianapolis",
            "state_or_region": "Indiana",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": True,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "published",
            "research_notes": "Best-supported last civilian employer before wartime military service. The source does not establish the exact transition into OSS.",
        },
        {
            "key": "warrack-wallace-standard-oil-b997",
            "person_id": PEOPLE[12][0],
            "organization_key": ORG_STANDARD,
            "organization_name_as_found": "Standard Oil Company",
            "relationship_type": "employment",
            "date_precision": "The obituary places this China employment after Purdue graduation and before Harvard Law School and the 1923 Baker & Daniels role; no years or corporate subsidiary are supplied.",
            "country": "China",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "published",
            "research_notes": "Earlier documented employment. The unspecified Standard Oil entity remains separate from named regional and successor organizations.",
        },
    ])
    return values


def claim(key: str, row: int, claim_type: str, text: str, paraphrase: str,
          identity: str, temporal: str, quality: str, confidence: str,
          publication: str, notes: str, source_links: list[dict[str, str]],
          affiliation_key: str | None = None) -> dict[str, object]:
    value: dict[str, object] = {
        "key": key, "person_id": PEOPLE[row][0], "claim_type": claim_type,
        "claim_text": text, "evidence_paraphrase": paraphrase,
        "identity_match_assessment": identity, "temporal_assessment": temporal,
        "source_quality": quality, "claim_confidence": confidence,
        "publication_status": publication, "match_notes": notes,
        "sources": source_links,
    }
    if affiliation_key:
        value["affiliation_key"] = affiliation_key
    return value


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, label, locator) in ARMY_OCCUPATIONS.items():
        name = PEOPLE[row][1]
        values.extend([
            claim(
                f"identity-{slug(name)}-b997", row, "identity",
                f"Indexed {name} is confirmed as the reviewed official Army entry record.",
                "The exact indexed and Army names agree, and a nonshared protected identifier connects the records.",
                "Confirmed by direct protected-identifier agreement; the identifier and record ordinal remain private.",
                f"The Army record dates entry to {date} and supplies only historical civilian code {code}.",
                "A_direct_official", "confirmed", "published",
                "Identity only; no named employer or exact OSS-transfer date is inferred.",
                [{"source_key": INDEX, "locator_override": f"PDF page 489 row {row}; protected identifier withheld"},
                 {"source_key": ARMY, "locator_override": "Accepted reviewed identity bridge; protected identifier withheld"}],
            ),
            claim(
                f"occupation-{slug(name)}-b997", row, "occupation",
                f"At Army entry on {date}, {name} was recorded in the historical {occupation} category; no named employer is identified.",
                f"The accepted Army record carries civilian-occupation code {code}, decoded from NARA's official code list.",
                "The category belongs only to the confirmed protected-identifier match; the identifier itself is not public.",
                "Strongly date-bounded to Army entry; it does not establish the immediate pre-OSS affiliation or a named employer.",
                "A_direct_official", "medium", "publish_qualified",
                "Published with its limits and excluded from verified-employer analytics.",
                [{"source_key": ARMY, "locator_override": f"Army entry {date}; civilian occupation code {code}; protected identifier withheld"},
                 {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46"},
                 {"source_key": CODES, "locator_override": locator, "excerpt_override": label}],
                f"{slug(name)}-army-occupation-b997",
            ),
        ])
    values.extend([
        claim(
            "identity-inovar-wallace-b997", 1, "identity",
            "Indexed Inovar A Wallace is a high-confidence match to the reviewed official Army record for Ingvar A Wallace.",
            "A nonshared protected identifier, surname, middle initial, and exceptionally distinctive one-letter given-name variant connect the records.",
            "High confidence, not confirmed, because the protected identifier agrees but the indexed Inovar and Army Ingvar spellings conflict.",
            "The Army record dates entry to 1 November 1945, after OSS dissolution; its occupation field is not published as pre-OSS evidence.",
            "A_direct_official", "high", "published",
            "Identity bridge only. The personnel file must resolve the spelling and pre-OSS chronology.",
            [{"source_key": INDEX, "locator_override": "PDF page 489 row 1; protected identifier withheld"},
             {"source_key": ARMY, "locator_override": "Accepted high-confidence name-variant bridge; protected identifier withheld"}],
        ),
        claim(
            "identity-warrack-wallace-b997", 12, "identity",
            "Indexed Warrack Wallace is a high-confidence match to W. Warrack Wallace, Purdue 1911, Indianapolis lawyer, and wartime military-intelligence major.",
            "The institutional obituary supplies the exceptionally distinctive exact surname and given name plus a compatible wartime intelligence chronology and Major rank.",
            "High confidence from the rare exact name and compatible military-intelligence biography; the personnel file remains unreviewed.",
            "The biography places engineering, China employment, law school, legal employment, and wartime military intelligence in sequence.",
            "B_authoritative_institutional", "high", "published",
            "The Box 814 file is still needed to establish the exact OSS assignment and transition date.",
            [{"source_key": INDEX, "locator_override": "PDF page 489 row 12; protected officer identifier withheld"},
             {"source_key": SHIELD, "locator_override": "PDF physical page 59, printed page 57", "excerpt_override": "W. Warrack Wallace, Purdue '11"}],
        ),
        claim(
            "last-civilian-warrack-wallace-b997", 12, "last_civilian_pre_service",
            "Baker & Daniels is Warrack Wallace's best-supported last civilian employer before wartime military service.",
            "The institutional obituary says he joined the Indianapolis law firm in 1923, became a senior partner specializing in corporate law, and later joined military intelligence.",
            "High-confidence rare-name identity supported by the same institutional biography and compatible indexed officer identifier.",
            "Documented prewar employment and best-supported last civilian role; the exact military-leave and OSS transition dates are not supplied.",
            "B_authoritative_institutional", "high", "published",
            "The employer is not labeled the immediate pre-OSS affiliation because an intervening military-intelligence assignment is documented.",
            [{"source_key": SHIELD, "locator_override": "PDF physical page 59, printed page 57", "excerpt_override": "former senior partner in the Indianapolis law firm of Baker & Daniels, which he joined in 1923"}],
            "warrack-wallace-baker-daniels-b997",
        ),
        claim(
            "earlier-standard-oil-warrack-wallace-b997", 12, "other_pre_oss_affiliation",
            "Warrack Wallace worked in China for Standard Oil Company after Purdue and before Harvard Law School.",
            "The institutional obituary explicitly places the employment between his engineering degree and legal education.",
            "High-confidence rare-name identity supported by the same institutional biography and compatible wartime intelligence chronology.",
            "Definitely prewar and earlier than Baker & Daniels; not immediate to OSS. The specific Standard Oil entity and dates are not identified.",
            "B_authoritative_institutional", "high", "published",
            "The generic historical company record is kept separate from named Standard Oil subsidiaries and successors.",
            [{"source_key": SHIELD, "locator_override": "PDF physical page 59, printed page 57", "excerpt_override": "After graduation he worked in China for the Standard Oil Company."}],
            "warrack-wallace-standard-oil-b997",
        ),
        claim(
            "identity-john-henry-waller-b997", 16, "identity",
            "Indexed John Henry Waller is a high-confidence match to CIA officer John H. Waller, who joined OSS in 1944.",
            "The original CIA Studies in Intelligence release uses the compatible full first name and middle initial and explicitly documents OSS entry.",
            "High confidence from the distinctive name, matching middle initial, and direct official OSS chronology; the Box 814 file remains unreviewed.",
            "The official biography dates the State Department-to-OSS move to 1944.",
            "A_direct_official", "high", "published",
            "The personnel file can supply a direct file linkage and fuller State Department role.",
            [{"source_key": INDEX, "locator_override": "PDF page 489 row 16"},
             {"source_key": WALLER, "locator_override": "PDF physical page 1, printed page 43"}],
        ),
        claim(
            "immediate-state-john-henry-waller-b997", 16, "immediate_pre_oss_affiliation",
            "The United States Department of State was John H. Waller's immediate documented affiliation before he joined OSS in 1944.",
            "The original CIA biography explicitly says he joined OSS from the State Department in 1944.",
            "High-confidence name and direct official OSS chronology; the indexed file can confirm the exact file linkage.",
            "Explicit immediate transition in 1944; no job title or month is supplied.",
            "A_direct_official", "high", "published",
            "Government assignment, not mislabeled as a private civilian employer.",
            [{"source_key": WALLER, "locator_override": "PDF physical page 1, printed page 43", "excerpt_override": "joined OSS from the State Department in 1944"}],
            "john-henry-waller-state-b997",
        ),
    ])
    return values


def base_update(row: int, **overrides: object) -> dict[str, object]:
    value: dict[str, object] = {
        "person_id": PEOPLE[row][0], "manual_review_required": True,
        "personnel_file_digitized": False, "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }
    value.update(overrides)
    return value


def person_updates() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, reason in UNRESOLVED.items():
        overrides: dict[str, object] = {}
        if row == 21:
            overrides = {
                "personnel_category": "foreign_or_allied_military_personnel",
                "commissioned_officer": True,
                "allied_or_foreign_personnel": True,
            }
        values.append(base_update(
            row,
            identity_status="unresolved",
            identity_evidence=f"The visually verified page 489 row preserves {PEOPLE[row][1]} and its archival context. {reason}",
            research_status="requires_archival_review",
            next_action=f"Review the indexed personnel file for corroborating identifiers, the immediate pre-OSS affiliation, and the last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}",
            **overrides,
        ))
    for row in ARMY_OCCUPATIONS:
        occupation = ARMY_OCCUPATIONS[row][2]
        values.append(base_update(
            row,
            identity_status="confirmed",
            identity_evidence="The exact indexed name and a nonshared protected identifier connect the row to the reviewed official Army record.",
            personnel_category="enlisted_army_personnel",
            commissioned_officer=False,
            allied_or_foreign_personnel=False,
            research_status="occupation_only_found",
            next_action=f"Review the indexed personnel file to identify any named employer behind the broad {occupation} category and establish the Army-to-OSS chronology.",
            nara_catalog_id="1263923",
        ))
    values.extend([
        base_update(
            1,
            identity_status="high_confidence",
            identity_evidence="A nonshared protected identifier, surname, middle initial, and exceptionally distinctive one-letter Inovar/Ingvar spelling variant connect the index and Army records. The spelling remains subject to personnel-file review.",
            name_variants=["Ingvar A Wallace"],
            personnel_category="enlisted_army_personnel",
            commissioned_officer=False,
            allied_or_foreign_personnel=False,
            research_status="needs_temporal_review",
            next_action="Review Box 813 to resolve the Inovar/Ingvar spelling and document the pre-OSS affiliation. The accepted Army entry is dated 1 November 1945, after OSS dissolution, so its occupation field is not used as pre-OSS evidence.",
            nara_catalog_id="1263923",
            archival_review_priority="critical",
        ),
        base_update(
            12,
            identity_status="high_confidence",
            identity_evidence="The exceptionally distinctive exact Warrack Wallace name and institutional biography document Purdue, law practice, military intelligence, Third Army service, and retirement as a Major in a chronology compatible with the index.",
            name_variants=["W. Warrack Wallace"],
            personnel_category="commissioned_army_officer",
            commissioned_officer=True,
            allied_or_foreign_personnel=False,
            research_status="verified_employer_found",
            next_action="Review Box 814 to establish the exact military-intelligence-to-OSS transition and assignment. Baker & Daniels is the verified last civilian employer; Standard Oil Company is documented earlier employment.",
            archival_review_priority="medium",
        ),
        base_update(
            16,
            identity_status="high_confidence",
            identity_evidence="The original CIA Studies in Intelligence release identifies John H. Waller and explicitly says he joined OSS from the State Department in 1944; the full indexed John Henry Waller form is compatible.",
            name_variants=["John H. Waller"],
            research_status="verified_employer_found",
            next_action="Review Box 814 to confirm the direct personnel-file linkage, State Department role, and any last civilian employer before government service. The immediate State Department-to-OSS transition is explicit.",
            archival_review_priority="medium",
        ),
    ])
    return values


def research_attempts() -> list[dict[str, object]]:
    attempts: list[dict[str, object]] = []
    sourced = set(ARMY_OCCUPATIONS) | {1, 12, 16}
    candidate_rejected = {2, 5, 9, 11, 14, 18}
    details = {
        1: "The protected-identifier Inovar/Ingvar bridge was accepted at high confidence, but its November 1945 Army entry cannot establish pre-OSS occupation.",
        12: "An institutional obituary supports the rare-name identity, Baker & Daniels as last civilian employer, earlier Standard Oil work in China, and wartime military-intelligence service.",
        16: "An original CIA release directly documents John H. Waller's 1944 State Department-to-OSS transition.",
    }
    for row, (person_id, name) in PEOPLE.items():
        if row in sourced:
            outcome, reviewed, rejected_count = "source_reviewed", 8, 5
            if row in details:
                note = details[row]
            else:
                note = f"A reviewed protected-identifier Army bridge supports identity and a qualified {ARMY_OCCUPATIONS[row][2]} category at Army entry; it supplies no named employer, workplace, or OSS-transfer date."
        elif row in candidate_rejected:
            outcome, reviewed, rejected_count = "candidate_rejected", 7, 7
            note = UNRESOLVED[row]
        else:
            outcome, reviewed, rejected_count = "no_result", 6, 6
            note = UNRESOLVED[row]
        attempts.append({
            "key": f"page489-row{row}-{slug(name)}-b997",
            "person_id": person_id,
            "source_adapter": "manual_staged_protocol",
            "query_text": f"{name}; NARA OSS index context; CIA Reading Room exact-name domain check; Library of Congress exact-name collection check; exact-name and meaningful variants; OSS, rank, branch, identifier and assignment clues; employer and occupation 1940; obituary, institutional, newspaper, directory and archival searches; indexed Box 812, 813 or 814; protected identifiers used only in private official-record comparison",
            "query_variant_type": "staged_identity_employment_archival_protocol_batch_997",
            "started_at": "2026-11-03T14:55:00Z",
            "completed_at": "2026-11-03T16:30:00Z",
            "outcome": outcome,
            "sources_reviewed": reviewed,
            "candidate_sources_rejected": rejected_count,
            "rejection_reasons": "Unbridged namesakes, snippets, commercial people-finder pages, relatives, unsourced genealogy, postwar-only leads, and sources without an OSS, protected-identifier, rank, unit, or personnel-file bridge were rejected. The Henry A. Wallace family lead, Paul Kimball Wallace obituary, and Helen Wallin alumni-page lead were not assigned without a direct bridge. Historical occupations were not converted into named employers, and the post-OSS Inovar/Ingvar Army occupation was withheld from pre-OSS claims.",
            "research_notes": f"{note} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain, and archival searches were checked as applicable. Grouped CIA Reading Room and Library of Congress discovery checks produced no additional publishable employer source for the cohort. The NARA index page was text-extracted, rendered, and visually checked; official Army bulk data, technical documentation, and code documentation were inspected locally. The CIA Waller release and Phi Kappa Psi obituary were opened and visually inspected. No search-result snippet was used as sole final evidence, no paywall or access control was bypassed, and no authenticated NARA Catalog API call was made.",
            "next_action": "Review the indexed personnel file for corroborating identifiers, the immediate pre-OSS affiliation, and the last civilian employer before wartime service.",
            "attempt_number": 1,
            "research_agent_version": "before-oss-b997-v1",
        })
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-997-v1",
        "reviewer": "Before OSS Batch 997 evidence review",
        "sources": sources(),
        "organizations": organizations(),
        "affiliations": affiliations(),
        "claims": claims(),
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }
    EvidenceBundle.model_validate(bundle)
    OUTPUT.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
