#!/usr/bin/env python3
"""Generate the reviewed Batch 941 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page461-ray-l-tarbox-to-jack-h-tattersall-"
    "review_batch-941_2026-10-28.json"
)

INDEX = "nara-index-b941"
ARMY = "army-bulk-b941"
TECH = "army-tech-b941"
CODES = "army-codes-b941"
TARGAKIS = "oss-greek-desk-targakis-b941"
TATE_OSS = "cia-oss-me-solon-tate-b941"
TASSINARI_ANPI = "anpi-ennio-tassinari-b941"
TASSINARI_SIUSA = "siusa-ori-tassinari-b941"

US_ARMY = "us-army-existing-b941"
ORI = "ori-b941"


PEOPLE = {
    1: ("a32c26eb-45b9-5881-98c3-251ce3e8ef9d", "Ray L Tarbox"),
    2: ("5fbf8900-7004-5c7e-a45b-e3836c407c1c", "Laurier R Tardiff"),
    3: ("72293415-151b-59ef-a265-187a0142a5d2", "John Targakis"),
    4: ("486a3afa-aa1c-57ff-9741-24860b997a7c", "John Targakis"),
    5: ("b2496d1b-8659-59c1-aec5-e161411e8658", "Louis Tarmina"),
    6: ("546541b8-c26f-5c09-ac26-0944ef1e2bf6", "Louis Tarnrinn"),
    7: ("bc607451-320d-5b9d-be1d-6f83a66b5c00", "Warren J Tarrant"),
    8: ("1a938ab2-b735-56c3-a1fb-6978403a6f9e", "Frank Tartaro"),
    9: ("2fc76078-f789-57e7-94a2-48874feb2e51", "Lewis S Taschler"),
    10: ("7f2e7c76-8491-5d90-8a2b-51142cb65c5a", "Louis J Taschler"),
    11: ("f61bcdd1-53e6-5a24-9513-90f54c99587c", "Esther Tash"),
    12: ("dfbbbfd1-a918-5fcc-87d8-82738ce676cf", "Yukio Tashiro"),
    13: ("4b1ae1aa-6a3e-5488-92d2-413e9ee234c3", "Milton V Tassi"),
    14: ("1db40257-5dad-5045-a40a-a82ed477a3bf", "Gloria P Tassin"),
    15: ("a52e7b76-189c-5a38-a441-de5a0e856b8a", "Ennio Tassinari"),
    16: ("d072f639-f9d3-5fb9-bb0b-fe38d39c295d", "Richard M Tasso"),
    17: ("73fd75bd-2d47-50a6-938b-485e9f221a78", "Oliver Tassotti"),
    18: ("fca8f7fa-627c-519c-ac48-9cefd40458b8", "Rudolf Tate"),
    19: ("7abf6438-df33-506d-a62d-c8182ab24aff", "Solon H Tate"),
    20: ("363d610c-6a82-5a1f-93a5-52070598fdad", "Solon H Tate"),
    21: ("3853b443-67c5-570c-bcf0-f2f086aedb71", "Alice Tatham"),
    22: ("c199732a-da53-5b1e-a740-895d6de73ba1", "Eddison C Tatham"),
    23: ("18db0105-4a8b-59d3-9b1e-a1425b21307e", "Jack H Tattersall"),
}


ARMY_OCCUPATIONS = [
    {"row": 5, "date": "1943-07-13", "code": "736", "occupation": "Chauffeurs and drivers, bus, taxi, truck, and tractor", "locator": "PDF physical page 174; historical category 7-36"},
    {"row": 10, "date": "1942-09-03", "code": "497", "occupation": "Electricians", "locator": "PDF physical page 174; historical category 4-97"},
    {"row": 12, "date": "1942-01-27", "code": "004", "occupation": "Artists, sculptors, and teachers of art", "locator": "PDF physical page 170; historical category 0-04", "variant": "Yudio Tashiro"},
    {"row": 13, "date": "1943-05-11", "code": "788", "occupation": "Warehousing, storekeeping, handling, loading, unloading, and related occupations", "locator": "PDF physical page 175; historical category 7-88"},
    {"row": 17, "date": "1942-04-01", "code": "721", "occupation": "Miners and mining-machine operators", "locator": "PDF physical page 174; historical category 7-21"},
    {"row": 18, "date": "1941-09-24", "code": "227", "occupation": "Waiters and waitresses, except private family", "locator": "PDF physical page 172; historical category 2-27", "variant": "Rudolph Tate"},
    {"row": 20, "date": "1940-10-01", "code": "175", "occupation": "Salespersons", "locator": "PDF physical page 171; historical category 1-75"},
    {"row": 23, "date": "1942-11-27", "code": "050", "occupation": "Laboratory technicians and assistants", "locator": "PDF physical page 171; historical category 0-50"},
]


UNRESOLVED = {
    1: "The protected identifier did not produce a defensible reviewed Army bridge, and exact-name OSS, employer, occupation and archival searches did not establish a dated pre-OSS affiliation.",
    2: "A distinctive-name enlistment lead lacks a protected identifier or direct Box 765 bridge and was not assigned to the indexed person.",
    6: "The visually verified source prints Louis Tarnrinn; exact-name and likely spelling-variant searches produced no defensible identity bridge.",
    7: "A school-yearbook namesake and other search leads lack an OSS, protected-identifier or Box-file bridge and were not assigned.",
    8: "Multiple Frank Tartaro namesakes could not be distinguished by OSS, military, obituary, occupation or institutional evidence.",
    9: "Exact-name and middle-initial OSS, employer, occupation, obituary and institutional searches produced no defensible identity bridge.",
    11: "Exact-name OSS, employer, occupation, obituary, directory and archival searches produced no dated person-specific bridge.",
    14: "Exact-name and likely spelling-variant searches produced no reliable identity, occupation or employer source.",
    16: "A naval-officer cemetery lead lacks the identifiers needed to connect it to the indexed Richard M. Tasso and was not assigned.",
    21: "Vital-record and genealogy leads lacked documentary OSS or Box-file evidence and were not used as identity or employment sources.",
    22: "Vital-record and genealogy leads lacked documentary OSS or Box-file evidence and were not used as identity or employment sources.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 765-766",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 461, rows 1-23; checked against layout-preserving text and a 300 dpi page render",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. Full protected identifiers remain private. Bernard Tatz on page 461 row 24 was checked as the next boundary.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; eight reviewed Batch 941 identity bridges; protected identifiers withheld",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "No raw bulk row or full protected identifier is retained in public assets. Coded occupations identify no employer or workplace.",
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
            "locator": "PDF physical pages 170-175; historical categories 0-04, 0-50, 1-75, 2-27, 4-97, 7-21, 7-36 and 7-88",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical occupation labels identify neither employers nor workplaces.",
        },
        {
            "key": TARGAKIS,
            "stable_url": "https://www.elia.org.gr/userfiles/pdf_archieve/1944%206-144%20Corfu%2C%20OSS%20Missions%2C%20Gorgon%2C%20Molossos%2C%20EAM-ELAS%2C%20EDES%2C%20Food%20Shortages%2C%20%5B17%20pgs%5D%20226-210-WN9123%20%28Admin%29.pdf",
            "archival_identifier": "RG 226, Entry 210, WN9123 (Admin)",
            "title": "Progress Report of Greek Desk, 1-15 October 1944",
            "author_creator": "James H. Oliver, Head of Greek Desk, Company B, 2677th Regiment OSS (Provisional)",
            "repository_publisher": "Hellenic Literary and Historical Archive (ELIA-MIET)",
            "publication_record_date": "1944-10-15",
            "locator": "PDF physical page 16; Gorgon Mission report names T/4 Sgt. John Targakis",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "Office of Strategic Services records concerning Greece",
            "rights_notes": "The original wartime report page was rendered and visually inspected. It cannot determine which of two identical index rows represents the named person.",
        },
        {
            "key": TATE_OSS,
            "stable_url": "https://www.cia.gov/readingroom/docs/BISHOP%2C%20ROBERT_0060.pdf",
            "archival_identifier": "CIA FOIA OSS Collection, BISHOP, ROBERT_0060",
            "title": "Assignment of Qualified Personnel to OSS-ME Parachute Unit",
            "author_creator": "Office of Strategic Services, U.S. Army Forces in the Middle East",
            "repository_publisher": "Central Intelligence Agency Freedom of Information Act Electronic Reading Room",
            "publication_record_date": "1944-07-01",
            "locator": "PDF page 1; M Sgt. Solon H. Tate, SI branch, parachute training completed 5 April 1944; protected identifier withheld",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "OSS Collection",
            "rights_notes": "The Reading Room's indexed document text was inspected in context. The exact protected identifier is used privately to distinguish the second index row and is excluded from public project data.",
        },
        {
            "key": TASSINARI_ANPI,
            "stable_url": "https://www.anpimodena.it/wp-content/uploads/2015/02/2012-dicembre.pdf",
            "title": "La guerra sulla pelle: Libro intervista a Ennio Tassinari, agente dell'ORI",
            "repository_publisher": "ANPI Provinciale di Modena, Resistenza & Antifascismo Oggi",
            "publication_record_date": "2012-12",
            "locator": "PDF physical page 14; printed page 14",
            "access_date": "2026-10-28",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Resistenza & Antifascismo Oggi, anno XXIII, n. 5",
            "rights_notes": "The full page was rendered and visually inspected; only project-authored paraphrases and a minimal excerpt are retained.",
        },
        {
            "key": TASSINARI_SIUSA,
            "stable_url": "https://siusa-archivi.cultura.gov.it/cgi-bin/siusa/pagina.pl?Chiave=600526&TipoPag=comparc",
            "archival_identifier": "SIUSA complex fonds key 600526",
            "title": "Organizzazione della Resistenza italiana - ORI. Radio Zella",
            "author_creator": "Sistema Informativo Unificato per le Soprintendenze Archivistiche",
            "repository_publisher": "Ministero della Cultura, Direzione generale Archivi",
            "locator": "Fonds history; Ennio Tassinari's 1989 donation and ORI relations with the American OSS",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "Archivi storici in Emilia-Romagna",
            "rights_notes": "Official archival finding-aid context corroborates the person and organization; the ANPI chronology supports the transition claim.",
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
            "normalization_notes": "Existing canonical organization reused.",
        },
        {
            "key": ORI,
            "canonical_name": "Organizzazione della Resistenza Italiana",
            "historical_name": "Organizzazione Resistenza Italiana (ORI)",
            "aliases": ["ORI", "Organizzazione per la Resistenza Italiana"],
            "organization_type": "Italian resistance and Allied liaison organization",
            "sector": "unknown",
            "country": "Italy",
            "active_dates": "1943-1945",
            "normalization_notes": "The historical organization remains separate from OSS; sources describe ORI as later incorporated into or placed within OSS.",
        },
    ]


def army_affiliation(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    return {
        "key": f"{slug(PEOPLE[row][1])}-occupation-b941",
        "person_id": PEOPLE[row][0],
        "occupation": item["occupation"],
        "relationship_type": "employment",
        "end_date": item["date"],
        "date_precision": f"Historical civilian-occupation code {item['code']} was recorded at Army entry on {item['date']}; no employer or OSS-transfer date is named.",
        "country": "United States",
        "immediate_pre_oss": False,
        "last_civilian_pre_service": False,
        "pre_oss_temporal_basis": "strongly_date_bounded",
        "identity_confidence": "confirmed" if row == 20 else "high_confidence",
        "claim_confidence": "medium",
        "source_quality": "A_direct_official",
        "publication_status": "publish_qualified",
        "research_notes": "The historical category is not converted into a named employer, workplace or exact job title.",
    }


def substantive_affiliations() -> list[dict[str, object]]:
    return [
        {
            "key": "ennio-tassinari-ori-b941",
            "person_id": PEOPLE[15][0],
            "organization_key": ORI,
            "organization_name_as_found": "ORI, Organizzazione Resistenza Italiana",
            "role_title": "ORI agent and participant in the organization's formation",
            "occupation": "resistance liaison and field agent",
            "relationship_type": "volunteer",
            "start_date": "1943-09",
            "end_date": "1944-03",
            "date_precision": "The institutional account dates Tassinari's arrival among the Allies and participation in ORI's formation after 8 September 1943, followed by OSS training and a March 1944 mission.",
            "city": "Naples and Pozzuoli",
            "country": "Italy",
            "immediate_pre_oss": True,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "explicit_immediate",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "published",
            "research_notes": "ORI is an institutional and resistance affiliation, not a civilian employer. The source explicitly states that ORI was later incorporated into OSS.",
        },
        {
            "key": "solon-h-tate-us-army-b941",
            "person_id": PEOPLE[20][0],
            "organization_key": US_ARMY,
            "organization_name_as_found": "U.S. Army Forces in the Middle East",
            "role_title": "Master sergeant, SI branch; OSS-ME Parachute Unit",
            "occupation": "Army enlisted service",
            "relationship_type": "military_assignment",
            "start_date": "1940-10-01",
            "end_date": "1944-07-01",
            "date_precision": "The Army record dates entry; the direct OSS-ME order of 1 July 1944 places the same identified soldier on parachute duty with the OSS-ME unit.",
            "city": "Cairo",
            "country": "Egypt",
            "immediate_pre_oss": True,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "confirmed",
            "claim_confidence": "high",
            "source_quality": "A_direct_official",
            "publication_status": "published",
            "research_notes": "Modeled as the best-supported Army-to-OSS military pathway, not as civilian employment. The separately indexed Solon H. Tate row has a different protected identifier and receives no copied claim.",
        },
    ]


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
    result: dict[str, object] = {
        "key": key,
        "person_id": PEOPLE[row][0],
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
    if affiliation_key:
        result["affiliation_key"] = affiliation_key
    return result


def army_identity_claim(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    name = PEOPLE[row][1]
    confirmed = row == 20
    variant = item.get("variant")
    direct = []
    if confirmed:
        direct.append({"source_key": TATE_OSS, "locator_override": "PDF page 1; exact name and protected identifier; identifier withheld", "excerpt_override": "M Sgt Solon H Tate"})
    return claim(
        row,
        f"identity-{slug(name)}-b941",
        "identity",
        f"The indexed {name} row is a {'confirmed' if confirmed else 'high-confidence'} match to the reviewed official Army record.",
        "A nonshared protected identifier connects the visually verified index row to the official Army record" + (" and a direct OSS-ME order" if confirmed else "") + ".",
        ("Confirmed by exact name and protected identifier in two independent official records." if confirmed else "High confidence from the protected-identifier bridge and " + ("a close documented name variant." if variant else "exact full-name agreement.")),
        "The Army record supports identity and a dated occupation category; the OSS transfer sequence is established only for the second Solon H. Tate row.",
        "A_direct_official",
        "confirmed" if confirmed else "high",
        [
            {"source_key": INDEX, "locator_override": f"PDF page 461 row {row}; protected identifier withheld"},
            {"source_key": ARMY, "locator_override": "Accepted reviewed identity bridge; protected identifier withheld"},
            *direct,
        ],
        "No protected identifier is exposed, and no employer or workplace is inferred from the identity bridge.",
    )


def army_occupation_claim(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    name = PEOPLE[row][1]
    key = f"{slug(name)}-occupation-b941"
    return claim(
        row,
        f"occupation-{slug(name)}-b941",
        "occupation",
        f"At Army entry on {item['date']}, {name} was recorded in the historical {str(item['occupation']).lower()} category; no employer is identified.",
        f"The accepted Army record carries civilian-occupation code {item['code']}, decoded from NARA's official code list.",
        "The occupation belongs only to the reviewed protected-identifier match; the identifier itself is not public.",
        "Strongly date-bounded to Army entry; it does not establish the immediate pre-OSS affiliation or a named employer.",
        "A_direct_official",
        "medium",
        [
            {"source_key": ARMY, "locator_override": f"Accepted reviewed identity record; civilian occupation code {item['code']}; protected identifier withheld"},
            {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46; Army-entry-date and civilian-occupation fields"},
            {"source_key": CODES, "locator_override": item["locator"], "excerpt_override": item["occupation"]},
        ],
        "The historical category remains a qualified occupation lead, not an employer, workplace, institution or exact title.",
        key,
    )


def substantive_claims() -> list[dict[str, object]]:
    claims: list[dict[str, object]] = []
    for row in (3, 4):
        claims.append(
            claim(
                row,
                f"conflict-john-targakis-row{row}-b941",
                "identity",
                "A direct OSS Greek Desk report names T/4 Sgt. John Targakis, but the index contains two identical John Targakis rows and the report cannot select between them.",
                "The October 1944 report places John Targakis with the Gorgon Mission and describes his Corfu liaison work.",
                "Ambiguous because both Box 766 index rows carry the same printed name and no distinguishing identifier.",
                "The report is contemporaneous OSS evidence but does not establish a pre-OSS affiliation or resolve the duplicate rows.",
                "A_direct_official",
                "conflicting",
                [
                    {"source_key": INDEX, "locator_override": f"PDF page 461 row {row}; one of two identical printed rows"},
                    {"source_key": TARGAKIS, "locator_override": "PDF physical page 16", "excerpt_override": "T/4 Sgt. John Targakis"},
                ],
                "Both source rows remain separate in one possible-duplicate group pending joint Box 766 review. No mission evidence is copied as a settled identity or pre-OSS affiliation.",
                publication_status="conflicting",
            )
        )
    claims.extend(
        [
            claim(
                15,
                "identity-ennio-tassinari-b941",
                "identity",
                "Indexed Ennio Tassinari is a high-confidence match to the Italian ORI/OSS resistance agent documented by ANPI and Italy's official archival information system.",
                "The distinctive exact name, Italian-citizen index note, wartime chronology and official ORI fonds description align.",
                "High confidence from a distinctive exact name and mutually reinforcing institutional and official archival evidence.",
                "The sources date his antifascist activity, ORI formation, OSS training and first mission from 1940 through March 1944.",
                "A_direct_official",
                "high",
                [
                    {"source_key": INDEX, "locator_override": "PDF page 461 row 15; note preserved as printed: Italian Ci"},
                    {"source_key": TASSINARI_ANPI, "locator_override": "PDF physical page 14"},
                    {"source_key": TASSINARI_SIUSA, "locator_override": "Fonds history and 1989 Tassinari donation"},
                ],
                "The index wording remains unchanged; foreign-national status and ORI affiliation do not imply commissioned-officer status.",
            ),
            claim(
                15,
                "immediate-ennio-tassinari-ori-b941",
                "immediate_pre_oss_affiliation",
                "The Organizzazione della Resistenza Italiana (ORI) is Ennio Tassinari's documented immediate institutional pathway into OSS training and service.",
                "ANPI states that he helped form ORI after reaching the Allies in Naples and that ORI was later placed within OSS.",
                "High-confidence identity from the distinctive exact name and official archival corroboration.",
                "Explicit immediate sequence from ORI formation to OSS incorporation, training at Pozzuoli and a March 1944 mission.",
                "B_authoritative_institutional",
                "high",
                [
                    {"source_key": TASSINARI_ANPI, "locator_override": "PDF physical page 14", "excerpt_override": "partecipa alla costituzione dell’ORI ... che verrà poi inquadrata nell’Oss"},
                    {"source_key": TASSINARI_SIUSA, "support_type": "context_only", "locator_override": "ORI Radio Zella fonds history"},
                ],
                "Modeled as a resistance/institutional affiliation, not a civilian employer.",
                "ennio-tassinari-ori-b941",
            ),
            claim(
                20,
                "immediate-solon-h-tate-army-b941",
                "immediate_pre_oss_affiliation",
                "The United States Army is the second Solon H. Tate row's best-supported immediate military pathway into an OSS-ME parachute assignment.",
                "The Army record dates entry, and a direct OSS-ME order places the same identified master sergeant on parachute duty with the unit.",
                "Confirmed by exact name and the same nonshared protected identifier in the index, Army record and direct OSS order.",
                "Strongly date-bounded Army-to-OSS-ME pathway; the sources do not identify a separate civilian affiliation immediately before OSS.",
                "A_direct_official",
                "high",
                [
                    {"source_key": ARMY, "locator_override": "Accepted reviewed identity and Army-entry record; protected identifier withheld"},
                    {"source_key": TATE_OSS, "locator_override": "PDF page 1; 1 July 1944 order; protected identifier withheld", "excerpt_override": "M Sgt Solon H Tate"},
                ],
                "The affiliation is military, not civilian employment. The separately printed Solon H. Tate row has a different protected identifier and receives no copied claim.",
                "solon-h-tate-us-army-b941",
            ),
        ]
    )
    return claims


def archival_update(row: int, reason: str) -> dict[str, object]:
    person_id, name = PEOPLE[row]
    box = "765" if row <= 2 else "766"
    return {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, Box {box} and archive location 230/86/41/07. {reason}",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": f"Review Box {box} for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }


def person_updates() -> list[dict[str, object]]:
    updates = [archival_update(row, reason) for row, reason in UNRESOLVED.items()]
    targakis_group = "possible-duplicate:john-targakis-page461-rows3-4"
    for row in (3, 4):
        updates.append(
            {
                "person_id": PEOPLE[row][0],
                "identity_status": "ambiguous",
                "identity_evidence": "A direct October 1944 OSS Greek Desk report names T/4 Sgt. John Targakis, but the index prints two identical John Targakis rows in Box 766 and provides no distinguishing identifier.",
                "manual_review_required": True,
                "possible_duplicate_group": targakis_group,
                "research_status": "conflicting_sources",
                "next_action": "Review both John Targakis files in Box 766 together. Keep the rows separate unless direct evidence establishes duplication or identifies which file belongs to the Gorgon Mission sergeant.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            }
        )
    for item in ARMY_OCCUPATIONS:
        row = int(item["row"])
        variant = item.get("variant")
        update: dict[str, object] = {
            "person_id": PEOPLE[row][0],
            "identity_status": "confirmed" if row == 20 else "high_confidence",
            "identity_evidence": ("The exact name and same nonshared protected identifier align across the index, official Army bulk file and a direct OSS-ME order." if row == 20 else "A nonshared protected identifier connects the visually verified index row to the reviewed official Army record. " + (f"The Army spelling {variant} is retained as a documented variant." if variant else "The full name agrees exactly.")),
            "personnel_category": "enlisted_army_personnel",
            "commissioned_officer": False,
            "allied_or_foreign_personnel": False,
            "manual_review_required": True,
            "research_status": "completed" if row == 20 else "occupation_only_found",
            "next_action": ("Review both Solon H. Tate files in Box 766 together and inspect the confirmed row for the last civilian employer and exact Army-to-OSS administrative sequence." if row == 20 else "Review Box 766 to identify the immediate pre-OSS affiliation and last civilian employer; do not convert the Army category into a named employer or institution."),
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
            "archival_review_priority": "critical" if row == 20 else "high",
        }
        if variant:
            update["name_variants"] = [variant]
        if row == 20:
            update["possible_duplicate_group"] = "different-identifiers:solon-h-tate-page461-rows19-20"
        updates.append(update)
    updates.extend(
        [
            {
                "person_id": PEOPLE[15][0],
                "identity_status": "high_confidence",
                "identity_evidence": "The distinctive exact name, the index's Italian-citizen note, an institutional wartime chronology and the official ORI archival finding aid align.",
                "personnel_category": "temporary_contract_or_special_personnel",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": True,
                "manual_review_required": True,
                "research_status": "completed",
                "next_action": "Review Box 766 for the administrative terms of Tassinari's OSS service and any civilian employment immediately before his 1940 underground activity; preserve ORI as an affiliation, not an employer.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "medium",
            },
            {
                "person_id": PEOPLE[19][0],
                "identity_status": "ambiguous",
                "identity_evidence": "The index prints a second Solon H. Tate with a different protected identifier. Official Army and OSS-ME evidence matches row 20's identifier, so no claim is transferred to this row.",
                "manual_review_required": True,
                "possible_duplicate_group": "different-identifiers:solon-h-tate-page461-rows19-20",
                "research_status": "conflicting_sources",
                "next_action": "Review both Solon H. Tate files in Box 766 together. Preserve the separate identifiers and people unless direct file evidence proves duplication.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
        ]
    )
    return updates


def research_attempts() -> list[dict[str, object]]:
    army_rows = {int(item["row"]) for item in ARMY_OCCUPATIONS}
    attempts: list[dict[str, object]] = []
    for row in sorted(PEOPLE):
        person_id, name = PEOPLE[row]
        if row in UNRESOLVED:
            outcome, reviewed, rejected, detail = "no_result", 7, 5, UNRESOLVED[row]
        elif row in (3, 4):
            outcome, reviewed, rejected, detail = "candidate_found", 9, 4, "A direct OSS Greek Desk report names John Targakis but cannot distinguish the two identical Box 766 rows; both remain separate and conflicting."
        elif row == 15:
            outcome, reviewed, rejected, detail = "source_reviewed", 10, 4, "Institutional and official archival evidence supports a high-confidence ORI-to-OSS pathway without recasting ORI as civilian employment."
        elif row == 19:
            outcome, reviewed, rejected, detail = "candidate_found", 8, 4, "The official Army and OSS-ME bridge belongs to the separately indexed Solon H. Tate row with a different protected identifier; no claim was transferred."
        elif row == 20:
            outcome, reviewed, rejected, detail = "source_reviewed", 10, 3, "Official Army and OSS-ME evidence confirms this specific row and supports a military Army-to-OSS pathway plus a dated occupation category."
        elif row in army_rows:
            outcome, reviewed, rejected, detail = "source_reviewed", 8, 4, "An accepted protected-identifier Army bridge supports identity and a dated historical occupation category, not an employer."
        else:
            raise AssertionError(f"Missing Batch 941 outcome for row {row}")
        attempts.append(
            {
                "key": f"page461-row{row}-{slug(name)}-b941",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA index and public Archives context; CIA Reading Room and exact-name discovery; OSS, rank and spelling variants; employer and occupation 1940; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Boxes 765-766; protected identifiers used privately only when defensible",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_941",
                "started_at": "2026-10-28T08:30:00Z",
                "completed_at": "2026-10-28T11:15:00Z",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search snippets, family-tree assertions, modern people-finder pages, postwar-only leads and sources without an OSS, protected-identifier or Box-file bridge were not assigned.",
                "research_notes": f"{detail} The index page and admitted PDF pages were visually checked. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": "Review the indexed personnel file for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before military service.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b941-v1",
            }
        )
    return attempts


def main() -> None:
    affiliations = [army_affiliation(item) for item in ARMY_OCCUPATIONS]
    affiliations += substantive_affiliations()
    claims = [army_identity_claim(item) for item in ARMY_OCCUPATIONS]
    claims += [army_occupation_claim(item) for item in ARMY_OCCUPATIONS]
    claims += substantive_claims()
    bundle = {
        "bundle_version": "batch-941-v1",
        "reviewer": "Before OSS Batch 941 evidence review",
        "sources": sources(),
        "organizations": organizations(),
        "affiliations": affiliations,
        "claims": claims,
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }
    EvidenceBundle.model_validate(bundle)
    OUTPUT.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
