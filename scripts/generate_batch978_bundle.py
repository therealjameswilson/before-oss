#!/usr/bin/env python3
"""Generate the reviewed Batch 978 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page479-william-van-cleef-to-samuel-van-hyning-"
    "review_batch-978_2026-10-30.json"
)

INDEX = "nara-index-b978"
ARMY = "army-bulk-b978"
TECH = "army-tech-b978"
CODES = "army-codes-b978"
BOWDOIN = "bowdoin-thomas-van-cleve-b978"
HISTORIC_ENGLAND = "historic-england-ides-van-der-gracht-b978"
OCTAGON = "aia-octagon-ides-van-der-gracht-b978"
ARCH_FORUM = "architectural-forum-ides-van-der-gracht-b978"
CIA_IDES = "cia-ides-van-der-gracht-operation-melanie-b978"
NARA_PAUL = "nara-paul-van-der-stricht-b978"
DVIDS_PAUL = "dvids-paul-van-der-stricht-b978"
TOLEDO_PAUL = "toledo-paul-van-der-stricht-b978"
TNA_JAN = "tna-jan-willem-van-driel-b978"
TNA_EMILE = "tna-emile-jean-elise-van-dyck-b978"
TNA_MARCEL = "tna-marcel-van-essen-b978"
CIA_ANDREW = "cia-andrew-van-esso-b978"
CIA_SAMUEL = "cia-samuel-van-hyning-coi-b978"

ORG_BOWDOIN = "bowdoin-b978"
ORG_AAF_345 = "aaf-345th-b978"
ORG_IDES_KILHAM = "ides-van-der-gracht-kilham-b978"
ORG_DELANO_ALDRICH = "delano-aldrich-b978"
ORG_COI = "coordinator-information-b978"


PEOPLE = {
    1: ("9db44dbe-b1b5-5303-8d36-819031afc12c", "William R Van Cleef"),
    2: ("5a9235b3-8018-5c0a-8c72-52b790897b30", "Richard L Van Cleve"),
    3: ("82f89e15-2a94-5280-950e-0d0cc1bba43b", "Thomas C Van Cleve"),
    4: ("c445350f-04b1-50b8-b933-061d5b0e9807", "John Van Costen"),
    5: ("2cf892b1-527f-5d01-bcf2-7dc1931e0668", "Albert Van Dam"),
    6: ("98b21a2b-b6c9-5690-8c1c-250795ae0239", "Cecil Van Den Beldt"),
    7: ("b71ef978-46c4-5d13-b5e7-f9f91cec2e80", "Ides Van Der Grac"),
    8: ("888a34d4-9b1b-5ae1-bbe2-a56fb00b2582", "George T Van Der Hoef"),
    9: ("263ae5be-4956-56c8-aa00-8e8e1d57d7af", "Paul R Van DerStricht"),
    10: ("2fa57046-ac09-5f66-b172-bd1fe428859f", "Jan W Van Driel"),
    11: ("d31820a7-1c8f-5514-9f78-b58cdb7481f9", "John Van Duyne"),
    12: ("08691531-2228-529b-84e3-28415a47daf7", "Emile J Van Dyck"),
    13: ("97efd8f9-be4d-5614-b6c0-e0e68fed0bca", "Margi Van Ende"),
    14: ("7c9f011a-69e4-58de-8abd-c6f49c9a350a", "Marcel Van Essen"),
    15: ("d59ad61c-a247-53c3-9863-40253350adeb", "Andrew E Van Esso"),
    16: ("f194594e-ee92-591a-a669-cb4771566bdf", "William Van Ewijk"),
    17: ("7d6043d3-e6f6-511b-ba65-42b2dfc26ca2", "Stephen C Van Fleet"),
    18: ("933aa9c0-d0c1-550d-8a5f-190564980b7d", "Edwin H Van Gessel"),
    19: ("6d1db677-9282-5e5a-b534-59c5ac87c3f5", "John T Van Hart"),
    20: ("c242b464-4491-5e4e-b271-fe81aeab10e5", "Alice Van Hoesen"),
    21: ("b96f8c23-e90e-5258-b800-893834cc9c23", "Florence Van Horn"),
    22: ("cd36567d-8292-5dc0-b15f-4d989bcc5028", "Charles H Van Houten"),
    23: ("3c7e94ee-2f09-553f-a9c6-05b77733a781", "Samuel Van Hyning"),
}

NEXT_PAUL_VAN_DENSTRICHT = "a1146a1f-3102-5b31-8565-c93ccc980831"
WILLIAM_DUPLICATE_GROUP = "page479-william-r-van-cleef-boxes-797-798"
PAUL_DUPLICATE_GROUP = "page479-480-paul-van-der-stricht-box798"

ARMY_OCCUPATIONS = [
    {
        "row": 5,
        "date": "1942-10-30",
        "code": "471",
        "occupation": "Jewelers, watchmakers, goldsmiths, and silversmiths",
        "public_occupation": "jeweler, watchmaker, goldsmith, or silversmith",
        "locator": "PDF physical page 173; category 4-71 Jewelers, watchmakers, goldsmiths, and silversmiths",
    },
    {
        "row": 19,
        "date": "1942-05-18",
        "code": "134",
        "occupation": "Shipping and receiving clerks",
        "public_occupation": "shipping or receiving clerk",
        "locator": "PDF physical page 171; category 1-34 Shipping and receiving clerks",
    },
]

UNRESOLVED = {
    1: "The adjacent same-name William R Van Cleef row in Box 798 remains separate; no reviewed source establishes duplication or either man's pre-OSS affiliation.",
    2: "Exact-name, initial, institutional, military, newspaper, obituary and archival searches produced no reliable identity bridge for Richard L Van Cleve.",
    4: "A federal fisheries biologist named John Van Oosten is only a spelling-variant namesake lead; no source bridges him to the indexed John Van Costen or OSS.",
    6: "An official Army candidate sharing the protected identifier names a different person and was rejected; no occupation or employer was transferred to Cecil Van Den Beldt.",
    8: "Exact-name and spacing-variant official, institutional, newspaper and archival searches produced no reliable identity bridge for George T Van Der Hoef.",
    11: "A postwar engineer with a similar name lacks the indexed warrant-style identifier and an OSS bridge and was rejected as a namesake lead.",
    13: "Exact-name and spacing-variant official, institutional, newspaper, obituary and archival searches produced no reliable identity bridge for Margi Van Ende.",
    16: "A Dutch resistance casualty with the same name died before OSS operations represented by this row and was rejected as a namesake; no indexed-person employer was found.",
    17: "A National Park Service namesake and other exact-name results lack the middle initial, protected identifier or OSS bridge needed to resolve Stephen C Van Fleet.",
    18: "Exact-name and spacing-variant official, institutional, newspaper, obituary and archival searches produced no reliable identity bridge for Edwin H Van Gessel.",
    20: "Social, educational and obituary results for Alice Van Hoesen do not establish the indexed identity or a pre-OSS employer.",
    21: "Common-name directory, teaching and obituary results do not provide the corroborating identifiers needed to resolve Florence Van Horn.",
    22: "A wartime airman namesake held a different rank from the indexed lieutenant colonel and was rejected; no reliable pre-OSS affiliation was found.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 797-800",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 479, rows 24-46; checked against layout-preserving text and an original-detail page render",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate; literal spellings, rank, clipped notes and location changes are preserved.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; three Batch 978 identity comparisons; protected identifiers and record ordinals withheld",
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
            "locator": "PDF physical pages 171 and 173; Batch 978 categories visually and textually checked",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical categories identify neither employers nor workplaces and are retained only where needed for auditability.",
        },
        {
            "key": BOWDOIN,
            "stable_url": "https://archivesspace.bowdoin.edu/repositories/2/resources/375",
            "archival_identifier": "Thomas Curtis Van Cleve Papers, M230",
            "title": "Thomas Curtis Van Cleve papers",
            "author_creator": "George J. Mitchell Department of Special Collections & Archives",
            "repository_publisher": "Bowdoin College Library",
            "publication_record_date": "Finding aid; collection dates 1912-1976",
            "locator": "Biographical/Historical Note: Bowdoin teaching, 1915-1954, interrupted by intelligence-officer service in both world wars",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Bowdoin College Special Collections & Archives",
        },
        {
            "key": HISTORIC_ENGLAND,
            "stable_url": "https://historicengland.org.uk/listing/the-list/list-entry/1375679",
            "archival_identifier": "National Heritage List for England 1375679",
            "title": "Aller Park School",
            "author_creator": "Historic England",
            "repository_publisher": "Historic England",
            "publication_record_date": "Listed 1998-07-16",
            "locator": "Official list entry, Details: 1929-31 design by Ides van der Gracht of Delano and Aldrich of New York",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "National Heritage List for England",
        },
        {
            "key": OCTAGON,
            "stable_url": "https://www.usmodernist.org/AJ/AJ-1943-09.pdf",
            "title": "The Octagon, September 1943",
            "author_creator": "American Institute of Architects",
            "repository_publisher": "American Institute of Architects; USModernist scan",
            "publication_record_date": "1943-09",
            "locator": "PDF page 4: April 1943 letter from Capt. Ides van der Gracht, 345th Bombardment Squadron, describing his intelligence-officer assignment",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "American Institute of Architects journal archive",
        },
        {
            "key": ARCH_FORUM,
            "stable_url": "https://www.usmodernist.org/AF/AF-1940-08.pdf",
            "title": "The Architectural Forum, August 1940",
            "author_creator": "Architectural Forum editorial staff",
            "repository_publisher": "Architectural Forum; USModernist scan",
            "publication_record_date": "1940-08",
            "locator": "Pages 127-133: Lincoln Hall project credited to Ides van der Gracht and Walter H. Kilham, Jr., Architects",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Architectural Forum archive",
        },
        {
            "key": CIA_IDES,
            "stable_url": "https://www.cia.gov/readingroom/docs/CIA-RDP91-00901R000400100003-3.pdf",
            "archival_identifier": "CIA-RDP91-00901R000400100003-3",
            "title": "Christian Science Monitor report on OSS veterans receiving the Dutch Resistance Memorial Cross",
            "author_creator": "Christian Science Monitor; released by Central Intelligence Agency",
            "repository_publisher": "CIA Reading Room",
            "publication_record_date": "1984 report; approved for release 2005-12-14",
            "locator": "Names Ides van der Gracht as a leader of OSS Operation Melanie in 1944",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "CIA Freedom of Information Act Electronic Reading Room",
        },
        {
            "key": NARA_PAUL,
            "stable_url": "https://www.archives.gov/files/research/jfk/releases/2022/104-10165-10133.pdf",
            "archival_identifier": "JFK release 104-10165-10133",
            "title": "Memorandum concerning Sgt. James J. Carpenter",
            "author_creator": "Paul van der Stricht, Lt. Col., AUS, Chief, Western European Section",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1944-10-10",
            "locator": "Headquarters OSS, European Theater of Operations, United States Army Forward; signature and title block",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "John F. Kennedy Assassination Records Collection",
            "document_number": "104-10165-10133",
        },
        {
            "key": DVIDS_PAUL,
            "stable_url": "https://www.dvidshub.net/news/467950/john-bross-receives-army-air-forces-commission-april-1942",
            "title": "John Bross Receives Army Air Forces Commission (April 1942)",
            "author_creator": "Lori S. Stewart, USAICoE Command Historian",
            "repository_publisher": "U.S. Army Intelligence Center of Excellence; Defense Visual Information Distribution Service",
            "publication_record_date": "2024-04-05",
            "locator": "Paragraph identifying Capt. Paul van der Stricht among the lawyers and officers assigned to England by January 1943",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "This Week in Military Intelligence History",
        },
        {
            "key": TOLEDO_PAUL,
            "stable_url": "https://core.ac.uk/download/pdf/213387027.pdf",
            "title": "Freeing France: The Allies, the Resistance, and the Jedburghs",
            "author_creator": "University of Toledo doctoral dissertation",
            "repository_publisher": "University of Toledo; CORE",
            "publication_record_date": "Scholarly dissertation",
            "locator": "Page 58: Paul van der Stricht described as a former New York attorney arriving for OSS work in January 1943",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "University of Toledo electronic theses and dissertations",
        },
        {
            "key": TNA_JAN,
            "stable_url": "https://discovery.nationalarchives.gov.uk/details/r/C9134612",
            "archival_identifier": "HS 9/1504/1",
            "title": "Jan Willem VAN DRIEL - born 28.02.1922",
            "author_creator": "Special Operations Executive",
            "repository_publisher": "The National Archives (United Kingdom)",
            "publication_record_date": "1939-1946",
            "locator": "Special Operations Executive personnel file catalogue entry",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "Records of Special Operations Executive: Personnel Files",
        },
        {
            "key": TNA_EMILE,
            "stable_url": "https://discovery.nationalarchives.gov.uk/details/r/C9134615",
            "archival_identifier": "HS 9/1504/4",
            "title": "Emile Jean Elise VAN DYCK - born 27.10.1919",
            "author_creator": "Special Operations Executive",
            "repository_publisher": "The National Archives (United Kingdom)",
            "publication_record_date": "1939-1946",
            "locator": "Special Operations Executive personnel file catalogue entry",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "Records of Special Operations Executive: Personnel Files",
        },
        {
            "key": TNA_MARCEL,
            "stable_url": "https://discovery.nationalarchives.gov.uk/details/r/C9134617",
            "archival_identifier": "HS 9/1504/6",
            "title": "Marcel VAN ESSEN - born 01.09.1916",
            "author_creator": "Special Operations Executive",
            "repository_publisher": "The National Archives (United Kingdom)",
            "publication_record_date": "1939-1946",
            "locator": "Special Operations Executive personnel file catalogue entry",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "Records of Special Operations Executive: Personnel Files",
        },
        {
            "key": CIA_ANDREW,
            "stable_url": "https://www.cia.gov/readingroom/docs/1957-10-10.pdf",
            "title": "Central Intelligence Group employment correspondence",
            "author_creator": "Andrew E. Van Esso, Chief, Procurement and Placement Section, Personnel Division",
            "repository_publisher": "CIA Reading Room",
            "publication_record_date": "1947-07-07; released compilation",
            "locator": "Letter signed by Andrew E. Van Esso in his postwar Central Intelligence Group personnel role",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "CIA Freedom of Information Act Electronic Reading Room",
            "rights_notes": "Postwar identity context only; not evidence of a pre-OSS employer.",
        },
        {
            "key": CIA_SAMUEL,
            "stable_url": "https://www.cia.gov/resources/csi/static/Eastern-Front-Turning-Point.pdf",
            "title": "The Eastern Front at the Turning Point",
            "repository_publisher": "Central Intelligence Agency, Center for the Study of Intelligence",
            "publication_record_date": "Declassified historical study",
            "locator": "Note 1: Samuel Van Hyning among the participants preparing COI Monograph No. 6, dated 1942-03-25",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Studies in Intelligence",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": ORG_BOWDOIN,
            "organization_id": "0881619e-5c59-5f34-bd86-11f409bfa463",
            "canonical_name": "Bowdoin College",
            "historical_name": "Bowdoin College",
            "aliases": ["Bowdoin"],
            "organization_type": "college",
            "sector": "academia_and_research",
            "city": "Brunswick",
            "state_or_region": "Maine",
            "country": "United States",
            "normalization_notes": "Existing canonical organization reused.",
        },
        {
            "key": ORG_AAF_345,
            "canonical_name": "345th Bombardment Squadron, United States Army Air Forces",
            "historical_name": "345th Bombardment Squadron",
            "aliases": ["A.A.F. 345th Bombardment Squadron"],
            "organization_type": "military unit",
            "sector": "military",
            "country": "United States",
            "active_dates": "Documented in North Africa in April 1943",
            "normalization_notes": "The squadron is kept distinct from the Army Air Forces as a whole.",
        },
        {
            "key": ORG_IDES_KILHAM,
            "canonical_name": "Ides van der Gracht and Walter H. Kilham Jr., Architects",
            "historical_name": "Ides van der Gracht & Walter H. Kilham, Jr., Architects",
            "aliases": ["van der Gracht and Kilham"],
            "organization_type": "architectural practice",
            "sector": "business_and_industry",
            "city": "New York",
            "state_or_region": "New York",
            "country": "United States",
            "active_dates": "Documented in 1940",
            "normalization_notes": "Historical partnership name retained; no modern successor substituted.",
        },
        {
            "key": ORG_DELANO_ALDRICH,
            "canonical_name": "Delano & Aldrich",
            "historical_name": "Delano and Aldrich",
            "aliases": ["Delano & Aldrich of New York"],
            "organization_type": "architectural firm",
            "sector": "business_and_industry",
            "city": "New York",
            "state_or_region": "New York",
            "country": "United States",
            "active_dates": "Ides van der Gracht documented with the firm, 1929-1931",
            "normalization_notes": "Historical firm name preserved exactly; the source does not establish a modern successor relationship.",
        },
        {
            "key": ORG_COI,
            "organization_id": "7717ee63-f94b-59b6-a06e-5b0f44350338",
            "canonical_name": "Coordinator of Information",
            "historical_name": "Office of the Coordinator of Information",
            "aliases": ["COI"],
            "organization_type": "federal intelligence organization",
            "sector": "federal_government",
            "city": "Washington",
            "state_or_region": "District of Columbia",
            "country": "United States",
            "active_dates": "1941-1942",
            "normalization_notes": "Existing canonical predecessor organization reused; participation is not silently converted into formal employment.",
        },
    ]


def occupation_affiliation(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    name = PEOPLE[row][1]
    return {
        "key": f"{slug(name)}-occupation-b978",
        "person_id": PEOPLE[row][0],
        "occupation": str(item["public_occupation"]),
        "relationship_type": "unknown",
        "start_date": str(item["date"]),
        "end_date": str(item["date"]),
        "date_precision": "Dated at Army entry; the historical category does not name an employer, workplace or duration",
        "country": "United States",
        "immediate_pre_oss": False,
        "last_civilian_pre_service": False,
        "pre_oss_temporal_basis": "strongly_date_bounded",
        "identity_confidence": "high_confidence",
        "claim_confidence": "medium",
        "source_quality": "A_direct_official",
        "publication_status": "publish_qualified",
        "research_notes": "Official historical occupation category only; excluded from employer analytics.",
    }


def affiliations() -> list[dict[str, object]]:
    values = [occupation_affiliation(item) for item in ARMY_OCCUPATIONS]
    values.extend(
        [
            {
                "key": "thomas-van-cleve-bowdoin-b978",
                "person_id": PEOPLE[3][0],
                "organization_key": ORG_BOWDOIN,
                "organization_name_as_found": "Bowdoin College",
                "role_title": "professor of history and political science",
                "occupation": "college professor",
                "relationship_type": "employment",
                "start_date": "1915",
                "end_date": "1942",
                "date_precision": "Teaching began in 1915 and was interrupted by World War II intelligence service; the exact interruption date is not supplied",
                "city": "Brunswick",
                "state_or_region": "Maine",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "probable_immediate",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Bowdoin is the last documented civilian employer before his World War II intelligence service; the precise OSS accession sequence remains unresolved.",
            },
            {
                "key": "ides-van-der-gracht-aaf-b978",
                "person_id": PEOPLE[7][0],
                "organization_key": ORG_AAF_345,
                "organization_name_as_found": "A.A.F. 345th Bombardment Squadron",
                "role_title": "intelligence officer",
                "occupation": "Army Air Forces officer",
                "relationship_type": "military_assignment",
                "start_date": "1943-04",
                "end_date": "1943-04",
                "date_precision": "Contemporary letter dated April 1943; duration not stated",
                "country": "United States",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "probable_immediate",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "published",
                "research_notes": "Best-supported immediate pre-OSS military pathway: April 1943 Army Air Forces intelligence assignment before documented 1944 OSS Operation Melanie leadership.",
            },
            {
                "key": "ides-van-der-gracht-kilham-b978",
                "person_id": PEOPLE[7][0],
                "organization_key": ORG_IDES_KILHAM,
                "organization_name_as_found": "Ides van der Gracht & Walter H. Kilham, Jr., Architects",
                "role_title": "architect and partner",
                "occupation": "architect",
                "relationship_type": "self_employment",
                "start_date": "1940",
                "end_date": "1940",
                "date_precision": "Architectural Forum project credit in August 1940; start and end dates not stated",
                "city": "New York",
                "state_or_region": "New York",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "published",
                "research_notes": "Last documented civilian professional practice before his Army Air Forces service; treated as self-employment in an eponymous partnership.",
            },
            {
                "key": "ides-van-der-gracht-delano-aldrich-b978",
                "person_id": PEOPLE[7][0],
                "organization_key": ORG_DELANO_ALDRICH,
                "organization_name_as_found": "Delano and Aldrich of New York",
                "role_title": "architect",
                "occupation": "architect",
                "relationship_type": "employment",
                "start_date": "1929",
                "end_date": "1931",
                "date_precision": "Official listed-building description dates the project 1929-1931",
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
                "research_notes": "Earlier documented prewar firm affiliation; not presented as the immediate predecessor to OSS.",
            },
            {
                "key": "paul-van-der-stricht-attorney-b978",
                "person_id": PEOPLE[9][0],
                "occupation": "attorney",
                "relationship_type": "unknown",
                "end_date": "1943-01",
                "date_precision": "A scholarly chronology calls him a former New York attorney when he arrived for OSS work in January 1943; no firm is named",
                "city": "New York",
                "state_or_region": "New York",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "probable_immediate",
                "identity_confidence": "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "publish_qualified",
                "research_notes": "Occupation only; no employer or law firm is inferred.",
            },
            {
                "key": "samuel-van-hyning-coi-b978",
                "person_id": PEOPLE[23][0],
                "organization_key": ORG_COI,
                "organization_name_as_found": "COI",
                "role_title": "participant in preparation of COI Monograph No. 6",
                "relationship_type": "professional_affiliation",
                "start_date": "1942-03-25",
                "end_date": "1942-03-25",
                "date_precision": "Monograph date; duration and employment status not stated",
                "city": "Washington",
                "state_or_region": "District of Columbia",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "published",
                "research_notes": "Direct participation in a dated predecessor-organization report; not converted into formal employment or an explicit OSS transfer.",
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
    identity_assessment: str,
    temporal_assessment: str,
    source_quality: str,
    confidence: str,
    source_links: list[dict[str, str]],
    notes: str,
    affiliation_key: str | None = None,
    publication_status: str = "published",
) -> dict[str, object]:
    value: dict[str, object] = {
        "key": key,
        "person_id": PEOPLE[row][0],
        "claim_type": claim_type,
        "claim_text": claim_text,
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


def army_identity_note(row: int) -> str:
    return (
        f"The official Army row has the exact indexed full name {PEOPLE[row][1]} and an exact, "
        "nonshared protected-identifier agreement. The identifier and raw record ordinal remain private."
    )


def army_claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for item in ARMY_OCCUPATIONS:
        row = int(item["row"])
        name = PEOPLE[row][1]
        values.append(
            claim(
                row,
                f"identity-{slug(name)}-army-b978",
                "identity",
                f"Indexed {name} is high-confidence matched to the official Army entry used for the dated occupation finding.",
                "An exact official Army name comparison and nonshared protected identifier support the identity match.",
                army_identity_note(row),
                "The Army entry date is preserved separately from the later OSS-index context.",
                "A_direct_official",
                "high",
                [{"source_key": INDEX}, {"source_key": ARMY, "locator_override": "Accepted identity bridge; protected identifier and raw record withheld"}],
                "Protected identifiers were used only for private resolution and remain absent from the evidence bundle and public output.",
            )
        )
        values.append(
            claim(
                row,
                f"occupation-{slug(name)}-b978",
                "occupation",
                f"At Army entry on {item['date']}, {name}'s historical civilian-occupation category was {str(item['occupation']).lower()}.",
                f"The official Army field carries historical code {item['code']}; NARA's code list defines it as {item['occupation']}.",
                army_identity_note(row),
                "Dated at Army entry before the later OSS-index context; no named employer, workplace or exact OSS-transfer date is supplied.",
                "A_direct_official",
                "medium",
                [
                    {"source_key": ARMY, "locator_override": "Accepted identity bridge; protected identifier and raw record withheld"},
                    {"source_key": TECH, "locator_override": "PDF physical pages 44-46; civilian-occupation field"},
                    {"source_key": CODES, "locator_override": str(item["locator"])},
                ],
                "Published as a qualified occupation only; excluded from verified-employer analytics.",
                f"{slug(name)}-occupation-b978",
                "publish_qualified",
            )
        )
    return values


def special_claims() -> list[dict[str, object]]:
    return [
        claim(
            3,
            "identity-thomas-van-cleve-b978",
            "identity",
            "Indexed Thomas C Van Cleve is high-confidence matched to Bowdoin professor Thomas Curtis Van Cleve, a World War II Army intelligence officer.",
            "The exact first and middle names, uncommon surname, intelligence service and indexed OSS context form a coherent identity bridge.",
            "High confidence from exact name expansion, institutional career chronology and explicit World War II intelligence-officer service.",
            "The finding aid establishes Bowdoin employment before wartime service but does not specify the date of OSS accession.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": INDEX}, {"source_key": BOWDOIN}],
            "The conclusion does not rely on the shared surname alone.",
        ),
        claim(
            3,
            "last-civilian-thomas-van-cleve-bowdoin-b978",
            "last_civilian_pre_service",
            "Thomas Curtis Van Cleve taught history and political science at Bowdoin College before his World War II intelligence service.",
            "Bowdoin's finding aid dates his teaching from 1915 to 1954 and states that World War II intelligence service interrupted that career.",
            "High-confidence exact-name and intelligence-context match.",
            "Bowdoin is the last documented civilian employer before wartime service; the exact OSS transition remains unproven.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": BOWDOIN}],
            "Published as last civilian employer before wartime service, not as an explicit immediate transfer into OSS.",
            "thomas-van-cleve-bowdoin-b978",
        ),
        claim(
            7,
            "identity-ides-van-der-gracht-b978",
            "identity",
            "Indexed Ides Van Der Grac is high-confidence matched to architect and Army intelligence officer Ides van Waterschoot van der Gracht, later a leader of OSS Operation Melanie.",
            "The rare name, matching major/captain officer trajectory, Army intelligence assignment and explicit OSS operation form a strong identity bridge.",
            "High confidence from an exceptionally rare name, source-documented name expansion, military intelligence context and explicit OSS service.",
            "Sources provide a 1940 architectural practice, an April 1943 Army assignment and 1944 OSS leadership.",
            "C_reputable_contemporary_or_scholarly",
            "high",
            [{"source_key": INDEX}, {"source_key": OCTAGON}, {"source_key": CIA_IDES}],
            "The indexed spelling remains primary; the full documented spelling is retained as a variant.",
        ),
        claim(
            7,
            "immediate-ides-van-der-gracht-aaf-b978",
            "immediate_pre_oss_affiliation",
            "Ides van der Gracht was an intelligence officer with the 345th Bombardment Squadron in North Africa in April 1943, before leading an OSS mission in 1944.",
            "A contemporary AIA letter identifies the unit and role; a CIA-released report identifies his later OSS Operation Melanie leadership.",
            "High-confidence rare-name and intelligence-role match.",
            "Best-supported probable immediate military pathway; the sources do not give a formal transfer date into OSS.",
            "C_reputable_contemporary_or_scholarly",
            "high",
            [{"source_key": OCTAGON}, {"source_key": CIA_IDES}],
            "Military assignment is not labeled a civilian employer.",
            "ides-van-der-gracht-aaf-b978",
        ),
        claim(
            7,
            "last-civilian-ides-van-der-gracht-kilham-b978",
            "last_civilian_pre_service",
            "In 1940 Ides van der Gracht practiced architecture with Walter H. Kilham Jr. in New York.",
            "A contemporary Architectural Forum project credits the eponymous architectural partnership; his 1943 letter describes having entered the Air Corps from architecture.",
            "High-confidence rare-name and continuous profession match.",
            "This is the last documented civilian practice before Army Air Forces service; exact end date is not stated.",
            "C_reputable_contemporary_or_scholarly",
            "high",
            [{"source_key": ARCH_FORUM}, {"source_key": OCTAGON, "support_type": "context_only"}],
            "Classified as self-employment in an eponymous partnership rather than inventing an employee relationship.",
            "ides-van-der-gracht-kilham-b978",
        ),
        claim(
            7,
            "earlier-ides-van-der-gracht-delano-aldrich-b978",
            "other_pre_oss_affiliation",
            "Ides van der Gracht worked as an architect with Delano and Aldrich of New York on Aller Park School in 1929-1931.",
            "Historic England's official list entry attributes the dated project to him as an architect of Delano and Aldrich.",
            "High-confidence rare-name and architectural-career match.",
            "Explicitly documented prewar employment, but too early to be the immediate OSS predecessor.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": HISTORIC_ENGLAND}],
            "Preserved as earlier employment, separate from his later architectural partnership and military assignment.",
            "ides-van-der-gracht-delano-aldrich-b978",
        ),
        claim(
            9,
            "identity-paul-van-der-stricht-b978",
            "identity",
            "Indexed Paul R Van DerStricht is high-confidence matched to Paul van der Stricht, the OSS lieutenant colonel who led the Western European Section.",
            "The rare name, exact lieutenant-colonel rank and a signed OSS memorandum establish the identity.",
            "High confidence from rare name, exact rank and direct signed OSS evidence.",
            "The 1944 memorandum establishes OSS identity but not a pre-OSS employer.",
            "A_direct_official",
            "confirmed",
            [{"source_key": INDEX}, {"source_key": NARA_PAUL}],
            "The separate Paul VanDenstricht index row remains distinct and is flagged as a possible duplicate rather than merged.",
        ),
        claim(
            9,
            "occupation-paul-van-der-stricht-b978",
            "occupation",
            "Paul van der Stricht was a New York attorney before his January 1943 OSS assignment in England.",
            "A scholarly operational history calls him a former New York attorney; an Army history independently identifies him among the lawyers and officers sent to England.",
            "High-confidence rare-name, rank and direct OSS identity match.",
            "Probable immediate civilian occupation, but no law firm or exact end date is documented.",
            "C_reputable_contemporary_or_scholarly",
            "medium",
            [{"source_key": TOLEDO_PAUL}, {"source_key": DVIDS_PAUL, "support_type": "context_only"}],
            "Published as qualified occupation only; no employer or self-employment status is inferred.",
            "paul-van-der-stricht-attorney-b978",
            "publish_qualified",
        ),
        claim(
            10,
            "identity-jan-willem-van-driel-b978",
            "identity",
            "Indexed Jan W Van Driel is high-confidence matched to Jan Willem Van Driel in the British Special Operations Executive personnel files.",
            "The exact first name, middle initial expansion, surname, Dutch Army note and official SOE personnel-file context align.",
            "High confidence from multiple corroborating identifiers beyond the name: middle initial, Dutch status, military grade context and SOE file.",
            "The personnel-file catalogue entry establishes wartime identity but not pre-OSS employment.",
            "A_direct_official",
            "high",
            [{"source_key": INDEX}, {"source_key": TNA_JAN}],
            "The physical British and NARA personnel files remain necessary for employer chronology.",
        ),
        claim(
            12,
            "identity-emile-jean-elise-van-dyck-b978",
            "identity",
            "Indexed Belgian captain Emile J Van Dyck is high-confidence matched to Emile Jean Elise Van Dyck in the British Special Operations Executive personnel files.",
            "The exact first name, middle initial expansion, surname, Belgian note, commissioned rank and official SOE file context align.",
            "High confidence from several corroborating identifiers beyond the name.",
            "The personnel-file catalogue entry establishes wartime identity but not a pre-OSS employer.",
            "A_direct_official",
            "high",
            [{"source_key": INDEX}, {"source_key": TNA_EMILE}],
            "The full name is retained as a source-documented variant; employer history awaits file review.",
        ),
        claim(
            14,
            "identity-marcel-van-essen-b978",
            "identity",
            "Indexed Lieutenant Marcel Van Essen is high-confidence matched to Marcel Van Essen in the British Special Operations Executive personnel files.",
            "The uncommon exact name, commissioned rank context and official SOE personnel-file entry form a strong wartime identity bridge.",
            "High confidence from uncommon exact name plus military and special-operations context.",
            "The personnel-file catalogue entry establishes wartime identity but not a pre-OSS employer.",
            "A_direct_official",
            "high",
            [{"source_key": INDEX}, {"source_key": TNA_MARCEL}],
            "Employer chronology awaits the underlying personnel files.",
        ),
        claim(
            15,
            "identity-andrew-van-esso-b978",
            "identity",
            "Indexed Andrew E Van Esso is probably the Andrew E. Van Esso who held a postwar Central Intelligence Group personnel-management role.",
            "The rare exact name and later intelligence-organizational context support a probable match, but the postwar source does not directly mention OSS.",
            "Probable identity only: rare exact name and coherent intelligence context without a direct personnel-file or wartime bridge.",
            "Postwar evidence is used only for identity context and supplies no pre-OSS employer.",
            "A_direct_official",
            "medium",
            [{"source_key": INDEX}, {"source_key": CIA_ANDREW}],
            "Visibly qualified; excluded from default employer analytics.",
            publication_status="publish_qualified",
        ),
        claim(
            23,
            "identity-samuel-van-hyning-b978",
            "identity",
            "Indexed Samuel Van Hyning is high-confidence matched to the Samuel Van Hyning who helped prepare a Coordinator of Information monograph in March 1942.",
            "The uncommon exact name and direct predecessor-intelligence-organization context form a strong identity bridge.",
            "High confidence from rare exact name and documented participation in the OSS predecessor organization.",
            "The dated March 1942 activity predates the OSS but does not establish his exact transition date.",
            "C_reputable_contemporary_or_scholarly",
            "high",
            [{"source_key": INDEX}, {"source_key": CIA_SAMUEL}],
            "The source establishes participation, not a formal job title or employer contract.",
        ),
        claim(
            23,
            "coi-samuel-van-hyning-b978",
            "other_pre_oss_affiliation",
            "Samuel Van Hyning participated in preparing Coordinator of Information Monograph No. 6, dated March 25, 1942.",
            "A CIA historical study names him among the participants preparing the dated COI report.",
            "High-confidence rare-name and predecessor-organization identity match.",
            "Explicitly documented before OSS creation, but not proven to be a formal employment relationship or immediate transfer.",
            "C_reputable_contemporary_or_scholarly",
            "high",
            [{"source_key": CIA_SAMUEL}],
            "Classified as professional affiliation; excluded from verified-employer analytics.",
            "samuel-van-hyning-coi-b978",
        ),
    ]


def claims() -> list[dict[str, object]]:
    return army_claims() + special_claims()


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
    for row, reason in UNRESOLVED.items():
        values.append(
            base_update(
                row,
                identity_status="ambiguous" if row in {1, 4, 6, 11, 16, 17, 22} else "unresolved",
                identity_evidence=f"The visually verified index row supplies {PEOPLE[row][1]}, a box number and archive location. {reason}",
                possible_duplicate_group=WILLIAM_DUPLICATE_GROUP if row == 1 else None,
                research_status="requires_archival_review",
                next_action=f"Review the indexed personnel file for corroborating identifiers, immediate pre-OSS affiliation and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}",
                archival_review_priority="critical" if row in {1, 4, 6, 11, 16, 22} else "high",
            )
        )

    for item in ARMY_OCCUPATIONS:
        row = int(item["row"])
        values.append(
            base_update(
                row,
                identity_status="high_confidence",
                identity_evidence=army_identity_note(row),
                personnel_category="enlisted_army_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                research_status="occupation_only_found",
                next_action="Review the indexed personnel file to establish the immediate pre-OSS affiliation and named last civilian employer; do not convert the Army occupation category into a workplace.",
            )
        )

    values.extend(
        [
            base_update(
                3,
                identity_status="high_confidence",
                identity_evidence="Exact name expansion, Bowdoin career chronology and explicit World War II intelligence-officer service support the identity.",
                name_variants=["Thomas Curtis Van Cleve"],
                personnel_category="commissioned_army_officer",
                commissioned_officer=True,
                allied_or_foreign_personnel=False,
                research_status="verified_employer_found",
                next_action="Review Box 798 to establish the precise sequence among Bowdoin, Army intelligence and OSS service.",
                archival_review_priority="medium",
            ),
            base_update(
                7,
                identity_status="high_confidence",
                identity_evidence="The rare name, documented full spelling, Army intelligence assignment and explicit OSS Operation Melanie leadership support the identity.",
                name_variants=["Ides van Waterschoot van der Gracht", "Ides van der Gracht"],
                personnel_category="commissioned_army_officer",
                commissioned_officer=True,
                allied_or_foreign_personnel=False,
                research_status="verified_employer_found",
                next_action="Review Box 798 for the formal Army-to-OSS transfer date and any intervening assignment.",
                archival_review_priority="medium",
            ),
            base_update(
                9,
                identity_status="confirmed",
                identity_evidence="The rare name, exact lieutenant-colonel rank and signed 1944 OSS memorandum establish the identity.",
                name_variants=["Paul van der Stricht", "Paul Robert van der Stricht", "Paul VanDenstricht"],
                personnel_category="commissioned_army_officer",
                commissioned_officer=True,
                allied_or_foreign_personnel=False,
                possible_duplicate_group=PAUL_DUPLICATE_GROUP,
                research_status="occupation_only_found",
                next_action="Review Box 798 and the adjacent VanDenstricht file to establish whether the rows duplicate one person and to identify his law firm or employer.",
                archival_review_priority="critical",
            ),
            base_update(
                10,
                identity_status="high_confidence",
                identity_evidence="The exact first name, middle initial expansion, surname, Dutch Army note, sergeant grade context and official SOE personnel file align.",
                name_variants=["Jan Willem Van Driel"],
                personnel_category="foreign_or_allied_military_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=True,
                research_status="requires_archival_review",
                next_action="Review HS 9/1504/1 and NARA Box 799 for civilian employment before Dutch Army and special-operations service.",
                archival_review_priority="high",
            ),
            base_update(
                12,
                identity_status="high_confidence",
                identity_evidence="Exact first name, middle initial expansion, surname, Belgian note, captain rank and official SOE personnel-file context align.",
                name_variants=["Emile Jean Elise Van Dyck"],
                personnel_category="foreign_or_allied_military_personnel",
                commissioned_officer=True,
                allied_or_foreign_personnel=True,
                research_status="requires_archival_review",
                next_action="Review HS 9/1504/4 and NARA Box 799 for prewar occupation, employer and the relationship between SOE and OSS service.",
                archival_review_priority="high",
            ),
            base_update(
                14,
                identity_status="high_confidence",
                identity_evidence="The uncommon exact name, lieutenant rank context and official SOE personnel-file entry form a strong wartime identity bridge.",
                personnel_category="commissioned_army_officer",
                commissioned_officer=True,
                allied_or_foreign_personnel=None,
                research_status="requires_archival_review",
                next_action="Review HS 9/1504/6 and NARA Box 799 for nationality, prewar occupation, employer and OSS accession chronology.",
                archival_review_priority="high",
            ),
            base_update(
                15,
                identity_status="probable",
                identity_evidence="The rare exact name and postwar Central Intelligence Group personnel role support a probable match, but no direct wartime bridge was found.",
                personnel_category="unknown_or_indeterminate",
                commissioned_officer=None,
                allied_or_foreign_personnel=None,
                research_status="requires_archival_review",
                next_action="Review Box 799 for direct identity evidence and pre-OSS employment; the postwar intelligence role is not pre-OSS evidence.",
                archival_review_priority="critical",
            ),
            base_update(
                23,
                identity_status="high_confidence",
                identity_evidence="The uncommon exact name and documented participation in a March 1942 Coordinator of Information monograph support the identity.",
                personnel_category="civilian_professional_or_administrative_grade",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                research_status="requires_archival_review",
                next_action="Review Box 799 to determine whether COI participation was formal employment, identify the immediate OSS transition and recover the last civilian employer.",
                archival_review_priority="high",
            ),
            {
                "person_id": NEXT_PAUL_VAN_DENSTRICHT,
                "manual_review_required": True,
                "possible_duplicate_group": PAUL_DUPLICATE_GROUP,
            },
        ]
    )
    return values


def research_attempts() -> list[dict[str, object]]:
    reviewed = {3: 4, 5: 4, 7: 7, 9: 5, 10: 2, 12: 2, 14: 2, 15: 3, 19: 4, 23: 3}
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        positive = row in reviewed
        if positive:
            outcome = "source_reviewed"
            sources_reviewed = reviewed[row]
            rejected = 3
            detail = "Reviewed official, institutional, contemporary or scholarly evidence produced the identity, occupation, employer, military-pathway or predecessor-affiliation outcome recorded in the bundle."
        else:
            outcome = "no_result"
            sources_reviewed = 5
            rejected = 5
            detail = UNRESOLVED[row]

        attempts.append(
            {
                "key": f"page479-row{row + 23}-{slug(name)}-b978",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index and official Archives context; CIA Reading Room, British National Archives or equivalent official-source context; exact-name and meaningful variants; OSS, SOE, Army, Navy, rank and unit clues; employer and occupation 1940; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Boxes 797-800; protected identifiers used only in private official-record comparison",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_978",
                "started_at": "2026-10-30T10:00:00Z",
                "completed_at": "2026-10-30T13:30:00Z",
                "outcome": outcome,
                "sources_reviewed": sources_reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search snippets, unsourced genealogy, people-finder pages, relatives, postwar-only employment leads and sources without an OSS, protected-identifier, rank, nationality or personnel-file bridge were rejected. Historical occupation codes and military service were not silently converted into employers.",
                "research_notes": f"{detail} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain and archival searches were checked as applicable. The index page and relevant Army technical and occupation-code pages were inspected directly. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": "Review the indexed personnel file for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before wartime service.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b978-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-978-v1",
        "reviewer": "Before OSS Batch 978 evidence review",
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
