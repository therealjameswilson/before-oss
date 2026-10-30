#!/usr/bin/env python3
"""Generate the reviewed Batch 985 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page483-george-vetlesen-to-peter-viezbicke-jr-"
    "review_batch-985_2026-10-30.json"
)

INDEX = "nara-index-b985"
ARMY = "army-bulk-b985"
TECH = "army-tech-b985"
CODES = "army-codes-b985"
COLUMBIA_VETLESEN = "columbia-georg-vetlesen-b985"
SNL_VETLESEN = "snl-georg-vetlesen-b985"
OREGON_VICOVARI = "oregon-statesman-vicovari-b985"
NEWYORKER_VICOVARI = "new-yorker-vicovari-b985"
LOC_VIECELI = "loc-vieceli-dostler-b985"
ONB_VIERTEL = "onb-berthold-viertel-b985"
NPS_PETER_VIERTEL = "nps-peter-viertel-b985"
AUSTRIAN_SOLDIERS = "austrian-soldiers-peter-viertel-b985"
YALE_VIETOR = "yale-alexander-vietor-b985"
PRINCETON_VIETOR = "princeton-thomas-vietor-b985"

ORG_BAAC = "british-american-ambulance-corps-b985"
ORG_WARNER = "warner-bros-b985"
ORG_MARINES = "us-marine-corps-b985"
ORG_COX_STEVENS = "cox-stevens-b985"
ORG_YALE = "yale-university-b985"
ORG_PRINCETON = "princeton-university-b985"


PEOPLE = {
    1: ("bdfb7886-8828-54f8-a9ed-5c0cf4fbec12", "George Vetlesen"),
    2: ("73ad5483-fde8-5f32-baf8-86c26b587fb0", "Lucienne Vetois"),
    3: ("ceba63b7-3955-5406-b42e-dc9ade9b2b62", "Earl F Vetter"),
    4: ("67ca8fac-b73e-5eb2-b6ab-722050536fbe", "Ethel M Vetter"),
    5: ("852fe132-4da7-54f3-8b43-9e496bb8bc4c", "Rene Veuve"),
    6: ("2c443b81-1651-50ee-b16a-c6fcaa97f384", "Joseph L Vezina"),
    7: ("a7005dd5-829e-581c-8152-261fbc4b065b", "Normand H Vezina"),
    8: ("6a3a0778-935e-59a4-9a93-b1aea9a400d8", "Pauline P Vezzani"),
    9: ("955a9027-9c32-5d43-bd3d-c011cf788a8a", "Joseph L Vicilante"),
    10: ("9934387e-de20-5f53-a5bd-3176ba81a74f", "Harold M Vick"),
    11: ("b0f9e8e5-84f6-5410-9a3a-3d6d66426819", "Billy D Vickers"),
    12: ("6204dcf0-a6fc-5cc1-b593-1f03b9f21dca", "Francis J Vicovari"),
    13: ("694d922b-cf1f-59fa-8a69-0266776bcb4b", "Mary M Victory"),
    14: ("31472523-fd05-5df5-b886-8a40950fb1c1", "Felix G Vidal"),
    15: ("7d48d498-46f5-5572-9cde-bb8673a72889", "Trinidad B Vidal"),
    16: ("ce163b3a-7988-579a-a924-7a7faf2437c4", "Livio Vieceli"),
    17: ("6d9ca923-aed1-5972-8936-ceed76854a23", "Edward C Viegel"),
    18: ("29d07d6e-5017-59db-a162-c722e8df0a96", "Berthold Viertel"),
    19: ("3c3aa688-f432-5c3c-a91c-1fa272cc8120", "Peter Viertel"),
    20: ("a3195826-1cb9-5229-a8be-95a093b6e10c", "Alexander O Vietor"),
    21: ("0850a43e-53ef-55cf-8b84-2bd15fada613", "Thomas F Vietor Jr."),
    22: ("fc460dd6-ef38-58f5-af82-942abdaa1e30", "Erik E Vieux"),
    23: ("efee5b47-6f91-5fb2-a0cf-81b67253cc45", "Peter P Viezbicke Jr."),
}


ARMY_FINDINGS = {
    3: {
        "date": "1942-10-07",
        "code": "718",
        "occupation": "Dyers",
        "public_occupation": "dyer",
        "relationship": "employment",
        "locator": "PDF physical page 174; historical category 7-18",
        "bridge": "protected",
    },
    15: {
        "date": "1943-05-17",
        "code": "721",
        "occupation": "Miners and mining-machine operators",
        "public_occupation": "miner or mining-machine operator",
        "relationship": "employment",
        "locator": "PDF physical page 174; historical category 7-21",
        "bridge": "protected",
    },
    16: {
        "date": "1941-04-29",
        "code": "048",
        "occupation": "Draftsmen",
        "public_occupation": "draftsman",
        "relationship": "employment",
        "locator": "PDF physical page 171; historical category 0-48",
        "bridge": "name_rank_operation",
    },
    23: {
        "date": "1942-12-23",
        "code": "170",
        "occupation": "Sales clerks",
        "public_occupation": "sales clerk",
        "relationship": "employment",
        "locator": "PDF physical page 171; historical category 1-70",
        "bridge": "protected",
    },
}


UNRESOLVED = {
    2: "Exact-name, French-language, OSS, employer, occupation, obituary, directory and archival searches supplied no reliable identity or pre-OSS affiliation bridge.",
    4: "Exact-name and initial-variant searches produced unbridged namesakes and no Box 804 or direct OSS connection.",
    6: "The indexed identifier narrows the archival target, but exact-name, military, obituary, employer and institutional searches did not establish a reliable biography or pre-OSS affiliation.",
    7: "Exact-name and Canadian or U.S. military searches produced multiple namesakes and no Box 804 or direct OSS bridge.",
    8: "Exact-name, spelling-variant, obituary, institutional and archival searches produced no reliable identity or pre-OSS affiliation bridge.",
    9: "Exact-name and likely Vigilante spelling-variant searches supplied no protected identifier, Box 804 or direct OSS bridge.",
    10: "The printed identifier is preserved privately, but it does not meet the official Army bulk file's eight-digit matching rule and reviewed sources did not establish a reliable identity or employer.",
    11: "Exact-name, military, obituary and institutional searches supplied only unrelated later namesakes and no Box 804 or direct OSS bridge.",
    13: "The common name and absence of an index identifier left obituary, directory, military and institutional candidates unresolved.",
    14: "The French second-lieutenant rank narrows the archival target, but reviewed French, military and OSS sources did not establish the officer's identity or pre-OSS sequence.",
    22: "Exact-name, French-language, military, obituary and archival searches supplied no reliable person-level identity or pre-OSS affiliation bridge.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 804-805",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 483, rows 1-23; checked against layout-preserving text and an original-detail page render",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate; original spelling and archival context are recoverable while public identifiers are masked.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; four protected-identifier comparisons and one exact-name Livio Vieceli lookup; identifiers and record ordinals withheld",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "No raw bulk row, record ordinal or full protected identifier enters the evidence bundle or public assets.",
        },
        {
            "key": TECH,
            "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf",
            "archival_identifier": "NN3-064-03-008; National Archives Identifier 1263923",
            "title": "World War II Army Enlistment Records: Reference Copy of Technical Documentation",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives at College Park - Electronic Records",
            "publication_record_date": "1994-2005; reference copy modified 2011",
            "locator": "PDF physical pages 44-46; name, Army-entry-date, grade and civilian-occupation fields",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
        },
        {
            "key": CODES,
            "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1CL_SD.pdf",
            "archival_identifier": "National Archives Identifier 1263923; Code No. 30",
            "title": "NARA Compiled Code Lists for the Electronic Army Serial Number Merged File",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives at College Park - Electronic Records",
            "publication_record_date": "2011-01-12; modified 2011-03-17",
            "locator": "PDF physical pages 171 and 174; four Batch 985 categories visually and textually checked",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical categories identify status or broad occupation, not a named employer, workplace or exact job title.",
        },
        {
            "key": COLUMBIA_VETLESEN,
            "stable_url": "https://lamont.columbia.edu/about/vetlesen-prize",
            "title": "The Vetlesen Prize",
            "author_creator": "Lamont-Doherty Earth Observatory",
            "repository_publisher": "Columbia University",
            "publication_record_date": "Current at access",
            "locator": "G. Unger Vetlesen biographical section",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Lamont-Doherty Earth Observatory institutional history",
            "rights_notes": "The biography uses Georg Unger Vetlesen; the bridge to indexed George Vetlesen remains visibly qualified.",
        },
        {
            "key": SNL_VETLESEN,
            "stable_url": "https://snl.no/OSS",
            "title": "OSS",
            "author_creator": "Mats Tangestuen",
            "repository_publisher": "Store norske leksikon",
            "publication_record_date": "Current at access",
            "locator": "Norway section naming Lt. Commander Georg Unger Vetlesen and describing his civilian occupation",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Store norske leksikon",
        },
        {
            "key": OREGON_VICOVARI,
            "stable_url": "https://oregonnews.uoregon.edu/lccn/sn85042470/1941-05-25/ed-1/seq-18/",
            "archival_identifier": "The Oregon Statesman, May 25, 1941, page 18, image 18",
            "title": "Here's Story of Zamzam Sinking",
            "author_creator": "Associated Press",
            "repository_publisher": "The Oregon Statesman; Historic Oregon Newspapers, University of Oregon Libraries",
            "publication_record_date": "1941-05-25",
            "locator": "Page 18; Francis J. Vicovari identified as leader of 24 American ambulance drivers bound for Africa",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Historic Oregon Newspapers",
        },
        {
            "key": NEWYORKER_VICOVARI,
            "stable_url": "https://www.newyorker.com/magazine/1941/04/26/1941-04-26-047-tny-cards-000186469",
            "title": "Eighty-Five Days from Lexington Avenue",
            "author_creator": "The New Yorker",
            "repository_publisher": "The New Yorker",
            "publication_record_date": "1941-04-26",
            "locator": "Contemporary account of the British American Ambulance Corps unit before sailing on the Zamzam",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "The New Yorker archive",
            "rights_notes": "Only a concise paraphrase is retained; the article is not reproduced.",
        },
        {
            "key": LOC_VIECELI,
            "stable_url": "https://tile.loc.gov/storage-services/service/ll/llmlp/2011525363_NT_Nazi_Vol-V/2011525363_NT_Nazi_Vol-V.pdf",
            "archival_identifier": "Nazi Conspiracy and Aggression, Volume V, document 2610-PS",
            "title": "Nazi Conspiracy and Aggression, Volume V",
            "author_creator": "Office of United States Chief of Counsel for Prosecution of Axis Criminality",
            "repository_publisher": "United States Government Printing Office; Library of Congress",
            "publication_record_date": "1946",
            "locator": "Document 2610-PS; Technical Sergeant Livio Vieceli and the 2677th Special Reconnaissance Battalion mission",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "Military Legal Resources",
            "rights_notes": "The public evidence note omits the full service number printed in the official document.",
        },
        {
            "key": ONB_VIERTEL,
            "stable_url": "https://data.onb.ac.at/nlv/nlv_lex/perslex/TV/Viertel_Berthold.htm",
            "title": "Berthold Viertel",
            "author_creator": "Literaturarchiv der Oesterreichischen Nationalbibliothek",
            "repository_publisher": "Austrian National Library",
            "publication_record_date": "2008-11",
            "locator": "Biographical entry describing writing, theater direction and film work",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Nachlaesse in Oesterreich - Personenlexikon",
        },
        {
            "key": NPS_PETER_VIERTEL,
            "stable_url": "https://www.nps.gov/articles/oss-in-action-the-mediterranean-and-european-theaters.htm",
            "title": "OSS in Action: The Mediterranean and European Theaters",
            "author_creator": "John Whiteclay Chambers II",
            "repository_publisher": "National Park Service",
            "publication_record_date": "2008; web edition current at access",
            "locator": "Special Intelligence section naming Peter Viertel, his 1942 screenwriting and recruitment from the Marine Corps",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "OSS Training in the National Parks and Service Abroad in World War II",
        },
        {
            "key": AUSTRIAN_SOLDIERS,
            "stable_url": "https://austriansoldiers.lbg.ac.at/bio/peter-viertel/?lang=en",
            "title": "Peter Viertel",
            "author_creator": "Austrian Heritage Archive research project",
            "repository_publisher": "Ludwig Boltzmann Institute for Research on Consequences of War",
            "publication_record_date": "Current at access",
            "locator": "Biographical chronology from university study and Warner Bros. work through Marine Corps and OSS transfer",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Austrian Soldiers in the United States Army",
            "rights_notes": "Full service identifiers shown by the source are not retained in public data.",
        },
        {
            "key": YALE_VIETOR,
            "stable_url": "https://hdl.handle.net/10079/fa/mssa.ms.0542",
            "archival_identifier": "MS 542, Alexander Orr Vietor Collection",
            "title": "Guide to the Alexander Orr Vietor Collection",
            "author_creator": "Manuscripts and Archives staff",
            "repository_publisher": "Yale University Library",
            "publication_record_date": "Finding aid current at access",
            "locator": "PDF page 4 of 7, Biographical / Historical section",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Yale University Library finding aids",
        },
        {
            "key": PRINCETON_VIETOR,
            "stable_url": "https://paw.princeton.edu/memorial/thomas-frederick-vietor-jr-38",
            "title": "Thomas Frederick Vietor Jr. '38",
            "author_creator": "Princeton Class of 1938",
            "repository_publisher": "Princeton Alumni Weekly",
            "publication_record_date": "2013-12-04",
            "locator": "Memorial identifying Princeton study and wartime OSS service on William Donovan's staff",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Princeton Alumni Weekly memorials",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": ORG_BAAC,
            "canonical_name": "British American Ambulance Corps",
            "historical_name": "British American Ambulance Corps",
            "aliases": ["British-American Ambulance Corps"],
            "organization_type": "wartime medical relief organization",
            "sector": "labor_nonprofit_and_religion",
            "city": "New York",
            "state_or_region": "New York",
            "country": "United States",
            "active_dates": "World War II",
            "normalization_notes": "Contemporary spelling variants are preserved; volunteer leadership is not converted into paid employment.",
        },
        {
            "key": ORG_WARNER,
            "canonical_name": "Warner Bros.",
            "historical_name": "Warner Bros.",
            "aliases": ["Warner Brothers"],
            "organization_type": "film studio",
            "sector": "arts_and_culture",
            "city": "Burbank",
            "state_or_region": "California",
            "country": "United States",
            "normalization_notes": "Historical studio name retained; no modern corporate parent is substituted.",
        },
        {
            "key": ORG_MARINES,
            "organization_id": "48217a0d-8af9-5502-b0ed-f24d49f634f9",
            "canonical_name": "United States Marine Corps",
            "historical_name": "United States Marine Corps",
            "aliases": ["U.S. Marine Corps", "Marine Corps"],
            "organization_type": "military service",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "Military assignment is not civilian employment.",
        },
        {
            "key": ORG_COX_STEVENS,
            "canonical_name": "Cox & Stevens",
            "historical_name": "Cox & Stevens",
            "organization_type": "naval architecture firm",
            "sector": "engineering_science_and_technology",
            "city": "New York",
            "state_or_region": "New York",
            "country": "United States",
            "active_dates": "documented 1937-1940 for Alexander O. Vietor",
            "normalization_notes": "Historical firm name preserved exactly as the Yale finding aid gives it.",
        },
        {
            "key": ORG_YALE,
            "organization_id": "918dedde-f9d1-5db1-8304-5c218a06b9b5",
            "canonical_name": "Yale University",
            "historical_name": "Yale University",
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "New Haven",
            "state_or_region": "Connecticut",
            "country": "United States",
        },
        {
            "key": ORG_PRINCETON,
            "organization_id": "ad6bb38c-850a-50e4-b092-d33163c93875",
            "canonical_name": "Princeton University",
            "historical_name": "Princeton University",
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "Princeton",
            "state_or_region": "New Jersey",
            "country": "United States",
            "normalization_notes": "Student status is modeled separately from employment.",
        },
    ]


def occupation_affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, item in ARMY_FINDINGS.items():
        values.append(
            {
                "key": f"{slug(PEOPLE[row][1])}-occupation-b985-row{row}",
                "person_id": PEOPLE[row][0],
                "occupation": item["public_occupation"],
                "relationship_type": item["relationship"],
                "end_date": item["date"],
                "date_precision": "Historical civilian-occupation category recorded at Army entry; employer, workplace and duration are not supplied",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "A_direct_official",
                "publication_status": "publish_qualified",
                "research_notes": "Official historical category only; excluded from verified-employer analytics and not narrowed beyond the code-list wording.",
            }
        )
    return values


def affiliations() -> list[dict[str, object]]:
    values = occupation_affiliations()
    values.extend(
        [
            {
                "key": "george-vetlesen-shipbuilding-b985",
                "person_id": PEOPLE[1][0],
                "role_title": "shipbuilder and naval engineer",
                "occupation": "shipbuilder and naval engineer",
                "relationship_type": "employment",
                "end_date": "1943",
                "date_precision": "Columbia documents many years in shipbuilding before Navy entry in 1943; no named employer or exact end date is supplied",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "probable",
                "claim_confidence": "medium",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "publish_qualified",
                "research_notes": "The George-to-Georg spelling bridge is probable, not settled; occupation is not converted into a named employer.",
            },
            {
                "key": "francis-vicovari-baac-b985",
                "person_id": PEOPLE[12][0],
                "organization_key": ORG_BAAC,
                "organization_name_as_found": "British American Ambulance Corps",
                "role_title": "ambulance-unit leader",
                "occupation": "ambulance driver and unit leader",
                "relationship_type": "volunteer",
                "start_date": "1940",
                "end_date": "1941-04",
                "date_precision": "Contemporary accounts document ambulance work in France in 1940 and leadership of the Africa-bound unit in April 1941; later captivity separates this work from OSS service",
                "city": "New York",
                "state_or_region": "New York",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "probable",
                "claim_confidence": "medium",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "publish_qualified",
                "research_notes": "The uncommon exact name and wartime chronology support a probable match, but Box 804 is required for a definitive OSS identity bridge.",
            },
            {
                "key": "berthold-viertel-film-b985",
                "person_id": PEOPLE[18][0],
                "role_title": "writer and director",
                "occupation": "writer, theater director and film director",
                "relationship_type": "employment",
                "start_date": "1928",
                "end_date": "1947",
                "date_precision": "The Austrian National Library documents U.S. and British film work from 1928-1947; the source does not state an OSS role or exact employment sequence",
                "country": "United States and United Kingdom",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "probable",
                "claim_confidence": "medium",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "publish_qualified",
                "research_notes": "The rare exact name supports a probable identity, but Box 804 must establish why his file appears in the OSS personnel index and whether this work preceded or overlapped it.",
            },
            {
                "key": "peter-viertel-warner-b985",
                "person_id": PEOPLE[19][0],
                "organization_key": ORG_WARNER,
                "organization_name_as_found": "Warner Bros.",
                "role_title": "office boy and screenwriter",
                "occupation": "screenwriter",
                "relationship_type": "employment",
                "end_date": "1942-07",
                "date_precision": "Institutional chronology places Warner Bros. work before probable voluntary Marine Corps entry in July 1942",
                "city": "Los Angeles",
                "state_or_region": "California",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Modeled as the last documented civilian employer before Marine service; the source does not supply a payroll title or exact departure day.",
            },
            {
                "key": "peter-viertel-marines-b985",
                "person_id": PEOPLE[19][0],
                "organization_key": ORG_MARINES,
                "organization_name_as_found": "Marine Corps",
                "role_title": "Marine; promoted to second lieutenant before OSS transfer",
                "relationship_type": "military_assignment",
                "start_date": "1942-07",
                "end_date": "1944",
                "date_precision": "Institutional chronology dates Marine entry to July 1942 and officer training and OSS transfer to 1944",
                "country": "United States",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "explicit_immediate",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Military assignment, not civilian employment. Both institutional sources explicitly place Marine service before OSS recruitment or transfer.",
            },
            {
                "key": "alexander-vietor-cox-stevens-b985",
                "person_id": PEOPLE[20][0],
                "organization_key": ORG_COX_STEVENS,
                "organization_name_as_found": "Cox & Stevens",
                "role_title": "associate",
                "occupation": "naval architecture",
                "relationship_type": "employment",
                "start_date": "1937",
                "end_date": "1940",
                "date_precision": "Yale finding-aid biographical chronology; definitely prewar but not shown as the immediate pre-OSS role",
                "city": "New York",
                "state_or_region": "New York",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "probable",
                "claim_confidence": "medium",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "publish_qualified",
                "research_notes": "The uncommon name and middle initial align, but Box 805 remains necessary to close the OSS identity bridge.",
            },
            {
                "key": "alexander-vietor-yale-b985",
                "person_id": PEOPLE[20][0],
                "organization_key": ORG_YALE,
                "organization_name_as_found": "Yale University",
                "role_title": "assistant to the director of the Art Gallery",
                "relationship_type": "employment",
                "start_date": "1941",
                "end_date": "1943",
                "date_precision": "Yale chronology dates the assistant role to 1941 and appointment as curator of maps to 1943; the relation to OSS service is not established",
                "city": "New Haven",
                "state_or_region": "Connecticut",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "probable",
                "claim_confidence": "medium",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "publish_qualified",
                "research_notes": "The Yale role is documented, but no source reviewed establishes whether it immediately preceded, overlapped or followed OSS work.",
            },
            {
                "key": "thomas-vietor-princeton-b985",
                "person_id": PEOPLE[21][0],
                "organization_key": ORG_PRINCETON,
                "organization_name_as_found": "Princeton",
                "role_title": "student; English major",
                "relationship_type": "student",
                "end_date": "1938",
                "date_precision": "Princeton Class of 1938; no evidence reviewed makes student status an employer or the immediate pre-OSS affiliation",
                "city": "Princeton",
                "state_or_region": "New Jersey",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Student status is not employment and is excluded from verified-employer analytics.",
            },
        ]
    )
    return values


def claim(
    row: int,
    key: str,
    claim_type: str,
    claim_text: str,
    evidence_paraphrase: str,
    identity_assessment: str,
    temporal_assessment: str,
    source_quality: str,
    confidence: str,
    source_links: list[dict[str, str]],
    notes: str,
    affiliation_key: str | None = None,
    publication_status: str = "published",
) -> dict[str, object]:
    value: dict[str, object] = {
        "key": key,
        "person_id": PEOPLE[row][0],
        "claim_type": claim_type,
        "claim_text": claim_text,
        "evidence_paraphrase": evidence_paraphrase,
        "identity_match_assessment": identity_assessment,
        "temporal_assessment": temporal_assessment,
        "source_quality": source_quality,
        "claim_confidence": confidence,
        "publication_status": publication_status,
        "match_notes": notes,
        "sources": source_links,
    }
    if affiliation_key:
        value["affiliation_key"] = affiliation_key
    return value


def army_identity_claim(row: int) -> dict[str, object]:
    name = PEOPLE[row][1]
    item = ARMY_FINDINGS[row]
    if item["bridge"] == "protected":
        evidence = "The exact official name and a nonshared protected-identifier agreement support the match."
        assessment = "High confidence from exact name and a nonshared protected identifier; the protected value and raw record are withheld."
        links = [
            {"source_key": INDEX},
            {"source_key": ARMY, "locator_override": "Accepted identity bridge; protected identifier and raw record withheld"},
        ]
    else:
        evidence = "The exact rare name in the Army file, indexed T/Sgt rank and official 2677th Special Reconnaissance Battalion record align."
        assessment = "High confidence from exact rare name, rank, dated Army entry and an independent official wartime unit record; no protected identifier is published."
        links = [
            {"source_key": INDEX},
            {"source_key": ARMY, "locator_override": "Exact-name Army bulk entry; raw record and identifier withheld"},
            {"source_key": LOC_VIECELI, "locator_override": "Document 2610-PS; name and Technical Sergeant rank"},
        ]
    return claim(
        row,
        f"identity-{slug(name)}-army-b985-row{row}",
        "identity",
        f"Indexed {name} is high-confidence matched to the official Army entry used for this dated pre-service finding.",
        evidence,
        assessment,
        "The Army entry date is preserved separately from the later OSS-index context.",
        "A_direct_official",
        "high",
        links,
        "Private identifiers and raw bulk records remain absent from the evidence bundle and public output.",
    )


def army_claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, item in ARMY_FINDINGS.items():
        name = PEOPLE[row][1]
        values.append(army_identity_claim(row))
        values.append(
            claim(
                row,
                f"occupation-{slug(name)}-b985-row{row}",
                "occupation",
                f"At Army entry on {item['date']}, {name}'s historical civilian category was {str(item['occupation']).lower()}.",
                f"The official Army field carries historical code {item['code']}; NARA's code list defines it as {item['occupation']}.",
                "High confidence from the reviewed official identity bridge.",
                "Dated at Army entry before the later OSS-index context; no named employer, workplace, duration or exact OSS-transfer date is supplied.",
                "A_direct_official",
                "medium",
                [
                    {"source_key": ARMY, "locator_override": "Reviewed Army entry; raw record and identifier withheld"},
                    {"source_key": TECH, "locator_override": "PDF physical pages 44-46; civilian-occupation field"},
                    {"source_key": CODES, "locator_override": str(item["locator"])},
                ],
                "Published as a qualified historical category only; excluded from verified-employer analytics.",
                f"{slug(name)}-occupation-b985-row{row}",
                "publish_qualified",
            )
        )
    return values


def special_claims() -> list[dict[str, object]]:
    return [
        claim(
            1,
            "identity-george-georg-vetlesen-b985",
            "identity",
            "Indexed George Vetlesen is probably the Norwegian-American OSS officer Georg Unger Vetlesen described by Columbia and Store norske leksikon.",
            "The uncommon surname, George/Georg spelling variant, Navy commander context and responsibility for Norway in OSS London align.",
            "Probable rather than high confidence because the index omits rank and identifiers and the adjacent Frederick Vetlesen row remains separate.",
            "Institutional sources document wartime OSS service and a 1943 Navy entry, while the index file remains necessary for a definitive bridge.",
            "B_authoritative_institutional",
            "medium",
            [{"source_key": INDEX}, {"source_key": COLUMBIA_VETLESEN}, {"source_key": SNL_VETLESEN}],
            "George and Frederick Vetlesen remain separate person entities. No claim or affiliation is transferred between them.",
            publication_status="publish_qualified",
        ),
        claim(
            1,
            "occupation-george-vetlesen-shipbuilding-b985",
            "occupation",
            "The probable Georg Unger Vetlesen match worked for many years as a U.S. shipbuilder and naval engineer before entering the Navy in 1943.",
            "Columbia describes years in shipbuilding and a 1943 Navy entry; Store norske leksikon describes his civilian work as engineering and shipping.",
            "Probable identity bridge from the uncommon name and matching OSS Norway role.",
            "Documented prewar occupation; no named employer or exact immediate-to-Navy sequence is supplied.",
            "B_authoritative_institutional",
            "medium",
            [{"source_key": COLUMBIA_VETLESEN}, {"source_key": SNL_VETLESEN}],
            "Published only as a qualified occupation, excluded from verified-employer analytics.",
            "george-vetlesen-shipbuilding-b985",
            "publish_qualified",
        ),
        claim(
            12,
            "identity-francis-vicovari-b985",
            "identity",
            "Indexed Francis J Vicovari is probably the Francis J. Vicovari who led a British American Ambulance Corps unit in 1941.",
            "Two contemporary sources identify the same uncommon exact name, New York location and ambulance-unit leadership.",
            "Probable identity because neither contemporary source explicitly names later OSS service or the indexed Box 804 file.",
            "The ambulance work is securely dated before U.S. entry into the war; later captivity prevents treating it as explicitly immediate to OSS.",
            "C_reputable_contemporary_or_scholarly",
            "medium",
            [{"source_key": INDEX}, {"source_key": OREGON_VICOVARI}, {"source_key": NEWYORKER_VICOVARI}],
            "Box 804 remains necessary for a definitive person-level bridge.",
            publication_status="publish_qualified",
        ),
        claim(
            12,
            "other-pre-oss-francis-vicovari-baac-b985",
            "other_pre_oss_affiliation",
            "In 1940-1941, Francis J. Vicovari drove ambulances in France and led a British American Ambulance Corps unit bound for Africa.",
            "The New Yorker describes his prior France ambulance work and unit leadership; the Associated Press account identifies him as leader of 24 ambulance drivers.",
            "Probable indexed identity from the uncommon exact name and wartime chronology.",
            "Definitely prewar, but not shown to be the immediate predecessor to OSS service.",
            "C_reputable_contemporary_or_scholarly",
            "medium",
            [{"source_key": OREGON_VICOVARI}, {"source_key": NEWYORKER_VICOVARI}],
            "Volunteer relationship, not assumed paid employment.",
            "francis-vicovari-baac-b985",
            "publish_qualified",
        ),
        claim(
            18,
            "identity-berthold-viertel-b985",
            "identity",
            "Indexed Berthold Viertel is probably the Austrian writer and director documented by the Austrian National Library.",
            "The exact rare name and U.S.-British wartime-era residence align, but the institutional biography does not state an OSS role.",
            "Probable identity; Box 804 is required to establish the personnel-index bridge.",
            "The biography documents film work spanning 1928-1947, including prewar years, but not an immediate OSS sequence.",
            "B_authoritative_institutional",
            "medium",
            [{"source_key": INDEX}, {"source_key": ONB_VIERTEL}],
            "Published with visible qualification and excluded from default confirmed/high analytics.",
            publication_status="publish_qualified",
        ),
        claim(
            18,
            "occupation-berthold-viertel-film-b985",
            "occupation",
            "Berthold Viertel worked as a writer, theater director and film director before and during the OSS period.",
            "The Austrian National Library supplies a dated professional chronology from Vienna through U.S. and British film work.",
            "Probable indexed identity from the exact rare name.",
            "Documented prewar occupation, but the source does not establish whether it immediately preceded or overlapped any OSS affiliation.",
            "B_authoritative_institutional",
            "medium",
            [{"source_key": ONB_VIERTEL}],
            "No employer is inferred from occupation alone.",
            "berthold-viertel-film-b985",
            "publish_qualified",
        ),
        claim(
            19,
            "identity-peter-viertel-b985",
            "identity",
            "Indexed 2nd Lt Peter Viertel is high-confidence matched to writer Peter Viertel, the Marine officer transferred to OSS Secret Intelligence.",
            "The exact rare name, indexed second-lieutenant rank, screenwriting history and explicit Marine-to-OSS chronology align across two institutional sources.",
            "High confidence from exact name, rank, occupation and two independent institutional wartime accounts.",
            "The sources explicitly sequence civilian screenwriting, Marine service and OSS transfer.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": INDEX}, {"source_key": NPS_PETER_VIERTEL}, {"source_key": AUSTRIAN_SOLDIERS}],
            "No full service identifier is retained in public evidence.",
        ),
        claim(
            19,
            "last-civilian-peter-viertel-warner-b985",
            "last_civilian_pre_service",
            "Peter Viertel's last documented civilian employer before Marine service was Warner Bros., where he worked as an office boy and screenwriter.",
            "The institutional chronology names Warner Bros. work before his probable voluntary Marine entry in July 1942; the NPS independently documents screenwriting in 1942.",
            "High-confidence Peter Viertel identity.",
            "Strongly date-bounded as the final named civilian employer before Marine service; exact payroll dates are not supplied.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": AUSTRIAN_SOLDIERS}, {"source_key": NPS_PETER_VIERTEL}],
            "Employer and military pathway are modeled separately.",
            "peter-viertel-warner-b985",
        ),
        claim(
            19,
            "immediate-peter-viertel-marines-b985",
            "immediate_pre_oss_affiliation",
            "Peter Viertel's immediate documented pre-OSS affiliation was the United States Marine Corps.",
            "Both institutional sources state that OSS recruited or transferred him from Marine service after promotion to second lieutenant.",
            "High-confidence Peter Viertel identity.",
            "Explicit immediate military transfer to OSS.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": NPS_PETER_VIERTEL}, {"source_key": AUSTRIAN_SOLDIERS}],
            "Military assignment, not a civilian employer.",
            "peter-viertel-marines-b985",
        ),
        claim(
            20,
            "identity-alexander-orr-vietor-b985",
            "identity",
            "Indexed Alexander O Vietor is probably Yale map scholar Alexander Orr Vietor.",
            "The uncommon first name, surname and middle initial align with Yale's exact expanded name and prewar chronology.",
            "Probable identity because the Yale finding aid does not mention OSS service or a personnel-file identifier.",
            "The source documents civilian employment from 1937 onward but does not establish its relation to OSS service.",
            "B_authoritative_institutional",
            "medium",
            [{"source_key": INDEX}, {"source_key": YALE_VIETOR}],
            "Box 805 remains necessary to close the OSS identity and temporal bridge.",
            publication_status="publish_qualified",
        ),
        claim(
            20,
            "other-pre-oss-alexander-vietor-cox-stevens-b985",
            "other_pre_oss_affiliation",
            "Alexander O. Vietor was an associate of the New York naval architecture firm Cox & Stevens from 1937 to 1940.",
            "Yale's finding aid supplies the firm, role, location and dates.",
            "Probable indexed identity from the uncommon name and middle initial.",
            "Definitely prewar, but not demonstrated as the immediate pre-OSS or last civilian employer.",
            "B_authoritative_institutional",
            "medium",
            [{"source_key": YALE_VIETOR}],
            "Published with visible identity qualification.",
            "alexander-vietor-cox-stevens-b985",
            "publish_qualified",
        ),
        claim(
            20,
            "other-pre-oss-alexander-vietor-yale-b985",
            "other_pre_oss_affiliation",
            "In 1941 Alexander O. Vietor became assistant to the director of the Yale University Art Gallery; Yale named him curator of maps in 1943.",
            "The Yale finding aid supplies the institutional roles and dates.",
            "Probable indexed identity from the uncommon name and middle initial.",
            "Documented prewar work, but the source does not establish whether it immediately preceded, overlapped or followed OSS service.",
            "B_authoritative_institutional",
            "medium",
            [{"source_key": YALE_VIETOR}],
            "The Yale role is not labeled immediate or last civilian employment.",
            "alexander-vietor-yale-b985",
            "publish_qualified",
        ),
        claim(
            21,
            "identity-thomas-f-vietor-jr-b985",
            "identity",
            "Indexed Thomas F Vietor Jr. is high-confidence matched to Princeton alumnus Thomas Frederick Vietor Jr., an OSS sergeant on William Donovan's Washington staff.",
            "Princeton's memorial supplies the exact expanded name, Jr. suffix, class, sergeant rank and explicit OSS assignment.",
            "High confidence from exact expanded identity and explicit institutional OSS account.",
            "The memorial documents Princeton education and wartime OSS service but no intervening civilian employer.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": INDEX}, {"source_key": PRINCETON_VIETOR}],
            "No pre-OSS employer is inferred from postwar advertising work.",
        ),
        claim(
            21,
            "other-pre-oss-thomas-vietor-princeton-b985",
            "other_pre_oss_affiliation",
            "Thomas Frederick Vietor Jr. studied English at Princeton and graduated with the Class of 1938.",
            "Princeton's memorial supplies the major and class year.",
            "High-confidence Thomas Frederick Vietor Jr. identity.",
            "Documented prewar student affiliation, not shown to be immediate to OSS service.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": PRINCETON_VIETOR}],
            "Student status is not an employer and is excluded from verified-employer analytics.",
            "thomas-vietor-princeton-b985",
        ),
    ]


def claims() -> list[dict[str, object]]:
    return army_claims() + special_claims()


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
    values: list[dict[str, object]] = []
    categories = {
        2: "unknown_or_indeterminate",
        4: "unknown_or_indeterminate",
        6: "unknown_or_indeterminate",
        7: "unknown_or_indeterminate",
        8: "unknown_or_indeterminate",
        9: "unknown_or_indeterminate",
        10: "unknown_or_indeterminate",
        11: "unknown_or_indeterminate",
        13: "unknown_or_indeterminate",
        14: "foreign_or_allied_military_personnel",
        22: "unknown_or_indeterminate",
    }
    for row, reason in UNRESOLVED.items():
        values.append(
            base_update(
                row,
                identity_status="unresolved",
                identity_evidence=f"The visually verified page 483 row supplies {PEOPLE[row][1]}, Box {804 if row < 20 else 805} and archive location 230/86/42/05. {reason}",
                personnel_category=categories[row],
                commissioned_officer=True if row == 14 else None,
                allied_or_foreign_personnel=True if row == 14 else False,
                research_status="requires_archival_review",
                next_action=f"Review the indexed personnel file for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}",
            )
        )

    for row, item in ARMY_FINDINGS.items():
        values.append(
            base_update(
                row,
                identity_status="high_confidence",
                identity_evidence=(
                    "The exact rare name, indexed Technical Sergeant rank, dated Army entry and official 2677th Special Reconnaissance Battalion record support a high-confidence match."
                    if row == 16
                    else "The exact official name and a nonshared protected-identifier agreement support the Army identity match; the protected value remains private."
                ),
                personnel_category="enlisted_army_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                research_status="occupation_only_found",
                next_action=f"Review Box {804 if row < 20 else 805} to identify the named employer behind historical occupation code {item['code']} and establish the Army-to-OSS chronology.",
                nara_catalog_id="1263923",
            )
        )

    values.extend(
        [
            base_update(
                1,
                identity_status="probable",
                identity_evidence="The uncommon surname, George/Georg spelling variant, Navy commander context and responsibility for Norway in OSS London align with Georg Unger Vetlesen; adjacent Frederick Vetlesen remains separate.",
                name_variants=["Georg Unger Vetlesen (probable institutional-name bridge)"],
                personnel_category="commissioned_naval_officer",
                commissioned_officer=True,
                allied_or_foreign_personnel=False,
                possible_duplicate_group="p482-483-vetlesen-adjacent-review-b985",
                research_status="occupation_only_found",
                next_action="Review Box 804 with the adjacent Frederick Vetlesen file to confirm the George/Georg identity, preserve the two printed rows correctly and identify any named shipbuilding employer before Navy service.",
                archival_review_priority="critical",
            ),
            base_update(
                5,
                identity_status="high_confidence",
                identity_evidence="Existing official CIA evidence explicitly identifies Rene Veuve as the birth name of OSS member Rene Joyeuse and documents his Free French and resistance pathway.",
                name_variants=["Rene Joyeuse"],
                personnel_category="foreign_or_allied_military_personnel",
                commissioned_officer=True,
                allied_or_foreign_personnel=True,
                manual_review_required=False,
                research_status="completed",
                next_action="The Free French and resistance pathway is documented. Review Box 804 only to refine dates and determine whether a separate civilian employer preceded wartime service.",
                archival_review_priority="medium",
            ),
            base_update(
                12,
                identity_status="probable",
                identity_evidence="Two contemporary sources identify the uncommon exact name, New York location and leadership of the 1941 British American Ambulance Corps unit; Box 804 remains necessary for a definitive OSS bridge.",
                personnel_category="unknown_or_indeterminate",
                commissioned_officer=None,
                allied_or_foreign_personnel=False,
                research_status="completed",
                next_action="The 1940-1941 ambulance affiliation is documented. Review Box 804 to confirm the identity bridge, captivity-to-OSS sequence and any earlier named civilian employer.",
                archival_review_priority="medium",
            ),
            base_update(
                17,
                identity_status="conflicting",
                identity_evidence="The page 483 Edward C Viegel row shares a protected identifier with separately printed Edward C Veigel on page 482, while the Army spelling agrees only with Veigel. No Army finding is transferred.",
                personnel_category="unknown_or_indeterminate",
                commissioned_officer=None,
                allied_or_foreign_personnel=False,
                possible_duplicate_group="p482-483-edward-veigel-viegel-conflict-b985",
                research_status="conflicting_sources",
                next_action="Review Boxes 802 and 804 together to resolve whether Edward C Veigel and Edward C Viegel are duplicate rows or different people before accepting any external identity or pre-OSS claim.",
                archival_review_priority="critical",
            ),
            base_update(
                18,
                identity_status="probable",
                identity_evidence="The exact rare name and U.S.-British film chronology align with the Austrian National Library biography, but the source does not state an OSS role.",
                personnel_category="civilian_professional_or_administrative_grade",
                commissioned_officer=False,
                allied_or_foreign_personnel=True,
                research_status="occupation_only_found",
                next_action="Review Box 804 to establish the personnel-index bridge, immediate pre-OSS status and any named film or theater employer during the relevant period.",
            ),
            base_update(
                19,
                identity_status="high_confidence",
                identity_evidence="The exact rare name, indexed second-lieutenant rank, screenwriting history and explicit Marine-to-OSS chronology align across two institutional sources.",
                personnel_category="commissioned_naval_officer",
                commissioned_officer=True,
                allied_or_foreign_personnel=False,
                research_status="verified_employer_found",
                next_action="Warner Bros. and the Marine-to-OSS pathway are documented. Review Box 804 to refine exact employment and transfer dates.",
                archival_review_priority="medium",
            ),
            base_update(
                20,
                identity_status="probable",
                identity_evidence="The uncommon first name, surname and middle initial align with Yale's Alexander Orr Vietor, but the finding aid does not mention OSS service.",
                name_variants=["Alexander Orr Vietor"],
                personnel_category="civilian_professional_or_administrative_grade",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                research_status="documented_prewar_employer_found",
                next_action="Review Box 805 to confirm the Yale identity and determine which role, if either, immediately preceded or overlapped OSS service.",
            ),
            base_update(
                21,
                identity_status="high_confidence",
                identity_evidence="Princeton's memorial supplies the exact expanded name, Jr. suffix, class, sergeant rank and explicit OSS assignment on William Donovan's Washington staff.",
                name_variants=["Thomas Frederick Vietor Jr."],
                personnel_category="enlisted_army_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                research_status="requires_archival_review",
                next_action="Princeton student status and OSS identity are documented. Review Box 805 to identify the immediate pre-OSS affiliation and last civilian employer between 1938 graduation and wartime service.",
            ),
        ]
    )
    return values


def research_attempts() -> list[dict[str, object]]:
    sourced = set(ARMY_FINDINGS) | {1, 5, 12, 18, 19, 20, 21}
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        if row in sourced:
            outcome = "source_reviewed"
            sources_reviewed = 8 if row in {1, 5, 12, 16, 19, 20, 21} else 6
            rejected = 3
            detail = "Reviewed official, contemporary and institutional sources produced the identity, occupation, student, volunteer, named-employer or military-pathway outcome recorded in the bundle."
        elif row == 17:
            outcome = "candidate_rejected"
            sources_reviewed = 5
            rejected = 4
            detail = "A shared protected identifier and conflicting Veigel/Viegel spelling prevent transfer of the Army candidate or any occupation data."
        elif row in UNRESOLVED:
            outcome = "no_result"
            sources_reviewed = 5
            rejected = 5
            detail = UNRESOLVED[row]
        else:
            outcome = "no_result"
            sources_reviewed = 5
            rejected = 5
            detail = "The staged protocol produced no reliable person-level identity or pre-OSS affiliation bridge."
        attempts.append(
            {
                "key": f"page483-row{row}-{slug(name)}-b985",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index and official Archives context; CIA Reading Room or equivalent official-source check; exact-name and meaningful variants; OSS, Army, Navy, Marines, rank, branch and assignment clues; employer and occupation 1940; obituary, institutional, newspaper, directory, Library of Congress and archival searches; indexed Box {804 if row < 20 else 805}; protected identifiers used only in private official-record comparison",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_985",
                "started_at": "2026-10-30T12:10:00Z",
                "completed_at": "2026-10-30T13:20:00Z",
                "outcome": outcome,
                "sources_reviewed": sources_reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, snippets, commercial people-finder pages, relatives, unsourced genealogy, postwar-only leads and sources without an OSS, protected-identifier, rank, unit or personnel-file bridge were rejected. Historical occupation categories, student status, volunteer work and military assignments were not converted into employers.",
                "research_notes": f"{detail} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain and archival searches were checked as applicable. The index page, official Army comparison, technical field definitions and every cited code-list page were inspected directly. Yale's finding-aid page was checked against a rendered page image. No search-result snippet was used as sole final evidence, no paywall or access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": "Review the indexed personnel file for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before wartime service.",
                "attempt_number": 2 if row == 5 else 1,
                "research_agent_version": "before-oss-b985-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-985-v1",
        "reviewer": "Before OSS Batch 985 evidence review",
        "sources": sources(),
        "organizations": organizations(),
        "affiliations": affiliations(),
        "claims": claims(),
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }
    EvidenceBundle.model_validate(bundle)
    OUTPUT.write_text(
        json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
