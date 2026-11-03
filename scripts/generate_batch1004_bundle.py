#!/usr/bin/env python3
"""Generate the reviewed Batch 1004 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page494-weber-to-weible-"
    "review_batch-1004_2026-11-03.json"
)

INDEX = "nara-index-b1004"
ARMY = "army-bulk-b1004"
TECH = "army-tech-b1004"
CODES = "army-codes-b1004"
LOC_WECHSBERG = "loc-joseph-wechsberg-b1004"
NARA_WEBERG = "nara-jfk-kenneth-weberg-b1004"
KOREAN_BOOK = "nlk-clarence-weems-b1004"
KOREAN_PHOTO = "nikh-clarence-weems-photo-b1004"

ORG_SELF = "self-employed-b1004"
ORG_NEW_YORKER = "new-yorker-b1004"
ORG_MIS = "military-intelligence-service-b1004"


# Page 494 contains 46 printed rows but 45 cautious person entities. Rows 11
# and 12 carry the same protected identifier and already link to one person.
PEOPLE = {
    1: ("fa864ef2-ce19-5dab-aa46-decabe576042", "Jeanette Weber"),
    2: ("b03e84c4-26e3-513b-9482-d33afba6d1c1", "Richard H Weber"),
    3: ("fea827ca-2745-5b7c-8745-e610e07e474f", "Hartwick E Weberg"),
    4: ("94bbea5f-4c8c-5bc8-9603-d6ed5146a09a", "Kenneth H Weberg"),
    5: ("1a3992ae-fdbe-5404-a21f-21832b7a8a02", "Charles A Webster"),
    6: ("bb981f1f-01ad-5658-bbfe-f3d41a626a1d", "David Webster Jr."),
    7: ("4c71e524-afc7-5ee5-912c-416088b94958", "Donald E Webster"),
    8: ("aaae78a1-5dc1-59e1-b287-e2669cffaf8a", "Douglas Webster"),
    9: ("5aec9009-6a31-551d-bb91-0bd6fda7f18c", "George F Webster"),
    10: ("cfe280b2-ad24-546f-90dc-384561bb93e7", "James H Webster"),
    11: ("dce8e648-8a95-57c1-8288-6fff7c40e98d", "John D Webster"),
    13: ("ae7fb230-7c76-523c-8497-696f2e4c8cba", "Pauline E Webster"),
    14: ("5aeca52f-7fcf-5049-92c9-707ab1929e28", "Vera M Webster"),
    15: ("54415368-3c67-5c39-9807-c8965eef8cd9", "Joseph Wechsberg"),
    16: ("f50fca9a-eeec-5f59-afcf-f2b2970a04b2", "Roland E Wechsberg"),
    17: ("bc3f2fee-eca3-5754-bfd4-067954af174a", "Ronald E Wechsler"),
    18: ("23eb2a08-3751-5eab-abb9-7e28cc226d7e", "Richard J Weckesser"),
    19: ("942b6d72-2420-5299-8623-bfbadf35c3e4", "Joseph E Weckler"),
    20: ("ae3d67ad-9869-5fe4-bd4c-7c2b581f39f6", "Margaret E Weddell"),
    21: ("c09a30c6-c0b1-5fb4-9ca0-8ea3730fd2be", "Arthur J Wedler"),
    22: ("7541818d-3e99-560c-bc6a-859069dfad54", "Edna Weed"),
    23: ("30916b94-186b-5a9f-a1e3-aef3ec5d4356", "Elizabeth J Weed"),
    24: ("d198f838-d0b6-5048-812f-034a37a8d367", "Elizabeth R Weed"),
    25: ("45d00a91-8bc8-5c3b-82cc-bf366837ef0b", "J M Weed"),
    26: ("36919928-0134-5ff4-9c8d-7285ef658362", "Ruth E Weed"),
    27: ("b14f8be8-0517-5ace-89c0-bd3b3677f16e", "John W Weeden"),
    28: ("6fcd0a5c-a4a4-55d6-b9b7-985973ab7330", "George W Weege"),
    29: ("cc2647f8-fad1-548e-b7b3-5b2e0071f3fb", "Clair H Weeks"),
    30: ("f41aff07-2672-5830-ba7f-1e57284df2cd", "Clair H Weeks"),
    31: ("3b2e4873-a760-55d0-ae98-8237bce27597", "Grohl H Weeks"),
    32: ("375d8c34-60ce-5426-ab58-50731599e624", "Robert O Weeks"),
    33: ("57a005d7-8004-5584-b7eb-79a4a51f875e", "Clarence Weems Jr."),
    34: ("c60326d2-d745-5833-ac58-28d7f00b5e37", "Michael K Weese"),
    35: ("f1ee23d2-3615-54bd-b86e-d5c8d2912fe1", "Walter E Weese"),
    36: ("f02ed8a5-87df-5780-b957-e61e22f9a8ab", "Betty E Weethee"),
    37: ("e6c61749-0296-5715-b1d2-0e30c6f8edbd", "Theodore G Wege"),
    38: ("72189316-9715-5f71-9013-8f3c161bd142", "Herbert A Weger"),
    39: ("1e2571b2-5f98-514d-b787-4362cbdb246f", "Alice E Wegner"),
    40: ("02cbd337-3848-538d-bb46-59534d055fd6", "Alfred P Wehren"),
    41: ("11c0d5e1-4686-52f1-90f0-8091fa866a0d", "Numa A Wehrle"),
    42: ("b325a60f-7ca1-5029-b5f3-e9ebc5b88f3a", "John E Wehrum"),
    43: ("0e9c2d1f-96d7-5023-8a93-ab3c07d5082b", "Arthur H Wehry"),
    44: ("a65e9e53-36b2-552e-9c8f-e49429759dc5", "Cheng S Wei"),
    45: ("92ef8efc-4bdf-5969-bf91-f734e0553cf6", "Wen Yuan Wei"),
    46: ("388d1b8a-73bf-5094-ac8b-c80844a27724", "Charles F Weible"),
}


ARMY_MATCHES = {
    4: {
        "date": "1942-09-04", "code": "105",
        "occupation": "general office clerk",
        "label": "Clerks, general office",
        "locator": "PDF physical page 171; historical category 1-05",
    },
    15: {
        "date": "1943-11-04", "code": "006",
        "occupation": "author, editor, or reporter",
        "label": "Authors, editors, and reporters",
        "locator": "PDF physical page 170; historical category 0-06",
    },
    18: {
        "date": "1942-07-14", "code": "736",
        "occupation": "chauffeur or driver",
        "label": "Chauffeurs and drivers, bus, taxi, truck, and tractor (semiskilled)",
        "locator": "PDF physical page 175; historical category 7-36",
    },
    21: {
        "date": "1943-07-22", "code": "794",
        "occupation": "machinist apprentice",
        "label": "Machinists' apprentices",
        "locator": "PDF physical page 175; historical category 7-94",
    },
    27: {
        "date": "1942-05-04", "code": "517",
        "occupation": "pattern or model maker, except paper",
        "label": "Pattern and model makers, except paper (skilled)",
        "locator": "PDF physical page 174; historical category 5-17",
    },
    34: {
        "date": "1942-01-28", "code": "849",
        "occupation": "unskilled printing or publishing worker",
        "label": "Unskilled occupations in printing and publishing, n.e.c.",
        "locator": "PDF physical page 175; historical category 8-49",
    },
    35: {
        "date": "1942-07-22", "code": "011",
        "occupation": "college president, professor, or instructor",
        "label": "College presidents, professors, and instructors",
        "locator": "PDF physical page 170; historical category 0-11",
    },
    42: {
        "date": "1941-01-27", "code": "103", "occupation": "checker",
        "label": "Checkers",
        "locator": "PDF physical page 171; historical category 1-03",
    },
    43: {
        "date": "1945-02-08", "code": "056", "occupation": "photographer",
        "label": "Photographers",
        "locator": "PDF physical page 171; historical category 0-56",
    },
}


PRINTED_CATEGORY = {
    1: ("civilian_professional_or_administrative_grade", False, False),
    11: ("commissioned_army_officer", True, False),
    17: ("enlisted_army_personnel", False, False),
    21: ("enlisted_army_personnel", False, False),
    35: ("enlisted_army_personnel", False, False),
    42: ("enlisted_army_personnel", False, False),
    44: ("foreign_or_allied_military_personnel", None, True),
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def box_for(row: int) -> str:
    if row == 11:
        return "821 and 828"
    return "821" if row <= 17 else "822"


def row_locator(row: int) -> str:
    return "rows 11-12" if row == 11 else f"row {row}"


def unresolved_reason(row: int) -> str:
    base = (
        "Exact-name and meaningful-variant searches across the NARA index context, "
        "CIA Reading Room, Library of Congress, OSS, employment, occupation, obituary, "
        "institutional, newspaper, directory, and archival sources produced no reliable "
        "identity and pre-OSS affiliation bridge; unbridged namesakes were rejected."
    )
    if row == 19:
        return (
            "Institutional sources document anthropologist Joseph E. Weckler Jr. at the "
            "Smithsonian and other wartime organizations, but no protected identifier, "
            "Box 822 linkage, or direct OSS personnel-file bridge establishes that he is "
            "the indexed Joseph E. Weckler. " + base
        )
    if row in {29, 30}:
        return (
            "The two page-494 Clair H. Weeks rows remain separate because only one carries "
            "a protected identifier. A postwar Disney-animator namesake lacks an OSS or "
            "personnel-file bridge and was rejected. " + base
        )
    if row == 40:
        return (
            "A Bowdoin alumni lead for Alfred P. Wehren supplied education but no named "
            "employer or indexed-file bridge. " + base
        )
    if row == 44:
        return (
            "The printed word 'Chinese' is preserved as a foreign-personnel notation; it "
            "is not converted into a military rank or commissioned-officer finding. " + base
        )
    if row == 45:
        return (
            "Modern finance and technology results for Wen-Yuan Wei are unbridged namesakes "
            "and were rejected. " + base
        )
    return base


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 821-822 and 828",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 494, rows 1-46; page 498 row 11 conflict cross-check",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 46 page-494 rows remain separate and link to 45 cautious person entities. Pages 494 and 498 were checked against original-detail renders. Full protected identifiers remain private.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; nine accepted protected-identifier comparisons; identifiers and record ordinals withheld",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "Eight exact-name bridges and the independently corroborated WACHSBERG/Wechsberg spelling conflict were accepted after private review. No Army record is treated as a named employer or direct OSS-transfer record.",
        },
        {
            "key": TECH,
            "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf",
            "archival_identifier": "NN3-064-03-008; National Archives Identifier 1263923",
            "title": "World War II Army Enlistment Records: Reference Copy of Technical Documentation",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives at College Park - Electronic Records",
            "publication_record_date": "1994-2005; reference copy modified 2011",
            "locator": "PDF physical pages 44-46; name, Army-entry-date, grade, and civilian-occupation fields",
            "access_date": "2026-11-03",
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
            "locator": "PDF physical pages 170-175; categories 0-06, 0-11, 0-56, 1-03, 1-05, 5-17, 7-36, 7-94, and 8-49",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical labels identify broad occupations, not named employers, institutions, workplaces, or exact OSS-transfer dates.",
        },
        {
            "key": LOC_WECHSBERG,
            "stable_url": "https://tile.loc.gov/storage-services/service/gdc/gdcfindingaidpdfs/ms009303/ms009303.pdf",
            "archival_identifier": "MSS56549; LC catalog record mm81056549",
            "title": "Joseph Wechsberg Papers: A Finding Aid to the Collection in the Library of Congress",
            "author_creator": "T. Michael Womack with Deloris Butler, Paul Colton, and Susie Moody",
            "repository_publisher": "Manuscript Division, Library of Congress",
            "publication_record_date": "2009; revised 2010-04",
            "locator": "PDF printed pages 3-4; biographical note",
            "access_date": "2026-11-03",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Joseph Wechsberg Papers",
            "rights_notes": "The chronology distinguishes freelance journalism and contributor status from later New Yorker staff employment in 1948.",
        },
        {
            "key": NARA_WEBERG,
            "stable_url": "https://www.archives.gov/files/research/jfk/releases/2022/104-10165-10141.pdf",
            "archival_identifier": "JFK release 104-10165-10141",
            "title": "Battle Participation Awards",
            "author_creator": "Office of Strategic Services, European Theater of Operations, United States Army",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1944",
            "locator": "PDF physical page 5; Tec 4 Kenneth H. Weberg roster entry; protected identifier withheld",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "John F. Kennedy Assassination Records Collection",
            "document_number": "104-10165-10141",
            "rights_notes": "The public claim omits the full protected identifier. The roster corroborates OSS identity, rank, and campaign participation, not a pre-OSS employer.",
        },
        {
            "key": KOREAN_BOOK,
            "stable_url": "https://oak.go.kr/nl-ir/bitstream/2020.oak/1128/1/%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%EC%9E%84%EC%8B%9C%EC%A0%95%EB%B6%80%20%EB%AF%B8%EA%B5%AD%20%EB%AC%B8%EC%84%9C%EB%A1%9C%20%EB%B3%B4%EB%8B%A4.pdf",
            "archival_identifier": "RG 165, Records of the War Department General and Special Staffs; Korea, Korean-American Politics",
            "title": "The Korean Provisional Government as Seen through U.S. Documents",
            "author_creator": "National Library of Korea",
            "repository_publisher": "National Library of Korea",
            "publication_record_date": "2019-11",
            "locator": "Printed pages 216-217; May 12, 1942 COI letter to Clarence B. Weems at M.I.S. Far East Branch; footnote 132 on printed page 263",
            "access_date": "2026-11-03",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Digitized U.S. National Archives documents on Korean modern history",
            "rights_notes": "The publication reproduces and translates an official RG 165 document and identifies Weems's March 1943 start in the OSS California office. It prints B. where other institutional sources print N.; the variant is retained.",
        },
        {
            "key": KOREAN_PHOTO,
            "stable_url": "https://contents.history.go.kr/photo/imsi/imsi_period03.do?lang=en",
            "title": "Photo Collection of Modern Korea - Korean Provisional Government, Chongqing period",
            "author_creator": "National Institute of Korean History",
            "repository_publisher": "National Institute of Korean History",
            "publication_record_date": "Historical photograph dated 1945-07",
            "locator": "Korean Independence Army section; caption identifying Captain Clarence N. Weems in Kunming, July 1945",
            "access_date": "2026-11-03",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Photo Collection of Modern Korea",
            "rights_notes": "Used for identity and rank corroboration only; the photograph is not republished by this project.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": ORG_SELF,
            "organization_id": "aa51c76b-2edd-5ca3-a14b-e40ca752af59",
            "canonical_name": "Self-employed",
            "historical_name": "Self-employed",
            "aliases": ["Freelance"],
            "organization_type": "self-employment",
            "sector": "self_employed",
            "normalization_notes": "Person-specific freelance roles are not treated as a shared firm or employer.",
        },
        {
            "key": ORG_NEW_YORKER,
            "organization_id": "d952a5bf-420f-5b7e-8c11-2bfa39fccfed",
            "canonical_name": "The New Yorker",
            "historical_name": "The New Yorker",
            "aliases": ["New Yorker"],
            "organization_type": "magazine",
            "sector": "journalism_and_media",
            "city": "New York",
            "state_or_region": "New York",
            "country": "United States",
            "normalization_notes": "Professional publishing affiliation is not silently converted into salaried employment.",
        },
        {
            "key": ORG_MIS,
            "organization_id": "cd1ea3ba-8a00-5c7b-8df9-9642abd73371",
            "canonical_name": "Military Intelligence Service (U.S. Army)",
            "historical_name": "Military Intelligence Service",
            "aliases": ["M.I.S.", "MIS"],
            "organization_type": "War Department military intelligence service",
            "sector": "military",
            "country": "United States",
            "active_dates": "1942-1945 (wartime unit relevant to this claim)",
            "normalization_notes": "The wartime document prints M.I.S.; this is modeled as a government assignment, not a civilian employer.",
        },
    ]


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, item in ARMY_MATCHES.items():
        values.append({
            "key": f"{slug(PEOPLE[row][1])}-army-occupation-b1004",
            "person_id": PEOPLE[row][0],
            "occupation": item["occupation"],
            "relationship_type": "unknown",
            "end_date": item["date"],
            "date_precision": f"Historical civilian-occupation code {item['code']} was recorded at Army entry on {item['date']}; no named employer, workplace, institution, or exact OSS-transfer date is supplied.",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "confirmed",
            "claim_confidence": "medium",
            "source_quality": "A_direct_official",
            "publication_status": "publish_qualified",
            "research_notes": "Broad historical occupation category only; no named employer, workplace, institution, or OSS transition is inferred.",
        })
    values.extend([
        {
            "key": "joseph-wechsberg-freelance-b1004",
            "person_id": PEOPLE[15][0],
            "organization_key": ORG_SELF,
            "organization_name_as_found": "free-lance journalist",
            "role_title": "Freelance journalist",
            "occupation": "journalist and writer",
            "relationship_type": "self_employment",
            "start_date": "1938",
            "end_date": "1943",
            "date_precision": "The Library of Congress chronology says Wechsberg became a freelance journalist in 1938; an official Army record dates entry to November 4, 1943.",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": True,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "confirmed",
            "claim_confidence": "high",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "published",
            "research_notes": "Self-employment is supported; no newspaper, magazine, or publisher is converted into an employer without separate evidence.",
        },
        {
            "key": "joseph-wechsberg-new-yorker-b1004",
            "person_id": PEOPLE[15][0],
            "organization_key": ORG_NEW_YORKER,
            "organization_name_as_found": "The New Yorker magazine",
            "role_title": "Contributor",
            "occupation": "journalist and writer",
            "relationship_type": "professional_affiliation",
            "start_date": "1943",
            "end_date": "1943",
            "date_precision": "The Library of Congress chronology records contributor status in 1943 and does not call him a staff member until 1948.",
            "city": "New York",
            "state_or_region": "New York",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "confirmed",
            "claim_confidence": "high",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "published",
            "research_notes": "Contributor status is a professional affiliation, not evidence of salaried employment by The New Yorker.",
        },
        {
            "key": "clarence-weems-mis-b1004",
            "person_id": PEOPLE[33][0],
            "organization_key": ORG_MIS,
            "organization_name_as_found": "M.I.S. Far East Branch",
            "role_title": "Korea specialist, Far East Branch",
            "occupation": "government intelligence analyst",
            "relationship_type": "government_assignment",
            "start_date": "1942-05",
            "end_date": "1943-03",
            "date_precision": "A May 12, 1942 official letter addresses Weems at the M.I.S. Far East Branch; the institutional publication says he began work at the OSS California office in March 1943. No transfer order was located.",
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
            "research_notes": "The sequence strongly suggests an M.I.S.-to-OSS pathway, but the exact transfer date and intervening Army status require the personnel file.",
        },
    ])
    return values


def make_claim(
    *, key: str, row: int, claim_type: str, text: str, paraphrase: str,
    identity: str, temporal: str, quality: str, confidence: str,
    publication: str, notes: str, source_links: list[dict[str, str]],
    affiliation_key: str | None = None,
) -> dict[str, object]:
    value: dict[str, object] = {
        "key": key,
        "person_id": PEOPLE[row][0],
        "claim_type": claim_type,
        "claim_text": text,
        "evidence_paraphrase": paraphrase,
        "identity_match_assessment": identity,
        "temporal_assessment": temporal,
        "source_quality": quality,
        "claim_confidence": confidence,
        "publication_status": publication,
        "match_notes": notes,
        "sources": source_links,
    }
    if affiliation_key:
        value["affiliation_key"] = affiliation_key
    return value


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, item in ARMY_MATCHES.items():
        name = PEOPLE[row][1]
        links = [
            {"source_key": INDEX, "locator_override": f"PDF page 494 {row_locator(row)}; protected identifier withheld"},
            {"source_key": ARMY, "locator_override": "Accepted reviewed identity bridge; protected identifier withheld"},
        ]
        if row == 4:
            links.append({
                "source_key": NARA_WEBERG,
                "locator_override": "PDF physical page 5; protected identifier withheld",
                "excerpt_override": "Tec 4 Kenneth H. Weberg",
            })
        if row == 15:
            links.append({
                "source_key": LOC_WECHSBERG,
                "locator_override": "Printed page 3; biographical note",
                "excerpt_override": "Technical sergeant, psychological warfare division, United States army",
            })
        values.append(make_claim(
            key=f"identity-{slug(name)}-b1004",
            row=row,
            claim_type="identity",
            text=f"Indexed {name} is confirmed as the reviewed official Army entry record.",
            paraphrase=(
                "A nonshared protected identifier connects the index and Army records; the Army surname spelling Wachsberg is independently reconciled by the distinctive Library of Congress chronology."
                if row == 15 else
                "The exact indexed and Army names agree, and a nonshared protected identifier connects the records."
            ),
            identity=(
                "Confirmed by the nonshared protected identifier, distinctive near-exact name, writer occupation category, and matching institutional Army chronology; the identifier remains private."
                if row == 15 else
                "Confirmed by exact name and a nonshared protected-identifier agreement; the identifier and record ordinal remain private."
            ),
            temporal=f"The Army record dates entry to {item['date']} and carries historical civilian code {item['code']}.",
            quality="A_direct_official",
            confidence="confirmed",
            publication="published",
            notes="Identity only; no named employer, workplace, institution, or exact OSS-transfer date is inferred.",
            source_links=links,
        ))
        values.append(make_claim(
            key=f"occupation-{slug(name)}-b1004",
            row=row,
            claim_type="occupation",
            text=f"At Army entry on {item['date']}, {name} was recorded in the historical {item['occupation']} category; no named employer or institution is identified.",
            paraphrase=f"The accepted Army record carries civilian-occupation code {item['code']}, decoded from NARA's official code list.",
            identity="The category belongs only to the confirmed protected-identifier match; the identifier itself is not public.",
            temporal="Strongly date-bounded to Army entry; it does not establish the immediate pre-OSS affiliation or a named employer, workplace, or institution.",
            quality="A_direct_official",
            confidence="medium",
            publication="publish_qualified",
            notes="Published with its limits and excluded from verified-employer analytics.",
            source_links=[
                {"source_key": ARMY, "locator_override": f"Army entry {item['date']}; civilian occupation code {item['code']}; protected identifier withheld"},
                {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46"},
                {"source_key": CODES, "locator_override": item["locator"], "excerpt_override": item["label"]},
            ],
            affiliation_key=f"{slug(name)}-army-occupation-b1004",
        ))

    values.extend([
        make_claim(
            key="identity-john-d-webster-b1004",
            row=11,
            claim_type="identity",
            text="The two printed John D. Webster rows on page 494 refer to one person entity while remaining separately preserved source rows.",
            paraphrase="Rows 11 and 12 print the same name and the same nonshared protected identifier; row 12 adds Major, Box 828, and the truncated note '? Move t'.",
            identity="Confirmed same-person linkage from a nonshared protected identifier printed in both source rows; the full identifier remains private.",
            temporal="The index does not supply employment or OSS-transfer chronology.",
            quality="A_direct_official",
            confidence="confirmed",
            publication="published",
            notes="The person link does not erase or deduplicate either immutable source row.",
            source_links=[{
                "source_key": INDEX,
                "locator_override": "PDF page 494 rows 11-12; protected identifier withheld",
                "excerpt_override": "John D Webster",
            }],
        ),
        make_claim(
            key="last-civilian-joseph-wechsberg-freelance-b1004",
            row=15,
            claim_type="last_civilian_pre_service",
            text="Joseph Wechsberg's last documented civilian work before U.S. Army service was self-employed freelance journalism.",
            paraphrase="The Library of Congress chronology says he became a freelance journalist in 1938 and was a New Yorker contributor in 1943; the Army record dates entry to November 4, 1943.",
            identity="Confirmed by the protected Army bridge plus the distinctive institutional biography and matching wartime chronology.",
            temporal="Strongly date-bounded as the last documented civilian work before Army entry; Army service intervened before the indexed OSS affiliation.",
            quality="B_authoritative_institutional",
            confidence="high",
            publication="published",
            notes="The New Yorker is not labeled his employer because the 1943 chronology says contributor and does not say staff member until 1948.",
            source_links=[
                {"source_key": LOC_WECHSBERG, "locator_override": "Printed page 3; biographical note", "excerpt_override": "Became free-lance journalist, writing in English"},
                {"source_key": ARMY, "locator_override": "Army entry November 4, 1943; protected identifier withheld"},
            ],
            affiliation_key="joseph-wechsberg-freelance-b1004",
        ),
        make_claim(
            key="other-preoss-joseph-wechsberg-new-yorker-b1004",
            row=15,
            claim_type="other_pre_oss_affiliation",
            text="Joseph Wechsberg was a contributor to The New Yorker in 1943; this is a professional affiliation, not a documented employer relationship.",
            paraphrase="The Library of Congress chronology distinguishes 1943 contributor status from the staff appointment it dates to 1948.",
            identity="Confirmed by the protected Army bridge plus the distinctive institutional biography.",
            temporal="Documented in 1943 before Army entry; it is not labeled the immediate pre-OSS affiliation.",
            quality="B_authoritative_institutional",
            confidence="high",
            publication="published",
            notes="Excluded from employer analytics because contributor status alone does not establish employment.",
            source_links=[{
                "source_key": LOC_WECHSBERG,
                "locator_override": "Printed page 3; biographical note",
                "excerpt_override": "Contributor, The New Yorker magazine",
            }],
            affiliation_key="joseph-wechsberg-new-yorker-b1004",
        ),
        make_claim(
            key="conflict-roland-e-wechsberg-b1004",
            row=16,
            claim_type="identity",
            text="Roland E. Wechsberg and Roland E. Weschler remain separate person entities because the same protected identifier appears with two different indexed surnames.",
            paraphrase="The visually checked index prints Roland E. Wechsberg on page 494 and Roland E. Weschler on page 498 with the same protected identifier.",
            identity="Conflicting source spellings; neither row is selected as canonical for the other without direct personnel-file evidence.",
            temporal="The index supplies no chronology that resolves the conflict.",
            quality="A_direct_official",
            confidence="conflicting",
            publication="conflicting",
            notes="Both source rows and both entities remain visible; the full identifier is withheld.",
            source_links=[{
                "source_key": INDEX,
                "locator_override": "PDF page 494 row 16 and page 498 row 11; protected identifier withheld",
            }],
        ),
        make_claim(
            key="identity-clarence-n-weems-b1004",
            row=33,
            claim_type="identity",
            text="The indexed Clarence Weems Jr. is a high-confidence match to Captain Clarence N. Weems of OSS service in Kunming.",
            paraphrase="The suffix, uncommon full name, officer status, Korean specialization, and National Institute of Korean History OSS caption align.",
            identity="High confidence from the matching suffix and officer status plus two independent Korean national institutions identifying Clarence N. Weems Jr. in wartime U.S. government and OSS roles.",
            temporal="The sources document M.I.S. work in 1942, an OSS California start in March 1943, and OSS service in Kunming in July 1945.",
            quality="B_authoritative_institutional",
            confidence="high",
            publication="published",
            notes="The indexed personnel file should still be reviewed because the index omits the middle initial and the published U.S. document reproduces B. where the photo caption gives N.",
            source_links=[
                {"source_key": INDEX, "locator_override": "PDF page 494 row 33; protected officer identifier withheld"},
                {"source_key": KOREAN_BOOK, "locator_override": "Printed pages 216-217 and footnote 132 on printed page 263"},
                {"source_key": KOREAN_PHOTO, "locator_override": "Korean Independence Army section; Kunming, July 1945", "excerpt_override": "Clarence N. Weems"},
            ],
        ),
        make_claim(
            key="immediate-clarence-weems-mis-b1004",
            row=33,
            claim_type="immediate_pre_oss_affiliation",
            text="The Military Intelligence Service Far East Branch is the best-supported probable immediate pre-OSS affiliation for Clarence N. Weems Jr.",
            paraphrase="An official May 1942 letter addresses Weems at the M.I.S. Far East Branch, while the institutional publication dates his OSS California work from March 1943.",
            identity="High-confidence match from the suffix, officer status, Korean specialization, and institutional OSS documentation.",
            temporal="Probable immediate sequence; the exact M.I.S. end date and transfer order have not been located.",
            quality="B_authoritative_institutional",
            confidence="medium",
            publication="publish_qualified",
            notes="Modeled as a government assignment, not a civilian employer. The J. B. Beaird oil-company lead remains unpublished for lack of an authoritative source.",
            source_links=[{
                "source_key": KOREAN_BOOK,
                "locator_override": "Printed pages 216-217 and footnote 132 on printed page 263",
                "excerpt_override": "M.I.S. Far East Branch",
            }],
            affiliation_key="clarence-weems-mis-b1004",
        ),
    ])
    return values


def base_update(row: int, **overrides: object) -> dict[str, object]:
    value: dict[str, object] = {
        "person_id": PEOPLE[row][0],
        "manual_review_required": True,
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }
    if row in PRINTED_CATEGORY:
        category, commissioned, allied = PRINTED_CATEGORY[row]
        value["personnel_category"] = category
        if commissioned is not None:
            value["commissioned_officer"] = commissioned
        value["allied_or_foreign_personnel"] = allied
    value.update(overrides)
    return value


def person_updates() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    special_rows = set(ARMY_MATCHES) | {11, 16, 33}
    for row in sorted(set(PEOPLE) - special_rows):
        reason = unresolved_reason(row)
        values.append(base_update(
            row,
            identity_status="unresolved",
            identity_evidence=f"The visually verified page 494 source preserves {PEOPLE[row][1]}, its printed rank or notation, archival box, and location. {reason}",
            research_status="requires_archival_review",
            next_action=f"Review the indexed Box {box_for(row)} personnel file for corroborating identifiers, the immediate pre-OSS affiliation, and the last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}",
        ))
    for row, item in ARMY_MATCHES.items():
        if row == 15:
            continue
        values.append(base_update(
            row,
            identity_status="confirmed",
            identity_evidence="The exact indexed name and a nonshared protected identifier connect the row to the reviewed official Army record.",
            personnel_category="enlisted_army_personnel",
            commissioned_officer=False,
            allied_or_foreign_personnel=False,
            research_status="occupation_only_found",
            next_action=f"Review the indexed Box {box_for(row)} personnel file to identify any named employer or institution behind the broad {item['occupation']} category and establish the Army-to-OSS chronology.",
            nara_catalog_id="1263923",
        ))
    values.extend([
        base_update(
            11,
            identity_status="confirmed",
            identity_evidence="The same nonshared protected identifier is printed for both John D. Webster rows; both rows remain separately preserved. Row 12 adds Major, Box 828, and the truncated note '? Move t'.",
            personnel_category="commissioned_army_officer",
            commissioned_officer=True,
            possible_duplicate_group="auto:dce8e648-8a95-57c1-8288-6fff7c40e98d",
            research_status="requires_archival_review",
            next_action="Review the indexed Box 821 and Box 828 personnel files to confirm the move or duplicate relationship and identify the immediate pre-OSS affiliation and last civilian employer.",
        ),
        base_update(
            15,
            identity_status="confirmed",
            identity_evidence="A nonshared protected identifier connects the index to an Army record printed WACHSBERG; the distinctive Library of Congress chronology corroborates Joseph Wechsberg's writer occupation and wartime Army service.",
            name_variants=["Joseph Wachsberg"],
            personnel_category="enlisted_army_personnel",
            commissioned_officer=False,
            allied_or_foreign_personnel=False,
            research_status="verified_employer_found",
            archival_review_priority="medium",
            next_action="Review the indexed Box 821 personnel file to establish the Army psychological-warfare-to-OSS chronology and test whether any civilian affiliation followed freelance journalism before Army entry.",
            nara_catalog_id="1263923",
        ),
        base_update(
            16,
            identity_status="conflicting",
            identity_evidence="The same protected identifier is printed for Roland E. Wechsberg on page 494 and Roland E. Weschler on page 498. The differently spelled source rows and person entities remain separate pending direct file evidence.",
            possible_duplicate_group="serial-conflict:35360597",
            research_status="conflicting_sources",
            archival_review_priority="critical",
            next_action="Review both the Box 821 Roland E. Wechsberg file and Box 827 Roland E. Weschler file to determine whether the shared protected identifier reflects a misspelling, cross-reference, or source error; do not merge on the identifier alone.",
        ),
        base_update(
            33,
            identity_status="high_confidence",
            identity_evidence="The suffix, uncommon full name, officer status, Korean specialization, and institutional documentation of Captain Clarence N. Weems in OSS service align.",
            name_variants=["Clarence N Weems Jr.", "Clarence B Weems Jr."],
            personnel_category="commissioned_army_officer",
            commissioned_officer=True,
            allied_or_foreign_personnel=False,
            research_status="completed",
            archival_review_priority="medium",
            next_action="Review the indexed Box 822 personnel file for the exact M.I.S.-to-OSS transfer order and last civilian employer. The J. B. Beaird oil-company lead remains unpublished until an authoritative source establishes it.",
        ),
    ])
    if len(values) != len(PEOPLE):
        raise RuntimeError(f"Expected {len(PEOPLE)} person updates, generated {len(values)}")
    return values


def research_attempts() -> list[dict[str, object]]:
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        if row in ARMY_MATCHES:
            item = ARMY_MATCHES[row]
            outcome, reviewed, rejected = "source_reviewed", 9, 5
            if row == 15:
                reviewed = 12
                note = "A reviewed protected-identifier Army bridge, Library of Congress chronology, and official occupation code support confirmed identity, freelance journalism as last documented civilian work, New Yorker contributor status, and a qualified writer occupation at Army entry."
            elif row == 4:
                reviewed = 10
                note = "A reviewed protected-identifier Army bridge and official OSS European Theater roster confirm identity; the Army code supports only a qualified general-office-clerk category at entry."
            else:
                note = f"A reviewed protected-identifier Army bridge supports identity and a qualified {item['occupation']} category at Army entry; no named employer, workplace, institution, or OSS-transfer date is supplied."
        elif row == 11:
            outcome, reviewed, rejected = "source_reviewed", 8, 5
            note = "Two separately preserved John D. Webster rows share a nonshared protected identifier and are confirmed as one person entity; the Box 821/828 move and employment chronology require archival review."
        elif row == 16:
            outcome, reviewed, rejected = "candidate_found", 8, 6
            note = "A visually verified protected-identifier conflict connects differently spelled Roland E. Wechsberg and Roland E. Weschler rows. Both entities remain separate and the conflict is published transparently."
        elif row == 33:
            outcome, reviewed, rejected = "source_reviewed", 13, 7
            note = "Korean national institutional sources support a high-confidence Clarence N. Weems Jr. identity and a qualified M.I.S.-to-OSS pathway. A discovery-only J. B. Beaird oil-company lead was withheld because no authoritative source was located."
        else:
            outcome, reviewed, rejected = "candidate_rejected", 7, 6
            note = unresolved_reason(row)
        attempts.append({
            "key": f"page494-row{row}-{slug(name)}-b1004",
            "person_id": person_id,
            "source_adapter": "manual_staged_protocol",
            "query_text": f"{name}; NARA OSS index context; CIA Reading Room, National Archives, and Library of Congress exact-name domain checks; exact-name and meaningful spelling, initial, suffix, punctuation, transliteration, and OCR variants; OSS, rank, branch, assignment, and identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory, and archival searches; indexed Box {box_for(row)}; protected identifiers used only in private official-record comparison",
            "query_variant_type": "staged_identity_employment_archival_protocol_batch_1004",
            "started_at": "2026-11-03T21:32:00Z",
            "completed_at": "2026-11-03T21:55:00Z",
            "outcome": outcome,
            "sources_reviewed": reviewed,
            "candidate_sources_rejected": rejected,
            "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, postwar-only leads, discovery-only biographies, and sources without an OSS, protected-identifier, rank, unit, or personnel-file bridge were rejected. Historical Army categories were not converted into named employers, workplaces, or institutions. Education and contributor status were not converted into employment. The unsupported J. B. Beaird oil-company lead was not published.",
            "research_notes": f"{note} Exact-name official-domain, OSS, employer, occupation, obituary, biography, institutional, newspaper, directory, and archival searches were checked as applicable. NARA index pages 494 and 498 were rendered and visually checked where relevant. Official Army bulk data, technical documentation, code documentation, and the Kenneth H. Weberg OSS roster were inspected. No authenticated NARA Catalog API call was made.",
            "next_action": f"Review the indexed Box {box_for(row)} personnel file for corroborating identifiers, the immediate pre-OSS affiliation, and the last civilian employer before wartime service.",
            "attempt_number": 1,
            "research_agent_version": "before-oss-b1004-v1",
        })
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-1004-v1",
        "reviewer": "Before OSS Batch 1004 evidence review",
        "sources": sources(),
        "organizations": organizations(),
        "affiliations": affiliations(),
        "claims": claims(),
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }
    EvidenceBundle.model_validate(bundle)
    OUTPUT.write_text(
        json.dumps(bundle, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
