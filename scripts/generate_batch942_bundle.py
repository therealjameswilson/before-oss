#!/usr/bin/env python3
"""Generate the reviewed Batch 942 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page461-bernard-tatz-to-jeanne-h-taylor-"
    "review_batch-942_2026-10-28.json"
)

INDEX = "nara-index-b942"
ARMY = "army-bulk-b942"
TECH = "army-tech-b942"
CODES = "army-codes-b942"
TAUB_IFZ = "ifz-kurt-taub-b942"
TAUB_TUL = "tul-kurt-taub-b942"
EDMOND_WASHU = "washu-edmond-taylor-b942"
JACK_CIA = "cia-oss-medics-jack-taylor-b942"
JACK_NAVY = "navy-memorial-jack-taylor-b942"
JACK_USHMM = "ushmm-jack-taylor-b942"

US_ARMY = "us-army-existing-b942"
US_NAVY = "us-navy-existing-b942"
COI = "coi-existing-b942"
SCHENKER = "schenker-b942"
CHICAGO_TRIBUNE = "chicago-tribune-b942"


PEOPLE = {
    24: ("9efed2b0-e157-5e59-af87-1db5d4181888", "Bernard Tatz"),
    25: ("4690c105-7f54-5c08-a0c1-f77d916157a1", "Kurt L Taub"),
    26: ("93138996-9799-5356-9a98-e66cdca2789c", "J G Tausig"),
    27: ("1a32bb9c-88e1-5e6a-b8f3-50879aad6cc0", "John G Tausig"),
    28: ("aee13560-6af5-51b9-bebd-19fe7ccbc248", "Ed E Taves"),
    29: ("148dde5f-c3db-5b04-b770-ade9b0c4af7a", "William Y Tayenaka"),
    30: ("f7c97c0e-e6a9-556e-961b-3e1cf287c8d3", "Allen Taylor"),
    31: ("d591a709-bf9f-5d65-a532-c542f296d771", "Anne V Taylor"),
    32: ("3bc90b19-829b-503d-ab57-b673c2c219cd", "Chester L Taylor"),
    33: ("56fee5f9-b773-5597-b1ff-8e78d84394d8", "Dorothy L Taylor"),
    34: ("d326c13a-a719-5c00-8436-9c220e4372ce", "Earle F Taylor"),
    35: ("b81ac9d4-5cca-523b-bdd1-d791389cba4a", "Edmond L Taylor"),
    36: ("972c2618-c2ea-5d07-82fc-fc9b46b12de7", "Edward H Taylor"),
    37: ("0a5f69a9-ed97-5cb4-9d62-5dfd9bc438fc", "Eleanor V Taylor"),
    38: ("ba65a7c4-40bc-5d9f-8ca9-a6aa07a5aa6b", "Ellen Taylor"),
    39: ("99b43df9-36d7-5601-b37f-d46f1f113d95", "Fred J Taylor"),
    40: ("9c2cb3bd-42f5-58d6-87c9-4509feba9b95", "George S Taylor"),
    41: ("9609a18b-f205-55bc-9d1b-9c46f19da0ff", "Geraldine B Taylor"),
    42: ("f6cc4878-76e0-5256-bc43-9e262680cc10", "Gordon L Taylor"),
    43: ("fda21df8-311a-5dd8-ae31-bcdb141d4445", "Harry E Taylor"),
    44: ("91a8199c-d31e-5837-94b9-8019a09dbf7d", "Jack H Taylor"),
    45: ("0ae037cd-3ef3-5424-acb3-6c6d8e8d2fc9", "James C Taylor"),
    46: ("db23d265-0e22-5004-96ad-ab1762b43b92", "Jeanne H Taylor"),
}


ARMY_OCCUPATIONS = [
    {"row": 24, "date": "1942-12-11", "code": "175", "occupation": "Salespersons", "locator": "PDF physical page 171; historical category 1-75", "variant": "Bernard H Tatz"},
    {"row": 40, "date": "1941-10-09", "code": "105", "occupation": "Clerks, general office", "locator": "PDF physical page 171; historical category 1-05"},
    {"row": 42, "date": "1941-02-21", "code": "149", "occupation": "Clerks and kindred occupations, n.e.c.", "locator": "PDF physical page 171; historical category 1-49"},
    {"row": 43, "date": "1943-02-04", "code": "316", "occupation": "Farm hands, general farms", "locator": "PDF physical page 173; historical category 3-16"},
]


UNRESOLVED = {
    28: "Exact-name OSS, military, employer, occupation, obituary and archival searches produced no defensible identity bridge.",
    29: "A postwar obituary identifies a namesake as a retired self-employed gardener but supplies no OSS bridge or pre-OSS chronology, so it was rejected for this claim.",
    30: "The common name and absence of distinguishing index data prevented a defensible identity or employment match.",
    31: "Exact-name and middle-initial searches produced no reliable OSS, employer, occupation or institutional bridge.",
    32: "The printed identifier format did not meet the standard Army merged-file pattern and was not altered or padded; other searches produced no defensible bridge.",
    33: "Exact-name and middle-initial searches produced no reliable OSS, employer, occupation or institutional bridge.",
    34: "A prewar geology-publication namesake lacked an OSS, identifier or Box 766 bridge and was not assigned.",
    36: "Exact-name and middle-initial searches produced no reliable OSS, employer, occupation or institutional bridge.",
    37: "Exact-name and middle-initial searches produced no reliable OSS, employer, occupation or institutional bridge.",
    38: "The common name and absence of distinguishing index data prevented a defensible identity or employment match.",
    39: "No matching standard Army record or reliable OSS, employer, occupation or institutional bridge was found; nonappearance is not proof of nonservice.",
    41: "Exact-name and middle-initial searches produced no reliable OSS, employer, occupation or institutional bridge.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 766-767",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 461, rows 24-46; checked against layout-preserving text and a 300 dpi page render",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. Full protected identifiers remain private. John F Taylor on page 462 row 1 was checked as the next boundary.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; five reviewed Batch 942 candidate records; protected identifiers withheld",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "No raw bulk row or full protected identifier is retained in public assets. Four records were accepted; one middle-initial conflict remains explicit.",
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
            "locator": "PDF physical pages 171 and 173; historical categories 1-05, 1-49, 1-75 and 3-16",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical occupation labels identify neither employers nor workplaces.",
        },
        {
            "key": TAUB_IFZ,
            "stable_url": "https://www.ifz-muenchen.de/heftarchiv/2007_2_1_lukes.pdf",
            "title": "Ein nachrichtendienstliches Versagen: Die Amerikaner und die kommunistische Machtergreifung in der Tschechoslowakei 1948",
            "author_creator": "Igor Lukes",
            "repository_publisher": "Institut für Zeitgeschichte München-Berlin, Vierteljahrshefte für Zeitgeschichte",
            "publication_record_date": "2007",
            "locator": "PDF physical page 13; printed page 213",
            "access_date": "2026-10-28",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Vierteljahrshefte für Zeitgeschichte, volume 55, issue 2",
            "rights_notes": "The page was rendered at 300 dpi and visually inspected. It identifies Taub's Schenker employment, 1943 draft and placement in OSS's Czech section.",
        },
        {
            "key": TAUB_TUL,
            "stable_url": "https://dspace.tul.cz/server/api/core/bitstreams/250a13c4-f8e7-4e71-9b59-60b94b9032d4/content",
            "title": "Sergej Solovjev v soukolí politického procesu 50. let",
            "author_creator": "Zuzana Novotná",
            "repository_publisher": "Technical University of Liberec",
            "publication_record_date": "2014",
            "locator": "PDF physical page 32; chapter 'Vojenská mise - Charles Katek a Kurt Taub'",
            "access_date": "2026-10-28",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Technical University of Liberec institutional repository",
            "rights_notes": "The page was rendered at 300 dpi and visually inspected. The chronology is credited in the thesis to Karel Pacner and is treated as secondary evidence.",
        },
        {
            "key": EDMOND_WASHU,
            "stable_url": "https://aspace.library.washu.edu/repositories/6/resources/102",
            "archival_identifier": "MS-MS-ms142",
            "title": "Edmond Taylor Papers",
            "author_creator": "Julian Edison Department of Special Collections",
            "repository_publisher": "Washington University Libraries",
            "publication_record_date": "Finding aid revised 2021-03-12",
            "locator": "Biographical Information section",
            "access_date": "2026-10-28",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Manuscripts Collecting Area",
            "rights_notes": "The finding aid links Taylor's Chicago Tribune career and 1940 book to COI service in 1941-1942 and the OSS planning board in 1942-1946.",
        },
        {
            "key": JACK_CIA,
            "stable_url": "https://www.cia.gov/resources/csi/static/Fighting-Doctors-of-OSS.pdf",
            "title": "The Fighting Doctors of the Office of Strategic Services: OSS Medics in Action",
            "author_creator": "Dr. Lester E. Bush; edited by Randy P. Burkett",
            "repository_publisher": "Central Intelligence Agency, Center for the Study of Intelligence",
            "publication_record_date": "2018-09",
            "locator": "PDF physical page 9; printed page 41",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "Studies in Intelligence, volume 62, number 3",
            "rights_notes": "The page was rendered at 300 dpi and visually inspected; the article explicitly says Taylor was a Los Angeles dentist when he joined OSS in August 1942.",
        },
        {
            "key": JACK_NAVY,
            "stable_url": "https://navylog.navymemorial.org/taylor-jack-15",
            "title": "Jack Hendrick Taylor",
            "author_creator": "United States Navy Memorial Navy Log; service memory submitted by CDR Roy A. Mosteller, USNR (Ret.)",
            "repository_publisher": "United States Navy Memorial",
            "locator": "Service summary and 'First Navy SEAL' service memory",
            "access_date": "2026-10-28",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Navy Log",
            "rights_notes": "The page dates Taylor's USNR service from 1941 and describes his Los Angeles dental practice before Navy service and his subsequent OSS recruitment.",
        },
        {
            "key": JACK_USHMM,
            "stable_url": "https://collections.ushmm.org/search/catalog/irn1000313",
            "archival_identifier": "Accession 1994.119.1; RG-60.2008; Film 838",
            "title": "American officers/POWs in Mauthausen",
            "author_creator": "United States Army Signal Corps",
            "repository_publisher": "United States Holocaust Memorial Museum",
            "publication_record_date": "1945",
            "locator": "Catalog description and transcript naming Lieutenant (Senior Grade) Jack H. Taylor, U.S. Navy",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "United States Holocaust Memorial Museum Film and Video Archive",
            "rights_notes": "Used to corroborate full-name identity, naval grade and wartime chronology; no sensitive personal data are reproduced.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {"key": US_ARMY, "organization_id": "28a26f92-78af-5a1a-9c09-a843eb5975b4", "canonical_name": "United States Army", "historical_name": "Army of the United States", "aliases": ["U.S. Army"], "organization_type": "military service", "sector": "military", "country": "United States", "normalization_notes": "Existing canonical organization reused."},
        {"key": US_NAVY, "organization_id": "3960fa8e-a551-56cf-8305-b2b9e4961b9d", "canonical_name": "United States Navy", "historical_name": "United States Navy", "aliases": ["U.S. Navy", "USNR", "United States Naval Reserve"], "organization_type": "military service", "sector": "military", "country": "United States", "normalization_notes": "Existing canonical organization reused; source wording preserves Naval Reserve status."},
        {"key": COI, "organization_id": "0b83aa42-d805-5c8a-bf39-fdf29c36b719", "canonical_name": "Office of the Coordinator of Information", "historical_name": "Office of the Coordinator of Information", "aliases": ["COI"], "organization_type": "federal intelligence and information agency", "sector": "federal_government", "country": "United States", "active_dates": "1941-1942", "normalization_notes": "Existing historical organization reused; it remains distinct from OSS."},
        {"key": SCHENKER, "canonical_name": "Schenker & Co.", "historical_name": "Schenker u. Co.", "aliases": ["Schenker", "Schenker & Co"], "organization_type": "freight forwarding company", "sector": "business_and_industry", "city": "Prague", "country": "Czechoslovakia", "normalization_notes": "Historical source name retained. No modern successor name is substituted."},
        {"key": CHICAGO_TRIBUNE, "canonical_name": "Chicago Tribune", "historical_name": "Chicago Tribune Paris edition and foreign news service", "aliases": ["Chicago Tribune's Paris edition", "Chicago Tribune foreign news service"], "organization_type": "newspaper", "sector": "journalism_and_media", "city": "Paris", "country": "France", "normalization_notes": "The historical Paris operations are preserved in source wording and are not silently merged with a modern corporate entity."},
    ]


def army_affiliation(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    return {
        "key": f"{slug(PEOPLE[row][1])}-occupation-b942",
        "person_id": PEOPLE[row][0],
        "occupation": item["occupation"],
        "relationship_type": "employment",
        "end_date": item["date"],
        "date_precision": f"Historical civilian-occupation code {item['code']} was recorded at Army entry on {item['date']}; no employer or OSS-transfer date is named.",
        "country": "United States",
        "immediate_pre_oss": False,
        "last_civilian_pre_service": False,
        "pre_oss_temporal_basis": "strongly_date_bounded",
        "identity_confidence": "high_confidence",
        "claim_confidence": "medium",
        "source_quality": "A_direct_official",
        "publication_status": "publish_qualified",
        "research_notes": "The historical category is not converted into a named employer, workplace or exact job title.",
    }


def substantive_affiliations() -> list[dict[str, object]]:
    return [
        {"key": "kurt-taub-us-army-b942", "person_id": PEOPLE[25][0], "organization_key": US_ARMY, "organization_name_as_found": "U.S. Army; Counter Intelligence Corps", "role_title": "enlisted soldier assigned to artillery and then the Counter Intelligence Corps", "occupation": "Army enlisted service", "relationship_type": "military_assignment", "start_date": "1943", "end_date": "1943", "date_precision": "The scholarly accounts date his 1943 draft, Army/CIC sequence and placement in the Czech section of OSS in Britain.", "country": "United States and United Kingdom", "immediate_pre_oss": True, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "strongly_date_bounded", "identity_confidence": "high_confidence", "claim_confidence": "high", "source_quality": "C_reputable_contemporary_or_scholarly", "publication_status": "published", "research_notes": "Modeled as the immediate military pathway, not as civilian employment."},
        {"key": "kurt-taub-boston-upholstery-b942", "person_id": PEOPLE[25][0], "organization_name_as_found": "unnamed upholstery shop in Boston", "role_title": "upholstery-shop worker", "occupation": "upholstery work", "relationship_type": "employment", "start_date": "1941", "end_date": "1943", "date_precision": "The university thesis says Taub began work in a Boston upholstery shop after arriving in the United States and joined the Army two years later.", "city": "Boston", "state_or_region": "Massachusetts", "country": "United States", "immediate_pre_oss": False, "last_civilian_pre_service": True, "pre_oss_temporal_basis": "strongly_date_bounded", "identity_confidence": "high_confidence", "claim_confidence": "medium", "source_quality": "C_reputable_contemporary_or_scholarly", "publication_status": "publish_qualified", "research_notes": "The employer's name is not identified; the project does not invent one."},
        {"key": "kurt-taub-schenker-b942", "person_id": PEOPLE[25][0], "organization_key": SCHENKER, "organization_name_as_found": "Schenker u. Co.", "role_title": "employee in the Prague office", "relationship_type": "employment", "start_date": "1926", "end_date": "1938", "date_precision": "The scholarly source dates his move to Prague and employment from 1926; the end year is bounded only by the family's flight after Hitler's advance and is approximate.", "city": "Prague", "country": "Czechoslovakia", "immediate_pre_oss": False, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "high_confidence", "claim_confidence": "high", "source_quality": "C_reputable_contemporary_or_scholarly", "publication_status": "published", "research_notes": "Earlier documented employment; not presented as the immediate pre-OSS role."},
        {"key": "edmond-taylor-coi-b942", "person_id": PEOPLE[35][0], "organization_key": COI, "organization_name_as_found": "Office of Coordinator of Information", "role_title": "psychological-warfare planner", "occupation": "journalist and writer recruited for government planning", "relationship_type": "government_assignment", "start_date": "1941", "end_date": "1942", "date_precision": "The Washington University finding aid explicitly dates COI service to 1941-1942 and OSS planning-board service to 1942-1946.", "country": "United States", "immediate_pre_oss": True, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "explicit_immediate", "identity_confidence": "high_confidence", "claim_confidence": "high", "source_quality": "B_authoritative_institutional", "publication_status": "published", "research_notes": "COI is a government assignment and institutional predecessor, not a civilian employer."},
        {"key": "edmond-taylor-chicago-tribune-b942", "person_id": PEOPLE[35][0], "organization_key": CHICAGO_TRIBUNE, "organization_name_as_found": "Chicago Tribune's Paris edition and foreign news service", "role_title": "reporter, news editor and head of the Paris bureau", "occupation": "journalist", "relationship_type": "employment", "start_date": "1928", "end_date": "1940", "date_precision": "The institutional finding aid documents the 1928 start, foreign news service from 1930 and Paris bureau leadership from 1933; it does not establish that this was the final civilian employer before COI.", "city": "Paris", "country": "France", "immediate_pre_oss": False, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "high_confidence", "claim_confidence": "high", "source_quality": "B_authoritative_institutional", "publication_status": "published", "research_notes": "Published as earlier documented employment, not as the last civilian employer; a final pre-COI employer remains unresolved in this batch."},
        {"key": "jack-taylor-us-navy-b942", "person_id": PEOPLE[44][0], "organization_key": US_NAVY, "organization_name_as_found": "United States Naval Reserve", "role_title": "line officer later serving with the OSS Maritime Unit", "occupation": "naval officer", "relationship_type": "military_assignment", "start_date": "1941", "end_date": "1942-08", "date_precision": "The Navy Memorial dates USNR service from 1941 and describes Donovan's subsequent recruitment; the CIA history dates the OSS join to August 1942.", "country": "United States", "immediate_pre_oss": True, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "strongly_date_bounded", "identity_confidence": "confirmed", "claim_confidence": "high", "source_quality": "B_authoritative_institutional", "publication_status": "published", "research_notes": "The immediate pathway is military, not civilian employment."},
        {"key": "jack-taylor-dental-practice-b942", "person_id": PEOPLE[44][0], "organization_name_as_found": "unnamed Los Angeles dental practice", "role_title": "dentist", "occupation": "dentist", "relationship_type": "employment", "end_date": "1941", "date_precision": "The Navy Memorial describes a well-established Los Angeles practice before Navy service; the CIA history independently says he was a Los Angeles dentist when he joined OSS in August 1942.", "city": "Los Angeles", "state_or_region": "California", "country": "United States", "immediate_pre_oss": False, "last_civilian_pre_service": True, "pre_oss_temporal_basis": "strongly_date_bounded", "identity_confidence": "confirmed", "claim_confidence": "high", "source_quality": "B_authoritative_institutional", "publication_status": "published", "research_notes": "No practice name or separate employing organization is supplied, so none is invented."},
    ]


def claim(row: int, key: str, claim_type: str, text: str, paraphrase: str, identity: str, temporal: str, quality: str, confidence: str, source_links: list[dict[str, object]], notes: str, affiliation_key: str | None = None, publication_status: str | None = None) -> dict[str, object]:
    result: dict[str, object] = {"key": key, "person_id": PEOPLE[row][0], "claim_type": claim_type, "claim_text": text, "evidence_paraphrase": paraphrase, "identity_match_assessment": identity, "temporal_assessment": temporal, "source_quality": quality, "claim_confidence": confidence, "publication_status": publication_status or ("published" if confidence in {"confirmed", "high"} else "publish_qualified"), "match_notes": notes, "sources": source_links}
    if affiliation_key:
        result["affiliation_key"] = affiliation_key
    return result


def army_claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for item in ARMY_OCCUPATIONS:
        row = int(item["row"])
        name = PEOPLE[row][1]
        variant = item.get("variant")
        values.append(claim(row, f"identity-{slug(name)}-b942", "identity", f"The indexed {name} row is a high-confidence match to the reviewed official Army record.", "A nonshared protected identifier connects the visually verified index row to the official Army record.", "High confidence from the private protected-identifier bridge and " + (f"the documented name form {variant}." if variant else "exact full-name agreement."), "The record supports identity and a dated occupation category but does not establish the OSS transfer sequence.", "A_direct_official", "high", [{"source_key": INDEX, "locator_override": f"PDF page 461 row {row}; protected identifier withheld"}, {"source_key": ARMY, "locator_override": "Accepted reviewed identity bridge; protected identifier withheld"}], "No protected identifier is exposed, and no employer or workplace is inferred from the identity bridge."))
        values.append(claim(row, f"occupation-{slug(name)}-b942", "occupation", f"At Army entry on {item['date']}, {name} was recorded in the historical {str(item['occupation']).lower()} category; no employer is identified.", f"The accepted Army record carries civilian-occupation code {item['code']}, decoded from NARA's official code list.", "The occupation belongs only to the reviewed protected-identifier match; the identifier itself is not public.", "Strongly date-bounded to Army entry; it does not establish the immediate pre-OSS affiliation or a named employer.", "A_direct_official", "medium", [{"source_key": ARMY, "locator_override": f"Accepted reviewed identity record; civilian occupation code {item['code']}; protected identifier withheld"}, {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46; Army-entry-date and civilian-occupation fields"}, {"source_key": CODES, "locator_override": item["locator"], "excerpt_override": item["occupation"]}], "The historical category remains a qualified occupation lead, not an employer, workplace, institution or exact title.", f"{slug(name)}-occupation-b942"))
    return values


def substantive_claims() -> list[dict[str, object]]:
    return [
        claim(45, "conflict-james-c-taylor-army-b942", "identity", "The indexed James C. Taylor row is not assigned to the reviewed James H. Taylor Army record because the middle initials conflict.", "The protected identifier points to a closely matching Army record, but C and H are not silently reconciled.", "Conflicting despite the private identifier link because the middle initial is a material disagreement.", "No Army occupation or affiliation is transferred until the personnel file resolves the discrepancy.", "A_direct_official", "conflicting", [{"source_key": INDEX, "locator_override": "PDF page 461 row 45; protected identifier withheld"}, {"source_key": ARMY, "support_type": "contradicts", "locator_override": "Reviewed candidate prints James H Taylor; protected identifier withheld"}], "The candidate is preserved for review, not rejected or published as this person.", publication_status="conflicting"),
        claim(25, "identity-kurt-l-taub-b942", "identity", "Indexed Kurt L. Taub is a high-confidence match to the Brno-born U.S. Army and OSS Czech-section member documented by two scholarly sources.", "The distinctive name, 1911 Brno birth, Army chronology and Czech-section OSS service align.", "High confidence from the distinctive exact indexed name and mutually reinforcing biographical and OSS chronology.", "Both sources place his Army/CIC service immediately before OSS assignment in Britain.", "C_reputable_contemporary_or_scholarly", "high", [{"source_key": INDEX, "locator_override": "PDF page 461 row 25"}, {"source_key": TAUB_IFZ, "locator_override": "PDF physical page 13; printed page 213"}, {"source_key": TAUB_TUL, "locator_override": "PDF physical page 32"}], "No famous-person biography was assigned by name alone; the OSS path and personal chronology provide the bridge."),
        claim(25, "immediate-kurt-taub-army-b942", "immediate_pre_oss_affiliation", "The United States Army, including a Counter Intelligence Corps assignment, is Kurt L. Taub's best-supported immediate pathway into OSS.", "The sources date his 1943 draft and Army/CIC sequence before assignment to the OSS Czech section in Britain.", "High-confidence distinctive identity and aligned wartime chronology.", "Strongly date-bounded military sequence; not described as civilian employment.", "C_reputable_contemporary_or_scholarly", "high", [{"source_key": TAUB_IFZ, "locator_override": "PDF physical page 13; printed page 213"}, {"source_key": TAUB_TUL, "locator_override": "PDF physical page 32"}], "Modeled as military assignment, not employer.", "kurt-taub-us-army-b942"),
        claim(25, "last-civilian-kurt-taub-b942", "last_civilian_pre_service", "Kurt L. Taub worked in an unnamed Boston upholstery shop before entering the U.S. Army in 1943.", "The university thesis says he began shop work after arriving in 1941 and entered the Army two years later.", "High-confidence identity from the distinctive name and shared chronology.", "Strongly date-bounded as the last documented civilian work before Army service; the employer name is unknown.", "C_reputable_contemporary_or_scholarly", "medium", [{"source_key": TAUB_TUL, "locator_override": "PDF physical page 32", "excerpt_override": "V Bostonu v USA začal pracovat v čalounické dílně"}], "The employer is not invented and the qualified claim does not identify a named organization.", "kurt-taub-boston-upholstery-b942"),
        claim(25, "earlier-kurt-taub-schenker-b942", "other_pre_oss_affiliation", "Kurt L. Taub worked for Schenker & Co. in Prague beginning in 1926.", "A scholarly article based partly on the author's interview with Taub identifies the freight-forwarding employer.", "High-confidence identity from distinctive name and biographical chronology.", "Documented prewar employment, not the immediate predecessor to OSS.", "C_reputable_contemporary_or_scholarly", "high", [{"source_key": TAUB_IFZ, "locator_override": "PDF physical page 13; printed page 213", "excerpt_override": "eine Anstellung bei Schenker u. Co."}], "Historical organization wording is preserved without substituting a modern successor.", "kurt-taub-schenker-b942"),
        claim(35, "identity-edmond-l-taylor-b942", "identity", "Indexed Edmond L. Taylor is a high-confidence match to the journalist, COI member and OSS planning-board member documented by Washington University.", "The unusual exact first and last name, direct COI/OSS chronology and wartime Navy service align with the index entry.", "High confidence from a distinctive name and an authoritative institutional finding aid that explicitly documents OSS service.", "The finding aid dates COI service in 1941-1942 and OSS planning-board service in 1942-1946.", "B_authoritative_institutional", "high", [{"source_key": INDEX, "locator_override": "PDF page 461 row 35"}, {"source_key": EDMOND_WASHU, "locator_override": "Biographical Information section"}], "The middle initial is retained from the index; the finding aid's detailed OSS chronology supplies the identity bridge."),
        claim(35, "immediate-edmond-taylor-coi-b942", "immediate_pre_oss_affiliation", "The Office of the Coordinator of Information is Edmond L. Taylor's documented immediate institutional affiliation before OSS planning-board service.", "Washington University's finding aid explicitly places him in COI in 1941-1942 and then the OSS planning board in 1942-1946.", "High-confidence identity from the distinctive name and direct OSS chronology.", "Explicit immediate government-agency sequence.", "B_authoritative_institutional", "high", [{"source_key": EDMOND_WASHU, "locator_override": "Biographical Information section", "excerpt_override": "invited to join the Office of Coordinator of Information (1941-1942)"}], "COI is modeled as a government assignment, not a civilian employer.", "edmond-taylor-coi-b942"),
        claim(35, "earlier-edmond-taylor-tribune-b942", "other_pre_oss_affiliation", "Edmond L. Taylor worked for the Chicago Tribune's Paris edition and foreign news service from 1928 through the prewar period.", "The institutional finding aid traces reporter, news-editor and Paris-bureau leadership roles.", "High-confidence identity from the distinctive name and same finding aid's direct OSS chronology.", "Documented prewar employment; not labeled the last civilian employer because this batch did not resolve every 1940-1941 position.", "B_authoritative_institutional", "high", [{"source_key": EDMOND_WASHU, "locator_override": "Biographical Information section"}], "The project preserves the distinction between earlier documented work and a proven final civilian employer.", "edmond-taylor-chicago-tribune-b942"),
        claim(44, "identity-jack-h-taylor-b942", "identity", "Indexed Jack H. Taylor is confirmed as the Los Angeles dentist, U.S. naval officer and OSS Maritime Unit member documented by CIA, the Navy Memorial and USHMM.", "The full indexed name, Los Angeles occupation, naval service and detailed OSS/POW chronology converge.", "Confirmed by multiple independent official or authoritative institutional sources, including a 1945 USHMM film transcript naming Jack H. Taylor.", "The sources align his 1941 Navy entry and August 1942 OSS entry.", "A_direct_official", "confirmed", [{"source_key": INDEX, "locator_override": "PDF page 461 row 44"}, {"source_key": JACK_CIA, "locator_override": "PDF physical page 9; printed page 41"}, {"source_key": JACK_NAVY, "locator_override": "Service summary and service memory"}, {"source_key": JACK_USHMM, "locator_override": "Catalog description and 1945 film transcript"}], "No protected service number is reproduced."),
        claim(44, "immediate-jack-taylor-navy-b942", "immediate_pre_oss_affiliation", "The United States Naval Reserve is Jack H. Taylor's best-supported immediate military affiliation before OSS recruitment.", "The Navy Memorial dates line-officer service from 1941 and subsequent Donovan recruitment; CIA dates his OSS entry to August 1942.", "Confirmed identity from full-name and converging official/institutional wartime evidence.", "Strongly date-bounded Navy-to-OSS sequence.", "B_authoritative_institutional", "high", [{"source_key": JACK_NAVY, "locator_override": "Service summary and service memory"}, {"source_key": JACK_CIA, "locator_override": "PDF physical page 9; printed page 41"}], "Modeled as a military assignment, not civilian employment.", "jack-taylor-us-navy-b942"),
        claim(44, "last-civilian-jack-taylor-dentist-b942", "last_civilian_pre_service", "Before Navy service, Jack H. Taylor was a dentist in an unnamed Los Angeles dental practice.", "The Navy Memorial describes his prewar practice; CIA independently calls him a Los Angeles dentist when he joined OSS.", "Confirmed identity from full-name and converging Navy, CIA and USHMM evidence.", "Strongly date-bounded before 1941 Navy service; the practice name is not identified.", "B_authoritative_institutional", "high", [{"source_key": JACK_NAVY, "locator_override": "Service memory", "excerpt_override": "a well-established dentist with a practice in Los Angeles"}, {"source_key": JACK_CIA, "locator_override": "PDF physical page 9; printed page 41", "excerpt_override": "a 33-year-old dentist in Los Angeles when he joined OSS"}], "No named employer or practice owner is inferred.", "jack-taylor-dental-practice-b942"),
    ]


def archival_update(row: int, reason: str) -> dict[str, object]:
    person_id, name = PEOPLE[row]
    box = "766" if row <= 36 else "767"
    return {"person_id": person_id, "identity_status": "unresolved", "identity_evidence": f"The visually verified index row supplies {name}, Box {box} and archive location 230/86/41/07. {reason}", "manual_review_required": True, "research_status": "requires_archival_review", "next_action": f"Review Box {box} for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.", "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "high"}


def person_updates() -> list[dict[str, object]]:
    updates = [archival_update(row, reason) for row, reason in UNRESOLVED.items()]
    for row in (26, 27):
        updates.append({"person_id": PEOPLE[row][0], "identity_status": "ambiguous", "identity_evidence": "The adjacent Box 766 rows print J G Tausig and John G Tausig. A John Geyer Tausig biography is a plausible lead, but no OSS, protected-identifier or personnel-file evidence selects either row or proves duplication.", "manual_review_required": True, "possible_duplicate_group": "possible-duplicate:j-g-john-g-tausig-page461-rows26-27", "research_status": "conflicting_sources", "next_action": "Review both Box 766 files together and preserve the two source rows unless direct evidence establishes duplication or identifies the John Geyer Tausig candidate.", "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "critical"})
    for item in ARMY_OCCUPATIONS:
        row = int(item["row"])
        update: dict[str, object] = {"person_id": PEOPLE[row][0], "identity_status": "high_confidence", "identity_evidence": "A nonshared protected identifier connects the visually verified index row to the reviewed official Army record; the full name agrees" + (f" through the documented Army form {item['variant']}." if item.get("variant") else " exactly."), "personnel_category": "enlisted_army_personnel", "commissioned_officer": False, "allied_or_foreign_personnel": False, "manual_review_required": True, "research_status": "occupation_only_found", "next_action": "Review the indexed personnel file to establish the immediate pre-OSS affiliation and named last civilian employer; do not convert the Army occupation category into a workplace.", "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "high"}
        if item.get("variant"):
            update["name_variants"] = [item["variant"]]
        updates.append(update)
    updates.extend([
        {"person_id": PEOPLE[25][0], "identity_status": "high_confidence", "identity_evidence": "The distinctive exact indexed name, Brno/Prague biography, 1943 Army entry and OSS Czech-section chronology align across two scholarly sources.", "personnel_category": "enlisted_army_personnel", "commissioned_officer": False, "allied_or_foreign_personnel": False, "manual_review_required": True, "research_status": "completed", "next_action": "Review Box 766 for the named Boston upholstery employer and exact Army/CIC transfer dates.", "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "medium"},
        {"person_id": PEOPLE[35][0], "identity_status": "high_confidence", "identity_evidence": "The distinctive name and Washington University finding aid directly connect the journalist to COI, the OSS planning board and wartime Navy service.", "personnel_category": "commissioned_naval_officer", "commissioned_officer": True, "allied_or_foreign_personnel": False, "manual_review_required": True, "research_status": "completed", "next_action": "Review Box 766 and contemporary 1940-1941 records to resolve his final civilian employer before COI without conflating it with earlier Chicago Tribune work.", "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "medium"},
        {"person_id": PEOPLE[44][0], "identity_status": "confirmed", "identity_evidence": "The full indexed name, Los Angeles dental occupation, USNR service, OSS Maritime Unit chronology and 1945 USHMM film transcript converge across independent official and institutional sources.", "name_variants": ["Jack Hendrick Taylor", "Jack Hedrick Taylor"], "personnel_category": "commissioned_naval_officer", "commissioned_officer": True, "allied_or_foreign_personnel": False, "manual_review_required": False, "research_status": "completed", "next_action": "Review Box 767 only if the exact historical name of the Los Angeles dental practice is needed.", "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "low"},
        {"person_id": PEOPLE[45][0], "identity_status": "conflicting", "identity_evidence": "A protected identifier points to a reviewed James H. Taylor Army record, but the index prints James C. Taylor. The material middle-initial conflict is preserved and no Army data are transferred.", "manual_review_required": True, "research_status": "conflicting_sources", "next_action": "Review the Box 767 personnel file and the Army source together to resolve the C/H middle-initial conflict before assigning any occupation or affiliation.", "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "critical"},
        {"person_id": PEOPLE[46][0], "identity_status": "probable", "identity_evidence": "The existing probable Index of American Design lead remains qualified because the reviewed NGA and CIA sources do not supply the middle initial H or a direct Box 767 bridge.", "manual_review_required": True, "research_status": "needs_identity_review", "next_action": "Review Box 767 for a middle-name or personnel-file bridge before upgrading the existing WPA Index of American Design affiliation.", "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "critical"},
    ])
    return updates


def research_attempts() -> list[dict[str, object]]:
    army_rows = {int(item["row"]) for item in ARMY_OCCUPATIONS}
    attempts: list[dict[str, object]] = []
    for row in sorted(PEOPLE):
        person_id, name = PEOPLE[row]
        if row in UNRESOLVED:
            outcome, reviewed, rejected, detail = "no_result", 7, 5, UNRESOLVED[row]
        elif row in (26, 27):
            outcome, reviewed, rejected, detail = "candidate_found", 8, 5, "A John Geyer Tausig biography is plausible, but the adjacent J G and John G rows and lack of an OSS or Box bridge prevent assignment."
        elif row in army_rows:
            outcome, reviewed, rejected, detail = "source_reviewed", 8, 4, "An accepted protected-identifier Army bridge supports identity and a dated historical occupation category, not an employer."
        elif row == 25:
            outcome, reviewed, rejected, detail = "source_reviewed", 10, 4, "Two scholarly sources support a high-confidence Army-to-OSS pathway, an unnamed Boston upholstery-shop job and earlier Schenker employment."
        elif row == 35:
            outcome, reviewed, rejected, detail = "source_reviewed", 10, 4, "Washington University's finding aid supports a high-confidence COI-to-OSS path and earlier Chicago Tribune employment; the final civilian employer remains unresolved."
        elif row == 44:
            outcome, reviewed, rejected, detail = "source_reviewed", 11, 3, "CIA, Navy Memorial and USHMM evidence confirms the dentist-to-Navy-to-OSS chronology without inventing a dental-practice name."
        elif row == 45:
            outcome, reviewed, rejected, detail = "candidate_found", 8, 4, "The protected identifier points to James H. Taylor, while the index prints James C. Taylor; the conflict is preserved and no Army fields are transferred."
        elif row == 46:
            outcome, reviewed, rejected, detail = "candidate_found", 7, 4, "The prior qualified Index of American Design affiliation was rechecked and retained as probable because no middle-initial or Box 767 bridge was found."
        else:
            raise AssertionError(f"Missing Batch 942 outcome for row {row}")
        attempts.append({"key": f"page461-row{row}-{slug(name)}-b942", "person_id": person_id, "source_adapter": "manual_staged_protocol", "query_text": f"{name}; NARA index and public Archives context; CIA Reading Room; exact-name and meaningful variants; OSS, rank and military clues; employer and occupation 1940; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Boxes 766-767; protected identifiers used privately only when defensible", "query_variant_type": "staged_identity_employment_archival_protocol_batch_942", "started_at": "2026-10-28T12:00:00Z", "completed_at": "2026-10-28T16:20:00Z", "outcome": outcome, "sources_reviewed": reviewed, "candidate_sources_rejected": rejected, "rejection_reasons": "Unbridged namesakes, search snippets, family-tree assertions, modern people-finder pages, postwar-only leads and sources without an OSS, protected-identifier or Box-file bridge were not assigned.", "research_notes": f"{detail} The index page and admitted PDF pages were visually checked. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA Catalog API call was made.", "next_action": "Review the indexed personnel file for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before military service.", "attempt_number": 2 if row == 46 else 1, "research_agent_version": "before-oss-b942-v1"})
    return attempts


def main() -> None:
    affiliations = [army_affiliation(item) for item in ARMY_OCCUPATIONS] + substantive_affiliations()
    claims = army_claims() + substantive_claims()
    bundle = {"bundle_version": "batch-942-v1", "reviewer": "Before OSS Batch 942 evidence review", "sources": sources(), "organizations": organizations(), "affiliations": affiliations, "claims": claims, "person_updates": person_updates(), "research_attempts": research_attempts()}
    EvidenceBundle.model_validate(bundle)
    OUTPUT.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
