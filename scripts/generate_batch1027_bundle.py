#!/usr/bin/env python3
"""Generate the reviewed Batch 1027 evidence bundle for PDF page 517."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page517-janet-yasunobu-to-merle-youkers-review_"
    "batch-1027_2026-11-04.json"
)

INDEX = "nara-index-b1027"
ARMY = "army-bulk-b1027"
TECH = "army-tech-b1027"
CODES = "army-codes-b1027"
CFA_YERKES = "cfa-yerkes-b1027"
ARMY_MUSEUM_YEMPUKU = "army-museum-yempuku-b1027"
CMH_NISEI = "cmh-nisei-linguists-b1027"
GOVINFO_YINKLEY = "govinfo-yinkley-b1027"
SAGE_YOKOI = "sage-yokoi-b1027"
OSS_TRAVEL_ORDER = "oss-travel-order-b1027"

ORG_UNIVERSITY_HAWAII = "university-hawaii-existing-b1027"
ORG_442_RCT = "442-rct-existing-b1027"
ORG_ARMY_ENGINEERS = "army-engineers-existing-b1027"
ORG_YALE = "yale-existing-b1027"
ORG_WPB = "wpb-existing-b1027"
ORG_SAGE = "sage-methodist-b1027"
ORG_OWI = "owi-existing-b1027"

PEOPLE = {
    1: ("1ca23cf4-8ac2-5579-a548-c5aef6a53f3d", "Janet C Yasunobu"),
    2: ("bf2a44e4-6fe0-5b80-92e9-a3dd0526a9a1", "Clinton T Yates Jr."),
    3: ("b9fabcc7-0d67-5a92-9f51-20e93b89237e", "Margaret P Yates"),
    4: ("e1f860f0-bb7a-5ae4-9fb7-f6769df184b4", "Marion C Yates"),
    5: ("4fc51f5b-5838-5a3b-a332-c2764ea448b7", "Constantine C Yavis"),
    6: ("e3da07b1-1afb-5ae5-8936-760117f79d3a", "Elaine Yavis"),
    7: ("34185655-9f88-51f5-a10e-834acea8a587", "Muriel Ross Yavis"),
    8: ("27018492-334d-5481-825c-998acb3cd7b4", "Jerome M Yawitz"),
    9: ("83cb77d2-97ff-5f01-bd76-fecb2f3cca78", "Edward C Yeadicke"),
    10: ("e689ac17-764e-5918-9c3e-7cf2c3f1e93f", "William L Yearse"),
    11: ("b69d8704-a687-510b-9002-f1dba01d34dc", "Ernest M Yeatman"),
    12: ("05ce91c3-11d1-5fd2-8fc3-b4d8776c8766", "Francis W Yeazell"),
    13: ("8905bb7e-ecf7-5d63-882a-10a2be64ce84", "Francis F Yee"),
    14: ("9e0936d4-d6d6-54e1-8aab-e9e460e96a4f", "Mee H Yee"),
    15: ("ef7bb393-1fb2-5ac1-806e-9401aad429ab", "Sin Y Yee"),
    16: ("fce6b6be-a51b-566e-833c-183a76cb3e6f", "Frederick Yeiser"),
    17: ("b24fb328-e90e-5b99-acfb-994c80a716db", "Jesse P Yellowley Jr."),
    18: ("0518eb8d-5e87-5981-b79f-87a99ab16913", "Ralph T Yempuku"),
    19: ("618548d0-83c2-53d5-87bc-2d48931f3b16", "Fook Li Yen"),
    20: ("4f4cd339-9a47-50e0-b1b4-1509c782882a", "Albert N Yenian"),
    21: ("515353ea-5df4-517e-a6b0-5eaf7ebce805", "David N Yerkes"),
    22: ("704f6a72-a179-50c6-8bec-1a27ef484b3f", "Melvin Yeroshefsky"),
    23: ("010c3147-8513-5295-9057-3d0d328c4fbb", "Erwin J Yessin"),
    24: ("d6481f01-cfb1-54a5-a5aa-e60ea88842e3", "Arden Yinkley Jr."),
    25: ("22403db0-8349-5709-a352-537ce5b5f761", "Clarence W Yoakum"),
    26: ("b5d79a48-9900-57ed-9b53-cb1de2a1042f", "Eff Lincoln Yoder"),
    27: ("e2220125-5fb2-59df-9dea-d25fdef05c97", "Jutaro Yokoi"),
    28: ("82b65efa-5246-5715-b881-f06ef495193a", "Louis Yollin"),
    29: ("0fc1cf43-e0d3-5379-836c-b20beae6bd30", "Battista T Yon"),
    30: ("ad58727f-32af-57c2-b704-6b2a90033f39", "Cecil B York"),
    31: ("387daba3-dfa1-5cd7-84b8-3ea4b6794dd2", "Hoil A York"),
    32: ("3c4d9bcf-0590-52a8-bc81-04086acb33ed", "Dolly K Yoshida"),
    33: ("adbf9746-8552-50f7-8b8d-761ea428c0a5", "Ihizuo Yoshida"),
    34: ("15eb879e-4646-5ad8-9f28-6a8376698bc7", "Shizuo Yoshida"),
    35: ("e1f44440-4a38-5a4f-9c29-03b5c3c61e3f", "Takehiko Yoshihashi"),
    36: ("4dc067df-71c1-5624-86cd-692ab73b318b", "Joseph G Yoshioka"),
    37: ("11331044-a508-5ffa-971a-dcfaec935e46", "Masao K Yoshioka"),
    38: ("c78e05ce-e24c-5afa-a445-1965279471ec", "Ruby Yoshioka"),
    39: ("f50f7fc3-bd26-5601-ad93-be444b0d4eeb", "Usuda Yoshisada"),
    40: ("6b00efc8-7e7e-553a-8060-839288086638", "George Yoshisato"),
    41: ("ee554251-5689-5426-9a40-c23eb0cec64d", "Shigeo Yoshitsugo"),
    42: ("b77020a9-43fc-5003-ac00-d401240682a4", "Haruki H Yoshizume"),
    43: ("86a97de9-a9d1-573d-ad78-0d8becbcf6b8", "Frank J Yost"),
    44: ("dcec00ad-c5d0-5286-9492-87b2345114bc", "Merritt T Yost"),
    45: ("8645b443-9116-5307-a055-291db584ffb1", "Frank J Youhouse"),
    46: ("b77cbce7-be3a-5031-97f5-336049318510", "Merle S Youkers"),
}

ARMY_OCCUPATIONS = {
    8: ("1943-07-05", "066", "technician, except laboratory", "Technicians, except laboratory", "PDF physical page 171"),
    11: ("1943-04-15", "104", "general clerk", "Clerks, general", "PDF physical page 171"),
    14: ("1943-01-22", "227", "waiter or waitress, except private family", "Waiters and waitresses, except private family", "PDF physical page 172"),
    16: ("1942-09-03", "006", "author, editor, or reporter", "Authors, editors, and reporters", "PDF physical page 170"),
    22: ("1943-04-20", "161", "huckster or peddler", "Hucksters and peddlers", "PDF physical page 171"),
    23: ("1943-04-12", "175", "salesperson", "Salespersons", "PDF physical page 171"),
    28: ("1942-08-14", "497", "electrician", "Electricians", "PDF physical page 174"),
    31: ("1942-10-17", "830", "lumberman, raftsman, or woodchopper", "Lumbermen, raftsmen, and woodchoppers", "PDF physical page 177"),
    43: ("1944-02-28", "048", "draftsman", "Draftsmen", "PDF physical page 171"),
    45: ("1943-03-08", "964", "nonprocess manufacturing occupation, not elsewhere classified", "Nonprocess occupations in manufacturing, n.e.c.", "PDF physical pages 176-177"),
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def source(key: str, **kwargs: object) -> dict[str, object]:
    value: dict[str, object] = {"key": key, "access_date": "2026-11-04"}
    value.update(kwargs)
    return value


def sources() -> list[dict[str, object]]:
    return [
        source(INDEX, stable_url="https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf", archival_identifier="RG 226, Entry A1-224, Boxes 857-858", title="OSS Personnel Files from Excel", author_creator="National Archives and Records Administration", repository_publisher="National Archives and Records Administration", publication_record_date="2010-12-23", locator="PDF page 517, rows 1-46; page 518 boundary and all page 517 rows visually checked at 180 dpi", source_quality="A_direct_official", collection_name="Records of the Office of Strategic Services, Record Group 226", rights_notes="All 46 printed rows remain separate. Full protected identifiers remain private."),
        source(ARMY, stable_url="https://catalog.archives.gov/id/1263923", archival_identifier="National Archives Identifier 1263923; parent series NAID 604357", title="Electronic Army Serial Number Merged File, ca. 1938-1946", author_creator="Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration", repository_publisher="National Archives and Records Administration", publication_record_date="1938-1946; merged file created 2002", locator="Official unrestricted ASNEF.FIN.DAT; eleven Batch 1027 protected-identifier candidates reviewed", source_quality="A_direct_official", collection_name="World War II Army Enlistment Records", document_number="ASNEF.FIN.DAT", rights_notes="No raw record or full protected identifier is retained in public assets. Coded occupations identify neither employer nor workplace."),
        source(TECH, stable_url="https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf", archival_identifier="NN3-064-03-008; National Archives Identifier 1263923", title="World War II Army Enlistment Records: Reference Copy of Technical Documentation", author_creator="National Archives and Records Administration", repository_publisher="National Archives at College Park - Electronic Records", publication_record_date="1994-2005; reference copy modified 2011", locator="PDF physical pages 44-46; identifier, name, Army-entry-date, grade and civilian-occupation fields", source_quality="A_direct_official", collection_name="World War II Army Enlistment Records technical documentation", rights_notes="Used to interpret selected fields only; source damage, coding limits and incomplete coverage remain applicable."),
        source(CODES, stable_url="https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1CL_SD.pdf", archival_identifier="National Archives Identifier 1263923; Code No. 30", title="NARA Compiled Code Lists for the Electronic Army Serial Number Merged File", author_creator="National Archives and Records Administration", repository_publisher="National Archives at College Park - Electronic Records", publication_record_date="2011-01-12; modified 2011-03-17", locator="PDF physical pages 170-177; Batch 1027 categories visually checked", source_quality="A_direct_official", collection_name="World War II Army Enlistment Records technical documentation", rights_notes="Historical categories identify neither employer, institution nor workplace."),
        source(CFA_YERKES, stable_url="https://www.cfa.gov/about-cfa/who-we-are/david-n-yerkes", title="David N. Yerkes", author_creator="United States Commission of Fine Arts", repository_publisher="United States Commission of Fine Arts", locator="Biographical paragraph identifying Harvard and Yale education followed by Army Corps of Engineers and OSS service", source_quality="B_authoritative_institutional", rights_notes="The federal biography supplies sequence but not an exact Corps-to-OSS transfer date."),
        source(ARMY_MUSEUM_YEMPUKU, stable_url="https://www.thenmusa.org/biographies/ralph-t-yempuku/", title="Ralph T. Yempuku", author_creator="Ellora Larsen", repository_publisher="National Museum of the United States Army", locator="Biography paragraphs on University of Hawaii employment, Hawaii Territorial Guard, Varsity Victory Volunteers, 442d RCT and OSS recruitment", source_quality="B_authoritative_institutional", rights_notes="The institutional biography supplies a dated civilian-to-military pathway and direct OSS recruitment narrative."),
        source(CMH_NISEI, stable_url="https://history.army.mil/portals/143/Images/Publications/catalog/70-99-1.pdf", archival_identifier="CMH Publication 70-99-1", title="Nisei Linguists: Japanese Americans in the Military Intelligence Service During World War II", author_creator="James C. McNaughton", repository_publisher="United States Army Center of Military History", publication_record_date="2006", locator="Printed page 141 for Ralph T. Yempuku; printed pages 208-209 for Takehiko Yoshihashi and the Denver OWI translation team", source_quality="A_direct_official", rights_notes="Official Army history. The Yoshihashi passage documents OWI work but not its exact relation to OSS."),
        source(GOVINFO_YINKLEY, stable_url="https://www.govinfo.gov/content/pkg/GOVPUB-PR32_5000-996837591d86fda4aee4e6d4fa603109/pdf/GOVPUB-PR32_5000-996837591d86fda4aee4e6d4fa603109.pdf", title="Victory: Official Weekly Bulletin of the Office of War Information", author_creator="United States Office of War Information", repository_publisher="United States Government Publishing Office", publication_record_date="1943-01-20", locator="Printed pages 86-87, Appointments and Resignations", source_quality="A_direct_official", rights_notes="Contemporary federal bulletin; it does not state when Yinkley joined OSS."),
        source(SAGE_YOKOI, stable_url="https://sgpumc.org/about-us/", title="About Us: History and Restoration", repository_publisher="Sage Granada Park United Methodist Church", locator="Institutional history of Rev. Jutaro Yokoi's El Monte ministry from 1930, Baptist pastorate through 1934, Methodist recognition and Sage Methodist Church", source_quality="B_authoritative_institutional", rights_notes="The church history establishes a prewar ministry but does not directly name OSS."),
        source(OSS_TRAVEL_ORDER, stable_url="https://www.historyofjapaneseinny.org/wp-content/uploads/2024/05/OFFICE-OF-STRATEGIC-SERVICES-1.pdf", archival_identifier="OSS Headquarters and Headquarters Detachment, 370.5 (27 Apr 45), corrected copy", title="Invitational Travel Orders, Shipment IJ-B857-HY", author_creator="Office of Strategic Services", repository_publisher="Reproduced by the History of Japanese in New York", publication_record_date="1945-04-30", locator="PDF physical page 11; corrected travel order visually checked", source_quality="A_direct_official", collection_name="Reproduced Office of Strategic Services records", rights_notes="The reproduced official order identifies OSS civilian employees. It supplies no pre-OSS employer."),
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {"key": ORG_UNIVERSITY_HAWAII, "organization_id": "54616c70-7882-5b9f-8aa5-877d670cb0d3", "canonical_name": "University of Hawaii", "historical_name": "University of Hawaii", "organization_type": "university", "sector": "academia_and_research", "city": "Honolulu", "state_or_region": "Hawaii", "country": "United States", "normalization_notes": "Historical institutional name from the Army Museum biography."},
        {"key": ORG_442_RCT, "organization_id": "1807a46f-a3a3-56fc-bfac-cbcefafd3a32", "canonical_name": "442nd Regimental Combat Team", "historical_name": "442d Regimental Combat Team", "aliases": ["442d RCT", "442nd RCT"], "organization_type": "United States Army regimental combat team", "sector": "military", "country": "United States", "normalization_notes": "The historical 442d spelling is preserved in the affiliation."},
        {"key": ORG_ARMY_ENGINEERS, "organization_id": "f2367526-082d-5cad-8156-c405c426f2e1", "canonical_name": "United States Army Corps of Engineers", "historical_name": "Army Corps of Engineers", "aliases": ["U.S. Army Corps of Engineers"], "organization_type": "military engineering branch", "sector": "military", "country": "United States", "normalization_notes": "Military assignment remains separate from civilian employment."},
        {"key": ORG_YALE, "organization_id": "918dedde-f9d1-5db1-8304-5c218a06b9b5", "canonical_name": "Yale University", "historical_name": "Yale University", "organization_type": "university", "sector": "academia_and_research", "city": "New Haven", "state_or_region": "Connecticut", "country": "United States", "normalization_notes": "Student status is not counted as employment."},
        {"key": ORG_WPB, "organization_id": "92be7d87-ebc8-5b56-b469-380867bdafe1", "canonical_name": "War Production Board", "historical_name": "War Production Board", "aliases": ["WPB"], "organization_type": "federal wartime production agency", "sector": "federal_government", "country": "United States", "active_dates": "1942-1945", "normalization_notes": "Government assignment remains separate from private employment."},
        {"key": ORG_SAGE, "canonical_name": "Sage Methodist Church", "historical_name": "Sage Methodist Church", "aliases": ["Sage Memorial Methodist Church"], "organization_type": "Methodist church", "sector": "labor_nonprofit_and_religion", "city": "El Monte", "state_or_region": "California", "country": "United States", "active_dates": "1930s-present through successor congregation", "normalization_notes": "The prewar church is not silently replaced by its modern successor, Sage Granada Park United Methodist Church."},
        {"key": ORG_OWI, "organization_id": "d907505c-05ff-502a-810c-e6189e186543", "canonical_name": "United States Office of War Information", "historical_name": "Office of War Information", "aliases": ["OWI"], "organization_type": "federal wartime information agency", "sector": "federal_government", "country": "United States", "active_dates": "1942-1945", "normalization_notes": "Government assignment remains separate from private employment."},
    ]


def affiliation(key: str, row: int, relationship: str, temporal: str, identity: str, confidence: str, quality: str, status: str = "published", **kwargs: object) -> dict[str, object]:
    value: dict[str, object] = {
        "key": key,
        "person_id": PEOPLE[row][0],
        "relationship_type": relationship,
        "pre_oss_temporal_basis": temporal,
        "identity_confidence": identity,
        "claim_confidence": confidence,
        "source_quality": quality,
        "publication_status": status,
    }
    value.update(kwargs)
    return value


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, _label, _locator) in ARMY_OCCUPATIONS.items():
        identity = "high_confidence" if row == 28 else "confirmed"
        values.append(affiliation(
            f"{slug(PEOPLE[row][1])}-army-occupation-b1027", row, "unknown",
            "strongly_date_bounded", identity, "medium", "A_direct_official", "publish_qualified",
            occupation=occupation, end_date=date,
            date_precision=f"Historical civilian-occupation code {code} was recorded at Army entry on {date}; no named employer or institution is supplied.",
            country="United States", immediate_pre_oss=False, last_civilian_pre_service=False,
            research_notes="Broad historical category only; excluded from verified-employer analytics and not narrowed beyond the official wording.",
        ))
    values.extend([
        affiliation("ralph-yempuku-university-hawaii-b1027", 18, "employment", "strongly_date_bounded", "high_confidence", "high", "B_authoritative_institutional", organization_key=ORG_UNIVERSITY_HAWAII, organization_name_as_found="the university", role_title="assistant instructor of physical education", start_date="1936", end_date="1941-12", date_precision="The Army Museum says he continued working at the university after 1936 graduation and joined the Hawaii Territorial Guard the day after Pearl Harbor.", city="Honolulu", state_or_region="Hawaii", country="United States", immediate_pre_oss=False, last_civilian_pre_service=True, research_notes="Last documented civilian employer before a series of military assignments; not immediate pre-OSS."),
        affiliation("ralph-yempuku-442-rct-b1027", 18, "military_assignment", "explicit_immediate", "high_confidence", "high", "A_direct_official", organization_key=ORG_442_RCT, organization_name_as_found="442d Regimental Combat Team", role_title="first lieutenant; basic-training participant", start_date="1944", end_date="1944-01", date_precision="Official Army history says OSS recruited at Camp Shelby and selected First Lieutenant Yempuku in January 1944; the Army Museum says recruitment followed his 442d basic training.", state_or_region="Mississippi", country="United States", immediate_pre_oss=True, last_civilian_pre_service=False, research_notes="Best-supported immediate military predecessor; kept separate from civilian university employment."),
        affiliation("david-yerkes-yale-b1027", 21, "student", "documented_prewar", "high_confidence", "high", "B_authoritative_institutional", organization_key=ORG_YALE, organization_name_as_found="Yale University", role_title="architecture master's student", date_precision="The federal biography places the Yale architecture degree before wartime Army Corps of Engineers and OSS service; exact graduation date is not supplied.", city="New Haven", state_or_region="Connecticut", country="United States", immediate_pre_oss=False, last_civilian_pre_service=False, research_notes="Student status is not employment."),
        affiliation("david-yerkes-army-engineers-b1027", 21, "military_assignment", "probable_immediate", "high_confidence", "medium", "B_authoritative_institutional", "publish_qualified", organization_key=ORG_ARMY_ENGINEERS, organization_name_as_found="U.S. Army Corps of Engineers", role_title="servicemember", date_precision="The federal biography orders the Army Corps of Engineers before OSS within World War II but supplies no transfer date or exact service dates.", country="United States", immediate_pre_oss=True, last_civilian_pre_service=False, research_notes="Probable immediate military predecessor; profile remains visibly qualified pending Box 858 review."),
        affiliation("arden-yinkley-wpb-b1027", 24, "government_assignment", "temporal_relation_uncertain", "probable", "medium", "A_direct_official", "publish_qualified", organization_key=ORG_WPB, organization_name_as_found="WPB Special Projects Salvage Branch", role_title="chief, Special Projects Salvage Branch", start_date="1943-01", date_precision="A January 20, 1943 federal bulletin says Yinkley, formerly the deputy, succeeded the branch chief; no tenure end date or OSS date is supplied.", country="United States", immediate_pre_oss=False, last_civilian_pre_service=False, research_notes="Documented wartime government post whose relation to OSS remains unresolved."),
        affiliation("jutaro-yokoi-sage-methodist-b1027", 27, "professional_affiliation", "documented_prewar", "probable", "medium", "B_authoritative_institutional", "publish_qualified", organization_key=ORG_SAGE, organization_name_as_found="Sage Methodist Church", role_title="pastor and founder", start_date="1934", end_date="1942", date_precision="The congregation says the Methodist conference recognized him in 1934 and that he continued the El Monte ministry until wartime incarceration; exact OSS chronology is unknown.", city="El Monte", state_or_region="California", country="United States", immediate_pre_oss=False, last_civilian_pre_service=False, research_notes="Professional religious affiliation, not labeled employment because compensation is not documented."),
        affiliation("takehiko-yoshihashi-owi-b1027", 35, "government_assignment", "temporal_relation_uncertain", "probable", "medium", "A_direct_official", "publish_qualified", organization_key=ORG_OWI, organization_name_as_found="Office of War Information", role_title="leader, Denver Japanese-language translation team", start_date="1944", end_date="1945", date_precision="Official Army history says Japanese broadcasts were translated in Denver by a twenty-one-person Nisei team under Yoshihashi; no OSS transition date is supplied.", city="Denver", state_or_region="Colorado", country="United States", immediate_pre_oss=False, last_civilian_pre_service=False, research_notes="Documented wartime government affiliation; sequence relative to OSS remains unresolved."),
    ])
    return values


def claim(key: str, row: int, claim_type: str, text: str, paraphrase: str, identity: str, temporal: str, quality: str, confidence: str, source_links: list[dict[str, str]], notes: str, status: str = "published", affiliation_key: str | None = None) -> dict[str, object]:
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
        "publication_status": status,
        "match_notes": notes,
        "sources": source_links,
    }
    if affiliation_key:
        value["affiliation_key"] = affiliation_key
    return value


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, label, locator) in ARMY_OCCUPATIONS.items():
        identity = "A nonshared protected identifier and exact official name agreement connect the index and Army records."
        if row == 28:
            identity = "A nonshared protected identifier connects the records, while the Army record shortens the given name to Lou; the name conflict remains explicit."
        values.append(claim(
            f"occupation-{slug(PEOPLE[row][1])}-b1027", row, "occupation",
            f"At Army entry, {PEOPLE[row][1]} was recorded in the broad historical category {label}.",
            f"The official Army record gives code {code} at entry on {date}; NARA's code list maps it to {occupation}.",
            identity, "Strongly date-bounded to Army entry; neither employer nor immediate OSS sequence is supplied.",
            "A_direct_official", "medium", [{"source_key": ARMY}, {"source_key": TECH}, {"source_key": CODES, "locator_override": locator}],
            "Historical category only. It is not converted into a named employer, workplace, or narrower modern occupation.", "publish_qualified",
            f"{slug(PEOPLE[row][1])}-army-occupation-b1027",
        ))
    values.extend([
        claim("identity-ralph-yempuku-b1027", 18, "identity", "Indexed Ralph T Yempuku is the University of Hawaii instructor and first lieutenant recruited from the 442d Regimental Combat Team into OSS Detachment 101.", "Official Army sources provide the exact distinctive name, university role, first-lieutenant rank, 442d assignment and direct OSS recruitment narrative.", "High confidence from rare exact name, middle initial, officer context and direct official OSS chronology.", "The sources explicitly place University employment before military service and OSS recruitment after 442d basic training.", "A_direct_official", "high", [{"source_key": INDEX}, {"source_key": ARMY_MUSEUM_YEMPUKU}, {"source_key": CMH_NISEI}], "The direct official chronology is specific enough for publication; the personnel file remains desirable for appointment dates."),
        claim("immediate-ralph-yempuku-b1027", 18, "immediate_pre_oss_affiliation", "Ralph T. Yempuku's immediate pre-OSS assignment was the 442d Regimental Combat Team at Camp Shelby.", "Army history says OSS recruited at Camp Shelby and selected First Lieutenant Yempuku in January 1944; the Army Museum places recruitment after his basic training.", "High-confidence exact identity from direct official OSS sources.", "Explicit immediate military transition with month-level precision.", "A_direct_official", "high", [{"source_key": CMH_NISEI}, {"source_key": ARMY_MUSEUM_YEMPUKU}], "Military assignment remains separate from civilian employment.", "published", "ralph-yempuku-442-rct-b1027"),
        claim("civilian-ralph-yempuku-b1027", 18, "last_civilian_pre_service", "The University of Hawaii was Ralph T. Yempuku's last documented civilian employer before wartime military service.", "The Army Museum says he continued working there as an assistant physical-education instructor after graduation and joined the Territorial Guard after Pearl Harbor.", "High-confidence exact identity from direct official OSS sources.", "Strongly date-bounded before the intervening Guard, auxiliary, 442d and OSS assignments.", "B_authoritative_institutional", "high", [{"source_key": ARMY_MUSEUM_YEMPUKU}, {"source_key": CMH_NISEI, "support_type": "context_only"}], "University employment is not conflated with his earlier student status.", "published", "ralph-yempuku-university-hawaii-b1027"),
        claim("identity-david-yerkes-b1027", 21, "identity", "Indexed David N Yerkes is the architect David Norton Yerkes who served in the Army Corps of Engineers and OSS during World War II.", "The federal biography supplies the expanded middle name, Harvard and Yale education, Army Corps of Engineers service and direct OSS service.", "High confidence from the exact name, middle initial and distinctive federal biography.", "The biography orders education before wartime military and OSS service but omits exact dates.", "B_authoritative_institutional", "high", [{"source_key": INDEX}, {"source_key": CFA_YERKES}], "The personnel file remains necessary to confirm rank and exact transfer timing."),
        claim("army-engineers-david-yerkes-b1027", 21, "immediate_pre_oss_affiliation", "David N. Yerkes probably served in the U.S. Army Corps of Engineers immediately before OSS.", "The federal biography lists Army Corps of Engineers service before OSS within a single World War II sequence.", "High-confidence exact identity from distinctive name and biography.", "Probable immediate sequence; no exact transfer date or intervening assignment is stated.", "B_authoritative_institutional", "medium", [{"source_key": CFA_YERKES}], "Visible qualification is required pending Box 858 review.", "publish_qualified", "david-yerkes-army-engineers-b1027"),
        claim("yale-david-yerkes-b1027", 21, "other_pre_oss_affiliation", "David N. Yerkes studied architecture at Yale University before wartime service.", "The federal biography says he earned a master's degree in architecture at Yale before Army Corps of Engineers and OSS service.", "High-confidence exact identity from distinctive name and biography.", "Documented before wartime service; not an employer and not immediate pre-OSS.", "B_authoritative_institutional", "high", [{"source_key": CFA_YERKES}], "Yale is modeled as student status, not employment.", "published", "david-yerkes-yale-b1027"),
        claim("identity-arden-yinkley-b1027", 24, "identity", "The indexed Arden Yinkley Jr. probably is the War Production Board official appointed to lead its Special Projects Salvage Branch in January 1943.", "The uncommon exact name and suffix align with a contemporary federal appointment notice, but the notice does not name OSS.", "Probable exact-name identity without a protected identifier or direct OSS bridge.", "The WPB appointment is dated January 1943; its relation to OSS remains unknown.", "A_direct_official", "medium", [{"source_key": INDEX}, {"source_key": GOVINFO_YINKLEY}], "Published with qualification pending the personnel file.", "publish_qualified"),
        claim("wpb-arden-yinkley-b1027", 24, "other_pre_oss_affiliation", "Arden Yinkley Jr. held a War Production Board salvage-branch leadership post in January 1943.", "The official bulletin says Yinkley, formerly the deputy, succeeded the chief of the Special Projects Salvage Branch.", "Probable identity from uncommon exact name and suffix.", "Dated wartime government role; not proven to precede OSS.", "A_direct_official", "medium", [{"source_key": GOVINFO_YINKLEY}], "Not labeled immediate or last civilian employer.", "publish_qualified", "arden-yinkley-wpb-b1027"),
        claim("identity-jutaro-yokoi-b1027", 27, "identity", "The indexed Jutaro Yokoi probably is the El Monte pastor who founded Sage Methodist Church and continued ministering during wartime incarceration.", "The rare exact name and coherent California wartime chronology align, but the church history does not name OSS.", "Probable rare-name identity without a protected identifier or direct OSS bridge.", "The ministry is documented from 1930; exact OSS entry remains unknown.", "B_authoritative_institutional", "medium", [{"source_key": INDEX}, {"source_key": SAGE_YOKOI}], "Published with qualification pending Box 858 review.", "publish_qualified"),
        claim("sage-jutaro-yokoi-b1027", 27, "other_pre_oss_affiliation", "Jutaro Yokoi served as a pastor and founded Sage Methodist Church in El Monte before World War II.", "The congregation says he began local ministry in 1930, became a recognized Methodist pastor in 1934 and founded the church in the 1930s.", "Probable identity from the rare exact name and coherent chronology.", "Documented prewar professional affiliation; exact compensation and OSS sequence are unknown.", "B_authoritative_institutional", "medium", [{"source_key": SAGE_YOKOI}], "Professional religious affiliation, not presented as a named employer.", "publish_qualified", "jutaro-yokoi-sage-methodist-b1027"),
        claim("identity-takehiko-yoshihashi-b1027", 35, "identity", "The indexed Takehiko Yoshihashi probably is the Office of War Information team leader documented in official Army history.", "The rare exact name, Denver wartime chronology and federal Japanese-language work align, but the history does not directly name his OSS service.", "Probable rare-name identity without a protected identifier or direct OSS bridge.", "The OWI work is dated to 1944-45; its sequence relative to OSS remains unknown.", "A_direct_official", "medium", [{"source_key": INDEX}, {"source_key": CMH_NISEI}], "Published with qualification pending Box 858 review.", "publish_qualified"),
        claim("owi-takehiko-yoshihashi-b1027", 35, "other_pre_oss_affiliation", "Takehiko Yoshihashi led the Denver team translating Office of War Information Japanese-language broadcasts during World War II.", "Official Army history identifies the twenty-one-person Denver translation team as working under Yoshihashi.", "Probable identity from the rare exact name and specific wartime chronology.", "Documented wartime government assignment; not proven to precede OSS.", "A_direct_official", "medium", [{"source_key": CMH_NISEI}], "Not labeled immediate or last civilian employer.", "publish_qualified", "takehiko-yoshihashi-owi-b1027"),
        claim("identity-shizuo-yoshida-b1027", 34, "identity", "Indexed Shizuo Yoshida is strongly supported as the OSS civilian employee named in an April 1945 overseas travel order.", "A corrected OSS order names Shizuo Yoshida among civilian employees traveling overseas for temporary OSS duty.", "High confidence from exact name, direct OSS status and the corresponding index entry; the name lacks an additional identifier.", "The order documents OSS status on April 30, 1945 but supplies no pre-OSS affiliation.", "A_direct_official", "high", [{"source_key": INDEX}, {"source_key": OSS_TRAVEL_ORDER}], "Identity and OSS status only; no employer is inferred."),
        claim("identity-yoshisada-usuda-b1027", 39, "identity", "The index's Usuda Yoshisada entry is strongly supported as Yoshisada Katoi Usuda, an OSS civilian employee named in an April 1945 travel order.", "The official order supplies surname-last full-name order and identifies Yoshisada Katoi Usuda as an OSS civilian employee.", "High confidence from the distinctive name components and direct OSS status; the index appears to transpose surname and given name.", "The order documents OSS status on April 30, 1945 but supplies no pre-OSS affiliation.", "A_direct_official", "high", [{"source_key": INDEX}, {"source_key": OSS_TRAVEL_ORDER}], "Original indexed order remains preserved; documented variants are added without silent correction."),
    ])
    return values


def unresolved_reason(row: int) -> str:
    reasons = {
        2: "The suffix and middle initial did not produce a unique identity-and-employment bridge; common-name candidates remained uncorroborated.",
        3: "Multiple Margaret P Yates namesakes lacked an OSS, Box 857 or contemporaneous employment bridge.",
        4: "Multiple Marion C Yates namesakes lacked an OSS, Box 857 or contemporaneous employment bridge.",
        7: "The compound indexed name did not yield a reliable OSS or employment bridge beyond the index.",
        10: "A veteran burial record corroborates Army service for a same-name man but supplies no protected-identifier, OSS or employment bridge.",
        12: "Sparse exact-name results and variant spellings did not establish Francis W Yeazell's identity or pre-OSS affiliation.",
        13: "Common-name and commercial people-search results did not establish the indexed Francis F Yee.",
        15: "Common-name and commercial people-search results did not establish the indexed Sin Y Yee.",
        17: "A veteran burial listing supports a same-name Army captain but supplies no OSS, Box 858 or employment bridge.",
        19: "The index explicitly prints Civilian, but exact-name and transliteration searches did not establish a pre-OSS institution or employer.",
        20: "A postwar business lead for an Albert Yenian and a same-name Navy veteran lack a protected-identifier or OSS bridge.",
        25: "Common-name results did not establish Clarence W Yoakum's identity or pre-OSS affiliation.",
        26: "The unusual name produced no reliable identity, OSS or employment bridge in accessible sources.",
        29: "The indexed name produced people-finder and namesake noise but no reliable wartime identity or employment evidence.",
        30: "A historical directory contains a Cecil B York banking lead, but it lacks an OSS or Box 858 identity bridge and was not accepted.",
        32: "A much later federal court caption names Dolly K Yoshida but supplies no wartime identity or pre-OSS evidence.",
        33: "The indexed spelling produced no reliable OSS or employment bridge in accessible sources.",
        36: "The exact-name search produced scholarly namesakes without an OSS or Box 858 bridge.",
        37: "The exact-name search produced no reliable wartime identity or pre-OSS employment bridge.",
        38: "Smithsonian evidence identifies a postwar science writer named Ruby Yoshioka, but it does not establish the indexed person's wartime identity or pre-OSS career.",
        40: "A postwar Hawaii obituary names a George Yoshisato but does not provide an OSS or pre-OSS identity bridge.",
        46: "The protected identifier points to an Army record for Roger E McCarren, a wholly different name; no identity or occupation is transferred.",
    }
    return reasons.get(row, "Accessible exact-name, official, CIA, OSS, employer, occupation, obituary, institutional, newspaper, directory and archival searches produced no reliable identity-and-affiliation bridge; unbridged namesakes and postwar-only leads were rejected.")


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
    special = set(ARMY_OCCUPATIONS) | {18, 21, 24, 27, 34, 35, 39, 46}
    values: list[dict[str, object]] = []
    for row in sorted(set(PEOPLE) - special):
        reason = unresolved_reason(row)
        extra: dict[str, object] = {}
        if row == 19:
            extra = {"personnel_category": "civilian_professional_or_administrative_grade", "commissioned_officer": False, "allied_or_foreign_personnel": False}
        values.append(base_update(
            row,
            identity_status="unresolved",
            identity_evidence=f"The visually verified page 517 source preserves {PEOPLE[row][1]}. {reason}",
            research_status="requires_archival_review",
            archival_review_priority="critical" if row in {3, 4, 7, 13, 15, 19, 25, 33, 36, 37, 38, 41, 42, 44} else "high",
            next_action=f"Review indexed Box {'858' if row >= 16 else '857'} for corroborating identifiers, immediate pre-OSS affiliation and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}",
            **extra,
        ))
    for row in sorted(ARMY_OCCUPATIONS):
        values.append(base_update(
            row,
            identity_status="high_confidence" if row == 28 else "confirmed",
            identity_evidence=(
                "A nonshared protected identifier links the index to the Army record, but the Army record shortens Louis to Lou; the conflict remains explicit."
                if row == 28 else
                "A nonshared protected identifier and exact official name agreement connect the index and Army records; the identifier remains private."
            ),
            name_variants=["Lou Yollin"] if row == 28 else [],
            replace_name_variants=False,
            personnel_category="enlisted_army_personnel",
            commissioned_officer=False,
            allied_or_foreign_personnel=False,
            research_status="occupation_only_found",
            nara_catalog_id="1263923",
            next_action=f"Review indexed Box {'858' if row >= 16 else '857'} to identify a named employer or institution and establish Army-to-OSS chronology; the bulk record supplies only a historical occupation category.",
        ))
    values.extend([
        base_update(18, identity_status="high_confidence", identity_evidence="Official Army sources provide the rare exact name, middle initial, first-lieutenant rank, University of Hawaii role, 442d assignment and direct OSS recruitment chronology.", personnel_category="commissioned_army_officer", commissioned_officer=True, allied_or_foreign_personnel=False, research_status="verified_employer_found", nara_catalog_id="1263923", archival_review_priority="medium", next_action="Review Box 858 to confirm the exact University of Hawaii end date, 442d assignment dates and January 1944 OSS appointment paperwork; the civilian employer and military predecessor are already strongly supported."),
        base_update(21, identity_status="high_confidence", identity_evidence="The federal Commission of Fine Arts biography expands the exact indexed name to David Norton Yerkes and directly links the architect to Army Corps of Engineers and OSS service.", research_status="needs_temporal_review", archival_review_priority="critical", next_action="Review Box 858 to confirm David N. Yerkes's rank, Corps of Engineers unit and exact transfer into OSS; Yale remains student status rather than employment."),
        base_update(24, identity_status="probable", identity_evidence="The uncommon exact name and suffix align with a January 1943 federal War Production Board appointment notice, but that notice does not name OSS or a protected identifier.", personnel_category="civilian_professional_or_administrative_grade", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="needs_temporal_review", archival_review_priority="critical", next_action="Review Box 858 to confirm Arden Yinkley Jr.'s identity and determine whether the War Production Board post preceded or overlapped OSS service."),
        base_update(27, identity_status="probable", identity_evidence="The rare exact name and institutional church history establish a coherent El Monte ministry and wartime-incarceration chronology, but no source directly names OSS.", personnel_category="civilian_professional_or_administrative_grade", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="needs_identity_review", archival_review_priority="critical", next_action="Review Box 858 to confirm Jutaro Yokoi's OSS identity, ministerial chronology and whether any government or military assignment intervened."),
        base_update(34, identity_status="high_confidence", identity_evidence="A visually verified corrected OSS order names Shizuo Yoshida as a civilian OSS employee in April 1945; the common name and missing extra identifier keep the match below confirmed.", personnel_category="civilian_professional_or_administrative_grade", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="requires_archival_review", archival_review_priority="critical", next_action="Review Box 858 for Shizuo Yoshida's identity, pre-OSS employer and recruitment chronology; the April 1945 OSS civilian status is already directly documented."),
        base_update(35, identity_status="probable", identity_evidence="Official Army history names Takehiko Yoshihashi as leader of a Denver OWI Japanese-translation team, but it does not directly link that rare-name biography to OSS.", personnel_category="civilian_professional_or_administrative_grade", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="needs_temporal_review", archival_review_priority="critical", next_action="Review Box 858 to confirm Takehiko Yoshihashi's OSS identity and determine whether OWI employment preceded or overlapped OSS service."),
        base_update(39, identity_status="high_confidence", identity_evidence="A visually verified corrected OSS order names Yoshisada Katoi Usuda as a civilian OSS employee; the distinctive components indicate that the index reverses surname and given name.", name_variants=["Yoshisada Katoi Usuda", "Usuda Yoshisada", "Yoshisada Usuda"], replace_name_variants=False, personnel_category="civilian_professional_or_administrative_grade", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="requires_archival_review", archival_review_priority="critical", next_action="Review Box 858 to confirm name order and spelling, pre-OSS employer and recruitment chronology; preserve the original indexed order alongside documented variants."),
        base_update(46, identity_status="conflicting", identity_evidence="The visually verified page 517 source preserves Merle S Youkers, but the same protected identifier points to an Army record for Roger E McCarren. The material name conflict prevents any transfer.", research_status="conflicting_sources", possible_duplicate_group="batch1027-merle-youkers-identifier-conflict", archival_review_priority="critical", next_action="Review Box 858 and the original identifier-bearing index source to resolve the Merle S Youkers/Roger E McCarren conflict. No Army occupation, grade or entry date is transferred."),
    ])
    if len(values) != 46:
        raise RuntimeError(f"Expected 46 person updates, generated {len(values)}")
    return values


def research_attempts() -> list[dict[str, object]]:
    substantiated = set(ARMY_OCCUPATIONS) | {18, 21, 24, 27, 34, 35, 39, 46}
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        box = "858" if row >= 16 else "857"
        if row in substantiated:
            outcome = "candidate_rejected" if row == 46 else "source_reviewed"
            reviewed = 10 if row in {18, 21, 24, 27, 34, 35, 39} else 7
            rejected = 5 if row == 46 else 3
            note = unresolved_reason(row) if row == 46 else "At least one identity, occupation, employer, student-status or institutional-pathway outcome is preserved with claim-level citations; remaining employer or temporal questions remain explicit."
        else:
            outcome = "candidate_rejected"
            reviewed = 5
            rejected = 4
            note = unresolved_reason(row)
        attempts.append({
            "key": f"page517-row{row}-{slug(name)}-b1027",
            "person_id": person_id,
            "source_adapter": "manual_staged_protocol",
            "query_text": f"{name}; NARA OSS index context; exact-name and meaningful initial, suffix, punctuation, transliteration and OCR variants; OSS, CIA Reading Room, rank, branch, assignment and protected-identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory and archival searches; indexed Box {box}",
            "query_variant_type": "staged_identity_employment_archival_protocol_batch_1027",
            "started_at": "2026-11-04T17:00:00-05:00",
            "completed_at": "2026-11-04T23:55:00-05:00",
            "outcome": outcome,
            "sources_reviewed": reviewed,
            "candidate_sources_rejected": rejected,
            "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, postwar-only leads and sources without an OSS, protected-identifier, rank, unit or personnel-file bridge were rejected. Army categories were not converted into named employers. The Lou/Louis conflict remained qualified, and a wholly different Army name was rejected.",
            "research_notes": f"{note} The official index, exact-name OSS searches, grouped CIA Reading Room checks, and employer, occupation, obituary, institutional, newspaper, directory and archival searches were reviewed as applicable. Page 517, the page 518 boundary, every cited NARA code-list page, OSS travel-order page 11, Nisei Linguists pages 141 and 208-209, and the January 20, 1943 Victory notice were checked. No authenticated NARA Catalog API request was made.",
            "next_action": f"Review indexed Box {box} for corroborating identifiers, immediate pre-OSS affiliation and last civilian employer before wartime service.",
            "attempt_number": 1,
            "research_agent_version": "before-oss-b1027-v1",
        })
    if len(attempts) != 46:
        raise RuntimeError(f"Expected 46 research attempts, generated {len(attempts)}")
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-1027-v1",
        "reviewer": "Before OSS Batch 1027 evidence review",
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
