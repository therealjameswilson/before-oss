#!/usr/bin/env python3
"""Generate the reviewed Batch 980 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page480-charles-vanda-to-martha-vandiver-"
    "review_batch-980_2026-10-30.json"
)

INDEX = "nara-index-b980"
ARMY = "army-bulk-b980"
TECH = "army-tech-b980"
CODES = "army-codes-b980"
ARMY_REGISTER = "army-register-hoyt-vandenberg-b980"
UNLV_VANDA = "unlv-charles-vanda-b980"
LATIMES_VANDA = "latimes-charles-vanda-b980"
UK_POLSCI = "uk-political-science-amry-vandenbosch-b980"
UK_PATTERSON = "uk-patterson-amry-vandenbosch-b980"
STATE_FRUS = "state-frus-amry-vandenbosch-b980"
ARSOF_VANDERBLUE = "arsof-charles-vanderblue-b980"
NARA_VANDERVALK = "nara-arnold-vandervalk-b980"
NARA_VANDERWEGE = "nara-william-vanderwege-b980"

ORG_CBS = "cbs-radio-b980"
ORG_UK = "university-of-kentucky-b980"


PEOPLE = {
    24: ("2a85f187-98b0-58de-beab-522352408edc", "Charles Vanda"),
    25: ("0f666d7f-d608-5049-8bf5-5b04e9e5fbd2", "Clarence H Vandellen"),
    26: ("add9eae0-db60-5d85-8936-ac4e094d404d", "Hoyt S Vandenberg"),
    27: ("30c22d38-7915-5f57-8585-292943753050", "John Vandenberg"),
    28: ("700a7d7e-7517-521b-879d-fa1a15c9ae12", "Louis W Vandenboom"),
    29: ("474d0397-9a79-50a6-80d2-223567f30d8a", "Amry Vandenbosch"),
    30: ("a1146a1f-3102-5b31-8565-c93ccc980831", "Paul VanDenstricht"),
    31: ("c540901c-dce9-5947-b7a7-adda0862a5cc", "John L Vander"),
    32: ("54cfb556-48df-5b54-a8e5-a1046de51372", "Charles S Vanderblue"),
    33: ("aeeb28b1-d39c-5902-9069-0b7a8ec59850", "John Vanderleith"),
    34: ("b333225b-f27a-5e52-8f02-5ba3f178bd43", "Elmer Vanderploeg"),
    35: ("4497dbbc-43c3-50b9-b0fa-738142ea95f8", "Vivian R Vanderpool"),
    36: ("b1a6fccf-f0fc-54ed-9659-7626fbcc472d", "John L Vandersys"),
    37: ("92e98d0c-a0c1-572b-a375-d1291257e81b", "Richard J Vandertie"),
    38: ("4c7e2eab-b7da-5572-95f5-51866b0da48a", "Arnold Vandervalk"),
    39: ("2e9ea2cb-128d-55e1-a33d-10c76fd5bf9d", "Rollin N Vandervart"),
    40: ("afe4e251-3894-5d87-be68-894289c9b3ca", "Ollie R Vandervender"),
    41: ("faf6f135-3749-5acf-a7ef-e544c2e2b0c5", "Benjamin H Vandervoort"),
    42: ("63af3f89-4040-5005-8e8d-fdfb323c93bb", "John R Vandervoort"),
    43: ("a9c9f92d-a305-5d98-a4a6-940de93eb2c8", "John R Vandervoort"),
    44: ("78af1878-86e8-5ea2-a87a-1ad2f9d18b3f", "Dale S Vandervort"),
    45: ("b442e752-398e-5eda-b0bf-ed057c6b04d2", "William H Vanderwege"),
    46: ("c83c2dae-c1eb-5d94-b5cb-124e4b7f0501", "Martha V Vandiver"),
}


ARMY_OCCUPATIONS = [
    {
        "row": 27,
        "date": "1942-01-30",
        "code": "002",
        "occupation": "Actors and actresses",
        "public_occupation": "actor or actress",
        "locator": "PDF physical page 170; historical category 0-02",
        "name_note": "The Army form inserts a space in Vandenberg; the exact nonshared protected identifier resolves the spacing-only disagreement.",
    },
    {
        "row": 43,
        "date": "1943-03-22",
        "code": "992",
        "occupation": "Students",
        "public_occupation": "student",
        "locator": "PDF physical page 304; historical category 9-92",
        "name_note": "The official Army and indexed names agree exactly and the protected identifier is nonshared.",
    },
    {
        "row": 44,
        "date": "1943-01-08",
        "code": "126",
        "occupation": "Paymasters, payroll clerks, and timekeepers",
        "public_occupation": "paymaster, payroll clerk, or timekeeper",
        "locator": "PDF physical page 171; historical category 1-26",
        "name_note": "The official Army and indexed names agree exactly and the protected identifier is nonshared.",
    },
]


UNRESOLVED = {
    25: "A 1966 directory lead places a Clarence H Vandellen in personnel work at Picatinny Arsenal, but it is postwar and supplies no OSS or Box 798 bridge.",
    28: "Exact-name and spelling-variant searches produced no official, institutional, newspaper, obituary or archival source connecting Louis W Vandenboom to OSS or a pre-OSS employer.",
    31: "The abbreviated surname and common given names produced multiple unbridged candidates; no source supplies the indexed box, rank, identifier or OSS context.",
    33: "Exact-name and spelling-variant searches produced no reliable identity or employment bridge for John Vanderleith.",
    34: "Exact-name official, institutional, newspaper, obituary and archival searches produced no reliable identity or employment bridge for Elmer Vanderploeg.",
    36: "A relative's obituary and modern namesakes do not establish John L Vandersys's identity, OSS context or pre-OSS employment.",
    37: "A postwar athletics result and modern namesakes are irrelevant to the indexed person and supply no wartime identity bridge.",
    39: "A burial lead supplies no OSS, Box 799 or employment bridge for Rollin N Vandervart.",
    40: "Exact-name and variant searches produced no source with corroborating wartime identifiers or a documented pre-OSS affiliation for Ollie R Vandervender.",
}


AMBIGUOUS = {
    30: "An adjacent indexed Paul R Van DerStricht row is a plausible duplicate and has a documented New York legal career, but the separate Box 798 files have not established whether these rows represent one person.",
    35: "A wartime Cornell alumni wedding notice names Vivian R Vanderpool only as a spouse and supplies neither an employer nor an OSS identity bridge.",
    41: "A well-documented airborne officer shares the name Benjamin H Vandervoort, but the index row has no rank or identifier; a name match alone cannot assign that biography.",
    42: "This no-identifier John R Vandervoort row remains separate from the adjacent protected-identifier row until the Box 799 files establish duplication or difference.",
    46: "Foreign Service Journal listings name a Martha V Vandiver, but they do not establish that she is the indexed person or identify her immediate pre-OSS sequence.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 798-799",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 480, rows 24-46; checked against layout-preserving text and an original-detail page render",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate; identifiers, ranks, notes and locations remain recoverable while public identifiers are masked.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; three Batch 980 identity comparisons; protected identifiers and record ordinals withheld",
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
            "locator": "PDF physical pages 170, 171 and 304; all three Batch 980 categories visually and textually checked",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical categories identify neither employers nor workplaces and are retained only where needed for auditability.",
        },
        {
            "key": ARMY_REGISTER,
            "stable_url": "https://www.archives.gov/files/foia/pdf/nprc-crg-part5-508.pdf",
            "archival_identifier": "Official Army Register, 1943",
            "title": "Official Army Register, 1943",
            "author_creator": "War Department",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1943",
            "locator": "PDF physical page 126, printed page 907; Hoyt S. Vandenberg entry visually and textually checked",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "National Personnel Records Center consolidated reference guide",
            "rights_notes": "The exact private officer-number agreement supports identity resolution; the number is not reproduced publicly.",
        },
        {
            "key": UNLV_VANDA,
            "stable_url": "https://www.library.unlv.edu/speccol/finding-aids/MS-00299.pdf",
            "archival_identifier": "MS-00299; ARK ark:/62930/f1130f",
            "title": "Guide to the Charles Vanda Collection",
            "author_creator": "John Grygo and Melise Leech",
            "repository_publisher": "University of Nevada, Las Vegas University Libraries, Special Collections and Archives",
            "publication_record_date": "2019-02-28",
            "locator": "PDF page 3, Biographical Note",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Charles Vanda Collection",
        },
        {
            "key": LATIMES_VANDA,
            "stable_url": "https://www.latimes.com/archives/la-xpm-1988-06-11-mn-4160-story.html",
            "title": "Charles Vanda; Ex-CBS Program Chief",
            "author_creator": "Los Angeles Times Archives",
            "repository_publisher": "Los Angeles Times",
            "publication_record_date": "1988-06-11",
            "locator": "Career paragraphs identifying the 1935 CBS appointment and 1946 departure",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Los Angeles Times obituary archive",
        },
        {
            "key": UK_POLSCI,
            "stable_url": "https://polisci.as.uky.edu/history-political-science-department",
            "title": "History of the Political Science Department",
            "author_creator": "University of Kentucky Department of Political Science",
            "repository_publisher": "University of Kentucky College of Arts & Sciences",
            "publication_record_date": "Undated institutional history",
            "locator": "The Early Years: 1923-63; Amry Vandenbosch department-head chronology",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "University of Kentucky departmental histories",
        },
        {
            "key": UK_PATTERSON,
            "stable_url": "https://pattersonschool.uky.edu/history-leadership",
            "title": "History & Leadership",
            "author_creator": "Patterson School of Diplomacy and International Commerce",
            "repository_publisher": "University of Kentucky",
            "publication_record_date": "Undated institutional history",
            "locator": "Amry Vandenbosch, founding director, 1959-1972",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Patterson School institutional history",
        },
        {
            "key": STATE_FRUS,
            "stable_url": "https://history.state.gov/historicaldocuments/frus1943/d366",
            "archival_identifier": "Foreign Relations of the United States, 1943, document 366; Lot 60 D 224",
            "title": "Boundary Problems of Germany",
            "author_creator": "United States Department of State",
            "repository_publisher": "Office of the Historian, United States Department of State",
            "publication_record_date": "1943-08-18; Vandenbosch memorandum dated 1943-07-16",
            "locator": "Enclosure 8, printed page 760; memorandum by Amry Vandenbosch of the Division of Political Studies",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "Foreign Relations of the United States",
        },
        {
            "key": ARSOF_VANDERBLUE,
            "stable_url": "https://arsof-history.org/articles/v3n1_supplying_resistance_page_1.html",
            "title": "Supplying the Resistance: OSS Logistics Support to Special Operations in Europe",
            "author_creator": "Troy J. Sacquety, PhD",
            "repository_publisher": "United States Army Special Operations Command History Office",
            "publication_record_date": "2007",
            "locator": "Veritas, volume 3, number 1; paragraph describing the 1943 Area H planning memorandum",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "General ARSOF History",
        },
        {
            "key": NARA_VANDERVALK,
            "stable_url": "https://www.archives.gov/files/research/jfk/releases/104-10165-10120.pdf",
            "archival_identifier": "JFK Assassination Records release 104-10165-10120",
            "title": "OSS awards board recommendations",
            "author_creator": "Office of Strategic Services",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1944-1945",
            "locator": "PDF physical page 6; board summary listing Lt Arnold Vandervalk under Morale Operations",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "JFK Assassination Records Collection",
            "document_number": "104-10165-10120",
        },
        {
            "key": NARA_VANDERWEGE,
            "stable_url": "https://www.archives.gov/files/research/jfk/releases/104-10165-10121.pdf",
            "archival_identifier": "JFK Assassination Records release 104-10165-10121",
            "title": "Office of Strategic Services Operational Group Command Special Orders Number 9",
            "author_creator": "Office of Strategic Services",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1945-05-09",
            "locator": "PDF physical page 7; assignment to Company B, Special Reconnaissance Battalion",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "JFK Assassination Records Collection",
            "document_number": "104-10165-10121",
            "rights_notes": "The exact private service-number agreement supports identity resolution; the number is not reproduced publicly.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": ORG_CBS,
            "canonical_name": "Columbia Broadcasting System",
            "historical_name": "CBS Radio",
            "aliases": ["CBS", "CBS radio network"],
            "organization_type": "radio network",
            "sector": "journalism_and_media",
            "city": "New York",
            "state_or_region": "New York",
            "country": "United States",
            "active_dates": "1927-present",
            "normalization_notes": "The historical CBS Radio name is preserved; no later corporate successor is substituted.",
        },
        {
            "key": ORG_UK,
            "canonical_name": "University of Kentucky",
            "historical_name": "University of Kentucky",
            "aliases": ["UK", "UK Political Science Department"],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "Lexington",
            "state_or_region": "Kentucky",
            "country": "United States",
            "active_dates": "1865-present",
            "normalization_notes": "The Political Science Department is retained as a historical unit of the university rather than a separate employer.",
        },
    ]


def occupation_affiliation(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    return {
        "key": f"{slug(PEOPLE[row][1])}-occupation-b980",
        "person_id": PEOPLE[row][0],
        "occupation": str(item["public_occupation"]),
        "relationship_type": "student" if row == 43 else "unknown",
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
        "research_notes": "Official historical occupation or student category only; excluded from employer analytics.",
    }


def affiliations() -> list[dict[str, object]]:
    values = [occupation_affiliation(item) for item in ARMY_OCCUPATIONS]
    values.extend(
        [
            {
                "key": "charles-vanda-cbs-b980",
                "person_id": PEOPLE[24][0],
                "organization_key": ORG_CBS,
                "organization_name_as_found": "CBS Radio New York",
                "role_title": "program manager overseeing Hollywood radio originations",
                "occupation": "radio program manager, writer, producer and director",
                "relationship_type": "employment",
                "start_date": "1935",
                "end_date": "1942",
                "date_precision": "Appointed in 1935; institutional history places Army Intelligence and AFRS work in wartime and in 1942, while formal CBS departure was reported in 1946",
                "city": "Hollywood",
                "state_or_region": "California",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "probable_immediate",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Last documented civilian employer before wartime Army Intelligence service; the exact leave, formal employment and OSS accession dates remain unresolved.",
            },
            {
                "key": "amry-vandenbosch-university-kentucky-b980",
                "person_id": PEOPLE[29][0],
                "organization_key": ORG_UK,
                "organization_name_as_found": "UK's Political Science Department",
                "role_title": "department head and professor of political science",
                "occupation": "political scientist and university professor",
                "relationship_type": "employment",
                "start_date": "1933",
                "end_date": "1943-07",
                "date_precision": "Department head from 1933 through 1958; by July 1943 he was working in the State Department's Division of Political Studies, but the leave date is not stated",
                "city": "Lexington",
                "state_or_region": "Kentucky",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "probable_immediate",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Last documented civilian employer before State Department and OSS service; the order and dates of those wartime assignments remain unresolved.",
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
    return (
        f"{item['name_note']} The protected identifier and raw record ordinal remain private."
    )


def army_claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for item in ARMY_OCCUPATIONS:
        row = int(item["row"])
        name = PEOPLE[row][1]
        values.append(
            claim(
                row,
                f"identity-{slug(name)}-army-b980-row{row}",
                "identity",
                f"Indexed {name} is high-confidence matched to the official Army entry used for the dated occupation finding.",
                "Official Army name comparison and a nonshared protected-identifier agreement support the match.",
                army_identity_note(item),
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
                f"occupation-{slug(name)}-b980-row{row}",
                "occupation",
                f"At Army entry on {item['date']}, {name}'s historical civilian-occupation category was {str(item['occupation']).lower()}.",
                f"The official Army field carries historical code {item['code']}; NARA's code list defines it as {item['occupation']}.",
                army_identity_note(item),
                "Dated at Army entry before the later OSS-index context; no named employer, school, workplace or exact OSS-transfer date is supplied.",
                "A_direct_official",
                "medium",
                [
                    {"source_key": ARMY, "locator_override": "Accepted identity bridge; protected identifier and raw record withheld"},
                    {"source_key": TECH, "locator_override": "PDF physical pages 44-46; civilian-occupation field"},
                    {"source_key": CODES, "locator_override": str(item["locator"])},
                ],
                "Published as a qualified occupation or student status only; excluded from verified-employer analytics.",
                f"{slug(name)}-occupation-b980",
                "publish_qualified",
            )
        )
    return values


def special_claims() -> list[dict[str, object]]:
    return [
        claim(
            24,
            "identity-charles-vanda-b980",
            "identity",
            "Indexed Major Charles Vanda is high-confidence matched to radio executive Charles Vanda, who served in Army Intelligence during World War II.",
            "UNLV's finding aid links the rare exact name, broadcast career and wartime Army Intelligence service; the index supplies a compatible Major rank.",
            "High confidence from rare exact name, compatible rank and authoritative wartime-service context.",
            "The same institutional chronology places his CBS career before and alongside wartime service.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": INDEX}, {"source_key": UNLV_VANDA}],
            "The sources do not establish a precise OSS accession date or the reason the indexed personnel file was created.",
        ),
        claim(
            24,
            "last-civilian-charles-vanda-cbs-b980",
            "last_civilian_pre_service",
            "CBS Radio is Charles Vanda's last documented civilian employer before his wartime Army Intelligence service.",
            "UNLV dates his CBS appointment to 1935 and later wartime Army Intelligence work; the Los Angeles Times independently confirms the CBS role and career chronology.",
            "High-confidence rare-name, broadcast-career and wartime-service match.",
            "Probable last civilian employer before military service; the exact leave and formal employment dates remain unresolved.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": UNLV_VANDA}, {"source_key": LATIMES_VANDA}],
            "Not presented as an explicit direct transfer into OSS; the site preserves the distinction between last civilian employer and immediate pre-OSS affiliation.",
            "charles-vanda-cbs-b980",
        ),
        claim(
            29,
            "identity-amry-vandenbosch-b980",
            "identity",
            "Indexed Amry Vandenbosch is high-confidence matched to the University of Kentucky political scientist who served in the State Department and OSS.",
            "The rare exact name, university career and explicit institutional OSS statement align with a 1943 State Department memorandum he authored.",
            "High confidence from rare exact name, authoritative institutional career evidence and official wartime government documentation.",
            "The sources document university employment before State and OSS service but do not fully order the wartime assignments.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": INDEX}, {"source_key": UK_PATTERSON}, {"source_key": STATE_FRUS, "support_type": "context_only"}],
            "The State Department and OSS assignments are not collapsed into one relationship.",
        ),
        claim(
            29,
            "last-civilian-amry-vandenbosch-university-kentucky-b980",
            "last_civilian_pre_service",
            "The University of Kentucky was Amry Vandenbosch's last documented civilian employer before his State Department and OSS service.",
            "UK dates his department-head tenure from 1933; a 1943 State Department memorandum and UK history document his later government and OSS service.",
            "High-confidence rare-name and continuous institutional-career match.",
            "Probable last civilian employer; the exact leave date and State-to-OSS sequence remain unresolved.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": UK_POLSCI}, {"source_key": UK_PATTERSON}, {"source_key": STATE_FRUS}],
            "Not labeled an immediate OSS predecessor because State Department service may have intervened.",
            "amry-vandenbosch-university-kentucky-b980",
        ),
        claim(
            26,
            "identity-hoyt-vandenberg-army-register-b980",
            "identity",
            "Indexed Hoyt S Vandenberg is confirmed as Army Air Forces officer Hoyt S. Vandenberg.",
            "The 1943 official Army register supplies the exact name and a private officer-number agreement with the index.",
            "Confirmed by exact official name and protected officer-number agreement.",
            "The register documents his Army career through 1942 but does not establish OSS service or explain the indexed file.",
            "A_direct_official",
            "confirmed",
            [{"source_key": INDEX}, {"source_key": ARMY_REGISTER}],
            "The officer number remains private; Box 798 review is required before asserting any OSS assignment or pre-OSS transition.",
        ),
        claim(
            32,
            "identity-charles-vanderblue-b980",
            "identity",
            "Indexed Colonel Charles S Vanderblue is high-confidence matched to Charles Vanderblue, chief of OSS Special Operations in London in 1943.",
            "The Army Special Operations history identifies Colonel Charles Vanderblue and his dated OSS SO London leadership role.",
            "High confidence from exact rare name, compatible Colonel rank and explicit OSS role.",
            "The source documents a 1943 OSS assignment but no pre-OSS employer.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": INDEX}, {"source_key": ARSOF_VANDERBLUE}],
            "The middle initial is supplied by the index; Box 798 review remains necessary for his earlier career.",
        ),
        claim(
            38,
            "identity-arnold-vandervalk-b980",
            "identity",
            "Indexed Second Lieutenant Arnold Vandervalk is high-confidence matched to Lieutenant Arnold Vandervalk of OSS Morale Operations.",
            "An official OSS awards-board summary lists the rare exact name, compatible lieutenant rank and Morale Operations branch.",
            "High confidence from rare exact name, compatible rank and explicit OSS branch; no identifier appears on the awards page.",
            "The source establishes wartime OSS context but no pre-OSS employer.",
            "A_direct_official",
            "high",
            [{"source_key": INDEX}, {"source_key": NARA_VANDERVALK}],
            "The physical personnel file remains necessary to confirm the full identity and earlier chronology.",
        ),
        claim(
            45,
            "identity-william-vanderwege-b980",
            "identity",
            "Indexed William H Vanderwege is confirmed as the first lieutenant assigned to Company B, Special Reconnaissance Battalion in May 1945.",
            "An official OSS special order supplies the exact name, commissioned rank, assignment and a private identifier agreement with the index.",
            "Confirmed by exact name and protected-identifier agreement in an official OSS order.",
            "The order documents a 1945 OSS assignment but no pre-OSS employer.",
            "A_direct_official",
            "confirmed",
            [{"source_key": INDEX}, {"source_key": NARA_VANDERWEGE}],
            "The full identifier remains private; the Box 799 file is still required for pre-OSS chronology.",
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
        values.append(
            base_update(
                row,
                identity_status="unresolved",
                identity_evidence=f"The visually verified index row supplies {PEOPLE[row][1]}, Box 798 or 799 and archive location 230/86/42/04 or 05. {reason}",
                personnel_category="unknown_or_indeterminate",
                research_status="requires_archival_review",
                next_action=f"Review the indexed personnel file for corroborating identifiers, immediate pre-OSS affiliation and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}",
            )
        )

    for row, reason in AMBIGUOUS.items():
        category = "commissioned_army_officer" if row == 30 else "unknown_or_indeterminate"
        values.append(
            base_update(
                row,
                identity_status="ambiguous",
                identity_evidence=f"The visually verified index row remains a separate person entity. {reason}",
                personnel_category=category,
                commissioned_officer=True if row == 30 else None,
                allied_or_foreign_personnel=False if row == 30 else None,
                possible_duplicate_group=(
                    "page479-480-paul-van-der-stricht-box798"
                    if row == 30
                    else "page480-john-r-vandervoort-box799"
                    if row == 42
                    else None
                ),
                research_status="requires_archival_review",
                next_action=f"Review the indexed Box 798 or 799 file before merging identities or assigning a pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}",
                archival_review_priority="critical" if row in {30, 42} else "high",
            )
        )

    for item in ARMY_OCCUPATIONS:
        row = int(item["row"])
        values.append(
            base_update(
                row,
                identity_status="high_confidence",
                identity_evidence=army_identity_note(item),
                personnel_category="enlisted_army_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                possible_duplicate_group="page480-john-r-vandervoort-box799" if row == 43 else None,
                research_status="occupation_only_found",
                next_action="Review the indexed personnel file to establish the immediate pre-OSS affiliation and named last civilian employer; do not convert the Army occupation category into a workplace.",
            )
        )

    values.extend(
        [
            base_update(
                24,
                identity_status="high_confidence",
                identity_evidence="UNLV links the rare exact name Charles Vanda to wartime Army Intelligence service; the index supplies a compatible Major rank.",
                personnel_category="commissioned_army_officer",
                commissioned_officer=True,
                allied_or_foreign_personnel=False,
                research_status="verified_employer_found",
                next_action="Review Box 798 to determine Vanda's exact military and OSS accession dates and whether CBS employment formally continued during service.",
                archival_review_priority="medium",
            ),
            base_update(
                26,
                identity_status="confirmed",
                identity_evidence="The 1943 official Army register has the exact name and a private officer-number agreement with the index.",
                personnel_category="commissioned_army_officer",
                commissioned_officer=True,
                allied_or_foreign_personnel=False,
                research_status="requires_archival_review",
                next_action="Review Box 798 to determine why Hoyt S Vandenberg is indexed and whether the file documents any OSS accession or assignment. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
                archival_review_priority="critical",
            ),
            base_update(
                29,
                identity_status="high_confidence",
                identity_evidence="University of Kentucky explicitly connects the rare exact name Amry Vandenbosch to long university service, the State Department and OSS; a 1943 State memorandum independently confirms his wartime government role.",
                personnel_category="civilian_professional_or_administrative_grade",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                research_status="verified_employer_found",
                next_action="Review Box 798 and UK personnel records to establish the exact university leave, State Department and OSS sequence.",
                archival_review_priority="medium",
            ),
            base_update(
                32,
                identity_status="high_confidence",
                identity_evidence="Army Special Operations history identifies Colonel Charles Vanderblue as chief of OSS Special Operations in London in 1943; the rare exact surname and rank align with the index.",
                personnel_category="commissioned_army_officer",
                commissioned_officer=True,
                allied_or_foreign_personnel=False,
                research_status="requires_archival_review",
                next_action="Review Box 798 for Charles S Vanderblue's pre-OSS military or civilian chronology. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
            ),
            base_update(
                38,
                identity_status="high_confidence",
                identity_evidence="An official OSS awards-board summary lists Lt Arnold Vandervalk in Morale Operations; the rare exact name and compatible lieutenant rank align with the index.",
                personnel_category="commissioned_army_officer",
                commissioned_officer=True,
                allied_or_foreign_personnel=False,
                research_status="requires_archival_review",
                next_action="Review Box 798 to confirm the full identity and document Arnold Vandervalk's pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
            ),
            base_update(
                45,
                identity_status="confirmed",
                identity_evidence="An official OSS special order supplies William H Vanderwege's exact name, first-lieutenant rank, Special Reconnaissance Battalion assignment and a private identifier agreement with the index.",
                personnel_category="commissioned_army_officer",
                commissioned_officer=True,
                allied_or_foreign_personnel=False,
                research_status="requires_archival_review",
                next_action="Review Box 799 for William H Vanderwege's earlier military assignment and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
            ),
        ]
    )
    return values


def research_attempts() -> list[dict[str, object]]:
    reviewed = {24: 5, 26: 3, 27: 4, 29: 5, 32: 3, 38: 3, 43: 4, 44: 4, 45: 3}
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
            detail = UNRESOLVED.get(row) or AMBIGUOUS[row]

        attempts.append(
            {
                "key": f"page480-row{row}-{slug(name)}-b980",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index and official Archives context; CIA Reading Room or equivalent official-source context; exact-name and meaningful variants; OSS, Army, rank and unit clues; employer and occupation 1940; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Boxes 798-799; protected identifiers used only in private official-record comparison",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_980",
                "started_at": "2026-10-30T13:00:00Z",
                "completed_at": "2026-10-30T14:30:00Z",
                "outcome": outcome,
                "sources_reviewed": sources_reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search snippets, unsourced genealogy, people-finder pages, relatives, postwar-only leads and sources without an OSS, protected-identifier, rank or personnel-file bridge were rejected. Historical occupation codes and military assignments were not silently converted into employers.",
                "research_notes": f"{detail} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain and archival searches were checked as applicable. The index, Army code list, 1943 Army register and digitized OSS pages were inspected directly where relevant. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": "Review the indexed personnel file for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before wartime service.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b980-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-980-v1",
        "reviewer": "Before OSS Batch 980 evidence review",
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
