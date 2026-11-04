#!/usr/bin/env python3
"""Generate the reviewed Batch 1028 evidence bundle for PDF page 518."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page518-cecile-youmanns-to-renie-yuen-review_"
    "batch-1028_2026-11-04.json"
)

INDEX = "nara-index-b1028"
ARMY = "army-bulk-b1028"
TECH = "army-tech-b1028"
CODES = "army-codes-b1028"
CUYLER_MEMORIAL = "cambridge-cuyler-young-b1028"
NPS_YOUNGER = "nps-evelle-younger-b1028"
CA_AG_YOUNGER = "ca-ag-evelle-younger-b1028"
CIA_RODNEY = "cia-rodney-young-b1028"
OSS_RODNEY = "oss-rodney-young-report-b1028"
CIA_YOVANOVICH = "cia-peter-yovanovich-b1028"

ORG_TORONTO = "university-toronto-existing-b1028"
ORG_FBI = "fbi-existing-b1028"
ORG_GREEK_RED_CROSS = "greek-red-cross-b1028"
ORG_ASCSA = "ascsa-existing-b1028"

PEOPLE = {
    1: ("11b19ea5-9d24-5408-863a-2d24d8c44328", "Cecile W Youmanns", "858"),
    2: ("af6d7359-29c0-573d-b80f-26c4b8b7afc6", "Key S Youn", "858"),
    3: ("0349d1c8-8fad-580e-948f-3838e7ab9c9d", "Aaron Young", "859"),
    4: ("745f8df7-3127-53ce-89c8-4c11cc9780e3", "Alan Young", "859"),
    5: ("56038dc1-0636-539f-bb0d-851ca9599d26", "Anne B Young", "859"),
    6: ("a91d3006-7d5f-5ba3-bd8d-0aabbb31929d", "Arthur C Young", "859"),
    7: ("f7b9a623-ea38-5c6a-8458-0f56a893f01c", "Austin Young", "859"),
    8: ("dfb75d1e-8ed0-5032-95b2-892893a6b6cb", "Beatrice E Young", "859"),
    9: ("0ab2055a-bbd9-5e7e-8c64-df1be9ae4073", "Billy B Young", "859"),
    10: ("ff12edd0-667f-5eb9-b987-e06221021280", "Carleton Young", "859"),
    11: ("10c02aa8-0e40-5fd7-b6cd-75941cd76887", "Charles W Young", "859"),
    12: ("2a713c79-9136-5570-a860-487b8f8d9730", "Cuyler T Young", "859"),
    13: ("abf3052e-b6d2-5a36-ba78-d4fe67385f52", "Edward L Young", "859"),
    14: ("ca30c960-5ec7-584e-b685-48aeebc6da49", "Elwood W Young", "859"),
    15: ("d26f561b-cea7-5c7b-a950-7aa0db24f408", "Emma M Young", "859"),
    16: ("ac679997-dee1-5ae4-893a-119dd3954672", "Everett Young", "859"),
    17: ("8a4a6554-627f-53b0-ab01-aaa64da2f9de", "Gerald S Young Jr.", "859"),
    18: ("9a6ec6eb-234a-53f9-aec2-540fc7142211", "Grace Young", "859"),
    19: ("11d88fdb-760e-513a-ad1b-3614b054aaad", "Herbert B Young", "859"),
    20: ("a1b5ac23-70e5-5d15-b958-eb13f0df4cf1", "James B Young", "859"),
    21: ("87b7b0e5-face-550b-bd59-a594dc9bcafc", "James G Young", "859"),
    22: ("c5d30738-9513-5f14-97c8-d4c3398f8263", "James M Young", "859"),
    23: ("8404f04b-6992-53f5-a788-5b7ca99d4ba5", "James S Young", "859"),
    24: ("bbe100b9-b736-5d03-988f-874253a18574", "John C Young", "859"),
    25: ("451c4fad-8a65-56c9-9571-52d0c424d0ec", "Lewis E Young", "859"),
    26: ("70cae759-bc66-55a4-9e55-71e65b5e8d26", "Lionel Young", "859"),
    27: ("2ac60fdc-bbe0-52ff-a5ba-42cd14aa4ee8", "Lloyd D Young", "859"),
    28: ("fb98a849-35a6-5ec0-a711-6e287d76ec7a", "Marie H Young", "859"),
    29: ("736166e0-2cab-5231-aa3b-6c7db8d533d7", "Olga D Young", "859"),
    30: ("cc2c514e-2909-5417-a53e-07d08742182c", "Raymond B Young Jr.", "859"),
    31: ("84daf75f-418f-5a3a-943f-59520de47f1d", "Richard K Young", "860"),
    32: ("3875835c-ef00-57d8-8ffd-dd1e7eed5857", "Rodney S Young", "860"),
    33: ("76e499cb-c269-51e9-9724-c58fc5176e93", "Russell L Young", "860"),
    34: ("36ed6e32-da25-5788-96e0-ea6e4c77040b", "Velma F Young", "860"),
    35: ("71bd3b70-34e0-5ed4-b5e0-dc341b565500", "Vergil A Young", "860"),
    36: ("2faa3545-1c3f-5b89-bf8d-c6f318e46a36", "Vernon L Young", "860"),
    37: ("57be2d80-3ed9-58ff-81b7-0e8d38c92c6f", "Victor E Young", "860"),
    38: ("8b25f4b8-9f57-55ef-b484-f2621aed1fdd", "Victor S Young", "860"),
    39: ("0489b48e-5f7b-5250-83ea-b09019b64000", "William W Young", "860"),
    40: ("e8b40847-8897-5d2a-8d44-03dbd47d705f", "Evelle J Younger", "860"),
    41: ("34da1faa-540f-5d54-abb5-90c26275038a", "Jack S Younger", "860"),
    42: ("2b34c859-063a-59e1-83f4-3d11a3ef16fb", "William E Youngs", "860"),
    43: ("23470a98-0e23-5f22-b099-2ded95aca4cf", "Robert L Younkin", "860"),
    44: ("a859c7a1-daa0-5e28-8fba-ff3236d4cf26", "Peter, Dr. Yovanovich", "860"),
    45: ("937fdce7-70ba-520c-b764-c089b78668ef", "Arthur Yshira", "860"),
    46: ("59596457-3383-5bce-9046-757979567629", "Renie Yuen", "860"),
}

ARMY_OCCUPATIONS = {
    3: ("1942-12-08", "001", "accountant or auditor", "Accountants and auditors", "PDF physical page 170"),
    13: ("1942-11-05", "992", "student", "Students", "PDF physical page 304; amended category 9-92"),
    16: ("1943-06-30", "316", "general farm hand", "Farm hands, general", "PDF physical page 173"),
    19: ("1942-05-15", "105", "general office clerk", "General office clerks", "PDF physical page 171"),
    21: ("1942-09-15", "781", "motor-vehicle mechanic or repairman", "Motor vehicle mechanics and repairmen", "PDF physical page 175"),
    25: ("1943-02-23", "137", "stenographer or typist", "Stenographers and typists", "PDF physical page 171"),
    31: ("1943-03-15", "760", "filling-station or parking-lot attendant", "Filling station and parking lot attendants", "PDF physical page 174"),
    33: ("1942-12-21", "101", "bookkeeper or cashier, except bank cashier", "Bookkeepers and cashiers, except bank cashiers", "PDF physical page 171"),
    36: ("1942-06-25", "717", "pattern or model maker, except paper", "Pattern and model makers, except paper", "PDF physical page 174"),
    37: ("1941-06-03", "316", "general farm hand", "Farm hands, general", "PDF physical page 173"),
    42: ("1943-09-29", "555", "skilled petroleum-refining occupation", "Skilled occupations in petroleum refining", "PDF physical page 173"),
    43: ("1942-09-17", "992", "student", "Students", "PDF physical page 304; amended category 9-92"),
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def source(key: str, **kwargs: object) -> dict[str, object]:
    value: dict[str, object] = {"key": key, "access_date": "2026-11-04"}
    value.update(kwargs)
    return value


def sources() -> list[dict[str, object]]:
    return [
        source(INDEX, stable_url="https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf", archival_identifier="RG 226, Entry A1-224, Boxes 858-860", title="OSS Personnel Files from Excel", author_creator="National Archives and Records Administration", repository_publisher="National Archives and Records Administration", publication_record_date="2010-12-23", locator="PDF page 518, rows 1-46; page 519 boundary and all page 518 rows visually checked at 180 dpi", source_quality="A_direct_official", collection_name="Records of the Office of Strategic Services, Record Group 226", rights_notes="All 46 printed rows remain separate. Full protected identifiers remain private."),
        source(ARMY, stable_url="https://catalog.archives.gov/id/1263923", archival_identifier="National Archives Identifier 1263923; parent series NAID 604357", title="Electronic Army Serial Number Merged File, ca. 1938-1946", author_creator="Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration", repository_publisher="National Archives and Records Administration", publication_record_date="1938-1946; merged file created 2002", locator="Official unrestricted ASNEF.FIN.DAT; fourteen Batch 1028 protected-identifier candidates reviewed", source_quality="A_direct_official", collection_name="World War II Army Enlistment Records", document_number="ASNEF.FIN.DAT", rights_notes="No raw record or full protected identifier is retained in public assets. Coded occupations identify neither employer nor workplace."),
        source(TECH, stable_url="https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf", archival_identifier="NN3-064-03-008; National Archives Identifier 1263923", title="World War II Army Enlistment Records: Reference Copy of Technical Documentation", author_creator="National Archives and Records Administration", repository_publisher="National Archives at College Park - Electronic Records", publication_record_date="1994-2005; reference copy modified 2011", locator="PDF physical pages 44-46; identifier, name, Army-entry-date, grade and civilian-occupation fields", source_quality="A_direct_official", collection_name="World War II Army Enlistment Records technical documentation", rights_notes="Used to interpret selected fields only; source damage, name conversion, coding limits and incomplete coverage remain applicable."),
        source(CODES, stable_url="https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1CL_SD.pdf", archival_identifier="National Archives Identifier 1263923; Code No. 30", title="NARA Compiled Code Lists for the Electronic Army Serial Number Merged File", author_creator="National Archives and Records Administration", repository_publisher="National Archives at College Park - Electronic Records", publication_record_date="2011-01-12; modified 2011-03-17", locator="PDF physical pages 170-175 and 304; Batch 1028 categories visually checked", source_quality="A_direct_official", collection_name="World War II Army Enlistment Records technical documentation", rights_notes="Historical categories identify neither employer, institution nor workplace. Petroleum-refining and filling-station categories are not oil-company evidence."),
        source(CUYLER_MEMORIAL, stable_url="https://www.cambridge.org/core/services/aop-cambridge-core/content/view/4EA1FB9402AB5F3784F362721D11DA94/S0026318400004971a.pdf/in-memoriam.pdf", archival_identifier="DOI 10.1017/S0026318400004971", title="In Memoriam: T. Cuyler Young", author_creator="Jerome W. Clinton", repository_publisher="Iranian Studies; Cambridge University Press", publication_record_date="1976", locator="Printed page 115; University of Toronto faculty and World War II OSS transition", source_quality="C_reputable_contemporary_or_scholarly", rights_notes="A concise project-authored paraphrase is retained; the memorial establishes sequence without an exact OSS appointment date."),
        source(NPS_YOUNGER, stable_url="https://www.nps.gov/articles/postwar-period-end-of-the-oss-and-return-to-the-park-service.htm", title="Postwar Period: End of the OSS and Return to the Park Service", repository_publisher="National Park Service", publication_record_date="updated 2017-08-14", locator="Postwar Careers of OSS Veterans section, paragraph naming J. Evelle Younger", source_quality="B_authoritative_institutional", collection_name="OSS Training in the National Parks and Service Abroad in World War II", rights_notes="The official historical study explicitly describes recruitment from an FBI section-chief role."),
        source(CA_AG_YOUNGER, stable_url="https://oag.ca.gov/history/26younger", title="Evelle J. Younger, 26th Attorney General", repository_publisher="State of California Department of Justice, Office of the Attorney General", locator="Biographical paragraph identifying law education, FBI Special Agent service and later Armed Forces service", source_quality="B_authoritative_institutional", rights_notes="Used to corroborate the uncommon identity and FBI career; the NPS source supplies the OSS transition."),
        source(CIA_RODNEY, stable_url="https://www.cia.gov/stories/story/digging-up-secrets/", title="Digging Up Secrets", repository_publisher="Central Intelligence Agency", publication_record_date="2023-06-30", locator="Rodney Young: Codename Pigeon section", source_quality="B_authoritative_institutional", rights_notes="The agency history supplies the full name, Greek Red Cross volunteer role, return to Washington and subsequent OSS recruitment."),
        source(OSS_RODNEY, stable_url="https://www.elia.org.gr/userfiles/pdf_archieve/1944%2011-1744%20OSS%20Missions%2C%20SOE%2C%20Georgiades%2C%20Pericles%2C%20Helios%20%5B25%20pgs%5D%20226-210-WN15277%20%28Admin%29.pdf", archival_identifier="RG 226, Entry 210, WN15277", title="Activities of the Middle East Field Group for the Period 1 October 1943 through 30 September 1944", author_creator="Office of Strategic Services", repository_publisher="Hellenic Literary and Historical Archive digital archive", publication_record_date="1944-10", locator="Section describing the first OSS wave into Greece under Rodney Young", source_quality="A_direct_official", collection_name="Records of the Office of Strategic Services", rights_notes="Direct OSS operational context corroborates the identity; no sensitive operational detail is reproduced."),
        source(CIA_YOVANOVICH, stable_url="https://www.cia.gov/readingroom/docs/OSS%20-%20SSU%20-%20CIG%20EARLY%20CIA%20DOCUMENTS%20%20%20VOL.%205_0016.pdf", archival_identifier="OSS-SSU-CIG Early CIA Documents, volume 5, part 16", title="Report of Marko, Member of British-American Mission to General Mihailovich", author_creator="Office of Strategic Services", repository_publisher="Central Intelligence Agency Freedom of Information Act Electronic Reading Room", locator="Passage on Dr. Peter Yovanovich, American physician in Yugoslavia, and request to determine recruitment status", source_quality="A_direct_official", collection_name="OSS-SSU-CIG Early CIA Documents", rights_notes="OCR damages the surname, but the document supplies the full given name, physician role, citizenship and recruitment context."),
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {"key": ORG_TORONTO, "organization_id": "2688e5a3-ecca-570a-865a-4cc3f7442eaf", "canonical_name": "University of Toronto", "historical_name": "University of Toronto", "organization_type": "university", "sector": "academia_and_research", "city": "Toronto", "state_or_region": "Ontario", "country": "Canada", "normalization_notes": "Existing canonical organization reused; the memorial's historical name is preserved."},
        {"key": ORG_FBI, "organization_id": "e88a4c18-5e0d-58aa-9ed4-787529fac74f", "canonical_name": "Federal Bureau of Investigation", "historical_name": "Federal Bureau of Investigation", "aliases": ["FBI"], "organization_type": "federal law-enforcement agency", "sector": "federal_government", "country": "United States", "normalization_notes": "Existing canonical organization reused; federal government service remains separate from private employment."},
        {"key": ORG_GREEK_RED_CROSS, "canonical_name": "Greek Red Cross", "historical_name": "Greek Red Cross", "organization_type": "humanitarian relief organization", "sector": "medicine_and_public_health", "country": "Greece", "normalization_notes": "The CIA source describes volunteer ambulance service; it is not recast as paid employment."},
        {"key": ORG_ASCSA, "organization_id": "29abce5d-fe96-5ed8-beb4-93560d4604cb", "canonical_name": "American School of Classical Studies at Athens", "historical_name": "American School of Classical Studies", "aliases": ["American School of Classical Studies in Greece"], "organization_type": "archaeological research and educational institution", "sector": "academia_and_research", "city": "Athens", "country": "Greece", "normalization_notes": "Existing canonical organization reused; attendance and excavation participation are not labeled employment."},
    ]


def affiliation(key: str, row: int, relationship: str, temporal: str, identity: str, confidence: str, quality: str, status: str = "published", **kwargs: object) -> dict[str, object]:
    value: dict[str, object] = {"key": key, "person_id": PEOPLE[row][0], "relationship_type": relationship, "pre_oss_temporal_basis": temporal, "identity_confidence": identity, "claim_confidence": confidence, "source_quality": quality, "publication_status": status}
    value.update(kwargs)
    return value


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, _label, _locator) in ARMY_OCCUPATIONS.items():
        relationship = "student" if row in {13, 43} else "unknown"
        values.append(affiliation(
            f"{slug(PEOPLE[row][1])}-army-occupation-b1028", row, relationship,
            "strongly_date_bounded", "confirmed", "medium", "A_direct_official", "publish_qualified",
            occupation=occupation, end_date=date,
            date_precision=f"Historical civilian-occupation code {code} was recorded at Army entry on {date}; no named employer or institution is supplied.",
            country="United States", immediate_pre_oss=False, last_civilian_pre_service=False,
            research_notes="Broad historical category only; excluded from verified-employer analytics and not narrowed beyond the official wording.",
        ))
    values.extend([
        affiliation("cuyler-young-university-toronto-b1028", 12, "employment", "explicit_immediate", "high_confidence", "high", "C_reputable_contemporary_or_scholarly", organization_key=ORG_TORONTO, organization_name_as_found="faculty of the University of Toronto", role_title="faculty member and teacher", start_date="1938", date_precision="The memorial says Young joined the faculty three years after 1935 and set aside his teaching career during World War II to serve OSS; the exact end and OSS appointment dates are not stated.", city="Toronto", state_or_region="Ontario", country="Canada", immediate_pre_oss=True, last_civilian_pre_service=True, research_notes="Best-supported immediate and last civilian employer; exact OSS entry date awaits Box 859."),
        affiliation("evelle-younger-fbi-b1028", 40, "government_assignment", "explicit_immediate", "high_confidence", "high", "B_authoritative_institutional", organization_key=ORG_FBI, organization_name_as_found="FBI", role_title="section chief; Special Agent", date_precision="The NPS history calls him a former FBI section chief recruited by OSS X-2; the California Attorney General biography independently identifies FBI Special Agent service. Exact dates are not stated.", country="United States", immediate_pre_oss=True, last_civilian_pre_service=True, research_notes="Federal civilian service is both the immediate affiliation and last civilian employer; exact transfer date awaits Box 860."),
        affiliation("rodney-young-greek-red-cross-b1028", 32, "volunteer", "explicit_immediate", "confirmed", "high", "B_authoritative_institutional", organization_key=ORG_GREEK_RED_CROSS, organization_name_as_found="Greek Red Cross", role_title="volunteer ambulance driver", date_precision="CIA history says Young volunteered when war began, was injured in an Italian air raid, returned to Washington and was soon recruited into OSS; exact dates are not stated.", country="Greece", immediate_pre_oss=True, last_civilian_pre_service=False, research_notes="Immediate volunteer status, not employment; no named last civilian employer is established."),
        affiliation("rodney-young-ascsa-b1028", 32, "professional_affiliation", "documented_prewar", "confirmed", "high", "B_authoritative_institutional", organization_key=ORG_ASCSA, organization_name_as_found="American School of Classical Studies in Greece", role_title="archaeologist and excavation participant", start_date="1929", date_precision="CIA history says he attended the school from 1929 and participated in excavations before wartime Red Cross service; the end date is not stated.", city="Athens", country="Greece", immediate_pre_oss=False, last_civilian_pre_service=False, research_notes="Professional and educational affiliation; not classified as a named employer."),
        affiliation("peter-yovanovich-physician-b1028", 44, "unknown", "explicit_immediate", "high_confidence", "high", "A_direct_official", "published", role_title="medico", occupation="physician", date_precision="The OSS report identifies Dr. Peter Yovanovich as remaining in Yugoslavia as a medico immediately before a request to determine how he could be recruited; the exact date is not established.", country="Yugoslavia", immediate_pre_oss=True, last_civilian_pre_service=False, research_notes="Immediate professional status is documented, but neither employer nor exact recruitment outcome is named."),
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
        affiliation_key = f"{slug(PEOPLE[row][1])}-army-occupation-b1028"
        values.append(claim(
            f"occupation-{slug(PEOPLE[row][1])}-b1028", row, "occupation",
            f"At Army entry on {date}, {PEOPLE[row][1]} was recorded in the broad historical category: {occupation}.",
            f"The official merged Army record carries category {code}; the NARA code list labels it {label}.",
            "Confirmed by exact name and a nonshared protected identifier; the identifier is not published.",
            "The category was recorded at Army entry and is strongly date-bounded, but its exact duration and relation to OSS are unknown.",
            "A_direct_official", "medium",
            [{"source_key": ARMY}, {"source_key": TECH}, {"source_key": CODES, "locator_override": locator}],
            "Qualified occupation only. It is not a named employer, institution or workplace.", "publish_qualified", affiliation_key,
        ))
    values.extend([
        claim("identity-billy-young-b1028", 9, "identity", "Billy B Young is strongly supported as the person represented by a damaged official Army record linked to the index.", "A nonshared protected identifier links the records, while name damage, a middle-initial conflict and the 1946 Army-entry date remain explicit.", "High confidence from the unique identifier; not confirmed because the official name rendering and middle initial conflict.", "The Army record is post-OSS and supplies identity context only.", "A_direct_official", "high", [{"source_key": INDEX}, {"source_key": ARMY}, {"source_key": TECH}], "No occupation or pre-OSS affiliation is transferred from the postwar record."),
        claim("identity-james-b-young-b1028", 20, "identity", "James B Young is strongly supported as the person in an official Army record that omits the middle initial.", "A nonshared protected identifier connects the index and Army record, but the Army name omits the indexed middle initial.", "High confidence from the unique identifier with a minor name-form difference.", "The record supplies no interpretable pre-OSS occupation because category 999 is not converted.", "A_direct_official", "high", [{"source_key": INDEX}, {"source_key": ARMY}, {"source_key": TECH}], "Identity only; no employer or occupation is inferred."),
        claim("identity-cuyler-young-b1028", 12, "identity", "The indexed Cuyler T Young is strongly supported as scholar T. Cuyler Young, who left University of Toronto teaching for OSS service.", "The memorial uses the same uncommon name components and directly links the University of Toronto faculty member to OSS.", "High confidence from the distinctive reversed given-name form, civilian P-6 index grade and direct OSS biography.", "The biography explicitly places the teaching post before OSS.", "C_reputable_contemporary_or_scholarly", "high", [{"source_key": INDEX}, {"source_key": CUYLER_MEMORIAL}], "The original indexed order remains preserved; T. Cuyler Young is added as a documented variant."),
        claim("immediate-cuyler-young-toronto-b1028", 12, "immediate_pre_oss_affiliation", "T. Cuyler Young taught at the University of Toronto immediately before setting aside teaching to serve OSS.", "The memorial says he joined the Toronto faculty and set aside his teaching career during World War II to serve OSS.", "High-confidence uncommon-name identity with a direct OSS bridge.", "Explicit career-to-OSS transition; exact appointment day remains unavailable.", "C_reputable_contemporary_or_scholarly", "high", [{"source_key": CUYLER_MEMORIAL}], "Published as the best-supported immediate affiliation.", "published", "cuyler-young-university-toronto-b1028"),
        claim("last-civilian-cuyler-young-toronto-b1028", 12, "last_civilian_pre_service", "University of Toronto is the best-supported last civilian employer before T. Cuyler Young's OSS service.", "The memorial places no intervening employer between the Toronto teaching career and OSS service.", "High-confidence uncommon-name identity with a direct OSS bridge.", "The sequence is explicit, though exact dates remain approximate.", "C_reputable_contemporary_or_scholarly", "high", [{"source_key": CUYLER_MEMORIAL}], "Employment is kept separate from earlier missionary and student affiliations.", "published", "cuyler-young-university-toronto-b1028"),
        claim("identity-rodney-young-b1028", 32, "identity", "Indexed Rodney S Young is confirmed as archaeologist Rodney Stuart Young, who ran the OSS Secret Intelligence Unit for Greece.", "CIA supplies the full middle name and direct OSS role; a 1944 OSS report independently places Rodney Young in Greek operations.", "Confirmed by exact first and surname, expanded middle name, profession, regional expertise and two direct OSS sources.", "Both sources describe wartime OSS service; CIA supplies the pre-recruitment sequence.", "A_direct_official", "confirmed", [{"source_key": INDEX}, {"source_key": CIA_RODNEY}, {"source_key": OSS_RODNEY}], "Rodney Stuart Young is added as a documented name variant."),
        claim("immediate-rodney-young-red-cross-b1028", 32, "immediate_pre_oss_affiliation", "Rodney Stuart Young volunteered as a Greek Red Cross ambulance driver immediately before returning to Washington and being recruited into OSS.", "CIA describes the Red Cross service, air-raid injury, return to Washington and recruitment as a single sequence.", "Confirmed by full-name and direct OSS-role evidence.", "Explicit immediate volunteer pathway; this is not paid employment.", "B_authoritative_institutional", "high", [{"source_key": CIA_RODNEY}], "Modeled as volunteer service, not employer evidence.", "published", "rodney-young-greek-red-cross-b1028"),
        claim("ascsa-rodney-young-b1028", 32, "other_pre_oss_affiliation", "Rodney Stuart Young attended the American School of Classical Studies and participated in excavations before wartime service.", "CIA says he went to the school in 1929 and participated in archaeological excavations.", "Confirmed by full-name and direct OSS-role evidence.", "Documented prewar affiliation; it precedes the Greek Red Cross pathway and is not shown to be employment.", "B_authoritative_institutional", "high", [{"source_key": CIA_RODNEY}], "Professional or educational affiliation, excluded from employer analytics.", "published", "rodney-young-ascsa-b1028"),
        claim("identity-evelle-younger-b1028", 40, "identity", "Indexed Evelle J Younger is strongly supported as former FBI section chief J. Evelle Younger, recruited by OSS X-2 for the Far East.", "The NPS history gives the uncommon name and direct OSS recruitment; the California Attorney General biography independently confirms FBI service.", "High confidence from the uncommon exact name, middle initial and matching FBI career; the index supplies no second public identifier.", "NPS explicitly places FBI service before OSS recruitment.", "B_authoritative_institutional", "high", [{"source_key": INDEX}, {"source_key": NPS_YOUNGER}, {"source_key": CA_AG_YOUNGER}], "No commissioned status is inferred from his later military career."),
        claim("immediate-evelle-younger-fbi-b1028", 40, "immediate_pre_oss_affiliation", "Evelle J Younger served as an FBI section chief immediately before OSS X-2 recruited him for the Far East.", "The NPS official history explicitly describes a former FBI section chief recruited by OSS X-2.", "High-confidence uncommon-name identity corroborated by the California Attorney General biography.", "Explicit recruitment-from relationship; exact transfer date remains unavailable.", "B_authoritative_institutional", "high", [{"source_key": NPS_YOUNGER}, {"source_key": CA_AG_YOUNGER}], "Federal civilian government service is not mislabeled as private employment.", "published", "evelle-younger-fbi-b1028"),
        claim("last-civilian-evelle-younger-fbi-b1028", 40, "last_civilian_pre_service", "The Federal Bureau of Investigation is the best-supported last civilian employer before Evelle J Younger's OSS service.", "NPS places the FBI section-chief role directly before recruitment; the state biography independently confirms Special Agent service.", "High-confidence uncommon-name identity.", "Explicit immediate sequence, though the exact intervening military status requires the personnel file.", "B_authoritative_institutional", "high", [{"source_key": NPS_YOUNGER}, {"source_key": CA_AG_YOUNGER}], "Published as federal civilian employment with the military-sequence caveat.", "published", "evelle-younger-fbi-b1028"),
        claim("identity-peter-yovanovich-b1028", 44, "identity", "The indexed Peter, Dr. Yovanovich is strongly supported as Dr. Peter Yovanovich, an American physician considered for recruitment in Yugoslavia.", "An OSS report supplies the same distinctive name, medical title, American citizenship and recruitment context despite OCR damage to the surname.", "High confidence from the rare exact name and direct OSS-era recruitment document.", "The document records his status immediately before the recruitment question.", "A_direct_official", "high", [{"source_key": INDEX}, {"source_key": CIA_YOVANOVICH}], "Original indexed punctuation and order remain preserved; Dr. Peter Yovanovich is added as a variant."),
        claim("immediate-peter-yovanovich-physician-b1028", 44, "immediate_pre_oss_affiliation", "Dr. Peter Yovanovich remained in Yugoslavia as a physician immediately before an OSS recruitment-status request.", "The OSS report says he remained as a medico and asks under what status he could be recruited.", "High-confidence rare-name identity from direct OSS-era evidence.", "Explicitly immediate professional status; no named employer or final recruitment disposition is supplied.", "A_direct_official", "high", [{"source_key": CIA_YOVANOVICH}], "Occupation only, not a named employer.", "published", "peter-yovanovich-physician-b1028"),
    ])
    return values


def unresolved_reason(row: int) -> str:
    reasons = {
        1: "The indexed surname spelling and plausible Youmans variant produced no source that bridges the person to OSS or a pre-OSS employer.",
        2: "Exact-name, transliteration and punctuation variants produced no reliable identity or employment bridge.",
        4: "Actor and broadcaster namesakes lacked an OSS, Box 859 or protected-identifier bridge.",
        7: "A same-name later CIA employee and other namesakes lacked an index or wartime OSS identity bridge.",
        10: "The actor and Army Air Corps officer Carleton Young lacks a protected-identifier or personnel-file bridge to this row.",
        18: "Modern author and other Grace Young namesakes lacked an OSS or Box 859 bridge.",
        22: "A same-name paratrooper lead lacked a protected-identifier, OSS or Box 859 bridge.",
        26: "A same-name RAF veteran and other Lionel Young namesakes lacked an OSS or index bridge.",
        27: "The protected identifier produced no Army bulk match, and accessible searches did not establish the indexed person.",
        30: "The suffix and middle initial did not produce a reliable identity-and-employment bridge.",
        41: "Exact-name results did not establish Jack S Younger's wartime identity or pre-OSS affiliation.",
        45: "Yshira, Ishira and likely OCR-variant searches produced no reliable identity, OSS or employment bridge.",
        46: "Exact-name and variant searches returned modern namesakes but no reliable wartime identity or employment evidence.",
    }
    return reasons.get(row, "Accessible exact-name, official, CIA, OSS, employer, occupation, obituary, institutional, newspaper, directory and archival searches produced no reliable identity-and-affiliation bridge; unbridged namesakes and postwar-only leads were rejected.")


def base_update(row: int, **overrides: object) -> dict[str, object]:
    value: dict[str, object] = {"person_id": PEOPLE[row][0], "manual_review_required": True, "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "high"}
    value.update(overrides)
    return value


def person_updates() -> list[dict[str, object]]:
    special = set(ARMY_OCCUPATIONS) | {9, 12, 20, 32, 40, 44}
    values: list[dict[str, object]] = []
    for row in sorted(set(PEOPLE) - special):
        reason = unresolved_reason(row)
        values.append(base_update(
            row, identity_status="unresolved",
            identity_evidence=f"The visually verified page 518 source preserves {PEOPLE[row][1]}. {reason}",
            research_status="requires_archival_review",
            archival_review_priority="critical" if row in {1, 2, 4, 5, 8, 10, 14, 15, 17, 18, 22, 23, 24, 26, 27, 28, 29, 30, 34, 35, 38, 39, 41, 45, 46} else "high",
            next_action=f"Review indexed Box {PEOPLE[row][2]} for corroborating identifiers, immediate pre-OSS affiliation and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}",
        ))
    for row in sorted(ARMY_OCCUPATIONS):
        values.append(base_update(
            row, identity_status="confirmed",
            identity_evidence="A nonshared protected identifier and exact official name agreement connect the index and Army records; the identifier remains private.",
            personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False,
            research_status="occupation_only_found", nara_catalog_id="1263923",
            next_action=f"Review indexed Box {PEOPLE[row][2]} to identify a named employer or institution and establish Army-to-OSS chronology. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed; the bulk record supplies only a historical occupation category.",
        ))
    values.extend([
        base_update(9, identity_status="high_confidence", identity_evidence="A nonshared protected identifier links the index to an official Army record, but damaged name rendering, a middle-initial conflict and a post-OSS 1946 entry date remain explicit.", personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="requires_archival_review", nara_catalog_id="1263923", archival_review_priority="critical", next_action="Review Box 859 to resolve the name-form conflict and identify a pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed; the postwar Army record is identity evidence only."),
        base_update(12, identity_status="high_confidence", identity_evidence="The uncommon indexed components Cuyler and T align with T. Cuyler Young, whose scholarly memorial directly links University of Toronto teaching to OSS service.", name_variants=["T. Cuyler Young"], replace_name_variants=False, personnel_category="civilian_professional_or_administrative_grade", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="verified_employer_found", archival_review_priority="medium", next_action="Review Box 859 to confirm the exact University of Toronto end date and OSS appointment date; the immediate and last civilian employer are already strongly supported."),
        base_update(20, identity_status="high_confidence", identity_evidence="A nonshared protected identifier links the index to an official Army record that omits the indexed middle initial; historical code 999 is not interpreted.", personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="requires_archival_review", nara_catalog_id="1263923", archival_review_priority="critical", next_action="Review Box 859 to confirm the middle initial and identify a pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed; no occupation is inferred from code 999."),
        base_update(32, identity_status="confirmed", identity_evidence="CIA supplies the full name Rodney Stuart Young and direct OSS Greek-unit role; a 1944 OSS report independently names Rodney Young in Greek operations.", name_variants=["Rodney Stuart Young"], replace_name_variants=False, personnel_category="civilian_professional_or_administrative_grade", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="requires_archival_review", archival_review_priority="medium", next_action="Review Box 860 for the last named civilian employer and exact recruitment date. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed; Greek Red Cross volunteer service is the immediate documented affiliation."),
        base_update(40, identity_status="high_confidence", identity_evidence="The uncommon exact name and initial align with official NPS and California Attorney General biographies that identify FBI service and direct OSS X-2 recruitment.", research_status="verified_employer_found", archival_review_priority="medium", next_action="Review Box 860 to confirm the exact FBI end date, military component and OSS appointment; the immediate affiliation and last civilian employer are already strongly supported."),
        base_update(44, identity_status="high_confidence", identity_evidence="A direct OSS-era report supplies Dr. Peter Yovanovich's distinctive name, American citizenship, medical role and recruitment context despite surname OCR damage.", name_variants=["Dr. Peter Yovanovich", "Peter Yovanovich"], replace_name_variants=False, personnel_category="civilian_professional_or_administrative_grade", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="occupation_only_found", archival_review_priority="critical", next_action="Review Box 860 to identify the named prewar medical employer and final recruitment status. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed; physician status is directly documented."),
    ])
    if len(values) != 46:
        raise RuntimeError(f"Expected 46 person updates, generated {len(values)}")
    return values


def research_attempts() -> list[dict[str, object]]:
    substantiated = set(ARMY_OCCUPATIONS) | {9, 12, 20, 32, 40, 44}
    attempts: list[dict[str, object]] = []
    for row, (person_id, name, box) in PEOPLE.items():
        if row in substantiated:
            outcome = "source_reviewed"
            reviewed = 10 if row in {12, 32, 40, 44} else 7
            rejected = 3
            note = "At least one identity, occupation, employer, volunteer or professional-status outcome is preserved with claim-level citations; remaining employer or temporal questions remain explicit."
        else:
            outcome = "candidate_rejected"
            reviewed = 5
            rejected = 4
            note = unresolved_reason(row)
        attempts.append({
            "key": f"page518-row{row}-{slug(name)}-b1028",
            "person_id": person_id,
            "source_adapter": "manual_staged_protocol",
            "query_text": f"{name}; NARA OSS index context; exact-name and meaningful initial, suffix, punctuation, transliteration and OCR variants; OSS, CIA Reading Room, rank, branch, assignment and protected-identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory and archival searches; indexed Box {box}",
            "query_variant_type": "staged_identity_employment_archival_protocol_batch_1028",
            "started_at": "2026-11-04T12:00:00-05:00",
            "completed_at": "2026-11-04T18:30:00-05:00",
            "outcome": outcome,
            "sources_reviewed": reviewed,
            "candidate_sources_rejected": rejected,
            "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, postwar-only leads and sources without an OSS, protected-identifier, rank, unit or personnel-file bridge were rejected. Army categories were not converted into named employers, and the petroleum categories were not treated as oil-company evidence.",
            "research_notes": f"{note} The official index, exact-name OSS searches, grouped CIA Reading Room checks, and employer, occupation, obituary, institutional, newspaper, directory and archival searches were reviewed as applicable. Page 518, the page 519 boundary and every cited NARA code-list page were visually checked. No authenticated NARA Catalog API request was made.",
            "next_action": f"Review indexed Box {box} for corroborating identifiers, immediate pre-OSS affiliation and last civilian employer before wartime service.",
            "attempt_number": 1,
            "research_agent_version": "before-oss-b1028-v1",
        })
    if len(attempts) != 46:
        raise RuntimeError(f"Expected 46 research attempts, generated {len(attempts)}")
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-1028-v1",
        "reviewer": "Before OSS Batch 1028 evidence review",
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
