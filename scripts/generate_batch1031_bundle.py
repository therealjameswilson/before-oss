#!/usr/bin/env python3
"""Generate the reviewed Batch 1031 evidence bundle for PDF page 521."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page521-ernest-zimmerman-to-charles-zuccardy-review_"
    "batch-1031_2026-11-04.json"
)

INDEX = "nara-index-b1031"
ARMY = "army-bulk-b1031"
TECH = "army-tech-b1031"
CODES = "army-codes-b1031"
LEGACY_ZINNER = "legacy-paul-zinner-b1031"
TUFTS = "tufts-paul-zinner-b1031"
CIA_ZINDER = "cia-sauerkrauts-zinder-b1031"
HDIPLO_ZINDER = "hdiplo-zinder-linder-b1031"
WAPO_ZLOTNICK = "wapo-zlotnick-b1031"
CORNELL_ZUBKOFF = "cornell-zubkoff-b1031"
IRE_ZOSCHKE = "ire-zoschke-b1031"
POSTGAZETTE_ZOTTER = "postgazette-zotter-b1031"
OSSOG = "ossog-z-personnel-b1031"
RITCHIE = "ritchie-zuccardy-b1031"

ORG_US_ARMY = "united-states-army-b1031"
ORG_BRITISH_ARMY = "british-army-b1031"
ORG_FOREIGN_LEGION = "french-foreign-legion-b1031"
ORG_TUFTS = "tufts-college-b1031"
ORG_CORNELL = "cornell-university-b1031"
ORG_IRE = "institute-radio-engineers-b1031"


PEOPLE = {
    1: ("91593a93-75d8-536e-aa31-9153ffaf4a4b", "Ernest W Zimmerman", "863"),
    2: ("b577b8a4-4618-51b5-957e-139367cf3d3d", "Norma G Zimmerman", "863"),
    3: ("6f6e062b-e5bb-5960-a258-c6335d16dff8", "Philip Zimmerman", "863"),
    4: ("dd82710a-35b9-5b68-ba90-6af65873b1f2", "William P Zimmerman", "863"),
    5: ("6fa506fd-02fe-5951-89d6-eecf9737c04c", "John M Zimmy", "863"),
    6: ("89903963-283b-5ff8-b5ea-5bfa880015e0", "Edmund F Zinder", "863"),
    7: ("6470f008-0e38-5acf-8a7e-9e01a1a3f23f", "Edward Zinder", "454"),
    8: ("96da891b-8867-5e4b-8409-e86c7884290c", "Montague H Zink", "863"),
    9: ("abcdbcf0-31ac-557c-b1fe-11aeb010bfcb", "Francis L Zinkand", "863"),
    10: ("69bd8d05-b22b-5382-8aec-eeddcd3f7fa7", "Frederick W Zinn", "863"),
    11: ("c614bd2d-fa23-5429-9ab3-fe7c27c43e56", "Alfons Zinner", "864"),
    12: ("3a8f7bc4-91e6-526a-9896-3b35a9da3a6a", "Paul E Zinner", "864"),
    13: ("e2d5f662-a8ea-5506-87ec-d99f79a6b8b1", "William J Zinno", "864"),
    14: ("16823de2-99fb-5bc3-a584-7e7de7005c6a", "Zygmund Ziolo", "864"),
    15: ("ad20fe54-bf86-5e29-8dcb-7b2fe852085e", "Barney S Zipes", "864"),
    16: ("30323052-1107-580c-b87f-85635aec0ff8", "Domonick J Zippelli", "864"),
    17: ("2f85e9bd-1a7b-597b-a0d8-cffaa403b403", "Leopold Zippin", "864"),
    18: ("9b852743-7c54-5620-b3f8-f6ae4eeefcdc", "Bruno V Zipser", "864"),
    19: ("21a56e05-3776-582e-9b16-70979f2f5273", "Bruno P Zipser", "864"),
    20: ("66280441-bb60-5b7d-b629-c341e00b412e", "Anthony Zirilli", "864"),
    21: ("9bec50ef-41da-5c1b-884a-96f6714d3875", "Edward C Zirkel", "864"),
    22: ("91b0b65b-38a9-573d-bee5-4593d906efa6", "Jean B Zissu", "864"),
    23: ("6069ad8f-0f7a-5772-b10f-243bea84c6e0", "Theodore B Zissu", "864"),
    24: ("be9a4d1c-d3a4-5fb7-b408-30c283a28f85", "Joseph Zito", "864"),
    25: ("ec3090fd-6a73-556e-82cc-a14399d2e4bf", "Louella M Zitzlisperger", "864"),
    26: ("cdb303f6-f4d4-5139-9b70-228afac84ed2", "Gilbert J Zivin", "864"),
    27: ("bd18c2fb-141c-52ea-a853-08b44637db52", "Jack Zlotnick", "864"),
    28: ("9effb5bc-22d1-5800-ad39-b8b2372203ff", "John J Zloza", "864"),
    29: ("725f1b30-f216-5d48-9a0c-2ab274dcad2d", "Frank V Zobatta", "864"),
    30: ("fb343e12-80c8-5b19-a2a0-a4a658c3bc22", "David Zobolovsky", "864"),
    31: ("98af41a7-754a-5603-8089-ddb11fbf3428", "Marvin G Zoch", "864"),
    32: ("05854557-f4df-5c19-a1e8-944b5907f43c", "Michael G Zoldi", "864"),
    33: ("9fc86e1a-281e-5f0b-82ff-ec7bd3cb3e26", "Keith W Zollinger", "864"),
    34: ("c209549f-0226-5253-854f-f15261e61ccc", "Jack N Zonana", "865"),
    35: ("415fa958-1b38-5f4f-b787-841aedc35e5f", "James Zonas", "865"),
    36: ("c9622e08-04bd-5076-a1d2-4d885fee5eee", "Raymond L Zonca", "865"),
    37: ("8379828c-c96d-511c-9bb8-8703154d24fc", "John W Zonenberg", "865"),
    38: ("f4c60409-21b0-53d5-ad18-dead7059eaa6", "Irene E Zorbas", "865"),
    39: ("3c07772b-8e42-5430-afad-17144efc49f3", "Jack H Zoschke", "865"),
    40: ("33d47af8-121c-5683-a5e9-ed5caa04cf1d", "Andgelo C Zotos", "865"),
    41: ("b2a9b748-4995-5757-9a20-59df588060a8", "Louis Zotter Jr.", "865"),
    42: ("f43d5dcf-bf07-5f39-9cd5-99b1f0e27f74", "Victor F Zrinyi", "865"),
    43: ("bf5175ac-57f6-528e-955a-876195b603f6", "Joseph Zsiba", "865"),
    44: ("64783aa3-7beb-56d7-90b1-09046ac6a0b8", "Maurice J Zubkoff", "865"),
    45: ("a593d570-1da7-55ae-9cf7-9bdb17bdcd24", "Michael Zubrick", "865"),
    46: ("51414282-6d0d-5b24-98b4-ee9032d42b03", "Charles A Zuccardy", "865"),
}


# Accepted, date-bounded Army categories whose historical definitions were checked.
# Undefined codes 502 and 324, shared/conflicting links, and the January 1946
# Zonenberg record are excluded. Duplicate Zippin bulk rows produce one claim.
ARMY_OCCUPATIONS = {
    4: ("1941-01-27", "001", "accountant or auditor", "Accountants and auditors", "PDF physical page 170"),
    5: ("1942-01-06", "583", "repairman or mechanic, not elsewhere classified", "Repairmen and mechanics, n.e.c.", "PDF physical page 176"),
    13: ("1942-12-30", "125", "office-machine operator", "Office machine operators", "PDF physical page 172"),
    15: ("1942-05-20", "175", "salesperson", "Salesmen and sales agents, except to consumers", "PDF physical page 172"),
    16: ("1942-10-22", "627", "textile-products fabrication worker", "Semiskilled occupations in fabrication of textile products, n.e.c.", "PDF physical page 177"),
    17: ("1942-06-29", "022", "lawyer or judge", "Lawyers and judges", "PDF physical page 170"),
    18: ("1943-10-05", "448", "pressman or plate printer", "Pressmen and plate printers, printing", "PDF physical page 174"),
    21: ("1942-02-13", "068", "semiprofessional occupation, not elsewhere classified", "Semiprofessional occupations, n.e.c.", "PDF physical page 171"),
    22: ("1943-03-15", "091", "purchasing agent or buyer, not elsewhere classified", "Purchasing agents and buyers, n.e.c.", "PDF physical page 171"),
    23: ("1943-03-15", "019", "mechanical engineer", "Mechanical engineers", "PDF physical page 170"),
    24: ("1942-12-01", "727", "construction or maintenance painter", "Painters, construction and maintenance", "PDF physical page 179"),
    26: ("1942-12-12", "992", "student", "Students", "PDF physical page 304; amended category 9-92"),
    27: ("1942-12-16", "137", "stenographer or typist", "Stenographers and typists", "PDF physical page 172"),
    28: ("1942-09-24", "678", "machine-shop worker", "Semiskilled machine-shop and related occupations, n.e.c.", "PDF physical page 178"),
    33: ("1941-08-05", "002", "actor or actress", "Actors and actresses", "PDF physical page 170"),
    40: ("1942-11-27", "661", "shoe-manufacturing worker", "Semiskilled occupations in manufacture of boots and shoes", "PDF physical page 178"),
    42: ("1943-04-03", "949", "transportation occupation, not elsewhere classified", "Transportation occupations, n.e.c.", "PDF physical page 181"),
    43: ("1943-04-17", "448", "pressman or plate printer", "Pressmen and plate printers, printing", "PDF physical page 174"),
    44: ("1942-11-05", "992", "student", "Students", "PDF physical page 304; amended category 9-92"),
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def source(key: str, **kwargs: object) -> dict[str, object]:
    value: dict[str, object] = {"key": key, "access_date": "2026-11-04"}
    value.update(kwargs)
    return value


def sources() -> list[dict[str, object]]:
    return [
        source(INDEX, stable_url="https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf", archival_identifier="RG 226, Entry A1-224, Boxes 454 and 863-865", title="OSS Personnel Files from Excel", author_creator="National Archives and Records Administration", repository_publisher="National Archives and Records Administration", publication_record_date="2010-12-23", locator="PDF page 521, rows 1-46; all rows and page boundaries visually checked", source_quality="A_direct_official", collection_name="Records of the Office of Strategic Services, Record Group 226", rights_notes="All 46 printed rows remain separate. Full protected identifiers remain private."),
        source(ARMY, stable_url="https://catalog.archives.gov/id/1263923", archival_identifier="National Archives Identifier 1263923; parent series NAID 604357", title="Electronic Army Serial Number Merged File, ca. 1938-1946", author_creator="Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration", repository_publisher="National Archives and Records Administration", publication_record_date="1938-1946; merged file created 2002", locator="Official unrestricted ASNEF.FIN.DAT; twenty-seven Batch 1031 candidate links explicitly reviewed", source_quality="A_direct_official", collection_name="World War II Army Enlistment Records", document_number="ASNEF.FIN.DAT", rights_notes="No raw record or full protected identifier is retained in public assets. Shared and conflicting links remain explicit."),
        source(TECH, stable_url="https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf", archival_identifier="NN3-064-03-008; National Archives Identifier 1263923", title="World War II Army Enlistment Records: Reference Copy of Technical Documentation", author_creator="National Archives and Records Administration", repository_publisher="National Archives at College Park - Electronic Records", publication_record_date="1994-2005; reference copy modified 2011", locator="PDF physical pages 44-46; identifier, name, Army-entry-date, grade and civilian-occupation fields", source_quality="A_direct_official", collection_name="World War II Army Enlistment Records technical documentation", rights_notes="Used to interpret selected fields only; source damage, name conversion, coding limits and incomplete coverage remain applicable."),
        source(CODES, stable_url="https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1CL_SD.pdf", archival_identifier="National Archives Identifier 1263923; Code No. 30", title="NARA Compiled Code Lists for the Electronic Army Serial Number Merged File", author_creator="National Archives and Records Administration", repository_publisher="National Archives at College Park - Electronic Records", publication_record_date="2011-01-12; modified 2011-03-17", locator="PDF physical pages 170-181 and 304; Batch 1031 categories visually checked", source_quality="A_direct_official", collection_name="World War II Army Enlistment Records technical documentation", rights_notes="Historical categories identify neither employer, institution nor workplace. Undefined codes 502 and 324 are not interpreted."),
        source(LEGACY_ZINNER, stable_url="https://www.legacy.com/us/obituaries/sfgate/name/paul-zinner-obituary?id=8536999", title="Paul Zinner obituary", repository_publisher="San Francisco Chronicle via Legacy.com", publication_record_date="2012-04-07 to 2012-04-08", locator="Biographical paragraph describing Tufts graduation, Army enlistment and research-analyst posting", source_quality="C_reputable_contemporary_or_scholarly", rights_notes="The obituary calls the office the Office of Strategic Studies; the project preserves that wording as an evident reference to the indexed OSS service rather than silently quoting a correction."),
        source(TUFTS, stable_url="https://dl.tufts.edu/teiviewer/parent/xp68ks62q/chapter/TennisMens.1942", archival_identifier="Tufts Digital Library ID xp68ks62q; component tufts:UA069.005.DO.00151", title="Athletic Rosters of Tufts University for the year 1942", author_creator="Tufts University Department of Physical Education and Athletics", repository_publisher="Tufts Digital Library", publication_record_date="1942", locator="Men's tennis roster; Paul E. Zinner", source_quality="B_authoritative_institutional", collection_name="Tufts University athletics rosters", rights_notes="Contemporary institutional roster corroborates student status; attendance is not employment."),
        source(CIA_ZINDER, stable_url="https://www.cia.gov/readingroom/docs/THE%20STORY%20OF%20THE%20SAUERKRAUTS_0001.pdf", archival_identifier="MO-MEDTO, 2677th Headquarters Detachment OSS (Provisional)", title="The Story of the Sauerkrauts", author_creator="Office of Strategic Services Morale Operations, Mediterranean Theater of Operations", repository_publisher="Central Intelligence Agency Freedom of Information Act Electronic Reading Room", publication_record_date="1944", locator="PDF pages 3-4 and photograph captions; Mr. Zinder in charge of the project", source_quality="A_direct_official", collection_name="CIA Freedom of Information Act Electronic Reading Room", rights_notes="Official wartime document establishes OSS role and surname form but does not alone identify the pre-OSS affiliation."),
        source(HDIPLO_ZINDER, stable_url="https://www.h-diplo.org/reviews/PDF/AR301.pdf", title="H-Diplo Article Review No. 301", author_creator="Günter Bischof", repository_publisher="H-Diplo and H-Net", publication_record_date="2011-04-29", locator="PDF page 4; summary of Florian Traussnig's research on Edmund F. Linder, alias Eddie Zinder", source_quality="C_reputable_contemporary_or_scholarly", rights_notes="Scholarly review explicitly links Linder and the Zinder alias and supplies the French Foreign Legion, British Army and OSS chronology."),
        source(WAPO_ZLOTNICK, stable_url="https://www.washingtonpost.com/archive/local/1987/08/02/austin-smith-real-estate-manager-dies/e451729c-e158-410d-abe2-a8bbce383ff7/", title="Jack Zlotnick, 72, retired political analyst, dies", repository_publisher="The Washington Post", publication_record_date="1987-08-01", locator="Obituary paragraphs for Jack Zlotnick", source_quality="C_reputable_contemporary_or_scholarly", rights_notes="The obituary documents Army and OSS service but does not state the exact transfer sequence."),
        source(CORNELL_ZUBKOFF, stable_url="https://ecommons.cornell.edu/bitstream/1813/37438/1/CUA_v33_1941_42_C.pdf", title="Cornell University Announcements: Directory of the University, 1941-42", author_creator="Cornell University", repository_publisher="Cornell University Library eCommons", publication_record_date="1941-1942", locator="Alphabetical directory entry for Zubkoff, Maurice Joseph, class of 1944", source_quality="B_authoritative_institutional", rights_notes="Contemporary directory corroborates student status; the class year does not by itself prove graduation."),
        source(IRE_ZOSCHKE, stable_url="https://www.worldradiohistory.com/Archive-IRE/40s/IRE-1942-Yearbook.pdf", title="Institute of Radio Engineers 1942 Yearbook", author_creator="Institute of Radio Engineers", repository_publisher="World Radio History digital archive", publication_record_date="1942", locator="Alphabetical membership catalog; Zoschke, Jack H. (A'40)", source_quality="B_authoritative_institutional", rights_notes="The directory establishes professional-association membership and an Indianapolis listing, not an employer or specific occupation."),
        source(POSTGAZETTE_ZOTTER, stable_url="https://obituaries.post-gazette.com/obituary/louis-zotter-1078662895", title="Louis Zotter obituary", repository_publisher="Pittsburgh Post-Gazette", publication_record_date="2010-05-23", locator="Biographical paragraph describing 1942-45 European Theater, 82nd Airborne, Headquarters G-2 and OSS service", source_quality="C_reputable_contemporary_or_scholarly", rights_notes="The source names multiple wartime assignments but does not establish their exact sequence."),
        source(OSSOG, stable_url="https://ossog.info/personnel.html", title="Office of Strategic Services Operational Groups personnel", repository_publisher="OSS Operational Groups historical project", locator="Personnel roster entries for Frank Zabatta, Joseph Zito, James Zonas, John Zonenberg and Louis Zotter", source_quality="D_correlative_or_secondary", rights_notes="Corroborative roster only. It supports wartime names, ranks and group context, not a pre-OSS employer."),
        source(RITCHIE, stable_url="https://www.theritchieboys.com/complete-roster/v-z-surnames", title="The Ritchie Boys complete roster: V-Z surnames", repository_publisher="The Ritchie Boys historical project", locator="V-Z roster; Zuccardy, Charles A.", source_quality="D_correlative_or_secondary", rights_notes="The roster is an identity and training lead only; it supplies no date or direct pre-OSS sequence."),
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {"key": ORG_US_ARMY, "canonical_name": "United States Army", "historical_name": "U.S. Army", "aliases": ["Army"], "organization_type": "military branch", "sector": "military", "country": "United States", "normalization_notes": "Military service is modeled separately from civilian employment."},
        {"key": ORG_BRITISH_ARMY, "canonical_name": "British Army", "historical_name": "British Army", "organization_type": "military branch", "sector": "military", "country": "United Kingdom", "normalization_notes": "The reviewed source does not identify Edmund Linder's unit."},
        {"key": ORG_FOREIGN_LEGION, "canonical_name": "French Foreign Legion", "historical_name": "French Foreign Legion", "organization_type": "military formation", "sector": "military", "country": "France", "normalization_notes": "The reviewed source supplies no regiment or exact service dates."},
        {"key": ORG_TUFTS, "canonical_name": "Tufts College", "historical_name": "Tufts College", "aliases": ["Tufts University"], "organization_type": "university", "sector": "academia_and_research", "city": "Medford", "state_or_region": "Massachusetts", "country": "United States", "active_dates": "1852-present; renamed Tufts University in 1954", "normalization_notes": "The historical source and obituary use Tufts College. Student status is not employment."},
        {"key": ORG_CORNELL, "canonical_name": "Cornell University", "historical_name": "Cornell University", "organization_type": "university", "sector": "academia_and_research", "city": "Ithaca", "state_or_region": "New York", "country": "United States", "normalization_notes": "Student status is not employment; the directory's class year does not prove graduation."},
        {"key": ORG_IRE, "canonical_name": "Institute of Radio Engineers", "historical_name": "Institute of Radio Engineers", "aliases": ["IRE"], "organization_type": "professional association", "sector": "engineering_science_and_technology", "country": "United States", "active_dates": "1912-1962", "normalization_notes": "The Institute merged with the American Institute of Electrical Engineers in 1963 to form IEEE; the historical name is retained."},
    ]


def affiliation(key: str, row: int, relationship: str, temporal: str, identity: str, confidence: str, quality: str, status: str = "published", **kwargs: object) -> dict[str, object]:
    value: dict[str, object] = {"key": key, "person_id": PEOPLE[row][0], "relationship_type": relationship, "pre_oss_temporal_basis": temporal, "identity_confidence": identity, "claim_confidence": confidence, "source_quality": quality, "publication_status": status}
    value.update(kwargs)
    return value


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, _label, _locator) in ARMY_OCCUPATIONS.items():
        identity = "high_confidence" if row in {5, 16, 40} else "confirmed"
        relationship = "student" if row in {26, 44} else "unknown"
        kwargs: dict[str, object] = {
            "occupation": occupation,
            "end_date": date,
            "date_precision": f"Historical civilian-occupation code {code} was recorded at Army entry on {date}; no named employer is supplied.",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "research_notes": "Broad historical category only; excluded from verified-employer analytics and not narrowed beyond the official wording.",
        }
        if row == 44:
            kwargs.update({"organization_key": ORG_CORNELL, "organization_name_as_found": "Cornell University", "occupation": None, "date_precision": "Cornell's 1941-42 directory lists Maurice Joseph Zubkoff in the class of 1944; the Army record independently codes him as a student at entry on 1942-11-05. Graduation is not inferred.", "state_or_region": "New York", "research_notes": "Two independent sources support student status. Cornell is an educational institution here, not an employer."})
        values.append(affiliation(
            f"{slug(PEOPLE[row][1])}-army-occupation-b1031" if row != 44 else "maurice-zubkoff-cornell-student-b1031",
            row,
            relationship,
            "strongly_date_bounded",
            identity,
            "high" if row == 44 else "medium",
            "B_authoritative_institutional" if row == 44 else "A_direct_official",
            "publish_qualified",
            **kwargs,
        ))
    values.extend([
        affiliation("edmund-zinder-foreign-legion-b1031", 6, "military_assignment", "documented_prewar", "high_confidence", "high", "C_reputable_contemporary_or_scholarly", organization_key=ORG_FOREIGN_LEGION, organization_name_as_found="foreign legion in France", role_title="legionnaire", start_date="1938", date_precision="The scholarly review says Edmund F. Linder fled Austria after the 1938 Anschluss and joined the foreign legion in France; exact dates and unit are not supplied.", country="France", immediate_pre_oss=False, last_civilian_pre_service=False, research_notes="Earlier documented military affiliation under the Linder name; not civilian employment."),
        affiliation("edmund-zinder-british-army-b1031", 6, "military_assignment", "explicit_immediate", "high_confidence", "high", "C_reputable_contemporary_or_scholarly", organization_key=ORG_BRITISH_ARMY, organization_name_as_found="British Army", role_title="servicemember", end_date="1943", date_precision="The scholarly review states that the British liberated Linder in 1943 and that, after brief British Army service, the OSS hired him for Morale Operations.", country="United Kingdom", immediate_pre_oss=True, last_civilian_pre_service=False, research_notes="Best-supported immediate military predecessor; exact unit and transfer date remain unknown."),
        affiliation("paul-zinner-tufts-student-b1031", 12, "student", "strongly_date_bounded", "high_confidence", "high", "B_authoritative_institutional", organization_key=ORG_TUFTS, organization_name_as_found="Tufts College", role_title="student", end_date="1943", date_precision="A 1942 institutional roster names Paul E. Zinner, and the obituary says he graduated from Tufts in 1943 before Army enlistment.", city="Medford", state_or_region="Massachusetts", country="United States", immediate_pre_oss=False, last_civilian_pre_service=False, research_notes="Education immediately before wartime service; Tufts is not labeled an employer."),
        affiliation("paul-zinner-us-army-b1031", 12, "military_assignment", "strongly_date_bounded", "high_confidence", "high", "C_reputable_contemporary_or_scholarly", organization_key=ORG_US_ARMY, organization_name_as_found="U.S. Army", role_title="enlisted servicemember", start_date="1943", date_precision="The obituary says Zinner graduated in 1943, enlisted in the Army and was posted as a Central Europe research analyst to the office it calls the Office of Strategic Studies.", country="United States", immediate_pre_oss=True, last_civilian_pre_service=False, research_notes="Best-supported immediate military pathway; the obituary's agency wording is preserved and the exact posting date is absent."),
        affiliation("jack-zlotnick-us-army-b1031", 27, "military_assignment", "probable_immediate", "confirmed", "medium", "C_reputable_contemporary_or_scholarly", "publish_qualified", organization_key=ORG_US_ARMY, organization_name_as_found="Army", role_title="servicemember", start_date="1942", date_precision="The Army bulk record dates entry to 1942-12-16; the obituary says he served in both the Army and OSS during World War II but does not state the transfer date.", country="United States", immediate_pre_oss=True, last_civilian_pre_service=False, research_notes="Probable immediate military pathway, visibly qualified because the obituary does not state a direct transfer."),
        affiliation("jack-zoschke-ire-b1031", 39, "professional_affiliation", "temporal_relation_uncertain", "probable", "medium", "B_authoritative_institutional", "publish_qualified", organization_key=ORG_IRE, organization_name_as_found="Institute of Radio Engineers", role_title="associate member", end_date="1942", date_precision="The 1942 yearbook lists Jack H. Zoschke with associate-member notation and an Indianapolis address; no employer or OSS date is supplied.", city="Indianapolis", state_or_region="Indiana", country="United States", immediate_pre_oss=False, last_civilian_pre_service=False, research_notes="Qualified professional-association lead; the indexed personnel file is needed to confirm identity and sequence."),
        affiliation("louis-zotter-us-army-b1031", 41, "military_assignment", "temporal_relation_uncertain", "high_confidence", "medium", "C_reputable_contemporary_or_scholarly", "publish_qualified", organization_key=ORG_US_ARMY, organization_name_as_found="82nd Airborne, Headquarters G2 (intelligence)", role_title="European Theater servicemember; 82nd Airborne and Headquarters G-2 intelligence", start_date="1942", end_date="1945", date_precision="The obituary describes 1942-45 European Theater service with the 82nd Airborne, Headquarters G-2 and OSS; it does not establish the order of those assignments.", country="United States", immediate_pre_oss=False, last_civilian_pre_service=False, research_notes="Documented military pathway but not labeled immediate because sequence remains unclear."),
    ])
    return values


def claim(key: str, row: int, claim_type: str, text: str, paraphrase: str, identity: str, temporal: str, quality: str, confidence: str, source_links: list[dict[str, str]], notes: str, status: str = "published", affiliation_key: str | None = None) -> dict[str, object]:
    value: dict[str, object] = {"key": key, "person_id": PEOPLE[row][0], "claim_type": claim_type, "claim_text": text, "evidence_paraphrase": paraphrase, "identity_match_assessment": identity, "temporal_assessment": temporal, "source_quality": quality, "claim_confidence": confidence, "publication_status": status, "match_notes": notes, "sources": source_links}
    if affiliation_key:
        value["affiliation_key"] = affiliation_key
    return value


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, label, locator) in ARMY_OCCUPATIONS.items():
        key = f"{slug(PEOPLE[row][1])}-army-occupation-b1031" if row != 44 else "maurice-zubkoff-cornell-student-b1031"
        identity_text = "High confidence from a nonshared protected linkage and reviewed spelling variants; the protected identifier is not published." if row in {5, 16, 40} else "Confirmed by exact name and a nonshared protected linkage; the protected identifier is not published."
        links = [
            {"source_key": INDEX, "support_type": "supports"},
            {"source_key": ARMY, "support_type": "supports"},
            {"source_key": TECH, "support_type": "context_only"},
            {"source_key": CODES, "support_type": "supports", "locator_override": locator},
        ]
        if row == 44:
            links.append({"source_key": CORNELL_ZUBKOFF, "support_type": "supports"})
            text = "Maurice J Zubkoff was a Cornell University student before Army service; Cornell is not treated as an employer."
            paraphrase = "Cornell's 1941-42 directory lists Maurice Joseph Zubkoff in the class of 1944, and the Army record independently records the student category at entry in 1942."
            temporal = "Strongly date-bounded by the 1941-42 directory and 1942 Army entry; graduation is not inferred."
            confidence = "high"
            quality = "B_authoritative_institutional"
            notes = "The uncommon exact full name, contemporary directory and protected Army linkage support the identity."
        else:
            text = f"At Army entry on {date}, {PEOPLE[row][1]} was recorded in the historical category {occupation}; no employer is identified."
            paraphrase = f"The Army bulk file records code {code} at entry, and the official code list defines it as {label}."
            temporal = "Strongly date-bounded to Army entry, but not proven to be the immediately preceding role."
            confidence = "medium"
            quality = "A_direct_official"
            notes = "The historical category is published only as a qualified occupation or student status and excluded from verified-employer analytics."
        values.append(claim(f"occupation-{slug(PEOPLE[row][1])}-b1031", row, "other_pre_oss_affiliation", text, paraphrase, identity_text, temporal, quality, confidence, links, notes, "publish_qualified", key))
    values.extend([
        claim("identity-edmund-zinder-linder-b1031", 6, "identity", "Indexed Edmund F Zinder is strongly supported as Edmund F. Linder, alias Eddie Zinder, who served in OSS Morale Operations.", "The scholarly review names Edmund F. Linder and explicitly gives Eddie Zinder as his alias; the official OSS document places Mr. Zinder in charge of the Sauerkraut project.", "High confidence from the exact Edmund F. name, explicit Zinder alias and independent official OSS surname context.", "Identity and wartime OSS context; this claim does not by itself establish a pre-OSS employer.", "C_reputable_contemporary_or_scholarly", "high", [{"source_key": INDEX}, {"source_key": HDIPLO_ZINDER}, {"source_key": CIA_ZINDER}], "The personnel file remains necessary to resolve all name forms and dates."),
        claim("earlier-edmund-zinder-foreign-legion-b1031", 6, "other_pre_oss_affiliation", "Edmund F. Linder, alias Eddie Zinder, served in the French Foreign Legion before his 1943 British liberation.", "The scholarly review places Linder in the Foreign Legion after his 1938 flight from Austria and before Vichy internment in North Africa.", "High confidence from the explicit alias bridge to indexed Edmund F Zinder.", "Documented earlier military affiliation; not shown as the immediate OSS predecessor.", "C_reputable_contemporary_or_scholarly", "high", [{"source_key": HDIPLO_ZINDER}], "Military service, not civilian employment.", "published", "edmund-zinder-foreign-legion-b1031"),
        claim("immediate-edmund-zinder-british-army-b1031", 6, "immediate_pre_oss_affiliation", "Brief British Army service is Edmund F. Linder's best-supported immediate affiliation before OSS Morale Operations.", "The scholarly review explicitly says that after brief British Army service the OSS hired Linder for Morale Operations in Italy.", "High confidence from the explicit Linder-Zinder alias bridge.", "Explicit immediate sequence, though unit and transfer date are absent.", "C_reputable_contemporary_or_scholarly", "high", [{"source_key": HDIPLO_ZINDER}], "Military assignment, not civilian employment.", "published", "edmund-zinder-british-army-b1031"),
        claim("student-paul-zinner-tufts-b1031", 12, "other_pre_oss_affiliation", "Paul E Zinner was a Tufts College student immediately before wartime Army service; Tufts is not treated as an employer.", "A 1942 Tufts athletics roster names Paul E. Zinner, and his obituary says he graduated in 1943 before enlisting.", "High confidence from the exact uncommon name, contemporary institutional roster and detailed Army-to-OSS biography.", "Strongly date-bounded to 1942-43 before Army enlistment.", "B_authoritative_institutional", "high", [{"source_key": TUFTS}, {"source_key": LEGACY_ZINNER}], "Education is modeled separately from employment.", "published", "paul-zinner-tufts-student-b1031"),
        claim("immediate-paul-zinner-army-b1031", 12, "immediate_pre_oss_affiliation", "U.S. Army service is Paul E Zinner's best-supported immediate pathway into the OSS research staff.", "The obituary states that he graduated in 1943, enlisted in the Army and was posted as a Central Europe research analyst to the wartime intelligence office.", "High confidence from the exact name, education chronology and direct wartime research-role description.", "Strongly date-bounded and sequential, but the exact posting date is absent.", "C_reputable_contemporary_or_scholarly", "high", [{"source_key": LEGACY_ZINNER}, {"source_key": TUFTS, "support_type": "context_only"}], "The obituary's Office of Strategic Studies wording is preserved in the source note.", "published", "paul-zinner-us-army-b1031"),
        claim("immediate-jack-zlotnick-army-b1031", 27, "immediate_pre_oss_affiliation", "Army service is Jack Zlotnick's probable military pathway into the OSS, but a direct transfer has not been documented.", "The official bulk record dates Army entry to December 1942, and the Washington Post obituary says he served in the Army and OSS during World War II.", "Confirmed by exact name, a nonshared protected linkage and a detailed obituary with Army, OSS and later CIA context.", "Probable immediate sequence; the obituary does not state the transfer order or date.", "C_reputable_contemporary_or_scholarly", "medium", [{"source_key": INDEX}, {"source_key": ARMY}, {"source_key": WAPO_ZLOTNICK}], "Military assignment, not civilian employment.", "publish_qualified", "jack-zlotnick-us-army-b1031"),
        claim("professional-jack-zoschke-ire-b1031", 39, "other_pre_oss_affiliation", "A 1942 professional directory lists a Jack H. Zoschke as an Institute of Radio Engineers associate member; the match and OSS sequence remain qualified.", "The Institute's 1942 membership catalog gives the exact uncommon name and an Indianapolis address but no employer.", "Probable identity from the uncommon exact name and compatible era; no second OSS identifier is available.", "Temporal relation to OSS service is uncertain.", "B_authoritative_institutional", "medium", [{"source_key": INDEX}, {"source_key": IRE_ZOSCHKE}], "Professional association only; no engineering occupation or employer is inferred.", "publish_qualified", "jack-zoschke-ire-b1031"),
        claim("military-louis-zotter-army-b1031", 41, "other_pre_oss_affiliation", "Louis Zotter Jr. had documented 1942-45 Army service with the 82nd Airborne and Headquarters G-2, but the sequence relative to OSS remains uncertain.", "The obituary lists the 82nd Airborne, Headquarters G-2 intelligence and OSS within his European Theater service; an OSS Operational Groups roster independently lists L. Zotter.", "High confidence from the uncommon exact surname, junior-index form, compatible wartime biography and corroborative OSS roster.", "Documented wartime military pathway; exact assignment order is not supplied.", "C_reputable_contemporary_or_scholarly", "medium", [{"source_key": POSTGAZETTE_ZOTTER}, {"source_key": OSSOG}], "Not labeled immediate until the personnel file establishes sequence.", "publish_qualified", "louis-zotter-us-army-b1031"),
        claim("conflict-frank-zobatta-zabatta-b1031", 29, "identity", "Frank V Zobatta and Frank V Zabatta remain separate index entities linked by a disputed shared Army identifier; no occupation is transferred.", "The page 521 Zobatta form and earlier Zabatta form are both preserved; the Army record and OSS roster use Zabatta.", "Conflicting because one protected identifier is attached to two separately printed index forms.", "Identity context only; no pre-OSS occupation is accepted.", "A_direct_official", "conflicting", [{"source_key": INDEX}, {"source_key": ARMY}, {"source_key": TECH}, {"source_key": OSSOG, "support_type": "context_only"}], "Personnel-file review is required before any merge or occupation transfer.", "conflicting"),
        claim("conflict-james-zonas-tonas-b1031", 35, "identity", "James Zonas remains a separate indexed T-4 and OSS roster entry, while a shared Army identifier also points to indexed James Tonas; no occupation is transferred.", "The index and OSS Operational Groups roster support the Zonas form, but the protected Army linkage is shared with a separate Tonas entity.", "Conflicting because the public name-and-rank evidence supports Zonas while the private linkage is not unique.", "Wartime identity context only; no pre-OSS occupation is accepted.", "A_direct_official", "conflicting", [{"source_key": INDEX}, {"source_key": OSSOG}, {"source_key": ARMY}, {"source_key": TECH}], "Both source rows remain separately recoverable and require personnel-file review.", "conflicting"),
        claim("conflict-john-zonenberg-army-b1031", 37, "identity", "An OSS Operational Groups roster supports indexed John W Zonenberg, but a linked Army record has middle initial M and a January 1946 entry date.", "The roster gives T/5 J. Zonenberg, while the Army record's middle initial and late date prevent its use as pre-OSS evidence.", "High confidence in the indexed wartime name from the uncommon roster entry; conflicting Army candidate remains unaccepted.", "The 1946 Army record cannot establish a pre-OSS affiliation.", "A_direct_official", "conflicting", [{"source_key": INDEX}, {"source_key": OSSOG}, {"source_key": ARMY, "support_type": "contradicts"}, {"source_key": TECH, "support_type": "context_only"}], "Personnel-file review is required to determine whether the Army record belongs to the indexed person.", "conflicting"),
        claim("identity-charles-zuccardy-ritchie-b1031", 46, "identity", "A Ritchie Boys roster lists Charles A. Zuccardy, providing a qualified wartime training lead for the indexed person.", "The historical project's V-Z roster gives the exact uncommon full name but supplies no date or direct OSS transfer evidence.", "Probable identity from the exact uncommon name; no second public identifier is available.", "Wartime identity lead only; pre-OSS sequence is not established.", "D_correlative_or_secondary", "medium", [{"source_key": INDEX}, {"source_key": RITCHIE}], "No commissioned status, employer or immediate affiliation is inferred.", "publish_qualified"),
    ])
    return values


def unresolved_reason(row: int) -> str:
    reasons = {
        1: "Exact-name and occupation searches did not distinguish the indexed Ernest W Zimmerman from namesakes.",
        2: "Exact-name, OSS, obituary and institutional searches produced no reliable identity-and-affiliation bridge for Norma G Zimmerman.",
        3: "The common name Philip Zimmerman produced no corroborating identifiers sufficient to resolve the indexed person.",
        7: "The index note says see Lind, but accessible sources do not establish whether Edward Zinder is Edmund F. Linder, a second person or a cross-reference row.",
        8: "The note also AS and exact-name searches did not establish Montague H Zink's identity or pre-OSS affiliation.",
        9: "Military and cemetery leads for Francis L Zinkand do not supply an OSS or second-identifier bridge or a pre-OSS employer.",
        10: "A prominent aviator named Frederick Zinn lacks the indexed middle initial and a direct OSS or Box 863 bridge, so the biography was rejected as a namesake lead.",
        11: "Exact-name and Pvt.-rank searches produced no reliable pre-OSS affiliation for Alfons Zinner.",
        14: "Exact-name and spelling-variant searches produced no reliable identity-and-affiliation bridge for Zygmund Ziolo.",
        19: "Searches did not distinguish Bruno P Zipser from Bruno V Zipser or establish a separate pre-OSS affiliation.",
        25: "Exact-name and spelling-variant searches produced no reliable identity-and-affiliation bridge for Louella M Zitzlisperger.",
        30: "Exact-name, transliteration and OCR-variant searches produced no reliable wartime identity or affiliation for David Zobolovsky.",
        31: "Exact-name and Sgt.-rank searches produced no reliable identity-and-affiliation bridge for Marvin G Zoch.",
        32: "Exact-name and likely spelling-variant searches produced no reliable wartime identity or pre-OSS affiliation for Michael G Zoldi.",
        34: "Exact-name, occupation and obituary searches produced no reliable pre-OSS affiliation for Jack N Zonana.",
        38: "A 1934 school-list result for Irene E Zorbas is too early and lacks an OSS bridge, so it is not presented as the indexed person's pre-OSS affiliation.",
        45: "Exact-name and likely spelling-variant searches produced no reliable wartime identity or pre-OSS affiliation for Michael Zubrick.",
    }
    return reasons.get(row, "Accessible official, CIA, OSS, exact-name, employer, occupation, obituary, institutional, newspaper, directory and archival searches produced no reliable identity-and-affiliation bridge; unbridged namesakes and postwar-only leads were rejected.")


def base_update(row: int, **overrides: object) -> dict[str, object]:
    value: dict[str, object] = {"person_id": PEOPLE[row][0], "manual_review_required": True, "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "high"}
    value.update(overrides)
    return value


def person_updates() -> list[dict[str, object]]:
    special = set(ARMY_OCCUPATIONS) | {6, 7, 12, 20, 29, 35, 36, 37, 39, 41, 46}
    values: list[dict[str, object]] = []
    for row in sorted(set(PEOPLE) - special):
        reason = unresolved_reason(row)
        extra: dict[str, object] = {}
        if row in {11, 31}:
            extra.update({"personnel_category": "enlisted_army_personnel", "commissioned_officer": False, "allied_or_foreign_personnel": False})
        values.append(base_update(row, identity_status="unresolved", identity_evidence=f"The visually verified page 521 source preserves {PEOPLE[row][1]}. {reason}", research_status="requires_archival_review", archival_review_priority="critical", next_action=f"Review indexed Box {PEOPLE[row][2]} for corroborating identifiers, immediate pre-OSS affiliation and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}", **extra))
    for row in sorted(ARMY_OCCUPATIONS):
        variants: list[str] = []
        identity_status = "confirmed"
        evidence = "A nonshared protected linkage and exact official name agreement connect the index and Army records; the protected identifier remains private."
        if row == 5:
            variants, identity_status, evidence = ["John M Zimn"], "high_confidence", "A nonshared protected linkage plus agreeing first name and middle initial connect the records; the damaged Army surname Zimn remains a visible variant of indexed Zimmy."
        elif row == 16:
            variants, identity_status, evidence = ["Dominick J Zippilli"], "high_confidence", "A nonshared protected linkage connects the indexed Domonick J Zippelli and Army Dominick J Zippilli forms; both spelling differences remain explicit."
        elif row == 40:
            variants, identity_status, evidence = ["Angelo C Zotos"], "high_confidence", "A nonshared protected linkage and uncommon surname connect indexed Andgelo to the Army form Angelo C Zotos; the forename difference remains explicit."
        next_action = f"Review indexed Box {PEOPLE[row][2]} to identify a named employer or institution and establish Army-to-OSS chronology. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed; the bulk record supplies only a historical occupation category."
        values.append(base_update(row, identity_status=identity_status, identity_evidence=evidence, name_variants=variants, replace_name_variants=False, personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="occupation_only_found", nara_catalog_id="1263923", next_action=next_action))
    values.extend([
        base_update(6, identity_status="high_confidence", identity_evidence="A scholarly review explicitly identifies OSS member Edmund F. Linder as Eddie Zinder, while an official OSS document places Mr. Zinder in charge of the Sauerkraut project.", name_variants=["Edmund F Linder", "Eddie Zinder", "Edmund Friedrich Linder"], replace_name_variants=False, personnel_category="foreign_or_allied_military_personnel", allied_or_foreign_personnel=True, possible_duplicate_group="batch1031-edmund-edward-zinder-linder-cross-reference", research_status="needs_temporal_review", archival_review_priority="critical", next_action="Review Box 863 and relevant British and French military files to confirm all name forms, units and dates and to identify any civilian work before the Foreign Legion. British Army service is the best-supported immediate predecessor, but no civilian employer has yet been identified."),
        base_update(7, identity_status="ambiguous", identity_evidence="The page 521 row says see Lind, but accessible evidence does not establish whether Edward Zinder is Edmund F. Linder, a separate person or only a cross-reference row.", name_variants=["Edward Lind"], replace_name_variants=False, possible_duplicate_group="batch1031-edmund-edward-zinder-linder-cross-reference", research_status="needs_identity_review", archival_review_priority="critical", next_action="Review Box 454 and the Lind cross-reference to determine whether Edward Zinder duplicates Edmund F. Linder or represents a separate person. No affiliation is transferred from Edmund while the identity remains ambiguous."),
        base_update(12, identity_status="high_confidence", identity_evidence="The exact uncommon name is supported by a contemporary Tufts roster and a detailed obituary that gives Tufts, Army and wartime intelligence chronology.", personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="occupation_only_found", archival_review_priority="medium", next_action="Review Box 864 and Army records for the exact OSS posting date and any civilian employment between Tufts and enlistment. Tufts is documented as student status, not employment."),
        base_update(20, identity_status="confirmed", identity_evidence="A nonshared protected linkage and exact official name agreement connect the index and Army records; undefined occupation code 502 remains uninterpreted.", personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="requires_archival_review", nara_catalog_id="1263923", archival_review_priority="critical", next_action="Review Box 864 to identify Anthony Zirilli's pre-OSS affiliation. No occupation or employer is inferred from undefined code 502."),
        base_update(29, identity_status="conflicting", identity_evidence="A protected Army identifier is shared by the separate printed forms Frank V Zabatta and Frank V Zobatta; the Army and OSS Operational Groups sources use Zabatta.", possible_duplicate_group="batch1029-frank-zabatta-zobatta-duplicate", research_status="conflicting_sources", nara_catalog_id="1263923", archival_review_priority="critical", next_action="Review Box 864, the earlier Frank V Zabatta file and the original Army record before merging or transferring any occupation. Both index rows remain separate."),
        base_update(35, identity_status="conflicting", identity_evidence="The index and OSS Operational Groups roster support James Zonas and T-4 rank, but a protected Army identifier is also attached to a separate James Tonas entity.", personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, possible_duplicate_group="batch960-james-tonas-zonas-shared-identifier", research_status="conflicting_sources", nara_catalog_id="1263923", archival_review_priority="critical", next_action="Review Box 865, the James Tonas file and original Army record to resolve the shared linkage. No occupation is transferred while the conflict remains."),
        base_update(36, identity_status="confirmed", identity_evidence="A nonshared protected linkage and exact official name agreement connect the index and Army records; the late-1945 record and undefined occupation code 324 remain identity context only.", personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="requires_archival_review", nara_catalog_id="1263923", archival_review_priority="critical", next_action="Review Box 865 to determine Raymond L Zonca's OSS dates and pre-OSS affiliation. The October 1945 Army record and undefined code 324 are not used as pre-OSS evidence."),
        base_update(37, identity_status="high_confidence", identity_evidence="An OSS Operational Groups roster gives the uncommon indexed surname and first initial with technician-fifth-grade rank; a separate Army candidate has the wrong middle initial and a January 1946 date.", personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="conflicting_sources", archival_review_priority="critical", next_action="Review Box 865 and the original Army record to determine whether its John M Zonenberg is indexed John W Zonenberg. The 1946 category is not treated as pre-OSS evidence."),
        base_update(39, identity_status="probable", identity_evidence="A contemporary professional directory gives the exact uncommon name Jack H. Zoschke and a compatible Indianapolis listing, but no OSS or second-identifier bridge.", personnel_category="unknown_or_indeterminate", research_status="needs_identity_review", archival_review_priority="critical", next_action="Review Box 865 to confirm the Institute of Radio Engineers listing belongs to the indexed person and to identify his employer, occupation and OSS entry date. The association listing is qualified and no employer is inferred."),
        base_update(41, identity_status="high_confidence", identity_evidence="A detailed obituary gives the uncommon name, compatible wartime European service and OSS context; an Operational Groups roster independently lists L. Zotter.", personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="needs_temporal_review", archival_review_priority="critical", next_action="Review Box 865 and Army records to establish the order of Louis Zotter Jr.'s 82nd Airborne, Headquarters G-2 and OSS assignments and to identify any pre-service civilian employer."),
        base_update(46, identity_status="probable", identity_evidence="A Ritchie Boys historical roster gives the exact uncommon name Charles A. Zuccardy but no date, rank or second public identifier.", research_status="needs_identity_review", archival_review_priority="critical", next_action="Review Box 865 and Camp Ritchie training records to confirm the identity and sequence. No commissioned status, immediate affiliation or civilian employer is inferred from the roster alone."),
    ])
    if len(values) != 46:
        raise RuntimeError(f"Expected 46 person updates, generated {len(values)}")
    return values


def research_attempts() -> list[dict[str, object]]:
    updates = {item["person_id"]: item for item in person_updates()}
    substantiated = set(ARMY_OCCUPATIONS) | {6, 7, 12, 20, 27, 29, 35, 36, 37, 39, 41, 46}
    attempts: list[dict[str, object]] = []
    for row, (person_id, name, box) in PEOPLE.items():
        status = str(updates[person_id]["research_status"])
        if row in substantiated:
            outcome = "candidate_rejected" if status in {"conflicting_sources", "needs_identity_review"} else "source_reviewed"
            reviewed = 10 if row in {6, 12, 27, 39, 41, 44, 46} else 7
            rejected = 5 if status in {"conflicting_sources", "needs_identity_review"} else 3
            note = "At least one reviewed identity, occupation, student, professional-association or military-affiliation outcome is preserved with claim-level citations; remaining employer and temporal questions remain explicit."
        else:
            outcome = "candidate_rejected"
            reviewed = 5
            rejected = 4
            note = unresolved_reason(row)
        attempts.append({
            "key": f"page521-row{row}-{slug(name)}-b1031",
            "person_id": person_id,
            "source_adapter": "manual_staged_protocol",
            "query_text": f"{name}; NARA OSS index context; exact-name and meaningful initial, suffix, punctuation, transliteration and OCR variants; OSS, CIA Reading Room, rank, branch, assignment and protected-identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory and archival searches; indexed Box {box}",
            "query_variant_type": "staged_identity_employment_archival_protocol_batch_1031",
            "started_at": "2026-11-04T15:00:00-05:00",
            "completed_at": "2026-11-05T05:30:00-05:00",
            "outcome": outcome,
            "sources_reviewed": reviewed,
            "candidate_sources_rejected": rejected,
            "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives and postwar-only leads were rejected. Shared or conflicting protected links were not converted into occupations. Army categories were not converted into named employers, undefined codes 502 and 324 were not interpreted, and a January 1946 category was not presented as pre-OSS evidence.",
            "research_notes": f"{note} The official index, exact-name OSS searches, grouped CIA Reading Room checks, and employer, occupation, obituary, institutional, newspaper, directory and archival searches were reviewed as applicable. Page 521, its boundaries and cited code-list pages were visually checked. A bounded Library of Congress request timed out and is preserved as a separate source-access error; no authenticated NARA Catalog API request was made.",
            "next_action": str(updates[person_id]["next_action"]),
            "attempt_number": 4 if row == 40 else 3,
            "research_agent_version": "before-oss-b1031-v1",
        })
    if len(attempts) != 46:
        raise RuntimeError(f"Expected 46 research attempts, generated {len(attempts)}")
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-1031-v1",
        "reviewer": "Before OSS Batch 1031 evidence review",
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
