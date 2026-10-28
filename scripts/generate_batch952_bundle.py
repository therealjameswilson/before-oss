#!/usr/bin/env python3
"""Generate the reviewed Batch 952 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page466-janet-f-thompson-to-theodore-j-thompson-"
    "review_batch-952_2026-10-28.json"
)

INDEX = "nara-index-b952"
ARMY = "army-bulk-b952"
TECH = "army-tech-b952"
CODES = "army-codes-b952"
NYT = "nyt-nancy-sweezy-b952"
LOC = "loc-nancy-sweezy-b952"
GUARDIAN = "guardian-nancy-sweezy-b952"


PEOPLE = {
    24: ("486640ca-c038-582b-b4df-dbd512dffb45", "Janet F Thompson"),
    25: ("1bc19839-6f39-5e04-b28f-72afa5fd5a3c", "Jewell B Thompson"),
    26: ("b12727ad-b305-5c2c-bd8a-9786837272b3", "John T Thompson"),
    27: ("90a9f102-232c-55fc-a275-ca7ca82c1b38", "John W Thompson"),
    28: ("3cfd83a9-5e1d-5920-98aa-cf7630fdddec", "Joseph E Thompson"),
    29: ("d7944d1c-7b93-5a35-98f2-8cb6737a1a96", "Lamont L Thompson"),
    30: ("a5c0ee99-b8e4-5f70-9074-d113e79440cb", "Laurence M Thompson"),
    31: ("9945b7ec-9ab9-56fc-a484-94becd5fbcd4", "LeeRoy Thompson"),
    32: ("0619c540-23cf-5697-87f7-fc058871e222", "Marion D Thompson"),
    33: ("2660465b-63d6-59c1-91d4-aca054d72759", "Mary E Thompson"),
    34: ("5bbd054a-e820-5c74-880c-9d85235342a1", "Mary A Thompson"),
    35: ("e3590a5f-1007-5f0a-b106-3cd81c58bd33", "Nancy Thompson"),
    36: ("5fba512f-eb22-5ebe-a53c-b0c4217cea38", "Opal P Thompson"),
    37: ("db62cb8f-a017-52ec-ab96-dff3b9f0b147", "Paul A Thompson"),
    38: ("a137be31-3157-5cfa-becf-f2423659260b", "Pauline A Thompson"),
    39: ("316ee217-052d-5203-9c80-8e70dbe46774", "Phyllis A Thompson"),
    40: ("227b24f6-fef9-5e1e-869b-bce9ca091e47", "Ralph Thompson"),
    41: ("b148c9ce-6792-5234-a0ee-31c9ab74c08d", "Raymond L Thompson"),
    42: ("6fb2c556-c7fa-554b-ae71-fb622729f5ab", "Robert E Thompson"),
    43: ("e2993cc7-b644-5a99-a169-2d65da695dbc", "Robert G Thompson"),
    44: ("1df0f65e-1f98-54cb-8ffc-bc9fc1f32bd7", "Robert J Thompson"),
    45: ("d3720510-804f-551f-a937-ca629f97c340", "Russell D Thompson"),
    46: ("80bf6dfc-a271-5271-9c32-efb46e068114", "Theodore J Thompson"),
}


UNRESOLVED = {
    24: "Modern legal-professional results are decades too late and provide no OSS or Box 774 bridge.",
    25: "Genealogy and people-finder results identify multiple Jewell Thompson namesakes but provide no OSS or Box 774 bridge.",
    26: "Common-name military, obituary and directory results lack two corroborating identifiers beyond the indexed name.",
    27: "Modern executive and veteran namesakes are chronologically impossible or lack an OSS and Box 774 bridge.",
    28: "A World War II Navy captain and other exact-name candidates lack an OSS, Box 775 or second-identifier bridge.",
    29: "A discovery-only death-index candidate and other namesakes supply no OSS or Box 775 linkage.",
    30: "Modern directory and people-finder results provide no defensible wartime identity or employment chronology.",
    31: "Postwar LeeRoy and Leroy Thompson obituaries concern younger or otherwise unbridged namesakes.",
    32: "Exact-name, official-domain, obituary and institutional searches produced no reliable identity or pre-OSS affiliation.",
    33: "Modern obituaries and historical directory fragments identify incompatible Mary E Thompson namesakes without an OSS bridge.",
    34: "Historical vital-record and directory results lack an OSS, Box 775 or corroborating identity bridge.",
    36: "Exact-name, occupation, obituary, institutional and archival searches produced no defensible identity bridge.",
    38: "Modern academic and obituary results concern later Pauline A Thompson namesakes and were not assigned.",
    39: "Modern employment, academic and discovery-only death results concern later or unbridged namesakes.",
    40: "Postwar Night Stalker articles, military rosters and several modern obituaries concern other Ralph Thompson namesakes.",
    41: "Earlier automated attempts and the current exact-name, official, newspaper, obituary and employment recheck found no Box 775 identity bridge.",
    42: "The prominent journalist Robert Elliott Thompson served in the wartime Navy, not the OSS; other exact-name records remain unbridged.",
    43: "Multiple World War II Robert G Thompson military records remain unselectable without a Box 775 or second-identifier bridge.",
    44: "Genealogy, obituary and modern records concern incompatible or unbridged Robert J Thompson namesakes.",
    45: "Modern business and obituary results provide no defensible wartime identity or Box 775 bridge.",
    46: "An Army Air Forces lieutenant missing in 1943 and a distinct Navy veteran are incompatible unbridged candidates; neither is assigned.",
}


ATTEMPT_NUMBERS = {row: 5 for row in PEOPLE}
ATTEMPT_NUMBERS[24] = 6
ATTEMPT_NUMBERS[41] = 17


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 774-775",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 466, rows 24-46; checked against layout-preserving text and a 220 dpi page render",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. Rows 24-27 are in Box 774 and rows 28-46 in Box 775. Full protected identifiers remain private.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; one reviewed Batch 952 candidate; protected identifier withheld",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "No raw bulk row or full protected identifier is retained in public assets. Paul A Thompson's identity was accepted; the occupation category names no employer.",
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
            "locator": "PDF physical page 173; historical category 4-75, Machinists",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "The historical occupation label is qualified and is never converted into a named employer, workplace or exact modern trade specialization.",
        },
        {
            "key": NYT,
            "stable_url": "https://www.nytimes.com/2010/02/26/arts/design/26sweezy.html",
            "archival_identifier": "The New York Times, February 25, 2010",
            "title": "Nancy Sweezy, Savior of Jugtown Pottery, Dies at 88",
            "author_creator": "Douglas Martin",
            "repository_publisher": "The New York Times",
            "publication_record_date": "2010-02-25",
            "locator": "Biographical paragraph reporting birth name, adoption, art-school study and OSS Research Branch work",
            "access_date": "2026-10-28",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "The New York Times obituaries",
            "rights_notes": "Used only as a concise identity lead. The common-name index row still lacks a second selector or Box 775 bridge, so the candidate is withheld from public facts.",
        },
        {
            "key": LOC,
            "stable_url": "https://tile.loc.gov/storage-services/service/gdc/gdcfindingaidpdfs/af020001/af020001.pdf",
            "archival_identifier": "AFC 2017/001; LCCN 2017655202",
            "title": "Nancy Sweezy collection [finding aid]",
            "author_creator": "Jesse Hocking and Carolina Restrepo; revised by Jesse Hocking and Sara Ludewig",
            "repository_publisher": "American Folklife Center, Library of Congress",
            "publication_record_date": "2020; revised 2023",
            "locator": "PDF page 2 biographical note; PDF page 44 wartime letters and European Political Report files",
            "access_date": "2026-10-28",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Nancy Sweezy collection",
            "rights_notes": "The finding aid establishes Nancy Sweezy's School of the Museum of Fine Arts study and overseas OSS Research and Analysis work, but does not print Thompson as her birth surname.",
        },
        {
            "key": GUARDIAN,
            "stable_url": "https://www.theguardian.com/p/2fj64",
            "archival_identifier": "The Guardian, Other Lives, March 15, 2010",
            "title": "Nancy Sweezy obituary",
            "author_creator": "Martha Sweezy",
            "repository_publisher": "The Guardian",
            "publication_record_date": "2010-03-15",
            "locator": "Obituary by her daughter; OSS analytical work and 1944 overseas chronology",
            "access_date": "2026-10-28",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Other Lives",
            "rights_notes": "Corroborates Nancy Sweezy's OSS chronology but does not independently supply the Thompson birth-name bridge.",
        },
    ]


def affiliations() -> list[dict[str, object]]:
    return [
        {
            "key": "paul-a-thompson-machinist-b952",
            "person_id": PEOPLE[37][0],
            "occupation": "machinist",
            "relationship_type": "employment",
            "end_date": "1941-04-03",
            "date_precision": "Historical category 4-75 was recorded at Army entry on 1941-04-03; no employer, shop, workplace or OSS-transfer date is named.",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "high_confidence",
            "claim_confidence": "medium",
            "source_quality": "A_direct_official",
            "publication_status": "publish_qualified",
            "research_notes": "The historical category is not converted into a named employer, workplace, exact specialization or immediate pre-OSS affiliation.",
        }
    ]


def claims() -> list[dict[str, object]]:
    return [
        {
            "key": "identity-paul-a-thompson-b952",
            "person_id": PEOPLE[37][0],
            "claim_type": "identity",
            "claim_text": "The indexed Paul A Thompson is a high-confidence match to the reviewed official Army record.",
            "evidence_paraphrase": "A nonshared protected identifier and exact full-name agreement connect the visually verified index row to the official Army record.",
            "identity_match_assessment": "High confidence from an exact full name and a private nonshared identifier.",
            "temporal_assessment": "The Army record dates entry into service but does not establish the exact OSS transfer date.",
            "source_quality": "A_direct_official",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "This identity decision does not establish a named employer or immediate OSS predecessor.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 466 row 37; Box 775; protected identifier withheld"},
                {"source_key": ARMY, "locator_override": "Reviewed name record; protected identifier withheld"},
                {"source_key": TECH, "support_type": "context_only", "locator_override": "Field definitions, PDF physical pages 44-46"},
            ],
        },
        {
            "key": "occupation-paul-a-thompson-b952",
            "person_id": PEOPLE[37][0],
            "affiliation_key": "paul-a-thompson-machinist-b952",
            "claim_type": "occupation",
            "claim_text": "At Army entry on 1941-04-03, Paul A Thompson was recorded in the historical Machinists category; no employer or workplace is identified.",
            "evidence_excerpt": "Machinists",
            "evidence_paraphrase": "The official bulk record supplies code 475; the visually reviewed NARA code list expands it as Machinists.",
            "identity_match_assessment": "High confidence from the accepted protected-identifier bridge and exact name agreement.",
            "temporal_assessment": "Strongly date-bounded at Army entry, but not shown to be the immediate pre-OSS affiliation.",
            "source_quality": "A_direct_official",
            "claim_confidence": "medium",
            "publication_status": "publish_qualified",
            "match_notes": "Published only as a qualified historical category. No shop, employer, workplace or exact specialization is inferred.",
            "sources": [
                {"source_key": ARMY, "locator_override": "Army entry 1941-04-03; code 475; identifier withheld"},
                {"source_key": CODES, "locator_override": "PDF physical page 173; historical category 4-75"},
            ],
        },
        {
            "key": "candidate-nancy-thompson-sweezy-b952",
            "person_id": PEOPLE[35][0],
            "claim_type": "identity",
            "claim_text": "Folklorist Nancy Sweezy, born Nancy Thompson, is a plausible but unconfirmed candidate for the indexed Nancy Thompson.",
            "evidence_excerpt": "During World War II, she worked overseas in the Research and Analysis Branch",
            "evidence_paraphrase": "A New York Times obituary reports Nancy Sweezy's Thompson birth name and OSS work; the Library of Congress and her daughter's obituary independently document her overseas OSS analytical work and art-school study.",
            "identity_match_assessment": "Ambiguous: the exact birth name and OSS context agree, but the common-name index row has no rank, protected identifier, birth data, assignment or Box 775 selector to supply the required second corroborating identifier.",
            "temporal_assessment": "The candidate sources document School of the Museum of Fine Arts study before OSS work, but none of that chronology may be transferred to the indexed row until identity is resolved.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "low",
            "publication_status": "withheld_low_confidence",
            "match_notes": "The candidate and possible Nancy Adams and Nancy Sweezy variants remain private review leads. No employer or student affiliation is published for the indexed person.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 466 row 35; Box 775"},
                {"source_key": NYT, "locator_override": "Biographical paragraph; birth name, adoption, art school and OSS Research Branch"},
                {"source_key": LOC, "locator_override": "PDF page 2 biographical note; PDF page 44 wartime files"},
                {"source_key": GUARDIAN, "locator_override": "Obituary by Martha Sweezy; OSS analysis and 1944 overseas chronology"},
            ],
        },
    ]


def archival_update(row: int, reason: str) -> dict[str, object]:
    person_id, name = PEOPLE[row]
    box = "774" if row <= 27 else "775"
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


def person_updates() -> list[dict[str, object]]:
    values = [archival_update(row, reason) for row, reason in UNRESOLVED.items()]
    values.extend(
        [
            {
                "person_id": PEOPLE[35][0],
                "identity_status": "ambiguous",
                "identity_evidence": "Folklorist Nancy Sweezy, born Nancy Thompson, is a plausible exact-name OSS candidate, but the common-name Box 775 row supplies no second corroborating selector. Her possible Adams and Sweezy names are not assigned as variants.",
                "personnel_category": "unknown_or_indeterminate",
                "manual_review_required": True,
                "research_status": "needs_identity_review",
                "next_action": "Review Box 775 for birth date, birthplace, adoptive or married names, School of the Museum of Fine Arts study, or Research and Analysis Branch assignment before merging the Nancy Sweezy candidate.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[37][0],
                "identity_status": "high_confidence",
                "identity_evidence": "A nonshared protected identifier and exact full-name agreement connect the visually verified Paul A Thompson index row to the reviewed official Army record.",
                "personnel_category": "enlisted_army_personnel",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "occupation_only_found",
                "next_action": "Review Box 775 to establish the immediate pre-OSS affiliation and named last civilian employer; do not convert the historical Machinists category into a workplace.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
        ]
    )
    return values


def research_attempts() -> list[dict[str, object]]:
    attempts: list[dict[str, object]] = []
    for row in sorted(PEOPLE):
        person_id, name = PEOPLE[row]
        box = "774" if row <= 27 else "775"
        if row in UNRESOLVED:
            outcome = "no_result"
            reviewed = 7
            rejected = 6
            detail = UNRESOLVED[row]
        elif row == 35:
            outcome = "candidate_found"
            reviewed = 10
            rejected = 7
            detail = "Nancy Sweezy is a well-documented OSS analyst born Nancy Thompson, but the common-name index row lacks a second selector; the candidate and her School of the Museum of Fine Arts chronology remain withheld pending Box 775 review."
        elif row == 37:
            outcome = "source_reviewed"
            reviewed = 8
            rejected = 6
            detail = "An accepted protected-identifier Army bridge supports identity and a dated historical Machinists category without naming an employer, workplace or immediate OSS predecessor."
        else:
            raise AssertionError(f"Missing Batch 952 outcome for row {row}")
        attempts.append(
            {
                "key": f"page466-row{row}-{slug(name)}-b952",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index and public Archives context; CIA Reading Room or equivalent official-source check; exact-name and meaningful variants; OSS and military clues; employer and occupation 1940; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Box {box}; protected identifiers used privately only when defensible",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_952",
                "started_at": "2026-10-28T15:20:00Z",
                "completed_at": "2026-10-28T17:20:00Z",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search snippets, unsourced genealogy, people-finder pages, modern records, postwar-only leads and sources without an OSS, protected-identifier or Box-file bridge were not assigned. Robert Elliott Thompson's Navy chronology, a 1943 Theodore J Thompson loss, and modern profiles were rejected or retained only as unassigned alternatives.",
                "research_notes": f"{detail} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain, CIA Reading Room-equivalent and Library of Congress searches were checked as applicable. The index and admitted Army and code-list sources were visually reviewed. The CIA site blocked automated access and the LoC adapter timed out for the first name, so those events are recorded as access outcomes rather than negative searches; equivalent public-domain checks were completed. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": f"Review Box {box} for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before wartime service.",
                "attempt_number": ATTEMPT_NUMBERS[row],
                "research_agent_version": "before-oss-b952-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-952-v1",
        "reviewer": "Before OSS Batch 952 evidence review",
        "sources": sources(),
        "organizations": [],
        "affiliations": affiliations(),
        "claims": claims(),
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }
    EvidenceBundle.model_validate(bundle)
    OUTPUT.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
