#!/usr/bin/env python3
"""Generate the reviewed Batch 901 evidence bundle from audited constants."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "research/evidence-page440-spence-to-sperling-review_batch-901_2026-10-25.json"

INDEX = "nara-index-b901"
ARMY = "army-bulk-b901"
TECH = "army-tech-b901"
CODES = "army-codes-b901"
SHD_OFFICERS = "shd-officers-speraber-b901"
SHD_NETWORKS = "shd-network-agents-speraber-b901"
BPSGM_BIO = "bpsgm-speraber-biography-b901"
BPSGM_MASTER = "bpsgm-speraber-master-b901"
ASCSA_HISTORY = "ascsa-sperling-yale-history-b901"
ASCSA_REPORT = "ascsa-sperling-yale-report-b901"
SPERLING_OBIT = "nyt-peter-sperling-obituary-b901"
OSS_GREEK_DESK = "oss-greek-desk-sperling-b901"
MET_SPERLING = "met-harry-sperling-b901"
WKU_DOUGLAS = "wku-douglas-spencer-b901"


# One entry per active person entity. Deforest Spencer represents two immutable
# source rows (page 440 rows 26-27) that remain separately preserved.
PEOPLE = {
    24: ("22d683f2-1f51-5f72-bd72-6c32c48b325c", "Marion J Spence"),
    25: ("f10bbf26-3c73-5a67-bdef-a4d2031e6a11", "Barbara Spencer"),
    26: ("04e3c400-20f0-5310-8a53-13861ee5852c", "Deforest Spencer"),
    28: ("64a557ab-4806-578a-8cf9-7dcbe16d8f5e", "Dorothy M Spencer"),
    29: ("12d9239d-bfc4-54ac-9dea-c52c45a0a08d", "Douglas Spencer"),
    30: ("cd4cefc2-85f7-5b72-b512-7ab4630ecc85", "F A Spencer"),
    31: ("0aee7f4e-25fa-554d-ade5-3adae58fae59", "Floyd A Spencer"),
    32: ("c1d34e5d-03a2-5c25-a727-51d76d1da055", "Francis G Spencer"),
    33: ("1d7db4a2-d24b-5d93-8407-2c7e46fd0161", "Frank C Spencer"),
    34: ("cfbace4a-ab61-5db8-bd53-0624906d5b64", "Frank B Spencer"),
    35: ("d54593fb-3737-5c08-bd00-cd0db0a3ded0", "Frederick A Spencer"),
    36: ("c965acc6-eea1-5d31-9165-4875cde97520", "James D Spencer"),
    37: ("33eeca2a-bc78-591e-9820-1b8b45c3b415", "James A Spencer"),
    38: ("eeef63b2-e307-5c6b-8197-8a3b2c3edd71", "Joseph E Spencer"),
    39: ("cf325764-5e3e-519f-bc0d-8d8b62550bca", "Alphonse G Spera"),
    40: ("c0d3ce41-37b3-5f38-a560-6f0cfd7e1658", "Edmond Speraber"),
    41: ("bbd9eabc-f647-53d3-b725-02603c3f5ce4", "Sam G Speranza"),
    42: ("2b062f8b-e7fa-55b9-a4b5-9886e7dcb970", "Joseph Sperli"),
    43: ("3f149a8a-c316-5285-919a-d6de772bc833", "Anton E Sperling"),
    44: ("cfb993f1-85e2-5a55-bd98-57d8fcf9defc", "Harry G Sperling"),
    45: ("0d333e9e-e785-5e69-94af-8f0c4b72cb3b", "Harry G Sperling"),
    46: ("7836eecd-c4d8-5d41-b89c-6335b0180b0a", "Jerome Sperling"),
}


ARMY_OCCUPATIONS = [
    {
        "row": 33,
        "slug": "frank-c-spencer",
        "date": "1942-01-05",
        "code": "591",
        "occupation": "Foremen, manufacturing",
        "relationship_type": "employment",
        "locator": "PDF physical page 175; category 5-91",
    },
    {
        "row": 34,
        "slug": "frank-b-spencer",
        "date": "1943-10-16",
        "code": "101",
        "occupation": "Bookkeepers and cashiers, except bank cashiers",
        "relationship_type": "employment",
        "locator": "PDF physical page 171; category 1-01",
    },
    {
        "row": 37,
        "slug": "james-a-spencer",
        "date": "1943-03-13",
        "code": "992",
        "occupation": "Students",
        "relationship_type": "student",
        "locator": "PDF physical page 304; corrected Code No. 30 category 9-92",
    },
    {
        "row": 42,
        "slug": "joseph-sperli",
        "date": "1942-03-28",
        "code": "736",
        "occupation": "Chauffeurs and drivers, bus, taxi, truck, and tractor",
        "relationship_type": "employment",
        "locator": "PDF physical page 174; category 7-36",
    },
]


UNRESOLVED = {
    24: "Exact-name, middle-initial, OSS, employer, occupation, obituary, institutional and archival searches did not identify the indexed person.",
    25: "The name produced multiple chronologically plausible women but no source that bridges one of them to OSS, Box 732 or a prewar employer.",
    28: "Exact-name searches returned unbridged namesakes and no wartime identity, occupation or employer chronology.",
    30: "Initials-only searches could not separate the indexed person from many namesakes or establish a pre-OSS affiliation.",
    31: "The exact name produced military and civilian namesakes but no source with the identifiers required to select the indexed person.",
    32: "Exact-name and middle-initial searches did not produce a source connecting the indexed person to an employer or OSS assignment.",
    35: "Rank-aware searches did not identify the indexed lieutenant commander or a named pre-OSS naval assignment; the physical file is required.",
    36: "The common name produced many results without the additional identifiers required by the project's common-name rule.",
    38: "Rank-aware searches did not establish which Major Joseph E Spencer is represented or document his immediate pre-OSS assignment.",
    39: "Exact-name and spelling-variant searches did not yield a defensible OSS identity or prewar employer match.",
    41: "Exact-name searches returned later and unrelated namesakes but no wartime identity or employer bridge.",
    43: "The exact name produced no source with an OSS, Box 732, military or employer identifier sufficient for resolution.",
}


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 731-732",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 440, rows 24-46; checked against layout-preserving text and a rendered page image",
            "access_date": "2026-10-25",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain immutable, including two Deforest Spencer rows and two Harry G Sperling rows. Full protected identifiers remain private.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; four accepted protected-identifier matches and one damaged-name conflict",
            "access_date": "2026-10-25",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "No raw row or full protected identifier is retained in public assets. A non-hit is not negative proof, and coded occupations identify no employer.",
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
            "access_date": "2026-10-25",
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
            "locator": "PDF physical pages 170-175 and 304; categories 004, 101, 591, 736 and corrected 992 visually or textually checked",
            "access_date": "2026-10-25",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical labels identify neither employers nor workplaces and are published only as qualified occupation evidence.",
        },
        {
            "key": SHD_OFFICERS,
            "stable_url": "https://www.servicehistorique.sga.defense.gouv.fr/sites/default/files/2020-01/SHDGR_REP_8YE_O-Z.pdf",
            "archival_identifier": "Service historique de la Défense, sous-série GR 8 YE, cote GR 8 YE 487",
            "title": "Officiers supérieurs et subalternes: armée de Terre, Gendarmerie et services communs, lettres O à Z",
            "author_creator": "Service historique de la Défense",
            "repository_publisher": "Service historique de la Défense, Centre historique des archives, Vincennes",
            "publication_record_date": "2015",
            "locator": "Entry GR 8 YE 487: Edmond Charles Speraber, capitaine médecin, service de santé; visually checked in the rendered PDF",
            "access_date": "2026-10-25",
            "source_quality": "A_direct_official",
            "collection_name": "Sous-série GR 8 YE",
            "rights_notes": "The official register establishes the full name, rank, branch and file pointer; it does not by itself establish OSS service or civilian employment.",
        },
        {
            "key": SHD_NETWORKS,
            "stable_url": "https://www.servicehistorique.sga.defense.gouv.fr/sites/default/files/2019-10/SHDGR_INV_28P4_DOSSIERS_DES_AGENTS_DES_RESEAUX_0.pdf",
            "archival_identifier": "Service historique de la Défense, GR 28 P 4 253 / 141; cross-reference GR 16 P 555475",
            "title": "Dossiers individuels des agents des réseaux",
            "author_creator": "Service historique de la Défense",
            "repository_publisher": "Service historique de la Défense",
            "publication_record_date": "2017",
            "locator": "Entry GR 28 P 4 253 / 141, dossier individuel de Edmond Speraber, 1945",
            "access_date": "2026-10-25",
            "source_quality": "A_direct_official",
            "collection_name": "Sous-série GR 28 P 4",
            "rights_notes": "The finding aid establishes an individual resistance-network file and archival cross-reference; the file contents were not reviewed.",
        },
        {
            "key": BPSGM_BIO,
            "stable_url": "https://www.bpsgm.fr/dr-edmond-speraber-le-pere-tranquille-de-la-cote-basque/",
            "title": "Dr Edmond Speraber: Le Père Tranquille de la Côte basque",
            "author_creator": "Didier Raillard",
            "repository_publisher": "Association Basses-Pyrénées dans la Seconde Guerre mondiale",
            "publication_record_date": "2024-06-10",
            "locator": "Biography paragraphs describing medical training, Saint-Jean-de-Luz practice, 1939-1940 mobilization and January 1943 NANA responsibility",
            "access_date": "2026-10-25",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "BPSGM historical biographies",
            "rights_notes": "Project-authored paraphrases only. The article cites Jean Crouzet's biography in Aide-mémoire des années sombres.",
        },
        {
            "key": BPSGM_MASTER,
            "stable_url": "https://www.bpsgm.fr/laulhe-benoit-resistance-au-pays-basque-30-le-reseau-du-dr-edmond-speraber/",
            "title": "La Résistance au Pays Basque, fiche 30: Le réseau du Dr Edmond Speraber",
            "author_creator": "Benoit Laulhe",
            "repository_publisher": "Association Basses-Pyrénées dans la Seconde Guerre mondiale",
            "publication_record_date": "2001; online 2017-03-31",
            "locator": "Master's research, fiche 30; medical practice, 1939 service as capitaine médecin and August 1940 demobilization",
            "access_date": "2026-10-25",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "University of Pau and Pays de l'Adour master's research",
            "rights_notes": "Project-authored paraphrases only; the source directly describes the return to general practice after demobilization.",
        },
        {
            "key": ASCSA_HISTORY,
            "stable_url": "https://www.ascsa.edu.gr/index.php/archives/history-of-the-american-school-1882-1942-appendix-vi",
            "title": "History of the American School 1882-1942 - Appendix VI",
            "author_creator": "Louis E. Lord",
            "repository_publisher": "American School of Classical Studies at Athens",
            "publication_record_date": "1947",
            "locator": "Appendix VI, Managing Committee: Jerome Sperling - Yale University - 1941-",
            "access_date": "2026-10-25",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "American School institutional history",
            "rights_notes": "The institutional listing establishes a Yale association from 1941; teaching employment is corroborated separately.",
        },
        {
            "key": ASCSA_REPORT,
            "stable_url": "https://www.ascsa.edu.gr/archives/uploads/ASCSA_AR_61_1941-42.pdf",
            "title": "Annual Report of the American School of Classical Studies at Athens, 1941-1942",
            "author_creator": "American School of Classical Studies at Athens",
            "repository_publisher": "American School of Classical Studies at Athens",
            "publication_record_date": "1942",
            "locator": "Managing Committee 1941-1942: Jerome Sperling, Yale University, New Haven, Connecticut",
            "access_date": "2026-10-25",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "American School annual reports",
            "rights_notes": "The report establishes the contemporary Yale affiliation but does not state the exact Yale job title.",
        },
        {
            "key": SPERLING_OBIT,
            "stable_url": "https://www.legacy.com/us/obituaries/nytimes/name/peter-sperling-obituary?id=23644738",
            "title": "Peter Ridley Sperling obituary",
            "repository_publisher": "The New York Times via Legacy.com",
            "publication_record_date": "2014-01",
            "locator": "Family-background paragraph describing Jerome Sperling beginning to teach at Yale after moving to New Haven",
            "access_date": "2026-10-25",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "rights_notes": "Used as corroboration for the father's Yale teaching, not as the principal identity source. No living-relative details are retained.",
        },
        {
            "key": OSS_GREEK_DESK,
            "stable_url": "https://www.elia.org.gr/userfiles/pdf_archieve/1944%2010-2344%20OSS%2C%20Theofanides%2C%20Merchant%20Seamen%2C%20King%2C%20%5B7%20pgs%5D%20226-210-WN10850%20%28Admin%29.pdf",
            "archival_identifier": "226-210-WN10850 (Admin)",
            "title": "South Eastern European Section SA/B - SI: Review of Period December 1941 - March 1943",
            "author_creator": "D. G. Stampados",
            "repository_publisher": "ELIA-MIET digital archive; declassified Office of Strategic Services record",
            "publication_record_date": "1944-10-23",
            "locator": "PDF page 4: Rodney Young recruited Jerome Sperling among past assistants in late April 1942; PDF page 7: Captain Jerry Sperling assignment",
            "access_date": "2026-10-25",
            "source_quality": "A_direct_official",
            "collection_name": "Declassified OSS records relating to Greece",
            "rights_notes": "The declassified memorandum establishes the rare-name OSS identity and recruitment chronology; OCR was checked against page context.",
        },
        {
            "key": MET_SPERLING,
            "stable_url": "https://www.metmuseum.org/perspectives/kleinberger-galleries",
            "title": "The Kleinberger Galleries: A History in Photographs",
            "repository_publisher": "The Metropolitan Museum of Art",
            "locator": "Paragraph describing Harry G. Sperling leading F. Kleinberger Galleries from 1933 and serving with OSS during World War II",
            "access_date": "2026-10-25",
            "source_quality": "B_authoritative_institutional",
            "rights_notes": "Discovery and candidate evidence only. Two separate index rows share this name, and neither is linked to the biography by the source.",
        },
        {
            "key": WKU_DOUGLAS,
            "stable_url": "https://people.wku.edu/sally.kuhlenschmidt/whimsy/oss/oss.htm",
            "title": "OSS Assessment Staff",
            "author_creator": "Sally Kuhlenschmidt",
            "repository_publisher": "Western Kentucky University",
            "locator": "List of psychologists associated with OSS selection assessment, including Douglas Spencer",
            "access_date": "2026-10-25",
            "source_quality": "D_correlative_or_secondary",
            "rights_notes": "Candidate evidence only. The index row lacks an initial, rank or protected-identifier bridge, so the name match is not published as identity fact.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": "yale-b901",
            "organization_id": "918dedde-f9d1-5db1-8304-5c218a06b9b5",
            "canonical_name": "Yale University",
            "historical_name": "Yale University",
            "aliases": ["Yale"],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "New Haven",
            "state_or_region": "Connecticut",
            "country": "United States",
            "normalization_notes": "Faculty employment and student attendance are modeled separately.",
        },
        {
            "key": "speraber-medical-practice-b901",
            "canonical_name": "Self-employed medical practice",
            "historical_name": "cabinet médical",
            "aliases": ["private medical practice", "general practice"],
            "organization_type": "self-employment",
            "sector": "self_employed",
            "city": "Saint-Jean-de-Luz",
            "state_or_region": "Pyrénées-Atlantiques",
            "country": "France",
            "active_dates": "documented 1919-1943 and after the war",
            "normalization_notes": "No clinic, partnership or institutional employer is inferred; the sources describe Speraber's own general medical practice.",
        },
        {
            "key": "french-army-health-service-b901",
            "canonical_name": "French Army Health Service",
            "historical_name": "service de santé",
            "aliases": ["Service de santé des armées"],
            "organization_type": "military medical service",
            "sector": "military",
            "country": "France",
            "normalization_notes": "The historical French service label is preserved; no hospital is treated as a separate employer without a specific employment source.",
        },
    ]


def army_affiliation(item: dict[str, object]) -> dict[str, object]:
    person_id, _name = PEOPLE[int(item["row"])]
    relationship = str(item["relationship_type"])
    return {
        "key": f"{item['slug']}-occupation-b901",
        "person_id": person_id,
        "relationship_type": relationship,
        "occupation": "Student; institution not recorded" if relationship == "student" else item["occupation"],
        "end_date": item["date"],
        "date_precision": f"Historical civilian-occupation code {item['code']} was recorded at Army entry on {item['date']}; no employer or OSS-transfer date is named.",
        "country": "United States",
        "immediate_pre_oss": False,
        "last_civilian_pre_service": False,
        "pre_oss_temporal_basis": "strongly_date_bounded",
        "identity_confidence": "high_confidence",
        "claim_confidence": "medium",
        "source_quality": "A_direct_official",
        "publication_status": "publish_qualified",
        "research_notes": "The historical category is not converted into a named employer, institution, workplace or exact title.",
    }


def substantive_affiliations() -> list[dict[str, object]]:
    return [
        {
            "key": "edmond-speraber-medical-practice-b901",
            "person_id": PEOPLE[40][0],
            "organization_key": "speraber-medical-practice-b901",
            "organization_name_as_found": "cabinet médical à Saint-Jean-de-Luz",
            "role_title": "general practitioner",
            "occupation": "physician",
            "relationship_type": "self_employment",
            "start_date": "1940-08-21",
            "end_date": None,
            "date_precision": "The sources date his demobilization to 21 August 1940 and state that he resumed general medical practice; they do not give a practice end date.",
            "city": "Saint-Jean-de-Luz",
            "state_or_region": "Pyrénées-Atlantiques",
            "country": "France",
            "immediate_pre_oss": True,
            "last_civilian_pre_service": True,
            "pre_oss_temporal_basis": "probable_immediate",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "published",
            "research_notes": "Two independently authored historical accounts place Speraber back in his own medical practice after demobilization and before his January 1943 NANA responsibility. Neither states that the practice ended at recruitment.",
        },
        {
            "key": "edmond-speraber-french-army-b901",
            "person_id": PEOPLE[40][0],
            "organization_key": "french-army-health-service-b901",
            "organization_name_as_found": "service de santé",
            "role_title": "capitaine médecin",
            "occupation": "military physician",
            "relationship_type": "military_assignment",
            "start_date": "1939-09-01",
            "end_date": "1940-08-21",
            "date_precision": "The historical biography supplies day-specific mobilization and demobilization dates; the official SHD register independently supplies rank and service branch.",
            "country": "France",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "A_direct_official",
            "publication_status": "published",
            "research_notes": "This documented wartime military assignment ended before the resumed civilian practice and is not mislabeled as an employer.",
        },
        {
            "key": "jerome-sperling-yale-b901",
            "person_id": PEOPLE[46][0],
            "organization_key": "yale-b901",
            "organization_name_as_found": "Yale University",
            "role_title": "teacher",
            "occupation": "archaeologist and classics scholar",
            "relationship_type": "employment",
            "start_date": "1941",
            "end_date": "1942-04",
            "date_precision": "ASCSA lists his Yale affiliation from 1941; a family obituary says he began teaching there; an official OSS memorandum dates his recruitment to late April 1942. No exact Yale separation date or department is stated.",
            "city": "New Haven",
            "state_or_region": "Connecticut",
            "country": "United States",
            "immediate_pre_oss": True,
            "last_civilian_pre_service": True,
            "pre_oss_temporal_basis": "probable_immediate",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "published",
            "research_notes": "Yale is the best-supported last civilian employer and probable immediate pre-OSS affiliation. The exact teaching title and transfer date remain unverified.",
        },
    ]


def army_identity_claim(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    person_id, name = PEOPLE[row]
    suffix_note = " The Army source additionally records the suffix Jr." if row == 33 else ""
    return {
        "key": f"identity-{item['slug']}-b901",
        "person_id": person_id,
        "claim_type": "identity",
        "claim_text": f"The indexed {name} row is a high-confidence match to the reviewed official Army record.{suffix_note}",
        "evidence_paraphrase": "A nonshared protected identifier connects the visually verified index row to the official Army record.",
        "identity_match_assessment": "High confidence from name agreement and a nonshared protected-identifier bridge.",
        "temporal_assessment": "The Army-entry record supports identity and a dated occupation category; it does not establish the OSS transfer sequence.",
        "source_quality": "A_direct_official",
        "claim_confidence": "high",
        "publication_status": "published",
        "match_notes": "No protected identifier is exposed, and no employer or workplace is inferred from the coded Army field.",
        "sources": [
            {"source_key": INDEX, "locator_override": f"PDF page 440 row {row}; protected identifier withheld"},
            {"source_key": ARMY, "locator_override": "Accepted reviewed identity bridge; protected identifier withheld"},
        ],
    }


def army_occupation_claim(item: dict[str, object]) -> dict[str, object]:
    person_id, name = PEOPLE[int(item["row"])]
    if item["relationship_type"] == "student":
        text = f"At Army entry on {item['date']}, {name} was recorded in the historical student category; no institution or employer is identified."
    else:
        text = f"At Army entry on {item['date']}, {name} was recorded in the historical {str(item['occupation']).lower()} category; no employer is identified."
    return {
        "key": f"occupation-{item['slug']}-b901",
        "person_id": person_id,
        "affiliation_key": f"{item['slug']}-occupation-b901",
        "claim_type": "occupation",
        "claim_text": text,
        "evidence_paraphrase": f"The accepted Army record carries civilian-occupation code {item['code']}, decoded from NARA's official code list.",
        "identity_match_assessment": "The occupation belongs only to the reviewed protected-identifier match; the identifier itself is not public.",
        "temporal_assessment": "Strongly date-bounded to Army entry; it does not establish the immediate pre-OSS affiliation or a named employer.",
        "source_quality": "A_direct_official",
        "claim_confidence": "medium",
        "publication_status": "publish_qualified",
        "match_notes": "The historical category is a qualified lead, not an employer, workplace, institution or exact title.",
        "sources": [
            {"source_key": ARMY, "locator_override": f"Accepted reviewed identity record; civilian occupation code {item['code']}; protected identifier withheld"},
            {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46; Army-entry-date and civilian-occupation fields"},
            {"source_key": CODES, "locator_override": item["locator"], "excerpt_override": item["occupation"]},
        ],
    }


def substantive_claims() -> list[dict[str, object]]:
    return [
        {
            "key": "identity-deforest-spencer-b901",
            "person_id": PEOPLE[26][0],
            "claim_type": "identity",
            "claim_text": "The two separately printed Deforest Spencer rows on page 440 are linked to one high-confidence person entity while both source rows remain preserved.",
            "evidence_paraphrase": "The adjacent rows use the same exact name and one protected identifier but point to Boxes 731 and 732.",
            "identity_match_assessment": "High confidence for one person represented by two immutable rows because the protected identifier is identical; no employer evidence is transferred.",
            "temporal_assessment": "The index supports duplicate resolution only and supplies no pre-OSS chronology.",
            "source_quality": "A_direct_official",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "Both source records remain visible. Review both boxes before treating either file as complete.",
            "sources": [{"source_key": INDEX, "locator_override": "PDF page 440 rows 26-27; protected identifier withheld"}],
        },
        {
            "key": "candidate-douglas-spencer-assessor-b901",
            "person_id": PEOPLE[29][0],
            "claim_type": "identity",
            "claim_text": "A secondary university-hosted list names an OSS selection assessor called Douglas Spencer, but the index row is not securely linked to him.",
            "evidence_paraphrase": "The candidate source supplies the same name and OSS context but no middle initial, rank, protected identifier or personnel-file pointer.",
            "identity_match_assessment": "Low-confidence candidate; a name match alone is insufficient for this common name.",
            "temporal_assessment": "No pre-OSS employer or dated predecessor role is established.",
            "source_quality": "D_correlative_or_secondary",
            "claim_confidence": "low",
            "publication_status": "withheld_low_confidence",
            "match_notes": "Keep the candidate in private review until Box 732 supplies at least two corroborating identifiers beyond the name.",
            "sources": [{"source_key": WKU_DOUGLAS}],
        },
        {
            "key": "candidate-harry-g-sperling-row44-b901",
            "person_id": PEOPLE[44][0],
            "claim_type": "identity",
            "claim_text": "The Metropolitan Museum documents an OSS veteran and art dealer named Harry G. Sperling, but the first of two index rows is not securely linked to him.",
            "evidence_paraphrase": "The institutional article supplies exact name, gallery leadership and OSS service but no index-row identifier.",
            "identity_match_assessment": "Low-confidence candidate because two separately printed index rows share the exact name and carry different protected identifiers.",
            "temporal_assessment": "F. Kleinberger Galleries is a possible pre-OSS employer only for the external biography, not yet for this index row.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "low",
            "publication_status": "withheld_low_confidence",
            "match_notes": "Do not publish the gallery employment for either row until the personnel files identify which, if either, is the museum's Harry G. Sperling.",
            "sources": [{"source_key": MET_SPERLING}],
        },
        {
            "key": "conflict-harry-g-sperling-row45-b901",
            "person_id": PEOPLE[45][0],
            "claim_type": "identity",
            "claim_text": "The second Harry G Sperling row has a protected-identifier bridge to an Army record whose source name is damaged; its art occupation is not transferred as fact.",
            "evidence_paraphrase": "The private identifier agrees uniquely, but the Army name does not agree with the index and two printed Harry G Sperling rows remain separate.",
            "identity_match_assessment": "Conflicting. The source damage and duplicate exact name require personnel-file review before accepting the Army occupation or external gallery biography.",
            "temporal_assessment": "The Army entry is dated 1942 but cannot safely establish the indexed person's occupation while identity remains conflicting.",
            "source_quality": "A_direct_official",
            "claim_confidence": "conflicting",
            "publication_status": "conflicting",
            "match_notes": "Full protected identifiers remain private. Review both Box 732 files together.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 440 rows 44-45; protected identifiers withheld"},
                {"source_key": ARMY, "support_type": "context_only", "locator_override": "Damaged-name identity candidate; protected identifier withheld"},
                {"source_key": CODES, "support_type": "context_only", "locator_override": "PDF physical page 170; category 004"},
            ],
        },
        {
            "key": "candidate-harry-g-sperling-row45-gallery-b901",
            "person_id": PEOPLE[45][0],
            "claim_type": "identity",
            "claim_text": "The Metropolitan Museum's Harry G. Sperling biography is a plausible lead for the second index row but remains unassigned.",
            "evidence_paraphrase": "The museum article links the exact name to F. Kleinberger Galleries and OSS service, but not to either index identifier.",
            "identity_match_assessment": "Low confidence; the conflicting Army form does not supply a safe bridge to the art dealer.",
            "temporal_assessment": "The gallery chronology cannot be transferred to this row while identity is unresolved.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "low",
            "publication_status": "withheld_low_confidence",
            "match_notes": "Keep private until direct file evidence resolves the same-name rows.",
            "sources": [{"source_key": MET_SPERLING}],
        },
        {
            "key": "identity-edmond-speraber-b901",
            "person_id": PEOPLE[40][0],
            "claim_type": "identity",
            "claim_text": "The indexed Captain Edmond Speraber is a high-confidence match to French medical officer and resistance-network leader Edmond Charles Speraber.",
            "evidence_paraphrase": "The rare exact surname and given name, captain rank, medical-service record and individual network-agent file converge on one person.",
            "identity_match_assessment": "High confidence from a distinctive name, matching officer rank and two complementary official French archival pointers, corroborated by independent historical accounts.",
            "temporal_assessment": "The official register dates removal from the officer rolls to August 1940; historical accounts then trace civilian practice and network work.",
            "source_quality": "A_direct_official",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "The identity is not based on name alone; the French rank and branch match the indexed captain designation.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 440 row 40; Box 732"},
                {"source_key": SHD_OFFICERS, "locator_override": "GR 8 YE 487"},
                {"source_key": SHD_NETWORKS, "locator_override": "GR 28 P 4 253 / 141"},
                {"source_key": BPSGM_BIO, "support_type": "context_only"},
            ],
        },
        {
            "key": "military-edmond-speraber-b901",
            "person_id": PEOPLE[40][0],
            "affiliation_key": "edmond-speraber-french-army-b901",
            "claim_type": "other_pre_oss_affiliation",
            "claim_text": "Edmond Speraber served as a French Army medical captain from mobilization in September 1939 until demobilization in August 1940.",
            "evidence_paraphrase": "The official SHD register records capitaine médecin in the health service; the historical biography supplies the mobilization chronology and medical postings.",
            "identity_match_assessment": "High-confidence identity from the rare name and matching captain/medical-service details.",
            "temporal_assessment": "Explicitly date-bounded before his return to civilian practice and later resistance-network responsibility.",
            "source_quality": "A_direct_official",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "This is a military assignment, not a civilian employer.",
            "sources": [
                {"source_key": SHD_OFFICERS, "locator_override": "GR 8 YE 487"},
                {"source_key": BPSGM_BIO, "locator_override": "Mobilization, medical postings and 21 August 1940 demobilization"},
                {"source_key": BPSGM_MASTER, "support_type": "context_only"},
            ],
        },
        {
            "key": "last-civilian-edmond-speraber-b901",
            "person_id": PEOPLE[40][0],
            "affiliation_key": "edmond-speraber-medical-practice-b901",
            "claim_type": "last_civilian_pre_service",
            "claim_text": "Edmond Speraber's own medical practice in Saint-Jean-de-Luz is his best-supported last civilian employment before his January 1943 NANA network responsibility.",
            "evidence_paraphrase": "Two historical accounts state that he resumed general medical practice after August 1940 demobilization and before assuming NANA responsibility in January 1943.",
            "identity_match_assessment": "High-confidence identity from the rare name, French officer file and matching medical biography.",
            "temporal_assessment": "Strongly date-bounded as the last documented civilian work; the sources do not state that he ceased practice on joining the network.",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "The relationship is self-employment. No hospital, clinic or later organization is invented as employer.",
            "sources": [
                {"source_key": BPSGM_BIO, "locator_override": "Return to Saint-Jean-de-Luz medical activities after 21 August 1940 demobilization"},
                {"source_key": BPSGM_MASTER, "locator_override": "General practice after August 1940 demobilization"},
            ],
        },
        {
            "key": "immediate-edmond-speraber-b901",
            "person_id": PEOPLE[40][0],
            "affiliation_key": "edmond-speraber-medical-practice-b901",
            "claim_type": "immediate_pre_oss_affiliation",
            "claim_text": "Speraber's Saint-Jean-de-Luz medical practice is his probable immediate pre-NANA affiliation; the accessible sources do not state a formal separation from practice.",
            "evidence_paraphrase": "The chronology runs from resumed medical practice through assistance to escape networks and then January 1943 responsibility for the Franco-American NANA network.",
            "identity_match_assessment": "High-confidence identity from official French files and matching biographical details.",
            "temporal_assessment": "Probable immediate rather than explicit immediate because the sources do not say he left the practice to join NANA.",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "claim_confidence": "medium",
            "publication_status": "publish_qualified",
            "match_notes": "The qualified wording must remain visible and NANA must not be treated as an ordinary civilian employer.",
            "sources": [
                {"source_key": BPSGM_BIO, "locator_override": "Medical practice, escape-network assistance and January 1943 NANA responsibility"},
                {"source_key": BPSGM_MASTER, "support_type": "context_only"},
            ],
        },
        {
            "key": "networks-edmond-speraber-b901",
            "person_id": PEOPLE[40][0],
            "claim_type": "other_pre_oss_affiliation",
            "claim_text": "Before taking responsibility for NANA in January 1943, Speraber used his medical role to assist injured or ill people moving through the Comète, Margot and Nivelle escape networks.",
            "evidence_paraphrase": "The biography dates this assistance through January 1943 and distinguishes it from his subsequent NANA responsibility.",
            "identity_match_assessment": "High-confidence identity from the rare name and official French military and network-file references.",
            "temporal_assessment": "Explicitly before the January 1943 NANA role, but not modeled as paid employment.",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "This is a documented resistance affiliation, not an employer claim.",
            "sources": [
                {"source_key": BPSGM_BIO, "locator_override": "Assistance to Comète, Margot and Nivelle escape networks through January 1943"},
                {"source_key": SHD_NETWORKS, "support_type": "context_only", "locator_override": "Individual network-agent dossier GR 28 P 4 253 / 141"},
            ],
        },
        {
            "key": "identity-jerome-sperling-b901",
            "person_id": PEOPLE[46][0],
            "claim_type": "identity",
            "claim_text": "The indexed Lieutenant Colonel Jerome Sperling is a high-confidence match to archaeologist and OSS Greek Desk officer Jerome W. Sperling.",
            "evidence_paraphrase": "A declassified OSS memorandum names Jerome Sperling among archaeologist Rodney Young's recruited assistants and records his Army officer progression and overseas assignment.",
            "identity_match_assessment": "High confidence from the distinctive exact name, commissioned Army rank, specific OSS Greek Desk chronology and matching academic network.",
            "temporal_assessment": "The official memorandum dates recruitment to late April 1942 and later wartime assignments.",
            "source_quality": "A_direct_official",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "The indexed rank is compatible with later promotion; the claim does not rely on a famous-name match alone.",
            "sources": [
                {"source_key": INDEX, "locator_override": "PDF page 440 row 46; Box 732"},
                {"source_key": OSS_GREEK_DESK, "locator_override": "PDF pages 4 and 7; recruitment and assignment chronology"},
                {"source_key": ASCSA_REPORT, "support_type": "context_only"},
            ],
        },
        {
            "key": "last-civilian-jerome-sperling-yale-b901",
            "person_id": PEOPLE[46][0],
            "affiliation_key": "jerome-sperling-yale-b901",
            "claim_type": "last_civilian_pre_service",
            "claim_text": "Yale University is Jerome Sperling's best-supported last civilian employer before his April 1942 recruitment to the OSS Greek Desk.",
            "evidence_paraphrase": "ASCSA contemporaneously lists Sperling with Yale from 1941, a family obituary states that he taught there, and an official OSS memorandum dates recruitment to late April 1942.",
            "identity_match_assessment": "High-confidence identity from the distinctive name, academic network and official OSS officer chronology.",
            "temporal_assessment": "Strongly date-bounded as the last documented civilian employment; no exact Yale separation date is stated.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "high",
            "publication_status": "published",
            "match_notes": "The role is conservatively labeled teacher because the reviewed sources do not name a formal Yale title or department.",
            "sources": [
                {"source_key": ASCSA_HISTORY, "locator_override": "Appendix VI: Jerome Sperling - Yale University - 1941-"},
                {"source_key": ASCSA_REPORT, "locator_override": "Managing Committee 1941-1942"},
                {"source_key": SPERLING_OBIT, "locator_override": "Family-background paragraph; teaching at Yale"},
                {"source_key": OSS_GREEK_DESK, "support_type": "context_only", "locator_override": "Late April 1942 recruitment chronology"},
            ],
        },
        {
            "key": "immediate-jerome-sperling-yale-b901",
            "person_id": PEOPLE[46][0],
            "affiliation_key": "jerome-sperling-yale-b901",
            "claim_type": "immediate_pre_oss_affiliation",
            "claim_text": "Yale is Jerome Sperling's probable immediate pre-OSS affiliation, but no reviewed source explicitly says that he left Yale directly for the Greek Desk.",
            "evidence_paraphrase": "The institutional chronology places him at Yale from 1941 and the official OSS chronology records recruitment in late April 1942.",
            "identity_match_assessment": "High-confidence identity from the rare name, academic network and official OSS officer role.",
            "temporal_assessment": "Probable immediate: the dates closely adjoin, but an explicit transfer phrase or separation date is absent.",
            "source_quality": "B_authoritative_institutional",
            "claim_confidence": "medium",
            "publication_status": "publish_qualified",
            "match_notes": "The public profile must preserve the qualified wording and distinguish this from the stronger last-civilian-employer conclusion.",
            "sources": [
                {"source_key": ASCSA_HISTORY, "locator_override": "Appendix VI: Yale affiliation from 1941"},
                {"source_key": OSS_GREEK_DESK, "locator_override": "Late April 1942 recruitment chronology"},
            ],
        },
    ]


def archive_update(row: int, reason: str) -> dict[str, object]:
    person_id, name = PEOPLE[row]
    return {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, Box 732 and archive location, but the staged official-context, CIA Reading Room, exact-name, occupation, employer, obituary, institutional, directory, newspaper and archival protocol found no defensible identity bridge. {reason}",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": "Review the indexed Box 732 personnel file for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "critical",
    }


def person_updates() -> list[dict[str, object]]:
    updates = [archive_update(row, reason) for row, reason in UNRESOLVED.items()]
    updates.append(
        {
            "person_id": PEOPLE[26][0],
            "identity_status": "high_confidence",
            "identity_evidence": "Two adjacent immutable source rows carry the exact same name and protected identifier while pointing to Boxes 731 and 732. They remain linked to one high-confidence entity without deleting either row.",
            "manual_review_required": True,
            "research_status": "requires_archival_review",
            "next_action": "Review the linked Deforest Spencer files in Boxes 731 and 732 together for identity corroboration and the last documented pre-OSS affiliation.",
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
            "archival_review_priority": "critical",
        }
    )
    for item in ARMY_OCCUPATIONS:
        person_id, _name = PEOPLE[int(item["row"])]
        update: dict[str, object] = {
            "person_id": person_id,
            "identity_status": "high_confidence",
            "identity_evidence": "A nonshared protected identifier connects the visually verified index row to the reviewed official Army record. The occupation field remains separate from employer and immediate-affiliation claims.",
            "personnel_category": "enlisted_army_personnel",
            "commissioned_officer": False,
            "allied_or_foreign_personnel": False,
            "manual_review_required": True,
            "research_status": "occupation_only_found",
            "next_action": "Review the indexed Box 732 personnel file to identify the immediate pre-OSS affiliation and last civilian employer; do not convert the Army category into a named employer or institution.",
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
            "archival_review_priority": "high",
        }
        if int(item["row"]) == 33:
            update["name_variants"] = ["Frank C Spencer Jr", "Frank C. Spencer Jr."]
        updates.append(update)
    updates.extend(
        [
            {
                "person_id": PEOPLE[29][0],
                "identity_status": "ambiguous",
                "identity_evidence": "A university-hosted secondary list supplies an OSS assessor candidate named Douglas Spencer, but the index row lacks the additional identifiers required for a common-name match.",
                "manual_review_required": True,
                "research_status": "needs_identity_review",
                "next_action": "Review Box 732 for psychology, assessment-staff, education, hometown or wartime-assignment identifiers before assigning the external biography.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[40][0],
                "identity_status": "high_confidence",
                "identity_evidence": "The rare exact name, captain rank, official French medical-service file and individual network-agent file converge with two independently authored historical accounts.",
                "name_variants": ["Edmond Charles Speraber", "Dr Edmond Speraber"],
                "personnel_category": "foreign_or_allied_military_personnel",
                "commissioned_officer": True,
                "allied_or_foreign_personnel": True,
                "manual_review_required": True,
                "research_status": "verified_employer_found",
                "next_action": "Review Box 732 and SHD files GR 8 YE 487, GR 28 P 4 253 / 141 and GR 16 P 555475 to confirm the precise OSS/NANA administrative relationship and whether medical practice continued concurrently.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[44][0],
                "identity_status": "ambiguous",
                "identity_evidence": "The exact name matches a documented OSS veteran and art dealer, but two separately printed index rows share this name and carry different protected identifiers.",
                "manual_review_required": True,
                "possible_duplicate_group": "same-name:harry-g-sperling-page440",
                "research_status": "needs_identity_review",
                "next_action": "Review both Harry G Sperling files in Box 732 for art-dealer, F. Kleinberger Galleries, New York, education or birth identifiers before assigning the biography.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[45][0],
                "identity_status": "conflicting",
                "identity_evidence": "A nonshared protected identifier points to a dated Army record, but the Army source name is damaged and does not agree with the index. A second index row carries the same exact name and a different identifier.",
                "manual_review_required": True,
                "possible_duplicate_group": "same-name:harry-g-sperling-page440",
                "research_status": "conflicting_sources",
                "next_action": "Review both Harry G Sperling files in Box 732 before accepting the Army art-occupation code or the F. Kleinberger Galleries biography for either row.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[46][0],
                "identity_status": "high_confidence",
                "identity_evidence": "The distinctive exact name, commissioned Army rank, Yale/ASCSA academic network and declassified OSS Greek Desk memorandum establish a high-confidence identity.",
                "name_variants": ["Jerome W. Sperling", "Jerome W Sperling", "Jerry Sperling"],
                "personnel_category": "commissioned_army_officer",
                "commissioned_officer": True,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "verified_employer_found",
                "next_action": "Review Box 732 and the Jerome W. Sperling papers to confirm his exact Yale title, separation date and whether another affiliation intervened before late-April 1942 recruitment.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
        ]
    )
    return updates


def research_attempts() -> list[dict[str, object]]:
    attempts: list[dict[str, object]] = []
    evidence_rows = {26, 29, 33, 34, 37, 40, 42, 44, 45, 46}
    for row, (person_id, name) in PEOPLE.items():
        boxes = "Boxes 731 and 732" if row == 26 else "Box 732"
        if row in UNRESOLVED:
            note = UNRESOLVED[row]
            sources_reviewed = 5
            rejected = 6
        elif row == 26:
            note = "The two immutable rows are already linked through their exact name and shared protected identifier; both boxes still require review for employer evidence."
            sources_reviewed = 5
            rejected = 4
        elif row in {33, 34, 37, 42}:
            note = "The accepted protected-identifier bridge supports identity and a dated historical occupation or student category, but not a named employer or immediate OSS chronology."
            sources_reviewed = 7
            rejected = 5
        elif row == 29:
            note = "A psychologist/OSS-assessor candidate was retained privately, but the common-name index row lacks two corroborating identifiers."
            sources_reviewed = 6
            rejected = 7
        elif row == 40:
            note = "Official French officer and network finding aids plus two independent historical accounts establish high-confidence identity, a 1939-1940 medical military assignment and the resumed private practice before NANA."
            sources_reviewed = 9
            rejected = 4
        elif row in {44, 45}:
            note = "The two same-name rows remain separate. The Metropolitan Museum biography is withheld from both, and the damaged-name Army lead for the second row remains conflicting."
            sources_reviewed = 7
            rejected = 8
        elif row == 46:
            note = "A declassified OSS memorandum establishes the rare-name officer identity and April 1942 recruitment, while ASCSA and an obituary establish Yale teaching from 1941."
            sources_reviewed = 9
            rejected = 4
        else:
            raise AssertionError(row)
        has_evidence = row in evidence_rows
        slug = name.lower().replace(" ", "-").replace("'", "") + f"-r{row}"
        attempts.append(
            {
                "key": f"page440-row{row}-{slug}-b901",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA/index context; CIA Reading Room exact-name check; OSS and rank variants; employer and occupation; obituary, institutional, newspaper, directory and archival searches; {boxes}; protected-identifier Army crosswalk where available",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_901",
                "started_at": "2026-10-25T13:50:00Z",
                "completed_at": "2026-10-25T14:57:00Z",
                "outcome": "source_reviewed" if has_evidence else "candidate_rejected",
                "sources_reviewed": sources_reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, chronologically irrelevant results, postwar-only leads and materially conflicting candidates were not assigned." if has_evidence else note,
                "research_notes": ("Reviewed evidence established a supported, provisional or explicitly conflicting outcome; public claims are limited to what the cited sources prove. " if has_evidence else "No reliable identity or pre-OSS employer was established after the staged search and namesake-rejection protocol. ") + note + " Search-result snippets were discovery aids only, no paywall or access control was bypassed, the CIA Reading Room and Library of Congress exact-name passes returned no relevant result, and no exposed NARA API credential was used.",
                "next_action": f"Review the indexed {boxes} personnel file{'s' if row == 26 else ''}.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b901-v1",
            }
        )
    return attempts


def main() -> None:
    affiliations = [army_affiliation(item) for item in ARMY_OCCUPATIONS]
    affiliations.extend(substantive_affiliations())
    claims = [army_identity_claim(item) for item in ARMY_OCCUPATIONS]
    claims.extend(army_occupation_claim(item) for item in ARMY_OCCUPATIONS)
    claims.extend(substantive_claims())
    bundle = {
        "bundle_version": "batch-901-v1",
        "reviewer": "Before OSS Batch 901 evidence review",
        "sources": sources(),
        "organizations": organizations(),
        "affiliations": affiliations,
        "claims": claims,
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }
    OUTPUT.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
