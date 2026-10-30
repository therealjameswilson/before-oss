#!/usr/bin/env python3
"""Generate the reviewed Batch 964 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page472-oliver-trechter-to-walter-treumann-"
    "review_batch-964_2026-10-29.json"
)

INDEX = "nara-index-b964"
ARMY = "army-bulk-b964"
TECH = "army-tech-b964"
CODES = "army-codes-b964"
GINNY = "loc-ginny-mission-b964"
TREGOR = "mmwf-nison-tregor-b964"
TRESSLER_USGS = "usgs-willis-tressler-1941-b964"
TRESSLER_USNI = "usni-willis-tressler-b964"


PEOPLE = {
    26: ("6fe4eaa1-86c3-5d63-b223-68b2fda75b23", "Oliver E Trechter"),
    27: ("aa208071-c04b-5558-914a-ad29030b8351", "Barton G Treece"),
    28: ("e86d1332-e250-5dba-9617-39881a7b50b4", "Charles J Trees"),
    29: ("2154d06f-9bf5-540e-91cb-457981d016ee", "Jack R Trees"),
    30: ("0718d886-9fd4-5f31-898d-dbceafc4595d", "John R Tregenza"),
    31: ("feb195b8-d812-5ea4-a6fe-099fcf1f4fa8", "Benny J Treglia"),
    32: ("e01974ac-1197-5c29-bd10-f2d67bef32f1", "Nison A Tregor"),
    33: ("e3f8a928-a21e-5256-8a0d-afe6fd52e211", "Guillaume M Treguier"),
    34: ("d9e3e3c9-c5c5-5678-8c31-457ee5325861", "Richard W Treiber"),
    35: ("b5cd7e5e-3876-538e-9d87-314f6a070e11", "John Treisner"),
    36: ("5764ba1f-30c0-524e-b87d-30f17d35fa85", "Raymond A Tremblay"),
    37: ("2759e2e9-c59f-51e0-a2f6-30e5ba9706cf", "Liberty J Tremonte"),
    38: ("b9829380-0583-5381-9759-6afa04b0f1d9", "Walter N Trenerry"),
    39: ("a5500bfe-9a3b-5869-ba82-bb6bb0fedce1", "Louis P Trent"),
    40: ("14ff91bd-993e-5aa5-b86b-73be3482c144", "Clarence J Trentman"),
    41: ("d91b1a09-beb1-5319-8181-bbb322b31ac4", "Peter Trerotole"),
    42: ("21c7b171-aa76-57b1-bafe-6358af0661af", "Rudolph Tressel"),
    43: ("a9d1c646-205e-5415-9c0c-9b53ab370f1e", "Willis L Tressler"),
    44: ("994d4a09-36fc-5536-b6ca-5f7bf153131d", "Burton S Tretheway"),
    45: ("b62e39d5-4d63-5bec-8d26-41a28df5984e", "Vincent R Treul"),
    46: ("94c8d58c-9b7d-5f1c-b385-330e76891e1b", "Walter Treumann"),
}


ARMY_OCCUPATIONS = [
    {
        "row": 26,
        "date": "1942-11-05",
        "code": "992",
        "occupation": "Students",
        "public_occupation": "student",
        "relationship": "student",
        "locator": "PDF physical page 304; amended historical category 9-92",
        "variant": "Oliver E Trechter Jr",
    },
    {
        "row": 29,
        "date": "1943-03-02",
        "code": "992",
        "occupation": "Students",
        "public_occupation": "student",
        "relationship": "student",
        "locator": "PDF physical page 304; amended historical category 9-92",
    },
    {
        "row": 31,
        "date": "1942-09-08",
        "code": "773",
        "occupation": "Cranemen, derrickmen, hoistmen, and shovelmen",
        "public_occupation": "craneman, derrickman, hoistman, or shovelman",
        "relationship": "employment",
        "locator": "PDF physical page 175; historical category 7-73",
    },
    {
        "row": 33,
        "date": "1942-07-25",
        "code": "226",
        "occupation": "Cooks, except private family",
        "public_occupation": "cook, except private family",
        "relationship": "employment",
        "locator": "PDF physical page 172; historical category 2-26",
    },
    {
        "row": 36,
        "date": "1943-06-24",
        "code": "461",
        "occupation": "Skilled occupations in manufacture of boots and shoes",
        "public_occupation": "skilled boot or shoe manufacturing occupation",
        "relationship": "employment",
        "locator": "PDF physical page 173; historical category 4-61",
    },
    {
        "row": 37,
        "date": "1943-03-08",
        "code": "693",
        "occupation": "Semiskilled occupations in fabrication of metal products, n.e.c.",
        "public_occupation": "semiskilled metal-products fabrication occupation, not elsewhere classified",
        "relationship": "employment",
        "locator": "PDF physical page 174; historical category 6-93",
    },
    {
        "row": 44,
        "date": "1943-03-17",
        "code": "992",
        "occupation": "Students",
        "public_occupation": "student",
        "relationship": "student",
        "locator": "PDF physical page 304; amended historical category 9-92",
    },
    {
        "row": 45,
        "date": "1942-10-24",
        "code": "101",
        "occupation": "Bookkeepers and cashiers, except bank cashiers",
        "public_occupation": "bookkeeper or cashier, except bank cashier",
        "relationship": "employment",
        "locator": "PDF physical page 171; historical category 1-01",
        "variant": "Vincent R Treul Jr",
    },
]


UNRESOLVED = {
    27: "A postwar Oklahoma professional-engineer namesake is plausible, but no protected identifier, OSS assignment or Box 784 bridge establishes that biography.",
    28: "Exact-name, official-domain, occupation, obituary, institutional, newspaper and archival searches produced no defensible identity bridge.",
    30: "Modern banking and family namesakes are chronologically incompatible or lack an OSS, protected-identifier or Box 784 bridge.",
    34: "Patent and other exact-name results did not establish the indexed person's identity, wartime service or pre-OSS affiliation.",
    35: "The no-initial name produced only weak genealogy and cemetery leads with no corroborating OSS or Box 784 identifier.",
    38: "A rare-name Minnesota lawyer and historian is a plausible namesake, but accessible sources do not connect his biography to OSS, the protected identifier or Box 785.",
    39: "The name is insufficiently distinctive, and accessible lawyer and public-record namesakes lack compatible wartime and OSS selectors.",
    40: "The protected identifier produced no Army bulk candidate, and exact-name searches produced no independent OSS or pre-OSS affiliation source.",
    41: "Exact-name and spelling-variant searches produced no reliable identity, occupation or institutional bridge.",
    42: "The no-initial name produced unrelated or insufficiently specific military and obituary results with no Box 785 bridge.",
    46: "A German-Jewish refugee and later State Department lawyer is a plausible rare-name lead, but no accessible source directly connects that biography to the Box 785 index row.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 784-785",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 472, rows 26-46; checked against layout-preserving text and the 200 dpi page render",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 21 printed rows remain separate. Protected identifiers remain private.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; eight accepted Batch 964 identity candidates; protected identifiers withheld",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "No raw bulk row, record ordinal or full protected identifier enters the evidence bundle or public assets. Historical occupation codes identify neither employers nor workplaces.",
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
            "access_date": "2026-10-29",
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
            "locator": "PDF physical pages 171-175 and 304; categories 1-01, 2-26, 4-61, 6-93, 7-73 and amended 9-92 visually checked",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Students is status, not employment. Historical occupation groups are qualified and never converted into named employers or exact workplaces.",
        },
        {
            "key": GINNY,
            "stable_url": "https://tile.loc.gov/storage-services/service/ll/llmlp/2011525363_NT_Nazi_Vol-V/2011525363_NT_Nazi_Vol-V.pdf",
            "archival_identifier": "Document 2610-PS",
            "title": "Nazi Conspiracy and Aggression, Volume V",
            "author_creator": "Office of United States Chief of Counsel for Prosecution of Axis Criminality",
            "repository_publisher": "United States Government Printing Office; Library of Congress digital copy",
            "publication_record_date": "1946",
            "locator": "PDF physical pages 335-336; affidavit concerning United States v. Anton Dostler and the Ginny Mission",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "Military Legal Resources, Library of Congress",
            "document_number": "2610-PS",
            "rights_notes": "The original published affidavit independently confirms Tremonte's exact identity, Army grade and 2677th Special Reconnaissance Battalion assignment. The public claim omits the protected identifier.",
        },
        {
            "key": TREGOR,
            "stable_url": "https://www.mmwf.org/monuments-men-and-women/nison-tregor",
            "title": "Captain Nison A. Tregor (US Army) (1904-1972)",
            "author_creator": "Monuments Men and Women Foundation",
            "repository_publisher": "Monuments Men and Women Foundation",
            "publication_record_date": None,
            "locator": "Biography sections covering 1920s-1930s portrait commissions, Washington studio, 1943 Army service and MFAA work",
            "access_date": "2026-10-29",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Monuments Men and Women biographies",
            "rights_notes": "The biography supports prewar commissioned sculpture and wartime Army context, but does not establish the exact OSS transfer date.",
        },
        {
            "key": TRESSLER_USGS,
            "stable_url": "https://pubs.usgs.gov/pp/0196c/report.pdf",
            "archival_identifier": "U.S. Geological Survey Professional Paper 196-C",
            "title": "Geology and Biology of North Atlantic Deep-Sea Cores Between Newfoundland and Ireland, Part 4: Ostracoda",
            "author_creator": "Willis L. Tressler",
            "repository_publisher": "United States Geological Survey; United States Government Printing Office",
            "publication_record_date": "1941",
            "locator": "Title page and scientific report",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "USGS Professional Papers",
            "document_number": "Professional Paper 196-C",
            "rights_notes": "The paper documents prewar scientific authorship, not employment by USGS or an immediate OSS affiliation.",
        },
        {
            "key": TRESSLER_USNI,
            "stable_url": "https://www.usni.org/people/willis-l-tressler",
            "title": "Willis L. Tressler",
            "author_creator": "U.S. Naval Institute",
            "repository_publisher": "U.S. Naval Institute",
            "publication_record_date": "1955",
            "locator": "Contributor biography for the November 1955 article Arctic and Antarctic",
            "access_date": "2026-10-29",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Proceedings contributor biographies",
            "rights_notes": "Used only to corroborate the scientist's field and publication continuity; the later Hydrographic Office position is not presented as pre-OSS employment.",
        },
    ]


def army_affiliation(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    return {
        "key": f"{slug(PEOPLE[row][1])}-occupation-b964",
        "person_id": PEOPLE[row][0],
        "occupation": item["public_occupation"],
        "relationship_type": item["relationship"],
        "end_date": item["date"],
        "date_precision": f"Historical civilian-occupation code {item['code']} was recorded at Army entry on {item['date']}; no employer, school, workplace or OSS-transfer date is named.",
        "country": "United States",
        "immediate_pre_oss": False,
        "last_civilian_pre_service": False,
        "pre_oss_temporal_basis": "strongly_date_bounded",
        "identity_confidence": "confirmed" if row == 37 else "high_confidence",
        "claim_confidence": "medium",
        "source_quality": "A_direct_official",
        "publication_status": "publish_qualified",
        "research_notes": "The historical category is not converted into a named employer, workplace, school, immediate affiliation or exact modern job title.",
    }


def claim(
    row: int,
    key: str,
    claim_type: str,
    claim_text: str,
    evidence_paraphrase: str,
    identity: str,
    temporal: str,
    source_quality: str,
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
        "claim_text": claim_text,
        "evidence_paraphrase": evidence_paraphrase,
        "identity_match_assessment": identity,
        "temporal_assessment": temporal,
        "source_quality": source_quality,
        "claim_confidence": confidence,
        "publication_status": publication_status
        or ("published" if confidence in {"confirmed", "high"} else "publish_qualified"),
        "match_notes": notes,
        "sources": source_links,
    }


def army_claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for item in ARMY_OCCUPATIONS:
        row = int(item["row"])
        name = PEOPLE[row][1]
        variant = item.get("variant")
        direct = row == 37
        paraphrase = "A nonshared protected identifier connects the visually verified index row to the official Army record."
        assessment = "High confidence from exact protected-identifier agreement plus compatible full-name evidence."
        confidence = "high"
        if variant:
            paraphrase += f" The Army record prints the preserved variant {variant}."
        if direct:
            paraphrase += " An independently published original military-trial affidavit repeats the same identity and wartime unit."
            assessment = "Confirmed by exact protected-identifier agreement, exact full-name evidence and an independent original military-trial record."
            confidence = "confirmed"
        links: list[dict[str, object]] = [
            {"source_key": INDEX, "locator_override": f"PDF page 472 row {row}; protected identifier withheld"},
            {"source_key": ARMY, "locator_override": "Accepted reviewed identity bridge; protected identifier withheld"},
        ]
        if direct:
            links.append(
                {
                    "source_key": GINNY,
                    "locator_override": "Document 2610-PS; PDF physical pages 335-336; protected identifier withheld",
                    "excerpt_override": "Technician Fifth Grade Liberty J. Tremonte",
                }
            )
        values.append(
            claim(
                row,
                f"identity-{slug(name)}-army-b964",
                "identity",
                f"Indexed {name} is a {'confirmed' if direct else 'high-confidence'} match to the reviewed official Army entry.",
                paraphrase,
                assessment,
                "Identity evidence only; the Army entry does not itself establish an OSS transfer date.",
                "A_direct_official",
                confidence,
                links,
                "The review accepts identity only for this source row, preserves source spellings and does not expose the protected identifier.",
            )
        )
        category = str(item["occupation"])
        if item["relationship"] == "student":
            text = f"At Army entry on {item['date']}, {name} was recorded in the historical Students category; no school or employer is identified."
        else:
            text = f"At Army entry on {item['date']}, the record coded {name}'s civilian occupation as {category}."
        values.append(
            claim(
                row,
                f"occupation-{slug(name)}-army-b964",
                "occupation",
                text,
                f"The official Army record contains civilian-occupation code {item['code']}; NARA's historical code list expands it to {category}.",
                "Confirmed identity from three agreeing direct records." if direct else "High-confidence identity from the accepted protected-identifier bridge and compatible full-name evidence.",
                "The code was recorded at Army entry and is date-bounded, but it identifies no employer, workplace, school or immediate OSS predecessor.",
                "A_direct_official",
                "medium",
                [
                    {"source_key": ARMY, "locator_override": f"Accepted identity record; civilian occupation code {item['code']}; protected identifier withheld"},
                    {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46; Army-entry-date and civilian-occupation fields"},
                    {"source_key": CODES, "locator_override": str(item["locator"]), "excerpt_override": category},
                ],
                "The historical category is published as qualified occupation or status evidence and is excluded from named-employer analytics.",
                f"{slug(name)}-occupation-b964",
                "publish_qualified",
            )
        )
    return values


def specialist_affiliations() -> list[dict[str, object]]:
    return [
        {
            "key": "nison-a-tregor-sculptor-b964",
            "person_id": PEOPLE[32][0],
            "role_title": "commissioned portrait sculptor",
            "occupation": "sculptor",
            "relationship_type": "self_employment",
            "end_date": "1943",
            "date_precision": "The institutional biography documents portrait commissions and a Washington studio before his 1943 Army service; it does not prove the final day of civilian work.",
            "city": "Washington",
            "state_or_region": "District of Columbia",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "high_confidence",
            "claim_confidence": "medium",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "publish_qualified",
            "research_notes": "The biography establishes commissioned sculptural work before Army service but does not identify an employer or the exact OSS transfer chronology.",
        },
        {
            "key": "willis-l-tressler-scientific-research-b964",
            "person_id": PEOPLE[43][0],
            "occupation": "scientific researcher and author on ostracods",
            "relationship_type": "professional_affiliation",
            "end_date": "1941",
            "date_precision": "A 1941 federal scientific paper documents authorship before the wartime OSS period; no employer or transfer date is established.",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "probable",
            "claim_confidence": "medium",
            "source_quality": "A_direct_official",
            "publication_status": "publish_qualified",
            "research_notes": "The rare exact name and continuous scientific specialty support a probable identity only. USGS is the publisher, not a claimed employer.",
        },
    ]


def claims() -> list[dict[str, object]]:
    values = army_claims()
    values.extend(
        [
            claim(
                37,
                "service-liberty-j-tremonte-ginny-b964",
                "identity",
                "An original U.S. military-trial affidavit identifies Liberty J. Tremonte as a technician fifth grade in the 2677th Special Reconnaissance Battalion during the Ginny Mission.",
                "Document 2610-PS names Tremonte, his grade and the battalion among the fifteen U.S. soldiers captured after landing near Stazione di Framura in March 1944.",
                "Confirmed by the exact full name and protected identifier independently repeated in the index, Army bulk file and original trial affidavit.",
                "The source documents a wartime Army assignment during OSS service, not the preceding civilian employer.",
                "A_direct_official",
                "confirmed",
                [
                    {"source_key": INDEX, "locator_override": "PDF page 472 row 37; protected identifier withheld"},
                    {"source_key": GINNY, "locator_override": "Document 2610-PS; PDF physical pages 335-336", "excerpt_override": "two officers and thirteen enlisted men of the 2677th Special Reconnaissance Battalion"},
                ],
                "The public claim omits the full identifier and does not call the historical occupation code an employer.",
            ),
            claim(
                32,
                "identity-nison-a-tregor-b964",
                "identity",
                "Indexed Nison A. Tregor is a high-confidence match to the sculptor and U.S. Army Monuments officer documented by the Monuments Men and Women Foundation.",
                "The institutional biography supplies the rare exact full name, 1904 birth, Washington sculptural career, 1943 Army service, captain's grade and European restitution work.",
                "High confidence from a rare exact full name plus compatible U.S. Army chronology, commissioned grade and specialized wartime European service.",
                "The source establishes wartime Army service but not the exact date or channel of OSS assignment.",
                "B_authoritative_institutional",
                "high",
                [
                    {"source_key": INDEX, "locator_override": "PDF page 472 row 32; Box 784"},
                    {"source_key": TREGOR, "locator_override": "Biography and wartime-service sections"},
                ],
                "The Box 784 file remains necessary to confirm the OSS administrative path and immediate predecessor.",
            ),
            claim(
                32,
                "prewar-nison-a-tregor-sculptor-b964",
                "other_pre_oss_affiliation",
                "Before Army service, Nison A. Tregor worked as a commissioned portrait sculptor from his own Washington studio.",
                "The institutional biography documents 1920s-1930s portrait commissions, a Washington residence and studio, and major completed subjects before U.S. entry into the war.",
                "High-confidence identity from the rare exact name and compatible Army and specialist chronology.",
                "Documented prewar self-employment; the source does not explicitly call it the immediate pre-OSS affiliation or name a separate employer.",
                "B_authoritative_institutional",
                "medium",
                [{"source_key": TREGOR, "locator_override": "1920s-1930s career and Washington-studio sections"}],
                "Published as qualified earlier pre-OSS self-employment and excluded from immediate-affiliation analytics.",
                "nison-a-tregor-sculptor-b964",
                "publish_qualified",
            ),
            claim(
                43,
                "identity-willis-l-tressler-b964",
                "identity",
                "The indexed Willis L. Tressler is a probable match to the ostracod researcher who published a federal scientific paper in 1941.",
                "A 1941 USGS paper and a later Naval Institute biography document the rare exact name and a continuous career in limnology, ecology, taxonomy and oceanography.",
                "Probable from the rare exact full name and continuous specialist field; no independent public source yet supplies an OSS, Box 785 or protected-identifier bridge.",
                "The paper predates the OSS period, while the later biography corroborates field continuity only.",
                "A_direct_official",
                "medium",
                [
                    {"source_key": INDEX, "locator_override": "PDF page 472 row 43; Box 785"},
                    {"source_key": TRESSLER_USGS, "locator_override": "1941 title page and report"},
                    {"source_key": TRESSLER_USNI, "support_type": "context_only", "locator_override": "1955 contributor biography"},
                ],
                "The identity remains visibly qualified and excluded from confirmed/high identity analytics pending Box 785 review.",
                publication_status="publish_qualified",
            ),
            claim(
                43,
                "prewar-willis-l-tressler-research-b964",
                "occupation",
                "A probable identity match indicates that Willis L. Tressler was publishing scientific research on ostracods in 1941.",
                "The federal report names Willis L. Tressler as author of the Ostracoda section of a North Atlantic deep-sea-core study.",
                "Probable identity only; the rare exact name and later field continuity are supportive but do not independently prove the OSS match.",
                "The report is explicitly dated 1941 and therefore documents prewar scientific work, but not an employer or immediate affiliation.",
                "A_direct_official",
                "medium",
                [{"source_key": TRESSLER_USGS, "locator_override": "1941 title page and report"}],
                "USGS is treated as publisher, not employer. The claim remains qualified pending personnel-file review.",
                "willis-l-tressler-scientific-research-b964",
                "publish_qualified",
            ),
        ]
    )
    return values


def unresolved_update(row: int, reason: str) -> dict[str, object]:
    person_id, name = PEOPLE[row]
    box = "784" if row <= 37 else "785"
    location = "230/86/42/02" if row <= 37 else "230/86/42/03"
    return {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, Box {box} and archive location {location}. {reason}",
        "personnel_category": "unknown_or_indeterminate",
        "commissioned_officer": None,
        "allied_or_foreign_personnel": False,
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": "Review the indexed personnel file for corroborating identifiers, immediate pre-OSS affiliation and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }


def army_update(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    person_id, name = PEOPLE[row]
    direct = row == 37
    evidence = f"A nonshared protected identifier connects the visually verified {name} index row to the reviewed official Army record."
    if direct:
        evidence += " An independent original military-trial affidavit repeats the exact identity and wartime unit."
    update: dict[str, object] = {
        "person_id": person_id,
        "identity_status": "confirmed" if direct else "high_confidence",
        "identity_evidence": evidence,
        "personnel_category": "enlisted_army_personnel",
        "commissioned_officer": False,
        "allied_or_foreign_personnel": False,
        "manual_review_required": True,
        "research_status": "occupation_only_found",
        "next_action": "Review Box 784 or 785 to establish the immediate pre-OSS affiliation and named last civilian employer; do not convert the Army occupation category into a workplace.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }
    if item.get("variant"):
        update["name_variants"] = [item["variant"]]
        update["identity_evidence"] = f"{evidence} The Army record preserves the compatible variant {item['variant']}."
    return update


def person_updates() -> list[dict[str, object]]:
    values = [unresolved_update(row, reason) for row, reason in UNRESOLVED.items()]
    values.extend(army_update(item) for item in ARMY_OCCUPATIONS)
    values.extend(
        [
            {
                "person_id": PEOPLE[32][0],
                "identity_status": "high_confidence",
                "identity_evidence": "A rare exact full name, compatible U.S. Army chronology, commissioned grade and specialized European wartime service connect the index row to the institutional Monuments biography.",
                "personnel_category": "commissioned_army_officer",
                "commissioned_officer": True,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "occupation_only_found",
                "next_action": "Review Box 784 to confirm Nison Tregor's OSS administrative path and determine whether his documented sculptural self-employment was the immediate predecessor.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[43][0],
                "identity_status": "probable",
                "identity_evidence": "A 1941 federal scientific paper and later institutional biography supply the rare exact name and continuous specialist field, but no independent OSS, Box 785 or protected-identifier bridge.",
                "personnel_category": "unknown_or_indeterminate",
                "commissioned_officer": None,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "occupation_only_found",
                "next_action": "Review Box 785 to confirm whether the indexed Willis L. Tressler is the ostracod researcher and to identify his immediate pre-OSS affiliation and employer.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
        ]
    )
    return values


def research_attempts() -> list[dict[str, object]]:
    army_rows = {int(item["row"]) for item in ARMY_OCCUPATIONS}
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        if row in army_rows:
            outcome, reviewed, rejected = "source_reviewed", 9, 5
            detail = "Accepted an exact nonshared protected-identifier Army bridge and verified the dated historical civilian-occupation code against NARA technical documentation."
            if row == 37:
                reviewed = 11
                detail += " An original U.S. military-trial affidavit independently confirmed Liberty Tremonte's identity, grade and wartime unit."
        elif row == 32:
            outcome, reviewed, rejected = "source_reviewed", 10, 6
            detail = "An authoritative institutional biography supplied a rare-name, Army-chronology and specialist-role match plus documented prewar commissioned sculpture; immediacy remains unproved."
        elif row == 43:
            outcome, reviewed, rejected = "source_reviewed", 10, 7
            detail = "A 1941 federal scientific paper and institutional biography support a probable rare-name identity and prewar scientific occupation, but not a confirmed OSS bridge or employer."
        else:
            outcome, reviewed, rejected = "no_result", 7, 6
            detail = UNRESOLVED[row]
        attempts.append(
            {
                "key": f"page472-row{row}-{slug(name)}-b964",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index and official Archives context; CIA Reading Room or equivalent official-source check; exact-name and meaningful variants; OSS, Army and rank clues; employer and occupation 1940; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Boxes 784-785; protected identifiers used only when defensible",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_964",
                "started_at": "2026-10-30T04:40:00Z",
                "completed_at": "2026-10-30T06:35:00Z",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search snippets, unsourced genealogy, people-finder pages, postwar-only leads and sources without an OSS, protected-identifier or Box-file bridge were rejected. Education and occupation categories were not converted into named employers. Search aliases were not treated as silent corrections.",
                "research_notes": f"{detail} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain, CIA Reading Room-equivalent and Library of Congress searches were checked as applicable. The index page, Army bulk file, technical documentation, occupation-code pages and cited original or institutional sources were inspected directly. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": "Review the indexed personnel file for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before wartime service.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b964-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-964-v1",
        "reviewer": "Before OSS Batch 964 evidence review",
        "sources": sources(),
        "organizations": [],
        "affiliations": [army_affiliation(item) for item in ARMY_OCCUPATIONS]
        + specialist_affiliations(),
        "claims": claims(),
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }
    EvidenceBundle.model_validate(bundle)
    OUTPUT.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
