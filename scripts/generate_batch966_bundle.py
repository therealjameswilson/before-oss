#!/usr/bin/env python3
"""Generate the reviewed Batch 966 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page473-michael-troisi-to-john-truden-"
    "review_batch-966_2026-10-30.json"
)

INDEX = "nara-index-b966"
ARMY = "army-bulk-b966"
TECH = "army-tech-b966"
CODES = "army-codes-b966"
TROMBETTI_ANPI = "anpi-trombetti-b966"
TRONDSEN_NARA = "nara-trondsen-award-b966"
TRONDSEN_KRIGSSEILER = "krigsseiler-trondsen-b966"
TRONSTAD_NBL = "nbl-tronstad-b966"
TRONSTAD_NTNU = "ntnu-tronstad-b966"
TRONSTAD_FFI = "ffi-tronstad-b966"


PEOPLE = {
    24: ("3e06b568-db40-5d2d-9cb5-2921372ae0d9", "Michael J Troisi"),
    25: ("98f948a9-b536-55ce-beeb-6d9b9676af99", "Frank Trojohak"),
    26: ("8ffd065a-0d35-5dac-9004-68cf33bdb78b", "Adams L Trollinger"),
    27: ("7affd747-6b2c-59da-b55b-c48217bd611d", "Benny Trombatore"),
    28: ("239eb1ea-4096-5cb2-9ed6-e83ee3a71a35", "Ferruccio Trombetti"),
    29: ("d4eae027-85f1-50db-8cfa-5fc4eee7b84f", "Inge Trondsen"),
    30: ("9d26e766-fb32-5506-a5bf-e1e68036ce38", "Lief Trondstad"),
    31: ("3771872a-8d0c-5a46-9edb-7f88f7a0ef57", "Marion L Tronoski"),
    32: ("fddeb05f-ea5b-5e20-8246-67e1df81e9ad", "Louis J Trotta"),
    33: ("17743b13-54c3-5b87-96b1-6098f864afb9", "Robert E Trotter"),
    34: ("ecbd4409-0b42-5d07-a33e-5be97302eb1d", "Albert L Troughton"),
    35: ("8f7035ca-2440-5a65-b7a9-6b51adfe8158", "Peter D Troupos"),
    36: ("3e39a157-114c-5644-9983-974a621bb097", "Howell B Trousdale"),
    37: ("a77efd7b-cd86-5e3f-b475-6bd44f2ac20c", "Albert K Trout"),
    38: ("bb910e68-8372-58d8-bcf7-f98bc0b9ef45", "Harold A Trout"),
    39: ("1f8b541f-c3b5-5b9e-b136-aeaa9e836a52", "Neva F Troutman"),
    40: ("2a7d5c3f-f48a-5124-8627-bc9d3a90b1db", "John E Trowbridge"),
    41: ("0b5434ef-51aa-555f-99e1-d8a2efcc51fa", "Thomas J Troxell"),
    42: ("99c88a15-886f-554b-9343-400923f57784", "Herbert Troyke"),
    43: ("a45d3f0c-5c3e-5d3b-936f-3760a14ee36f", "Ernest A Trudeau"),
    44: ("469cd537-bead-5280-bb00-dbc3b0b963c7", "Francis H Trudeau"),
    45: ("74b8e18a-d2de-5eb9-bc25-01d7251a5570", "Dorothy J Trudel"),
    46: ("eaa68846-88e6-53d3-b6e6-48d371cbac27", "John V Truden"),
}


ARMY_OCCUPATIONS = [
    {
        "row": 24,
        "date": "1943-03-09",
        "code": "685",
        "occupation": "Welders and flame cutters",
        "public_occupation": "welder or flame cutter",
        "relationship_type": "unknown",
        "locator": "PDF physical page 174; historical category 6-85",
    },
    {
        "row": 32,
        "date": "1943-02-12",
        "code": "678",
        "occupation": "Machine shop and related occupations, n.e.c.",
        "public_occupation": "machine-shop occupation, not elsewhere classified",
        "relationship_type": "unknown",
        "locator": "PDF physical page 177; historical category 6-78",
    },
    {
        "row": 33,
        "date": "1943-04-21",
        "code": "316",
        "occupation": "Farm hands, general farms",
        "public_occupation": "general-farm hand",
        "relationship_type": "employment",
        "locator": "PDF physical page 172; historical category 3-16",
    },
    {
        "row": 38,
        "date": "1942-04-28",
        "code": "306",
        "occupation": "General farmers",
        "public_occupation": "general farmer",
        "relationship_type": "unknown",
        "locator": "PDF physical page 172; historical category 3-06",
    },
    {
        "row": 41,
        "date": "1942-08-28",
        "code": "227",
        "occupation": "Waiters and waitresses, except private family",
        "public_occupation": "waiter",
        "relationship_type": "employment",
        "locator": "PDF physical page 172; historical category 2-27",
    },
    {
        "row": 43,
        "date": "1941-01-16",
        "code": "138",
        "occupation": "Stock clerks",
        "public_occupation": "stock clerk",
        "relationship_type": "employment",
        "locator": "PDF physical page 171; historical category 1-38",
    },
    {
        "row": 46,
        "date": "1943-03-18",
        "code": "992",
        "occupation": "Students",
        "public_occupation": "student",
        "relationship_type": "student",
        "locator": "PDF physical page 304; historical category 9-92",
    },
]


UNRESOLVED = {
    26: "A derivative birth-place lead and family material lacked an OSS, protected-identifier or Box 786 bridge and was rejected.",
    27: "Exact-name, occupation, obituary, institutional, newspaper and archival searches produced no defensible identity bridge.",
    31: "Exact-name and spelling-variant searches produced no reliable OSS identity, dated occupation or employing organization.",
    34: "Military mission-list and burial namesakes lacked an OSS, protected-identifier or Box 786 bridge and cannot support a pre-OSS claim.",
    35: "A church memorial and similarly named people lacked corroborating OSS or service identifiers and were rejected.",
    36: "Exact-name, occupation, obituary and archival searches produced no defensible identity or chronology for the indexed person.",
    37: "The common name produced multiple namesakes without two corroborating identifiers beyond the name.",
    39: "Exact-name and variant searches produced no reliable identity bridge or documented pre-OSS affiliation.",
    40: "Multiple John E Trowbridge namesakes remained indistinguishable without two corroborating identifiers beyond the name.",
    42: "Derivative birth and death material supplied no OSS, protected-identifier or Box 786 bridge and was not used.",
    44: "An official British-file catalogue lead could not be inspected in accessible form and did not independently bridge the indexed person to OSS or a pre-OSS employer.",
    45: "A descendant's obituary was irrelevant to the indexed person's employment and identity and was rejected; no reliable direct source was found.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Box 786",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 473, rows 24-46; checked against layout-preserving text and a 200 dpi page render",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. Protected identifiers remain private.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; eight accepted Batch 966 identity candidates; protected identifiers withheld",
            "access_date": "2026-10-29",
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
            "access_date": "2026-10-29",
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
            "locator": "PDF physical pages 171, 172, 174, 177 and 304; seven Batch 966 historical civilian-status categories visually and textually checked",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical occupation and student groups identify neither employers, workplaces nor schools.",
        },
        {
            "key": TROMBETTI_ANPI,
            "stable_url": "https://anpibologna.it/wp-content/uploads/2018/10/RESISTENZA_2008_4.pdf",
            "title": "Attenzione, qui radio Mele…, tutte le notizie sui nazifascisti",
            "author_creator": "R.B.; based on research by Marco Minardi",
            "repository_publisher": "ANPI Provinciale di Bologna",
            "publication_record_date": "2008-09",
            "locator": "Resistenza, year VI, no. 4, printed pages 14-15; PDF physical pages 14-15",
            "access_date": "2026-10-29",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Resistenza, organ of ANPI Provinciale di Bologna",
            "rights_notes": "Only concise project-authored paraphrases and excerpts under 25 words are retained.",
        },
        {
            "key": TRONDSEN_NARA,
            "stable_url": "https://www.archives.gov/files/research/jfk/releases/104-10165-10120.pdf",
            "archival_identifier": "JFK release 104-10165-10120; OSS SO Branch award recommendations",
            "title": "Survey of Board Recommendations: SO Branch, Bronze Star (continued)",
            "author_creator": "Office of Strategic Services",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1945",
            "locator": "PDF physical page 114, printed page 75; Sub-Lt Inge Trondsen row visually inspected against its own recommendation text",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "JFK Assassination Records Collection",
            "document_number": "104-10165-10120",
            "rights_notes": "The adjacent Jens Nordlie recommendation is not attributed to Trondsen.",
        },
        {
            "key": TRONDSEN_KRIGSSEILER,
            "stable_url": "https://krigsseilerregisteret.no/sjofolk/%35%33%33%36%38%32",
            "archival_identifier": "Krigsseilerregisteret: Inge Trondsen; source references include TNA HS 9/1486/3",
            "title": "Inge Trondsen",
            "author_creator": "Norsk senter for krigsseilerhistorie",
            "repository_publisher": "Krigsseilerregisteret; Stiftelsen Arkivet",
            "locator": "Opplysninger and Mønstringer tabs; M/S Thalatta row and Norwegian Navy chronology",
            "access_date": "2026-10-29",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Krigsseilerregisteret",
            "rights_notes": "The public record number is URL-encoded because its digit string coincides with an unrelated private index identifier. The register warns that individual records may be incomplete.",
        },
        {
            "key": TRONSTAD_NBL,
            "stable_url": "https://nbl.snl.no/Leif_Tronstad",
            "title": "Leif Tronstad",
            "author_creator": "Gunnar Thorsen",
            "repository_publisher": "Norsk biografisk leksikon; Store norske leksikon",
            "publication_record_date": "1999-2005; page last updated 2026-06-06",
            "locator": "Career paragraphs on NTH, Norsk Aluminium Co., Norsk Hydro, 1940 mobilization and 1941 Norwegian High Command service",
            "access_date": "2026-10-29",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Norsk biografisk leksikon",
            "rights_notes": "The source supports the Leif Tronstad biography but does not independently bridge the misspelled OSS index row.",
        },
        {
            "key": TRONSTAD_NTNU,
            "stable_url": "https://uhs.vm.ntnu.no/tronstad-og-tungtvannet/",
            "title": "Tronstad og tungtvannet",
            "author_creator": "Tove Eivindsen",
            "repository_publisher": "NTNU University Historical Collections",
            "publication_record_date": "2017-11-09",
            "locator": "Biographical section on NTH professorship, Norsk Hydro consulting and wartime resistance work",
            "access_date": "2026-10-29",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "NTNU University Historical Collections",
        },
        {
            "key": TRONSTAD_FFI,
            "stable_url": "https://www.ffi.no/en/publications/fact-sheets/leif-tronstad--the-father-of-ffi",
            "archival_identifier": "FFI fact sheet, January 2026",
            "title": "Leif Tronstad — The Father of FFI",
            "author_creator": "Norwegian Defence Research Establishment",
            "repository_publisher": "Norwegian Defence Research Establishment",
            "publication_record_date": "2026-01",
            "locator": "PDF page 1; biography, NTH professorship held at the April 1940 invasion and Norwegian High Command major rank",
            "access_date": "2026-10-29",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "FFI fact sheets",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": "italian-resistance-lazio",
            "canonical_name": "Italian Resistance in Lazio",
            "historical_name": "Resistenza nell'area dei Castelli romani, Civitavecchia e Viterbo",
            "aliases": ["Lazio Resistance", "Italian partisan resistance in Lazio"],
            "organization_type": "resistance movement",
            "sector": "military",
            "state_or_region": "Lazio",
            "country": "Italy",
            "active_dates": "1943-1944",
            "normalization_notes": "A regional resistance status, not a single corporate employer or a claim of formal rank.",
        },
        {
            "key": "royal-italian-army",
            "canonical_name": "Royal Italian Army",
            "historical_name": "Regio Esercito Italiano",
            "aliases": ["Italian Royal Army", "Regio Esercito"],
            "organization_type": "military service",
            "sector": "military",
            "country": "Italy",
            "active_dates": "1861-1946",
            "normalization_notes": "The historical wartime service is preserved without substituting the modern Italian Army.",
        },
        {
            "key": "royal-norwegian-navy",
            "canonical_name": "Royal Norwegian Navy",
            "historical_name": "Den Kongelige Norske Marine",
            "aliases": ["Norwegian Navy", "Norsk marine", "RN"],
            "organization_type": "military service",
            "sector": "military",
            "country": "Norway",
            "normalization_notes": "Trondsen's institutional register says he served in the Norwegian Navy for the rest of the war after September 1940.",
        },
        {
            "key": "norwegian-institute-of-technology",
            "canonical_name": "Norwegian Institute of Technology",
            "historical_name": "Norges tekniske høgskole",
            "aliases": ["NTH", "Norwegian Institute of Technology (NTH)"],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "Trondheim",
            "country": "Norway",
            "active_dates": "1910-1996",
            "normalization_notes": "The historical institution is retained rather than silently replaced by its modern NTNU successor.",
        },
        {
            "key": "norsk-hydro",
            "canonical_name": "Norsk Hydro",
            "historical_name": "Norsk Hydro",
            "aliases": ["Norsk Hydro-Elektrisk Kvælstofaktieselskab"],
            "organization_type": "industrial company",
            "sector": "business_and_industry",
            "country": "Norway",
            "normalization_notes": "The historical company name is preserved; consulting is modeled as a professional affiliation, not silently converted into salaried employment.",
        },
        {
            "key": "norsk-aluminium-company",
            "canonical_name": "Norsk Aluminium Company",
            "historical_name": "Norsk Aluminium Co.",
            "aliases": ["NACO", "Norsk Aluminium Co."],
            "organization_type": "industrial company",
            "sector": "business_and_industry",
            "country": "Norway",
            "normalization_notes": "The historical company remains distinct from later corporate successors and mergers.",
        },
    ]


def army_affiliation(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    return {
        "key": f"{slug(PEOPLE[row][1])}-occupation-b966",
        "person_id": PEOPLE[row][0],
        "occupation": item["public_occupation"],
        "relationship_type": item["relationship_type"],
        "end_date": item["date"],
        "date_precision": f"Historical civilian-status code {item['code']} was recorded at Army entry on {item['date']}; no employer, workplace, school or OSS-transfer date is named.",
        "country": "United States",
        "immediate_pre_oss": False,
        "last_civilian_pre_service": False,
        "pre_oss_temporal_basis": "strongly_date_bounded",
        "identity_confidence": "high_confidence",
        "claim_confidence": "medium",
        "source_quality": "A_direct_official",
        "publication_status": "publish_qualified",
        "research_notes": "The historical category is not converted into a named employer, workplace, school, self-employment claim or immediate pre-OSS affiliation.",
    }


def specialist_affiliations() -> list[dict[str, object]]:
    return [
        {
            "key": "ferruccio-trombetti-resistance-b966",
            "person_id": PEOPLE[28][0],
            "organization_key": "italian-resistance-lazio",
            "organization_name_as_found": "Resistenza nell'area dei Castelli romani, Civitavecchia e Viterbo",
            "role_title": "partisan and resistance organizer",
            "relationship_type": "volunteer",
            "start_date": "1943-09",
            "end_date": "1944-06",
            "date_precision": "The account places his Resistance organizing between the September 1943 defense of Rome and Rome's June 1944 liberation, immediately before OSS selection.",
            "state_or_region": "Lazio",
            "country": "Italy",
            "immediate_pre_oss": True,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "explicit_immediate",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "published",
            "research_notes": "The source explicitly says the Rome Communist federation recommended Trombetti and OSS selected him for Operation Appomatox after the liberation of Rome.",
        },
        {
            "key": "ferruccio-trombetti-hemp-worker-b966",
            "person_id": PEOPLE[28][0],
            "role_title": "hemp worker",
            "occupation": "hemp worker",
            "relationship_type": "employment",
            "end_date": "1937",
            "date_precision": "The profile identifies hemp work before compulsory military service and deployment to Spain in 1937; no employer is named.",
            "state_or_region": "Emilia-Romagna",
            "country": "Italy",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "high_confidence",
            "claim_confidence": "medium",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "publish_qualified",
            "research_notes": "The occupation is not converted into a named employer and is not labeled the immediate OSS predecessor.",
        },
        {
            "key": "ferruccio-trombetti-italian-army-b966",
            "person_id": PEOPLE[28][0],
            "organization_key": "royal-italian-army",
            "organization_name_as_found": "regio esercito italiano; II Reggimento granatieri",
            "role_title": "conscript; 2nd Grenadier Regiment",
            "relationship_type": "military_assignment",
            "start_date": "1937",
            "end_date": "1943-09",
            "date_precision": "The account dates Spain service to 1937-1939, continued Royal Italian Army retention and the September 1943 defense of Rome.",
            "country": "Italy",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "high_confidence",
            "claim_confidence": "medium",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "publish_qualified",
            "research_notes": "This earlier military chronology is separated from his later Resistance status and OSS selection.",
        },
        {
            "key": "inge-trondsen-navy-b966",
            "person_id": PEOPLE[29][0],
            "organization_key": "royal-norwegian-navy",
            "organization_name_as_found": "den norske marine; Sub-Lt Inge Trondsen, RN",
            "role_title": "ensign and sub-lieutenant; captain of a U.S. sub-chaser",
            "relationship_type": "military_assignment",
            "start_date": "1940-09-03",
            "end_date": "1945",
            "date_precision": "The maritime register dates his acceptance to the Navy radio course to 3 September 1940 and says he served in the Navy for the rest of the war; the original OSS sheet supplies the sub-lieutenant rank and clandestine command.",
            "country": "Norway",
            "immediate_pre_oss": True,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "probable_immediate",
            "identity_confidence": "confirmed",
            "claim_confidence": "medium",
            "source_quality": "A_direct_official",
            "publication_status": "publish_qualified",
            "research_notes": "The sources establish an ongoing Allied naval affiliation during OSS cooperation, but not a formal administrative transfer into U.S. OSS employment.",
        },
        {
            "key": "inge-trondsen-thalatta-b966",
            "person_id": PEOPLE[29][0],
            "organization_name_as_found": "M/S Thalatta (vessel; employing company not named)",
            "role_title": "fourth mate",
            "occupation": "merchant-marine fourth mate",
            "relationship_type": "professional_affiliation",
            "start_date": "1940-01-12",
            "end_date": "1940-08-01",
            "date_precision": "The muster records fourth-mate service from 12 January to 1 August 1940; the Navy radio-course acceptance followed on 3 September 1940.",
            "country": "Norway",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "confirmed",
            "claim_confidence": "high",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "published",
            "research_notes": "The shipboard service is modeled as a professional affiliation, not an employer. The employing company and any intervening August-September status remain unresolved.",
        },
        {
            "key": "leif-tronstad-nth-b966",
            "person_id": PEOPLE[30][0],
            "organization_key": "norwegian-institute-of-technology",
            "organization_name_as_found": "Norges tekniske høgskole (NTH)",
            "role_title": "professor and institute head in inorganic chemistry",
            "occupation": "chemistry professor",
            "relationship_type": "employment",
            "start_date": "1931",
            "end_date": "1940-04",
            "date_precision": "NBL dates his docent appointment to 1931, institute leadership to 1934 and professorship to 1936; FFI says he still held the position when Germany invaded in April 1940.",
            "city": "Trondheim",
            "country": "Norway",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": True,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "probable",
            "claim_confidence": "medium",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "publish_qualified",
            "research_notes": "The employment is explicit for Leif Tronstad, but the misspelled Lief Trondstad OSS index identity lacks an independent file or OSS bridge.",
        },
        {
            "key": "leif-tronstad-hydro-b966",
            "person_id": PEOPLE[30][0],
            "organization_key": "norsk-hydro",
            "organization_name_as_found": "Norsk Hydro",
            "role_title": "consultant on heavy-water production",
            "occupation": "chemical consultant",
            "relationship_type": "professional_affiliation",
            "start_date": "1934",
            "end_date": "1940",
            "date_precision": "NBL dates the consulting relationship from 1934; the exact contract end is not given, so 1940 marks the prewar research boundary rather than a proven termination.",
            "country": "Norway",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "probable",
            "claim_confidence": "medium",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "publish_qualified",
            "research_notes": "Consulting is preserved as a professional affiliation and not assumed to be salaried employment or the immediate OSS predecessor.",
        },
        {
            "key": "leif-tronstad-norsk-aluminium-b966",
            "person_id": PEOPLE[30][0],
            "organization_key": "norsk-aluminium-company",
            "organization_name_as_found": "Norsk Aluminium Co.",
            "role_title": "permanent consultant",
            "occupation": "corrosion-research consultant",
            "relationship_type": "professional_affiliation",
            "start_date": "1934",
            "end_date": "1940",
            "date_precision": "NBL states that he became a permanent consultant in 1934; 1940 marks the prewar research boundary rather than a documented termination.",
            "country": "Norway",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "probable",
            "claim_confidence": "medium",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "publish_qualified",
            "research_notes": "The consulting role is explicit, but the indexed identity remains probable and the relationship is not promoted to a named employer claim.",
        },
    ]


def claim(
    row: int,
    key: str,
    claim_type: str,
    claim_text: str,
    evidence_paraphrase: str,
    identity: str,
    temporal: str,
    source_quality: str,
    confidence: str,
    source_links: list[dict[str, object]],
    notes: str,
    affiliation_key: str | None = None,
    publication_status: str | None = None,
) -> dict[str, object]:
    return {
        "key": key,
        "person_id": PEOPLE[row][0],
        "affiliation_key": affiliation_key,
        "claim_type": claim_type,
        "claim_text": claim_text,
        "evidence_paraphrase": evidence_paraphrase,
        "identity_match_assessment": identity,
        "temporal_assessment": temporal,
        "source_quality": source_quality,
        "claim_confidence": confidence,
        "publication_status": publication_status
        or ("published" if confidence in {"confirmed", "high"} else "publish_qualified"),
        "match_notes": notes,
        "sources": source_links,
    }


def army_claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for item in ARMY_OCCUPATIONS:
        row = int(item["row"])
        name = PEOPLE[row][1]
        values.append(
            claim(
                row,
                f"identity-{slug(name)}-army-b966",
                "identity",
                f"Indexed {name} is a high-confidence match to the reviewed official Army entry.",
                "A nonshared protected identifier connects the visually verified index row to an official Army row carrying the exact full indexed name.",
                "High confidence from exact protected-identifier agreement plus exact full-name agreement.",
                "Identity evidence only; the Army entry does not establish an OSS transfer date or later wartime grade.",
                "A_direct_official",
                "high",
                [
                    {"source_key": INDEX, "locator_override": f"PDF page 473 row {row}; protected identifier withheld"},
                    {"source_key": ARMY, "locator_override": "Accepted reviewed identity bridge; protected identifier withheld"},
                ],
                "The review accepts identity only for this source row and exposes neither the protected identifier nor the raw Army record.",
            )
        )
        category = str(item["occupation"])
        values.append(
            claim(
                row,
                f"occupation-{slug(name)}-army-b966",
                "occupation",
                f"At Army entry on {item['date']}, the record coded {name}'s civilian status as {category}.",
                f"The official Army row contains civilian-status code {item['code']}; NARA's historical code list expands it to {category}.",
                "High-confidence identity from the accepted protected-identifier bridge and exact full-name agreement.",
                "The code is date-bounded at Army entry but identifies no employer, workplace, school or immediate OSS predecessor.",
                "A_direct_official",
                "medium",
                [
                    {"source_key": ARMY, "locator_override": f"Accepted identity row; civilian-status code {item['code']}; protected identifier withheld"},
                    {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46; Army-entry-date and civilian-occupation fields"},
                    {"source_key": CODES, "locator_override": str(item["locator"]), "excerpt_override": category},
                ],
                "The category is published as qualified occupation or student evidence and excluded from named-employer analytics.",
                f"{slug(name)}-occupation-b966",
                "publish_qualified",
            )
        )
    return values


def specialist_claims() -> list[dict[str, object]]:
    return [
        claim(
            25,
            "identity-frank-trojohak-army-b966",
            "identity",
            "Indexed Frank Trojohak is a high-confidence match to the official Army row printed as Frank Trojchak.",
            "A nonshared protected identifier agrees exactly; the surnames differ by one internal character, and both spellings are retained.",
            "High confidence from unique protected-identifier agreement and a narrowly compatible surname transcription variant; manual review remains required.",
            "The Army row is dated after OSS disbandment, so its grade, occupation code and date are not used as pre-OSS evidence.",
            "A_direct_official",
            "high",
            [
                {"source_key": INDEX, "locator_override": "PDF page 473 row 25; Frank Trojohak; protected identifier withheld"},
                {"source_key": ARMY, "locator_override": "Accepted Frank Trojchak identity candidate; protected identifier withheld"},
            ],
            "The spelling discrepancy remains visible and no post-OSS biographical field is projected backward.",
        ),
        claim(
            28,
            "identity-ferruccio-trombetti-b966",
            "identity",
            "Indexed Ferruccio Trombetti is a high-confidence match to the Italian Resistance organizer selected by OSS for Operation Appomatox.",
            "The institutional Resistance history supplies the rare exact name, birthplace, military and partisan chronology, OSS selection and Appomatox command.",
            "High confidence from the rare exact name plus detailed, direct OSS-operation chronology in a reputable Resistance-history publication.",
            "The source explicitly orders Army service, Resistance organizing, OSS selection and the August 1944 parachute mission.",
            "C_reputable_contemporary_or_scholarly",
            "high",
            [
                {"source_key": INDEX, "locator_override": "PDF page 473 row 28; Box 786"},
                {"source_key": TROMBETTI_ANPI, "locator_override": "Printed pages 14-15", "excerpt_override": "Operazione Appomatox… affidata ad un responsabile, il bolognese Ferruccio Trombetti"},
            ],
            "No famous-name substitution is required: the source itself links the exact person to OSS.",
        ),
        claim(
            28,
            "immediate-ferruccio-trombetti-resistance-b966",
            "immediate_pre_oss_affiliation",
            "Ferruccio Trombetti's immediate pre-OSS status was partisan and Resistance organizer in Lazio.",
            "The account says he organized Resistance activity through Rome's liberation and was then recommended to and selected by OSS for Operation Appomatox.",
            "High-confidence exact-name OSS identity from the same detailed institutional history.",
            "Explicit immediate: the source directly sequences Resistance organizing, Rome's liberation, OSS selection and mission training.",
            "C_reputable_contemporary_or_scholarly",
            "high",
            [{"source_key": TROMBETTI_ANPI, "locator_override": "Printed page 14; paragraphs on Lazio Resistance and OSS selection"}],
            "The relationship is modeled as volunteer Resistance activity, not a civilian employer or formal commissioned rank.",
            "ferruccio-trombetti-resistance-b966",
        ),
        claim(
            28,
            "prewar-ferruccio-trombetti-hemp-worker-b966",
            "occupation",
            "Before compulsory military service, Ferruccio Trombetti worked as a hemp worker.",
            "The biographical caption identifies his farming-family background, vocational schooling and hemp work before the 1937 military call-up.",
            "High-confidence identity from the rare exact name and direct OSS-operation chronology.",
            "Documented prewar occupation; no employer is named and it was not the immediate predecessor to OSS.",
            "C_reputable_contemporary_or_scholarly",
            "medium",
            [{"source_key": TROMBETTI_ANPI, "locator_override": "Printed page 14; biographical caption", "excerpt_override": "Di famiglia contadina… poi operaio canapino"}],
            "The occupation remains separate from any named employer claim.",
            "ferruccio-trombetti-hemp-worker-b966",
            "publish_qualified",
        ),
        claim(
            28,
            "prewar-ferruccio-trombetti-italian-army-b966",
            "other_pre_oss_affiliation",
            "Ferruccio Trombetti served as an Italian conscript in Spain and later in the Royal Italian Army's 2nd Grenadier Regiment before entering the Resistance.",
            "The history dates Spain service to 1937-1939, continued Army retention, later Yugoslavia service and September 1943 fighting in Rome.",
            "High-confidence identity from the rare exact name and direct OSS-operation chronology.",
            "Documented earlier military affiliation; the later Resistance status, not this Army assignment, immediately preceded OSS selection.",
            "C_reputable_contemporary_or_scholarly",
            "medium",
            [{"source_key": TROMBETTI_ANPI, "locator_override": "Printed page 14; military chronology"}],
            "The source describes conscription and does not support commissioned-officer status.",
            "ferruccio-trombetti-italian-army-b966",
            "publish_qualified",
        ),
        claim(
            29,
            "identity-inge-trondsen-b966",
            "identity",
            "Indexed Inge Trondsen is confirmed as the Norwegian naval sub-lieutenant commended in an original OSS award record.",
            "An original OSS sheet supplies the exact name and sub-lieutenant rank; a Norwegian institutional register independently supplies the same name, nationality, Navy rank and wartime chronology.",
            "Confirmed by an exact-name original OSS record and an independent institutional service register with matching nationality and rank.",
            "The sources document wartime Navy service and clandestine operations but not a formal transfer into U.S. OSS employment.",
            "A_direct_official",
            "confirmed",
            [
                {"source_key": INDEX, "locator_override": "PDF page 473 row 29; Box 786"},
                {"source_key": TRONDSEN_NARA, "locator_override": "PDF physical page 114, printed page 75", "excerpt_override": "Sub-Lt Inge Trondsen, RN"},
                {"source_key": TRONDSEN_KRIGSSEILER, "locator_override": "Opplysninger tab; Norwegian Navy service and ranks"},
            ],
            "The recommendation text aligned with Trondsen's row is kept distinct from the adjacent Jens Nordlie entry.",
        ),
        claim(
            29,
            "immediate-inge-trondsen-navy-b966",
            "immediate_pre_oss_affiliation",
            "Inge Trondsen's best-supported affiliation during his OSS cooperation was commissioned service in the Royal Norwegian Navy.",
            "The maritime register says he entered the Navy radio course in September 1940 and served for the rest of the war; the OSS sheet calls him a sub-lieutenant and clandestine sub-chaser captain.",
            "Confirmed exact-name identity from original OSS and independent Norwegian institutional records.",
            "Probable immediate: continuous Navy service overlaps the documented OSS operation, but no transfer order was found.",
            "A_direct_official",
            "medium",
            [
                {"source_key": TRONDSEN_NARA, "locator_override": "PDF physical page 114, printed page 75; Trondsen row", "excerpt_override": "Captain of US sub-chaser operating clandestinely into Norway"},
                {"source_key": TRONDSEN_KRIGSSEILER, "locator_override": "Opplysninger tab; accepted to Navy radio course 3 September 1940"},
            ],
            "Published as a qualified ongoing Allied military affiliation, not a civilian employer.",
            "inge-trondsen-navy-b966",
            "publish_qualified",
        ),
        claim(
            29,
            "occupation-inge-trondsen-thalatta-b966",
            "occupation",
            "Immediately before Norwegian Navy training, Inge Trondsen served as fourth mate aboard M/S Thalatta.",
            "The institutional muster lists fourth-mate service from 12 January to 1 August 1940; the Navy radio-course acceptance followed on 3 September.",
            "Confirmed identity from original OSS and independent institutional service records.",
            "Strongly date-bounded before military service, but the employing company and any August-September intervening status are not named.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": TRONDSEN_KRIGSSEILER, "locator_override": "Mønstringer tab; M/S Thalatta row"}],
            "The vessel is not presented as his employer, and the claim is excluded from named-employer analytics.",
            "inge-trondsen-thalatta-b966",
        ),
        claim(
            30,
            "identity-leif-tronstad-b966",
            "identity",
            "The indexed Lief Trondstad is a probable match to Norwegian chemist and wartime major Leif Hans Larsen Tronstad.",
            "Independent Norwegian institutional biographies supply the distinctive near-match name, NTH professorship, resistance work and Norwegian High Command major rank.",
            "Probable only: the index transposes the given-name vowels and adds a surname letter, while no independent OSS, Box 786 or protected-identifier bridge was found.",
            "The biographies establish prewar and wartime chronology for Leif Tronstad but not his administrative relationship to the OSS index file.",
            "B_authoritative_institutional",
            "medium",
            [
                {"source_key": INDEX, "locator_override": "PDF page 473 row 30; indexed as Lief Trondstad"},
                {"source_key": TRONSTAD_NBL, "locator_override": "Career and wartime chronology"},
                {"source_key": TRONSTAD_FFI, "locator_override": "Fact sheet page 1; biography and major rank"},
            ],
            "Both index and biographical spellings remain visible; the profile requires Box 786 review before identity can be promoted.",
            publication_status="publish_qualified",
        ),
        claim(
            30,
            "last-civilian-leif-tronstad-nth-b966",
            "last_civilian_pre_service",
            "If the probable identity is correct, Leif Tronstad's last civilian employer before wartime service was the Norwegian Institute of Technology, where he was a chemistry professor and institute head.",
            "NBL dates his academic appointments; FFI states that he still held the full professorship when Germany invaded in April 1940.",
            "Probable index identity only; the employer and chronology are authoritative for Leif Tronstad himself.",
            "Strongly date-bounded: the professorship continued to the April 1940 invasion and his immediate military and resistance activity.",
            "B_authoritative_institutional",
            "medium",
            [
                {"source_key": TRONSTAD_NBL, "locator_override": "Paragraph on NTH appointments from 1931 through the 1936 professorship"},
                {"source_key": TRONSTAD_FFI, "locator_override": "Fact sheet page 1", "excerpt_override": "a full professorship at NTH, a position he still held when Germany invaded"},
            ],
            "The claim remains visibly qualified and is excluded from confirmed/high default employer analytics.",
            "leif-tronstad-nth-b966",
            "publish_qualified",
        ),
        claim(
            30,
            "prewar-leif-tronstad-hydro-b966",
            "other_pre_oss_affiliation",
            "If the probable identity is correct, Leif Tronstad was a Norsk Hydro consultant on heavy-water production from 1934.",
            "NBL explicitly dates the consulting relationship to 1934; NTNU independently describes his prewar consulting work on the Vemork heavy-water plant.",
            "Probable index identity only; the consulting relationship is well documented for Leif Tronstad himself.",
            "Documented prewar affiliation, but neither salaried employment nor immediate OSS precedence is established.",
            "B_authoritative_institutional",
            "medium",
            [
                {"source_key": TRONSTAD_NBL, "locator_override": "Paragraph on Norsk Hydro heavy-water consulting from 1934"},
                {"source_key": TRONSTAD_NTNU, "support_type": "context_only", "locator_override": "Biographical section on prewar Norsk Hydro consulting"},
            ],
            "Modeled as professional affiliation rather than a named employer.",
            "leif-tronstad-hydro-b966",
            "publish_qualified",
        ),
        claim(
            30,
            "prewar-leif-tronstad-norsk-aluminium-b966",
            "other_pre_oss_affiliation",
            "If the probable identity is correct, Leif Tronstad became a permanent consultant to Norsk Aluminium Company in 1934.",
            "NBL explicitly links his corrosion research reputation to the permanent consulting appointment.",
            "Probable index identity only; the consulting relationship is authoritative for Leif Tronstad himself.",
            "Documented prewar affiliation; the exact contract form and its relation to any OSS service are unresolved.",
            "B_authoritative_institutional",
            "medium",
            [{"source_key": TRONSTAD_NBL, "locator_override": "Paragraph on Norsk Aluminium Co. consulting from 1934"}],
            "Modeled as professional affiliation rather than a named employer.",
            "leif-tronstad-norsk-aluminium-b966",
            "publish_qualified",
        ),
    ]


def claims() -> list[dict[str, object]]:
    return army_claims() + specialist_claims()


def unresolved_update(row: int, reason: str) -> dict[str, object]:
    person_id, name = PEOPLE[row]
    return {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, Box 786 and archive location 230/86/42/03. {reason}",
        "personnel_category": "unknown_or_indeterminate",
        "commissioned_officer": None,
        "allied_or_foreign_personnel": False,
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": "Review Box 786 for corroborating identifiers, immediate pre-OSS affiliation and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }


def army_update(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    person_id, name = PEOPLE[row]
    relationship = "student status" if row == 46 else "historical civilian occupation"
    return {
        "person_id": person_id,
        "identity_status": "high_confidence",
        "identity_evidence": f"A nonshared protected identifier and exact full-name agreement connect the visually verified {name} index row to the reviewed official Army row.",
        "personnel_category": "enlisted_army_personnel",
        "commissioned_officer": False,
        "allied_or_foreign_personnel": False,
        "manual_review_required": True,
        "research_status": "occupation_only_found",
        "next_action": f"Review Box 786 to establish the immediate pre-OSS affiliation, wartime grade and named last civilian employer; do not convert the Army {relationship} category into a workplace.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }


def person_updates() -> list[dict[str, object]]:
    values = [unresolved_update(row, reason) for row, reason in UNRESOLVED.items()]
    values.extend(army_update(item) for item in ARMY_OCCUPATIONS)
    values.extend(
        [
            {
                "person_id": PEOPLE[25][0],
                "identity_status": "high_confidence",
                "identity_evidence": "A nonshared protected identifier connects the index's Frank Trojohak to an official Army row printed as Frank Trojchak. The one-character surname discrepancy remains visible and requires file review.",
                "name_variants": ["Frank Trojchak"],
                "personnel_category": "unknown_or_indeterminate",
                "commissioned_officer": None,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Review Box 786 and an original service record to confirm the surname spelling and pre-OSS status. The post-OSS-dated Army grade and occupation code are withheld from pre-OSS claims.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[28][0],
                "identity_status": "high_confidence",
                "identity_evidence": "A reputable institutional Resistance history supplies the rare exact name, birthplace, Army and partisan chronology, direct OSS selection and leadership of Operation Appomatox.",
                "name_variants": ["Ferruccio Michelangeli"],
                "personnel_category": "foreign_or_allied_military_personnel",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": True,
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Review Box 786 and the cited Appomatox archival materials to confirm administrative OSS status and identify any named civilian employer before conscription.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[29][0],
                "identity_status": "confirmed",
                "identity_evidence": "An original OSS award sheet identifies Sub-Lieutenant Inge Trondsen by exact name and rank, while an independent Norwegian institutional register supplies matching Navy rank, nationality and wartime chronology.",
                "personnel_category": "foreign_or_allied_military_personnel",
                "commissioned_officer": True,
                "allied_or_foreign_personnel": True,
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Review Box 786 and TNA HS 9/1486/3 for the exact OSS relationship, employing company for M/S Thalatta and any affiliation between the August 1940 muster end and September Navy course.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[30][0],
                "identity_status": "probable",
                "identity_evidence": "Independent Norwegian institutional biographies document the distinctive Leif Tronstad name, NTH professorship, consulting work, resistance service and major rank, but no independent OSS or protected-identifier bridge resolves the index spellings Lief Trondstad.",
                "name_variants": ["Leif Tronstad", "Leif Hans Larsen Tronstad"],
                "personnel_category": "foreign_or_allied_military_personnel",
                "commissioned_officer": True,
                "allied_or_foreign_personnel": True,
                "manual_review_required": True,
                "research_status": "documented_prewar_employer_found",
                "next_action": "Review Box 786 to confirm the spelling-variant identity and OSS relationship. Preserve NTH as a qualified last civilian employer and the two consulting roles as separate professional affiliations.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
        ]
    )
    return values


def research_attempts() -> list[dict[str, object]]:
    army_rows = {int(item["row"]) for item in ARMY_OCCUPATIONS}
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        if row in army_rows:
            outcome, reviewed, rejected = "source_reviewed", 4, 4
            detail = "Accepted an exact full-name, nonshared protected-identifier Army bridge and verified the dated historical civilian-status category against NARA technical documentation."
        elif row == 25:
            outcome, reviewed, rejected = "source_reviewed", 2, 6
            detail = "Accepted a narrowly compatible one-character surname variant because the private identifier is exact and nonshared; post-OSS-dated Army fields were not used as pre-OSS evidence."
        elif row == 28:
            outcome, reviewed, rejected = "source_reviewed", 2, 5
            detail = "A reputable institutional Resistance history directly documented the rare exact-name OSS identity, immediate partisan pathway, earlier Army service and hemp-work occupation."
        elif row == 29:
            outcome, reviewed, rejected = "source_reviewed", 3, 4
            detail = "An original OSS award record and an independent Norwegian maritime register confirmed identity, Navy rank, clandestine naval command and dated fourth-mate service."
        elif row == 30:
            outcome, reviewed, rejected = "source_reviewed", 4, 5
            detail = "Three Norwegian institutional biographies support a probable spelling-variant identity, NTH employment and two consulting affiliations, but no independent OSS bridge was found."
        else:
            outcome, reviewed, rejected = "no_result", 7, 6
            detail = UNRESOLVED[row]
        attempts.append(
            {
                "key": f"page473-row{row}-{slug(name)}-b966",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index and official Archives context; CIA Reading Room or equivalent official-source check; exact-name and meaningful variants; OSS, Army, Navy and rank clues; employer and occupation 1940; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Box 786; protected identifiers used only when defensible",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_966",
                "started_at": "2026-10-30T03:40:00Z",
                "completed_at": "2026-10-30T05:10:00Z",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search snippets, unsourced genealogy, family references, people-finder pages, postwar-only leads and sources without an OSS, protected-identifier or Box-file bridge were rejected. A vessel, occupation category, student status, consultant relationship and later rank were not silently converted into employers or immediate affiliations.",
                "research_notes": f"{detail} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain, CIA Reading Room-equivalent and Library of Congress searches were checked as applicable. The index page, Army bulk file, technical documentation, occupation-code pages and cited original or institutional sources were inspected directly. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": "Review the indexed Box 786 personnel file for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before wartime service.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b966-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-966-v1",
        "reviewer": "Before OSS Batch 966 evidence review",
        "sources": sources(),
        "organizations": organizations(),
        "affiliations": [army_affiliation(item) for item in ARMY_OCCUPATIONS]
        + specialist_affiliations(),
        "claims": claims(),
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }
    EvidenceBundle.model_validate(bundle)
    OUTPUT.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
