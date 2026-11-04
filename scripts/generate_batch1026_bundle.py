#!/usr/bin/env python3
"""Generate the reviewed Batch 1026 evidence bundle for PDF page 516."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page516-william-wynn-to-george-yasukochi-review_"
    "batch-1026_2026-11-04.json"
)

INDEX = "nara-index-b1026"
ARMY = "army-bulk-b1026"
TECH = "army-tech-b1026"
CODES = "army-codes-b1026"
XANTHOPOULOS = "oss-battle-award-xanthopoulos-b1026"
WA_POST_YAFFE = "washington-post-yaffe-b1026"
GILA_YAHANDA = "gila-news-courier-yahanda-b1026"
PARK_BUGLE_YAHANDA = "park-bugle-yahanda-b1026"
DENSHO_YAMAMOTO = "pacemaker-yamamoto-b1026"
PENN_YAMAMOTO = "penn-language-log-yamamoto-b1026"
PACIFIC_CITIZEN_YAMAZAKI = "pacific-citizen-yamazaki-b1026"
CIA_FBIS = "cia-fbis-yanaga-b1026"
WASEDA_YANAGA = "waseda-yanaga-b1026"
OXFORD_YARMOLINSKY = "oxford-yarmolinsky-b1026"
CRIMSON_YARMOLINSKY = "crimson-yarmolinsky-b1026"
EISENHOWER_YARROW = "eisenhower-yarrow-b1026"

ORG_US_ARMY = "us-army-existing-b1026"
ORG_HARVARD = "harvard-existing-b1026"
ORG_ARMY_AIR_CORPS = "army-air-corps-existing-b1026"
ORG_SELF_EMPLOYED = "self-employed-existing-b1026"
ORG_GILA = "gila-river-relocation-center-b1026"
ORG_NAVY_LEAGUE = "philadelphia-navy-league-school-b1026"
ORG_NAVY_LANGUAGE_BOULDER = "navy-language-school-boulder-existing-b1026"
ORG_NEW_WORLD_SUN = "new-world-sun-b1026"
ORG_SANGYO_NIPPO = "sangyo-nippo-b1026"
ORG_UC_BERKELEY = "uc-berkeley-existing-b1026"
ORG_NAVY_LANGUAGE = "navy-language-school-existing-b1026"
ORG_OWI = "owi-existing-b1026"
ORG_FBIS = "fbis-existing-b1026"
ORG_NYC_DA = "nyc-da-existing-b1026"

PEOPLE = {
    1: ("71194404-92a8-5be9-b1de-a21f058d7fa0", "William J Wynn", "856"),
    2: ("ae5245a1-6ded-5007-9442-5f81772309af", "Eleanor G Wynne", "856"),
    3: ("bd8c7c10-60f3-5300-b374-404b904d1a8a", "Matthew Wysocki", "856"),
    4: ("3479fda3-536c-5125-b264-d20aafdf7af3", "Winton Wysocki", "856"),
    5: ("aaffa12b-2686-527b-b49b-e24cef164bb6", "Glen D Wysong", "856"),
    6: ("ca32abc9-7b7a-5946-bd4f-0f8aab7bea84", "Jean C Wysong", "856"),
    7: ("efb85d82-fa0e-569e-a6ec-9bb4bcf83ce0", "Michael D Wythe", "856"),
    8: ("bbd08a25-0e34-51de-a2e7-542ef5aefe8e", "* X", "856"),
    9: ("131320a3-459b-58f2-a229-38a074c5c3a1", "Louis J Xanthopoulos", "856"),
    10: ("92e109fd-5086-5e85-9570-354a4dc31f78", "Charles W Yacin", "856"),
    11: ("b7c478ce-48d1-509b-a84f-cdead310eb15", "Edith B Yaciw", "856"),
    12: ("18308f5a-58a4-55b6-816e-297926c18557", "Nicholas Yacob", "856"),
    13: ("701b086a-f319-5aab-8b35-c4e073090839", "Sumner J Yaffe", "856"),
    14: ("abcaf0e6-2355-5bda-ba0d-07e10e8cabe7", "Joseph A Yager Jr.", "856"),
    15: ("6005c55f-475d-50f9-8823-6d97a730e295", "Albert Yaggi", "856"),
    16: ("c169789b-c27a-5721-a7f9-4a50cc73d7c9", "Teizo Yahanda", "856"),
    17: ("aeb0e377-880e-5adf-9aaf-c5a4d0cb329c", "Arthur M Yahiro", "856"),
    18: ("26d9685c-73ec-57e2-bfd7-20237fc0a610", "Pierre J Yakes", "856"),
    19: ("68749985-bda3-5980-894f-9dc38f9cb4c7", "William F Yakey", "856"),
    20: ("87c1940d-257a-546e-b112-2e609262c6bf", "Thomas B Yale", "856"),
    21: ("146ef530-6128-5e09-836e-da4cecdf13b8", "Hatsumi Yamada", "856"),
    22: ("fa3a7e26-be34-5233-a698-c9b387538e99", "Sylvia Yamalaki", "856"),
    23: ("6385e145-dbc4-57bf-a947-c1abde87659f", "Kiyoshi Yamamoto", "856"),
    24: ("694e706b-bf34-5b36-96cf-10bda80cd32c", "Sannosuke Yamamoto", "857"),
    25: ("58a58dae-030f-5679-b412-a4b2e06ff5c2", "Thomas S Yamamoto", "857"),
    26: ("d21924dc-6368-5b04-b419-02f67feffb6c", "Jack C Yamasaki", "857"),
    27: ("dc715ed3-fd0c-53ee-aa8a-a9cdd07713c7", "Nawoto Yamauchi", "857"),
    28: ("8642e536-31e3-5988-be3b-9c87159b846b", "Tomomasa Yamazaki", "857"),
    29: ("9a228001-aa0d-5872-85db-78fc9d4600f4", "Ohitoshi Yanaga", "857"),
    30: ("d88e56da-df9b-5494-b6e6-1f8fa79951d9", "Abe Yanches", "856"),
    31: ("53fc0caa-0581-5681-9a53-023c70851e42", "Alexander Yaney Jr.", "857"),
    32: ("a59bf3fb-ccf7-54c6-8c9a-6df2cac5cb2c", "Richard R Yanke", "857"),
    33: ("b4db6ca0-5aae-57bb-9086-2d016197777b", "Isaac Yano", "857"),
    34: ("f17b3d16-f454-5afa-ae92-e90ac266b670", "Elias Yanovsky", "857"),
    35: ("ae3c110f-62d4-50e5-8a1b-b701bdc7550b", "Shan-Yu Yao", "857"),
    36: ("59940cbc-2ff8-57ab-9dd4-7a6d20d8ee1b", "John T Yarborough", "857"),
    37: ("cbb3dacb-f0a4-56f1-909c-8203e73f5fa2", "Elmo E Yarbrough", "857"),
    38: ("c11f1cc7-d458-54fd-8200-8f39d5cb4e98", "William S Yarbrough", "857"),
    39: ("adb39191-76c6-59e0-a77b-7c520345b122", "John Yarmey", "857"),
    40: ("c745600c-6f17-5254-92a8-5704677223ab", "Adam Yarmolinsky", "857"),
    41: ("a78b210f-08ba-5c72-b1fa-a7c95ce04626", "Beatrice M Yarrington", "857"),
    42: ("137fec8f-6764-5c2b-8353-2abbc225eca0", "Marion Yarrington", "857"),
    43: ("902d2511-80f5-5681-b32f-43e0643c61e2", "Andrew H Yarrow", "857"),
    44: ("cb3f3e20-4d50-5108-95a7-84f5a9d97472", "Bernard Yarrow", "857"),
    45: ("27075e38-db18-5511-aa78-cda30bdf7bc0", "Sylvia T Yarrow", "857"),
    46: ("6a02bf01-35bd-5a1d-9f99-6fda905fc905", "George Yasukochi", "857"),
}

ARMY_OCCUPATIONS = {
    9: ("1941-03-17", "071", "hotel or restaurant manager", "Managers, hotels and restaurants", "PDF physical page 171; historical category 0-71"),
    10: ("1942-05-23", "688", "mechanical treatment of metals occupation, not elsewhere classified", "Mechanical treatment of metals, n.e.c.", "PDF physical page 174; historical category 6-88"),
    12: ("1942-10-15", "893", "fabrication of metal products occupation, not elsewhere classified", "Fabrication of metal products, n.e.c.", "PDF physical page 174; historical category 8-93"),
    13: ("1943-02-15", "992", "student", "Students", "PDF physical page 304; amended category 9-92"),
    14: ("1944-01-26", "105", "general office clerk", "General office clerks", "PDF physical page 171; historical category 1-05"),
    18: ("1944-02-25", "723", "construction machinery operator, not elsewhere classified", "Construction machinery operators, n.e.c.", "PDF physical page 174; historical category 7-23"),
    21: ("1942-12-14", "306", "general farmer", "Farmers, general", "PDF physical page 172; historical category 3-06"),
    27: ("1944-08-15", "959", "trade or service occupation, not elsewhere classified", "Trades and services, n.e.c.", "PDF physical page 174; historical category 9-59"),
    30: ("1942-10-15", "185", "salesperson or sales agent, except to consumers", "Salesmen and sales agents, except to consumers", "PDF physical page 172; historical category 1-85"),
    32: ("1942-07-25", "142", "telephone operator", "Telephone operators", "PDF physical page 171; historical category 1-42"),
    37: ("1942-07-11", "736", "chauffeur or driver of a bus, taxi, truck, or tractor", "Chauffeurs and drivers, bus, taxi, truck, and tractor", "PDF physical page 174; historical category 7-36"),
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def source(key: str, **kwargs: object) -> dict[str, object]:
    value: dict[str, object] = {"key": key, "access_date": "2026-11-04"}
    value.update(kwargs)
    return value


def sources() -> list[dict[str, object]]:
    return [
        source(INDEX, stable_url="https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf", archival_identifier="RG 226, Entry A1-224, Boxes 856-857", title="OSS Personnel Files from Excel", author_creator="National Archives and Records Administration", repository_publisher="National Archives and Records Administration", publication_record_date="2010-12-23", locator="PDF page 516, rows 1-46; page 517 boundary and all page 516 rows visually checked at 180 dpi", source_quality="A_direct_official", collection_name="Records of the Office of Strategic Services, Record Group 226", rights_notes="All 46 printed rows remain separate. Full protected identifiers remain private."),
        source(ARMY, source_id="cf280d3e-1262-5963-90d7-40ffa66c53a3", stable_url="https://catalog.archives.gov/id/1263923", archival_identifier="National Archives Identifier 1263923; parent series NAID 604357", title="Electronic Army Serial Number Merged File, ca. 1938-1946", author_creator="Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration", repository_publisher="National Archives and Records Administration", publication_record_date="1938-1946; merged file created 2002", locator="Official unrestricted ASNEF.FIN.DAT; twelve Batch 1026 protected-identifier candidates reviewed", source_quality="A_direct_official", collection_name="World War II Army Enlistment Records", document_number="ASNEF.FIN.DAT", rights_notes="No raw record or full protected identifier is retained in public assets. Coded occupations identify neither employer nor workplace."),
        source(TECH, source_id="f24044fe-5fcd-5d78-96d4-25d577e90703", stable_url="https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf", archival_identifier="NN3-064-03-008; National Archives Identifier 1263923", title="World War II Army Enlistment Records: Reference Copy of Technical Documentation", author_creator="National Archives and Records Administration", repository_publisher="National Archives at College Park - Electronic Records", publication_record_date="1994-2005; reference copy modified 2011", locator="PDF physical pages 44-46; identifier, name, Army-entry-date, grade and civilian-occupation fields", source_quality="A_direct_official", collection_name="World War II Army Enlistment Records technical documentation", rights_notes="Used to interpret selected fields only; source damage, coding limits and incomplete coverage remain applicable."),
        source(CODES, source_id="ace136c1-722a-5af0-a43b-bab53792ae6a", stable_url="https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1CL_SD.pdf", archival_identifier="National Archives Identifier 1263923; Code No. 30", title="NARA Compiled Code Lists for the Electronic Army Serial Number Merged File", author_creator="National Archives and Records Administration", repository_publisher="National Archives at College Park - Electronic Records", publication_record_date="2011-01-12; modified 2011-03-17", locator="PDF physical pages 170-175 and 304; Batch 1026 categories visually checked", source_quality="A_direct_official", collection_name="World War II Army Enlistment Records technical documentation", rights_notes="Historical categories identify neither employer, institution nor workplace."),
        source(XANTHOPOULOS, stable_url="https://documents3.theblackvault.com/documents/jfkfiles/NARA-Oct2017/NARA-Nov-2017/104-10165-10120.pdf", archival_identifier="NARA release document 104-10165-10120", title="Battle Participation Awards - Germany Campaign (No. 2)", author_creator="Headquarters, European Theater of Operations, Office of Strategic Services", repository_publisher="National Archives release; public mirror by The Black Vault", publication_record_date="1945-05-03", locator="PDF physical page 5; 31st Field Detachment list visually checked", source_quality="A_direct_official", collection_name="Declassified OSS records", document_number="104-10165-10120", rights_notes="The public mirror reproduces a declassified official record. Full service numbers are not republished."),
        source(WA_POST_YAFFE, stable_url="https://www.washingtonpost.com/local/obituaries/sumner-j-yaffe-nih-official/2011/08/24/gIQAQSIeeJ_story.html", title="Sumner J. Yaffe, NIH official", author_creator="Matt Schudel", repository_publisher="The Washington Post", publication_record_date="2011-08-25", locator="Biographical paragraphs covering Harvard study, wartime Army intelligence and postwar degrees", source_quality="C_reputable_contemporary_or_scholarly", rights_notes="Obituary chronology is used with the exact protected-identifier Army match; unrelated family details are not retained."),
        source(GILA_YAHANDA, stable_url="https://tile.loc.gov/storage-services/service/sgp/sgpbatches/batch_dlc_anacostia_ver01/data/sn83025353/00237288671/1945031001/1464.pdf", archival_identifier="Chronicling America, Gila News-Courier, March 10, 1945, page 7", title="Yahanda Visits Monterey, Calif.", repository_publisher="Gila News-Courier; Library of Congress Chronicling America", publication_record_date="1945-03-10", locator="PDF physical page 1, newspaper page 7; Teizo Yahanda item visually checked", source_quality="C_reputable_contemporary_or_scholarly", collection_name="Chronicling America", rights_notes="Contemporary camp newspaper; the block-manager role is not silently converted into private employment."),
        source(PARK_BUGLE_YAHANDA, stable_url="https://www.parkbugle.org/wp-content/uploads/backissues/1980/10.pdf", title="The Yahandas: a family for all seasons", repository_publisher="Park Bugle", publication_record_date="1980-10", locator="PDF physical page 3; prewar Carmel dry-cleaning and alterations business visually checked", source_quality="C_reputable_contemporary_or_scholarly", rights_notes="Community-newspaper retrospective. The Army draft passage concerns Teizo's son David and is not attributed to Teizo."),
        source(DENSHO_YAMAMOTO, stable_url="https://encyclopedia.densho.org/media/ddr-densho-146/ddr-densho-146-26-mezzanine-aafee7a861.pdf", archival_identifier="Densho Digital Repository ddr-densho-146-26; Pacemaker, July 15, 1942, page 6", title="Pacemaker, July 15, 1942, page 6", repository_publisher="Pacemaker; Densho Digital Repository", publication_record_date="1942-07-15", locator="Page 6 item reporting that Sannosuke Yamamoto was teaching Japanese to five Marines in Philadelphia", source_quality="C_reputable_contemporary_or_scholarly", collection_name="Densho Digital Repository", rights_notes="Contemporary newspaper evidence; the exact OSS transition date is not supplied."),
        source(PENN_YAMAMOTO, stable_url="https://itre.cis.upenn.edu/~myl/languagelog/archives/002553.html", title="The interpreter shortage", author_creator="Bill Poser", repository_publisher="Language Log, University of Pennsylvania", publication_record_date="2005-10-17", locator="Description of the 1944 title page for Japanese for Military and Civilian Use", source_quality="C_reputable_contemporary_or_scholarly", rights_notes="The scholarly description transcribes Yamamoto's historical title as Instructor of Japanese, Philadelphia Navy League School."),
        source(PACIFIC_CITIZEN_YAMAZAKI, stable_url="https://pacificcitizen.org/wp-content/uploads/archives-menu/Vol.023_%2324_Dec_21_1946.pdf", title="Tomomasa Yamazaki, former California newspaperman, among 22 victims of air tragedy", repository_publisher="Pacific Citizen", publication_record_date="1946-12-21", locator="PDF physical page 41; wartime biography visually checked", source_quality="C_reputable_contemporary_or_scholarly", collection_name="Pacific Citizen archive", rights_notes="Contemporary obituary identifies the Navy-school, Army-intelligence and newspaper chronology; it does not itself name OSS."),
        source(CIA_FBIS, stable_url="https://www.cia.gov/resources/csi/static/fbis-against-the-axis.pdf", archival_identifier="Studies in Intelligence, FBIS Against the Axis, 1941-1945", title="FBIS Against the Axis, 1941-1945: Open-Source Intelligence From the Airwaves", author_creator="Stephen C. Mercado", repository_publisher="Central Intelligence Agency, Center for the Study of Intelligence", publication_record_date="2001", locator="PDF physical page 4, printed page 3; Chitoshi Yanaga paragraph visually checked", source_quality="A_direct_official", collection_name="Studies in Intelligence", rights_notes="Official historical article; used with the dated institutional chronology rather than as a standalone OSS identity bridge."),
        source(WASEDA_YANAGA, stable_url="https://memory.w.waseda.jp/newsletter/619", archival_identifier="Waseda University Memory and Reconciliation Studies newsletter essay 619", title="Japanese Americans Who Contributed to the U.S. War Effort - As Soldiers and Civilians in the Pacific Theater", repository_publisher="Waseda University, Institute for Reconciliation Studies", publication_record_date="2025", locator="Sections on Chitoshi Yanaga; dated 1937-45 career list; explicit statement that indexed Ohitoshi is a misspelling of Chitoshi", source_quality="B_authoritative_institutional", rights_notes="Institutional essay cites the indexed NARA personnel file and preserves the misspelling as a documented variant rather than silently correcting it."),
        source(OXFORD_YARMOLINSKY, stable_url="https://academic.oup.com/american-national-biography/reference/63042/reference-article-abstract/570587837", archival_identifier="American National Biography, article 0700853", title="Yarmolinsky, Adam (1922-2000), public policymaker", author_creator="Russell Stevenson", repository_publisher="Oxford University Press", publication_record_date="2014-10", locator="Biographical extract covering Harvard College graduation in 1943 and U.S. Army Air Corps enlistment", source_quality="C_reputable_contemporary_or_scholarly", rights_notes="The biography supplies chronology but not an OSS identity bridge; publication remains qualified."),
        source(CRIMSON_YARMOLINSKY, stable_url="https://www.thecrimson.com/article/1776/1/22/wsc-holds-open-meeting-tonight-ptonights/", title="WSC Holds Open Meeting Tonight", repository_publisher="The Harvard Crimson", locator="Contemporary item identifying Adam Yarmolinsky '43 as Harvard War Service Committee chairman", source_quality="C_reputable_contemporary_or_scholarly", rights_notes="Contemporary student-newspaper corroboration; the displayed archival date is unreliable and is not used."),
        source(EISENHOWER_YARROW, stable_url="https://www.eisenhowerlibrary.gov/sites/default/files/finding-aids/pdf/yarrow-bernard-papers.pdf", archival_identifier="Bernard Yarrow Papers, Eisenhower Presidential Library", title="Bernard Yarrow Papers, 1907-1973", author_creator="Dwight D. Eisenhower Presidential Library", repository_publisher="National Archives and Records Administration", locator="PDF physical page 2; private law practice, assistant district attorney appointment and November 1942 OSS transition visually checked", source_quality="B_authoritative_institutional", collection_name="Bernard Yarrow Papers", rights_notes="Official finding aid supplies an explicit immediate transition; no unrelated family details are reproduced."),
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {"key": ORG_US_ARMY, "organization_id": "28a26f92-78af-5a1a-9c09-a843eb5975b4", "canonical_name": "United States Army", "historical_name": "United States Army", "aliases": ["U.S. Army", "Army"], "organization_type": "military service", "sector": "military", "country": "United States", "normalization_notes": "Military assignment remains separate from civilian employment."},
        {"key": ORG_HARVARD, "organization_id": "45ddf347-21c6-59f5-a8ae-517418adf941", "canonical_name": "Harvard University", "historical_name": "Harvard University", "organization_type": "university", "sector": "academia_and_research", "city": "Cambridge", "state_or_region": "Massachusetts", "country": "United States", "normalization_notes": "Student status is not counted as employment."},
        {"key": ORG_ARMY_AIR_CORPS, "organization_id": "27378252-f855-504f-b916-d3fb6fb40fd0", "canonical_name": "United States Army Air Corps", "historical_name": "U.S. Army Air Corps", "aliases": ["Army Air Corps"], "organization_type": "military air arm", "sector": "military", "country": "United States", "normalization_notes": "The biography's historical wording is preserved."},
        {"key": ORG_SELF_EMPLOYED, "organization_id": "2d0f4eae-d528-5d59-8b11-6660b1e4fa4a", "canonical_name": "Self-employed", "historical_name": "Self-employed", "organization_type": "self-employment", "sector": "self_employed", "country": "United States", "normalization_notes": "Used only where ownership or operation of one's own business is stated."},
        {"key": ORG_GILA, "canonical_name": "Gila River Relocation Center", "historical_name": "Gila River Relocation Center", "aliases": ["Canal Camp", "Canal"], "organization_type": "War Relocation Authority detention center", "sector": "federal_government", "city": "Rivers", "state_or_region": "Arizona", "country": "United States", "active_dates": "1942-1945", "normalization_notes": "The coercive incarceration context is explicit; a block-manager role is not recast as ordinary private employment."},
        {"key": ORG_NAVY_LEAGUE, "canonical_name": "Philadelphia Navy League School", "historical_name": "Philadelphia Navy League School", "organization_type": "wartime language school", "sector": "military", "city": "Philadelphia", "state_or_region": "Pennsylvania", "country": "United States", "normalization_notes": "Historical name from the 1944 book title page; no modern successor is substituted."},
        {"key": ORG_NAVY_LANGUAGE_BOULDER, "organization_id": "4b6ddf65-f2de-5c0e-8268-012c61b37279", "canonical_name": "U.S. Navy Japanese Language School, Boulder", "historical_name": "Naval Language School in Boulder", "aliases": ["Navy school at Boulder"], "organization_type": "military language school", "sector": "military", "city": "Boulder", "state_or_region": "Colorado", "country": "United States", "normalization_notes": "Civilian teaching at the military school remains employment rather than military service."},
        {"key": ORG_NEW_WORLD_SUN, "canonical_name": "New World-Sun", "historical_name": "New World-Sun", "organization_type": "Japanese American newspaper", "sector": "journalism_and_media", "city": "San Francisco", "state_or_region": "California", "country": "United States", "active_dates": "1935-1942", "normalization_notes": "The hyphenated historical newspaper name from the contemporary source is preserved."},
        {"key": ORG_SANGYO_NIPPO, "canonical_name": "Sangyo Nippo", "historical_name": "Sangyo Nippo", "organization_type": "Japanese American newspaper", "sector": "journalism_and_media", "city": "Los Angeles", "state_or_region": "California", "country": "United States", "normalization_notes": "Historical newspaper identity is preserved without silent merger into another Japanese-language publication."},
        {"key": ORG_UC_BERKELEY, "organization_id": "dd5d0a44-0368-5e91-a5d3-074de36840ed", "canonical_name": "University of California, Berkeley", "historical_name": "University of California, Berkeley", "organization_type": "university", "sector": "academia_and_research", "city": "Berkeley", "state_or_region": "California", "country": "United States", "normalization_notes": "The Waseda chronology and official CIA history identify the Berkeley teaching role."},
        {"key": ORG_NAVY_LANGUAGE, "organization_id": "1fa7fc4e-b1c2-5794-94e2-986180d3820f", "canonical_name": "United States Navy Japanese Language School", "historical_name": "Naval Intelligence Language School", "aliases": ["U.S. Navy Japanese Language School"], "organization_type": "United States Navy language school", "sector": "military", "country": "United States", "normalization_notes": "Historical teaching assignment remains distinct from uniformed military service."},
        {"key": ORG_OWI, "organization_id": "d907505c-05ff-502a-810c-e6189e186543", "canonical_name": "United States Office of War Information", "historical_name": "Office of War Information", "aliases": ["OWI"], "organization_type": "federal wartime information agency", "sector": "federal_government", "country": "United States", "active_dates": "1942-1945", "normalization_notes": "Government assignment is separate from private employment."},
        {"key": ORG_FBIS, "organization_id": "82743d08-1a05-5ef9-ab62-6fa33b67c90c", "canonical_name": "Foreign Broadcast Intelligence Service, Federal Communications Commission", "historical_name": "Foreign Broadcast Intelligence Service", "aliases": ["FBIS"], "organization_type": "federal foreign-broadcast intelligence service", "sector": "federal_government", "country": "United States", "normalization_notes": "The dated 1944 adviser role is the best-supported immediate institutional predecessor to OSS."},
        {"key": ORG_NYC_DA, "organization_id": "9c396f0e-f44b-51b6-bda3-bea8c292236c", "canonical_name": "New York County District Attorney's Office", "historical_name": "Office of the District Attorney, New York County", "aliases": ["New York County District Attorney's Office"], "organization_type": "county prosecutor's office", "sector": "state_or_local_government", "city": "New York", "state_or_region": "New York", "country": "United States", "normalization_notes": "The Rackets Bureau role is preserved as a civilian government assignment."},
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
        identity = "high_confidence" if row in {10, 30} else "confirmed"
        relationship = "student" if row == 13 else "unknown"
        values.append(affiliation(
            f"{slug(PEOPLE[row][1])}-army-occupation-b1026", row, relationship,
            "strongly_date_bounded", identity, "medium", "A_direct_official", "publish_qualified",
            occupation=occupation, end_date=date,
            date_precision=f"Historical civilian-occupation code {code} was recorded at Army entry on {date}; no named employer or institution is supplied.",
            country="United States", immediate_pre_oss=False, last_civilian_pre_service=False,
            research_notes="Broad historical category only; excluded from verified-employer analytics and not narrowed beyond the official wording.",
        ))
    values.extend([
        affiliation("sumner-yaffe-harvard-student-b1026", 13, "student", "strongly_date_bounded", "confirmed", "high", "C_reputable_contemporary_or_scholarly", organization_key=ORG_HARVARD, organization_name_as_found="Harvard University", role_title="student", end_date="1943", date_precision="The obituary says Harvard studies were interrupted by World War II; the official Army record dates entry to February 15, 1943 and codes civilian status as student.", city="Cambridge", state_or_region="Massachusetts", country="United States", immediate_pre_oss=False, last_civilian_pre_service=False, research_notes="Student status is not classified as employment; Army intelligence intervened before any OSS assignment."),
        affiliation("teizo-yahanda-gila-b1026", 16, "unknown", "documented_prewar", "probable", "medium", "C_reputable_contemporary_or_scholarly", "publish_qualified", organization_key=ORG_GILA, organization_name_as_found="Canal", role_title="central block manager", end_date="1945-03", date_precision="Contemporary camp newspaper identifies the role on March 10, 1945; the OSS start date is not supplied.", city="Rivers", state_or_region="Arizona", country="United States", immediate_pre_oss=False, last_civilian_pre_service=False, research_notes="Role occurred within forced incarceration and is not labeled ordinary employment. Exact OSS sequence requires the personnel file."),
        affiliation("teizo-yahanda-self-employed-b1026", 16, "self_employment", "documented_prewar", "probable", "medium", "C_reputable_contemporary_or_scholarly", "publish_qualified", organization_key=ORG_SELF_EMPLOYED, organization_name_as_found="a successful dry cleaning and alterations business", role_title="co-owner", occupation="dry cleaner and alterations business owner", end_date="1942", date_precision="The retrospective places the Carmel business before wartime incarceration; exact start and closure dates are not supplied.", city="Carmel", state_or_region="California", country="United States", immediate_pre_oss=False, last_civilian_pre_service=True, research_notes="Published as a qualified prewar self-employment finding; the retrospective source and unbridged OSS start prevent a settled immediate claim."),
        affiliation("sannosuke-yamamoto-navy-league-b1026", 24, "employment", "temporal_relation_uncertain", "probable", "medium", "C_reputable_contemporary_or_scholarly", "publish_qualified", organization_key=ORG_NAVY_LEAGUE, organization_name_as_found="Philadelphia Navy League School", role_title="instructor of Japanese", start_date="1942", end_date="1944", date_precision="A July 1942 contemporary item reports teaching Marines; the 1944 book title page names the school and title. Exact OSS entry remains unknown.", city="Philadelphia", state_or_region="Pennsylvania", country="United States", immediate_pre_oss=False, last_civilian_pre_service=False, research_notes="The job is documented, but cannot yet be labeled immediate or definitively pre-OSS without the Box 857 file."),
        affiliation("tomomasa-yamazaki-navy-school-b1026", 28, "employment", "strongly_date_bounded", "probable", "medium", "C_reputable_contemporary_or_scholarly", "publish_qualified", organization_key=ORG_NAVY_LANGUAGE_BOULDER, organization_name_as_found="Navy school at Boulder, Colo.", role_title="language instructor", end_date="1945", date_precision="The 1946 obituary says Yamazaki volunteered for Army intelligence after serving as a Navy-school language instructor; exact dates are not supplied.", city="Boulder", state_or_region="Colorado", country="United States", immediate_pre_oss=False, last_civilian_pre_service=True, research_notes="Best-supported last civilian employer before Army intelligence, but not labeled immediate pre-OSS because the article does not name OSS."),
        affiliation("tomomasa-yamazaki-new-world-sun-b1026", 28, "employment", "documented_prewar", "probable", "medium", "C_reputable_contemporary_or_scholarly", "publish_qualified", organization_key=ORG_NEW_WORLD_SUN, organization_name_as_found="New World-Sun", role_title="editorial staff member", end_date="1942", date_precision="The contemporary obituary says he formerly served on the editorial staff; exact dates and order relative to Sangyo Nippo are not supplied.", city="San Francisco", state_or_region="California", country="United States", immediate_pre_oss=False, last_civilian_pre_service=False, research_notes="Earlier documented employment; not promoted to immediate or last employer."),
        affiliation("tomomasa-yamazaki-sangyo-nippo-b1026", 28, "employment", "documented_prewar", "probable", "medium", "C_reputable_contemporary_or_scholarly", "publish_qualified", organization_key=ORG_SANGYO_NIPPO, organization_name_as_found="Sangyo Nippo", role_title="editorial staff member", end_date="1942", date_precision="The contemporary obituary says he formerly served on the editorial staff; exact dates and order relative to New World-Sun are not supplied.", city="Los Angeles", state_or_region="California", country="United States", immediate_pre_oss=False, last_civilian_pre_service=False, research_notes="Earlier documented employment; not promoted to immediate or last employer."),
        affiliation("chitoshi-yanaga-berkeley-b1026", 29, "employment", "strongly_date_bounded", "high_confidence", "high", "B_authoritative_institutional", organization_key=ORG_UC_BERKELEY, organization_name_as_found="University of California", role_title="instructor in Japanese history and government", start_date="1937", end_date="1942", date_precision="The Waseda chronology dates the appointment 1937-42; CIA history independently says he taught at the University of California.", city="Berkeley", state_or_region="California", country="United States", immediate_pre_oss=False, last_civilian_pre_service=True, research_notes="Last documented civilian employer before intervening wartime government assignments; not immediate pre-OSS."),
        affiliation("chitoshi-yanaga-navy-language-b1026", 29, "government_assignment", "strongly_date_bounded", "high_confidence", "high", "A_direct_official", organization_key=ORG_NAVY_LANGUAGE, organization_name_as_found="US Navy Japanese Language School", role_title="instructor of intelligence officers", end_date="1942", date_precision="CIA history places the language-school instruction before OWI; precise dates are not supplied.", country="United States", immediate_pre_oss=False, last_civilian_pre_service=False, research_notes="Government teaching assignment remains separate from university employment."),
        affiliation("chitoshi-yanaga-owi-b1026", 29, "government_assignment", "strongly_date_bounded", "high_confidence", "high", "B_authoritative_institutional", organization_key=ORG_OWI, organization_name_as_found="Office of War Information", role_title="Director of Japanese Translation and Research", start_date="1942", end_date="1944", date_precision="Waseda reproduces a dated career list for 1942-44; CIA history independently describes him as heading Japanese translation and research.", country="United States", immediate_pre_oss=False, last_civilian_pre_service=False, research_notes="Documented intervening federal assignment before FBIS and OSS."),
        affiliation("chitoshi-yanaga-fbis-b1026", 29, "government_assignment", "strongly_date_bounded", "high_confidence", "high", "B_authoritative_institutional", organization_key=ORG_FBIS, organization_name_as_found="Foreign Broadcast Intelligence Service, F.C.C.", role_title="Far Eastern Adviser", start_date="1944", end_date="1944", date_precision="The dated chronology places FBIS in 1944 immediately before OSS and State Department service in 1944-45.", country="United States", immediate_pre_oss=True, last_civilian_pre_service=False, research_notes="Best-supported immediate institutional predecessor; exact transfer day remains unavailable."),
        affiliation("adam-yarmolinsky-harvard-b1026", 40, "student", "documented_prewar", "probable", "medium", "C_reputable_contemporary_or_scholarly", "publish_qualified", organization_key=ORG_HARVARD, organization_name_as_found="Harvard College", role_title="student; Harvard War Service Committee chairman", end_date="1943", date_precision="American National Biography dates graduation to 1943; a contemporary Crimson item identifies his committee role.", city="Cambridge", state_or_region="Massachusetts", country="United States", immediate_pre_oss=False, last_civilian_pre_service=False, research_notes="Student status is not employment; no direct OSS identity bridge has been found."),
        affiliation("adam-yarmolinsky-army-air-corps-b1026", 40, "military_assignment", "temporal_relation_uncertain", "probable", "medium", "C_reputable_contemporary_or_scholarly", "publish_qualified", organization_key=ORG_ARMY_AIR_CORPS, organization_name_as_found="U.S. Army Air Corps", role_title="enlisted servicemember", start_date="1943", end_date="1946", date_precision="The biography says he enlisted after his 1943 Harvard graduation; another official chronology dates military service 1943-46, but no exact OSS sequence is supplied.", country="United States", immediate_pre_oss=False, last_civilian_pre_service=False, research_notes="Military pathway is qualified pending the Box 857 personnel file."),
        affiliation("bernard-yarrow-nyc-da-b1026", 44, "government_assignment", "explicit_immediate", "high_confidence", "high", "B_authoritative_institutional", organization_key=ORG_NYC_DA, organization_name_as_found="assistant district attorney", role_title="assistant district attorney, Rackets Bureau", start_date="1938-01-01", end_date="1942-11", date_precision="The official finding aid says Yarrow resigned the assistant district attorney post in November 1942 and joined OSS.", city="New York", state_or_region="New York", country="United States", immediate_pre_oss=True, last_civilian_pre_service=True, research_notes="Explicit immediate civilian government post; kept distinct from earlier private law practice."),
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
        identity = "A nonshared protected identifier and exact official name agreement connect the index and Army records." if row not in {10, 30} else "A nonshared protected identifier connects the records, but the Army surname differs by one letter; identity remains high rather than confirmed."
        values.append(claim(
            f"occupation-{slug(PEOPLE[row][1])}-b1026", row, "occupation",
            f"At Army entry, {PEOPLE[row][1]} was recorded in the broad historical category {label}.",
            f"The official Army record gives code {code} at entry on {date}; NARA's code list maps it to {occupation}.",
            identity, "Strongly date-bounded to Army entry; neither employer nor immediate OSS sequence is supplied.",
            "A_direct_official", "medium", [{"source_key": ARMY}, {"source_key": TECH}, {"source_key": CODES, "locator_override": locator}],
            "Historical category only. It is not converted into a named employer, workplace, or narrower modern occupation.", "publish_qualified",
            f"{slug(PEOPLE[row][1])}-army-occupation-b1026",
        ))
    values.extend([
        claim("identity-louis-xanthopoulos-b1026", 9, "identity", "Indexed Louis J Xanthopoulos is the Army technician listed with the OSS 31st Field Detachment during the Germany Campaign.", "A nonshared protected Army identifier confirms the exact name; the dated OSS headquarters order independently lists him in the 31st Field Detachment.", "Confirmed by exact name, protected identifier and a direct OSS unit document.", "The order documents OSS field service in May 1945; it does not establish his pre-OSS employer.", "A_direct_official", "confirmed", [{"source_key": INDEX}, {"source_key": ARMY}, {"source_key": XANTHOPOULOS}], "Full service numbers remain private; the claim is identity and wartime service only."),
        claim("identity-sumner-yaffe-b1026", 13, "identity", "Indexed Sumner J Yaffe is the Harvard student whose studies were interrupted by wartime Army intelligence service.", "The exact protected-identifier Army record gives student status and February 1943 entry; the obituary supplies the distinctive full name, Harvard and Army intelligence chronology.", "Confirmed by the exact protected identifier and corroborating rare-name chronology.", "Both sources cover the immediate pre-Army period; an exact Army-to-OSS date is unavailable.", "A_direct_official", "high", [{"source_key": INDEX}, {"source_key": ARMY}, {"source_key": WA_POST_YAFFE}], "The obituary is corroborative; the Army record remains the identity anchor."),
        claim("student-sumner-yaffe-b1026", 13, "other_pre_oss_affiliation", "Sumner J. Yaffe was a Harvard University student immediately before wartime Army service.", "The obituary says wartime service interrupted his Harvard studies, while the official Army record codes his entry occupation as student.", "Confirmed exact identity from the protected identifier and corroborating biography.", "Strongly date-bounded before Army service; Army intelligence intervened before OSS.", "C_reputable_contemporary_or_scholarly", "high", [{"source_key": WA_POST_YAFFE}, {"source_key": ARMY, "support_type": "context_only"}, {"source_key": CODES, "support_type": "context_only"}], "Harvard is an educational affiliation here, not an employer.", "published", "sumner-yaffe-harvard-student-b1026"),
        claim("identity-teizo-yahanda-b1026", 16, "identity", "The indexed Teizo Yahanda probably is the Carmel business owner and Gila River Canal block manager documented in contemporary and retrospective sources.", "The rare exact name, California chronology and 1945 Canal role align, but neither source names OSS or a protected identifier.", "Probable, not confirmed: rare exact name and coherent chronology without a direct OSS bridge.", "The sources document prewar and March 1945 roles; exact OSS entry remains unknown.", "C_reputable_contemporary_or_scholarly", "medium", [{"source_key": INDEX}, {"source_key": GILA_YAHANDA}, {"source_key": PARK_BUGLE_YAHANDA}], "Published with qualification; Box 856 remains necessary for confirmation.", "publish_qualified"),
        claim("gila-teizo-yahanda-b1026", 16, "other_pre_oss_affiliation", "Teizo Yahanda served as central block manager for the Canal section of the Gila River Relocation Center in March 1945.", "A contemporary camp newspaper identifies his role and a thirty-day leave to investigate relocation in California.", "Probable identity from the rare exact name and compatible chronology.", "Dated March 1945, but not proven to be the immediate pre-OSS affiliation.", "C_reputable_contemporary_or_scholarly", "medium", [{"source_key": GILA_YAHANDA}], "The incarceration context is explicit; this is not presented as ordinary private employment.", "publish_qualified", "teizo-yahanda-gila-b1026"),
        claim("self-employed-teizo-yahanda-b1026", 16, "last_civilian_pre_service", "Before wartime incarceration, Teizo Yahanda co-owned a dry-cleaning and alterations business in Carmel, California.", "A community-newspaper retrospective says Teizo and Takeko Yahanda started and operated the successful Carmel business before wartime removal.", "Probable identity from the rare exact name and compatible family chronology.", "Documented prewar self-employment; exact end date and OSS sequence remain unverified.", "C_reputable_contemporary_or_scholarly", "medium", [{"source_key": PARK_BUGLE_YAHANDA}], "Published as qualified last documented civilian self-employment, not as a proven immediate OSS predecessor.", "publish_qualified", "teizo-yahanda-self-employed-b1026"),
        claim("identity-sannosuke-yamamoto-b1026", 24, "identity", "The indexed Sannosuke Yamamoto probably is the Philadelphia Japanese-language instructor documented in 1942 and 1944.", "The uncommon exact name, Philadelphia residence since 1905 and wartime language-instruction chronology align, but no source directly names OSS.", "Probable exact-name identity; no protected identifier or direct OSS bridge.", "The teaching role is wartime; its relation to OSS remains uncertain.", "C_reputable_contemporary_or_scholarly", "medium", [{"source_key": INDEX}, {"source_key": DENSHO_YAMAMOTO}, {"source_key": PENN_YAMAMOTO}], "Publication is qualified and excluded from default analytics pending Box 857 review.", "publish_qualified"),
        claim("navy-league-sannosuke-yamamoto-b1026", 24, "other_pre_oss_affiliation", "Sannosuke Yamamoto taught Japanese at the Philadelphia Navy League School during World War II.", "A contemporary 1942 item reports him teaching five Marines; a scholarly description of his 1944 book transcribes his school and instructor title.", "Probable identity from the uncommon exact name and consistent Philadelphia chronology.", "Documented wartime role, but the exact OSS transition cannot be established.", "C_reputable_contemporary_or_scholarly", "medium", [{"source_key": DENSHO_YAMAMOTO}, {"source_key": PENN_YAMAMOTO}], "Not labeled immediate or last civilian employer until the personnel file supplies chronology.", "publish_qualified", "sannosuke-yamamoto-navy-league-b1026"),
        claim("identity-tomomasa-yamazaki-b1026", 28, "identity", "The indexed Tomomasa Yamazaki probably is the former California newspaperman, Navy-school instructor and Army intelligence technician described by Pacific Citizen.", "The rare exact name and specific wartime intelligence chronology align, but the newspaper does not name OSS or a protected identifier.", "Probable rare-name identity without a direct OSS bridge.", "The obituary orders civilian employment before Army intelligence; exact OSS chronology remains unknown.", "C_reputable_contemporary_or_scholarly", "medium", [{"source_key": INDEX}, {"source_key": PACIFIC_CITIZEN_YAMAZAKI}], "Published with qualification; Box 857 should confirm the OSS connection.", "publish_qualified"),
        claim("navy-school-tomomasa-yamazaki-b1026", 28, "last_civilian_pre_service", "Tomomasa Yamazaki's last documented civilian employer before Army intelligence service was the Navy Japanese Language School at Boulder.", "The contemporary obituary says he volunteered for Army intelligence after serving as a language instructor at the Navy school.", "Probable rare-name identity and specific wartime chronology.", "Strongly date-bounded as the immediate predecessor to Army intelligence, not proven immediate pre-OSS.", "C_reputable_contemporary_or_scholarly", "medium", [{"source_key": PACIFIC_CITIZEN_YAMAZAKI}], "Civilian teaching at a military school remains employment; the claim is qualified pending personnel-file confirmation.", "publish_qualified", "tomomasa-yamazaki-navy-school-b1026"),
        claim("new-world-sun-tomomasa-yamazaki-b1026", 28, "other_pre_oss_affiliation", "Tomomasa Yamazaki formerly worked on the editorial staff of the New World-Sun in San Francisco.", "The 1946 obituary explicitly names the newspaper and editorial-staff relationship.", "Probable rare-name identity without a direct OSS bridge.", "Definitely earlier than Army intelligence, but exact dates and order among newspaper jobs are unknown.", "C_reputable_contemporary_or_scholarly", "medium", [{"source_key": PACIFIC_CITIZEN_YAMAZAKI}], "Earlier documented employment; not promoted to immediate or last employer.", "publish_qualified", "tomomasa-yamazaki-new-world-sun-b1026"),
        claim("sangyo-nippo-tomomasa-yamazaki-b1026", 28, "other_pre_oss_affiliation", "Tomomasa Yamazaki formerly worked on the editorial staff of Sangyo Nippo in Los Angeles.", "The 1946 obituary explicitly names the newspaper and editorial-staff relationship.", "Probable rare-name identity without a direct OSS bridge.", "Definitely earlier than Army intelligence, but exact dates and order among newspaper jobs are unknown.", "C_reputable_contemporary_or_scholarly", "medium", [{"source_key": PACIFIC_CITIZEN_YAMAZAKI}], "Earlier documented employment; not promoted to immediate or last employer.", "publish_qualified", "tomomasa-yamazaki-sangyo-nippo-b1026"),
        claim("identity-chitoshi-yanaga-b1026", 29, "identity", "The index entry Ohitoshi Yanaga is a misspelling of Chitoshi Yanaga, the scholar who joined OSS Research and Analysis in 1944.", "Waseda explicitly identifies the indexed spelling as a Chitoshi misspelling, cites the Box 857 personnel file and describes his 1944 OSS assessment and section.", "High confidence from an explicit institutional review of the indexed personnel file and unique chronology.", "The cited personnel-file review dates OSS assessment to September-October 1944.", "B_authoritative_institutional", "high", [{"source_key": INDEX}, {"source_key": WASEDA_YANAGA}], "Ohitoshi remains preserved as the original index spelling; Chitoshi is added as a documented variant."),
        claim("fbis-chitoshi-yanaga-b1026", 29, "immediate_pre_oss_affiliation", "Chitoshi Yanaga's best-supported immediate pre-OSS affiliation was the Foreign Broadcast Intelligence Service of the Federal Communications Commission.", "The dated career sequence places a 1944 FBIS Far Eastern Adviser role immediately before OSS and State Department service in 1944-45.", "High-confidence identity from the explicit indexed-spelling bridge.", "Strongly date-bounded; exact transfer day is not supplied.", "B_authoritative_institutional", "high", [{"source_key": WASEDA_YANAGA}, {"source_key": CIA_FBIS, "support_type": "context_only"}], "Best-supported institutional predecessor; kept separate from OWI and university employment.", "published", "chitoshi-yanaga-fbis-b1026"),
        claim("berkeley-chitoshi-yanaga-b1026", 29, "last_civilian_pre_service", "The University of California, Berkeley was Chitoshi Yanaga's last documented civilian employer before intervening wartime government assignments.", "The institutional chronology dates his Japanese history and government instruction to 1937-42; CIA history independently confirms University of California teaching.", "High-confidence identity from the explicit indexed-spelling bridge.", "Employment ends in 1942 before OWI, FBIS and OSS; not immediate pre-OSS.", "B_authoritative_institutional", "high", [{"source_key": WASEDA_YANAGA}, {"source_key": CIA_FBIS}], "Historical university employment remains distinct from student status and wartime government work.", "published", "chitoshi-yanaga-berkeley-b1026"),
        claim("navy-language-chitoshi-yanaga-b1026", 29, "other_pre_oss_affiliation", "Before OWI, Chitoshi Yanaga instructed intelligence officers at the U.S. Navy Japanese Language School.", "CIA's official history explicitly places this instruction before his OWI translation and research leadership.", "High-confidence identity from the explicit indexed-spelling bridge and unique career sequence.", "Strongly ordered before OWI; exact dates are not supplied.", "A_direct_official", "high", [{"source_key": CIA_FBIS}, {"source_key": WASEDA_YANAGA, "support_type": "context_only"}], "Government teaching assignment, not civilian university employment.", "published", "chitoshi-yanaga-navy-language-b1026"),
        claim("owi-chitoshi-yanaga-b1026", 29, "other_pre_oss_affiliation", "Chitoshi Yanaga directed Japanese translation and research at the Office of War Information from 1942 to 1944.", "Waseda supplies the dated title; CIA's official history independently describes him as heading the same work.", "High-confidence identity from the explicit indexed-spelling bridge and unique career sequence.", "Documented intervening federal assignment before FBIS and OSS.", "B_authoritative_institutional", "high", [{"source_key": WASEDA_YANAGA}, {"source_key": CIA_FBIS}], "Government assignment is not labeled a private employer.", "published", "chitoshi-yanaga-owi-b1026"),
        claim("identity-adam-yarmolinsky-b1026", 40, "identity", "The indexed Adam Yarmolinsky probably is the 1943 Harvard graduate who enlisted in the U.S. Army Air Corps.", "The exact uncommon name and compatible 1943 student-to-military chronology align, but the biography does not mention OSS or a protected identifier.", "Probable exact-name identity without a direct OSS bridge.", "The sources date Harvard and Army service; exact OSS relation remains unknown.", "C_reputable_contemporary_or_scholarly", "medium", [{"source_key": INDEX}, {"source_key": OXFORD_YARMOLINSKY}, {"source_key": CRIMSON_YARMOLINSKY}], "Published with qualification pending Box 857 review.", "publish_qualified"),
        claim("harvard-adam-yarmolinsky-b1026", 40, "other_pre_oss_affiliation", "Adam Yarmolinsky was a Harvard College student and Harvard War Service Committee chairman before Army Air Corps service.", "American National Biography dates his graduation to 1943; a contemporary Crimson item identifies his committee chairmanship.", "Probable identity from the uncommon exact name and compatible chronology.", "Documented before military service; not proven immediate pre-OSS.", "C_reputable_contemporary_or_scholarly", "medium", [{"source_key": OXFORD_YARMOLINSKY}, {"source_key": CRIMSON_YARMOLINSKY}], "Harvard is an educational affiliation, not an employer.", "publish_qualified", "adam-yarmolinsky-harvard-b1026"),
        claim("army-air-corps-adam-yarmolinsky-b1026", 40, "other_pre_oss_affiliation", "Adam Yarmolinsky enlisted in the U.S. Army Air Corps after graduating from Harvard in 1943.", "American National Biography explicitly orders the 1943 graduation before wartime Army Air Corps enlistment.", "Probable identity from the uncommon exact name and compatible chronology.", "Military pathway is documented, but the exact OSS transition is not.", "C_reputable_contemporary_or_scholarly", "medium", [{"source_key": OXFORD_YARMOLINSKY}], "Military assignment remains separate from civilian employment.", "publish_qualified", "adam-yarmolinsky-army-air-corps-b1026"),
        claim("identity-bernard-yarrow-b1026", 44, "identity", "Indexed Bernard Yarrow is the New York assistant district attorney who joined OSS in November 1942.", "The official finding aid supplies the exact name, dated district-attorney chronology and direct OSS service narrative.", "High confidence from the rare exact name and authoritative direct OSS chronology.", "The source explicitly dates the transition to November 1942.", "B_authoritative_institutional", "high", [{"source_key": INDEX}, {"source_key": EISENHOWER_YARROW}], "The finding aid is authoritative; the physical personnel file remains desirable for appointment details."),
        claim("immediate-bernard-yarrow-b1026", 44, "immediate_pre_oss_affiliation", "Bernard Yarrow's immediate pre-OSS affiliation was the New York County District Attorney's Office, where he served in the Rackets Bureau.", "The finding aid says he resigned the assistant district attorney post in November 1942 and joined OSS.", "High-confidence exact identity from the official finding aid and direct OSS narrative.", "Explicit immediate transition with month-level precision.", "B_authoritative_institutional", "high", [{"source_key": EISENHOWER_YARROW}], "Civilian government assignment is not recast as private-sector employment.", "published", "bernard-yarrow-nyc-da-b1026"),
        claim("civilian-bernard-yarrow-b1026", 44, "last_civilian_pre_service", "The New York County District Attorney's Office was Bernard Yarrow's last documented civilian employer before OSS service.", "The official finding aid dates the assistant district attorney post from January 1, 1938 through his November 1942 resignation for OSS.", "High-confidence exact identity from the official finding aid and direct OSS narrative.", "Explicitly the civilian post he left for OSS.", "B_authoritative_institutional", "high", [{"source_key": EISENHOWER_YARROW}], "The earlier private law practice is not mislabeled as the immediate employer.", "published", "bernard-yarrow-nyc-da-b1026"),
    ])
    return values


def unresolved_reason(row: int) -> str:
    reasons = {
        8: "The source prints only an asterisk and X with the note review, so no person-level identity can be resolved online.",
        11: "The adjacent Charles W Yacin Army lead uses the surname Yaciw, but it carries Charles's protected identifier; it is not transferred to Edith B Yaciw.",
        17: "Accessible Arthur Yahiro leads use a conflicting middle name or postwar-only chronology and do not establish Arthur M Yahiro.",
        23: "The common name Kiyoshi Yamamoto produced multiple unbridged candidates and no unique OSS-to-employment link.",
        25: "The common name Thomas S Yamamoto produced multiple unbridged candidates and no unique OSS-to-employment link.",
        31: "Postwar Foreign Service material for an Alexander Yaney Jr. does not establish the indexed person's pre-OSS identity or employer.",
        33: "The short name Isaac Yano produced plausible namesakes without an OSS, protected-identifier or personnel-file bridge.",
        39: "The protected identifier printed for John Yarmey points to an Army record for Louis M Fossarelli, a wholly different name; no identity or occupation is transferred.",
        46: "At least two plausible George Yasukochi candidates have different California and education chronologies, and the index supplies no middle name or protected identifier to choose between them.",
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
    special = set(ARMY_OCCUPATIONS) | {16, 24, 28, 29, 39, 40, 44}
    values: list[dict[str, object]] = []
    for row in sorted(set(PEOPLE) - special):
        reason = unresolved_reason(row)
        status = "needs_identity_review" if row in {8, 17, 46} else "requires_archival_review"
        values.append(base_update(
            row,
            identity_status="ambiguous" if status == "needs_identity_review" else "unresolved",
            identity_evidence=f"The visually verified page 516 source preserves {PEOPLE[row][1]} and Box {PEOPLE[row][2]}. {reason}",
            research_status=status,
            archival_review_priority="critical" if row in {8, 11, 17, 23, 25, 31, 33, 46} else "high",
            next_action=f"Review indexed Box {PEOPLE[row][2]} for corroborating identifiers, immediate pre-OSS affiliation and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}",
        ))
    for row in sorted(ARMY_OCCUPATIONS):
        if row in {10, 30}:
            variant = "Charles W Yaciw" if row == 10 else "Abe Yaches"
            identity_status = "high_confidence"
            identity_evidence = "A nonshared protected identifier links the index to the Army record, but the Army surname differs by one letter; the variant and conflict remain explicit."
            variants = [variant]
        else:
            identity_status = "confirmed"
            identity_evidence = "A nonshared protected identifier and exact official name agreement connect the index and Army records; the identifier remains private."
            variants = None
        updates: dict[str, object] = {
            "identity_status": identity_status,
            "identity_evidence": identity_evidence,
            "personnel_category": "enlisted_army_personnel",
            "commissioned_officer": False,
            "allied_or_foreign_personnel": False,
            "research_status": "occupation_only_found",
            "nara_catalog_id": "1263923",
            "archival_review_priority": "high",
            "next_action": f"Review indexed Box {PEOPLE[row][2]} to identify a named employer or institution and establish Army-to-OSS chronology; the bulk record supplies only a historical occupation category.",
        }
        if variants:
            updates.update({"name_variants": variants, "replace_name_variants": False})
        values.append(base_update(row, **updates))
    values.extend([
        base_update(16, identity_status="probable", identity_evidence="The rare exact name, California business history and contemporary 1945 Canal block-manager role form a coherent chronology, but neither source directly names OSS or a protected identifier.", personnel_category="civilian_professional_or_administrative_grade", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="documented_prewar_employer_found", archival_review_priority="critical", next_action="Review Box 856 to confirm Teizo Yahanda's identity, Carmel business dates, incarceration chronology and exact transition from Gila River to OSS."),
        base_update(24, identity_status="probable", identity_evidence="The uncommon exact name, Philadelphia residence and 1942-44 Japanese-language instruction align, but no reviewed source directly links that biography to OSS.", personnel_category="civilian_professional_or_administrative_grade", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="needs_temporal_review", archival_review_priority="critical", next_action="Review Box 857 to confirm Sannosuke Yamamoto's identity and determine whether Philadelphia Navy League School employment preceded or overlapped OSS service."),
        base_update(28, identity_status="probable", identity_evidence="The rare exact name and contemporary Navy-school, newspaper and Army-intelligence chronology align, but Pacific Citizen does not name OSS or a protected identifier.", personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="documented_prewar_employer_found", archival_review_priority="critical", next_action="Review Box 857 to confirm Tomomasa Yamazaki's OSS connection, newspaper dates and Navy-school-to-Army-intelligence chronology."),
        base_update(29, identity_status="high_confidence", identity_evidence="Waseda explicitly identifies indexed Ohitoshi Yanaga as a misspelling of Chitoshi Yanaga, cites the Box 857 OSS personnel file and supplies his 1944 OSS section and assessment chronology.", name_variants=["Chitoshi Yanaga", "Yanaga Chitoshi", "弥永千利"], replace_name_variants=False, personnel_category="civilian_professional_or_administrative_grade", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="verified_employer_found", archival_review_priority="medium", next_action="Review Box 857 to transcribe the September-October 1944 OSS assessment and confirm the exact FBIS-to-OSS transfer date; Berkeley, OWI and FBIS chronology is already strongly supported."),
        base_update(39, identity_status="conflicting", identity_evidence="The visually verified page 516 source preserves John Yarmey, but the same protected identifier points to an Army record for Louis M Fossarelli. The material name conflict prevents any transfer.", research_status="conflicting_sources", possible_duplicate_group="batch1026-john-yarmey-identifier-conflict", archival_review_priority="critical", next_action="Review Box 857 and the original identifier-bearing index source to resolve the John Yarmey/Louis M Fossarelli conflict. No Army occupation or grade is transferred."),
        base_update(40, identity_status="probable", identity_evidence="The uncommon exact name and 1943 Harvard-to-Army-Air-Corps chronology align, but the biographical sources do not directly name OSS or a protected identifier.", personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="occupation_only_found", archival_review_priority="critical", next_action="Review Box 857 to confirm Adam Yarmolinsky's OSS identity, Army Air Corps assignment and whether any civilian employer intervened after Harvard."),
        base_update(44, identity_status="high_confidence", identity_evidence="The rare exact name and official Eisenhower Library finding aid supply an explicit New York assistant-district-attorney-to-OSS transition in November 1942.", personnel_category="civilian_professional_or_administrative_grade", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="completed", archival_review_priority="medium", next_action="Review Box 857 to confirm OSS appointment paperwork and exact November 1942 dates; the immediate civilian government affiliation is already explicit."),
    ])
    if len(values) != 46:
        raise RuntimeError(f"Expected 46 person updates, generated {len(values)}")
    return values


def research_attempts() -> list[dict[str, object]]:
    substantiated = set(ARMY_OCCUPATIONS) | {16, 24, 28, 29, 39, 40, 44}
    attempts: list[dict[str, object]] = []
    for row, (person_id, name, box) in PEOPLE.items():
        if row in substantiated:
            outcome = "source_reviewed" if row != 39 else "candidate_rejected"
            reviewed = 10 if row in {16, 24, 28, 29, 40, 44} else 7
            rejected = 3 if row != 39 else 5
            note = "At least one identity, occupation, employer, student-status or institutional-pathway outcome is preserved with claim-level citations; remaining employer or temporal questions remain explicit." if row != 39 else unresolved_reason(39)
        else:
            outcome = "candidate_rejected"
            reviewed = 5
            rejected = 4
            note = unresolved_reason(row)
        attempts.append({
            "key": f"page516-row{row}-{slug(name)}-b1026",
            "person_id": person_id,
            "source_adapter": "manual_staged_protocol",
            "query_text": f"{name}; NARA OSS index context; exact-name and meaningful initial, suffix, punctuation, transliteration and OCR variants; OSS, CIA Reading Room, rank, branch, assignment and protected-identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory and archival searches; indexed Box {box}",
            "query_variant_type": "staged_identity_employment_archival_protocol_batch_1026",
            "started_at": "2026-11-04T19:00:00Z",
            "completed_at": "2026-11-05T01:30:00Z",
            "outcome": outcome,
            "sources_reviewed": reviewed,
            "candidate_sources_rejected": rejected,
            "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, postwar-only leads and sources without an OSS, protected-identifier, rank, unit or personnel-file bridge were rejected. Army categories were not converted into named employers. One-letter Army-name conflicts remained qualified, and a wholly different Army name was rejected.",
            "research_notes": f"{note} The official index, exact-name OSS searches, grouped CIA Reading Room checks, and employer, occupation, obituary, institutional, newspaper, directory and archival searches were reviewed as applicable. Page 516, the page 517 boundary, every cited NARA code-list page, Yarrow finding-aid page 2, CIA FBIS page 3, Xanthopoulos order page 5, Gila News-Courier page 7, Park Bugle page 3 and Pacific Citizen page 41 were visually checked. No authenticated NARA Catalog API request was made.",
            "next_action": f"Review indexed Box {box} for corroborating identifiers, immediate pre-OSS affiliation and last civilian employer before wartime service.",
            "attempt_number": 1,
            "research_agent_version": "before-oss-b1026-v1",
        })
    if len(attempts) != 46:
        raise RuntimeError(f"Expected 46 research attempts, generated {len(attempts)}")
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-1026-v1",
        "reviewer": "Before OSS Batch 1026 evidence review",
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
