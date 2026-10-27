#!/usr/bin/env python3
"""Generate the reviewed Batch 927 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import uuid
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / (
    "research/evidence-page454-richard-w-stubbs-to-anton-m-sturrett-"
    "review_batch-927_2026-10-27.json"
)

INDEX = "nara-index-b927"
ARMY = "army-bulk-b927"
TECH = "army-tech-b927"
CODES = "army-codes-b927"
BROADCASTING = "broadcasting-milburn-stuckwish-b927"
LORRIS = "lorris-andre-studler-b927"
AFH = "alliance-francaise-andre-studler-b927"

PEOPLE = {
    1: ("e5e776b8-838a-5134-9260-ab3689b45911", "Richard W Stubbs", "754"),
    2: ("7cfbdb61-a69c-52d0-a5e6-0e231dcd7b94", "Henri Stuber", "754"),
    3: ("f74af8e7-fcfa-59f7-ac55-15f09a6dc691", "Charles H Stubing", "754"),
    4: ("11275515-e068-5f2d-a6aa-2948b20653a0", "Albert E Stucchio", "754"),
    5: ("7fffeae0-b21a-59fd-8459-07c091f1a6a1", "Frances J Stuckart", "754"),
    6: ("aa07696d-4d28-52cf-b475-bf3d4bddcef4", "Milburn Stuckwish", "754"),
    7: ("ec3bf3ea-b87e-5082-a555-dbe8b0193dbe", "Herbert L Studer", "755"),
    8: ("efd15875-a9d2-5057-ae7f-86b219a950cb", "Andre Studler", "755"),
    9: ("e0d20032-a8a6-5969-ac0d-7b8b4b0f8825", "Andre Studler", "755"),
    10: ("9a99693e-5e8e-5169-8d79-dcc67092fcd1", "Raymond E Stuehrmann", "755"),
    11: ("9b759a46-6f5c-55e3-a43c-7cb5defe636d", "Chester A Stull", "755"),
    12: ("0187e76b-697c-50f6-b339-dd21113fc090", "Thomas L Stuller", "755"),
    13: ("c60f1480-7bf2-51b5-97cf-22490aa910da", "Herbert Q Stump", "755"),
    14: ("9850650d-d563-5820-96d2-5ef1531fc79d", "St. Claire D Stumper", "755"),
    15: ("22ee62e0-b002-58a3-9457-a32070fdb2ce", "* Stur", "755"),
    16: ("4526cad1-9e66-5fdb-b2e2-be181091b4ad", "Melvin Sturcz", "755"),
    17: ("84a73577-2e7a-51de-8c84-2b57d0740b94", "Curtis E Sturgeon", "755"),
    18: ("06cae7dc-f03d-503e-a737-7540ee80be5c", "Orvil D Sturgeon", "755"),
    19: ("a1b14ddc-bc9d-5967-b71e-abab7126851c", "Harry D Sturges", "755"),
    20: ("5bac785c-c25d-5df9-8727-52f18314b1a8", "Harry W Sturges", "755"),
    21: ("5c56dbfd-1ee8-5e72-8db0-7993c3d29b3b", "Harriet M Sturgis", "755"),
    22: ("a0233aea-bec1-5f0c-8cc2-17b83e6be0f8", "Norman R Sturgis", "755"),
    23: ("daa577d8-28fa-5ae1-a29a-e56c693b3451", "Anton M Sturrett", "755"),
}

ARMY_IDENTITIES = {
    4: {"entry": "1942-12-14", "grade": "PVT", "undefined_code": "093"},
    5: {"entry": "1942-11-28", "grade": "PVT", "variant": "Francis J Stuckart"},
    6: {"entry": "1943-03-08", "grade": "PVT", "variant": "Milburn H Stuckwish"},
    7: {"entry": "1942-11-19", "grade": "PVT"},
    8: {"entry": "1942-12-15", "grade": "PVT", "undefined_code": "993"},
    10: {"entry": "1943-05-12", "grade": "PVT"},
    13: {"entry": "1942-07-31", "grade": "PVT"},
    17: {"entry": "1942-09-12", "grade": "PVT"},
    18: {"entry": "1942-04-14", "grade": "PVT"},
    19: {"entry": "1943-03-19", "grade": "PVT"},
}

ARMY_OCCUPATIONS = {
    5: ("781", "Mechanics and repairmen, motor vehicle", "employment", "PDF physical page 175; historical category 7-81"),
    6: ("983", "Mechanics and repairmen, n.e.c.", "employment", "PDF physical page 175; historical category 9-83"),
    7: ("112", "Clerks in trade, n.e.c.", "employment", "PDF physical page 171; historical category 1-12"),
    10: ("138", "Stock clerks", "employment", "PDF physical pages 171 and 304; historical category 1-38"),
    13: ("721", "Miners and mining-machine operators", "employment", "PDF physical page 174; historical category 7-21"),
    17: ("105", "Clerks, general office", "employment", "PDF physical page 171; historical category 1-05"),
    18: ("316", "Farm hands, general farms", "employment", "PDF physical page 172; historical category 3-16"),
    19: ("992", "Students", "student", "PDF physical page 304; amended historical category 9-92"),
}

UNRESOLVED = {
    1: "Common-name searches produced no two-identifier bridge to the Box 754 person.",
    2: "Exact-name and spelling-variant searches found no reliable OSS identity bridge or pre-OSS affiliation.",
    3: "Exact-name and middle-initial searches found no person-specific source tied to OSS or Box 754.",
    11: "Common-name and middle-initial searches found no reliable identity bridge or pre-OSS affiliation.",
    12: "A veteran-register namesake lacks a protected-identifier, Box 755 or OSS bridge and was not assigned.",
    14: "Exact-name and punctuation-variant searches found no corroborating identifier or reliable affiliation.",
    15: "The index explicitly notes that no first name is present; an incomplete surname cannot support safe person matching.",
    16: "A Sturcz-to-Sturz family-name lead and later insurance career lack an OSS, Box 755 or protected-identifier bridge.",
    20: "Common-name searches produced no two-identifier bridge to the Box 755 person.",
    21: "Exact-name and middle-initial searches found no reliable OSS identity bridge or pre-OSS affiliation.",
    22: "Common-name and middle-initial searches found no person-specific source tied to OSS or Box 755.",
    23: "The protected index value produced no matching Army candidate, and public searches found no defensible identity bridge.",
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
            "archival_identifier": "RG 226, Entry A1-224, Boxes 754-755",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 454, rows 1-23; checked against layout-preserving text and the rendered page image",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. Full identifiers remain private. Two Andre Studler rows with different identifiers are not merged.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; ten accepted Batch 927 protected-identifier candidates",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "No raw record or full protected identifier is retained in public assets. Codes 093 and 993 remain uninterpreted; other coded occupations name neither employer nor workplace.",
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
            "access_date": "2026-10-26",
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
            "locator": "PDF physical pages 171-176 and 304; Batch 927 categories visually checked",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical categories identify neither employer nor workplace. Codes 093 and 993 are absent from the reviewed list and remain uninterpreted.",
        },
        {
            "key": BROADCASTING,
            "stable_url": "https://archive.org/details/broadcasting22unse/page/n1377/mode/1up",
            "archival_identifier": "Internet Archive item broadcasting22unse; Library of Congress call number TK 6540 .B85; LCCN 33014221",
            "title": "Broadcasting, June 1, 1942",
            "author_creator": "Broadcasting Publications Inc.",
            "repository_publisher": "Broadcasting Publications Inc.; digitized by the Library of Congress and Media History Digital Library",
            "publication_record_date": "1942-06-01",
            "locator": "Printed page 44, middle-left column; Internet Archive leaf 1377",
            "access_date": "2026-10-26",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Broadcasting [Jan-June 1942], volume 22",
            "rights_notes": "Contemporary trade report visually checked against the page scan. The excerpt is limited to the words needed to support the claim.",
        },
        {
            "key": LORRIS,
            "stable_url": "https://www.museelorris.fr/resistants/andre-joseph-lucien-marie-studler",
            "title": "André Joseph Lucien Marie STUDLER",
            "author_creator": "Musée départemental de la Résistance et de la Déportation de Lorris",
            "repository_publisher": "Musée départemental de la Résistance et de la Déportation de Lorris",
            "publication_record_date": "page accessed 2026",
            "locator": "Biographical chronology and prewar-employment paragraph",
            "access_date": "2026-10-26",
            "source_quality": "B_authoritative_institutional",
            "rights_notes": "The biography names 1939 work at an unnamed U.S. distillery and later OSS/SOE service, but cannot be assigned to either same-name index row.",
        },
        {
            "key": AFH,
            "stable_url": "https://afheritage.org/lilian-vera-rolfe-au-dela-du-courage",
            "title": "Lilian Vera Rolfe: Au-delà du courage",
            "author_creator": "Alliance Française Heritage",
            "repository_publisher": "Alliance Française Heritage",
            "publication_record_date": "page accessed 2026",
            "locator": "Historian-network discussion identifying André Studler",
            "access_date": "2026-10-26",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "rights_notes": "Corroborates the biographical candidate's French birth, OSS affiliation and SOE Historian-network service; it does not distinguish the two index rows.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": "wsoy-b927",
            "canonical_name": "WSOY",
            "historical_name": "WSOY",
            "aliases": ["WSOY Radio"],
            "organization_type": "radio station",
            "sector": "journalism_and_media",
            "city": "Decatur",
            "state_or_region": "Illinois",
            "country": "United States",
            "normalization_notes": "Historical call sign preserved. No modern ownership or successor relationship is inferred.",
        },
        {
            "key": "us-army-signal-corps-b927",
            "organization_id": "37fe0e48-9745-5a0a-8e04-6be9bc7c5c91",
            "canonical_name": "United States Army Signal Corps",
            "historical_name": "Signal Corps",
            "aliases": ["U.S. Army Signal Corps"],
            "organization_type": "military branch",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "Existing canonical organization reused. The contemporary source says only that Stuckwish joined the Signal Corps.",
        },
    ]


def affiliations() -> list[dict[str, object]]:
    result: list[dict[str, object]] = []
    for row, (code, occupation, relationship, _locator) in ARMY_OCCUPATIONS.items():
        result.append({
            "key": f"{slug(PEOPLE[row][1])}-occupation-b927",
            "person_id": PEOPLE[row][0],
            "occupation": occupation,
            "relationship_type": relationship,
            "end_date": ARMY_IDENTITIES[row]["entry"],
            "date_precision": f"Historical civilian-occupation code {code} was recorded at Army entry on {ARMY_IDENTITIES[row]['entry']}; no employer, school, workplace or OSS-transfer date is named.",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "high_confidence",
            "claim_confidence": "medium",
            "source_quality": "A_direct_official",
            "publication_status": "publish_qualified",
            "research_notes": "The historical category is not converted into a named employer, school, institution, workplace or exact job title.",
        })
    result.extend([
        {
            "key": "milburn-stuckwish-wsoy-b927",
            "person_id": PEOPLE[6][0],
            "organization_key": "wsoy-b927",
            "organization_name_as_found": "WSOY",
            "role_title": "chief engineer",
            "occupation": "radio engineer",
            "relationship_type": "employment",
            "end_date": "1942-06",
            "date_precision": "A June 1, 1942 contemporary report says WSOY chief engineer Milburn H. Stuckwish had joined the Signal Corps; exact separation and enlistment dates are not supplied.",
            "city": "Decatur",
            "state_or_region": "Illinois",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": True,
            "pre_oss_temporal_basis": "explicit_immediate",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "published",
            "research_notes": "This is the named civilian employer immediately before Signal Corps service, not the immediate OSS predecessor because military service intervened.",
        },
        {
            "key": "milburn-stuckwish-signal-corps-b927",
            "person_id": PEOPLE[6][0],
            "organization_key": "us-army-signal-corps-b927",
            "organization_name_as_found": "Signal Corps",
            "role_title": "Signal Corps member assigned to engineering training",
            "relationship_type": "military_assignment",
            "start_date": "1942-06",
            "end_date": "1943-03-08",
            "date_precision": "A June 1, 1942 report says he had joined and would report to the University of Illinois for six months of engineering work; the Army row records entry on 1943-03-08, so the administrative chronology requires file review.",
            "state_or_region": "Illinois",
            "country": "United States",
            "immediate_pre_oss": True,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "probable_immediate",
            "identity_confidence": "high_confidence",
            "claim_confidence": "medium",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "publish_qualified",
            "research_notes": "Best-supported wartime predecessor to OSS, but the reviewed sources do not state the OSS transfer date and the Army-entry date postdates the trade report.",
        },
    ])
    return result


def army_identity_claim(row: int) -> dict[str, object]:
    name = PEOPLE[row][1]
    data = ARMY_IDENTITIES[row]
    if row == 5:
        assessment = "High confidence from the nonshared protected identifier; the Frances/Francis first-name discrepancy is preserved as a variant and requires personnel-file review."
    else:
        assessment = "High confidence from the exact or compatible full name and a nonshared protected identifier."
    note = "The protected identifier is withheld from public data; no employer or OSS assignment is inferred from the Army row."
    if row in {4, 8}:
        note += f" Occupation code {data['undefined_code']} remains uninterpreted because it is absent from the reviewed official code list."
    return {
        "key": f"identity-{slug(name)}-row{row}-b927",
        "person_id": PEOPLE[row][0],
        "claim_type": "identity",
        "claim_text": f"The indexed {name} row is a high-confidence match to an official Army record dated {data['entry']}.",
        "evidence_paraphrase": "The reviewed Army row agrees through a nonshared protected identifier and an exact or explicitly preserved name variant.",
        "identity_match_assessment": assessment,
        "temporal_assessment": f"The record documents Army entry on {data['entry']}; it does not establish the OSS transfer date.",
        "source_quality": "A_direct_official",
        "claim_confidence": "high",
        "publication_status": "published",
        "match_notes": note,
        "sources": [
            {"source_key": INDEX, "locator_override": f"PDF page 454 row {row}; Box {PEOPLE[row][2]}"},
            {"source_key": ARMY, "locator_override": f"Accepted reviewed identity record; Army entry {data['entry']}; protected identifier withheld"},
            {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46; field definitions"},
        ],
    }


def army_occupation_claim(row: int) -> dict[str, object]:
    code, occupation, _relationship, locator = ARMY_OCCUPATIONS[row]
    name = PEOPLE[row][1]
    text = f"At Army entry on {ARMY_IDENTITIES[row]['entry']}, {name} was recorded in the historical occupation category {occupation}; no employer is identified."
    if occupation == "Students":
        text = f"At Army entry on {ARMY_IDENTITIES[row]['entry']}, {name} was recorded in the historical occupation group Students; no school or employer is identified."
    return {
        "key": f"occupation-{slug(name)}-b927",
        "person_id": PEOPLE[row][0],
        "affiliation_key": f"{slug(name)}-occupation-b927",
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
            "key": "last-civilian-milburn-stuckwish-wsoy-b927",
            "person_id": PEOPLE[6][0],
            "affiliation_key": "milburn-stuckwish-wsoy-b927",
            "claim_type": "last_civilian_pre_service",
            "claim_text": "Milburn H. Stuckwish was chief engineer of WSOY in Decatur, Illinois, immediately before joining the Signal Corps in 1942, making WSOY his last documented civilian employer before military service.",
            "evidence_excerpt": "chief engineer of WSOY, Decatur, Ill., has joined the Signal Corps",
            "evidence_paraphrase": "A contemporary radio trade journal names Stuckwish, his WSOY role and the transition into Signal Corps service in one sentence.",
            "identity_match_assessment": "High confidence from the rare full name with middle initial, the protected-identifier Army bridge and the compatible mechanics-and-repair occupation category.",
            "temporal_assessment": "Explicit immediate transition from WSOY to the Signal Corps in a June 1, 1942 report; the precise administrative dates still require the personnel file.",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "WSOY is a named employer. University of Illinois is described only as planned Signal Corps engineering training and is not classified as an employer.",
            "sources": [
                {"source_key": BROADCASTING, "locator_override": "Printed page 44, middle-left column; Internet Archive leaf 1377"},
                {"source_key": ARMY, "support_type": "context_only", "locator_override": "Accepted reviewed identity record; protected identifier withheld"},
            ],
        },
        {
            "key": "immediate-milburn-stuckwish-signal-corps-b927",
            "person_id": PEOPLE[6][0],
            "affiliation_key": "milburn-stuckwish-signal-corps-b927",
            "claim_type": "immediate_pre_oss_affiliation",
            "claim_text": "The best-supported immediate pre-OSS pathway for Milburn H. Stuckwish is Signal Corps service after leaving WSOY; the OSS transfer date has not been located.",
            "evidence_excerpt": "has joined the Signal Corps",
            "evidence_paraphrase": "The June 1942 report places Signal Corps service immediately after WSOY employment and describes planned engineering training.",
            "identity_match_assessment": "High-confidence person match; the protected identifier remains private.",
            "temporal_assessment": "Probable immediate to OSS rather than explicit: the military transition is explicit, but no reviewed source dates the later OSS transfer.",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "claim_confidence": "medium",
            "publication_status": "publish_qualified",
            "match_notes": "Military assignment, not civilian employment. The personnel file remains necessary to resolve the 1942 report and 1943 Army-entry date.",
            "sources": [
                {"source_key": BROADCASTING, "locator_override": "Printed page 44, middle-left column; Internet Archive leaf 1377"},
                {"source_key": ARMY, "support_type": "context_only", "locator_override": "Accepted reviewed identity record; Army entry 1943-03-08; protected identifier withheld"},
            ],
        },
    ])
    for row in (8, 9):
        result.append({
            "key": f"identity-andre-joseph-studler-candidate-row{row}-b927",
            "person_id": PEOPLE[row][0],
            "claim_type": "identity",
            "claim_text": "André Joseph Lucien Marie Studler, a French-American OSS/SOE officer who worked in an unnamed U.S. distillery in 1939, is an unassigned candidate for this index row.",
            "evidence_excerpt": "travaille dans une distillerie aux Etats-Unis",
            "evidence_paraphrase": "The museum biography gives birth and death dates, alias Sylvain, 1939 distillery work, OSS service and detachment to the SOE Historian network.",
            "identity_match_assessment": "Low for this row: two exact-name index rows carry different identifiers, and the biography contains no identifier that selects either file.",
            "temporal_assessment": "The 1939 distillery occupation is explicitly prewar, but it cannot be assigned to either indexed entity and the employer is unnamed.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "low",
            "publication_status": "withheld_low_confidence",
            "match_notes": "Private candidate attached to both rows. The entities remain separate; neither receives a published distillery affiliation.",
            "sources": [
                {"source_key": INDEX, "locator_override": f"PDF page 454 row {row}; Box 755; full identifier private"},
                {"source_key": LORRIS, "locator_override": "Biographical chronology and prewar-employment paragraph"},
                {"source_key": AFH, "support_type": "context_only", "locator_override": "Historian-network discussion identifying André Studler"},
            ],
        })
    return result


def archival_update(row: int, reason: str) -> dict[str, object]:
    person_id, name, box = PEOPLE[row]
    return {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, Box {box} and archive location, but staged official, CIA, OSS, employment, occupation, obituary, institutional, newspaper, directory and archival searches found no defensible identity bridge. {reason}",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": f"Review Box {box} for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "critical" if row == 15 else "high",
    }


def person_updates() -> list[dict[str, object]]:
    updates = [archival_update(row, reason) for row, reason in UNRESOLVED.items()]
    group = duplicate_group("andre-studler-page454-b927")
    for row, data in ARMY_IDENTITIES.items():
        name = PEOPLE[row][1]
        if row == 5:
            evidence = "A nonshared protected identifier links the indexed Frances J Stuckart row to an official Army record spelling the first name Francis. The discrepancy remains visible."
        else:
            evidence = "An exact or compatible full name and nonshared protected identifier connect the index row to the official Army record."
        status = "occupation_only_found" if row in ARMY_OCCUPATIONS else "requires_archival_review"
        if row == 6:
            status = "verified_employer_found"
        next_action = f"Review Box {PEOPLE[row][2]} for the immediate pre-OSS affiliation and named employer or institution."
        if row == 6:
            next_action = "Review Box 754 to establish the Signal Corps-to-OSS transfer date and reconcile the June 1942 trade report with the March 1943 Army-entry date. WSOY is verified as the last civilian employer."
        elif row in {4, 8}:
            next_action += f" Historical occupation code {data['undefined_code']} remains uninterpreted."
        update: dict[str, object] = {
            "person_id": PEOPLE[row][0],
            "identity_status": "high_confidence",
            "identity_evidence": evidence,
            "personnel_category": "enlisted_army_personnel",
            "commissioned_officer": False,
            "allied_or_foreign_personnel": False,
            "manual_review_required": True,
            "research_status": status,
            "next_action": next_action,
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
            "archival_review_priority": "critical" if row == 8 else "high",
        }
        if data.get("variant"):
            update["name_variants"] = [str(data["variant"])]
        if row == 8:
            update["possible_duplicate_group"] = group
            update["identity_evidence"] += " A museum biography is an unassigned candidate because a second Andre Studler row has a different identifier."
        updates.append(update)
    updates.append({
        **archival_update(9, "A strong museum biography names an OSS/SOE officer, but the adjacent exact-name row carries a different identifier and public evidence selects neither file."),
        "identity_status": "ambiguous",
        "possible_duplicate_group": group,
        "archival_review_priority": "critical",
        "identity_evidence": "Two Andre Studler source rows have different identifiers and therefore remain separate. A museum biography for André Joseph Lucien Marie Studler cannot be assigned to either file without direct linkage.",
        "next_action": "Review both Box 755 files together for birth date, alias Sylvain, nationality, Army history and OSS/SOE Historian-network references before assigning the biography or its unnamed-distillery occupation.",
    })
    return updates


def research_attempts() -> list[dict[str, object]]:
    attempts: list[dict[str, object]] = []
    for row, (person_id, name, box) in PEOPLE.items():
        if row == 6:
            outcome, reviewed, rejected = "source_reviewed", 9, 3
            detail = "A contemporary June 1942 trade report establishes WSOY, the chief-engineer role and the immediate transition to Signal Corps service; the accepted Army bridge corroborates identity."
        elif row == 8:
            outcome, reviewed, rejected = "candidate_found", 9, 4
            detail = "The Army row establishes this indexed entity, but the museum biography remains unassigned because the adjacent same-name index entity has a different identifier."
        elif row == 9:
            outcome, reviewed, rejected = "candidate_found", 8, 4
            detail = "The museum OSS/SOE biography is a strong exact-name candidate, but no identifier selects this row rather than the adjacent same-name row."
        elif row in ARMY_IDENTITIES:
            outcome, reviewed, rejected = "source_reviewed", 7, 3
            if row in ARMY_OCCUPATIONS:
                detail = f"An accepted protected-identifier Army bridge establishes high-confidence identity and the dated historical category {ARMY_OCCUPATIONS[row][1]}, but no named employer or institution."
            else:
                detail = f"An accepted protected-identifier Army bridge establishes high-confidence identity, but occupation code {ARMY_IDENTITIES[row]['undefined_code']} remains uninterpreted and no named employer or institution was found."
        else:
            outcome, reviewed, rejected = "no_result", 6, 3
            detail = UNRESOLVED[row]
        attempts.append({
            "key": f"page454-row{row}-{slug(name)}-b927",
            "person_id": person_id,
            "source_adapter": "manual_staged_protocol",
            "query_text": f"{name}; NARA index and public Archives context; CIA Reading Room site-restricted exact-name check; OSS and spelling variants; employer and occupation 1940; obituary, institutional, newspaper, directory and archival searches; Box {box}; protected-identifier Army crosswalk where defensible",
            "query_variant_type": "staged_identity_employment_archival_protocol_batch_927",
            "started_at": "2026-10-27T02:30:00Z",
            "completed_at": "2026-10-27T05:30:00Z",
            "outcome": outcome,
            "sources_reviewed": reviewed,
            "candidate_sources_rejected": rejected,
            "rejection_reasons": "Unbridged namesakes, search snippets, family-only assertions, modern profiles, postwar-only leads and sources without an OSS or Box-file bridge were not assigned. Grouped CIA Reading Room and Library of Congress exact-name checks returned no person-specific result.",
            "research_notes": f"{detail} The index page and relevant Army code pages were visually checked. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA API call was made.",
            "next_action": f"Review Box {box} for corroborating identifiers and the immediate pre-OSS affiliation or last civilian employer.",
            "attempt_number": 1,
            "research_agent_version": "before-oss-b927-v1",
        })
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-927-v1",
        "reviewer": "Before OSS Batch 927 evidence review",
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
