#!/usr/bin/env python3
"""Generate the reviewed Batch 977 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page479-melchiore-valeriano-to-william-van-cleef-"
    "review_batch-977_2026-10-30.json"
)

INDEX = "nara-index-b977"
ARMY = "army-bulk-b977"
TECH = "army-tech-b977"
CODES = "army-codes-b977"
VALLIMARESCU_LOC = "loc-vallimarescu-oral-history-b977"
VALLIMARESCU_ADST = "adst-vallimarescu-dominican-reader-b977"
VAN_BEUREN_TIME = "time-archbold-van-beuren-cue-b977"
VAN_BEUREN_CONGRESS = "congressional-record-archbold-van-beuren-b977"
VAN_BIESBROECK_UCHICAGO = "uchicago-van-biesbroeck-finding-aid-b977"
VAN_BIESBROECK_BAY_LEAVES = "bay-leaves-micheline-van-biesbroeck-b977"

HARVARD = "harvard-b977"
US_ARMY = "us-army-b977"
CUE = "cue-magazine-b977"


PEOPLE = {
    1: ("95a691b7-d95f-5e6f-a737-2aa82f15476e", "Melchiore Valeriano"),
    2: ("f96fa4a8-3df9-533f-a15f-f2cc2ed13a42", "Helen Valerius"),
    3: ("ac44646e-5c94-5090-92b3-8da69e883761", "Neal A Valiant"),
    4: ("b6ac172d-0919-5286-9637-2d6510182f02", "Edgar M Valk"),
    5: ("ba07fe40-ff1e-5c41-9a6f-a2657abc04c6", "Dale E Vallance"),
    6: ("03474dc7-0d37-5866-8c6d-a09f7134b64b", "Jean Vallery"),
    7: ("d469ff8c-4692-5809-befe-c96f9057693b", "Armand I Vallieres"),
    8: ("cc2ab2ea-3666-5a30-bd9d-6ed30780161e", "Serban Vallimarescu"),
    9: ("e8c77f21-eceb-562a-872b-06fa0bc02bca", "A Valusis"),
    10: ("9f2f9334-22dd-54e6-bb2b-402a9369480f", "Marcos Valvis"),
    11: ("88b9fdac-9570-56a0-887e-693dfc275d6f", "William L Van Alen"),
    12: ("0598817d-ded2-53ba-a6d1-c70edba42a6c", "Greta Van Antwerp"),
    13: ("3e9f09d0-2a84-505f-ae59-60b1ae8dd865", "Gerhard P Van Arkel"),
    14: ("0ecf5a46-6eab-5031-9a99-91762e876b8e", "Ruth B Van Arkel"),
    15: ("160528a9-bcfb-5d1c-9245-f13b211a484b", "Albert H Van Arsdale"),
    16: ("d63972d5-780e-5713-acb9-ba6f80f56d1f", "Douglas W Van Arsdale"),
    17: ("56e73541-eae0-539c-8d04-9d72435da777", "Charles J Van Bergen"),
    18: ("70551449-2677-5354-a80d-54f9453361f9", "Archbold Van Beuren"),
    19: ("1bf6cea5-af41-5643-99f0-b10932a33e0e", "Micheline Van Biesbroec"),
    20: ("4b330868-c4c6-5535-904a-1ba64479343a", "Cornelius C Van Boecop"),
    21: ("d09fe90c-ed61-5f4f-b0ca-6c41689f5b63", "Frank Van Brunt"),
    22: ("baad67f6-7232-5fcd-8074-dd069c5119e5", "Delbert E Van Camplear"),
    23: ("a1f63a96-6d2f-53c0-8a5e-ded8307cd190", "William R Van Cleef"),
}

NEXT_WILLIAM_VAN_CLEEF = "9db44dbe-b1b5-5303-8d36-819031afc12c"
DUPLICATE_GROUP = "page479-william-r-van-cleef-boxes-797-798"


ARMY_OCCUPATIONS = [
    {
        "row": 3,
        "date": "1943-09-08",
        "code": "749",
        "occupation": "Transportation occupations, not elsewhere classified",
        "public_occupation": "transportation worker, not elsewhere classified",
        "relationship_type": "unknown",
        "locator": "PDF physical page 174; category 7-49 Transportation occupations, n.e.c.",
    },
    {
        "row": 7,
        "date": "1942-10-27",
        "code": "992",
        "occupation": "Students",
        "public_occupation": "student",
        "relationship_type": "student",
        "locator": "Corrected Code No. 30, PDF physical page 304; category 9-92 Students",
    },
    {
        "row": 10,
        "date": "1943-05-13",
        "code": "736",
        "occupation": "Chauffeurs and drivers, bus, taxi, truck, and tractor",
        "public_occupation": "chauffeur or driver",
        "relationship_type": "unknown",
        "locator": "PDF physical page 174; category 7-36 Chauffeurs and drivers, bus, taxi, truck, and tractor",
    },
    {
        "row": 21,
        "date": "1942-09-26",
        "code": "066",
        "occupation": "Technicians, except laboratory",
        "public_occupation": "technician, except laboratory",
        "relationship_type": "unknown",
        "locator": "PDF physical page 171; category 0-66 Technicians, except laboratory",
    },
]


UNRESOLVED = {
    1: "Exact-name and spelling-variant searches produced no reliable identity or pre-OSS affiliation for Melchiore Valeriano.",
    2: "Exact-name official, institutional, newspaper, obituary and archival searches produced no reliable identity bridge for Helen Valerius.",
    4: "Exact-name and middle-initial searches produced no source with the corroborating identifiers needed to resolve Edgar M Valk.",
    5: "Exact-name official, institutional, military and newspaper searches produced no reliable identity bridge for Dale E Vallance.",
    6: "Exact-name and spelling-variant searches produced no defensible identity or pre-OSS affiliation for Jean Vallery.",
    9: "The initials-only form A Valusis is insufficiently distinctive, and reviewed searches produced no source with two corroborating identifiers.",
    11: "A prominent architect with the same name is a plausible namesake, but no reviewed source connects him to Box 797 or OSS; the lead was rejected.",
    12: "Exact-name official, institutional, obituary, newspaper and archival searches produced no reliable identity bridge for Greta Van Antwerp.",
    13: "Exact-name and spelling-variant searches produced no reliable identity or pre-OSS affiliation for Gerhard P Van Arkel.",
    14: "Exact-name and spelling-variant searches produced no reliable identity or pre-OSS affiliation for Ruth B Van Arkel.",
    15: "The index supplies Sergeant rank, but searches did not identify a source that bridges Albert H Van Arsdale to a named pre-OSS employer.",
    16: "Exact-name official, military, institutional, newspaper and archival searches produced no reliable identity bridge for Douglas W Van Arsdale.",
    17: "Exact-name and spelling-variant searches produced no source with the corroborating identifiers needed to resolve Charles J Van Bergen.",
    20: "A Dutch colonial-aviation namesake is plausible, but discovery sources do not establish that he is the indexed person; the lead remains unaccepted.",
    22: "Exact-name and spelling-variant searches produced no reliable identity or pre-OSS affiliation for Delbert E Van Camplear; the clipped index note remains unresolved.",
    23: "The index contains a second William R Van Cleef in a different box; no source establishes duplication or identifies either man's pre-OSS affiliation.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 796-798",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 479, rows 1-23; checked against layout-preserving text and an original-detail page render",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate; literal spellings, rank, clipped notes and the adjacent duplicate-name row are preserved.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; four Batch 977 identity comparisons; protected identifiers and record ordinals withheld",
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
            "locator": "PDF physical pages 171 and 174 plus corrected page 304; Batch 977 categories visually and textually checked",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical categories identify neither employers nor workplaces and are retained only where needed for auditability.",
        },
        {
            "key": VALLIMARESCU_LOC,
            "stable_url": "https://tile.loc.gov/storage-services/service/mss/mfdip/2004/2004val03/2004val03.pdf",
            "archival_identifier": "Library of Congress item mfdipbib001210",
            "title": "Interview with Serban Vallimarescu",
            "author_creator": "Cliff Groce, interviewer; Serban Vallimarescu, interviewee",
            "repository_publisher": "Association for Diplomatic Studies and Training; Library of Congress",
            "publication_record_date": "Interview begun 1989-05-25; copyright 1998",
            "locator": "Pages 1-2 and 7: Army and Allied Control Commission chronology, explicit OSS recollection, and Harvard attendance",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Frontline Diplomacy: The Foreign Affairs Oral History Collection",
        },
        {
            "key": VALLIMARESCU_ADST,
            "stable_url": "https://adst.org/Readers/Dominican-Republic.pdf",
            "title": "Dominican Republic Country Reader",
            "author_creator": "Association for Diplomatic Studies and Training",
            "repository_publisher": "Association for Diplomatic Studies and Training",
            "publication_record_date": "Compiled oral-history reader",
            "locator": "Serban Vallimarescu biographical header: Harvard BA 1942 and U.S. Army lieutenant service, 1942-1945",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Foreign Affairs Oral History Collection country readers",
        },
        {
            "key": VAN_BEUREN_TIME,
            "stable_url": "https://time.com/archive/6761789/the-press-gentlemen-all/",
            "title": "The Press: Gentlemen All",
            "author_creator": "TIME editorial staff",
            "repository_publisher": "TIME",
            "publication_record_date": "1939-08-21",
            "locator": "Contemporary account of Archbold Van Beuren joining Cue and promoting the publication in metropolitan New York",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "TIME archive",
        },
        {
            "key": VAN_BEUREN_CONGRESS,
            "stable_url": "https://www.govinfo.gov/content/pkg/GPO-CRECB-1950-pt5/pdf/GPO-CRECB-1950-pt5-12-1.pdf",
            "archival_identifier": "Congressional Record, 81st Congress, May 9, 1950",
            "title": "Congressional Record: Proceedings and Debates of the 81st Congress, Second Session",
            "author_creator": "United States Congress; reprinted Washington Daily News article",
            "repository_publisher": "U.S. Government Publishing Office",
            "publication_record_date": "1950-05-09",
            "locator": "Reprinted contemporary reporting identifies Archbold van Beuren as an OSS security chief",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Congressional Record",
        },
        {
            "key": VAN_BIESBROECK_UCHICAGO,
            "stable_url": "https://www.lib.uchicago.edu/e/scrc/findingaids/view.php?eadid=ICU.SPCL.VANBIESBROECKG",
            "archival_identifier": "ICU.SPCL.VANBIESBROECKG",
            "title": "George Van Biesbroeck Papers, 1910-1975: Finding Aid",
            "author_creator": "University of Chicago Library, Hanna Holborn Gray Special Collections Research Center",
            "repository_publisher": "University of Chicago Library",
            "publication_record_date": "Finding aid",
            "locator": "Biographical note names daughter Micheline Van Biesbroeck and places the family at Williams Bay",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "University of Chicago Library finding aids",
        },
        {
            "key": VAN_BIESBROECK_BAY_LEAVES,
            "stable_url": "https://asset.library.wisc.edu/1711.dl/IW5C5VQXQYORB82/E/file-777f2.pdf?dl=",
            "title": "The Wisconsin Bay Leaves",
            "author_creator": "Williams Bay High School editorial staff",
            "repository_publisher": "Williams Bay High School; University of Wisconsin Digital Collections",
            "publication_record_date": "1933-06-01",
            "locator": "Senior class play and high-school graduation context naming Micheline Van Biesbroeck",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Wisconsin Local History and Biography Articles",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": HARVARD,
            "organization_id": "45ddf347-21c6-59f5-a8ae-517418adf941",
            "canonical_name": "Harvard University",
            "historical_name": "Harvard University",
            "aliases": ["Harvard"],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "Cambridge",
            "state_or_region": "Massachusetts",
            "country": "United States",
            "normalization_notes": "Existing canonical organization reused; attendance remains student status and is never silently converted into employment.",
        },
        {
            "key": US_ARMY,
            "organization_id": "28a26f92-78af-5a1a-9c09-a843eb5975b4",
            "canonical_name": "United States Army",
            "historical_name": "Army of the United States",
            "aliases": ["U.S. Army"],
            "organization_type": "military service",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "Existing canonical organization reused; military assignment remains distinct from civilian employment.",
        },
        {
            "key": CUE,
            "canonical_name": "Cue magazine",
            "historical_name": "Cue",
            "aliases": ["Cue New York"],
            "organization_type": "entertainment listings magazine",
            "sector": "journalism_and_media",
            "city": "New York",
            "state_or_region": "New York",
            "country": "United States",
            "active_dates": "Founded in 1932; Archbold Van Beuren documented in 1939",
            "normalization_notes": "The historical magazine is preserved as Cue; the source establishes a professional business affiliation but not a formal employee title.",
        },
    ]


def occupation_affiliation(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    name = PEOPLE[row][1]
    return {
        "key": f"{slug(name)}-occupation-b977",
        "person_id": PEOPLE[row][0],
        "occupation": str(item["public_occupation"]),
        "relationship_type": str(item["relationship_type"]),
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
        "research_notes": "Official historical occupation or student category at Army entry; excluded from verified-employer analytics.",
    }


def affiliations() -> list[dict[str, object]]:
    values = [occupation_affiliation(item) for item in ARMY_OCCUPATIONS]
    values.extend(
        [
            {
                "key": "serban-vallimarescu-harvard-b977",
                "person_id": PEOPLE[8][0],
                "organization_key": HARVARD,
                "organization_name_as_found": "Harvard",
                "role_title": "student",
                "occupation": "undergraduate student",
                "relationship_type": "student",
                "start_date": "1940",
                "end_date": "1942",
                "date_precision": "Oral history places him at Harvard from 1940; the ADST biographical header gives BA 1942",
                "city": "Cambridge",
                "state_or_region": "Massachusetts",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Student status before Army service; Harvard is not classified as an employer.",
            },
            {
                "key": "serban-vallimarescu-army-b977",
                "person_id": PEOPLE[8][0],
                "organization_key": US_ARMY,
                "organization_name_as_found": "U.S. Army",
                "role_title": "lieutenant",
                "occupation": "Army officer",
                "relationship_type": "military_assignment",
                "start_date": "1942",
                "end_date": "1945",
                "date_precision": "ADST biographical header dates Army service 1942-1945; the index prints 1st Lt",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "temporal_relation_uncertain",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Military pathway evidence only; the reviewed sources do not establish the exact transfer into or assignment within OSS.",
            },
            {
                "key": "archbold-van-beuren-cue-b977",
                "person_id": PEOPLE[18][0],
                "organization_key": CUE,
                "organization_name_as_found": "Cue",
                "role_title": "promoter and business associate",
                "occupation": "magazine promoter",
                "relationship_type": "professional_affiliation",
                "start_date": "1939",
                "end_date": "1939",
                "date_precision": "A contemporary August 1939 profile describes his role but not its start or end dates",
                "city": "New York",
                "state_or_region": "New York",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "published",
                "research_notes": "The contemporary source establishes a professional business affiliation, not a formal employment contract or immediate OSS transition.",
            },
            {
                "key": "micheline-van-biesbroeck-williams-bay-b977",
                "person_id": PEOPLE[19][0],
                "organization_name_as_found": "Williams Bay High School",
                "role_title": "senior student",
                "occupation": "high-school student",
                "relationship_type": "student",
                "start_date": "1933",
                "end_date": "1933",
                "date_precision": "Contemporary June 1933 school publication",
                "city": "Williams Bay",
                "state_or_region": "Wisconsin",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "probable",
                "claim_confidence": "medium",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "publish_qualified",
                "research_notes": "Qualified student-status evidence for the documented spelling variant; not employment and not included in default analytics.",
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
                f"identity-{slug(name)}-army-b977",
                "identity",
                f"Indexed {name} is high-confidence matched to the official Army entry used for the dated occupation finding.",
                "The reviewed official Army comparison and a nonshared protected identifier support the match; the private identifier is not published.",
                army_identity_note(row),
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
                f"occupation-{slug(name)}-b977",
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
                f"{slug(name)}-occupation-b977",
                "publish_qualified",
            )
        )
    return values


def special_claims() -> list[dict[str, object]]:
    return [
        claim(
            8,
            "identity-serban-vallimarescu-b977",
            "identity",
            "Indexed Serban Vallimarescu is high-confidence matched to the Harvard graduate and U.S. Army lieutenant who recalled wartime service with OSS.",
            "The rare exact name, printed first-lieutenant rank and source-explicit OSS recollection form a coherent identity bridge.",
            "High confidence from an exceptionally distinctive exact name, matching commissioned rank and an institutional oral history explicitly placing him with OSS.",
            "The oral history and biographical header provide prewar education and wartime Army dates but not the exact OSS accession date.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": INDEX}, {"source_key": VALLIMARESCU_LOC}, {"source_key": VALLIMARESCU_ADST}],
            "The index note 'also AS' is preserved without interpretation; no employer is inferred from Harvard attendance or Army service.",
        ),
        claim(
            8,
            "student-serban-vallimarescu-harvard-b977",
            "other_pre_oss_affiliation",
            "Serban Vallimarescu attended Harvard and received a BA in 1942 before his documented wartime Army service.",
            "His oral history places him at Harvard from 1940, while the ADST biographical header records a Harvard BA in 1942 and Army service beginning that year.",
            "High-confidence rare-name and explicit OSS oral-history match.",
            "Strongly date-bounded before or at the start of Army service; student status is not employment.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": VALLIMARESCU_LOC}, {"source_key": VALLIMARESCU_ADST}],
            "Harvard is classified as a student institution and excluded from employer analytics.",
            "serban-vallimarescu-harvard-b977",
        ),
        claim(
            8,
            "military-serban-vallimarescu-army-b977",
            "other_pre_oss_affiliation",
            "Serban Vallimarescu served in the U.S. Army as a lieutenant from 1942 to 1945.",
            "The ADST biographical header dates the service and identifies his grade; the NARA index independently prints first lieutenant.",
            "High-confidence rare-name, rank and OSS-context match.",
            "Wartime military pathway; the exact relation between Army assignment and OSS service is not established.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": INDEX}, {"source_key": VALLIMARESCU_ADST}],
            "Military assignment is kept distinct from a civilian employer and from the still-unresolved immediate OSS predecessor.",
            "serban-vallimarescu-army-b977",
        ),
        claim(
            18,
            "identity-archbold-van-beuren-b977",
            "identity",
            "Indexed Archbold Van Beuren is high-confidence matched to the Cue magazine associate later identified in contemporary reporting as an OSS security chief.",
            "The exceptionally uncommon exact name links a 1939 Cue profile with a government-preserved reproduction of reporting about his OSS role.",
            "High confidence from the rare exact name and a direct OSS contextual bridge in contemporary reporting preserved by Congress.",
            "The sources establish 1939 professional activity and later OSS service but do not explicitly narrate the transition.",
            "C_reputable_contemporary_or_scholarly",
            "high",
            [{"source_key": INDEX}, {"source_key": VAN_BEUREN_TIME}, {"source_key": VAN_BEUREN_CONGRESS}],
            "The Congressional Record source is treated as preserved contemporary reporting, not as a personnel-file statement.",
        ),
        claim(
            18,
            "other-archbold-van-beuren-cue-b977",
            "other_pre_oss_affiliation",
            "Archbold Van Beuren joined Cue and promoted the magazine in metropolitan New York by 1939.",
            "A contemporary TIME profile describes his association with Cue and his role promoting the publication.",
            "High-confidence rare exact-name match corroborated by separate OSS-context evidence.",
            "Explicitly documented in 1939 before OSS, but not shown to be the immediate predecessor or a formal employment contract.",
            "C_reputable_contemporary_or_scholarly",
            "high",
            [{"source_key": VAN_BEUREN_TIME}, {"source_key": VAN_BEUREN_CONGRESS, "support_type": "context_only"}],
            "Classified as professional affiliation rather than employment and excluded from verified-employer analytics.",
            "archbold-van-beuren-cue-b977",
        ),
        claim(
            19,
            "identity-micheline-van-biesbroeck-b977",
            "identity",
            "Indexed Micheline Van Biesbroec is probably the Micheline Van Biesbroeck named in a University of Chicago finding aid and a 1933 Williams Bay school publication.",
            "The near-exact rare name and Williams Bay context support a probable spelling-variant match, but no reviewed source directly bridges the woman to OSS.",
            "Probable identity only: distinctive near-exact name and coherent institutional context, without a personnel-file, protected-identifier or explicit OSS bridge.",
            "The 1933 evidence is prewar but remote from OSS service.",
            "B_authoritative_institutional",
            "medium",
            [{"source_key": INDEX}, {"source_key": VAN_BIESBROECK_UCHICAGO}, {"source_key": VAN_BIESBROECK_BAY_LEAVES}],
            "The indexed spelling remains primary; Van Biesbroeck is retained as a source-documented variant and the conclusion is visibly qualified.",
            publication_status="publish_qualified",
        ),
        claim(
            19,
            "student-micheline-van-biesbroeck-b977",
            "other_pre_oss_affiliation",
            "Micheline Van Biesbroeck was a Williams Bay High School senior in 1933.",
            "A contemporary school publication names her in the senior-class and graduation context; the university finding aid corroborates the family and location.",
            "Probable spelling-variant identity, not confirmed OSS identity.",
            "Documented prewar student status; not an employer and not shown to be immediately before OSS.",
            "C_reputable_contemporary_or_scholarly",
            "medium",
            [{"source_key": VAN_BIESBROECK_BAY_LEAVES}, {"source_key": VAN_BIESBROECK_UCHICAGO, "support_type": "context_only"}],
            "Published with qualification and excluded from default analytics.",
            "micheline-van-biesbroeck-williams-bay-b977",
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
        values.append(
            base_update(
                row,
                identity_status="ambiguous" if row in {11, 20, 23} else "unresolved",
                identity_evidence=f"The visually verified index row supplies {PEOPLE[row][1]}, a box number and archive location 230/86/42/04. {reason}",
                personnel_category="unknown_or_indeterminate",
                commissioned_officer=None,
                allied_or_foreign_personnel=None,
                possible_duplicate_group=DUPLICATE_GROUP if row == 23 else None,
                research_status="requires_archival_review",
                next_action=f"Review the indexed personnel file for corroborating identifiers, immediate pre-OSS affiliation and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}",
                archival_review_priority="critical" if row in {9, 11, 20, 23} else "high",
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
                8,
                identity_status="high_confidence",
                identity_evidence="The exceptionally distinctive exact name, printed first-lieutenant rank and Library of Congress oral history explicitly placing him with OSS support the identity.",
                personnel_category="commissioned_army_officer",
                commissioned_officer=True,
                allied_or_foreign_personnel=False,
                research_status="occupation_only_found",
                next_action="Review Box 796 to establish the exact OSS accession chronology and any named last civilian employer; Harvard attendance and Army service are not civilian employment.",
                archival_review_priority="medium",
            ),
            base_update(
                18,
                identity_status="high_confidence",
                identity_evidence="The exceptionally uncommon exact name links a contemporary 1939 Cue profile to government-preserved reporting that identifies Archbold van Beuren as an OSS security chief.",
                personnel_category="civilian_professional_or_administrative_grade",
                commissioned_officer=False,
                allied_or_foreign_personnel=None,
                research_status="completed",
                next_action="Review Box 797 if available to determine whether Cue immediately preceded OSS and whether the professional association was formal employment.",
                archival_review_priority="medium",
            ),
            base_update(
                19,
                identity_status="probable",
                identity_evidence="The rare near-exact name and Williams Bay context support a probable match to Micheline Van Biesbroeck, but no reviewed source directly bridges her to OSS.",
                name_variants=["Micheline Van Biesbroeck"],
                personnel_category="unknown_or_indeterminate",
                commissioned_officer=None,
                allied_or_foreign_personnel=None,
                research_status="requires_archival_review",
                next_action="Review Box 797 for direct identity evidence and later employment chronology; the 1933 school affiliation is qualified student status only.",
                archival_review_priority="critical",
            ),
            {
                "person_id": NEXT_WILLIAM_VAN_CLEEF,
                "manual_review_required": True,
                "possible_duplicate_group": DUPLICATE_GROUP,
            },
        ]
    )
    return values


def research_attempts() -> list[dict[str, object]]:
    reviewed_rows = {3, 7, 8, 10, 18, 19, 21}
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        if row in reviewed_rows:
            outcome = "source_reviewed"
            reviewed = 8 if row in {8, 18, 19} else 6
            rejected = 4
            detail = "Reviewed official, institutional or contemporary evidence produced the identity, occupation, student, military-pathway or professional-affiliation outcome recorded in the bundle."
        else:
            outcome = "no_result"
            reviewed = 6
            rejected = 6
            detail = UNRESOLVED[row]

        special_rejection = ""
        if row == 11:
            special_rejection = " The William Laurens Van Alen architect lead lacks an OSS or Box 797 bridge and was rejected."
        elif row == 19:
            special_rejection = " The spelling variant is published only as a probable identity and qualified 1933 student affiliation."
        elif row == 20:
            special_rejection = " Dutch aviation and genealogy leads lack an OSS or personnel-file bridge and remain unpublished."
        elif row == 23:
            special_rejection = " The adjacent same-name person in Box 797 remains separate and is flagged for duplicate review rather than merged."

        attempts.append(
            {
                "key": f"page479-row{row}-{slug(name)}-b977",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index and official Archives context; CIA Reading Room or equivalent official-source context; exact-name and meaningful variants; OSS, Army, Navy, rank and unit clues; employer and occupation 1940; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Boxes 796-798; protected identifiers used only in private official-record comparison",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_977",
                "started_at": "2026-10-30T17:05:00Z",
                "completed_at": "2026-10-30T19:50:00Z",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search snippets, unsourced genealogy, people-finder pages, relatives, postwar-only employment leads and sources without an OSS, protected-identifier or personnel-file bridge were rejected. Historical occupation codes and military service were not silently converted into employers." + special_rejection,
                "research_notes": f"{detail} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain and archival searches were checked as applicable. CIA Reading Room exact-name searches returned no relevant result for the unresolved cohort; this negative search was not used to prove non-employment. The index page, Army bulk file, technical documentation and relevant occupation-code pages were inspected directly. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": "Review the indexed personnel file for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before wartime service.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b977-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-977-v1",
        "reviewer": "Before OSS Batch 977 evidence review",
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
