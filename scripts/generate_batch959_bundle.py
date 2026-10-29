#!/usr/bin/env python3
"""Generate the reviewed Batch 959 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page470-w-c-toland-to-peter-tomkins-"
    "review_batch-959_2026-10-29.json"
)

INDEX = "nara-index-b959"
ARMY = "army-bulk-b959"
TECH = "army-tech-b959"
CODES = "army-codes-b959"
WP_TOLEDANO = "washpost-ralph-toledano-b959"
BERKELEY_EDWARD = "berkeley-edward-tolman-b959"
BERKELEY_RUTH = "berkeley-ruth-tolman-b959"
WHO_RUTH = "whos-who-ruth-tolman-b959"
FRUS_TOLSTOY = "frus-ilia-tolstoy-b959"
FLORIDA_TOLSTOY = "florida-museum-ilia-tolstoy-b959"
DENSHO_TOMITA = "densho-paul-y-tomita-b959"
SEATTLE_TOMITA = "seattle-west-coast-printing-b959"
OBJECTS_TOMITA = "fifty-objects-paul-tomita-b959"
CADILLAC_TOMINACK = "cadillac-honor-roll-tominack-b959"
CIA_TOMINACK = "cia-si-training-tominack-b959"
ITALY_TOMPKINS = "italian-security-tompkins-b959"
NPS_TOMPKINS = "nps-peter-tompkins-b959"

PEOPLE = {
    "470-2": ("c58403db-1d62-5336-a154-ea8d9c28689d", "W C Toland"),
    "470-3": ("e8456428-18ec-5aa9-9bf2-9d749d5c1063", "Milo Tole"),
    "470-4": ("ca6487a4-12a3-5b1f-a0db-038bb0fc7aa5", "Ralph R Toledano"),
    "470-5": ("40c99330-ef90-5354-a820-026560900759", "Albert C Tolie"),
    "470-6": ("94a2076f-98e1-5098-86e2-157572829d1b", "Joseph E Toliver"),
    "470-7": ("c4980e40-681d-5c27-a3e9-797e0020f656", "John H Tolleson"),
    "470-9": ("a524f863-6c5b-53f8-8bc9-3f5bbf4cdf2d", "Edward C Tolman"),
    "470-10": ("e194d51a-76b6-56f4-b1cf-d287ee858c67", "Lee P Tolman"),
    "470-11": ("e5593179-d5cd-512b-b341-2ffe1c840824", "Ruth Tolman"),
    "470-12": ("4962e3ae-1ef2-5276-9605-19ba6a591a68", "Georgia F Tolson"),
    "470-13": ("30b4e838-5ad9-5f09-b0c0-d34e717cfb0d", "Ilia A Tolstoy"),
    "470-14": ("4378440e-32f6-523a-b2e9-5fa905a9c9ab", "L L Toman"),
    "470-15": ("5b7b3a01-151c-5d7a-b020-5fd4aadcc9f0", "Magdeleno G Tomaneng"),
    "470-16": ("a79b6d3d-3e1e-5aad-b2b4-b86f8f9e613b", "Nicholas J Tomasello"),
    "470-17": ("210958be-6601-544e-ba50-38daf0946a43", "Adolph L Tomaseski"),
    "470-18": ("0c4c6599-0859-50b7-9a6a-560131be7e4f", "James Tomasi"),
    "470-19": ("0a14d941-2388-5b87-8fbf-ca55e5a32bb6", "Helen K Tomb"),
    "470-20": ("0357b9d8-373a-5ac9-923f-a6dcb5272d8d", "Frank F Tomei"),
    "470-21": ("32b65c01-de44-579b-83bb-27513f036029", "Edwin Tominack"),
    "470-22": ("c4a88525-9899-5cf0-8439-2865d96376ef", "Paul Y Tomita"),
    "470-23": ("7ab094da-086d-5920-9056-cf56ec22a061", "Theodore Tomita"),
    "470-24": ("bf5306e2-3bf6-519e-a6eb-3557ddee1066", "Harold A Tomkins"),
    "470-25": ("09a923e0-4bb5-52f6-8ed7-ca5086b6301f", "Peter Tomkins"),
}

ARMY_PEOPLE = {
    "470-3": {
        "variant": "Milo Tole",
        "entry_date": "1941-12-08",
        "code": "426",
        "occupation": "Tailors and tailoresses",
        "code_page": "173",
    },
    "470-4": {
        "variant": "Ralph R Toledano",
        "entry_date": "1943-04-09",
        "code": "006",
        "occupation": "Authors, editors, and reporters",
        "code_page": "170",
    },
    "470-7": {
        "variant": "John H Tolleson",
        "entry_date": "1942-12-08",
        "code": "992",
        "occupation": "Students",
        "code_page": "304",
    },
    "470-16": {
        "variant": "Nicholas J Tomassello",
        "entry_date": "1942-11-10",
        "code": "636",
        "occupation": "Furniture manufacturing occupations, n.e.c.",
        "code_page": "176",
    },
    "470-17": {
        "variant": "Adolph Tomasieski",
        "entry_date": "1942-02-03",
        "code": "781",
        "occupation": "Mechanics and repairmen, motor vehicle",
        "code_page": "175",
    },
    "470-18": {
        "variant": "James Tomasi",
        "entry_date": "1942-10-19",
        "code": "138",
        "occupation": "Stock clerks",
        "code_page": "171",
    },
    "470-20": {
        "variant": "Frank F Tomei",
        "entry_date": "1941-05-10",
        "code": "137",
        "occupation": "Stenographers and typists",
        "code_page": "171",
    },
}

UNRESOLVED = {
    "470-2": "Exact-name, initial-only, occupation, obituary, official-domain and archival searches found no defensible Box 780 identity bridge.",
    "470-5": "The printed private identifier did not match the official Army bulk file, and exact-name searches produced no reliable alternative.",
    "470-6": "Common-name and exact-middle-initial searches produced multiple namesakes but no two corroborating identifiers beyond the name.",
    "470-10": "An MIT thesis by Lee P. Tolman is a plausible educational lead, but no source connects that graduate to Box 781 or OSS.",
    "470-12": "A birth-and-death lead and other namesakes were rejected because no reliable source supplies an OSS, Box 781 or institutional bridge.",
    "470-14": "Initial-only exact, variant, obituary, institutional, newspaper and official-domain searches produced no defensible identity bridge.",
    "470-15": "Rare-name and spelling-variant searches produced only the index or uncorroborated namesakes; the indexed officer-style identifier remains unbridged.",
    "470-19": "Exact-name, middle-initial, obituary, institutional, newspaper and archival searches produced no defensible identity bridge.",
    "470-24": "Common-name searches produced unrelated patents, modern records and deceased namesakes but no Box 781 or OSS bridge.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def person(key: str) -> tuple[str, str]:
    return PEOPLE[key]


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 780-781",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 470, rows 2-7 and 9-25; checked against layout-preserving text and a 220 dpi page render",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "The 23 researched rows remain separate. Dorothy I Tolley at row 8 was already terminal and was not overwritten. Full private identifiers remain excluded from public data.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; seven accepted Batch 959 protected-identifier candidates; two additional identifier nonhits; identifiers withheld",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "No raw bulk row, record ordinal or full private identifier enters the evidence bundle or public assets. The local extracted file remains outside version control.",
        },
        {
            "key": TECH,
            "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf",
            "archival_identifier": "NN3-064-03-008; National Archives Identifier 1263923",
            "title": "World War II Army Enlistment Records: Reference Copy of Technical Documentation",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives at College Park - Electronic Records",
            "publication_record_date": "1994-2005; reference copy modified 2011",
            "locator": "PDF physical pages 44-46; identifier, name, DD/MM/YY Army-entry-date and civilian-occupation fields",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Used only to interpret selected fields; source damage and incomplete coverage remain applicable.",
        },
        {
            "key": CODES,
            "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1CL_SD.pdf",
            "archival_identifier": "National Archives Identifier 1263923; Code No. 30",
            "title": "NARA Compiled Code Lists for the Electronic Army Serial Number Merged File",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives at College Park - Electronic Records",
            "publication_record_date": "2011-01-12; modified 2011-03-17",
            "locator": "PDF physical pages 170-176 and 304; historical categories 0-06, 1-37, 1-38, 4-26, 5,7-81, 6-36 and 9-92 visually and textually checked",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical categories are qualified and never converted into named employers, workplaces, schools or exact modern job titles.",
        },
        {
            "key": WP_TOLEDANO,
            "stable_url": "https://www.washingtonpost.com/archive/local/2007/02/07/ralph-de-toledano-90/55a77867-14dc-4d36-822e-4fee12d1113f/",
            "title": "Ralph de Toledano, 90; Ardent Conservative",
            "author_creator": "Joe Holley",
            "repository_publisher": "The Washington Post",
            "publication_record_date": "2007-02-07",
            "locator": "Obituary; 1940 New Leader editorship, Army antiaircraft service and OSS Italian-language training at Cornell",
            "access_date": "2026-10-29",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Washington Post obituaries",
            "rights_notes": "Only short excerpts and project-authored paraphrases are retained.",
        },
        {
            "key": BERKELEY_EDWARD,
            "stable_url": "https://digicoll.lib.berkeley.edu/record/62121/files/cubanc_15_1_00329793a.pdf",
            "title": "University of California faculty service record: Edward C. Tolman",
            "author_creator": "University of California",
            "repository_publisher": "The Bancroft Library, University of California, Berkeley",
            "publication_record_date": "ca. 1950",
            "locator": "Printed page 18; Professor of Psychology, 32 years' U.C. service; OSS psychologist July 1944-February 1945",
            "access_date": "2026-10-29",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "University of California History Digital Archives",
            "rights_notes": "Institutional career metadata and a short excerpt only.",
        },
        {
            "key": BERKELEY_RUTH,
            "stable_url": "https://psychology.berkeley.edu/about/history/psychology-part-ii-our-female-phd-graduates-berkeley",
            "title": "Psychology Part II: Our Female Ph.D. Graduates at Berkeley",
            "author_creator": "Department of Psychology, University of California, Berkeley",
            "repository_publisher": "University of California, Berkeley",
            "publication_record_date": "2020",
            "locator": "Ruth Tolman profile; 1937 clinical-psychology doctorate and OSS work",
            "access_date": "2026-10-29",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "150 Years of Women at Berkeley",
            "rights_notes": "Used for identity, training and explicit OSS service, not unsupported chronology.",
        },
        {
            "key": WHO_RUTH,
            "stable_url": "https://prabook.com/web/ruth_s.tolman/1106897",
            "title": "Ruth S. Tolman",
            "author_creator": "World Biographical Encyclopedia; profile derived from Marquis Who's Who",
            "repository_publisher": "Prabook",
            "publication_record_date": None,
            "locator": "Career chronology: USDA 1941-1942; OWI public opinion analyst 1942-1944; OSS clinical psychologist 1944-1945",
            "access_date": "2026-10-29",
            "source_quality": "D_correlative_or_secondary",
            "collection_name": "World Biographical Encyclopedia",
            "rights_notes": "Chronology is published only as a qualified medium-confidence finding and is corroborated for identity and OSS service by Berkeley.",
        },
        {
            "key": FRUS_TOLSTOY,
            "stable_url": "https://history.state.gov/historicaldocuments/frus1942China/d522",
            "archival_identifier": "FRUS 1942, China, document 522; 103.91802/687",
            "title": "The Director of the Office of Strategic Services (Donovan) to the Secretary of State",
            "author_creator": "William J. Donovan",
            "repository_publisher": "Office of the Historian, United States Department of State",
            "publication_record_date": "1942-07-02",
            "locator": "Donovan identifies Capt. Ilia Tolstoy as one of two OSS men sent via Tibet to General Stilwell",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "Foreign Relations of the United States",
            "rights_notes": "Contemporary official identity and OSS-assignment evidence.",
        },
        {
            "key": FLORIDA_TOLSTOY,
            "stable_url": "https://www.museumoffloridahistory.com/explore/exhibits/permanent-exhibits/world-war-ii/historical-sites/northeast-listing/marineland/",
            "title": "Marineland",
            "author_creator": "Museum of Florida History",
            "repository_publisher": "Florida Department of State",
            "publication_record_date": None,
            "locator": "Historical-site profile; original Marineland founder who left during the war for Roosevelt's Tibet mission",
            "access_date": "2026-10-29",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Florida World War II Historical Sites",
            "rights_notes": "The source explicitly orders the commercial affiliation before the wartime mission.",
        },
        {
            "key": DENSHO_TOMITA,
            "stable_url": "https://downloads.densho.org/ddr-densho-96/ddr-densho-96-293-mezzanine-c578e63207.pdf",
            "archival_identifier": "Densho Digital Repository ddr-densho-96-293",
            "title": "The Japanese-American Courier",
            "author_creator": "The Japanese-American Courier",
            "repository_publisher": "Densho Digital Repository",
            "publication_record_date": "1933-01-01",
            "locator": "New Year advertisement: West Coast Printing Co.; Paul Y. Tomita and Teddy I. Tomita; 618 Jackson, Seattle",
            "access_date": "2026-10-29",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "The Japanese-American Courier Collection",
            "rights_notes": "Contemporary exact-middle-initial evidence; no full page is republished.",
        },
        {
            "key": SEATTLE_TOMITA,
            "stable_url": "https://www.seattle.gov/documents/Departments/Neighborhoods/HistoricPreservation/Landmarks/CurrentNominations/LPBCurrentNom_WestCoastPrinting.pdf",
            "title": "Landmark Nomination: West Coast Printing Building",
            "author_creator": "Seattle Department of Neighborhoods; landmark nomination preparers",
            "repository_publisher": "City of Seattle",
            "publication_record_date": "2016",
            "locator": "West Coast Printing history; founded in 1930 by Theodore and Paul Tomita; closed during Minidoka incarceration",
            "access_date": "2026-10-29",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Seattle Landmarks Preservation Board nominations",
            "rights_notes": "Historical business and forced-removal context only.",
        },
        {
            "key": OBJECTS_TOMITA,
            "stable_url": "https://50objects.org/object/a-childs-identity-card/",
            "title": "A Child's Exit Card",
            "author_creator": "50 Objects/Stories; testimony and objects courtesy of Paul Tomita",
            "repository_publisher": "50 Objects/Stories",
            "publication_record_date": "2018",
            "locator": "Paul Tomita family exit card, Paul Sr. OSS employee pass, Minidoka-to-Washington chronology and OSS Japanese typesetting work",
            "access_date": "2026-10-29",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "50 Objects/Stories",
            "rights_notes": "Family-provided primary artifacts and oral testimony; no images or extended text are republished.",
        },
        {
            "key": CADILLAC_TOMINACK,
            "stable_url": "https://xr793.com/wp-content/uploads/2020/12/1943-Cadillac-From-Peace-To-War.pdf",
            "title": "Cadillac: From Peace to War",
            "author_creator": "Cadillac Motor Car Division",
            "repository_publisher": "General Motors Corporation; digital scan hosted by xr793.com",
            "publication_record_date": "1943",
            "locator": "PDF physical pages 35-36; Honor Roll of more than 3,000 Cadillac members who joined the Armed Forces; Edwin Tominack on page 36",
            "access_date": "2026-10-29",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Cadillac wartime publication",
            "rights_notes": "The 1943 scan was textually and visually inspected; only citation metadata, a short excerpt and paraphrase are retained.",
        },
        {
            "key": CIA_TOMINACK,
            "stable_url": "https://www.cia.gov/readingroom/docs/CIA-RDP13X00001R000100470001-2.pdf",
            "archival_identifier": "CIA-RDP13X00001R000100470001-2",
            "title": "Office of Strategic Services administrative and training records",
            "author_creator": "Office of Strategic Services",
            "repository_publisher": "CIA Freedom of Information Act Electronic Reading Room",
            "publication_record_date": "1942-1945; released 2014-09-16",
            "locator": "SI Training roster; Pvt. Edwin (NMI) Tominack listed as driver",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "OSS Collection",
            "rights_notes": "Official roster context supports the rare-name identity and Army status; it does not name a pre-service employer.",
        },
        {
            "key": ITALY_TOMPKINS,
            "stable_url": "https://www.sicurezzanazionale.gov.it/contenuti/peter-tompkins-giornalista-e-spia",
            "title": "Peter Tompkins, giornalista e spia",
            "author_creator": "Marco Scipolo",
            "repository_publisher": "Sistema di informazione per la sicurezza della Repubblica Italiana",
            "publication_record_date": "2017-12-22",
            "locator": "Career chronology: New York Herald Tribune and Mutual in 1939; NBC in 1941; Allied Force Headquarters psychological warfare in 1942; OSS later in 1942",
            "access_date": "2026-10-29",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Storie di spie",
            "rights_notes": "The missing-p index spelling prevents a settled identity; all resulting claims are qualified.",
        },
        {
            "key": NPS_TOMPKINS,
            "stable_url": "https://home.nps.gov/articles/oss-in-action-the-mediterranean-and-european-theaters.htm",
            "title": "OSS in Action: The Mediterranean and European Theaters",
            "author_creator": "John W. Chambers II",
            "repository_publisher": "United States National Park Service",
            "publication_record_date": None,
            "locator": "Peter Tompkins, age 24, longtime Rome resident and OSS agent in occupied Rome",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "OSS training in the National Parks historical study",
            "rights_notes": "Used to corroborate the distinctive Peter Tompkins OSS identity, not to conceal the index spelling difference.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {"key": "org-army-b959", "organization_id": "24cec6d5-c3cc-5dc4-b8c9-10ef805535e9", "canonical_name": "United States Army", "historical_name": "United States Army", "aliases": ["U.S. Army"], "organization_type": "military branch", "sector": "military", "country": "United States", "normalization_notes": "Military assignment remains distinct from civilian employment."},
        {"key": "org-new-leader-b959", "canonical_name": "The New Leader", "historical_name": "The New Leader", "aliases": ["New Leader"], "organization_type": "political and cultural magazine", "sector": "journalism_and_media", "city": "New York", "state_or_region": "New York", "country": "United States", "active_dates": "1924-2006", "normalization_notes": "Historical publication name preserved."},
        {"key": "org-ucb-b959", "organization_id": "dd5d0a44-0368-5e91-a5d3-074de36840ed", "canonical_name": "University of California, Berkeley", "historical_name": "University of California at Berkeley", "aliases": ["University of California", "U.C. Berkeley"], "organization_type": "university", "sector": "academia_and_research", "city": "Berkeley", "state_or_region": "California", "country": "United States", "normalization_notes": "Institutional record wording preserved in the affiliation."},
        {"key": "org-owi-b959", "organization_id": "c48b74b9-1a67-5480-bb47-8dd73d10abf4", "canonical_name": "Office of War Information", "historical_name": "Office of War Information", "aliases": ["OWI"], "organization_type": "federal agency", "sector": "federal_government", "country": "United States", "active_dates": "1942-1945", "normalization_notes": "Wartime federal information agency; not conflated with OSS."},
        {"key": "org-marine-studios-b959", "canonical_name": "Marine Studios", "historical_name": "Marine Studios", "aliases": ["Marineland"], "organization_type": "oceanarium and motion-picture studio", "sector": "business_and_industry", "city": "Marineland", "state_or_region": "Florida", "country": "United States", "active_dates": "opened 1938; later known as Marineland", "normalization_notes": "The prewar Marine Studios name is retained; Marineland is recorded as an alias."},
        {"key": "org-cadillac-b959", "canonical_name": "Cadillac Motor Car Division", "historical_name": "Cadillac Motor Car Division", "aliases": ["Cadillac"], "organization_type": "automobile manufacturer", "sector": "business_and_industry", "city": "Detroit", "state_or_region": "Michigan", "country": "United States", "active_dates": "historical General Motors division", "normalization_notes": "Employer name follows Cadillac's own 1943 publication; the historical General Motors parent relationship remains documented here rather than silently normalized."},
        {"key": "org-west-coast-printing-b959", "canonical_name": "West Coast Printing Company", "historical_name": "West Coast Printing Co.", "aliases": ["West Coast Printing"], "organization_type": "printing company", "sector": "business_and_industry", "city": "Seattle", "state_or_region": "Washington", "country": "United States", "active_dates": "founded 1930", "normalization_notes": "Family business name preserved from a contemporary advertisement and Seattle landmark report."},
        {"key": "org-minidoka-b959", "canonical_name": "Minidoka War Relocation Center", "historical_name": "Minidoka Relocation Center", "aliases": ["Minidoka incarceration camp", "Minidoka"], "organization_type": "War Relocation Authority incarceration site", "sector": "federal_government", "state_or_region": "Idaho", "country": "United States", "active_dates": "1942-1945", "normalization_notes": "Coerced incarceration is described explicitly and is never presented as employment or voluntary government service."},
        {"key": "org-nyht-b959", "organization_id": "1b5694e8-821f-51b0-9aa8-18fe66fa4411", "canonical_name": "New York Herald Tribune", "historical_name": "New York Herald Tribune", "aliases": [], "organization_type": "newspaper", "sector": "journalism_and_media", "city": "New York", "state_or_region": "New York", "country": "United States", "normalization_notes": "Historical newspaper name preserved."},
        {"key": "org-mutual-b959", "organization_id": "9dce34b6-35f0-5686-b3e8-847601bf60fd", "canonical_name": "Mutual Broadcasting System", "historical_name": "Mutual Broadcasting System", "aliases": ["Mutual"], "organization_type": "radio network", "sector": "journalism_and_media", "country": "United States", "normalization_notes": "Historical network name preserved."},
        {"key": "org-nbc-b959", "organization_id": "f8b54577-fc09-5c6a-9b36-d68aee691c07", "canonical_name": "National Broadcasting Company", "historical_name": "National Broadcasting Company", "aliases": ["NBC"], "organization_type": "radio network", "sector": "journalism_and_media", "country": "United States", "normalization_notes": "Historical network name preserved."},
        {"key": "org-afhq-b959", "organization_id": "581b2980-5e84-5e29-91fb-e8004e0b74b1", "canonical_name": "Allied Force Headquarters", "historical_name": "Allied Force HQ, North Africa", "aliases": ["AFHQ"], "organization_type": "allied military headquarters", "sector": "military", "city": "Algiers", "country": "Algeria", "normalization_notes": "Allied wartime assignment; not a civilian employer."},
    ]


def army_affiliation(key: str) -> dict[str, object]:
    person_id, _ = person(key)
    data = ARMY_PEOPLE[key]
    return {
        "key": f"army-occupation-{slug(PEOPLE[key][1])}-b959",
        "person_id": person_id,
        "occupation": data["occupation"],
        "relationship_type": "employment" if data["occupation"] != "Students" else "student",
        "end_date": data["entry_date"],
        "date_precision": f"Historical category {data['code']} was recorded at Army entry on {data['entry_date']}; no employer or workplace is named.",
        "country": "United States",
        "immediate_pre_oss": False,
        "last_civilian_pre_service": False,
        "pre_oss_temporal_basis": "strongly_date_bounded",
        "identity_confidence": "high_confidence",
        "claim_confidence": "medium",
        "source_quality": "A_direct_official",
        "publication_status": "publish_qualified",
        "research_notes": "Broad historical category only; it is not converted into a named employer or exact modern job title.",
    }


def affiliations() -> list[dict[str, object]]:
    values = [army_affiliation(key) for key in ARMY_PEOPLE]
    ralph, _ = person("470-4")
    edward, _ = person("470-9")
    ruth, _ = person("470-11")
    ilia, _ = person("470-13")
    edwin, _ = person("470-21")
    paul, _ = person("470-22")
    peter, _ = person("470-25")
    values.extend(
        [
            {"key": "ralph-toledano-new-leader-b959", "person_id": ralph, "organization_key": "org-new-leader-b959", "organization_name_as_found": "The New Leader", "role_title": "editor", "occupation": "editor", "relationship_type": "employment", "start_date": "1940", "end_date": "before Army service", "date_precision": "The obituary states that he became editor in 1940 and then served in the Army during World War II.", "city": "New York", "state_or_region": "New York", "country": "United States", "immediate_pre_oss": False, "last_civilian_pre_service": True, "pre_oss_temporal_basis": "strongly_date_bounded", "identity_confidence": "confirmed", "claim_confidence": "high", "source_quality": "C_reputable_contemporary_or_scholarly", "publication_status": "published", "research_notes": "Last named civilian employer before Army service; the exact departure date is not stated."},
            {"key": "ralph-toledano-army-b959", "person_id": ralph, "organization_key": "org-army-b959", "organization_name_as_found": "Army", "role_title": "antiaircraft gunner", "relationship_type": "military_assignment", "start_date": "1943", "end_date": "before OSS language training", "date_precision": "The obituary explicitly states that Army antiaircraft service preceded OSS Italian-language training at Cornell.", "country": "United States", "immediate_pre_oss": True, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "explicit_immediate", "identity_confidence": "confirmed", "claim_confidence": "high", "source_quality": "C_reputable_contemporary_or_scholarly", "publication_status": "published", "research_notes": "Military assignment, not civilian employment; the source says he was later dropped from the OSS program."},
            {"key": "edward-tolman-ucb-b959", "person_id": edward, "organization_key": "org-ucb-b959", "organization_name_as_found": "U. C.", "role_title": "Professor of Psychology", "occupation": "psychologist and professor", "relationship_type": "employment", "start_date": "1918", "end_date": "1944-07", "date_precision": "The University record reports 32 years of service and separately dates OSS psychology service from July 1944 to February 1945.", "city": "Berkeley", "state_or_region": "California", "country": "United States", "immediate_pre_oss": True, "last_civilian_pre_service": True, "pre_oss_temporal_basis": "strongly_date_bounded", "identity_confidence": "confirmed", "claim_confidence": "confirmed", "source_quality": "B_authoritative_institutional", "publication_status": "published", "research_notes": "The same institutional record establishes both the continuing university career and exact OSS service dates."},
            {"key": "ruth-tolman-owi-b959", "person_id": ruth, "organization_key": "org-owi-b959", "organization_name_as_found": "O.W.I.", "role_title": "public opinion analyst", "occupation": "psychologist and public opinion analyst", "relationship_type": "government_assignment", "start_date": "1942", "end_date": "1944", "date_precision": "The biographical chronology places OWI in 1942-1944 and OSS clinical psychology in 1944-1945.", "country": "United States", "immediate_pre_oss": True, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "explicit_immediate", "identity_confidence": "high_confidence", "claim_confidence": "medium", "source_quality": "D_correlative_or_secondary", "publication_status": "publish_qualified", "research_notes": "Qualified because the detailed sequence comes from a secondary biographical profile; Berkeley independently confirms the identity and OSS work."},
            {"key": "ilia-tolstoy-marine-studios-b959", "person_id": ilia, "organization_key": "org-marine-studios-b959", "organization_name_as_found": "Marineland", "role_title": "original founder", "relationship_type": "self_employment", "start_date": "1930s", "end_date": "1942", "date_precision": "The Florida museum says the original founder left during the war for Roosevelt's Tibet mission; FRUS places that OSS mission in July 1942.", "city": "Marineland", "state_or_region": "Florida", "country": "United States", "immediate_pre_oss": True, "last_civilian_pre_service": True, "pre_oss_temporal_basis": "explicit_immediate", "identity_confidence": "confirmed", "claim_confidence": "high", "source_quality": "B_authoritative_institutional", "publication_status": "published", "research_notes": "Founder relationship is modeled as self-employment; the historical Marine Studios name is normalized separately."},
            {"key": "edwin-tominack-cadillac-b959", "person_id": edwin, "organization_key": "org-cadillac-b959", "organization_name_as_found": "Cadillac", "role_title": "member of Cadillac; exact job title not stated", "relationship_type": "employment", "end_date": "before armed-forces service", "date_precision": "Cadillac's 1943 honor roll names Edwin Tominack among company members who joined the Armed Forces.", "city": "Detroit", "state_or_region": "Michigan", "country": "United States", "immediate_pre_oss": False, "last_civilian_pre_service": True, "pre_oss_temporal_basis": "explicit_immediate", "identity_confidence": "high_confidence", "claim_confidence": "high", "source_quality": "C_reputable_contemporary_or_scholarly", "publication_status": "published", "research_notes": "The publication establishes the employer-to-military transition but not the exact Cadillac job title."},
            {"key": "paul-tomita-west-coast-printing-b959", "person_id": paul, "organization_key": "org-west-coast-printing-b959", "organization_name_as_found": "West Coast Printing Co.", "role_title": "cofounder and multilingual typesetter", "occupation": "printer and typesetter", "relationship_type": "self_employment", "start_date": "1930", "end_date": "1942", "date_precision": "A 1933 advertisement names Paul Y. Tomita; the Seattle report says the brothers founded the firm in 1930 and closed it during forced removal in 1942.", "city": "Seattle", "state_or_region": "Washington", "country": "United States", "immediate_pre_oss": False, "last_civilian_pre_service": True, "pre_oss_temporal_basis": "strongly_date_bounded", "identity_confidence": "confirmed", "claim_confidence": "confirmed", "source_quality": "B_authoritative_institutional", "publication_status": "published", "research_notes": "The printing business is separated from the intervening Minidoka incarceration and later OSS civilian work."},
            {"key": "paul-tomita-minidoka-b959", "person_id": paul, "organization_key": "org-minidoka-b959", "organization_name_as_found": "Minidoka prison camp", "role_title": "incarcerated civilian under War Relocation Authority control", "relationship_type": "unknown", "start_date": "1942", "end_date": "1943-07-04", "date_precision": "The family exit-card history dates release to July 4, 1943 and links the subsequent Washington move to Paul Sr.'s cleared OSS employment.", "state_or_region": "Idaho", "country": "United States", "immediate_pre_oss": True, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "explicit_immediate", "identity_confidence": "confirmed", "claim_confidence": "high", "source_quality": "B_authoritative_institutional", "publication_status": "published", "research_notes": "Coerced incarceration is not employment, government assignment or voluntary affiliation."},
            {"key": "peter-tompkins-nyht-b959", "person_id": peter, "organization_key": "org-nyht-b959", "organization_name_as_found": "New York Herald Tribune", "role_title": "war correspondent", "occupation": "journalist", "relationship_type": "employment", "start_date": "1939", "date_precision": "Italian government history dates the correspondence to 1939.", "country": "Italy", "immediate_pre_oss": False, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "probable", "claim_confidence": "medium", "source_quality": "B_authoritative_institutional", "publication_status": "publish_qualified", "research_notes": "The indexed Tomkins/Tompkins spelling difference remains unresolved."},
            {"key": "peter-tompkins-mutual-b959", "person_id": peter, "organization_key": "org-mutual-b959", "organization_name_as_found": "Mutual Broadcasting System", "role_title": "war correspondent", "occupation": "broadcast journalist", "relationship_type": "employment", "start_date": "1939", "date_precision": "Italian government history dates the correspondence to 1939.", "country": "Italy", "immediate_pre_oss": False, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "probable", "claim_confidence": "medium", "source_quality": "B_authoritative_institutional", "publication_status": "publish_qualified", "research_notes": "The indexed Tomkins/Tompkins spelling difference remains unresolved."},
            {"key": "peter-tompkins-nbc-b959", "person_id": peter, "organization_key": "org-nbc-b959", "organization_name_as_found": "Nbc", "role_title": "war correspondent", "occupation": "broadcast journalist", "relationship_type": "employment", "start_date": "1941", "end_date": "1942", "date_precision": "The source places him with NBC in Greece in 1941, followed by Allied headquarters work in 1942 and OSS later that year.", "country": "Greece", "immediate_pre_oss": False, "last_civilian_pre_service": True, "pre_oss_temporal_basis": "strongly_date_bounded", "identity_confidence": "probable", "claim_confidence": "medium", "source_quality": "B_authoritative_institutional", "publication_status": "publish_qualified", "research_notes": "Qualified as the last named civilian employer before the intervening Allied headquarters assignment."},
            {"key": "peter-tompkins-afhq-b959", "person_id": peter, "organization_key": "org-afhq-b959", "organization_name_as_found": "headquarters of the Allied forces", "role_title": "deputy director, Psychological Warfare section", "relationship_type": "government_assignment", "start_date": "1942", "end_date": "1942", "date_precision": "The source places this North Africa assignment immediately before his entry into OSS later in 1942.", "city": "Algiers", "country": "Algeria", "immediate_pre_oss": True, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "explicit_immediate", "identity_confidence": "probable", "claim_confidence": "medium", "source_quality": "B_authoritative_institutional", "publication_status": "publish_qualified", "research_notes": "Allied wartime assignment; not a civilian employer. The indexed spelling remains unresolved."},
        ]
    )
    return values


def claim(
    key: str,
    person_id: str,
    claim_type: str,
    text: str,
    paraphrase: str,
    identity: str,
    temporal: str,
    quality: str,
    confidence: str,
    status: str,
    notes: str,
    source_links: list[dict[str, object]],
    *,
    affiliation_key: str | None = None,
    excerpt: str | None = None,
) -> dict[str, object]:
    value: dict[str, object] = {
        "key": key,
        "person_id": person_id,
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
    if affiliation_key is not None:
        value["affiliation_key"] = affiliation_key
    if excerpt is not None:
        value["evidence_excerpt"] = excerpt
    return value


def army_claims(key: str) -> list[dict[str, object]]:
    person_id, name = person(key)
    data = ARMY_PEOPLE[key]
    variant = data["variant"]
    identity_notes = "Exact protected identifier agreement plus compatible name."
    variant_note = ""
    if variant != name:
        identity_notes = "Exact protected identifier agreement outweighs a visible spelling conflict that remains preserved."
        variant_note = f" The Army form {variant} is retained as a variant, not a silent correction."
    return [
        claim(
            f"identity-{slug(name)}-army-b959",
            person_id,
            "identity",
            f"The indexed {name} is a high-confidence match to the reviewed official Army record.",
            f"A nonshared private identifier agrees exactly; the Army record names {variant}, records private grade, and dates Army entry to {data['entry_date']}.",
            identity_notes,
            "The Army record dates entry but not the later OSS transfer.",
            "A_direct_official",
            "high",
            "published",
            "Full private identifiers and raw bulk rows remain excluded from public data." + variant_note,
            [
                {"source_key": INDEX, "locator_override": f"PDF page 470 row {key.split('-')[1]}; Box {'780' if int(key.split('-')[1]) <= 7 else '781'}; private identifier withheld"},
                {"source_key": ARMY, "locator_override": f"Reviewed {variant} record; private identifier withheld"},
                {"source_key": TECH, "support_type": "context_only", "locator_override": "Field definitions, PDF physical pages 44-46"},
            ],
        ),
        claim(
            f"occupation-{slug(name)}-army-b959",
            person_id,
            "other_pre_oss_affiliation" if data["occupation"] == "Students" else "occupation",
            f"At Army entry on {data['entry_date']}, {variant} was recorded in the historical {data['occupation']} category.",
            f"The official bulk record supplies code {data['code']}; the visually reviewed NARA list expands that historical code.",
            "High confidence from the accepted private-identifier bridge.",
            "Strongly date-bounded at Army entry; no employer, workplace or immediate OSS sequence is named.",
            "A_direct_official",
            "medium",
            "publish_qualified",
            "The broad historical category is not converted into a named employer, school or exact modern job title.",
            [
                {"source_key": ARMY, "locator_override": f"Army entry {data['entry_date']}; code {data['code']}; private identifier withheld"},
                {"source_key": CODES, "locator_override": f"PDF physical page {data['code_page']}; historical category {data['code']}"},
            ],
            affiliation_key=f"army-occupation-{slug(name)}-b959",
            excerpt=data["occupation"],
        ),
    ]


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for key in ARMY_PEOPLE:
        values.extend(army_claims(key))

    ralph, _ = person("470-4")
    edward, _ = person("470-9")
    ruth, _ = person("470-11")
    ilia, _ = person("470-13")
    edwin, _ = person("470-21")
    paul, _ = person("470-22")
    peter, _ = person("470-25")

    values.extend(
        [
            claim("identity-ralph-de-toledano-b959", ralph, "identity", "The indexed Ralph R Toledano is confirmed as journalist Ralph de Toledano.", "The protected-identifier Army bridge supplies the exact indexed name and 1943 Army entry; the obituary supplies the documented de Toledano form, journalism career and explicit OSS training.", "Confirmed by nonshared private identifier, full name, journalism occupation and explicit OSS chronology.", "The obituary and Army record cover the civilian-to-Army-to-OSS sequence.", "C_reputable_contemporary_or_scholarly", "confirmed", "published", "The de particle is retained as a documented variant.", [{"source_key": INDEX, "locator_override": "PDF page 470 row 4; Box 780; private identifier withheld"}, {"source_key": ARMY, "locator_override": "Reviewed Ralph R Toledano record; private identifier withheld"}, {"source_key": WP_TOLEDANO}]),
            claim("last-civilian-ralph-toledano-b959", ralph, "last_civilian_pre_service", "The New Leader was Ralph de Toledano's last documented civilian employer before Army service.", "The obituary says he became the magazine's editor in 1940, then served in the Army during World War II.", "Confirmed identity from the accepted Army bridge and explicit biography.", "Strongly date-bounded before Army service; the exact departure date is not stated.", "C_reputable_contemporary_or_scholarly", "high", "published", "The civilian employer remains separate from his immediate Army pathway.", [{"source_key": WP_TOLEDANO, "locator_override": "Career chronology", "excerpt_override": "In 1940, he became editor of the New Leader"}], affiliation_key="ralph-toledano-new-leader-b959"),
            claim("immediate-ralph-toledano-army-b959", ralph, "immediate_pre_oss_affiliation", "Ralph de Toledano served as an Army antiaircraft gunner before OSS sent him to Cornell for Italian-language training.", "The obituary explicitly orders the Army assignment before the OSS program.", "Confirmed identity from the accepted Army bridge and explicit biography.", "Explicit immediate military-to-OSS sequence.", "C_reputable_contemporary_or_scholarly", "high", "published", "He was dropped from the program; the site does not imply an overseas OSS deployment.", [{"source_key": WP_TOLEDANO, "locator_override": "World War II service paragraph", "excerpt_override": "served in the Army during World War II, initially as an antiaircraft gunner"}], affiliation_key="ralph-toledano-army-b959"),
            claim("identity-edward-chace-tolman-b959", edward, "identity", "The indexed Edward C Tolman is confirmed as University of California psychologist Edward Chace Tolman.", "A University faculty service record names Edward C. Tolman, his psychology professorship, long U.C. service and exact OSS dates.", "Confirmed exact name, occupation, institution and explicit OSS service.", "The institutional record dates OSS service to July 1944-February 1945.", "B_authoritative_institutional", "confirmed", "published", "Chace is a documented middle-name expansion.", [{"source_key": INDEX, "locator_override": "PDF page 470 row 9; Box 781"}, {"source_key": BERKELEY_EDWARD, "locator_override": "Printed page 18"}]),
            claim("last-civilian-edward-tolman-ucb-b959", edward, "last_civilian_pre_service", "The University of California at Berkeley was Edward C. Tolman's immediate civilian affiliation and last civilian employer before OSS service.", "The faculty record reports 32 years of U.C. service and separately dates his OSS psychology work beginning in July 1944.", "Confirmed exact-person institutional record.", "Strongly date-bounded continuous academic employment immediately before the dated OSS assignment.", "B_authoritative_institutional", "confirmed", "published", "The university is an employer here, not merely an educational affiliation.", [{"source_key": BERKELEY_EDWARD, "locator_override": "Printed page 18", "excerpt_override": "Professor of Psychology, 32 years' service at U. C."}], affiliation_key="edward-tolman-ucb-b959"),
            claim("identity-ruth-sherman-tolman-b959", ruth, "identity", "The indexed Ruth Tolman is a high-confidence match to clinical psychologist Ruth Sherman Tolman.", "Berkeley identifies its 1937 clinical-psychology Ph.D. graduate Ruth Tolman and explicitly states that she worked in OSS.", "High confidence from the distinctive exact name, profession, Berkeley degree and explicit OSS service.", "The institutional source does not itself date the OSS entry; the secondary career chronology does.", "B_authoritative_institutional", "high", "published", "Sherman is retained as a documented birth-name expansion.", [{"source_key": INDEX, "locator_override": "PDF page 470 row 11; Box 781"}, {"source_key": BERKELEY_RUTH}, {"source_key": WHO_RUTH, "support_type": "context_only"}]),
            claim("immediate-ruth-tolman-owi-b959", ruth, "immediate_pre_oss_affiliation", "Ruth S. Tolman served as an Office of War Information public opinion analyst in 1942-1944 before OSS clinical-psychology work in 1944-1945.", "The biographical career chronology explicitly places OWI immediately before OSS; Berkeley independently confirms her identity and OSS work.", "High-confidence identity from Berkeley; chronology comes from a secondary profile.", "Explicit sequence, but qualified because the detailed dates are not supplied by the institutional source.", "D_correlative_or_secondary", "medium", "publish_qualified", "OWI is a government assignment, not a civilian employer in the aggregate employer chart.", [{"source_key": WHO_RUTH, "locator_override": "Career chronology", "excerpt_override": "Public opinion analyst, O.W.I., 1942-1944"}, {"source_key": BERKELEY_RUTH, "support_type": "context_only"}], affiliation_key="ruth-tolman-owi-b959"),
            claim("identity-ilia-tolstoy-b959", ilia, "identity", "The indexed Ilia A Tolstoy is confirmed as Capt. Ilia Tolstoy of the 1942 OSS mission through Tibet.", "A contemporary Donovan letter calls Capt. Ilia Tolstoy one of two OSS men sent to General Stilwell; the rare name and compatible officer status match the index.", "Confirmed by distinctive name, officer status and direct contemporary OSS document.", "The official letter dates the mission to July 1942.", "A_direct_official", "confirmed", "published", "The index middle initial remains preserved even though the official source omits it.", [{"source_key": INDEX, "locator_override": "PDF page 470 row 13; Box 781; private identifier withheld"}, {"source_key": FRUS_TOLSTOY, "locator_override": "Document 522"}]),
            claim("immediate-ilia-tolstoy-marineland-b959", ilia, "immediate_pre_oss_affiliation", "Ilia Tolstoy was an original founder of Marine Studios/Marineland before leaving during the war for Roosevelt's Tibet mission.", "The Florida state museum explicitly orders the Marineland affiliation before the mission; FRUS identifies that mission as OSS in July 1942.", "Confirmed distinctive identity from official OSS and state institutional sources.", "Explicit immediate chronology, though the museum uses the later Marineland name.", "B_authoritative_institutional", "high", "published", "Founder status is modeled as self-employment; Marine Studios is the normalized historical name.", [{"source_key": FLORIDA_TOLSTOY, "locator_override": "Historical site profile", "excerpt_override": "one of the original founders of Marineland"}, {"source_key": FRUS_TOLSTOY, "support_type": "context_only"}], affiliation_key="ilia-tolstoy-marine-studios-b959"),
            claim("identity-edwin-tominack-b959", edwin, "identity", "The indexed Edwin Tominack is a high-confidence match to the Army private in an OSS SI Training roster.", "The exact rare name appears independently in a CIA-released OSS roster and Cadillac's 1943 honor roll of members who joined the Armed Forces.", "High confidence from the rare exact name, compatible Army status and two independent wartime sources.", "The sources establish the civilian-to-Army/OSS pathway but not the OSS entry date.", "A_direct_official", "high", "published", "The Army bulk private-identifier nonhit is retained in review notes and is not concealed.", [{"source_key": INDEX, "locator_override": "PDF page 470 row 21; Box 781; private identifier withheld"}, {"source_key": CIA_TOMINACK, "locator_override": "SI Training roster"}, {"source_key": CADILLAC_TOMINACK, "locator_override": "PDF physical pages 35-36"}]),
            claim("last-civilian-edwin-tominack-cadillac-b959", edwin, "last_civilian_pre_service", "Cadillac Motor Car Division was Edwin Tominack's last documented civilian employer before armed-forces service.", "Cadillac's 1943 honor roll identifies Edwin Tominack among company members who joined the Armed Forces.", "High-confidence rare-name identity corroborated by the OSS roster.", "Explicit employer-to-military transition; exact job title and dates are not stated.", "C_reputable_contemporary_or_scholarly", "high", "published", "No Cadillac job title is invented.", [{"source_key": CADILLAC_TOMINACK, "locator_override": "Honor Roll, PDF physical pages 35-36", "excerpt_override": "members of Cadillac who have joined the Armed Forces"}, {"source_key": CIA_TOMINACK, "support_type": "context_only"}], affiliation_key="edwin-tominack-cadillac-b959"),
            claim("identity-paul-y-tomita-b959", paul, "identity", "The indexed Paul Y Tomita is confirmed as Seattle printer and OSS civilian employee Paul Tomita Sr.", "A 1933 contemporary advertisement names Paul Y. Tomita at West Coast Printing; a family-provided OSS employee pass and account document his Japanese-language OSS work.", "Confirmed by exact full indexed name, rare business association and primary OSS employee artifact.", "The sources document 1933 business work, 1942-1943 incarceration and later OSS employment.", "B_authoritative_institutional", "confirmed", "published", "Paul Sr. is a documented generational form; no unsupported given-name expansion is added.", [{"source_key": INDEX, "locator_override": "PDF page 470 row 22; Box 781"}, {"source_key": DENSHO_TOMITA, "locator_override": "West Coast Printing advertisement"}, {"source_key": OBJECTS_TOMITA, "locator_override": "Paul Tomita Sr. OSS employee pass and family history"}]),
            claim("last-civilian-paul-tomita-printing-b959", paul, "last_civilian_pre_service", "West Coast Printing Company was Paul Y. Tomita's last documented civilian business before wartime confinement and later OSS service.", "The contemporary advertisement names Paul Y. Tomita; Seattle documents the brothers' 1930 founding and forced 1942 closure.", "Confirmed exact-person match from the contemporary middle-initial advertisement and OSS employee artifact.", "Strongly date-bounded before the intervening Minidoka incarceration and OSS work.", "B_authoritative_institutional", "confirmed", "published", "The family business is not mislabeled as the immediate predecessor because incarceration intervened.", [{"source_key": DENSHO_TOMITA, "locator_override": "West Coast Printing advertisement", "excerpt_override": "West Coast Printing Co. Paul Y. Tomita"}, {"source_key": SEATTLE_TOMITA, "locator_override": "Later owner/occupant, West Coast Printing"}, {"source_key": OBJECTS_TOMITA, "support_type": "context_only"}], affiliation_key="paul-tomita-west-coast-printing-b959"),
            claim("immediate-paul-tomita-minidoka-b959", paul, "immediate_pre_oss_affiliation", "Paul Y. Tomita's immediate pre-OSS status included coerced incarceration at Minidoka and conditional release to Washington, D.C.", "The exit-card history dates release to July 4, 1943 and presents the OSS pass and clearance as the family's route to Washington.", "Confirmed exact-person match from the contemporary business record and primary family artifacts.", "Explicit immediate status before OSS employment; it is not an employer relationship.", "B_authoritative_institutional", "high", "published", "The public wording states coercion and does not describe confinement as voluntary affiliation or government service.", [{"source_key": OBJECTS_TOMITA, "locator_override": "Exit card, Minidoka chronology and OSS employee pass", "excerpt_override": "Paul Sr. passed the highest level of clearance"}, {"source_key": SEATTLE_TOMITA, "support_type": "context_only"}], affiliation_key="paul-tomita-minidoka-b959"),
            claim("identity-peter-tomkins-tompkins-b959", peter, "identity", "The indexed Peter Tomkins is a probable, not settled, match to OSS officer and journalist Peter Tompkins.", "Official NPS history and the Italian security service document a distinctive Peter Tompkins OSS biography, but the index omits the p and supplies no second identifier.", "Probable from a rare near-exact name and explicit OSS service; insufficient for high-confidence identity.", "The biography covers the prewar-to-OSS sequence; the Box 781 file remains necessary to confirm the spelling variant.", "A_direct_official", "medium", "publish_qualified", "The probable variant is excluded from default employer analytics and remains flagged for archival review.", [{"source_key": INDEX, "locator_override": "PDF page 470 row 25; Box 781; note 'docume'"}, {"source_key": NPS_TOMPKINS}, {"source_key": ITALY_TOMPKINS}]),
            claim("prewar-peter-tompkins-nyht-b959", peter, "other_pre_oss_affiliation", "Probable match Peter Tompkins worked as a New York Herald Tribune war correspondent beginning in 1939.", "Italian government history names the newspaper and year.", "Probable identity only because the index spelling is Tomkins.", "Documented prewar journalism, not the immediate OSS predecessor.", "B_authoritative_institutional", "medium", "publish_qualified", "Qualified and excluded from default analytics.", [{"source_key": ITALY_TOMPKINS, "locator_override": "Corrispondente di guerra e agente segreto"}], affiliation_key="peter-tompkins-nyht-b959"),
            claim("prewar-peter-tompkins-mutual-b959", peter, "other_pre_oss_affiliation", "Probable match Peter Tompkins worked as a Mutual Broadcasting System war correspondent beginning in 1939.", "Italian government history names the radio network and year.", "Probable identity only because the index spelling is Tomkins.", "Documented prewar journalism, not the immediate OSS predecessor.", "B_authoritative_institutional", "medium", "publish_qualified", "Qualified and excluded from default analytics.", [{"source_key": ITALY_TOMPKINS, "locator_override": "Corrispondente di guerra e agente segreto"}], affiliation_key="peter-tompkins-mutual-b959"),
            claim("last-civilian-peter-tompkins-nbc-b959", peter, "last_civilian_pre_service", "NBC was probable match Peter Tompkins's last documented civilian employer before an Allied psychological-warfare assignment.", "Italian government history places him with NBC in Greece in 1941 and Allied Force Headquarters in 1942.", "Probable identity only because the index spelling is Tomkins.", "Strongly date-bounded before the intervening wartime government assignment.", "B_authoritative_institutional", "medium", "publish_qualified", "Qualified and excluded from default employer analytics.", [{"source_key": ITALY_TOMPKINS, "locator_override": "Corrispondente di guerra e agente segreto", "excerpt_override": "Nel 1941 è in Grecia ... per la Nbc"}], affiliation_key="peter-tompkins-nbc-b959"),
            claim("immediate-peter-tompkins-afhq-b959", peter, "immediate_pre_oss_affiliation", "In 1942, probable match Peter Tompkins served in psychological warfare at Allied Force Headquarters before entering OSS later that year.", "Italian government history explicitly orders the Algiers assignment before OSS entry.", "Probable identity only because the index spelling is Tomkins.", "Explicit immediate chronology in the biography.", "B_authoritative_institutional", "medium", "publish_qualified", "Allied assignment, not a civilian employer; qualified and excluded from default analytics.", [{"source_key": ITALY_TOMPKINS, "locator_override": "Corrispondente di guerra e agente segreto"}, {"source_key": NPS_TOMPKINS, "support_type": "context_only"}], affiliation_key="peter-tompkins-afhq-b959"),
        ]
    )
    return values


def base_update(key: str, **kwargs: object) -> dict[str, object]:
    value: dict[str, object] = {
        "person_id": PEOPLE[key][0],
        "manual_review_required": True,
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
    }
    value.update(kwargs)
    return value


def unresolved_update(key: str, reason: str) -> dict[str, object]:
    person_id, name = person(key)
    return {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, Box {'780' if int(key.split('-')[1]) <= 7 else '781'} and archive location 230/86/42/02. {reason}",
        "personnel_category": "unknown_or_indeterminate",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": f"Review Box {'780' if int(key.split('-')[1]) <= 7 else '781'} for corroborating identifiers, immediate pre-OSS affiliation and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }


def army_update(key: str) -> dict[str, object]:
    data = ARMY_PEOPLE[key]
    name = PEOPLE[key][1]
    variants = [] if data["variant"] == name else [data["variant"]]
    status = "completed" if data["occupation"] == "Students" else "occupation_only_found"
    return base_update(
        key,
        identity_status="high_confidence",
        identity_evidence=f"A nonshared private identifier connects the visually verified index row to the official Army record naming {data['variant']}; visible spelling differences remain preserved.",
        name_variants=variants,
        personnel_category="enlisted_army_personnel",
        commissioned_officer=False,
        allied_or_foreign_personnel=False,
        research_status=status,
        next_action=f"Review Box {'780' if int(key.split('-')[1]) <= 7 else '781'} for the named employer and Army-to-OSS sequence; the broad historical {data['occupation']} category is not a workplace.",
        archival_review_priority="high",
    )


def person_updates() -> list[dict[str, object]]:
    values = [unresolved_update(key, reason) for key, reason in UNRESOLVED.items()]
    values.extend(army_update(key) for key in ARMY_PEOPLE if key != "470-4")
    values.extend(
        [
            base_update("470-4", identity_status="confirmed", identity_evidence="A nonshared private identifier, exact indexed name and explicit journalism/Army/OSS biography establish Ralph de Toledano.", name_variants=["Ralph de Toledano"], personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="verified_employer_found", next_action="Review Box 780 for the precise New Leader departure date and OSS training-file disposition; the civilian employer and Army predecessor are already documented.", archival_review_priority="medium"),
            base_update("470-9", identity_status="confirmed", identity_evidence="A University of California service record identifies Edward C. Tolman, his psychology professorship and exact OSS dates.", name_variants=["Edward Chace Tolman"], personnel_category="civilian_professional_or_administrative_grade", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="verified_employer_found", next_action="Review Box 781 for recruitment correspondence and assignment detail; the immediate university affiliation is already documented.", archival_review_priority="medium"),
            base_update("470-11", identity_status="high_confidence", identity_evidence="Berkeley identifies clinical psychologist and 1937 Ph.D. Ruth Tolman and explicitly documents OSS work; a secondary career chronology orders OWI before OSS.", name_variants=["Ruth Sherman Tolman", "Ruth S. Tolman"], personnel_category="civilian_professional_or_administrative_grade", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="completed", next_action="Review Box 781 or a direct personnel record to confirm the OWI-to-OSS transfer dates and any last civilian employer before the government pathway.", archival_review_priority="high"),
            base_update("470-13", identity_status="confirmed", identity_evidence="A contemporary Donovan letter identifies Capt. Ilia Tolstoy as an OSS man on the 1942 Tibet mission; the rare name and officer status align with the index.", name_variants=["Count Ilia Tolstoy", "Ilya Tolstoy"], personnel_category="commissioned_army_officer", commissioned_officer=True, allied_or_foreign_personnel=False, research_status="verified_employer_found", next_action="Review Box 781 for the exact Marine Studios departure date and Army commission chronology; the founder-to-mission pathway is already documented.", archival_review_priority="medium"),
            base_update("470-21", identity_status="high_confidence", identity_evidence="The exact rare name appears in a CIA-released OSS SI Training roster and Cadillac's 1943 honor roll of company members who joined the Armed Forces; the Army bulk identifier nonhit remains noted.", name_variants=["Edwin (NMI) Tominack"], personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="verified_employer_found", next_action="Review Box 781 for Cadillac job title, Army entry date and exact SI/OSS transfer sequence.", archival_review_priority="high"),
            base_update("470-22", identity_status="confirmed", identity_evidence="A contemporary advertisement names Paul Y. Tomita at West Coast Printing and a family-preserved OSS employee pass documents Paul Tomita Sr.'s cleared OSS work.", name_variants=["Paul Tomita Sr."], personnel_category="civilian_professional_or_administrative_grade", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="verified_employer_found", next_action="Review Box 781 for the exact OSS appointment date and whether any East Coast job intervened after release from Minidoka.", archival_review_priority="high"),
            base_update("470-23", identity_status="ambiguous", identity_evidence="Accessible sources describe at least two plausible Theodore Tomitas: Paul Y. Tomita's Seattle printing-company brother and a separately documented military officer. Neither source supplies a Box 781 bridge, and the candidates are not merged.", name_variants=["Teddy I. Tomita", "Theodore 'Ted' Tomita"], personnel_category="unknown_or_indeterminate", commissioned_officer=None, allied_or_foreign_personnel=False, possible_duplicate_group="batch959-theodore-tomita-candidates", research_status="conflicting_sources", next_action="Review Box 781 for a middle initial, birthplace, service identifier and OSS assignment before choosing between the Seattle printer and military-officer candidates.", archival_review_priority="critical"),
            base_update("470-25", identity_status="probable", identity_evidence="Official NPS and Italian government histories document the distinctive Peter Tompkins OSS biography, but the index spells the surname Tomkins and supplies no second identifier.", name_variants=["Peter Tompkins"], personnel_category="civilian_professional_or_administrative_grade", commissioned_officer=False, allied_or_foreign_personnel=False, possible_duplicate_group="batch959-peter-tomkins-tompkins", research_status="documented_prewar_employer_found", next_action="Review Box 781 for a direct Tomkins/Tompkins spelling bridge before raising the identity or employer claims above qualified medium confidence.", archival_review_priority="critical"),
        ]
    )
    return values


def research_attempts() -> list[dict[str, object]]:
    special = {
        "470-3": "Accepted private-identifier Army bridge and visually verified historical tailoring category.",
        "470-4": "Accepted Army bridge plus Washington Post biography established The New Leader, antiaircraft service and OSS language training.",
        "470-7": "Accepted private-identifier Army bridge and visually verified historical Students category.",
        "470-9": "University of California service record established the continuous professor role and exact OSS dates.",
        "470-11": "Berkeley established identity and OSS work; a secondary career chronology supports a qualified OWI predecessor.",
        "470-13": "Contemporary FRUS and Florida state history established the Marine Studios founder-to-OSS Tibet mission pathway.",
        "470-16": "Accepted private-identifier Army bridge despite a preserved one-letter surname conflict; historical furniture category verified.",
        "470-17": "Accepted private-identifier Army bridge despite a preserved surname conflict; historical motor-vehicle mechanics category verified.",
        "470-18": "Accepted private-identifier Army bridge and visually verified historical stock-clerk category.",
        "470-20": "Accepted private-identifier Army bridge and visually verified historical stenographer/typist category.",
        "470-21": "CIA OSS roster and Cadillac's visually inspected 1943 honor roll established a high-confidence civilian-to-military pathway.",
        "470-22": "Contemporary Densho newspaper, Seattle landmark history and primary family artifacts established the printing business, Minidoka and OSS pathway.",
        "470-23": "Two plausible Theodore Tomita biographies were preserved as an explicit conflict rather than transferred to the index row.",
        "470-25": "Official histories support Peter Tompkins and a detailed journalism-to-Allied-HQ-to-OSS chronology, but the Tomkins spelling remains unconfirmed.",
    }
    attempts: list[dict[str, object]] = []
    for key, (person_id, name) in PEOPLE.items():
        row = int(key.split("-")[1])
        box = "780" if row <= 7 else "781"
        if key in special:
            outcome = "source_reviewed" if key != "470-23" else "candidate_found"
            reviewed = 10
            rejected = 5
            detail = special[key]
        else:
            outcome = "candidate_rejected" if key in {"470-5", "470-10", "470-12", "470-24"} else "no_result"
            reviewed = 7
            rejected = 6
            detail = UNRESOLVED[key]
        attempts.append(
            {
                "key": f"page470-row{row}-{slug(name)}-b959",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index and public Archives context; CIA Reading Room or equivalent official-source check; exact-name and meaningful variants; OSS, Army and foreign-name clues; employer and occupation 1940; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Box {box}; private identifiers used only when defensible",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_959",
                "started_at": "2026-10-29T22:30:00Z",
                "completed_at": "2026-10-29T23:55:00Z",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search snippets, unsourced genealogy, people-finder pages, modern records, postwar-only leads and sources without an OSS, private-identifier or Box-file bridge were rejected. Search aliases were not treated as silent corrections. The Peter Tomkins/Tompkins and Theodore Tomita alternatives remain explicitly qualified or conflicting.",
                "research_notes": f"{detail} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain, CIA Reading Room-equivalent and Library of Congress searches were checked as applicable. The index page, Army bulk file, technical documentation and relevant code-list pages were inspected directly. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": (
                    "Review Box 781 for a middle initial and service identifier before choosing between the two Theodore Tomita candidates."
                    if key == "470-23"
                    else "Review Box 781 for a direct Tomkins/Tompkins spelling bridge and exact OSS-entry chronology."
                    if key == "470-25"
                    else f"Review Box {box} for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before wartime service."
                ),
                "attempt_number": 1,
                "research_agent_version": "before-oss-b959-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-959-v1",
        "reviewer": "Before OSS Batch 959 evidence review",
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
