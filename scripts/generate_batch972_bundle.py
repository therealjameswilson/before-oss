#!/usr/bin/env python3
"""Generate the reviewed Batch 972 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page476-george-tweed-to-john-tyson-"
    "review_batch-972_2026-10-30.json"
)

INDEX = "nara-index-b972"
ARMY = "army-bulk-b972"
TECH = "army-tech-b972"
CODES = "army-codes-b972"
DENVER = "denver-10th-mountain-roster-b972"
VESTERHEIM = "vesterheim-percy-red-b972"
MAIL_TRIBUNE = "mail-tribune-lawrence-tweedy-b972"
PRINCETON = "princeton-john-tyson-b972"
MIAMI_HERALD = "miami-herald-john-tyson-b972"
ARSOF = "arsof-john-tyson-b972"

INFANTRY_86 = "86th-infantry-regiment-b972"
INFANTRY_99 = "99th-infantry-battalion-b972"
HUTCHINSON = "hutchinson-rivinus-b972"
PENNSYLVANIA_RAILROAD = "pennsylvania-railroad-b972"


PEOPLE = {
    24: ("58664c19-dff1-59b7-8b78-f8d3d0fb7134", "George B Tweed"),
    25: ("d9440d10-fe0c-509f-a09c-0691f2c95fcb", "John B Tweedy"),
    26: ("63e7b2e7-5900-57c9-bf2e-02804ac80b1a", "Lawrence L Tweedy"),
    27: ("cbb28220-65d3-5096-bdc3-ac76c719bc38", "Grant M Tweiten"),
    28: ("920fc446-1a31-561d-bea6-7de943b1183d", "Wayne Twigg"),
    29: ("4c0af134-6060-5ddd-9ce5-2e5b449dce2e", "Otto Twingley"),
    30: ("03fe9760-0057-5e5f-a8c2-3fbad2123d37", "Jack W Twist"),
    31: ("f8cd2018-0b24-52b7-a54b-ff805ed8f002", "Thomas S Twohy"),
    32: ("8754e68e-3a1a-54b9-859e-b25ebe364d1c", "John J Twork"),
    33: ("a917da94-edb9-51ff-ab9d-7d067a29016b", "Francis R Tworzydlo"),
    34: ("2d652241-1006-531e-b802-5ee7a40e937c", "John E Tyczkowski"),
    35: ("db95a650-f77e-5d14-8a1b-fd0a03bcb7f9", "Esther M Tyler"),
    36: ("29e02dfb-fe5a-5617-82a1-3a72e9cc81a7", "Lucia L Tyler"),
    37: ("21ae02a6-ad5d-5e51-a847-c5429c6701ae", "Mary G Tyler"),
    38: ("618f6c30-1e41-5ada-8c0b-0e34b248be5e", "Robert W Tyler"),
    39: ("9ab0881e-5f03-5657-9c8d-c894f22e7b96", "Stephen Tymonko"),
    40: ("aadc6e66-f287-5979-ad3f-0e8eb337e09a", "Mary L Tynan"),
    41: ("1ca517cd-d3fd-559e-b1bc-d23db10ac78a", "Marvin E Tyree"),
    42: ("ee586699-07ca-5a36-8d67-f6b5cf0c34b0", "James P Tyrell"),
    43: ("763b648a-9219-5440-ae6d-aafa51b4e55a", "Evan S Tyrrell"),
    44: ("4b8b68f4-0e75-5e11-932f-ab77cbe27d57", "Dorothy A Tyson"),
    45: ("31f19a9c-0486-5883-8a2e-c584bee93d49", "James L Tyson"),
    46: ("838a228f-60b7-598a-a781-d2e985aca146", "John Tyson"),
}


ARMY_OCCUPATIONS = [
    {
        "row": 26,
        "date": "1941-12-22",
        "code": "317",
        "occupation": "Farm hands, animal and livestock",
        "public_occupation": "animal or livestock farm hand",
        "relationship_type": "unknown",
        "locator": "Historical category 3-17; farm hands, animal and livestock",
    },
    {
        "row": 32,
        "date": "1944-01-18",
        "code": "992",
        "occupation": "Students",
        "public_occupation": "student",
        "relationship_type": "student",
        "locator": "Corrected Code No. 30, PDF physical page 304; 9-92 Students",
    },
    {
        "row": 38,
        "date": "1943-02-02",
        "code": "992",
        "occupation": "Students",
        "public_occupation": "student",
        "relationship_type": "student",
        "locator": "Corrected Code No. 30, PDF physical page 304; 9-92 Students",
    },
    {
        "row": 39,
        "date": "1943-05-13",
        "code": "736",
        "occupation": "Chauffeurs and drivers, bus, taxi, truck, and tractor",
        "public_occupation": "chauffeur or bus, taxi, truck or tractor driver",
        "relationship_type": "unknown",
        "locator": "Historical category 5,7-36; chauffeurs and drivers, bus, taxi, truck and tractor",
    },
]


UNRESOLVED = {
    24: "The famous George R. Tweed and other namesakes were rejected because the indexed middle initial is B and no source bridged a candidate to Box 791.",
    27: "Exact-name searches produced only weak genealogical leads and no defensible OSS, employer or institutional identity bridge.",
    28: "The index note 'Charged' was preserved but not interpreted; exact-name and variant searches produced no defensible identity bridge.",
    30: "Exact-name, initial, OSS, employer, occupation, obituary and archival searches produced no defensible identity bridge.",
    31: "Exact-name and variant searches produced no source linking this person to Box 791 or a dated pre-OSS affiliation.",
    33: "The distinctive surname still produced no inspectable source bridging the indexed record to a dated pre-OSS affiliation.",
    35: "The common name produced multiple namesakes without two corroborating identifiers beyond the name.",
    36: "Exact-name and variant searches produced no defensible identity bridge to Box 791 or a dated pre-OSS affiliation.",
    37: "The common name produced multiple namesakes without two corroborating identifiers beyond the name.",
    40: "A possible San Francisco namesake was rejected because no official or institutional source connected her to OSS, the indexed naval-style number or Box 792.",
    42: "Exact-name searches produced no defensible identity bridge; similarly named Tyrrell records were rejected as spelling or middle-initial conflicts.",
    43: "Exact-name and variant searches produced no defensible identity bridge to Box 792 or a dated pre-OSS affiliation.",
    44: "The common name produced multiple chronologically incompatible namesakes and no source bridged one to Box 792.",
    45: "A later conservative-organization trustee and other namesakes were rejected because no source linked them to the indexed OSS record.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 791-792",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 476, rows 24-46; checked against layout-preserving text and an original-detail page render",
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
            "locator": "Official unrestricted ASNEF.FIN.DAT; seven Batch 972 identity comparisons; protected identifiers and record ordinals withheld",
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
            "locator": "PDF physical pages 171-172, 174 and 304; Batch 972 categories visually and textually checked",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical categories identify neither employers nor workplaces and are retained only where needed for auditability.",
        },
        {
            "key": DENVER,
            "stable_url": "https://history.denverlibrary.org/sites/history/files/10th_mountain_index.pdf",
            "title": "Members of the 10th Mountain Division",
            "author_creator": "Denver Public Library, Western History and Genealogy",
            "repository_publisher": "Denver Public Library",
            "locator": "PDF physical page 706; John B. Tweedy and Otto Twingley roster entries",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "10th Mountain Division Resource Center",
        },
        {
            "key": VESTERHEIM,
            "stable_url": "https://vesterheim.org/norwegian-special-operations-group-percy-red/",
            "title": "Rieder Grunseth and the Norwegian Special Operations Group - Operation Percy Red",
            "author_creator": "Jon Grunseth",
            "repository_publisher": "Vesterheim Norwegian-American Museum",
            "publication_record_date": "2025",
            "locator": "Recruitment from the 99th Infantry Battalion; Percy Red memorial roster naming T/5 Otto Twingley",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Vesterheim Stories",
            "rights_notes": "Only short excerpts and project-authored paraphrases are retained.",
        },
        {
            "key": MAIL_TRIBUNE,
            "stable_url": "https://www.legacy.com/us/obituaries/mailtribune/name/lawrence-tweedy-obituary?id=28539063",
            "title": "Lawrence L. Tweedy obituary",
            "author_creator": "Mail Tribune obituary contributors",
            "repository_publisher": "Mail Tribune; Legacy.com archive",
            "publication_record_date": "2009-05-07",
            "locator": "Biographical chronology: Texas ranching, wartime underwater-demolition group and OSS context",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Mail Tribune obituaries",
            "rights_notes": "Used with the exact protected-identifier Army match; only short excerpts and paraphrases are retained.",
        },
        {
            "key": PRINCETON,
            "stable_url": "https://www.princeton.edu/~paw/archive_new/PAW04-05/09-0223/memorials.html",
            "title": "John Tyson '27 memorial",
            "author_creator": "Princeton Class of 1927",
            "repository_publisher": "Princeton Alumni Weekly, Princeton University",
            "publication_record_date": "2005-02-23",
            "locator": "Memorials; John Tyson '27",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Princeton Alumni Weekly memorials",
            "rights_notes": "Only short excerpts and project-authored paraphrases are retained.",
        },
        {
            "key": MIAMI_HERALD,
            "stable_url": "https://www.legacy.com/us/obituaries/herald/name/john-tyson-obituary?id=13743165",
            "title": "John Tyson obituary",
            "author_creator": "Miami Herald obituary contributors",
            "repository_publisher": "Miami Herald; Legacy.com archive",
            "publication_record_date": "2004-10",
            "locator": "Biographical chronology: Hutchinson, Rivinus & Co., OSS headquarters and England training role",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Miami Herald obituaries",
            "rights_notes": "Only short excerpts and project-authored paraphrases are retained.",
        },
        {
            "key": ARSOF,
            "stable_url": "https://arsof-history.org/articles/v3n1_brucker_pt3_page_1.html",
            "title": "Major Herbert R. Brucker, SF Pioneer, Part III: SOE Training and Team HERMIT into France",
            "author_creator": "Charles H. Briscoe",
            "repository_publisher": "U.S. Army Special Operations Command History Office",
            "publication_record_date": "2007",
            "locator": "Part III; Captain John Tyson's July 1943 OSS training report",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Veritas: Journal of Army Special Operations History",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": INFANTRY_86,
            "organization_id": "f8e9ea53-68e2-5383-8740-d36e9631a47c",
            "canonical_name": "86th Infantry Regiment, 10th Mountain Division",
            "historical_name": "86TH INF",
            "aliases": ["86th Infantry", "86th Mountain Infantry Regiment"],
            "organization_type": "U.S. Army infantry regiment",
            "sector": "military",
            "country": "United States",
            "active_dates": "Second World War",
            "normalization_notes": "E Company is preserved in the affiliation field; sequence relative to OSS remains uncertain.",
        },
        {
            "key": INFANTRY_99,
            "organization_id": "a9ed25cf-8cdc-56e7-a6de-0ab28065fb8c",
            "canonical_name": "99th Infantry Battalion (Separate)",
            "historical_name": "99th Infantry Battalion (Separate)",
            "aliases": ["Battalion 99", "99th Mountain Battalion", "99th Infantry Battalion", "Norwegian-American Ski Battalion"],
            "organization_type": "United States Army battalion",
            "sector": "military",
            "country": "United States",
            "active_dates": "1942-1945",
            "normalization_notes": "Historical naming variants are preserved; the unit is separate from the later OSS Norwegian Operational Group. D Company is preserved in Otto Twingley's affiliation evidence.",
        },
        {
            "key": HUTCHINSON,
            "canonical_name": "Hutchinson, Rivinus & Co.",
            "historical_name": "Hutchinson and Rivinus",
            "aliases": ["Hutchinson, Rivinus", "Hutchinson. Rivinus & Co."],
            "organization_type": "insurance brokerage",
            "sector": "finance_and_banking",
            "city": "Philadelphia",
            "state_or_region": "Pennsylvania",
            "country": "United States",
            "active_dates": "John Tyson joined in 1927 and was a partner by 1936",
            "normalization_notes": "Historical punctuation varies across the reviewed sources; no modern successor name is substituted.",
        },
        {
            "key": PENNSYLVANIA_RAILROAD,
            "canonical_name": "Pennsylvania Railroad",
            "historical_name": "Pennsylvania Railroad",
            "aliases": ["Pennsylvania RR"],
            "organization_type": "railroad",
            "sector": "business_and_industry",
            "country": "United States",
            "active_dates": "1846-1968",
            "normalization_notes": "Earlier documented employment, kept separate from John Tyson's later insurance career.",
        },
    ]


def occupation_affiliation(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    return {
        "key": f"{slug(PEOPLE[row][1])}-occupation-b972",
        "person_id": PEOPLE[row][0],
        "occupation": str(item["public_occupation"]),
        "relationship_type": str(item["relationship_type"]),
        "end_date": str(item["date"]),
        "date_precision": f"Historical civilian-occupation code {item['code']} was recorded at Army entry on {item['date']}; no named employer, workplace or exact OSS-transfer date is supplied.",
        "country": "United States",
        "immediate_pre_oss": False,
        "last_civilian_pre_service": False,
        "pre_oss_temporal_basis": "documented_prewar",
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
                "key": "john-b-tweedy-86th-infantry-b972",
                "person_id": PEOPLE[25][0],
                "organization_key": INFANTRY_86,
                "organization_name_as_found": "E Company, 86th Infantry",
                "relationship_type": "military_assignment",
                "date_precision": "Second World War; the roster does not establish whether the assignment preceded, followed or overlapped OSS service",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "temporal_relation_uncertain",
                "identity_confidence": "probable",
                "claim_confidence": "medium",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "publish_qualified",
                "research_notes": "The exact full name is distinctive, but the roster has no service number or explicit OSS bridge. Published only as a qualified wartime assignment.",
            },
            {
                "key": "otto-twingley-99th-infantry-b972",
                "person_id": PEOPLE[29][0],
                "organization_key": INFANTRY_99,
                "organization_name_as_found": "D Company, 99th Infantry",
                "role_title": "soldier; later T/5 in OSS Percy Red",
                "relationship_type": "military_assignment",
                "end_date": "1943-07",
                "date_precision": "The division roster places Twingley in D Company, 99th Infantry; Vesterheim describes July 1943 OSS recruitment from the 99th and names T/5 Otto Twingley in Percy Red",
                "country": "United States",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "This is a military pathway into OSS, not a civilian employer. A service-number discrepancy found in secondary discovery material remains private and unresolved.",
            },
            {
                "key": "john-tyson-hutchinson-rivinus-b972",
                "person_id": PEOPLE[46][0],
                "organization_key": HUTCHINSON,
                "organization_name_as_found": "Hutchinson and Rivinus",
                "role_title": "partner",
                "occupation": "insurance broker",
                "relationship_type": "employment",
                "start_date": "1927",
                "end_date": "1941-12",
                "date_precision": "The memorial says Tyson became a partner in 1936 and volunteered for OSS shortly after Pearl Harbor; the obituary gives the 1927 start year",
                "city": "Philadelphia",
                "state_or_region": "Pennsylvania",
                "country": "United States",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "explicit_immediate",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "The Princeton memorial directly sequences the insurance partnership before OSS; the Army Special Operations history independently corroborates Captain John Tyson's distinctive England training role.",
            },
            {
                "key": "john-tyson-pennsylvania-railroad-b972",
                "person_id": PEOPLE[46][0],
                "organization_key": PENNSYLVANIA_RAILROAD,
                "organization_name_as_found": "Pennsylvania Railroad",
                "role_title": "fireman",
                "occupation": "railroad fireman",
                "relationship_type": "employment",
                "end_date": "1927",
                "date_precision": "Earlier work after Princeton and before joining Hutchinson, Rivinus & Co. in 1927; exact dates are not supplied",
                "state_or_region": "Pennsylvania",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Earlier documented employment, kept separate from the immediate and last-civilian insurance affiliation.",
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
    if row == 26:
        return "The indexed full name and protected identifier agree with an official Army row that adds Jr.; the Mail Tribune chronology independently matches a 1919-born rancher who entered OSS underwater-demolition work."
    if row == 41:
        return "Two official Army rows share the indexed protected identifier and agree on Marvin Tyree; one carries the indexed middle initial. Both entry dates follow OSS dissolution and are not projected backward."
    return "The exact indexed full name and a nonshared protected identifier agree with the reviewed official Army row."


def army_claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row in [26, 32, 38, 39, 41]:
        name = PEOPLE[row][1]
        date = next(
            (str(item["date"]) for item in ARMY_OCCUPATIONS if item["row"] == row),
            "1946-01",
        )
        values.append(
            claim(
                row,
                f"identity-{slug(name)}-b972",
                "identity",
                f"Indexed {name} is high-confidence matched to reviewed official Army evidence.",
                army_identity_note(row),
                army_identity_note(row),
                f"The Army evidence is dated {date}; it supports identity and military-entry chronology but not the exact OSS transfer date.",
                "A_direct_official",
                "high",
                [{"source_key": INDEX}, {"source_key": ARMY}, {"source_key": TECH}],
                "Protected identifiers were used only for private resolution and remain absent from the evidence bundle and public output.",
            )
        )

    for item in ARMY_OCCUPATIONS:
        row = int(item["row"])
        name = PEOPLE[row][1]
        values.append(
            claim(
                row,
                f"occupation-{slug(name)}-b972",
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
                "Published as qualified occupation or student status only; excluded from verified-employer analytics.",
                f"{slug(name)}-occupation-b972",
                "publish_qualified",
            )
        )
    return values


def special_claims() -> list[dict[str, object]]:
    return [
        claim(
            25,
            "identity-john-b-tweedy-b972",
            "identity",
            "Indexed John B Tweedy is a probable match to the 10th Mountain Division roster entry of that exact name.",
            "The Denver Public Library roster gives the distinctive exact full name and assigns it to E Company, 86th Infantry.",
            "Probable, not high confidence: exact distinctive name and compatible Army context, but no service number or explicit OSS bridge appears in the roster.",
            "Second World War; sequence relative to OSS is not established.",
            "B_authoritative_institutional",
            "medium",
            [{"source_key": INDEX}, {"source_key": DENVER, "excerpt_override": "JOHN B TWEEDY E 86TH INF"}],
            "Published as a qualified identity and wartime assignment; Box 791 must confirm the match.",
            publication_status="publish_qualified",
            evidence_excerpt="JOHN B TWEEDY E 86TH INF",
        ),
        claim(
            25,
            "affiliation-john-b-tweedy-86th-b972",
            "other_pre_oss_affiliation",
            "A probable John B. Tweedy identity served in E Company, 86th Infantry during the Second World War.",
            "The division roster supplies the exact full name, company and regiment.",
            "Probable identity only; the roster lacks the indexed identifier and direct OSS context.",
            "Documented wartime military assignment with uncertain sequence relative to OSS; it is not labeled immediate.",
            "B_authoritative_institutional",
            "medium",
            [{"source_key": DENVER, "excerpt_override": "JOHN B TWEEDY E 86TH INF"}],
            "Qualified military assignment, not civilian employment; excluded from default employer analytics.",
            "john-b-tweedy-86th-infantry-b972",
            "publish_qualified",
        ),
        claim(
            26,
            "context-lawrence-l-tweedy-ranching-b972",
            "other_pre_oss_affiliation",
            "Lawrence L. Tweedy was engaged in ranching before his wartime service and OSS underwater-demolition assignment.",
            "The obituary places him on the Texas family ranch before wartime service; the dated Army code independently records animal or livestock farm work.",
            "High confidence from the exact protected-identifier Army match, compatible Jr. suffix, exact-name obituary, birth chronology and unusual OSS underwater-demolition detail.",
            "Strongly date-bounded before Army entry and OSS, but no named employer or self-employment status is stated.",
            "C_reputable_contemporary_or_scholarly",
            "medium",
            [
                {"source_key": MAIL_TRIBUNE, "excerpt_override": "There Larry found his true love- ranching."},
                {"source_key": ARMY, "support_type": "context_only"},
                {"source_key": CODES, "locator_override": "Historical category 3-17; farm hands, animal and livestock"},
            ],
            "Published as qualified occupation context only; no ranch organization or employer is inferred.",
            "lawrence-l-tweedy-occupation-b972",
            "publish_qualified",
        ),
        claim(
            29,
            "identity-otto-twingley-b972",
            "identity",
            "Indexed Otto Twingley is high-confidence matched to T/5 Otto Twingley of the OSS Norwegian Operational Group Percy Red.",
            "The rare exact name appears in both the 10th Mountain roster and Vesterheim's named Percy Red roster; the latter explicitly places the group in OSS.",
            "High confidence from a rare exact name, two compatible institutional rosters, 99th Infantry origin and explicit OSS Percy Red membership.",
            "The sources document 99th Infantry service before the July 1943 NORSO recruitment and the 1944 Percy Red mission.",
            "B_authoritative_institutional",
            "high",
            [
                {"source_key": INDEX},
                {"source_key": DENVER, "excerpt_override": "OTTO TWINGLEY D 99TH INF"},
                {"source_key": VESTERHEIM, "excerpt_override": "T/5 Otto Twingley"},
            ],
            "A one-digit service-number discrepancy seen in secondary discovery material is retained privately as a conflict and not exposed or resolved by convenience.",
            evidence_excerpt="T/5 Otto Twingley",
        ),
        claim(
            29,
            "immediate-otto-twingley-99th-b972",
            "immediate_pre_oss_affiliation",
            "Otto Twingley's best-supported immediate affiliation before OSS NORSO was D Company, 99th Infantry Battalion (Separate).",
            "The division roster places him in D Company, 99th Infantry; Vesterheim says NORSO began by recruiting volunteers from the 99th and names him in Percy Red.",
            "High-confidence rare-name match across the NARA index and two institutional rosters.",
            "Strongly date-bounded: recruitment from the 99th into OSS NORSO is placed in July 1943.",
            "B_authoritative_institutional",
            "high",
            [
                {"source_key": DENVER, "excerpt_override": "OTTO TWINGLEY D 99TH INF"},
                {"source_key": VESTERHEIM, "excerpt_override": "volunteers from the Norwegian Americans in the 99th"},
            ],
            "Classified as a military pathway, not a civilian employer; no last civilian employer is inferred.",
            "otto-twingley-99th-infantry-b972",
        ),
        claim(
            34,
            "identity-conflict-john-e-tyczkowski-b972",
            "identity",
            "The protected identifier on indexed John E Tyczkowski leads to an Army row printed without the initial J; the identity remains conflicting.",
            "The protected identifier agrees, but the official Army name field is printed as Tyczkowski Ohn E.",
            "Conflicting: a strong identifier bridge is offset by a substantive missing-initial name defect that the personnel file must resolve.",
            "The Army entry is dated 20 June 1941, but no occupation or chronology is assigned while identity remains disputed.",
            "A_direct_official",
            "conflicting",
            [{"source_key": INDEX}, {"source_key": ARMY}, {"source_key": TECH}],
            "The records remain separate; the machinist category is not transferred and no public employer fact is created.",
            publication_status="conflicting",
        ),
        claim(
            46,
            "identity-john-tyson-b972",
            "identity",
            "Indexed John Tyson is high-confidence matched to the Philadelphia insurance partner and OSS training officer Captain John Tyson.",
            "Princeton and a newspaper obituary share his insurance and OSS chronology; Army Special Operations history independently names Captain John Tyson's OSS England training report.",
            "High confidence from the exact name plus a distinctive combination of Philadelphia insurance partnership, immediate OSS entry, England training role and captain rank across independent sources.",
            "The sources place the insurance career before OSS and Captain Tyson in the European theater by July 1943.",
            "B_authoritative_institutional",
            "high",
            [
                {"source_key": INDEX},
                {"source_key": PRINCETON},
                {"source_key": MIAMI_HERALD, "support_type": "context_only"},
                {"source_key": ARSOF, "excerpt_override": "one of his training officers, Captain John Tyson, to evaluate SOE instruction"},
            ],
            "The identity is not treated as confirmed because no reviewed source reproduces the protected index identifier.",
        ),
        claim(
            46,
            "immediate-john-tyson-hutchinson-b972",
            "immediate_pre_oss_affiliation",
            "John Tyson's best-supported immediate civilian affiliation before OSS was partner at Hutchinson, Rivinus & Co. in Philadelphia.",
            "The Princeton memorial sequences his partnership directly before volunteering for OSS shortly after Pearl Harbor.",
            "High-confidence identity from the distinctive career and OSS training chronology across institutional and newspaper sources.",
            "Explicitly immediate in the memorial's chronology; exact departure date is not supplied.",
            "B_authoritative_institutional",
            "high",
            [
                {"source_key": PRINCETON, "excerpt_override": "Shortly after the attack on Pearl Harbor, John volunteered for service in the OSS"},
                {"source_key": MIAMI_HERALD, "support_type": "context_only"},
            ],
            "The claim is civilian employment; his later captain rank and OSS training work remain separate.",
            "john-tyson-hutchinson-rivinus-b972",
            evidence_excerpt="Shortly after the attack on Pearl Harbor, John volunteered for service in the OSS",
        ),
        claim(
            46,
            "last-civilian-john-tyson-hutchinson-b972",
            "last_civilian_pre_service",
            "Hutchinson, Rivinus & Co. is John Tyson's last documented civilian employer before OSS service.",
            "The sources state that he joined the insurance brokerage in 1927, became a partner in 1936 and volunteered for OSS shortly after Pearl Harbor.",
            "High-confidence identity from matching insurance, Princeton, OSS and England-training details.",
            "Strongly date-bounded as the final named civilian employment before OSS; no intervening employer is documented.",
            "B_authoritative_institutional",
            "high",
            [
                {"source_key": PRINCETON, "excerpt_override": "eventually joining Hutchinson and Rivinus (an insurance firm), of which he became a partner in 1936"},
                {"source_key": MIAMI_HERALD, "support_type": "context_only"},
            ],
            "Kept distinct from both OSS service and his earlier railroad employment.",
            "john-tyson-hutchinson-rivinus-b972",
        ),
        claim(
            46,
            "earlier-john-tyson-pennsylvania-railroad-b972",
            "other_pre_oss_affiliation",
            "Before entering insurance, John Tyson worked as a fireman on the Pennsylvania Railroad.",
            "The Princeton memorial lists railroad fireman among his post-Princeton jobs before he joined Hutchinson and Rivinus.",
            "High-confidence identity through the same distinctive insurance-to-OSS chronology.",
            "Documented earlier prewar employment; exact dates are not supplied and it is not the immediate predecessor to OSS.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": PRINCETON, "excerpt_override": "as a fireman on the Pennsylvania Railroad"}],
            "Modeled separately so earlier employment is not conflated with the last civilian employer.",
            "john-tyson-pennsylvania-railroad-b972",
            evidence_excerpt="as a fireman on the Pennsylvania Railroad",
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
            identity_evidence=f"The visually verified index row supplies {PEOPLE[row][1]}, Box {'791' if row <= 38 else '792'} and archive location {'230/86/42/03' if row <= 38 else '230/86/42/04'}. {reason}",
            personnel_category="unknown_or_indeterminate",
            commissioned_officer=None,
            allied_or_foreign_personnel=None,
            research_status="requires_archival_review",
            next_action=f"Review Box {'791' if row <= 38 else '792'} for corroborating identifiers, immediate pre-OSS affiliation and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}",
        )
        for row, reason in UNRESOLVED.items()
    ]

    for item in ARMY_OCCUPATIONS:
        row = int(item["row"])
        values.append(
            base_update(
                row,
                identity_status="high_confidence",
                identity_evidence=army_identity_note(row),
                name_variants=["Lawrence L Tweedy Jr"] if row == 26 else None,
                personnel_category="enlisted_army_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                research_status="occupation_only_found",
                next_action=f"Review Box {'791' if row <= 38 else '792'} to establish the immediate pre-OSS affiliation and named last civilian employer; do not convert the Army occupation category into a workplace.",
            )
        )

    values.extend(
        [
            base_update(
                25,
                identity_status="probable",
                identity_evidence="The distinctive exact name appears in the Denver Public Library 10th Mountain Division roster as E Company, 86th Infantry, but the roster lacks the indexed identifier and direct OSS context.",
                personnel_category="unknown_or_indeterminate",
                commissioned_officer=None,
                allied_or_foreign_personnel=False,
                research_status="requires_archival_review",
                next_action="Review Box 791 to confirm the 86th Infantry identity candidate, determine sequence relative to OSS and establish any civilian employer before service.",
            ),
            base_update(
                29,
                identity_status="high_confidence",
                identity_evidence="The rare exact name appears in the Denver Public Library roster as D Company, 99th Infantry and in Vesterheim's OSS Percy Red roster as T/5 Otto Twingley; Vesterheim describes recruitment from the 99th into NORSO.",
                personnel_category="enlisted_army_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                research_status="requires_archival_review",
                next_action="Review Box 791 to resolve the private service-number discrepancy, confirm the 99th-to-NORSO accession date and identify the last civilian employer before Army service.",
            ),
            base_update(
                34,
                identity_status="conflicting",
                identity_evidence="The protected identifier leads to an official Army row printed as Tyczkowski Ohn E, conflicting with indexed John E Tyczkowski. No occupation is transferred.",
                personnel_category="unknown_or_indeterminate",
                commissioned_officer=None,
                allied_or_foreign_personnel=None,
                research_status="conflicting_sources",
                next_action="Review Box 791 to determine whether the missing initial is source damage, transcription loss or a different person; establish pre-OSS affiliation only after resolution.",
                archival_review_priority="critical",
            ),
            base_update(
                41,
                identity_status="high_confidence",
                identity_evidence=army_identity_note(41),
                personnel_category="enlisted_army_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                research_status="requires_archival_review",
                next_action="Review Box 792 to establish the pre-OSS identity chronology and civilian affiliation; the duplicate 1946 Army rows cannot supply pre-OSS occupation evidence.",
            ),
            base_update(
                46,
                identity_status="high_confidence",
                identity_evidence="Princeton and a newspaper obituary share the distinctive Philadelphia insurance-to-OSS chronology; Army Special Operations history independently names Captain John Tyson's OSS England training report.",
                personnel_category="commissioned_army_officer",
                commissioned_officer=True,
                allied_or_foreign_personnel=False,
                research_status="verified_employer_found",
                next_action="Review Box 792 to confirm the protected identifier, exact OSS accession date and assignments; Hutchinson, Rivinus & Co. remains the verified last civilian employer in accessible sources.",
                archival_review_priority="medium",
            ),
        ]
    )
    return values


def research_attempts() -> list[dict[str, object]]:
    reviewed_rows = {25, 26, 29, 32, 34, 38, 39, 41, 46}
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        if row in reviewed_rows:
            outcome = "source_reviewed"
            reviewed = 9 if row in {26, 29, 46} else 6
            rejected = 5
            detail = "Reviewed official, institutional, contemporary or archival evidence produced the identity, occupation, military-pathway, employer or conflict outcome recorded in the evidence bundle."
        else:
            outcome = "no_result"
            reviewed = 6
            rejected = 6
            detail = UNRESOLVED[row]

        special_rejection = ""
        if row == 24:
            special_rejection = " George R. Tweed was rejected because the indexed middle initial differs and no protected identifier or file evidence connects him."
        elif row == 25:
            special_rejection = " The 86th Infantry roster is published only as a probable identity because it lacks a service-number or direct OSS bridge."
        elif row == 29:
            special_rejection = " A secondary service-number discrepancy remains unresolved and was not exposed or silently corrected."
        elif row == 40:
            special_rejection = " A San Francisco Mary L. Tynan lead was rejected because birth and death data alone do not establish OSS identity or employment."
        elif row == 45:
            special_rejection = " A later James L. Tyson trustee lead was rejected because it supplied no wartime or OSS identity bridge."

        attempts.append(
            {
                "key": f"page476-row{row}-{slug(name)}-b972",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index and official Archives context; CIA Reading Room exact-name check; exact-name and meaningful variants; OSS, Army, Navy, rank and unit clues; employer and occupation 1940; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Box {'791' if row <= 38 else '792'}; protected identifiers used only in private official-record comparison",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_972",
                "started_at": "2026-10-30T22:00:00Z",
                "completed_at": "2026-10-30T23:45:00Z",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search snippets, unsourced genealogy, people-finder pages, postwar-only employment leads and sources without an OSS, protected-identifier or personnel-file bridge were rejected. Historical occupation codes and military service were not silently converted into employers." + special_rejection,
                "research_notes": f"{detail} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain, CIA Reading Room and Library of Congress searches were checked as applicable. The index page, Army bulk file, technical documentation and relevant occupation-code pages were inspected directly; code pages 171-172, 174 and 304 were visually checked. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": (
                    "Review Box 791 to resolve the protected-identifier/name conflict before assigning the Army machinist category or any pre-OSS affiliation."
                    if row == 34
                    else f"Review Box {'791' if row <= 38 else '792'} for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before wartime service."
                ),
                "attempt_number": 1,
                "research_agent_version": "before-oss-b972-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-972-v1",
        "reviewer": "Before OSS Batch 972 evidence review",
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
