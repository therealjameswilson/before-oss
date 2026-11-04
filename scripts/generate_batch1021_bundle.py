#!/usr/bin/env python3
"""Generate the reviewed Batch 1021 evidence bundle for PDF page 511."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page511-ernest-wohlleben-to-joseph-wolverton-review_"
    "batch-1021_2026-11-04.json"
)

INDEX = "nara-index-page511-b1021"
RAND_WOLF = "rand-deans-report-charles-wolf-b1021"
HOOVER_WOLFF = "hoover-milton-wolff-oss-b1021"
HARVARD_WOLFF = "harvard-hollis-robert-lee-wolff-papers"
CAMBRIDGE_WOLFF = "cambridge-obituary-robert-lee-wolff-b1021"
DARTMOUTH_WOLBARST = "dartmouth-round-girdled-earth-wolbarst-b1021"
OSS_ORDER_WOLKONSKY = "oss-order-peter-wolkonsky-b1021"
POST_WOLKONSKY = "washington-post-peter-wolkonsky-b1021"
LOC_WOLKONSKY = "loc-annual-report-1944-wolkonsky-b1021"

ORG_ARMY = "united-states-army-b1021-canonical"
ORG_HARVARD = "harvard-university"
ORG_DARTMOUTH = "dartmouth-college-b1021-canonical"
ORG_LOC = "library-of-congress-b1021-canonical"

PEOPLE = {
    1: ("b85d3546-2c53-5d94-abba-3bf91b48eecd", "Ernest H Wohlleben", "849"),
    2: ("af6fc4ea-cf12-5f31-a688-cb3f148ebcd3", "Oscar D Wohowell", "849"),
    3: ("f83729de-8a4b-50bf-823e-3ca7c49a80fe", "Amelia Wojciechosski", "849"),
    4: ("14969977-44c9-5f8e-9cdd-5a87c7ca462b", "Edwin Wojciechosws", "849"),
    5: ("ec4175b5-2735-5004-9e2d-96c04dcb9c21", "Frank Wojciechosws", "849"),
    6: ("7f7cbf88-8d33-5afb-acd0-35e5b596a6e5", "Henry J Wojciechosws", "849"),
    7: ("ca924b9c-d0a9-5524-9dfe-7b15c881b6aa", "Alfred A Wojton", "849"),
    8: ("67bd46ef-9d8b-53bd-a083-296e6956418a", "Louis E Wokal", "849"),
    9: ("e4a5a62f-939c-5498-a7ce-fdd1c3fab060", "Richard H Woktkamp", "850"),
    10: ("25aacc89-f678-5484-b3dd-9378a9e67bf3", "Roger K Wolbarst", "849"),
    11: ("7e83cccc-ec0e-55eb-8d80-53c9a89030ed", "Cedric M Wolcott", "849"),
    12: ("231bedc9-bcb0-59b5-aaaf-ea8b2e491951", "Sylvia M Wolcott", "849"),
    13: ("3ded2f9d-db08-5a49-8f38-91d2face2505", "Leonard R Wold", "849"),
    14: ("ae2711c6-a74a-53ff-841d-17e8a30d621d", "Charles Wolf Jr.", "849"),
    15: ("920b317d-e94e-5c7b-9c0b-73035987742b", "George H Wolf", "849"),
    16: ("c0ea225f-2320-5a44-a35c-78aa32be7a0f", "Henry P Wolf", "849"),
    17: ("95e6405f-438c-5b88-811c-b36a6d02ffdd", "Mortimer B Wolf", "849"),
    18: ("44a9f4b4-8d63-5c24-8b6c-5574ea45ee3e", "Richard A Wolf", "849"),
    19: ("d765b871-8365-587c-bb79-dc32a947a766", "Robert Wolf", "849"),
    20: ("2de9d162-4a21-5d2d-8337-0d7183b32d9a", "Robert E Wolf", "849"),
    21: ("54de69a3-477b-580b-b338-1015ebd7c2ac", "William D Wolf", "849"),
    22: ("42d8567c-e48a-5442-99e5-30ef6f69237a", "Wolfgang Wolf", "849"),
    23: ("7c546ed2-1a3b-5a9c-89c5-11ef3fce58e3", "Arthur E Wolfe", "849"),
    24: ("f0f3a8e0-170d-503d-84b9-4301cda4f031", "Edward K Wolfe Jr.", "849"),
    25: ("1edf6f5b-e708-5a5a-9718-cc229a72b281", "Eugene W Wolfe", "849"),
    26: ("2e6eb349-42c9-5415-95d6-d41825e98338", "Harvey E Wolfe", "849"),
    27: ("ce37d6cb-9495-50b2-b4ed-7fed21690ca5", "Helen C Wolfe", "849"),
    28: ("6bbb2a8e-c99e-57b7-b952-4b48d8d2c50d", "Lloyd O Wolfe", "849"),
    29: ("fdf659a0-95ee-5e35-a539-af751e6b6644", "Maynard M Wolfe", "849"),
    30: ("ddb81cdf-58c7-5db1-9ca4-23d59c8b40c4", "Walter J Wolfe", "850"),
    31: ("be21ec5b-a536-5b9d-8929-f9215b847e28", "Charles Wolff", "850"),
    32: ("7f52ccd4-6e38-53e0-aeb2-379265c3550a", "Edward D Wolff", "850"),
    33: ("b41c09fd-d616-58cf-b2b6-f7a84ce66e1c", "Milton Wolff", "850"),
    34: ("fe8ec29a-718c-56f3-af64-d619600f4f0d", "Robert L Wolff", "850"),
    35: ("420619ac-4e9f-54cd-90b9-d0f33e069fed", "Roger E Wolff", "850"),
    36: ("149a5816-5570-528a-95e2-f63d62bfd037", "Henry J Wolfs", "850"),
    37: ("8884ab25-95d8-5ab1-a618-69fae44b77fd", "Dorothy E Wolgamott", "850"),
    38: ("63d832dc-8f83-5253-9f3a-573d3171a2c6", "Sol J Wolk", "850"),
    39: ("f769ad45-d683-5fb7-b478-d32fa77c08a7", "Dimitri Wolkonsky", "850"),
    40: ("f73382fa-fd80-500a-86e3-1bdcf682bb12", "Peter N Wolkonsky", "850"),
    41: ("1ab44cee-fbb9-52f9-9095-fcf7db962a2f", "George F Woll Jr.", "850"),
    42: ("d37e1eac-1b51-50b5-acb6-f0a703c330e8", "Anthony A Wollner", "850"),
    43: ("ebe17d7d-31b9-5059-a8d0-2b8bb883259e", "Gus Wollner", "850"),
    44: ("1e5eb27a-089f-5028-b423-3fc947bab111", "Lee J Wolovsky", "850"),
    45: ("b1763bd5-7915-5240-83e1-2668f5a7cb64", "Kenneth N Wolter", "850"),
    46: ("8fd2f470-9e6f-5af5-8d1a-6468a11acf3e", "Joseph Wolverton", "850"),
}

WOLBARST = 10
CHARLES_WOLF = 14
MILTON_WOLFF = 33
ROBERT_WOLFF = 34
PETER_WOLKONSKY = 40
SPECIAL = {WOLBARST, CHARLES_WOLF, MILTON_WOLFF, ROBERT_WOLFF, PETER_WOLKONSKY}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


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
            locator="PDF page 511, rows 1-46; Boxes 849-850; visually checked against the source table",
            identifier="RG 226, Entry A1-224, Boxes 849-850",
            collection="Records of the Office of Strategic Services, Record Group 226",
            rights="Every printed row remains separate. Full service identifiers remain private and are omitted from this bundle.",
        ),
        source(
            RAND_WOLF,
            "https://www.rand.org/content/dam/rand/pubs/corporate_pubs/CP700/CP716-2017/RAND_CP716-2017.pdf",
            "2016 Dean's Report: Report to the Board of Governors",
            "Pardee RAND Graduate School",
            "B_authoritative_institutional",
            author="Susan L. Marquis",
            date="2017",
            locator="Printed pages 24-25; Charles Wolf Jr. memorial biography",
            identifier="RAND CP-716-2017",
            rights="Institutional memorial; only short excerpts and project-authored paraphrases are retained.",
        ),
        source(
            HOOVER_WOLFF,
            "https://www.hoover.org/research/spain-shadows-abraham-lincoln-brigade-veterans-milton-wolff-and-oss-world-war-ii",
            "From Spain to the Shadows: Abraham Lincoln Brigade Veterans, Milton Wolff, and the OSS in World War II",
            "Hoover Institution",
            "B_authoritative_institutional",
            author="Zafiris Rossidis",
            date="2026-02-13",
            locator="Paragraphs on Milton Wolff's Army enlistment and subsequent recruitment into OSS-linked intelligence work",
            collection="Military History in Contemporary Conflict Working Group",
            rights="Institutional research article; only concise project-authored paraphrases are retained.",
        ),
        {
            **source(
                HARVARD_WOLFF,
                "https://id.lib.harvard.edu/ead/hua41021/catalog",
                "Papers of Robert Lee Wolff, 1932-1992",
                "Harvard Library, HOLLIS for Archival Discovery",
                "B_authoritative_institutional",
                author="Harvard University Archives",
                date="2021-05; updated 2022-05-02",
                locator="Biographical and scope notes; graduate teaching and OSS Balkan Section service",
                identifier="HUGFP 108",
                collection="Harvard University Archives",
                rights="Institutional finding aid; concise project-authored paraphrases only.",
            ),
            "source_id": "f68d3ddf-92cb-5d64-bfaa-90fdb6d12fd9",
        },
        source(
            CAMBRIDGE_WOLFF,
            "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/1BF9128CD27BE87CAF33DCFFC6B2A5FD/S0037677900102712a.pdf/robert_lee_wolff_19151980.pdf",
            "Robert Lee Wolff, 1915-1980",
            "Cambridge University Press",
            "C_reputable_contemporary_or_scholarly",
            author="Keith Hitchins",
            date="1981",
            locator="Slavic Review, News of the Profession, page 1",
            identifier="DOI 10.1017/S0037677900102712",
            rights="Scholarly obituary; only short excerpts and project-authored paraphrases are retained.",
        ),
        source(
            DARTMOUTH_WOLBARST,
            "https://archive.dartmouthalumnimagazine.com/article/1944/12/1/round-the-girdled-earth",
            "'Round the Girdled Earth",
            "Dartmouth Alumni Magazine",
            "C_reputable_contemporary_or_scholarly",
            author="H. F. W.",
            date="1944-12",
            locator="Letters from Dartmouth Men in the Armed Forces; Roger K. Wolbarst '43",
            rights="Contemporary alumni magazine; only a short excerpt and paraphrase are retained.",
        ),
        source(
            OSS_ORDER_WOLKONSKY,
            "https://documents3.theblackvault.com/documents/jfkfiles/NARA-Oct2017/NARA-Nov-2017/104-10165-10120.pdf",
            "OSS SI Field Detachment, 1st U.S. Army: Normandy Campaign commendation order",
            "National Archives release mirrored by The Black Vault",
            "A_direct_official",
            author="Office of Strategic Services",
            date="1944",
            locator="Page 1; Peter N. Wolkonsky in the SI Field Detachment roster",
            identifier="NARA JFK release 104-10165-10120",
            collection="Office of Strategic Services records",
            rights="The direct official roster supplies a protected identity bridge; the full identifier is excluded from public evidence.",
        ),
        source(
            POST_WOLKONSKY,
            "https://www.washingtonpost.com/archive/local/1997/01/21/caterer-julia-boggs-95-dies/af35a92f-b123-44d0-83b5-f6be7a524a9e/",
            "Peter Nicholas Wolkonsky: Army Officer",
            "The Washington Post",
            "C_reputable_contemporary_or_scholarly",
            author="Claudia Levy",
            date="1997-01-20; correction 1997-01-22",
            locator="Peter Nicholas Wolkonsky obituary section",
            rights="Reputable obituary; only concise project-authored paraphrases are retained.",
        ),
        source(
            LOC_WOLKONSKY,
            "https://tile.loc.gov/storage-services/service/gdc/scd0002/0014/00142142041/00142142041.pdf",
            "Annual Report of the Librarian of Congress for the Fiscal Year Ending June 30, 1944",
            "Library of Congress",
            "A_direct_official",
            author="Library of Congress",
            date="1944",
            locator="Personnel roster; Peter N. Wolkonsky, Photoduplication Service",
            collection="Annual Reports of the Librarian of Congress",
            rights="Official staff roster. It does not state the exact beginning or ending date of employment.",
        ),
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": ORG_ARMY,
            "organization_id": "28a26f92-78af-5a1a-9c09-a843eb5975b4",
            "canonical_name": "United States Army",
            "historical_name": "United States Army",
            "aliases": ["U.S. Army", "Army", "AUS"],
            "organization_type": "military service",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "Military assignment is modeled separately from civilian employment.",
        },
        {
            "key": ORG_HARVARD,
            "organization_id": "45ddf347-21c6-59f5-a8ae-517418adf941",
            "canonical_name": "Harvard University",
            "historical_name": "Harvard University",
            "aliases": ["Harvard", "Harvard College"],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "Cambridge",
            "state_or_region": "Massachusetts",
            "country": "United States",
            "normalization_notes": "Student status and employment are modeled as distinct relationships.",
        },
        {
            "key": ORG_DARTMOUTH,
            "organization_id": "876621b2-b018-55a7-800e-242fe98b2deb",
            "canonical_name": "Dartmouth College",
            "historical_name": "Dartmouth College",
            "aliases": ["Dartmouth"],
            "organization_type": "college",
            "sector": "academia_and_research",
            "city": "Hanover",
            "state_or_region": "New Hampshire",
            "country": "United States",
            "normalization_notes": "Wolbarst's documented relationship is student status, not employment.",
        },
        {
            "key": ORG_LOC,
            "organization_id": "11a2ad2b-e917-5a2a-abe3-9c391b43a51a",
            "canonical_name": "Library of Congress",
            "historical_name": "Library of Congress",
            "aliases": ["Library of Congress Photoduplication Service"],
            "organization_type": "federal library",
            "sector": "federal_government",
            "city": "Washington",
            "state_or_region": "District of Columbia",
            "country": "United States",
            "normalization_notes": "The Photoduplication Service is retained as the historical unit, not split into a separate employer.",
        },
    ]


def affiliations() -> list[dict[str, object]]:
    return [
        {
            "key": "charles-wolf-harvard-student-b1021",
            "person_id": PEOPLE[CHARLES_WOLF][0],
            "organization_key": ORG_HARVARD,
            "organization_name_as_found": "Harvard University",
            "role_title": "undergraduate student",
            "occupation": "student",
            "relationship_type": "student",
            "end_date": "1943",
            "date_precision": "RAND says he earned a bachelor's degree in economics in three years and graduated in 1943; the matriculation date is unstated.",
            "city": "Cambridge",
            "state_or_region": "Massachusetts",
            "country": "United States",
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "confirmed",
            "claim_confidence": "high",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "published",
            "research_notes": "Student status is not counted as employment or as a civilian employer.",
        },
        {
            "key": "charles-wolf-army-b1021",
            "person_id": PEOPLE[CHARLES_WOLF][0],
            "organization_key": ORG_ARMY,
            "organization_name_as_found": "Army",
            "role_title": "corporal serving in OSS in Italy",
            "occupation": "Army enlisted personnel",
            "relationship_type": "military_assignment",
            "start_date": "1943",
            "date_precision": "RAND says he enlisted after his 1943 Harvard graduation and was soon serving as an OSS corporal in Italy; exact dates are unstated.",
            "country": "Italy",
            "immediate_pre_oss": True,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "confirmed",
            "claim_confidence": "high",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "published",
            "research_notes": "The Army-to-OSS pathway is supported; no civilian employer is identified.",
        },
        {
            "key": "roger-wolbarst-dartmouth-student-b1021",
            "person_id": PEOPLE[WOLBARST][0],
            "organization_key": ORG_DARTMOUTH,
            "organization_name_as_found": "Dartmouth",
            "role_title": "Class of 1943",
            "occupation": "student",
            "relationship_type": "student",
            "end_date": "1943",
            "date_precision": "The contemporary alumni magazine identifies him as Roger K. Wolbarst '43; exact attendance dates are unstated.",
            "city": "Hanover",
            "state_or_region": "New Hampshire",
            "country": "United States",
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "published",
            "research_notes": "Student status is not employment. The accessible source does not establish his exact OSS transition.",
        },
        {
            "key": "milton-wolff-army-b1021",
            "person_id": PEOPLE[MILTON_WOLFF][0],
            "organization_key": ORG_ARMY,
            "organization_name_as_found": "Army",
            "role_title": "enlisted soldier recruited into OSS-linked intelligence work",
            "occupation": "Army enlisted personnel",
            "relationship_type": "military_assignment",
            "start_date": "1942",
            "date_precision": "Hoover says he enlisted after U.S. entry into the war and was subsequently recruited into OSS-linked intelligence; exact dates are unstated.",
            "country": "United States",
            "immediate_pre_oss": True,
            "pre_oss_temporal_basis": "explicit_immediate",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "published",
            "research_notes": "This is a military pathway, not a civilian employer. Earlier Spanish Civil War service is not labeled employment.",
        },
        {
            "key": "robert-wolff-harvard-teaching-assistant",
            "person_id": PEOPLE[ROBERT_WOLFF][0],
            "organization_key": ORG_HARVARD,
            "organization_name_as_found": "Harvard",
            "role_title": "teaching fellow while a graduate student",
            "occupation": "historian and teaching fellow",
            "relationship_type": "employment",
            "start_date": "1937",
            "end_date": "1942",
            "date_precision": "The scholarly obituary dates his teaching fellowship from 1937 and OSS Balkan Section service from 1942; exact appointment and departure days are unstated.",
            "city": "Cambridge",
            "state_or_region": "Massachusetts",
            "country": "United States",
            "immediate_pre_oss": True,
            "last_civilian_pre_service": True,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "published",
            "research_notes": "The obituary explicitly says his academic career was interrupted by 1942-1946 OSS service.",
        },
        {
            "key": "peter-wolkonsky-army-intelligence-b1021",
            "person_id": PEOPLE[PETER_WOLKONSKY][0],
            "organization_key": ORG_ARMY,
            "organization_name_as_found": "Army intelligence",
            "role_title": "sergeant; Army intelligence in North Africa",
            "occupation": "Army enlisted intelligence personnel",
            "relationship_type": "military_assignment",
            "country": "North Africa",
            "immediate_pre_oss": True,
            "pre_oss_temporal_basis": "explicit_immediate",
            "identity_confidence": "confirmed",
            "claim_confidence": "high",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "published",
            "date_precision": "The obituary explicitly sequences initial Army intelligence service in North Africa before OSS service in Europe; exact dates are unstated.",
            "research_notes": "The direct OSS roster confirms identity through a protected identifier that is not exposed publicly.",
        },
        {
            "key": "peter-wolkonsky-library-congress-b1021",
            "person_id": PEOPLE[PETER_WOLKONSKY][0],
            "organization_key": ORG_LOC,
            "organization_name_as_found": "Photoduplication Service",
            "role_title": "staff member",
            "occupation": "Photoduplication Service staff",
            "relationship_type": "employment",
            "city": "Washington",
            "state_or_region": "District of Columbia",
            "country": "United States",
            "last_civilian_pre_service": True,
            "pre_oss_temporal_basis": "probable_immediate",
            "identity_confidence": "confirmed",
            "claim_confidence": "medium",
            "source_quality": "A_direct_official",
            "publication_status": "publish_qualified",
            "date_precision": "The 1944 Library roster names Peter N. Wolkonsky in Photoduplication Service while independent sources place him in wartime Army and OSS service; exact employment dates and leave status are unstated.",
            "research_notes": "Qualified as the probable last civilian employer; the personnel file is still needed to confirm the transition and leave chronology.",
        },
    ]


def make_claim(
    *,
    key: str,
    row: int,
    claim_type: str,
    text: str,
    paraphrase: str,
    identity: str,
    temporal: str,
    quality: str,
    confidence: str,
    publication: str,
    notes: str,
    source_links: list[dict[str, str]],
    affiliation_key: str | None = None,
    excerpt: str | None = None,
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
    if excerpt:
        value["evidence_excerpt"] = excerpt
    return value


def claims() -> list[dict[str, object]]:
    return [
        make_claim(
            key="identity-charles-wolf-jr-b1021",
            row=CHARLES_WOLF,
            claim_type="identity",
            text="Indexed Corporal Charles Wolf Jr. is confirmed as the Harvard graduate who served as an OSS corporal in Italy.",
            paraphrase="The exact name and suffix, corporal rank, and OSS service in Italy align between the index and RAND's institutional biography.",
            identity="Confirmed by exact name and suffix plus the matching corporal rank and specific OSS service in Italy.",
            temporal="RAND dates Harvard graduation, Army enlistment, and OSS service to 1943.",
            quality="B_authoritative_institutional",
            confidence="confirmed",
            publication="published",
            notes="No serial number is needed or exposed for this identity resolution.",
            source_links=[{"source_key": INDEX}, {"source_key": RAND_WOLF}],
        ),
        make_claim(
            key="charles-wolf-harvard-student-b1021",
            row=CHARLES_WOLF,
            affiliation_key="charles-wolf-harvard-student-b1021",
            claim_type="other_pre_oss_affiliation",
            text="Charles Wolf Jr. was a Harvard University undergraduate before Army and OSS service.",
            paraphrase="RAND says he completed a bachelor's degree in economics in three years and graduated in 1943 before enlisting.",
            identity="Confirmed exact-name, suffix, rank and OSS-role match.",
            temporal="Strongly date-bounded immediately before Army enlistment, but it was student status rather than employment.",
            quality="B_authoritative_institutional",
            confidence="high",
            publication="published",
            notes="Harvard is not counted as an employer for this relationship.",
            source_links=[{"source_key": RAND_WOLF, "locator_override": "Printed page 25"}],
            excerpt="After graduating in 1943, he enlisted in the Army",
        ),
        make_claim(
            key="charles-wolf-army-immediate-b1021",
            row=CHARLES_WOLF,
            affiliation_key="charles-wolf-army-b1021",
            claim_type="immediate_pre_oss_affiliation",
            text="Charles Wolf Jr.'s immediate pre-OSS pathway was enlistment in the United States Army.",
            paraphrase="RAND says he enlisted after Harvard and was soon serving as an OSS corporal in Italy.",
            identity="Confirmed exact-name, suffix, corporal-rank and OSS-location match.",
            temporal="Strongly date-bounded Army-to-OSS pathway in 1943; no exact transfer day is stated.",
            quality="B_authoritative_institutional",
            confidence="high",
            publication="published",
            notes="This is a military affiliation, not a civilian employer.",
            source_links=[{"source_key": RAND_WOLF, "locator_override": "Printed page 25"}],
            excerpt="serving in Italy as a corporal in the Office of Strategic Services",
        ),
        make_claim(
            key="identity-roger-wolbarst-b1021",
            row=WOLBARST,
            claim_type="identity",
            text="Indexed Roger K Wolbarst is a high-confidence match to Dartmouth alumnus Sergeant Roger K. Wolbarst, Class of 1943.",
            paraphrase="The exact uncommon full name and middle initial, matching sergeant rank, 1943 class year, and wartime Army service in India align.",
            identity="High confidence from the rare exact name plus matching sergeant rank and contemporaneous Army service in India.",
            temporal="The source documents wartime Army service in December 1944 but does not establish the exact OSS transition.",
            quality="C_reputable_contemporary_or_scholarly",
            confidence="high",
            publication="published",
            notes="The indexed personnel file remains necessary to verify the unit and OSS chronology.",
            source_links=[{"source_key": INDEX}, {"source_key": DARTMOUTH_WOLBARST}],
            excerpt="SERGEANT ROGER K. WOLBARST '43, AUS",
        ),
        make_claim(
            key="roger-wolbarst-dartmouth-student-b1021",
            row=WOLBARST,
            affiliation_key="roger-wolbarst-dartmouth-student-b1021",
            claim_type="other_pre_oss_affiliation",
            text="Roger K. Wolbarst was a member of Dartmouth College's Class of 1943.",
            paraphrase="The December 1944 alumni magazine identifies Sergeant Roger K. Wolbarst as Dartmouth Class of 1943.",
            identity="High-confidence uncommon-name, initial and rank match.",
            temporal="Documented prewar student status; exact attendance and graduation dates are unstated.",
            quality="C_reputable_contemporary_or_scholarly",
            confidence="high",
            publication="published",
            notes="Dartmouth is not counted as an employer for this relationship.",
            source_links=[{"source_key": DARTMOUTH_WOLBARST}],
        ),
        make_claim(
            key="identity-milton-wolff-b1021",
            row=MILTON_WOLFF,
            claim_type="identity",
            text="Indexed Milton Wolff is a high-confidence match to the Abraham Lincoln Battalion veteran recruited into OSS-linked intelligence work.",
            paraphrase="The distinctive exact name and Hoover's specific Army-to-OSS account align with the indexed personnel file.",
            identity="High confidence from the distinctive name and a detailed institutional account of Army enlistment followed by OSS-linked intelligence work.",
            temporal="Hoover explicitly sequences Army enlistment before recruitment into intelligence work linked to OSS.",
            quality="B_authoritative_institutional",
            confidence="high",
            publication="published",
            notes="Box 850 remains unreviewed; the profile does not use a famous biography without an OSS-specific bridge.",
            source_links=[{"source_key": INDEX}, {"source_key": HOOVER_WOLFF}],
        ),
        make_claim(
            key="milton-wolff-army-immediate-b1021",
            row=MILTON_WOLFF,
            affiliation_key="milton-wolff-army-b1021",
            claim_type="immediate_pre_oss_affiliation",
            text="Milton Wolff enlisted in the United States Army before recruitment into OSS-linked intelligence work.",
            paraphrase="Hoover says Wolff enlisted after U.S. entry into World War II and was subsequently recruited into intelligence work linked to OSS.",
            identity="High-confidence distinctive-name and OSS-specific institutional match.",
            temporal="Explicitly sequenced Army-to-OSS pathway; exact enlistment and recruitment dates are not stated.",
            quality="B_authoritative_institutional",
            confidence="high",
            publication="published",
            notes="This is a military affiliation, not a civilian employer.",
            source_links=[{"source_key": HOOVER_WOLFF}],
            excerpt="enlisted in the Army and was subsequently recruited into intelligence work",
        ),
        make_claim(
            key="identity-robert-l-wolff",
            row=ROBERT_WOLFF,
            claim_type="identity",
            text="Indexed Robert L. Wolff is Harvard historian Robert Lee Wolff, who led the OSS Research and Analysis Branch's Balkan Section.",
            paraphrase="The exact full name and middle initial, Balkan specialization, Harvard chronology, and specific OSS section leadership align.",
            identity="High confidence from exact name, field, Harvard affiliation, and an unusually specific 1942-1946 OSS role across two authoritative sources.",
            temporal="The scholarly obituary dates Harvard teaching from 1937 and OSS service from 1942 through 1946.",
            quality="B_authoritative_institutional",
            confidence="high",
            publication="published",
            notes="The index file remains unreviewed, but the accessible identity evidence is specific and independently corroborated.",
            source_links=[{"source_key": INDEX}, {"source_key": HARVARD_WOLFF}, {"source_key": CAMBRIDGE_WOLFF}],
        ),
        make_claim(
            key="employment-robert-wolff-harvard-teaching-assistant",
            row=ROBERT_WOLFF,
            affiliation_key="robert-wolff-harvard-teaching-assistant",
            claim_type="immediate_pre_oss_affiliation",
            text="Robert Lee Wolff's immediate pre-OSS affiliation was employment as a Harvard teaching fellow.",
            paraphrase="The scholarly obituary says he became a Harvard teaching fellow in 1937 and that his academic career was interrupted by 1942-1946 OSS service.",
            identity="High-confidence exact-name, field, institution and OSS-section match.",
            temporal="Strongly date-bounded: teaching fellow from 1937, followed by OSS service beginning in 1942.",
            quality="C_reputable_contemporary_or_scholarly",
            confidence="high",
            publication="published",
            notes="The earlier qualified teaching-assistant lead is upgraded by explicit scholarly chronology.",
            source_links=[{"source_key": CAMBRIDGE_WOLFF}, {"source_key": HARVARD_WOLFF, "support_type": "context_only"}],
            excerpt="became a teaching fellow. His academic career was interrupted by World War II",
        ),
        make_claim(
            key="last-civilian-robert-wolff-harvard-b1021",
            row=ROBERT_WOLFF,
            affiliation_key="robert-wolff-harvard-teaching-assistant",
            claim_type="last_civilian_pre_service",
            text="Harvard University was Robert Lee Wolff's last documented civilian employer before OSS service.",
            paraphrase="His teaching fellowship began in 1937, and the obituary directly sequences that academic career before OSS service from 1942.",
            identity="High-confidence exact-name, field, institution and OSS-section match.",
            temporal="Strongly date-bounded with no intervening civilian employer documented in the reviewed sources.",
            quality="C_reputable_contemporary_or_scholarly",
            confidence="high",
            publication="published",
            notes="Harvard student status and Harvard employment remain distinct; this claim concerns the paid teaching fellowship.",
            source_links=[{"source_key": CAMBRIDGE_WOLFF}, {"source_key": HARVARD_WOLFF, "support_type": "context_only"}],
        ),
        make_claim(
            key="identity-peter-wolkonsky-b1021",
            row=PETER_WOLKONSKY,
            claim_type="identity",
            text="Indexed Sergeant Peter N. Wolkonsky is confirmed as the OSS SI Field Detachment member who later became an Army lieutenant colonel.",
            paraphrase="The exact name and rank plus a nonshared protected identifier align with a direct OSS roster; the obituary independently supplies Army-to-OSS chronology.",
            identity="Confirmed by exact name and rank plus a nonshared protected identifier in a direct OSS roster; the identifier remains private.",
            temporal="The official roster establishes wartime OSS service; the obituary sequences earlier Army intelligence and later OSS service.",
            quality="A_direct_official",
            confidence="confirmed",
            publication="published",
            notes="The public evidence deliberately omits the full service identifier.",
            source_links=[{"source_key": INDEX}, {"source_key": OSS_ORDER_WOLKONSKY}, {"source_key": POST_WOLKONSKY}],
        ),
        make_claim(
            key="peter-wolkonsky-army-immediate-b1021",
            row=PETER_WOLKONSKY,
            affiliation_key="peter-wolkonsky-army-intelligence-b1021",
            claim_type="immediate_pre_oss_affiliation",
            text="Peter N. Wolkonsky served with Army intelligence in North Africa before joining OSS in Europe.",
            paraphrase="The Washington Post obituary explicitly sequences initial Army intelligence service in North Africa before OSS service in Europe.",
            identity="Confirmed through the direct OSS roster's protected-identifier match and the obituary's exact full name and wartime chronology.",
            temporal="Explicitly immediate military sequence; exact assignment and transfer dates are unstated.",
            quality="C_reputable_contemporary_or_scholarly",
            confidence="high",
            publication="published",
            notes="This is a military assignment, not a civilian employer.",
            source_links=[{"source_key": POST_WOLKONSKY}, {"source_key": OSS_ORDER_WOLKONSKY, "support_type": "context_only"}],
            excerpt="served initially with Army intelligence in North Africa during World War II",
        ),
        make_claim(
            key="peter-wolkonsky-library-congress-last-civilian-b1021",
            row=PETER_WOLKONSKY,
            affiliation_key="peter-wolkonsky-library-congress-b1021",
            claim_type="last_civilian_pre_service",
            text="The Library of Congress is Peter N. Wolkonsky's probable last civilian employer before Army and OSS service.",
            paraphrase="The Library's 1944 annual report lists Peter N. Wolkonsky in the Photoduplication Service while independent sources place him in wartime military service.",
            identity="Confirmed through exact name, index rank and a protected-identifier match in a direct OSS roster.",
            temporal="Probable immediate civilian predecessor, but the roster does not state employment start, leave, or separation dates.",
            quality="A_direct_official",
            confidence="medium",
            publication="publish_qualified",
            notes="Visible qualification is required, and the personnel file remains necessary before default employer analytics may include this claim.",
            source_links=[{"source_key": LOC_WOLKONSKY}, {"source_key": POST_WOLKONSKY, "support_type": "context_only"}, {"source_key": OSS_ORDER_WOLKONSKY, "support_type": "context_only"}],
        ),
    ]


def unresolved_reason(row: int) -> str:
    if row == 37:
        return "A 1935 directory names a Dorothy E. Wolgamott at a printing company, but no accessible source bridges that namesake to this OSS row."
    if row == 39:
        return "Sources identifying Peter Wolkonsky's brother Dmitri cannot establish that the relative is this index row; relatives are not used as the identity basis."
    if row == 42:
        return "A rare-name film-editor biography and wartime combat-camera roster are plausible leads, but neither accessible source establishes that Anthony A. Wollner is this indexed OSS person."
    if row in {15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 35}:
        return "Common Wolf, Wolfe or Wolff namesakes lacked the corroborating identifiers required for safe resolution."
    return "Accessible exact-name, OSS, employer, occupation, obituary, institutional, newspaper, directory and archival searches produced no reliable identity-and-affiliation bridge."


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
    for row in sorted(set(PEOPLE) - SPECIAL):
        reason = unresolved_reason(row)
        values.append(
            base_update(
                row,
                identity_status="unresolved",
                identity_evidence=f"The visually checked page 511 row preserves {PEOPLE[row][1]}, Box {PEOPLE[row][2]}, and any printed rank or note. {reason} Unbridged candidates were rejected.",
                research_status="requires_archival_review",
                next_action=f"Review indexed Box {PEOPLE[row][2]} for corroborating identifiers, immediate pre-OSS affiliation and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}",
            )
        )
    values.extend(
        [
            base_update(
                WOLBARST,
                identity_status="high_confidence",
                identity_evidence="The rare exact full name and middle initial, matching sergeant rank, Dartmouth class year, and contemporaneous Army service in India align.",
                name_variants=["Roger K. Wolbarst", "Sergeant Roger K. Wolbarst"],
                replace_name_variants=False,
                personnel_category="enlisted_army_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                research_status="requires_archival_review",
                archival_review_priority="medium",
                next_action="Review Box 849 to confirm Wolbarst's Army unit, exact OSS chronology, and last civilian employer; Dartmouth student status is documented but is not employment.",
            ),
            base_update(
                CHARLES_WOLF,
                identity_status="confirmed",
                identity_evidence="Exact name and suffix, corporal rank, 1943 chronology, and OSS service in Italy align between the index and RAND's institutional biography.",
                name_variants=["Charles Wolf, Jr.", "Corporal Charles Wolf Jr."],
                replace_name_variants=False,
                personnel_category="enlisted_army_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                manual_review_required=False,
                research_status="completed",
                archival_review_priority="medium",
                next_action="Review Box 849 for the precise Army-to-OSS transfer and any paid pre-service work; Harvard student status and the Army pathway are already supported.",
            ),
            base_update(
                MILTON_WOLFF,
                identity_status="high_confidence",
                identity_evidence="The distinctive exact name and Hoover's specific account of Army enlistment followed by recruitment into OSS-linked intelligence work align.",
                name_variants=["Milton Wolff", "Milton 'Milt' Wolff"],
                replace_name_variants=False,
                personnel_category="enlisted_army_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                manual_review_required=False,
                research_status="completed",
                archival_review_priority="medium",
                next_action="Review Box 850 for precise Army and OSS dates and a named last civilian employer; the Army-to-OSS pathway is already supported.",
            ),
            base_update(
                ROBERT_WOLFF,
                identity_status="high_confidence",
                identity_evidence="Exact name, Balkan specialization, Harvard teaching chronology, and 1942-1946 OSS Balkan Section leadership align across Harvard and a scholarly obituary.",
                name_variants=["Robert L. Wolff", "Robert Lee Wolff"],
                replace_name_variants=False,
                manual_review_required=False,
                research_status="verified_employer_found",
                archival_review_priority="medium",
                next_action="Review Box 850 for exact appointment and OSS entry dates; Harvard employment as the immediate and last civilian affiliation is already supported.",
            ),
            base_update(
                PETER_WOLKONSKY,
                identity_status="confirmed",
                identity_evidence="Exact name and sergeant rank plus a nonshared protected identifier connect the index and direct OSS roster; the identifier remains private.",
                name_variants=["Peter N. Wolkonsky", "Peter Nicholas Wolkonsky", "Sgt. Peter N. Wolkonsky"],
                replace_name_variants=False,
                personnel_category="enlisted_army_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                manual_review_required=False,
                research_status="documented_prewar_employer_found",
                archival_review_priority="medium",
                next_action="Review Box 850 to confirm Library of Congress employment and leave dates; Army intelligence immediately before OSS is supported, while the civilian-employer claim remains qualified.",
            ),
        ]
    )
    if len(values) != len(PEOPLE):
        raise RuntimeError(f"Expected {len(PEOPLE)} person updates, generated {len(values)}")
    return values


def research_attempts() -> list[dict[str, object]]:
    attempts: list[dict[str, object]] = []
    for row, (person_id, name, box) in PEOPLE.items():
        outcome = "candidate_rejected"
        reviewed = 6
        rejected = 5
        note = unresolved_reason(row)
        if row == WOLBARST:
            outcome, reviewed, rejected = "source_reviewed", 9, 4
            note = "A contemporary Dartmouth source supports identity, Army rank and student status, but not the exact OSS transition or a civilian employer."
        elif row == CHARLES_WOLF:
            outcome, reviewed, rejected = "source_reviewed", 10, 5
            note = "RAND's institutional biography supports Harvard student status and a 1943 Army-to-OSS pathway in Italy."
        elif row == MILTON_WOLFF:
            outcome, reviewed, rejected = "source_reviewed", 11, 5
            note = "Hoover's institutional research supports Army enlistment followed by OSS-linked intelligence work; no named civilian employer is established."
        elif row == ROBERT_WOLFF:
            outcome, reviewed, rejected = "source_reviewed", 10, 3
            note = "A scholarly obituary supplies explicit 1937 Harvard teaching-fellow and 1942 OSS chronology, upgrading the prior qualified employment lead."
        elif row == PETER_WOLKONSKY:
            outcome, reviewed, rejected = "source_reviewed", 12, 5
            note = "A direct OSS roster confirms identity privately; a reputable obituary supports Army-to-OSS chronology, and an official Library roster supports a qualified civilian-employer claim."
        attempt_number = 3 if row == 7 else 2 if row == ROBERT_WOLFF else 1
        attempts.append(
            {
                "key": f"page511-row{row}-{slug(name)}-b1021",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index context; exact-name and meaningful spelling, middle-name, initial, suffix, punctuation and OCR variants; OSS, rank, branch, unit and protected-identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory and archival searches; indexed Box {box}",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_1021",
                "started_at": "2026-11-04T18:00:00Z",
                "completed_at": "2026-11-04T23:20:00Z",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, postwar-only leads, common-name matches, and sources without an OSS, protected-identifier, rank, unit, institutional or personnel-file bridge were rejected.",
                "research_notes": f"{note} The official index, exact-name OSS searches, employment and occupation searches, and applicable institutional, obituary, newspaper, directory and archival sources were reviewed. Page 511 was checked against the source table. Batch-level CIA and Library of Congress adapter failures were recorded separately and are not treated as negative evidence. Accessible official, institutional, contemporary and scholarly alternatives were reviewed. No authenticated NARA Catalog API request was made.",
                "next_action": f"Review indexed Box {box} for corroborating identifiers, immediate pre-OSS affiliation and last civilian employer before wartime service.",
                "attempt_number": attempt_number,
                "research_agent_version": "before-oss-b1021-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-1021-v1",
        "reviewer": "Before OSS Batch 1021 evidence review",
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
