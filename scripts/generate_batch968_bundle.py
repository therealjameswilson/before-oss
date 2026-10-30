#!/usr/bin/env python3
"""Generate the reviewed Batch 968 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page474-michalis-tsirmulas-to-margaret-tugas-"
    "review_batch-968_2026-10-30.json"
)

INDEX = "nara-index-b968"
ARMY = "army-bulk-b968"
TECH = "army-tech-b968"
CODES = "army-codes-b968"
DPAA_TSIRMULAS = "dpaa-tsirmulas-b968"
OSSOG_PERSONNEL = "ossog-personnel-b968"
USWM_TSOLAS = "uswm-tsolas-b968"
OSSOG_TSouderos = "ossog-tsouderos-b968"
AFTER_BATTLE = "after-battle-tsouderos-b968"
DENSHO_TSURUTANI = "densho-tsurutani-b968"
PACIFIC_CITIZEN_TSURUTANI = "pacific-citizen-tsurutani-b968"
PRINCETON_TUCKER = "princeton-robert-tucker-b968"
WAPO_TUCKER = "wapo-robert-tucker-b968"
WAPO_TUCKERMAN = "wapo-laura-tuckerman-b968"


PEOPLE = {
    24: ("2a3e1fd8-a46d-553e-aa39-0ae740bdf7b6", "Michalis Tsirmulas"),
    25: ("e6c5814a-672a-5bac-ae39-2a26838efc57", "Tsun O Tso"),
    26: ("b292cf8c-e222-5691-af95-d8b9611a1804", "George T Tsohonis"),
    27: ("b26df1e4-6235-529e-a944-eb433fac14da", "James Tsolas"),
    28: ("1a007dc6-b269-5628-b725-877372b6a93d", "John E Tsouderos"),
    29: ("c1d3dce5-ca55-5fab-b00b-48b340b5691e", "Henry J Tsurutani"),
    30: ("7a7cc39d-f5f6-5acd-bac5-0a09bacd19e1", "Frances M Tuchscher"),
    31: ("7b279230-6292-529c-9480-87e12a7c69a1", "Emily Tuck"),
    32: ("5fe05290-6b8b-5b6a-84f7-049e0b5c627a", "G L Tucker"),
    33: ("bcb3f46a-5f2f-5770-9a73-250b2c1a855f", "Gertrude G Tucker"),
    34: ("f494ab67-5719-579c-8e05-3127319d62f9", "Isota A Tucker"),
    35: ("c1f47b06-84b9-5924-9e22-6b55c72bd8b0", "James R Tucker"),
    36: ("1783f52f-a39e-5f77-b1e5-7f0b882b5bb8", "Lula E Tucker"),
    37: ("d3a34ac7-43ac-5275-ae27-cb95fc84324d", "Robert C Tucker"),
    38: ("96fb3fa0-c6cf-5e8b-b7fb-84ae878c8326", "Robert W Tucker"),
    39: ("7d27b4fb-6450-5bc4-a3e5-81821aacccf2", "Roger S Tucker"),
    40: ("5de20758-c6bd-5ac2-9599-9ad015af799f", "William R Tucker"),
    41: ("a9947f65-e455-5916-b23c-22b3d93f9c1f", "Laura W Tuckerman"),
    42: ("4139f4b9-2858-53d7-8ec5-de13855ba5ae", "Margaret C Tuckerman"),
    43: ("f9bd1785-ba59-57e9-b1c0-30854e721f7b", "Bert A Tueling"),
    44: ("23f36d5e-436d-59f4-80d7-c784630bad71", "Lois R Tufts"),
    45: ("13d4e94d-069e-59ae-9c82-148c1d872244", "Robert W Tufts"),
    46: ("fe30d53d-9014-56f2-8470-bf66465c91d4", "Margaret E Tugas"),
}


ARMY_OCCUPATIONS = [
    {
        "row": 24,
        "date": "1943-05-13",
        "code": "227",
        "occupation": "Waiters and waitresses, except private family",
        "public_occupation": "waiter",
        "relationship": "unknown",
        "locator": "PDF physical page 172; historical category 2-27",
        "identity": "confirmed",
        "identity_note": "The protected identifier connects the index to the Army transcription TEIRMULAS MICHALIS; DPAA and the OSS Greek Operational Group roster independently identify Michalis Tsirmulas.",
        "identity_sources": [DPAA_TSIRMULAS, OSSOG_PERSONNEL],
        "variants": ["Teirmulas Michalis"],
    },
    {
        "row": 26,
        "date": "1942-04-23",
        "code": "185",
        "occupation": "Salesmen and sales agents, except to consumers",
        "public_occupation": "salesman or sales agent",
        "relationship": "unknown",
        "locator": "PDF physical pages 171-172; historical category 1-85",
        "identity": "high_confidence",
        "identity_note": "An exact full name and nonshared protected identifier connect the index row to the reviewed official Army row.",
        "identity_sources": [],
        "variants": [],
    },
    {
        "row": 27,
        "date": "1943-01-12",
        "code": "227",
        "occupation": "Waiters and waitresses, except private family",
        "public_occupation": "waiter",
        "relationship": "unknown",
        "locator": "PDF physical page 172; historical category 2-27",
        "identity": "high_confidence",
        "identity_note": "The protected identifier connects the index to the corrupted Army name TBOLA JAMES; Greek Operational Group sources independently identify Staff Sergeant James A Tsolas.",
        "identity_sources": [OSSOG_PERSONNEL, USWM_TSOLAS],
        "variants": ["James A Tsolas", "Tbola James"],
    },
    {
        "row": 35,
        "date": "1942-11-10",
        "code": "770",
        "occupation": "Firemen, other than process firemen",
        "public_occupation": "fireman other than a process fireman",
        "relationship": "unknown",
        "locator": "PDF physical page 174; historical category 7-70",
        "identity": "high_confidence",
        "identity_note": "An exact full name and nonshared protected identifier connect the index row to the reviewed official Army row.",
        "identity_sources": [],
        "variants": [],
    },
    {
        "row": 39,
        "date": "1942-06-13",
        "code": "137",
        "occupation": "Stenographers and typists",
        "public_occupation": "stenographer or typist",
        "relationship": "unknown",
        "locator": "PDF physical page 172; historical category 1-37",
        "identity": "high_confidence",
        "identity_note": "An exact full name and nonshared protected identifier connect the index row to the reviewed official Army row.",
        "identity_sources": [],
        "variants": [],
    },
    {
        "row": 40,
        "date": "1943-06-08",
        "code": "992",
        "occupation": "Students",
        "public_occupation": "student",
        "relationship": "student",
        "locator": "PDF physical page 304; corrected historical category 9-92",
        "identity": "high_confidence",
        "identity_note": "An exact full name and nonshared protected identifier connect the index row to the reviewed official Army row.",
        "identity_sources": [],
        "variants": [],
    },
    {
        "row": 45,
        "date": "1944-12-11",
        "code": "039",
        "occupation": "Professional occupations, not elsewhere classified",
        "public_occupation": "professional occupation, not elsewhere classified",
        "relationship": "unknown",
        "locator": "PDF physical page 171; historical category 0-39",
        "identity": "high_confidence",
        "identity_note": "An exact full name and nonshared protected identifier connect the index row to the reviewed official Army row.",
        "identity_sources": [],
        "variants": [],
    },
]


UNRESOLVED = {
    25: "Exact-name, transliteration-variant, official-domain, occupation, obituary and archival searches produced no defensible identity bridge.",
    30: "A postwar State Department editor-writer record for the exact name was rejected as temporally insufficient and no independent OSS identity bridge was found.",
    31: "The common name produced multiple modern and historical namesakes without two corroborating identifiers beyond the name.",
    32: "Initials-only exact and variant searches could not distinguish a unique person or dated pre-OSS affiliation.",
    33: "The common name produced plausible namesakes but no source tied one to OSS, Box 788 or another corroborating identifier.",
    34: "The unusual indexed spelling yielded only unbridged genealogical leads and no reliable OSS, occupation or employer evidence.",
    36: "Exact-name, initials, occupation, obituary, newspaper and archival searches produced no defensible identity bridge.",
    38: "Multiple Robert W Tucker namesakes were found; none supplied the required OSS and second-identifier bridge, and the later scholar was rejected.",
    42: "Searches found family and social-register context but no source tied Margaret C Tuckerman to OSS or a dated pre-OSS occupation.",
    43: "A discovery-only family-history profile supplied age and draft context but no OSS or occupation bridge and was rejected as final evidence.",
    44: "Exact-name, initials, occupation, obituary and archival searches produced no reliable identity bridge; people-finder results were rejected.",
    46: "Exact-name, spelling-variant, employer, obituary, newspaper and archival searches produced no defensible identity bridge.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 787-788",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 474, rows 24-46; checked against layout-preserving text and a 200 dpi page render",
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
            "locator": "Official unrestricted ASNEF.FIN.DAT; seven accepted Batch 968 comparisons; protected identifiers and record ordinals withheld",
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
            "locator": "PDF physical pages 171-174 and corrected page 304; seven Batch 968 categories visually and textually checked",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical categories identify neither employers nor workplaces and are retained only where needed for auditability.",
        },
        {
            "key": DPAA_TSIRMULAS,
            "stable_url": "https://www.dpaa.mil/Portals/85/WWIIAccounting/wwii_una_ARMY_20211015.pdf",
            "archival_identifier": "DPAA World War II Army personnel still unaccounted for",
            "title": "World War II Army Personnel Still Unaccounted For",
            "author_creator": "Defense POW/MIA Accounting Agency",
            "repository_publisher": "Defense POW/MIA Accounting Agency",
            "publication_record_date": "2021-10-15",
            "locator": "Michalis Tsirmulas entry; Technical Fifth Grade; 2671st Special Reconnaissance Battalion, OSS; protected identifier withheld",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "World War II accounting lists",
        },
        {
            "key": OSSOG_PERSONNEL,
            "stable_url": "https://ossog.info/personnel.html",
            "title": "OSS Operational Groups Personnel",
            "author_creator": "OSS Operational Groups veterans history project",
            "repository_publisher": "OSS Operational Groups",
            "publication_record_date": None,
            "locator": "Greek Operational Groups roster; Michalis Tsirmulas and James A. Tsolas",
            "access_date": "2026-10-30",
            "source_quality": "D_correlative_or_secondary",
            "collection_name": "OSS Operational Groups personnel roster",
            "rights_notes": "Used to corroborate identity and OSS unit context, not to infer a pre-OSS employer.",
        },
        {
            "key": USWM_TSOLAS,
            "stable_url": "https://uswarmemorials.org/html/people_details.php?PeopleID=24832",
            "title": "James A. Tsolas",
            "author_creator": "U.S. War Memorials Overseas",
            "repository_publisher": "U.S. War Memorials Overseas",
            "publication_record_date": None,
            "locator": "Person profile; staff sergeant, Company C, 2671st Special Reconnaissance Battalion",
            "access_date": "2026-10-30",
            "source_quality": "D_correlative_or_secondary",
            "collection_name": "World War II personnel profiles",
        },
        {
            "key": OSSOG_TSouderos,
            "stable_url": "https://ossog.info/balkans/greek_08.html",
            "title": "Greek Operational Group VIII",
            "author_creator": "OSS Operational Groups veterans history project",
            "repository_publisher": "OSS Operational Groups",
            "publication_record_date": None,
            "locator": "Personnel roster; Sergeant John E. Tsouderos",
            "access_date": "2026-10-30",
            "source_quality": "D_correlative_or_secondary",
            "collection_name": "OSS Operational Groups unit histories",
        },
        {
            "key": AFTER_BATTLE,
            "stable_url": "https://dokumen.pub/after-the-battle-behind-the-scenes-with-the-oss-in-greece-186.html",
            "title": "Behind the Scenes with the OSS in Greece",
            "author_creator": "Robert E. Perdue with James Chimbidis",
            "repository_publisher": "After the Battle, issue 186; online text mirror",
            "publication_record_date": "2020",
            "locator": "Issue 186, printed page 5; John E. Tsouderos biographical caption",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "After the Battle magazine",
            "rights_notes": "Only short excerpts and project-authored paraphrases are retained.",
        },
        {
            "key": DENSHO_TSURUTANI,
            "stable_url": "https://ddr.densho.org/media/ddr-densho-125/ddr-densho-125-165-mezzanine-52a2d5a3a9.htm",
            "archival_identifier": "denshopd-i125-00165",
            "title": "Manzanar Free Press pictorial: Legal Services",
            "author_creator": "Manzanar Free Press",
            "repository_publisher": "Densho Digital Repository",
            "publication_record_date": "1943-11-19",
            "locator": "Legal Services section; Director of Legal Aid Henry J. Tsurutani",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Manzanar Free Press",
        },
        {
            "key": PACIFIC_CITIZEN_TSURUTANI,
            "stable_url": "https://pacificcitizen.org/wp-content/uploads/archives-menu/Vol.021_%2305_Aug_04_1945.pdf",
            "title": "Pacific Citizen, volume 21, number 5",
            "author_creator": "Pacific Citizen",
            "repository_publisher": "Pacific Citizen archive",
            "publication_record_date": "1945-08-04",
            "locator": "Item identifying Henry J. Tsurutani as formerly an attorney in Los Angeles and then engaged in war work",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Pacific Citizen archive",
        },
        {
            "key": PRINCETON_TUCKER,
            "stable_url": "https://www.princeton.edu/news/2010/08/03/robert-tucker-renowned-soviet-expert-and-stalin-biographer-dies?section=facstaff",
            "title": "Robert Tucker, renowned Soviet expert and Stalin biographer, dies",
            "author_creator": "Princeton University Office of Communications",
            "repository_publisher": "Princeton University",
            "publication_record_date": "2010-08-03",
            "locator": "Obituary; Harvard degrees and OSS service from 1942 to 1944",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
        },
        {
            "key": WAPO_TUCKER,
            "stable_url": "https://www.washingtonpost.com/archive/local/2010/07/31/professor-was-scholar-of-sovietera-politics-and-history/8f697b4e-9060-4705-90ea-f33ecd727121/",
            "title": "Professor was scholar of Soviet-era politics and history",
            "author_creator": "Matt Schudel",
            "repository_publisher": "The Washington Post",
            "publication_record_date": "2010-07-31",
            "locator": "Obituary; Harvard education, intensive Russian-language training and OSS chronology",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "rights_notes": "Only project-authored paraphrases are retained.",
        },
        {
            "key": WAPO_TUCKERMAN,
            "stable_url": "https://www.washingtonpost.com/local/obituaries/laura-tuckerman-triest-100-dies/2012/09/02/7386116a-f453-11e1-a612-3cfc842a6d89_story.html",
            "title": "Laura Tuckerman Triest, 100, dies",
            "author_creator": "Matt Schudel",
            "repository_publisher": "The Washington Post",
            "publication_record_date": "2012-09-02",
            "locator": "Obituary; Depression-era dress-shop employment and 1942 work for William Donovan",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "rights_notes": "Only a short excerpt and project-authored paraphrases are retained.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": "army-field-artillery-b968",
            "organization_id": "04d90237-ae57-55c9-91fc-00744f8d6170",
            "canonical_name": "United States Army Field Artillery",
            "historical_name": "U.S. Army Field Artillery",
            "aliases": ["Field Artillery"],
            "organization_type": "Army branch",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "Existing canonical organization reused; military assignment remains distinct from civilian employment.",
        },
        {
            "key": "harvard-b968",
            "organization_id": "45ddf347-21c6-59f5-a8ae-517418adf941",
            "canonical_name": "Harvard University",
            "historical_name": "Harvard University",
            "aliases": ["Harvard"],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "Cambridge",
            "state_or_region": "Massachusetts",
            "country": "United States",
            "normalization_notes": "Existing canonical organization reused; Robert C Tucker's relationship is student status, never employment.",
        },
        {
            "key": "manzanar-legal-aid-b968",
            "canonical_name": "Manzanar Relocation Center Legal Aid Section",
            "historical_name": "Legal Aid Section, Manzanar Relocation Center",
            "aliases": ["Manzanar Legal Aid Section"],
            "organization_type": "federal relocation-center legal service",
            "sector": "federal_government",
            "city": "Manzanar",
            "state_or_region": "California",
            "country": "United States",
            "active_dates": "1942-1945",
            "normalization_notes": "Modeled as a government assignment at the historical center; no private employer or modern successor is inferred.",
        },
    ]


def occupation_affiliation(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    return {
        "key": f"{slug(PEOPLE[row][1])}-occupation-b968",
        "person_id": PEOPLE[row][0],
        "occupation": item["public_occupation"],
        "relationship_type": item["relationship"],
        "end_date": item["date"],
        "date_precision": f"Historical civilian-status code {item['code']} was recorded at Army entry on {item['date']}; no employer, school, workplace or OSS-transfer date is named.",
        "country": "United States",
        "immediate_pre_oss": False,
        "last_civilian_pre_service": False,
        "pre_oss_temporal_basis": "strongly_date_bounded",
        "identity_confidence": item["identity"],
        "claim_confidence": "medium",
        "source_quality": "A_direct_official",
        "publication_status": "publish_qualified",
        "research_notes": "The historical category is not converted into a named employer, school, workplace or immediate pre-OSS affiliation.",
    }


def specialist_affiliations() -> list[dict[str, object]]:
    return [
        {
            "key": "john-tsouderos-field-artillery-b968",
            "person_id": PEOPLE[28][0],
            "organization_key": "army-field-artillery-b968",
            "organization_name_as_found": "Field Artillery",
            "role_title": "enlisted soldier and trained medic",
            "relationship_type": "military_assignment",
            "start_date": "1942",
            "end_date": "1942-1943",
            "date_precision": "A scholarly unit history says Tsouderos qualified as a medic in July 1942 and served with Field Artillery before entering OSS; exact transfer date is unstated.",
            "country": "United States",
            "immediate_pre_oss": True,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "explicit_immediate",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "published",
            "research_notes": "Immediate military assignment, not a civilian employer.",
        },
        {
            "key": "john-tsouderos-waiter-b968",
            "person_id": PEOPLE[28][0],
            "occupation": "busboy or waiter",
            "relationship_type": "employment",
            "end_date": "1942",
            "date_precision": "The unit history states that he worked as a busboy or waiter until drafted; no employing establishment is named.",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": True,
            "pre_oss_temporal_basis": "explicit_immediate",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "published",
            "research_notes": "Best-supported last civilian occupation before Army service; the employer remains unidentified.",
        },
        {
            "key": "henry-tsurutani-manzanar-b968",
            "person_id": PEOPLE[29][0],
            "organization_key": "manzanar-legal-aid-b968",
            "organization_name_as_found": "Legal Aid Section, Manzanar Relocation Center",
            "role_title": "Director of Legal Aid",
            "occupation": "attorney",
            "relationship_type": "government_assignment",
            "start_date": "1942-1943",
            "end_date": "1943",
            "date_precision": "A November 1943 Manzanar publication identifies Tsurutani as Director of Legal Aid; the exact start and end dates are not established.",
            "city": "Manzanar",
            "state_or_region": "California",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "high_confidence",
            "claim_confidence": "medium",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "publish_qualified",
            "research_notes": "Government/legal-aid assignment; the evidence does not establish a private employer or prove that this was immediately before OSS.",
        },
        {
            "key": "henry-tsurutani-attorney-b968",
            "person_id": PEOPLE[29][0],
            "occupation": "attorney",
            "relationship_type": "unknown",
            "end_date": "1942",
            "date_precision": "A contemporary 1945 article describes him as formerly an attorney in Los Angeles; no firm, dates or employment arrangement is named.",
            "city": "Los Angeles",
            "state_or_region": "California",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "high_confidence",
            "claim_confidence": "medium",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "publish_qualified",
            "research_notes": "Occupation only; no law firm or self-employment relationship is inferred.",
        },
        {
            "key": "robert-c-tucker-language-training-b968",
            "person_id": PEOPLE[37][0],
            "role_title": "Russian-language trainee",
            "occupation": "student",
            "relationship_type": "student",
            "end_date": "1942",
            "date_precision": "The obituary places intensive Russian-language training after his 1941 Harvard master's degree and before his 1942 OSS service; no institution is named.",
            "country": "United States",
            "immediate_pre_oss": True,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "high_confidence",
            "claim_confidence": "medium",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "publish_qualified",
            "research_notes": "Immediate pre-OSS student/training status with the institution unresolved; not employment.",
        },
        {
            "key": "robert-c-tucker-harvard-b968",
            "person_id": PEOPLE[37][0],
            "organization_key": "harvard-b968",
            "organization_name_as_found": "Harvard University",
            "role_title": "graduate student",
            "occupation": "student",
            "relationship_type": "student",
            "start_date": "1935",
            "end_date": "1941",
            "date_precision": "Princeton records a Harvard bachelor's degree in 1939 and master's degree in 1941, followed by OSS service beginning in 1942.",
            "city": "Cambridge",
            "state_or_region": "Massachusetts",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "published",
            "research_notes": "Harvard is documented as an educational institution, not an employer.",
        },
        {
            "key": "laura-tuckerman-dress-shop-b968",
            "person_id": PEOPLE[41][0],
            "occupation": "dress-shop worker",
            "relationship_type": "employment",
            "end_date": "1930s",
            "date_precision": "The obituary places the job during the Depression and OSS work beginning in 1942; it does not name the shop or prove this was her last pre-OSS job.",
            "state_or_region": "District of Columbia",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "high_confidence",
            "claim_confidence": "medium",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "publish_qualified",
            "research_notes": "Earlier documented employment; the shop is unnamed and immediacy is not established.",
        },
    ]


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
    evidence_excerpt: str | None = None,
) -> dict[str, object]:
    value: dict[str, object] = {
        "key": key,
        "person_id": PEOPLE[row][0],
        "claim_type": claim_type,
        "claim_text": claim_text,
        "evidence_excerpt": evidence_excerpt,
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


def occupation_claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for item in ARMY_OCCUPATIONS:
        row = int(item["row"])
        name = PEOPLE[row][1]
        identity_sources = [{"source_key": INDEX}, {"source_key": ARMY}]
        identity_sources.extend({"source_key": key} for key in item["identity_sources"])
        identity_confidence = "confirmed" if item["identity"] == "confirmed" else "high"
        values.append(
            claim(
                row,
                f"identity-{slug(name)}-b968",
                "identity",
                f"Indexed {name} is {item['identity'].replace('_', '-')} matched to the reviewed Army entry and retained name variants.",
                item["identity_note"],
                item["identity_note"],
                "The Army entry date establishes military-entry chronology but not the date of OSS transfer.",
                "A_direct_official",
                identity_confidence,
                identity_sources,
                "Protected identifiers were used only for private resolution and remain absent from the evidence bundle and public output.",
            )
        )
        values.append(
            claim(
                row,
                f"occupation-{slug(name)}-b968",
                "other_pre_oss_affiliation" if item["relationship"] == "student" else "occupation",
                f"At Army entry on {item['date']}, {name}'s historical civilian-status category was {item['occupation'].lower()}.",
                f"The official Army field carries historical code {item['code']}; NARA's code list defines it as {item['occupation']}.",
                item["identity_note"],
                "Strongly date-bounded to Army entry; no employer, school, workplace or OSS-transfer date is named.",
                "A_direct_official",
                "medium",
                [
                    {"source_key": ARMY, "locator_override": "Accepted identity bridge; protected identifier and raw record withheld"},
                    {"source_key": TECH, "locator_override": "PDF physical pages 44-46; civilian-occupation field"},
                    {"source_key": CODES, "locator_override": item["locator"]},
                ],
                "Published as qualified occupation or student status only; excluded from verified-employer analytics.",
                f"{slug(name)}-occupation-b968",
                "publish_qualified",
            )
        )
    return values


def specialist_claims() -> list[dict[str, object]]:
    return [
        claim(
            28,
            "identity-john-tsouderos-b968",
            "identity",
            "Indexed John E Tsouderos is a high-confidence match to Sergeant John E. Tsouderos of the OSS Greek Operational Groups.",
            "An OSS unit roster and a detailed unit history supply the exact name, sergeant rank and Greek Operational Group service.",
            "High confidence from the exact uncommon full name, indexed protected identifier and matching direct OSS context.",
            "The sources document his Army pathway before OSS but do not give an exact OSS entry date.",
            "C_reputable_contemporary_or_scholarly",
            "high",
            [{"source_key": INDEX}, {"source_key": OSSOG_TSouderos}, {"source_key": AFTER_BATTLE}],
            "Family relationship is context only and is not used as the principal identity basis.",
        ),
        claim(
            28,
            "immediate-john-tsouderos-field-artillery-b968",
            "immediate_pre_oss_affiliation",
            "John E Tsouderos served with U.S. Army Field Artillery immediately before entering OSS.",
            "The unit history explicitly states that he served with Field Artillery before coming to OSS after qualifying as a medic.",
            "High-confidence exact-name match in two OSS Greek Operational Group sources.",
            "Explicit immediate sequence, although exact transfer dates and unit are unstated.",
            "C_reputable_contemporary_or_scholarly",
            "high",
            [{"source_key": AFTER_BATTLE, "excerpt_override": "had served with the Field Artillery before he came to the OSS"}, {"source_key": OSSOG_TSouderos, "support_type": "context_only"}],
            "Military assignment, not civilian employment.",
            "john-tsouderos-field-artillery-b968",
        ),
        claim(
            28,
            "last-civilian-john-tsouderos-waiter-b968",
            "last_civilian_pre_service",
            "John E Tsouderos worked as a busboy or waiter before he was drafted; the employer is not identified.",
            "The unit history explicitly places busboy or waiter work before his draft and subsequent Army and OSS service.",
            "High-confidence exact-name match in two OSS Greek Operational Group sources.",
            "Explicitly before the draft; no employer or precise dates are named.",
            "C_reputable_contemporary_or_scholarly",
            "high",
            [{"source_key": AFTER_BATTLE, "excerpt_override": "worked as a busboy or waiter until he was drafted"}],
            "Occupation and employment relationship are preserved without inventing a restaurant or hotel.",
            "john-tsouderos-waiter-b968",
        ),
        claim(
            29,
            "identity-henry-tsurutani-b968",
            "identity",
            "Indexed Henry J Tsurutani is a high-confidence match to attorney Henry J. Tsurutani of Manzanar's Legal Aid Section.",
            "A contemporary Manzanar publication and a 1945 Japanese American newspaper both supply the exact uncommon full name and legal profession.",
            "High confidence from the exact rare full name, wartime chronology and consistent legal profession across independent contemporary sources.",
            "The sources document wartime roles but do not state the exact date he entered OSS.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": INDEX}, {"source_key": DENSHO_TSURUTANI}, {"source_key": PACIFIC_CITIZEN_TSURUTANI}],
            "No employer or transfer sequence is inferred beyond the cited evidence.",
        ),
        claim(
            29,
            "prewar-henry-tsurutani-manzanar-b968",
            "other_pre_oss_affiliation",
            "Henry J Tsurutani served as Director of Legal Aid at the Manzanar Relocation Center.",
            "The November 1943 Manzanar Free Press identifies Henry J. Tsurutani as Director of Legal Aid in the center's Legal Aid Section.",
            "High-confidence exact rare-name identity with matching legal profession.",
            "Documented wartime role; its exact temporal relation to OSS entry remains uncertain.",
            "B_authoritative_institutional",
            "medium",
            [{"source_key": DENSHO_TSURUTANI, "excerpt_override": "Director of Legal Aid Henry J. Tsurutani"}],
            "Government assignment; no private employer or immediate-OSS sequence is asserted.",
            "henry-tsurutani-manzanar-b968",
            "publish_qualified",
        ),
        claim(
            29,
            "prewar-henry-tsurutani-attorney-b968",
            "occupation",
            "Henry J Tsurutani had worked as an attorney in Los Angeles before his wartime assignment; no firm is identified.",
            "A contemporary 1945 item describes him as formerly an attorney in Los Angeles before later war work.",
            "High-confidence exact rare-name identity with matching legal profession.",
            "Documented earlier occupation; no dates, firm or immediate relationship to OSS are supplied.",
            "C_reputable_contemporary_or_scholarly",
            "medium",
            [{"source_key": PACIFIC_CITIZEN_TSURUTANI}],
            "No law firm, self-employment status or named employer is inferred.",
            "henry-tsurutani-attorney-b968",
            "publish_qualified",
        ),
        claim(
            37,
            "identity-robert-c-tucker-b968",
            "identity",
            "Indexed Robert C Tucker is a high-confidence match to Soviet specialist Robert Charles Tucker, who served in OSS from 1942 to 1944.",
            "Princeton and The Washington Post independently supply his exact indexed name, Harvard chronology and 1942-1944 OSS service.",
            "High confidence from exact name and middle initial plus matching education, language specialty and explicit OSS service.",
            "Both sources date Harvard and language preparation before OSS service.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": INDEX}, {"source_key": PRINCETON_TUCKER}, {"source_key": WAPO_TUCKER}],
            "The identity is not based on later academic prominence alone.",
        ),
        claim(
            37,
            "immediate-robert-c-tucker-language-training-b968",
            "immediate_pre_oss_affiliation",
            "Immediately before OSS service, Robert C Tucker undertook intensive Russian-language training at an unidentified institution.",
            "The obituary places intensive Russian-language training after his Harvard degrees and immediately before his OSS work.",
            "High-confidence exact-name identity with explicit OSS chronology.",
            "Strongly date-bounded before OSS; training institution and exact dates are unresolved.",
            "C_reputable_contemporary_or_scholarly",
            "medium",
            [{"source_key": WAPO_TUCKER}],
            "Student/training status only; no employer is inferred.",
            "robert-c-tucker-language-training-b968",
            "publish_qualified",
        ),
        claim(
            37,
            "prewar-robert-c-tucker-harvard-b968",
            "other_pre_oss_affiliation",
            "Robert C Tucker was a Harvard University student, earning a bachelor's degree in 1939 and master's degree in 1941.",
            "Princeton records both Harvard degrees before his 1942 OSS service; The Washington Post independently confirms the chronology.",
            "High-confidence exact-name identity with explicit OSS chronology.",
            "Documented educational affiliation ending before OSS service.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": PRINCETON_TUCKER}, {"source_key": WAPO_TUCKER}],
            "Harvard is an educational institution here, never an employer.",
            "robert-c-tucker-harvard-b968",
        ),
        claim(
            41,
            "identity-laura-tuckerman-b968",
            "identity",
            "Indexed Laura W Tuckerman is a high-confidence match to Laura Wolcott Tuckerman Triest, who began wartime work for William Donovan in 1942.",
            "The obituary supplies the expanded exact name and direct chronology from 1942 work for Donovan into OSS duties.",
            "High confidence from the exact uncommon indexed name and explicit OSS chronology in a reputable obituary.",
            "The obituary dates the start of her wartime service but does not establish every intervening prewar role.",
            "C_reputable_contemporary_or_scholarly",
            "high",
            [{"source_key": INDEX}, {"source_key": WAPO_TUCKERMAN}],
            "The expanded name is retained as a documented variant.",
        ),
        claim(
            41,
            "prewar-laura-tuckerman-dress-shop-b968",
            "other_pre_oss_affiliation",
            "During the Depression, Laura W Tuckerman worked at an unnamed dress shop.",
            "The obituary records paid dress-shop work during the Depression and later OSS work beginning in 1942.",
            "High-confidence exact-name identity with explicit OSS chronology.",
            "Definitely pre-OSS, but not shown to be her immediate predecessor role or last civilian employer.",
            "C_reputable_contemporary_or_scholarly",
            "medium",
            [{"source_key": WAPO_TUCKERMAN, "excerpt_override": "worked at a dress shop"}],
            "The unnamed shop is not fabricated or normalized to an employer.",
            "laura-tuckerman-dress-shop-b968",
            "publish_qualified",
        ),
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
        base_update(
            row,
            identity_status="unresolved",
            identity_evidence=f"The visually verified index row supplies {PEOPLE[row][1]}, Box {'787' if row <= 29 else '788'} and archive location 230/86/42/03. {reason}",
            personnel_category="unknown_or_indeterminate",
            commissioned_officer=None,
            allied_or_foreign_personnel=False,
            research_status="requires_archival_review",
            next_action=f"Review the indexed personnel file for corroborating identifiers, immediate pre-OSS affiliation and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}",
        )
        for row, reason in UNRESOLVED.items()
    ]

    for item in ARMY_OCCUPATIONS:
        row = int(item["row"])
        extras: dict[str, object] = {}
        if item["variants"]:
            extras["name_variants"] = item["variants"]
        values.append(
            base_update(
                row,
                identity_status=item["identity"],
                identity_evidence=item["identity_note"],
                personnel_category="enlisted_army_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                research_status="occupation_only_found",
                next_action="Review the indexed personnel file to establish the immediate pre-OSS affiliation, wartime grade and named last civilian employer; do not convert the Army occupation category into a workplace.",
                **extras,
            )
        )

    values.extend(
        [
            base_update(28, identity_status="high_confidence", identity_evidence="An OSS Greek Operational Group roster and a detailed unit history supply the exact name, sergeant rank and Army-to-OSS pathway.", name_variants=["John E. Tsouderos"], personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="occupation_only_found", next_action="Review Box 787 for the exact Field Artillery unit, draft and OSS transfer dates, and the name of the restaurant or establishment where he worked."),
            base_update(29, identity_status="high_confidence", identity_evidence="The uncommon exact full name and legal profession appear in independent contemporary Manzanar and Japanese American newspaper sources.", name_variants=["Henry Junya Tsurutani"], personnel_category="civilian_professional_or_administrative_grade", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="occupation_only_found", next_action="Review Box 787 and War Relocation Authority records to establish the exact OSS entry date, administrative employment relationship and any named Los Angeles law firm."),
            base_update(37, identity_status="high_confidence", identity_evidence="Princeton and The Washington Post independently connect Robert C. Tucker/Robert Charles Tucker, Harvard education, Russian-language preparation and explicit 1942-1944 OSS service.", name_variants=["Robert Charles Tucker"], personnel_category="civilian_professional_or_administrative_grade", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="occupation_only_found", next_action="Review Box 788 and wartime training records to identify the Russian-language training institution and determine whether any civilian employer intervened after Harvard."),
            base_update(41, identity_status="high_confidence", identity_evidence="A reputable obituary supplies Laura Wolcott Tuckerman's exact expanded name and direct chronology from 1942 work for William Donovan into OSS duties.", name_variants=["Laura Wolcott Tuckerman", "Laura Tuckerman Triest"], personnel_category="civilian_professional_or_administrative_grade", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="occupation_only_found", next_action="Review Box 788 to identify the immediate 1942 recruitment pathway, the unnamed Depression-era dress shop and any intervening employment."),
        ]
    )
    return values


def research_attempts() -> list[dict[str, object]]:
    source_review_rows = {24, 26, 27, 28, 29, 35, 37, 39, 40, 41, 45}
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        if row in source_review_rows:
            outcome = "source_reviewed"
            reviewed = 6 if row in {24, 27, 28, 29, 37, 41} else 4
            rejected = 4
            detail = "Reviewed direct, institutional or contemporary evidence produced the qualified identity, occupation, student, government or military-pathway outcome recorded in the evidence bundle."
        else:
            outcome = "no_result"
            reviewed = 6
            rejected = 6
            detail = UNRESOLVED[row]
        attempts.append(
            {
                "key": f"page474-row{row}-{slug(name)}-b968",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index and official Archives context; CIA Reading Room or equivalent official-source check; exact-name and meaningful variants; OSS, Army, rank and unit clues; employer and occupation 1940; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Boxes 787-788; protected identifiers used only when defensible",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_968",
                "started_at": "2026-10-30T18:35:00Z",
                "completed_at": "2026-10-30T22:45:00Z",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search snippets, unsourced genealogy, people-finder pages, postwar-only employment leads and sources without an OSS, protected-identifier or personnel-file bridge were rejected. Historical occupation codes, military service and student status were not silently converted into employers.",
                "research_notes": f"{detail} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain, CIA Reading Room-equivalent and Library of Congress searches were checked as applicable. The index page, Army bulk file, technical documentation and occupation-code pages were inspected directly. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": f"Review the indexed Box {'787' if row <= 29 else '788'} personnel file for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before wartime service.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b968-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-968-v1",
        "reviewer": "Before OSS Batch 968 evidence review",
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
