#!/usr/bin/env python3
"""Generate the reviewed Batch 923 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "research/evidence-page452-carl-strahle-to-william-j-strauss-review_batch-923_2026-10-26.json"

INDEX = "nara-index-b923"
ARMY = "army-bulk-b923"
TECH = "army-tech-b923"
CODES = "army-codes-b923"
BOWDOIN = "bowdoin-arthur-stratton-b923"
CCU = "ccu-chester-strait-b923"
OREGON = "oregon-news-chester-strait-b923"
PROVIDENCE = "providence-directory-irving-strasmich-b923"
RIJHA = "rijha-irving-strasmich-b923"
MEMORIAL = "special-operations-memorial-ralph-stratis-b923"
SHD = "shd-jean-strauss-b923"
INFILTRATIONS = "infiltrations-jean-strauss-b923"


PEOPLE = {
    1: ("8cbb3774-7e59-5d55-bffb-53acecd22cd2", "Carl A Strahle"),
    2: ("f9da7ec5-13c9-58b9-82b6-d23563f5f9f7", "David C Strain"),
    3: ("87f3b2ad-f8df-51eb-b329-2e6f130f09c0", "Chester U Strait"),
    4: ("c94b3848-9fd5-5853-ba51-7d70a707f844", "Eric W Strait"),
    5: ("972a7829-ca52-58bc-9597-b70e0a545af6", "Mario C Strambi"),
    6: ("f756f79c-5861-5b36-b2e8-0a2439f88282", "Carl O Strand"),
    7: ("fa55068c-e7b6-5df7-8b60-c9d6f53b4719", "Philip R Strand"),
    8: ("ea04c4d9-241f-52fe-950c-4527a4c5de5a", "Gloria Strashun"),
    9: ("b2bac5dc-7654-5841-a2bb-8bd0ec1e87a1", "David T Strasinger"),
    10: ("8a29e7f0-d5a9-592c-bad5-39061fd0a0f1", "Irving H Strasmich"),
    11: ("1933c580-1550-57b5-b64b-a552134b0674", "John G Stratford"),
    12: ("2cd8072e-ab12-5eb2-958a-ee82f5e17bd1", "Ralph N Stratis"),
    13: ("17cdb2c1-6f4e-5de8-843c-b623c8b630e3", "Arthur Stratton"),
    14: ("e12f553f-c269-5280-83cd-a93ce1d9b25e", "Donald Stratton"),
    15: ("6a9c043b-80ce-5712-a398-4f494790d7ac", "Joseph M Straub"),
    16: ("4ee4ac5f-f8de-5020-b864-1f0a4d49d393", "Suzanne Straub"),
    17: ("a85c5a8e-d1a6-552c-8fd1-1f158bb6a41c", "Charles Straughn"),
    18: ("6891cabd-4f97-54fc-9124-8e47cc99cbe5", "Kenneth H Straus"),
    19: ("f36cfcbc-5657-5640-a1a9-5a790c938a5e", "Walter Straus"),
    20: ("80763df7-ed6d-5048-ab8d-0b02bfb25db2", "Frances C Strauss"),
    21: ("5e5dee83-05e7-57de-9f5c-516b74de4492", "Jean S Strauss"),
    22: ("445357d5-dcbd-553d-be0a-ce3195fef4aa", "Otto Strauss"),
    23: ("a0685439-62bd-583d-8ee2-402a9bdf6282", "William J Strauss"),
}


UNRESOLVED = {
    1: "An exact-name obituary described a printing career without establishing that it began before Army or OSS service; cemetery and document mirrors did not supply a defensible employer chronology.",
    4: "The index note is damaged or displaced, and exact-name and variant searches produced no defensible identity or affiliation bridge.",
    5: "The printed eight-digit identifier produced no Army bulk match, and discovery-only genealogy results supplied no OSS bridge.",
    6: "A different Carl O Strand Army row carried a conflicting identifier and was rejected as a namesake.",
    7: "Exact-name, occupation, employer, obituary, institutional, newspaper and archival searches produced no defensible identity bridge.",
    8: "Exact-name and variant searches produced no person-specific result with an OSS or Box 752 bridge.",
    11: "The PFC rank is preserved from the index, but common-name searches produced no second corroborating identifier or pre-OSS affiliation.",
    16: "Exact-name and variant searches produced no defensible wartime identity or employment evidence.",
    17: "Modern biographies and directory results concerned later-born or otherwise unbridged Charles Straughn namesakes.",
    20: "Exact-name and variant searches produced no defensible identity, employer or institutional result.",
}


ARMY_OCCUPATIONS = {
    2: {
        "code": "558",
        "occupation": "Meatcutters, except in slaughtering and packing houses",
        "entry_date": "1941-03-31",
        "code_locator": "PDF physical page 173; historical category 5-58",
    },
    9: {
        "code": "992",
        "occupation": "Students",
        "entry_date": "1943-04-02",
        "code_locator": "PDF physical page 304; corrected historical category 9-92",
    },
    14: {
        "code": "105",
        "occupation": "Clerks, general office",
        "entry_date": "1940-10-15",
        "code_locator": "PDF physical page 176; historical category 1-05",
    },
    15: {
        "code": "226",
        "occupation": "Cooks, except private family",
        "entry_date": "1941-01-27",
        "code_locator": "PDF physical page 172; historical category 2-26",
    },
    18: {
        "code": "992",
        "occupation": "Students",
        "entry_date": "1943-06-11",
        "code_locator": "PDF physical page 304; corrected historical category 9-92",
    },
    19: {
        "code": "148",
        "occupation": "Agents and appraisers, not elsewhere classified",
        "entry_date": "1943-03-15",
        "code_locator": "PDF physical page 176; historical category 1-48",
    },
    22: {
        "code": "965",
        "occupation": "Nonprocess occupations in manufacturing, not elsewhere classified",
        "entry_date": "1942-10-16",
        "code_locator": "PDF physical page 174; historical category 9-65, visually checked",
    },
    23: {
        "code": "304",
        "occupation": "Dairy farmers",
        "entry_date": "1943-03-08",
        "code_locator": "PDF physical page 176; historical category 3-04",
    },
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 751-752",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 452, rows 1-23; checked against layout-preserving text and a rendered page image",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. Full identifiers remain private. The Eric W Strait note and Jean S Strauss French rank note were visually verified.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; nine accepted and one rejected Batch 923 protected-identifier candidates",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "No raw row or full protected identifier is retained in public assets. The Ralph N Stratis/George Norman F conflict was rejected. Coded occupations identify no employer.",
        },
        {
            "key": TECH,
            "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf",
            "archival_identifier": "NN3-064-03-008; National Archives Identifier 1263923",
            "title": "World War II Army Enlistment Records: Reference Copy of Technical Documentation",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives at College Park - Electronic Records",
            "publication_record_date": "1994-2005; reference copy modified 2011",
            "locator": "PDF physical pages 44-46; identifier, name, Army-entry-date, grade and civilian-occupation fields",
            "access_date": "2026-10-26",
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
            "locator": "PDF physical pages 172-176 and 304; accepted Batch 923 categories visually checked, including 9-65 and corrected 9-92",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "The historical occupation categories identify neither an employer nor a workplace and are published only as qualified leads.",
        },
        {
            "key": BOWDOIN,
            "stable_url": "https://archivesspace.bowdoin.edu/repositories/2/resources/321",
            "archival_identifier": "M173",
            "title": "Arthur Stratton papers",
            "author_creator": "Emma Barton-Norris",
            "repository_publisher": "George J. Mitchell Department of Special Collections & Archives, Bowdoin College Library",
            "publication_record_date": "2023",
            "locator": "Biographical/Historical Note, lines 60-66",
            "access_date": "2026-10-26",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Arthur Stratton papers",
            "rights_notes": "The finding aid explicitly dates Robert College teaching to 1942-1944 and says he then joined OSS.",
        },
        {
            "key": CCU,
            "stable_url": "https://ccu.edu.mm/ccu-history/",
            "title": "CCU History",
            "author_creator": "Chin Christian University",
            "repository_publisher": "Chin Christian University",
            "locator": "History section, opening paragraph",
            "access_date": "2026-10-26",
            "source_quality": "B_authoritative_institutional",
            "rights_notes": "The institutional history names Rev Dr Chester U Strait as an American Baptist missionary who opened the Hakha Bible school in 1928.",
        },
        {
            "key": OREGON,
            "stable_url": "https://oregonnews.uoregon.edu/lccn/sn90051770/1942-05-11/ed-1/seq-1/",
            "archival_identifier": "sn90051770, 1942-05-11, edition 1, page 1",
            "title": "The Bend Bulletin",
            "repository_publisher": "Historic Oregon Newspapers, University of Oregon Libraries",
            "publication_record_date": "1942-05-11",
            "locator": "Page 1; Baptist convention notice naming Rev. Chester U. Strait",
            "access_date": "2026-10-26",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "rights_notes": "Contemporary newspaper context identifies him as a missionary to Burma in May 1942; it does not establish an OSS entry date.",
        },
        {
            "key": PROVIDENCE,
            "stable_url": "https://ldsgenealogy.com/RI/books/Polks-Providence-Providence-County-RI-city-directory-1942-part-270.htm",
            "title": "Polk's Providence city directory, 1942",
            "repository_publisher": "Polk directory reproduced by LDSGenealogy from Archive.org",
            "publication_record_date": "1942",
            "locator": "Part 270; Strasmich entries",
            "access_date": "2026-10-26",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "rights_notes": "The transcription names both a private law office and Rhode Island Division of Taxation role. The page warns that its transcription may contain OCR errors; exact wording is retained and corroborated separately.",
        },
        {
            "key": RIJHA,
            "stable_url": "https://rijha.org/wp-content/uploads/RIJH-Notes/Notes%20PDF/Notes%2012.2%201996.pdf",
            "title": "Early Rhode Island Jewish Lawyers",
            "repository_publisher": "Rhode Island Jewish Historical Association",
            "publication_record_date": "1996",
            "locator": "Rhode Island Jewish Historical Notes, volume 12.2, page 237",
            "access_date": "2026-10-26",
            "source_quality": "B_authoritative_institutional",
            "rights_notes": "The institutional roster identifies Irving H. Strasmich of Providence and gives his 1939 bar-admission date.",
        },
        {
            "key": MEMORIAL,
            "stable_url": "https://75thrra.org/wp-content/uploads/2022/11/2010_1.pdf",
            "title": "Patrolling, Summer 2010",
            "author_creator": "Special Operations Memorial Foundation",
            "repository_publisher": "75th Ranger Regiment Association",
            "publication_record_date": "2010-05-15",
            "locator": "PDF page 87, printed page 86; Special Operations Memorial Update",
            "access_date": "2026-10-26",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "rights_notes": "The memorial update says the OSS Society funded the Detachment 101 casualty names and includes T/SGT Ralph N. Stratis. It does not resolve the conflicting Army identifier.",
        },
        {
            "key": SHD,
            "stable_url": "https://www.servicehistorique.sga.defense.gouv.fr/sites/default/files/2019-10/SHDGR_INV_28P4_DOSSIERS_DES_AGENTS_DES_RESEAUX_0.pdf",
            "archival_identifier": "GR 28 P 4 394/74; GR 16 P 557827",
            "title": "Dossiers des agents des réseaux",
            "author_creator": "Service historique de la Défense",
            "repository_publisher": "Ministère des Armées, France",
            "publication_record_date": "2017",
            "locator": "Inventory entry GR 28 P 4 394/74, dossier individuel de Jean Strauss, 1943-1944",
            "access_date": "2026-10-26",
            "source_quality": "A_direct_official",
            "rights_notes": "The official inventory confirms a Jean Strauss resistance-network file but does not itself give rank, alias, employer or a pre-OSS role.",
        },
        {
            "key": INFILTRATIONS,
            "stable_url": "https://polejeanmoulin.com/resources/infiltrations_en_france.pdf",
            "title": "Historique 2ieme GM: Infiltrations en France",
            "repository_publisher": "Pôle Jean Moulin",
            "publication_record_date": "2017-12-31",
            "locator": "10 July 1944; Sussex/OSS Sanctuaire mission entry",
            "access_date": "2026-10-26",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "rights_notes": "The compiled chronology cites NARA M1623, an OSS Sanctuaire mission report, French military files and RAF logs. Its former SAS/FAFL statement is published only as a qualified lead.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": "robert-college-b923",
            "organization_id": "f1e21135-44f7-55fb-aad3-c0378ef5782f",
            "canonical_name": "Robert College",
            "historical_name": "Robert College",
            "aliases": [],
            "organization_type": "college",
            "sector": "academia_and_research",
            "city": "Istanbul",
            "country": "Turkey",
            "normalization_notes": "The historical institutional name is retained. The teaching job also served as cover for a separate intelligence assignment.",
        },
        {
            "key": "free-french-forces-b923",
            "organization_id": "e69cd54a-0807-54a9-b819-01cae8268999",
            "canonical_name": "Free French Forces",
            "historical_name": "Free French forces",
            "aliases": ["Forces françaises libres", "Free French"],
            "organization_type": "Allied military forces",
            "sector": "military",
            "country": "France",
            "active_dates": "1940-1944",
            "normalization_notes": "The source's wording is preserved; no specific French branch or unit is inferred.",
        },
        {
            "key": "american-baptist-foreign-mission-society-b923",
            "organization_id": "345ab958-cdb0-42c8-973f-6a7bde05e2b2",
            "canonical_name": "American Baptist Foreign Mission Society",
            "historical_name": "American Baptist Foreign Mission Society",
            "aliases": ["American Baptist mission", "American Baptist missionary service"],
            "organization_type": "missionary society",
            "sector": "labor_nonprofit_and_religion",
            "country": "United States",
            "normalization_notes": "The institutional source says American Baptist missionary. A separate Chin community history supplies the historical society name; the source wording remains visible.",
        },
        {
            "key": "rhode-island-division-taxation-b923",
            "organization_id": "50429896-84a6-4701-9df3-f759921e9ec8",
            "canonical_name": "Rhode Island Division of Taxation",
            "historical_name": "RI Div of Taxation",
            "aliases": ["Rhode Island Division of Taxation", "RI Div of Taxation"],
            "organization_type": "state government tax agency",
            "sector": "state_or_local_government",
            "city": "Providence",
            "state_or_region": "Rhode Island",
            "country": "United States",
            "normalization_notes": "Historical directory wording is preserved; no modern successor is substituted.",
        },
    ]


def affiliations() -> list[dict[str, object]]:
    result: list[dict[str, object]] = [
        {
            "key": "chester-strait-baptist-mission-b923",
            "person_id": PEOPLE[3][0],
            "organization_key": "american-baptist-foreign-mission-society-b923",
            "organization_name_as_found": "American Baptist missionary",
            "role_title": "missionary and Bible-school founder",
            "occupation": "missionary and educator",
            "relationship_type": "employment",
            "start_date": "1925",
            "end_date": "1940-12",
            "date_precision": "Institutional sources date the Hakha Bible school to 1928 and describe service between the world wars; a community history dates departure from Hakha to December 1940.",
            "city": "Hakha",
            "state_or_region": "Chin Hills",
            "country": "Burma",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "published",
            "research_notes": "A definite prewar institutional affiliation, but the reviewed sources do not prove it was immediately before OSS or identify the transition from missionary work to wartime service.",
        },
        {
            "key": "irving-strasmich-ri-taxation-b923",
            "person_id": PEOPLE[10][0],
            "organization_key": "rhode-island-division-taxation-b923",
            "organization_name_as_found": "RI Div of Taxation",
            "role_title": "tax research director",
            "occupation": "lawyer and tax researcher",
            "relationship_type": "government_assignment",
            "start_date": "1942",
            "end_date": "1943-10-27",
            "date_precision": "The 1942 city directory records the role; Army entry occurred on 1943-10-27. The exact end date and OSS transfer date are not stated.",
            "city": "Providence",
            "state_or_region": "Rhode Island",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": True,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "published",
            "research_notes": "The directory records this government role concurrently with private law practice. Neither is claimed as the immediate OSS predecessor.",
        },
        {
            "key": "irving-strasmich-law-practice-b923",
            "person_id": PEOPLE[10][0],
            "organization_name_as_found": "lawyer, 171 Westminster, room 312",
            "role_title": "lawyer",
            "occupation": "lawyer",
            "relationship_type": "self_employment",
            "start_date": "1942",
            "end_date": "1943-10-27",
            "date_precision": "The 1942 city directory gives a private office address; Army entry occurred on 1943-10-27. The exact end date and OSS transfer date are not stated.",
            "city": "Providence",
            "state_or_region": "Rhode Island",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": True,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "published",
            "research_notes": "No firm name is supplied. The role was concurrent with his Rhode Island tax assignment, so the two affiliations are not placed in an invented sequence.",
        },
        {
            "key": "arthur-stratton-robert-college-b923",
            "person_id": PEOPLE[13][0],
            "organization_key": "robert-college-b923",
            "organization_name_as_found": "Robert College",
            "role_title": "English teacher",
            "occupation": "teacher",
            "relationship_type": "employment",
            "start_date": "1942",
            "end_date": "1944",
            "date_precision": "Bowdoin's finding aid explicitly says he taught from 1942 to 1944, when he joined OSS; exact dates are not supplied.",
            "city": "Istanbul",
            "country": "Turkey",
            "immediate_pre_oss": True,
            "last_civilian_pre_service": True,
            "pre_oss_temporal_basis": "explicit_immediate",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "published",
            "research_notes": "The source explicitly links the end of this employment to joining OSS. Robert College's historical name is retained.",
        },
        {
            "key": "jean-strauss-free-french-b923",
            "person_id": PEOPLE[21][0],
            "organization_key": "free-french-forces-b923",
            "organization_name_as_found": "SAS FAFL",
            "role_title": "lieutenant",
            "relationship_type": "military_assignment",
            "end_date": "1944-07-10",
            "date_precision": "A compiled mission chronology describes Jean Strauss, alias Jean Sagan, as formerly SAS/FAFL before the 10 July 1944 OSS Sanctuaire mission; exact service dates are not supplied.",
            "country": "France",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "high_confidence",
            "claim_confidence": "medium",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "publish_qualified",
            "research_notes": "Military assignment, not civilian employment. The source's SAS/FAFL abbreviation is preserved and not expanded into a more specific unit without direct file review.",
        },
    ]
    for row, data in ARMY_OCCUPATIONS.items():
        relationship = "student" if data["occupation"] == "Students" else "employment"
        result.append(
            {
                "key": f"{slug(PEOPLE[row][1])}-occupation-b923",
                "person_id": PEOPLE[row][0],
                "occupation": data["occupation"],
                "relationship_type": relationship,
                "end_date": data["entry_date"],
                "date_precision": f"Historical civilian-occupation code {data['code']} was recorded at Army entry on {data['entry_date']}; no employer, school, workplace or OSS-transfer date is named.",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "A_direct_official",
                "publication_status": "publish_qualified",
                "research_notes": "The historical category is not converted into a named employer, school, institution, workplace or exact job title.",
            }
        )
    return result


def claims() -> list[dict[str, object]]:
    result: list[dict[str, object]] = [
        {
            "key": "identity-chester-strait-b923",
            "person_id": PEOPLE[3][0],
            "claim_type": "identity",
            "claim_text": "The indexed Chester U Strait is a high-confidence match to Rev. Dr. Chester U. Strait, the American Baptist missionary and educator in Hakha.",
            "evidence_excerpt": "Rev Dr Chester U Strait and spouse, an American Baptist missionary couple",
            "evidence_paraphrase": "Chin Christian University gives the exact distinctive name and identifies the Hakha missionary and Bible-school role.",
            "identity_match_assessment": "High confidence from exact first name, middle initial and surname plus a distinctive long-term institutional role documented by multiple Chin sources.",
            "temporal_assessment": "The missionary work is documented from 1925 through 1940; the reviewed sources do not establish his OSS entry date.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "The finding does not assume that missionary service was immediately before OSS or conflate later Army chaplaincy with civilian employment.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 452 row 3; Box 751; protected identifier withheld"},
                {"source_key": CCU, "locator_override": "History section, opening paragraph"},
                {"source_key": OREGON, "support_type": "context_only", "locator_override": "Page 1; May 1942 Baptist convention notice"},
            ],
        },
        {
            "key": "prewar-chester-strait-b923",
            "person_id": PEOPLE[3][0],
            "affiliation_key": "chester-strait-baptist-mission-b923",
            "claim_type": "other_pre_oss_affiliation",
            "claim_text": "Chester U. Strait served as an American Baptist missionary and educator in Hakha, establishing a Bible school in 1928; this is documented prewar work, not a proven immediate OSS predecessor.",
            "evidence_excerpt": "started a Bible school in Hakha in 1928",
            "evidence_paraphrase": "The institutional history names Strait and dates the Hakha Bible school to 1928; a contemporary 1942 newspaper still described him as a missionary to Burma.",
            "identity_match_assessment": "High-confidence match from the exact distinctive name and corroborating missionary chronology.",
            "temporal_assessment": "Definitely pre-OSS, but the transition to wartime service and OSS is not established.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "Organization wording is normalized separately and the historical source wording remains visible.",
            "sources": [
                {"source_key": CCU, "locator_override": "History section, opening paragraph"},
                {"source_key": OREGON, "support_type": "context_only", "locator_override": "Page 1; May 1942 Baptist convention notice"},
            ],
        },
        {
            "key": "identity-irving-strasmich-b923",
            "person_id": PEOPLE[10][0],
            "claim_type": "identity",
            "claim_text": "The indexed Irving H Strasmich is a high-confidence match to Providence lawyer and Rhode Island tax research director Irving H. Strasmich.",
            "evidence_excerpt": "Irving H lawyer ... also tax research dir RI Div of Taxation",
            "evidence_paraphrase": "The exact name, accepted protected Army identifier, 1942 directory entry and institutional bar-admission roster agree.",
            "identity_match_assessment": "High confidence from exact full-name agreement, a nonshared protected identifier, Providence location and independent professional records.",
            "temporal_assessment": "The directory documents both civilian roles in 1942; Army entry occurred on 1943-10-27.",
            "source_quality": "A_direct_official",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "The protected identifier is not exposed. Neither concurrent 1942 role is forced into an unsupported sequence.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 452 row 10; Box 752; protected identifier withheld"},
                {"source_key": ARMY, "locator_override": "Accepted reviewed identity bridge; protected identifier withheld"},
                {"source_key": PROVIDENCE, "locator_override": "Part 270; Strasmich entries"},
                {"source_key": RIJHA, "support_type": "context_only", "locator_override": "Volume 12.2, page 237"},
            ],
        },
        {
            "key": "last-civilian-irving-strasmich-tax-b923",
            "person_id": PEOPLE[10][0],
            "affiliation_key": "irving-strasmich-ri-taxation-b923",
            "claim_type": "last_civilian_pre_service",
            "claim_text": "In 1942 Irving H. Strasmich was tax research director for the Rhode Island Division of Taxation; the role is strongly date-bounded before his 1943 Army entry but not explicitly tied to OSS recruitment.",
            "evidence_excerpt": "tax research dir RI Div of Taxation",
            "evidence_paraphrase": "The 1942 city directory names the agency and role; the accepted official Army record dates entry to 1943-10-27.",
            "identity_match_assessment": "High-confidence identity from exact name, professional context and the accepted protected Army bridge.",
            "temporal_assessment": "Strongly date-bounded last civilian government role; exact end and OSS transition dates are unknown.",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "Government assignment is kept distinct from private law practice and from a civilian employer label.",
            "sources": [
                {"source_key": PROVIDENCE, "locator_override": "Part 270; Strasmich entries"},
                {"source_key": ARMY, "support_type": "context_only", "locator_override": "Accepted reviewed identity record; Army entry 1943-10-27; protected identifier withheld"},
            ],
        },
        {
            "key": "last-civilian-irving-strasmich-law-b923",
            "person_id": PEOPLE[10][0],
            "affiliation_key": "irving-strasmich-law-practice-b923",
            "claim_type": "last_civilian_pre_service",
            "claim_text": "Irving H. Strasmich also maintained a Providence law office in 1942; it was concurrent with his state tax role and no law-firm employer is named.",
            "evidence_excerpt": "lawyer 171 Westminster rm 312",
            "evidence_paraphrase": "The directory supplies a private office address, while the bar roster independently confirms his 1939 admission.",
            "identity_match_assessment": "High-confidence identity from exact name, Providence professional records and the accepted protected Army bridge.",
            "temporal_assessment": "Strongly date-bounded before Army entry, but the exact end date and sequence relative to the tax role are unknown.",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "Presented as self-employment; no firm or employer is invented.",
            "sources": [
                {"source_key": PROVIDENCE, "locator_override": "Part 270; Strasmich entries"},
                {"source_key": RIJHA, "support_type": "context_only", "locator_override": "Volume 12.2, page 237"},
            ],
        },
        {
            "key": "identity-ralph-stratis-b923",
            "person_id": PEOPLE[12][0],
            "claim_type": "identity",
            "claim_text": "The exact-name Ralph N. Stratis is documented as an OSS Detachment 101 technical sergeant, but the index's protected identifier selects a different Army name and remains in conflict.",
            "evidence_excerpt": "T/SGT Ralph N. Stratis",
            "evidence_paraphrase": "A special-operations memorial list funded by the OSS Society names Stratis among Detachment 101 losses; the Army identifier candidate names George Norman F and was rejected.",
            "identity_match_assessment": "The distinctive exact name and OSS unit support the indexed person, but the protected identifier conflict prevents a confirmed identity and blocks transfer of all Army fields.",
            "temporal_assessment": "The memorial establishes wartime OSS service, not a pre-OSS employer.",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "claim_confidence": "high",
            "publication_status": "publish_qualified",
            "match_notes": "The conflict is displayed rather than resolved by convenience. No occupation code from the rejected Army row is transferred.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 452 row 12; Box 752; protected identifier withheld"},
                {"source_key": MEMORIAL, "locator_override": "PDF page 87, printed page 86; Detachment 101 list"},
                {"source_key": ARMY, "support_type": "contradicts", "locator_override": "Rejected candidate; official row names George Norman F; protected identifier withheld"},
            ],
        },
        {
            "key": "identity-arthur-stratton-b923",
            "person_id": PEOPLE[13][0],
            "claim_type": "identity",
            "claim_text": "The indexed Arthur Stratton is a high-confidence match to author and educator Arthur Mills Stratton.",
            "evidence_excerpt": "Arthur Mills Stratton was born on July 27, 1911",
            "evidence_paraphrase": "Bowdoin's archival finding aid gives the full name and explicitly documents Robert College teaching followed by OSS service.",
            "identity_match_assessment": "High confidence from the exact name, an authoritative archival biography and the unusually specific Robert College-to-OSS chronology.",
            "temporal_assessment": "The finding aid dates Robert College employment to 1942-1944 and says he joined OSS in 1944.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "The index omits the middle name; it is added only as a documented variant.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 452 row 13; Box 752"},
                {"source_key": BOWDOIN, "locator_override": "Biographical/Historical Note, lines 60-66"},
            ],
        },
        {
            "key": "immediate-arthur-stratton-b923",
            "person_id": PEOPLE[13][0],
            "affiliation_key": "arthur-stratton-robert-college-b923",
            "claim_type": "immediate_pre_oss_affiliation",
            "claim_text": "Arthur Mills Stratton taught English at Robert College in Turkey from 1942 to 1944, when he joined OSS.",
            "evidence_excerpt": "taught English at Robert College in Turkey from 1942 to 1944, when he joined",
            "evidence_paraphrase": "The Bowdoin archival finding aid explicitly links the dated employment to his entry into OSS.",
            "identity_match_assessment": "High-confidence identity from the authoritative full-name biography and direct OSS chronology.",
            "temporal_assessment": "Explicit immediate predecessor: the source says the teaching ended when he joined OSS in 1944.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "Robert College is retained as the historical employer name; no modern institution is substituted.",
            "sources": [{"source_key": BOWDOIN, "locator_override": "Biographical/Historical Note, line 63"}],
        },
        {
            "key": "identity-jean-strauss-b923",
            "person_id": PEOPLE[21][0],
            "claim_type": "identity",
            "claim_text": "The indexed French Lieutenant Jean S Strauss is a high-confidence match to Jean Strauss, alias Jean Sagan, of the OSS Sanctuaire mission.",
            "evidence_excerpt": "Jean Strauss alias Jean Sagan",
            "evidence_paraphrase": "The exact name, French military context, OSS mission chronology and official French resistance-network dossier align.",
            "identity_match_assessment": "High confidence from the exact name, French lieutenant note, a specific OSS mission and an official French dossier for Jean Strauss covering 1943-1944.",
            "temporal_assessment": "The official dossier covers 1943-1944; the mission chronology dates Sanctuaire to July 1944.",
            "source_quality": "A_direct_official",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "The Sagan alias is retained as a documented variant. The official inventory alone does not supply the alias, so the compiled chronology remains separately cited.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 452 row 21; LT; French note; Box 752"},
                {"source_key": SHD, "locator_override": "GR 28 P 4 394/74; GR 16 P 557827; 1943-1944"},
                {"source_key": INFILTRATIONS, "locator_override": "10 July 1944; OSS Sanctuaire mission entry"},
            ],
        },
        {
            "key": "preoss-jean-strauss-free-french-b923",
            "person_id": PEOPLE[21][0],
            "affiliation_key": "jean-strauss-free-french-b923",
            "claim_type": "other_pre_oss_affiliation",
            "claim_text": "A compiled mission chronology describes Jean Strauss, alias Jean Sagan, as formerly SAS/FAFL before his July 1944 OSS Sanctuaire mission; the exact unit and dates require file review.",
            "evidence_excerpt": "Jean Strauss alias Jean Sagan ... Ex SAS FAFL 35721",
            "evidence_paraphrase": "The chronology places a Free French/SAS antecedent before the named OSS mission and cites NARA, French military and RAF records.",
            "identity_match_assessment": "High-confidence person match, but the antecedent service detail depends on a compiled chronology rather than a reviewed personnel file.",
            "temporal_assessment": "Earlier than the July 1944 OSS mission, but exact start and end dates are not established.",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "claim_confidence": "medium",
            "publication_status": "publish_qualified",
            "match_notes": "Military assignment, not civilian employment. The source abbreviation is preserved and the exact unit remains an archival-review question.",
            "sources": [
                {"source_key": INFILTRATIONS, "locator_override": "10 July 1944; OSS Sanctuaire mission entry"},
                {"source_key": SHD, "support_type": "context_only", "locator_override": "Official Jean Strauss dossier inventory, 1943-1944"},
            ],
        },
    ]

    for row, data in ARMY_OCCUPATIONS.items():
        name = PEOPLE[row][1]
        result.append(
            {
                "key": f"identity-{slug(name)}-b923",
                "person_id": PEOPLE[row][0],
                "claim_type": "identity",
                "claim_text": f"The indexed {name} row is a high-confidence match to the reviewed official Army record.",
                "evidence_paraphrase": "A nonshared protected identifier and compatible name connect the visually verified index row to the official Army record.",
                "identity_match_assessment": "High confidence from exact full-name agreement and a nonshared protected-identifier bridge.",
                "temporal_assessment": f"The Army entry is dated {data['entry_date']}; it does not establish an OSS transfer date.",
                "source_quality": "A_direct_official",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "No protected identifier is exposed, and the historical occupation is kept separate from employer claims.",
                "sources": [
                    {"source_key": INDEX, "locator_override": f"PDF page 452 row {row}; Box 752; protected identifier withheld"},
                    {"source_key": ARMY, "locator_override": "Accepted reviewed identity bridge; protected identifier withheld"},
                ],
            }
        )
        article = "an" if data["occupation"].lower().startswith(tuple("aeiou")) else "a"
        if data["occupation"] == "Students":
            claim_text = f"At Army entry on {data['entry_date']}, {name} was recorded in the historical occupation group Students; no school or employer is identified."
        else:
            claim_text = f"At Army entry on {data['entry_date']}, {name} was recorded in {article} historical occupation category, {data['occupation']}; no employer is identified."
        result.append(
            {
                "key": f"occupation-{slug(name)}-b923",
                "person_id": PEOPLE[row][0],
                "affiliation_key": f"{slug(name)}-occupation-b923",
                "claim_type": "occupation",
                "claim_text": claim_text,
                "evidence_excerpt": data["occupation"],
                "evidence_paraphrase": f"The accepted Army record carries civilian-occupation code {data['code']}, decoded from NARA's official code list.",
                "identity_match_assessment": "The category belongs only to the reviewed protected-identifier match; the identifier itself is not public.",
                "temporal_assessment": "Strongly date-bounded to Army entry; it does not establish the immediate pre-OSS affiliation or a named employer.",
                "source_quality": "A_direct_official",
                "claim_confidence": "medium",
                "publication_status": "publish_qualified",
                "match_notes": "The historical category is a qualified lead, not a named employer, school, institution, workplace or exact title.",
                "sources": [
                    {"source_key": ARMY, "locator_override": f"Accepted reviewed identity record; civilian occupation code {data['code']}; protected identifier withheld"},
                    {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46; Army-entry-date and civilian-occupation fields"},
                    {"source_key": CODES, "locator_override": data["code_locator"], "excerpt_override": data["occupation"]},
                ],
            }
        )
    return result


def unresolved_update(row: int) -> dict[str, object]:
    person_id, name = PEOPLE[row]
    category = "unknown_or_indeterminate"
    commissioned: bool | None = None
    if row == 1:
        category = "commissioned_army_officer"
        commissioned = True
    elif row == 11:
        category = "enlisted_army_personnel"
        commissioned = False
    return {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, rank where printed, Box 751 or 752 and archive location, but staged NARA/index, CIA Reading Room, exact-name OSS, occupation, employer, obituary, institutional, newspaper and archival searches found no defensible identity bridge. {UNRESOLVED[row]}",
        "personnel_category": category,
        "commissioned_officer": commissioned,
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": "Review the indexed personnel file for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "critical",
    }


def person_updates() -> list[dict[str, object]]:
    updates = [unresolved_update(row) for row in UNRESOLVED]
    updates.extend(
        [
            {
                "person_id": PEOPLE[3][0],
                "identity_status": "high_confidence",
                "identity_evidence": "The exact distinctive name and Chin institutional histories identify Rev. Dr. Chester U. Strait as an American Baptist missionary and educator in Hakha before World War II.",
                "name_variants": ["Rev. Dr. Chester U. Strait", "Chester Ulysses Strait"],
                "personnel_category": "civilian_professional_or_administrative_grade",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "documented_prewar_employer_found",
                "next_action": "Review Box 751 for the wartime transition from missionary work to any Army or OSS assignment. The American Baptist affiliation is documented prewar, not proven immediate.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[10][0],
                "identity_status": "high_confidence",
                "identity_evidence": "Exact name, a nonshared protected Army identifier, a 1942 Providence directory and an institutional bar roster identify lawyer and Rhode Island tax research director Irving H. Strasmich.",
                "personnel_category": "enlisted_army_personnel",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "verified_employer_found",
                "next_action": "Review Box 752 for the exact end dates of the concurrent law and Rhode Island tax roles and for the immediate OSS recruitment or transfer chronology.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[12][0],
                "identity_status": "conflicting",
                "identity_evidence": "An OSS Society-supported memorial list identifies T/SGT Ralph N. Stratis in OSS Detachment 101, but the protected index identifier selects an official Army row named George Norman F. The conflict blocks transfer of every Army field.",
                "personnel_category": "enlisted_army_personnel",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "conflicting_sources",
                "next_action": "Review Box 752 to establish the correct protected identifier and pre-OSS affiliation. Do not use occupation code 736 from the rejected Army row.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[13][0],
                "identity_status": "high_confidence",
                "identity_evidence": "Bowdoin's authoritative archival biography identifies Arthur Mills Stratton and explicitly connects his 1942-1944 Robert College teaching to joining OSS.",
                "name_variants": ["Arthur Mills Stratton"],
                "personnel_category": "civilian_professional_or_administrative_grade",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": False,
                "manual_review_required": False,
                "research_status": "verified_employer_found",
                "next_action": "Review Box 752 only to refine the exact 1944 OSS entry date and assignment; the immediate Robert College employment is already explicit.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "not_required",
            },
            {
                "person_id": PEOPLE[21][0],
                "identity_status": "high_confidence",
                "identity_evidence": "The exact name, indexed French lieutenant rank, official 1943-1944 French resistance-network dossier and OSS Sanctuaire mission chronology identify Jean Strauss, alias Jean Sagan.",
                "name_variants": ["Jean Strauss", "Jean Sagan"],
                "personnel_category": "foreign_or_allied_military_personnel",
                "commissioned_officer": True,
                "allied_or_foreign_personnel": True,
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Review the French GR 28 P 4 394/74 and GR 16 P 557827 files plus Box 752 to establish exact SAS/FAFL unit, dates and any earlier civilian employment.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
        ]
    )
    for row, data in ARMY_OCCUPATIONS.items():
        updates.append(
            {
                "person_id": PEOPLE[row][0],
                "identity_status": "high_confidence",
                "identity_evidence": "An exact full name and nonshared protected identifier connect the index row to the official Army record.",
                "personnel_category": "enlisted_army_personnel",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "occupation_only_found",
                "next_action": f"Review Box 752 to identify the immediate pre-OSS affiliation and last civilian employer; do not convert the Army category '{data['occupation']}' into a named employer or institution.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            }
        )
    return updates


def research_attempts() -> list[dict[str, object]]:
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        if row == 3:
            outcome = "source_reviewed"
            detail = "Institutional and contemporary sources established high-confidence identity and American Baptist missionary and educational work in Hakha, but not the immediate OSS transition."
            sources_reviewed, rejected = 8, 3
        elif row == 10:
            outcome = "source_reviewed"
            detail = "An accepted Army bridge, 1942 city directory and bar roster established high-confidence identity, concurrent private law practice and a Rhode Island tax-research role before 1943 Army entry."
            sources_reviewed, rejected = 9, 3
        elif row == 12:
            outcome = "candidate_rejected"
            detail = "Independent evidence identifies T/SGT Ralph N. Stratis in OSS Detachment 101, but the protected identifier selects George Norman F; the Army candidate and every attached field were rejected."
            sources_reviewed, rejected = 8, 5
        elif row == 13:
            outcome = "source_reviewed"
            detail = "Bowdoin's archival finding aid established high-confidence identity and explicit immediate Robert College employment from 1942 to the 1944 OSS entry."
            sources_reviewed, rejected = 7, 2
        elif row == 21:
            outcome = "source_reviewed"
            detail = "An official French dossier inventory and a cited mission chronology established high-confidence identity and a qualified former SAS/FAFL military antecedent, but no civilian employer."
            sources_reviewed, rejected = 9, 4
        elif row in ARMY_OCCUPATIONS:
            outcome = "source_reviewed"
            detail = f"An accepted protected-identifier Army bridge established identity and a dated historical category, {ARMY_OCCUPATIONS[row]['occupation']}, but no named employer or institution."
            sources_reviewed, rejected = 6, 3
        elif row in {1, 5, 6, 11, 17}:
            outcome = "candidate_rejected"
            detail = UNRESOLVED[row]
            sources_reviewed, rejected = 6, 5
        else:
            outcome = "no_result"
            detail = UNRESOLVED[row]
            sources_reviewed, rejected = 5, 3
        attempts.append(
            {
                "key": f"page452-row{row}-{slug(name)}-b923",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA/index and public Archives context; CIA Reading Room site-restricted exact-name check; OSS and rank variants; employer and occupation; obituary, institutional, newspaper, directory and archival searches; Boxes 751-752; protected-identifier Army crosswalk where defensible",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_923",
                "started_at": "2026-10-26T10:04:00Z",
                "completed_at": "2026-10-26T10:34:00Z",
                "outcome": outcome,
                "sources_reviewed": sources_reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, discovery-only genealogy or people-finder results, wrong identifiers, wrong initials, postwar-only leads and sources without an OSS or Box-file bridge were not assigned." if outcome == "source_reviewed" else detail,
                "research_notes": f"{detail} The CIA adapter failed closed on its robots check; separate site-restricted public Reading Room searches returned no exact-name result. The Library of Congress adapter failed before returning results, so institutional, obituary, newspaper, directory and archival web searches supplied the alternative protocol step. No search snippet was used as final evidence, no access control was bypassed, and no authenticated NARA API call was made.",
                "next_action": "Review the indexed personnel file for corroborating identifiers and the immediate pre-OSS affiliation or last civilian employer.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b923-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-923-v1",
        "reviewer": "Before OSS Batch 923 evidence review",
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
