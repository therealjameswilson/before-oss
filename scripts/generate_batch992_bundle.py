#!/usr/bin/env python3
"""Generate the reviewed Batch 992 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page486-vyhnal-to-wadsworth-"
    "review_batch-992_2026-11-03.json"
)

INDEX = "nara-index-b992"
ARMY = "army-bulk-b992"
TECH = "army-tech-b992"
CODES = "army-codes-b992"
UMN = "umn-commencement-wachsmuth-b992"
AFSA = "afsa-wabeke-b992"
ORG_UMN = "university-minnesota-b992"


PEOPLE = {
    24: ("6c54d837-08b0-5ea8-ac67-20a5a9dac9ed", "William Vyhnal"),
    25: ("ec9478ce-7f0d-5119-a623-35b1d85606f1", "Henry Waas"),
    26: ("104c6d8f-56ef-574c-83c9-a77be88717b0", "Bertus Harry Wabeke"),
    27: ("43702028-77fa-508f-87ba-611149fc00b3", "Daniel L Wachner"),
    28: ("7dfbbef1-b7c6-5180-9b1c-39c3e3f5ad71", "Ruth M Wachs"),
    29: ("ff3e3bf6-50ff-584e-b4bd-93f375eb53ae", "John E Wachsmuth"),
    30: ("7dfb0209-7e0e-5d19-8124-3b873e0f3264", "Robert A Wacht"),
    31: ("513fca2b-f391-5b4c-829d-45742f5d887f", "Ruth E Waddell"),
    32: ("483e3bc7-e5d7-5242-8201-7d9906eb0b6f", "William E Waddell"),
    33: ("a71edd00-2296-51ea-8c61-bb85eee7aa0c", "Catherine Wade"),
    34: ("e32621a4-ab2c-585b-8e57-0b8d866e8dfc", "Charles S Wade"),
    35: ("6c4fc1e4-c315-5a60-93b4-177def3c7506", "Emmitt M Wade"),
    36: ("ff583686-338b-5109-b433-5843d0e20780", "Grant H Wade"),
    37: ("dadf7da5-596b-5b2a-9c79-042bb37f0476", "Nena Violet Wade"),
    38: ("ba820870-b924-56f4-8a09-8d231f4550c2", "Stanley F Wade"),
    39: ("5035b1e1-ea6f-5fe2-a516-3087c26dd204", "Alfred Inge Wadell"),
    40: ("9aab06e7-109d-5b25-88fa-8cd1bf095ece", "Frank Wadena"),
    41: ("956c1940-c4ea-585d-a9d9-fa55bafb651b", "Mildred B Wadkins"),
    42: ("454be13a-b545-548c-8b6e-2d4d7e19e483", "Julia F Wadleigh"),
    43: ("88ce0a53-fea0-5b8e-8e06-81f2b9f91bdf", "Frederick J Wadley III"),
    44: ("c5c9705a-3a43-552c-bb27-bb097a531f17", "Milton J Wadlow"),
    45: ("818022e6-813b-5f18-84b3-bae818d7ee84", "Harold E Wadman"),
    46: ("82f8e2aa-c474-5b1a-90d9-190b1e567b5c", "Claude V Wadsworth"),
}


UNRESOLVED = {
    24: "Exact-name, OSS, employer, occupation, obituary, institutional, newspaper and archival searches produced no reliable identity bridge.",
    25: "The index identifies a French second lieutenant, but Henry/Henri Waas and BCRA variants produced no source that connects a namesake to Box 810.",
    27: "Exact-name, middle-initial, OSS, occupation, obituary, directory and archival searches produced no reliable identity bridge.",
    28: "Exact-name and middle-initial searches produced no source with an OSS, protected-identifier or personnel-file bridge.",
    30: "The unusually formatted protected identifier produced no compatible official Army candidate, and name searches did not supply a defensible alternative bridge.",
    31: "Common-name results lacked the middle initial, OSS assignment and two corroborating identifiers required for assignment.",
    32: "Common-name results and wartime rosters did not connect a William E. Waddell to this Box 810 row.",
    33: "Common-name searches produced multiple incompatible candidates without a protected identifier or OSS assignment bridge.",
    35: "The protected identifier produced no compatible reviewed Army bulk candidate; exact-name searches found no reliable pre-OSS chronology.",
    36: "The protected identifier produced no compatible reviewed Army bulk candidate; common-name searches remained unbridged.",
    37: "The distinctive exact name produced no source with an OSS, employer, occupation or archival bridge.",
    38: "At least two Stanley F. Wade namesakes appear in public records; neither has the corroborating identifiers needed for assignment.",
    39: "Exact and spelling-variant searches for Alfred Inge or Alfred I. Wadell produced no source linking a namesake to the protected identifier or OSS.",
    40: "Exact-name, identifier, OSS, occupation, obituary, institutional and newspaper searches produced no reliable match.",
    41: "Exact-name, occupation, directory, obituary, newspaper and archival searches produced no reliable identity bridge.",
    42: "A 1940 registration index names a Mrs. Julia F. Wadleigh as a relative, but it does not establish her own identity, OSS service or employment and was rejected.",
    44: "Postwar RCA Communications material names Milton J. Wadlow, but it supplies neither an OSS bridge nor evidence that the later job preceded OSS.",
    45: "Exact-name, OSS, military, occupation, obituary and archival searches produced no reliable identity bridge.",
    46: "A VA-derived cemetery transcription names a World War II Army lieutenant colonel Claude V. Wadsworth, but it lacks the indexed identifier, OSS link and pre-service chronology.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 809-810",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 486, rows 24-46; checked against layout-preserving text and an original-detail page render",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. Protected identifiers remain private. Page 486 row 47, Geoffrey E. Wagner, is outside this cohort.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; two accepted protected-identifier comparisons; identifiers and record ordinals withheld",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "Exact name and nonshared protected identifier confirmed two Army identities. Raw bulk rows, record ordinals and full identifiers do not enter public assets.",
        },
        {
            "key": TECH,
            "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf",
            "archival_identifier": "NN3-064-03-008; National Archives Identifier 1263923",
            "title": "World War II Army Enlistment Records: Reference Copy of Technical Documentation",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives at College Park - Electronic Records",
            "publication_record_date": "1994-2005; reference copy modified 2011",
            "locator": "PDF physical pages 44-46; name, Army-entry-date, grade and civilian-occupation fields",
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
            "locator": "PDF physical pages 172 and 178 visually inspected; historical categories 2-66 and 5-83",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical categories identify broad occupations, not named employers, workplaces, police agencies or exact OSS-transfer dates.",
        },
        {
            "key": UMN,
            "stable_url": "https://hdl.handle.net/11299/57565",
            "archival_identifier": "University Digital Conservancy handle 11299/57565; bitstream 8ce1ff9b-1fed-41a2-9a5e-2c9b9f82fc26",
            "title": "Commencement Program, 1943",
            "author_creator": "University of Minnesota",
            "repository_publisher": "University of Minnesota Digital Conservancy",
            "publication_record_date": "1943-06-12",
            "locator": "PDF physical page 52, printed page 15; Department of Military Science and Tactics, Reserve Officers Training Corps Graduates, Coast Artillery Corps Reserve; visually inspected",
            "access_date": "2026-11-03",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "University of Minnesota commencement programs",
            "rights_notes": "The program documents a 1943 ROTC affiliation. It does not identify an employer or state when Wachsmuth entered OSS.",
        },
        {
            "key": AFSA,
            "stable_url": "https://afsa.org/sites/default/files/fsj-1954-06-june_0.pdf",
            "archival_identifier": "Foreign Service Journal, June 1954, printed page 42",
            "title": "The Foreign Service Journal, June 1954",
            "author_creator": "American Foreign Service Association",
            "repository_publisher": "American Foreign Service Association",
            "publication_record_date": "1954-06",
            "locator": "PDF physical page 44, printed page 42, Personals column; visually inspected",
            "access_date": "2026-11-03",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Foreign Service Journal archive",
            "rights_notes": "Postwar institutional biography used only as qualified identity context. Education and later State Department work are not converted into pre-OSS employment.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": ORG_UMN,
            "organization_id": "a7d41a87-9f88-51a4-9eb3-fb8de0ce10a1",
            "canonical_name": "University of Minnesota",
            "historical_name": "University of Minnesota",
            "aliases": [],
            "organization_type": "public university",
            "sector": "academia_and_research",
            "city": "Minneapolis and Saint Paul",
            "state_or_region": "Minnesota",
            "country": "United States",
            "normalization_notes": "Historical name preserved. Golda Stegner's staff role is distinct from her later student listing. John E. Wachsmuth's ROTC affiliation is not treated as civilian employment.",
        }
    ]


def affiliations() -> list[dict[str, object]]:
    return [
        {
            "key": "wachsmuth-umn-rotc-b992",
            "person_id": PEOPLE[29][0],
            "organization_key": ORG_UMN,
            "organization_name_as_found": "University of Minnesota, Department of Military Science and Tactics",
            "role_title": "Reserve Officers Training Corps graduate, Coast Artillery Corps Reserve",
            "relationship_type": "student",
            "end_date": "1943-06-12",
            "date_precision": "The 1943 commencement program lists John E. Wachsmuth among ROTC graduates under Coast Artillery Corps Reserve; his exact OSS-entry date is unknown.",
            "city": "Minneapolis",
            "state_or_region": "Minnesota",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "temporal_relation_uncertain",
            "identity_confidence": "probable",
            "claim_confidence": "medium",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "publish_qualified",
            "research_notes": "A wartime university and ROTC affiliation, not employment. Box 810 is needed to establish identity and sequence relative to OSS.",
        },
        {
            "key": "charles-wade-army-category-b992",
            "person_id": PEOPLE[34][0],
            "occupation": "repairmen and mechanics, n.e.c.",
            "relationship_type": "employment",
            "end_date": "1943-04-30",
            "date_precision": "Historical civilian-occupation code 583 was recorded at Army entry on 1943-04-30; no employer, workplace or OSS-transfer date is named.",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "confirmed",
            "claim_confidence": "medium",
            "source_quality": "A_direct_official",
            "publication_status": "publish_qualified",
            "research_notes": "Broad historical category only; no company, trade specialty or exact job is inferred.",
        },
        {
            "key": "frederick-wadley-army-category-b992",
            "person_id": PEOPLE[43][0],
            "occupation": "policemen and detectives, public service",
            "relationship_type": "employment",
            "end_date": "1943-05-29",
            "date_precision": "Historical civilian-occupation code 266 was recorded at Army entry on 1943-05-29; no police agency, employer or OSS-transfer date is named.",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "confirmed",
            "claim_confidence": "medium",
            "source_quality": "A_direct_official",
            "publication_status": "publish_qualified",
            "research_notes": "Historical public-service category only; no employing agency or jurisdiction is inferred.",
        },
    ]


def source_links(*keys: str) -> list[dict[str, str]]:
    return [{"source_key": key} for key in keys]


def claim(
    key: str,
    row: int,
    claim_type: str,
    text: str,
    paraphrase: str,
    identity: str,
    temporal: str,
    quality: str,
    confidence: str,
    status: str,
    notes: str,
    links: list[dict[str, str]],
    affiliation_key: str | None = None,
) -> dict[str, object]:
    value: dict[str, object] = {
        "key": key,
        "person_id": PEOPLE[row][0],
        "claim_type": claim_type,
        "claim_text": text,
        "evidence_paraphrase": paraphrase,
        "identity_match_assessment": identity,
        "temporal_assessment": temporal,
        "source_quality": quality,
        "claim_confidence": confidence,
        "publication_status": status,
        "match_notes": notes,
        "sources": links,
    }
    if affiliation_key:
        value["affiliation_key"] = affiliation_key
    return value


def claims() -> list[dict[str, object]]:
    return [
        claim(
            "identity-bertus-harry-wabeke-b992",
            26,
            "identity",
            "Indexed Bertus Harry Wabeke is probably the same rare-name World War II veteran profiled by the Foreign Service Journal in 1954.",
            "The institutional biography uses the exact three-part name, identifies him as a World War II veteran and gives a coherent postwar State Department chronology.",
            "Probable from the exceptionally distinctive exact full name and compatible World War II service; the reviewed source does not state OSS service or the indexed identifier.",
            "The biography is postwar identity context and does not establish his immediate pre-OSS affiliation.",
            "B_authoritative_institutional",
            "medium",
            "publish_qualified",
            "No education, authorship or later State Department work is presented as a pre-OSS employer.",
            source_links(INDEX, AFSA),
        ),
        claim(
            "identity-john-e-wachsmuth-b992",
            29,
            "identity",
            "Indexed John E Wachsmuth is a probable match to the John E. Wachsmuth listed as a 1943 University of Minnesota ROTC graduate.",
            "The institutional program uses the exact name and places him in a compatible wartime Coast Artillery Corps Reserve pathway.",
            "Probable from exact full name and compatible wartime military context; the program does not reproduce the indexed identifier or name OSS.",
            "The program is dated 12 June 1943; the exact OSS-entry date remains unknown.",
            "B_authoritative_institutional",
            "medium",
            "publish_qualified",
            "Box 810 is required before upgrading the identity to high confidence or classifying commissioned status.",
            source_links(INDEX, UMN),
        ),
        claim(
            "rotc-john-e-wachsmuth-b992",
            29,
            "other_pre_oss_affiliation",
            "A University of Minnesota program lists John E. Wachsmuth among its 1943 ROTC graduates under Coast Artillery Corps Reserve.",
            "The printed Department of Military Science and Tactics section places his exact name beneath the Coast Artillery Corps Reserve heading.",
            "Probable identity from exact name and compatible military context; no protected-identifier bridge was available.",
            "Dated wartime affiliation; its sequence relative to OSS is not established, so it is not marked immediate.",
            "B_authoritative_institutional",
            "medium",
            "publish_qualified",
            "The university is recorded as a student/ROTC affiliation and is excluded from employer analytics.",
            [
                {
                    "source_key": UMN,
                    "locator_override": "PDF physical page 52, printed page 15",
                    "excerpt_override": "RESERVE OFFICERS TRAINING CORPS GRADUATES ... Coast Artillery Corps Reserve ... JOHN E. WACHSMUTH",
                }
            ],
            "wachsmuth-umn-rotc-b992",
        ),
        claim(
            "identity-charles-s-wade-b992",
            34,
            "identity",
            "Indexed Charles S Wade is confirmed as the official Army entry record printed as Charles S Wade Jr.",
            "The index and Army bulk record agree in exact name and a nonshared protected identifier; the Army record supplies the Jr suffix.",
            "Confirmed by direct protected-identifier agreement; the identifier and bulk ordinal remain private.",
            "The Army record dates entry to 30 April 1943 and supplies only a broad civilian-occupation code.",
            "A_direct_official",
            "confirmed",
            "published",
            "Identity only; no employer or exact OSS-transfer date is inferred.",
            source_links(INDEX, ARMY),
        ),
        claim(
            "occupation-charles-s-wade-b992",
            34,
            "occupation",
            "At Army entry on 30 April 1943, Charles S. Wade Jr. was recorded in the historical repairmen and mechanics, n.e.c. category; no employer is identified.",
            "The accepted Army record carries civilian-occupation code 583, decoded from NARA's official code list.",
            "The occupation belongs only to the confirmed protected-identifier match.",
            "Strongly date-bounded to Army entry; it does not establish the immediate pre-OSS affiliation or a named employer.",
            "A_direct_official",
            "medium",
            "publish_qualified",
            "The broad historical category is not converted into a modern specialty, company or workplace.",
            [
                {"source_key": ARMY, "locator_override": "Army entry 1943-04-30; civilian occupation code 583; protected identifier withheld"},
                {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46; Army-entry-date and civilian-occupation fields"},
                {"source_key": CODES, "locator_override": "PDF physical page 178; historical category 5-83", "excerpt_override": "Repairmen and mechanics, n. e. c."},
            ],
            "charles-wade-army-category-b992",
        ),
        claim(
            "identity-frederick-j-wadley-iii-b992",
            43,
            "identity",
            "Indexed Frederick J Wadley III is confirmed as the official Army entry record printed as Frederick J Wadley Third.",
            "The index and Army bulk record agree in exact name, suffix and a nonshared protected identifier.",
            "Confirmed by direct protected-identifier agreement; the identifier and bulk ordinal remain private.",
            "The Army record dates entry to 29 May 1943 and supplies only a broad civilian-occupation code.",
            "A_direct_official",
            "confirmed",
            "published",
            "Identity only; no police agency, employer or exact OSS-transfer date is inferred.",
            source_links(INDEX, ARMY),
        ),
        claim(
            "occupation-frederick-j-wadley-iii-b992",
            43,
            "occupation",
            "At Army entry on 29 May 1943, Frederick J. Wadley III was recorded in the historical policemen and detectives, public service category; no agency is identified.",
            "The accepted Army record carries civilian-occupation code 266, decoded from NARA's official code list.",
            "The occupation belongs only to the confirmed protected-identifier and suffix match.",
            "Strongly date-bounded to Army entry; it does not establish the immediate pre-OSS affiliation or employing jurisdiction.",
            "A_direct_official",
            "medium",
            "publish_qualified",
            "The historical category is not converted into a named police department, detective agency or exact job title.",
            [
                {"source_key": ARMY, "locator_override": "Army entry 1943-05-29; civilian occupation code 266; protected identifier withheld"},
                {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46; Army-entry-date and civilian-occupation fields"},
                {"source_key": CODES, "locator_override": "PDF physical page 172; historical category 2-66", "excerpt_override": "Policemen and detectives, public service"},
            ],
            "frederick-wadley-army-category-b992",
        ),
    ]


def base_update(row: int, **overrides: object) -> dict[str, object]:
    value: dict[str, object] = {
        "person_id": PEOPLE[row][0],
        "manual_review_required": True,
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }
    value.update(overrides)
    return value


def person_updates() -> list[dict[str, object]]:
    values = [
        base_update(
            row,
            identity_status="unresolved",
            identity_evidence=f"The visually verified page 486 row preserves {PEOPLE[row][1]} and its Box 809 or 810 context. {reason}",
            research_status="requires_archival_review",
            next_action=f"Review the indexed personnel file for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}",
        )
        for row, reason in UNRESOLVED.items()
    ]
    values.extend(
        [
            base_update(
                26,
                identity_status="probable",
                identity_evidence="The exceptionally distinctive exact full name and compatible World War II veteran status support a probable match to the 1954 Foreign Service Journal biography, but no protected identifier or explicit OSS bridge was found.",
                research_status="requires_archival_review",
                next_action="Review Box 810 to confirm the probable identity and determine Wabeke's 1944 institutional role, OSS entry, immediate affiliation and last civilian employer. The reviewed postwar biography is identity context only.",
                archival_review_priority="high",
            ),
            base_update(
                29,
                identity_status="probable",
                identity_evidence="The exact full name and compatible wartime Coast Artillery Corps Reserve ROTC context support a probable match to the University of Minnesota program; the program lacks the indexed identifier and does not name OSS.",
                research_status="requires_archival_review",
                next_action="Review Box 810 to confirm the Minnesota ROTC match, commissioned status, the later military chronology, OSS entry and any civilian employer.",
                archival_review_priority="high",
            ),
            base_update(
                34,
                identity_status="confirmed",
                identity_evidence="The exact official name and a nonshared protected identifier connect the visually verified index row to the Army record; the Army record adds the Jr suffix.",
                name_variants=["Charles S Wade Jr"],
                personnel_category="enlisted_army_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                research_status="occupation_only_found",
                next_action="Review Box 810 to identify any named employer behind historical code 583 and establish the Army-to-OSS chronology.",
                nara_catalog_id="1263923",
            ),
            base_update(
                43,
                identity_status="confirmed",
                identity_evidence="The exact official name, suffix and a nonshared protected identifier connect the visually verified index row to the Army record.",
                name_variants=["Frederick J Wadley Third"],
                personnel_category="enlisted_army_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                research_status="occupation_only_found",
                next_action="Review Box 810 to identify the public-service agency behind historical code 266 and establish the Army-to-OSS chronology.",
                nara_catalog_id="1263923",
            ),
        ]
    )
    return values


def research_attempts() -> list[dict[str, object]]:
    sourced = {26, 29, 34, 43}
    candidate_rejected = {38, 42, 44, 46}
    details = {
        26: "A visually reviewed institutional biography produced a probable rare-name identity but no pre-OSS employer or explicit OSS bridge.",
        29: "A visually reviewed University of Minnesota program produced a probable, temporally qualified 1943 ROTC affiliation but no employer or OSS-entry date.",
        34: "The protected-identifier Army bridge produced a confirmed identity and a qualified historical mechanics occupation category.",
        43: "The protected-identifier and suffix bridge produced a confirmed identity and a qualified historical public-service police/detective category.",
    }
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        if row in sourced:
            outcome, reviewed, rejected = "source_reviewed", 8, 5
            detail = details[row]
        elif row in candidate_rejected:
            outcome, reviewed, rejected = "candidate_rejected", 7, 7
            detail = UNRESOLVED[row]
        else:
            outcome, reviewed, rejected = "no_result", 6, 6
            detail = UNRESOLVED.get(row, "No reliable identity or pre-OSS affiliation bridge was found.")
        attempts.append(
            {
                "key": f"page486-row{row}-{slug(name)}-b992",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index context; CIA Reading Room exact-name domain check; Library of Congress exact-name collection check; exact-name and meaningful variants; OSS, rank, branch, identifier and assignment clues; employer and occupation 1940; obituary, institutional, newspaper, directory and archival searches; indexed Box 809 or 810; protected identifiers used only in private official-record comparison",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_992",
                "started_at": "2026-11-02T22:45:00Z",
                "completed_at": "2026-11-03T12:35:00Z",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, snippets, commercial people-finder pages, relatives, unsourced genealogy, postwar-only leads and sources without an OSS, protected-identifier, rank, unit or personnel-file bridge were rejected. The Julia F. Wadleigh relative listing, Milton J. Wadlow RCA career, Stanley F. Wade namesakes and Claude V. Wadsworth cemetery lead were not assigned. Historical Army categories were not converted into named employers or agencies.",
                "research_notes": f"{detail} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain and archival searches were checked as applicable. Grouped exact-name CIA Reading Room and Library of Congress domain searches returned no results for the 23-person cohort. The NARA index, official Army bulk data, technical documentation and code-list pages were inspected directly; code-list physical pages 172 and 178, University of Minnesota physical page 52 and Foreign Service Journal physical page 44 were rendered and visually checked. No search-result snippet was used as sole final evidence, no paywall or access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": "Review the indexed personnel file for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before wartime service.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b992-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-992-v1",
        "reviewer": "Before OSS Batch 992 evidence review",
        "sources": sources(),
        "organizations": organizations(),
        "affiliations": affiliations(),
        "claims": claims(),
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }
    EvidenceBundle.model_validate(bundle)
    OUTPUT.write_text(
        json.dumps(bundle, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
