#!/usr/bin/env python3
"""Generate the reviewed Batch 938 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / (
    "research/evidence-page459-john-t-takach-to-max-v-talbot-"
    "review_batch-938_2026-10-28.json"
)

INDEX = "nara-index-b938"
ARMY = "army-bulk-b938"
TECH = "army-tech-b938"
CODES = "army-codes-b938"
TODDY = "toddy-story-b938"
OSS_TRAVEL = "oss-travel-orders-b938"
BHSM = "bhsm-taka-nursery-b938"
AMACHE = "amache-directory-b938"
MISLS = "misls-shiro-takeda-b938"
TOPAZ = "topaz-gene-takei-b938"
MACALESTER = "macalester-gene-takei-b938"
WRA_TAKENO = "wra-roy-takeno-b938"
LOC_ADAMS = "loc-born-free-equal-b938"
EAGLE = "project-eagle-talarek-b938"
POLAND = "poland-exile-talarek-b938"
AFSA = "afsa-jerree-talbot-smith-b938"

PEOPLE = {
    24: ("047fda06-9304-53c6-9437-d5cb32fbb542", "John T Takach"),
    25: ("3baa382a-8c60-5637-9e0f-7cd71386eda3", "Alfred J Takacs"),
    26: ("317f3ad9-e305-56f0-bea0-e34a6dd96ca1", "Kuniyasu Takahashi"),
    27: ("3bbd01d0-97fb-504c-b6d2-62cfa9328e17", "Minekichi Takahashi"),
    28: ("fb335f1e-9687-586f-b536-a50c132cb3b2", "Shigeharu Takahashi"),
    29: ("77cd3c5d-3f74-5f1a-adef-db289f4037af", "Robert S Takakuwa"),
    30: ("880de019-0520-5181-81d2-51aca3ae2365", "William A Takala"),
    31: ("95e3497e-b8db-5e19-99ed-6d006a651eed", "William A Takala"),
    32: ("c27ff5cf-2087-5fb6-957d-db545b5b69e5", "Sakichi Takao"),
    33: ("fa42ca9a-8f36-5778-a2e9-5b9377acc783", "Tadao T Takayanagi"),
    34: ("05108fc5-e7da-5ba3-b52c-ea14c04fd66b", "Tokutaro Takayanagi"),
    35: ("44f1c17b-ad29-5fef-a08a-6d9210fca5d6", "Seiichi Takeda"),
    36: ("5914a559-6eae-5e54-a54b-e32cd04c33c2", "Shiro Takeda"),
    37: ("817240da-d0ea-5603-9ed3-d9074ca881f4", "Gene M Takei"),
    38: ("f984cbc5-1d0a-5a35-8936-bf36d85f1f8f", "Roy M Takeno"),
    39: ("8960fc28-a865-5389-b2a0-0a492e2d84f0", "Haga Takeshi"),
    40: ("0b02acc1-b885-5352-8023-57ec3bbf95a2", "John Tako"),
    41: ("36c9a385-88ce-5b27-8440-500dd6a07976", "Josef Talarek"),
    42: ("37c01a7e-2c83-5edb-bdc6-e7ab29819871", "Hampton Talbot"),
    43: ("f6038c58-22f8-571c-95a3-96f048f958e2", "James F Talbot"),
    44: ("7aadf0d0-3879-50a9-ada4-26e643ff4e29", "Janice Talbot"),
    45: ("44a3dee4-42a3-5bfb-b8a5-9a2c681b0c48", "Jerree Lee S Talbot"),
    46: ("298d6c95-4287-5df1-a39e-f2f38c7dc946", "Max V Talbot"),
}

UNRESOLVED = {
    24: "Exact-name OSS, Army, employment, obituary and archival searches supplied no Box 763 identity bridge.",
    25: "Exact-name and spelling-variant OSS, Army, occupation and archival searches supplied no defensible identity bridge.",
    26: "Exact-name English and Japanese searches produced only modern or unbridged namesakes.",
    27: "The prominent 1858-1925 namesake cannot be the indexed OSS person, and no separate Box 763 identity bridge was found.",
    28: "Two incompatible same-name wartime biographies remain plausible; neither can be assigned without the Box 763 file.",
    29: "A wartime-incarceration article fragment did not supply the full name or an OSS bridge and was not assigned.",
    30: "This row remains separate from the second William A. Takala because the two printed protected identifiers differ; an unrelated Army namesake was rejected.",
    39: "A postwar Japanese American Committee for Democracy name-order lead lacks an OSS or pre-OSS identity bridge.",
    40: "Exact-name OSS, Army, employment, obituary and archival searches supplied no Box 764 identity bridge.",
    42: "Common-name OSS, military, employment, obituary and archival searches supplied no defensible Box 764 identity bridge.",
    43: "Common-name OSS, military, employment, obituary and archival searches supplied no defensible Box 764 identity bridge.",
    44: "Exact-name OSS, employment, obituary, institutional and archival searches supplied no Box 764 identity bridge.",
    46: "Exact-name OSS, military, employment, obituary and archival searches supplied no Box 764 identity bridge.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 763-764",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 459, rows 24-46; checked against layout-preserving text and a 300 dpi page render",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. Full protected identifiers remain private. The next-page boundary was visually checked.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; one accepted Batch 938 identity candidate",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "The accepted match uses a nonshared protected identifier. No raw bulk row or full identifier is included in public output.",
        },
        {
            "key": TECH,
            "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf",
            "archival_identifier": "NN3-064-03-008; National Archives Identifier 1263923",
            "title": "World War II Army Enlistment Records: Reference Copy of Technical Documentation",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives at College Park - Electronic Records",
            "publication_record_date": "1994-2005; reference copy modified 2011",
            "locator": "PDF physical pages 44-46; identifier, name, Army-entry-date, grade and occupation fields",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Used only to interpret selected fields.",
        },
        {
            "key": CODES,
            "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1CL_SD.pdf",
            "archival_identifier": "National Archives Identifier 1263923; Code No. 30",
            "title": "NARA Compiled Code Lists for the Electronic Army Serial Number Merged File",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives at College Park - Electronic Records",
            "publication_record_date": "2011-01-12; modified 2011-03-17",
            "locator": "PDF physical page 171; historical category 1-16 visually checked",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "The historical occupation label identifies neither an employer nor a workplace.",
        },
        {
            "key": TODDY,
            "stable_url": "https://www.youngbuddhisteditorial.com/articles/toddys-story",
            "title": "Toddy's Story",
            "author_creator": "The Young Buddhist Editorial; contributed by Tracy Takayanagi Hui",
            "repository_publisher": "The Young Buddhist Editorial",
            "publication_record_date": "March 2; year not displayed",
            "locator": "Family account based on Tadao Takayanagi's NARA file; student, incarceration, hotel, hospital, tavern and OSS sequence",
            "access_date": "2026-10-28",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Through Our Eyes",
            "rights_notes": "The account is by his daughter and explicitly identifies the family-held NARA evidence. Only short excerpts and project-authored paraphrases are retained.",
        },
        {
            "key": OSS_TRAVEL,
            "stable_url": "https://www.historyofjapaneseinny.org/wp-content/uploads/2024/05/OFFICE-OF-STRATEGIC-SERVICES-1.pdf",
            "archival_identifier": "OSS Headquarters and Headquarters Detachment, corrected Invitational Travel Orders, shipment IJ-B857-HY",
            "title": "Invitational Travel Orders, Shipment IJ-B857-HY",
            "author_creator": "Office of Strategic Services",
            "repository_publisher": "History of Japanese in New York",
            "publication_record_date": "1945-04-30",
            "locator": "PDF physical page 11; Tadao Takayanagi and Seiichi Takeda among named civilian OSS employees",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "Office of Strategic Services records",
            "rights_notes": "The scanned order page was rendered at high resolution and visually inspected.",
        },
        {
            "key": BHSM,
            "stable_url": "https://exhibitsbhs.org/putting-down-roots/",
            "title": "Putting Down Roots: Establishing a Japanese American community in Berkeley",
            "author_creator": "Berkeley Historical Society & Museum",
            "repository_publisher": "Berkeley Historical Society & Museum",
            "locator": "Takayanagi family entry; Taka Nursery and 1920 Sixth Street",
            "access_date": "2026-10-28",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "BHSM Online Exhibits",
            "rights_notes": "The exhibit identifies Tokutaro, Hide, Tadao and the family nursery. It does not establish the OSS entry date.",
        },
        {
            "key": AMACHE,
            "stable_url": "https://digicoll.lib.berkeley.edu/record/174120/files/cubanc_35_1_00260907ta.pdf",
            "archival_identifier": "Bancroft Library digital record 174120",
            "title": "Amache Consumer Enterprises, Inc. directory",
            "author_creator": "Amache Consumer Enterprises, Inc.",
            "repository_publisher": "Bancroft Library, University of California, Berkeley",
            "publication_record_date": "1944",
            "locator": "PDF physical page 9; employees, Office: Takao, Sakichi",
            "access_date": "2026-10-28",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Japanese American Evacuation and Resettlement Records",
            "rights_notes": "The contemporary directory page was visually inspected. The role is presented in the coercive context of wartime incarceration.",
        },
        {
            "key": MISLS,
            "stable_url": "https://www.javadc.org/MISLS%20Registry%2002-02-03.pdf",
            "archival_identifier": "Military Intelligence Service Language School Registry 1941-46, row 8572",
            "title": "Military Intelligence Service Language School Registry 1941-46",
            "author_creator": "Japanese American Veterans Association",
            "repository_publisher": "Japanese American Veterans Association",
            "locator": "Merged PDF page 169 of 418, row 8572; Takeda Shiro, Faculty, Civilian",
            "access_date": "2026-10-28",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Military Intelligence Service registry",
            "rights_notes": "The registry page was visually inspected. It gives no exact appointment or OSS-transfer date.",
        },
        {
            "key": TOPAZ,
            "stable_url": "https://topazstories.com/test-case/",
            "title": "Test Case",
            "author_creator": "Eugene Takei; contributed by Dawn Ishisaki and family; edited by Ruth Sasaki",
            "repository_publisher": "Topaz Stories",
            "publication_record_date": "2021-10-02; updated 2025-03-18",
            "locator": "Family account: Army enlistment, 1942 Fort Leonard Wood assignment and OSS service in Burma",
            "access_date": "2026-10-28",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Topaz Stories",
            "rights_notes": "The account preserves the family history and wartime-incarceration context. Postwar work is not used as pre-OSS evidence.",
        },
        {
            "key": MACALESTER,
            "stable_url": "https://www.macalester.edu/news/2024/02/the-notes-we-shared/",
            "title": "The Notes We Shared",
            "author_creator": "Julie Hessler",
            "repository_publisher": "Macalester College",
            "publication_record_date": "2024-02-16",
            "locator": "1969 class note for Gene M. Takei, class of 1949",
            "access_date": "2026-10-28",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Macalester Today",
            "rights_notes": "Used only as an identity bridge for the middle initial and college association; the postwar employer is excluded.",
        },
        {
            "key": WRA_TAKENO,
            "stable_url": "https://digicoll.lib.berkeley.edu/record/181779/files/cubanc_35_2_01227196ta.pdf",
            "archival_identifier": "Bancroft Library digital record 181779",
            "title": "War Relocation Authority Project Reports Officer letter concerning Roy M. Takeno",
            "author_creator": "Lucy W. Adams, Assistant Project Director, War Relocation Authority",
            "repository_publisher": "Bancroft Library, University of California, Berkeley",
            "publication_record_date": "1944-01-13",
            "locator": "PDF physical page 19; Roy M. Takeno biography and Manzanar Free Press editorship",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "Japanese American Evacuation and Resettlement Records",
            "rights_notes": "The contemporary letter was visually inspected and preserves the incarceration context.",
        },
        {
            "key": LOC_ADAMS,
            "stable_url": "https://tile.loc.gov/storage-services/service/gdc/gdclccn/45/00/29/75/45002975/45002975.pdf",
            "archival_identifier": "Library of Congress Control Number 45002975",
            "title": "Born Free and Equal",
            "author_creator": "Ansel Adams",
            "repository_publisher": "Library of Congress",
            "publication_record_date": "1944",
            "locator": "PDF physical page 54, printed page 53; Roy M. Takeno, Manzanar Office of Reports and Rocky Shimpo",
            "access_date": "2026-10-28",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Library of Congress digitized books",
            "rights_notes": "The contemporary page was visually inspected. Only a short excerpt and project-authored paraphrase are retained.",
        },
        {
            "key": EAGLE,
            "stable_url": "https://www.universitas.com.pl/pl/ksiazki/1167-2123-project-eagle-polscy-wywiadowcy-w-raportach-i-dokumentach-wojennych-amerykanskiego-biura-sluzb-strategicznych.html",
            "archival_identifier": "ISBN 978-83-242-3549-0; printed pages 148-149; NARA RG 226, Entry 210, Box 5, Folder 29",
            "title": "Project Eagle: Polscy wywiadowcy w raportach i dokumentach wojennych amerykańskiego Biura Służb Strategicznych",
            "author_creator": "John S. Micgiel",
            "repository_publisher": "Towarzystwo Autorów i Wydawców Prac Naukowych UNIVERSITAS",
            "publication_record_date": "2019",
            "locator": "Printed pages 148-149; Private Józef Talarek, real name Józef Herzyk, Orange Blossom radio operator",
            "access_date": "2026-10-28",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Project Eagle archival study",
            "rights_notes": "The study cites the underlying NARA file. Forced labor and German conscription are preserved as coercive, not voluntary employment.",
        },
        {
            "key": POLAND,
            "stable_url": "https://polandinexile.com/es/article/continental-action/",
            "title": "Continental Action",
            "author_creator": "Poland in Exile",
            "repository_publisher": "Poland in Exile",
            "locator": "Orange Blossom mission table, 9 April 1945; Sgt. Józef Herzyk (Talarek), W/T operator",
            "access_date": "2026-10-28",
            "source_quality": "D_correlative_or_secondary",
            "collection_name": "Polish wartime operations histories",
            "rights_notes": "Used as corroboration for the alias and mission only; the table cites Micgiel's archival study.",
        },
        {
            "key": AFSA,
            "stable_url": "https://afsa.org/sites/default/files/fsj-1943-09-september_0.pdf",
            "archival_identifier": "American Foreign Service Journal, volume 20, number 9, page 464",
            "title": "The American Foreign Service Journal",
            "author_creator": "American Foreign Service Association",
            "repository_publisher": "American Foreign Service Association",
            "publication_record_date": "1943-09",
            "locator": "PDF physical page 22, printed page 464; Jerree Lee Talbot Smith working in the Office of Censorship",
            "access_date": "2026-10-28",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "American Foreign Service Journal",
            "rights_notes": "The page was visually inspected. The unusual name alignment is probable, not confirmed, pending Box 764 review.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {"key": "army-existing-b938", "organization_id": "28a26f92-78af-5a1a-9c09-a843eb5975b4", "canonical_name": "United States Army", "historical_name": "Army of the United States", "aliases": ["U.S. Army"], "organization_type": "military service", "sector": "military", "country": "United States", "normalization_notes": "Existing canonical organization reused."},
        {"key": "misls-existing-b938", "organization_id": "505260bf-425e-56b6-add8-af85df816a81", "canonical_name": "Military Intelligence Service Language School", "historical_name": "Military Intelligence Service Language School", "aliases": ["MISLS", "MIS Language School"], "organization_type": "United States Army language school", "sector": "military", "city": "Savage", "state_or_region": "Minnesota", "country": "United States", "normalization_notes": "Existing canonical organization reused; the registry describes Shiro Takeda as civilian faculty."},
        {"key": "polish-forces-existing-b938", "organization_id": "8043a812-1527-5eab-af0c-08670108993d", "canonical_name": "Polish Armed Forces in the West", "historical_name": "Polish Army", "aliases": ["Polish Armed Forces"], "organization_type": "allied armed forces", "sector": "military", "country": "Poland", "normalization_notes": "Existing canonical organization reused."},
        {"key": "ucb-existing-b938", "organization_id": "dd5d0a44-0368-5e91-a5d3-074de36840ed", "canonical_name": "University of California, Berkeley", "historical_name": "University of California at Berkeley", "aliases": ["UC Berkeley", "Cal"], "organization_type": "university", "sector": "academia_and_research", "city": "Berkeley", "state_or_region": "California", "country": "United States", "normalization_notes": "Existing canonical organization reused; modeled as student status."},
        {"key": "wra-existing-b938", "organization_id": "c967ec9a-5346-5137-bdbd-18695be3517c", "canonical_name": "War Relocation Authority", "historical_name": "War Relocation Authority", "aliases": ["WRA"], "organization_type": "federal agency", "sector": "federal_government", "country": "United States", "active_dates": "1942-1946", "normalization_notes": "Existing canonical organization reused with explicit wartime-incarceration context."},
        {"key": "university-hospital-ann-arbor-b938", "canonical_name": "University Hospital (Ann Arbor)", "historical_name": "University Hospital", "aliases": [], "organization_type": "teaching hospital", "sector": "medicine_and_public_health", "city": "Ann Arbor", "state_or_region": "Michigan", "country": "United States", "normalization_notes": "The historical name as reported by Tadao Takayanagi's daughter is preserved; no modern successor name is substituted."},
        {"key": "hotel-utah-b938", "canonical_name": "Hotel Utah", "historical_name": "Hotel Utah", "aliases": [], "organization_type": "hotel", "sector": "business_and_industry", "city": "Salt Lake City", "state_or_region": "Utah", "country": "United States", "normalization_notes": "Historical employer name preserved."},
        {"key": "webers-tavern-b938", "canonical_name": "Weber's Tavern", "historical_name": "Weber's Tavern", "aliases": [], "organization_type": "restaurant", "sector": "business_and_industry", "city": "Ann Arbor", "state_or_region": "Michigan", "country": "United States", "normalization_notes": "Historical employer name preserved; no modern successor is assumed."},
        {"key": "taka-nursery-b938", "canonical_name": "Taka Nursery", "historical_name": "Taka Nursery", "aliases": [], "organization_type": "family nursery", "sector": "self_employed", "city": "Berkeley", "state_or_region": "California", "country": "United States", "active_dates": "before 1942", "normalization_notes": "Family home business selling cut flowers; modeled as self-employment."},
        {"key": "amache-consumer-b938", "canonical_name": "Amache Consumer Enterprises, Inc.", "historical_name": "Amache Consumer Enterprises, Inc.", "aliases": ["Amache Cooperative Enterprises"], "organization_type": "consumer cooperative within a wartime incarceration center", "sector": "business_and_industry", "city": "Amache", "state_or_region": "Colorado", "country": "United States", "active_dates": "1942-1945", "normalization_notes": "The organization and employment are presented in the coercive context of wartime incarceration."},
        {"key": "japan-california-daily-b938", "canonical_name": "Japan-California Daily News", "historical_name": "Japan-California Daily News", "aliases": [], "organization_type": "newspaper", "sector": "journalism_and_media", "state_or_region": "California", "country": "United States", "normalization_notes": "Historical newspaper name preserved from the 1944 WRA letter."},
        {"key": "rocky-shimpo-b938", "canonical_name": "Rocky Shimpo", "historical_name": "The Rocky Shimpo", "aliases": [], "organization_type": "newspaper", "sector": "journalism_and_media", "city": "Denver", "state_or_region": "Colorado", "country": "United States", "normalization_notes": "Historical newspaper name preserved."},
        {"key": "office-censorship-b938", "canonical_name": "U.S. Office of Censorship", "historical_name": "Office of Censorship", "aliases": ["United States Office of Censorship"], "organization_type": "federal wartime agency", "sector": "federal_government", "city": "Washington", "state_or_region": "District of Columbia", "country": "United States", "active_dates": "1941-1945", "normalization_notes": "Historical agency name preserved."},
    ]


def affiliation(**kwargs: object) -> dict[str, object]:
    return kwargs


def affiliations() -> list[dict[str, object]]:
    return [
        affiliation(key="william-takala-row31-occupation-b938", person_id=PEOPLE[31][0], occupation="Correspondence clerks", relationship_type="employment", end_date="1942-12-31", date_precision="Civilian occupation at Army entry; beginning and duration are not stated", country="United States", immediate_pre_oss=False, last_civilian_pre_service=False, pre_oss_temporal_basis="strongly_date_bounded", identity_confidence="high_confidence", claim_confidence="medium", source_quality="A_direct_official", publication_status="publish_qualified", research_notes="The official historical category is tied to Army entry. It identifies no employer or workplace and is not promoted to an immediate OSS affiliation."),
        affiliation(key="sakichi-takao-amache-b938", person_id=PEOPLE[32][0], organization_key="amache-consumer-b938", organization_name_as_found="Amache Consumer Enterprises, Inc., Office", role_title="Office employee", occupation="office worker", relationship_type="employment", start_date="1944", end_date="1944", date_precision="Listed in the 1944 directory; exact start, end and OSS-transfer dates are not stated", city="Amache", state_or_region="Colorado", country="United States", immediate_pre_oss=False, last_civilian_pre_service=False, pre_oss_temporal_basis="temporal_relation_uncertain", identity_confidence="probable", claim_confidence="medium", source_quality="B_authoritative_institutional", publication_status="publish_qualified", research_notes="The rare exact name supports a probable match. The role occurred during wartime incarceration and is not promoted to an immediate predecessor without Box 763 evidence."),
        affiliation(key="tadao-takayanagi-ucb-b938", person_id=PEOPLE[33][0], organization_key="ucb-existing-b938", organization_name_as_found="UC Berkeley", role_title="Student", occupation="student", relationship_type="student", end_date="1942", date_precision="Student in 1942; forced to leave before wartime incarceration", city="Berkeley", state_or_region="California", country="United States", immediate_pre_oss=False, last_civilian_pre_service=False, pre_oss_temporal_basis="documented_prewar", identity_confidence="high_confidence", claim_confidence="medium", source_quality="C_reputable_contemporary_or_scholarly", publication_status="publish_qualified", research_notes="Student status is not employment."),
        affiliation(key="tadao-takayanagi-topaz-b938", person_id=PEOPLE[33][0], organization_key="wra-existing-b938", organization_name_as_found="Topaz Relocation Center", role_title="Ambulance driver", occupation="ambulance driver", relationship_type="government_assignment", start_date="1942", end_date="1942-1943", date_precision="After arrival at Topaz and before relocation to Salt Lake City; exact dates not stated", city="Topaz", state_or_region="Utah", country="United States", immediate_pre_oss=False, last_civilian_pre_service=False, pre_oss_temporal_basis="documented_prewar", identity_confidence="high_confidence", claim_confidence="medium", source_quality="C_reputable_contemporary_or_scholarly", publication_status="publish_qualified", research_notes="The role occurred within coercive wartime incarceration and is not presented as ordinary voluntary government employment."),
        affiliation(key="tadao-takayanagi-hotel-utah-b938", person_id=PEOPLE[33][0], organization_key="hotel-utah-b938", organization_name_as_found="Hotel Utah", role_title="Busboy", occupation="busboy", relationship_type="employment", end_date="before Army recruitment", date_precision="After leaving Topaz and before moving to Ann Arbor; exact dates not stated", city="Salt Lake City", state_or_region="Utah", country="United States", immediate_pre_oss=False, last_civilian_pre_service=False, pre_oss_temporal_basis="documented_prewar", identity_confidence="high_confidence", claim_confidence="medium", source_quality="C_reputable_contemporary_or_scholarly", publication_status="publish_qualified", research_notes="Earlier named civilian employer; not treated as the final pre-OSS job."),
        affiliation(key="tadao-takayanagi-university-hospital-b938", person_id=PEOPLE[33][0], organization_key="university-hospital-ann-arbor-b938", organization_name_as_found="University Hospital", role_title="Butcher", occupation="butcher", relationship_type="employment", end_date="before Army recruitment", date_precision="Immediately before visiting the Army recruiting office; exact date not stated", city="Ann Arbor", state_or_region="Michigan", country="United States", immediate_pre_oss=True, last_civilian_pre_service=True, pre_oss_temporal_basis="explicit_immediate", identity_confidence="high_confidence", claim_confidence="medium", source_quality="C_reputable_contemporary_or_scholarly", publication_status="publish_qualified", research_notes="The family account directly sequences this job, an Army recruiting-office visit and his OSS unit. It is the best-supported primary last civilian employer."),
        affiliation(key="tadao-takayanagi-webers-b938", person_id=PEOPLE[33][0], organization_key="webers-tavern-b938", organization_name_as_found="Weber's Tavern", role_title="Second job; role not stated", relationship_type="employment", end_date="before Army recruitment", date_precision="Held as a second Ann Arbor job; exact dates and role are not stated", city="Ann Arbor", state_or_region="Michigan", country="United States", immediate_pre_oss=False, last_civilian_pre_service=False, pre_oss_temporal_basis="strongly_date_bounded", identity_confidence="high_confidence", claim_confidence="medium", source_quality="C_reputable_contemporary_or_scholarly", publication_status="publish_qualified", research_notes="Named concurrent or near-concurrent job; the role is not invented."),
        affiliation(key="tokutaro-takayanagi-taka-nursery-b938", person_id=PEOPLE[34][0], organization_key="taka-nursery-b938", organization_name_as_found="Taka Nursery", role_title="Co-owner and flower grower", occupation="nurseryman; cut-flower grower", relationship_type="self_employment", end_date="1942", date_precision="Family business before forced removal in 1942; exact starting date not stated", city="Berkeley", state_or_region="California", country="United States", immediate_pre_oss=False, last_civilian_pre_service=True, pre_oss_temporal_basis="documented_prewar", identity_confidence="probable", claim_confidence="medium", source_quality="B_authoritative_institutional", publication_status="publish_qualified", research_notes="The institutional exhibit identifies Tokutaro and family members. Box 763 is still needed to prove the transition to OSS."),
        affiliation(key="shiro-takeda-misls-b938", person_id=PEOPLE[36][0], organization_key="misls-existing-b938", organization_name_as_found="Military Intelligence Service Language School", role_title="Civilian faculty member", occupation="language-school faculty", relationship_type="employment", date_precision="Registry covers 1941-1946; exact faculty and OSS-transfer dates are not stated", country="United States", immediate_pre_oss=False, last_civilian_pre_service=False, pre_oss_temporal_basis="temporal_relation_uncertain", identity_confidence="probable", claim_confidence="medium", source_quality="B_authoritative_institutional", publication_status="publish_qualified", research_notes="The exact name and civilian-faculty designation support a probable match, but no protected identifier or OSS date is supplied."),
        affiliation(key="gene-takei-army-b938", person_id=PEOPLE[37][0], organization_key="army-existing-b938", organization_name_as_found="U.S. Army; Fort Leonard Wood", role_title="Private First Class", occupation="soldier", relationship_type="military_assignment", start_date="1941-12-22", end_date="1942-1945", date_precision="Enlisted 1941-12-22; at Fort Leonard Wood in 1942; later spent the war years with OSS in Burma", city="Fort Leonard Wood", state_or_region="Missouri", country="United States", immediate_pre_oss=True, last_civilian_pre_service=False, pre_oss_temporal_basis="strongly_date_bounded", identity_confidence="high_confidence", claim_confidence="medium", source_quality="C_reputable_contemporary_or_scholarly", publication_status="publish_qualified", research_notes="Modeled as a military pathway into OSS, not a civilian employer."),
        affiliation(key="roy-takeno-japan-california-b938", person_id=PEOPLE[38][0], organization_key="japan-california-daily-b938", organization_name_as_found="Japan-California Daily News, English Section", role_title="Editor, English Section", occupation="newspaper editor", relationship_type="employment", end_date="1942", date_precision="Before forced removal in 1942; exact dates not stated", state_or_region="California", country="United States", immediate_pre_oss=False, last_civilian_pre_service=False, pre_oss_temporal_basis="documented_prewar", identity_confidence="probable", claim_confidence="medium", source_quality="A_direct_official", publication_status="publish_qualified", research_notes="Contemporary WRA letter; sequence relative to OSS remains unproved."),
        affiliation(key="roy-takeno-manzanar-b938", person_id=PEOPLE[38][0], organization_key="wra-existing-b938", organization_name_as_found="Manzanar Office of Reports and Manzanar Free Press", role_title="Editor; in charge, Office of Reports", occupation="newspaper editor", relationship_type="government_assignment", start_date="1943", end_date="1944", date_precision="Editor for the preceding year as of 1944-01-13; relocated before the 1944 book was published", city="Manzanar", state_or_region="California", country="United States", immediate_pre_oss=False, last_civilian_pre_service=False, pre_oss_temporal_basis="documented_prewar", identity_confidence="probable", claim_confidence="medium", source_quality="A_direct_official", publication_status="publish_qualified", research_notes="The role is presented within coercive wartime incarceration and is not promoted to immediate pre-OSS without Box 764 evidence."),
        affiliation(key="roy-takeno-rocky-shimpo-b938", person_id=PEOPLE[38][0], organization_key="rocky-shimpo-b938", organization_name_as_found="The Rocky Shimpo", role_title="Editor", occupation="newspaper editor", relationship_type="employment", start_date="1944", end_date="1944-1945", date_precision="Recent relocation to Denver in the 1944 source; exact dates and OSS transition not stated", city="Denver", state_or_region="Colorado", country="United States", immediate_pre_oss=False, last_civilian_pre_service=True, pre_oss_temporal_basis="documented_prewar", identity_confidence="probable", claim_confidence="medium", source_quality="C_reputable_contemporary_or_scholarly", publication_status="publish_qualified", research_notes="Latest named civilian employer in the accessible chronology, but not proven immediately before OSS."),
        affiliation(key="josef-talarek-polish-forces-b938", person_id=PEOPLE[41][0], organization_key="polish-forces-existing-b938", organization_name_as_found="Polish Army; Project Eagle", role_title="Private, later sergeant; wireless operator", occupation="military radio operator", relationship_type="military_assignment", start_date="1944", end_date="1945-04", date_precision="After surrender to the Allies in July 1944 and before the Orange Blossom mission on 1945-04-09", country="United Kingdom", immediate_pre_oss=True, last_civilian_pre_service=False, pre_oss_temporal_basis="strongly_date_bounded", identity_confidence="high_confidence", claim_confidence="high", source_quality="C_reputable_contemporary_or_scholarly", publication_status="published", research_notes="The official index note says Polish Army; the NARA-backed archival study and independent mission history identify the Talarek alias and Project Eagle role. Earlier German service was compulsory and is not modeled as voluntary employment."),
        affiliation(key="jerree-talbot-office-censorship-b938", person_id=PEOPLE[45][0], organization_key="office-censorship-b938", organization_name_as_found="Office of Censorship", role_title="Employee; role not stated", relationship_type="government_assignment", start_date="1943-09", end_date="1943-09", date_precision="Working there when reported in September 1943; exact dates and OSS transition not stated", city="Washington", state_or_region="District of Columbia", country="United States", immediate_pre_oss=False, last_civilian_pre_service=False, pre_oss_temporal_basis="temporal_relation_uncertain", identity_confidence="probable", claim_confidence="medium", source_quality="C_reputable_contemporary_or_scholarly", publication_status="publish_qualified", research_notes="The unusual printed sequence Jerree Lee S Talbot probably corresponds to Jerree Lee Talbot Smith, but Box 764 must confirm the surname ordering."),
    ]


def identity_claim(row: int, text: str, paraphrase: str, assessment: str, temporal: str, quality: str, confidence: str, sources_list: list[dict[str, object]], notes: str) -> dict[str, object]:
    return {"key": f"identity-{slug(PEOPLE[row][1])}-row{row}-b938", "person_id": PEOPLE[row][0], "claim_type": "identity", "claim_text": text, "evidence_paraphrase": paraphrase, "identity_match_assessment": assessment, "temporal_assessment": temporal, "source_quality": quality, "claim_confidence": confidence, "publication_status": "published" if confidence in {"confirmed", "high"} else "publish_qualified", "match_notes": notes, "sources": sources_list}


def affiliation_claim(row: int, key: str, affiliation_key: str, claim_type: str, text: str, paraphrase: str, assessment: str, temporal: str, quality: str, confidence: str, source_keys: list[dict[str, object]], notes: str, excerpt: str | None = None) -> dict[str, object]:
    claim = {"key": key, "person_id": PEOPLE[row][0], "affiliation_key": affiliation_key, "claim_type": claim_type, "claim_text": text, "evidence_paraphrase": paraphrase, "identity_match_assessment": assessment, "temporal_assessment": temporal, "source_quality": quality, "claim_confidence": confidence, "publication_status": "published" if confidence in {"confirmed", "high"} else "publish_qualified", "match_notes": notes, "sources": source_keys}
    if excerpt:
        claim["evidence_excerpt"] = excerpt
    return claim


def claims() -> list[dict[str, object]]:
    result = [
        identity_claim(31, "The second indexed William A Takala row is a high-confidence match to an official Army record dated 31 December 1942.", "The reviewed record agrees in exact full name and through a nonshared protected identifier.", "High confidence from a nonshared protected identifier; the identifier itself is withheld.", "The Army record documents entry on 1942-12-31 but not the OSS transfer date.", "A_direct_official", "high", [{"source_key": INDEX, "locator_override": "PDF page 459 row 31; Box 763; protected identifier withheld"}, {"source_key": ARMY, "locator_override": "Accepted reviewed identity record; Army entry 1942-12-31; protected identifier withheld"}, {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46; field definitions"}], "The same-name row 30 carries a different protected identifier and remains a separate unresolved person."),
        affiliation_claim(31, "occupation-william-takala-row31-b938", "william-takala-row31-occupation-b938", "occupation", "At Army entry on 31 December 1942, this William A. Takala was recorded in the historical category Correspondence clerks; no employer or workplace is identified.", "The accepted Army record carries occupation code 116, decoded from NARA's official code list.", "The category is assigned only to the accepted protected-identifier match.", "Strongly date-bounded to Army entry, but not proven immediately before OSS.", "A_direct_official", "medium", [{"source_key": ARMY, "locator_override": "Army entry 1942-12-31; occupation code 116; protected identifier withheld"}, {"source_key": CODES, "locator_override": "PDF physical page 171; historical category 1-16"}], "Historical language is preserved and not converted into a company or workplace.", "Correspondence clerks"),
        identity_claim(32, "Indexed Sakichi Takao is a probable match to the rare exact-name office employee in the 1944 Amache Consumer Enterprises directory.", "The contemporary directory gives the exact rare name and a compatible wartime institutional role.", "Probable from the rare exact name and compatible wartime chronology; no OSS-specific identifier is supplied.", "The directory dates the role to 1944 but not its sequence relative to OSS.", "B_authoritative_institutional", "medium", [{"source_key": INDEX, "locator_override": "PDF page 459 row 32; Box 763"}, {"source_key": AMACHE, "locator_override": "PDF physical page 9; Employees, Office: Takao, Sakichi"}], "Box 763 remains necessary to confirm identity and the OSS transition."),
        affiliation_claim(32, "prewar-sakichi-takao-amache-b938", "sakichi-takao-amache-b938", "other_pre_oss_affiliation", "A 1944 directory lists Sakichi Takao as an office employee of Amache Consumer Enterprises, Inc.", "The contemporary cooperative directory places the rare exact name in its office staff list.", "Probable identity from the rare exact name; no protected identifier or direct OSS link.", "Documented wartime affiliation; its relation to OSS is uncertain.", "B_authoritative_institutional", "medium", [{"source_key": AMACHE, "locator_override": "PDF physical page 9; office staff list"}], "The employment is qualified and explicitly contextualized within wartime incarceration.", "Takao, Sakichi"),
        identity_claim(33, "Indexed Tadao T Takayanagi is a high-confidence match to Tadao ‘Toddy’ Takayanagi, a civilian OSS employee named in a 1945 travel order and described by his daughter from family-held NARA records.", "A direct OSS order and an independent family account align the rare exact name, Berkeley family and OSS service.", "High confidence from the rare exact name, direct OSS order and daughter-authored NARA-backed chronology.", "The order dates his OSS employment to 1945; the family account supplies the earlier sequence.", "A_direct_official", "high", [{"source_key": INDEX, "locator_override": "PDF page 459 row 33; Box 763"}, {"source_key": OSS_TRAVEL, "locator_override": "PDF physical page 11; civilian OSS employee Tadao Takayanagi"}, {"source_key": TODDY, "locator_override": "Family chronology; daughter and NARA-file provenance"}], "The source spelling and indexed middle initial are preserved."),
        affiliation_claim(33, "prewar-tadao-ucb-b938", "tadao-takayanagi-ucb-b938", "other_pre_oss_affiliation", "Tadao Takayanagi was a UC Berkeley student in 1942 before forced removal.", "His daughter identifies his student status and interruption by wartime incarceration.", "High-confidence identity from the direct OSS order and family source.", "Explicitly before the later jobs and OSS; exact dates are not stated.", "C_reputable_contemporary_or_scholarly", "medium", [{"source_key": TODDY, "locator_override": "Family chronology; UC Berkeley student in 1942"}], "Student status is not classified as employment."),
        affiliation_claim(33, "prewar-tadao-topaz-b938", "tadao-takayanagi-topaz-b938", "other_pre_oss_affiliation", "During incarceration at Topaz, Tadao Takayanagi worked as an ambulance driver.", "The family account directly describes the role before his Salt Lake City relocation.", "High-confidence identity from the direct OSS order and family source.", "Documented before the hotel, hospital and OSS sequence.", "C_reputable_contemporary_or_scholarly", "medium", [{"source_key": TODDY, "locator_override": "Family chronology; Topaz ambulance-driver role"}], "The coercive incarceration setting is explicit; this is not presented as ordinary voluntary government employment."),
        affiliation_claim(33, "prewar-tadao-hotel-utah-b938", "tadao-takayanagi-hotel-utah-b938", "other_pre_oss_affiliation", "After leaving Topaz, Tadao Takayanagi worked as a busboy at Hotel Utah in Salt Lake City.", "The family account names the hotel and role in the sequence before Ann Arbor.", "High-confidence identity from the direct OSS order and family source.", "Documented before the University Hospital job; exact dates are not stated.", "C_reputable_contemporary_or_scholarly", "medium", [{"source_key": TODDY, "locator_override": "Family chronology; Hotel Utah busboy role"}], "Earlier named civilian employer, not the final pre-OSS role."),
        affiliation_claim(33, "immediate-tadao-university-hospital-b938", "tadao-takayanagi-university-hospital-b938", "immediate_pre_oss_affiliation", "Tadao Takayanagi's best-supported immediate pre-OSS civilian employer was University Hospital in Ann Arbor, where he worked as a butcher before visiting the Army recruiting office.", "The family chronology directly sequences the hospital job, recruiting-office visit and later OSS unit.", "High-confidence identity from a direct OSS order and the daughter-authored account.", "Explicit immediate sequence, though the exact recruitment date is unstated.", "C_reputable_contemporary_or_scholarly", "medium", [{"source_key": TODDY, "locator_override": "Family chronology; University Hospital butcher job followed by Army recruiting-office visit"}], "Modeled as both the immediate affiliation and best-supported primary last civilian employer; the separate tavern job remains visible.", "job as a butcher at the University Hospital in Ann Arbor"),
        affiliation_claim(33, "prewar-tadao-webers-b938", "tadao-takayanagi-webers-b938", "other_pre_oss_affiliation", "Tadao Takayanagi also held a second job at Weber's Tavern while in Ann Arbor; the role is not stated.", "The family account names the second employer but supplies no role or exact date.", "High-confidence identity from the direct OSS order and family source.", "Strongly date-bounded to the Ann Arbor period before recruitment; concurrency is not fully stated.", "C_reputable_contemporary_or_scholarly", "medium", [{"source_key": TODDY, "locator_override": "Family chronology; named second Ann Arbor job"}], "No restaurant role is invented."),
        identity_claim(34, "Indexed Tokutaro Takayanagi is a probable match to the Berkeley flower grower who ran Taka Nursery with his wife and was Tadao Takayanagi's father.", "The rare exact name, documented family relationship and adjacent indexed family member support the lead.", "Probable from the rare exact name and independent institutional family history; no direct OSS document names Tokutaro.", "The nursery is documented before forced removal in 1942; the OSS transition remains unknown.", "B_authoritative_institutional", "medium", [{"source_key": INDEX, "locator_override": "PDF page 459 row 34; Box 763"}, {"source_key": BHSM, "locator_override": "Takayanagi family entry; Taka Nursery"}, {"source_key": TODDY, "support_type": "supports", "locator_override": "Tadao's family chronology; father had a flower nursery"}], "Adjacency alone is not treated as proof; Box 763 must confirm the person."),
        affiliation_claim(34, "prewar-tokutaro-taka-nursery-b938", "tokutaro-takayanagi-taka-nursery-b938", "last_civilian_pre_service", "Before forced removal in 1942, Tokutaro and Hide Takayanagi ran Taka Nursery, a Berkeley home business selling cut flowers.", "The Berkeley Historical Society exhibit identifies the couple, business, product and home address.", "Probable identity from the rare exact name and family link; no direct OSS identifier.", "Documented prewar self-employment; immediacy before OSS is not established.", "B_authoritative_institutional", "medium", [{"source_key": BHSM, "locator_override": "Takayanagi family entry; Taka Nursery and 1920 Sixth Street"}], "Qualified as the last documented civilian work, not an asserted immediate OSS predecessor.", "ran the Taka Nursery, selling cut flowers from their home business"),
        identity_claim(35, "Indexed Seiichi Takeda is a high-confidence match to the civilian OSS employee named in the 30 April 1945 overseas travel order.", "The direct OSS order gives the exact name among a small group of civilian employees.", "High confidence from the exact name and direct OSS personnel order; no protected identifier is supplied.", "The order establishes OSS employment by 1945-04-30 but no pre-OSS affiliation.", "A_direct_official", "high", [{"source_key": INDEX, "locator_override": "PDF page 459 row 35; Box 764"}, {"source_key": OSS_TRAVEL, "locator_override": "PDF physical page 11; Seiichi Takeda among named civilian OSS employees"}], "No employer or occupation is inferred before OSS."),
        identity_claim(36, "Indexed Shiro Takeda is a probable match to the civilian faculty member in the Military Intelligence Service Language School registry.", "The institutional registry gives the exact name and civilian-faculty designation.", "Probable from the exact name and compatible wartime intelligence-language context; no protected identifier or OSS reference is supplied.", "The registry spans 1941-1946 and does not date the assignment relative to OSS.", "B_authoritative_institutional", "medium", [{"source_key": INDEX, "locator_override": "PDF page 459 row 36; Box 764"}, {"source_key": MISLS, "locator_override": "Merged PDF page 169, row 8572; Takeda Shiro, Faculty, Civilian"}], "Box 764 remains necessary to confirm identity and chronology."),
        affiliation_claim(36, "prewar-shiro-takeda-misls-b938", "shiro-takeda-misls-b938", "other_pre_oss_affiliation", "The MISLS registry lists Shiro Takeda as civilian faculty at the Military Intelligence Service Language School.", "The institutional row explicitly labels him Faculty and Civilian.", "Probable identity from the exact name and compatible context.", "Wartime affiliation documented, but the sequence relative to OSS is uncertain.", "B_authoritative_institutional", "medium", [{"source_key": MISLS, "locator_override": "Merged PDF page 169, row 8572"}], "Published as a qualified institutional affiliation, not a proven immediate predecessor.", "Faculty ... Civilian"),
        identity_claim(37, "Indexed Gene M Takei is a high-confidence match to Gene Takei, the Army serviceman whose family history states that he served with OSS in Burma.", "The rare name, middle-initial bridge, Army chronology, Macalester association and explicit OSS family history align the person.", "High confidence from the family OSS account and independent Macalester middle-initial identity bridge.", "The sources place him in the Army in 1942, OSS during the war and Macalester after the war.", "C_reputable_contemporary_or_scholarly", "high", [{"source_key": INDEX, "locator_override": "PDF page 459 row 37; Box 764; protected identifier withheld"}, {"source_key": TOPAZ, "locator_override": "Family account; Army enlistment, Fort Leonard Wood and OSS service in Burma"}, {"source_key": MACALESTER, "support_type": "supports", "locator_override": "1969 class note; Gene M. Takei, class of 1949"}], "The postwar employer in the Macalester note is not used as pre-OSS evidence."),
        affiliation_claim(37, "immediate-gene-takei-army-b938", "gene-takei-army-b938", "immediate_pre_oss_affiliation", "Gene Takei's best-supported immediate pre-OSS affiliation was the U.S. Army: he enlisted in December 1941, served as a PFC at Fort Leonard Wood in 1942, and later served with OSS in Burma.", "The family account supplies the Army-to-OSS chronology and specific 1942 assignment.", "High-confidence identity from the family OSS history and institutional middle-initial bridge.", "Strongly date-bounded military pathway; no separate transfer date is stated.", "C_reputable_contemporary_or_scholarly", "medium", [{"source_key": TOPAZ, "locator_override": "Family account; Fort Leonard Wood in 1942 and later OSS service in Burma"}], "Modeled as a military assignment, not a civilian employer.", "PFC Gene Takei was stationed at Fort Leonard Wood in Missouri"),
        identity_claim(38, "Indexed Roy M Takeno is a probable match to Roy M. Takeno, the contemporary WRA editor whose wartime newspaper career is documented by official and Library of Congress sources.", "The rare exact name and middle initial align across the index and two contemporary sources.", "Probable from the rare exact name and middle initial; the sources do not mention OSS or a protected identifier.", "The sources date the journalism sequence to 1942-1944, but not the OSS transition.", "A_direct_official", "medium", [{"source_key": INDEX, "locator_override": "PDF page 459 row 38; Box 764"}, {"source_key": WRA_TAKENO, "locator_override": "PDF physical page 19; exact name, education and newspaper chronology"}, {"source_key": LOC_ADAMS, "support_type": "supports", "locator_override": "PDF physical page 54; Manzanar and Rocky Shimpo chronology"}], "Box 764 is needed for a direct identity and OSS chronology bridge."),
        affiliation_claim(38, "prewar-roy-takeno-japan-california-b938", "roy-takeno-japan-california-b938", "other_pre_oss_affiliation", "Before forced removal in 1942, Roy M. Takeno edited the English Section of the Japan-California Daily News.", "A contemporary WRA letter explicitly names the role and newspaper.", "Probable identity from the rare exact name and middle initial.", "Explicitly before forced removal, but not proven immediately before OSS.", "A_direct_official", "medium", [{"source_key": WRA_TAKENO, "locator_override": "PDF physical page 19; pre-evacuation newspaper role"}], "Qualified until Box 764 connects the editor directly to the index person.", "before evacuation editor of the English Section"),
        affiliation_claim(38, "prewar-roy-takeno-manzanar-b938", "roy-takeno-manzanar-b938", "other_pre_oss_affiliation", "In 1943-1944 Roy M. Takeno edited the Manzanar Free Press and directed the War Relocation Authority's Office of Reports at Manzanar.", "The WRA letter names him as Free Press editor; the contemporary book identifies his Office of Reports direction.", "Probable identity from the rare exact name and middle initial in two contemporary sources.", "Documented wartime role; its relation to OSS is uncertain.", "A_direct_official", "medium", [{"source_key": WRA_TAKENO, "locator_override": "PDF physical page 19; Manzanar Free Press editorship"}, {"source_key": LOC_ADAMS, "locator_override": "PDF physical page 54; Office of Reports direction"}], "The coercive incarceration setting is explicit and the role is not promoted to immediate pre-OSS."),
        affiliation_claim(38, "prewar-roy-takeno-rocky-shimpo-b938", "roy-takeno-rocky-shimpo-b938", "last_civilian_pre_service", "By 1944 Roy M. Takeno had relocated to Denver as editor of The Rocky Shimpo.", "A contemporary source directly identifies the move and newspaper role.", "Probable identity from the rare exact name and middle initial.", "Latest named civilian employer in the accessible chronology, but not proven immediately before OSS.", "C_reputable_contemporary_or_scholarly", "medium", [{"source_key": LOC_ADAMS, "locator_override": "PDF physical page 54, printed page 53; Rocky Shimpo role"}], "Qualified last documented civilian employer; Box 764 is needed for the OSS sequence.", "relocation in Denver ... as editor of The Rocky Shimpo"),
        identity_claim(41, "Indexed Josef Talarek is a high-confidence match to Polish Project Eagle radio operator Józef Herzyk, who served under the name Józef Talarek.", "The archival study explicitly identifies the Talarek alias, and an independent mission history corroborates it.", "High confidence from the exact alias, index Polish Army note, role, age and NARA-backed Project Eagle record.", "The sources place him in Polish/OSS preparation after July 1944 and on the Orange Blossom mission in April 1945.", "C_reputable_contemporary_or_scholarly", "high", [{"source_key": INDEX, "locator_override": "PDF page 459 row 41; Box 764; printed note Polish Ar"}, {"source_key": EAGLE, "locator_override": "Printed pages 148-149; Private Józef Talarek, real name Józef Herzyk"}, {"source_key": POLAND, "support_type": "supports", "locator_override": "Orange Blossom mission table; 9 April 1945"}], "Józef Herzyk is preserved as a documented real-name variant; earlier German service was compulsory."),
        affiliation_claim(41, "immediate-josef-talarek-polish-forces-b938", "josef-talarek-polish-forces-b938", "immediate_pre_oss_affiliation", "Józef Herzyk, serving as Józef Talarek, entered the OSS-linked Project Eagle pathway through the Polish Armed Forces in the West and served as the Orange Blossom wireless operator.", "The official index note, NARA-backed archival study and mission history align the Polish military and OSS operational sequence.", "High-confidence alias match supported by the official index, NARA-backed scholarship and corroborative mission history.", "Strongly date-bounded after his July 1944 surrender and before the April 1945 OSS mission.", "C_reputable_contemporary_or_scholarly", "high", [{"source_key": INDEX, "locator_override": "PDF page 459 row 41; printed Polish Army note"}, {"source_key": EAGLE, "locator_override": "Printed pages 148-149; alias, rank and radio-operator role"}, {"source_key": POLAND, "support_type": "supports", "locator_override": "Orange Blossom mission table"}], "Modeled as an Allied military assignment, not a civilian employer.", "Sgt. Józef Herzyk (Talarek) W/T operator"),
        identity_claim(45, "Indexed Jerree Lee S Talbot is a probable match to Jerree Lee Talbot Smith, who was working in the U.S. Office of Censorship in 1943.", "The unusual four-part indexed sequence aligns closely with the equally unusual full name in a contemporary institutional journal.", "Probable, not confirmed: the index may have transposed or truncated the surname ordering, and Box 764 must resolve it.", "The journal dates the government role to September 1943 but not its relation to OSS.", "C_reputable_contemporary_or_scholarly", "medium", [{"source_key": INDEX, "locator_override": "PDF page 459 row 45; Box 764; printed as Talbot, Jerree Lee, S"}, {"source_key": AFSA, "locator_override": "PDF physical page 22, printed page 464; Jerree Lee Talbot Smith"}], "The full source name is a variant lead, not a silent correction of the index."),
        affiliation_claim(45, "prewar-jerree-talbot-censorship-b938", "jerree-talbot-office-censorship-b938", "other_pre_oss_affiliation", "A September 1943 Foreign Service journal reported Jerree Lee Talbot Smith working in the U.S. Office of Censorship in Washington.", "The contemporary journal names the person, agency and city.", "Probable alignment to indexed Jerree Lee S Talbot; surname ordering remains unresolved.", "Documented wartime government assignment; the sequence relative to OSS is uncertain.", "C_reputable_contemporary_or_scholarly", "medium", [{"source_key": AFSA, "locator_override": "PDF physical page 22, printed page 464"}], "Published only as a qualified affiliation pending Box 764 confirmation.", "is working in the Office of Censorship in Washington"),
    ]
    return result


def archival_update(row: int, reason: str) -> dict[str, object]:
    person_id, name = PEOPLE[row]
    box = "763" if row <= 34 else "764"
    status = "ambiguous" if row in {28, 39} else "unresolved"
    priority = "critical" if status == "ambiguous" else "high"
    update: dict[str, object] = {
        "person_id": person_id,
        "identity_status": status,
        "identity_evidence": f"The visually verified index row supplies {name}, Box {box} and archive location 230/86/41/06. {reason}",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": f"Review Box {box} for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": priority,
    }
    if row in {30}:
        update["possible_duplicate_group"] = "page459-william-a-takala-rows30-31"
        update["next_action"] = "Review both William A. Takala files in Box 763. Keep the rows separate because their protected identifiers differ."
    return update


def person_updates() -> list[dict[str, object]]:
    updates = [archival_update(row, reason) for row, reason in UNRESOLVED.items()]
    updates.extend([
        {"person_id": PEOPLE[31][0], "identity_status": "high_confidence", "identity_evidence": "A nonshared protected identifier connects the visually verified second William A. Takala row to the reviewed official Army record. The occupation field remains separate from employer claims.", "personnel_category": "enlisted_army_personnel", "commissioned_officer": False, "allied_or_foreign_personnel": False, "manual_review_required": True, "possible_duplicate_group": "page459-william-a-takala-rows30-31", "research_status": "occupation_only_found", "next_action": "Review both Box 763 files for the immediate pre-OSS affiliation; do not merge the two rows because their protected identifiers differ.", "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "high"},
        {"person_id": PEOPLE[32][0], "identity_status": "probable", "identity_evidence": "A visually inspected 1944 institutional directory lists the rare exact name Sakichi Takao as an Amache Consumer Enterprises office employee, but supplies no OSS-specific identifier.", "manual_review_required": True, "research_status": "needs_temporal_review", "next_action": "Review Box 763 to confirm identity and determine whether the Amache office role preceded OSS directly.", "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "high"},
        {"person_id": PEOPLE[33][0], "identity_status": "high_confidence", "identity_evidence": "A direct 1945 OSS civilian travel order and daughter-authored chronology based on the family NARA file align the rare exact name, Berkeley family and OSS service.", "name_variants": ["Tadao Toddy Takayanagi"], "personnel_category": "civilian_professional_or_administrative_grade", "commissioned_officer": False, "allied_or_foreign_personnel": False, "manual_review_required": True, "research_status": "verified_employer_found", "next_action": "Review Box 763 for exact employment and recruitment dates and whether Weber's Tavern overlapped University Hospital at Army entry.", "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "medium"},
        {"person_id": PEOPLE[34][0], "identity_status": "probable", "identity_evidence": "The rare exact name and institutional Takayanagi family history identify Tokutaro as Tadao's father and co-operator of Taka Nursery, but no direct OSS record names him.", "manual_review_required": True, "research_status": "documented_prewar_employer_found", "next_action": "Review Box 763 to confirm identity and the transition from Taka Nursery or an intervening wartime affiliation to OSS.", "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "high"},
        {"person_id": PEOPLE[35][0], "identity_status": "high_confidence", "identity_evidence": "A visually inspected direct OSS travel order names Seiichi Takeda among civilian OSS employees in April 1945.", "personnel_category": "civilian_professional_or_administrative_grade", "commissioned_officer": False, "allied_or_foreign_personnel": False, "manual_review_required": True, "research_status": "requires_archival_review", "next_action": "Review Box 764 for his identity details, pre-OSS employer and OSS recruitment chronology.", "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "high"},
        {"person_id": PEOPLE[36][0], "identity_status": "probable", "identity_evidence": "The exact name and Civilian Faculty designation in a visually inspected MISLS registry row support a probable identity, but no protected identifier or OSS link is supplied.", "personnel_category": "civilian_professional_or_administrative_grade", "commissioned_officer": False, "manual_review_required": True, "research_status": "needs_temporal_review", "next_action": "Review Box 764 and MISLS personnel records for exact faculty dates and any direct transfer to OSS.", "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "high"},
        {"person_id": PEOPLE[37][0], "identity_status": "high_confidence", "identity_evidence": "The rare name and Macalester middle-initial bridge align with a family history that explicitly documents Army enlistment, Fort Leonard Wood and OSS service in Burma.", "name_variants": ["Eugene Takei", "Mamoru Sasaki"], "personnel_category": "enlisted_army_personnel", "commissioned_officer": False, "allied_or_foreign_personnel": False, "manual_review_required": True, "research_status": "completed", "next_action": "Review Box 764 for the exact Army-to-OSS transfer date, Burma assignment and last civilian employer before enlistment.", "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "medium"},
        {"person_id": PEOPLE[38][0], "identity_status": "probable", "identity_evidence": "Two contemporary sources identify the rare exact name and middle initial and document a coherent 1942-1944 newspaper chronology, but neither mentions OSS.", "manual_review_required": True, "research_status": "documented_prewar_employer_found", "next_action": "Review Box 764 to confirm identity, determine whether Rocky Shimpo immediately preceded OSS, and document his OSS entry date.", "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "high"},
        {"person_id": PEOPLE[41][0], "identity_status": "high_confidence", "identity_evidence": "NARA-backed scholarship explicitly identifies Private Józef Talarek as Józef Herzyk; the index's Polish Army note and an independent Orange Blossom mission history corroborate the alias and OSS-linked role.", "name_variants": ["Józef Talarek", "Józef Herzyk", "Josef Herzyk"], "personnel_category": "foreign_or_allied_military_personnel", "commissioned_officer": False, "allied_or_foreign_personnel": True, "manual_review_required": True, "research_status": "completed", "next_action": "Review Box 764 and the cited RG 226 Entry 210 folder for enlistment and Project Eagle training dates and any civilian work before forced labor and conscription.", "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "medium"},
        {"person_id": PEOPLE[45][0], "identity_status": "probable", "identity_evidence": "The unusual indexed sequence Jerree Lee S Talbot closely aligns with contemporary Jerree Lee Talbot Smith, but the surname ordering remains unresolved without Box 764.", "name_variants": ["Jerree Lee Talbot Smith"], "personnel_category": "civilian_professional_or_administrative_grade", "commissioned_officer": False, "manual_review_required": True, "research_status": "needs_temporal_review", "next_action": "Review Box 764 to confirm the surname ordering, Office of Censorship identity and sequence into OSS.", "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "critical"},
    ])
    return updates


def research_attempts() -> list[dict[str, object]]:
    substantive = {
        31: ("source_reviewed", 8, 3, "A nonshared protected identifier supports a high-confidence Army identity bridge and dated occupation-only evidence."),
        32: ("source_reviewed", 10, 4, "A contemporary directory supports a probable Amache cooperative office role with explicit incarceration context."),
        33: ("source_reviewed", 13, 3, "A direct OSS travel order and family NARA-backed chronology support a high-confidence identity and explicit University Hospital-to-recruitment sequence."),
        34: ("source_reviewed", 11, 4, "An institutional family history supports a probable Taka Nursery self-employment claim; the OSS transition remains unproved."),
        35: ("source_reviewed", 9, 4, "A direct OSS travel order confirms civilian OSS employment but no reliable pre-OSS affiliation was found."),
        36: ("source_reviewed", 10, 4, "An institutional registry supports a probable civilian MISLS faculty affiliation with unresolved chronology."),
        37: ("source_reviewed", 11, 3, "Family and institutional sources support a high-confidence Army-to-OSS pathway and preserve incarceration context."),
        38: ("source_reviewed", 13, 4, "Two contemporary sources document a probable 1942-1944 newspaper chronology; Box 764 is needed for the OSS bridge."),
        41: ("source_reviewed", 12, 3, "NARA-backed scholarship and a corroborative mission history support a high-confidence Talarek/Herzyk alias and Polish military pathway."),
        45: ("source_reviewed", 10, 5, "A contemporary institutional journal supports a probable Office of Censorship affiliation, but surname ordering and chronology require Box 764."),
    }
    attempts = []
    for row in sorted(PEOPLE):
        person_id, name = PEOPLE[row]
        box = "763" if row <= 34 else "764"
        if row in UNRESOLVED:
            outcome, reviewed, rejected, detail = "no_result", 7, 4, UNRESOLVED[row]
        else:
            outcome, reviewed, rejected, detail = substantive[row]
        attempts.append({
            "key": f"page459-row{row}-{slug(name)}-b938",
            "person_id": person_id,
            "source_adapter": "manual_staged_protocol",
            "query_text": f"{name}; NARA index and public Archives context; CIA Reading Room site-restricted exact-name discovery; OSS and spelling variants; employer and occupation 1940; obituary, institutional, newspaper, Library of Congress and archival searches; Box {box}; protected-identifier Army crosswalk where defensible",
            "query_variant_type": "staged_identity_employment_archival_protocol_batch_938",
            "started_at": "2026-10-28T05:35:00Z",
            "completed_at": "2026-10-28T07:10:00Z",
            "outcome": outcome,
            "sources_reviewed": reviewed,
            "candidate_sources_rejected": rejected,
            "rejection_reasons": "Unbridged namesakes, search snippets, family-tree assertions, modern people-finder pages, postwar-only leads and sources without an OSS, protected-identifier or Box-file bridge were not assigned. Grouped CIA Reading Room exact-name checks produced no additional defensible person-specific result.",
            "research_notes": f"{detail} The index page and every admitted PDF page were visually checked. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA Catalog API call was made.",
            "next_action": f"Review Box {box} for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before military service.",
            "attempt_number": 1,
            "research_agent_version": "before-oss-b938-v1",
        })
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-938-v1",
        "reviewer": "Before OSS Batch 938 evidence review",
        "sources": sources(),
        "organizations": organizations(),
        "affiliations": affiliations(),
        "claims": claims(),
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }
    OUTPUT.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
