#!/usr/bin/env python3
"""Generate the reviewed Batch 947 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page464-marcelen-j-tezak-to-milton-theaman-"
    "review_batch-947_2026-10-28.json"
)

INDEX = "nara-index-b947"
ARMY = "army-bulk-b947"
TECH = "army-tech-b947"
CODES = "army-codes-b947"
STATE_THAYER = "state-history-thayer-b947"
FRUS_THAYER = "frus-thayer-b947"
GAZETTE_THACKTHWAITE = "london-gazette-thackthwaite-b947"
MUSEUM_THACKTHWAITE = "resistance-museum-thackthwaite-b947"
MUSEUM_PERSON_THACKTHWAITE = "resistance-museum-person-thackthwaite-b947"
MVR_THACKTHWAITE = "mvr-thackthwaite-b947"
ASSESSMENT_THEAMAN = "assessment-staff-theaman-b947"

STATE = "department-of-state-b947"
SOE = "special-operations-executive-b947"
RASC = "royal-army-service-corps-b947"


PEOPLE = {
    1: ("f9f222b7-721e-54fc-9bcd-e22ad431a59f", "Marcelen J Tezak"),
    2: ("d2783d4b-fe3b-560d-b190-f6f84e6de449", "William M Thabit"),
    3: ("4c53ed20-1ce2-507d-a269-34b4bd9eb7ca", "Vera L Thacher"),
    4: ("a29532d6-9a7c-5f1e-b629-13b2e5b7b5ab", "Henry H Thackthwaite"),
    5: ("403f4110-6b65-5ad9-9953-88cc025cc06e", "Shelby Thames"),
    6: ("99367b41-0a3e-5c62-aef5-3104871326bd", "Travis H Thames"),
    7: ("0cd1511a-436c-5194-8cb8-8fc06f3704f2", "Spiro Thanas"),
    8: ("1c92d07c-cd55-5e30-b2a4-e08d875b4053", "William J Thanos"),
    9: ("d8530779-7a9c-5320-b4f7-3da486e87dc4", "William Thanos"),
    10: ("192eba0d-f4e2-5312-94bf-0296d77898ef", "Melvin E Tharp"),
    11: ("7d9b1c4a-da89-520e-8cbf-5f710df54b6a", "Melvin E Tharp"),
    12: ("b07b5eb3-e214-51be-bf1f-74bab9fcec48", "Robert E Tharp"),
    13: ("bb719215-673f-594d-a912-d2b97c02d1b0", "William G Tharp"),
    14: ("a6b1e854-e46e-504a-8d46-fca99c2da9fc", "Kathryn L Tharpe"),
    15: ("642defc6-04d1-5ac0-9662-e4a5c22454ff", "Herbert S Thatcher"),
    16: ("289cb16a-9b6f-5f3b-a998-3d93b87d9cd2", "Charles W Thayer"),
    17: ("41a0b4c5-ff81-52f7-ae21-5bbaf74742ab", "Frank A Thayer"),
    18: ("b925f995-0e43-5318-b36c-83627a67fe75", "Guy V Thayer"),
    19: ("11cb30b6-b205-5398-951d-25b488c3ca42", "John O Thayer"),
    20: ("c802b855-fe16-54cc-b66b-ddc1df2d6aaa", "William F Thayer"),
    21: ("2865eae8-783c-5524-849e-5c4f981cf01f", "William A Thayer"),
    22: ("85cf7aaf-41bb-520b-9b90-3eb782d0c1df", "William A Thayer"),
    23: ("748e62ad-1fcb-57da-9267-515ca36220c8", "Milton Theaman"),
}


ARMY_RECORDS = [
    {
        "row": 1,
        "date": "1940-09-19",
        "code": "999",
        "occupation": None,
        "public_occupation": None,
        "locator": None,
    },
    {
        "row": 6,
        "date": "1943-02-23",
        "code": "306",
        "occupation": "General farmers",
        "public_occupation": "general farmer",
        "locator": "PDF physical page 172; historical category 3-06",
    },
    {
        "row": 7,
        "date": "1943-08-31",
        "code": "513",
        "occupation": "Skilled occupations in manufacture of miscellaneous products",
        "public_occupation": "skilled occupation in manufacture of miscellaneous products",
        "locator": "PDF physical page 174; historical category 5-13",
    },
    {
        "row": 8,
        "date": "1943-06-08",
        "code": "992",
        "occupation": "Students",
        "public_occupation": "student",
        "locator": "PDF physical page 304; amended historical category 9-92",
        "relationship": "student",
    },
    {
        "row": 11,
        "date": "1943-02-13",
        "code": "097",
        "occupation": "Managers and officials, n.e.c.",
        "public_occupation": "manager or official, not elsewhere classified",
        "locator": "PDF physical page 171; historical category 0-97",
    },
    {
        "row": 17,
        "date": "1943-03-13",
        "code": "433",
        "occupation": "Skilled general woodworking occupations, n.e.c.",
        "public_occupation": "skilled general woodworking occupation, not elsewhere classified",
        "locator": "PDF physical page 173; historical category 4-33",
        "name_variant": "Frank A Thayer Jr",
    },
    {
        "row": 20,
        "date": "1942-08-05",
        "code": "402",
        "occupation": "Skilled occupations in production of bakery products, n.e.c.",
        "public_occupation": "skilled bakery-production occupation, not elsewhere classified",
        "locator": "PDF physical page 173; historical category 4-02",
        "name_variant": "William F Thayer Jr",
    },
    {
        "row": 22,
        "date": "1942-01-12",
        "code": "688",
        "occupation": "Semiskilled occupations in mechanical treatment of metals, n.e.c.",
        "public_occupation": "semiskilled mechanical metal-treatment occupation, not elsewhere classified",
        "locator": "PDF physical page 174; historical category 6-88",
    },
]


UNRESOLVED = {
    2: "Exact-name and meaningful-variant searches produced only the index and unbridged genealogy or namesake leads.",
    3: "Exact-name and Thacher/Thatcher variant searches found no official, institutional or contemporary source connecting this row to OSS or a pre-OSS affiliation.",
    5: "Searches returned unrelated later people and unbridged genealogy leads; none matched the index identifiers or Box 770 context.",
    12: "Several same-name military and obituary candidates lacked the private identifier, OSS context and a second corroborating identifier.",
    13: "Common-name military and directory candidates could not be connected to the indexed officer-style row or Box 771.",
    14: "Exact-name, obituary, institutional, directory and archival searches did not produce a reliable OSS identity or employer bridge.",
    15: "A 1940 labor-law attorney named Herbert S. Thatcher is a plausible lead, but no source connects him to OSS, Box 771 or another indexed identifier.",
    18: "An unverified genealogy lead and several namesakes lacked an OSS, Box 771 or protected-identifier bridge.",
    19: "A same-name Massachusetts man and directory leads lacked an OSS, Box 771 or protected-identifier bridge and were rejected.",
}


DUPLICATES = {
    8: "william-thanos-page464-rows8-9-b947",
    9: "william-thanos-page464-rows8-9-b947",
    10: "melvin-e-tharp-page464-rows10-11-b947",
    11: "melvin-e-tharp-page464-rows10-11-b947",
    21: "william-a-thayer-page464-rows21-22-b947",
    22: "william-a-thayer-page464-rows21-22-b947",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 770-771",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 464, rows 1-23; checked against layout-preserving text and a 300 dpi page render",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. The adjacent Thanos, Melvin E. Tharp and William A. Thayer rows remain unmerged. Costas A. Theodorou at row 24 was visually checked as the next boundary. Full protected identifiers remain private.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; nine reviewed Batch 947 candidates; protected identifiers withheld",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "No raw bulk row or full protected identifier is retained in public assets. Eight exact or suffix-variant identities were accepted. One unrelated Hucal record sharing William A. Thayer's private identifier was rejected as a direct name conflict. Code 999 is not interpreted or published.",
        },
        {
            "key": TECH,
            "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf",
            "archival_identifier": "NN3-064-03-008; National Archives Identifier 1263923",
            "title": "World War II Army Enlistment Records: Reference Copy of Technical Documentation",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives at College Park - Electronic Records",
            "publication_record_date": "1994-2005; reference copy modified 2011",
            "locator": "PDF physical pages 44-46; identifier, name, Army-entry-date, grade and civilian-occupation fields",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Used to interpret selected fields only; source damage, coding limits and incomplete coverage remain applicable.",
        },
        {
            "key": CODES,
            "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1CL_SD.pdf",
            "archival_identifier": "National Archives Identifier 1263923; Code No. 30",
            "title": "NARA Compiled Code Lists for the Electronic Army Serial Number Merged File",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives at College Park - Electronic Records",
            "publication_record_date": "2011-01-12; modified 2011-03-17",
            "locator": "PDF physical pages 171-174 and 304; reviewed historical categories 0-97, 3-06, 4-02, 4-33, 5-13, 6-88 and 9-92",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "All relevant pages were rendered and visually inspected. Students is status, not employment. Other historical labels are qualified and never converted into named employers.",
        },
        {
            "key": STATE_THAYER,
            "stable_url": "https://history.state.gov/departmenthistory/people/thayer-charles-wheeler",
            "title": "Charles Wheeler Thayer (1910-1969)",
            "author_creator": "Office of the Historian",
            "repository_publisher": "United States Department of State",
            "locator": "People directory entry; Career Foreign Service Officer; Afghanistan service through July 2, 1942",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "Department History: People",
            "rights_notes": "This official page supplies the expanded middle name, career Foreign Service status and dated Afghanistan assignment. It does not state an OSS transfer date.",
        },
        {
            "key": FRUS_THAYER,
            "stable_url": "https://history.state.gov/historicaldocuments/frus1944v04/d1312",
            "archival_identifier": "Foreign Relations of the United States, 1944, Volume IV, document 1312",
            "title": "Report by Major Charles W. Thayer of the Independent American Military Mission to Marshal Tito",
            "author_creator": "Charles W. Thayer",
            "repository_publisher": "Office of the Historian, United States Department of State",
            "publication_record_date": "1944-11-04",
            "locator": "Document 1312 and editor's footnote 91",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "Foreign Relations of the United States",
            "rights_notes": "The document identifies Thayer as a U.S. Army major leading the mission; the editorial note calls him a former Foreign Service Officer. It supports chronology but not an exact OSS transfer date.",
        },
        {
            "key": GAZETTE_THACKTHWAITE,
            "stable_url": "https://www.thegazette.co.uk/London/issue/37909/supplement/1313/data.pdf",
            "archival_identifier": "The London Gazette, issue 37909, supplement, page 1313",
            "title": "The London Gazette: Foreign Decorations",
            "author_creator": "Central Chancery of the Orders of Knighthood",
            "repository_publisher": "The London Gazette",
            "publication_record_date": "1947-03-20",
            "locator": "Supplement page 1313; Henry Hopkinson Augustus Thackthwaite, Royal Army Service Corps",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "Official public record of the United Kingdom",
            "rights_notes": "The official notice supplies Thackthwaite's expanded name, acting-major status and Royal Army Service Corps affiliation. The printed service number is not reproduced publicly here.",
        },
        {
            "key": MUSEUM_THACKTHWAITE,
            "stable_url": "https://www.museedelaresistanceenligne.org/media7626-Avion-britannique-Halifax-B-Mark-II",
            "title": "Avion britannique Halifax B Mark II",
            "author_creator": "Fondation de la Resistance; Musee de la Resistance en ligne",
            "repository_publisher": "Musee de la Resistance en ligne",
            "locator": "Union mission narrative; Captain Henri Thackthwaite, alias Procureur",
            "access_date": "2026-10-28",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Musee de la Resistance en ligne",
            "rights_notes": "The institutional narrative identifies Thackthwaite as a British SOE member in the interallied Union mission with OSS officer Peter Ortiz and BCRA officer Camille Monnier.",
        },
        {
            "key": MUSEUM_PERSON_THACKTHWAITE,
            "stable_url": "https://www.museedelaresistanceenligne.org/personnedetail.php?id=31553",
            "title": "Henry Thackthwaite",
            "author_creator": "Fondation de la Resistance; Musee de la Resistance en ligne",
            "repository_publisher": "Musee de la Resistance en ligne",
            "locator": "Person entry; SOE Section RF; Union I mission, January 6-May 3, 1944",
            "access_date": "2026-10-28",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Musee de la Resistance en ligne",
            "rights_notes": "Used for mission dates and SOE section context. The entry is not treated as evidence that this British officer became a U.S. OSS employee.",
        },
        {
            "key": MVR_THACKTHWAITE,
            "stable_url": "https://mvr.asso.fr/thackthwaite/",
            "title": "Henry Hopkinson Augustus Thackthwaite, Procureur",
            "author_creator": "Memoire et Resistance en Vercors",
            "repository_publisher": "Memoire et Resistance en Vercors",
            "locator": "Biographical chronology; prewar translator and teacher; British Army and SOE service",
            "access_date": "2026-10-28",
            "source_quality": "D_correlative_or_secondary",
            "collection_name": "Biographical histories of the Resistance in the Vercors",
            "rights_notes": "Used as a qualified secondary chronology and occupation lead. It cites the 1939 register and official records but does not name a civilian employer.",
        },
        {
            "key": ASSESSMENT_THEAMAN,
            "stable_url": "https://wellcomecollection.org/works/z9va5p3c",
            "archival_identifier": "Wellcome Collection b32174317; Assessment of Men: Selection of Personnel for the Office of Strategic Services",
            "title": "Assessment of Men: Selection of Personnel for the Office of Strategic Services",
            "author_creator": "Office of Strategic Services Assessment Staff",
            "repository_publisher": "Rinehart and Company; digital copy hosted by Wellcome Collection",
            "publication_record_date": "1948",
            "locator": "Printed pages v-vi; IIIF images b32174317_0011.jp2 and b32174317_0012.jp2",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "Wellcome Collection digitized books",
            "rights_notes": "The original OSS staff roster prints Milton Theaman, M.S., 2nd Lt., station S. The preceding page defines S as Fairfax, Virginia and the dagger as final-research, composition or first-draft participation. No parenthetical pre-government institution is printed for him.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": STATE,
            "organization_id": "4d2fbb5f-218d-5445-b7b3-4c2fd22f0286",
            "canonical_name": "United States Department of State",
            "historical_name": "Department of State",
            "aliases": ["U.S. Department of State", "Foreign Service"],
            "organization_type": "federal government department",
            "sector": "federal_government",
            "country": "United States",
            "normalization_notes": "Existing Department of State organization reused. Charles W. Thayer's Foreign Service assignment is government service, not a private-sector employer.",
        },
        {
            "key": SOE,
            "organization_id": "b917eced-da73-5c67-8579-3fdacb16a31a",
            "canonical_name": "Special Operations Executive",
            "historical_name": "Special Operations Executive",
            "aliases": ["SOE", "SOE Section RF"],
            "organization_type": "British wartime government organization",
            "sector": "federal_government",
            "country": "United Kingdom",
            "active_dates": "1940-1946",
            "normalization_notes": "Existing organization reused. Henry Thackthwaite remained a British SOE officer serving in an interallied mission with OSS; the record does not recast him as a U.S. employee.",
        },
        {
            "key": RASC,
            "canonical_name": "Royal Army Service Corps",
            "historical_name": "Royal Army Service Corps",
            "aliases": ["RASC"],
            "organization_type": "British Army corps",
            "sector": "military",
            "country": "United Kingdom",
            "active_dates": "1888-1965",
            "normalization_notes": "Kept distinct from the Special Operations Executive. The official Gazette identifies Thackthwaite with the Royal Army Service Corps.",
        },
    ]


def army_affiliation(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    name = PEOPLE[row][1]
    is_student = item.get("relationship") == "student"
    return {
        "key": f"{slug(name)}-row{row}-occupation-b947",
        "person_id": PEOPLE[row][0],
        "occupation": item["public_occupation"],
        "relationship_type": "student" if is_student else "employment",
        "end_date": item["date"],
        "date_precision": f"Historical civilian-occupation code {item['code']} was recorded at Army entry on {item['date']}; no employer, school, workplace or OSS-transfer date is named.",
        "country": "United States",
        "immediate_pre_oss": False,
        "last_civilian_pre_service": False,
        "pre_oss_temporal_basis": "strongly_date_bounded",
        "identity_confidence": "high_confidence",
        "claim_confidence": "medium",
        "source_quality": "A_direct_official",
        "publication_status": "publish_qualified",
        "research_notes": "The historical category is not converted into a named employer, workplace, school, immediate affiliation or exact modern job title.",
    }


def affiliations() -> list[dict[str, object]]:
    values = [
        army_affiliation(item)
        for item in ARMY_RECORDS
        if item["public_occupation"] is not None
    ]
    values.extend(
        [
            {
                "key": "henry-thackthwaite-soe-b947",
                "person_id": PEOPLE[4][0],
                "organization_key": SOE,
                "organization_name_as_found": "British Special Operations Executive (SOE), Section RF",
                "role_title": "Captain; Union interallied mission member; alias Procureur",
                "relationship_type": "government_assignment",
                "start_date": "1944-01-06",
                "end_date": "1944-05-03",
                "date_precision": "Institutional Resistance Museum records place Captain Thackthwaite of SOE Section RF in the Union mission from January 6 to May 3, 1944, alongside OSS and BCRA officers.",
                "country": "United Kingdom and France",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "explicit_immediate",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "This is the best-supported source affiliation for his OSS-indexed interallied service. It does not imply that the British officer became a U.S. OSS employee.",
            },
            {
                "key": "henry-thackthwaite-rasc-b947",
                "person_id": PEOPLE[4][0],
                "organization_key": RASC,
                "organization_name_as_found": "Royal Army Service Corps",
                "role_title": "British Army officer; captain and later acting major",
                "relationship_type": "military_assignment",
                "start_date": "1939",
                "date_precision": "A qualified secondary chronology places him in the British Army in 1939 and detached to SOE in 1943-1944; the official Gazette confirms the expanded name, acting-major rank and Royal Army Service Corps affiliation.",
                "country": "United Kingdom",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "A_direct_official",
                "publication_status": "publish_qualified",
                "research_notes": "The 1939 start comes from the secondary chronology; the official Gazette independently establishes the exact person and corps.",
            },
            {
                "key": "henry-thackthwaite-occupation-b947",
                "person_id": PEOPLE[4][0],
                "occupation": "translator and teacher",
                "relationship_type": "employment",
                "end_date": "1939",
                "date_precision": "The secondary Vercors chronology describes prewar work as a translator and teacher but names no employer and gives no exact employment dates.",
                "country": "United Kingdom",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "D_correlative_or_secondary",
                "publication_status": "publish_qualified",
                "research_notes": "Occupation only. No school, translation agency or other employer is inferred.",
            },
            {
                "key": "charles-thayer-state-b947",
                "person_id": PEOPLE[16][0],
                "organization_key": STATE,
                "organization_name_as_found": "Foreign Service",
                "role_title": "Career Foreign Service officer; charge d'affaires ad interim in Afghanistan",
                "relationship_type": "government_assignment",
                "end_date": "1942-07-02",
                "date_precision": "The official State Department biography dates his Kabul charge assignment through July 2, 1942; by November 1944 an official FRUS document identifies him as a U.S. Army major and former Foreign Service Officer.",
                "country": "United States and Afghanistan",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "probable_immediate",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "A_direct_official",
                "publication_status": "publish_qualified",
                "research_notes": "State/Foreign Service is the best-supported predecessor affiliation, but the sources do not state the exact transfer date or exclude an intervening Army assignment.",
            },
        ]
    )
    return values


def claim(
    row: int,
    key: str,
    claim_type: str,
    claim_text: str,
    evidence_paraphrase: str,
    identity: str,
    temporal: str,
    source_quality: str,
    confidence: str,
    source_links: list[dict[str, object]],
    notes: str,
    affiliation_key: str | None = None,
    publication_status: str | None = None,
) -> dict[str, object]:
    return {
        "key": key,
        "person_id": PEOPLE[row][0],
        "affiliation_key": affiliation_key,
        "claim_type": claim_type,
        "claim_text": claim_text,
        "evidence_paraphrase": evidence_paraphrase,
        "identity_match_assessment": identity,
        "temporal_assessment": temporal,
        "source_quality": source_quality,
        "claim_confidence": confidence,
        "publication_status": publication_status
        or ("published" if confidence in {"confirmed", "high"} else "publish_qualified"),
        "match_notes": notes,
        "sources": source_links,
    }


def army_claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for item in ARMY_RECORDS:
        row = int(item["row"])
        name = PEOPLE[row][1]
        variant = item.get("name_variant")
        identity_paraphrase = (
            f"A nonshared protected identifier connects the visually verified index row to the official Army record, which prints the preserved suffix variant {variant}."
            if variant
            else "A nonshared protected identifier connects the visually verified index row to the official Army record, and the full name agrees exactly."
        )
        identity_assessment = (
            "High confidence from a private nonshared identifier, aligned full name and a documented Jr. suffix variant."
            if variant
            else "High confidence from a private nonshared identifier plus exact full-name agreement."
        )
        extra = ""
        if row == 22:
            extra = " A separate bulk record naming Hucal Julian S shared the private identifier but was explicitly rejected as a name conflict."
        values.append(
            claim(
                row,
                f"identity-{slug(name)}-row{row}-army-b947",
                "identity",
                f"Indexed {name} is a high-confidence match to the reviewed official Army entry.",
                identity_paraphrase + extra,
                identity_assessment,
                "Identity evidence only; the Army entry does not itself establish an OSS transfer date.",
                "A_direct_official",
                "high",
                [
                    {"source_key": INDEX, "locator_override": f"PDF page 464 row {row}; protected identifier withheld"},
                    {"source_key": ARMY, "locator_override": "Accepted reviewed identity bridge; protected identifier withheld"},
                ],
                "The review accepts identity only for the matching source row, preserves source spellings and does not expose the protected identifier.",
            )
        )
        if item["public_occupation"] is None:
            continue
        category = str(item["occupation"])
        if item.get("relationship") == "student":
            claim_text = f"At Army entry on {item['date']}, {name} was recorded in the historical Students category; no school or employer is identified."
        else:
            claim_text = f"At Army entry on {item['date']}, the record coded {name}'s civilian occupation as {category}."
        values.append(
            claim(
                row,
                f"occupation-{slug(name)}-row{row}-army-b947",
                "occupation",
                claim_text,
                f"The official Army record contains civilian-occupation code {item['code']}; NARA's historical code list expands it to {category}.",
                identity_assessment,
                "The code was recorded at Army entry and is date-bounded, but it identifies no employer, workplace, school or immediate OSS predecessor.",
                "A_direct_official",
                "medium",
                [
                    {"source_key": ARMY, "locator_override": f"Accepted reviewed identity record; civilian occupation code {item['code']}; protected identifier withheld"},
                    {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46; Army-entry-date and civilian-occupation fields"},
                    {"source_key": CODES, "locator_override": str(item["locator"]), "excerpt_override": category},
                ],
                "The historical category is published as qualified occupation or status evidence and is excluded from named-employer analytics.",
                f"{slug(name)}-row{row}-occupation-b947",
                "publish_qualified",
            )
        )
    return values


def substantive_claims() -> list[dict[str, object]]:
    return [
        claim(
            4,
            "identity-henry-thackthwaite-b947",
            "identity",
            "Indexed Henry H. Thackthwaite is a high-confidence match to British officer Henry Hopkinson Augustus Thackthwaite, alias Procureur.",
            "The rare surname and matching first and middle initial align with the expanded official name; institutional Resistance records place him in an interallied mission with OSS.",
            "High confidence from the rare exact indexed name pattern, expanded official name, British rank and explicit OSS-connected mission context.",
            "The sources establish wartime service and mission dates; the Box 770 file remains needed to document why the Allied officer appears in the U.S. personnel index.",
            "A_direct_official",
            "high",
            [
                {"source_key": INDEX, "locator_override": "PDF page 464 row 4"},
                {"source_key": GAZETTE_THACKTHWAITE, "locator_override": "Supplement page 1313; expanded name and Royal Army Service Corps"},
                {"source_key": MUSEUM_THACKTHWAITE, "locator_override": "Union mission narrative; Captain Henri Thackthwaite, alias Procureur"},
            ],
            "The profile identifies him as British and Allied personnel and does not call him a U.S. OSS employee or agent.",
        ),
        claim(
            4,
            "immediate-henry-thackthwaite-soe-b947",
            "immediate_pre_oss_affiliation",
            "Henry Thackthwaite's best-supported source affiliation for his OSS-indexed interallied work was the British Special Operations Executive, Section RF.",
            "The Resistance Museum identifies Captain Thackthwaite as a British SOE member in the Union mission with OSS officer Peter Ortiz and BCRA officer Camille Monnier.",
            "High-confidence rare-name identity with aligned rank, alias, organization and explicit OSS-connected mission.",
            "Explicit assignment context from January to May 1944; this is an Allied source affiliation, not evidence of U.S. employment.",
            "B_authoritative_institutional",
            "high",
            [
                {"source_key": MUSEUM_THACKTHWAITE, "locator_override": "Union mission narrative"},
                {"source_key": MUSEUM_PERSON_THACKTHWAITE, "locator_override": "SOE Section RF; Union I mission, January 6-May 3, 1944"},
            ],
            "Published as the immediate source affiliation for an Allied mission participant; the qualification prevents conflating SOE and OSS.",
            "henry-thackthwaite-soe-b947",
        ),
        claim(
            4,
            "military-henry-thackthwaite-rasc-b947",
            "other_pre_oss_affiliation",
            "Henry Thackthwaite served as a British Army officer in the Royal Army Service Corps before his SOE detachment.",
            "The official Gazette identifies his expanded name, acting-major rank and Royal Army Service Corps; the Vercors chronology places Army entry in 1939 and SOE detachment in 1943-1944.",
            "High confidence from the expanded rare name, official corps record and compatible SOE chronology.",
            "The 1939-to-1943 sequence is supported by a qualified secondary chronology; the corps affiliation is independently official.",
            "A_direct_official",
            "high",
            [
                {"source_key": GAZETTE_THACKTHWAITE, "locator_override": "Supplement page 1313"},
                {"source_key": MVR_THACKTHWAITE, "support_type": "context_only", "locator_override": "British Army entry and SOE-detachment chronology"},
            ],
            "The military assignment is separate from both the unnamed prewar civilian work and the later SOE mission.",
            "henry-thackthwaite-rasc-b947",
            "publish_qualified",
        ),
        claim(
            4,
            "occupation-henry-thackthwaite-b947",
            "occupation",
            "Before British Army service, Henry Thackthwaite was described as a translator and teacher; no civilian employer is named.",
            "The Vercors biographical chronology describes prewar work as a translator and teacher before British Army entry in 1939.",
            "High-confidence person match from the rare expanded name and wartime service context.",
            "Documented as prewar occupation only; exact dates and employer remain unknown.",
            "D_correlative_or_secondary",
            "medium",
            [{"source_key": MVR_THACKTHWAITE, "locator_override": "Prewar occupation and 1939 Army-entry chronology"}],
            "Published only as qualified occupation evidence. No school, agency or employer is inferred.",
            "henry-thackthwaite-occupation-b947",
            "publish_qualified",
        ),
        claim(
            16,
            "identity-charles-wheeler-thayer-b947",
            "identity",
            "Indexed Charles W. Thayer is a high-confidence match to Foreign Service officer and U.S. Army Major Charles Wheeler Thayer.",
            "Official State Department pages align the exact indexed name, expanded middle name, Foreign Service career, Afghanistan assignment and 1944 major rank.",
            "High confidence from exact full-name pattern, compatible officer rank, direct official chronology and distinctive wartime mission.",
            "The sources establish the person and a State-to-Army chronology; the Box 771 file is still needed for the exact OSS linkage and transfer date.",
            "A_direct_official",
            "high",
            [
                {"source_key": INDEX, "locator_override": "PDF page 464 row 16; protected identifier withheld"},
                {"source_key": STATE_THAYER, "locator_override": "Career Foreign Service Officer; Afghanistan assignment"},
                {"source_key": FRUS_THAYER, "locator_override": "Document 1312 and editor's footnote 91"},
            ],
            "The profile uses official sources and does not infer a more specific OSS role than the indexed file establishes.",
        ),
        claim(
            16,
            "immediate-charles-thayer-state-b947",
            "immediate_pre_oss_affiliation",
            "Charles Wheeler Thayer's best-supported pre-OSS predecessor affiliation was the United States Foreign Service in the Department of State.",
            "The State biography calls him a career Foreign Service Officer and dates his Kabul charge assignment through July 2, 1942; FRUS later calls him a former Foreign Service Officer and Army major.",
            "High-confidence exact identity from two official State Department records and the indexed officer row.",
            "Probable immediate predecessor: the official chronology brackets State service and later Army command but does not state the exact transfer date or exclude an intervening assignment.",
            "A_direct_official",
            "high",
            [
                {"source_key": STATE_THAYER, "locator_override": "Career Foreign Service Officer; charge d'affaires ad interim, Afghanistan, through July 2, 1942"},
                {"source_key": FRUS_THAYER, "locator_override": "November 4, 1944 report; former Foreign Service Officer"},
            ],
            "Published as a qualified government assignment, not a civilian-company employer and not an explicit recruitment-from claim.",
            "charles-thayer-state-b947",
            "publish_qualified",
        ),
        claim(
            23,
            "identity-milton-theaman-b947",
            "identity",
            "Indexed Milton Theaman is a high-confidence match to the OSS Assessment Staff roster's Milton Theaman, M.S., second lieutenant, at Fairfax, Virginia.",
            "The original OSS volume prints the rare exact name with second-lieutenant rank and station code S; the preceding page defines S as Fairfax and the dagger's staff-work meaning.",
            "High confidence from the rare exact name, officer-style index entry and direct original OSS staff roster.",
            "The roster proves wartime OSS staff service but prints no parenthetical pre-government institution and supplies no pre-OSS employer.",
            "A_direct_official",
            "high",
            [
                {"source_key": INDEX, "locator_override": "PDF page 464 row 23; protected identifier withheld"},
                {"source_key": ASSESSMENT_THEAMAN, "locator_override": "Printed pages v-vi; staff legend and Milton Theaman entry", "excerpt_override": "Milton Theaman, M.S., 2nd Lt. S"},
            ],
            "The profile publishes the direct identity and OSS staff context but retains an archival-review outcome for the unanswered pre-OSS question.",
        ),
    ]


def archival_update(row: int, reason: str) -> dict[str, object]:
    person_id, name = PEOPLE[row]
    box = "770" if row <= 11 else "771"
    location = "230/86/41/07" if row <= 11 else "230/86/42/01"
    return {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, Box {box} and archive location {location}. {reason}",
        "personnel_category": "unknown_or_indeterminate",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": f"Review Box {box} for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }


def army_update(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    person_id, name = PEOPLE[row]
    evidence = f"A nonshared protected identifier connects the visually verified {name} index row to the reviewed official Army record."
    update: dict[str, object] = {
        "person_id": person_id,
        "identity_status": "high_confidence",
        "identity_evidence": evidence,
        "personnel_category": "enlisted_army_personnel",
        "commissioned_officer": False,
        "allied_or_foreign_personnel": False,
        "manual_review_required": True,
        "research_status": "occupation_only_found" if item["public_occupation"] else "requires_archival_review",
        "next_action": "Review the indexed personnel file to establish the immediate pre-OSS affiliation and named last civilian employer; do not convert the Army code into a workplace.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "critical" if row == 22 else "high",
    }
    if item.get("name_variant"):
        update["name_variants"] = [str(item["name_variant"])]
        update["identity_evidence"] += f" The Army record preserves the suffix variant {item['name_variant']}."
    else:
        update["identity_evidence"] += " The full name agrees exactly."
    if row == 1:
        update["next_action"] = "Review Box 770 to identify the immediate pre-OSS affiliation and last civilian employer. Army code 999 remains uninterpreted and is not published."
    if row == 22:
        update["identity_evidence"] += " A separate Hucal Julian S bulk record sharing the private identifier was rejected as an unrelated name conflict."
    if row in DUPLICATES:
        update["possible_duplicate_group"] = DUPLICATES[row]
        update["next_action"] = "Review both adjacent same-name Box files together. Keep the source rows separate and do not transfer the accepted Army evidence to the other row."
    return update


def duplicate_update(row: int, detail: str) -> dict[str, object]:
    person_id, name = PEOPLE[row]
    box = "770" if row <= 11 else "771"
    return {
        "person_id": person_id,
        "identity_status": "ambiguous",
        "identity_evidence": detail,
        "personnel_category": "unknown_or_indeterminate",
        "manual_review_required": True,
        "possible_duplicate_group": DUPLICATES[row],
        "research_status": "needs_identity_review",
        "next_action": f"Review both adjacent same-name Box {box} files together and compare identifiers, birth details, ranks and OSS assignments. Do not transfer evidence between rows.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "critical",
    }


def person_updates() -> list[dict[str, object]]:
    updates = [archival_update(row, reason) for row, reason in UNRESOLVED.items()]
    updates.extend(army_update(item) for item in ARMY_RECORDS)
    updates.extend(
        [
            duplicate_update(
                9,
                "The index prints William Thanos without a protected identifier immediately after William J. Thanos with one. Name similarity and adjacency are insufficient to merge them; the accepted Army student record applies only to row 8.",
            ),
            duplicate_update(
                10,
                "Page 464 contains two separate Melvin E. Tharp rows with different protected identifiers and different indexed personnel styles. The accepted Army record applies only to row 11.",
            ),
            duplicate_update(
                21,
                "The index prints William A. Thayer without a protected identifier immediately before a separate protected William A. Thayer row. The accepted Army record and rejected Hucal collision apply only to row 22.",
            ),
            {
                "person_id": PEOPLE[4][0],
                "identity_status": "high_confidence",
                "identity_evidence": "The rare indexed name aligns with official expanded name Henry Hopkinson Augustus Thackthwaite, British Army rank and an institutional account of his SOE interallied mission with OSS officer Peter Ortiz.",
                "name_variants": ["Henry Hopkinson Augustus Thackthwaite", "Henri Thackthwaite", "Procureur"],
                "personnel_category": "foreign_or_allied_military_personnel",
                "commissioned_officer": True,
                "allied_or_foreign_personnel": True,
                "manual_review_required": True,
                "research_status": "needs_temporal_review",
                "next_action": "Review Box 770 to document why the British SOE officer is indexed, verify the exact liaison status and identify any named prewar civilian employer.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[16][0],
                "identity_status": "high_confidence",
                "identity_evidence": "Official State Department records align indexed Charles W. Thayer with Charles Wheeler Thayer, a career Foreign Service Officer and later U.S. Army major in the Independent American Military Mission to Tito.",
                "name_variants": ["Charles Wheeler Thayer"],
                "personnel_category": "commissioned_army_officer",
                "commissioned_officer": True,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "needs_temporal_review",
                "next_action": "Review Box 771 to confirm the exact Foreign Service-to-Army/OSS transfer sequence and determine whether an intervening assignment occurred after July 2, 1942.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[23][0],
                "identity_status": "high_confidence",
                "identity_evidence": "The rare exact name and officer-style index entry align with the original OSS Assessment Staff roster's Milton Theaman, M.S., second lieutenant, at the Fairfax, Virginia station.",
                "personnel_category": "commissioned_army_officer",
                "commissioned_officer": True,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": "Review Box 771 to identify the immediate pre-OSS affiliation and last civilian employer. The staff roster prints no parenthetical pre-government institution for Theaman.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
        ]
    )
    return updates


def research_attempts() -> list[dict[str, object]]:
    army_rows = {int(item["row"]) for item in ARMY_RECORDS}
    attempts: list[dict[str, object]] = []
    for row in sorted(PEOPLE):
        person_id, name = PEOPLE[row]
        if row in UNRESOLVED:
            outcome, reviewed, rejected, detail = "no_result", 6, 6, UNRESOLVED[row]
        elif row in {9, 10, 21}:
            outcome, reviewed, rejected, detail = (
                "candidate_found",
                6,
                5,
                "An adjacent same-name index row has different or missing protected identifiers. The rows remain separate and evidence is isolated to the bridged row.",
            )
        elif row == 4:
            outcome, reviewed, rejected, detail = (
                "source_reviewed",
                10,
                4,
                "Official and institutional sources identify the rare-name British Army officer, his SOE Section RF interallied mission and a qualified prewar translator-teacher occupation without a named employer.",
            )
        elif row == 16:
            outcome, reviewed, rejected, detail = (
                "source_reviewed",
                9,
                4,
                "Two official State Department records establish Charles Wheeler Thayer's Foreign Service career, dated Kabul assignment and later U.S. Army major role; the exact transfer remains qualified.",
            )
        elif row == 23:
            outcome, reviewed, rejected, detail = (
                "source_reviewed",
                8,
                5,
                "An original OSS Assessment Staff roster establishes the rare-name identity, second-lieutenant rank and Fairfax station, but prints no pre-government institution or employer.",
            )
        elif row in army_rows:
            outcome, reviewed, rejected, detail = (
                "source_reviewed",
                7,
                5,
                "An accepted protected-identifier Army bridge supports identity and, where the code is interpretable, a dated historical occupation or student-status category; it does not name an employer or immediate OSS affiliation.",
            )
        else:
            raise AssertionError(f"Missing Batch 947 outcome for row {row}")
        attempts.append(
            {
                "key": f"page464-row{row}-{slug(name)}-b947",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index and public Archives context; CIA Reading Room or equivalent official-source check; exact-name and meaningful variants; OSS and military clues; employer and occupation 1940; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Boxes 770-771; protected identifiers used privately only when defensible",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_947",
                "started_at": "2026-10-28T09:20:00Z",
                "completed_at": "2026-10-28T10:34:00Z",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search snippets, family-tree assertions, modern people-finder pages, postwar-only leads and sources without an OSS, protected-identifier or Box-file bridge were not assigned.",
                "research_notes": f"{detail} The index page and admitted Army, code-list, official or institutional pages were visually checked where applicable. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": "Review the indexed personnel file for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before wartime service.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b947-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-947-v1",
        "reviewer": "Before OSS Batch 947 evidence review",
        "sources": sources(),
        "organizations": organizations(),
        "affiliations": affiliations(),
        "claims": army_claims() + substantive_claims(),
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }
    EvidenceBundle.model_validate(bundle)
    OUTPUT.write_text(
        json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
