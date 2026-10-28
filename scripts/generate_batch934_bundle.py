#!/usr/bin/env python3
"""Generate the reviewed Batch 934 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / (
    "research/evidence-page457-james-a-sweatte-to-frank-l-sweetser-"
    "review_batch-934_2026-10-27.json"
)

INDEX = "nara-index-b934"
ARMY_SOURCE = "army-bulk-b934"
TECH = "army-tech-b934"
CODES = "army-codes-b934"
RAUCH = "rauch-paul-sweet-b934"
INTERVIEW = "historian-paul-sweet-b934"
MILITANT = "militant-paul-sweet-b934"
DENSHO = "densho-frank-sweetser-b934"
DARTMOUTH = "dartmouth-war-directory-b934"
CEMETERY = "mass-national-cemetery-b934"
JOY_OBIT = "joyeuse-sweet-obituary-b934"
YALe = "yale-lennig-sweet-papers-b934"

PEOPLE = {
    24: ("0d7a18fb-d090-53ee-bc1a-fabc925f35c1", "James A Sweatte"),
    25: ("c136aa83-99a4-5012-8d3b-a7fe6f4b6205", "Bernard Swedloff"),
    26: ("59adfad9-f19b-54ad-936e-aacdc831ad1e", "Elizabeth Sweeka"),
    27: ("d6b51654-69c3-533c-93b4-ae95ba12d407", "Lois E Sweeley"),
    28: ("db758e9a-5aeb-5fda-8823-ffb3942ff064", "Barbara P Sweeney"),
    29: ("ae367bc5-46ff-5f52-8cb8-05f48c242ba3", "James S Sweeney"),
    30: ("f62adfa3-3bee-578d-a1d2-3b0aa552e622", "Joseph M Sweeney"),
    31: ("19544301-a933-5438-a865-c53b61a00169", "Joseph M Sweeney"),
    32: ("3b7319af-74d7-59fe-900a-2b3ab69c1c99", "Patrick J Sweeney"),
    33: ("3585ad1f-cdbd-5643-84f0-365e1dc43671", "Rae Sweeney"),
    34: ("07716dc8-d660-5f9b-a104-fb5f793c2787", "Robert G Sweeney"),
    35: ("2cabc942-d942-54ef-9a8c-1e1da1d4deeb", "Ruth E Sweeney"),
    36: ("10239687-5a89-5853-b0a5-3432b8094e3e", "Arabella Sweet"),
    37: ("0dcbdae1-4a16-5fca-bbd9-8ac24e9403b7", "Arthur P Sweet"),
    38: ("38f49725-f884-5673-af3c-d0177b454316", "Earl P Sweet"),
    39: ("e424a19b-9ebd-56b8-8940-ebc8f9cde496", "Florence H Sweet"),
    40: ("cb620f27-eab1-5efc-901c-2bd26fc0142f", "Joyeuse Sweet"),
    41: ("12efa622-83d0-5c8d-85f0-f86c4387b424", "Paul Sweet"),
    42: ("52839b7b-b20f-5e43-9d08-a869e5f6047f", "Paul R Sweet"),
    43: ("d302baf2-5f79-5d8c-bb24-c6e952a74aeb", "Paul R Sweet"),
    44: ("e282916a-cbf7-5f18-9e7f-b72c9c45ab7b", "Walden E Sweet"),
    45: ("0bc1344f-24f1-5892-8848-22294c9acdd7", "Adelaide V Sweetser"),
    46: ("046a86b6-7fbe-5a18-82dd-e52adb1b6957", "Frank L Sweetser"),
}

PAUL_DUPLICATE_GROUP = "p457-paul-r-sweet-r42-r43-b934"

ARMY = {
    30: {
        "entry": "1942-07-11",
        "code": "133",
        "occupation": "Secretaries",
        "locator": "PDF physical page 171; historical category 1-33",
    },
    37: {
        "entry": "1943-08-04",
        "code": "072",
        "occupation": "Retail managers",
        "locator": "PDF physical page 171; historical category 0-72",
    },
    38: {
        "entry": "1943-03-05",
        "code": "963",
        "occupation": "Nonprocess occupations in manufacturing, n.e.c.",
        "locator": "PDF physical page 174; historical category 9-63",
    },
}

UNRESOLVED = {
    24: "Exact-name OSS, military, employment and obituary searches supplied no Box 760 identity bridge.",
    25: "A rare-name Signal Corps officer-candidate and Pennsylvania radio records remain unassigned because the index row supplies no second corroborating identifier.",
    26: "Exact-name and spelling-variant searches supplied no defensible OSS or Box 760 identity bridge.",
    27: "Exact-name, institutional and newspaper searches supplied no defensible OSS or Box 760 identity bridge.",
    28: "Exact-name and employment searches did not distinguish the indexed Barbara P Sweeney from namesakes.",
    29: "Exact-name and military searches did not distinguish the indexed James S Sweeney from namesakes.",
    31: "This separately printed Joseph M Sweeney row carries a different protected identifier from row 30 and remains a separate unresolved person.",
    32: "Exact-name and military searches supplied no two-identifier match for Patrick J Sweeney.",
    33: "Exact-name, obituary and institutional searches supplied no defensible identity bridge for Rae Sweeney.",
    34: "The protected identifier and common name did not yield a defensible official-record match for Robert G Sweeney.",
    35: "Exact-name and employment searches supplied no defensible OSS or Box 760 identity bridge for Ruth E Sweeney.",
    36: "Exact-name and spelling-variant searches supplied no corroborated identity bridge for Arabella Sweet.",
    39: "Exact-name and institutional searches supplied no corroborated identity bridge for Florence H Sweet.",
    41: "The middle-initial-free Paul Sweet row remains separate from both printed Paul R Sweet rows and has no defensible identity bridge.",
    43: "This no-rank Paul R Sweet row may relate to the separately printed Dr Paul R Sweet row, but the shared name and box do not justify a merge or claim transfer.",
    44: "Exact-name, military and obituary searches supplied no two-identifier match for Walden E Sweet.",
    45: "Exact-name and spelling-variant searches supplied no defensible identity bridge for Adelaide V Sweetser.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 760-761",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 457, rows 24-46; checked against layout-preserving text and the rendered page image",
            "access_date": "2026-10-27",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. Full identifiers remain private. The two printed Paul R Sweet rows use an opaque possible-duplicate group without being merged.",
        },
        {
            "key": ARMY_SOURCE,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; three reviewed Batch 934 identity candidates",
            "access_date": "2026-10-27",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "Three exact-name, nonshared protected-identifier matches are accepted. No raw row or full identifier is public.",
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
            "access_date": "2026-10-27",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Used to interpret selected fields only.",
        },
        {
            "key": CODES,
            "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1CL_SD.pdf",
            "archival_identifier": "National Archives Identifier 1263923; Code No. 30",
            "title": "NARA Compiled Code Lists for the Electronic Army Serial Number Merged File",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives at College Park - Electronic Records",
            "publication_record_date": "2011-01-12; modified 2011-03-17",
            "locator": "PDF physical pages 171 and 174; categories 072, 133 and 963 visually checked",
            "access_date": "2026-10-27",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical categories identify neither a named employer nor workplace.",
        },
        {
            "key": RAUCH,
            "stable_url": "https://discovery.ucl.ac.uk/id/eprint/10099481/3/Rauch_Allied%20Intelligence%20Officers%E2%80%99%20Encounters%20with%20German%20Civilians.pdf",
            "archival_identifier": "DOI 10.1017/S0008938919001006",
            "title": "Good Bets, Bad Bets and Dark Horses: Allied Intelligence Officers' Encounters with German Civilians, 1944-45",
            "author_creator": "Stefanie Rauch",
            "repository_publisher": "Central European History; Cambridge University Press; UCL Discovery",
            "publication_record_date": "2020-03",
            "locator": "PDF pages 4 and 29; exact Box 761 Dr. Paul R. Sweet personnel-file citation and OSS Research & Analysis chronology",
            "access_date": "2026-10-27",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Central European History 53, no. 1",
            "rights_notes": "The article cites the exact RG 226 Entry 224 Box 761 personnel file and distinguishes OSS service from prewar academic employment.",
        },
        {
            "key": INTERVIEW,
            "stable_url": "https://www.tandfonline.com/doi/abs/10.1111/j.1540-6563.1997.tb00992.x",
            "archival_identifier": "DOI 10.1111/j.1540-6563.1997.tb00992.x",
            "title": "Interview with Paul Sweet",
            "author_creator": "Paul R. Sweet; Linda Cooke Johnson",
            "repository_publisher": "The Historian; Taylor & Francis",
            "publication_record_date": "1997",
            "locator": "Abstract and biographical note; Bates College teaching listed",
            "access_date": "2026-10-27",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "The Historian 59, no. 2",
            "rights_notes": "Only the public abstract and biographical note were used.",
        },
        {
            "key": MILITANT,
            "stable_url": "https://www.marxists.org/history/etol/newspape/themilitant/1945/v9n10-mar-10-1945.pdf",
            "archival_identifier": "The Militant, vol. 9, no. 10",
            "title": "Report Gives Real Story of German People's Views",
            "repository_publisher": "The Militant",
            "publication_record_date": "1945-03-10",
            "locator": "Page 2; Paul Sweet identified contemporaneously as professor of German history at Bates College",
            "access_date": "2026-10-27",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "The Militant newspaper archive",
            "rights_notes": "Used only as a contemporaneous corroboration of the named Bates College role, not for political interpretation.",
        },
        {
            "key": DENSHO,
            "stable_url": "https://encyclopedia.densho.org/Frank_L._Sweetser/",
            "archival_identifier": "Densho Encyclopedia person article",
            "title": "Frank L. Sweetser",
            "repository_publisher": "Densho Encyclopedia",
            "publication_record_date": "2015-05-12",
            "locator": "Biographical paragraph; Columbia, War Relocation Authority and Navy chronology",
            "access_date": "2026-10-27",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Densho Encyclopedia",
            "rights_notes": "The text is CC BY-NC-SA 3.0. Only a short excerpt and project-authored paraphrase are retained.",
        },
        {
            "key": DARTMOUTH,
            "stable_url": "https://archive.dartmouthalumnimagazine.com/article/1943/12/1/dartmouth-war-directory",
            "archival_identifier": "Dartmouth Alumni Magazine, December 1943",
            "title": "Dartmouth War Directory",
            "author_creator": "Dartmouth Alumni Records Office",
            "repository_publisher": "Dartmouth Alumni Magazine",
            "publication_record_date": "1943-12",
            "locator": "Class of 1934 listing; Frank L. Sweetser, Lieutenant (junior grade), Naval Reserve",
            "access_date": "2026-10-27",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Dartmouth Alumni Magazine Archive",
            "rights_notes": "Contemporary institutional roster used to corroborate the exact full name, class year, Navy status and rank.",
        },
        {
            "key": CEMETERY,
            "stable_url": "https://www.interment.net/data/us/ma/barnstable/massnat/mass_swte.htm",
            "archival_identifier": "Massachusetts National Cemetery transcription, Sweetser entry",
            "title": "Massachusetts National Cemetery - Surnames Sw-Te",
            "repository_publisher": "Interment.net",
            "locator": "Frank L Sweetser entry; birth and death dates, U.S. Navy, Lieutenant",
            "access_date": "2026-10-27",
            "source_quality": "D_correlative_or_secondary",
            "collection_name": "Massachusetts National Cemetery transcriptions",
            "rights_notes": "Used only as corroboration of the same birth and death dates and Navy rank reported by institutional sources.",
        },
        {
            "key": JOY_OBIT,
            "stable_url": "https://www.tributearchive.com/obituaries/1650013/joyeuse-sweet-buell",
            "archival_identifier": "Macy & Son Funeral Directors obituary",
            "title": "Joyeuse Sweet Buell Obituary",
            "author_creator": "Macy & Son Funeral Directors",
            "repository_publisher": "Tribute Archive",
            "publication_record_date": "2007",
            "locator": "Biographical paragraph; parents, Sidwell 1940 and Mount Holyoke 1944",
            "access_date": "2026-10-27",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Tribute Archive obituaries",
            "rights_notes": "The obituary reports a 1923 birth year; the Yale finding aid reports 1922. The disagreement is preserved.",
        },
        {
            "key": YALe,
            "stable_url": "https://ead-pdfs.library.yale.edu/103.pdf",
            "archival_identifier": "RG 150, Lennig Sweet Papers",
            "title": "Guide to the Lennig Sweet Papers",
            "author_creator": "Yale Divinity Library Special Collections",
            "repository_publisher": "Yale University Library",
            "locator": "PDF page 4; Lennig and Helen Firman Sweet family chronology naming daughter Joyeuse",
            "access_date": "2026-10-27",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Lennig Sweet Papers, Record Group 150",
            "rights_notes": "The finding aid reports Joyeuse as born in 1922, one year earlier than the obituary. The discrepancy prevents an unqualified identity claim.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": "bates-college-b934",
            "canonical_name": "Bates College",
            "historical_name": "Bates College",
            "aliases": [],
            "organization_type": "college",
            "sector": "academia_and_research",
            "city": "Lewiston",
            "state_or_region": "Maine",
            "country": "United States",
            "active_dates": "1855-present",
            "normalization_notes": "Historical college name preserved; no modern successor substitution is required.",
        },
        {
            "key": "wra-b934",
            "canonical_name": "War Relocation Authority",
            "historical_name": "War Relocation Authority",
            "aliases": ["WRA"],
            "organization_type": "federal agency",
            "sector": "federal_government",
            "city": "Washington",
            "state_or_region": "District of Columbia",
            "country": "United States",
            "active_dates": "1942-1946",
            "normalization_notes": "The historical federal agency is kept distinct from later organizations and is not described with a modern successor name.",
        },
        {
            "key": "mount-holyoke-existing-b934",
            "organization_id": "5ccae842-432b-5af6-9ac6-50b6f58c7515",
            "canonical_name": "Mount Holyoke College",
            "historical_name": "Mt. Holyoke College",
            "aliases": ["Mount Holyoke", "Mt. Holyoke"],
            "organization_type": "college",
            "sector": "academia_and_research",
            "city": "South Hadley",
            "state_or_region": "Massachusetts",
            "country": "United States",
            "normalization_notes": "Existing canonical organization reused. Student status is not employment.",
        },
        {
            "key": "columbia-existing-b934",
            "organization_id": "87e3d52a-9ace-512a-9677-e966b7fbd5e5",
            "canonical_name": "Columbia University",
            "historical_name": "Columbia University",
            "aliases": ["Columbia"],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "New York",
            "state_or_region": "New York",
            "country": "United States",
            "normalization_notes": "Existing canonical organization reused. Graduate student status is not employment.",
        },
    ]


def army_affiliations() -> list[dict[str, object]]:
    result: list[dict[str, object]] = []
    for row, data in ARMY.items():
        person_id, name = PEOPLE[row]
        result.append(
            {
                "key": f"{slug(name)}-row{row}-occupation-b934",
                "person_id": person_id,
                "occupation": data["occupation"],
                "relationship_type": "employment",
                "end_date": data["entry"],
                "date_precision": "Army entry date; beginning and duration are not stated",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "A_direct_official",
                "publication_status": "publish_qualified",
                "research_notes": "The official historical category is tied to Army entry. It identifies no employer or workplace and is not promoted to an immediate pre-OSS affiliation.",
            }
        )
    return result


def named_affiliations() -> list[dict[str, object]]:
    return [
        {
            "key": "joyeuse-sweet-mount-holyoke-b934",
            "person_id": PEOPLE[40][0],
            "organization_key": "mount-holyoke-existing-b934",
            "organization_name_as_found": "Mount Holyoke College",
            "role_title": "Student; B.A. in Economics",
            "occupation": "student",
            "relationship_type": "student",
            "end_date": "1944",
            "date_precision": "Graduation year stated in the obituary",
            "city": "South Hadley",
            "state_or_region": "Massachusetts",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "probable",
            "claim_confidence": "medium",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "publish_qualified",
            "research_notes": "Student status, not employment. The rare exact name and matching parents support a probable identity, but the obituary and Yale finding aid disagree by one year on birth year.",
        },
        {
            "key": "paul-r-sweet-bates-b934",
            "person_id": PEOPLE[42][0],
            "organization_key": "bates-college-b934",
            "organization_name_as_found": "Bates College",
            "role_title": "Professor of German history",
            "occupation": "historian and professor",
            "relationship_type": "employment",
            "date_precision": "Last pre-OSS teaching institution supported; exact leave, separation and transition dates not stated",
            "city": "Lewiston",
            "state_or_region": "Maine",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": True,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "published",
            "research_notes": "The interview lists Bates among Sweet's teaching posts, and a contemporaneous 1945 newspaper identifies him as its professor of German history. The exact termination or leave date remains unresolved.",
        },
        {
            "key": "frank-l-sweetser-columbia-b934",
            "person_id": PEOPLE[46][0],
            "organization_key": "columbia-existing-b934",
            "organization_name_as_found": "Columbia University",
            "role_title": "Doctoral student; Ph.D. dissertation completed",
            "occupation": "sociology doctoral student",
            "relationship_type": "student",
            "end_date": "1942",
            "date_precision": "Completion year stated by Densho",
            "city": "New York",
            "state_or_region": "New York",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "published",
            "research_notes": "Graduate student status, not employment; Densho dates completion before the War Relocation Authority position.",
        },
        {
            "key": "frank-l-sweetser-wra-b934",
            "person_id": PEOPLE[46][0],
            "organization_key": "wra-b934",
            "organization_name_as_found": "War Relocation Authority's Community Analysis Section",
            "role_title": "Initial assistant director; deputy to John Fee Embree",
            "occupation": "sociologist",
            "relationship_type": "employment",
            "start_date": "1942",
            "end_date": "1943",
            "date_precision": "Eight-month tenure ending in summer 1943; exact start and end days not stated",
            "city": "Washington",
            "state_or_region": "District of Columbia",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": True,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "published",
            "research_notes": "Densho explicitly says Sweetser left this civilian federal role in summer 1943 to join the Navy. The intervening Navy service means WRA is not labeled the immediate pre-OSS assignment.",
        },
    ]


def affiliations() -> list[dict[str, object]]:
    return [*army_affiliations(), *named_affiliations()]


def army_claims() -> list[dict[str, object]]:
    result: list[dict[str, object]] = []
    for row, data in ARMY.items():
        person_id, name = PEOPLE[row]
        result.extend(
            [
                {
                    "key": f"identity-{slug(name)}-row{row}-b934",
                    "person_id": person_id,
                    "claim_type": "identity",
                    "claim_text": f"The indexed {name} row {row} is a high-confidence match to an official Army record dated {data['entry']}.",
                    "evidence_paraphrase": "The reviewed Army row agrees through the exact full name and a nonshared protected identifier.",
                    "identity_match_assessment": "High confidence from an exact full name and a nonshared protected identifier.",
                    "temporal_assessment": f"The Army record documents entry on {data['entry']}; it does not establish the OSS transfer date.",
                    "source_quality": "A_direct_official",
                    "claim_confidence": "high",
                    "publication_status": "published",
                    "match_notes": "The protected identifier is withheld. No employer or workplace is inferred.",
                    "sources": [
                        {"source_key": INDEX, "locator_override": f"PDF page 457 row {row}; Box {'760' if row == 30 else '761'}"},
                        {"source_key": ARMY_SOURCE, "locator_override": f"Accepted reviewed identity record; Army entry {data['entry']}; protected identifier withheld"},
                        {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46; field definitions"},
                    ],
                },
                {
                    "key": f"occupation-{slug(name)}-row{row}-b934",
                    "person_id": person_id,
                    "affiliation_key": f"{slug(name)}-row{row}-occupation-b934",
                    "claim_type": "occupation",
                    "claim_text": f"At Army entry on {data['entry']}, {name} was recorded in the historical category {data['occupation']}; no employer or workplace is identified.",
                    "evidence_excerpt": data["occupation"],
                    "evidence_paraphrase": f"The accepted Army record carries civilian-occupation code {data['code']}, decoded from NARA's official code list.",
                    "identity_match_assessment": "The category is assigned only to the accepted protected-identifier match; the identifier itself is not public.",
                    "temporal_assessment": "Strongly date-bounded to Army entry, but not proven to be the immediate pre-OSS affiliation.",
                    "source_quality": "A_direct_official",
                    "claim_confidence": "medium",
                    "publication_status": "publish_qualified",
                    "match_notes": "Historical language is preserved and is not converted into a company, workplace or more specific modern job title.",
                    "sources": [
                        {"source_key": ARMY_SOURCE, "locator_override": f"Army entry {data['entry']}; civilian-occupation code {data['code']}; protected identifier withheld"},
                        {"source_key": CODES, "locator_override": data["locator"]},
                    ],
                },
            ]
        )
    return result


def named_claims() -> list[dict[str, object]]:
    return [
        {
            "key": "identity-joyeuse-sweet-b934",
            "person_id": PEOPLE[40][0],
            "claim_type": "identity",
            "claim_text": "The indexed Joyeuse Sweet is a probable match to Joyeuse Sweet Buell, daughter of Lennig and Helen Firman Sweet and a 1944 Mount Holyoke graduate.",
            "evidence_paraphrase": "The obituary and Yale finding aid independently align the rare exact name and both parents, but differ by one year on Joyeuse's birth year.",
            "identity_match_assessment": "Probable rather than high confidence because neither source explicitly mentions OSS or Box 761, and the birth-year disagreement remains unresolved.",
            "temporal_assessment": "The 1944 graduation is documented before the end of OSS operations but is not proven to be immediately before OSS service.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "medium",
            "publication_status": "publish_qualified",
            "match_notes": "The one-year birth discrepancy is retained. Box 761 remains necessary before upgrading the identity.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 457 row 40; Box 761"},
                {"source_key": JOY_OBIT, "locator_override": "Biographical paragraph; parents and education"},
                {"source_key": YALe, "locator_override": "PDF page 4; family chronology", "support_type": "supports"},
            ],
        },
        {
            "key": "other-joyeuse-sweet-mount-holyoke-b934",
            "person_id": PEOPLE[40][0],
            "affiliation_key": "joyeuse-sweet-mount-holyoke-b934",
            "claim_type": "other_pre_oss_affiliation",
            "claim_text": "Joyeuse Sweet graduated from Mount Holyoke College in 1944 with a B.A. in Economics.",
            "evidence_excerpt": "Mount Holyoke College ... in 1944 with a B.A. in Economics",
            "evidence_paraphrase": "The obituary names the college, year and degree; Yale corroborates the rare-name family identity but not the education detail.",
            "identity_match_assessment": "Probable identity with an unresolved one-year birth-date discrepancy.",
            "temporal_assessment": "Documented pre-OSS student affiliation; not employment and not established as immediate.",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "claim_confidence": "medium",
            "publication_status": "publish_qualified",
            "match_notes": "The college is not labeled an employer.",
            "sources": [{"source_key": JOY_OBIT, "locator_override": "Biographical paragraph; education chronology"}],
        },
        {
            "key": "identity-paul-r-sweet-row42-b934",
            "person_id": PEOPLE[42][0],
            "claim_type": "identity",
            "claim_text": "The indexed Dr Paul R Sweet row is a high-confidence match to historian Paul R. Sweet of OSS Research & Analysis and the Psychological Warfare Division.",
            "evidence_paraphrase": "Rauch cites the exact RG 226 Entry 224 Box 761 file for Dr. Paul R. Sweet and aligns the name, title, German-history specialty and wartime OSS chronology.",
            "identity_match_assessment": "High confidence from the exact name, Dr title, exact index box and direct archival file citation in a peer-reviewed scholarly source.",
            "temporal_assessment": "Rauch documents OSS Research & Analysis service in London before the autumn 1944 field assignment.",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "The separately printed no-rank Paul R Sweet row remains a separate possible duplicate and receives no transferred claim.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 457 row 42; Dr; Box 761"},
                {"source_key": RAUCH, "locator_override": "PDF pages 4 and 29; exact Box 761 personnel-file citation"},
            ],
        },
        {
            "key": "last-civilian-paul-r-sweet-bates-b934",
            "person_id": PEOPLE[42][0],
            "affiliation_key": "paul-r-sweet-bates-b934",
            "claim_type": "last_civilian_pre_service",
            "claim_text": "Paul R. Sweet's best-supported last civilian employer before OSS service is Bates College, where he taught history.",
            "evidence_excerpt": "professor of German history at Bates College",
            "evidence_paraphrase": "Sweet's published interview lists Bates among his teaching posts, and a contemporaneous March 1945 newspaper identifies his Bates role while reporting his Army intelligence work.",
            "identity_match_assessment": "High confidence through the exact Box 761 Dr. Paul R. Sweet file citation and matching historian chronology.",
            "temporal_assessment": "Strongly date-bounded as the last identified pre-OSS civilian teaching post; the exact leave or separation date is not stated, so it is not labeled explicit immediate.",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "No intervening civilian employer is documented in the reviewed sources. The personnel file should confirm the exact transition date.",
            "sources": [
                {"source_key": INTERVIEW, "locator_override": "Public abstract and biographical note; Bates College teaching"},
                {"source_key": MILITANT, "locator_override": "Page 2; contemporaneous Bates College role"},
                {"source_key": RAUCH, "support_type": "supports", "locator_override": "PDF pages 4 and 29; identity and OSS chronology"},
            ],
        },
        {
            "key": "identity-frank-l-sweetser-b934",
            "person_id": PEOPLE[46][0],
            "claim_type": "identity",
            "claim_text": "The indexed Frank L Sweetser is a high-confidence match to sociologist and Navy Lieutenant Frank L. Sweetser, born in 1913.",
            "evidence_paraphrase": "Densho, the contemporary Dartmouth roster and cemetery transcription align the exact full name, 1934 Dartmouth class, Navy service and rank, and the same birth and death dates.",
            "identity_match_assessment": "High confidence from a distinctive exact full name and multiple mutually consistent educational, chronological and military identifiers across independent sources.",
            "temporal_assessment": "Densho explicitly dates the WRA-to-Navy transition to summer 1943; the exact Navy-to-OSS sequence remains unestablished.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "The index establishes the Box 761 OSS-file context. The sources do not establish an exact OSS assignment date.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 457 row 46; Box 761"},
                {"source_key": DENSHO, "locator_override": "Biographical paragraph"},
                {"source_key": DARTMOUTH, "locator_override": "Class of 1934 listing; Lieutenant (junior grade), Naval Reserve"},
                {"source_key": CEMETERY, "support_type": "supports", "locator_override": "Frank L Sweetser entry; birth and death dates, Navy Lieutenant"},
            ],
        },
        {
            "key": "other-frank-l-sweetser-columbia-b934",
            "person_id": PEOPLE[46][0],
            "affiliation_key": "frank-l-sweetser-columbia-b934",
            "claim_type": "other_pre_oss_affiliation",
            "claim_text": "Frank L. Sweetser completed his Columbia University Ph.D. dissertation in 1942 before joining the War Relocation Authority.",
            "evidence_excerpt": "finished his Ph.D. dissertation ... in 1942",
            "evidence_paraphrase": "Densho places the Columbia doctoral work immediately before the WRA position.",
            "identity_match_assessment": "High confidence from the distinctive exact-name and Navy chronology across independent sources.",
            "temporal_assessment": "Explicitly pre-WRA and pre-Navy student affiliation; not employment.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "Columbia University is not labeled an employer.",
            "sources": [{"source_key": DENSHO, "locator_override": "Biographical paragraph; Columbia-to-WRA chronology"}],
        },
        {
            "key": "last-civilian-frank-l-sweetser-wra-b934",
            "person_id": PEOPLE[46][0],
            "affiliation_key": "frank-l-sweetser-wra-b934",
            "claim_type": "last_civilian_pre_service",
            "claim_text": "Frank L. Sweetser's last documented civilian employer before Navy service was the War Relocation Authority, where he was assistant director of the Community Analysis Section.",
            "evidence_excerpt": "leaving in the summer of 1943 to join the navy",
            "evidence_paraphrase": "Densho identifies Sweetser as the section's initial assistant director and John Fee Embree's deputy for eight months, ending when he joined the Navy.",
            "identity_match_assessment": "High confidence from the distinctive exact-name, Dartmouth, Navy rank, birth-date and chronology alignment.",
            "temporal_assessment": "Explicit civilian-to-military transition in 1943. WRA is not labeled the immediate pre-OSS affiliation because Navy service intervened and the later Navy-to-OSS sequence is not established.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "The physical personnel file is still needed to establish the Navy-to-OSS sequence and exact OSS assignment.",
            "sources": [
                {"source_key": DENSHO, "locator_override": "Biographical paragraph; WRA role and summer 1943 Navy transition"},
                {"source_key": DARTMOUTH, "support_type": "supports", "locator_override": "December 1943 Navy roster"},
            ],
        },
    ]


def claims() -> list[dict[str, object]]:
    return [*army_claims(), *named_claims()]


def archival_update(row: int, reason: str) -> dict[str, object]:
    person_id, name = PEOPLE[row]
    box = "760" if row <= 35 else "761"
    update: dict[str, object] = {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, Box {box} and archive location, but staged official-register, CIA-site, OSS, employment, occupation, obituary, institutional, newspaper, Library of Congress and archival searches found no defensible identity bridge. {reason}",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": f"Review Box {box} for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }
    if row == 43:
        update["possible_duplicate_group"] = PAUL_DUPLICATE_GROUP
        update["archival_review_priority"] = "critical"
        update["next_action"] = "Review both Box 761 Paul R Sweet files together. Do not merge the printed rows or transfer Dr Paul R Sweet's Bates claim unless the files establish duplication."
    return update


def person_updates() -> list[dict[str, object]]:
    updates = [archival_update(row, reason) for row, reason in UNRESOLVED.items()]
    for row in ARMY:
        box = "760" if row == 30 else "761"
        updates.append(
            {
                "person_id": PEOPLE[row][0],
                "identity_status": "high_confidence",
                "identity_evidence": "An exact full name and nonshared protected identifier connect the visually verified index row to the reviewed official Army record. The historical occupation field remains separate from employer and immediate-affiliation claims.",
                "personnel_category": "enlisted_army_personnel",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "occupation_only_found",
                "next_action": f"Review Box {box} for the immediate pre-OSS affiliation and a named employer or institution.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            }
        )
    updates.extend(
        [
            {
                "person_id": PEOPLE[40][0],
                "identity_status": "probable",
                "identity_evidence": "The rare exact name and both parents align between an obituary and Yale finding aid, supporting a probable match. Their 1923 versus 1922 birth-year disagreement and absence of an OSS-specific bridge prevent a high-confidence identity.",
                "name_variants": ["Joyeuse Sweet Buell", "Joy Sweet Buell"],
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Review Box 761 to resolve the birth-year discrepancy, confirm the identity and determine the immediate pre-OSS affiliation. Mount Holyoke is documented only as student status.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[42][0],
                "identity_status": "high_confidence",
                "identity_evidence": "A peer-reviewed scholarly article cites the exact RG 226 Entry 224 Box 761 file for Dr. Paul R. Sweet and aligns the name, title, German-history specialty and OSS Research & Analysis chronology.",
                "name_variants": ["Paul R. Sweet", "Dr. Paul R. Sweet"],
                "personnel_category": "civilian_professional_or_administrative_grade",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "possible_duplicate_group": PAUL_DUPLICATE_GROUP,
                "research_status": "verified_employer_found",
                "next_action": "Review Box 761 to confirm the exact Bates College leave or separation date and resolve the separately printed no-rank Paul R Sweet row.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[46][0],
                "identity_status": "high_confidence",
                "identity_evidence": "Densho, a contemporary Dartmouth roster and cemetery transcription align the distinctive exact full name, 1934 class, 1913 birth, Navy service and lieutenant rank.",
                "name_variants": ["Frank L. Sweetser"],
                "personnel_category": "commissioned_naval_officer",
                "commissioned_officer": True,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "verified_employer_found",
                "next_action": "Review Box 761 to establish the Navy-to-OSS sequence and exact OSS assignment; the WRA-to-Navy transition is already documented.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
        ]
    )
    return updates


def research_attempts() -> list[dict[str, object]]:
    attempts: list[dict[str, object]] = []
    for row in sorted(PEOPLE):
        person_id, name = PEOPLE[row]
        box = "760" if row <= 35 else "761"
        if row in ARMY:
            outcome, reviewed, rejected = "source_reviewed", 9, 3
            detail = "An exact name and nonshared protected identifier support a high-confidence official Army identity bridge and dated occupation-only evidence."
        elif row == 40:
            outcome, reviewed, rejected = "source_reviewed", 10, 4
            detail = "Two sources support a probable rare-name identity and 1944 Mount Holyoke student affiliation, while a one-year birth discrepancy remains explicit."
        elif row == 42:
            outcome, reviewed, rejected = "source_reviewed", 13, 4
            detail = "An exact Box 761 personnel-file citation supports a high-confidence identity, and two sources support Bates College as the best-documented last civilian employer."
        elif row == 46:
            outcome, reviewed, rejected = "source_reviewed", 12, 4
            detail = "Independent institutional and biographical sources support a high-confidence identity, Columbia student status and an explicit War Relocation Authority-to-Navy chronology."
        else:
            outcome, reviewed, rejected = "no_result", 7, 4
            detail = UNRESOLVED[row]
        attempts.append(
            {
                "key": f"page457-row{row}-{slug(name)}-b934",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA index and public Archives context; CIA Reading Room site-restricted exact-name discovery; OSS and spelling variants; employer and occupation 1940; obituary, institutional, newspaper, Library of Congress and archival searches; Box {box}; protected-identifier Army crosswalk where defensible",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_934",
                "started_at": "2026-10-27T23:00:00Z",
                "completed_at": "2026-10-28T00:35:00Z",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search snippets, genealogy-only assertions, modern people-finder pages, postwar-only leads and sources without an OSS, protected-identifier or Box-file bridge were not assigned. Grouped CIA Reading Room and Library of Congress exact-name checks produced no additional defensible person-specific result.",
                "research_notes": f"{detail} The index page and relevant Army code-list pages were visually checked. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA API call was made.",
                "next_action": f"Review Box {box} for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before military service.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b934-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-934-v1",
        "reviewer": "Before OSS Batch 934 evidence review",
        "sources": sources(),
        "organizations": organizations(),
        "affiliations": affiliations(),
        "claims": claims(),
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }
    OUTPUT.write_text(
        json.dumps(bundle, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
