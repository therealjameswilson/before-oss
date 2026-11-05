#!/usr/bin/env python3
"""Generate the reviewed Batch 1038 evidence bundle for PDF page 293."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page293-james-p-mann-to-kenneth-mar-review_"
    "batch-1038_2026-11-04.json"
)

INDEX = "nara-index-b1038"
ARMY = "army-bulk-b1038"
TECH = "army-tech-b1038"
CODES = "army-codes-b1038"
MANSION = "ordre-liberation-jacques-mansion-b1038"
MAX_MANUS = "snl-max-manus-b1038"
ANDRE_MANUEL = "fondation-resistance-andre-manuel-b1038"
EMILE_MANUELLO = "shd-emile-manuello-b1038"
NEVIO_MANZANI = "unt-nevio-manzani-b1038"

ORG_RENAULT = "renault-b1038"


PEOPLE = {
    1: ("26cf8d42-c611-5e2e-9494-df7b213bc134", "James P Mann", "479"),
    2: ("6e4d747e-fb3a-5297-8318-bb7b239fbd02", "John P Mann Jr.", "479"),
    3: ("ebf32d58-2fca-596e-b023-717ffeebec20", "Kenneth D Mann", "479"),
    4: ("be07a4a6-942f-5bee-b77d-4162eede4846", "Mary H Mann", "479"),
    5: ("d77b3503-6118-593b-995d-8273ec05c372", "Robert T Mann", "479"),
    6: ("1d7e9f2e-3403-5ee1-ac16-e9fcfb97bf4f", "William L Mann", "480"),
    7: ("5e9ed945-e214-53e1-8c83-3446dbd8db3c", "John W Manners", "480"),
    8: ("392fe164-4c4f-5874-98e4-b5fc5fba6129", "Cyrus E Manniere", "480"),
    9: ("68cd1001-097f-596c-9961-a17da3bdb505", "Daniel A Manning", "480"),
    10: ("167f52e8-f2d9-57f3-8f71-aebe47df3717", "Harold G Manning", "480"),
    11: ("43d0bb66-4c39-5627-85a1-3a85350d973d", "Howard E Manning", "480"),
    12: ("6dbad887-2256-5362-ab3b-688c6f87ea83", "John J Manning", "480"),
    13: ("03537667-9ea3-5c9a-b7ab-ee33af2d0d6b", "Thomas J Manning", "480"),
    14: ("5ddf4d80-7af1-5078-9b50-06a9e0705a8d", "Michael Manno", "480"),
    15: ("e39610c5-3508-5326-b6e8-7bc7f5844670", "Marcus Manoloe", "480"),
    16: ("798d689f-47f0-5a82-8431-3139452a1f57", "Pauline G Manos", "480"),
    17: ("a0fa5bdb-b8ea-5687-9795-d96fd9bd71be", "William Manousos", "480"),
    18: ("a2b09cb6-3b53-5af4-8fb3-31671036b628", "Harold Mansfield", "480"),
    19: ("7addede0-b9db-5f54-a831-77428d8df269", "Harry N Mansfield", "480"),
    20: ("ab408e1e-c431-558f-8d36-5d6fac3e63db", "Muriel E Mansfield", "480"),
    21: ("93870392-6c06-5b81-84a2-3257240f5c83", "Walter R Mansfield", "480"),
    22: ("5cd35483-b9f5-554f-928b-9bce1cf63709", "Jacques Mansion", "480"),
    23: ("184947d7-a92b-5a0f-823f-54956bb5d535", "Pauline Manson", "480"),
    24: ("48867a9a-9f06-5030-81f9-0dd9653fd321", "Robert S Mantho", "480"),
    25: ("fed59067-6662-5984-af15-0e36427b43a3", "* Manthos", "480"),
    26: ("0698f5a2-a00e-5fd7-b858-8760f5151f0b", "George Mantikas", "480"),
    27: ("2af0ccb5-311e-5a96-99eb-3d85a88b16db", "Peter A Manto", "480"),
    28: ("50e5bbea-fcf9-5999-abf6-86dd08906329", "Homer D Mantooth Jr.", "480"),
    29: ("b29a2bfc-73e5-5f2a-a5fe-0f7544c43dd4", "Donald E Mantz", "480"),
    30: ("125584b9-05ce-5833-a0db-f9550d80946d", "James F Mantz", "480"),
    31: ("974a420d-0ec8-5cde-ad74-70357b5d6f2a", "John Manual", "534"),
    32: ("04af8d16-7199-5e3f-86b7-5a0025b8b4fa", "Andre Manuel", "481"),
    33: ("b41a0277-8b4b-5ede-a54f-b31d603462ef", "Frank E Manuel", "481"),
    34: ("eb3e155b-ef45-5aee-a023-198f1d69f4b1", "Emile Manuello", "481"),
    35: ("d4accc1a-ac40-56e8-87d8-614932c6bf63", "John O Manula", "481"),
    36: ("4dde52b0-59f6-5901-912f-6dee1395b614", "Max Manus", "481"),
    37: ("48e597d6-7582-55a7-b40f-38a4add8b3c0", "Louis P Manusos", "481"),
    38: ("42d404a2-81e4-5d78-8d11-2e288215e30d", "Michael P Manusos", "481"),
    39: ("e4018ad8-7c06-53df-8436-dbc98b4bd1c1", "Nevio J Manzani", "481"),
    40: ("b8f268d0-c860-51b9-b5af-c565bb762c61", "Carl R Manzi", "481"),
    41: ("0e07e1b0-01c5-5f68-b19a-a7e83febd878", "Peter J Manzione", "481"),
    42: ("d00f6968-ba9f-5e29-9214-2e8d9e65bb8a", "Vincenzo J Manzo", "481"),
    43: ("2265bcdd-ddb7-5765-b661-c21449c36949", "Doreen Mao", "481"),
    44: ("9d8076ef-a817-5eca-95b7-48a5e4bbc860", "Jack D Mapes", "481"),
    45: ("12d914e2-a8a4-55b3-8fbc-53dbc701b7ce", "Caroline E Maphis", "481"),
    46: ("aa60fe3c-1995-5dac-9b6d-a94b65fe24af", "Kenneth Mar", "481"),
}

REVIEW_ROWS = tuple(row for row in PEOPLE if row != 11)

# These are broad historical categories recorded at Army entry. They do not
# identify an employer, institution, workplace, or the Army-to-OSS sequence.
ARMY_ASSOCIATIONS = {
    5: ("1943-02-24", "992", "student", "Students", "student", "PDF physical page 304; corrected historical category 9-92"),
    7: ("1941-12-30", "137", "stenographer or typist", "Stenographers and typists", "unknown", "PDF physical page 171; historical category 1-37"),
    10: ("1943-09-02", "736", "driver or chauffeur", "Drivers and chauffeurs, bus, taxi, truck, and tractor", "unknown", "PDF physical page 175; historical category 7-36"),
    14: ("1942-07-11", "444", "compositor or typesetter", "Compositors and typesetters", "unknown", "PDF physical page 173; historical category 4,6-44"),
    17: ("1943-06-07", "221", "bartender", "Bartenders", "unknown", "PDF physical page 172; historical category 2-21"),
    19: ("1944-09-04", "992", "student", "Students", "student", "PDF physical page 304; corrected historical category 9-92"),
    27: ("1942-12-01", "627", "worker in fabrication of textile products, not elsewhere classified", "Occupations in fabrication of textile products, n.e.c.", "unknown", "PDF physical page 173; historical category 6,8-27"),
    29: ("1942-03-07", "736", "driver or chauffeur", "Drivers and chauffeurs, bus, taxi, truck, and tractor", "unknown", "PDF physical page 175; historical category 7-36"),
    40: ("1943-05-22", "232", "barber, beautician, or manicurist", "Barbers, beauticians, and manicurists", "unknown", "PDF physical page 172; historical category 2-32"),
    41: ("1942-11-28", "098", "manager or official, not elsewhere classified", "Managers and officials, n.e.c.", "unknown", "PDF physical page 171; historical category 0-98"),
}

ARMY_IDENTITY_ONLY = {
    35: ("1943-03-06", "Occupation code 047 is absent from the visually checked official list and is not interpreted."),
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
            archival_identifier="RG 226, Entry A1-224, Boxes 479-481 and 534",
            title="OSS Personnel Files from Excel",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="2010-12-23",
            locator="PDF page 293, rows 1-46; page and every printed row visually checked at 180 dpi",
            source_quality="A_direct_official",
            collection_name="Records of the Office of Strategic Services, Record Group 226",
            rights_notes="All 46 printed rows remain separate. The Cyrus E. Manniere rank-column number and incomplete Manthos name are preserved without silent correction.",
        ),
        source(
            ARMY,
            stable_url="https://catalog.archives.gov/id/1263923",
            archival_identifier="National Archives Identifier 1263923; parent series NAID 604357",
            title="Electronic Army Serial Number Merged File, ca. 1938-1946",
            author_creator="Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="1938-1946; merged file created 2002",
            locator="Official unrestricted ASNEF.FIN.DAT; nineteen Batch 1038 candidates explicitly reviewed; twelve accepted and seven rejected",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records",
            document_number="ASNEF.FIN.DAT",
            rights_notes="No raw record, full protected identifier, or bulk-record ordinal is retained in public assets. Two duplicate Michael Manno rows were both reviewed explicitly.",
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
            locator="PDF physical pages 171-175 and 304; all ten published categories visually checked; code 047 absent",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records technical documentation",
            rights_notes="Historical categories identify neither employer, institution, workplace, nor exact Army-to-OSS sequence. Code 047 is not interpreted.",
        ),
        source(
            MANSION,
            stable_url="https://www.ordredelaliberation.fr/fr/compagnons/jacques-mansion",
            title="Jacques MANSION",
            author_creator="Ordre de la Libération",
            repository_publisher="Ordre de la Libération et son Musée",
            publication_record_date="Biographical notice based on the Order's archives",
            locator="Biographie; Renault Sales Service and September 1939 mobilization chronology",
            source_quality="A_direct_official",
            collection_name="Compagnons de la Libération",
            rights_notes="The official biography directly dates Renault employment before mobilization, but does not establish the exact later transition into an OSS-indexed file.",
        ),
        source(
            MAX_MANUS,
            stable_url="https://snl.no/Max_Manus",
            title="Max Manus – motstandsmann og forretningsdrivende",
            author_creator="Frode Færøy and Arnfinn Moland, Forsvarshistorisk museum",
            repository_publisher="Store norske leksikon",
            publication_record_date="Continuously updated institutional biography",
            locator="Bakgrunn; September-November 1939 chronology",
            source_quality="B_authoritative_institutional",
            collection_name="Store norske leksikon",
            rights_notes="The biography identifies his father's flower business but does not supply the firm's name.",
        ),
        source(
            ANDRE_MANUEL,
            stable_url="https://www.fondationresistance.org/wp-content/uploads/2025/05/LettreResistance050.pdf",
            title="La Lettre de la Fondation de la Résistance, no. 50",
            repository_publisher="Fondation de la Résistance",
            publication_record_date="2007-09",
            locator="PDF physical page 5; BCRA and SOE discussion naming André Manuel as Passy's deputy; visually checked at 180 dpi",
            source_quality="B_authoritative_institutional",
            collection_name="La Lettre de la Fondation de la Résistance",
            rights_notes="Supports wartime BCRA identity only; it does not identify a civilian employer or exact OSS-file relationship.",
        ),
        source(
            EMILE_MANUELLO,
            stable_url="https://museedelaresistanceenligne.org/doc/pdf/ressource_source/243.pdf",
            archival_identifier="GR 28 P 4 522/34; GR 16 P 390360",
            title="Archives de la France combattante: Dossiers individuels des agents des réseaux et des mouvements",
            author_creator="Jérôme Blondet et al., under the direction of Frédéric Quéguineur",
            repository_publisher="Service historique de la Défense",
            publication_record_date="2017",
            locator="PDF physical page 127; exact-name 1944 Emile Manuello dossier entry; visually checked at 170 dpi",
            source_quality="A_direct_official",
            collection_name="GR 28 P 4, Archives de la France combattante",
            rights_notes="An archival lead, not proof that the French file and indexed OSS file represent the same person; no employer is inferred.",
        ),
        source(
            NEVIO_MANZANI,
            stable_url="https://texashistory.unt.edu/ark:/67531/metadc2331674/",
            title="Captain Edwin DuBose Oral History Interview, Appendix: The Dostler Case",
            author_creator="University of North Texas Oral History Collection; After the Battle, no. 94",
            repository_publisher="University of North Texas Digital Library",
            publication_record_date="Interview 1997; appendix article 1996",
            locator="PDF physical page 51, article page 11; Captain Nevio J. Manzani and 2671st Special Reconnaissance Battalion, OSS; visually checked at 170 dpi",
            source_quality="B_authoritative_institutional",
            collection_name="Admiral Nimitz Museum and University of North Texas Oral History Collection",
            rights_notes="Supports wartime OSS identity and unit only; it does not identify a pre-OSS employer or preceding assignment.",
        ),
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": ORG_RENAULT,
            "canonical_name": "Renault",
            "historical_name": "Société Anonyme des Usines Renault",
            "aliases": ["Renault Sales Service"],
            "organization_type": "automobile manufacturer",
            "sector": "business_and_industry",
            "city": "Paris",
            "country": "France",
            "active_dates": "Historical employer name used in the late 1930s",
            "normalization_notes": "The source wording 'Service Vente de Renault à Paris' is preserved on the affiliation. No modern corporate successor is substituted.",
        }
    ]


def army_affiliation_key(row: int) -> str:
    return f"{slug(PEOPLE[row][1])}-army-association-b1038"


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
                "key": "jacques-mansion-renault-b1038",
                "person_id": PEOPLE[22][0],
                "organization_key": ORG_RENAULT,
                "organization_name_as_found": "Service Vente de Renault à Paris",
                "role_title": "controller in the Sales Service",
                "occupation": "sales-service controller",
                "relationship_type": "employment",
                "end_date": "1939-09",
                "date_precision": "The official biography places Renault employment before mobilization in September 1939; intervening French military and intelligence service followed.",
                "city": "Paris",
                "country": "France",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "A_direct_official",
                "publication_status": "published",
                "research_notes": "Renault is the best-supported last civilian employer before wartime service, not the immediate predecessor to the later OSS-indexed relationship.",
            },
            {
                "key": "max-manus-father-flower-business-b1038",
                "person_id": PEOPLE[36][0],
                "organization_name_as_found": "his father's flower business",
                "role_title": "worker in his father's flower business",
                "occupation": "flower-business worker",
                "relationship_type": "employment",
                "start_date": "1939-09",
                "end_date": "1939-11 or later",
                "date_precision": "The institutional biography states that Manus worked in his father's flower business after returning to Norway in September 1939 and then volunteered for Finland after the November invasion.",
                "city": "Oslo area",
                "country": "Norway",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "The employer is preserved exactly at the level supported by the source; no business name is invented.",
            },
        ]
    )
    return values


def army_identity_assessment(row: int) -> str:
    duplicate_note = " Two duplicate official Army rows agree on all publishable fields and were both accepted explicitly." if row == 14 else ""
    return "Confirmed by exact official name agreement and a nonshared protected linkage; the protected identifier remains private." + duplicate_note


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, label, relationship, locator) in ARMY_ASSOCIATIONS.items():
        values.append(
            {
                "key": f"army-{slug(PEOPLE[row][1])}-b1038",
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
    values.append(
        {
            "key": "identity-john-o-manula-army-b1038",
            "person_id": PEOPLE[35][0],
            "claim_type": "identity",
            "claim_text": "Indexed John O. Manula is a reviewed match to the official Army record.",
            "evidence_paraphrase": "A nonshared protected linkage and exact name agreement connect the index and Army record; no full identifier or raw record is published.",
            "identity_match_assessment": army_identity_assessment(35),
            "temporal_assessment": "Army entry is dated March 6, 1943. Occupation code 047 is absent from the visually checked list and is not interpreted.",
            "source_quality": "A_direct_official",
            "claim_confidence": "confirmed",
            "publication_status": "published",
            "match_notes": "Identity evidence only; the unsupported code is not converted into occupation or affiliation evidence.",
            "sources": [
                {"source_key": INDEX},
                {"source_key": ARMY},
                {"source_key": TECH, "support_type": "context_only"},
                {"source_key": CODES, "support_type": "context_only"},
            ],
        }
    )
    values.extend(
        [
            {
                "key": "identity-jacques-mansion-b1038",
                "person_id": PEOPLE[22][0],
                "claim_type": "identity",
                "claim_text": "Indexed Jacques Mansion is high-confidence identified as the Free French BCRA officer and Companion of the Liberation.",
                "evidence_paraphrase": "The official biography gives the exact name, French intelligence chronology, repeated special missions, and later captain rank.",
                "identity_match_assessment": "High confidence from the uncommon exact name, French allied-intelligence context, and an official wartime biography; the Box 480 file remains unreviewed.",
                "temporal_assessment": "The biography dates military and intelligence activity from 1939 through 1945.",
                "source_quality": "A_direct_official",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "The official chronology is highly specific, but the indexed personnel file is still needed to establish the exact OSS administrative relationship.",
                "sources": [{"source_key": MANSION}, {"source_key": INDEX, "support_type": "context_only"}],
            },
            {
                "key": "renault-jacques-mansion-b1038",
                "person_id": PEOPLE[22][0],
                "affiliation_key": "jacques-mansion-renault-b1038",
                "claim_type": "last_civilian_pre_service",
                "claim_text": "Jacques Mansion's best-supported last civilian employer before wartime service was Renault's Sales Service in Paris.",
                "evidence_paraphrase": "The official biography places his Renault Sales Service controller position immediately before September 1939 mobilization.",
                "identity_match_assessment": "High confidence from the uncommon exact name and detailed official French intelligence biography.",
                "temporal_assessment": "Strongly date-bounded as the last civilian employment before military service; intervening service means it is not labeled immediate pre-OSS.",
                "source_quality": "A_direct_official",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "Employer and role are preserved in the source's historical wording.",
                "sources": [{"source_key": MANSION}],
            },
            {
                "key": "identity-max-manus-b1038",
                "person_id": PEOPLE[36][0],
                "claim_type": "identity",
                "claim_text": "Indexed Lieutenant Max Manus is high-confidence identified as Norwegian resistance member Maximo Guillermo Manus.",
                "evidence_paraphrase": "The institutional biography gives the distinctive name and documents his Finnish service, Norwegian resistance, and Kompani Linge service.",
                "identity_match_assessment": "High confidence from the distinctive exact name, compatible lieutenant context, and authoritative Allied special-operations chronology.",
                "temporal_assessment": "The biography dates his civilian work and successive wartime service from 1939 onward.",
                "source_quality": "B_authoritative_institutional",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "The Box 481 file remains necessary to determine why the Allied officer appears in the OSS personnel index.",
                "sources": [{"source_key": MAX_MANUS}, {"source_key": INDEX, "support_type": "context_only"}],
            },
            {
                "key": "flower-business-max-manus-b1038",
                "person_id": PEOPLE[36][0],
                "affiliation_key": "max-manus-father-flower-business-b1038",
                "claim_type": "last_civilian_pre_service",
                "claim_text": "Max Manus's best-supported last civilian employer before wartime service was his father's flower business.",
                "evidence_paraphrase": "The biography places work in his father's flower business after his September 1939 return and before volunteering for Finland.",
                "identity_match_assessment": "High confidence from the distinctive exact name and compatible Allied special-operations chronology.",
                "temporal_assessment": "Strongly date-bounded as his last documented civilian employment before military service; the firm's name is not supplied.",
                "source_quality": "B_authoritative_institutional",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "No organization is normalized beyond the source; the unnamed family business remains explicit.",
                "sources": [{"source_key": MAX_MANUS}],
            },
            {
                "key": "identity-andre-manuel-b1038",
                "person_id": PEOPLE[32][0],
                "claim_type": "identity",
                "claim_text": "Indexed Lieutenant Colonel Andre Manuel is high-confidence identified as André Manuel, Passy's BCRA deputy.",
                "evidence_paraphrase": "The Fondation de la Résistance names André Manuel as Passy's active deputy among BCRA leaders working with British special services.",
                "identity_match_assessment": "High confidence from the uncommon exact name, senior allied-intelligence context, and compatible indexed rank; the Box 481 file remains unreviewed.",
                "temporal_assessment": "Wartime BCRA identity evidence only; no civilian employer or exact transition into the indexed OSS relationship is established.",
                "source_quality": "B_authoritative_institutional",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "No discovery-only civilian-employment lead is published without a dated authoritative bridge.",
                "sources": [{"source_key": ANDRE_MANUEL}, {"source_key": INDEX, "support_type": "context_only"}],
            },
            {
                "key": "identity-emile-manuello-b1038",
                "person_id": PEOPLE[34][0],
                "claim_type": "identity",
                "claim_text": "A 1944 French resistance dossier for Emile Manuello is a qualified identity lead for indexed Lieutenant Emile Manuello.",
                "evidence_paraphrase": "The official SHD inventory lists an exact-name 1944 individual resistance dossier with archival references GR 28 P 4 522/34 and GR 16 P 390360.",
                "identity_match_assessment": "Probable but not conclusive: the rare exact name, 1944 date, and indexed French note align, but the two files have not been cross-compared.",
                "temporal_assessment": "The French dossier is dated 1944; it does not identify an employer or the exact OSS-file relationship.",
                "source_quality": "A_direct_official",
                "claim_confidence": "medium",
                "publication_status": "publish_qualified",
                "match_notes": "Published as an archival lead with explicit qualification; no affiliation is transferred.",
                "sources": [{"source_key": EMILE_MANUELLO}, {"source_key": INDEX, "support_type": "context_only"}],
            },
            {
                "key": "identity-nevio-manzani-b1038",
                "person_id": PEOPLE[39][0],
                "claim_type": "identity",
                "claim_text": "Indexed Captain Nevio J. Manzani is high-confidence identified as the OSS officer of the 2671st Special Reconnaissance Battalion.",
                "evidence_paraphrase": "A digitized historical account names Captain Nevio J. Manzani in an OSS investigation by the 2671st Special Reconnaissance Battalion.",
                "identity_match_assessment": "High confidence from the exact uncommon name with middle initial, matching captain rank, and direct OSS-unit context.",
                "temporal_assessment": "Wartime OSS identity and assignment evidence only; no preceding employer or unit transfer is established.",
                "source_quality": "B_authoritative_institutional",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "The Box 481 personnel file remains necessary to establish pre-OSS chronology.",
                "sources": [{"source_key": NEVIO_MANZANI}, {"source_key": INDEX, "support_type": "context_only"}],
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
        "identity_evidence": f"The visually verified page 293 source preserves {name}, Box {box}, rank or grade when printed, notes when present, and archive location. Staged official, exact-name, employment, occupation, obituary, institutional, newspaper, directory, and archival searches did not establish a defensible identity-and-affiliation bridge.",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": f"Review indexed Box {box} for corroborating identifiers, immediate pre-OSS affiliation, and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }


def person_updates() -> list[dict[str, object]]:
    updates = [base_update(row) for row in REVIEW_ROWS]
    by_row = {row: update for row, update in zip(REVIEW_ROWS, updates, strict=True)}

    for row in set(ARMY_ASSOCIATIONS) | set(ARMY_IDENTITY_ONLY):
        by_row[row].update(
            identity_status="confirmed",
            identity_evidence=army_identity_assessment(row),
            personnel_category="enlisted_army_personnel",
            commissioned_officer=False,
            allied_or_foreign_personnel=False,
            nara_catalog_id="1263923",
        )
        if row in ARMY_ASSOCIATIONS:
            by_row[row].update(
                research_status="occupation_only_found",
                next_action=f"Review Box {PEOPLE[row][2]} to identify a named employer or institution and establish Army-to-OSS chronology. The protected Army link supplies only a broad historical occupation or student-status category.",
            )
        else:
            by_row[row].update(
                next_action=f"Review Box {PEOPLE[row][2]} to establish the immediate pre-OSS affiliation and last civilian employer. The Army record is retained for identity only because code 047 is unsupported.",
            )

    by_row[8].update(
        identity_status="ambiguous",
        identity_evidence="Indexed Cyrus E. Manniere follows a separate Cyrus E. Manierre record on page 292. Page 293 also places a numeric value in Manniere's rank column. The rows remain separate and no Manierre claim is copied.",
        possible_duplicate_group="batch1038-cyrus-manniere-manierre-spelling",
        research_status="needs_identity_review",
        archival_review_priority="critical",
        next_action="Jointly review the Box 479 Cyrus E. Manierre file and Box 480 Cyrus E. Manniere record. Preserve the page 293 rank-column number without silent correction.",
    )
    for row, evidence, next_action in (
        (15, "A same-family Army lead was rejected because its name differs and its protected identifier is shared with the earlier Marcus Manaloe record; no fields were transferred.", "Jointly review the Marcus Manaloe and Marcus Manoloe files before accepting an Army identity or merging either spelling."),
        (24, "The exact-name Army lead was rejected because its protected identifier is shared with a different indexed person; no fields were transferred.", "Review Box 480 and the conflicting identifier-bearing records before accepting any Army identity or occupation for Robert S. Mantho."),
        (31, "The protected-linkage Army lead names a different person and shares that person's indexed identifier; no fields were transferred to John Manual.", "Review Box 534 and the conflicting identifier-bearing records before assigning an Army identity or occupation to John Manual."),
    ):
        by_row[row].update(
            identity_status="conflicting",
            identity_evidence=evidence,
            research_status="conflicting_sources",
            archival_review_priority="critical",
            next_action=next_action,
        )
    by_row[25].update(
        identity_status="unresolved",
        identity_evidence="The index prints only the surname Manthos with an asterisk and the note 'no first n'. No first name may be reconstructed from unrelated namesakes.",
        research_status="needs_identity_review",
        archival_review_priority="critical",
        next_action="Review Box 480 and the original index card to recover any given name or corroborating identifier before further research.",
    )
    by_row[44].update(
        identity_status="ambiguous",
        identity_evidence="The index prints Jack D. Mapes with the note 'or March'. Exact-name and variant leads did not establish which surname or identity is intended.",
        research_status="needs_identity_review",
        archival_review_priority="critical",
        next_action="Review Box 481 and the original index card to resolve the Mapes/March note before assigning any biography or affiliation.",
    )
    by_row[46].update(
        identity_status="ambiguous",
        identity_evidence="A protected-linkage Army candidate has a damaged, nonmatching name. It was rejected and no identity or occupation fields were transferred.",
        research_status="needs_identity_review",
        archival_review_priority="critical",
        next_action="Review Box 481 and the original identifier-bearing record before accepting or rejecting the damaged Kenneth Mar Army lead.",
    )
    by_row[22].update(
        identity_status="high_confidence",
        identity_evidence="The uncommon exact name and official French biography's detailed Free French and BCRA chronology support Jacques Mansion.",
        personnel_category="foreign_or_allied_military_personnel",
        commissioned_officer=True,
        allied_or_foreign_personnel=True,
        research_status="verified_employer_found",
        archival_review_priority="medium",
        next_action="Review Box 480 to establish Mansion's exact OSS administrative relationship and whether a later allied assignment immediately preceded it.",
    )
    by_row[32].update(
        identity_status="high_confidence",
        identity_evidence="The uncommon exact name, senior indexed rank, and Fondation de la Résistance account naming André Manuel as Passy's BCRA deputy support the identity.",
        name_variants=["André Manuel"],
        replace_name_variants=False,
        personnel_category="foreign_or_allied_military_personnel",
        commissioned_officer=True,
        allied_or_foreign_personnel=True,
        next_action="Review Box 481 and French service records to establish André Manuel's immediate pre-OSS affiliation and dated civilian employment chronology.",
    )
    by_row[34].update(
        identity_status="probable",
        identity_evidence="An official SHD inventory lists an exact-name 1944 French resistance dossier. The rare name and indexed French note align, but the two files have not been cross-compared.",
        personnel_category="foreign_or_allied_military_personnel",
        commissioned_officer=True,
        allied_or_foreign_personnel=True,
        research_status="needs_identity_review",
        archival_review_priority="critical",
        next_action="Compare Box 481 with SHD files GR 28 P 4 522/34 and GR 16 P 390360 before treating the French archival lead as the same person or publishing an affiliation.",
    )
    by_row[36].update(
        identity_status="high_confidence",
        identity_evidence="The distinctive exact name, compatible lieutenant context, and institutional chronology of Finnish, Norwegian resistance, and Kompani Linge service support Max Manus.",
        name_variants=["Maximo Guillermo Manus"],
        replace_name_variants=False,
        personnel_category="foreign_or_allied_military_personnel",
        commissioned_officer=True,
        allied_or_foreign_personnel=True,
        research_status="documented_prewar_employer_found",
        archival_review_priority="medium",
        next_action="Review Box 481 to establish the indexed OSS relationship and determine whether Kompani Linge or another allied assignment immediately preceded it.",
    )
    by_row[39].update(
        identity_status="high_confidence",
        identity_evidence="The exact uncommon name with middle initial, matching captain rank, and direct OSS 2671st Special Reconnaissance Battalion context support Nevio J. Manzani.",
        personnel_category="commissioned_army_officer",
        commissioned_officer=True,
        allied_or_foreign_personnel=False,
        next_action="Review Box 481 and unit records to identify Manzani's assignment immediately before the 2671st and his last civilian employer.",
    )

    if len(updates) != 45 or PEOPLE[11][0] in {item["person_id"] for item in updates}:
        raise RuntimeError("Expected 45 updates with Howard E. Manning excluded")
    return updates


def unresolved_reason(row: int) -> str:
    special = {
        8: "The adjacent Manierre/Manniere spellings and malformed rank-column value require joint file review.",
        15: "A different-name, shared-identifier Army lead was rejected and no fields were transferred.",
        22: "The official biography supports Renault as the last civilian employer before military service.",
        24: "A shared-identifier Army lead was rejected and no fields were transferred.",
        25: "The index supplies no first name, so namesake research cannot be assigned safely.",
        31: "A different-name, shared-identifier Army lead was rejected and no fields were transferred.",
        32: "Institutional history supports BCRA identity but not a dated civilian employer or exact OSS transition.",
        34: "The SHD exact-name dossier is retained as a qualified archival identity lead only.",
        36: "The institutional biography supports an unnamed family flower business as last civilian employment before wartime service.",
        39: "A digitized historical account supports exact OSS identity and unit, but not earlier employment.",
        44: "The index's Mapes-or-March note remains unresolved.",
        46: "The damaged-name Army candidate was rejected and no fields were transferred.",
    }
    return special.get(
        row,
        "Unbridged namesakes, snippets, commercial people-finder pages, unsourced genealogy, relatives, and postwar-only leads did not establish this indexed person's identity or pre-OSS affiliation.",
    )


def research_attempts() -> list[dict[str, object]]:
    updates = {item["person_id"]: item for item in person_updates()}
    substantiated = set(ARMY_ASSOCIATIONS) | set(ARMY_IDENTITY_ONLY) | {22, 32, 34, 36, 39}
    candidate_review = {8, 15, 24, 25, 31, 44, 46}
    values: list[dict[str, object]] = []
    for row in REVIEW_ROWS:
        person_id, name, box = PEOPLE[row]
        outcome = "source_reviewed" if row in substantiated else "candidate_found" if row in candidate_review else "candidate_rejected"
        values.append(
            {
                "key": f"page293-row{row}-{slug(name)}-b1038",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index context; exact-name and meaningful initial, suffix, alias, punctuation and OCR variants; OSS and CIA Reading Room; rank, branch, assignment and protected-identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory and archival searches; indexed Box {box}",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_1038",
                "started_at": "2026-11-04T21:50:00-05:00",
                "completed_at": "2026-11-04T23:35:00-05:00",
                "outcome": outcome,
                "sources_reviewed": 8 if row in substantiated else 5,
                "candidate_sources_rejected": 2 if row in substantiated else 4,
                "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, and postwar-only leads were rejected. Shared-identifier and different-name Army candidates were rejected. Army categories were not converted into named employers, and code 047 was not interpreted.",
                "research_notes": f"{unresolved_reason(row)} The official index, exact-name OSS searches, targeted CIA context, employment and occupation searches, and institutional, newspaper, obituary, directory, and archival searches were reviewed as applicable. Page 293 and cited PDF evidence pages were visually checked. No authenticated NARA Catalog API request was made.",
                "next_action": str(updates[person_id]["next_action"]),
                "attempt_number": 1,
                "research_agent_version": "before-oss-b1038-v1",
            }
        )
    if len(values) != 45:
        raise RuntimeError(f"Expected 45 research attempts, generated {len(values)}")
    return values


def main() -> None:
    bundle = {
        "bundle_version": "batch-1038-v1",
        "reviewer": "Before OSS Batch 1038 evidence review",
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
