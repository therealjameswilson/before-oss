#!/usr/bin/env python3
"""Generate the reviewed Batch 943 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page462-john-f-taylor-to-francis-m-tchitcherine-"
    "review_batch-943_2026-10-28.json"
)

INDEX = "nara-index-b943"
ARMY = "army-bulk-b943"
TECH = "army-tech-b943"
CODES = "army-codes-b943"
RAWLEIGH_OSSOG = "ossog-rawleigh-taylor-b943"
RAWLEIGH_ISRAL = "isral-rawleigh-taylor-b943"
RAWLEIGH_WOODBERRY = "woodberry-rawleigh-taylor-b943"
FRANCIS_CIA = "cia-francis-tchitcherine-b943"

WOODBERRY = "woodberry-forest-school-b943"


PEOPLE = {
    1: ("f45e1881-7443-544c-a6d2-61ae21a9fcb5", "John F Taylor"),
    2: ("533a164e-8c23-5183-af61-1b542b8be527", "John G Taylor"),
    3: ("d750f344-9f0b-50a4-9260-8eeb12ffc64b", "John G Taylor"),
    4: ("a9f8d91f-2069-5e3c-82ed-b266ab54eaf8", "John H Taylor"),
    5: ("4b6e0700-4a21-5dc0-90b4-97967938e904", "John C Taylor"),
    6: ("659e745e-754d-59db-a8cb-1d3e1d5a8d0b", "Joseph O Taylor"),
    7: ("249a43c1-086c-5c0f-995f-aa29391cb4e0", "Kathleen Taylor"),
    8: ("b4d879fd-dfdb-5f98-b62c-9957787b631f", "Leonard P Taylor"),
    9: ("89e6570c-e0e9-537e-b537-ec1551970c79", "Lily R Taylor"),
    10: ("c61380d6-bfbb-5863-ad3e-69cc4486db70", "Louis L Taylor"),
    11: ("333ae34d-97a1-592e-bddd-36de0c6602b5", "Norma J Taylor"),
    12: ("8f23d067-f742-541c-a4f0-a647430198c6", "Parks T Taylor"),
    13: ("4ca0144a-5859-5df2-ac19-df87c9d76a55", "Phillip W Taylor"),
    14: ("9dd1d344-9994-5ea4-b22e-af95a2a41ef4", "Prentiss T Taylor"),
    15: ("e21e7798-ab38-54ca-a7b2-e07133fdf4cc", "Rawleigh W Taylor"),
    16: ("3778e767-0ebf-528d-ac11-03fb71134621", "Robert L Taylor"),
    17: ("3910749d-7a9e-53a9-b624-64b46bcf4bac", "Robert W Taylor"),
    18: ("dda141ab-cf75-57bb-9452-c63e5895db8e", "Roy L Taylor"),
    19: ("0f550df6-3515-5c5e-834c-93fcaea5ddd3", "Thomas R Taylor"),
    20: ("6390416d-1aa7-5a26-88a4-bc41ebf62699", "Vernon E Taylor"),
    21: ("8157c091-5fcf-571b-aa0c-da0e00d3c274", "Walter Taylor"),
    22: ("b3a97353-9e07-5c12-a7dd-dfec882ae56a", "William W Taylor"),
    23: ("a93e6139-511f-5b46-bf56-77cd1bb3c73b", "Francis M Tchitcherine"),
}


ARMY_OCCUPATIONS = [
    {"row": 1, "date": "1942-05-19", "code": "134", "occupation": "Shipping and receiving clerks", "public_occupation": "shipping and receiving clerk", "locator": "PDF physical page 171; historical category 1-34"},
    {"row": 4, "date": "1943-02-15", "code": "992", "occupation": "Students", "public_occupation": "student", "locator": "PDF physical page 304; amended historical category 9-92", "relationship": "student"},
    {"row": 5, "date": "1942-10-13", "code": "048", "occupation": "Draftsmen", "public_occupation": "draftsman", "locator": "PDF physical page 171; historical category 0-48"},
    {"row": 6, "date": "1941-10-14", "code": "849", "occupation": "Occupations in printing and publishing, n.e.c.", "public_occupation": "printing and publishing occupation, not elsewhere classified", "locator": "PDF physical page 173; historical category 8-49"},
    {"row": 12, "date": "1942-05-15", "code": "123", "occupation": "Messengers, errand boys, and office boys and girls", "public_occupation": "messenger, errand, and office-worker category", "locator": "PDF physical page 171; historical category 1-23"},
    {"row": 16, "date": "1942-10-31", "code": "760", "occupation": "Attendants, filling stations and parking lots", "public_occupation": "filling-station and parking-lot attendant", "locator": "PDF physical page 174; historical category 7-60"},
    {"row": 17, "date": "1942-11-07", "code": "699", "occupation": "Occupations in manufacture of radios and phonographs", "public_occupation": "radio and phonograph manufacturing occupation", "locator": "PDF physical page 174; historical category 6-99"},
    {"row": 20, "date": "1942-07-18", "code": "105", "occupation": "Clerks, general office", "public_occupation": "general office clerk", "locator": "PDF physical page 171; historical category 1-05"},
]


UNRESOLVED = {
    7: "Exact-name and institutional searches produced no defensible OSS, employer, occupation or archival identity bridge.",
    9: "Exact-name and middle-initial searches produced no defensible OSS, employer, occupation or archival identity bridge.",
    10: "No matching standard Army merged-file record or reliable OSS, employer, occupation or institutional bridge was found.",
    11: "Exact-name and middle-initial searches produced no defensible OSS, employer, occupation or archival identity bridge.",
    13: "Exact-name searches returned modern namesakes and postwar records without an OSS, protected-identifier or Box 767 bridge; they were rejected.",
    18: "The common name and absence of distinguishing public index data prevented a defensible identity or employment match.",
    21: "The common name and absence of distinguishing public index data prevented a defensible identity or employment match.",
    22: "Exact-name and middle-initial searches produced no defensible OSS, employer, occupation or archival identity bridge.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Box 767",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 462, rows 1-23; checked against layout-preserving text and a 300 dpi page render",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. Full protected identifiers remain private. Ivan M. Tchok on page 462 row 24 was checked as the next boundary.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; ten reviewed Batch 943 candidates; protected identifiers withheld",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "No raw bulk row or full protected identifier is retained in public assets. Nine identities were accepted; one middle-initial conflict remains explicit. Code 999 was not interpreted.",
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
            "access_date": "2026-10-28",
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
            "locator": "PDF physical pages 171, 173-174 and 304; reviewed historical categories 0-48, 1-05, 1-23, 1-34, 6-99, 7-60, 8-49 and 9-92",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical occupation labels identify neither employers nor workplaces. Undefined code 999 was not interpreted.",
        },
        {
            "key": RAWLEIGH_OSSOG,
            "stable_url": "https://ossog.info/italy/roanoke.html",
            "title": "Italy: Mission Roanoke",
            "author_creator": "OSS Operational Groups research project",
            "repository_publisher": "OSS Operational Groups",
            "locator": "Mission summary, personnel list, and source note identifying Capt. Rawleigh W. D. Taylor, Jr.",
            "access_date": "2026-10-28",
            "source_quality": "D_correlative_or_secondary",
            "collection_name": "OSS Operational Groups mission histories",
            "rights_notes": "The page states that its summary was compiled from end-of-mission reports of Capt. Taylor and 1st Lt. Gallaher retrieved from NARA. It supports identity, not a pre-OSS employer.",
        },
        {
            "key": RAWLEIGH_ISRAL,
            "stable_url": "https://www.isral.it/wp-content/uploads/2018/12/QSC20_lunati.pdf",
            "title": "L'Archivio del Fondo Materazzi",
            "author_creator": "Gabriele Lunati",
            "repository_publisher": "Istituto per la storia della resistenza e della società contemporanea in provincia di Alessandria (ISRAL)",
            "publication_record_date": "1996",
            "locator": "Quaderno di storia contemporanea, number 20, PDF physical page 1",
            "access_date": "2026-10-28",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Quaderno di storia contemporanea",
            "rights_notes": "The page was rendered at 200 dpi and visually inspected. It identifies Lt. Rawleigh W. D. Taylor as Roanoke commander, 7 March-17 May 1945, using an archive derived from NARA-held originals.",
        },
        {
            "key": RAWLEIGH_WOODBERRY,
            "stable_url": "https://www.woodberry.org/news-detail?pk=507520",
            "title": "Woodberry Dedicates Taylor Enclosure",
            "author_creator": "Woodberry Forest School",
            "repository_publisher": "Woodberry Forest School",
            "publication_record_date": "2009-10-13",
            "locator": "Opening paragraph identifying Rawleigh W. D. Taylor, Jr., class of 1938",
            "access_date": "2026-10-28",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Woodberry Forest School news",
            "rights_notes": "The rare full-name form and suffix align with the Roanoke personnel list. The page documents student/alumni status only, not employment.",
        },
        {
            "key": FRANCIS_CIA,
            "stable_url": "https://www.cia.gov/readingroom/docs/CIA-RDP13X00001R000100140007-2.pdf",
            "archival_identifier": "CIA-RDP13X00001R000100140007-2",
            "title": "Personnel Changes and Appointments for the Month of April 1944",
            "author_creator": "Office of Strategic Services",
            "repository_publisher": "Central Intelligence Agency Freedom of Information Act Electronic Reading Room",
            "publication_record_date": "1944",
            "locator": "Single-page personnel-changes document; CD Branch entry for Francis M. Tchitcherine",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "CIA FOIA OSS Collection",
            "document_number": "CIA-RDP13X00001R000100140007-2",
            "rights_notes": "The official document identifier and indexed full text were reviewed. A follow-up direct retrieval redirected to CIA system maintenance, so the profile requests a fresh direct check when service returns.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": WOODBERRY,
            "canonical_name": "Woodberry Forest School",
            "historical_name": "Woodberry Forest School",
            "aliases": ["Woodberry"],
            "organization_type": "secondary boarding school",
            "sector": "academia_and_research",
            "city": "Woodberry Forest",
            "state_or_region": "Virginia",
            "country": "United States",
            "normalization_notes": "Institutional name retained. Student attendance is modeled separately from employment.",
        }
    ]


def army_affiliation(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    name = PEOPLE[row][1]
    return {
        "key": f"{slug(name)}-occupation-b943",
        "person_id": PEOPLE[row][0],
        "occupation": item["public_occupation"],
        "relationship_type": item.get("relationship", "employment"),
        "end_date": item["date"],
        "date_precision": f"Historical civilian-occupation code {item['code']} was recorded at Army entry on {item['date']}; no employer, school, or OSS-transfer date is named.",
        "country": "United States",
        "immediate_pre_oss": False,
        "last_civilian_pre_service": False,
        "pre_oss_temporal_basis": "strongly_date_bounded",
        "identity_confidence": "high_confidence",
        "claim_confidence": "medium",
        "source_quality": "A_direct_official",
        "publication_status": "publish_qualified",
        "research_notes": "The historical category is not converted into a named employer, workplace, school, immediate affiliation, or exact modern job title.",
    }


def affiliations() -> list[dict[str, object]]:
    values = [army_affiliation(item) for item in ARMY_OCCUPATIONS]
    values.append(
        {
            "key": "rawleigh-taylor-woodberry-b943",
            "person_id": PEOPLE[15][0],
            "organization_key": WOODBERRY,
            "organization_name_as_found": "Woodberry Forest School",
            "role_title": "student; class of 1938",
            "relationship_type": "student",
            "end_date": "1938",
            "date_precision": "Woodberry Forest School identifies Rawleigh W. D. Taylor, Jr. as a member of the class of 1938; the page does not establish his later transition into military or OSS service.",
            "city": "Woodberry Forest",
            "state_or_region": "Virginia",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "published",
            "research_notes": "Published as a documented prewar student affiliation, never as an employer or immediate predecessor to OSS.",
        }
    )
    return values


def claim(row: int, key: str, claim_type: str, text: str, paraphrase: str, identity: str, temporal: str, quality: str, confidence: str, source_links: list[dict[str, object]], notes: str, affiliation_key: str | None = None, publication_status: str | None = None) -> dict[str, object]:
    result: dict[str, object] = {
        "key": key,
        "person_id": PEOPLE[row][0],
        "claim_type": claim_type,
        "claim_text": text,
        "evidence_paraphrase": paraphrase,
        "identity_match_assessment": identity,
        "temporal_assessment": temporal,
        "source_quality": quality,
        "claim_confidence": confidence,
        "publication_status": publication_status or ("published" if confidence in {"confirmed", "high"} else "publish_qualified"),
        "match_notes": notes,
        "sources": source_links,
    }
    if affiliation_key:
        result["affiliation_key"] = affiliation_key
    return result


def army_claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for item in ARMY_OCCUPATIONS:
        row = int(item["row"])
        name = PEOPLE[row][1]
        values.append(
            claim(
                row,
                f"identity-{slug(name)}-b943",
                "identity",
                f"The indexed {name} row is a high-confidence match to the reviewed official Army record.",
                "A nonshared protected identifier connects the visually verified index row to the official Army record, and the full name agrees exactly.",
                "High confidence from the private protected-identifier bridge and exact full-name agreement.",
                "The record supports identity and a dated occupation or student-status category but does not establish the OSS transfer sequence.",
                "A_direct_official",
                "high",
                [
                    {"source_key": INDEX, "locator_override": f"PDF page 462 row {row}; protected identifier withheld"},
                    {"source_key": ARMY, "locator_override": "Accepted reviewed identity bridge; protected identifier withheld"},
                ],
                "No protected identifier is exposed, and no employer, workplace or school is inferred from the identity bridge.",
            )
        )
        values.append(
            claim(
                row,
                f"occupation-{slug(name)}-b943",
                "occupation",
                f"At Army entry on {item['date']}, {name} was recorded in the historical {str(item['public_occupation']).lower()} category; no employer or institution is identified.",
                f"The accepted Army record carries civilian-occupation code {item['code']}, decoded from NARA's official code list.",
                "The category belongs only to the reviewed protected-identifier match; the identifier itself is not public.",
                "Strongly date-bounded to Army entry; it does not establish the immediate pre-OSS affiliation or a named employer or school.",
                "A_direct_official",
                "medium",
                [
                    {"source_key": ARMY, "locator_override": f"Accepted reviewed identity record; civilian occupation code {item['code']}; protected identifier withheld"},
                    {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46; Army-entry-date and civilian-occupation fields"},
                    {"source_key": CODES, "locator_override": item["locator"], "excerpt_override": item["occupation"]},
                ],
                "The historical category remains a qualified occupation or status lead, not an employer, workplace, institution or exact modern title.",
                f"{slug(name)}-occupation-b943",
            )
        )
    return values


def substantive_claims() -> list[dict[str, object]]:
    return [
        claim(
            8,
            "identity-leonard-p-taylor-b943",
            "identity",
            "The indexed Leonard P. Taylor row is a high-confidence match to the official Army record that prints the first name Lenord.",
            "A nonshared protected identifier connects the two records; the close first-name spelling disagreement is preserved as a documented variant.",
            "High confidence from the nonshared private identifier, matching surname and middle initial, and a close first-name spelling variant.",
            "The Army record supports identity and an entry date only; occupation code 999 is undefined and is not interpreted.",
            "A_direct_official",
            "high",
            [
                {"source_key": INDEX, "locator_override": "PDF page 462 row 8; protected identifier withheld"},
                {"source_key": ARMY, "locator_override": "Accepted reviewed identity record printing Lenord P Taylor; protected identifier withheld"},
                {"source_key": CODES, "support_type": "context_only", "locator_override": "Code 999 is not defined in the reviewed code list"},
            ],
            "The spelling variant is visible in the profile. No occupation or employer is transferred from undefined code 999.",
        ),
        claim(
            19,
            "conflict-thomas-r-taylor-army-b943",
            "identity",
            "The indexed Thomas R. Taylor row is not assigned to the reviewed Thomas W. Taylor Army record because the middle initials conflict.",
            "The protected identifier points to a closely matching Army record, but R and W are not silently reconciled.",
            "Conflicting despite the private identifier link because the middle initial is a material disagreement.",
            "No Army occupation, grade or affiliation is transferred until the personnel file resolves the discrepancy.",
            "A_direct_official",
            "conflicting",
            [
                {"source_key": INDEX, "locator_override": "PDF page 462 row 19; protected identifier withheld"},
                {"source_key": ARMY, "support_type": "contradicts", "locator_override": "Reviewed candidate prints Thomas W Taylor; protected identifier withheld"},
            ],
            "The candidate is preserved for review, not rejected or published as this person.",
            publication_status="conflicting",
        ),
        claim(
            15,
            "identity-rawleigh-w-taylor-b943",
            "identity",
            "Indexed Rawleigh W. Taylor is a high-confidence match to Capt. Rawleigh W. D. Taylor, Jr., commander of OSS Mission Roanoke.",
            "The rare name, middle initial, full-name expansion, suffix, officer status and direct OSS mission evidence converge across institutional and scholarly sources.",
            "High confidence from the distinctive rare name and mutually reinforcing full-name, school, military-rank and OSS-mission evidence.",
            "The sources document class-of-1938 status and an OSS Operational Group command in 1945, but not the immediate pre-OSS transition.",
            "B_authoritative_institutional",
            "high",
            [
                {"source_key": INDEX, "locator_override": "PDF page 462 row 15; protected identifier withheld"},
                {"source_key": RAWLEIGH_OSSOG, "locator_override": "Mission personnel list and NARA-based end-of-mission summary"},
                {"source_key": RAWLEIGH_ISRAL, "locator_override": "Quaderno di storia contemporanea 20, PDF physical page 1"},
                {"source_key": RAWLEIGH_WOODBERRY, "locator_override": "Opening paragraph identifying Rawleigh W. D. Taylor, Jr. '38"},
            ],
            "The full-name expansion is published as a documented variant. No civilian employer or unproven Army-to-OSS transfer is inferred.",
        ),
        claim(
            15,
            "prewar-rawleigh-taylor-woodberry-b943",
            "other_pre_oss_affiliation",
            "Rawleigh W. D. Taylor, Jr. was a student at Woodberry Forest School and belonged to the class of 1938.",
            "Woodberry Forest School identifies him as an alumnus in the class of 1938; the same rare full name identifies the Roanoke commander.",
            "High-confidence identity from the rare exact full name and suffix across the institutional school page and two OSS mission sources.",
            "Documented prewar student affiliation; not shown to be his immediate pre-OSS status and never classified as employment.",
            "B_authoritative_institutional",
            "high",
            [
                {"source_key": RAWLEIGH_WOODBERRY, "locator_override": "Opening paragraph", "excerpt_override": "Rawleigh W. D. Taylor, Jr. '38"},
                {"source_key": RAWLEIGH_OSSOG, "support_type": "context_only", "locator_override": "Mission personnel list naming Capt Rawleigh W.D. Taylor, Jr."},
                {"source_key": RAWLEIGH_ISRAL, "support_type": "context_only", "locator_override": "PDF physical page 1; Roanoke commander"},
            ],
            "Student status remains distinct from both employment and the unresolved immediate pathway into OSS.",
            "rawleigh-taylor-woodberry-b943",
        ),
        claim(
            23,
            "identity-francis-m-tchitcherine-b943",
            "identity",
            "Indexed Francis M. Tchitcherine is a high-confidence match to the OSS CD Branch administrator named in an official personnel-changes document.",
            "The distinctive exact full name appears in an official OSS personnel document appointing him chief of the Censorship Division and administrative officer in CD Branch.",
            "High confidence from the distinctive exact indexed name and a direct official OSS role document.",
            "The 1944 document establishes OSS identity and role, not a pre-OSS employer or earlier affiliation.",
            "A_direct_official",
            "high",
            [
                {"source_key": INDEX, "locator_override": "PDF page 462 row 23"},
                {"source_key": FRANCIS_CIA, "locator_override": "CD Branch personnel-change entry", "excerpt_override": "Mr. Francis M. Tchitcherine, presently on duty as Asst. Chief, Censorship Division"},
            ],
            "The CIA document's stable identifier is retained. Because the live CIA service redirected to maintenance on recheck, the next action requests direct retrieval when service returns.",
        ),
    ]


def archival_update(row: int, reason: str) -> dict[str, object]:
    person_id, name = PEOPLE[row]
    return {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, Box 767 and archive location 230/86/41/07. {reason}",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": "Review Box 767 for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }


def person_updates() -> list[dict[str, object]]:
    updates = [archival_update(row, reason) for row, reason in UNRESOLVED.items()]
    for row in (2, 3):
        updates.append(
            {
                "person_id": PEOPLE[row][0],
                "identity_status": "ambiguous",
                "identity_evidence": "The adjacent Box 767 rows both print John G. Taylor; one has a protected identifier and one does not. No public source or file evidence proves that they are the same person or identifies either row.",
                "manual_review_required": True,
                "possible_duplicate_group": "possible-duplicate:john-g-taylor-page462-rows2-3",
                "research_status": "conflicting_sources",
                "next_action": "Review both Box 767 files together and preserve the two source rows unless direct evidence establishes duplication or separates the identities.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            }
        )
    for item in ARMY_OCCUPATIONS:
        row = int(item["row"])
        updates.append(
            {
                "person_id": PEOPLE[row][0],
                "identity_status": "high_confidence",
                "identity_evidence": "A nonshared protected identifier connects the visually verified index row to the reviewed official Army record, and the full name agrees exactly.",
                "personnel_category": "enlisted_army_personnel",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "occupation_only_found",
                "next_action": "Review the indexed personnel file to establish the immediate pre-OSS affiliation and named last civilian employer; do not convert the Army occupation or student-status category into a workplace or institution.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            }
        )
    updates.extend(
        [
            {
                "person_id": PEOPLE[8][0],
                "identity_status": "high_confidence",
                "identity_evidence": "A nonshared protected identifier connects indexed Leonard P. Taylor to the Army record printing Lenord P. Taylor. The close spelling variant is preserved; undefined occupation code 999 is not interpreted.",
                "name_variants": ["Lenord P Taylor"],
                "personnel_category": "enlisted_army_personnel",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Review Box 767 to confirm the Leonard/Lenord spelling and establish the immediate pre-OSS affiliation and named civilian employer.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[14][0],
                "identity_status": "ambiguous",
                "identity_evidence": "The artist Prentiss Taylor is a plausible distinctive-name lead with documented prewar activity, but no official OSS, protected-identifier or Box 767 bridge connects that biography to indexed Prentiss T. Taylor.",
                "manual_review_required": True,
                "research_status": "needs_identity_review",
                "next_action": "Review Box 767 for a middle name, birth information, occupation or direct link before assigning the artist biography or any of its prewar affiliations.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[15][0],
                "identity_status": "high_confidence",
                "identity_evidence": "The rare indexed name aligns with Capt. Rawleigh W. D. Taylor, Jr. across a NARA-report-based mission history, an institutional historical article and Woodberry Forest School's class-of-1938 identification.",
                "name_variants": ["Rawleigh W. D. Taylor, Jr.", "Rawleigh William Downman Taylor Jr."],
                "personnel_category": "commissioned_army_officer",
                "commissioned_officer": True,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Review Box 767 and Virginia Military Institute records to establish the immediate pre-OSS military pathway and any civilian employer; Woodberry student status is not an employer.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[19][0],
                "identity_status": "conflicting",
                "identity_evidence": "A protected identifier points to a reviewed Thomas W. Taylor Army record, but the index prints Thomas R. Taylor. The material middle-initial conflict is preserved and no Army data are transferred.",
                "manual_review_required": True,
                "research_status": "conflicting_sources",
                "next_action": "Review the Box 767 personnel file and the Army source together to resolve the R/W middle-initial conflict before assigning any occupation or affiliation.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[23][0],
                "identity_status": "high_confidence",
                "identity_evidence": "The distinctive exact indexed name appears in an official OSS personnel-changes document naming Francis M. Tchitcherine as a CD Branch censorship and administrative officer.",
                "personnel_category": "civilian_professional_or_administrative_grade",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Retrieve the official CIA document again after maintenance and review Box 767 for pre-OSS employment, citizenship or government-service chronology.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
        ]
    )
    return updates


def research_attempts() -> list[dict[str, object]]:
    army_rows = {int(item["row"]) for item in ARMY_OCCUPATIONS}
    attempts: list[dict[str, object]] = []
    for row in sorted(PEOPLE):
        person_id, name = PEOPLE[row]
        if row in UNRESOLVED:
            outcome, reviewed, rejected, detail = "no_result", 7, 5, UNRESOLVED[row]
        elif row in (2, 3):
            outcome, reviewed, rejected, detail = "candidate_found", 8, 5, "The two adjacent John G. Taylor rows remain a possible duplicate group, but neither a name match nor the presence of a protected identifier in only one row proves identity or duplication."
        elif row in army_rows:
            outcome, reviewed, rejected, detail = "source_reviewed", 8, 4, "An accepted protected-identifier Army bridge supports identity and a dated historical occupation or student-status category, not an employer or institution."
        elif row == 8:
            outcome, reviewed, rejected, detail = "source_reviewed", 8, 4, "A nonshared protected identifier supports the Leonard/Lenord spelling variant. Undefined code 999 was not interpreted, and no employer was found."
        elif row == 14:
            outcome, reviewed, rejected, detail = "candidate_found", 9, 6, "Smithsonian and Library of Congress sources document the artist Prentiss Taylor, but no OSS, protected-identifier or Box 767 bridge assigns that biography to this indexed row."
        elif row == 15:
            outcome, reviewed, rejected, detail = "source_reviewed", 11, 4, "OSS Operational Groups, ISRAL and Woodberry evidence supports a high-confidence Rawleigh W. D. Taylor, Jr. identity and a prewar class-of-1938 student affiliation; the immediate pathway and last civilian employer remain unresolved."
        elif row == 19:
            outcome, reviewed, rejected, detail = "candidate_found", 8, 4, "The protected identifier points to Thomas W. Taylor, while the index prints Thomas R. Taylor; the conflict is preserved and no Army fields are transferred."
        elif row == 23:
            outcome, reviewed, rejected, detail = "source_reviewed", 10, 6, "An official OSS personnel-changes document supports the distinctive exact-name identity and CD Branch role. It does not identify a pre-OSS employer, and direct CIA retrieval was temporarily blocked by system maintenance on recheck."
        else:
            raise AssertionError(f"Missing Batch 943 outcome for row {row}")
        attempts.append(
            {
                "key": f"page462-row{row}-{slug(name)}-b943",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA index and public Archives context; CIA Reading Room; exact-name and meaningful variants; OSS, rank and military clues; employer and occupation 1940; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Box 767; protected identifiers used privately only when defensible",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_943",
                "started_at": "2026-10-28T16:30:00Z",
                "completed_at": "2026-10-28T20:15:00Z",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search snippets, family-tree assertions, modern people-finder pages, postwar-only leads and sources without an OSS, protected-identifier or Box-file bridge were not assigned.",
                "research_notes": f"{detail} The index page and admitted PDF pages were visually checked. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": "Review the indexed personnel file for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before military service.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b943-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-943-v1",
        "reviewer": "Before OSS Batch 943 evidence review",
        "sources": sources(),
        "organizations": organizations(),
        "affiliations": affiliations(),
        "claims": army_claims() + substantive_claims(),
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }
    EvidenceBundle.model_validate(bundle)
    OUTPUT.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
