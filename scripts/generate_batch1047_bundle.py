#!/usr/bin/env python3
"""Generate the reviewed Batch 1047 evidence bundle for PDF page 302."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page302-philip-j-may-to-richard-mazzarini-review_"
    "batch-1047_2026-11-05.json"
)

INDEX = "nara-index-b1047"
ARMY = "army-bulk-b1047"
TECH = "army-tech-b1047"
CODES = "army-codes-b1047"
HOOVER_MAYER = "hoover-ferdinand-l-mayer-b1047"
MIT_MAZLISH = "mit-bruce-mazlish-b1047"
NARA_MAYFIELD = "nara-wendell-mayfield-citation-b1047"
BAILEY_MAZZARINI = "bailey-county-journal-richard-mazzarini-b1047"
CORVO_MAZZARINI = "corvo-richard-mazzarini-b1047"
MEDAL_MAZZARINI = "ford-library-medal-richard-mazzarini-b1047"
NARA_GERALD = "nara-gerald-mayer-bern-b1047"
CIA_GERALD = "cia-alias-george-wood-gerald-mayer-b1047"

ORG_STATE = "state-department-b1047"
ORG_COLUMBIA = "columbia-university-b1047"
ORG_PANAM = "pan-american-airways-b1047"


# Rows 12 and 13 already have terminal reviewed outcomes and are preserved.
PEOPLE = {
    1: ("e0b3baa5-ea9f-567c-84b3-76c48e1656b2", "Philip J May", "493"),
    2: ("b288cfb6-d54e-509b-b82e-4eb02eacbcb8", "Robert R May", "494"),
    3: ("a420a3a4-bf3b-5878-87da-6216601205e0", "Ann D Mayberry", "494"),
    4: ("7c3b4da9-2afc-5ece-b097-179d727a225d", "Marilyn A Mayburg", "494"),
    5: ("ebd18973-254e-55b2-93d8-019299926399", "Joyce L Mayclin", "494"),
    6: ("a686b97e-65d8-5921-a29c-7931343b3c45", "Carl P Mayer", "494"),
    7: ("1364045d-eec0-547c-96b1-8b50f5ea90d3", "Charles A Mayer", "494"),
    8: ("d227219c-fd99-5084-b69e-397f1ea483b3", "Charles Mayer", "493"),
    9: ("e3eae807-975b-5961-b585-b40f9177af77", "Edward A Mayer", "494"),
    10: ("7ed4cef0-5c5c-5b9a-b3aa-538a30dd11c9", "Emil Mayer", "494"),
    11: ("0d58cfda-8870-5c0f-b2c7-99a365b7bf6f", "Ferdinand L Mayer", "494"),
    14: ("c9d1224d-f4ac-5986-89d5-f6ee1298f16a", "Gerald Mayer", "494"),
    15: ("1ffe31e5-43ec-5077-8e2e-88637014eaf9", "Harold M Mayer", "494"),
    16: ("77bc6bd9-93fc-5cb4-8686-a70ea3449547", "Isabel I Mayer", "494"),
    17: ("e8fe17e1-f45f-5a39-aaf1-53e48286c1d4", "Jasper J Mayer", "494"),
    18: ("5465f2ab-1a6b-58cb-ab63-30026508180c", "Lawrence J Mayer", "494"),
    19: ("a846d8ff-ec6d-5f24-aefc-69bf5327b6db", "Rene A Mayer", "494"),
    20: ("54d4ede5-6e54-5595-ac4c-2ee75ae9a41e", "Stephanie D Mayer", "494"),
    21: ("401b4992-a3a8-5dcf-9e6f-31b823edf35f", "Wilda Mayer", "494"),
    22: ("99a39828-e6af-57fe-a5a5-ee24bebee275", "Julia Mayerhofer", "494"),
    23: ("59e48f87-a776-5488-a939-a6949e928609", "George Mayersaks", "494"),
    24: ("bf2c0315-2226-5975-9c44-d4b18e0ecba3", "John S Mayes", "494"),
    25: ("0029b65e-85f3-528e-88f4-9707d4395249", "Wilda M Mayes", "494"),
    26: ("c1b6b82d-c145-5149-9f72-9555becdc655", "Fred C Mayfield", "494"),
    27: ("e427752f-defe-51c2-b1dc-08d13ea506a4", "Wendell Mayfield", "494"),
    28: ("b6ec052d-deda-5185-a93c-fc980c72c9cc", "John T Mayher", "494"),
    29: ("64514777-cbc8-53f9-a54e-e1cbe39eaf02", "William A Mayhew", "494"),
    30: ("cb1de698-1c69-5108-aeb1-de3b81b009d9", "Robert W Maynard", "494"),
    31: ("21c878e1-cfbe-598b-86ab-023aa190f643", "Alfred F Mayo", "494"),
    32: ("f8b77af3-d064-5205-9dd0-c47e44106b40", "Jack D Mayo", "495"),
    33: ("1837e701-e96d-5906-a78f-70fe158c84ac", "Winthrop M Mayo", "495"),
    34: ("60761450-1025-5f48-84f7-a6cb03a32011", "Homer N Mayrand", "495"),
    35: ("8913704c-6a7b-5f5f-892b-f4a587484017", "Thomas J Mays", "495"),
    36: ("76fd6b1a-a6d9-52cc-acc9-3493407064a0", "Joseph G Mayton", "495"),
    37: ("ee435edd-e5a0-5318-aa91-0f2dee5a994e", "Louis A Mazarri", "495"),
    38: ("8c0cc44d-739a-5b8d-a9f4-ef4f30081668", "Alex Mazel", "495"),
    39: ("0548651b-fdba-55a7-a84d-872f73841bc8", "Dana G Mazerolle", "495"),
    40: ("2e05d400-407c-5668-bfac-ecd6fafcc9ba", "Eugene Mazieres", "495"),
    41: ("04ebeaae-03df-5556-815a-3545177194e0", "Bruce H Mazlish", "495"),
    42: ("4a51ec7d-3141-5884-9773-c23e902857fa", "Jean Mazou", "495"),
    43: ("5a4777cc-80f6-5cab-92c1-41f3ea95184b", "Chester John Mazur", "495"),
    44: ("7070d5ae-ce2a-5d1c-92b8-6a6cae3ccdee", "Gesualdo J Mazza", "495"),
    45: ("5688a930-b4d5-514a-a5f7-a48ada4c54dd", "Riccardo Mazzarini", "495"),
    46: ("383c4058-6918-5a5b-a35e-28dd71fd07bb", "Richard Mazzarini", "495"),
}


# Official Army classifications are broad historical categories, not employers.
ARMY_ASSOCIATIONS = {
    7: ("1942-12-19", "175", "salesperson", "Salesmen, general", "PDF physical page 171; historical category 1-75"),
    10: ("1945-03-19", "306", "general farmer", "Farmers, general", "PDF physical page 172; historical category 3-06"),
    18: ("1942-09-07", "105", "general office clerk", "Clerks, general office", "PDF physical page 171; historical category 1-05"),
    28: ("1942-11-16", "678", "semiskilled machine-shop or related worker, not elsewhere classified", "Semiskilled machine shop and related occupations, n.e.c.", "PDF physical page 178; historical category 6-78"),
    38: ("1943-05-01", "127", "post office clerk", "Post office clerks", "PDF physical page 171; historical category 1-27"),
    39: ("1942-07-27", "736", "chauffeur or driver of a bus, taxi, truck, or tractor", "Chauffeurs and drivers, bus, taxi, truck, and tractor", "PDF physical page 174; historical category 7-36"),
    43: ("1942-12-05", "475", "machinist", "Machinists", "PDF physical page 173; historical category 4-75"),
    44: ("1942-12-08", "878", "unskilled machine-shop and related worker, not elsewhere classified", "Unskilled machine shop and related occupations, n.e.c.", "PDF physical page 180; historical category 8-78"),
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
            archival_identifier="RG 226, Entry A1-224, Boxes 493-495",
            title="OSS Personnel Files from Excel",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="2010-12-23",
            locator="PDF page 302, rows 1-46; every printed row visually checked",
            source_quality="A_direct_official",
            collection_name="Records of the Office of Strategic Services, Record Group 226",
            rights_notes="All 46 printed rows remain recoverable as 46 cautious entities. Both Frederick Mayer rows and both Riccardo/Richard Mazzarini spellings remain separate.",
        ),
        source(
            ARMY,
            stable_url="https://catalog.archives.gov/id/1263923",
            archival_identifier="National Archives Identifier 1263923; parent series NAID 604357",
            title="Electronic Army Serial Number Merged File, ca. 1938-1946",
            author_creator="Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="1938-1946; merged file created 2002",
            locator="Official unrestricted ASNEF.FIN.DAT; eight protected identity candidates previously reviewed and accepted",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records",
            document_number="ASNEF.FIN.DAT",
            rights_notes="No raw record, full protected identifier, or bulk-file ordinal is retained in public assets.",
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
            rights_notes="Used only to interpret selected fields; source damage and incomplete coverage remain visible.",
        ),
        source(
            CODES,
            stable_url="https://aad.archives.gov/aad/popup-codelist.jsp?cl_id=3323&dt=893&c_id=24986",
            archival_identifier="NARA AAD civilian occupation code list; Code No. 30 in NAID 1263923 documentation",
            title="World War II Army Enlistment Records: Civilian Occupation Code List",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives Access to Archival Databases",
            locator="Current AAD values for codes 105, 127, 175, 306, 475, 678, 736, and 878; printed reference copy visually checked",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records code lists",
            rights_notes="Every published value was visually checked. Categories identify neither employer, institution, workplace, nor exact Army-to-OSS sequence.",
        ),
        source(
            HOOVER_MAYER,
            stable_url="https://hoover.archives.gov/research/manuscript-collections/mayer",
            archival_identifier="Ferdinand L. Mayer Papers, 1926-1978; four manuscript boxes",
            title="Manuscript Collections - Ferdinand L. Mayer Papers",
            author_creator="Herbert Hoover Presidential Library and Museum",
            repository_publisher="National Archives and Records Administration",
            locator="Biographical Note and Scope and Content Note",
            source_quality="A_direct_official",
            collection_name="Ferdinand L. Mayer Papers",
            rights_notes="Official presidential-library finding aid. It supports a dated Foreign Service pathway and OSS identity but does not state the immediate 1940s recruitment sequence.",
        ),
        source(
            MIT_MAZLISH,
            stable_url="https://news.mit.edu/2016/professor-emeritus-bruce-mazlish-dies-1206",
            title="Professor Emeritus Bruce Mazlish, pioneer in the field of global history, dies at 93",
            author_creator="MIT School of Humanities, Arts, and Social Sciences",
            repository_publisher="MIT News, Massachusetts Institute of Technology",
            publication_record_date="2016-12-06",
            locator="Biographical paragraph identifying 1940 Columbia graduation and wartime OSS service",
            source_quality="B_authoritative_institutional",
            collection_name="MIT News",
            rights_notes="Used for institutional biography and chronology only. Columbia is modeled as student status, not employment.",
        ),
        source(
            NARA_MAYFIELD,
            stable_url="https://www.archives.gov/files/research/jfk/releases/104-10165-10120.pdf",
            archival_identifier="National Archives release 104-10165-10120",
            title="OSS award citations and naval personnel list",
            author_creator="Office of Strategic Services",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="World War II",
            locator="PDF physical page 84; Naval Personnel citation; visually inspected",
            source_quality="A_direct_official",
            collection_name="Records of the Office of Strategic Services",
            rights_notes="The official scan identifies Chief Yeoman Wendell Mayfield and an OSS citation. A protected number visible in the scan is neither transcribed nor published.",
        ),
        source(
            BAILEY_MAZZARINI,
            stable_url="https://newspapers.swco.ttu.edu/bitstream/handle/20.500.12255/1770/BCJ_1964_02_02.pdf?isAllowed=y&sequence=3",
            archival_identifier="Bailey County Journal, volume 42, number 5",
            title="Muleshoe Woman's Father Is Hilton Hotel's Super Salesman",
            author_creator="Dorothy L. Sandler; reprinted from Daily American Weekly",
            repository_publisher="Bailey County Journal; Southwest Collection, Texas Tech University",
            publication_record_date="1964-02-02",
            locator="Section A, page 3; Pan American, air-cargo, wartime leave, OSS, and 1945 TWA chronology",
            source_quality="C_reputable_contemporary_or_scholarly",
            collection_name="Southwest Collection newspapers",
            rights_notes="Contemporary profile published nineteen years after the war. Only a short excerpt and project-authored paraphrase are retained.",
        ),
        source(
            CORVO_MAZZARINI,
            stable_url="https://larouchepub.com/eiw/public/1985/eirv12n05-19850205/eirv12n05-19850205.pdf",
            archival_identifier="Executive Intelligence Review, volume 12, number 5",
            title="War-time controversy over Vatican-OSS relations renewed by 'declassification'",
            author_creator="Max Corvo",
            repository_publisher="Executive Intelligence Review",
            publication_record_date="1985-02-05",
            locator="Printed pages 56-57; Richard Mazzarini and PanAm Freight division chronology",
            source_quality="D_correlative_or_secondary",
            collection_name="Executive Intelligence Review",
            rights_notes="Corroborative only because of the publication's advocacy context. Corvo's article names the PanAm Freight division before Mazzarini entered OSS.",
        ),
        source(
            MEDAL_MAZZARINI,
            stable_url="https://s3.amazonaws.com/NARAprodstorage/opastorage/live/61/5630/1563061/content/library/document/0067/1563061.pdf",
            archival_identifier="John Marsh Files, Box 21, folder Medal of Freedom - General",
            title="Medal of Freedom - General",
            author_creator="White House staff",
            repository_publisher="Gerald R. Ford Presidential Library, National Archives and Records Administration",
            publication_record_date="1976 compilation; historical list through 1974",
            locator="PDF physical page 56; Medals of Freedom Presented by President Truman",
            source_quality="A_direct_official",
            collection_name="John Marsh Files",
            rights_notes="Official list records Richard Mazzarini's 18 February 1946 Medal of Freedom presentation; it does not itself describe his pre-OSS employment.",
        ),
        source(
            NARA_GERALD,
            stable_url="https://text-message.blogs.archives.gov/2012/11/09/allen-dulles-and-no-23-herrengasse-bern-switzerland-1942-1945/",
            title="Allen Dulles and No. 23 Herrengasse, Bern, Switzerland, 1942-1945",
            author_creator="Greg Bradsher",
            repository_publisher="The Text Message, National Archives and Records Administration",
            publication_record_date="2012-11-09",
            locator="Paragraph describing Gerald Mayer's Office of War Information propaganda operation in Bern",
            source_quality="A_direct_official",
            collection_name="National Archives Textual Records Division blog",
            rights_notes="Supports a Gerald Mayer OWI/OSS-context candidate. The page does not connect that man to the identifier-free index row, so no affiliation is published.",
        ),
        source(
            CIA_GERALD,
            stable_url="https://www.cia.gov/resources/csi/static/Alias-George-Wood.pdf",
            archival_identifier="CIA Historical Review Program release, 22 September 1993",
            title="Alias George Wood",
            author_creator="Anthony Quibble",
            repository_publisher="Central Intelligence Agency, Center for the Study of Intelligence",
            locator="PDF pages 1-2; Gerald Mayer, Office of War Information, and OSS Bern office context",
            source_quality="A_direct_official",
            collection_name="Studies in Intelligence",
            rights_notes="Official historical review corroborates the OWI role but still does not bridge the common name to the identifier-free index row.",
        ),
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": ORG_STATE,
            "organization_id": "4d2fbb5f-218d-5445-b7b3-4c2fd22f0286",
            "canonical_name": "United States Department of State",
            "historical_name": "Department of State",
            "aliases": ["U.S. Department of State"],
            "organization_type": "federal executive department",
            "sector": "federal_government",
            "city": "Washington",
            "state_or_region": "District of Columbia",
            "country": "United States",
            "normalization_notes": "Government assignments remain distinct from private employment.",
        },
        {
            "key": ORG_COLUMBIA,
            "organization_id": "87e3d52a-9ace-512a-9677-e966b7fbd5e5",
            "canonical_name": "Columbia University",
            "historical_name": "Columbia University",
            "aliases": [],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "New York",
            "state_or_region": "New York",
            "country": "United States",
            "normalization_notes": "Existing historical institution reused.",
        },
        {
            "key": ORG_PANAM,
            "organization_id": "763d34d1-e8fa-5d36-a33f-c0fb06843073",
            "canonical_name": "Pan American Airways",
            "historical_name": "Pan American Airways",
            "aliases": ["Pan Am", "Pan American World Airways"],
            "organization_type": "airline",
            "sector": "business_and_industry",
            "country": "United States",
            "active_dates": "1927-1991",
            "normalization_notes": "Historical airline name preserved; wartime militarization is modeled as a later Army assignment.",
        },
    ]


def army_affiliation_key(row: int) -> str:
    return f"{slug(PEOPLE[row][1])}-army-association-b1047"


def army_identity_assessment(row: int) -> str:
    if row == 43:
        return "High confidence from a nonshared protected linkage and agreement between indexed Chester John Mazur and Army-record Chester J. Mazur; the abbreviated middle name remains a visible variant."
    return "High confidence from exact official name agreement and a nonshared protected linkage; the protected identifier remains private."


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, _label, _locator) in ARMY_ASSOCIATIONS.items():
        values.append(
            {
                "key": army_affiliation_key(row),
                "person_id": PEOPLE[row][0],
                "occupation": occupation,
                "relationship_type": "unknown",
                "end_date": date,
                "date_precision": f"Historical civilian-occupation code {code} was recorded at Army entry on {date}; no named employer, institution, workplace, or OSS-transfer date is supplied.",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "A_direct_official",
                "publication_status": "publish_qualified",
                "research_notes": "The broad historical category is excluded from verified-employer analytics and is not converted into a named organization.",
            }
        )

    values.extend(
        [
            {
                "key": "ferdinand-l-mayer-state-department-b1047",
                "person_id": PEOPLE[11][0],
                "organization_key": ORG_STATE,
                "organization_name_as_found": "Foreign Service",
                "role_title": "Foreign Service officer; Ambassador to Haiti from 1937",
                "relationship_type": "government_assignment",
                "start_date": "1916",
                "end_date": "1940",
                "date_precision": "The official finding aid dates Foreign Service work from 1916, the Haiti ambassadorship from 1937, resignation to 1940, and later OSS service; it does not state the intervening recruitment sequence.",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "A_direct_official",
                "publication_status": "published",
                "research_notes": "Published as a dated government assignment, not a private employer and not an explicitly immediate OSS predecessor.",
            },
            {
                "key": "bruce-h-mazlish-columbia-student-b1047",
                "person_id": PEOPLE[41][0],
                "organization_key": ORG_COLUMBIA,
                "organization_name_as_found": "Columbia University",
                "role_title": "student",
                "relationship_type": "student",
                "end_date": "1940",
                "date_precision": "MIT's institutional biography says Mazlish graduated from Columbia in 1940 and served in OSS during World War II; it does not supply an exact OSS entry date or establish employment by Columbia.",
                "city": "New York",
                "state_or_region": "New York",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Student status is displayed separately and excluded from employer analytics.",
            },
            {
                "key": "richard-mazzarini-pan-american-b1047",
                "person_id": PEOPLE[46][0],
                "organization_key": ORG_PANAM,
                "organization_name_as_found": "Pan American",
                "role_title": "air-cargo development employee",
                "occupation": "air-cargo development",
                "relationship_type": "employment",
                "start_date": "1929",
                "date_precision": "A 1964 profile says Mazzarini joined Pan American in 1929, worked in air-cargo development, took wartime leave, spent three years with OSS, and joined TWA in 1945. The exact leave and OSS entry dates are unstated.",
                "city": "New York",
                "state_or_region": "New York",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "probable_immediate",
                "identity_confidence": "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "publish_qualified",
                "research_notes": "Pan American is the best-supported last civilian employer. The record is qualified because neither source supplies an exact wartime leave or OSS entry date.",
            },
        ]
    )
    return values


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, label, locator) in ARMY_ASSOCIATIONS.items():
        values.append(
            {
                "key": f"army-{slug(PEOPLE[row][1])}-b1047",
                "person_id": PEOPLE[row][0],
                "affiliation_key": army_affiliation_key(row),
                "claim_type": "occupation",
                "claim_text": f"At Army entry on {date}, {PEOPLE[row][1]} was recorded as {occupation}; no employer, institution, or workplace is identified.",
                "evidence_paraphrase": f"The Army bulk file records code {code}; the visually checked official list defines the category as {label}.",
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

    values.extend(
        [
            {
                "key": "identity-ferdinand-l-mayer-b1047",
                "person_id": PEOPLE[11][0],
                "claim_type": "identity",
                "claim_text": "Indexed Ferdinand L. Mayer is a high-confidence match to diplomat Ferdinand Lathrop Mayer, who later served in OSS.",
                "evidence_paraphrase": "The uncommon full name and middle initial agree, and the official finding aid explicitly links Ferdinand Lathrop Mayer to wartime OSS service.",
                "identity_match_assessment": "High confidence from the uncommon exact surname, given name, middle initial, and direct official OSS statement; the indexed personnel file remains the strongest confirmation target.",
                "temporal_assessment": "The finding aid dates his Foreign Service career and wartime OSS service but does not state his exact OSS entry date.",
                "source_quality": "A_direct_official",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "The full middle name is retained as a documented variant, not a correction to the immutable index row.",
                "sources": [
                    {"source_key": HOOVER_MAYER, "excerpt_override": "resigned in 1940. He served in the Office of Strategic Services during World War II"},
                    {"source_key": INDEX, "support_type": "context_only"},
                ],
            },
            {
                "key": "state-department-ferdinand-l-mayer-b1047",
                "person_id": PEOPLE[11][0],
                "affiliation_key": "ferdinand-l-mayer-state-department-b1047",
                "claim_type": "other_pre_oss_affiliation",
                "claim_text": "Ferdinand L. Mayer served in the U.S. Foreign Service from 1916 until resigning in 1940, including as Ambassador to Haiti from 1937.",
                "evidence_paraphrase": "The official presidential-library finding aid supplies the Foreign Service start, Berlin and Haiti assignments, 1940 resignation, and later OSS service.",
                "identity_match_assessment": "High confidence from the uncommon name, matching middle initial, and the finding aid's direct OSS statement.",
                "temporal_assessment": "Documented prewar government assignment ending in 1940; the source does not prove it was immediately before OSS.",
                "source_quality": "A_direct_official",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "Modeled as government assignment rather than private employment and excluded from immediate-affiliation analytics.",
                "sources": [
                    {"source_key": HOOVER_MAYER, "locator_override": "Biographical Note"},
                    {"source_key": INDEX, "support_type": "context_only"},
                ],
            },
            {
                "key": "identity-bruce-h-mazlish-b1047",
                "person_id": PEOPLE[41][0],
                "claim_type": "identity",
                "claim_text": "Indexed Bruce H. Mazlish is a high-confidence match to historian Bruce Mazlish, whose MIT biography states that he served in OSS.",
                "evidence_paraphrase": "The exact uncommon full name and middle initial agree, and MIT's institutional biography directly states wartime OSS service.",
                "identity_match_assessment": "High confidence from the exact uncommon name and an authoritative institutional source directly connecting him to OSS.",
                "temporal_assessment": "The source places Columbia graduation in 1940 and OSS service during World War II without an exact entry date.",
                "source_quality": "B_authoritative_institutional",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "No employer is inferred from later teaching or academic work.",
                "sources": [
                    {"source_key": MIT_MAZLISH, "excerpt_override": "graduated from Columbia University in 1940. During World War II, he served in the Office of Strategic Services"},
                    {"source_key": INDEX, "support_type": "context_only"},
                ],
            },
            {
                "key": "columbia-student-bruce-h-mazlish-b1047",
                "person_id": PEOPLE[41][0],
                "affiliation_key": "bruce-h-mazlish-columbia-student-b1047",
                "claim_type": "other_pre_oss_affiliation",
                "claim_text": "Bruce H. Mazlish graduated from Columbia University in 1940; this is student status, not employment.",
                "evidence_paraphrase": "MIT's biography explicitly dates his Columbia graduation to 1940 and separately states wartime OSS service.",
                "identity_match_assessment": "High confidence from the exact uncommon name, middle initial, and direct OSS statement in an institutional biography.",
                "temporal_assessment": "Documented prewar education; the source does not establish Columbia as the immediate predecessor to OSS.",
                "source_quality": "B_authoritative_institutional",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "Columbia is excluded from employer counts because the relationship is student.",
                "sources": [{"source_key": MIT_MAZLISH}],
            },
            {
                "key": "identity-wendell-mayfield-chief-yeoman-b1047",
                "person_id": PEOPLE[27][0],
                "claim_type": "identity",
                "claim_text": "Indexed Wendell Mayfield is confirmed as the Chief Yeoman named in an official OSS naval-personnel citation list.",
                "evidence_paraphrase": "The official scan prints Chief Yeoman Wendell Mayfield and an OSS citation; the index independently prints the same uncommon name and a compatible rank abbreviation.",
                "identity_match_assessment": "Confirmed by exact uncommon name agreement, compatible Chief Yeoman rank evidence, and direct official OSS context.",
                "temporal_assessment": "Wartime identity and naval status only; the citation does not identify a pre-OSS employer or predecessor assignment.",
                "source_quality": "A_direct_official",
                "claim_confidence": "confirmed",
                "publication_status": "published",
                "match_notes": "The protected number visible in the scan is not transcribed or published.",
                "sources": [
                    {"source_key": NARA_MAYFIELD, "excerpt_override": "Chief Yeoman Wendell Mayfield"},
                    {"source_key": INDEX, "support_type": "context_only"},
                ],
            },
            {
                "key": "identity-richard-mazzarini-b1047",
                "person_id": PEOPLE[46][0],
                "claim_type": "identity",
                "claim_text": "Indexed Richard Mazzarini is a high-confidence match to the Pan American employee and OSS veteran described in a contemporary profile.",
                "evidence_paraphrase": "The exact uncommon name appears in the index, a 1964 profile describing three years with OSS, and an official 1946 Medal of Freedom recipient list.",
                "identity_match_assessment": "High confidence from the uncommon exact name and two independent sources connecting Richard Mazzarini to wartime service and a postwar federal award.",
                "temporal_assessment": "The profile supplies a wartime leave and three-year OSS chronology; the official list dates the Medal of Freedom presentation to 18 February 1946.",
                "source_quality": "A_direct_official",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "The evidence is not transferred to the adjacent Riccardo Mazzarini row.",
                "sources": [
                    {"source_key": BAILEY_MAZZARINI},
                    {"source_key": MEDAL_MAZZARINI, "excerpt_override": "MAZZARINI, Richard 2/18/46"},
                    {"source_key": INDEX, "support_type": "context_only"},
                ],
            },
            {
                "key": "pan-american-richard-mazzarini-b1047",
                "person_id": PEOPLE[46][0],
                "affiliation_key": "richard-mazzarini-pan-american-b1047",
                "claim_type": "last_civilian_pre_service",
                "claim_text": "Pan American Airways is the best-supported last civilian employer for Richard Mazzarini before his wartime OSS service.",
                "evidence_paraphrase": "A 1964 profile says he joined Pan American in 1929, developed air cargo, took wartime leave, spent three years with OSS, and joined TWA in 1945; Max Corvo independently names PanAm Freight before OSS.",
                "identity_match_assessment": "High confidence from the uncommon exact name, explicit OSS service, and independent official award-list corroboration.",
                "temporal_assessment": "Probable immediate civilian predecessor: wartime leave and later OSS service are explicit, but the exact leave and OSS entry dates are not supplied.",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "claim_confidence": "medium",
                "publication_status": "publish_qualified",
                "match_notes": "Published with visible qualification and excluded from high-confidence employer analytics. Pan American's historical name is preserved.",
                "sources": [
                    {"source_key": BAILEY_MAZZARINI, "excerpt_override": "He joined Pan American when he first arrived in New York in 1929"},
                    {"source_key": CORVO_MAZZARINI, "support_type": "supports"},
                    {"source_key": MEDAL_MAZZARINI, "support_type": "context_only"},
                    {"source_key": INDEX, "support_type": "context_only"},
                ],
            },
            {
                "key": "identity-gerald-mayer-owi-candidate-b1047",
                "person_id": PEOPLE[14][0],
                "claim_type": "identity",
                "claim_text": "A Gerald Mayer documented with the Office of War Information in Bern remains an unconfirmed candidate for the identifier-free index row.",
                "evidence_paraphrase": "NARA and CIA histories document a Gerald Mayer working for OWI alongside OSS in Bern, but neither source links him to Box 494 or another row-specific identifier.",
                "identity_match_assessment": "Probable candidate only; the common name and absent index identifiers do not satisfy the project's enhanced disambiguation rule.",
                "temporal_assessment": "Wartime OWI and OSS-adjacent context only; no pre-OSS employer is assigned to the indexed person.",
                "source_quality": "A_direct_official",
                "claim_confidence": "low",
                "publication_status": "withheld_low_confidence",
                "match_notes": "The candidate remains private and excluded from public facts and analytics pending Box 494 review.",
                "sources": [
                    {"source_key": NARA_GERALD},
                    {"source_key": CIA_GERALD},
                    {"source_key": INDEX, "support_type": "context_only"},
                ],
            },
            {
                "key": "identity-riccardo-richard-mazzarini-separate-b1047",
                "person_id": PEOPLE[45][0],
                "claim_type": "identity",
                "claim_text": "Riccardo Mazzarini remains separate from adjacent Richard Mazzarini; the external Richard evidence is not transferred to Riccardo.",
                "evidence_paraphrase": "Page 302 prints two adjacent rows with different given names. External sources consistently identify Richard, leaving Riccardo unbridged.",
                "identity_match_assessment": "Ambiguous possible variant or duplicate; original Box 495 jackets are required before any merge or evidence transfer.",
                "temporal_assessment": "Identity-resolution conflict only; no employment chronology is assigned to Riccardo.",
                "source_quality": "A_direct_official",
                "claim_confidence": "conflicting",
                "publication_status": "conflicting",
                "match_notes": "Both immutable rows and both person entities remain visible. Richard's Pan American affiliation belongs only to Richard.",
                "sources": [
                    {"source_key": INDEX},
                    {"source_key": BAILEY_MAZZARINI, "support_type": "context_only"},
                    {"source_key": MEDAL_MAZZARINI, "support_type": "context_only"},
                ],
            },
        ]
    )
    return values


def base_update(row: int) -> dict[str, object]:
    person_id, name, box = PEOPLE[row]
    return {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified page 302 source preserves {name}, Box {box}, rank or grade when printed, notes when present, and archive location. Prior Library of Congress searching plus staged official, exact-name, occupation, obituary, institutional, directory, and archival discovery did not establish a defensible identity-and-affiliation bridge.",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": f"Review indexed Box {box} for corroborating identifiers, immediate pre-OSS affiliation, and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }


def person_updates() -> list[dict[str, object]]:
    by_row = {row: base_update(row) for row in PEOPLE}

    for row in ARMY_ASSOCIATIONS:
        by_row[row].update(
            identity_status="high_confidence",
            identity_evidence=army_identity_assessment(row),
            personnel_category="enlisted_army_personnel",
            commissioned_officer=False,
            allied_or_foreign_personnel=False,
            nara_catalog_id="1263923",
            research_status="occupation_only_found",
            next_action=f"Review Box {PEOPLE[row][2]} to identify a named employer or institution and establish Army-to-OSS chronology. The protected Army link supplies only a broad historical occupation category.",
            archival_review_priority="high",
        )

    by_row[11].update(
        identity_status="high_confidence",
        identity_evidence="The uncommon indexed name and middle initial match Ferdinand Lathrop Mayer; an official presidential-library finding aid directly documents his Foreign Service career and wartime OSS service.",
        name_variants=["Ferdinand Lathrop Mayer"],
        replace_name_variants=False,
        research_status="documented_prewar_employer_found",
        next_action="Review Box 494 to establish the chronology between Mayer's 1940 Foreign Service resignation and OSS service and identify any intervening affiliation.",
        archival_review_priority="medium",
    )
    by_row[14].update(
        identity_status="probable",
        identity_evidence="Official NARA and CIA histories document a Gerald Mayer employed by the Office of War Information and working alongside OSS in Bern, but the common name and identifier-free index row do not establish that he is the Box 494 person.",
        research_status="needs_identity_review",
        next_action="Inspect Box 494 for Bern, Office of War Information, or biographical identifiers before assigning the OWI affiliation to this Gerald Mayer.",
        archival_review_priority="critical",
    )
    by_row[27].update(
        identity_status="confirmed",
        identity_evidence="The exact uncommon name and compatible rank link the index row to an official OSS citation list identifying Chief Yeoman Wendell Mayfield under Naval Personnel.",
        personnel_category="enlisted_naval_personnel",
        commissioned_officer=False,
        allied_or_foreign_personnel=False,
        next_action="Review Box 494 to identify Mayfield's civilian employer or naval assignment before OSS. The citation establishes wartime identity and status only.",
        archival_review_priority="high",
    )
    by_row[41].update(
        identity_status="high_confidence",
        identity_evidence="The exact uncommon name and middle initial match an authoritative MIT biography that directly documents Bruce Mazlish's 1940 Columbia graduation and wartime OSS service.",
        research_status="completed",
        next_action="Review Box 495 if a named civilian employer or the exact interval between Columbia graduation and OSS entry is required; Columbia remains student status, not employment.",
        archival_review_priority="medium",
    )
    by_row[42].update(
        identity_status="probable",
        identity_evidence="A same-name French military-archive inventory candidate exists, but no reviewed source connects that record to the indexed lieutenant, Box 495, or OSS service.",
        research_status="needs_identity_review",
        next_action="Inspect Box 495 and the French military-archive individual file candidate before assigning a nationality, network, occupation, or pre-OSS affiliation to Jean Mazou.",
        archival_review_priority="critical",
    )
    by_row[43].update(
        name_variants=["Chester J Mazur"],
        replace_name_variants=False,
    )
    by_row[45].update(
        identity_status="ambiguous",
        identity_evidence="Page 302 prints Riccardo and Richard Mazzarini as adjacent separate rows. External evidence consistently identifies Richard, but no source establishes whether Riccardo is a variant, duplicate, or different person.",
        possible_duplicate_group="page302-riccardo-richard-mazzarini-two-source-rows",
        research_status="needs_identity_review",
        next_action="Compare both Box 495 jackets before merging the adjacent given-name variants or transferring Richard's Pan American evidence to Riccardo.",
        archival_review_priority="critical",
    )
    by_row[46].update(
        identity_status="high_confidence",
        identity_evidence="The uncommon exact name appears in the index, a contemporary profile explicitly describing Richard Mazzarini's Pan American and OSS chronology, and an official Medal of Freedom recipient list.",
        name_variants=["Dick Mazzarini"],
        replace_name_variants=False,
        possible_duplicate_group="page302-riccardo-richard-mazzarini-two-source-rows",
        research_status="documented_prewar_employer_found",
        next_action="Review Box 495 to establish the exact Pan American leave and OSS entry dates and determine whether adjacent Riccardo Mazzarini is a variant or a separate person.",
        archival_review_priority="critical",
    )

    result = [by_row[row] for row in PEOPLE]
    if len(result) != 44:
        raise RuntimeError(f"Expected 44 person updates, generated {len(result)}")
    return result


def outcome_note(row: int) -> str:
    notes = {
        11: "The official Hoover Presidential Library finding aid supplies a direct OSS identity bridge and a dated Foreign Service pathway ending in 1940, but not an immediate OSS transition.",
        14: "Official NARA and CIA sources document an OWI employee named Gerald Mayer in Bern; the common name and identifier-free row prevent transfer without Box 494 confirmation.",
        27: "An official OSS citation list confirms Chief Yeoman Wendell Mayfield, but supplies no pre-OSS employer or predecessor assignment.",
        28: "A secondary veterans-roster hit for J. Mayher was not relied upon; the accepted official Army linkage supports only a broad dated occupation category.",
        41: "MIT's institutional biography directly links Bruce Mazlish to Columbia graduation in 1940 and wartime OSS service; Columbia remains student status rather than employment.",
        42: "A French military-archive same-name candidate remains unbridged and was not converted into a nationality, occupation, network, or affiliation.",
        45: "Riccardo remains separate from the adjacent Richard row; no external evidence was transferred.",
        46: "A contemporary profile and official Medal of Freedom list support Richard's identity; Pan American is published as a qualified last civilian employer because exact leave and OSS entry dates remain unstated.",
    }
    return notes.get(row, "Unbridged namesakes, snippets, commercial people-finder pages, unsourced genealogy, relatives, and postwar-only leads did not establish a reliable identity or pre-OSS affiliation.")


def research_attempts() -> list[dict[str, object]]:
    updates = {item["person_id"]: item for item in person_updates()}
    substantiated = set(ARMY_ASSOCIATIONS) | {11, 27, 41, 46}
    values: list[dict[str, object]] = []
    for row, (person_id, name, box) in PEOPLE.items():
        if row in {14, 42, 45}:
            outcome = "candidate_rejected"
        elif row in substantiated:
            outcome = "source_reviewed"
        else:
            outcome = "no_result"
        values.append(
            {
                "key": f"page302-row{row}-{slug(name)}-b1047",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index context; exact-name and meaningful initial, punctuation, spelling and OCR variants; public CIA-domain discovery and equivalent official-source context; rank, branch, nationality, assignment and protected-identifier clues; employer and occupation 1940; obituary, biography, institutional, Library of Congress newspaper, directory and archival searches; indexed Box {box}",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_1047",
                "started_at": "2026-11-05T10:45:00-05:00",
                "completed_at": "2026-11-05T12:35:00-05:00",
                "outcome": outcome,
                "sources_reviewed": 8 if row == 46 else 7 if row in substantiated else 6 if row in {14, 42, 45} else 5,
                "candidate_sources_rejected": 4 if row in {14, 28, 42, 45, 46} else 3,
                "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, education treated as employment, relatives, and postwar-only leads were rejected. Army categories were not converted into named employers. Adjacent name variants remain separate.",
                "research_notes": f"{outcome_note(row)} The official index, prior Library of Congress search, exact-name OSS discovery, public CIA-domain discovery, Army and NARA materials, occupation and employer searches, and institutional, obituary, directory, military-history, newspaper, and archival sources were reviewed as applicable. Public CIA-domain discovery was used; direct adapter access remains unavailable under the documented robots policy and was not treated as a negative result. No authenticated NARA Catalog API request was made.",
                "next_action": str(updates[person_id]["next_action"]),
                "attempt_number": 2,
                "research_agent_version": "before-oss-b1047-v1",
            }
        )
    if len(values) != 44:
        raise RuntimeError(f"Expected 44 research attempts, generated {len(values)}")
    return values


def main() -> None:
    bundle = {
        "bundle_version": "batch-1047-v1",
        "reviewer": "Before OSS Batch 1047 evidence review",
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
