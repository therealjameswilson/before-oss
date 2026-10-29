#!/usr/bin/env python3
"""Generate the reviewed Batch 958 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page469-gordon-r-tobin-to-page470-n-s-tokutaro-"
    "review_batch-958_2026-10-29.json"
)

INDEX = "nara-index-b958"
ARMY = "army-bulk-b958"
TECH = "army-tech-b958"
CODES = "army-codes-b958"
APSR_OWI = "apsr-irwin-tobin-owi-b958"
APSR_POST = "apsr-irwin-tobin-postwar-b958"
TOBROCKE = "indystar-floyd-tobrocke-b958"
SCU_TODA = "scu-honey-toda-letter-b958"
MANZANAR_FP = "manzanar-free-press-honey-toda-b958"
UMD_TODA = "umd-honey-toda-commencement-b958"
HOUSE_TODD = "house-paul-todd-b958"
FRUS_TODOROVIC = "frus-borislav-todorovich-b958"
ZNACI_TODOROVIC = "znaci-borislav-todorovic-b958"
DENSHO_SLOCUM = "densho-tokutaro-slocum-b958"

PEOPLE = {
    "469-24": ("07e04072-b55c-5389-be3d-3380b27391d3", "Gordon R Tobin"),
    "469-25": ("31bf8dc1-da43-5fdf-8895-d318f1004945", "Irwin M Tobin"),
    "469-26": ("0791692f-1f8a-58df-8039-81eb59f48a15", "John D Tobin"),
    "469-27": ("3bf1f8cb-412a-51d1-b8dc-db4d35062c57", "Robert P Tobin"),
    "469-28": ("9e5c54a0-ce0e-5216-92d5-5c44212b079b", "Floyd C Tobrocke"),
    "469-29": ("7266d744-4bba-551f-bd82-c432e8f0e8ee", "Gerard A Toby"),
    "469-30": ("c7cb1281-ced3-5596-969f-01d3db991c78", "John Tocarsic"),
    "469-31": ("128b53e8-fb1f-5daf-bdf7-918120fb3430", "Francis Tocci"),
    "469-32": ("8becc7a0-8fd1-51c8-8810-1d90799619ce", "Honey M Toda"),
    "469-33": ("464c9397-7c2e-5a4d-9822-c823b5b75910", "Arthur F Todd"),
    "469-34": ("9dcb4274-c36c-56cc-88bc-33b7720d0458", "Frederick P Todd"),
    "469-35": ("bf7424eb-dca8-551b-8f2a-e619370bd8a7", "Harvey A Todd"),
    "469-36": ("85cccea5-b404-540a-b6ec-baab298bdf08", "Howard F Todd"),
    "469-37": ("92548794-93f5-5dca-af1b-35b2f525a5f5", "Letha M Todd"),
    "469-38": ("06b1dfe4-e894-51d9-ac0d-46570074ef6f", "Luella A Todd"),
    "469-39": ("1b3d60c5-adc1-5f23-9122-f560d75bb44a", "Millard H Todd"),
    "469-40": ("63bf5fdb-dfd5-5bef-ba43-c599b2af1cb8", "Paul H Todd"),
    "469-41": ("9ec01f9d-7e3e-5949-b3cd-dd0baa9608f2", "Paul H Todd"),
    "469-42": ("b4eb53ab-f457-5032-a8e3-68ad1c21cff1", "Suzanne Todd"),
    "469-43": ("108625da-e49b-58e7-be3a-ad169b3911e6", "Borislav J Todorovic"),
    "469-45": ("0d36d7ab-ff22-5c46-a366-1f499e9784a1", "Stewart T Togans"),
    "469-46": ("99cbe6e1-6cc3-523b-8465-af3561438325", "Frances J Togliavia"),
    "470-1": ("e9fbb26c-883f-5f49-af50-c25d256c66d9", "N S Tokutaro"),
}

UNRESOLVED = {
    "469-24": "Exact-name and meaningful-variant searches found no second identifier or Box 779 bridge.",
    "469-26": "A common-name search produced multiple military and civilian namesakes but no defensible Box 779 or OSS bridge.",
    "469-27": "An architect with the same name and other namesakes were rejected because no source connects them to Box 779 or OSS.",
    "469-30": "A rare-name postwar Navy radio technician is plausible, but the accessible Navy evidence does not establish that he is the indexed Box 780 person or identify a pre-OSS affiliation.",
    "469-31": "Common-name, official-domain, obituary, directory and employment searches produced no defensible Box 780 identity bridge.",
    "469-34": "A prominent military historian with the same name was not assigned because the accessible biography lacks a private-identifier, Box 780 or direct OSS bridge.",
    "469-35": "Exact-name and protected-number searches produced no reliable identity or pre-OSS affiliation.",
    "469-36": "Multiple exact-name candidates were rejected because none supplies two corroborating identifiers beyond the common name.",
    "469-37": "Exact-name, variant, obituary, institutional, newspaper and archival searches produced no defensible identity bridge.",
    "469-38": "Exact-name, variant, obituary, institutional, newspaper and archival searches produced no defensible identity bridge.",
    "469-39": "The official Army bulk file contains no matching protected identifier, and exact-name searches produced no defensible alternative.",
    "469-40": "This row has a different printed private identifier from row 41. It remains separate and unresolved; Paul Harold Todd Jr. is assigned only to row 41.",
    "469-42": "A common-name search produced numerous namesakes but no defensible OSS or Box 780 bridge.",
    "469-45": "Exact-name and variant searches produced no reliable identity or pre-OSS affiliation.",
    "469-46": "The printed Togliavia spelling and plausible variants produced no reliable identity or pre-OSS affiliation.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def page_row(key: str) -> tuple[int, int]:
    page, row = key.split("-")
    return int(page), int(row)


def archive_box(key: str) -> str:
    page, row = page_row(key)
    return "779" if page == 469 and row <= 27 else "780"


def person(key: str) -> tuple[str, str]:
    return PEOPLE[key]


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 779-780",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 469, rows 24-43 and 45-46, plus page 470 row 1; checked against layout-preserving text and 220 dpi page renders",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "The 23 researched rows remain separate. Hans V Tofte at page 469 row 44 was already completed and was not overwritten. Full private identifiers remain excluded from public data.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; three accepted Batch 958 protected-identifier candidates; one nonhit; identifiers withheld",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "No raw bulk row, record ordinal or full private identifier enters the evidence bundle or public assets. The downloaded local file was hash-verified and remains outside version control.",
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
            "rights_notes": "Used only to interpret selected fields; coding limits, source damage and incomplete coverage remain applicable.",
        },
        {
            "key": CODES,
            "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1CL_SD.pdf",
            "archival_identifier": "National Archives Identifier 1263923; Code No. 30",
            "title": "NARA Compiled Code Lists for the Electronic Army Serial Number Merged File",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives at College Park - Electronic Records",
            "publication_record_date": "2011-01-12; modified 2011-03-17",
            "locator": "PDF physical pages 172 and 178; historical categories 1-01, 5-83 and 9-92 visually and textually checked",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical categories are qualified and never converted into named employers, workplaces, schools or exact modern job titles.",
        },
        {
            "key": APSR_OWI,
            "stable_url": "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/E1A0F5E785E5BFD90CEE70E41D3EB7EC/S0003055400049327a.pdf/personal_and_miscellaneous.pdf",
            "archival_identifier": "DOI 10.1017/S0003055400049327",
            "title": "Personal and Miscellaneous",
            "author_creator": "Frederic A. Ogg",
            "repository_publisher": "American Political Science Review; Cambridge University Press",
            "publication_record_date": "1945",
            "locator": "Printed page 993; Irwin M. Tobin on leave from Rhode Island State College as an Office of War Information information specialist in England",
            "access_date": "2026-10-29",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "American Political Science Review",
            "rights_notes": "Only citation metadata, a short excerpt and project-authored paraphrase are retained.",
        },
        {
            "key": APSR_POST,
            "stable_url": "https://www.cambridge.org/core/journals/american-political-science-review/article/personal-and-miscellaneous/93564C8D286B89DFFF8210C9A0C8BB9D",
            "archival_identifier": "DOI 10.1017/S0003055400050450",
            "title": "Personal and Miscellaneous",
            "author_creator": "Frederic A. Ogg",
            "repository_publisher": "American Political Science Review; Cambridge University Press",
            "publication_record_date": "1946-02",
            "locator": "Volume 40, issue 1, printed page 126; Office of War Information followed by Office of Strategic Services",
            "access_date": "2026-10-29",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "American Political Science Review",
            "rights_notes": "The contemporary notice explicitly orders OWI before OSS and names Tobin's academic position. Only a short excerpt and paraphrase are retained.",
        },
        {
            "key": TOBROCKE,
            "stable_url": "https://www.legacy.com/us/obituaries/indystar/name/floyd-tobrocke-obituary?id=48778856",
            "title": "Floyd Tobrocke Obituary",
            "author_creator": None,
            "repository_publisher": "The Indianapolis Star via Legacy.com",
            "publication_record_date": "2003-12-12",
            "locator": "Obituary identifying Floyd C. Tobrocke, Army captain and 1940 University of Illinois graduate",
            "access_date": "2026-10-29",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "The Indianapolis Star obituaries",
            "rights_notes": "Later teaching is used only as identity context; it is not projected backward as pre-OSS employment.",
        },
        {
            "key": SCU_TODA,
            "stable_url": "https://dh.scu.edu/exhibits/items/show/3902",
            "title": "Correspondence from Honey Toda to Betty Salzman, July 26, 1942",
            "author_creator": "Honey Toda",
            "repository_publisher": "Kennedy Library Online Archive; Santa Clara University Digital Exhibits",
            "publication_record_date": "1942-07-26",
            "locator": "Item metadata and letter description placing Honey Toda at Manzanar in July 1942",
            "access_date": "2026-10-29",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Civil Rights - Fall 2023",
            "rights_notes": "The letter supplies identity and chronology context only; no complete letter text is republished.",
        },
        {
            "key": MANZANAR_FP,
            "stable_url": "https://ddr.densho.org/ddr-densho-125-307/",
            "archival_identifier": "ddr-densho-125-307",
            "title": "Manzanar Free Press, Volume 6, Number 63",
            "author_creator": "Manzanar Free Press editorial staff",
            "repository_publisher": "Manzanar Relocation Center; digitized by Densho Digital Repository",
            "publication_record_date": "1945-01-27",
            "locator": "Page 2, 'Former Resident Receive High Honors'",
            "access_date": "2026-10-29",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Manzanar Free Press Collection",
            "rights_notes": "The contemporary notice documents Manzanar school-office work and University of Maryland study and clerical work. Short excerpts only.",
        },
        {
            "key": UMD_TODA,
            "stable_url": "https://archive.hshsl.umaryland.edu/bitstream/handle/10713/3875/1938-1948.pdf",
            "archival_identifier": "UMB Digital Archive handle 10713/3875",
            "title": "University of Maryland commencement programs, 1938-1948",
            "author_creator": "University of Maryland",
            "repository_publisher": "University of Maryland; UMB Digital Archive",
            "publication_record_date": "1938-1948",
            "locator": "College of Arts and Sciences Bachelor of Arts candidates and College Park First Honors list; Honey Mitsuye Toda",
            "access_date": "2026-10-29",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "University of Maryland commencement programs",
            "rights_notes": "Institutional program metadata and a project-authored paraphrase only.",
        },
        {
            "key": HOUSE_TODD,
            "stable_url": "https://history.house.gov/People/Listing/T/TODD,-Paul-Harold,-Jr--(T000294)/",
            "archival_identifier": "Biographical Directory identifier T000294",
            "title": "TODD, Paul Harold, Jr.",
            "author_creator": "Office of the Historian and Office of Art and Archives",
            "repository_publisher": "U.S. House of Representatives",
            "publication_record_date": None,
            "locator": "Concise biography: Cornell B.S. 1942; U.S. Army Signal Corps and Office of Strategic Services, 1942-1945",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "History, Art & Archives, U.S. House of Representatives",
            "rights_notes": "Later political and business careers are excluded from pre-OSS claims.",
        },
        {
            "key": FRUS_TODOROVIC,
            "stable_url": "https://history.state.gov/historicaldocuments/frus1944v04/d1304",
            "archival_identifier": "FRUS 1944, Europe, Volume IV, document 1304; 860H.01/9-1644",
            "title": "The Secretary of State to the United States Political Adviser on the Staff of the Supreme Allied Commander, Mediterranean Theater",
            "author_creator": "United States Department of State",
            "repository_publisher": "Office of the Historian, United States Department of State",
            "publication_record_date": "1944-09-23",
            "locator": "Pages 1408-1410 and footnotes; Capt. Borislav Todorovich, Assistant Military Attaché at the Yugoslav Embassy in Washington",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "Foreign Relations of the United States",
            "rights_notes": "The official document establishes a 1944 Royal Yugoslav military and embassy assignment, not an exact OSS entry date.",
        },
        {
            "key": ZNACI_TODOROVIC,
            "stable_url": "https://znaci.org/00001/4_14_3_42.htm",
            "archival_identifier": "Zbornik dokumenata Vojnoistorijskog instituta, Tom XIV, Knjiga 3, document 654",
            "title": "Documents of the Military History Institute, Volume XIV, Book 3",
            "author_creator": "Yugoslav Military History Institute, document compilation",
            "repository_publisher": "Znaci.net digital collection",
            "publication_record_date": "1943-11-13 document; later compilation",
            "locator": "Document 654; Capt. Bora Todorovic accompanies U.S. officers Albert Seitz and Walter Mansfield through Yugoslav corps",
            "access_date": "2026-10-29",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "World War II document collection",
            "rights_notes": "Used with official FRUS and the OSS index; it supports liaison context but not a named civilian employer.",
        },
        {
            "key": DENSHO_SLOCUM,
            "stable_url": "https://encyclopedia.densho.org/Tokutaro_Slocum/",
            "title": "Tokutaro Slocum",
            "author_creator": "Brian Niiya",
            "repository_publisher": "Densho Encyclopedia",
            "publication_record_date": "2020-07-29 update",
            "locator": "Biography; citizenship campaign, JACL and Anti-Axis Committee activity, Manzanar chronology, and later OSS Far East Intelligence Section work",
            "access_date": "2026-10-29",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Densho Encyclopedia",
            "rights_notes": "The source supports an unusual component-order correction: indexed N S Tokutaro corresponds to Tokutaro Nishimura Slocum. No sensitive family details are retained.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {"key": "org-owi-b958", "organization_id": "c48b74b9-1a67-5480-bb47-8dd73d10abf4", "canonical_name": "Office of War Information", "historical_name": "Office of War Information", "aliases": ["OWI"], "organization_type": "federal agency", "sector": "federal_government", "country": "United States", "active_dates": "1942-1945", "normalization_notes": "Wartime federal information agency; not conflated with OSS."},
        {"key": "org-rhode-island-state-b958", "canonical_name": "Rhode Island State College", "historical_name": "Rhode Island State College", "aliases": ["Rhode Island State"], "organization_type": "college", "sector": "academia_and_research", "city": "Kingston", "state_or_region": "Rhode Island", "country": "United States", "active_dates": "1892-1951 under this name", "normalization_notes": "Historical name preserved; later University of Rhode Island is not substituted."},
        {"key": "org-uillinois-b958", "organization_id": "43e2ed32-130f-5604-9973-b99d09d4c8be", "canonical_name": "University of Illinois", "historical_name": "University of Illinois", "aliases": [], "organization_type": "university", "sector": "academia_and_research", "state_or_region": "Illinois", "country": "United States", "normalization_notes": "Student status is not classified as employment."},
        {"key": "org-manzanar-education-b958", "canonical_name": "Manzanar Relocation Center Education Department", "historical_name": "Manzanar Relocation Center Education Department", "aliases": ["Manzanar school office"], "organization_type": "federal relocation-center education office", "sector": "federal_government", "city": "Manzanar", "state_or_region": "California", "country": "United States", "active_dates": "1942-1945", "normalization_notes": "A War Relocation Authority unit. Toda's coerced-incarceration context is preserved; the relationship is not simplified into ordinary voluntary employment."},
        {"key": "org-umd-b958", "organization_id": "57b220a8-e7c0-53d8-8565-a287d3bc6bd7", "canonical_name": "University of Maryland", "historical_name": "University of Maryland", "aliases": [], "organization_type": "university", "sector": "academia_and_research", "city": "College Park", "state_or_region": "Maryland", "country": "United States", "normalization_notes": "Student and clerical relationships are modeled separately."},
        {"key": "org-cornell-b958", "organization_id": "e1357e85-f9f9-5409-b56d-a75b4c3326fa", "canonical_name": "Cornell University", "historical_name": "Cornell University", "aliases": [], "organization_type": "university", "sector": "academia_and_research", "city": "Ithaca", "state_or_region": "New York", "country": "United States", "normalization_notes": "Student status is not classified as employment."},
        {"key": "org-signal-corps-b958", "organization_id": "37fe0e48-9745-5a0a-8e04-6be9bc7c5c91", "canonical_name": "United States Army Signal Corps", "historical_name": "Signal Corps", "aliases": ["Army Signal Corps"], "organization_type": "military branch", "sector": "military", "country": "United States", "normalization_notes": "Military assignment remains distinct from civilian employment."},
        {"key": "org-royal-yugoslav-army-b958", "organization_id": "e26dbadb-4a0b-5b59-ba26-722c20551bba", "canonical_name": "Royal Yugoslav Army", "historical_name": "Vojska Kraljevine Jugoslavije", "aliases": ["Yugoslav Royal Army", "Yugoslav Supreme Command"], "organization_type": "foreign allied military", "sector": "military", "country": "Kingdom of Yugoslavia", "normalization_notes": "The source wording and wartime command context are preserved."},
        {"key": "org-yugoslav-embassy-b958", "canonical_name": "Yugoslav Embassy in Washington", "historical_name": "Yugoslav Embassy in Washington", "aliases": ["Embassy of the Kingdom of Yugoslavia in Washington"], "organization_type": "foreign embassy", "sector": "federal_government", "city": "Washington", "state_or_region": "District of Columbia", "country": "Kingdom of Yugoslavia", "active_dates": "wartime assignment documented in 1944", "normalization_notes": "Historical royal-government context retained."},
        {"key": "org-jacl-b958", "organization_id": "91a81994-284a-5bd9-9de2-9b20fb7f6e18", "canonical_name": "Japanese American Citizens League", "historical_name": "Japanese American Citizens League", "aliases": ["JACL"], "organization_type": "civil-rights and civic organization", "sector": "labor_nonprofit_and_religion", "country": "United States", "normalization_notes": "Professional and political affiliation; not classified as employment."},
        {"key": "org-anti-axis-b958", "canonical_name": "Anti-Axis Committee", "historical_name": "Anti-Axis Committee", "aliases": [], "organization_type": "wartime civic committee", "sector": "labor_nonprofit_and_religion", "city": "Los Angeles", "state_or_region": "California", "country": "United States", "active_dates": "1941-1942", "normalization_notes": "A short-lived Japanese American civic committee; affiliation is not classified as employment."},
    ]


def affiliations() -> list[dict[str, object]]:
    irwin, _ = person("469-25")
    floyd, _ = person("469-28")
    gerard, _ = person("469-29")
    honey, _ = person("469-32")
    arthur, _ = person("469-33")
    paul, _ = person("469-41")
    borislav, _ = person("469-43")
    slocum, _ = person("470-1")
    return [
        {"key": "irwin-tobin-owi-b958", "person_id": irwin, "organization_key": "org-owi-b958", "organization_name_as_found": "Office of War Information", "role_title": "Information Specialist", "relationship_type": "government_assignment", "end_date": "before later OSS service", "date_precision": "Contemporary notices place him on leave from Rhode Island State College with OWI in England, followed later by OSS service.", "country": "United Kingdom", "immediate_pre_oss": True, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "explicit_immediate", "identity_confidence": "confirmed", "claim_confidence": "confirmed", "source_quality": "C_reputable_contemporary_or_scholarly", "publication_status": "published", "research_notes": "OWI is a government assignment, not a civilian employer."},
        {"key": "irwin-tobin-risc-b958", "person_id": irwin, "organization_key": "org-rhode-island-state-b958", "organization_name_as_found": "Rhode Island State College", "role_title": "assistant professor of political science", "occupation": "political scientist and professor", "relationship_type": "employment", "end_date": "before OWI service", "date_precision": "A contemporary notice describes Tobin as on leave from the college while serving OWI in England.", "state_or_region": "Rhode Island", "country": "United States", "immediate_pre_oss": False, "last_civilian_pre_service": True, "pre_oss_temporal_basis": "explicit_immediate", "identity_confidence": "confirmed", "claim_confidence": "confirmed", "source_quality": "C_reputable_contemporary_or_scholarly", "publication_status": "published", "research_notes": "The college is the last named civilian employer before the intervening OWI government assignment."},
        {"key": "floyd-tobrocke-uillinois-b958", "person_id": floyd, "organization_key": "org-uillinois-b958", "organization_name_as_found": "University of Illinois", "role_title": "student; 1940 graduate", "relationship_type": "student", "end_date": "1940", "date_precision": "Graduation year stated in a newspaper obituary.", "state_or_region": "Illinois", "country": "United States", "immediate_pre_oss": False, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "high_confidence", "claim_confidence": "high", "source_quality": "C_reputable_contemporary_or_scholarly", "publication_status": "published", "research_notes": "Student status is not employment; no immediate pre-OSS employer is established."},
        {"key": "gerard-toby-army-category-b958", "person_id": gerard, "occupation": "repairmen and mechanics, n. e. c.", "relationship_type": "employment", "end_date": "1942-10-29", "date_precision": "Historical category 5-83 was recorded at Army entry on 1942-10-29; no employer or workplace is named.", "country": "United States", "immediate_pre_oss": False, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "strongly_date_bounded", "identity_confidence": "high_confidence", "claim_confidence": "medium", "source_quality": "A_direct_official", "publication_status": "publish_qualified", "research_notes": "Broad historical category only; Gerard/Gerald spelling conflict remains visible."},
        {"key": "honey-toda-manzanar-school-b958", "person_id": honey, "organization_key": "org-manzanar-education-b958", "organization_name_as_found": "Manzanar school office", "role_title": "secretary to Superintendent of Schools Dr. Genevieve Carter", "occupation": "secretary", "relationship_type": "government_assignment", "end_date": "before 1945-01-27", "date_precision": "The January 1945 Manzanar Free Press describes the role retrospectively as occurring while Toda was incarcerated at Manzanar.", "city": "Manzanar", "state_or_region": "California", "country": "United States", "immediate_pre_oss": False, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "temporal_relation_uncertain", "identity_confidence": "high_confidence", "claim_confidence": "medium", "source_quality": "C_reputable_contemporary_or_scholarly", "publication_status": "publish_qualified", "research_notes": "The coerced-incarceration context is explicit. The accessible source does not establish the role's exact relation to OSS entry."},
        {"key": "honey-toda-umd-student-b958", "person_id": honey, "organization_key": "org-umd-b958", "organization_name_as_found": "University of Maryland", "role_title": "student; Bachelor of Arts candidate and first-honors recipient", "occupation": "sociology student", "relationship_type": "student", "end_date": "1945", "date_precision": "Institutional and contemporary sources place her at College Park and report first honors by January 1945.", "city": "College Park", "state_or_region": "Maryland", "country": "United States", "immediate_pre_oss": False, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "temporal_relation_uncertain", "identity_confidence": "high_confidence", "claim_confidence": "high", "source_quality": "B_authoritative_institutional", "publication_status": "publish_qualified", "research_notes": "Student status is not employment; the exact OSS-entry date remains unknown."},
        {"key": "honey-toda-umd-secretary-b958", "person_id": honey, "organization_key": "org-umd-b958", "organization_name_as_found": "University of Maryland", "role_title": "secretary to the school", "occupation": "secretary", "relationship_type": "employment", "start_date": "1945-01", "date_precision": "A January 27, 1945 contemporary notice says she was then working as a secretary to the school while pursuing a master's degree.", "city": "College Park", "state_or_region": "Maryland", "country": "United States", "immediate_pre_oss": False, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "temporal_relation_uncertain", "identity_confidence": "high_confidence", "claim_confidence": "medium", "source_quality": "C_reputable_contemporary_or_scholarly", "publication_status": "publish_qualified", "research_notes": "The employer is named, but the accessible source does not establish whether this was the last civilian employer before OSS."},
        {"key": "arthur-todd-army-category-b958", "person_id": arthur, "occupation": "bookkeepers and cashiers, except bank cashiers", "relationship_type": "employment", "end_date": "1943-05-22", "date_precision": "Historical category 1-01 was recorded at Army entry on 1943-05-22; no employer or workplace is named.", "country": "United States", "immediate_pre_oss": False, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "strongly_date_bounded", "identity_confidence": "high_confidence", "claim_confidence": "medium", "source_quality": "A_direct_official", "publication_status": "publish_qualified", "research_notes": "Broad historical category only; the damaged Army name form remains documented."},
        {"key": "paul-todd-cornell-b958", "person_id": paul, "organization_key": "org-cornell-b958", "organization_name_as_found": "Cornell University", "role_title": "student; B.S. 1942", "relationship_type": "student", "end_date": "1942", "date_precision": "The official congressional biography dates the B.S. to 1942; the accepted Army record carries the historical Students category at December 1942 entry.", "city": "Ithaca", "state_or_region": "New York", "country": "United States", "immediate_pre_oss": False, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "strongly_date_bounded", "identity_confidence": "confirmed", "claim_confidence": "high", "source_quality": "A_direct_official", "publication_status": "published", "research_notes": "This is the last documented civilian status before Army service, not an employer."},
        {"key": "paul-todd-signal-corps-b958", "person_id": paul, "organization_key": "org-signal-corps-b958", "organization_name_as_found": "United States Army Signal Corps", "role_title": "service member", "relationship_type": "military_assignment", "start_date": "1942", "end_date": "1945", "date_precision": "The official biography groups Signal Corps and OSS service within 1942-1945 but does not state the transfer date.", "country": "United States", "immediate_pre_oss": False, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "temporal_relation_uncertain", "identity_confidence": "confirmed", "claim_confidence": "high", "source_quality": "A_direct_official", "publication_status": "publish_qualified", "research_notes": "Signal Corps is a military pathway, not a civilian employer. Source order is not treated as proof of immediacy."},
        {"key": "borislav-todorovic-royal-army-b958", "person_id": borislav, "organization_key": "org-royal-yugoslav-army-b958", "organization_name_as_found": "Yugoslav Supreme Command", "role_title": "captain; liaison officer accompanying Allied military missions", "relationship_type": "military_assignment", "start_date": "1943", "end_date": "1944", "date_precision": "A November 1943 wartime message names Capt. Bora Todorovic accompanying U.S. officers; exact OSS-file chronology remains uncertain.", "country": "Kingdom of Yugoslavia", "immediate_pre_oss": False, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "temporal_relation_uncertain", "identity_confidence": "high_confidence", "claim_confidence": "high", "source_quality": "C_reputable_contemporary_or_scholarly", "publication_status": "publish_qualified", "research_notes": "Foreign allied military assignment; not a U.S. civilian employer or proof of commissioned U.S. status."},
        {"key": "borislav-todorovic-embassy-b958", "person_id": borislav, "organization_key": "org-yugoslav-embassy-b958", "organization_name_as_found": "Yugoslav Embassy in Washington", "role_title": "Assistant Military Attaché", "relationship_type": "military_assignment", "end_date": "1944-08", "date_precision": "FRUS identifies Capt. Borislav Todorovich in this assignment before his late-August 1944 departure from the United States.", "city": "Washington", "state_or_region": "District of Columbia", "country": "United States", "immediate_pre_oss": False, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "temporal_relation_uncertain", "identity_confidence": "high_confidence", "claim_confidence": "high", "source_quality": "A_direct_official", "publication_status": "publish_qualified", "research_notes": "The official assignment is dated, but its exact relation to the indexed OSS file is not established."},
        {"key": "tokutaro-slocum-jacl-b958", "person_id": slocum, "organization_key": "org-jacl-b958", "organization_name_as_found": "Japanese American Citizens League", "role_title": "citizenship activist and early-1930s participant; later welcomed back", "relationship_type": "professional_affiliation", "start_date": "1930s", "end_date": "1942", "date_precision": "Densho documents the prewar citizenship campaign and renewed wartime involvement but not a salaried employment relationship.", "country": "United States", "immediate_pre_oss": False, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "high_confidence", "claim_confidence": "high", "source_quality": "B_authoritative_institutional", "publication_status": "published", "research_notes": "Professional/civic affiliation only; not an employer."},
        {"key": "tokutaro-slocum-anti-axis-b958", "person_id": slocum, "organization_key": "org-anti-axis-b958", "organization_name_as_found": "Anti-Axis Committee", "role_title": "chair and intelligence-committee participant", "relationship_type": "professional_affiliation", "start_date": "1941-12", "end_date": "1942", "date_precision": "Densho places the committee activity after Pearl Harbor and before Slocum's removal to Manzanar in spring 1942.", "city": "Los Angeles", "state_or_region": "California", "country": "United States", "immediate_pre_oss": False, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "strongly_date_bounded", "identity_confidence": "high_confidence", "claim_confidence": "high", "source_quality": "B_authoritative_institutional", "publication_status": "published", "research_notes": "Civic wartime affiliation; not classified as employment or proof of an OSS entry date."},
    ]


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


def claims() -> list[dict[str, object]]:
    irwin, _ = person("469-25")
    floyd, _ = person("469-28")
    gerard, _ = person("469-29")
    honey, _ = person("469-32")
    arthur, _ = person("469-33")
    paul, _ = person("469-41")
    borislav, _ = person("469-43")
    slocum, _ = person("470-1")
    values = [
        claim("identity-irwin-tobin-b958", irwin, "identity", "The indexed Irwin M Tobin is confirmed as Rhode Island State College political scientist Irwin M. Tobin.", "Two contemporary APSR notices name the exact person, his academic role, OWI assignment and later OSS service.", "Confirmed by exact name, middle initial, occupation, institution and explicit OSS chronology.", "The notices are contemporary to the OWI-to-OSS transition.", "C_reputable_contemporary_or_scholarly", "confirmed", "published", "No facts from other Irwin Tobin namesakes were transferred.", [{"source_key": INDEX, "locator_override": "PDF page 469 row 25; Box 779"}, {"source_key": APSR_OWI, "locator_override": "Printed page 993"}, {"source_key": APSR_POST, "locator_override": "Volume 40 issue 1, printed page 126"}]),
        claim("immediate-irwin-tobin-owi-b958", irwin, "immediate_pre_oss_affiliation", "Irwin M. Tobin served in England with the Office of War Information before later service with OSS.", "A 1946 APSR notice explicitly orders the two agencies: OWI in England, then OSS.", "Confirmed exact-person match from the linked contemporary notices.", "Explicit immediate sequence: OWI service is stated before later OSS service.", "C_reputable_contemporary_or_scholarly", "confirmed", "published", "OWI is modeled as a government assignment, not a civilian employer.", [{"source_key": APSR_POST, "locator_override": "Printed page 126", "excerpt_override": "service in England with the Office of War Information and later with the Office of Strategic Services"}, {"source_key": APSR_OWI, "locator_override": "Printed page 993"}], affiliation_key="irwin-tobin-owi-b958"),
        claim("last-civilian-irwin-tobin-risc-b958", irwin, "last_civilian_pre_service", "Rhode Island State College was Irwin M. Tobin's last documented civilian employer before the intervening OWI assignment.", "A contemporary notice calls Tobin a professor on leave from Rhode Island State College while serving OWI in England.", "Confirmed exact-person match from name, institution, role and later OSS sequence.", "The leave wording directly places the college job before and continuing into the OWI assignment.", "C_reputable_contemporary_or_scholarly", "confirmed", "published", "The historical college name is preserved; student status is not involved.", [{"source_key": APSR_OWI, "locator_override": "Printed page 993", "excerpt_override": "on leave from Rhode Island State College as Information Specialist, O.W.I."}, {"source_key": APSR_POST, "locator_override": "Printed page 126"}], affiliation_key="irwin-tobin-risc-b958"),
        claim("identity-floyd-tobrocke-b958", floyd, "identity", "The indexed Floyd C Tobrocke is a high-confidence match to the Indianapolis educator and World War II Army captain.", "The rare exact full name, compatible generation and World War II Army captain service support the match.", "High confidence from an exceptionally distinctive exact name plus compatible wartime service.", "The obituary documents education and military service but not the exact OSS entry date.", "C_reputable_contemporary_or_scholarly", "high", "published", "Later Tech High employment is identity context only and is not labeled pre-OSS.", [{"source_key": INDEX, "locator_override": "PDF page 469 row 28; Box 780"}, {"source_key": TOBROCKE}]),
        claim("prewar-floyd-tobrocke-uillinois-b958", floyd, "other_pre_oss_affiliation", "Floyd C. Tobrocke graduated from the University of Illinois in 1940.", "The Indianapolis Star obituary identifies him as a 1940 graduate.", "High confidence from the accepted rare-name identity.", "Documented prewar student affiliation; not shown to be the immediately prior OSS role.", "C_reputable_contemporary_or_scholarly", "high", "published", "University attendance is not classified as employment.", [{"source_key": TOBROCKE, "excerpt_override": "a 1940 graduate of the University of Illinois"}], affiliation_key="floyd-tobrocke-uillinois-b958"),
        claim("identity-gerard-toby-army-b958", gerard, "identity", "The indexed Gerard A Toby is a high-confidence match to the official Army record printed as Gerald A Toby.", "A nonshared private identifier agrees exactly; the Gerard/Gerald given-name conflict is retained.", "High confidence from exact private identifier agreement plus compatible surname and middle initial.", "The Army record dates entry but not the OSS transfer.", "A_direct_official", "high", "published", "The variant is documented, not silently corrected.", [{"source_key": INDEX, "locator_override": "PDF page 469 row 29; Box 780; private identifier withheld"}, {"source_key": ARMY, "locator_override": "Reviewed Gerald A Toby record; private identifier withheld"}, {"source_key": TECH, "support_type": "context_only", "locator_override": "Field definitions, PDF physical pages 44-46"}]),
        claim("occupation-gerard-toby-army-b958", gerard, "occupation", "At Army entry on 1942-10-29, Gerard/Gerald A Toby was recorded in the historical Repairmen and mechanics, n. e. c. category.", "The official bulk record supplies code 583; the visually reviewed NARA list expands it as category 5-83.", "High confidence from the accepted private-identifier bridge.", "Strongly date-bounded at Army entry; no employer, workplace or immediate OSS sequence is named.", "A_direct_official", "medium", "publish_qualified", "The broad historical category is not converted into a modern specialty or named employer.", [{"source_key": ARMY, "locator_override": "Army entry 1942-10-29; code 583; private identifier withheld"}, {"source_key": CODES, "locator_override": "PDF physical page 178; category 5-83"}], affiliation_key="gerard-toby-army-category-b958", excerpt="Repairmen and mechanics, n. e. c."),
        claim("identity-honey-toda-b958", honey, "identity", "The indexed Honey M Toda is a high-confidence match to Honey Mitsuye Toda.", "Institutional records preserve the rare full name and place Honey Toda at Manzanar in 1942 and the University of Maryland by 1945.", "High confidence from the rare exact given and family names, matching middle initial, and coherent Manzanar-to-Maryland chronology.", "The sources document 1942-1945 but do not give her exact OSS entry date.", "B_authoritative_institutional", "high", "published", "Mitsuye is retained as a documented expansion, not a replacement for the index spelling.", [{"source_key": INDEX, "locator_override": "PDF page 469 row 32; Box 780"}, {"source_key": SCU_TODA}, {"source_key": UMD_TODA}]),
        claim("work-honey-toda-manzanar-b958", honey, "other_pre_oss_affiliation", "While incarcerated at Manzanar, Honey Toda worked as secretary to the superintendent of schools.", "The January 1945 Manzanar Free Press retrospectively names Honey Toda and Dr. Genevieve Carter.", "High-confidence rare-name match supported by institutional full-name and 1942 Manzanar records.", "Documented wartime work before January 1945; relation to OSS entry is uncertain.", "C_reputable_contemporary_or_scholarly", "medium", "publish_qualified", "The claim preserves coerced-incarceration context and does not treat the role as ordinary voluntary employment.", [{"source_key": MANZANAR_FP, "locator_override": "Volume 6 number 63, page 2", "excerpt_override": "Honey Toda was a secretary of Superintendent of Schools Dr. Genevieve Carter"}, {"source_key": SCU_TODA, "support_type": "context_only"}], affiliation_key="honey-toda-manzanar-school-b958"),
        claim("student-honey-toda-umd-b958", honey, "other_pre_oss_affiliation", "Honey Mitsuye Toda studied sociology at the University of Maryland and received first honors by January 1945.", "The university program names her as a Bachelor of Arts candidate and first-honors recipient; a contemporary notice says she pursued graduate study.", "High-confidence match from the distinctive full name and Manzanar chronology.", "Dated wartime student affiliation; exact relation to OSS entry remains uncertain.", "B_authoritative_institutional", "high", "publish_qualified", "Student status is not classified as employment.", [{"source_key": UMD_TODA, "locator_override": "Bachelor of Arts candidates and First Honors list"}, {"source_key": MANZANAR_FP, "locator_override": "Volume 6 number 63, page 2"}], affiliation_key="honey-toda-umd-student-b958"),
        claim("work-honey-toda-umd-b958", honey, "other_pre_oss_affiliation", "In January 1945, Honey Toda was reported working as a secretary at the University of Maryland while pursuing a master's degree.", "The contemporary Manzanar Free Press notice names her current study and clerical work at the school.", "High-confidence match from the distinctive name and linked institutional chronology.", "Explicitly current in January 1945, but not proven to be the last civilian employer before OSS.", "C_reputable_contemporary_or_scholarly", "medium", "publish_qualified", "Published as documented wartime employment with temporal qualification, not as a settled immediate predecessor.", [{"source_key": MANZANAR_FP, "locator_override": "Volume 6 number 63, page 2", "excerpt_override": "is now working as a secretary to the school"}, {"source_key": UMD_TODA, "support_type": "context_only"}], affiliation_key="honey-toda-umd-secretary-b958"),
        claim("identity-arthur-todd-army-b958", arthur, "identity", "The indexed Arthur F Todd is a high-confidence match to the reviewed official Army record with the damaged name form Arth R F Todd.", "A nonshared private identifier agrees exactly; the source-damaged Army name still contains Arthur-like text, F and Todd.", "High confidence from exact private identifier agreement despite visible name-field damage.", "The Army record dates entry but not the OSS transfer.", "A_direct_official", "high", "published", "The damaged form is preserved as a variant and is not treated as a corrected middle name.", [{"source_key": INDEX, "locator_override": "PDF page 469 row 33; Box 780; private identifier withheld"}, {"source_key": ARMY, "locator_override": "Reviewed Arth R F Todd record; private identifier withheld"}, {"source_key": TECH, "support_type": "context_only"}]),
        claim("occupation-arthur-todd-army-b958", arthur, "occupation", "At Army entry on 1943-05-22, Arthur F Todd was recorded in the historical Bookkeepers and cashiers, except bank cashiers category.", "The official bulk record supplies code 101; the NARA list expands it as category 1-01.", "High confidence from the accepted private-identifier bridge.", "Strongly date-bounded at Army entry; no employer, workplace or immediate OSS sequence is named.", "A_direct_official", "medium", "publish_qualified", "The category is not converted into a named employer or exact job title.", [{"source_key": ARMY, "locator_override": "Army entry 1943-05-22; code 101; private identifier withheld"}, {"source_key": CODES, "locator_override": "PDF physical page 172; category 1-01"}], affiliation_key="arthur-todd-army-category-b958", excerpt="Bookkeepers and cashiers, except bank cashiers"),
        claim("identity-paul-harold-todd-b958", paul, "identity", "Indexed page 469 row 41 is confirmed as Paul Harold Todd Jr.; the separate row 40 remains unresolved.", "The row 41 private identifier matches an official Army record naming Paul H Todd Jr.; the official House biography supplies the full name, Cornell degree and OSS service.", "Confirmed by nonshared private identifier, suffix, Cornell chronology and explicit OSS service.", "Army entry and official biography date the pathway to 1942-1945.", "A_direct_official", "confirmed", "published", "The two Paul H Todd rows are not merged because their printed private identifiers differ.", [{"source_key": INDEX, "locator_override": "PDF page 469 row 41; Box 780; private identifier withheld"}, {"source_key": ARMY, "locator_override": "Reviewed Paul H Todd Jr record; private identifier withheld"}, {"source_key": HOUSE_TODD}]),
        claim("student-paul-harold-todd-cornell-b958", paul, "other_pre_oss_affiliation", "Paul Harold Todd Jr. earned a Cornell University B.S. in 1942 and was recorded in the Army's historical Students category at December 1942 entry.", "The official House biography and accepted Army record independently support the dated student pathway.", "Confirmed identity from the private identifier, suffix and official biography.", "Strongly date-bounded before or at Army entry; not employment.", "A_direct_official", "high", "published", "Cornell is a student affiliation and is excluded from employer analytics.", [{"source_key": HOUSE_TODD, "locator_override": "Concise biography"}, {"source_key": ARMY, "locator_override": "Army entry 1942-12-09; historical code 992; private identifier withheld"}, {"source_key": CODES, "locator_override": "Historical category 9-92"}], affiliation_key="paul-todd-cornell-b958"),
        claim("military-paul-harold-todd-signal-b958", paul, "other_pre_oss_affiliation", "Paul Harold Todd Jr. served in the U.S. Army Signal Corps and OSS during 1942-1945.", "The official House biography names both wartime organizations within the same date span.", "Confirmed exact person from the accepted Army bridge and official full-name biography.", "The source does not provide the Signal Corps-to-OSS transfer date, so immediacy is not asserted.", "A_direct_official", "high", "publish_qualified", "Signal Corps is modeled as a military assignment, not a civilian employer.", [{"source_key": HOUSE_TODD, "locator_override": "Concise biography", "excerpt_override": "served in the United States Army Signal Corps and the Office of Strategic Services, 1942-1945"}], affiliation_key="paul-todd-signal-corps-b958"),
        claim("identity-borislav-todorovic-b958", borislav, "identity", "The indexed Borislav J Todorovic is a high-confidence match to Royal Yugoslav Army captain Borislav Todorovich.", "The distinctive name is joined by wartime U.S. liaison service with OSS officer Walter Mansfield and an official 1944 U.S. diplomatic record.", "High confidence from the rare exact name, Allied liaison context and official Royal Yugoslav military assignment.", "The sources cover 1943-1944 but do not expose the exact OSS personnel-file chronology.", "A_direct_official", "high", "published", "The J middle initial is preserved from the index; Todorovich and Todorović are documented variants.", [{"source_key": INDEX, "locator_override": "PDF page 469 row 43; Box 780"}, {"source_key": FRUS_TODOROVIC}, {"source_key": ZNACI_TODOROVIC}]),
        claim("military-borislav-todorovic-liaison-b958", borislav, "other_pre_oss_affiliation", "In 1943, Capt. Borislav Todorovic served with the Yugoslav Supreme Command as a liaison accompanying Allied military missions.", "A wartime message names him accompanying U.S. officers Albert Seitz and Walter Mansfield through Yugoslav corps.", "High-confidence distinctive-name match supported by official FRUS assignment evidence.", "Dated wartime military assignment; exact sequence relative to the indexed OSS file remains uncertain.", "C_reputable_contemporary_or_scholarly", "high", "publish_qualified", "Foreign allied military service is not classified as U.S. commissioned or civilian employment.", [{"source_key": ZNACI_TODOROVIC, "locator_override": "Document 654, 1943-11-13"}, {"source_key": FRUS_TODOROVIC, "support_type": "context_only"}], affiliation_key="borislav-todorovic-royal-army-b958"),
        claim("military-borislav-todorovic-embassy-b958", borislav, "other_pre_oss_affiliation", "In 1944, Capt. Borislav Todorovich was Assistant Military Attaché at the Yugoslav Embassy in Washington.", "FRUS identifies the exact wartime office and says he remained a commissioned Royal Yugoslav Army officer.", "High-confidence match from the distinctive name and compatible Allied liaison chronology.", "Explicitly dated in 1944; relation to the OSS file remains uncertain.", "A_direct_official", "high", "publish_qualified", "The embassy assignment is not converted into a civilian employer claim.", [{"source_key": FRUS_TODOROVIC, "locator_override": "Pages 1408-1410 and footnotes", "excerpt_override": "Capt. Borislav Todorovich, Assistant Military Attaché at the Yugoslav Embassy in Washington"}], affiliation_key="borislav-todorovic-embassy-b958"),
        claim("identity-tokutaro-slocum-b958", slocum, "identity", "The indexed N S Tokutaro is a high-confidence match to Tokutaro Nishimura Slocum.", "The index's three components appear in displaced order; Densho identifies the distinctive full name and later OSS Far East Intelligence Section work.", "High confidence from the exact unusual component set plus explicit OSS service and compatible wartime context.", "The biography orders Manzanar and protective custody before later OSS work but does not give an OSS entry date.", "B_authoritative_institutional", "high", "published", "The source-row spelling remains recoverable; the corrected display form is retained as a documented variant.", [{"source_key": INDEX, "locator_override": "PDF page 470 row 1; Box 780"}, {"source_key": DENSHO_SLOCUM}]),
        claim("prewar-tokutaro-slocum-jacl-b958", slocum, "other_pre_oss_affiliation", "Tokutaro Nishimura Slocum was a prewar citizenship activist associated with the Japanese American Citizens League.", "Densho documents his role in the campaign that culminated in the 1935 Nye-Lea Act and his renewed wartime JACL involvement.", "High confidence from the resolved distinctive identity and explicit biography.", "Documented in the 1930s and before later OSS service; not shown to be the immediate predecessor.", "B_authoritative_institutional", "high", "published", "Civic affiliation is not classified as employment.", [{"source_key": DENSHO_SLOCUM, "locator_override": "Early Life and Citizenship Campaign; War Years and Aftermath"}], affiliation_key="tokutaro-slocum-jacl-b958"),
        claim("wartime-tokutaro-slocum-anti-axis-b958", slocum, "other_pre_oss_affiliation", "After Pearl Harbor and before removal to Manzanar, Tokutaro Slocum chaired or led activities of the Los Angeles Anti-Axis Committee.", "Densho places this civic and intelligence-oriented committee activity before his 1942 confinement and later OSS work.", "High confidence from the resolved distinctive identity and explicit institutional biography.", "Strongly date-bounded before later OSS service, but protective custody and other intervening status prevent an immediacy claim.", "B_authoritative_institutional", "high", "published", "The role is described as a civic affiliation, not employment or an OSS assignment.", [{"source_key": DENSHO_SLOCUM, "locator_override": "War Years and Aftermath"}], affiliation_key="tokutaro-slocum-anti-axis-b958"),
    ]
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
    duplicate = "batch958-paul-h-todd-page469" if key == "469-40" else None
    return {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, Box {archive_box(key)} and archive location 230/86/42/02. {reason}",
        "personnel_category": "unknown_or_indeterminate",
        "manual_review_required": True,
        "possible_duplicate_group": duplicate,
        "research_status": "requires_archival_review",
        "next_action": f"Review Box {archive_box(key)} for corroborating identifiers, immediate pre-OSS affiliation and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "critical" if key in {"469-34", "469-40"} else "high",
    }


def person_updates() -> list[dict[str, object]]:
    values = [unresolved_update(key, reason) for key, reason in UNRESOLVED.items()]
    values.extend(
        [
            base_update("469-25", identity_status="confirmed", identity_evidence="Two contemporary APSR notices identify the exact name, college role, OWI assignment and later OSS service.", personnel_category="civilian_professional_or_administrative_grade", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="verified_employer_found", next_action="Review Box 779 for the exact OSS entry date and assignment; the OWI predecessor and Rhode Island State College employer are already explicit.", archival_review_priority="medium"),
            base_update("469-28", identity_status="high_confidence", identity_evidence="The exceptionally rare exact name, compatible generation and World War II Army captain service support the obituary match.", personnel_category="commissioned_army_officer", commissioned_officer=True, allied_or_foreign_personnel=False, research_status="completed", next_action="Review Box 780 for the employer or occupation between the 1940 University of Illinois graduation and OSS service; do not project later Tech High employment backward.", archival_review_priority="high"),
            base_update("469-29", identity_status="high_confidence", identity_evidence="A nonshared private identifier connects Gerard A Toby to the official Army record printed Gerald A Toby; the conflict remains visible.", name_variants=["Gerald A Toby"], personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="occupation_only_found", next_action="Review Box 780 for the named employer, exact mechanical specialty and Army-to-OSS sequence.", archival_review_priority="high"),
            base_update("469-32", identity_status="high_confidence", identity_evidence="The rare exact given and family names, matching middle initial and coherent Manzanar-to-Maryland chronology establish Honey Mitsuye Toda.", name_variants=["Honey Mitsuye Toda"], personnel_category="civilian_professional_or_administrative_grade", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="completed", next_action="Review Box 780 for the OSS entry date and whether University of Maryland clerical work immediately preceded service.", archival_review_priority="high"),
            base_update("469-33", identity_status="high_confidence", identity_evidence="A nonshared private identifier connects Arthur F Todd to the official Army record despite the source-damaged Arth R F name form.", name_variants=["Arth R F Todd"], personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="occupation_only_found", next_action="Review Box 780 for the named employer and Army-to-OSS sequence; the broad bookkeeping/cashier category is not a workplace.", archival_review_priority="high"),
            base_update("469-41", identity_status="confirmed", identity_evidence="A nonshared private identifier, the Jr suffix and an official House biography connect row 41 to Paul Harold Todd Jr.; row 40 remains separate.", name_variants=["Paul Harold Todd Jr."], personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, possible_duplicate_group="batch958-paul-h-todd-page469", research_status="completed", next_action="Review both Box 780 Paul H Todd files before any merge and establish the Signal Corps-to-OSS transfer date.", archival_review_priority="critical"),
            base_update("469-43", identity_status="high_confidence", identity_evidence="The distinctive name, wartime liaison service with OSS officer Walter Mansfield and official FRUS military-attaché record support Borislav Todorovic.", name_variants=["Borislav Todorovich", "Borislav Todorović", "Bora Todorovic"], personnel_category="foreign_or_allied_military_personnel", commissioned_officer=True, allied_or_foreign_personnel=True, research_status="completed", next_action="Review Box 780 for the precise relationship between Royal Yugoslav assignments and the indexed OSS file.", archival_review_priority="high"),
            base_update("470-1", identity_status="high_confidence", identity_evidence="The displaced index components N S Tokutaro align with Tokutaro Nishimura Slocum, whose distinctive biography explicitly includes later OSS Far East Intelligence Section work.", name_variants=["Tokutaro Nishimura Slocum", "Tokutaro 'Tokie' Slocum", "Tokie Slocum"], personnel_category="unknown_or_indeterminate", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="completed", next_action="Review Box 780 for the exact OSS entry date and any employment between protective custody after Manzanar and OSS service.", archival_review_priority="high"),
        ]
    )
    return values


def research_attempts() -> list[dict[str, object]]:
    special = {
        "469-25": "Contemporary APSR notices explicitly established Rhode Island State College leave, OWI service in England and later OSS service.",
        "469-28": "A newspaper obituary established the rare-name Army captain, 1940 University of Illinois graduate and later educator; only the student affiliation is treated as prewar.",
        "469-29": "An accepted protected-identifier Army bridge established the Gerard/Gerald variant and a dated historical repairmen-and-mechanics category without a named employer.",
        "469-32": "Institutional records and a contemporary camp newspaper established the Honey Mitsuye Toda identity, Manzanar school-office work and 1945 University of Maryland study and clerical work.",
        "469-33": "An accepted protected-identifier Army bridge established identity despite a damaged name field and supplied a dated historical bookkeeping/cashier category.",
        "469-41": "An accepted protected-identifier Army bridge plus the official House biography established Paul Harold Todd Jr., Cornell study, Signal Corps and OSS service; the separate row 40 was not merged.",
        "469-43": "Official FRUS and a wartime Yugoslav document established the distinctive Royal Yugoslav liaison and military-attaché chronology without inventing a civilian employer.",
        "470-1": "Densho resolved the displaced index components to Tokutaro Nishimura Slocum and documented prewar JACL, Anti-Axis Committee, Manzanar and later OSS chronology.",
    }
    attempts: list[dict[str, object]] = []
    for key, (person_id, name) in PEOPLE.items():
        page, row = page_row(key)
        box = archive_box(key)
        if key in special:
            outcome = "source_reviewed"
            reviewed = 9
            rejected = 5
            detail = special[key]
        else:
            outcome = "candidate_rejected" if key in {"469-27", "469-30", "469-34", "469-39", "469-40"} else "no_result"
            reviewed = 7
            rejected = 6
            detail = UNRESOLVED[key]
        attempts.append(
            {
                "key": f"page{page}-row{row}-{slug(name)}-b958",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index and public Archives context; CIA Reading Room or equivalent official-source check; exact-name and meaningful variants; OSS, military and foreign-name clues; employer and occupation 1940; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Box {box}; private identifiers used only when defensible",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_958",
                "started_at": "2026-10-29T20:00:00Z",
                "completed_at": "2026-10-29T22:25:00Z",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search snippets, unsourced genealogy, people-finder pages, modern records, postwar-only leads and sources without an OSS, private-identifier or Box-file bridge were rejected. Search aliases were not treated as silent corrections. Distinct private identifiers prevented merging the two Paul H Todd rows.",
                "research_notes": f"{detail} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain, CIA Reading Room-equivalent and Library of Congress searches were checked as applicable. The index pages, Army bulk file, technical documentation and relevant code-list pages were inspected directly. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": (
                    "Compare both separate Paul H Todd Box 780 files before any duplicate merge or transfer of Paul Harold Todd Jr. claims."
                    if key in {"469-40", "469-41"}
                    else f"Review Box {box} for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before wartime service."
                ),
                "attempt_number": 1,
                "research_agent_version": "before-oss-b958-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-958-v1",
        "reviewer": "Before OSS Batch 958 evidence review",
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
