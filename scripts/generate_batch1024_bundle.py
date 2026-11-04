#!/usr/bin/env python3
"""Generate the reviewed Batch 1024 evidence bundle for PDF page 514."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page514-mallery-wooster-to-margaret-wright-review_"
    "batch-1024_2026-11-04.json"
)

INDEX = "nara-index-b1024"
ARMY = "army-bulk-b1024"
TECH = "army-tech-b1024"
CODES = "army-codes-b1024"
TRUMAN_WRIGHT = "truman-edwin-wright-oral-history-b1024"
MET_WORKUM = "met-emily-workum-portrait-b1024"
OCEANSPRINGS_WORKUM = "oceansprings-emily-workum-biography-b1024"
NARA_WRACHFORD = "nara-ccc-wrachford-reels-b1024"

ORG_US_ARMY = "us-army-existing-b1024"
ORG_COLUMBIA = "columbia-university-existing-b1024"
ORG_NORTHERN_WESTCHESTER = "northern-westchester-clinic-b1024"

PEOPLE = {
    1: ("e4ebc575-2642-5160-906a-2220d43319a3", "Mallery O Wooster", "853"),
    2: ("6a2fc5d3-4608-566a-afd9-9c48efbcd1f7", "Allen D Wooten", "853"),
    3: ("3802a76b-8fb6-5020-b142-b19ec3e550ee", "William R Wooters", "853"),
    4: ("db7e468d-6e52-563d-8d25-7dd14ade55fd", "John E Worachek", "853"),
    5: ("065c3277-eb87-52c4-8456-74a653bd36c3", "Francis V Worcester", "853"),
    6: ("a3b9e51b-2c13-5889-bb9a-dc959c61b0c2", "John R Work", "853"),
    7: ("314b1dc2-58d5-586e-aaf8-0fc01fa10921", "Hazel E Workman", "853"),
    8: ("2555ddaa-472b-5630-b6f9-c52781aebe9e", "Emily H Workum", "853"),
    9: ("beec339a-9075-5fff-9e7e-1632477271d9", "Paul M Worley", "853"),
    10: ("8fd24250-43e5-5330-a7f3-29c9a1f4ada9", "Sally M Wormser", "853"),
    11: ("cbd91da7-a43f-5ced-b92c-5f471ddbba13", "Theodore F Worple", "853"),
    12: ("2b68a52c-d389-534a-8b3a-001ffb98830d", "Thomas H Worrall", "853"),
    13: ("5a6300b5-f7b9-552f-b052-345c2bbacf1c", "John C Worrell", "853"),
    14: ("8f6d87ae-e002-509e-bf1b-12512ad9fd8d", "Betty Ann Worsely", "853"),
    15: ("8c779c48-c92e-58a5-9db1-7b480f6fb6f9", "David A Worsly", "853"),
    16: ("31be06d3-a1fb-5be9-ba07-3efbe66faae6", "Frederick W Worst", "853"),
    17: ("21388810-0a8a-5f5d-bdb1-6ed02d25f177", "George C Worth", "853"),
    18: ("962853de-164c-55b0-aa10-439c0aae48c0", "William B Worthy", "853"),
    19: ("a2ffc735-84c0-5e72-865e-e5579f893645", "Lothar Wortman", "853"),
    20: ("b5d82a22-dcf7-51ec-992b-c8199bcb3166", "Elizabeth M Woulfe", "853"),
    21: ("20130ac6-fb8d-5e08-9dc8-9d9d6098cc58", "Henry F Wozniak", "853"),
    22: ("d35058ed-5a03-5b7b-8769-7650dda55859", "George E Wrachford", "853"),
    23: ("bacc5d53-32be-5a1a-8ec5-72e332d447a0", "Bobby C Wrenn", "853"),
    24: ("16ad9ade-bd1f-5eac-843f-9115cd2a9097", "Edward F Wrenn Jr.", "853"),
    25: ("345e523e-83f2-5b3a-ae18-4f745f2c3a5d", "Norman T Wrenn", "853"),
    26: ("b6c13589-41be-5f1c-9a52-f662f48e5feb", "Andrew H Wright", "854"),
    27: ("fbd1587a-8f82-54b9-9b16-2e95d65c402d", "Ann M Wright", "854"),
    28: ("d11373af-da6f-554e-b456-b6ebe11da5ab", "Anne K Wright", "854"),
    29: ("25db8320-11d8-5776-8408-691c9225636d", "Arthur B Wright", "854"),
    30: ("243c82f6-449e-5656-8680-59fd2f9e80cf", "Beatrice W Wright", "854"),
    31: ("2244d0f0-15f1-5806-8232-44f5be0cd300", "Beaumont W Wright", "854"),
    32: ("88a61421-49bc-5f72-923f-034a214eac40", "Charles V Wright", "854"),
    33: ("d3ef2fe4-bdb1-5d64-9f3c-b194f5b7cdb0", "Charles E Wright Jr.", "854"),
    34: ("28bffbec-ec05-59f0-8618-aaf11c4ad797", "Donald M Wright", "854"),
    35: ("2ec84e9a-5e64-5dc9-8227-cb806101b381", "Edwin M Wright", "854"),
    36: ("d49a02a9-01ac-5bb7-acd0-6ab47b9e0287", "Helen L Wright", "854"),
    37: ("08340508-1629-5443-92bc-62e5714b79f6", "Herman A Wright", "854"),
    38: ("1aac6838-e712-577b-8079-8dc6dad43b32", "Jean Wright", "854"),
    39: ("9e1d0812-7646-5ad5-9171-de472084ee9d", "Jesse P Wright", "854"),
    40: ("2abcc94f-1aca-5499-9c4d-6f5fb1916533", "John K Wright", "854"),
    41: ("9cce31ed-15fc-5eb6-a277-c241ae558f40", "Josephine Wright", "854"),
    42: ("27bbe658-9a36-53cc-b114-9bf29cd4a1d1", "Kenneth M Wright", "854"),
    43: ("2dd1526a-f746-53d1-ba89-6373f6bb36cb", "Leroy J Wright", "854"),
    44: ("165c1e05-8406-5a62-985d-88497d7271ec", "Leslie E Wright Jr.", "854"),
    45: ("75cb5453-a487-5b69-9029-3f1b48eb92f4", "Lester L Wright", "854"),
    46: ("b579fba6-2f2e-57e7-a375-34fcf6400951", "Margaret E Wright", "854"),
}

ARMY_OCCUPATIONS = {
    3: ("1943-01-18", "137", "stenographer or typist", "Stenographers and typists", "PDF physical page 171; historical category 1-37", "unknown"),
    19: ("1941-05-20", "068", "semiprofessional occupation, not elsewhere classified", "Semiprofessional occupations, n.e.c.", "PDF physical page 171; historical category 0-68", "unknown"),
    22: ("1941-09-24", "781", "mechanic or repairman, motor vehicle", "Mechanics and repairmen, motor vehicle", "PDF physical page 175; historical category 7-81", "unknown"),
    26: ("1943-02-22", "992", "student", "Students", "PDF physical page 304; amended category 9-92", "student"),
    32: ("1942-09-11", "056", "photographer", "Photographers", "PDF physical page 171; historical category 0-56", "unknown"),
    33: ("1942-10-10", "678", "machine-shop or related occupation, not elsewhere classified", "Machine shop and related occupations, n.e.c.", "PDF physical page 174; historical category 6-78", "unknown"),
    34: ("1943-03-15", "992", "student", "Students", "PDF physical page 304; amended category 9-92", "student"),
    37: ("1940-07-27", "736", "chauffeur or driver of a bus, taxi, truck, or tractor", "Chauffeurs and drivers, bus, taxi, truck, and tractor", "PDF physical page 174; historical category 7-36", "unknown"),
    39: ("1940-11-25", "065", "embalmer or undertaker", "Embalmers and undertakers", "PDF physical page 171; historical category 0-65", "unknown"),
    44: ("1942-07-23", "003", "architect", "Architects", "PDF physical page 170; historical category 0-03", "unknown"),
    45: ("1943-04-21", "180", "salesman to consumers", "Salesmen, to consumers", "PDF physical page 172; historical category 1-80", "unknown"),
}

ARMY_IDENTITY_ONLY = {
    42: ("1945-11-22", "The reviewed Army entry postdates OSS dissolution; no grade, occupation, or pre-OSS chronology is transferred."),
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def source(key: str, **kwargs: object) -> dict[str, object]:
    value: dict[str, object] = {"key": key, "access_date": "2026-11-04"}
    value.update(kwargs)
    return value


def sources() -> list[dict[str, object]]:
    return [
        source(INDEX, stable_url="https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf", archival_identifier="RG 226, Entry A1-224, Boxes 853-854", title="OSS Personnel Files from Excel", author_creator="National Archives and Records Administration", repository_publisher="National Archives and Records Administration", publication_record_date="2010-12-23", locator="PDF page 514, rows 1-46; visually checked at 180 dpi against the source table", source_quality="A_direct_official", collection_name="Records of the Office of Strategic Services, Record Group 226", rights_notes="All 46 printed rows remain separate. Full service or serial numbers remain private."),
        source(ARMY, source_id="cf280d3e-1262-5963-90d7-40ffa66c53a3", stable_url="https://catalog.archives.gov/id/1263923", archival_identifier="National Archives Identifier 1263923; parent series NAID 604357", title="Electronic Army Serial Number Merged File, ca. 1938-1946", author_creator="Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration", repository_publisher="National Archives and Records Administration", publication_record_date="1938-1946; merged file created 2002", locator="Official unrestricted ASNEF.FIN.DAT; twelve Batch 1024 protected-identifier candidates reviewed", source_quality="A_direct_official", collection_name="World War II Army Enlistment Records", document_number="ASNEF.FIN.DAT", rights_notes="No raw record or full protected identifier is retained in public assets. Coded occupations identify neither employer nor workplace."),
        source(TECH, source_id="f24044fe-5fcd-5d78-96d4-25d577e90703", stable_url="https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf", archival_identifier="NN3-064-03-008; National Archives Identifier 1263923", title="World War II Army Enlistment Records: Reference Copy of Technical Documentation", author_creator="National Archives and Records Administration", repository_publisher="National Archives at College Park - Electronic Records", publication_record_date="1994-2005; reference copy modified 2011", locator="PDF physical pages 44-46; identifier, name, Army-entry-date, grade and civilian-occupation fields", source_quality="A_direct_official", collection_name="World War II Army Enlistment Records technical documentation", rights_notes="Used to interpret selected fields only; source damage, coding limits and incomplete coverage remain applicable."),
        source(CODES, source_id="ace136c1-722a-5af0-a43b-bab53792ae6a", stable_url="https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1CL_SD.pdf", archival_identifier="National Archives Identifier 1263923; Code No. 30", title="NARA Compiled Code Lists for the Electronic Army Serial Number Merged File", author_creator="National Archives and Records Administration", repository_publisher="National Archives at College Park - Electronic Records", publication_record_date="2011-01-12; modified 2011-03-17", locator="PDF physical pages 170-175 and 304; Batch 1024 categories visually checked", source_quality="A_direct_official", collection_name="World War II Army Enlistment Records technical documentation", rights_notes="Historical categories identify neither employer, institution nor workplace."),
        source(TRUMAN_WRIGHT, stable_url="https://www.trumanlibrary.gov/library/oral-histories/wright", archival_identifier="Edwin M. Wright oral history interview, July 26, 1974", title="Edwin M. Wright Oral History Interview", author_creator="Edwin M. Wright; interviewer Richard D. McKinzie", repository_publisher="Harry S. Truman Presidential Library & Museum", publication_record_date="1974-07-26", locator="Biographical introduction and interview discussion of 1921-1942 education, work and OSS recruitment", source_quality="B_authoritative_institutional", collection_name="Harry S. Truman Library Oral Histories"),
        source(MET_WORKUM, stable_url="https://www.metmuseum.org/art/collection/search/273720", archival_identifier="The Metropolitan Museum of Art object 1994.254.375", title="[Emily Workum, Bedford Village, New York]", author_creator="Walker Evans", repository_publisher="The Metropolitan Museum of Art", publication_record_date="1939-1940", locator="Object title, date, creator and collection record", source_quality="B_authoritative_institutional", collection_name="The Met Collection"),
        source(OCEANSPRINGS_WORKUM, stable_url="https://oceanspringsarchives.net/node/39", archival_identifier="Emily Lyon Hamill Workum biographical entry", title="Emily Workum", repository_publisher="Ocean Springs Archives", locator="Biographical entry describing acting and Planned Parenthood activity before World War II", source_quality="D_correlative_or_secondary", collection_name="Ocean Springs Archives biographical collection", rights_notes="Used as a qualified biographical source; claims are not promoted to confirmed or high confidence without a stronger direct record."),
        source(NARA_WRACHFORD, stable_url="https://www.archives.gov/files/st-louis/pdf/w-reels.pdf", archival_identifier="Civilian Conservation Corps personnel records digitization list, W reels", title="Civilian Conservation Corps Personnel Records Digitization List: W", author_creator="National Archives at St. Louis", repository_publisher="National Archives and Records Administration", locator="Wrachford, George Franklin entry", source_quality="A_direct_official", collection_name="Civilian Conservation Corps personnel records", rights_notes="Context for the Army middle-name form only; it does not independently link the CCC record to the OSS index row."),
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {"key": ORG_US_ARMY, "organization_id": "28a26f92-78af-5a1a-9c09-a843eb5975b4", "canonical_name": "United States Army", "historical_name": "United States Army", "aliases": ["U.S. Army", "Army", "AUS"], "organization_type": "military service", "sector": "military", "country": "United States", "normalization_notes": "Military assignment is modeled separately from civilian employment."},
        {"key": ORG_COLUMBIA, "organization_id": "87e3d52a-9ace-512a-9677-e966b7fbd5e5", "canonical_name": "Columbia University", "historical_name": "Columbia University", "organization_type": "university", "sector": "academia_and_research", "city": "New York", "state_or_region": "New York", "country": "United States", "normalization_notes": "Student status is not represented as employment by the university."},
        {"key": ORG_NORTHERN_WESTCHESTER, "canonical_name": "Northern Westchester Planned Parenthood clinic", "historical_name": "Northern Westchester clinic", "aliases": ["Northern Westchester clinic at Mount Kisco"], "organization_type": "family-planning clinic", "sector": "medicine_and_public_health", "city": "Mount Kisco", "state_or_region": "New York", "country": "United States", "active_dates": "founded 1935", "normalization_notes": "The source's historical wording is preserved; no modern organizational successor is substituted."},
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
        identity = "high_confidence" if row == 22 else "confirmed"
        values.append(affiliation(
            f"{slug(PEOPLE[row][1])}-army-occupation-b1024", row, relationship,
            "strongly_date_bounded", identity, "medium", "A_direct_official", "publish_qualified",
            occupation=occupation, end_date=date,
            date_precision=f"Historical civilian-occupation code {code} was recorded at Army entry on {date}; no named employer or institution is supplied.",
            country="United States", immediate_pre_oss=False, last_civilian_pre_service=False,
            research_notes="Broad historical category only; excluded from verified-employer analytics and not narrowed beyond the official wording.",
        ))
    values.extend([
        affiliation("emily-workum-northern-westchester-b1024", 8, "volunteer", "documented_prewar", "high_confidence", "medium", "D_correlative_or_secondary", "publish_qualified", organization_key=ORG_NORTHERN_WESTCHESTER, organization_name_as_found="Northern Westchester clinic at Mount Kisco", role_title="co-founder and volunteer", start_date="1935", date_precision="The biographical entry says she co-founded the clinic in 1935 and describes long-term volunteer service; it does not establish the OSS transition.", city="Mount Kisco", state_or_region="New York", country="United States", immediate_pre_oss=False, last_civilian_pre_service=False, research_notes="Qualified volunteer affiliation only; it is not recast as paid employment or an immediate OSS predecessor."),
        affiliation("emily-workum-actress-b1024", 8, "unknown", "documented_prewar", "high_confidence", "medium", "D_correlative_or_secondary", "publish_qualified", occupation="actress", end_date="1931-02", date_precision="The biographical entry describes stage work before her February 1931 marriage; no employer or company is named.", country="United States", immediate_pre_oss=False, last_civilian_pre_service=False, research_notes="Earlier occupation only. Productions named in the biography are not silently converted into employers."),
        affiliation("edwin-wright-columbia-student-b1024", 35, "student", "strongly_date_bounded", "probable", "medium", "B_authoritative_institutional", "publish_qualified", organization_key=ORG_COLUMBIA, organization_name_as_found="Columbia", role_title="doctoral student", occupation="doctoral research in Middle Eastern studies", start_date="1937", end_date="1941", date_precision="Wright's oral history dates doctoral work to 1937-1941 and then describes OSS recruitment when wartime demand arose.", city="New York", state_or_region="New York", country="United States", immediate_pre_oss=True, last_civilian_pre_service=False, research_notes="Best-supported immediate affiliation is student status, not employment by Columbia. The common-name index match remains probable pending personnel-file confirmation."),
        affiliation("edwin-wright-iran-educator-b1024", 35, "unknown", "documented_prewar", "probable", "medium", "B_authoritative_institutional", "publish_qualified", role_title="principal of several high schools", occupation="educator and school principal", start_date="1921", end_date="1937", date_precision="The oral history dates educational work in Tabriz, Rasht and Hamadan from 1921 to 1937 but does not name the schools.", country="Iran", immediate_pre_oss=False, last_civilian_pre_service=False, research_notes="Documented earlier work with no named employer; Columbia study intervened before OSS recruitment."),
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
        disputed_initial = row == 22
        identity_confidence = "high" if disputed_initial else "confirmed"
        identity_assessment = "High confidence from a nonshared protected identifier despite the indexed E and Army F middle-initial conflict; the identifier remains private." if disputed_initial else "Confirmed by a nonshared protected identifier and exact official name agreement; the identifier remains private."
        source_links: list[dict[str, str]] = [
            {"source_key": INDEX, "locator_override": f"PDF page 514, row {row}; Box {PEOPLE[row][2]}"},
            {"source_key": ARMY},
            {"source_key": TECH, "support_type": "context_only"},
        ]
        if disputed_initial:
            source_links.append({"source_key": NARA_WRACHFORD, "support_type": "context_only"})
        values.append(claim(f"identity-{slug(name)}-b1024", row, "identity", f"Indexed {name} is {'a high-confidence match to' if disputed_initial else 'confirmed as'} the reviewed Army record.", "The official sources connect the records through a nonshared protected identifier; the George Wrachford middle-initial discrepancy remains visible." if disputed_initial else "The official sources agree through a nonshared protected identifier and exact name evidence.", identity_assessment, "Identity evidence only; Army entry is not treated as an exact OSS-transition date.", "A_direct_official", identity_confidence, source_links, "The review withholds the identifier and does not convert Army fields into a named employer."))
        values.append(claim(f"occupation-{slug(name)}-b1024", row, "occupation", f"At Army entry on {date}, {name}'s record carried historical civilian-occupation category {code}: {occupation}.", f"The official bulk record carries code {code}; NARA's compiled list labels that category '{label}'.", identity_assessment, "Strongly date-bounded at Army entry, but not proof of an immediate predecessor affiliation or exact OSS start date.", "A_direct_official", "medium", [{"source_key": ARMY}, {"source_key": TECH, "support_type": "context_only"}, {"source_key": CODES, "locator_override": locator}], "A historical category only; excluded from verified-employer analytics and never converted into a named employer.", "publish_qualified", f"{slug(name)}-army-occupation-b1024"))
    for row, (date, note) in ARMY_IDENTITY_ONLY.items():
        name = PEOPLE[row][1]
        values.append(claim(f"identity-{slug(name)}-b1024", row, "identity", f"Indexed {name} is confirmed as the reviewed Army record.", "The exact official name and a nonshared protected identifier connect the index and Army records.", "Confirmed by exact official name agreement and a nonshared protected identifier; the identifier remains private.", f"Army entry is dated {date}. {note}", "A_direct_official", "confirmed", [{"source_key": INDEX, "locator_override": f"PDF page 514, row {row}; Box {PEOPLE[row][2]}"}, {"source_key": ARMY}, {"source_key": TECH, "support_type": "context_only"}], "Identity only; no Army grade, occupation or post-OSS chronology is converted into pre-OSS evidence."))
    values.extend([
        claim("identity-emily-workum-b1024", 8, "identity", "Indexed Emily H Workum is high-confidence identified as Emily Hamill Workum of Bedford Village, New York.", "The Met's 1939-1940 object title and the biographical entry independently use the rare Emily Workum name and Bedford-area context.", "High confidence from the rare exact first and surname, compatible middle initial, Bedford context and mutually compatible institutional chronology; the personnel file remains unreviewed.", "The records document prewar activity but do not establish an OSS start date.", "B_authoritative_institutional", "high", [{"source_key": INDEX}, {"source_key": MET_WORKUM}, {"source_key": OCEANSPRINGS_WORKUM}], "The sources support qualified identity; no family relationship or later activity is used as a substitute for prewar evidence."),
        claim("northern-westchester-emily-workum-b1024", 8, "other_pre_oss_affiliation", "Emily Workum co-founded and volunteered with the Northern Westchester clinic at Mount Kisco beginning in 1935.", "The biographical entry dates the clinic's founding to 1935 and describes Workum's long volunteer service.", "High-confidence identity from the rare name and independent Bedford-area institutional record.", "Documented prewar volunteer affiliation; immediacy to OSS and paid status are not established.", "D_correlative_or_secondary", "medium", [{"source_key": OCEANSPRINGS_WORKUM}, {"source_key": MET_WORKUM, "support_type": "context_only"}], "Published with qualification as volunteer service, never as employment.", "publish_qualified", "emily-workum-northern-westchester-b1024"),
        claim("actress-emily-workum-b1024", 8, "occupation", "Emily Workum worked as an actress before her February 1931 marriage.", "The biographical entry describes roles in New York and Chicago before the marriage but names no employer or company.", "High-confidence identity from the rare name and independent Bedford-area institutional record.", "Earlier documented prewar occupation; not shown to be immediate to OSS.", "D_correlative_or_secondary", "medium", [{"source_key": OCEANSPRINGS_WORKUM}, {"source_key": MET_WORKUM, "support_type": "context_only"}], "Productions are not converted into employers; the claim remains qualified.", "publish_qualified", "emily-workum-actress-b1024"),
        claim("identity-edwin-wright-b1024", 35, "identity", "Indexed Edwin M Wright is probably the Middle East specialist interviewed by the Truman Library about his OSS Research and Analysis service.", "The official oral history uses the exact name and middle initial and gives a specific OSS recruitment chronology involving Persian-language research.", "Probable rather than high-confidence because the index row supplies no public corroborator beyond the common exact name; the personnel file remains unreviewed.", "The oral history explicitly covers education and employment before wartime OSS recruitment.", "B_authoritative_institutional", "medium", [{"source_key": INDEX}, {"source_key": TRUMAN_WRIGHT}], "The profile remains visibly qualified and excluded from default identity-dependent analytics."),
        claim("columbia-edwin-wright-b1024", 35, "immediate_pre_oss_affiliation", "Edwin M. Wright's best-supported immediate pre-OSS affiliation was doctoral study at Columbia University from 1937 through 1941.", "Wright dates his Columbia doctoral work to 1937-1941 and next describes OSS recruitment for Persian-language research.", "Probable index identity based on exact name and middle initial plus a specific official OSS self-report; the personnel file is still needed.", "Strongly date-bounded as the last documented status before OSS recruitment; the source does not give an exact joining date.", "B_authoritative_institutional", "medium", [{"source_key": TRUMAN_WRIGHT}], "Student status, not employment by Columbia; published with qualification.", "publish_qualified", "edwin-wright-columbia-student-b1024"),
        claim("educator-edwin-wright-b1024", 35, "occupation", "Edwin M. Wright worked as a school principal and educator in Iran from 1921 to 1937.", "The oral history dates educational work and principalships in Tabriz, Rasht and Hamadan but does not name the schools.", "Probable index identity based on exact name and middle initial plus a specific official OSS self-report.", "Documented earlier prewar work; Columbia doctoral study intervened before OSS recruitment.", "B_authoritative_institutional", "medium", [{"source_key": TRUMAN_WRIGHT}], "No unnamed school is invented as an employer, and the work is not marked immediate.", "publish_qualified", "edwin-wright-iran-educator-b1024"),
    ])
    return values


def unresolved_reason(row: int) -> str:
    reasons = {
        1: "A third-party memorial lead supplies life dates but no reliable OSS or pre-OSS employment bridge.",
        2: "A historical search result points to a Detachment 101 document naming Allen D. Wooten, but the original URL now redirects to unrelated content and no stable preserved copy was found; it is not used as final evidence.",
        4: "A school-administrator namesake could not be connected to the index row by two corroborating identifiers and is rejected.",
        18: "A prominent journalist namesake could not be bridged to the index row and is not assigned by name alone.",
        19: "A 1933 marriage lead lacks an OSS or protected-identifier bridge and is rejected as employment evidence.",
        24: "A historical search result points to a Detachment 101 document naming Edward F. Wrenn, but the original URL now redirects to unrelated content and no stable preserved copy was found; it is not used as final evidence.",
        44: "A 1948 San Francisco directory lead is postwar and unbridged, so it is not transferred to the indexed person.",
    }
    return reasons.get(row, "Accessible exact-name, official, OSS, employer, occupation, obituary, institutional, newspaper, directory and archival searches produced no reliable identity-and-affiliation bridge; unbridged namesakes and postwar-only leads were rejected.")


def base_update(row: int, **overrides: object) -> dict[str, object]:
    value: dict[str, object] = {"person_id": PEOPLE[row][0], "manual_review_required": True, "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "high"}
    value.update(overrides)
    return value


def person_updates() -> list[dict[str, object]]:
    special = set(ARMY_OCCUPATIONS) | set(ARMY_IDENTITY_ONLY) | {8, 35}
    values: list[dict[str, object]] = []
    for row in sorted(set(PEOPLE) - special):
        reason = unresolved_reason(row)
        values.append(base_update(row, identity_status="unresolved", identity_evidence=f"The visually verified page 514 source preserves {PEOPLE[row][1]} and Box {PEOPLE[row][2]}. {reason}", research_status="requires_archival_review", archival_review_priority="critical" if row in {2, 4, 18, 24} else "high", next_action=f"Review indexed Box {PEOPLE[row][2]} for corroborating identifiers, immediate pre-OSS affiliation and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}"))
    for row in ARMY_OCCUPATIONS:
        disputed_initial = row == 22
        updates: dict[str, object] = {
            "identity_status": "high_confidence" if disputed_initial else "confirmed",
            "identity_evidence": "A nonshared protected identifier connects the official records despite the indexed E and Army F middle-initial discrepancy; the identifier remains private." if disputed_initial else "A nonshared protected identifier and exact official name agreement connect the index and Army records; the identifier remains private.",
            "research_status": "occupation_only_found",
            "nara_catalog_id": "1263923",
            "next_action": f"Review indexed Box {PEOPLE[row][2]} to identify a named employer or institution and establish Army-to-OSS chronology; the bulk record supplies only a historical occupation category.",
        }
        if disputed_initial:
            updates["name_variants"] = ["George F Wrachford", "George Franklin Wrachford"]
            updates["replace_name_variants"] = False
        if row != 44:
            updates.update({"personnel_category": "enlisted_army_personnel", "commissioned_officer": False, "allied_or_foreign_personnel": False})
        values.append(base_update(row, **updates))
    values.extend([
        base_update(42, identity_status="confirmed", identity_evidence="A nonshared protected identifier and exact official name agreement connect the records; the dated Army entry is post-OSS and supports identity only.", research_status="requires_archival_review", nara_catalog_id="1263923", next_action="Review Box 854 for Kenneth M Wright's pre-OSS affiliation. The November 1945 Army entry is not used as pre-OSS evidence."),
        base_update(8, identity_status="high_confidence", identity_evidence="The rare exact name, compatible middle initial and independent Bedford-area institutional context support high confidence.", name_variants=["Emily Hamill Workum", "Emily Lyon Hamill Workum"], replace_name_variants=False, research_status="occupation_only_found", archival_review_priority="medium", next_action="Review Box 853 to confirm identity, determine whether any paid work followed her documented acting and volunteer roles, and establish the immediate OSS predecessor."),
        base_update(35, identity_status="probable", identity_evidence="The exact name and middle initial match an official oral history with a specific OSS Research and Analysis recruitment narrative; the common-name index row supplies no second public identifier.", name_variants=["Edwin M. Wright"], replace_name_variants=False, research_status="occupation_only_found", archival_review_priority="critical", next_action="Review Box 854 to confirm the common-name identity and the Columbia-to-OSS chronology; student status and earlier educational work are qualified pending that bridge."),
    ])
    if len(values) != 46:
        raise RuntimeError(f"Expected 46 person updates, generated {len(values)}")
    return values


def research_attempts() -> list[dict[str, object]]:
    attempts: list[dict[str, object]] = []
    substantiated = {8, 35} | set(ARMY_OCCUPATIONS) | set(ARMY_IDENTITY_ONLY)
    for row, (person_id, name, box) in PEOPLE.items():
        if row in substantiated:
            outcome = "source_reviewed"
            reviewed = 8 if row in {8, 35} else 6
            rejected = 4
            note = "At least one identity, occupation or affiliation outcome is preserved with claim-level citations; unresolved employer or temporal questions remain explicit."
        else:
            outcome = "candidate_rejected"
            reviewed = 5
            rejected = 4
            note = unresolved_reason(row)
        attempts.append({
            "key": f"page514-row{row}-{slug(name)}-b1024",
            "person_id": person_id,
            "source_adapter": "manual_staged_protocol",
            "query_text": f"{name}; NARA OSS index context; exact-name and meaningful initial, suffix, punctuation and OCR variants; OSS, rank, branch, assignment and protected-identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory and archival searches; indexed Box {box}",
            "query_variant_type": "staged_identity_employment_archival_protocol_batch_1024",
            "started_at": "2026-11-04T13:40:00Z",
            "completed_at": "2026-11-04T15:20:00Z",
            "outcome": outcome,
            "sources_reviewed": reviewed,
            "candidate_sources_rejected": rejected,
            "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, postwar-only leads and sources without an OSS, protected-identifier, rank, unit or personnel-file bridge were rejected. Army categories were not converted into named employers. A hijacked historical document URL was treated as discovery only and not cited as final evidence.",
            "research_notes": f"{note} The official index, exact-name searches, CIA or equivalent official context, and employer, occupation, obituary, institutional, newspaper, directory and archival leads were reviewed as applicable. Page 514 and every cited NARA code-list page were visually checked. No authenticated NARA Catalog API request was made.",
            "next_action": f"Review indexed Box {box} for corroborating identifiers, immediate pre-OSS affiliation and last civilian employer before wartime service.",
            "attempt_number": 1,
            "research_agent_version": "before-oss-b1024-v1",
        })
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-1024-v1",
        "reviewer": "Before OSS Batch 1024 evidence review",
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
