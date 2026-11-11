#!/usr/bin/env python3
"""Generate the reviewed Batch 1050 evidence bundle for PDF page 305."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page305-margaret-j-mcclellan-to-charles-h-mccormick-review_"
    "batch-1050_2026-11-11.json"
)

INDEX = "nara-index-b1050"
ARMY = "army-bulk-b1050"
TECH = "army-tech-b1050"
CODES = "army-codes-b1050"
CARNEGIE = "carnegie-impulse-mcclintic-b1050"
BROADCASTING = "broadcasting-mccollom-b1050"
NGA = "nga-mcconaughy-b1050"
CT_HISTORY = "ct-history-mcconaughy-b1050"

ORG_MELLON = "mellon-national-bank-b1050"
ORG_VIII_BOMBER = "viii-bomber-command-b1050"
ORG_BENTON = "benton-bowles-b1050"
ORG_UCR = "united-china-relief-b1050"
ORG_WESLEYAN = "wesleyan-b1050"
ORG_BOWDOIN = "bowdoin-b1050"
ORG_DARTMOUTH = "dartmouth-b1050"
ORG_KNOX = "knox-college-b1050"


PEOPLE = {
    1: ("a4ce86ec-c3fb-56ca-aaa6-09c97d9c92ea", "Margaret J McClellan", "499"),
    2: ("2a12df1c-a025-57e5-8f6b-7e8f6f0505a7", "Norman J McClellan", "499"),
    3: ("da7746cb-eb49-5171-bdf0-e19ebef75538", "Caspar S McClelland", "499"),
    4: ("4ea55cbd-0640-5854-9ec4-7eed327cea5d", "John P McClelland", "499"),
    5: ("88d504f9-11aa-56af-b035-26a367cad9f7", "Robert McClenahan", "499"),
    6: ("db25499c-d71d-5cbb-afe4-46a96fbc3727", "Mary McClenon", "499"),
    7: ("5396ca3e-dd9d-5b69-9ed9-5e312e36f4cb", "Ruth K McClenon", "499"),
    8: ("073741a6-1c20-5321-af39-d72645caa59a", "Ruth K McClenon", "499"),
    9: ("a6911402-9f5f-5a47-ae11-6a42509d5368", "Stewart McClintic", "499"),
    10: ("15d5ee70-c60d-5dc3-a5f1-0471d0b78929", "Floyd F McClintock", "499"),
    11: ("376a2dba-15b5-5be8-8f4c-5d2de233d6c2", "Jack M McClintock", "499"),
    12: ("941086c8-45d8-5ee6-b050-7cd48fbb4846", "Purlmon B McClinton", "499"),
    13: ("4339fbf0-fe6e-508d-8b59-c2af7230ba2f", "Lester D McClung", "499"),
    14: ("1a5cddd1-adc9-59c0-bc1d-62ffecc1b87b", "Louise K McClung", "499"),
    15: ("44dcc3ee-3f5a-514e-8670-52aea3158d12", "Albert McClure", "499"),
    16: ("7d2e664b-6cf3-5488-9009-cacef28f868d", "Douglas T McClure", "499"),
    17: ("e046ed74-9bc8-5d56-8f0b-3bd84ec0ded6", "Ernest L McClure", "499"),
    18: ("98f1b9e9-918e-5a77-8408-6d6be06e3138", "Russell S McClure", "499"),
    19: ("70ff13d0-273c-5aaa-8d83-0d327aab6067", "John J McCole", "499"),
    20: ("51b951af-5498-5e4a-8fad-f116c358817a", "Harold C McCollom", "499"),
    21: ("3b715d57-6fcc-58f1-8da6-b8438bf52f62", "Elmer L McCollum", "499"),
    22: ("2e2830de-b4c5-5f7a-abb6-f8f8d4d0bb72", "James I McCollum", "499"),
    23: ("24491f3b-b7bd-5973-94fd-2a0a38b14cf1", "Oscar D McCollum", "499"),
    24: ("3bf3ecc1-9b6d-5c69-96ed-7ac97d10c1f3", "James L Dr. McConaughy", "499"),
    25: ("09a01b55-1b0b-589d-9fb9-89c75af69569", "Pierce R McConaughy", "499"),
    26: ("bc697771-2b32-5d6b-86ab-7688e9d55c4b", "George R McCone", "500"),
    27: ("d838129e-b5ed-52cd-9449-4d79a33227cb", "Kathryn B McConley", "500"),
    28: ("125bfabb-acda-5899-90be-19611f290c1e", "Robert J McConnachie", "500"),
    29: ("bfbff01f-9da6-51ce-84bf-b9a70d5a1e24", "John N McConnaughe", "500"),
    30: ("cba23874-cf2a-5ca3-b045-56053f6a33f2", "Walter H McConnel", "500"),
    31: ("771cc7ec-6630-54cf-9306-77c4c38e98f6", "Grace F McConnell", "500"),
    32: ("518c60fb-39d1-52ef-9d84-b47ccd633b53", "Jack W McConnell", "500"),
    33: ("6845608b-2e9f-5f12-95d0-81a068c3f28a", "John W McConnell", "500"),
    34: ("123d4acb-8070-5861-9bf0-e63f414e0544", "Joseph B McConnell", "500"),
    35: ("1d3809ab-aebc-5f8a-a598-69ad7ae4d366", "Ruby B McConnell", "500"),
    36: ("86150935-5fdc-53bb-8a8e-aa36e5a696e7", "Helen M McConville", "500"),
    37: ("ce939630-afb6-5c83-8e4b-1723522f5684", "Cornelia B McCook", "500"),
    38: ("6530a476-0f7c-58aa-bb49-3fb56edc8118", "Alice M McCool", "500"),
    39: ("ef714a0d-639b-584c-b23e-b994ad27312e", "Alice M McCool", "500"),
    40: ("11561770-114f-5e51-9220-efe6e7eff8dc", "Alice M McCool", "500"),
    41: ("0117726c-b9b2-5f11-b02a-38d27fa72f5e", "Joseph McCord", "500"),
    42: ("2dea82f8-ef50-5603-821f-1f03c5f3ea0b", "Wallack H McCord", "500"),
    43: ("fee8799f-5d0c-5f90-8067-17e6f4a2b1a1", "Robert L McCorkle", "500"),
    44: ("c0ee9f3a-1962-5c66-8e8b-a4391431f5d0", "Kenneth D McCormack", "500"),
    45: ("b5e20e5d-89ca-55d0-8e18-04dbb0146402", "William M McCormack", "500"),
    46: ("0d41e55c-f979-5993-b500-86ac19a851b8", "Charles H McCormick", "500"),
}


# Oscar D. McCollum's accepted Army identity row is dated 1946-04-27, so its
# draftsman code is not published as pre-OSS evidence without a service sequence.
ARMY_ASSOCIATIONS = {
    10: ("1943-12-08", "134", "shipping and receiving clerk", "Shipping and receiving clerks", "PDF physical page 171; historical code 1-34"),
    11: ("1942-02-20", "688", "mechanical treatment of metals occupation, not elsewhere classified", "Occupations in mechanical treatment of metals (rolling, stamping, forging, pressing, etc.), n.e.c.", "PDF physical page 174; historical category 4, 6-88"),
    16: ("1942-11-11", "992", "student", "Students", "PDF physical page 304; corrected historical code 9-92"),
    19: ("1942-09-15", "992", "student", "Students", "PDF physical page 304; corrected historical code 9-92"),
    20: ("1944-04-03", "006", "author, editor, or reporter", "Authors, editors, and reporters", "PDF physical page 170; historical code 0-06"),
    22: ("1942-08-13", "948", "sailor or deckhand, except U.S. Navy", "Sailors and deckhands, except U.S. Navy", "PDF physical page 174; historical code 9-48"),
    28: ("1942-09-11", "992", "student", "Students", "PDF physical page 304; corrected historical code 9-92"),
    29: ("1943-05-17", "992", "student", "Students", "PDF physical page 304; corrected historical code 9-92"),
    42: ("1942-05-22", "006", "author, editor, or reporter", "Authors, editors, and reporters", "PDF physical page 170; historical code 0-06"),
    45: ("1942-04-16", "316", "general farm hand", "Farm hands, general farms", "PDF physical page 172; historical code 3-16"),
}

IDENTITY_REVIEW_ROWS = {7, 8, 21, 38, 39, 40}
DUPLICATE_GROUPS = {
    7: "p305-ruth-k-mcclenon-repeat-b623",
    8: "p305-ruth-k-mcclenon-repeat-b623",
    21: "p304-305-elmer-mcccollum-mccollum-b623",
    38: "p305-alice-m-mccool-three-rows-b623",
    39: "p305-alice-m-mccool-three-rows-b623",
    40: "p305-alice-m-mccool-three-rows-b623",
}

ATTEMPT_NUMBER_3 = {21, 28, 29, 42, 45}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def source(key: str, **kwargs: object) -> dict[str, object]:
    value: dict[str, object] = {"key": key, "access_date": "2026-11-11"}
    value.update(kwargs)
    return value


def sources() -> list[dict[str, object]]:
    return [
        source(
            INDEX,
            stable_url="https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            archival_identifier="RG 226, Entry A1-224, Boxes 499-500",
            title="OSS Personnel Files from Excel",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="2010-12-23",
            locator="PDF page 305, rows 1-46; every printed row visually checked",
            source_quality="A_direct_official",
            collection_name="Records of the Office of Strategic Services, Record Group 226",
            rights_notes="All 46 printed rows remain recoverable as separate source records and cautious person entities. Full protected identifiers remain private.",
        ),
        source(
            ARMY,
            stable_url="https://catalog.archives.gov/id/1263923",
            archival_identifier="National Archives Identifier 1263923; parent series NAID 604357",
            title="Electronic Army Serial Number Merged File, ca. 1938-1946",
            author_creator="Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="1938-1946; merged file created 2002",
            locator="Official unrestricted ASNEF.FIN.DAT; previously reviewed row-specific protected identity crosswalks",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records",
            document_number="ASNEF.FIN.DAT",
            rights_notes="No raw record, protected identifier, or bulk response is retained in public assets. Shared or conflicting candidates were not used for occupations.",
        ),
        source(
            TECH,
            stable_url="https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf",
            archival_identifier="NN3-064-03-008; National Archives Identifier 1263923",
            title="World War II Army Enlistment Records: Reference Copy of Technical Documentation",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives at College Park - Electronic Records",
            publication_record_date="1994-2005; reference copy modified 2011",
            locator="PDF physical pages 44-46; Army-entry date, grade, and civilian-occupation fields",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records technical documentation",
            rights_notes="Used only to interpret selected fields; the bulk file does not name an employer or establish the Army-to-OSS sequence.",
        ),
        source(
            CODES,
            stable_url="https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf",
            archival_identifier="Code No. 30 in NAID 1263923 technical documentation",
            title="World War II Army Enlistment Records: Civilian Occupation Code Lists",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives at College Park - Electronic Records",
            locator="PDF physical pages 170-174 and amended page 304; printed reference-copy pages visually checked",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records code lists",
            rights_notes="Historical categories identify neither employer, institution, workplace, nor exact Army-to-OSS chronology.",
        ),
        source(
            CARNEGIE,
            stable_url="https://www.carnegiehero.org/wp-content/uploads/2020/08/issue33.pdf",
            archival_identifier="imPULSE, Issue 33",
            title="Decorated wartime intelligence analyst used skills to benefit Hero Fund's work",
            author_creator="Mary Brignano",
            repository_publisher="Carnegie Hero Fund Commission",
            publication_record_date="2013-03",
            locator="imPULSE Issue 33, printed pages 4-5",
            source_quality="B_authoritative_institutional",
            collection_name="imPULSE newsletter",
            rights_notes="Only concise project-authored notes and excerpts are retained publicly; the article connects the exact name to OSS service and the bank career.",
        ),
        source(
            BROADCASTING,
            stable_url="https://www.worldradiohistory.com/Archive-BC/BC-1946/1946-04-29-BC.pdf",
            archival_identifier="Broadcasting, volume 30, number 17",
            title="Broadcasting: The Weekly Newsmagazine of Radio",
            repository_publisher="Broadcasting Publications, Inc.",
            publication_record_date="1946-04-29",
            locator="Printed page 62, Agencies column",
            source_quality="C_reputable_contemporary_or_scholarly",
            collection_name="World Radio History: Broadcasting archive",
            rights_notes="Contemporary trade-press notice; only a short supporting excerpt and citation metadata are published.",
        ),
        source(
            NGA,
            stable_url="https://www.nga.org/governor/james-lukens-mcconaughy/",
            archival_identifier="National Governors Association former-governor biography",
            title="Gov. James Lukens McConaughy",
            repository_publisher="National Governors Association",
            locator="About section",
            source_quality="B_authoritative_institutional",
            collection_name="Former Governors",
            rights_notes="Institutional biography used for exact-name identity and pre-OSS academic chronology.",
        ),
        source(
            CT_HISTORY,
            stable_url="https://connecticuthistory.org/did-you-know-a-connecticut-governor-was-a-us-spy/",
            archival_identifier="The Connector, volume 11, number 2",
            title="Did You Know a Connecticut Governor Was a US Spy?",
            author_creator="Paul E. Baran, Government Archivist for the Connecticut State Library",
            repository_publisher="Connecticut History, a Connecticut Humanities project",
            publication_record_date="2021-07-14; originally published 2009-04",
            locator="Biography paragraphs 1-3",
            source_quality="B_authoritative_institutional",
            collection_name="Connecticut History",
            rights_notes="The profile uses neutral OSS-personnel language rather than repeating the page title's 'spy' label.",
        ),
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": ORG_MELLON,
            "organization_id": "54e22e9d-130a-57e7-9d86-3ae19db2b6cf",
            "canonical_name": "Mellon National Bank",
            "historical_name": "Mellon National Bank",
            "aliases": ["Mellon Nat. Bank", "Mellon National Bank and Trust Company"],
            "organization_type": "bank",
            "sector": "finance_and_banking",
            "city": "Pittsburgh",
            "state_or_region": "Pennsylvania",
            "country": "United States",
            "normalization_notes": "The exact Mellon National Bank and Trust Company wording remains on McClintic's affiliation. It is not replaced with a modern successor or merged with less specific Mellon Bank records.",
        },
        {
            "key": ORG_VIII_BOMBER,
            "canonical_name": "VIII Bomber Command",
            "historical_name": "U.S. VIII Bomber Command",
            "aliases": ["Eighth Air Force", "VIII Bomber Command"],
            "organization_type": "military air command",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "The source's historical unit wording is retained. The article notes a later Eighth Air Force redesignation; the two names are not treated as contemporaneous synonyms in the affiliation text.",
        },
        {
            "key": ORG_BENTON,
            "organization_id": "fd1f6ea8-99fa-58a9-b81f-b9f9f2f47a08",
            "canonical_name": "Benton & Bowles",
            "historical_name": "Benton & Bowles",
            "aliases": ["Benton and Bowles"],
            "organization_type": "advertising agency",
            "sector": "advertising_and_public_relations",
            "city": "New York",
            "state_or_region": "New York",
            "country": "United States",
            "active_dates": "1929-1985",
            "normalization_notes": "Historical agency name retained without substituting a successor organization.",
        },
        {
            "key": ORG_UCR,
            "canonical_name": "United China Relief",
            "historical_name": "United China Relief",
            "aliases": ["United China Relief Fund"],
            "organization_type": "wartime relief organization",
            "sector": "labor_nonprofit_and_religion",
            "country": "United States",
            "normalization_notes": "The two institutional sources use United China Relief and United China Relief Fund. The presidency is modeled as a professional affiliation because the sources do not establish paid employment.",
        },
        {
            "key": ORG_WESLEYAN,
            "organization_id": "5c5be7ce-b123-5389-9904-e6eb76c98cfe",
            "canonical_name": "Wesleyan University",
            "historical_name": "Wesleyan University",
            "aliases": [],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "Middletown",
            "state_or_region": "Connecticut",
            "country": "United States",
            "normalization_notes": "Student and employment relationships are modeled separately; McConaughy's presidency is employment, while United China Relief remains a distinct professional affiliation.",
        },
        {
            "key": ORG_BOWDOIN,
            "organization_id": "0881619e-5c59-5f34-bd86-11f409bfa463",
            "canonical_name": "Bowdoin College",
            "historical_name": "Bowdoin College",
            "aliases": ["Bowdoin"],
            "organization_type": "college",
            "sector": "academia_and_research",
            "city": "Brunswick",
            "state_or_region": "Maine",
            "country": "United States",
            "normalization_notes": "Existing canonical organization reused; McConaughy's teaching employment remains separate from education or alumni status.",
        },
        {
            "key": ORG_DARTMOUTH,
            "organization_id": "876621b2-b018-55a7-800e-242fe98b2deb",
            "canonical_name": "Dartmouth College",
            "historical_name": "Dartmouth College",
            "aliases": [],
            "organization_type": "college",
            "sector": "academia_and_research",
            "city": "Hanover",
            "state_or_region": "New Hampshire",
            "country": "United States",
            "normalization_notes": "Employment and student relationships remain separate; McConaughy's professorship is modeled as employment.",
        },
        {
            "key": ORG_KNOX,
            "canonical_name": "Knox College",
            "historical_name": "Knox College",
            "aliases": [],
            "organization_type": "college",
            "sector": "academia_and_research",
            "city": "Galesburg",
            "state_or_region": "Illinois",
            "country": "United States",
            "normalization_notes": "The NGA biography documents McConaughy's presidency but does not disaggregate its dates from the adjoining Wesleyan chronology, so no exact dates are inferred.",
        },
    ]


def army_affiliation_key(row: int) -> str:
    return f"{slug(PEOPLE[row][1])}-army-entry-occupation-b1050"


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, _label, _locator) in ARMY_ASSOCIATIONS.items():
        values.append(
            {
                "key": army_affiliation_key(row),
                "person_id": PEOPLE[row][0],
                "occupation": occupation,
                "relationship_type": "student" if code == "992" else "unknown",
                "end_date": date,
                "date_precision": f"Historical civilian-occupation code {code} was recorded at Army entry on {date}; no named employer, institution, workplace, or OSS-transfer date is supplied.",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "temporal_relation_uncertain",
                "identity_confidence": "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "A_direct_official",
                "publication_status": "publish_qualified",
                "research_notes": "The historical category is excluded from verified-employer analytics and is not converted into a named organization. The official sources do not establish its sequence relative to OSS service.",
            }
        )

    values.extend(
        [
            {
                "key": "stewart-mcclintic-mellon-b1050",
                "person_id": PEOPLE[9][0],
                "organization_key": ORG_MELLON,
                "organization_name_as_found": "Mellon National Bank and Trust Company",
                "role_title": "corporate-loan work",
                "relationship_type": "employment",
                "end_date": "1942",
                "date_precision": "The institutional profile says McClintic's continuous bank career was interrupted only by war service beginning almost immediately after Pearl Harbor; it does not supply the hire date or exact last workday.",
                "city": "Pittsburgh",
                "state_or_region": "Pennsylvania",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "The bank is the last documented civilian employer before Army Air Forces service, not the immediate military predecessor to OSS.",
            },
            {
                "key": "stewart-mcclintic-viii-bomber-command-b1050",
                "person_id": PEOPLE[9][0],
                "organization_key": ORG_VIII_BOMBER,
                "organization_name_as_found": "U.S. VIII Bomber Command",
                "role_title": "Army Air Forces officer",
                "relationship_type": "military_assignment",
                "start_date": "1942",
                "end_date": "1942",
                "date_precision": "The profile places McClintic with VIII Bomber Command by summer 1942 and then in a short OSS assignment; no exact transfer date is supplied.",
                "country": "United Kingdom",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "The military pathway is kept separate from Mellon National Bank employment.",
            },
            {
                "key": "harold-mccollom-benton-bowles-b1050",
                "person_id": PEOPLE[20][0],
                "organization_key": ORG_BENTON,
                "organization_name_as_found": "Benton & Bowles",
                "role_title": "account executive",
                "occupation": "advertising account executive",
                "relationship_type": "employment",
                "date_precision": "The April 1946 trade notice says McCollom had completed two years of military service and had previously been an account executive at Benton & Bowles; the exact departure date is not printed.",
                "city": "New York",
                "state_or_region": "New York",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "published",
                "research_notes": "The employer is supported by contemporary trade press and the identity by the index plus a protected official Army crosswalk. No immediate military-to-OSS assignment is inferred.",
            },
            {
                "key": "james-mcconaughy-united-china-relief-b1050",
                "person_id": PEOPLE[24][0],
                "organization_key": ORG_UCR,
                "organization_name_as_found": "United China Relief",
                "role_title": "president",
                "relationship_type": "professional_affiliation",
                "start_date": "1942",
                "end_date": "1946",
                "date_precision": "Connecticut History dates the presidency to 1942-1946 and says Donovan recruited McConaughy to OSS in late 1943 while he held that position.",
                "country": "United States",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "explicit_immediate",
                "identity_confidence": "confirmed",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "The presidency is not labeled employment because neither source establishes a paid employment relationship.",
            },
            {
                "key": "james-mcconaughy-wesleyan-b1050",
                "person_id": PEOPLE[24][0],
                "organization_key": ORG_WESLEYAN,
                "organization_name_as_found": "Wesleyan University",
                "role_title": "president",
                "occupation": "university president",
                "relationship_type": "employment",
                "start_date": "1925",
                "end_date": "1943",
                "date_precision": "Both institutional biographies date the Wesleyan presidency to 1925-1943; the precise end date relative to his late-1943 OSS recruitment is not supplied.",
                "city": "Middletown",
                "state_or_region": "Connecticut",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "probable_immediate",
                "identity_confidence": "confirmed",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Wesleyan is the last documented civilian employer; United China Relief is separately modeled as the immediate professional affiliation and is not silently converted into employment.",
            },
            {
                "key": "james-mcconaughy-bowdoin-b1050",
                "person_id": PEOPLE[24][0],
                "organization_key": ORG_BOWDOIN,
                "organization_name_as_found": "Bowdoin College",
                "role_title": "teacher of English and education",
                "occupation": "teacher",
                "relationship_type": "employment",
                "start_date": "1909",
                "end_date": "1915",
                "date_precision": "Years stated by the National Governors Association biography.",
                "city": "Brunswick",
                "state_or_region": "Maine",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "confirmed",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Earlier documented employment, not an immediate predecessor to OSS.",
            },
            {
                "key": "james-mcconaughy-dartmouth-b1050",
                "person_id": PEOPLE[24][0],
                "organization_key": ORG_DARTMOUTH,
                "organization_name_as_found": "Dartmouth",
                "role_title": "professor of education",
                "occupation": "professor",
                "relationship_type": "employment",
                "start_date": "1918",
                "end_date": "1925",
                "date_precision": "Years stated by the National Governors Association biography.",
                "city": "Hanover",
                "state_or_region": "New Hampshire",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "confirmed",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Earlier documented employment, not an immediate predecessor to OSS.",
            },
            {
                "key": "james-mcconaughy-knox-b1050",
                "person_id": PEOPLE[24][0],
                "organization_key": ORG_KNOX,
                "organization_name_as_found": "Knox College",
                "role_title": "president",
                "occupation": "college president",
                "relationship_type": "employment",
                "date_precision": "The National Governors Association biography documents the presidency but does not separately date it; no date range is inferred.",
                "city": "Galesburg",
                "state_or_region": "Illinois",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "confirmed",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Earlier documented employment with deliberately unspecified dates.",
            },
        ]
    )
    return values


def claim(
    key: str,
    row: int,
    claim_type: str,
    claim_text: str,
    evidence_paraphrase: str,
    identity_match_assessment: str,
    temporal_assessment: str,
    source_quality: str,
    claim_confidence: str,
    publication_status: str,
    match_notes: str,
    source_links: list[dict[str, str]],
    affiliation_key: str | None = None,
) -> dict[str, object]:
    value: dict[str, object] = {
        "key": key,
        "person_id": PEOPLE[row][0],
        "claim_type": claim_type,
        "claim_text": claim_text,
        "evidence_paraphrase": evidence_paraphrase,
        "identity_match_assessment": identity_match_assessment,
        "temporal_assessment": temporal_assessment,
        "source_quality": source_quality,
        "claim_confidence": claim_confidence,
        "publication_status": publication_status,
        "match_notes": match_notes,
        "sources": source_links,
    }
    if affiliation_key:
        value["affiliation_key"] = affiliation_key
    return value


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, label, locator) in ARMY_ASSOCIATIONS.items():
        values.append(
            claim(
                f"army-entry-{slug(PEOPLE[row][1])}-b1050",
                row,
                "occupation",
                f"At Army entry on {date}, {PEOPLE[row][1]} was recorded as {occupation}; no employer, institution, or workplace is identified.",
                f"The official Army bulk file records code {code}; the visually checked official list defines the category as {label}.",
                "High confidence from matching official name evidence and a previously reviewed, nonshared protected identity linkage; the protected identifier remains private.",
                "The category is fixed to the Army-entry date, but its sequence relative to OSS service is not established.",
                "A_direct_official",
                "medium",
                "publish_qualified",
                "The broad historical category remains qualified, is excluded from verified-employer analytics, and is not converted into a named organization.",
                [
                    {"source_key": INDEX, "support_type": "context_only"},
                    {"source_key": ARMY},
                    {"source_key": TECH, "support_type": "context_only"},
                    {"source_key": CODES, "locator_override": locator},
                ],
                army_affiliation_key(row),
            )
        )

    values.extend(
        [
            claim(
                "identity-stewart-mcclintic-b1050",
                9,
                "identity",
                "Indexed Lieutenant Colonel Stewart McClintic is the Pittsburgh banker and wartime Army Air Forces officer described by the Carnegie Hero Fund Commission.",
                "The uncommon exact name, compatible lieutenant-colonel rank, explicit OSS service, Army Air Forces chronology, and Pittsburgh biography form a specific identity bridge.",
                "High confidence from an uncommon exact name plus compatible rank, branch, wartime location, and explicit OSS context in an institutional profile.",
                "The profile dates civilian banking, Army Air Forces service, VIII Bomber Command, OSS, and later USSTAF service in sequence.",
                "B_authoritative_institutional",
                "high",
                "published",
                "No famous-name inference is required; the source directly names OSS and the compatible wartime rank.",
                [{"source_key": CARNEGIE}, {"source_key": INDEX, "support_type": "context_only"}],
            ),
            claim(
                "mellon-stewart-mcclintic-b1050",
                9,
                "last_civilian_pre_service",
                "Mellon National Bank and Trust Company was Stewart McClintic's last documented civilian employer before his Army Air Forces service.",
                "The institutional profile says McClintic remained with the bank until retirement and that only wartime service interrupted his bank career.",
                "High-confidence identity from the direct OSS and compatible-rank bridge in the same institutional profile.",
                "Strongly date-bounded: bank work continued until war service began almost immediately after Pearl Harbor; Army service began early in 1942.",
                "B_authoritative_institutional",
                "high",
                "published",
                "The bank is not mislabeled as McClintic's immediate military predecessor to OSS.",
                [{"source_key": CARNEGIE, "excerpt_override": "He went to work for Mellon National Bank and Trust Company"}],
                "stewart-mcclintic-mellon-b1050",
            ),
            claim(
                "viii-bomber-command-stewart-mcclintic-b1050",
                9,
                "immediate_pre_oss_affiliation",
                "Stewart McClintic served with U.S. VIII Bomber Command before a short OSS assignment.",
                "The institutional profile places him with VIII Bomber Command by summer 1942 and then states that he had a short OSS assignment before joining USSTAF intelligence.",
                "High-confidence identity from the uncommon exact name and compatible lieutenant-colonel, Army Air Forces, and OSS evidence.",
                "Strongly date-bounded military predecessor; no exact transfer date is supplied.",
                "B_authoritative_institutional",
                "high",
                "published",
                "The VIII Bomber Command assignment is separate from his last civilian bank employer.",
                [{"source_key": CARNEGIE, "excerpt_override": "By the summer of that year, he was in England, assigned to the U.S. VIII Bomber Command."}],
                "stewart-mcclintic-viii-bomber-command-b1050",
            ),
            claim(
                "benton-bowles-harold-mccollom-b1050",
                20,
                "last_civilian_pre_service",
                "Harold C. McCollom Jr. was an account executive at Benton & Bowles before two years of military service.",
                "A contemporary April 1946 advertising-industry notice explicitly sequences Benton & Bowles employment before two years of military service.",
                "High confidence from the rare exact name with suffix, compatible two-year military chronology, official Army identity crosswalk, and related Army-entry occupation category.",
                "Strongly date-bounded to the civilian role immediately before the two-year military-service interval; the exact departure date is not printed.",
                "C_reputable_contemporary_or_scholarly",
                "high",
                "published",
                "The claim does not infer an OSS unit or treat the broad Army-entry occupation code as the employer source.",
                [
                    {"source_key": BROADCASTING, "excerpt_override": "previously account executive at Benton & Bowles, New York"},
                    {"source_key": ARMY, "support_type": "context_only"},
                    {"source_key": INDEX, "support_type": "context_only"},
                ],
                "harold-mccollom-benton-bowles-b1050",
            ),
            claim(
                "identity-james-lukens-mcconaughy-b1050",
                24,
                "identity",
                "Indexed Dr. James L. McConaughy is James Lukens McConaughy, the educator recruited as an OSS civilian deputy in 1943.",
                "Two institutional biographies supply the full middle name, doctorate-level academic career, matching initial, direct OSS service, and compatible civilian status.",
                "Confirmed by the exact indexed name and title pattern plus two institutional sources that explicitly identify his OSS leadership role.",
                "Both biographies place the academic and relief-organization roles before and during his 1943-1945 OSS service.",
                "B_authoritative_institutional",
                "confirmed",
                "published",
                "The full middle name is retained as a sourced variant; the indexed Dr. placement remains recoverable.",
                [{"source_key": NGA}, {"source_key": CT_HISTORY}, {"source_key": INDEX, "support_type": "context_only"}],
            ),
            claim(
                "united-china-relief-james-mcconaughy-b1050",
                24,
                "immediate_pre_oss_affiliation",
                "James Lukens McConaughy was president of United China Relief when William J. Donovan recruited him to OSS in late 1943.",
                "Connecticut History explicitly dates the presidency to 1942-1946 and the OSS recruitment to late 1943; NGA independently confirms both roles.",
                "Confirmed identity from exact name, academic chronology, and explicit OSS leadership evidence in two institutional sources.",
                "Explicit immediate professional affiliation at recruitment; the sources do not establish that the presidency was paid employment.",
                "B_authoritative_institutional",
                "high",
                "published",
                "United China Relief is modeled as a professional affiliation, not silently converted into an employer.",
                [
                    {"source_key": CT_HISTORY, "excerpt_override": "In late 1943 McConaughy was recruited by Major General William J. Donovan of the OSS"},
                    {"source_key": NGA},
                ],
                "james-mcconaughy-united-china-relief-b1050",
            ),
            claim(
                "wesleyan-james-mcconaughy-b1050",
                24,
                "last_civilian_pre_service",
                "Wesleyan University was James Lukens McConaughy's last documented civilian employer before OSS recruitment.",
                "Both institutional biographies date his Wesleyan presidency to 1925-1943, and Connecticut History dates OSS recruitment to late 1943.",
                "Confirmed identity from exact name, title, chronology, and explicit OSS role across two institutional sources.",
                "Probably the last civilian employer before OSS; the source does not print the precise end date, and United China Relief is separately modeled as the immediate professional affiliation.",
                "B_authoritative_institutional",
                "high",
                "published",
                "The employer and immediate affiliation categories remain distinct.",
                [
                    {"source_key": CT_HISTORY, "excerpt_override": "President of Wesleyan University in Middletown (1925-1943)"},
                    {"source_key": NGA},
                ],
                "james-mcconaughy-wesleyan-b1050",
            ),
        ]
    )

    for key, affiliation_key, organization, role, dates in (
        ("bowdoin-james-mcconaughy-b1050", "james-mcconaughy-bowdoin-b1050", "Bowdoin College", "taught English and education", "1909-1915"),
        ("dartmouth-james-mcconaughy-b1050", "james-mcconaughy-dartmouth-b1050", "Dartmouth College", "professor of education", "1918-1925"),
        ("knox-james-mcconaughy-b1050", "james-mcconaughy-knox-b1050", "Knox College", "president", "date not separately stated"),
    ):
        values.append(
            claim(
                key,
                24,
                "other_pre_oss_affiliation",
                f"James Lukens McConaughy worked at {organization} as {role} ({dates}).",
                f"The National Governors Association biography documents McConaughy's {organization} role; dates are preserved only where the source states them.",
                "Confirmed identity from the exact-name and direct OSS bridge in the institutional biographies.",
                "Documented prewar employment, not presented as the immediate predecessor to OSS.",
                "B_authoritative_institutional",
                "high",
                "published",
                "Education and employment are not conflated; the recorded role is employment.",
                [{"source_key": NGA}],
                affiliation_key,
            )
        )
    return values


def unresolved_message(name: str, box: str) -> str:
    return (
        f"Review the indexed Box {box} personnel file for corroborating identifiers, the immediate pre-OSS affiliation, and the last civilian employer. "
        "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed."
    )


def person_updates() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (person_id, name, box) in PEOPLE.items():
        update: dict[str, object] = {
            "person_id": person_id,
            "manual_review_required": True,
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
        }
        if row == 9:
            update.update(
                identity_status="high_confidence",
                identity_evidence="An uncommon exact name, compatible lieutenant-colonel rank, explicit OSS service, Army Air Forces chronology, and Pittsburgh biography connect the index row to the Carnegie Hero Fund institutional profile.",
                personnel_category="commissioned_army_officer",
                commissioned_officer=True,
                allied_or_foreign_personnel=False,
                research_status="verified_employer_found",
                next_action="Review Box 499 for McClintic's precise OSS transfer date and any personnel-file confirmation of his bank role.",
                archival_review_priority="medium",
            )
        elif row == 20:
            update.update(
                identity_status="high_confidence",
                identity_evidence="The index and official Army bulk entry agree in base full name and a nonshared protected identifier; the Army suffix Jr. aligns with the contemporary advertising-industry notice and its two-year military chronology.",
                name_variants=["Harold C McCollom Jr."],
                personnel_category="enlisted_army_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                nara_catalog_id="1263923",
                research_status="verified_employer_found",
                next_action="Review Box 499 for McCollom's immediate military-to-OSS assignment and exact employment departure date.",
                archival_review_priority="medium",
            )
        elif row == 24:
            update.update(
                identity_status="confirmed",
                identity_evidence="The exact indexed name and Dr. title pattern align with two institutional biographies that provide the full middle name, academic chronology, and explicit 1943-1945 OSS civilian-deputy service.",
                name_variants=["James L. McConaughy", "James Lukens McConaughy"],
                personnel_category="civilian_professional_or_administrative_grade",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                research_status="verified_employer_found",
                next_action="Review Box 499 for McConaughy's exact OSS appointment date and direct personnel-file confirmation of the transition from Wesleyan and United China Relief.",
                archival_review_priority="medium",
            )
        elif row in ARMY_ASSOCIATIONS:
            update.update(
                identity_status="high_confidence",
                identity_evidence="A previously reviewed official Army bulk crosswalk agrees in name and a nonshared protected identifier. The linkage supports identity but supplies only a broad historical occupation category.",
                personnel_category="enlisted_army_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                nara_catalog_id="1263923",
                research_status="occupation_only_found",
                next_action=f"Review Box {box} to identify a named employer or institution and establish the Army-to-OSS chronology. The official bulk record supplies only a broad historical occupation category.",
                archival_review_priority="high",
            )
        elif row == 23:
            update.update(
                identity_status="high_confidence",
                identity_evidence="The index and official Army bulk entry agree in base full name and a nonshared protected identifier, with Jr. retained as a sourced variant. The Army entry is dated 27 April 1946 and is not used as pre-OSS occupation evidence.",
                name_variants=["Oscar D McCollum Jr."],
                personnel_category="enlisted_army_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                nara_catalog_id="1263923",
                research_status="requires_archival_review",
                next_action="Review Box 499 to establish the OSS service sequence and determine whether the 27 April 1946 Army entry has any relevance to pre-OSS employment. No occupation claim is published from the postwar-dated entry.",
                archival_review_priority="high",
            )
        elif row == 21:
            update.update(
                identity_status="conflicting",
                identity_evidence="The adjacent page-304 Elmer L. McCcollum and page-305 Elmer L. McCollum rows differ in spelling and rank context. They remain separate because the current evidence does not prove duplication.",
                possible_duplicate_group=DUPLICATE_GROUPS[row],
                research_status="conflicting_sources",
                next_action="Compare the page-304 and page-305 Box 499 personnel files before merging, transferring an occupation, or resolving the rank and surname spelling conflict.",
                archival_review_priority="critical",
            )
        elif row in IDENTITY_REVIEW_ROWS:
            update.update(
                identity_status="ambiguous",
                identity_evidence="The index contains repeated same-name rows without enough distinguishing information to merge them. Each printed row remains a separate entity pending direct personnel-file comparison.",
                possible_duplicate_group=DUPLICATE_GROUPS[row],
                research_status="requires_archival_review",
                next_action=unresolved_message(name, box),
                archival_review_priority="critical",
            )
        else:
            update.update(
                identity_status="unresolved",
                identity_evidence="Exact-name and meaningful-variant checks across the NARA index context, official CIA and Archives domains, OSS discovery, Library of Congress newspapers, employment, occupation, obituary, institutional, directory, and archival sources produced no reliable identity and pre-OSS affiliation bridge; unbridged namesakes were rejected.",
                research_status="requires_archival_review",
                next_action=unresolved_message(name, box),
                archival_review_priority="high",
            )
        values.append(update)
    if len(values) != 46:
        raise RuntimeError(f"Expected 46 person updates, generated {len(values)}")
    return values


def outcome_note(row: int) -> str:
    if row == 9:
        return "An institutional profile bridges the exact person to OSS, VIII Bomber Command, and Mellon National Bank and Trust Company."
    if row == 20:
        return "Contemporary trade press documents Benton & Bowles employment before military service; the official Army crosswalk supports identity and a qualified occupation category."
    if row == 24:
        return "Two institutional biographies document McConaughy's OSS leadership, immediate United China Relief affiliation, Wesleyan employment, and earlier academic roles."
    if row in ARMY_ASSOCIATIONS:
        return "A previously accepted official Army identity crosswalk supports a qualified Army-entry occupation or student category but no named employer or OSS-transfer sequence."
    if row == 23:
        return "The accepted official Army identity crosswalk is dated after the wartime OSS period; its occupation code is withheld pending chronology review."
    if row in IDENTITY_REVIEW_ROWS:
        return "A repeated name, spelling conflict, or insufficiently distinguished source row remains separate for direct personnel-file comparison."
    return "No reliable identity or pre-OSS affiliation was established; unbridged namesakes and chronologically irrelevant results were rejected."


def research_attempts() -> list[dict[str, object]]:
    updates = {item["person_id"]: item for item in person_updates()}
    values: list[dict[str, object]] = []
    for row, (person_id, name, box) in PEOPLE.items():
        if row in {9, 20, 24}:
            outcome = "source_reviewed"
            reviewed = 9
            rejected = 3
        elif row in ARMY_ASSOCIATIONS or row == 23:
            outcome = "source_reviewed"
            reviewed = 7
            rejected = 3
        elif row in IDENTITY_REVIEW_ROWS:
            outcome = "candidate_rejected"
            reviewed = 6
            rejected = 5
        else:
            outcome = "no_result"
            reviewed = 5
            rejected = 3
        values.append(
            {
                "key": f"page305-row{row}-{slug(name)}-b1050",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index context; exact-name and meaningful initial, punctuation, spelling and OCR variants; official CIA Reading Room and Archives domain checks; OSS, rank, branch, assignment and protected-identifier clues; employer and occupation 1940; obituary, biography, institutional, Library of Congress newspaper, directory and archival searches; indexed Box {box}",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_1050",
                "started_at": "2026-11-11T06:05:00-05:00",
                "completed_at": "2026-11-11T07:35:00-05:00",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, postwar-only leads, and sources without an OSS, rank, protected-identifier, unit, or personnel-file bridge were rejected. Repeated and spelling-conflict rows remain separate. Army categories were not converted into named employers.",
                "research_notes": f"{outcome_note(row)} The official index, earlier Library of Congress item-level pass, exact-name OSS search, official CIA and Archives domain searches, occupation and employer searches, and obituary, institutional, directory, military-history, newspaper, and archival discovery were reviewed as applicable. Direct CIA adapter access was not treated as a negative result. No authenticated NARA Catalog API request was made.",
                "next_action": str(updates[person_id]["next_action"]),
                "attempt_number": 3 if row in ATTEMPT_NUMBER_3 else 2,
                "research_agent_version": "before-oss-b1050-v1",
            }
        )
    if len(values) != 46:
        raise RuntimeError(f"Expected 46 research attempts, generated {len(values)}")
    return values


def main() -> None:
    bundle = {
        "bundle_version": "batch-1050-v1",
        "reviewer": "Before OSS Batch 1050 evidence review",
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
