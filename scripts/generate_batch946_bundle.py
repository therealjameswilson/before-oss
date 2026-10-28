#!/usr/bin/env python3
"""Generate the reviewed Batch 946 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page463-henry-w-terrett-to-erika-teutsch-"
    "review_batch-946_2026-10-28.json"
)

INDEX = "nara-index-b946"
ARMY = "army-bulk-b946"
TECH = "army-tech-b946"
CODES = "army-codes-b946"
SWARTHMORE_PROFILE = "swarthmore-profile-teutsch-b946"
SWARTHMORE_MEMORIAL = "swarthmore-memorial-teutsch-b946"
OSSOG = "ossog-personnel-b946"
VA_TERZEN = "va-cemetery-terzen-b946"

SWARTHMORE = "swarthmore-college-b946"


PEOPLE = {
    24: ("aebe55ca-6471-5529-b9b9-ce7502b1716d", "Henry W Terrett"),
    25: ("a8575c75-1395-56ae-aa75-e3682156d30e", "Walter L Terrill"),
    26: ("6db6bbce-c97a-5977-8231-5829a9fbef86", "Rocco E Terrone"),
    27: ("1c07bfe7-a8a8-5284-b4b4-d215442105c0", "James R Terry"),
    28: ("c573aa1d-646b-57bb-ad7c-53ec81567d04", "Rollin E Terry"),
    29: ("57e4222f-297e-5302-91fc-d1d74bb686cf", "Harry J Terwilliger"),
    30: ("398cf0e8-557c-5b10-b853-a764d32cc4be", "Alexander J Terzaghi"),
    31: ("20c04d14-0e5d-589d-ad9d-98992fae8d8e", "Adrian Terzian"),
    32: ("b7be437e-2360-530e-bdaa-151f5216328f", "Fred Teschner"),
    33: ("deba6c6c-275b-5696-8b18-72647305e4df", "Edward Tesdorff"),
    34: ("845073eb-17ca-51a2-89fd-3cd4d606e5f9", "William G Tesi"),
    35: ("b14d12d5-bc9c-5762-bfce-36ec79eccf78", "John R Teske"),
    36: ("59c899f0-ea9b-5d4f-9947-415764b54940", "John R Teske"),
    37: ("cc4b077b-540a-55a1-9008-a89c84d07356", "Joseph J Tesoriere"),
    38: ("f49a8bb6-17bd-57cc-a6b5-8ca0bead42f3", "Emil Tessari"),
    39: ("e3e63998-895a-5043-8aff-584c6b2ee42e", "John Tessitore"),
    40: ("bf398b17-a0bb-593a-b1b2-39602a310499", "Frank C Test"),
    41: ("58ced547-179f-5c8d-b880-480fa680ddfc", "Janet Testerman"),
    42: ("ba92e4c7-4f0f-57c4-a9a5-1b8a7df2b1c8", "* Testi"),
    43: ("dc16580f-e943-5e38-a78c-e1b02a7985c0", "Joseph Testo"),
    44: ("26b0c21c-c39d-5c2d-b1ac-1cc2ca6c5a7f", "Leo P Tetrault"),
    45: ("c27c77fc-f69a-562d-912b-e3df7f1547df", "Leo P Tetrealt"),
    46: ("436a8686-43bb-5463-a073-1bd851b02d04", "Erika Teutsch"),
}

PRIOR_WALTER_TERRELL = "f238d457-78c8-5960-985c-b84c7b7586e0"


ARMY_OCCUPATIONS = [
    {"row": 26, "date": "1943-12-08", "code": "024", "occupation": "Musicians and teachers of music", "public_occupation": "musician or music teacher", "locator": "PDF physical page 171; historical category 0-24"},
    {"row": 27, "date": "1944-01-18", "code": "992", "occupation": "Students", "public_occupation": "student", "locator": "PDF physical page 304; amended historical category 9-92", "relationship": "student"},
    {"row": 28, "date": "1942-07-28", "code": "108", "occupation": "Insurance clerks, n.e.c.", "public_occupation": "insurance clerk, not elsewhere classified", "locator": "PDF physical page 171; historical category 1-08"},
    {"row": 30, "date": "1941-04-19", "code": "105", "occupation": "Clerks, general office", "public_occupation": "general office clerk", "locator": "PDF physical page 171; historical category 1-05"},
    {"row": 31, "date": "1943-07-29", "code": "685", "occupation": "Welders and flame cutters", "public_occupation": "welder or flame cutter", "locator": "PDF physical page 174; historical category 6-85"},
    {"row": 34, "date": "1942-11-21", "code": "732", "occupation": "Construction occupations, n.e.c.", "public_occupation": "semiskilled construction occupation, not elsewhere classified", "locator": "PDF physical page 174; historical category 7-32"},
    {"row": 37, "date": "1942-12-05", "code": "717", "occupation": "Pattern and model makers, except paper", "public_occupation": "pattern or model maker, except paper", "locator": "PDF physical page 174; historical category 7-17"},
    {"row": 39, "date": "1941-09-05", "code": "619", "occupation": "Occupations in manufacture of textiles, n.e.c.", "public_occupation": "semiskilled textile-manufacturing occupation, not elsewhere classified", "locator": "PDF physical page 173; historical category 6-19"},
    {"row": 40, "date": "1942-12-15", "code": "685", "occupation": "Welders and flame cutters", "public_occupation": "welder or flame cutter", "locator": "PDF physical page 174; historical category 6-85"},
    {"row": 43, "date": "1942-10-02", "code": "992", "occupation": "Students", "public_occupation": "student", "locator": "PDF physical page 304; amended historical category 9-92", "relationship": "student"},
    {"row": 45, "date": "1943-01-19", "code": "138", "occupation": "Stock clerks", "public_occupation": "stock clerk", "locator": "PDF physical page 171; historical category 1-38"},
]


UNRESOLVED = {
    29: "A same-name electrical-business lead lacked the protected identifier, a middle-initial bridge and any OSS or Box 770 connection, so it was rejected.",
    32: "Exact-name searches produced modern people-finder records and genealogy leads only; none established this protected-identifier person, OSS service or a pre-OSS affiliation.",
    33: "A Danish estate-owner namesake was not connected to OSS, Box 770 or any corroborating identifier; no defensible identity or employment match was made.",
    38: "A genealogy lead supplied a possible birth and death span but no OSS, Box 770 or employment bridge, so it was not assigned.",
    41: "Exact-name, obituary, institutional and OSS searches produced no reliable identity or pre-OSS affiliation bridge.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 769-770",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 463, rows 24-46; checked against layout-preserving text and a 300 dpi page render",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. The two John R. Teske rows, the Tetrault/Tetrealt rows and the adjacent Terrell/Terrill spellings remain unmerged. Full protected identifiers remain private. Marcelen J. Tezak at page 464 row 1 was visually checked as the next boundary.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; twelve reviewed Batch 946 candidates; protected identifiers withheld",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "No raw bulk row or full protected identifier is retained in public assets. Eleven identities were accepted; Henry W./M. Terrett remains an explicit middle-initial conflict. Historical occupation codes identify neither employers nor workplaces.",
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
            "access_date": "2026-10-28",
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
            "locator": "PDF physical pages 171, 173-174 and 304; reviewed historical categories 0-24, 1-05, 1-08, 1-38, 6-19, 6-85, 7-17, 7-32 and 9-92",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "All relevant pages were rendered and visually inspected. Students is status, not employment. Other historical labels are qualified and never converted into named employers.",
        },
        {
            "key": SWARTHMORE_PROFILE,
            "stable_url": "https://archive.swarthmore.edu/bulletin_2008-2014/wp-content/archived_issues_pdf/Bulletin_2002_03.pdf?__raw=1",
            "archival_identifier": "Swarthmore College Bulletin, March 2002",
            "title": "Living in the Present: At 78, Erika Teutsch '44 Still Works Full Time to Make a Difference for People",
            "author_creator": "Jeffrey Lott",
            "repository_publisher": "Swarthmore College",
            "publication_record_date": "2002-03",
            "locator": "Printed page 52; PDF physical page 46",
            "access_date": "2026-10-28",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Swarthmore College Bulletin",
            "rights_notes": "The official college PDF page was rendered at 220 dpi and visually inspected. It explicitly identifies Erika Teutsch '44 and an OSS stint. Postwar career details are outside the present claim.",
        },
        {
            "key": SWARTHMORE_MEMORIAL,
            "stable_url": "https://magazine.swarthmore.edu/issue/spring-2021/their-light-lives-on/",
            "archival_identifier": "Swarthmore Bulletin, Spring 2021 in memoriam",
            "title": "Their Light Lives On",
            "author_creator": "Swarthmore College Bulletin",
            "repository_publisher": "Swarthmore College",
            "publication_record_date": "2021",
            "locator": "Erika Teutsch '44 entry",
            "access_date": "2026-10-28",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Swarthmore College Bulletin",
            "rights_notes": "The institutional memorial states that Teutsch worked overseas for the U.S. government after graduating. It does not name the exact first overseas post or state a day-level chronology.",
        },
        {
            "key": OSSOG,
            "stable_url": "https://ossog.info/personnel.html",
            "title": "Office of Strategic Services Operational Groups: Personnel",
            "author_creator": "OSS Operational Groups research project",
            "repository_publisher": "OSS Operational Groups",
            "locator": "Personnel lists for John Tessitore and T/4 L. P. Tetreault; project notes cite NARA RG 226 operational records",
            "access_date": "2026-10-28",
            "source_quality": "D_correlative_or_secondary",
            "collection_name": "OSS Operational Groups mission histories",
            "rights_notes": "Used only as corroborative assignment and spelling context. It does not establish a pre-OSS employer and is not the principal identity bridge.",
        },
        {
            "key": VA_TERZEN,
            "stable_url": "https://gravelocator.cem.va.gov/",
            "archival_identifier": "Riverside National Cemetery, Section A, Site 533",
            "title": "Nationwide Gravesite Locator",
            "author_creator": "National Cemetery Administration",
            "repository_publisher": "U.S. Department of Veterans Affairs",
            "publication_record_date": "record current at access",
            "locator": "Adrian Terzen, 1923-1990; U.S. Army, TEC5, World War II; Riverside National Cemetery",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "National Cemetery Administration burial records",
            "rights_notes": "Used as corroborative name and service context for the protected-identifier Army match. It supplies no employer or OSS transfer chronology.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": SWARTHMORE,
            "organization_id": "fb0648df-23c8-5fd9-bd9e-4491ce8ecf13",
            "canonical_name": "Swarthmore College",
            "historical_name": "Swarthmore College",
            "aliases": ["Swarthmore"],
            "organization_type": "college",
            "sector": "academia_and_research",
            "city": "Swarthmore",
            "state_or_region": "Pennsylvania",
            "country": "United States",
            "normalization_notes": "Existing student-institution organization reused. Erika Teutsch's attendance is modeled as student status, never employment.",
        }
    ]


def army_affiliation(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    name = PEOPLE[row][1]
    is_student = item.get("relationship") == "student"
    return {
        "key": f"{slug(name)}-occupation-b946",
        "person_id": PEOPLE[row][0],
        "occupation": item["public_occupation"],
        "relationship_type": "student" if is_student else "employment",
        "end_date": item["date"],
        "date_precision": f"Historical civilian-occupation code {item['code']} was recorded at Army entry on {item['date']}; no employer, school, workplace or OSS-transfer date is named.",
        "country": "United States",
        "immediate_pre_oss": False,
        "last_civilian_pre_service": False,
        "pre_oss_temporal_basis": "strongly_date_bounded",
        "identity_confidence": "high_confidence",
        "claim_confidence": "medium",
        "source_quality": "A_direct_official",
        "publication_status": "publish_qualified",
        "research_notes": "The historical category is not converted into a named employer, workplace, school, immediate affiliation or exact modern job title.",
    }


def affiliations() -> list[dict[str, object]]:
    values = [army_affiliation(item) for item in ARMY_OCCUPATIONS]
    values.append(
        {
            "key": "erika-teutsch-swarthmore-b946",
            "person_id": PEOPLE[46][0],
            "organization_key": SWARTHMORE,
            "organization_name_as_found": "Swarthmore",
            "role_title": "economics student; class of 1944",
            "relationship_type": "student",
            "end_date": "1944",
            "date_precision": "The college identifies Teutsch as class of 1944 and says she worked overseas for the U.S. government after graduating; its 2002 profile explicitly includes OSS service, but no source states the exact start day or excludes a short intervening federal assignment.",
            "city": "Swarthmore",
            "state_or_region": "Pennsylvania",
            "country": "United States",
            "immediate_pre_oss": True,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "probable_immediate",
            "identity_confidence": "high_confidence",
            "claim_confidence": "medium",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "publish_qualified",
            "research_notes": "Swarthmore is a documented student institution, not an employer. The Box 770 personnel file is still needed to prove the exact graduation-to-OSS sequence and identify any earlier civilian employer.",
        }
    )
    return values


def claim(
    row: int,
    key: str,
    claim_type: str,
    claim_text: str,
    evidence_paraphrase: str,
    identity: str,
    temporal: str,
    source_quality: str,
    confidence: str,
    source_links: list[dict[str, object]],
    notes: str,
    affiliation_key: str | None = None,
    publication_status: str | None = None,
) -> dict[str, object]:
    return {
        "key": key,
        "person_id": PEOPLE[row][0],
        "affiliation_key": affiliation_key,
        "claim_type": claim_type,
        "claim_text": claim_text,
        "evidence_paraphrase": evidence_paraphrase,
        "identity_match_assessment": identity,
        "temporal_assessment": temporal,
        "source_quality": source_quality,
        "claim_confidence": confidence,
        "publication_status": publication_status
        or ("published" if confidence in {"confirmed", "high"} else "publish_qualified"),
        "match_notes": notes,
        "sources": source_links,
    }


def army_claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for item in ARMY_OCCUPATIONS:
        row = int(item["row"])
        name = PEOPLE[row][1]
        variant = row in {31, 45}
        identity_paraphrase = (
            "A nonshared protected identifier connects the visually verified index row to the official Army record; the close surname spelling variant is retained."
            if variant
            else "A nonshared protected identifier connects the visually verified index row to the official Army record, and the full name agrees exactly."
        )
        identity_assessment = (
            "High confidence from a private unique identifier, aligned given name and a documented close surname variant."
            if variant
            else "High confidence from a private unique identifier plus exact full-name agreement."
        )
        identity_links: list[dict[str, object]] = [
            {"source_key": INDEX, "locator_override": f"PDF page 463 row {row}; protected identifier withheld"},
            {"source_key": ARMY, "locator_override": "Accepted reviewed identity bridge; protected identifier withheld"},
        ]
        if row == 31:
            identity_links.append({"source_key": VA_TERZEN, "support_type": "context_only", "locator_override": "Adrian Terzen; U.S. Army TEC5; World War II"})
        if row in {39, 45}:
            identity_links.append({"source_key": OSSOG, "support_type": "context_only", "locator_override": "Operational Group personnel spelling and assignment context"})
        values.append(
            claim(
                row,
                f"identity-{slug(name)}-army-b946",
                "identity",
                f"Indexed {name} is a high-confidence match to the reviewed official Army entry.",
                identity_paraphrase,
                identity_assessment,
                "Identity evidence only; the Army entry does not itself establish an OSS transfer date.",
                "A_direct_official",
                "high",
                identity_links,
                "The review accepts identity only for the matching source row, preserves source spellings and does not expose the protected identifier.",
            )
        )
        category = str(item["occupation"])
        if item.get("relationship") == "student":
            claim_text = f"At Army entry on {item['date']}, {name} was recorded in the historical Students category; no school or employer is identified."
        else:
            claim_text = f"At Army entry on {item['date']}, the record coded {name}'s civilian occupation as {category}."
        values.append(
            claim(
                row,
                f"occupation-{slug(name)}-army-b946",
                "occupation",
                claim_text,
                f"The official Army record contains civilian-occupation code {item['code']}; NARA's historical code list expands it to {category}.",
                "High-confidence identity from the accepted protected-identifier bridge and exact or preserved close-variant name agreement.",
                "The code was recorded at Army entry and is date-bounded, but it identifies no employer, workplace, school or immediate OSS predecessor.",
                "A_direct_official",
                "medium",
                [
                    {"source_key": ARMY, "locator_override": f"Accepted reviewed identity record; civilian occupation code {item['code']}; protected identifier withheld"},
                    {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46; Army-entry-date and civilian-occupation fields"},
                    {"source_key": CODES, "locator_override": str(item["locator"]), "excerpt_override": category},
                ],
                "The historical category is published as qualified occupation or status evidence and is excluded from named-employer analytics.",
                f"{slug(name)}-occupation-b946",
                "publish_qualified",
            )
        )
    return values


def substantive_claims() -> list[dict[str, object]]:
    return [
        claim(
            24,
            "identity-henry-terrett-conflict-b946",
            "identity",
            "The indexed Henry W. Terrett row conflicts with an official Army record printing Henry M. Terrett despite a matching protected identifier.",
            "The private identifier agrees, but the middle initial does not; no occupation, grade or biography is transferred until the indexed file resolves the collision.",
            "Conflicting identity evidence: unique identifier agreement is strong, but the printed middle initials W and M directly disagree.",
            "Identity conflict only; the candidate Army chronology and occupation are withheld.",
            "A_direct_official",
            "conflicting",
            [
                {"source_key": INDEX, "locator_override": "PDF page 463 row 24; prints Henry W. Terrett; protected identifier withheld"},
                {"source_key": ARMY, "support_type": "contradicts", "locator_override": "Reviewed bulk candidate prints Henry M. Terrett; protected identifier withheld"},
            ],
            "The conflict is visible on the public profile and excluded from default analytics. Box 769 must resolve it.",
            publication_status="conflicting",
        ),
        claim(
            46,
            "identity-erika-teutsch-b946",
            "identity",
            "Indexed Erika Teutsch is a high-confidence match to Swarthmore College alumna and documented OSS staff member Erika Teutsch '44.",
            "The rare exact name appears in the index and two Swarthmore institutional accounts; the 2002 profile explicitly includes an OSS stint.",
            "High confidence from the distinctive exact name, class year, explicit institutional OSS statement and compatible wartime chronology.",
            "Identity is strong; the precise entry date and assignment require the Box 770 personnel file.",
            "B_authoritative_institutional",
            "high",
            [
                {"source_key": INDEX, "locator_override": "PDF page 463 row 46"},
                {"source_key": SWARTHMORE_PROFILE, "locator_override": "Printed page 52; PDF physical page 46", "excerpt_override": "Her resume includes a stint at the Office of Strategic Services"},
                {"source_key": SWARTHMORE_MEMORIAL, "support_type": "context_only", "locator_override": "Erika Teutsch '44 entry"},
            ],
            "No postwar employer is substituted for the pre-OSS question, and unrelated personal details are excluded.",
        ),
        claim(
            46,
            "immediate-erika-teutsch-swarthmore-b946",
            "immediate_pre_oss_affiliation",
            "Erika Teutsch was probably a Swarthmore College student immediately before her wartime OSS service; Swarthmore was an educational institution, not her employer.",
            "Swarthmore identifies her as class of 1944, says she worked overseas for the U.S. government after graduating and separately documents an OSS stint.",
            "High-confidence identity from the rare exact name and the institution's explicit OSS account.",
            "Probable immediate chronology: the sources place graduation before overseas federal work and OSS within the remaining wartime window, but do not give a start day or exclude a brief intervening assignment.",
            "B_authoritative_institutional",
            "medium",
            [
                {"source_key": SWARTHMORE_MEMORIAL, "locator_override": "Erika Teutsch '44 entry", "excerpt_override": "After graduating from Swarthmore, Erika worked overseas for the U.S. government"},
                {"source_key": SWARTHMORE_PROFILE, "locator_override": "Printed page 52; PDF physical page 46", "excerpt_override": "Her resume includes a stint at the Office of Strategic Services"},
            ],
            "Published only as a qualified student-affiliation finding. The personnel file is needed to confirm immediacy and identify any earlier civilian employer.",
            "erika-teutsch-swarthmore-b946",
            "publish_qualified",
        ),
    ]


def archival_update(row: int, reason: str) -> dict[str, object]:
    person_id, name = PEOPLE[row]
    return {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, Box 770 and archive location 230/86/41/07. {reason}",
        "personnel_category": "unknown_or_indeterminate",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": "Review Box 770 for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }


def army_update(row: int) -> dict[str, object]:
    person_id, name = PEOPLE[row]
    evidence = f"A nonshared protected identifier connects the visually verified {name} index row to the reviewed official Army record."
    variants: list[str] | None = None
    if row == 31:
        evidence += " The Army and VA records print the close surname variant Adrian Terzen."
        variants = ["Adrian Terzen"]
    elif row == 45:
        evidence += " The Army record prints Leo P. Tetrault, while a corroborative OSS personnel list prints L. P. Tetreault."
        variants = ["Leo P Tetrault", "Leo P Tetreault"]
    else:
        evidence += " The full name agrees exactly."
    update: dict[str, object] = {
        "person_id": person_id,
        "identity_status": "high_confidence",
        "identity_evidence": evidence,
        "personnel_category": "enlisted_army_personnel",
        "commissioned_officer": False,
        "allied_or_foreign_personnel": False,
        "manual_review_required": True,
        "research_status": "occupation_only_found",
        "next_action": "Review Box 770 to establish the immediate pre-OSS affiliation and named last civilian employer; do not convert the Army occupation category into a workplace.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }
    if variants:
        update["name_variants"] = variants
    return update


def person_updates() -> list[dict[str, object]]:
    updates = [archival_update(row, reason) for row, reason in UNRESOLVED.items()]
    updates.extend(
        army_update(int(item["row"]))
        for item in ARMY_OCCUPATIONS
        if int(item["row"]) != 45
    )

    updates.extend(
        [
            {
                "person_id": PEOPLE[24][0],
                "identity_status": "conflicting",
                "identity_evidence": "The nonshared protected identifier agrees with an official Army record, but the index prints Henry W. Terrett and the Army record prints Henry M. Terrett. No grade, occupation or biography is transferred.",
                "personnel_category": "unknown_or_indeterminate",
                "manual_review_required": True,
                "research_status": "conflicting_sources",
                "next_action": "Review Box 769 to resolve the Henry W./M. Terrett middle-initial conflict before assigning the Army record or any occupation.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[25][0],
                "identity_status": "ambiguous",
                "identity_evidence": "The index prints Walter L. Terrill without a protected identifier immediately after a separate Walter L. Terrell row with one. Name similarity and adjacency are insufficient to merge them.",
                "personnel_category": "unknown_or_indeterminate",
                "manual_review_required": True,
                "possible_duplicate_group": "walter-l-terrell-terrill-page463-rows22-25-b946",
                "research_status": "needs_identity_review",
                "next_action": "Review both Box 769 files together and compare identifiers, birth details and OSS assignments. Do not transfer row 22 evidence to row 25.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PRIOR_WALTER_TERRELL,
                "identity_status": "unresolved",
                "identity_evidence": "The index prints Walter L. Terrell with a protected identifier. A separate Walter L. Terrill row appears three rows later without one; name similarity and adjacency are insufficient to merge them.",
                "manual_review_required": True,
                "possible_duplicate_group": "walter-l-terrell-terrill-page463-rows22-25-b946",
                "research_status": "requires_archival_review",
                "next_action": "Review both Box 769 files together and compare identifiers, birth details and OSS assignments. Preserve the rows separately unless direct evidence proves duplication.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[35][0],
                "identity_status": "ambiguous",
                "identity_evidence": "Page 463 contains two separate John R. Teske rows; row 35 has no protected identifier and row 36 has one. A common normalized name alone cannot establish duplication.",
                "personnel_category": "unknown_or_indeterminate",
                "manual_review_required": True,
                "possible_duplicate_group": "john-r-teske-page463-rows35-36-b946",
                "research_status": "needs_identity_review",
                "next_action": "Review both Box 770 files together and compare identifiers, birth details, ranks and OSS assignments. Do not merge or transfer evidence by name.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[36][0],
                "identity_status": "ambiguous",
                "identity_evidence": "Page 463 contains two separate John R. Teske rows; row 36 has a protected identifier but no accepted Army or public-source bridge, while row 35 has no identifier. A name match alone cannot establish duplication.",
                "personnel_category": "unknown_or_indeterminate",
                "manual_review_required": True,
                "possible_duplicate_group": "john-r-teske-page463-rows35-36-b946",
                "research_status": "needs_identity_review",
                "next_action": "Review both Box 770 files together and compare identifiers, birth details, ranks and OSS assignments. Do not merge or transfer evidence by name.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[42][0],
                "identity_status": "ambiguous",
                "identity_evidence": "The visually verified page 463 row contains only the surname Testi and an asterisk, with a printed review note and no given name or protected identifier. Public searches cannot resolve it safely.",
                "personnel_category": "unknown_or_indeterminate",
                "manual_review_required": True,
                "research_status": "needs_identity_review",
                "next_action": "Review the Box 770 file and original finding aids to recover the given name, identifiers and any pre-OSS affiliation. Do not assign a namesake from surname-only searches.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[44][0],
                "identity_status": "ambiguous",
                "identity_evidence": "The index prints Leo P. Tetrault without a protected identifier immediately before a separate Leo P. Tetrealt row with one. The accepted Army evidence applies only to row 45.",
                "personnel_category": "unknown_or_indeterminate",
                "manual_review_required": True,
                "possible_duplicate_group": "leo-p-tetrault-tetrealt-page463-rows44-45-b946",
                "research_status": "needs_identity_review",
                "next_action": "Review both Box 770 files together and compare identifiers, birth details and OSS assignments. Do not transfer row 45 evidence to row 44.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                **army_update(45),
                "possible_duplicate_group": "leo-p-tetrault-tetrealt-page463-rows44-45-b946",
                "next_action": "Review both Box 770 files together to determine whether rows 44 and 45 are duplicate references or different people, and to establish the immediate pre-OSS affiliation without transferring the protected identifier.",
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[46][0],
                "identity_status": "high_confidence",
                "identity_evidence": "The rare exact name aligns across the index and two Swarthmore institutional accounts; the 2002 profile explicitly documents Erika Teutsch '44 as having served in the OSS.",
                "name_variants": ["Erika Teutsch '44"],
                "personnel_category": "civilian_professional_or_administrative_grade",
                "commissioned_officer": False,
                "manual_review_required": True,
                "research_status": "needs_temporal_review",
                "next_action": "Review Box 770 to confirm the exact 1944 sequence between Swarthmore graduation and OSS entry and to identify any earlier civilian employer.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
        ]
    )
    return updates


def research_attempts() -> list[dict[str, object]]:
    army_rows = {int(item["row"]) for item in ARMY_OCCUPATIONS}
    attempts: list[dict[str, object]] = []
    for row in sorted(PEOPLE):
        person_id, name = PEOPLE[row]
        if row in UNRESOLVED:
            outcome, reviewed, rejected, detail = "no_result", 5, 5, UNRESOLVED[row]
        elif row == 24:
            outcome, reviewed, rejected, detail = (
                "source_reviewed",
                6,
                5,
                "A protected-identifier Army candidate conflicts on the middle initial, so the conflict is preserved and all occupation evidence is withheld.",
            )
        elif row in {25, 35, 36, 44}:
            outcome, reviewed, rejected, detail = (
                "candidate_found",
                6,
                5,
                "An adjacent same-name or close-spelling index row creates a possible duplicate relationship, but missing or different protected identifiers prevent a merge or evidence transfer.",
            )
        elif row == 42:
            outcome, reviewed, rejected, detail = (
                "no_result",
                5,
                5,
                "The surname-only asterisk row cannot be resolved safely through public searches and requires the physical file.",
            )
        elif row == 46:
            outcome, reviewed, rejected, detail = (
                "source_reviewed",
                8,
                4,
                "Two Swarthmore institutional sources establish the rare-name identity, class of 1944, graduation-before-overseas-government-work chronology and explicit OSS service; exact immediacy remains qualified.",
            )
        elif row in army_rows:
            outcome, reviewed, rejected, detail = (
                "source_reviewed",
                6,
                4,
                "An accepted protected-identifier Army bridge supports identity and a dated historical occupation or student-status category, not a named employer or immediate OSS affiliation.",
            )
        else:
            raise AssertionError(f"Missing Batch 946 outcome for row {row}")
        attempts.append(
            {
                "key": f"page463-row{row}-{slug(name)}-b946",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index and public Archives context; CIA Reading Room or equivalent official source; exact-name and meaningful variants; OSS and military clues; employer and occupation 1940; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Boxes 769-770; protected identifiers used privately only when defensible",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_946",
                "started_at": "2026-10-28T08:15:00Z",
                "completed_at": "2026-10-28T09:16:00Z",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search snippets, family-tree assertions, modern people-finder pages, postwar-only leads and sources without an OSS, protected-identifier or Box-file bridge were not assigned.",
                "research_notes": f"{detail} The index page and admitted Army, code-list or institutional PDF pages were visually checked where applicable. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": "Review the indexed personnel file for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before wartime service.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b946-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-946-v1",
        "reviewer": "Before OSS Batch 946 evidence review",
        "sources": sources(),
        "organizations": organizations(),
        "affiliations": affiliations(),
        "claims": army_claims() + substantive_claims(),
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }
    EvidenceBundle.model_validate(bundle)
    OUTPUT.write_text(
        json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
