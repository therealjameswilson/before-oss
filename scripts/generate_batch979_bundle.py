#!/usr/bin/env python3
"""Generate the reviewed Batch 979 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page480-elizabeth-van-kuyk-to-robert-vance-"
    "review_batch-979_2026-10-30.json"
)

INDEX = "nara-index-b979"
ARMY = "army-bulk-b979"
TECH = "army-tech-b979"
CODES = "army-codes-b979"
HOLLIS_VAN_NICE = "hollis-robert-van-nice-b979"
DOAKS_HOMECOMING = "doaks-robert-van-nice-homecoming-b979"
CLARK_OSS = "clark-samuel-van-valkenburg-oss-b979"
CLARK_CAREER = "clark-samuel-van-valkenburg-career-b979"
CLARK_1941 = "clark-samuel-van-valkenburg-1941-b979"

ORG_HAGIA = "hagia-sophia-survey-emerson-b979"
ORG_SMITH = "myron-bement-smith-iran-survey-b979"
ORG_CLARK = "clark-university-b979"


PEOPLE = {
    1: ("fb3e8af2-3eae-5f71-a06a-2904d98f2713", "Elizabeth Van Kuyk"),
    2: ("06727acb-210c-530c-b3d2-89669ee76e47", "Rene W Van Lacke"),
    3: ("984c6f78-7ba5-53be-8291-587a9d28b756", "Piet Van Leer"),
    4: ("74658c63-7063-50dd-80e3-fc8fe12c23c0", "R V Van Liew"),
    5: ("e240bfb5-a20e-5627-abe5-83e29e6125f6", "Robert L Van Nice"),
    6: ("278e9f10-8396-5443-9dfe-c9418f5951e8", "Leonard M Van Noppen"),
    7: ("f2cf633f-617a-53fd-bcb7-600722b3638a", "Winifred M Van Patter"),
    8: ("9f97d996-8a72-5f90-b67e-3509147fd391", "Alex Van Praag"),
    9: ("de73693e-01b3-50f0-bc95-5a3de7ba626b", "Dollis E Van Roden"),
    10: ("38e76cc5-6d85-520e-8fe5-77f67f2fecfd", "Peter H Van Scherpe"),
    11: ("8117f959-f643-505f-b656-e2b7d1821fd0", "* Van Scyloren"),
    12: ("78082177-5934-590a-9391-3201b6a26439", "Chester F Van Sickle"),
    13: ("b1783b70-92f1-5dce-b2e2-a289886121cb", "Max W Van Sickle"),
    14: ("0647d353-da82-5cc5-9f0d-7e132c79d718", "Francis E Van Timmeren"),
    15: ("a1668642-89d6-5c37-a417-d4a0be299485", "Hubert Van Tol"),
    16: ("76710072-32d8-5806-ad70-a5b5a51c5fbd", "Donald W Van Treese"),
    17: ("5c2d05d0-126f-5ad7-bda6-cc6ecb9023c9", "Samuel Van Valkenber"),
    18: ("257d18cd-9707-51fe-96b6-dae5d64f329f", "Claude W Van Vleet"),
    19: ("74d44806-10bc-5ab5-a40f-59945ef10f1a", "Howard E Van Winkle Jr"),
    20: ("9f8f0d7d-1213-5fe1-8f5a-12208d2207cc", "Helen Van Zonnevel"),
    21: ("a9d5d4ca-9a95-549c-b20a-aacb35bb8ed6", "Johan Adria Van Zuylen"),
    22: ("5d8a4511-445b-55fd-a3b7-bd61d72ae30c", "Robert J Vanasse"),
    23: ("3b744079-1ec3-5900-8789-440107b7a057", "Robert G Vance"),
}


ARMY_OCCUPATIONS = [
    {
        "row": 2,
        "date": "1942-08-31",
        "code": "126",
        "occupation": "Paymasters, payroll clerks, and timekeepers",
        "public_occupation": "paymaster, payroll clerk, or timekeeper",
        "locator": "PDF physical page 171; historical category 1-26",
    },
    {
        "row": 4,
        "date": "1942-04-20",
        "code": "316",
        "occupation": "Farm hands, general farms",
        "public_occupation": "farm hand on a general farm",
        "locator": "PDF physical page 172; historical category 3-16",
    },
    {
        "row": 14,
        "date": "1941-06-17",
        "code": "893",
        "occupation": "Occupations in fabrication of metal products, not elsewhere classified",
        "public_occupation": "metal-products fabrication occupation, not elsewhere classified",
        "locator": "PDF physical page 174; historical category 8-93",
    },
    {
        "row": 16,
        "date": "1942-07-30",
        "code": "583",
        "occupation": "Mechanics and repairmen, not elsewhere classified",
        "public_occupation": "mechanic or repairman, not elsewhere classified",
        "locator": "PDF physical page 175; historical category 5-83",
    },
    {
        "row": 23,
        "date": "1943-08-14",
        "code": "056",
        "occupation": "Photographers",
        "public_occupation": "photographer",
        "locator": "PDF physical page 171; historical category 0-56",
    },
]


UNRESOLVED = {
    1: "A rare-name December 1943 Foreign Service Journal visitor listing for Elizabeth Jeanne Van Kuyk in Madrid lacks the middle-name, OSS or personnel-file bridge needed to resolve the indexed person; a 1955 oil-industry role is postwar and names no employer.",
    3: "Exact-name and Dutch spelling-variant searches produced unrelated historical and modern namesakes but no OSS, Box 799 or pre-OSS-employment bridge for Piet Van Leer.",
    6: "The exact name appears in postwar Universal C.I.T. safety material, but no source connects that executive to the indexed first lieutenant or establishes his pre-OSS career.",
    7: "Exact-name official, institutional, newspaper, obituary and archival searches produced no reliable identity bridge for Winifred M Van Patter.",
    8: "A prominent Illinois engineer named Alex Van Praag and several wartime Van Praag military records remain unbridged namesakes; no source ties the indexed protected identifier to that engineering career.",
    9: "Exact-name and spelling-variant official, institutional, newspaper, obituary and archival searches produced no reliable identity bridge for Dollis E Van Roden.",
    10: "Exact-name searches produced modern property and people-finder results but no contemporaneous OSS, military or employment bridge for Peter H Van Scherpe.",
    11: "The source explicitly prints an asterisk and notes that no first name is available; surname-variant searches cannot safely resolve this person without the physical file.",
    12: "Exact-name, protected-identifier, military, obituary and institutional searches did not isolate the indexed Chester F Van Sickle.",
    13: "A burial lead for a World War II veteran named Max W Van Sickle supplies no OSS, Box 800 or employment bridge and cannot establish the indexed identity.",
    15: "Search results identify several later people named Hubert Van Tol, including a 1913 birth lead and modern professionals, but none provides the corroborating identifiers required for the indexed person.",
    18: "The indexed first-lieutenant rank was preserved, but exact-name military, institutional, obituary and archival searches produced no reliable identity or employment bridge for Claude W Van Vleet.",
    19: "Exact-name and suffix-variant official, military, newspaper, obituary and archival searches produced no reliable identity bridge for Howard E Van Winkle Jr.",
    20: "Van Zonnevel and Van Zonneveld spelling searches produced no source with an OSS, Box 800 or pre-OSS-employment bridge for Helen Van Zonnevel.",
    21: "Dutch name-expansion and transliteration searches produced no reliable source tying Johan Adria Van Zuylen to a pre-OSS employer or wartime identity.",
    22: "The indexed staff-sergeant row remains separate from multiple Robert J Vanasse namesakes; none supplies matching wartime identifiers or employer chronology.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 797-800",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 480, rows 1-23; checked against layout-preserving text and an original-detail page render",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate; literal clipped spellings, ranks, identifiers, note and locations are preserved.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; five Batch 979 identity comparisons; protected identifiers and record ordinals withheld",
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
            "locator": "PDF physical pages 171, 172, 174 and 175; all five Batch 979 categories visually and textually checked",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical categories identify neither employers nor workplaces and are retained only where needed for auditability.",
        },
        {
            "key": HOLLIS_VAN_NICE,
            "stable_url": "https://hollisarchives.lib.harvard.edu/catalog/dca00007",
            "archival_identifier": "MS.BZ.012",
            "title": "Robert L. Van Nice fieldwork records and papers, circa 1936-1989",
            "author_creator": "Image Collections and Fieldwork Archives",
            "repository_publisher": "Dumbarton Oaks, Trustees for Harvard University",
            "publication_record_date": "Finding aid finalized 2014; last indexed 2026-06-21",
            "locator": "Biographical/Historical Note: Iran survey, William Emerson's Hagia Sophia project and 1944-1945 OSS X-2 service",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Image Collections and Fieldwork Archives, Dumbarton Oaks",
            "rights_notes": "Finding aid used for concise project-authored claims; no archival item images are republished.",
        },
        {
            "key": DOAKS_HOMECOMING,
            "stable_url": "https://icfadumbartonoaks.wordpress.com/2014/07/09/hagia-sophia-homecoming-returning-to-istanbul-after-world-war-ii/",
            "title": "Hagia Sophia Homecoming: Returning to Istanbul after World War II",
            "author_creator": "Beth Bayley",
            "repository_publisher": "Image Collections and Fieldwork Archives, Dumbarton Oaks",
            "publication_record_date": "2014-07-09",
            "locator": "Opening chronology: Cambridge drawings, then OSS work in London and Bern",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Dumbarton Oaks ICFA blog",
        },
        {
            "key": CLARK_OSS,
            "stable_url": "https://www.clarku.edu/news/2015/04/29/no-spy-games-but-plenty-of-research/",
            "title": "No spy games, but plenty of research",
            "author_creator": "Jim Keogh",
            "repository_publisher": "Clark University",
            "publication_record_date": "2015-04-29",
            "locator": "Paragraph identifying Professor Samuel Van Valkenburg as a Clark professor who had worked at OSS",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Clark University News",
        },
        {
            "key": CLARK_CAREER,
            "stable_url": "https://s45055.pcdn.co/departments/geography/www-content/blogs.dir/5/files/sites/44/2018/10/Monadnock1962Vol36April.pdf",
            "title": "Dr. Van at Clark",
            "author_creator": "Clark University Graduate School of Geography",
            "repository_publisher": "Clark University",
            "publication_record_date": "1962-04",
            "locator": "Biographical article: permanent Clark appointment in 1932 after visiting-professor service beginning in 1927",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "The Monadnock",
        },
        {
            "key": CLARK_1941,
            "stable_url": "https://www.clarku.edu/departments/geography/wp-content/blogs.dir/5/files/sites/44/2018/10/Monadnock.1941.Vol16.No1_.Dec_.pdf",
            "title": "The Monadnock, Volume XVI, Number 1",
            "author_creator": "Clark University Graduate School of Geography",
            "repository_publisher": "Clark University",
            "publication_record_date": "1941-12",
            "locator": "Faculty notes: Van Valkenburg teaching, conducting research and representing the Geography Department in 1941",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "The Monadnock",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": ORG_HAGIA,
            "canonical_name": "Hagia Sophia architectural survey (William Emerson project)",
            "historical_name": "study of Hagia Sophia",
            "aliases": ["Hagia Sophia survey", "St. Sophia project", "Santa Sophia project"],
            "organization_type": "independent architectural research project",
            "sector": "academia_and_research",
            "city": "Istanbul",
            "country": "Turkey",
            "active_dates": "1937-1989",
            "normalization_notes": "William Emerson personally sponsored the project from 1937 to 1957; it was separately funded and independently run, so MIT, the Byzantine Institute and Dumbarton Oaks are not silently substituted as the 1937 employer.",
        },
        {
            "key": ORG_SMITH,
            "canonical_name": "Myron Bement Smith Iranian architectural survey",
            "historical_name": "architectural survey in Iran under Myron Bement Smith",
            "aliases": ["Masjid-i Juma survey"],
            "organization_type": "architectural research project",
            "sector": "academia_and_research",
            "city": "Isfahan",
            "country": "Iran",
            "active_dates": "1936-1937",
            "normalization_notes": "Named as a project because the finding aid says Van Nice worked under Smith but does not identify a corporate or institutional employer.",
        },
        {
            "key": ORG_CLARK,
            "canonical_name": "Clark University",
            "historical_name": "Clark University",
            "aliases": ["Clark University Graduate School of Geography"],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "Worcester",
            "state_or_region": "Massachusetts",
            "country": "United States",
            "active_dates": "1887-present",
            "normalization_notes": "The Graduate School of Geography is retained as a historical unit of Clark University rather than a separate employer.",
        },
    ]


def occupation_affiliation(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    name = PEOPLE[row][1]
    return {
        "key": f"{slug(name)}-occupation-b979",
        "person_id": PEOPLE[row][0],
        "occupation": str(item["public_occupation"]),
        "relationship_type": "unknown",
        "start_date": str(item["date"]),
        "end_date": str(item["date"]),
        "date_precision": "Dated at Army entry; the historical category does not name an employer, workplace or duration",
        "country": "United States",
        "immediate_pre_oss": False,
        "last_civilian_pre_service": False,
        "pre_oss_temporal_basis": "strongly_date_bounded",
        "identity_confidence": "high_confidence",
        "claim_confidence": "medium",
        "source_quality": "A_direct_official",
        "publication_status": "publish_qualified",
        "research_notes": "Official historical occupation category only; excluded from employer analytics.",
    }


def affiliations() -> list[dict[str, object]]:
    values = [occupation_affiliation(item) for item in ARMY_OCCUPATIONS]
    values.extend(
        [
            {
                "key": "robert-van-nice-hagia-sophia-b979",
                "person_id": PEOPLE[5][0],
                "organization_key": ORG_HAGIA,
                "organization_name_as_found": "large scale study of Hagia Sophia",
                "role_title": "architectural surveyor",
                "occupation": "architect",
                "relationship_type": "employment",
                "start_date": "1937",
                "end_date": "1944",
                "date_precision": "Emerson hired Van Nice in 1937; wartime Cambridge drawing work preceded OSS service beginning in 1944",
                "city": "Istanbul",
                "country": "Turkey",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "confirmed",
                "claim_confidence": "confirmed",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Best-supported immediate civilian affiliation and last civilian work before OSS; MIT, Dumbarton Oaks and the Byzantine Institute are not substituted as employers.",
            },
            {
                "key": "robert-van-nice-iran-survey-b979",
                "person_id": PEOPLE[5][0],
                "organization_key": ORG_SMITH,
                "organization_name_as_found": "worked in Iran under the architect and archaeologist Myron Bement Smith",
                "role_title": "architectural survey assistant",
                "occupation": "architect",
                "relationship_type": "employment",
                "start_date": "1936-10",
                "end_date": "1937-07",
                "date_precision": "Finding aid gives October 1936 through July 1937",
                "city": "Isfahan",
                "country": "Iran",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "confirmed",
                "claim_confidence": "confirmed",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Earlier documented prewar employment, kept separate from the later Hagia Sophia project.",
            },
            {
                "key": "samuel-van-valkenburg-clark-b979",
                "person_id": PEOPLE[17][0],
                "organization_key": ORG_CLARK,
                "organization_name_as_found": "Clark University",
                "role_title": "professor of geography",
                "occupation": "geographer and university professor",
                "relationship_type": "employment",
                "start_date": "1932",
                "end_date": "1942",
                "date_precision": "Permanent appointment began in 1932; Clark documents active teaching in 1941, but the exact OSS leave date is not stated",
                "city": "Worcester",
                "state_or_region": "Massachusetts",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "probable_immediate",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Last documented civilian employer before OSS work. The exact OSS start and relationship to wartime Quartermaster consulting await file review.",
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
    return value


def army_identity_note(row: int) -> str:
    return (
        f"The official Army row has the exact indexed full name {PEOPLE[row][1]} and an exact, "
        "nonshared protected-identifier agreement. The identifier and raw record ordinal remain private."
    )


def army_claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for item in ARMY_OCCUPATIONS:
        row = int(item["row"])
        name = PEOPLE[row][1]
        values.append(
            claim(
                row,
                f"identity-{slug(name)}-army-b979",
                "identity",
                f"Indexed {name} is high-confidence matched to the official Army entry used for the dated occupation finding.",
                "An exact official Army name comparison and nonshared protected identifier support the identity match.",
                army_identity_note(row),
                "The Army entry date is preserved separately from the later OSS-index context.",
                "A_direct_official",
                "high",
                [{"source_key": INDEX}, {"source_key": ARMY, "locator_override": "Accepted identity bridge; protected identifier and raw record withheld"}],
                "Protected identifiers were used only for private resolution and remain absent from the evidence bundle and public output.",
            )
        )
        values.append(
            claim(
                row,
                f"occupation-{slug(name)}-b979",
                "occupation",
                f"At Army entry on {item['date']}, {name}'s historical civilian-occupation category was {str(item['occupation']).lower()}.",
                f"The official Army field carries historical code {item['code']}; NARA's code list defines it as {item['occupation']}.",
                army_identity_note(row),
                "Dated at Army entry before the later OSS-index context; no named employer, workplace or exact OSS-transfer date is supplied.",
                "A_direct_official",
                "medium",
                [
                    {"source_key": ARMY, "locator_override": "Accepted identity bridge; protected identifier and raw record withheld"},
                    {"source_key": TECH, "locator_override": "PDF physical pages 44-46; civilian-occupation field"},
                    {"source_key": CODES, "locator_override": str(item["locator"])},
                ],
                "Published as a qualified occupation only; excluded from verified-employer analytics.",
                f"{slug(name)}-occupation-b979",
                "publish_qualified",
            )
        )
    return values


def special_claims() -> list[dict[str, object]]:
    return [
        claim(
            5,
            "identity-robert-van-nice-b979",
            "identity",
            "Indexed Robert L Van Nice is confirmed as architect Robert Lawrence Van Nice, who served in OSS X-2 in London and Bern in 1944-1945.",
            "The institutional finding aid gives his full name, architectural career, exact OSS branch, offices and service years.",
            "Confirmed by an authoritative collection-level biography based partly on his official OSS dossier.",
            "The same chronology documents his prewar work and later OSS service.",
            "B_authoritative_institutional",
            "confirmed",
            [{"source_key": INDEX}, {"source_key": HOLLIS_VAN_NICE}],
            "The indexed spelling remains primary; the full name is retained as a documented variant.",
        ),
        claim(
            5,
            "immediate-robert-van-nice-hagia-sophia-b979",
            "immediate_pre_oss_affiliation",
            "Before his 1944 OSS X-2 service, Robert Lawrence Van Nice worked on William Emerson's independently run architectural survey of Hagia Sophia.",
            "The finding aid says Emerson hired him in 1937; Dumbarton Oaks states that Cambridge drawing work preceded his London and Bern OSS work.",
            "Confirmed exact-name, career and OSS dossier chronology.",
            "Strongly date-bounded immediate civilian work; the exact 1944 transition day is not stated.",
            "B_authoritative_institutional",
            "confirmed",
            [{"source_key": HOLLIS_VAN_NICE}, {"source_key": DOAKS_HOMECOMING}],
            "The project—not MIT, the Byzantine Institute or postwar Dumbarton Oaks—is the historically supported affiliation.",
            "robert-van-nice-hagia-sophia-b979",
        ),
        claim(
            5,
            "last-civilian-robert-van-nice-hagia-sophia-b979",
            "last_civilian_pre_service",
            "Robert Lawrence Van Nice's last documented civilian work before OSS was architectural surveying and drawing for the Hagia Sophia project sponsored by William Emerson.",
            "The institutional chronology runs from Emerson's 1937 hiring through wartime Cambridge drawings and then to OSS service in 1944.",
            "Confirmed exact-name and career chronology.",
            "Last documented civilian work before OSS; no intervening employer is identified.",
            "B_authoritative_institutional",
            "confirmed",
            [{"source_key": HOLLIS_VAN_NICE}, {"source_key": DOAKS_HOMECOMING}],
            "Reported separately from his immediate-affiliation claim so the two research questions remain auditable.",
            "robert-van-nice-hagia-sophia-b979",
        ),
        claim(
            5,
            "earlier-robert-van-nice-smith-b979",
            "other_pre_oss_affiliation",
            "From October 1936 through July 1937, Robert Lawrence Van Nice worked under architect and archaeologist Myron Bement Smith on surveys in Iran.",
            "The finding aid dates the Iran work and describes his measurements and drawings at Isfahan, Shiraz and Ashtarjan.",
            "Confirmed exact-name and continuous architectural-career evidence.",
            "Explicitly documented prewar work, preceding the Hagia Sophia project.",
            "B_authoritative_institutional",
            "confirmed",
            [{"source_key": HOLLIS_VAN_NICE}],
            "Kept as earlier employment rather than being presented as the immediate OSS predecessor.",
            "robert-van-nice-iran-survey-b979",
        ),
        claim(
            17,
            "identity-samuel-van-valkenburg-b979",
            "identity",
            "Indexed Samuel Van Valkenber is high-confidence matched to Clark University geographer Samuel Van Valkenburg, who worked at OSS.",
            "Clark's institutional article explicitly joins the professor's name, Clark role and OSS service; the index surname is visibly clipped at the table boundary.",
            "High confidence from rare-name expansion, university role and explicit OSS context.",
            "Clark sources document his faculty career before and after wartime service.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": INDEX}, {"source_key": CLARK_OSS}, {"source_key": CLARK_CAREER, "support_type": "context_only"}],
            "The printed truncated form remains recoverable and the documented full spelling is a variant.",
        ),
        claim(
            17,
            "last-civilian-samuel-van-valkenburg-clark-b979",
            "last_civilian_pre_service",
            "Samuel Van Valkenburg was a Clark University geography professor before his wartime OSS work.",
            "Clark records his permanent appointment from 1932, active teaching and research in 1941, and later identifies him as an OSS veteran.",
            "High-confidence rare-name, institutional-role and explicit OSS match.",
            "Clark is the last documented civilian employer; the exact OSS start and any intervening government assignment remain unresolved.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": CLARK_CAREER}, {"source_key": CLARK_1941}, {"source_key": CLARK_OSS}],
            "Not labeled an explicit direct transfer; wartime Quartermaster consulting is later and remains a separate chronology question.",
            "samuel-van-valkenburg-clark-b979",
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
    values: list[dict[str, object]] = []
    ambiguous = {1, 6, 8, 11, 13, 15, 22}
    for row, reason in UNRESOLVED.items():
        category = None
        officer = None
        allied = None
        if row in {6, 18}:
            category = "commissioned_army_officer"
            officer = True
            allied = False
        elif row == 22:
            category = "enlisted_army_personnel"
            officer = False
            allied = False
        values.append(
            base_update(
                row,
                identity_status="ambiguous" if row in ambiguous else "unresolved",
                identity_evidence=f"The visually verified index row supplies {PEOPLE[row][1]}, a box number and archive location. {reason}",
                personnel_category=category,
                commissioned_officer=officer,
                allied_or_foreign_personnel=allied,
                research_status="requires_archival_review",
                next_action=f"Review the indexed personnel file for corroborating identifiers, immediate pre-OSS affiliation and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}",
                archival_review_priority="critical" if row in {1, 8, 11, 15, 22} else "high",
            )
        )

    for item in ARMY_OCCUPATIONS:
        row = int(item["row"])
        values.append(
            base_update(
                row,
                identity_status="high_confidence",
                identity_evidence=army_identity_note(row),
                personnel_category="enlisted_army_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                research_status="occupation_only_found",
                next_action="Review the indexed personnel file to establish the immediate pre-OSS affiliation and named last civilian employer; do not convert the Army occupation category into a workplace.",
            )
        )

    values.extend(
        [
            base_update(
                5,
                identity_status="confirmed",
                identity_evidence="The Dumbarton Oaks finding aid supplies Robert Lawrence Van Nice's exact career chronology and states that his 1944-1945 X-2 work is documented in his NARA OSS dossier.",
                name_variants=["Robert Lawrence Van Nice", "Robert Van Nice"],
                personnel_category="civilian_professional_or_administrative_grade",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                research_status="verified_employer_found",
                next_action="Review Box 800 and the NARA dossier copies in MS.BZ.012 to establish the exact 1944 accession date and formal project-employment terms.",
                archival_review_priority="medium",
            ),
            base_update(
                17,
                identity_status="high_confidence",
                identity_evidence="Clark University explicitly identifies Professor Samuel Van Valkenburg as having worked at OSS; the rare name and visibly clipped indexed surname align.",
                name_variants=["Samuel Van Valkenburg", "Samuel van Valkenburg"],
                personnel_category="civilian_professional_or_administrative_grade",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                research_status="verified_employer_found",
                next_action="Review Box 800 and Clark's Samuel Van Valkenburg papers to establish the exact OSS start, employment status and relationship to wartime Quartermaster consulting.",
                archival_review_priority="medium",
            ),
        ]
    )
    return values


def research_attempts() -> list[dict[str, object]]:
    reviewed = {2: 4, 4: 4, 5: 4, 14: 4, 16: 4, 17: 4, 23: 4}
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        if row in reviewed:
            outcome = "source_reviewed"
            sources_reviewed = reviewed[row]
            rejected = 3
            detail = "Reviewed official or institutional evidence produced the identity, occupation or employer outcome recorded in the bundle."
        else:
            outcome = "no_result"
            sources_reviewed = 5
            rejected = 5
            detail = UNRESOLVED[row]

        attempts.append(
            {
                "key": f"page480-row{row}-{slug(name)}-b979",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index and official Archives context; CIA Reading Room or equivalent official-source context; exact-name and meaningful variants; OSS, Army, rank and unit clues; employer and occupation 1940; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Boxes 797-800; protected identifiers used only in private official-record comparison",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_979",
                "started_at": "2026-10-30T14:00:00Z",
                "completed_at": "2026-10-30T18:00:00Z",
                "outcome": outcome,
                "sources_reviewed": sources_reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search snippets, unsourced genealogy, people-finder and property pages, relatives, postwar-only employment leads and sources without an OSS, protected-identifier, rank or personnel-file bridge were rejected. Historical occupation codes and military service were not silently converted into employers.",
                "research_notes": f"{detail} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain and archival searches were checked as applicable. The index page and NARA Army occupation-code pages were inspected directly. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": "Review the indexed personnel file for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before wartime service.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b979-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-979-v1",
        "reviewer": "Before OSS Batch 979 evidence review",
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
