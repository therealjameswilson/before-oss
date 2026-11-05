#!/usr/bin/env python3
"""Generate the reviewed Batch 1040 evidence bundle for PDF page 295."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page295-laura-margulas-to-richard-s-marnocaa-review_"
    "batch-1040_2026-11-05.json"
)

INDEX = "nara-index-b1040"
ARMY = "army-bulk-b1040"
TECH = "army-tech-b1040"
CODES = "army-codes-b1040"
MARKOTNY_NARA = "nara-antoni-markotny-award-b1040"
MARKOUTSAS_HOOVER = "hoover-george-markoutsas-b1040"
MARMANDE_PROUST = "plan-proust-raymond-marmande-b1040"
MARLIN_DIFP = "difp-ervin-marlin-b1040"
MARLIN_NARA = "nara-entry210-ervin-marlin-b1040"
MARITZ_NPS = "nps-raymond-maritz-b1040"
MARITZ_AIA = "aia-raymond-maritz-b1040"

ORG_ARMY = "us-army-b1040"
ORG_FSA = "federal-security-agency-b1040"
ORG_TRINITY = "trinity-college-dublin-b1040"
ORG_MARITZ = "maritz-young-dusard-b1040"


PEOPLE = {
    1: ("2fb5eb54-becf-5721-8f0a-19e421f6793f", "Laura Margulas", "483"),
    2: ("cfb2e73c-107c-579a-941c-1356f22076a2", "Melvin A Margulies", "483"),
    3: ("8f501618-75c0-5990-a576-530900f9c2ca", "Walter J Marheeka", "483"),
    4: ("d9e757d9-01de-58c6-9112-8b8f642db261", "Thomas S Marhefka", "483"),
    5: ("04d1bc37-de10-5065-a818-1e85581b95a0", "Milan Marich", "483"),
    6: ("d1b23065-8aed-57f4-883e-85be7fa96e68", "Francis Marin", "483"),
    7: ("d938f6b6-8c35-52af-a624-d8ff485d262f", "Rudolph Marinacci", "483"),
    8: ("533a7656-e0db-5b72-8287-289bdd1e4df5", "Alfred E Marinelli Jr.", "483"),
    9: ("730e0d7f-d180-5bbe-ac72-d71f79439be9", "Carmel C Marinelli", "483"),
    10: ("a03bd6a4-951d-5f7c-a60d-fa4262ef3eac", "Daniel Marinelli", "483"),
    11: ("13b26dd2-2440-546b-8a30-14d41d03b8ec", "Harry A Marini", "483"),
    12: ("befb9bf8-df84-5e92-8bec-165df969dda7", "Joseph L Marino", "483"),
    13: ("cbd235d3-84cf-552f-800b-4b51df5c2b94", "Peter T Marino", "483"),
    14: ("79116c75-ada2-50c9-9d74-54a382e134b5", "Ivo J Marinovic", "483"),
    15: ("81e0956f-ad62-5249-a193-4ba54f209068", "Fred G Mario", "483"),
    16: ("a3c803d1-4ee1-5c08-99e2-580e8c82f03e", "Bernadette A Marion", "483"),
    17: ("58effa7e-349b-5864-be24-3568512448d8", "Raymond E Maritz", "483"),
    18: ("102a6fee-0163-5f47-82f9-b58e5c336542", "Jack Mark", "483"),
    19: ("3162cf56-ff37-5516-b85a-49c930e316ce", "Morris Mark", "483"),
    20: ("190e7957-db99-5027-8d69-5719c1a61129", "Joseph E Markee", "483"),
    21: ("92db1541-68b4-5bcc-b7c5-e8778cff7229", "Arthur F Markel", "483"),
    22: ("2156cb61-8bc8-5755-a2bb-73727da4d659", "Dennis A Marketos", "483"),
    23: ("acf1e9ff-472b-5b19-b73b-2e0deeb1b97f", "George W Markette Jr.", "483"),
    24: ("0681618a-15fc-57be-b9f8-a9b4e08e4498", "Mary P Markham", "483"),
    25: ("c6fc42fb-a3d6-52d9-8e1f-f72fa24e6e34", "Stanley R Markham", "483"),
    26: ("579370ab-33c6-5a4a-ba6d-9ac2e2da73ce", "Theodore N Markidis", "483"),
    27: ("35a5f249-1fc2-57ad-9e93-ae13a4279577", "Murray E Markley", "483"),
    28: ("9bc573d5-c28f-575b-8290-35f6802cd70a", "Antoni Markotny", "483"),
    29: ("929854ef-6184-51c7-9c61-1910d009b617", "George C Markoutsas", "483"),
    30: ("de329d65-ae50-5201-9581-8d95b3605b46", "Adolph Markovitz", "483"),
    31: ("4c97849a-21f8-5fa6-8993-522ca899e735", "Allen H Marks", "483"),
    32: ("30fec548-28f9-5cef-9e4a-a6a625c649a1", "Beth E Marks", "483"),
    33: ("2e68e4ee-5a3e-5520-bedb-1895ca6c3b98", "Clarence M Marks", "483"),
    34: ("dd2784b6-c932-5e2d-853b-f3ac1692f014", "Robert B Marks", "483"),
    35: ("f3430c7f-6a9c-5f0e-a45e-9b3bcd0dd605", "Malcolm R Markson Jr.", "483"),
    36: ("7adb4df8-1864-5512-93e5-6aa86949c693", "William J Markure", "484"),
    37: ("6b918934-0ff5-5f2d-89be-4519964441ce", "Florence Marlatt", "484"),
    38: ("ed1f0d66-2e30-59a8-a824-38611dea9b0a", "William D Marley", "484"),
    39: ("d2b1e446-e325-5ef6-b740-65e7ee92d2f1", "Ervin R Marlin", "484"),
    40: ("bbf34e82-2609-5ea2-a001-631747d97260", "Gertrude Marlin", "484"),
    41: ("b810e025-3d80-5ee1-b513-7815060304ae", "Wayne S Marling", "484"),
    42: ("753b602d-e9b5-56eb-9b0e-acda285d7da7", "Wentworth J Marling", "484"),
    43: ("2e9db2ba-e130-5832-8ed7-d4c920873f5e", "Elden A Marlow", "484"),
    44: ("a84c5ed2-74e7-59f9-8345-efdc00a04c47", "Goodson G Marlow", "484"),
    45: ("3e7ecf52-360f-5ed5-9776-788d6e229496", "Raymond-Jea Marmande", "484"),
    46: ("5f2ac5f3-3165-5f9a-8773-de9beda50d77", "Richard S Marnocaa", "484"),
}

# Exact-name, nonshared Army identity links whose historical civilian code can
# safely be published as a broad category. Codes 999 remain uninterpreted, and
# Robert B. Marks's 1945 Army entry is not treated as pre-OSS chronology.
ARMY_ASSOCIATIONS = {
    2: ("1942-10-23", "175", "salesperson", "Salesmen and saleswomen, n.e.c.", "unknown", "PDF physical page 171; historical category 1-75"),
    7: ("1943-04-05", "685", "welder or flame cutter", "Welders and flame cutters", "unknown", "PDF physical page 174; historical category 6-85"),
    8: ("1942-02-18", "426", "tailor or tailoress", "Tailors and tailoresses", "unknown", "PDF physical page 173; historical category 4-26"),
    10: ("1942-12-21", "594", "construction foreman", "Foremen, construction", "unknown", "PDF physical page 175; historical category 5-94"),
    11: ("1942-07-11", "735", "routeman", "Routemen", "unknown", "PDF physical page 174; historical category 7-35"),
    13: ("1943-07-17", "583", "mechanic or repairman, not elsewhere classified", "Mechanics and repairmen, n.e.c.", "unknown", "PDF physical page 175; historical category 5,8-83"),
    19: ("1943-12-09", "105", "general office clerk", "Clerks, general office", "unknown", "PDF physical page 171; historical category 1-05"),
    21: ("1942-11-28", "992", "student", "Students", "student", "PDF physical page 304; corrected historical category 9-92"),
    23: ("1942-09-08", "992", "student", "Students", "student", "PDF physical page 304; corrected historical category 9-92"),
    26: ("1942-10-22", "508", "optician, lens grinder, or lens polisher", "Opticians, lens grinders and polishers", "unknown", "PDF physical page 174; historical category 5-08"),
    27: ("1943-06-15", "992", "student", "Students", "student", "PDF physical page 304; corrected historical category 9-92"),
    33: ("1941-06-30", "316", "general farm hand", "Farm hands, general", "unknown", "PDF physical page 172; historical category 3-16"),
    35: ("1942-11-12", "992", "student", "Students", "student", "PDF physical page 304; corrected historical category 9-92"),
    36: ("1941-06-02", "677", "metal filer, grinder, buffer, or polisher", "Filers, grinders, buffers, and polishers, metal", "unknown", "PDF physical page 174; historical category 6-77"),
    41: ("1942-01-27", "793", "carpenter apprentice", "Apprentices, carpenters", "unknown", "PDF physical page 175; historical category 7-93"),
    43: ("1942-10-08", "905", "worker building transportation equipment other than automobiles or aircraft", "Transportation equipment, except automobiles and aircraft, occupations n.e.c.", "unknown", "PDF physical page 174; historical category 9-05"),
    44: ("1943-09-29", "513", "miscellaneous-products manufacturing worker", "Miscellaneous products manufacturing occupations, n.e.c.", "unknown", "PDF physical page 174; historical category 5-13"),
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def source(key: str, **kwargs: object) -> dict[str, object]:
    value: dict[str, object] = {"key": key, "access_date": "2026-11-05"}
    value.update(kwargs)
    return value


def sources() -> list[dict[str, object]]:
    return [
        source(
            INDEX,
            stable_url="https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            archival_identifier="RG 226, Entry A1-224, Boxes 483-484",
            title="OSS Personnel Files from Excel",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="2010-12-23",
            locator="PDF page 295, rows 1-46; page and every printed row visually checked at 180 dpi",
            source_quality="A_direct_official",
            collection_name="Records of the Office of Strategic Services, Record Group 226",
            rights_notes="Every printed row remains recoverable. The clipped Raymond-Jea spelling and incomplete 'Folder is' note are preserved exactly.",
        ),
        source(
            ARMY,
            stable_url="https://catalog.archives.gov/id/1263923",
            archival_identifier="National Archives Identifier 1263923; parent series NAID 604357",
            title="Electronic Army Serial Number Merged File, ca. 1938-1946",
            author_creator="Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="1938-1946; merged file created 2002",
            locator="Official unrestricted ASNEF.FIN.DAT; 24 identity candidates explicitly reviewed; 20 accepted and four rejected",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records",
            document_number="ASNEF.FIN.DAT",
            rights_notes="No raw record, full protected identifier, or bulk-record ordinal is retained in public assets.",
        ),
        source(
            TECH,
            stable_url="https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf",
            archival_identifier="NN3-064-03-008; National Archives Identifier 1263923",
            title="World War II Army Enlistment Records: Reference Copy of Technical Documentation",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives at College Park - Electronic Records",
            publication_record_date="1994-2005; reference copy modified 2011",
            locator="PDF physical pages 44-46; identity, Army-entry-date, grade, and civilian-occupation fields",
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
            locator="PDF physical pages 171-175 and 304; all published categories visually checked",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records technical documentation",
            rights_notes="Historical categories identify neither employer, institution, workplace, nor exact Army-to-OSS sequence. Code 999 remains uninterpreted.",
        ),
        source(
            MARKOTNY_NARA,
            stable_url="https://www.archives.gov/files/research/jfk/releases/104-10165-10120.pdf",
            archival_identifier="104-10165-10120",
            title="OSS awards list",
            author_creator="Office of Strategic Services",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="1945-07-18",
            locator="PDF page 23; Bronze Star approval list; Sgt Antoni Markotny",
            source_quality="A_direct_official",
            collection_name="JFK Assassination Records Collection; declassified OSS record",
            rights_notes="Supports identity and a wartime mission, not a pre-OSS civilian employer.",
        ),
        source(
            MARKOUTSAS_HOOVER,
            stable_url="https://hvr-tms2em.stanford.edu/internal/media/dispatcher/331532/full",
            archival_identifier="HIA-GOODFELLOW-4-A-9-5-3",
            title="OSS personnel board report concerning Capt. George C. Markoutsas, M.C.",
            author_creator="Office of Strategic Services",
            repository_publisher="Hoover Institution Library & Archives, Stanford University",
            publication_record_date="1944",
            locator="Report chronology: Army entry September 1942; OSS assignment October 1943",
            source_quality="A_direct_official",
            collection_name="Millard Preston Goodfellow papers",
            rights_notes="Supports the Army-to-OSS sequence and medical-officer identity; it does not name a civilian employer.",
        ),
        source(
            MARMANDE_PROUST,
            stable_url="https://www.plan-sussex-1944.net/fr/plan-proust.html",
            title="Le Plan Proust",
            author_creator="Serge Larcher",
            repository_publisher="Plan Sussex 1943-1944",
            publication_record_date="Historical research page, accessed 2026-11-05",
            locator="Mission Chat; observer Raymond Marmande, alias Jacques Larcy; parachuted 30 August 1944",
            source_quality="C_reputable_contemporary_or_scholarly",
            collection_name="Plan Proust mission history",
            rights_notes="Supports a high-confidence identity bridge and wartime mission only; it does not establish prior employment.",
        ),
        source(
            MARLIN_DIFP,
            stable_url="https://api.pageplace.de/preview/DT0400.9781908997326_A30782579/preview-9781908997326_A30782579.pdf",
            archival_identifier="ISBN 978-1-908997-32-6",
            title="Documents on Irish Foreign Policy, Volume VII, 1941-1945",
            author_creator="Catriona Crowe, Ronan Fanning, Michael Kennedy, Dermot Keogh, and Eunan O'Halpin, editors",
            repository_publisher="Royal Irish Academy; National Archives of Ireland; Department of Foreign Affairs",
            publication_record_date="2010; first e-published 2017",
            locator="Biographical details, PDF page 37 (printed xxxvi), Ervin 'Spike' Marlin",
            source_quality="A_direct_official",
            collection_name="Documents on Irish Foreign Policy",
            rights_notes="The edited official-record volume supplies the 1939-1944 employment and OSS chronology.",
        ),
        source(
            MARLIN_NARA,
            stable_url="https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/entry-210.pdf",
            archival_identifier="RG 226, Entry 210",
            title="Records of the Office of Strategic Services, Entry 210 inventory",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="Inventory published 2008",
            locator="Entry describing OSS representative Ervin Ross Marlin in Ireland, July 1942-July 1943",
            source_quality="A_direct_official",
            collection_name="Records of the Office of Strategic Services, Record Group 226",
            rights_notes="Corroborates the exact OSS identity and overlap with the legation role; it does not convert that cover role into pre-OSS employment.",
        ),
        source(
            MARITZ_NPS,
            stable_url="https://mostateparks.com/sites/mostateparks/files/St-Louis_Independent-City_Goodwill-Building.pdf",
            archival_identifier="NPS Form 10-900, Goodwill Building, St. Louis",
            title="Goodwill Building National Register of Historic Places Registration Form",
            author_creator="Missouri Department of Natural Resources",
            repository_publisher="National Park Service and Missouri Department of Natural Resources",
            publication_record_date="2020 draft nomination",
            locator="Section 8, continuation pages 33-34; Raymond E. Maritz biography",
            source_quality="A_direct_official",
            collection_name="National Register of Historic Places",
            rights_notes="Explicitly states that Maritz left the firm in 1942 to join OSS.",
        ),
        source(
            MARITZ_AIA,
            stable_url="https://www.usmodernist.org/AIAMI/MSA-1955-04.pdf",
            title="Monthly Bulletin, Michigan Society of Architects, April 1955",
            author_creator="Michigan Society of Architects",
            repository_publisher="Michigan Society of Architects; digitized by USModernist",
            publication_record_date="1955-04",
            locator="Page 18; Raymond E. Maritz notice",
            source_quality="C_reputable_contemporary_or_scholarly",
            collection_name="American Institute of Architects periodicals",
            rights_notes="Independently identifies the firm, exact person, and wartime OSS service.",
        ),
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": ORG_ARMY,
            "canonical_name": "United States Army",
            "historical_name": "U.S. Army",
            "aliases": ["United States Army"],
            "organization_type": "military service",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "A branch-level organization only; no unit or command is inferred from the source.",
        },
        {
            "key": ORG_FSA,
            "canonical_name": "United States Federal Security Agency",
            "historical_name": "United States Federal Security Agency",
            "aliases": ["Federal Security Agency", "FSA"],
            "organization_type": "federal agency",
            "sector": "federal_government",
            "city": "Washington",
            "state_or_region": "District of Columbia",
            "country": "United States",
            "active_dates": "1939-1953",
            "normalization_notes": "Historical agency name preserved; not replaced by a successor department.",
        },
        {
            "key": ORG_TRINITY,
            "canonical_name": "Trinity College Dublin",
            "historical_name": "Trinity College Dublin",
            "aliases": ["TCD"],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "Dublin",
            "country": "Ireland",
            "normalization_notes": "Modeled as student status, never as employment.",
        },
        {
            "key": ORG_MARITZ,
            "canonical_name": "Maritz, Young and Dusard",
            "historical_name": "Maritz, Young and Dusard",
            "aliases": ["Maritz, Young & Dusard"],
            "organization_type": "architecture firm",
            "sector": "business_and_industry",
            "city": "St. Louis",
            "state_or_region": "Missouri",
            "country": "United States",
            "active_dates": "1934-1942",
            "normalization_notes": "Historical spelling in the cited sources is preserved; no later Raymond E. Maritz & Sons name is substituted.",
        },
    ]


def army_affiliation_key(row: int) -> str:
    return f"{slug(PEOPLE[row][1])}-army-association-b1040"


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
                "key": "raymond-e-maritz-firm-b1040",
                "person_id": PEOPLE[17][0],
                "organization_key": ORG_MARITZ,
                "organization_name_as_found": "Maritz, Young and Dusard",
                "role_title": "architect and partner",
                "occupation": "architect",
                "relationship_type": "employment",
                "start_date": "1934",
                "end_date": "1942",
                "date_precision": "The National Register history says Maritz left the firm in 1942 to join OSS; the professional notice independently identifies the firm and OSS service.",
                "city": "St. Louis",
                "state_or_region": "Missouri",
                "country": "United States",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "explicit_immediate",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "A_direct_official",
                "publication_status": "published",
                "research_notes": "The source explicitly states the transition; no modern successor is substituted for the historical firm.",
            },
            {
                "key": "george-c-markoutsas-army-b1040",
                "person_id": PEOPLE[29][0],
                "organization_key": ORG_ARMY,
                "organization_name_as_found": "Army",
                "role_title": "captain, medical officer",
                "relationship_type": "military_assignment",
                "start_date": "1942-09",
                "end_date": "1943-10",
                "date_precision": "An official OSS report says he entered the Army in September 1942 and was assigned to OSS in October 1943.",
                "country": "United States",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "explicit_immediate",
                "identity_confidence": "confirmed",
                "claim_confidence": "confirmed",
                "source_quality": "A_direct_official",
                "publication_status": "published",
                "research_notes": "The claim is limited to the Army-to-OSS transition; no civilian medical employer is inferred.",
            },
            {
                "key": "ervin-r-marlin-fsa-b1040",
                "person_id": PEOPLE[39][0],
                "organization_key": ORG_FSA,
                "organization_name_as_found": "United States Federal Security Agency",
                "role_title": "assistant director",
                "relationship_type": "government_assignment",
                "start_date": "1939",
                "end_date": "1942",
                "date_precision": "The official edited chronology dates the FSA role to 1939-1942 and his OSS-linked Dublin/London sequence from 1942 onward.",
                "city": "Washington",
                "state_or_region": "District of Columbia",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "confirmed",
                "claim_confidence": "confirmed",
                "source_quality": "A_direct_official",
                "publication_status": "published",
                "research_notes": "The intervening legation title overlapped his OSS representative role, so it is not mislabeled as pre-OSS employment.",
            },
            {
                "key": "ervin-r-marlin-trinity-b1040",
                "person_id": PEOPLE[39][0],
                "organization_key": ORG_TRINITY,
                "organization_name_as_found": "Trinity College Dublin",
                "role_title": "history student",
                "relationship_type": "student",
                "start_date": "1929",
                "end_date": "1932",
                "date_precision": "The official edited biographical register dates his history studies and BA to 1929-1932.",
                "city": "Dublin",
                "country": "Ireland",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "confirmed",
                "claim_confidence": "confirmed",
                "source_quality": "A_direct_official",
                "publication_status": "published",
                "research_notes": "Student status is modeled separately and is not counted as an employer.",
            },
        ]
    )
    return values


def army_identity_assessment(row: int) -> str:
    suffix = " A damaged-name alternative was rejected without transferring fields." if row == 27 else ""
    return "Confirmed by exact official name agreement and a nonshared protected linkage; the protected identifier remains private." + suffix


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, label, relationship, locator) in ARMY_ASSOCIATIONS.items():
        values.append(
            {
                "key": f"army-{slug(PEOPLE[row][1])}-b1040",
                "person_id": PEOPLE[row][0],
                "affiliation_key": army_affiliation_key(row),
                "claim_type": "other_pre_oss_affiliation" if relationship == "student" else "occupation",
                "claim_text": f"At Army entry on {date}, {PEOPLE[row][1]} was recorded as {occupation}; no employer, institution, or workplace is identified.",
                "evidence_paraphrase": f"The Army bulk file records code {code}; the visually checked official list defines the category as {label}.",
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

    for row, note in (
        (9, "The official record uses undefined historical code 999, so no occupation or employer is published."),
        (12, "The official record uses undefined historical code 999, so no occupation or employer is published."),
        (34, "The exact Army link is accepted, but the January 1945 entry is not safely classified as pre-OSS chronology."),
    ):
        values.append(
            {
                "key": f"identity-{slug(PEOPLE[row][1])}-b1040",
                "person_id": PEOPLE[row][0],
                "claim_type": "identity",
                "claim_text": f"An official Army record confirms the identity bridge for {PEOPLE[row][1]}; it does not establish a publishable pre-OSS employer.",
                "evidence_paraphrase": note,
                "identity_match_assessment": army_identity_assessment(row),
                "temporal_assessment": "The Army record is identity evidence only and is not promoted into a pre-OSS affiliation claim.",
                "source_quality": "A_direct_official",
                "claim_confidence": "confirmed",
                "publication_status": "published",
                "match_notes": "Full protected identifiers and raw Army rows remain private.",
                "sources": [{"source_key": INDEX}, {"source_key": ARMY}, {"source_key": TECH, "support_type": "context_only"}],
            }
        )

    values.extend(
        [
            {
                "key": "maritz-firm-immediate-b1040",
                "person_id": PEOPLE[17][0],
                "affiliation_key": "raymond-e-maritz-firm-b1040",
                "claim_type": "immediate_pre_oss_affiliation",
                "claim_text": "Raymond E. Maritz left the St. Louis architecture firm Maritz, Young and Dusard in 1942 to join OSS.",
                "evidence_paraphrase": "The National Register history explicitly dates the transition; a 1955 professional notice independently connects the same architect to the firm and OSS.",
                "identity_match_assessment": "High confidence from the distinctive exact name, profession, firm, location, wartime OSS service, and two independent institutional sources.",
                "temporal_assessment": "Explicitly immediate: the official history says he left the firm in 1942 to join OSS.",
                "source_quality": "A_direct_official",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "The indexed Box 483 file remains unreviewed, so identity confidence is high rather than confirmed.",
                "sources": [{"source_key": MARITZ_NPS}, {"source_key": MARITZ_AIA}, {"source_key": INDEX, "support_type": "context_only"}],
            },
            {
                "key": "identity-antoni-markotny-b1040",
                "person_id": PEOPLE[28][0],
                "claim_type": "identity",
                "claim_text": "A declassified OSS awards record identifies Sgt Antoni Markotny and a wartime mission into Germany.",
                "evidence_paraphrase": "The official award list matches the uncommon indexed name and rank and records Bronze Star approval.",
                "identity_match_assessment": "Confirmed by the exact uncommon name, matching sergeant rank, and direct OSS record.",
                "temporal_assessment": "Wartime OSS identity evidence only; no pre-OSS employer or affiliation is established.",
                "source_quality": "A_direct_official",
                "claim_confidence": "confirmed",
                "publication_status": "published",
                "match_notes": "The mission evidence is not recast as an earlier employer.",
                "sources": [{"source_key": MARKOTNY_NARA}, {"source_key": INDEX, "support_type": "context_only"}],
            },
            {
                "key": "army-george-c-markoutsas-b1040",
                "person_id": PEOPLE[29][0],
                "affiliation_key": "george-c-markoutsas-army-b1040",
                "claim_type": "immediate_pre_oss_affiliation",
                "claim_text": "George C. Markoutsas entered the U.S. Army in September 1942 and was assigned to OSS in October 1943.",
                "evidence_paraphrase": "An official 1944 OSS personnel report gives the dates and identifies him as Capt. George C. Markoutsas, M.C.",
                "identity_match_assessment": "Confirmed by exact full name, captain rank, medical-corps designation, and a direct OSS personnel record.",
                "temporal_assessment": "Explicitly sequential Army-to-OSS assignment; no civilian medical employer is inferred.",
                "source_quality": "A_direct_official",
                "claim_confidence": "confirmed",
                "publication_status": "published",
                "match_notes": "The affiliation is U.S. Army at branch level because no pre-OSS unit is named.",
                "sources": [{"source_key": MARKOUTSAS_HOOVER}, {"source_key": INDEX, "support_type": "context_only"}],
            },
            {
                "key": "fsa-ervin-r-marlin-b1040",
                "person_id": PEOPLE[39][0],
                "affiliation_key": "ervin-r-marlin-fsa-b1040",
                "claim_type": "last_civilian_pre_service",
                "claim_text": "Ervin R. Marlin's last documented civilian government employer before OSS service was the U.S. Federal Security Agency.",
                "evidence_paraphrase": "The official edited chronology dates his assistant-director role to 1939-1942 and OSS-linked service from 1942 onward.",
                "identity_match_assessment": "Confirmed by the exact name and middle name, senior civilian grade, detailed chronology, and NARA's separate description of OSS representative Ervin Ross Marlin.",
                "temporal_assessment": "Strongly date-bounded as the last civilian government role; a legation title overlapped rather than preceded his OSS work.",
                "source_quality": "A_direct_official",
                "claim_confidence": "confirmed",
                "publication_status": "published",
                "match_notes": "Modeled as a government assignment and last civilian role, not a private employer.",
                "sources": [{"source_key": MARLIN_DIFP}, {"source_key": MARLIN_NARA}, {"source_key": INDEX, "support_type": "context_only"}],
            },
            {
                "key": "trinity-ervin-r-marlin-b1040",
                "person_id": PEOPLE[39][0],
                "affiliation_key": "ervin-r-marlin-trinity-b1040",
                "claim_type": "other_pre_oss_affiliation",
                "claim_text": "Ervin R. Marlin studied history at Trinity College Dublin from 1929 to 1932.",
                "evidence_paraphrase": "The official edited biographical register records his BA history studies and dates.",
                "identity_match_assessment": "Confirmed by the same exact-name, middle-name, employment, and OSS chronology.",
                "temporal_assessment": "Documented prewar student status; it is not employment and is excluded from employer analytics.",
                "source_quality": "A_direct_official",
                "claim_confidence": "confirmed",
                "publication_status": "published",
                "match_notes": "Student status remains separate from employment.",
                "sources": [{"source_key": MARLIN_DIFP}],
            },
            {
                "key": "identity-raymond-marmande-b1040",
                "person_id": PEOPLE[45][0],
                "claim_type": "identity",
                "claim_text": "The clipped index entry Raymond-Jea Marmande is strongly supported as Raymond Marmande, alias Jacques Larcy, of the Proust Chat mission.",
                "evidence_paraphrase": "The mission history identifies Raymond Marmande as the Chat observer and dates his parachute mission to 30 August 1944.",
                "identity_match_assessment": "High confidence from the rare surname, compatible clipped given name, French officer context, alias, and specific OSS/BCRA mission.",
                "temporal_assessment": "Wartime identity and mission evidence only; no pre-OSS employer is established.",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "The raw indexed spelling remains unchanged while documented variants support search and display.",
                "sources": [{"source_key": MARMANDE_PROUST}, {"source_key": INDEX, "support_type": "context_only"}],
            },
        ]
    )
    return values


def base_update(row: int) -> dict[str, object]:
    person_id, name, box = PEOPLE[row]
    return {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified page 295 source preserves {name}, Box {box}, rank or grade when printed, notes when present, and archive location. Staged official, exact-name, employment, occupation, obituary, institutional, newspaper, directory, and archival searches did not establish a defensible identity-and-affiliation bridge.",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": f"Review indexed Box {box} for corroborating identifiers, immediate pre-OSS affiliation, and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }


def person_updates() -> list[dict[str, object]]:
    updates = [base_update(row) for row in PEOPLE]
    by_row = {row: update for row, update in zip(PEOPLE, updates, strict=True)}

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

    for row, extra in (
        (9, "The accepted Army identity row uses undefined historical code 999; no occupation was inferred."),
        (12, "The accepted Army identity row uses undefined historical code 999; no occupation was inferred."),
        (34, "The accepted Army identity row dates to January 1945; its category was not treated as pre-OSS chronology."),
    ):
        by_row[row].update(
            identity_status="confirmed",
            identity_evidence=army_identity_assessment(row) + " " + extra,
            nara_catalog_id="1263923",
            research_status="requires_archival_review",
            next_action=f"Review Box {PEOPLE[row][2]} to establish a reliable pre-OSS chronology and named employer; the accepted Army identity row does not support one.",
        )

    by_row[15].update(
        identity_status="conflicting",
        identity_evidence="Two protected-linkage Army candidates carry materially different or damaged names. Both were rejected and no identity or occupation fields were transferred.",
        research_status="conflicting_sources",
        archival_review_priority="critical",
        next_action="Review Box 483 and the conflicting identifier-bearing Army files before assigning any external identity to Fred G. Mario.",
    )
    by_row[22].update(
        identity_status="conflicting",
        identity_evidence="The Army candidate prints Dennis D., while the OSS index prints Dennis A. Marketos. It was rejected and no identity or occupation field was transferred.",
        research_status="conflicting_sources",
        archival_review_priority="critical",
        next_action="Review Box 483 and the original index card before resolving the Marketos middle-initial conflict.",
    )
    by_row[46].update(
        identity_status="ambiguous",
        identity_evidence="The index prints the unusual surname Marnocaa, while a protected-number duplicate candidate conflicts with another indexed person. No merge was made.",
        possible_duplicate_group="batch1040-richard-s-marnocaa-identity-conflict",
        research_status="needs_identity_review",
        archival_review_priority="critical",
        next_action="Jointly review Box 484, the original index card, and the conflicting linked file before correcting spelling or merging identities.",
    )

    by_row[17].update(
        identity_status="high_confidence",
        identity_evidence="The exact distinctive name, St. Louis architecture profession and firm, explicit 1942 OSS transition, and independent professional corroboration support Raymond E. Maritz.",
        research_status="verified_employer_found",
        archival_review_priority="medium",
        next_action="Review Box 483 to confirm the high-confidence identity and add exact OSS assignment dates while preserving the explicit 1942 firm-to-OSS transition.",
    )
    by_row[28].update(
        identity_status="confirmed",
        identity_evidence="The exact uncommon name, matching sergeant rank, and direct declassified OSS awards record establish Antoni Markotny.",
        personnel_category="enlisted_army_personnel",
        commissioned_officer=False,
        allied_or_foreign_personnel=False,
        research_status="requires_archival_review",
        archival_review_priority="high",
        next_action="Review Box 483 to identify Markotny's pre-OSS employer or military assignment; the award record establishes identity and mission only.",
    )
    by_row[29].update(
        identity_status="confirmed",
        identity_evidence="An official 1944 OSS report matches the full name and captain/medical-officer context and gives the Army-to-OSS dates.",
        personnel_category="commissioned_army_officer",
        commissioned_officer=True,
        allied_or_foreign_personnel=False,
        research_status="completed",
        archival_review_priority="medium",
        next_action="Review Box 483 to identify any civilian medical employer before Army entry; the immediate Army-to-OSS transition is already documented.",
    )
    by_row[39].update(
        identity_status="confirmed",
        identity_evidence="The official Irish foreign-policy register and NARA inventory match Ervin Ross Marlin and provide a detailed Federal Security Agency, Dublin, and OSS chronology.",
        name_variants=["Ervin Ross Marlin", "Ervin 'Spike' Marlin"],
        replace_name_variants=False,
        research_status="verified_employer_found",
        archival_review_priority="medium",
        next_action="Review Box 484 to refine the formal OSS entry date and distinguish his Dublin diplomatic cover from his already-active OSS representative role.",
    )
    by_row[45].update(
        identity_status="high_confidence",
        identity_evidence="The rare surname, clipped Raymond-Jea index spelling, French S/Lt context, alias Jacques Larcy, and Proust Chat mission support Raymond Marmande.",
        name_variants=["Raymond Marmande", "Jacques Larcy"],
        replace_name_variants=False,
        personnel_category="foreign_or_allied_military_personnel",
        commissioned_officer=True,
        allied_or_foreign_personnel=True,
        research_status="requires_archival_review",
        archival_review_priority="high",
        next_action="Review Box 484 and the cited French mission files to identify Marmande's affiliation before Proust and any civilian employer.",
    )

    if len(updates) != 46:
        raise RuntimeError(f"Expected 46 person updates, generated {len(updates)}")
    return updates


def outcome_note(row: int) -> str:
    notes = {
        9: "The exact Army identity bridge was accepted, but code 999 remains undefined.",
        12: "The exact Army identity bridge was accepted, but code 999 remains undefined.",
        15: "Two damaged or different-name Army candidates were rejected without field transfer.",
        17: "Official and professional histories support Maritz, Young and Dusard as the explicit immediate pre-OSS employer.",
        22: "The Dennis A./Dennis D. middle-initial conflict was rejected and preserved for archival review.",
        27: "The exact Army candidate was accepted; a damaged-name alternative was rejected without field transfer.",
        28: "A NARA award record confirms Markotny's identity and mission but names no prior employer.",
        29: "An official OSS report documents the September 1942 Army entry and October 1943 OSS assignment.",
        34: "The exact Army identity bridge was accepted, but the 1945 entry was not classified as pre-OSS employment.",
        39: "The official chronology supports the Federal Security Agency as the last civilian government employer and Trinity as student status.",
        45: "Mission history supports Raymond Marmande and alias Jacques Larcy but names no prior employer.",
        46: "The unusual Marnocaa spelling and conflicting duplicate-person candidate remain unresolved.",
    }
    return notes.get(row, "Unbridged namesakes, snippets, commercial people-finder pages, unsourced genealogy, relatives, and postwar-only leads did not establish a reliable identity or pre-OSS affiliation.")


def research_attempts() -> list[dict[str, object]]:
    updates = {item["person_id"]: item for item in person_updates()}
    substantiated = set(ARMY_ASSOCIATIONS) | {9, 12, 17, 28, 29, 34, 39, 45}
    candidate_review = {15, 22, 27, 46}
    values: list[dict[str, object]] = []
    for row, (person_id, name, box) in PEOPLE.items():
        outcome = "source_reviewed" if row in substantiated else "candidate_found" if row in candidate_review else "candidate_rejected"
        values.append(
            {
                "key": f"page295-row{row}-{slug(name)}-b1040",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index context; exact-name and meaningful initial, suffix, alias, punctuation and OCR variants; OSS and CIA Reading Room; rank, branch, assignment and protected-identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory and archival searches; indexed Box {box}",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_1040",
                "started_at": "2026-11-05T10:20:00-05:00",
                "completed_at": "2026-11-05T13:40:00-05:00",
                "outcome": outcome,
                "sources_reviewed": 9 if row in substantiated else 5,
                "candidate_sources_rejected": 2 if row in substantiated else 4,
                "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, and postwar-only leads were rejected. Different-name or conflicting-initial Army candidates were rejected. Army categories were not converted into named employers.",
                "research_notes": f"{outcome_note(row)} The official index, exact-name OSS searches, targeted CIA context, employment and occupation searches, and institutional, newspaper, obituary, directory, and archival searches were reviewed as applicable. Page 295 and cited PDF evidence pages were visually checked. No authenticated NARA Catalog API request was made.",
                "next_action": str(updates[person_id]["next_action"]),
                "attempt_number": 1,
                "research_agent_version": "before-oss-b1040-v1",
            }
        )
    if len(values) != 46:
        raise RuntimeError(f"Expected 46 research attempts, generated {len(values)}")
    return values


def main() -> None:
    bundle = {
        "bundle_version": "batch-1040-v1",
        "reviewer": "Before OSS Batch 1040 evidence review",
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
