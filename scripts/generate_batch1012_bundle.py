#!/usr/bin/env python3
"""Generate the reviewed Batch 1012 evidence bundle for PDF page 502."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page502-whitley-to-wiener-review_"
    "batch-1012_2026-11-04.json"
)

INDEX = "nara-index-b1012"
ARMY = "army-bulk-b1012"
TECH = "army-tech-b1012"
CODES = "army-codes-b1012"
WHOS_WHO = "whos-who-thomas-whitney-b1012"
FSJ_1940 = "fsj-george-whittinghill-1940-b1012"
FSJ_1944 = "fsj-george-whittinghill-1944-b1012"
HOOVER = "hoover-oss-personnel-board-whittinghill-b1012"
CRIMSON = "harvard-crimson-whittlesey-b1012"
ACADEMY = "american-academy-whittlesey-b1012"

ORG_BENNETT = "bennett-college-unspecified-b1012"
ORG_STATE = "department-of-state-existing-b1012"
ORG_G2_POW = "g2-afhq-pow-section-b1012"
ORG_TIME = "time-inc-existing-b1012"
ORG_HARVARD = "harvard-existing-b1012"

PEOPLE = {
    1: ("7838874e-963c-5779-9f0f-052b2e87a620", "Jack Whitley"),
    2: ("db7520cb-4275-59a9-937b-70390dcfd5e9", "Flody C Whitlow"),
    3: ("70be42d4-9df1-5189-ad85-b559c44ada31", "Floyd C Whitlow"),
    4: ("9b7626c8-45d0-5cb0-8b5e-a8ab980bfca1", "Alain S Whitman"),
    5: ("5b21625a-1574-5e6a-8908-9015adef921c", "Elda Whitman"),
    6: ("bf76f3c6-a6aa-541f-b867-48ec63a8fc3e", "James L Whitman"),
    7: ("5dcda7f2-ca42-5496-8172-c3977437fb27", "James R Whitman"),
    8: ("dc2d945c-570f-5723-b27b-4f4e51f922f9", "Joe Whitman"),
    9: ("73cae803-0d8c-5461-9cc5-9baee05eeea8", "Marvin L Whitmer"),
    10: ("946bb265-5ef0-59ea-8da7-85dd2c21d22f", "Hamie L Whitmore"),
    11: ("dbdfbbb8-f3dc-5d95-815e-1de8a3798d66", "Alice Whitney"),
    12: ("ea14553b-c7e5-5f1c-950f-54161d1441f8", "Burke E Whitney"),
    13: ("dde0cd8f-aee1-5fa2-aaa7-b96bad191921", "Stephen Whitney"),
    14: ("ffb02d3b-860c-5391-9fc8-14b2a7630182", "Stephen Whitney"),
    15: ("91277af5-9982-59b9-ba32-db8c5ba278fe", "Thomas P Whitney"),
    16: ("74e0a6d6-7eec-518b-b850-d8bea49dc339", "William D Whitney"),
    17: ("227bcffa-5ff0-5f4d-99a3-e8ab46383f9a", "Charles W Whittaker"),
    18: ("ec6577b3-4b52-50c6-b2e2-3e137cfd10b2", "Lee Whittaker"),
    19: ("ee4576f2-9604-547e-9481-6dcdfef67f8a", "Frank H Whittemore"),
    20: ("ed72223d-e154-5da0-95b4-690d57ae2889", "Henry L Whittemore Jr."),
    21: ("d5f92db6-28db-5b37-9cd1-6fce3b67a68b", "Robert F Whitten"),
    22: ("f4c1c840-dee1-5968-a016-9d2d7cae193b", "Charles A Whittier"),
    23: ("412a907d-1dbf-5de6-828d-24f893a656e2", "George D Whittinghill"),
    24: ("a3079498-0b64-5e35-bb48-ecf2de04516e", "Robert B Whittinghill"),
    25: ("9fa0f8ff-40fe-5719-a157-532bcb46afe5", "Derwent Whittlesey"),
    26: ("8d95ec22-1b44-5079-a891-4f18761db83b", "Ivan D Whitver"),
    27: ("2c2de58d-6615-542f-9038-2fa14bd830dd", "Charles F Wible Jr."),
    28: ("e0aef62a-65d5-5ad9-8889-28b2436c3d4e", "Robert Wichmann"),
    29: ("2a068be3-dbc9-54e7-ae6d-0c1f52745884", "Frank J Wicichowski"),
    30: ("5bf43b23-92a8-5b64-ae7b-8b672e5a3b0c", "Norman C Wicker"),
    31: ("b0839f15-2b3c-587b-a93c-4690809b6da0", "Norman E Wicker"),
    32: ("ee7d8330-1d97-57f9-b53f-e15bdf91945e", "Eleanor E Wickert"),
    33: ("df2f5b71-5523-57ff-ab69-480d2e9d61c6", "George A Wickes"),
    34: ("53f28d57-a6a5-56f2-8c4d-11db2bb46d86", "John A Wickham"),
    35: ("019f50f9-50a3-51aa-9069-50cd1685e0e2", "Richard V Wickham"),
    36: ("cd75f4b2-34ac-5131-ae2c-2404ac4aa3ac", "Jeannette Wicks"),
    37: ("6360e3d0-4a67-500b-a484-f3a9a0ca6364", "Walter F Wicks"),
    38: ("f288f7ea-401e-5d56-8a21-a3c1f2567c4f", "Donald R Widman"),
    39: ("03e5f5f3-37a4-54ec-aa9e-6ba1c600b8e0", "Frederick J Widmayer"),
    40: ("91a4ff2a-58a5-541a-a684-cb8030536b0f", "Dean R Widrig"),
    41: ("0a3f6f92-1312-590d-b7de-5b28b9ea8228", "Howard Wiedemann"),
    42: ("6712cfeb-a2cd-5299-96da-2e4624a7e396", "Hermann C Wiegert"),
    43: ("419a4fe6-8242-5019-a86d-1adf5ad8ce69", "Clarion B Wiener"),
    44: ("e738ef02-1123-5431-9403-b2f396a69e2c", "Irene P Wiener"),
    45: ("7c128775-a49f-52b3-b2ea-9983ed87bdeb", "Louis L Wiener"),
    46: ("54d06d0f-f16d-5578-aec9-3ead65fe5c79", "Max Wiener"),
}

ARMY_MATCHES = {
    6: {"date": "1942-01-12", "code": "819", "occupation": "unskilled textile-manufacturing worker, not elsewhere classified", "label": "Unskilled occupations in manufacture of textiles, n.e.c.", "locator": "PDF physical page 176; historical category 8-19"},
    8: {"date": "1942-06-23", "code": "185", "occupation": "salesman or sales agent, except sales to consumers", "label": "Salesmen and sales agents, except to consumers", "locator": "PDF physical page 172; historical category 1-85"},
    14: {"date": "1943-09-14", "code": "031", "occupation": "secondary-school teacher or principal", "label": "Teachers, secondary schools, and principals", "locator": "PDF physical page 171; historical category 0-31"},
    18: {"date": "1943-04-05", "code": "580", "occupation": "airplane mechanic or repairman", "label": "Airplane mechanics and repairmen", "locator": "PDF physical page 174; historical category 5-80"},
    19: {"date": "1942-12-17", "code": "022", "occupation": "lawyer or judge", "label": "Lawyers and judges", "locator": "PDF physical page 171; historical category 0-22", "identity": "high_confidence"},
    20: {"date": "1942-08-14", "code": "031", "occupation": "secondary-school teacher or principal", "label": "Teachers, secondary schools, and principals", "locator": "PDF physical page 171; historical category 0-31"},
    27: {"date": "1943-04-27", "code": "992", "occupation": "student", "label": "Students", "locator": "PDF physical page 304; amended historical category 9-92"},
    29: {"date": "1943-03-11", "code": "963", "occupation": "unskilled nonprocess manufacturing worker, not elsewhere classified", "label": "Unskilled nonprocess occupations in manufacturing, n.e.c.", "locator": "PDF physical page 177; historical category 9-63"},
    33: {"date": "1943-07-14", "code": "992", "occupation": "student", "label": "Students", "locator": "PDF physical page 304; amended historical category 9-92"},
    38: {"date": "1941-02-25", "code": "006", "occupation": "author, editor, or reporter", "label": "Authors, editors, and reporters", "locator": "PDF physical page 171; historical category 0-06"},
    40: {"date": "1942-12-09", "code": "553", "occupation": "telegraph, telephone, or power lineman or serviceman", "label": "Telegraph, telephone, and power linemen and servicemen", "locator": "PDF physical page 174; historical category 5-53"},
}

SPECIAL_ROWS = {15, 23, 24, 25}
CONFLICT_ROW = 17


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def box_for(row: int) -> str:
    if row <= 4:
        return "833"
    if row <= 26:
        return "834"
    return "835"


def occupation_key(row: int) -> str:
    return f"{slug(PEOPLE[row][1])}-army-occupation-row{row}-b1012"


def sources() -> list[dict[str, object]]:
    return [
        {"key": INDEX, "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf", "archival_identifier": "RG 226, Entry A1-224, Boxes 833-835", "title": "OSS Personnel Files from Excel", "author_creator": "National Archives and Records Administration", "repository_publisher": "National Archives and Records Administration", "publication_record_date": "2010-12-23", "locator": "PDF page 502, rows 1-46; visually checked against a 180 dpi render", "access_date": "2026-11-04", "source_quality": "A_direct_official", "collection_name": "Records of the Office of Strategic Services, Record Group 226", "rights_notes": "All 46 printed rows remain separate. Original spelling is preserved; full service or officer identifiers remain private."},
        {"key": ARMY, "stable_url": "https://catalog.archives.gov/id/1263923", "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357", "title": "Electronic Army Serial Number Merged File, ca. 1938-1946", "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration", "repository_publisher": "National Archives and Records Administration", "publication_record_date": "1938-1946; merged file created 2002", "locator": "Official unrestricted ASNEF.FIN.DAT; 11 accepted and one conflicting protected-identifier comparisons; identifiers and raw rows withheld", "access_date": "2026-11-04", "source_quality": "A_direct_official", "collection_name": "World War II Army Enlistment Records", "document_number": "ASNEF.FIN.DAT", "rights_notes": "Army-entry occupation categories are not named employers, institutions, or exact OSS-transfer records. The Charles W. Whitaker or Whittaker conflict remains unresolved."},
        {"key": TECH, "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf", "archival_identifier": "NN3-064-03-008; National Archives Identifier 1263923", "title": "World War II Army Enlistment Records: Reference Copy of Technical Documentation", "author_creator": "National Archives and Records Administration", "repository_publisher": "National Archives at College Park - Electronic Records", "publication_record_date": "1994-2005; reference copy modified 2011", "locator": "PDF physical pages 44-46; fixed-width identifier, name, entry-date, grade, and civilian-occupation fields", "access_date": "2026-11-04", "source_quality": "A_direct_official", "collection_name": "World War II Army Enlistment Records technical documentation"},
        {"key": CODES, "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1CL_SD.pdf", "archival_identifier": "National Archives Identifier 1263923; Code No. 30", "title": "NARA Compiled Code Lists for the Electronic Army Serial Number Merged File", "author_creator": "National Archives and Records Administration", "repository_publisher": "National Archives at College Park - Electronic Records", "publication_record_date": "2011-01-12; modified 2011-03-17", "locator": "PDF physical pages 171-177 and 304; relevant categories visually inspected", "access_date": "2026-11-04", "source_quality": "A_direct_official", "collection_name": "World War II Army Enlistment Records technical documentation", "rights_notes": "Historical categories are published with their limits and never converted into a named employer or institution."},
        {"key": WHOS_WHO, "stable_url": "https://whitlock.one-name.net/references/page07/R1102.pdf", "archival_identifier": "Who's Who in the World, 6th edition, page 1141", "title": "Who's Who in the World, 1982-1983: Thomas Porter Whitney", "author_creator": "Marquis Who's Who", "repository_publisher": "Marquis Who's Who; digital excerpt hosted by the Whitlock Family One-Name Study", "publication_record_date": "1982-1983", "locator": "Printed page 1141; Thomas Porter Whitney entry; visually inspected", "access_date": "2026-11-04", "source_quality": "C_reputable_contemporary_or_scholarly", "rights_notes": "A later biographical directory is used for the specific pre-OSS chronology. The source says Bennett College but does not identify which institution of that name."},
        {"key": FSJ_1940, "stable_url": "https://afsa.org/sites/default/files/fsj-1940-11-november_0.pdf", "archival_identifier": "The American Foreign Service Journal, volume 17, number 11", "title": "The American Foreign Service Journal, November 1940", "author_creator": "American Foreign Service Association", "repository_publisher": "American Foreign Service Association", "publication_record_date": "1940-11", "locator": "PDF physical page 39; printed page 633; Foreign Service personnel notice; visually inspected", "access_date": "2026-11-04", "source_quality": "B_authoritative_institutional", "collection_name": "The American Foreign Service Journal"},
        {"key": FSJ_1944, "stable_url": "https://afsa.org/sites/default/files/fsj-1944-12-december_0.pdf", "archival_identifier": "The American Foreign Service Journal, volume 21, number 12", "title": "The American Foreign Service Journal, December 1944", "author_creator": "American Foreign Service Association", "repository_publisher": "American Foreign Service Association", "publication_record_date": "1944-12", "locator": "PDF physical page 43; printed page 685; Foreign Service personnel in the armed services; visually inspected", "access_date": "2026-11-04", "source_quality": "B_authoritative_institutional", "collection_name": "The American Foreign Service Journal"},
        {"key": HOOVER, "stable_url": "https://digitalcollections.hoover.org/internal/media/dispatcher/331573/full", "archival_identifier": "Hoover digital media 331573", "title": "Office of Strategic Services Personnel Board Report, Caserta", "author_creator": "Office of Strategic Services", "repository_publisher": "Hoover Institution Library & Archives", "publication_record_date": "1944-05-04 through 1944-05-24", "locator": "PDF physical page 51; printed page 52; entry XXX for 1st Lieutenant Robert B. Whittinghill", "access_date": "2026-11-04", "source_quality": "A_direct_official", "collection_name": "Office of Strategic Services records", "rights_notes": "The complete official report was read through the repository's indexed PDF text after the binary endpoint denied or timed out direct local download. Only concise project-authored notes and short excerpts are retained."},
        {"key": CRIMSON, "stable_url": "https://www.thecrimson.com/article/1956/11/26/well-known-geographer-derwent-whittlesey-dies-pderwent/", "archival_identifier": "The Harvard Crimson, 1956-11-26", "title": "Well-Known Geographer Derwent Whittlesey Dies", "author_creator": "The Harvard Crimson", "repository_publisher": "The Harvard Crimson", "publication_record_date": "1956-11-26", "locator": "Obituary paragraphs 1-3; Harvard appointment and promotion chronology", "access_date": "2026-11-04", "source_quality": "B_authoritative_institutional", "rights_notes": "The institutional obituary documents Harvard employment from 1928 and promotion in 1943; it does not establish an immediate transition into OSS."},
        {"key": ACADEMY, "stable_url": "https://www.amacad.org/person/derwent-stainthorpe-whittlesey", "archival_identifier": "American Academy member profile", "title": "Derwent Stainthorpe Whittlesey", "author_creator": "American Academy of Arts and Sciences", "repository_publisher": "American Academy of Arts and Sciences", "publication_record_date": "Profile last updated 2025-04", "locator": "Member profile: full name, Harvard University, geographer and educator", "access_date": "2026-11-04", "source_quality": "B_authoritative_institutional"},
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {"key": ORG_BENNETT, "canonical_name": "Bennett College (institution unspecified)", "historical_name": "Bennett College", "aliases": [], "organization_type": "college (institution unspecified)", "sector": "academia_and_research", "country": "United States", "normalization_notes": "The biographical source does not distinguish Bennett College in Greensboro from Bennett College in Millbrook. The record is intentionally not merged with either institution."},
        {"key": ORG_STATE, "organization_id": "4d2fbb5f-218d-5445-b7b3-4c2fd22f0286", "canonical_name": "United States Department of State", "historical_name": "Department of State", "aliases": ["U.S. Department of State", "Foreign Service of the United States"], "organization_type": "federal executive department", "sector": "federal_government", "city": "Washington", "state_or_region": "District of Columbia", "country": "United States", "normalization_notes": "Existing canonical department reused. Foreign Service work is modeled as a government assignment, not private employment."},
        {"key": ORG_G2_POW, "canonical_name": "Prisoner of War Section, G-2, Allied Force Headquarters", "historical_name": "Prisoner of War Section of G-2, AFHQ", "aliases": ["POW Section, G-2, AFHQ"], "organization_type": "military intelligence section", "sector": "military", "country": "Allied Force Headquarters", "active_dates": "World War II", "normalization_notes": "Preserved as a distinct wartime assignment. It is not collapsed into the OSS or a generic United States Army organization."},
        {"key": ORG_TIME, "organization_id": "a33daa04-06e0-5837-86e2-daf4909b1e45", "canonical_name": "Time, Inc.", "historical_name": "Time, Inc.", "aliases": ["Time Inc."], "organization_type": "magazine publisher", "sector": "journalism_and_media", "country": "United States", "normalization_notes": "Existing canonical publisher reused. Source wording such as Time magazine remains on each affiliation; magazine titles are not silently substituted for the employer."},
        {"key": ORG_HARVARD, "organization_id": "45ddf347-21c6-59f5-a8ae-517418adf941", "canonical_name": "Harvard University", "historical_name": "Harvard University", "aliases": ["Harvard"], "organization_type": "university", "sector": "academia_and_research", "city": "Cambridge", "state_or_region": "Massachusetts", "country": "United States", "normalization_notes": "Employment and student relationships are modeled separately."},
    ]


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, item in ARMY_MATCHES.items():
        identity = item.get("identity", "confirmed")
        values.append({
            "key": occupation_key(row),
            "person_id": PEOPLE[row][0],
            "occupation": item["occupation"],
            "relationship_type": "student" if item["code"] == "992" else "unknown",
            "end_date": item["date"],
            "date_precision": f"Historical civilian-occupation code {item['code']} was recorded at Army entry on {item['date']}; no named employer or institution is supplied.",
            "country": "United States",
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": identity,
            "claim_confidence": "medium",
            "source_quality": "A_direct_official",
            "publication_status": "publish_qualified",
            "research_notes": "Broad historical category only; no named employer, workplace, school, publication, firm, court, or exact OSS transition is inferred.",
        })
    values.extend([
        {"key": "thomas-whitney-bennett-b1012", "person_id": PEOPLE[15][0], "organization_key": ORG_BENNETT, "organization_name_as_found": "Bennett College", "role_title": "instructor of social sciences", "occupation": "educator", "relationship_type": "employment", "start_date": "1940", "end_date": "1941", "date_precision": "The directory gives 1940-1941, immediately followed by OSS social-science work beginning in 1941; exact days and which Bennett College are not identified.", "country": "United States", "immediate_pre_oss": True, "last_civilian_pre_service": True, "pre_oss_temporal_basis": "strongly_date_bounded", "identity_confidence": "high_confidence", "claim_confidence": "high", "source_quality": "C_reputable_contemporary_or_scholarly", "publication_status": "published", "research_notes": "The exact distinctive full name and explicit Bennett-to-OSS chronology support the match. The historical institution remains unresolved rather than guessed."},
        {"key": "george-whittinghill-state-b1012", "person_id": PEOPLE[23][0], "organization_key": ORG_STATE, "organization_name_as_found": "American Clerk at Milan; American Vice Consul at Lyon", "role_title": "American Clerk; appointed American Vice Consul", "relationship_type": "government_assignment", "end_date": "1940-11", "date_precision": "A November 1940 personnel notice documents the State assignment; a December 1944 Foreign Service roster lists him in the Army. An intervening civilian role cannot be ruled out.", "country": "United States Foreign Service", "last_civilian_pre_service": True, "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "high_confidence", "claim_confidence": "medium", "source_quality": "B_authoritative_institutional", "publication_status": "publish_qualified", "research_notes": "Published as the latest currently documented civilian government affiliation before the Army, not as an explicit immediate transition to OSS."},
        {"key": "robert-whittinghill-g2-pow-b1012", "person_id": PEOPLE[24][0], "organization_key": ORG_G2_POW, "organization_name_as_found": "Prisoner of War Section of G-2, AFHQ", "role_title": "Prisoner of War Section staff; order-of-battle work after transfer", "relationship_type": "military_assignment", "end_date": "1943-11", "date_precision": "The official report explicitly states that he was assigned to OSS from this section in November 1943.", "country": "Allied Force Headquarters", "immediate_pre_oss": True, "pre_oss_temporal_basis": "explicit_immediate", "identity_confidence": "confirmed", "claim_confidence": "confirmed", "source_quality": "A_direct_official", "publication_status": "published", "research_notes": "Direct official transition evidence; this is a military assignment, not a civilian employer."},
        {"key": "robert-whittinghill-time-b1012", "person_id": PEOPLE[24][0], "organization_key": ORG_TIME, "organization_name_as_found": "Time magazine", "relationship_type": "employment", "end_date": "1941-07", "date_precision": "The official report says this was civilian work before he entered the Army in July 1941; it does not establish the order relative to his teaching job.", "country": "Italy and France", "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "confirmed", "claim_confidence": "confirmed", "source_quality": "A_direct_official", "publication_status": "published", "research_notes": "The source names the employer but not the role or exact dates. It is not labeled the last civilian employer because the sequence of the two civilian jobs is unknown."},
        {"key": "robert-whittinghill-private-school-b1012", "person_id": PEOPLE[24][0], "organization_name_as_found": "a private school near Cornell", "role_title": "teacher of French and Italian", "occupation": "teacher", "relationship_type": "employment", "end_date": "1941-07", "date_precision": "The official report says this was civilian work before Army entry in July 1941; the school and exact dates are not named.", "state_or_region": "New York", "country": "United States", "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "confirmed", "claim_confidence": "confirmed", "source_quality": "A_direct_official", "publication_status": "published", "research_notes": "The employer remains unnamed. The job is not labeled last civilian employment because its sequence relative to Time magazine is unknown."},
        {"key": "derwent-whittlesey-harvard-b1012", "person_id": PEOPLE[25][0], "organization_key": ORG_HARVARD, "organization_name_as_found": "Harvard", "role_title": "professor of geography", "occupation": "geographer and educator", "relationship_type": "employment", "start_date": "1928", "date_precision": "The institutional obituary says he came to Harvard in 1928 and became a full professor in 1943; it does not document an OSS transition.", "city": "Cambridge", "state_or_region": "Massachusetts", "country": "United States", "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "high_confidence", "claim_confidence": "high", "source_quality": "B_authoritative_institutional", "publication_status": "published", "research_notes": "A distinctive full name and two institutional profiles establish the Harvard affiliation. Wartime government consultancy is context only and is not converted into an OSS assignment."},
    ])
    return values


def make_claim(*, key: str, row: int, claim_type: str, text: str, paraphrase: str,
               identity: str, temporal: str, quality: str, confidence: str,
               publication: str, notes: str, source_links: list[dict[str, str]],
               affiliation_key: str | None = None) -> dict[str, object]:
    value: dict[str, object] = {
        "key": key,
        "person_id": PEOPLE[row][0],
        "claim_type": claim_type,
        "claim_text": text,
        "evidence_paraphrase": paraphrase,
        "identity_match_assessment": identity,
        "temporal_assessment": temporal,
        "source_quality": quality,
        "claim_confidence": confidence,
        "publication_status": publication,
        "match_notes": notes,
        "sources": source_links,
    }
    if affiliation_key:
        value["affiliation_key"] = affiliation_key
    return value


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, item in ARMY_MATCHES.items():
        name = PEOPLE[row][1]
        high_identity = row == 19
        identity_confidence = "high" if high_identity else "confirmed"
        identity_assessment = (
            "A nonshared protected identifier and matching given name and middle initial support the record; the Army surname omits the initial W and prints HITTEMORE."
            if high_identity else
            "Confirmed by an exact-name, nonshared protected-identifier match; the identifier remains private."
        )
        identity_text = (
            "Frank H. Whittemore is a high-confidence match to the Army record despite its HITTEMORE surname spelling."
            if high_identity else
            f"Indexed {name} is confirmed as the matching Army record by exact name and a nonshared protected identifier."
        )
        values.append(make_claim(
            key=f"identity-{slug(name)}-row{row}-b1012",
            row=row,
            claim_type="identity",
            text=identity_text,
            paraphrase="The official OSS index and Army bulk record agree on a nonshared private identifier; the identifier is withheld from public data.",
            identity=identity_assessment,
            temporal=f"The Army record is dated {item['date']}; it supports identity but does not establish the exact Army-to-OSS sequence.",
            quality="A_direct_official",
            confidence=identity_confidence,
            publication="published",
            notes="The historical occupation field is handled in a separate qualified claim and never converted into a named employer.",
            source_links=[
                {"source_key": INDEX, "locator_override": f"PDF page 502 row {row}; protected identifier withheld"},
                {"source_key": ARMY, "locator_override": f"Army entry {item['date']}; protected identifier and bulk ordinal withheld"},
                {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46"},
            ],
        ))
        values.append(make_claim(
            key=f"occupation-{slug(name)}-row{row}-b1012",
            row=row,
            claim_type="occupation",
            text=f"At Army entry on {item['date']}, {name} was recorded in the historical {item['occupation']} category; no named employer or institution is identified.",
            paraphrase=f"The accepted Army record carries civilian-occupation code {item['code']}, decoded from NARA's official code list.",
            identity=identity_assessment,
            temporal="Strongly date-bounded to Army entry; it does not establish the immediate pre-OSS affiliation or a named employer.",
            quality="A_direct_official",
            confidence="medium",
            publication="publish_qualified",
            notes="Published with its limits and excluded from verified-employer analytics.",
            source_links=[
                {"source_key": ARMY, "locator_override": f"Army entry {item['date']}; civilian occupation code {item['code']}; protected identifier withheld"},
                {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46"},
                {"source_key": CODES, "locator_override": item["locator"], "excerpt_override": item["label"]},
            ],
            affiliation_key=occupation_key(row),
        ))

    values.extend([
        make_claim(key="identity-charles-whittaker-conflict-b1012", row=17, claim_type="identity", text="The page-502 Charles W. Whittaker and page-500 Charles W. Whitaker records share a protected identifier, but their printed surname spellings conflict and they remain separate.", paraphrase="The Army record uses WHITAKER, while the two index rows have distinct surname spellings; no occupation or chronology is assigned to either as settled fact.", identity="Conflicting. The protected identifier is not unique across the two printed index rows, so it cannot resolve the spelling or entity assignment.", temporal="The Army record cannot be assigned to either index entity as settled pre-OSS evidence.", quality="A_direct_official", confidence="conflicting", publication="conflicting", notes="Both source rows and person entities remain visible in the protected conflict group; the private identifier is never published.", source_links=[{"source_key": INDEX, "locator_override": "PDF pages 500 and 502; Charles W. Whitaker and Charles W. Whittaker rows; protected identifier withheld"}, {"source_key": ARMY, "support_type": "contradicts", "locator_override": "Army surname WHITAKER; protected identifier withheld"}]),
        make_claim(key="identity-thomas-porter-whitney-b1012", row=15, claim_type="identity", text="Thomas P. Whitney is identified at high confidence as Thomas Porter Whitney, a Bennett College instructor and OSS social-science analyst.", paraphrase="A specific biographical directory gives the full name and the sequence from Bennett College in 1940-1941 to OSS in 1941-1944.", identity="High confidence from the distinctive exact name, middle initial, and explicit OSS chronology; the personnel file remains unreviewed.", temporal="The directory gives consecutive 1940-1941 and 1941-1944 roles.", quality="C_reputable_contemporary_or_scholarly", confidence="high", publication="published", notes="The institution called Bennett College is not silently resolved to a campus that the source does not identify.", source_links=[{"source_key": INDEX, "locator_override": "PDF page 502 row 15"}, {"source_key": WHOS_WHO, "locator_override": "Printed page 1141", "excerpt_override": "Instr. social scis. Bennett Coll., 1940-41; social sci. analyst OSS, Washington, 1941-44"}]),
        make_claim(key="immediate-thomas-whitney-bennett-b1012", row=15, claim_type="immediate_pre_oss_affiliation", text="Thomas Porter Whitney taught social sciences at an institution named Bennett College in 1940-1941 immediately before documented OSS work beginning in 1941.", paraphrase="The directory places the Bennett College role directly before his OSS social-science analyst service.", identity="High-confidence distinctive-name match with an explicit OSS chronology.", temporal="Strongly date-bounded; the source gives consecutive years but not exact transition dates.", quality="C_reputable_contemporary_or_scholarly", confidence="high", publication="published", notes="Which Bennett College is unresolved and is made explicit in the organization record.", source_links=[{"source_key": WHOS_WHO, "locator_override": "Printed page 1141", "excerpt_override": "Instr. social scis. Bennett Coll., 1940-41; social sci. analyst OSS, Washington, 1941-44"}], affiliation_key="thomas-whitney-bennett-b1012"),
        make_claim(key="last-civilian-thomas-whitney-bennett-b1012", row=15, claim_type="last_civilian_pre_service", text="Bennett College is the last documented civilian employer before Thomas Porter Whitney's OSS service in the reviewed source.", paraphrase="The biographical chronology lists Bennett College in 1940-1941 and OSS immediately afterward in 1941-1944.", identity="High-confidence distinctive-name match with an explicit OSS chronology.", temporal="Strongly date-bounded; no intervening role is shown, but exact transition dates are unavailable.", quality="C_reputable_contemporary_or_scholarly", confidence="high", publication="published", notes="The employer wording is preserved while the exact Bennett institution remains unresolved.", source_links=[{"source_key": WHOS_WHO, "locator_override": "Printed page 1141", "excerpt_override": "Instr. social scis. Bennett Coll., 1940-41; social sci. analyst OSS, Washington, 1941-44"}], affiliation_key="thomas-whitney-bennett-b1012"),
        make_claim(key="identity-george-whittinghill-b1012", row=23, claim_type="identity", text="George D. Whittinghill is a high-confidence match to the Foreign Service officer documented in 1940 and listed in the Army in 1944.", paraphrase="Two institutional Foreign Service Journal notices use the same rare exact name and give a coherent prewar Foreign Service and wartime Army chronology.", identity="High confidence from a rare exact full name and two independent date-specific institutional notices; no protected identifier bridge is available.", temporal="The notices date the Foreign Service role to 1940 and Army status to 1944.", quality="B_authoritative_institutional", confidence="high", publication="published", notes="The evidence supports the identity and documented chronology but not a precise OSS transfer date.", source_links=[{"source_key": INDEX, "locator_override": "PDF page 502 row 23"}, {"source_key": FSJ_1940, "locator_override": "PDF physical page 39; printed page 633", "excerpt_override": "George D. Whittinghill of New York, American Clerk at Milan, Italy"}, {"source_key": FSJ_1944, "locator_override": "PDF physical page 43; printed page 685", "excerpt_override": "Whittinghill, George D. — Army"}]),
        make_claim(key="last-civilian-george-whittinghill-state-b1012", row=23, claim_type="last_civilian_pre_service", text="The United States Department of State is the latest civilian government institution currently documented for George D. Whittinghill before his wartime Army service.", paraphrase="A 1940 notice identifies his clerk and vice-consular work; a 1944 institutional roster lists him in the Army.", identity="High-confidence rare-name match across the index and two institutional notices.", temporal="Documented prewar and qualified as the latest currently found role; the four-year evidence gap does not rule out an intervening affiliation.", quality="B_authoritative_institutional", confidence="medium", publication="publish_qualified", notes="The claim is excluded from immediate-affiliation analytics and remains subject to Box 834 review.", source_links=[{"source_key": FSJ_1940, "locator_override": "PDF physical page 39; printed page 633", "excerpt_override": "American Clerk at Milan, Italy, has been appointed American Vice Consul at Lyon, France"}, {"source_key": FSJ_1944, "support_type": "context_only", "locator_override": "PDF physical page 43; printed page 685", "excerpt_override": "Whittinghill, George D. — Army"}], affiliation_key="george-whittinghill-state-b1012"),
        make_claim(key="identity-robert-whittinghill-b1012", row=24, claim_type="identity", text="The indexed Robert B. Whittinghill is confirmed as the first lieutenant described in the May 1944 OSS Personnel Board report.", paraphrase="The exact name and private officer identifier agree between the index and official report; the identifier is withheld.", identity="Confirmed by exact name and a matching protected identifier in two official OSS records.", temporal="The report documents Army entry in 1941, commission in 1942, and OSS assignment in November 1943.", quality="A_direct_official", confidence="confirmed", publication="published", notes="Direct official evidence connects the person, military chronology, immediate assignment, and two civilian jobs.", source_links=[{"source_key": INDEX, "locator_override": "PDF page 502 row 24; protected identifier withheld"}, {"source_key": HOOVER, "locator_override": "PDF physical page 51; printed page 52; entry XXX; protected identifier withheld", "excerpt_override": "1st Lieutenant Robert B. Whittinghill"}]),
        make_claim(key="immediate-robert-whittinghill-g2-pow-b1012", row=24, claim_type="immediate_pre_oss_affiliation", text="Robert B. Whittinghill was assigned to OSS from the Prisoner of War Section of G-2, Allied Force Headquarters, in November 1943.", paraphrase="The official OSS report explicitly names the section from which he was transferred and the month of assignment.", identity="Confirmed by exact name and matching protected identifier.", temporal="Explicit immediate transition in November 1943.", quality="A_direct_official", confidence="confirmed", publication="published", notes="Modeled as a military assignment, not a civilian employer.", source_links=[{"source_key": HOOVER, "locator_override": "PDF physical page 51; printed page 52; entry XXX", "excerpt_override": "Assigned to OSS from Prisoner of War Section of G-2, AFHQ"}], affiliation_key="robert-whittinghill-g2-pow-b1012"),
        make_claim(key="employment-robert-whittinghill-time-b1012", row=24, claim_type="other_pre_oss_affiliation", text="Before entering the Army, Robert B. Whittinghill worked for Time magazine in Italy and France.", paraphrase="The official OSS report names Time magazine and the countries of employment but does not give his role or dates.", identity="Confirmed by exact name and matching protected identifier.", temporal="Documented civilian work before Army entry in July 1941; not shown to be the immediate pre-OSS or last civilian role.", quality="A_direct_official", confidence="confirmed", publication="published", notes="The sequence relative to his private-school teaching is unknown, so neither is labeled the last civilian employer.", source_links=[{"source_key": HOOVER, "locator_override": "PDF physical page 51; printed page 52; entry XXX", "excerpt_override": "worked for Time magazine in Italy and France"}], affiliation_key="robert-whittinghill-time-b1012"),
        make_claim(key="employment-robert-whittinghill-private-school-b1012", row=24, claim_type="other_pre_oss_affiliation", text="Before entering the Army, Robert B. Whittinghill taught French and Italian at an unnamed private school near Cornell.", paraphrase="The official OSS report documents the subjects and approximate location but does not name the school or dates.", identity="Confirmed by exact name and matching protected identifier.", temporal="Documented civilian work before Army entry in July 1941; not shown to be the immediate pre-OSS or last civilian role.", quality="A_direct_official", confidence="confirmed", publication="published", notes="The employer remains explicitly unnamed and is not normalized to Cornell University.", source_links=[{"source_key": HOOVER, "locator_override": "PDF physical page 51; printed page 52; entry XXX", "excerpt_override": "taught French and Italian in a private school near Cornell"}], affiliation_key="robert-whittinghill-private-school-b1012"),
        make_claim(key="identity-derwent-whittlesey-b1012", row=25, claim_type="identity", text="Derwent Whittlesey is identified at high confidence as Derwent Stainthorpe Whittlesey, the Harvard geographer and educator.", paraphrase="The rare name, institutional profile, and Harvard obituary agree on the full name, profession, institution, and chronology.", identity="High confidence from a distinctive name and two authoritative institutional sources; the indexed personnel file remains unreviewed.", temporal="The Harvard chronology begins in 1928 and documents full-professor status in 1943.", quality="B_authoritative_institutional", confidence="high", publication="published", notes="Wartime consultancy mentioned in the obituary is not converted into a specific OSS assignment.", source_links=[{"source_key": INDEX, "locator_override": "PDF page 502 row 25"}, {"source_key": ACADEMY, "locator_override": "Member profile", "excerpt_override": "Derwent Stainthorpe Whittlesey; Harvard University; Geographer; Educator"}, {"source_key": CRIMSON, "locator_override": "Obituary paragraphs 1-3", "excerpt_override": "Derwent S. Whittlesey, professor of Geography"}]),
        make_claim(key="employment-derwent-whittlesey-harvard-b1012", row=25, claim_type="other_pre_oss_affiliation", text="Derwent Stainthorpe Whittlesey joined Harvard in 1928 and was a full professor of geography by 1943.", paraphrase="Harvard's institutional obituary provides the appointment and promotion chronology; the Academy profile independently confirms Harvard and his profession.", identity="High-confidence distinctive-name match supported by two authoritative institutional sources.", temporal="Documented prewar employment; the sources do not establish that Harvard was his immediate pre-OSS affiliation.", quality="B_authoritative_institutional", confidence="high", publication="published", notes="Published as documented prewar employment and excluded from immediate-affiliation analytics.", source_links=[{"source_key": CRIMSON, "locator_override": "Obituary paragraphs 1-3", "excerpt_override": "In 1928 he came to Harvard and was made a full professor in 1943."}, {"source_key": ACADEMY, "support_type": "context_only", "locator_override": "Member profile", "excerpt_override": "Harvard University; Geographer; Educator"}], affiliation_key="derwent-whittlesey-harvard-b1012"),
    ])
    return values


def unresolved_reason(row: int) -> str:
    prefix = {
        1: "English footballer and modern legal-professional namesakes were rejected as unrelated. ",
        3: "A 1955 Congressional Record reference to a Major Floyd C. Whitlow lacks an OSS, Box 833, or protected-identifier bridge and remains unassigned. ",
        7: "Multiple James R. Whitman namesakes lacked a second corroborating identifier. ",
        10: "A rare-name veterans-cemetery lead for Hamie L. Whitmore lacks an OSS, Box 834, or protected-identifier bridge and remains unassigned. ",
        13: "This printed first-lieutenant Stephen Whitney row remains separate from the no-rank namesake matched to an Army enlistment record. ",
        21: "Cemetery and obituary namesakes lacked a Box 834 or OSS bridge. ",
        22: "World War I veteran and other namesake leads lacked a Box 834 or OSS bridge. ",
        32: "A 1951-1953 exact-name government employee-list lead is postwar and supplies no bridge to the index row or a pre-OSS affiliation. ",
        39: "An exact-name Army burial lead lacks an OSS, Box 835, or protected-identifier bridge. ",
        43: "A Clarion Bartell Wiener veterans lead is chronologically plausible but lacks an OSS or Box 835 bridge. ",
        45: "An exact-name Arlington burial candidate lacks an OSS, Box 835, or protected-identifier bridge. ",
        46: "Numerous Max Wiener namesakes could not be distinguished with the identifiers available online. ",
    }.get(row, "")
    return prefix + "Exact-name and meaningful-variant searches across the NARA index context, OSS, employment, occupation, obituary, institutional, newspaper, directory, and archival sources produced no reliable identity and pre-OSS affiliation bridge; unbridged namesakes were rejected."


def base_update(row: int, **overrides: object) -> dict[str, object]:
    value: dict[str, object] = {
        "person_id": PEOPLE[row][0],
        "manual_review_required": True,
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }
    value.update(overrides)
    return value


def person_updates() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    reviewed_rows = set(ARMY_MATCHES) | SPECIAL_ROWS | {CONFLICT_ROW}
    for row in sorted(set(PEOPLE) - reviewed_rows):
        reason = unresolved_reason(row)
        values.append(base_update(
            row,
            identity_status="unresolved",
            identity_evidence=f"The visually verified page 502 source preserves {PEOPLE[row][1]}, archival Box {box_for(row)}, and the printed index context. {reason}",
            research_status="requires_archival_review",
            next_action=f"Review the indexed Box {box_for(row)} personnel file for corroborating identifiers, the immediate pre-OSS affiliation, and the last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}",
        ))
    for row, item in ARMY_MATCHES.items():
        high_identity = row == 19
        evidence = "A nonshared protected identifier connects the official index and Army record; the identifier remains private."
        if high_identity:
            evidence += " The given name and middle initial agree, but the Army surname is HITTEMORE, so identity remains high confidence rather than confirmed."
        if row == 14:
            evidence += " The match belongs to the no-rank Stephen Whitney row; the separately printed first-lieutenant namesake remains distinct."
        values.append(base_update(
            row,
            identity_status="high_confidence" if high_identity else "confirmed",
            identity_evidence=evidence,
            personnel_category="enlisted_army_personnel",
            commissioned_officer=False,
            research_status="occupation_only_found",
            nara_catalog_id="1263923",
            next_action=f"Review indexed Box {box_for(row)} to identify a named employer or institution and establish the Army-to-OSS chronology; the official bulk record supplies only a historical occupation category at Army entry.",
        ))
    values.extend([
        base_update(17, identity_status="conflicting", identity_evidence="The page-502 Charles W. Whittaker and page-500 Charles W. Whitaker rows share a protected identifier, while the Army record uses WHITAKER. Both person entities remain separate and the private identifier is withheld.", research_status="conflicting_sources", next_action="Review both indexed personnel files in Boxes 831 and 834 to resolve whether the protected identifier was duplicated, misspelled, or assigned to only one person; do not assign the Army occupation meanwhile."),
        base_update(15, identity_status="high_confidence", identity_evidence="The distinctive exact name, expanded full name, and explicit 1940-1944 Bennett College to OSS chronology support a high-confidence identity. The source does not identify which Bennett College.", name_variants=["Thomas P Whitney", "Thomas P. Whitney", "Thomas Porter Whitney"], replace_name_variants=True, personnel_category="civilian_professional_or_administrative_grade", commissioned_officer=False, research_status="verified_employer_found", next_action="Review Box 834 to confirm which Bennett College employed Whitney, exact transition dates, and whether another affiliation intervened."),
        base_update(23, identity_status="high_confidence", identity_evidence="Two institutional Foreign Service Journal notices use the rare exact name George D. Whittinghill and document a coherent 1940 Foreign Service and 1944 Army chronology.", name_variants=["George D Whittinghill", "George D. Whittinghill"], replace_name_variants=True, research_status="documented_prewar_employer_found", next_action="Review Box 834 to establish the Army and OSS transition dates and determine whether an affiliation intervened after the documented 1940 State Department role."),
        base_update(24, identity_status="confirmed", identity_evidence="The exact name and a matching protected officer identifier connect the index row to a direct May 1944 OSS Personnel Board report; the identifier remains private.", name_variants=["Robert B Whittinghill", "Robert B. Whittinghill"], replace_name_variants=True, personnel_category="commissioned_army_officer", commissioned_officer=True, research_status="verified_employer_found", next_action="Review Box 834 to identify the unnamed private school near Cornell and determine the sequence and dates of the school and Time magazine employment."),
        base_update(25, identity_status="high_confidence", identity_evidence="The rare indexed name, full-name institutional profile, Harvard affiliation, profession, and 1928-1943 chronology support a high-confidence identity.", name_variants=["Derwent Whittlesey", "Derwent S. Whittlesey", "Derwent Stainthorpe Whittlesey"], replace_name_variants=True, research_status="documented_prewar_employer_found", next_action="Review Box 834 to establish Whittlesey's specific OSS relationship and determine whether Harvard or a government consultancy was the immediate pre-OSS affiliation."),
    ])
    if len(values) != len(PEOPLE):
        raise RuntimeError(f"Expected {len(PEOPLE)} person updates, generated {len(values)}")
    return values


def research_attempts() -> list[dict[str, object]]:
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        outcome = "candidate_rejected"
        reviewed = 6
        rejected = 5
        note = unresolved_reason(row)
        if row in ARMY_MATCHES:
            outcome, reviewed, rejected = "source_reviewed", 9, 5
            item = ARMY_MATCHES[row]
            note = f"An accepted official Army bridge supports identity and a qualified {item['occupation']} category at Army entry; no named employer or exact OSS-transfer date is supplied."
        elif row == CONFLICT_ROW:
            outcome, reviewed, rejected = "candidate_found", 8, 5
            note = "The protected identifier is shared by two separately printed index rows with Whitaker and Whittaker spellings, while the Army record uses Whitaker. The conflict is preserved and no occupation is assigned."
        elif row == 15:
            outcome, reviewed, rejected = "source_reviewed", 11, 6
            note = "A visually inspected biographical-directory entry establishes Thomas Porter Whitney's 1940-1941 Bennett College employment followed by 1941-1944 OSS work; which Bennett College remains unresolved."
        elif row == 23:
            outcome, reviewed, rejected = "source_reviewed", 12, 6
            note = "Two visually inspected Foreign Service Journal notices establish George D. Whittinghill's 1940 State Department role and 1944 Army status; the evidence gap prevents an unqualified immediate-transition claim."
        elif row == 24:
            outcome, reviewed, rejected = "source_reviewed", 12, 5
            note = "A direct official OSS Personnel Board report, connected by exact name and protected identifier, establishes his immediate G-2 assignment plus Time magazine and unnamed private-school employment."
        elif row == 25:
            outcome, reviewed, rejected = "source_reviewed", 10, 5
            note = "A Harvard obituary and American Academy profile establish Derwent Stainthorpe Whittlesey's Harvard employment from 1928 and full-professor status by 1943; no immediate OSS transition is inferred."
        if row == 3:
            reviewed, rejected = 8, 6
        if row == 10:
            reviewed, rejected = 8, 6
        if row == 32:
            reviewed, rejected = 8, 6
        if row == 43:
            reviewed, rejected = 9, 7
        attempts.append({
            "key": f"page502-row{row}-{slug(name)}-b1012",
            "person_id": person_id,
            "source_adapter": "manual_staged_protocol",
            "query_text": f"{name}; NARA OSS index context; bounded CIA Reading Room and Library of Congress adapter checks; exact-name and meaningful spelling, initial, suffix, punctuation, and OCR variants; OSS, rank, branch, assignment, and identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory, and archival searches; indexed Box {box_for(row)}; protected identifiers used only in private official-record comparison",
            "query_variant_type": "staged_identity_employment_archival_protocol_batch_1012",
            "started_at": "2026-11-04T05:45:00Z",
            "completed_at": "2026-11-04T06:45:00Z",
            "outcome": outcome,
            "sources_reviewed": reviewed,
            "candidate_sources_rejected": rejected,
            "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, postwar-only leads, discovery-only biographies, and sources without an OSS, protected-identifier, rank, unit, or personnel-file bridge were rejected. Historical Army categories were not converted into named employers, workplaces, or institutions. Student status was not converted into employment.",
            "research_notes": f"{note} Exact-name official-domain, OSS, employer, occupation, obituary, biography, institutional, newspaper, directory, and archival searches were checked as applicable. NARA index page 502 and relevant Army code-list and institutional evidence pages were visually checked. The CIA adapter was blocked by robots policy and the Library of Congress adapter timed out during bounded checks; neither failure is treated as a negative result. Manual accessible alternatives were reviewed and the access failures remain separately auditable. No authenticated NARA Catalog API call was made.",
            "next_action": f"Review the indexed Box {box_for(row)} personnel file for corroborating identifiers, the immediate pre-OSS affiliation, and the last civilian employer before wartime service.",
            "attempt_number": 1,
            "research_agent_version": "before-oss-b1012-v1",
        })
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-1012-v1",
        "reviewer": "Before OSS Batch 1012 evidence review",
        "sources": sources(),
        "organizations": organizations(),
        "affiliations": affiliations(),
        "claims": claims(),
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }
    EvidenceBundle.model_validate(bundle)
    OUTPUT.write_text(
        json.dumps(bundle, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
