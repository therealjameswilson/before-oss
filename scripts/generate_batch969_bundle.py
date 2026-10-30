#!/usr/bin/env python3
"""Generate the reviewed Batch 969 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page475-gaston-tuggle-to-euclide-turcotte-"
    "review_batch-969_2026-10-30.json"
)

INDEX = "nara-index-b969"
ARMY = "army-bulk-b969"
TECH = "army-tech-b969"
CODES = "army-codes-b969"
DET101_TUGGLE = "det101-tuggle-b969"
NPS_TULLY = "nps-joseph-tully-b969"
TURANO_OBIT = "nytimes-turano-obit-b969"
PERSICO = "persico-papers-turano-b969"
OSSOG_TURCO = "ossog-turco-b969"
NARA_TULARAK = "nara-entry210-tularak-b969"
REYNOLDS_TULARAK = "reynolds-tularak-b969"


PEOPLE = {
    1: ("56ba9eee-1bb0-5054-a45e-4699f644e0d8", "Gaston E Tuggle"),
    2: ("5d842394-776f-549a-a6cf-d8c4c3037525", "Donald G Tuinstra"),
    3: ("a5bf76a7-2699-51ba-af14-6e2d1aa572c3", "Nicholas Tukalo"),
    4: ("e1bb7d16-57bd-5199-8a64-744c85b4f691", "Sam Tularak"),
    5: ("4d0ce179-3d73-55b5-b97c-9cf938f35f1c", "Murray A Tulis"),
    6: ("a48648cb-bc3b-5fcc-9123-b7e9ff3feddf", "Charles O Tulka"),
    7: ("a0badc47-6594-5946-8e5a-a01e23d0f246", "Robt E Tullen"),
    8: ("1649ead5-2a9a-5f10-86fe-00dd4b3474bd", "Robert E Tulley"),
    9: ("0b414d74-66f8-550d-a466-dad5b793fa9f", "Dorothy G Tully"),
    10: ("26b244ae-83c3-5a4d-8c8b-df1b31174f7a", "Jack A Tully"),
    11: ("ec8827c8-9bcd-5dbb-89ca-df454bd11cf6", "Joseph J Tully"),
    12: ("d28301f9-8700-5685-8cbc-6f08462b0663", "Susan Tully"),
    13: ("93e7815f-bcb2-5a0e-88a2-da7233aab883", "Barney R Tumbiolo"),
    14: ("384228de-0f41-53e7-8405-f4fbe2000c17", "John W Tumbridge"),
    15: ("b2afe78f-52cc-56de-88f7-87f6014ba057", "Harry T Tun"),
    16: ("5bef741a-256e-5848-b824-0147cb9c6653", "Chen Dao Tung"),
    17: ("4fbbb540-7cbd-5a56-884c-679d4a06c62b", "Annis L Tunis"),
    18: ("39fcc188-1258-510e-b442-d0cb0828d3b0", "Bill K Tunnel"),
    19: ("1a7c8fa9-a745-57e2-8fcf-367d049b5318", "Edwin D Tunnell"),
    20: ("3cfe62b7-af17-5849-b5d9-0e966470945d", "Frederick H Tunnell"),
    21: ("cdde1d60-e611-5f8b-83c3-b6cb604755c5", "Anthony Turano"),
    22: ("cdd69d6f-4836-54d4-ad47-bb2001257b3d", "Carmen Turco"),
    23: ("f58e7cd0-d5c2-57b8-b186-31809a186ffc", "Euclide Turcotte"),
}


ARMY_OCCUPATIONS = [
    {
        "row": 1,
        "date": "1942-08-24",
        "code": "606",
        "occupation": "Semiskilled occupations in processing dairy products",
        "public_occupation": "semiskilled worker in dairy-products processing",
        "locator": "PDF physical page 173; historical category 6-06",
        "identity": "confirmed",
        "identity_note": "The exact nonshared protected identifier connects the index and official Army row; a declassified Detachment 101 order independently prints Gaston E. Tuggle with the same identifier and sergeant rank.",
        "identity_sources": [DET101_TUGGLE],
        "temporal_basis": "documented_prewar",
    },
    {
        "row": 2,
        "date": "1943-01-28",
        "code": "788",
        "occupation": "Warehousing, storekeeping, handling, loading, unloading, and related occupations",
        "public_occupation": "warehousing, storekeeping, handling, loading or unloading worker",
        "locator": "PDF physical page 174; historical category 7-88",
        "identity": "high_confidence",
        "identity_note": "An exact full name and nonshared protected identifier connect the index row to the reviewed official Army row.",
        "identity_sources": [],
        "temporal_basis": "documented_prewar",
    },
    {
        "row": 8,
        "date": "1943-07-13",
        "code": "736",
        "occupation": "Chauffeurs and drivers, bus, taxi, truck, and tractor",
        "public_occupation": "chauffeur or driver of a bus, taxi, truck or tractor",
        "locator": "PDF physical page 174; historical category 7-36",
        "identity": "high_confidence",
        "identity_note": "The official Army row prints the exact indexed name Robert E Tulley and the shared protected identifier. The neighboring Robt E Tullen row remains separate and conflicting; no merge is made.",
        "identity_sources": [],
        "temporal_basis": "documented_prewar",
    },
    {
        "row": 11,
        "date": "1943-07-22",
        "code": "992",
        "occupation": "Students",
        "public_occupation": "student",
        "locator": "PDF physical page 304; corrected historical category 9-92",
        "identity": "high_confidence",
        "identity_note": "The exact nonshared protected identifier connects the index and official Army row; a National Park Service history independently identifies Corporal Joseph J. Tully as an OSS Area C cadre member.",
        "identity_sources": [NPS_TULLY],
        "temporal_basis": "documented_prewar",
    },
    {
        "row": 13,
        "date": "1943-05-18",
        "code": "757",
        "occupation": "Occupations in laundering, cleaning, dyeing, and pressing apparel and other articles",
        "public_occupation": "laundering, cleaning, dyeing or apparel-pressing worker",
        "locator": "PDF physical page 174; historical category 7-57",
        "identity": "high_confidence",
        "identity_note": "An exact full name and nonshared protected identifier connect the index row to the reviewed official Army row.",
        "identity_sources": [],
        "temporal_basis": "documented_prewar",
    },
    {
        "row": 20,
        "date": "1945-07-24",
        "code": "136",
        "occupation": "Statistical clerks and compilers",
        "public_occupation": "statistical clerk or compiler",
        "locator": "PDF physical pages 171 and 304; historical category 1-36",
        "identity": "high_confidence",
        "identity_note": "The nonshared protected identifier connects Frederick H Tunnell to the official Army spelling Frederic H Tunnell Jr; the spelling and suffix difference remain visible as variants.",
        "identity_sources": [],
        "temporal_basis": "temporal_relation_uncertain",
        "variants": ["Frederic H Tunnell Jr"],
    },
    {
        "row": 23,
        "date": "1943-04-23",
        "code": "619",
        "occupation": "Semiskilled occupations in manufacture of textiles, not elsewhere classified",
        "public_occupation": "semiskilled textile-manufacturing worker, not elsewhere classified",
        "locator": "PDF physical page 173; historical category 6-19",
        "identity": "high_confidence",
        "identity_note": "An exact full name and nonshared protected identifier connect the index row to the reviewed official Army row.",
        "identity_sources": [],
        "temporal_basis": "documented_prewar",
    },
]


IDENTITY_ONLY = {
    3: {
        "date": "1942-06-27",
        "identity": "high_confidence",
        "note": "An exact full name and nonshared protected identifier connect the index row to the reviewed official Army row. Historical code 999 supplies no safely decoded civilian occupation.",
        "variants": [],
    },
    6: {
        "date": "1946-04-02",
        "identity": "high_confidence",
        "note": "An exact full name and nonshared protected identifier connect the index row to the reviewed official Army row. The 1946 date is post-OSS and code 274 is not safely decoded, so nothing is projected backward as a pre-OSS occupation.",
        "variants": [],
    },
    19: {
        "date": "1942-04-27",
        "identity": "high_confidence",
        "note": "An exact full name and nonshared protected identifier connect the index row to the reviewed official Army row. Historical code 999 supplies no safely decoded civilian occupation.",
        "variants": [],
    },
}


UNRESOLVED = {
    5: "Discovery-only genealogy suggested a 1923-1979 namesake, but no source connected that person to OSS or established a dated occupation.",
    9: "The common name produced multiple namesakes and no source supplied two corroborating identifiers beyond the name.",
    10: "Exact-name, initial, OSS, occupation, obituary and archival searches produced no defensible identity bridge.",
    12: "The name-only searches produced multiple plausible namesakes without a second identifier or dated OSS context.",
    14: "An older Brooklyn engineer and public official with the exact name was rejected because no evidence ties him to this OSS index row.",
    15: "Exact-name, spacing and transliteration variants in official, obituary, institutional and archival searches produced no reliable identity bridge.",
    16: "Chinese-name order and transliteration variants were searched, but no source tied a candidate to OSS, Box 789 or another corroborating identifier.",
    17: "Exact-name, initial, employer, obituary, newspaper and archival searches produced no defensible identity bridge.",
    18: "Exact-name, Tunnel/Tunnell variants, employer, obituary and archival searches produced no defensible identity bridge.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 788-789",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 475, rows 1-23; checked against layout-preserving text and a 200 dpi page render",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. Protected identifiers remain private.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; ten accepted and one rejected Batch 969 identity comparisons; protected identifiers and record ordinals withheld",
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
            "locator": "PDF physical pages 171-174 and corrected page 304; seven Batch 969 categories visually and textually checked",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical categories identify neither employers nor workplaces and are retained only where needed for auditability.",
        },
        {
            "key": DET101_TUGGLE,
            "stable_url": "https://www.javadc.org/java/docs/1945-03-15%20OSSSU%20Detachment%20101%20Promotions%20and%20Citations%20OCR%20P11_MA.pdf",
            "archival_identifier": "Headquarters Northern Combat Area Command, General Orders No. 6; extract in OSS SU Detachment 101 records",
            "title": "Promotions and Citations Report, Detachment 101",
            "author_creator": "Headquarters, OSS Special Unit Detachment 101",
            "repository_publisher": "Japanese American Veterans Association digital archive",
            "publication_record_date": "1945-05-15; attached order 1945-04-10",
            "locator": "PDF page 11, Combat Infantryman Badge extract; Sgt. Gaston E. Tuggle, effective 1944-01-01; protected identifier withheld",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "OSS Detachment 101 records",
            "rights_notes": "Direct declassified official document facsimile; the public claim omits the full service number.",
        },
        {
            "key": NPS_TULLY,
            "stable_url": "https://www.nps.gov/articles/transforming-prince-william-forest-park-into-military-camps.htm",
            "title": "Transforming Prince William Forest Park into Military Camps",
            "author_creator": "John Whiteclay Chambers II",
            "repository_publisher": "National Park Service",
            "publication_record_date": None,
            "locator": "Communications School, Area C section; Corporal Joseph J. Tully, Area C cadre, November 1944-October 1945; note 134",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "OSS Training in the National Parks and Service Abroad in World War II",
        },
        {
            "key": TURANO_OBIT,
            "stable_url": "https://www.legacy.com/us/obituaries/nytimes/name/anthony-turano-obituary?id=33949891",
            "title": "Anthony Turano Obituary",
            "author_creator": None,
            "repository_publisher": "The New York Times via Legacy.com",
            "publication_record_date": "2010-02-19 to 2010-02-20",
            "locator": "Obituary; OSS service, major rank and resumption of a commercial-photography career",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "The New York Times obituaries",
            "rights_notes": "Only a short excerpt and project-authored paraphrases are retained.",
        },
        {
            "key": PERSICO,
            "stable_url": "https://oac.cdlib.org/findaid/ark:/13030/tf0d5n97c1/",
            "archival_identifier": "Hoover Institution Library & Archives collection 81137",
            "title": "Joseph E. Persico papers, 1943-1980",
            "author_creator": "Joseph E. Persico; finding aid by Hoover Institution Library and Archives staff",
            "repository_publisher": "Hoover Institution Library & Archives",
            "publication_record_date": "Finding aid encoded 2024-05-01",
            "locator": "Box 5, tape 11; interview recording with Nam de Beaufort and Anthony Turano; research for Piercing the Reich",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Joseph E. Persico papers",
        },
        {
            "key": OSSOG_TURCO,
            "stable_url": "https://ossog.info/personnel.html",
            "title": "OSS Operational Groups Personnel",
            "author_creator": "OSS Operational Groups veterans history project",
            "repository_publisher": "OSS Operational Groups",
            "publication_record_date": None,
            "locator": "Italian Operational Groups roster; Peedee team; S/Sgt. Carmen Turco",
            "access_date": "2026-10-30",
            "source_quality": "D_correlative_or_secondary",
            "collection_name": "OSS Operational Groups personnel roster",
            "rights_notes": "Used only for a qualified identity and OSS-assignment lead, not to infer pre-OSS employment.",
        },
        {
            "key": NARA_TULARAK,
            "stable_url": "https://www.archives.gov/iwg/declassified-records/rg-226-oss/entry-210.pdf",
            "archival_identifier": "RG 226, Entry 210, WN#13644",
            "title": "Records of the Office of Strategic Services, Entry 210",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": None,
            "locator": "Translation of a letter from Thai leader Sanguan Tularak, 1944-09-05, WN#13644",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
        },
        {
            "key": REYNOLDS_TULARAK,
            "stable_url": "https://assets.cambridge.org/97805218/36012/frontmatter/9780521836012_frontmatter.pdf",
            "title": "Thailand's Secret War: The Free Thai, OSS, and SOE During World War II",
            "author_creator": "E. Bruce Reynolds",
            "repository_publisher": "Cambridge University Press",
            "publication_record_date": "2005",
            "locator": "Front matter, illustration 7; Sanguan Tularak training for OSS DURIAN at Trincomalee, Ceylon",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Thailand's Secret War",
            "rights_notes": "Used only to document the unbridged Sanguan Tularak lead; no copyrighted image is republished.",
        },
    ]


def occupation_affiliation(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    return {
        "key": f"{slug(PEOPLE[row][1])}-occupation-b969",
        "person_id": PEOPLE[row][0],
        "occupation": item["public_occupation"],
        "relationship_type": "student" if item["code"] == "992" else "unknown",
        "end_date": item["date"],
        "date_precision": f"Historical civilian-status code {item['code']} was recorded at Army entry on {item['date']}; no employer, school, workplace or OSS-transfer date is named.",
        "country": "United States",
        "immediate_pre_oss": False,
        "last_civilian_pre_service": False,
        "pre_oss_temporal_basis": item["temporal_basis"],
        "identity_confidence": item["identity"],
        "claim_confidence": "medium",
        "source_quality": "A_direct_official",
        "publication_status": "publish_qualified",
        "research_notes": "The historical category is not converted into a named employer, school, workplace or immediate pre-OSS affiliation.",
    }


def affiliations() -> list[dict[str, object]]:
    values = [occupation_affiliation(item) for item in ARMY_OCCUPATIONS]
    values.append(
        {
            "key": "anthony-turano-commercial-photographer-b969",
            "person_id": PEOPLE[21][0],
            "occupation": "commercial photographer",
            "relationship_type": "unknown",
            "date_precision": "The obituary says Turano resumed his commercial-photography career after wartime OSS service; it does not identify the prewar employer, dates or employment arrangement.",
            "city": "New York City",
            "state_or_region": "New York",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "high_confidence",
            "claim_confidence": "medium",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "publish_qualified",
            "research_notes": "Occupation only. Anton Bruehl is not named as Turano's prewar employer, so the studio is not projected backward.",
        }
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
    evidence_excerpt: str | None = None,
) -> dict[str, object]:
    value: dict[str, object] = {
        "key": key,
        "person_id": PEOPLE[row][0],
        "claim_type": claim_type,
        "claim_text": claim_text,
        "evidence_excerpt": evidence_excerpt,
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


def army_claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for item in ARMY_OCCUPATIONS:
        row = int(item["row"])
        name = PEOPLE[row][1]
        identity_sources = [{"source_key": INDEX}, {"source_key": ARMY}]
        identity_sources.extend({"source_key": key} for key in item["identity_sources"])
        identity_confidence = "confirmed" if item["identity"] == "confirmed" else "high"
        values.append(
            claim(
                row,
                f"identity-{slug(name)}-b969",
                "identity",
                f"Indexed {name} is {item['identity'].replace('_', '-')} matched to the reviewed Army entry.",
                item["identity_note"],
                item["identity_note"],
                "The Army entry date establishes military-entry chronology but not the exact OSS transfer date.",
                "A_direct_official",
                identity_confidence,
                identity_sources,
                "Protected identifiers were used only for private resolution and remain absent from the evidence bundle and public output.",
            )
        )
        values.append(
            claim(
                row,
                f"occupation-{slug(name)}-b969",
                "other_pre_oss_affiliation" if item["code"] == "992" else "occupation",
                f"At Army entry on {item['date']}, {name}'s historical civilian-status category was {item['occupation'].lower()}.",
                f"The official Army field carries historical code {item['code']}; NARA's code list defines it as {item['occupation']}.",
                item["identity_note"],
                (
                    "The 1945 Army-entry date is close to the end of OSS and its relation to OSS service is uncertain; no employer is named."
                    if item["temporal_basis"] == "temporal_relation_uncertain"
                    else "Dated at Army entry before the later OSS-index context; no employer, school, workplace or exact OSS-transfer date is named."
                ),
                "A_direct_official",
                "medium",
                [
                    {"source_key": ARMY, "locator_override": "Accepted identity bridge; protected identifier and raw record withheld"},
                    {"source_key": TECH, "locator_override": "PDF physical pages 44-46; civilian-occupation field"},
                    {"source_key": CODES, "locator_override": item["locator"]},
                ],
                "Published as qualified occupation or student status only; excluded from verified-employer analytics.",
                f"{slug(name)}-occupation-b969",
                "publish_qualified",
            )
        )

    for row, item in IDENTITY_ONLY.items():
        name = PEOPLE[row][1]
        values.append(
            claim(
                row,
                f"identity-{slug(name)}-b969",
                "identity",
                f"Indexed {name} is high-confidence matched to a reviewed official Army record.",
                item["note"],
                item["note"],
                f"The official Army entry date is {item['date']}; it does not establish a usable pre-OSS occupation.",
                "A_direct_official",
                "high",
                [{"source_key": INDEX}, {"source_key": ARMY}, {"source_key": TECH}],
                "Identity evidence only; no employer or occupation is inferred from undecoded or unusable historical code data.",
            )
        )
    return values


def specialist_claims() -> list[dict[str, object]]:
    return [
        claim(
            7,
            "identity-conflict-robt-tullen-b969",
            "identity",
            "The indexed Robt E Tullen row remains in an unresolved identity conflict with the separately indexed Robert E Tulley row.",
            "Both index rows carry the same protected identifier, while the official Army row prints Robert E Tulley. The two source rows remain separate and are not merged.",
            "Conflicting name evidence on a shared protected identifier; physical-file review is required.",
            "The conflict prevents publication of a pre-OSS occupation for Robt E Tullen.",
            "A_direct_official",
            "conflicting",
            [{"source_key": INDEX}, {"source_key": ARMY}],
            "The full identifier is withheld. This conflict is visible and excluded from default analytics.",
            publication_status="conflicting",
        ),
        claim(
            4,
            "sanguan-tularak-unbridged-lead-b969",
            "identity",
            "Indexed Sam Tularak may be related to the well-documented Sanguan Tularak OSS/Free Thai record, but the identity is not established.",
            "NARA records and a scholarly OSS history document Sanguan Tularak, while no reviewed source equates the indexed forename Sam with Sanguan.",
            "Name and OSS context are suggestive, but no alias, identifier, box-file or second biographical bridge was found.",
            "No employment chronology is assigned to the indexed person while identity remains ambiguous.",
            "A_direct_official",
            "low",
            [{"source_key": INDEX}, {"source_key": NARA_TULARAK}, {"source_key": REYNOLDS_TULARAK}],
            "Retained as a private review lead and withheld from public facts and analytics.",
            publication_status="withheld_low_confidence",
        ),
        claim(
            21,
            "identity-anthony-turano-b969",
            "identity",
            "Indexed Anthony Turano is a high-confidence match to commercial photographer and OSS veteran Anthony (Tony) Turano.",
            "The obituary explicitly connects the exact name to OSS service and Piercing the Reich; the Persico papers list an Anthony Turano interview used for that book.",
            "High confidence from the uncommon exact name, explicit OSS statement and independent Persico archival interview pointer.",
            "The obituary documents prewar occupation by describing his postwar return to the same career, but does not name a prewar employer.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": INDEX}, {"source_key": TURANO_OBIT}, {"source_key": PERSICO}],
            "The later Anton Bruehl studio relationship is not projected backward without dated evidence.",
        ),
        claim(
            21,
            "prewar-anthony-turano-photographer-b969",
            "occupation",
            "Anthony Turano worked as a commercial photographer before wartime OSS service; the prewar employer is not identified.",
            "His obituary says he resumed his commercial-photography career after OSS service, establishing the occupation before the interruption of wartime service.",
            "High-confidence identity based on explicit OSS obituary evidence and the Persico archival interview pointer.",
            "Documented prewar occupation, but neither immediacy nor a named employer is established.",
            "C_reputable_contemporary_or_scholarly",
            "medium",
            [{"source_key": TURANO_OBIT, "excerpt_override": "before resuming his career as a commercial photographer in New York City"}],
            "Occupation only; Anton Bruehl is not identified as the prewar employer.",
            "anthony-turano-commercial-photographer-b969",
            "publish_qualified",
        ),
        claim(
            22,
            "identity-carmen-turco-b969",
            "identity",
            "Indexed Carmen Turco is a probable match to Staff Sergeant Carmen Turco of the OSS Peedee Italian Operational Group.",
            "The veterans roster supplies the exact name, staff-sergeant rank and Peedee assignment, but no service number or second person-specific identifier.",
            "Probable exact-name match in direct OSS context; Box 789 must confirm the identity.",
            "The source documents an OSS assignment, not a pre-OSS employer or occupation.",
            "D_correlative_or_secondary",
            "medium",
            [{"source_key": INDEX}, {"source_key": OSSOG_TURCO, "excerpt_override": "S/Sgt. Carmen Turco"}],
            "Published only as a qualified identity lead; excluded from verified-employer analytics.",
            publication_status="publish_qualified",
        ),
    ]


def claims() -> list[dict[str, object]]:
    return army_claims() + specialist_claims()


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
    values = [
        base_update(
            row,
            identity_status="unresolved",
            identity_evidence=f"The visually verified index row supplies {PEOPLE[row][1]}, Box {'788' if row <= 12 else '789'} and archive location 230/86/42/03. {reason}",
            personnel_category="unknown_or_indeterminate",
            commissioned_officer=None,
            allied_or_foreign_personnel=None,
            research_status="requires_archival_review",
            next_action=f"Review the indexed personnel file for corroborating identifiers, immediate pre-OSS affiliation and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}",
        )
        for row, reason in UNRESOLVED.items()
    ]

    for item in ARMY_OCCUPATIONS:
        row = int(item["row"])
        variants = item.get("variants")
        values.append(
            base_update(
                row,
                identity_status=item["identity"],
                identity_evidence=item["identity_note"],
                name_variants=variants if variants else None,
                personnel_category="enlisted_army_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                possible_duplicate_group=("serial-conflict:33691027" if row == 8 else None),
                research_status="occupation_only_found",
                next_action=(
                    "Review Box 788 to determine whether the neighboring Tullen row is a transcription variant or a distinct person, then establish the immediate pre-OSS affiliation and named last civilian employer."
                    if row == 8
                    else "Review the indexed personnel file to establish the immediate pre-OSS affiliation and named last civilian employer; do not convert the Army occupation category into a workplace."
                ),
            )
        )

    for row, item in IDENTITY_ONLY.items():
        values.append(
            base_update(
                row,
                identity_status=item["identity"],
                identity_evidence=item["note"],
                name_variants=item["variants"] or None,
                personnel_category="enlisted_army_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                research_status="requires_archival_review",
                next_action="Review the indexed personnel file to establish the immediate pre-OSS affiliation and last civilian employer; no usable historical occupation category was established.",
            )
        )

    values.extend(
        [
            base_update(4, identity_status="ambiguous", identity_evidence="The indexed forename Sam and the documented Thai leader Sanguan Tularak share a rare surname and OSS context, but no reviewed source establishes an alias or direct identity bridge.", personnel_category="unknown_or_indeterminate", commissioned_officer=None, allied_or_foreign_personnel=None, research_status="requires_archival_review", next_action="Review Box 788 to determine whether Sam Tularak is Sanguan Tularak or another person before assigning any Thai government, Free Thai or tobacco-monopoly affiliation."),
            base_update(7, identity_status="conflicting", identity_evidence="The protected identifier is printed on both this Robt E Tullen row and a separate Robert E Tulley row; the official Army row prints Robert E Tulley. Both index rows remain separate.", personnel_category="unknown_or_indeterminate", commissioned_officer=None, allied_or_foreign_personnel=None, possible_duplicate_group="serial-conflict:33691027", research_status="conflicting_sources", next_action="Review Box 788 and the original file label to determine whether Tullen is a transcription variant, a duplicate index row or a distinct person. Do not merge with Robert E Tulley without direct evidence."),
            base_update(21, identity_status="high_confidence", identity_evidence="A New York Times obituary explicitly links Anthony (Tony) Turano to OSS service and Piercing the Reich; the Persico papers independently list an Anthony Turano interview used for that book.", name_variants=["Anthony (Tony) Turano", "Tony Turano"], personnel_category="unknown_or_indeterminate", commissioned_officer=True, allied_or_foreign_personnel=False, research_status="occupation_only_found", next_action="Review Box 789 and the Persico interview to identify Turano's immediate pre-OSS affiliation and determine whether Anton Bruehl's studio employed him before the war."),
            base_update(22, identity_status="probable", identity_evidence="An OSS Operational Groups roster lists the exact name as Staff Sergeant Carmen Turco on the Peedee team, but supplies no protected identifier or second person-specific bridge.", personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="requires_archival_review", next_action="Review Box 789 to confirm the Peedee identity and establish the immediate pre-OSS affiliation and last civilian employer."),
        ]
    )
    return values


def research_attempts() -> list[dict[str, object]]:
    source_review_rows = {1, 2, 3, 4, 6, 7, 8, 11, 13, 19, 20, 21, 22, 23}
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        if row in source_review_rows:
            outcome = "candidate_rejected" if row == 4 else "source_reviewed"
            reviewed = 7 if row in {1, 4, 11, 21, 22} else 5
            rejected = 5
            detail = "Reviewed official, institutional, contemporary or archival evidence produced the identity, occupation, student, conflict or qualified-candidate outcome recorded in the evidence bundle."
        else:
            outcome = "no_result"
            reviewed = 6
            rejected = 6
            detail = UNRESOLVED[row]
        attempts.append(
            {
                "key": f"page475-row{row}-{slug(name)}-b969",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index and official Archives context; CIA Reading Room or equivalent official-source check; exact-name and meaningful variants; OSS, Army, rank and unit clues; employer and occupation 1940; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Boxes 788-789; protected identifiers used only when defensible",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_969",
                "started_at": "2026-10-30T03:10:00Z",
                "completed_at": "2026-10-30T05:05:00Z",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search snippets, unsourced genealogy, people-finder pages, postwar-only employment leads and sources without an OSS, protected-identifier or personnel-file bridge were rejected. Historical occupation codes, military service and student status were not silently converted into employers.",
                "research_notes": f"{detail} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain, CIA Reading Room-equivalent and Library of Congress searches were checked as applicable. The index page, Army bulk file, technical documentation and occupation-code pages were inspected directly. The Sam/Sanguan Tularak lead remains unbridged and withheld; the Tullen/Tulley conflict remains visible. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": f"Review the indexed Box {'788' if row <= 12 else '789'} personnel file for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before wartime service.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b969-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-969-v1",
        "reviewer": "Before OSS Batch 969 evidence review",
        "sources": sources(),
        "organizations": [],
        "affiliations": affiliations(),
        "claims": claims(),
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }
    EvidenceBundle.model_validate(bundle)
    OUTPUT.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
