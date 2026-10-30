#!/usr/bin/env python3
"""Generate the reviewed Batch 974 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page477-joe-ulmer-to-morris-unterberger-"
    "review_batch-974_2026-10-30.json"
)

INDEX = "nara-index-b974"
ARMY = "army-bulk-b974"
TECH = "army-tech-b974"
CODES = "army-codes-b974"
PHS_UNDERHILL = "phs-irvin-underhill-papers-b974"
PHS_UNDERHILL_BIO = "phs-irvin-underhill-biography-b974"
SOGANG_UNDERWOOD = "aks-discovering-korea-underwood-b974"
UCLA_MISSIONARIES = "ucla-korean-christianity-underwood-b974"
KOREA_NET = "korea-net-underwood-family-b974"
KOREA_SOCIETY = "korea-society-horace-underwood-b974"
YONSEI_ARCHIVES = "yonsei-horace-underwood-b974"
BERKELEY_IHOUSE = "berkeley-ihouse-warren-unna-b974"
EIGHTH_AFHS = "eighth-afhs-matthew-ungerleider-b974"
JAVA_MIS = "java-mis-registry-kazuo-unoki-b974"
INTERMENT_ULVESAKER = "interment-nels-ulvesaker-b974"

PHA = "philadelphia-housing-authority-b974"
WEST_AFRICA_MISSION = "pcusa-west-africa-mission-b974"
YONHI = "yonhi-college-b974"
US_NAVY = "united-states-navy-b974"
UC_BERKELEY = "uc-berkeley-b974"


PEOPLE = {
    24: ("c2108c77-94f6-5ba8-84e9-f531f877b938", "Joe W Ulmer"),
    25: ("34363099-20a9-5b4b-8a83-685bf9d192d1", "Kent D Ulrich"),
    26: ("69b2549a-bd6a-550e-8fd7-f425eb57491b", "Nels Ulvesaker"),
    27: ("a776790f-bf8a-5001-973b-6b39190ef45a", "Robert A Ulving"),
    28: ("a382a962-571b-561f-8516-02c7fa2c1064", "George A Uman"),
    29: ("e1c04578-f0d6-50b2-b0a2-6d95c4c8fe50", "Karl S Umberger"),
    30: ("2d98d4a5-9a9c-5a05-b25e-a2a75dc34c26", "Marcia Umbsen"),
    31: ("0deabb2f-7b88-5a56-be9c-b618edbfdabd", "Max E Umpleby"),
    32: ("f2db89b9-b496-5f4d-afbd-1f110e601ad5", "Irvin W Underhill"),
    33: ("9291090f-d334-5c13-810a-7b918a350b3e", "Claire Leon Underwood"),
    34: ("e4ca0559-3f57-518f-bc12-d94fbba57a43", "Gailey B Underwood"),
    35: ("7883ec1d-e618-57e5-a553-4a80d47d04ea", "George W Underwood"),
    36: ("536de873-11c1-5341-988c-7f520d5a26b9", "Horace H Underwood"),
    37: ("89066262-89dc-577e-9b54-b46aad1f4cfb", "Horace G Underwood"),
    38: ("3fa535e8-ad0d-56b7-8685-66c144a2890b", "Irene J Underwood"),
    39: ("153d29a7-046b-536b-82b9-e25df61ee401", "James B Underwood"),
    40: ("c3136cd5-cbac-5260-b604-0a32476975eb", "Orval Underwood"),
    41: ("d6e53de7-07ac-5a66-8bff-f679ce8273bb", "Richard F Underwood"),
    42: ("465d1553-ecba-5ac8-9585-df2a4f744703", "William A Underwood"),
    43: ("93cafd62-5e8c-5d6d-b5dd-c4dbb9a7bbcd", "Matthew J Ungerleider"),
    44: ("a09cf2e4-ef7f-5d2d-be17-227cdd2ef24e", "Warren W Unna"),
    45: ("261b84f9-c78f-5894-80e6-f05f0e2a6c1c", "Kazuo Unoki"),
    46: ("fafe63fd-3da6-5268-a85f-7deef1c12d88", "Morris Unterberger"),
}


ARMY_OCCUPATIONS = [
    {
        "row": 25,
        "date": "1942-08-19",
        "code": "583",
        "occupation": "Mechanics and repairmen, not elsewhere classified",
        "public_occupation": "mechanic or repairman, not elsewhere classified",
        "relationship_type": "unknown",
        "temporal_basis": "documented_prewar",
        "locator": "PDF physical pages 175-176; category 5-83 Mechanics and repairmen, n.e.c.",
    },
    {
        "row": 31,
        "date": "1943-03-10",
        "code": "992",
        "occupation": "Students",
        "public_occupation": "student",
        "relationship_type": "student",
        "temporal_basis": "documented_prewar",
        "locator": "Corrected Code No. 30, PDF physical page 304; category 9-92 Students",
    },
    {
        "row": 41,
        "date": "1945-06-27",
        "code": "992",
        "occupation": "Students",
        "public_occupation": "student",
        "relationship_type": "student",
        "temporal_basis": "temporal_relation_uncertain",
        "locator": "Corrected Code No. 30, PDF physical page 304; category 9-92 Students",
    },
    {
        "row": 43,
        "date": "1942-12-02",
        "code": "138",
        "occupation": "Stock clerks",
        "public_occupation": "stock clerk",
        "relationship_type": "unknown",
        "temporal_basis": "documented_prewar",
        "locator": "PDF physical page 176; category 1-38 Stock clerks",
    },
]


UNRESOLVED = {
    24: "A protected identifier did not produce an exact Army bulk match, and common-name searches did not yield an OSS or Box 793 identity bridge.",
    26: "A VA-derived cemetery transcription and a specialist Camp Ritchie roster contain the uncommon name Nels Ulvesaker, but neither connects the person to Box 793 or a pre-OSS employer.",
    27: "A birth-and-death lead for a Robert A Ulving did not supply an OSS, archival-box, occupation or employer bridge.",
    28: "Exact-name and date-only leads for George A Uman lacked an OSS, Box 794, occupation or employer bridge.",
    29: "A county historical archive lists Karl Stafford Umberger wartime letters, but the finding-aid lead does not establish OSS identity or a pre-OSS affiliation.",
    30: "A 1932 San Francisco social-register entry for Marcia Umbsen establishes neither occupation nor the indexed OSS identity.",
    33: "A modern obituary candidate for Claire Leon Underwood lacked an OSS, Box 794 or wartime identity bridge.",
    34: "Newspaper and directory searches for Gailey B Underwood produced no defensible wartime identity or employer evidence.",
    35: "The common name George W Underwood produced unrelated namesakes and no two corroborating identifiers beyond the name.",
    38: "An Irène J. Underwood archival name lead was rejected because no source connected it to OSS, Box 794 or the indexed person.",
    39: "The common name James B Underwood produced unrelated records and no source with two corroborating identifiers beyond the name.",
    40: "Exact-name, obituary, institutional, newspaper and archival searches produced no defensible identity bridge for Orval Underwood.",
    42: "The common name William A Underwood and a protected-identifier Army nonmatch yielded no defensible OSS identity or employer evidence.",
    46: "Exact-name, occupation, obituary, institutional and archival searches produced no defensible OSS identity or pre-OSS affiliation for Morris Unterberger.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 793-794",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 477, rows 24-46; checked against layout-preserving text and an original-detail page render",
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
            "locator": "Official unrestricted ASNEF.FIN.DAT; four Batch 974 identity comparisons; protected identifiers and record ordinals withheld",
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
            "locator": "PDF physical pages 175-176 and corrected page 304; Batch 974 categories visually and textually checked",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical categories identify neither employers nor workplaces and are retained only where needed for auditability.",
        },
        {
            "key": PHS_UNDERHILL,
            "stable_url": "https://pcusa.org/historical-society/collections/research-tools/guides-archival-collections/rg-418",
            "archival_identifier": "Presbyterian Historical Society RG 418",
            "title": "Guide to the Irvin Windfield Underhill Papers",
            "author_creator": "Bill Brock, Collection Management Archivist",
            "repository_publisher": "Presbyterian Historical Society",
            "publication_record_date": "2006-02",
            "locator": "Biographical note and collection overview; missionary, housing-authority and wartime OSS-consulting chronology",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Irvin Windfield Underhill Papers",
        },
        {
            "key": PHS_UNDERHILL_BIO,
            "stable_url": "https://pcusa.org/news-storytelling/blogs/historical-society-blog/african-american-leaders-irvin-windfield-underhill-jr",
            "title": "African American Leaders: Irvin Windfield Underhill, Jr.",
            "author_creator": "Presbyterian Historical Society staff",
            "repository_publisher": "Presbyterian Historical Society",
            "publication_record_date": "2023-08-07",
            "locator": "Biography; West Africa Mission, 1940 return and Philadelphia Housing Authority chronology",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "African American Leaders Series",
        },
        {
            "key": SOGANG_UNDERWOOD,
            "stable_url": "https://anthony.sogang.ac.kr/DiscoveringKorea.pdf",
            "archival_identifier": "ISBN 978-89-7105-794-0-93910",
            "title": "Discovering Korea at the Start of the Twentieth Century",
            "author_creator": "Brother Anthony, editor",
            "repository_publisher": "Academy of Korean Studies; Sogang University author site",
            "publication_record_date": "2011",
            "locator": "Preface, The Underwood family, PDF page 14; Horace Horton Underwood chronology",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Royal Asiatic Society Korea Branch historical essays",
        },
        {
            "key": UCLA_MISSIONARIES,
            "stable_url": "https://koreanchristianity.cdh.ucla.edu/biographies/missionaries/",
            "title": "Missionaries",
            "author_creator": "UCLA Online Archive Korean Christianity",
            "repository_publisher": "University of California, Los Angeles",
            "publication_record_date": None,
            "locator": "Missionary roster: Horace Horton Underwood (1890-1951), Northern Presbyterian mission, 1912-1951",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "UCLA Online Archive Korean Christianity",
        },
        {
            "key": KOREA_NET,
            "stable_url": "https://www.korea.net/NewsFocus/Culture/view?articleId=178962",
            "title": "US family that helped shape modern Korea",
            "author_creator": "Jeon Han",
            "repository_publisher": "Korea.net, Korean Culture and Information Service",
            "publication_record_date": "2019-11-07",
            "locator": "Like father, like son section; distinguishes Horace Horton Underwood from his eldest son Horace Grant Underwood",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Korea.net Culture",
        },
        {
            "key": KOREA_SOCIETY,
            "stable_url": "https://www.koreasociety.org/signature-events/van-fleet-award/2002-van-fleet-award/",
            "title": "2002 Van Fleet Award Honoree: Horace G. Underwood",
            "author_creator": "The Korea Society",
            "repository_publisher": "The Korea Society",
            "publication_record_date": "2002-10-11",
            "locator": "Honoree biography; Chosen Christian College teaching, Japanese internment, repatriation and U.S. Navy language-officer service",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "James A. Van Fleet Award honorees",
        },
        {
            "key": YONSEI_ARCHIVES,
            "stable_url": "https://archives.yonsei.ac.kr/Contents_PlanContents/view/1575",
            "title": "Horace Grant Underwood II (1917-2004)",
            "author_creator": "Yonsei University Archives",
            "repository_publisher": "Yonsei University Archives",
            "publication_record_date": "2024",
            "locator": "Biographical chronology: missionary appointment 1939, English instructor 1940-1941, U.S. Navy 1942-1946",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Twentieth anniversary of Horace Grant Underwood II",
        },
        {
            "key": BERKELEY_IHOUSE,
            "stable_url": "https://ihouse.berkeley.edu/sites/default/files/ihtimesfall2019.pdf",
            "title": "International House Times, Fall 2019",
            "author_creator": "International House Berkeley",
            "repository_publisher": "University of California, Berkeley",
            "publication_record_date": "2019",
            "locator": "PDF printed page 20; Warren Unna memorial",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "International House Times",
        },
        {
            "key": EIGHTH_AFHS,
            "stable_url": "https://www.8thafhs.org/wp-content/uploads/2024/09/2024-9RD.pdf",
            "title": "Eighth Air Force News, September 2024",
            "author_creator": "Eighth Air Force Historical Society",
            "repository_publisher": "Eighth Air Force Historical Society",
            "publication_record_date": "2024-09",
            "locator": "PDF page 10; Tec4 Matthew Ungerleider, Headquarters Detachment, OSS",
            "access_date": "2026-10-30",
            "source_quality": "D_correlative_or_secondary",
            "collection_name": "Eighth Air Force News",
        },
        {
            "key": JAVA_MIS,
            "stable_url": "https://java-us.org/wp-content/uploads/2023/09/8.pdf",
            "title": "Military Intelligence Service Registry Merged (alphabetical)",
            "author_creator": "Seiki Oshiro, Paul Tani, Mitzi Matsui and Grant Ichikawa, compilers",
            "repository_publisher": "Japanese American Veterans Association",
            "publication_record_date": "2023-09",
            "locator": "PDF page 186 of 418; Kazuo Unoki, Fort Snelling 1946 class",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Military Intelligence Service registry",
            "rights_notes": "The registry's service identifier was compared privately; only the matching numeric-sequence assessment is retained, never the number itself.",
        },
        {
            "key": INTERMENT_ULVESAKER,
            "stable_url": "https://www.interment.net/united-states/oregon/multnomah-county/portland/willamette-national-cemetery/transcription/411.php?page=169&sort=za",
            "title": "Willamette National Cemetery: Veterans Affairs Database",
            "author_creator": "Interment.net",
            "repository_publisher": "Interment.net",
            "publication_record_date": "2025-04-17",
            "locator": "Page 169; Nels Ulvesaker, 1911-1977, U.S. Army",
            "access_date": "2026-10-30",
            "source_quality": "D_correlative_or_secondary",
            "collection_name": "VA-derived national cemetery transcription",
            "rights_notes": "Discovery and rejection context only; it does not establish the indexed identity or a pre-OSS affiliation.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": PHA,
            "canonical_name": "Philadelphia Housing Authority",
            "historical_name": "Philadelphia Housing Authority",
            "aliases": ["PHA", "City of Philadelphia Housing Authority"],
            "organization_type": "municipal public-housing authority",
            "sector": "state_or_local_government",
            "city": "Philadelphia",
            "state_or_region": "Pennsylvania",
            "country": "United States",
            "active_dates": "1937-present",
            "normalization_notes": "Richard Allen Homes is preserved in the affiliation wording as the managed housing project; the source identifies the Housing Authority as the employer.",
        },
        {
            "key": WEST_AFRICA_MISSION,
            "canonical_name": "Presbyterian Church in the U.S.A. West Africa Mission",
            "historical_name": "West Africa Mission of the Board of Foreign Missions of the Presbyterian Church in the U.S.A.",
            "aliases": ["West Africa Mission", "PCUSA West Africa Mission"],
            "organization_type": "religious mission",
            "sector": "labor_nonprofit_and_religion",
            "country": "Cameroon",
            "active_dates": "Irvin Underhill appointment 1928; field service 1929-1940",
            "normalization_notes": "Recorded as a professional religious affiliation, not silently converted into salaried employment.",
        },
        {
            "key": YONHI,
            "canonical_name": "Yonhi College",
            "historical_name": "Yonhui College (Chosen Christian College)",
            "aliases": ["Yonhui College", "Chosen Christian College", "Gyeongsin School"],
            "organization_type": "college",
            "sector": "academia_and_research",
            "city": "Seoul",
            "country": "Korea",
            "active_dates": "Historical predecessor of Yonsei University; wartime names preserved",
            "normalization_notes": "Historical college names are preserved; Yonsei University is noted only as a documented successor, not substituted as the wartime employer.",
        },
        {
            "key": US_NAVY,
            "organization_id": "3960fa8e-a551-56cf-8305-b2b9e4961b9d",
            "canonical_name": "United States Navy",
            "historical_name": "United States Navy",
            "aliases": ["U.S. Navy", "US Navy"],
            "organization_type": "military service",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "Existing canonical military organization reused; Horace Grant Underwood's language-officer service is not treated as civilian employment.",
        },
        {
            "key": UC_BERKELEY,
            "organization_id": "dd5d0a44-0368-5e91-a5d3-074de36840ed",
            "canonical_name": "University of California, Berkeley",
            "historical_name": "University of California at Berkeley",
            "aliases": ["UC Berkeley", "University of California, Berkeley", "Cal"],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "Berkeley",
            "state_or_region": "California",
            "country": "United States",
            "normalization_notes": "Existing canonical university reused. Warren Unna's student status is separate from employment and excluded from employer analytics.",
        },
    ]


def occupation_affiliation(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    return {
        "key": f"{slug(PEOPLE[row][1])}-occupation-b974",
        "person_id": PEOPLE[row][0],
        "occupation": str(item["public_occupation"]),
        "relationship_type": str(item["relationship_type"]),
        "end_date": str(item["date"]),
        "date_precision": f"Historical civilian-occupation code {item['code']} was recorded at Army entry on {item['date']}; no named employer, workplace or exact OSS-transfer date is supplied.",
        "country": "United States",
        "immediate_pre_oss": False,
        "last_civilian_pre_service": False,
        "pre_oss_temporal_basis": str(item["temporal_basis"]),
        "identity_confidence": "high_confidence",
        "claim_confidence": "medium",
        "source_quality": "A_direct_official",
        "publication_status": "publish_qualified",
        "research_notes": "Occupation or student status only. The historical category is not a named employer and is excluded from verified-employer analytics.",
    }


def affiliations() -> list[dict[str, object]]:
    values = [occupation_affiliation(item) for item in ARMY_OCCUPATIONS]
    values.extend(
        [
            {
                "key": "irvin-underhill-philadelphia-housing-authority-b974",
                "person_id": PEOPLE[32][0],
                "organization_key": PHA,
                "organization_name_as_found": "Philadelphia Housing Authority's Richard Allen Homes",
                "role_title": "manager of Richard Allen Homes",
                "occupation": "public-housing manager",
                "relationship_type": "employment",
                "start_date": "1941-08",
                "end_date": "1951-05",
                "date_precision": "The institutional finding aid gives August 1941-May 1951 and separately identifies wartime consulting for OSS",
                "city": "Philadelphia",
                "state_or_region": "Pennsylvania",
                "country": "United States",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Housing Authority employment spans the wartime OSS consulting context. The source supports concurrency, not a claim that he left the employer for OSS.",
            },
            {
                "key": "irvin-underhill-west-africa-mission-b974",
                "person_id": PEOPLE[32][0],
                "organization_key": WEST_AFRICA_MISSION,
                "organization_name_as_found": "West Africa Mission of the Board of Foreign Missions of the Presbyterian Church in the U.S.A.",
                "role_title": "missionary, minister and school supervisor",
                "occupation": "missionary",
                "relationship_type": "professional_affiliation",
                "start_date": "1928-03",
                "end_date": "1940-11",
                "date_precision": "Appointed in 1928; field service in French Cameroun from 1929 until returning to Philadelphia in November 1940",
                "country": "Cameroon",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Earlier professional affiliation. The source does not require classifying missionary appointment as salaried employment.",
            },
            {
                "key": "horace-h-underwood-yonhi-president-b974",
                "person_id": PEOPLE[36][0],
                "organization_key": YONHI,
                "organization_name_as_found": "Yonhui College (Chosen Christian College or Gyeongsin School)",
                "role_title": "third president",
                "occupation": "college president and educator",
                "relationship_type": "employment",
                "start_date": "1934",
                "end_date": "1941",
                "date_precision": "The Academy of Korean Studies volume places his appointment in 1934 and Japanese repatriation in 1942; the presidency ended before repatriation",
                "city": "Seoul",
                "country": "Korea",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "publish_qualified",
                "research_notes": "Best-supported last civilian employer before wartime repatriation and the NARA OSS-file context. No source explicitly states that he left the college directly for OSS.",
            },
            {
                "key": "horace-g-underwood-chosen-christian-college-b974",
                "person_id": PEOPLE[37][0],
                "organization_key": YONHI,
                "organization_name_as_found": "Chosen Christian College",
                "role_title": "English instructor",
                "occupation": "teacher",
                "relationship_type": "employment",
                "start_date": "1939",
                "end_date": "1941",
                "date_precision": "Korea Society states that he returned in 1939 and taught until Japanese internment in 1941; Yonsei Archives gives 1940-1941",
                "city": "Seoul",
                "country": "Korea",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Last documented civilian employer before internment, repatriation and U.S. Navy service. Student or family relationships are not used as employment evidence.",
            },
            {
                "key": "horace-g-underwood-us-navy-language-officer-b974",
                "person_id": PEOPLE[37][0],
                "organization_key": US_NAVY,
                "organization_name_as_found": "U.S. Navy",
                "role_title": "Korean and Japanese language officer",
                "occupation": "military language officer",
                "relationship_type": "military_assignment",
                "start_date": "1942",
                "end_date": "1946",
                "date_precision": "Korea Society and Yonsei Archives independently place U.S. Navy service from 1942 through 1946; neither states the exact OSS relationship",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "temporal_relation_uncertain",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Documented military pathway, not civilian employment. It may have preceded or overlapped OSS duty; the accessible sources do not decide the sequence.",
            },
            {
                "key": "warren-unna-uc-berkeley-student-b974",
                "person_id": PEOPLE[44][0],
                "organization_key": UC_BERKELEY,
                "organization_name_as_found": "UC Berkeley",
                "role_title": "international-relations student",
                "occupation": "student",
                "relationship_type": "student",
                "end_date": "1943",
                "date_precision": "The institutional alumni periodical says he graduated in 1943; it does not state the date or nature of OSS entry",
                "city": "Berkeley",
                "state_or_region": "California",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "probable",
                "claim_confidence": "medium",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "publish_qualified",
                "research_notes": "Student status, not employment. The uncommon name and wartime chronology support a probable match, but Box 794 must confirm the indexed identity.",
            },
        ]
    )
    return values


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
    if evidence_excerpt:
        value["evidence_excerpt"] = evidence_excerpt
    return value


def army_identity_note(row: int) -> str:
    return (
        f"The official Army bulk row has the exact indexed full name {PEOPLE[row][1]} "
        "and an exact, nonshared protected-identifier agreement. The identifier and raw "
        "record ordinal remain private."
    )


def army_claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for item in ARMY_OCCUPATIONS:
        row = int(item["row"])
        name = PEOPLE[row][1]
        links = [
            {"source_key": INDEX},
            {"source_key": ARMY, "locator_override": "Accepted identity bridge; protected identifier and raw record withheld"},
        ]
        values.append(
            claim(
                row,
                f"identity-{slug(name)}-army-b974",
                "identity",
                f"Indexed {name} is high-confidence matched to the official Army entry used for the dated occupation finding.",
                "The official Army name agrees exactly and a nonshared protected identifier agrees with the NARA index row.",
                army_identity_note(row),
                "The Army entry date is preserved separately from the later OSS-index context.",
                "A_direct_official",
                "high",
                links,
                "Protected identifiers were used only for private resolution and remain absent from the evidence bundle and public output.",
            )
        )
        values.append(
            claim(
                row,
                f"occupation-{slug(name)}-b974",
                "occupation",
                f"At Army entry on {item['date']}, {name}'s historical civilian-occupation category was {str(item['occupation']).lower()}.",
                f"The official Army field carries historical code {item['code']}; NARA's code list defines it as {item['occupation']}.",
                army_identity_note(row),
                (
                    "Dated at Army entry before the later OSS-index context; no named employer, workplace or exact OSS-transfer date is supplied."
                    if item["temporal_basis"] == "documented_prewar"
                    else "Dated at Army entry in 1945; the accessible evidence does not establish whether this status preceded or overlapped OSS service."
                ),
                "A_direct_official",
                "medium",
                [
                    {"source_key": ARMY, "locator_override": "Accepted identity bridge; protected identifier and raw record withheld"},
                    {"source_key": TECH, "locator_override": "PDF physical pages 44-46; civilian-occupation field"},
                    {"source_key": CODES, "locator_override": str(item["locator"])},
                ],
                "Published as qualified occupation or student status only; excluded from verified-employer analytics.",
                f"{slug(name)}-occupation-b974",
                "publish_qualified",
            )
        )
    return values


def special_claims() -> list[dict[str, object]]:
    return [
        claim(
            32,
            "identity-irvin-windfield-underhill-b974",
            "identity",
            "Indexed Irvin W Underhill is high-confidence matched to Irvin Windfield Underhill Jr., the missionary and housing manager who consulted for OSS during World War II.",
            "The exact name and middle initial align with an institutional finding aid that explicitly names his wartime OSS consulting.",
            "High confidence from the distinctive full name, matching middle initial, detailed institutional chronology and explicit OSS consulting context.",
            "The finding aid places Philadelphia Housing Authority employment from 1941 to 1951 and OSS consulting during World War II.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": INDEX}, {"source_key": PHS_UNDERHILL}, {"source_key": PHS_UNDERHILL_BIO, "support_type": "context_only"}],
            "No missionary education, relatives or later pastorates are used to infer an employer.",
        ),
        claim(
            32,
            "immediate-irvin-underhill-pha-b974",
            "immediate_pre_oss_affiliation",
            "Irvin W. Underhill's best-supported civilian affiliation at the start of his OSS consulting was the Philadelphia Housing Authority, where he managed Richard Allen Homes.",
            "The finding aid documents Housing Authority management from August 1941 to May 1951 and separately states that he consulted for OSS during the war.",
            "High-confidence distinctive-name match with explicit OSS context in the same institutional source.",
            "Strongly date-bounded across wartime OSS consulting; the evidence supports concurrent employment rather than a departure from the Housing Authority.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": PHS_UNDERHILL, "excerpt_override": "From August 1941 to May 1951, he was the manager of the Philadelphia Housing Authority's Richard Allen Homes"}],
            "Immediate affiliation is phrased as employment at or before OSS consulting, not as an unsupported direct recruitment claim.",
            "irvin-underhill-philadelphia-housing-authority-b974",
        ),
        claim(
            32,
            "last-civilian-irvin-underhill-pha-b974",
            "last_civilian_pre_service",
            "Philadelphia Housing Authority is Irvin W. Underhill's last documented civilian employer before or during his wartime OSS consulting.",
            "The institutional chronology begins the housing-management role in 1941 and places OSS consulting during World War II.",
            "High-confidence exact-name and explicit OSS-consulting match.",
            "Strongly date-bounded; no intervening civilian employer is documented before the OSS consulting context.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": PHS_UNDERHILL}, {"source_key": PHS_UNDERHILL_BIO, "support_type": "context_only"}],
            "The profile notes that employment may have continued concurrently with consulting.",
            "irvin-underhill-philadelphia-housing-authority-b974",
        ),
        claim(
            32,
            "earlier-irvin-underhill-west-africa-mission-b974",
            "other_pre_oss_affiliation",
            "Irvin W. Underhill served with the Presbyterian West Africa Mission in French Cameroun from 1929 to 1940.",
            "The finding aid documents appointment in 1928, eleven years of field service and his November 1940 return to Philadelphia.",
            "High-confidence distinctive-name institutional match.",
            "Documented prewar professional affiliation ending before Housing Authority employment and OSS consulting.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": PHS_UNDERHILL, "excerpt_override": "During his eleven years of service in the mission field, from 1929 to 1940"}],
            "Relationship recorded as professional affiliation because the source does not require classifying the appointment as salaried employment.",
            "irvin-underhill-west-africa-mission-b974",
        ),
        claim(
            36,
            "identity-horace-horton-underwood-b974",
            "identity",
            "Indexed Horace H Underwood is high-confidence matched to Horace Horton Underwood (1890-1951), the Korea missionary and Yonhi College president.",
            "The exact rare name and middle initial align across the index, the UCLA missionary roster and an Academy of Korean Studies chronology.",
            "High confidence from the rare exact full name, matching middle initial, institutional missionary dates and distinction from his son Horace Grant Underwood II.",
            "The sources place Yonhi leadership through 1941 and Japanese repatriation in 1942; the exact OSS accession remains undocumented.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": INDEX}, {"source_key": UCLA_MISSIONARIES}, {"source_key": SOGANG_UNDERWOOD}, {"source_key": KOREA_NET, "support_type": "context_only"}],
            "Father and son remain separate people; no family relationship is used as the principal identity basis.",
        ),
        claim(
            36,
            "last-civilian-horace-h-underwood-yonhi-b974",
            "last_civilian_pre_service",
            "Yonhi College is Horace Horton Underwood's last documented civilian employer before wartime repatriation and the indexed OSS context.",
            "A scholarly institutional volume says he became the college's third president in 1934, remained in Korea until the Pacific War and was repatriated in 1942.",
            "High-confidence rare-name and institutional-chronology match.",
            "Strongly date-bounded but not explicitly described as a direct move from the college into OSS; therefore published as qualified.",
            "C_reputable_contemporary_or_scholarly",
            "medium",
            [{"source_key": SOGANG_UNDERWOOD, "excerpt_override": "In 1934, he was appointed the third president of Yonhui College"}, {"source_key": UCLA_MISSIONARIES, "support_type": "context_only"}],
            "No modern Yonsei employer name is substituted for the historical college.",
            "horace-h-underwood-yonhi-president-b974",
            "publish_qualified",
        ),
        claim(
            37,
            "identity-horace-grant-underwood-ii-b974",
            "identity",
            "Indexed Horace G Underwood is high-confidence matched to Horace Grant Underwood II (1917-2004), the Chosen Christian College instructor and U.S. Navy language officer.",
            "The rare name and middle initial align with two institutional chronologies that independently sequence teaching, internment, repatriation and Navy service.",
            "High confidence from the rare full name, matching middle initial, wartime Korean/Japanese language service and clear distinction from Horace Horton Underwood.",
            "Both institutional sources place college teaching before 1942 Navy service; neither states the exact OSS duty sequence.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": INDEX}, {"source_key": KOREA_SOCIETY}, {"source_key": YONSEI_ARCHIVES}, {"source_key": KOREA_NET, "support_type": "context_only"}],
            "The profile retains the suffix II and Korean name only as documented variants; it does not merge him with his father or grandfather.",
        ),
        claim(
            37,
            "last-civilian-horace-g-underwood-chosen-b974",
            "last_civilian_pre_service",
            "Chosen Christian College is Horace Grant Underwood II's last documented civilian employer before internment, repatriation and U.S. Navy service.",
            "Korea Society states that he returned in 1939, taught English, was interned in 1941, repatriated in 1942 and then joined the Navy.",
            "High-confidence rare-name match corroborated by Yonsei Archives.",
            "Strongly date-bounded and explicitly sequenced before military service, though no source states the precise OSS accession.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": KOREA_SOCIETY, "excerpt_override": "returned to Seoul and taught English at Chosen Christian College"}, {"source_key": YONSEI_ARCHIVES}],
            "Student status is not inferred; the source explicitly describes teaching.",
            "horace-g-underwood-chosen-christian-college-b974",
        ),
        claim(
            37,
            "other-horace-g-underwood-navy-b974",
            "other_pre_oss_affiliation",
            "Horace Grant Underwood II served in the U.S. Navy as a Korean and Japanese language officer from 1942 to 1946.",
            "Korea Society identifies the role and languages; Yonsei Archives independently gives the 1942-1946 service interval.",
            "High-confidence rare-name institutional match.",
            "The Navy service may have preceded or overlapped OSS work; the accessible sources do not establish the sequence, so it is not labeled immediate.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": KOREA_SOCIETY, "excerpt_override": "joined the U.S. Navy and served as a Korean and Japanese language officer in the Pacific"}, {"source_key": YONSEI_ARCHIVES}],
            "Military assignment remains distinct from the civilian college employer.",
            "horace-g-underwood-us-navy-language-officer-b974",
        ),
        claim(
            43,
            "identity-matthew-j-ungerleider-b974",
            "identity",
            "Indexed Matthew J Ungerleider is high-confidence matched to the Army entrant later recorded as Technician Fourth Grade in Headquarters Detachment, OSS.",
            "The official Army row exactly matches the indexed name and protected identifier; a specialist historical-society article independently names the OSS detachment and wartime death.",
            army_identity_note(43),
            "The Army occupation is dated at 1942 entry; the specialist source places him in OSS Headquarters Detachment by his 1944 death.",
            "A_direct_official",
            "high",
            [{"source_key": INDEX}, {"source_key": ARMY}, {"source_key": EIGHTH_AFHS, "support_type": "context_only", "excerpt_override": "Matthew Ungerleider who was attached to Headquarters Detachment, OSS"}],
            "The OSS assignment corroborates identity but is not mislabeled as a pre-OSS employer or affiliation.",
        ),
        claim(
            44,
            "identity-warren-unna-candidate-b974",
            "identity",
            "Indexed Warren W Unna is probably the Warren Unna who graduated from UC Berkeley in 1943, but Box 794 must confirm the match.",
            "The uncommon name and wartime graduation chronology align; the institutional memorial does not include the middle initial or an OSS identifier.",
            "Probable only because the source omits the middle initial and does not explicitly mention OSS.",
            "The documented 1943 degree precedes the index context, but the exact OSS accession remains unknown.",
            "B_authoritative_institutional",
            "medium",
            [{"source_key": INDEX}, {"source_key": BERKELEY_IHOUSE}],
            "The qualified candidate is excluded from default analytics and requires personnel-file confirmation.",
            publication_status="publish_qualified",
        ),
        claim(
            44,
            "other-warren-unna-berkeley-student-b974",
            "other_pre_oss_affiliation",
            "A probable Warren W. Unna identity graduated from UC Berkeley in 1943 with a degree in international relations.",
            "The institutional alumni periodical gives the university, degree field and year.",
            "Probable identity only; Box 794 must confirm the middle initial and OSS bridge.",
            "Documented wartime student status, not shown to be the immediate predecessor to OSS.",
            "B_authoritative_institutional",
            "medium",
            [{"source_key": BERKELEY_IHOUSE, "excerpt_override": "He graduated in 1943 from UC Berkeley with a degree in international relations."}],
            "Student status is not employment; postwar newspaper work is not projected backward.",
            "warren-unna-uc-berkeley-student-b974",
            "publish_qualified",
        ),
        claim(
            45,
            "identity-kazuo-unoki-mis-b974",
            "identity",
            "Indexed Kazuo Unoki is high-confidence matched to the Military Intelligence Service Language School registry entry for the 1946 Fort Snelling class.",
            "The rare exact name and entire numeric identifier sequence agree; the registry adds a prefix absent from the printed index.",
            "High confidence from the rare exact name and protected numeric-sequence agreement across independent archival contexts.",
            "The registry class is dated 1946 and therefore is used for identity only, not as proof of a pre-OSS affiliation.",
            "C_reputable_contemporary_or_scholarly",
            "high",
            [{"source_key": INDEX}, {"source_key": JAVA_MIS, "locator_override": "PDF page 186; identifier compared privately and withheld"}],
            "No full identifier is stored or published. The 1946 language-school entry is not included in pre-OSS analytics.",
        ),
    ]


def claims() -> list[dict[str, object]]:
    return army_claims() + special_claims()


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
            identity_evidence=f"The visually verified index row supplies {PEOPLE[row][1]}, Box {'793' if row <= 27 else '794'} and archive location 230/86/42/04. {reason}",
            personnel_category="unknown_or_indeterminate",
            commissioned_officer=None,
            allied_or_foreign_personnel=None,
            research_status="requires_archival_review",
            next_action=f"Review Box {'793' if row <= 27 else '794'} for corroborating identifiers, immediate pre-OSS affiliation and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}",
        )
        for row, reason in UNRESOLVED.items()
    ]

    for row in [25, 31, 41, 43]:
        temporal_note = (
            " The 1945 Army-entry date does not by itself establish whether the student status preceded or overlapped OSS service."
            if row == 41
            else ""
        )
        values.append(
            base_update(
                row,
                identity_status="high_confidence",
                identity_evidence=army_identity_note(row),
                personnel_category="enlisted_army_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                research_status="occupation_only_found",
                next_action=f"Review Box {'793' if row == 25 else '794'} to establish the immediate pre-OSS affiliation and named last civilian employer; do not convert the Army occupation category into a workplace.{temporal_note}",
            )
        )

    values.extend(
        [
            base_update(
                32,
                identity_status="high_confidence",
                identity_evidence="The distinctive indexed name and middle initial match the Presbyterian Historical Society finding aid, which explicitly documents wartime OSS consulting, Philadelphia Housing Authority employment and earlier mission service.",
                name_variants=["Irvin Windfield Underhill Jr.", "Irvin W. Underhill"],
                personnel_category="civilian_professional_or_administrative_grade",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                research_status="verified_employer_found",
                next_action="Review Box 794 to establish the exact OSS consulting dates and duty while preserving Philadelphia Housing Authority employment as concurrent unless the file proves otherwise.",
                archival_review_priority="medium",
            ),
            base_update(
                36,
                identity_status="high_confidence",
                identity_evidence="The rare exact name and middle initial align with Horace Horton Underwood across UCLA, Korea.net and Academy of Korean Studies sources; those sources distinguish him from his son Horace Grant Underwood II.",
                name_variants=["Horace Horton Underwood", "Won Han-gyeong"],
                personnel_category="unknown_or_indeterminate",
                commissioned_officer=None,
                allied_or_foreign_personnel=False,
                research_status="documented_prewar_employer_found",
                next_action="Review Box 794 to confirm Horace Horton Underwood's exact OSS role and the sequence between the 1941 end of the Yonhi presidency, 1942 repatriation and OSS service.",
                archival_review_priority="medium",
            ),
            base_update(
                37,
                identity_status="high_confidence",
                identity_evidence="The rare exact name and middle initial align with Korea Society and Yonsei Archives chronologies of Chosen Christian College teaching, internment, repatriation and service as a U.S. Navy Korean/Japanese language officer.",
                name_variants=["Horace Grant Underwood II", "Won Il-han"],
                personnel_category="commissioned_naval_officer",
                commissioned_officer=True,
                allied_or_foreign_personnel=False,
                research_status="documented_prewar_employer_found",
                next_action="Review Box 794 to establish whether U.S. Navy language service preceded or overlapped OSS duty and to document the exact accession or assignment mechanism.",
                archival_review_priority="medium",
            ),
            base_update(
                44,
                identity_status="probable",
                identity_evidence="An institutional UC Berkeley memorial identifies the uncommon name Warren Unna and a 1943 international-relations degree, but omits the indexed middle initial and any OSS identifier.",
                personnel_category="unknown_or_indeterminate",
                commissioned_officer=None,
                allied_or_foreign_personnel=False,
                research_status="occupation_only_found",
                next_action="Review Box 794 to confirm the Warren Unna identity, wartime service chronology and any employer between UC Berkeley and OSS.",
                archival_review_priority="critical",
            ),
            base_update(
                45,
                identity_status="high_confidence",
                identity_evidence="The rare exact name and complete numeric identifier sequence agree with the 1946 Military Intelligence Service Language School registry entry; the registry prefix absent from the index is treated as a formatting difference.",
                personnel_category="unknown_or_indeterminate",
                commissioned_officer=None,
                allied_or_foreign_personnel=False,
                research_status="requires_archival_review",
                next_action="Review Box 794 to identify Kazuo Unoki's pre-OSS employment and establish how OSS service related to the 1946 Fort Snelling language-school entry.",
                archival_review_priority="high",
            ),
        ]
    )
    return values


def research_attempts() -> list[dict[str, object]]:
    reviewed_rows = {25, 31, 32, 36, 37, 41, 43, 44, 45}
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        if row in reviewed_rows:
            outcome = "source_reviewed"
            reviewed = 10 if row in {32, 36, 37} else 7
            rejected = 5
            detail = "Reviewed official, institutional, scholarly or specialist evidence produced the identity, occupation, student, military-pathway or employer outcome recorded in the evidence bundle."
        else:
            outcome = "no_result"
            reviewed = 6
            rejected = 6
            detail = UNRESOLVED[row]

        special_rejection = ""
        if row == 26:
            special_rejection = " A VA-derived cemetery entry and specialist Camp Ritchie roster were retained as leads only because neither bridges the person to Box 793 or an employer."
        elif row == 29:
            special_rejection = " The Karl Stafford Umberger wartime-letter index is an archival lead, not proof that the indexed Karl S Umberger is that person."
        elif row == 30:
            special_rejection = " Social-register residence was not converted into occupation, employment or OSS identity evidence."
        elif row == 38:
            special_rejection = " An archival Irène J. Underwood name was rejected for lack of an OSS or Box 794 bridge."
        elif row == 44:
            special_rejection = " Postwar San Francisco Chronicle and Washington Post employment was not projected backward into the pre-OSS period."
        elif row == 45:
            special_rejection = " The 1946 MISLS entry supports identity only and is not presented as a pre-OSS affiliation."

        box = "793" if row <= 27 else "794"
        attempts.append(
            {
                "key": f"page477-row{row}-{slug(name)}-b974",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index and official Archives context; permitted CIA official-source context or documented robots-policy limitation; exact-name and meaningful variants; OSS, Army, Navy, rank and unit clues; employer and occupation 1940; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Box {box}; protected identifiers used only in private official-record comparison",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_974",
                "started_at": "2026-10-30T08:10:00Z",
                "completed_at": "2026-10-30T10:00:00Z",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search snippets, unsourced genealogy, people-finder pages, relatives, postwar-only employment leads and sources without an OSS, protected-identifier or personnel-file bridge were rejected. Historical occupation codes and military service were not silently converted into employers." + special_rejection,
                "research_notes": f"{detail} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain and archival searches were checked as applicable. The automated CIA Reading Room route remains disallowed by the site's robots policy, so it was not queried and is not described as a negative result; permitted official or equivalent institutional sources and the physical-file route were used instead. The index page, Army bulk file, technical documentation and occupation-code pages were inspected directly; code pages 175-176 and corrected page 304 were visually checked. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": f"Review Box {box} for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before wartime service.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b974-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-974-v1",
        "reviewer": "Before OSS Batch 974 evidence review",
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
