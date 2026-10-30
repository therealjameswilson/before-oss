#!/usr/bin/env python3
"""Generate the reviewed Batch 960 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page470-471-william-tommaselli-to-andrew-torrielli-"
    "review_batch-960_2026-10-29.json"
)

INDEX = "nara-index-b960"
ARMY = "army-bulk-b960"
TECH = "army-tech-b960"
CODES = "army-codes-b960"
TONER = "eisenhower-albert-toner-b960"
TONESK_OAC = "hoover-tonesk-finding-aid-b960"
TONESK_STANFORD = "stanford-tonesk-oss-b960"
AFI_TONG = "afi-kam-tong-b960"
MSU_TONGYAI = "msu-singkata-tongyai-b960"
TARTU_TONISSON = "tartu-heldur-tonisson-b960"
FHS_TORNEMAN = "fhs-algot-torneman-b960"
MUSEUM_TORNEMAN = "digitaltmuseum-algot-torneman-b960"
IFZ_TORRIELLI = "ifz-andrew-torrielli-b960"
CINII_TORRIELLI = "cinii-andrew-torrielli-b960"


PEOPLE = {
    "470-26": ("992b1460-7ac8-5143-bc1b-c6988825a7dd", "William Tommaselli"),
    "470-27": ("adb891cf-7fcb-566f-8f65-7cb03759880a", "James Tonas"),
    "470-28": ("01cdf4be-55c7-5363-8616-6c8d9c30396d", "Albert P Toner"),
    "470-29": ("8c2fa4a7-79ce-5cb6-94b2-bdd3a62d9cd6", "Williams Tonesk"),
    "470-30": ("09c6b8d8-d95e-5dd9-8159-157d75226ae8", "Cleo Toney"),
    "470-31": ("cefa0781-3205-501d-b471-654156ee46e7", "Henry K Tong"),
    "470-32": ("54afd4bf-9e0c-5128-8a61-8e95af05ab39", "Kam D Tong"),
    "470-33": ("e0c8562b-11de-5ec4-bd8a-f77ae1d09ec0", "Singkata Tongyai"),
    "470-34": ("e209f10a-8ffa-57b5-84ae-2bde8d0d6009", "Heldur Tonisson"),
    "470-35": ("bec54ce9-9f30-585f-a8d3-40f3d69056b9", "Bruce L Tonks"),
    "470-36": ("646b0a43-8828-59f5-ace4-c3b6eb7a5372", "Carlo D Tonno"),
    "470-37": ("cdf5e832-7e02-5d0f-8f95-1881bea19c97", "Signa E Toole"),
    "470-38": ("12d621e0-b818-599b-ba57-06d4ecc185ba", "Alfred G Toombs"),
    "470-39": ("0c3ec0ff-f10a-5996-b4b1-6559a737d997", "Clarence S Topp"),
    "470-40": ("37658069-28b0-5005-aa4d-853c327d6a29", "Dwight M Tordter"),
    "470-41": ("11073e78-1467-5b62-b48b-aaf3c14539ba", "Milton F Torem"),
    "470-42": ("8cb368fe-7899-505a-a7f3-42c0364eb8f1", "Jean T Torgerson"),
    "470-43": ("fddc196b-b62a-5af5-a926-57aa5bac6c74", "Alex J Torma"),
    "470-44": ("0df4d4e9-ca8d-520a-8c72-112be29ca903", "Algot Torneman"),
    "470-45": ("b6e24bd4-6a99-56f8-a4de-435dcb4a4639", "Norma E Tornquist"),
    "470-46": ("df1f03f6-c447-5815-9f14-937e93fea776", "Jack Torosky"),
    "471-1": ("55f01433-3660-5589-81e9-f7fdcd326074", "Christopher Torper"),
    "471-2": ("961cbce5-a593-57d3-a344-3b7094e38fe5", "Andrew J Torrielli"),
}


ARMY_PEOPLE = {
    "470-26": ("William Tommaselli", "1943-03-25", "736", "Chauffeurs and drivers, bus, taxi, truck, tractor", "175"),
    "470-30": ("Cleo Toney", "1942-04-25", "721", "Miners and mining-machine operators", "174"),
    "470-31": ("Henry K Tong", "1945-02-27", "072", "Retail managers", "170"),
    "470-41": ("Milton F Torem", "1943-05-04", "992", "Students", "304"),
    "470-43": ("Alex J Torma", "1942-06-22", "716", "Painters, except construction and maintenance", "174"),
    "470-46": ("Jack Torosky", "1943-03-10", "016", "Civil engineers", "170"),
    "471-1": ("Christopher Torper", "1942-10-26", "686", "Blacksmiths, forgemen, and hammermen", "176"),
}


UNRESOLVED = {
    "470-35": "Exact-name, middle-initial, OSS, occupation, obituary, institutional, newspaper and archival searches produced no defensible Box 781 identity bridge.",
    "470-36": "Exact-name and spelling-variant searches produced no reliable identity or pre-OSS affiliation beyond the index row.",
    "470-37": "Exact-name, middle-initial, obituary, institutional, newspaper and official-domain searches produced no defensible Box 781 identity bridge.",
    "470-38": "A same-name Virginia author and homeowner is a plausible lead, but no source supplies an OSS, Box 781 or second-identifier bridge.",
    "470-39": "A same-name World War II Army captain is plausible, but the accessible evidence does not connect him to Box 781 or document a pre-OSS affiliation.",
    "470-40": "The unusual printed surname, exact-name variants and the index note produced no defensible identity bridge; the moved-file notation requires archival review.",
    "470-42": "Exact-name, middle-initial, obituary, institutional and archival searches produced only unbridged namesakes.",
    "470-45": "Exact-name, middle-initial, obituary, institutional, newspaper and archival searches produced no defensible Box 782 identity bridge.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def person(key: str) -> tuple[str, str]:
    return PEOPLE[key]


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 780-782",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 470, rows 26-46, and page 471, rows 1-2; checked against layout text and 300 dpi renders",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate people. Full private identifiers remain excluded from public evidence and exports.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; seven accepted Batch 960 candidates and one rejected conflicting-name candidate; identifiers withheld",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "No raw bulk row, record ordinal or full private identifier enters the evidence bundle or public assets.",
        },
        {
            "key": TECH,
            "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf",
            "archival_identifier": "NN3-064-03-008; National Archives Identifier 1263923",
            "title": "World War II Army Enlistment Records: Reference Copy of Technical Documentation",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives at College Park - Electronic Records",
            "publication_record_date": "1994-2005; reference copy modified 2011",
            "locator": "PDF physical pages 44-46; identifier, name, entry-date and civilian-occupation fields",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Used only to interpret selected fields; source damage and incomplete coverage remain applicable.",
        },
        {
            "key": CODES,
            "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1CL_SD.pdf",
            "archival_identifier": "National Archives Identifier 1263923; Code No. 30",
            "title": "NARA Compiled Code Lists for the Electronic Army Serial Number Merged File",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives at College Park - Electronic Records",
            "publication_record_date": "2011-01-12; modified 2011-03-17",
            "locator": "PDF physical pages 170, 174-176 and 304; seven historical civilian-occupation categories checked",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical categories are qualified and never converted into named employers, workplaces, schools or exact modern job titles.",
        },
        {
            "key": TONER,
            "stable_url": "https://www.eisenhowerlibrary.gov/sites/default/files/research/oral-histories/oral-history-transcripts/toner-albert-491.pdf",
            "archival_identifier": "Oral history 491",
            "title": "Oral History Interview with Albert P. Toner",
            "author_creator": "Albert P. Toner; interviewer Maclyn Burg",
            "repository_publisher": "Dwight D. Eisenhower Presidential Library",
            "publication_record_date": "1974-11-19",
            "locator": "Transcript pages 17-18, PDF physical pages 19-20; visually inspected",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "Eisenhower Library Oral Histories",
            "rights_notes": "Direct first-person chronology; only a short excerpt and project-authored paraphrase are retained.",
        },
        {
            "key": TONESK_OAC,
            "stable_url": "https://oac.cdlib.org/findaid/ark:/13030/c8f47sht",
            "archival_identifier": "Hoover Institution collection 2015C36",
            "title": "Tonesk (William John) papers, 1923-1992",
            "author_creator": "Hoover Institution Library & Archives staff",
            "repository_publisher": "Online Archive of California; Hoover Institution Library & Archives",
            "publication_record_date": "finding aid last indexed 2026-07-21",
            "locator": "Biographical history; International Telephone and Telegraph, Raymond Whitcomb, Pan American Airways and Office of Naval Intelligence chronology",
            "access_date": "2026-10-29",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "William John Tonesk papers",
            "rights_notes": "The finding aid does not resolve the index's printed given-name difference; all claims remain qualified.",
        },
        {
            "key": TONESK_STANFORD,
            "stable_url": "https://events.stanford.edu/event/a_man_in_the_room_where_it_happened_the_cold_war_odyssey_of_william_j_tonesk",
            "title": "A Man in the Room Where It Happened: The Cold War Odyssey of William J. Tonesk",
            "author_creator": "Anna Mazurkiewicz",
            "repository_publisher": "Stanford University",
            "publication_record_date": "2024-01-19",
            "locator": "Event biography; earlier career included ONI, OSS, CIA and State Department",
            "access_date": "2026-10-29",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Stanford University Events",
            "rights_notes": "Corroborates William J. Tonesk's OSS service but not the index's Williams spelling.",
        },
        {
            "key": AFI_TONG,
            "stable_url": "https://catalog.afi.com/Film/6023-INTERNATIONAL-SETTLEMENT",
            "title": "International Settlement",
            "author_creator": "Twentieth Century-Fox Film Corporation",
            "repository_publisher": "American Film Institute Catalog",
            "publication_record_date": "1938",
            "locator": "Cast credits; Kam Tong as Leong",
            "access_date": "2026-10-29",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "AFI Catalog of Feature Films",
            "rights_notes": "Supports documented prewar acting work; it does not establish a named employer or itself bridge the middle name.",
        },
        {
            "key": MSU_TONGYAI,
            "stable_url": "https://onthebanks.msu.edu/recordFiles/162-565-350/S201_1942.pdf",
            "title": "Eighty-Fourth Annual Commencement, Michigan State College",
            "author_creator": "Michigan State College",
            "repository_publisher": "Michigan State University Archives and Historical Collections",
            "publication_record_date": "1942-06-13",
            "locator": "Printed page 11, PDF physical page 10; B.S. in Police Administration candidate Singkata Tongyai",
            "access_date": "2026-10-29",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "On the Banks of the Red Cedar",
            "rights_notes": "Student relationship is not treated as employment and is not claimed as the immediate OSS predecessor.",
        },
        {
            "key": TARTU_TONISSON,
            "stable_url": "https://dspace.ut.ee/server/api/core/bitstreams/2be58fe3-0ac3-4346-9489-d971c2fcec42/content",
            "title": "Diplomitöö",
            "author_creator": "Heldur Tõnisson",
            "repository_publisher": "University of Tartu DSpace",
            "publication_record_date": "1938",
            "locator": "Title page; Heldur Tõnisson; Tartu; 1938",
            "access_date": "2026-10-29",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "University of Tartu digital repository",
            "rights_notes": "Supports the accented name form and a 1938 university diploma-work affiliation, not an immediate OSS chronology.",
        },
        {
            "key": FHS_TORNEMAN,
            "stable_url": "https://fhs.diva-portal.org/smash/get/diva2%3A1339834/FULLTEXT01.pdf",
            "title": "Militärhistorisk tidskrift 2018",
            "author_creator": "Swedish Defence University contributors",
            "repository_publisher": "Swedish Defence University",
            "publication_record_date": "2018",
            "locator": "Printed page 90; undated C-byrån group list names Notarie Algot Törneman, Stockholm, for Dalarna",
            "access_date": "2026-10-29",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Militärhistorisk tidskrift",
            "rights_notes": "Documents a Swedish wartime intelligence affiliation; its exact sequence relative to OSS remains uncertain.",
        },
        {
            "key": MUSEUM_TORNEMAN,
            "stable_url": "https://preprod.digitaltmuseum.se/021039710272/torneman-algot-1909-1993",
            "archival_identifier": "KulturNav UUID 956ca0fa-d429-4fac-9554-65d6b7634224",
            "title": "Törneman, Algot (1909-1993)",
            "author_creator": "Värmlands Museum",
            "repository_publisher": "DigitaltMuseum",
            "publication_record_date": "2021-04-27; updated 2026-09-29",
            "locator": "Authority record; Algot Jarl Gustav Törneman; jurist and artist",
            "access_date": "2026-10-29",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "People associated with Värmlands Museum",
            "rights_notes": "Authority metadata only; no image is republished.",
        },
        {
            "key": IFZ_TORRIELLI,
            "stable_url": "https://www.ifz-muenchen.de/heftarchiv/2003_2_5_stehle.pdf",
            "title": "Geheimes aus Bonn für Moskau vom Vatikan",
            "author_creator": "Hansjakob Stehle",
            "repository_publisher": "Institut für Zeitgeschichte München-Berlin",
            "publication_record_date": "2003",
            "locator": "Printed page 264, PDF physical page 2; 16 July 1944 OSS letter signed by Lt. Col. Andrew J. Torrielli",
            "access_date": "2026-10-29",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Vierteljahrshefte für Zeitgeschichte 51, no. 2",
            "rights_notes": "Scholarly article quotes a contemporary OSS letter and establishes exact name, rank and OSS role.",
        },
        {
            "key": CINII_TORRIELLI,
            "stable_url": "https://ci.nii.ac.jp/ncid/BA17591867",
            "archival_identifier": "NCID BA17591867",
            "title": "Italian Opinion on America: As Revealed by Italian Travelers, 1850-1900",
            "author_creator": "Andrew Joseph Torrielli",
            "repository_publisher": "CiNii Books, National Institute of Informatics",
            "publication_record_date": "1941",
            "locator": "Bibliographic record; Harvard Studies in Romance Languages, volume 15; Harvard University, 1941",
            "access_date": "2026-10-29",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "CiNii Books",
            "rights_notes": "Documents prewar scholarly authorship, not a Harvard employment relationship.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {"key": "org-army-b960", "organization_id": "24cec6d5-c3cc-5dc4-b8c9-10ef805535e9", "canonical_name": "United States Army", "historical_name": "United States Army", "aliases": ["U.S. Army"], "organization_type": "military branch", "sector": "military", "country": "United States", "normalization_notes": "Military assignment remains distinct from civilian employment."},
        {"key": "org-pba-b960", "canonical_name": "Public Buildings Administration, Federal Works Agency", "historical_name": "Public Buildings Administration of the Federal Works Agency", "aliases": ["Public Buildings Administration", "PBA", "Federal Works Agency"], "organization_type": "federal agency", "sector": "federal_government", "city": "Washington", "state_or_region": "District of Columbia", "country": "United States", "active_dates": "1939-1949", "normalization_notes": "Historical agency and parent wording follows Toner's testimony; it is not replaced by the later General Services Administration."},
        {"key": "org-itt-b960", "canonical_name": "International Telephone and Telegraph Corporation", "historical_name": "International Telephone and Telegraph", "aliases": ["ITT"], "organization_type": "telecommunications company", "sector": "business_and_industry", "city": "New York", "state_or_region": "New York", "country": "United States", "normalization_notes": "Historical finding-aid wording preserved."},
        {"key": "org-raymond-whitcomb-b960", "canonical_name": "Raymond Whitcomb, Inc.", "historical_name": "Raymond Whitcomb, Inc.", "aliases": [], "organization_type": "travel agency", "sector": "business_and_industry", "country": "United States", "normalization_notes": "Kept separate from later travel businesses or successors."},
        {"key": "org-pan-am-b960", "canonical_name": "Pan American Airways", "historical_name": "Pan American Airways", "aliases": ["Pan Am"], "organization_type": "airline", "sector": "business_and_industry", "country": "United States", "normalization_notes": "The 1940 historical name is preserved rather than silently substituted with a later corporate form."},
        {"key": "org-oni-b960", "organization_id": "f45dd890-7883-5272-9f32-4eb34218760f", "canonical_name": "Office of Naval Intelligence", "historical_name": "Office of Naval Intelligence", "aliases": ["ONI"], "organization_type": "military intelligence agency", "sector": "military", "country": "United States", "normalization_notes": "Government/military assignment, not civilian employment."},
        {"key": "org-msu-b960", "organization_id": "24ac156d-62e6-5107-a412-646391d990a2", "canonical_name": "Michigan State College", "historical_name": "Michigan State College of Agriculture and Applied Science", "aliases": ["M.S.C.", "Michigan State University"], "organization_type": "university", "sector": "academia_and_research", "city": "East Lansing", "state_or_region": "Michigan", "country": "United States", "normalization_notes": "Student relationship uses the historical college name and remains distinct from employment."},
        {"key": "org-tartu-b960", "canonical_name": "University of Tartu", "historical_name": "Tartu Ülikool", "aliases": ["Tartu University"], "organization_type": "university", "sector": "academia_and_research", "city": "Tartu", "country": "Estonia", "normalization_notes": "Student/diploma-work relationship, not employment."},
        {"key": "org-cbyran-b960", "canonical_name": "C-byrån", "historical_name": "Centralbyrån (C-byrån)", "aliases": ["Centralbyrån"], "organization_type": "Swedish military intelligence organization", "sector": "military", "country": "Sweden", "active_dates": "World War II", "normalization_notes": "Historical Swedish name retained; not merged with a successor service."},
    ]


def affiliation(
    key: str,
    person_id: str,
    relationship: str,
    temporal: str,
    identity: str,
    confidence: str,
    quality: str,
    status: str,
    notes: str,
    **kwargs: object,
) -> dict[str, object]:
    value: dict[str, object] = {
        "key": key,
        "person_id": person_id,
        "relationship_type": relationship,
        "pre_oss_temporal_basis": temporal,
        "identity_confidence": identity,
        "claim_confidence": confidence,
        "source_quality": quality,
        "publication_status": status,
        "research_notes": notes,
    }
    value.update(kwargs)
    return value


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for key, (variant, entry_date, code, occupation, _page) in ARMY_PEOPLE.items():
        person_id, name = person(key)
        probable = key == "470-46"
        values.append(
            affiliation(
                f"army-occupation-{slug(name)}-b960",
                person_id,
                "student" if occupation == "Students" else "employment",
                "strongly_date_bounded",
                "probable" if probable else "high_confidence",
                "medium",
                "A_direct_official",
                "publish_qualified",
                f"Historical code {code} at Army entry; no named employer or workplace is inferred. Full private identifier withheld.",
                occupation=occupation,
                end_date=entry_date,
                date_precision="exact Army entry date; occupation current at entry",
                country="United States",
            )
        )

    albert, _ = person("470-28")
    tonesk, _ = person("470-29")
    kam, _ = person("470-32")
    singkata, _ = person("470-33")
    heldur, _ = person("470-34")
    algot, _ = person("470-44")
    values.extend(
        [
            affiliation("albert-toner-pba-b960", albert, "government_assignment", "explicit_immediate", "confirmed", "confirmed", "A_direct_official", "published", "Direct testimony dates the agency job from February through November 1941 and explicitly places COI next.", organization_key="org-pba-b960", organization_name_as_found="Public Buildings Administration of the Federal Works Agency", role_title="messenger, then clerical employee", occupation="federal clerical employee", start_date="1941-02", end_date="1941-11", date_precision="month", city="Washington", state_or_region="District of Columbia", country="United States", immediate_pre_oss=True, last_civilian_pre_service=False),
            affiliation("tonesk-itt-b960", tonesk, "employment", "documented_prewar", "probable", "medium", "B_authoritative_institutional", "publish_qualified", "Qualified because the index prints Williams Tonesk and the archive describes William John Tonesk.", organization_key="org-itt-b960", organization_name_as_found="International Telephone and Telegraph", role_title="supervisor", start_date="1929", end_date="1931", date_precision="year", city="New York", state_or_region="New York", country="United States"),
            affiliation("tonesk-raymond-whitcomb-b960", tonesk, "employment", "documented_prewar", "probable", "medium", "B_authoritative_institutional", "publish_qualified", "The finding aid does not state exact start and end years; the identity remains probable.", organization_key="org-raymond-whitcomb-b960", organization_name_as_found="Raymond Whitcomb, Inc.", role_title="chief lecturer for global travel", country="United States"),
            affiliation("tonesk-pan-am-b960", tonesk, "employment", "strongly_date_bounded", "probable", "medium", "B_authoritative_institutional", "publish_qualified", "The finding aid places Pan American Airways in 1940 and ONI by 1943; identity remains probable.", organization_key="org-pan-am-b960", organization_name_as_found="Pan American Airways", start_date="1940", end_date="before 1943", date_precision="year and bounded endpoint", country="United States", last_civilian_pre_service=True),
            affiliation("tonesk-oni-b960", tonesk, "military_assignment", "probable_immediate", "probable", "medium", "B_authoritative_institutional", "publish_qualified", "Hoover dates ONI by 1943 and Stanford independently lists both ONI and OSS; exact transfer chronology remains unresolved.", organization_key="org-oni-b960", organization_name_as_found="Office of Naval Intelligence", role_title="lieutenant", start_date="by 1943", date_precision="year", country="United States", immediate_pre_oss=True),
            affiliation("kam-tong-actor-b960", kam, "professional_affiliation", "documented_prewar", "probable", "medium", "B_authoritative_institutional", "publish_qualified", "AFI documents a 1938 screen credit; no studio employment or immediate OSS chronology is inferred.", role_title="actor", occupation="motion-picture actor", start_date="1938", end_date="1938", date_precision="year", country="United States"),
            affiliation("singkata-tongyai-msu-b960", singkata, "student", "documented_prewar", "high_confidence", "high", "B_authoritative_institutional", "published", "The rare exact name appears in the college commencement record; student status is not employment.", organization_key="org-msu-b960", organization_name_as_found="Michigan State College", role_title="B.S. candidate in Police Administration", occupation="student", end_date="1942-06-13", date_precision="exact commencement date", city="East Lansing", state_or_region="Michigan", country="United States"),
            affiliation("heldur-tonisson-tartu-b960", heldur, "student", "documented_prewar", "probable", "medium", "B_authoritative_institutional", "publish_qualified", "The university repository documents the accented name and 1938 diploma work; the Box file is still needed for a direct OSS bridge.", organization_key="org-tartu-b960", organization_name_as_found="Tartu", role_title="diploma-work author", occupation="student", end_date="1938", date_precision="year", city="Tartu", country="Estonia"),
            affiliation("algot-torneman-cbyran-b960", algot, "government_assignment", "temporal_relation_uncertain", "probable", "medium", "C_reputable_contemporary_or_scholarly", "publish_qualified", "A scholarly military-history source names him in a wartime C-byrån list; exact sequence relative to OSS is unresolved.", organization_key="org-cbyran-b960", organization_name_as_found="C-byrån", role_title="Dalarna group leader", occupation="jurist", city="Stockholm", country="Sweden"),
        ]
    )
    return values


def claim(
    key: str,
    person_id: str,
    claim_type: str,
    text: str,
    paraphrase: str,
    identity: str,
    temporal: str,
    quality: str,
    confidence: str,
    status: str,
    notes: str,
    source_links: list[dict[str, object]],
    *,
    affiliation_key: str | None = None,
    excerpt: str | None = None,
) -> dict[str, object]:
    value: dict[str, object] = {
        "key": key,
        "person_id": person_id,
        "claim_type": claim_type,
        "claim_text": text,
        "evidence_paraphrase": paraphrase,
        "identity_match_assessment": identity,
        "temporal_assessment": temporal,
        "source_quality": quality,
        "claim_confidence": confidence,
        "publication_status": status,
        "match_notes": notes,
        "sources": source_links,
    }
    if affiliation_key is not None:
        value["affiliation_key"] = affiliation_key
    if excerpt is not None:
        value["evidence_excerpt"] = excerpt
    return value


def army_claims(key: str) -> list[dict[str, object]]:
    person_id, name = person(key)
    variant, entry_date, code, occupation, page = ARMY_PEOPLE[key]
    shared = key == "470-46"
    identity_confidence = "medium" if shared else "high"
    identity_status = "publish_qualified" if shared else "published"
    identity_assessment = (
        "Probable: the exact rare name agrees, but the index identifier is also printed on an unrelated row."
        if shared
        else "High confidence from exact protected-identifier agreement and a compatible exact name."
    )
    notes = (
        "The Army row agrees with Jack Torosky, but the same index identifier appears for Hagop T. Hagopian; no merge was made."
        if shared
        else "Full private identifiers and raw bulk rows remain excluded from public data."
    )
    return [
        claim(
            f"identity-{slug(name)}-army-b960",
            person_id,
            "identity",
            f"The indexed {name} is a {'probable' if shared else 'high-confidence'} match to the reviewed official Army record.",
            f"The protected identifier agrees and the Army record names {variant}; Army entry was {entry_date}.",
            identity_assessment,
            "The Army record dates entry but not the later OSS transfer.",
            "A_direct_official",
            identity_confidence,
            identity_status,
            notes,
            [
                {"source_key": INDEX, "locator_override": f"PDF page {key.split('-')[0]} row {key.split('-')[1]}; Box {'781' if key not in {'470-46', '471-1'} else '782'}; private identifier withheld"},
                {"source_key": ARMY, "locator_override": f"Reviewed {variant} record; private identifier withheld"},
                {"source_key": TECH, "support_type": "context_only", "locator_override": "Field definitions, PDF physical pages 44-46"},
            ],
        ),
        claim(
            f"occupation-{slug(name)}-army-b960",
            person_id,
            "other_pre_oss_affiliation" if occupation == "Students" else "occupation",
            f"At Army entry on {entry_date}, {variant} was recorded in the historical {occupation} category.",
            f"The official bulk record supplies code {code}; the visually reviewed NARA list expands that historical code.",
            "Probable because of the shared index identifier." if shared else "High confidence from the accepted private-identifier bridge.",
            "Strongly date-bounded at Army entry; no employer, workplace or immediate OSS sequence is named.",
            "A_direct_official",
            "medium",
            "publish_qualified",
            "The broad historical category is not converted into a named employer, school or exact modern job title.",
            [
                {"source_key": ARMY, "locator_override": f"Army entry {entry_date}; code {code}; private identifier withheld"},
                {"source_key": CODES, "locator_override": f"PDF physical page {page}; historical category {code}"},
            ],
            affiliation_key=f"army-occupation-{slug(name)}-b960",
            excerpt=occupation,
        ),
    ]


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for key in ARMY_PEOPLE:
        values.extend(army_claims(key))

    james, _ = person("470-27")
    albert, _ = person("470-28")
    tonesk, _ = person("470-29")
    kam, _ = person("470-32")
    singkata, _ = person("470-33")
    heldur, _ = person("470-34")
    algot, _ = person("470-44")
    andrew, _ = person("471-2")
    values.extend(
        [
            claim("identity-james-tonas-conflict-b960", james, "identity", "James Tonas remains in conflict with a separate indexed James Zonas row and an Army record naming James Zonas.", "The protected identifier printed for James Tonas is also printed for James Zonas on PDF page 521; the Army file names Zonas, not Tonas.", "Conflicting: the shared identifier and differing surnames do not justify a merge or transfer of Zonas evidence to Tonas.", "No pre-OSS chronology can be assigned until both personnel files are compared.", "A_direct_official", "conflicting", "conflicting", "Both source rows remain separate people and the Army candidate is not accepted for James Tonas.", [{"source_key": INDEX, "locator_override": "PDF page 470 row 27 and PDF page 521 row 35; shared private identifier withheld"}, {"source_key": ARMY, "locator_override": "Reviewed James Zonas record; private identifier withheld"}]),
            claim("identity-albert-toner-b960", albert, "identity", "The indexed Albert P Toner is confirmed as the Eisenhower Library oral-history interviewee Albert P. Toner.", "Toner directly describes entering COI, later OSS, after a 1941 federal-agency job; the exact indexed name and chronology agree.", "Confirmed by exact full indexed name and direct first-person COI/OSS chronology.", "The testimony dates the predecessor job and COI entry to February and November 1941.", "A_direct_official", "confirmed", "published", "No biographical facts from a namesake were transferred.", [{"source_key": INDEX, "locator_override": "PDF page 470 row 28; Box 781"}, {"source_key": TONER, "locator_override": "Transcript pages 17-18"}]),
            claim("immediate-albert-toner-pba-b960", albert, "immediate_pre_oss_affiliation", "Albert P. Toner worked for the Public Buildings Administration of the Federal Works Agency immediately before joining COI in November 1941.", "He dates the agency job to February 1941, advancement from messenger to clerical work, and COI entry to November.", "Confirmed direct first-person evidence.", "Explicit immediate chronology, with month-level dates and no known intervening affiliation.", "A_direct_official", "confirmed", "published", "Modeled as a government assignment, not a civilian employer aggregate.", [{"source_key": TONER, "locator_override": "Transcript pages 17-18", "excerpt_override": "Public Buildings Administration of the Federal Works Agency"}], affiliation_key="albert-toner-pba-b960"),
            claim("identity-william-tonesk-b960", tonesk, "identity", "The indexed Williams Tonesk is a probable match to intelligence officer William John Tonesk.", "Hoover documents William John Tonesk's career; Stanford independently lists ONI and OSS service, but the index prints Williams.", "Probable from the rare surname and explicit OSS career; the given-name discrepancy prevents a high-confidence identity.", "The institutional sources cover the prewar-to-wartime sequence, but the Box 781 file is needed to bridge the spelling.", "B_authoritative_institutional", "medium", "publish_qualified", "Williams remains the indexed form; William John is a documented candidate variant, not a silent correction.", [{"source_key": INDEX, "locator_override": "PDF page 470 row 29; Box 781"}, {"source_key": TONESK_OAC}, {"source_key": TONESK_STANFORD}]),
            claim("prewar-tonesk-itt-b960", tonesk, "other_pre_oss_affiliation", "Probable match William John Tonesk worked as an International Telephone and Telegraph supervisor from 1929 to 1931.", "The Hoover finding aid supplies the employer, role and dates.", "Probable identity only because the index prints Williams Tonesk.", "Documented prewar employment, not the immediate OSS predecessor.", "B_authoritative_institutional", "medium", "publish_qualified", "Excluded from default confirmed/high analytics.", [{"source_key": TONESK_OAC}], affiliation_key="tonesk-itt-b960"),
            claim("prewar-tonesk-raymond-whitcomb-b960", tonesk, "other_pre_oss_affiliation", "Probable match William John Tonesk was chief lecturer for global travel at Raymond Whitcomb, Inc.", "The Hoover finding aid names the travel agency and role.", "Probable identity only because the index prints Williams Tonesk.", "Documented before the 1940 Pan American Airways move; exact dates are not stated.", "B_authoritative_institutional", "medium", "publish_qualified", "Excluded from default confirmed/high analytics.", [{"source_key": TONESK_OAC}], affiliation_key="tonesk-raymond-whitcomb-b960"),
            claim("last-civilian-tonesk-pan-am-b960", tonesk, "last_civilian_pre_service", "Pan American Airways was probable match William John Tonesk's last documented civilian employer before wartime intelligence service.", "The Hoover chronology places Pan American Airways in 1940 and ONI by 1943.", "Probable identity only because the index prints Williams Tonesk.", "Strongly date-bounded before the ONI assignment; exact departure date is not stated.", "B_authoritative_institutional", "medium", "publish_qualified", "Qualified and excluded from default employer analytics.", [{"source_key": TONESK_OAC, "excerpt_override": "He moved on to Pan American Airways in 1940"}], affiliation_key="tonesk-pan-am-b960"),
            claim("immediate-tonesk-oni-b960", tonesk, "immediate_pre_oss_affiliation", "Office of Naval Intelligence was the probable wartime predecessor to William John Tonesk's OSS service.", "Hoover places him in ONI as a lieutenant by 1943; Stanford independently lists both ONI and OSS in his earlier career.", "Probable identity only because the index prints Williams Tonesk.", "Probable immediate sequence; the accessible sources do not state an exact ONI-to-OSS transfer date.", "B_authoritative_institutional", "medium", "publish_qualified", "Military/government assignment, not a civilian employer.", [{"source_key": TONESK_OAC}, {"source_key": TONESK_STANFORD}], affiliation_key="tonesk-oni-b960"),
            claim("identity-kam-dai-tong-b960", kam, "identity", "The indexed Kam D Tong is a probable match to actor Kam Tong, also documented as Kam Dai Tong.", "The rare indexed name and middle initial align with the documented actor form; AFI confirms prewar screen work, but no second OSS identifier was found.", "Probable, not high-confidence, because the index supplies no additional identifier and AFI does not document OSS service.", "The 1938 credit is definitely prewar; its relation to OSS entry is not stated.", "B_authoritative_institutional", "medium", "publish_qualified", "The candidate remains flagged for Box 781 confirmation.", [{"source_key": INDEX, "locator_override": "PDF page 470 row 32; Box 781"}, {"source_key": AFI_TONG}]),
            claim("occupation-kam-tong-actor-b960", kam, "occupation", "Probable match Kam Tong had documented motion-picture acting work by 1938.", "The AFI catalog credits Kam Tong as Leong in the 1938 film International Settlement.", "Probable identity based on the rare name and middle-name alignment.", "Documented prewar work, not a named employer or immediate predecessor.", "B_authoritative_institutional", "medium", "publish_qualified", "No studio employment relationship is inferred from a film credit.", [{"source_key": AFI_TONG, "excerpt_override": "Kam Tong"}], affiliation_key="kam-tong-actor-b960"),
            claim("identity-singkata-tongyai-b960", singkata, "identity", "The indexed Singkata Tongyai is a high-confidence match to the Michigan State College graduate of the same name.", "The rare exact name appears in Michigan State's 1942 commencement list for Police Administration and in the OSS personnel index.", "High confidence from a distinctive exact name and contemporaneous institutional record.", "The degree predates wartime service; the OSS entry sequence remains unknown.", "B_authoritative_institutional", "high", "published", "The student relationship is not an employer claim.", [{"source_key": INDEX, "locator_override": "PDF page 470 row 33; Box 781"}, {"source_key": MSU_TONGYAI, "locator_override": "Printed page 11"}]),
            claim("prewar-singkata-tongyai-msu-b960", singkata, "other_pre_oss_affiliation", "Singkata Tongyai was a Michigan State College student and 1942 B.S. candidate in Police Administration.", "The official commencement program lists his exact name under the degree in Police Administration.", "High-confidence rare-name identity.", "Documented prewar education; not shown to be the immediate OSS predecessor.", "B_authoritative_institutional", "high", "published", "Student status is kept separate from employment.", [{"source_key": MSU_TONGYAI, "excerpt_override": "Singkata Tongyai"}], affiliation_key="singkata-tongyai-msu-b960"),
            claim("identity-heldur-tonisson-b960", heldur, "identity", "The indexed Heldur Tonisson is a probable match to Estonian jurist Heldur Tõnisson.", "The University of Tartu repository records a 1938 diploma work by Heldur Tõnisson; the rare name aligns after restoring the diacritic.", "Probable from the rare name, but no independent OSS or Box-file identifier was found.", "The diploma work is prewar; its relation to OSS entry remains unknown.", "B_authoritative_institutional", "medium", "publish_qualified", "Tõnisson is retained as a documented variant, not a silent correction.", [{"source_key": INDEX, "locator_override": "PDF page 470 row 34; Box 781"}, {"source_key": TARTU_TONISSON}]),
            claim("prewar-heldur-tonisson-tartu-b960", heldur, "other_pre_oss_affiliation", "Probable match Heldur Tõnisson completed diploma work at the University of Tartu in 1938.", "The university repository's item names Heldur Tõnisson, Tartu and 1938.", "Probable identity from the rare accented/unaccented name pair.", "Documented prewar education, not an employer or immediate predecessor.", "B_authoritative_institutional", "medium", "publish_qualified", "Excluded from default confirmed/high analytics.", [{"source_key": TARTU_TONISSON}], affiliation_key="heldur-tonisson-tartu-b960"),
            claim("identity-algot-torneman-b960", algot, "identity", "The indexed Algot Torneman is a probable match to Swedish jurist Algot Törneman.", "A Swedish Defence University history names Algot Törneman in a C-byrån group list; museum authority data supplies his full form and jurist occupation.", "Probable from the rare name, compatible wartime intelligence context and institutional authority record.", "The C-byrån list is wartime but undated; sequence relative to OSS remains uncertain.", "B_authoritative_institutional", "medium", "publish_qualified", "Törneman is retained as a documented variant; no exact OSS transfer is asserted.", [{"source_key": INDEX, "locator_override": "PDF page 470 row 44; Box 782"}, {"source_key": FHS_TORNEMAN}, {"source_key": MUSEUM_TORNEMAN}]),
            claim("wartime-algot-torneman-cbyran-b960", algot, "other_pre_oss_affiliation", "Probable match Algot Törneman served as C-byrån's Dalarna group leader in Sweden's wartime intelligence organization.", "The Swedish Defence University history reproduces an undated C-byrån list naming him; museum authority data identifies him as a jurist.", "Probable identity from rare name and compatible occupation.", "Documented wartime affiliation; exact temporal relationship to OSS is uncertain.", "C_reputable_contemporary_or_scholarly", "medium", "publish_qualified", "Not presented as a civilian employer or an explicit immediate predecessor.", [{"source_key": FHS_TORNEMAN, "excerpt_override": "Notarie Algot Törneman, Stockholm"}, {"source_key": MUSEUM_TORNEMAN, "support_type": "context_only"}], affiliation_key="algot-torneman-cbyran-b960"),
            claim("identity-andrew-torrielli-b960", andrew, "identity", "The indexed Andrew J Torrielli is confirmed as Lt. Col. Andrew J. Torrielli of OSS.", "A scholarly history cites a contemporary 16 July 1944 letter signed by Lt. Col. Andrew J. Torrielli thanking a helper for aid to OSS.", "Confirmed by exact full indexed name, compatible officer status and an explicit OSS document.", "The cited letter establishes an OSS role in July 1944.", "C_reputable_contemporary_or_scholarly", "confirmed", "published", "Joseph is a documented middle-name expansion from the 1941 bibliographic record.", [{"source_key": INDEX, "locator_override": "PDF page 471 row 2; Box 782; private identifier withheld"}, {"source_key": IFZ_TORRIELLI, "locator_override": "Printed page 264"}]),
            claim("occupation-andrew-torrielli-author-b960", andrew, "occupation", "Andrew Joseph Torrielli was the author of a Harvard-published scholarly book in 1941.", "CiNii records his 1941 volume Italian Opinion on America in Harvard Studies in Romance Languages.", "Confirmed identity from exact full name and independent OSS officer evidence.", "Documented prewar scholarly authorship; no university employment is inferred.", "B_authoritative_institutional", "high", "published", "Publication by Harvard is not classified as employment or student status.", [{"source_key": CINII_TORRIELLI, "excerpt_override": "by Andrew J. Torrielli"}, {"source_key": IFZ_TORRIELLI, "support_type": "context_only"}]),
        ]
    )
    return values


def base_update(key: str, **kwargs: object) -> dict[str, object]:
    value: dict[str, object] = {
        "person_id": PEOPLE[key][0],
        "manual_review_required": True,
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
    }
    value.update(kwargs)
    return value


def unresolved_update(key: str, reason: str) -> dict[str, object]:
    person_id, name = person(key)
    page, row_text = key.split("-")
    box = "780" if key == "470-40" else "781" if int(row_text) <= 43 else "782"
    return {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, Box {box} and archive location 230/86/42/02. {reason}",
        "personnel_category": "unknown_or_indeterminate",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": f"Review Box {box} for corroborating identifiers, immediate pre-OSS affiliation and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }


def army_update(key: str) -> dict[str, object]:
    variant, _entry_date, _code, occupation, _page = ARMY_PEOPLE[key]
    name = PEOPLE[key][1]
    shared = key == "470-46"
    return base_update(
        key,
        identity_status="probable" if shared else "high_confidence",
        identity_evidence=(
            "The exact rare name agrees with the official Army record, but the private index identifier is also printed on an unrelated Hagop T. Hagopian row; no merge was made."
            if shared
            else f"A nonshared private identifier connects the visually verified index row to the official Army record naming {variant}."
        ),
        personnel_category="enlisted_army_personnel",
        commissioned_officer=False,
        allied_or_foreign_personnel=False,
        possible_duplicate_group="batch960-jack-torosky-shared-identifier" if shared else None,
        research_status="completed" if occupation == "Students" else "occupation_only_found",
        next_action=f"Review Box {'781' if key not in {'470-46', '471-1'} else '782'} for a named employer and the Army-to-OSS sequence; the broad historical {occupation} category is not a workplace.",
        archival_review_priority="critical" if shared else "high",
    )


def person_updates() -> list[dict[str, object]]:
    values = [unresolved_update(key, reason) for key, reason in UNRESOLVED.items()]
    values.extend(army_update(key) for key in ARMY_PEOPLE)
    values.extend(
        [
            base_update("470-27", identity_status="conflicting", identity_evidence="The index identifier is shared with a separate James Zonas row, while the Army record names Zonas. Both source rows remain separate and no evidence is transferred to James Tonas.", personnel_category="unknown_or_indeterminate", commissioned_officer=None, allied_or_foreign_personnel=False, possible_duplicate_group="batch960-james-tonas-zonas-shared-identifier", research_status="conflicting_sources", next_action="Compare the James Tonas file in Box 781 with the James Zonas file in Box 865 for surname, service identifier and OSS assignment before resolving the identity.", archival_review_priority="critical"),
            base_update("470-28", identity_status="confirmed", identity_evidence="An Eisenhower Library oral history under the exact name Albert P. Toner gives a direct February-November 1941 federal-agency-to-COI chronology.", name_variants=["Albert P. Toner"], personnel_category="civilian_professional_or_administrative_grade", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="completed", next_action="Review Box 781 for the COI appointment paper and exact Public Buildings Administration position titles; the immediate predecessor is already directly documented.", archival_review_priority="medium"),
            base_update("470-29", identity_status="probable", identity_evidence="Hoover and Stanford document William John Tonesk's ONI and OSS career, but the index prints Williams Tonesk and supplies no second public identifier.", name_variants=["William John Tonesk", "Władysław Jan Toniecki"], personnel_category="unknown_or_indeterminate", commissioned_officer=None, allied_or_foreign_personnel=False, possible_duplicate_group="batch960-williams-william-tonesk", research_status="documented_prewar_employer_found", next_action="Review Box 781 for a direct Williams/William Tonesk spelling bridge and the ONI-to-OSS transfer date before raising the identity or Pan American claim above medium confidence.", archival_review_priority="critical"),
            base_update("470-32", identity_status="probable", identity_evidence="The rare indexed form Kam D Tong aligns with documented actor Kam Dai Tong, and AFI confirms 1938 film work, but no second OSS or Box-file identifier was found.", name_variants=["Kam Dai Tong", "Kam Tong"], personnel_category="unknown_or_indeterminate", commissioned_officer=None, allied_or_foreign_personnel=False, possible_duplicate_group="batch960-kam-dai-tong", research_status="occupation_only_found", next_action="Review Box 781 for birthplace, date of birth and OSS assignment before raising the actor identity above probable confidence.", archival_review_priority="critical"),
            base_update("470-33", identity_status="high_confidence", identity_evidence="Michigan State's 1942 commencement record supplies the rare exact name Singkata Tongyai and a Police Administration degree; the index supplies the same rare full name.", personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=True, research_status="completed", next_action="Review Box 781 for the post-college military pathway and the exact OSS entry sequence; student status is already documented.", archival_review_priority="high"),
            base_update("470-34", identity_status="probable", identity_evidence="The University of Tartu repository documents Heldur Tõnisson and a 1938 diploma work; the rare name aligns with the index after restoring the diacritic, but no direct OSS bridge was found.", name_variants=["Heldur Tõnisson", "Heldur Jaan Tõnisson"], personnel_category="unknown_or_indeterminate", commissioned_officer=None, allied_or_foreign_personnel=True, possible_duplicate_group="batch960-heldur-tonisson-tonisson", research_status="completed", next_action="Review Box 781 for nationality, wartime movements and an OSS assignment bridge before raising the identity above probable confidence.", archival_review_priority="critical"),
            base_update("470-44", identity_status="probable", identity_evidence="A Swedish Defence University history names Algot Törneman in C-byrån's wartime group organization, and museum authority data identifies the rare-name jurist.", name_variants=["Algot Törneman", "Algot Jarl Gustav Törneman"], personnel_category="unknown_or_indeterminate", commissioned_officer=None, allied_or_foreign_personnel=True, possible_duplicate_group="batch960-algot-torneman-torneman", research_status="completed", next_action="Review Box 782 for the OSS relationship and exact C-byrån chronology before treating the Swedish intelligence role as an immediate predecessor.", archival_review_priority="critical"),
            base_update("471-2", identity_status="confirmed", identity_evidence="A scholarly history cites a contemporary OSS letter signed by Lt. Col. Andrew J. Torrielli; the exact name and officer context align with the index.", name_variants=["Andrew Joseph Torrielli"], personnel_category="commissioned_army_officer", commissioned_officer=True, allied_or_foreign_personnel=False, research_status="occupation_only_found", next_action="Review Box 782 for the 1941-to-Army chronology and the last civilian employer; scholarly authorship is documented but no employer has been inferred.", archival_review_priority="high"),
        ]
    )
    return values


def research_attempts() -> list[dict[str, object]]:
    special = {
        "470-26": "Accepted exact-name private-identifier Army bridge and verified historical driver category.",
        "470-27": "Preserved the James Tonas/James Zonas shared-identifier surname conflict; no candidate was selected.",
        "470-28": "Direct Eisenhower Library testimony established the February-November 1941 Public Buildings Administration-to-COI pathway.",
        "470-29": "Hoover and Stanford established William John Tonesk's employment and ONI/OSS career, but the Williams/William bridge remains qualified.",
        "470-30": "Accepted exact-name private-identifier Army bridge and verified historical mining category.",
        "470-31": "Accepted exact-name private-identifier Army bridge and verified historical retail-manager category.",
        "470-32": "AFI documented prewar acting by probable match Kam Tong; no studio employer or high-confidence OSS identity was inferred.",
        "470-33": "Michigan State's commencement program established exact-name student status and a 1942 Police Administration degree.",
        "470-34": "University of Tartu evidence established a probable rare-name student/diploma-work match with the accented form preserved.",
        "470-41": "Accepted exact-name private-identifier Army bridge and verified historical student category.",
        "470-43": "Accepted exact-name private-identifier Army bridge and verified historical painter category.",
        "470-44": "Swedish Defence University and museum authority sources established a probable C-byrån jurist match with unresolved OSS chronology.",
        "470-46": "Accepted the exact-name Army candidate but preserved the unrelated shared-index-identifier conflict and lowered identity confidence.",
        "471-1": "Accepted exact-name private-identifier Army bridge despite the damaged private grade field; verified historical blacksmith category.",
        "471-2": "Scholarly evidence established the exact-name Lt. Col. OSS identity; a 1941 bibliographic record established prewar authorship without an employer inference.",
    }
    attempts: list[dict[str, object]] = []
    for key, (person_id, name) in PEOPLE.items():
        page, row = key.split("-")
        row_number = int(row)
        box = "780" if key == "470-40" else "781" if (page == "470" and row_number <= 43) else "782"
        if key in special:
            outcome = "candidate_found" if key in {"470-27", "470-29", "470-32", "470-34", "470-44", "470-46"} else "source_reviewed"
            reviewed = 10
            rejected = 5
            detail = special[key]
        else:
            outcome = "candidate_rejected" if key in {"470-38", "470-39"} else "no_result"
            reviewed = 7
            rejected = 6
            detail = UNRESOLVED[key]
        attempts.append(
            {
                "key": f"page{page}-row{row}-{slug(name)}-b960",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index and public Archives context; CIA Reading Room or equivalent official-source check; exact-name and meaningful variants; OSS, Army and foreign-name clues; employer and occupation 1940; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Box {box}; private identifiers used only when defensible",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_960",
                "started_at": "2026-10-29T23:55:00Z",
                "completed_at": "2026-10-30T01:25:00Z",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search snippets, unsourced genealogy, people-finder pages, postwar-only leads and sources without an OSS, private-identifier or Box-file bridge were rejected. Search aliases were not treated as silent corrections. Shared identifiers and spelling differences remain explicit.",
                "research_notes": f"{detail} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain, CIA Reading Room-equivalent and Library of Congress searches were checked as applicable. The index pages, Army bulk file, technical documentation and relevant code-list pages were inspected directly. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": (
                    "Compare the James Tonas file in Box 781 with the James Zonas file in Box 865 before resolving the shared-identifier conflict."
                    if key == "470-27"
                    else f"Review Box {box} for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before wartime service."
                ),
                "attempt_number": 1,
                "research_agent_version": "before-oss-b960-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-960-v1",
        "reviewer": "Before OSS Batch 960 evidence review",
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
