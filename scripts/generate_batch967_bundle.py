#!/usr/bin/env python3
"""Generate the reviewed Batch 967 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page474-robert-true-to-ernest-tsikerdanos-"
    "review_batch-967_2026-10-30.json"
)

INDEX = "nara-index-b967"
ARMY = "army-bulk-b967"
TECH = "army-tech-b967"
CODES = "army-codes-b967"
TRUELSEN_DBL = "lex-truelsen-b967"
TRUEX_OSS = "javadc-truex-oss-b967"
TRUEX_MEMOIR = "cnumc-truex-b967"
TRUMPS_WAPO = "wapo-trumps-b967"
TRUMPS_ARMY = "army-trumps-b967"
TRYFOROS_CIA = "cia-tryforos-b967"
TRYGSTAD_ND = "nd-trygstad-b967"
ASSESSMENT = "assessment-men-b967"
TRYON_NPS = "nps-tryon-b967"
TRYON_BERKELEY = "berkeley-tryon-b967"
TSANTES_OSS = "elia-tsantes-oss-b967"
TSIKERDANOS_WAPO = "wapo-tsikerdanos-b967"
TSIKERDANOS_ARMY = "arsof-tsikerdanos-b967"
TRULAND_BURIAL = "interment-truland-b967"
TRUMM_ENLISTMENT = "jodaviess-trumm-b967"


PEOPLE = {
    1: ("1f3f2f86-1131-5c89-afa0-4584b27e1f66", "Robert E True"),
    2: ("a597dda4-f3f2-5810-b6a9-b64c36c3a35f", "Svend Truelsen"),
    3: ("d3e1dd89-72b7-50c4-ae48-5d35b7c412df", "Ralph J Truex"),
    4: ("ca3e1a33-98bc-5e87-8111-5854761e079a", "Jerry Truhlar"),
    5: ("06f87d98-2b77-5cc7-9201-187642246fd2", "Jerry Truhler"),
    6: ("32803515-8f02-5e84-b5e8-7070b27bcc53", "William D Truland"),
    7: ("a9084a8e-b3c8-5693-a4ea-e7b1d10636ec", "Robert Truman"),
    8: ("979cc12a-a410-51fe-baf0-df2fa24f98aa", "Carl J Trumm"),
    9: ("8ad7fbdb-a037-59e3-a49d-f650195d497d", "Shirly R Trumps"),
    10: ("d2405232-fb46-5186-bdf1-21943702ef2b", "Margaret M Trun"),
    11: ("3464bec3-da6a-5f1a-848f-6ce2fc249ed0", "Joseph Trunecek"),
    12: ("262eb5f7-5878-5754-ace3-cd794c08888e", "Charles V Trupia"),
    13: ("4ad3f882-8c87-5f79-80f5-f747a692788e", "John F Trutza"),
    14: ("f0ed9496-997a-5d53-b06f-1ba768443d37", "Nicholas Tryforos"),
    15: ("ac8023d9-1343-57d2-b7e1-3b20feaedfea", "Bernard H Trygstad"),
    16: ("0aaf902d-ab7a-5157-8f85-606a5bdd7ec0", "Frieda B Tryon"),
    17: ("fd420531-2b35-5def-bec9-c2c195d0c421", "Robert C Tryon"),
    18: ("f71cf73f-d6a4-572a-989d-c2817e211b99", "Yueh C Tsai"),
    19: ("31dbb69d-f3fc-5f4e-a8d7-8ed1806f9911", "Ioannis Tsankaris"),
    20: ("80e11206-f295-5b89-a9b9-56d41c5a08e2", "Eleftherius Tsantes"),
    21: ("46c805e8-c8de-5fd5-9f26-8ccfb50d76e3", "Ernest C Tschonis"),
    22: ("42b9c424-c2f9-5881-ae1c-1d2677b0b01b", "Cheng K Tseng"),
    23: ("307cecc3-b3f5-5f4c-98e7-f1aede79589c", "Ernest Tsikerdanos"),
}


ARMY_OCCUPATIONS = [
    {
        "row": 6,
        "date": "1943-01-29",
        "code": "061",
        "occupation": "Radio operators",
        "public_occupation": "radio operator",
        "locator": "PDF physical page 171; historical category 0-61",
        "identity": "probable",
        "identity_note": "The official Army bulk file has one exact rare-name record, independently corroborated as a World War II Army veteran, but no protected-identifier bridge to Box 786 was available.",
        "extra_source": TRULAND_BURIAL,
    },
    {
        "row": 8,
        "date": "1941-09-03",
        "code": "002",
        "occupation": "Actors and actresses",
        "public_occupation": "actor or actress",
        "locator": "PDF physical page 170; historical category 0-02",
        "identity": "probable",
        "identity_note": "The official Army bulk file has one exact rare-name record, and a county enlistment index independently gives the same name and entry date, but no Box 787 bridge was available.",
        "extra_source": TRUMM_ENLISTMENT,
    },
    {
        "row": 11,
        "date": "1944-12-28",
        "code": "133",
        "occupation": "Secretaries",
        "public_occupation": "secretary",
        "locator": "PDF physical page 171; historical category 1-33",
        "identity": "high_confidence",
        "identity_note": "An exact full name and nonshared protected identifier connect the index row to the reviewed official Army row.",
    },
    {
        "row": 13,
        "date": "1942-12-04",
        "code": "578",
        "occupation": "Millwrights",
        "public_occupation": "millwright",
        "locator": "PDF physical page 175; historical category 5-78",
        "identity": "high_confidence",
        "identity_note": "The exact nonshared protected identifier bridges the index row to an Army name with a one-character spacing/transcription defect; both forms remain visible.",
    },
    {
        "row": 18,
        "date": "1943-04-19",
        "code": "209",
        "occupation": "Miscellaneous servants, private family",
        "public_occupation": "private-family domestic-service occupation",
        "locator": "PDF physical page 172; historical category 2-09",
        "identity": "high_confidence",
        "identity_note": "An exact full name and nonshared protected identifier connect the index row to the reviewed official Army row.",
    },
    {
        "row": 19,
        "date": "1943-02-15",
        "code": "727",
        "occupation": "Painters, construction and maintenance",
        "public_occupation": "construction or maintenance painter",
        "locator": "PDF physical page 174; historical category 7-27",
        "identity": "high_confidence",
        "identity_note": "The exact nonshared protected identifier connects the index row to Ioannis E Tsankaris; the corrupt Army grade field is not interpreted.",
    },
    {
        "row": 20,
        "date": "1943-05-19",
        "code": "030",
        "occupation": "Teachers, primary school and kindergarten",
        "public_occupation": "primary-school or kindergarten teacher",
        "locator": "PDF physical page 171; historical category 0-30",
        "identity": "confirmed",
        "identity_note": "The protected identifier connects the index, Army row printed as Terry T Tsantes and an original OSS record printed as Eleftherios T Tsantes.",
        "extra_source": TSANTES_OSS,
    },
]


UNRESOLVED = {
    1: "Three official Army rows carry the exact common name Robert E True, and the index row supplies no protected identifier or second discriminator.",
    4: "Exact-name, spelling-variant, official-domain, occupation, obituary, institutional, newspaper and archival searches produced no defensible identity bridge.",
    5: "Exact-name and spelling-variant searches produced no independent identity bridge; the adjacent Jerry Truhlar row is treated only as a possible duplicate, never a merge.",
    7: "The common name and missing middle initial produced multiple namesakes without two corroborating identifiers beyond the name.",
    10: "Exact-name, initials, occupation, obituary, institutional, newspaper and archival searches produced no defensible identity bridge.",
    21: "Exact-name and variant searches produced no reliable OSS identity, dated occupation or employing organization.",
    22: "Exact-name and transliteration-variant searches produced no reliable identity bridge, dated occupation or employing organization.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 786-787",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 474, rows 1-23; checked against layout-preserving text and a 200 dpi page render",
            "access_date": "2026-10-30",
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
            "locator": "Official unrestricted ASNEF.FIN.DAT; six accepted, one rejected and two name-only Batch 967 comparisons; protected identifiers withheld",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "No raw bulk row, record ordinal or full protected identifier enters the evidence bundle or public assets. The 1946 Ernest Tsikerdanos row supports identity only, never pre-OSS chronology.",
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
            "locator": "PDF physical pages 170-175; seven Batch 967 historical civilian-status categories visually and textually checked",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical occupation groups identify neither employers nor workplaces and retain period terminology only where needed for auditability.",
        },
        {
            "key": TRUELSEN_DBL,
            "stable_url": "https://biografiskleksikon.lex.dk/Svend_Truelsen",
            "title": "Svend Truelsen",
            "author_creator": "Merete Harding and Jørgen Hæstrup",
            "repository_publisher": "Dansk Biografisk Leksikon; Lex.dk",
            "publication_record_date": "2015-01-04",
            "locator": "Biographical chronology: Landbrugsrådet employment, Agriculture Ministry committee, intelligence work and May 1944 departure",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Dansk Biografisk Leksikon",
        },
        {
            "key": TRUEX_OSS,
            "stable_url": "https://www.javadc.org/java/docs/1945-03-15%20OSSSU%20Detachment%20101%20Promotions%20and%20Citations%20OCR%20P11_MA.pdf",
            "archival_identifier": "OSS Detachment 101 promotions and citations memorandum, 15 March 1945",
            "title": "OSS Detachment 101 Promotions and Citations",
            "author_creator": "Office of Strategic Services, Detachment 101",
            "repository_publisher": "Japanese American Veterans Association digital archive",
            "publication_record_date": "1945-03-15",
            "locator": "Promotion recommendations; Ralph J Truex, First Lieutenant",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "Digitized OSS Detachment 101 records",
        },
        {
            "key": TRUEX_MEMOIR,
            "stable_url": "https://www.cnumc.org/files/pdf_documents/journals/journal2013_revised110713.pdf",
            "title": "Ovidia Truex Brackney memoir",
            "author_creator": "Ovidia Truex Brackney",
            "repository_publisher": "Commission on Archives and History, Western North Carolina Conference of the United Methodist Church",
            "publication_record_date": "2013",
            "locator": "Journal, printed page 289; January 1943 West Point graduation and OSS volunteering chronology",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Historical Society journal",
        },
        {
            "key": TRUMPS_WAPO,
            "stable_url": "https://www.washingtonpost.com/archive/local/2006/12/05/army-col-shirly-ray-trumps/99adcb28-64f9-478d-b08f-2b75a58058ba/",
            "title": "Army Col. Shirly Ray Trumps",
            "author_creator": "Joe Holley",
            "repository_publisher": "The Washington Post",
            "publication_record_date": "2006-12-05",
            "locator": "Obituary; National Guard, 1940 Army entry, 1942 commission and 1943 OSS application chronology",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
        },
        {
            "key": TRUMPS_ARMY,
            "stable_url": "https://www.armyupress.army.mil/Journals/Military-Review/Online-Exclusive/2024-OLE/Glorious-Amateurs/",
            "title": "Glorious Amateurs: The Women of the OSS",
            "author_creator": "U.S. Army University Press",
            "repository_publisher": "U.S. Army University Press",
            "publication_record_date": "2024",
            "locator": "Jedburgh Team Ronald photograph caption; spelling variant Shirley R. Trumps",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
        },
        {
            "key": TRYFOROS_CIA,
            "stable_url": "https://www.cia.gov/readingroom/docs/BISHOP%2C%20ROBERT_0060.pdf",
            "archival_identifier": "OSS U.S. Army Forces Middle East memorandum, 1 July 1944",
            "title": "Assignment of Qualified Personnel to OSS-ME Parachute Unit",
            "author_creator": "Office of Strategic Services, U.S. Army Forces in the Middle East",
            "repository_publisher": "Central Intelligence Agency Reading Room",
            "publication_record_date": "1944-07-01",
            "locator": "PDF page 1; Second Lieutenant Nicholas J. P. Tryforos; protected identifier withheld",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "OSS Collection",
        },
        {
            "key": TRYGSTAD_ND,
            "stable_url": "https://www.veterans.nd.gov/sites/www/files/documents/resource/T.pdf",
            "title": "North Dakota World War II Military Service Record: T",
            "author_creator": "North Dakota Department of Veterans Affairs",
            "repository_publisher": "North Dakota Department of Veterans Affairs",
            "publication_record_date": "World War II service compilation",
            "locator": "Printed page 1511; Bernard H Trygstad Navy service, dates and lieutenant junior grade",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
        },
        {
            "key": ASSESSMENT,
            "stable_url": "https://mcoecbamcoepwprd01.blob.core.usgovcloudapi.net/library/ebooks/Assessment_of_Men_Final.pdf",
            "title": "Assessment of Men: Selection of Personnel for the Office of Strategic Services",
            "author_creator": "OSS Assessment Staff",
            "repository_publisher": "War Department; U.S. Army digital library",
            "publication_record_date": "1948",
            "locator": "Front matter, printed page vii; staff listing for Frieda B. Tryon and University of North Carolina",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
        },
        {
            "key": TRYON_NPS,
            "stable_url": "https://www.nps.gov/articles/a-wartime-organization-for-unconventional-warfare.htm",
            "title": "A Wartime Organization for Unconventional Warfare",
            "author_creator": "National Park Service",
            "repository_publisher": "National Park Service",
            "publication_record_date": "not stated",
            "locator": "Assessing Recruits section; Robert C. Tryon from the University of California",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
        },
        {
            "key": TRYON_BERKELEY,
            "stable_url": "https://psychology.berkeley.edu/about/history/memoriam",
            "title": "In Memoriam: Robert Choate Tryon",
            "author_creator": "University of California, Berkeley Department of Psychology",
            "repository_publisher": "University of California, Berkeley",
            "publication_record_date": "not stated",
            "locator": "Robert Choate Tryon memorial; faculty service from 1931 and wartime OSS planning role",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
        },
        {
            "key": TSANTES_OSS,
            "stable_url": "https://www.elia.org.gr/userfiles/pdf_archieve/1944%209-1544%20Date%20Estimated%2C%20OSS%20Missions%2C%20SOE%2C%20Train%20Sabotage%2C%20Katerini%2C%20Tsirmulas%2C%20226-99-45-5%20%28Admin%29.pdf",
            "archival_identifier": "RG 226, train-sabotage mission administrative record, 1944",
            "title": "OSS Missions and SOE Train Sabotage Administrative Record",
            "author_creator": "Office of Strategic Services",
            "repository_publisher": "Hellenic Literary and Historical Archive",
            "publication_record_date": "1944",
            "locator": "Greek Operational Group personnel listing; Sergeant Eleftherios T. Tsantes; protected identifier withheld",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "Digitized OSS records",
        },
        {
            "key": TSIKERDANOS_WAPO,
            "stable_url": "https://www.washingtonpost.com/archive/local/1997/12/18/ernest-j-tsikerdanos-dies/e63e4b6a-93c3-47a8-8e3e-2f8f52a70006/",
            "title": "Ernest J. Tsikerdanos Dies",
            "author_creator": "Bart Barnes",
            "repository_publisher": "The Washington Post",
            "publication_record_date": "1997-12-18",
            "locator": "Obituary; 1942 Army entry, 82nd Airborne service and OSS recruitment chronology",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
        },
        {
            "key": TSIKERDANOS_ARMY,
            "stable_url": "https://arsof-history.org/articles/pdf/v4n2_wings_over_burma.pdf",
            "title": "Wings Over Burma",
            "author_creator": "U.S. Army Special Operations Command History Office",
            "repository_publisher": "U.S. Army Special Operations Command History Office",
            "publication_record_date": "not stated",
            "locator": "Detachment 101 photograph caption; Corporal Ernest J. Tsikerdanos",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
        },
        {
            "key": TRULAND_BURIAL,
            "stable_url": "https://www.interment.net/united-states/maine/veterans-burials/records.php?page=546",
            "title": "Maine Veterans Memorial Cemetery Burial Records",
            "repository_publisher": "Interment.net",
            "publication_record_date": "not stated",
            "locator": "William D. Truland entry; U.S. Army sergeant and World War II service",
            "access_date": "2026-10-30",
            "source_quality": "D_correlative_or_secondary",
        },
        {
            "key": TRUMM_ENLISTMENT,
            "stable_url": "https://genealogytrails.com/ill/jodaviess/ww2enlistments.html",
            "title": "Jo Daviess County World War II Enlistments",
            "repository_publisher": "Illinois Genealogy Trails",
            "publication_record_date": "not stated",
            "locator": "Carl J. Trumm entry; 3 September 1941 Army entry",
            "access_date": "2026-10-30",
            "source_quality": "D_correlative_or_secondary",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": "us-army-b967",
            "organization_id": "28a26f92-78af-5a1a-9c09-a843eb5975b4",
            "canonical_name": "United States Army",
            "historical_name": "Army of the United States",
            "aliases": ["U.S. Army"],
            "organization_type": "military service",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "Existing canonical organization reused; military assignment remains distinct from civilian employment.",
        },
        {
            "key": "us-navy-b967",
            "organization_id": "3960fa8e-a551-56cf-8305-b2b9e4961b9d",
            "canonical_name": "United States Navy",
            "historical_name": "United States Navy",
            "aliases": ["U.S. Navy", "USNR"],
            "organization_type": "military service",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "Existing canonical organization reused; service is not a civilian employer.",
        },
        {
            "key": "usma-b967",
            "organization_id": "a6458663-2447-50ce-aa34-4a72ffa79348",
            "canonical_name": "United States Military Academy",
            "historical_name": "United States Military Academy at West Point",
            "aliases": ["West Point", "USMA"],
            "organization_type": "military academy",
            "sector": "academia_and_research",
            "city": "West Point",
            "state_or_region": "New York",
            "country": "United States",
            "normalization_notes": "Existing canonical organization reused; cadet/student status is not employment.",
        },
        {
            "key": "uc-berkeley-b967",
            "organization_id": "dd5d0a44-0368-5e91-a5d3-074de36840ed",
            "canonical_name": "University of California, Berkeley",
            "historical_name": "University of California at Berkeley",
            "aliases": ["University of California", "UC Berkeley"],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "Berkeley",
            "state_or_region": "California",
            "country": "United States",
            "normalization_notes": "Existing canonical organization reused; source wording is preserved in the affiliation.",
        },
        {
            "key": "unc-b967",
            "organization_id": "9cc015ac-3491-56a3-aa28-f56963885d3c",
            "canonical_name": "University of North Carolina at Chapel Hill",
            "historical_name": "University of North Carolina",
            "aliases": ["University of North Carolina", "UNC", "UNC-Chapel Hill"],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "Chapel Hill",
            "state_or_region": "North Carolina",
            "country": "United States",
            "normalization_notes": "Existing canonical organization reused; the 1948 staff list establishes affiliation but not the relationship type.",
        },
        {
            "key": "82nd-airborne-b967",
            "organization_id": "f0133687-d4bd-5cf5-ab49-d2b155920f3d",
            "canonical_name": "82nd Airborne Division",
            "historical_name": "82nd Airborne Division",
            "aliases": ["82nd Airborne"],
            "organization_type": "Army division",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "Existing canonical organization reused as a military assignment, not a civilian employer.",
        },
        {
            "key": "landbrugsraadet-b967",
            "canonical_name": "Danish Agricultural Council",
            "historical_name": "Landbrugsrådet",
            "aliases": ["Landbrugsraadet", "Danish Agriculture Council"],
            "organization_type": "agricultural trade council",
            "sector": "business_and_industry",
            "city": "Copenhagen",
            "country": "Denmark",
            "normalization_notes": "The historical Danish name is preserved and is not replaced by a modern successor organization.",
        },
        {
            "key": "danish-intelligence-b967",
            "canonical_name": "Danish General Staff Intelligence Service",
            "historical_name": "Generalstabens Efterretningssektion",
            "aliases": ["Danish military intelligence", "General Staff intelligence section"],
            "organization_type": "military intelligence service",
            "sector": "military",
            "country": "Denmark",
            "normalization_notes": "The source describes both official intelligence work and the later clandestine network; administrative continuity requires archival review.",
        },
        {
            "key": "danish-agriculture-ministry-b967",
            "canonical_name": "Danish Ministry of Agriculture",
            "historical_name": "Landbrugsministeriet",
            "aliases": ["Ministry of Agriculture"],
            "organization_type": "national government ministry",
            "sector": "federal_government",
            "city": "Copenhagen",
            "country": "Denmark",
            "normalization_notes": "Foreign national-government assignment; modeled separately from Landbrugsrådet employment.",
        },
        {
            "key": "louisiana-national-guard-b967",
            "canonical_name": "Louisiana National Guard",
            "historical_name": "Louisiana National Guard",
            "aliases": [],
            "organization_type": "state National Guard",
            "sector": "military",
            "state_or_region": "Louisiana",
            "country": "United States",
            "normalization_notes": "State military affiliation distinct from later active U.S. Army service.",
        },
    ]


def occupation_affiliation(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    return {
        "key": f"{slug(PEOPLE[row][1])}-occupation-b967",
        "person_id": PEOPLE[row][0],
        "occupation": item["public_occupation"],
        "relationship_type": "unknown",
        "end_date": item["date"],
        "date_precision": f"Historical civilian-status code {item['code']} was recorded at Army entry on {item['date']}; no employer, workplace or OSS-transfer date is named.",
        "country": "United States",
        "immediate_pre_oss": False,
        "last_civilian_pre_service": False,
        "pre_oss_temporal_basis": "strongly_date_bounded",
        "identity_confidence": item["identity"],
        "claim_confidence": "medium",
        "source_quality": "A_direct_official",
        "publication_status": "publish_qualified",
        "research_notes": "The historical category is not converted into a named employer, workplace or immediate pre-OSS affiliation.",
    }


def specialist_affiliations() -> list[dict[str, object]]:
    return [
        {
            "key": "svend-truelsen-landbrugsraadet-b967",
            "person_id": PEOPLE[2][0],
            "organization_key": "landbrugsraadet-b967",
            "organization_name_as_found": "Landbrugsrådet",
            "role_title": "secretary",
            "occupation": "agricultural-council secretary",
            "relationship_type": "employment",
            "start_date": "1936",
            "end_date": "1944-05",
            "date_precision": "The biography dates employment from 1936 and his departure from Denmark to May 1944; the exact formal employment end is not stated.",
            "city": "Copenhagen",
            "country": "Denmark",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": True,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "published",
            "research_notes": "Best-supported last civilian employer. It is separated from intelligence and Agriculture Ministry assignments.",
        },
        {
            "key": "svend-truelsen-intelligence-b967",
            "person_id": PEOPLE[2][0],
            "organization_key": "danish-intelligence-b967",
            "organization_name_as_found": "General Staff intelligence section and reconstructed intelligence network",
            "role_title": "intelligence officer and network leader",
            "relationship_type": "military_assignment",
            "start_date": "1943-08",
            "end_date": "1944-05",
            "date_precision": "The biography says Truelsen rebuilt Danish intelligence after 29 August 1943 and left Denmark for Allied service in May 1944.",
            "country": "Denmark",
            "immediate_pre_oss": True,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "explicit_immediate",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "published",
            "research_notes": "The immediate pathway is an intelligence/military affiliation, not a civilian employer.",
        },
        {
            "key": "svend-truelsen-agriculture-ministry-b967",
            "person_id": PEOPLE[2][0],
            "organization_key": "danish-agriculture-ministry-b967",
            "organization_name_as_found": "Landbrugsministeriets kødforsyningsudvalg",
            "role_title": "daily head of the meat-supply committee",
            "relationship_type": "government_assignment",
            "start_date": "1939-12",
            "end_date": "1943-08",
            "date_precision": "The biography places the committee assignment after his December 1939 return from General Staff intelligence; the precise end is not stated.",
            "city": "Copenhagen",
            "country": "Denmark",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "high_confidence",
            "claim_confidence": "medium",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "publish_qualified",
            "research_notes": "Modeled as a government assignment; the source does not establish the ministry as his employer.",
        },
        {
            "key": "ralph-truex-us-army-b967",
            "person_id": PEOPLE[3][0],
            "organization_key": "us-army-b967",
            "organization_name_as_found": "United States Army",
            "role_title": "commissioned officer",
            "relationship_type": "military_assignment",
            "start_date": "1943-01",
            "end_date": "1943",
            "date_precision": "The family memoir dates his West Point graduation and marriage to January 1943 and says he then volunteered for OSS service; the exact transfer date is not given.",
            "country": "United States",
            "immediate_pre_oss": True,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "probable_immediate",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "published",
            "research_notes": "Military pathway, not civilian employment. The OSS memorandum independently confirms Ralph J Truex as a First Lieutenant in Detachment 101.",
        },
        {
            "key": "ralph-truex-usma-b967",
            "person_id": PEOPLE[3][0],
            "organization_key": "usma-b967",
            "organization_name_as_found": "U.S. Military Academy",
            "role_title": "cadet and graduate",
            "relationship_type": "student",
            "end_date": "1943-01",
            "date_precision": "The family memoir dates graduation to January 1943.",
            "city": "West Point",
            "state_or_region": "New York",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "published",
            "research_notes": "Student/cadet status is explicitly separated from employment.",
        },
        {
            "key": "shirly-trumps-us-army-b967",
            "person_id": PEOPLE[9][0],
            "organization_key": "us-army-b967",
            "organization_name_as_found": "Army",
            "role_title": "infantry second lieutenant",
            "relationship_type": "military_assignment",
            "start_date": "1940",
            "end_date": "1943",
            "date_precision": "The obituary dates Army entry to 1940, commission to 1942 and the French-language special-mission application and OSS entry to 1943.",
            "country": "United States",
            "immediate_pre_oss": True,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "explicit_immediate",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "published",
            "research_notes": "The obituary explicitly describes application from active Army service to the OSS program.",
        },
        {
            "key": "shirly-trumps-louisiana-guard-b967",
            "person_id": PEOPLE[9][0],
            "organization_key": "louisiana-national-guard-b967",
            "organization_name_as_found": "Louisiana National Guard",
            "role_title": "National Guard member",
            "relationship_type": "military_assignment",
            "end_date": "1940",
            "date_precision": "The obituary says he joined the Army in 1940 as a Louisiana National Guard member.",
            "state_or_region": "Louisiana",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "published",
            "research_notes": "Earlier military affiliation; no civilian employer is inferred.",
        },
        {
            "key": "bernard-trygstad-navy-b967",
            "person_id": PEOPLE[15][0],
            "organization_key": "us-navy-b967",
            "organization_name_as_found": "U.S. Navy",
            "role_title": "lieutenant junior grade",
            "relationship_type": "military_assignment",
            "start_date": "1942-09-17",
            "end_date": "1945-12-31",
            "date_precision": "North Dakota's official service record supplies entry and separation dates and final listed grade; it does not date an OSS transfer.",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "temporal_relation_uncertain",
            "identity_confidence": "probable",
            "claim_confidence": "medium",
            "source_quality": "A_direct_official",
            "publication_status": "publish_qualified",
            "research_notes": "Rare exact name and compatible Navy service support a probable identity, but Box 787 must establish the OSS bridge and immediate sequence.",
        },
        {
            "key": "frieda-tryon-unc-b967",
            "person_id": PEOPLE[16][0],
            "organization_key": "unc-b967",
            "organization_name_as_found": "University of North Carolina",
            "role_title": "OSS Assessment Staff member associated with the University of North Carolina",
            "relationship_type": "professional_affiliation",
            "end_date": "1945",
            "date_precision": "The OSS staff list supplies the institutional parenthetical but neither a job title nor the date or type of the university relationship.",
            "state_or_region": "North Carolina",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "temporal_relation_uncertain",
            "identity_confidence": "high_confidence",
            "claim_confidence": "medium",
            "source_quality": "A_direct_official",
            "publication_status": "publish_qualified",
            "research_notes": "The parenthetical is preserved as professional affiliation and is not promoted to employment or student status.",
        },
        {
            "key": "robert-tryon-berkeley-b967",
            "person_id": PEOPLE[17][0],
            "organization_key": "uc-berkeley-b967",
            "organization_name_as_found": "University of California",
            "role_title": "psychology professor",
            "occupation": "psychologist",
            "relationship_type": "employment",
            "start_date": "1931",
            "end_date": "1943",
            "date_precision": "Berkeley dates faculty service from 1931 and describes wartime OSS service; NPS independently says Tryon came from the University of California to lead assessment design. Exact leave date requires archive review.",
            "city": "Berkeley",
            "state_or_region": "California",
            "country": "United States",
            "immediate_pre_oss": True,
            "last_civilian_pre_service": True,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "confirmed",
            "claim_confidence": "high",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "published",
            "research_notes": "Two independent federal and university sources connect the exact person, institution and OSS assessment role.",
        },
        {
            "key": "ernest-tsikerdanos-82nd-b967",
            "person_id": PEOPLE[23][0],
            "organization_key": "82nd-airborne-b967",
            "organization_name_as_found": "82nd Airborne",
            "role_title": "soldier and volunteer",
            "relationship_type": "military_assignment",
            "start_date": "1942",
            "end_date": "1943",
            "date_precision": "The obituary says he joined the Army in 1942, volunteered for the 82nd Airborne and was then recruited into OSS; the exact recruitment date is not given.",
            "country": "United States",
            "immediate_pre_oss": True,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "explicit_immediate",
            "identity_confidence": "confirmed",
            "claim_confidence": "high",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "published",
            "research_notes": "The 82nd Airborne is an immediate military assignment, not a civilian employer. His high-school graduation is not treated as employment.",
        },
    ]


def claim(
    row: int,
    key: str,
    claim_type: str,
    text: str,
    paraphrase: str,
    identity: str,
    temporal: str,
    quality: str,
    confidence: str,
    links: list[dict[str, object]],
    notes: str,
    affiliation: str | None = None,
    publication_status: str | None = None,
) -> dict[str, object]:
    return {
        "key": key,
        "person_id": PEOPLE[row][0],
        "affiliation_key": affiliation,
        "claim_type": claim_type,
        "claim_text": text,
        "evidence_paraphrase": paraphrase,
        "identity_match_assessment": identity,
        "temporal_assessment": temporal,
        "source_quality": quality,
        "claim_confidence": confidence,
        "publication_status": publication_status or ("published" if confidence in {"confirmed", "high"} else "publish_qualified"),
        "match_notes": notes,
        "sources": links,
    }


def occupation_claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for item in ARMY_OCCUPATIONS:
        row = int(item["row"])
        name = PEOPLE[row][1]
        identity_confidence = str(item["identity"])
        identity_claim_confidence = "confirmed" if identity_confidence == "confirmed" else ("high" if identity_confidence == "high_confidence" else "medium")
        identity_links: list[dict[str, object]] = [
            {"source_key": INDEX, "locator_override": f"PDF page 474 row {row}; protected identifier withheld when present"},
            {"source_key": ARMY, "locator_override": "Reviewed identity comparison; protected identifier and bulk ordinal withheld"},
        ]
        extra = item.get("extra_source")
        if extra:
            identity_links.append({"source_key": str(extra), "support_type": "context_only"})
        values.append(
            claim(
                row,
                f"identity-{slug(name)}-army-b967",
                "identity",
                f"Indexed {name} is a {identity_confidence.replace('_', ' ')} match to the reviewed official Army entry.",
                str(item["identity_note"]),
                str(item["identity_note"]),
                "Identity evidence only; the source does not establish an OSS transfer date.",
                "A_direct_official",
                identity_claim_confidence,
                identity_links,
                "Protected identifiers and raw Army records remain private. Probable identities remain excluded from default employer analytics.",
                publication_status="publish_qualified" if identity_claim_confidence == "medium" else "published",
            )
        )
        values.append(
            claim(
                row,
                f"occupation-{slug(name)}-army-b967",
                "occupation",
                f"At Army entry on {item['date']}, the record coded {name}'s civilian status as {item['occupation']}.",
                f"The official Army row contains civilian-status code {item['code']}; NARA's historical code list expands it to {item['occupation']}.",
                str(item["identity_note"]),
                "The category is date-bounded at Army entry but identifies no employer, workplace or immediate OSS predecessor.",
                "A_direct_official",
                "medium",
                [
                    {"source_key": ARMY, "locator_override": f"Reviewed row; civilian-status code {item['code']}; protected identifier withheld when present"},
                    {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46; Army-entry-date and civilian-occupation fields"},
                    {"source_key": CODES, "locator_override": str(item["locator"]), "excerpt_override": str(item["occupation"])},
                ],
                "Published as qualified occupation evidence only and excluded from named-employer analytics.",
                f"{slug(name)}-occupation-b967",
                "publish_qualified",
            )
        )
    return values


def specialist_claims() -> list[dict[str, object]]:
    return [
        claim(2, "identity-svend-truelsen-b967", "identity", "Indexed Svend Truelsen is a high-confidence match to the Danish officer and intelligence organizer documented by Dansk Biografisk Leksikon.", "The rare exact name, reserve-officer status and wartime intelligence chronology align with the indexed foreign-personnel row.", "High confidence from the rare exact name, rank context and coherent wartime chronology; the Box 787 file remains unreviewed.", "Identity evidence spans the prewar through May 1944 chronology.", "B_authoritative_institutional", "high", [{"source_key": INDEX, "locator_override": "PDF page 474 row 2; Box 787"}, {"source_key": TRUELSEN_DBL}], "No unrelated NARA personnel PDF is cited; a previously explored Lucien Conein file was rejected after full-text OCR review."),
        claim(2, "last-civilian-svend-truelsen-b967", "last_civilian_pre_service", "Svend Truelsen's best-supported last civilian employer before Allied service was Landbrugsrådet, where he served as secretary.", "The biography dates his appointment as Landbrugsrådet secretary to 1936 and his departure for Allied service to May 1944.", "High-confidence rare-name identity with matching reserve-officer and intelligence chronology.", "Strongly date-bounded, though the exact formal employment end is not stated.", "B_authoritative_institutional", "high", [{"source_key": TRUELSEN_DBL, "locator_override": "Employment and May 1944 departure chronology"}], "The council is a civilian employer; military intelligence and ministry assignments remain separate.", "svend-truelsen-landbrugsraadet-b967"),
        claim(2, "immediate-svend-truelsen-intelligence-b967", "immediate_pre_oss_affiliation", "Svend Truelsen's immediate pre-Allied affiliation was the Danish intelligence network he rebuilt after August 1943.", "The biography says he reconstructed Danish intelligence after 29 August 1943 and left Denmark for Allied service in May 1944.", "High-confidence rare-name identity and matching officer chronology.", "Explicit immediate sequence from clandestine intelligence leadership to Allied service.", "B_authoritative_institutional", "high", [{"source_key": TRUELSEN_DBL, "locator_override": "Wartime intelligence chronology after 29 August 1943"}], "Modeled as military/intelligence assignment, not employment.", "svend-truelsen-intelligence-b967"),
        claim(2, "prewar-svend-truelsen-ministry-b967", "other_pre_oss_affiliation", "Svend Truelsen served as daily head of the Danish Agriculture Ministry's meat-supply committee after December 1939.", "The biography explicitly names the committee role after his return from General Staff intelligence.", "High-confidence rare-name identity.", "Documented prewar and wartime government assignment; exact end and employment form remain uncertain.", "B_authoritative_institutional", "medium", [{"source_key": TRUELSEN_DBL}], "The ministry is not labeled his employer.", "svend-truelsen-agriculture-ministry-b967", "publish_qualified"),
        claim(3, "identity-ralph-truex-b967", "identity", "Indexed Ralph J Truex is a high-confidence match to the West Point graduate and OSS Detachment 101 First Lieutenant.", "An original OSS promotion memorandum gives the exact name and rank; a family memoir independently supplies the middle name, West Point graduation and OSS volunteering chronology.", "High confidence from exact full-name OSS evidence plus independent biographical chronology.", "The sources cover January 1943 through Detachment 101 service.", "A_direct_official", "high", [{"source_key": INDEX, "locator_override": "PDF page 474 row 3; officer identifier withheld"}, {"source_key": TRUEX_OSS}, {"source_key": TRUEX_MEMOIR}], "The source set supports identity and military pathway, not a civilian employer."),
        claim(3, "immediate-ralph-truex-army-b967", "immediate_pre_oss_affiliation", "Ralph J Truex entered OSS from commissioned U.S. Army service after graduating from West Point in January 1943.", "The memoir says he graduated from West Point and volunteered for OSS; the original OSS memorandum later lists him as a First Lieutenant.", "High-confidence exact-name identity from original OSS and independent biographical sources.", "Probable immediate Army pathway; the exact transfer date was not found.", "C_reputable_contemporary_or_scholarly", "high", [{"source_key": TRUEX_MEMOIR, "locator_override": "Printed page 289"}, {"source_key": TRUEX_OSS, "support_type": "context_only"}], "Military assignment, not civilian employment.", "ralph-truex-us-army-b967"),
        claim(3, "student-ralph-truex-usma-b967", "other_pre_oss_affiliation", "Ralph J Truex graduated from the U.S. Military Academy in January 1943.", "The memoir explicitly dates West Point graduation to January 1943.", "High-confidence identity supported by original OSS and memoir evidence.", "Strongly date-bounded before Army and OSS service.", "C_reputable_contemporary_or_scholarly", "high", [{"source_key": TRUEX_MEMOIR, "locator_override": "Printed page 289"}], "Cadet/student status is not employment.", "ralph-truex-usma-b967"),
        claim(9, "identity-shirly-trumps-b967", "identity", "Indexed Shirly R Trumps is a high-confidence match to Army officer Shirly Ray Trumps of OSS Jedburgh Team Ronald.", "The obituary gives the exact uncommon name, full middle name and OSS application chronology; Army University Press independently captions the Jedburgh officer with a Shirley spelling variant.", "High confidence from the unusual exact name, matching commissioned rank and independent OSS/Jedburgh evidence.", "The chronology covers 1940 National Guard status through 1943 OSS entry.", "C_reputable_contemporary_or_scholarly", "high", [{"source_key": INDEX, "locator_override": "PDF page 474 row 9; officer identifier withheld"}, {"source_key": TRUMPS_WAPO}, {"source_key": TRUMPS_ARMY}], "Both Shirly and Shirley variants remain visible."),
        claim(9, "immediate-shirly-trumps-army-b967", "immediate_pre_oss_affiliation", "Shirly R Trumps applied to OSS from commissioned U.S. Army service in 1943.", "The obituary says the Army sought French-speaking special-mission volunteers in 1943 and that Trumps applied and joined OSS.", "High-confidence unusual-name identity with independent Jedburgh corroboration.", "Explicit immediate sequence from Army service to OSS application.", "C_reputable_contemporary_or_scholarly", "high", [{"source_key": TRUMPS_WAPO}], "Military assignment, not civilian employment.", "shirly-trumps-us-army-b967"),
        claim(9, "prewar-shirly-trumps-guard-b967", "other_pre_oss_affiliation", "Before active Army service, Shirly R Trumps belonged to the Louisiana National Guard.", "The obituary states he entered the Army in 1940 as a Louisiana National Guard member.", "High-confidence unusual-name identity.", "Documented earlier military affiliation.", "C_reputable_contemporary_or_scholarly", "high", [{"source_key": TRUMPS_WAPO}], "No civilian employer is inferred.", "shirly-trumps-louisiana-guard-b967"),
        claim(14, "identity-nicholas-tryforos-b967", "identity", "Indexed Nicholas Tryforos is confirmed as Second Lieutenant Nicholas J. P. Tryforos assigned to an OSS Middle East parachute unit.", "An original OSS memorandum supplies the expanded name, rank, branch, parachute-training date and the same protected officer identifier as the index.", "Confirmed by exact protected-identifier agreement and an original OSS personnel assignment record.", "The record documents OSS service in July 1944 but does not identify a pre-OSS employer.", "A_direct_official", "confirmed", [{"source_key": INDEX, "locator_override": "PDF page 474 row 14; protected identifier withheld"}, {"source_key": TRYFOROS_CIA, "locator_override": "PDF page 1; protected identifier withheld"}], "A Library of Congress Nicholas J. Tryforos namesake with enlisted rank and a different service history was explicitly rejected."),
        claim(15, "identity-bernard-trygstad-b967", "identity", "Indexed Bernard H Trygstad is a probable match to the North Dakota naval officer of the same rare full name.", "North Dakota's official record supplies the rare exact full name, wartime Navy dates and lieutenant junior grade.", "Probable only because the index has no protected identifier and no independent OSS or Box 787 bridge was found.", "The official service chronology overlaps the OSS period but does not date an OSS assignment.", "A_direct_official", "medium", [{"source_key": INDEX, "locator_override": "PDF page 474 row 15; Box 787"}, {"source_key": TRYGSTAD_ND, "locator_override": "Printed page 1511"}], "Excluded from confirmed/high identity analytics until the personnel file is reviewed.", publication_status="publish_qualified"),
        claim(15, "navy-bernard-trygstad-b967", "other_pre_oss_affiliation", "If the probable identity is correct, Bernard H Trygstad served in the U.S. Navy from September 1942 through December 1945 and attained lieutenant junior grade.", "North Dakota's official service record supplies the dates, branch, theater and final listed grade.", "Probable rare-name identity without an OSS bridge.", "Wartime service is explicit, but its immediate relation to OSS is unknown.", "A_direct_official", "medium", [{"source_key": TRYGSTAD_ND, "locator_override": "Printed page 1511"}], "Qualified military affiliation; no civilian employer is inferred.", "bernard-trygstad-navy-b967", "publish_qualified"),
        claim(16, "identity-frieda-tryon-b967", "identity", "Indexed Frieda B Tryon is a high-confidence match to the Frieda B. Tryon listed on the OSS Assessment Staff.", "The original OSS staff publication supplies the exact full indexed name and a University of North Carolina parenthetical.", "High confidence from the exact uncommon full name in a direct OSS staff list.", "The staff list documents OSS-era affiliation but does not date the university relationship.", "A_direct_official", "high", [{"source_key": INDEX, "locator_override": "PDF page 474 row 16; Box 787"}, {"source_key": ASSESSMENT, "locator_override": "Printed page vii"}], "The university parenthetical is not silently converted into employment."),
        claim(16, "affiliation-frieda-tryon-unc-b967", "other_pre_oss_affiliation", "The OSS Assessment Staff listed Frieda B. Tryon with the University of North Carolina.", "The staff list places University of North Carolina in parentheses after her name.", "High-confidence exact-name identity in a direct OSS source.", "Temporal relationship and role at the university are uncertain.", "A_direct_official", "medium", [{"source_key": ASSESSMENT, "locator_override": "Printed page vii", "excerpt_override": "Frieda B. Tryon (University of North Carolina)"}], "Published only as professional affiliation, not employer or student status.", "frieda-tryon-unc-b967", "publish_qualified"),
        claim(17, "identity-robert-tryon-b967", "identity", "Indexed Robert C Tryon is confirmed as Berkeley psychologist Robert Choate Tryon of the OSS Assessment Staff.", "NPS identifies Robert C. Tryon from the University of California as an OSS assessment leader; Berkeley independently gives his full name and wartime OSS planning role.", "Confirmed by exact name, institution, profession and matching OSS role across two authoritative sources.", "The sources establish both prewar faculty employment and wartime OSS service.", "B_authoritative_institutional", "confirmed", [{"source_key": INDEX, "locator_override": "PDF page 474 row 17; Box 787"}, {"source_key": TRYON_NPS}, {"source_key": TRYON_BERKELEY}], "Robert C. Tryon is distinct from Frieda B. Tryon; no kinship is inferred."),
        claim(17, "immediate-robert-tryon-berkeley-b967", "immediate_pre_oss_affiliation", "Robert C Tryon's immediate pre-OSS affiliation was the University of California, Berkeley, where he was a psychology professor.", "NPS says Tryon came from the University of California to lead OSS assessment design; Berkeley dates his faculty service from 1931 and notes wartime OSS duty.", "Confirmed identity from matching exact name, institution, profession and OSS role.", "Strongly date-bounded; the precise leave date remains unresolved.", "B_authoritative_institutional", "high", [{"source_key": TRYON_NPS, "locator_override": "Assessing Recruits section"}, {"source_key": TRYON_BERKELEY, "locator_override": "Robert Choate Tryon memorial"}], "The institutional and wartime chronology supports both immediate affiliation and last civilian employer.", "robert-tryon-berkeley-b967"),
        claim(17, "last-civilian-robert-tryon-berkeley-b967", "last_civilian_pre_service", "The University of California, Berkeley was Robert C Tryon's last documented civilian employer before OSS service.", "Berkeley records faculty service from 1931, while NPS explicitly describes him as coming from the University of California to OSS assessment work.", "Confirmed identity across two authoritative sources.", "Strongly date-bounded immediately before wartime OSS work.", "B_authoritative_institutional", "high", [{"source_key": TRYON_BERKELEY}, {"source_key": TRYON_NPS}], "Included in default verified-employer analytics.", "robert-tryon-berkeley-b967"),
        claim(23, "identity-ernest-tsikerdanos-b967", "identity", "Indexed Ernest Tsikerdanos is confirmed as Ernest John 'Chick' Tsikerdanos of OSS Detachment 101.", "The protected identifier bridges the index and official Army bulk row; Washington Post and Army history independently supply the full name and Detachment 101 service.", "Confirmed by exact protected-identifier agreement, an unusual exact surname and independent OSS service evidence.", "The official Army bulk record is dated February 1946 and is used for identity only, not pre-OSS chronology.", "A_direct_official", "confirmed", [{"source_key": INDEX, "locator_override": "PDF page 474 row 23; protected identifier withheld"}, {"source_key": ARMY, "locator_override": "Accepted identity bridge; 1946 fields excluded; protected identifier withheld"}, {"source_key": TSIKERDANOS_WAPO}, {"source_key": TSIKERDANOS_ARMY}], "Post-OSS Army fields are excluded from all prehistory claims."),
        claim(23, "immediate-ernest-tsikerdanos-82nd-b967", "immediate_pre_oss_affiliation", "Ernest Tsikerdanos entered OSS after volunteering for the U.S. Army's 82nd Airborne Division.", "The obituary says he joined the Army as an eighteen-year-old high-school graduate, volunteered for the 82nd Airborne and was then recruited into OSS.", "Confirmed identity from protected-identifier, exact-name and independent Detachment 101 evidence.", "Explicit immediate sequence from 82nd Airborne service to OSS recruitment.", "C_reputable_contemporary_or_scholarly", "high", [{"source_key": TSIKERDANOS_WAPO}, {"source_key": TSIKERDANOS_ARMY, "support_type": "context_only"}], "Military assignment, not civilian employment; high-school graduation is not treated as a job.", "ernest-tsikerdanos-82nd-b967"),
    ]


def claims() -> list[dict[str, object]]:
    return occupation_claims() + specialist_claims()


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
    values = [
        base_update(row, identity_status="ambiguous" if row == 1 else "unresolved", identity_evidence=f"The visually verified index row supplies {PEOPLE[row][1]}, Box {'786' if row <= 3 else '787'} and archive location 230/86/42/03. {reason}", personnel_category="unknown_or_indeterminate", commissioned_officer=None, allied_or_foreign_personnel=False, research_status="requires_archival_review", next_action=f"Review the indexed personnel file for corroborating identifiers, immediate pre-OSS affiliation and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}")
        for row, reason in UNRESOLVED.items()
    ]
    # Preserve adjacent spelling variants as a possible duplicate cluster, never a merge.
    for value in values:
        if value["person_id"] in {PEOPLE[4][0], PEOPLE[5][0]}:
            value["possible_duplicate_group"] = "page474-jerry-truhlar-truhler"

    for item in ARMY_OCCUPATIONS:
        row = int(item["row"])
        values.append(base_update(row, identity_status=item["identity"], identity_evidence=item["identity_note"], name_variants=["Ioannis E Tsankaris"] if row == 19 else (["Eleftherios T Tsantes", "Terry T Tsantes"] if row == 20 else None), personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="occupation_only_found", next_action="Review the indexed personnel file to establish the immediate pre-OSS affiliation, wartime grade and named last civilian employer; do not convert the Army occupation category into a workplace."))

    values.extend(
        [
            base_update(2, identity_status="high_confidence", identity_evidence="The rare exact name, reserve-officer status and coherent Danish intelligence chronology support a high-confidence match to the indexed row.", personnel_category="foreign_or_allied_military_personnel", commissioned_officer=True, allied_or_foreign_personnel=True, research_status="verified_employer_found", next_action="Review Box 786 to confirm administrative OSS status and the exact end of Landbrugsrådet employment; preserve intelligence and ministry assignments separately."),
            base_update(3, identity_status="high_confidence", identity_evidence="An original OSS Detachment 101 memorandum supplies the exact name and First Lieutenant rank; an independent family memoir supplies Ralph Joseph Truex, January 1943 West Point graduation and OSS volunteering.", name_variants=["Ralph Joseph Truex"], personnel_category="commissioned_army_officer", commissioned_officer=True, allied_or_foreign_personnel=False, research_status="occupation_only_found", next_action="Review Box 786 for the exact Army-to-OSS transfer date and any last civilian employer before West Point."),
            base_update(9, identity_status="high_confidence", identity_evidence="The unusual exact name, Army commission and 1943 OSS application chronology in a reputable obituary align with an Army institutional Jedburgh caption.", name_variants=["Shirly Ray Trumps", "Shirley R. Trumps"], personnel_category="commissioned_army_officer", commissioned_officer=True, allied_or_foreign_personnel=False, research_status="occupation_only_found", next_action="Review Box 787 for the exact OSS entry date and any civilian employment before National Guard service."),
            base_update(12, identity_status="conflicting", identity_evidence="The only protected-identifier Army candidate carries a completely different full name from Charles V Trupia; the candidate was rejected and none of its fields were transferred.", personnel_category="unknown_or_indeterminate", commissioned_officer=None, allied_or_foreign_personnel=False, research_status="conflicting_sources", next_action="Review Box 787 and original service documentation to resolve the protected-identifier collision. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.", archival_review_priority="critical"),
            base_update(14, identity_status="confirmed", identity_evidence="An original CIA Reading Room OSS memorandum supplies Second Lieutenant Nicholas J. P. Tryforos and the same protected officer identifier as the index.", name_variants=["Nicholas J. P. Tryforos"], personnel_category="commissioned_army_officer", commissioned_officer=True, allied_or_foreign_personnel=False, research_status="requires_archival_review", next_action="Review Box 787 for the assignment immediately before the OSS Middle East parachute unit and the last civilian employer. Keep the rejected enlisted Nicholas J. Tryforos namesake separate."),
            base_update(15, identity_status="probable", identity_evidence="North Dakota's official record gives the rare exact full name, Navy dates and lieutenant junior grade, but no independent OSS or protected-identifier bridge.", personnel_category="commissioned_naval_officer", commissioned_officer=True, allied_or_foreign_personnel=False, research_status="occupation_only_found", next_action="Review Box 787 to confirm the identity, OSS relationship and immediate pre-OSS assignment; do not infer a civilian employer from postwar pharmacy evidence.", archival_review_priority="critical"),
            base_update(16, identity_status="high_confidence", identity_evidence="The original OSS Assessment Staff publication lists the uncommon exact full name Frieda B. Tryon with a University of North Carolina parenthetical.", personnel_category="civilian_professional_or_administrative_grade", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="occupation_only_found", next_action="Review Box 787 and UNC records to determine whether the institutional parenthetical denotes employment, study or another professional relationship."),
            base_update(17, identity_status="confirmed", identity_evidence="NPS and UC Berkeley independently connect Robert C. Tryon/Robert Choate Tryon, the University of California, psychology and OSS assessment leadership.", name_variants=["Robert Choate Tryon"], personnel_category="civilian_professional_or_administrative_grade", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="verified_employer_found", next_action="Review Box 787 and Berkeley leave records for the precise OSS start and university leave date."),
            base_update(23, identity_status="confirmed", identity_evidence="The protected identifier bridges the index and official Army bulk identity; Washington Post and Army institutional sources independently identify Ernest John Tsikerdanos in OSS Detachment 101.", name_variants=["Ernest John Tsikerdanos", "Chick Tsikerdanos"], personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="occupation_only_found", next_action="Review Box 787 for the exact 82nd Airborne-to-OSS recruitment date and any civilian employment before Army entry. Do not use the February 1946 Army fields as prehistory."),
        ]
    )
    return values


def research_attempts() -> list[dict[str, object]]:
    source_review_rows = {2, 3, 6, 8, 9, 11, 13, 14, 15, 16, 17, 18, 19, 20, 23}
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        if row in source_review_rows:
            outcome = "source_reviewed"
            reviewed = 5 if row in {2, 3, 9, 17, 23} else 4
            rejected = 4
            detail = "Reviewed direct or institutional evidence produced the qualified identity, occupation, military pathway or employer outcome recorded in the evidence bundle."
        elif row == 12:
            outcome = "candidate_rejected"
            reviewed = 5
            rejected = 7
            detail = "Rejected the only protected-identifier Army candidate because it carries a completely different full name from Charles V Trupia; no record fields were transferred."
        else:
            outcome = "no_result"
            reviewed = 7
            rejected = 6
            detail = UNRESOLVED[row]
        attempts.append(
            {
                "key": f"page474-row{row}-{slug(name)}-b967",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index and official Archives context; CIA Reading Room or equivalent official-source check; exact-name and meaningful variants; OSS, Army, Navy and rank clues; employer and occupation 1940; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Boxes 786-787; protected identifiers used only when defensible",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_967",
                "started_at": "2026-10-30T14:20:00Z",
                "completed_at": "2026-10-30T18:30:00Z",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search snippets, unsourced genealogy, people-finder pages, postwar-only employment leads and sources without an OSS, protected-identifier or personnel-file bridge were rejected. Historical occupation codes, military service, student status and institutional parentheticals were not silently converted into employers.",
                "research_notes": f"{detail} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain, CIA Reading Room-equivalent and Library of Congress searches were checked as applicable. The index page, Army bulk file, technical documentation and occupation-code pages were inspected directly. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": "Review the indexed Box 786 or 787 personnel file for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before wartime service.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b967-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-967-v1",
        "reviewer": "Before OSS Batch 967 evidence review",
        "sources": sources(),
        "organizations": organizations(),
        "affiliations": [occupation_affiliation(item) for item in ARMY_OCCUPATIONS] + specialist_affiliations(),
        "claims": claims(),
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }
    EvidenceBundle.model_validate(bundle)
    OUTPUT.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
