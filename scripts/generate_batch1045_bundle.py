#!/usr/bin/env python3
"""Generate the reviewed Batch 1045 evidence bundle for PDF page 300."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page300-steve-p-mathiakes-to-leonard-j-matuszek-review_"
    "batch-1045_2026-11-05.json"
)

INDEX = "nara-index-b1045"
ARMY = "army-bulk-b1045"
TECH = "army-tech-b1045"
CODES = "army-codes-b1045"
NISEI = "army-nisei-linguists-b1045"
MATSUNAKA_CIA = "cia-matsunaka-photo-b1045"
RADIO_WARFARE = "soley-radio-warfare-b1045"
MATHIEU_MEMORIAL = "database-memoire-mathieu-b1045"
MATHIEU_PRINCETON = "princeton-veterans-mathieu-b1045"

ORG_ARMY = "org-us-army-b1045"
ORG_PRINCETON = "org-princeton-b1045"


PEOPLE = {
    1: ("95550d67-f249-54d3-86ef-524de6f4d374", "Steve P Mathiakes", "486"),
    2: ("905b8028-540f-5a94-be03-c13d3bb166ea", "Bjarne Mathieson", "491"),
    3: ("d24a41b6-f228-5667-8eba-98b8508140e9", "John T Mathieson", "491"),
    4: ("73fb81df-2e65-550f-a151-551890e4f0ae", "Arthur Mathieu", "491"),
    5: ("1cf617cf-8efe-5bf8-8d3c-800ca365c944", "Carlo-Felice Mathieu", "491"),
    6: ("1bf7c1d5-bc90-5777-9f9e-28b73f353e30", "Charles L Mathieu", "491"),
    7: ("52c37048-4382-5ddc-9860-3fe8371d6bbe", "Rene Mathieu", "491"),
    8: ("fca002e6-da76-5af0-a742-2d2beaf8550e", "Harold L Mathis", "491"),
    9: ("106f76e8-7a5f-553d-824d-8186ceffb73d", "John H Mathis", "491"),
    10: ("4737a7cb-63cd-5c54-b5fd-843f5066a49f", "Sylvia M Mathisen", "491"),
    11: ("4c38aeeb-feb5-55ca-8ef7-839f5d19b548", "Odette H Mathison", "491"),
    12: ("66401352-b31f-52b5-8d03-75b256db47fe", "Jeanette L Mathwig", "491"),
    13: ("b3d6b8a5-ab1b-5a43-bf01-6047ced68a25", "Lesley Mathwig", "491"),
    14: ("07c58ab0-139e-5391-bbb6-e1ef4436c8d4", "Edward S Matla", "491"),
    15: ("d424be94-ec64-519f-a732-9869f81effaa", "Harry Matoba", "491"),
    16: ("e0b85199-a220-588b-a074-8ba2d2e300ba", "Joseph Matovich", "491"),
    17: ("85de25f7-b9a8-5a76-9869-eca21ce6b592", "Friotjof G Matson", "491"),
    18: ("947b557f-152e-52ac-81f1-3dd2aef471e8", "William S Matsoukas", "491"),
    19: ("1f848c6c-4c6d-5de0-b97c-ae81a2b91a19", "George Matsumoto", "492"),
    20: ("4c1bc377-1904-5fea-a33b-0a74402eb3ac", "Charles Y Matsunaka", "492"),
    21: ("47043749-9334-5442-9e31-6df75488fc59", "Shigeru Matsuo", "492"),
    22: ("44df2777-a96c-595c-9c9d-16bfb5ba8245", "Andrew J Matta", "492"),
    23: ("04779f02-471a-5c54-8c76-1ef3f4003b3d", "Joseph H Mattera", "492"),
    24: ("77743719-9692-5fd9-97f5-2397b7a1727d", "John C Matthai", "492"),
    25: ("1479ff2b-1805-581f-b4fe-89665e966e61", "Viola M Matthew", "492"),
    26: ("5b6d4d0d-6087-5a10-ac03-a99d49312c15", "Dan Matthews", "492"),
    27: ("3151712d-bd8a-51df-a51a-223f4fbcaa84", "Daniel G Matthews", "492"),
    28: ("15111cbf-54d1-5638-b3d6-4926c949f60c", "Dorothy G Matthews", "492"),
    29: ("25689d5d-02b6-5777-afd0-5053e025dec6", "Eugene K Matthews", "492"),
    30: ("c91e6700-1847-531b-9b16-ea7876434623", "Eugene K Matthews", "492"),
    31: ("336445f2-7cd8-593d-8b6b-6d59a08888f9", "George B Matthews", "492"),
    32: ("5c197a78-49b5-5b8f-b217-e838d685fe9d", "Jackson Matthews", "492"),
    33: ("1c170419-84cf-54dd-a55a-5a51735e1e01", "James C Matthews", "492"),
    34: ("d86dadc0-8c4d-5518-8a69-609bc9029ae3", "James P Matthews", "492"),
    35: ("c6ffdaf7-3b7c-593c-989b-26e0e58c0f23", "Philip M Matthews", "492"),
    36: ("708c62f1-43b9-59f8-8dde-c9df2228825c", "Robert C Matthews", "492"),
    37: ("de4438e2-e7da-5c89-984b-4942be7f58f8", "William V Matthews", "492"),
    38: ("db06a736-4923-5ab9-9993-463b9e02e1c3", "Donald D Mattila", "492"),
    39: ("6e34efde-384e-504c-bd16-d1361fa6a4a8", "Earl C Mattingly", "492"),
    40: ("2fca279d-fe26-594e-a496-08e735e74f03", "Margaret Mattinson", "492"),
    41: ("45bf27e6-84a5-5e8e-8464-4db7d2379370", "Frank D Mattiola", "492"),
    42: ("b49d7f8f-1b4b-58db-89cd-5a0065b94c74", "Otto E Mattiza", "492"),
    43: ("73bab1f5-6cbd-5544-8a08-5882afea277b", "F Anna Mattox", "492"),
    44: ("60726e08-7d8b-5974-a456-05453bb7e674", "Alexander T Matus", "492"),
    45: ("6198a309-ed5b-555d-b679-4a47da4f17a9", "Edward J Matusik", "492"),
    46: ("9a8fba43-d741-5280-9895-6c322e18620f", "Leonard J Matuszek", "492"),
}


# Official AAD labels are preserved as broad historical categories. None names an
# employer, institution, workplace, or the exact affiliation immediately before OSS.
ARMY_ASSOCIATIONS = {
    8: ("1942-05-08", "316", "general farm hand", "Farm hands, general farms", "unknown", "confirmed"),
    9: ("1943-08-25", "619", "semiskilled textile-manufacturing worker, not elsewhere classified", "Semiskilled occupations in manufacture of textiles, n.e.c.", "unknown", "high_confidence"),
    13: ("1942-02-14", "105", "general office clerk", "Clerks, general office", "unknown", "high_confidence"),
    14: ("1943-06-25", "878", "unskilled machine-shop and related worker, not elsewhere classified", "Unskilled machine shop and related occupations, n.e.c.", "unknown", "confirmed"),
    16: ("1942-11-24", "992", "student", "Students", "student", "confirmed"),
    20: ("1941-03-05", "061", "radio operator", "Radio operators", "unknown", "confirmed"),
    22: ("1943-03-31", "992", "student", "Students", "student", "high_confidence"),
    23: ("1942-06-26", "339", "nursery and landscaping laborer", "Nursery and landscaping laborers", "unknown", "confirmed"),
    27: ("1942-07-22", "111", "railroad clerk, not elsewhere classified", "Railroad clerks, n.e.c.", "unknown", "confirmed"),
    37: ("1942-04-09", "048", "draftsman", "Draftsmen", "unknown", "confirmed"),
    38: ("1941-12-23", "401", "baker", "Bakers", "unknown", "confirmed"),
    39: ("1942-11-13", "581", "motor-vehicle mechanic", "Mechanics and repairmen, motor vehicle", "unknown", "confirmed"),
    41: ("1942-03-06", "002", "actor", "Actors and actresses", "unknown", "confirmed"),
    44: ("1942-10-30", "685", "semiskilled welder or flame cutter", "Semiskilled welders and flame cutters", "unknown", "confirmed"),
    46: ("1942-11-05", "703", "semiskilled aircraft-building worker, not elsewhere classified", "Semiskilled occupations in building of aircraft, n.e.c.", "unknown", "confirmed"),
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
            archival_identifier="RG 226, Entry A1-224, Boxes 486 and 491-492",
            title="OSS Personnel Files from Excel",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="2010-12-23",
            locator="PDF page 300, rows 1-46; every printed row visually checked",
            source_quality="A_direct_official",
            collection_name="Records of the Office of Strategic Services, Record Group 226",
            rights_notes="All 46 rows remain separate. The two Eugene K. Matthews rows, variant ranks, private identifiers, and original spellings remain recoverable.",
        ),
        source(
            ARMY,
            stable_url="https://catalog.archives.gov/id/1263923",
            archival_identifier="National Archives Identifier 1263923; parent series NAID 604357",
            title="Electronic Army Serial Number Merged File, ca. 1938-1946",
            author_creator="Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="1938-1946; merged file created 2002",
            locator="Official unrestricted ASNEF.FIN.DAT; 15 protected candidates explicitly reviewed and accepted",
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
            locator="Current AAD values for codes 002, 048, 061, 105, 111, 316, 339, 401, 581, 619, 685, 703, 878, and 992; printed reference copy visually checked",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records code lists",
            rights_notes="Every used value was visually checked. Categories identify neither employer, institution, workplace, nor exact Army-to-OSS sequence.",
        ),
        source(
            NISEI,
            stable_url="https://history.army.mil/portals/143/Images/Publications/catalog/70-99-1.pdf",
            archival_identifier="CMH Pub 70-99-1",
            title="Nisei Linguists: Japanese Americans in the Military Intelligence Service During World War II",
            author_creator="James C. McNaughton",
            repository_publisher="U.S. Army Center of Military History, Department of the Army",
            publication_record_date="2006",
            locator="Printed pages 285-286; Charles Y. Matsunaka's service in India and volunteer OSS Burma assignment",
            source_quality="A_direct_official",
            collection_name="U.S. Army Center of Military History publications",
            document_number="CMH Pub 70-99-1",
            rights_notes="Official Army history. It does not identify Matsunaka's precise pre-OSS unit, so only a qualified U.S. Army pathway is modeled.",
        ),
        source(
            MATSUNAKA_CIA,
            stable_url="https://www.cia.gov/resources/csi/static/d5c6fa0380917bb5c60e4297500a166f/Studies-Vol64-2-June2020.pdf",
            archival_identifier="Studies in Intelligence, Vol. 64, No. 2",
            title="Remembering Louis Austin O'Jibway: A Native American Hero in the OSS and CIA",
            author_creator="John Whiteclay Chambers II",
            repository_publisher="Central Intelligence Agency, Center for the Study of Intelligence",
            publication_record_date="2020-06",
            locator="Printed page 28, note 28; 1945 team photograph identification",
            source_quality="A_direct_official",
            collection_name="Studies in Intelligence",
            rights_notes="Used only as independent wartime identity and OSS-team context for T/4 Charles Y. Matsunaka.",
        ),
        source(
            RADIO_WARFARE,
            stable_url="https://www.worldradiohistory.com/BOOKSHELF-ARH/History/Radio-Warfare-L-Soley-1989.pdf",
            archival_identifier="ISBN 0-275-93051-3",
            title="Radio Warfare: OSS and CIA Subversive Propaganda",
            author_creator="Lawrence C. Soley",
            repository_publisher="Praeger; digital copy hosted by World Radio History",
            publication_record_date="1989",
            locator="Printed pages 177-178; OSS communications team transfer from Cairo to Kunming",
            source_quality="C_reputable_contemporary_or_scholarly",
            collection_name="Scholarly monograph",
            rights_notes="Only project-authored paraphrases and a short excerpt are retained. The book establishes wartime OSS communications work, not a pre-service employer.",
        ),
        source(
            MATHIEU_MEMORIAL,
            stable_url="https://www.database-memoire.eu/prive/en-us/rhone-us/192-rhone-m-us/8467-mathieu-arturo-c-f-2677r-oss",
            archival_identifier="MATHIEU Arturo C-F - 2677R OSS",
            title="MATHIEU Arturo C-F - 2677R OSS",
            author_creator="Database-Memoire volunteer editors",
            repository_publisher="Database-Memoire.eu",
            locator="Biographical table and Story section; pre-enlistment occupation, full name, service details, and teaching chronology",
            source_quality="D_correlative_or_secondary",
            collection_name="Rhône American Cemetery memorial biographies",
            rights_notes="The page cites ABMC, Find a Grave, and Fold3 but does not expose its underlying records. Used with visible qualification; institutions named in the narrative are not silently converted into employers.",
        ),
        source(
            MATHIEU_PRINCETON,
            stable_url="https://cst.princeton.edu/sites/g/files/toruqf6481/files/mapping_princeton_0.pdf",
            archival_identifier="Princeton University Veterans Mapping Project",
            title="Remembering Princeton Veterans",
            author_creator="Princeton University",
            repository_publisher="Princeton University",
            locator="Veterans list, Arturo Carlo-Felice Mathieu, G.S. 1940",
            source_quality="B_authoritative_institutional",
            collection_name="Princeton University veterans project",
            rights_notes="Supports graduate-student identity and status only. Princeton is not labeled an employer.",
        ),
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": ORG_ARMY,
            "organization_id": "9c84f95f-d69d-57ca-9bb9-29e960bc7a7e",
            "canonical_name": "United States Army",
            "historical_name": "U.S. Army",
            "aliases": ["Army of the United States", "U.S. Army in India"],
            "organization_type": "military service",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "The source identifies Matsunaka as an Army technician serving in India but does not name his precise unit. The record is not narrowed to SEATIC or Fourteenth Air Force without individual evidence.",
        },
        {
            "key": ORG_PRINCETON,
            "organization_id": "18f3b54c-3712-5e82-b1a7-a4d4b663f2e0",
            "canonical_name": "Princeton University",
            "historical_name": "Princeton University Graduate School",
            "aliases": ["Princeton Graduate School", "Princeton University, G.S."],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "Princeton",
            "state_or_region": "New Jersey",
            "country": "United States",
            "normalization_notes": "Modeled only as Arturo Carlo-Felice Mathieu's graduate-student affiliation. It is not counted as employment.",
        },
    ]


def army_affiliation_key(row: int) -> str:
    return f"{slug(PEOPLE[row][1])}-army-association-b1045"


def army_identity_assessment(row: int) -> str:
    if row == 9:
        return "High confidence from a nonshared protected linkage and matching name fields; the Army record's added Sr. remains a visible variant rather than a silent correction."
    if row == 13:
        return "High confidence from a nonshared protected linkage and the uncommon name; the Army record's added middle initial remains a visible variant."
    if row == 22:
        return "High confidence from a nonshared protected linkage and matching name fields; the Army record's added Jr. remains a visible variant rather than a silent correction."
    return "Confirmed by exact official name agreement and a nonshared protected linkage; the protected identifier remains private."


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, _label, relationship, identity) in ARMY_ASSOCIATIONS.items():
        item: dict[str, object] = {
            "key": army_affiliation_key(row),
            "person_id": PEOPLE[row][0],
            "relationship_type": relationship,
            "end_date": date,
            "date_precision": f"Historical civilian-occupation code {code} was recorded at Army entry on {date}; no named employer, institution, workplace, or OSS-transfer date is supplied.",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": identity,
            "claim_confidence": "medium",
            "source_quality": "A_direct_official",
            "publication_status": "publish_qualified",
            "research_notes": "The broad historical category is excluded from verified-employer analytics and is not converted into a named organization.",
        }
        if relationship == "student":
            item["role_title"] = "student"
        else:
            item["occupation"] = occupation
        values.append(item)

    values.extend(
        [
            {
                "key": "charles-y-matsunaka-us-army-india-b1045",
                "person_id": PEOPLE[20][0],
                "organization_key": ORG_ARMY,
                "organization_name_as_found": "serving in India",
                "role_title": "T/5; Army technician serving in India",
                "relationship_type": "military_assignment",
                "end_date": "1944-late",
                "date_precision": "The official Army history says that after eight months two Nisei serving in India, including T/5 Charles Y. Matsunaka, volunteered to replace OSS personnel in Burma; it does not identify his precise unit or transfer day.",
                "country": "India",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "probable_immediate",
                "identity_confidence": "confirmed",
                "claim_confidence": "high",
                "source_quality": "A_direct_official",
                "publication_status": "published",
                "research_notes": "Best-supported immediate military pathway. SEATIC and Fourteenth Air Force are discussed as recruitment pools but are not assigned to Matsunaka individually.",
            },
            {
                "key": "carlo-felice-mathieu-teacher-b1045",
                "person_id": PEOPLE[5][0],
                "role_title": "teacher of French and Spanish",
                "occupation": "language teacher",
                "relationship_type": "employment",
                "start_date": "1934",
                "end_date": "1937",
                "date_precision": "The memorial biography labels teaching French and Spanish as his pre-enlistment job and dates teaching to 1934-1937; it does not reliably identify the employing institution or establish continuity to 1943 enlistment.",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "D_correlative_or_secondary",
                "publication_status": "publish_qualified",
                "research_notes": "Published as a qualified occupation only. Swarthmore, Villanova, Princeton, and Lawrenceville are not converted into employers from the narrative's unclear sequence.",
            },
            {
                "key": "carlo-felice-mathieu-princeton-student-b1045",
                "person_id": PEOPLE[5][0],
                "organization_key": ORG_PRINCETON,
                "organization_name_as_found": "Princeton University, G.S.",
                "role_title": "graduate student",
                "relationship_type": "student",
                "end_date": "1940",
                "date_precision": "Princeton's veterans list identifies Arturo Carlo-Felice Mathieu as G.S. 1940; the exact enrollment dates and degree status are not supplied.",
                "city": "Princeton",
                "state_or_region": "New Jersey",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "publish_qualified",
                "research_notes": "Student status, not employment. The institutional record does not establish the immediate predecessor to OSS.",
            },
        ]
    )
    return values


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, label, relationship, _identity) in ARMY_ASSOCIATIONS.items():
        values.append(
            {
                "key": f"army-{slug(PEOPLE[row][1])}-b1045",
                "person_id": PEOPLE[row][0],
                "affiliation_key": army_affiliation_key(row),
                "claim_type": "other_pre_oss_affiliation" if relationship == "student" else "occupation",
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
                    {"source_key": CODES, "locator_override": f"Current AAD civilian occupation code {code}"},
                ],
            }
        )

    values.extend(
        [
            {
                "key": "identity-charles-y-matsunaka-b1045",
                "person_id": PEOPLE[20][0],
                "claim_type": "identity",
                "claim_text": "Indexed T/4 Charles Y. Matsunaka is confirmed as the Nisei Army technician who volunteered for OSS service in Burma.",
                "evidence_paraphrase": "The official Army history gives the exact name, technician grade, India setting, volunteer transition, and Burma language and radio-intercept work; CIA independently identifies him in a 1945 team photograph.",
                "identity_match_assessment": "Confirmed by the exact uncommon name and middle initial, matching technician-grade context, nonshared protected linkage, and two official wartime-history sources.",
                "temporal_assessment": "Wartime identity and Army-to-OSS pathway; the precise pre-OSS unit and transfer date are not supplied.",
                "source_quality": "A_direct_official",
                "claim_confidence": "confirmed",
                "publication_status": "published",
                "match_notes": "The index prints T-4 while the Army history prints T5g.; rank timing or source variation is preserved rather than silently harmonized.",
                "sources": [
                    {"source_key": NISEI, "excerpt_override": "T5g. Charles Y. Matsunaka were inserted into the Burmese jungle"},
                    {"source_key": MATSUNAKA_CIA, "support_type": "context_only", "excerpt_override": "Front Row: T/4 Charles Y. Matsunaka"},
                    {"source_key": INDEX, "support_type": "context_only"},
                    {"source_key": ARMY, "support_type": "context_only"},
                ],
            },
            {
                "key": "immediate-charles-y-matsunaka-us-army-b1045",
                "person_id": PEOPLE[20][0],
                "affiliation_key": "charles-y-matsunaka-us-army-india-b1045",
                "claim_type": "immediate_pre_oss_affiliation",
                "claim_text": "Charles Y. Matsunaka's best-supported immediate pre-OSS affiliation was U.S. Army service in India.",
                "evidence_paraphrase": "The Army history says Matsunaka was serving in India when he volunteered to replace OSS Nisei personnel and was inserted into Burma for language and radio-intercept work.",
                "identity_match_assessment": "Confirmed by the exact uncommon name, middle initial, technician-grade context, protected linkage, and official Army and CIA histories.",
                "temporal_assessment": "Probable immediate pathway: the narrative moves directly from Army service in India to volunteering for the OSS replacement mission, but does not name his unit or exact transfer date.",
                "source_quality": "A_direct_official",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "Modeled at Army level only; SEATIC and Fourteenth Air Force are not attributed to Matsunaka individually.",
                "sources": [
                    {"source_key": NISEI, "excerpt_override": "After eight months two other Nisei serving in India volunteered to take their places."},
                    {"source_key": MATSUNAKA_CIA, "support_type": "context_only"},
                ],
            },
            {
                "key": "identity-joseph-matovich-b1045",
                "person_id": PEOPLE[16][0],
                "claim_type": "identity",
                "claim_text": "Indexed T/3 Joseph Matovich is confirmed as an OSS communications technician transferred from Cairo to Kunming.",
                "evidence_paraphrase": "A scholarly history names Joseph Matovich in an OSS communications team that arrived in Kunming after completing work in North Africa and the Mediterranean.",
                "identity_match_assessment": "Confirmed by the exact uncommon name, nonshared protected linkage, enlisted technician context, and explicit OSS communications-team identification.",
                "temporal_assessment": "Wartime OSS assignment chronology only; it does not identify a civilian employer before Army entry.",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "claim_confidence": "high",
                "publication_status": "published",
                "match_notes": "The source documents OSS work, not an immediate pre-OSS civilian affiliation. The Army record separately supports only student status at entry.",
                "sources": [
                    {"source_key": RADIO_WARFARE, "excerpt_override": "an OSS communications team including Joseph Matovich, Richard Marshak, and others arrived in Kunming from Cairo in December"},
                    {"source_key": INDEX, "support_type": "context_only"},
                    {"source_key": ARMY, "support_type": "context_only"},
                ],
            },
            {
                "key": "identity-carlo-felice-mathieu-b1045",
                "person_id": PEOPLE[5][0],
                "claim_type": "identity",
                "claim_text": "Indexed Carlo-Felice Mathieu is strongly supported as Arturo Carlo Felice Mathieu, a prewar language teacher and Princeton graduate student who later served with OSS.",
                "evidence_paraphrase": "The memorial page supplies the expanded rare name and an officer-number form matching the protected index number; Princeton independently lists the same full name among veterans.",
                "identity_match_assessment": "High confidence from the exceptionally distinctive expanded name, matching protected officer-number digits, compatible wartime service, and independent Princeton institutional listing.",
                "temporal_assessment": "The sources document prewar teaching and graduate study before 1943 enlistment, but do not establish an immediate pre-OSS employer.",
                "source_quality": "D_correlative_or_secondary",
                "claim_confidence": "high",
                "publication_status": "publish_qualified",
                "match_notes": "The protected number is used for review but never exposed publicly. The memorial's school sequence is not treated as a sequence of employers.",
                "sources": [
                    {"source_key": MATHIEU_MEMORIAL},
                    {"source_key": MATHIEU_PRINCETON, "support_type": "context_only"},
                    {"source_key": INDEX, "support_type": "context_only"},
                ],
            },
            {
                "key": "occupation-carlo-felice-mathieu-teacher-b1045",
                "person_id": PEOPLE[5][0],
                "affiliation_key": "carlo-felice-mathieu-teacher-b1045",
                "claim_type": "occupation",
                "claim_text": "A secondary memorial biography identifies Arturo Carlo Felice Mathieu's pre-enlistment occupation as teacher of French and Spanish.",
                "evidence_paraphrase": "The biography labels language teaching as his job before enlistment and dates teaching to 1934-1937, without reliably naming the employer.",
                "identity_match_assessment": "High-confidence rare-name and protected-number match, independently supported by Princeton's full-name veterans list.",
                "temporal_assessment": "Documented prewar occupation; not shown to be the immediate role before 1943 enlistment and not assigned to a named institution.",
                "source_quality": "D_correlative_or_secondary",
                "claim_confidence": "medium",
                "publication_status": "publish_qualified",
                "match_notes": "Published with visible qualification and excluded from named-employer analytics.",
                "sources": [
                    {"source_key": MATHIEU_MEMORIAL, "excerpt_override": "JOB BEFORE ENLISTEMENT | Teacher of French and Spanish"},
                    {"source_key": MATHIEU_PRINCETON, "support_type": "context_only"},
                ],
            },
            {
                "key": "student-carlo-felice-mathieu-princeton-b1045",
                "person_id": PEOPLE[5][0],
                "affiliation_key": "carlo-felice-mathieu-princeton-student-b1045",
                "claim_type": "other_pre_oss_affiliation",
                "claim_text": "Princeton University lists Arturo Carlo-Felice Mathieu as a Graduate School veteran associated with 1940.",
                "evidence_paraphrase": "The institutional veterans list gives the exact expanded name followed by G.S. 1940.",
                "identity_match_assessment": "High confidence from the exceptionally distinctive full name and independent protected-number bridge to the index.",
                "temporal_assessment": "Documented prewar student affiliation; not employment and not established as the immediate predecessor to OSS.",
                "source_quality": "B_authoritative_institutional",
                "claim_confidence": "medium",
                "publication_status": "publish_qualified",
                "match_notes": "Princeton is modeled only as a student affiliation and excluded from employer analytics.",
                "sources": [
                    {"source_key": MATHIEU_PRINCETON, "excerpt_override": "Arturo Carlo-Felice Mathieu, G.S. 1940"},
                    {"source_key": MATHIEU_MEMORIAL, "support_type": "context_only"},
                ],
            },
            {
                "key": "identity-eugene-k-matthews-captain-b1045",
                "person_id": PEOPLE[29][0],
                "claim_type": "identity",
                "claim_text": "The indexed Captain Eugene K. Matthews remains separate from the adjacent second-lieutenant row and a spelling-variant record pending file review.",
                "evidence_paraphrase": "The index prints separate rows with different grades and protected identifiers; the captain also resembles a separately indexed Mathews spelling variant.",
                "identity_match_assessment": "Ambiguous: a shared or similar name is insufficient to merge records, and protected conflicts require review of the underlying files.",
                "temporal_assessment": "No external Army chronology or occupation is transferred pending Box 492 and related-file comparison.",
                "source_quality": "A_direct_official",
                "claim_confidence": "conflicting",
                "publication_status": "conflicting",
                "match_notes": "No private identifier is exposed. Possible duplication remains visible without silently merging source rows.",
                "sources": [{"source_key": INDEX}],
            },
            {
                "key": "identity-eugene-k-matthews-second-lieutenant-b1045",
                "person_id": PEOPLE[30][0],
                "claim_type": "identity",
                "claim_text": "The indexed Second Lieutenant Eugene K. Matthews remains separate because the protected identifier conflicts with another indexed name.",
                "evidence_paraphrase": "The private index evidence links the printed identifier to a different indexed person, so no merge or external candidate data is accepted.",
                "identity_match_assessment": "Conflicting: the common name cannot overcome a protected-identifier conflict, and the adjacent captain row has a different identifier and grade.",
                "temporal_assessment": "No Army chronology, occupation, or candidate identity is published pending review of Box 492 and the conflicting file.",
                "source_quality": "A_direct_official",
                "claim_confidence": "conflicting",
                "publication_status": "conflicting",
                "match_notes": "The conflict is reported without exposing either protected identifier or attaching another person's data.",
                "sources": [{"source_key": INDEX}],
            },
        ]
    )
    return values


def base_update(row: int) -> dict[str, object]:
    person_id, name, box = PEOPLE[row]
    return {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified page 300 source preserves {name}, Box {box}, rank or grade when printed, notes when present, and archive location. Staged official, exact-name, employment, occupation, obituary, institutional, newspaper, directory, and archival searches did not establish a defensible identity-and-affiliation bridge.",
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
        identity = ARMY_ASSOCIATIONS[row][5]
        by_row[row].update(
            identity_status=identity,
            identity_evidence=army_identity_assessment(row),
            personnel_category="enlisted_army_personnel",
            commissioned_officer=False,
            allied_or_foreign_personnel=False,
            nara_catalog_id="1263923",
            research_status="occupation_only_found",
            next_action=f"Review Box {PEOPLE[row][2]} to identify a named employer or institution and establish Army-to-OSS chronology. The protected Army link supplies only a broad historical occupation or student-status category.",
        )

    by_row[5].update(
        identity_status="high_confidence",
        identity_evidence="The exceptionally distinctive expanded name Arturo Carlo Felice Mathieu, matching protected officer-number digits, compatible OSS service, and an independent Princeton veterans listing strongly identify the indexed Carlo-Felice Mathieu.",
        name_variants=["Arturo Carlo Felice Mathieu", "Arturo Carlo-Felice Mathieu"],
        replace_name_variants=False,
        personnel_category="commissioned_army_officer",
        commissioned_officer=True,
        allied_or_foreign_personnel=False,
        research_status="occupation_only_found",
        next_action="Review Box 491 and the underlying ABMC or military record to confirm rank and identify the immediate pre-OSS affiliation and last civilian employer. Language teaching and Princeton graduate study are documented, but no institution is established as his final employer.",
        archival_review_priority="medium",
    )
    by_row[9].update(
        name_variants=["John H Mathis Sr."],
        replace_name_variants=False,
        archival_review_priority="critical",
    )
    by_row[13].update(
        name_variants=["Lesley M Mathwig"],
        replace_name_variants=False,
        archival_review_priority="critical",
    )
    by_row[16].update(
        identity_status="confirmed",
        identity_evidence="The exact uncommon name, nonshared protected linkage, T-3 technician context, and scholarly history's explicit OSS communications-team identification confirm Joseph Matovich.",
        personnel_category="enlisted_army_personnel",
        commissioned_officer=False,
        allied_or_foreign_personnel=False,
        research_status="occupation_only_found",
        next_action="Review Box 491 to identify Joseph Matovich's school or any named employer before Army entry and establish his pre-Cairo Army or OSS chronology. The Army file records only student status at entry.",
        archival_review_priority="medium",
    )
    by_row[20].update(
        identity_status="confirmed",
        identity_evidence="The exact uncommon name and middle initial, nonshared protected linkage, technician-grade context, official Army account of volunteering from India for OSS Burma service, and CIA photograph identification confirm Charles Y. Matsunaka.",
        name_variants=["Charles Y. Matsunaka", "T/4 Charles Y. Matsunaka", "T/5 Charles Y. Matsunaka"],
        replace_name_variants=False,
        personnel_category="enlisted_army_personnel",
        commissioned_officer=False,
        allied_or_foreign_personnel=False,
        research_status="occupation_only_found",
        next_action="Review Box 492 and Army personnel records to identify Matsunaka's precise unit before volunteering for OSS, his last civilian employer, and the exact rank and transfer chronology. The best-supported predecessor is qualified U.S. Army service in India.",
        archival_review_priority="medium",
    )
    by_row[22].update(
        name_variants=["Andrew J Matta Jr."],
        replace_name_variants=False,
        archival_review_priority="critical",
    )
    by_row[29].update(
        identity_status="ambiguous",
        identity_evidence="Page 300 prints a captain and a second lieutenant as separate Eugene K. Matthews rows with different protected identifiers. The captain also resembles a separately indexed Mathews spelling variant, but the source files have not been compared and no merge is accepted.",
        research_status="needs_identity_review",
        next_action="Compare the Box 492 captain file with the separately indexed Eugene K. Mathews record and the adjacent second-lieutenant file. Preserve all source rows until protected identifiers, ranks, and file contents establish whether any represent the same person.",
        archival_review_priority="critical",
    )
    by_row[30].update(
        identity_status="conflicting",
        identity_evidence="The second-lieutenant row's protected identifier conflicts with another indexed name, while the adjacent captain row has a different identifier and grade. No merge or external candidate data is accepted.",
        research_status="needs_identity_review",
        next_action="Review the Box 492 second-lieutenant file and the conflicting indexed file before assigning any identity, Army chronology, occupation, or affiliation. Keep this row separate from the captain record.",
        archival_review_priority="critical",
    )

    result = [by_row[row] for row in PEOPLE]
    if len(result) != 46:
        raise RuntimeError(f"Expected 46 person updates, generated {len(result)}")
    return result


def outcome_note(row: int) -> str:
    notes = {
        5: "A qualified secondary memorial and an independent Princeton institutional list support the expanded identity, language-teaching occupation, and graduate-student status, but not an immediate employer.",
        16: "A scholarly history establishes Matovich's wartime OSS communications identity; the protected Army record supplies only student status at entry.",
        19: "A George Matsumoto architect and a Hoover profile of Joji Matsumoto were rejected because neither source supplied a bridge to this Box 492 row.",
        20: "Official Army and CIA histories confirm Matsunaka and a probable Army-in-India pathway into OSS; the precise predecessor unit and civilian employer remain unresolved.",
        29: "The captain row remains an ambiguous possible duplicate of another indexed spelling variant; no merge was made.",
        30: "The second-lieutenant row remains conflicting because its protected identifier is associated with another indexed name; no candidate fields were transferred.",
    }
    return notes.get(row, "Unbridged namesakes, snippets, commercial people-finder pages, unsourced genealogy, relatives, and postwar-only leads did not establish a reliable identity or pre-OSS affiliation.")


def research_attempts() -> list[dict[str, object]]:
    updates = {item["person_id"]: item for item in person_updates()}
    substantiated = set(ARMY_ASSOCIATIONS) | {5}
    values: list[dict[str, object]] = []
    for row, (person_id, name, box) in PEOPLE.items():
        if row in {29, 30}:
            outcome = "candidate_rejected"
        elif row in substantiated:
            outcome = "source_reviewed"
        else:
            outcome = "no_result"
        values.append(
            {
                "key": f"page300-row{row}-{slug(name)}-b1045",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index context; exact-name and meaningful initial, suffix, punctuation, spelling and OCR variants; OSS and permitted CIA or equivalent official-source context; rank, branch, nationality, assignment and protected-identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory and archival searches; indexed Box {box}",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_1045",
                "started_at": "2026-11-05T16:05:00-05:00",
                "completed_at": "2026-11-05T18:40:00-05:00",
                "outcome": outcome,
                "sources_reviewed": 9 if row in {5, 16, 20} else 7 if row in substantiated or row in {29, 30} else 6,
                "candidate_sources_rejected": 3 if row in substantiated else 5,
                "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, education treated as employment, and postwar-only leads were rejected. Army categories were not converted into named employers. Protected conflicts and spelling variants remain visible.",
                "research_notes": f"{outcome_note(row)} The official index, exact-name OSS searches, permitted official-source context, Army and NARA materials, employment and occupation searches, and institutional, newspaper, obituary, directory, military-history, and archival sources were reviewed as applicable. Page 300 and every used Army code were visually checked. No authenticated NARA Catalog API request was made.",
                "next_action": str(updates[person_id]["next_action"]),
                "attempt_number": 1,
                "research_agent_version": "before-oss-b1045-v1",
            }
        )
    if len(values) != 46:
        raise RuntimeError(f"Expected 46 research attempts, generated {len(values)}")
    return values


def main() -> None:
    bundle = {
        "bundle_version": "batch-1045-v1",
        "reviewer": "Before OSS Batch 1045 evidence review",
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
