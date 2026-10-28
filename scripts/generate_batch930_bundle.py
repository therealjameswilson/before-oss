#!/usr/bin/env python3
"""Generate the reviewed Batch 930 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import uuid
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / (
    "research/evidence-page455-john-l-sullivan-to-elinor-h-summers-"
    "review_batch-930_2026-10-27.json"
)

INDEX = "nara-index-b930"
ARMY = "army-bulk-b930"
TECH = "army-tech-b930"
CODES = "army-codes-b930"
SULLOWAY_FINDING_AID = "nhhs-sulloway-finding-aid-b930"
OFFICIAL_REGISTER = "official-register-1943-b930"
AMACHE_LEAVE = "berkeley-amache-leave-b930"

JOHN_L_GROUP = "11f41a4b-d7a5-52ca-bf54-f3295c8a213a"

PEOPLE = {
    24: ("cca2cffa-2270-5b47-9ef6-666706057b05", "John L Sullivan", "757"),
    25: ("1bf7a6a5-b2b8-575c-98c7-2c2dabd79a48", "John L Sullivan", "757"),
    26: ("4de5a14f-5ca1-5267-b56e-eab157fe4939", "John W Sullivan", "757"),
    27: ("3c6e6e5c-59a3-541b-8acd-51204243227c", "Leo E Sullivan", "757"),
    28: ("69aae1f4-cc49-5b26-86ba-5782f9ce687c", "Leslie F Sullivan", "757"),
    29: ("6f6c6933-ea91-574f-afde-93c02d04e065", "Mary L Sullivan", "757"),
    30: ("bd96d822-ef30-5b41-b9a7-830974f0dedf", "Phillip B Sullivan", "757"),
    31: ("46808238-ddda-5ac1-9686-48515565caec", "Phyllis A Sullivan", "757"),
    32: ("f8fd70de-0878-51c3-a901-66c5f8104788", "Richard E Sullivan", "757"),
    33: ("4efe4157-32eb-5ae0-a682-0a9219a23dd3", "Richard P Sullivan", "757"),
    34: ("7c49fa2c-9da6-5134-8f26-c1e2dcbeb631", "Thomas J Sullivan", "757"),
    35: ("aa513060-bc48-57e7-8260-caaa874a3bee", "Thomas V Sullivan", "757"),
    36: ("4c81aa01-870e-501f-ae9f-c54de01297c2", "William H Sullivan", "757"),
    37: ("eb928c89-4472-5038-98f9-78343042b846", "Alvah W Sulloway", "758"),
    38: ("ceff069a-9287-5cf2-8109-339aeda1ed7a", "Leonard Sultan", "758"),
    39: ("0ce88b2f-5413-5a46-b5f4-bccf37837d22", "Alfred F Sumabat", "758"),
    40: ("80542357-a72c-57b3-a590-b452b2827ba5", "Mercedes Sumi", "758"),
    41: ("1b764b72-6166-56ed-8896-cea761979131", "Shingo Sumi", "758"),
    42: ("79541560-3d33-5b65-8458-aa01f9d3e4b5", "Helen P Summerlin", "758"),
    43: ("f726cb2f-798c-56a5-9112-cd287137b5d4", "Roy C Summerlin", "758"),
    44: ("d9b876f4-34ba-5f11-907a-a645936912db", "Charnelle H Summers", "758"),
    45: ("a466c051-eb38-5c1c-a190-eb1d19f29c28", "Donald B Summers", "758"),
    46: ("ed415c3b-04a3-5806-9aea-33973ab8a08a", "Elinor H Summers", "758"),
}

ARMY_IDENTITIES = {
    27: {"entry": "1946-01-31", "grade": "PFC", "code": "480", "post_oss": True},
    28: {"entry": "1941-01-25", "grade": "PVT", "code": "859"},
    34: {"entry": "1943-07-14", "grade": "PVT", "code": "724"},
    35: {"entry": "1942-11-30", "grade": "PVT", "code": "902"},
}

ARMY_OCCUPATIONS = {
    28: (
        "Occupations in the manufacture of leather",
        "PDF physical page 173; historical category 8-59",
    ),
    34: (
        "Brick and stone masons, and tile setters",
        "PDF physical pages 174 and 304; historical category 7-24",
    ),
    35: (
        "Occupations in the manufacture of automobiles, not elsewhere classified",
        "PDF physical page 174; historical category 9-02",
    ),
}

UNRESOLVED = {
    26: "The printed identifier has no accepted Army bulk match, and common-name results did not supply an independent Box 757 bridge.",
    29: "Common-name results produced namesakes but no two-identifier bridge to the Box 757 person.",
    30: "Exact-name and variant searches found no source that linked this person to OSS context or a pre-OSS affiliation.",
    31: "Common-name results produced namesakes but no two-identifier bridge to the Box 757 person.",
    36: "Common-name results produced no sufficiently specific identity bridge or reliable pre-OSS affiliation.",
    38: "A same-name 1940 census-derived discovery lead lacked any OSS, protected-identifier or Box 758 bridge and was rejected.",
    39: "Exact-name, Philippine and transliteration searches produced no corroborating identity or pre-OSS affiliation.",
    42: "Multiple same-name vital-record and genealogy leads lacked an OSS, identifier or Box 758 bridge and were rejected.",
    44: "Exact-name and spelling-variant searches produced no reliable external identity or employment evidence.",
    45: "Common-name results produced no two-identifier bridge to the Box 758 person.",
    46: "Exact-name and spelling-variant searches produced no reliable external identity or employment evidence.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def duplicate_group(key: str) -> str:
    return str(uuid.uuid5(uuid.NAMESPACE_URL, f"before-oss:{key}"))


RICHARD_GROUP = duplicate_group("richard-e-p-sullivan-page455-rows32-33")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 757-758",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 455, rows 24-46; checked against layout-preserving text and the rendered page image",
            "access_date": "2026-10-27",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. Full identifiers remain private. Three John L Sullivan rows and the Richard E/Richard P Sullivan pair are not silently merged.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; five reviewed Batch 930 protected-identifier candidates",
            "access_date": "2026-10-27",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "No raw record or full protected identifier is retained in public assets. Leo E Sullivan's 1946 entry is identity-only. Richard E/Richard P remains a published conflict.",
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
            "locator": "PDF physical pages 173, 174 and 304; Batch 930 categories visually checked",
            "access_date": "2026-10-27",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical categories identify neither employer nor workplace. The 1946 Leo E Sullivan category is not published as pre-OSS evidence.",
        },
        {
            "key": SULLOWAY_FINDING_AID,
            "stable_url": "https://www.nhhistory.org/finding_aids/finding_aids/Sulloway_Alvah_Papers_2007.035.pdf",
            "archival_identifier": "New Hampshire Historical Society collection 2007.035",
            "title": "Guide to the Alvah Sulloway Papers, 1836-2006",
            "author_creator": "Sandra Wheeler",
            "repository_publisher": "New Hampshire Historical Society",
            "publication_record_date": "2008",
            "locator": "PDF physical pages 2-3; visually checked biographical chronology",
            "access_date": "2026-10-27",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Alvah Sulloway Papers, 1836-2006",
            "document_number": "2007.035",
            "rights_notes": "The finding aid identifies the father's firm as Sulloway & Hollis, states that Alvah joined it after law school, and dates his OSS service to 1942-1945.",
        },
        {
            "key": OFFICIAL_REGISTER,
            "stable_url": "https://www.govinfo.gov/content/pkg/GOVPUB-CS1-3497893fa707a7a3803ce15b4ac4e6ad/pdf/GOVPUB-CS1-3497893fa707a7a3803ce15b4ac4e6ad.pdf",
            "archival_identifier": "GovInfo 10055624; printed page 301",
            "title": "Official Register of the United States, 1943",
            "author_creator": "United States Civil Service Commission",
            "repository_publisher": "U.S. Government Publishing Office",
            "publication_record_date": "1943",
            "locator": "PDF physical page 319, printed page 301; Office of Strategic Services, Secretariat",
            "access_date": "2026-10-27",
            "source_quality": "A_direct_official",
            "collection_name": "Official Register of the United States",
            "rights_notes": "Visually checked. It lists Alvah W. Sulloway as Chief of the OSS Secretariat and does not identify a military rank.",
        },
        {
            "key": AMACHE_LEAVE,
            "stable_url": "https://digicoll.lib.berkeley.edu/record/174635/files/cubanc_35_1_01249806ta.pdf",
            "archival_identifier": "BANC MSS 67/14 c, folder L2.15:2; record 174635; ark:/13030/k6zs33mg",
            "title": "Japanese translation layouts (2 of 7)",
            "author_creator": "United States War Relocation Authority",
            "repository_publisher": "The Bancroft Library, University of California, Berkeley",
            "publication_record_date": "July 1944",
            "locator": "PDF physical page 85; Granada Pioneer leave list dated 20 July 1944, entries 3-4",
            "access_date": "2026-10-27",
            "source_quality": "A_direct_official",
            "collection_name": "Japanese American Evacuation and Resettlement Records 1930-1974",
            "document_number": "cubanc_35_1_01249806ta.pdf",
            "rights_notes": "The federal record was visually checked. It documents involuntary confinement, indefinite leave and an OSS destination employer; no home address or family relationship is reproduced or inferred.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": "sulloway-hollis-b930",
            "canonical_name": "Sulloway & Hollis",
            "historical_name": "Sulloway & Hollis",
            "aliases": ["his father's law firm"],
            "organization_type": "law firm",
            "sector": "law",
            "city": "Concord",
            "state_or_region": "New Hampshire",
            "country": "United States",
            "active_dates": "Established before 1941; exact dates not fixed by the reviewed finding aid",
            "normalization_notes": "The finding aid calls Frank J. Sulloway a founder and principal of Sulloway & Hollis, then states that Alvah joined his father's law firm. This supports the normalization without substituting a later firm name.",
        },
        {
            "key": "granada-relocation-center-b930",
            "canonical_name": "Granada Relocation Center (Amache)",
            "historical_name": "Granada Relocation Center",
            "aliases": ["Amache", "Granada Pioneer"],
            "organization_type": "federal wartime incarceration center",
            "sector": "federal_government",
            "city": "Granada",
            "state_or_region": "Colorado",
            "country": "United States",
            "active_dates": "1942-1945",
            "normalization_notes": "This was an incarceration site administered by the War Relocation Authority. The relationship is involuntary confinement, not employment, education or voluntary affiliation.",
        },
    ]


def affiliations() -> list[dict[str, object]]:
    result: list[dict[str, object]] = []
    for row, (occupation, _locator) in ARMY_OCCUPATIONS.items():
        data = ARMY_IDENTITIES[row]
        result.append({
            "key": f"{slug(PEOPLE[row][1])}-occupation-b930",
            "person_id": PEOPLE[row][0],
            "occupation": occupation,
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
    result.append({
        "key": "alvah-sulloway-sulloway-hollis-b930",
        "person_id": PEOPLE[37][0],
        "organization_key": "sulloway-hollis-b930",
        "organization_name_as_found": "his father's law firm",
        "role_title": "lawyer",
        "occupation": "attorney",
        "relationship_type": "employment",
        "start_date": "1941",
        "end_date": "1942",
        "date_precision": "The finding aid states that Sulloway graduated from Harvard Law School in 1941, then joined his father's law firm, and served in OSS from 1942 through 1945.",
        "city": "Concord",
        "state_or_region": "New Hampshire",
        "country": "United States",
        "immediate_pre_oss": True,
        "last_civilian_pre_service": True,
        "pre_oss_temporal_basis": "strongly_date_bounded",
        "identity_confidence": "high_confidence",
        "claim_confidence": "high",
        "source_quality": "B_authoritative_institutional",
        "publication_status": "published",
        "research_notes": "The chronology strongly bounds the firm as the immediate and last civilian employment before OSS service; the finding aid does not give an exact hire or separation day.",
    })
    for row in (40, 41):
        result.append({
            "key": f"{slug(PEOPLE[row][1])}-amache-b930",
            "person_id": PEOPLE[row][0],
            "organization_key": "granada-relocation-center-b930",
            "organization_name_as_found": "Granada Pioneer, Amache, Colorado",
            "role_title": "incarcerated resident granted indefinite leave",
            "relationship_type": "unknown",
            "end_date": "1944-07-22",
            "date_precision": "A federal leave list dated 20 July 1944 records departure for Washington, D.C. on 22 July and identifies the Office of Strategic Services as employer-to-be.",
            "city": "Granada",
            "state_or_region": "Colorado",
            "country": "United States",
            "immediate_pre_oss": True,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "explicit_immediate",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "A_direct_official",
            "publication_status": "published",
            "research_notes": "This is an involuntary confinement status immediately before OSS employment, not employment by or voluntary affiliation with the center. No earlier civilian employer is identified.",
        })
    return result


def army_identity_claim(row: int) -> dict[str, object]:
    name = PEOPLE[row][1]
    data = ARMY_IDENTITIES[row]
    temporal = f"The Army record documents entry on {data['entry']}; it does not establish the OSS transfer date."
    note = "The protected identifier is withheld from public data; no employer is inferred from the Army row."
    if data.get("post_oss"):
        temporal = "The record dates Army entry to 31 January 1946, after OSS dissolution; it is identity and classification evidence only."
        note = "The protected identifier is withheld. The post-OSS occupation code is not published as pre-OSS evidence."
    return {
        "key": f"identity-{slug(name)}-row{row}-b930",
        "person_id": PEOPLE[row][0],
        "claim_type": "identity",
        "claim_text": f"The indexed {name} row is a high-confidence match to an official Army record dated {data['entry']}.",
        "evidence_paraphrase": "The reviewed Army row agrees through a nonshared protected identifier and exact full name.",
        "identity_match_assessment": "High confidence from a nonshared protected identifier and exact full name.",
        "temporal_assessment": temporal,
        "source_quality": "A_direct_official",
        "claim_confidence": "high",
        "publication_status": "published",
        "match_notes": note,
        "sources": [
            {"source_key": INDEX, "locator_override": f"PDF page 455 row {row}; Box {PEOPLE[row][2]}"},
            {"source_key": ARMY, "locator_override": f"Accepted reviewed identity record; Army entry {data['entry']}; protected identifier withheld"},
            {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46; field definitions"},
        ],
    }


def army_occupation_claim(row: int) -> dict[str, object]:
    name = PEOPLE[row][1]
    data = ARMY_IDENTITIES[row]
    occupation, locator = ARMY_OCCUPATIONS[row]
    return {
        "key": f"occupation-{slug(name)}-b930",
        "person_id": PEOPLE[row][0],
        "affiliation_key": f"{slug(name)}-occupation-b930",
        "claim_type": "occupation",
        "claim_text": f"At Army entry on {data['entry']}, {name} was recorded in the historical occupation category {occupation}; no employer or workplace is identified.",
        "evidence_excerpt": occupation,
        "evidence_paraphrase": f"The accepted Army record carries civilian-occupation code {data['code']}, decoded from NARA's official code list.",
        "identity_match_assessment": "The category belongs only to the reviewed protected-identifier match; the identifier itself is not public.",
        "temporal_assessment": "Dated to Army entry; it does not establish an immediate pre-OSS affiliation or named employer.",
        "source_quality": "A_direct_official",
        "claim_confidence": "medium",
        "publication_status": "publish_qualified",
        "match_notes": "The historical category is a qualified lead, not a named employer, institution, workplace or exact title.",
        "sources": [
            {"source_key": ARMY, "locator_override": f"Accepted reviewed identity record; civilian occupation code {data['code']}; protected identifier withheld"},
            {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46; Army-entry-date and civilian-occupation fields"},
            {"source_key": CODES, "locator_override": locator, "excerpt_override": occupation},
        ],
    }


def claims() -> list[dict[str, object]]:
    result = [army_identity_claim(row) for row in ARMY_IDENTITIES]
    result.extend(army_occupation_claim(row) for row in ARMY_OCCUPATIONS)
    result.extend([
        {
            "key": "richard-e-p-sullivan-conflict-b930",
            "person_id": PEOPLE[32][0],
            "claim_type": "identity",
            "claim_text": "The indexed Richard E Sullivan row shares a nonpublic identifier with an Army record for Richard P Sullivan; the middle-initial conflict is unresolved.",
            "evidence_paraphrase": "The protected identifier agrees, but the official Army name conflicts with the index and also matches the adjacent identifier-free Richard P Sullivan row.",
            "identity_match_assessment": "Conflicting. The identifier is strong evidence for the Richard E row, while the exact Army name points toward the adjacent Richard P row.",
            "temporal_assessment": "The Army row records entry on 24 April 1943 and student code 992; neither is assigned as a settled fact until Box 757 resolves the name conflict.",
            "source_quality": "A_direct_official",
            "claim_confidence": "conflicting",
            "publication_status": "conflicting",
            "match_notes": "Both index rows remain separate. No middle initial is silently corrected and no occupation affiliation is published for either person.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 455 rows 32-33; two separate Richard E and Richard P Sullivan rows; Box 757"},
                {"source_key": ARMY, "locator_override": "Conflicting reviewed identity record; name Richard P Sullivan; Army entry 1943-04-24; protected identifier withheld"},
                {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46; field definitions"},
                {"source_key": CODES, "support_type": "context_only", "locator_override": "PDF physical page 304; amended category 9-92 Students"},
            ],
        },
        {
            "key": "identity-alvah-w-sulloway-b930",
            "person_id": PEOPLE[37][0],
            "claim_type": "identity",
            "claim_text": "The indexed Alvah W Sulloway is a high-confidence match to Alvah Woodbury Sulloway, the lawyer documented in the OSS General Counsel's office and as Chief of its Secretariat.",
            "evidence_paraphrase": "An institutional finding aid and the 1943 Official Register independently align the distinctive exact name, legal profession and OSS service.",
            "identity_match_assessment": "High confidence from a distinctive exact name and two independent authoritative sources with explicit OSS roles.",
            "temporal_assessment": "The finding aid dates OSS legal service to 1942-1945; the Official Register lists him in 1943.",
            "source_quality": "A_direct_official",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "The full middle-name variant is retained. The official register supports civilian rather than commissioned classification.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 455 row 37; Box 758"},
                {"source_key": SULLOWAY_FINDING_AID, "locator_override": "PDF physical pages 2-3; biographical chronology"},
                {"source_key": OFFICIAL_REGISTER, "locator_override": "PDF physical page 319, printed page 301; OSS Secretariat"},
            ],
        },
        {
            "key": "alvah-sulloway-immediate-law-firm-b930",
            "person_id": PEOPLE[37][0],
            "affiliation_key": "alvah-sulloway-sulloway-hollis-b930",
            "claim_type": "immediate_pre_oss_affiliation",
            "claim_text": "After graduating from Harvard Law School in 1941, Alvah W Sulloway joined his father's Concord law firm, Sulloway & Hollis, before beginning OSS legal service in 1942.",
            "evidence_excerpt": "Alvah then joined his father's law firm in Concord.",
            "evidence_paraphrase": "The finding aid gives the firm relationship and adjacent 1941-1942 chronology, and identifies the father's firm as Sulloway & Hollis.",
            "identity_match_assessment": "High-confidence identity from the distinctive name and independent official OSS register entry.",
            "temporal_assessment": "Strongly date-bounded as the employment immediately between 1941 law-school graduation and 1942 OSS service; exact dates are not stated.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "Published as immediate pre-OSS employment with the date-bounded qualifier; no exact day or later firm name is inferred.",
            "sources": [
                {"source_key": SULLOWAY_FINDING_AID, "locator_override": "PDF physical pages 2-3; 1941 graduation, father's law firm, 1942-1945 OSS service"},
                {"source_key": OFFICIAL_REGISTER, "support_type": "context_only", "locator_override": "1943 official OSS Secretariat identity"},
            ],
        },
        {
            "key": "alvah-sulloway-last-civilian-law-firm-b930",
            "person_id": PEOPLE[37][0],
            "affiliation_key": "alvah-sulloway-sulloway-hollis-b930",
            "claim_type": "last_civilian_pre_service",
            "claim_text": "Sulloway & Hollis is the best-supported last civilian employer before Alvah W Sulloway's OSS service.",
            "evidence_paraphrase": "The institutional chronology places no intervening employer or military assignment between the Concord law firm and OSS service beginning in 1942.",
            "identity_match_assessment": "High-confidence identity from distinctive name and explicit OSS legal roles.",
            "temporal_assessment": "Strongly date-bounded, not an explicit 'recruited from' statement.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "Kept separate from the immediate-affiliation claim even though the same employer satisfies both categories on current evidence.",
            "sources": [{"source_key": SULLOWAY_FINDING_AID, "locator_override": "PDF physical pages 2-3; consecutive 1941-1942 chronology"}],
        },
    ])
    for row in (40, 41):
        name = PEOPLE[row][1]
        result.extend([
            {
                "key": f"identity-{slug(name)}-b930",
                "person_id": PEOPLE[row][0],
                "claim_type": "identity",
                "claim_text": f"The indexed {name} is a high-confidence match to the person named in a federal Amache leave list whose employer-to-be was the Office of Strategic Services.",
                "evidence_excerpt": "Employer to be Office of Strategic Services.",
                "evidence_paraphrase": "The federal record names the exact distinctive person, departure date and OSS destination; Mercedes and Shingo appear together in both the leave list and adjacent index rows.",
                "identity_match_assessment": "High confidence from the exact distinctive name, paired-name context, same dated OSS destination and adjacent Box 758 index placement.",
                "temporal_assessment": "The leave list is dated 20 July 1944 and records departure for Washington on 22 July 1944.",
                "source_quality": "A_direct_official",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "No family relationship is inferred. The source establishes impending civilian OSS employment but does not name a job title or earlier employer.",
                "sources": [
                    {"source_key": INDEX, "locator_override": f"PDF page 455 row {row}; Box 758"},
                    {"source_key": AMACHE_LEAVE, "locator_override": f"PDF physical page 85; {'entry 3' if row == 40 else 'entry 4'}; 22 July 1944"},
                ],
            },
            {
                "key": f"{slug(name)}-immediate-amache-b930",
                "person_id": PEOPLE[row][0],
                "affiliation_key": f"{slug(name)}-amache-b930",
                "claim_type": "immediate_pre_oss_affiliation",
                "claim_text": f"Immediately before OSS employment, {name} was an incarcerated resident of Granada Relocation Center (Amache) and was granted indefinite leave to depart for Washington on 22 July 1944.",
                "evidence_excerpt": "Employer to be Office of Strategic Services.",
                "evidence_paraphrase": "The federal leave list directly links the end of Amache confinement to the dated Washington departure and OSS employment.",
                "identity_match_assessment": "High confidence from the exact distinctive name and paired OSS transition evidence.",
                "temporal_assessment": "Explicit immediate transition: leave for Washington on 22 July 1944, with OSS identified as employer-to-be.",
                "source_quality": "A_direct_official",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "The center relationship is involuntary confinement, not employment or a voluntary institutional affiliation. No earlier civilian employer is inferred.",
                "sources": [{"source_key": AMACHE_LEAVE, "locator_override": f"PDF physical page 85; {'entry 3' if row == 40 else 'entry 4'}"}],
            },
        ])
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
    for row, data in ARMY_IDENTITIES.items():
        status = "occupation_only_found" if row in ARMY_OCCUPATIONS else "requires_archival_review"
        evidence = "An exact full name and nonshared protected identifier connect the index row to the official Army record."
        if data.get("post_oss"):
            evidence += " The 1946 entry is post-OSS and therefore supports identity and personnel classification only."
        updates.append({
            "person_id": PEOPLE[row][0],
            "identity_status": "high_confidence",
            "identity_evidence": evidence,
            "personnel_category": "enlisted_army_personnel",
            "commissioned_officer": False,
            "allied_or_foreign_personnel": False,
            "manual_review_required": True,
            "research_status": status,
            "next_action": f"Review Box {PEOPLE[row][2]} for the immediate pre-OSS affiliation and a named employer or institution.",
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
            "archival_review_priority": "high",
        })
    updates.extend([
        {
            **archival_update(24, "This is the second of three adjacent identical John L Sullivan rows; the rows remain separate.", priority="critical"),
            "identity_status": "ambiguous",
            "identity_evidence": "Three separately printed John L Sullivan rows occur consecutively on page 455 with the same box and no visible identifier. Name and adjacency alone cannot establish duplication.",
            "possible_duplicate_group": JOHN_L_GROUP,
            "next_action": "Review all three Box 757 John L Sullivan files together for identifiers, cross-references and duplicate-file evidence before merging or assigning any external biography.",
        },
        {
            **archival_update(25, "This is the third of three adjacent identical John L Sullivan rows; the rows remain separate.", priority="critical"),
            "identity_status": "ambiguous",
            "identity_evidence": "Three separately printed John L Sullivan rows occur consecutively on page 455 with the same box and no visible identifier. Name and adjacency alone cannot establish duplication.",
            "possible_duplicate_group": JOHN_L_GROUP,
            "next_action": "Review all three Box 757 John L Sullivan files together for identifiers, cross-references and duplicate-file evidence before merging or assigning any external biography.",
        },
        {
            "person_id": PEOPLE[32][0],
            "identity_status": "conflicting",
            "identity_evidence": "A nonshared protected identifier links the index row to an Army record, but the index prints Richard E Sullivan and the Army record prints Richard P Sullivan; an adjacent index row separately prints Richard P Sullivan without an identifier.",
            "name_variants": ["Richard P Sullivan"],
            "manual_review_required": True,
            "possible_duplicate_group": RICHARD_GROUP,
            "research_status": "conflicting_sources",
            "next_action": "Review both Box 757 Richard Sullivan files and original index cards together to determine whether the identifier, middle initial or file association is erroneous before accepting the Army identity or student category.",
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
            "archival_review_priority": "critical",
        },
        {
            "person_id": PEOPLE[33][0],
            "identity_status": "ambiguous",
            "identity_evidence": "This separately printed Richard P Sullivan row has no visible identifier, while the adjacent Richard E Sullivan row's nonpublic identifier matches an Army record named Richard P Sullivan.",
            "name_variants": ["Richard E Sullivan"],
            "manual_review_required": True,
            "possible_duplicate_group": RICHARD_GROUP,
            "research_status": "requires_archival_review",
            "next_action": "Review both Box 757 Richard Sullivan files and original index cards together before merging, correcting an initial or assigning the Army record.",
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
            "archival_review_priority": "critical",
        },
        {
            "person_id": PEOPLE[37][0],
            "identity_status": "high_confidence",
            "identity_evidence": "The distinctive exact indexed name aligns with an institutional finding aid documenting OSS legal service and the 1943 Official Register's OSS Secretariat entry.",
            "name_variants": ["Alvah Woodbury Sulloway"],
            "personnel_category": "civilian_professional_or_administrative_grade",
            "commissioned_officer": False,
            "allied_or_foreign_personnel": False,
            "manual_review_required": True,
            "research_status": "verified_employer_found",
            "next_action": "Review Box 758 for the exact recruitment or appointment date and any direct application or résumé confirming the 1941-1942 law-firm transition.",
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
            "archival_review_priority": "medium",
        },
        {
            "person_id": PEOPLE[40][0],
            "identity_status": "high_confidence",
            "identity_evidence": "A federal Amache leave list names Mercedes Sumi, dates her 22 July 1944 departure for Washington and identifies OSS as employer-to-be; she appears beside Shingo Sumi in both sources.",
            "personnel_category": "civilian_professional_or_administrative_grade",
            "commissioned_officer": False,
            "allied_or_foreign_personnel": False,
            "manual_review_required": True,
            "research_status": "requires_archival_review",
            "next_action": "Review Box 758 for her OSS position, exact start date and any civilian employer before wartime incarceration. No earlier employer is inferred from the leave list.",
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
            "archival_review_priority": "critical",
        },
        {
            "person_id": PEOPLE[41][0],
            "identity_status": "high_confidence",
            "identity_evidence": "A federal Amache leave list names Shingo Sumi, dates his 22 July 1944 departure for Washington and identifies OSS as employer-to-be; he appears beside Mercedes Sumi in both sources.",
            "personnel_category": "civilian_professional_or_administrative_grade",
            "commissioned_officer": False,
            "allied_or_foreign_personnel": False,
            "manual_review_required": True,
            "research_status": "requires_archival_review",
            "next_action": "Review Box 758 for his OSS position, exact start date and any civilian employer before wartime incarceration. No earlier employer is inferred from the leave list.",
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
            "archival_review_priority": "critical",
        },
        {
            "person_id": PEOPLE[43][0],
            "identity_status": "unresolved",
            "identity_evidence": "The visually checked index directly prints Roy C Summerlin as 2nd Lt in Box 758, but exact-name, rank, official-register, CIA-site, obituary, institutional and archival searches found no defensible external identity bridge or employer.",
            "personnel_category": "commissioned_army_officer",
            "commissioned_officer": True,
            "allied_or_foreign_personnel": False,
            "manual_review_required": True,
            "research_status": "requires_archival_review",
            "next_action": "Review Box 758 for branch, assignment, full identity and last civilian employer before military service. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
            "archival_review_priority": "high",
        },
    ])
    return updates


def research_attempts() -> list[dict[str, object]]:
    attempts: list[dict[str, object]] = []
    for row in sorted(PEOPLE):
        person_id, name, box = PEOPLE[row]
        if row in ARMY_IDENTITIES:
            outcome, reviewed, rejected = "source_reviewed", 8, 3
            detail = "A nonshared protected identifier supports a high-confidence official Army identity bridge."
            if row in ARMY_OCCUPATIONS:
                detail += " The dated occupation category names no employer or workplace."
            else:
                detail += " The 1946 record is post-OSS and was not converted into pre-OSS evidence."
        elif row == 32:
            outcome, reviewed, rejected = "source_reviewed", 9, 4
            detail = "The protected identifier agrees but the middle initial conflicts with the Army record and an adjacent index row; the conflict remains public and unresolved."
        elif row == 33:
            outcome, reviewed, rejected = "candidate_found", 8, 5
            detail = "The adjacent identifier conflict creates a possible duplicate or indexing error; this row remains separate pending joint file review."
        elif row == 37:
            outcome, reviewed, rejected = "source_reviewed", 11, 3
            detail = "An institutional finding aid and official register support a high-confidence identity and strongly date-bounded Sulloway & Hollis employment before OSS service."
        elif row in {40, 41}:
            outcome, reviewed, rejected = "source_reviewed", 10, 3
            detail = "A federal Amache leave list explicitly connects involuntary confinement to a 22 July 1944 departure for OSS employment; it names no earlier civilian employer."
        elif row in {24, 25}:
            outcome, reviewed, rejected = "candidate_found", 7, 5
            detail = "Three identical adjacent John L Sullivan rows remain separate and require joint Box 757 review before any external biography is assigned."
        elif row == 43:
            outcome, reviewed, rejected = "no_result", 7, 4
            detail = "The index directly supports commissioned-officer classification, but no reliable external identity or employment source was found."
        else:
            outcome, reviewed, rejected = "no_result", 6, 4
            detail = UNRESOLVED[row]
        attempts.append({
            "key": f"page455-row{row}-{slug(name)}-b930",
            "person_id": person_id,
            "source_adapter": "manual_staged_protocol",
            "query_text": f"{name}; NARA index and public Archives context; 1943 Official Register; CIA Reading Room site-restricted exact-name discovery; OSS and spelling variants; employer and occupation 1940; obituary, institutional, newspaper, Library of Congress and archival searches; Box {box}; protected-identifier Army crosswalk where defensible",
            "query_variant_type": "staged_identity_employment_archival_protocol_batch_930",
            "started_at": "2026-10-27T20:00:00Z",
            "completed_at": "2026-10-28T00:20:00Z",
            "outcome": outcome,
            "sources_reviewed": reviewed,
            "candidate_sources_rejected": rejected,
            "rejection_reasons": "Unbridged namesakes, search snippets, family-only assertions, modern profiles, postwar-only leads and sources without an OSS or Box-file bridge were not assigned. Grouped CIA Reading Room and Library of Congress exact-name checks returned no additional person-specific pre-OSS result. A Densho Names Registry check for the Sumi pair was blocked by source access and was not bypassed.",
            "research_notes": f"{detail} The index, Sulloway, Amache, official-register and relevant Army code-list pages were visually checked where applicable. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA API call was made.",
            "next_action": f"Review Box {box} for corroborating identifiers and the immediate pre-OSS affiliation or last civilian employer.",
            "attempt_number": 1,
            "research_agent_version": "before-oss-b930-v1",
        })
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-930-v1",
        "reviewer": "Before OSS Batch 930 evidence review",
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
