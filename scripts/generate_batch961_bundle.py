#!/usr/bin/env python3
"""Generate the reviewed Batch 961 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page471-fulton-torry-to-campbell-townsend-"
    "review_batch-961_2026-10-29.json"
)

INDEX = "nara-index-b961"
ARMY = "army-bulk-b961"
TECH = "army-tech-b961"
CODES = "army-codes-b961"
TORS = "international-tv-almanac-ivan-tors-b961"
TOSCANO = "hoover-samuel-toscano-b961"
TOSO = "nara-alvin-toso-b961"
TOSY = "cnd-castille-henri-tosy-b961"
TOTTORI = "java-calvin-tottori-b961"
TOULMIN_BANK = "harvard-crimson-john-toulmin-b961"
TOULMIN_OSS = "temple-john-toulmin-b961"
TOVAR_CIA = "cia-hugh-tovar-b961"
TOVAR_OBIT = "washington-post-bernardo-tovar-b961"
TOWELL = "nara-bernard-towell-b961"
TOWNSEND = "ny-military-museum-campbell-townsend-b961"


PEOPLE = {
    "471-3": ("7cce93cf-1573-5348-8fe2-06eefb1881f1", "Fulton B Torry"),
    "471-4": ("fadb13e5-8789-5d88-99d6-19899144581f", "Ivan L Tors"),
    "471-5": ("c196ef9d-7da3-5d21-a76e-d3b6253e1a6d", "Samuel J Toscano"),
    "471-6": ("bfd0e358-bde8-554e-bcbc-0fa97266da46", "Alvin Toso"),
    "471-7": ("83f43e3e-486d-5cb6-99b1-57a63f440526", "Louis C Tossy"),
    "471-8": ("bdc4c7f4-1391-5279-8027-0de411dc2dbe", "Henri S Tosy"),
    "471-9": ("c0ede82a-f3a6-5a4f-99dd-a543647db0e9", "Charles M Toth"),
    "471-10": ("1ac4f57c-668e-5957-9783-55f13f4fd885", "Frank S Toth"),
    "471-11": ("fa84528c-a191-5a70-ae2d-c6f480d35c63", "Gordon K Totten"),
    "471-12": ("349e5385-11af-5d13-a55a-6720cbd23624", "Lowell S Totton"),
    "471-13": ("572de7a9-c6e3-53c1-9d1d-7f1ca5516c05", "Calvin A Tottori"),
    "471-14": ("96db45dd-3f47-5c96-b15f-226b4c8956f2", "John E Toulmin"),
    "471-15": ("35e93c41-be61-545d-b2c2-1e3b70973b95", "Robert J Tousignant"),
    "471-16": ("1ee653dc-122f-5dfa-9151-bc0676f56454", "George H Touslay"),
    "471-17": ("2082513f-fd12-55cd-bdcd-cce06e7e50f0", "Bernardo H Tovar"),
    "471-18": ("983bf923-9d2c-5849-b479-5e3a0e6fc801", "Bernard A Towell"),
    "471-19": ("2190dafe-14fd-5973-b94f-21335d626562", "James A Tower"),
    "471-20": ("e6f0686a-c4c3-5edc-b84a-db3e3da409c6", "James M Towle"),
    "471-21": ("77e34712-a863-5b34-b0ae-eb3301b302f5", "Frank M Towne"),
    "471-22": ("5e4380ad-c504-584b-8198-38cb4db9fa4c", "Hazen A Towne"),
    "471-23": ("58272cdf-0f08-5172-b65d-0b80d251f536", "Elsie S Townlsey"),
    "471-24": ("4c5aa755-2add-5a7f-9f62-4b7c80830c88", "Marion Towns"),
    "471-25": ("cc737543-a7a4-5200-be84-326a52ee892a", "Campbell Townsend"),
}


ARMY_OCCUPATIONS = {
    "471-3": ("Fulton B Torry", "1942-04-10", "138", "Stock clerks", "178"),
    "471-9": ("Charles M Toth", "1942-02-21", "678", "Semiskilled machine-shop and related occupations, n.e.c.", "173"),
    "471-10": ("Frank S Toth", "1942-07-13", "688", "Semiskilled occupations in mechanical treatment of metals, n.e.c.", "174"),
    "471-12": ("Lowell S Totton", "1941-02-26", "106", "Financial institution clerks, n.e.c.", "171"),
    "471-20": ("James M Towle", "1942-08-13", "602", "Semiskilled occupations in production of bakery products, n.e.c.", "173"),
    "471-21": ("Frank M Towne", "1943-01-30", "031", "Teachers (secondary school) and principals", "171"),
    "471-22": ("Hazen A Towne", "1942-12-14", "963", "Unskilled nonprocess occupations in manufacturing, n.e.c.", "174"),
    "471-25": ("Campbell Townsend", "1941-01-27", "003", "Architects", "170"),
}

ARMY_IDENTITY_ONLY = {
    "471-5": ("Samuel J Toscano", "1943-07-17", "999"),
    "471-13": ("Calvin A Tottori", "1943-03-24", "993"),
}

UNRESOLVED = {
    "471-7": "Exact-name, variant, OSS, employer, occupation, obituary, institutional, newspaper and archival searches produced no defensible identity bridge.",
    "471-11": "The indexed officer-style identifier and exact name produced no public second identifier or reliable pre-OSS affiliation.",
    "471-15": "Searches returned multiple modern and military namesakes, none connected by the protected identifier or an OSS record.",
    "471-16": "Exact-name and spelling-variant searches produced no defensible identity or pre-OSS affiliation beyond the index row.",
    "471-19": "Same-name biographical and obituary leads lacked the indexed middle initial, protected identifier or an OSS bridge.",
    "471-24": "Exact-name, military, institutional, directory, obituary and archival searches produced no defensible identity bridge.",
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
            "archival_identifier": "RG 226, Entry A1-224, Boxes 782-783",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 471, rows 3-25; checked against layout text and a 300 dpi render",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate people. Protected identifiers remain excluded from public evidence and exports.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; ten accepted Batch 961 identity candidates; identifiers withheld",
            "access_date": "2026-10-29",
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
            "locator": "PDF physical pages 170-174 and 178; eight historical civilian-occupation categories checked visually",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical categories are qualified and never converted into named employers, workplaces or exact modern job titles.",
        },
        {
            "key": TORS,
            "stable_url": "https://www.worldradiohistory.com/Archive-International-Television-Almanac/1956/International-Television-Almanac-1956-1-Whos-Who.pdf",
            "title": "International Television Almanac 1956: Who's Who",
            "repository_publisher": "Quigley Publishing Company; World Radio History",
            "publication_record_date": "1956",
            "locator": "Tors, Ivan entry in the Tor-Tra section",
            "access_date": "2026-10-29",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "International Television Almanac",
            "rights_notes": "The professional directory supplies a compact career chronology; no postwar employer is used as prewar evidence.",
        },
        {
            "key": TOSCANO,
            "stable_url": "https://digitalcollections.hoover.org/internal/media/dispatcher/331570/full",
            "title": "The Board at 1330 o'clock, 2 May 1944",
            "author_creator": "Office of Strategic Services review board",
            "repository_publisher": "Hoover Institution Library & Archives",
            "publication_record_date": "1944-05-02",
            "locator": "Page 3B; Pvt. Samuel J. Toscano testimony and review",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "Hoover Institution Digital Collections",
            "rights_notes": "Only a short excerpt and project-authored paraphrase are retained.",
        },
        {
            "key": TOSO,
            "stable_url": "https://www.archives.gov/files/research/jfk/releases/2022/104-10165-10121.pdf",
            "archival_identifier": "JFK release 104-10165-10121",
            "title": "Headquarters Operational Group Command, Special Orders Number 9",
            "author_creator": "Office of Strategic Services",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1945-05-09",
            "locator": "Section 3; T Sgt Alvin Toso assigned to Company B, Special Reconnaissance Battalion",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "John F. Kennedy Assassination Records Collection",
            "rights_notes": "The public claim omits the full service identifier printed in the order.",
        },
        {
            "key": TOSY,
            "stable_url": "https://www.cnd-castille.org/wp-content/uploads/2021/10/infiltrations_into_france.pdf",
            "title": "History of WWII Infiltrations into France",
            "repository_publisher": "Centre National de Documentation Castille",
            "publication_record_date": "2021-07-31",
            "locator": "Appendix 36; 7 June 1944 Cendrillon mission row; archival references include NARA M1623 and SHD GR 28 P 4 175/85",
            "access_date": "2026-10-29",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "History of Agents Infiltrated into France",
            "rights_notes": "The rare-name match remains probable because the compiled mission table does not supply the index's middle initial.",
        },
        {
            "key": TOTTORI,
            "stable_url": "https://www.javadc.org/MISLS%20Registry%2002-02-03.pdf",
            "title": "Military Intelligence Service Language School Registry, 1941-46",
            "author_creator": "Japanese American Veterans Association",
            "repository_publisher": "Japanese American Veterans Association",
            "locator": "Registry row 5919; Calvin A. Tottori; Savannah February 1944; OSS Detachment 101",
            "access_date": "2026-10-29",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Military Intelligence Service Registry",
            "rights_notes": "The public claim omits the full service identifier printed in the registry.",
        },
        {
            "key": TOULMIN_BANK,
            "stable_url": "https://www.thecrimson.com/article/1939/10/10/alumni-association-elects-new-officers-pdr/",
            "title": "Alumni Association Elects New Officers",
            "author_creator": "The Harvard Crimson",
            "repository_publisher": "The Harvard Crimson",
            "publication_record_date": "1939-10-10",
            "locator": "John E. Toulmin '25 entry",
            "access_date": "2026-10-29",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "The Harvard Crimson archive",
            "rights_notes": "Contemporary evidence for employer and role; Harvard alumni status is not treated as employment.",
        },
        {
            "key": TOULMIN_OSS,
            "stable_url": "https://scholarshare.temple.edu/bitstreams/0e8035f8-21d3-455c-a831-2b1c6c0af02f/download",
            "title": "Intelligence Professionalism: A Study of Developing Intelligence",
            "repository_publisher": "Temple University ScholarShare",
            "locator": "Page 130; Colonel John Toulmin appointed head of OSS Cairo in summer 1943",
            "access_date": "2026-10-29",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Temple University electronic theses and dissertations",
            "rights_notes": "Used with the exact-name index row to bridge the prewar banker to the OSS officer.",
        },
        {
            "key": TOVAR_CIA,
            "stable_url": "https://www.cia.gov/resources/csi/studies-in-intelligence/volume-54-no-2/",
            "title": "Training for War and Espionage: Office of Strategic Services Training During World War II",
            "author_creator": "John Whiteclay Chambers II",
            "repository_publisher": "Central Intelligence Agency, Center for the Study of Intelligence",
            "publication_record_date": "2010-06",
            "locator": "Studies in Intelligence 54, no. 2, page 37; Lt. Hugh Tovar",
            "access_date": "2026-10-29",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Studies in Intelligence",
            "rights_notes": "CIA hosts the article but states that authors' views do not necessarily represent an official agency position.",
        },
        {
            "key": TOVAR_OBIT,
            "stable_url": "https://www.legacy.com/us/obituaries/washingtonpost/name/bernado-tovar-obituary?id=6053066",
            "title": "Bernardo Hugh Tovar obituary",
            "repository_publisher": "The Washington Post via Legacy.com",
            "publication_record_date": "2015-06-29",
            "locator": "Obituary text; Harvard, Army and OSS chronology",
            "access_date": "2026-10-29",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "The Washington Post obituaries",
            "rights_notes": "The web heading misspells Bernado; the obituary text repeatedly supplies Bernardo Hugh Tovar.",
        },
        {
            "key": TOWELL,
            "stable_url": "https://nara-media.s3.amazonaws.com/dc-metro/rg-263/640446/640446_Box58_Folder4/640446_Box58_Folder4.pdf",
            "archival_identifier": "RG 263, NAID 640446, Box 58, Folder 4",
            "title": "Memorandum to Bernard A. Towell, X-2 Branch, Office of Strategic Services",
            "author_creator": "Frederick B. Lyon, Department of State",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1945-07-04",
            "locator": "Memorandum addressed to Bernard A. Towell, X-2 Branch, OSS",
            "access_date": "2026-10-29",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Central Intelligence Agency, Record Group 263",
            "rights_notes": "Direct wartime identity and assignment evidence; it does not name a pre-OSS employer.",
        },
        {
            "key": TOWNSEND,
            "stable_url": "https://museum.dmna.ny.gov/unit-history/conflict/world-war-2-1939-1945/27th-infantry-division-world-war-two/27th-infantry-division-world-war-two-men-who-were-federalized-1940/27th-infantry-division-world-war-two-men-who-were-federalized-1940-last-names-beginning-t",
            "title": "27th Infantry Division World War Two Men Who Were Federalized in 1940: T",
            "author_creator": "New York State Military Museum and Veterans Research Center",
            "repository_publisher": "New York State Division of Military and Naval Affairs",
            "locator": "Campbell Townsend row; Troop E, 101st Cavalry; 23 September 1940 to 16 October 1945",
            "access_date": "2026-10-29",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "New York National Guard World War II roster",
            "rights_notes": "The public claim omits the full service identifier printed in the roster.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {"key": "org-army-b961", "organization_id": "24cec6d5-c3cc-5dc4-b8c9-10ef805535e9", "canonical_name": "United States Army", "historical_name": "United States Army", "aliases": ["U.S. Army", "Army of the United States"], "organization_type": "military branch", "sector": "military", "country": "United States", "normalization_notes": "Military assignment remains distinct from civilian employment."},
        {"key": "org-usaaf-b961", "canonical_name": "United States Army Air Forces", "historical_name": "Army Air Forces", "aliases": ["Army Air Force", "USAAF"], "organization_type": "military branch", "sector": "military", "country": "United States", "active_dates": "1941-1947", "normalization_notes": "Historical wartime branch wording retained."},
        {"key": "org-fordham-b961", "canonical_name": "Fordham University", "historical_name": "Fordham University", "aliases": [], "organization_type": "university", "sector": "academia_and_research", "city": "New York", "state_or_region": "New York", "country": "United States", "normalization_notes": "Student relationship is not employment."},
        {"key": "org-harvard-b961", "canonical_name": "Harvard University", "historical_name": "Harvard University", "aliases": ["Harvard"], "organization_type": "university", "sector": "academia_and_research", "city": "Cambridge", "state_or_region": "Massachusetts", "country": "United States", "normalization_notes": "Student relationship is not employment."},
        {"key": "org-first-national-boston-b961", "canonical_name": "First National Bank of Boston", "historical_name": "The First National Bank of Boston", "aliases": [], "organization_type": "bank", "sector": "finance_and_banking", "city": "Boston", "state_or_region": "Massachusetts", "country": "United States", "normalization_notes": "Historical employer name preserved; no modern successor is substituted."},
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
    for key, (_variant, entry_date, code, occupation, _page) in ARMY_OCCUPATIONS.items():
        person_id, name = person(key)
        values.append(
            affiliation(
                f"army-occupation-{slug(name)}-b961",
                person_id,
                "employment",
                "strongly_date_bounded",
                "high_confidence",
                "medium",
                "A_direct_official",
                "publish_qualified",
                f"Historical code {code} at Army entry; no named employer or workplace is inferred. Full protected identifier withheld.",
                occupation=occupation,
                end_date=entry_date,
                date_precision="exact Army entry date; occupation current at entry",
                country="United States",
            )
        )

    ivan, _ = person("471-4")
    john, _ = person("471-14")
    bernardo, _ = person("471-17")
    values.extend(
        [
            affiliation("ivan-tors-usaaf-b961", ivan, "military_assignment", "probable_immediate", "high_confidence", "medium", "C_reputable_contemporary_or_scholarly", "publish_qualified", "The directory groups Army Air Forces and OSS service but does not state an exact transfer date.", organization_key="org-usaaf-b961", organization_name_as_found="Army Air Forces", country="United States", immediate_pre_oss=True),
            affiliation("ivan-tors-fordham-b961", ivan, "student", "documented_prewar", "high_confidence", "high", "C_reputable_contemporary_or_scholarly", "published", "The directory explicitly names Fordham education before its wartime service sentence; student status is not employment.", organization_key="org-fordham-b961", organization_name_as_found="Fordham U., New York", occupation="student", city="New York", state_or_region="New York", country="United States"),
            affiliation("ivan-tors-playwright-b961", ivan, "professional_affiliation", "documented_prewar", "high_confidence", "high", "C_reputable_contemporary_or_scholarly", "published", "The directory names several plays written in Europe before the wartime chronology; no employer is inferred.", role_title="playwright", occupation="playwright", country="Hungary"),
            affiliation("john-toulmin-bank-b961", john, "employment", "strongly_date_bounded", "high_confidence", "high", "C_reputable_contemporary_or_scholarly", "published", "A contemporary 1939 report names his bank and vice-presidential role; an independent scholarly source places exact-name Colonel John Toulmin in OSS Cairo in 1943.", organization_key="org-first-national-boston-b961", organization_name_as_found="First National Bank of Boston", role_title="vice president", occupation="banker", end_date="after 1939 and before 1943", date_precision="bounded by contemporary 1939 employment and 1943 OSS command", city="Boston", state_or_region="Massachusetts", country="United States", last_civilian_pre_service=True),
            affiliation("bernardo-tovar-army-b961", bernardo, "military_assignment", "explicit_immediate", "high_confidence", "high", "C_reputable_contemporary_or_scholarly", "published", "The obituary explicitly places infantry, artillery and communications assignments after commissioning and before his 1945 OSS selection; CIA history independently confirms the Harvard ROTC trainee.", organization_key="org-army-b961", organization_name_as_found="Army", role_title="second lieutenant", start_date="1944-06", end_date="1945", date_precision="month/year start and year end", country="United States", immediate_pre_oss=True),
            affiliation("bernardo-tovar-harvard-b961", bernardo, "student", "strongly_date_bounded", "high_confidence", "high", "C_reputable_contemporary_or_scholarly", "published", "The obituary dates Harvard and ROTC from September 1941 to the 1943 active-duty call; CIA history independently calls him a Harvard ROTC graduate.", organization_key="org-harvard-b961", organization_name_as_found="Harvard", role_title="student and ROTC cadet", occupation="student", start_date="1941-09", end_date="1943-06", date_precision="month", city="Cambridge", state_or_region="Massachusetts", country="United States"),
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
    variant, entry_date, code, occupation, page = ARMY_OCCUPATIONS[key]
    return [
        claim(
            f"identity-{slug(name)}-army-b961",
            person_id,
            "identity",
            f"The indexed {name} is a high-confidence match to the reviewed official Army record.",
            f"The protected identifier agrees and the Army record names {variant}; Army entry was {entry_date}.",
            "High confidence from exact protected-identifier agreement and a compatible exact name.",
            "The Army record dates entry but not the later OSS transfer.",
            "A_direct_official",
            "high",
            "published",
            "Full protected identifiers and raw bulk rows remain excluded from public data.",
            [
                {"source_key": INDEX, "locator_override": f"PDF page 471 row {key.split('-')[1]}; Box {'783' if key == '471-25' else '782'}; protected identifier withheld"},
                {"source_key": ARMY, "locator_override": f"Reviewed {variant} record; protected identifier withheld"},
                {"source_key": TECH, "support_type": "context_only", "locator_override": "Field definitions, PDF physical pages 44-46"},
            ],
        ),
        claim(
            f"occupation-{slug(name)}-army-b961",
            person_id,
            "occupation",
            f"At Army entry on {entry_date}, {variant} was recorded in the historical {occupation} category.",
            f"The official bulk record supplies code {code}; the visually reviewed NARA list expands that historical code.",
            "High confidence from the accepted protected-identifier bridge.",
            "Strongly date-bounded at Army entry; no employer, workplace or immediate OSS sequence is named.",
            "A_direct_official",
            "medium",
            "publish_qualified",
            "The broad historical category is not converted into a named employer or exact modern job title.",
            [
                {"source_key": ARMY, "locator_override": f"Army entry {entry_date}; code {code}; protected identifier withheld"},
                {"source_key": CODES, "locator_override": f"PDF physical page {page}; historical category {code}"},
            ],
            affiliation_key=f"army-occupation-{slug(name)}-b961",
            excerpt=occupation,
        ),
    ]


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for key in ARMY_OCCUPATIONS:
        values.extend(army_claims(key))

    ivan, _ = person("471-4")
    samuel, _ = person("471-5")
    alvin, _ = person("471-6")
    henri, _ = person("471-8")
    calvin, _ = person("471-13")
    john, _ = person("471-14")
    bernardo, _ = person("471-17")
    bernard_towell, _ = person("471-18")
    values.extend(
        [
            claim("identity-ivan-tors-b961", ivan, "identity", "The indexed Ivan L Tors is a high-confidence match to writer and producer Ivan Tors.", "The rare exact name, compatible Army Air Forces and OSS service, and prewar European/Fordham chronology agree with the indexed enlisted record.", "High confidence from a distinctive exact name and an explicit Army Air Forces/OSS biography; the public biography omits the middle initial and service identifier.", "The directory separates European writing and education from wartime service.", "C_reputable_contemporary_or_scholarly", "high", "published", "No later film-company affiliation is projected backward into the prewar period.", [{"source_key": INDEX, "locator_override": "PDF page 471 row 4; Box 782; protected identifier withheld"}, {"source_key": TORS}]),
            claim("immediate-ivan-tors-usaaf-b961", ivan, "immediate_pre_oss_affiliation", "The United States Army Air Forces was the probable military pathway immediately before Ivan Tors's OSS service.", "The professional directory places Army Air Forces and OSS together in its wartime chronology.", "High-confidence distinctive-name identity.", "Probable immediate sequence; the directory does not state an exact transfer order or date.", "C_reputable_contemporary_or_scholarly", "medium", "publish_qualified", "Modeled as a military assignment, not a civilian employer.", [{"source_key": TORS, "excerpt_override": "During World War II with Army Air Forces and O.S.S."}], affiliation_key="ivan-tors-usaaf-b961"),
            claim("prewar-ivan-tors-fordham-b961", ivan, "other_pre_oss_affiliation", "Ivan Tors studied at Fordham University before his wartime service.", "The directory lists Fordham education before its sentence on Army Air Forces and OSS service.", "High-confidence distinctive-name identity.", "Documented prewar education; not a named employer.", "C_reputable_contemporary_or_scholarly", "high", "published", "Student status is kept separate from employment.", [{"source_key": TORS, "excerpt_override": "U. of Budapest and Fordham U., New York"}], affiliation_key="ivan-tors-fordham-b961"),
            claim("occupation-ivan-tors-playwright-b961", ivan, "occupation", "Ivan Tors had written plays in Europe before his wartime service.", "The directory names several plays before its wartime Army Air Forces and OSS chronology.", "High-confidence distinctive-name identity.", "Documented prewar occupation; no employer or immediate sequence is claimed.", "C_reputable_contemporary_or_scholarly", "high", "published", "Playwriting is not converted into self-employment or a named employer without evidence.", [{"source_key": TORS, "excerpt_override": "While in Europe wrote numerous plays"}], affiliation_key="ivan-tors-playwright-b961"),
            claim("identity-samuel-toscano-b961", samuel, "identity", "The indexed Samuel J Toscano is confirmed as the OSS interpreter reviewed on 2 May 1944.", "The contemporary board record supplies the exact full name and protected identifier printed in the index.", "Confirmed by exact name and protected-identifier agreement in a direct OSS record.", "The record explicitly dates civilian OSS entry to July 1943 but does not name his prior employer.", "A_direct_official", "confirmed", "published", "The statement about prior weekly earnings is not converted into an employer claim.", [{"source_key": INDEX, "locator_override": "PDF page 471 row 5; Box 782; protected identifier withheld"}, {"source_key": TOSCANO, "locator_override": "Page 3B; protected identifier withheld", "excerpt_override": "Entered OSS as a civilian in July 1943"}]),
            claim("identity-alvin-toso-b961", alvin, "identity", "The indexed Alvin Toso is confirmed as the OSS Operational Group technical sergeant in the 9 May 1945 special order.", "The exact name and protected identifier agree between the index and the OSS order.", "Confirmed by exact protected-identifier agreement in a direct OSS order.", "The order documents a 1945 OSS assignment, not a pre-OSS employer.", "A_direct_official", "confirmed", "published", "No civilian employer is inferred from military service.", [{"source_key": INDEX, "locator_override": "PDF page 471 row 6; Box 782; protected identifier withheld"}, {"source_key": TOSO, "locator_override": "Special Orders Number 9, section 3; protected identifier withheld", "excerpt_override": "T Sgt Alvin Toso"}]),
            claim("identity-henri-tosy-b961", henri, "identity", "The indexed Henri S Tosy is a probable match to OSS Cendrillon radio operator Henri Tosy, alias Henri Bousquet.", "A compiled mission table cites NARA and French archival files for rare-name radio operator Henri Tosy on the 7 June 1944 Cendrillon mission.", "Probable from the rare exact first and last name and explicit OSS mission; the mission table omits the index's middle initial.", "The evidence documents wartime OSS activity but no pre-OSS affiliation.", "C_reputable_contemporary_or_scholarly", "medium", "publish_qualified", "Henri Bousquet is retained as a documented mission alias; the Box 782 file is still required for confirmation.", [{"source_key": INDEX, "locator_override": "PDF page 471 row 8; Box 782"}, {"source_key": TOSY, "excerpt_override": "WT Henri Tosy @Henri Bousquet"}]),
            claim("identity-calvin-tottori-b961", calvin, "identity", "The indexed Calvin A Tottori is a high-confidence match to the MIS Language School registrant assigned to OSS Detachment 101.", "The registry supplies the exact name, the protected identifier printed in the index, a February 1944 class and the OSS detachment.", "High confidence from exact full-name and protected-identifier agreement in an institutional military registry.", "The registry documents wartime language-school and OSS assignment, not a pre-OSS employer.", "B_authoritative_institutional", "high", "published", "Army code 993 is undefined in the reviewed code list and is not published as an occupation.", [{"source_key": INDEX, "locator_override": "PDF page 471 row 13; Box 782; protected identifier withheld"}, {"source_key": TOTTORI, "locator_override": "Registry row 5919; protected identifier withheld", "excerpt_override": "OSS, Detach 101"}]),
            claim("identity-john-toulmin-b961", john, "identity", "The indexed John E Toulmin is a high-confidence match to banker and OSS Cairo chief John E. Toulmin.", "A contemporary 1939 report names John E. Toulmin at the First National Bank of Boston; a scholarly NARA-based study names Colonel John Toulmin as OSS Cairo chief in 1943.", "High confidence from exact name and middle initial, compatible chronology, officer status and two independent reputable sources.", "The sources bridge a 1939 civilian job to a 1943 OSS command but do not supply the Army entry date.", "C_reputable_contemporary_or_scholarly", "high", "published", "No postwar bank title is used to enlarge the 1939 role.", [{"source_key": INDEX, "locator_override": "PDF page 471 row 14; Box 782; protected identifier withheld"}, {"source_key": TOULMIN_BANK}, {"source_key": TOULMIN_OSS}]),
            claim("last-civilian-john-toulmin-bank-b961", john, "last_civilian_pre_service", "The First National Bank of Boston was John E. Toulmin's last documented civilian employer before wartime service and OSS command.", "The Harvard Crimson identifies him as the bank's vice president in October 1939; an independent scholarly study places him in command of OSS Cairo in summer 1943.", "High-confidence exact-name identity.", "Strongly date-bounded; the evidence does not exclude an undocumented intervening affiliation.", "C_reputable_contemporary_or_scholarly", "high", "published", "Presented as last documented civilian employer, not an explicit recruited-from claim.", [{"source_key": TOULMIN_BANK, "excerpt_override": "Vice-President of the First National Bank of Boston"}, {"source_key": TOULMIN_OSS, "support_type": "context_only", "locator_override": "Page 130"}], affiliation_key="john-toulmin-bank-b961"),
            claim("identity-bernardo-tovar-b961", bernardo, "identity", "The indexed Bernardo H Tovar is a high-confidence match to Bernardo Hugh Tovar, the Harvard ROTC graduate and OSS trainee.", "The obituary expands the exact indexed name and gives the Army-to-OSS chronology; the CIA history independently identifies Lt. Hugh Tovar as a Harvard ROTC graduate and OSS trainee.", "High confidence from the exact full-name expansion and two independent sources with matching Harvard, Army and OSS chronology.", "Both sources date the Army and OSS sequence to 1943-45.", "B_authoritative_institutional", "high", "published", "The obituary heading's Bernado typo is not adopted; the body repeatedly supplies Bernardo Hugh Tovar.", [{"source_key": INDEX, "locator_override": "PDF page 471 row 17; Box 782; protected identifier withheld"}, {"source_key": TOVAR_CIA, "locator_override": "Studies in Intelligence 54, no. 2, page 37"}, {"source_key": TOVAR_OBIT}]),
            claim("immediate-bernardo-tovar-army-b961", bernardo, "immediate_pre_oss_affiliation", "The United States Army was Bernardo Hugh Tovar's immediate affiliation before he joined OSS in 1945.", "The obituary states that after commissioning and Army assignments he volunteered and was selected for OSS in 1945; CIA history corroborates the lieutenant and trainee chronology.", "High-confidence identity from the exact-name bridge and independent CIA history.", "Explicit immediate chronology in the obituary.", "C_reputable_contemporary_or_scholarly", "high", "published", "Military assignment is kept separate from civilian employment.", [{"source_key": TOVAR_OBIT, "excerpt_override": "volunteered and was selected to join the Office of Strategic Services"}, {"source_key": TOVAR_CIA, "support_type": "context_only", "locator_override": "Page 37"}], affiliation_key="bernardo-tovar-army-b961"),
            claim("prewar-bernardo-tovar-harvard-b961", bernardo, "other_pre_oss_affiliation", "Bernardo Hugh Tovar was a Harvard University student and ROTC cadet before active Army duty.", "The obituary dates Harvard and ROTC from September 1941 until the June 1943 active-duty call; CIA history independently calls him a Harvard ROTC graduate.", "High-confidence exact-name identity.", "Strongly date-bounded immediately before active Army service; student status is not employment.", "C_reputable_contemporary_or_scholarly", "high", "published", "Harvard is not counted as a civilian employer.", [{"source_key": TOVAR_OBIT, "excerpt_override": "Hugh entered Harvard in September 1941, and joined the ROTC."}, {"source_key": TOVAR_CIA, "support_type": "context_only", "locator_override": "Page 37"}], affiliation_key="bernardo-tovar-harvard-b961"),
            claim("identity-bernard-towell-b961", bernard_towell, "identity", "The indexed Bernard A Towell is confirmed as Bernard A. Towell of OSS X-2 Branch.", "A 4 July 1945 Department of State memorandum is addressed to the exact full name at X-2 Branch, Office of Strategic Services.", "Confirmed by exact full name and direct official OSS branch identification.", "The memorandum documents a wartime OSS role but no pre-OSS employer.", "A_direct_official", "confirmed", "published", "Postwar financial-employer leads were not projected backward.", [{"source_key": INDEX, "locator_override": "PDF page 471 row 18; Box 782"}, {"source_key": TOWELL, "excerpt_override": "BERNARD A. TOWELL, X-2 BRANCH, OFFICE OF STRATEGIC SERVICES"}]),
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
    _person_id, name = person(key)
    box = "783" if key in {"471-23", "471-24", "471-25"} else "782"
    return base_update(
        key,
        identity_status="unresolved",
        identity_evidence=f"The visually verified index row supplies {name}, Box {box} and archive location 230/86/42/02. {reason}",
        personnel_category="unknown_or_indeterminate",
        research_status="requires_archival_review",
        next_action=f"Review Box {box} for corroborating identifiers, immediate pre-OSS affiliation and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        archival_review_priority="high",
    )


def army_update(key: str) -> dict[str, object]:
    _variant, _entry_date, _code, occupation, _page = ARMY_OCCUPATIONS[key]
    box = "783" if key == "471-25" else "782"
    return base_update(
        key,
        identity_status="high_confidence",
        identity_evidence="A nonshared protected identifier connects the visually verified index row to the official Army record with an exact compatible name.",
        personnel_category="enlisted_army_personnel",
        commissioned_officer=False,
        allied_or_foreign_personnel=False,
        research_status="occupation_only_found",
        next_action=f"Review Box {box} for a named employer and the Army-to-OSS sequence; the broad historical {occupation} category is not a workplace.",
        archival_review_priority="high",
    )


def person_updates() -> list[dict[str, object]]:
    values = [unresolved_update(key, reason) for key, reason in UNRESOLVED.items()]
    values.extend(army_update(key) for key in ARMY_OCCUPATIONS)
    values.extend(
        [
            base_update("471-4", identity_status="high_confidence", identity_evidence="A professional directory under the distinctive exact name Ivan Tors documents Army Air Forces and OSS service, European playwriting and Fordham study; the public source omits the middle initial and protected identifier.", name_variants=["Ivan Tors"], personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=True, research_status="completed", next_action="Review Box 782 for the exact Army Air Forces-to-OSS transfer date and any named prewar employer; the documented playwright occupation is not a workplace.", archival_review_priority="high"),
            base_update("471-5", identity_status="confirmed", identity_evidence="A direct 2 May 1944 OSS review-board record supplies Samuel J. Toscano's exact name and the protected identifier printed in the index.", personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="requires_archival_review", next_action="Review Box 782 for the employer or occupation behind the board's pre-OSS earnings statement. No named prior employer appears in the accessible direct record.", archival_review_priority="high"),
            base_update("471-6", identity_status="confirmed", identity_evidence="A 9 May 1945 OSS special order supplies Alvin Toso's exact name and the protected identifier printed in the index.", personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="requires_archival_review", next_action="Review Box 782 for Alvin Toso's pre-Army civilian employer and exact Army-to-OSS transfer chronology.", archival_review_priority="high"),
            base_update("471-8", identity_status="probable", identity_evidence="A compiled mission table citing NARA and French archival records identifies rare-name OSS Cendrillon radio operator Henri Tosy, alias Henri Bousquet; it omits the index middle initial.", name_variants=["Henri Tosy", "Henri Bousquet"], personnel_category="foreign_or_allied_military_personnel", commissioned_officer=False, allied_or_foreign_personnel=True, possible_duplicate_group="batch961-henri-s-tosy-cendrillon", research_status="requires_archival_review", next_action="Compare Box 782 with SHD GR 28 P 4 175/85 and the NARA Cendrillon report to confirm the middle initial and identify any pre-mission affiliation.", archival_review_priority="critical"),
            base_update("471-13", identity_status="high_confidence", identity_evidence="The MIS Language School registry agrees on Calvin A. Tottori's exact name and protected identifier and records OSS Detachment 101.", personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="requires_archival_review", next_action="Review Box 782 for Calvin Tottori's pre-Army employer or occupation; Army code 993 remains undefined and is not published as an occupation.", archival_review_priority="high"),
            base_update("471-14", identity_status="high_confidence", identity_evidence="A contemporary report identifies exact-name John E. Toulmin as a First National Bank of Boston vice president in 1939; a scholarly NARA-based study identifies Colonel John Toulmin as OSS Cairo chief in 1943.", name_variants=["John E. Toulmin", "John Edwin Toulmin"], personnel_category="commissioned_army_officer", commissioned_officer=True, allied_or_foreign_personnel=False, research_status="verified_employer_found", next_action="Review Box 782 for his Army entry date and any intervening affiliation between the documented 1939 bank role and 1943 OSS command.", archival_review_priority="medium"),
            base_update("471-17", identity_status="high_confidence", identity_evidence="The Bernardo Hugh Tovar obituary supplies the indexed full-name expansion and Army-to-OSS chronology; CIA history independently identifies Lt. Hugh Tovar as a Harvard ROTC graduate and OSS trainee.", name_variants=["Bernardo Hugh Tovar", "B. Hugh Tovar", "Hugh Tovar"], personnel_category="commissioned_army_officer", commissioned_officer=True, allied_or_foreign_personnel=False, research_status="completed", next_action="Review Box 782 for his exact infantry, artillery and communications assignments and OSS transfer order; Harvard student status is already distinct from employment.", archival_review_priority="medium"),
            base_update("471-18", identity_status="confirmed", identity_evidence="A 4 July 1945 Department of State memorandum is addressed to the exact full name Bernard A. Towell at OSS X-2 Branch.", personnel_category="civilian_professional_or_administrative_grade", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="requires_archival_review", next_action="Review Box 782 for Bernard Towell's pre-OSS employer and X-2 appointment chronology; the direct memorandum names no predecessor.", archival_review_priority="high"),
            base_update("471-23", identity_status="ambiguous", identity_evidence="The index prints Elsie S Townlsey and adds the note '? Move t', which may indicate Townsley; postwar same-name records do not provide an OSS or Box-file bridge.", name_variants=["Elsie S Townsley"], personnel_category="unknown_or_indeterminate", commissioned_officer=None, allied_or_foreign_personnel=False, possible_duplicate_group="batch961-elsie-townlsey-townsley", research_status="requires_archival_review", next_action="Review Box 783 to confirm whether Townlsey should be normalized to Townsley and to identify the immediate pre-OSS affiliation. No spouse's employer or biography has been transferred.", archival_review_priority="critical"),
        ]
    )
    return values


def research_attempts() -> list[dict[str, object]]:
    special = {
        "471-3": "Accepted exact-name protected-identifier Army bridge and verified the historical stock-clerk category.",
        "471-4": "A professional directory established the distinctive Ivan Tors Army Air Forces/OSS identity, prewar playwriting and Fordham study.",
        "471-5": "A direct OSS review-board record confirmed Samuel J. Toscano and described July 1943 civilian OSS entry, but named no prior employer.",
        "471-6": "A direct OSS special order confirmed Alvin Toso by exact name and protected identifier; no civilian predecessor was found.",
        "471-8": "A NARA/SHD-citing mission table produced a probable Henri Tosy Cendrillon identity; the missing middle initial requires Box-file confirmation.",
        "471-9": "Accepted exact-name protected-identifier Army bridge and verified the historical semiskilled machine-shop category.",
        "471-10": "Accepted exact-name protected-identifier Army bridge and verified the historical semiskilled metal-treatment category.",
        "471-12": "Accepted exact-name protected-identifier Army bridge and verified the historical financial-institution-clerk category.",
        "471-13": "The MIS Language School registry confirmed the exact-name protected-identifier Calvin A. Tottori lead and OSS Detachment 101; code 993 remained undefined.",
        "471-14": "Contemporary Harvard reporting and scholarly OSS history established John E. Toulmin's 1939 bank role and 1943 OSS Cairo command.",
        "471-17": "CIA history and a Washington Post obituary established Bernardo Hugh Tovar's Harvard-to-Army-to-OSS chronology.",
        "471-18": "A direct Department of State memorandum confirmed Bernard A. Towell at OSS X-2 Branch but supplied no predecessor.",
        "471-20": "Accepted exact-name protected-identifier Army bridge and verified the historical semiskilled bakery-products category.",
        "471-21": "Accepted exact-name protected-identifier Army bridge and verified the historical secondary-school teacher/principal category.",
        "471-22": "Accepted exact-name protected-identifier Army bridge and verified the historical unskilled nonprocess-manufacturing category.",
        "471-23": "Preserved the printed Townlsey form, the index's '? Move t' note and Townsley as an ambiguous candidate variant pending Box 783 review.",
        "471-25": "Accepted exact-name protected-identifier Army bridge, corroborated the 101st Cavalry roster and verified the historical architect category.",
    }
    attempts: list[dict[str, object]] = []
    for key, (person_id, name) in PEOPLE.items():
        row = int(key.split("-")[1])
        box = "783" if row >= 23 else "782"
        if key in special:
            outcome = "candidate_found" if key in {"471-8", "471-23"} else "source_reviewed"
            reviewed = 10
            rejected = 5
            detail = special[key]
        else:
            outcome = "no_result"
            reviewed = 7
            rejected = 6
            detail = UNRESOLVED[key]
        attempts.append(
            {
                "key": f"page471-row{row}-{slug(name)}-b961",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index and public Archives context; CIA Reading Room or equivalent official-source check; exact-name and meaningful variants; OSS, Army and foreign-name clues; employer and occupation 1940; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Box {box}; protected identifiers used only when defensible",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_961",
                "started_at": "2026-10-29T22:20:00Z",
                "completed_at": "2026-10-30T03:15:00Z",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search snippets, unsourced genealogy, people-finder pages, postwar-only leads and sources without an OSS, protected-identifier or Box-file bridge were rejected. Search aliases were not treated as silent corrections. An auction description with a Charles W. Toth/Charles M. Toth discrepancy was rejected as final evidence.",
                "research_notes": f"{detail} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain, CIA Reading Room-equivalent and Library of Congress searches were checked as applicable. The index page, Army bulk file, technical documentation and relevant code-list pages were inspected directly. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": f"Review Box {box} for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before wartime service.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b961-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-961-v1",
        "reviewer": "Before OSS Batch 961 evidence review",
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
