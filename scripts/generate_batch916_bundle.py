#!/usr/bin/env python3
"""Generate the reviewed Batch 916 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import uuid
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "research/evidence-page448-stevens-to-stewart-review_batch-916_2026-10-25.json"

INDEX = "nara-index-b916"
ARMY = "army-bulk-b916"
TECH = "army-tech-b916"
CODES = "army-codes-b916"
EOA_ARTHUR = "encyclopedia-alabama-arthur-stewart-b916"
DIXIE_ARTHUR = "dixie-art-colony-arthur-stewart-b916"
BMA_ARTHUR = "birmingham-museum-arthur-stewart-b916"

PEOPLE = {
    24: ("59aef3b2-c750-53ca-ae7b-b655520fac6b", "Rebecca B Stevens"),
    25: ("8a9a7f4d-a482-5901-a9c5-2d3102153e8f", "Rowland P Stevens"),
    26: ("b968b43f-3213-5f0c-a176-335cdef07db8", "Alexander Stevenson"),
    27: ("a9149157-d807-516b-b2fe-49bf722495eb", "Beatrice Ellen Stevenson"),
    28: ("f85654fd-b770-5089-88f2-aa6e0d5d4b21", "Caroline S Stevenson"),
    29: ("0a9b0230-fe9b-5242-91e3-2799e1d8b28d", "Chester Stevenson"),
    30: ("b5f8a1e5-9fc9-55bb-923a-dd2248c55366", "Dorothy S Stevenson"),
    31: ("ce0c6016-a47a-5cb8-8495-01fc0967c3e4", "Harold R Stevenson"),
    32: ("0c1c613e-024d-5afc-9a43-1ef18d06932a", "Thomas T Stevenson"),
    33: ("e5fcfea6-b88a-5014-9c82-e3ac48159c39", "Viola M Stevenson"),
    34: ("4e7c1024-67a2-5bd5-af44-8b7fc75cad42", "Wayne J Stevenson"),
    35: ("5ed0be1f-d66f-50be-b9e0-b16e22090251", "Richard C Steward"),
    36: ("edef257d-0310-5658-9b94-ec2807a16757", "Arthur W Stewart"),
    37: ("d4159c13-03e6-5bdf-b2ca-822b44c3cf1b", "Charles L Stewart"),
    38: ("29512173-cebb-5f66-9f7c-c5f5faddff1c", "Dean W Stewart"),
    39: ("f6fa86e3-545f-5628-9e71-4ab7a97085d0", "Donald C Stewart"),
    40: ("d2588419-39c6-56c9-bdec-34411ed7e547", "Francis J Stewart"),
    41: ("c9cb6a53-a776-5546-a5bd-7e0d9050485d", "George W Stewart"),
    42: ("a07b46f7-fd11-5e8b-99d3-459107ce1ad5", "Gordon Stewart"),
    43: ("0923d0e0-c668-5900-89e7-8b6ec446a291", "Grace A Stewart"),
    44: ("db9f016d-859a-59a8-8215-fb8378f17a24", "Gretchen E Stewart"),
    45: ("9138358d-a977-5800-befd-70a991f2f5f7", "Harrison M Stewart"),
    46: ("9a695ad7-53e7-5bab-8db7-690290c2cab1", "Harvey S Stewart"),
}

ARMY_OCCUPATIONS = [
    {"row": 26, "date": "1945-03-03", "code": "039", "occupation": "Professional occupations, not elsewhere classified", "locator": "PDF physical page 171; category 0-39"},
    {"row": 34, "date": "1940-09-16", "code": "105", "occupation": "Clerks, general office", "locator": "PDF physical page 171; category 1-05"},
    {"row": 35, "date": "1943-02-09", "code": "043", "occupation": "Decorators and window dressers", "locator": "PDF physical page 171; category 0-43"},
    {"row": 36, "date": "1941-07-17", "code": "004", "occupation": "Artists, sculptors, and teachers of art", "locator": "PDF physical page 170; category 0-04"},
    {"row": 37, "date": "1943-05-29", "code": "097", "occupation": "Managers and officials, not elsewhere classified", "locator": "PDF physical page 171; category 0-97"},
    {"row": 38, "date": "1942-03-04", "code": "128", "occupation": "Mail carriers", "locator": "PDF physical page 171; category 1-28"},
    {"row": 39, "date": "1942-07-17", "code": "071", "occupation": "Hotel and restaurant managers", "locator": "PDF physical page 171; category 0-71"},
    {"row": 40, "date": "1944-07-10", "code": "261", "occupation": "Guards and watchmen, except crossing watchmen", "locator": "PDF physical page 172; category 2-61"},
    {"row": 41, "date": "1942-04-28", "code": "306", "occupation": "General farmers", "locator": "PDF physical page 172; category 3-06"},
    {"row": 45, "date": "1943-06-21", "code": "992", "occupation": "Students", "locator": "PDF physical page 304; amended category 9-92"},
    {"row": 46, "date": "1942-08-24", "code": "266", "occupation": "Policemen and detectives, public service", "locator": "PDF physical page 172; category 2-66"},
]

UNRESOLVED = {
    24: "Exact-name, middle-initial, obituary, institutional, newspaper, directory and archival searches produced no defensible identity bridge.",
    25: "The protected index identifier produced no compatible official Army candidate, and exact-name variants produced no reliable identity or chronology.",
    27: "The full indexed given name was preserved, but exact-name and institutional searches found no person-specific OSS or employment bridge.",
    28: "Common-name and initial searches returned incompatible directory and family-history results without an OSS assignment or two corroborating identifiers.",
    29: "Exact-name, occupation, obituary and archival searches found no reliable pre-OSS identity or employer evidence.",
    30: "Common-name results did not supply the protected identifier, OSS assignment or corroborating chronology required for assignment.",
    31: "A later Cleveland insurance-directory namesake lacks an OSS, protected-identifier or wartime chronology bridge and was not assigned.",
    32: "Exact-name and middle-initial searches produced no source with a defensible OSS identity bridge or pre-OSS chronology.",
    33: "Exact-name, occupation, newspaper, obituary and archival searches produced no reliable person-specific match.",
    42: "A biography of OSS officer Gordon Matthews Stewart is a plausible namesake only; the no-middle-name index row has no protected identifier or Box 746 bridge to that biography.",
    43: "Exact-name, occupation, obituary, institutional and archival searches produced no defensible identity or employment match.",
    44: "Exact-name and variant searches produced no source with two corroborating identifiers beyond the name.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def stable_id(kind: str, value: str) -> str:
    return str(uuid.uuid5(uuid.NAMESPACE_URL, f"before-oss:{kind}:{value}"))


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Box 746",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 448, rows 24-46; checked against layout-preserving text and a rendered page image",
            "access_date": "2026-10-25",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All printed rows remain separate. Full protected identifiers remain private.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; eleven accepted reviewed Batch 916 identity bridges",
            "access_date": "2026-10-25",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "No raw row or full protected identifier is retained in public assets. Coded occupations identify no employer.",
        },
        {
            "key": TECH,
            "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf",
            "archival_identifier": "NN3-064-03-008; National Archives Identifier 1263923",
            "title": "World War II Army Enlistment Records: Reference Copy of Technical Documentation",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives at College Park - Electronic Records",
            "publication_record_date": "1994-2005; reference copy modified 2011",
            "locator": "PDF physical pages 44-46; identifier, name, entry-date, grade and civilian-occupation fields",
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
            "locator": "PDF physical pages 170-172 and 304; all eleven Batch 916 categories visually checked",
            "access_date": "2026-10-25",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical labels identify neither employers nor workplaces. The amended table maps code 992 to Students.",
        },
        {
            "key": EOA_ARTHUR,
            "stable_url": "https://encyclopediaofalabama.org/article/dixie-art-colony/",
            "title": "Dixie Art Colony",
            "author_creator": "Lynn Barstis Williams Katz, Auburn University Libraries",
            "repository_publisher": "Encyclopedia of Alabama",
            "publication_record_date": "2025-04-18; updated 2025-12-05",
            "locator": "Paragraphs describing Arthur Stewart's 1936 arrival, Perry County background and art study at Judson College",
            "access_date": "2026-10-25",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Encyclopedia of Alabama",
            "rights_notes": "Institutional history used for a concise prewar affiliation; no employer relationship is inferred.",
        },
        {
            "key": DIXIE_ARTHUR,
            "stable_url": "https://dixieartcolony.org/gallery-category/arthur-stewart/",
            "title": "Arthur Stewart Archives",
            "author_creator": "Dixie Art Colony Foundation",
            "repository_publisher": "Dixie Art Colony Foundation",
            "publication_record_date": "Collection pages dated 2016-2023",
            "locator": "Arthur Stewart artist category and artwork records identifying Arthur Walter Stewart",
            "access_date": "2026-10-25",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Dixie Art Colony Foundation archives",
            "rights_notes": "Direct organizational archive used to corroborate the full name and artistic affiliation.",
        },
        {
            "key": BMA_ARTHUR,
            "stable_url": "https://www.artsbma.org/collection/miss-hannah-elliott/",
            "title": "Miss Hannah Elliott",
            "author_creator": "Birmingham Museum of Art",
            "repository_publisher": "Birmingham Museum of Art",
            "publication_record_date": "Artwork dated 1940",
            "locator": "Collection record for Arthur Stewart's 1940 portrait, accession 1981.51",
            "access_date": "2026-10-25",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Birmingham Museum of Art collection",
            "rights_notes": "Museum metadata corroborates the artist's 1915-2001 life dates and documented prewar activity.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": "dixie-art-colony-b916",
            "organization_id": stable_id("organization", "Dixie Art Colony historical Alabama"),
            "canonical_name": "Dixie Art Colony",
            "historical_name": "Dixie Art Colony",
            "aliases": [],
            "organization_type": "informal art colony and summer art school",
            "sector": "arts_and_culture",
            "state_or_region": "Alabama",
            "country": "United States",
            "active_dates": "1933-1945; 1947-1948",
            "normalization_notes": "The historical colony is distinct from the Dixie Art Colony Foundation, founded in 2015. Participant status is not employment.",
        }
    ]


def army_affiliation(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    person_id, name = PEOPLE[row]
    is_student = item["code"] == "992"
    return {
        "key": f"{slug(name)}-occupation-b916",
        "person_id": person_id,
        "relationship_type": "student" if is_student else "employment",
        "occupation": item["occupation"],
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
        "research_notes": "The historical category is not converted into a named employer, workplace or exact title.",
    }


def affiliations() -> list[dict[str, object]]:
    values = [army_affiliation(item) for item in ARMY_OCCUPATIONS]
    values.append(
        {
            "key": "arthur-w-stewart-dixie-art-colony-b916",
            "person_id": PEOPLE[36][0],
            "organization_key": "dixie-art-colony-b916",
            "organization_name_as_found": "Dixie Art Colony",
            "role_title": "artist participant",
            "occupation": "artist",
            "relationship_type": "professional_affiliation",
            "start_date": "1936",
            "date_precision": "The institutional history states that Arthur Stewart joined in 1936; no end date or employment relationship is supplied.",
            "state_or_region": "Alabama",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "published",
            "research_notes": "Dixie Art Colony was an art camp and summer art school. Arthur Stewart is modeled as a participant, not an employee, and the affiliation is not labeled immediately pre-OSS.",
        }
    )
    return values


def army_claims(item: dict[str, object]) -> list[dict[str, object]]:
    row = int(item["row"])
    person_id, name = PEOPLE[row]
    return [
        {
            "key": f"identity-{slug(name)}-b916",
            "person_id": person_id,
            "claim_type": "identity",
            "claim_text": f"The indexed {name} row is a high-confidence match to the reviewed official Army record.",
            "evidence_paraphrase": "A nonshared protected identifier and compatible name connect the visually verified index row to the official Army record.",
            "identity_match_assessment": "High confidence from the nonshared protected-identifier bridge and compatible name.",
            "temporal_assessment": "The Army record supports identity and a dated occupation category; it does not establish the OSS transfer sequence.",
            "source_quality": "A_direct_official",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "No protected identifier is exposed, and the coded occupation is kept separate from employer claims.",
            "sources": [
                {"source_key": INDEX, "locator_override": f"PDF page 448 row {row}; protected identifier withheld"},
                {"source_key": ARMY, "locator_override": "Accepted reviewed identity bridge; protected identifier withheld"},
            ],
        },
        {
            "key": f"occupation-{slug(name)}-b916",
            "person_id": person_id,
            "affiliation_key": f"{slug(name)}-occupation-b916",
            "claim_type": "occupation",
            "claim_text": f"At Army entry on {item['date']}, the official record assigned {name} the historical civilian-occupation category '{item['occupation']}'; no employer is identified.",
            "evidence_paraphrase": f"The Army entry field carries code {item['code']}, which the visually checked NARA code list maps to the stated category.",
            "identity_match_assessment": "High confidence from a nonshared protected-identifier bridge between the index and official Army record.",
            "temporal_assessment": "Strongly date-bounded at Army entry, but neither immediate pre-OSS status nor a named employer is established.",
            "source_quality": "A_direct_official",
            "claim_confidence": "medium",
            "publication_status": "publish_qualified",
            "match_notes": "Historical code-language is retained and excluded from default confirmed/high-confidence employer analytics.",
            "sources": [
                {"source_key": ARMY, "locator_override": f"Army-entry date {item['date']}; occupation code {item['code']}; protected identifier withheld"},
                {"source_key": TECH, "support_type": "context_only", "locator_override": "Civilian-occupation field definition"},
                {"source_key": CODES, "locator_override": item["locator"], "excerpt_override": item["occupation"]},
            ],
        },
    ]


def arthur_claims() -> list[dict[str, object]]:
    person_id = PEOPLE[36][0]
    identity_assessment = "High confidence from the nonshared protected identifier, Army name with junior suffix, Alabama birth and residence, 1915 birth year, artist occupation, and mutually compatible institutional art records."
    return [
        {
            "key": "identity-arthur-walter-stewart-b916",
            "person_id": person_id,
            "claim_type": "identity",
            "claim_text": "The indexed Arthur W. Stewart is a high-confidence match to Alabama artist Arthur Walter Stewart (1915-2001).",
            "evidence_paraphrase": "The Army bridge supplies the suffix, Alabama context, 1915 birth year and artist code; art institutions independently document the matching artist and prewar work.",
            "identity_match_assessment": identity_assessment,
            "temporal_assessment": "The combined records establish a dated prewar artistic identity but do not identify an OSS entry date or immediate predecessor employer.",
            "source_quality": "A_direct_official",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "No single public source exposes the protected identifier. The identity is high-confidence rather than confirmed from a digitized OSS personnel file.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 448 row 36; protected identifier withheld"},
                {"source_key": ARMY, "locator_override": "Accepted Arthur W Stewart Jr identity bridge; protected identifier withheld"},
                {"source_key": EOA_ARTHUR},
                {"source_key": DIXIE_ARTHUR, "excerpt_override": "Arthur Walter Stewart"},
                {"source_key": BMA_ARTHUR, "excerpt_override": "Arthur Stewart, American, 1915 - 2001"},
            ],
        },
        {
            "key": "other-pre-oss-arthur-stewart-dixie-art-colony-b916",
            "person_id": person_id,
            "affiliation_key": "arthur-w-stewart-dixie-art-colony-b916",
            "claim_type": "other_pre_oss_affiliation",
            "claim_text": "Arthur W. Stewart joined the Dixie Art Colony as an artist participant in 1936.",
            "evidence_excerpt": "In 1936, Arthur Stewart joined the colony.",
            "evidence_paraphrase": "The institutional history identifies the Perry County artist, describes his earlier art study and dates his arrival at the colony to 1936.",
            "identity_match_assessment": identity_assessment,
            "temporal_assessment": "Documented prewar professional affiliation. The source does not call the colony his employer or establish that it immediately preceded OSS service.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "Participant status is kept separate from employment, student status, and immediate pre-OSS affiliation.",
            "sources": [
                {"source_key": EOA_ARTHUR, "excerpt_override": "In 1936, Arthur Stewart joined the colony."},
                {"source_key": DIXIE_ARTHUR, "locator_override": "Arthur Stewart artist category and collection records"},
                {"source_key": BMA_ARTHUR, "support_type": "context_only", "locator_override": "Arthur Stewart painting dated 1940"},
            ],
        },
    ]


def accepted_update(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    person_id, name = PEOPLE[row]
    update: dict[str, object] = {
        "person_id": person_id,
        "identity_status": "high_confidence",
        "identity_evidence": "A nonshared protected identifier and compatible name connect the visually verified index row to the reviewed official Army record. The historical occupation field remains separate from employer and immediate-affiliation claims.",
        "personnel_category": "enlisted_army_personnel",
        "commissioned_officer": False,
        "allied_or_foreign_personnel": False,
        "manual_review_required": True,
        "research_status": "occupation_only_found",
        "next_action": "Review the indexed Box 746 personnel file to identify the immediate pre-OSS affiliation and last civilian employer; do not convert the Army occupation category into a named employer.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }
    if row == 36:
        update.update(
            {
                "identity_evidence": "A nonshared protected identifier links the index row to Arthur W Stewart Jr in the official Army file. Alabama birth and residence, a 1915 birth year and the artist occupation align with institutional records for Arthur Walter Stewart and his prewar work. The personnel file is still needed for the immediate pre-OSS affiliation.",
                "name_variants": ["Arthur W Stewart Jr", "Arthur Walter Stewart"],
                "next_action": "Review the indexed Box 746 personnel file to identify Arthur Walter Stewart's immediate pre-OSS affiliation and last civilian employer. Dixie Art Colony participation is documented but is not employment.",
                "archival_review_priority": "medium",
            }
        )
    elif row == 45:
        update["name_variants"] = ["Harrison M Stewart Jr"]
    return update


def unresolved_update(row: int) -> dict[str, object]:
    person_id, name = PEOPLE[row]
    return {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, Box 746 and archive location, but staged NARA context, CIA Reading Room, exact-name, occupation, employer, obituary, institutional, newspaper, directory, Library of Congress and archival searches found no defensible identity bridge. {UNRESOLVED[row]}",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": "Review the indexed Box 746 personnel file for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "critical" if row in {25, 31, 42} else "high",
    }


def person_updates() -> list[dict[str, object]]:
    updates = [accepted_update(item) for item in ARMY_OCCUPATIONS]
    updates.extend(unresolved_update(row) for row in UNRESOLVED)
    return updates


def research_attempts() -> list[dict[str, object]]:
    accepted_rows = {int(item["row"]) for item in ARMY_OCCUPATIONS}
    attempts = []
    for row, (person_id, name) in PEOPLE.items():
        if row in accepted_rows:
            outcome = "source_reviewed"
            if row == 36:
                detail = "The official Army identity and occupation were accepted. Institutional art sources support Arthur Walter Stewart's 1936 Dixie Art Colony participation and prewar activity, but do not name an immediate employer."
                sources_reviewed = 11
                rejected = 4
            else:
                detail = "A reviewed official Army identity and dated historical occupation or student category were accepted; no named employer is supplied."
                sources_reviewed = 8
                rejected = 5
        else:
            outcome = "candidate_rejected"
            detail = UNRESOLVED[row]
            sources_reviewed = 7
            rejected = 7
        attempts.append(
            {
                "key": f"page448-row{row}-{slug(name)}-b916",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA/index context; CIA Reading Room and Library of Congress official-domain exact-name checks; OSS, rank and spelling variants; employer and occupation; obituary, institutional, newspaper, directory and archival searches; Box 746; protected-identifier Army crosswalk where available",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_916",
                "started_at": "2026-10-26T01:56:00Z",
                "completed_at": "2026-10-26T02:42:00Z",
                "outcome": outcome,
                "sources_reviewed": sources_reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, discovery-only results, chronologically incompatible records and postwar-only material were not assigned." if row in accepted_rows else detail,
                "research_notes": f"{detail} Search-result snippets were discovery aids only; public claims point to inspectable sources. No access control was bypassed, and no exposed NARA API credential was used.",
                "next_action": "Review the indexed Box 746 personnel file for exact employment dates and the documented pre-OSS transition." if row == 36 else "Review the indexed Box 746 personnel file for corroborating identifiers and the last documented pre-OSS affiliation.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b916-v1",
            }
        )
    return attempts


def main() -> None:
    claims: list[dict[str, object]] = []
    for item in ARMY_OCCUPATIONS:
        claims.extend(army_claims(item))
    claims.extend(arthur_claims())
    bundle = {
        "bundle_version": "batch-916-v1",
        "reviewer": "Before OSS Batch 916 evidence review",
        "sources": sources(),
        "organizations": organizations(),
        "affiliations": affiliations(),
        "claims": claims,
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }
    OUTPUT.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
