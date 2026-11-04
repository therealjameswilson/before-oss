#!/usr/bin/env python3
"""Generate the reviewed Batch 1016 evidence bundle for PDF page 506."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page506-lansing-williams-to-lawrence-j-willinger-review_"
    "batch-1016_2026-11-04.json"
)

INDEX = "nara-index-b1016"
ARMY = "army-bulk-b1016"
TECH = "army-tech-b1016"
CODES = "army-codes-b1016"
BALL_EASTERNER = "ball-state-easterner-1935-b1016"
BALL_ALUMNUS = "ball-state-alumnus-1949-b1016"
CIA_APRIL = "cia-oss-april-1944-b1016"
CIA_EUROPE = "cia-oss-europe-mediterranean-b1016"
FSJ_1950 = "afsa-fsj-1950-b1016"
FSJ_1940 = "afsa-fsj-1940-b1016"

ORG_BALL_STATE = "ball-state-teachers-college-b1016"
ORG_STATE = "us-department-of-state-b1016"

PEOPLE = {
    1: ("9c00e055-1c02-5eda-967c-3732586a8a87", "Lansing Williams"),
    2: ("ab0d962e-4482-543b-bd0d-f00c08786a12", "Lauri A Williams"),
    3: ("868ac8d2-4681-5cfc-b8d5-f3a1eea717e7", "Layton R Williams"),
    4: ("d95e19f3-f8d8-5c16-99af-b3d01c359a66", "Malcolm J Williams"),
    5: ("54eea12e-cef2-5b4e-ad4b-a22ee0504a8d", "Margaret C Williams"),
    6: ("f23a2cd6-373a-51b5-8eed-0cf13f6f18a7", "Mary C Williams"),
    7: ("9ad42d6a-3d3b-5b73-a070-49ffc5286952", "Mary E Williams"),
    8: ("552f2500-37cb-560c-bbef-c02888ef8d45", "Melvin Williams"),
    9: ("bcdd1801-9e44-5309-9092-6a00c948fff9", "Milton D Williams"),
    10: ("4bec75e2-b1c0-5e76-bcb8-5cb595f1da81", "Morris S Williams"),
    11: ("3c3fccfc-f30f-5927-b2e9-886bceb5b1a4", "Nathaniel Williams"),
    12: ("704c9bb8-e7d6-5d8e-b9fe-024055783508", "Norman Williams"),
    13: ("9fbc584e-e6a7-5708-9e8d-8cea1401cc9a", "Oscar C Williams"),
    14: ("c13d658f-31cb-5212-816e-d7f4ce551675", "Payne Williams II"),
    15: ("40209512-a9e1-5c12-bbd1-579ddb6b221b", "Peter W Williams"),
    16: ("46c59f1d-3db7-5691-af89-81306e245ca0", "Randolph A Williams"),
    17: ("ab653302-9bef-56bc-b3d2-a5a27973c224", "Robert G Williams"),
    18: ("2df9a0b5-f465-5c87-a6d1-67ff06724783", "Robert L Williams"),
    19: ("c00580fa-3ff9-59a3-8129-6076523c2c53", "Roy L Williams"),
    20: ("917e5bcb-35c7-55d6-bfbf-d28518c6ae6c", "Roy N Williams Jr."),
    21: ("5c5c1754-5cb9-540c-8fbc-5c1b856076e1", "Violet R Williams"),
    22: ("f10b2a0f-a1a6-562d-bf30-90ee9126bb63", "Walker F Williams"),
    23: ("7c2800ca-c8d3-5c70-8fb5-8195119f381a", "William O Williams"),
    24: ("b1f21268-2fc0-5310-ac57-e14e17668182", "William Williams"),
    25: ("8b4b90bb-2a25-5a34-9913-721ff076a07d", "William A Williams"),
    26: ("1160b5a5-704f-53b8-9e14-2d215b324998", "William B Williams"),
    27: ("2dbd2cd4-f1f5-5ff3-83fe-2827933c577d", "William C Williams"),
    28: ("5a53e687-e1e9-50b3-9ab1-a7508a84d0ff", "William E Williams Jr."),
    29: ("0729999c-f1e1-54d7-b52f-e8639740c653", "Wyman Williams"),
    30: ("c94d0247-bd4d-5fcf-80f7-9280b94a7c62", "Barbara A Williamson"),
    31: ("fda8c002-7cd2-5aca-a8e2-97f0101ba96a", "Benjamin E Williamson"),
    32: ("31120da9-ecca-53d8-8853-76af0acf0588", "David Williamson"),
    33: ("484cc607-e764-596f-95b0-2b4ec476c1ef", "Elizabeth C Williamson"),
    34: ("a7611fff-cc66-5b19-9764-3189a7a192a7", "Emmy Lou Williamson"),
    35: ("bf2193a9-c716-5245-9168-e0cc9647d6dc", "Florence Williamson"),
    36: ("32cb5ae6-a2e8-5d14-afbe-569ce8538033", "Francis T Williamson"),
    37: ("82a8bc6b-a73c-5371-9ac8-0722b0407d98", "Jayo Williamson"),
    38: ("0ae3193f-ee6c-5284-9b6b-41a6d88adff3", "Lyman O Williamson"),
    39: ("17e644f0-841f-5ef5-bbe3-c7045b5ae8cb", "Margaret W Williamson"),
    40: ("85775a46-c409-5b9c-b184-c961815bd292", "Mary F Williamson"),
    41: ("db029202-c913-5084-9858-7ffa277f265f", "Zetha Williamson"),
    42: ("57845e9a-5fa4-56c0-b634-adcaa992d19b", "Buck M Williford"),
    43: ("b1d5cd65-0bf2-506a-83d6-c93cca2a9dc0", "Colleen G Williford"),
    44: ("ccb6a192-6bbd-551c-a113-ee964f028c39", "Edna E Williford"),
    45: ("7d303a23-1a5e-550e-886d-f81a22d372d8", "Robert H Williford"),
    46: ("d1576e97-4d34-575b-a909-1d9f69060c65", "Lawrence J Willinger"),
}

ARMY_OCCUPATIONS = {
    10: {"date": "1943-02-10", "code": "799", "occupation": "apprentice to another trade", "label": "Apprentices to other trades", "relationship": "unknown", "locator": "PDF physical page 175; historical category 7-99"},
    14: {"date": "1942-10-17", "code": "992", "occupation": "student", "label": "Students", "relationship": "student", "locator": "PDF physical page 304; corrected Code No. 30 entry 9-92", "identity": "high_confidence"},
    22: {"date": "1942-06-24", "code": "137", "occupation": "stenographer or typist", "label": "Stenographers and typists", "relationship": "unknown", "locator": "PDF physical page 172; historical category 1-37"},
    26: {"date": "1944-04-06", "code": "447", "occupation": "photoengraver", "label": "Photoengravers", "relationship": "unknown", "locator": "PDF physical page 173; historical category 4-47"},
    31: {"date": "1942-11-17", "code": "583", "occupation": "skilled mechanic or repairman, not elsewhere classified", "label": "Mechanics and repairmen, n.e.c.", "relationship": "unknown", "locator": "PDF physical page 174; historical category 5-83"},
    45: {"date": "1942-05-05", "code": "732", "occupation": "semiskilled construction occupation, not elsewhere classified", "label": "Construction occupations, n.e.c.", "relationship": "unknown", "locator": "PDF physical page 175; historical category 7-32", "identity": "high_confidence"},
}

IDENTITY_ONLY = {9, 15}
CONFLICT_ROW = 12
DAVID_ROW = 32
JAYO_ROW = 37


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def box_for(row: int) -> str:
    if row <= 18:
        return "840"
    if row <= 40:
        return "841"
    return "842"


def occupation_key(row: int) -> str:
    return f"{slug(PEOPLE[row][1])}-army-occupation-row{row}-b1016"


def sources() -> list[dict[str, object]]:
    return [
        {"key": INDEX, "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf", "archival_identifier": "RG 226, Entry A1-224, Boxes 840-842", "title": "OSS Personnel Files from Excel", "author_creator": "National Archives and Records Administration", "repository_publisher": "National Archives and Records Administration", "publication_record_date": "2010-12-23", "locator": "PDF page 506, rows 1-46; visually checked against a 180 dpi render", "access_date": "2026-11-04", "source_quality": "A_direct_official", "collection_name": "Records of the Office of Strategic Services, Record Group 226", "rights_notes": "All 46 printed rows remain separate. Original spelling, ranks, boxes and archival locations are preserved; full service identifiers remain private."},
        {"key": ARMY, "stable_url": "https://catalog.archives.gov/id/1263923", "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357", "title": "Electronic Army Serial Number Merged File, ca. 1938-1946", "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration", "repository_publisher": "National Archives and Records Administration", "publication_record_date": "1938-1946; merged file created 2002", "locator": "Official unrestricted ASNEF.FIN.DAT; eight accepted and two conflicting protected-identifier comparisons; identifiers and raw rows withheld", "access_date": "2026-11-04", "source_quality": "A_direct_official", "collection_name": "World War II Army Enlistment Records", "document_number": "ASNEF.FIN.DAT", "rights_notes": "Army-entry categories are not named employers or exact OSS-transfer records. Code 478 is not interpreted; Norman Williams's duplicated conflicting rows transfer no data."},
        {"key": TECH, "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf", "archival_identifier": "NN3-064-03-008; National Archives Identifier 1263923", "title": "World War II Army Enlistment Records: Reference Copy of Technical Documentation", "author_creator": "National Archives and Records Administration", "repository_publisher": "National Archives at College Park - Electronic Records", "publication_record_date": "1994-2005; reference copy modified 2011", "locator": "PDF physical pages 44-46; fixed-width identifier, name, entry-date, grade, and civilian-occupation fields", "access_date": "2026-11-04", "source_quality": "A_direct_official", "collection_name": "World War II Army Enlistment Records technical documentation"},
        {"key": CODES, "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1CL_SD.pdf", "archival_identifier": "National Archives Identifier 1263923; Code No. 30", "title": "NARA Compiled Code Lists for the Electronic Army Serial Number Merged File", "author_creator": "National Archives and Records Administration", "repository_publisher": "National Archives at College Park - Electronic Records", "publication_record_date": "2011-01-12; modified 2011-03-17", "locator": "PDF physical pages 172-175 and 304; all six published categories visually inspected", "access_date": "2026-11-04", "source_quality": "A_direct_official", "collection_name": "World War II Army Enlistment Records technical documentation", "rights_notes": "Historical categories are published with their limits and never converted into a named employer or institution. Code 478 is not defined in the inspected table and is withheld."},
        {"key": BALL_EASTERNER, "stable_url": "https://dmr.bsu.edu/digital/api/collection/BSUDlyNws/id/3496/download", "archival_identifier": "Ball State Digital Media Repository, BSUDlyNws item 3496", "title": "The Easterner, April 12, 1935", "author_creator": "Student staff of The Easterner", "repository_publisher": "Ball State Teachers College; Ball State University Digital Media Repository", "publication_record_date": "1935-04-12", "locator": "Printed page 2, masthead; visually inspected", "access_date": "2026-11-04", "source_quality": "B_authoritative_institutional", "collection_name": "Ball State Daily News archives", "rights_notes": "The exact distinctive name appears as an assistant copy editor. The masthead supports student-newspaper participation, not paid employment."},
        {"key": BALL_ALUMNUS, "stable_url": "https://dmr.bsu.edu/digital/api/collection/BSUAlumMag/id/7765/download", "archival_identifier": "Ball State Digital Media Repository, BSUAlumMag item 7765", "title": "Ball State Alumnus, Spring 1949", "author_creator": "Ball State Alumni Association", "repository_publisher": "Ball State Alumni Association; Ball State University Digital Media Repository", "publication_record_date": "1949", "locator": "Volume VII, printed page 12, Class of 1939; visually inspected", "access_date": "2026-11-04", "source_quality": "B_authoritative_institutional", "collection_name": "Ball State Alumnus", "rights_notes": "The class note corroborates 1939 alumni status and gives postwar information. Postwar newspaper and printing work is not modeled as pre-OSS employment."},
        {"key": CIA_APRIL, "stable_url": "https://www.cia.gov/readingroom/docs/CIA-RDP13X00001R000100140007-2.pdf", "archival_identifier": "CIA-RDP13X00001R000100140007-2", "title": "Report on OSS Activities for the Month of April 1944", "author_creator": "Office of Strategic Services", "repository_publisher": "CIA Freedom of Information Act Electronic Reading Room", "publication_record_date": "1944-04", "locator": "Personnel Changes and Appointments, April 1944; David Williamson entry", "access_date": "2026-11-04", "source_quality": "A_direct_official", "collection_name": "OSS Collection", "document_number": "CIA-RDP13X00001R000100140007-2"},
        {"key": CIA_EUROPE, "stable_url": "https://www.cia.gov/readingroom/docs/CIA-RDP13X00001R000100410007-2.pdf", "archival_identifier": "CIA-RDP13X00001R000100410007-2", "title": "OSS correspondence and reports on European operations", "author_creator": "Office of Strategic Services", "repository_publisher": "CIA Freedom of Information Act Electronic Reading Room", "publication_record_date": "1944", "locator": "Correspondence addressed to David Williamson, Chief, European and Mediterranean Operations", "access_date": "2026-11-04", "source_quality": "A_direct_official", "collection_name": "OSS Collection", "document_number": "CIA-RDP13X00001R000100410007-2"},
        {"key": FSJ_1950, "stable_url": "https://afsa.org/sites/default/files/fsj-1950-12-december_0.pdf", "archival_identifier": "Foreign Service Journal, December 1950, page 25", "title": "Training for the Foreign Service—Class of 1925", "author_creator": "American Foreign Service Association", "repository_publisher": "The Foreign Service Journal; American Foreign Service Association", "publication_record_date": "1950-12", "locator": "Printed page 25; PDF physical page 27; visually inspected", "access_date": "2026-11-04", "source_quality": "B_authoritative_institutional", "collection_name": "Foreign Service Journal archive", "rights_notes": "The retrospective identifies the Foreign Service officer, his 1942 resignation, class and postings; it does not mention OSS or the Box 841 file."},
        {"key": FSJ_1940, "stable_url": "https://afsa.org/sites/default/files/fsj-1940-10-october_0.pdf", "archival_identifier": "Foreign Service Journal, October 1940, page 563", "title": "The Foreign Service Journal, October 1940", "author_creator": "American Foreign Service Association", "repository_publisher": "The Foreign Service Journal; American Foreign Service Association", "publication_record_date": "1940-10", "locator": "Printed page 563; PDF physical page 29; Embassy and Consulate General, Rome caption; visually inspected", "access_date": "2026-11-04", "source_quality": "C_reputable_contemporary_or_scholarly", "collection_name": "Foreign Service Journal archive"},
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {"key": ORG_BALL_STATE, "canonical_name": "Ball State Teachers College", "historical_name": "Ball State Teachers College", "aliases": ["Ball State"], "organization_type": "teachers college", "sector": "academia_and_research", "city": "Muncie", "state_or_region": "Indiana", "country": "United States", "active_dates": "1929-1961 under this historical name", "normalization_notes": "Historical name in the 1935 source is preserved. The modern successor is Ball State University; no modern name is substituted into the claim."},
        {"key": ORG_STATE, "organization_id": "4d2fbb5f-218d-5445-b7b3-4c2fd22f0286", "canonical_name": "United States Department of State", "historical_name": "Department of State", "aliases": ["U.S. Department of State", "Foreign Service", "Foreign Service of the United States"], "organization_type": "federal executive department", "sector": "federal_government", "city": "Washington", "state_or_region": "District of Columbia", "country": "United States", "normalization_notes": "Existing canonical department reused. Foreign Service and embassy postings are modeled as government assignments, not private civilian employment."},
    ]


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, item in ARMY_OCCUPATIONS.items():
        identity = item.get("identity", "confirmed")
        values.append({"key": occupation_key(row), "person_id": PEOPLE[row][0], "occupation": item["occupation"], "relationship_type": item["relationship"], "end_date": item["date"], "date_precision": f"Historical civilian-occupation code {item['code']} was recorded at Army entry on {item['date']}; no named employer or institution is supplied.", "country": "United States", "pre_oss_temporal_basis": "strongly_date_bounded", "identity_confidence": identity, "claim_confidence": "medium", "source_quality": "A_direct_official", "publication_status": "publish_qualified", "research_notes": "Broad historical category only; no employer, workplace, institution, exact specialty beyond the code, or exact OSS transition is inferred."})
    values.extend([
        {"key": "jayo-williamson-ball-state-b1016", "person_id": PEOPLE[JAYO_ROW][0], "organization_key": ORG_BALL_STATE, "organization_name_as_found": "Ball State Teachers College", "role_title": "assistant copy editor, The Easterner", "occupation": "student newspaper staff member", "relationship_type": "student", "start_date": "1935", "end_date": "1939", "date_precision": "The 1935 masthead documents the role on April 12, 1935; the 1949 alumni magazine identifies Jayo Williamson with the Class of 1939. Continuous attendance or paid employment is not inferred.", "city": "Muncie", "state_or_region": "Indiana", "country": "United States", "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "probable", "claim_confidence": "medium", "source_quality": "B_authoritative_institutional", "publication_status": "publish_qualified", "research_notes": "Published as qualified student affiliation because the distinctive-name sources lack a direct Box 841 or protected-identifier bridge. The college is not labeled an employer."},
        {"key": "david-williamson-state-department-b1016", "person_id": PEOPLE[DAVID_ROW][0], "organization_key": ORG_STATE, "organization_name_as_found": "Foreign Service", "role_title": "Foreign Service Officer, class V", "occupation": "diplomat", "relationship_type": "government_assignment", "end_date": "1942", "date_precision": "The 1950 institutional retrospective states that David Williamson resigned in 1942 as FSO V. The direct OSS records establish Mediterranean and European operations duties by 1944 but not an exact OSS start date.", "country": "United States", "immediate_pre_oss": True, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "probable_immediate", "identity_confidence": "high_confidence", "claim_confidence": "high", "source_quality": "B_authoritative_institutional", "publication_status": "published", "research_notes": "The exact name, 1942 resignation, diplomatic postings in Algiers and Europe, and subsequent OSS European/Mediterranean operations role form a strong identity and chronology bridge. The gap prevents an explicit-immediate designation."},
    ])
    return values


def make_claim(*, key: str, row: int, claim_type: str, text: str, paraphrase: str,
               identity: str, temporal: str, quality: str, confidence: str,
               publication: str, notes: str, source_links: list[dict[str, str]],
               affiliation_key: str | None = None,
               excerpt: str | None = None) -> dict[str, object]:
    value: dict[str, object] = {"key": key, "person_id": PEOPLE[row][0], "claim_type": claim_type, "claim_text": text, "evidence_paraphrase": paraphrase, "identity_match_assessment": identity, "temporal_assessment": temporal, "source_quality": quality, "claim_confidence": confidence, "publication_status": publication, "match_notes": notes, "sources": source_links}
    if affiliation_key:
        value["affiliation_key"] = affiliation_key
    if excerpt:
        value["evidence_excerpt"] = excerpt
    return value


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, item in ARMY_OCCUPATIONS.items():
        name = PEOPLE[row][1]
        identity = item.get("identity", "confirmed")
        label = "a high-confidence" if identity == "high_confidence" else "a confirmed"
        values.append(make_claim(key=f"identity-{slug(name)}-row{row}-b1016", row=row, claim_type="identity", text=f"Indexed {name} has {label} identity bridge to the matching Army record.", paraphrase="The official index and Army bulk record agree on the indexed name or reviewed spelling variant and a protected identifier not shared by another index person.", identity=("High confidence from the protected identifier plus the distinctive Payne Williams / WILLIAMS PAYNE KND rendering." if row == 14 else "High confidence from the protected identifier plus matching Robert H and the WILLIFORD/WILLEFORD spelling variant." if row == 45 else "Confirmed by exact name plus a nonshared protected identifier; the identifier remains private."), temporal="Identity evidence only; the Army entry date is not treated as an OSS transition date.", quality="A_direct_official", confidence=("high" if identity == "high_confidence" else "confirmed"), publication="published", notes="The accepted candidate decision preserves full identifiers outside public outputs.", source_links=[{"source_key": INDEX, "support_type": "supports", "locator_override": f"PDF page 506, row {row}; Box {box_for(row)}"}, {"source_key": ARMY, "support_type": "supports"}, {"source_key": TECH, "support_type": "context_only"}]))
        values.append(make_claim(key=f"occupation-{slug(name)}-row{row}-b1016", row=row, affiliation_key=occupation_key(row), claim_type="occupation", text=f"The Army entry record classifies {name}'s civilian status or occupation broadly as {item['occupation']}.", paraphrase=f"At Army entry on {item['date']}, historical code {item['code']} maps to '{item['label']}.' The record names no employer or institution.", identity=f"{identity.replace('_', ' ').title()} through the reviewed protected-identifier bridge.", temporal="Strongly dated at Army entry; the evidence does not establish the exact OSS transition or a named immediate predecessor.", quality="A_direct_official", confidence="medium", publication="publish_qualified", notes="The historical category is qualified and excluded from verified-employer analytics.", source_links=[{"source_key": ARMY, "support_type": "supports"}, {"source_key": TECH, "support_type": "context_only"}, {"source_key": CODES, "support_type": "supports", "locator_override": item["locator"]}]))
    for row, code_note in ((9, "The Army entry is dated November 27, 1945, after the OSS was dissolved, so code 014 and the entry grade are not used as pre-OSS evidence."), (15, "Civilian-occupation code 478 is left uninterpreted because the inspected official table does not define 4-78.")):
        name = PEOPLE[row][1]
        values.append(make_claim(key=f"identity-{slug(name)}-row{row}-b1016", row=row, claim_type="identity", text=f"Indexed {name} is confirmed as the matching Army record by exact name and a nonshared protected identifier.", paraphrase=f"The official records agree on the complete name and protected identifier. {code_note}", identity="Confirmed by exact name plus a nonshared protected identifier; the identifier remains private.", temporal="Identity evidence only; no occupation, employer or OSS transition is derived.", quality="A_direct_official", confidence="confirmed", publication="published", notes=code_note, source_links=[{"source_key": INDEX, "support_type": "supports", "locator_override": f"PDF page 506, row {row}; Box {box_for(row)}"}, {"source_key": ARMY, "support_type": "supports"}, {"source_key": TECH, "support_type": "context_only"}, {"source_key": CODES, "support_type": "context_only"}]))
    values.extend([
        make_claim(key="norman-williams-army-conflict-b1016", row=CONFLICT_ROW, claim_type="identity", text="Norman Williams cannot be assigned either Army row because one protected identifier points to materially conflicting names and record details.", paraphrase="The identifier appears on an exact Norman Williams Army row and on a second corrupted-name row with different entry and occupation data.", identity="Conflicting; protected-identifier agreement does not resolve the duplicated incompatible Army records.", temporal="No Army date, grade, occupation or chronology is transferred.", quality="A_direct_official", confidence="conflicting", publication="conflicting", notes="Direct Box 840 and underlying Army-source review is required; full identifiers remain private.", source_links=[{"source_key": INDEX, "support_type": "supports", "locator_override": "PDF page 506, row 12; Box 840"}, {"source_key": ARMY, "support_type": "contradicts"}]),
        make_claim(key="identity-jayo-williamson-b1016", row=JAYO_ROW, claim_type="identity", text="The indexed Jayo Williamson is a probable match to the Ball State Class of 1939 student of the same distinctive name.", paraphrase="A 1935 student-paper masthead and 1949 alumni class note repeat the distinctive exact name at the same institution.", identity="Probable from the distinctive exact name, 1935 student role and Class of 1939 corroboration; no direct Box 841 or protected-identifier bridge was available.", temporal="Both institutional records place the person before the OSS period; the 1949 item is retrospective.", quality="B_authoritative_institutional", confidence="medium", publication="publish_qualified", notes="Qualified identity and student affiliation only. Postwar work in the alumni note is not presented as pre-OSS employment.", source_links=[{"source_key": INDEX, "support_type": "supports", "locator_override": "PDF page 506, row 37; Box 841"}, {"source_key": BALL_EASTERNER, "support_type": "supports", "locator_override": "Printed page 2, masthead"}, {"source_key": BALL_ALUMNUS, "support_type": "supports", "locator_override": "Printed page 12, Class of 1939"}]),
        make_claim(key="jayo-williamson-ball-state-claim-b1016", row=JAYO_ROW, affiliation_key="jayo-williamson-ball-state-b1016", claim_type="other_pre_oss_affiliation", text="Jayo Williamson served as an assistant copy editor on The Easterner while a Ball State Teachers College student and was in the Class of 1939.", paraphrase="The April 12, 1935 masthead names Jayo Williamson among assistant copy editors; the institutional alumni magazine identifies Jayo Williamson with the Class of 1939.", identity="Probable distinctive-name match supported by two Ball State institutional records.", temporal="Documented prewar student affiliation; neither source establishes OSS recruitment, an employer or continuous attendance dates.", quality="B_authoritative_institutional", confidence="medium", publication="publish_qualified", notes="Relationship type is student. The historical college name is preserved and the institution is not counted as an employer.", source_links=[{"source_key": BALL_EASTERNER, "support_type": "supports", "locator_override": "Printed page 2, masthead"}, {"source_key": BALL_ALUMNUS, "support_type": "supports", "locator_override": "Printed page 12, Class of 1939"}], excerpt="Assistant Copy Editors: Olive Gnagi, Ruth O'Donnell, Jayo Williamson."),
        make_claim(key="identity-david-williamson-b1016", row=DAVID_ROW, claim_type="identity", text="The indexed David Williamson is a high-confidence match to the former Foreign Service officer who led European and Mediterranean operations for OSS.", paraphrase="The Foreign Service record dates his 1942 resignation after Algiers and European postings; two direct OSS records place the same name in Mediterranean and European operations leadership.", identity="High confidence from exact name, sequenced 1942 Foreign Service departure, geographic specialization, and two direct OSS role records; the common name prevents confirmed status without Box 841.", temporal="Foreign Service departure is dated 1942; direct OSS appointments and correspondence document the role by 1944.", quality="A_direct_official", confidence="high", publication="published", notes="Two corroborating identifiers beyond the name—chronology and European/Mediterranean professional specialization—support publication, while the unreviewed personnel file keeps the match below confirmed.", source_links=[{"source_key": INDEX, "support_type": "supports", "locator_override": "PDF page 506, row 32; Box 841"}, {"source_key": CIA_APRIL, "support_type": "supports", "locator_override": "Personnel Changes and Appointments, April 1944"}, {"source_key": CIA_EUROPE, "support_type": "supports", "locator_override": "Correspondence to Chief, European and Mediterranean Operations"}, {"source_key": FSJ_1950, "support_type": "supports", "locator_override": "Printed page 25"}, {"source_key": FSJ_1940, "support_type": "context_only", "locator_override": "Printed page 563"}]),
        make_claim(key="david-williamson-state-department-claim-b1016", row=DAVID_ROW, affiliation_key="david-williamson-state-department-b1016", claim_type="immediate_pre_oss_affiliation", text="David Williamson's best-supported probable immediate pre-OSS affiliation was the U.S. Foreign Service, from which he resigned in 1942 as an FSO V.", paraphrase="The AFSA retrospective dates the resignation to 1942 after posts including Algiers and London; direct OSS records document Mediterranean and European operations leadership by 1944.", identity="High-confidence bridge from chronology and matching geographic specialization across institutional and direct official records.", temporal="Probable immediate: the 1942 Foreign Service endpoint precedes the documented OSS role, but the sources do not state 'left State to join OSS' or give an exact OSS start date.", quality="B_authoritative_institutional", confidence="high", publication="published", notes="Modeled as a government assignment, not a private civilian employer. It is excluded from last-civilian-employer counts and remains qualified as probable immediate.", source_links=[{"source_key": FSJ_1950, "support_type": "supports", "locator_override": "Printed page 25"}, {"source_key": FSJ_1940, "support_type": "supports", "locator_override": "Printed page 563"}, {"source_key": CIA_APRIL, "support_type": "supports", "locator_override": "Personnel Changes and Appointments, April 1944"}, {"source_key": CIA_EUROPE, "support_type": "supports", "locator_override": "Correspondence to Chief, European and Mediterranean Operations"}], excerpt="resigned in 1942 as an FSO V after serving at Algiers, Tehran, Constantinople, Budapest, Bern, the Department and London"),
    ])
    return values


def unresolved_reason(row: int) -> str:
    special = {
        20: "The suffix Jr. is preserved and was included in name-variant searches.",
        24: "The single-name form William Williams is exceptionally common and cannot be resolved from name alone.",
        27: "The printed second-lieutenant rank establishes commissioned Army status but not a pre-OSS employer or assignment.",
        42: "The printed T/3 rank establishes enlisted Army status but not a pre-OSS employer or assignment.",
        46: "The exact middle initial was retained in all searches, but unbridged namesakes were rejected.",
    }.get(row, "")
    prefix = f"{special} " if special else ""
    return prefix + "Exact-name and meaningful-variant official, OSS, employer, occupation, obituary, institutional, newspaper, directory and archival searches produced no reliable identity-and-affiliation bridge; unbridged namesakes were rejected."


def base_update(row: int, **overrides: object) -> dict[str, object]:
    value: dict[str, object] = {"person_id": PEOPLE[row][0], "manual_review_required": True, "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "high"}
    value.update(overrides)
    return value


def person_updates() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    reviewed = set(ARMY_OCCUPATIONS) | IDENTITY_ONLY | {CONFLICT_ROW, DAVID_ROW, JAYO_ROW}
    for row in sorted(set(PEOPLE) - reviewed):
        reason = unresolved_reason(row)
        values.append(base_update(row, identity_status="unresolved", identity_evidence=f"The visually verified page 506 source preserves {PEOPLE[row][1]}, archival Box {box_for(row)}, and the printed rank when present. {reason}", research_status="requires_archival_review", next_action=f"Review indexed Box {box_for(row)} for corroborating identifiers, immediate pre-OSS affiliation, and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}"))
    for row in ARMY_OCCUPATIONS:
        identity = ARMY_OCCUPATIONS[row].get("identity", "confirmed")
        values.append(base_update(row, identity_status=identity, identity_evidence=("A nonshared protected identifier plus the distinctive name rendering supports high confidence; the identifier remains private." if identity == "high_confidence" else "An exact name and nonshared protected identifier connect the official index and Army record; the identifier remains private."), personnel_category="enlisted_army_personnel", commissioned_officer=False, research_status="occupation_only_found", nara_catalog_id="1263923", next_action=f"Review indexed Box {box_for(row)} to identify a named employer or institution and establish Army-to-OSS chronology; the bulk record supplies only a historical category at Army entry."))
    values.extend([
        base_update(9, identity_status="confirmed", identity_evidence="Exact name and a nonshared protected identifier connect the index and Army record; the November 1945 Army entry is post-OSS and yields no pre-OSS claim.", personnel_category="enlisted_army_personnel", commissioned_officer=False, research_status="requires_archival_review", nara_catalog_id="1263923", next_action="Review Box 840 for a named pre-OSS employer or affiliation. The Army bridge confirms identity only because the entry is dated after OSS dissolution."),
        base_update(15, identity_status="confirmed", identity_evidence="Exact name and a nonshared protected identifier connect the index and Army record; code 478 remains uninterpreted.", personnel_category="enlisted_army_personnel", commissioned_officer=False, research_status="requires_archival_review", nara_catalog_id="1263923", next_action="Review Box 840 for a named employer and Army-to-OSS chronology. The accepted Army bridge confirms identity only."),
        base_update(CONFLICT_ROW, identity_status="conflicting", identity_evidence="One protected identifier appears on an exact Norman Williams Army row and a second materially different corrupted-name row. No Army data are transferred.", research_status="conflicting_sources", archival_review_priority="critical", next_action="Review Box 840 and the underlying Army source to resolve the duplicated protected-identifier conflict before assigning occupation, grade or chronology."),
        base_update(DAVID_ROW, identity_status="high_confidence", identity_evidence="A 1942 Foreign Service resignation after Algiers and European postings aligns with two direct OSS records naming David Williamson in European and Mediterranean operations leadership. Box 841 was not reviewed.", name_variants=["David Williamson"], replace_name_variants=True, personnel_category="civilian_professional_or_administrative_grade", commissioned_officer=False, research_status="requires_archival_review", archival_review_priority="medium", next_action="Review Box 841 to confirm the common-name identity directly, establish the exact OSS entry date, and test whether the Foreign Service was truly immediate rather than probable immediate."),
        base_update(JAYO_ROW, identity_status="probable", identity_evidence="Two Ball State institutional sources repeat the distinctive exact name and support a 1935 student-paper role and Class of 1939 status, but no Box 841 or protected-identifier bridge was available.", name_variants=["Jayo Williamson"], replace_name_variants=True, research_status="needs_identity_review", archival_review_priority="high", next_action="Review Box 841 against the Ball State Class of 1939 records. The published student affiliation is qualified and is not an employer claim."),
    ])
    if len(values) != len(PEOPLE):
        raise RuntimeError(f"Expected {len(PEOPLE)} person updates, generated {len(values)}")
    return values


def research_attempts() -> list[dict[str, object]]:
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        outcome, reviewed, rejected = "candidate_rejected", 6, 5
        note = unresolved_reason(row)
        if row in ARMY_OCCUPATIONS:
            outcome, reviewed, rejected = "source_reviewed", 9, 5
            note = f"An accepted Army bridge supports identity and a qualified {ARMY_OCCUPATIONS[row]['occupation']} category at Army entry; no named employer or exact OSS-transfer date is supplied."
        elif row in IDENTITY_ONLY:
            outcome, reviewed, rejected = "source_reviewed", 9, 5
            note = "An accepted Army bridge confirms identity only; post-OSS chronology or undefined occupation coding prevents a pre-OSS occupation claim."
        elif row == CONFLICT_ROW:
            outcome, reviewed, rejected = "candidate_found", 9, 6
            note = "A duplicated protected identifier points to incompatible Army rows. The conflict is preserved and no Army data are transferred."
        elif row == DAVID_ROW:
            outcome, reviewed, rejected = "source_reviewed", 13, 7
            note = "Two direct OSS records and two Foreign Service Journal records support a high-confidence identity and probable immediate Foreign Service affiliation; the common-name match still requires Box 841 confirmation."
        elif row == JAYO_ROW:
            outcome, reviewed, rejected = "source_reviewed", 11, 6
            note = "Two Ball State institutional records support a probable identity and qualified prewar student affiliation; postwar work is not treated as pre-OSS employment."
        attempts.append({"key": f"page506-row{row}-{slug(name)}-b1016", "person_id": person_id, "source_adapter": "manual_staged_protocol", "query_text": f"{name}; NARA OSS index context; exact-name and meaningful spelling, initial, suffix, punctuation and OCR variants; OSS, rank, branch, assignment and identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory and archival searches; indexed Box {box_for(row)}; protected identifiers used only in private official-record comparison", "query_variant_type": "staged_identity_employment_archival_protocol_batch_1016", "started_at": "2026-11-04T14:15:00Z", "completed_at": "2026-11-04T16:30:00Z", "outcome": outcome, "sources_reviewed": reviewed, "candidate_sources_rejected": rejected, "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, postwar-only leads, discovery-only biographies and sources without an OSS, protected-identifier, rank, unit or personnel-file bridge were rejected. Army categories were not converted into named employers or institutions.", "research_notes": f"{note} Exact-name official-domain, OSS, employer, occupation, obituary, institutional, newspaper, directory and archival searches were checked as applicable. Index page 506 and relevant code-list pages were visually checked. A bounded Library of Congress adapter check encountered URLError, and a CIA adapter check encountered CiaRobotsUnavailable; both are recorded separately and are not treated as negative results. Accessible official and institutional alternatives were reviewed. No authenticated NARA Catalog API call was made.", "next_action": f"Review indexed Box {box_for(row)} for corroborating identifiers, the immediate pre-OSS affiliation, and last civilian employer before wartime service.", "attempt_number": 1, "research_agent_version": "before-oss-b1016-v1"})
    return attempts


def main() -> None:
    bundle = {"bundle_version": "batch-1016-v1", "reviewer": "Before OSS Batch 1016 evidence review", "sources": sources(), "organizations": organizations(), "affiliations": affiliations(), "claims": claims(), "person_updates": person_updates(), "research_attempts": research_attempts()}
    EvidenceBundle.model_validate(bundle)
    OUTPUT.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
