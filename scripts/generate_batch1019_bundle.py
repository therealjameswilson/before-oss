#!/usr/bin/env python3
"""Generate the reviewed Batch 1019 evidence bundle for PDF page 509."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page509-george-p-wing-to-wimon-wiriyawit-review_"
    "batch-1019_2026-11-04.json"
)

INDEX = "nara-index-b1019"
ARMY = "army-bulk-b1019"
TECH = "army-tech-b1019"
CODES = "army-codes-b1019"
NARA_AWARDS = "nara-oss-awards-winkelhorn-b1019"
DANISH_DIRECTORY = "dansker-i-udlandet-winkelhorn-b1019"
DOD_WINNACKER = "dod-winnacker-b1019"
COLORADO_WINNACKER = "colorado-program-winnacker-b1019"
AHA_WINNACKER = "aha-annual-report-winnacker-b1019"
CIA_WIMON = "cia-oss-free-thai-b1019"
KPI_WIMON = "kpi-wimon-b1019"

ORG_GOLDMAN = "goldman-sachs-b1019"
ORG_WPB = "war-production-board-b1019"
ORG_DANISH_ITALIAN = "danish-italian-export-b1019"
ORG_NYU = "new-york-university-b1019"
ORG_MICHIGAN = "university-of-michigan-b1019"
ORG_NEBRASKA = "university-of-nebraska-b1019"
ORG_MIT = "mit-b1019"
ORG_CHULA = "chulalongkorn-b1019"

PEOPLE = {
    1: ("5fb44e30-7915-551a-8af0-005b5ae39805", "George P Wing"),
    2: ("c1c1f3e4-635f-5545-9bb0-6d10d0b184eb", "Harold E Wing"),
    3: ("90fd6216-9150-5708-81a6-f1092d6840d6", "William H Wing"),
    4: ("25ff31a3-cb41-5e92-9ec4-cc0084502e4f", "Thomas J Wing Wo"),
    5: ("11c6fac7-6e29-53fa-a32d-50c9ea814476", "Frances E Winger"),
    6: ("da6d422c-70f7-51a0-bc9e-9a99e2a5cc88", "Wesley E Winger"),
    7: ("1dd5aa99-39a9-5301-bf36-4cc84e816857", "James A Winget"),
    8: ("f1501905-806e-5059-a740-aba58050d2ac", "Gene L Wingo"),
    9: ("955754e9-07eb-59a2-9b42-fa39c63f7857", "James Wingo"),
    10: ("7b923b27-1d19-5bd5-9f10-21807b28c512", "Thurston C Wingo"),
    11: ("b335511e-d91c-593f-b6b0-64ea33d41d8c", "John C Winkel"),
    12: ("665fece9-5eb8-53a8-bc20-545723aa9f96", "Kai G Winkelhorn"),
    13: ("ba7a458a-a5ce-570c-85ca-42b7856ce3cf", "John C Winkle"),
    14: ("b1f12f3a-c678-5bfe-83c7-a5e3c3c881b6", "Edmund Winkler"),
    15: ("3e5ee620-2a72-55fd-aeaf-4ca4aef3a829", "Ernest Winkler"),
    16: ("6dee6349-f141-5a66-99d2-20df54d15ebc", "William G Winn"),
    17: ("d5641a20-e416-5d03-ab2f-b17d6ccece51", "William N Winn Jr."),
    18: ("d63344e6-19c8-57a3-b62e-70c2744d4a7d", "Rudolph A Winnacker"),
    19: ("46bca5b6-f8df-50a2-88ba-c8fa2a1fc35f", "George Winner"),
    20: ("ef78a1a7-97e2-5959-80d7-13dfd64429ec", "George L Winner"),
    21: ("0df5f127-9086-5e9b-a080-fa1b09bc595e", "George Winnett"),
    22: ("69a18426-fbd7-5236-b84f-ee4be48ce1ec", "William E Winnett"),
    23: ("c72a92fb-9aac-5540-ba01-2284693dd88d", "Robert S Winniford"),
    24: ("9e277cc7-84a0-5b1e-bb05-357d5e5196fa", "William Q Winsborough"),
    25: ("e039fbef-c867-543d-af92-a020772eb7be", "George P Winship"),
    26: ("f96e6cb0-895b-5de5-bff1-6465f6d39929", "Anne Winslow"),
    27: ("a2f639a1-7255-5044-9c52-fa7fdf09e135", "Donald S Winslow"),
    28: ("3d66a221-7685-5086-bfe5-06bcd216f8eb", "Eddie M Winslow"),
    29: ("7d615a90-2594-5878-a908-16918738bcdd", "Harriet A Winslow"),
    30: ("722c2543-c481-5062-880f-a76e48189a96", "Jane Winslow"),
    31: ("feb1b217-da98-57f1-9791-204a363a5c03", "Sylvia C Winslow"),
    32: ("599cb674-7abe-5707-b91b-4984deb281e4", "Warren O Winstanley"),
    33: ("3ea40a46-adc8-57bf-932e-9b5edc7af32e", "Ernst F Winter"),
    34: ("b66216ee-9eb0-56c4-83e8-6f496f37359a", "Frank E Winter"),
    35: ("fcbe054b-9799-534e-8578-13c7c8751206", "Philip Winter"),
    36: ("773f60fc-c8d0-571d-b8e3-cac954a81948", "Florien Winteriter"),
    37: ("3ea8c344-a3cf-5dcf-89ec-40382243e0b5", "Frank J Winterrath"),
    38: ("3eb9aaef-6753-56c7-9212-dbcf276c5a69", "Harry Winters"),
    39: ("20ec61c0-7da0-5652-8f22-e74819c77eae", "Kurt Winters"),
    40: ("8b85f939-d1f9-5aec-81b7-c1b463c92554", "George H Winterstein"),
    41: ("9f6a026a-5c39-588e-8723-94bad66733b1", "Henry J Wintjen"),
    42: ("7749c6a1-feee-5ce3-90b7-6714686f0878", "David H Winton"),
    43: ("56ac40be-d377-509b-8a9b-00519c42af43", "Benedict D Wiora"),
    44: ("528e3f5e-7289-5bde-927b-cfff01d6393a", "Clarence J Wipfli Jr."),
    45: ("4026b71c-43bb-5641-ac41-a085912d6635", "Charles F Wireman"),
    46: ("1f71b51b-f7c7-5bd3-8ccf-c5a8e07fde6f", "Wimon Wiriyawit"),
}

ARMY_OCCUPATIONS = {
    1: ("1942-11-07", "992", "student", "Students", "student", "PDF physical page 304; corrected Code No. 30 entry 9-92"),
    2: ("1942-12-15", "755", "semiskilled motion-picture projectionist", "Motion picture projectionists", "unknown", "PDF physical page 174; historical category 7-55"),
    3: ("1942-10-30", "031", "secondary-school teacher or principal", "Teachers (secondary school) and principals", "unknown", "PDF physical page 170; historical category 0-31"),
    6: ("1943-08-17", "599", "foreman, not elsewhere classified", "Foremen, n.e.c.", "unknown", "PDF physical page 174; historical category 5-99"),
    7: ("1943-03-25", "316", "general farm hand", "Farm hands, general farms", "unknown", "PDF physical page 173; historical category 3-16"),
    11: ("1942-09-11", "134", "shipping or receiving clerk", "Shipping and receiving clerks", "unknown", "PDF physical page 171; historical category 1-34"),
    19: ("1943-08-20", "072", "retail manager", "Managers, retail trade", "unknown", "PDF physical page 171; historical category 0-72"),
    22: ("1942-04-15", "316", "general farm hand", "Farm hands, general farms", "unknown", "PDF physical page 173; historical category 3-16"),
    34: ("1942-06-30", "002", "actor or actress", "Actors and actresses", "unknown", "PDF physical page 170; historical category 0-02"),
    37: ("1943-06-29", "891", "unskilled furnace, smelting, or pouring worker", "Furnacemen, smelters, and pourers", "unknown", "PDF physical page 174; historical category 8-91"),
    40: ("1942-12-21", "157", "insurance salesman", "Insurance salesmen", "unknown", "PDF physical page 171; historical category 1-57"),
    43: ("1942-06-27", "138", "stock clerk", "Stock clerks and storekeepers", "unknown", "PDF physical page 171; historical category 1-38"),
    45: ("1943-02-15", "137", "stenographer or typist", "Stenographers and typists", "unknown", "PDF physical page 171; historical category 1-37"),
}

ARMY_CONFLICT = 4
KAI = 12
RUDOLPH = 18
WINNER_INDEX = 19
WINNER_NAME = 20
WIMON = 46
WINNER_DUPLICATE_GROUP = "page509-george-winner-box846"


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def occupation_key(row: int) -> str:
    return f"{slug(PEOPLE[row][1])}-army-occupation-row{row}-b1019"


def sources() -> list[dict[str, object]]:
    return [
        {"key": INDEX, "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf", "archival_identifier": "RG 226, Entry A1-224, Box 846", "title": "OSS Personnel Files from Excel", "author_creator": "National Archives and Records Administration", "repository_publisher": "National Archives and Records Administration", "publication_record_date": "2010-12-23", "locator": "PDF page 509, rows 1-46; visually checked against a 180 dpi render", "access_date": "2026-11-04", "source_quality": "A_direct_official", "collection_name": "Records of the Office of Strategic Services, Record Group 226", "rights_notes": "All 46 printed rows remain separate. Original spelling, ranks, notes, box and location are preserved; full service identifiers remain private."},
        {"key": ARMY, "stable_url": "https://catalog.archives.gov/id/1263923", "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357", "title": "Electronic Army Serial Number Merged File, ca. 1938-1946", "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration", "repository_publisher": "National Archives and Records Administration", "publication_record_date": "1938-1946; merged file created 2002", "locator": "Official unrestricted ASNEF.FIN.DAT; thirteen accepted and one conflicting protected-identifier comparisons; identifiers and raw rows withheld", "access_date": "2026-11-04", "source_quality": "A_direct_official", "collection_name": "World War II Army Enlistment Records", "document_number": "ASNEF.FIN.DAT", "rights_notes": "Army-entry categories are neither named employers nor exact OSS-transfer records. The Thomas J. Wing Wo identifier conflict transfers no Army data."},
        {"key": TECH, "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf", "archival_identifier": "NN3-064-03-008; National Archives Identifier 1263923", "title": "World War II Army Enlistment Records: Reference Copy of Technical Documentation", "author_creator": "National Archives and Records Administration", "repository_publisher": "National Archives at College Park - Electronic Records", "publication_record_date": "1994-2005; reference copy modified 2011", "locator": "PDF physical pages 44-46; fixed-width identifier, name, entry-date, grade and civilian-occupation fields", "access_date": "2026-11-04", "source_quality": "A_direct_official", "collection_name": "World War II Army Enlistment Records technical documentation"},
        {"key": CODES, "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1CL_SD.pdf", "archival_identifier": "National Archives Identifier 1263923; Code No. 30", "title": "NARA Compiled Code Lists for the Electronic Army Serial Number Merged File", "author_creator": "National Archives and Records Administration", "repository_publisher": "National Archives at College Park - Electronic Records", "publication_record_date": "2011-01-12; modified 2011-03-17", "locator": "PDF physical pages 170-175 and 304; all thirteen published categories visually inspected", "access_date": "2026-11-04", "source_quality": "A_direct_official", "collection_name": "World War II Army Enlistment Records technical documentation", "rights_notes": "Historical categories are published with their limits and never converted into a named employer or institution."},
        {"key": NARA_AWARDS, "stable_url": "https://www.archives.gov/files/research/jfk/releases/104-10165-10120.pdf", "archival_identifier": "NARA record 104-10165-10120; CIA-origin OSS file", "title": "OSS Awards and Decorations Board survey, SO Branch", "author_creator": "Office of Strategic Services", "repository_publisher": "National Archives and Records Administration", "publication_record_date": "1945", "locator": "PDF physical page 154; internal page 36; visually inspected from the original scan", "access_date": "2026-11-04", "source_quality": "A_direct_official", "collection_name": "JFK Assassination Records Collection", "document_number": "104-10165-10120", "rights_notes": "The official record names Lt. Col. Kai G. Winkelhorn and documents Danish-section service; it does not supply pre-OSS employment."},
        {"key": DANISH_DIRECTORY, "stable_url": "https://slaegtsbibliotek.dk/928717.pdf", "title": "Danske i Udlandet 1956", "author_creator": "A. Kamp, editor", "repository_publisher": "Foreningen Dansk Samvirke; digitized by Danske Slægtsforskere", "publication_record_date": "1956", "locator": "PDF physical page 334; printed page 336; visually inspected", "access_date": "2026-11-04", "source_quality": "C_reputable_contemporary_or_scholarly", "collection_name": "Slægtsforskernes Bibliotek", "rights_notes": "The directory gives a dated employment and service chronology. Short excerpts and project-authored English paraphrases only are retained."},
        {"key": DOD_WINNACKER, "stable_url": "https://history.defense.gov/Multimedia/Biographies/Article-View/Article/571274/rudolph-winnacker/", "title": "Rudolph Winnacker", "author_creator": "Office of the Secretary of Defense Historical Office", "repository_publisher": "U.S. Department of Defense", "publication_record_date": "undated", "locator": "Biography section", "access_date": "2026-11-04", "source_quality": "A_direct_official", "collection_name": "Past OSD Historians", "rights_notes": "Official biography directly links Winnacker's academic work and OSS research service; exact faculty dates come from the corroborating institutional program."},
        {"key": COLORADO_WINNACKER, "stable_url": "https://www.yumpu.com/en/document/view/23279463/1962-university-of-colorado-boulder/4", "title": "1962 University of Colorado program", "author_creator": "University of Colorado Public Relations Department", "repository_publisher": "University of Colorado; digital copy hosted by Yumpu", "publication_record_date": "1962", "locator": "Page 4, Rudolph A. Winnacker biography", "access_date": "2026-11-04", "source_quality": "C_reputable_contemporary_or_scholarly", "rights_notes": "The institutional program explicitly dates the Michigan and Nebraska faculty sequence and Winnacker's departure from Nebraska for Washington and OSS research."},
        {"key": AHA_WINNACKER, "stable_url": "https://www.historians.org/wp-content/uploads/2024/08/1938-Annual-Report.pdf", "title": "Annual Report of the American Historical Association for the Year 1938", "author_creator": "American Historical Association", "repository_publisher": "American Historical Association", "publication_record_date": "1939", "locator": "Proceedings, page 23; Rudolph A. Winnacker listed with University of Nebraska", "access_date": "2026-11-04", "source_quality": "B_authoritative_institutional", "collection_name": "American Historical Association annual reports"},
        {"key": CIA_WIMON, "stable_url": "https://www.cia.gov/resources/csi/static/OSS-and-Free-Thai.pdf", "title": "War of a Different Kind: OSS and Free Thai Operations in World War II", "author_creator": "Bob Bergin", "repository_publisher": "Central Intelligence Agency, Center for the Study of Intelligence", "publication_record_date": "2011-12", "locator": "Studies in Intelligence 55, no. 4, physical pages 3-4; printed pages 13-14", "access_date": "2026-11-04", "source_quality": "A_direct_official", "collection_name": "Studies in Intelligence", "rights_notes": "The official history documents Wimon Wiriyawit's OSS training and Operation HOTFOOT role. It does not by itself identify a pre-OSS employer."},
        {"key": KPI_WIMON, "stable_url": "https://wiki.kpi.ac.th/index.php?title=วิมล_วิริยะวิทย์", "title": "วิมล วิริยะวิทย์ (Wimon Wiriyawit)", "author_creator": "Professor Noranit Setabutr; reviewed by Associate Professor Dr. Niyom Rathamarit", "repository_publisher": "King Prajadhipok's Institute", "publication_record_date": "undated", "locator": "Biography paragraphs on education and Free Thai recruitment", "access_date": "2026-11-04", "source_quality": "B_authoritative_institutional", "collection_name": "Thai Politics and Government Database", "rights_notes": "Project-authored English paraphrases preserve the source's chronology. Apparent date typographical errors elsewhere on the page are not repeated."},
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {"key": ORG_GOLDMAN, "canonical_name": "Goldman, Sachs & Co.", "historical_name": "Goldman, Sachs & Co.", "aliases": ["Goldman Sachs & Co."], "organization_type": "investment bank", "sector": "finance_and_banking", "city": "New York", "state_or_region": "New York", "country": "United States", "active_dates": "Kai G. Winkelhorn documented there from 1924 until wartime government service in 1942", "normalization_notes": "The historical comma form is preserved; no modern corporate structure is substituted."},
        {"key": ORG_WPB, "canonical_name": "War Production Board", "historical_name": "War Production Board", "aliases": ["WPB"], "organization_type": "federal wartime agency", "sector": "federal_government", "city": "Washington", "state_or_region": "District of Columbia", "country": "United States", "active_dates": "1942-1945", "normalization_notes": "Modeled as a government assignment, not a private-sector employer."},
        {"key": ORG_DANISH_ITALIAN, "canonical_name": "Dansk-Italiensk Export Co.", "historical_name": "Dansk-Italiensk Export Co.", "aliases": ["Danish-Italian Export Company"], "organization_type": "export company", "sector": "business_and_industry", "city": "Genoa and Catania", "country": "Italy", "active_dates": "Kai G. Winkelhorn documented there, 1921-1923", "normalization_notes": "The directory's historical name is preserved; no successor is inferred."},
        {"key": ORG_NYU, "canonical_name": "New York University", "historical_name": "New York University", "aliases": ["NYU"], "organization_type": "university", "sector": "academia_and_research", "city": "New York", "state_or_region": "New York", "country": "United States", "active_dates": "Kai G. Winkelhorn studied economics and banking, 1925-1927", "normalization_notes": "Student affiliation only; NYU is not treated as his employer."},
        {"key": ORG_MICHIGAN, "canonical_name": "University of Michigan", "historical_name": "University of Michigan", "aliases": [], "organization_type": "university", "sector": "academia_and_research", "city": "Ann Arbor", "state_or_region": "Michigan", "country": "United States", "active_dates": "Rudolph A. Winnacker on the faculty, 1931-1936", "normalization_notes": "Historical institution name preserved."},
        {"key": ORG_NEBRASKA, "canonical_name": "University of Nebraska", "historical_name": "University of Nebraska", "aliases": ["University of Nebraska-Lincoln"], "organization_type": "university", "sector": "academia_and_research", "city": "Lincoln", "state_or_region": "Nebraska", "country": "United States", "active_dates": "Rudolph A. Winnacker taught there, 1936-1941", "normalization_notes": "The 1930s-1940s historical name is preserved rather than silently replaced with the modern campus name."},
        {"key": ORG_MIT, "canonical_name": "Massachusetts Institute of Technology", "historical_name": "Massachusetts Institute of Technology", "aliases": ["MIT"], "organization_type": "university", "sector": "academia_and_research", "city": "Cambridge", "state_or_region": "Massachusetts", "country": "United States", "active_dates": "Wimon Wiriyawit studied there from 1940 and took wartime leave in 1942", "normalization_notes": "Student status is not employment."},
        {"key": ORG_CHULA, "canonical_name": "Chulalongkorn University", "historical_name": "Chulalongkorn University", "aliases": [], "organization_type": "university", "sector": "academia_and_research", "city": "Bangkok", "country": "Thailand", "active_dates": "Wimon Wiriyawit studied engineering there before departing for MIT in 1940", "normalization_notes": "Student status is not employment; a Royal Thai Air Force scholarship is not converted into a military assignment."},
    ]


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, _label, relationship, _locator) in ARMY_OCCUPATIONS.items():
        identity = "high_confidence" if row == WINNER_INDEX else "confirmed"
        values.append({"key": occupation_key(row), "person_id": PEOPLE[row][0], "occupation": occupation, "relationship_type": relationship, "end_date": date, "date_precision": f"Historical civilian-occupation code {code} was recorded at Army entry on {date}; no named employer or institution is supplied.", "country": "United States", "pre_oss_temporal_basis": "strongly_date_bounded", "identity_confidence": identity, "claim_confidence": "medium", "source_quality": "A_direct_official", "publication_status": "publish_qualified", "research_notes": "Broad historical category only; no employer, workplace, institution, exact specialty beyond the code, or exact OSS transition is inferred."})
    values.extend([
        {"key": "kai-winkelhorn-wpb-b1019", "person_id": PEOPLE[KAI][0], "organization_key": ORG_WPB, "organization_name_as_found": "War Production Board, Washington", "role_title": "staff member; exact title not stated", "relationship_type": "government_assignment", "start_date": "1942", "end_date": "1943", "date_precision": "The 1956 directory places him at the War Production Board in 1942, then in the U.S. Army and OSS in 1943; exact months are not supplied.", "city": "Washington", "state_or_region": "District of Columbia", "country": "United States", "immediate_pre_oss": True, "pre_oss_temporal_basis": "strongly_date_bounded", "identity_confidence": "high_confidence", "claim_confidence": "high", "source_quality": "C_reputable_contemporary_or_scholarly", "publication_status": "published", "research_notes": "Best-supported immediate government affiliation; not a civilian company employer."},
        {"key": "kai-winkelhorn-goldman-b1019", "person_id": PEOPLE[KAI][0], "organization_key": ORG_GOLDMAN, "organization_name_as_found": "Goldman, Sachs & Co.", "role_title": "banker", "occupation": "banker", "relationship_type": "employment", "start_date": "1924", "end_date": "1942", "date_precision": "The directory says he had been with the firm since 1924 and next places him at the War Production Board in 1942.", "city": "New York", "state_or_region": "New York", "country": "United States", "last_civilian_pre_service": True, "pre_oss_temporal_basis": "strongly_date_bounded", "identity_confidence": "high_confidence", "claim_confidence": "high", "source_quality": "C_reputable_contemporary_or_scholarly", "publication_status": "published", "research_notes": "Last named civilian employer before the documented federal-government and Army/OSS pathway."},
        {"key": "kai-winkelhorn-danish-italian-b1019", "person_id": PEOPLE[KAI][0], "organization_key": ORG_DANISH_ITALIAN, "organization_name_as_found": "Dansk-Italiensk Export Co.", "role_title": "employee; later authorized signatory", "occupation": "export-company employee", "relationship_type": "employment", "start_date": "1921", "end_date": "1923", "date_precision": "The directory dates Genoa employment to 1921-1922 and a prokurist role in Catania to 1922-1923.", "city": "Genoa and Catania", "country": "Italy", "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "high_confidence", "claim_confidence": "high", "source_quality": "C_reputable_contemporary_or_scholarly", "publication_status": "published", "research_notes": "Earlier documented employment; not immediate and not the last civilian employer."},
        {"key": "kai-winkelhorn-nyu-b1019", "person_id": PEOPLE[KAI][0], "organization_key": ORG_NYU, "organization_name_as_found": "New York University", "role_title": "economics and banking student", "occupation": "student", "relationship_type": "student", "start_date": "1925", "end_date": "1927", "date_precision": "The directory dates courses in economics and banking to 1925-1927.", "city": "New York", "state_or_region": "New York", "country": "United States", "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "high_confidence", "claim_confidence": "high", "source_quality": "C_reputable_contemporary_or_scholarly", "publication_status": "published", "research_notes": "Student affiliation only; not employment."},
        {"key": "rudolph-winnacker-nebraska-b1019", "person_id": PEOPLE[RUDOLPH][0], "organization_key": ORG_NEBRASKA, "organization_name_as_found": "University of Nebraska", "role_title": "faculty member and teacher of history", "occupation": "historian and university teacher", "relationship_type": "employment", "start_date": "1936", "end_date": "1941", "date_precision": "The institutional program dates teaching to 1936-1941 and explicitly sequences his departure for Washington and OSS research.", "city": "Lincoln", "state_or_region": "Nebraska", "country": "United States", "immediate_pre_oss": True, "last_civilian_pre_service": True, "pre_oss_temporal_basis": "explicit_immediate", "identity_confidence": "high_confidence", "claim_confidence": "high", "source_quality": "C_reputable_contemporary_or_scholarly", "publication_status": "published", "research_notes": "Best-supported immediate and last civilian employer. The exact COI/OSS administrative appointment date is not stated."},
        {"key": "rudolph-winnacker-michigan-b1019", "person_id": PEOPLE[RUDOLPH][0], "organization_key": ORG_MICHIGAN, "organization_name_as_found": "University of Michigan", "role_title": "faculty member", "occupation": "historian and university teacher", "relationship_type": "employment", "start_date": "1931", "end_date": "1936", "date_precision": "The institutional program dates the faculty appointment to 1931-1936.", "city": "Ann Arbor", "state_or_region": "Michigan", "country": "United States", "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "high_confidence", "claim_confidence": "high", "source_quality": "C_reputable_contemporary_or_scholarly", "publication_status": "published", "research_notes": "Earlier documented employment; not the immediate pre-OSS affiliation."},
        {"key": "wimon-mit-b1019", "person_id": PEOPLE[WIMON][0], "organization_key": ORG_MIT, "organization_name_as_found": "MIT", "role_title": "undergraduate engineering student", "occupation": "student", "relationship_type": "student", "start_date": "1940", "end_date": "1942", "date_precision": "The King Prajadhipok's Institute biography says he was a final-year undergraduate in 1942 and took leave to volunteer for the Free Thai.", "city": "Cambridge", "state_or_region": "Massachusetts", "country": "United States", "immediate_pre_oss": True, "pre_oss_temporal_basis": "explicit_immediate", "identity_confidence": "high_confidence", "claim_confidence": "high", "source_quality": "B_authoritative_institutional", "publication_status": "published", "research_notes": "Immediate civilian status before Free Thai/OSS service; MIT is an educational institution, not his employer."},
        {"key": "wimon-chulalongkorn-b1019", "person_id": PEOPLE[WIMON][0], "organization_key": ORG_CHULA, "organization_name_as_found": "Faculty of Engineering, Chulalongkorn University", "role_title": "engineering student", "occupation": "student", "relationship_type": "student", "end_date": "1940", "date_precision": "The biography says he left during his second year after winning a Royal Thai Air Force scholarship to continue at MIT in 1940.", "city": "Bangkok", "country": "Thailand", "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "high_confidence", "claim_confidence": "high", "source_quality": "B_authoritative_institutional", "publication_status": "published", "research_notes": "Earlier student affiliation only; neither Chulalongkorn University nor the scholarship is treated as employment."},
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
    for row, (date, code, occupation, label, _relationship, locator) in ARMY_OCCUPATIONS.items():
        name = PEOPLE[row][1]
        is_winner = row == WINNER_INDEX
        identity_confidence = "high" if is_winner else "confirmed"
        identity_assessment = ("High confidence from a nonshared protected identifier, surname and first-name agreement, with the Army record supplying middle initial L; the identifier remains private." if is_winner else "Confirmed by a nonshared protected identifier and corroborating official name evidence; the identifier remains private.")
        values.append(make_claim(key=f"identity-{slug(name)}-row{row}-b1019", row=row, claim_type="identity", text=("Indexed George Winner is a high-confidence match to the Army record naming George L Winner." if is_winner else f"Indexed {name} is confirmed as the matching Army record."), paraphrase="The official index and Army record agree through a nonshared protected identifier and compatible name evidence.", identity=identity_assessment, temporal="Identity evidence only; the Army entry date is not treated as an OSS transition date.", quality="A_direct_official", confidence=identity_confidence, publication="published", notes="The accepted review preserves name variants, withholds the full identifier and does not convert Army fields into a named employer.", source_links=[{"source_key": INDEX, "support_type": "supports", "locator_override": f"PDF page 509, row {row}; Box 846"}, {"source_key": ARMY, "support_type": "supports"}, {"source_key": TECH, "support_type": "context_only"}]))
        values.append(make_claim(key=f"occupation-{slug(name)}-row{row}-b1019", row=row, affiliation_key=occupation_key(row), claim_type="occupation", text=f"At Army entry on {date}, {name}'s record carried historical civilian-occupation category {code}: {occupation}.", paraphrase=f"The official bulk record carries code {code}; NARA's compiled list labels that category '{label}'.", identity=identity_assessment, temporal="Strongly date-bounded at Army entry, but neither an exact OSS start date nor proof of an immediate predecessor affiliation.", quality="A_direct_official", confidence="medium", publication="publish_qualified", notes="A historical category only. It is excluded from verified-employer analytics and never converted into a named employer or institution.", source_links=[{"source_key": ARMY, "support_type": "supports"}, {"source_key": TECH, "support_type": "context_only"}, {"source_key": CODES, "support_type": "supports", "locator_override": locator}]))
    values.extend([
        make_claim(key="thomas-wing-wo-army-conflict-b1019", row=ARMY_CONFLICT, claim_type="identity", text="Thomas J Wing Wo cannot be assigned the Army occupation lead because the Army row materially changes the surname to Wingawo.", paraphrase="The protected identifier agrees, but the official Army name differs enough that no identity, occupation or chronology is transferred.", identity="Conflicting; a protected identifier alone cannot overcome a materially different surname.", temporal="No Army date, grade, occupation or chronology is transferred.", quality="A_direct_official", confidence="conflicting", publication="conflicting", notes="Direct Box 846 and underlying Army-source review are required; full identifiers remain private.", source_links=[{"source_key": INDEX, "support_type": "supports", "locator_override": "PDF page 509, row 4; Box 846"}, {"source_key": ARMY, "support_type": "contradicts"}]),
        make_claim(key="identity-kai-winkelhorn-b1019", row=KAI, claim_type="identity", text="The indexed Lieutenant Colonel Kai G Winkelhorn is a high-confidence match to the Danish-American banker and OSS Danish-section officer.", paraphrase="The rare exact name and rank align across the index, an official OSS awards record and a dated Danish biographical directory.", identity="High confidence from exact distinctive name, exact lieutenant-colonel rank, direct OSS role and coherent employment chronology; Box 846 remains unreviewed.", temporal="The directory dates War Production Board service to 1942 and U.S. Army/OSS service to 1943; the official OSS record documents Danish-section duties.", quality="A_direct_official", confidence="high", publication="published", notes="The independent official and contemporary-directory sources support identity without exposing private identifiers.", source_links=[{"source_key": INDEX, "support_type": "supports", "locator_override": "PDF page 509, row 12; Lieutenant Colonel; Box 846"}, {"source_key": NARA_AWARDS, "support_type": "supports", "locator_override": "PDF physical page 154; internal page 36"}, {"source_key": DANISH_DIRECTORY, "support_type": "supports", "locator_override": "PDF physical page 334; printed page 336"}], excerpt="Lt Col Kai G. Winkelhorn — Approved"),
        make_claim(key="kai-winkelhorn-wpb-claim-b1019", row=KAI, affiliation_key="kai-winkelhorn-wpb-b1019", claim_type="immediate_pre_oss_affiliation", text="Kai G. Winkelhorn's best-supported immediate pre-OSS affiliation was the War Production Board in Washington in 1942.", paraphrase="The directory places Winkelhorn at the War Production Board in 1942, followed by appointment as a U.S. Army captain and OSS service in 1943.", identity="High-confidence exact-name, exact-rank and direct-OSS-role match.", temporal="Strongly date-bounded immediate government assignment; exact months and an administrative transfer document are unavailable.", quality="C_reputable_contemporary_or_scholarly", confidence="high", publication="published", notes="A federal wartime assignment, not a private civilian employer.", source_links=[{"source_key": DANISH_DIRECTORY, "support_type": "supports", "locator_override": "PDF physical page 334; printed page 336"}, {"source_key": NARA_AWARDS, "support_type": "context_only", "locator_override": "PDF physical page 154; internal page 36"}]),
        make_claim(key="kai-winkelhorn-goldman-claim-b1019", row=KAI, affiliation_key="kai-winkelhorn-goldman-b1019", claim_type="last_civilian_pre_service", text="Goldman, Sachs & Co. was Kai G. Winkelhorn's last documented civilian employer before his War Production Board, Army and OSS service.", paraphrase="The directory says he worked for Goldman, Sachs & Co. from 1924 and next places him at the War Production Board in 1942.", identity="High-confidence exact-name, exact-rank and direct-OSS-role match.", temporal="Strongly date-bounded as the last named private employer before the intervening federal assignment; exact departure month is unavailable.", quality="C_reputable_contemporary_or_scholarly", confidence="high", publication="published", notes="Goldman Sachs is kept separate from the intervening War Production Board assignment.", source_links=[{"source_key": DANISH_DIRECTORY, "support_type": "supports", "locator_override": "PDF physical page 334; printed page 336"}], excerpt="I bankfirmaet Goldman, Sachs & Co., N.Y. siden 1924."),
        make_claim(key="kai-winkelhorn-danish-italian-claim-b1019", row=KAI, affiliation_key="kai-winkelhorn-danish-italian-b1019", claim_type="other_pre_oss_affiliation", text="Kai G. Winkelhorn worked for Dansk-Italiensk Export Co. in Genoa and Catania from 1921 to 1923.", paraphrase="The directory dates employment in Genoa to 1921-1922 and an authorized-signatory role in Catania to 1922-1923.", identity="High-confidence exact-name, rank and direct-OSS-role match.", temporal="Documented earlier prewar employment, not immediate and not the last civilian employer.", quality="C_reputable_contemporary_or_scholarly", confidence="high", publication="published", notes="Historical company name retained; no successor is inferred.", source_links=[{"source_key": DANISH_DIRECTORY, "support_type": "supports", "locator_override": "PDF physical page 334; printed page 336"}]),
        make_claim(key="kai-winkelhorn-nyu-claim-b1019", row=KAI, affiliation_key="kai-winkelhorn-nyu-b1019", claim_type="other_pre_oss_affiliation", text="Kai G. Winkelhorn took courses in economics and banking at New York University from 1925 to 1927.", paraphrase="The directory records the course subject and dates.", identity="High-confidence exact-name, rank and direct-OSS-role match.", temporal="Documented earlier prewar student affiliation.", quality="C_reputable_contemporary_or_scholarly", confidence="high", publication="published", notes="Student status is not employment.", source_links=[{"source_key": DANISH_DIRECTORY, "support_type": "supports", "locator_override": "PDF physical page 334; printed page 336"}]),
        make_claim(key="identity-rudolph-winnacker-b1019", row=RUDOLPH, claim_type="identity", text="Indexed Rudolph A Winnacker is a high-confidence match to the historian who taught at Michigan and Nebraska before OSS research service.", paraphrase="The rare exact name and middle initial align with the official DoD biography and an institutional program giving the same academic-to-OSS chronology.", identity="High confidence from a distinctive exact name and two independent sources directly linking the academic and OSS roles; Box 846 remains unreviewed.", temporal="The institutional program dates Michigan to 1931-1936, Nebraska to 1936-1941 and the subsequent move to Washington for OSS work.", quality="A_direct_official", confidence="high", publication="published", notes="The direct OSS link prevents a famous-namesake assignment based on name alone.", source_links=[{"source_key": INDEX, "support_type": "supports", "locator_override": "PDF page 509, row 18; Box 846"}, {"source_key": DOD_WINNACKER, "support_type": "supports"}, {"source_key": COLORADO_WINNACKER, "support_type": "supports", "locator_override": "Page 4"}]),
        make_claim(key="rudolph-winnacker-nebraska-immediate-b1019", row=RUDOLPH, affiliation_key="rudolph-winnacker-nebraska-b1019", claim_type="immediate_pre_oss_affiliation", text="Rudolph A. Winnacker's immediate pre-OSS affiliation was the University of Nebraska, where he taught from 1936 to 1941.", paraphrase="The institutional program says he left Nebraska for Washington and OSS research; the AHA's 1938 report independently confirms the Nebraska affiliation.", identity="High-confidence distinctive-name and direct-OSS-role match.", temporal="Explicitly sequenced as the role he left for Washington and OSS work; the exact appointment day is unavailable.", quality="C_reputable_contemporary_or_scholarly", confidence="high", publication="published", notes="The 1941 end date may precede the formal June 1942 naming of OSS; no unsupported COI appointment date is supplied.", source_links=[{"source_key": COLORADO_WINNACKER, "support_type": "supports", "locator_override": "Page 4"}, {"source_key": DOD_WINNACKER, "support_type": "supports"}, {"source_key": AHA_WINNACKER, "support_type": "supports", "locator_override": "Proceedings, page 23"}]),
        make_claim(key="rudolph-winnacker-nebraska-last-civilian-b1019", row=RUDOLPH, affiliation_key="rudolph-winnacker-nebraska-b1019", claim_type="last_civilian_pre_service", text="The University of Nebraska was Rudolph A. Winnacker's last documented civilian employer before his wartime OSS work.", paraphrase="The dated faculty sequence ends with Nebraska in 1941, followed by his move to Washington for OSS research.", identity="High-confidence distinctive-name and direct-OSS-role match.", temporal="Explicitly sequenced last civilian employment before the wartime intelligence role.", quality="C_reputable_contemporary_or_scholarly", confidence="high", publication="published", notes="No intervening employer is documented in the reviewed sources.", source_links=[{"source_key": COLORADO_WINNACKER, "support_type": "supports", "locator_override": "Page 4"}, {"source_key": DOD_WINNACKER, "support_type": "supports"}]),
        make_claim(key="rudolph-winnacker-michigan-claim-b1019", row=RUDOLPH, affiliation_key="rudolph-winnacker-michigan-b1019", claim_type="other_pre_oss_affiliation", text="Rudolph A. Winnacker served on the University of Michigan faculty from 1931 to 1936.", paraphrase="The institutional program supplies the faculty dates, and the official DoD biography corroborates teaching at Michigan and Nebraska.", identity="High-confidence distinctive-name and direct-OSS-role match.", temporal="Documented earlier prewar employment.", quality="C_reputable_contemporary_or_scholarly", confidence="high", publication="published", notes="Earlier employment, not the immediate pre-OSS affiliation.", source_links=[{"source_key": COLORADO_WINNACKER, "support_type": "supports", "locator_override": "Page 4"}, {"source_key": DOD_WINNACKER, "support_type": "supports"}]),
        make_claim(key="identity-wimon-wiriyawit-b1019", row=WIMON, claim_type="identity", text="Indexed Wimon Wiriyawit is a high-confidence match to the MIT student and Free Thai officer trained by OSS for Operation HOTFOOT.", paraphrase="The rare exact name aligns across the index, the CIA's official operation history and King Prajadhipok's Institute's detailed biography.", identity="High confidence from a rare exact name and two independent institutional sources describing the same training, parachute mission and chronology; Box 846 remains unreviewed.", temporal="The institutional biography dates MIT study and wartime leave to 1942; the CIA history dates OSS training and the September 1944 mission.", quality="A_direct_official", confidence="high", publication="published", notes="The identity does not depend on later government employment.", source_links=[{"source_key": INDEX, "support_type": "supports", "locator_override": "PDF page 509, row 46; Box 846"}, {"source_key": CIA_WIMON, "support_type": "supports", "locator_override": "Physical page 3; printed page 13"}, {"source_key": KPI_WIMON, "support_type": "supports", "locator_override": "Education and Free Thai recruitment paragraphs"}], excerpt="Two Free Thai officers, Wimon Wiriyawit and Bunmak Desabut, completed training at the OSS facility at Trincomalee, Ceylon."),
        make_claim(key="wimon-mit-immediate-b1019", row=WIMON, affiliation_key="wimon-mit-b1019", claim_type="immediate_pre_oss_affiliation", text="Wimon Wiriyawit's immediate pre-OSS status was MIT undergraduate student; he took leave in 1942 to volunteer for the Free Thai.", paraphrase="King Prajadhipok's Institute says he was in his final undergraduate year at MIT and then took study leave to volunteer.", identity="High-confidence rare-name and matching OSS-operation chronology.", temporal="Explicitly immediate student status before volunteering; MIT is not an employer.", quality="B_authoritative_institutional", confidence="high", publication="published", notes="The Royal Thai Air Force scholarship is preserved as context and not converted into employment or a military assignment.", source_links=[{"source_key": KPI_WIMON, "support_type": "supports", "locator_override": "Education and Free Thai recruitment paragraphs"}, {"source_key": CIA_WIMON, "support_type": "context_only", "locator_override": "Physical pages 3-4; printed pages 13-14"}]),
        make_claim(key="wimon-chulalongkorn-claim-b1019", row=WIMON, affiliation_key="wimon-chulalongkorn-b1019", claim_type="other_pre_oss_affiliation", text="Before MIT, Wimon Wiriyawit studied engineering at Chulalongkorn University until 1940.", paraphrase="The institutional biography says he left during his second year after winning a scholarship to continue engineering study in the United States.", identity="High-confidence rare-name and matching OSS-operation chronology.", temporal="Documented earlier prewar student affiliation.", quality="B_authoritative_institutional", confidence="high", publication="published", notes="Student status is not employment; no degree completion is inferred.", source_links=[{"source_key": KPI_WIMON, "support_type": "supports", "locator_override": "Education paragraph"}]),
    ])
    return values


def unresolved_reason(row: int) -> str:
    special = {
        13: "The printed Staff Sergeant rank establishes enlisted Army status but not a pre-OSS employer or assignment.",
        42: "The printed Ensign and USNR notation establish commissioned naval status but not a pre-OSS employer or assignment.",
    }.get(row, "")
    prefix = f"{special} " if special else ""
    return prefix + "Accessible exact-name, official, OSS, employer, occupation, obituary, institutional, newspaper, directory and archival searches produced no reliable identity-and-affiliation bridge; unbridged namesakes and postwar-only leads were rejected."


def base_update(row: int, **overrides: object) -> dict[str, object]:
    value: dict[str, object] = {"person_id": PEOPLE[row][0], "manual_review_required": True, "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "high"}
    value.update(overrides)
    return value


def person_updates() -> list[dict[str, object]]:
    special = set(ARMY_OCCUPATIONS) | {ARMY_CONFLICT, KAI, RUDOLPH, WINNER_NAME, WIMON}
    values: list[dict[str, object]] = []
    for row in sorted(set(PEOPLE) - special):
        reason = unresolved_reason(row)
        overrides: dict[str, object] = {}
        if row == 13:
            overrides.update(personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False)
        elif row == 42:
            overrides.update(personnel_category="commissioned_naval_officer", commissioned_officer=True, allied_or_foreign_personnel=False)
        values.append(base_update(row, identity_status="unresolved", identity_evidence=f"The visually verified page 509 source preserves {PEOPLE[row][1]}, archival Box 846, and the printed rank or note when present. {reason}", research_status="requires_archival_review", next_action=f"Review indexed Box 846 for corroborating identifiers, immediate pre-OSS affiliation and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}", **overrides))
    for row in ARMY_OCCUPATIONS:
        is_winner = row == WINNER_INDEX
        values.append(base_update(row, identity_status="high_confidence" if is_winner else "confirmed", identity_evidence=("A nonshared protected identifier plus surname and first-name agreement support high confidence; the Army row supplies middle initial L, and the identifier remains private." if is_winner else "A nonshared protected identifier and corroborating official name evidence connect the index and Army records; the identifier remains private."), name_variants=["George L Winner"] if is_winner else None, replace_name_variants=False, personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, possible_duplicate_group=WINNER_DUPLICATE_GROUP if is_winner else None, research_status="occupation_only_found", nara_catalog_id="1263923", next_action="Review indexed Box 846 to identify a named employer or institution and establish Army-to-OSS chronology; the bulk record supplies only a historical category at Army entry."))
    values.extend([
        base_update(ARMY_CONFLICT, identity_status="conflicting", identity_evidence="The protected identifier points to an Army row naming Wingawo Thomas J rather than Thomas J Wing Wo. No Army data are transferred.", research_status="conflicting_sources", archival_review_priority="critical", next_action="Review Box 846 and the underlying Army source to resolve the protected-identifier/name conflict before assigning occupation, grade or chronology."),
        base_update(KAI, identity_status="high_confidence", identity_evidence="The rare exact name and lieutenant-colonel rank align across the index, a direct OSS awards record and a dated Danish biographical directory.", name_variants=["Kai G. Winkelhorn", "Kai Winkelhorn"], replace_name_variants=False, personnel_category="commissioned_army_officer", commissioned_officer=True, allied_or_foreign_personnel=False, research_status="verified_employer_found", archival_review_priority="medium", next_action="Review Box 846 to verify exact War Production Board, Army and OSS appointment dates; the immediate affiliation and last civilian employer are already supported."),
        base_update(RUDOLPH, identity_status="high_confidence", identity_evidence="The distinctive exact name and middle initial align with an official DoD OSS biography and an institutional program giving the same academic chronology.", name_variants=["Rudolph A. Winnacker"], replace_name_variants=False, research_status="verified_employer_found", archival_review_priority="medium", next_action="Review Box 846 to establish the exact 1941-1942 COI/OSS appointment date and branch chronology; the Nebraska-to-OSS sequence is already supported."),
        base_update(WINNER_NAME, identity_status="probable", identity_evidence="The adjacent index row is an exact name match to the Army row reached through George Winner's private identifier, but the two printed source rows remain separate and cannot be merged without Box 846 review.", possible_duplicate_group=WINNER_DUPLICATE_GROUP, research_status="needs_identity_review", archival_review_priority="critical", next_action="Compare the adjacent George Winner and George L Winner folders in Box 846 before merging entities or transferring the Army occupation to this row."),
        base_update(WIMON, identity_status="high_confidence", identity_evidence="The rare exact name aligns across the index, CIA's official Operation HOTFOOT history and King Prajadhipok's Institute's detailed biography.", name_variants=["Wimon Wiriyawit", "วิมล วิริยะวิทย์", "Wimol Wiriyavit"], replace_name_variants=False, personnel_category="foreign_or_allied_military_personnel", commissioned_officer=True, allied_or_foreign_personnel=True, research_status="completed", archival_review_priority="medium", next_action="Review Box 846 to verify exact Free Thai and OSS appointment dates; the immediate MIT student pathway is already supported."),
    ])
    if len(values) != len(PEOPLE):
        raise RuntimeError(f"Expected {len(PEOPLE)} person updates, generated {len(values)}")
    return values


def research_attempts() -> list[dict[str, object]]:
    attempts: list[dict[str, object]] = []
    enriched = {KAI, RUDOLPH, WIMON}
    for row, (person_id, name) in PEOPLE.items():
        outcome, reviewed, rejected = "candidate_rejected", 6, 5
        note = unresolved_reason(row)
        if row in ARMY_OCCUPATIONS:
            outcome, reviewed, rejected = "source_reviewed", 9, 4
            note = f"An accepted Army bridge supports identity and a qualified {ARMY_OCCUPATIONS[row][2]} category at Army entry; no named employer or exact OSS-transfer date is supplied."
        elif row == ARMY_CONFLICT:
            outcome, reviewed, rejected = "candidate_found", 8, 5
            note = "A protected identifier points to the materially different Army surname Wingawo. The conflict is preserved and no Army data are transferred."
        elif row == WINNER_NAME:
            outcome, reviewed, rejected = "candidate_found", 8, 5
            note = "The adjacent George Winner row reaches an Army record naming George L Winner, but the two index rows remain separate pending Box 846 review."
        elif row in enriched:
            outcome, reviewed, rejected = "source_reviewed", 13, 6
            note = {
                KAI: "A visually inspected Danish directory and official NARA OSS awards record support the Goldman Sachs-to-War Production Board-to-OSS sequence.",
                RUDOLPH: "An official DoD biography, institutional program and contemporary AHA record support the Michigan-to-Nebraska-to-OSS sequence.",
                WIMON: "CIA's official operation history and King Prajadhipok's Institute support the Chulalongkorn/MIT student pathway into Free Thai and OSS service.",
            }[row]
        attempts.append({"key": f"page509-row{row}-{slug(name)}-b1019", "person_id": person_id, "source_adapter": "manual_staged_protocol", "query_text": f"{name}; NARA OSS index context; exact-name and meaningful spelling, initial, suffix, punctuation, transliteration and OCR variants; OSS, rank, branch, assignment and identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory and archival searches; indexed Box 846; protected identifiers used only in private official-record comparison", "query_variant_type": "staged_identity_employment_archival_protocol_batch_1019", "started_at": "2026-11-04T09:20:00Z", "completed_at": "2026-11-04T11:55:00Z", "outcome": outcome, "sources_reviewed": reviewed, "candidate_sources_rejected": rejected, "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, postwar-only leads, discovery-only biographies and sources without an OSS, protected-identifier, rank, unit or personnel-file bridge were rejected. Army categories were not converted into named employers or institutions.", "research_notes": f"{note} The official index, Army bulk comparison, exact-name searches, official OSS context and available employer, occupation, obituary, institutional, newspaper, directory and archival leads were reviewed as applicable. Index page 509, relevant NARA code-list pages, the Winkelhorn directory page and NARA OSS awards physical page 154 were visually checked. Batch-level CIA and Library of Congress adapters each failed closed with an access error recorded separately; those errors are not negative evidence. Accessible official, institutional and scholarly alternatives were reviewed. No authenticated NARA Catalog API request was made.", "next_action": "Review indexed Box 846 for corroborating identifiers, immediate pre-OSS affiliation and last civilian employer before wartime service.", "attempt_number": 1, "research_agent_version": "before-oss-b1019-v1"})
    return attempts


def main() -> None:
    bundle = {"bundle_version": "batch-1019-v1", "reviewer": "Before OSS Batch 1019 evidence review", "sources": sources(), "organizations": organizations(), "affiliations": affiliations(), "claims": claims(), "person_updates": person_updates(), "research_attempts": research_attempts()}
    EvidenceBundle.model_validate(bundle)
    OUTPUT.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
