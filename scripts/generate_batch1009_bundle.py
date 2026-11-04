#!/usr/bin/env python3
"""Generate the reviewed Batch 1009 evidence bundle for PDF page 499."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page499-westphal-to-wheeler-"
    "review_batch-1009_2026-11-03.json"
)

INDEX = "nara-index-b1009"
ARMY = "army-bulk-b1009"
TECH = "army-tech-b1009"
CODES = "army-codes-b1009"
USEA = "usea-elkins-wetherill-b1009"
OAC = "oac-nathaniel-weyl-b1009"
REED = "reed-donald-wheeler-b1009"
RUNE = "runeberg-gosta-wetterhall-b1009"
REGIMENT = "dalregementet-wetterhall-b1009"

ORG_PENN = "penn-b1009"
ORG_FIRST_TROOP = "first-troop-philadelphia-b1009"
ORG_SIGNAL = "signal-corps-b1009"
ORG_BEW = "board-economic-warfare-b1009"
ORG_FED = "federal-reserve-board-b1009"
ORG_AAA = "agricultural-adjustment-b1009"
ORG_YALE = "yale-b1009"
ORG_KRIGSSKOLAN = "krigsskolan-b1009"
ORG_RANGER = "swedish-army-ranger-school-b1009"

REVERSED_ELKINS_ID = "a7882b4d-91f8-53a7-953c-ce2a5344820c"

PEOPLE = {
    1: ("14c96599-61a4-5137-96be-af621d00ec6f", "Westphal Mau M Weston"),
    2: ("3cc43895-068a-5665-a183-c2ae2651556e", "Elkins Wetherill"),
    3: ("f6367530-b7ea-5ba1-bc83-b9e68bd1d211", "Curtis J Wethington"),
    4: ("0f936f33-9975-5d30-ae99-8464b7a769cf", "Melvin H Wetmore"),
    5: ("6e67ec35-b0ba-5f09-acfd-bd90fffa1163", "James E Wetrich"),
    6: ("531df8e6-9882-5569-8501-a2708c296072", "Gosta C.F. Wetterhall"),
    7: ("77aff1f6-37c6-5b0c-a1fc-6be4680cebd1", "Kenneth L Wettstein"),
    8: ("f4d61b8b-2635-5e36-9059-61e3b97bd937", "Albert L Wetzel"),
    9: ("66d247aa-65b1-5da8-992f-8dc025834910", "Richard C Wetzel"),
    10: ("6fde13fa-256f-531a-9c73-06aae304033d", "Victor A Wetzler"),
    11: ("7ded2005-246b-5e26-90a2-a22f78243da9", "Peter Weyer"),
    12: ("e8006d10-4bff-5709-8158-4b9d992f6f96", "Nathaniel Weyl"),
    13: ("de724ede-6859-5ab1-aeac-e8729c0c1d3c", "Walter Weyl"),
    14: ("ce02494a-9625-5fde-b55c-0292939fb143", "Stephen C Weyland"),
    15: ("ba23240d-7619-58a7-8292-50501df15f4a", "Thomas H Whalen"),
    16: ("abf01a50-b0cc-5f09-aac7-8807763c3cd0", "Faith S Whaley"),
    17: ("f263835a-3334-543f-9cf9-945c548e6b84", "Joseph S Whallen"),
    18: ("979b6fb6-3abc-5d93-a16d-312a37573a06", "Daniel O Whallon"),
    19: ("47a54693-66c5-5519-8f92-9f4d13ec6943", "Joseph F Whalon"),
    20: ("ca848a3a-f268-5bcd-90f6-8ddee866fd47", "Le Roy Whan"),
    21: ("bd8f2c86-c96d-5f3c-b68b-2e4635f86bd3", "Donald L Wharton"),
    22: ("3a8524a5-446e-5b0e-9e7a-6da9b2f76900", "Jack R Wheat"),
    23: ("e64b4ca2-13c8-5e73-ab08-158c09489117", "Jack R Wheat"),
    24: ("46b3553b-f74d-50b6-9cae-c63a19c0ecfa", "John P Wheat"),
    25: ("9cd78d4b-c2ed-5614-9741-e89a17057d95", "Robert I Wheat"),
    26: ("49bba267-8013-57b4-8322-248127a4cefa", "Alice G Wheaton"),
    27: ("0f883c74-4f9b-5212-b1cf-542ef0014b1b", "Jesse D Wheaton"),
    28: ("944823db-b607-50ca-b08c-b0aca466e5f4", "Barbara B Wheeler"),
    29: ("c5d47c44-9d28-5eb4-a610-e325f5858a0e", "Donald N Wheeler"),
    30: ("239f1ec5-0b8e-5167-9aa6-ecc18b00e185", "Donald Wheeler"),
    31: ("a3dfd306-c539-5efc-98aa-2eb50775da64", "Elmore Wheeler"),
    32: ("a73c97b1-3be6-5698-800a-5e838d7d1a1b", "George R Wheeler"),
    33: ("bb132943-7aad-5797-991f-d0cf970e2d03", "Howard D Wheeler"),
    34: ("090a518b-209c-57ab-9ef3-869914daa9c2", "Howard F Wheeler"),
    35: ("ce8b8cd9-89bb-5fc7-bb59-ec8344827598", "John L Wheeler"),
    36: ("817fb808-4d88-5fd2-800a-ba9078a7f1dd", "John W Wheeler"),
    37: ("afbd0519-adb4-5422-a950-6d77586a0bd6", "Leroy E Wheeler"),
    38: ("b8b1cbff-61cb-5d62-bfe3-283741bac968", "Lois E Wheeler"),
    39: ("b06a0a47-2a69-586e-9bca-5ecf768f3d59", "Margaret I Wheeler"),
    40: ("b0b4f3f5-18b8-5289-bbed-6d018545c699", "Nelson O Wheeler"),
    41: ("b53f79f1-f484-5bc9-9fb2-b393b4247ddb", "Raymond K Wheeler"),
    42: ("dc881c88-c124-5a5e-a6ff-a8c0c7e890cf", "Roderick D Wheeler"),
    43: ("b6a5be11-cf9a-5bd1-82be-6b1298efc275", "Sydney W Wheeler"),
    44: ("55924f02-fc8b-5d1d-83ae-f5f87160070b", "William C Wheeler"),
    45: ("fd44c322-a652-5965-a756-fd5eebaa6944", "William J Wheeler"),
    46: ("24b3b97a-eb41-5324-b1ca-57093922f0c3", "William M Wheeler Jr."),
}

ARMY_MATCHES = {
    3: {"date": "1943-08-13", "code": "339", "occupation": "nursery and landscaping laborer", "label": "Nursery and landscaping laborers", "locator": "PDF physical page 173; historical category 3-39"},
    4: {"date": "1942-12-28", "code": "530", "occupation": "steam fitter, gas fitter, or plumber", "label": "Steam fitters, gas fitters, and plumbers", "locator": "PDF physical page 173; historical category 5-30"},
    5: {"date": "1943-08-26", "code": "583", "occupation": "mechanic or repairman, not elsewhere classified", "label": "Mechanics and repairmen, n.e.c.", "locator": "PDF physical page 173; historical category 5-83"},
    14: {"date": "1942-10-14", "code": "018", "occupation": "industrial engineer", "label": "Engineers, industrial", "locator": "PDF physical page 170; historical category 0-18"},
    23: {"date": "1943-11-04", "code": "992", "occupation": "student", "label": "Students", "locator": "PDF physical page 304; amended historical category 9-92"},
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def box_for(row: int) -> str:
    if row == 1:
        return "828"
    if row <= 36:
        return "829"
    return "830"


def occupation_key(row: int) -> str:
    return f"{slug(PEOPLE[row][1])}-army-occupation-row{row}-b1009"


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 828-830",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 499, rows 1-46",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 46 printed rows remain separate; full service numbers remain private.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; five accepted and two conflicting protected-identifier comparisons; identifiers withheld",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "Army-entry occupations are not named employers, institutions, or exact OSS-transfer records.",
        },
        {
            "key": TECH,
            "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf",
            "archival_identifier": "NN3-064-03-008; National Archives Identifier 1263923",
            "title": "World War II Army Enlistment Records: Reference Copy of Technical Documentation",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives at College Park - Electronic Records",
            "publication_record_date": "1994-2005; reference copy modified 2011",
            "locator": "PDF physical pages 44-46; name, entry-date, grade, and civilian-occupation fields",
            "access_date": "2026-11-03",
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
            "locator": "PDF physical pages 170-175 and 304",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
        },
        {
            "key": USEA,
            "stable_url": "https://useventing.com/news-media/news/elkins-wetherill-1919-2011",
            "title": "Elkins Wetherill, 1919-2011",
            "repository_publisher": "United States Eventing Association",
            "publication_record_date": "2011-08-22",
            "locator": "Biographical notice, second paragraph",
            "access_date": "2026-11-03",
            "source_quality": "B_authoritative_institutional",
            "rights_notes": "Supports the education-to-Army chronology and direct OSS identity; it does not identify a civilian employer.",
        },
        {
            "key": OAC,
            "stable_url": "https://oac.cdlib.org/findaid/ark:/13030/tf0489n3tj",
            "archival_identifier": "Nathaniel Weyl papers, collection 86003",
            "title": "Weyl (Nathaniel) papers, 1920-2004",
            "author_creator": "Finding aid prepared by Dale Reed",
            "repository_publisher": "Hoover Institution Library & Archives via Online Archive of California",
            "publication_record_date": "Finding aid encoded 2024-11-26",
            "locator": "Biographical chronology, 1933-1945",
            "access_date": "2026-11-03",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Nathaniel Weyl papers",
            "rights_notes": "The finding aid identifies the collection's government-service records and date-bounded economist positions.",
        },
        {
            "key": REED,
            "stable_url": "https://www.reed.edu/reed-magazine/in-memoriam/archive.php?letter=W",
            "title": "Donald N. Wheeler '35",
            "repository_publisher": "Reed College",
            "publication_record_date": "Memorial for death on 2002-11-08",
            "locator": "In Memoriam archive, Donald N. Wheeler entry",
            "access_date": "2026-11-03",
            "source_quality": "B_authoritative_institutional",
            "rights_notes": "Directly identifies Donald Niven Wheeler, his Yale teaching, and five years as OSS chief economist.",
        },
        {
            "key": RUNE,
            "stable_url": "https://runeberg.org/vemarvem/svea64/0890.html",
            "title": "Wetterhall, Gösta C F",
            "repository_publisher": "Project Runeberg reproduction of Vem är Vem? Svealand utom Stor-Stockholm 1964",
            "publication_record_date": "1964",
            "locator": "Printed page 866; original scan visually inspected",
            "access_date": "2026-11-03",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "rights_notes": "The scan records promotion to major in 1944 and teaching at Krigsskolan in 1938-1943; OCR was checked against the image.",
        },
        {
            "key": REGIMENT,
            "stable_url": "https://hooga.se/00%20Dalregementetsmuseer/gamla_dalreghemsidan/03_Samlingar/03_bibliotek/sepals_2009/sepals.htm",
            "title": "Review of Roger Albrigtsen's Operation Sepals",
            "repository_publisher": "Dalregementets museer historical website",
            "publication_record_date": "2009",
            "locator": "Swedish Help section summary",
            "access_date": "2026-11-03",
            "source_quality": "D_correlative_or_secondary",
            "rights_notes": "Institutional historical summary; used only for a qualified wartime assignment, not an immediate-pre-OSS conclusion.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {"key": ORG_PENN, "organization_id": "40f6dffe-883f-58ac-8fd0-3f769bfd06fa", "canonical_name": "University of Pennsylvania", "historical_name": "University of Pennsylvania", "sector": "academia_and_research", "country": "United States", "normalization_notes": "Existing canonical organization reused; student status is not employment."},
        {"key": ORG_FIRST_TROOP, "canonical_name": "First Troop Philadelphia City Cavalry", "historical_name": "First Troop Philadelphia Cavalry", "aliases": ["First Troop Philadelphia Cavalry"], "organization_type": "military unit", "sector": "military", "city": "Philadelphia", "state_or_region": "Pennsylvania", "country": "United States", "normalization_notes": "Preserves the shorter form used by the source while supplying the unit's canonical name."},
        {"key": ORG_SIGNAL, "organization_id": "37fe0e48-9745-5a0a-8e04-6be9bc7c5c91", "canonical_name": "United States Army Signal Corps", "historical_name": "Signal Corps", "aliases": ["U.S. Army Signal Corps"], "organization_type": "military branch", "sector": "military", "country": "United States", "normalization_notes": "Existing canonical organization reused."},
        {"key": ORG_BEW, "organization_id": "c560e197-f162-5279-b2f2-b75de9c71872", "canonical_name": "Board of Economic Warfare", "historical_name": "U.S. Board of Economic Warfare", "aliases": ["U.S. Board of Economic Warfare"], "organization_type": "federal agency", "sector": "federal_government", "country": "United States", "normalization_notes": "Existing canonical organization reused."},
        {"key": ORG_FED, "organization_id": "931db319-c199-51a4-8874-cba16bd3ecb5", "canonical_name": "Board of Governors of the Federal Reserve System", "historical_name": "U.S. Federal Reserve Board", "aliases": ["Federal Reserve Board"], "organization_type": "federal agency", "sector": "federal_government", "country": "United States", "normalization_notes": "Existing canonical organization reused; the historical name from the finding aid is preserved."},
        {"key": ORG_AAA, "canonical_name": "Agricultural Adjustment Administration", "historical_name": "U.S. Agricultural Adjustment Administration", "aliases": ["AAA"], "organization_type": "federal agency", "sector": "federal_government", "country": "United States", "active_dates": "1933-1942", "normalization_notes": "Historical federal agency; no modern successor is substituted."},
        {"key": ORG_YALE, "organization_id": "918dedde-f9d1-5db1-8304-5c218a06b9b5", "canonical_name": "Yale University", "historical_name": "Yale", "organization_type": "university", "sector": "academia_and_research", "state_or_region": "Connecticut", "country": "United States", "normalization_notes": "Existing canonical organization reused."},
        {"key": ORG_KRIGSSKOLAN, "canonical_name": "Krigsskolan", "historical_name": "Krigsskolan", "aliases": ["KS", "Swedish Military Academy"], "organization_type": "military academy", "sector": "military", "country": "Sweden", "normalization_notes": "Preserves the Swedish historical name; the source abbreviation KS is expanded cautiously."},
        {"key": ORG_RANGER, "canonical_name": "Swedish Army Ranger School", "historical_name": "Jägarskolan", "aliases": ["Army Ranger School"], "organization_type": "military school", "sector": "military", "city": "Abisko/Kiruna", "country": "Sweden", "normalization_notes": "English canonical label paired with the Swedish historical name supplied by the institutional history."},
    ]


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, item in ARMY_MATCHES.items():
        values.append({
            "key": occupation_key(row),
            "person_id": PEOPLE[row][0],
            "occupation": item["occupation"],
            "relationship_type": "student" if item["code"] == "992" else "unknown",
            "end_date": item["date"],
            "date_precision": f"Historical civilian-occupation code {item['code']} was recorded at Army entry on {item['date']}; no named employer or institution is supplied.",
            "country": "United States",
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "confirmed",
            "claim_confidence": "medium",
            "source_quality": "A_direct_official",
            "publication_status": "publish_qualified",
            "research_notes": "Broad historical category only; no named employer, workplace, institution, or exact OSS transition is inferred.",
        })
    values.extend([
        {"key": "elkins-penn-student-b1009", "person_id": PEOPLE[2][0], "organization_key": ORG_PENN, "organization_name_as_found": "University of Pennsylvania", "relationship_type": "student", "end_date": "1941", "date_precision": "Studies were interrupted in 1941 when his cavalry unit entered active duty.", "city": "Philadelphia", "state_or_region": "Pennsylvania", "country": "United States", "pre_oss_temporal_basis": "explicit_immediate", "identity_confidence": "high_confidence", "claim_confidence": "high", "source_quality": "B_authoritative_institutional", "publication_status": "published", "research_notes": "Immediate civilian status before active military service, not employment and not a last-civilian-employer claim."},
        {"key": "elkins-first-troop-b1009", "person_id": PEOPLE[2][0], "organization_key": ORG_FIRST_TROOP, "organization_name_as_found": "First Troop Philadelphia Cavalry", "relationship_type": "military_assignment", "start_date": "1941", "date_precision": "The unit was called to active duty in 1941; the source does not give the end date.", "city": "Philadelphia", "state_or_region": "Pennsylvania", "country": "United States", "pre_oss_temporal_basis": "strongly_date_bounded", "identity_confidence": "high_confidence", "claim_confidence": "high", "source_quality": "B_authoritative_institutional", "publication_status": "published", "research_notes": "A pre-OSS military pathway; not labeled the immediate predecessor without exact transfer chronology."},
        {"key": "elkins-signal-corps-b1009", "person_id": PEOPLE[2][0], "organization_key": ORG_SIGNAL, "organization_name_as_found": "Signal Corps", "relationship_type": "military_assignment", "start_date": "1941", "end_date": "1945", "date_precision": "The notice lists Signal Corps within his World War II Army service but gives no exact dates or transfer order.", "country": "United States", "pre_oss_temporal_basis": "temporal_relation_uncertain", "identity_confidence": "high_confidence", "claim_confidence": "medium", "source_quality": "B_authoritative_institutional", "publication_status": "publish_qualified", "research_notes": "Military affiliation only; sequence relative to OSS remains unresolved."},
        {"key": "wetterhall-krigsskolan-b1009", "person_id": PEOPLE[6][0], "organization_key": ORG_KRIGSSKOLAN, "organization_name_as_found": "KS", "role_title": "Teacher", "occupation": "military instructor", "relationship_type": "military_assignment", "start_date": "1938", "end_date": "1943", "date_precision": "The visually checked Swedish directory abbreviates the entry as teacher at KS, 1938-1943.", "country": "Sweden", "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "high_confidence", "claim_confidence": "medium", "source_quality": "C_reputable_contemporary_or_scholarly", "publication_status": "publish_qualified", "research_notes": "Prewar military teaching assignment; not an immediate-pre-OSS conclusion."},
        {"key": "wetterhall-ranger-school-b1009", "person_id": PEOPLE[6][0], "organization_key": ORG_RANGER, "organization_name_as_found": "Jägarskolan", "role_title": "Commander", "relationship_type": "military_assignment", "start_date": "1944", "end_date": "1945", "date_precision": "The institutional history places him in command at the time of the 1944-1945 Sepals operations.", "city": "Abisko/Kiruna", "country": "Sweden", "pre_oss_temporal_basis": "temporal_relation_uncertain", "identity_confidence": "high_confidence", "claim_confidence": "medium", "source_quality": "D_correlative_or_secondary", "publication_status": "publish_qualified", "research_notes": "Wartime Swedish assignment; the source does not establish direct OSS employment or exact assignment sequence."},
        {"key": "weyl-bew-b1009", "person_id": PEOPLE[12][0], "organization_key": ORG_BEW, "organization_name_as_found": "U.S. Board of Economic Warfare", "role_title": "Economist", "occupation": "economist", "relationship_type": "government_assignment", "start_date": "1942", "end_date": "1943", "date_precision": "Finding-aid chronology gives years only.", "country": "United States", "last_civilian_pre_service": True, "pre_oss_temporal_basis": "strongly_date_bounded", "identity_confidence": "high_confidence", "claim_confidence": "high", "source_quality": "B_authoritative_institutional", "publication_status": "published", "research_notes": "Last documented civilian government assignment before 1943-1945 Army service; not labeled immediate pre-OSS."},
        {"key": "weyl-fed-b1009", "person_id": PEOPLE[12][0], "organization_key": ORG_FED, "organization_name_as_found": "U.S. Federal Reserve Board", "role_title": "Economist", "occupation": "economist", "relationship_type": "government_assignment", "start_date": "1941", "end_date": "1942", "date_precision": "Finding-aid chronology gives years only.", "country": "United States", "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "high_confidence", "claim_confidence": "high", "source_quality": "B_authoritative_institutional", "publication_status": "published", "research_notes": "Earlier documented pre-OSS government assignment."},
        {"key": "weyl-aaa-b1009", "person_id": PEOPLE[12][0], "organization_key": ORG_AAA, "organization_name_as_found": "U.S. Agricultural Adjustment Administration", "role_title": "Economist", "occupation": "economist", "relationship_type": "government_assignment", "start_date": "1933", "end_date": "1934", "date_precision": "Finding-aid chronology gives years only.", "country": "United States", "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "high_confidence", "claim_confidence": "high", "source_quality": "B_authoritative_institutional", "publication_status": "published", "research_notes": "Earlier documented pre-OSS government assignment."},
        {"key": "donald-wheeler-yale-b1009", "person_id": PEOPLE[29][0], "organization_key": ORG_YALE, "organization_name_as_found": "Yale", "role_title": "Teacher", "occupation": "teacher", "relationship_type": "employment", "end_date": "1941", "date_precision": "The institutional memorial says he taught briefly at Yale before nearly a decade in Washington, including OSS; it supplies no exact year.", "state_or_region": "Connecticut", "country": "United States", "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "high_confidence", "claim_confidence": "medium", "source_quality": "B_authoritative_institutional", "publication_status": "publish_qualified", "research_notes": "Earlier employment only; intervening Washington work is not identified, so Yale is not labeled immediate or last civilian employer."},
    ])
    return values


def make_claim(*, key: str, row: int, claim_type: str, text: str, paraphrase: str,
               identity: str, temporal: str, quality: str, confidence: str,
               publication: str, notes: str, source_links: list[dict[str, str]],
               affiliation_key: str | None = None) -> dict[str, object]:
    value: dict[str, object] = {
        "key": key, "person_id": PEOPLE[row][0], "claim_type": claim_type,
        "claim_text": text, "evidence_paraphrase": paraphrase,
        "identity_match_assessment": identity, "temporal_assessment": temporal,
        "source_quality": quality, "claim_confidence": confidence,
        "publication_status": publication, "match_notes": notes,
        "sources": source_links,
    }
    if affiliation_key:
        value["affiliation_key"] = affiliation_key
    return value


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, item in ARMY_MATCHES.items():
        name = PEOPLE[row][1]
        values.append(make_claim(
            key=f"occupation-{slug(name)}-row{row}-b1009", row=row,
            claim_type="occupation",
            text=f"At Army entry on {item['date']}, {name} was recorded in the historical {item['occupation']} category; no named employer or institution is identified.",
            paraphrase=f"The accepted Army record carries civilian-occupation code {item['code']}, decoded from NARA's official code list.",
            identity="The category belongs only to the accepted exact-name, protected-identifier match; the identifier is not public.",
            temporal="Strongly date-bounded to Army entry; it does not establish the immediate pre-OSS affiliation or a named employer.",
            quality="A_direct_official", confidence="medium", publication="publish_qualified",
            notes="Published with its limits and excluded from verified-employer analytics.",
            source_links=[
                {"source_key": ARMY, "locator_override": f"Army entry {item['date']}; civilian occupation code {item['code']}; protected identifier withheld"},
                {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46"},
                {"source_key": CODES, "locator_override": item["locator"], "excerpt_override": item["label"]},
            ], affiliation_key=occupation_key(row),
        ))
    values.extend([
        make_claim(key="identity-elkins-wetherill-b1009", row=2, claim_type="identity", text="Indexed Captain Elkins Wetherill is a high-confidence match to the Penn student whose Army service included the Cavalry, Signal Corps, and OSS.", paraphrase="The exact distinctive name, captain rank in the index, Philadelphia/Penn context, and direct OSS statement align.", identity="High confidence; the protected index identifier is not reproduced publicly.", temporal="The biographical notice dates active duty from 1941 and return to school to 1945.", quality="B_authoritative_institutional", confidence="high", publication="published", notes="The separately printed page-134 Wetherill Elkins row remains a possible transposed duplicate, not silently merged.", source_links=[{"source_key": INDEX, "locator_override": "PDF page 499 row 2; protected identifier withheld"}, {"source_key": USEA, "locator_override": "Second paragraph", "excerpt_override": "His army service during World War II included the Cavalry, Signal Corps and OSS"}]),
        make_claim(key="student-elkins-penn-b1009", row=2, claim_type="other_pre_oss_affiliation", text="Elkins Wetherill was a University of Pennsylvania student immediately before his cavalry unit entered active duty in 1941.", paraphrase="The notice says his Penn studies were interrupted in 1941 when First Troop Philadelphia Cavalry was called to active duty.", identity="High-confidence distinctive-name and OSS-context match.", temporal="Explicit civilian status before active military service; student status is not employment.", quality="B_authoritative_institutional", confidence="high", publication="published", notes="University attendance is modeled as student status, never as an employer or last-civilian-employer claim.", source_links=[{"source_key": USEA, "locator_override": "Second paragraph", "excerpt_override": "In 1941 his studies were interrupted as the First Troop Philadelphia Cavalry was called to active duty"}], affiliation_key="elkins-penn-student-b1009"),
        make_claim(key="military-elkins-first-troop-b1009", row=2, claim_type="other_pre_oss_affiliation", text="Elkins Wetherill entered active duty with First Troop Philadelphia Cavalry in 1941.", paraphrase="The institutional notice explicitly connects the interrupted Penn studies to the cavalry unit's call to active duty.", identity="High-confidence distinctive-name and OSS-context match.", temporal="Strongly date-bounded pre-OSS military pathway, but the exact transfer date is not supplied.", quality="B_authoritative_institutional", confidence="high", publication="published", notes="Military assignment, not civilian employment and not labeled immediate pre-OSS.", source_links=[{"source_key": USEA, "locator_override": "Second paragraph", "excerpt_override": "First Troop Philadelphia Cavalry was called to active duty"}], affiliation_key="elkins-first-troop-b1009"),
        make_claim(key="military-elkins-signal-corps-b1009", row=2, claim_type="other_pre_oss_affiliation", text="Elkins Wetherill's World War II Army service included the Signal Corps, but its sequence relative to OSS remains uncertain.", paraphrase="The notice names the Cavalry, Signal Corps, and OSS without dates for each component.", identity="High-confidence distinctive-name and OSS-context match.", temporal="Temporal relation uncertain; no immediate-pre-OSS assignment is asserted.", quality="B_authoritative_institutional", confidence="medium", publication="publish_qualified", notes="Qualified military affiliation only.", source_links=[{"source_key": USEA, "locator_override": "Second paragraph", "excerpt_override": "included the Cavalry, Signal Corps and OSS"}], affiliation_key="elkins-signal-corps-b1009"),
        make_claim(key="identity-gosta-wetterhall-b1009", row=6, claim_type="identity", text="Indexed Swedish Major Gosta C.F. Wetterhall is a high-confidence match to Swedish officer Gösta C. F. Wetterhall.", paraphrase="The distinctive full initials, Swedish nationality, and major rank in 1944 align with the index.", identity="High confidence from rare full name, initials, nationality, and rank.", temporal="The directory's promotion chronology places him at major rank during the OSS period.", quality="C_reputable_contemporary_or_scholarly", confidence="high", publication="published", notes="The Swedish diacritic form is preserved as a documented variant.", source_links=[{"source_key": INDEX, "locator_override": "PDF page 499 row 6"}, {"source_key": RUNE, "locator_override": "Printed page 866; original scan", "excerpt_override": "WETTERHALL, GÖSTA C F ... major 44"}]),
        make_claim(key="military-wetterhall-krigsskolan-b1009", row=6, claim_type="other_pre_oss_affiliation", text="Gösta C. F. Wetterhall served as a teacher at Krigsskolan from 1938 to 1943.", paraphrase="The visually checked Swedish directory records the abbreviated entry 'lär KS 38-43.'", identity="High-confidence rare-name, nationality, and rank match.", temporal="Documented prewar military teaching assignment; no direct OSS-entry date is given.", quality="C_reputable_contemporary_or_scholarly", confidence="medium", publication="publish_qualified", notes="The historical Swedish organization name is preserved; the assignment is not labeled immediate.", source_links=[{"source_key": RUNE, "locator_override": "Printed page 866; original scan", "excerpt_override": "lär KS 38-43"}], affiliation_key="wetterhall-krigsskolan-b1009"),
        make_claim(key="military-wetterhall-ranger-school-b1009", row=6, claim_type="other_pre_oss_affiliation", text="A Swedish regimental history places Gösta Wetterhall in command of the Ski Battalion and Army Ranger School during the 1944-1945 Sepals operations.", paraphrase="The historical summary names Wetterhall and identifies his command at Abisko/Kiruna during the events described.", identity="High-confidence rare-name and Swedish officer match.", temporal="Wartime assignment documented, but the source does not establish direct OSS employment or exact sequencing.", quality="D_correlative_or_secondary", confidence="medium", publication="publish_qualified", notes="Military assignment only; excluded from employer analytics and not labeled immediate pre-OSS.", source_links=[{"source_key": REGIMENT, "locator_override": "Swedish Help section summary"}], affiliation_key="wetterhall-ranger-school-b1009"),
        make_claim(key="identity-nathaniel-weyl-b1009", row=12, claim_type="identity", text="Indexed Nathaniel Weyl is a high-confidence match to economist Nathaniel Weyl, whose archival finding aid records 1943-1945 Army service.", paraphrase="The exact distinctive name, age-compatible chronology, and Army service bridge the indexed person to the archival collection.", identity="High confidence from distinctive exact name and matching wartime service chronology.", temporal="The finding aid dates government work immediately before 1943-1945 Army service.", quality="B_authoritative_institutional", confidence="high", publication="published", notes="No unrelated political or postwar assertions are necessary for the pre-OSS claim.", source_links=[{"source_key": INDEX, "locator_override": "PDF page 499 row 12"}, {"source_key": OAC, "locator_override": "Biographical chronology, 1941-1945", "excerpt_override": "1943-1945 | U.S. Army service"}]),
        make_claim(key="last-civilian-weyl-bew-b1009", row=12, claim_type="last_civilian_pre_service", text="Nathaniel Weyl served as an economist at the U.S. Board of Economic Warfare in 1942-1943, his last documented civilian assignment before Army service.", paraphrase="The archival finding aid places Board of Economic Warfare work immediately before 1943-1945 Army service.", identity="High-confidence distinctive-name and wartime-service match.", temporal="Strongly date-bounded as last civilian government assignment before service; not proven immediate pre-OSS.", quality="B_authoritative_institutional", confidence="high", publication="published", notes="Government assignment is not mislabeled as a private employer.", source_links=[{"source_key": OAC, "locator_override": "Biographical chronology, 1942-1945", "excerpt_override": "1942-1943 | Economist, U.S. Board of Economic Warfare"}], affiliation_key="weyl-bew-b1009"),
        make_claim(key="earlier-weyl-fed-b1009", row=12, claim_type="other_pre_oss_affiliation", text="Nathaniel Weyl served as an economist at the U.S. Federal Reserve Board in 1941-1942.", paraphrase="The archival finding aid gives the agency, role, and year range.", identity="High-confidence distinctive-name and wartime-service match.", temporal="Documented earlier pre-OSS government assignment.", quality="B_authoritative_institutional", confidence="high", publication="published", notes="Historical agency wording is preserved.", source_links=[{"source_key": OAC, "locator_override": "Biographical chronology, 1941-1942", "excerpt_override": "1941-1942 | Economist, U.S. Federal Reserve Board"}], affiliation_key="weyl-fed-b1009"),
        make_claim(key="earlier-weyl-aaa-b1009", row=12, claim_type="other_pre_oss_affiliation", text="Nathaniel Weyl served as an economist at the U.S. Agricultural Adjustment Administration in 1933-1934.", paraphrase="The archival finding aid gives the agency, role, and year range.", identity="High-confidence distinctive-name and wartime-service match.", temporal="Documented earlier pre-OSS government assignment.", quality="B_authoritative_institutional", confidence="high", publication="published", notes="Historical agency wording is preserved.", source_links=[{"source_key": OAC, "locator_override": "Biographical chronology, 1933-1934", "excerpt_override": "1933-1934 | Economist, U.S. Agricultural Adjustment Administration"}], affiliation_key="weyl-aaa-b1009"),
        make_claim(key="identity-donald-niven-wheeler-b1009", row=29, claim_type="identity", text="Indexed Donald N. Wheeler is a high-confidence match to Donald Niven Wheeler, identified by Reed College as an OSS chief economist.", paraphrase="The exact first name and middle initial, distinctive expanded middle name, and direct OSS economist role align.", identity="High confidence from institutional biography and direct OSS employment context.", temporal="The memorial places Yale teaching before nearly a decade in Washington that included five years in OSS.", quality="B_authoritative_institutional", confidence="high", publication="published", notes="The expanded middle name is added as a documented variant.", source_links=[{"source_key": INDEX, "locator_override": "PDF page 499 row 29"}, {"source_key": REED, "locator_override": "Donald N. Wheeler entry", "excerpt_override": "including five years as chief economist in the Office of Strategic Services"}]),
        make_claim(key="earlier-donald-wheeler-yale-b1009", row=29, claim_type="other_pre_oss_affiliation", text="Donald Niven Wheeler taught briefly at Yale before working in Washington, including five years in OSS.", paraphrase="The Reed memorial explicitly places brief Yale teaching before his Washington career.", identity="High-confidence exact-name and direct OSS-role match.", temporal="Documented prewar employment only; intervening Washington work is unspecified, so Yale is not labeled immediate or last civilian employer.", quality="B_authoritative_institutional", confidence="medium", publication="publish_qualified", notes="Qualified earlier employment and excluded from immediate-employer analytics.", source_links=[{"source_key": REED, "locator_override": "Donald N. Wheeler entry", "excerpt_override": "He taught briefly at Yale before working nearly a decade in Washington, D.C."}], affiliation_key="donald-wheeler-yale-b1009"),
        make_claim(key="identity-john-wheat-conflict-b1009", row=24, claim_type="identity", text="John P. Wheat remains in source conflict because two Army bulk records carry the same protected index identifier but different entry dates and occupation codes.", paraphrase="One official record indicates February 1943 and code 002; the other indicates June 1942 and code 402.", identity="Conflicting official bulk records; neither occupational result is selected or published as fact.", temporal="The conflicting entry dates prevent a reliable Army-entry chronology.", quality="A_direct_official", confidence="conflicting", publication="conflicting", notes="The protected identifier and record ordinals are omitted from public data.", source_links=[{"source_key": INDEX, "locator_override": "PDF page 499 row 24; protected identifier withheld"}, {"source_key": ARMY, "locator_override": "Two conflicting bulk records; protected identifier and ordinals withheld"}]),
    ])
    return values


def unresolved_reason(row: int) -> str:
    prefix = {
        10: "A secondary Ritchie Boys roster suggests an alias connection to Victor A. Velen, but it lacks enough identifiers and pre-OSS chronology to publish. ",
        22: "This unnumbered Jack R. Wheat row is not merged with the separately printed numbered row 23 solely on name. ",
        30: "Donald Niven Wheeler evidence belongs to the separately indexed Donald N. Wheeler row 29 and is not reassigned to this initial-less row. ",
        42: "A secondary Ritchie Boys roster contains the exact name but supplies no pre-OSS affiliation or second identifier. ",
    }.get(row, "")
    return prefix + (
        "Exact-name and meaningful-variant searches across the NARA index context, CIA Reading Room, "
        "Library of Congress, OSS, employment, occupation, obituary, institutional, newspaper, directory, "
        "and archival sources produced no reliable identity and pre-OSS affiliation bridge; unbridged namesakes were rejected."
    )


def base_update(row: int, **overrides: object) -> dict[str, object]:
    value: dict[str, object] = {
        "person_id": PEOPLE[row][0], "manual_review_required": True,
        "personnel_file_digitized": False, "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }
    if row in {22, 23}:
        value["possible_duplicate_group"] = "name-only:jack-r-wheat-page499"
    value.update(overrides)
    return value


def person_updates() -> list[dict[str, object]]:
    special = set(ARMY_MATCHES) | {2, 6, 12, 24, 29}
    values: list[dict[str, object]] = []
    for row in sorted(set(PEOPLE) - special):
        reason = unresolved_reason(row)
        values.append(base_update(
            row, identity_status="unresolved",
            identity_evidence=f"The visually verified page 499 source preserves {PEOPLE[row][1]}, its printed rank or notation, archival box, and location. {reason}",
            research_status="requires_archival_review",
            next_action=f"Review the indexed Box {box_for(row)} personnel file for corroborating identifiers, the immediate pre-OSS affiliation, and the last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}",
        ))
    for row in ARMY_MATCHES:
        item = ARMY_MATCHES[row]
        values.append(base_update(
            row, identity_status="confirmed",
            identity_evidence="The exact indexed and Army names agree, and a nonshared protected identifier connects the records. The identifier remains private.",
            personnel_category="enlisted_army_personnel", commissioned_officer=False,
            research_status="occupation_only_found", nara_catalog_id="1263923",
            next_action=f"Review the indexed Box {box_for(row)} personnel file to identify any named employer or institution behind the broad {item['occupation']} category and establish the Army-to-OSS chronology.",
        ))
    values.extend([
        base_update(2, identity_status="high_confidence", identity_evidence="The distinctive indexed name and captain rank align with an institutional biography that directly names his Penn studies, 1941 Army activation, Signal Corps, and OSS service.", name_variants=["Elkins Wetherill"], replace_name_variants=True, personnel_category="commissioned_army_officer", commissioned_officer=True, possible_duplicate_group="transposition:elkins-wetherill", research_status="completed", archival_review_priority="critical", next_action="Review the Box 829 personnel file to determine the exact Signal Corps-to-OSS sequence and whether the page-134 Wetherill Elkins row is a transposed duplicate."),
        base_update(6, identity_status="high_confidence", identity_evidence="The rare full initials, Swedish note, major rank, and Swedish biographical record for Gösta C. F. Wetterhall align.", name_variants=["Gosta C.F. Wetterhall", "Gösta C. F. Wetterhall", "Gösta Wetterhall"], replace_name_variants=True, personnel_category="foreign_or_allied_military_personnel", commissioned_officer=True, allied_or_foreign_personnel=True, research_status="completed", archival_review_priority="critical", next_action="Review the Box 829 personnel file to establish Wetterhall's exact relationship to OSS and the sequence of his Swedish assignments."),
        base_update(12, identity_status="high_confidence", identity_evidence="The distinctive exact name and the Hoover finding aid's 1943-1945 Army-service chronology connect the indexed person to economist Nathaniel Weyl.", research_status="completed", archival_review_priority="critical", next_action="Review the Box 829 personnel file to establish the exact Army-to-OSS assignment and test whether the Board of Economic Warfare was the immediate civilian predecessor to OSS."),
        base_update(24, identity_status="conflicting", identity_evidence="Two Army bulk records carry the same exact name and protected index identifier but disagree on Army-entry date and civilian-occupation code.", personnel_category="enlisted_army_personnel", commissioned_officer=False, research_status="conflicting_sources", archival_review_priority="critical", nara_catalog_id="1263923", next_action="Review the Box 829 personnel file and original Army source context to resolve the two official bulk records before publishing any occupation."),
        base_update(29, identity_status="high_confidence", identity_evidence="The exact Donald N. Wheeler name and institutional memorial's expanded middle name and direct OSS chief-economist role align.", name_variants=["Donald N Wheeler", "Donald Niven Wheeler"], replace_name_variants=True, personnel_category="civilian_professional_or_administrative_grade", commissioned_officer=False, research_status="completed", archival_review_priority="critical", next_action="Review the Box 829 personnel file to identify Wheeler's intervening Washington employment and determine the immediate pre-OSS affiliation and last civilian employer."),
        {"person_id": REVERSED_ELKINS_ID, "identity_status": "ambiguous", "identity_evidence": "The page-134 Wetherill Elkins row may be a transposition of the separately indexed Captain Elkins Wetherill, but it lacks the page-499 protected identifier and remains a separate entity pending file review.", "manual_review_required": True, "possible_duplicate_group": "transposition:elkins-wetherill", "research_status": "needs_identity_review", "next_action": "Compare the Box 216 and Box 829 personnel files before merging or rejecting the transposed-name hypothesis.", "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "critical"},
    ])
    if len(values) != len(PEOPLE) + 1:
        raise RuntimeError(f"Expected {len(PEOPLE) + 1} person updates, generated {len(values)}")
    return values


def research_attempts() -> list[dict[str, object]]:
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        if row in ARMY_MATCHES:
            item = ARMY_MATCHES[row]
            outcome, reviewed, rejected = "source_reviewed", 9, 5
            note = f"A reviewed exact-name, protected-identifier Army bridge supports identity and a qualified {item['occupation']} category at Army entry; no named employer, institution, workplace, or OSS-transfer date is supplied."
        elif row == 2:
            outcome, reviewed, rejected = "source_reviewed", 12, 6
            note = "An institutional biography directly documents Penn student status, 1941 activation with First Troop Philadelphia Cavalry, Signal Corps, and OSS service; exact transfer sequence remains unresolved."
        elif row == 6:
            outcome, reviewed, rejected = "source_reviewed", 11, 6
            note = "A visually inspected Swedish biographical entry and regimental history support the identity, 1938-1943 military teaching, and a qualified 1944-1945 command assignment."
        elif row == 12:
            outcome, reviewed, rejected = "source_reviewed", 11, 5
            note = "The Hoover finding aid gives a date-bounded federal economist chronology ending in Board of Economic Warfare work immediately before 1943-1945 Army service."
        elif row == 24:
            outcome, reviewed, rejected = "source_reviewed", 10, 6
            note = "Two official Army bulk records agree on exact name and protected identifier but conflict on entry date and occupation; neither occupation is published."
        elif row == 29:
            outcome, reviewed, rejected = "source_reviewed", 11, 6
            note = "A Reed College memorial expands the middle name, directly states five years as OSS chief economist, and documents earlier Yale teaching without proving immediacy."
        else:
            outcome, reviewed, rejected = "candidate_rejected", 7, 6
            note = unresolved_reason(row)
        attempts.append({
            "key": f"page499-row{row}-{slug(name)}-b1009",
            "person_id": person_id,
            "source_adapter": "manual_staged_protocol",
            "query_text": f"{name}; NARA OSS index context; CIA Reading Room, National Archives, and Library of Congress exact-name domain checks; exact-name and meaningful spelling, initial, suffix, punctuation, transliteration, and OCR variants; OSS, rank, branch, assignment, and identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory, and archival searches; indexed Box {box_for(row)}; protected identifiers used only in private official-record comparison",
            "query_variant_type": "staged_identity_employment_archival_protocol_batch_1009",
            "started_at": "2026-11-04T03:50:00Z",
            "completed_at": "2026-11-04T04:45:00Z",
            "outcome": outcome,
            "sources_reviewed": reviewed,
            "candidate_sources_rejected": rejected,
            "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, postwar-only leads, discovery-only biographies, and sources without an OSS, protected-identifier, rank, unit, or personnel-file bridge were rejected. Historical Army categories were not converted into named employers, workplaces, or institutions. Student status was not converted into employment.",
            "research_notes": f"{note} Exact-name official-domain, OSS, employer, occupation, obituary, biography, institutional, newspaper, directory, and archival searches were checked as applicable. NARA index page 499 and relevant evidence images were visually checked. No authenticated NARA Catalog API call was made.",
            "next_action": f"Review the indexed Box {box_for(row)} personnel file for corroborating identifiers, the immediate pre-OSS affiliation, and the last civilian employer before wartime service.",
            "attempt_number": 1,
            "research_agent_version": "before-oss-b1009-v1",
        })
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-1009-v1",
        "reviewer": "Before OSS Batch 1009 evidence review",
        "sources": sources(), "organizations": organizations(),
        "affiliations": affiliations(), "claims": claims(),
        "person_updates": person_updates(), "research_attempts": research_attempts(),
    }
    EvidenceBundle.model_validate(bundle)
    OUTPUT.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
