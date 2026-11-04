#!/usr/bin/env python3
"""Generate the reviewed Batch 1029 evidence bundle for PDF page 519."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page519-francis-yuhashi-to-joseph-zbeig-review_"
    "batch-1029_2026-11-04.json"
)

INDEX = "nara-index-b1029"
ARMY = "army-bulk-b1029"
TECH = "army-tech-b1029"
CODES = "army-codes-b1029"
ZAGORIA_OBIT = "sinai-zagoria-b1029"
ZAGIER_BOOK = "halban-zagier-b1029"
ZAGIER_NARA = "nara-zagier-ssu-b1029"
PROJECT_EAGLE = "micgiel-project-eagle-b1029"
LA_DIRECTORY = "la-planning-zaikowsky-b1029"
ARMY_REGISTER = "nara-army-register-zarembo-b1029"
NPS_ZAREMBO = "nps-zarembo-b1029"
NSA_ZARET = "nsa-zaret-b1029"
NH_GUARD = "nh-national-guard-zarkadas-b1029"
IRRIGATOR = "densho-zarubica-b1029"
DDPA_ZARFOSS = "ddpa-zarfoss-b1029"
OSSOG = "ossog-roster-b1029"
USWM_ZAPHIRIS = "uswm-zaphiris-b1029"

ORG_BROOKLYN = "brooklyn-college-b1029"
ORG_GERMAN_ARMY = "german-army-b1029"
ORG_USMA = "usma-b1029"
ORG_QMC = "army-quartermaster-b1029"
ORG_LINCOLN = "lincoln-brigade-b1029"
ORG_NH_GUARD = "nh-guard-172fa-b1029"
ORG_MINIDOKA = "minidoka-relocation-center-b1029"

PEOPLE = {
    1: ("96c96581-0b4e-51f0-a317-9b4ca1f16749", "Francis S Yuhashi", "860"),
    2: ("24377fa3-e485-5af8-89fc-1ff250166f9e", "Albert A Yurko", "860"),
    3: ("4d9f33c3-aedc-5902-ab6b-94e94b9e094a", "Frank V Zabatta", "860"),
    4: ("c7d52a69-36e8-5ff0-9809-17f26a82ca10", "Charles A Zabel", "860"),
    5: ("3da8c5be-fcff-516a-913a-64852ddc0d7b", "Dante T Zaccanini", "860"),
    6: ("2dda7ed3-23b0-59c3-b286-ddac28e13dc9", "Walter A Zach", "860"),
    7: ("f3e211f9-6003-57d5-b568-62fe962e7ed0", "George E Zachariades", "860"),
    8: ("da3b4e77-7caf-5691-84a8-b821eaf42646", "Heinz Zacharian", "860"),
    9: ("4f623bf9-f400-5866-88a3-394bca69152c", "Bernard A Zachmann", "860"),
    10: ("da2f9a29-00f7-5fe5-b7d4-08e69d39087f", "David D Zagier", "860"),
    11: ("d71b8b07-7f93-507d-8942-6ddfbfd27549", "Sylvia B Zagoria", "860"),
    12: ("b1d8132b-5d0d-5df2-90b1-ca768fd3defc", "Wilhelm Zagorski", "860"),
    13: ("28731009-1509-598a-aef3-741efd736443", "Nicholas G Zahardis", "860"),
    14: ("a576f303-7153-5afa-b08b-9f31c16677e7", "Constantine Zahariades", "860"),
    15: ("440f52da-44e6-5029-967b-78b3adbb91d9", "Dim V Zaikowsky", "860"),
    16: ("2e280f11-b880-5663-97eb-b2a88a3480ac", "Edward Zajac", "860"),
    17: ("488d8b89-3a4f-53d8-8b6f-571bba8fed04", "Bill C Zajdel", "860"),
    18: ("47cb425c-832f-507e-9099-4b27c115930c", "William A Zajic", "860"),
    19: ("e0647019-19ad-5171-bfd7-d7fd99940350", "David L Zakon", "860"),
    20: ("61a65d0e-8fe2-54d4-a0a1-6ef6f42be113", "David L Zakon", "860"),
    21: ("958b4c6f-56d8-5030-855d-fa2a7ebc9c64", "Nick Zakos", "860"),
    22: ("9cbd5e93-5c80-5bf1-a9e3-1d12a60fccb7", "Doris Adele Zalkind", "860"),
    23: ("cf23b87a-a754-50fd-81fb-806d3d228ec3", "Tehodore F Zaloga", "861"),
    24: ("3bf3a9de-d451-5851-8661-8f585b0467d5", "Louis J Zammarcella", "861"),
    25: ("93117a98-43b9-52e3-9d11-6589abc37423", "Bruno G Zamparo", "861"),
    26: ("8b35412c-7d7d-5b98-9a49-9a0d8ea8de1c", "Mario Zamparo", "861"),
    27: ("d3cbb295-eab8-50d8-976f-216fd5f1cc61", "Anthony F Zanardi", "861"),
    28: ("6c0266ab-c481-50ad-918d-e312c60157ef", "Henry G Zander", "861"),
    29: ("4f125d6b-f723-5ca7-9134-9880df8cd8a6", "Ladimer J Zanski", "861"),
    30: ("de74c158-a05f-5d95-b848-fa2540457239", "Peter H Zapantes", "861"),
    31: ("9ccf7a62-a7da-5bec-8ed9-ee707c7601aa", "Emauel N Zaphiris", "861"),
    32: ("f8f79f38-29b7-532c-a305-b1af7d59d790", "George Zappin", "861"),
    33: ("19706e46-7ad4-5119-b731-2e044fb675e3", "Henry A Zarbo", "861"),
    34: ("1cf63a7e-fb32-5eaf-9e21-e4cf3cf1782f", "Jerome Zarcone", "861"),
    35: ("3e83394b-b3bd-59b3-9e90-9d2c6c36cb23", "Edward B Zarembo", "861"),
    36: ("53c254f1-9051-549f-af5e-5c8e8a368804", "John A Zarembski", "861"),
    37: ("137d7de3-00cf-5560-891d-b6e6ef238c03", "Daniel A Zaret", "861"),
    38: ("14ba6973-e21e-5a50-a112-4f7fc76dabb3", "Gweneth Zarfoss", "861"),
    39: ("182217fd-87f2-5ba1-a581-6a4e067956d6", "Archie C Zarkadas", "861"),
    40: ("1db68209-4e9a-5d37-bec6-4f9c826ef982", "Paul J Zarras", "861"),
    41: ("0e1b0b0d-1ebc-5470-aca9-796cab193bbb", "Milovan R Zarubica", "861"),
    42: ("fd0289fd-737e-5a13-8927-a866ac1f4286", "Cora V Zaser", "861"),
    43: ("9f0e97f7-6707-5833-a97a-3c357192915b", "Asa Zatz", "861"),
    44: ("b5849a8b-5c38-5592-8b11-90b84cf5487c", "Peter C Zavalis", "861"),
    45: ("048cd3a2-794e-58d5-877b-ab0b2be0aeb1", "Marie E Zavitosky", "861"),
    46: ("ba9ad024-a5b5-595a-b5bb-81305902bd5a", "Joseph S Zbeig", "861"),
}

ARMY_OCCUPATIONS = {
    1: ("1941-07-15", "387", "fisherman or oysterman", "Fishermen and oystermen", "PDF physical page 173"),
    2: ("1942-12-09", "314", "dairy farm hand", "Farm hands, dairy", "PDF physical page 173"),
    5: ("1942-11-05", "992", "student", "Students", "PDF physical page 304; amended category 9-92"),
    6: ("1942-09-15", "992", "student", "Students", "PDF physical page 304; amended category 9-92"),
    7: ("1942-09-28", "031", "secondary-school teacher or principal", "Teachers (secondary school) and principals", "PDF physical page 170"),
    9: ("1944-02-10", "072", "retail manager", "Managers, retail stores", "PDF physical page 171"),
    14: ("1943-06-08", "226", "cook, except private family", "Cooks, except private family", "PDF physical page 172"),
    16: ("1942-04-23", "227", "waiter or waitress, except private family", "Waiters and waitresses, except private family", "PDF physical page 172"),
    18: ("1941-05-23", "513", "skilled miscellaneous-products manufacturing occupation", "Skilled occupations in manufacture of miscellaneous products, n.e.c.", "PDF physical page 174"),
    19: ("1944-03-01", "061", "radio operator", "Radio operators", "PDF physical page 171"),
    28: ("1943-05-26", "992", "student", "Students", "PDF physical page 304; amended category 9-92"),
    30: ("1943-01-27", "227", "waiter or waitress, except private family", "Waiters and waitresses, except private family", "PDF physical page 172"),
    31: ("1941-06-21", "227", "waiter or waitress, except private family", "Waiters and waitresses, except private family", "PDF physical page 172"),
    32: ("1942-08-12", "072", "retail manager", "Managers, retail stores", "PDF physical page 171"),
    34: ("1942-04-13", "627", "textile-products fabrication occupation, not elsewhere classified", "Occupations in fabrication of textile products, n.e.c.", "PDF physical page 175"),
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def source(key: str, **kwargs: object) -> dict[str, object]:
    value: dict[str, object] = {"key": key, "access_date": "2026-11-04"}
    value.update(kwargs)
    return value


def sources() -> list[dict[str, object]]:
    return [
        source(INDEX, stable_url="https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf", archival_identifier="RG 226, Entry A1-224, Boxes 860-861", title="OSS Personnel Files from Excel", author_creator="National Archives and Records Administration", repository_publisher="National Archives and Records Administration", publication_record_date="2010-12-23", locator="PDF page 519, rows 1-46; page 520 boundary and all page 519 rows visually checked at 180 dpi", source_quality="A_direct_official", collection_name="Records of the Office of Strategic Services, Record Group 226", rights_notes="All 46 printed rows remain separate. Full protected identifiers remain private."),
        source(ARMY, stable_url="https://catalog.archives.gov/id/1263923", archival_identifier="National Archives Identifier 1263923; parent series NAID 604357", title="Electronic Army Serial Number Merged File, ca. 1938-1946", author_creator="Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration", repository_publisher="National Archives and Records Administration", publication_record_date="1938-1946; merged file created 2002", locator="Official unrestricted ASNEF.FIN.DAT; twenty-two Batch 1029 candidate links explicitly reviewed", source_quality="A_direct_official", collection_name="World War II Army Enlistment Records", document_number="ASNEF.FIN.DAT", rights_notes="No raw record or full protected identifier is retained in public assets. Shared and conflicting links remain explicit."),
        source(TECH, stable_url="https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf", archival_identifier="NN3-064-03-008; National Archives Identifier 1263923", title="World War II Army Enlistment Records: Reference Copy of Technical Documentation", author_creator="National Archives and Records Administration", repository_publisher="National Archives at College Park - Electronic Records", publication_record_date="1994-2005; reference copy modified 2011", locator="PDF physical pages 44-46; identifier, name, Army-entry-date, grade and civilian-occupation fields", source_quality="A_direct_official", collection_name="World War II Army Enlistment Records technical documentation", rights_notes="Used to interpret selected fields only; source damage, name conversion, coding limits and incomplete coverage remain applicable."),
        source(CODES, stable_url="https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1CL_SD.pdf", archival_identifier="National Archives Identifier 1263923; Code No. 30", title="NARA Compiled Code Lists for the Electronic Army Serial Number Merged File", author_creator="National Archives and Records Administration", repository_publisher="National Archives at College Park - Electronic Records", publication_record_date="2011-01-12; modified 2011-03-17", locator="PDF physical pages 170-175 and 304; Batch 1029 categories visually checked", source_quality="A_direct_official", collection_name="World War II Army Enlistment Records technical documentation", rights_notes="Historical categories identify neither employer, institution nor workplace. Undefined code 999 is not interpreted."),
        source(ZAGORIA_OBIT, stable_url="https://sinaimemorial.org/single-obituary/?id=e52af9f8-ff76-4018-974a-dbc241122102", title="Obituary: Sylvia Beatrice Zagoria", repository_publisher="Sinai Memorial Chapel", publication_record_date="2022", locator="Biographical paragraph on Brooklyn College graduation, wartime move to Washington and one year as an OSS analyst", source_quality="C_reputable_contemporary_or_scholarly", rights_notes="Family-supplied obituary. It supports a clear chronology but is not a personnel record; postwar jobs are not used as pre-OSS evidence."),
        source(ZAGIER_BOOK, stable_url="https://books.google.com/books/about/Botchki.html?id=RtEbDQAAQBAJ", title="Botchki", author_creator="David Zagier; publisher biography by Halban Publishers", repository_publisher="Halban Publishers; Google Books metadata display", publication_record_date="2016", locator="About the author section", source_quality="C_reputable_contemporary_or_scholarly", rights_notes="Publisher biography links journalism in South Africa, Paris and London to wartime OSS recruitment; no named newspaper is supplied."),
        source(ZAGIER_NARA, stable_url="https://www.archives.gov/files/research/holocaust/microfilm-publications/m1934-subject-list.pdf", archival_identifier="Microfilm Publication M1934", title="Subject Listing of Numbered Documents in M1934, OSS Washington Secret Intelligence/Special Funds Records, 1942-46", author_creator="National Archives and Records Administration", repository_publisher="National Archives and Records Administration", locator="Reel 17, document 0005685; FSRO, David D. Zagier", source_quality="A_direct_official", collection_name="OSS Washington Secret Intelligence/Special Funds Records", rights_notes="Corroborates the distinctive identity in successor SSU records; it does not establish the pre-OSS occupation."),
        source(PROJECT_EAGLE, stable_url="https://dokumen.pub/project-eagle-john-s-micgiel-ksika.html", archival_identifier="Cites NARA RG 226, Entry A1-224, Box 860; Entry 210, Box 5", title="Project Eagle: Polish Intelligence Officers in Reports and Wartime Documents of the Office of Strategic Services", author_creator="John S. Micgiel", repository_publisher="Universitas", publication_record_date="2019", locator="Printed pages 118-119, Wilhelm Zagórski biography and Daiquiri mission notes", source_quality="C_reputable_contemporary_or_scholarly", rights_notes="Scholarly source based on identified NARA records; spelling with the Polish diacritic is preserved as a documented variant."),
        source(LA_DIRECTORY, stable_url="https://planning.lacity.gov/eir/nops/5420Sunset/IS-5%20-%20Phase%20I%20ESA.pdf", title="Phase I Environmental Site Assessment: 5420, 5422 and 5450 Sunset Boulevard", author_creator="Laura Cattaneo; Russell M. Cote", repository_publisher="City of Los Angeles Department of City Planning document repository", publication_record_date="2016-08-10", locator="PDF physical page 159; 1942 Los Angeles directory transcription", source_quality="C_reputable_contemporary_or_scholarly", rights_notes="The report transcribes a contemporary directory entry. Residential information is not retained or published."),
        source(ARMY_REGISTER, stable_url="https://www.archives.gov/files/foia/pdf/nprc-crg-part4-508.pdf", archival_identifier="Official Army Register, active list, printed page 967", title="Official Army Register", author_creator="United States Army", repository_publisher="National Archives and Records Administration", publication_record_date="1942", locator="Active list page 967, Edward B. Zarembo", source_quality="A_direct_official", rights_notes="Documents West Point cadet service and appointment as a Quartermaster Corps second lieutenant."),
        source(NPS_ZAREMBO, stable_url="https://www.nps.gov/articles/oss-in-action-the-pacific-and-the-far-east.htm", title="OSS in Action: The Pacific and the Far East", repository_publisher="National Park Service", locator="Team Jackal section naming Captain Edward B. Zarembo", source_quality="B_authoritative_institutional", rights_notes="Official historical study corroborates the uncommon identity and commissioned OSS service; it does not state the OSS entry date."),
        source(NSA_ZARET, stable_url="https://www.nsa.gov/Helpful-Links/NSA-FOIA/Declassification-Transparency-Initiatives/Historical-Releases/Venona/smdpage14707/68/", title="Venona Documents: Information about and from Daniel A. Zaret", author_creator="National Security Agency", repository_publisher="National Security Agency", publication_record_date="1943-08-11; later declassified", locator="11AUG_ZARET.PDF description and linked document", source_quality="A_direct_official", collection_name="Venona historical releases", rights_notes="The official description identifies Zaret as an explosives expert formerly with the Lincoln Brigade; the exact OSS transition is not given."),
        source(NH_GUARD, stable_url="https://worldwartwoveterans.org/wp-content/uploads/2020/10/National-Guard-of-the-State-of-New-Hampshire-1939-PdF-Book.pdf", title="National Guard of the State of New Hampshire, 1939", author_creator="State of New Hampshire", repository_publisher="Historical official handbook reproduced by World War II Veterans", publication_record_date="1939", locator="Headquarters Battery and Combat Train, First Battalion, 172nd Field Artillery roster", source_quality="C_reputable_contemporary_or_scholarly", rights_notes="Contemporary official handbook names Archie C. Zarkadas; the exact later Army-to-OSS chronology remains unknown."),
        source(IRRIGATOR, stable_url="https://downloads.densho.org/ddr-densho-119/ddr-densho-119-20-mezzanine-786c5ea285.pdf", archival_identifier="Densho Digital Repository ddr-densho-119-20", title="Bay City Beckons Sr. Carpenter Zarubica", repository_publisher="The Irrigator; Densho Digital Repository", publication_record_date="1942-12-19", locator="Printed page 4", source_quality="C_reputable_contemporary_or_scholarly", rights_notes="Contemporary camp newspaper documents Zarubica's Minidoka carpenter-shop employment and departure for another job; it does not name the next employer."),
        source(DDPA_ZARFOSS, stable_url="https://www.distinguisheddaughtersofpa.org/Resources/Directory%201949-2024.pdf", title="Distinguished Daughters of Pennsylvania: 75th Anniversary Directory", repository_publisher="Distinguished Daughters of Pennsylvania", locator="Gweneth T. Zarfoss biographical entry", source_quality="B_authoritative_institutional", rights_notes="The entry connects the rare name to wartime naval intelligence work but uses rank terminology inconsistent with standard naval usage; no commissioned status is inferred."),
        source(OSSOG, stable_url="https://ossog.info/personnel.html", title="Office of Strategic Services Operational Groups Personnel", repository_publisher="OSS Operational Groups historical project", locator="Greek Operational Group V roster and Italian Fourth Group roster", source_quality="D_correlative_or_secondary", rights_notes="Corroborative roster only. It supports wartime identity and unit context, not a pre-OSS employer."),
        source(USWM_ZAPHIRIS, stable_url="https://uswarmemorials.org/html/people_details.php?PeopleID=24846", title="Emanuel Nick Zaphiris", repository_publisher="US War Memorials Overseas", locator="Greek Operational Group biographical entry", source_quality="D_correlative_or_secondary", rights_notes="Corroborative monument record supports the Emanuel spelling and middle name; protected identifier content is not reproduced in project data."),
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {"key": ORG_BROOKLYN, "canonical_name": "Brooklyn College", "historical_name": "Brooklyn College", "organization_type": "public college", "sector": "academia_and_research", "city": "Brooklyn", "state_or_region": "New York", "country": "United States", "normalization_notes": "Student status is not classified as employment."},
        {"key": ORG_GERMAN_ARMY, "canonical_name": "German Army", "historical_name": "German Army", "aliases": ["Wehrmacht Heer"], "organization_type": "military branch", "sector": "military", "country": "Germany", "active_dates": "1935-1945", "normalization_notes": "Zagórski's service is explicitly described as conscription and is not presented as voluntary."},
        {"key": ORG_USMA, "canonical_name": "United States Military Academy", "historical_name": "United States Military Academy", "aliases": ["West Point", "U.S.M.A."], "organization_type": "federal military academy", "sector": "academia_and_research", "city": "West Point", "state_or_region": "New York", "country": "United States", "normalization_notes": "Cadet or student status is separate from employment."},
        {"key": ORG_QMC, "canonical_name": "United States Army Quartermaster Corps", "historical_name": "Quartermaster Corps", "aliases": ["Q.M.C."], "organization_type": "United States Army branch", "sector": "military", "country": "United States", "normalization_notes": "Military assignment remains separate from civilian employment."},
        {"key": ORG_LINCOLN, "canonical_name": "Abraham Lincoln Brigade", "historical_name": "Lincoln Brigade", "aliases": ["Abraham Lincoln Battalion"], "organization_type": "American volunteer formation in the International Brigades", "sector": "military", "country": "Spain", "active_dates": "1937-1938", "normalization_notes": "Volunteer service in the Spanish Civil War; not a civilian employer."},
        {"key": ORG_NH_GUARD, "canonical_name": "Headquarters Battery and Combat Train, First Battalion, 172nd Field Artillery", "historical_name": "Headquarters Battery and Combat Train, First Battalion, 172nd Field Artillery", "aliases": ["1st Battalion, 172nd Field Artillery", "New Hampshire National Guard"], "organization_type": "National Guard field-artillery unit", "sector": "military", "state_or_region": "New Hampshire", "country": "United States", "normalization_notes": "The historical unit is preserved rather than silently collapsed into a modern successor."},
        {"key": ORG_MINIDOKA, "canonical_name": "Minidoka Relocation Center", "historical_name": "Minidoka Relocation Center (Hunt)", "aliases": ["Hunt", "Minidoka War Relocation Center"], "organization_type": "War Relocation Authority confinement site", "sector": "federal_government", "state_or_region": "Idaho", "country": "United States", "active_dates": "1942-1945", "normalization_notes": "The historical federal institution and its coercive confinement context are preserved."},
    ]


def affiliation(key: str, row: int, relationship: str, temporal: str, identity: str, confidence: str, quality: str, status: str = "published", **kwargs: object) -> dict[str, object]:
    value: dict[str, object] = {"key": key, "person_id": PEOPLE[row][0], "relationship_type": relationship, "pre_oss_temporal_basis": temporal, "identity_confidence": identity, "claim_confidence": confidence, "source_quality": quality, "publication_status": status}
    value.update(kwargs)
    return value


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, _label, _locator) in ARMY_OCCUPATIONS.items():
        identity = "high_confidence" if row in {5, 28, 31} else "confirmed"
        relationship = "student" if row in {5, 6, 28} else "unknown"
        values.append(affiliation(
            f"{slug(PEOPLE[row][1])}-army-occupation-b1029", row, relationship,
            "strongly_date_bounded", identity, "medium", "A_direct_official", "publish_qualified",
            occupation=occupation, end_date=date,
            date_precision=f"Historical civilian-occupation code {code} was recorded at Army entry on {date}; no named employer or institution is supplied.",
            country="United States", immediate_pre_oss=False, last_civilian_pre_service=False,
            research_notes="Broad historical category only; excluded from verified-employer analytics and not narrowed beyond the official wording.",
        ))
    values.extend([
        affiliation("david-zagier-journalist-b1029", 10, "employment", "probable_immediate", "confirmed", "medium", "C_reputable_contemporary_or_scholarly", "publish_qualified", occupation="journalist", date_precision="The publisher biography places journalism in South Africa, Paris and London before wartime travel to the United States and OSS recruitment; no employer or exact end date is named.", country="South Africa; France; United Kingdom", immediate_pre_oss=True, last_civilian_pre_service=True, research_notes="Best-supported civilian occupation and pathway; qualified because the chronology supplies no exact final journalism date or employer."),
        affiliation("sylvia-zagoria-brooklyn-college-b1029", 11, "student", "strongly_date_bounded", "high_confidence", "high", "C_reputable_contemporary_or_scholarly", organization_key=ORG_BROOKLYN, organization_name_as_found="Brooklyn College", role_title="student", end_date="1943", date_precision="The obituary states that Zagoria graduated in 1943 and then came to Washington during World War II to join OSS for a year.", city="Brooklyn", state_or_region="New York", country="United States", immediate_pre_oss=True, last_civilian_pre_service=False, research_notes="Immediate educational status, not employment."),
        affiliation("sylvia-zagoria-dance-instructor-b1029", 11, "employment", "documented_prewar", "high_confidence", "medium", "C_reputable_contemporary_or_scholarly", "publish_qualified", occupation="dance instructor", date_precision="The obituary places work as a dance instructor at an unnamed New York State children's summer camp before college; dates and employer name are absent.", state_or_region="New York", country="United States", immediate_pre_oss=False, last_civilian_pre_service=False, research_notes="Earlier documented work; not presented as the immediate predecessor or a named employer."),
        affiliation("wilhelm-zagorski-railway-worker-b1029", 12, "employment", "strongly_date_bounded", "high_confidence", "high", "C_reputable_contemporary_or_scholarly", occupation="railway worker", end_date="1943-01", date_precision="Micgiel's archival study says Zagórski worked on the railway in Bohumín from late 1940 until January 1943, after earlier forced labor.", city="Bohumín", country="Czechoslovakia", immediate_pre_oss=False, last_civilian_pre_service=True, research_notes="Last documented civilian occupation before conscription; no railway employer is named."),
        affiliation("wilhelm-zagorski-german-army-b1029", 12, "military_assignment", "strongly_date_bounded", "high_confidence", "high", "C_reputable_contemporary_or_scholarly", organization_key=ORG_GERMAN_ARMY, organization_name_as_found="German Army", role_title="conscripted soldier", start_date="1943", end_date="1944-06-28", date_precision="The study says he was conscripted in 1943, sent to France and captured by American forces at Cherbourg on June 28, 1944.", country="Germany; France", immediate_pre_oss=False, last_civilian_pre_service=False, research_notes="Coerced military service; Allied custody and later recruitment steps prevent labeling it the immediate OSS predecessor."),
        affiliation("dim-zaikowsky-film-technician-b1029", 15, "unknown", "temporal_relation_uncertain", "probable", "medium", "C_reputable_contemporary_or_scholarly", "publish_qualified", occupation="film technician", end_date="1942", date_precision="A 1942 Los Angeles directory transcription records the rare exact name with the occupation 'film techn'; no employer or OSS start date is supplied.", city="Los Angeles", state_or_region="California", country="United States", immediate_pre_oss=False, last_civilian_pre_service=False, research_notes="Useful occupation lead, but relation to OSS service requires the personnel file."),
        affiliation("edward-zarembo-usma-b1029", 35, "student", "documented_prewar", "confirmed", "high", "A_direct_official", organization_key=ORG_USMA, organization_name_as_found="U. S. M. A.", role_title="cadet", start_date="1937-07-02", end_date="1941-06-11", date_precision="The official register records cadet service from July 2, 1937 and a 1941 USMA degree and commission.", city="West Point", state_or_region="New York", country="United States", immediate_pre_oss=False, last_civilian_pre_service=False, research_notes="Student and cadet status, not civilian employment."),
        affiliation("edward-zarembo-quartermaster-b1029", 35, "military_assignment", "probable_immediate", "confirmed", "medium", "A_direct_official", "publish_qualified", organization_key=ORG_QMC, organization_name_as_found="Q. M. C.", role_title="second lieutenant; later captain", start_date="1941-06-11", date_precision="The official register records a Quartermaster Corps commission on June 11, 1941; NPS independently identifies Captain Zarembo in an OSS China mission. The transfer date is absent.", country="United States", immediate_pre_oss=True, last_civilian_pre_service=False, research_notes="Best-supported prior military branch, qualified because an intervening assignment or transfer date is not documented."),
        affiliation("daniel-zaret-lincoln-brigade-b1029", 37, "volunteer", "documented_prewar", "high_confidence", "high", "A_direct_official", organization_key=ORG_LINCOLN, organization_name_as_found="Lincoln Brigade", role_title="volunteer; explosives expert", end_date="1939", date_precision="NSA describes Daniel A. Zaret in a 1943 wartime document as an explosives expert who had been with the Lincoln Brigade during the Spanish Civil War.", country="Spain", immediate_pre_oss=False, last_civilian_pre_service=False, research_notes="Earlier volunteer military service, not civilian employment and not proven to be the immediate OSS predecessor."),
        affiliation("archie-zarkadas-nh-guard-b1029", 39, "military_assignment", "documented_prewar", "high_confidence", "high", "C_reputable_contemporary_or_scholarly", organization_key=ORG_NH_GUARD, organization_name_as_found="Headquarters Battery and Combat Train, First Battalion, 172nd Field Artillery", role_title="private", end_date="1939", date_precision="The contemporary 1939 New Hampshire National Guard handbook lists Archie C. Zarkadas in the unit's private roster; later Army-to-OSS chronology is not supplied.", state_or_region="New Hampshire", country="United States", immediate_pre_oss=False, last_civilian_pre_service=False, research_notes="Documented prewar military affiliation; not labeled immediate."),
        affiliation("milovan-zarubica-minidoka-b1029", 41, "employment", "temporal_relation_uncertain", "probable", "medium", "C_reputable_contemporary_or_scholarly", "publish_qualified", organization_key=ORG_MINIDOKA, organization_name_as_found="Hunt", role_title="senior foreman carpenter", start_date="1942-08-02", end_date="1942-12-18", date_precision="The contemporary camp newspaper says Milovan Zarubica served as senior foreman carpenter from August 2 until leaving December 18, 1942 for another San Francisco job.", state_or_region="Idaho", country="United States", immediate_pre_oss=False, last_civilian_pre_service=False, research_notes="Named wartime institution and job are documented, but the omitted middle initial and unknown next job prevent immediate-employer classification."),
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
        key = f"{slug(PEOPLE[row][1])}-army-occupation-b1029"
        identity = "High confidence from a nonshared protected identifier; the documented spelling or suffix variant remains visible." if row in {5, 28, 31} else "Confirmed by exact name and a nonshared protected identifier; the identifier is not published."
        values.append(claim(
            f"occupation-{slug(PEOPLE[row][1])}-b1029", row, "occupation",
            f"At Army entry on {date}, {PEOPLE[row][1]} was recorded in the broad historical category: {occupation}.",
            f"The official merged Army record carries category {code}; the NARA code list labels it {label}.",
            identity,
            "The category was recorded at Army entry and is strongly date-bounded, but its exact duration and relation to OSS are unknown.",
            "A_direct_official", "medium",
            [{"source_key": ARMY}, {"source_key": TECH}, {"source_key": CODES, "locator_override": locator}],
            "Qualified occupation or student status only. It is not a named employer, institution or workplace.", "publish_qualified", key,
        ))
    values.extend([
        claim("conflict-frank-zabatta-b1029", 3, "identity", "Frank V Zabatta remains a separate source-row entity from the page-521 Frank V Zobatta row pending duplicate review.", "The protected identifier is shared by the two spelling variants, while an Operational Groups roster uses Frank Zabatta.", "Conflicting at the entity level because one protected identifier links two separately preserved index rows.", "Identity evidence only; no occupation is transferred or counted twice.", "A_direct_official", "conflicting", [{"source_key": INDEX}, {"source_key": ARMY}, {"source_key": OSSOG, "support_type": "context_only"}], "The likely duplicate is visible and not silently merged.", "conflicting"),
        claim("identity-david-zagier-b1029", 10, "identity", "Indexed David D Zagier is confirmed as journalist David Zagier, later recorded in successor SSU files.", "A protected identifier links the index to an Army record that omits the middle initial; publisher and NARA sources independently supply the full distinctive name and OSS/SSU chronology.", "Confirmed by the protected identifier, full distinctive name and official successor record.", "The Army record is post-OSS and supplies identity only; the publisher biography supplies the earlier career sequence.", "A_direct_official", "confirmed", [{"source_key": INDEX}, {"source_key": ARMY}, {"source_key": ZAGIER_BOOK}, {"source_key": ZAGIER_NARA}], "The post-OSS Army occupation code is not used as pre-OSS evidence."),
        claim("immediate-david-zagier-journalist-b1029", 10, "immediate_pre_oss_affiliation", "Journalism is David D Zagier's best-supported civilian occupation immediately before wartime travel to the United States and OSS recruitment.", "The publisher biography places journalism in South Africa, Paris and London before his wartime move to the United States, where OSS recruited him.", "Confirmed identity from protected and official evidence.", "Probable immediate sequence; no final newspaper, exact end date or intervening status is named.", "C_reputable_contemporary_or_scholarly", "medium", [{"source_key": ZAGIER_BOOK}], "Published with qualification as an occupation, not a named employer.", "publish_qualified", "david-zagier-journalist-b1029"),
        claim("last-civilian-david-zagier-b1029", 10, "last_civilian_pre_service", "Journalism is the best-supported last civilian occupation before David D Zagier's OSS recruitment, but no employer is identified.", "The publisher chronology names no intervening civilian role between journalism and OSS recruitment.", "Confirmed distinctive identity.", "Probable, not explicit; exact dates remain unavailable.", "C_reputable_contemporary_or_scholarly", "medium", [{"source_key": ZAGIER_BOOK}], "Excluded from verified-employer counts because no organization is named.", "publish_qualified", "david-zagier-journalist-b1029"),
        claim("identity-sylvia-zagoria-b1029", 11, "identity", "Indexed Sylvia B Zagoria is strongly supported as Sylvia Beatrice Zagoria, a 1943 Brooklyn College graduate who joined OSS as an analyst.", "The obituary expands the middle name and directly links the exact rare name to one year of OSS analytical work.", "High confidence from the rare exact name, expanded middle name and direct OSS bridge.", "The obituary supplies a dated college-to-OSS sequence.", "C_reputable_contemporary_or_scholarly", "high", [{"source_key": INDEX}, {"source_key": ZAGORIA_OBIT}], "Sylvia Beatrice Zagoria is added as a documented name variant."),
        claim("immediate-sylvia-zagoria-student-b1029", 11, "immediate_pre_oss_affiliation", "Brooklyn College student status is Sylvia Beatrice Zagoria's best-supported immediate pre-OSS affiliation.", "The obituary says she graduated in 1943 and then came to Washington during World War II to join OSS.", "High-confidence rare-name identity with a direct OSS bridge.", "Strongly date-bounded transition; the exact recruitment day is not stated.", "C_reputable_contemporary_or_scholarly", "high", [{"source_key": ZAGORIA_OBIT}], "Student status is not presented as employment.", "published", "sylvia-zagoria-brooklyn-college-b1029"),
        claim("earlier-sylvia-zagoria-dance-b1029", 11, "other_pre_oss_affiliation", "Before college, Sylvia Beatrice Zagoria worked as a dance instructor at an unnamed New York State children's summer camp.", "The obituary identifies the camp role but provides neither camp name nor dates.", "High-confidence identity from the same direct OSS biography.", "Documented before college and therefore before OSS, but not immediate.", "C_reputable_contemporary_or_scholarly", "medium", [{"source_key": ZAGORIA_OBIT}], "Occupation only; no employer name is invented.", "publish_qualified", "sylvia-zagoria-dance-instructor-b1029"),
        claim("identity-wilhelm-zagorski-b1029", 12, "identity", "Indexed Sgt. Wilhelm Zagorski is strongly supported as Project Eagle radio operator Wilhelm Zagórski.", "Micgiel cites the indexed Box 860 personnel file and direct OSS mission records, and supplies the same given name, surname and sergeant status.", "High confidence from an explicit archival citation to this personnel file and mission biography.", "The source reconstructs the full pre-OSS sequence.", "C_reputable_contemporary_or_scholarly", "high", [{"source_key": INDEX}, {"source_key": PROJECT_EAGLE}], "Wilhelm Zagórski is added as a documented diacritic variant."),
        claim("last-civilian-wilhelm-zagorski-b1029", 12, "last_civilian_pre_service", "Railway work in Bohumín is Wilhelm Zagórski's last documented civilian occupation before German military conscription.", "The archival study dates the railway work from late 1940 to January 1943 and conscription later in 1943.", "High-confidence identity tied to the same personnel file.", "Strongly date-bounded last civilian occupation before military service; no employer name is given.", "C_reputable_contemporary_or_scholarly", "high", [{"source_key": PROJECT_EAGLE}], "No railway company is inferred.", "published", "wilhelm-zagorski-railway-worker-b1029"),
        claim("military-wilhelm-zagorski-b1029", 12, "other_pre_oss_affiliation", "Wilhelm Zagórski was conscripted into the German Army in 1943 and captured by American forces in June 1944.", "The study documents conscription, deployment to France and capture at Cherbourg.", "High-confidence identity from the cited personnel and mission files.", "Strongly date-bounded before Project Eagle, but Allied custody and recruitment steps intervene.", "C_reputable_contemporary_or_scholarly", "high", [{"source_key": PROJECT_EAGLE}], "Coerced service is explicitly labeled and is not treated as civilian employment.", "published", "wilhelm-zagorski-german-army-b1029"),
        claim("identity-constantine-zahariades-b1029", 14, "identity", "Constantine Zahariades is confirmed by the protected Army link and corroborated as an OSS Greek Operational Group technician fifth grade.", "The official bulk record exactly matches the indexed name, while the operational roster independently supplies the wartime unit and grade.", "Confirmed by a nonshared protected identifier and exact name.", "The roster establishes wartime OSS context; the Army record supplies only the earlier occupation category.", "A_direct_official", "confirmed", [{"source_key": INDEX}, {"source_key": ARMY}, {"source_key": OSSOG}], "Operational role does not establish a civilian employer."),
        claim("occupation-dim-zaikowsky-b1029", 15, "occupation", "A 1942 Los Angeles directory records Dim V Zaikowsky as a film technician.", "A municipal planning report reproduces the contemporary directory entry with the rare exact name and abbreviated occupation.", "Probable identity from the rare exact name; no second wartime identifier is public.", "The 1942 date is clear, but its relation to the unknown OSS entry date is uncertain.", "C_reputable_contemporary_or_scholarly", "medium", [{"source_key": LA_DIRECTORY}], "Qualified occupation lead; residential information is withheld.", "publish_qualified", "dim-zaikowsky-film-technician-b1029"),
        claim("identity-mario-zamparo-b1029", 26, "identity", "Mario Zamparo is confirmed as the person in an official Army record linked to the index.", "Exact name agreement and a nonshared protected identifier connect the records, but the grade is damaged and category 999 is undefined.", "Confirmed by exact name and protected identifier.", "Identity only; no occupation or pre-OSS affiliation can be derived.", "A_direct_official", "confirmed", [{"source_key": INDEX}, {"source_key": ARMY}, {"source_key": TECH}, {"source_key": CODES}], "Undefined data is not silently interpreted."),
        claim("identity-emanuel-zaphiris-b1029", 31, "identity", "Indexed Emauel N Zaphiris is strongly supported as Emanuel Nick Zaphiris of the OSS Greek Operational Group.", "A protected identifier links the Army record using Emanuel N; the memorial source independently supplies Emanuel Nick and the OSS unit.", "High confidence from the nonshared identifier, close spelling correction and unit corroboration.", "Wartime identity is strong; the Army occupation category remains the only pre-service work evidence.", "A_direct_official", "high", [{"source_key": INDEX}, {"source_key": ARMY}, {"source_key": USWM_ZAPHIRIS}], "Original indexed spelling remains visible; Emanuel N and Emanuel Nick are documented variants."),
        claim("identity-henry-zarbo-b1029", 33, "identity", "Henry A Zarbo is confirmed as the person in an official Army record linked to the index.", "Exact name agreement and a nonshared protected identifier connect the records; category 999 is undefined.", "Confirmed by exact name and protected identifier.", "Identity only; no occupation or pre-OSS affiliation can be derived.", "A_direct_official", "confirmed", [{"source_key": INDEX}, {"source_key": ARMY}, {"source_key": TECH}, {"source_key": CODES}], "Undefined data is not silently interpreted."),
        claim("identity-edward-zarembo-b1029", 35, "identity", "Indexed Edward B Zarembo is confirmed as the West Point graduate and Quartermaster Corps officer later serving as an OSS captain in China.", "The official register supplies the exact uncommon name, Army officer record and West Point chronology; NPS independently names the OSS captain.", "Confirmed by the exact uncommon name and mutually consistent official Army and OSS sources.", "The sources bracket pre-OSS and OSS service but do not give the transfer date.", "A_direct_official", "confirmed", [{"source_key": INDEX}, {"source_key": ARMY_REGISTER}, {"source_key": NPS_ZAREMBO}], "Commissioned Army status is directly documented."),
        claim("usma-edward-zarembo-b1029", 35, "other_pre_oss_affiliation", "Edward B Zarembo was a United States Military Academy cadet from 1937 until his 1941 graduation and commission.", "The official Army register supplies the dates, academy and resulting commission.", "Confirmed official identity.", "Explicitly before OSS service; student and cadet status is not employment.", "A_direct_official", "high", [{"source_key": ARMY_REGISTER}], "Excluded from employer analytics.", "published", "edward-zarembo-usma-b1029"),
        claim("immediate-edward-zarembo-qmc-b1029", 35, "immediate_pre_oss_affiliation", "The Quartermaster Corps is Edward B Zarembo's best-supported military affiliation before OSS, but the exact transfer is unverified.", "The official register records his 1941 Quartermaster Corps commission; NPS later identifies him as an OSS captain.", "Confirmed identity in both official sources.", "Probable immediate sequence only; an intervening unit or assignment remains possible.", "A_direct_official", "medium", [{"source_key": ARMY_REGISTER}, {"source_key": NPS_ZAREMBO}], "Published with a temporal qualification and excluded from verified-employer analytics.", "publish_qualified", "edward-zarembo-quartermaster-b1029"),
        claim("identity-daniel-zaret-b1029", 37, "identity", "Indexed Daniel A Zaret is strongly supported as the wartime explosives expert described in NSA's Venona release.", "The official release uses the same distinctive full name and describes a wartime intelligence subject with earlier Lincoln Brigade service.", "High confidence from the rare exact full name and contemporaneous intelligence context; the linked document does not explicitly name OSS.", "The Lincoln Brigade service clearly precedes the 1943 document and OSS index context.", "A_direct_official", "high", [{"source_key": INDEX}, {"source_key": NSA_ZARET}], "The personnel file remains necessary for a direct identity bridge and OSS dates."),
        claim("lincoln-brigade-daniel-zaret-b1029", 37, "other_pre_oss_affiliation", "Daniel A Zaret had served with the Lincoln Brigade during the Spanish Civil War and was described as an explosives expert.", "NSA's official Venona description states both the earlier brigade service and technical expertise.", "High-confidence rare-name identity.", "Documented prewar volunteer service; not shown to be immediate to OSS.", "A_direct_official", "high", [{"source_key": NSA_ZARET}], "Volunteer military service, not a civilian employer.", "published", "daniel-zaret-lincoln-brigade-b1029"),
        claim("identity-gweneth-zarfoss-b1029", 38, "identity", "Indexed Gweneth Zarfoss is probably Gweneth T. Zarfoss, described by a Pennsylvania institutional directory as a wartime naval intelligence woman.", "The rare exact first and surname align, and the directory supplies a middle initial and wartime intelligence context.", "Probable rather than confirmed because the source does not name OSS or a second identifier.", "Wartime service context only; no pre-OSS occupation is dated.", "B_authoritative_institutional", "medium", [{"source_key": INDEX}, {"source_key": DDPA_ZARFOSS}], "The source's 'First Lieutenant in the Navy' wording conflicts with standard naval rank terminology, so commissioned status is not inferred.", "publish_qualified"),
        claim("identity-archie-zarkadas-b1029", 39, "identity", "Indexed Archie C Zarkadas is strongly supported as the New Hampshire National Guard servicemember of the same rare exact name.", "A contemporary official handbook lists Archie C. Zarkadas in a field-artillery unit before the United States entered the war.", "High confidence from the rare exact full name and military context; no public protected-identifier bridge is supplied.", "The 1939 affiliation clearly predates OSS.", "C_reputable_contemporary_or_scholarly", "high", [{"source_key": INDEX}, {"source_key": NH_GUARD}], "The exact Army-to-OSS sequence still requires Box 861."),
        claim("nh-guard-archie-zarkadas-b1029", 39, "other_pre_oss_affiliation", "Archie C Zarkadas served in a New Hampshire National Guard field-artillery unit in 1939.", "The official handbook lists him among the unit's privates.", "High-confidence rare-name identity.", "Documented prewar affiliation; it is not shown to be immediate to OSS.", "C_reputable_contemporary_or_scholarly", "high", [{"source_key": NH_GUARD}], "Military assignment, not employment.", "published", "archie-zarkadas-nh-guard-b1029"),
        claim("identity-paul-zarras-b1029", 40, "identity", "Indexed Paul J Zarras is strongly supported as the corporal listed in OSS Greek Operational Group V.", "The rare exact name and middle initial match the historical roster, which directly places him in an OSS unit.", "High confidence from the exact distinctive name and direct OSS unit context.", "Wartime identity only; no pre-OSS affiliation is supplied.", "D_correlative_or_secondary", "high", [{"source_key": INDEX}, {"source_key": OSSOG}], "The personnel file is still needed for a direct source and pre-OSS career."),
        claim("identity-milovan-zarubica-b1029", 41, "identity", "Indexed Milovan R Zarubica is probably the Milovan Zarubica who supervised the Minidoka carpenter shop in 1942.", "The contemporary camp newspaper gives the rare exact first and surname, wartime date and skilled role; the index alone supplies the middle initial.", "Probable identity because the newspaper omits the middle initial and does not mention OSS.", "The 1942 job is wartime, but its exact relation to OSS entry remains unknown.", "C_reputable_contemporary_or_scholarly", "medium", [{"source_key": INDEX}, {"source_key": IRRIGATOR}], "Published only as a qualified candidate identity and employment chronology.", "publish_qualified"),
        claim("minidoka-milovan-zarubica-b1029", 41, "other_pre_oss_affiliation", "Milovan Zarubica served as senior foreman carpenter at Minidoka in 1942 before leaving for another San Francisco job.", "The contemporary camp paper dates his role and explicitly notes departure for an unnamed next job.", "Probable identity from the rare name; the middle initial is absent.", "Temporal relation to OSS is uncertain, and this cannot be the immediate predecessor because the source names an intervening job.", "C_reputable_contemporary_or_scholarly", "medium", [{"source_key": IRRIGATOR}], "The next employer is not invented; Minidoka is not marked immediate.", "publish_qualified", "milovan-zarubica-minidoka-b1029"),
        claim("conflict-asa-zatz-b1029", 43, "identity", "Asa Zatz's protected identifier points to a damaged Army name rendered only as Z Z; no occupation is transferred.", "The identifier link is specific, but the Army name and grade are damaged and the historical occupation code cannot safely resolve the person.", "Conflicting until the original personnel and Army records are reviewed.", "Identity context only; no pre-OSS occupation or employer is accepted.", "A_direct_official", "conflicting", [{"source_key": INDEX}, {"source_key": ARMY}, {"source_key": TECH}], "Postwar theatrical and translation leads were rejected as pre-OSS evidence.", "conflicting"),
    ])
    return values


def unresolved_reason(row: int) -> str:
    reasons = {
        4: "A short officer-like identifier and common-name results did not establish Charles A Zabel's identity or pre-OSS affiliation.",
        8: "Exact-name and likely transliteration searches produced no reliable OSS, military or employment bridge for Heinz Zacharian.",
        13: "The exact name produced no reliable wartime identity or pre-OSS employment bridge.",
        17: "Exact-name and Army-focused searches did not establish a reliable identity or employer beyond the index.",
        20: "The second David L Zakon row lacks the protected identifier attached to the separate row 19 entity; the two rows remain separate pending file review.",
        21: "Exact-name and Greek-name variants produced no reliable identity or employment bridge.",
        22: "Exact-name searches produced modern and family-history noise but no reliable wartime identity or pre-OSS affiliation.",
        23: "The indexed Tehodore spelling and Theodore variants produced no reliable identity-and-employment bridge.",
        24: "Exact-name and spelling-variant searches produced no reliable employer or dated pre-OSS affiliation.",
        25: "The similar Mario Zamparo row cannot be used to identify Bruno G Zamparo; exact-name searches produced no reliable bridge.",
        27: "Exact-name and Italian-name searches produced no reliable wartime identity or employment evidence.",
        29: "Exact-name results did not establish Ladimer J Zanski's identity or pre-OSS affiliation.",
        36: "A 508th Parachute Infantry roster contains a same-name John A Zarembski, but no OSS, Box 861 or second-identifier bridge establishes that namesake.",
        42: "Postwar Indiana University and business evidence fits a same-name Cora V Zaser but does not establish her wartime identity or pre-OSS occupation.",
        44: "A wartime 50th Armored Infantry Battalion roster contains Peter C Zavalis, but no second identifier or OSS transition establishes the match.",
        45: "Exact indexed-spelling and likely Zavitovsky variants produced no reliable wartime identity or employment bridge.",
        46: "Exact-name and likely spelling-variant searches produced no reliable identity, OSS role or pre-OSS affiliation.",
    }
    return reasons.get(row, "Accessible official, CIA, OSS, exact-name, employer, occupation, obituary, institutional, newspaper, directory and archival searches produced no reliable identity-and-affiliation bridge; unbridged namesakes and postwar-only leads were rejected.")


def base_update(row: int, **overrides: object) -> dict[str, object]:
    value: dict[str, object] = {"person_id": PEOPLE[row][0], "manual_review_required": True, "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "high"}
    value.update(overrides)
    return value


def person_updates() -> list[dict[str, object]]:
    special = set(ARMY_OCCUPATIONS) | {3, 10, 11, 12, 14, 15, 26, 31, 33, 35, 37, 38, 39, 40, 41, 43, 44}
    values: list[dict[str, object]] = []
    for row in sorted(set(PEOPLE) - special):
        reason = unresolved_reason(row)
        values.append(base_update(row, identity_status="unresolved", identity_evidence=f"The visually verified page 519 source preserves {PEOPLE[row][1]}. {reason}", research_status="requires_archival_review", archival_review_priority="critical" if row in {4, 8, 13, 20, 22, 23, 24, 25, 27, 29, 36, 42, 45, 46} else "high", next_action=f"Review indexed Box {PEOPLE[row][2]} for corroborating identifiers, immediate pre-OSS affiliation and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}"))
    for row in sorted(ARMY_OCCUPATIONS):
        variants: list[str] = []
        identity_status = "confirmed"
        evidence = "A nonshared protected identifier and exact official name agreement connect the index and Army records; the identifier remains private."
        if row == 5:
            variants, identity_status, evidence = ["Dante T Zaccagnini"], "high_confidence", "A nonshared protected identifier connects the index to an Army record using the close surname variant Zaccagnini."
        elif row == 28:
            variants, identity_status, evidence = ["Henry G Zander III"], "high_confidence", "A nonshared protected identifier connects the records; the Army form adds the suffix III."
        elif row == 31:
            variants, identity_status, evidence = ["Emanuel N Zaphiris", "Emanuel Nick Zaphiris"], "high_confidence", "A nonshared protected identifier connects the records, and independent Greek Operational Group evidence supports the Emanuel spelling and Nick middle name."
        values.append(base_update(row, identity_status=identity_status, identity_evidence=evidence, name_variants=variants, replace_name_variants=False, personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="occupation_only_found", nara_catalog_id="1263923", next_action=f"Review indexed Box {PEOPLE[row][2]} to identify a named employer or institution and establish Army-to-OSS chronology. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed; the bulk record supplies only a historical occupation category."))
    values.extend([
        base_update(3, identity_status="conflicting", identity_evidence="The protected identifier is shared by page 519 Frank V Zabatta and page 521 Frank V Zobatta. The likely spelling-variant duplicate remains two source rows and two cautious entities pending merge review.", possible_duplicate_group="batch1029-frank-zabatta-zobatta-duplicate", research_status="conflicting_sources", archival_review_priority="critical", next_action="Review Boxes 860 and 864 and the original identifier-bearing files to determine whether the Zabatta and Zobatta rows represent one person. No Army occupation is transferred while the cluster remains unresolved."),
        base_update(10, identity_status="confirmed", identity_evidence="A nonshared protected identifier links the index to an Army record omitting the middle initial; a publisher biography and NARA SSU listing independently supply the full distinctive name and OSS chronology.", personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="occupation_only_found", nara_catalog_id="1263923", archival_review_priority="medium", next_action="Review Box 860 to identify David D Zagier's final newspaper or employer and exact OSS recruitment date; journalism is the best-supported occupation, but no employer is named."),
        base_update(11, identity_status="high_confidence", identity_evidence="The rare exact name and expanded middle name in the obituary directly connect Brooklyn College graduation to one year as an OSS analyst.", name_variants=["Sylvia Beatrice Zagoria"], replace_name_variants=False, personnel_category="civilian_professional_or_administrative_grade", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="occupation_only_found", archival_review_priority="medium", next_action="Review Box 860 to confirm the 1943 OSS appointment date and whether an employer intervened after Brooklyn College; student status is not counted as employment."),
        base_update(12, identity_status="high_confidence", identity_evidence="Micgiel's archival study cites this Box 860 personnel file and direct OSS mission records for Sgt. Wilhelm Zagórski.", name_variants=["Wilhelm Zagórski"], replace_name_variants=False, personnel_category="foreign_or_allied_military_personnel", commissioned_officer=False, allied_or_foreign_personnel=True, research_status="occupation_only_found", archival_review_priority="medium", next_action="Review Box 860 to document the Allied-custody, Polish-force and OSS recruitment sequence and to identify the Bohumín railway employer. Railway work remains the last documented civilian occupation before military service."),
        base_update(15, identity_status="probable", identity_evidence="A 1942 Los Angeles directory transcription supplies the rare exact name Dim V Zaikowsky and the occupation film technician, but no source directly bridges it to OSS beyond the index.", research_status="needs_temporal_review", archival_review_priority="critical", next_action="Review Box 860 to confirm the Los Angeles directory identity, named studio or employer and relation of the 1942 occupation to OSS entry."),
        base_update(26, identity_status="confirmed", identity_evidence="A nonshared protected identifier and exact official name agreement connect the index and Army records; damaged grade text and undefined code 999 remain uninterpreted.", personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="requires_archival_review", nara_catalog_id="1263923", archival_review_priority="critical", next_action="Review Box 861 to identify Mario Zamparo's pre-OSS affiliation. No occupation or employer is inferred from undefined code 999."),
        base_update(33, identity_status="confirmed", identity_evidence="A nonshared protected identifier and exact official name agreement connect the index and Army records; undefined code 999 remains uninterpreted.", personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="requires_archival_review", nara_catalog_id="1263923", archival_review_priority="critical", next_action="Review Box 861 to identify Henry A Zarbo's pre-OSS affiliation. No occupation or employer is inferred from undefined code 999."),
        base_update(35, identity_status="confirmed", identity_evidence="The official Army register supplies the uncommon exact name, West Point history and Quartermaster commission; NPS independently names Captain Edward B Zarembo in an OSS China mission.", personnel_category="commissioned_army_officer", commissioned_officer=True, allied_or_foreign_personnel=False, research_status="needs_temporal_review", archival_review_priority="critical", next_action="Review Box 861 to determine Zarembo's exact Quartermaster-to-OSS transfer and any intervening unit. No civilian employer is documented before his military career."),
        base_update(37, identity_status="high_confidence", identity_evidence="NSA's official Venona release uses the rare exact full name Daniel A. Zaret and describes a 1943 intelligence subject with earlier Lincoln Brigade service.", research_status="occupation_only_found", archival_review_priority="critical", next_action="Review Box 861 to establish a direct public identity bridge, immediate pre-OSS assignment and civilian employment after the Spanish Civil War."),
        base_update(38, identity_status="probable", identity_evidence="A Pennsylvania institutional directory links the rare name Gweneth T. Zarfoss to wartime naval intelligence, but it does not name OSS or a second identifier and uses nonstandard naval rank terminology.", name_variants=["Gweneth T Zarfoss"], replace_name_variants=False, research_status="needs_identity_review", archival_review_priority="critical", next_action="Review Box 861 and naval personnel records to confirm the middle name, service branch, rank terminology, OSS relationship and pre-service occupation. No commissioned status is inferred from the current source."),
        base_update(39, identity_status="high_confidence", identity_evidence="A contemporary New Hampshire National Guard handbook lists the rare exact name Archie C. Zarkadas in a field-artillery unit before the war.", research_status="needs_temporal_review", archival_review_priority="critical", next_action="Review Box 861 to confirm the National Guard identity, later Signal Corps status and exact transfer into OSS; no civilian employer is yet documented."),
        base_update(40, identity_status="high_confidence", identity_evidence="A historical OSS Operational Groups roster lists the rare exact name and middle initial Paul J. Zarras as a corporal in Greek Operational Group V.", personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="requires_archival_review", archival_review_priority="critical", next_action="Review Box 861 for a direct source, immediate pre-OSS assignment and last civilian employer; the roster establishes wartime identity only."),
        base_update(41, identity_status="probable", identity_evidence="A contemporary 1942 camp newspaper documents a rare-name Milovan Zarubica as senior foreman carpenter, but omits the indexed middle initial and does not mention OSS.", research_status="needs_temporal_review", archival_review_priority="critical", next_action="Review Box 861 to confirm the Minidoka identity and identify the unnamed San Francisco job that followed; Minidoka is not labeled the immediate OSS predecessor."),
        base_update(43, identity_status="conflicting", identity_evidence="The protected identifier points to a damaged Army name rendered only as Z Z. The link is preserved, but no identity, occupation or grade is transferred without the original records.", research_status="conflicting_sources", nara_catalog_id="1263923", archival_review_priority="critical", next_action="Review Box 861 and the original Army record to resolve the damaged name and determine whether any occupation code belongs to Asa Zatz. Postwar theatrical and translation careers are not treated as pre-OSS evidence."),
        base_update(44, identity_status="probable", identity_evidence="A wartime 50th Armored Infantry Battalion roster contains the rare exact name Peter C. Zavalis, but it supplies no second identifier or OSS transition.", research_status="needs_identity_review", archival_review_priority="critical", next_action="Review Box 861 to confirm the 50th Armored Infantry identity, service chronology and pre-OSS civilian employer. The unit lead is not published as settled affiliation evidence."),
    ])
    if len(values) != 46:
        raise RuntimeError(f"Expected 46 person updates, generated {len(values)}")
    return values


def research_attempts() -> list[dict[str, object]]:
    updates = {item["person_id"]: item for item in person_updates()}
    substantiated = set(ARMY_OCCUPATIONS) | {3, 10, 11, 12, 14, 15, 26, 31, 33, 35, 37, 38, 39, 40, 41, 43, 44}
    attempts: list[dict[str, object]] = []
    for row, (person_id, name, box) in PEOPLE.items():
        status = str(updates[person_id]["research_status"])
        if row in substantiated:
            outcome = "candidate_rejected" if status == "conflicting_sources" else "source_reviewed"
            reviewed = 11 if row in {10, 11, 12, 35, 37, 38, 39, 41} else 7
            rejected = 5 if status in {"conflicting_sources", "needs_identity_review"} else 3
            note = "At least one reviewed identity, occupation, student, volunteer, employment or military-affiliation outcome is preserved with claim-level citations; remaining employer and temporal questions remain explicit."
        else:
            outcome = "candidate_rejected"
            reviewed = 5
            rejected = 4
            note = unresolved_reason(row)
        attempts.append({
            "key": f"page519-row{row}-{slug(name)}-b1029",
            "person_id": person_id,
            "source_adapter": "manual_staged_protocol",
            "query_text": f"{name}; NARA OSS index context; exact-name and meaningful initial, suffix, punctuation, transliteration and OCR variants; OSS, CIA Reading Room, rank, branch, assignment and protected-identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory and archival searches; indexed Box {box}",
            "query_variant_type": "staged_identity_employment_archival_protocol_batch_1029",
            "started_at": "2026-11-04T13:00:00-05:00",
            "completed_at": "2026-11-04T23:59:00-05:00",
            "outcome": outcome,
            "sources_reviewed": reviewed,
            "candidate_sources_rejected": rejected,
            "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives and postwar-only leads were rejected. Shared or damaged protected-identifier links were not converted into occupations. Army categories were not converted into named employers, and undefined category 999 was not interpreted.",
            "research_notes": f"{note} The official index, exact-name OSS searches, grouped CIA Reading Room checks, and employer, occupation, obituary, institutional, newspaper, directory and archival searches were reviewed as applicable. Page 519, the page 520 boundary and cited code-list pages were visually checked. No authenticated NARA Catalog API request was made.",
            "next_action": str(updates[person_id]["next_action"]),
            "attempt_number": 1,
            "research_agent_version": "before-oss-b1029-v1",
        })
    if len(attempts) != 46:
        raise RuntimeError(f"Expected 46 research attempts, generated {len(attempts)}")
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-1029-v1",
        "reviewer": "Before OSS Batch 1029 evidence review",
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
