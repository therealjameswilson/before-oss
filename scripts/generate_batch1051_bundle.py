#!/usr/bin/env python3
"""Generate the reviewed Batch 1051 evidence bundle for PDF page 306."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page306-howard-p-mccormick-to-william-c-mccutcheon-review_"
    "batch-1051_2026-11-11.json"
)

INDEX = "nara-index-b1051"
ARMY = "army-bulk-b1051"
TECH = "army-tech-b1051"
CODES = "army-codes-b1051"
LOC_MCCOY = "loc-frank-ross-mccoy-b1051"
WASHINGTON_POST = "washington-post-thomas-mccoy-b1051"
SMITHSONIAN = "smithsonian-joseph-mccrindle-b1051"
UC_MEMORIAL = "uc-memorial-george-mccune-b1051"
MCCUNE_FOUNDATION = "mccune-foundation-marshall-b1051"

ORG_FPA = "foreign-policy-association-b1051"
ORG_ARMY = "united-states-army-b1051"
ORG_HARVARD = "harvard-university-b1051"
ORG_OCCIDENTAL = "occidental-college-b1051"
ORG_ARMY_SPECIAL_SERVICES = "army-special-services-b1051"


PEOPLE = {
    1: ("5086d94f-a417-54b8-ba0b-0f30e293fc43", "Howard P McCormick", "500"),
    2: ("cd75924a-d04d-5585-96c4-4f2d4d8f3841", "John F McCormick", "500"),
    3: ("ce1f1a7b-e464-56e3-b497-5061e75aebeb", "John I McCormick", "500"),
    4: ("d647f359-3158-50f9-bdef-260a88cf5e5c", "Lila G McCormick", "500"),
    5: ("4cbb3e26-30b0-53f0-9e1a-0e19a4af2684", "Marjorie M McCormick", "500"),
    6: ("c26ef12a-eaa3-5b80-b868-781e4866491c", "Robert W McCormick", "500"),
    7: ("29170d7f-5242-5fd5-a271-647f2a89f820", "Virgina McCoud", "500"),
    8: ("118dd0d9-52fa-5f97-9806-5ba3f0dce348", "Virgina C McCould", "499"),
    9: ("32768128-71a0-59f9-a535-9a8eca39cd10", "Benard H McCoy", "500"),
    10: ("4696b43a-af78-58b0-830a-e4bcc9c410e4", "Francis T McCoy", "500"),
    11: ("9ae63d13-d710-54ad-8223-1b7df9539013", "Frank P McCoy", "501"),
    12: ("adbb1da1-14ea-5d70-9445-9b429be33320", "Frank R McCoy", "501"),
    13: ("50f35fc0-e854-5221-ae4e-0742b47cc0ac", "George A McCoy", "501"),
    14: ("50fe03ef-69fd-51d6-8e68-5fa1a606a8e2", "James V McCoy", "501"),
    15: ("5dd734ac-994b-5ca4-b62b-c6294659106f", "Margaret E McCoy", "501"),
    16: ("98efde88-d3cb-59fd-8682-c611443b12d5", "Priscilla L McCoy", "501"),
    17: ("4a702359-1c88-5f8b-9086-fe0532896069", "Ruth M McCoy", "501"),
    18: ("14fd8141-1e60-5dc7-8822-fb74feedfc23", "Thomas F McCoy", "501"),
    19: ("6eed87e4-103e-554e-8386-328b3844cb48", "Thomas M McCoy", "501"),
    20: ("7cc8269b-4f1b-5de6-b103-6ad33435966b", "Wade W McCoy", "501"),
    21: ("d8350c53-c8c2-58dc-a145-bcc543ac508c", "Wilber D McCoy", "501"),
    22: ("4ee3c4a3-b18c-55e5-a6ae-6605402b86de", "William J McCoy", "501"),
    23: ("4917ebd7-ee43-5e3a-9461-7415c965375d", "Charles McCracken Jr.", "501"),
    24: ("615d5039-2e2c-50fa-b8d4-9e772f537dc6", "Ivna W McCrary", "501"),
    25: ("4960f431-455c-5d03-a23d-90159edbc153", "Jack L McCrary", "501"),
    26: ("72d1dd8d-db1f-5147-8789-333c85d5e2f8", "Ruth M McCrary", "501"),
    27: ("af0435c1-a04e-533d-9289-1ee6cdf53e12", "Ivan W McCray", "501"),
    28: ("b9edcade-258b-53c5-99e9-762d1027d630", "Jane N/M McCray", "501"),
    29: ("f2f7ce7e-7889-5ccb-8ab9-d15249a99646", "Willis E McCray", "501"),
    30: ("885df8a2-155f-5c30-a3ab-420f739a67df", "Melvin L McCrea", "501"),
    31: ("dcdfe506-9da3-5c6c-a6c9-a3390f77923c", "Samuel H McCrea", "501"),
    32: ("5c8d3d2a-bf5e-5c0a-bbf5-cad9ad10f2c2", "Julia F McCrimmon", "501"),
    33: ("4c8522f4-9712-584a-924e-ba55ee072e88", "Joseph F McCrindle", "501"),
    34: ("9c68dd21-4877-5709-b14a-e757abb377f9", "Joseph F McCrindle", "501"),
    35: ("32fa7614-3e98-5869-b8ab-fadd5dfb3c2b", "Kenneth A McCrum", "501"),
    36: ("5b2e97be-a6ac-585c-8051-c4b3a1524dd2", "John I McCulloch", "501"),
    37: ("4fdbe340-445c-57cd-b750-4343e0bccc59", "George B McCullough", "501"),
    38: ("b6fa8688-ffba-5d7d-b519-6cafd1b32633", "James J McCullough", "501"),
    39: ("08656ac8-1885-55d6-bcf8-2f2c2fefe8b8", "James L McCullough", "501"),
    40: ("b829d19d-21ec-5782-9a3a-6d8021c2e3a9", "Wilton E McCullough", "501"),
    41: ("c69ef820-17f0-5460-83df-d717087725f5", "George M McCune", "501"),
    42: ("b035428e-2bc2-5a6c-b645-7e5671b55de0", "Marshall L McCune", "501"),
    43: ("5f937b58-0d9e-50fc-a489-4b16b8006575", "Richard W McCune", "501"),
    44: ("e94dbad1-4b8b-5711-9848-15f87646bac8", "Wallace H McCune", "502"),
    45: ("b9e3c574-7309-55a8-9474-e87b683a784d", "Alexander F McCurdy", "502"),
    46: ("0d0bd61d-c89e-5141-b5bd-623cb4977c3d", "William C McCutcheon", "502"),
}


# Only nonshared, wartime-dated Army links with useful codes become qualified
# occupation evidence. Codes 999 are indeterminate, while the 1946 entries are
# postwar-dated and therefore withheld from pre-OSS publication.
ARMY_OCCUPATIONS = {
    1: ("1942-09-16", "118", "general industry clerk", "General industry clerks", "PDF physical page 171; historical code 1-18"),
    2: ("1942-09-03", "684", "semiskilled structural or ornamental metal worker", "Semiskilled occupations in structural and ornamental metal work", "PDF physical page 174; historical code 6-84"),
    33: ("1943-05-25", "992", "student", "Students", "PDF physical page 304; corrected historical code 9-92"),
    38: ("1943-03-26", "685", "semiskilled welder or flame cutter", "Semiskilled welders and flame cutters", "PDF physical page 174; historical code 6-85"),
    45: ("1944-06-22", "475", "machinist", "Machinists", "PDF physical page 173; historical code 4-75"),
}

ARMY_IDENTITY_ROWS = {30, 31, 33, 38, 40, 45}
POSTWAR_ARMY_ROWS = {23, 40}
SHARED_OR_DUPLICATE_ROWS = {7, 8, 24, 25, 27, 33, 34}
DUPLICATE_GROUPS = {
    7: "p306-virgina-mccoud-mccould-b623",
    8: "p306-virgina-mccoud-mccould-b623",
    24: "p306-ivna-mccrary-ivan-mccray-b623",
    25: "p304-306-jack-mccarary-mccrary-b623",
    27: "p306-ivna-mccrary-ivan-mccray-b623",
    33: "p306-joseph-f-mccrindle-distinct-identifiers-b623",
    34: "p306-joseph-f-mccrindle-distinct-identifiers-b623",
}

ATTEMPT_NUMBERS = {
    1: 3, 2: 3, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 2, 9: 3,
    10: 2, 11: 2, 12: 3, 13: 2, 14: 2, 15: 2, 16: 2, 17: 2,
    18: 2, 19: 2, 20: 2, 21: 2, 22: 3, 23: 3, 24: 1, 25: 1,
    26: 1, 27: 1, 28: 1, 29: 1, 30: 1, 31: 1, 32: 1, 33: 1,
    34: 1, 35: 1, 36: 1, 37: 1, 38: 1, 39: 1, 40: 1, 41: 1,
    42: 1, 43: 1, 44: 1, 45: 2, 46: 1,
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def source(key: str, **kwargs: object) -> dict[str, object]:
    value: dict[str, object] = {"key": key, "access_date": "2026-11-11"}
    value.update(kwargs)
    return value


def sources() -> list[dict[str, object]]:
    return [
        source(
            INDEX,
            stable_url="https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            archival_identifier="RG 226, Entry A1-224, Boxes 499-502",
            title="OSS Personnel Files from Excel",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="2010-12-23",
            locator="PDF page 306, rows 1-46; every printed row visually checked",
            source_quality="A_direct_official",
            collection_name="Records of the Office of Strategic Services, Record Group 226",
            rights_notes="All 46 printed rows remain separate. Full protected identifiers remain private.",
        ),
        source(
            ARMY,
            stable_url="https://catalog.archives.gov/id/1263923",
            archival_identifier="National Archives Identifier 1263923; parent series NAID 604357",
            title="Electronic Army Serial Number Merged File, ca. 1938-1946",
            author_creator="Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="1938-1946; merged file created 2002",
            locator="Official unrestricted ASNEF.FIN.DAT; reviewed row-specific private identity crosswalks",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records",
            document_number="ASNEF.FIN.DAT",
            rights_notes="No raw record, protected identifier, or bulk ordinal is retained in public assets. Shared or conflicting links are withheld.",
        ),
        source(
            TECH,
            stable_url="https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf",
            archival_identifier="NN3-064-03-008; National Archives Identifier 1263923",
            title="World War II Army Enlistment Records: Reference Copy of Technical Documentation",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives at College Park - Electronic Records",
            publication_record_date="1994-2005; reference copy modified 2011",
            locator="PDF physical pages 44-46; Army-entry date, grade, and civilian-occupation fields",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records technical documentation",
            rights_notes="Used only to interpret selected fields; the bulk file does not identify a named employer or prove the Army-to-OSS sequence.",
        ),
        source(
            CODES,
            stable_url="https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf",
            archival_identifier="Code No. 30 in NAID 1263923 technical documentation",
            title="World War II Army Enlistment Records: Civilian Occupation Code Lists",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives at College Park - Electronic Records",
            locator="PDF physical pages 171, 173-174, and amended page 304; printed code lists visually checked",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records code lists",
            rights_notes="The codes supply broad dated categories, not employers, workplaces, institutions, or OSS chronology.",
        ),
        source(
            LOC_MCCOY,
            stable_url="https://findingaids.loc.gov/repositories/19/resources/5729",
            archival_identifier="Frank Ross McCoy Papers, Library of Congress Manuscript Division",
            title="Frank Ross McCoy Papers",
            author_creator="Frank Ross McCoy",
            repository_publisher="Library of Congress Manuscript Division",
            publication_record_date="1862-1957; finding aid current at access",
            locator="Biographical Note; entries for 1938-1945",
            source_quality="B_authoritative_institutional",
            collection_name="Frank Ross McCoy Papers",
            rights_notes="The finding aid supplies an institutional chronology; it does not establish why McCoy appears in the OSS personnel index.",
        ),
        source(
            WASHINGTON_POST,
            stable_url="https://www.washingtonpost.com/archive/local/2009/12/06/obituaries/6c638098-7ddf-4d38-97ec-2e7b98641abc/",
            title="Obituaries: Thomas F. McCoy",
            author_creator="Matt Schudel",
            repository_publisher="The Washington Post",
            publication_record_date="2009-12-06",
            locator="Thomas F. McCoy obituary",
            source_quality="C_reputable_contemporary_or_scholarly",
            collection_name="Obituaries",
            rights_notes="Only a short supporting excerpt and project-authored paraphrase are retained.",
        ),
        source(
            SMITHSONIAN,
            stable_url="https://www.aaa.si.edu/collections/joseph-f-mccrindle-papers-16085/biographical-note",
            archival_identifier="Joseph F. McCrindle papers, 1877-2013",
            title="Biographical Note | Joseph F. McCrindle papers, 1877-2013",
            repository_publisher="Archives of American Art, Smithsonian Institution",
            locator="Biographical note",
            source_quality="B_authoritative_institutional",
            collection_name="Joseph F. McCrindle papers",
            rights_notes="The note supports only the lieutenant row; the separate corporal row has a different private identifier and remains distinct.",
        ),
        source(
            UC_MEMORIAL,
            stable_url="https://digicoll.lib.berkeley.edu/nanna/record/81372/files/inmemoriam1948.pdf?registerDownload=1&version=1&withMetadata=0&withWatermark=0",
            archival_identifier="University of California In Memoriam, 1948",
            title="In Memoriam, 1948",
            author_creator="University of California Academic Senate",
            repository_publisher="University of California",
            publication_record_date="1948",
            locator="PDF physical page 19; George McAfee McCune memorial, internal pages 2-3",
            source_quality="B_authoritative_institutional",
            collection_name="University of California In Memoriam",
            rights_notes="The university memorial explicitly sequences Occidental College employment and leave for OSS work.",
        ),
        source(
            MCCUNE_FOUNDATION,
            stable_url="https://nmmccune.org/who-we-are/",
            title="Who We Are",
            repository_publisher="Marshall L. and Perrine D. McCune Charitable Foundation",
            locator="Legacy section",
            source_quality="B_authoritative_institutional",
            collection_name="McCune Foundation history",
            rights_notes="The institutional biography supports identity and a wartime Army Special Services assignment, but not its exact sequence relative to OSS.",
        ),
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": ORG_FPA,
            "organization_id": "a454df0d-8adb-50ba-81cf-b4da2bbfae73",
            "canonical_name": "Foreign Policy Association",
            "historical_name": "Foreign Policy Association",
            "aliases": [],
            "organization_type": "nonprofit civic organization",
            "sector": "labor_nonprofit_and_religion",
            "city": "New York",
            "state_or_region": "New York",
            "country": "United States",
            "normalization_notes": "Existing canonical organization reused. McCoy's presidency is modeled as a professional affiliation because the finding aid does not establish paid employment.",
        },
        {
            "key": ORG_ARMY,
            "organization_id": "28a26f92-78af-5a1a-9c09-a843eb5975b4",
            "canonical_name": "United States Army",
            "historical_name": "U.S. Army",
            "aliases": ["Army"],
            "organization_type": "military service",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "Existing canonical organization reused. A military assignment is never labeled civilian employment.",
        },
        {
            "key": ORG_HARVARD,
            "organization_id": "45ddf347-21c6-59f5-a8ae-517418adf941",
            "canonical_name": "Harvard University",
            "historical_name": "Harvard University",
            "aliases": ["Harvard"],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "Cambridge",
            "state_or_region": "Massachusetts",
            "country": "United States",
            "normalization_notes": "McCrindle's attendance is a student relationship, not employment.",
        },
        {
            "key": ORG_OCCIDENTAL,
            "canonical_name": "Occidental College",
            "historical_name": "Occidental College",
            "aliases": ["Occidental"],
            "organization_type": "college",
            "sector": "academia_and_research",
            "city": "Los Angeles",
            "state_or_region": "California",
            "country": "United States",
            "normalization_notes": "Historical college name retained. The memorial identifies employment on the history staff and leave for OSS work.",
        },
        {
            "key": ORG_ARMY_SPECIAL_SERVICES,
            "canonical_name": "U.S. Army Special Services",
            "historical_name": "Special Services",
            "aliases": ["Army Special Services"],
            "organization_type": "military program",
            "sector": "military",
            "country": "United States",
            "active_dates": "World War II",
            "normalization_notes": "The historical program is retained separately from the parent Army so the source wording and assignment remain visible.",
        },
    ]


def army_affiliation_key(row: int) -> str:
    return f"{slug(PEOPLE[row][1])}-army-entry-occupation-b1051"


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation, _label, _locator) in ARMY_OCCUPATIONS.items():
        values.append(
            {
                "key": army_affiliation_key(row),
                "person_id": PEOPLE[row][0],
                "occupation": occupation,
                "relationship_type": "student" if code == "992" else "unknown",
                "end_date": date,
                "date_precision": f"Historical civilian-occupation code {code} was recorded at Army entry on {date}; no named employer, institution, workplace, or OSS-transfer date is supplied.",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "temporal_relation_uncertain",
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
                "key": "frank-ross-mccoy-fpa-b1051",
                "person_id": PEOPLE[12][0],
                "organization_key": ORG_FPA,
                "organization_name_as_found": "Foreign Policy Association",
                "role_title": "president",
                "relationship_type": "professional_affiliation",
                "start_date": "1939",
                "end_date": "1945",
                "date_precision": "The Library of Congress finding aid dates the presidency to 1939-1945; it does not state whether this role explains the OSS index entry.",
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
                "research_notes": "Documented prewar and wartime professional affiliation; not presented as an employer or immediate OSS predecessor.",
            },
            {
                "key": "thomas-f-mccoy-army-b1051",
                "person_id": PEOPLE[18][0],
                "organization_key": ORG_ARMY,
                "organization_name_as_found": "Army",
                "role_title": "Army officer",
                "relationship_type": "military_assignment",
                "date_precision": "The obituary states that McCoy served in the Army during World War II and was selected for OSS; no exact transfer date or unit is printed.",
                "country": "United States",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "explicit_immediate",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "C_reputable_contemporary_or_scholarly",
                "publication_status": "published",
                "research_notes": "The military pathway is distinct from an unidentified last civilian employer.",
            },
            {
                "key": "joseph-feder-mccrindle-harvard-b1051",
                "person_id": PEOPLE[34][0],
                "organization_key": ORG_HARVARD,
                "organization_name_as_found": "Harvard",
                "relationship_type": "student",
                "end_date": "1944",
                "date_precision": "The Smithsonian note says McCrindle graduated from Harvard in 1944; it does not establish the exact sequence relative to his OSS service.",
                "city": "Cambridge",
                "state_or_region": "Massachusetts",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "temporal_relation_uncertain",
                "identity_confidence": "confirmed",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "publish_qualified",
                "research_notes": "Student status is not an employer claim. This evidence belongs only to the lieutenant row, not the distinct corporal row.",
            },
            {
                "key": "george-mcafee-mccune-occidental-b1051",
                "person_id": PEOPLE[41][0],
                "organization_key": ORG_OCCIDENTAL,
                "organization_name_as_found": "Occidental College",
                "role_title": "history instructor and associate professor",
                "occupation": "historian and college teacher",
                "relationship_type": "employment",
                "start_date": "1939",
                "end_date": "1942",
                "date_precision": "The 1948 university memorial says McCune served on Occidental's history staff from 1939 and received leave in 1942 to work for OSS; his staff affiliation formally continued to 1946.",
                "city": "Los Angeles",
                "state_or_region": "California",
                "country": "United States",
                "immediate_pre_oss": True,
                "last_civilian_pre_service": True,
                "pre_oss_temporal_basis": "explicit_immediate",
                "identity_confidence": "confirmed",
                "claim_confidence": "confirmed",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "The memorial explicitly sequences leave from Occidental for OSS work. The 1942 transition is used while the continuing leave-status relationship through 1946 is preserved in the date note.",
            },
            {
                "key": "marshall-lockhart-mccune-army-special-services-b1051",
                "person_id": PEOPLE[42][0],
                "organization_key": ORG_ARMY_SPECIAL_SERVICES,
                "organization_name_as_found": "Special Services",
                "role_title": "Special Services Officer",
                "relationship_type": "military_assignment",
                "start_date": "1941",
                "end_date": "1946",
                "date_precision": "The foundation biography places his volunteer Army service and Far East Special Services assignment during World War II and gives a 1946 discharge; exact assignment dates and OSS sequence are unstated.",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "temporal_relation_uncertain",
                "identity_confidence": "high_confidence",
                "claim_confidence": "medium",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "publish_qualified",
                "research_notes": "Documented wartime military assignment; not labeled the immediate OSS predecessor without a direct chronology.",
            },
        ]
    )
    return values


def claim(
    key: str,
    row: int,
    claim_type: str,
    claim_text: str,
    evidence_paraphrase: str,
    identity_match_assessment: str,
    temporal_assessment: str,
    source_quality: str,
    claim_confidence: str,
    publication_status: str,
    match_notes: str,
    source_links: list[dict[str, str]],
    affiliation_key: str | None = None,
) -> dict[str, object]:
    value: dict[str, object] = {
        "key": key,
        "person_id": PEOPLE[row][0],
        "claim_type": claim_type,
        "claim_text": claim_text,
        "evidence_paraphrase": evidence_paraphrase,
        "identity_match_assessment": identity_match_assessment,
        "temporal_assessment": temporal_assessment,
        "source_quality": source_quality,
        "claim_confidence": claim_confidence,
        "publication_status": publication_status,
        "match_notes": match_notes,
        "sources": source_links,
    }
    if affiliation_key:
        value["affiliation_key"] = affiliation_key
    return value


def identity_claims() -> list[dict[str, object]]:
    values = [
        claim(
            "identity-frank-ross-mccoy-b1051", 12, "identity",
            "Indexed Major General Frank R. McCoy is Frank Ross McCoy, whose papers are described by the Library of Congress.",
            "The finding aid supplies the full middle name and an exceptional major-general chronology matching the indexed name and rank.",
            "High confidence from exact name and initial, exceptional rank, and a continuous authoritative military chronology.",
            "The finding aid documents prewar and wartime roles but not why the personnel index includes McCoy.",
            "B_authoritative_institutional", "high", "published",
            "The stronger institutional bridge supplements an earlier probable identity review without inferring OSS duties.",
            [{"source_key": LOC_MCCOY}, {"source_key": INDEX, "support_type": "context_only"}],
        ),
        claim(
            "identity-thomas-frederick-mccoy-b1051", 18, "identity",
            "Indexed Major Thomas F. McCoy is Thomas Frederick McCoy, the Army officer selected for OSS service in London.",
            "The obituary gives the full middle name, World War II Army service, selection for OSS, London duty, and a compatible officer chronology.",
            "High confidence from exact name and initial, compatible major rank, and explicit Army-to-OSS service.",
            "The source explicitly places Army service before OSS selection.",
            "C_reputable_contemporary_or_scholarly", "high", "published",
            "The full middle name is retained as a sourced variant; no civilian employer is inferred.",
            [{"source_key": WASHINGTON_POST}, {"source_key": INDEX, "support_type": "context_only"}],
        ),
        claim(
            "identity-joseph-feder-mccrindle-b1051", 34, "identity",
            "The indexed Lieutenant Joseph F. McCrindle is Joseph Feder McCrindle, the Harvard graduate who served with OSS in London and attained first lieutenant.",
            "The Smithsonian note supplies the full middle name, explicit London OSS service, and the exact first-lieutenant rank.",
            "Confirmed for the lieutenant row by the rare exact name, matching rank, and explicit OSS service. The distinct corporal row is excluded.",
            "The student and wartime chronology is documented, although the exact Harvard-to-OSS transition is unstated.",
            "B_authoritative_institutional", "confirmed", "published",
            "Different private identifiers keep the corporal and lieutenant rows separate; this biography is not transferred to the corporal.",
            [{"source_key": SMITHSONIAN}, {"source_key": INDEX, "support_type": "context_only"}],
        ),
        claim(
            "identity-george-mcafee-mccune-b1051", 41, "identity",
            "Indexed George M. McCune is George McAfee McCune, the Occidental historian placed on leave to work for OSS in 1942.",
            "The university memorial supplies the full middle name, exact OSS transition, occupation, and a continuous wartime chronology.",
            "Confirmed by exact name and initial plus a direct institutional statement of OSS service.",
            "The memorial explicitly dates the move from Occidental employment to OSS work in 1942.",
            "B_authoritative_institutional", "confirmed", "published",
            "The full middle name is retained as a sourced variant.",
            [{"source_key": UC_MEMORIAL}, {"source_key": INDEX, "support_type": "context_only"}],
        ),
        claim(
            "identity-marshall-lockhart-mccune-b1051", 42, "identity",
            "Indexed Lieutenant Marshall L. McCune is Marshall Lockhart McCune, the wartime Army Special Services officer described by his family foundation.",
            "The institutional biography supplies the rare full name, compatible Army officer service, Far East assignment, and 1946 discharge.",
            "High confidence from a rare exact name, matching initial, compatible lieutenant rank, and detailed wartime Army chronology.",
            "The biography documents wartime service but does not state the exact relation between Special Services and OSS.",
            "B_authoritative_institutional", "high", "published",
            "The identity is strong, but the assignment remains temporally qualified.",
            [{"source_key": MCCUNE_FOUNDATION}, {"source_key": INDEX, "support_type": "context_only"}],
        ),
    ]

    for row, variant, extra in (
        (30, None, "The code 999 occupation field is indeterminate and is not published."),
        (31, "Samuel H McCrea Jr.", "The Army suffix is retained as a sourced name variant; code 999 is not published."),
        (33, None, "The unique link belongs to the corporal row only; the separate lieutenant row remains distinct."),
        (38, None, "The link supports a qualified Army-entry occupation category."),
        (40, None, "The Army entry is dated 28 June 1946, so its occupation is withheld as postwar-dated."),
        (45, None, "The link supports a qualified Army-entry occupation category."),
    ):
        variant_text = f" The official record supplies the variant {variant}." if variant else ""
        values.append(
            claim(
                f"identity-{slug(PEOPLE[row][1])}-army-b1051", row, "identity",
                f"The indexed {PEOPLE[row][1]} row has a high-confidence identity link to an official Army enlistment record.",
                "The official index name and the Army entry agree after fixed-width spacing is normalized, and the private identifier is nonshared for this row.",
                "High confidence from matching official name evidence and a reviewed, nonshared private identifier link; the identifier remains private." + variant_text,
                "The Army-entry date supports identity, not by itself the chronology of OSS service.",
                "A_direct_official", "high", "published",
                extra,
                [{"source_key": ARMY}, {"source_key": INDEX, "support_type": "context_only"}],
            )
        )
    return values


def claims() -> list[dict[str, object]]:
    values = identity_claims()
    for row, (date, code, occupation, label, locator) in ARMY_OCCUPATIONS.items():
        values.append(
            claim(
                f"army-entry-{slug(PEOPLE[row][1])}-b1051", row, "occupation",
                f"At Army entry on {date}, {PEOPLE[row][1]} was recorded as {occupation}; no employer, institution, or workplace is identified.",
                f"The official Army bulk file records code {code}; the visually checked official list defines the category as {label}.",
                "High confidence from matching official name evidence and a reviewed, nonshared private identifier linkage; the identifier remains private.",
                "The category is fixed to the Army-entry date, but its sequence relative to OSS service is not established.",
                "A_direct_official", "medium", "publish_qualified",
                "The historical category remains qualified, excluded from verified-employer analytics, and is not converted into a named organization.",
                [
                    {"source_key": INDEX, "support_type": "context_only"},
                    {"source_key": ARMY},
                    {"source_key": TECH, "support_type": "context_only"},
                    {"source_key": CODES, "locator_override": locator},
                ],
                army_affiliation_key(row),
            )
        )

    values.extend(
        [
            claim(
                "fpa-frank-ross-mccoy-b1051", 12, "other_pre_oss_affiliation",
                "Frank Ross McCoy was president of the Foreign Policy Association from 1939 to 1945.",
                "The Library of Congress biographical chronology dates the presidency to 1939-1945 alongside other official wartime assignments.",
                "High confidence from exact name and initial, exceptional rank, and the authoritative papers finding aid.",
                "Documented before and during the wartime period, but not established as the immediate OSS predecessor.",
                "B_authoritative_institutional", "high", "published",
                "The presidency is a professional affiliation, not silently converted into paid employment.",
                [{"source_key": LOC_MCCOY, "excerpt_override": "1939-1945 President, Foreign Policy Association"}],
                "frank-ross-mccoy-fpa-b1051",
            ),
            claim(
                "army-thomas-frederick-mccoy-b1051", 18, "immediate_pre_oss_affiliation",
                "Thomas Frederick McCoy served in the U.S. Army before he was selected for OSS service.",
                "The obituary explicitly sequences World War II Army service and selection for OSS, followed by London service.",
                "High confidence from exact name and initial, compatible major rank, and explicit Army and OSS context.",
                "Explicit immediate military pathway; the exact transfer date and unit are unstated.",
                "C_reputable_contemporary_or_scholarly", "high", "published",
                "The Army assignment is not labeled a civilian employer, and no last civilian employer is inferred.",
                [{"source_key": WASHINGTON_POST, "excerpt_override": "He served in the Army during World War II and was selected to work for the Office of Strategic Services"}],
                "thomas-f-mccoy-army-b1051",
            ),
            claim(
                "harvard-joseph-feder-mccrindle-b1051", 34, "other_pre_oss_affiliation",
                "Joseph Feder McCrindle graduated from Harvard in 1944.",
                "The Smithsonian biographical note documents Harvard graduation in 1944 and separate wartime OSS service in London.",
                "Confirmed for the lieutenant row by rare exact name, full middle name, matching first-lieutenant rank, and explicit OSS service.",
                "Student status is pre- or early-wartime, but its exact sequence relative to OSS is not stated.",
                "B_authoritative_institutional", "high", "publish_qualified",
                "Harvard is recorded as an educational institution, never an employer; evidence is not transferred to the corporal row.",
                [{"source_key": SMITHSONIAN, "excerpt_override": "He graduated from Harvard University in 1944"}],
                "joseph-feder-mccrindle-harvard-b1051",
            ),
            claim(
                "occidental-george-mcafee-mccune-b1051", 41, "immediate_pre_oss_affiliation",
                "George McAfee McCune worked on the Occidental College history staff immediately before receiving leave in 1942 to work for OSS.",
                "The university memorial explicitly says he served on Occidental's history staff from 1939 and was given leave in 1942 for OSS work.",
                "Confirmed by the full name, direct OSS statement, and continuous academic chronology in an institutional memorial.",
                "Explicit immediate civilian employment and last documented civilian employer before OSS work.",
                "B_authoritative_institutional", "confirmed", "published",
                "The formal staff affiliation continuing on leave to 1946 is preserved without obscuring the 1942 transition.",
                [{"source_key": UC_MEMORIAL, "excerpt_override": "From 1939 to 1946 he served on the history staff at Occidental College"}],
                "george-mcafee-mccune-occidental-b1051",
            ),
            claim(
                "army-special-services-marshall-mccune-b1051", 42, "other_pre_oss_affiliation",
                "Marshall Lockhart McCune served as a U.S. Army Special Services Officer in the Far East during World War II.",
                "The family foundation biography documents his volunteer Army service, Far East Special Services assignment, and 1946 discharge.",
                "High confidence from a rare full name, matching initial, compatible lieutenant rank, and detailed wartime Army chronology.",
                "The assignment is documented during the wartime period, but its relation to OSS is uncertain.",
                "B_authoritative_institutional", "medium", "publish_qualified",
                "The assignment is not presented as an immediate OSS predecessor or civilian employment.",
                [{"source_key": MCCUNE_FOUNDATION, "excerpt_override": "stationed in the Far East as a Special Services Officer"}],
                "marshall-lockhart-mccune-army-special-services-b1051",
            ),
        ]
    )
    return values


def unresolved_message(name: str, box: str) -> str:
    return (
        f"Review the indexed Box {box} personnel file for corroborating identifiers, the immediate pre-OSS affiliation, and the last civilian employer. "
        "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed."
    )


def person_updates() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (person_id, name, box) in PEOPLE.items():
        update: dict[str, object] = {
            "person_id": person_id,
            "manual_review_required": True,
            "personnel_file_digitized": False,
            "personnel_file_reviewed": False,
        }
        if row in {1, 2}:
            update.update(
                identity_status="high_confidence",
                identity_evidence="Previously reviewed official index and Army entries agree in name and a nonshared private identifier. The link supports identity and a broad historical occupation category only.",
                nara_catalog_id="1263923",
                research_status="occupation_only_found",
                next_action=f"Review Box {box} for a named employer or institution and the Army-to-OSS sequence.",
                archival_review_priority="high",
            )
        elif row == 12:
            update.update(
                identity_status="high_confidence",
                identity_evidence="The indexed name, middle initial, and exceptional major-general rank align with the Library of Congress Frank Ross McCoy Papers and their continuous military chronology.",
                name_variants=["Frank Ross McCoy"],
                research_status="requires_archival_review",
                next_action="Review Box 501 to determine why McCoy appears in the OSS index and whether the Foreign Policy Association or another wartime role preceded any OSS assignment.",
                archival_review_priority="high",
            )
        elif row == 18:
            update.update(
                identity_status="high_confidence",
                identity_evidence="The exact name and initial, compatible major rank, and obituary's explicit Army-to-OSS chronology identify Thomas Frederick McCoy.",
                name_variants=["Thomas Frederick McCoy"],
                research_status="requires_archival_review",
                next_action="Review Box 501 for the precise Army unit and OSS transfer date and for McCoy's last civilian employer before wartime service.",
                archival_review_priority="high",
            )
        elif row == 22:
            update.update(
                identity_status="conflicting",
                identity_evidence="The private identifier printed for this index row maps to an official Army record for a different name. No occupation or identity evidence is transferred.",
                research_status="conflicting_sources",
                next_action="Review Box 501 to resolve the conflicting protected identifier before assigning any Army occupation or biography.",
                archival_review_priority="critical",
            )
        elif row == 23:
            update.update(
                identity_status="high_confidence",
                identity_evidence="A previously reviewed official Army crosswalk agrees in name and a nonshared private identifier, but the Army entry is dated 10 July 1946.",
                nara_catalog_id="1263923",
                research_status="requires_archival_review",
                next_action="Review Box 501 to establish the OSS chronology before using the postwar-dated 10 July 1946 Army entry as pre-OSS evidence.",
                archival_review_priority="high",
            )
        elif row in {24, 27}:
            update.update(
                identity_status="ambiguous",
                identity_evidence="The Ivna W. McCrary and Ivan W. McCray rows share one private identifier, while the official Army entry uses Ivan W. McCray. Neither row receives the occupation pending file comparison.",
                possible_duplicate_group=DUPLICATE_GROUPS[row],
                research_status="requires_archival_review",
                next_action="Compare both Box 501 personnel files and the shared private identifier before merging or transferring Army evidence.",
                archival_review_priority="critical",
            )
        elif row == 25:
            update.update(
                identity_status="ambiguous",
                identity_evidence="This row shares a private identifier with the page-304 Jack L. McCarary spelling variant. The official Army name resembles McCrary, but the two source rows remain separate.",
                possible_duplicate_group=DUPLICATE_GROUPS[row],
                research_status="requires_archival_review",
                next_action="Compare the page-304 and page-306 personnel files before merging the Jack L. McCarary/McCrary rows or transferring Army evidence.",
                archival_review_priority="critical",
            )
        elif row in {30, 31}:
            update.update(
                identity_status="high_confidence",
                identity_evidence="The official index and Army entry agree after fixed-width name spacing is normalized, and the reviewed private identifier is nonshared. Army occupation code 999 is indeterminate and is not published.",
                name_variants=["Samuel H McCrea Jr."] if row == 31 else None,
                nara_catalog_id="1263923",
                research_status="requires_archival_review",
                next_action=f"Review Box {box} for a named employer or occupation and the Army-to-OSS sequence; code 999 supplies no useful occupation.",
                archival_review_priority="high",
            )
        elif row == 33:
            update.update(
                identity_status="high_confidence",
                identity_evidence="A nonshared official Army link matches the corporal row and supports the student category at Army entry. The separate lieutenant row has a different private identifier.",
                possible_duplicate_group=DUPLICATE_GROUPS[row],
                nara_catalog_id="1263923",
                research_status="occupation_only_found",
                next_action="Review both Box 501 Joseph F. McCrindle files to preserve the separate identities and identify the corporal's institution and OSS chronology.",
                archival_review_priority="critical",
            )
        elif row == 34:
            update.update(
                identity_status="confirmed",
                identity_evidence="The Smithsonian biography supplies the rare full name Joseph Feder McCrindle, explicit London OSS service, and the exact first-lieutenant rank. It belongs only to this lieutenant row.",
                name_variants=["Joseph Feder McCrindle"],
                possible_duplicate_group=DUPLICATE_GROUPS[row],
                research_status="requires_archival_review",
                next_action="Review both Box 501 files to establish the exact Harvard-to-OSS chronology and confirm why a distinct corporal row bears the same indexed name.",
                archival_review_priority="critical",
            )
        elif row == 38:
            update.update(
                identity_status="high_confidence",
                identity_evidence="The official index and Army entry agree in name and a nonshared private identifier, supporting a qualified Army-entry occupation category.",
                nara_catalog_id="1263923",
                research_status="occupation_only_found",
                next_action="Review Box 501 for a named employer and the Army-to-OSS sequence.",
                archival_review_priority="high",
            )
        elif row == 40:
            update.update(
                identity_status="high_confidence",
                identity_evidence="The official index and Army entry agree in name and a nonshared private identifier, but the Army entry is dated 28 June 1946.",
                nara_catalog_id="1263923",
                research_status="requires_archival_review",
                next_action="Review Box 501 to establish the OSS chronology before using the postwar-dated 28 June 1946 Army entry as pre-OSS evidence.",
                archival_review_priority="high",
            )
        elif row == 41:
            update.update(
                identity_status="confirmed",
                identity_evidence="The university memorial supplies the full middle name, Occidental employment, and a direct statement that McCune received leave in 1942 to work for OSS.",
                name_variants=["George McAfee McCune"],
                personnel_category="civilian_professional_or_administrative_grade",
                commissioned_officer=False,
                allied_or_foreign_personnel=False,
                research_status="verified_employer_found",
                next_action="Review Box 501 for McCune's exact OSS appointment date and the terms of his Occidental leave.",
                archival_review_priority="medium",
            )
        elif row == 42:
            update.update(
                identity_status="high_confidence",
                identity_evidence="A rare exact name, matching initial, compatible lieutenant rank, and institutional biography's detailed wartime Army chronology identify Marshall Lockhart McCune.",
                name_variants=["Marshall Lockhart McCune"],
                research_status="requires_archival_review",
                next_action="Review Box 501 to place the Far East Special Services assignment relative to OSS and identify McCune's last civilian employer.",
                archival_review_priority="high",
            )
        elif row == 45:
            update.update(
                identity_status="high_confidence",
                identity_evidence="The official index and Army entry agree in name and a nonshared private identifier, supporting a qualified Army-entry machinist category.",
                nara_catalog_id="1263923",
                research_status="occupation_only_found",
                next_action="Review Box 502 for a named employer and the Army-to-OSS sequence.",
                archival_review_priority="high",
            )
        elif row in {7, 8}:
            update.update(
                identity_status="ambiguous",
                identity_evidence="The adjacent Virgina McCoud and Virgina C. McCould rows may be spelling variants, but the current evidence does not establish that they are one person.",
                possible_duplicate_group=DUPLICATE_GROUPS[row],
                research_status="requires_archival_review",
                next_action=unresolved_message(name, box),
                archival_review_priority="critical",
            )
        else:
            update.update(
                identity_status="unresolved",
                identity_evidence="Exact-name and meaningful-variant checks across official index context and accessible official, institutional, military, newspaper, obituary, directory, and archival discovery sources produced no reliable identity and pre-OSS affiliation bridge; unbridged namesakes were rejected.",
                research_status="requires_archival_review",
                next_action=unresolved_message(name, box),
                archival_review_priority="high",
            )
        values.append({key: value for key, value in update.items() if value is not None})
    if len(values) != 46:
        raise RuntimeError(f"Expected 46 person updates, generated {len(values)}")
    return values


def outcome_note(row: int) -> str:
    if row in {1, 2, 33, 38, 45}:
        return "An accepted official Army identity link supports a qualified dated occupation or student category but no named employer or OSS-transfer sequence."
    if row in {12, 18, 34, 41, 42}:
        return "An authoritative institutional or reputable obituary source supports a specific identity and pre-OSS or wartime affiliation with explicit temporal qualification."
    if row in {23, 30, 31, 40}:
        return "An official Army link supports identity, but an indeterminate occupation code or postwar date prevents a pre-OSS occupation claim."
    if row in {7, 8, 22, 24, 25, 27}:
        return "A repeated row, shared identifier, spelling conflict, or identifier-to-name conflict remains separate for direct personnel-file comparison."
    return "No reliable identity or pre-OSS affiliation was established; unbridged namesakes and chronologically irrelevant results were rejected."


def research_attempts() -> list[dict[str, object]]:
    updates = {item["person_id"]: item for item in person_updates()}
    values: list[dict[str, object]] = []
    sourced_rows = {1, 2, 12, 18, 23, 30, 31, 33, 34, 38, 40, 41, 42, 45}
    conflict_rows = {7, 8, 22, 24, 25, 27}
    for row, (person_id, name, box) in PEOPLE.items():
        if row in sourced_rows:
            outcome, reviewed, rejected = "source_reviewed", 7, 3
        elif row in conflict_rows:
            outcome, reviewed, rejected = "candidate_rejected", 6, 5
        else:
            outcome, reviewed, rejected = "no_result", 5, 3
        values.append(
            {
                "key": f"page306-row{row}-{slug(name)}-b1051",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index context; exact-name and meaningful initial, punctuation, spacing, spelling and OCR variants; accessible official CIA and Archives domain discovery; OSS, rank, branch, assignment and private-identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory and archival searches; indexed Box {box}",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_1051",
                "started_at": "2026-11-11T06:35:00-05:00",
                "completed_at": "2026-11-11T07:45:00-05:00",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, postwar-only leads, and sources without an OSS, rank, private-identifier, unit, or personnel-file bridge were rejected. Shared identifiers and duplicate rows remain separate. Army categories were not converted into named employers.",
                "research_notes": f"{outcome_note(row)} The official index, earlier Library of Congress item-level work where available, accessible exact-name OSS and official-domain discovery, occupation and employer searches, and obituary, institutional, directory, military-history, newspaper, and archival checks were reviewed as applicable. A direct CIA adapter attempt ended at robots denial and a Library of Congress adapter query timed out; neither access failure was treated as a negative result. No authenticated NARA Catalog API request was made.",
                "next_action": str(updates[person_id]["next_action"]),
                "attempt_number": ATTEMPT_NUMBERS[row],
                "research_agent_version": "before-oss-b1051-v1",
            }
        )
    if len(values) != 46:
        raise RuntimeError(f"Expected 46 research attempts, generated {len(values)}")
    return values


def build_bundle() -> dict[str, object]:
    return {
        "bundle_version": "batch-1051-v1",
        "reviewer": "Before OSS Batch 1051 evidence review",
        "sources": sources(),
        "organizations": organizations(),
        "affiliations": affiliations(),
        "claims": claims(),
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }


def main() -> None:
    bundle = build_bundle()
    EvidenceBundle.model_validate(bundle)
    OUTPUT.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
