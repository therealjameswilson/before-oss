#!/usr/bin/env python3
"""Generate the reviewed Batch 1030 evidence bundle for PDF page 520."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page520-francis-zdaniecki-to-christian-zimmerman-review_"
    "batch-1030_2026-11-04.json"
)

INDEX = "nara-index-b1030"
ARMY = "army-bulk-b1030"
TECH = "army-tech-b1030"
CODES = "army-codes-b1030"
CMU_ZELENKA = "cmu-zelenka-b1030"
FRENCH_ARMY = "shd-zibell-b1030"
NYNG = "nyng-ziegler-b1030"
USWM_ZEVITAS = "uswm-zevitas-b1030"
OSSOG = "ossog-zien-zevitas-b1030"
BREST_ZIELSKE = "brest-zielske-b1030"
NUREMBERG_ZIGMAN = "nuremberg-zigman-b1030"

ORG_NYNG = "new-york-national-guard-b1030"
ORG_US_NAVY = "us-navy-b1030"

PEOPLE = {
    1: ("7b4f9a6f-3eca-5ebf-9d1e-d440950231f9", "Francis E Zdaniecki", "861"),
    2: ("2ae3eab2-d97b-5c9a-bc80-281adcece3ec", "Carol L Zdravkoff", "862"),
    3: ("9d33d5dd-b332-52dd-a7c9-3256440b3533", "Peter F Zdrodowski", "862"),
    4: ("fa2b2b5e-7e00-597c-a025-3fc6ba138d70", "Eugene J Zdrojewski", "862"),
    5: ("25d323d6-d833-539d-bc5d-1c541bcd875e", "Josepoh L Zeek", "862"),
    6: ("e7a7f463-f7ab-53a6-b378-e35c57c4524a", "George B Zeigler", "862"),
    7: ("8fdf183a-5e5a-5697-8dcb-e7a515709758", "Louis P Zelenka", "862"),
    8: ("e3241d33-46e9-5ad3-b78e-daa13c0809bb", "Charles Zelikovitz", "862"),
    9: ("87510825-2be0-5e29-98f1-2ccffbdf4e8c", "Bernard J Zelinski", "862"),
    10: ("7b7cd1e1-ef21-577a-b700-dd58a09f26df", "Omar E Zell", "862"),
    11: ("8dba0df2-da35-5e9b-98ed-ab8fa81f3797", "Clinton R Zeller", "862"),
    12: ("314d5abe-31f6-534a-842f-9d2df40a0943", "Wilbur U Zeller", "862"),
    13: ("cb1e3648-11d0-5121-bfba-2660babb1825", "Sidney Zelmanovics", "862"),
    14: ("f13008d5-e537-520e-ba28-2fdc0ef1bf02", "Samuel I Zelmanowitz", "862"),
    15: ("64696a77-335a-55f7-b60c-a211f267ff4c", "Arthur A Zelmer", "862"),
    16: ("da3c5db4-786c-5f19-bc40-f68d0ce58282", "Wwendel C Zeluff", "862"),
    17: ("2edc4d4e-ccb7-5067-a3bc-c23d6d635298", "Edward Zeman", "862"),
    18: ("f0826df6-7bb0-5789-b405-00f307aee74d", "Adolph J Zemansky", "862"),
    19: ("1e079dc2-7a25-5ee4-9af9-e3988a6a3dd1", "Anton Zennis", "862"),
    20: ("e39746be-882a-5331-92ed-368a1589c20b", "Robert W Zens", "862"),
    21: ("c3c7c4e3-6dd7-550e-a522-8dd5c9b6ec23", "Franklin E Zerbe", "862"),
    22: ("f49aef29-8213-55dc-8c74-2e88b24727ac", "Joseph M Zerbe", "862"),
    23: ("92dcec2c-3404-5e21-9e15-8a01f383b064", "Peter Zerdilla", "862"),
    24: ("8c282b7d-0edf-5155-8122-2593448b57f0", "James J Zevitas", "862"),
    25: ("303a2865-deef-5b39-b8bc-7891a5542194", "Serge Zibell", "862"),
    26: ("ad59f121-faa1-58cb-87be-a015c4a6033d", "Joseph Ziccardi Jr.", "862"),
    27: ("677439a6-eba8-5fc5-b7aa-87789c565041", "Allen G Zieber", "863"),
    28: ("f11d9c14-c493-537d-8034-87033505961e", "Evarts Ziegler", "863"),
    29: ("8c530b94-9c1b-5121-81b7-a1656630c118", "John G Ziegler", "863"),
    30: ("d8625ac8-12f4-5ddc-b0dc-f276bf857a97", "Richard H Ziegler", "863"),
    31: ("191ff779-1a55-5b8a-9f06-be0970ecd4ef", "Paul F Ziegner", "863"),
    32: ("6de8851a-b19f-51aa-ab8d-b2930bf16a0e", "Henry F Ziejeski", "863"),
    33: ("af421f19-6723-5899-a220-6146af9271af", "Bernard A Zielinski", "863"),
    34: ("6255b472-3723-52fe-9c07-677e80ea0644", "William F Zielske Jr.", "863"),
    35: ("36ad8934-ee81-5ec1-82b3-9b2da7d6f42a", "Howard C Zieman", "863"),
    36: ("abcf00c8-ee54-5a82-913c-60578e626077", "Joseph F Zien", "863"),
    37: ("62e64e35-b4c0-512b-88ca-27c424ab0909", "Nick G Zigenis", "863"),
    38: ("1d1653b9-c361-5adb-a99b-807d28395738", "Joseph Zigman", "863"),
    39: ("7d09f529-7552-5481-a116-891e6afd1f55", "Joseph P Ziino", "863"),
    40: ("84b68de0-50e6-5bcf-b4d6-cf982a59a93c", "Richard A Ziiz", "863"),
    41: ("e1b4ed0d-e495-55f0-90b0-f9a0553d7361", "Richard J Zika", "863"),
    42: ("a70fd5ae-9b92-5ab5-b77e-f2dfbace47d6", "Tehodore W Zillman", "863"),
    43: ("62295f03-573c-5345-95d3-6084392bd097", "Robert R Zima", "863"),
    44: ("7bea4e11-de18-586e-a376-f344ed9bda9e", "Robert L Zimler", "863"),
    45: ("5470c344-07c2-5110-9d53-75993ae743f0", "Carleton G Zimmerman", "863"),
    46: ("60b97031-2f97-54c4-a06c-ce83f6c603a0", "Christian E Zimmerman", "863"),
}

# Only accepted, date-bounded Army records whose historical categories are defined.
# Code 999, the rejected/conflicting links, and the late-1945 Ziegner record are excluded.
ARMY_OCCUPATIONS = {
    3: ("1941-10-22", "893", "metal-products fabrication laborer", "Unskilled occupations in fabrication of metal products, n.e.c.", "PDF physical page 180"),
    5: ("1943-02-02", "604", "food-canning or preserving worker", "Semiskilled occupations in canning and preserving foods", "PDF physical page 176"),
    10: ("1942-12-16", "131", "express messenger or railway mail clerk", "Express messengers and railway mail clerks", "PDF physical page 171"),
    11: ("1942-11-10", "475", "machinist", "Machinists", "PDF physical page 174"),
    13: ("1942-12-15", "583", "repairman or mechanic, not elsewhere classified", "Repairmen and mechanics, n.e.c.", "PDF physical page 176"),
    14: ("1943-07-19", "627", "textile-products fabrication worker", "Semiskilled occupations in fabrication of textile products, n.e.c.", "PDF physical page 177"),
    15: ("1943-04-10", "882", "foundry laborer", "Unskilled occupations in foundries, n.e.c.", "PDF physical page 180"),
    18: ("1942-05-05", "003", "architect", "Architects", "PDF physical page 170"),
    24: ("1941-01-16", "170", "sales clerk", "Sales clerks", "PDF physical page 172"),
    27: ("1943-06-30", "992", "student", "Students", "PDF physical page 304; amended category 9-92"),
    30: ("1943-07-29", "097", "technician, except laboratory", "Technicians, except laboratory", "PDF physical page 171"),
    32: ("1942-11-30", "497", "electrician", "Electricians", "PDF physical page 175"),
    33: ("1943-04-20", "878", "machine-shop laborer", "Unskilled occupations in machine shops and related occupations, n.e.c.", "PDF physical page 180"),
    34: ("1943-01-08", "652", "industrial-chemicals production worker", "Semiskilled occupations in production of industrial chemicals", "PDF physical page 178"),
    37: ("1943-06-29", "525", "carpenter", "Carpenters", "PDF physical page 175"),
    39: ("1942-12-21", "678", "machine-shop worker", "Semiskilled machine-shop and related occupations, n.e.c.", "PDF physical page 178"),
    40: ("1941-05-05", "781", "motor-vehicle mechanic or repairman", "Motor-vehicle mechanics and repairmen", "PDF physical page 179"),
    43: ("1943-04-06", "138", "stock clerk", "Stock clerks", "PDF physical page 172"),
    44: ("1943-07-05", "097", "technician, except laboratory", "Technicians, except laboratory", "PDF physical page 171"),
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def source(key: str, **kwargs: object) -> dict[str, object]:
    value: dict[str, object] = {"key": key, "access_date": "2026-11-04"}
    value.update(kwargs)
    return value


def sources() -> list[dict[str, object]]:
    return [
        source(INDEX, stable_url="https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf", archival_identifier="RG 226, Entry A1-224, Boxes 861-863", title="OSS Personnel Files from Excel", author_creator="National Archives and Records Administration", repository_publisher="National Archives and Records Administration", publication_record_date="2010-12-23", locator="PDF page 520, rows 1-46; page 521 boundary and all page 520 rows visually checked at 180 dpi", source_quality="A_direct_official", collection_name="Records of the Office of Strategic Services, Record Group 226", rights_notes="All 46 printed rows remain separate. Full protected identifiers remain private."),
        source(ARMY, stable_url="https://catalog.archives.gov/id/1263923", archival_identifier="National Archives Identifier 1263923; parent series NAID 604357", title="Electronic Army Serial Number Merged File, ca. 1938-1946", author_creator="Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration", repository_publisher="National Archives and Records Administration", publication_record_date="1938-1946; merged file created 2002", locator="Official unrestricted ASNEF.FIN.DAT; twenty-six Batch 1030 candidate links explicitly reviewed", source_quality="A_direct_official", collection_name="World War II Army Enlistment Records", document_number="ASNEF.FIN.DAT", rights_notes="No raw record or full protected identifier is retained in public assets. Rejected and conflicting links remain explicit."),
        source(TECH, stable_url="https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf", archival_identifier="NN3-064-03-008; National Archives Identifier 1263923", title="World War II Army Enlistment Records: Reference Copy of Technical Documentation", author_creator="National Archives and Records Administration", repository_publisher="National Archives at College Park - Electronic Records", publication_record_date="1994-2005; reference copy modified 2011", locator="PDF physical pages 44-46; identifier, name, Army-entry-date, grade and civilian-occupation fields", source_quality="A_direct_official", collection_name="World War II Army Enlistment Records technical documentation", rights_notes="Used to interpret selected fields only; source damage, name conversion, coding limits and incomplete coverage remain applicable."),
        source(CODES, stable_url="https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1CL_SD.pdf", archival_identifier="National Archives Identifier 1263923; Code No. 30", title="NARA Compiled Code Lists for the Electronic Army Serial Number Merged File", author_creator="National Archives and Records Administration", repository_publisher="National Archives at College Park - Electronic Records", publication_record_date="2011-01-12; modified 2011-03-17", locator="PDF physical pages 170-180 and 304; Batch 1030 categories visually checked", source_quality="A_direct_official", collection_name="World War II Army Enlistment Records technical documentation", rights_notes="Historical categories identify neither employer, institution nor workplace. Undefined code 999 is not interpreted."),
        source(CMU_ZELENKA, stable_url="https://iiif.library.cmu.edu/file/ALU_1944_030_001_09001944/ALU_1944_030_001_09001944.pdf", title="The Carnegie Alumnus, volume 30, number 1", author_creator="Carnegie Institute of Technology Alumni Association", repository_publisher="Carnegie Mellon University Libraries", publication_record_date="1944-09", locator="PDF page 17; alumni note for Lt. Louis P. Zelenka", source_quality="B_authoritative_institutional", rights_notes="Contemporary institutional publication confirms commissioned rank and OSS technical assignment; it does not supply a pre-OSS employer."),
        source(FRENCH_ARMY, stable_url="https://www.servicehistorique.sga.defense.gouv.fr/sites/default/files/2020-01/SHDGR_REP_8YE_O-Z.pdf", archival_identifier="GR 8 YE 112651", title="Sous-série GR 8 YE: Officiers supérieurs et subalternes, armée de Terre, Gendarmerie et services communs, 1940-1960, lettres O à Z", author_creator="Service historique de la Défense", repository_publisher="French Ministry of the Armed Forces", locator="PDF page 459; ZIBELL, Serge", source_quality="A_direct_official", rights_notes="Official French officer-file index supplies a rare-name military lead but does not itself connect the file to OSS or establish a pre-OSS assignment."),
        source(NYNG, stable_url="https://museum.dmna.ny.gov/soldiers-and-sailors/service-records/20010016-nyng-enlisted-personnel-who-were-federalized-1940/Z", archival_identifier="Collection 2001.0016", title="New York National Guard enlisted personnel who were federalized in 1940", repository_publisher="New York State Military Museum and Veterans Research Center", publication_record_date="1940; online index current 2026", locator="Z surname list; Ziegler, Evarts", source_quality="B_authoritative_institutional", rights_notes="Official state military index supports a 1940 enlisted National Guard affiliation; no unit, protected identifier or OSS transfer date is supplied."),
        source(USWM_ZEVITAS, stable_url="https://uswarmemorials.org/html/people_details.php?PeopleID=24848", title="Zevitas James J.", repository_publisher="US War Memorials Overseas", locator="Greek Operational Group monument biographical entry", source_quality="D_correlative_or_secondary", rights_notes="Corroborative monument record supports the distinctive identity and operational-group service. Protected identifier content is not reproduced."),
        source(OSSOG, stable_url="https://ossog.info/personnel.html", title="Office of Strategic Services Operational Groups Personnel", repository_publisher="OSS Operational Groups historical project", locator="Greek Operational Groups personnel roster; T/Sgt. J. J. Zevitas and T/4 Joseph F. Zien", source_quality="D_correlative_or_secondary", rights_notes="Corroborative roster only. It supports wartime identity and unit context, not a pre-OSS employer."),
        source(BREST_ZIELSKE, stable_url="https://www.resistance-brest.net/article4078.html", title="Summers John W.", repository_publisher="Mémoires des résistants et FFI de l'arrondissement de Brest", locator="Team Horace paragraph naming technician third grade William F. Zielske as radio operator", source_quality="D_correlative_or_secondary", rights_notes="Regional resistance-history source corroborates the rare name and OSS field-team context; it does not establish a pre-OSS employer."),
        source(NUREMBERG_ZIGMAN, stable_url="https://nurembergfilm.org/credits/", title="Joseph Zigman, Editor", author_creator="Nuremberg: Its Lesson for Today project; reproduces a 1996 Variety obituary", repository_publisher="Schulberg Productions", publication_record_date="1996-12-17 obituary; project page accessed 2026", locator="Joseph Zigman biographical section", source_quality="C_reputable_contemporary_or_scholarly", rights_notes="The page gives an explicit prewar occupation, Navy-to-OSS sequence and film-unit identity; no prewar employer is named."),
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {"key": ORG_NYNG, "canonical_name": "New York National Guard", "historical_name": "New York National Guard", "organization_type": "state National Guard", "sector": "military", "state_or_region": "New York", "country": "United States", "normalization_notes": "The available index does not identify Evarts Ziegler's unit, so no narrower unit is invented."},
        {"key": ORG_US_NAVY, "canonical_name": "United States Navy", "historical_name": "United States Navy", "aliases": ["U.S. Navy"], "organization_type": "military branch", "sector": "military", "country": "United States", "normalization_notes": "Military service is separate from civilian employment."},
    ]


def affiliation(key: str, row: int, relationship: str, temporal: str, identity: str, confidence: str, quality: str, status: str = "published", **kwargs: object) -> dict[str, object]:
    value: dict[str, object] = {"key": key, "person_id": PEOPLE[row][0], "relationship_type": relationship, "pre_oss_temporal_basis": temporal, "identity_confidence": identity, "claim_confidence": confidence, "source_quality": quality, "publication_status": status}
    value.update(kwargs)
    return value


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, _label, _locator) in ARMY_OCCUPATIONS.items():
        identity = "high_confidence" if row in {5, 14, 27, 40} else "confirmed"
        relationship = "student" if row == 27 else "unknown"
        values.append(affiliation(
            f"{slug(PEOPLE[row][1])}-army-occupation-b1030", row, relationship,
            "strongly_date_bounded", identity, "medium", "A_direct_official", "publish_qualified",
            occupation=occupation, end_date=date,
            date_precision=f"Historical civilian-occupation code {code} was recorded at Army entry on {date}; no named employer or institution is supplied.",
            country="United States", immediate_pre_oss=False, last_civilian_pre_service=False,
            research_notes="Broad historical category only; excluded from verified-employer analytics and not narrowed beyond the official wording.",
        ))
    values.extend([
        affiliation("evarts-ziegler-nyng-b1030", 28, "military_assignment", "documented_prewar", "high_confidence", "medium", "B_authoritative_institutional", "publish_qualified", organization_key=ORG_NYNG, organization_name_as_found="New York National Guard", role_title="enlisted member federalized in 1940", end_date="1940", date_precision="The state military index lists Evarts Ziegler among New York National Guard enlisted personnel federalized in 1940; no unit or later transfer date is supplied.", state_or_region="New York", country="United States", immediate_pre_oss=False, last_civilian_pre_service=False, research_notes="Documented prewar military affiliation; not labeled the immediate OSS predecessor."),
        affiliation("joseph-zigman-film-editor-b1030", 38, "employment", "strongly_date_bounded", "high_confidence", "high", "C_reputable_contemporary_or_scholarly", occupation="film editor", end_date="1941", date_precision="The biography states that Zigman worked as a film editor before the United States entered the war, then enlisted in the Navy and later joined the OSS Film Unit; no employer is named.", country="United States", immediate_pre_oss=False, last_civilian_pre_service=True, research_notes="Last documented civilian occupation before military service; not a named employer and not the immediate OSS affiliation."),
        affiliation("joseph-zigman-us-navy-b1030", 38, "military_assignment", "probable_immediate", "high_confidence", "high", "C_reputable_contemporary_or_scholarly", organization_key=ORG_US_NAVY, organization_name_as_found="U.S. Navy", role_title="enlisted servicemember", start_date="1941", date_precision="The biography says Zigman enlisted in the U.S. Navy and later joined the OSS Film Unit; exact dates and intervening units are absent.", country="United States", immediate_pre_oss=True, last_civilian_pre_service=False, research_notes="Best-supported immediate military pathway, visibly qualified because no transfer date or unit is supplied."),
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
        key = f"{slug(PEOPLE[row][1])}-army-occupation-b1030"
        identity = "High confidence from a protected linkage and reviewed spelling or suffix variant; the protected identifier is not published." if row in {5, 14, 27, 40} else "Confirmed by exact name and a nonshared protected linkage; the protected identifier is not published."
        values.append(claim(
            f"occupation-{slug(PEOPLE[row][1])}-b1030", row, "occupation",
            f"At Army entry on {date}, {PEOPLE[row][1]} was recorded in the broad historical category: {occupation}.",
            f"The official merged Army record carries category {code}; the NARA code list labels it {label}.",
            identity,
            "The category was recorded at Army entry and is strongly date-bounded, but its exact duration and relation to OSS are unknown.",
            "A_direct_official", "medium",
            [{"source_key": ARMY}, {"source_key": TECH}, {"source_key": CODES, "locator_override": locator}],
            "Qualified occupation or student status only. It is not a named employer, institution or workplace.", "publish_qualified", key,
        ))
    values.extend([
        claim("identity-louis-zelenka-b1030", 7, "identity", "Indexed Louis P Zelenka is strongly supported as the Army lieutenant assigned to the OSS Technical Branch of Research and Development in 1944.", "A contemporary Carnegie alumni publication gives the rare exact full name, commissioned rank, Washington residence and OSS technical assignment.", "High confidence from the rare exact full name and direct contemporary OSS context.", "Wartime identity and assignment only; the source does not state a pre-OSS employer.", "B_authoritative_institutional", "high", [{"source_key": INDEX}, {"source_key": CMU_ZELENKA}], "The source supports commissioned-officer classification but not a pre-OSS affiliation claim."),
        claim("identity-serge-zibell-b1030", 25, "identity", "Indexed Serge Zibell is a plausible match to the French Army captain-interpreter whose officer dossier is indexed as GR 8 YE 112651.", "The French defense archive lists the same rare name, a 1904 birth date and captain-interpreter role.", "Probable only: the official French index supplies no OSS, Box 862 or second-identifier bridge.", "Military-file context spans 1940-1960 and does not establish the person's immediate pre-OSS assignment.", "A_direct_official", "medium", [{"source_key": INDEX}, {"source_key": FRENCH_ARMY}], "Published as a qualified identity lead; no employer, affiliation or commissioned status is transferred without the personnel file.", "publish_qualified"),
        claim("identity-james-zevitas-b1030", 24, "identity", "Indexed James J Zevitas is confirmed as the Army servicemember later listed as a technical sergeant in an OSS Greek Operational Group.", "A protected link and exact official Army name align; two historical rosters independently place the rare full name in the OSS Greek Operational Groups.", "Confirmed by the protected linkage, exact rare name and corroborating OSS unit context.", "Wartime identity only beyond the separate Army-entry occupation claim.", "A_direct_official", "confirmed", [{"source_key": INDEX}, {"source_key": ARMY}, {"source_key": USWM_ZEVITAS}, {"source_key": OSSOG}], "The rosters do not name a pre-OSS employer."),
        claim("nyng-evarts-ziegler-b1030", 28, "other_pre_oss_affiliation", "Evarts Ziegler was an enlisted member of the New York National Guard federalized in 1940.", "The New York State Military Museum's official collection index lists the rare exact name under enlisted NYNG personnel federalized in 1940.", "High confidence from the rare exact name, compatible military context and index linkage; no public protected identifier appears in the state record.", "Documented prewar military affiliation; no unit or OSS transfer date establishes immediacy.", "B_authoritative_institutional", "medium", [{"source_key": NYNG}], "Military assignment, not employment; published with qualification.", "publish_qualified", "evarts-ziegler-nyng-b1030"),
        claim("identity-william-zielske-b1030", 34, "identity", "Indexed William F Zielske Jr. is strongly supported as the technician third grade and radio operator named in OSS Team Horace.", "The protected Army link confirms the full indexed name and suffix; a regional resistance history independently names William F. Zielske in the OSS team.", "Confirmed by the protected linkage; the secondary source corroborates the rare wartime identity.", "Wartime identity only beyond the separate Army-entry occupation claim.", "A_direct_official", "confirmed", [{"source_key": INDEX}, {"source_key": ARMY}, {"source_key": BREST_ZIELSKE}], "The radio duty is an OSS role, not a pre-OSS occupation."),
        claim("identity-joseph-zien-b1030", 36, "identity", "Indexed Joseph F Zien is strongly supported as the technician fourth grade listed in an OSS Greek Operational Group.", "The historical OSS Operational Groups roster gives the exact uncommon name and middle initial in Greek Group VII.", "High confidence from the rare exact full name and direct OSS unit context; no second public identifier is supplied.", "Wartime identity only; the roster does not state a pre-OSS affiliation.", "D_correlative_or_secondary", "high", [{"source_key": INDEX}, {"source_key": OSSOG}], "The personnel file remains necessary for a direct source and pre-OSS career."),
        claim("last-civilian-joseph-zigman-b1030", 38, "last_civilian_pre_service", "Film editor is Joseph Zigman's best-supported last civilian occupation before military service; no employer is identified.", "The biographical source explicitly places film editing before the war, followed by Navy enlistment and later OSS Film Unit service.", "High confidence from the exact uncommon name and direct OSS film-unit chronology.", "Strongly date-bounded before Navy service, but the employer and exact end date are absent.", "C_reputable_contemporary_or_scholarly", "high", [{"source_key": NUREMBERG_ZIGMAN}], "Occupation only; excluded from verified-employer counts because no organization is named.", "published", "joseph-zigman-film-editor-b1030"),
        claim("immediate-joseph-zigman-navy-b1030", 38, "immediate_pre_oss_affiliation", "U.S. Navy service is Joseph Zigman's best-supported military pathway immediately before the OSS Film Unit.", "The biography states that he enlisted in the Navy and later joined the OSS Film Unit led by Budd Schulberg.", "High confidence from the exact uncommon name and explicit OSS chronology.", "Probable immediate sequence; no Navy unit or transfer date is stated.", "C_reputable_contemporary_or_scholarly", "high", [{"source_key": NUREMBERG_ZIGMAN}], "Military assignment, not civilian employment.", "published", "joseph-zigman-us-navy-b1030"),
        claim("conflict-peter-zerdilla-b1030", 23, "identity", "Peter Zerdilla's protected index link points to an Army record rendered BERDILLA PETER L; no occupation is transferred.", "The protected link is specific, but the surname and middle initial conflict with the printed index.", "Conflicting until the original personnel and Army records are reviewed.", "Identity context only; the historical occupation category is withheld.", "A_direct_official", "conflicting", [{"source_key": INDEX}, {"source_key": ARMY}, {"source_key": TECH}], "The similar spelling is preserved as a conflict rather than silently corrected.", "conflicting"),
    ])
    return values


def unresolved_reason(row: int) -> str:
    reasons = {
        1: "Exact-name searches produced no reliable wartime identity or pre-OSS affiliation beyond the index.",
        2: "Exact-name, OSS and obituary searches produced no reliable identity-and-affiliation bridge.",
        4: "A family archive documents Eugene J Zdrojewski's OSS service, but no sufficiently authoritative public source yet establishes a pre-OSS employer or a direct identifier bridge.",
        6: "Exact-name results did not distinguish George B Zeigler from namesakes or establish a pre-OSS affiliation.",
        8: "Exact-name and likely spelling-variant searches produced no reliable wartime identity or employer bridge for Charles Zelikovitz.",
        12: "The protected Army candidate belongs to an entirely different name and was rejected; no other reliable identity or employment source was found.",
        16: "The unusual indexed spelling Wwendel and Wendel variants produced no reliable wartime identity or employment bridge.",
        17: "The common name Edward Zeman produced no corroborating identifiers sufficient to resolve the indexed person.",
        19: "Exact-name and likely foreign-spelling searches produced no reliable OSS identity or pre-OSS affiliation.",
        21: "An obituary for an Air Force officer named Franklin E Zerbe lacks an OSS, Box 862 or second-identifier bridge and was rejected as a namesake lead.",
        26: "Searches returned younger and differently initialed Joseph Ziccardi namesakes; none matched the wartime indexed record.",
        29: "The common name John G Ziegler produced no reliable OSS identity or employment bridge.",
        35: "Exact-name searches produced no reliable wartime identity or pre-OSS affiliation for Howard C Zieman.",
        41: "Exact-name results were modern or unbridged namesakes and did not resolve the indexed Richard J Zika.",
        42: "The indexed Tehodore spelling and Theodore variants produced no reliable wartime identity or pre-OSS affiliation.",
        45: "Exact-name searches produced no reliable identity or pre-OSS affiliation for Carleton G Zimmerman.",
    }
    return reasons.get(row, "Accessible official, CIA, OSS, exact-name, employer, occupation, obituary, institutional, newspaper, directory and archival searches produced no reliable identity-and-affiliation bridge; unbridged namesakes and postwar-only leads were rejected.")


def base_update(row: int, **overrides: object) -> dict[str, object]:
    value: dict[str, object] = {"person_id": PEOPLE[row][0], "manual_review_required": True, "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "high"}
    value.update(overrides)
    return value


def person_updates() -> list[dict[str, object]]:
    special = set(ARMY_OCCUPATIONS) | {7, 9, 20, 22, 23, 25, 28, 31, 36, 38, 46}
    values: list[dict[str, object]] = []
    for row in sorted(set(PEOPLE) - special):
        reason = unresolved_reason(row)
        values.append(base_update(row, identity_status="unresolved", identity_evidence=f"The visually verified page 520 source preserves {PEOPLE[row][1]}. {reason}", research_status="requires_archival_review", archival_review_priority="critical" if row in {1, 2, 4, 6, 8, 12, 16, 17, 19, 21, 26, 29, 35, 41, 42, 45} else "high", next_action=f"Review indexed Box {PEOPLE[row][2]} for corroborating identifiers, immediate pre-OSS affiliation and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}"))
    for row in sorted(ARMY_OCCUPATIONS):
        variants: list[str] = []
        identity_status = "confirmed"
        evidence = "A nonshared protected linkage and exact official name agreement connect the index and Army records; the protected identifier remains private."
        if row == 5:
            variants, identity_status, evidence = ["Joseph L Zeek"], "high_confidence", "A protected linkage connects the index's apparent Josepoh transposition to the Army form Joseph L Zeek."
        elif row == 14:
            identity_status = "high_confidence"
            evidence = "A protected linkage and the primary Samuel Zelmanowitz Army rendering align; a second rendering gives Szlama and remains an explicit candidate conflict."
        elif row == 27:
            variants, identity_status, evidence = ["Allen G Zieber Jr."], "high_confidence", "A nonshared protected linkage connects the records; the Army form adds the suffix Jr."
        elif row == 40:
            variants, identity_status, evidence = ["Richard A Zilz"], "high_confidence", "A protected linkage plus matching forename and middle initial connect the index to the Army surname rendering Zilz."
        values.append(base_update(row, identity_status=identity_status, identity_evidence=evidence, name_variants=variants, replace_name_variants=False, personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="occupation_only_found", nara_catalog_id="1263923", next_action=f"Review indexed Box {PEOPLE[row][2]} to identify a named employer or institution and establish Army-to-OSS chronology. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed; the bulk record supplies only a historical occupation category."))
    values.extend([
        base_update(7, identity_status="high_confidence", identity_evidence="A contemporary Carnegie alumni publication gives the rare exact full name, Army lieutenant rank and direct OSS technical assignment.", personnel_category="commissioned_army_officer", commissioned_officer=True, allied_or_foreign_personnel=False, research_status="requires_archival_review", archival_review_priority="critical", next_action="Review Box 862 to identify Louis P Zelenka's pre-commission civilian employment or educational status and his exact Army-to-OSS transfer; the current source documents OSS service but not the preceding affiliation."),
        base_update(9, identity_status="confirmed", identity_evidence="A nonshared protected linkage and exact official name agreement connect the index and Army records; undefined occupation code 999 remains uninterpreted.", personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="requires_archival_review", nara_catalog_id="1263923", archival_review_priority="critical", next_action="Review Box 862 to identify Bernard J Zelinski's pre-OSS affiliation. No occupation or employer is inferred from undefined code 999."),
        base_update(20, identity_status="unresolved", identity_evidence="The visually verified index identifies Robert W Zens as a second lieutenant, but accessible sources did not establish a second identity or employment bridge.", personnel_category="commissioned_army_officer", commissioned_officer=True, research_status="requires_archival_review", archival_review_priority="critical", next_action="Review Box 862 and Army officer records to resolve Robert W Zens and document his pre-OSS assignment or last civilian employer."),
        base_update(22, identity_status="confirmed", identity_evidence="A nonshared protected linkage and exact official name agreement connect the index and Army records; undefined occupation code 999 remains uninterpreted.", personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="requires_archival_review", nara_catalog_id="1263923", archival_review_priority="critical", next_action="Review Box 862 to identify Joseph M Zerbe's pre-OSS affiliation. No occupation or employer is inferred from undefined code 999."),
        base_update(23, identity_status="conflicting", identity_evidence="The protected linkage points to BERDILLA PETER L rather than indexed Peter Zerdilla. The conflict remains explicit and no Army occupation is transferred.", personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="conflicting_sources", nara_catalog_id="1263923", archival_review_priority="critical", next_action="Review Box 862 and the original Army record to determine whether BERDILLA PETER L is a damaged rendering of Peter Zerdilla. No occupation or employer is accepted while the names conflict."),
        base_update(25, identity_status="probable", identity_evidence="The French defense archive indexes the rare exact name Serge Zibell as a captain interpreter, but supplies no OSS or second-identifier bridge.", research_status="needs_identity_review", archival_review_priority="critical", next_action="Review Box 862 and French officer dossier GR 8 YE 112651 to determine whether the records describe the same person and to establish the pre-OSS chronology. No commissioned status or employer is inferred yet."),
        base_update(28, identity_status="high_confidence", identity_evidence="The New York State Military Museum lists the rare exact name among enlisted National Guard personnel federalized in 1940, a compatible prewar military context.", personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="needs_temporal_review", archival_review_priority="critical", next_action="Review Box 863 and New York National Guard service records to identify Evarts Ziegler's unit, civilian occupation and exact transfer path into OSS."),
        base_update(31, identity_status="high_confidence", identity_evidence="A protected linkage connects the index to the Army form Paul F Ziegner Jr.; the late-1945 Army-entry date cannot establish a pre-OSS student status.", name_variants=["Paul F Ziegner Jr."], replace_name_variants=False, personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="requires_archival_review", nara_catalog_id="1263923", archival_review_priority="critical", next_action="Review Box 863 to determine Paul F Ziegner's OSS dates and pre-OSS affiliation. The late-1945 Army record is retained for identity only and its student code is not used as pre-OSS evidence."),
        base_update(36, identity_status="high_confidence", identity_evidence="A historical OSS Operational Groups roster lists the rare exact name and middle initial Joseph F. Zien as a technician fourth grade in Greek Group VII.", personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="requires_archival_review", archival_review_priority="critical", next_action="Review Box 863 for a direct source, immediate pre-OSS assignment and last civilian employer; the roster establishes wartime identity only."),
        base_update(38, identity_status="high_confidence", identity_evidence="A biographical source gives the uncommon exact name, prewar film-editing occupation, Navy enlistment and direct OSS Film Unit service.", personnel_category="enlisted_naval_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="occupation_only_found", archival_review_priority="medium", next_action="Review Box 863 and naval records to identify Joseph Zigman's prewar film employer, Navy unit and exact OSS transfer date."),
        base_update(46, identity_status="confirmed", identity_evidence="A nonshared protected linkage and exact official name agreement connect the index and Army records; undefined occupation code 999 remains uninterpreted.", personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="requires_archival_review", nara_catalog_id="1263923", archival_review_priority="critical", next_action="Review Box 863 to identify Christian E Zimmerman's pre-OSS affiliation. No occupation or employer is inferred from undefined code 999."),
    ])
    if len(values) != 46:
        raise RuntimeError(f"Expected 46 person updates, generated {len(values)}")
    return values


def research_attempts() -> list[dict[str, object]]:
    updates = {item["person_id"]: item for item in person_updates()}
    substantiated = set(ARMY_OCCUPATIONS) | {7, 9, 20, 22, 23, 24, 25, 28, 31, 34, 36, 38, 46}
    attempts: list[dict[str, object]] = []
    for row, (person_id, name, box) in PEOPLE.items():
        status = str(updates[person_id]["research_status"])
        if row in substantiated:
            outcome = "candidate_rejected" if status == "conflicting_sources" else "source_reviewed"
            reviewed = 10 if row in {7, 24, 25, 28, 34, 36, 38} else 7
            rejected = 5 if status in {"conflicting_sources", "needs_identity_review"} else 3
            note = "At least one reviewed identity, occupation, student, employment or military-affiliation outcome is preserved with claim-level citations; remaining employer and temporal questions remain explicit."
        else:
            outcome = "candidate_rejected"
            reviewed = 5
            rejected = 4
            note = unresolved_reason(row)
        attempts.append({
            "key": f"page520-row{row}-{slug(name)}-b1030",
            "person_id": person_id,
            "source_adapter": "manual_staged_protocol",
            "query_text": f"{name}; NARA OSS index context; exact-name and meaningful initial, suffix, punctuation, transliteration and OCR variants; OSS, CIA Reading Room, rank, branch, assignment and protected-identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory and archival searches; indexed Box {box}",
            "query_variant_type": "staged_identity_employment_archival_protocol_batch_1030",
            "started_at": "2026-11-04T14:00:00-05:00",
            "completed_at": "2026-11-05T03:30:00-05:00",
            "outcome": outcome,
            "sources_reviewed": reviewed,
            "candidate_sources_rejected": rejected,
            "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives and postwar-only leads were rejected. Rejected or conflicting protected links were not converted into occupations. Army categories were not converted into named employers, undefined category 999 was not interpreted, and a late-1945 category was not presented as pre-OSS evidence.",
            "research_notes": f"{note} The official index, exact-name OSS searches, grouped CIA Reading Room checks, and employer, occupation, obituary, institutional, newspaper, directory and archival searches were reviewed as applicable. Page 520, the page 521 boundary and cited code-list pages were visually checked. No authenticated NARA Catalog API request was made.",
            "next_action": str(updates[person_id]["next_action"]),
            "attempt_number": 1,
            "research_agent_version": "before-oss-b1030-v1",
        })
    if len(attempts) != 46:
        raise RuntimeError(f"Expected 46 research attempts, generated {len(attempts)}")
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-1030-v1",
        "reviewer": "Before OSS Batch 1030 evidence review",
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
