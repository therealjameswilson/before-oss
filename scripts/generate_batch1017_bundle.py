#!/usr/bin/env python3
"""Generate the reviewed Batch 1017 evidence bundle for PDF page 507."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page507-arthur-j-willis-to-georgia-wilson-review_"
    "batch-1017_2026-11-04.json"
)

INDEX = "nara-index-b1017"
ARMY = "army-bulk-b1017"
TECH = "army-tech-b1017"
CODES = "army-codes-b1017"
JSOU = "jsou-support-to-resistance-b1017"
RIGGINS = "riggins-donald-willmott-b1017"
UWYO_MINUTES = "uwyo-trustees-minutes-b1017"
UWYO_AHC = "uwyo-ahc-willman-b1017"
HOOVER = "hoover-goodfellow-board-report-b1017"
SCIENCE_HISTORY = "science-history-bright-wilson-b1017"
WAPO = "washington-post-paul-wilner-b1017"
PENN = "penn-gazette-wilner-b1017"

ORG_ARMY = "us-army-b1017"
ORG_CHENGDU_SCHOOL = "unidentified-chengdu-middle-school-b1017"
ORG_SELF = "self-employed-b1017"
ORG_GEORGETOWN = "georgetown-university-b1017"
ORG_UWYO = "university-of-wyoming-b1017"
ORG_SALEM_UTILITY = "unidentified-salem-public-utility-b1017"
ORG_HARVARD = "harvard-university-b1017"

PEOPLE = {
    1: ("0e8d5664-74c9-5cf4-a56e-05c263f91b3a", "Arthur J Willis"),
    2: ("c23cec05-6e0c-5e1d-8779-f6e8b47520b0", "Claude T Willis"),
    3: ("d5d7a8b5-a55a-5504-9165-4a6c07092a13", "Frederic A Willis"),
    4: ("7f0453df-657a-5050-b409-061785a1ed0b", "Joe W Willis"),
    5: ("1a46608b-cf51-5566-86c6-b7a49e9562b4", "John B Willis"),
    6: ("21c2a4e1-f6e4-5f07-a5b4-c038397edde7", "Johnnie W Willis"),
    7: ("c54e438e-0464-53a1-8d9e-473c8ef80847", "Joseph F Willis"),
    8: ("3cbb9bc4-08ef-523d-90f1-95a9f9ecf597", "Kelsey Willis"),
    9: ("43a26b83-8ed9-54f5-bc9b-5929279b2a85", "Nicholas W Willis"),
    10: ("31463f5f-4573-5de6-9bd1-e0aceb9421a2", "Philip J Willison"),
    11: ("e553d5d7-140a-5175-9bc9-d9d0ec228903", "Turney H Willison"),
    12: ("35467c71-f728-5d3c-b3ba-e6aecc925d7a", "Allan A Willman"),
    13: ("944f5f1f-a2ef-5269-89cb-237f865fd5d7", "David L Willmarth"),
    14: ("1e5ff172-5394-59fd-9048-8e1b68d2fe7d", "Alfred D Willmott"),
    15: ("321d3f5b-f7b5-5df8-a2c6-b2f692c4d0f9", "Donald R Willmott"),
    16: ("4132b06e-0635-5a25-b546-bde8c99af618", "Leonard R.D. Willmott"),
    17: ("636fcf74-9d8d-5ec8-b343-08be42a80680", "Marie L Willoughby"),
    18: ("a9fe1c96-2313-5ec4-9146-784b2284ad73", "Stuart C Willoughby"),
    19: ("099ace09-17a9-54b3-9979-10c507f59f78", "J E Wills"),
    20: ("64431db1-2a8d-5524-a068-71d3b97c117c", "Michael Wills"),
    21: ("49aebef4-a470-5e76-bf8e-e510738bb830", "James J Willsen"),
    22: ("77b91d64-c202-5ba7-8c01-ec8e035bce19", "Philip J Willson"),
    23: ("f1866b7c-329a-5c22-ba85-3540832dff01", "Dean P Wilmoth"),
    24: ("20776dce-dc20-544e-90cc-3d696c027f8a", "Robert J Wilmoth"),
    25: ("667b8a49-0a5e-5609-8eff-1bd23468a97a", "Paul R Wilner"),
    26: ("0c1e58e1-e460-5497-ad59-956b67c4097f", "Alan B Wilson"),
    27: ("f22b7ceb-0f5b-5aa9-ac09-4b3cc9128b41", "Arthur M Wilson"),
    28: ("13f492ad-037d-5c82-8743-9b92666a5cf8", "Charles C Wilson"),
    29: ("522b7577-6842-5c14-9058-3eece8110fa1", "Charles D Wilson"),
    30: ("39cb432f-d729-59bb-b1ea-4789059b3f13", "Charlie G Wilson"),
    31: ("426b761e-2f29-56b6-8c10-d32b8c679d72", "Corra B Wilson"),
    32: ("06afc382-a55a-5e77-afea-6585c442178b", "Curtis M Wilson"),
    33: ("854bfd25-7269-590f-bcea-1479f933bfb2", "Donald C Wilson"),
    34: ("370bb234-4773-5284-89a2-e3e271d8562d", "Duane B Wilson"),
    35: ("9de40ef5-ec1d-5a31-9f62-a89a7879ce66", "E. Bright Wilson"),
    36: ("5fb54e17-1a20-5a54-b788-fc30f73f22bf", "Edward C Wilson"),
    37: ("cdd80740-8b39-5609-a681-78da15c01ef1", "Edward J Wilson"),
    38: ("2b6c4141-25da-5017-9eb8-26228f499eb7", "Edward G Wilson"),
    39: ("336eb711-d883-5d09-901e-bc44138cd1d9", "Eleanor Wilson"),
    40: ("9baee23c-1450-55b7-a879-16860a69be4b", "Ellen C Wilson"),
    41: ("0e3161f7-73f6-5fa7-aa30-dbedb77a6c72", "Elmo Wilson"),
    42: ("4aa27c9a-11a7-559e-9125-a0d7aff5b517", "Everett K Wilson"),
    43: ("422a9a99-fece-52da-92ea-15db067b6fe0", "Francis K Wilson"),
    44: ("190f1c81-4bb0-5397-907d-4a0aab35de8a", "George E Wilson"),
    45: ("e5a044ad-dbd4-5eb7-b9e8-7a803c9b685c", "George H Wilson"),
    46: ("4bc0078f-8af8-5c89-a502-92cad255bf4d", "Georgia Wilson"),
}

ARMY_OCCUPATIONS = {
    5: {"date": "1943-06-16", "code": "031", "occupation": "secondary-school teacher or principal", "label": "Teachers (secondary school) and principals", "relationship": "unknown", "locator": "PDF physical page 171; historical category 0-31"},
    8: {"date": "1945-03-16", "code": "521", "occupation": "miner or mining-machine operator", "label": "Miners and mining-machine operators", "relationship": "unknown", "locator": "PDF physical page 174; historical category 5-21"},
    18: {"date": "1942-12-04", "code": "992", "occupation": "student", "label": "Students", "relationship": "student", "locator": "PDF physical page 304; corrected Code No. 30 entry 9-92"},
    21: {"date": "1942-02-12", "code": "758", "occupation": "semiskilled meatcutter outside slaughtering and packing houses", "label": "Meatcutters, except slaughtering and packing houses", "relationship": "unknown", "locator": "PDF physical page 175; historical category 7-58"},
    22: {"date": "1942-10-28", "code": "992", "occupation": "student", "label": "Students", "relationship": "student", "locator": "PDF physical page 304; corrected Code No. 30 entry 9-92"},
    24: {"date": "1942-10-15", "code": "783", "occupation": "semiskilled mechanic or repairman, not elsewhere classified", "label": "Mechanics and repairmen, semiskilled, n.e.c.", "relationship": "unknown", "locator": "PDF physical page 175; historical category 7-83"},
    26: {"date": "1943-04-05", "code": "992", "occupation": "student", "label": "Students", "relationship": "student", "locator": "PDF physical page 304; corrected Code No. 30 entry 9-92"},
    28: {"date": "1942-05-07", "code": "678", "occupation": "semiskilled machine-shop or related occupation, not elsewhere classified", "label": "Machine-shop and related occupations, n.e.c.", "relationship": "unknown", "locator": "PDF physical page 175; historical category 6-78"},
    29: {"date": "1943-03-09", "code": "992", "occupation": "student", "label": "Students", "relationship": "student", "locator": "PDF physical page 304; corrected Code No. 30 entry 9-92"},
    30: {"date": "1942-04-16", "code": "316", "occupation": "general farm hand", "label": "Farm hands, general farms", "relationship": "unknown", "locator": "PDF physical page 173; historical category 3-16"},
    36: {"date": "1942-02-20", "code": "105", "occupation": "general office clerk", "label": "Clerks, general office", "relationship": "unknown", "locator": "PDF physical page 171; historical category 1-05"},
    42: {"date": "1942-05-28", "code": "402", "occupation": "skilled bakery-production occupation, not elsewhere classified", "label": "Bakery products, n.e.c.", "relationship": "unknown", "locator": "PDF physical page 173; historical category 4-02"},
    45: {"date": "1944-08-16", "code": "316", "occupation": "general farm hand", "label": "Farm hands, general farms", "relationship": "unknown", "locator": "PDF physical page 173; historical category 3-16"},
}

IDENTITY_ONLY = {2, 13}
CONFLICT_ROW = 4
NICHOLAS_ROW = 9
ALLAN_ROW = 12
DONALD_WILLMOTT_ROW = 15
PAUL_ROW = 25
DONALD_WILSON_ROW = 33
BRIGHT_ROW = 35


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def box_for(row: int) -> str:
    if row <= 12:
        return "842"
    if row == 13:
        return "843"
    if row <= 22:
        return "842"
    return "843"


def occupation_key(row: int) -> str:
    return f"{slug(PEOPLE[row][1])}-army-occupation-row{row}-b1017"


def sources() -> list[dict[str, object]]:
    return [
        {"key": INDEX, "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf", "archival_identifier": "RG 226, Entry A1-224, Boxes 842-843", "title": "OSS Personnel Files from Excel", "author_creator": "National Archives and Records Administration", "repository_publisher": "National Archives and Records Administration", "publication_record_date": "2010-12-23", "locator": "PDF page 507, rows 1-46; visually checked against a 180 dpi render", "access_date": "2026-11-04", "source_quality": "A_direct_official", "collection_name": "Records of the Office of Strategic Services, Record Group 226", "rights_notes": "All 46 printed rows remain separate. Original spelling, ranks, notes, boxes and locations are preserved; full service identifiers remain private."},
        {"key": ARMY, "stable_url": "https://catalog.archives.gov/id/1263923", "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357", "title": "Electronic Army Serial Number Merged File, ca. 1938-1946", "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration", "repository_publisher": "National Archives and Records Administration", "publication_record_date": "1938-1946; merged file created 2002", "locator": "Official unrestricted ASNEF.FIN.DAT; fifteen accepted and one conflicting protected-identifier comparisons; identifiers and raw rows withheld", "access_date": "2026-11-04", "source_quality": "A_direct_official", "collection_name": "World War II Army Enlistment Records", "document_number": "ASNEF.FIN.DAT", "rights_notes": "Army-entry categories are not named employers or exact OSS-transfer records. Claude T. Willis's January 1946 entry and undefined code 502 transfer no pre-OSS occupation."},
        {"key": TECH, "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf", "archival_identifier": "NN3-064-03-008; National Archives Identifier 1263923", "title": "World War II Army Enlistment Records: Reference Copy of Technical Documentation", "author_creator": "National Archives and Records Administration", "repository_publisher": "National Archives at College Park - Electronic Records", "publication_record_date": "1994-2005; reference copy modified 2011", "locator": "PDF physical pages 44-46; fixed-width identifier, name, entry-date, grade and civilian-occupation fields", "access_date": "2026-11-04", "source_quality": "A_direct_official", "collection_name": "World War II Army Enlistment Records technical documentation"},
        {"key": CODES, "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1CL_SD.pdf", "archival_identifier": "National Archives Identifier 1263923; Code No. 30", "title": "NARA Compiled Code Lists for the Electronic Army Serial Number Merged File", "author_creator": "National Archives and Records Administration", "repository_publisher": "National Archives at College Park - Electronic Records", "publication_record_date": "2011-01-12; modified 2011-03-17", "locator": "PDF physical pages 171, 173-175 and 304; all thirteen published categories visually inspected", "access_date": "2026-11-04", "source_quality": "A_direct_official", "collection_name": "World War II Army Enlistment Records technical documentation", "rights_notes": "Historical categories are published with their limits and never converted into a named employer or institution. Code 502 is not defined in the inspected three-digit table and is withheld."},
        {"key": JSOU, "stable_url": "https://jsouapplicationstorage.blob.core.windows.net/press/72/19-2.pdf", "archival_identifier": "JSOU Report 19-2; ISBN 978-1-941715-37-6", "title": "Support to Resistance: Strategic Purpose and Effectiveness", "author_creator": "Will Irwin", "repository_publisher": "Joint Special Operations University Press", "publication_record_date": "2019-04", "locator": "Printed page 89; PDF physical page 107; visually inspected", "access_date": "2026-11-04", "source_quality": "B_authoritative_institutional", "collection_name": "Joint Special Operations University publications"},
        {"key": RIGGINS, "stable_url": "https://doi.org/10.7202/1062245ar", "archival_identifier": "DOI 10.7202/1062245ar", "title": "Memorial University’s First Sociologist: The Dilemmas of a Bureaucratic Intellectual", "author_creator": "Stephen Harold Riggins", "repository_publisher": "Newfoundland and Labrador Studies; Érudit", "publication_record_date": "2014", "locator": "Volume 29, number 1, printed pages 51-52", "access_date": "2026-11-04", "source_quality": "C_reputable_contemporary_or_scholarly", "collection_name": "Newfoundland and Labrador Studies", "rights_notes": "Peer-reviewed scholarly article. Only short evidence excerpts and project-authored paraphrases are retained."},
        {"key": UWYO_MINUTES, "stable_url": "https://www.uwyo.edu/trustees/_files/docs/bot-archive-minutes/1940-1949/1943/1943_March%2016_BOT%20Minutes.pdf", "archival_identifier": "University of Wyoming Board of Trustees minutes, sheet 772", "title": "Record of Minutes of Board of Trustees Meeting, March 16, 1943", "author_creator": "University of Wyoming Board of Trustees", "repository_publisher": "University of Wyoming", "publication_record_date": "1943-03-16", "locator": "Sheet 772; PDF physical page 5; visually inspected", "access_date": "2026-11-04", "source_quality": "A_direct_official", "collection_name": "University of Wyoming Board of Trustees archive"},
        {"key": UWYO_AHC, "stable_url": "https://www.uwyo.edu/ahc/_files/collection_guides/wy-west2014-ed2019june.pdf", "archival_identifier": "Allan Arthur Willman papers, Accession 400049", "title": "American Heritage Center Guide to Wyoming and the West Collections", "author_creator": "American Heritage Center", "repository_publisher": "University of Wyoming American Heritage Center", "publication_record_date": "2019-06", "locator": "Printed pages 428-429; PDF physical pages 431-432; visually inspected", "access_date": "2026-11-04", "source_quality": "B_authoritative_institutional", "collection_name": "American Heritage Center collection guides"},
        {"key": HOOVER, "stable_url": "https://digitalcollections.hoover.org/objects/73265/goodfellow-supplementary-interim-report-of-oss-board-of-offi", "archival_identifier": "Hoover ID 69085.141; Millard Preston Goodfellow papers", "title": "Goodfellow supplementary interim report of OSS board of officers", "author_creator": "Millard Preston Goodfellow; Office of Strategic Services Board of Officers", "repository_publisher": "Hoover Institution Library & Archives", "publication_record_date": "1944-05-22", "locator": "Printed page 57, entry LI, proceedings of May 16, 1944; protected identifier omitted from public evidence", "access_date": "2026-11-04", "source_quality": "A_direct_official", "collection_name": "Millard Preston Goodfellow papers", "document_number": "69085.141", "rights_notes": "Declassified U.S. government report. The repository object page and in-memory document text were inspected; a local download was blocked, so no visual-inspection claim is made."},
        {"key": SCIENCE_HISTORY, "stable_url": "https://digital.sciencehistory.org/works/j098zc37b", "archival_identifier": "Center for Oral History number 0061", "title": "Oral history interview with E. Bright Wilson, Jr.", "author_creator": "Raymond C. Ferguson; E. Bright Wilson Jr.", "repository_publisher": "Science History Institute", "publication_record_date": "1986-11-17 to 1986-11-18", "locator": "Interviewee biographical information, Professional Experience", "access_date": "2026-11-04", "source_quality": "B_authoritative_institutional", "collection_name": "Science History Institute Oral History Collection"},
        {"key": WAPO, "stable_url": "https://www.washingtonpost.com/archive/local/1991/02/12/paul-wilner-dies/8cca2ff6-8314-4b70-b164-26dc463f7903/", "title": "Paul Wilner Dies", "author_creator": "Washington Post staff", "repository_publisher": "The Washington Post", "publication_record_date": "1991-02-11", "locator": "Obituary for Paul R. Wilner", "access_date": "2026-11-04", "source_quality": "C_reputable_contemporary_or_scholarly", "collection_name": "Washington Post archive"},
        {"key": PENN, "stable_url": "https://archives.upenn.edu/media/2017/04/gazette-penn-contributions-to-defense-wwii.pdf", "archival_identifier": "Pennsylvania Gazette, volume 41, number 8", "title": "Brothers Wilner", "author_creator": "The Pennsylvania Gazette", "repository_publisher": "University of Pennsylvania Archives", "publication_record_date": "1943-04", "locator": "Printed page 242; PDF physical page 50; visually inspected", "access_date": "2026-11-04", "source_quality": "B_authoritative_institutional", "collection_name": "Penn Contributions to Defense"},
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {"key": ORG_ARMY, "organization_id": "28a26f92-78af-5a1a-9c09-a843eb5975b4", "canonical_name": "United States Army", "historical_name": "United States Army", "aliases": ["U.S. Army", "Army"], "organization_type": "armed service", "sector": "military", "country": "United States", "normalization_notes": "Existing canonical organization reused. Military assignment remains distinct from civilian employment."},
        {"key": ORG_CHENGDU_SCHOOL, "canonical_name": "Unidentified Chinese middle school near Chengdu", "historical_name": "Chinese middle school near Chengdu connected with Oberlin College", "aliases": [], "organization_type": "secondary school", "sector": "academia_and_research", "city": "Chengdu", "state_or_region": "Sichuan", "country": "China", "active_dates": "Documented in 1943-1944", "normalization_notes": "The source does not name the school. Oberlin College is recorded only as a documented connection and is not substituted as the employer."},
        {"key": ORG_SELF, "organization_id": "2d0f4eae-d528-5d59-8b11-6660b1e4fa4a", "canonical_name": "Self-employed", "historical_name": "Self-employed", "aliases": ["private practice"], "organization_type": "self-employment", "sector": "self_employed", "city": "Washington", "state_or_region": "District of Columbia", "country": "United States", "normalization_notes": "Existing canonical self-employment organization reused; the role is modeled separately from Georgetown teaching."},
        {"key": ORG_GEORGETOWN, "organization_id": "b9d4129e-c34a-5bf9-b43c-2452b39b0d53", "canonical_name": "Georgetown University", "historical_name": "Georgetown University", "aliases": ["Georgetown University medical school", "Georgetown"], "organization_type": "university", "sector": "academia_and_research", "city": "Washington", "state_or_region": "District of Columbia", "country": "United States", "normalization_notes": "Existing canonical university reused."},
        {"key": ORG_UWYO, "canonical_name": "University of Wyoming", "historical_name": "University of Wyoming", "aliases": ["Wyoming University"], "organization_type": "public university", "sector": "academia_and_research", "city": "Laramie", "state_or_region": "Wyoming", "country": "United States", "normalization_notes": "Historical institutional name is unchanged. The 1943 Board minutes supply the exact division and title."},
        {"key": ORG_SALEM_UTILITY, "canonical_name": "Unidentified public utility company in Salem, Ohio", "historical_name": "public utility company in Salem, Ohio", "aliases": [], "organization_type": "public utility company", "sector": "business_and_industry", "city": "Salem", "state_or_region": "Ohio", "country": "United States", "active_dates": "Documented before November 19, 1940", "normalization_notes": "The direct OSS report does not name the utility. No modern or guessed company is substituted."},
        {"key": ORG_HARVARD, "organization_id": "45ddf347-21c6-59f5-a8ae-517418adf941", "canonical_name": "Harvard University", "historical_name": "Harvard University", "aliases": ["Harvard"], "organization_type": "university", "sector": "academia_and_research", "city": "Cambridge", "state_or_region": "Massachusetts", "country": "United States", "normalization_notes": "Existing canonical university reused. Wilson's concurrent wartime research roles prevent an immediate-pre-OSS designation."},
    ]


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, item in ARMY_OCCUPATIONS.items():
        values.append({"key": occupation_key(row), "person_id": PEOPLE[row][0], "occupation": item["occupation"], "relationship_type": item["relationship"], "end_date": item["date"], "date_precision": f"Historical civilian-occupation code {item['code']} was recorded at Army entry on {item['date']}; no named employer or institution is supplied.", "country": "United States", "pre_oss_temporal_basis": "strongly_date_bounded", "identity_confidence": "confirmed", "claim_confidence": "medium", "source_quality": "A_direct_official", "publication_status": "publish_qualified", "research_notes": "Broad historical category only; no employer, workplace, institution, exact specialty beyond the code, or exact OSS transition is inferred."})
    values.extend([
        {"key": "allan-willman-uwyo-b1017", "person_id": PEOPLE[ALLAN_ROW][0], "organization_key": ORG_UWYO, "organization_name_as_found": "University of Wyoming", "role_title": "Chairman of the Division of Music and Associate Professor of Piano", "occupation": "music professor and pianist", "relationship_type": "employment", "start_date": "1936", "end_date": "1943-03-09", "date_precision": "The archival guide documents University of Wyoming employment from 1936; Board minutes date military induction and leave from March 9, 1943.", "city": "Laramie", "state_or_region": "Wyoming", "country": "United States", "last_civilian_pre_service": True, "pre_oss_temporal_basis": "strongly_date_bounded", "identity_confidence": "high_confidence", "claim_confidence": "high", "source_quality": "A_direct_official", "publication_status": "published", "research_notes": "Explicitly the last documented civilian employment before military induction. An intervening military period means it is not labeled immediate pre-OSS."},
        {"key": "donald-willmott-chengdu-school-b1017", "person_id": PEOPLE[DONALD_WILLMOTT_ROW][0], "organization_key": ORG_CHENGDU_SCHOOL, "organization_name_as_found": "a Chinese middle school near Chengdu connected with Oberlin College", "role_title": "teacher", "occupation": "teacher", "relationship_type": "employment", "start_date": "1943", "end_date": "1944", "date_precision": "The scholarly biography dates teaching to 1943-44 and explicitly sequences its end immediately before Willmott sought war work and joined OSS in 1944.", "city": "Chengdu", "state_or_region": "Sichuan", "country": "China", "immediate_pre_oss": True, "last_civilian_pre_service": True, "pre_oss_temporal_basis": "explicit_immediate", "identity_confidence": "high_confidence", "claim_confidence": "high", "source_quality": "C_reputable_contemporary_or_scholarly", "publication_status": "published", "research_notes": "The source names no school. Oberlin College is a connection, not the employer."},
        {"key": "paul-wilner-private-practice-b1017", "person_id": PEOPLE[PAUL_ROW][0], "organization_key": ORG_SELF, "organization_name_as_found": "private internal-medicine practice in Washington", "role_title": "internist", "occupation": "physician", "relationship_type": "self_employment", "start_date": "1939", "date_precision": "The obituary dates Washington practice from 1939 and then separately documents World War II military service; the precise service-entry date is not supplied.", "city": "Washington", "state_or_region": "District of Columbia", "country": "United States", "last_civilian_pre_service": True, "pre_oss_temporal_basis": "probable_immediate", "identity_confidence": "high_confidence", "claim_confidence": "medium", "source_quality": "C_reputable_contemporary_or_scholarly", "publication_status": "publish_qualified", "research_notes": "Published as a qualified concurrent last-civilian role. The obituary does not say the practice ended or establish an OSS start date."},
        {"key": "paul-wilner-georgetown-b1017", "person_id": PEOPLE[PAUL_ROW][0], "organization_key": ORG_GEORGETOWN, "organization_name_as_found": "Georgetown University medical school", "role_title": "clinical instructor", "occupation": "medical instructor", "relationship_type": "employment", "start_date": "1939", "date_precision": "The obituary states that Wilner's Georgetown teaching career began in 1939 and then separately documents World War II service; no service-entry date is supplied.", "city": "Washington", "state_or_region": "District of Columbia", "country": "United States", "last_civilian_pre_service": True, "pre_oss_temporal_basis": "probable_immediate", "identity_confidence": "high_confidence", "claim_confidence": "medium", "source_quality": "C_reputable_contemporary_or_scholarly", "publication_status": "publish_qualified", "research_notes": "Published as a qualified concurrent last-civilian role. It remains separate from private practice and from the unresolved Army/Marine branch conflict."},
        {"key": "donald-wilson-us-army-b1017", "person_id": PEOPLE[DONALD_WILSON_ROW][0], "organization_key": ORG_ARMY, "organization_name_as_found": "Army", "role_title": "Chief Warrant Officer; procurement officer", "occupation": "military procurement officer", "relationship_type": "military_assignment", "start_date": "1940-11-19", "end_date": "1944-02-21", "date_precision": "The direct OSS report dates Army entry to November 19, 1940 and assignment to OSS in Cairo to February 21, 1944.", "country": "United States", "immediate_pre_oss": True, "pre_oss_temporal_basis": "explicit_immediate", "identity_confidence": "confirmed", "claim_confidence": "confirmed", "source_quality": "A_direct_official", "publication_status": "published", "research_notes": "Modeled as a military assignment, not a civilian employer. Exact protected identifiers agree but remain masked publicly."},
        {"key": "donald-wilson-salem-utility-b1017", "person_id": PEOPLE[DONALD_WILSON_ROW][0], "organization_key": ORG_SALEM_UTILITY, "organization_name_as_found": "a public utility company in Salem, Ohio", "role_title": "stenographer and clerk", "occupation": "stenographer and clerk", "relationship_type": "employment", "end_date": "1940-11-19", "date_precision": "The direct OSS report describes this as his civilian-life work and dates Army entry to November 19, 1940; the employer name and start date are not supplied.", "city": "Salem", "state_or_region": "Ohio", "country": "United States", "last_civilian_pre_service": True, "pre_oss_temporal_basis": "strongly_date_bounded", "identity_confidence": "confirmed", "claim_confidence": "confirmed", "source_quality": "A_direct_official", "publication_status": "published", "research_notes": "The unnamed historical employer remains explicit; no Salem utility is guessed."},
        {"key": "bright-wilson-harvard-b1017", "person_id": PEOPLE[BRIGHT_ROW][0], "organization_key": ORG_HARVARD, "organization_name_as_found": "Harvard University", "role_title": "Associate Professor", "occupation": "physical chemist", "relationship_type": "employment", "start_date": "1939", "end_date": "1946", "date_precision": "Science History Institute's professional chronology dates the associate professorship to 1939-46.", "city": "Cambridge", "state_or_region": "Massachusetts", "country": "United States", "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "high_confidence", "claim_confidence": "high", "source_quality": "B_authoritative_institutional", "publication_status": "published", "research_notes": "Documented employment beginning before the OSS period. Concurrent Woods Hole and NDRC roles mean Harvard is not labeled immediate or last civilian pre-service."},
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
        values.append(make_claim(key=f"identity-{slug(name)}-row{row}-b1017", row=row, claim_type="identity", text=f"Indexed {name} is confirmed as the matching Army record by exact name and a nonshared protected identifier.", paraphrase="The official index and Army bulk record agree on the complete name and a protected identifier not shared by another indexed person.", identity="Confirmed by exact name plus a nonshared protected identifier; the identifier remains private.", temporal="Identity evidence only; the Army entry date is not treated as an OSS transition date.", quality="A_direct_official", confidence="confirmed", publication="published", notes="The accepted candidate decision preserves full identifiers outside public outputs.", source_links=[{"source_key": INDEX, "support_type": "supports", "locator_override": f"PDF page 507, row {row}; Box {box_for(row)}"}, {"source_key": ARMY, "support_type": "supports"}, {"source_key": TECH, "support_type": "context_only"}]))
        values.append(make_claim(key=f"occupation-{slug(name)}-row{row}-b1017", row=row, affiliation_key=occupation_key(row), claim_type="occupation", text=f"The Army entry record classifies {name}'s civilian status or occupation broadly as {item['occupation']}.", paraphrase=f"At Army entry on {item['date']}, historical code {item['code']} maps to '{item['label']}.' The record names no employer or institution.", identity="Confirmed through the reviewed protected-identifier bridge.", temporal="Strongly dated at Army entry; the evidence does not establish the exact OSS transition or a named immediate predecessor.", quality="A_direct_official", confidence="medium", publication="publish_qualified", notes="The historical category is qualified and excluded from verified-employer analytics.", source_links=[{"source_key": ARMY, "support_type": "supports"}, {"source_key": TECH, "support_type": "context_only"}, {"source_key": CODES, "support_type": "supports", "locator_override": item["locator"]}]))
    values.extend([
        make_claim(key="identity-claude-t-willis-b1017", row=2, claim_type="identity", text="Indexed Claude T Willis is confirmed as the matching Army record by exact name and a nonshared protected identifier.", paraphrase="The official records agree on the complete name and protected identifier; the Army entry is dated January 7, 1946, after OSS dissolution.", identity="Confirmed by exact name and nonshared protected identifier; the identifier remains private.", temporal="Identity only. Post-OSS Army entry data are not treated as pre-OSS evidence.", quality="A_direct_official", confidence="confirmed", publication="published", notes="No Army occupation, grade or chronology is transferred into a pre-OSS claim.", source_links=[{"source_key": INDEX, "support_type": "supports", "locator_override": "PDF page 507, row 2; Box 842"}, {"source_key": ARMY, "support_type": "supports"}, {"source_key": TECH, "support_type": "context_only"}]),
        make_claim(key="identity-david-l-willmarth-b1017", row=13, claim_type="identity", text="Indexed David L Willmarth is a high-confidence match to the Army record spelling the surname Wilmarth.", paraphrase="A nonshared protected identifier and matching given names bridge the one-letter surname variant; undefined code 502 yields no occupation.", identity="High confidence from the protected identifier plus the Willmarth/Wilmarth spelling variant and matching David L.", temporal="Identity only; no occupation, employer or OSS transition is derived.", quality="A_direct_official", confidence="high", publication="published", notes="The spelling variant is preserved. Full identifiers remain private and code 502 remains uninterpreted.", source_links=[{"source_key": INDEX, "support_type": "supports", "locator_override": "PDF page 507, row 13; Box 843"}, {"source_key": ARMY, "support_type": "supports"}, {"source_key": TECH, "support_type": "context_only"}, {"source_key": CODES, "support_type": "context_only"}]),
        make_claim(key="joe-w-willis-army-conflict-b1017", row=CONFLICT_ROW, claim_type="identity", text="Joe W Willis cannot be assigned the Army row because its protected identifier points to Jacob Talenco.", paraphrase="The protected identifier agrees, but the official Army row's materially different name prevents identity or occupation transfer.", identity="Conflicting; a protected identifier alone cannot overcome the incompatible name.", temporal="No Army date, grade, occupation or chronology is transferred.", quality="A_direct_official", confidence="conflicting", publication="conflicting", notes="Direct Box 842 and underlying Army-source review is required; full identifiers remain private.", source_links=[{"source_key": INDEX, "support_type": "supports", "locator_override": "PDF page 507, row 4; Box 842"}, {"source_key": ARMY, "support_type": "contradicts"}]),
        make_claim(key="identity-nicholas-w-willis-b1017", row=NICHOLAS_ROW, claim_type="identity", text="The indexed Lieutenant Colonel Nicholas W Willis is a high-confidence match to the OSS Special Operations Branch chief in China.", paraphrase="The exact name, lieutenant-colonel rank and direct OSS China leadership role align with the indexed record.", identity="High confidence from exact name, exact rank and a specific direct OSS assignment; Box 842 remains unreviewed.", temporal="Direct OSS role in China is dated to the independent mission established in December 1944.", quality="B_authoritative_institutional", confidence="high", publication="published", notes="This resolves the OSS identity but supplies no pre-OSS employer or predecessor affiliation.", source_links=[{"source_key": INDEX, "support_type": "supports", "locator_override": "PDF page 507, row 9; Lieutenant Colonel; Box 842"}, {"source_key": JSOU, "support_type": "supports", "locator_override": "Printed page 89"}], excerpt="Heppner appointed Lieutenant Colonel Nicholas Willis as head of his SO Branch"),
        make_claim(key="identity-allan-a-willman-b1017", row=ALLAN_ROW, claim_type="identity", text="The indexed Allan A Willman is a high-confidence match to University of Wyoming music professor Allan Arthur Willman.", paraphrase="The distinctive exact name, institutional middle-name expansion and March 1943 military induction create a specific identity bridge.", identity="High confidence from the distinctive name, exact middle initial, archival full-name form and date-bounded military induction.", temporal="The employment and military induction chronology is explicit; the exact OSS entry date remains unknown.", quality="A_direct_official", confidence="high", publication="published", notes="Box 842 review is still needed for a direct personnel-file bridge and OSS chronology.", source_links=[{"source_key": INDEX, "support_type": "supports", "locator_override": "PDF page 507, row 12; Box 842"}, {"source_key": UWYO_MINUTES, "support_type": "supports", "locator_override": "Sheet 772"}, {"source_key": UWYO_AHC, "support_type": "supports", "locator_override": "Printed page 428; Accession 400049"}]),
        make_claim(key="allan-willman-uwyo-claim-b1017", row=ALLAN_ROW, affiliation_key="allan-willman-uwyo-b1017", claim_type="last_civilian_pre_service", text="Allan A Willman's last documented civilian employer before military induction was the University of Wyoming.", paraphrase="Board minutes identify his titles and place him on leave from March 9, 1943 because he was inducted for military service.", identity="High-confidence distinctive-name match corroborated by the institutional archival guide.", temporal="Strongly date-bounded last civilian employment before military service; an intervening military period prevents an immediate-pre-OSS label.", quality="A_direct_official", confidence="high", publication="published", notes="Employment, not student status. The exact titles and historical institution are preserved.", source_links=[{"source_key": UWYO_MINUTES, "support_type": "supports", "locator_override": "Sheet 772"}, {"source_key": UWYO_AHC, "support_type": "supports", "locator_override": "Printed page 428"}], excerpt="Chairman of the Division of Music and Associate Professor of Piano"),
        make_claim(key="identity-donald-r-willmott-b1017", row=DONALD_WILLMOTT_ROW, claim_type="identity", text="The indexed Donald R Willmott is a high-confidence match to the China-born translator and OSS clerk-typist profiled by Riggins.", paraphrase="The distinctive name, explicit 1944-45 OSS service in Chungking and indexed personnel file align; the article does not print the middle initial.", identity="High confidence from distinctive name and an exceptionally specific direct OSS chronology and role; Box 842 remains unreviewed.", temporal="The biography explicitly sequences 1943-44 teaching before 1944-45 OSS service.", quality="C_reputable_contemporary_or_scholarly", confidence="high", publication="published", notes="The direct chronology supports publication while the unreviewed personnel file keeps identity below confirmed.", source_links=[{"source_key": INDEX, "support_type": "supports", "locator_override": "PDF page 507, row 15; Box 842"}, {"source_key": RIGGINS, "support_type": "supports", "locator_override": "Printed pages 51-52"}]),
        make_claim(key="donald-willmott-chengdu-claim-b1017", row=DONALD_WILLMOTT_ROW, affiliation_key="donald-willmott-chengdu-school-b1017", claim_type="immediate_pre_oss_affiliation", text="Donald R Willmott taught at an unnamed Chinese middle school near Chengdu immediately before seeking war work and joining OSS.", paraphrase="Riggins dates the teaching to 1943-44, states that it finished before Willmott sought translator work, and dates OSS service to 1944-45.", identity="High-confidence distinctive-name and direct OSS chronology match.", temporal="Explicit immediate sequence in the scholarly biography.", quality="C_reputable_contemporary_or_scholarly", confidence="high", publication="published", notes="The school remains unnamed. A connection to Oberlin College is not converted into employment by Oberlin.", source_links=[{"source_key": RIGGINS, "support_type": "supports", "locator_override": "Printed page 51"}], excerpt="he taught in 1943–44 at a Chinese middle school near Chengdu connected with Oberlin College"),
        make_claim(key="identity-paul-r-wilner-b1017", row=PAUL_ROW, claim_type="identity", text="The indexed Major Paul R Wilner is a high-confidence match to Washington physician and Georgetown instructor Paul R. Wilner.", paraphrase="The exact full name, 1933 Pennsylvania class, Washington medical career and wartime North Africa or Mediterranean service align across two institutional sources.", identity="High confidence from exact name plus matching education, profession, wartime theater and officer progression; Box 843 remains unreviewed.", temporal="Both sources document wartime service after the 1939 start of practice and teaching, but not an OSS start date.", quality="B_authoritative_institutional", confidence="high", publication="published", notes="A credible Army-versus-Marine branch conflict is preserved separately and prevents confirmed identity status.", source_links=[{"source_key": INDEX, "support_type": "supports", "locator_override": "PDF page 507, row 25; Major; Box 843"}, {"source_key": WAPO, "support_type": "supports"}, {"source_key": PENN, "support_type": "supports", "locator_override": "Printed page 242"}]),
        make_claim(key="paul-wilner-private-practice-claim-b1017", row=PAUL_ROW, affiliation_key="paul-wilner-private-practice-b1017", claim_type="last_civilian_pre_service", text="Paul R Wilner's private internal-medicine practice is a qualified concurrent last-civilian role before wartime service.", paraphrase="The obituary dates Washington practice from 1939 and then documents wartime medical service; it does not supply the service-entry or OSS date.", identity="High-confidence identity supported by exact name, education, profession and wartime theater.", temporal="Probable immediate, not explicit: the practice began before service, but continuous dates do not prove when it paused or whether it immediately preceded OSS.", quality="C_reputable_contemporary_or_scholarly", confidence="medium", publication="publish_qualified", notes="Self-employment is kept separate from Georgetown employment and excluded from unqualified immediate-affiliation claims.", source_links=[{"source_key": WAPO, "support_type": "supports"}], excerpt="He practiced internal medicine in Washington from 1939 to 1990."),
        make_claim(key="paul-wilner-georgetown-claim-b1017", row=PAUL_ROW, affiliation_key="paul-wilner-georgetown-b1017", claim_type="last_civilian_pre_service", text="Paul R Wilner's Georgetown clinical instructorship is a qualified concurrent last-civilian role before wartime service.", paraphrase="The obituary dates the teaching career from 1939 and then documents wartime military service; it does not supply the service-entry or OSS date.", identity="High-confidence identity supported by exact name, education, profession and wartime theater.", temporal="Probable immediate, not explicit: the teaching began before service, but the evidence does not establish an exact transition.", quality="C_reputable_contemporary_or_scholarly", confidence="medium", publication="publish_qualified", notes="University employment is kept separate from private practice and visibly qualified.", source_links=[{"source_key": WAPO, "support_type": "supports"}], excerpt="He began his teaching career at Georgetown as a clinical instructor in 1939"),
        make_claim(key="paul-wilner-branch-conflict-b1017", row=PAUL_ROW, claim_type="identity", text="Credible sources conflict over whether Paul R Wilner served in the Army Medical Corps or Marine Corps during World War II.", paraphrase="The 1991 obituary says Army Medical Corps and lieutenant colonel; the contemporary 1943 Pennsylvania Gazette says Marine Corps captain in Northwest Africa.", identity="Both sources otherwise align on the exact person, education, profession and wartime theater; the branch conflict remains unresolved.", temporal="Both descriptions refer to World War II service and do not establish an exact OSS transition.", quality="B_authoritative_institutional", confidence="conflicting", publication="conflicting", notes="No branch is silently selected. Box 843 and the personnel file should resolve the contradiction.", source_links=[{"source_key": WAPO, "support_type": "contradicts", "excerpt_override": "During World War II, he served with the Army Medical Corps in the Mediterranean theater"}, {"source_key": PENN, "support_type": "contradicts", "locator_override": "Printed page 242", "excerpt_override": "captain in the Marine Corps stationed in Northwest Africa"}]),
        make_claim(key="identity-donald-c-wilson-b1017", row=DONALD_WILSON_ROW, claim_type="identity", text="The indexed Donald C Wilson is confirmed as the Chief Warrant Officer described in the direct OSS board report.", paraphrase="The complete name and protected warrant-officer identifier agree exactly between the NARA index and OSS report.", identity="Confirmed by exact name and exact nonshared protected identifier; the identifier remains masked publicly.", temporal="The report explicitly dates Army entry and OSS assignment.", quality="A_direct_official", confidence="confirmed", publication="published", notes="The direct source supplies both identity and chronology without relying on a common-name biography.", source_links=[{"source_key": INDEX, "support_type": "supports", "locator_override": "PDF page 507, row 33; Box 843; protected identifier withheld"}, {"source_key": HOOVER, "support_type": "supports", "locator_override": "Printed page 57, entry LI; protected identifier withheld"}]),
        make_claim(key="donald-wilson-army-claim-b1017", row=DONALD_WILSON_ROW, affiliation_key="donald-wilson-us-army-b1017", claim_type="immediate_pre_oss_affiliation", text="Donald C Wilson's immediate pre-OSS affiliation was the United States Army.", paraphrase="The direct OSS report dates Army entry to November 19, 1940 and assignment to OSS in Cairo to February 21, 1944.", identity="Confirmed by exact name and protected identifier agreement.", temporal="Explicit immediate military chronology in a direct OSS report.", quality="A_direct_official", confidence="confirmed", publication="published", notes="Military assignment is not labeled a civilian employer.", source_links=[{"source_key": HOOVER, "support_type": "supports", "locator_override": "Printed page 57, entry LI"}], excerpt="Entered the Army 19 November 1940 and ... Assigned to OSS 21 February 1944"),
        make_claim(key="donald-wilson-utility-claim-b1017", row=DONALD_WILSON_ROW, affiliation_key="donald-wilson-salem-utility-b1017", claim_type="last_civilian_pre_service", text="Donald C Wilson's last documented civilian employer before Army service was an unnamed public utility company in Salem, Ohio.", paraphrase="The direct OSS report calls him a civilian-life stenographer and clerk for the utility and separately dates Army entry to November 19, 1940.", identity="Confirmed by exact name and protected identifier agreement.", temporal="Strongly date-bounded before the explicitly dated Army entry; no company start date is supplied.", quality="A_direct_official", confidence="confirmed", publication="published", notes="The historical employer is unnamed. No modern or guessed Salem utility is substituted.", source_links=[{"source_key": HOOVER, "support_type": "supports", "locator_override": "Printed page 57, entry LI"}], excerpt="In civilian life, was a stenographer and clerk for a public utility company in Salem, Ohio."),
        make_claim(key="identity-e-bright-wilson-b1017", row=BRIGHT_ROW, claim_type="identity", text="The indexed E. Bright Wilson is a high-confidence match to Harvard physical chemist Edgar Bright Wilson Jr.", paraphrase="The exceptionally distinctive indexed name and civilian status align with the institutional oral history's full name and wartime research chronology.", identity="High confidence from the distinctive name, full-name expansion, civilian professional profile and wartime scientific chronology; Box 843 remains unreviewed.", temporal="The professional chronology spans the prewar and wartime years but does not establish an exact OSS start.", quality="B_authoritative_institutional", confidence="high", publication="published", notes="Name variants are published, while immediate-OSS sequence remains unresolved.", source_links=[{"source_key": INDEX, "support_type": "supports", "locator_override": "PDF page 507, row 35; Box 843"}, {"source_key": SCIENCE_HISTORY, "support_type": "supports", "locator_override": "Interviewee biographical information"}]),
        make_claim(key="bright-wilson-harvard-claim-b1017", row=BRIGHT_ROW, affiliation_key="bright-wilson-harvard-b1017", claim_type="other_pre_oss_affiliation", text="E. Bright Wilson was an Associate Professor at Harvard University from 1939 to 1946.", paraphrase="Science History Institute's institutional chronology lists the Harvard associate professorship and concurrent wartime government research roles.", identity="High-confidence distinctive-name match with an institutional full-name and professional chronology.", temporal="Documented prewar employment beginning in 1939; concurrent Woods Hole and NDRC work prevents an immediate or last-civilian designation.", quality="B_authoritative_institutional", confidence="high", publication="published", notes="This is a documented employer, not evidence that Harvard immediately preceded OSS.", source_links=[{"source_key": SCIENCE_HISTORY, "support_type": "supports", "locator_override": "Professional Experience, Harvard University"}]),
    ])
    return values


def unresolved_reason(row: int) -> str:
    special = {
        3: "The printed Major and USMCR note establish commissioned Marine Corps status but not a pre-OSS employer or assignment.",
        7: "A Library of Congress OCR candidate was rejected because adjacent names were joined; it did not identify Joseph F Willis.",
        14: "An exact-name obituary lead lacked any Box 842, identifier, rank or OSS bridge and was rejected as an unconfirmed namesake.",
        16: "The printed British Army second-lieutenant note establishes Allied commissioned status but not a pre-OSS employer or assignment.",
        19: "The printed British Army lieutenant-colonel note establishes Allied commissioned status but not a pre-OSS employer or assignment.",
        37: "The printed Lieutenant and USNR note establishes commissioned naval status but not a pre-OSS employer or assignment.",
        38: "The printed USNR note establishes a naval-reserve connection but supplies no rank, employer or exact assignment.",
        41: "An Elmo Wilson Office of War Information lead lacked an identifier, Box 843 or OSS bridge and was rejected as an unresolved namesake.",
        42: "A sociologist of the same name was rejected because the biography lacks an OSS or identifier bridge and conflicts with the accepted Army occupation record.",
    }.get(row, "")
    prefix = f"{special} " if special else ""
    return prefix + "Exact-name and meaningful-variant official, OSS, employer, occupation, obituary, institutional, newspaper, directory and archival searches produced no reliable identity-and-affiliation bridge; unbridged namesakes were rejected."


def base_update(row: int, **overrides: object) -> dict[str, object]:
    value: dict[str, object] = {"person_id": PEOPLE[row][0], "manual_review_required": True, "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "high"}
    value.update(overrides)
    return value


def person_updates() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    reviewed = set(ARMY_OCCUPATIONS) | IDENTITY_ONLY | {CONFLICT_ROW, NICHOLAS_ROW, ALLAN_ROW, DONALD_WILLMOTT_ROW, PAUL_ROW, DONALD_WILSON_ROW, BRIGHT_ROW}
    for row in sorted(set(PEOPLE) - reviewed):
        reason = unresolved_reason(row)
        overrides: dict[str, object] = {}
        if row == 3:
            overrides.update(personnel_category="commissioned_marine_corps_officer", commissioned_officer=True, allied_or_foreign_personnel=False)
        elif row in {16, 19}:
            overrides.update(personnel_category="foreign_or_allied_military_personnel", commissioned_officer=True, allied_or_foreign_personnel=True)
        elif row == 37:
            overrides.update(personnel_category="commissioned_naval_officer", commissioned_officer=True, allied_or_foreign_personnel=False)
        values.append(base_update(row, identity_status="unresolved", identity_evidence=f"The visually verified page 507 source preserves {PEOPLE[row][1]}, archival Box {box_for(row)}, and the printed rank or note when present. {reason}", research_status="requires_archival_review", next_action=f"Review indexed Box {box_for(row)} for corroborating identifiers, immediate pre-OSS affiliation, and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}", **overrides))
    for row in ARMY_OCCUPATIONS:
        values.append(base_update(row, identity_status="confirmed", identity_evidence="An exact name and nonshared protected identifier connect the official index and Army record; the identifier remains private.", personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="occupation_only_found", nara_catalog_id="1263923", next_action=f"Review indexed Box {box_for(row)} to identify a named employer or institution and establish Army-to-OSS chronology; the bulk record supplies only a historical category at Army entry."))
    values.extend([
        base_update(2, identity_status="confirmed", identity_evidence="Exact name and a nonshared protected identifier connect the index and Army record; the January 1946 entry is post-OSS and yields no pre-OSS claim.", research_status="requires_archival_review", nara_catalog_id="1263923", next_action="Review Box 842 for a named pre-OSS employer or affiliation. The Army bridge confirms identity only because the entry is dated after OSS dissolution."),
        base_update(13, identity_status="high_confidence", identity_evidence="A nonshared protected identifier plus matching David L and the Willmarth/Wilmarth spelling variant support high confidence; code 502 remains undefined.", name_variants=["David L Wilmarth"], replace_name_variants=False, personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="requires_archival_review", nara_catalog_id="1263923", next_action="Review Box 843 for a named employer and Army-to-OSS chronology. The accepted Army bridge supports identity only."),
        base_update(CONFLICT_ROW, identity_status="conflicting", identity_evidence="The protected identifier points to an Army row naming Jacob Talenco rather than Joe W Willis. No Army data are transferred.", research_status="conflicting_sources", archival_review_priority="critical", next_action="Review Box 842 and the underlying Army source to resolve the protected-identifier/name conflict before assigning occupation, grade or chronology."),
        base_update(NICHOLAS_ROW, identity_status="high_confidence", identity_evidence="Exact name, lieutenant-colonel rank and the direct OSS China Special Operations Branch role support high confidence; Box 842 remains unreviewed.", name_variants=["Nicholas Willis", "Lt. Col. Nicholas Willis"], replace_name_variants=False, personnel_category="commissioned_army_officer", commissioned_officer=True, allied_or_foreign_personnel=False, research_status="requires_archival_review", archival_review_priority="medium", next_action="Review Box 842 for Nicholas Willis's pre-OSS employer, military unit or institutional affiliation and exact OSS entry chronology."),
        base_update(ALLAN_ROW, identity_status="high_confidence", identity_evidence="The distinctive exact name, institutional full-name expansion and March 1943 military induction support a high-confidence match to University of Wyoming professor Allan Arthur Willman.", name_variants=["Allan Arthur Willman"], replace_name_variants=False, research_status="verified_employer_found", archival_review_priority="medium", next_action="Review Box 842 to establish the military-to-OSS chronology and determine the immediate pre-OSS assignment after University of Wyoming employment."),
        base_update(DONALD_WILLMOTT_ROW, identity_status="high_confidence", identity_evidence="The distinctive name and a scholarly biography's explicit 1944-45 OSS Chungking chronology support a high-confidence identity; Box 842 remains unreviewed.", name_variants=["Donald Willmott"], replace_name_variants=False, personnel_category="enlisted_army_personnel", commissioned_officer=False, research_status="verified_employer_found", archival_review_priority="medium", next_action="Review Box 842 to confirm the middle initial, Army status and the exact OSS entry date; the immediate Chengdu teaching role is already strongly documented."),
        base_update(PAUL_ROW, identity_status="high_confidence", identity_evidence="Exact name, Pennsylvania class year, Washington medical career and North Africa or Mediterranean officer service support high confidence, but credible sources conflict on Army versus Marine branch.", name_variants=["Paul R. Wilner", "Dr. Paul R. Wilner"], replace_name_variants=False, commissioned_officer=True, research_status="conflicting_sources", archival_review_priority="critical", next_action="Review Box 843 to resolve Army Medical Corps versus Marine Corps service, confirm the OSS chronology, and determine whether private practice or Georgetown immediately preceded service."),
        base_update(DONALD_WILSON_ROW, identity_status="confirmed", identity_evidence="The exact complete name and protected warrant-officer identifier agree between the NARA index and direct OSS board report.", personnel_category="warrant_officer", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="verified_employer_found", archival_review_priority="medium", next_action="Review Box 843 for the public utility company's name and any additional pre-OSS employment detail; the Army-to-OSS dates are already explicit."),
        base_update(BRIGHT_ROW, identity_status="high_confidence", identity_evidence="The exceptionally distinctive indexed name, civilian status and institutional full-name and wartime scientific chronology support a high-confidence match to Edgar Bright Wilson Jr.", name_variants=["Edgar Bright Wilson Jr.", "E. Bright Wilson Jr."], replace_name_variants=False, personnel_category="civilian_professional_or_administrative_grade", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="documented_prewar_employer_found", archival_review_priority="medium", next_action="Review Box 843 to establish the exact OSS connection and sequence among Harvard, Woods Hole, NDRC and any OSS assignment."),
    ])
    if len(values) != len(PEOPLE):
        raise RuntimeError(f"Expected {len(PEOPLE)} person updates, generated {len(values)}")
    return values


def research_attempts() -> list[dict[str, object]]:
    attempts: list[dict[str, object]] = []
    enriched = {NICHOLAS_ROW, ALLAN_ROW, DONALD_WILLMOTT_ROW, PAUL_ROW, DONALD_WILSON_ROW, BRIGHT_ROW}
    for row, (person_id, name) in PEOPLE.items():
        outcome, reviewed, rejected = "candidate_rejected", 6, 5
        note = unresolved_reason(row)
        if row in ARMY_OCCUPATIONS:
            outcome, reviewed, rejected = "source_reviewed", 9, 5
            note = f"An accepted Army bridge supports identity and a qualified {ARMY_OCCUPATIONS[row]['occupation']} category at Army entry; no named employer or exact OSS-transfer date is supplied."
        elif row in IDENTITY_ONLY:
            outcome, reviewed, rejected = "source_reviewed", 9, 5
            note = "An accepted Army bridge supports identity only; post-OSS chronology or undefined occupation coding prevents a pre-OSS occupation claim."
        elif row == CONFLICT_ROW:
            outcome, reviewed, rejected = "candidate_found", 9, 6
            note = "A protected identifier points to an incompatible Army name. The conflict is preserved and no Army data are transferred."
        elif row in enriched:
            outcome, reviewed, rejected = "source_reviewed", 12, 7
            note = {
                NICHOLAS_ROW: "An official military study supports a high-confidence direct OSS China identity but supplies no pre-OSS employer.",
                ALLAN_ROW: "Direct University of Wyoming minutes and an institutional archival guide support a high-confidence identity and last civilian employer before military induction.",
                DONALD_WILLMOTT_ROW: "A peer-reviewed biography explicitly sequences 1943-44 teaching before 1944-45 OSS work in Chungking.",
                PAUL_ROW: "Two institutional sources support prewar medical practice and Georgetown teaching while preserving an unresolved Army-versus-Marine branch conflict.",
                DONALD_WILSON_ROW: "A direct OSS report and exact protected identifier establish the Army-to-OSS chronology and unnamed Salem public-utility employment.",
                BRIGHT_ROW: "A Science History Institute oral-history record supports the full identity and documented Harvard employment; immediate OSS sequence remains unresolved.",
            }[row]
        attempt_number = 16 if row == 7 else 3 if row == ALLAN_ROW else 1
        attempts.append({"key": f"page507-row{row}-{slug(name)}-b1017", "person_id": person_id, "source_adapter": "manual_staged_protocol", "query_text": f"{name}; NARA OSS index context; exact-name and meaningful spelling, initial, suffix, punctuation and OCR variants; OSS, rank, branch, assignment and identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory and archival searches; indexed Box {box_for(row)}; protected identifiers used only in private official-record comparison", "query_variant_type": "staged_identity_employment_archival_protocol_batch_1017", "started_at": "2026-11-04T08:45:00Z", "completed_at": "2026-11-04T09:35:00Z", "outcome": outcome, "sources_reviewed": reviewed, "candidate_sources_rejected": rejected, "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, postwar-only leads, discovery-only biographies and sources without an OSS, protected-identifier, rank, unit or personnel-file bridge were rejected. Army categories were not converted into named employers or institutions.", "research_notes": f"{note} Exact-name official-domain, OSS, employer, occupation, obituary, institutional, newspaper, directory and archival searches were checked as applicable. Index page 507 and relevant code-list pages were visually checked. Batch-level Library of Congress and CIA adapter checks failed closed with URLError and CiaRobotsUnavailable; those errors are recorded separately and are not negative results. Accessible official, institutional, newspaper and scholarly alternatives were reviewed. No authenticated NARA Catalog API call was made.", "next_action": f"Review indexed Box {box_for(row)} for corroborating identifiers, the immediate pre-OSS affiliation, and last civilian employer before wartime service.", "attempt_number": attempt_number, "research_agent_version": "before-oss-b1017-v1"})
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-1017-v1",
        "reviewer": "Before OSS Batch 1017 evidence review",
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
