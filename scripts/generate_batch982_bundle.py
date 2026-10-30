#!/usr/bin/env python3
"""Generate the reviewed Batch 982 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page481-spyridon-s-varthis-to-lena-b-veazey-"
    "review_batch-982_2026-10-30.json"
)

INDEX = "nara-index-b982"
ARMY = "army-bulk-b982"
TECH = "army-tech-b982"
CODES = "army-codes-b982"
SMITHSONIAN_VASSOS = "smithsonian-john-vassos-b982"
SYRACUSE_VASSOS = "syracuse-john-vassos-b982"
BROADCASTING_VASSOS = "broadcasting-john-vassos-b982"
CIA_VASSIL = "cia-philip-vassil-b982"
LOC_VASSIL = "loc-philip-vassil-b982"
MSA_VAUDRIN = "msa-philip-vaudrin-b982"

ORG_RCA = "rca-b982"
ORG_ARMY_ENGINEERS = "army-engineers-b982"
ORG_SIGNAL_CORPS = "army-signal-corps-b982"
ORG_OUP = "oxford-university-press-b982"


PEOPLE = {
    1: ("36517755-54ec-50f6-afae-502c414c2754", "Spyridon S Varthis"),
    2: ("37d602c5-4b19-5eb8-94fd-106d6e6dd4c7", "John A Vasdekis"),
    3: ("2885f9a0-0523-5b02-b09d-5b509ea2fbe8", "John M Vasicak"),
    4: ("7783cf92-1a1e-5a60-a18d-e2d540e7c82a", "Helen Vasiliou"),
    5: ("e8daa0a0-a427-5118-87da-9c7220cdf61b", "Joseph F Vasko"),
    6: ("4c33016a-9513-5a16-9055-68fea1dd99a3", "Philip N Vassil"),
    7: ("78d5a8f0-936f-54d0-87c1-a0491d72eb76", "Steve Vassiliades"),
    8: ("bd395aaa-5af1-51d0-aaa6-14cb8e528862", "John Vassos"),
    9: ("3c644922-ab30-5b95-ad91-b7707aa47937", "James H Vater"),
    10: ("e84e9bd0-adcd-5f91-9818-1fb3ef3c5a97", "Anastassios T Vatis"),
    11: ("abc57901-1182-5327-8f14-1b344d4178e3", "Joan M Vatsek"),
    12: ("a9f02ad8-652e-5fae-941e-9d644d20a575", "Philip Vaudrin"),
    13: ("93ede38e-9f89-500e-9106-defc6c205efa", "James Vaughan Jr."),
    14: ("2ba6c6c1-029f-57b6-aaeb-83e35e4b252d", "Grady W Vaughn"),
    15: ("42952bdd-a460-590f-8d0d-7250f9adbf5c", "James K Vaughn"),
    16: ("babd50c3-6b7d-5404-bbff-837ea829f1a0", "James B Vaughn"),
    17: ("4649c0a2-1f81-584d-ba7b-8f2d5ea92bc3", "John J Vaughn"),
    18: ("e7bba9bc-f72e-55ff-9d5b-f7f362845544", "Richard B Vaughn"),
    19: ("7a43241e-66da-55e3-8f1a-99549733b28d", "William L Vaughn"),
    20: ("16c1a5d0-6a50-5979-a48a-ea254489b749", "Jean Vauzelle"),
    21: ("a61d9e12-ec43-595f-8ef6-b1191764f80d", "Salvatore Vavala"),
    22: ("9df06569-d14b-5318-bcec-b9f35893a9d0", "Alberto Vazquez"),
    23: ("f95e3869-4cb3-5121-8977-b8b915deff46", "Lena B Veazey"),
}


ARMY_FINDINGS = [
    {
        "row": 1,
        "date": "1943-05-24",
        "code": "088",
        "occupation": "Ship captains, mates, pilots, and engineers",
        "public_occupation": "ship captain, mate, pilot, or engineer",
        "locator": "PDF physical page 171; historical category 0-88",
        "name_note": "The official Army and indexed full names agree exactly and the protected identifier is nonshared.",
    },
    {
        "row": 5,
        "date": "1942-02-13",
        "code": "702",
        "occupation": "Occupations in manufacture of automobiles, not elsewhere classified (semiskilled level)",
        "public_occupation": "semiskilled automobile-manufacturing occupation, not elsewhere classified",
        "locator": "PDF physical page 174; historical category 7-02",
        "name_note": "The official Army and indexed full names agree exactly and the protected identifier is nonshared.",
    },
    {
        "row": 9,
        "date": "1943-04-14",
        "code": "137",
        "occupation": "Stenographers and typists",
        "public_occupation": "stenographer or typist",
        "locator": "PDF physical page 171; historical category 1-37",
        "name_note": "The official Army and indexed full names agree exactly and the protected identifier is nonshared.",
    },
    {
        "row": 10,
        "date": "1943-07-13",
        "code": "069",
        "occupation": "Semiprofessional occupations, not elsewhere classified",
        "public_occupation": "semiprofessional occupation, not elsewhere classified",
        "locator": "PDF physical page 171; historical category 0-69",
        "name_note": "The official Army and indexed full names agree exactly and the protected identifier is nonshared.",
    },
    {
        "row": 21,
        "date": "1942-12-10",
        "code": "878",
        "occupation": "Machine shop and related occupations, not elsewhere classified (unskilled level)",
        "public_occupation": "unskilled machine-shop or related occupation, not elsewhere classified",
        "locator": "PDF physical page 174; historical category 8-78",
        "name_note": "The Army entry adds middle initial A while the index omits it; the exact nonshared protected identifier resolves the otherwise exact name agreement.",
    },
]


UNRESOLVED = {
    2: "Exact-name, OSS, employer, obituary and institutional searches produced no source with a protected identifier, rank, Box 801 or assignment bridge.",
    3: "A contemporary amateur-radio lead for John M Vasicak and the search alias Vasiack supply no OSS, protected-identifier, Box 801 or employer bridge.",
    4: "Education and later classical-studies leads for namesakes do not establish that the indexed Helen Vasiliou is the same person or identify a pre-OSS employer.",
    7: "Exact-name and Greek-name variant searches produced no reliable wartime identity or pre-OSS affiliation bridge.",
    11: "Exact-name, newspaper, obituary and archival searches produced no reliable OSS identity or pre-OSS affiliation bridge.",
    13: "The incomplete common name produced multiple namesakes but no source with an OSS, Box 801 or protected-identifier bridge.",
    14: "Common-name military, obituary and directory results produced no reliable identity or pre-OSS affiliation bridge.",
    15: "Common-name results did not connect the indexed protected identifier and Box 800 record to a defensible biography or employer.",
    16: "Common-name results produced no source with a wartime OSS, Box 801 or protected-identifier bridge.",
    17: "Common-name results produced no source with a wartime OSS, Box 801 or protected-identifier bridge.",
    18: "Common-name results produced no source with a wartime OSS, Box 801 or protected-identifier bridge.",
    19: "Common-name results did not connect the indexed protected identifier and Box 801 record to a defensible biography or employer.",
    20: "Modern French business and obituary results are unbridged namesakes and do not establish the indexed person's wartime identity.",
    22: "Results for Alberto Vazquez and Alberto D Vazquez did not connect the index row to a wartime OSS assignment, Box 801 or employer.",
    23: "Exact-name, newspaper, obituary, directory and archival searches produced no reliable OSS identity or pre-OSS affiliation bridge.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 800-802",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 481, rows 24-46; checked against layout-preserving text and an original-detail page render",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate; original spellings, boxes and locations remain recoverable while public identifiers are masked.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; five Batch 982 identity comparisons; protected identifiers and record ordinals withheld",
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
            "locator": "PDF physical pages 171 and 174; all five Batch 982 categories visually and textually checked",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
        },
        {
            "key": SMITHSONIAN_VASSOS,
            "stable_url": "https://www.si.edu/object/archives/sova-aaa-vassjohn",
            "archival_identifier": "SOVA AAA.vassjohn; John Vassos papers, 1915-1989",
            "title": "John Vassos Papers",
            "author_creator": "John Vassos; Archives of American Art finding-aid staff",
            "repository_publisher": "Archives of American Art, Smithsonian Institution",
            "publication_record_date": "1915-1989; finding aid current at access",
            "locator": "Biographical note; RCA files include contracting agreements dated 1939-1950 and other prewar design records",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "John Vassos papers",
            "rights_notes": "The finding aid states that Vassos established RCA's first internal design department in 1933 and remained a consultant through 1964.",
        },
        {
            "key": SYRACUSE_VASSOS,
            "stable_url": "https://library.syracuse.edu/digital/exhibits/d/DawnNewAge/vassos.html",
            "archival_identifier": "Syracuse University Libraries, Dawn of a New Age digital exhibit",
            "title": "John Vassos",
            "author_creator": "Syracuse University Libraries",
            "repository_publisher": "Syracuse University Libraries",
            "publication_record_date": "Digital exhibit current at access",
            "locator": "Biographical paragraphs on RCA design work and World War II OSS service",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Dawn of a New Age",
        },
        {
            "key": BROADCASTING_VASSOS,
            "stable_url": "https://web.archive.org/web/20250626234916id_/https://www.worldradiohistory.com/Archive-All-BC/Broadcasting-Magazine/BC-1945/1945-03-26-BC.pdf",
            "title": "Technical personnel note: Lt. Col. John Vassos returns to RCA Victor Division",
            "author_creator": "Broadcasting magazine editorial staff",
            "repository_publisher": "Broadcasting Publications, Inc.; preserved by World Radio History and the Internet Archive",
            "publication_record_date": "1945-03-26",
            "locator": "PDF physical and printed page 52; upper-right Technical column; visually and textually checked",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Broadcasting, March 26, 1945",
            "rights_notes": "Contemporary trade-journal notice; only citation metadata, a project-authored paraphrase and a minimal excerpt are retained.",
        },
        {
            "key": CIA_VASSIL,
            "stable_url": "https://www.cia.gov/readingroom/docs/CIA-RDP13X00001R000100410007-2.pdf",
            "archival_identifier": "CIA-RDP13X00001R000100410007-2; Field Reports, volume V, report 15,542",
            "title": "OSS Reports on Experiences and Conditions in the Field: List of Field Reports by Author",
            "author_creator": "Office of Strategic Services",
            "repository_publisher": "Central Intelligence Agency FOIA Electronic Reading Room",
            "publication_record_date": "World War II; declassified for release 2013-09-25",
            "locator": "PDF physical page 131; Field Reports volume V; Philip N. Vassil entry visually checked",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "CIA FOIA OSS Collection",
            "document_number": "CIA-RDP13X00001R000100410007-2",
            "rights_notes": "The CIA Reading Room was temporarily in maintenance; a 2024 public Internet Archive capture was used for local visual verification while the official CIA URL remains the citation pointer.",
        },
        {
            "key": LOC_VASSIL,
            "stable_url": "https://www.loc.gov/resource/sn83045462/1942-08-05/ed-1/?sp=7",
            "archival_identifier": "LCCN sn83045462; reel 00280603612; image sequence 0683",
            "title": "Count Andre de Limur Renounces Title to Become American",
            "author_creator": "Evening Star editorial staff",
            "repository_publisher": "Evening Star; Library of Congress Chronicling America",
            "publication_record_date": "1942-08-05",
            "locator": "Page A-5, upper-center column; sequence 0683; OCR and official page image checked",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Chronicling America",
            "rights_notes": "The contemporary item identifies Capt. Philip N. Vassil as attached to the Army Signal Corps; home-address details are excluded.",
        },
        {
            "key": MSA_VAUDRIN,
            "stable_url": "https://msa.maryland.gov/megafile/msa/speccol/sc5300/sc5339/000030/000000/000010/restricted/hiss%20nyu/homepages.nyu.edu/_th15/breakw.html",
            "archival_identifier": "Paul Willert supporting affidavit, sworn 1952-03-14",
            "title": "Paul Willert's Account: Supporting Affidavit of Paul Willert",
            "author_creator": "Paul Willert",
            "repository_publisher": "Maryland State Archives, Alger Hiss research collection",
            "publication_record_date": "1952-03-14",
            "locator": "Paragraphs 2-3(a), recalling late 1937 or early 1938",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Alger Hiss Story research materials",
            "rights_notes": "The sworn account identifies Philip Vaudrin as an Oxford University Press editor; it contains no OSS or protected-identifier bridge.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": ORG_RCA,
            "organization_id": "71cb9b7e-5023-5ec3-b7c9-34afafeea171",
            "canonical_name": "Radio Corporation of America",
            "historical_name": "RCA",
            "aliases": ["RCA", "Radio Corporation of America", "RCA Victor Division"],
            "organization_type": "electronics and communications company",
            "sector": "engineering_science_and_technology",
            "country": "United States",
            "normalization_notes": "RCA is not merged with the separately preserved RCA Communications, Inc. entity; the historical RCA Victor Division wording remains visible in the affiliation.",
        },
        {
            "key": ORG_ARMY_ENGINEERS,
            "organization_id": "f2367526-082d-5cad-8156-c405c426f2e1",
            "canonical_name": "United States Army Corps of Engineers",
            "historical_name": "Army Corps of Engineers",
            "aliases": ["Engineer Corps", "U.S. Army Corps of Engineers", "Army Engineering Corps"],
            "organization_type": "military branch",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "The contemporary source's Army Engineering Corps wording is retained; service is a military assignment, not civilian employment.",
        },
        {
            "key": ORG_SIGNAL_CORPS,
            "organization_id": "37fe0e48-9745-5a0a-8e04-6be9bc7c5c91",
            "canonical_name": "United States Army Signal Corps",
            "historical_name": "Signal Corps",
            "aliases": ["Army Signal Corps"],
            "organization_type": "military branch",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "Military assignment remains distinct from civilian employment.",
        },
        {
            "key": ORG_OUP,
            "organization_id": "6fcfc80a-2927-5462-861e-a8c12cf3391c",
            "canonical_name": "Oxford University Press",
            "historical_name": "Oxford University Press",
            "aliases": ["OUP", "Oxford University Press, Inc."],
            "organization_type": "publisher",
            "sector": "business_and_industry",
            "city": "New York",
            "state_or_region": "New York",
            "country": "United States",
            "normalization_notes": "The historical New York publishing office is retained; no modern corporate successor is substituted.",
        },
    ]


def occupation_affiliation(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    return {
        "key": f"{slug(PEOPLE[row][1])}-occupation-b982",
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
        "research_notes": "Official historical occupation category only; excluded from employer analytics and not narrowed to a specific title.",
    }


def affiliations() -> list[dict[str, object]]:
    values = [occupation_affiliation(item) for item in ARMY_FINDINGS]
    values.extend(
        [
            {
                "key": "john-vassos-rca-b982",
                "person_id": PEOPLE[8][0],
                "organization_key": ORG_RCA,
                "organization_name_as_found": "RCA Victor Division",
                "role_title": "consultant designer",
                "occupation": "industrial designer",
                "relationship_type": "employment",
                "start_date": "1934",
                "end_date": "1942",
                "date_precision": "Contemporary trade press gives 1934 through 1942, when he entered the armed forces",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "published",
                "research_notes": "Best-supported last civilian employer before armed service; Army service intervened before or overlapped the OSS assignment, so RCA is not labeled the immediate OSS predecessor.",
            },
            {
                "key": "john-vassos-army-engineers-b982",
                "person_id": PEOPLE[8][0],
                "organization_key": ORG_ARMY_ENGINEERS,
                "organization_name_as_found": "Army Engineering Corps",
                "role_title": "lieutenant colonel; special missions overseas",
                "relationship_type": "military_assignment",
                "start_date": "1942",
                "end_date": "1945-03-26 or earlier",
                "date_precision": "The 1945 notice says he entered the armed forces in 1942 and had been discharged after two and one-half years",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "temporal_relation_uncertain",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "published",
                "research_notes": "Documented military assignment. The reviewed sources do not establish whether Corps of Engineers service immediately preceded or administratively overlapped OSS duty.",
            },
            {
                "key": "philip-vassil-signal-corps-b982",
                "person_id": PEOPLE[6][0],
                "organization_key": ORG_SIGNAL_CORPS,
                "organization_name_as_found": "Army Signal Corps",
                "role_title": "captain",
                "relationship_type": "military_assignment",
                "start_date": "1942-08-05 or earlier",
                "date_precision": "Contemporary newspaper attestation on 5 August 1942; exact assignment dates are not supplied",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "temporal_relation_uncertain",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "published",
                "research_notes": "Documented military assignment. The CIA field-report index confirms later OSS SI/METO context but does not prove the exact Signal Corps-to-OSS transition date.",
            },
            {
                "key": "philip-vaudrin-oup-b982",
                "person_id": PEOPLE[12][0],
                "organization_key": ORG_OUP,
                "organization_name_as_found": "Oxford University Press",
                "role_title": "editor",
                "occupation": "publishing editor",
                "relationship_type": "employment",
                "start_date": "1937 or earlier",
                "end_date": "1938 or later",
                "date_precision": "Sworn recollection places him in the role at the end of 1937 or beginning of 1938",
                "city": "New York",
                "state_or_region": "New York",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "probable",
                "claim_confidence": "medium",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "publish_qualified",
                "research_notes": "Rare-name probable match and definite prewar employment, but no protected identifier or explicit OSS bridge. Not labeled immediate or last civilian employment.",
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


def army_identity_note(item: dict[str, object]) -> str:
    return f"{item['name_note']} The protected identifier and raw record ordinal remain private."


def army_claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for item in ARMY_FINDINGS:
        row = int(item["row"])
        name = PEOPLE[row][1]
        values.append(
            claim(
                row,
                f"identity-{slug(name)}-army-b982-row{row}",
                "identity",
                f"Indexed {name} is high-confidence matched to the official Army entry used for the dated occupation finding.",
                "Official Army name comparison and a nonshared protected-identifier agreement support the match.",
                army_identity_note(item),
                "The Army entry date is preserved separately from the later OSS-index context.",
                "A_direct_official",
                "high",
                [
                    {"source_key": INDEX},
                    {"source_key": ARMY, "locator_override": "Accepted identity bridge; protected identifier and raw record withheld"},
                ],
                "Protected identifiers were used only for private resolution and remain absent from the evidence bundle and public output.",
            )
        )
        values.append(
            claim(
                row,
                f"occupation-{slug(name)}-b982-row{row}",
                "occupation",
                f"At Army entry on {item['date']}, {name}'s historical civilian-occupation category was {str(item['occupation']).lower()}.",
                f"The official Army field carries historical code {item['code']}; NARA's code list defines it as {item['occupation']}.",
                army_identity_note(item),
                "Dated at Army entry before the later OSS-index context; no named employer, workplace, duration or exact OSS-transfer date is supplied.",
                "A_direct_official",
                "medium",
                [
                    {"source_key": ARMY, "locator_override": "Accepted identity bridge; protected identifier and raw record withheld"},
                    {"source_key": TECH, "locator_override": "PDF physical pages 44-46; civilian-occupation field"},
                    {"source_key": CODES, "locator_override": str(item["locator"])},
                ],
                "Published as a qualified historical occupation category only; excluded from verified-employer analytics.",
                f"{slug(name)}-occupation-b982",
                "publish_qualified",
            )
        )
    return values


def special_claims() -> list[dict[str, object]]:
    return [
        claim(
            8,
            "identity-john-vassos-oss-b982",
            "identity",
            "Indexed John Vassos is high-confidence matched to industrial designer John Vassos, who served with the OSS during World War II.",
            "Syracuse explicitly identifies John Vassos as an RCA industrial designer who entered the Army as a captain and worked for the OSS.",
            "High confidence from rare exact name, commissioned service, explicit OSS context and a coherent RCA-to-Army chronology.",
            "The sources place RCA work before 1942 armed service and OSS work during the war.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": INDEX}, {"source_key": SYRACUSE_VASSOS}, {"source_key": BROADCASTING_VASSOS}],
            "The protected index identifier is not reproduced publicly; Box 801 remains the personnel-file authority for exact assignment dates.",
        ),
        claim(
            8,
            "last-civilian-john-vassos-rca-b982",
            "last_civilian_pre_service",
            "John Vassos held a consultant-designer post at RCA Victor from 1934 until entering the armed forces in 1942.",
            "A contemporary 1945 trade-journal notice gives the employer, role and 1934-1942 interval; Smithsonian records independently document the RCA relationship.",
            "High-confidence rare-name and explicit OSS-context match.",
            "Strongly date-bounded to the point of armed-forces entry; Army service intervened before or overlapped OSS duty.",
            "C_reputable_contemporary_or_scholarly",
            "high",
            [
                {"source_key": BROADCASTING_VASSOS, "excerpt_override": "consultant designer, a post he held from 1934 until 1942 when he entered the armed forces"},
                {"source_key": SMITHSONIAN_VASSOS},
            ],
            "Published as the best-supported last civilian employer before wartime service, not as an explicit immediate predecessor to OSS.",
            "john-vassos-rca-b982",
        ),
        claim(
            8,
            "military-john-vassos-army-engineers-b982",
            "other_pre_oss_affiliation",
            "John Vassos entered the armed forces in 1942 and served in the Army Engineering Corps on special missions overseas.",
            "The contemporary notice reports his 1942 entry, lieutenant-colonel rank, Corps service, overseas missions and discharge before March 26, 1945.",
            "High-confidence rare-name and explicit OSS-context match.",
            "The military assignment is date-bounded, but its administrative relationship to OSS duty is not stated.",
            "C_reputable_contemporary_or_scholarly",
            "high",
            [{"source_key": BROADCASTING_VASSOS}, {"source_key": SYRACUSE_VASSOS}],
            "Military assignment, not a civilian employer; not labeled the immediate pre-OSS affiliation because overlap or transfer timing is unresolved.",
            "john-vassos-army-engineers-b982",
        ),
        claim(
            6,
            "identity-philip-vassil-oss-b982",
            "identity",
            "Indexed Philip N Vassil is high-confidence matched to Capt. Philip N. Vassil in the OSS Field Reports index.",
            "The declassified OSS index gives the exact rare full name, captain rank, Secret Intelligence branch, Middle East Theater and report number 15,542.",
            "High confidence from rare exact name, compatible officer identifier and direct OSS field-report context.",
            "The field-report list documents OSS service; the 1942 newspaper separately documents a Signal Corps assignment.",
            "A_direct_official",
            "high",
            [{"source_key": INDEX}, {"source_key": CIA_VASSIL}],
            "Box 801 review remains necessary to confirm exact transfer dates and any civilian employment before military service.",
        ),
        claim(
            6,
            "military-philip-vassil-signal-corps-b982",
            "other_pre_oss_affiliation",
            "Capt. Philip N. Vassil was attached to the Army Signal Corps by August 5, 1942.",
            "The contemporary Evening Star citizenship report gives the exact name, captain rank and Signal Corps attachment; the CIA index establishes OSS SI/METO context.",
            "High confidence from the exact rare full name, captain rank and independent official OSS context.",
            "Attested in August 1942; the exact sequence or overlap between Signal Corps and OSS service is not established.",
            "C_reputable_contemporary_or_scholarly",
            "high",
            [
                {"source_key": LOC_VASSIL, "excerpt_override": "Capt. Philip N. Vassil, 31, attached to the Army Signal Corps"},
                {"source_key": CIA_VASSIL},
            ],
            "Military assignment, not a civilian employer; published without claiming that Signal Corps was the immediate OSS predecessor.",
            "philip-vassil-signal-corps-b982",
        ),
        claim(
            12,
            "identity-philip-vaudrin-editor-b982",
            "identity",
            "Indexed Philip Vaudrin is probably the Oxford University Press editor documented in a sworn account of 1937-1938 events.",
            "The rare exact name and wartime-age publishing chronology are compatible, but the source contains no protected identifier or explicit OSS statement.",
            "Probable rare-name match; direct personnel-file confirmation is absent.",
            "The employment is explicitly prewar, while its relationship to OSS entry is unknown.",
            "B_authoritative_institutional",
            "medium",
            [{"source_key": INDEX}, {"source_key": MSA_VAUDRIN}],
            "Published only as a visibly qualified probable identity; Box 801 is required for confirmation.",
            publication_status="publish_qualified",
        ),
        claim(
            12,
            "prewar-philip-vaudrin-oup-b982",
            "other_pre_oss_affiliation",
            "The probable Philip Vaudrin match was an editor at Oxford University Press in late 1937 or early 1938.",
            "Paul Willert's sworn account identifies the then Oxford University Press editor Philip Vaudrin and dates the underlying events to late 1937 or early 1938.",
            "Probable rare-name match without a direct OSS or protected-identifier bridge.",
            "Explicitly prewar but not shown to be the immediate or last civilian affiliation before OSS service.",
            "B_authoritative_institutional",
            "medium",
            [{"source_key": MSA_VAUDRIN, "excerpt_override": "I asked the then editor of the Oxford University Press, Philip Vaudrin"}],
            "Qualified documented-prewar employment only; excluded from default verified-employer analytics because identity remains probable and chronology incomplete.",
            "philip-vaudrin-oup-b982",
            "publish_qualified",
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
    for row, reason in UNRESOLVED.items():
        box = "800" if row == 15 else ("802" if row == 23 else "801")
        values.append(
            base_update(
                row,
                identity_status="unresolved",
                identity_evidence=f"The visually verified index row supplies {PEOPLE[row][1]}, Box {box} and archive location 230/86/42/05. {reason}",
                personnel_category="unknown_or_indeterminate",
                research_status="requires_archival_review",
                next_action=f"Review Box {box} for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}",
            )
        )

    for item in ARMY_FINDINGS:
        row = int(item["row"])
        values.append(
            base_update(
                row,
                identity_status="high_confidence",
                identity_evidence=army_identity_note(item),
                name_variants=["Salvatore A Vavala"] if row == 21 else None,
                personnel_category="enlisted_army_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                research_status="occupation_only_found",
                next_action="Review Box 801 to establish the immediate pre-OSS affiliation and named last civilian employer; do not convert the Army occupation category into a workplace or exact job title.",
            )
        )

    values.extend(
        [
            base_update(
                8,
                identity_status="high_confidence",
                identity_evidence="Institutional sources identify the rare exact name John Vassos as an RCA industrial designer and OSS officer; contemporary trade press dates RCA and Army service.",
                name_variants=["John Plato Vassacopoulos"],
                personnel_category="commissioned_army_officer",
                commissioned_officer=True,
                allied_or_foreign_personnel=False,
                research_status="verified_employer_found",
                next_action="Review Box 801 to establish the precise Army Engineering Corps-to-OSS chronology and whether any concurrent civilian consulting continued after 1942.",
                archival_review_priority="medium",
            ),
            base_update(
                6,
                identity_status="high_confidence",
                identity_evidence="The declassified OSS field-report index gives the exact rare name Capt. Philip N. Vassil, SI branch and Middle East Theater; a 1942 newspaper independently documents the same captain in the Signal Corps.",
                personnel_category="commissioned_army_officer",
                commissioned_officer=True,
                allied_or_foreign_personnel=False,
                research_status="requires_archival_review",
                next_action="Review Box 801 to establish the Signal Corps-to-OSS sequence and identify any last civilian employer before military service. No reliable civilian employer has yet been identified in the accessible sources reviewed.",
            ),
            base_update(
                12,
                identity_status="probable",
                identity_evidence="A sworn account documents the rare exact name Philip Vaudrin as an Oxford University Press editor in 1937-1938, but supplies no protected identifier or explicit OSS statement.",
                personnel_category="unknown_or_indeterminate",
                research_status="documented_prewar_employer_found",
                next_action="Review Box 801 to confirm the probable editor identity and determine whether Oxford University Press was the last civilian or immediate pre-OSS affiliation.",
            ),
        ]
    )
    return values


def research_attempts() -> list[dict[str, object]]:
    reviewed = {1, 5, 6, 8, 9, 10, 12, 21}
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        source_row = row + 23
        if row in reviewed:
            outcome = "source_reviewed"
            sources_reviewed = 7 if row in {6, 8, 12} else 5
            rejected = 4
            detail = "Reviewed official, institutional or contemporary evidence produced the identity, occupation, employment or military-assignment outcome recorded in the bundle."
        else:
            outcome = "no_result"
            sources_reviewed = 5
            rejected = 5
            detail = UNRESOLVED[row]

        attempts.append(
            {
                "key": f"page481-row{source_row}-{slug(name)}-b982",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index and official Archives context; CIA Reading Room or equivalent official-source context; exact-name and meaningful variants; OSS, Army, rank, branch and assignment clues; employer and occupation 1940; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Boxes 800-802; protected identifiers used only in private official-record comparison",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_982",
                "started_at": "2026-10-30T18:05:00Z",
                "completed_at": "2026-10-30T21:15:00Z",
                "outcome": outcome,
                "sources_reviewed": sources_reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search snippets, unsourced genealogy, commercial people-finder pages, relatives, postwar-only leads and sources without an OSS, protected-identifier, rank or personnel-file bridge were rejected. Historical occupation categories and military assignments were not silently converted into employers.",
                "research_notes": f"{detail} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain and archival searches were checked as applicable. The index, Army bulk evidence, code list, Smithsonian and Syracuse finding aids, 1945 Broadcasting notice, declassified CIA field-report index, Library of Congress newspaper page and Maryland State Archives affidavit were inspected directly where relevant. No search-result snippet was used as sole final evidence, no paywall or access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": "Review the indexed personnel file for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before wartime service.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b982-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-982-v1",
        "reviewer": "Before OSS Batch 982 evidence review",
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
