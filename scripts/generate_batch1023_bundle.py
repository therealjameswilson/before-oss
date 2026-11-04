#!/usr/bin/env python3
"""Generate the reviewed Batch 1023 evidence bundle for PDF page 513."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page513-william-wood-to-perry-woosley-review_"
    "batch-1023_2026-11-04.json"
)

INDEX = "nara-index-b1023"
ARMY = "army-bulk-b1023"
TECH = "army-tech-b1023"
CODES = "army-codes-b1023"
KCL_WOODHOUSE = "kcl-special-forces-woodhouse-b1023"
IWM_WOODHOUSE = "iwm-woodhouse-interview-b1023"
JSTOR_WOOLBERT = "jstor-woolbert-foreign-affairs-1941-b1023"
UARK_WOOLCOCK = "uark-charles-morrow-wilson-papers-b1023"
SMITHSONIAN_WOOLCOCK = "smithsonian-iris-woolcock-photo-b1023"
CIA_WOOLINGTON = "cia-fighting-doctors-woolington-b1023"
JAVA_WOOLINGTON = "java-detachment101-woolington-b1023"
KCL_WOOLLEY = "kcl-hargreaves-woolley-b1023"
CIA_WOOLLEY = "cia-guardian-spies-woolley-b1023"
YALE_WOOLVERTON = "yale-woolverton-papers-b1023"
NARA_WOOLVERTON = "nara-oss-woolverton-1945-b1023"

ORG_GREEK_MISSION = "allied-military-mission-greece-b1023"
ORG_FOREIGN_AFFAIRS = "foreign-affairs-b1023"
ORG_ROYAL_NAVY = "royal-navy-b1023"
ORG_US_ARMY = "us-army-existing-b1023"
ORG_NEW_YORK_TRANSFER = "new-york-transfer-company-b1023"

WOOLINGTON_GROUP = "page513-sam-a-s-woolington-b1023"

PEOPLE = {
    1: ("569a07a6-1fff-5df3-9eb5-36d6336f3410", "William N Wood", "851"),
    2: ("83391f24-5548-5b16-8df5-a9b2055e0f6b", "William C Wood Jr.", "851"),
    3: ("4928746a-ac5d-5f66-b577-726010aef058", "William L Woodard", "851"),
    4: ("76c0d842-4300-5232-b60c-02fa0807bb19", "Marion L Woodburn", "851"),
    5: ("a33d476d-dfe6-52d0-8e22-a62f4e348162", "Donald Woodbury", "851"),
    6: ("7cba2a67-1b57-5566-a0cc-c25fc5d09de2", "Roger F Woodbury", "851"),
    7: ("a0967c02-d74a-5d6c-b7da-c76c52797068", "Virginia A Woodbury", "851"),
    8: ("747edf86-631b-582d-b66b-cfbf1d1564ae", "Charles C Woodcock", "851"),
    9: ("ca16e152-dc73-50fc-a7da-5ba895abae5f", "Louis E Woodcock", "852"),
    10: ("eb9a6cd4-dd5e-5af1-a5a1-dc70b19fe76f", "William H Woodford", "852"),
    11: ("b3045f6a-2338-5298-b5eb-b0e1cc04eefb", "Christopher M Woodhouse", "852"),
    12: ("f4f82943-7c0e-5685-8c8e-7d6ba7762cdf", "Roy Woodin", "852"),
    13: ("59c73959-8661-538f-a7d5-5dc05d32b282", "Louis K Woodland", "852"),
    14: ("91f6b254-a1e6-555a-84eb-aeea8a0aa144", "Eleanor H Woodman", "852"),
    15: ("cd6652de-d5e5-5cda-a89b-0a20e2fb79a3", "Beverly M Woodner", "852"),
    16: ("ebca3cdf-dc40-5e34-9bde-690470f02cfa", "Kenneth E Woodring", "852"),
    17: ("7d735504-b61f-50ce-a252-3cd9b65b56c4", "Shealene L Woodring", "852"),
    18: ("c62cbdcf-9ae8-51ae-b59f-90f8fe385fe0", "Dean A Woodruff", "852"),
    19: ("a7cb1638-f299-59dc-9822-bfac54cd74ed", "Emily C Woodruff", "852"),
    20: ("d7c71e24-73f1-5c22-b68e-63fc8e4e0ad0", "Fern L Woodruff", "852"),
    21: ("cba1f456-5990-5e7f-a275-edf180930f00", "Alexander H Woods", "852"),
    22: ("4139bb94-cb35-5970-ab1a-65d44fa48a26", "Douglas Woods", "852"),
    23: ("ee4fded9-c62f-5991-8fbf-d45c0a02b4bf", "Francis Woods", "852"),
    24: ("0134183a-bc8e-5ca2-95e1-946a1ddd222e", "Frank C Woods", "852"),
    25: ("da9e9220-afbe-52ab-b168-40c194aa673d", "Robert E Woods", "852"),
    26: ("b6831660-04c1-5027-bbff-15043ee59871", "Ruth M Woods", "852"),
    27: ("b3152881-2a9a-5a55-8195-4dfc8e9d86c1", "Stewart A Woods", "852"),
    28: ("6f6b73da-73b6-5ed5-aa7d-95143c2a7f06", "William H Woods", "852"),
    29: ("cab91020-0ac0-5d54-ad8c-2a34d3503a1e", "William J Woods", "852"),
    30: ("e7696fed-4826-5fda-b2d1-dc8606bb0d6f", "J P Woodside", "852"),
    31: ("4497e1be-176a-5b22-ab0a-b6f25d9dea64", "A. Arthur Woodward", "852"),
    32: ("77743230-fbed-50d5-80b7-1c9c21aabe3d", "Valorus C Woodworth", "852"),
    33: ("d357d3b8-b20c-5b33-a179-210672225c13", "Thomas Wooh", "852"),
    34: ("27dfd47b-0c66-5d10-8b61-10a07d7b549f", "Robert G Woolbert", "852"),
    35: ("e18fcc1d-d6de-5baf-945e-fc1a766993b4", "Iris Woolcock", "852"),
    36: ("5aacf593-8453-534a-b5b4-eddc8541a15e", "James H Wooley", "852"),
    37: ("b004796b-b64c-501a-839e-4d13e2dd1144", "Sam A Woolington", "852"),
    38: ("798d27bb-223f-538c-bb58-9b965dc3789c", "Sam S Woolington", "852"),
    39: ("93df2242-7184-577e-b648-d2b2ff830364", "H.G.A. Woolley", "852"),
    40: ("1104fd19-47a2-554f-9dde-8511172900e4", "Henry P Woolley", "852"),
    41: ("5a49a084-6fcd-503e-b552-637caf999651", "Herbert B Woolley", "853"),
    42: ("b3beb768-33e3-52a8-96d3-47515b2cca28", "Vivienne M Woolley", "853"),
    43: ("200641ea-480c-5ed6-b0fd-4a8abc3ac2bc", "John M Woolsey", "853"),
    44: ("1fa33b3a-3bbc-5973-a107-f6d2556b70e9", "Herbert N Woolson", "853"),
    45: ("90f77e6d-ed3b-5148-8cd3-a96ab0779541", "William H Woolverton", "853"),
    46: ("fdcd1c4c-fa87-5667-ac01-560b69a46621", "Perry Woosley", "853"),
}

ARMY_OCCUPATIONS = {
    3: ("1944-09-04", "002", "actor or actress", "Actors and actresses", "PDF physical page 170; historical category 0-02", "unknown"),
    13: ("1943-07-06", "992", "student", "Students", "PDF physical page 304; amended category 9-92", "student"),
    21: ("1941-10-01", "002", "actor or actress", "Actors and actresses", "PDF physical page 170; historical category 0-02", "unknown"),
    29: ("1942-07-06", "097", "manager or official, not elsewhere classified", "Managers and officials, n.e.c.", "PDF physical page 171; historical category 0-97", "unknown"),
    36: ("1943-05-13", "137", "stenographer or typist", "Stenographers and typists", "PDF physical page 171; historical category 1-37", "unknown"),
}

ARMY_IDENTITY_ONLY = {
    25: ("1946-03-26", "The reviewed Army entry postdates OSS dissolution; no grade, occupation, or pre-OSS chronology is transferred."),
    40: ("1940-12-23", "Historical occupation code 999 is undefined and is not interpreted."),
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def source(key: str, **kwargs: object) -> dict[str, object]:
    value: dict[str, object] = {"key": key, "access_date": "2026-11-04"}
    value.update(kwargs)
    return value


def sources() -> list[dict[str, object]]:
    return [
        source(INDEX, stable_url="https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf", archival_identifier="RG 226, Entry A1-224, Boxes 851-853", title="OSS Personnel Files from Excel", author_creator="National Archives and Records Administration", repository_publisher="National Archives and Records Administration", publication_record_date="2010-12-23", locator="PDF page 513, rows 1-46; visually checked at 180 dpi against the source table", source_quality="A_direct_official", collection_name="Records of the Office of Strategic Services, Record Group 226", rights_notes="All 46 printed rows remain separate. Full service or serial numbers remain private."),
        source(ARMY, source_id="cf280d3e-1262-5963-90d7-40ffa66c53a3", stable_url="https://catalog.archives.gov/id/1263923", archival_identifier="National Archives Identifier 1263923; parent series NAID 604357", title="Electronic Army Serial Number Merged File, ca. 1938-1946", author_creator="Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration", repository_publisher="National Archives and Records Administration", publication_record_date="1938-1946; merged file created 2002", locator="Official unrestricted ASNEF.FIN.DAT; eight Batch 1023 protected-identifier candidates reviewed", source_quality="A_direct_official", collection_name="World War II Army Enlistment Records", document_number="ASNEF.FIN.DAT", rights_notes="No raw record or full protected identifier is retained in public assets. Coded occupations identify neither employer nor workplace."),
        source(TECH, source_id="f24044fe-5fcd-5d78-96d4-25d577e90703", stable_url="https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf", archival_identifier="NN3-064-03-008; National Archives Identifier 1263923", title="World War II Army Enlistment Records: Reference Copy of Technical Documentation", author_creator="National Archives and Records Administration", repository_publisher="National Archives at College Park - Electronic Records", publication_record_date="1994-2005; reference copy modified 2011", locator="PDF physical pages 44-46; identifier, name, Army-entry-date, grade and civilian-occupation fields", source_quality="A_direct_official", collection_name="World War II Army Enlistment Records technical documentation", rights_notes="Used to interpret selected fields only; source damage, coding limits and incomplete coverage remain applicable."),
        source(CODES, source_id="ace136c1-722a-5af0-a43b-bab53792ae6a", stable_url="https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1CL_SD.pdf", archival_identifier="National Archives Identifier 1263923; Code No. 30", title="NARA Compiled Code Lists for the Electronic Army Serial Number Merged File", author_creator="National Archives and Records Administration", repository_publisher="National Archives at College Park - Electronic Records", publication_record_date="2011-01-12; modified 2011-03-17", locator="PDF physical pages 170-171 and 304; Batch 1023 categories visually checked", source_quality="A_direct_official", collection_name="World War II Army Enlistment Records technical documentation", rights_notes="Historical categories identify neither employer, institution nor workplace. Undefined code 999 is not interpreted."),
        source(KCL_WOODHOUSE, stable_url="https://www.kcl.ac.uk/library/assets/archives/specialforces.pdf", archival_identifier="Liddell Hart Centre for Military Archives, Woodhouse papers", title="Special Forces Research Guide", author_creator="Liddell Hart Centre for Military Archives", repository_publisher="King's College London", locator="PDF page 3, WOODHOUSE, Col C M, 5th Baron Terrington entry", source_quality="B_authoritative_institutional", collection_name="King's College London Archives research guides"),
        source(IWM_WOODHOUSE, stable_url="https://film.iwmcollections.org.uk/record/27037", archival_identifier="Film MGH 1301", title="ALL OUR YESTERDAYS: INTERVIEW WITH C M WOODHOUSE", author_creator="Imperial War Museums", repository_publisher="Imperial War Museums", locator="Collection record identifying Colonel Christopher Montague Woodhouse and the Allied Military Mission in Greece", source_quality="B_authoritative_institutional", collection_name="IWM Film"),
        source(JSTOR_WOOLBERT, stable_url="https://www.jstor.org/stable/20029081", archival_identifier="Foreign Affairs, Vol. 19, No. 2 (January 1941)", title="Recent Books on International Relations", author_creator="Robert Gale Woolbert", repository_publisher="Foreign Affairs; JSTOR", publication_record_date="1941-01", locator="Bibliographic record and byline", source_quality="C_reputable_contemporary_or_scholarly", collection_name="Foreign Affairs archive"),
        source(UARK_WOOLCOCK, stable_url="https://uark.as.atlas-sys.com/repositories/2/resources/1047", archival_identifier="Charles Morrow Wilson Papers", title="Charles Morrow Wilson Papers", author_creator="University of Arkansas Libraries Special Collections", repository_publisher="University of Arkansas Libraries", locator="Biographical timeline, ca. 1935-1937", source_quality="B_authoritative_institutional", collection_name="University of Arkansas Libraries finding aids"),
        source(SMITHSONIAN_WOOLCOCK, stable_url="https://www.si.edu/object/photograph-edna-reindel-her-cat-dozy%3AAAADCD_item_6376", archival_identifier="AAA object record item 6376", title="Photograph of Edna Reindel with her cat Dozy", author_creator="Iris Woolcock", repository_publisher="Smithsonian Institution", publication_record_date="ca. 1940", locator="Object record and creator credit", source_quality="B_authoritative_institutional", collection_name="Archives of American Art"),
        source(CIA_WOOLINGTON, stable_url="https://www.cia.gov/static/Fighting-Doctors-of-OSS.pdf", archival_identifier="Studies in Intelligence historical article", title="The Fighting Doctors of OSS", author_creator="Central Intelligence Agency", repository_publisher="Central Intelligence Agency", locator="Section identifying Dr. Sam Woolington as a Detachment 101 medical officer", source_quality="A_direct_official", collection_name="Studies in Intelligence"),
        source(JAVA_WOOLINGTON, stable_url="https://www.javadc.org/java/docs/1945-03-15%20OSSSU%20Detachment%20101%20Promotions%20and%20Citations%20OCR%20P11_MA.pdf", archival_identifier="OSS Special Operations Unit Detachment 101 promotions and citations, 15 March 1945", title="Detachment 101 Promotions and Citations", author_creator="Office of Strategic Services", repository_publisher="Java Veterans Association", publication_record_date="1945-03-15", locator="Page 11, promotion entry for Sam S. Woolington; full officer identifier withheld", source_quality="D_correlative_or_secondary", collection_name="Java Veterans Association document archive"),
        source(KCL_WOOLLEY, stable_url="https://kclpure.kcl.ac.uk/ws/files/2929338/521594.pdf", archival_identifier="King's College London doctoral thesis, 2008", title="An Analysis of the Rise, Use, Evolution and Value of Anglo-American Commando and Special Forces Formations, 1939-1945", author_creator="Andrew Lennox Hargreaves", repository_publisher="King's College London", publication_record_date="2008-08", locator="PDF printed pages 113-114; Woolley's Royal Navy attachment to COI and Maritime Unit command", source_quality="C_reputable_contemporary_or_scholarly", collection_name="King's Research Portal"),
        source(CIA_WOOLLEY, stable_url="https://www.cia.gov/resources/csi/static/UNCLASSIFIED-Extracts-Studies-67-1-March-2023.pdf", archival_identifier="Studies in Intelligence, Vol. 67, No. 1", title="Guardian Spies—From the Archive", author_creator="Central Intelligence Agency", repository_publisher="Central Intelligence Agency", publication_record_date="2023-03", locator="Guardian Spies section on the British naval officer assigned to organize OSS maritime training", source_quality="A_direct_official", collection_name="Studies in Intelligence"),
        source(YALE_WOOLVERTON, stable_url="https://ead-pdfs.library.yale.edu/3510.pdf", archival_identifier="MS 1748", title="William Henderson Woolverton Papers", author_creator="Manuscripts and Archives, Yale University Library", repository_publisher="Yale University Library", locator="PDF page 4, Biographical / Historical note", source_quality="B_authoritative_institutional", collection_name="Yale University Library finding aids"),
        source(NARA_WOOLVERTON, stable_url="https://www.archives.gov/files/research/jfk/releases/2022/104-10165-10143.pdf", archival_identifier="104-10165-10143", title="Headquarters 2677th Regiment OSS memorandum concerning Lt. William H. Woolverton", author_creator="Office of Strategic Services", repository_publisher="National Archives and Records Administration", publication_record_date="1945-01-14", locator="Memorandum heading and subject line", source_quality="A_direct_official", collection_name="JFK Assassination Records Collection; OSS record"),
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {"key": ORG_GREEK_MISSION, "canonical_name": "Allied Military Mission to the Greek Guerrillas", "historical_name": "British Military Mission to the Greek Guerrillas", "aliases": ["Allied Military Mission in Greece", "British Military Mission"], "organization_type": "Allied military mission", "sector": "military", "country": "Greece", "active_dates": "1942-1945", "normalization_notes": "The mission's British and later Allied names are preserved; it is not merged into OSS."},
        {"key": ORG_FOREIGN_AFFAIRS, "canonical_name": "Foreign Affairs", "historical_name": "Foreign Affairs", "organization_type": "foreign-policy journal", "sector": "journalism_and_media", "city": "New York", "state_or_region": "New York", "country": "United States", "normalization_notes": "Modeled only as a professional publication affiliation; authorship does not establish employment by the journal or its publisher."},
        {"key": ORG_ROYAL_NAVY, "canonical_name": "Royal Navy", "historical_name": "Royal Navy", "aliases": ["RN", "British Royal Navy"], "organization_type": "armed service", "sector": "military", "country": "United Kingdom", "normalization_notes": "Royal Navy service is a military assignment, never a civilian employer."},
        {"key": ORG_US_ARMY, "organization_id": "28a26f92-78af-5a1a-9c09-a843eb5975b4", "canonical_name": "United States Army", "historical_name": "United States Army", "aliases": ["U.S. Army", "Army", "AUS"], "organization_type": "military service", "sector": "military", "country": "United States", "normalization_notes": "Military assignment is modeled separately from civilian employment."},
        {"key": ORG_NEW_YORK_TRANSFER, "canonical_name": "New York Transfer Company", "historical_name": "New York Transfer Company", "organization_type": "transportation company", "sector": "business_and_industry", "city": "New York", "state_or_region": "New York", "country": "United States", "normalization_notes": "Historical company name preserved exactly as supplied by the Yale finding aid; no modern successor is substituted."},
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
    for row, (date, code, occupation, _label, _locator, relationship) in ARMY_OCCUPATIONS.items():
        values.append(affiliation(
            f"{slug(PEOPLE[row][1])}-army-occupation-b1023", row, relationship,
            "strongly_date_bounded", "high_confidence" if row == 13 else "confirmed",
            "medium", "A_direct_official", "publish_qualified",
            occupation=occupation, end_date=date,
            date_precision=f"Historical civilian-occupation code {code} was recorded at Army entry on {date}; no named employer or institution is supplied.",
            country="United States", immediate_pre_oss=False, last_civilian_pre_service=False,
            research_notes="Broad historical category only; it is excluded from verified-employer analytics and is not narrowed beyond the official wording.",
        ))
    values.extend([
        affiliation("woodhouse-allied-mission-b1023", 11, "military_assignment", "temporal_relation_uncertain", "high_confidence", "high", "B_authoritative_institutional", organization_key=ORG_GREEK_MISSION, organization_name_as_found="British, later Allied, Military Mission to the Greek guerrillas", role_title="second in command; later commander", start_date="1942", end_date="1945", date_precision="King's dates second-in-command service to 1942-1943 and mission command to 1943-1945; exact sequence relative to the indexed OSS file is not established", country="Greece", immediate_pre_oss=False, last_civilian_pre_service=False, research_notes="Documented Allied wartime assignment. It is not presented as a civilian employer or an established immediate OSS predecessor."),
        affiliation("woolbert-foreign-affairs-b1023", 34, "professional_affiliation", "documented_prewar", "high_confidence", "medium", "C_reputable_contemporary_or_scholarly", "publish_qualified", organization_key=ORG_FOREIGN_AFFAIRS, organization_name_as_found="Foreign Affairs", role_title="author and book reviewer", occupation="writer and reviewer on international affairs", end_date="1941-01", date_precision="A January 1941 Foreign Affairs bibliographic record carries Robert Gale Woolbert's byline; no employment relationship is stated", city="New York", state_or_region="New York", country="United States", immediate_pre_oss=False, last_civilian_pre_service=False, research_notes="Professional publication affiliation only. It does not prove employment by Foreign Affairs or the Council on Foreign Relations."),
        affiliation("iris-woolcock-photographer-b1023", 35, "unknown", "documented_prewar", "high_confidence", "medium", "B_authoritative_institutional", "publish_qualified", occupation="photographer", end_date="1940", date_precision="A Smithsonian object credits Iris Woolcock as photographer around 1940; the Arkansas finding aid independently places the distinctive name in the mid-1930s", country="United States", immediate_pre_oss=False, last_civilian_pre_service=False, research_notes="Occupation only. No employer, studio, self-employment status, or immediate OSS transition is inferred."),
        affiliation("woolley-royal-navy-b1023", 39, "military_assignment", "explicit_immediate", "confirmed", "high", "A_direct_official", organization_key=ORG_ROYAL_NAVY, organization_name_as_found="Royal Navy", role_title="commander attached to COI to advise on maritime methods", start_date="1942-02", end_date="1943-01", date_precision="The scholarly history explicitly dates Woolley's Royal Navy attachment to COI to February 1942 and his OSS Maritime Unit command to January 1943", city="Washington", state_or_region="District of Columbia", country="United States", immediate_pre_oss=True, last_civilian_pre_service=False, research_notes="Direct Royal Navy-to-COI/OSS assignment; military service, not civilian employment."),
        affiliation("woolverton-us-army-b1023", 45, "military_assignment", "strongly_date_bounded", "high_confidence", "high", "B_authoritative_institutional", organization_key=ORG_US_ARMY, organization_name_as_found="Army Transportation Corps", role_title="officer at Staten Island Port of Embarkation and with the Transportation Corps in England", start_date="1942", end_date="1945-01", date_precision="Yale dates his Army commission to 1942 and two years at the port before England; a direct OSS memorandum names him on 14 January 1945", country="United States and United Kingdom", immediate_pre_oss=True, last_civilian_pre_service=False, research_notes="Strongly date-bounded military pathway into the indexed OSS context; the sources do not state an exact transfer day."),
        affiliation("woolverton-family-farms-b1023", 45, "self_employment", "strongly_date_bounded", "high_confidence", "high", "B_authoritative_institutional", occupation="farm manager", role_title="manager of two large farms on the family estate", start_date="1928", end_date="1942", date_precision="Yale says he managed the farms after moving to Alexandria in 1928 and was commissioned in the Army in 1942", city="Alexandria", state_or_region="Pennsylvania", country="United States", immediate_pre_oss=False, last_civilian_pre_service=True, research_notes="Last civilian work before Army service. No separate employing organization is invented for the family estate."),
        affiliation("woolverton-new-york-transfer-b1023", 45, "employment", "documented_prewar", "high_confidence", "high", "B_authoritative_institutional", organization_key=ORG_NEW_YORK_TRANSFER, organization_name_as_found="New York Transfer Company", role_title="company officer", start_date="1919", end_date="1928", date_precision="Yale places this job after his 1919 return from wartime service and before his 1928 move to Pennsylvania", city="New York", state_or_region="New York", country="United States", immediate_pre_oss=False, last_civilian_pre_service=False, research_notes="Earlier documented employment, kept separate from the later farm management and Army pathway."),
    ])
    return values


def claim(key: str, row: int, claim_type: str, text: str, paraphrase: str, identity: str, temporal: str, quality: str, confidence: str, source_links: list[dict[str, str]], notes: str, status: str = "published", affiliation_key: str | None = None) -> dict[str, object]:
    value: dict[str, object] = {
        "key": key, "person_id": PEOPLE[row][0], "claim_type": claim_type,
        "claim_text": text, "evidence_paraphrase": paraphrase,
        "identity_match_assessment": identity, "temporal_assessment": temporal,
        "source_quality": quality, "claim_confidence": confidence,
        "publication_status": status, "match_notes": notes, "sources": source_links,
    }
    if affiliation_key:
        value["affiliation_key"] = affiliation_key
    return value


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, label, locator, _relationship) in ARMY_OCCUPATIONS.items():
        name = PEOPLE[row][1]
        high = row == 13
        values.append(claim(f"identity-{slug(name)}-b1023", row, "identity", f"Indexed {name} is {'a high-confidence match to' if high else 'confirmed as'} the reviewed Army record.", "The official sources agree through a nonshared protected identifier and compatible name evidence.", "High confidence from a nonshared protected identifier and a one-letter Louis/Lois variant; the identifier remains private." if high else "Confirmed by a nonshared protected identifier and exact official name agreement; the identifier remains private.", "Identity evidence only; Army entry is not treated as an exact OSS-transition date.", "A_direct_official", "high" if high else "confirmed", [{"source_key": INDEX, "locator_override": f"PDF page 513, row {row}; Box {PEOPLE[row][2]}"}, {"source_key": ARMY}, {"source_key": TECH, "support_type": "context_only"}], "The review withholds the identifier and does not convert Army fields into a named employer."))
        values.append(claim(f"occupation-{slug(name)}-b1023", row, "occupation", f"At Army entry on {date}, {name}'s record carried historical civilian-occupation category {code}: {occupation}.", f"The official bulk record carries code {code}; NARA's compiled list labels that category '{label}'.", "High confidence from protected-identifier agreement and the compatible Louis/Lois name variant." if high else "Confirmed by protected-identifier agreement and exact official name evidence.", "Strongly date-bounded at Army entry, but not proof of an immediate predecessor affiliation or exact OSS start date.", "A_direct_official", "medium", [{"source_key": ARMY}, {"source_key": TECH, "support_type": "context_only"}, {"source_key": CODES, "locator_override": locator}], "A historical category only; excluded from verified-employer analytics and never converted into a named employer.", "publish_qualified", f"{slug(name)}-army-occupation-b1023"))
    for row, (date, note) in ARMY_IDENTITY_ONLY.items():
        name = PEOPLE[row][1]
        values.append(claim(f"identity-{slug(name)}-b1023", row, "identity", f"Indexed {name} is confirmed as the reviewed Army record.", "The exact official name and a nonshared protected identifier connect the index and Army records.", "Confirmed by exact official name agreement and a nonshared protected identifier; the identifier remains private.", f"Army entry is dated {date}. {note}", "A_direct_official", "confirmed", [{"source_key": INDEX, "locator_override": f"PDF page 513, row {row}; Box {PEOPLE[row][2]}"}, {"source_key": ARMY}, {"source_key": TECH, "support_type": "context_only"}], "Identity only; no Army grade, undefined occupation, or post-OSS chronology is converted into pre-OSS evidence."))
    values.extend([
        claim("identity-christopher-woodhouse-b1023", 11, "identity", "Indexed Christopher M Woodhouse is high-confidence identified as Colonel Christopher Montague Woodhouse, later 5th Baron Terrington.", "King's and IWM use the full name or exact initials and document command of the Allied Military Mission in Greece, matching the index's British note.", "High confidence from exact initials, rare surname, British status and a specific Allied wartime command; the personnel file remains unreviewed.", "The sources document 1942-1945 Allied service but not the exact sequence relative to the indexed OSS file.", "B_authoritative_institutional", "high", [{"source_key": INDEX}, {"source_key": KCL_WOODHOUSE}, {"source_key": IWM_WOODHOUSE}], "The British mission is kept distinct from OSS and civilian employment."),
        claim("allied-mission-christopher-woodhouse-b1023", 11, "other_pre_oss_affiliation", "Christopher M. Woodhouse served as second in command and later commander of the British, then Allied, Military Mission to the Greek guerrillas.", "King's dates the roles to 1942-1945; IWM independently identifies him as commander of the Allied Military Mission in Greece.", "High-confidence identity from the rare name, initials and British wartime context.", "Documented wartime assignment; its exact temporal relationship to the indexed OSS personnel file is uncertain.", "B_authoritative_institutional", "high", [{"source_key": KCL_WOODHOUSE}, {"source_key": IWM_WOODHOUSE}], "Published as an Allied military assignment, not a civilian employer or settled immediate predecessor.", affiliation_key="woodhouse-allied-mission-b1023"),
        claim("identity-robert-woolbert-b1023", 34, "identity", "Indexed Robert G Woolbert is high-confidence identified as Foreign Affairs author Robert Gale Woolbert.", "The rare full surname, first name and middle initial agree with the contemporary byline.", "High confidence from a rare exact name pattern and compatible prewar date, but no personnel-file bridge has yet been reviewed.", "The 1941 publication predates OSS; it does not establish an OSS start date.", "C_reputable_contemporary_or_scholarly", "high", [{"source_key": INDEX}, {"source_key": JSTOR_WOOLBERT}], "The match supports qualified publication; the personnel file remains necessary for direct confirmation."),
        claim("foreign-affairs-robert-woolbert-b1023", 34, "other_pre_oss_affiliation", "Robert Gale Woolbert published book reviews in Foreign Affairs before U.S. entry into the war.", "A January 1941 Foreign Affairs record carries his full byline.", "High-confidence identity from the distinctive full name and compatible date.", "Documented prewar professional affiliation; it does not prove employment or immediacy to OSS.", "C_reputable_contemporary_or_scholarly", "medium", [{"source_key": JSTOR_WOOLBERT}], "Authorship is not recast as employment by Foreign Affairs or the Council on Foreign Relations.", "publish_qualified", "woolbert-foreign-affairs-b1023"),
        claim("identity-iris-woolcock-b1023", 35, "identity", "Indexed Iris Woolcock is high-confidence identified as the photographer documented by the Smithsonian and University of Arkansas.", "Two institutional records use the rare exact name and place her in the United States during the 1930s and around 1940.", "High confidence from the distinctive exact name and mutually compatible institutional chronology; no personnel-file bridge has yet been reviewed.", "The records predate U.S. wartime OSS activity but do not establish an OSS transition.", "B_authoritative_institutional", "high", [{"source_key": INDEX}, {"source_key": UARK_WOOLCOCK}, {"source_key": SMITHSONIAN_WOOLCOCK}], "The finding aid is used for chronology; no spouse's employment is transferred to her."),
        claim("occupation-iris-woolcock-b1023", 35, "occupation", "Iris Woolcock was a photographer by about 1940.", "The Smithsonian credits Iris Woolcock as creator of a photograph dated about 1940.", "High-confidence identity from the distinctive exact name and corroborating institutional chronology.", "Documented prewar occupation; no employer, studio, self-employment status, or immediate OSS relationship is stated.", "B_authoritative_institutional", "medium", [{"source_key": SMITHSONIAN_WOOLCOCK}, {"source_key": UARK_WOOLCOCK, "support_type": "context_only"}], "Published as qualified occupation only; no employer is invented.", "publish_qualified", "iris-woolcock-photographer-b1023"),
        claim("identity-sam-woolington-b1023", 38, "identity", "Indexed Sam S Woolington is confirmed as the Detachment 101 medical officer documented in direct OSS and CIA sources.", "The exact full name and a privately matched officer identifier agree with an OSS promotion record; CIA independently describes Dr. Sam Woolington's Detachment 101 role.", "Confirmed through exact name, protected-identifier agreement and compatible medical-officer context; the full identifier remains private.", "Wartime identity evidence only; the sources do not identify pre-OSS employment.", "A_direct_official", "confirmed", [{"source_key": INDEX}, {"source_key": JAVA_WOOLINGTON}, {"source_key": CIA_WOOLINGTON}], "The adjacent Sam A Woolington index row remains separate in a possible-duplicate group pending joint folder review."),
        claim("identity-hga-woolley-b1023", 39, "identity", "Indexed H.G.A. Woolley is confirmed as the Royal Navy commander attached to COI and later appointed to command the OSS Maritime Unit.", "The exact initials, commander rank and British note agree with a scholarly history grounded in named RG 226 records and an official CIA history.", "Confirmed from exact initials, rank, nationality note and a unique COI/OSS Maritime Unit chronology.", "The sources explicitly sequence Royal Navy service, COI attachment and OSS Maritime Unit command.", "A_direct_official", "confirmed", [{"source_key": INDEX}, {"source_key": KCL_WOOLLEY}, {"source_key": CIA_WOOLLEY}], "No civilian occupation or later screenwriting lead is used."),
        claim("royal-navy-hga-woolley-b1023", 39, "immediate_pre_oss_affiliation", "Commander H.G.A. Woolley's immediate predecessor affiliation was the Royal Navy, from which he was attached to COI in February 1942.", "Hargreaves explicitly identifies Woolley as an experienced British naval officer loaned to COI; CIA independently documents the British naval assignment.", "Confirmed by exact initials, commander rank, British note and unique maritime chronology.", "Explicit immediate Royal Navy-to-COI sequence, followed by OSS Maritime Unit command in January 1943.", "A_direct_official", "high", [{"source_key": KCL_WOOLLEY}, {"source_key": CIA_WOOLLEY}], "Military assignment, not civilian employment.", affiliation_key="woolley-royal-navy-b1023"),
        claim("identity-william-woolverton-b1023", 45, "identity", "Indexed William H Woolverton is high-confidence identified as William Henderson Woolverton of the Yale papers and the 2677th Regiment OSS memorandum.", "Yale supplies the full name and Army chronology; a direct 1945 OSS memorandum names Lt. William H. Woolverton.", "High confidence from exact name and middle initial, commissioned Army status and direct OSS context; the personnel file remains unreviewed.", "The sources establish prewar employment, 1942 Army entry and OSS context by January 1945.", "A_direct_official", "high", [{"source_key": INDEX}, {"source_key": YALE_WOOLVERTON}, {"source_key": NARA_WOOLVERTON}], "Protected identifiers remain private; the chronology does not depend on them."),
        claim("army-william-woolverton-b1023", 45, "immediate_pre_oss_affiliation", "William H. Woolverton's best-supported immediate pre-OSS pathway was U.S. Army transportation service.", "Yale places him at the Staten Island Port of Embarkation and then with the Transportation Corps in England; an OSS memorandum names him in January 1945.", "High-confidence identity from exact name, middle initial, officer status and direct OSS context.", "Strongly date-bounded Army-to-OSS sequence; no source states the exact transfer day.", "B_authoritative_institutional", "high", [{"source_key": YALE_WOOLVERTON}, {"source_key": NARA_WOOLVERTON}], "Qualified as strongly date-bounded, not explicit immediate language.", affiliation_key="woolverton-us-army-b1023"),
        claim("farms-william-woolverton-b1023", 45, "last_civilian_pre_service", "William H. Woolverton managed two large family-estate farms in Alexandria, Pennsylvania, before his 1942 Army commission.", "Yale dates his move and farm management from 1928 and next records the 1942 commission.", "High-confidence identity from the full-name Yale papers and direct OSS corroboration.", "Strongly date-bounded as the last documented civilian work before Army service.", "B_authoritative_institutional", "high", [{"source_key": YALE_WOOLVERTON}], "Modeled as self-employment/family-estate management; no employer is invented.", affiliation_key="woolverton-family-farms-b1023"),
        claim("new-york-transfer-william-woolverton-b1023", 45, "other_pre_oss_affiliation", "William H. Woolverton was an officer of the New York Transfer Company from 1919 until moving to Pennsylvania in 1928.", "Yale's biographical note places the named company between his first wartime service and later farm management.", "High-confidence identity from the full-name Yale papers and direct OSS corroboration.", "Documented earlier prewar employment; it was not his last civilian role before the 1942 commission.", "B_authoritative_institutional", "high", [{"source_key": YALE_WOOLVERTON}], "Earlier employer kept separate from the later family-farm role.", affiliation_key="woolverton-new-york-transfer-b1023"),
    ])
    return values


def unresolved_reason(row: int) -> str:
    reasons = {
        5: "The protected-identifier Army candidate is Ronald T Woodbury, not Donald Woodbury, and is rejected entirely.",
        16: "An unofficial wartime organization-chart lead names Kenneth E. Woodring in an OSS finance role but supplies no pre-OSS affiliation or direct source bridge.",
        31: "An archaeologist namesake could not be bridged to the index row and is rejected.",
        37: "The adjacent confirmed Sam S Woolington record makes a duplicate or index-variation possible, but the different middle initial prohibits merging.",
        43: "Official sources document Judge John Munro Woolsey and Lt. John M. Woolsey Jr.; neither is bridged to this index row, so both remain rejected alternatives.",
        44: "A Spokane enlistment namesake has a different full protected identifier and is rejected.",
    }
    return reasons.get(row, "Accessible exact-name, official, OSS, employer, occupation, obituary, institutional, newspaper, directory and archival searches produced no reliable identity-and-affiliation bridge; unbridged namesakes and postwar-only leads were rejected.")


def base_update(row: int, **overrides: object) -> dict[str, object]:
    value: dict[str, object] = {"person_id": PEOPLE[row][0], "manual_review_required": True, "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "high"}
    value.update(overrides)
    return value


def person_updates() -> list[dict[str, object]]:
    special = set(ARMY_OCCUPATIONS) | set(ARMY_IDENTITY_ONLY) | {11, 34, 35, 38, 39, 45}
    values: list[dict[str, object]] = []
    for row in sorted(set(PEOPLE) - special):
        reason = unresolved_reason(row)
        values.append(base_update(row, identity_status="ambiguous" if row == 37 else "unresolved", identity_evidence=f"The visually verified page 513 source preserves {PEOPLE[row][1]} and Box {PEOPLE[row][2]}. {reason}", possible_duplicate_group=WOOLINGTON_GROUP if row == 37 else None, research_status="requires_archival_review", archival_review_priority="critical" if row in {5, 31, 37, 43, 44} else "high", next_action=f"Review indexed Box {PEOPLE[row][2]} for corroborating identifiers, immediate pre-OSS affiliation and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}"))
    for row in ARMY_OCCUPATIONS:
        high = row == 13
        values.append(base_update(row, identity_status="high_confidence" if high else "confirmed", identity_evidence="A nonshared protected identifier and a one-letter Louis/Lois variant connect the official records; the identifier remains private." if high else "A nonshared protected identifier and exact official name agreement connect the index and Army records; the identifier remains private.", name_variants=["Lois K Woodland"] if high else None, replace_name_variants=False, personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="occupation_only_found", nara_catalog_id="1263923", next_action=f"Review indexed Box {PEOPLE[row][2]} to identify a named employer or institution and establish Army-to-OSS chronology; the bulk record supplies only a historical occupation category."))
    values.extend([
        base_update(25, identity_status="confirmed", identity_evidence="A nonshared protected identifier and exact official name agreement connect the records; the dated Army entry is post-OSS and supports identity only.", research_status="requires_archival_review", nara_catalog_id="1263923", next_action="Review Box 852 for Robert E Woods's pre-OSS affiliation. The 1946 Army entry is not used as pre-OSS evidence."),
        base_update(40, identity_status="confirmed", identity_evidence="A nonshared protected identifier and exact official name agreement connect the records; undefined code 999 supplies no occupation.", personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="requires_archival_review", nara_catalog_id="1263923", next_action="Review Box 852 for Henry P Woolley's immediate affiliation and last civilian employer; code 999 is not interpreted."),
        base_update(11, identity_status="high_confidence", identity_evidence="Exact initials, rare surname, the index's British note and the documented Allied mission command support high confidence.", name_variants=["Christopher Montague Woodhouse", "C. M. Woodhouse", "5th Baron Terrington"], replace_name_variants=False, personnel_category="foreign_or_allied_military_personnel", commissioned_officer=True, allied_or_foreign_personnel=True, research_status="requires_archival_review", archival_review_priority="medium", next_action="Review Box 852 to establish the Allied-mission relationship to OSS and identify the last civilian employer; the wartime assignment is documented but its exact sequence is not."),
        base_update(34, identity_status="high_confidence", identity_evidence="The rare exact first name, surname and middle initial align with Robert Gale Woolbert's dated Foreign Affairs byline; the personnel file remains unreviewed.", name_variants=["Robert Gale Woolbert"], replace_name_variants=False, research_status="occupation_only_found", archival_review_priority="medium", next_action="Review Box 852 to confirm identity, determine whether Foreign Affairs was employment or only authorship, and identify the immediate pre-OSS affiliation."),
        base_update(35, identity_status="high_confidence", identity_evidence="Two institutional records use the rare exact name and place photographer Iris Woolcock in a compatible prewar chronology.", research_status="occupation_only_found", archival_review_priority="medium", next_action="Review Box 852 to confirm identity, identify any photography employer or self-employment status, and establish the OSS transition."),
        base_update(38, identity_status="confirmed", identity_evidence="Exact name, a privately matched officer identifier and compatible Detachment 101 medical-officer sources confirm the record; the identifier remains withheld.", name_variants=["Dr. Sam Woolington", "Sam S. Woolington"], replace_name_variants=False, personnel_category="commissioned_army_officer", commissioned_officer=True, allied_or_foreign_personnel=False, possible_duplicate_group=WOOLINGTON_GROUP, research_status="requires_archival_review", archival_review_priority="critical", next_action="Review both Sam A and Sam S Woolington folders in Box 852 to resolve possible duplication and identify pre-OSS medical employment."),
        base_update(39, identity_status="confirmed", identity_evidence="Exact initials, commander rank, British note and a unique Royal Navy-to-COI/OSS Maritime Unit chronology converge.", name_variants=["Commander H.G.A. Woolley", "H. G. A. Woolley"], replace_name_variants=False, personnel_category="foreign_or_allied_military_personnel", commissioned_officer=True, allied_or_foreign_personnel=True, research_status="completed", archival_review_priority="medium", next_action="Review Box 852 for any documented last civilian employer before Royal Navy service; the immediate Royal Navy pathway is already supported."),
        base_update(45, identity_status="high_confidence", identity_evidence="The exact name and middle initial, commissioned Army chronology, Yale full name and direct 1945 OSS memorandum converge.", name_variants=["William Henderson Woolverton", "Lt. William H. Woolverton"], replace_name_variants=False, personnel_category="commissioned_army_officer", commissioned_officer=True, allied_or_foreign_personnel=False, research_status="verified_employer_found", archival_review_priority="medium", next_action="Review Box 853 for the exact Army-to-OSS transfer date; last civilian farm management and earlier New York Transfer Company employment are documented."),
    ])
    if len(values) != 46:
        raise RuntimeError(f"Expected 46 person updates, generated {len(values)}")
    return values


def research_attempts() -> list[dict[str, object]]:
    attempts: list[dict[str, object]] = []
    substantiated = {11, 34, 35, 38, 39, 45} | set(ARMY_OCCUPATIONS) | set(ARMY_IDENTITY_ONLY)
    for row, (person_id, name, box) in PEOPLE.items():
        if row in substantiated:
            outcome = "source_reviewed"
            reviewed = 8 if row in {11, 34, 35, 38, 39, 45} else 5
            rejected = 4
            note = "At least one identity, occupation or affiliation outcome is preserved with claim-level citations; unresolved employer or temporal questions remain explicit."
        else:
            outcome = "candidate_rejected"
            reviewed = 6
            rejected = 5
            note = unresolved_reason(row)
        attempts.append({
            "key": f"page513-row{row}-{slug(name)}-b1023",
            "person_id": person_id,
            "source_adapter": "manual_staged_protocol",
            "query_text": f"{name}; NARA OSS index context; exact-name and meaningful initial, suffix, punctuation and OCR variants; OSS, rank, branch, assignment and protected-identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory and archival searches; indexed Box {box}",
            "query_variant_type": "staged_identity_employment_archival_protocol_batch_1023",
            "started_at": "2026-11-04T18:20:00Z",
            "completed_at": "2026-11-04T22:10:00Z",
            "outcome": outcome,
            "sources_reviewed": reviewed,
            "candidate_sources_rejected": rejected,
            "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, postwar-only leads and sources without an OSS, protected-identifier, rank, unit or personnel-file bridge were rejected. Army categories were not converted into named employers.",
            "research_notes": f"{note} The official index, exact-name searches, CIA or equivalent official context, and employer, occupation, obituary, institutional, newspaper, directory and archival leads were reviewed as applicable. Page 513 and every cited NARA code-list page were visually checked. No authenticated NARA Catalog API request was made.",
            "next_action": f"Review indexed Box {box} for corroborating identifiers, immediate pre-OSS affiliation and last civilian employer before wartime service.",
            "attempt_number": 1,
            "research_agent_version": "before-oss-b1023-v1",
        })
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-1023-v1",
        "reviewer": "Before OSS Batch 1023 evidence review",
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
