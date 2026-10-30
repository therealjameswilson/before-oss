#!/usr/bin/env python3
"""Generate the reviewed Batch 971 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page476-olive-turner-to-edgar-twamley-"
    "review_batch-971_2026-10-30.json"
)

INDEX = "nara-index-b971"
ARMY = "army-bulk-b971"
TECH = "army-tech-b971"
CODES = "army-codes-b971"
NARA_TURQUET = "nara-turquet-awards-b971"
OLYMPEDIA_TURQUET = "olympedia-turquet-b971"
BC_TWAMLEY_1944 = "broadcasting-twamley-1944-b971"
BC_TWAMLEY_1945 = "broadcasting-twamley-1945-b971"

RAMC = "royal-army-medical-corps-b971"
WBEN = "wben-inc-b971"
NBC = "national-broadcasting-company-existing-b971"


PEOPLE = {
    1: ("29257549-20a2-519d-858e-65d3eb00ddc2", "Olive J Turner"),
    2: ("0eebd349-e415-5ab5-ae7a-c417e0d35a0e", "Oscar Turner"),
    3: ("ece51c24-29cf-55ea-a9c2-dc04418d82fa", "Robert A Turner"),
    4: ("361649a6-a65b-54fe-885d-cd221d8ddf0d", "Robert E Turner"),
    5: ("ca63ec77-3678-579d-b108-0c42339f3618", "Vernon R Turner"),
    6: ("76723c8e-f874-5f8d-99c5-c49b694f053c", "Wilmore J Turner"),
    7: ("18814fea-530b-54a0-b9b9-95796b9c7e5b", "Willison H Turney"),
    8: ("0de56684-395c-5d73-9852-dd5badbae081", "Norman R Turpin"),
    9: ("496bbce6-47da-55c9-aeed-65f4617ff538", "Robert G Turpin"),
    10: ("eeb98a02-d488-5656-9ebd-bcd1888908dd", "Sara Turpin"),
    11: ("91d98415-0ab9-5ae7-ad47-eb25417b9efa", "Pierre M Turquet"),
    12: ("30a89768-a52e-545c-8ec8-a5c450017a3e", "William A Turrell"),
    13: ("92055f33-0141-56b2-bd86-56f59bddfcc2", "Cipriano E Turri"),
    14: ("3f2a6b2e-dcf5-515a-94f3-a1ae05e54772", "Carl F Turvey"),
    15: ("052bcbc9-333c-58c7-a951-397c3184ada3", "Wladyslaw Turzecki"),
    16: ("63e62b1e-f409-5fbc-9c2f-d35a61acab50", "Everett D Tutor"),
    17: ("75832d36-db7c-5fc4-a832-7c6d46963459", "Hiram D Tuttle"),
    18: ("e731c885-b01a-5dc9-8732-01ed4f9d6bc2", "Kenneth D Tuttle"),
    19: ("07162a59-8b5f-5c63-9f05-5d4159a63090", "Shirley R Tutun"),
    20: ("3c67dcdf-554f-56fa-b1ff-0c60867058a9", "Catherine B Tuvo"),
    21: ("552d5697-fe1f-5db4-9650-fcbeefc6ea7b", "Albert Tversky"),
    22: ("3f8f78f8-9de6-577e-a77e-f983172f1c1e", "Arnold E Tvinnerain"),
    23: ("3b47a877-c697-51bb-ba4b-6d5a2e688501", "Edgar H Twamley"),
}


ARMY_OCCUPATIONS = [
    {
        "row": 5,
        "date": "1943-05-20",
        "code": "098",
        "occupation": "Managers and officials, not elsewhere classified",
        "public_occupation": "manager or official, not elsewhere classified",
        "locator": "Historical category 0-98; managers and officials, n.e.c.",
    },
    {
        "row": 7,
        "date": "1943-06-28",
        "code": "649",
        "occupation": "Semiskilled occupations in printing and publishing, not elsewhere classified",
        "public_occupation": "semiskilled printing or publishing worker, not elsewhere classified",
        "locator": "Historical category 6-49; printing and publishing, n.e.c.",
    },
    {
        "row": 18,
        "date": "1942-12-09",
        "code": "430",
        "occupation": "Lumbermen, raftsmen, and woodchoppers",
        "public_occupation": "lumberman, raftsman or woodchopper",
        "locator": "Historical category 4-30; lumbermen, raftsmen and woodchoppers",
    },
    {
        "row": 21,
        "date": "1942-10-10",
        "code": "105",
        "occupation": "Clerks, general office",
        "public_occupation": "general-office clerk",
        "locator": "Historical category 1-05; clerks, general office",
    },
]


IDENTITY_ONLY = {
    13: {
        "date": "1943-05-17",
        "note": "The exact indexed full name and a nonshared protected identifier agree with the reviewed official Army row. Historical code 993 was not decoded.",
    },
    16: {
        "date": "1942-11-17",
        "note": "The exact indexed full name and a nonshared protected identifier agree with the reviewed official Army row. Historical code 358 was not decoded.",
    },
    17: {
        "date": "1945-12-21",
        "note": "The exact indexed full name and a nonshared protected identifier agree with the reviewed official Army row. The entry date follows OSS dissolution and code 055 was not decoded.",
    },
}


UNRESOLVED = {
    1: "Name-only searches produced multiple plausible namesakes without a second identifier or dated OSS context.",
    2: "A 1943 NBC and Office of War Information broadcasting candidate was rejected because no source bridged that Oscar Turner to Box 790 or OSS.",
    3: "The common name produced multiple namesakes without two corroborating identifiers beyond the name.",
    4: "The common name produced multiple namesakes without two corroborating identifiers beyond the name.",
    8: "Exact-name and variant searches produced no defensible identity bridge to Box 790 or OSS.",
    9: "The common name produced multiple namesakes without two corroborating identifiers beyond the name.",
    10: "Name-only searches produced multiple plausible namesakes without a second identifier or dated OSS context.",
    12: "Exact-name, initial, OSS, employer, occupation, obituary, institutional and archival searches produced no defensible identity bridge.",
    14: "Exact-name, initial, OSS, employer, occupation, obituary, institutional and archival searches produced no defensible identity bridge.",
    15: "Foreign-name and transliteration searches produced no source that bridged the indexed spelling to Box 790 or OSS.",
    19: "Exact-name and variant searches produced no defensible identity bridge to Box 790 or OSS.",
    20: "Exact-name and variant searches produced no defensible identity bridge to Box 790 or OSS.",
    22: "Exact-name, variant and Scandinavian-name searches produced no defensible identity bridge to Box 790 or OSS.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def box_for(row: int) -> str:
    return "789" if row == 6 else "790"


def army_identity_note(row: int) -> str:
    if row in IDENTITY_ONLY:
        return str(IDENTITY_ONLY[row]["note"])
    return (
        "The exact indexed full name and a nonshared protected identifier agree with the reviewed official Army row."
    )


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 789-790",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 476, rows 1-23; checked against layout-preserving text and an original-detail page render",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. Protected identifiers remain private.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; seven accepted Batch 971 identity comparisons and one retained conflict; protected identifiers and record ordinals withheld",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "No raw bulk row, record ordinal or full protected identifier enters the evidence bundle or public assets.",
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
            "access_date": "2026-10-30",
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
            "locator": "PDF physical pages 171, 173 and 174; four Batch 971 categories visually and textually checked",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical categories identify neither employers nor workplaces and are retained only where needed for auditability.",
        },
        {
            "key": NARA_TURQUET,
            "stable_url": "https://www.archives.gov/files/research/jfk/releases/104-10165-10120.pdf",
            "archival_identifier": "Record Number 104-10165-10120",
            "title": "BARKS/FLYERS; PARIS - SECT. 2D.1 (CHEV, L.)",
            "author_creator": "Headquarters Detachment, Office of Strategic Services, European Theater of Operations",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1944-1945",
            "locator": "PDF physical pages 5-6 (handwritten pages 119-120); 1 July 1945 minutes and 26 June 1945 awards-board attachment; rendered, OCR-located and visually inspected",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "JFK Assassination Records Collection; OSS awards and decorations records",
            "document_number": "104-10165-10120",
            "rights_notes": "The official scan establishes the exact name, major rank, British Army status and OSS Secret Intelligence branch context, not a pre-OSS employer.",
        },
        {
            "key": OLYMPEDIA_TURQUET,
            "stable_url": "https://www.olympedia.org/athletes/22203",
            "title": "Pierre Turquet",
            "author_creator": "Olympedia contributors",
            "repository_publisher": "Olympedia",
            "locator": "Biographical information and biography; full name, education, medical training and Royal Army Medical Corps service",
            "access_date": "2026-10-30",
            "source_quality": "D_correlative_or_secondary",
            "collection_name": "Olympedia athlete biographies",
            "rights_notes": "Used with the original OSS record only for a qualified identity and RAMC wartime-affiliation assessment; no immediate sequence is inferred.",
        },
        {
            "key": BC_TWAMLEY_1944,
            "stable_url": "https://www.worldradiohistory.com/Archive-All-BC/Broadcasting-Magazine/BC-1944/1944-09-25-BC.pdf",
            "title": "Thompson Heads WBEN As Twamley Successor",
            "author_creator": "Broadcasting magazine",
            "repository_publisher": "Broadcasting Publications, Inc.; World Radio History scan",
            "publication_record_date": "1944-09-25",
            "locator": "Printed page 70; full indexed article text reviewed",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Broadcasting magazine archive",
            "rights_notes": "Only short excerpts and project-authored paraphrases are retained.",
        },
        {
            "key": BC_TWAMLEY_1945,
            "stable_url": "https://www.worldradiohistory.com/Archive-All-BC/Broadcasting-Magazine/BC-1945/1945-07-23-BC.pdf",
            "title": "Broadcasting, July 23, 1945",
            "author_creator": "Broadcasting magazine",
            "repository_publisher": "Broadcasting Publications, Inc.; World Radio History scan",
            "publication_record_date": "1945-07-23",
            "locator": "Printed page 3; personnel item naming Edgar H. Twamley, WBEN and the Office of Strategic Services; full indexed page text reviewed",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Broadcasting magazine archive",
            "rights_notes": "Only a short excerpt and project-authored paraphrase are retained.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": RAMC,
            "canonical_name": "Royal Army Medical Corps",
            "historical_name": "Royal Army Medical Corps",
            "aliases": ["RAMC"],
            "organization_type": "British Army medical corps",
            "sector": "military",
            "country": "United Kingdom",
            "active_dates": "1898-present",
            "normalization_notes": "The corps is kept distinct from the British Army as a whole. The reviewed evidence supports a qualified wartime assignment but not its sequence relative to OSS.",
        },
        {
            "key": WBEN,
            "canonical_name": "WBEN Inc.",
            "historical_name": "WBEN Inc.",
            "aliases": ["WBEN", "WBEN Buffalo"],
            "organization_type": "radio station licensee",
            "sector": "journalism_and_media",
            "city": "Buffalo",
            "state_or_region": "New York",
            "country": "United States",
            "active_dates": "Documented during Edgar H. Twamley's 1932-1944 tenure",
            "normalization_notes": "The historical company and call sign are preserved as printed. It is not silently replaced by a modern successor or current station owner.",
        },
        {
            "key": NBC,
            "organization_id": "f8b54577-fc09-5c6a-9b36-d68aee691c07",
            "canonical_name": "National Broadcasting Company",
            "historical_name": "National Broadcasting Company",
            "aliases": ["NBC"],
            "organization_type": "radio network",
            "sector": "journalism_and_media",
            "country": "United States",
            "normalization_notes": "Historical network name preserved. This record is reused from the canonical organizations table.",
        },
    ]


def occupation_affiliation(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    name = PEOPLE[row][1]
    return {
        "key": f"{slug(name)}-occupation-b971",
        "person_id": PEOPLE[row][0],
        "occupation": item["public_occupation"],
        "relationship_type": "unknown",
        "end_date": item["date"],
        "date_precision": f"Historical civilian-occupation code {item['code']} was recorded at Army entry on {item['date']}; no employer, workplace or OSS-transfer date is named.",
        "country": "United States",
        "immediate_pre_oss": False,
        "last_civilian_pre_service": False,
        "pre_oss_temporal_basis": "documented_prewar",
        "identity_confidence": "high_confidence",
        "claim_confidence": "medium",
        "source_quality": "A_direct_official",
        "publication_status": "publish_qualified",
        "research_notes": "Occupation only. The historical category is not a named employer or institution and is excluded from verified-employer analytics.",
    }


def affiliations() -> list[dict[str, object]]:
    values = [occupation_affiliation(item) for item in ARMY_OCCUPATIONS]
    values.extend(
        [
            {
                "key": "pierre-turquet-ramc-b971",
                "person_id": PEOPLE[11][0],
                "organization_key": RAMC,
                "organization_name_as_found": "Royal Army Medical Corps (RAMC)",
                "role_title": "Major",
                "occupation": "medical officer",
                "relationship_type": "military_assignment",
                "date_precision": "Second World War; the exact start, end and sequence relative to OSS Secret Intelligence are not established",
                "country": "United Kingdom",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "temporal_relation_uncertain",
                "identity_confidence": "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "D_correlative_or_secondary",
                "publication_status": "publish_qualified",
                "research_notes": "The official OSS record confirms the exact name, major rank, British Army status and SI branch; Olympedia supplies the RAMC affiliation. Neither establishes an immediate-pre-OSS transfer sequence.",
            },
            {
                "key": "edgar-twamley-wben-b971",
                "person_id": PEOPLE[23][0],
                "organization_key": WBEN,
                "organization_name_as_found": "WBEN Inc.",
                "role_title": "station director",
                "occupation": "radio station executive",
                "relationship_type": "employment",
                "start_date": "1932",
                "end_date": "1944-09",
                "date_precision": "The contemporary September 1944 article says Twamley had been with WBEN since 1932 and left for confidential overseas government service; a July 1945 item identifies his recent service as OSS.",
                "city": "Buffalo",
                "state_or_region": "New York",
                "country": "United States",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "published",
                "research_notes": "Two contemporary trade-journal items connect the same distinctive exact name, WBEN role, overseas government departure and later explicit OSS service. No military cover status is relabeled as civilian employment.",
            },
            {
                "key": "edgar-twamley-nbc-b971",
                "person_id": PEOPLE[23][0],
                "organization_key": NBC,
                "organization_name_as_found": "NBC",
                "role_title": "station relations staff",
                "relationship_type": "employment",
                "end_date": "1932",
                "date_precision": "The September 1944 article says he worked on NBC's station relations staff before joining WBEN in 1932; exact dates are not supplied.",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "published",
                "research_notes": "Earlier documented employment, kept separate from the immediate/last-civilian WBEN affiliation.",
            },
        ]
    )
    return values


def claim(
    row: int,
    key: str,
    claim_type: str,
    claim_text: str,
    evidence_paraphrase: str,
    identity_assessment: str,
    temporal_assessment: str,
    source_quality: str,
    confidence: str,
    source_links: list[dict[str, str]],
    notes: str,
    affiliation_key: str | None = None,
    publication_status: str = "published",
    evidence_excerpt: str | None = None,
) -> dict[str, object]:
    value: dict[str, object] = {
        "key": key,
        "person_id": PEOPLE[row][0],
        "claim_type": claim_type,
        "claim_text": claim_text,
        "evidence_paraphrase": evidence_paraphrase,
        "identity_match_assessment": identity_assessment,
        "temporal_assessment": temporal_assessment,
        "source_quality": source_quality,
        "claim_confidence": confidence,
        "publication_status": publication_status,
        "match_notes": notes,
        "sources": source_links,
    }
    if affiliation_key:
        value["affiliation_key"] = affiliation_key
    if evidence_excerpt:
        value["evidence_excerpt"] = evidence_excerpt
    return value


def army_claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    rows = [int(item["row"]) for item in ARMY_OCCUPATIONS] + list(IDENTITY_ONLY)
    for row in rows:
        name = PEOPLE[row][1]
        note = army_identity_note(row)
        date = next(
            (str(item["date"]) for item in ARMY_OCCUPATIONS if item["row"] == row),
            str(IDENTITY_ONLY.get(row, {}).get("date", "")),
        )
        values.append(
            claim(
                row,
                f"identity-{slug(name)}-b971",
                "identity",
                f"Indexed {name} is high-confidence matched to a reviewed official Army record.",
                note,
                note,
                f"The official Army entry date is {date}; it establishes military-entry chronology but not the exact OSS transfer date.",
                "A_direct_official",
                "high",
                [{"source_key": INDEX}, {"source_key": ARMY}, {"source_key": TECH}],
                "Protected identifiers were used only for private resolution and remain absent from the evidence bundle and public output.",
            )
        )

    for item in ARMY_OCCUPATIONS:
        row = int(item["row"])
        name = PEOPLE[row][1]
        values.append(
            claim(
                row,
                f"occupation-{slug(name)}-b971",
                "occupation",
                f"At Army entry on {item['date']}, {name}'s historical civilian-occupation category was {str(item['occupation']).lower()}.",
                f"The official Army field carries historical code {item['code']}; NARA's code list defines it as {item['occupation']}.",
                army_identity_note(row),
                "Dated at Army entry before the later OSS-index context; no employer, workplace or exact OSS-transfer date is named.",
                "A_direct_official",
                "medium",
                [
                    {"source_key": ARMY, "locator_override": "Accepted identity bridge; protected identifier and raw record withheld"},
                    {"source_key": TECH, "locator_override": "PDF physical pages 44-46; civilian-occupation field"},
                    {"source_key": CODES, "locator_override": str(item["locator"])},
                ],
                "Published as qualified occupation only; excluded from verified-employer analytics.",
                f"{slug(name)}-occupation-b971",
                "publish_qualified",
            )
        )
    return values


def special_claims() -> list[dict[str, object]]:
    return [
        claim(
            6,
            "identity-conflict-wilmore-turner-b971",
            "identity",
            "The protected identifier on indexed Wilmore J Turner leads to an Army row printed as Turner J W; the identity remains conflicting.",
            "The protected identifier agrees, but the official Army name reverses the initials and omits the indexed given name Wilmore.",
            "Conflicting: a strong identifier bridge is offset by a substantive name disagreement that the personnel file must resolve.",
            "The Army entry is dated 21 January 1942, but no occupation or chronology is assigned to the indexed person while identity remains disputed.",
            "A_direct_official",
            "conflicting",
            [{"source_key": INDEX}, {"source_key": ARMY}, {"source_key": TECH}],
            "The records remain separate; the Army occupation is not transferred and no public employer fact is created.",
            publication_status="conflicting",
        ),
        claim(
            11,
            "identity-pierre-turquet-b971",
            "identity",
            "Indexed Pierre M Turquet is a high-confidence match to British Army Major Pierre M. Turquet of OSS Secret Intelligence.",
            "An original OSS awards-board attachment identifies the exact uncommon name, middle initial, major rank, British Army status and SI branch.",
            "High confidence based on the uncommon exact name and middle initial in a direct OSS record, reinforced by a compatible British wartime biography.",
            "The award-board attachment is dated 26 June 1945; it establishes wartime OSS and British Army context, not a pre-OSS employer or accession date.",
            "A_direct_official",
            "high",
            [
                {"source_key": INDEX},
                {"source_key": NARA_TURQUET, "excerpt_override": "Maj Pierre M. Turquet, Br. Army"},
                {"source_key": OLYMPEDIA_TURQUET, "support_type": "context_only"},
            ],
            "The profile distinguishes Allied military personnel from U.S. OSS employment and does not infer an immediate-pre-OSS sequence.",
            evidence_excerpt="Maj Pierre M. Turquet, Br. Army",
        ),
        claim(
            11,
            "affiliation-pierre-turquet-ramc-b971",
            "other_pre_oss_affiliation",
            "A high-confidence Pierre M. Turquet identity served as a Royal Army Medical Corps major during the Second World War.",
            "Olympedia identifies Pierre Maurice Turquet as a RAMC major; the original OSS record independently identifies Major Pierre M. Turquet of the British Army in SI.",
            "High-confidence identity from the direct OSS record; the RAMC detail comes from a reputable specialist biography and remains qualified.",
            "Documented wartime affiliation, but its sequence relative to OSS Secret Intelligence is uncertain and it is not labeled immediate pre-OSS.",
            "D_correlative_or_secondary",
            "medium",
            [
                {"source_key": NARA_TURQUET, "excerpt_override": "Maj Pierre M. Turquet, Br. Army"},
                {"source_key": OLYMPEDIA_TURQUET, "excerpt_override": "He served in the Royal Army Medical Corps (RAMC) as a major in World War II"},
            ],
            "Published as a qualified military assignment, not civilian employment, and excluded from verified-employer analytics.",
            "pierre-turquet-ramc-b971",
            "publish_qualified",
        ),
        claim(
            23,
            "identity-edgar-twamley-b971",
            "identity",
            "Indexed Edgar H Twamley is high-confidence matched to the WBEN station director who served with OSS.",
            "Two contemporary Broadcasting items repeat the distinctive exact name and WBEN role; the July 1945 item explicitly states recent Office of Strategic Services service.",
            "High confidence from a distinctive exact full-name and middle-initial match, continuous WBEN role, and explicit contemporaneous OSS statement.",
            "The articles document departure in September 1944 and recent OSS service in July 1945.",
            "C_reputable_contemporary_or_scholarly",
            "high",
            [
                {"source_key": INDEX},
                {"source_key": BC_TWAMLEY_1944},
                {"source_key": BC_TWAMLEY_1945, "excerpt_override": "former director of WBEN Buffalo, and recently in the Office of Strategic Services"},
            ],
            "The direct contemporaneous OSS statement bridges the index to the same rare-name radio executive without importing unrelated postwar career details.",
            evidence_excerpt="former director of WBEN Buffalo, and recently in the Office of Strategic Services",
        ),
        claim(
            23,
            "immediate-edgar-twamley-wben-b971",
            "immediate_pre_oss_affiliation",
            "Edgar H. Twamley's best-supported immediate civilian affiliation before OSS was station director at WBEN Inc. in Buffalo.",
            "A September 1944 article says the station director left WBEN for confidential overseas government service; a July 1945 item identifies his recent service as OSS.",
            "High-confidence distinctive exact-name match across two contemporary issues and the NARA index.",
            "Strongly date-bounded: the sources connect the WBEN departure in September 1944 to overseas government service and later identify that service as OSS.",
            "C_reputable_contemporary_or_scholarly",
            "high",
            [
                {"source_key": BC_TWAMLEY_1944, "excerpt_override": "has accepted a confidential overseas assignment"},
                {"source_key": BC_TWAMLEY_1945, "excerpt_override": "recently in the Office of Strategic Services"},
            ],
            "The claim is framed as the immediate civilian affiliation; the accessible sources do not establish whether an Army administrative status intervened or overlapped.",
            "edgar-twamley-wben-b971",
        ),
        claim(
            23,
            "last-civilian-edgar-twamley-wben-b971",
            "last_civilian_pre_service",
            "WBEN Inc. is Edgar H. Twamley's last documented civilian employer before his overseas government and OSS service.",
            "The contemporary succession notice says he had worked at WBEN since 1932 and was leaving the station for overseas government service.",
            "High-confidence distinctive exact-name match, reinforced by the subsequent explicit OSS statement.",
            "Strongly date-bounded as the final named civilian employment immediately before the September 1944 departure.",
            "C_reputable_contemporary_or_scholarly",
            "high",
            [
                {"source_key": BC_TWAMLEY_1944, "excerpt_override": "has been with WBEN since 1932"},
                {"source_key": BC_TWAMLEY_1945, "support_type": "context_only"},
            ],
            "Kept separate from both OSS service and earlier NBC employment.",
            "edgar-twamley-wben-b971",
        ),
        claim(
            23,
            "earlier-edgar-twamley-nbc-b971",
            "other_pre_oss_affiliation",
            "Before joining WBEN in 1932, Edgar H. Twamley worked on NBC's station relations staff.",
            "The September 1944 contemporary profile explicitly places the NBC station-relations job before his 1932 WBEN tenure.",
            "High-confidence match through the same distinctive exact-name WBEN and OSS chronology.",
            "Explicitly earlier than WBEN and therefore documented prewar employment, not the immediate predecessor to OSS.",
            "C_reputable_contemporary_or_scholarly",
            "high",
            [{"source_key": BC_TWAMLEY_1944}],
            "Modeled separately so an earlier employer is not conflated with the last civilian employer.",
            "edgar-twamley-nbc-b971",
        ),
    ]


def claims() -> list[dict[str, object]]:
    return army_claims() + special_claims()


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
            identity_evidence=f"The visually verified index row supplies {PEOPLE[row][1]}, Box {box_for(row)} and archive location 230/86/42/03. {reason}",
            personnel_category="unknown_or_indeterminate",
            commissioned_officer=None,
            allied_or_foreign_personnel=None,
            research_status="requires_archival_review",
            next_action=f"Review Box {box_for(row)} for corroborating identifiers, immediate pre-OSS affiliation and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}",
        )
        for row, reason in UNRESOLVED.items()
    ]

    for item in ARMY_OCCUPATIONS:
        row = int(item["row"])
        values.append(
            base_update(
                row,
                identity_status="high_confidence",
                identity_evidence=army_identity_note(row),
                personnel_category="enlisted_army_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                research_status="occupation_only_found",
                next_action="Review Box 790 to establish the immediate pre-OSS affiliation and named last civilian employer; do not convert the Army occupation category into a workplace.",
            )
        )

    for row, item in IDENTITY_ONLY.items():
        values.append(
            base_update(
                row,
                identity_status="high_confidence",
                identity_evidence=item["note"],
                personnel_category="enlisted_army_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                research_status="requires_archival_review",
                next_action="Review Box 790 to establish the immediate pre-OSS affiliation and last civilian employer; no usable historical occupation category was established.",
            )
        )

    values.extend(
        [
            base_update(
                6,
                identity_status="conflicting",
                identity_evidence="The protected identifier leads to an official Army row printed as Turner J W, conflicting with indexed Wilmore J Turner. The records remain separate and no occupation is transferred.",
                personnel_category="unknown_or_indeterminate",
                commissioned_officer=None,
                allied_or_foreign_personnel=None,
                research_status="conflicting_sources",
                next_action="Review Box 789 to determine whether Turner J W is Wilmore J Turner, a transposition, or a different person; establish pre-OSS affiliation only after resolution.",
                archival_review_priority="critical",
            ),
            base_update(
                11,
                identity_status="high_confidence",
                identity_evidence="An original OSS awards-board attachment identifies the uncommon exact name Major Pierre M. Turquet as British Army personnel in Secret Intelligence; a compatible specialist biography supplies the full name and RAMC service.",
                name_variants=["Pierre Maurice Turquet"],
                personnel_category="foreign_or_allied_military_personnel",
                commissioned_officer=True,
                allied_or_foreign_personnel=True,
                research_status="requires_archival_review",
                next_action="Review Box 790 and British service records to establish the date and basis of Turquet's OSS SI connection, the sequence of RAMC service, and any last civilian employer before wartime service.",
            ),
            base_update(
                23,
                identity_status="high_confidence",
                identity_evidence="Two contemporary Broadcasting items repeat the distinctive exact name and WBEN station-director role; the July 1945 item explicitly identifies recent Office of Strategic Services service.",
                personnel_category="unknown_or_indeterminate",
                commissioned_officer=None,
                allied_or_foreign_personnel=False,
                research_status="verified_employer_found",
                next_action="Review Box 790 to confirm the precise OSS accession date, assignment and any intervening or cover Army status; WBEN remains the verified last civilian employer in the accessible record.",
                archival_review_priority="medium",
            ),
        ]
    )
    return values


def research_attempts() -> list[dict[str, object]]:
    reviewed_rows = {5, 6, 7, 11, 13, 16, 17, 18, 21, 23}
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        if row in reviewed_rows:
            outcome = "source_reviewed"
            reviewed = 8 if row in {11, 23} else 5
            rejected = 5
            detail = "Reviewed official, contemporary, specialist or archival evidence produced the identity, occupation, military-affiliation, employer or conflict outcome recorded in the evidence bundle."
        else:
            outcome = "no_result"
            reviewed = 6
            rejected = 6
            detail = UNRESOLVED[row]

        special_rejection = ""
        if row == 2:
            special_rejection = " A 1943 broadcasting trade-journal result for an NBC employee entering the Office of War Information was rejected because no source linked that person to OSS or Box 790."
        if row == 16:
            special_rejection = " A reproduced obituary naming Detachment 101 and pre-enlistment study was retained only as a lead because no inspectable original publisher or institutional source was located."
        if row == 17:
            special_rejection = " An early twentieth-century lawyer with the same name was rejected as chronologically incompatible."

        attempts.append(
            {
                "key": f"page476-row{row}-{slug(name)}-b971",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index and official Archives context; CIA Reading Room or equivalent official-source check; exact-name and meaningful variants; OSS, Army, rank and unit clues; employer and occupation 1940; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Boxes {box_for(row)}; protected identifiers used only when defensible",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_971",
                "started_at": "2026-10-30T17:00:00Z",
                "completed_at": "2026-10-30T21:30:00Z",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search snippets, unsourced genealogy, people-finder pages, postwar-only employment leads and sources without an OSS, protected-identifier or personnel-file bridge were rejected. Historical occupation codes and military service were not silently converted into employers." + special_rejection,
                "research_notes": f"{detail} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain, CIA Reading Room-equivalent and Library of Congress searches were checked as applicable. The index page, Army bulk file, technical documentation and relevant occupation-code pages were inspected directly. The image-only NARA Turquet file was OCR-located and visually verified. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": (
                    "Review Box 789 to resolve the protected-identifier/name conflict before assigning any Army occupation or pre-OSS affiliation."
                    if row == 6
                    else f"Review Box {box_for(row)} for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before wartime service."
                ),
                "attempt_number": 1,
                "research_agent_version": "before-oss-b971-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-971-v1",
        "reviewer": "Before OSS Batch 971 evidence review",
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
