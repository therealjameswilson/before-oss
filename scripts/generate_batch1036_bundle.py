#!/usr/bin/env python3
"""Generate the reviewed Batch 1036 evidence bundle for PDF page 291."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page291-sylvester-maiza-to-william-j-malone-review_"
    "batch-1036_2026-11-04.json"
)

INDEX = "nara-index-b1036"
ARMY = "army-bulk-b1036"
TECH = "army-tech-b1036"
CODES = "army-codes-b1036"
MALENBAUM_CR = "congressional-record-malenbaum-b1036"
MALENBAUM_HARVARD = "harvard-crimson-malenbaum-b1036"
MAKRIS_ROSTER = "oss-greek-og-makris-b1036"
MALFETTES_HISTORY = "infiltrations-france-malfettes-b1036"

ORG_OPA = "opa-b1036"
ORG_HARVARD = "harvard-b1036"


PEOPLE = {
    1: ("371b5cab-9753-52ef-8cc7-a84b8660853f", "Sylvester Maiza", "476"),
    2: ("72814464-7e22-50a7-93ef-6d31a56597bd", "Lillian Majar", "476"),
    3: ("81295f7f-9ff4-5ca0-ab7d-5c75ebcacd42", "Robert Major", "476"),
    4: ("8a1107de-5180-5d37-b7cb-265d9f3fd7a2", "Sarah Majors", "476"),
    5: ("847ceb18-40df-5905-b976-c9870688169a", "Thomas B Majure", "476"),
    6: ("1585a5b0-ac2f-5d96-b31c-73de8d94b1ca", "Paul Makanowitzky", "476"),
    7: ("fdf243b2-fe0a-59c1-a634-c3d1c63b4ab0", "George S Makepeace", "476"),
    8: ("d945d0d2-91b0-5c58-b940-5167da988687", "Tovivo Maki", "476"),
    9: ("807b04ee-0902-5561-8d81-f852ac02f8b3", "Gene Mako", "476"),
    10: ("f8b31500-28c6-5a2b-b839-6d808405d511", "Lambros G Makris", "476"),
    11: ("3315b0d4-1548-5977-a632-8e623693c9e4", "Antonio A Malakis", "476"),
    12: ("1669aff3-3883-5ee9-b26b-e7786262cc8a", "Clarence J Malakowsky", "476"),
    13: ("8f06bce3-98b1-50ed-9374-ba87c380aec9", "John Malandre", "476"),
    14: ("8d02c26f-1085-5787-9e03-309395bb1414", "John Malanore", "476"),
    15: ("aa8aca81-09fa-55ba-a35b-d02680076044", "Victor Malaspina", "476"),
    16: ("4c4fbefa-3115-57ea-bdc7-15aaf59fff5c", "Frank Malavask Jr.", "476"),
    17: ("5cb03613-df14-5b2c-8849-2e9ae2fcb4a4", "Hanson J Malbrough", "476"),
    18: ("1410b512-4857-595a-934c-0c9aa61e6993", "Edward V Malcom", "476"),
    19: ("892d0768-822a-5d99-8ae9-f67429730287", "Raymund S Malec", "477"),
    20: ("c075d283-bef5-5c80-a499-e8ae353455e0", "Wilfred Malenbaum", "477"),
    21: ("a76d70f9-a63b-5e3a-bdfd-d86b0e2dbe90", "Alexander B Maley", "477"),
    22: ("faee7841-6790-53dc-9b93-262fe20be144", "Maxime Malfettes", "477"),
    23: ("32a41d50-11f3-5222-82a4-547e848f29d5", "John F Malia", "477"),
    24: ("cc301165-edd8-5b23-9cc3-79842f6492a2", "Wilson B Malick", "477"),
    25: ("8ba2be90-7d3d-5e8f-a50f-02e96c93c1ac", "Edith Malinofsky", "477"),
    26: ("c99f9b22-6c95-5b97-9570-18b0e3a6a95f", "Victor Malispino", "477"),
    27: ("ab42783f-5c5c-5aef-b80e-75cdd4083363", "Louis T Malizia Jr.", "477"),
    28: ("8da5b625-0784-5c9d-a756-f39887196e3b", "Martin L Malkin", "477"),
    29: ("9b0d2874-1cea-5438-9407-68df938ca238", "Julius B Maller", "477"),
    30: ("17814442-286b-58a5-9920-d4718da57410", "Harry S Mallon", "477"),
    31: ("3489a66a-3e09-5b5e-8aba-fec001b9bd75", "Barbara S Mallory", "477"),
    32: ("55b487ee-6a40-58c1-9408-c60cbb6b96a4", "Hal N Mallory", "477"),
    33: ("d7693575-ea82-52a6-858a-63baf05ac5f0", "Jasper T Mallory", "477"),
    34: ("418500f7-93a8-5ff2-8bc0-087d9396bdf2", "Lloyd A Mallory", "477"),
    35: ("8326f585-6b57-53b5-bee7-acb760b305ed", "John W Malloy", "477"),
    36: ("4b32f0b8-d82d-5fa9-bf72-b88c39ee77ba", "Valeria Mally", "477"),
    37: ("d0beb127-df61-5886-91a3-53cc506b2075", "Harold N Malmin", "477"),
    38: ("abccd8f0-91f4-56d6-bfb8-267026bce6d2", "Patricia C Malmsted", "477"),
    39: ("13077851-f1d4-5607-b882-418038025305", "Patricia C Malmstedt", "477"),
    40: ("658b52c4-3150-5edf-95d1-ed09d54845ae", "Philip J Malmstedt", "477"),
    41: ("7113b95a-11f2-5c41-845c-d4898a48c124", "Ethel M Malone", "477"),
    42: ("3b621093-42ff-560c-be18-66ea99a3c342", "J D Malone", "477"),
    43: ("ba2d8b5a-f2fb-5b18-a1d3-f7e44bce0c86", "John F Malone", "477"),
    44: ("6c7964f4-a075-5be2-a9e2-57fa0ac70a32", "Merrill E Malone", "478"),
    45: ("54ad3523-641d-56d8-89f8-ee63d30ea3e0", "William E Malone Jr.", "478"),
    46: ("12704c00-5626-5ae7-8142-e7f3fcbc7d44", "William J Malone", "478"),
}

# A protected linkage was explicitly reviewed for every row here. Rows 8 and
# 12 are identity-only: the former is dated too late to use as pre-OSS evidence,
# and the latter carries undefined occupation code 999.
ARMY_ASSOCIATIONS = {
    1: ("1942-03-02", "770", "fireman other than a process fireman", "Firemen, other than process firemen", "unknown", "PDF physical page 174; historical category 7-70"),
    6: ("1942-08-24", "024", "musician or teacher of music", "Musicians and teachers of music", "unknown", "PDF physical page 171; historical category 0-24"),
    7: ("1942-10-14", "112", "clerk in trade, not elsewhere classified", "Clerks in trade, n.e.c.", "unknown", "PDF physical page 171; historical category 1-12"),
    11: ("1942-11-07", "229", "kitchen worker in a hotel, restaurant, railroad, steamship, or related establishment", "Kitchen workers in hotels, restaurants, railroads, steamships, etc., n.e.c.", "unknown", "PDF physical page 172; historical category 2-29"),
    15: ("1942-01-16", "227", "waiter or waitress outside private-family service", "Waiters and waitresses, except private family", "unknown", "PDF physical page 172; historical category 2-27"),
    23: ("1943-03-06", "002", "actor or actress", "Actors and actresses", "unknown", "PDF physical page 175; alphabetical category 0-02"),
    24: ("1942-09-25", "530", "steam fitter, gas fitter, or plumber", "Plumbers, gas fitters, and steam fitters", "unknown", "PDF physical page 174; historical category 5-30"),
    27: ("1943-03-06", "170", "sales clerk", "Sales clerks", "unknown", "PDF physical page 171; historical category 1-70"),
    30: ("1942-11-17", "781", "motor-vehicle mechanic or repairman", "Mechanics and repairmen, motor vehicle", "unknown", "PDF physical page 175; historical category 7-81"),
    32: ("1943-05-06", "992", "student", "Students", "student", "PDF physical page 304; corrected historical category 9-92"),
    34: ("1942-11-05", "101", "bookkeeper or cashier outside bank cashiering", "Bookkeepers and cashiers, except bank cashiers", "unknown", "PDF physical page 171; historical category 1-01"),
    40: ("1941-06-21", "101", "bookkeeper or cashier outside bank cashiering", "Bookkeepers and cashiers, except bank cashiers", "unknown", "PDF physical page 171; historical category 1-01"),
    43: ("1942-10-28", "781", "motor-vehicle mechanic or repairman", "Mechanics and repairmen, motor vehicle", "unknown", "PDF physical page 175; historical category 7-81"),
    44: ("1943-07-01", "240", "recreation or amusement attendant, not elsewhere classified", "Attendants, recreation and amusement, n.e.c.", "unknown", "PDF physical page 172; historical category 2-40"),
    46: ("1942-07-13", "137", "stenographer or typist", "Stenographers and typists", "unknown", "PDF physical page 171; historical category 1-37"),
}

ARMY_IDENTITY_ONLY = {
    8: ("1945-06-16", "The late-war Army entry and student code are not used as pre-OSS evidence."),
    12: ("1943-06-09", "Occupation code 999 is undefined and is not interpreted."),
}

VARIANT_ROWS = {6, 8, 23, 32, 44}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def source(key: str, **kwargs: object) -> dict[str, object]:
    value: dict[str, object] = {"key": key, "access_date": "2026-11-04"}
    value.update(kwargs)
    return value


def sources() -> list[dict[str, object]]:
    return [
        source(
            INDEX,
            stable_url="https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            archival_identifier="RG 226, Entry A1-224, Boxes 476-478",
            title="OSS Personnel Files from Excel",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="2010-12-23",
            locator="PDF page 291, rows 1-46; page and every printed row visually checked at 180 dpi",
            source_quality="A_direct_official",
            collection_name="Records of the Office of Strategic Services, Record Group 226",
            rights_notes="All 46 printed rows remain separate. Full protected identifiers remain private, including the malformed John W. Malloy value.",
        ),
        source(
            ARMY,
            stable_url="https://catalog.archives.gov/id/1263923",
            archival_identifier="National Archives Identifier 1263923; parent series NAID 604357",
            title="Electronic Army Serial Number Merged File, ca. 1938-1946",
            author_creator="Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="1938-1946; merged file created 2002",
            locator="Official unrestricted ASNEF.FIN.DAT; eighteen Batch 1036 identity candidates explicitly reviewed; seventeen accepted and one rejected",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records",
            document_number="ASNEF.FIN.DAT",
            rights_notes="No raw record, full protected identifier, or bulk-record ordinal is retained in public assets.",
        ),
        source(
            TECH,
            stable_url="https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf",
            archival_identifier="NN3-064-03-008; National Archives Identifier 1263923",
            title="World War II Army Enlistment Records: Reference Copy of Technical Documentation",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives at College Park - Electronic Records",
            publication_record_date="1994-2005; reference copy modified 2011",
            locator="PDF physical pages 44-46; identifier, name, Army-entry-date, grade and civilian-occupation fields",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records technical documentation",
            rights_notes="Used to interpret selected fields only; source damage, coding limits, and incomplete coverage remain applicable.",
        ),
        source(
            CODES,
            stable_url="https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1CL_SD.pdf",
            archival_identifier="National Archives Identifier 1263923; Code No. 30",
            title="NARA Compiled Code Lists for the Electronic Army Serial Number Merged File",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives at College Park - Electronic Records",
            publication_record_date="2011-01-12; modified 2011-03-17",
            locator="PDF physical pages 171-175 and 304; all fifteen published Batch 1036 categories visually checked",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records technical documentation",
            rights_notes="Historical categories identify neither employer, institution, workplace, nor exact Army-to-OSS sequence. Undefined code 999 is not interpreted.",
        ),
        source(
            MALENBAUM_CR,
            stable_url="https://www.govinfo.gov/content/pkg/GPO-CRECB-1948-pt2/pdf/GPO-CRECB-1948-pt2-16.pdf",
            archival_identifier="Congressional Record, Senate, March 12, 1948, printed page 2661",
            title="Congressional Record—Senate",
            author_creator="United States Congress",
            repository_publisher="U.S. Government Publishing Office",
            publication_record_date="1948-03-12",
            locator="Printed page 2661; PDF physical page 54; Wilfred Malenbaum entry visually and textually checked",
            source_quality="A_direct_official",
            collection_name="Congressional Record",
            rights_notes="The official chronology places OPA in 1941 immediately before OSS service dated 1941-1945, but supplies no exact transition month.",
        ),
        source(
            MALENBAUM_HARVARD,
            stable_url="https://www.thecrimson.com/article/1936/4/14/stoughton-awards-go-all-to-dorchester/",
            title="Stoughton Awards Go All to Dorchester Men",
            repository_publisher="The Harvard Crimson",
            publication_record_date="1936-04-14",
            locator="Scholarship announcement identifying Wilfred Malenbaum as a second-year graduate student in economics",
            source_quality="C_reputable_contemporary_or_scholarly",
            collection_name="The Harvard Crimson archive",
            rights_notes="The contemporary item supports student status, not employment by Harvard.",
        ),
        source(
            MAKRIS_ROSTER,
            stable_url="https://www.elia.org.gr/userfiles/pdf_archieve/1944%209-1544%20Date%20Estimated%2C%20OSS%20Missions%2C%20SOE%2C%20Train%20Sabotage%2C%20Katerini%2C%20Tsirmulas%2C%20226-99-45-5%20%28Admin%29.pdf",
            archival_identifier="RG 226-99-45-5 (Admin)",
            title="OSS Greek Operational Group personnel roster",
            author_creator="Office of Strategic Services",
            repository_publisher="Hellenic Literary and Historical Archive (ELIA-MIET)",
            publication_record_date="1944-09 (estimated by repository)",
            locator="PDF physical page 16, roster page 3; Lambros G. Makris entry visually and textually checked",
            source_quality="A_direct_official",
            collection_name="OSS Missions and SOE records",
            rights_notes="The public claim withholds the full identifier printed in the roster; it is used only to confirm identity and wartime OSS context.",
        ),
        source(
            MALFETTES_HISTORY,
            stable_url="https://www.resistance-brest.net/IMG/pdf/infiltrations_en_francedec2024.pdf",
            title="Historique 2ieme GM: Infiltrations en France, 1940-1945",
            author_creator="Pedro C. F. de Flers",
            repository_publisher="Resistance-Brest.net",
            publication_record_date="2024-12-31 revision",
            locator="PDF physical page 118; 27 January 1944 Mission Varlin row visually and textually checked",
            source_quality="C_reputable_contemporary_or_scholarly",
            collection_name="Historical table of agents infiltrated and exfiltrated in France",
            rights_notes="The compiled table cites British and French archival series. It supports a qualified identity and mission context, not pre-OSS employment.",
        ),
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": ORG_OPA,
            "organization_id": "22df26e9-7191-58a7-a228-6a6cc8dfa4f1",
            "canonical_name": "Office of Price Administration",
            "historical_name": "Office of Price Administration",
            "aliases": ["OPA"],
            "organization_type": "federal wartime agency",
            "sector": "federal_government",
            "city": "Washington",
            "state_or_region": "District of Columbia",
            "country": "United States",
            "active_dates": "1941-1947",
            "normalization_notes": "Existing canonical organization reused. Government service is modeled separately from private employment.",
        },
        {
            "key": ORG_HARVARD,
            "organization_id": "45ddf347-21c6-59f5-a8ae-517418adf941",
            "canonical_name": "Harvard University",
            "historical_name": "Harvard University",
            "aliases": ["Harvard"],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "Cambridge",
            "state_or_region": "Massachusetts",
            "country": "United States",
            "normalization_notes": "Student status and employment remain separate relationships.",
        },
    ]


def army_affiliation_key(row: int) -> str:
    return f"{slug(PEOPLE[row][1])}-army-association-b1036"


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, _label, relationship, _locator) in ARMY_ASSOCIATIONS.items():
        identity = "high_confidence" if row in VARIANT_ROWS else "confirmed"
        value: dict[str, object] = {
            "key": army_affiliation_key(row),
            "person_id": PEOPLE[row][0],
            "relationship_type": relationship,
            "end_date": date,
            "date_precision": f"Historical civilian-occupation code {code} was recorded at Army entry on {date}; no named employer, institution, or workplace is supplied.",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": identity,
            "claim_confidence": "medium",
            "source_quality": "A_direct_official",
            "publication_status": "publish_qualified",
            "research_notes": "The broad historical category is not converted into a named employer and is excluded from verified-employer analytics.",
        }
        if relationship == "student":
            value["role_title"] = "student"
        else:
            value["occupation"] = occupation
        values.append(value)
    values.extend(
        [
            {
                "key": "wilfred-malenbaum-opa-b1036",
                "person_id": PEOPLE[20][0],
                "organization_key": ORG_OPA,
                "organization_name_as_found": "OPA",
                "role_title": "economist",
                "occupation": "economist",
                "relationship_type": "government_assignment",
                "end_date": "1941",
                "date_precision": "The Congressional Record dates both OPA and the start of OSS service to 1941 but gives no month or exact transfer date.",
                "city": "Washington",
                "state_or_region": "District of Columbia",
                "country": "United States",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "probable_immediate",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "A_direct_official",
                "publication_status": "publish_qualified",
                "research_notes": "Best-supported immediate government affiliation. It is not labeled a private employer, and the exact 1941 transition remains unresolved.",
            },
            {
                "key": "wilfred-malenbaum-harvard-student-b1036",
                "person_id": PEOPLE[20][0],
                "organization_key": ORG_HARVARD,
                "organization_name_as_found": "Harvard",
                "role_title": "graduate student in economics",
                "occupation": "student",
                "relationship_type": "student",
                "date_precision": "A contemporary April 1936 notice identifies Malenbaum as a second-year graduate student in economics; it does not give the full enrollment span.",
                "city": "Cambridge",
                "state_or_region": "Massachusetts",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "published",
                "research_notes": "Student status is not employment. The OPA government assignment intervened before OSS service.",
            },
        ]
    )
    return values


def army_identity_assessment(row: int) -> str:
    assessments = {
        6: "High confidence from a nonshared protected linkage and the close Makanowitzky/Makanowitsky spelling variant; the identifier remains private.",
        8: "High confidence from a nonshared protected linkage despite the indexed Tovivo and Army Toivo W name difference; the identifier remains private.",
        23: "High confidence from a nonshared protected linkage despite the indexed F and Army J middle-initial conflict; the discrepancy remains visible.",
        32: "High confidence from a nonshared protected linkage and exact first and surname; the Army form omits the indexed middle initial N.",
        44: "High confidence from a nonshared protected linkage and the close Merrill/Morrill spelling variant; the identifier remains private.",
    }
    return assessments.get(
        row,
        "Confirmed by exact official name agreement and a nonshared protected linkage; the protected identifier remains private.",
    )


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, label, relationship, locator) in ARMY_ASSOCIATIONS.items():
        values.append(
            {
                "key": f"army-{slug(PEOPLE[row][1])}-b1036",
                "person_id": PEOPLE[row][0],
                "affiliation_key": army_affiliation_key(row),
                "claim_type": "other_pre_oss_affiliation" if relationship == "student" else "occupation",
                "claim_text": f"At Army entry on {date}, {PEOPLE[row][1]} was recorded as {occupation}; no employer, institution, or workplace is identified.",
                "evidence_paraphrase": f"The Army bulk file records code {code}, and the visually checked official code list defines the category as {label}.",
                "identity_match_assessment": army_identity_assessment(row),
                "temporal_assessment": "Strongly date-bounded to Army entry, but not proven to be the immediately preceding role or status before OSS.",
                "source_quality": "A_direct_official",
                "claim_confidence": "medium",
                "publication_status": "publish_qualified",
                "match_notes": "The historical category is qualified, excluded from verified-employer analytics, and not converted into a named organization.",
                "sources": [
                    {"source_key": INDEX},
                    {"source_key": ARMY},
                    {"source_key": TECH, "support_type": "context_only"},
                    {"source_key": CODES, "locator_override": locator},
                ],
            }
        )
    for row, (date, note) in ARMY_IDENTITY_ONLY.items():
        values.append(
            {
                "key": f"identity-{slug(PEOPLE[row][1])}-army-b1036",
                "person_id": PEOPLE[row][0],
                "claim_type": "identity",
                "claim_text": f"Indexed {PEOPLE[row][1]} is a reviewed match to the official Army record.",
                "evidence_paraphrase": "A nonshared protected linkage connects the official index and Army record; no full identifier or raw record is published.",
                "identity_match_assessment": army_identity_assessment(row),
                "temporal_assessment": f"Army entry is dated {date}. {note}",
                "source_quality": "A_direct_official",
                "claim_confidence": "high" if row == 8 else "confirmed",
                "publication_status": "published",
                "match_notes": "Identity evidence only; no undefined or chronologically unsafe occupation is converted into pre-OSS evidence.",
                "sources": [
                    {"source_key": INDEX},
                    {"source_key": ARMY},
                    {"source_key": TECH, "support_type": "context_only"},
                ],
            }
        )
    values.extend(
        [
            {
                "key": "identity-wilfred-malenbaum-b1036",
                "person_id": PEOPLE[20][0],
                "claim_type": "identity",
                "claim_text": "Indexed Wilfred Malenbaum is high-confidence identified as the economist who led the OSS Food and Agriculture Section.",
                "evidence_paraphrase": "The Congressional Record uses the exact uncommon name and gives a 1941-1945 OSS section-chief chronology compatible with the indexed civilian grade.",
                "identity_match_assessment": "High confidence from the rare exact name, matching civilian professional-grade context, and a direct official OSS chronology; Box 477 remains unreviewed.",
                "temporal_assessment": "The official entry explicitly dates OPA and OSS activity to 1941 and OSS service through 1945.",
                "source_quality": "A_direct_official",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "No famous-name or postwar-only inference is required; the direct official chronology names both OPA and OSS.",
                "sources": [{"source_key": MALENBAUM_CR}, {"source_key": INDEX, "support_type": "context_only"}],
            },
            {
                "key": "opa-wilfred-malenbaum-b1036",
                "person_id": PEOPLE[20][0],
                "affiliation_key": "wilfred-malenbaum-opa-b1036",
                "claim_type": "immediate_pre_oss_affiliation",
                "claim_text": "Wilfred Malenbaum's best-supported immediate pre-OSS affiliation was service as an economist with the Office of Price Administration in 1941.",
                "evidence_paraphrase": "The Congressional Record lists economist, OPA, 1941 immediately before chief of the OSS Food and Agriculture Section, 1941-1945.",
                "identity_match_assessment": "High confidence from the rare exact name, compatible civilian grade, and direct official OSS role chronology.",
                "temporal_assessment": "Probable immediate predecessor: the sequence is explicit, but both entries are dated only to 1941 and an exact transfer date is absent.",
                "source_quality": "A_direct_official",
                "claim_confidence": "high",
                "publication_status": "publish_qualified",
                "match_notes": "Modeled as a government assignment, not a private employer. No last civilian employer is inferred from Harvard student status.",
                "sources": [{"source_key": MALENBAUM_CR}],
            },
            {
                "key": "harvard-student-wilfred-malenbaum-b1036",
                "person_id": PEOPLE[20][0],
                "affiliation_key": "wilfred-malenbaum-harvard-student-b1036",
                "claim_type": "other_pre_oss_affiliation",
                "claim_text": "Wilfred Malenbaum was a Harvard graduate student in economics by April 1936.",
                "evidence_paraphrase": "A contemporary Harvard newspaper identifies Wilfred Malenbaum as a second-year graduate student studying economics.",
                "identity_match_assessment": "High confidence from the rare exact name and the compatible Harvard and economics chronology in the later official record.",
                "temporal_assessment": "Documented prewar student status; it is neither employment nor the immediate predecessor to OSS because OPA intervened.",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "Harvard is not labeled an employer. The notice does not establish the full enrollment span.",
                "sources": [{"source_key": MALENBAUM_HARVARD}, {"source_key": MALENBAUM_CR, "support_type": "context_only"}],
            },
            {
                "key": "identity-lambros-makris-greek-og-b1036",
                "person_id": PEOPLE[10][0],
                "claim_type": "identity",
                "claim_text": "Indexed Technician Fifth Grade Lambros G. Makris appears on a direct OSS Greek Operational Group roster.",
                "evidence_paraphrase": "The wartime roster repeats the exact full name and technician grade and carries the same nonshared protected identifier as the index.",
                "identity_match_assessment": "Confirmed by exact name, matching technician grade, and a matching protected identifier; the identifier is withheld.",
                "temporal_assessment": "Direct wartime OSS identity evidence only; the roster does not identify a pre-OSS employer or affiliation.",
                "source_quality": "A_direct_official",
                "claim_confidence": "confirmed",
                "publication_status": "published",
                "match_notes": "The roster establishes OSS Greek Operational Group context, not an earlier employer or occupation.",
                "sources": [{"source_key": MAKRIS_ROSTER}, {"source_key": INDEX, "support_type": "context_only"}],
            },
            {
                "key": "identity-maxime-malfettes-varlin-b1036",
                "person_id": PEOPLE[22][0],
                "claim_type": "identity",
                "claim_text": "Indexed Sergeant Maxime Malfettes is high-confidence associated with the BCRA/SOE RF Mission Varlin record.",
                "evidence_paraphrase": "A sourced historical table records Sgt. Maxime Malfettes, aliases Tartuffe and Maxime Brunet, on Mission Varlin on January 27, 1944.",
                "identity_match_assessment": "High confidence from the rare exact name, matching sergeant rank, and specific wartime special-operations context; the indexed personnel file is still needed.",
                "temporal_assessment": "Wartime identity context only; the source does not establish a pre-OSS employer or sequence into the indexed file.",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "claim_confidence": "medium",
                "publication_status": "publish_qualified",
                "match_notes": "BCRA/SOE service is not silently relabeled as OSS employment, and no prewar affiliation is inferred.",
                "sources": [{"source_key": MALFETTES_HISTORY}, {"source_key": INDEX, "support_type": "context_only"}],
            },
        ]
    )
    return values


def base_update(row: int) -> dict[str, object]:
    name = PEOPLE[row][1]
    box = PEOPLE[row][2]
    return {
        "person_id": PEOPLE[row][0],
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified page 291 source preserves {name}, Box {box}, rank or grade when printed, notes when present, and archive location. Staged official, exact-name, employment, occupation, obituary, institutional, newspaper, directory, and archival searches did not establish a defensible identity-and-affiliation bridge.",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": f"Review indexed Box {box} for corroborating identifiers, immediate pre-OSS affiliation, and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }


def person_updates() -> list[dict[str, object]]:
    updates = [base_update(row) for row in PEOPLE]
    by_row = {row: update for row, update in zip(PEOPLE, updates, strict=True)}

    for row in set(ARMY_ASSOCIATIONS) | set(ARMY_IDENTITY_ONLY):
        identity = "high_confidence" if row in VARIANT_ROWS else "confirmed"
        by_row[row].update(
            identity_status=identity,
            identity_evidence=army_identity_assessment(row),
            personnel_category="enlisted_army_personnel",
            commissioned_officer=False,
            allied_or_foreign_personnel=False,
            nara_catalog_id="1263923",
            archival_review_priority="high",
        )
        if row in ARMY_ASSOCIATIONS:
            by_row[row].update(
                research_status="occupation_only_found",
                next_action=f"Review Box {PEOPLE[row][2]} to identify a named employer or institution and establish Army-to-OSS chronology. The protected Army link supplies only a broad historical occupation or student-status category.",
            )
        else:
            by_row[row].update(
                research_status="requires_archival_review",
                next_action=f"Review Box {PEOPLE[row][2]} to establish the immediate pre-OSS affiliation and last civilian employer. The accepted Army record is retained for identity only.",
            )

    by_row[5].update(
        identity_evidence="A protected Army candidate was explicitly rejected because the Army name is materially different from Thomas B. Majure. No identity, occupation, or chronology was transferred.",
        archival_review_priority="critical",
        next_action="Review Box 476 and the original identifier-bearing index record to resolve the rejected Army candidate. No candidate occupation is published.",
    )
    by_row[6].update(name_variants=["Paul Makanowitsky"], replace_name_variants=False)
    by_row[8].update(name_variants=["Toivo W Maki"], replace_name_variants=False, archival_review_priority="critical")
    by_row[23].update(name_variants=["John J Malia"], replace_name_variants=False, archival_review_priority="critical")
    by_row[32].update(name_variants=["Hal Mallory"], replace_name_variants=False)
    by_row[44].update(name_variants=["Morrill E Malone"], replace_name_variants=False)

    by_row[9].update(
        identity_status="ambiguous",
        identity_evidence="A distinctive professional-tennis namesake with USC and wartime Navy chronology was reviewed, but no independent OSS, protected-identifier, rank, or Box linkage establishes that he is the indexed Gene Mako. The biography is not assigned by name alone.",
        research_status="needs_identity_review",
        archival_review_priority="critical",
        next_action="Review Box 476 for Gene Mako's full name, birth data, Navy or OSS assignment, and pre-service chronology before assigning the tennis biography.",
    )
    by_row[10].update(
        identity_status="confirmed",
        identity_evidence="A direct OSS Greek Operational Group roster repeats the exact full name and technician grade and carries the same nonshared protected identifier as the index; the identifier remains private.",
        personnel_category="enlisted_army_personnel",
        commissioned_officer=False,
        allied_or_foreign_personnel=False,
        research_status="requires_archival_review",
        archival_review_priority="high",
        next_action="Review Box 476 for Lambros G. Makris's pre-OSS employer, occupation, and military chronology. The roster establishes wartime OSS identity only.",
    )
    by_row[20].update(
        identity_status="high_confidence",
        identity_evidence="The rare exact name, compatible civilian professional grade, and official 1941-1945 chronology identifying Wilfred Malenbaum as chief of the OSS Food and Agriculture Section support a high-confidence match.",
        personnel_category="civilian_professional_or_administrative_grade",
        commissioned_officer=False,
        allied_or_foreign_personnel=False,
        research_status="completed",
        archival_review_priority="medium",
        next_action="Review Box 477 for the exact 1941 OPA-to-OSS transition and any last civilian employer before the intervening federal assignment. Harvard is documented as student status, not employment.",
    )
    by_row[22].update(
        identity_status="high_confidence",
        identity_evidence="The rare exact name, matching sergeant rank, and specific BCRA/SOE RF Mission Varlin context support a high-confidence identity, while the indexed personnel file remains unreviewed.",
        name_variants=["Tartuffe", "Maxime Brunet"],
        replace_name_variants=False,
        personnel_category="foreign_or_allied_military_personnel",
        commissioned_officer=False,
        allied_or_foreign_personnel=True,
        research_status="requires_archival_review",
        archival_review_priority="critical",
        next_action="Review Box 477 to establish Maxime Malfettes's relationship to the indexed OSS file and identify his prewar occupation or institutional affiliation. BCRA/SOE service is not treated as civilian employment.",
    )
    by_row[29].update(
        identity_status="ambiguous",
        identity_evidence="An exact-name psychologist and author affiliated with the American Jewish Committee was reviewed, but accessible authoritative sources did not independently connect that biography to the indexed P-5 row or establish the required OSS identity bridge.",
        research_status="needs_identity_review",
        archival_review_priority="critical",
        next_action="Review Box 477 for Julius B. Maller's full biographical identifiers and employment history before assigning the psychologist biography or any named institution.",
    )

    duplicate_groups = {
        13: "page291-john-malandre-malanore-b1036",
        14: "page291-john-malandre-malanore-b1036",
        15: "page291-victor-malaspina-malispino-b1036",
        26: "page291-victor-malaspina-malispino-b1036",
        38: "page291-patricia-malmsted-malmstedt-b1036",
        39: "page291-patricia-malmsted-malmstedt-b1036",
    }
    for row, group in duplicate_groups.items():
        by_row[row]["possible_duplicate_group"] = group
    for row in (13, 14, 26, 38, 39):
        by_row[row].update(
            identity_status="ambiguous",
            research_status="needs_identity_review",
            archival_review_priority="critical",
            next_action=f"Review both Box {PEOPLE[row][2]} spelling-variant rows in duplicate group {duplicate_groups[row]} before any merge or transfer of identity and affiliation evidence.",
        )
    by_row[15]["archival_review_priority"] = "critical"
    by_row[35].update(
        archival_review_priority="critical",
        next_action="Review Box 477 and the original index source for John W. Malloy. The printed identifier was ingested in malformed scientific notation and is unusable for identity resolution; it is not exposed publicly.",
    )

    if len(updates) != 46:
        raise RuntimeError(f"Expected 46 person updates, generated {len(updates)}")
    return updates


def unresolved_reason(row: int) -> str:
    special = {
        5: "A materially different Army-name candidate was rejected; no identity or occupation was transferred.",
        9: "A famous tennis namesake was reviewed but not assigned because no independent OSS or protected-identifier bridge was found.",
        10: "A direct roster confirms Lambros G. Makris in the OSS Greek Operational Group but supplies no pre-OSS affiliation.",
        13: "The adjacent Malandre and Malanore spellings remain separate possible-duplicate entities pending Box 476 review.",
        14: "The adjacent Malandre and Malanore spellings remain separate possible-duplicate entities pending Box 476 review.",
        20: "Official evidence supports OPA as Wilfred Malenbaum's probable immediate government affiliation and Harvard as earlier student status; no last civilian employer is established.",
        22: "Mission Varlin evidence supports identity and aliases but not a pre-OSS employer or transition into the indexed file.",
        26: "The Malaspina and Malispino spellings remain separate possible-duplicate entities; only the Malaspina row has accepted Army evidence.",
        29: "The exact-name psychologist biography lacks an independent OSS or personnel-file bridge and remains unassigned.",
        35: "The printed identifier is malformed scientific notation and cannot be used for identity resolution.",
        38: "The adjacent Malmsted and Malmstedt spellings remain separate possible-duplicate entities pending Box 477 review.",
        39: "The adjacent Malmsted and Malmstedt spellings remain separate possible-duplicate entities pending Box 477 review.",
    }
    return special.get(
        row,
        "Unbridged namesakes, snippets, commercial people-finder pages, unsourced genealogy, relatives, and postwar-only leads did not establish this indexed person's identity or pre-OSS affiliation.",
    )


def research_attempts() -> list[dict[str, object]]:
    updates = {item["person_id"]: item for item in person_updates()}
    substantiated = set(ARMY_ASSOCIATIONS) | set(ARMY_IDENTITY_ONLY) | {10, 20, 22}
    candidate_review = {9, 13, 14, 26, 29, 38, 39}
    values: list[dict[str, object]] = []
    for row in PEOPLE:
        person_id, name, box = PEOPLE[row]
        outcome = "source_reviewed" if row in substantiated else "candidate_found" if row in candidate_review else "candidate_rejected"
        values.append(
            {
                "key": f"page291-row{row}-{slug(name)}-b1036",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index context; exact-name and meaningful initial, suffix, alias, punctuation and OCR variants; OSS and CIA Reading Room; rank, branch, assignment and protected-identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory and archival searches; indexed Box {box}",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_1036",
                "started_at": "2026-11-04T16:45:00-05:00",
                "completed_at": "2026-11-04T18:42:00-05:00",
                "outcome": outcome,
                "sources_reviewed": 7 if row in substantiated else 5,
                "candidate_sources_rejected": 2 if row in substantiated else 4,
                "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, and postwar-only leads were rejected. Army categories were not converted into named employers; the 1945 Maki category and undefined Malakowsky code were not published as occupations; and possible duplicates were not merged.",
                "research_notes": f"{unresolved_reason(row)} The official index, exact-name OSS searches, targeted CIA context, employment and occupation searches, and institutional, newspaper, obituary, directory, and archival searches were reviewed as applicable. Page 291, the cited Army code-list pages, Congressional Record page 2661, the Makris roster, and the Malfettes mission table were visually checked where used. No authenticated NARA Catalog API request was made.",
                "next_action": str(updates[person_id]["next_action"]),
                "attempt_number": 1,
                "research_agent_version": "before-oss-b1036-v1",
            }
        )
    if len(values) != 46:
        raise RuntimeError(f"Expected 46 research attempts, generated {len(values)}")
    return values


def main() -> None:
    bundle = {
        "bundle_version": "batch-1036-v1",
        "reviewer": "Before OSS Batch 1036 evidence review",
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
