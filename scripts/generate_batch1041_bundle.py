#!/usr/bin/env python3
"""Generate the reviewed Batch 1041 evidence bundle for PDF page 296."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page296-richard-s-marnocha-to-robert-f-marszalek-review_"
    "batch-1041_2026-11-05.json"
)

INDEX = "nara-index-b1041"
ARMY = "army-bulk-b1041"
TECH = "army-tech-b1041"
CODES = "army-codes-b1041"
MARQUARD_NARA = "nara-carl-marquard-b1041"
MARQUARD_NAVY = "navy-all-hands-carl-marquard-b1041"
MARQUARD_BIO = "crudo-carl-marquard-b1041"
MARSALES_UW = "uw-hildegarde-marsales-b1041"
MARSALES_OBIT = "cress-hildegarde-marsales-b1041"
MARSCHING_NBC = "nbc-transmitter-john-marsching-b1041"
MARSCHING_BROADCASTING = "broadcasting-john-marsching-b1041"
MARSHALL_SAE = "sae-maclean-marshall-b1041"
MARSHALL_CORNWALL_BIO = "bmh-james-marshall-cornwall-b1041"
MARSHALL_CORNWALL_SOE = "herrington-james-marshall-cornwall-b1041"

ORG_MASCOT = "mascot-pictures-b1041"
ORG_UW = "university-of-wisconsin-b1041"
ORG_KNOX = "knox-school-cooperstown-b1041"
ORG_NBC = "national-broadcasting-company-b1041"
ORG_CAP = "civil-air-patrol-ocd-b1041"
ORG_BRITISH_ARMY = "british-army-b1041"
ORG_SOE = "special-operations-executive-b1041"


PEOPLE = {
    1: ("f2d841bd-ea19-5b97-b16d-7152373af21a", "Richard S Marnocha", "484"),
    2: ("7bce6972-c985-5458-ba14-1b85d53124cf", "Carl J Marold", "484"),
    3: ("75bafb38-7055-5fb6-b51a-62579ee4435d", "Marion J Marosz", "484"),
    4: ("055d603f-37dc-5380-825f-ef574e812fb2", "Michael A Marotti", "484"),
    5: ("e5c96fb8-21a0-5bf0-9375-3a4b3ed7c1b0", "John P Marquand Jr.", "484"),
    6: ("68c3948f-1dfc-5ab9-a6f0-a1a16dcf6a02", "Carl F Marquard", "484"),
    7: ("7d2d7e73-891d-5dea-a0ec-304fac30de21", "Dorothy F Marquardt", "484"),
    8: ("10e38e55-2e4f-599f-b39c-e94a74e2ae6e", "Robert M Marr", "484"),
    9: ("39853fbc-f600-505d-96c2-4d0fee412ec5", "Samuel M Marr", "484"),
    10: ("09aa3679-9c33-5ebc-a5d7-cf89cfee6a3a", "William G Marr", "484"),
    11: ("923da988-8984-5165-985d-91c65a92df81", "Norine Marra", "484"),
    12: ("dc723c9f-7ca6-56fc-86b8-cd1c04431f68", "Donald E Marriner", "484"),
    13: ("84cbf17c-b33e-58d2-ab99-4b7aaf44e83c", "William L Marritts", "484"),
    14: ("c10c2fea-a4cb-553d-b78c-b6cb70ada206", "Joseph Marrone", "484"),
    15: ("552f1ac8-d361-52ac-a8e8-452df59982d9", "Vera D Marrow", "484"),
    16: ("8c645beb-4287-5b8d-b020-3418dcf097b1", "Hildegarde R Marsales", "485"),
    17: ("5d0cef1b-eb8a-58aa-9373-f7a05aea1d9e", "Bernard L Marsalese", "485"),
    18: ("ee0225cf-4f92-5e12-9d79-9d1b797a47cd", "John H Marsching", "485"),
    19: ("6b601dd3-fa9d-54f6-a8e3-06ad674c27bd", "Walter W Marseille", "485"),
    20: ("18e87582-e73c-5ca8-869a-aeda2763c31e", "Joseph J Marsh", "485"),
    21: ("97484653-2192-54d2-9bea-10c29e29932b", "Robert A Marsh", "485"),
    22: ("4fc7c6d6-26a7-51a8-aea0-6dec1041e39f", "Robert W Marsh", "485"),
    23: ("3cf0b0df-6b92-513f-b3cd-1596ceb95198", "Ruth Marsh", "485"),
    24: ("50c70f7c-dfec-5a4e-9c02-5ca83112c7f3", "Timothy R Marsh", "485"),
    25: ("1bab1c93-d7c7-57c4-9632-b325b24c3c2b", "Richard Marshak", "485"),
    26: ("4cde3108-35bc-5a07-9baa-beeb0c4bce0b", "Amy G Marshall", "485"),
    27: ("1c0bf216-76cf-5444-ba1a-ac373bc715ae", "Carl D Marshall", "485"),
    28: ("580a69c2-ad8e-5916-904d-d2f4e24c51ce", "Cornwall Marshall", "485"),
    29: ("46fd4a69-6ebd-55ec-919f-ca3c9c72b393", "Ellis L Marshall", "485"),
    30: ("6f405e2e-0cfb-5e10-bff3-daa3aa97d166", "Ernest A Marshall", "485"),
    31: ("724617a4-e74e-5cf3-bab1-bfcaa5225b91", "Hazel M Marshall", "485"),
    32: ("e7ef659f-dc02-5ca3-8cec-a9e5aa05cb34", "John M Marshall", "485"),
    33: ("152685f3-1427-52d3-b56c-573a0d5e8f6f", "Joseph M Marshall", "485"),
    34: ("f516c142-79c4-5b3d-aee5-f37d24d6dda0", "Lee Marshall", "485"),
    35: ("170b79ee-5ab1-5c01-9434-d12cdb0d291b", "Maclean Marshall", "485"),
    36: ("509ce24d-6acb-526c-82cb-3be6893d137a", "Robert C Marshall", "485"),
    37: ("1681f272-f6e4-594a-b549-ef7511ffd5ce", "Roger D Marshall", "485"),
    38: ("4b09e612-bec5-5c0a-aa44-6e8d15ba2d8e", "Theron W Marshall", "485"),
    39: ("e61fa10a-5f4f-5091-a99c-f3ea987b23dd", "Thoma Marshall", "485"),
    40: ("cd49dd3f-ab06-51d2-a276-956c7c95b363", "Warwick G Marshall Jr.", "485"),
    41: ("e589cafb-9d36-5b4f-b200-91cd452e6508", "William S Marshall", "485"),
    42: ("05d0c7e2-b024-5d5c-a109-d10e9bdcc78b", "Woffard E Marshall", "485"),
    43: ("cf0e34d2-366a-5d72-a306-baa7f81263fb", "James H Marshall-Corn", "485"),
    44: ("38c5f013-1ba1-5ecb-9629-39f564a96f5f", "Charles S Marston", "485"),
    45: ("e4f8e744-f28c-5104-b846-919e59dad3f6", "Horace M Marston", "485"),
    46: ("b11f3d02-9ea0-5e62-8839-0e43ac2edcb6", "Robert F Marszalek", "485"),
}


ARMY_ASSOCIATIONS = {
    2: ("1943-06-07", "022", "lawyer or judge", "Lawyers and judges", "unknown", "PDF physical page 171; historical category 0-22"),
    3: ("1943-05-14", "992", "student", "Students", "student", "PDF physical page 304; corrected historical category 9-92"),
    5: ("1943-02-16", "002", "actor", "Actors and actresses", "unknown", "PDF physical page 304; historical category 0-02"),
    20: ("1944-01-15", "065", "embalmer or undertaker", "Embalmers and undertakers", "unknown", "PDF physical page 171; historical category 0-65"),
    22: ("1942-12-15", "992", "student", "Students", "student", "PDF physical page 304; corrected historical category 9-92"),
    25: ("1942-10-03", "471", "jeweler, watchmaker, goldsmith, or silversmith", "Jewelers, watchmakers, goldsmiths, and silversmiths", "unknown", "PDF physical page 173; historical category 4-71"),
    30: ("1942-11-11", "681", "molder", "Molders", "unknown", "PDF physical page 174; historical category 6-81"),
    33: ("1943-06-23", "138", "stock clerk", "Stock clerks", "unknown", "PDF physical page 171; historical category 1-38"),
    34: ("1944-01-12", "992", "student", "Students", "student", "PDF physical page 304; corrected historical category 9-92"),
    35: ("1943-04-13", "004", "artist, sculptor, or teacher of art", "Artists, sculptors, and teachers of art", "unknown", "PDF physical page 304; historical category 0-04"),
    38: ("1943-05-15", "105", "general office clerk", "Clerks, general office", "unknown", "PDF physical page 171; historical category 1-05"),
    40: ("1941-05-07", "497", "electrician", "Electricians", "unknown", "PDF physical page 174; historical category 4-97"),
    41: ("1941-02-21", "525", "carpenter", "Carpenters", "unknown", "PDF physical page 175; historical category 5-25"),
    44: ("1941-01-16", "861", "boot-and-shoe manufacturing worker", "Occupations in manufacture of boots and shoes", "unknown", "PDF physical page 173; historical category 8-61"),
    46: ("1942-11-20", "992", "student", "Students", "student", "PDF physical page 304; corrected historical category 9-92"),
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def source(key: str, **kwargs: object) -> dict[str, object]:
    value: dict[str, object] = {"key": key, "access_date": "2026-11-05"}
    value.update(kwargs)
    return value


def sources() -> list[dict[str, object]]:
    return [
        source(
            INDEX,
            stable_url="https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            archival_identifier="RG 226, Entry A1-224, Boxes 484-485",
            title="OSS Personnel Files from Excel",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="2010-12-23",
            locator="PDF page 296, rows 1-46; every printed row visually checked at 180 dpi",
            source_quality="A_direct_official",
            collection_name="Records of the Office of Strategic Services, Record Group 226",
            rights_notes="All 46 rows remain separate. Marnocha, Maclean, Thoma, Woffard, Marshall-Corn, and the 'Also Mat' note are preserved exactly; full identifiers stay private.",
        ),
        source(
            ARMY,
            stable_url="https://catalog.archives.gov/id/1263923",
            archival_identifier="National Archives Identifier 1263923; parent series NAID 604357",
            title="Electronic Army Serial Number Merged File, ca. 1938-1946",
            author_creator="Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="1938-1946; merged file created 2002",
            locator="Official unrestricted ASNEF.FIN.DAT; 16 candidates explicitly reviewed; 15 accepted and one rejected",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records",
            document_number="ASNEF.FIN.DAT",
            rights_notes="No raw record, full protected identifier, or bulk-record ordinal is retained in public assets.",
        ),
        source(
            TECH,
            stable_url="https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf",
            archival_identifier="NN3-064-03-008; National Archives Identifier 1263923",
            title="World War II Army Enlistment Records: Reference Copy of Technical Documentation",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives at College Park - Electronic Records",
            publication_record_date="1994-2005; reference copy modified 2011",
            locator="PDF physical pages 44-46; identity, Army-entry-date, grade, and civilian-occupation fields",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records technical documentation",
            rights_notes="Used only to interpret selected fields; source damage and incomplete coverage remain applicable.",
        ),
        source(
            CODES,
            stable_url="https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1CL_SD.pdf",
            archival_identifier="National Archives Identifier 1263923; Code No. 30",
            title="NARA Compiled Code Lists for the Electronic Army Serial Number Merged File",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives at College Park - Electronic Records",
            publication_record_date="2011-01-12; modified 2011-03-17",
            locator="PDF physical pages 171-175 and 304; all cited categories visually checked at 180 dpi",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records technical documentation",
            rights_notes="The categories identify neither employer, institution, workplace, nor exact Army-to-OSS sequence.",
        ),
        source(
            MARQUARD_NARA,
            stable_url="https://unwritten-record.blogs.archives.gov/2025/03/06/only-wac-photographer-in-e-t-o-sergeant-irene-marquardt/",
            title="‘Only Wac Photographer in E.T.O.’: Sergeant Irene Marquardt",
            author_creator="Alex Lange",
            repository_publisher="National Archives, The Unwritten Record",
            publication_record_date="2025-03-06",
            locator="Paragraph identifying Carl F. Marquard Jr. of Los Angeles as a Navy photographer attached to OSS",
            source_quality="B_authoritative_institutional",
            collection_name="National Archives Special Media Division blog",
            rights_notes="Supports the exact Navy/OSS identity; it does not establish pre-OSS employment.",
        ),
        source(
            MARQUARD_NAVY,
            stable_url="https://thenavycwo.com/the-archives/all-hands-magazine?catid=16&id=201%3Aall-hands-june-1946&task=download.send",
            title="All Hands, June 1946",
            author_creator="Bureau of Naval Personnel",
            repository_publisher="United States Navy; digitized by The Navy CWO",
            publication_record_date="1946-06",
            locator="Awards list; Carl F. Marquard, Sp(P)1c, USNR, Hollywood; OSS field photo branch, June 1944",
            source_quality="A_direct_official",
            collection_name="All Hands magazine",
            rights_notes="Direct official rank, location, Navy, and OSS attachment evidence.",
        ),
        source(
            MARQUARD_BIO,
            stable_url="https://normalexposure.com/brick-marquard-asc/",
            title="Brick Marquard, ASC",
            author_creator="Richard Crudo, ASC",
            repository_publisher="Normal Exposure",
            publication_record_date="2025-04-01",
            locator="Biographical paragraphs on the mid-1930s Mascot Pictures work and wartime OSS cinematography",
            source_quality="C_reputable_contemporary_or_scholarly",
            collection_name="Professional cinematography biography",
            rights_notes="Used as a qualified professional biography; the earlier job is not asserted as immediately pre-OSS.",
        ),
        source(
            MARSALES_UW,
            stable_url="https://asset.library.wisc.edu/1711.dl/JVIDJAKT5PDR68X/E/file-64542.pdf?dl=",
            archival_identifier="University of Wisconsin Board of Regents minutes",
            title="Minutes of the regular meeting of the Board",
            author_creator="University of Wisconsin Board of Regents",
            repository_publisher="University of Wisconsin Digital Collections",
            publication_record_date="1943",
            locator="PDF physical page 25, printed page 10; German appointments for the 15-week 1943 summer session",
            source_quality="A_direct_official",
            collection_name="University of Wisconsin Board minutes",
            rights_notes="The page was visually checked at 220 dpi. Compensation is not reproduced publicly.",
        ),
        source(
            MARSALES_OBIT,
            stable_url="https://www.cressfuneralservice.com/obituaries/hildegarde-scheibe",
            title="Hildegarde Scheibe obituary",
            author_creator="Family of Hildegarde Scheibe",
            repository_publisher="Cress Funeral and Cremation Services",
            publication_record_date="2012-08",
            locator="Biographical paragraphs on Knox School, UW-Madison, Washington, and OSS translation work",
            source_quality="C_reputable_contemporary_or_scholarly",
            collection_name="Published obituary",
            rights_notes="The detailed chronology is corroborated by the official 1943 university appointment; no postwar career is used as pre-OSS evidence.",
        ),
        source(
            MARSCHING_NBC,
            stable_url="https://www.worldradiohistory.com/Archive-Station-Albums/Networks/NBC-Transmitter/NBC-Transmitter-1938-Jan.pdf",
            title="NBC Transmitter, Names in the News",
            author_creator="National Broadcasting Company",
            repository_publisher="National Broadcasting Company; digitized by World Radio History",
            publication_record_date="1938",
            locator="PDF physical page 124, printed page 4; visually checked at 200 dpi",
            source_quality="B_authoritative_institutional",
            collection_name="NBC Transmitter",
            rights_notes="The rare-name biography documents NBC, earlier insurance work, and First World War military intelligence but does not itself mention OSS.",
        ),
        source(
            MARSCHING_BROADCASTING,
            stable_url="https://www.worldradiohistory.com/Archive-BC/BC-1939/1939-06-01-BC.pdf",
            title="Broadcasting, June 1, 1939",
            author_creator="Broadcasting magazine",
            repository_publisher="Broadcasting Publications; digitized by World Radio History",
            publication_record_date="1939-06-01",
            locator="PDF physical and printed page 43; visually checked at 200 dpi",
            source_quality="C_reputable_contemporary_or_scholarly",
            collection_name="Broadcasting magazine",
            rights_notes="Contemporary corroboration of the NBC title; the index file is still needed to confirm the probable identity.",
        ),
        source(
            MARSHALL_SAE,
            stable_url="https://saearchives.net/wp-content/uploads/2023/10/1943_Mar_the_record_Vol63_No1__.pdf",
            title="The Record of Sigma Alpha Epsilon, March 1943",
            author_creator="Sigma Alpha Epsilon",
            repository_publisher="Sigma Alpha Epsilon archives",
            publication_record_date="1943-03",
            locator="PDF physical page 24, printed page 22; Virginia Omicron service roster; visually checked at 200 dpi",
            source_quality="C_reputable_contemporary_or_scholarly",
            collection_name="The Record of Sigma Alpha Epsilon",
            rights_notes="The contemporary roster supplies class year, rank, and Civil Air Patrol/OCD affiliation; it is not an employer claim.",
        ),
        source(
            MARSHALL_CORNWALL_BIO,
            stable_url="https://www.britishmilitaryhistory.co.uk/wp-content/uploads/sites/124/2020/12/MARSHALL-CORNWALL-General-Sir-James-Handyside-V1_1.pdf",
            title="A Concise Biography of General Sir James H. Marshall-Cornwall",
            author_creator="Robert Palmer, M.A.; assisted by Stephen Heal",
            repository_publisher="BritishMilitaryHistory.co.uk",
            publication_record_date="2020-12-03",
            locator="PDF pages 1 and 9; British Army, Western Command, War Office, and 4 January 1943 retirement chronology",
            source_quality="C_reputable_contemporary_or_scholarly",
            collection_name="British Military History biographies",
            rights_notes="Used as a sourced secondary biography; the clipped index spelling and possible duplicate row remain visible.",
        ),
        source(
            MARSHALL_CORNWALL_SOE,
            stable_url="https://dora.dmu.ac.uk/bitstream/handle/2086/2421/Ian%20Herrington%20PhD.pdf",
            archival_identifier="De Montfort University doctoral thesis",
            title="The Special Operations Executive in Norway 1940-1945: Policy and Operations in the Strategic and Political Context",
            author_creator="Ian Herrington",
            repository_publisher="De Montfort University",
            publication_record_date="2004",
            locator="Printed page 175 and note 135; January 11, 1943 Kingston House meeting on OSS activities in Norway",
            source_quality="C_reputable_contemporary_or_scholarly",
            collection_name="De Montfort University research repository",
            rights_notes="The thesis cites the underlying PRO meeting précis and identifies Sir James Marshall-Cornwall as SOE; exact OSS personnel status remains unresolved.",
        ),
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {"key": ORG_MASCOT, "canonical_name": "Mascot Pictures", "historical_name": "Mascot Pictures", "organization_type": "motion-picture studio", "sector": "arts_and_culture", "city": "Los Angeles", "state_or_region": "California", "country": "United States", "active_dates": "1927-1935", "normalization_notes": "Historical studio name preserved; no Republic Pictures successor is substituted."},
        {"key": ORG_UW, "canonical_name": "University of Wisconsin", "historical_name": "University of Wisconsin", "aliases": ["UW-Madison"], "organization_type": "university", "sector": "academia_and_research", "city": "Madison", "state_or_region": "Wisconsin", "country": "United States", "normalization_notes": "The 1943 institutional name is preserved; employment and student status remain distinct."},
        {"key": ORG_KNOX, "canonical_name": "Knox School", "historical_name": "Knox School", "organization_type": "school", "sector": "academia_and_research", "city": "Cooperstown", "state_or_region": "New York", "country": "United States", "normalization_notes": "The obituary's historical school name is preserved without inferring a modern successor."},
        {"key": ORG_NBC, "canonical_name": "National Broadcasting Company", "historical_name": "National Broadcasting Company", "aliases": ["NBC"], "organization_type": "broadcast network", "sector": "journalism_and_media", "city": "New York", "state_or_region": "New York", "country": "United States", "normalization_notes": "Historical corporate name preserved; the international division and German section remain subordinate units."},
        {"key": ORG_CAP, "canonical_name": "Civil Air Patrol", "historical_name": "Civil Air Patrol, Office of Civilian Defense", "aliases": ["Civil Air Patrol OCD", "CAP"], "organization_type": "civil-defense aviation organization", "sector": "federal_government", "country": "United States", "active_dates": "Under Office of Civilian Defense, 1941-April 1943", "normalization_notes": "The contemporary 'Civil Air Patrol, OCD' wording is preserved; volunteer service is not labeled civilian employment."},
        {"key": ORG_BRITISH_ARMY, "canonical_name": "British Army", "historical_name": "British Army", "organization_type": "military service", "sector": "military", "country": "United Kingdom", "normalization_notes": "Branch-level entity; Western Command and War Office duties are preserved in the affiliation rather than silently merged with SOE."},
        {"key": ORG_SOE, "canonical_name": "Special Operations Executive", "historical_name": "Special Operations Executive", "aliases": ["SOE"], "organization_type": "wartime government organization", "sector": "federal_government", "country": "United Kingdom", "active_dates": "1940-1946", "normalization_notes": "Kept separate from OSS and MI5; the cited source establishes a 1943 SOE role but not OSS employment."},
    ]


def army_affiliation_key(row: int) -> str:
    return f"{slug(PEOPLE[row][1])}-army-association-b1041"


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, _label, relationship, _locator) in ARMY_ASSOCIATIONS.items():
        item: dict[str, object] = {
            "key": army_affiliation_key(row),
            "person_id": PEOPLE[row][0],
            "relationship_type": relationship,
            "end_date": date,
            "date_precision": f"Historical civilian-occupation code {code} was recorded at Army entry on {date}; no named employer, institution, or workplace is supplied.",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "confirmed",
            "claim_confidence": "medium",
            "source_quality": "A_direct_official",
            "publication_status": "publish_qualified",
            "research_notes": "The broad historical category is excluded from verified-employer analytics and is not converted into a named organization.",
        }
        if relationship == "student":
            item["role_title"] = "student"
        else:
            item["occupation"] = occupation
        values.append(item)

    values.extend(
        [
            {"key": "carl-f-marquard-mascot-b1041", "person_id": PEOPLE[6][0], "organization_key": ORG_MASCOT, "organization_name_as_found": "Mascot Pictures", "role_title": "assistant cameraman", "occupation": "camera worker", "relationship_type": "employment", "start_date": "mid-1930s", "date_precision": "The professional biography dates the role only to the mid-1930s; later pre-OSS work and the immediate transition remain unknown.", "city": "Los Angeles", "state_or_region": "California", "country": "United States", "immediate_pre_oss": False, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "confirmed", "claim_confidence": "medium", "source_quality": "C_reputable_contemporary_or_scholarly", "publication_status": "publish_qualified", "research_notes": "A documented earlier employer, not the claimed immediate predecessor to OSS."},
            {"key": "hildegarde-r-marsales-uw-b1041", "person_id": PEOPLE[16][0], "organization_key": ORG_UW, "organization_name_as_found": "University of Wisconsin", "role_title": "German instructor", "occupation": "language instructor", "relationship_type": "employment", "start_date": "1943", "end_date": "1943", "date_precision": "Official board minutes list a 15-week 1943 summer appointment under German; the obituary then sequences her move to Washington and OSS work.", "city": "Madison", "state_or_region": "Wisconsin", "country": "United States", "immediate_pre_oss": True, "last_civilian_pre_service": True, "pre_oss_temporal_basis": "probable_immediate", "identity_confidence": "high_confidence", "claim_confidence": "high", "source_quality": "A_direct_official", "publication_status": "published", "research_notes": "Employment is direct; immediacy is qualified because the exact OSS start date is absent."},
            {"key": "hildegarde-r-marsales-knox-b1041", "person_id": PEOPLE[16][0], "organization_key": ORG_KNOX, "organization_name_as_found": "Knox School", "role_title": "French and German teacher", "occupation": "teacher", "relationship_type": "employment", "start_date": "1936", "end_date": "1939", "date_precision": "The obituary says she taught there for two years after her 1936 Vassar graduation and before graduate study beginning in 1939; exact dates are approximate.", "city": "Cooperstown", "state_or_region": "New York", "country": "United States", "immediate_pre_oss": False, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "high_confidence", "claim_confidence": "medium", "source_quality": "C_reputable_contemporary_or_scholarly", "publication_status": "publish_qualified", "research_notes": "Earlier documented employment, not the last role before OSS."},
            {"key": "john-h-marsching-nbc-b1041", "person_id": PEOPLE[18][0], "organization_key": ORG_NBC, "organization_name_as_found": "NBC", "role_title": "chief, German section, International Program Division", "occupation": "broadcasting executive", "relationship_type": "employment", "start_date": "1938", "end_date": "1939", "date_precision": "NBC announced the appointment in 1938 and Broadcasting still identified the role in June 1939; later chronology is unknown.", "city": "New York", "state_or_region": "New York", "country": "United States", "immediate_pre_oss": False, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "documented_prewar", "identity_confidence": "probable", "claim_confidence": "medium", "source_quality": "B_authoritative_institutional", "publication_status": "publish_qualified", "research_notes": "Rare-name probable match. Box 485 is still needed for a direct bridge and later sequence."},
            {"key": "maclean-marshall-cap-b1041", "person_id": PEOPLE[35][0], "organization_key": ORG_CAP, "organization_name_as_found": "Civil Air Patrol, OCD", "role_title": "second lieutenant", "relationship_type": "volunteer", "end_date": "1943-03", "date_precision": "A March 1943 roster identifies the affiliation; the official Army record dates Army entry to 13 April 1943.", "country": "United States", "immediate_pre_oss": False, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "strongly_date_bounded", "identity_confidence": "confirmed", "claim_confidence": "high", "source_quality": "C_reputable_contemporary_or_scholarly", "publication_status": "published", "research_notes": "A pre-Army civil-defense affiliation, not employment and not proven to be the immediate OSS predecessor."},
            {"key": "james-h-marshall-corn-british-army-b1041", "person_id": PEOPLE[43][0], "organization_key": ORG_BRITISH_ARMY, "organization_name_as_found": "British Army", "role_title": "general; Western Command and War Office liaison duties", "relationship_type": "military_assignment", "start_date": "1941-12-01", "end_date": "1943-01-04", "date_precision": "The biography dates Western Command, the later War Office work involving SOE and MI5, and Army retirement.", "country": "United Kingdom", "immediate_pre_oss": False, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "temporal_relation_uncertain", "identity_confidence": "high_confidence", "claim_confidence": "medium", "source_quality": "C_reputable_contemporary_or_scholarly", "publication_status": "publish_qualified", "research_notes": "The index row is clipped and has a possible same-box duplicate; no direct transfer to OSS is asserted."},
            {"key": "james-h-marshall-corn-soe-b1041", "person_id": PEOPLE[43][0], "organization_key": ORG_SOE, "organization_name_as_found": "SOE", "role_title": "SOE representative in an OSS liaison meeting", "relationship_type": "government_assignment", "start_date": "1943-01-11", "end_date": "1943-01-11", "date_precision": "The scholarly source cites a meeting précis and identifies Sir James Marshall-Cornwall as SOE at the 11 January 1943 meeting.", "country": "United Kingdom", "immediate_pre_oss": False, "last_civilian_pre_service": False, "pre_oss_temporal_basis": "temporal_relation_uncertain", "identity_confidence": "high_confidence", "claim_confidence": "high", "source_quality": "C_reputable_contemporary_or_scholarly", "publication_status": "published", "research_notes": "A documented SOE affiliation during OSS liaison, not proof that he joined OSS."},
        ]
    )
    return values


def army_identity_assessment(row: int) -> str:
    if row == 35:
        return "Confirmed by a nonshared protected linkage and the spacing-only Maclean/Mac Lean variant; the protected identifier remains private."
    return "Confirmed by exact official name agreement and a nonshared protected linkage; the protected identifier remains private."


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, label, relationship, locator) in ARMY_ASSOCIATIONS.items():
        values.append(
            {
                "key": f"army-{slug(PEOPLE[row][1])}-b1041",
                "person_id": PEOPLE[row][0],
                "affiliation_key": army_affiliation_key(row),
                "claim_type": "other_pre_oss_affiliation" if relationship == "student" else "occupation",
                "claim_text": f"At Army entry on {date}, {PEOPLE[row][1]} was recorded as {occupation}; no employer, institution, or workplace is identified.",
                "evidence_paraphrase": f"The Army bulk file records code {code}; the visually checked official list defines the category as {label}.",
                "identity_match_assessment": army_identity_assessment(row),
                "temporal_assessment": "Strongly date-bounded to Army entry, but not proven to be the immediately preceding role or status before OSS.",
                "source_quality": "A_direct_official",
                "claim_confidence": "medium",
                "publication_status": "publish_qualified",
                "match_notes": "The historical category is qualified, excluded from verified-employer analytics, and not converted into a named organization.",
                "sources": [{"source_key": INDEX}, {"source_key": ARMY}, {"source_key": TECH, "support_type": "context_only"}, {"source_key": CODES, "locator_override": locator}],
            }
        )

    values.extend(
        [
            {"key": "identity-carl-f-marquard-b1041", "person_id": PEOPLE[6][0], "claim_type": "identity", "claim_text": "Indexed Carl F. Marquard is confirmed as Navy photographer Carl F. ‘Brick’ Marquard Jr., attached to an OSS field photo branch.", "evidence_paraphrase": "The NARA account and official Navy awards list align on the exact name, Navy photography role, Los Angeles/Hollywood, and OSS attachment.", "identity_match_assessment": "Confirmed by exact name, matching specialist-photographer rank, Navy branch, location, and direct OSS attachment in two official sources.", "temporal_assessment": "Wartime identity evidence; it does not by itself establish an earlier employer.", "source_quality": "A_direct_official", "claim_confidence": "confirmed", "publication_status": "published", "match_notes": "Carl Fred and Brick are published as documented variants while the index spelling remains unchanged.", "sources": [{"source_key": MARQUARD_NARA}, {"source_key": MARQUARD_NAVY}, {"source_key": INDEX, "support_type": "context_only"}]},
            {"key": "mascot-carl-f-marquard-b1041", "person_id": PEOPLE[6][0], "affiliation_key": "carl-f-marquard-mascot-b1041", "claim_type": "other_pre_oss_affiliation", "claim_text": "Carl F. ‘Brick’ Marquard worked as an assistant cameraman at Mascot Pictures in the mid-1930s.", "evidence_paraphrase": "A professional biography by a former ASC president identifies the studio and role before describing Marquard's wartime OSS cinematography.", "identity_match_assessment": "Confirmed wartime identity from two official sources; the distinctive full name and cinematography career connect the earlier job.", "temporal_assessment": "Documented earlier prewar employment; not shown to be the immediate predecessor to OSS.", "source_quality": "C_reputable_contemporary_or_scholarly", "claim_confidence": "medium", "publication_status": "publish_qualified", "match_notes": "Excluded from immediate-employer analytics pending a fuller 1935-1942 chronology.", "sources": [{"source_key": MARQUARD_BIO}, {"source_key": MARQUARD_NARA, "support_type": "context_only"}, {"source_key": MARQUARD_NAVY, "support_type": "context_only"}]},
            {"key": "identity-hildegarde-r-marsales-b1041", "person_id": PEOPLE[16][0], "claim_type": "identity", "claim_text": "Hildegarde R. Marsales is strongly identified as Hildegarde Marsales Scheibe, the UW German instructor who later performed German translation work for OSS.", "evidence_paraphrase": "The exact uncommon name appears in official university minutes; the detailed obituary supplies the same UW, language, Washington, and OSS chronology.", "identity_match_assessment": "High confidence from exact uncommon name and middle initial, language specialization, UW chronology, Washington move, and explicit OSS work.", "temporal_assessment": "The university appointment is dated to 1943; the exact OSS start date is not supplied.", "source_quality": "A_direct_official", "claim_confidence": "high", "publication_status": "published", "match_notes": "The marriage surname is retained as a documented variant, not substituted for the index name.", "sources": [{"source_key": MARSALES_UW}, {"source_key": MARSALES_OBIT}, {"source_key": INDEX, "support_type": "context_only"}]},
            {"key": "uw-hildegarde-r-marsales-immediate-b1041", "person_id": PEOPLE[16][0], "affiliation_key": "hildegarde-r-marsales-uw-b1041", "claim_type": "immediate_pre_oss_affiliation", "claim_text": "Hildegarde R. Marsales's probable immediate pre-OSS affiliation was German-language teaching at the University of Wisconsin in 1943.", "evidence_paraphrase": "Official minutes record the summer appointment; the obituary then sequences her incomplete doctorate, move to Washington, and OSS translation work.", "identity_match_assessment": "High-confidence exact-name and language-career match across official and detailed biographical sources.", "temporal_assessment": "Probable immediate: the dated role precedes the described move to Washington, but the exact OSS appointment date is absent.", "source_quality": "A_direct_official", "claim_confidence": "high", "publication_status": "published", "match_notes": "The role is direct employment; the immediacy badge remains qualified.", "sources": [{"source_key": MARSALES_UW, "locator_override": "PDF physical page 25, printed page 10"}, {"source_key": MARSALES_OBIT}]},
            {"key": "uw-hildegarde-r-marsales-last-civilian-b1041", "person_id": PEOPLE[16][0], "affiliation_key": "hildegarde-r-marsales-uw-b1041", "claim_type": "last_civilian_pre_service", "claim_text": "The University of Wisconsin is Hildegarde R. Marsales's last documented civilian employer before her OSS work.", "evidence_paraphrase": "The reviewed chronology places the 1943 university appointment before her Washington move and OSS translation work, with no intervening employer named.", "identity_match_assessment": "High-confidence exact-name and language-career match.", "temporal_assessment": "Strongly date-bounded last documented civilian employer; the absence of exact transition dates prevents an unqualified immediate claim.", "source_quality": "A_direct_official", "claim_confidence": "high", "publication_status": "published", "match_notes": "Last documented does not mean no other affiliation existed.", "sources": [{"source_key": MARSALES_UW}, {"source_key": MARSALES_OBIT}]},
            {"key": "knox-hildegarde-r-marsales-b1041", "person_id": PEOPLE[16][0], "affiliation_key": "hildegarde-r-marsales-knox-b1041", "claim_type": "other_pre_oss_affiliation", "claim_text": "Before graduate study, Hildegarde Marsales taught French and German at the Knox School in Cooperstown for two years.", "evidence_paraphrase": "The detailed obituary explicitly names the school, subjects, and two-year duration after her 1936 Vassar graduation.", "identity_match_assessment": "High-confidence exact-name and language-career match, corroborated by the later official UW appointment.", "temporal_assessment": "Documented earlier prewar employment; not the final role before OSS.", "source_quality": "C_reputable_contemporary_or_scholarly", "claim_confidence": "medium", "publication_status": "publish_qualified", "match_notes": "Approximate 1936-1939 bounds are derived from the stated two-year role and 1939 graduate-school start.", "sources": [{"source_key": MARSALES_OBIT}, {"source_key": MARSALES_UW, "support_type": "context_only"}]},
            {"key": "nbc-john-h-marsching-b1041", "person_id": PEOPLE[18][0], "affiliation_key": "john-h-marsching-nbc-b1041", "claim_type": "other_pre_oss_affiliation", "claim_text": "A probable identity candidate for indexed John H. Marsching became chief of NBC's German section in 1938 and still held that role in June 1939.", "evidence_paraphrase": "NBC's employee publication gives the appointment and rare-name biography; a contemporary trade magazine independently confirms the title.", "identity_match_assessment": "Probable from the exceptionally rare exact name and middle initial plus a military-intelligence, German-language, and wartime-relevant career; Box 485 is unreviewed.", "temporal_assessment": "Documented prewar employment for the probable candidate; the later NBC-to-OSS sequence is unknown.", "source_quality": "B_authoritative_institutional", "claim_confidence": "medium", "publication_status": "publish_qualified", "match_notes": "Displayed as qualified evidence and excluded from default employer analytics.", "sources": [{"source_key": MARSCHING_NBC, "locator_override": "PDF physical page 124, printed page 4"}, {"source_key": MARSCHING_BROADCASTING, "locator_override": "PDF page 43"}, {"source_key": INDEX, "support_type": "context_only"}]},
            {"key": "cap-maclean-marshall-b1041", "person_id": PEOPLE[35][0], "affiliation_key": "maclean-marshall-cap-b1041", "claim_type": "other_pre_oss_affiliation", "claim_text": "In March 1943, MacLean Marshall was listed as a Civil Air Patrol second lieutenant under the Office of Civilian Defense, immediately before Army entry.", "evidence_paraphrase": "A contemporary roster records Civil Air Patrol/OCD and class year 1936; the accepted Army record dates entry to 13 April 1943.", "identity_match_assessment": "Confirmed by the distinctive spacing-only name variant, contemporary chronology, and nonshared protected Army linkage.", "temporal_assessment": "Strongly date-bounded pre-Army affiliation; not proven to be the immediate affiliation before OSS.", "source_quality": "C_reputable_contemporary_or_scholarly", "claim_confidence": "high", "publication_status": "published", "match_notes": "Modeled as volunteer civil-defense service rather than employment.", "sources": [{"source_key": MARSHALL_SAE}, {"source_key": ARMY}, {"source_key": INDEX, "support_type": "context_only"}]},
            {"key": "identity-james-h-marshall-corn-b1041", "person_id": PEOPLE[43][0], "claim_type": "identity", "claim_text": "The clipped index entry James H. Marshall-Corn is strongly supported as General Sir James Handyside Marshall-Cornwall.", "evidence_paraphrase": "The clipped surname and initials align with a distinctive British general whose 1942-43 work directly involved SOE, MI5, and OSS liaison.", "identity_match_assessment": "High confidence from the rare clipped hyphenated name, exact initials, same wartime liaison sphere, and direct SOE/OSS meeting evidence; Box 485 remains unreviewed.", "temporal_assessment": "Identity and wartime institutional context are supported; the exact reason for the OSS index file is still unresolved.", "source_quality": "C_reputable_contemporary_or_scholarly", "claim_confidence": "high", "publication_status": "published", "match_notes": "A same-box Cornwall Marshall row is preserved as a possible duplicate rather than merged.", "sources": [{"source_key": MARSHALL_CORNWALL_BIO}, {"source_key": MARSHALL_CORNWALL_SOE}, {"source_key": INDEX, "support_type": "context_only"}]},
            {"key": "british-army-james-h-marshall-corn-b1041", "person_id": PEOPLE[43][0], "affiliation_key": "james-h-marshall-corn-british-army-b1041", "claim_type": "other_pre_oss_affiliation", "claim_text": "James Handyside Marshall-Cornwall commanded British Western Command before War Office work involving relations between SOE and MI5, retiring from the Army on 4 January 1943.", "evidence_paraphrase": "The sourced military biography gives the Western Command, War Office liaison, and retirement sequence.", "identity_match_assessment": "High-confidence rare-name and wartime-liaison match to the clipped index entry.", "temporal_assessment": "Documented wartime military assignment; its precise relation to the OSS index file is uncertain.", "source_quality": "C_reputable_contemporary_or_scholarly", "claim_confidence": "medium", "publication_status": "publish_qualified", "match_notes": "Not labeled immediate pre-OSS because no transfer into OSS is documented.", "sources": [{"source_key": MARSHALL_CORNWALL_BIO}, {"source_key": INDEX, "support_type": "context_only"}]},
            {"key": "soe-james-h-marshall-corn-b1041", "person_id": PEOPLE[43][0], "affiliation_key": "james-h-marshall-corn-soe-b1041", "claim_type": "other_pre_oss_affiliation", "claim_text": "On 11 January 1943, Sir James Marshall-Cornwall represented SOE at a meeting about OSS activities in Norway.", "evidence_paraphrase": "The scholarly study cites the underlying British meeting précis and labels Marshall-Cornwall as SOE.", "identity_match_assessment": "High-confidence rare-name, initials, and SOE/OSS liaison-context match.", "temporal_assessment": "Dated institutional affiliation during OSS liaison; it does not establish that he joined OSS.", "source_quality": "C_reputable_contemporary_or_scholarly", "claim_confidence": "high", "publication_status": "published", "match_notes": "SOE remains distinct from OSS; the index-file relationship requires archival review.", "sources": [{"source_key": MARSHALL_CORNWALL_SOE}, {"source_key": MARSHALL_CORNWALL_BIO, "support_type": "context_only"}]},
        ]
    )
    return values


def base_update(row: int) -> dict[str, object]:
    person_id, name, box = PEOPLE[row]
    detail = ""
    if row == 37:
        detail = " The printed note 'Also Mat' is preserved without expansion or inference."
    if row == 39:
        detail = " The printed first name Thoma is preserved without silently changing it to Thomas."
    if row == 42:
        detail = " Woffard is preserved as printed; Wofford search variants did not establish a reliable bridge."
    return {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified page 296 source preserves {name}, Box {box}, rank or grade when printed, notes when present, and archive location.{detail} Staged official, exact-name, employment, occupation, obituary, institutional, newspaper, directory, and archival searches did not establish a defensible identity-and-affiliation bridge.",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": f"Review indexed Box {box} for corroborating identifiers, immediate pre-OSS affiliation, and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }


def person_updates() -> list[dict[str, object]]:
    updates = [base_update(row) for row in PEOPLE]
    by_row = {row: update for row, update in zip(PEOPLE, updates, strict=True)}

    for row in ARMY_ASSOCIATIONS:
        by_row[row].update(
            identity_status="confirmed",
            identity_evidence=army_identity_assessment(row),
            personnel_category="enlisted_army_personnel",
            commissioned_officer=False,
            allied_or_foreign_personnel=False,
            nara_catalog_id="1263923",
            research_status="occupation_only_found",
            next_action=f"Review Box {PEOPLE[row][2]} to identify a named employer or institution and establish Army-to-OSS chronology. The protected Army link supplies only a broad historical occupation or student-status category.",
        )

    by_row[1].update(identity_status="ambiguous", identity_evidence="The index prints Richard S. Marnocha, while page 295 prints Richard S. Marnocaa with a related protected-identifier conflict. Both rows remain separate and no spelling correction or merge was made.", possible_duplicate_group="p295-296-richard-s-marnocaa-marnocha-b622", research_status="needs_identity_review", archival_review_priority="critical", next_action="Jointly review Boxes 484, the original index cards, and protected identifier evidence for Richard S. Marnocha and Richard S. Marnocaa before correcting or merging either row.")
    by_row[13].update(identity_status="conflicting", identity_evidence="The index prints Marritts while the Army candidate prints Merritts, and the protected identifier is shared across three separately printed index spellings. The candidate was rejected and no Army fields were transferred.", possible_duplicate_group="p296-317-william-l-marritts-variants-b622", research_status="conflicting_sources", archival_review_priority="critical", next_action="Jointly review Boxes 484 and 519, the original index cards, and the shared protected-identifier records for Marritts, Meritts, and Merritts before any merge or spelling correction.")
    by_row[6].update(identity_status="confirmed", identity_evidence="The exact name, Navy specialist-photographer rank, Los Angeles/Hollywood location, and direct OSS field-photo attachment align across the index and two official sources.", name_variants=["Carl F. Marquard Jr.", "Carl Fred Marquard", "Brick Marquard"], replace_name_variants=False, personnel_category="enlisted_naval_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="documented_prewar_employer_found", archival_review_priority="medium", next_action="Review Box 484 to identify Marquard's final civilian employer before Navy/OSS service and the exact Mascot-to-wartime chronology; Mascot Pictures is documented only as an earlier employer.")
    by_row[16].update(identity_status="high_confidence", identity_evidence="The exact uncommon name and middle initial, language specialization, official 1943 UW appointment, Washington move, and explicit OSS translation work converge.", name_variants=["Hildegarde Marsales Scheibe", "Hildegarde M. Scheibe"], replace_name_variants=False, research_status="verified_employer_found", archival_review_priority="medium", next_action="Review Box 485 to confirm the exact UW departure and OSS appointment dates; University of Wisconsin is already the last documented civilian employer and probable immediate affiliation.")
    by_row[18].update(identity_status="probable", identity_evidence="Two contemporary publications identify an exceptionally rare exact-name John H. Marsching as NBC's German-section chief, a First World War military-intelligence major, and former insurance broker. Box 485 still lacks a direct external bridge.", research_status="documented_prewar_employer_found", archival_review_priority="critical", next_action="Review Box 485 for NBC, German-language, education, and military-intelligence identifiers before raising the probable John H. Marsching match above medium confidence or identifying his immediate pre-OSS employer.")
    by_row[24] = {"person_id": PEOPLE[24][0], "manual_review_required": True, "research_status": "verified_employer_found", "next_action": "Review Box 485 for the civilian Signal Corps work location, exact employment dates, and OSS contract paperwork.", "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "medium"}
    by_row[27] = {"person_id": PEOPLE[27][0], "manual_review_required": True, "research_status": "requires_archival_review", "next_action": "Review Box 485 and Army service records using private protected-identifier evidence to distinguish Carl D. Marshall from namesakes and establish any pre-OSS employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.", "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "high"}
    duplicate_group = "p296-cornwall-marshall-james-h-marshall-corn-b1041"
    by_row[28].update(identity_status="ambiguous", identity_evidence="The same Box 485 contains Cornwall Marshall and the clipped James H. Marshall-Corn row. Their ordering may point to Sir James Handyside Marshall-Cornwall, but the two printed rows remain separate and unmerged.", possible_duplicate_group=duplicate_group, research_status="needs_identity_review", archival_review_priority="critical", next_action="Review both Box 485 index cards and personnel-file contents together before assigning the Marshall-Cornwall biography to Cornwall Marshall or merging the two source rows.")
    by_row[35].update(name_variants=["MacLean Marshall", "Mac Lean Marshall"], replace_name_variants=False, next_action="Review Box 485 to identify a named civilian employer and the Army-to-OSS sequence. The Civil Air Patrol/OCD affiliation and broad Army-entry occupation category are documented, but neither supplies a named employer.")
    by_row[43].update(identity_status="high_confidence", identity_evidence="The rare clipped Marshall-Corn surname, exact James H. initials, British general chronology, War Office SOE/MI5 liaison, and a January 1943 SOE/OSS meeting strongly support Sir James Handyside Marshall-Cornwall.", name_variants=["Sir James Handyside Marshall-Cornwall", "James H. Marshall-Cornwall"], replace_name_variants=False, possible_duplicate_group=duplicate_group, personnel_category="foreign_or_allied_military_personnel", commissioned_officer=True, allied_or_foreign_personnel=True, research_status="needs_identity_review", archival_review_priority="critical", next_action="Review both Box 485 source rows and file contents to resolve the possible Cornwall Marshall duplicate and establish why Marshall-Cornwall received an OSS personnel-index file; no OSS employment is inferred.")

    updates = [by_row[row] for row in PEOPLE]
    if len(updates) != 46:
        raise RuntimeError(f"Expected 46 person updates, generated {len(updates)}")
    return updates


def outcome_note(row: int) -> str:
    notes = {
        1: "The adjacent Marnocha/Marnocaa spelling and protected-linkage conflict remains unresolved and unmerged.",
        6: "Official Navy/OSS evidence confirms Carl F. Marquard; Mascot Pictures is retained only as earlier documented employment.",
        13: "The shared protected identifier and Marritts/Merritts/Meritts spelling conflict was rejected without field transfer.",
        16: "Official university minutes and a detailed obituary support UW German employment, earlier Knox School teaching, and later OSS translation work.",
        18: "Two contemporary broadcasting publications support a medium-confidence probable NBC identity; a direct personnel-file bridge remains necessary.",
        24: "Existing reviewed Signal Corps and Coyne Radio School evidence was rechecked and preserved without duplication or downgrade.",
        27: "Eighteen prior attempts and the current staged review still do not establish a defensible Carl D. Marshall employer.",
        28: "Cornwall Marshall remains a separate possible duplicate of the clipped James H. Marshall-Corn row.",
        35: "The accepted Army link and a contemporary roster support MacLean Marshall's broad occupation category and Civil Air Patrol/OCD affiliation.",
        43: "British military and scholarly evidence strongly supports Marshall-Cornwall and documents SOE/OSS liaison, but the possible same-box duplicate remains unresolved.",
    }
    return notes.get(row, "Unbridged namesakes, snippets, commercial people-finder pages, unsourced genealogy, relatives, and postwar-only leads did not establish a reliable identity or pre-OSS affiliation.")


def research_attempts() -> list[dict[str, object]]:
    updates = {item["person_id"]: item for item in person_updates()}
    substantiated = set(ARMY_ASSOCIATIONS) | {6, 16, 18, 24, 35, 43}
    candidate_review = {1, 13, 28}
    values: list[dict[str, object]] = []
    for row, (person_id, name, box) in PEOPLE.items():
        outcome = "source_reviewed" if row in substantiated else "candidate_found" if row in candidate_review else "candidate_rejected"
        attempt_number = 2 if row == 24 else 19 if row == 27 else 1
        values.append(
            {
                "key": f"page296-row{row}-{slug(name)}-b1041",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index context; exact-name and meaningful initial, suffix, alias, punctuation and OCR variants; OSS and CIA Reading Room context; rank, branch, assignment and protected-identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory and archival searches; indexed Box {box}",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_1041",
                "started_at": "2026-11-05T08:00:00-05:00",
                "completed_at": "2026-11-05T10:20:00-05:00",
                "outcome": outcome,
                "sources_reviewed": 10 if row in substantiated else 6,
                "candidate_sources_rejected": 3 if row in substantiated else 5,
                "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, and postwar-only leads were rejected. Conflicting or shared-identifier Army candidates were rejected. Army categories were not converted into named employers.",
                "research_notes": f"{outcome_note(row)} The official index, exact-name OSS searches, targeted CIA and institutional context, employment and occupation searches, and newspaper, obituary, directory, and archival sources were reviewed as applicable. Page 296 and every cited PDF evidence page were visually checked. No authenticated NARA Catalog API request was made.",
                "next_action": str(updates[person_id]["next_action"]),
                "attempt_number": attempt_number,
                "research_agent_version": "before-oss-b1041-v1",
            }
        )
    if len(values) != 46:
        raise RuntimeError(f"Expected 46 research attempts, generated {len(values)}")
    return values


def main() -> None:
    bundle = {
        "bundle_version": "batch-1041-v1",
        "reviewer": "Before OSS Batch 1041 evidence review",
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
