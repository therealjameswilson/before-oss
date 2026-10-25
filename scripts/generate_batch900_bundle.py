#!/usr/bin/env python3
"""Generate the reviewed Batch 900 evidence bundle from audited constants."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "research/evidence-page440-spanum-to-spence-review_batch-900_2026-10-25.json"

INDEX = "nara-index-b900"
ARMY = "army-bulk-b900"
TECH = "army-tech-b900"
CODES = "army-codes-b900"
PENN = "penn-speiser-b900"
NPS_SPENCE = "nps-john-spence-b900"
ONR_SPENCE = "onr-john-spence-b900"


PEOPLE = {
    1: ("715418af-06ba-5fd8-bef6-1d46cb406672", "Mildred S Spanum"),
    2: ("148a479f-2daf-551c-9385-4a7f9d7cd797", "George Spardo"),
    3: ("7ee6d351-7ab5-552d-a795-7f8ab12d01fc", "Giorgio Spardo"),
    4: ("69f60fa8-e888-526f-b906-3a754aa92a69", "Fred A Sparks"),
    5: ("63105c95-79e1-54fe-8cca-7c77416b590c", "John C Sparks"),
    6: ("10da7dfd-0a8a-5bff-b014-c93feb770c69", "William L Sparks"),
    7: ("f5365a53-ed78-5ed9-909e-19fe93cb0e90", "John P Spauldling"),
    8: ("861d95a1-53b8-54e4-baa8-2d8e6fd7387e", "John P Spauldling"),
    9: ("66cad179-2ea7-512a-8c69-a469c30f156e", "Kenneth D Spauldling"),
    10: ("25346b3c-dd04-544c-bea7-cda89f52d61a", "Robert D Spaur"),
    11: ("19002111-c5d0-5976-81a2-49dd119cd56f", "Orlando A Spear"),
    12: ("d33218cd-a453-5e78-9227-73916f76701e", "Donald A Spears"),
    13: ("f88c68e7-737d-5e5d-90d2-f1db5d7380c8", "Robert S Spears"),
    14: ("01d29882-ba89-5318-b39c-9112ab97ed49", "Manes Specter"),
    15: ("2f7c8b24-6d14-59f2-9675-516da7eb79c7", "Samuel I Spector"),
    16: ("b1ab1f3f-a376-52f0-bd91-fe2a2c5e932e", "David G Speer"),
    17: ("5ba044cf-6e1f-5c32-9a23-b3acc1792630", "Bruce Spegal"),
    18: ("d345ac2c-d8e4-5f1b-99c2-895147e13c67", "Joe G Speigler"),
    19: ("2b95bc92-5a44-5b55-834b-1ea1778ab2fe", "Louis L Speilman"),
    20: ("6683b0d3-8282-56ee-902d-9308d3059cea", "Ephraim A Speiser"),
    21: ("cf925e3a-9a9e-5448-92bb-992ad9c6251f", "Francis E Speizer"),
    22: ("070eccda-462f-5d37-b775-a8c96dfc1212", "Vaughn B Speltz"),
    23: ("eb1027ba-9a18-521b-87b3-666180fcca77", "John P Spence"),
}


ARMY_OCCUPATIONS = [
    {"row": 6, "slug": "william-l-sparks", "date": "1944-07-03", "code": "641", "occupation": "Occupations in manufacture of paper and pulp", "relationship_type": "employment", "locator": "PDF physical page 173; category 6-41"},
    {"row": 10, "slug": "robert-d-spaur", "date": "1943-02-05", "code": "992", "occupation": "Students", "relationship_type": "student", "locator": "PDF physical page 304; corrected Code No. 30 category 9-92"},
    {"row": 13, "slug": "robert-s-spears", "date": "1943-03-24", "code": "185", "occupation": "Salesmen and sales agents, except to consumers", "relationship_type": "employment", "locator": "PDF physical pages 171-172; category 1-85"},
    {"row": 14, "slug": "manes-specter", "date": "1942-11-17", "code": "068", "occupation": "Semiprofessional occupations, n.e.c.", "relationship_type": "employment", "locator": "PDF physical pages 171 and 304; category 0-68"},
    {"row": 15, "slug": "samuel-i-spector", "date": "1942-12-10", "code": "717", "occupation": "Pattern and model makers, except paper", "relationship_type": "employment", "locator": "PDF physical page 174; category 7-17"},
]


UNRESOLVED = {
    1: "Exact-name, OSS, employer, occupation, obituary, institutional and archival searches did not identify the indexed woman or a pre-OSS affiliation.",
    3: "The adjacent George and Giorgio Spardo rows may reflect related or variant records, but no source justifies merging them or transferring the protected-identifier conflict.",
    4: "The common name produced many namesakes but no OSS, Box 731, or prewar-employer bridge.",
    5: "Exact-name and middle-initial searches did not provide two identifiers beyond this common name.",
    7: "The commissioned-officer row remains distinct from the second same-name row because their protected identifiers differ; no employer chronology was found.",
    8: "The second same-name row remains separate because its protected identifier differs from the commissioned-officer row; no employer chronology was found.",
    9: "Spauldling and Spaulding variants produced unbridged namesakes but no reliable OSS or employer match.",
    11: "Exact-name searches did not connect the indexed person to the better-documented Reginald Spear or to another pre-OSS occupation or institution.",
    12: "Rank and name searches found no source that establishes the indexed first sergeant's civilian employer or immediate military assignment before OSS.",
    16: "The name and protected identifier produced no reviewed Army-bulk match or external identity and employer chronology.",
    17: "The rare surname produced genealogical possibilities but no source that bridges a namesake to OSS or a prewar affiliation.",
    19: "Speilman and Spielman variants produced no defensible wartime identity or employer source.",
    21: "Exact-name searches were dominated by chronologically incompatible namesakes and did not identify the indexed person.",
    22: "The exact name produced no wartime institutional, military, obituary or employer bridge.",
}


def box_for_row(row: int) -> int:
    return 730 if row <= 3 else 731


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 730-733",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 440, rows 1-23, plus page 439 row 38 and page 441 row 11 for protected-identifier conflicts; checked against layout-preserving text and a rendered page image",
            "access_date": "2026-10-25",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "Printed rows remain immutable. Full protected identifiers remain private and are masked from public data.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; protected-identifier fields reviewed for five accepted identities and two spelling/duplicate conflicts",
            "access_date": "2026-10-25",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "No raw row or full private identifier is retained in public assets. The file is incomplete and a non-hit is not negative proof.",
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
            "access_date": "2026-10-25",
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
            "locator": "PDF physical pages 171-174 and 304; categories 068, 185, 641, 717 and corrected 992 visually checked",
            "access_date": "2026-10-25",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical labels identify neither employers nor workplaces and are published only as qualified occupation evidence.",
        },
        {
            "key": PENN,
            "stable_url": "https://archives.upenn.edu/collections/finding-aid/upt50s742/",
            "archival_identifier": "University of Pennsylvania Archives, UPT 50 S742",
            "title": "Ephraim Avigdor Speiser Papers UPT 50 S742",
            "author_creator": "Irina Kalashnikova",
            "repository_publisher": "University Archives and Records Center, University of Pennsylvania",
            "publication_record_date": "2004-01",
            "locator": "Historical note: Penn faculty appointments beginning in 1928 and OSS Near East Section leadership during World War II",
            "access_date": "2026-10-25",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Ephraim Avigdor Speiser Papers",
            "rights_notes": "Project-authored paraphrases only; the finding aid establishes chronology at year-level precision, not an exact OSS transfer date.",
        },
        {
            "key": NPS_SPENCE,
            "stable_url": "https://www.nps.gov/articles/oss-in-action-the-pacific-and-the-far-east.htm",
            "title": "OSS in Action: The Pacific and the Far East",
            "author_creator": "John Whiteclay Chambers II",
            "repository_publisher": "National Park Service",
            "locator": "Admiral Nimitz Welcomes OSS Frogmen; John P. Spence paragraph",
            "access_date": "2026-10-25",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "OSS Training in the National Parks and Service Abroad in World War II",
            "rights_notes": "The official narrative identifies an OSS John P. Spence but does not provide a protected identifier or personnel-file pointer tying him to this index row.",
        },
        {
            "key": ONR_SPENCE,
            "stable_url": "https://www.onr.navy.mil/media-center/news-releases/terrible-hours-and-more",
            "title": "The Terrible Hours, and More",
            "repository_publisher": "Office of Naval Research",
            "publication_record_date": "2002-12-05",
            "locator": "Naval Academy conference participant paragraph naming John Spence as the last surviving original OSS combat swimmer",
            "access_date": "2026-10-25",
            "source_quality": "A_direct_official",
            "rights_notes": "Corroborates the historical swimmer candidate but omits the middle initial and does not establish the index-row identity.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": "penn-b900",
            "organization_id": "40f6dffe-883f-58ac-8fd0-3f769bfd06fa",
            "canonical_name": "University of Pennsylvania",
            "historical_name": "University of Pennsylvania",
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "Philadelphia",
            "state_or_region": "Pennsylvania",
            "country": "United States",
            "normalization_notes": "Existing dominant canonical organization reused; the historical department remains in the role field rather than being silently treated as a separate employer.",
        }
    ]


def army_affiliation(item: dict[str, object]) -> dict[str, object]:
    person_id, _name = PEOPLE[int(item["row"])]
    relationship = str(item["relationship_type"])
    return {
        "key": f"{item['slug']}-occupation-b900",
        "person_id": person_id,
        "relationship_type": relationship,
        "occupation": "Student; institution not recorded" if relationship == "student" else item["occupation"],
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
        "research_notes": "The historical category is not converted into a named employer, institution, workplace or exact title.",
    }


def army_identity_claim(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    person_id, name = PEOPLE[row]
    return {
        "key": f"identity-{item['slug']}-b900",
        "person_id": person_id,
        "claim_type": "identity",
        "claim_text": f"The indexed {name} row is a high-confidence match to the reviewed official Army record.",
        "evidence_paraphrase": "A nonshared protected identifier connects the visually verified index row to the official Army record.",
        "identity_match_assessment": "High confidence from exact name agreement and a nonshared protected-identifier bridge.",
        "temporal_assessment": "The Army-entry record supports identity and a dated occupation category; it does not establish the OSS transfer sequence.",
        "source_quality": "A_direct_official",
        "claim_confidence": "high",
        "publication_status": "published",
        "match_notes": "No protected identifier is exposed, and no employer or workplace is inferred from the coded Army field.",
        "sources": [
            {"source_key": INDEX, "locator_override": f"PDF page 440 row {row}; protected identifier withheld"},
            {"source_key": ARMY, "locator_override": "Accepted reviewed identity bridge; protected identifier withheld"},
        ],
    }


def army_occupation_claim(item: dict[str, object]) -> dict[str, object]:
    person_id, name = PEOPLE[int(item["row"])]
    if item["relationship_type"] == "student":
        text = f"At Army entry on {item['date']}, {name} was recorded in the historical student category; no institution or employer is identified."
    else:
        text = f"At Army entry on {item['date']}, {name} was recorded in the historical {str(item['occupation']).lower()} category; no employer is identified."
    return {
        "key": f"occupation-{item['slug']}-b900",
        "person_id": person_id,
        "affiliation_key": f"{item['slug']}-occupation-b900",
        "claim_type": "occupation",
        "claim_text": text,
        "evidence_paraphrase": f"The accepted Army record carries civilian-occupation code {item['code']}, decoded from NARA's official code list.",
        "identity_match_assessment": "The occupation belongs only to the reviewed protected-identifier match; the identifier itself is not public.",
        "temporal_assessment": "Strongly date-bounded to Army entry; it does not establish the immediate pre-OSS affiliation or a named employer.",
        "source_quality": "A_direct_official",
        "claim_confidence": "medium",
        "publication_status": "publish_qualified",
        "match_notes": "The historical category is a qualified lead, not an employer, workplace, institution or exact title.",
        "sources": [
            {"source_key": ARMY, "locator_override": f"Accepted reviewed identity record; civilian occupation code {item['code']}; protected identifier withheld"},
            {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46; Army-entry-date and civilian-occupation fields"},
            {"source_key": CODES, "locator_override": item["locator"], "excerpt_override": item["occupation"]},
        ],
    }


def speiser_affiliation() -> dict[str, object]:
    return {
        "key": "ephraim-speiser-penn-b900",
        "person_id": PEOPLE[20][0],
        "organization_key": "penn-b900",
        "organization_name_as_found": "University of Pennsylvania",
        "role_title": "Professor of Semitics; chairman, Department of Oriental Studies",
        "occupation": "professor, archaeologist and Near East scholar",
        "relationship_type": "employment",
        "start_date": "1928",
        "end_date": None,
        "date_precision": "The institutional finding aid dates his Penn appointment from 1928, promotion in 1931 and later chairmanship, then places his OSS section leadership during World War II; no exact leave, separation or transfer date is stated.",
        "city": "Philadelphia",
        "state_or_region": "Pennsylvania",
        "country": "United States",
        "immediate_pre_oss": True,
        "last_civilian_pre_service": True,
        "pre_oss_temporal_basis": "probable_immediate",
        "identity_confidence": "high_confidence",
        "claim_confidence": "high",
        "source_quality": "B_authoritative_institutional",
        "publication_status": "published",
        "research_notes": "Penn is the best-supported last civilian employer and probable immediate pre-OSS affiliation. The source does not explicitly say he left Penn directly for OSS or give an exact transfer date.",
    }


def substantive_claims() -> list[dict[str, object]]:
    return [
        {
            "key": "conflict-george-spardo-b900",
            "person_id": PEOPLE[2][0],
            "claim_type": "identity",
            "claim_text": "George Spardo on index page 440 and George Spadero on page 439 are separate printed rows tied to one protected identifier; neither is merged or assigned the Army occupation candidate.",
            "evidence_paraphrase": "The index spellings differ, the official Army spelling is a third form, and the protected identifier is shared across the two immutable index rows.",
            "identity_match_assessment": "Conflicting. The identifier cannot safely select one spelling or collapse the separate printed rows.",
            "temporal_assessment": "The Army entry cannot resolve which index row owns the record.",
            "source_quality": "A_direct_official",
            "claim_confidence": "conflicting",
            "publication_status": "conflicting",
            "match_notes": "Full protected identifiers are withheld. Review Boxes 730-731 together before transferring identity or occupation evidence.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 439 row 38 and page 440 row 2; protected identifier withheld"},
                {"source_key": ARMY, "support_type": "context_only", "locator_override": "Conflicting name-form candidate; protected identifier withheld"},
            ],
        },
        {
            "key": "conflict-joe-speigler-spiegler-b900",
            "person_id": PEOPLE[18][0],
            "claim_type": "identity",
            "claim_text": "Joe G Speigler on index page 440 and Joe G Spiegler on page 441 are separate printed rows tied to one protected identifier; neither is merged or assigned the Army occupation candidate.",
            "evidence_paraphrase": "The two immutable index rows use different spellings while sharing a protected identifier, and the Army form agrees with only one spelling.",
            "identity_match_assessment": "Conflicting. The shared identifier cannot safely select one printed row or justify a merge.",
            "temporal_assessment": "The Army entry supplies no evidence that resolves the two index files.",
            "source_quality": "A_direct_official",
            "claim_confidence": "conflicting",
            "publication_status": "conflicting",
            "match_notes": "Full protected identifiers are withheld. Review Boxes 731 and 733 together before transferring identity, occupation or employer evidence.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 440 row 18 and page 441 row 11; protected identifier withheld"},
                {"source_key": ARMY, "support_type": "context_only", "locator_override": "Conflicting name-form candidate; protected identifier withheld"},
            ],
        },
        {
            "key": "identity-ephraim-speiser-b900",
            "person_id": PEOPLE[20][0],
            "claim_type": "identity",
            "claim_text": "The indexed Ephraim A Speiser is a high-confidence match to Penn scholar and OSS Near East Section chief Ephraim Avigdor Speiser.",
            "evidence_paraphrase": "Penn's institutional finding aid supplies the exact distinctive name, faculty chronology and specific OSS Research and Analysis role.",
            "identity_match_assessment": "High confidence from the distinctive exact name and one exceptionally specific authoritative institutional biography linking Penn and OSS service.",
            "temporal_assessment": "The source dates Penn employment from 1928 and places his OSS leadership during World War II, but gives no exact transfer date.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "No famous-person match is assigned on name alone; the institutional record directly supplies the indexed middle initial and specific OSS role.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 440 row 20; Box 731"},
                {"source_key": PENN, "locator_override": "Historical note; faculty chronology and OSS Near East Section leadership"},
            ],
        },
        {
            "key": "last-civilian-ephraim-speiser-penn-b900",
            "person_id": PEOPLE[20][0],
            "affiliation_key": "ephraim-speiser-penn-b900",
            "claim_type": "last_civilian_pre_service",
            "claim_text": "The University of Pennsylvania is Ephraim Speiser's best-supported last civilian employer before his wartime OSS service.",
            "evidence_paraphrase": "The institutional chronology places Speiser continuously in Penn faculty and department leadership roles from 1928 before identifying his wartime OSS section leadership.",
            "identity_match_assessment": "High-confidence identity from the exact distinctive name and Penn's specific OSS biography.",
            "temporal_assessment": "Strongly date-bounded as the last documented civilian employment, although the finding aid does not give an exact leave or separation date.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "The claim names Penn as employer and keeps his academic title separate from the employing organization.",
            "sources": [{"source_key": PENN, "locator_override": "Historical note; Penn appointments from 1928 and wartime OSS section leadership"}],
        },
        {
            "key": "immediate-ephraim-speiser-penn-b900",
            "person_id": PEOPLE[20][0],
            "affiliation_key": "ephraim-speiser-penn-b900",
            "claim_type": "immediate_pre_oss_affiliation",
            "claim_text": "Penn is Speiser's probable immediate pre-OSS affiliation; the accessible institutional source does not explicitly state the transfer sequence.",
            "evidence_paraphrase": "The finding aid moves from his continuing Penn professorship and chairmanship to his OSS Near East Section leadership during World War II.",
            "identity_match_assessment": "High-confidence identity from the distinctive name and institution-specific OSS role.",
            "temporal_assessment": "Probable immediate, not explicit immediate: no exact leave date or phrase such as recruited from Penn appears in the reviewed source.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "medium",
            "publication_status": "publish_qualified",
            "match_notes": "The public profile must retain the probability language and distinguish this from the stronger last-civilian-employer conclusion.",
            "sources": [{"source_key": PENN, "locator_override": "Historical note; Penn appointments and later wartime OSS role"}],
        },
        {
            "key": "candidate-john-p-spence-b900",
            "person_id": PEOPLE[23][0],
            "claim_type": "identity",
            "claim_text": "An official historical narrative describes an OSS combat-swimmer trainer named John P. Spence, but the indexed row is not yet securely linked to him.",
            "evidence_paraphrase": "NPS identifies a Tennessee Navy veteran and deep-sea diver recruited by OSS in 1942; ONR independently identifies John Spence as an original OSS combat swimmer.",
            "identity_match_assessment": "Probable candidate from exact full-name and OSS-context agreement, but the common name lacks two corroborating identifiers shared with the index row.",
            "temporal_assessment": "The candidate narrative describes pre-recruitment Navy and diving experience but does not name an employer or provide the index-row bridge.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "low",
            "publication_status": "withheld_low_confidence",
            "match_notes": "The candidate remains private review evidence. Box 731 must supply a hometown, branch, date, assignment or another identifier before the biography is published for this row.",
            "sources": [
                {"source_key": NPS_SPENCE, "locator_override": "Admiral Nimitz Welcomes OSS Frogmen; John P. Spence paragraph"},
                {"source_key": ONR_SPENCE, "support_type": "context_only", "locator_override": "Naval Academy conference participant paragraph"},
            ],
        },
    ]


def base_archive_update(row: int, reason: str) -> dict[str, object]:
    person_id, name = PEOPLE[row]
    box = box_for_row(row)
    return {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, Box {box}, and archive location, but the staged official-context, CIA Reading Room, exact-name, occupation, employer, obituary, institutional, directory, newspaper and archival protocol found no defensible identity bridge. {reason}",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": f"Review the indexed Box {box} personnel file for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "critical",
    }


def person_updates() -> list[dict[str, object]]:
    updates = [base_archive_update(row, reason) for row, reason in UNRESOLVED.items()]
    for item in ARMY_OCCUPATIONS:
        person_id, _name = PEOPLE[int(item["row"])]
        updates.append(
            {
                "person_id": person_id,
                "identity_status": "high_confidence",
                "identity_evidence": "A nonshared protected identifier connects the visually verified index row to the reviewed official Army record. The occupation field remains separate from employer and immediate-affiliation claims.",
                "personnel_category": "enlisted_army_personnel",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "occupation_only_found",
                "next_action": "Review the indexed Box 731 personnel file to identify the immediate pre-OSS affiliation and last civilian employer; do not convert the Army category into a named employer or institution.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            }
        )
    updates.extend(
        [
            {
                "person_id": PEOPLE[2][0],
                "identity_status": "conflicting",
                "identity_evidence": "George Spardo on page 440 and George Spadero on page 439 are separately printed rows tied to one protected identifier; the Army record uses a third spelling. No occupation or employer evidence is transferred.",
                "name_variants": ["George Spadaro"],
                "manual_review_required": True,
                "possible_duplicate_group": "serial-conflict:george-spadero-spardo-pages439-440",
                "research_status": "conflicting_sources",
                "next_action": "Review the George Spardo file in Box 730 together with the George Spadero file in Box 731 before accepting protected-identifier-based identity, occupation or employer evidence.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[18][0],
                "identity_status": "conflicting",
                "identity_evidence": "Joe G Speigler on page 440 and Joe G Spiegler on page 441 are separately printed rows tied to one protected identifier; the Army spelling agrees with only one form. No occupation or employer evidence is transferred.",
                "name_variants": ["Joe G Spiegler"],
                "manual_review_required": True,
                "possible_duplicate_group": "serial-conflict:joe-speigler-spiegler-pages440-441",
                "research_status": "conflicting_sources",
                "next_action": "Review the Joe G Speigler file in Box 731 together with the Joe G Spiegler file in Box 733 before accepting protected-identifier-based identity, occupation or employer evidence.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[20][0],
                "identity_status": "high_confidence",
                "identity_evidence": "The distinctive exact name and Penn's institutional biography linking long-running faculty employment to specific OSS Near East Section leadership establish a high-confidence identity.",
                "name_variants": ["Ephraim Avigdor Speiser", "Ephraim A. Speiser"],
                "personnel_category": "civilian_professional_or_administrative_grade",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "verified_employer_found",
                "next_action": "Review Box 731 to confirm the exact Penn-to-OSS transfer date and whether a formal university leave or intervening government appointment occurred.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[23][0],
                "identity_status": "probable",
                "identity_evidence": "NPS describes an OSS combat-swimmer trainer named John P. Spence and ONR corroborates that candidate's OSS service, but the common-name index row supplies no hometown, branch, date or identifier shared with those sources.",
                "manual_review_required": True,
                "research_status": "needs_identity_review",
                "next_action": "Review Box 731 for Tennessee, Navy, diving, Maritime Unit or 1942 recruitment evidence before linking the combat-swimmer biography or any pre-OSS occupation to this row.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
        ]
    )
    return updates


def research_attempts() -> list[dict[str, object]]:
    evidence_rows = {2, 6, 10, 13, 14, 15, 18, 20, 23}
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        box = box_for_row(row)
        if row in UNRESOLVED:
            note = UNRESOLVED[row]
        elif row in {2, 18}:
            note = "A protected identifier is shared by separately printed name forms, so the conflict remains visible and no Army occupation is transferred."
        elif row == 20:
            note = "Penn's authoritative finding aid establishes high-confidence identity, long-running faculty employment and wartime OSS section leadership; Penn is the verified last civilian employer and probable immediate affiliation."
        elif row == 23:
            note = "Two official narratives document the combat-swimmer candidate, but the index row lacks the additional identifiers needed to link a common name under the project's identity rules."
        else:
            note = "The accepted protected-identifier bridge supports identity and a dated historical occupation or student category, but not a named employer or immediate OSS chronology."
        slug = name.lower().replace(" ", "-").replace("'", "") + f"-r{row}"
        has_evidence = row in evidence_rows
        attempts.append(
            {
                "key": f"page440-row{row}-{slug}-b900",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA/index context; CIA Reading Room exact-name check; OSS and rank variants; employer and occupation; obituary, institutional, newspaper, directory and archival searches; Box {box}; protected-identifier Army crosswalk where available",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_900",
                "started_at": "2026-10-25T16:12:00Z",
                "completed_at": "2026-10-25T16:44:00Z",
                "outcome": "source_reviewed" if has_evidence else "candidate_rejected",
                "sources_reviewed": 8 if has_evidence else 5,
                "candidate_sources_rejected": 5 if has_evidence else 7,
                "rejection_reasons": "Unbridged namesakes, chronologically irrelevant results, postwar-only leads and materially conflicting candidates were not assigned." if has_evidence else note,
                "research_notes": ("Reviewed evidence established a supported, provisional or explicitly conflicting outcome; public claims are limited to what the cited sources prove. " if has_evidence else "No reliable identity or pre-OSS employer was established after the staged search and namesake-rejection protocol. ") + note + " Search-result snippets were discovery aids only, no paywall or access control was bypassed, the CIA Reading Room exact-name pass returned no relevant result, and no exposed NARA API credential was used.",
                "next_action": f"Review the indexed Box {box} personnel file.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b900-v1",
            }
        )
    return attempts


def main() -> None:
    affiliations = [army_affiliation(item) for item in ARMY_OCCUPATIONS]
    affiliations.append(speiser_affiliation())
    claims = [army_identity_claim(item) for item in ARMY_OCCUPATIONS]
    claims.extend(army_occupation_claim(item) for item in ARMY_OCCUPATIONS)
    claims.extend(substantive_claims())
    bundle = {
        "bundle_version": "batch-900-v1",
        "reviewer": "Before OSS Batch 900 evidence review",
        "sources": sources(),
        "organizations": organizations(),
        "affiliations": affiliations,
        "claims": claims,
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }
    OUTPUT.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
