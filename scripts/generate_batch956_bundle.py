#!/usr/bin/env python3
"""Generate the reviewed Batch 956 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page468-francis-e-tifft-to-paul-tinken-"
    "review_batch-956_2026-10-29.json"
)

INDEX = "nara-index-b956"
ARMY = "army-bulk-b956"
TECH = "army-tech-b956"
CODES = "army-codes-b956"
GOODFELLOW = "goodfellow-board-b956"
NARA_STOCKHOLM = "nara-entry210-tikander-b956"
SNL_OSS = "snl-oss-tikander-b956"
DOJ_TOBACCO = "doj-tobacco-tikander-b956"
LEX_TILLISCH = "lex-tillisch-b956"
ARSOF_TILLY = "arsof-tilly-b956"
AFSA_TIHANY = "afsa-tihany-b956"
CAMBRIDGE_TIHANY = "cambridge-tihany-b956"
YOUNG_COUNTY = "young-county-timmons-b956"

DOJ_ORG = "doj-existing-b956"
US_ARMY_ORG = "us-army-existing-b956"
ARTEX_ORG = "artex-spraying-b956"
ROYAL_DANISH_ARMY_ORG = "royal-danish-army-b956"
DANISH_INTEL_ORG = "danish-military-intelligence-b956"

PEOPLE = {
    24: ("a0bd0a5a-c84a-583d-8c32-70f0d70ff0f5", "Francis E Tifft"),
    25: ("41e97d7c-2565-5045-a44e-106b7a50adf3", "Howard Tige"),
    26: ("0f8a3234-6350-5a2e-9267-5c694628432d", "Leslie C Tihany"),
    27: ("7d0c43ba-dbfa-58d2-ad26-3ff193f4713a", "Wilho Tikander"),
    28: ("1a7e8ce1-0cf5-5ebc-bf40-6ba680014bff", "Ellen Tilden"),
    29: ("d0598d0d-cd23-5ded-a0a2-1743c0c40086", "Fred F Tilden"),
    30: ("874180b1-ff6b-5554-9504-7d2fc87af7de", "Maurice Tillier"),
    31: ("8ce0b528-2f00-58cd-bf2e-6060a4c9c7fe", "Fritz G Tillisch"),
    32: ("31cbce2f-6538-5d21-9cb4-e3f891f11fc3", "David E Tillquist"),
    33: ("558046a4-244c-5692-b0ab-c50b1ebb18b9", "James L Tilly"),
    34: ("f450b8cf-d969-5276-99a1-fb75826843bc", "John T Timlin"),
    35: ("f2bd8f15-de2a-5220-9d22-866dfee20e50", "Eric W Timm"),
    36: ("3297f5e3-76fc-5d8d-81a0-ede4cbfbc1ed", "Otwell D Timmons"),
    37: ("188c1274-dce6-566a-90f4-59e272ed5cee", "Robert H Timmons"),
    38: ("d36d2d6f-02da-54e3-a648-bf17fd4d8d63", "Robert N Timmons"),
    39: ("d35174b0-5825-50f9-9d72-69270948de36", "Louis Timpanaro"),
    40: ("b2662fec-7f07-5a20-bb29-f1fdfc623a83", "Richard W Tims"),
    41: ("7251b2e3-58ce-548f-ac74-bccbc72fa0b2", "Richard Tims"),
    42: ("c2e53f26-0638-5ec9-80ee-af9d295e7505", "Charles P Tindall"),
    43: ("6eccefb8-1664-5c28-b4ab-c522e10e6e70", "Francis S Tindall"),
    44: ("f34c8b9d-f960-58a8-8c01-9db8c47a65c9", "Edgar J Tingle"),
    45: ("a8818ca9-a414-56d9-a1c0-e73e5dbca13b", "Joseph Tinkelman"),
    46: ("f6677edd-4954-5f08-8ebf-f07a88165a1d", "Paul Tinken"),
}

# The technical documentation defines the six-character Army entry date as
# DD/MM/YY. The categories describe status or occupation at Army entry; they
# do not name an employer or establish an immediate OSS predecessor.
ARMY_CATEGORIES = {
    24: ("1944-11-10", "Chauffeurs and drivers, bus, taxi, truck, and tractor", "7-36", 174, "employment"),
    40: ("1943-03-20", "Semiprofessional occupations, n.e.c.", "0-68", 171, "employment"),
    42: ("1942-11-16", "Students", "9-92", 304, "student"),
    45: ("1943-03-16", "Students", "9-92", 304, "student"),
}

UNRESOLVED = {
    25: "The printed '? Move' note was preserved. Exact-name, variant, official-domain, obituary, directory and institutional searches produced no defensible Box 777 identity bridge.",
    28: "Exact-name, OSS, employer, obituary, newspaper, directory and institutional searches produced no defensible Box 778 identity bridge.",
    29: "Exact-name and middle-initial searches produced namesakes but no second identifier, wartime chronology or Box 778 bridge.",
    30: "Exact-name and French-language variants produced no reliable OSS, occupation or Box 778 identity bridge.",
    32: "Exact-name, middle-initial, military, obituary, directory and institutional searches produced no defensible Box 778 identity bridge.",
    34: "The common name produced military and obituary namesakes, none with two corroborating identifiers beyond the name or a Box 778 bridge.",
    35: "Exact-name and initials searches produced modern namesakes but no reliable wartime, OSS or Box 778 identity bridge.",
    37: "The only protected-identifier Army candidate names Robert N Timmons rather than indexed Robert H Timmons. The substantive middle-initial conflict was rejected and no facts were transferred.",
    38: "A Robert N Timmons Army record was linked by a different indexed row's protected identifier; it was not reassigned to this unnumbered namesake. No independent Box 778 bridge was found.",
    41: "Exact-name, officer-number, military, obituary and institutional searches produced no defensible Box 779 identity bridge.",
    43: "Exact-name, middle-initial, obituary, directory and institutional searches produced no defensible Box 779 identity bridge.",
    44: "A postwar Small Business Administration contributor has the same name, but the source does not bridge him to Box 779 or establish a pre-OSS affiliation.",
    46: "Exact-name and spelling-variant searches produced no reliable OSS, employer, military or Box 779 identity bridge.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def archive_box(row: int) -> str:
    if row == 25:
        return "777"
    if row <= 39:
        return "778"
    return "779"


def archive_location(row: int) -> str:
    return "230/86/42/01" if row == 25 else "230/86/42/02"


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 777-779",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 468, rows 24-46; checked against layout-preserving text and a 220 dpi page render",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate; the Howard Tige '? Move' note is preserved and full protected identifiers remain private.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; six Batch 956 candidates reviewed; identifiers withheld",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "Five identity leads were accepted and one middle-initial conflict was rejected. No raw bulk row or full protected identifier enters public assets.",
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
            "rights_notes": "Used to interpret selected fields only; source damage, coding limits and incomplete coverage remain applicable.",
        },
        {
            "key": CODES,
            "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1CL_SD.pdf",
            "archival_identifier": "National Archives Identifier 1263923; Code No. 30",
            "title": "NARA Compiled Code Lists for the Electronic Army Serial Number Merged File",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives at College Park - Electronic Records",
            "publication_record_date": "2011-01-12; modified 2011-03-17",
            "locator": "PDF physical pages 171, 174 and 304; four reviewed historical categories",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical categories are qualified and never converted into named employers, workplaces or exact modern job titles.",
        },
        {
            "key": GOODFELLOW,
            "stable_url": "https://digitalcollections.hoover.org/internal/media/dispatcher/331531/full",
            "archival_identifier": "HIA-GOODFELLOW-4-A-9-4-4",
            "title": "Goodfellow Board examination of OSS personnel arriving from Palermo",
            "author_creator": "Office of Strategic Services Goodfellow Board",
            "repository_publisher": "Hoover Institution Library & Archives Digital Collections; declassified OSS record",
            "publication_record_date": "1944-05-22; approved for release 2005-05-03",
            "locator": "PDF physical pages 2-3, section III, Cpl. Louis Timpanaro",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "Goodfellow papers / declassified Office of Strategic Services records",
            "document_number": "HIA-GOODFELLOW-4-A-9-4-4",
            "rights_notes": "Only a short excerpt, citation metadata and project-authored paraphrase are retained; the full document is not republished.",
        },
        {
            "key": NARA_STOCKHOLM,
            "stable_url": "https://www.archives.gov/iwg/declassified-records/rg-226-oss/entry-210.pdf",
            "archival_identifier": "RG 226, Entry 210, WN#13386",
            "title": "Records of the Office of Strategic Services (Record Group 226), Entry 210",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010 inventory of 1940-1946 records",
            "locator": "PDF physical page 98; memos on OSS Stockholm operations by Wilho Tikander",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "document_number": "WN#13386",
            "rights_notes": "Inventory metadata is retained; underlying record content is not cached or republished.",
        },
        {
            "key": SNL_OSS,
            "stable_url": "https://snl.no/OSS",
            "title": "OSS",
            "author_creator": "Tore Pryser",
            "repository_publisher": "Store norske leksikon",
            "publication_record_date": "accessed 2026-10-29",
            "locator": "Section on the Stockholm office; Wilho Tikander paragraph",
            "access_date": "2026-10-29",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Store norske leksikon",
            "rights_notes": "A short excerpt and project-authored paraphrase are retained; no complete copyrighted page is republished.",
        },
        {
            "key": DOJ_TOBACCO,
            "stable_url": "https://appliedantitrust.com/06_conspiracy/00_classic_cases/01_am_tobacco/american_tobcco_edky_information7_24_1940.pdf",
            "archival_identifier": "U.S. District Court, Eastern District of Kentucky, Criminal No. 6670",
            "title": "United States of America v. The American Tobacco Company et al.: Information",
            "author_creator": "United States Department of Justice",
            "repository_publisher": "U.S. Government Printing Office; public scan hosted by Applied Antitrust Law",
            "publication_record_date": "1940-07-24",
            "locator": "PDF physical pages 1 and 16; Wilho Tikander listed among Special Attorneys",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "Historic federal antitrust case filings",
            "document_number": "Criminal No. 6670",
            "rights_notes": "The direct federal filing is cited as evidence of a point-in-time Justice Department assignment, not an inferred end date or immediate OSS transfer.",
        },
        {
            "key": LEX_TILLISCH,
            "stable_url": "https://biografiskleksikon.lex.dk/Frits_G._Tillisch",
            "title": "Frits G. Tillisch",
            "author_creator": "Hans Christian Bjerg and Merete Harding",
            "repository_publisher": "Dansk Biografisk Leksikon / Lex.dk",
            "publication_record_date": "last modified 2012-07-13",
            "locator": "Biographical chronology, paragraphs on Royal Life Guards and wartime military intelligence",
            "access_date": "2026-10-29",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Dansk Biografisk Leksikon",
            "rights_notes": "The article is authored in part by an emeritus senior archivist at the Danish National Archives; excerpts remain under 25 words.",
        },
        {
            "key": ARSOF_TILLY,
            "stable_url": "https://arsof-history.org/articles/v4n1_myitkyina_part_1_page_1.html",
            "title": "A Special Forces Model: OSS Detachment 101 in the Myitkyina Campaign, Part I",
            "author_creator": "Troy J. Sacquety, PhD",
            "repository_publisher": "U.S. Army Special Operations History Office",
            "publication_record_date": "2008",
            "locator": "Phase Two, photograph caption and March 1944 narrative naming LT James L. Tilly",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "Veritas, Vol. 4, No. 1",
            "rights_notes": "The article cites Tilly reports in NARA RG 226 and supports identity and commissioned status, not a pre-OSS employer.",
        },
        {
            "key": AFSA_TIHANY,
            "stable_url": "https://afsa.org/sites/default/files/fsj-1997-04-april_0.pdf",
            "title": "The Foreign Service Journal, April 1997: In Memory, Leslie C. Tihany",
            "author_creator": "American Foreign Service Association",
            "repository_publisher": "American Foreign Service Association",
            "publication_record_date": "1997-04",
            "locator": "PDF physical page 69 (printed page 55), Leslie C. Tihany obituary",
            "access_date": "2026-10-29",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "The Foreign Service Journal",
            "rights_notes": "Used for identity, education and U.S. Army chronology only; later career details are not treated as pre-OSS evidence.",
        },
        {
            "key": CAMBRIDGE_TIHANY,
            "stable_url": "https://www.cambridge.org/core/journals/language/article/abs/sanskrit-corayati-hungarian-csor/E28F2BB163DBEBC5AF383913A10061BC",
            "archival_identifier": "DOI 10.2307/408949",
            "title": "Sanskrit coráyati, Hungarian csór-",
            "author_creator": "Leslie C. Tihany",
            "repository_publisher": "Language / Linguistic Society of America; Cambridge University Press",
            "publication_record_date": "1940-06",
            "locator": "Language, volume 16, issue 2, pages 151-153",
            "access_date": "2026-10-29",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Language",
            "rights_notes": "Bibliographic metadata supports dated linguistic scholarship; it does not establish an employer or institutional appointment.",
        },
        {
            "key": YOUNG_COUNTY,
            "stable_url": "https://worldwartwoveterans.org/wp-content/uploads/2020/08/young-county-texas-wm.pdf",
            "title": "Men and Women in the Armed Forces from Young County",
            "author_creator": "Young County, Texas, American Legion posts and community contributors",
            "repository_publisher": "Contemporary Young County veterans memorial volume; public scan hosted by WorldWarTwoVeterans.org",
            "publication_record_date": "ca. 1946",
            "locator": "PDF physical page 60; entry for S/Sgt. Otwell D. Timmons",
            "access_date": "2026-10-29",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Young County World War II veterans memorial",
            "rights_notes": "The 65-page scan was text-extracted and the cited entry was visually checked against a rendered page. No image is republished.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": DOJ_ORG,
            "organization_id": "9e3f0482-04d1-5745-ac04-4ed0d5132090",
            "canonical_name": "U.S. Department of Justice",
            "historical_name": "United States Department of Justice",
            "aliases": ["Department of Justice", "DOJ"],
            "organization_type": "federal executive department",
            "sector": "federal_government",
            "country": "United States",
            "normalization_notes": "Existing canonical organization reused for a documented 1940 Special Attorney assignment.",
        },
        {
            "key": US_ARMY_ORG,
            "organization_id": "28a26f92-78af-5a1a-9c09-a843eb5975b4",
            "canonical_name": "United States Army",
            "historical_name": "Army of the United States",
            "aliases": ["U.S. Army", "Army"],
            "organization_type": "military service",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "Existing canonical organization reused; the contemporary source names the affiliation only as the Army.",
        },
        {
            "key": ARTEX_ORG,
            "canonical_name": "Artex Spraying Company",
            "historical_name": "Artex Spraying Company",
            "aliases": [],
            "organization_type": "industrial spraying and finishing company",
            "sector": "business_and_industry",
            "city": "New York",
            "state_or_region": "New York",
            "country": "United States",
            "active_dates": "Documented in 1942",
            "normalization_notes": "Historical name is preserved exactly. No modern successor, ownership relationship or expanded legal name has been inferred.",
        },
        {
            "key": ROYAL_DANISH_ARMY_ORG,
            "canonical_name": "Royal Danish Army",
            "historical_name": "Den Kongelige Livgarde / Hærens Gymnastikskole",
            "aliases": ["Danish Army", "Den Kongelige Livgarde", "Royal Life Guards"],
            "organization_type": "military service",
            "sector": "military",
            "country": "Denmark",
            "normalization_notes": "The broad Army organization is normalized separately while the two historically named postings remain in the as-found field.",
        },
        {
            "key": DANISH_INTEL_ORG,
            "canonical_name": "Danish Military Intelligence Service (wartime illegal service)",
            "historical_name": "den militære efterretningstjeneste",
            "aliases": ["Hærens Efterretningstjeneste", "illegal military intelligence service"],
            "organization_type": "wartime military intelligence service",
            "sector": "military",
            "country": "Denmark",
            "active_dates": "1943-1945",
            "normalization_notes": "This wartime clandestine service is kept separate from later Danish defense-intelligence organizations; no modern successor equivalence is asserted.",
        },
    ]


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (entry_date, category, code, _page, relationship) in ARMY_CATEGORIES.items():
        values.append(
            {
                "key": f"army-category-row{row}-b956",
                "person_id": PEOPLE[row][0],
                "occupation": category.lower(),
                "relationship_type": relationship,
                "end_date": entry_date,
                "date_precision": f"Historical category {code} was recorded at Army entry on {entry_date}; no employer, workplace, school or OSS-transfer date is named.",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "A_direct_official",
                "publication_status": "publish_qualified",
                "research_notes": "The historical category is not converted into a named employer, educational institution, workplace, exact specialization or immediate pre-OSS affiliation.",
            }
        )
    values.extend(
        [
            {
                "key": "linguist-leslie-tihany-b956",
                "person_id": PEOPLE[26][0],
                "occupation": "linguist and scholar",
                "relationship_type": "professional_affiliation",
                "end_date": "1940-06",
                "date_precision": "A named linguistics article was published in June 1940; an employer or institutional appointment is not identified.",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "publish_qualified",
                "research_notes": "Authorship and field are documented, but publication does not establish salaried employment, a workplace or the immediate predecessor to Army/OSS service.",
            },
            {
                "key": "doj-special-attorney-wilho-tikander-b956",
                "person_id": PEOPLE[27][0],
                "organization_key": DOJ_ORG,
                "organization_name_as_found": "United States Department of Justice",
                "role_title": "Special Attorney",
                "occupation": "attorney",
                "relationship_type": "government_assignment",
                "end_date": "1940-07-24",
                "date_precision": "Named in a federal court filing dated 1940-07-24; beginning and end dates are not established.",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "confirmed",
                "claim_confidence": "high",
                "source_quality": "A_direct_official",
                "publication_status": "published",
                "research_notes": "The direct filing establishes a point-in-time Justice Department assignment. It does not prove this was the immediate OSS predecessor or the last civilian employer.",
            },
            {
                "key": "royal-danish-army-frits-tillisch-b956",
                "person_id": PEOPLE[31][0],
                "organization_key": ROYAL_DANISH_ARMY_ORG,
                "organization_name_as_found": "Den Kongelige Livgarde and Hærens Gymnastikskole",
                "role_title": "commissioned officer",
                "occupation": "army officer",
                "relationship_type": "military_assignment",
                "start_date": "1938",
                "end_date": "1943-08-29",
                "date_precision": "Commissioned in 1938; Royal Life Guards from 1939; Army Gymnastics School in 1942 through 1943-08-29.",
                "country": "Denmark",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "The biography documents military service before his underground intelligence work; the accessible sources do not establish an OSS entry date.",
            },
            {
                "key": "danish-intelligence-frits-tillisch-b956",
                "person_id": PEOPLE[31][0],
                "organization_key": DANISH_INTEL_ORG,
                "organization_name_as_found": "den militære efterretningstjeneste",
                "role_title": "chief, Central Jutland section",
                "occupation": "military intelligence officer",
                "relationship_type": "military_assignment",
                "start_date": "1943-11",
                "end_date": "1945-05",
                "date_precision": "Intelligence work from November 1943; section chief from 1944-05-09 until the end of the German occupation.",
                "city": "Aarhus",
                "country": "Denmark",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "temporal_relation_uncertain",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "publish_qualified",
                "research_notes": "The wartime assignment is explicit, but its sequence relative to any OSS personnel-file relationship is not established and is not labeled immediate pre-OSS.",
            },
            {
                "key": "us-army-otwell-timmons-b956",
                "person_id": PEOPLE[36][0],
                "organization_key": US_ARMY_ORG,
                "organization_name_as_found": "Army",
                "role_title": "staff sergeant",
                "occupation": "soldier",
                "relationship_type": "military_assignment",
                "start_date": "1936",
                "end_date": "1945",
                "date_precision": "The contemporary county memorial says he entered the Army in 1936 and was discharged in 1945; exact dates and units are not supplied.",
                "country": "United States",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "probable_immediate",
                "identity_confidence": "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "publish_qualified",
                "research_notes": "Continuous Army service makes the Army the best-supported broad immediate pathway, but the memorial does not name an OSS transfer date or specific immediately preceding unit.",
            },
            {
                "key": "artex-spraying-louis-timpanaro-b956",
                "person_id": PEOPLE[39][0],
                "organization_key": ARTEX_ORG,
                "organization_name_as_found": "Artex Spraying Company",
                "role_title": "auto and wood sprayer",
                "occupation": "spray painter",
                "relationship_type": "employment",
                "end_date": "1942-11-19",
                "date_precision": "The direct OSS examination states that he entered OSS on 1942-11-19 and names the job he held in New York immediately beforehand.",
                "city": "New York",
                "state_or_region": "New York",
                "country": "United States",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "explicit_immediate",
                "identity_confidence": "confirmed",
                "claim_confidence": "confirmed",
                "source_quality": "A_direct_official",
                "publication_status": "published",
                "research_notes": "A direct wartime OSS personnel examination supplies the entry date, employer and role; a protected identifier independently matches the index and Army bulk record.",
            },
        ]
    )
    return values


def army_claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (entry_date, category, code, page, _relationship) in ARMY_CATEGORIES.items():
        person_id, name = PEOPLE[row]
        values.append(
            {
                "key": f"identity-row{row}-army-b956",
                "person_id": person_id,
                "claim_type": "identity",
                "claim_text": f"The indexed {name} is a high-confidence match to the reviewed official Army record.",
                "evidence_paraphrase": "A nonshared protected identifier and exact name agreement connect the visually verified index row to the official Army record.",
                "identity_match_assessment": "High confidence from private nonshared identifier agreement and exact compatible name evidence.",
                "temporal_assessment": "The Army record dates entry into service but does not establish the exact OSS transfer date.",
                "source_quality": "A_direct_official",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "This identity decision does not establish a named employer or immediate OSS predecessor.",
                "sources": [
                    {"source_key": INDEX, "locator_override": f"PDF page 468 row {row}; Box {archive_box(row)}; protected identifier withheld"},
                    {"source_key": ARMY, "locator_override": "Reviewed name record; protected identifier withheld"},
                    {"source_key": TECH, "support_type": "context_only", "locator_override": "Field definitions and DD/MM/YY date format, PDF physical pages 44-46"},
                ],
            }
        )
        values.append(
            {
                "key": f"category-row{row}-army-b956",
                "person_id": person_id,
                "affiliation_key": f"army-category-row{row}-b956",
                "claim_type": "occupation",
                "claim_text": f"At Army entry on {entry_date}, {name} was recorded in the historical {category} category; no employer, workplace or institution is identified.",
                "evidence_excerpt": category,
                "evidence_paraphrase": f"The official bulk record supplies historical code {code}; the visually reviewed NARA code list expands it as {category}.",
                "identity_match_assessment": "High confidence from private nonshared identifier agreement and exact compatible name evidence.",
                "temporal_assessment": "Strongly date-bounded at Army entry, but not shown to be the immediate pre-OSS affiliation.",
                "source_quality": "A_direct_official",
                "claim_confidence": "medium",
                "publication_status": "publish_qualified",
                "match_notes": "Published only as a qualified historical category. No employer, workplace, school or exact modern specialization is inferred.",
                "sources": [
                    {"source_key": ARMY, "locator_override": f"Army entry {entry_date}; historical code {code}; protected identifier withheld"},
                    {"source_key": CODES, "locator_override": f"PDF physical page {page}; historical category {code}"},
                ],
            }
        )
    return values


def claims() -> list[dict[str, object]]:
    values = army_claims()
    values.extend(
        [
            {
                "key": "identity-leslie-tihany-b956",
                "person_id": PEOPLE[26][0],
                "claim_type": "identity",
                "claim_text": "The indexed Leslie C Tihany is a high-confidence match to the Hungarian-born U.S. Army veteran, linguist and later Foreign Service officer Leslie C. Tihany.",
                "evidence_excerpt": "Leslie C. Tihany, 85, a retired FSO, academician and Congregational minister",
                "evidence_paraphrase": "An institutional obituary and a named 1940 scholarly publication supply a distinctive exact-name chronology compatible with the index.",
                "identity_match_assessment": "High confidence from the distinctive exact full name, middle initial, U.S. Army service and dated scholarly record.",
                "temporal_assessment": "The sources place his linguistic scholarship before U.S. Army service, but do not establish an OSS entry date.",
                "source_quality": "B_authoritative_institutional",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "Identity is published; no specific faculty employer is assigned because the obituary does not date the listed appointments.",
                "sources": [
                    {"source_key": INDEX, "locator_override": "PDF page 468 row 26; Box 778"},
                    {"source_key": AFSA_TIHANY, "locator_override": "PDF physical page 69 (printed page 55), obituary paragraph"},
                    {"source_key": CAMBRIDGE_TIHANY, "support_type": "context_only", "locator_override": "Language 16:2, June 1940, pages 151-153"},
                ],
            },
            {
                "key": "occupation-leslie-tihany-b956",
                "person_id": PEOPLE[26][0],
                "affiliation_key": "linguist-leslie-tihany-b956",
                "claim_type": "occupation",
                "claim_text": "Leslie C. Tihany was publishing linguistic scholarship by June 1940; the reviewed sources do not identify his employer or prove this was his immediate pre-OSS role.",
                "evidence_excerpt": "Sanskrit coráyati, Hungarian csór-",
                "evidence_paraphrase": "The journal record names Tihany as author of a linguistics article published in June 1940.",
                "identity_match_assessment": "High confidence from the distinctive exact name, matching middle initial and institutional biographical record.",
                "temporal_assessment": "Explicitly dated prewar scholarship; employer and immediacy remain unknown.",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "claim_confidence": "high",
                "publication_status": "publish_qualified",
                "match_notes": "Published as documented prewar occupation/scholarship, not as employment by the journal, publisher or any university.",
                "sources": [
                    {"source_key": CAMBRIDGE_TIHANY, "locator_override": "Language 16:2, June 1940, pages 151-153"},
                    {"source_key": AFSA_TIHANY, "support_type": "context_only", "locator_override": "PDF physical page 69, identity and Army chronology"},
                ],
            },
            {
                "key": "identity-wilho-tikander-b956",
                "person_id": PEOPLE[27][0],
                "claim_type": "identity",
                "claim_text": "The indexed Wilho Tikander is confirmed as the Chicago attorney who became chief of OSS operations in Stockholm.",
                "evidence_excerpt": "WILHO TIKANDER, OSS Chief in Stockholm",
                "evidence_paraphrase": "The official NARA inventory explicitly identifies the distinctive exact-name person as OSS Chief in Stockholm.",
                "identity_match_assessment": "Confirmed by the distinctive exact name in both the personnel index and official OSS records inventory, reinforced by compatible legal chronology.",
                "temporal_assessment": "NARA documents his wartime OSS leadership; a separate 1940 filing documents earlier Justice Department work.",
                "source_quality": "A_direct_official",
                "claim_confidence": "confirmed",
                "publication_status": "published",
                "match_notes": "The identity bridge supports the earlier legal assignment but does not establish the exact OSS recruitment date.",
                "sources": [
                    {"source_key": INDEX, "locator_override": "PDF page 468 row 27; Box 778"},
                    {"source_key": NARA_STOCKHOLM, "locator_override": "PDF physical page 98; WN#13386"},
                    {"source_key": SNL_OSS, "support_type": "context_only", "locator_override": "Stockholm office paragraph"},
                ],
            },
            {
                "key": "doj-special-attorney-wilho-tikander-claim-b956",
                "person_id": PEOPLE[27][0],
                "affiliation_key": "doj-special-attorney-wilho-tikander-b956",
                "claim_type": "other_pre_oss_affiliation",
                "claim_text": "Wilho Tikander was serving as a Special Attorney for the U.S. Department of Justice in a federal antitrust case filed July 24, 1940.",
                "evidence_excerpt": "WILHO TIKANDER — Special Attorneys",
                "evidence_paraphrase": "The direct federal court filing lists Tikander among the Justice Department's Special Attorneys.",
                "identity_match_assessment": "Confirmed from the highly distinctive exact name and official NARA identification of the same Chicago attorney as OSS Stockholm chief.",
                "temporal_assessment": "Explicitly dated before OSS existed; no source reviewed proves it was the immediate predecessor or last civilian employer.",
                "source_quality": "A_direct_official",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "Published as a documented earlier government assignment, not as a proven immediate pre-OSS affiliation.",
                "sources": [
                    {"source_key": DOJ_TOBACCO, "locator_override": "PDF physical pages 1 and 16; filed 1940-07-24"},
                    {"source_key": NARA_STOCKHOLM, "support_type": "context_only", "locator_override": "PDF physical page 98; WN#13386"},
                ],
            },
            {
                "key": "identity-frits-tillisch-b956",
                "person_id": PEOPLE[31][0],
                "claim_type": "identity",
                "claim_text": "The indexed Fritz G Tillisch is a high-confidence match to Danish officer Frits Gustav Tillisch; Fritz is retained as the index spelling and Frits as a documented variant.",
                "evidence_excerpt": "Frits G. Tillisch, Frits Gustav Tillisch ... officer",
                "evidence_paraphrase": "The Danish biographical lexicon supplies the distinctive full name, middle initial, military chronology and wartime intelligence role.",
                "identity_match_assessment": "High confidence from the rare surname, matching middle initial, near-identical Frits/Fritz spelling and compatible Allied wartime intelligence context.",
                "temporal_assessment": "The biography dates his Army and Danish intelligence roles but does not establish an OSS personnel-file date.",
                "source_quality": "B_authoritative_institutional",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "The variant spelling is preserved transparently; no name correction overwrites the printed index form.",
                "sources": [
                    {"source_key": INDEX, "locator_override": "PDF page 468 row 31; Box 778; printed Fritz spelling"},
                    {"source_key": LEX_TILLISCH, "locator_override": "Opening biography and wartime chronology; Frits spelling"},
                ],
            },
            {
                "key": "royal-danish-army-frits-tillisch-claim-b956",
                "person_id": PEOPLE[31][0],
                "affiliation_key": "royal-danish-army-frits-tillisch-b956",
                "claim_type": "other_pre_oss_affiliation",
                "claim_text": "Frits G. Tillisch was a commissioned Danish Army officer, serving with the Royal Life Guards from 1939 and at the Army Gymnastics School in 1942-1943.",
                "evidence_excerpt": "Han kom 1939 til livgarden og var på Hærens gymnastik-skole 1942–29.8.1943.",
                "evidence_paraphrase": "The authoritative Danish biography dates his commission and named Army postings before his illegal military-intelligence work.",
                "identity_match_assessment": "High confidence from the distinctive name, documented spelling variant and detailed compatible wartime chronology.",
                "temporal_assessment": "Explicit prewar and early-war military service; the accessible sources do not prove its exact relation to an OSS personnel-file date.",
                "source_quality": "B_authoritative_institutional",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "Published as a documented earlier military affiliation, not a civilian employer or proven immediate OSS predecessor.",
                "sources": [{"source_key": LEX_TILLISCH, "locator_override": "Biographical chronology, paragraph 1"}],
            },
            {
                "key": "danish-intelligence-frits-tillisch-claim-b956",
                "person_id": PEOPLE[31][0],
                "affiliation_key": "danish-intelligence-frits-tillisch-b956",
                "claim_type": "other_pre_oss_affiliation",
                "claim_text": "From November 1943 Frits G. Tillisch worked in the clandestine Danish military intelligence service and became chief of its Central Jutland section on May 9, 1944.",
                "evidence_excerpt": "Fra nov. 1943 arbejdede T. med affotografering og bearbejdning af efterretningsrapporter",
                "evidence_paraphrase": "The biography documents his intelligence work, appointment and reporting network through the end of the German occupation.",
                "identity_match_assessment": "High confidence from the distinctive exact surname, middle initial, spelling variant and detailed military chronology.",
                "temporal_assessment": "The wartime assignment is explicit, but its sequence relative to an OSS personnel-file relationship remains uncertain.",
                "source_quality": "B_authoritative_institutional",
                "claim_confidence": "high",
                "publication_status": "publish_qualified",
                "match_notes": "Published with a temporal warning and excluded from default immediate-pre-OSS analytics.",
                "sources": [{"source_key": LEX_TILLISCH, "locator_override": "Biographical chronology, paragraphs 1-3"}],
            },
            {
                "key": "identity-james-tilly-b956",
                "person_id": PEOPLE[33][0],
                "claim_type": "identity",
                "claim_text": "The indexed James L Tilly is a high-confidence match to Lieutenant James L. Tilly of OSS Detachment 101 in Burma.",
                "evidence_excerpt": "LT James L. Tilly ... was the OSS advisor to Kachin leader Zing Tawng Naw",
                "evidence_paraphrase": "The U.S. Army Special Operations History Office names the exact full name and rank in a Detachment 101 role and cites Tilly's NARA RG 226 reports.",
                "identity_match_assessment": "High confidence from exact full name and middle initial, commissioned-officer context, OSS unit and underlying RG 226 citations.",
                "temporal_assessment": "The source places Tilly in OSS Detachment 101 in March 1944 but does not identify his pre-OSS employer or assignment.",
                "source_quality": "A_direct_official",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "Identity and commissioned Army status are published; pre-OSS affiliation remains unresolved pending Box 778 review.",
                "sources": [
                    {"source_key": INDEX, "locator_override": "PDF page 468 row 33; Box 778; protected officer identifier withheld"},
                    {"source_key": ARSOF_TILLY, "locator_override": "Phase Two, lines/caption naming LT James L. Tilly; notes cite RG 226"},
                ],
            },
            {
                "key": "identity-otwell-timmons-b956",
                "person_id": PEOPLE[36][0],
                "claim_type": "identity",
                "claim_text": "The indexed Otwell D Timmons is a high-confidence match to Staff Sergeant Otwell D. Timmons of Young County, Texas.",
                "evidence_excerpt": "S/Sgt. Otwell D. Timmons ... Entered Army, 1936",
                "evidence_paraphrase": "A contemporary county memorial gives the distinctive exact name, Army chronology, Young County origin and China-Burma-India service.",
                "identity_match_assessment": "High confidence from the rare exact full name, matching middle initial, continuous U.S. Army service and compatible China-Burma-India chronology.",
                "temporal_assessment": "The memorial dates Army service from 1936 to 1945 but does not name an OSS transfer.",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "The contemporary record is sufficient for a qualified broad Army pathway; the personnel file remains necessary for the exact OSS assignment.",
                "sources": [
                    {"source_key": INDEX, "locator_override": "PDF page 468 row 36; Box 778; protected identifier withheld"},
                    {"source_key": YOUNG_COUNTY, "locator_override": "PDF physical page 60; Otwell D. Timmons entry visually checked"},
                ],
            },
            {
                "key": "us-army-otwell-timmons-claim-b956",
                "person_id": PEOPLE[36][0],
                "affiliation_key": "us-army-otwell-timmons-b956",
                "claim_type": "immediate_pre_oss_affiliation",
                "claim_text": "Otwell D. Timmons served continuously in the U.S. Army from 1936 through 1945; this is the best-supported broad immediate pathway, although his pre-OSS unit and transfer date remain unverified.",
                "evidence_excerpt": "Entered Army, 1936 ... Served in Aleutians, China, Burma and India ... Discharged in 1945.",
                "evidence_paraphrase": "The contemporary county record documents uninterrupted Army service across the period in which the indexed OSS relationship occurred.",
                "identity_match_assessment": "High confidence from the rare exact full name, matching initial and compatible wartime geography.",
                "temporal_assessment": "Probable immediate affiliation at the broad service level; exact unit and OSS transfer sequence are not stated.",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "claim_confidence": "medium",
                "publication_status": "publish_qualified",
                "match_notes": "Shown as a qualified military pathway and excluded from last-civilian-employer counts.",
                "sources": [{"source_key": YOUNG_COUNTY, "locator_override": "PDF physical page 60; Otwell D. Timmons entry"}],
            },
            {
                "key": "identity-louis-timpanaro-b956",
                "person_id": PEOPLE[39][0],
                "claim_type": "identity",
                "claim_text": "The indexed Louis Timpanaro is confirmed as the corporal examined by the OSS Goodfellow Board in May 1944.",
                "evidence_excerpt": "Cpl. Louis Timpanaro",
                "evidence_paraphrase": "The direct OSS examination and the index share the exact name and a private nonshared identifier; the Army record independently agrees.",
                "identity_match_assessment": "Confirmed by exact private identifier agreement across the index and direct OSS document, exact name and compatible Army record.",
                "temporal_assessment": "The direct document states he entered OSS on 1942-11-19 and entered the Army through OSS on 1943-03-08.",
                "source_quality": "A_direct_official",
                "claim_confidence": "confirmed",
                "publication_status": "published",
                "match_notes": "The protected identifier is used privately for resolution and withheld from public text and exports.",
                "sources": [
                    {"source_key": INDEX, "locator_override": "PDF page 468 row 39; Box 778; protected identifier withheld"},
                    {"source_key": GOODFELLOW, "locator_override": "PDF physical pages 2-3, section III; protected identifier withheld"},
                    {"source_key": ARMY, "support_type": "context_only", "locator_override": "Reviewed name record and Army entry 1943-03-08; protected identifier withheld"},
                ],
            },
            {
                "key": "immediate-artex-louis-timpanaro-b956",
                "person_id": PEOPLE[39][0],
                "affiliation_key": "artex-spraying-louis-timpanaro-b956",
                "claim_type": "immediate_pre_oss_affiliation",
                "claim_text": "Immediately before entering OSS on November 19, 1942, Louis Timpanaro worked in New York as an auto and wood sprayer for Artex Spraying Company.",
                "evidence_excerpt": "where he was an auto and wood sprayer in the Artex Spraying Company",
                "evidence_paraphrase": "A direct wartime OSS personnel examination supplies his OSS entry date, employer, role and New York location in one chronological statement.",
                "identity_match_assessment": "Confirmed by exact private identifier agreement and exact name across the index and direct OSS record.",
                "temporal_assessment": "Explicit immediate predecessor: the source states the job and then the 1942-11-19 OSS entry date.",
                "source_quality": "A_direct_official",
                "claim_confidence": "confirmed",
                "publication_status": "published",
                "match_notes": "Published as immediate pre-OSS employment with the historical employer name preserved exactly.",
                "sources": [{"source_key": GOODFELLOW, "locator_override": "PDF physical pages 2-3, section III"}],
            },
            {
                "key": "last-civilian-artex-louis-timpanaro-b956",
                "person_id": PEOPLE[39][0],
                "affiliation_key": "artex-spraying-louis-timpanaro-b956",
                "claim_type": "last_civilian_pre_service",
                "claim_text": "Artex Spraying Company is the last documented civilian employer before Louis Timpanaro entered OSS and later entered the Army through OSS.",
                "evidence_excerpt": "He entered the Army 8 March 1943 through OSS",
                "evidence_paraphrase": "The direct record places Artex before OSS entry in November 1942 and Army entry through OSS in March 1943.",
                "identity_match_assessment": "Confirmed by exact private identifier and name agreement.",
                "temporal_assessment": "The source explicitly orders civilian employment, OSS entry and later Army entry.",
                "source_quality": "A_direct_official",
                "claim_confidence": "confirmed",
                "publication_status": "published",
                "match_notes": "This is counted in last-civilian-employer analytics as well as immediate-affiliation analytics, without duplicating the affiliation record.",
                "sources": [{"source_key": GOODFELLOW, "locator_override": "PDF physical pages 2-3, section III"}],
            },
        ]
    )
    return values


def archival_update(row: int, reason: str) -> dict[str, object]:
    person_id, name = PEOPLE[row]
    box = archive_box(row)
    return {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, Box {box} and archive location {archive_location(row)}. {reason}",
        "personnel_category": "unknown_or_indeterminate",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": f"Review Box {box} for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "critical" if row in {37, 38} else "high",
    }


def army_update(row: int) -> dict[str, object]:
    return {
        "person_id": PEOPLE[row][0],
        "identity_status": "high_confidence",
        "identity_evidence": "A nonshared protected identifier and exact compatible name connect the visually verified index row to the reviewed official Army record.",
        "personnel_category": "enlisted_army_personnel",
        "commissioned_officer": False,
        "allied_or_foreign_personnel": False,
        "manual_review_required": True,
        "research_status": "occupation_only_found",
        "next_action": f"Review Box {archive_box(row)} to establish the immediate pre-OSS affiliation and named last civilian employer; do not convert the Army category into a workplace or school.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }


def person_updates() -> list[dict[str, object]]:
    values = [archival_update(row, reason) for row, reason in UNRESOLVED.items()]
    values.extend(army_update(row) for row in ARMY_CATEGORIES)
    values.extend(
        [
            {
                "person_id": PEOPLE[26][0],
                "identity_status": "high_confidence",
                "identity_evidence": "The distinctive exact name and middle initial appear in the index, an institutional Foreign Service obituary, and dated scholarly publications; U.S. Army service supplies compatible wartime chronology.",
                "name_variants": ["Leslie C. Tihany", "Leslie Charles Tihany"],
                "personnel_category": "unknown_or_indeterminate",
                "manual_review_required": True,
                "research_status": "occupation_only_found",
                "next_action": "Review Box 778 to date U.S. Army and OSS service and identify any named immediate employer or academic appointment; do not infer an employer from publication or education.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[27][0],
                "identity_status": "confirmed",
                "identity_evidence": "The distinctive exact name is explicitly identified by NARA as OSS Chief in Stockholm; a 1940 federal court filing and authoritative institutional history supply compatible legal chronology.",
                "name_variants": ["Wilho Tikander"],
                "personnel_category": "civilian_professional_or_administrative_grade",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "completed",
                "next_action": "Review Box 778 and WN#13386 to establish the exact OSS recruitment date and whether any position intervened after the documented 1940 Justice Department assignment.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "nara_catalog_id": "WN#13386",
                "archival_review_priority": "medium",
            },
            {
                "person_id": PEOPLE[31][0],
                "identity_status": "high_confidence",
                "identity_evidence": "The rare surname, matching middle initial, documented Frits/Fritz variant and detailed Danish military-intelligence chronology support the indexed identity without overwriting the source spelling.",
                "name_variants": ["Frits G. Tillisch", "Frits Gustav Tillisch"],
                "personnel_category": "foreign_or_allied_military_personnel",
                "commissioned_officer": True,
                "allied_or_foreign_personnel": True,
                "manual_review_required": True,
                "research_status": "completed",
                "next_action": "Review Box 778 to establish how and when Tillisch's Danish service related to the OSS personnel file; the wartime intelligence assignment is not labeled immediate pre-OSS without that bridge.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "medium",
            },
            {
                "person_id": PEOPLE[33][0],
                "identity_status": "high_confidence",
                "identity_evidence": "The exact full name and middle initial, commissioned-officer context, OSS Detachment 101 role and NARA RG 226 report citations establish a strong identity bridge.",
                "name_variants": ["James L. Tilly", "Lieutenant James L. Tilly"],
                "personnel_category": "commissioned_army_officer",
                "commissioned_officer": True,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Review Box 778 for the Army unit, occupation or employer immediately before OSS Detachment 101; the accessible official history begins with his OSS role.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[36][0],
                "identity_status": "high_confidence",
                "identity_evidence": "The rare exact name and middle initial, continuous U.S. Army service and China-Burma-India chronology match the indexed wartime context.",
                "name_variants": ["Otwell D. Timmons", "Otwell Dudley Timmons"],
                "personnel_category": "enlisted_army_personnel",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "completed",
                "next_action": "Review Box 778 to establish the specific Army unit immediately preceding OSS assignment and any pre-1936 civilian employer; keep the broad Army pathway qualified until then.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[39][0],
                "identity_status": "confirmed",
                "identity_evidence": "A direct OSS personnel examination, the index and the official Army record agree in exact name and a private nonshared identifier.",
                "name_variants": ["Louis S Timpanaro", "Cpl. Louis Timpanaro"],
                "personnel_category": "enlisted_army_personnel",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "verified_employer_found",
                "next_action": "Review Box 778 for employment dates, company address and any additional pre-OSS roles; the direct May 1944 OSS examination already establishes Artex Spraying Company as immediate and last civilian employer.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "medium",
            },
        ]
    )
    return values


def research_attempts() -> list[dict[str, object]]:
    attempts: list[dict[str, object]] = []
    special = {
        26: ("source_reviewed", 10, 5, "An institutional obituary and dated scholarly publication establish identity, U.S. Army chronology and prewar linguistic work, but not a named employer or immediate predecessor."),
        27: ("source_reviewed", 12, 6, "NARA explicitly identifies Tikander as OSS Stockholm chief; a direct 1940 federal filing documents a Justice Department Special Attorney assignment, but the exact OSS recruitment sequence remains open."),
        31: ("source_reviewed", 10, 5, "An authoritative Danish biography establishes the Frits/Fritz variant, commissioned Army service and clandestine military-intelligence work; the OSS-file sequence is not established."),
        33: ("source_reviewed", 9, 6, "The U.S. Army Special Operations History Office establishes the exact-name lieutenant's OSS Detachment 101 identity and rank, but begins after his pre-OSS pathway."),
        36: ("source_reviewed", 9, 5, "A visually checked contemporary county veterans volume documents continuous Army service from 1936 to 1945 and CBI service, supporting a qualified broad Army pathway."),
        39: ("source_reviewed", 11, 4, "A direct May 1944 OSS personnel examination explicitly names Artex Spraying Company, the auto-and-wood-sprayer role and the 1942-11-19 OSS entry date; private identifier agreement confirms identity."),
    }
    for row in sorted(PEOPLE):
        person_id, name = PEOPLE[row]
        box = archive_box(row)
        if row in special:
            outcome, reviewed, rejected, detail = special[row]
        elif row in UNRESOLVED:
            outcome = "candidate_rejected" if row in {37, 38, 44} else "no_result"
            reviewed = 7
            rejected = 6
            detail = UNRESOLVED[row]
        elif row in ARMY_CATEGORIES:
            entry_date, category, _code, _page, _relationship = ARMY_CATEGORIES[row]
            outcome = "source_reviewed"
            reviewed = 8
            rejected = 5
            detail = f"An accepted protected-identifier Army bridge supports identity and a dated historical {category} category at Army entry on {entry_date}, without naming an employer or workplace."
        else:
            raise AssertionError(f"Missing Batch 956 outcome for row {row}")
        attempts.append(
            {
                "key": f"page468-row{row}-{slug(name)}-b956",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index and public Archives context; CIA Reading Room or equivalent official-source check; exact-name and meaningful variants; OSS and military clues; employer and occupation 1940; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Box {box}; protected identifiers used privately only when defensible",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_956",
                "started_at": "2026-10-29T18:45:00Z",
                "completed_at": "2026-10-29T20:30:00Z",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search snippets, unsourced genealogy, people-finder pages, modern records, postwar-only leads and sources without an OSS, protected-identifier or Box-file bridge were not assigned. Spelling variants were search aliases only. Differing protected identifiers and substantive name conflicts were rejected.",
                "research_notes": f"{detail} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain, CIA Reading Room-equivalent and Library of Congress searches were checked as applicable. The index page, Army technical documentation and occupation-code pages were inspected directly. The Young County entry and index rows were visually checked. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": f"Review Box {box} for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before wartime service.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b956-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-956-v1",
        "reviewer": "Before OSS Batch 956 evidence review",
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
