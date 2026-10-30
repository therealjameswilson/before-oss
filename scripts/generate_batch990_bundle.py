#!/usr/bin/env python3
"""Generate the reviewed Batch 990 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page485-von-moltke-to-vournas-"
    "review_batch-990_2026-10-30.json"
)

INDEX = "nara-index-b990"
ARMY = "army-bulk-b990"
TECH = "army-tech-b990"
CODES = "army-codes-b990"
PAB_MOLTKE = "pab-wilhelm-viggo-von-moltke-b990"
DVIDS_RIPPER = "dvids-rudolf-von-ripper-b990"
ARMY_RIPPER = "army-rudolf-von-ripper-b990"
VONNEUMAN_CV = "nicholas-vonneuman-cv-b990"
HARVARD_1942 = "harvard-crimson-von-stade-1942-b990"
HARVARD_1995 = "harvard-crimson-von-stade-1995-b990"
CIA_CART = "cia-mapmakers-voskuil-b990"
UIUC_1940 = "uiuc-voskuil-1940-b990"
PRINCETON_VOTICHENKO = "princeton-votichenko-b990"
RESISTANCE_VOUGNON = "resistance-museum-vougnon-b990"
USWM_VOULGARAKIS = "us-war-memorials-voulgarakis-b990"
OSSOG_VOULGARAKIS = "oss-operational-groups-voulgarakis-b990"
WAPO_VOURNAS = "washington-post-vournas-b990"
AHEPA_VOURNAS = "ahepa-vournas-b990"
COURT_VOURNAS = "court-vournas-1940-b990"

ORG_HOWE_STONOROV_KAHN = "howe-stonorov-kahn-b990"
ORG_US_ARMY = "us-army-b990"
ORG_NATIONAL_CITY = "national-city-bank-new-york-b990"
ORG_NAVAL_INTEL = "office-naval-intelligence-b990"
ORG_HARVARD = "harvard-college-b990"
ORG_COI_CART = "coi-cartography-section-b990"
ORG_UIUC = "university-illinois-b990"
ORG_US_NAVY = "us-navy-b990"
ORG_PRINCETON = "princeton-university-b990"
ORG_MAQUIS_C134 = "maquis-c134-b990"

SCHUSCHNIGG_GROUP = "p416-p485-walter-schuschnigg-b990"
VOOT_GROUP = "p416-p485-bert-vogt-voot-b990"
WALTER_SCHUSCHNIGG_ID = "d644ca01-1045-5458-ac8d-3373d7a2ca4b"
BERT_VOGT_ID = "4560d7c3-f72b-5ffd-be8c-e00d2ab655b8"


PEOPLE = {
    24: ("b8227a87-17a5-52a4-80d7-d31ff6dee558", "Wilhelm-Viggo E.F. Von Moltke"),
    25: ("aa89d58a-8da6-593e-8326-0cc9fd347daa", "Robert A Von Neuman"),
    26: ("afe08b69-e1ee-5700-b66f-373c322ebc88", "Rudolph C Von Ripper"),
    27: ("a4669b2c-e62f-5f67-8788-467466c49f16", "Walter Von Schuschn"),
    28: ("ff7f569a-385a-5a25-bcb8-4c3ad1482600", "Franz Von Seidler"),
    29: ("8a43d6b7-7310-5ded-b614-163865da9fe4", "Joseph Vona"),
    30: ("fe5b6b14-d45d-5d5f-97fe-d43b8dfbaa97", "Roy P Vonel"),
    31: ("54c6913a-3cf1-57fa-a0d1-c9fff105ba31", "John G Vonetes"),
    32: ("e0bfc44d-4a4f-5019-bdee-c27bf69ed7a7", "Nicholas A Vonneuman"),
    33: ("aa840791-02df-5e25-82f1-0bd391955bb5", "Francis S Vonstade"),
    34: ("03ce197a-fcd3-5ea8-b9a4-cc3c83b02da0", "James A Voorhees"),
    35: ("d9f08064-0aa3-5dc0-aa1b-cc99525c59fe", "John S Voorhees"),
    36: ("335da26b-23b5-532f-b451-bbc3030ab3a4", "Bert D Voot"),
    37: ("6726c8ad-2148-572f-b157-acaa6620b369", "Henri G.W. Vorbroker"),
    38: ("09daafe4-c14a-5f0b-827a-5ce19ecfb3b4", "Donald W Vose"),
    39: ("7ed7291c-2f3a-5fc5-9ae7-8c34a10cd660", "Robert J Voskuil"),
    40: ("00cfd64f-fb8a-5b33-b745-65d7e28fd264", "Raymond G Vosper"),
    41: ("8d107515-262c-5fb5-8a0a-4e9f3f782c12", "T.Alexander Votichenko"),
    42: ("f7484bdc-8aa4-52bf-a82f-8d9971ef4998", "Mario J Votinelli"),
    43: ("09554b6e-359e-5d5c-9d23-c4083c684e43", "Claude Vougnon"),
    44: ("a64bc4dd-29e4-5aff-a951-d48b1d668310", "Steve Voulgarakis"),
    45: ("6a2fc444-1dc1-5918-a72c-3ce9f111875b", "Adam Voulgaris"),
    46: ("2ca75e2b-edd4-5471-a531-c74859a0b266", "George C Vournas"),
}


UNRESOLVED = {
    25: "A scholarly OSS history names a Robert von Neumann as a research assistant, while art-market and biographical leads point to different Robert von Neumanns. None supplies the indexed middle initial or a protected-identifier bridge.",
    28: "Exact-name, spelling-variant, OSS, employer, occupation, obituary, institutional and archival searches produced no reliable identity bridge.",
    29: "A Joseph Vona obituary names a Westinghouse engineer and Army veteran, but the common name and absence of a matching middle initial or protected identifier make the candidate unsafe to assign.",
    31: "Exact-name, middle-initial, OSS, employer, occupation, obituary, directory, institutional and archival searches produced no reliable identity bridge.",
    35: "Exact-name, middle-initial, OSS, employer, occupation, obituary, directory, institutional and archival searches produced no reliable identity bridge.",
    37: "Exact-name, punctuation-variant, naval-grade, OSS, employer, occupation, obituary, institutional and archival searches produced no reliable identity bridge.",
    45: "Exact-name, OSS, employer, occupation, obituary, institutional and archival searches produced no reliable identity bridge.",
}


ARMY_OCCUPATIONS = {
    30: ("1942-12-03", "057", "Athletes, sports instructors, and sports officials", "athlete, sports instructor, or sports official"),
    38: ("1942-07-01", "002", "Actors and actresses", "actor or actress"),
    42: ("1942-08-27", "636", "Semiskilled occupations in manufacture of furniture, n.e.c.", "semiskilled worker in furniture manufacture"),
    44: ("1942-03-26", "170", "Sales clerks", "sales clerk"),
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 807-808",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 485, rows 24-46; checked against layout-preserving text and an original-detail page render",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. Protected identifiers remain private. Walter Von Schuschn and Walter Schuschnigg remain separate possible duplicates; Bert D Voot remains separate from Bert D Vogt.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; eight protected-identifier comparisons; identifiers and record ordinals withheld",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "Seven identity bridges were accepted; Bert D Voot remains a shared-identifier name conflict. No raw bulk row, record ordinal or full identifier enters public assets.",
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
            "locator": "Civilian occupation code list; codes 001, 002, 057, 170 and 636 reviewed; code 999 remains undefined",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical categories identify broad occupations, not named employers, workplaces or exact jobs. Raymond Vosper's post-OSS record is used only for identity.",
        },
        {
            "key": PAB_MOLTKE,
            "stable_url": "https://www.philadelphiabuildings.org/pab/app/ar_display.cfm/22760",
            "archival_identifier": "Philadelphia Architects and Buildings architect record 22760",
            "title": "Moltke, Wilhelm Viggo von (1911-1992)",
            "author_creator": "Emily T. Cooperman, Rima M. Girnius, and Sandra L. Tatman",
            "repository_publisher": "Athenaeum of Philadelphia and University of Pennsylvania Architectural Archives",
            "publication_record_date": None,
            "locator": "Biographical record; professional experience and military service",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Philadelphia Architects and Buildings",
            "rights_notes": "The rare name and chronology are compatible, but the profile omits the indexed E.F. initials and does not mention OSS; identity and employment remain qualified.",
        },
        {
            "key": DVIDS_RIPPER,
            "stable_url": "https://www.dvidshub.net/news/printable/543490",
            "archival_identifier": "DVIDS story 543490",
            "title": "Rudolf von Ripper: Warrior, Artist, and Witness to War",
            "author_creator": "Maj. William McGehee",
            "repository_publisher": "Defense Visual Information Distribution Service; 1st Armored Division",
            "publication_record_date": "2025-07-22",
            "locator": "Biography sections on 1942 Army entry, hospital laboratory duty and the War Art Unit",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "1st Armored Division and Fort Bliss",
        },
        {
            "key": ARMY_RIPPER,
            "stable_url": "https://innovation.army.mil/Test-Page/videoid/972164/dvpTag/IMCOM/",
            "archival_identifier": "U.S. Army video feature 972164",
            "title": "Rudolf von Ripper",
            "author_creator": "United States Army",
            "repository_publisher": "United States Army",
            "publication_record_date": None,
            "locator": "Feature description; Army art service followed by recruitment into the wartime intelligence organization",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "United States Army historical features",
            "rights_notes": "The page uses an imprecise expansion of OSS; the project normalizes only the organization name and preserves the underlying Army-to-OSS sequence.",
        },
        {
            "key": VONNEUMAN_CV,
            "stable_url": "https://gwern.net/doc/math/1987-vonneumann.pdf",
            "archival_identifier": "Appendix G, Curriculum Vitae of Nicholas A. Vonneuman",
            "title": "John von Neumann As Seen By His Brother",
            "author_creator": "Nicholas A. Vonneuman",
            "repository_publisher": "Nicholas A. Vonneuman",
            "publication_record_date": "1987",
            "locator": "PDF physical page 75, printed page 70; curriculum vitae employment chronology visually inspected",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Author's autobiographical manuscript",
            "rights_notes": "The project stores only a citation and concise paraphrase. The exact-name autobiographical chronology is corroborated by the official Army identity bridge.",
        },
        {
            "key": HARVARD_1942,
            "stable_url": "https://www.thecrimson.com/article/1942/5/1/dean-von-stade-leaves-college-for/",
            "archival_identifier": "The Harvard Crimson, May 1, 1942",
            "title": "Dean Von Stade Leaves College For Service",
            "author_creator": "The Harvard Crimson",
            "repository_publisher": "The Harvard Crimson",
            "publication_record_date": "1942-05-01",
            "locator": "Contemporary report on Francis Skiddy von Stade Jr.'s resignation as assistant dean",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "The Harvard Crimson archive",
        },
        {
            "key": HARVARD_1995,
            "stable_url": "https://www.thecrimson.com/article/1995/10/3/former-mather-master-von-stade-dead/",
            "archival_identifier": "The Harvard Crimson, October 3, 1995",
            "title": "Former Mather Master Von Stade Dead at 91",
            "author_creator": "The Harvard Crimson",
            "repository_publisher": "The Harvard Crimson",
            "publication_record_date": "1995-10-03",
            "locator": "Institutional obituary; assistant-dean appointment and departure for Naval Intelligence",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "The Harvard Crimson archive",
        },
        {
            "key": CIA_CART,
            "stable_url": "https://www.cia.gov/stories/story/the-mapmakers-craft-a-history-of-cartography-at-cia/",
            "archival_identifier": "CIA historical feature, The Mapmaker's Craft",
            "title": "The Mapmaker's Craft: A History of Cartography at CIA",
            "author_creator": "Central Intelligence Agency",
            "repository_publisher": "Central Intelligence Agency",
            "publication_record_date": None,
            "locator": "Section on the COI Cartography Section's formation after Pearl Harbor and transition to OSS",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "CIA historical stories",
        },
        {
            "key": UIUC_1940,
            "stable_url": "https://www.trustees.uillinois.edu/trustees/minutes/1940/1940-05-28-uibot.pdf",
            "archival_identifier": "University of Illinois Board of Trustees minutes, May 28, 1940",
            "title": "Meeting of the Board of Trustees, University of Illinois, May 28, 1940",
            "author_creator": "University of Illinois Board of Trustees",
            "repository_publisher": "University of Illinois",
            "publication_record_date": "1940-05-28",
            "locator": "PDF physical page 27, printed page 961; Robert J. Voskuil appointment visually inspected",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "University of Illinois Board of Trustees minutes",
        },
        {
            "key": PRINCETON_VOTICHENKO,
            "stable_url": "https://paw.princeton.edu/memorial/taras-votichenko-40",
            "archival_identifier": "Princeton Alumni Weekly memorial: Taras Votichenko '40",
            "title": "Taras Votichenko '40",
            "author_creator": "Princeton Alumni Weekly",
            "repository_publisher": "Princeton University",
            "publication_record_date": None,
            "locator": "Memorial; Princeton graduation, Navy service, military-government work and OSS context",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Princeton Alumni Weekly memorials",
            "rights_notes": "The memorial's phrase 'after the war' is retained as a chronology caveat because OSS ceased operations in October 1945.",
        },
        {
            "key": RESISTANCE_VOUGNON,
            "stable_url": "https://www.museedelaresistanceenligne.org/media.php?expo=&media=9516",
            "archival_identifier": "Musée de la Résistance en ligne media 9516",
            "title": "Maquis C-134 commandé par Claude Vougnon",
            "author_creator": "Musée de la Résistance en ligne",
            "repository_publisher": "Fondation de la Résistance",
            "publication_record_date": None,
            "locator": "Collection description identifying Claude Vougnon as commander of Maquis C-134",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Musée de la Résistance en ligne",
        },
        {
            "key": USWM_VOULGARAKIS,
            "stable_url": "https://uswarmemorials.org/html/people_details.php?PeopleID=24841",
            "archival_identifier": "US War Memorials profile 24841",
            "title": "Steve Voulgarakis",
            "author_creator": "US War Memorials Overseas, Inc.",
            "repository_publisher": "US War Memorials Overseas, Inc.",
            "publication_record_date": None,
            "locator": "Service profile; identifier, Army entry, rank, unit and Greek-American OSS volunteer context",
            "access_date": "2026-10-30",
            "source_quality": "D_correlative_or_secondary",
            "collection_name": "US War Memorials personnel profiles",
            "rights_notes": "The public profile's full service number is not reproduced in project claims or public exports.",
        },
        {
            "key": OSSOG_VOULGARAKIS,
            "stable_url": "https://ossog.info/balkans/greek_04.html",
            "archival_identifier": "OSS Operational Groups, Greek group roster page 4",
            "title": "Greek Operational Group personnel",
            "author_creator": "OSS Operational Groups",
            "repository_publisher": "OSS Operational Groups veterans-history project",
            "publication_record_date": None,
            "locator": "Roster listing Sgt. Steve Voulgarakis",
            "access_date": "2026-10-30",
            "source_quality": "D_correlative_or_secondary",
            "collection_name": "OSS Operational Groups",
        },
        {
            "key": WAPO_VOURNAS,
            "stable_url": "https://www.washingtonpost.com/archive/local/1995/10/31/ww-bennett-foreign-service-officer-dies/46b247f6-c3a3-46c1-8421-48d8c538917e/",
            "archival_identifier": "The Washington Post, October 31, 1995",
            "title": "W.W. Bennett, Foreign Service Officer, Dies",
            "author_creator": "The Washington Post",
            "repository_publisher": "The Washington Post",
            "publication_record_date": "1995-10-31",
            "locator": "Obituary item on legal practice and Army assignment to OSS",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "The Washington Post archive",
        },
        {
            "key": AHEPA_VOURNAS,
            "stable_url": "https://ahepahistory.org/History-of-the-Order-of-AHEPA-1922-1972-George-Leber/part-III-chapter-seven-the-years-1939-1945.html",
            "archival_identifier": "AHEPA history, Part III, Chapter Seven",
            "title": "The Years 1939-1945",
            "author_creator": "George J. Leber",
            "repository_publisher": "Order of AHEPA historical archive",
            "publication_record_date": None,
            "locator": "Wartime account of George C. Vournas as AHEPA president and U.S. Army officer",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "History of the Order of AHEPA, 1922-1972",
        },
        {
            "key": COURT_VOURNAS,
            "stable_url": "https://www.leagle.com/decision/1940826110f2d7161616",
            "archival_identifier": "110 F.2d 716 (1940)",
            "title": "Skiriotes v. Florida",
            "author_creator": "United States Court of Appeals, Fifth Circuit",
            "repository_publisher": "Leagle legal archive",
            "publication_record_date": "1940",
            "locator": "Counsel listing naming George C. Vournas as attorney",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Federal court decisions",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {"key": ORG_HOWE_STONOROV_KAHN, "canonical_name": "Howe, Stonorov & Kahn", "historical_name": "Howe, Stonorov & Kahn", "organization_type": "architecture firm", "sector": "business_and_industry", "city": "Philadelphia", "state_or_region": "Pennsylvania", "country": "United States", "normalization_notes": "Historical firm name preserved; no successor organization is substituted."},
        {"key": ORG_US_ARMY, "canonical_name": "United States Army", "historical_name": "U.S. Army", "aliases": ["US Army"], "organization_type": "armed service", "sector": "military", "country": "United States", "normalization_notes": "Specific units and programs remain in role fields when supported."},
        {"key": ORG_NATIONAL_CITY, "canonical_name": "National City Bank of New York", "historical_name": "National City Bank of New York", "organization_type": "bank", "sector": "finance_and_banking", "city": "New York", "state_or_region": "New York", "country": "United States", "active_dates": "Historical name used through 1955", "normalization_notes": "The 1937-1942 historical employer name is preserved; no modern successor is substituted."},
        {"key": ORG_NAVAL_INTEL, "canonical_name": "Office of Naval Intelligence", "historical_name": "Naval Intelligence", "aliases": ["ONI"], "organization_type": "military intelligence organization", "sector": "military", "country": "United States", "normalization_notes": "The obituary's historical wording is preserved in the affiliation."},
        {"key": ORG_HARVARD, "canonical_name": "Harvard College", "historical_name": "Harvard College", "organization_type": "college", "sector": "academia_and_research", "city": "Cambridge", "state_or_region": "Massachusetts", "country": "United States", "normalization_notes": "Harvard College is retained as the named employer rather than silently broadened to the university."},
        {"key": ORG_COI_CART, "canonical_name": "Coordinator of Information Cartography Section", "historical_name": "COI Cartography Section", "aliases": ["Cartography Section"], "organization_type": "federal intelligence cartography unit", "sector": "federal_government", "city": "Washington", "state_or_region": "District of Columbia", "country": "United States", "active_dates": "1941-1942; transferred into OSS in June 1942", "normalization_notes": "The predecessor section is kept distinct from the later OSS Cartography Section."},
        {"key": ORG_UIUC, "canonical_name": "University of Illinois", "historical_name": "University of Illinois", "organization_type": "public university", "sector": "academia_and_research", "city": "Urbana", "state_or_region": "Illinois", "country": "United States"},
        {"key": ORG_US_NAVY, "canonical_name": "United States Navy", "historical_name": "U.S. Navy", "aliases": ["US Navy"], "organization_type": "armed service", "sector": "military", "country": "United States"},
        {"key": ORG_PRINCETON, "canonical_name": "Princeton University", "historical_name": "Princeton University", "organization_type": "university", "sector": "student", "city": "Princeton", "state_or_region": "New Jersey", "country": "United States", "normalization_notes": "Student status is not counted as employment."},
        {"key": ORG_MAQUIS_C134, "canonical_name": "Maquis C-134", "historical_name": "Maquis C-134", "aliases": ["C-134", "Forces françaises de l'intérieur"], "organization_type": "French Resistance formation", "sector": "military", "country": "France", "normalization_notes": "The maquis formation is retained as a historical Allied military/resistance affiliation."},
    ]


def affiliation(key: str, row: int, relationship_type: str, temporal: str, identity: str, confidence: str, quality: str, status: str = "published", **kwargs: object) -> dict[str, object]:
    value: dict[str, object] = {
        "key": key,
        "person_id": PEOPLE[row][0],
        "relationship_type": relationship_type,
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
    for row, (date, _code, _official, public) in ARMY_OCCUPATIONS.items():
        values.append(affiliation(
            f"{slug(PEOPLE[row][1])}-army-category-b990",
            row, "employment", "strongly_date_bounded", "high_confidence", "medium", "A_direct_official", "publish_qualified",
            occupation=public, end_date=date,
            date_precision="Historical civilian-occupation category recorded at Army entry; employer, workplace, duration and exact job are not supplied",
            country="United States", immediate_pre_oss=False, last_civilian_pre_service=False,
            research_notes="Official historical category only; excluded from verified-employer analytics and not narrowed beyond the code-list wording.",
        ))
    values.extend([
        affiliation("moltke-howe-stonorov-kahn-b990", 24, "employment", "strongly_date_bounded", "probable", "medium", "B_authoritative_institutional", "publish_qualified", organization_key=ORG_HOWE_STONOROV_KAHN, organization_name_as_found="Howe, Stonorov & Kahn", role_title="architect", occupation="architect", end_date="1942", date_precision="Institutional biography lists the firm in 1942 and Army service beginning in 1943", city="Philadelphia", state_or_region="Pennsylvania", country="United States", immediate_pre_oss=False, last_civilian_pre_service=True, research_notes="Qualified last civilian employer before Army service; the profile omits the indexed initials and does not directly link him to OSS."),
        affiliation("ripper-us-army-b990", 26, "military_assignment", "explicit_immediate", "high_confidence", "high", "A_direct_official", organization_key=ORG_US_ARMY, organization_name_as_found="U.S. Army", role_title="War Art Unit artist and intelligence officer", occupation="artist and Army officer", start_date="1942", date_precision="Official Army sources document Army service followed by recruitment into OSS; exact transfer date is not supplied", country="United States", immediate_pre_oss=True, last_civilian_pre_service=False, research_notes="Army assignment immediately before OSS; no civilian employer is inferred."),
        affiliation("vonneuman-us-army-b990", 32, "military_assignment", "explicit_immediate", "confirmed", "confirmed", "A_direct_official", organization_key=ORG_US_ARMY, organization_name_as_found="U.S. Army", role_title="Infantry Replacement Training Center and Army Specialized Training Program", start_date="1942", end_date="1943", date_precision="Author's curriculum vitae gives 1942-1943 Army training followed by 1943-1945 detached service with OSS", country="United States", immediate_pre_oss=True, last_civilian_pre_service=False, research_notes="Exact-name autobiographical chronology corroborated by the official Army identity bridge."),
        affiliation("vonneuman-national-city-b990", 32, "employment", "strongly_date_bounded", "confirmed", "high", "C_reputable_contemporary_or_scholarly", organization_key=ORG_NATIONAL_CITY, organization_name_as_found="National City Bank of New York", role_title="auditor, Comptrollers Department", occupation="auditor", start_date="1937", end_date="1942", date_precision="Author's curriculum vitae gives 1937-1942, followed by U.S. Army service", city="New York", state_or_region="New York", country="United States", immediate_pre_oss=False, last_civilian_pre_service=True, research_notes="Last documented civilian employer before Army service; the historical bank name is preserved."),
        affiliation("von-stade-naval-intelligence-b990", 33, "military_assignment", "probable_immediate", "high_confidence", "high", "B_authoritative_institutional", "publish_qualified", organization_key=ORG_NAVAL_INTEL, organization_name_as_found="Naval Intelligence", role_title="wartime intelligence service", start_date="1942", date_precision="Institutional obituary says he left Harvard to join Naval Intelligence; exact later transfer into OSS is not supplied", country="United States", immediate_pre_oss=True, last_civilian_pre_service=False, research_notes="Qualified predecessor affiliation; Box 808 is needed to establish the Naval Intelligence-to-OSS sequence."),
        affiliation("von-stade-harvard-b990", 33, "employment", "explicit_immediate", "high_confidence", "high", "B_authoritative_institutional", organization_key=ORG_HARVARD, organization_name_as_found="Harvard College", role_title="Assistant Dean", occupation="college administrator", start_date="1940", end_date="1942-05", date_precision="Contemporary report and institutional obituary say he resigned in May 1942 to enter wartime service", city="Cambridge", state_or_region="Massachusetts", country="United States", immediate_pre_oss=False, last_civilian_pre_service=True, research_notes="Last civilian employer before Naval Intelligence; not recast as the immediate OSS predecessor."),
        affiliation("voskuil-coi-cartography-b990", 39, "government_assignment", "explicit_immediate", "confirmed", "confirmed", "A_direct_official", organization_key=ORG_COI_CART, organization_name_as_found="COI Cartography Section", role_title="geographer and cartographer", start_date="1941-12", end_date="1942-06", date_precision="CIA history says Voskuil joined the COI Cartography Section after Pearl Harbor; COI became OSS on 13 June 1942", city="Washington", state_or_region="District of Columbia", country="United States", immediate_pre_oss=True, last_civilian_pre_service=False, research_notes="Direct predecessor assignment transferred into OSS."),
        affiliation("voskuil-uiuc-b990", 39, "employment", "strongly_date_bounded", "confirmed", "high", "B_authoritative_institutional", organization_key=ORG_UIUC, organization_name_as_found="University of Illinois", role_title="Assistant in Geography", occupation="geographer", start_date="1940-09-01", end_date="1941-06", date_precision="Board minutes appoint him for ten months beginning 1 September 1940; CIA history places him in COI after Pearl Harbor", city="Urbana", state_or_region="Illinois", country="United States", immediate_pre_oss=False, last_civilian_pre_service=True, research_notes="Last documented civilian employer before COI; no later civilian role was found in the reviewed chronology."),
        affiliation("votichenko-us-navy-b990", 41, "military_assignment", "probable_immediate", "high_confidence", "medium", "B_authoritative_institutional", "publish_qualified", organization_key=ORG_US_NAVY, organization_name_as_found="Navy", role_title="lieutenant commander; military-government assignment in liberated France", start_date="1941", end_date="1945", date_precision="Princeton memorial places the Navy and military-government service during World War II and later associates him with OSS in North Africa", country="United States", immediate_pre_oss=True, last_civilian_pre_service=False, research_notes="Qualified predecessor affiliation because the memorial's OSS chronology is imprecise."),
        affiliation("votichenko-princeton-b990", 41, "student", "documented_prewar", "high_confidence", "high", "B_authoritative_institutional", organization_key=ORG_PRINCETON, organization_name_as_found="Princeton", role_title="undergraduate student", end_date="1940", date_precision="Princeton class memorial identifies him as a 1940 graduate", city="Princeton", state_or_region="New Jersey", country="United States", immediate_pre_oss=False, last_civilian_pre_service=False, research_notes="Student status only; Princeton is not classified as his employer."),
        affiliation("vougnon-maquis-c134-b990", 43, "military_assignment", "probable_immediate", "probable", "medium", "B_authoritative_institutional", "publish_qualified", organization_key=ORG_MAQUIS_C134, organization_name_as_found="Maquis C-134", role_title="commander", start_date="1944-04", date_precision="Resistance-museum record identifies Claude Vougnon as commander; exact OSS liaison and transfer chronology require the personnel file", country="France", immediate_pre_oss=True, last_civilian_pre_service=False, research_notes="Qualified Allied resistance affiliation based on the rare exact name and compatible lieutenant context."),
        affiliation("vournas-us-army-b990", 46, "military_assignment", "explicit_immediate", "high_confidence", "high", "C_reputable_contemporary_or_scholarly", organization_key=ORG_US_ARMY, organization_name_as_found="Army", role_title="officer assigned to OSS in Europe and North Africa", start_date="1943", date_precision="Obituary explicitly says the Army assigned him to OSS; AHEPA history independently places him on Army duty in Egypt in 1943", country="United States", immediate_pre_oss=True, last_civilian_pre_service=False, research_notes="Direct Army-to-OSS assignment; indexed Major rank is compatible."),
        affiliation("vournas-private-practice-b990", 46, "self_employment", "strongly_date_bounded", "high_confidence", "high", "C_reputable_contemporary_or_scholarly", organization_name_as_found="private practice of international law", role_title="attorney", occupation="lawyer", end_date="1942", date_precision="A 1940 federal decision lists him as counsel; obituary describes a long private practice before and after wartime Army service", city="Washington", state_or_region="District of Columbia", country="United States", immediate_pre_oss=False, last_civilian_pre_service=True, research_notes="Qualified as self-employment because no law firm is named in the reviewed sources."),
    ])
    return values


def claim(row: int, key: str, claim_type: str, claim_text: str, paraphrase: str, identity: str, temporal: str, quality: str, confidence: str, sources_value: list[dict[str, str]], notes: str, affiliation_key: str | None = None, status: str = "published") -> dict[str, object]:
    value: dict[str, object] = {
        "key": key, "person_id": PEOPLE[row][0], "claim_type": claim_type,
        "claim_text": claim_text, "evidence_paraphrase": paraphrase,
        "identity_match_assessment": identity, "temporal_assessment": temporal,
        "source_quality": quality, "claim_confidence": confidence,
        "publication_status": status, "match_notes": notes, "sources": sources_value,
    }
    if affiliation_key:
        value["affiliation_key"] = affiliation_key
    return value


def identity_claim(row: int, text: str, paraphrase: str, identity: str, temporal: str, quality: str, confidence: str, sources_value: list[dict[str, str]], notes: str, status: str = "published") -> dict[str, object]:
    return claim(row, f"identity-{slug(PEOPLE[row][1])}-b990", "identity", text, paraphrase, identity, temporal, quality, confidence, sources_value, notes, status=status)


def affiliation_claim(row: int, key: str, claim_type: str, text: str, paraphrase: str, identity: str, temporal: str, quality: str, confidence: str, sources_value: list[dict[str, str]], notes: str, status: str = "published") -> dict[str, object]:
    return claim(row, f"claim-{key}", claim_type, text, paraphrase, identity, temporal, quality, confidence, sources_value, notes, key, status)


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, official, _public) in ARMY_OCCUPATIONS.items():
        key = f"{slug(PEOPLE[row][1])}-army-category-b990"
        if row != 44:
            values.append(identity_claim(row, f"Indexed {PEOPLE[row][1]} is high-confidence matched to the official Army entry reviewed for Batch 990.", "The exact official name and a nonshared protected identifier directly link the printed row to the reviewed Army record.", "High confidence from exact name and a nonshared protected identifier; the protected value and raw bulk record are withheld.", "The dated Army entry precedes the later OSS-index context; the personnel file remains necessary to document the transfer sequence.", "A_direct_official", "high", [{"source_key": INDEX}, {"source_key": ARMY, "locator_override": "Accepted identity bridge; protected identifier and raw record withheld"}], "The identity bridge does not by itself establish an employer or immediate pre-OSS affiliation."))
        values.append(affiliation_claim(row, key, "occupation", f"At Army entry on {date}, {PEOPLE[row][1]}'s historical civilian category was {official.lower()}.", f"The official Army field carries historical code {code}; NARA's code list defines it as {official}.", "High confidence from the reviewed official identity bridge.", "Dated at Army entry before the later OSS-index context; no named employer, workplace, duration or exact OSS-transfer date is supplied.", "A_direct_official", "medium", [{"source_key": ARMY, "locator_override": "Reviewed Army entry; raw record and identifier withheld"}, {"source_key": TECH}, {"source_key": CODES, "locator_override": f"Historical civilian occupation code {code}"}], "Published as a qualified historical category only; excluded from verified-employer analytics.", "publish_qualified"))
    values.extend([
        identity_claim(24, "The indexed Wilhelm-Viggo E.F. Von Moltke is probably the architect Wilhelm Viggo von Moltke documented in an institutional architecture database.", "The rare name and chronology agree; the profile documents Harvard study, Philadelphia architecture work in 1942 and U.S. Army service beginning in 1943.", "Probable because the profile omits the indexed E.F. initials and does not mention OSS.", "The employment is dated 1942 and Army service 1943, but the OSS transfer is not documented.", "B_authoritative_institutional", "medium", [{"source_key": INDEX}, {"source_key": PAB_MOLTKE}], "Qualified identity pending review of Box 808.", "publish_qualified"),
        affiliation_claim(24, "moltke-howe-stonorov-kahn-b990", "last_civilian_pre_service", "Wilhelm Viggo von Moltke worked for Howe, Stonorov & Kahn in 1942 before U.S. Army service began in 1943.", "The institutional professional biography lists the Philadelphia architecture firm in 1942 and Army service from 1943.", "Probable identity from the rare name and chronology; the indexed initials and OSS link remain unconfirmed.", "Strongly date-bounded as the last listed civilian employment before Army service; not proven immediate to OSS.", "B_authoritative_institutional", "medium", [{"source_key": PAB_MOLTKE}], "Published as qualified last-civilian employment and excluded from default high-identity analytics.", "publish_qualified"),
        identity_claim(26, "Indexed Rudolph C Von Ripper is high-confidence identified as Austrian-born artist and U.S. Army officer Rudolf Charles von Ripper.", "Official Army sources give the matching distinctive name, Charles middle name, 1942 Army entry, art service and later OSS recruitment.", "High confidence from the distinctive exact name, matching middle name and direct Army-to-OSS chronology.", "Official sources establish Army service before OSS recruitment.", "A_direct_official", "high", [{"source_key": INDEX}, {"source_key": DVIDS_RIPPER}, {"source_key": ARMY_RIPPER}], "The indexed personnel file remains necessary for the exact transfer date."),
        affiliation_claim(26, "ripper-us-army-b990", "immediate_pre_oss_affiliation", "Rudolf von Ripper served in the U.S. Army, including the War Art Unit, before recruitment into OSS.", "Official Army sources describe his Army art and intelligence service followed by OSS recruitment.", "High-confidence identity from the distinctive name and Charles middle name.", "Explicit Army-to-OSS sequence; exact transfer date is not supplied.", "A_direct_official", "high", [{"source_key": DVIDS_RIPPER}, {"source_key": ARMY_RIPPER}], "Military assignment, not civilian employment."),
        identity_claim(32, "Indexed Nicholas A Vonneuman is confirmed as the Army serviceman and OSS assignee whose curriculum vitae appears in his 1987 manuscript.", "Exact name, nonshared protected Army identifier, matching 1942 entry and an autobiographical 1943-1945 OSS chronology converge.", "Confirmed from the official protected-identifier bridge plus a specific first-person employment and OSS chronology.", "The curriculum vitae explicitly sequences bank, Army training and detached OSS service.", "A_direct_official", "confirmed", [{"source_key": INDEX}, {"source_key": ARMY, "locator_override": "Accepted exact-name identity bridge; identifier withheld"}, {"source_key": VONNEUMAN_CV}], "The first-person source is corroborated by the official Army record."),
        affiliation_claim(32, "vonneuman-us-army-b990", "immediate_pre_oss_affiliation", "Nicholas A. Vonneuman moved from Army infantry and language training into detached OSS service in 1943.", "His curriculum vitae gives 1942-1943 Army training followed by 1943-1945 U.S. Army detached service with OSS.", "Confirmed by exact-name autobiographical chronology and the official Army identity bridge.", "Explicit sequence directly identifies the predecessor military assignment.", "A_direct_official", "confirmed", [{"source_key": VONNEUMAN_CV}, {"source_key": ARMY, "locator_override": "Accepted exact-name identity bridge; identifier withheld"}], "No civilian employer is inferred from the Army assignment."),
        affiliation_claim(32, "vonneuman-national-city-b990", "last_civilian_pre_service", "Nicholas A. Vonneuman was an auditor in National City Bank of New York's Comptrollers Department from 1937 to 1942.", "His curriculum vitae lists the bank and role immediately before 1942-1943 Army service.", "Confirmed by exact-name autobiography and official Army bridge.", "Strongly date-bounded as the last civilian employer before Army service.", "C_reputable_contemporary_or_scholarly", "high", [{"source_key": VONNEUMAN_CV}, {"source_key": ARMY, "support_type": "context_only", "locator_override": "Official 1942 Army-entry corroboration; identifier withheld"}], "Historical employer name preserved; not modernized."),
        identity_claim(33, "Indexed Francis S Vonstade is high-confidence identified as Francis Skiddy von Stade Jr., Harvard assistant dean and wartime Naval Intelligence entrant.", "Contemporary and institutional Harvard sources use the full name and document his 1942 resignation for wartime intelligence service.", "High confidence from the distinctive surname, matching first initial and direct wartime chronology.", "The sources explicitly place Harvard employment before Naval Intelligence.", "B_authoritative_institutional", "high", [{"source_key": INDEX}, {"source_key": HARVARD_1942}, {"source_key": HARVARD_1995}], "The personnel file remains necessary to document the later OSS transfer."),
        affiliation_claim(33, "von-stade-naval-intelligence-b990", "immediate_pre_oss_affiliation", "Francis Skiddy von Stade Jr. joined Naval Intelligence after leaving Harvard in 1942.", "Harvard's institutional obituary says he left the College to join Naval Intelligence.", "High-confidence identity from the distinctive name and matching wartime transition.", "Probable immediate OSS predecessor; the source does not give the later transfer date.", "B_authoritative_institutional", "high", [{"source_key": HARVARD_1995}], "Published as a qualified predecessor military-intelligence affiliation.", "publish_qualified"),
        affiliation_claim(33, "von-stade-harvard-b990", "last_civilian_pre_service", "Francis Skiddy von Stade Jr. was Harvard College Assistant Dean until resigning for wartime service in May 1942.", "A contemporary report records the resignation; Harvard's obituary says he had been assistant dean since 1940 and left for Naval Intelligence.", "High-confidence identity from two Harvard sources and the distinctive name.", "Explicit transition from the last civilian employer into wartime intelligence service.", "B_authoritative_institutional", "high", [{"source_key": HARVARD_1942}, {"source_key": HARVARD_1995}], "Harvard is the last civilian employer, not the immediate OSS predecessor."),
        identity_claim(34, "Indexed James A Voorhees is high-confidence matched to the official Army entry spelled James A Voorhes.", "A nonshared protected identifier and one-letter surname variant connect the index row to the Army record.", "High confidence from the protected identifier and minor spelling variant; the protected value is withheld.", "The 23 February 1942 Army entry precedes OSS service, but code 999 supplies no occupation.", "A_direct_official", "high", [{"source_key": INDEX}, {"source_key": ARMY, "locator_override": "Accepted one-letter name variant; protected identifier withheld"}], "No occupation or employer is inferred from undefined historical code 999."),
        identity_claim(36, "Bert D Voot remains a conflicting identity because the printed protected identifier is also assigned to Bert D Vogt and the Army record uses Vogt.", "Two separately indexed people share the identifier while the official Army name agrees only with Bert D Vogt.", "Conflicting: a shared identifier documents an index or filing problem, not permission to merge different printed names.", "No pre-OSS occupation or affiliation can be transferred until both personnel files are compared.", "A_direct_official", "conflicting", [{"source_key": INDEX}, {"source_key": ARMY, "support_type": "contradicts", "locator_override": "Army candidate name differs; protected identifier withheld"}], "Both source rows remain separate in the existing conflict group.", "conflicting"),
        identity_claim(39, "Indexed Robert J Voskuil is confirmed as the geographer who joined the COI Cartography Section and later served as a naval officer in OSS cartography.", "University minutes give exact name and occupation; CIA history places Robert Voskuil in COI cartography, matching the indexed naval rank and OSS file.", "Confirmed from exact name, occupational continuity, official predecessor-organization history and compatible indexed naval rank.", "The dated university appointment precedes COI formation and transfer into OSS.", "A_direct_official", "confirmed", [{"source_key": INDEX}, {"source_key": CIA_CART}, {"source_key": UIUC_1940}], "The combination is specific enough to distinguish the person from namesakes."),
        affiliation_claim(39, "voskuil-coi-cartography-b990", "immediate_pre_oss_affiliation", "Robert Voskuil joined the Coordinator of Information Cartography Section after Pearl Harbor; that section became part of OSS in June 1942.", "CIA's history names Voskuil and the predecessor section, which was operating by February 1942 before COI became OSS.", "Confirmed from exact name, geography/cartography continuity and indexed OSS naval context.", "Explicit predecessor-organization transition into OSS.", "A_direct_official", "confirmed", [{"source_key": CIA_CART}, {"source_key": INDEX, "support_type": "context_only"}], "Direct predecessor government assignment."),
        affiliation_claim(39, "voskuil-uiuc-b990", "last_civilian_pre_service", "Robert J. Voskuil was Assistant in Geography at the University of Illinois for ten months beginning 1 September 1940.", "Board minutes give his exact name, department, appointment length and start date; CIA history next places him in COI after Pearl Harbor.", "Confirmed from exact name, occupation and the later official cartography chronology.", "Strongly date-bounded as the last documented civilian employer before COI.", "B_authoritative_institutional", "high", [{"source_key": UIUC_1940}, {"source_key": CIA_CART, "support_type": "context_only"}], "No later civilian employer was found in the reviewed sequence."),
        identity_claim(40, "Indexed Raymond G Vosper is high-confidence matched to the official Army entry reviewed for Batch 990.", "The exact official name and a nonshared protected identifier directly link the printed row to the reviewed Army record.", "High confidence from exact name and a nonshared protected identifier; the protected value is withheld.", "The Army entry is dated 16 October 1945, after OSS dissolution, so it supports identity only.", "A_direct_official", "high", [{"source_key": INDEX}, {"source_key": ARMY, "locator_override": "Accepted identity bridge; protected identifier withheld"}], "Historical code 125 is not transferred because the dated record is post-OSS."),
        identity_claim(41, "Indexed T.Alexander Votichenko is high-confidence identified as Princeton alumnus Taras A. Votichenko, a Navy lieutenant commander associated with OSS in North Africa.", "The rare surname, T./Taras first name, Alexander middle name and Navy-to-OSS wartime chronology agree.", "High confidence from the distinctive name and direct institutional Navy and OSS context.", "The memorial's phrase 'after the war' makes the precise OSS transition uncertain.", "B_authoritative_institutional", "high", [{"source_key": INDEX}, {"source_key": PRINCETON_VOTICHENKO}], "Name variant retained; Box 808 should clarify the transfer date."),
        affiliation_claim(41, "votichenko-us-navy-b990", "immediate_pre_oss_affiliation", "Taras A. Votichenko served as a Navy lieutenant commander and helped establish U.S. military government in liberated France before his documented OSS association.", "Princeton's memorial places his Navy and military-government work during World War II and then identifies an OSS role in North Africa.", "High-confidence identity from the rare full-name variant and direct wartime context.", "Probable predecessor assignment; the memorial's exact OSS timing is imprecise.", "B_authoritative_institutional", "medium", [{"source_key": PRINCETON_VOTICHENKO}], "Qualified military pathway, excluded from unqualified immediate-affiliation counts.", "publish_qualified"),
        affiliation_claim(41, "votichenko-princeton-b990", "other_pre_oss_affiliation", "Taras A. Votichenko was a Princeton University student and graduated in the Class of 1940.", "Princeton's memorial identifies his class year and undergraduate study.", "High-confidence identity from the rare name and wartime biography.", "Documented prewar student status; not employment and not shown as immediately pre-OSS.", "B_authoritative_institutional", "high", [{"source_key": PRINCETON_VOTICHENKO}], "Student status is kept separate from employment."),
        identity_claim(43, "The indexed Claude Vougnon is probably the French Resistance commander of Maquis C-134.", "A Resistance museum identifies the rare exact name as maquis commander; the indexed first-lieutenant rank is compatible with the wartime context.", "Probable from the rare exact name and compatible Allied rank, but no protected identifier directly links the records.", "The source documents 1944 resistance command; the OSS liaison sequence still requires the personnel file.", "B_authoritative_institutional", "medium", [{"source_key": INDEX}, {"source_key": RESISTANCE_VOUGNON}], "Qualified identity pending Box 808 review.", "publish_qualified"),
        affiliation_claim(43, "vougnon-maquis-c134-b990", "immediate_pre_oss_affiliation", "Claude Vougnon commanded the French Resistance formation Maquis C-134 in 1944.", "The Resistance museum's collection description directly identifies Vougnon as commander.", "Probable identity from the rare name and compatible lieutenant context.", "Probable immediate Allied resistance affiliation; the OSS transfer or liaison date is not established.", "B_authoritative_institutional", "medium", [{"source_key": RESISTANCE_VOUGNON}], "Published as qualified Allied military context, not civilian employment.", "publish_qualified"),
        identity_claim(44, "Indexed Steve Voulgarakis is high-confidence identified as the Army sergeant and Greek Operational Group member documented in veterans-history sources.", "The exact rare name and protected service-number agreement connect the index, official Army record and unit histories.", "High confidence from exact name, nonshared official identifier and consistent Greek Operational Group service.", "The Army entry and unit history precede or coincide with OSS service; no named civilian employer is supplied.", "A_direct_official", "high", [{"source_key": INDEX}, {"source_key": ARMY, "locator_override": "Accepted identity bridge; protected identifier withheld"}, {"source_key": USWM_VOULGARAKIS, "support_type": "context_only"}, {"source_key": OSSOG_VOULGARAKIS, "support_type": "context_only"}], "Full service number remains excluded from public data."),
        identity_claim(46, "Indexed George C Vournas is high-confidence identified as the lawyer and Army officer assigned to OSS in Europe and North Africa.", "Exact name, indexed Major rank, Army-to-OSS obituary and AHEPA wartime officer chronology converge.", "High confidence from the distinctive exact name and two independent wartime biographical sources.", "The sources explicitly place private legal practice before Army and Army assignment before OSS.", "C_reputable_contemporary_or_scholarly", "high", [{"source_key": INDEX}, {"source_key": WAPO_VOURNAS}, {"source_key": AHEPA_VOURNAS}], "The personnel file remains necessary for exact dates."),
        affiliation_claim(46, "vournas-us-army-b990", "immediate_pre_oss_affiliation", "George C. Vournas was a U.S. Army officer assigned to OSS in Europe and North Africa.", "The obituary explicitly describes the Army assignment; AHEPA history independently places him on Army duty in Egypt in 1943.", "High-confidence identity from exact name, officer status and compatible wartime chronology.", "Explicit immediate Army-to-OSS assignment.", "C_reputable_contemporary_or_scholarly", "high", [{"source_key": WAPO_VOURNAS}, {"source_key": AHEPA_VOURNAS}], "Military assignment, not civilian employment."),
        affiliation_claim(46, "vournas-private-practice-b990", "last_civilian_pre_service", "George C. Vournas practiced law privately before wartime Army service.", "A 1940 federal decision lists him as counsel, and his obituary describes more than six decades in private international-law practice.", "High-confidence identity from the exact name and direct Army-to-OSS biography.", "Strongly date-bounded civilian work before Army service; no named firm is supplied.", "C_reputable_contemporary_or_scholarly", "high", [{"source_key": COURT_VOURNAS}, {"source_key": WAPO_VOURNAS}], "Recorded as self-employment rather than inventing a law-firm employer."),
    ])
    return values


def base_update(row: int, **overrides: object) -> dict[str, object]:
    value: dict[str, object] = {
        "person_id": PEOPLE[row][0], "manual_review_required": True,
        "personnel_file_digitized": False, "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }
    value.update(overrides)
    return value


def person_updates() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, reason in UNRESOLVED.items():
        values.append(base_update(row, identity_status="unresolved", identity_evidence=f"The visually verified page 485 row preserves {PEOPLE[row][1]} and its indexed Box 808 context. {reason}", research_status="requires_archival_review", next_action=f"Review the indexed personnel file for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}"))
    for row in ARMY_OCCUPATIONS:
        values.append(base_update(row, identity_status="high_confidence", identity_evidence="The exact official name and a nonshared protected-identifier agreement support the Army identity match; the protected value remains private.", personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="occupation_only_found", next_action="Review Box 808 to identify any named employer behind the historical Army category and establish the Army-to-OSS chronology.", nara_catalog_id="1263923"))
    values.extend([
        base_update(24, identity_status="probable", identity_evidence="The rare name and chronology agree with an institutional architecture biography, but the profile omits the indexed E.F. initials and does not mention OSS.", name_variants=["Wilhelm Viggo von Moltke"], research_status="documented_prewar_employer_found", next_action="Review Box 808 for an identity bridge and the Army-to-OSS chronology. Howe, Stonorov & Kahn is published only as qualified last civilian employment.", archival_review_priority="medium"),
        base_update(26, identity_status="high_confidence", identity_evidence="Official Army sources give the distinctive name, Charles middle name, 1942 Army entry, art service and later OSS recruitment.", name_variants=["Rudolf Charles von Ripper", "Rudolf von Ripper"], personnel_category="commissioned_army_officer", commissioned_officer=True, allied_or_foreign_personnel=False, research_status="completed", next_action="Review Box 808 for exact Army-to-OSS transfer dates and any last civilian employer.", archival_review_priority="medium"),
        base_update(27, identity_status="ambiguous", identity_evidence="The index separately prints Walter Von Schuschn in Box 808 and Walter Schuschnigg in Box 690. The rare truncated name suggests a possible duplicate, but different boxes and no protected identifier prohibit merging.", possible_duplicate_group=SCHUSCHNIGG_GROUP, research_status="requires_archival_review", next_action="Compare the Box 808 Walter Von Schuschn file with the Box 690 Walter Schuschnigg file before assigning identity or employment.", archival_review_priority="critical"),
        {"person_id": WALTER_SCHUSCHNIGG_ID, "manual_review_required": True, "possible_duplicate_group": SCHUSCHNIGG_GROUP, "archival_review_priority": "critical", "next_action": "Compare the Box 690 Walter Schuschnigg file with the Box 808 Walter Von Schuschn file; preserve both source rows until direct evidence resolves duplication."},
        base_update(32, identity_status="confirmed", identity_evidence="The official exact-name protected-identifier bridge and Nicholas A. Vonneuman's own curriculum vitae independently establish Army entry, training and detached OSS service.", personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="verified_employer_found", next_action="Box 808 can refine the transfer date and assignment, but the immediate Army pathway and National City Bank employment are documented.", archival_review_priority="low", nara_catalog_id="1263923"),
        base_update(33, identity_status="high_confidence", identity_evidence="Contemporary and institutional Harvard sources use the distinctive full name and document his 1942 resignation for Naval Intelligence.", name_variants=["Francis Skiddy von Stade Jr."], research_status="verified_employer_found", next_action="Review Box 808 to establish the Naval Intelligence-to-OSS transfer date; Harvard College is documented as the last civilian employer.", archival_review_priority="medium"),
        base_update(34, identity_status="high_confidence", identity_evidence="A nonshared protected identifier and one-letter official surname variant connect James A Voorhees to Army entry James A Voorhes.", personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="requires_archival_review", next_action="Review Box 808 for pre-OSS employment and Army-to-OSS chronology. Historical code 999 is undefined.", nara_catalog_id="1263923"),
        base_update(36, identity_status="conflicting", identity_evidence="The printed protected identifier is shared by separately indexed Bert D Voot and Bert D Vogt, while the official Army record uses Vogt. No identity, occupation or employer is transferred.", possible_duplicate_group=VOOT_GROUP, research_status="conflicting_sources", next_action="Review both indexed personnel files together before assigning identity, occupation or pre-OSS affiliation.", archival_review_priority="critical"),
        {"person_id": BERT_VOGT_ID, "manual_review_required": True, "possible_duplicate_group": VOOT_GROUP, "archival_review_priority": "critical", "next_action": "Compare the Bert D Vogt and Bert D Voot personnel files; preserve both source rows until direct evidence resolves the protected-identifier conflict."},
        base_update(39, identity_status="confirmed", identity_evidence="Exact-name University employment, geography/cartography continuity, CIA predecessor-organization history and the compatible indexed naval rank establish the identity.", personnel_category="commissioned_naval_officer", commissioned_officer=True, allied_or_foreign_personnel=False, research_status="verified_employer_found", next_action="Box 808 can refine his OSS rank chronology; COI Cartography and University of Illinois employment are documented.", archival_review_priority="low"),
        base_update(40, identity_status="high_confidence", identity_evidence="The exact official name and a nonshared protected-identifier agreement support the Army identity match; the protected value remains private.", personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="requires_archival_review", next_action="Review Box 808. The accepted Army identity record entered after OSS dissolution, so its occupation supplies no pre-OSS evidence.", nara_catalog_id="1263923"),
        base_update(41, identity_status="high_confidence", identity_evidence="The rare T./Taras Alexander Votichenko name and institutional Navy, military-government and OSS context agree.", name_variants=["Taras A. Votichenko"], personnel_category="commissioned_naval_officer", commissioned_officer=True, allied_or_foreign_personnel=False, research_status="requires_archival_review", next_action="Review Box 808 to resolve the memorial's imprecise OSS chronology and identify any civilian employer before Navy service."),
        base_update(43, identity_status="probable", identity_evidence="A Resistance museum identifies the rare exact name as commander of Maquis C-134; the indexed first-lieutenant context is compatible, but no direct file bridge exists.", personnel_category="foreign_or_allied_military_personnel", commissioned_officer=True, allied_or_foreign_personnel=True, research_status="requires_archival_review", next_action="Review Box 808 for the exact OSS liaison or transfer chronology and civilian background."),
        base_update(46, identity_status="high_confidence", identity_evidence="Exact name, indexed Major rank, Army-to-OSS obituary and independent AHEPA wartime officer chronology converge.", personnel_category="commissioned_army_officer", commissioned_officer=True, allied_or_foreign_personnel=False, research_status="verified_employer_found", next_action="Box 808 can refine dates; Army assignment to OSS and pre-service private legal practice are documented.", archival_review_priority="low"),
    ])
    return values


def research_attempts() -> list[dict[str, object]]:
    sourced = {24, 26, 30, 32, 33, 34, 36, 38, 39, 40, 41, 42, 43, 44, 46}
    details = {
        24: "Institutional architecture evidence produced a qualified 1942 last-civilian employer and probable identity.",
        26: "Official Army histories established a high-confidence Army-to-OSS pathway.",
        32: "Official Army evidence and the subject's visually reviewed curriculum vitae established the bank, Army and OSS chronology.",
        33: "Contemporary and institutional Harvard sources established the last civilian employer and Naval Intelligence transition.",
        39: "Official CIA history and visually reviewed University minutes established the COI predecessor assignment and last civilian employer.",
        41: "Princeton's memorial established a high-confidence identity and qualified Navy pathway while leaving exact OSS timing uncertain.",
        43: "Resistance-museum evidence produced a qualified probable identity and Allied resistance affiliation.",
        46: "Obituary, institutional history and a federal court record established Army assignment and pre-service legal practice.",
    }
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        if row in sourced:
            outcome, reviewed, rejected = "source_reviewed", 8, 5
            detail = details.get(row, "Official Army identity review produced the accepted identity, qualified historical occupation, identity-only or conflict outcome recorded in the bundle.")
        else:
            outcome, reviewed, rejected = "no_result", 6, 6
            detail = UNRESOLVED.get(row, "No reliable identity or pre-OSS affiliation bridge was found.")
        attempts.append({
            "key": f"page485-row{row}-{slug(name)}-b990", "person_id": person_id,
            "source_adapter": "manual_staged_protocol",
            "query_text": f"{name}; NARA OSS index context; CIA Reading Room or equivalent official-source check; Library of Congress collection check; exact-name and meaningful variants; OSS, rank, branch, identifier and assignment clues; employer and occupation 1940; obituary, institutional, newspaper, directory and archival searches; indexed Box 807 or 808; protected identifiers used only in private official-record comparison",
            "query_variant_type": "staged_identity_employment_archival_protocol_batch_990",
            "started_at": "2026-10-30T16:30:00Z", "completed_at": "2026-10-30T18:45:00Z",
            "outcome": outcome, "sources_reviewed": reviewed, "candidate_sources_rejected": rejected,
            "rejection_reasons": "Unbridged namesakes, snippets, commercial people-finder pages, relatives, unsourced genealogy, postwar-only leads and sources without an OSS, protected-identifier, rank, unit or personnel-file bridge were rejected. Robert von Neumann candidates and Joseph Vona's obituary were not assigned without corroboration. Historical Army occupation categories were not converted into named employers. Walter Von Schuschn and Walter Schuschnigg, and Bert D Voot and Bert D Vogt, remain separate possible duplicates or conflicts.",
            "research_notes": f"{detail} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain and archival searches were checked as applicable. The CIA adapter recorded its robots restriction without bypass. The LoC.gov adapter timed out and was not treated as negative evidence; a current collection check produced no publishable candidate for this review. The NARA index page and official Army technical evidence were inspected directly. Relevant PDF pages for Nicholas Vonneuman and Robert Voskuil were rendered and visually checked. No search-result snippet was used as sole final evidence, no paywall or access control was bypassed, and no authenticated NARA Catalog API call was made.",
            "next_action": "Review the indexed personnel file for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before wartime service.",
            "attempt_number": 1, "research_agent_version": "before-oss-b990-v1",
        })
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-990-v1",
        "reviewer": "Before OSS Batch 990 evidence review",
        "sources": sources(), "organizations": organizations(),
        "affiliations": affiliations(), "claims": claims(),
        "person_updates": person_updates(), "research_attempts": research_attempts(),
    }
    EvidenceBundle.model_validate(bundle)
    OUTPUT.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
