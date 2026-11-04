#!/usr/bin/env python3
"""Generate the reviewed Batch 1033 backfill bundle for PDF page 288."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page288-sylvia-macdonald-to-roderick-maclennan-review_"
    "batch-1033_2026-11-04.json"
)

INDEX = "nara-index-b1033"
ARMY = "army-bulk-b1033"
TECH = "army-tech-b1033"
CODES = "army-codes-b1033"
FRASER_MACFARLAND = "fraser-macfarland-b1033"
OSS_MACFARLAND = "oss-seesi-macfarland-b1033"
CIA_MACFARLAND = "cia-field-conditions-macfarland-b1033"
NIXON_MACGREGOR = "nixon-macgregor-b1033"
DARTMOUTH_MACGREGOR = "dartmouth-macgregor-b1033"
GOOGLE_MACK = "google-books-gerstle-mack-b1033"
NLI_MACK = "nli-gerstle-mack-b1033"
BERKELEY_MACKINNON = "berkeley-in-memoriam-mackinnon-b1033"
BERKELEY_PSYCH = "berkeley-psych-history-mackinnon-b1033"

ORG_NORTHERN_TRUST = "northern-trust-company-b1033"
ORG_DARTMOUTH = "dartmouth-existing-b1033"
ORG_ARMY = "us-army-existing-b1033"
ORG_BRYN_MAWR = "bryn-mawr-existing-b1033"


PEOPLE = {
    1: ("059e882a-14c0-5cd8-bab4-ae438fd6ea75", "Sylvia H MacDonald", "470"),
    2: ("04b3760d-6bf4-5154-82cd-62a0ba70d850", "William I MacDonald", "470"),
    3: ("478e93a3-1003-5dbe-afad-fce0614a7525", "Andrew S MacDowell", "470"),
    4: ("620abb72-c1e1-5359-9b9d-0846590c89b4", "Howard A Mace", "470"),
    5: ("2a6b3d58-409a-5abf-9a55-f4086aabfb65", "Lanning MacFarland", "471"),
    6: ("d32bbfd2-3542-502d-91fc-ca6c158041c6", "Donald C MacFarlane", "471"),
    7: ("a5987bdb-67ab-54b3-980c-908b6fefea23", "Clark MacGregor", "471"),
    8: ("438a3e9f-1de4-50de-980e-b68f2d9b8e98", "Clark MacGregor", "471"),
    9: ("9745a109-ff5f-5ec5-8e82-9418d0b58331", "David B MacGregor", "471"),
    10: ("53d5dc82-0e8a-53c2-bd01-fc629722875b", "George E MacGregor", "471"),
    11: ("08c6e161-92e9-5e48-bdf5-fbd8dea9be48", "Alma C MacHado", "471"),
    12: ("e894b200-4209-5a59-9cb8-05a201d6eb20", "Emily R MacHado", "471"),
    13: ("6404d6ab-30eb-5e29-9ba2-35e995361703", "Lawrence A MacHado", "471"),
    14: ("5d61ce53-4a83-5665-a909-25d9eafead3e", "Leonards MacHado", "471"),
    15: ("377634ed-c642-58d9-9340-4e93520668e0", "Marton O Machen", "471"),
    16: ("cb158750-4fbb-594c-9614-b9a0702bb7a2", "Raymond E Macht", "471"),
    17: ("878f4309-9124-59ec-8a4d-18d536ec9035", "Albert J Machuta", "471"),
    18: ("bdd46c22-4b10-5dd4-b41b-e182e6b5d378", "Henry V Macias", "471"),
    19: ("15e52ea0-2405-53fd-9447-4e4c4b2ccf12", "Donald E Macinnis", "471"),
    20: ("c6eab494-63be-5081-9ff0-9af27cd1f91a", "Henry D Macintosh", "471"),
    21: ("6f240424-45d9-5d08-b6a0-5cee1ffc7553", "Stanley J Macioch", "471"),
    22: ("d5d3a163-d899-5c02-912c-5a8fceecd039", "Gerstle Mack", "471"),
    23: ("0301b2fe-0895-5de3-ae5d-ebf2ad85d22a", "Lewis G Mack", "471"),
    24: ("a900d7e3-c408-55c0-9f01-cc84500e4a19", "Paul J Mack", "471"),
    25: ("e241c3d2-b1a1-5856-94f7-18f4dfff4c33", "Solveig M Mack", "471"),
    26: ("bcf823b9-b012-5cb0-abb7-6207e73ce404", "Grace M Mackay", "471"),
    27: ("b2da3b89-0942-5b61-a402-b17d1759dc16", "Robert Mackay", "471"),
    28: ("68a1d214-2fa2-5e47-b50a-ba863f43d004", "Lawrence E Mackechnie", "472"),
    29: ("18b7c7af-33ae-5ef2-a1d9-60aa8682e7cf", "Franklin H MacKenzie", "472"),
    30: ("d0b70a18-1b58-54d5-8978-bbb152a1c616", "Lucy M MacKenzie", "472"),
    31: ("90b1746e-8188-5d8b-8e60-62a6f1f2e066", "Malcolm S MacKenzie", "472"),
    32: ("7f796d25-c694-5f0c-be35-f649c24e5c82", "Malcolm S MacKenzie", "472"),
    33: ("fe21c6f9-1243-5e7f-902f-b321098ac839", "William A MacKenzie", "472"),
    34: ("d2c1eccf-e4c0-5516-b4cb-148dda97b3c2", "William S MacKenzie", "472"),
    35: ("384aa901-4395-5391-b05f-afbfd9cab5f2", "Paul J Mackey", "472"),
    36: ("97e02f59-d318-5c77-b594-07c7acc1e384", "Virginia Mackey", "472"),
    37: ("b1614fc7-42ac-500c-a1f4-eb3f4679310c", "Bernard J Mackin", "472"),
    38: ("b12abcb6-290d-51d4-a4dd-1c93cde3ebff", "Charles D MacKinnon", "472"),
    39: ("b12f7b98-15a6-5fed-bb0a-1c7ae661c1ad", "Donald W MacKinnon", "472"),
    40: ("8209a50a-c108-5695-93da-9f7ed7d527b6", "William MacKintosh", "472"),
    41: ("55c443a2-7e9e-57a9-b6e4-5214ed8b925a", "James W Mackle", "472"),
    42: ("841c6498-d2d0-5f4b-9647-858bae95a778", "Anita S MacLean", "472"),
    43: ("15f0ef26-c8c5-57ce-9ea5-279ecb8992ec", "Henry F MacLean", "472"),
    44: ("8e310ac5-7dd9-56f4-8998-6c448820699e", "John A MacLean", "472"),
    45: ("8ddc5afa-d226-5413-9e6a-3c4a52362da2", "Madeleine E MacLean", "472"),
    46: ("28fdd42a-eea4-5ee8-8438-158bbcbb73de", "Roderick S MacLennan", "472"),
}


ARMY_ASSOCIATIONS = {
    3: ("1942-07-30", "902", "unskilled aircraft-building occupation, n.e.c.", "Occupations in building of aircraft, n.e.c.", "unknown", "PDF physical page 174; historical category 9-02"),
    4: ("1942-04-25", "480", "sheet-metal worker, coppersmith, or tinsmith", "Tinsmiths, coppersmiths, and sheet metal workers", "unknown", "PDF physical page 174; historical category 4-80"),
    6: ("1942-08-26", "586", "skilled photographic-process occupation", "Photographic process occupations", "unknown", "PDF physical page 175; historical category 5-86"),
    13: ("1942-12-28", "736", "chauffeur or driver of a bus, taxi, truck, or tractor", "Chauffeurs and drivers, bus, taxi, truck, and tractor", "unknown", "PDF physical page 174; historical category 7-36"),
    15: ("1942-12-03", "316", "general farm hand", "Farm hands, general farms", "unknown", "PDF physical page 172; historical category 3-16"),
    21: ("1943-06-30", "992", "student", "Students", "student", "PDF physical page 304; corrected historical category 9-92"),
    24: ("1941-05-28", "103", "checker", "Checkers", "unknown", "PDF physical page 171; historical category 1-03"),
    28: ("1942-03-24", "987", "surveying chainman, rodman, or axman", "Chainmen, rodmen, and axmen, surveying", "unknown", "PDF physical page 175; historical category 9-87"),
    33: ("1943-05-19", "964", "unskilled nonprocess manufacturing occupation, n.e.c.", "Nonprocess occupations in manufacturing, n.e.c.", "unknown", "PDF physical page 174; historical category 9-64"),
    44: ("1942-10-10", "028", "statistician", "Statisticians", "unknown", "PDF physical page 171; historical category 0-28"),
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def source(key: str, **kwargs: object) -> dict[str, object]:
    value: dict[str, object] = {"key": key, "access_date": "2026-11-04"}
    value.update(kwargs)
    return value


def sources() -> list[dict[str, object]]:
    return [
        source(
            INDEX,
            stable_url="https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            archival_identifier="RG 226, Entry A1-224, Boxes 470-472",
            title="OSS Personnel Files from Excel",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="2010-12-23",
            locator="PDF page 288, rows 1-46; all rows visually checked at 180 dpi",
            source_quality="A_direct_official",
            collection_name="Records of the Office of Strategic Services, Record Group 226",
            rights_notes="All 46 printed rows remain separate. Full protected identifiers remain private.",
        ),
        source(
            ARMY,
            stable_url="https://catalog.archives.gov/id/1263923",
            archival_identifier="National Archives Identifier 1263923; parent series NAID 604357",
            title="Electronic Army Serial Number Merged File, ca. 1938-1946",
            author_creator="Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="1938-1946; merged file created 2002",
            locator="Official unrestricted ASNEF.FIN.DAT; eleven accepted and one rejected Batch 1033 identity candidates explicitly reviewed",
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
            locator="PDF physical pages 44-46; identifier, name, Army-entry-date, grade and civilian-occupation fields",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records technical documentation",
            rights_notes="Used to interpret selected fields only; source damage, coding limits, and incomplete coverage remain applicable.",
        ),
        source(
            CODES,
            stable_url="https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1CL_SD.pdf",
            archival_identifier="National Archives Identifier 1263923; Code No. 30",
            title="NARA Compiled Code Lists for the Electronic Army Serial Number Merged File",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives at College Park - Electronic Records",
            publication_record_date="2011-01-12; modified 2011-03-17",
            locator="PDF physical pages 171, 172, 174, 175 and 304; all ten published Batch 1033 categories visually checked",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records technical documentation",
            rights_notes="Historical categories identify neither employer, institution, workplace, nor exact Army-to-OSS sequence.",
        ),
        source(
            FRASER_MACFARLAND,
            stable_url="https://fraser.stlouisfed.org/files/docs/publications/nfr/mcbanker/midcontinentbanker_194205.pdf",
            title="Mid-Continent Banker: May 1942, Volume 38, No. 5",
            repository_publisher="Federal Reserve Bank of St. Louis FRASER",
            publication_record_date="May 1942",
            locator="PDF page 44, 'Will Attend Illinois Convention,' Chicago list",
            source_quality="C_reputable_contemporary_or_scholarly",
            collection_name="Mid-Continent Banker",
            rights_notes="The contemporary trade journal lists Lanning Macfarland as a Northern Trust Company vice president; it does not state his departure date.",
        ),
        source(
            OSS_MACFARLAND,
            stable_url="https://www.elia.org.gr/userfiles/pdf_archieve/1944%2010-2344%20OSS%2C%20Theofanides%2C%20Merchant%20Seamen%2C%20King%2C%20%5B7%20pgs%5D%20226-210-WN10850%20%28Admin%29.pdf",
            archival_identifier="RG 226, 210-WN10850",
            title="South Eastern European Section SA/b-SI: Review of Period December 1941-March 1943",
            author_creator="D. G. Stampados, Captain AC",
            repository_publisher="Greek Literary and Historical Archive digital collection; declassified OSS record",
            publication_record_date="1944-10-23",
            locator="PDF page 6, paragraphs 9-13",
            source_quality="A_direct_official",
            collection_name="Records of the Office of Strategic Services",
            document_number="226-210-WN10850",
            rights_notes="The official memorandum says MacFarland did not join the organization until December 1942 and describes his Yugoslav and Istanbul work.",
        ),
        source(
            CIA_MACFARLAND,
            stable_url="https://www.cia.gov/readingroom/docs/CIA-RDP13X00001R000100410005-4.pdf",
            archival_identifier="CIA-RDP13X00001R000100410005-4",
            title="Report on Field Conditions",
            author_creator="Colonel Sidney S. Hubenstein",
            repository_publisher="Central Intelligence Agency Freedom of Information Act Electronic Reading Room",
            publication_record_date="wartime report; declassified release approved 2013-09-25",
            locator="PDF page 1, paragraphs 1-3",
            source_quality="A_direct_official",
            collection_name="OSS Collection",
            document_number="CIA-RDP13X00001R000100410005-4",
            rights_notes="The report places MacFarland en route from America to establish the OSS mission in Turkey in March 1943 and in Istanbul by May.",
        ),
        source(
            NIXON_MACGREGOR,
            stable_url="https://www.nixonlibrary.gov/sites/default/files/virtuallibrary/documents/contested/contested_box_34/Contested-34-09.pdf",
            archival_identifier="Richard Nixon Presidential Library, Contested Materials Collection, Box 34, Folder 9",
            title="Biography: Clark MacGregor",
            repository_publisher="Richard Nixon Presidential Library and Museum",
            locator="PDF page 18; education and military sections",
            source_quality="A_direct_official",
            collection_name="Contested Materials Collection",
            rights_notes="The biography dates Army enlistment to 1942-10-01, overseas OSS service to summer 1943, a battlefield commission, and Dartmouth attendance and graduation.",
        ),
        source(
            DARTMOUTH_MACGREGOR,
            stable_url="https://archive.dartmouthalumnimagazine.com/article/1941/10/1/trustee-scholarships",
            title="Trustee Scholarships",
            repository_publisher="Dartmouth Alumni Magazine Archive",
            publication_record_date="October 1941",
            locator="Article text, scholarship recipients",
            source_quality="B_authoritative_institutional",
            collection_name="Dartmouth Alumni Magazine",
            rights_notes="The contemporary institutional publication lists Clark MacGregor '44 of Minneapolis as a scholarship recipient.",
        ),
        source(
            GOOGLE_MACK,
            stable_url="https://books.google.com/books/about/The_Land_Divided_A_History_of_the_Panama.html?id=OiX_EAAAQBAJ",
            title="The Land Divided: A History of the Panama Canal and Other Isthmian Canal Projects",
            author_creator="Gerstle Mack",
            repository_publisher="Plunkett Lake Press via Google Books",
            publication_record_date="2024 reissue; original work published 1944",
            locator="Publisher-supplied author biography",
            source_quality="C_reputable_contemporary_or_scholarly",
            rights_notes="The publisher biography links the distinctive author to OSS service in England and describes his prewar architectural and biographical writing.",
        ),
        source(
            NLI_MACK,
            stable_url="https://catalogue.nli.ie/Record/vtls000472935",
            archival_identifier="National Library of Ireland record vtls000472935",
            title="Toulouse-Lautrec",
            author_creator="Gerstle Mack",
            repository_publisher="National Library of Ireland",
            publication_record_date="1938",
            locator="Catalog record; London: J. Cape, 1938",
            source_quality="B_authoritative_institutional",
            collection_name="National Library of Ireland Catalogue",
            rights_notes="The institutional catalog confirms a substantial prewar biography by Gerstle Mack; it does not name an employer.",
        ),
        source(
            BERKELEY_MACKINNON,
            stable_url="https://digicoll.lib.berkeley.edu/record/81423/files/inmemoriam1987.pdf",
            title="Donald Wallace MacKinnon, Psychology: Berkeley, 1903-1987",
            author_creator="University of California Academic Senate memorial authors",
            repository_publisher="University of California, Berkeley Library Digital Collections",
            publication_record_date="1987",
            locator="In Memoriam 1987, PDF pages 67-68",
            source_quality="B_authoritative_institutional",
            collection_name="University of California In Memoriam",
            rights_notes="The memorial explicitly dates his Bryn Mawr professorship to 1933-47 and leave to direct OSS Station S in 1944-46.",
        ),
        source(
            BERKELEY_PSYCH,
            stable_url="https://digicoll.lib.berkeley.edu/record/230584/files/history_of_ca_psych_department.pdf",
            title="History of the University of California Psychology Department at Berkeley",
            repository_publisher="University of California, Berkeley Library Digital Collections",
            locator="PDF page 14, World War II section",
            source_quality="B_authoritative_institutional",
            collection_name="University of California Psychology Department history",
            rights_notes="The departmental history says Henry Murray brought Donald MacKinnon from Bryn Mawr in 1944 to direct OSS Station S for two years.",
        ),
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": ORG_NORTHERN_TRUST,
            "canonical_name": "Northern Trust Company",
            "historical_name": "Northern Trust Company",
            "aliases": ["Northern Trust"],
            "organization_type": "bank and trust company",
            "sector": "finance_and_banking",
            "city": "Chicago",
            "state_or_region": "Illinois",
            "country": "United States",
            "normalization_notes": "The 1942 historical employer name is retained; no modern successor name is substituted.",
        },
        {
            "key": ORG_DARTMOUTH,
            "organization_id": "876621b2-b018-55a7-800e-242fe98b2deb",
            "canonical_name": "Dartmouth College",
            "historical_name": "Dartmouth College",
            "organization_type": "college",
            "sector": "academia_and_research",
            "city": "Hanover",
            "state_or_region": "New Hampshire",
            "country": "United States",
            "normalization_notes": "Student status remains separate from employment.",
        },
        {
            "key": ORG_ARMY,
            "organization_id": "28a26f92-78af-5a1a-9c09-a843eb5975b4",
            "canonical_name": "United States Army",
            "historical_name": "United States Army",
            "aliases": ["U.S. Army", "Army"],
            "organization_type": "military service",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "Military service is modeled as an assignment, not a civilian employer.",
        },
        {
            "key": ORG_BRYN_MAWR,
            "organization_id": "242079a5-4289-5105-83e6-51898d6cb032",
            "canonical_name": "Bryn Mawr College",
            "historical_name": "Bryn Mawr College",
            "organization_type": "college",
            "sector": "academia_and_research",
            "city": "Bryn Mawr",
            "state_or_region": "Pennsylvania",
            "country": "United States",
            "normalization_notes": "The historical college name is retained; documented professorial employment is distinct from education.",
        },
    ]


def affiliation(
    key: str,
    row: int,
    relationship: str,
    temporal: str,
    identity: str,
    confidence: str,
    quality: str,
    status: str = "published",
    **kwargs: object,
) -> dict[str, object]:
    value: dict[str, object] = {
        "key": key,
        "person_id": PEOPLE[row][0],
        "relationship_type": relationship,
        "pre_oss_temporal_basis": temporal,
        "identity_confidence": identity,
        "claim_confidence": confidence,
        "source_quality": quality,
        "publication_status": status,
    }
    value.update(kwargs)
    return value


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    high_identity_rows = {3, 6, 28, 33, 44}
    for row, (date, code, occupation, _label, relationship, _locator) in ARMY_ASSOCIATIONS.items():
        identity = "high_confidence" if row in high_identity_rows else "confirmed"
        kwargs: dict[str, object] = {
            "end_date": date,
            "date_precision": f"Historical civilian-occupation code {code} was recorded at Army entry on {date}; no named employer or workplace is supplied.",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "research_notes": "The broad historical category is not converted into a named employer and is excluded from verified-employer analytics.",
        }
        if relationship == "student":
            kwargs["role_title"] = "student"
        else:
            kwargs["occupation"] = occupation
        values.append(
            affiliation(
                f"{slug(PEOPLE[row][1])}-army-association-b1033",
                row,
                relationship,
                "strongly_date_bounded",
                identity,
                "medium",
                "A_direct_official",
                "publish_qualified",
                **kwargs,
            )
        )
    values.extend(
        [
            affiliation(
                "lanning-macfarland-northern-trust-b1033",
                5,
                "employment",
                "strongly_date_bounded",
                "high_confidence",
                "high",
                "C_reputable_contemporary_or_scholarly",
                organization_key=ORG_NORTHERN_TRUST,
                organization_name_as_found="Northern Trust Company",
                role_title="vice president",
                end_date="1942-12",
                date_precision="A contemporary May 1942 banking journal lists Macfarland as vice president; an OSS memorandum says he joined in December 1942. No exact departure date or direct recruitment-from statement is available.",
                city="Chicago",
                state_or_region="Illinois",
                country="United States",
                immediate_pre_oss=False,
                last_civilian_pre_service=True,
                research_notes="Best-supported last civilian employer before OSS. The seven-month bound is strong, but immediacy is not asserted without a direct transition statement.",
            ),
            affiliation(
                "clark-macgregor-dartmouth-b1033",
                7,
                "student",
                "strongly_date_bounded",
                "confirmed",
                "high",
                "A_direct_official",
                organization_key=ORG_DARTMOUTH,
                organization_name_as_found="Dartmouth College",
                role_title="undergraduate student",
                start_date="1940",
                end_date="1942-10-01",
                date_precision="The Nixon Library biography places Dartmouth attendance after June 1940 high-school graduation and before Army enlistment on 1942-10-01; the October 1941 Dartmouth article independently lists him as a student and scholarship recipient.",
                city="Hanover",
                state_or_region="New Hampshire",
                country="United States",
                immediate_pre_oss=False,
                last_civilian_pre_service=False,
                research_notes="Student status, not employment; Army service intervened before OSS assignment.",
            ),
            affiliation(
                "clark-macgregor-us-army-b1033",
                7,
                "military_assignment",
                "explicit_immediate",
                "confirmed",
                "high",
                "A_direct_official",
                organization_key=ORG_ARMY,
                organization_name_as_found="U.S. Army",
                role_title="Private before overseas OSS assignment",
                start_date="1942-10-01",
                end_date="1943",
                date_precision="The Nixon Library biography gives the exact Army enlistment date and says he was sent overseas with OSS in summer 1943; it later records a battlefield commission and 1945 discharge as a second lieutenant.",
                country="United States",
                immediate_pre_oss=True,
                last_civilian_pre_service=False,
                research_notes="The immediate predecessor is a military assignment, not a civilian employer. The index separately preserves his T SGT rank.",
            ),
            affiliation(
                "gerstle-mack-writer-b1033",
                22,
                "unknown",
                "documented_prewar",
                "high_confidence",
                "high",
                "B_authoritative_institutional",
                role_title="writer and biographer",
                occupation="writer and biographer",
                start_date="1935",
                end_date="1938",
                date_precision="The publisher biography dates major biographies to 1935 and 1938; the National Library of Ireland independently catalogs the 1938 Toulouse-Lautrec biography. Neither source names an employer or proves this was his immediate pre-OSS role.",
                city="New York",
                state_or_region="New York",
                country="United States",
                immediate_pre_oss=False,
                last_civilian_pre_service=False,
                research_notes="Published as a documented prewar occupation only. Self-employment and a named publisher-employer are not inferred.",
            ),
            affiliation(
                "donald-mackinnon-bryn-mawr-b1033",
                39,
                "employment",
                "explicit_immediate",
                "high_confidence",
                "high",
                "B_authoritative_institutional",
                organization_key=ORG_BRYN_MAWR,
                organization_name_as_found="Bryn Mawr College",
                role_title="professor of psychology",
                start_date="1933",
                end_date="1947",
                date_precision="The Berkeley memorial dates the professorship to 1933-47 and explicitly identifies leave in 1944-46 to direct OSS Station S.",
                city="Bryn Mawr",
                state_or_region="Pennsylvania",
                country="United States",
                immediate_pre_oss=True,
                last_civilian_pre_service=True,
                research_notes="The employer continued while MacKinnon was on leave; it is both the explicit immediate civilian affiliation and last civilian employer before OSS service.",
            ),
        ]
    )
    return values


def claim(
    key: str,
    row: int,
    claim_type: str,
    text: str,
    paraphrase: str,
    identity: str,
    temporal: str,
    quality: str,
    confidence: str,
    source_links: list[dict[str, str]],
    notes: str,
    status: str = "published",
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
        "publication_status": status,
        "match_notes": notes,
        "sources": source_links,
    }
    if affiliation_key:
        value["affiliation_key"] = affiliation_key
    return value


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    high_identity_rows = {3, 6, 28, 33, 44}
    for row, (date, code, occupation, label, relationship, locator) in ARMY_ASSOCIATIONS.items():
        identity = (
            "High confidence from a nonshared protected linkage plus a reviewed spacing or suffix variation; the protected identifier is not published."
            if row in high_identity_rows
            else "Confirmed by exact official name agreement and a nonshared protected linkage; the protected identifier is not published."
        )
        key = f"{slug(PEOPLE[row][1])}-army-association-b1033"
        claim_type = "other_pre_oss_affiliation" if relationship == "student" else "occupation"
        values.append(
            claim(
                f"army-{slug(PEOPLE[row][1])}-b1033",
                row,
                claim_type,
                f"At Army entry on {date}, {PEOPLE[row][1]} was recorded as {occupation}; no employer or workplace is identified.",
                f"The Army bulk file records code {code}, and the visually checked official code list defines the category as {label}.",
                identity,
                "Strongly date-bounded to Army entry, but not proven to be the immediately preceding role or status before OSS.",
                "A_direct_official",
                "medium",
                [
                    {"source_key": INDEX},
                    {"source_key": ARMY},
                    {"source_key": TECH, "support_type": "context_only"},
                    {"source_key": CODES, "locator_override": locator},
                ],
                "The historical category is qualified, excluded from verified-employer analytics, and not converted into a named organization.",
                "publish_qualified",
                key,
            )
        )
    values.extend(
        [
            claim(
                "last-civilian-lanning-macfarland-b1033",
                5,
                "last_civilian_pre_service",
                "Northern Trust Company is the best-supported last civilian employer before Lanning MacFarland joined OSS in December 1942.",
                "A May 1942 banking journal lists him as a Northern Trust vice president; an OSS memorandum says he joined the organization in December 1942.",
                "High confidence from the uncommon exact name, direct OSS chronology, and a second official report placing him in charge of the Turkey mission.",
                "Strongly date-bounded within seven months, but no source explicitly says he left Northern Trust directly for OSS.",
                "C_reputable_contemporary_or_scholarly",
                "high",
                [{"source_key": FRASER_MACFARLAND}, {"source_key": OSS_MACFARLAND}, {"source_key": CIA_MACFARLAND}],
                "Published as last civilian employer; immediate-pre-OSS status remains unasserted.",
                "published",
                "lanning-macfarland-northern-trust-b1033",
            ),
            claim(
                "student-clark-macgregor-b1033",
                7,
                "other_pre_oss_affiliation",
                "Clark MacGregor attended Dartmouth College before enlisting in the U.S. Army on October 1, 1942.",
                "The Nixon Library biography supplies the education-to-enlistment sequence, and a 1941 Dartmouth publication independently identifies him as a student and scholarship recipient.",
                "Confirmed for the ranked index row by the exact Army entry date, protected linkage, name, and official biography; the adjacent unranked row remains separate.",
                "Strongly date-bounded before Army service; Dartmouth is not an employer.",
                "A_direct_official",
                "high",
                [{"source_key": NIXON_MACGREGOR}, {"source_key": DARTMOUTH_MACGREGOR}, {"source_key": ARMY, "support_type": "context_only"}],
                "The student relationship is excluded from employer analytics.",
                "published",
                "clark-macgregor-dartmouth-b1033",
            ),
            claim(
                "immediate-clark-macgregor-army-b1033",
                7,
                "immediate_pre_oss_affiliation",
                "Clark MacGregor's documented immediate pre-OSS affiliation was the U.S. Army.",
                "The Nixon Library biography says he enlisted as a private on October 1, 1942 and was sent overseas with OSS in summer 1943.",
                "Confirmed for the ranked row by the protected Army linkage, exact Army entry date, official biography, and compatible T SGT index rank.",
                "Explicit military-to-OSS sequence; this is not a civilian employer.",
                "A_direct_official",
                "high",
                [{"source_key": NIXON_MACGREGOR}, {"source_key": ARMY, "support_type": "context_only"}, {"source_key": INDEX, "support_type": "context_only"}],
                "The biography's later battlefield commission supports the separate commissioned-officer flag without rewriting the indexed T SGT rank.",
                "published",
                "clark-macgregor-us-army-b1033",
            ),
            claim(
                "occupation-gerstle-mack-b1033",
                22,
                "occupation",
                "Gerstle Mack was a documented prewar writer and biographer, but no named employer or immediate OSS predecessor is established.",
                "A publisher biography links the distinctive author to OSS service and dates biographies to 1935 and 1938; the National Library of Ireland catalogs the 1938 work.",
                "High confidence from the rare exact name, direct OSS link, and independent institutional bibliographic record.",
                "Documented prewar work only; it is not shown to be immediately before OSS and is not recast as self-employment.",
                "B_authoritative_institutional",
                "high",
                [{"source_key": GOOGLE_MACK}, {"source_key": NLI_MACK}],
                "No publisher is labeled an employer and no postwar career is used to fill the gap.",
                "published",
                "gerstle-mack-writer-b1033",
            ),
            claim(
                "immediate-donald-mackinnon-bryn-mawr-b1033",
                39,
                "immediate_pre_oss_affiliation",
                "Donald Wallace MacKinnon's immediate pre-OSS civilian affiliation was his Bryn Mawr College professorship.",
                "Berkeley's memorial says he held the Bryn Mawr professorship from 1933-47 and was on leave in 1944-46 to direct OSS Station S.",
                "High confidence from the full-name institutional memorial, exact middle initial, explicit OSS role, and independent departmental history.",
                "Explicit employer-to-OSS leave sequence.",
                "B_authoritative_institutional",
                "high",
                [{"source_key": BERKELEY_MACKINNON}, {"source_key": BERKELEY_PSYCH}],
                "The continuing leave relationship is preserved rather than inventing a resignation date.",
                "published",
                "donald-mackinnon-bryn-mawr-b1033",
            ),
            claim(
                "last-civilian-donald-mackinnon-bryn-mawr-b1033",
                39,
                "last_civilian_pre_service",
                "Bryn Mawr College is Donald Wallace MacKinnon's documented last civilian employer before directing OSS Station S.",
                "The university memorial explicitly states that he took leave from his Bryn Mawr professorship for the 1944-46 OSS assignment.",
                "High confidence from a specific institutional memorial and corroborating department history.",
                "Explicitly immediate and continuous through leave.",
                "B_authoritative_institutional",
                "high",
                [{"source_key": BERKELEY_MACKINNON}, {"source_key": BERKELEY_PSYCH}],
                "Published as civilian employment, not education or a generic professional affiliation.",
                "published",
                "donald-mackinnon-bryn-mawr-b1033",
            ),
        ]
    )
    return values


def base_update(row: int, **overrides: object) -> dict[str, object]:
    name = PEOPLE[row][1]
    box = PEOPLE[row][2]
    value: dict[str, object] = {
        "person_id": PEOPLE[row][0],
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified page 288 source preserves {name}, Box {box}, rank or grade when printed, and archive location. Staged official, exact-name, employment, occupation, obituary, institutional, newspaper, directory, and archival searches did not establish a defensible identity-and-affiliation bridge.",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": f"Review indexed Box {box} for corroborating identifiers, immediate pre-OSS affiliation, and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }
    value.update(overrides)
    return value


def person_updates() -> list[dict[str, object]]:
    updates = [base_update(row) for row in PEOPLE]
    by_row = {row: updates[row - 1] for row in PEOPLE}

    high_identity_rows = {3, 6, 28, 33, 44}
    variants = {
        3: ["Andrew S Mac Dowell Jr", "Andrew S. MacDowell Jr."],
        6: ["Donald C Mac Farlane"],
        28: ["Lawrence E Mac Kechnie"],
        33: ["William A Mac Kenzie"],
        44: ["John A Mac Lean"],
    }
    for row in ARMY_ASSOCIATIONS:
        status = "high_confidence" if row in high_identity_rows else "confirmed"
        by_row[row].update(
            identity_status=status,
            identity_evidence=(
                "A nonshared protected linkage plus reviewed name spacing or suffix variation connects the official index and Army records; the protected identifier remains private."
                if status == "high_confidence"
                else "Exact official name agreement and a nonshared protected linkage connect the index and Army records; the protected identifier remains private."
            ),
            name_variants=variants.get(row),
            replace_name_variants=False,
            personnel_category=("enlisted_army_personnel" if row != 21 else "enlisted_army_personnel"),
            commissioned_officer=False,
            allied_or_foreign_personnel=False,
            research_status="occupation_only_found",
            nara_catalog_id="1263923",
            archival_review_priority="critical" if row in {3, 28, 44} else "high",
            next_action=f"Review Box {PEOPLE[row][2]} to identify a named employer or institution and establish Army-to-OSS chronology. The protected Army link supplies only a broad historical occupation or status category.",
        )

    by_row[5].update(
        identity_status="high_confidence",
        identity_evidence="The uncommon exact name appears in a contemporary banking journal and two direct OSS records that date recruitment and describe the Turkey mission.",
        name_variants=["Lanning Macfarland", "Lanning 'Packy' Macfarland"],
        replace_name_variants=False,
        research_status="verified_employer_found",
        next_action="Review Box 471 for the exact Northern Trust departure date, employment contract, and any intervening status between the May 1942 journal listing and December 1942 OSS entry.",
        archival_review_priority="medium",
    )
    by_row[7].update(
        identity_status="confirmed",
        identity_evidence="A nonshared protected linkage, the exact Army entry date repeated in an official Nixon Library biography, the compatible indexed T SGT rank, and direct OSS chronology confirm the ranked Clark MacGregor row.",
        name_variants=["Clark Mac Gregor"],
        replace_name_variants=False,
        personnel_category="enlisted_army_personnel",
        commissioned_officer=True,
        allied_or_foreign_personnel=False,
        possible_duplicate_group="page288-clark-macgregor-adjacent-rows-b1033",
        research_status="completed",
        nara_catalog_id="1263923",
        next_action="Review both Box 471 rows to determine why Clark MacGregor appears twice and to identify any civilian employer before Dartmouth and Army service. Do not transfer evidence to the adjacent unranked row without a file bridge.",
        archival_review_priority="critical",
    )
    by_row[8].update(
        identity_status="ambiguous",
        identity_evidence="The index prints an adjacent unranked Clark MacGregor row, but only the ranked row has the protected Army linkage and exact-date official biography. Normalized-name identity alone is insufficient to merge them.",
        possible_duplicate_group="page288-clark-macgregor-adjacent-rows-b1033",
        research_status="needs_identity_review",
        next_action="Compare both Box 471 personnel files before any merge. No Dartmouth, Army, occupation, or OSS pathway evidence is transferred from the ranked row to this adjacent unranked entity.",
        archival_review_priority="critical",
    )
    by_row[14].update(
        identity_status="ambiguous",
        identity_evidence="The source prints Leonards MacHado, 1st Lt., with note 'Also 017.' Exact and Leonard S Machado variants did not establish a defensible identity bridge, and the unusual indexed spelling remains uncorrected.",
        research_status="needs_identity_review",
        next_action="Review Box 471 and the 'Also 017' cross-reference to establish the full name, rank sequence, identity, and pre-OSS affiliation.",
        archival_review_priority="critical",
    )
    by_row[22].update(
        identity_status="high_confidence",
        identity_evidence="A publisher biography links the distinctive exact-name author to OSS service in England; an independent National Library of Ireland catalog confirms his 1938 biography.",
        name_variants=["Lewis Gerstle Mack"],
        replace_name_variants=False,
        research_status="occupation_only_found",
        next_action="Review Box 471 to determine whether writing was Gerstle Mack's immediate pre-OSS status, whether he was self-employed, and whether a named employer or military assignment intervened.",
        archival_review_priority="high",
    )
    by_row[27].update(
        identity_status="ambiguous",
        identity_evidence="Page 288 prints Major Robert Mackay in Box 471; page 304 prints Robert McCay in Box 499 with the same private identifier. The surname variation is strong duplicate evidence, but the different boxes require direct confirmation.",
        possible_duplicate_group="p288-304-robert-mackay-mccay-b621",
        personnel_category="commissioned_army_officer",
        commissioned_officer=True,
        research_status="needs_identity_review",
        next_action="Compare the Box 471 and Box 499 files to confirm whether Robert Mackay and Robert McCay are rank-sequence or spelling duplicates before merging.",
        archival_review_priority="high",
    )
    for row in (31, 32):
        by_row[row].update(
            identity_status="ambiguous",
            identity_evidence="Page 288 prints two separate Malcolm S MacKenzie rows in Box 472 with different grades. No independent identifier or personnel-file evidence establishes whether they are one person or namesakes.",
            possible_duplicate_group="page288-malcolm-s-mackenzie-adjacent-rows-b1033",
            research_status="needs_identity_review",
            next_action="Compare both Box 472 personnel files before any merge and establish each row's pre-OSS affiliation. No grade, identity, or employment evidence is transferred between them.",
            archival_review_priority="critical",
        )
    by_row[39].update(
        identity_status="high_confidence",
        identity_evidence="University of California institutional histories supply Donald Wallace MacKinnon's full name, Bryn Mawr chronology, and direct OSS Station S role, matching the indexed name and middle initial.",
        name_variants=["Donald Wallace MacKinnon"],
        replace_name_variants=False,
        research_status="verified_employer_found",
        next_action="Review Box 472 to confirm OSS appointment details and whether any short assignment intervened; accessible institutional evidence explicitly establishes Bryn Mawr leave for OSS Station S.",
        archival_review_priority="medium",
    )

    if len(updates) != 46:
        raise RuntimeError(f"Expected 46 person updates, generated {len(updates)}")
    return updates


def unresolved_reason(row: int) -> str:
    special = {
        8: "The adjacent unranked Clark MacGregor row was not merged with the ranked, protected-identifier row.",
        14: "The unusual Leonards spelling and 'Also 017' note require the indexed file before any correction or identity assignment.",
        27: "The Mackay/McCay same-identifier duplicate remains unresolved across two boxes.",
        31: "The first Malcolm S MacKenzie row remains separate from the adjacent same-name row with a different grade.",
        32: "The second Malcolm S MacKenzie row remains separate from the adjacent same-name row with a different grade.",
        43: "Exact-name and lieutenant-focused searches found no reliable identity or pre-OSS affiliation for Henry F MacLean.",
        45: "Exact-name and employment-focused searches found no reliable identity or pre-OSS affiliation for Madeleine E MacLean.",
        46: "Exact-name and meaningful-variant searches found no reliable identity or pre-OSS affiliation for Roderick S MacLennan.",
    }
    return special.get(
        row,
        "Unbridged namesakes, snippets, commercial people-finder pages, unsourced genealogy, relatives, and postwar-only leads did not establish this indexed person's identity or pre-OSS affiliation.",
    )


def research_attempts() -> list[dict[str, object]]:
    updates = {item["person_id"]: item for item in person_updates()}
    substantiated = set(ARMY_ASSOCIATIONS) | {5, 7, 22, 27, 39}
    values: list[dict[str, object]] = []
    for row, (person_id, name, box) in PEOPLE.items():
        next_action = str(updates[person_id]["next_action"])
        values.append(
            {
                "key": f"page288-row{row}-{slug(name)}-b1033",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index context; exact-name and meaningful initial, suffix, spacing, punctuation and OCR variants; OSS and CIA Reading Room; rank, branch, assignment and protected-identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory and archival searches; indexed Box {box}",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_1033",
                "started_at": "2026-11-04T15:58:00-05:00",
                "completed_at": "2026-11-04T18:20:00-05:00",
                "outcome": "source_reviewed" if row in substantiated else "candidate_rejected",
                "sources_reviewed": 8 if row in {5, 7, 39} else (6 if row == 22 else (5 if row in substantiated else 5)),
                "candidate_sources_rejected": 3 if row in substantiated else 4,
                "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, and postwar-only leads were rejected. Army categories were not converted into named employers; adjacent identical names were not merged; and discovery-only material was not published as evidence.",
                "research_notes": f"{unresolved_reason(row)} The official index, exact-name OSS searches, targeted CIA context, employment and occupation searches, and institutional, newspaper, obituary, directory, and archival searches were reviewed as applicable. Page 288 and all cited code-list pages were visually checked. The CIA and Library of Congress adapter errors remain recorded separately and are not treated as negative source results. No authenticated NARA Catalog API request was made.",
                "next_action": next_action,
                "attempt_number": 4,
                "research_agent_version": "before-oss-b1033-v1",
            }
        )
    if len(values) != 46:
        raise RuntimeError(f"Expected 46 research attempts, generated {len(values)}")
    return values


def main() -> None:
    bundle = {
        "bundle_version": "batch-1033-v1",
        "reviewer": "Before OSS Batch 1033 evidence review",
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
