from __future__ import annotations

# Rebuilds the reviewed Batch 1013 evidence bundle deterministically.
import json
from pathlib import Path


OUT = Path("research/evidence-page503-wiener-to-wiley-review_batch-1013_2026-11-04.json")
ACCESS_DATE = "2026-11-04"
STARTED_AT = "2026-11-04T06:45:00Z"
COMPLETED_AT = "2026-11-04T08:45:00Z"
AGENT_VERSION = "before-oss-b1013-v1"


PEOPLE = [
    (1, "1a09c318-edad-5b53-b5a6-e752c38e2891", "Thomas Wiener", "835"),
    (2, "42b65160-afad-5cdd-84f2-b59d748ea19e", "Walter F Wiener", "835"),
    (3, "1bd72a34-651e-5fad-ad01-ca4386dde398", "August I Wieners", "835"),
    (4, "09b95d6e-af48-51ae-875a-56dd51e66193", "Harold J Wiens", "835"),
    (5, "dcd81c36-9104-5983-89da-2e692bf44d6e", "Henry W Wieringa", "835"),
    (6, "7c7a5efb-1a6f-5647-b23e-484c136a8b49", "Leona E.D. Wierum", "836"),
    (7, "5237f1ae-be94-5279-a828-2ae3fe9cd318", "Walter Wierzbicki", "836"),
    (8, "37d1722d-9e45-5228-94c9-daa472b73c3c", "Heinrich A Wieschhoff", "836"),
    (9, "1c37314d-af73-5479-9c7a-c98b444755af", "Melvin C Wiese", "836"),
    (10, "44b988a2-d0f0-5852-afd2-769b954552b7", "Clifford C Wiesen", "836"),
    (11, "286b1d59-b9db-5a12-bdf1-b48165c2a72e", "Louis A Wiesner", "836"),
    (12, "31b9257c-f13a-50b9-ade0-ad0b1fb9e1c7", "Donald F Wiggin", "836"),
    (13, "1e334e6c-7cbe-5080-b0df-bdb164600264", "Charles W Wiggins", "836"),
    (14, "08407581-67ef-52e0-ac7e-ae51d0d5a413", "Robert S Wiggins", "836"),
    (15, "cb1a78c4-c52e-58b6-a68b-5f408babb4a7", "Frederick Wight", "836"),
    (16, "8c0cad5e-0fa5-520b-bcb1-4e7d01bb12c5", "Louis D Wight", "836"),
    (17, "70d09633-c395-59db-b065-1d4f0f851ceb", "Russell B Wight", "836"),
    (18, "de221dc5-a780-5b56-8085-99abedcaca82", "Royce Wightman", "836"),
    (19, "171a26db-42c9-565e-819d-94fba7d81005", "John C Wigington", "836"),
    (20, "1394fbf4-a578-5c51-89d9-e3474d330405", "Robert J Wigner", "836"),
    (21, "9e78c8e0-04a5-5ba0-a839-9c8c08de5f11", "Constantine A Wihtol", "836"),
    (22, "544bb2dd-2960-5f20-9e14-455e9713bd4c", "Orvin I Wikoff", "836"),
    (23, "046d53ed-9633-58a8-8339-1ef920bd1cbb", "John W Wikstrand", "836"),
    (24, "b858c2fe-60c2-5143-bdc1-39ff82d92713", "John A Wilbert", "836"),
    (25, "988b1615-a74b-5020-a82d-cbd8831f21c9", "C. Martin Wilbur", "836"),
    (26, "6626039a-00cd-5019-83cf-ba7c2ee78786", "Lawrence L Wilbur Jr.", "836"),
    (27, "d0880868-5f3e-5e66-a151-2fef9dca3593", "Richard H Wilbur", "836"),
    (28, "d2a8e5cd-25e8-5f56-bc24-c332632a27b8", "George E Wilcox", "836"),
    (29, "906dfc12-2033-5a55-b215-e918d4cb0e78", "James A Wilcox", "836"),
    (30, "d9373462-a1d3-5787-be85-0fd7a890afbd", "James W Wilcox", "836"),
    (31, "f3e1ac0e-38c2-5f41-a736-7996f9422758", "Oliver W Wilcox", "836"),
    (32, "b8b02544-5345-50b5-92d6-bce85aab0f07", "Ray Wilcox", "836"),
    (33, "37950eb8-f987-562e-a9d1-672fdeb154f4", "Stanley Wilcox", "836"),
    (34, "70b7d720-3821-57d3-9d87-f778baf05acf", "Isabelle S Wild", "836"),
    (35, "8c157b72-9357-54b7-869b-aa3f78b904ea", "Mount G Wild", "836"),
    (36, "c6f89842-e6f6-5b1e-9a41-f59914ea2365", "Norman Wild", "836"),
    (37, "706f91cf-7f26-5755-b2f1-19699edc7731", "Payson S Wild", "836"),
    (38, "a5d67311-8176-505a-808c-c425cddb5f2b", "John H Wilde", "836"),
    (39, "926d4a3d-7c3a-5eb7-a2dc-5d383388e2c9", "Charles Wilder", "836"),
    (40, "c516cb4c-9706-55a7-b726-784cde9e56f0", "Forrest G Wilder Jr.", "836"),
    (41, "339e3d2e-1514-555e-9f3b-f937783aafa0", "Gordon J Wilder", "836"),
    (42, "8bcc4be4-f8a8-5ff9-a612-bf0e5d1b78a8", "Edith M Wildrick", "836"),
    (43, "25d8d021-07c1-5a1c-b394-d9aa5a953c7d", "Charles R Wilds", "836"),
    (44, "cfee7651-162f-5c02-9354-88a8166a24d2", "Arthur J Wildt", "836"),
    (45, "df4f63f5-d123-543f-9741-d0de4e97b9a9", "E. David Wiley", "836"),
    (46, "e787fa88-e6c7-53f2-83db-2d509a343a58", "John C Wiley", "836"),
]


ARMY = {
    "44b988a2-d0f0-5852-afd2-769b954552b7": ("103", "checker", "1943-07-26", "confirmed"),
    "70d09633-c395-59db-b065-1d4f0f851ceb": ("031", "secondary-school teacher or principal", "1945-01-30", "confirmed"),
    "1394fbf4-a578-5c51-89d9-e3474d330405": ("137", "stenographer or typist", "1946-10-03", "confirmed"),
    "544bb2dd-2960-5f20-9e14-455e9713bd4c": ("781", "motor-vehicle mechanic or repairman", "1942-08-18", "high_confidence"),
    "6626039a-00cd-5019-83cf-ba7c2ee78786": ("002", "actor or actress", "1943-03-03", "confirmed"),
    "f3e1ac0e-38c2-5f41-a736-7996f9422758": ("878", "machine-shop or related occupation, not elsewhere classified", "1942-08-19", "confirmed"),
    "37950eb8-f987-562e-a9d1-672fdeb154f4": ("031", "secondary-school teacher or principal", "1943-04-09", "confirmed"),
    "a5d67311-8176-505a-808c-c425cddb5f2b": ("992", "student", "1942-09-14", "confirmed"),
    "c516cb4c-9706-55a7-b726-784cde9e56f0": ("402", "skilled worker in production of bakery products, not elsewhere classified", "1942-08-11", "confirmed"),
    "25d8d021-07c1-5a1c-b394-d9aa5a953c7d": ("992", "student", "1944-06-28", "confirmed"),
}


CONFLICTS = {
    "dcd81c36-9104-5983-89da-2e692bf44d6e": "The protected identifier printed for Henry W. Wieringa resolves in the official Army file to PULS KENNETH M, a materially different name.",
    "b858c2fe-60c2-5143-bdc1-39ff82d92713": "The protected identifier printed for John A. Wilbert resolves in the official Army file to INCHIERCHIERE PAUL, a materially different name.",
}


RICH = {
    "37d1722d-9e45-5228-94c9-daa472b73c3c",
    "286b1d59-b9db-5a12-bdf1-b48165c2a72e",
    "cb1a78c4-c52e-58b6-a68b-5f408babb4a7",
    "706f91cf-7f26-5755-b2f1-19699edc7731",
    "e787fa88-e6c7-53f2-83db-2d509a343a58",
    "988b1615-a74b-5020-a82d-cbd8831f21c9",
}


SPECIAL_REJECTIONS = {
    "d0880868-5f3e-5e66-a151-2fef9dca3593": "The famous poet Richard P. Wilbur has a different middle initial and was rejected as a namesake; no source bridges him to the indexed Richard H. Wilbur.",
    "8c157b72-9357-54b7-869b-aa3f78b904ea": "A contemporary marriage notice corroborates the name and lieutenant rank but supplies no employer, institution, OSS assignment, or second identity bridge.",
    "cfee7651-162f-5c02-9354-88a8166a24d2": "A bounded CIA adapter check was disallowed by site robots policy and a Library of Congress adapter check timed out; neither access failure is treated as a negative result.",
}


sources = [
    {
        "key": "nara-index-b1013",
        "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
        "archival_identifier": "RG 226, Entry A1-224, Boxes 835-836",
        "title": "OSS Personnel Files from Excel",
        "author_creator": "National Archives and Records Administration",
        "repository_publisher": "National Archives and Records Administration",
        "publication_record_date": "2010-12-23",
        "locator": "PDF page 503, rows 1-46; visually checked against a 180 dpi render",
        "access_date": ACCESS_DATE,
        "source_quality": "A_direct_official",
        "collection_name": "Records of the Office of Strategic Services, Record Group 226",
        "rights_notes": "All 46 printed rows remain separate. Original spelling is preserved; full service or officer identifiers remain private.",
    },
    {
        "key": "army-bulk-b1013",
        "stable_url": "https://catalog.archives.gov/id/1263923",
        "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
        "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
        "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
        "repository_publisher": "National Archives and Records Administration",
        "publication_record_date": "1938-1946; merged file created 2002",
        "locator": "Official unrestricted ASNEF.FIN.DAT; ten accepted and two conflicting protected-identifier comparisons; identifiers and raw rows withheld",
        "access_date": ACCESS_DATE,
        "source_quality": "A_direct_official",
        "collection_name": "World War II Army Enlistment Records",
        "document_number": "ASNEF.FIN.DAT",
        "rights_notes": "Army-entry categories are not named employers, institutions, or exact OSS-transfer records. Two identifier conflicts remain unresolved.",
    },
    {
        "key": "army-tech-b1013",
        "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf",
        "archival_identifier": "NN3-064-03-008; National Archives Identifier 1263923",
        "title": "World War II Army Enlistment Records: Reference Copy of Technical Documentation",
        "author_creator": "National Archives and Records Administration",
        "repository_publisher": "National Archives at College Park - Electronic Records",
        "publication_record_date": "1994-2005; reference copy modified 2011",
        "locator": "PDF physical pages 44-46; fixed-width identifier, name, entry-date, grade, and civilian-occupation fields",
        "access_date": ACCESS_DATE,
        "source_quality": "A_direct_official",
        "collection_name": "World War II Army Enlistment Records technical documentation",
    },
    {
        "key": "army-codes-b1013",
        "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1CL_SD.pdf",
        "archival_identifier": "National Archives Identifier 1263923; Code No. 30",
        "title": "NARA Compiled Code Lists for the Electronic Army Serial Number Merged File",
        "author_creator": "National Archives and Records Administration",
        "repository_publisher": "National Archives at College Park - Electronic Records",
        "publication_record_date": "2011-01-12; modified 2011-03-17",
        "locator": "PDF physical pages 171-177 and 304; relevant categories visually inspected",
        "access_date": ACCESS_DATE,
        "source_quality": "A_direct_official",
        "collection_name": "World War II Army Enlistment Records technical documentation",
        "rights_notes": "Historical categories are published with their limits and never converted into a named employer or institution.",
    },
    {
        "key": "fernuni-wieschhoff-b1013",
        "stable_url": "https://www.fernuni-hagen.de/geschichte/docs/9-geschichtswoche/stadtplan_hagen_koloniale_spuren_a2.pdf",
        "archival_identifier": "Hagen - Stadt der FernUniversität public-history map, location 15",
        "title": "Fern und exotisch vor der Haustür? Koloniale Spuren in Hagen",
        "author_creator": "Lehrgebiet Geschichte Europas in der Welt",
        "repository_publisher": "FernUniversität in Hagen",
        "publication_record_date": "2019",
        "locator": "PDF physical page 1, location 15, Heinrich Wieschhoff",
        "access_date": ACCESS_DATE,
        "source_quality": "B_authoritative_institutional",
        "rights_notes": "The institutional public-history source dates a University Museum curatorship to 1941 and OSS Africa work to 1942-1945.",
    },
    {
        "key": "penn-history-wieschhoff-b1013",
        "stable_url": "https://anthropology.sas.upenn.edu/sites/www.sas.upenn.edu.anthropology/files/page/A%20Short%20History%20of%20Anthropology%20at%20Penn.pdf",
        "archival_identifier": "Expedition magazine, A Short History of Anthropology at Penn",
        "title": "A Short History of Anthropology at Penn",
        "author_creator": "Igor Kopytoff",
        "repository_publisher": "University of Pennsylvania Museum of Archaeology and Anthropology",
        "publication_record_date": "2006",
        "locator": "PDF physical page 7; printed page 31; Heinrich Wieschhoff (1942-47)",
        "access_date": ACCESS_DATE,
        "source_quality": "B_authoritative_institutional",
    },
    {
        "key": "un-wieschhoff-b1013",
        "stable_url": "https://digitallibrary.un.org/nanna/record/3948429/files/Secretariat_News_-_29_Sep_1961.pdf?registerDownload=1&version=1&withMetadata=0&withWatermark=0",
        "archival_identifier": "United Nations Secretariat News, volume XV, edition 16",
        "title": "United Nations Secretariat News, 29 September 1961",
        "author_creator": "United Nations Secretariat",
        "repository_publisher": "United Nations Digital Library",
        "publication_record_date": "1961-09-29",
        "locator": "PDF physical page 9; tribute to Heinrich A. Wieschhoff",
        "access_date": ACCESS_DATE,
        "source_quality": "A_direct_official",
    },
    {
        "key": "uc-wight-b1013",
        "stable_url": "https://digicoll.lib.berkeley.edu/record/81149/files/inmemoriam1986.pdf",
        "archival_identifier": "University of California Academic Senate, In Memoriam 1986",
        "title": "Frederick S. Wight, Art: Los Angeles, 1902-1986",
        "author_creator": "University of California Academic Senate",
        "repository_publisher": "University of California",
        "publication_record_date": "1986",
        "locator": "PDF physical page 176; printed pages 322-323",
        "access_date": ACCESS_DATE,
        "source_quality": "B_authoritative_institutional",
    },
    {
        "key": "stern-wight-b1013",
        "stable_url": "https://www.louissternfinearts.com/artists/frederick-wight/biography",
        "archival_identifier": "Louis Stern Fine Arts artist biography",
        "title": "Frederick Wight: Biography",
        "author_creator": "Louis Stern Fine Arts",
        "repository_publisher": "Louis Stern Fine Arts",
        "locator": "Biography paragraphs 1-4; pre-Navy portrait work and Naval Division OSS chronology",
        "access_date": ACCESS_DATE,
        "source_quality": "C_reputable_contemporary_or_scholarly",
    },
    {
        "key": "afsa-wiesner-b1013",
        "stable_url": "https://afsa.org/sites/default/files/fsj-2002-12-december_0.pdf",
        "archival_identifier": "The Foreign Service Journal, December 2002",
        "title": "In Memory: Louis A. Wiesner",
        "author_creator": "American Foreign Service Association",
        "repository_publisher": "American Foreign Service Association",
        "publication_record_date": "2002-12",
        "locator": "PDF physical page 78; printed page 64",
        "access_date": ACCESS_DATE,
        "source_quality": "B_authoritative_institutional",
        "collection_name": "The Foreign Service Journal",
    },
    {
        "key": "crimson-payson-wild-b1013",
        "stable_url": "https://www.thecrimson.com/article/1943/3/22/faculty-defense-group-busy-with-war/",
        "archival_identifier": "The Harvard Crimson, 1943-03-22",
        "title": "Faculty Defense Group Busy with War Work",
        "repository_publisher": "The Harvard Crimson",
        "publication_record_date": "1943-03-22",
        "locator": "Paragraph headed by the Universities Committee on Post War International Problems",
        "access_date": ACCESS_DATE,
        "source_quality": "C_reputable_contemporary_or_scholarly",
        "rights_notes": "The contemporary report establishes Harvard employment on a specific date, not its sequence relative to OSS service.",
    },
    {
        "key": "state-wiley-b1013",
        "stable_url": "https://history.state.gov/departmenthistory/people/wiley-john-cooper",
        "archival_identifier": "Office of the Historian, Department History, John Cooper Wiley",
        "title": "John Cooper Wiley (1893-1967)",
        "author_creator": "Office of the Historian",
        "repository_publisher": "United States Department of State",
        "locator": "Career Foreign Service Officer profile and mission chronology",
        "access_date": ACCESS_DATE,
        "source_quality": "A_direct_official",
        "rights_notes": "This source documents John Cooper Wiley's diplomatic career but does not by itself connect him to the indexed John C. Wiley.",
    },
]


organizations = [
    {
        "key": "penn-museum-existing-b1013",
        "organization_id": "2a302514-388b-51b7-bb53-0a249ac972c5",
        "canonical_name": "University of Pennsylvania Museum",
        "historical_name": "University Museum, University of Pennsylvania",
        "aliases": ["Penn Museum", "University Museum"],
        "organization_type": "university museum",
        "sector": "academia_and_research",
        "city": "Philadelphia",
        "state_or_region": "Pennsylvania",
        "country": "United States",
        "normalization_notes": "Existing museum organization reused; the African Section remains source wording on the affiliation.",
    },
    {
        "key": "naval-reserve-existing-b1013",
        "organization_id": "1b90fcf6-604d-588b-8a30-7bb08c930c6f",
        "canonical_name": "United States Naval Reserve",
        "historical_name": "United States Naval Reserve",
        "aliases": ["U.S. Naval Reserve", "USNR"],
        "organization_type": "naval reserve component",
        "sector": "military",
        "country": "United States",
        "normalization_notes": "Existing canonical military organization reused.",
    },
    {
        "key": "self-employed-existing-b1013",
        "organization_id": "2d0f4eae-d528-5d59-8b11-6660b1e4fa4a",
        "canonical_name": "Self-employed",
        "historical_name": "Self-employed",
        "aliases": ["Private practice", "Own business"],
        "organization_type": "self-employment status",
        "sector": "self_employed",
        "country": "United States",
        "normalization_notes": "Existing canonical status reused; it does not imply a named firm or employer.",
    },
    {
        "key": "cfr-existing-b1013",
        "organization_id": "9244edb3-b1aa-546a-b280-a12d8ae26f8b",
        "canonical_name": "Council on Foreign Relations",
        "historical_name": "Council on Foreign Relations",
        "aliases": ["CFR"],
        "organization_type": "foreign-policy research organization",
        "sector": "labor_nonprofit_and_religion",
        "city": "New York",
        "state_or_region": "New York",
        "country": "United States",
        "normalization_notes": "Existing canonical organization reused.",
    },
    {
        "key": "harvard-existing-b1013",
        "organization_id": "45ddf347-21c6-59f5-a8ae-517418adf941",
        "canonical_name": "Harvard University",
        "historical_name": "Harvard University",
        "aliases": ["Harvard"],
        "organization_type": "university",
        "sector": "academia_and_research",
        "city": "Cambridge",
        "state_or_region": "Massachusetts",
        "country": "United States",
        "normalization_notes": "Existing canonical university reused. Employment and student relationships remain separate.",
    },
    {
        "key": "state-existing-b1013",
        "organization_id": "4d2fbb5f-218d-5445-b7b3-4c2fd22f0286",
        "canonical_name": "United States Department of State",
        "historical_name": "Department of State",
        "aliases": ["U.S. Department of State", "Foreign Service of the United States"],
        "organization_type": "federal executive department",
        "sector": "federal_government",
        "city": "Washington",
        "state_or_region": "District of Columbia",
        "country": "United States",
        "normalization_notes": "Existing canonical department reused. John Cooper Wiley remains a nonpublic identity candidate for the indexed John C. Wiley.",
    },
]


affiliations: list[dict] = []
claims: list[dict] = []
person_updates: list[dict] = []
research_attempts: list[dict] = []


def source_link(key: str, excerpt: str | None = None, locator: str | None = None) -> dict:
    value = {"source_key": key, "support_type": "supports"}
    if excerpt:
        value["excerpt_override"] = excerpt
    if locator:
        value["locator_override"] = locator
    return value


def add_claim(
    key: str,
    person_id: str,
    claim_type: str,
    text: str,
    paraphrase: str,
    identity: str,
    temporal: str,
    quality: str,
    confidence: str,
    publication: str,
    match_notes: str,
    claim_sources: list[dict],
    affiliation_key: str | None = None,
    excerpt: str | None = None,
) -> None:
    claim = {
        "key": key,
        "person_id": person_id,
        "claim_type": claim_type,
        "claim_text": text,
        "evidence_paraphrase": paraphrase,
        "identity_match_assessment": identity,
        "temporal_assessment": temporal,
        "source_quality": quality,
        "claim_confidence": confidence,
        "publication_status": publication,
        "match_notes": match_notes,
        "sources": claim_sources,
    }
    if affiliation_key:
        claim["affiliation_key"] = affiliation_key
    if excerpt:
        claim["evidence_excerpt"] = excerpt
    claims.append(claim)


for person_id, (code, occupation, entry_date, identity_confidence) in ARMY.items():
    name = next(name for _, pid, name, _ in PEOPLE if pid == person_id)
    slug = name.lower().replace(".", "").replace(" ", "-")
    affiliation_key = f"{slug}-army-occupation-b1013"
    is_student = occupation == "student"
    affiliations.append(
        {
            "key": affiliation_key,
            "person_id": person_id,
            "occupation": occupation,
            "relationship_type": "student" if is_student else "unknown",
            "end_date": entry_date,
            "date_precision": f"Historical civilian-occupation code {code} was recorded at Army entry on {entry_date}; no named employer or institution is supplied.",
            "country": "United States",
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": identity_confidence,
            "claim_confidence": "medium",
            "source_quality": "A_direct_official",
            "publication_status": "publish_qualified",
            "research_notes": "Broad historical category only; no named employer, workplace, school, production, firm, or exact OSS transition is inferred.",
        }
    )
    identity_pub = "published" if identity_confidence == "confirmed" else "publish_qualified"
    identity_claim_conf = "confirmed" if identity_confidence == "confirmed" else "high"
    identity_note = (
        "The exact indexed and Army names agree and a nonshared protected identifier connects the records."
        if identity_confidence == "confirmed"
        else "A nonshared protected identifier and the indexed name connect the records; an unexplained trailing initial keeps identity at high confidence."
    )
    add_claim(
        f"{slug}-army-identity-b1013",
        person_id,
        "identity",
        f"The indexed {name} and the official Army entry refer to the same person.",
        identity_note,
        identity_note,
        "The Army entry predates or bounds the later OSS index context; it does not establish an OSS transfer date.",
        "A_direct_official",
        identity_claim_conf,
        identity_pub,
        "Protected identifiers were compared only in the private database and are omitted from public claims and downloads.",
        [source_link("nara-index-b1013"), source_link("army-bulk-b1013"), source_link("army-tech-b1013")],
    )
    claim_type = "other_pre_oss_affiliation" if is_student else "occupation"
    add_claim(
        f"{slug}-army-occupation-claim-b1013",
        person_id,
        claim_type,
        f"At Army entry on {entry_date}, {name} was classified as {occupation}.",
        f"The official Army record carries historical civilian-occupation code {code}, decoded by NARA as {occupation}.",
        identity_note,
        "The category is recorded at Army entry. It is date-bounded but does not identify the immediate OSS predecessor.",
        "A_direct_official",
        "medium",
        "publish_qualified",
        "The historical category is not converted into a named employer, institution, school, workplace, or production.",
        [source_link("army-bulk-b1013"), source_link("army-tech-b1013"), source_link("army-codes-b1013")],
        affiliation_key=affiliation_key,
    )


for person_id, conflict_text in CONFLICTS.items():
    name = next(name for _, pid, name, _ in PEOPLE if pid == person_id)
    slug = name.lower().replace(".", "").replace(" ", "-")
    add_claim(
        f"{slug}-army-identifier-conflict-b1013",
        person_id,
        "identity",
        "The protected identifier printed in the OSS index conflicts with the name in the official Army record.",
        conflict_text + " No Army identity, occupation, grade, or chronology is transferred.",
        "The names materially disagree despite the same protected identifier; the indexed personnel file is required.",
        "The conflict concerns identity, so the Army chronology cannot be assigned to this person.",
        "A_direct_official",
        "conflicting",
        "conflicting",
        "The protected identifier is retained privately and masked from public output.",
        [source_link("nara-index-b1013"), source_link("army-bulk-b1013"), source_link("army-tech-b1013")],
    )


# Heinrich A. Wieschhoff: date-bounded University Museum curator to OSS chronology.
wieschhoff = "37d1722d-9e45-5228-94c9-daa472b73c3c"
wieschhoff_aff = "heinrich-wieschhoff-penn-museum-b1013"
affiliations.append(
    {
        "key": wieschhoff_aff,
        "person_id": wieschhoff,
        "organization_key": "penn-museum-existing-b1013",
        "organization_name_as_found": "University Museum, University of Pennsylvania, African Section",
        "role_title": "Curator of the African Section",
        "occupation": "anthropologist and Africanist",
        "relationship_type": "employment",
        "start_date": "1941",
        "end_date": "1942",
        "date_precision": "The FernUniversität history dates the curatorship to 1941 and OSS Africa work to 1942-1945; exact appointment and transition dates remain unverified.",
        "city": "Philadelphia",
        "state_or_region": "Pennsylvania",
        "country": "United States",
        "immediate_pre_oss": True,
        "last_civilian_pre_service": True,
        "pre_oss_temporal_basis": "strongly_date_bounded",
        "identity_confidence": "high_confidence",
        "claim_confidence": "high",
        "source_quality": "B_authoritative_institutional",
        "publication_status": "published",
        "research_notes": "The institutional chronology places the University Museum curatorship immediately before OSS Africa work; the personnel file is still needed for exact dates and grade.",
    }
)
add_claim(
    "heinrich-wieschhoff-identity-b1013",
    wieschhoff,
    "identity",
    "The indexed Heinrich A. Wieschhoff is the anthropologist Heinrich Albert Wieschhoff.",
    "Three institutional sources connect the distinctive full name to Pennsylvania anthropology, United States government work, and the 1942-1945 OSS chronology.",
    "Distinctive exact name and middle initial, profession, institution, and wartime government chronology align.",
    "The sources cover the pre-OSS, wartime, and postwar sequence.",
    "B_authoritative_institutional",
    "high",
    "published",
    "No competing Heinrich A. Wieschhoff candidate was found; the direct personnel file has not yet been reviewed.",
    [source_link("nara-index-b1013"), source_link("fernuni-wieschhoff-b1013"), source_link("penn-history-wieschhoff-b1013"), source_link("un-wieschhoff-b1013")],
)
for claim_type, key, text in (
    ("immediate_pre_oss_affiliation", "heinrich-wieschhoff-immediate-b1013", "Heinrich A. Wieschhoff's immediate pre-OSS affiliation was the University Museum, University of Pennsylvania, where he curated the African Section."),
    ("last_civilian_pre_service", "heinrich-wieschhoff-last-civilian-b1013", "Heinrich A. Wieschhoff's last documented civilian employer before OSS service was the University Museum, University of Pennsylvania."),
):
    add_claim(
        key,
        wieschhoff,
        claim_type,
        text,
        "FernUniversität's institutional history dates the curatorship to 1941 and OSS Africa work to 1942-1945; Penn independently documents Wieschhoff in anthropology.",
        "The distinctive name, field, Penn institution, and OSS chronology align across institutional sources.",
        "The 1941 curatorship immediately precedes the 1942-1945 OSS work, although exact transition dates remain unverified.",
        "B_authoritative_institutional",
        "high",
        "published",
        "The claim uses the historical institution name and does not substitute a modern successor organization.",
        [source_link("fernuni-wieschhoff-b1013", "1941 Kurator der Afrikanischen Sektion des Universitätsmuseums ... Zwischen 1942 und 1945 arbeitete Wieschhoff als Afrikaexperte im Office of Strategic Services."), source_link("penn-history-wieschhoff-b1013")],
        affiliation_key=wieschhoff_aff,
    )


# Frederick Stallknecht Wight: Naval Reserve immediately before OSS; self-employed painter before Navy.
wight = "cb1a78c4-c52e-58b6-a68b-5f408babb4a7"
wight_navy_aff = "frederick-wight-naval-reserve-b1013"
wight_self_aff = "frederick-wight-self-employed-b1013"
affiliations.extend(
    [
        {
            "key": wight_navy_aff,
            "person_id": wight,
            "organization_key": "naval-reserve-existing-b1013",
            "organization_name_as_found": "United States Naval Reserve",
            "role_title": "Lieutenant commander",
            "occupation": "naval officer; illustrator and newspaper editor",
            "relationship_type": "military_assignment",
            "start_date": "1942",
            "end_date": "1944",
            "date_precision": "The memorial states 1942-1945 Naval Reserve service and a transfer to OSS after the Normandy landing; the exact transfer date is not stated.",
            "country": "United States",
            "immediate_pre_oss": True,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "explicit_immediate",
            "identity_confidence": "confirmed",
            "claim_confidence": "high",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "published",
            "research_notes": "Military assignment, not a civilian employer. The source explicitly says the Naval Reserve service preceded transfer to OSS.",
        },
        {
            "key": wight_self_aff,
            "person_id": wight,
            "organization_key": "self-employed-existing-b1013",
            "organization_name_as_found": "self-employed",
            "role_title": "Portrait painter and writer",
            "occupation": "artist and novelist",
            "relationship_type": "self_employment",
            "start_date": "1925",
            "end_date": "1942",
            "date_precision": "The biography says Wight supported himself painting portraits after returning from Paris, moved to Chatham in 1938, and joined the Navy during World War II; exact end date is not stated.",
            "city": "Chatham",
            "state_or_region": "Massachusetts",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": True,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "confirmed",
            "claim_confidence": "high",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "publication_status": "published",
            "research_notes": "This is the last documented civilian livelihood before Navy service, separate from the immediate Naval Reserve predecessor to OSS.",
        },
    ]
)
add_claim(
    "frederick-wight-identity-b1013",
    wight,
    "identity",
    "The indexed Frederick Wight is artist and naval officer Frederick Stallknecht Wight.",
    "The exact name, Naval Reserve rank, explicit OSS transfer, and London service form a specific identity bridge.",
    "Exact indexed name plus the institutional memorial's explicit Naval Reserve-to-OSS chronology make the identity match specific.",
    "Both biographies cover the pre-Navy, Naval Reserve, OSS, and postwar sequence.",
    "B_authoritative_institutional",
    "confirmed",
    "published",
    "No competing Frederick Wight with the same wartime chronology was found.",
    [source_link("nara-index-b1013"), source_link("uc-wight-b1013"), source_link("stern-wight-b1013")],
)
add_claim(
    "frederick-wight-immediate-b1013",
    wight,
    "immediate_pre_oss_affiliation",
    "Frederick Wight transferred to OSS after serving as a lieutenant commander in the United States Naval Reserve.",
    "The University of California memorial explicitly states that his Naval Reserve service preceded transfer to OSS; the gallery biography independently places him in the OSS Naval Division.",
    "Exact name, rank, branch, Normandy chronology, and London OSS service align.",
    "The source explicitly identifies the transfer sequence, but not the exact transfer date.",
    "B_authoritative_institutional",
    "high",
    "published",
    "The Naval Reserve is modeled as a military assignment, not a civilian employer.",
    [source_link("uc-wight-b1013", "served as a lieutenant commander, United States Naval Reserve ... and afterwards transferred to the O.S.S."), source_link("stern-wight-b1013")],
    affiliation_key=wight_navy_aff,
)
add_claim(
    "frederick-wight-last-civilian-b1013",
    wight,
    "last_civilian_pre_service",
    "Frederick Wight's last documented civilian livelihood before Navy service was self-employment as a portrait painter and writer.",
    "The gallery biography states that he supported himself painting portraits and later joined the Navy; the university memorial documents novels published before and during the war years.",
    "The exact person and continuous artistic biography are supported by two institutional sources.",
    "The civilian activity precedes Navy service; the exact final working date is not stated.",
    "C_reputable_contemporary_or_scholarly",
    "high",
    "published",
    "No named employing studio, gallery, publisher, or firm is inferred.",
    [source_link("stern-wight-b1013", "Upon his return to Cape Cod, he supported himself painting portraits of figures in art and writing circles."), source_link("uc-wight-b1013")],
    affiliation_key=wight_self_aff,
)


# Louis Arnold Wiesner: Harvard employment, then CFR, then OSS.
wiesner = "286b1d59-b9db-5a12-bdf1-b48165c2a72e"
wiesner_cfr_aff = "louis-wiesner-cfr-b1013"
wiesner_harvard_aff = "louis-wiesner-harvard-b1013"
affiliations.extend(
    [
        {
            "key": wiesner_cfr_aff,
            "person_id": wiesner,
            "organization_key": "cfr-existing-b1013",
            "organization_name_as_found": "Council on Foreign Relations",
            "role_title": "Research Secretary",
            "occupation": "foreign-policy researcher",
            "relationship_type": "employment",
            "start_date": "1942",
            "end_date": "1943",
            "date_precision": "Year precision stated in the AFSA obituary.",
            "city": "New York",
            "state_or_region": "New York",
            "country": "United States",
            "immediate_pre_oss": True,
            "last_civilian_pre_service": True,
            "pre_oss_temporal_basis": "explicit_immediate",
            "identity_confidence": "confirmed",
            "claim_confidence": "confirmed",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "published",
            "research_notes": "The obituary explicitly sequences CFR (1942-43) before OSS research analysis (1943-44).",
        },
        {
            "key": wiesner_harvard_aff,
            "person_id": wiesner,
            "organization_key": "harvard-existing-b1013",
            "organization_name_as_found": "Harvard",
            "role_title": "Graduate Assistant and Teaching Fellow",
            "occupation": "graduate assistant and teaching fellow in history",
            "relationship_type": "employment",
            "start_date": "1939",
            "end_date": "1942",
            "date_precision": "Year precision stated in the AFSA obituary.",
            "city": "Cambridge",
            "state_or_region": "Massachusetts",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "confirmed",
            "claim_confidence": "confirmed",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "published",
            "research_notes": "Earlier documented employment; CFR intervened before OSS.",
        },
    ]
)
add_claim(
    "louis-wiesner-identity-b1013",
    wiesner,
    "identity",
    "The indexed Louis A. Wiesner is Foreign Service officer Louis Arnold Wiesner.",
    "The exact name and middle initial are paired with an explicit 1943-1944 OSS Research Analyst role in AFSA's obituary.",
    "Exact name, middle initial, OSS role, and year range form a direct institutional identity bridge.",
    "The obituary gives a continuous 1939-1944 employment chronology.",
    "B_authoritative_institutional",
    "confirmed",
    "published",
    "The explicit OSS employment line distinguishes this person from namesakes.",
    [source_link("nara-index-b1013"), source_link("afsa-wiesner-b1013")],
)
add_claim(
    "louis-wiesner-immediate-b1013",
    wiesner,
    "immediate_pre_oss_affiliation",
    "Louis A. Wiesner's immediate pre-OSS affiliation was the Council on Foreign Relations, where he served as Research Secretary in 1942-1943.",
    "AFSA explicitly sequences the Council on Foreign Relations role before his 1943-1944 OSS Research Analyst role.",
    "The exact indexed name and explicit OSS chronology identify the person.",
    "The source explicitly provides the immediate sequence.",
    "B_authoritative_institutional",
    "confirmed",
    "published",
    "The Council on Foreign Relations is preserved as the historical employer named by the source.",
    [source_link("afsa-wiesner-b1013", "Research Secretary at the Council on Foreign Relations (1942-43) and then a Research Analyst at the Office of Strategic Services (1943-44).")],
    affiliation_key=wiesner_cfr_aff,
)
add_claim(
    "louis-wiesner-last-civilian-b1013",
    wiesner,
    "last_civilian_pre_service",
    "Louis A. Wiesner's last documented civilian employer before OSS service was the Council on Foreign Relations.",
    "AFSA dates CFR employment to 1942-1943 and OSS employment to 1943-1944.",
    "The exact indexed name and explicit OSS chronology identify the person.",
    "The consecutive year ranges support the last civilian employer designation.",
    "B_authoritative_institutional",
    "confirmed",
    "published",
    "OSS service is treated as the transition point for this project's civilian-employer field.",
    [source_link("afsa-wiesner-b1013")],
    affiliation_key=wiesner_cfr_aff,
)
add_claim(
    "louis-wiesner-harvard-b1013",
    wiesner,
    "other_pre_oss_affiliation",
    "Louis A. Wiesner was employed by Harvard as a Graduate Assistant and Teaching Fellow from 1939 to 1942.",
    "AFSA's obituary states the Harvard titles and dates; the later CFR role prevents this from being labeled immediate pre-OSS employment.",
    "The same continuous obituary identifies the person and later OSS role.",
    "Definitely before OSS, but not immediate because CFR intervened.",
    "B_authoritative_institutional",
    "confirmed",
    "published",
    "This is employment, not merely education; the source explicitly names assistant and teaching-fellow roles.",
    [source_link("afsa-wiesner-b1013", "also a Graduate Assistant and Teaching Fellow from 1939 to 1942")],
    affiliation_key=wiesner_harvard_aff,
)


# Payson S. Wild: exact contemporary Harvard role, sequence to OSS unresolved.
payson = "706f91cf-7f26-5755-b2f1-19699edc7731"
payson_aff = "payson-wild-harvard-b1013"
affiliations.append(
    {
        "key": payson_aff,
        "person_id": payson,
        "organization_key": "harvard-existing-b1013",
        "organization_name_as_found": "Harvard",
        "role_title": "Associate Professor of Government",
        "occupation": "political scientist and professor",
        "relationship_type": "employment",
        "date_precision": "A contemporary Harvard Crimson report documents the role on 1943-03-22; the sequence relative to OSS service is not established.",
        "city": "Cambridge",
        "state_or_region": "Massachusetts",
        "country": "United States",
        "immediate_pre_oss": False,
        "last_civilian_pre_service": False,
        "pre_oss_temporal_basis": "temporal_relation_uncertain",
        "identity_confidence": "high_confidence",
        "claim_confidence": "medium",
        "source_quality": "C_reputable_contemporary_or_scholarly",
        "publication_status": "publish_qualified",
        "research_notes": "The employment is documented on a wartime date, but the personnel file is required to determine whether it preceded, overlapped, or followed the OSS appointment.",
    }
)
add_claim(
    "payson-wild-identity-b1013",
    payson,
    "identity",
    "The indexed Payson S. Wild is the Harvard political scientist of that distinctive name.",
    "A contemporary Harvard report gives the exact uncommon name and middle initial and identifies his government professorship.",
    "The uncommon exact name and middle initial strongly support identity, but the personnel file has not been reviewed.",
    "The report documents a March 1943 role; OSS sequence remains unresolved.",
    "C_reputable_contemporary_or_scholarly",
    "high",
    "published",
    "No competing Payson S. Wild was found.",
    [source_link("nara-index-b1013"), source_link("crimson-payson-wild-b1013")],
)
add_claim(
    "payson-wild-harvard-claim-b1013",
    payson,
    "other_pre_oss_affiliation",
    "Payson S. Wild was an Associate Professor of Government at Harvard in March 1943.",
    "The contemporary Crimson report identifies Wild's Harvard title while describing his wartime committee work.",
    "The distinctive exact name and middle initial strongly support identity.",
    "Employment is documented on 1943-03-22, but its sequence relative to OSS service is uncertain.",
    "C_reputable_contemporary_or_scholarly",
    "medium",
    "publish_qualified",
    "The profile must not label Harvard the immediate or last civilian employer until the OSS appointment date is established.",
    [source_link("crimson-payson-wild-b1013", "Payson S. Wild, associate professor of Government")],
    affiliation_key=payson_aff,
)


# John C. Wiley: retain John Cooper Wiley as a private, low-confidence candidate only.
wiley = "e787fa88-e6c7-53f2-83db-2d509a343a58"
wiley_aff = "john-wiley-state-candidate-b1013"
affiliations.append(
    {
        "key": wiley_aff,
        "person_id": wiley,
        "organization_key": "state-existing-b1013",
        "organization_name_as_found": "Foreign Service of the United States",
        "role_title": "Career Foreign Service Officer",
        "occupation": "diplomat",
        "relationship_type": "government_assignment",
        "end_date": "1940-07-25",
        "date_precision": "The official profile dates John Cooper Wiley's departure from Riga; no inspected source directly bridges him to the indexed John C. Wiley or establishes the intervening 1940-1944 chronology.",
        "country": "United States",
        "immediate_pre_oss": False,
        "last_civilian_pre_service": False,
        "pre_oss_temporal_basis": "temporal_relation_uncertain",
        "identity_confidence": "probable",
        "claim_confidence": "low",
        "source_quality": "A_direct_official",
        "publication_status": "withheld_low_confidence",
        "research_notes": "Nonpublic candidate only. An exact name and plausible diplomatic chronology are insufficient for this common-name case without an OSS, personnel-file, or second corroborating identifier bridge.",
    }
)
add_claim(
    "john-wiley-state-candidate-identity-b1013",
    wiley,
    "identity",
    "John Cooper Wiley is a candidate for the indexed John C. Wiley, not a resolved identity.",
    "The official State profile supplies the full name and diplomatic chronology, but no inspected source directly links that diplomat to this OSS index row.",
    "An exact name match alone is insufficient for this common-name case.",
    "A 1940-1944 chronology gap prevents assignment of the State career as a pre-OSS fact.",
    "A_direct_official",
    "low",
    "needs_review",
    "A direct personnel-file or explicit OSS document bridge is required before publication.",
    [source_link("nara-index-b1013"), source_link("state-wiley-b1013")],
)
add_claim(
    "john-wiley-state-candidate-affiliation-b1013",
    wiley,
    "other_pre_oss_affiliation",
    "John Cooper Wiley served in the United States Foreign Service, but that career is not yet assigned publicly to the indexed John C. Wiley.",
    "The official profile documents John Cooper Wiley's career, not the identity bridge to the OSS index row.",
    "Probable candidate only; exact name is not enough.",
    "The official career predates the index era, but the candidate's OSS sequence is unverified.",
    "A_direct_official",
    "low",
    "withheld_low_confidence",
    "Excluded from public facts, downloads, and default analytics pending direct evidence.",
    [source_link("state-wiley-b1013")],
    affiliation_key=wiley_aff,
)


def archival_next(name: str, box: str, extra: str = "") -> str:
    base = (
        f"Review the indexed Box {box} personnel file for corroborating identifiers, the immediate pre-OSS affiliation, and the last civilian employer before wartime service. "
        "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed."
    )
    return base + (f" {extra}" if extra else "")


for row, person_id, name, box in PEOPLE:
    if person_id in ARMY:
        code, occupation, entry_date, identity_confidence = ARMY[person_id]
        extra = ""
        if person_id == "544bb2dd-2960-5f20-9e14-455e9713bd4c":
            extra = " The Army entry's trailing L remains an unexplained name difference."
        if person_id == "6626039a-00cd-5019-83cf-ba7c2ee78786":
            extra = " An older artist with the same name lacks the junior suffix and Army bridge and was rejected as a namesake."
        identity_evidence = (
            f"The visually verified page 503 row and official Army entry agree on the indexed name and a nonshared protected identifier. Historical code {code} supports only a qualified {occupation} category at Army entry on {entry_date}; no named employer, institution, or exact OSS-transfer date is supplied.{extra}"
        )
        person_updates.append(
            {
                "person_id": person_id,
                "identity_status": identity_confidence,
                "identity_evidence": identity_evidence,
                "personnel_category": "enlisted_army_personnel",
                "commissioned_officer": False,
                "manual_review_required": True,
                "research_status": "occupation_only_found",
                "next_action": f"Review the indexed Box {box} personnel file to identify the named employer or institution and exact OSS transition; preserve code {code} only as the broad Army-entry category.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            }
        )
    elif person_id in CONFLICTS:
        person_updates.append(
            {
                "person_id": person_id,
                "identity_status": "conflicting",
                "identity_evidence": CONFLICTS[person_id] + " No Army identity, occupation, grade, or chronology is transferred pending direct personnel-file review.",
                "manual_review_required": True,
                "research_status": "conflicting_sources",
                "next_action": f"Review the indexed Box {box} personnel file and reconcile the protected-identifier conflict before assigning any Army record or pre-OSS affiliation.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            }
        )
    elif person_id == wieschhoff:
        person_updates.append(
            {
                "person_id": person_id,
                "identity_status": "high_confidence",
                "identity_evidence": "Distinctive exact name and middle initial, Penn anthropology and museum work, a 1941 curatorship, 1942-1945 OSS Africa work, and later United Nations service align across three institutional sources.",
                "name_variants": ["Heinrich Albert Wieschhoff"],
                "personnel_category": "civilian_professional_or_administrative_grade",
                "commissioned_officer": False,
                "manual_review_required": True,
                "research_status": "verified_employer_found",
                "next_action": "Review Box 836 to confirm the exact University Museum departure, OSS appointment date, and personnel grade.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "medium",
            }
        )
    elif person_id == wight:
        person_updates.append(
            {
                "person_id": person_id,
                "identity_status": "confirmed",
                "identity_evidence": "The exact indexed name, lieutenant commander rank, Naval Reserve service, Normandy chronology, and explicit transfer to OSS align in University of California and artist-biography sources.",
                "name_variants": ["Frederick S. Wight", "Frederick Stallknecht Wight"],
                "personnel_category": "commissioned_naval_officer",
                "commissioned_officer": True,
                "manual_review_required": True,
                "research_status": "verified_employer_found",
                "next_action": "Review Box 836 to establish the exact Naval Reserve-to-OSS transfer date and verify whether portrait work continued until Navy entry.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "medium",
            }
        )
    elif person_id == wiesner:
        person_updates.append(
            {
                "person_id": person_id,
                "identity_status": "confirmed",
                "identity_evidence": "AFSA's institutional obituary explicitly identifies Louis A. Wiesner as a Council on Foreign Relations Research Secretary in 1942-1943 and OSS Research Analyst in 1943-1944.",
                "name_variants": ["Louis Arnold Wiesner"],
                "personnel_category": "civilian_professional_or_administrative_grade",
                "commissioned_officer": False,
                "manual_review_required": True,
                "research_status": "verified_employer_found",
                "next_action": "Review Box 836 to confirm exact CFR departure and OSS appointment dates and personnel grade.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "medium",
            }
        )
    elif person_id == payson:
        person_updates.append(
            {
                "person_id": person_id,
                "identity_status": "high_confidence",
                "identity_evidence": "A contemporary Harvard report gives the distinctive exact name and middle initial and identifies Payson S. Wild as Associate Professor of Government on 1943-03-22; the OSS appointment sequence is not established.",
                "personnel_category": "civilian_professional_or_administrative_grade",
                "commissioned_officer": False,
                "manual_review_required": True,
                "research_status": "needs_temporal_review",
                "next_action": "Review Box 836 for the OSS appointment date and determine whether Harvard employment preceded, overlapped, or followed OSS service.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            }
        )
    elif person_id == wiley:
        person_updates.append(
            {
                "person_id": person_id,
                "identity_status": "probable",
                "identity_evidence": "John Cooper Wiley is a plausible candidate because the official State profile supplies the full name and a wartime diplomatic chronology, but no inspected source directly links him to the indexed John C. Wiley. The candidate remains nonpublic.",
                "manual_review_required": True,
                "research_status": "needs_identity_review",
                "next_action": "Review Box 836 or an explicit OSS document for a second corroborating identifier before assigning John Cooper Wiley's State Department career to this index row.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            }
        )
    elif person_id == "988b1615-a74b-5020-a82d-cbd8831f21c9":
        person_updates.append(
            {
                "person_id": person_id,
                "manual_review_required": True,
                "research_status": "verified_employer_found",
                "next_action": "Review Box 836 to confirm Wilbur's OSS grade and exact Field Museum departure and OSS appointment dates.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "medium",
            }
        )
    else:
        special = SPECIAL_REJECTIONS.get(person_id, "")
        identity_evidence = (
            f"The visually verified page 503 source preserves {name}, archival Box {box}, and the printed index context. "
            + (special + " " if special else "")
            + "Exact-name and meaningful-variant searches across the NARA index context, OSS, employment, occupation, obituary, institutional, newspaper, directory, and archival sources produced no reliable identity and pre-OSS affiliation bridge; unbridged namesakes were rejected."
        )
        person_updates.append(
            {
                "person_id": person_id,
                "identity_status": "unresolved",
                "identity_evidence": identity_evidence,
                "manual_review_required": True,
                "research_status": "requires_archival_review",
                "next_action": archival_next(name, box, special),
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            }
        )

    if person_id in ARMY:
        outcome = "source_reviewed"
        reviewed = 9
        rejected = 5
        code, occupation, entry_date, _ = ARMY[person_id]
        notes = f"An accepted official Army bridge supports identity and a qualified {occupation} category at Army entry on {entry_date}; no named employer or exact OSS-transfer date is supplied."
    elif person_id in CONFLICTS:
        outcome = "source_reviewed"
        reviewed = 8
        rejected = 5
        notes = CONFLICTS[person_id] + " The conflict is preserved; no Army occupation or chronology was transferred."
    elif person_id == wieschhoff:
        outcome = "source_reviewed"
        reviewed = 10
        rejected = 4
        notes = "Three institutional sources support the distinctive identity and a strongly date-bounded University Museum curatorship immediately before 1942-1945 OSS Africa work."
    elif person_id == wight:
        outcome = "source_reviewed"
        reviewed = 9
        rejected = 3
        notes = "University and artist-biography sources support the Naval Reserve-to-OSS transfer and separate earlier self-employment as a portrait painter and writer."
    elif person_id == wiesner:
        outcome = "source_reviewed"
        reviewed = 8
        rejected = 3
        notes = "AFSA's obituary explicitly sequences Harvard employment, Council on Foreign Relations employment, OSS service, and the Foreign Service."
    elif person_id == payson:
        outcome = "source_reviewed"
        reviewed = 8
        rejected = 4
        notes = "A contemporary Harvard report supports identity and Harvard employment on 1943-03-22, but the sequence relative to OSS service remains unresolved."
    elif person_id == wiley:
        outcome = "candidate_found"
        reviewed = 9
        rejected = 6
        notes = "John Cooper Wiley remains a private low-confidence candidate. The official State profile lacks a direct OSS or personnel-file bridge, and search snippets or book-search text were not accepted as final evidence."
    elif person_id == "988b1615-a74b-5020-a82d-cbd8831f21c9":
        outcome = "source_reviewed"
        reviewed = 5
        rejected = 2
        notes = "Existing reviewed Field Museum and NARA evidence was rechecked and preserved without duplicating or downgrading the published affiliation or claims."
    else:
        outcome = "candidate_rejected"
        reviewed = 6
        rejected = 5
        notes = SPECIAL_REJECTIONS.get(person_id, "")
        if notes:
            notes += " "
        notes += "Exact-name and meaningful-variant searches produced no reliable identity and pre-OSS affiliation bridge; unbridged namesakes were rejected."

    common_notes = (
        " Exact-name official-domain, OSS, employer, occupation, obituary, biography, institutional, newspaper, directory, and archival searches were checked as applicable. "
        "NARA index page 503 and relevant Army code-list and institutional evidence pages were visually checked. "
        "The CIA adapter was disallowed by robots policy and the Library of Congress adapter timed out during bounded checks for Arthur J. Wildt; neither failure is treated as a negative result. Manual accessible alternatives were reviewed. "
        "No authenticated NARA Catalog API call was made."
    )
    attempt_number = 4 if person_id == "cfee7651-162f-5c02-9354-88a8166a24d2" else (2 if person_id == "988b1615-a74b-5020-a82d-cbd8831f21c9" else 1)
    research_attempts.append(
        {
            "key": f"page503-row{row}-{name.lower().replace('.', '').replace(' ', '-')}-b1013",
            "person_id": person_id,
            "source_adapter": "manual_staged_protocol",
            "query_text": f"{name}; NARA OSS index context; bounded CIA Reading Room and Library of Congress adapter checks; exact-name and meaningful spelling, initial, suffix, punctuation, and OCR variants; OSS, rank, branch, assignment, and identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory, and archival searches; indexed Box {box}; protected identifiers used only in private official-record comparison",
            "query_variant_type": "staged_identity_employment_archival_protocol_batch_1013",
            "started_at": STARTED_AT,
            "completed_at": COMPLETED_AT,
            "outcome": outcome,
            "sources_reviewed": reviewed,
            "candidate_sources_rejected": rejected,
            "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, postwar-only leads, discovery-only biographies, and sources without an OSS, protected-identifier, rank, unit, or personnel-file bridge were rejected. Historical Army categories were not converted into named employers, workplaces, schools, or institutions. Student status was not converted into employment.",
            "research_notes": notes + common_notes,
            "next_action": next(update["next_action"] for update in person_updates if update["person_id"] == person_id),
            "attempt_number": attempt_number,
            "research_agent_version": AGENT_VERSION,
        }
    )


bundle = {
    "bundle_version": "batch-1013-v1",
    "reviewer": "Before OSS Batch 1013 evidence review",
    "sources": sources,
    "organizations": organizations,
    "affiliations": affiliations,
    "claims": claims,
    "person_updates": person_updates,
    "research_attempts": research_attempts,
}


OUT.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(
    json.dumps(
        {
            "output": str(OUT),
            "sources": len(sources),
            "organizations": len(organizations),
            "affiliations": len(affiliations),
            "claims": len(claims),
            "person_updates": len(person_updates),
            "research_attempts": len(research_attempts),
        },
        indent=2,
    )
)
