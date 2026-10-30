#!/usr/bin/env python3
"""Generate the reviewed Batch 973 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page477-robert-tyson-to-doris-ulmer-"
    "review_batch-973_2026-10-30.json"
)

INDEX = "nara-index-b973"
ARMY = "army-bulk-b973"
TECH = "army-tech-b973"
CODES = "army-codes-b973"
VA_UCCELLINI = "va-john-uccellini-b973"
NPS_UBERTI = "nps-bruno-uberti-b973"
CLEMENTE = "clemente-bruno-uberti-b973"
HARVARD_ULICH = "harvard-robert-ulich-papers-b973"
HARVARD_DEFENSE = "harvard-defense-robert-ulich-b973"
BARNES_ULLMAN = "barnes-edward-ullman-b973"
BERKELEY_ULLMAN = "berkeley-edward-ullman-b973"
NEWSCHOOL_PAUL = "newschool-paul-ullman-b973"
US_WAR_MEMORIALS = "us-war-memorials-paul-ullman-b973"
CIA_PFORZHEIMER = "cia-pforzheimer-robert-ullman-b973"
TAYLOR_ROBERT = "taylor-robert-ullman-b973"
PRINCETON_ULMER = "princeton-alfred-ulmer-b973"
CIA_ENCYCLOPEDIA = "cia-encyclopedia-alfred-ulmer-b973"

ARMY_MEDICAL = "us-army-medical-corps-b973"
HARVARD_GSE = "harvard-graduate-school-education-b973"
UCHICAGO = "university-chicago-b973"
AFS = "american-field-service-b973"
PATHE = "pathe-news-b973"
ONI = "office-naval-intelligence-b973"
BENTON_BOWLES = "benton-bowles-b973"
JACKSONVILLE_JOURNAL = "jacksonville-journal-b973"


PEOPLE = {
    1: ("ee68d2b2-2b29-57ae-b381-2afa4762953f", "Robert M Tyson"),
    2: ("bb632a58-a6c6-517a-8fa5-84e250185644", "John D Tyus"),
    3: ("e4a178e3-5b78-53a9-b5d6-384661eec6e5", "Basil Tzitzis"),
    4: ("085ff861-6de1-5f7e-817e-8b7f0edf1734", "Bruno Uberti"),
    5: ("e57fb641-762d-5337-973a-e483baec31dd", "John N Uccellini"),
    6: ("cd11446a-8c89-5d7a-9df0-1aab4f038ea3", "Edward J Uchno"),
    7: ("609741dd-dcbd-52f6-a07c-7e787ea110ff", "Louis D Udvari"),
    8: ("3fcd03ff-e331-5ef4-9204-1398a6af1584", "Charles Uehara"),
    9: ("29f4b909-e41b-526c-8445-a39db466fad9", "Philip P Ugiss"),
    10: ("50a6b801-5bcc-502f-9446-b52a9d70b963", "Joseph E Uher"),
    11: ("c89e5ba9-8b2e-5002-aecf-0f932f13f8da", "Katherine L Uhler"),
    12: ("740604f3-1388-57f3-803f-96cf7120b0c5", "Lottie Uhlfelder"),
    13: ("48260e6b-f244-57b6-be8f-5c2d8ee2c74d", "John D Ukrop"),
    14: ("51db351b-7ebb-5bb8-baef-1dbcf923876c", "Robert Ulich"),
    15: ("f82fa3bc-3391-50ca-ba0e-c1c52b1e73f0", "John Ulivelli"),
    16: ("674731e3-d0e1-5de5-bf5d-a53ed586b806", "Edward L Ullman"),
    17: ("c869743e-850c-5045-bbef-5ca46c834aa8", "Maurice S Ullman"),
    18: ("5eda059a-79a4-53cf-88a7-af55d8361f31", "Paul Ullman"),
    19: ("35fcd984-3c1b-5d81-9860-e78ae844988d", "Robert Ullman"),
    20: ("9ccd8f48-5c5e-5ca1-95d2-477a6e5e473a", "Elinor Ulman"),
    21: ("db799a3d-911d-5efb-885b-e26e9597189a", "Louis M Ulmann"),
    22: ("f097cf61-b748-5a27-af34-8021a6b6e43d", "Alfred C Ulmer"),
    23: ("f9fdff5e-bd5e-5a02-81c7-b5da3fb2f350", "Doris B Ulmer"),
}


ARMY_OCCUPATIONS = [
    {
        "row": 1,
        "date": "1945-02-17",
        "code": "097",
        "occupation": "Managers and officials, not elsewhere classified",
        "public_occupation": "manager or official, not elsewhere classified",
        "relationship_type": "unknown",
        "locator": "Historical category 0-97; managers and officials, not elsewhere classified",
    },
    {
        "row": 2,
        "date": "1943-06-14",
        "code": "232",
        "occupation": "Barbers, beauticians, and manicurists",
        "public_occupation": "barber, beautician or manicurist",
        "relationship_type": "unknown",
        "locator": "Historical category 2-32; barbers, beauticians, and manicurists",
    },
    {
        "row": 3,
        "date": "1943-04-22",
        "code": "527",
        "occupation": "Painters, construction and maintenance",
        "public_occupation": "construction or maintenance painter",
        "relationship_type": "unknown",
        "locator": "Historical category 5-27; painters, construction and maintenance",
    },
    {
        "row": 5,
        "date": "1942-11-25",
        "code": "475",
        "occupation": "Machinists",
        "public_occupation": "machinist",
        "relationship_type": "unknown",
        "locator": "Historical category 4-75; machinists",
    },
    {
        "row": 13,
        "date": "1942-11-02",
        "code": "992",
        "occupation": "Students",
        "public_occupation": "student",
        "relationship_type": "student",
        "locator": "Corrected Code No. 30, PDF physical page 304; 9-92 Students",
    },
]


UNRESOLVED = {
    7: "Searches found postwar people-directory results and other Louis Udvari namesakes, but no source bridged one to Box 793 or a dated pre-OSS affiliation.",
    8: "Exact-name, OSS, employment, obituary, institutional, newspaper and archival searches produced no defensible identity bridge.",
    9: "The printed officer-style identifier was preserved privately, but accessible sources did not connect Philip P Ugiss to an occupation, employer or OSS assignment.",
    10: "The common name produced unrelated records and no source with two corroborating identifiers beyond the name.",
    11: "Exact-name and middle-initial searches produced unrelated modern and historical namesakes without an OSS or Box 793 bridge.",
    12: "Exact-name, spelling-variant, obituary, institutional and archival searches produced no defensible identity bridge.",
    15: "A John Ulivelli born in 1920 is only an unsourced genealogical lead; the official Army file had no exact protected-identifier match and no employer evidence was found.",
    17: "Exact-name, middle-initial, OSS, occupation, obituary and archival searches produced no defensible identity bridge.",
    20: "An art-therapy namesake was rejected because no source connected her to OSS, Box 793 or the indexed spelling Elinor Ulman.",
    21: "A Louisiana Louis M. Ulmann Jr. born in 1926 and other namesakes were rejected because none had an OSS, Box 793 or wartime identity bridge.",
    23: "Alfred Ulmer's wife Doris Gibson Bridges was not adopted as the indexed Doris B Ulmer because a spousal relationship is not independent OSS identity evidence.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 792-793",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 477, rows 1-23; checked against layout-preserving text and an original-detail page render",
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
            "locator": "Official unrestricted ASNEF.FIN.DAT; seven Batch 973 identity comparisons; protected identifiers and record ordinals withheld",
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
            "locator": "PDF physical pages 171-174 and 304; Batch 973 categories visually and textually checked",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical categories identify neither employers nor workplaces and are retained only where needed for auditability.",
        },
        {
            "key": VA_UCCELLINI,
            "stable_url": "https://www.vlm.cem.va.gov/JOHNNUCCELLINI/5DBA016",
            "archival_identifier": "Long Island National Cemetery, Section V, Site 596",
            "title": "John N Uccellini Veterans Legacy Memorial",
            "author_creator": "National Cemetery Administration",
            "repository_publisher": "United States Department of Veterans Affairs",
            "publication_record_date": "Veteran dates 1922-1992",
            "locator": "Service panel: United States Army sergeant, World War II",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "Veterans Legacy Memorial",
        },
        {
            "key": NPS_UBERTI,
            "stable_url": "https://www.nps.gov/parkhistory/online_books/oss/chap8.pdf",
            "title": "OSS Training in the National Parks and Service Abroad in World War II, Chapter 8",
            "author_creator": "John Whiteclay Chambers II",
            "repository_publisher": "National Park Service",
            "publication_record_date": "2008",
            "locator": "Chapter 8, Area B training and Dr. Bruno Uberti's service in Italy",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "National Park Service history of OSS training",
        },
        {
            "key": CLEMENTE,
            "stable_url": "https://www.tandfonline.com/toc/rjih20/2/1?nav=tocList",
            "archival_identifier": "Journal of Intelligence History 2:1 (2002), pages 37-64",
            "title": "OSS Medical Intelligence in the Mediterranean Theater: A Brief History",
            "author_creator": "Jonathan D. Clemente",
            "repository_publisher": "Journal of Intelligence History; Taylor & Francis",
            "publication_record_date": "2002; online 2012-10-05",
            "locator": "Pages 47-48; Bruno Uberti chronology and Max Corvo recruitment; article footnotes cite RG 226 and Max Corvo's memoir",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Journal of Intelligence History",
            "rights_notes": "Citation metadata and a short project-authored paraphrase only; no article copy is stored.",
        },
        {
            "key": HARVARD_ULICH,
            "stable_url": "https://hollisarchives.lib.harvard.edu/catalog/hua92020",
            "archival_identifier": "Harvard University Archives HUG 4860.xx",
            "title": "Papers of Robert Ulich, 1919-1977 and undated",
            "author_creator": "Harvard University Archives",
            "repository_publisher": "Harvard Library",
            "publication_record_date": "Finding aid created 2021; updated 2023-09-26",
            "locator": "Biographical note: Harvard Graduate School of Education employment, 1935-1960",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Harvard University Archives",
        },
        {
            "key": HARVARD_DEFENSE,
            "stable_url": "https://hollisarchives.lib.harvard.edu/download_collection_pdf/hua12007.pdf",
            "archival_identifier": "Harvard University Archives HUD 3139",
            "title": "Records of American Defense, Harvard Group: an inventory",
            "author_creator": "Harvard University Archives",
            "repository_publisher": "Harvard Library",
            "publication_record_date": "Records 1940-1945; finding aid current 2026",
            "locator": "PDF page 54; Box 44 OSS Special Requests, 1943; Box 45 Robert Ulich, CVII, 1943",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "American Defense, Harvard Group records",
        },
        {
            "key": BARNES_ULLMAN,
            "stable_url": "https://blogs.ubc.ca/trevorbarnes/files/2015/01/PAPER_Geographical_Intelligence.pdf",
            "title": "Geographical intelligence: American geographers and research and analysis in the Office of Strategic Services 1941-1945",
            "author_creator": "Trevor J. Barnes",
            "repository_publisher": "Journal of Historical Geography; University of British Columbia author copy",
            "publication_record_date": "2006-01",
            "locator": "Article abstract and discussion of Edward Ullman's JANIS work for OSS Research and Analysis",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Journal of Historical Geography 32:1",
            "document_number": "doi:10.1016/j.jhg.2005.06.001",
        },
        {
            "key": BERKELEY_ULLMAN,
            "stable_url": "https://digicoll.lib.berkeley.edu/nanna/record/217627/files/versatilebotanist00consrich.pdf?registerDownload=1&version=1&withMetadata=0&withWatermark=0",
            "archival_identifier": "Regional Oral History Office interview, page 69",
            "title": "A versatile American botanist: plant taxonomy and university governance",
            "author_creator": "Lincoln Constance; interview by Suzanne B. Riess",
            "repository_publisher": "Bancroft Library, University of California, Berkeley",
            "publication_record_date": "1987",
            "locator": "Page 69; Edward Ullman completing his geography doctorate in Chicago in 1942",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Regional Oral History Office",
        },
        {
            "key": NEWSCHOOL_PAUL,
            "stable_url": "https://aspace.archives.newschool.edu/repositories/3/resources/34",
            "archival_identifier": "Eugene Paul Ullman papers, KA.0042",
            "title": "Guide to the Eugene Paul Ullman papers",
            "author_creator": "New School Archives and Special Collections staff",
            "repository_publisher": "The New School Archives and Special Collections",
            "publication_record_date": "2012-02-16; revised 2025-07-11",
            "locator": "Biographical note and Series 2; Paul Ullman's artistic work, American Field Service volunteering and OSS work",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Eugene Paul Ullman papers",
        },
        {
            "key": US_WAR_MEMORIALS,
            "stable_url": "https://www.uswarmemorials.org/html/people_details.php?PeopleID=34481",
            "title": "Paul Eugene Ullman",
            "author_creator": "U.S. War Memorials Overseas",
            "repository_publisher": "U.S. War Memorials Overseas",
            "publication_record_date": None,
            "locator": "Biographical chronology: painter-illustrator, stockbroker at OSS recruitment, civilian OSS service and 1944 death",
            "access_date": "2026-10-30",
            "source_quality": "D_correlative_or_secondary",
            "collection_name": "People honored on overseas memorials",
            "rights_notes": "The page attributes its biographical information to Find a Grave; employment claims remain visibly qualified.",
        },
        {
            "key": CIA_PFORZHEIMER,
            "stable_url": "https://www.cia.gov/resources/csi/static/interviewing-an-intelligence-icon.pdf",
            "title": "Interviewing an Intelligence Icon: A CIA Oral History of Walter Pforzheimer",
            "author_creator": "Central Intelligence Agency Center for the Study of Intelligence",
            "repository_publisher": "Central Intelligence Agency",
            "publication_record_date": "2001",
            "locator": "Page 40; Robert Ullman and Donald Downes at the early OSS-connected dinner",
            "access_date": "2026-10-30",
            "source_quality": "A_direct_official",
            "collection_name": "Studies in Intelligence",
        },
        {
            "key": TAYLOR_ROBERT,
            "stable_url": "https://dataylor1.medium.com/https-medium-com-dataylor1-back-when-the-oss-meant-business-f0863bbdf8f7",
            "title": "Back When the OSS Meant Business",
            "author_creator": "D. A. Taylor",
            "repository_publisher": "Medium",
            "publication_record_date": "2018-03-19",
            "locator": "Recruiting for Success section; Robert Ullman's Pathé News employment and work with Donald Downes",
            "access_date": "2026-10-30",
            "source_quality": "D_correlative_or_secondary",
            "rights_notes": "Used only with the official CIA oral-history identity context; the resulting claim is qualified and requires Box 793 confirmation.",
        },
        {
            "key": PRINCETON_ULMER,
            "stable_url": "https://paw.princeton.edu/memorial/alfred-conrad-ulmer-jr-39",
            "archival_identifier": "Princeton Class of 1939 memorial",
            "title": "Alfred Conrad Ulmer Jr. '39",
            "author_creator": "The Princeton Class of 1939",
            "repository_publisher": "Princeton Alumni Weekly",
            "publication_record_date": "2013-12-04",
            "locator": "Memorial chronology: U.S. Naval Intelligence in North Africa and Italy, followed by OSS in occupied Vienna",
            "access_date": "2026-10-30",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Princeton Alumni Memorials",
        },
        {
            "key": CIA_ENCYCLOPEDIA,
            "stable_url": "https://www.marco-carboni.it/wp-content/uploads/2023/11/Encyclopedia-of-the-Central-Intelligence-Agency.pdf",
            "archival_identifier": "Encyclopedia of the Central Intelligence Agency, Alfred Conrad Ulmer Jr. entry",
            "title": "Encyclopedia of the Central Intelligence Agency",
            "author_creator": "W. Thomas Smith Jr.",
            "repository_publisher": "Facts On File / Infobase Publishing; accessible reference scan",
            "publication_record_date": "2003",
            "locator": "Alfred Conrad Ulmer Jr. entry, page 231 of the printed volume",
            "access_date": "2026-10-30",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "rights_notes": "Only citation metadata and short evidence paraphrases are retained; no scan is stored or republished.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": ARMY_MEDICAL,
            "organization_id": "684d8dc3-57fe-51f0-88a2-084514015c8f",
            "canonical_name": "United States Army Medical Corps",
            "historical_name": "U.S. Army Medical Corps",
            "aliases": ["Army Medical Corps", "Medical Corps, United States Army"],
            "organization_type": "United States Army medical corps",
            "sector": "military",
            "country": "United States",
            "active_dates": "1818-present; historical Second World War name preserved",
            "normalization_notes": "Modeled as a military organization, not a civilian medical employer.",
        },
        {
            "key": HARVARD_GSE,
            "canonical_name": "Harvard Graduate School of Education",
            "historical_name": "Harvard Graduate School of Education",
            "aliases": ["Harvard University Graduate School of Education"],
            "organization_type": "university graduate school",
            "sector": "academia_and_research",
            "city": "Cambridge",
            "state_or_region": "Massachusetts",
            "country": "United States",
            "normalization_notes": "Preserved as the employing school named by Harvard rather than silently collapsed into the parent university.",
        },
        {
            "key": UCHICAGO,
            "organization_id": "f2c878b0-ee44-573d-ab30-7e4282bc85e5",
            "canonical_name": "University of Chicago",
            "historical_name": "University of Chicago",
            "aliases": ["Chicago"],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "Chicago",
            "state_or_region": "Illinois",
            "country": "United States",
            "normalization_notes": "Student status is separate from employment and excluded from employer analytics.",
        },
        {
            "key": AFS,
            "organization_id": "393fb75c-520a-5a51-91d6-0df0f0983f58",
            "canonical_name": "American Field Service",
            "historical_name": "American Field Service",
            "aliases": ["AFS", "American Field Service ambulance corps"],
            "organization_type": "volunteer ambulance service",
            "sector": "labor_nonprofit_and_religion",
            "country": "United States",
            "active_dates": "1914-present; wartime ambulance service before later educational mission",
            "normalization_notes": "Paul Ullman's relationship is recorded as volunteering, not employment.",
        },
        {
            "key": PATHE,
            "canonical_name": "Pathé News",
            "historical_name": "Pathé",
            "aliases": ["Pathé news agency", "Pathé News agency"],
            "organization_type": "newsreel and news agency",
            "sector": "journalism_and_media",
            "city": "New York",
            "state_or_region": "New York",
            "country": "United States",
            "normalization_notes": "Historical name preserved; the uncertain Robert Ullman identity is not included in default employer analytics.",
        },
        {
            "key": ONI,
            "organization_id": "f45dd890-7883-5272-9f32-4eb34218760f",
            "canonical_name": "Office of Naval Intelligence",
            "historical_name": "U.S. Naval Intelligence",
            "aliases": ["United States Naval Intelligence", "ONI"],
            "organization_type": "United States Navy intelligence organization",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "The Princeton memorial's wording is preserved; normalization to ONI reflects the historical U.S. Navy organization.",
        },
        {
            "key": BENTON_BOWLES,
            "organization_id": "fd1f6ea8-99fa-58a9-b81f-b9f9f2f47a08",
            "canonical_name": "Benton & Bowles",
            "historical_name": "Benton & Bowles",
            "aliases": ["Benton and Bowles"],
            "organization_type": "advertising agency",
            "sector": "advertising_and_public_relations",
            "city": "New York",
            "state_or_region": "New York",
            "country": "United States",
            "active_dates": "1929-1985",
            "normalization_notes": "Historical agency name retained without substituting a successor organization.",
        },
        {
            "key": JACKSONVILLE_JOURNAL,
            "canonical_name": "Jacksonville Journal",
            "historical_name": "Jacksonville Journal",
            "aliases": ["The Jacksonville Journal"],
            "organization_type": "newspaper",
            "sector": "journalism_and_media",
            "city": "Jacksonville",
            "state_or_region": "Florida",
            "country": "United States",
            "active_dates": "1887-1988",
            "normalization_notes": "Earlier documented newspaper employment, separate from Benton & Bowles and wartime service.",
        },
    ]


def occupation_affiliation(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    return {
        "key": f"{slug(PEOPLE[row][1])}-occupation-b973",
        "person_id": PEOPLE[row][0],
        "occupation": str(item["public_occupation"]),
        "relationship_type": str(item["relationship_type"]),
        "end_date": str(item["date"]),
        "date_precision": f"Historical civilian-occupation code {item['code']} was recorded at Army entry on {item['date']}; no named employer, workplace or exact OSS-transfer date is supplied.",
        "country": "United States",
        "immediate_pre_oss": False,
        "last_civilian_pre_service": False,
        "pre_oss_temporal_basis": "documented_prewar",
        "identity_confidence": "high_confidence",
        "claim_confidence": "medium",
        "source_quality": "A_direct_official",
        "publication_status": "publish_qualified",
        "research_notes": "Occupation or student status only. The historical category is not a named employer and is excluded from verified-employer analytics.",
    }


def affiliations() -> list[dict[str, object]]:
    values = [occupation_affiliation(item) for item in ARMY_OCCUPATIONS]
    values.extend(
        [
            {
                "key": "bruno-uberti-army-medical-corps-b973",
                "person_id": PEOPLE[4][0],
                "organization_key": ARMY_MEDICAL,
                "organization_name_as_found": "U.S. Army Medical Corps",
                "role_title": "medical officer",
                "occupation": "physician",
                "relationship_type": "military_assignment",
                "end_date": "1942",
                "date_precision": "By 1942 he was a Medical Corps officer stationed in Washington; Max Corvo then recruited him for OSS Italian Secret Intelligence",
                "city": "Washington",
                "state_or_region": "District of Columbia",
                "country": "United States",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "explicit_immediate",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "published",
                "research_notes": "Explicit military pathway into OSS, not a civilian employer. No pre-Army medical employer is inferred from education or profession.",
            },
            {
                "key": "robert-ulich-harvard-gse-b973",
                "person_id": PEOPLE[14][0],
                "organization_key": HARVARD_GSE,
                "organization_name_as_found": "Harvard Graduate School of Education",
                "role_title": "Professor of the History and Philosophy of Education",
                "occupation": "professor",
                "relationship_type": "employment",
                "start_date": "1935",
                "end_date": "1960",
                "date_precision": "Harvard documents continuous teaching from 1935 to 1960; a separate 1943 defense-group file names Robert Ulich beside OSS special-request material",
                "city": "Cambridge",
                "state_or_region": "Massachusetts",
                "country": "United States",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Harvard employment spans the 1943 OSS-request context. The sources do not establish whether he took leave or served concurrently.",
            },
            {
                "key": "edward-l-ullman-university-chicago-student-b973",
                "person_id": PEOPLE[16][0],
                "organization_key": UCHICAGO,
                "organization_name_as_found": "Chicago",
                "role_title": "doctoral student in geography",
                "occupation": "geographer",
                "relationship_type": "student",
                "end_date": "1942",
                "date_precision": "An institutional oral history places him completing his geography doctorate in Chicago in 1942; scholarly research places him in OSS R&A during the war",
                "city": "Chicago",
                "state_or_region": "Illinois",
                "country": "United States",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "probable_immediate",
                "identity_confidence": "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "publish_qualified",
                "research_notes": "Student status is not employment. The exact OSS accession date and any intervening role require Box 793 review.",
            },
            {
                "key": "paul-ullman-stockbroker-b973",
                "person_id": PEOPLE[18][0],
                "occupation": "stockbroker",
                "relationship_type": "unknown",
                "end_date": "1943",
                "date_precision": "A memorial biography says he was working as a stockbroker when recruited by OSS; neither firm nor exact date is supplied",
                "country": "United States",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "explicit_immediate",
                "identity_confidence": "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "D_correlative_or_secondary",
                "publication_status": "publish_qualified",
                "research_notes": "Occupation-only evidence from a secondary memorial page; no brokerage or self-employment status is invented.",
            },
            {
                "key": "paul-ullman-american-field-service-b973",
                "person_id": PEOPLE[18][0],
                "organization_key": AFS,
                "organization_name_as_found": "American Field Service's ambulance corps",
                "role_title": "ambulance corps volunteer",
                "relationship_type": "volunteer",
                "end_date": "1944",
                "date_precision": "The New School finding aid says he volunteered to return to France with AFS and engaged in confidential OSS work; exact sequence is not supplied",
                "country": "France",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "temporal_relation_uncertain",
                "identity_confidence": "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "publish_qualified",
                "research_notes": "Volunteer service is kept separate from both stockbroker occupation and OSS work.",
            },
            {
                "key": "paul-ullman-painter-illustrator-b973",
                "person_id": PEOPLE[18][0],
                "occupation": "painter and illustrator",
                "relationship_type": "unknown",
                "end_date": "1940",
                "date_precision": "The New School finding aid describes his prewar artistic career and return from France in 1940; no employing organization is named",
                "country": "France",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "publish_qualified",
                "research_notes": "Earlier documented occupation. The source does not establish employment or self-employment status, and no gallery or employer is inferred.",
            },
            {
                "key": "robert-ullman-pathe-b973",
                "person_id": PEOPLE[19][0],
                "organization_key": PATHE,
                "organization_name_as_found": "Pathé",
                "occupation": "news-agency employee",
                "relationship_type": "employment",
                "date_precision": "A secondary historical article places a Robert Ullman at Pathé while assisting Donald Downes; the official CIA oral history corroborates the Downes-Ullman OSS context but not the employer",
                "city": "New York",
                "state_or_region": "New York",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "temporal_relation_uncertain",
                "identity_confidence": "probable",
                "claim_confidence": "medium",
                "source_quality": "D_correlative_or_secondary",
                "publication_status": "publish_qualified",
                "research_notes": "Qualified identity candidate only. Box 793 must establish that the indexed Robert Ullman is this Pathé employee.",
            },
            {
                "key": "alfred-c-ulmer-naval-intelligence-b973",
                "person_id": PEOPLE[22][0],
                "organization_key": ONI,
                "organization_name_as_found": "US Naval Intelligence",
                "role_title": "naval intelligence officer",
                "relationship_type": "military_assignment",
                "end_date": "1945",
                "date_precision": "Princeton places Naval Intelligence service in North Africa and Italy before OSS Vienna; the reference biography says he was detached to OSS from Naval Intelligence",
                "country": "United States",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "explicit_immediate",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Military assignment immediately preceding OSS, not civilian employment.",
            },
            {
                "key": "alfred-c-ulmer-benton-bowles-b973",
                "person_id": PEOPLE[22][0],
                "organization_key": BENTON_BOWLES,
                "organization_name_as_found": "Benton & Bowles",
                "role_title": "public-relations staff member",
                "occupation": "advertising and public-relations executive",
                "relationship_type": "employment",
                "end_date": "1941",
                "date_precision": "The reference biography places the role after Princeton in 1939 and before U.S. Naval Reserve service after American entry into the war",
                "city": "New York",
                "state_or_region": "New York",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "strongly_date_bounded",
                "identity_confidence": "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "publish_qualified",
                "research_notes": "Best-supported last civilian employer before Navy and OSS; qualified because one accessible reference biography supplies the employer sequence.",
            },
            {
                "key": "alfred-c-ulmer-jacksonville-journal-b973",
                "person_id": PEOPLE[22][0],
                "organization_key": JACKSONVILLE_JOURNAL,
                "organization_name_as_found": "Jacksonville Journal",
                "role_title": "newspaper reporter",
                "occupation": "reporter",
                "relationship_type": "employment",
                "start_date": "1935",
                "end_date": "1937",
                "date_precision": "The reference biography gives 1935-1937, before Princeton graduation and later Benton & Bowles employment",
                "city": "Jacksonville",
                "state_or_region": "Florida",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "publish_qualified",
                "research_notes": "Earlier documented civilian employment, kept separate from Benton & Bowles and Naval Intelligence.",
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
    evidence_excerpt: str | None = None,
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
    if evidence_excerpt:
        value["evidence_excerpt"] = evidence_excerpt
    return value


def army_identity_note(row: int) -> str:
    if row == 5:
        return "The exact indexed full name and nonshared protected identifier agree with the reviewed official Army row; the VA memorial independently confirms a World War II Army sergeant of that exact name."
    return "The exact indexed full name and a nonshared protected identifier agree with the reviewed official Army row."


def army_claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row in [1, 2, 3, 5, 6, 13]:
        name = PEOPLE[row][1]
        date = next(
            (str(item["date"]) for item in ARMY_OCCUPATIONS if item["row"] == row),
            "1943-04-16",
        )
        links: list[dict[str, str]] = [
            {"source_key": INDEX},
            {"source_key": ARMY},
            {"source_key": TECH},
        ]
        if row == 5:
            links.append({"source_key": VA_UCCELLINI, "support_type": "context_only"})
        values.append(
            claim(
                row,
                f"identity-{slug(name)}-b973",
                "identity",
                f"Indexed {name} is high-confidence matched to reviewed official Army evidence.",
                army_identity_note(row),
                army_identity_note(row),
                f"The Army evidence is dated {date}; it supports identity and military-entry chronology but not the exact OSS transfer date.",
                "A_direct_official",
                "high",
                links,
                "Protected identifiers were used only for private resolution and remain absent from the evidence bundle and public output.",
            )
        )

    for item in ARMY_OCCUPATIONS:
        row = int(item["row"])
        name = PEOPLE[row][1]
        values.append(
            claim(
                row,
                f"occupation-{slug(name)}-b973",
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
                "Published as qualified occupation or student status only; excluded from verified-employer analytics.",
                f"{slug(name)}-occupation-b973",
                "publish_qualified",
            )
        )
    return values


def special_claims() -> list[dict[str, object]]:
    return [
        claim(
            4,
            "identity-bruno-uberti-b973",
            "identity",
            "Indexed Bruno Uberti is high-confidence matched to Captain Bruno Uberti, the Italian-born physician recruited into OSS Italian Secret Intelligence.",
            "The rare exact name, NPS Area B context and scholarly Army Medical Corps-to-OSS chronology identify one person.",
            "High confidence from the rare exact name plus independent official and archive-based scholarly OSS contexts.",
            "The sources place him in the Army Medical Corps by 1942 and then in OSS Italian SI.",
            "C_reputable_contemporary_or_scholarly",
            "high",
            [{"source_key": INDEX}, {"source_key": NPS_UBERTI}, {"source_key": CLEMENTE}],
            "No education, refugee history or physician title is converted into an unnamed civilian employer.",
        ),
        claim(
            4,
            "immediate-bruno-uberti-army-medical-corps-b973",
            "immediate_pre_oss_affiliation",
            "Bruno Uberti's best-supported immediate affiliation before OSS was the U.S. Army Medical Corps in Washington.",
            "Clemente states that Uberti was a Medical Corps officer in Washington by 1942 and that Max Corvo recruited him into OSS.",
            "High-confidence rare-name identity with official NPS corroboration.",
            "Explicitly immediate military pathway; exact recruitment day is not supplied.",
            "C_reputable_contemporary_or_scholarly",
            "high",
            [{"source_key": CLEMENTE, "excerpt_override": "By 1942, Uberti was an officer in the U.S. Army Medical Corps stationed in Washington."}, {"source_key": NPS_UBERTI, "support_type": "context_only"}],
            "Military assignment, not civilian employment; no pre-Army employer has been identified.",
            "bruno-uberti-army-medical-corps-b973",
            evidence_excerpt="Max Corvo, who was then organizing Italian SI, recruited him into OSS.",
        ),
        claim(
            14,
            "identity-robert-ulich-b973",
            "identity",
            "Indexed Robert Ulich is high-confidence matched to the Harvard education professor named in a 1943 American Defense, Harvard Group file beside OSS special-request material.",
            "Harvard's finding aids supply the rare exact name, continuous professorship and a 1943 OSS-request collection context.",
            "High confidence from rare exact name, matching 1943 OSS context and Harvard institutional chronology.",
            "Harvard employment ran continuously across 1943; exact OSS accession or leave status is not documented.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": INDEX}, {"source_key": HARVARD_ULICH}, {"source_key": HARVARD_DEFENSE}],
            "Box 793 should confirm the precise nature of Ulich's OSS relationship, but the employer chronology is strongly supported.",
        ),
        claim(
            14,
            "immediate-robert-ulich-harvard-b973",
            "immediate_pre_oss_affiliation",
            "Robert Ulich's best-supported immediate civilian affiliation before or at OSS entry was the Harvard Graduate School of Education.",
            "Harvard states that Ulich taught there from 1935 to 1960; a separate 1943 defense-group file places him in OSS special-request context.",
            "High-confidence rare-name institutional match.",
            "Strongly date-bounded across the 1943 OSS context; leave versus concurrent service remains unknown.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": HARVARD_ULICH, "excerpt_override": "taught at the Harvard Graduate School of Education from 1935 to 1960"}, {"source_key": HARVARD_DEFENSE}],
            "The same documented affiliation is the best-supported last civilian employer before wartime OSS work.",
            "robert-ulich-harvard-gse-b973",
            evidence_excerpt="taught at the Harvard Graduate School of Education from 1935 to 1960",
        ),
        claim(
            14,
            "last-civilian-robert-ulich-harvard-b973",
            "last_civilian_pre_service",
            "Harvard Graduate School of Education is Robert Ulich's last documented civilian employer before the indexed OSS context.",
            "Harvard's institutional chronology documents uninterrupted employment spanning the 1943 OSS-request file.",
            "High-confidence rare-name match across two Harvard finding aids and the NARA index.",
            "Strongly date-bounded; no intervening employer is documented, though concurrent service remains possible.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": HARVARD_ULICH}, {"source_key": HARVARD_DEFENSE}],
            "Employer and role are supported; the exact OSS duty status still requires file review.",
            "robert-ulich-harvard-gse-b973",
        ),
        claim(
            16,
            "identity-edward-l-ullman-b973",
            "identity",
            "Indexed Edward L Ullman is high-confidence matched to geographer Edward Louis Ullman of OSS Research and Analysis.",
            "The exact name and middle initial align with a scholarly OSS geography history and a 1942 institutional oral-history chronology.",
            "High confidence from exact middle initial, distinctive profession and direct OSS R&A evidence.",
            "The sources place doctoral completion and OSS geography work in 1942 and the wartime period.",
            "C_reputable_contemporary_or_scholarly",
            "high",
            [{"source_key": INDEX}, {"source_key": BARNES_ULLMAN}, {"source_key": BERKELEY_ULLMAN}],
            "No postwar university employer is projected backward into the pre-OSS period.",
        ),
        claim(
            16,
            "immediate-edward-l-ullman-chicago-b973",
            "immediate_pre_oss_affiliation",
            "Edward L. Ullman's best-supported immediate pre-OSS status was geography doctoral student at the University of Chicago.",
            "A Berkeley oral history places him completing his doctorate in Chicago in 1942; Barnes documents his OSS R&A geographic-intelligence work.",
            "High-confidence exact-name, middle-initial and professional match.",
            "Probably immediate in 1942, but no source explicitly states that he left the university directly for OSS.",
            "B_authoritative_institutional",
            "medium",
            [{"source_key": BERKELEY_ULLMAN, "excerpt_override": "Edward Ullman, who had been my friend at Pullman and who was completing his doctorate there in geography."}, {"source_key": BARNES_ULLMAN}],
            "Student status is not an employer and is excluded from employer analytics.",
            "edward-l-ullman-university-chicago-student-b973",
            "publish_qualified",
        ),
        claim(
            18,
            "identity-paul-eugene-ullman-b973",
            "identity",
            "Indexed Paul Ullman is high-confidence matched to Paul Eugene Ullman, the artist and American Field Service volunteer who performed confidential OSS work.",
            "The New School's family papers identify Paul Ullman, his artistic career, AFS volunteering, OSS work and 1944 death in France.",
            "High confidence from exact name, rare life chronology, institutional family papers and explicit OSS service.",
            "The chronology is wartime and ends with his 1944 mission and death.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": INDEX}, {"source_key": NEWSCHOOL_PAUL}, {"source_key": US_WAR_MEMORIALS, "support_type": "context_only"}],
            "Name variants and occupational claims remain tied to the institutional chronology; disputed details are not promoted.",
        ),
        claim(
            18,
            "immediate-paul-ullman-stockbroker-b973",
            "immediate_pre_oss_affiliation",
            "Paul Ullman's reported occupation at OSS recruitment was stockbroker; no brokerage has yet been identified.",
            "U.S. War Memorials says he was working as a stockbroker when recruited by OSS.",
            "High-confidence identity from the New School finding aid; employment detail comes from a secondary memorial page.",
            "Explicitly immediate in the secondary account, but no date or firm is supplied.",
            "D_correlative_or_secondary",
            "medium",
            [{"source_key": US_WAR_MEMORIALS, "excerpt_override": "He was working as a stockbroker when he was recruited by the OSS."}, {"source_key": NEWSCHOOL_PAUL, "support_type": "context_only"}],
            "Published as a qualified occupation-only finding; neither an employer nor self-employment is invented.",
            "paul-ullman-stockbroker-b973",
            "publish_qualified",
            "He was working as a stockbroker when he was recruited by the OSS.",
        ),
        claim(
            18,
            "other-paul-ullman-afs-b973",
            "other_pre_oss_affiliation",
            "Paul Ullman volunteered with the American Field Service ambulance corps before or alongside his confidential OSS work.",
            "The New School finding aid documents the AFS relationship and OSS work but does not state their exact sequence.",
            "High-confidence identity from institutional family papers and explicit OSS chronology.",
            "Wartime relationship with uncertain sequence; not labeled immediate and not counted as employment.",
            "B_authoritative_institutional",
            "medium",
            [{"source_key": NEWSCHOOL_PAUL, "excerpt_override": "volunteered to return to France with the American Field Service's ambulance corps"}],
            "Volunteer relationship kept distinct from his reported stockbroker occupation.",
            "paul-ullman-american-field-service-b973",
            "publish_qualified",
        ),
        claim(
            18,
            "earlier-paul-ullman-artist-b973",
            "other_pre_oss_affiliation",
            "Paul Ullman worked as a painter and illustrator before wartime service.",
            "The New School finding aid describes his long prewar artistic career in Europe and return to the United States in 1940.",
            "High-confidence identity from institutional family papers.",
            "Documented prewar occupation, not shown to be the immediate predecessor to OSS.",
            "B_authoritative_institutional",
            "medium",
            [{"source_key": NEWSCHOOL_PAUL, "excerpt_override": "Paul, an artist and illustrator who had spent much of his life in Europe"}],
            "No employing organization is named; recorded separately from AFS and stockbroker evidence.",
            "paul-ullman-painter-illustrator-b973",
            "publish_qualified",
        ),
        claim(
            19,
            "identity-robert-ullman-pathe-candidate-b973",
            "identity",
            "Indexed Robert Ullman is probably the Pathé News employee who assisted OSS recruiter Donald Downes, but Box 793 must confirm the match.",
            "A CIA oral history places Robert Ullman with Downes in early OSS context; a secondary history supplies the Pathé employment detail.",
            "Probable only: the indexed record has no middle initial or public identifier, and the official source does not name the employer.",
            "The sources describe wartime activity but do not establish whether Pathé preceded or overlapped OSS service.",
            "D_correlative_or_secondary",
            "medium",
            [{"source_key": INDEX}, {"source_key": CIA_PFORZHEIMER}, {"source_key": TAYLOR_ROBERT}],
            "The candidate remains excluded from default analytics and requires personnel-file confirmation.",
            publication_status="publish_qualified",
        ),
        claim(
            19,
            "other-robert-ullman-pathe-b973",
            "other_pre_oss_affiliation",
            "A probable Robert Ullman identity worked for Pathé News in Manhattan while assisting Donald Downes with OSS-related work.",
            "Taylor names Pathé and describes the office and recruiting work; the CIA oral history independently links Robert Ullman and Downes.",
            "Probable identity only; Box 793 is needed because the index supplies no middle initial or public service identifier.",
            "Temporal relationship to formal OSS entry is uncertain, so the employer is not labeled immediate or last civilian.",
            "D_correlative_or_secondary",
            "medium",
            [{"source_key": TAYLOR_ROBERT, "excerpt_override": "a Yale friend named Robert Ullman, who worked for the news agency Pathé in Manhattan"}, {"source_key": CIA_PFORZHEIMER, "support_type": "context_only"}],
            "Visible qualification and exclusion from default employer analytics are required until archival confirmation.",
            "robert-ullman-pathe-b973",
            "publish_qualified",
        ),
        claim(
            22,
            "identity-alfred-conrad-ulmer-b973",
            "identity",
            "Indexed Alfred C Ulmer is high-confidence matched to Alfred Conrad Ulmer Jr., Princeton '39, U.S. Naval Intelligence and OSS officer.",
            "The exact name and middle initial align with a Princeton institutional memorial and a detailed reference biography sharing Navy-to-OSS chronology.",
            "High confidence from exact middle initial and distinctive Naval Intelligence, Italy and OSS Vienna chronology.",
            "The sources place civilian employment before Navy service and Navy intelligence immediately before OSS.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": INDEX}, {"source_key": PRINCETON_ULMER}, {"source_key": CIA_ENCYCLOPEDIA}],
            "No relationship to indexed Doris B Ulmer is used as identity evidence for either record.",
        ),
        claim(
            22,
            "immediate-alfred-ulmer-naval-intelligence-b973",
            "immediate_pre_oss_affiliation",
            "Alfred C. Ulmer's best-supported immediate affiliation before OSS was U.S. Naval Intelligence.",
            "Princeton places Naval Intelligence service in North Africa and Italy before OSS Vienna; the reference biography says he was detached to OSS from Naval Intelligence.",
            "High-confidence exact-name and distinctive service-chronology match.",
            "Explicit military pathway into OSS; exact detachment date is not supplied.",
            "B_authoritative_institutional",
            "high",
            [{"source_key": PRINCETON_ULMER, "excerpt_override": "served overseas with US Naval Intelligence in North Africa and Italy, staying on in occupied Vienna with the OSS"}, {"source_key": CIA_ENCYCLOPEDIA}],
            "Military assignment, not civilian employment.",
            "alfred-c-ulmer-naval-intelligence-b973",
            evidence_excerpt="served overseas with US Naval Intelligence in North Africa and Italy, staying on in occupied Vienna with the OSS",
        ),
        claim(
            22,
            "last-civilian-alfred-ulmer-benton-bowles-b973",
            "last_civilian_pre_service",
            "Benton & Bowles is Alfred C. Ulmer's last documented civilian employer before U.S. Naval Reserve and OSS service.",
            "The reference biography places him on the agency's public-relations staff after Princeton and before joining the Naval Reserve.",
            "High-confidence identity from Princeton and the reference biography's matching full name and service chronology.",
            "Strongly date-bounded before wartime military service; exact employment dates are not supplied.",
            "C_reputable_contemporary_or_scholarly",
            "medium",
            [{"source_key": CIA_ENCYCLOPEDIA, "excerpt_override": "Following Princeton, he served on the public relations staff of Benton & Bowles"}, {"source_key": PRINCETON_ULMER, "support_type": "context_only"}],
            "Published as qualified because the accessible employer sequence rests on one reputable reference biography.",
            "alfred-c-ulmer-benton-bowles-b973",
            "publish_qualified",
        ),
        claim(
            22,
            "earlier-alfred-ulmer-jacksonville-journal-b973",
            "other_pre_oss_affiliation",
            "Alfred C. Ulmer worked as a Jacksonville Journal reporter from 1935 to 1937.",
            "The reference biography gives the newspaper, role and dates before his 1939 Princeton graduation.",
            "High-confidence identity from the matching full name and distinctive Navy-to-OSS chronology.",
            "Documented earlier prewar employment, not the last civilian role before service.",
            "C_reputable_contemporary_or_scholarly",
            "medium",
            [{"source_key": CIA_ENCYCLOPEDIA, "excerpt_override": "worked as a newspaper reporter for the Jacksonville (Florida) Journal from 1935 until 1937"}],
            "Kept separate from Benton & Bowles and wartime Naval Intelligence.",
            "alfred-c-ulmer-jacksonville-journal-b973",
            "publish_qualified",
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
    values = [
        base_update(
            row,
            identity_status="unresolved",
            identity_evidence=f"The visually verified index row supplies {PEOPLE[row][1]}, Box {'792' if row <= 3 else '793'} and archive location 230/86/42/04. {reason}",
            personnel_category="unknown_or_indeterminate",
            commissioned_officer=None,
            allied_or_foreign_personnel=None,
            research_status="requires_archival_review",
            next_action=f"Review Box {'792' if row <= 3 else '793'} for corroborating identifiers, immediate pre-OSS affiliation and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}",
        )
        for row, reason in UNRESOLVED.items()
    ]

    for row in [1, 2, 3, 5, 6, 13]:
        status = "occupation_only_found" if row != 6 else "requires_archival_review"
        values.append(
            base_update(
                row,
                identity_status="high_confidence",
                identity_evidence=army_identity_note(row),
                personnel_category="enlisted_army_personnel",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                research_status=status,
                next_action=f"Review Box {'792' if row <= 3 else '793'} to establish the immediate pre-OSS affiliation and named last civilian employer; do not convert the Army occupation category into a workplace." if row != 6 else "Review Box 793 to establish Edward J Uchno's pre-OSS occupation and employer; the official Army identity match carries undefined category 999, which is not interpreted.",
            )
        )

    values.extend(
        [
            base_update(
                4,
                identity_status="high_confidence",
                identity_evidence="The rare exact name appears in an official NPS OSS history and an archive-based scholarly study that explicitly sequences U.S. Army Medical Corps service before Max Corvo's OSS recruitment.",
                name_variants=["Dr. Bruno Uberti", "Captain Bruno Uberti", "Capt. Bruno Uberti, MC"],
                personnel_category="commissioned_army_officer",
                commissioned_officer=True,
                allied_or_foreign_personnel=False,
                research_status="occupation_only_found",
                next_action="Review Box 793 to confirm the exact Army-to-OSS transfer date and identify any civilian medical employer before Army service.",
                archival_review_priority="medium",
            ),
            base_update(
                14,
                identity_status="high_confidence",
                identity_evidence="Harvard's finding aids supply the rare exact name, continuous 1935-1960 professorship and a 1943 American Defense, Harvard Group file entry beside OSS special-request material.",
                name_variants=["Robert Ulich, 1890-1977"],
                personnel_category="unknown_or_indeterminate",
                commissioned_officer=None,
                allied_or_foreign_personnel=False,
                research_status="verified_employer_found",
                next_action="Review Box 793 to establish Ulich's precise OSS duty, accession or leave status; Harvard remains the verified best-supported civilian employer.",
                archival_review_priority="medium",
            ),
            base_update(
                16,
                identity_status="high_confidence",
                identity_evidence="The exact middle initial and distinctive geography profession align with a scholarly history of Edward Ullman's OSS R&A work and an institutional oral history placing doctoral completion in Chicago in 1942.",
                name_variants=["Edward Louis Ullman", "Edward L. Ullman"],
                personnel_category="unknown_or_indeterminate",
                commissioned_officer=None,
                allied_or_foreign_personnel=False,
                research_status="occupation_only_found",
                next_action="Review Box 793 to confirm the exact OSS accession date, any intervening affiliation and whether University of Chicago student status immediately preceded service.",
                archival_review_priority="medium",
            ),
            base_update(
                18,
                identity_status="high_confidence",
                identity_evidence="The New School's institutional family papers identify Paul Ullman, his artistic career, American Field Service volunteering, confidential OSS work and 1944 death in France.",
                name_variants=["Paul Eugene Ullman", "Paul Ullman, 1906-1944"],
                personnel_category="unknown_or_indeterminate",
                commissioned_officer=None,
                allied_or_foreign_personnel=False,
                research_status="occupation_only_found",
                next_action="Review Box 793 to identify the brokerage behind the reported stockbroker occupation and establish the exact AFS-to-OSS sequence.",
                archival_review_priority="medium",
            ),
            base_update(
                19,
                identity_status="probable",
                identity_evidence="A CIA oral history links Robert Ullman to Donald Downes in early OSS context; a secondary historical article identifies Downes's Yale friend Robert Ullman as a Pathé employee. The index has no middle initial or public identifier.",
                personnel_category="unknown_or_indeterminate",
                commissioned_officer=None,
                allied_or_foreign_personnel=None,
                research_status="requires_archival_review",
                next_action="Review Box 793 to confirm or reject the Pathé News identity candidate and determine whether that employment preceded or overlapped formal OSS service.",
                archival_review_priority="critical",
            ),
            base_update(
                22,
                identity_status="high_confidence",
                identity_evidence="The exact middle initial and distinctive Princeton, U.S. Naval Intelligence, North Africa, Italy and OSS Vienna chronology agree across institutional and scholarly reference sources.",
                name_variants=["Alfred Conrad Ulmer Jr.", "Alfred C. Ulmer Jr.", "Al Ulmer"],
                personnel_category="commissioned_naval_officer",
                commissioned_officer=True,
                allied_or_foreign_personnel=False,
                research_status="documented_prewar_employer_found",
                next_action="Review Box 793 to confirm the exact Naval Intelligence-to-OSS detachment date and seek primary employment documentation for Benton & Bowles and the Jacksonville Journal.",
                archival_review_priority="medium",
            ),
        ]
    )
    return values


def research_attempts() -> list[dict[str, object]]:
    reviewed_rows = {1, 2, 3, 4, 5, 6, 13, 14, 16, 18, 19, 22}
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        if row in reviewed_rows:
            outcome = "source_reviewed"
            reviewed = 11 if row in {4, 14, 16, 18, 22} else 7
            rejected = 5
            detail = "Reviewed official, institutional, scholarly, contemporary or archival evidence produced the identity, occupation, military-pathway, employer or qualified-candidate outcome recorded in the evidence bundle."
        else:
            outcome = "no_result"
            reviewed = 6
            rejected = 6
            detail = UNRESOLVED[row]

        special_rejection = ""
        if row == 15:
            special_rejection = " A birth-and-death-only John Ulivelli genealogy lead was rejected as unbridged; the official Army protected identifier did not match."
        elif row == 19:
            special_rejection = " The Pathé candidate remains probable because the index supplies no middle initial and the official CIA oral history does not state the employer."
        elif row == 20:
            special_rejection = " An art-therapy namesake was rejected for lack of OSS and Box 793 evidence and because the indexed surname is Ulman."
        elif row == 21:
            special_rejection = " A Louisiana namesake born in 1926 was rejected as unbridged and chronologically weak."
        elif row == 23:
            special_rejection = " Doris Gibson Bridges was not accepted merely because she was Alfred Ulmer's spouse."

        box = "792" if row <= 3 else "793"
        attempts.append(
            {
                "key": f"page477-row{row}-{slug(name)}-b973",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index and official Archives context; CIA Reading Room exact-name check; exact-name and meaningful variants; OSS, Army, Navy, rank and unit clues; employer and occupation 1940; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Box {box}; protected identifiers used only in private official-record comparison",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_973",
                "started_at": "2026-10-30T23:50:00Z",
                "completed_at": "2026-10-31T01:30:00Z",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search snippets, unsourced genealogy, people-finder pages, relatives, postwar-only employment leads and sources without an OSS, protected-identifier or personnel-file bridge were rejected. Historical occupation codes and military service were not silently converted into employers." + special_rejection,
                "research_notes": f"{detail} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain, CIA Reading Room and Library of Congress searches were checked as applicable. The index page, Army bulk file, technical documentation and relevant occupation-code pages were inspected directly; code pages 171-174 and 304 were visually checked. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": f"Review Box {box} for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before wartime service.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b973-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-973-v1",
        "reviewer": "Before OSS Batch 973 evidence review",
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
