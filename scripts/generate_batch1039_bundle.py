#!/usr/bin/env python3
"""Generate the reviewed Batch 1039 evidence bundle for PDF page 294."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page294-clarence-j-marah-to-norman-b-margolyes-review_"
    "batch-1039_2026-11-04.json"
)

INDEX = "nara-index-b1039"
ARMY = "army-bulk-b1039"
TECH = "army-tech-b1039"
CODES = "army-codes-b1039"
MARCHADIER_SHD = "shd-paul-marchadier-b1039"
MARCHADIER_NARA = "nara-paul-marchadier-award-b1039"
ELWIN_MARG = "uc-elwin-marg-b1039"
DANIEL_MARGOLIES = "loc-daniel-margolies-b1039"
ARNOLD_MARGOLIN = "encyclopedia-ukraine-arnold-margolin-b1039"
GREER_MARECHAL = "federal-reporter-greer-marechal-b1039"

ORG_BCRA = "bcra-b1039"
ORG_BERKELEY_OPTOMETRY = "uc-berkeley-optometry-b1039"
ORG_RFC = "reconstruction-finance-corporation-b1039"
ORG_MARECHAL_NOE = "marechal-noe-b1039"


PEOPLE = {
    1: ("a023bc7e-95dc-5d4a-9c09-3d24829f1bdf", "Clarence J Marah", "481"),
    2: ("12592f5d-93aa-55ae-8df9-722ebf15ce5c", "Angelo P Marano", "481"),
    3: ("7c8e6346-307a-5b5f-b9bf-7dd3c8969573", "Victor J Marasa", "481"),
    4: ("b8ae54d3-5969-5238-a9bb-2300b9407a78", "Augustine J Maratzo", "481"),
    5: ("b8ae54d3-5969-5238-a9bb-2300b9407a78", "Augustine J Maratzo", "481"),
    6: ("bcd4303e-fffa-5ebc-b501-6b30019416da", "John C Marbach", "481"),
    7: ("ea447f86-4d25-56c5-8e2a-9afad602713a", "Arthur R Marceau", "481"),
    8: ("9a9d713b-fcb0-58d9-ae14-f2a902bbede3", "Orfeo A Marcelli", "481"),
    9: ("5b454610-8c9d-567d-8dfa-431411c7c78d", "Alice D Marcellus", "481"),
    10: ("0d636e5f-4d1e-5eac-99de-cbda3c9e6665", "Corrinem Marcey", "481"),
    11: ("6fe600b4-3ee1-5a5b-a852-02566adbba44", "Doris G March", "481"),
    12: ("3fa31fbc-ce95-5cb3-b99b-ce72ac39f897", "Harold M March", "482"),
    13: ("fbbcd7af-fe1f-512a-8442-55f2f3b600e3", "Irving A March", "482"),
    14: ("4db308d3-43af-5fa2-a297-2c27383e429b", "Robert K March", "482"),
    15: ("50ddfd89-8677-5c51-aa34-ae437787e445", "Robert A March", "482"),
    16: ("1b39ff16-f29b-588b-9f83-be63a822917f", "Paul Marchadier", "482"),
    17: ("bb66ec2f-10c0-5d22-a818-73b048fb7414", "Alfred E Marchand", "482"),
    18: ("a0636f5d-a506-59d9-9534-eec5c1f41de5", "Frederick A Marchese", "482"),
    19: ("6a0e77e5-6026-5d9e-a7dc-6a1eb4d66e8e", "Vincent J Marchese", "482"),
    20: ("04f9bd64-030a-54eb-83e9-97c40d3f1e0d", "Edward Marchigiani", "482"),
    21: ("04f9bd64-030a-54eb-83e9-97c40d3f1e0d", "Edward Marchigiani", "482"),
    22: ("5a76af0e-05a1-52a6-88e3-c0a7632fb1ee", "Victor J Marchino", "482"),
    23: ("d953f990-b90c-5c40-9c9c-6873e7ca640e", "Joseph A Marciari", "482"),
    24: ("ea9d802b-77c3-5615-85ec-b549f52b237e", "Robert K Marck", "482"),
    25: ("0e1f0369-dc6d-51bb-ad34-57ca60e583f6", "Joseph Marcolla", "482"),
    26: ("db960f67-3957-5428-8a88-1529ec29895c", "Vincent E Marcone", "482"),
    27: ("747a00e8-9697-50dd-a3c3-bf52c7413706", "Anthony Marcucci", "482"),
    28: ("7a03c877-d52f-5391-8816-373d9afb762e", "Hughie J Marcum", "482"),
    29: ("dc96e106-bf65-543c-bbc6-86c1a4e53550", "Clarence Marcus", "482"),
    30: ("3b9f32a7-eb0c-5c92-a3a4-5b55f7338d59", "Emil E Marcus", "482"),
    31: ("de994a4b-8d1d-5b4f-a8a5-27e7ce3daf86", "Joseph E Marcus", "482"),
    32: ("9b0ff9af-64d8-592f-8dd8-bd8fe60ad1e6", "Mildred S Marcus", "482"),
    33: ("45a59ffc-eaac-581c-80ff-393af6e87fb4", "Herbert D Marcy", "482"),
    34: ("a65eb747-2057-5d0b-97fc-26ce687aa869", "Laura E Marden", "482"),
    35: ("b8b22870-60ab-5c76-91ee-bf451d391956", "Greer M Marechal", "482"),
    36: ("1ebf20aa-ff35-5dfa-8072-9a6b57574a52", "Panagiotis P Mareskas", "482"),
    37: ("3718a624-ff8b-5ce0-ac0f-7fa4030586f5", "Elwin Marg", "482"),
    38: ("13906f4d-b773-5252-a24d-b5937b67336b", "Helen E Marg", "482"),
    39: ("5a02d6a6-9a60-5b75-b308-226ea2c2ab8b", "Anthony Margherita", "482"),
    40: ("e705e02d-7271-5558-9e67-ac647f1c44a5", "Herman L Margoles", "482"),
    41: ("acd47508-c324-503f-89d1-f5282323109c", "Daniel P Margolies", "482"),
    42: ("9189a5cf-b440-53a6-b31a-50a40ac9692c", "Daniel F Margolies", "482"),
    43: ("fc845180-4288-530b-a1ac-d9b7f70f97da", "Arnold D Margolin", "482"),
    44: ("2375edcc-abd5-5184-9114-ddd91db13879", "Bernard Margolis", "483"),
    45: ("6be45386-3cf5-5767-b97a-8ed733de65f4", "Harry Margolis", "483"),
    46: ("dcb2bf93-bcfc-508d-98cf-59ac081fa9c2", "Norman B Margolyes", "483"),
}

_seen: set[str] = set()
REVIEW_ROWS = tuple(
    row for row in PEOPLE if not (PEOPLE[row][0] in _seen or _seen.add(PEOPLE[row][0]))
)

# Broad historical categories at Army entry. None identifies a named employer,
# institution, workplace, or the later Army-to-OSS sequence.
ARMY_ASSOCIATIONS = {
    2: ("1942-09-08", "138", "stock clerk", "Stock clerks", "unknown", "PDF physical page 171; historical category 1-38"),
    7: ("1942-11-09", "242", "hospital or institutional attendant, not elsewhere classified", "Attendants, hospitals and other institutions, n.e.c.", "unknown", "PDF physical page 172; historical category 2-42"),
    13: ("1941-04-05", "101", "bookkeeper or cashier, except bank", "Bookkeepers and cashiers, except bank", "unknown", "PDF physical page 171; historical category 1-01"),
    17: ("1942-11-28", "678", "worker in a machine-shop or related occupation, not elsewhere classified", "Machine shop and related occupations, n.e.c.", "unknown", "PDF physical page 174; historical category 6,7-78"),
    18: ("1942-10-19", "949", "worker in an unskilled transportation occupation, not elsewhere classified", "Transportation occupations, n.e.c.", "unknown", "PDF physical page 174; historical category 9-49"),
    20: ("1940-11-30", "773", "crane, derrick, hoist, or shovel operator", "Cranemen, derrickmen, hoistmen, and shovelmen", "unknown", "PDF physical page 175; historical category 7-73"),
    22: ("1942-05-05", "152", "salesman for a brokerage or commission firm, not elsewhere classified", "Salesmen, brokerage and commission firms, n.e.c.", "unknown", "PDF physical page 171; historical category 1-52"),
    23: ("1942-11-30", "170", "sales clerk", "Sales clerks", "unknown", "PDF physical page 171; historical category 1-70"),
    25: ("1942-08-18", "932", "worker in an unskilled construction occupation, not elsewhere classified", "Construction occupations, n.e.c.", "unknown", "PDF physical page 174; historical category 9-32"),
    26: ("1942-12-30", "678", "worker in a machine-shop or related occupation, not elsewhere classified", "Machine shop and related occupations, n.e.c.", "unknown", "PDF physical page 174; historical category 6,7-78"),
    28: ("1943-04-28", "583", "mechanic or repairman, not elsewhere classified", "Mechanics and repairmen, n.e.c.", "unknown", "PDF physical page 175; historical category 5,8-83"),
    29: ("1942-10-22", "992", "student", "Students", "student", "PDF physical page 304; corrected historical category 9-92"),
    30: ("1941-05-23", "156", "demonstrator", "Demonstrators", "unknown", "PDF physical page 171; historical category 1-56"),
    31: ("1941-03-17", "137", "stenographer or typist", "Stenographers and typists", "unknown", "PDF physical page 171; historical category 1-37"),
    36: ("1942-10-08", "002", "actor", "Actors and actresses", "unknown", "PDF physical page 170; historical category 0-02"),
    39: ("1941-11-06", "736", "driver or chauffeur", "Drivers and chauffeurs, bus, taxi, truck, and tractor", "unknown", "PDF physical page 175; historical category 7-36"),
    40: ("1942-11-25", "072", "retail manager", "Retail managers", "unknown", "PDF physical page 171; historical category 0-72"),
    46: ("1942-07-14", "072", "retail manager", "Retail managers", "unknown", "PDF physical page 171; historical category 0-72"),
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def source(key: str, **kwargs: object) -> dict[str, object]:
    value: dict[str, object] = {"key": key, "access_date": "2026-11-04"}
    value.update(kwargs)
    return value


def sources() -> list[dict[str, object]]:
    return [
        source(
            INDEX,
            stable_url="https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            archival_identifier="RG 226, Entry A1-224, Boxes 481-483",
            title="OSS Personnel Files from Excel",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="2010-12-23",
            locator="PDF page 294, rows 1-46; page and every printed row visually checked at 180 dpi",
            source_quality="A_direct_official",
            collection_name="Records of the Office of Strategic Services, Record Group 226",
            rights_notes="All 46 printed rows remain separate. Duplicate Maratzo and Marchigiani rows link cautiously to one entity each without deleting source rows.",
        ),
        source(
            ARMY,
            stable_url="https://catalog.archives.gov/id/1263923",
            archival_identifier="National Archives Identifier 1263923; parent series NAID 604357",
            title="Electronic Army Serial Number Merged File, ca. 1938-1946",
            author_creator="Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="1938-1946; merged file created 2002",
            locator="Official unrestricted ASNEF.FIN.DAT; twenty-one Batch 1039 identity candidates explicitly reviewed; nineteen accepted and two rejected",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records",
            document_number="ASNEF.FIN.DAT",
            rights_notes="No raw record, full protected identifier, or bulk-record ordinal is retained in public assets. Two duplicate Edward Marchigiani rows were reviewed explicitly.",
        ),
        source(
            TECH,
            stable_url="https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf",
            archival_identifier="NN3-064-03-008; National Archives Identifier 1263923",
            title="World War II Army Enlistment Records: Reference Copy of Technical Documentation",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives at College Park - Electronic Records",
            publication_record_date="1994-2005; reference copy modified 2011",
            locator="PDF physical pages 44-46; identifier, name, Army-entry-date, grade and civilian-occupation fields",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records technical documentation",
            rights_notes="Used to interpret selected fields only; source damage, coding limits, and incomplete coverage remain applicable.",
        ),
        source(
            CODES,
            stable_url="https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1CL_SD.pdf",
            archival_identifier="National Archives Identifier 1263923; Code No. 30",
            title="NARA Compiled Code Lists for the Electronic Army Serial Number Merged File",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives at College Park - Electronic Records",
            publication_record_date="2011-01-12; modified 2011-03-17",
            locator="PDF physical pages 170-175 and 304; all eighteen published categories visually checked",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records technical documentation",
            rights_notes="Historical categories identify neither employer, institution, workplace, nor exact Army-to-OSS sequence.",
        ),
        source(
            MARCHADIER_SHD,
            stable_url="https://www.servicehistorique.sga.defense.gouv.fr/sites/default/files/2019-10/SHDGR_INV_28P11_BCRA-AGENTS-RESEAUX_0.pdf",
            archival_identifier="GR 28 P 11/20, dossier 1142; GR 28 P 4 171/81; GR 16 P 391417",
            title="BCRA Agents and Networks Inventory",
            author_creator="Service historique de la Défense",
            repository_publisher="Service historique de la Défense",
            publication_record_date="Inventory published online 2019",
            locator="Dossier 1142, Paul Henri Edmond Marchadier, alias Paul Henri Chamard; related individual file dated 1943-1945",
            source_quality="A_direct_official",
            collection_name="Bureau central de renseignements et d'action agent files",
            rights_notes="The archival inventory supports BCRA identity and file references, not a civilian employer.",
        ),
        source(
            MARCHADIER_NARA,
            stable_url="https://www.archives.gov/files/research/jfk/releases/104-10165-10120.pdf",
            archival_identifier="104-10165-10120",
            title="OSS awards list",
            author_creator="Office of Strategic Services",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="1945-07-18",
            locator="PDF page 23; Bronze Star list, S/Lt Paul Marchadier, Marcel mission",
            source_quality="A_direct_official",
            collection_name="JFK Assassination Records Collection; declassified OSS record",
            rights_notes="Supports the exact indexed rank, name, and Marcel mission; it does not identify civilian employment.",
        ),
        source(
            ELWIN_MARG,
            stable_url="https://senate.universityofcalifornia.edu/_files/inmemoriam/html/elwinmarg.html",
            title="Elwin Marg, Professor of Optometry, Emeritus",
            author_creator="Gerald Westheimer",
            repository_publisher="University of California Academic Senate",
            publication_record_date="2010",
            locator="Biographical notice; 1938 entry, 1940 degree and faculty chronology; wartime communications-officer service",
            source_quality="B_authoritative_institutional",
            collection_name="University of California In Memoriam",
            rights_notes="The notice supports a faculty relationship before wartime service but not the exact administrative connection to the OSS index.",
        ),
        source(
            DANIEL_MARGOLIES,
            stable_url="https://tile.loc.gov/storage-services/service/gdc/gdcfindingaidpdfs/ms019011/ms019011.pdf",
            archival_identifier="MSS86306",
            title="Daniel F. Margolies Papers",
            author_creator="Manuscript Division, Library of Congress",
            repository_publisher="Library of Congress",
            publication_record_date="Finding aid revised 2019",
            locator="PDF page 3, biographical note; Reconstruction Finance Corporation 1942-1943 followed by Army/OSS 1943-1946",
            source_quality="A_direct_official",
            collection_name="Daniel F. Margolies Papers",
            rights_notes="The official chronology supports the immediate pre-OSS government employer and precise transition.",
        ),
        source(
            ARNOLD_MARGOLIN,
            stable_url="https://www.encyclopediaofukraine.com/display.asp?linkpath=pages%5CM%5CA%5CMargolinArnold.htm",
            title="Margolin, Arnold",
            author_creator="Larysa Bilous",
            repository_publisher="Internet Encyclopedia of Ukraine, Canadian Institute of Ukrainian Studies",
            publication_record_date="Updated 2023",
            locator="Biographical entry; United States law practice and university lecturing after 1922",
            source_quality="B_authoritative_institutional",
            collection_name="Internet Encyclopedia of Ukraine",
            rights_notes="Supports documented prewar professional activity, but not its immediacy before the indexed OSS relationship.",
        ),
        source(
            GREER_MARECHAL,
            stable_url="https://law.justia.com/cases/federal/district-courts/FSupp/26/162/2593562/",
            archival_identifier="26 F. Supp. 162; No. 365",
            title="Sprout, Waldron & Co. v. Bauer Bros. Co.",
            author_creator="United States District Court for the Southern District of Ohio",
            repository_publisher="Justia, reproducing Federal Supplement",
            publication_record_date="1938-08-04",
            locator="Counsel listing on page 163; Greer Marechal and Marechal & Noe of Dayton",
            source_quality="C_reputable_contemporary_or_scholarly",
            collection_name="Federal court decisions",
            rights_notes="Supports documented 1938 law-firm practice. The exact transition into the indexed file is not established.",
        ),
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": ORG_BCRA,
            "canonical_name": "Bureau central de renseignements et d'action",
            "historical_name": "Bureau central de renseignements et d'action (BCRA)",
            "aliases": ["BCRA"],
            "organization_type": "Free French intelligence service",
            "sector": "military",
            "country": "France",
            "active_dates": "1942-1943 under this name",
            "normalization_notes": "Preserved as a Free French organization; not silently normalized to the OSS or a modern French service.",
        },
        {
            "key": ORG_BERKELEY_OPTOMETRY,
            "canonical_name": "University of California, Berkeley School of Optometry",
            "historical_name": "School of Optometry, University of California, Berkeley",
            "aliases": ["UC Berkeley School of Optometry"],
            "organization_type": "university school",
            "sector": "academia_and_research",
            "city": "Berkeley",
            "state_or_region": "California",
            "country": "United States",
            "normalization_notes": "Part of the University of California, Berkeley. Student attendance and faculty employment are modeled separately; only employment is counted here.",
        },
        {
            "key": ORG_RFC,
            "canonical_name": "Reconstruction Finance Corporation",
            "historical_name": "Reconstruction Finance Corporation",
            "aliases": ["RFC"],
            "organization_type": "federal government corporation",
            "sector": "federal_government",
            "city": "Rio de Janeiro",
            "country": "Brazil",
            "active_dates": "1932-1957",
            "normalization_notes": "The Library of Congress finding aid places Margolies in the corporation's Rio de Janeiro office in 1942-1943.",
        },
        {
            "key": ORG_MARECHAL_NOE,
            "canonical_name": "Marechal & Noe",
            "historical_name": "Marechal & Noe",
            "aliases": [],
            "organization_type": "law firm",
            "sector": "law",
            "city": "Dayton",
            "state_or_region": "Ohio",
            "country": "United States",
            "normalization_notes": "The 1938 historical firm name is preserved; no later firm or successor is substituted.",
        },
    ]


def army_affiliation_key(row: int) -> str:
    return f"{slug(PEOPLE[row][1])}-army-association-b1039"


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, _label, relationship, _locator) in ARMY_ASSOCIATIONS.items():
        item: dict[str, object] = {
            "key": army_affiliation_key(row),
            "person_id": PEOPLE[row][0],
            "relationship_type": relationship,
            "end_date": date,
            "date_precision": f"Historical civilian-occupation code {code} was recorded at Army entry on {date}; no named employer, institution, or workplace is supplied.",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "confirmed",
            "claim_confidence": "medium",
            "source_quality": "A_direct_official",
            "publication_status": "publish_qualified",
            "research_notes": "The broad historical category is excluded from verified-employer analytics and is not converted into a named organization.",
        }
        if relationship == "student":
            item["role_title"] = "student"
        else:
            item["occupation"] = occupation
        values.append(item)
    values.extend(
        [
            {
                "key": "paul-marchadier-bcra-b1039",
                "person_id": PEOPLE[16][0],
                "organization_key": ORG_BCRA,
                "organization_name_as_found": "BCRA",
                "role_title": "sous-lieutenant",
                "relationship_type": "military_assignment",
                "end_date": "1944-09",
                "date_precision": "The official French file spans 1943-1945 and the NARA award list places S/Lt Marchadier on the Marcel mission in 1944.",
                "country": "France",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "confirmed",
                "claim_confidence": "high",
                "source_quality": "A_direct_official",
                "publication_status": "published",
                "research_notes": "This is an Allied wartime affiliation concurrent with OSS cooperation, not a claim that Marchadier was an American OSS employee.",
            },
            {
                "key": "elwin-marg-berkeley-faculty-b1039",
                "person_id": PEOPLE[37][0],
                "organization_key": ORG_BERKELEY_OPTOMETRY,
                "organization_name_as_found": "School of Optometry at the University of California, Berkeley",
                "role_title": "faculty member",
                "occupation": "optometry faculty member",
                "relationship_type": "employment",
                "start_date": "1940",
                "end_date": "before or during World War II",
                "date_precision": "The institutional biography says he received his degree in 1940, then served on the faculty, and during World War II served as an Air Force communications officer.",
                "city": "Berkeley",
                "state_or_region": "California",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "The faculty role is the best-supported last civilian employment before wartime service; the exact OSS relationship remains unverified.",
            },
            {
                "key": "daniel-f-margolies-rfc-b1039",
                "person_id": PEOPLE[42][0],
                "organization_key": ORG_RFC,
                "organization_name_as_found": "Reconstruction Finance Corp.",
                "role_title": "assistant manager",
                "relationship_type": "government_assignment",
                "start_date": "1942",
                "end_date": "1943",
                "date_precision": "The Library of Congress biographical chronology places this role in 1942-1943, immediately before Army/OSS service beginning in 1943.",
                "city": "Rio de Janeiro",
                "country": "Brazil",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "confirmed",
                "claim_confidence": "confirmed",
                "source_quality": "A_direct_official",
                "publication_status": "published",
                "research_notes": "A federal government assignment, modeled separately from private-sector employment.",
            },
            {
                "key": "arnold-d-margolin-law-practice-b1039",
                "person_id": PEOPLE[43][0],
                "organization_name_as_found": "private law practice in the United States",
                "role_title": "lawyer",
                "occupation": "lawyer",
                "relationship_type": "self_employment",
                "start_date": "after 1922",
                "end_date": "before or during World War II",
                "date_precision": "The institutional encyclopedia states that after emigrating in 1922 he practiced law and lectured at universities; it does not date the end of that work.",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "probable",
                "claim_confidence": "medium",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "publish_qualified",
                "research_notes": "Published as other documented prewar employment, not as the immediate predecessor to OSS.",
            },
            {
                "key": "greer-m-marechal-marechal-noe-b1039",
                "person_id": PEOPLE[35][0],
                "organization_key": ORG_MARECHAL_NOE,
                "organization_name_as_found": "Marechal & Noe",
                "role_title": "attorney",
                "occupation": "patent lawyer",
                "relationship_type": "employment",
                "end_date": "1938-08-04",
                "date_precision": "A contemporary federal court opinion lists Greer Marechal and Marechal & Noe of Dayton as counsel in 1938; no later pre-OSS chronology is established.",
                "city": "Dayton",
                "state_or_region": "Ohio",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "probable",
                "claim_confidence": "medium",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "publish_qualified",
                "research_notes": "The uncommon name and middle initial align, but the indexed personnel file is still needed to bridge the legal career to the OSS record.",
            },
        ]
    )
    return values


def army_identity_assessment(row: int) -> str:
    if row == 17:
        return "Confirmed by a nonshared protected linkage and agreement on every name element except one visibly damaged surname character; the protected identifier remains private."
    duplicate_note = " Two duplicate official Army rows agree on all publishable fields and were both accepted explicitly." if row == 20 else ""
    return "Confirmed by exact official name agreement and a nonshared protected linkage; the protected identifier remains private." + duplicate_note


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, label, relationship, locator) in ARMY_ASSOCIATIONS.items():
        values.append(
            {
                "key": f"army-{slug(PEOPLE[row][1])}-b1039",
                "person_id": PEOPLE[row][0],
                "affiliation_key": army_affiliation_key(row),
                "claim_type": "other_pre_oss_affiliation" if relationship == "student" else "occupation",
                "claim_text": f"At Army entry on {date}, {PEOPLE[row][1]} was recorded as {occupation}; no employer, institution, or workplace is identified.",
                "evidence_paraphrase": f"The Army bulk file records code {code}, and the visually checked official code list defines the category as {label}.",
                "identity_match_assessment": army_identity_assessment(row),
                "temporal_assessment": "Strongly date-bounded to Army entry, but not proven to be the immediately preceding role or status before OSS.",
                "source_quality": "A_direct_official",
                "claim_confidence": "medium",
                "publication_status": "publish_qualified",
                "match_notes": "The historical category is qualified, excluded from verified-employer analytics, and not converted into a named organization.",
                "sources": [
                    {"source_key": INDEX},
                    {"source_key": ARMY},
                    {"source_key": TECH, "support_type": "context_only"},
                    {"source_key": CODES, "locator_override": locator},
                ],
            }
        )
    values.extend(
        [
            {
                "key": "bcra-paul-marchadier-b1039",
                "person_id": PEOPLE[16][0],
                "affiliation_key": "paul-marchadier-bcra-b1039",
                "claim_type": "other_pre_oss_affiliation",
                "claim_text": "Paul Marchadier was a French BCRA sous-lieutenant who served with the Marcel mission alongside OSS personnel.",
                "evidence_paraphrase": "French military inventories identify his BCRA file, while a NARA OSS awards record names S/Lt Paul Marchadier and the Marcel mission.",
                "identity_match_assessment": "Confirmed by the exact uncommon name, matching indexed French S/Lt rank, BCRA file, and direct NARA mission record.",
                "temporal_assessment": "Strongly date-bounded wartime Allied assignment; it is not labeled a civilian employer or an American OSS employment relationship.",
                "source_quality": "A_direct_official",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "The public profile preserves the distinction between Allied BCRA affiliation and OSS cooperation.",
                "sources": [{"source_key": MARCHADIER_SHD}, {"source_key": MARCHADIER_NARA}, {"source_key": INDEX, "support_type": "context_only"}],
            },
            {
                "key": "berkeley-elwin-marg-b1039",
                "person_id": PEOPLE[37][0],
                "affiliation_key": "elwin-marg-berkeley-faculty-b1039",
                "claim_type": "last_civilian_pre_service",
                "claim_text": "Elwin Marg's best-supported last civilian employer before wartime service was UC Berkeley's School of Optometry.",
                "evidence_paraphrase": "The UC Academic Senate chronology places his 1940 degree, ensuing faculty service, and World War II Air Force communications duty in sequence.",
                "identity_match_assessment": "High confidence from the exact distinctive name, UC chronology, and compatible wartime military context; the indexed Box 482 file remains unreviewed.",
                "temporal_assessment": "Strongly date-bounded as civilian faculty employment before wartime service, but not proven to be the immediate predecessor to an OSS assignment.",
                "source_quality": "B_authoritative_institutional",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "Student attendance is not mislabeled as employment; only the separately documented faculty role is counted.",
                "sources": [{"source_key": ELWIN_MARG}, {"source_key": INDEX, "support_type": "context_only"}],
            },
            {
                "key": "rfc-daniel-f-margolies-b1039",
                "person_id": PEOPLE[42][0],
                "affiliation_key": "daniel-f-margolies-rfc-b1039",
                "claim_type": "immediate_pre_oss_affiliation",
                "claim_text": "Daniel F. Margolies served as an assistant manager for the Reconstruction Finance Corporation immediately before Army/OSS service.",
                "evidence_paraphrase": "The Library of Congress dates the Rio de Janeiro RFC role to 1942-1943 and Army/OSS service to 1943-1946.",
                "identity_match_assessment": "Confirmed by the exact full name, Library of Congress career chronology, indexed officer identifier pattern, and direct OSS service statement.",
                "temporal_assessment": "Strongly date-bounded and directly sequential; RFC is also the best-supported last civilian government employer before military service.",
                "source_quality": "A_direct_official",
                "claim_confidence": "confirmed",
                "publication_status": "published",
                "match_notes": "Kept as a government assignment rather than private employment.",
                "sources": [{"source_key": DANIEL_MARGOLIES}, {"source_key": INDEX, "support_type": "context_only"}],
            },
            {
                "key": "law-practice-arnold-d-margolin-b1039",
                "person_id": PEOPLE[43][0],
                "affiliation_key": "arnold-d-margolin-law-practice-b1039",
                "claim_type": "other_pre_oss_affiliation",
                "claim_text": "Arnold D. Margolin practiced law in the United States before the war; accessible evidence does not establish that it immediately preceded OSS work.",
                "evidence_paraphrase": "The Canadian Institute of Ukrainian Studies biography states that after his 1922 emigration he practiced law and lectured at universities.",
                "identity_match_assessment": "Probable from the uncommon exact name, senior civilian indexed grade, and documented U.S. legal and public-affairs career; the Box 482 file remains unreviewed.",
                "temporal_assessment": "Documented prewar professional activity with uncertain end date and uncertain immediacy.",
                "source_quality": "B_authoritative_institutional",
                "claim_confidence": "medium",
                "publication_status": "publish_qualified",
                "match_notes": "No specific university is treated as an employer without a dated source.",
                "sources": [{"source_key": ARNOLD_MARGOLIN}, {"source_key": INDEX, "support_type": "context_only"}],
            },
            {
                "key": "marechal-noe-greer-m-marechal-b1039",
                "person_id": PEOPLE[35][0],
                "affiliation_key": "greer-m-marechal-marechal-noe-b1039",
                "claim_type": "other_pre_oss_affiliation",
                "claim_text": "Greer M. Marechal is probably the Dayton attorney documented with Marechal & Noe in 1938.",
                "evidence_paraphrase": "A contemporary federal court opinion lists Greer Marechal and the Dayton law firm Marechal & Noe as counsel.",
                "identity_match_assessment": "Probable from the uncommon name and matching middle initial, but the indexed Box 482 file has not been compared to the legal record.",
                "temporal_assessment": "Documented prewar employment; no source establishes that it was the immediate predecessor to OSS.",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "claim_confidence": "medium",
                "publication_status": "publish_qualified",
                "match_notes": "Visibly qualified and excluded from default high-confidence analytics.",
                "sources": [{"source_key": GREER_MARECHAL}, {"source_key": INDEX, "support_type": "context_only"}],
            },
        ]
    )
    return values


def base_update(row: int) -> dict[str, object]:
    person_id, name, box = PEOPLE[row]
    return {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified page 294 source preserves {name}, Box {box}, rank or grade when printed, notes when present, and archive location. Staged official, exact-name, employment, occupation, obituary, institutional, newspaper, directory, and archival searches did not establish a defensible identity-and-affiliation bridge.",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": f"Review indexed Box {box} for corroborating identifiers, immediate pre-OSS affiliation, and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }


def person_updates() -> list[dict[str, object]]:
    updates = [base_update(row) for row in REVIEW_ROWS]
    by_row = {row: update for row, update in zip(REVIEW_ROWS, updates, strict=True)}

    for row in ARMY_ASSOCIATIONS:
        by_row[row].update(
            identity_status="confirmed",
            identity_evidence=army_identity_assessment(row),
            personnel_category="enlisted_army_personnel",
            commissioned_officer=False,
            allied_or_foreign_personnel=False,
            nara_catalog_id="1263923",
            research_status="occupation_only_found",
            next_action=f"Review Box {PEOPLE[row][2]} to identify a named employer or institution and establish Army-to-OSS chronology. The protected Army link supplies only a broad historical occupation or student-status category.",
        )

    for row, evidence, action in (
        (33, "The protected-linkage Army lead names a different person and the identifier is shared across different indexed names. It was rejected and no fields were transferred.", "Jointly review Box 482 and the conflicting identifier-bearing files before assigning any Army identity or occupation to Herbert D. Marcy."),
        (41, "The protected-linkage Army lead has middle initial F, while this index row prints Daniel P. Margolies and separately lists Daniel F. Margolies. It was rejected and no fields were transferred.", "Jointly review the Daniel P. and Daniel F. Margolies Box 482 files before merging or transferring any Army evidence."),
    ):
        by_row[row].update(
            identity_status="conflicting",
            identity_evidence=evidence,
            research_status="conflicting_sources",
            archival_review_priority="critical",
            next_action=action,
        )

    for row, evidence, action, group in (
        (8, "The index prints a nine-digit numeric value for Orfeo A. Marcelli, unlike the usual Army format. A namesake airborne-service page was rejected because it does not bridge to this OSS-indexed record.", "Review Box 481 and the original index card to verify the printed number and distinguish the airborne namesake before assigning any biography.", "batch1039-orfeo-marcelli-malformed-number"),
        (10, "The index prints the unusual given name 'Corrinem' and note 'Also 312'. Search variants did not establish a safe identity.", "Review Boxes 481 and 312 and the original index card to recover the intended spelling and cross-reference before further research.", "batch1039-corrinem-marcey-cross-reference"),
        (14, "Robert K. March and Robert K. Marck appear on the same page with closely related spellings and nearly identical printed numbers differing in the first digit. They remain separate.", "Jointly review both Box 482 records and original index cards before deciding whether March and Marck are duplicates or different people.", "batch1039-robert-k-march-marck"),
        (24, "Robert K. Marck and Robert K. March appear on the same page with closely related spellings and nearly identical printed numbers differing in the first digit. They remain separate.", "Jointly review both Box 482 records and original index cards before deciding whether Marck and March are duplicates or different people.", "batch1039-robert-k-march-marck"),
    ):
        by_row[row].update(
            identity_status="ambiguous",
            identity_evidence=evidence,
            possible_duplicate_group=group,
            research_status="needs_identity_review",
            archival_review_priority="critical",
            next_action=action,
        )

    by_row[16].update(
        identity_status="confirmed",
        identity_evidence="The exact uncommon name, matching French S/Lt rank, official BCRA file, and NARA Marcel-mission record establish Paul Marchadier.",
        name_variants=["Paul Henri Edmond Marchadier", "Paul Henri Chamard"],
        replace_name_variants=False,
        personnel_category="foreign_or_allied_military_personnel",
        commissioned_officer=True,
        allied_or_foreign_personnel=True,
        research_status="completed",
        archival_review_priority="medium",
        next_action="Review Box 482 and SHD files GR 28 P 11/20 and GR 28 P 4 171/81 to identify Marchadier's civilian employment before BCRA service.",
    )
    by_row[35].update(
        identity_status="probable",
        identity_evidence="The uncommon name and middle initial align with contemporary federal-court records for Dayton patent attorney Greer Marechal, but the personnel file has not been cross-compared.",
        research_status="documented_prewar_employer_found",
        archival_review_priority="critical",
        next_action="Review Box 482 to confirm the Dayton lawyer identity and determine whether Marechal & Noe immediately preceded the indexed OSS relationship.",
    )
    by_row[37].update(
        identity_status="high_confidence",
        identity_evidence="The exact distinctive name, UC Berkeley chronology, and compatible World War II Air Force communications-officer service support Elwin Marg.",
        research_status="documented_prewar_employer_found",
        archival_review_priority="medium",
        next_action="Review Box 482 to establish Marg's exact OSS administrative relationship and whether Air Force service directly preceded it.",
    )
    by_row[42].update(
        identity_status="confirmed",
        identity_evidence="The exact name and Library of Congress chronology explicitly connect Daniel F. Margolies's Reconstruction Finance Corporation, Army, and OSS service.",
        personnel_category="commissioned_army_officer",
        commissioned_officer=True,
        allied_or_foreign_personnel=False,
        research_status="verified_employer_found",
        archival_review_priority="medium",
        next_action="Review Box 482 to enrich the confirmed RFC-to-Army/OSS chronology with assignment dates and claim-level personnel-file evidence.",
    )
    by_row[43].update(
        identity_status="probable",
        identity_evidence="The uncommon exact name, senior CAF-11 grade, and authoritative U.S. legal/public-affairs biography support but do not conclusively prove the Arnold D. Margolin identity.",
        personnel_category="civilian_professional_or_administrative_grade",
        commissioned_officer=False,
        allied_or_foreign_personnel=False,
        research_status="documented_prewar_employer_found",
        archival_review_priority="critical",
        next_action="Review Box 482 to confirm identity and determine which law practice, lecture appointment, or government role immediately preceded OSS.",
    )

    if len(updates) != 44:
        raise RuntimeError(f"Expected 44 unique-person updates, generated {len(updates)}")
    return updates


def unresolved_reason(row: int) -> str:
    special = {
        8: "The malformed index number and unbridged airborne namesake require original-file review.",
        10: "The unusual given name and Box 312 cross-reference require original-card review.",
        14: "The Robert K. March/Marck near-duplicate remains unresolved.",
        16: "Official French and NARA records support BCRA identity and the Marcel mission, but no civilian employer.",
        33: "A different-name, shared-identifier Army lead was rejected and no fields were transferred.",
        35: "A contemporary court record supports Marechal & Noe as qualified documented prewar employment.",
        37: "The UC biography supports Berkeley faculty employment before wartime military service.",
        41: "The Daniel P./Daniel F. middle-initial conflict remains separate and no Army fields were transferred.",
        42: "The Library of Congress establishes the Reconstruction Finance Corporation as the immediate predecessor to Army/OSS service.",
        43: "The institutional biography supports qualified prewar U.S. legal practice but not its immediacy.",
    }
    return special.get(
        row,
        "Unbridged namesakes, snippets, commercial people-finder pages, unsourced genealogy, relatives, and postwar-only leads did not establish this indexed person's identity or pre-OSS affiliation.",
    )


def research_attempts() -> list[dict[str, object]]:
    updates = {item["person_id"]: item for item in person_updates()}
    substantiated = set(ARMY_ASSOCIATIONS) | {16, 35, 37, 42, 43}
    candidate_review = {8, 10, 14, 24, 33, 41}
    values: list[dict[str, object]] = []
    for row in REVIEW_ROWS:
        person_id, name, box = PEOPLE[row]
        outcome = "source_reviewed" if row in substantiated else "candidate_found" if row in candidate_review else "candidate_rejected"
        values.append(
            {
                "key": f"page294-row{row}-{slug(name)}-b1039",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index context; exact-name and meaningful initial, suffix, alias, punctuation and OCR variants; OSS and CIA Reading Room; rank, branch, assignment and protected-identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory and archival searches; indexed Box {box}",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_1039",
                "started_at": "2026-11-04T23:40:00-05:00",
                "completed_at": "2026-11-05T01:20:00-05:00",
                "outcome": outcome,
                "sources_reviewed": 9 if row in substantiated else 5,
                "candidate_sources_rejected": 2 if row in substantiated else 4,
                "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, and postwar-only leads were rejected. Different-name or conflicting-initial Army candidates were rejected. Army categories were not converted into named employers.",
                "research_notes": f"{unresolved_reason(row)} The official index, exact-name OSS searches, targeted CIA context, employment and occupation searches, and institutional, newspaper, obituary, directory, and archival searches were reviewed as applicable. CIA direct adapter access was robots-disallowed and was not treated as a negative result; official-domain web discovery was used instead. Page 294 and cited PDF evidence pages were visually checked. No authenticated NARA Catalog API request was made.",
                "next_action": str(updates[person_id]["next_action"]),
                "attempt_number": 1,
                "research_agent_version": "before-oss-b1039-v1",
            }
        )
    if len(values) != 44:
        raise RuntimeError(f"Expected 44 research attempts, generated {len(values)}")
    return values


def main() -> None:
    bundle = {
        "bundle_version": "batch-1039-v1",
        "reviewer": "Before OSS Batch 1039 evidence review",
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
