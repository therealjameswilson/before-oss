#!/usr/bin/env python3
"""Generate the reviewed Batch 903 evidence bundle from audited constants."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "research/evidence-page441-spiro-to-sporborg-review_batch-903_2026-10-25.json"

INDEX = "nara-index-b903"
ARMY = "army-bulk-b903"
TECH = "army-tech-b903"
CODES = "army-codes-b903"
LOC = "loc-boris-spiroff-b903"
NARA_SPORBORG = "nara-sporborg-decoration-b903"
GAZETTE = "gazette-sporborg-b903"
THAMES = "thames-sporborg-b903"
PORTSMOUTH = "portsmouth-sporborg-b903"


PEOPLE = {
    24: ("11cec430-f1ae-54a7-a7f8-88bcf9e56e3f", "Grace M Spiro"),
    25: ("530dee8f-d811-52b3-9ce6-947fd8437f20", "Peter Spiro"),
    27: ("e320d8b6-f26d-571e-8c55-cf3d3a467fd6", "Boris Spiroff"),
    29: ("5bb9f08a-0dc5-5b05-bf5c-3501904dd704", "William J Spiropoulos"),
    31: ("444d1c7f-7f85-5878-b878-d132b50891b3", "Milton A Spitz"),
    32: ("196e731e-4de0-5486-a7a0-7b145ea2cba7", "Walter F Spitzform"),
    33: ("797c8fe4-dfef-5653-a86c-7a7f6691b0f1", "Leo X Spitzmiller"),
    34: ("9900da1b-432b-5534-8360-6cdd50145779", "Louis Spivack"),
    35: ("d4181030-6808-51e2-b300-b1b68df03c83", "Sydney S Spivack"),
    36: ("369d1bb2-2282-5067-a13b-bf14bb63c9c2", "Joel T Spivey"),
    37: ("a8fc7cbb-2157-578d-8c17-e61621c439c7", "Price C Spivey"),
    38: ("aa59166b-a63b-5de3-b1a8-67f72c9eae9a", "Robert D Splain"),
    39: ("013a1f06-583e-5f24-900b-332459b484db", "Chester J Splawski"),
    41: ("398dbd77-1516-521b-b9a9-10a0f179f94b", "William Spoeleof"),
    42: ("13f8243d-e6dc-521a-b442-65065c364571", "Evalea Spoesser"),
    43: ("0f562200-3554-5fdc-9dcd-7994d1b3a83f", "Carlton W Spohn"),
    44: ("e7e1f08f-2602-5c99-a721-fcc5cd0e439f", "John Spondike"),
    45: ("7e5fad17-c743-5fef-8091-40fa9dddc734", "Chester L Spooner"),
    46: ("38e803b7-7115-5fcc-a55c-7e49d04dfb43", "Henry N Sporborg"),
}


ARMY_OCCUPATIONS = [
    {"row": 25, "slug": "peter-spiro", "date": "1942-10-24", "code": "688", "occupation": "Occupations in mechanical treatment of metals, not elsewhere classified", "relationship_type": "employment", "locator": "PDF physical page 174; category 6-88"},
    {"row": 29, "slug": "william-j-spiropoulos", "date": "1942-09-15", "code": "061", "occupation": "Radio operators", "relationship_type": "employment", "locator": "PDF physical page 171; category 0-61"},
    {"row": 34, "slug": "louis-spivack", "date": "1942-07-24", "code": "072", "occupation": "Retail managers", "relationship_type": "employment", "locator": "PDF physical page 171; category 0-72"},
    {"row": 36, "slug": "joel-t-spivey", "date": "1942-06-26", "code": "221", "occupation": "Bartenders", "relationship_type": "employment", "locator": "PDF physical page 172; category 2-21"},
    {"row": 39, "slug": "chester-j-splawski", "date": "1941-10-20", "code": "736", "occupation": "Chauffeurs and drivers, bus, taxi, truck, and tractor", "relationship_type": "employment", "locator": "PDF physical page 174; category 7-36"},
    {"row": 44, "slug": "john-spondike", "date": "1943-04-02", "code": "992", "occupation": "Students", "relationship_type": "student", "locator": "PDF physical page 304; corrected Code No. 30 category 9-92"},
]


UNRESOLVED = {
    31: "Exact-name and institutional searches did not identify which Milton A Spitz is represented or establish a pre-OSS affiliation.",
    32: "A 1940 amateur-radio listing and postwar Foreign Service record for a Walter F Spitzform lack a second identifier linking them to this index row.",
    33: "Postwar patent and namesake results did not establish Leo X Spitzmiller's pre-OSS identity or employment.",
    35: "Exact-name, occupation, obituary and archival searches did not produce a defensible Sydney S Spivack identity bridge.",
    37: "Exact-name and variant searches did not connect Price C Spivey to a dated employer or pre-OSS institution.",
    38: "Exact-name, employer and obituary searches did not establish the indexed Robert D Splain's identity or chronology.",
    41: "The indexed spelling produced no reliable identity, occupation or employer match for William Spoeleof.",
    42: "The distinctive indexed name produced no source connecting Evalea Spoesser to OSS chronology or a named employer.",
    43: "A Coast Guard namesake lacks corroborating identifiers and is not assigned to the Carlton W Spohn index row.",
}


def archive_box(row: int) -> str:
    if row <= 35:
        return "733"
    if row == 39:
        return "733 and 734"
    return "734"


def sources() -> list[dict[str, object]]:
    return [
        {"key": INDEX, "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf", "archival_identifier": "RG 226, Entry A1-224, Boxes 733-734", "title": "OSS Personnel Files from Excel", "author_creator": "National Archives and Records Administration", "repository_publisher": "National Archives and Records Administration", "publication_record_date": "2010-12-23", "locator": "PDF page 441, rows 24-46; checked against layout-preserving text and a rendered page image", "access_date": "2026-10-25", "source_quality": "A_direct_official", "collection_name": "Records of the Office of Strategic Services, Record Group 226", "rights_notes": "All 23 printed rows remain immutable. Four exact duplicate pairs are linked only through matching protected identifiers; the adjacent Grace M Spiro rows remain separate. Full protected identifiers remain private."},
        {"key": ARMY, "stable_url": "https://catalog.archives.gov/id/1263923", "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357", "title": "Electronic Army Serial Number Merged File, ca. 1938-1946", "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration", "repository_publisher": "National Archives and Records Administration", "publication_record_date": "1938-1946; merged file created 2002", "locator": "Official unrestricted ASNEF.FIN.DAT; nine accepted row-level identity bridges representing six people and one rejected substantive name conflict", "access_date": "2026-10-25", "source_quality": "A_direct_official", "collection_name": "World War II Army Enlistment Records", "document_number": "ASNEF.FIN.DAT", "rights_notes": "No raw row or full protected identifier is retained in public assets. Coded occupations identify no employer, and a non-hit is not negative proof."},
        {"key": TECH, "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf", "archival_identifier": "NN3-064-03-008; National Archives Identifier 1263923", "title": "World War II Army Enlistment Records: Reference Copy of Technical Documentation", "author_creator": "National Archives and Records Administration", "repository_publisher": "National Archives at College Park - Electronic Records", "publication_record_date": "1994-2005; reference copy modified 2011", "locator": "PDF physical pages 44-46; identifier, name, Army-entry-date, grade and civilian-occupation fields", "access_date": "2026-10-25", "source_quality": "A_direct_official", "collection_name": "World War II Army Enlistment Records technical documentation", "rights_notes": "Used to interpret selected fields only; source damage, coding limits and incomplete coverage remain applicable."},
        {"key": CODES, "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1CL_SD.pdf", "archival_identifier": "National Archives Identifier 1263923; Code No. 30", "title": "NARA Compiled Code Lists for the Electronic Army Serial Number Merged File", "author_creator": "National Archives and Records Administration", "repository_publisher": "National Archives at College Park - Electronic Records", "publication_record_date": "2011-01-12; modified 2011-03-17", "locator": "PDF physical pages 171-174 and 304; categories 061, 072, 221, 688, 736 and corrected 992 visually checked", "access_date": "2026-10-25", "source_quality": "A_direct_official", "collection_name": "World War II Army Enlistment Records technical documentation", "rights_notes": "Historical labels identify neither employers nor workplaces. The malformed John Spondike grade field is not published."},
        {"key": LOC, "stable_url": "https://www.loc.gov/item/afc2001001.02029/", "archival_identifier": "AFC/2001/001/2029", "title": "Boris Robert Spiroff Collection", "author_creator": "Boris Robert Spiroff", "repository_publisher": "Veterans History Project, American Folklife Center, Library of Congress", "publication_record_date": "1937-1953; collection record", "locator": "Veterans History Project service summary; Army service 1937-1945 and OSS recruitment in 1943", "access_date": "2026-10-25", "source_quality": "A_direct_official", "collection_name": "Veterans History Project Collection", "rights_notes": "Project-authored paraphrases only. No manuscript images or copyrighted narrative text are republished."},
        {"key": NARA_SPORBORG, "stable_url": "https://www.archives.gov/files/research/jfk/releases/104-10165-10120.pdf", "archival_identifier": "104-10165-10120", "title": "SO Branch Decorations Board list", "repository_publisher": "National Archives and Records Administration", "locator": "PDF page 7; Henry N. Sporborg entry", "access_date": "2026-10-25", "source_quality": "A_direct_official", "collection_name": "JFK Assassination Records releases", "rights_notes": "The record describes a British SOE officer's assistance to SO/OSS; it is not used to recast him as a U.S. OSS employee."},
        {"key": GAZETTE, "stable_url": "https://www.thegazette.co.uk/London/issue/36866/supplement/5/data.pdf", "archival_identifier": "London Gazette issue 36866, supplement page 5", "title": "Supplement to The London Gazette, 1 January 1945", "repository_publisher": "The Gazette", "publication_record_date": "1945-01-01", "locator": "Page 5; Lieutenant-Colonel Henry Nathan Sporborg, Civil Assistant, War Office", "access_date": "2026-10-25", "source_quality": "A_direct_official", "rights_notes": "Official corroboration of full name, rank and War Office status."},
        {"key": THAMES, "stable_url": "https://www.thamesrcarchive.co.uk/index.php/sporborg-h-n", "archival_identifier": "TRC-A-0195", "title": "Sporborg, Henry Nathan", "repository_publisher": "Thames Rowing Club Archive", "locator": "Authority record; authorized name, dates, Slaughter & May partnership and SOE liaison function", "access_date": "2026-10-25", "source_quality": "B_authoritative_institutional", "rights_notes": "Authority data only; the record cites the Oxford Dictionary of National Biography."},
        {"key": PORTSMOUTH, "stable_url": "https://pure.port.ac.uk/ws/portalfiles/portal/80427900/Venner_Acc_Historians_Journal_revision_2.pdf", "title": "John Boldero Venner: Chartered Accountant and SOE Finance Director", "repository_publisher": "University of Portsmouth Research Portal; Accounting Historians Journal accepted manuscript", "publication_record_date": "2023", "locator": "Accepted manuscript page 11; Sporborg's Slaughter & May partnership, early-war Ministry of Economic Warfare service and move into SOE", "access_date": "2026-10-25", "source_quality": "C_reputable_contemporary_or_scholarly", "rights_notes": "Used for project-authored chronology only; no long excerpt is retained."},
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {"key": "us-army-b903", "organization_id": "24facf23-e75a-54f2-a37a-0ef1509bc18a", "canonical_name": "United States Army", "historical_name": "U.S. Army", "aliases": ["Army of the United States"], "organization_type": "military_service", "sector": "military", "country": "United States", "normalization_notes": "Reuses the reviewed canonical organization and is modeled as a military assignment, not a civilian employer."},
        {"key": "soe-b903", "organization_id": "15cd00a2-f691-5c45-8ae4-b1a9b3cf1a2e", "canonical_name": "Special Operations Executive", "historical_name": "Special Operations Executive", "aliases": ["SOE"], "organization_type": "British wartime government organization", "sector": "federal_government", "country": "United Kingdom", "active_dates": "1940-1946", "normalization_notes": "Reuses an existing canonical organization; retained separately from OSS."},
        {"key": "slaughter-may-b903", "canonical_name": "Slaughter and May", "historical_name": "Slaughter & May", "aliases": ["Slaughter and May"], "organization_type": "law firm", "sector": "law", "city": "London", "country": "United Kingdom", "normalization_notes": "The historical ampersand form is preserved as found. No successor or merger inference is made."},
    ]


def army_affiliation(item: dict[str, object]) -> dict[str, object]:
    person_id, _ = PEOPLE[int(item["row"])]
    student = item["relationship_type"] == "student"
    return {"key": f"{item['slug']}-occupation-b903", "person_id": person_id, "relationship_type": item["relationship_type"], "occupation": "Student; institution not recorded" if student else item["occupation"], "end_date": item["date"], "date_precision": f"Historical civilian-occupation code {item['code']} was recorded at Army entry on {item['date']}; no employer or OSS-transfer date is named.", "country": "United States", "immediate_pre_oss": False, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "strongly_date_bounded", "identity_confidence": "high_confidence", "claim_confidence": "medium", "source_quality": "A_direct_official", "publication_status": "publish_qualified", "research_notes": "The historical category is not converted into a named employer, institution, workplace or exact title."}


def army_identity_claim(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    person_id, name = PEOPLE[row]
    variant = " The official Army spelling is Louis Spivak and is retained as a documented variant." if row == 34 else ""
    return {"key": f"identity-{item['slug']}-b903", "person_id": person_id, "claim_type": "identity", "claim_text": f"The indexed {name} row is a high-confidence match to the reviewed official Army record.{variant}", "evidence_paraphrase": "A nonshared protected identifier connects the visually verified index row to the official Army record.", "identity_match_assessment": "High confidence from the protected-identifier bridge and exact name agreement, or a minor documented spelling variant for Louis Spivack.", "temporal_assessment": "The Army record supports identity and a dated occupation category; it does not establish the OSS transfer sequence.", "source_quality": "A_direct_official", "claim_confidence": "high", "publication_status": "published", "match_notes": "No protected identifier is exposed, and no employer or workplace is inferred from the coded field.", "sources": [{"source_key": INDEX, "locator_override": f"PDF page 441 row {row}; duplicate companion row included where present; protected identifier withheld"}, {"source_key": ARMY, "locator_override": "Accepted reviewed identity bridge; protected identifier withheld"}]}


def army_occupation_claim(item: dict[str, object]) -> dict[str, object]:
    person_id, name = PEOPLE[int(item["row"])]
    category = "student category" if item["relationship_type"] == "student" else f"historical {str(item['occupation']).lower()} category"
    return {"key": f"occupation-{item['slug']}-b903", "person_id": person_id, "affiliation_key": f"{item['slug']}-occupation-b903", "claim_type": "occupation", "claim_text": f"At Army entry on {item['date']}, {name} was recorded in the {category}; no employer is identified.", "evidence_paraphrase": f"The accepted Army record carries civilian-occupation code {item['code']}, decoded from NARA's official code list.", "identity_match_assessment": "The occupation belongs only to the reviewed protected-identifier match; the identifier itself is not public.", "temporal_assessment": "Strongly date-bounded to Army entry; it does not establish the immediate pre-OSS affiliation or a named employer.", "source_quality": "A_direct_official", "claim_confidence": "medium", "publication_status": "publish_qualified", "match_notes": "The historical category is a qualified lead, not an employer, workplace, institution or exact title.", "sources": [{"source_key": ARMY, "locator_override": f"Accepted reviewed identity record; civilian occupation code {item['code']}; protected identifier withheld"}, {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46; Army-entry-date and civilian-occupation fields"}, {"source_key": CODES, "locator_override": item["locator"], "excerpt_override": item["occupation"]}]}


def substantive_affiliations() -> list[dict[str, object]]:
    return [
        {"key": "boris-spiroff-us-army-b903", "person_id": PEOPLE[27][0], "organization_key": "us-army-b903", "organization_name_as_found": "Army", "role_title": "enlisted soldier; later First Sergeant", "relationship_type": "military_assignment", "start_date": "1937", "end_date": "1943", "date_precision": "Library of Congress dates Army service from 1937 and states that OSS recruited him in 1943; no exact transfer date is given.", "country": "United States", "immediate_pre_oss": True, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "explicit_immediate", "identity_confidence": "confirmed", "claim_confidence": "confirmed", "source_quality": "A_direct_official", "publication_status": "published", "research_notes": "The Army assignment is the explicit immediate predecessor to OSS recruitment and is not labeled a civilian employer."},
        {"key": "henry-sporborg-soe-b903", "person_id": PEOPLE[46][0], "organization_key": "soe-b903", "organization_name_as_found": "SOE", "role_title": "Vice-Chief; principal liaison officer", "relationship_type": "government_assignment", "start_date": "1940", "end_date": None, "date_precision": "Scholarly chronology places him in SOE from its 1940 formation; the official NARA record identifies him as Vice-Chief when assisting SO/OSS. No OSS employment is implied.", "country": "United Kingdom", "immediate_pre_oss": True, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "explicit_immediate", "identity_confidence": "confirmed", "claim_confidence": "confirmed", "source_quality": "A_direct_official", "publication_status": "published", "research_notes": "This is the documented allied institutional affiliation relevant to the OSS index file, not U.S. OSS employment."},
        {"key": "henry-sporborg-slaughter-may-b903", "person_id": PEOPLE[46][0], "organization_key": "slaughter-may-b903", "organization_name_as_found": "Slaughter & May", "role_title": "partner", "occupation": "solicitor", "relationship_type": "employment", "start_date": None, "end_date": "1939", "date_precision": "Institutional and scholarly sources identify him as a partner before early-war Ministry of Economic Warfare and SOE service; no exact separation date is available.", "city": "London", "country": "United Kingdom", "immediate_pre_oss": False, "last_civilian_pre_service": True, "pre_oss_temporal_basis": "probable_immediate", "identity_confidence": "confirmed", "claim_confidence": "medium", "source_quality": "B_authoritative_institutional", "publication_status": "publish_qualified", "research_notes": "Best-supported last civilian employer before wartime government service. The end year reflects entry into early-war government work, not an exact firm departure date."},
    ]


def substantive_claims() -> list[dict[str, object]]:
    return [
        {"key": "identity-boris-spiroff-b903", "person_id": PEOPLE[27][0], "claim_type": "identity", "claim_text": "The indexed Boris Spiroff is confirmed as Army First Sergeant Boris Robert Spiroff, recruited by OSS in 1943 for a Balkans Operational Group.", "evidence_paraphrase": "The Library of Congress record gives his full name, Army service, OSS unit and 1943 recruitment; the NARA index preserves two matching rows.", "identity_match_assessment": "Confirmed from the distinctive name, official OSS/Army chronology and the matching protected identifier on both index rows.", "temporal_assessment": "Army service began in 1937 and OSS recruitment occurred in 1943.", "source_quality": "A_direct_official", "claim_confidence": "confirmed", "publication_status": "published", "match_notes": "The profile uses the documented role and does not generalize OSS personnel as spies or operatives.", "sources": [{"source_key": INDEX, "locator_override": "PDF page 441 rows 27-28; protected identifier withheld"}, {"source_key": LOC}]},
        {"key": "immediate-boris-spiroff-army-b903", "person_id": PEOPLE[27][0], "affiliation_key": "boris-spiroff-us-army-b903", "claim_type": "immediate_pre_oss_affiliation", "claim_text": "The United States Army is Boris Robert Spiroff's documented immediate pre-OSS affiliation.", "evidence_paraphrase": "Library of Congress dates his Army service from 1937 and states that his language skills attracted OSS recruiters in 1943.", "identity_match_assessment": "Confirmed by the official collection record and the duplicate protected-identifier index rows.", "temporal_assessment": "Explicit immediate sequence: Army service preceded OSS recruitment in 1943.", "source_quality": "A_direct_official", "claim_confidence": "confirmed", "publication_status": "published", "match_notes": "This is a military assignment, not a civilian employer. No earlier civilian employer is identified.", "sources": [{"source_key": LOC}]},
        {"key": "identity-henry-sporborg-b903", "person_id": PEOPLE[46][0], "claim_type": "identity", "claim_text": "The indexed Henry N Sporborg is confirmed as Lieutenant-Colonel Henry Nathan Sporborg, Vice-Chief of Britain's Special Operations Executive.", "evidence_paraphrase": "NARA names Henry N. Sporborg as SOE Vice-Chief; the Gazette supplies the full name and rank, matching the index's British Army note.", "identity_match_assessment": "Confirmed by exact name and middle initial, British military status, rank and the official SOE/OSS context.", "temporal_assessment": "The sources place him in wartime SOE and the War Office; they do not make him a U.S. OSS employee.", "source_quality": "A_direct_official", "claim_confidence": "confirmed", "publication_status": "published", "match_notes": "The public profile preserves the distinction between an allied liaison file and U.S. OSS employment.", "sources": [{"source_key": INDEX, "locator_override": "PDF page 441 row 46; note 'Br. Army'"}, {"source_key": NARA_SPORBORG}, {"source_key": GAZETTE}]},
        {"key": "immediate-henry-sporborg-soe-b903", "person_id": PEOPLE[46][0], "affiliation_key": "henry-sporborg-soe-b903", "claim_type": "immediate_pre_oss_affiliation", "claim_text": "Henry Sporborg's documented allied affiliation in the OSS relationship was Britain's Special Operations Executive, where he served as Vice-Chief.", "evidence_paraphrase": "A NARA record states that SOE Vice-Chief Henry N. Sporborg materially helped establish SO/OSS.", "identity_match_assessment": "Confirmed by the official NARA record, Gazette rank and the index's British Army note.", "temporal_assessment": "Explicit contemporaneous institutional relationship to the establishment of SO/OSS; not a claim of U.S. OSS employment.", "source_quality": "A_direct_official", "claim_confidence": "confirmed", "publication_status": "published", "match_notes": "SOE remains a separate British organization in the data model.", "sources": [{"source_key": NARA_SPORBORG}, {"source_key": THAMES, "support_type": "context_only"}]},
        {"key": "last-civilian-henry-sporborg-slaughter-may-b903", "person_id": PEOPLE[46][0], "affiliation_key": "henry-sporborg-slaughter-may-b903", "claim_type": "last_civilian_pre_service", "claim_text": "Slaughter & May is Henry Sporborg's best-supported last civilian employer before early-war British government and SOE service.", "evidence_paraphrase": "An institutional authority record calls him a partner; a scholarly chronology places that legal career before Ministry of Economic Warfare and SOE service.", "identity_match_assessment": "Confirmed identity from distinctive full name and matching wartime roles.", "temporal_assessment": "Probable immediate civilian predecessor; the sequence is supported but no exact firm separation date is stated.", "source_quality": "B_authoritative_institutional", "claim_confidence": "medium", "publication_status": "publish_qualified", "match_notes": "The claim is visibly qualified and does not infer an exact end date.", "sources": [{"source_key": THAMES}, {"source_key": PORTSMOUTH}]},
        {"key": "conflict-chester-spooner-b903", "person_id": PEOPLE[45][0], "claim_type": "identity", "claim_text": "Chester L Spooner's protected identifier points to an Army record under the materially different name Peter Messinger.", "evidence_paraphrase": "The protected identifier agrees, but the names do not; the Army occupation and identity are therefore withheld.", "identity_match_assessment": "Conflicting. A protected identifier cannot override a substantive full-name disagreement without personnel-file evidence.", "temporal_assessment": "No Army occupation or date is transferred while identity remains conflicting.", "source_quality": "A_direct_official", "claim_confidence": "conflicting", "publication_status": "conflicting", "match_notes": "Review the Box 734 file before correcting an identifier, merging people or accepting the candidate.", "sources": [{"source_key": INDEX, "locator_override": "PDF page 441 row 45; protected identifier withheld"}, {"source_key": ARMY, "support_type": "context_only", "locator_override": "Rejected substantive name-conflict candidate; protected identifier withheld"}]},
    ]


def archive_update(row: int, reason: str) -> dict[str, object]:
    person_id, name = PEOPLE[row]
    box = archive_box(row)
    return {"person_id": person_id, "identity_status": "unresolved", "identity_evidence": f"The visually verified index row supplies {name}, Box {box} and archive location, but the staged official-context, CIA Reading Room, exact-name, occupation, employer, obituary, institutional, directory, newspaper and archival protocol found no defensible identity bridge. {reason}", "manual_review_required": True, "research_status": "requires_archival_review", "next_action": f"Review the indexed Box {box} personnel file for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.", "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "critical"}


def person_updates() -> list[dict[str, object]]:
    updates = [archive_update(row, reason) for row, reason in UNRESOLVED.items()]
    updates.append({"person_id": PEOPLE[24][0], "identity_status": "ambiguous", "identity_evidence": "This is the second of two adjacent, separately printed Grace M Spiro rows. Neither has a protected identifier, so name alone cannot establish duplication.", "manual_review_required": True, "possible_duplicate_group": "same-name:grace-m-spiro-page441", "research_status": "needs_identity_review", "next_action": "Review both Box 733 and Box 734 personnel files together before merging the rows or assigning an external biography.", "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "critical"})
    for item in ARMY_OCCUPATIONS:
        row = int(item["row"])
        person_id, _ = PEOPLE[row]
        update = {"person_id": person_id, "identity_status": "high_confidence", "identity_evidence": "A nonshared protected identifier connects the visually verified index row to the reviewed official Army record. The occupation field remains separate from employer and immediate-affiliation claims.", "personnel_category": "enlisted_army_personnel", "commissioned_officer": False, "allied_or_foreign_personnel": False, "manual_review_required": True, "research_status": "occupation_only_found", "next_action": f"Review the indexed Box {archive_box(row)} personnel file to identify the immediate pre-OSS affiliation and last civilian employer; do not convert the Army category into a named employer or institution.", "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "high"}
        if row == 34:
            update["name_variants"] = ["Louis Spivak"]
            update["identity_evidence"] = "A nonshared protected identifier links the index row to the official Army spelling Louis Spivak. The one-letter orthographic variant is documented rather than silently corrected."
        updates.append(update)
    updates.extend([
        {"person_id": PEOPLE[27][0], "identity_status": "confirmed", "identity_evidence": "The Library of Congress supplies the distinctive full name, Army service, OSS recruitment in 1943 and Balkans Operational Group assignment; both printed index rows share a protected identifier.", "name_variants": ["Boris Robert Spiroff", "Bob Spiroff"], "personnel_category": "enlisted_army_personnel", "commissioned_officer": False, "allied_or_foreign_personnel": False, "manual_review_required": False, "research_status": "completed", "next_action": "Optional archival review may seek any civilian employment before his 1937 Army entry; no civilian employer is inferred from current sources.", "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "medium"},
        {"person_id": PEOPLE[45][0], "identity_status": "conflicting", "identity_evidence": "The protected identifier points to an official Army record under the materially different name Peter Messinger. The conflict prevents identity or occupation transfer.", "manual_review_required": True, "possible_duplicate_group": "identifier-conflict:chester-l-spooner-peter-messinger", "research_status": "conflicting_sources", "next_action": "Review the Box 734 personnel file before correcting the index identifier, accepting the Army record or linking another person.", "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "critical"},
        {"person_id": PEOPLE[46][0], "identity_status": "confirmed", "identity_evidence": "Exact name and middle initial, British Army note, lieutenant-colonel rank and official NARA evidence identifying SOE Vice-Chief Henry N. Sporborg confirm the identity.", "name_variants": ["Henry Nathan Sporborg", "Harry Sporborg"], "personnel_category": "foreign_or_allied_military_personnel", "commissioned_officer": True, "allied_or_foreign_personnel": True, "manual_review_required": True, "research_status": "verified_employer_found", "next_action": "Review the Box 734 allied liaison file and British records to refine Slaughter & May dates and the exact administrative basis for his OSS index file.", "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "high"},
    ])
    return updates


def research_attempts() -> list[dict[str, object]]:
    attempts = []
    evidence_rows = {25, 27, 29, 34, 36, 39, 44, 45, 46}
    for row, (person_id, name) in PEOPLE.items():
        if row == 24:
            note, reviewed, rejected = "The adjacent same-name row prevents a name-only identity assignment; both personnel files require comparison.", 6, 8
        elif row in UNRESOLVED:
            note, reviewed, rejected = UNRESOLVED[row], 5, 6
        elif row in {25, 29, 34, 36, 39, 44}:
            note, reviewed, rejected = "The accepted protected-identifier bridge supports identity and a dated historical occupation or student category, but not a named employer or immediate OSS chronology.", 7, 5
        elif row == 27:
            note, reviewed, rejected = "The Library of Congress collection confirms Boris Robert Spiroff's Army service from 1937 and explicit OSS recruitment in 1943.", 9, 4
        elif row == 45:
            note, reviewed, rejected = "The Army candidate is withheld because its protected identifier points to the materially different name Peter Messinger.", 7, 7
        elif row == 46:
            note, reviewed, rejected = "NARA confirms Henry N. Sporborg as SOE Vice-Chief who assisted SO/OSS; institutional and scholarly sources document Slaughter & May before early-war government service.", 11, 4
        else:
            raise AssertionError(row)
        attempts.append({"key": f"page441-row{row}-{name.lower().replace(' ', '-')}-b903", "person_id": person_id, "source_adapter": "manual_staged_protocol", "query_text": f"{name}; NARA/index context; CIA Reading Room exact-name check; OSS and rank variants; employer and occupation; obituary, institutional, newspaper, directory and archival searches; Box {archive_box(row)}; protected-identifier Army crosswalk where available", "query_variant_type": "staged_identity_employment_archival_protocol_batch_903", "started_at": "2026-10-25T20:05:00Z", "completed_at": "2026-10-25T21:46:00Z", "outcome": "source_reviewed" if row in evidence_rows else "candidate_rejected", "sources_reviewed": reviewed, "candidate_sources_rejected": rejected, "rejection_reasons": "Unbridged namesakes, chronologically irrelevant results, postwar-only leads and materially conflicting candidates were not assigned." if row in evidence_rows else note, "research_notes": ("Reviewed evidence established a supported, qualified or explicitly conflicting outcome. " if row in evidence_rows else "No reliable identity or pre-OSS employer was established after the staged search and namesake-rejection protocol. ") + note + " Search-result snippets were discovery aids only, no paywall or access control was bypassed, targeted CIA Reading Room and Library of Congress exact-name passes were included, and no exposed NARA API credential was used.", "next_action": f"Review the indexed Box {archive_box(row)} personnel file; compare paired files where a duplicate or identifier conflict is recorded.", "attempt_number": 1, "research_agent_version": "before-oss-b903-v1"})
    return attempts


def main() -> None:
    affiliations = [army_affiliation(item) for item in ARMY_OCCUPATIONS] + substantive_affiliations()
    claims = [army_identity_claim(item) for item in ARMY_OCCUPATIONS]
    claims += [army_occupation_claim(item) for item in ARMY_OCCUPATIONS]
    claims += substantive_claims()
    bundle = {"bundle_version": "batch-903-v1", "reviewer": "Before OSS Batch 903 evidence review", "sources": sources(), "organizations": organizations(), "affiliations": affiliations, "claims": claims, "person_updates": person_updates(), "research_attempts": research_attempts()}
    OUTPUT.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
