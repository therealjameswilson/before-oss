#!/usr/bin/env python3
"""Generate the reviewed Batch 948 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page464-costas-a-theodorou-to-corcoran-thom-"
    "review_batch-948_2026-10-28.json"
)

INDEX = "nara-index-b948"
ARMY = "army-bulk-b948"
TECH = "army-tech-b948"
CODES = "army-codes-b948"
HOOVER_BOARD = "hoover-oss-board-mediterranean-b948"
OSSOG = "oss-operational-groups-personnel-b948"
WAPO_THOM = "washington-post-corcoran-thom-b948"

US_ARMY = "us-army-existing-b948"
ATHENS = "university-athens-existing-b948"
RIGGS = "riggs-national-bank-b948"


PEOPLE = {
    24: ("7f3c14f8-1069-50e5-a05a-0bc958ba9316", "Costas A Theodorou"),
    25: ("abafc141-5add-5adc-83dd-98e30147d32c", "Sotiris Theodorou"),
    26: ("d905ceb1-67b5-561e-b232-080b02cb81fc", "Terry Theodorou"),
    27: ("698e35ea-2c1b-5ef5-bbc1-0538dbae0ba2", "Adrien W Theriault"),
    28: ("962f7b23-23aa-5b3b-9257-dbb20201d3e8", "William A Theurer"),
    29: ("99f5be17-f251-59c3-9fc4-4272a1d96cea", "Ann Thibault"),
    30: ("c9c58a7a-a4e3-50e5-a0e2-c04202a59622", "John H Thibault"),
    31: ("6925ac26-afb4-5be7-8617-50269fb4dad6", "Joseph R Thibault"),
    32: ("d7423224-e9c0-5d09-8b06-43a512defa1c", "Raymond G Thibault"),
    33: ("52c9f309-7c41-5afa-a0c1-09dd7f99ab69", "Edison P Thibodeaux"),
    34: ("7e18000b-32d7-5c97-a54f-8bb955fc1eae", "Alphonse P Thiele"),
    35: ("e336d001-148e-529d-89c5-8f9ac23b9545", "Robert J Thiele"),
    36: ("6a895d08-e55a-5784-8715-52468002443f", "Charles G Thielicke"),
    37: ("d870f173-8868-5a38-8215-7fc2d30f3d5d", "Frank W Thielker"),
    38: ("2ed459bb-34ce-5960-91cb-d26cd4270e1d", "Robert J Thill"),
    39: ("dfb0fd93-2e00-5236-a792-87275fcb7c5e", "Annie Thinesse"),
    40: ("0b509df6-b304-5e0a-92b5-fc5086fd1073", "Bernice J Thiry"),
    41: ("5f3dfaeb-dabc-561c-b889-116698346e31", "Elinor H Thiry"),
    42: ("25c682d2-ac73-579c-9649-94922301241b", "Richard E Thistle"),
    43: ("b2a79e77-4935-54dd-9c61-df4ea777464d", "Paul Thole"),
    44: ("53f5f040-5e44-5067-a8b9-64902fd75d8c", "Lawrence C Tholey"),
    45: ("84de4a5d-043b-58d6-996a-5d23ff1f77df", "Calvin E Tholson"),
    46: ("4e994f47-5541-52d0-aba8-3fe93334198e", "Corcoran Thom"),
}


ARMY_RECORDS = [
    {"row": 24, "date": "1942-06-11", "code": "227", "occupation": "waiter or waitress, except private family", "label": "Waiters and waitresses, except private family", "locator": "PDF physical page 172; historical category 2-27"},
    {"row": 26, "date": "1942-08-10", "code": "001", "occupation": "accountant or auditor", "label": "Accountants and auditors", "locator": "PDF physical page 170; historical category 0-01"},
    {"row": 27, "date": "1944-03-20", "code": "475", "occupation": "machinist", "label": "Machinists", "locator": "PDF physical page 173; historical category 4-75"},
    {"row": 33, "date": "1943-02-26", "code": "993", "occupation": None, "label": None, "locator": None},
    {"row": 35, "date": "1942-10-24", "code": "048", "occupation": "draftsman", "label": "Draftsmen", "locator": "PDF physical page 171; historical category 0-48"},
    {"row": 44, "date": "1943-02-13", "code": "137", "occupation": "stenographer or typist", "label": "Stenographers and typists", "locator": "PDF physical page 171; historical category 1-37"},
    {"row": 45, "date": "1943-07-15", "code": "316", "occupation": "farm hand on a general farm", "label": "Farm hands, general farms", "locator": "PDF physical page 172; historical category 3-16"},
]


UNRESOLVED = {
    28: "Exact-name and variant searches produced unbridged namesakes but no defensible OSS identity or pre-OSS affiliation.",
    29: "Exact-name, institutional, obituary, newspaper and archival searches produced no reliable identity or employer bridge.",
    30: "Common-name results lacked the indexed middle initial, OSS context and a second corroborating identifier.",
    31: "Military and directory namesakes could not be connected to the indexed protected row or Box 771.",
    32: "Exact-name and military searches produced multiple namesakes without an OSS or Box-file bridge.",
    36: "Exact-name, military, institutional and obituary searches produced no reliable OSS identity or pre-OSS affiliation.",
    37: "Exact-name and spelling-variant searches produced no defensible identity or employment result.",
    38: "Common-name military and obituary candidates lacked a protected-identifier or OSS bridge and were rejected.",
    39: "A secondary account describes an OSS-connected French woman with this rare name, but the underlying official record and pre-OSS chronology remain unverified.",
    40: "Exact-name, obituary, institutional and archival searches produced no reliable identity or employer bridge.",
    41: "Exact-name and meaningful-variant searches produced no reliable OSS identity or pre-OSS affiliation.",
    42: "Common-name military and directory candidates lacked an OSS, Box 772 or protected-identifier bridge.",
    43: "A CIA Reading Room OCR hit was a false positive, and other exact-name results did not establish this indexed person.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 771-772",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 464, rows 24-46; checked against layout-preserving text and a 220 dpi page render",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. Costas A. Theodorou and Corcoran Thom were visually checked as the first and last boundaries; Robert Thomale on page 465 is the next record. Full protected identifiers remain private.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; seven reviewed Batch 948 candidates; protected identifiers withheld",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "No raw bulk row or full protected identifier is retained in public assets. Seven exact-name identities were accepted. Historical code 993 remains uninterpreted and unpublished.",
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
            "locator": "PDF physical pages 170-173; reviewed historical categories 0-01, 0-48, 1-37, 2-27, 3-16 and 4-75",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical occupation labels are qualified and never converted into named employers. Code 993 is not interpreted or published.",
        },
        {
            "key": HOOVER_BOARD,
            "stable_url": "https://digitalcollections.hoover.org/internal/media/dispatcher/331573/full",
            "archival_identifier": "Hoover Digital Collections media 331573",
            "title": "Office of Strategic Services Board proceedings examining Mediterranean-theater personnel",
            "author_creator": "Office of Strategic Services",
            "repository_publisher": "Hoover Institution Library & Archives",
            "publication_record_date": "1944-05-04 to 1944-05-24",
            "locator": "PDF physical page 39, A. P. Thiele; PDF physical page 58, Theodorou Sotiris",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "Office of Strategic Services records",
            "rights_notes": "Direct declassified OSS board proceedings. Protected service identifiers printed in the source are used privately for identity resolution and omitted from public text.",
        },
        {
            "key": OSSOG,
            "stable_url": "https://ossog.info/personnel.html",
            "title": "Office of Strategic Services Operational Groups: Personnel",
            "author_creator": "OSS Operational Groups research project",
            "repository_publisher": "OSS Operational Groups",
            "locator": "Greek Group II personnel roster; Costas A. Theodorou",
            "access_date": "2026-10-28",
            "source_quality": "D_correlative_or_secondary",
            "collection_name": "OSS Operational Groups histories",
            "rights_notes": "Used only as corroborative wartime identity context. It does not establish Costas Theodorou's pre-OSS occupation or immediate predecessor affiliation.",
        },
        {
            "key": WAPO_THOM,
            "stable_url": "https://www.washingtonpost.com/archive/local/1985/03/06/corcoran-thom-retired-riggs-executive-dies/53a9c54e-3d7f-4d39-83e6-278c41d00eab/",
            "title": "Corcoran Thom, Retired Riggs Executive, Dies",
            "author_creator": "The Washington Post",
            "repository_publisher": "The Washington Post",
            "publication_record_date": "1985-03-05",
            "locator": "Career and World War II service paragraphs",
            "access_date": "2026-10-28",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Washington Post obituary archive",
            "rights_notes": "The obituary supplies a 1928 Riggs career start and Army Air Forces combat-intelligence service. It does not itself describe OSS service or an Army-to-OSS transfer.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": US_ARMY,
            "organization_id": "28a26f92-78af-5a1a-9c09-a843eb5975b4",
            "canonical_name": "United States Army",
            "historical_name": "Army of the United States",
            "aliases": ["U.S. Army"],
            "organization_type": "military service",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "Existing canonical organization reused. Army service is modeled as military assignment, not civilian employment.",
        },
        {
            "key": ATHENS,
            "organization_id": "31f32f7f-e7dc-5c4b-a43f-38432dbcca53",
            "canonical_name": "National and Kapodistrian University of Athens",
            "historical_name": "University of Athens",
            "aliases": ["University of Athens"],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "Athens",
            "country": "Greece",
            "normalization_notes": "Existing university organization reused. Sotiris Theodorou's graduate status is student affiliation, not employment.",
        },
        {
            "key": RIGGS,
            "canonical_name": "Riggs National Bank",
            "historical_name": "Riggs National Bank",
            "aliases": ["Riggs"],
            "organization_type": "bank",
            "sector": "finance_and_banking",
            "city": "Washington",
            "state_or_region": "District of Columbia",
            "country": "United States",
            "active_dates": "1836-2005",
            "normalization_notes": "Historical bank name preserved. No modern successor is substituted for Corcoran Thom's prewar employer.",
        },
    ]


def army_affiliation(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    return {
        "key": f"{slug(PEOPLE[row][1])}-occupation-b948",
        "person_id": PEOPLE[row][0],
        "occupation": item["occupation"],
        "relationship_type": "employment",
        "end_date": item["date"],
        "date_precision": f"Historical civilian-occupation code {item['code']} was recorded at Army entry on {item['date']}; no employer, workplace or OSS-transfer date is named.",
        "country": "United States",
        "immediate_pre_oss": False,
        "last_civilian_pre_service": False,
        "pre_oss_temporal_basis": "strongly_date_bounded",
        "identity_confidence": "high_confidence",
        "claim_confidence": "medium",
        "source_quality": "A_direct_official",
        "publication_status": "publish_qualified",
        "research_notes": "The historical category is not converted into a named employer, workplace, immediate affiliation or exact modern job title.",
    }


def affiliations() -> list[dict[str, object]]:
    values = [army_affiliation(item) for item in ARMY_RECORDS if item["occupation"]]
    values.extend(
        [
            {
                "key": "sotiris-theodorou-army-b948",
                "person_id": PEOPLE[25][0],
                "organization_key": US_ARMY,
                "organization_name_as_found": "Army",
                "role_title": "Sergeant",
                "relationship_type": "military_assignment",
                "start_date": "1942-10",
                "end_date": "1943-10",
                "date_precision": "Month precision from the OSS board: Army entry in October 1942 and OSS assignment in October 1943.",
                "country": "United States",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "explicit_immediate",
                "identity_confidence": "high_confidence",
                "claim_confidence": "confirmed",
                "source_quality": "A_direct_official",
                "publication_status": "published",
                "research_notes": "The Army is an explicit military predecessor to OSS assignment, not a civilian employer.",
            },
            {
                "key": "sotiris-theodorou-civilian-occupation-b948",
                "person_id": PEOPLE[25][0],
                "occupation": "lawyer and contractor",
                "relationship_type": "employment",
                "end_date": "1942-10",
                "date_precision": "The May 1944 OSS board describes his civilian life before October 1942 Army entry; no employer, firm or exact dates are named.",
                "country": "Greece or United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "A_direct_official",
                "publication_status": "published",
                "research_notes": "Occupation only. Self-employment is not inferred, and no law firm, contracting business or client is invented.",
            },
            {
                "key": "sotiris-theodorou-athens-b948",
                "person_id": PEOPLE[25][0],
                "organization_key": ATHENS,
                "organization_name_as_found": "University of Athens",
                "relationship_type": "student",
                "date_precision": "The OSS board calls him a graduate; no attendance or degree dates are supplied.",
                "city": "Athens",
                "country": "Greece",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "A_direct_official",
                "publication_status": "published",
                "research_notes": "Student affiliation only; the university is not classified as his employer.",
            },
            {
                "key": "alphonse-thiele-army-b948",
                "person_id": PEOPLE[34][0],
                "organization_key": US_ARMY,
                "organization_name_as_found": "Army; Camp Mackall, North Carolina",
                "role_title": "Enlisted man; later second lieutenant",
                "relationship_type": "military_assignment",
                "start_date": "1940-10",
                "date_precision": "The OSS board states Army entry in October 1940 and explicit OSS recruitment for Special Operations from Camp Mackall; the recruitment date is not printed.",
                "city": "Camp Mackall",
                "state_or_region": "North Carolina",
                "country": "United States",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "explicit_immediate",
                "identity_confidence": "confirmed",
                "claim_confidence": "confirmed",
                "source_quality": "A_direct_official",
                "publication_status": "published",
                "research_notes": "The Army assignment is explicit and separate from his earlier civilian machinist occupation.",
            },
            {
                "key": "alphonse-thiele-machinist-b948",
                "person_id": PEOPLE[34][0],
                "occupation": "machinist",
                "relationship_type": "employment",
                "end_date": "1940-10",
                "date_precision": "The OSS board describes civilian life before October 1940 Army entry; no employer or exact dates are named.",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "confirmed",
                "claim_confidence": "confirmed",
                "source_quality": "A_direct_official",
                "publication_status": "published",
                "research_notes": "Occupation only. His light-aircraft pilot license is a qualification, not an employer or occupation claim.",
            },
            {
                "key": "corcoran-thom-riggs-b948",
                "person_id": PEOPLE[46][0],
                "organization_key": RIGGS,
                "organization_name_as_found": "Riggs National Bank",
                "role_title": "bank employee; later assistant branch manager and executive",
                "relationship_type": "employment",
                "start_date": "1928",
                "date_precision": "The obituary dates the career start to 1928 and places Army Air Forces service in World War II; it does not supply an exact mobilization or prewar employment end date.",
                "city": "Washington",
                "state_or_region": "District of Columbia",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "published",
                "research_notes": "Published as the last documented civilian employer before wartime service, not as an explicit immediate OSS predecessor.",
            },
        ]
    )
    return values


def claim(
    row: int,
    key: str,
    claim_type: str,
    text: str,
    paraphrase: str,
    identity: str,
    temporal: str,
    quality: str,
    confidence: str,
    source_links: list[dict[str, object]],
    notes: str,
    affiliation_key: str | None = None,
    publication_status: str | None = None,
) -> dict[str, object]:
    return {
        "key": key,
        "person_id": PEOPLE[row][0],
        "affiliation_key": affiliation_key,
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


def army_claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for item in ARMY_RECORDS:
        row = int(item["row"])
        name = PEOPLE[row][1]
        identity_sources = [
            {"source_key": INDEX, "locator_override": f"PDF page 464 row {row}; protected identifier withheld"},
            {"source_key": ARMY, "locator_override": "Reviewed exact-name record; protected identifier withheld"},
            {"source_key": TECH, "support_type": "context_only", "locator_override": "Field definitions, PDF physical pages 44-46"},
        ]
        if row == 24:
            identity_sources.append({"source_key": OSSOG, "support_type": "context_only", "locator_override": "Greek Group II personnel roster"})
        values.append(
            claim(
                row,
                f"identity-{slug(name)}-b948",
                "identity",
                f"The indexed {name} is a high-confidence match to the exact-name official Army enlistment record.",
                "A nonshared protected identifier connects the visually verified index row to the official Army record, and the full name agrees exactly.",
                "High confidence from a private nonshared identifier plus exact full-name agreement.",
                "The Army record dates entry into service; it does not establish the person's exact OSS transfer date.",
                "A_direct_official",
                "high",
                identity_sources,
                "This identity decision does not by itself establish a named employer or immediate OSS predecessor.",
            )
        )
        if item["occupation"]:
            values.append(
                claim(
                    row,
                    f"occupation-{slug(name)}-b948",
                    "occupation",
                    f"At Army entry on {item['date']}, {name}'s record carried the historical civilian-occupation category {item['label']}; no employer is named.",
                    f"The official bulk record supplies code {item['code']}; the visually reviewed NARA code list expands it as {item['label']}.",
                    "High confidence from the accepted protected-identifier bridge and exact name.",
                    "Strongly date-bounded at Army entry, but not shown to be the immediate pre-OSS affiliation.",
                    "A_direct_official",
                    "medium",
                    [
                        {"source_key": ARMY, "locator_override": f"Army entry {item['date']}; code {item['code']}; identifier withheld"},
                        {"source_key": CODES, "locator_override": item["locator"]},
                    ],
                    "Published only as a qualified historical occupation category. No workplace or named employer is inferred.",
                    f"{slug(name)}-occupation-b948",
                    "publish_qualified",
                )
            )
    return values


def substantive_claims() -> list[dict[str, object]]:
    return [
        claim(25, "identity-sotiris-theodorou-b948", "identity", "Indexed Sotiris Theodorou is a high-confidence match to the OSS board's Sergeant Theodorou Sotiris.", "The rare exact name, Army and OSS chronology, Greek-language context and Box 771 index placement align.", "High confidence from a rare exact name and direct original OSS personnel examination; the index row itself prints no protected identifier.", "The May 1944 board records October 1942 Army entry and October 1943 OSS assignment.", "A_direct_official", "high", [{"source_key": INDEX, "locator_override": "PDF page 464 row 25"}, {"source_key": HOOVER_BOARD, "locator_override": "PDF physical page 58; Theodorou Sotiris entry", "excerpt_override": "In civilian life, was a lawyer and contractor."}], "The public claim omits the service number printed in the board record."),
        claim(25, "immediate-sotiris-theodorou-army-b948", "immediate_pre_oss_affiliation", "Sotiris Theodorou's documented immediate pre-OSS affiliation was the United States Army.", "The OSS board dates his Army entry to October 1942 and assignment to OSS to October 1943.", "High-confidence rare-name identity from a direct OSS personnel examination.", "Explicit immediate Army-to-OSS sequence with month precision.", "A_direct_official", "confirmed", [{"source_key": HOOVER_BOARD, "locator_override": "PDF physical page 58; Army and OSS assignment chronology"}], "Modeled as a military assignment, not a civilian employer.", "sotiris-theodorou-army-b948"),
        claim(25, "civilian-sotiris-theodorou-b948", "last_civilian_pre_service", "Before Army service, Sotiris Theodorou was a lawyer and contractor; no employer or firm is named.", "The direct OSS board describes his civilian work and places it before October 1942 Army entry.", "High-confidence rare-name identity from the original OSS record.", "Strongly date-bounded as civilian work before Army entry; exact dates are absent.", "A_direct_official", "high", [{"source_key": HOOVER_BOARD, "locator_override": "PDF physical page 58; civilian-life sentence", "excerpt_override": "In civilian life, was a lawyer and contractor."}], "Self-employment and a named firm are not inferred.", "sotiris-theodorou-civilian-occupation-b948"),
        claim(25, "student-sotiris-theodorou-athens-b948", "other_pre_oss_affiliation", "Sotiris Theodorou was a graduate of the University of Athens.", "The OSS board explicitly describes him as a graduate of the University of Athens.", "High-confidence rare-name identity from the original OSS record.", "Documented prewar education; no dates are provided and it is not employment.", "A_direct_official", "high", [{"source_key": HOOVER_BOARD, "locator_override": "PDF physical page 58; education sentence"}], "Student affiliation is kept distinct from employer fields.", "sotiris-theodorou-athens-b948"),
        claim(34, "identity-alphonse-thiele-b948", "identity", "Indexed Alphonse P. Thiele is confirmed as OSS second lieutenant A. P. Thiele.", "The index and OSS board agree in initials and the same protected officer identifier; the board supplies Army and OSS chronology.", "Confirmed by a direct original OSS personnel examination and exact protected-identifier linkage.", "The board records Army entry, recruitment from Camp Mackall and May 1944 duties.", "A_direct_official", "confirmed", [{"source_key": INDEX, "locator_override": "PDF page 464 row 34; officer identifier withheld"}, {"source_key": HOOVER_BOARD, "locator_override": "PDF physical page 39; A. P. Thiele entry; identifier withheld", "excerpt_override": "Was machinist in civilian life and held pilot's licence for light aircraft."}], "The public claim masks the officer identifier and separates occupation from the pilot qualification."),
        claim(34, "immediate-alphonse-thiele-army-b948", "immediate_pre_oss_affiliation", "Alphonse P. Thiele's documented immediate pre-OSS affiliation was the United States Army at Camp Mackall, North Carolina.", "The OSS board says he entered the Army in October 1940 and was recruited by OSS for Special Operations from Camp Mackall.", "Confirmed exact person from the matching protected officer identifier.", "Explicit recruitment-from statement; the exact recruitment date is not printed.", "A_direct_official", "confirmed", [{"source_key": HOOVER_BOARD, "locator_override": "PDF physical page 39; Army entry and recruitment-from sentence"}], "Camp Mackall is preserved as the historical assignment location; the Army is not labeled a civilian employer.", "alphonse-thiele-army-b948"),
        claim(34, "civilian-alphonse-thiele-machinist-b948", "last_civilian_pre_service", "Before entering the Army, Alphonse P. Thiele was a machinist; no employer is named.", "The OSS board describes civilian machinist work and dates Army entry to October 1940.", "Confirmed exact person from the matching protected officer identifier.", "Strongly date-bounded before October 1940 Army entry; exact employment dates are absent.", "A_direct_official", "confirmed", [{"source_key": HOOVER_BOARD, "locator_override": "PDF physical page 39; civilian-life sentence", "excerpt_override": "Was machinist in civilian life."}], "His pilot license is not converted into employment or institutional affiliation.", "alphonse-thiele-machinist-b948"),
        claim(46, "identity-corcoran-thom-b948", "identity", "Indexed Corcoran Thom is a high-confidence match to banker and wartime Army Air Forces intelligence officer Corcoran Thom Jr.", "The distinctive exact name, compatible officer-style index record, Washington career and World War II intelligence service align.", "High confidence from the rare exact name, compatible wartime officer context and detailed institutional chronology; the obituary does not mention OSS.", "The obituary establishes prewar banking and wartime Army Air Forces service but not the OSS transfer.", "C_reputable_contemporary_or_scholarly", "high", [{"source_key": INDEX, "locator_override": "PDF page 464 row 46; protected identifier withheld"}, {"source_key": WAPO_THOM, "locator_override": "Career and World War II service paragraphs"}], "Published with an explicit qualification that the accessible obituary does not document the OSS link."),
        claim(46, "employer-corcoran-thom-riggs-b948", "last_civilian_pre_service", "Riggs National Bank is Corcoran Thom Jr.'s best-supported last civilian employer before World War II military service.", "The obituary states that he began at Riggs in 1928, then separately describes Army Air Forces combat-intelligence service during World War II.", "High-confidence rare-name identity with compatible wartime officer context.", "Strongly date-bounded prewar career, but not an explicit immediate OSS predecessor and without an exact mobilization date.", "C_reputable_contemporary_or_scholarly", "high", [{"source_key": WAPO_THOM, "locator_override": "Career and World War II service paragraphs", "excerpt_override": "Mr. Thom began his career with Riggs in 1928."}], "The claim is limited to last civilian employer before wartime service; it does not assert recruitment directly from Riggs into OSS.", "corcoran-thom-riggs-b948"),
    ]


def archival_update(row: int, reason: str) -> dict[str, object]:
    person_id, name = PEOPLE[row]
    box = "771" if row <= 32 else "772"
    return {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, Box {box} and archive location 230/86/42/01. {reason}",
        "personnel_category": "unknown_or_indeterminate",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": f"Review Box {box} for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }


def army_update(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    person_id, name = PEOPLE[row]
    return {
        "person_id": person_id,
        "identity_status": "high_confidence",
        "identity_evidence": f"A nonshared protected identifier and exact full name connect the visually verified {name} index row to the reviewed official Army record.",
        "personnel_category": "enlisted_army_personnel",
        "commissioned_officer": False,
        "allied_or_foreign_personnel": False,
        "manual_review_required": True,
        "research_status": "occupation_only_found" if item["occupation"] else "requires_archival_review",
        "next_action": "Review the indexed personnel file to establish the immediate pre-OSS affiliation and named last civilian employer; do not convert the Army code into a workplace." if item["occupation"] else "Review Box 772 to identify the immediate pre-OSS affiliation and last civilian employer. Historical code 993 remains uninterpreted and is not published.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }


def person_updates() -> list[dict[str, object]]:
    values = [archival_update(row, reason) for row, reason in UNRESOLVED.items()]
    values.extend(army_update(item) for item in ARMY_RECORDS)
    values.extend(
        [
            {
                "person_id": PEOPLE[25][0],
                "identity_status": "high_confidence",
                "identity_evidence": "A direct original OSS board examination aligns the rare exact name, Greek background, Army-to-OSS chronology and wartime assignment.",
                "name_variants": ["Theodorou Sotiris"],
                "personnel_category": "enlisted_army_personnel",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": True,
                "manual_review_required": True,
                "research_status": "verified_employer_found",
                "next_action": "Review Box 771 for the named law or contracting employer, exact pre-Army dates and citizenship or nationality details only when relevant to identity; do not publish sensitive data.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "medium",
            },
            {
                "person_id": PEOPLE[34][0],
                "identity_status": "confirmed",
                "identity_evidence": "The original OSS board and index share A. P. Thiele's protected officer identifier and initials; the board supplies full Army, OSS and civilian chronology.",
                "name_variants": ["A P Thiele"],
                "personnel_category": "commissioned_army_officer",
                "commissioned_officer": True,
                "allied_or_foreign_personnel": False,
                "manual_review_required": False,
                "research_status": "verified_employer_found",
                "next_action": "Optional Box 772 review may identify his civilian machinist employer and exact OSS recruitment date; no employer is inferred from occupation alone.",
                "personnel_file_digitized": True,
                "personnel_file_reviewed": True,
                "archival_review_priority": "low",
            },
            {
                "person_id": PEOPLE[46][0],
                "identity_status": "high_confidence",
                "identity_evidence": "The distinctive exact name, officer-style index entry, long Washington banking career and World War II Army Air Forces combat-intelligence service support Corcoran Thom Jr.; the obituary does not itself mention OSS.",
                "name_variants": ["Corcoran Thom Jr"],
                "personnel_category": "commissioned_army_officer",
                "commissioned_officer": True,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "verified_employer_found",
                "next_action": "Review Box 772 to confirm the exact Army Air Forces-to-OSS relationship and mobilization date. Riggs is established only as the last civilian employer before wartime service.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "medium",
            },
        ]
    )
    return values


def research_attempts() -> list[dict[str, object]]:
    army_rows = {int(item["row"]) for item in ARMY_RECORDS}
    attempts: list[dict[str, object]] = []
    for row in sorted(PEOPLE):
        person_id, name = PEOPLE[row]
        if row in UNRESOLVED:
            outcome, reviewed, rejected, detail = "no_result", 6, 6, UNRESOLVED[row]
        elif row in army_rows:
            outcome, reviewed, rejected, detail = "source_reviewed", 7, 5, "An accepted exact-name protected-identifier Army bridge supports identity and, when interpretable, a dated historical occupation category; it does not name an employer or immediate OSS affiliation."
        elif row == 25:
            outcome, reviewed, rejected, detail = "source_reviewed", 10, 4, "A direct OSS board examination establishes the Army-to-OSS sequence, civilian lawyer-and-contractor occupation and University of Athens graduate status."
        elif row == 34:
            outcome, reviewed, rejected, detail = "source_reviewed", 10, 3, "A direct OSS board examination and matching protected officer identifier confirm identity, recruitment from the Army at Camp Mackall and civilian machinist occupation."
        elif row == 46:
            outcome, reviewed, rejected, detail = "source_reviewed", 9, 5, "A reputable obituary establishes the rare-name banker's 1928 Riggs career start and wartime Army Air Forces combat-intelligence service; the OSS link remains for Box-file verification."
        else:
            raise AssertionError(f"Missing Batch 948 outcome for row {row}")
        attempts.append(
            {
                "key": f"page464-row{row}-{slug(name)}-b948",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index and public Archives context; CIA Reading Room or equivalent official-source check; exact-name and meaningful variants; OSS and military clues; employer and occupation 1940; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Boxes 771-772; protected identifiers used privately only when defensible",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_948",
                "started_at": "2026-10-28T14:00:00Z",
                "completed_at": "2026-10-28T16:30:00Z",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search snippets, family-tree assertions, discovery-only secondary claims, modern people-finder pages, postwar-only leads and sources without an OSS, protected-identifier or Box-file bridge were not assigned.",
                "research_notes": f"{detail} The index page and admitted Army, code-list, official, institutional or newspaper pages were checked where applicable. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": "Review the indexed personnel file for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before wartime service.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b948-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-948-v1",
        "reviewer": "Before OSS Batch 948 evidence review",
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
