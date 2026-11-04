#!/usr/bin/env python3
"""Generate the reviewed Batch 1032 evidence bundle for PDF page 522."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page522-anthony-zucco-to-john-zwergel-review_"
    "batch-1032_2026-11-04.json"
)

INDEX = "nara-index-b1032"
ARMY = "army-bulk-b1032"
TECH = "army-tech-b1032"
CODES = "army-codes-b1032"
UN_ZUNG = "un-yearbook-zung-b1032"
SOOCHOW_ZUNG = "columbia-soochow-zung-b1032"
NARA_ZURLO = "nara-officer-cards-zurlo-b1032"
HOOVER_ZURLO = "hoover-ncr-interviews-zurlo-b1032"

ORG_NYU = "new-york-university-b1032"


PEOPLE = {
    1: ("a5c87af2-1156-568d-ab50-40ccdaa85d1d", "Anthony N Zucco", "865"),
    2: ("70602e22-738a-58a1-956f-45698184dc48", "John V Zuckerman", "865"),
    3: ("1f692e11-43bb-5e02-8699-d3d0ea2f9268", "John V Zuckerman", "865"),
    4: ("7b03d9d4-3553-5331-8fc9-be947a9e4cfd", "John M Zueker", "865"),
    5: ("5243a4ea-5b4a-53c8-8c58-86aa9d7a1d82", "Cecilia S Zung", "865"),
    6: ("ca2f3312-b7b6-54c8-b088-ef8a8aa8436e", "Charles J Zupa", "865"),
    7: ("ee85b027-0732-5308-a09d-9a47dfd86e53", "James R Zurfluh", "865"),
    8: ("eb71f275-786d-5245-b2dc-1f1eefb67f45", "Angelo A Zurlo", "865"),
    9: ("4c5f05af-5ed3-5fd2-ab0f-05e9244f1731", "James V Zvolanek", "865"),
    10: ("7de24aae-904f-5ac9-9a6a-5bd5c730ebab", "Francis J Zwakhals", "865"),
    11: ("dd37b20f-054b-5f9f-97bd-485d8cf38477", "Stefan M Zweig", "865"),
    12: ("fdbb05d5-ed7c-50d8-b0a6-f007d0d3521f", "John A Zwergel", "865"),
}


# Code 999 is intentionally absent: the inspected official table does not
# provide a reliable label that can be published as James Zurfluh's occupation.
ARMY_OCCUPATIONS = {
    1: ("1943-06-05", "226", "cook, except private family", "Cooks, except private family", "PDF physical page 172; historical category 2-26"),
    2: ("1942-05-05", "185", "salesperson or sales agent, except to consumers", "Salesmen and sales agents, except to consumers", "PDF physical page 172; historical categories 1-85 through 1-87"),
    4: ("1942-10-21", "105", "general office clerk", "Clerks, general office", "PDF physical page 171; historical category 1-05"),
    6: ("1942-10-10", "105", "general office clerk", "Clerks, general office", "PDF physical page 171; historical category 1-05"),
    10: ("1943-06-15", "088", "ship captain, mate, pilot, or engineer", "Ship captains, mates, pilots, and engineers", "PDF physical page 171; historical category 0-88"),
    12: ("1943-06-17", "736", "chauffeur or driver of a bus, taxi, truck, or tractor", "Chauffeurs and drivers, bus, taxi, truck, and tractor", "PDF physical page 174; historical categories 5, 7-36"),
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def source(key: str, **kwargs: object) -> dict[str, object]:
    value: dict[str, object] = {"key": key, "access_date": "2026-11-04"}
    value.update(kwargs)
    return value


def sources() -> list[dict[str, object]]:
    return [
        source(
            INDEX,
            stable_url="https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            archival_identifier="RG 226, Entry A1-224, Box 865",
            title="OSS Personnel Files from Excel",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="2010-12-23",
            locator="PDF page 522, rows 1-12; final page and all rows visually checked",
            source_quality="A_direct_official",
            collection_name="Records of the Office of Strategic Services, Record Group 226",
            rights_notes="All twelve printed rows remain separate. Full protected identifiers remain private.",
        ),
        source(
            ARMY,
            stable_url="https://catalog.archives.gov/id/1263923",
            archival_identifier="National Archives Identifier 1263923; parent series NAID 604357",
            title="Electronic Army Serial Number Merged File, ca. 1938-1946",
            author_creator="Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="1938-1946; merged file created 2002",
            locator="Official unrestricted ASNEF.FIN.DAT; seven Batch 1032 candidate links explicitly reviewed",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records",
            document_number="ASNEF.FIN.DAT",
            rights_notes="No raw record or full protected identifier is retained in public assets.",
        ),
        source(
            TECH,
            stable_url="https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf",
            archival_identifier="NN3-064-03-008; National Archives Identifier 1263923",
            title="World War II Army Enlistment Records: Reference Copy of Technical Documentation",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives at College Park - Electronic Records",
            publication_record_date="1994-2005; reference copy modified 2011",
            locator="PDF physical pages 44-46; identifier, name, Army-entry-date, grade and civilian-occupation fields",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records technical documentation",
            rights_notes="Used to interpret selected fields only; source damage, coding limits and incomplete coverage remain applicable.",
        ),
        source(
            CODES,
            stable_url="https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1CL_SD.pdf",
            archival_identifier="National Archives Identifier 1263923; Code No. 30",
            title="NARA Compiled Code Lists for the Electronic Army Serial Number Merged File",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives at College Park - Electronic Records",
            publication_record_date="2011-01-12; modified 2011-03-17",
            locator="PDF physical pages 171, 172 and 174; all six published Batch 1032 categories visually checked",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records technical documentation",
            rights_notes="Historical categories identify neither employer, institution nor workplace. Code 999 remains uninterpreted.",
        ),
        source(
            UN_ZUNG,
            stable_url="https://cdn.un.org/unyearbook/yun/chapter_pdf/1947-48YUN/1947-48_APPENDICES.pdf",
            title="Yearbook of the United Nations 1947-48",
            author_creator="United Nations",
            repository_publisher="United Nations",
            publication_record_date="1949",
            locator="Who's Who in the United Nations, page 1093; Cecilia Sieu-ling Zung entry",
            source_quality="B_authoritative_institutional",
            collection_name="Yearbook of the United Nations",
            rights_notes="Contemporary institutional biography explicitly identifies OSS work and separates education, legal practice, postal-censorship work and postwar teaching.",
        ),
        source(
            SOOCHOW_ZUNG,
            stable_url="https://journals.library.columbia.edu/index.php/cjal/article/download/3137/6798",
            title="Training China's Early Modern Lawyers: Soochow University Law School",
            author_creator="Alison W. Conner",
            repository_publisher="Journal of Chinese Law, Columbia University",
            publication_record_date="Spring 1994",
            locator="Volume 8, number 1, pages 24-25",
            source_quality="C_reputable_contemporary_or_scholarly",
            collection_name="Journal of Chinese Law",
            rights_notes="Scholarly institutional history corroborates the full name, Soochow class, Columbia degrees, 1942 NYU J.S.D. and 1946 faculty appointment.",
        ),
        source(
            NARA_ZURLO,
            stable_url="https://www.archives.gov/iwg/declassified-records/rg-226-oss/personnel-folder-list.pdf",
            archival_identifier="RG 226, Entry UD-WX 1567, Box 100, microfilm roll 21",
            title="OSS: Headquarters and Headquarters Detachment Personnel Records",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            locator="Microfilm roll list: Officer Personnel Record Cards, Waugh through Zurlo, Angelo A.",
            source_quality="A_direct_official",
            collection_name="Records of the Office of Strategic Services, Record Group 226",
            rights_notes="Official finding aid confirms that Angelo A. Zurlo appears in the officer personnel-card sequence; it supplies no pre-OSS employer.",
        ),
        source(
            HOOVER_ZURLO,
            stable_url="https://digitalcollections.hoover.org/internal/media/dispatcher/331574/full",
            title="Index of Personnel Interviewed in the North African Theater of Operations",
            author_creator="United States Office of Strategic Services",
            repository_publisher="Hoover Institution Library & Archives Digital Collections",
            publication_record_date="1940s",
            locator="PDF page 20, entry 594; Angelo A. Zurlo, 1st Lt., Bari",
            source_quality="A_direct_official",
            collection_name="Declassified United States government records",
            rights_notes="The wartime index establishes rank and station but does not supply a pre-OSS employer or transfer sequence.",
        ),
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": ORG_NYU,
            "canonical_name": "New York University",
            "historical_name": "New York University Law School",
            "aliases": ["N.Y. University", "New York University School of Law"],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "New York",
            "state_or_region": "New York",
            "country": "United States",
            "normalization_notes": "Student status is not employment; the historical institutional name is preserved from the sources.",
        }
    ]


def affiliation(key: str, row: int, relationship: str, temporal: str, identity: str, confidence: str, quality: str, status: str = "published", **kwargs: object) -> dict[str, object]:
    value: dict[str, object] = {
        "key": key,
        "person_id": PEOPLE[row][0],
        "relationship_type": relationship,
        "pre_oss_temporal_basis": temporal,
        "identity_confidence": identity,
        "claim_confidence": confidence,
        "source_quality": quality,
        "publication_status": status,
    }
    value.update(kwargs)
    return value


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, _label, _locator) in ARMY_OCCUPATIONS.items():
        identity = "high_confidence" if row in {4, 10} else "confirmed"
        values.append(
            affiliation(
                f"{slug(PEOPLE[row][1])}-army-occupation-b1032",
                row,
                "unknown",
                "strongly_date_bounded",
                identity,
                "medium",
                "A_direct_official",
                "publish_qualified",
                occupation=occupation,
                end_date=date,
                date_precision=f"Historical civilian-occupation code {code} was recorded at Army entry on {date}; no named employer is supplied.",
                country="United States",
                immediate_pre_oss=False,
                last_civilian_pre_service=False,
                research_notes="Broad historical category only; excluded from verified-employer analytics and not narrowed beyond the official wording.",
            )
        )
    values.extend(
        [
            affiliation(
                "cecilia-zung-shanghai-law-practice-b1032",
                5,
                "self_employment",
                "documented_prewar",
                "high_confidence",
                "high",
                "B_authoritative_institutional",
                occupation="lawyer",
                role_title="practising lawyer",
                start_date="1934",
                end_date="1937",
                date_precision="The UN yearbook explicitly dates private legal practice in Shanghai to 1934-37; it does not connect that work directly to OSS recruitment.",
                city="Shanghai",
                country="China",
                immediate_pre_oss=False,
                last_civilian_pre_service=False,
                research_notes="Documented earlier self-employment; not presented as the immediate predecessor or last civilian role before OSS.",
            ),
            affiliation(
                "cecilia-zung-nyu-student-b1032",
                5,
                "student",
                "strongly_date_bounded",
                "high_confidence",
                "high",
                "C_reputable_contemporary_or_scholarly",
                organization_key=ORG_NYU,
                organization_name_as_found="New York University Law School",
                role_title="J.S.D. student",
                end_date="1942",
                date_precision="The scholarly institutional history dates Zung's J.S.D. to 1942; no matriculation date is supplied.",
                city="New York",
                state_or_region="New York",
                country="United States",
                immediate_pre_oss=False,
                last_civilian_pre_service=False,
                research_notes="Education is modeled separately from employment.",
            ),
            affiliation(
                "cecilia-zung-postal-censor-translator-b1032",
                5,
                "government_assignment",
                "temporal_relation_uncertain",
                "high_confidence",
                "medium",
                "B_authoritative_institutional",
                "publish_qualified",
                role_title="U.S. Postal Censor and Senior Translator",
                occupation="postal censor and senior translator",
                date_precision="The UN biography lists this former U.S. work before former OSS work but supplies no dates or explicit direct-transfer statement.",
                city="San Francisco and New York",
                country="United States",
                immediate_pre_oss=False,
                last_civilian_pre_service=False,
                research_notes="Potentially the closest documented pre-OSS government role, but sequence and employing bureau remain unproven.",
            ),
        ]
    )
    return values


def claim(key: str, row: int, claim_type: str, text: str, paraphrase: str, identity: str, temporal: str, quality: str, confidence: str, source_links: list[dict[str, str]], notes: str, status: str = "published", affiliation_key: str | None = None) -> dict[str, object]:
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
        "sources": source_links,
    }
    if affiliation_key:
        value["affiliation_key"] = affiliation_key
    return value


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, label, locator) in ARMY_OCCUPATIONS.items():
        key = f"{slug(PEOPLE[row][1])}-army-occupation-b1032"
        identity = (
            "High confidence from a nonshared protected linkage plus reviewed name variation; the protected identifier is not published."
            if row in {4, 10}
            else "Confirmed by exact name and a nonshared protected linkage; the protected identifier is not published."
        )
        values.append(
            claim(
                f"occupation-{slug(PEOPLE[row][1])}-b1032",
                row,
                "occupation",
                f"At Army entry on {date}, {PEOPLE[row][1]} was recorded in the historical category {occupation}; no employer is identified.",
                f"The Army bulk file records code {code} at entry, and the official code list defines it as {label}.",
                identity,
                "Strongly date-bounded to Army entry, but not proven to be the immediately preceding role.",
                "A_direct_official",
                "medium",
                [
                    {"source_key": INDEX},
                    {"source_key": ARMY},
                    {"source_key": TECH, "support_type": "context_only"},
                    {"source_key": CODES, "locator_override": locator},
                ],
                "The historical category is qualified, excluded from verified-employer analytics and not converted into a named employer.",
                "publish_qualified",
                key,
            )
        )
    values.extend(
        [
            claim(
                "identity-cecilia-zung-b1032",
                5,
                "identity",
                "Indexed Cecilia S Zung is strongly supported as Cecilia Sieu-ling Zung, a Chinese lawyer and former OSS biographical research analyst.",
                "The contemporary UN biography names Cecilia Sieu-ling Zung and explicitly identifies her former OSS research work; the scholarly history corroborates her education and career.",
                "High confidence from the uncommon surname, matching Cecilia S initials, explicit OSS role and independent institutional chronology.",
                "Identity and wartime OSS context; the claim does not establish an immediate predecessor.",
                "B_authoritative_institutional",
                "high",
                [{"source_key": INDEX}, {"source_key": UN_ZUNG}, {"source_key": SOOCHOW_ZUNG}],
                "The full Sieu-ling form is retained as a documented name variant.",
            ),
            claim(
                "earlier-cecilia-zung-law-practice-b1032",
                5,
                "other_pre_oss_affiliation",
                "Cecilia Sieu-ling Zung practiced law in Shanghai from 1934 to 1937.",
                "The UN yearbook explicitly dates her Shanghai legal practice to 1934-37.",
                "High confidence through the explicit OSS identity bridge in the same institutional biography.",
                "Documented prewar self-employment; not shown as immediate before OSS.",
                "B_authoritative_institutional",
                "high",
                [{"source_key": UN_ZUNG}],
                "No firm is named, so the relationship is self-employment rather than an invented employer.",
                "published",
                "cecilia-zung-shanghai-law-practice-b1032",
            ),
            claim(
                "student-cecilia-zung-nyu-b1032",
                5,
                "other_pre_oss_affiliation",
                "Cecilia Sieu-ling Zung completed a J.S.D. at New York University Law School in 1942; the university is not treated as an employer.",
                "The Columbia-published institutional history identifies Zung and dates her New York University J.S.D. to 1942.",
                "High confidence from the uncommon full name and matching education chronology in two institutional sources.",
                "Strongly date-bounded to 1942; no direct OSS-recruitment sequence is stated.",
                "C_reputable_contemporary_or_scholarly",
                "high",
                [{"source_key": SOOCHOW_ZUNG}, {"source_key": UN_ZUNG, "support_type": "context_only"}],
                "Education remains separate from employment.",
                "published",
                "cecilia-zung-nyu-student-b1032",
            ),
            claim(
                "government-cecilia-zung-postal-censor-b1032",
                5,
                "other_pre_oss_affiliation",
                "Before or during her U.S. wartime career, Cecilia Sieu-ling Zung worked as a U.S. postal censor and senior translator; the precise sequence before OSS is unproven.",
                "The UN biography lists former U.S. postal-censor and senior-translator work in San Francisco and New York before former OSS research work.",
                "High confidence through the explicit rare-name and OSS bridge in the same source.",
                "Temporal relation remains uncertain because no dates or direct-transfer language are supplied.",
                "B_authoritative_institutional",
                "medium",
                [{"source_key": UN_ZUNG}],
                "The source does not name a bureau, so no employing organization is invented and the role is not labeled immediate.",
                "publish_qualified",
                "cecilia-zung-postal-censor-translator-b1032",
            ),
            claim(
                "identity-angelo-zurlo-officer-b1032",
                8,
                "identity",
                "Angelo A Zurlo was an OSS first lieutenant stationed at Bari and appears in the official officer personnel-card sequence.",
                "NARA's official roll list ends its officer personnel cards with Zurlo; a wartime OSS interview index lists Angelo A. Zurlo as a first lieutenant at Bari.",
                "High confidence from the exact uncommon full name in two independent OSS records.",
                "Wartime identity, commissioned status and station only; no pre-OSS affiliation is established.",
                "A_direct_official",
                "high",
                [{"source_key": INDEX}, {"source_key": NARA_ZURLO}, {"source_key": HOOVER_ZURLO}],
                "The claim supports commissioned Army-officer classification but not an employer or immediate predecessor.",
            ),
            claim(
                "duplicate-john-v-zuckerman-row2-b1032",
                2,
                "identity",
                "Two adjacent John V Zuckerman rows remain separate; the first has a reviewed Army identity link and the note 'also AS.'",
                "The source index prints two separate rows, while only the first currently has a nonshared protected Army linkage.",
                "Confirmed for the first row; the second row remains ambiguous and is not merged solely on normalized name.",
                "Identity-resolution context only.",
                "A_direct_official",
                "conflicting",
                [{"source_key": INDEX}, {"source_key": ARMY, "support_type": "context_only"}],
                "Both source rows and person entities remain separately recoverable.",
                "conflicting",
            ),
            claim(
                "duplicate-john-v-zuckerman-row3-b1032",
                3,
                "identity",
                "The second adjacent John V Zuckerman row remains a separate ambiguous entity pending personnel-file review.",
                "The source index prints this row separately from the 'also AS' row; no independent public or protected identifier currently resolves it.",
                "Ambiguous because an identical normalized name alone is insufficient for a merge.",
                "Identity-resolution context only.",
                "A_direct_official",
                "conflicting",
                [{"source_key": INDEX}],
                "No occupation or affiliation is transferred from the first row.",
                "conflicting",
            ),
        ]
    )
    return values


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
    updates = [
        base_update(1, identity_status="confirmed", identity_evidence="A nonshared protected linkage and exact official name agreement connect the index and Army records; the protected identifier remains private.", personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="occupation_only_found", nara_catalog_id="1263923", next_action="Review Box 865 to identify a named employer or institution and establish Army-to-OSS chronology. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed; the bulk record supplies only a historical cook category."),
        base_update(2, identity_status="confirmed", identity_evidence="A nonshared protected linkage and exact official name agreement connect the first printed John V Zuckerman row to an Army record; the adjacent same-name row remains separate.", personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, possible_duplicate_group="batch1032-john-v-zuckerman-adjacent-rows", research_status="occupation_only_found", nara_catalog_id="1263923", archival_review_priority="critical", next_action="Review both adjacent Box 865 rows and the 'also AS' cross-reference before any merge. Identify a named employer and Army-to-OSS chronology; the bulk record supplies only a historical sales category."),
        base_update(3, identity_status="ambiguous", identity_evidence="The index prints a second adjacent John V Zuckerman row with a different protected identifier, but no independent public identity or affiliation bridge was found.", possible_duplicate_group="batch1032-john-v-zuckerman-adjacent-rows", research_status="needs_identity_review", archival_review_priority="critical", next_action="Review both Box 865 personnel files and the 'also AS' notation to determine whether the adjacent rows describe one person, two people or a cross-reference. No occupation or affiliation is transferred from the first row."),
        base_update(4, identity_status="high_confidence", identity_evidence="A nonshared protected linkage plus agreeing first name and middle initial connect indexed John M Zueker to Army John M Zucker; both surname spellings remain visible.", name_variants=["John M Zucker"], replace_name_variants=False, personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="occupation_only_found", nara_catalog_id="1263923", archival_review_priority="critical", next_action="Review Box 865 to confirm the Zueker/Zucker spelling and identify a named employer or institution. No reliable pre-OSS employer has yet been identified; the bulk record supplies only a historical office-clerk category."),
        base_update(5, identity_status="high_confidence", identity_evidence="A contemporary UN biography explicitly identifies Cecilia Sieu-ling Zung as a former OSS biographical research analyst; an independent scholarly institutional history corroborates her education and career.", name_variants=["Cecilia Sieu-ling Zung", "Cecilia S L Zung", "Cheng Xiuling"], replace_name_variants=False, personnel_category="civilian_professional_or_administrative_grade", commissioned_officer=False, allied_or_foreign_personnel=True, research_status="documented_prewar_employer_found", archival_review_priority="high", next_action="Review Box 865 to date the postal-censor and senior-translator work, determine whether it directly preceded OSS, and identify the employing bureau. The 1934-37 Shanghai law practice is documented earlier self-employment, not labeled immediate."),
        base_update(6, identity_status="confirmed", identity_evidence="A nonshared protected linkage and exact official name agreement connect the index and Army records; the protected identifier remains private.", personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="occupation_only_found", nara_catalog_id="1263923", next_action="Review Box 865 to identify a named employer or institution and establish Army-to-OSS chronology. No reliable pre-OSS employer has yet been identified; the bulk record supplies only a historical office-clerk category."),
        base_update(7, identity_status="confirmed", identity_evidence="A nonshared protected linkage and exact official name agreement connect the index and Army records; occupation code 999 remains uninterpreted.", personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="requires_archival_review", nara_catalog_id="1263923", archival_review_priority="critical", next_action="Review Box 865 to identify James R Zurfluh's pre-OSS affiliation. No occupation or employer is inferred from code 999, and no reliable pre-OSS employer has yet been identified in the accessible sources reviewed."),
        base_update(8, identity_status="high_confidence", identity_evidence="The exact uncommon full name appears in NARA's official officer personnel-card range and a wartime OSS interview index, which identifies Angelo A. Zurlo as a first lieutenant at Bari.", personnel_category="commissioned_army_officer", commissioned_officer=True, allied_or_foreign_personnel=False, research_status="requires_archival_review", archival_review_priority="critical", next_action="Review Box 865 and the officer personnel card on Box 100 roll 21 to identify Angelo A Zurlo's immediate pre-OSS assignment and last civilian employer. Accessible evidence establishes rank and OSS station only."),
        base_update(9, identity_status="unresolved", identity_evidence="The visually verified final-page source preserves James V Zvolanek, but exact-name, OSS, obituary, occupation, official and archival searches produced no reliable identity-and-affiliation bridge.", research_status="requires_archival_review", archival_review_priority="critical", next_action="Review Box 865 for corroborating identifiers, immediate pre-OSS affiliation and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed; an unsourced genealogy lead was rejected."),
        base_update(10, identity_status="high_confidence", identity_evidence="A nonshared protected linkage plus uncommon surname and middle initial connect indexed Francis J Zwakhals to Army Francois J Zwakhals; both forename forms remain visible.", name_variants=["Francois J Zwakhals", "François J Zwakhals"], replace_name_variants=False, personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="occupation_only_found", nara_catalog_id="1263923", archival_review_priority="critical", next_action="Review Box 865 to confirm the Francis/Francois form, identify a named maritime employer and establish Army-to-OSS chronology. The bulk record supplies only a historical maritime occupation category."),
        base_update(11, identity_status="unresolved", identity_evidence="Exact-name searches were dominated by the famous Austrian author and did not yield a corroborating identifier for indexed Stefan M Zweig.", research_status="requires_archival_review", archival_review_priority="critical", next_action="Review Box 865 for nationality, birth date, rank, assignment and pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed, and the famous author's biography is not assigned to this row."),
        base_update(12, identity_status="confirmed", identity_evidence="A nonshared protected linkage and exact official name agreement connect the index and Army records; the protected identifier remains private.", personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="occupation_only_found", nara_catalog_id="1263923", next_action="Review Box 865 to identify a named employer or institution and establish Army-to-OSS chronology. No reliable pre-OSS employer has yet been identified; the bulk record supplies only a historical driver category."),
    ]
    if len(updates) != 12:
        raise RuntimeError(f"Expected 12 person updates, generated {len(updates)}")
    return updates


def unresolved_reason(row: int) -> str:
    return {
        3: "The adjacent same-name row lacks an independent identifier and was not merged solely on normalized name.",
        7: "The official Army link supports identity, but code 999 remains uninterpreted and no named employer was found.",
        9: "An unsourced genealogy lead did not establish an OSS bridge or pre-OSS affiliation.",
        11: "The famous Austrian author is an unbridged namesake; no reliable identity-and-affiliation bridge was found.",
    }.get(row, "Unbridged namesakes, discovery-only summaries, snippets and postwar-only leads did not establish a pre-OSS employer.")


def research_attempts() -> list[dict[str, object]]:
    updates = {item["person_id"]: item for item in person_updates()}
    values: list[dict[str, object]] = []
    for row, (person_id, name, box) in PEOPLE.items():
        status = str(updates[person_id]["research_status"])
        substantiated = row in set(ARMY_OCCUPATIONS) | {5, 7, 8}
        values.append(
            {
                "key": f"page522-row{row}-{slug(name)}-b1032",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index context; exact-name and meaningful initial, spelling, punctuation, transliteration and OCR variants; OSS, CIA Reading Room, rank, branch, assignment and protected-identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory and archival searches; indexed Box {box}",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_1032",
                "started_at": "2026-11-04T13:45:00-05:00",
                "completed_at": "2026-11-04T15:50:00-05:00",
                "outcome": "source_reviewed" if substantiated else "candidate_rejected",
                "sources_reviewed": 10 if row in {5, 8} else (7 if substantiated else 5),
                "candidate_sources_rejected": 3 if substantiated else 4,
                "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives and postwar-only leads were rejected. Army categories were not converted into named employers, code 999 was not interpreted, adjacent identical names were not merged, and discovery-only material about John V Zuckerman was not published as evidence.",
                "research_notes": f"{unresolved_reason(row)} The official index, exact-name OSS searches, targeted NARA and CIA context, and employer, occupation, obituary, institutional, newspaper, directory and archival searches were reviewed as applicable. Page 522 and cited code-list pages were visually checked. The CIA adapter's robots restriction and a bounded Library of Congress timeout remain preserved as separate source-access attempts; no authenticated NARA Catalog API request was made.",
                "next_action": str(updates[person_id]["next_action"]),
                "attempt_number": 3,
                "research_agent_version": "before-oss-b1032-v1",
            }
        )
    if len(values) != 12:
        raise RuntimeError(f"Expected 12 research attempts, generated {len(values)}")
    return values


def main() -> None:
    bundle = {
        "bundle_version": "batch-1032-v1",
        "reviewer": "Before OSS Batch 1032 evidence review",
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
