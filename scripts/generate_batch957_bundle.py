#!/usr/bin/env python3
"""Generate the reviewed Batch 957 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page469-george-s-tinlakos-to-bentley-tobin-"
    "review_batch-957_2026-10-29.json"
)

INDEX = "nara-index-b957"
ARMY = "army-bulk-b957"
TECH = "army-tech-b957"
CODES = "army-codes-b957"
GREECE = "after-battle-tiniakos-b957"
GREEK_MEMORIAL = "us-war-memorials-tiniakos-b957"
STANFORD = "stanford-timoshenko-b957"
BROADCASTING = "broadcasting-tinney-b957"
MBC_TISCH = "mbc-tisch-b957"
ANU_TITIEV = "anu-titiev-b957"
UM_TITIEV = "umich-titiev-b957"
MOMA_TITUS = "moma-roy-titus-b957"
WSU_TJERANDSEN = "wsu-tjerandsen-b957"
LEGACY_TJERANDSEN = "legacy-tjerandsen-b957"
UTAH_TOBARI = "utah-tobari-b957"
BERKELEY_TOBARI = "berkeley-tobari-b957"
SMITHSONIAN_TOBIAS = "smithsonian-tobias-b957"

US_ARMY = "us-army-existing-b957"
STANFORD_ORG = "stanford-existing-b957"
MUTUAL_ORG = "mutual-existing-b957"
NYU_ORG = "nyu-existing-b957"
UMICH_ORG = "umich-existing-b957"
HELENA_ORG = "helena-rubinstein-b957"
UTAH_ORG = "university-utah-b957"
USAAF_ORG = "usaaf-existing-b957"
FAP_ORG = "federal-art-project-existing-b957"
IDAHO_ORG = "university-idaho-b957"
GREEK_MARINE_ORG = "greek-merchant-marine-b957"


PEOPLE = {
    1: ("fb61ba6c-6059-550e-9839-82e058ce3783", "George S Tinlakos"),
    2: ("48d659c6-cab8-5a75-9e42-15f9c5efb2c9", "Vladimir Tinmoshenko"),
    3: ("2b9323d8-17cb-5503-b9ab-240238a9dad4", "Gerhard Tinner"),
    4: ("4977142b-28b4-5965-b7b5-7eb62d661f34", "Amedee Tinners"),
    5: ("3b2e307c-2e90-50fc-aa80-a0203028cef8", "Calvin L Tinney"),
    6: ("eb1fe0e8-97f5-5885-8d74-e9323154bd9b", "Paul Tinney"),
    7: ("f4b40566-0b08-527f-bf49-e7afc4b7650f", "Louise H Tipp"),
    8: ("d255da88-c17e-5014-bc51-06e5a972cc32", "Timonthy L Tippit"),
    9: ("818d4e1f-d461-5cde-b8d3-85c50d2ae0a3", "Lloyd R Tipton"),
    10: ("1c215017-0200-51c6-b49d-566f9a78cdcb", "Joseph Tirpik"),
    11: ("affc7800-9e2e-51f2-bc04-f5e4fdae4af4", "Laurence A Tisch"),
    12: ("b7a5fe6e-a8bc-5da9-a1e4-fb5d7e7e9566", "Chamroon Tishyarandara"),
    13: ("385e9df4-b96c-55fb-9879-2cec534c8cd3", "Paul Tison"),
    14: ("4f650f82-d872-5bab-a27f-c2937118926c", "Mischa Titiev"),
    15: ("0a50dadb-9ce7-5fcf-a35b-cee05810da13", "Austin E Titus"),
    16: ("5c7948a6-b3c3-5ae7-b64e-3c6f7bf1c6f9", "Gerald Titus"),
    17: ("c4470663-f746-5d1b-8be4-a8d01c796fc0", "Roy Titus"),
    18: ("2a6e984b-0962-5841-9d7c-c7ff1d07d76b", "Kenneth D Tivey"),
    19: ("6a5bf026-1024-547c-9b12-ee8055a12439", "Carl Tjerandsen"),
    20: ("fdbd568c-3c2f-59eb-a1c0-098d2e3fc429", "Carl Tjerandsen"),
    21: ("8b47480b-a586-540b-80c3-fdb94bdd067b", "Joseph M Tobari"),
    22: ("178ce891-c060-5d71-8c4c-20646d94107c", "Abraham J Tobias"),
    23: ("cd940470-af04-59be-b654-97e6ccaf928b", "Bentley Tobin"),
}


# The technical documentation defines the six-character Army entry date as
# DD/MM/YY. Categories are point-in-time status or occupation labels, never
# named employers, workplaces, schools, or proof of the OSS transfer date.
ARMY_CATEGORIES = {
    1: ("1943-01-22", "Cooks, except private family", "2-26", 172, "employment", "high_confidence"),
    5: ("1943-09-07", "Authors, editors, and reporters", "0-06", 170, "employment", "confirmed"),
    6: ("1942-08-14", "Architects", "0-03", 170, "employment", "confirmed"),
    11: ("1942-12-10", "Students", "9-92", 304, "student", "high_confidence"),
    17: ("1942-10-01", "Managers and officials, n.e.c.", "0-97", 171, "employment", "confirmed"),
    19: ("1944-07-17", "Professional occupations, n.e.c.", "0-39", 171, "employment", "high_confidence"),
    21: ("1943-05-05", "Students", "9-92", 304, "student", "confirmed"),
    23: ("1942-08-07", "Actors and actresses", "0-02", 170, "employment", "confirmed"),
}


UNRESOLVED = {
    3: "Exact-name, German-language, OSS, military, obituary, directory and institutional searches produced no defensible Box 779 identity bridge.",
    4: "Exact-name, French-language and spelling-variant searches produced no reliable wartime identity, occupation or Box 778 bridge.",
    7: "A same-name death-index lead lacked an OSS, occupation, employer or second-identifier bridge and was rejected.",
    8: "The printed Timonthy spelling and Timothy variants were searched; modern and historical namesakes supplied no reliable Box 779 bridge.",
    9: "The common name produced military and obituary namesakes, none with two corroborating identifiers beyond the name.",
    10: "A secondary OSS operational-group roster contains an S/Sgt. J. Y. G. Tirpik, but the initials and chronology do not safely resolve indexed Joseph Tirpik.",
    12: "Exact printed spelling and Thai transliteration variants produced no reliable OSS, institutional, diplomatic or occupational identity bridge.",
    13: "The common name produced French, U.S. military and obituary namesakes, none with a second identifier or Box 779 bridge.",
    15: "Exact-name, middle-initial, official-domain, military, obituary and directory searches produced no defensible Box 779 identity bridge.",
    16: "The common name produced multiple wartime and later namesakes but no two corroborating identifiers or reliable Box 779 bridge.",
    18: "Exact-name, private-identifier, Army, obituary and Commonwealth variants produced no reliable identity or pre-OSS affiliation.",
    20: "A second printed Carl Tjerandsen row carries a distinct private identifier. It remains separate from row 19 pending Box 779 review and is not double-counted.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def archive_box(row: int) -> str:
    return "778" if row in {2, 4} else "779"


def source(
    key: str,
    url: str,
    title: str,
    publisher: str,
    quality: str,
    locator: str,
    *,
    creator: str | None = None,
    date: str | None = None,
    archival_id: str | None = None,
    collection: str | None = None,
    document: str | None = None,
    rights: str | None = None,
) -> dict[str, object]:
    return {
        "key": key,
        "stable_url": url,
        "archival_identifier": archival_id,
        "title": title,
        "author_creator": creator,
        "repository_publisher": publisher,
        "publication_record_date": date,
        "locator": locator,
        "access_date": "2026-10-29",
        "source_quality": quality,
        "collection_name": collection,
        "document_number": document,
        "rights_notes": rights,
    }


def sources() -> list[dict[str, object]]:
    return [
        source(
            INDEX,
            "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "OSS Personnel Files from Excel",
            "National Archives and Records Administration",
            "A_direct_official",
            "PDF page 469, rows 1-23; checked against layout-preserving text and a 220 dpi page render",
            creator="National Archives and Records Administration",
            date="2010-12-23",
            archival_id="RG 226, Entry A1-224, Boxes 778-779",
            collection="Records of the Office of Strategic Services, Record Group 226",
            rights="All 23 printed rows remain separate. Printed Tinlakos, Tinmoshenko and Timonthy spellings are preserved; private identifiers remain private.",
        ),
        source(
            ARMY,
            "https://catalog.archives.gov/id/1263923",
            "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "National Archives and Records Administration",
            "A_direct_official",
            "Official unrestricted ASNEF.FIN.DAT; eight Batch 957 candidates reviewed; private identifiers withheld",
            creator="Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            date="1938-1946; merged file created 2002",
            archival_id="National Archives Identifier 1263923; parent series NAID 604357",
            collection="World War II Army Enlistment Records",
            document="ASNEF.FIN.DAT",
            rights="Eight reviewed identity leads were accepted. No raw bulk row, response payload or full protected identifier enters public assets.",
        ),
        source(
            TECH,
            "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf",
            "World War II Army Enlistment Records: Reference Copy of Technical Documentation",
            "National Archives at College Park - Electronic Records",
            "A_direct_official",
            "PDF physical pages 44-46; name, identifier, DD/MM/YY Army-entry-date and occupation fields",
            creator="National Archives and Records Administration",
            date="1994-2005; reference copy modified 2011",
            archival_id="NN3-064-03-008; National Archives Identifier 1263923",
            collection="World War II Army Enlistment Records technical documentation",
        ),
        source(
            CODES,
            "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1CL_SD.pdf",
            "NARA Compiled Code Lists for the Electronic Army Serial Number Merged File",
            "National Archives at College Park - Electronic Records",
            "A_direct_official",
            "PDF physical pages 170-172 and amended page 304; eight reviewed historical categories",
            creator="National Archives and Records Administration",
            date="2011-01-12; modified 2011-03-17",
            archival_id="National Archives Identifier 1263923; Code No. 30",
            collection="World War II Army Enlistment Records technical documentation",
            rights="Historical categories are qualified and never converted into named employers, workplaces, institutions or exact modern job titles.",
        ),
        source(
            GREECE,
            "https://dokumen.pub/after-the-battle-behind-the-scenes-with-the-oss-in-greece-186.html",
            "Behind the Lines with the OSS in Greece",
            "After the Battle, no. 186",
            "C_reputable_contemporary_or_scholarly",
            "Issue pages 5, 10 and 24; George S. Tiniakos biography and Operational Group II roster",
            creator="Robert E. Perdue, Jr.; edited by Karel Margry",
            date="2019",
            collection="After the Battle, number 186",
            rights="Only short excerpts and project-authored paraphrases are retained; the full copyrighted issue is not republished.",
        ),
        source(
            GREEK_MEMORIAL,
            "https://www.uswarmemorials.org/html/monument_details.php?MemID=1865&SiteID=1414&file=monument_details.php&page=4",
            "Greek Operational Group (OSS) Soldier Monument",
            "American War Memorials Overseas, Inc.",
            "B_authoritative_institutional",
            "Monument history and plaque roster naming George S. Tiniakos",
            date="monument dedicated 2005-05-26",
            collection="Athens Hellenic Army ALSOS Park memorial database",
        ),
        source(
            STANFORD,
            "https://ageconsearch.umn.edu/record/136771/files/fris-1965-05-03-383.pdf",
            "Memorial Resolution: Vladimir P. Timoshenko, 1885-1965",
            "Stanford University Food Research Institute; AgEcon Search",
            "B_authoritative_institutional",
            "PDF physical pages 1-2; permanent Stanford staff and wartime OSS consultant chronology",
            creator="Joseph S. Davis; Edward S. Shaw; Helen C. Farnsworth",
            date="1965",
            collection="Food Research Institute Studies memorial resolutions",
        ),
        source(
            BROADCASTING,
            "https://www.worldradiohistory.com/Archive-BC/BC-1943/1943-09-27-BC.pdf",
            "Tinney to Army",
            "Broadcasting and Broadcast Advertising; World Radio History",
            "C_reputable_contemporary_or_scholarly",
            "PDF physical page 45; September 27, 1943 industry notice",
            creator="Broadcasting Publications, Inc.",
            date="1943-09-27",
            collection="Broadcasting and Broadcast Advertising",
            rights="A short excerpt and paraphrase support the dated Mutual-to-Army transition; the full issue is not republished.",
        ),
        source(
            MBC_TISCH,
            "https://www.museum.tv/tv-encyclopedia-17/tisch-laurence",
            "Laurence Tisch",
            "Museum of Broadcast Communications",
            "B_authoritative_institutional",
            "Biographical header and first paragraph; education and U.S. Army OSS service",
            date="accessed 2026-10-29",
            collection="Museum of Broadcast Communications Encyclopedia of Television",
        ),
        source(
            ANU_TITIEV,
            "https://openresearch-repository.anu.edu.au/bitstreams/97d1413e-cddf-4d92-b5cd-e1bd6a8de5f9/download",
            "George Ernest Morrison Lecture introduction for Mischa Titiev",
            "Australian National University Open Research Repository",
            "B_authoritative_institutional",
            "Biographical introduction; 1942 University of Michigan ASTP appointment and following-year OSS entry",
            creator="Australian National University",
            date="1954",
            collection="George Ernest Morrison Lectures in Ethnology",
        ),
        source(
            UM_TITIEV,
            "https://quod.lib.umich.edu/cgi/p/pod/dod-idx/anthropology.pdf?c=bicentennial%3Bidno%3D13950886.0002.006%3Bformat%3Dpdf",
            "Anthropology: The University of Michigan, An Encyclopedic Survey",
            "Regents of the University of Michigan",
            "B_authoritative_institutional",
            "PDF physical pages 8 and 11; 1935 appointment and prewar faculty chronology",
            creator="Carl E. Guthe and later departmental historians",
            date="1942; 1975; compiled 2015",
            collection="University of Michigan Bicentennial Encyclopedic Survey",
        ),
        source(
            MOMA_TITUS,
            "https://www.moma.org/docs/press_archives/5442/releases/MOMA_1976_0102_89a.pdf",
            "Biographical Notes - Roy and Niuta Titus",
            "Museum of Modern Art",
            "B_authoritative_institutional",
            "PDF physical page 1; Helena Rubinstein chronology and wartime OSS exception",
            creator="Museum of Modern Art",
            date="1976-10",
            document="No. 89A",
            collection="Museum of Modern Art press archives",
        ),
        source(
            WSU_TJERANDSEN,
            "https://content.libraries.wsu.edu/digital/api/collection/powwows/id/15090/download",
            "Washington State University Hilltopics, October-November 1982",
            "Washington State University Libraries",
            "B_authoritative_institutional",
            "PDF page 18; Carl Tjerandsen chronology, 1934-1945",
            creator="Washington State University Alumni Association",
            date="1982-10/11",
            collection="Washington State University alumni publications",
        ),
        source(
            LEGACY_TJERANDSEN,
            "https://www.legacy.com/us/obituaries/montereyherald/name/carl-tjerandsen-obituary?id=26814556",
            "Carl Tjerandsen Obituary",
            "Monterey Herald via Legacy.com",
            "C_reputable_contemporary_or_scholarly",
            "Obituary paragraphs 1-3; education, University of Idaho and OSS officer service",
            date="2005-03-23",
        ),
        source(
            UTAH_TOBARI,
            "https://attheu.utah.edu/arts-humanities/saving-the-legacy-honoring-veterans-through-oral-histories/",
            "Saving the Legacy: Honoring veterans through oral histories",
            "University of Utah J. Willard Marriott Library",
            "B_authoritative_institutional",
            "Joseph 'Joe' Tobari section; Salt Lake City origin, 1943 enlistment and 442nd RCT service",
            creator="Duston Mazzella, Special Collections",
            date="2025-11-05",
            collection="Saving the Legacy Oral Histories Collection A0864",
        ),
        source(
            BERKELEY_TOBARI,
            "https://digicoll.lib.berkeley.edu/record/176281/files/cubanc_35_1_00263103ta.pdf",
            "Wartime Japanese American student record naming Joseph Mamoru Tobari",
            "University of California, Berkeley, Bancroft Library Digital Collections",
            "B_authoritative_institutional",
            "Digitized record entry: Joseph Mamoru Tobari — University of Utah",
            date="ca. 1942-1943",
            collection="Japanese American student relocation records",
        ),
        source(
            SMITHSONIAN_TOBIAS,
            "https://sirismm.si.edu/EADpdfs/AAA.tobijoel.pdf",
            "A Finding Aid to the Abraham Joel Tobias Papers, 1913-2000",
            "Archives of American Art, Smithsonian Institution",
            "A_direct_official",
            "PDF physical pages 3-4 and 6; biographical note and wartime records",
            creator="Carla De Luise",
            date="2006-11-30",
            archival_id="AAA.tobijoel",
            collection="Abraham Joel Tobias papers, 1913-2000",
        ),
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": US_ARMY,
            "organization_id": "28a26f92-78af-5a1a-9c09-a843eb5975b4",
            "canonical_name": "United States Army",
            "historical_name": "Army of the United States",
            "aliases": ["U.S. Army", "Army"],
            "organization_type": "military service",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "Existing heavily linked canonical organization reused.",
        },
        {
            "key": STANFORD_ORG,
            "organization_id": "63b7b9f4-ee2a-51b3-b83a-d483901bdc38",
            "canonical_name": "Stanford University",
            "historical_name": "Food Research Institute, Stanford University",
            "aliases": ["Stanford Food Research Institute", "Food Research Institute"],
            "organization_type": "university and research institute",
            "sector": "academia_and_research",
            "city": "Stanford",
            "state_or_region": "California",
            "country": "United States",
            "active_dates": "Food Research Institute at Stanford, 1921-1996",
            "normalization_notes": "The historical Food Research Institute unit is preserved in the as-found field; no modern unit equivalence is asserted.",
        },
        {
            "key": MUTUAL_ORG,
            "organization_id": "9dce34b6-35f0-5686-b3e8-847601bf60fd",
            "canonical_name": "Mutual Broadcasting System",
            "historical_name": "Mutual Broadcasting System",
            "aliases": ["Mutual", "MBS"],
            "organization_type": "radio network",
            "sector": "journalism_and_media",
            "city": "New York",
            "state_or_region": "New York",
            "country": "United States",
            "active_dates": "1934-1999",
            "normalization_notes": "Existing canonical organization reused; the historical network name is retained.",
        },
        {
            "key": NYU_ORG,
            "organization_id": "54f70fa3-cf82-5149-84fb-72372b2e348a",
            "canonical_name": "New York University",
            "historical_name": "New York University",
            "aliases": ["NYU"],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "New York",
            "state_or_region": "New York",
            "country": "United States",
            "normalization_notes": "Existing canonical organization reused; student status is not counted as employment.",
        },
        {
            "key": UMICH_ORG,
            "organization_id": "4ee8a858-3cd1-5a2d-94a7-0d3c7a3fdb3a",
            "canonical_name": "University of Michigan",
            "historical_name": "University of Michigan",
            "aliases": ["U-M", "Michigan"],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "Ann Arbor",
            "state_or_region": "Michigan",
            "country": "United States",
            "normalization_notes": "Existing heavily linked canonical organization reused.",
        },
        {
            "key": HELENA_ORG,
            "canonical_name": "Helena Rubinstein Inc.",
            "historical_name": "Helena Rubinstein Inc.",
            "aliases": ["Helena Rubinstein", "British affiliate of Helena Rubinstein Inc."],
            "organization_type": "cosmetics company",
            "sector": "business_and_industry",
            "city": "New York",
            "state_or_region": "New York",
            "country": "United States",
            "normalization_notes": "The 1976 institutional biography names both the British affiliate and American company; no modern owner is substituted.",
        },
        {
            "key": UTAH_ORG,
            "canonical_name": "University of Utah",
            "historical_name": "University of Utah",
            "aliases": ["the U"],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "Salt Lake City",
            "state_or_region": "Utah",
            "country": "United States",
            "normalization_notes": "Student affiliation remains separate from employment analytics.",
        },
        {
            "key": USAAF_ORG,
            "organization_id": "75a3a185-5c26-548b-8be6-9bcdf51bc4eb",
            "canonical_name": "United States Army Air Forces",
            "historical_name": "Intelligence Division, Army Air Force",
            "aliases": ["Army Air Forces", "AAF"],
            "organization_type": "military air service",
            "sector": "military",
            "country": "United States",
            "active_dates": "1941-1947",
            "normalization_notes": "Existing canonical organization reused; the finding aid's singular historical wording is preserved as found.",
        },
        {
            "key": FAP_ORG,
            "organization_id": "9cd8468b-fd4f-5e10-a70c-6a83d42560fd",
            "canonical_name": "Federal Art Project",
            "historical_name": "Federal Arts Project",
            "aliases": ["WPA Federal Art Project", "Federal Arts Project"],
            "organization_type": "federal arts employment program",
            "sector": "federal_government",
            "country": "United States",
            "active_dates": "1935-1943",
            "normalization_notes": "Existing canonical organization reused; Smithsonian's plural wording is preserved in the affiliation.",
        },
        {
            "key": IDAHO_ORG,
            "canonical_name": "University of Idaho",
            "historical_name": "University of Idaho",
            "aliases": [],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "Moscow",
            "state_or_region": "Idaho",
            "country": "United States",
            "normalization_notes": "Named historical employer; later institutions are not conflated with it.",
        },
        {
            "key": GREEK_MARINE_ORG,
            "canonical_name": "Greek Merchant Marine",
            "historical_name": "Greek merchant marine",
            "aliases": ["Greek merchant navy"],
            "organization_type": "national merchant shipping service",
            "sector": "business_and_industry",
            "country": "Greece",
            "normalization_notes": "A broad professional affiliation, not a named shipowner or employer; no company is inferred.",
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
    status: str,
    *,
    organization_key: str | None = None,
    organization_name: str | None = None,
    role: str | None = None,
    occupation: str | None = None,
    start: str | None = None,
    end: str | None = None,
    precision: str | None = None,
    city: str | None = None,
    state: str | None = None,
    country: str | None = None,
    immediate: bool = False,
    last_civilian: bool = False,
    notes: str | None = None,
) -> dict[str, object]:
    return {
        "key": key,
        "person_id": PEOPLE[row][0],
        "organization_key": organization_key,
        "organization_name_as_found": organization_name,
        "role_title": role,
        "occupation": occupation,
        "relationship_type": relationship,
        "start_date": start,
        "end_date": end,
        "date_precision": precision,
        "city": city,
        "state_or_region": state,
        "country": country,
        "immediate_pre_oss": immediate,
        "last_civilian_pre_service": last_civilian,
        "pre_oss_temporal_basis": temporal,
        "identity_confidence": identity,
        "claim_confidence": confidence,
        "source_quality": quality,
        "publication_status": status,
        "research_notes": notes,
    }


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (entry_date, category, code, _page, relationship, identity) in ARMY_CATEGORIES.items():
        values.append(
            affiliation(
                f"army-category-row{row}-b957",
                row,
                relationship,
                "strongly_date_bounded",
                identity,
                "medium",
                "A_direct_official",
                "publish_qualified",
                occupation=category.lower(),
                end=entry_date,
                country="United States",
                precision=f"Historical category {code} at Army entry on {entry_date}; no employer, workplace, school or OSS-transfer date is named.",
                notes="Published only as a qualified historical category; it is not converted into a named employer or exact modern occupation.",
            )
        )

    values.extend(
        [
            affiliation(
                "greek-merchant-marine-george-tiniakos-b957", 1, "professional_affiliation", "strongly_date_bounded", "high_confidence", "high", "C_reputable_contemporary_or_scholarly", "published",
                organization_key=GREEK_MARINE_ORG, organization_name="Greek merchant marine", role="merchant seaman", occupation="merchant mariner", start="1929", end="1943-01", country="Greece / international",
                precision="Joined at about age 15, returned after Greek Army service, and left ship in Boston before entering U.S. military service in January 1943.",
                notes="The source names a maritime service, not a ship, shipping line or employer; no company is inferred.",
            ),
            affiliation(
                "us-army-george-tiniakos-b957", 1, "military_assignment", "probable_immediate", "high_confidence", "medium", "C_reputable_contemporary_or_scholarly", "publish_qualified",
                organization_key=US_ARMY, organization_name="U.S. military service / Greek Battalion", role="enlisted soldier; later Technician Fifth Grade", occupation="soldier", start="1943-01", end="1944", country="United States / Greece", immediate=True,
                precision="Entered U.S. military service in January 1943 and later served in OSS Operational Group II; the exact transfer date is not stated.",
                notes="Published as the best-supported broad military pathway, not a specific immediately preceding unit on a known date.",
            ),
            affiliation(
                "stanford-timoshenko-b957", 2, "employment", "strongly_date_bounded", "high_confidence", "high", "B_authoritative_institutional", "published",
                organization_key=STANFORD_ORG, organization_name="Food Research Institute, Stanford University", role="professor of commodity economics; senior staff", occupation="economist", start="1936", end="1950", city="Stanford", state="California", country="United States", immediate=True, last_civilian=True,
                precision="Permanent senior staff from 1936; served for a time during World War II as an OSS consultant; became emeritus in 1950.",
                notes="Stanford was his continuing home institution while he consulted for OSS; this is not described as a resignation-and-transfer sequence.",
            ),
            affiliation(
                "mutual-calvin-tinney-b957", 5, "employment", "explicit_immediate", "confirmed", "high", "C_reputable_contemporary_or_scholarly", "published",
                organization_key=MUTUAL_ORG, organization_name="Mutual network", role="radio news commentator", occupation="author, editor, reporter and broadcaster", start="1941-08", end="1943-09-27", city="New York", state="New York", country="United States", immediate=True, last_civilian=True,
                precision="A September 27, 1943 industry notice says he had until recently broadcast for Mutual and reported for active Army duty that day.",
                notes="The dated contemporary transition supports Mutual as the immediate and last documented civilian employer before Army service.",
            ),
            affiliation(
                "nyu-laurence-tisch-b957", 11, "student", "strongly_date_bounded", "high_confidence", "high", "B_authoritative_institutional", "published",
                organization_key=NYU_ORG, organization_name="New York University", role="student", occupation="student", end="1942", city="New York", state="New York", country="United States", immediate=True,
                precision="B.S. awarded in 1942; official Army entry record categorized him as a student on 1942-12-10.",
                notes="Student status is an institutional affiliation, not employment. Graduate study in 1943 is noted in the source but is not forced into the pre-entry sequence.",
            ),
            affiliation(
                "umich-mischa-titiev-b957", 14, "employment", "explicit_immediate", "high_confidence", "high", "B_authoritative_institutional", "published",
                organization_key=UMICH_ORG, organization_name="University of Michigan", role="anthropology faculty; Supervisor, Army Specialized Training Program for the Far East", occupation="anthropologist and educator", start="1936", end="1943", city="Ann Arbor", state="Michigan", country="United States", immediate=True, last_civilian=True,
                precision="University faculty from 1936; appointed ASTP supervisor in 1942; an ANU biographical introduction says he joined OSS during the following year.",
                notes="The source explicitly orders the University appointment, 1942 ASTP role and following-year OSS entry.",
            ),
            affiliation(
                "helena-rubinstein-roy-titus-b957", 17, "employment", "explicit_immediate", "confirmed", "confirmed", "B_authoritative_institutional", "published",
                organization_key=HELENA_ORG, organization_name="Helena Rubinstein Inc.", role="business employee", occupation="business manager", end="1942", city="New York", state="New York", country="United States", immediate=True, last_civilian=True,
                precision="The MoMA biography says his company career was continuous except for wartime OSS service; the exact OSS entry date and prewar title are not supplied.",
                notes="Later executive titles are not projected backward onto the pre-OSS period.",
            ),
            affiliation(
                "university-idaho-carl-tjerandsen-b957", 19, "employment", "documented_prewar", "high_confidence", "high", "B_authoritative_institutional", "published",
                organization_key=IDAHO_ORG, organization_name="University of Idaho", role="assistant professor of business", occupation="educator", start="1934", end="1935", city="Moscow", state="Idaho", country="United States",
                precision="Washington State University alumni chronology dates the appointment to 1934-1935.",
                notes="Documented earlier employment; not presented as the immediate OSS predecessor.",
            ),
            affiliation(
                "federal-land-use-carl-tjerandsen-b957", 19, "government_assignment", "documented_prewar", "high_confidence", "high", "B_authoritative_institutional", "publish_qualified",
                organization_name="federal land-use planning (agency not identified)", role="land-use planner", occupation="planner", start="1935", end="1942", country="United States",
                precision="The WSU chronology dates federal land-use planning work to 1935-1942 but does not name an agency.",
                notes="No department, bureau or employer is invented from the broad federal description.",
            ),
            affiliation(
                "food-research-carl-tjerandsen-b957", 19, "professional_affiliation", "explicit_immediate", "high_confidence", "high", "B_authoritative_institutional", "publish_qualified",
                organization_name="food and agriculture research (institution not identified)", role="researcher", occupation="food and agriculture researcher", start="1942", end="1944", country="United States", immediate=True,
                precision="The WSU chronology places food and agriculture research in 1942-1944 directly before 1944-1945 U.S. Army OSS service.",
                notes="This is the immediate documented activity, but the source does not name an employer or sponsoring institution.",
            ),
            affiliation(
                "university-utah-joseph-tobari-b957", 21, "student", "strongly_date_bounded", "confirmed", "high", "B_authoritative_institutional", "published",
                organization_key=UTAH_ORG, organization_name="University of Utah", role="student", occupation="student", end="1943-05-05", city="Salt Lake City", state="Utah", country="United States", immediate=True,
                precision="A wartime institutional record connects Joseph Mamoru Tobari to the University of Utah; the Army record labels him a student at entry on 1943-05-05.",
                notes="Student status is not classified as employment and is excluded from employer analytics.",
            ),
            affiliation(
                "usaaf-abraham-tobias-b957", 22, "military_assignment", "explicit_immediate", "high_confidence", "high", "A_direct_official", "published",
                organization_key=USAAF_ORG, organization_name="Intelligence Division, Army Air Force", role="art director", occupation="art director and graphic designer", end="1945", country="United States", immediate=True,
                precision="The Smithsonian finding aid places the Army Air Force intelligence art-director role before employment as an OSS graphic designer in 1945.",
                notes="Published as the immediate documented military assignment, not as a civilian employer.",
            ),
            affiliation(
                "fap-abraham-tobias-b957", 22, "government_assignment", "documented_prewar", "high_confidence", "high", "A_direct_official", "published",
                organization_key=FAP_ORG, organization_name="Federal Arts Project", role="muralist", occupation="artist and muralist", start="1938", end="1940", city="New York", state="New York", country="United States",
                precision="The Smithsonian finding aid dates Federal Arts Project work to 1938-1940.",
                notes="Documented earlier government arts work; the reviewed source does not establish it as the last civilian employer before wartime service.",
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
    status: str,
    notes: str,
    source_links: list[dict[str, str]],
    *,
    affiliation_key: str | None = None,
    excerpt: str | None = None,
) -> dict[str, object]:
    return {
        "key": key,
        "person_id": PEOPLE[row][0],
        "affiliation_key": affiliation_key,
        "claim_type": claim_type,
        "claim_text": text,
        "evidence_excerpt": excerpt,
        "evidence_paraphrase": paraphrase,
        "identity_match_assessment": identity,
        "temporal_assessment": temporal,
        "source_quality": quality,
        "claim_confidence": confidence,
        "publication_status": status,
        "match_notes": notes,
        "sources": source_links,
    }


def army_claims() -> list[dict[str, object]]:
    context_sources = {
        1: [{"source_key": GREECE, "locator_override": "Issue page 5 biography and page 10 roster naming George S. Tiniakos"}],
        5: [{"source_key": BROADCASTING, "locator_override": "PDF page 45, Tinney to Army"}],
        11: [{"source_key": MBC_TISCH, "locator_override": "Biographical header, education and Army OSS line"}],
        17: [{"source_key": MOMA_TITUS, "locator_override": "PDF page 1, exact Roy V. Titus chronology"}],
        19: [{"source_key": WSU_TJERANDSEN, "locator_override": "PDF page 18, 1934-1945 chronology"}],
        21: [{"source_key": UTAH_TOBARI, "locator_override": "Joseph 'Joe' Tobari section"}],
    }
    values: list[dict[str, object]] = []
    for row, (entry_date, category, code, page, _relationship, identity_confidence) in ARMY_CATEGORIES.items():
        person_id, name = PEOPLE[row]
        exact = row not in {1, 11, 19}
        confidence = "confirmed" if exact else "high"
        assessment = (
            "Confirmed from exact compatible name and private nonshared identifier agreement, with independent biographical corroboration where available."
            if exact
            else "High confidence from private nonshared identifier agreement, a transparent spelling difference, and independent distinctive-name wartime evidence."
        )
        links = [
            {"source_key": INDEX, "locator_override": f"PDF page 469 row {row}; Box {archive_box(row)}; private identifier withheld"},
            {"source_key": ARMY, "locator_override": "Reviewed name record; private identifier withheld"},
            *context_sources.get(row, []),
        ]
        values.append(
            claim(
                f"identity-row{row}-army-b957", row, "identity",
                f"The indexed {name} is a {identity_confidence.replace('_', ' ')} match to the reviewed official Army record.",
                "A private nonshared identifier connects the visually verified index row to the Army record; independent sources corroborate distinctive spelling variants where needed.",
                assessment,
                "The Army record dates entry into service but does not by itself establish the OSS transfer date.",
                "A_direct_official", confidence, "published",
                "The identity decision does not by itself establish a named employer or immediate OSS predecessor; private identifiers remain withheld.",
                links,
            )
        )
        values.append(
            claim(
                f"category-row{row}-army-b957", row, "occupation",
                f"At Army entry on {entry_date}, {name} was recorded in the historical {category} category; no employer, workplace or institution is identified.",
                f"The official bulk record supplies historical code {code}; the inspected NARA code list expands it as {category}.",
                assessment,
                "Strongly date-bounded at Army entry, but not proof of the immediate pre-OSS affiliation.",
                "A_direct_official", "medium", "publish_qualified",
                "Published only as a qualified historical category; no employer, school, workplace or exact modern specialization is inferred.",
                [
                    {"source_key": ARMY, "locator_override": f"Army entry {entry_date}; historical code {code}; private identifier withheld"},
                    {"source_key": CODES, "locator_override": f"PDF physical page {page}; historical category {code}"},
                    {"source_key": TECH, "support_type": "context_only", "locator_override": "Field definitions and DD/MM/YY date format, PDF pages 44-46"},
                ],
                affiliation_key=f"army-category-row{row}-b957",
                excerpt=category,
            )
        )
    return values


def claims() -> list[dict[str, object]]:
    values = army_claims()
    values.extend(
        [
            claim(
                "merchant-marine-george-tiniakos-b957", 1, "other_pre_oss_affiliation",
                "George S. Tiniakos served in the Greek merchant marine before U.S. military service; no shipowner or company is identified.",
                "A detailed scholarly history says he joined the Greek merchant marine at 15, returned after Greek Army duty, and left ship in Boston before U.S. enlistment.",
                "High confidence from the index-private-identifier bridge, rare Tiniakos/Tinlakos variant, middle initial and exact OSS operational-group context.",
                "Strongly date-bounded before U.S. military entry in January 1943, with an intervening Greek Army period in 1938-1940.",
                "C_reputable_contemporary_or_scholarly", "high", "published",
                "The broad merchant-marine affiliation is published; a ship, shipping line and employer remain unknown.",
                [{"source_key": GREECE, "locator_override": "Issue page 5, George Tiniakos biography"}],
                affiliation_key="greek-merchant-marine-george-tiniakos-b957",
                excerpt="had joined the Greek merchant marine at age 15",
            ),
            claim(
                "army-path-george-tiniakos-b957", 1, "immediate_pre_oss_affiliation",
                "The U.S. Army is George S. Tiniakos's best-supported broad immediate pathway into OSS Operational Group II; the precise transfer date remains unknown.",
                "The source dates U.S. military entry to January 1943 and later lists him as Technician Fifth Grade in OSS Operational Group II.",
                "High confidence from private identifier agreement, distinctive spelling variant and an exact OSS roster.",
                "Probable immediate at the broad service level; the specific unit immediately before OSS and transfer date are not stated.",
                "C_reputable_contemporary_or_scholarly", "medium", "publish_qualified",
                "Excluded from civilian-employer analytics and shown with an uncertainty warning.",
                [
                    {"source_key": GREECE, "locator_override": "Issue pages 5 and 10"},
                    {"source_key": GREEK_MEMORIAL, "support_type": "context_only", "locator_override": "Plaque roster and unit history"},
                ],
                affiliation_key="us-army-george-tiniakos-b957",
            ),
            claim(
                "identity-vladimir-timoshenko-b957", 2, "identity",
                "The indexed Vladimir Tinmoshenko is a high-confidence match to Stanford economist and OSS consultant Vladimir P. Timoshenko; both spellings remain visible.",
                "Stanford's memorial resolution identifies the rare name, academic specialty, permanent Food Research Institute appointment and wartime OSS consultancy.",
                "High confidence from the rare near-exact surname, exact given name, authoritative OSS chronology and compatible box context; the printed extra 'n' is not silently corrected.",
                "The memorial dates permanent Stanford staff from 1936 and service for a time as an OSS consultant during World War II.",
                "B_authoritative_institutional", "high", "published",
                "The normalized variant is published alongside, not instead of, the printed Tinmoshenko form.",
                [
                    {"source_key": INDEX, "locator_override": "PDF page 469 row 2; Box 778; printed Tinmoshenko spelling"},
                    {"source_key": STANFORD, "locator_override": "PDF pages 1-2; permanent staff and OSS consultancy"},
                ],
                excerpt="During World War II Professor Timoshenko served for a time in Washington as consultant",
            ),
            claim(
                "stanford-immediate-vladimir-timoshenko-b957", 2, "immediate_pre_oss_affiliation",
                "Stanford University's Food Research Institute was Vladimir P. Timoshenko's continuing home institution when he served as an OSS consultant during World War II.",
                "The Stanford memorial says he was permanent senior staff from 1936 and separately notes wartime OSS consulting service.",
                "High confidence from the distinctive name, specialization and authoritative institutional chronology.",
                "Strongly date-bounded and concurrent; the source does not describe a resignation or exclusive transfer to OSS.",
                "B_authoritative_institutional", "high", "published",
                "Displayed as a continuing academic affiliation and employer, with the concurrent-consultant relationship made explicit.",
                [{"source_key": STANFORD, "locator_override": "PDF pages 1-2"}],
                affiliation_key="stanford-timoshenko-b957",
                excerpt="was on its permanent senior staff from 1936",
            ),
            claim(
                "stanford-last-civilian-vladimir-timoshenko-b957", 2, "last_civilian_pre_service",
                "Stanford University's Food Research Institute is the last documented civilian employer connected to Vladimir P. Timoshenko's wartime OSS consultancy.",
                "Permanent senior-staff status beginning in 1936 continued across the wartime consultancy described in the same institutional memorial.",
                "High confidence from the rare name and authoritative Stanford resolution.",
                "The source supports continuity but does not supply an OSS start date or say he left Stanford.",
                "B_authoritative_institutional", "high", "publish_qualified",
                "Counted as the last documented civilian employer, not as proof of a discrete transfer date.",
                [{"source_key": STANFORD, "locator_override": "PDF pages 1-2"}],
                affiliation_key="stanford-timoshenko-b957",
            ),
            claim(
                "mutual-immediate-calvin-tinney-b957", 5, "immediate_pre_oss_affiliation",
                "Immediately before Army duty in September 1943, Calvin L. 'Cal' Tinney was a radio news commentator for the Mutual Broadcasting System.",
                "A contemporary industry notice says he had until recently broadcast commentaries for Mutual and reported for active duty on September 27.",
                "Confirmed by exact private identifier and name agreement, the Cal/Calvin variant, and a dated contemporary transition notice.",
                "Explicit immediate transition from Mutual broadcasting to active Army duty on 1943-09-27.",
                "C_reputable_contemporary_or_scholarly", "high", "published",
                "Published as named civilian employment immediately before Army service; the later OSS transfer date remains unknown.",
                [{"source_key": BROADCASTING, "locator_override": "PDF physical page 45, Tinney to Army"}],
                affiliation_key="mutual-calvin-tinney-b957",
                excerpt="until recently broadcasting his ... commentaries ... over Mutual network",
            ),
            claim(
                "mutual-last-civilian-calvin-tinney-b957", 5, "last_civilian_pre_service",
                "Mutual Broadcasting System is Calvin L. Tinney's last documented civilian employer before active Army duty.",
                "The same September 1943 notice explicitly places his Mutual broadcasting immediately before active duty.",
                "Confirmed by private identifier, exact indexed name and contemporary chronology.",
                "Explicitly ordered in a point-in-time industry notice.",
                "C_reputable_contemporary_or_scholarly", "high", "published",
                "Counted in last-civilian-employer analytics; no later pre-OSS civilian employer is inferred.",
                [{"source_key": BROADCASTING, "locator_override": "PDF physical page 45"}],
                affiliation_key="mutual-calvin-tinney-b957",
            ),
            claim(
                "student-laurence-tisch-b957", 11, "immediate_pre_oss_affiliation",
                "Laurence A. Tisch completed a New York University degree in 1942 and was recorded as a student at Army entry on December 10, 1942.",
                "The Museum of Broadcast Communications dates his NYU B.S. to 1942; the official Army record labels him a student at entry.",
                "High confidence from private identifier agreement, distinctive full name, transparent Laurence/Lawrence conflict and independent Army OSS biography.",
                "Strongly date-bounded before Army OSS service, while 1943 graduate study makes the precise wartime sequence non-linear.",
                "B_authoritative_institutional", "high", "publish_qualified",
                "Student status is published as an institutional affiliation, not as employment by NYU.",
                [
                    {"source_key": MBC_TISCH, "locator_override": "Biographical header and education line"},
                    {"source_key": ARMY, "locator_override": "Army entry 1942-12-10; historical student code; private identifier withheld"},
                ],
                affiliation_key="nyu-laurence-tisch-b957",
            ),
            claim(
                "identity-mischa-titiev-b957", 14, "identity",
                "The indexed Mischa Titiev is confirmed as the University of Michigan anthropologist who joined the OSS in 1943.",
                "ANU and University of Michigan institutional histories supply the exact distinctive name, faculty chronology, 1942 ASTP role and following-year OSS entry.",
                "Confirmed by exact rare name and two authoritative institutional chronologies explicitly identifying University of Michigan and OSS service.",
                "The sources order faculty service, the 1942 ASTP appointment and the following-year OSS entry.",
                "B_authoritative_institutional", "confirmed", "published",
                "No famous-name assignment rests on name alone; the institutional chronology supplies the bridge.",
                [
                    {"source_key": INDEX, "locator_override": "PDF page 469 row 14; Box 779"},
                    {"source_key": ANU_TITIEV, "locator_override": "Biographical introduction"},
                    {"source_key": UM_TITIEV, "support_type": "context_only", "locator_override": "PDF pages 8 and 11"},
                ],
            ),
            claim(
                "umich-immediate-mischa-titiev-b957", 14, "immediate_pre_oss_affiliation",
                "Mischa Titiev's immediate documented pre-OSS affiliation was the University of Michigan, where he supervised the Far East Army Specialized Training Program in 1942.",
                "The ANU biography says he joined Michigan's faculty, received the ASTP appointment in 1942, and joined OSS during the following year.",
                "Confirmed identity from exact rare name and explicit institutional OSS chronology.",
                "Explicit immediate sequence: 1942 ASTP supervisor at Michigan, then OSS during the following year.",
                "B_authoritative_institutional", "high", "published",
                "The Army-sponsored program role is shown within his continuing University employment; it is not mislabeled as a separate private employer.",
                [{"source_key": ANU_TITIEV, "locator_override": "Biographical introduction"}],
                affiliation_key="umich-mischa-titiev-b957",
                excerpt="During the following year he joined the Office of Strategic Services",
            ),
            claim(
                "umich-last-civilian-mischa-titiev-b957", 14, "last_civilian_pre_service",
                "The University of Michigan is Mischa Titiev's last documented civilian employer before OSS service.",
                "Institutional histories place him on Michigan's anthropology faculty from 1936 and order his 1942 ASTP role before the following-year OSS entry.",
                "Confirmed identity from exact name and matching university/OSS chronology.",
                "Explicitly date-bounded immediately before OSS entry in 1943.",
                "B_authoritative_institutional", "high", "published",
                "Counted in civilian-employer analytics; the ASTP assignment is described separately within the same affiliation.",
                [
                    {"source_key": ANU_TITIEV, "locator_override": "Biographical introduction"},
                    {"source_key": UM_TITIEV, "locator_override": "PDF pages 8 and 11"},
                ],
                affiliation_key="umich-mischa-titiev-b957",
            ),
            claim(
                "helena-immediate-roy-titus-b957", 17, "immediate_pre_oss_affiliation",
                "Roy V. Titus worked for Helena Rubinstein Inc. immediately before and after his wartime OSS service.",
                "A Museum of Modern Art biography says his company career continued without interruption except for wartime OSS service.",
                "Confirmed by private identifier agreement, exact surname and authoritative Roy V. Titus OSS chronology.",
                "Explicit immediate relationship; the biography identifies OSS as the sole exception to his company career.",
                "B_authoritative_institutional", "confirmed", "published",
                "The prewar role is kept broad because later executive titles are not projected backward.",
                [{"source_key": MOMA_TITUS, "locator_override": "PDF physical page 1, lines 10-18"}],
                affiliation_key="helena-rubinstein-roy-titus-b957",
                excerpt="Except for his service in the Office of Strategic Services during World War II",
            ),
            claim(
                "helena-last-civilian-roy-titus-b957", 17, "last_civilian_pre_service",
                "Helena Rubinstein Inc. is Roy V. Titus's last documented civilian employer before OSS service.",
                "The institutional biography presents continuous company service with OSS as the wartime exception.",
                "Confirmed by exact private identifier and specific institutional biography.",
                "Explicitly immediate but without a precise OSS entry date.",
                "B_authoritative_institutional", "confirmed", "published",
                "Counted in last-civilian-employer analytics with the historical company name preserved.",
                [{"source_key": MOMA_TITUS, "locator_override": "PDF physical page 1"}],
                affiliation_key="helena-rubinstein-roy-titus-b957",
            ),
            claim(
                "university-idaho-carl-tjerandsen-b957", 19, "other_pre_oss_affiliation",
                "Carl Tjerandsen was an assistant professor of business at the University of Idaho in 1934-1935.",
                "Washington State University's alumni chronology names the employer, role and dates; a published obituary independently names his teaching there.",
                "High confidence for row 19 from private identifier agreement, rare surname, compatible Army chronology and independent institutional biography.",
                "Documented earlier employment, followed by federal planning and food-agriculture research before 1944 Army OSS service.",
                "B_authoritative_institutional", "high", "published",
                "The second distinct index row remains separate; this claim is not duplicated onto it.",
                [
                    {"source_key": WSU_TJERANDSEN, "locator_override": "PDF page 18"},
                    {"source_key": LEGACY_TJERANDSEN, "support_type": "context_only", "locator_override": "Obituary paragraphs 1-3"},
                ],
                affiliation_key="university-idaho-carl-tjerandsen-b957",
            ),
            claim(
                "federal-planning-carl-tjerandsen-b957", 19, "other_pre_oss_affiliation",
                "Carl Tjerandsen worked in federal land-use planning from 1935 to 1942; the reviewed source does not name the agency.",
                "The WSU alumni chronology supplies the field and dates but no department or bureau.",
                "High confidence for row 19 from rare-name and private-identifier evidence.",
                "Documented prewar work between University of Idaho teaching and later food-agriculture research.",
                "B_authoritative_institutional", "high", "publish_qualified",
                "No federal agency is invented; the broad as-found wording remains visible.",
                [{"source_key": WSU_TJERANDSEN, "locator_override": "PDF page 18"}],
                affiliation_key="federal-land-use-carl-tjerandsen-b957",
            ),
            claim(
                "food-research-immediate-carl-tjerandsen-b957", 19, "immediate_pre_oss_affiliation",
                "Carl Tjerandsen's immediate documented pre-OSS activity was food and agriculture research in 1942-1944; the institution is not identified.",
                "The WSU chronology places this research directly before 1944-1945 U.S. Army OSS service.",
                "High confidence for row 19 from private identifier, rare name and compatible chronology; row 20 remains separate.",
                "Explicit chronological adjacency, but no employer or sponsoring institution is named.",
                "B_authoritative_institutional", "high", "publish_qualified",
                "Excluded from named-employer analytics and not copied to the second index row.",
                [{"source_key": WSU_TJERANDSEN, "locator_override": "PDF page 18"}],
                affiliation_key="food-research-carl-tjerandsen-b957",
                excerpt="1942-44, research in food and agriculture; 1944-45, U.S. Army",
            ),
            claim(
                "student-joseph-tobari-b957", 21, "immediate_pre_oss_affiliation",
                "Joseph Mamoru Tobari was affiliated with the University of Utah as a student before entering the Army in 1943.",
                "A wartime student record names Tobari and the University of Utah; the Army record labels him a student at entry, and Utah's oral history confirms 1943 enlistment.",
                "Confirmed by private identifier agreement, exact first and last name, matching middle initial, Utah origin and 442nd service chronology.",
                "Strongly date-bounded at Army entry on 1943-05-05.",
                "B_authoritative_institutional", "high", "published",
                "Student status is not counted as employment; an OSS transfer date remains unverified.",
                [
                    {"source_key": BERKELEY_TOBARI, "locator_override": "Digitized wartime record naming Joseph Mamoru Tobari and University of Utah"},
                    {"source_key": UTAH_TOBARI, "locator_override": "Joseph 'Joe' Tobari section"},
                    {"source_key": ARMY, "locator_override": "Army entry 1943-05-05; historical student code; private identifier withheld"},
                ],
                affiliation_key="university-utah-joseph-tobari-b957",
            ),
            claim(
                "identity-abraham-joel-tobias-b957", 22, "identity",
                "The indexed Abraham J Tobias is a high-confidence match to New York muralist and OSS graphic designer Abraham Joel Tobias.",
                "The Smithsonian finding aid supplies the exact first name, surname, middle initial, wartime armed-forces role and 1945 OSS employment.",
                "High confidence from exact full name and middle initial plus a distinctive art-director and OSS graphic-design chronology.",
                "The finding aid orders Army Air Force intelligence work before OSS employment in 1945.",
                "A_direct_official", "high", "published",
                "The middle name is added as a documented variant; the source-index form remains recoverable.",
                [
                    {"source_key": INDEX, "locator_override": "PDF page 469 row 22; Box 779"},
                    {"source_key": SMITHSONIAN_TOBIAS, "locator_override": "PDF physical pages 3-4"},
                ],
            ),
            claim(
                "usaaf-immediate-abraham-tobias-b957", 22, "immediate_pre_oss_affiliation",
                "Abraham Joel Tobias served as an art director with the Army Air Force Intelligence Division before becoming an OSS graphic designer in 1945.",
                "The Smithsonian biographical note gives both wartime roles in sequence.",
                "High confidence from exact full-name compatibility and a highly specific art-and-intelligence chronology.",
                "Explicit immediate sequence, though exact start and end dates are not supplied.",
                "A_direct_official", "high", "published",
                "Shown as a military assignment, not a civilian employer.",
                [{"source_key": SMITHSONIAN_TOBIAS, "locator_override": "PDF physical page 3, biographical note"}],
                affiliation_key="usaaf-abraham-tobias-b957",
                excerpt="an art director with the Intelligence Division, Army Air Force",
            ),
            claim(
                "fap-abraham-tobias-b957", 22, "other_pre_oss_affiliation",
                "Abraham Joel Tobias worked for the Federal Arts Project as a muralist from 1938 to 1940.",
                "The Smithsonian finding aid dates his Federal Arts Project work and describes his muralist training.",
                "High confidence from exact name, middle initial and specific OSS art-career chronology.",
                "Documented prewar work, but not shown to be the last civilian employer before wartime service.",
                "A_direct_official", "high", "published",
                "Published as earlier employment; no gap-filling claim is made for 1941-1944.",
                [{"source_key": SMITHSONIAN_TOBIAS, "locator_override": "PDF physical page 3"}],
                affiliation_key="fap-abraham-tobias-b957",
                excerpt="He worked for the Federal Arts Project, 1938-1940",
            ),
        ]
    )
    return values


def base_update(row: int, **values: object) -> dict[str, object]:
    return {
        "person_id": PEOPLE[row][0],
        "manual_review_required": True,
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        **values,
    }


def person_updates() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, reason in UNRESOLVED.items():
        values.append(
            base_update(
                row,
                identity_status="ambiguous" if row == 20 else "unresolved",
                identity_evidence=(
                    f"The visually verified index row supplies {PEOPLE[row][1]}, Box {archive_box(row)} and location 230/86/42/02. {reason}"
                ),
                personnel_category="unknown_or_indeterminate",
                possible_duplicate_group="batch957-carl-tjerandsen-page469" if row == 20 else None,
                research_status="requires_archival_review",
                next_action=(
                    "Compare both Carl Tjerandsen personnel files in Box 779 using the distinct private identifiers; do not merge or duplicate biographical claims without direct file evidence."
                    if row == 20
                    else f"Review Box {archive_box(row)} for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed."
                ),
                archival_review_priority="critical" if row in {10, 20} else "high",
            )
        )

    values.extend(
        [
            base_update(1, identity_status="high_confidence", identity_evidence="A private nonshared identifier, rare Tinlakos/Tiniakos spelling variant, middle initial and exact OSS Operational Group II evidence establish a strong bridge without overwriting the printed form.", name_variants=["George S. Tiniakos", "Tech/5 George S. Tiniakos"], personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="completed", next_action="Review Box 779 for the named ship or shipping employer, exact Greek Battalion assignment and OSS transfer date.", archival_review_priority="medium"),
            base_update(2, identity_status="high_confidence", identity_evidence="The rare near-exact name and authoritative Stanford memorial explicitly connect Vladimir P. Timoshenko to the Food Research Institute and wartime OSS consultancy; the printed Tinmoshenko form remains preserved.", name_variants=["Vladimir P. Timoshenko", "Vladimir Timoshenko"], personnel_category="civilian_professional_or_administrative_grade", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="verified_employer_found", next_action="Review Box 778 for the OSS consultancy dates and whether Stanford employment was formally interrupted; current evidence supports a continuing home institution.", archival_review_priority="medium"),
            base_update(5, identity_status="confirmed", identity_evidence="Exact name and private identifier agreement connect the index to the Army record; a contemporary broadcast-industry notice supplies the Cal/Calvin variant and dated Mutual-to-Army transition.", name_variants=["Cal Tinney", "Calvin L. Tinney", "Calvin Lawrence Tinney"], personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="verified_employer_found", next_action="Review Box 779 for the OSS transfer date and assignment; Mutual is already established as the last civilian employer before active Army duty.", archival_review_priority="medium"),
            base_update(6, identity_status="confirmed", identity_evidence="Exact name and a private nonshared identifier connect the visually verified index row to the official Army record.", personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="occupation_only_found", next_action="Review Box 779 to identify the architectural employer or practice and the specific Army-to-OSS pathway; the coded category does not name either.", archival_review_priority="high"),
            base_update(11, identity_status="high_confidence", identity_evidence="A private nonshared identifier, distinctive full name, transparent Laurence/Lawrence spelling conflict and an institutional biography explicitly naming Army OSS service establish a strong identity bridge.", name_variants=["Laurence Alan Tisch", "Lawrence A Tisch"], personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="occupation_only_found", next_action="Review Box 779 to establish the exact sequence among NYU graduation, Army entry, 1943 graduate study and OSS assignment; do not treat student status as employment.", archival_review_priority="high"),
            base_update(14, identity_status="confirmed", identity_evidence="Two authoritative institutional histories identify the exact distinctive name, University of Michigan faculty role, 1942 ASTP appointment and following-year OSS service.", name_variants=["Mischa Titiev", "Misha Titiev"], personnel_category="civilian_professional_or_administrative_grade", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="verified_employer_found", next_action="Review Box 779 for the formal leave, OSS entry date and assignment; University of Michigan is already documented as the immediate and last civilian employer.", archival_review_priority="medium"),
            base_update(17, identity_status="confirmed", identity_evidence="Exact private identifier agreement and the matching initial in an authoritative MoMA biography explicitly connect Roy V. Titus, Helena Rubinstein Inc. and wartime OSS service.", name_variants=["Roy V. Titus"], personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="verified_employer_found", next_action="Review Box 779 for the OSS entry date and prewar company title; do not project later executive titles backward.", archival_review_priority="medium"),
            base_update(19, identity_status="high_confidence", identity_evidence="A private nonshared identifier, rare surname, compatible Army record, WSU institutional chronology and obituary support row 19; row 20 remains a separate ambiguous entity.", name_variants=["Carl Tjerandsen", "Carl Tjerandse"], personnel_category="enlisted_army_personnel", possible_duplicate_group="batch957-carl-tjerandsen-page469", research_status="completed", next_action="Review both Box 779 files to determine whether the two source rows represent one person at different service stages or distinct records; do not merge automatically.", archival_review_priority="critical"),
            base_update(21, identity_status="confirmed", identity_evidence="Exact private identifier and name agreement, the compatible middle initial, Utah origin, 1943 enlistment and 442nd service chronology confirm Joseph Mamoru Tobari.", name_variants=["Joseph Mamoru Tobari", "Joseph 'Joe' Tobari"], personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="completed", next_action="Review Box 779 for the relationship between 442nd service and the indexed OSS personnel file; student status at University of Utah is documented.", archival_review_priority="high"),
            base_update(22, identity_status="high_confidence", identity_evidence="The exact first name, surname and middle initial plus Smithsonian documentation of Army Air Force intelligence and 1945 OSS graphic-design work support Abraham Joel Tobias.", name_variants=["Abraham Joel Tobias"], personnel_category="unknown_or_indeterminate", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="completed", next_action="Review Box 779 to establish service status, dates and any civilian work between the Federal Arts Project and Army Air Force assignment.", archival_review_priority="medium"),
            base_update(23, identity_status="confirmed", identity_evidence="The distinctive exact name and private nonshared identifier connect the index row to the official Army record.", personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="occupation_only_found", next_action="Review Box 779 for the acting employer, production or venue and the Army-to-OSS sequence; the historical actor category alone does not name an employer.", archival_review_priority="high"),
        ]
    )
    return values


def research_attempts() -> list[dict[str, object]]:
    special = {
        1: "Private identifier review plus a scholarly OSS Greece history and memorial roster established the Tiniakos variant, merchant-marine background and broad U.S. Army pathway.",
        2: "A Stanford memorial resolution established the rare Timoshenko variant, permanent Food Research Institute employment and wartime OSS consultancy.",
        5: "Private identifier review and a contemporary broadcast-industry notice established Mutual employment immediately before active Army duty.",
        6: "Private identifier review established a dated historical Architects category at Army entry; no employer or practice was identified.",
        11: "Private identifier review and an institutional biography established the Laurence/Lawrence identity, NYU degree and Army OSS service; the exact education-service sequence remains qualified.",
        14: "ANU and University of Michigan institutional histories explicitly ordered Michigan faculty and ASTP work before the following-year OSS entry.",
        17: "Private identifier review and a MoMA biography explicitly established Helena Rubinstein Inc. as the employer before and after OSS service.",
        19: "Private identifier review, WSU chronology and a published obituary established earlier teaching, federal planning and immediate food-agriculture research; the duplicate row remains separate.",
        21: "Private identifier review, wartime student records and a University of Utah oral-history summary established identity, student status and 1943 enlistment.",
        22: "A Smithsonian finding aid established the exact-name art career, Army Air Force intelligence assignment and 1945 OSS employment.",
        23: "Private identifier review established a dated historical Actors and actresses category at Army entry; no employer, production or venue was identified.",
    }
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in sorted(PEOPLE.items()):
        if row in special:
            outcome = "source_reviewed"
            reviewed = 9
            rejected = 5
            detail = special[row]
        else:
            outcome = "candidate_rejected" if row in {7, 10, 20} else "no_result"
            reviewed = 7
            rejected = 6
            detail = UNRESOLVED[row]
        attempts.append(
            {
                "key": f"page469-row{row}-{slug(name)}-b957",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index and public Archives context; CIA Reading Room or equivalent official-source check; exact-name and meaningful variants; OSS and military clues; employer and occupation 1940; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Box {archive_box(row)}; private identifiers used only when defensible",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_957",
                "started_at": "2026-10-29T21:00:00Z",
                "completed_at": "2026-10-29T23:30:00Z",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search snippets, unsourced genealogy, people-finder pages, modern records, postwar-only leads and sources without an OSS, private-identifier or Box-file bridge were rejected. Search aliases were not treated as silent corrections. The two Carl Tjerandsen rows were not merged.",
                "research_notes": f"{detail} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain, CIA Reading Room-equivalent and Library of Congress searches were checked as applicable. The index page, Army documentation and relevant occupation-code pages were inspected directly. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": (
                    "Compare both distinct Carl Tjerandsen Box 779 files before any merge or duplicate attribution."
                    if row == 20
                    else f"Review Box {archive_box(row)} for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before wartime service."
                ),
                "attempt_number": 1,
                "research_agent_version": "before-oss-b957-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-957-v1",
        "reviewer": "Before OSS Batch 957 evidence review",
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
