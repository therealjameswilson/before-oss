#!/usr/bin/env python3
"""Generate the reviewed Batch 1020 evidence bundle for PDF page 510."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page510-hedwig-wirowski-to-chester-wohlert-review_"
    "batch-1020_2026-11-04.json"
)

INDEX = "nara-index-b1020"
ARMY = "army-bulk-b1020"
TECH = "army-tech-b1020"
CODES = "army-codes-b1020"
WLUDYKA_REPORT = "oss-caserta-board-wludyka-b1020"
SOLEY_WITHROW = "soley-radio-warfare-withrow-b1020"
FBI_DONOVAN_FIRM = "fbi-donovan-firm-b1020"
CMH_WITHROW = "cmh-advice-support-withrow-b1020"
NARA_WITTMANN = "nara-aliu-wittmann-b1020"
GETTY_WITTMANN = "getty-wittmann-finding-aid-b1020"
SMITHSONIAN_WITTMANN = "smithsonian-wittmann-finding-aid-b1020"
SKIDMORE_WITTMANN = "skidmore-news-wittmann-b1020"

ORG_ARMY = "us-army-b1020"
ORG_DONOVAN_FIRM = "donovan-leisure-newton-lumbard-b1020"
ORG_PORTLAND = "portland-art-museum-b1020"
ORG_HYDE = "hyde-collection-b1020"
ORG_SKIDMORE = "skidmore-college-b1020"
ORG_ROCKHILL = "rockhill-nelson-gallery-b1020"
ORG_ATC = "army-air-forces-air-transport-command-b1020"

PEOPLE = {
    1: ("b4b7b290-54bf-553a-b066-eb7e8da2c290", "Hedwig Wirowski", "846"),
    2: ("cb75f026-58ed-5598-b335-ead5aec65d54", "Helen M Wirth", "846"),
    3: ("9f9382bd-342c-582d-abc2-c7d6a870133e", "Jeanne A Wirtzer", "846"),
    4: ("b85ac61f-ab30-581f-bfc7-cf12b7274f14", "Dorothy E Wise", "846"),
    5: ("2b5716e9-bcec-53a6-9643-997dde2b8efc", "Thomas A Wise", "846"),
    6: ("6205afac-f3d4-5843-a199-75da2e51e8be", "Compton Wiseman", "847"),
    7: ("13bca019-8f4c-5f40-9f62-15f0a42b1ac2", "Edward C Wiseman", "847"),
    8: ("c3d3bf13-437b-5516-b62b-21d94fa5631d", "Perry S Wiseman", "847"),
    9: ("8100d25e-b091-5cfc-b6f5-0f4fc746a9c2", "Richard H Wiseman", "847"),
    10: ("62703042-2f77-5bda-982d-84bc85cb3bdf", "William A Wiseman", "847"),
    11: ("7ac0f4ab-1444-5819-9a43-ee750f6f5617", "Frank G Wisner", "847"),
    12: ("19ef5f51-53ea-5b43-8e32-9bced3988192", "Jerome J Wisniewski", "847"),
    13: ("8fed55bb-3c46-5f00-93e3-52aa17426a7c", "Leonard G Wisniewski", "847"),
    14: ("5f956427-cd1e-525e-a08d-d54a5c9b155f", "John F Wiswell", "847"),
    15: ("f6b3d97c-7a75-504d-8102-c8fe56f5a115", "Ernest J Wisynski", "847"),
    16: ("32fb210d-4237-55eb-bd81-5535cb63d981", "William D Witchey", "847"),
    17: ("45acebc5-5b1f-5f0e-b967-8d7c3cec43d6", "Everett W Withee", "847"),
    18: ("13d7e8eb-8d70-5639-ae63-051ee0f2867f", "Robert D Witherill", "847"),
    19: ("b62081b4-a876-5022-9b8b-59e34f809e6d", "William B Witherow", "847"),
    20: ("f30f7f8d-3f40-555e-9fe8-b07f3cb94161", "Allene L Withers", "847"),
    21: ("1465cdd3-a6e6-5d4d-8653-eb134c31447b", "Percy L Withers", "847"),
    22: ("d0afd4bc-3cf2-5157-a1ef-39bab37c717b", "Paul R Witherspoon", "847"),
    23: ("712fe131-fc7a-55be-8b3f-d4922c992f45", "James R Withrow Jr.", "847"),
    24: ("7ff19d0e-17e4-5fea-a0f8-0fd1aba5cbc1", "Kurt G Witrofsky", "847"),
    25: ("93db574e-2055-55e7-8ea4-058239aa598d", "Dee Ray Witt", "847"),
    26: ("79519f38-fa50-5fd5-bf63-89559cbc829c", "Eros C Witt", "848"),
    27: ("6cc3be88-1ed8-571a-b1ee-6791245cae12", "Ludwig Witt", "848"),
    28: ("fc49f85a-f5d0-5928-88aa-8777fce7431b", "William K Wittausch", "848"),
    29: ("0dcde8f9-348a-550e-8f37-5bc896779f73", "Elden H Witte", "848"),
    30: ("cbe4f95a-d9e5-55c9-9718-8009bcf979c4", "Samuel E Wittel", "848"),
    31: ("bc612ccc-5ee9-5303-8ff7-5c60d00af8df", "George W.B. Witten", "848"),
    32: ("0f78881e-4d64-5146-815d-49f395bf8974", "Wilford M Wittenberg", "848"),
    33: ("9af5653f-b029-5395-a049-f75078a90fca", "Carl F Wittke", "848"),
    34: ("86e490ea-5e4e-5901-b85b-5584cee3659a", "Robert E Wittke", "848"),
    35: ("b7e30866-a352-5e8f-a161-7455fddd3348", "Joseph F Wittman", "848"),
    36: ("b94996b5-ff25-5e3a-a0c6-26e2a11c2eff", "Margaret Wittman", "848"),
    37: ("d800fdf2-10cc-53a8-8ef6-246dfa5b0c2a", "Otto Wittman Jr.", "848"),
    38: ("48121c94-a8ae-5758-900e-3b0cbde41d21", "John E Witushynski", "848"),
    39: ("e6ec64b7-bd06-5826-bfc2-a75ca16a2069", "Aubrey W Wix", "848"),
    40: ("7019adce-7081-5b95-9da8-15916518307d", "Edna L Wixon", "848"),
    41: ("a5557c77-d03c-5255-b8a3-fc8fd0f51eca", "Ernest J Wixynski", "848"),
    42: ("30f3b163-8dd2-5926-974e-396efe09a963", "Peter S Wludyka", "848"),
    43: ("697bf9d5-0e74-52fa-9d36-9929de21310d", "Elmer G Woehl", "849"),
    44: ("9d158dd5-f1b2-5775-a0f5-6d4951e2885d", "Emmett Wofford", "849"),
    45: ("7b2f226d-a9bc-5642-b460-25cf25ff7b9e", "William L Wofford", "849"),
    46: ("261bda6d-62c8-57ee-b43f-4eb8865aa028", "Chester G Wohlert", "849"),
}

# Only official categories that were assigned in NARA's visually inspected
# three-digit table and predate OSS dissolution are published.
ARMY_OCCUPATIONS = {
    8: ("1944-01-20", "316", "general farm hand", "Farm hands, general farms", "PDF physical page 173; historical category 3-16"),
    9: ("1942-09-14", "788", "warehousing, storekeeping, handling, loading or unloading worker, not elsewhere classified", "Warehousing, storekeeping, handling, loading, unloading, and related occupations, n.e.c.", "PDF physical page 174; historical category 7-88"),
    10: ("1942-05-16", "307", "animal and livestock farmer", "Farmers, animal and livestock", "PDF physical page 173; historical category 3-07"),
    24: ("1943-05-14", "736", "chauffeur or driver", "Chauffeurs and drivers, bus, taxi, truck, and tractor", "PDF physical page 174; historical category 7-36"),
    25: ("1943-03-04", "989", "miscellaneous occupation not elsewhere classified", "Miscellaneous occupations, n.e.c.", "PDF physical page 175; historical category 9-89"),
    27: ("1942-09-01", "050", "laboratory technician or assistant", "Laboratory technicians and assistants", "PDF physical page 170; historical category 0-50"),
    28: ("1944-03-10", "097", "manager or official not elsewhere classified", "Managers and officials, n.e.c.", "PDF physical page 171; historical category 0-97"),
    38: ("1941-03-13", "105", "general office clerk", "Clerks, general office", "PDF physical page 171; historical category 1-05"),
    45: ("1943-04-07", "056", "photographer", "Photographers", "PDF physical page 170; historical category 0-56"),
}

ARMY_IDENTITY_ONLY = {
    17: "Code 609 is unassigned in the official three-digit table and is not interpreted.",
    22: "The Army entry is dated 20 December 1945, after OSS dissolution, so its code and grade are not used as pre-OSS evidence.",
    44: "Code 590 is unassigned in the official three-digit table and is not interpreted.",
}

FRANK = 11
WITHROW = 23
WITTMANN = 37
WLUDYKA = 42
DUPLICATE_GROUP = "page510-ernest-wisynski-wixynski-boxes847-849"


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def occupation_key(row: int) -> str:
    return f"{slug(PEOPLE[row][1])}-army-occupation-row{row}-b1020"


def source(
    key: str,
    url: str,
    title: str,
    publisher: str,
    quality: str,
    *,
    author: str | None = None,
    date: str | None = None,
    locator: str | None = None,
    identifier: str | None = None,
    collection: str | None = None,
    document: str | None = None,
    rights: str | None = None,
) -> dict[str, object]:
    value: dict[str, object] = {
        "key": key,
        "stable_url": url,
        "title": title,
        "repository_publisher": publisher,
        "access_date": "2026-11-04",
        "source_quality": quality,
    }
    for field, item in {
        "author_creator": author,
        "publication_record_date": date,
        "locator": locator,
        "archival_identifier": identifier,
        "collection_name": collection,
        "document_number": document,
        "rights_notes": rights,
    }.items():
        if item is not None:
            value[field] = item
    return value


def sources() -> list[dict[str, object]]:
    return [
        source(
            INDEX,
            "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "OSS Personnel Files from Excel",
            "National Archives and Records Administration",
            "A_direct_official",
            author="National Archives and Records Administration",
            date="2010-12-23",
            locator="PDF page 510, rows 1-46; visually checked against a 180 dpi render",
            identifier="RG 226, Entry A1-224, Boxes 846-849",
            collection="Records of the Office of Strategic Services, Record Group 226",
            rights="All printed rows remain separate. Full service identifiers remain private.",
        ),
        source(
            ARMY,
            "https://catalog.archives.gov/id/1263923",
            "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "National Archives and Records Administration",
            "A_direct_official",
            author="Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            date="1938-1946; merged file created 2002",
            locator="Official unrestricted ASNEF.FIN.DAT; twelve accepted protected-identifier comparisons; identifiers and raw rows withheld",
            identifier="National Archives Identifier 1263923; parent series NAID 604357",
            collection="World War II Army Enlistment Records",
            document="ASNEF.FIN.DAT",
            rights="Army-entry categories are not named employers or exact OSS-transfer records.",
        ),
        source(
            TECH,
            "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf",
            "World War II Army Enlistment Records: Reference Copy of Technical Documentation",
            "National Archives at College Park - Electronic Records",
            "A_direct_official",
            author="National Archives and Records Administration",
            date="1994-2005; reference copy modified 2011",
            locator="PDF physical pages 44-46; fixed-width identifier, name, entry-date, grade and civilian-occupation fields",
            identifier="NN3-064-03-008; National Archives Identifier 1263923",
            collection="World War II Army Enlistment Records technical documentation",
        ),
        source(
            CODES,
            "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1CL_SD.pdf",
            "NARA Compiled Code Lists for the Electronic Army Serial Number Merged File",
            "National Archives at College Park - Electronic Records",
            "A_direct_official",
            author="National Archives and Records Administration",
            date="2011-01-12; modified 2011-03-17",
            locator="PDF physical pages 170-175; assigned categories visually inspected; codes 590 and 609 confirmed absent",
            identifier="National Archives Identifier 1263923; Code No. 30",
            collection="World War II Army Enlistment Records technical documentation",
            rights="Only assigned historical categories are published; undefined codes are not expanded.",
        ),
        source(
            WLUDYKA_REPORT,
            "https://digitalcollections.hoover.org/internal/media/dispatcher/331573/full",
            "OSS Board interviews of AAI personnel, Caserta and Bari",
            "Hoover Institution Library & Archives Digital Collections",
            "A_direct_official",
            author="Office of Strategic Services",
            date="1944-05-04 through 1944-05-17",
            locator="Printed page 58, item LIX; board session at OSS Headquarters, Bari, 17 May 1944",
            collection="Office of Strategic Services records",
            rights="The direct official report is paraphrased; the full protected service number is not retained in public data.",
        ),
        source(
            SOLEY_WITHROW,
            "https://www.worldradiohistory.com/BOOKSHELF-ARH/History/Radio-Warfare-L-Soley-1989.pdf",
            "Radio Warfare: OSS and CIA Subversive Propaganda",
            "Praeger Publishers",
            "C_reputable_contemporary_or_scholarly",
            author="Lawrence C. Soley",
            date="1989",
            locator="Printed pages 51-52 and 160-161; PDF text lines 2971-2995 and 8773-8799",
            document="ISBN 0-275-93051-3; Library of Congress 88-25187",
            rights="Short excerpts and project-authored paraphrases only; no book pages are republished.",
        ),
        source(
            FBI_DONOVAN_FIRM,
            "https://vault.fbi.gov/William%20J%20Donovan%20/William%20J%20Donovan%20Part%2006/",
            "William J. Donovan Part 6 of 7",
            "Federal Bureau of Investigation, The Vault",
            "A_direct_official",
            author="Federal Bureau of Investigation",
            date="1940",
            locator="PDF lines 403-476; 27 September and 4 October 1940 firm letterhead and correspondence",
            collection="FBI Records: The Vault, William J. Donovan",
            rights="Used to normalize the historical name of Donovan's 1940 law firm, not as proof by itself that Withrow worked there.",
        ),
        source(
            CMH_WITHROW,
            "https://history.army.mil/portals/143/Images/Publications/catalog/91-1.pdf",
            "Advice and Support: The Early Years, 1941-1960",
            "U.S. Army Center of Military History",
            "A_direct_official",
            author="Ronald H. Spector",
            date="1983",
            locator="Printed page 67; Lieutenant James R. Withrow Jr., U.S. Navy, OSS India veteran",
            document="CMH Pub 91-1",
            rights="Used for identity, service branch and OSS-role corroboration, not for pre-OSS employment chronology.",
        ),
        source(
            NARA_WITTMANN,
            "https://www.archives.gov/research/holocaust/art/oss-art-looting-investigation-unit-reports.html",
            "OSS Art Looting Investigation Unit Reports",
            "National Archives and Records Administration",
            "A_direct_official",
            author="Michael Hussey, Michael J. Kurtz, and Greg Bradsher",
            date="page last reviewed 2016-08-15",
            locator="Art Looting Investigation Unit background; Otto Wittman personnel paragraph",
            collection="Holocaust-Era Assets Records",
            rights="The page confirms that Otto Wittman joined the OSS unit; chronology comes from archival finding aids.",
        ),
        source(
            GETTY_WITTMANN,
            "https://oac.cdlib.org/findaid/ark:/13030/c8cf9wq0",
            "Otto Wittmann papers relating to the Art Looting Investigation Unit of the United States Office of Strategic Services",
            "Getty Research Institute; Online Archive of California",
            "B_authoritative_institutional",
            author="Getty Research Institute",
            date="finding aid for papers dated 1933-2000, bulk 1945-1946",
            locator="Background biography, especially paragraphs on Hyde Collection, Portland Art Museum, military service and 3 August 1945 OSS transfer",
            identifier="Getty Research Institute Accession no. 910130",
            rights="Archival finding-aid metadata and concise project-authored paraphrases only.",
        ),
        source(
            SMITHSONIAN_WITTMANN,
            "https://sirismm.si.edu/EADpdfs/AAA.wittotto.pdf",
            "A Finding Aid to the Otto Wittmann Papers, 1932-1996",
            "Archives of American Art, Smithsonian Institution",
            "B_authoritative_institutional",
            author="Jayna M. Hanson",
            date="2012-05-21",
            locator="PDF pages 1-2, collection overview and biographical note",
            identifier="AAA.wittotto",
            rights="Finding-aid metadata only; no archival items are republished.",
        ),
        source(
            SKIDMORE_WITTMANN,
            "https://digitalcoll.skidmore.edu/nanna/record/357/files/0_complete_object.pdf?registerDownload=1&version=1&withMetadata=0&withWatermark=0",
            "Skidmore News, Volume 16, Number 2",
            "Skidmore College Digital Collections",
            "C_reputable_contemporary_or_scholarly",
            author="Skidmore News",
            date="1940-10-16",
            locator="Printed page 4; note accompanying Otto W. Wittman Jr.'s article",
            rights="Contemporary college newspaper; only a short excerpt and paraphrase are retained.",
        ),
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {"key": ORG_ARMY, "canonical_name": "United States Army", "historical_name": "United States Army", "aliases": ["U.S. Army"], "organization_type": "military service", "sector": "military", "country": "United States", "active_dates": "Peter S. Wludyka entered in September 1940 and was recruited by OSS in Cairo", "normalization_notes": "Modeled as a military assignment, not civilian employment."},
        {"key": ORG_DONOVAN_FIRM, "canonical_name": "Donovan, Leisure, Newton & Lumbard", "historical_name": "Donovan, Leisure, Newton & Lumbard", "aliases": ["Donovan, Leisure, Newton Lumbard", "William J. Donovan's New York law firm"], "organization_type": "law firm", "sector": "law", "city": "New York", "state_or_region": "New York", "country": "United States", "active_dates": "Name documented on 1940 firm letterhead", "normalization_notes": "The 1940 historical name is preserved; no later Irvine name or successor is substituted."},
        {"key": ORG_PORTLAND, "canonical_name": "Portland Art Museum", "historical_name": "Portland Art Museum", "aliases": ["Portland Museum of Art"], "organization_type": "art museum", "sector": "arts_and_culture", "city": "Portland", "state_or_region": "Oregon", "country": "United States", "active_dates": "Otto Wittmann briefly served as assistant director in 1941", "normalization_notes": "The Getty finding aid's wording is preserved; this Oregon institution is not confused with the Maine museum."},
        {"key": ORG_HYDE, "canonical_name": "The Hyde Collection", "historical_name": "The Hyde Collection", "aliases": ["Mrs. Hyde's private art collection"], "organization_type": "art collection and museum", "sector": "arts_and_culture", "city": "Glens Falls", "state_or_region": "New York", "country": "United States", "active_dates": "Otto Wittmann served as curator before his 1941 Army draft", "normalization_notes": "The private collection's historical status is preserved."},
        {"key": ORG_SKIDMORE, "canonical_name": "Skidmore College", "historical_name": "Skidmore College", "aliases": [], "organization_type": "college", "sector": "academia_and_research", "city": "Saratoga Springs", "state_or_region": "New York", "country": "United States", "active_dates": "Otto Wittmann was a part-time Fine and Applied Art instructor in October 1940", "normalization_notes": "Employment is modeled separately from the finding aid's statement that he also pursued graduate study."},
        {"key": ORG_ROCKHILL, "canonical_name": "William Rockhill Nelson Gallery of Art and Mary Atkins Museum of Fine Arts", "historical_name": "Rockhill Nelson Gallery of Art", "aliases": ["Nelson-Atkins Museum of Art"], "organization_type": "art museum", "sector": "arts_and_culture", "city": "Kansas City", "state_or_region": "Missouri", "country": "United States", "active_dates": "Otto Wittmann worked there from September 1933 until 1937", "normalization_notes": "Historical name is preserved; modern successor name appears only as an alias."},
        {"key": ORG_ATC, "canonical_name": "U.S. Army Air Forces Air Transport Command", "historical_name": "Air Transport Command", "aliases": ["Army Air Force Air Transport Command", "ATC"], "organization_type": "military command", "sector": "military", "city": "Washington", "state_or_region": "District of Columbia", "country": "United States", "active_dates": "Otto Wittmann served there before his 3 August 1945 transfer to OSS ALIU", "normalization_notes": "A military assignment, not civilian employment; the reviewed sources also describe a later War Department assignment."},
    ]


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, _label, _locator) in ARMY_OCCUPATIONS.items():
        identity = "high_confidence" if row in {25, 45} else "confirmed"
        values.append({
            "key": occupation_key(row),
            "person_id": PEOPLE[row][0],
            "occupation": occupation,
            "relationship_type": "unknown",
            "end_date": date,
            "date_precision": f"Historical civilian-occupation code {code} was recorded at Army entry on {date}; no named employer or institution is supplied.",
            "country": "United States",
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": identity,
            "claim_confidence": "medium",
            "source_quality": "A_direct_official",
            "publication_status": "publish_qualified",
            "research_notes": "Broad historical category only; no employer, workplace, institution, exact specialty beyond the code, or exact OSS transition is inferred.",
        })
    values.extend([
        {"key": "peter-wludyka-army-b1020", "person_id": PEOPLE[WLUDYKA][0], "organization_key": ORG_ARMY, "organization_name_as_found": "Army", "role_title": "Technician Fourth Grade; recruited in Cairo for OSS Services", "occupation": "Army enlisted clerk", "relationship_type": "military_assignment", "start_date": "1940-09", "date_precision": "The 17 May 1944 OSS report says he entered the Army in September 1940, was recruited in Cairo, and was assigned to Bari on 28 January 1944; exact recruitment day is unstated.", "city": "Cairo", "country": "Egypt", "immediate_pre_oss": True, "pre_oss_temporal_basis": "explicit_immediate", "identity_confidence": "confirmed", "claim_confidence": "confirmed", "source_quality": "A_direct_official", "publication_status": "published", "research_notes": "Direct Army-to-OSS pathway; no civilian employer is established."},
        {"key": "james-withrow-donovan-firm-b1020", "person_id": PEOPLE[WITHROW][0], "organization_key": ORG_DONOVAN_FIRM, "organization_name_as_found": "Donovan's law firm", "role_title": "attorney", "occupation": "lawyer", "relationship_type": "employment", "date_precision": "Soley places Withrow at Donovan's New York firm in 1940 and explicitly says Donovan later recruited him into OSS; the exact recruitment date is not stated.", "city": "New York", "state_or_region": "New York", "country": "United States", "immediate_pre_oss": True, "last_civilian_pre_service": True, "pre_oss_temporal_basis": "explicit_immediate", "identity_confidence": "high_confidence", "claim_confidence": "high", "source_quality": "C_reputable_contemporary_or_scholarly", "publication_status": "published", "research_notes": "The historical firm name is independently normalized from 1940 official letterhead. No later firm name is substituted."},
        {"key": "otto-wittmann-portland-b1020", "person_id": PEOPLE[WITTMANN][0], "organization_key": ORG_PORTLAND, "organization_name_as_found": "Portland Art Museum", "role_title": "assistant director", "occupation": "museum professional", "relationship_type": "employment", "start_date": "1941", "end_date": "1941-12", "date_precision": "The Getty finding aid says Wittmann briefly served while on reserve and resumed military service after Pearl Harbor in December 1941; exact dates are unstated.", "city": "Portland", "state_or_region": "Oregon", "country": "United States", "last_civilian_pre_service": True, "pre_oss_temporal_basis": "explicit_immediate", "identity_confidence": "confirmed", "claim_confidence": "high", "source_quality": "B_authoritative_institutional", "publication_status": "published", "research_notes": "Last documented civilian employer before resumed wartime service; not his immediate pre-OSS military assignment."},
        {"key": "otto-wittmann-atc-b1020", "person_id": PEOPLE[WITTMANN][0], "organization_key": ORG_ATC, "organization_name_as_found": "Air Transport Command", "role_title": "Army Air Forces officer; later major", "occupation": "military officer", "relationship_type": "military_assignment", "start_date": "1941-12", "end_date": "1945-08-03", "date_precision": "Institutional finding aids place him in Air Transport Command and the War Department before his dated 3 August 1945 OSS ALIU transfer; exact command-transfer dates are unavailable.", "city": "Washington", "state_or_region": "District of Columbia", "country": "United States", "immediate_pre_oss": True, "pre_oss_temporal_basis": "strongly_date_bounded", "identity_confidence": "confirmed", "claim_confidence": "high", "source_quality": "B_authoritative_institutional", "publication_status": "published", "research_notes": "Best-supported named military pathway. The intervening generic War Department description is preserved in the claim note rather than silently collapsed."},
        {"key": "otto-wittmann-hyde-b1020", "person_id": PEOPLE[WITTMANN][0], "organization_key": ORG_HYDE, "organization_name_as_found": "Hyde Collection", "role_title": "curator", "occupation": "curator", "relationship_type": "employment", "start_date": "1938", "end_date": "1941", "date_precision": "The Getty finding aid identifies this as the position held until his 1941 Army draft; Skidmore News independently identifies him as curator in October 1940.", "city": "Glens Falls", "state_or_region": "New York", "country": "United States", "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "confirmed", "claim_confidence": "high", "source_quality": "B_authoritative_institutional", "publication_status": "published", "research_notes": "Earlier civilian employment; a later brief Portland appointment is the last documented civilian employer before resumed service."},
        {"key": "otto-wittmann-skidmore-b1020", "person_id": PEOPLE[WITTMANN][0], "organization_key": ORG_SKIDMORE, "organization_name_as_found": "Skidmore College", "role_title": "part-time instructor in Fine and Applied Art", "occupation": "art instructor", "relationship_type": "employment", "end_date": "1940-10-16", "date_precision": "Contemporary issue date establishes the position by 16 October 1940 and says his lecture series was entering its third year; exact appointment dates are unavailable.", "city": "Saratoga Springs", "state_or_region": "New York", "country": "United States", "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "confirmed", "claim_confidence": "high", "source_quality": "C_reputable_contemporary_or_scholarly", "publication_status": "published", "research_notes": "Employment is distinct from graduate study; the college is not treated only as an alma mater."},
        {"key": "otto-wittmann-rockhill-b1020", "person_id": PEOPLE[WITTMANN][0], "organization_key": ORG_ROCKHILL, "organization_name_as_found": "Rockhill Nelson Gallery of Art", "role_title": "curator of prints and museum staff member", "occupation": "museum curator", "relationship_type": "employment", "start_date": "1933-09", "end_date": "1937", "date_precision": "The Getty finding aid dates the initial appointment to September 1933 and the next Fogg Museum phase to 1937.", "city": "Kansas City", "state_or_region": "Missouri", "country": "United States", "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "confirmed", "claim_confidence": "high", "source_quality": "B_authoritative_institutional", "publication_status": "published", "research_notes": "Earlier documented museum employment; the historical gallery name is retained."},
    ])
    return values


def make_claim(
    *, key: str, row: int, claim_type: str, text: str, paraphrase: str,
    identity: str, temporal: str, quality: str, confidence: str,
    publication: str, notes: str, source_links: list[dict[str, str]],
    affiliation_key: str | None = None, excerpt: str | None = None,
) -> dict[str, object]:
    value: dict[str, object] = {
        "key": key, "person_id": PEOPLE[row][0], "claim_type": claim_type,
        "claim_text": text, "evidence_paraphrase": paraphrase,
        "identity_match_assessment": identity, "temporal_assessment": temporal,
        "source_quality": quality, "claim_confidence": confidence,
        "publication_status": publication, "match_notes": notes,
        "sources": source_links,
    }
    if affiliation_key:
        value["affiliation_key"] = affiliation_key
    if excerpt:
        value["evidence_excerpt"] = excerpt
    return value


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    army_rows = set(ARMY_OCCUPATIONS) | set(ARMY_IDENTITY_ONLY)
    for row in sorted(army_rows):
        name = PEOPLE[row][1]
        identity_confidence = "high" if row in {25, 44, 45} else "confirmed"
        identity_status = "high confidence" if identity_confidence == "high" else "confirmed"
        values.append(make_claim(
            key=f"identity-{slug(name)}-row{row}-b1020", row=row,
            claim_type="identity",
            text=f"Indexed {name} is {identity_status} as the matching Army record.",
            paraphrase="The official index and Army record agree through a nonshared protected identifier and compatible name evidence.",
            identity=("High confidence from a nonshared protected identifier and compatible name evidence; the Army record expands or supplies a middle name or initial." if row in {25, 44, 45} else "Confirmed by a nonshared protected identifier and exact official name agreement; the identifier remains private."),
            temporal="Identity evidence only; the Army entry date is not treated as an OSS transition date.",
            quality="A_direct_official", confidence=identity_confidence,
            publication="published",
            notes="The accepted review withholds the full identifier and does not convert Army fields into a named employer.",
            source_links=[
                {"source_key": INDEX, "support_type": "supports", "locator_override": f"PDF page 510, row {row}; Box {PEOPLE[row][2]}"},
                {"source_key": ARMY, "support_type": "supports"},
                {"source_key": TECH, "support_type": "context_only"},
            ],
        ))
        if row in ARMY_OCCUPATIONS:
            date, code, occupation, label, locator = ARMY_OCCUPATIONS[row]
            values.append(make_claim(
                key=f"occupation-{slug(name)}-row{row}-b1020", row=row,
                affiliation_key=occupation_key(row), claim_type="occupation",
                text=f"At Army entry on {date}, {name}'s record carried historical civilian-occupation category {code}: {occupation}.",
                paraphrase=f"The official bulk record carries code {code}; NARA's compiled list labels that category '{label}'.",
                identity=("High confidence from protected-identifier agreement and compatible name evidence." if row in {25, 45} else "Confirmed by protected-identifier agreement and exact official name evidence."),
                temporal="Strongly date-bounded at Army entry, but neither an exact OSS start date nor proof of an immediate predecessor affiliation.",
                quality="A_direct_official", confidence="medium",
                publication="publish_qualified",
                notes="A historical category only. It is excluded from verified-employer analytics and never converted into a named employer or institution.",
                source_links=[
                    {"source_key": ARMY, "support_type": "supports"},
                    {"source_key": TECH, "support_type": "context_only"},
                    {"source_key": CODES, "support_type": "supports", "locator_override": locator},
                ],
            ))
    values.extend([
        make_claim(key="identity-peter-wludyka-b1020", row=WLUDYKA, claim_type="identity", text="Indexed Peter S Wludyka is confirmed as the Technician Fourth Grade whom an OSS board interviewed in Bari in May 1944.", paraphrase="The exact uncommon name and protected service identifier match the index, and the direct OSS report supplies Army and OSS chronology.", identity="Confirmed by exact uncommon name plus a nonshared protected identifier in a direct OSS personnel interview; the identifier remains private.", temporal="The report dates Army entry, Cairo recruitment and Bari assignment.", quality="A_direct_official", confidence="confirmed", publication="published", notes="A modern professor with the same name was rejected as a namesake and supplies no evidence to this profile.", source_links=[{"source_key": INDEX, "support_type": "supports", "locator_override": "PDF page 510, row 42; Box 848"}, {"source_key": WLUDYKA_REPORT, "support_type": "supports", "locator_override": "Printed page 58, item LIX"}]),
        make_claim(key="peter-wludyka-army-immediate-b1020", row=WLUDYKA, affiliation_key="peter-wludyka-army-b1020", claim_type="immediate_pre_oss_affiliation", text="Peter S. Wludyka was serving in the U.S. Army when OSS recruited him in Cairo for Services.", paraphrase="The May 1944 OSS board report says he entered the Army in September 1940 and was recruited by OSS in Cairo before assignment to Bari.", identity="Confirmed by exact name and protected-identifier agreement in a direct OSS report.", temporal="Explicitly immediate Army-to-OSS recruitment; the exact Cairo recruitment day is not stated.", quality="A_direct_official", confidence="confirmed", publication="published", notes="This is a military assignment, not a civilian employer; no last civilian employer is identified.", source_links=[{"source_key": WLUDYKA_REPORT, "support_type": "supports", "locator_override": "Printed page 58, item LIX"}], excerpt="Was recruited by OSS in Cairo for Services."),
        make_claim(key="identity-james-withrow-b1020", row=WITHROW, claim_type="identity", text="Indexed James R Withrow Jr. is a high-confidence match to the U.S. Navy lieutenant and OSS Morale Operations officer.", paraphrase="The exact name and suffix align with a scholarly OSS history and an official Army history identifying Lieutenant Withrow as a Navy officer and OSS India veteran.", identity="High confidence from exact full name and suffix, lieutenant rank, U.S. Navy branch, and direct OSS Far East roles across independent sources; Box 847 remains unreviewed.", temporal="The sources place him at Donovan's firm in 1940, then in OSS Morale Operations and the postwar Saigon mission.", quality="A_direct_official", confidence="high", publication="published", notes="Unrelated modern and geographic namesakes were rejected.", source_links=[{"source_key": INDEX, "support_type": "supports", "locator_override": "PDF page 510, row 23; Box 847"}, {"source_key": SOLEY_WITHROW, "support_type": "supports", "locator_override": "Printed pages 51-52 and 160-161"}, {"source_key": CMH_WITHROW, "support_type": "supports", "locator_override": "Printed page 67"}]),
        make_claim(key="james-withrow-law-firm-immediate-b1020", row=WITHROW, affiliation_key="james-withrow-donovan-firm-b1020", claim_type="immediate_pre_oss_affiliation", text="James R. Withrow Jr.'s immediate pre-OSS affiliation was William J. Donovan's New York law firm, where he worked as an attorney.", paraphrase="Soley identifies Withrow as a young attorney in Donovan's firm, says Donovan assigned his 1940 destroyer-transfer research, and explicitly states Donovan recruited him into OSS.", identity="High-confidence exact-name, suffix, Navy-rank and OSS-role match.", temporal="Explicit firm-to-OSS recruitment sequence, although no exact recruitment date is given.", quality="C_reputable_contemporary_or_scholarly", confidence="high", publication="published", notes="Official 1940 firm letterhead independently supplies the historical firm name; it is context, not standalone proof of Withrow's employment.", source_links=[{"source_key": SOLEY_WITHROW, "support_type": "supports", "locator_override": "Printed pages 51-52 and 160-161"}, {"source_key": FBI_DONOVAN_FIRM, "support_type": "context_only", "locator_override": "27 September and 4 October 1940 firm letterhead"}, {"source_key": CMH_WITHROW, "support_type": "context_only", "locator_override": "Printed page 67"}], excerpt="James Withrow was a young attorney in Donovan's law firm"),
        make_claim(key="james-withrow-law-firm-last-civilian-b1020", row=WITHROW, affiliation_key="james-withrow-donovan-firm-b1020", claim_type="last_civilian_pre_service", text="Donovan, Leisure, Newton & Lumbard was James R. Withrow Jr.'s last documented civilian employer before his Navy and OSS service.", paraphrase="The documented chronology moves from Withrow's attorney work in Donovan's firm to recruitment by Donovan into OSS as a lieutenant.", identity="High-confidence exact-name, suffix, Navy-rank and OSS-role match.", temporal="Explicit recruitment from the firm; no intervening civilian employer is documented in the reviewed sources.", quality="C_reputable_contemporary_or_scholarly", confidence="high", publication="published", notes="The firm name is normalized from official 1940 letterhead and is not replaced by a postwar variant.", source_links=[{"source_key": SOLEY_WITHROW, "support_type": "supports", "locator_override": "Printed pages 51-52 and 160-161"}, {"source_key": FBI_DONOVAN_FIRM, "support_type": "context_only", "locator_override": "1940 firm letterhead"}]),
        make_claim(key="identity-otto-wittmann-b1020", row=WITTMANN, claim_type="identity", text="Indexed Major Otto Wittman Jr. is confirmed as museum professional and Army Air Forces Major Otto Wittmann Jr., who transferred to OSS ALIU.", paraphrase="The exact name, suffix and major rank align across the index, NARA's ALIU history, and two institutional finding aids with direct OSS and military chronology.", identity="Confirmed by exact distinctive name and suffix, matching major rank, and direct institutional records linking the same museum career, Army Air Forces service and OSS ALIU role.", temporal="The finding aids date the civilian career, 1941 military service and 3 August 1945 OSS transfer.", quality="A_direct_official", confidence="confirmed", publication="published", notes="The published variant preserves the double-n surname used in archival sources while retaining the index's single-n spelling.", source_links=[{"source_key": INDEX, "support_type": "supports", "locator_override": "PDF page 510, row 37; Major; Box 848"}, {"source_key": NARA_WITTMANN, "support_type": "supports", "locator_override": "ALIU personnel paragraph"}, {"source_key": GETTY_WITTMANN, "support_type": "supports", "locator_override": "Background biography"}, {"source_key": SMITHSONIAN_WITTMANN, "support_type": "supports", "locator_override": "PDF page 2"}]),
        make_claim(key="otto-wittmann-atc-immediate-b1020", row=WITTMANN, affiliation_key="otto-wittmann-atc-b1020", claim_type="immediate_pre_oss_affiliation", text="Otto Wittmann Jr.'s best-supported immediate pre-OSS pathway was Army Air Forces service in Air Transport Command and the War Department.", paraphrase="The finding aids place him in Air Transport Command and then the War Department before a dated 3 August 1945 transfer to the OSS Art Looting Investigation Unit.", identity="Confirmed exact-name, suffix, rank and OSS-role match.", temporal="Strongly date-bounded military pathway; the source names an intervening War Department placement but not a more specific unit.", quality="B_authoritative_institutional", confidence="high", publication="published", notes="Air Transport Command is the last specifically named military command, while the broader War Department placement is preserved rather than erased.", source_links=[{"source_key": GETTY_WITTMANN, "support_type": "supports", "locator_override": "Background biography, paragraphs on military service and 3 August 1945 transfer"}, {"source_key": SMITHSONIAN_WITTMANN, "support_type": "supports", "locator_override": "PDF page 2"}, {"source_key": NARA_WITTMANN, "support_type": "context_only", "locator_override": "ALIU personnel paragraph"}]),
        make_claim(key="otto-wittmann-portland-last-civilian-b1020", row=WITTMANN, affiliation_key="otto-wittmann-portland-b1020", claim_type="last_civilian_pre_service", text="Portland Art Museum was Otto Wittmann Jr.'s last documented civilian employer before he resumed wartime service in December 1941.", paraphrase="The Getty finding aid says he briefly served as assistant director while on reserve, then resumed service after Pearl Harbor.", identity="Confirmed exact-name, suffix, rank and OSS-role match.", temporal="Explicitly sequenced as the final civilian role before resumed military service.", quality="B_authoritative_institutional", confidence="high", publication="published", notes="The brief Portland appointment is kept separate from his earlier concurrent Hyde Collection and Skidmore roles.", source_links=[{"source_key": GETTY_WITTMANN, "support_type": "supports", "locator_override": "Background biography, 1941 Portland and military-service paragraph"}]),
        make_claim(key="otto-wittmann-hyde-prewar-b1020", row=WITTMANN, affiliation_key="otto-wittmann-hyde-b1020", claim_type="other_pre_oss_affiliation", text="Otto Wittmann Jr. served as curator of The Hyde Collection before his 1941 Army draft.", paraphrase="The Getty finding aid explicitly sequences the Hyde curatorship before his draft; contemporary Skidmore News independently identifies him as Mrs. Hyde's curator in October 1940.", identity="Confirmed exact-name, suffix, rank and OSS-role match.", temporal="Documented prewar employment; a later brief Portland role prevents treating it as the last civilian employer.", quality="B_authoritative_institutional", confidence="high", publication="published", notes="The source's historical description as a private collection is preserved.", source_links=[{"source_key": GETTY_WITTMANN, "support_type": "supports", "locator_override": "Background biography"}, {"source_key": SKIDMORE_WITTMANN, "support_type": "supports", "locator_override": "Printed page 4"}], excerpt="Mr. Wittman is curator of the private art collection of Mrs. Hyde."),
        make_claim(key="otto-wittmann-skidmore-prewar-b1020", row=WITTMANN, affiliation_key="otto-wittmann-skidmore-b1020", claim_type="other_pre_oss_affiliation", text="In October 1940, Otto Wittmann Jr. was a part-time instructor in Skidmore College's Fine and Applied Art department.", paraphrase="The contemporary college newspaper identifies the position and says his illustrated art-lecture series was beginning its third year.", identity="Confirmed through exact distinctive name and the same Hyde Collection context preserved by institutional finding aids.", temporal="Contemporary documented prewar employment; not the last civilian employer.", quality="C_reputable_contemporary_or_scholarly", confidence="high", publication="published", notes="Skidmore employment is not inferred from education; it is directly documented by the college newspaper.", source_links=[{"source_key": SKIDMORE_WITTMANN, "support_type": "supports", "locator_override": "Printed page 4"}], excerpt="part-time instructor in the department of Fine and Applied Art at Skidmore College"),
        make_claim(key="otto-wittmann-rockhill-prewar-b1020", row=WITTMANN, affiliation_key="otto-wittmann-rockhill-b1020", claim_type="other_pre_oss_affiliation", text="Otto Wittmann Jr. began museum work at the Rockhill Nelson Gallery of Art in Kansas City in September 1933.", paraphrase="The Getty finding aid dates the appointment and describes his museum work before the 1937 Fogg Museum phase.", identity="Confirmed exact-name, suffix, rank and OSS-role match.", temporal="Documented earlier prewar employment.", quality="B_authoritative_institutional", confidence="high", publication="published", notes="The historical gallery name is retained; the modern Nelson-Atkins name is only an alias.", source_links=[{"source_key": GETTY_WITTMANN, "support_type": "supports", "locator_override": "Background biography, 1933-1937 paragraphs"}, {"source_key": SMITHSONIAN_WITTMANN, "support_type": "context_only", "locator_override": "PDF page 2"}]),
    ])
    return values


def unresolved_reason(row: int) -> str:
    if row == 33:
        return "The exact name matches historian Carl Frederick Wittke, but accessible sources did not bridge that academic to this OSS index row; the famous-biography candidate is rejected pending Box 848 evidence."
    if row in {15, 41}:
        return "Ernest J Wisynski and Ernest J Wixynski are plausible spelling variants, but their separate rows and different boxes cannot be merged without joint folder review."
    if row == 7:
        return "The printed PM/3c and USNR notation establish enlisted naval status but not identity beyond the index or a pre-OSS employer."
    return "Accessible exact-name, official, OSS, employer, occupation, obituary, institutional, newspaper, directory and archival searches produced no reliable identity-and-affiliation bridge; unbridged namesakes and postwar-only leads were rejected."


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
    special = set(ARMY_OCCUPATIONS) | set(ARMY_IDENTITY_ONLY) | {FRANK, WITHROW, WITTMANN, WLUDYKA}
    values: list[dict[str, object]] = []
    for row in sorted(set(PEOPLE) - special):
        reason = unresolved_reason(row)
        overrides: dict[str, object] = {}
        if row == 7:
            overrides.update(personnel_category="enlisted_naval_personnel", commissioned_officer=False, allied_or_foreign_personnel=False)
        if row in {15, 41}:
            overrides.update(possible_duplicate_group=DUPLICATE_GROUP, archival_review_priority="critical")
        if row == 33:
            overrides.update(archival_review_priority="critical")
        values.append(base_update(
            row,
            identity_status="unresolved",
            identity_evidence=f"The visually verified page 510 source preserves {PEOPLE[row][1]}, archival Box {PEOPLE[row][2]}, and the printed rank or note when present. {reason}",
            research_status="requires_archival_review",
            next_action=f"Review indexed Box {PEOPLE[row][2]} for corroborating identifiers, immediate pre-OSS affiliation and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}",
            **overrides,
        ))
    for row in ARMY_OCCUPATIONS:
        values.append(base_update(
            row,
            identity_status="high_confidence" if row in {25, 45} else "confirmed",
            identity_evidence=("A nonshared protected identifier and compatible official name evidence connect the records; the Army row expands or supplies a middle name or initial, and the identifier remains private." if row in {25, 45} else "A nonshared protected identifier and exact official name agreement connect the index and Army records; the identifier remains private."),
            name_variants=(["Dee R Witt"] if row == 25 else ["William Lawrence Wofford"] if row == 45 else None),
            replace_name_variants=False,
            personnel_category="enlisted_army_personnel",
            commissioned_officer=False,
            allied_or_foreign_personnel=False,
            research_status="occupation_only_found",
            nara_catalog_id="1263923",
            next_action=f"Review indexed Box {PEOPLE[row][2]} to identify a named employer or institution and establish Army-to-OSS chronology; the bulk record supplies only a historical category at Army entry.",
        ))
    for row, limitation in ARMY_IDENTITY_ONLY.items():
        values.append(base_update(
            row,
            identity_status="high_confidence" if row == 44 else "confirmed",
            identity_evidence=("A nonshared protected identifier and compatible name evidence connect the index and Army records; the Army row supplies middle initial A, and the identifier remains private." if row == 44 else "A nonshared protected identifier and exact official name agreement connect the index and Army records; the identifier remains private."),
            name_variants=["Emmett A Wofford"] if row == 44 else None,
            replace_name_variants=False,
            personnel_category="enlisted_army_personnel",
            commissioned_officer=False,
            allied_or_foreign_personnel=False,
            research_status="requires_archival_review",
            nara_catalog_id="1263923",
            next_action=f"Review indexed Box {PEOPLE[row][2]} for the pre-OSS employer, unit and chronology. {limitation}",
        ))
    values.extend([
        base_update(FRANK, identity_status="high_confidence", identity_evidence="Exact full name, matching lieutenant commander rank and Navy note, ONI dates, law-firm partnership, and OSS service align.", name_variants=["Frank G. Wisner", "Frank Gardiner Wisner", "Wisner, Frank G"], replace_name_variants=False, personnel_category="commissioned_naval_officer", commissioned_officer=True, allied_or_foreign_personnel=False, manual_review_required=False, research_status="verified_employer_found", archival_review_priority="medium", next_action="Review Box 847 for the precise Carter, Ledyard departure and ONI-to-OSS transfer dates; prior reviewed claims remain authoritative."),
        base_update(WITHROW, identity_status="high_confidence", identity_evidence="The exact name and suffix, Navy lieutenant rank, and direct OSS Far East roles align across scholarly and official military histories.", name_variants=["James R. Withrow Jr.", "Lieutenant James R. Withrow Jr."], replace_name_variants=False, personnel_category="commissioned_naval_officer", commissioned_officer=True, allied_or_foreign_personnel=False, research_status="verified_employer_found", archival_review_priority="medium", next_action="Review Box 847 to establish the exact firm-departure, Navy commission and OSS recruitment dates; the immediate and last civilian employer are already supported."),
        base_update(WITTMANN, identity_status="confirmed", identity_evidence="The exact distinctive name and suffix, matching major rank, museum chronology, Army Air Forces service and OSS ALIU role align across NARA and institutional finding aids.", name_variants=["Otto Wittmann Jr.", "Major Otto Wittmann Jr.", "Otto W. Wittman Jr."], replace_name_variants=False, personnel_category="commissioned_army_officer", commissioned_officer=True, allied_or_foreign_personnel=False, research_status="verified_employer_found", archival_review_priority="medium", next_action="Review Box 848 to verify command-transfer dates and the brief Portland appointment; the last civilian employer and military-to-OSS pathway are already supported."),
        base_update(WLUDYKA, identity_status="confirmed", identity_evidence="The exact uncommon name and a nonshared protected identifier match a direct May 1944 OSS personnel interview that supplies Army and OSS chronology.", name_variants=["Peter S. Wludyka", "T/4 Peter S Wludyka"], replace_name_variants=False, personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="completed", archival_review_priority="medium", next_action="Review Box 848 for the last civilian employer before September 1940 Army entry; the Army-to-OSS Cairo recruitment pathway is already confirmed."),
    ])
    if len(values) != len(PEOPLE):
        raise RuntimeError(f"Expected {len(PEOPLE)} person updates, generated {len(values)}")
    return values


def research_attempts() -> list[dict[str, object]]:
    attempts: list[dict[str, object]] = []
    enriched = {WITHROW, WITTMANN, WLUDYKA}
    for row, (person_id, name, box) in PEOPLE.items():
        outcome, reviewed, rejected = "candidate_rejected", 6, 5
        note = unresolved_reason(row)
        if row in ARMY_OCCUPATIONS:
            outcome, reviewed, rejected = "source_reviewed", 9, 4
            note = f"An accepted Army bridge supports identity and a qualified {ARMY_OCCUPATIONS[row][2]} category at Army entry; no named employer or exact OSS-transfer date is supplied."
        elif row in ARMY_IDENTITY_ONLY:
            outcome, reviewed, rejected = "source_reviewed", 8, 4
            note = f"An accepted Army bridge supports identity only. {ARMY_IDENTITY_ONLY[row]}"
        elif row == FRANK:
            outcome, reviewed, rejected = "source_reviewed", 7, 3
            note = "Prior reviewed evidence remains authoritative: ONI is the immediate military affiliation and Carter, Ledyard & Milburn the last civilian employer."
        elif row in enriched:
            outcome, reviewed, rejected = "source_reviewed", 12, 6
            note = {
                WITHROW: "A scholarly OSS history, official Army history and official 1940 firm record support the Donovan law-firm-to-Navy/OSS sequence.",
                WITTMANN: "NARA and institutional finding aids plus contemporary Skidmore News support the museum-to-Army Air Forces-to-OSS ALIU chronology.",
                WLUDYKA: "A direct May 1944 OSS board report confirms Army entry and recruitment by OSS in Cairo for Services.",
            }[row]
        attempt_number = 2 if row == FRANK else 3 if row == 39 else 1
        attempts.append({
            "key": f"page510-row{row}-{slug(name)}-b1020",
            "person_id": person_id,
            "source_adapter": "manual_staged_protocol",
            "query_text": f"{name}; NARA OSS index context; exact-name and meaningful spelling, initial, suffix, punctuation and OCR variants; OSS, rank, branch, assignment and identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory and archival searches; indexed Box {box}; protected identifiers used only in private official-record comparison",
            "query_variant_type": "staged_identity_employment_archival_protocol_batch_1020",
            "started_at": "2026-11-04T12:20:00Z",
            "completed_at": "2026-11-04T17:10:00Z",
            "outcome": outcome,
            "sources_reviewed": reviewed,
            "candidate_sources_rejected": rejected,
            "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, postwar-only leads, discovery-only biographies and sources without an OSS, protected-identifier, rank, unit or personnel-file bridge were rejected. Army categories were not converted into named employers or institutions.",
            "research_notes": f"{note} The official index, exact-name searches, official OSS context and available employer, occupation, obituary, institutional, newspaper, directory and archival leads were reviewed as applicable. Index page 510 and relevant NARA code-list pages were visually checked. The Withrow book passages, Wittmann finding-aid passages and Skidmore newspaper page were inspected directly. Batch-level CIA and Library of Congress adapters failed closed with access errors recorded separately; those errors are not negative evidence. Accessible official, institutional and scholarly alternatives were reviewed. No authenticated NARA Catalog API request was made.",
            "next_action": f"Review indexed Box {box} for corroborating identifiers, immediate pre-OSS affiliation and last civilian employer before wartime service.",
            "attempt_number": attempt_number,
            "research_agent_version": "before-oss-b1020-v1",
        })
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-1020-v1",
        "reviewer": "Before OSS Batch 1020 evidence review",
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
