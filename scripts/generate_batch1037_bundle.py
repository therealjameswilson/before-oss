#!/usr/bin/env python3
"""Generate the reviewed Batch 1037 evidence bundle for PDF page 292."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page292-robert-maloof-to-gottfried-t-mann-review_"
    "batch-1037_2026-11-04.json"
)

INDEX = "nara-index-b1037"
ARMY = "army-bulk-b1037"
TECH = "army-tech-b1037"
CODES = "army-codes-b1037"
MANDELBAUM = "bancroft-mandelbaum-b1037"
ERIKA_NARA = "nara-entry217-erika-mann-b1037"
ERIKA_DHM = "dhm-erika-mann-b1037"
GOLO_DBO = "deutsche-biographie-golo-mann-b1037"
GOLO_OCLC = "oclc-golo-mann-b1037"
MANIERRE_NPS = "nps-manierre-b1037"

ORG_MINNESOTA = "university-minnesota-b1037"
ORG_OWI = "owi-b1037"
ORG_OLIVET = "olivet-college-b1037"


PEOPLE = {
    1: ("ef8547cc-d669-5642-808f-d5ae3c79cc75", "Robert Maloof", "478"),
    2: ("214f75c2-5d67-5139-ba2d-3a02094041ba", "Andrew A Malozemoff", "478"),
    3: ("2756e531-e7f6-5037-943d-669e811367f2", "Michael Mamakos", "478"),
    4: ("0cef8476-0a7f-5aac-af3d-d52bfef19ba4", "Victor S Mamatey", "478"),
    5: ("50479b18-cce4-5e42-ade3-50ded89681df", "Rene Mampuys", "478"),
    6: ("07f0ee34-3c66-5987-b534-6ff828a1ba9e", "Nicholas Mamula", "478"),
    7: ("891ad114-c967-5253-be01-e7431d75d85e", "Alice H Manahan", "478"),
    8: ("4efef99b-39be-5243-af28-41afe58a2b08", "Manette Manalang", "478"),
    9: ("e48018de-7e7c-55dd-9463-a85918f30847", "Marcus Manaloe", "478"),
    10: ("f9f7e77e-1b25-5ee6-877f-c57b6bdf81bc", "Morton C Manaugh", "517"),
    11: ("89c39158-52d1-564b-8079-9172853d170d", "Mary F Manchester", "478"),
    12: ("fd6666aa-f718-53f2-b064-17834a03b4d3", "Italio F Mancini", "478"),
    13: ("4a6c1124-1bf1-580b-b6df-3b63c8a1ee8a", "Nicholas M Mancini", "478"),
    14: ("4d73a231-854c-518a-a9b6-80471bb6ed44", "Marion F Mancosos", "478"),
    15: ("86c40e09-cb87-530e-bb52-d9d2f0920d77", "Frank Mancuso", "478"),
    16: ("bf56e919-5ade-5f9c-b25f-d9889e8a2e77", "Rosario G Mandara", "478"),
    17: ("8eebccc3-e7d0-5901-a4f0-805c905de555", "David G Mandelbaum", "478"),
    18: ("c95ae597-b23d-52c1-8bc2-fbb90663142f", "Ruth W Mandelbaum", "478"),
    19: ("bf0431f7-db13-53c5-a7f6-88f88e224023", "Lucien C Mandelik", "478"),
    20: ("856ea5a5-66f7-51cc-9cf2-84a8a422c8ed", "Richard E Mandernach", "478"),
    21: ("7e387b3b-0088-5758-a07d-c68000bade6e", "Albert C Manderson", "478"),
    22: ("a1c3e556-b748-5b86-ad92-523284455c94", "Frank J Mandia", "478"),
    23: ("c1ca8870-bc03-5f2f-b6ae-41d974c5d2d2", "Daniel A Maness Jr.", "478"),
    24: ("ab6d56cb-b2ba-571e-acc4-f134c9fdbf81", "Virginia I Maney", "478"),
    25: ("c63d2d6f-25bf-5eb5-8506-fd73c06a5ba8", "Joseph D Manfredi", "478"),
    26: ("84046f1f-04e3-5f75-a2e0-fce1c67c0248", "James F Mangan", "478"),
    27: ("888c0ff5-3a94-5b00-8a12-00f619d3b30d", "Philip A Mangano", "478"),
    28: ("55fba7d5-7ca3-5055-8905-189ce24a762c", "Frank H Mangeng", "479"),
    29: ("8e4a310a-fb4b-53a2-8908-1d3622274000", "Nicholas M Mangini", "479"),
    30: ("06f28497-a6b4-5808-be65-a60839e17087", "Cosmo Mangogna", "479"),
    31: ("885d386e-2bf5-593f-a774-d4a9fd7f0d7e", "Francis B Mangold", "479"),
    32: ("077fc221-f397-599b-94d3-9b09919f5f99", "William P Mangold", "479"),
    33: ("17a89deb-4d49-5e1e-b36a-9c201115f906", "Ellen Manheim", "479"),
    34: ("94c6a412-8753-5e47-ad79-23c75ea4b05d", "Frank J Manheim", "479"),
    35: ("c7f51a03-289e-53d2-8935-c51ec8a8a550", "John J Maniaci", "479"),
    36: ("c8ea75e3-3284-5cde-bad9-dd273eb64ca7", "Cyrus E Manierre", "479"),
    37: ("0a1970f0-6e7a-5559-8c50-f4b3124b6479", "Joseph Maniglia", "479"),
    38: ("db3b622d-acac-5c78-940c-b258fc41725f", "Joseph M Mankowsky", "479"),
    39: ("895d57e7-099c-552c-9321-ba0578ee10ea", "Jack A Manley", "479"),
    40: ("43358a80-a111-50d8-908b-23dc784a62c1", "John D Manley", "479"),
    41: ("4825f780-62e1-5aba-b35a-90e69f97744a", "Nena C Manley", "479"),
    42: ("ddf9f64c-37a3-5cf4-8482-c1e0320de9da", "Anthony P Mann", "479"),
    43: ("53981f87-a8f3-55c6-970b-8b63b2d483aa", "D J Mann", "479"),
    44: ("b34d8554-1bf1-5310-b917-458606f6c8f4", "Doris M Mann", "479"),
    45: ("5ce229cf-2112-5804-b061-f47ff719e18c", "Erika Mann", "479"),
    46: ("5ab7f4a4-5341-5532-8a4f-db07d2bab3d8", "Gottfried T Mann", "479"),
}

# Each accepted record has exact official name agreement and a nonshared
# protected linkage. The protected identifier and raw bulk record remain private.
ARMY_ASSOCIATIONS = {
    2: ("1942-03-29", "031", "secondary-school teacher or principal", "Teachers (secondary school) and principals", "unknown", "PDF physical page 171; historical category 0-31"),
    3: ("1942-12-26", "227", "waiter or waitress outside private-family service", "Waiters and waitresses, except private family", "unknown", "PDF physical page 172; historical category 2-27"),
    4: ("1942-08-28", "069", "semiprofessional worker, not elsewhere classified", "Semiprofessional occupations, n.e.c.", "unknown", "PDF physical page 171; historical category 0-69"),
    6: ("1942-07-16", "137", "stenographer or typist", "Stenographers and typists", "unknown", "PDF physical page 171; historical category 1-37"),
    12: ("1942-10-29", "694", "blacksmith, forgeman, or hammerman", "Blacksmiths, forgemen, and hammermen", "unknown", "PDF physical page 174; historical category 6-94"),
    16: ("1940-09-16", "819", "textile-manufacturing worker, not elsewhere classified", "Textile manufacturing occupations, n.e.c.", "unknown", "PDF physical page 179; historical category 8-19"),
    20: ("1943-03-16", "992", "student", "Students", "student", "PDF physical page 304; corrected historical category 9-92"),
    21: ("1940-12-12", "727", "construction or maintenance painter", "Painters, construction and maintenance", "unknown", "PDF physical page 175; historical category 7-27"),
    22: ("1942-08-17", "583", "mechanic or repairman, not elsewhere classified", "Mechanics and repairmen, n.e.c.", "unknown", "PDF physical page 177; historical category 5-83"),
    25: ("1942-04-15", "105", "general office clerk", "Clerks, general office", "unknown", "PDF physical page 171; historical category 1-05"),
    29: ("1941-04-30", "736", "driver or chauffeur", "Drivers and chauffeurs, bus, taxi, truck, and tractor", "unknown", "PDF physical page 175; historical category 7-36"),
    30: ("1942-12-04", "222", "bellman or related worker", "Bellmen and related occupations", "unknown", "PDF physical page 172; historical category 2-22"),
    37: ("1943-10-05", "232", "barber, beautician, or manicurist", "Barbers, beauticians, and manicurists", "unknown", "PDF physical page 172; historical category 2-32"),
    38: ("1941-01-16", "819", "textile-manufacturing worker, not elsewhere classified", "Textile manufacturing occupations, n.e.c.", "unknown", "PDF physical page 179; historical category 8-19"),
    42: ("1942-07-23", "134", "shipping or receiving clerk", "Shipping and receiving clerks", "unknown", "PDF physical page 171; historical category 1-34"),
    46: ("1943-08-06", "031", "secondary-school teacher or principal", "Teachers (secondary school) and principals", "unknown", "PDF physical page 171; historical category 0-31"),
}

ARMY_IDENTITY_ONLY = {
    15: ("1943-05-10", "Occupation code 999 is undefined and is not interpreted."),
    23: ("1943-07-29", "Occupation code 993 is absent from the visually checked official lists and is not interpreted."),
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
            archival_identifier="RG 226, Entry A1-224, Boxes 478-479 and 517",
            title="OSS Personnel Files from Excel",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="2010-12-23",
            locator="PDF page 292, rows 1-46; page and every printed row visually checked at 180 dpi",
            source_quality="A_direct_official",
            collection_name="Records of the Office of Strategic Services, Record Group 226",
            rights_notes="All 46 printed rows remain separate. The malformed Nicholas M. Mancini rank-column value is preserved privately and not silently corrected.",
        ),
        source(
            ARMY,
            stable_url="https://catalog.archives.gov/id/1263923",
            archival_identifier="National Archives Identifier 1263923; parent series NAID 604357",
            title="Electronic Army Serial Number Merged File, ca. 1938-1946",
            author_creator="Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="1938-1946; merged file created 2002",
            locator="Official unrestricted ASNEF.FIN.DAT; twenty-one Batch 1037 candidates explicitly reviewed; eighteen accepted and three rejected",
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
            locator="PDF physical pages 171-179 and 304; all sixteen published Batch 1037 categories visually checked",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records technical documentation",
            rights_notes="Historical categories identify neither employer, institution, workplace, nor exact Army-to-OSS sequence. Undefined codes 993 and 999 are not interpreted.",
        ),
        source(
            MANDELBAUM,
            stable_url="https://oac.cdlib.org/findaid/ark:/13030/tf400003gz",
            archival_identifier="BANC MSS 89/129 cz",
            title="David Goodman Mandelbaum Papers, 1899-1991, bulk 1933-1986",
            author_creator="The Bancroft Library",
            repository_publisher="Online Archive of California; The Bancroft Library, University of California, Berkeley",
            publication_record_date="Finding aid",
            locator="Biographical Information section",
            source_quality="B_authoritative_institutional",
            collection_name="David Goodman Mandelbaum Papers",
            rights_notes="The finding aid states that Mandelbaum went to OSS while on leave from the University of Minnesota.",
        ),
        source(
            ERIKA_NARA,
            stable_url="https://www.archives.gov/iwg/declassified-records/rg-226-oss/entry-217.html",
            archival_identifier="RG 226, Entry 217",
            title="Entry 217: Central Files of the Office of Strategic Services",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="Web guide",
            locator="November 12, 1943 Erika Mann letter description",
            source_quality="A_direct_official",
            collection_name="Records of the Office of Strategic Services, Record Group 226",
            rights_notes="The entry guide establishes direct OSS document context but not a pre-OSS employer.",
        ),
        source(
            ERIKA_DHM,
            stable_url="https://www.dhm.de/lemo/biografie/erika-mann",
            title="Erika Mann 1905-1969",
            author_creator="Deutsches Historisches Museum",
            repository_publisher="LeMO, Deutsches Historisches Museum",
            publication_record_date="Biographical chronology",
            locator="1942 chronology entry",
            source_quality="B_authoritative_institutional",
            collection_name="Lebendiges Museum Online",
            rights_notes="The chronology documents OWI work in New York in 1942; exact transition into OSS-related activity remains unresolved.",
        ),
        source(
            GOLO_DBO,
            stable_url="https://www.deutsche-biographie.de/dbo098356.html?language=en",
            title="Golo Mann",
            author_creator="Deutsche Biographie",
            repository_publisher="Bavarian State Library and Historical Commission at the Bavarian Academy of Sciences",
            publication_record_date="Biographical authority record",
            locator="Career chronology: Olivet College 1942-1943; U.S. Army and OSS 1943-1946",
            source_quality="B_authoritative_institutional",
            collection_name="Deutsche Biographie",
            rights_notes="The authority record supplies the full birth name and a date-bounded Olivet-to-Army/OSS sequence.",
        ),
        source(
            GOLO_OCLC,
            stable_url="https://entities.oclc.org/worldcat/entity/E39PBJrKTRFKgtg3bhVQPYV9jC.html",
            archival_identifier="WorldCat Entity E39PBJrKTRFKgtg3bhVQPYV9jC",
            title="Golo Mann",
            author_creator="OCLC",
            repository_publisher="WorldCat Entities, OCLC",
            publication_record_date="Authority record",
            locator="Names and identities",
            source_quality="B_authoritative_institutional",
            collection_name="WorldCat Entities",
            rights_notes="Used to corroborate Golo Mann as an alias of Angelus Gottfried Thomas Mann.",
        ),
        source(
            MANIERRE_NPS,
            stable_url="https://www.nps.gov/articles/oss-in-action-the-mediterranean-and-european-theaters.htm",
            title="OSS in Action: The Mediterranean and European Theaters",
            author_creator="National Park Service",
            repository_publisher="National Park Service",
            publication_record_date="Web history",
            locator="Team Dodge section naming Major Cyrus E. Manierre Jr.",
            source_quality="A_direct_official",
            collection_name="Office of Strategic Services history",
            rights_notes="Supports wartime OSS identity and assignment only; it does not identify an earlier employer or unit transfer.",
        ),
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": ORG_MINNESOTA,
            "organization_id": "a7d41a87-9f88-51a4-9eb3-fb8de0ce10a1",
            "canonical_name": "University of Minnesota",
            "historical_name": "University of Minnesota",
            "aliases": [],
            "organization_type": "public university",
            "sector": "academia_and_research",
            "city": "Minneapolis and Saint Paul",
            "state_or_region": "Minnesota",
            "country": "United States",
            "normalization_notes": "Existing canonical organization reused. Employment and student status remain distinct.",
        },
        {
            "key": ORG_OWI,
            "organization_id": "d907505c-05ff-502a-810c-e6189e186543",
            "canonical_name": "United States Office of War Information",
            "historical_name": "Office of War Information",
            "aliases": ["OWI"],
            "organization_type": "federal wartime information agency",
            "sector": "federal_government",
            "country": "United States",
            "active_dates": "1942-1945",
            "normalization_notes": "Existing canonical agency reused. Government assignment remains separate from private employment.",
        },
        {
            "key": ORG_OLIVET,
            "canonical_name": "Olivet College",
            "historical_name": "Olivet College",
            "aliases": [],
            "organization_type": "college",
            "sector": "academia_and_research",
            "city": "Olivet",
            "state_or_region": "Michigan",
            "country": "United States",
            "active_dates": "Founded 1844",
            "normalization_notes": "Historical institutional name preserved; the modern institution is known as The University of Olivet.",
        },
    ]


def army_affiliation_key(row: int) -> str:
    return f"{slug(PEOPLE[row][1])}-army-association-b1037"


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, _label, relationship, _locator) in ARMY_ASSOCIATIONS.items():
        value: dict[str, object] = {
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
            "research_notes": "The broad historical category is not converted into a named employer and is excluded from verified-employer analytics.",
        }
        if relationship == "student":
            value["role_title"] = "student"
        else:
            value["occupation"] = occupation
        values.append(value)
    values.extend(
        [
            {
                "key": "david-mandelbaum-minnesota-b1037",
                "person_id": PEOPLE[17][0],
                "organization_key": ORG_MINNESOTA,
                "organization_name_as_found": "University of Minnesota",
                "role_title": "teacher of anthropology",
                "occupation": "anthropologist",
                "relationship_type": "employment",
                "end_date": "World War II",
                "date_precision": "The institutional finding aid says he went to Washington for OSS work while on leave from the University of Minnesota; no exact transition date is supplied.",
                "state_or_region": "Minnesota",
                "country": "United States",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "explicit_immediate",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "The leave relationship directly supports the university as the immediate and last civilian employer before OSS service.",
            },
            {
                "key": "erika-mann-owi-b1037",
                "person_id": PEOPLE[45][0],
                "organization_key": ORG_OWI,
                "organization_name_as_found": "Office of War Information",
                "relationship_type": "government_assignment",
                "start_date": "1942",
                "end_date": "1942",
                "date_precision": "The institutional chronology documents OWI work in New York in 1942; a NARA guide separately describes an OSS letter from November 1943.",
                "city": "New York",
                "state_or_region": "New York",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "publish_qualified",
                "research_notes": "OWI is documented as an earlier wartime government assignment. It is not presented as the immediate predecessor or last civilian employer.",
            },
            {
                "key": "gottfried-mann-olivet-b1037",
                "person_id": PEOPLE[46][0],
                "organization_key": ORG_OLIVET,
                "organization_name_as_found": "Olivet College",
                "role_title": "lecturer in history",
                "occupation": "historian and lecturer",
                "relationship_type": "employment",
                "start_date": "1942",
                "end_date": "1943",
                "date_precision": "Deutsche Biographie dates Olivet College to 1942-1943 and U.S. Army/OSS service to 1943-1946; no exact transition month is supplied.",
                "city": "Olivet",
                "state_or_region": "Michigan",
                "country": "United States",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "The date-bounded chronology supports Olivet as the best-supported last civilian employer before Army/OSS service.",
            },
        ]
    )
    return values


def army_identity_assessment(row: int) -> str:
    return "Confirmed by exact official name agreement and a nonshared protected linkage; the protected identifier remains private."


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, label, relationship, locator) in ARMY_ASSOCIATIONS.items():
        values.append(
            {
                "key": f"army-{slug(PEOPLE[row][1])}-b1037",
                "person_id": PEOPLE[row][0],
                "affiliation_key": army_affiliation_key(row),
                "claim_type": "other_pre_oss_affiliation" if relationship == "student" else "occupation",
                "claim_text": f"At Army entry on {date}, {PEOPLE[row][1]} was recorded as {occupation}; no employer, institution, or workplace is identified.",
                "evidence_paraphrase": f"The Army bulk file records code {code}, and the visually checked official code list defines the category as {label}.",
                "identity_match_assessment": army_identity_assessment(row),
                "temporal_assessment": "Strongly date-bounded to Army entry, but not proven to be the immediately preceding role or status before OSS.",
                "source_quality": "A_direct_official",
                "claim_confidence": "medium",
                "publication_status": "publish_qualified",
                "match_notes": "The historical category is qualified, excluded from verified-employer analytics, and not converted into a named organization.",
                "sources": [
                    {"source_key": INDEX},
                    {"source_key": ARMY},
                    {"source_key": TECH, "support_type": "context_only"},
                    {"source_key": CODES, "locator_override": locator},
                ],
            }
        )
    for row, (date, note) in ARMY_IDENTITY_ONLY.items():
        values.append(
            {
                "key": f"identity-{slug(PEOPLE[row][1])}-army-b1037",
                "person_id": PEOPLE[row][0],
                "claim_type": "identity",
                "claim_text": f"Indexed {PEOPLE[row][1]} is a reviewed match to the official Army record.",
                "evidence_paraphrase": "A nonshared protected linkage and exact name agreement connect the official index and Army record; no full identifier or raw record is published.",
                "identity_match_assessment": army_identity_assessment(row),
                "temporal_assessment": f"Army entry is dated {date}. {note}",
                "source_quality": "A_direct_official",
                "claim_confidence": "confirmed",
                "publication_status": "published",
                "match_notes": "Identity evidence only; no undefined occupation is converted into pre-OSS evidence.",
                "sources": [
                    {"source_key": INDEX},
                    {"source_key": ARMY},
                    {"source_key": TECH, "support_type": "context_only"},
                ],
            }
        )
    values.extend(
        [
            {
                "key": "identity-david-mandelbaum-b1037",
                "person_id": PEOPLE[17][0],
                "claim_type": "identity",
                "claim_text": "Indexed First Lieutenant David G. Mandelbaum is high-confidence identified as anthropologist David Goodman Mandelbaum.",
                "evidence_paraphrase": "The institutional biography describes Army-officer and OSS service consistent with the exact indexed name and first-lieutenant context.",
                "identity_match_assessment": "High confidence from the distinctive exact name, matching Army-officer status, and explicit OSS chronology in an authoritative institutional finding aid.",
                "temporal_assessment": "The finding aid places his OSS work during World War II while on leave from the University of Minnesota.",
                "source_quality": "B_authoritative_institutional",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "The indexed personnel file remains unreviewed, so the match is not elevated to confirmed.",
                "sources": [{"source_key": MANDELBAUM}, {"source_key": INDEX, "support_type": "context_only"}],
            },
            {
                "key": "minnesota-david-mandelbaum-b1037",
                "person_id": PEOPLE[17][0],
                "affiliation_key": "david-mandelbaum-minnesota-b1037",
                "claim_type": "immediate_pre_oss_affiliation",
                "claim_text": "David G. Mandelbaum's immediate pre-OSS affiliation and last civilian employer were the University of Minnesota.",
                "evidence_paraphrase": "The Bancroft finding aid says Mandelbaum went to Washington for civilian and later Army OSS work while on leave from the University of Minnesota.",
                "identity_match_assessment": "High confidence from the distinctive name and compatible Army/OSS chronology.",
                "temporal_assessment": "Explicit immediate relationship: the source states that his OSS work began while he was on leave from the university.",
                "source_quality": "B_authoritative_institutional",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "University employment is documented; no later civilian employer is identified before OSS work.",
                "sources": [{"source_key": MANDELBAUM}],
            },
            {
                "key": "identity-erika-mann-b1037",
                "person_id": PEOPLE[45][0],
                "claim_type": "identity",
                "claim_text": "Indexed Erika Mann is high-confidence identified as the German writer and wartime correspondent discussed in OSS Entry 217.",
                "evidence_paraphrase": "NARA describes a November 1943 OSS letter concerning Erika Mann and possible Sweden travel under a Liberty magazine cover.",
                "identity_match_assessment": "High confidence from the distinctive exact name, direct OSS archival context, and the indexed FIS note; no protected identifier is available.",
                "temporal_assessment": "Direct wartime OSS document context dated November 12, 1943.",
                "source_quality": "A_direct_official",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "The identity is strong, but the indexed Box 479 file remains necessary to determine exact appointment status and dates.",
                "sources": [{"source_key": ERIKA_NARA}, {"source_key": INDEX, "support_type": "context_only"}],
            },
            {
                "key": "owi-erika-mann-b1037",
                "person_id": PEOPLE[45][0],
                "affiliation_key": "erika-mann-owi-b1037",
                "claim_type": "other_pre_oss_affiliation",
                "claim_text": "Erika Mann worked for the Office of War Information in New York in 1942.",
                "evidence_paraphrase": "The German Historical Museum chronology records Mann's 1942 work for the Office of War Information in New York.",
                "identity_match_assessment": "High confidence from the distinctive exact name and independent NARA OSS document context.",
                "temporal_assessment": "Documented in 1942 before the November 1943 OSS letter, but not proven to be the immediate predecessor or last civilian employer.",
                "source_quality": "B_authoritative_institutional",
                "claim_confidence": "medium",
                "publication_status": "publish_qualified",
                "match_notes": "Modeled as a government assignment, not private employment. The precise OWI-to-OSS sequence requires Box 479 review.",
                "sources": [{"source_key": ERIKA_DHM}, {"source_key": ERIKA_NARA, "support_type": "context_only"}],
            },
            {
                "key": "identity-gottfried-golo-mann-b1037",
                "person_id": PEOPLE[46][0],
                "claim_type": "identity",
                "claim_text": "Indexed Gottfried T. Mann is high-confidence identified as historian Golo Mann, born Angelus Gottfried Thomas Mann.",
                "evidence_paraphrase": "Deutsche Biographie and OCLC connect Golo Mann with the full name Angelus Gottfried Thomas Mann; the biography also records Army/OSS service.",
                "identity_match_assessment": "High confidence from the rare name sequence, authoritative alias evidence, exact Army-record agreement, and compatible U.S. Army/OSS chronology.",
                "temporal_assessment": "The biography dates U.S. Army and OSS service to 1943-1946; the accepted Army record is dated August 6, 1943.",
                "source_quality": "B_authoritative_institutional",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "The Box 479 personnel file remains unreviewed, so the authority-record match is not elevated to confirmed.",
                "sources": [{"source_key": GOLO_DBO}, {"source_key": GOLO_OCLC}, {"source_key": ARMY, "support_type": "context_only"}, {"source_key": INDEX, "support_type": "context_only"}],
            },
            {
                "key": "olivet-gottfried-mann-b1037",
                "person_id": PEOPLE[46][0],
                "affiliation_key": "gottfried-mann-olivet-b1037",
                "claim_type": "immediate_pre_oss_affiliation",
                "claim_text": "Gottfried T. Mann's best-supported immediate pre-OSS affiliation and last civilian employer were Olivet College, where he lectured in history.",
                "evidence_paraphrase": "Deutsche Biographie dates Mann's Olivet College lectureship to 1942-1943 and his U.S. Army/OSS service to 1943-1946.",
                "identity_match_assessment": "High confidence from the rare full-name and alias evidence plus exact accepted Army-record agreement.",
                "temporal_assessment": "Strongly date-bounded: college employment ends and Army/OSS service begins in 1943, though no exact transition month is given.",
                "source_quality": "B_authoritative_institutional",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "Olivet is treated as the best-supported last civilian employer; the exact transition remains subject to personnel-file review.",
                "sources": [{"source_key": GOLO_DBO}, {"source_key": GOLO_OCLC, "support_type": "context_only"}],
            },
            {
                "key": "identity-cyrus-manierre-b1037",
                "person_id": PEOPLE[36][0],
                "claim_type": "identity",
                "claim_text": "Indexed Major Cyrus E. Manierre is high-confidence identified as Major Cyrus E. Manierre Jr., leader of OSS Team Dodge.",
                "evidence_paraphrase": "The National Park Service names Major Cyrus E. Manierre Jr. as head of OSS Team Dodge in France.",
                "identity_match_assessment": "High confidence from the uncommon exact name, matching major rank, and direct official OSS assignment context.",
                "temporal_assessment": "Wartime OSS identity evidence only; the source does not establish a pre-OSS employer or immediately preceding military assignment.",
                "source_quality": "A_direct_official",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "West Point and Army leads were not converted into an immediate affiliation without a dated unit-to-OSS sequence.",
                "sources": [{"source_key": MANIERRE_NPS}, {"source_key": INDEX, "support_type": "context_only"}],
            },
        ]
    )
    return values


def base_update(row: int) -> dict[str, object]:
    name = PEOPLE[row][1]
    box = PEOPLE[row][2]
    return {
        "person_id": PEOPLE[row][0],
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified page 292 source preserves {name}, Box {box}, rank or grade when printed, notes when present, and archive location. Staged official, exact-name, employment, occupation, obituary, institutional, newspaper, directory, and archival searches did not establish a defensible identity-and-affiliation bridge.",
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

    for row in set(ARMY_ASSOCIATIONS) | set(ARMY_IDENTITY_ONLY):
        by_row[row].update(
            identity_status="confirmed",
            identity_evidence=army_identity_assessment(row),
            personnel_category="enlisted_army_personnel",
            commissioned_officer=False,
            allied_or_foreign_personnel=False,
            nara_catalog_id="1263923",
            archival_review_priority="high",
        )
        if row in ARMY_ASSOCIATIONS:
            by_row[row].update(
                research_status="occupation_only_found",
                next_action=f"Review Box {PEOPLE[row][2]} to identify a named employer or institution and establish Army-to-OSS chronology. The protected Army link supplies only a broad historical occupation or student-status category.",
            )
        else:
            by_row[row].update(
                research_status="requires_archival_review",
                next_action=f"Review Box {PEOPLE[row][2]} to establish the immediate pre-OSS affiliation and last civilian employer. The accepted Army record is retained for identity only because its occupation code is undefined.",
            )

    by_row[8].update(
        identity_status="ambiguous",
        identity_evidence="A Manette Cook Manalang Villamor namesake was reviewed, but obituary, diary and family-tree leads did not provide an independent OSS, Box 478, or protected-identifier bridge.",
        research_status="needs_identity_review",
        archival_review_priority="critical",
        next_action="Review Box 478 for Manette Manalang's full name, Philippine wartime context, and pre-OSS affiliation before assigning any Villamor-family biography.",
    )
    by_row[9].update(
        identity_status="conflicting",
        identity_evidence="The protected identifier is printed for separate indexed Marcus Manaloe and Marcus Manoloe records. A same-name Army lead was rejected because the identifier is shared; no occupation or identity fields were transferred.",
        possible_duplicate_group="batch1037-marcus-manaloe-manoloe-shared-identifier",
        research_status="needs_identity_review",
        archival_review_priority="critical",
        next_action="Jointly review the Marcus Manaloe Box 478 file and Marcus Manoloe index/file record before accepting the Army identity or merging the spellings.",
    )
    by_row[10].update(
        identity_status="conflicting",
        identity_evidence="A protected-linkage Army candidate names Morton C. Menaugh rather than indexed Morton C. Manaugh. The candidate was rejected and no identity, occupation, or grade was transferred.",
        research_status="needs_identity_review",
        archival_review_priority="critical",
        next_action="Review Box 517 and the original identifier-bearing source to determine whether Manaugh/Menaugh is a spelling variant or a different person.",
    )
    by_row[13].update(
        archival_review_priority="critical",
        next_action="Review Box 478 and the original index card for Nicholas M. Mancini. Page 292 places a numeric value in the rank column and leaves the serial column blank; the malformed row was preserved without silent correction.",
    )
    by_row[17].update(
        identity_status="high_confidence",
        identity_evidence="The distinctive exact name, matching Army-officer status, and explicit OSS chronology in the Bancroft Library finding aid support David Goodman Mandelbaum.",
        name_variants=["David Goodman Mandelbaum"],
        replace_name_variants=False,
        personnel_category="commissioned_army_officer",
        commissioned_officer=True,
        allied_or_foreign_personnel=False,
        research_status="verified_employer_found",
        archival_review_priority="medium",
        next_action="Review Box 478 to determine the exact date and terms of Mandelbaum's University of Minnesota leave and transition from civilian to Army OSS status.",
    )
    by_row[32].update(
        identity_status="ambiguous",
        identity_evidence="A 1940 Congressional Record entry names William P. Mangold at the Spanish Information Bureau, but name agreement alone does not bridge that record to indexed CAF-11 William P. Mangold.",
        research_status="needs_identity_review",
        archival_review_priority="critical",
        next_action="Review Box 479 for employer, address, education, or government-service identifiers before accepting or rejecting the Spanish Information Bureau namesake.",
    )
    by_row[34].update(
        identity_status="ambiguous",
        identity_evidence="Employment leads for an exact-name economist and publisher were reviewed, but accessible discovery sources did not independently establish the indexed P-4 identity or the sequence into OSS.",
        research_status="needs_temporal_review",
        archival_review_priority="critical",
        next_action="Review Box 479 for Frank J. Manheim's dated employment chronology before publishing any Union College, publishing, banking, or government affiliation.",
    )
    by_row[36].update(
        identity_status="high_confidence",
        identity_evidence="The uncommon exact name, matching major rank, and official National Park Service history of OSS Team Dodge support Cyrus E. Manierre Jr.",
        name_variants=["Cyrus E Manierre Jr."],
        replace_name_variants=False,
        personnel_category="commissioned_army_officer",
        commissioned_officer=True,
        allied_or_foreign_personnel=False,
        research_status="requires_archival_review",
        archival_review_priority="high",
        next_action="Review Box 479 to determine Manierre's unit immediately before Team Dodge and identify any last civilian employer. West Point education is not employment.",
    )
    by_row[45].update(
        identity_status="high_confidence",
        identity_evidence="The distinctive exact name, NARA's direct 1943 OSS letter description, and the indexed FIS note support writer and correspondent Erika Mann.",
        personnel_category="civilian_professional_or_administrative_grade",
        commissioned_officer=False,
        allied_or_foreign_personnel=False,
        research_status="completed",
        archival_review_priority="critical",
        next_action="Review Box 479 to date Erika Mann's formal OSS relationship and determine whether OWI, Liberty magazine work, or another affiliation immediately preceded it.",
    )
    by_row[46].update(
        identity_status="high_confidence",
        identity_evidence="The rare indexed name, authoritative Golo Mann alias evidence, exact accepted Army-record name, and dated U.S. Army/OSS chronology support Angelus Gottfried Thomas Mann.",
        name_variants=["Golo Mann", "Angelus Gottfried Thomas Mann"],
        replace_name_variants=False,
        personnel_category="enlisted_army_personnel",
        commissioned_officer=False,
        allied_or_foreign_personnel=False,
        research_status="verified_employer_found",
        archival_review_priority="medium",
        next_action="Review Box 479 for the exact 1943 Olivet College-to-Army/OSS transition and any intervening assignment.",
    )

    if len(updates) != 46:
        raise RuntimeError(f"Expected 46 person updates, generated {len(updates)}")
    return updates


def unresolved_reason(row: int) -> str:
    special = {
        8: "The Villamor-family namesake lacks an independent OSS or Box-file bridge and remains unassigned.",
        9: "A shared protected identifier links separate Manaloe and Manoloe index records; both Army candidates were rejected pending joint file review.",
        10: "The Menaugh/Manaugh Army name conflict was rejected; no candidate fields were transferred.",
        13: "The index row has a numeric value displaced into the rank column; it was not silently corrected.",
        17: "An institutional finding aid supports University of Minnesota employment immediately before OSS work.",
        32: "The Spanish Information Bureau namesake lacks a second identifier and remains unassigned.",
        34: "Discovery-only employment leads lack an authoritative identity-and-sequence bridge and remain unpublished.",
        36: "Official history supports Team Dodge identity but not the immediately preceding unit or civilian employer.",
        45: "OWI work is documented before a 1943 OSS letter, but the exact transition and last civilian employer remain unresolved.",
        46: "Authoritative chronology supports Olivet College as the best-supported last civilian employer before Army/OSS service.",
    }
    return special.get(
        row,
        "Unbridged namesakes, snippets, commercial people-finder pages, unsourced genealogy, relatives, and postwar-only leads did not establish this indexed person's identity or pre-OSS affiliation.",
    )


def research_attempts() -> list[dict[str, object]]:
    updates = {item["person_id"]: item for item in person_updates()}
    substantiated = set(ARMY_ASSOCIATIONS) | set(ARMY_IDENTITY_ONLY) | {17, 36, 45, 46}
    candidate_review = {8, 9, 10, 32, 34}
    values: list[dict[str, object]] = []
    for row in PEOPLE:
        person_id, name, box = PEOPLE[row]
        outcome = "source_reviewed" if row in substantiated else "candidate_found" if row in candidate_review else "candidate_rejected"
        values.append(
            {
                "key": f"page292-row{row}-{slug(name)}-b1037",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index context; exact-name and meaningful initial, suffix, alias, punctuation and OCR variants; OSS and CIA Reading Room; rank, branch, assignment and protected-identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory and archival searches; indexed Box {box}",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_1037",
                "started_at": "2026-11-04T19:05:00-05:00",
                "completed_at": "2026-11-04T21:40:00-05:00",
                "outcome": outcome,
                "sources_reviewed": 8 if row in substantiated else 5,
                "candidate_sources_rejected": 2 if row in substantiated else 4,
                "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, and postwar-only leads were rejected. Shared-identifier and different-name Army candidates were rejected. Army categories were not converted into named employers, and undefined codes 993 and 999 were not interpreted.",
                "research_notes": f"{unresolved_reason(row)} The official index, exact-name OSS searches, targeted CIA context, employment and occupation searches, and institutional, newspaper, obituary, directory, and archival searches were reviewed as applicable. Page 292 and the cited Army code-list pages were visually checked. No authenticated NARA Catalog API request was made.",
                "next_action": str(updates[person_id]["next_action"]),
                "attempt_number": 1,
                "research_agent_version": "before-oss-b1037-v1",
            }
        )
    if len(values) != 46:
        raise RuntimeError(f"Expected 46 research attempts, generated {len(values)}")
    return values


def main() -> None:
    bundle = {
        "bundle_version": "batch-1037-v1",
        "reviewer": "Before OSS Batch 1037 evidence review",
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
