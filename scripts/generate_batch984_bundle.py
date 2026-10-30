#!/usr/bin/env python3
"""Generate the reviewed Batch 984 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page482-william-verback-to-frederick-vetlesen-"
    "review_batch-984_2026-10-31.json"
)

INDEX = "nara-index-b984"
ARMY = "army-bulk-b984"
TECH = "army-tech-b984"
CODES = "army-codes-b984"
VERKAMP_OBIT = "verkamp-obituary-b984"
VARIAN_FRY = "varian-fry-verzeano-b984"
VERRILL_CASE = "verrill-court-opinion-b984"
NPS_VERGHIS = "nps-george-verghis-b984"
NPS_VESTNER = "nps-eliot-vestner-b984"
BRONXVILLE_VESTNER = "bronxville-eliot-vestner-b984"
COLUMBIA_VETLESEN = "columbia-vetlesen-b984"
NARA_VETLESEN = "nara-vetlesen-award-b984"

ORG_CINCINNATI = "university-cincinnati-b984"
ORG_RESCUE = "centre-americain-secours-b984"
ORG_VERRILL = "verrill-hale-booth-ives-b984"
ORG_ARMY = "us-army-b984"


PEOPLE = {
    24: ("2dac46d2-9b5d-5730-acb6-23290829a089", "William Verback"),
    25: ("001e9673-0fc6-5dce-8429-abcf0e475057", "Madeline Verga"),
    26: ("f130b15b-0575-58cc-8929-9fa5bea41b7e", "Francis C Verger"),
    27: ("7d7ba9de-cab0-5a67-bd1b-582ad1123eac", "George W Verghis"),
    28: ("4b0ba62d-83e4-552e-8adc-0330ebce47ee", "Henri L Vergon"),
    29: ("e29bb927-f990-5078-ac90-68fcb0e38634", "George M Verhaeghe"),
    30: ("97ba01a2-5b0c-5d2b-9b34-a62d709313d6", "Joseph P Verkamp"),
    31: ("fb8792f6-08ec-586f-99b9-9790913e5ff4", "Robert L Verlin"),
    32: ("d147ce88-5433-52e2-a501-9cf351a625a5", "Robert J Vermillion"),
    33: ("359d97f4-5f6d-58ed-b8fa-f11f6ed4bef0", "Frank Vernon"),
    34: ("eddd5dcf-bf46-54cb-b9e7-3f681a4ad351", "Robert L Vernon"),
    35: ("342a327e-add8-548f-b7fa-10a3a1c18940", "Joseph R Verreault"),
    36: ("cda23c4c-3ae2-585f-9b79-f597967a8f66", "Robinson Verrill"),
    37: ("6847cada-7512-51e5-a133-c7cd6a13c3d7", "Margaret Verrnay"),
    38: ("b435df81-7601-52f3-a167-211173b83f8e", "Irving A Verschoor"),
    39: ("cf546e55-06b5-5eb2-82a7-9f264e930744", "Marcel Verzeano"),
    40: ("55337c5f-4136-5242-b58d-ba8372a9f01c", "Joseph Veselinovich"),
    41: ("3ca4b213-c8ba-56c1-807e-0296b80429fe", "Erik J Vesely"),
    42: ("cc7777d3-a62d-5a6f-9243-6a726dda4fba", "John W Vest"),
    43: ("b9932397-4c76-5442-bcfd-9875324e5c76", "James O Vestal"),
    44: ("f632036c-0896-5d74-bc26-a7e2c699d503", "Carolyn B Vester"),
    45: ("ab78876d-899a-55db-98f8-03ff916bf315", "Eliot N Vestner"),
    46: ("aa2df4e4-b97f-51cf-999d-d600620f6366", "Frederick Vetlesen"),
}


ARMY_FINDINGS = {
    31: {
        "date": "1942-04-16",
        "code": "056",
        "occupation": "Photographers",
        "public_occupation": "photographer",
        "locator": "PDF physical page 171; historical category 0-56",
    },
    32: {
        "date": "1943-04-14",
        "code": "103",
        "occupation": "Checkers",
        "public_occupation": "checker",
        "locator": "PDF physical page 171; historical category 1-03",
    },
    34: {
        "date": "1942-09-28",
        "code": "175",
        "occupation": "Salespersons",
        "public_occupation": "salesperson",
        "locator": "PDF physical page 171; historical category 1-75",
    },
    39: {
        "date": "1943-12-11",
        "code": "026",
        "occupation": "Physicians and surgeons",
        "public_occupation": "physician or surgeon",
        "locator": "PDF physical page 171; historical category 0-26",
    },
    42: {
        "date": "1942-08-11",
        "code": "419",
        "occupation": "Occupations in manufacture of textiles, not elsewhere classified",
        "public_occupation": "textile-manufacturing occupation, not elsewhere classified",
        "locator": "PDF physical page 173; historical category 4-19",
    },
    43: {
        "date": "1942-02-03",
        "code": "226",
        "occupation": "Cooks, except private family",
        "public_occupation": "cook, except in a private family",
        "locator": "PDF physical page 172; historical category 2-26",
    },
}


UNRESOLVED = {
    24: "Exact-name, OSS, employer, occupation, obituary, directory and archival searches supplied no reliable identity or pre-OSS affiliation bridge.",
    25: "The protected identifier and Box 802 distinguish this row, but reviewed exact-name and institutional searches did not establish a reliable biography or pre-OSS affiliation.",
    26: "Exact-name and spelling-variant searches produced multiple unbridged namesakes and no protected-identifier, Box 803 or direct OSS connection.",
    28: "The French rank and Box 803 narrow the archival target, but accessible French, military and OSS searches did not establish the lieutenant's identity or pre-OSS sequence.",
    29: "Wartime Jedburgh and award-roster leads support an OSS officer with this exact name and rank, but they do not establish a pre-OSS employer or a sufficiently documented civilian chronology.",
    33: "The common name and absence of an index identifier left obituary, military and directory candidates unresolved.",
    35: "French-Canadian and U.S. namesake results supplied no protected identifier, Box 803 or direct OSS bridge.",
    37: "Exact-name and likely spelling-variant searches supplied no reliable identity, occupation or pre-OSS affiliation bridge.",
    38: "A same-name postwar newspaper lead mentions British intelligence and OSS experience but does not establish the indexed identity or a dated pre-OSS affiliation.",
    41: "Exact-name and Central European spelling-variant searches supplied no protected identifier, Box 804 or direct OSS bridge.",
    44: "Exact-name, employer, occupation, obituary, directory and archival searches supplied no reliable identity or pre-OSS affiliation bridge.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 802-804",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 482, rows 24-46; checked against layout-preserving text and an original-detail page render",
            "access_date": "2026-10-31",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate; original spelling and archival context are recoverable while public identifiers are masked.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; eight Batch 984 identity comparisons; protected identifiers and record ordinals withheld",
            "access_date": "2026-10-31",
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
            "access_date": "2026-10-31",
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
            "locator": "PDF physical pages 171-173; six published Batch 984 categories visually and textually checked; code 993 left uninterpreted",
            "access_date": "2026-10-31",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical categories identify status or broad occupation, not a named employer, workplace or exact job title.",
        },
        {
            "key": VERKAMP_OBIT,
            "stable_url": "https://www.legacy.com/us/obituaries/cincinnati/name/joseph-verkamp-obituary?id=39661908",
            "title": "Joseph P. Verkamp obituary",
            "author_creator": "The Cincinnati Enquirer",
            "repository_publisher": "The Cincinnati Enquirer; Legacy.com",
            "publication_record_date": "2005-04-29",
            "locator": "Biographical paragraph describing University of Cincinnati engineering study, Army enlistment and OSS assignment",
            "access_date": "2026-10-31",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Cincinnati Enquirer obituaries",
            "rights_notes": "The obituary's 1943 enlistment year conflicts with the official Army file's 1942 entry date; the discrepancy is retained.",
        },
        {
            "key": VARIAN_FRY,
            "stable_url": "https://www.varianfry.org/sauvage_fry_oxford_en.htm",
            "title": "Varian Fry in Marseille",
            "author_creator": "Pierre Sauvage",
            "repository_publisher": "Varian Fry Institute; Chambon Foundation",
            "publication_record_date": "2001",
            "locator": "Section describing American Rescue Center staffer and physician Marcel Verzeano",
            "access_date": "2026-10-31",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Varian Fry Institute historical resources",
        },
        {
            "key": VERRILL_CASE,
            "stable_url": "https://openjurist.org/25/f2d/232/railways-corp-v-ray-consol-copper-co",
            "archival_identifier": "25 F.2d 232; U.S. Court of Appeals for the First Circuit; April 9, 1928",
            "title": "Railways Corporation v. Ray Consolidated Copper Company",
            "author_creator": "United States Court of Appeals for the First Circuit",
            "repository_publisher": "OpenJurist",
            "publication_record_date": "1928-04-09",
            "locator": "Counsel listing names Robinson Verrill and the firm Verrill, Hale, Booth & Ives",
            "access_date": "2026-10-31",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Federal Reporter, Second Series",
            "document_number": "25 F.2d 232",
        },
        {
            "key": NPS_VERGHIS,
            "stable_url": "https://home.nps.gov/articles/oss-in-action-the-mediterranean-and-european-theaters.htm",
            "title": "OSS in Action: The Mediterranean and European Theaters",
            "author_creator": "John Whiteclay Chambers II",
            "repository_publisher": "National Park Service",
            "publication_record_date": "2008; web edition current at access",
            "locator": "Greek-American Operational Group section naming Captain George Verghis",
            "access_date": "2026-10-31",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "OSS Training in the National Parks and Service Abroad in World War II",
        },
        {
            "key": NPS_VESTNER,
            "stable_url": "https://www.nps.gov/articles/instructing-for-dangerous-missions.htm",
            "title": "Instructing for Dangerous Missions",
            "author_creator": "John Whiteclay Chambers II",
            "repository_publisher": "National Park Service",
            "publication_record_date": "2008; web edition current at access",
            "locator": "Area A instructor section naming Captain Eliot N. Vestner as chief instructor in 1943",
            "access_date": "2026-10-31",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "OSS Training in the National Parks and Service Abroad in World War II",
        },
        {
            "key": BRONXVILLE_VESTNER,
            "archival_identifier": "Bronxville Historical Conservancy, Bronxville's World War II, page 38",
            "title": "Bronxville's World War II",
            "author_creator": "Raymond H. Geselbracht",
            "repository_publisher": "Bronxville Historical Conservancy",
            "publication_record_date": "2024",
            "locator": "PDF physical page 38; Eliot N. Vestner, Sr. and Eliot N. Vestner, Jr.",
            "access_date": "2026-10-31",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Bronxville Historical Conservancy local histories",
            "rights_notes": "Used only for concise chronology; the public site does not reproduce the page.",
        },
        {
            "key": COLUMBIA_VETLESEN,
            "stable_url": "https://lamont.columbia.edu/about/vetlesen-prize",
            "title": "The Vetlesen Prize",
            "author_creator": "Lamont-Doherty Earth Observatory",
            "repository_publisher": "Columbia University",
            "publication_record_date": "Current at access",
            "locator": "Biographical section on Georg Unger Vetlesen",
            "access_date": "2026-10-31",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Lamont-Doherty Earth Observatory institutional history",
            "rights_notes": "The institutional biography uses Georg Unger Vetlesen; the identity bridge to indexed Frederick Vetlesen remains qualified.",
        },
        {
            "key": NARA_VETLESEN,
            "stable_url": "https://www.archives.gov/files/research/jfk/releases/104-10165-10120.pdf",
            "archival_identifier": "JFK release 104-10165-10120; OSS SO Branch awards-board recommendations",
            "title": "Survey of Board Recommendations: SO Branch",
            "author_creator": "Office of Strategic Services",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "World War II; released 2017",
            "locator": "PDF physical page 155, document page 35; Legion of Merit recommendation for Cmdr. Frederick W. G. U. Vetlesen, USNR",
            "access_date": "2026-10-31",
            "source_quality": "A_direct_official",
            "collection_name": "JFK Assassination Records Collection",
            "document_number": "104-10165-10120",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": ORG_CINCINNATI,
            "organization_id": "999ca910-2376-5acc-a6dd-092ba19c2ab5",
            "canonical_name": "University of Cincinnati",
            "historical_name": "University of Cincinnati",
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "Cincinnati",
            "state_or_region": "Ohio",
            "country": "United States",
            "normalization_notes": "Student status is modeled separately from employment.",
        },
        {
            "key": ORG_RESCUE,
            "organization_id": "463def8b-1633-5a8d-8c1a-af710fc29b9a",
            "canonical_name": "Centre américain de secours",
            "historical_name": "Centre américain de secours",
            "aliases": ["American Rescue Center", "Centre Américain de Secours"],
            "organization_type": "refugee relief and rescue organization",
            "sector": "labor_nonprofit_and_religion",
            "city": "Marseille",
            "country": "France",
            "active_dates": "1940-1941",
            "normalization_notes": "The historical French and English names are retained as aliases; no modern successor is substituted.",
        },
        {
            "key": ORG_VERRILL,
            "canonical_name": "Verrill, Hale, Booth & Ives",
            "historical_name": "Verrill, Hale, Booth & Ives",
            "organization_type": "law firm",
            "sector": "law",
            "city": "Portland",
            "state_or_region": "Maine",
            "country": "United States",
            "active_dates": "documented by 1928",
            "normalization_notes": "Historical firm name preserved; no modern firm name is substituted.",
        },
        {
            "key": ORG_ARMY,
            "organization_id": "28a26f92-78af-5a1a-9c09-a843eb5975b4",
            "canonical_name": "United States Army",
            "historical_name": "Army of the United States",
            "aliases": ["U.S. Army", "Army"],
            "organization_type": "military service",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "Military assignment is not classified as civilian employment.",
        },
    ]


def occupation_affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, item in ARMY_FINDINGS.items():
        values.append(
            {
                "key": f"{slug(PEOPLE[row][1])}-occupation-b984-row{row}",
                "person_id": PEOPLE[row][0],
                "occupation": item["public_occupation"],
                "relationship_type": "employment",
                "end_date": item["date"],
                "date_precision": "Historical civilian-occupation category recorded at Army entry; employer, workplace and duration are not supplied",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "A_direct_official",
                "publication_status": "publish_qualified",
                "research_notes": "Official historical category only; excluded from verified-employer analytics and not narrowed beyond the code-list wording.",
            }
        )
    return values


def affiliations() -> list[dict[str, object]]:
    values = occupation_affiliations()
    values.extend(
        [
            {
                "key": "joseph-verkamp-cincinnati-student-b984",
                "person_id": PEOPLE[30][0],
                "organization_key": ORG_CINCINNATI,
                "organization_name_as_found": "University of Cincinnati",
                "role_title": "engineering student",
                "relationship_type": "student",
                "end_date": "Before Army entry",
                "date_precision": "The obituary says he left engineering studies to enlist; its 1943 enlistment year conflicts with the official Army entry date of 1942-10-28",
                "city": "Cincinnati",
                "state_or_region": "Ohio",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "published",
                "research_notes": "Student status is not employment. The conflicting enlistment years are displayed rather than harmonized.",
            },
            {
                "key": "marcel-verzeano-american-rescue-center-b984",
                "person_id": PEOPLE[39][0],
                "organization_key": ORG_RESCUE,
                "organization_name_as_found": "American Rescue Center",
                "role_title": "staffer and physician",
                "occupation": "physician",
                "relationship_type": "professional_affiliation",
                "start_date": "1940",
                "end_date": "1941",
                "date_precision": "Documented Marseille rescue-work period before later U.S. Army entry; not shown to be the immediate pre-OSS role",
                "city": "Marseille",
                "country": "France",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Modeled as professional affiliation because the reviewed source does not establish payroll status.",
            },
            {
                "key": "robinson-verrill-law-firm-b984",
                "person_id": PEOPLE[36][0],
                "organization_key": ORG_VERRILL,
                "organization_name_as_found": "Verrill, Hale, Booth & Ives",
                "role_title": "lawyer",
                "occupation": "lawyer",
                "relationship_type": "employment",
                "start_date": "1928",
                "date_precision": "Contemporary counsel listing; definitely prewar but not demonstrated as the immediate predecessor to Army or OSS service",
                "city": "Portland",
                "state_or_region": "Maine",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "probable",
                "claim_confidence": "medium",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "publish_qualified",
                "research_notes": "Exact uncommon name and contemporary firm association are strong, but Box 803 remains necessary to close the person-level identity bridge.",
            },
            {
                "key": "eliot-vestner-us-army-b984",
                "person_id": PEOPLE[45][0],
                "organization_key": ORG_ARMY,
                "organization_name_as_found": "Army",
                "role_title": "Army officer; later OSS Area A chief instructor",
                "relationship_type": "military_assignment",
                "start_date": "1941-12",
                "end_date": "By 1943",
                "date_precision": "Army service began about two weeks after Pearl Harbor; the NPS documents an OSS captain and chief instructor in 1943",
                "city": "Washington",
                "state_or_region": "District of Columbia",
                "country": "United States",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "probable_immediate",
                "identity_confidence": "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "publish_qualified",
                "research_notes": "The sources establish an Army-to-OSS chronology but do not state the exact transfer date or identify a civilian employer.",
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


def army_identity_claim(row: int) -> dict[str, object]:
    name = PEOPLE[row][1]
    return claim(
        row,
        f"identity-{slug(name)}-army-b984-row{row}",
        "identity",
        f"Indexed {name} is high-confidence matched to the official Army entry used for this dated pre-service finding.",
        "The exact official name and a nonshared protected-identifier agreement support the match.",
        "High confidence from exact name and a nonshared protected identifier; the protected value and raw record are withheld.",
        "The Army entry date is preserved separately from the later OSS-index context.",
        "A_direct_official",
        "high",
        [
            {"source_key": INDEX},
            {
                "source_key": ARMY,
                "locator_override": "Accepted identity bridge; protected identifier and raw record withheld",
            },
        ],
        "Protected identifiers were used only for private resolution and remain absent from the evidence bundle and public output.",
    )


def army_claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, item in ARMY_FINDINGS.items():
        name = PEOPLE[row][1]
        values.append(army_identity_claim(row))
        values.append(
            claim(
                row,
                f"occupation-{slug(name)}-b984-row{row}",
                "occupation",
                f"At Army entry on {item['date']}, {name}'s historical civilian category was {str(item['occupation']).lower()}.",
                f"The official Army field carries historical code {item['code']}; NARA's code list defines it as {item['occupation']}.",
                "High confidence from exact name and a nonshared protected identifier.",
                "Dated at Army entry before the later OSS-index context; no named employer, workplace, duration or exact OSS-transfer date is supplied.",
                "A_direct_official",
                "medium",
                [
                    {
                        "source_key": ARMY,
                        "locator_override": "Accepted identity bridge; protected identifier and raw record withheld",
                    },
                    {"source_key": TECH, "locator_override": "PDF physical pages 44-46; civilian-occupation field"},
                    {"source_key": CODES, "locator_override": str(item["locator"])},
                ],
                "Published as a qualified historical category only; excluded from verified-employer analytics.",
                f"{slug(name)}-occupation-b984-row{row}",
                "publish_qualified",
            )
        )
    return values


def special_claims() -> list[dict[str, object]]:
    return [
        army_identity_claim(30),
        claim(
            30,
            "last-civilian-joseph-verkamp-student-b984",
            "other_pre_oss_affiliation",
            "Joseph P. Verkamp was an engineering student at the University of Cincinnati immediately before entering Army service.",
            "His obituary says he left University of Cincinnati engineering studies to enlist and was later assigned to the OSS.",
            "High confidence from exact uncommon name, PFC context, official protected-identifier agreement and explicit obituary OSS service.",
            "Strongly date-bounded as the last documented civilian status before Army service; the obituary's 1943 year conflicts with the official 1942 entry date.",
            "C_reputable_contemporary_or_scholarly",
            "high",
            [
                {"source_key": INDEX},
                {"source_key": ARMY, "locator_override": "Official Army entry date 1942-10-28; protected identifier withheld"},
                {"source_key": VERKAMP_OBIT},
            ],
            "Student status is not employment and is therefore not marked as a last civilian employer. The date conflict is disclosed and not silently reconciled.",
            "joseph-verkamp-cincinnati-student-b984",
        ),
        claim(
            27,
            "identity-george-verghis-greek-og-b984",
            "identity",
            "Indexed George W Verghis is high-confidence matched to the Captain George Verghis who led Greek-American OSS Operational Group missions.",
            "The uncommon exact first and last name, captain context and Greek Operational Group service align with the indexed official record.",
            "High confidence, but the NPS source omits the middle initial and protected identifier; Box 803 remains the final identity check.",
            "The NPS account documents wartime OSS operations, not a pre-OSS employer or transfer chronology.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": INDEX}, {"source_key": NPS_VERGHIS}],
            "No pre-OSS employer is inferred from the operational history.",
        ),
        claim(
            39,
            "other-pre-oss-marcel-verzeano-rescue-center-b984",
            "other_pre_oss_affiliation",
            "Before later U.S. Army and OSS service, Marcel Verzeano worked as a physician and staffer with the American Rescue Center in Marseille.",
            "The Varian Fry Institute identifies Marcel Verzeano as an American Rescue Center staffer and Romanian Jewish doctor involved in refugee rescue.",
            "High confidence from the rare exact name, physician description and exact official protected-identifier match to the indexed later officer.",
            "Documented in Marseille in 1940-1941; the evidence does not establish it as the immediate predecessor to Army or OSS service.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": INDEX}, {"source_key": ARMY}, {"source_key": VARIAN_FRY}],
            "Modeled as professional affiliation because the reviewed source does not establish payroll status.",
            "marcel-verzeano-american-rescue-center-b984",
        ),
        claim(
            36,
            "other-pre-oss-robinson-verrill-law-firm-b984",
            "other_pre_oss_affiliation",
            "A 1928 federal appellate case identifies Robinson Verrill as a lawyer with Verrill, Hale, Booth & Ives in Portland, Maine.",
            "The contemporary counsel listing names Robinson Verrill and the historical Portland law firm.",
            "Probable match from the uncommon exact name and legal profession; Box 803 is required to close the identity bridge to the later lieutenant colonel.",
            "Definitely prewar, but too early to establish the firm as the immediate pre-OSS or last civilian employer.",
            "C_reputable_contemporary_or_scholarly",
            "medium",
            [{"source_key": INDEX}, {"source_key": VERRILL_CASE}],
            "Published with visible qualification and excluded from default confirmed/high employer analytics.",
            "robinson-verrill-law-firm-b984",
            "publish_qualified",
        ),
        claim(
            45,
            "identity-eliot-n-vestner-b984",
            "identity",
            "Indexed Eliot N Vestner is high-confidence matched to Captain Eliot N. Vestner, the OSS Area A chief instructor in 1943.",
            "The exact uncommon name, indexed identifier, Army chronology and official NPS Area A role align.",
            "High confidence from exact full-name agreement, the indexed protected identifier and two concordant institutional histories.",
            "The sources establish Army service beginning in December 1941 and an OSS training role in 1943.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": INDEX}, {"source_key": NPS_VESTNER}, {"source_key": BRONXVILLE_VESTNER}],
            "The civilian employer before Army entry remains unidentified.",
        ),
        claim(
            45,
            "immediate-eliot-vestner-army-b984",
            "immediate_pre_oss_affiliation",
            "Eliot N. Vestner's best-supported immediate pre-OSS status is U.S. Army service begun in December 1941.",
            "A local institutional history dates his Army entry to about two weeks after Pearl Harbor; the NPS places him in OSS Area A by 1943.",
            "High-confidence Eliot N. Vestner identity.",
            "Probable immediate military pathway; the sources do not state the exact Army-to-OSS transfer date.",
            "B_authoritative_institutional",
            "medium",
            [{"source_key": BRONXVILLE_VESTNER}, {"source_key": NPS_VESTNER}],
            "Military assignment, not a civilian employer. The claim remains visibly qualified.",
            "eliot-vestner-us-army-b984",
            "publish_qualified",
        ),
        claim(
            46,
            "identity-frederick-vetlesen-b984",
            "identity",
            "Indexed Commander Frederick Vetlesen is confirmed as Cmdr. Frederick W. G. U. Vetlesen, USNR, in an official OSS awards-board record.",
            "The official record matches the uncommon indexed name, commander rank and Norwegian-Danish resistance mission.",
            "Confirmed for the exact Frederick Vetlesen OSS record; the separate bridge to Columbia's Georg Unger Vetlesen remains probable rather than settled.",
            "The award record documents OSS wartime work, not the prewar civilian chronology.",
            "A_direct_official",
            "confirmed",
            [{"source_key": INDEX}, {"source_key": NARA_VETLESEN}],
            "The official spelling is preserved. The Columbia name variant is not silently substituted.",
        ),
        claim(
            46,
            "occupation-frederick-vetlesen-shipbuilder-b984",
            "occupation",
            "Columbia's institutional biography supports a probable prewar occupation for indexed Frederick Vetlesen as a shipbuilder in the United States.",
            "Columbia describes Georg Unger Vetlesen as a successful U.S. shipbuilder who became a Navy commander and worked with Norwegian resistance during World War II.",
            "Probable identity bridge from the highly distinctive Vetlesen surname, commander rank, Navy service and Norwegian-resistance mission; first names conflict.",
            "Documented as prewar civilian work, but neither a named employer nor an exact immediate-to-Navy chronology is supplied.",
            "B_authoritative_institutional",
            "medium",
            [{"source_key": COLUMBIA_VETLESEN}, {"source_key": NARA_VETLESEN}],
            "Published only as a qualified occupation lead. Box 804 is required before treating Georg and Frederick as the same person for confirmed analytics.",
            publication_status="publish_qualified",
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
    categories = {
        24: "unknown_or_indeterminate",
        25: "unknown_or_indeterminate",
        26: "unknown_or_indeterminate",
        28: "foreign_or_allied_military_personnel",
        29: "commissioned_army_officer",
        33: "unknown_or_indeterminate",
        35: "unknown_or_indeterminate",
        37: "unknown_or_indeterminate",
        38: "unknown_or_indeterminate",
        41: "unknown_or_indeterminate",
        44: "unknown_or_indeterminate",
    }
    for row, reason in UNRESOLVED.items():
        values.append(
            base_update(
                row,
                identity_status="probable" if row == 29 else "unresolved",
                identity_evidence=f"The visually verified page 482 row supplies {PEOPLE[row][1]} and Box {802 if row < 26 else (803 if row < 41 else 804)}. {reason}",
                personnel_category=categories[row],
                commissioned_officer=True if row == 29 else (False if row == 28 else None),
                allied_or_foreign_personnel=True if row == 28 else False,
                research_status="requires_archival_review",
                next_action=f"Review the indexed personnel file for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}",
            )
        )

    values.append(
        base_update(
            27,
            identity_status="high_confidence",
            identity_evidence="The uncommon exact name, indexed protected identifier, captain context and National Park Service Greek Operational Group history support a high-confidence match.",
            personnel_category="commissioned_army_officer",
            commissioned_officer=True,
            allied_or_foreign_personnel=False,
            research_status="requires_archival_review",
            next_action="Review Box 803 to verify the middle initial and identify the immediate pre-OSS affiliation and last civilian employer; the operational history documents OSS service only.",
        )
    )

    values.append(
        base_update(
            30,
            identity_status="high_confidence",
            identity_evidence="Exact uncommon name, PFC context, official nonshared protected identifier and an obituary explicitly linking Army service to OSS support this match.",
            personnel_category="enlisted_army_personnel",
            commissioned_officer=False,
            allied_or_foreign_personnel=False,
            research_status="completed",
            next_action="Student status immediately before Army service is documented. Review Box 803 to reconcile the 1942 official Army-entry date with the obituary's 1943 year and to determine whether separate civilian employment existed.",
            nara_catalog_id="1263923",
            archival_review_priority="medium",
        )
    )

    for row in ARMY_FINDINGS:
        status = "occupation_only_found"
        next_action = f"Review Box {803 if row < 41 else 804} to identify the named employer behind historical occupation code {ARMY_FINDINGS[row]['code']} and establish the Army-to-OSS chronology."
        if row == 39:
            next_action = "Review Box 803 to determine whether the Marseille rescue affiliation was followed by another civilian role and to establish the Army-to-OSS chronology."
        values.append(
            base_update(
                row,
                identity_status="high_confidence",
                identity_evidence="The exact official name and a nonshared protected-identifier agreement support the Army identity match; the protected value remains private.",
                name_variants=["Maurice Verzeano"] if row == 39 else None,
                personnel_category="commissioned_army_officer" if row == 39 else "enlisted_army_personnel",
                commissioned_officer=True if row == 39 else False,
                allied_or_foreign_personnel=False,
                research_status=status,
                next_action=next_action,
                nara_catalog_id="1263923",
            )
        )

    values.append(
        base_update(
            36,
            identity_status="probable",
            identity_evidence="A contemporary federal case identifies an uncommon exact-name Portland lawyer, but Box 803 is still needed to connect him definitively to the indexed lieutenant colonel.",
            personnel_category="commissioned_army_officer",
            commissioned_officer=True,
            allied_or_foreign_personnel=False,
            research_status="documented_prewar_employer_found",
            next_action="Review Box 803 to confirm the Portland law-firm identity and determine whether Verrill, Hale, Booth & Ives remained the last civilian employer before wartime service.",
        )
    )

    values.append(
        base_update(
            40,
            identity_status="conflicting",
            identity_evidence="The page 482 second-lieutenant row is distinct, but its protected identifier is already associated with a differently named printed source row; no Army finding is transferred.",
            personnel_category="commissioned_army_officer",
            commissioned_officer=True,
            allied_or_foreign_personnel=False,
            possible_duplicate_group="protected-identifier-conflict-b984",
            research_status="conflicting_sources",
            next_action="Review Box 803 and the separately indexed conflicting row to resolve the protected-identifier discrepancy before accepting any external identity or pre-OSS claim.",
            archival_review_priority="critical",
        )
    )

    values.append(
        base_update(
            45,
            identity_status="high_confidence",
            identity_evidence="The exact uncommon name, indexed protected identifier, Army chronology and National Park Service identification of Captain Eliot N. Vestner as OSS Area A chief instructor align.",
            personnel_category="commissioned_army_officer",
            commissioned_officer=True,
            allied_or_foreign_personnel=False,
            research_status="completed",
            next_action="The Army-to-OSS pathway is documented with a qualified transfer chronology. Review Box 804 to identify his last civilian employer before Army service and the exact transfer date.",
            archival_review_priority="medium",
        )
    )

    values.append(
        base_update(
            46,
            identity_status="confirmed",
            identity_evidence="The exact uncommon indexed name and commander rank match the official OSS award record for Cmdr. Frederick W. G. U. Vetlesen, USNR. The bridge to Columbia's Georg Unger Vetlesen remains probable.",
            name_variants=["Frederick W. G. U. Vetlesen", "Georg Unger Vetlesen (probable institutional-name bridge)"],
            personnel_category="commissioned_naval_officer",
            commissioned_officer=True,
            allied_or_foreign_personnel=False,
            research_status="requires_archival_review",
            next_action="Review Box 804 to determine whether Frederick W. G. U. Vetlesen and Georg Unger Vetlesen are the same person and to identify any named shipbuilding employer before Navy service.",
            archival_review_priority="critical",
        )
    )
    return values


def research_attempts() -> list[dict[str, object]]:
    sourced = set(ARMY_FINDINGS) | {27, 30, 36, 45, 46}
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        if row in sourced:
            outcome = "source_reviewed"
            sources_reviewed = 8 if row in {30, 39, 45, 46} else 6
            rejected = 3
            detail = "Reviewed official and institutional sources produced the identity, occupation, student, professional, legal-employment or military-pathway outcome recorded in the bundle."
        elif row == 40:
            outcome = "candidate_rejected"
            sources_reviewed = 5
            rejected = 4
            detail = "A protected-identifier conflict with a differently named printed row prevents transfer of the Army candidate or any occupation data."
        elif row in UNRESOLVED:
            outcome = "no_result"
            sources_reviewed = 5
            rejected = 5
            detail = UNRESOLVED[row]
        else:
            outcome = "no_result"
            sources_reviewed = 5
            rejected = 5
            detail = "The staged protocol produced no reliable person-level identity or pre-OSS affiliation bridge."
        attempts.append(
            {
                "key": f"page482-row{row}-{slug(name)}-b984",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index and official Archives context; CIA Reading Room or equivalent official-source check; exact-name and meaningful variants; OSS, Army, Navy, rank, branch and assignment clues; employer and occupation 1940; obituary, institutional, newspaper, directory, Library of Congress and archival searches; indexed Box {802 if row < 26 else (803 if row < 41 else 804)}; protected identifiers used only in private official-record comparison",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_984",
                "started_at": "2026-10-31T01:05:00Z",
                "completed_at": "2026-10-31T12:55:00Z",
                "outcome": outcome,
                "sources_reviewed": sources_reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, snippets, commercial people-finder pages, relatives, unsourced genealogy, postwar-only leads and sources without an OSS, protected-identifier, rank, unit or personnel-file bridge were rejected. Historical occupation categories and military assignments were not converted into employers.",
                "research_notes": f"{detail} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain and archival searches were checked as applicable. The index page, official Army comparison, technical field definitions and every cited code-list page were inspected directly. The Bronxville and OSS awards PDFs were OCR-assisted only after source inspection, then checked against rendered page images. Code 993 was left uninterpreted. No search-result snippet was used as sole final evidence, no paywall or access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": "Review the indexed personnel file for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before wartime service.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b984-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-984-v1",
        "reviewer": "Before OSS Batch 984 evidence review",
        "sources": sources(),
        "organizations": organizations(),
        "affiliations": affiliations(),
        "claims": claims(),
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }
    EvidenceBundle.model_validate(bundle)
    OUTPUT.write_text(
        json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
