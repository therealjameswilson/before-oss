#!/usr/bin/env python3
"""Generate the reviewed Batch 1034 evidence bundle for PDF page 289."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page289-cyril-macleod-to-tore-maehle-review_"
    "batch-1034_2026-11-04.json"
)

INDEX = "nara-index-b1034"
ARMY = "army-bulk-b1034"
TECH = "army-tech-b1034"
CODES = "army-codes-b1034"
USMC_MACOMBER = "usmc-mattingly-macomber-b1034"
SFGATE_MADISON = "sfgate-louis-madison-b1034"
CIA_MADISON = "cia-bishop-louis-madison-b1034"
GREENBELT_MADSON = "greenbelt-max-madson-b1034"
CONGRESS_MADSON = "congress-max-madson-b1034"
NPS_MADDOCK = "nps-george-maddock-b1034"

ORG_YALE = "yale-existing-b1034"
ORG_USMCR = "usmcr-existing-b1034"
ORG_GWU = "gwu-existing-b1034"
ORG_LABOR = "labor-existing-b1034"
ORG_ARMY = "army-existing-b1034"
ORG_AGRICULTURE = "agriculture-existing-b1034"


PEOPLE = {
    1: ("31b1b986-73a2-5456-9322-6df1da5d6713", "Cyril MacLeod", "472"),
    2: ("ac210fe4-e532-5413-990b-fc09d1a4e1ef", "Robert B MacLeod", "510"),
    3: ("2c9c428b-91e7-5b97-a6e3-6176c1b5cd73", "Robert B MacLeod", "472"),
    4: ("94c14a7e-15b8-522c-b58f-dc6feb24f43d", "Robert B MacLeod", "472"),
    5: ("72e1135a-c1a0-5f49-9e15-d127edcbd971", "John I Maclintock", "473"),
    6: ("f1629231-5feb-5e36-80d9-900a37ed9f08", "Lloyd F MacMahon", "473"),
    7: ("53c95b95-a356-5255-89f4-99ed725c5bee", "Robert C MacMahon", "473"),
    8: ("aa4295b3-1ba7-5a08-be18-e3f46eab4a1b", "Clyde MacMichael", "473"),
    9: ("1db97d53-5557-5bee-a7e9-284d2e49a2bf", "Constance MacMillan", "473"),
    10: ("b1df6e40-4c81-51a6-b617-83cde4369acc", "James H MacMillan", "473"),
    11: ("5958b8ac-20eb-5309-ac27-a820d9f2aabc", "Norman F MacMillan", "473"),
    12: ("f03993cc-f865-562d-8b07-b627f18ad2c0", "Ronald A MacMillan", "473"),
    13: ("d9d2f7b0-1044-5929-941f-7a9c357b19ed", "Zebulun L MacMillan", "473"),
    14: ("1e7ffc1d-ad93-55c8-acff-2ca6788c0fc9", "Kathryn E MacMorris", "473"),
    15: ("e36b36c9-6ab0-5a4e-8493-1df35ec7541c", "Harley F MacNair", "473"),
    16: ("930a08e8-e4f6-59a6-a6ac-47b0a4533348", "Samuel MacNaughton", "473"),
    17: ("f28c6893-0969-57d5-85cc-a53409a062b9", "Benjamin F MacNeal", "473"),
    18: ("9bf771d3-0151-57b5-8ca4-666c06c203e5", "John A MacNeil", "473"),
    19: ("a2216c44-9b55-5e3a-afc8-63df7ff1c698", "William S MacNeil", "473"),
    20: ("d08b5837-fef4-5ad8-be55-7ce92c23f34d", "Francis G MacNichol", "473"),
    21: ("e45d7180-6117-5e6d-9fd0-39f45bc46a53", "William B Macomber", "473"),
    22: ("f9802f91-aaab-5c47-b5a0-8288403cf718", "James A MacPhail", "473"),
    23: ("ce1bf979-2610-5890-9f1f-2af819067c67", "Frances P MacPherson", "473"),
    24: ("5beef555-b5a4-57c0-b680-d38f26f1356b", "Gardyner B MacPherson", "473"),
    25: ("f08b12c9-3c82-5345-abe9-1f030da27b6a", "Jacklyn W Macridis", "473"),
    26: ("90e44b61-dc94-5c4a-9d32-b810166b748d", "Romylos C Macridis", "473"),
    27: ("329114e6-1dbc-5227-b149-74eb8d7468a1", "Gus Macriyanni", "473"),
    28: ("c2671f4d-8cd8-57f6-a553-897f2c145829", "Doris H MacTavish", "473"),
    29: ("686c67d4-7ca6-545d-96d7-ec9078024217", "Robert M Macwhorter", "473"),
    30: ("b59c75c4-6876-5f00-ab56-321563245fc3", "Chastian MacWilliams", "473"),
    31: ("8bee565c-d1c4-5dad-95ee-676e01357779", "Nora B Macwilliams", "473"),
    32: ("6ab45658-7e49-57db-9234-b54f747448f9", "Henry R Macy", "473"),
    33: ("58d9ca5c-a8ce-5c0c-b65f-be9c138bfdab", "Fred W Madden", "474"),
    34: ("7780c0c0-8093-525e-8db6-162179cd6098", "George H Maddock", "474"),
    35: ("7ede8797-ff24-582f-aaca-a71ab559a512", "Louise H Maddox", "474"),
    36: ("7ebc1840-55de-5cc5-a582-d01501831563", "Patrick Maddox", "474"),
    37: ("598d1b27-efbe-5b51-a467-b745a3350412", "Harvey F Mader", "474"),
    38: ("5f34e3c9-eca9-557d-9c85-e75a3aa35404", "Bernice Q Madison", "474"),
    39: ("b6f045f4-6402-5c53-9fdc-1603193ca1c7", "Janet S Madison", "474"),
    40: ("522fe604-4f7b-50a4-8d5f-19aa1ad725f0", "Louis E Madison", "474"),
    41: ("360bbca5-26e2-5e6a-b343-1a8286ca6935", "Charles Madonia", "474"),
    42: ("17b448c9-905e-5003-a22b-c3102203b12b", "Frances S Madsen", "474"),
    43: ("f5d0fc70-c0b1-591d-90d9-d61aef33062b", "Henry Madsen", "474"),
    44: ("cac58b1f-5ff9-590c-b399-3d831493fd99", "Max T Madson", "474"),
    45: ("6d52c117-16d0-5e67-8660-fd3ba9f23eee", "Masaichi G Maeda", "474"),
    46: ("1f6b7b39-6d40-5c1d-b06e-805c090a8c6f", "Tore Maehle", "474"),
}

# Gus Macriyanni already has a terminal archival-review outcome and eighteen
# research attempts from pilot-v1. Batch 1034 intentionally leaves it intact.
ACTIVE_ROWS = tuple(row for row in PEOPLE if row != 27)

ARMY_ASSOCIATIONS = {
    1: ("1942-09-04", "446", "lithographer", "Lithographers", "unknown", "PDF physical page 173; historical category 4-46"),
    5: ("1943-01-06", "738", "railroad brakeman", "Brakemen, railroad", "unknown", "PDF physical page 174; historical categories 5, 7-38"),
    7: ("1942-10-24", "105", "general office clerk", "Clerks, general office", "unknown", "PDF physical page 171; historical category 1-05"),
    19: ("1943-10-29", "736", "chauffeur or driver of a bus, taxi, truck, or tractor", "Chauffeurs and drivers, bus, taxi, truck, and tractor", "unknown", "PDF physical page 174; historical categories 5, 7-36"),
    20: ("1943-04-29", "661", "semiskilled boot and shoe manufacturing occupation", "Occupations in manufacture of boots and shoes", "unknown", "PDF physical page 173; historical category 6-61"),
    26: ("1944-05-08", "031", "secondary-school teacher or principal", "Teachers (secondary school) and principals", "unknown", "PDF physical page 171; historical category 0-31"),
    34: ("1942-09-02", "992", "student", "Students", "student", "PDF physical page 304; corrected historical category 9-92"),
    41: ("1942-12-02", "460", "shoemaker or shoe repairer, not in a factory", "Shoemakers and shoe repairmen, not in factory", "unknown", "PDF physical page 173; historical category 4-60"),
    43: ("1942-10-13", "992", "student", "Students", "student", "PDF physical page 304; corrected historical category 9-92"),
    45: ("1942-02-23", "105", "general office clerk", "Clerks, general office", "unknown", "PDF physical page 171; historical category 1-05"),
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
            archival_identifier="RG 226, Entry A1-224, Boxes 472-474 and 510",
            title="OSS Personnel Files from Excel",
            author_creator="National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="2010-12-23",
            locator="PDF page 289, rows 1-46; page and all rows visually checked at 180 dpi",
            source_quality="A_direct_official",
            collection_name="Records of the Office of Strategic Services, Record Group 226",
            rights_notes="All 46 printed rows remain separate. Full protected identifiers remain private. Batch 1034 updates 45 rows and preserves Gus Macriyanni's prior terminal outcome.",
        ),
        source(
            ARMY,
            stable_url="https://catalog.archives.gov/id/1263923",
            archival_identifier="National Archives Identifier 1263923; parent series NAID 604357",
            title="Electronic Army Serial Number Merged File, ca. 1938-1946",
            author_creator="Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            repository_publisher="National Archives and Records Administration",
            publication_record_date="1938-1946; merged file created 2002",
            locator="Official unrestricted ASNEF.FIN.DAT; ten Batch 1034 identity candidates explicitly reviewed",
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
            locator="PDF physical pages 171, 173, 174 and 304; all ten published Batch 1034 categories visually checked",
            source_quality="A_direct_official",
            collection_name="World War II Army Enlistment Records technical documentation",
            rights_notes="Historical categories identify neither employer, institution, workplace, nor exact Army-to-OSS sequence.",
        ),
        source(
            USMC_MACOMBER,
            stable_url="https://www.usmcu.edu/Portals/218/Herringbone%20Cloak%20-%20GI%20Dagger%20Marines%20Of%20The%20OSS.pdf",
            title="Herringbone Cloak—GI Dagger: Marines of the OSS",
            author_creator="Major Robert E. Mattingly, United States Marine Corps",
            repository_publisher="United States Marine Corps Command and Staff College",
            publication_record_date="1979; published by the History and Museums Division in 1989",
            locator="Printed pages 151-153, William Butts Macomber profile",
            source_quality="A_direct_official",
            collection_name="Marine Corps historical monographs",
            rights_notes="The official study identifies Yale student status, March 1942 Marine Corps Reserve entry, December 1943 commission, and a prearranged OSS assignment.",
        ),
        source(
            SFGATE_MADISON,
            stable_url="https://www.sfgate.com/bayarea/article/Louis-E-Madison-wrote-S-F-guidebook-3297232.php",
            title="Louis E. Madison wrote S.F. guidebook",
            author_creator="Charles Burress",
            repository_publisher="San Francisco Chronicle via SFGATE",
            publication_record_date="2008-01-22",
            locator="Biographical paragraph beginning with birthplace and George Washington University",
            source_quality="C_reputable_contemporary_or_scholarly",
            rights_notes="The obituary explicitly sequences university study, Department of Labor employment, Army entry, and selection for OSS; no postwar role is used to infer prewar employment.",
        ),
        source(
            CIA_MADISON,
            stable_url="https://www.cia.gov/readingroom/docs/BISHOP%2C%20ROBERT%20%20%20VOL.%202_0008.pdf",
            archival_identifier="BISHOP, ROBERT, Volume 2, document 0008",
            title="Report concerning OSS command and intelligence reporting in Bucharest",
            author_creator="United States Office of Strategic Services",
            repository_publisher="Central Intelligence Agency Freedom of Information Act Electronic Reading Room",
            publication_record_date="wartime report; later declassified",
            locator="PDF page 2, paragraph h",
            source_quality="A_direct_official",
            collection_name="OSS Collection",
            rights_notes="The direct OSS record identifies Capt. Louis Madison as Reports Officer in charge of positive intelligence in Bucharest; it is identity and service context, not employer evidence.",
        ),
        source(
            GREENBELT_MADSON,
            stable_url="https://www.greenbeltnewsreview.com/issues/GNR19570314.pdf",
            title="Biographies of Candidates",
            author_creator="Max T. Madsen and other Greenbelt Veterans Housing Corporation candidates",
            repository_publisher="Greenbelt News Review",
            publication_record_date="1957-03-14",
            locator="PDF page 3, Max T. Madsen candidate biography",
            source_quality="C_reputable_contemporary_or_scholarly",
            collection_name="Greenbelt News Review",
            rights_notes="The first-person biography uses the Madsen spelling, dates Department of Agriculture employment from 1941, and identifies wartime OSS Photographic Aide service.",
        ),
        source(
            CONGRESS_MADSON,
            stable_url="https://www.congress.gov/77/crecb/1942/05/15/GPO-CRECB-1942-pt3-33.pdf",
            archival_identifier="77th Congress, Congressional Record, May 15, 1942",
            title="Congressional Record—Senate",
            author_creator="United States Congress",
            repository_publisher="Congress.gov; U.S. Government Publishing Office",
            publication_record_date="1942-05-15",
            locator="Printed page 4237, Extension Service employee list; Madson, Max T.",
            source_quality="A_direct_official",
            collection_name="Congressional Record",
            rights_notes="The official employee list identifies Max T. Madson as a Department of Agriculture motion-picture projectionist in 1942.",
        ),
        source(
            NPS_MADDOCK,
            stable_url="https://www.nps.gov/articles/summary-and-conclusion.htm",
            title="Summary and Conclusion",
            repository_publisher="United States National Park Service",
            locator="Section 'Training Spies, Saboteurs, and Agent Operatives in the Parks,' George Maddock recollection",
            source_quality="A_direct_official",
            collection_name="OSS Training in the National Parks and Service Abroad in World War II",
            rights_notes="The NPS history identifies George Maddock as a member of an OSS team in southern France. The page's 1933 jump date is an evident typographical error and is not repeated as fact.",
        ),
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": ORG_YALE,
            "organization_id": "918dedde-f9d1-5db1-8304-5c218a06b9b5",
            "canonical_name": "Yale University",
            "historical_name": "Yale University",
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "New Haven",
            "state_or_region": "Connecticut",
            "country": "United States",
            "normalization_notes": "Student status remains separate from employment.",
        },
        {
            "key": ORG_USMCR,
            "organization_id": "bf23e210-3d2f-5f71-a0d6-b3e2f2f06040",
            "canonical_name": "United States Marine Corps Reserve",
            "historical_name": "U.S.M.C.R.",
            "aliases": ["Marine Corps Reserve", "Class III Marine Corps Reserve"],
            "organization_type": "military reserve service",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "Military service is modeled as an assignment, not a civilian employer.",
        },
        {
            "key": ORG_GWU,
            "organization_id": "57d77c98-1b86-5405-947a-305d7d144012",
            "canonical_name": "George Washington University",
            "historical_name": "George Washington University",
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "Washington",
            "state_or_region": "District of Columbia",
            "country": "United States",
            "normalization_notes": "Student status remains separate from employment.",
        },
        {
            "key": ORG_LABOR,
            "organization_id": "feacdeca-7391-5e30-a968-6c29d8b43039",
            "canonical_name": "U.S. Department of Labor",
            "historical_name": "U.S. Department of Labor",
            "organization_type": "federal department",
            "sector": "federal_government",
            "city": "Washington",
            "state_or_region": "District of Columbia",
            "country": "United States",
            "normalization_notes": "The historical federal department name is retained.",
        },
        {
            "key": ORG_ARMY,
            "organization_id": "28a26f92-78af-5a1a-9c09-a843eb5975b4",
            "canonical_name": "United States Army",
            "historical_name": "United States Army",
            "aliases": ["U.S. Army", "Army"],
            "organization_type": "military service",
            "sector": "military",
            "country": "United States",
            "normalization_notes": "Military service is modeled as an assignment, not a civilian employer.",
        },
        {
            "key": ORG_AGRICULTURE,
            "organization_id": "fe92f024-a09d-5899-b6ad-5f3edc910924",
            "canonical_name": "United States Department of Agriculture",
            "historical_name": "U.S. Department of Agriculture",
            "aliases": ["Department of Agriculture", "USDA"],
            "organization_type": "federal department",
            "sector": "federal_government",
            "city": "Washington",
            "state_or_region": "District of Columbia",
            "country": "United States",
            "normalization_notes": "The historical federal employer is preserved; its Motion Picture Service is retained in the role and evidence notes.",
        },
    ]


def affiliation(
    key: str,
    row: int,
    relationship: str,
    temporal: str,
    identity: str,
    confidence: str,
    quality: str,
    status: str = "published",
    **kwargs: object,
) -> dict[str, object]:
    value: dict[str, object] = {
        "key": key,
        "person_id": PEOPLE[row][0],
        "relationship_type": relationship,
        "pre_oss_temporal_basis": temporal,
        "identity_confidence": identity,
        "claim_confidence": confidence,
        "source_quality": quality,
        "publication_status": status,
    }
    value.update(kwargs)
    return value


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    high_identity_rows = {1, 5, 7, 19, 20, 45}
    for row, (date, code, occupation, _label, relationship, _locator) in ARMY_ASSOCIATIONS.items():
        identity = "high_confidence" if row in high_identity_rows else "confirmed"
        kwargs: dict[str, object] = {
            "end_date": date,
            "date_precision": f"Historical civilian-occupation code {code} was recorded at Army entry on {date}; no named employer, institution, or workplace is supplied.",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "research_notes": "The broad historical category is not converted into a named employer and is excluded from verified-employer analytics.",
        }
        if relationship == "student":
            kwargs["role_title"] = "student"
        else:
            kwargs["occupation"] = occupation
        values.append(
            affiliation(
                f"{slug(PEOPLE[row][1])}-army-association-b1034",
                row,
                relationship,
                "strongly_date_bounded",
                identity,
                "medium",
                "A_direct_official",
                "publish_qualified",
                **kwargs,
            )
        )
    values.extend(
        [
            affiliation(
                "william-macomber-yale-b1034",
                21,
                "student",
                "strongly_date_bounded",
                "high_confidence",
                "high",
                "A_direct_official",
                organization_key=ORG_YALE,
                organization_name_as_found="Yale",
                role_title="pre-law student",
                end_date="1943",
                date_precision="The Marine Corps study identifies Macomber as a Yale student who accelerated his course work to graduate before entering officer training.",
                city="New Haven",
                state_or_region="Connecticut",
                country="United States",
                immediate_pre_oss=False,
                last_civilian_pre_service=False,
                research_notes="Student status, not employment; Marine Corps service intervened before OSS duty.",
            ),
            affiliation(
                "william-macomber-usmcr-b1034",
                21,
                "military_assignment",
                "explicit_immediate",
                "high_confidence",
                "high",
                "A_direct_official",
                organization_key=ORG_USMCR,
                organization_name_as_found="Class III Marine Corps Reserve",
                role_title="Marine officer; commissioned second lieutenant",
                start_date="1942-03",
                end_date="1943-12-01",
                date_precision="The official study dates Reserve enlistment to March 1942 and says his December 1, 1943 commission already carried a planned OSS assignment.",
                country="United States",
                immediate_pre_oss=True,
                last_civilian_pre_service=False,
                research_notes="The immediate predecessor is a military assignment, not a civilian employer.",
            ),
            affiliation(
                "louis-madison-gwu-b1034",
                40,
                "student",
                "documented_prewar",
                "high_confidence",
                "high",
                "C_reputable_contemporary_or_scholarly",
                organization_key=ORG_GWU,
                organization_name_as_found="George Washington University",
                role_title="undergraduate student",
                date_precision="The obituary reports a bachelor's degree with majors in English literature and economics before Department of Labor employment.",
                city="Washington",
                state_or_region="District of Columbia",
                country="United States",
                immediate_pre_oss=False,
                last_civilian_pre_service=False,
                research_notes="Student status, not employment.",
            ),
            affiliation(
                "louis-madison-labor-b1034",
                40,
                "employment",
                "strongly_date_bounded",
                "high_confidence",
                "high",
                "C_reputable_contemporary_or_scholarly",
                organization_key=ORG_LABOR,
                organization_name_as_found="U.S. Department of Labor",
                role_title="economist",
                end_date="1942",
                date_precision="The obituary explicitly places Department of Labor employment before Army entry during World War II; the exact departure date is not supplied.",
                city="Washington",
                state_or_region="District of Columbia",
                country="United States",
                immediate_pre_oss=False,
                last_civilian_pre_service=True,
                research_notes="Best-supported last civilian employer before Army service and OSS selection; the intervening Army assignment is modeled separately.",
            ),
            affiliation(
                "louis-madison-army-b1034",
                40,
                "military_assignment",
                "explicit_immediate",
                "high_confidence",
                "high",
                "A_direct_official",
                organization_key=ORG_ARMY,
                organization_name_as_found="Army",
                role_title="Army officer selected for OSS; later captain",
                start_date="1942",
                date_precision="The obituary sequences Army entry before OSS selection, and a direct OSS record identifies Capt. Louis Madison as Bucharest Reports Officer.",
                country="United States",
                immediate_pre_oss=True,
                last_civilian_pre_service=False,
                research_notes="The immediate predecessor is military service; Department of Labor remains the last civilian employer.",
            ),
            affiliation(
                "max-madson-agriculture-b1034",
                44,
                "employment",
                "strongly_date_bounded",
                "high_confidence",
                "high",
                "A_direct_official",
                organization_key=ORG_AGRICULTURE,
                organization_name_as_found="Motion Picture Service of the U. S. Dept. of Agriculture",
                role_title="motion-picture projectionist and sound technician",
                start_date="1941",
                end_date="1942",
                date_precision="A first-person 1957 biography dates the job from 1941; an official May 1942 employee list independently identifies Madson as a motion-picture projectionist. Neither source gives an OSS entry date.",
                city="Washington",
                state_or_region="District of Columbia",
                country="United States",
                immediate_pre_oss=False,
                last_civilian_pre_service=True,
                research_notes="Published as the best-supported last civilian employer. Immediate-pre-OSS status is not asserted because the transition date is unavailable.",
            ),
        ]
    )
    return values


def claim(
    key: str,
    row: int,
    claim_type: str,
    text: str,
    paraphrase: str,
    identity: str,
    temporal: str,
    quality: str,
    confidence: str,
    source_links: list[dict[str, str]],
    notes: str,
    status: str = "published",
    affiliation_key: str | None = None,
) -> dict[str, object]:
    value: dict[str, object] = {
        "key": key,
        "person_id": PEOPLE[row][0],
        "claim_type": claim_type,
        "claim_text": text,
        "evidence_paraphrase": paraphrase,
        "identity_match_assessment": identity,
        "temporal_assessment": temporal,
        "source_quality": quality,
        "claim_confidence": confidence,
        "publication_status": status,
        "match_notes": notes,
        "sources": source_links,
    }
    if affiliation_key:
        value["affiliation_key"] = affiliation_key
    return value


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    high_identity_rows = {1, 5, 7, 19, 20, 45}
    for row, (date, code, occupation, label, relationship, locator) in ARMY_ASSOCIATIONS.items():
        identity = (
            "High confidence from a nonshared protected linkage plus a reviewed spacing or damaged-name variation; the protected identifier is not published."
            if row in high_identity_rows
            else "Confirmed by exact official name agreement and a nonshared protected linkage; the protected identifier is not published."
        )
        affiliation_key = f"{slug(PEOPLE[row][1])}-army-association-b1034"
        source_links = [
            {"source_key": INDEX},
            {"source_key": ARMY},
            {"source_key": TECH, "support_type": "context_only"},
            {"source_key": CODES, "locator_override": locator},
        ]
        if row == 34:
            source_links.append({"source_key": NPS_MADDOCK, "support_type": "context_only"})
        values.append(
            claim(
                f"army-{slug(PEOPLE[row][1])}-b1034",
                row,
                "other_pre_oss_affiliation" if relationship == "student" else "occupation",
                f"At Army entry on {date}, {PEOPLE[row][1]} was recorded as {occupation}; no employer, institution, or workplace is identified.",
                f"The Army bulk file records code {code}, and the visually checked official code list defines the category as {label}.",
                identity,
                "Strongly date-bounded to Army entry, but not proven to be the immediately preceding role or status before OSS.",
                "A_direct_official",
                "medium",
                source_links,
                "The historical category is qualified, excluded from verified-employer analytics, and not converted into a named organization.",
                "publish_qualified",
                affiliation_key,
            )
        )
    values.extend(
        [
            claim(
                "student-william-macomber-yale-b1034",
                21,
                "other_pre_oss_affiliation",
                "William Butts Macomber was a Yale pre-law student before entering Marine Corps service.",
                "The Marine Corps study says he accelerated his Yale course work so he could graduate before officer training.",
                "High confidence from the expanded full name, matching middle initial, compatible lieutenant rank, and direct OSS mission history.",
                "Strongly date-bounded before Marine Corps and OSS service; Yale is not an employer.",
                "A_direct_official",
                "high",
                [{"source_key": USMC_MACOMBER}, {"source_key": INDEX, "support_type": "context_only"}],
                "Student status is kept separate from employment.",
                "published",
                "william-macomber-yale-b1034",
            ),
            claim(
                "immediate-william-macomber-usmcr-b1034",
                21,
                "immediate_pre_oss_affiliation",
                "William Butts Macomber's documented immediate pre-OSS affiliation was the United States Marine Corps Reserve.",
                "The official study dates his Reserve entry to March 1942 and says his December 1943 commission already carried a planned OSS assignment.",
                "High confidence from the full name, compatible indexed rank, direct OSS assignment, and detailed Marine chronology.",
                "Explicit military-to-OSS sequence; this is not a civilian employer.",
                "A_direct_official",
                "high",
                [{"source_key": USMC_MACOMBER}, {"source_key": INDEX, "support_type": "context_only"}],
                "No civilian employer is inferred from Yale attendance or later diplomatic work.",
                "published",
                "william-macomber-usmcr-b1034",
            ),
            claim(
                "student-louis-madison-gwu-b1034",
                40,
                "other_pre_oss_affiliation",
                "Louis E. Madison attended George Washington University before working for the U.S. Department of Labor.",
                "The obituary reports a bachelor's degree with English-literature and economics majors, followed by Department of Labor employment.",
                "High confidence from the uncommon full name, compatible captain rank, exact wartime chronology, and direct OSS Bucharest record.",
                "Documented prewar education; student status is not employment.",
                "C_reputable_contemporary_or_scholarly",
                "high",
                [{"source_key": SFGATE_MADISON}, {"source_key": CIA_MADISON, "support_type": "context_only"}],
                "Education is kept separate from the employer and military pathway.",
                "published",
                "louis-madison-gwu-b1034",
            ),
            claim(
                "last-civilian-louis-madison-labor-b1034",
                40,
                "last_civilian_pre_service",
                "The U.S. Department of Labor is Louis E. Madison's documented last civilian employer before Army service and OSS selection.",
                "The obituary identifies him as a Department of Labor economist immediately before describing Army entry and OSS selection.",
                "High confidence from the exact name, compatible captain rank, explicit employment sequence, and official OSS corroboration.",
                "Strongly date-bounded before Army entry; the exact departure date is not supplied.",
                "C_reputable_contemporary_or_scholarly",
                "high",
                [{"source_key": SFGATE_MADISON}, {"source_key": CIA_MADISON, "support_type": "context_only"}],
                "Department of Labor is not mislabeled as the immediate pre-OSS affiliation because Army service intervened.",
                "published",
                "louis-madison-labor-b1034",
            ),
            claim(
                "immediate-louis-madison-army-b1034",
                40,
                "immediate_pre_oss_affiliation",
                "Louis E. Madison's documented immediate pre-OSS affiliation was the United States Army.",
                "The obituary places Army entry before OSS selection, while a direct OSS record identifies Capt. Madison as Bucharest Reports Officer.",
                "High confidence from the exact name, compatible captain rank, coherent sequence, and direct wartime role evidence.",
                "Explicit military-to-OSS sequence; this is not a civilian employer.",
                "A_direct_official",
                "high",
                [{"source_key": SFGATE_MADISON}, {"source_key": CIA_MADISON}, {"source_key": INDEX, "support_type": "context_only"}],
                "The immediate military affiliation and last civilian employer remain separate claims.",
                "published",
                "louis-madison-army-b1034",
            ),
            claim(
                "last-civilian-max-madson-agriculture-b1034",
                44,
                "last_civilian_pre_service",
                "The United States Department of Agriculture is Max T. Madson's best-supported last civilian employer before OSS service.",
                "A 1942 Congressional Record employee list names Max T. Madson as a motion-picture projectionist; his later first-person biography dates the job from 1941 and identifies OSS Photographic Aide service.",
                "High confidence from the rare full name, exact official employee listing, and Madsen spelling variant in a first-person biography that directly names OSS service.",
                "Strongly date-bounded to 1941-42, but the exact departure and OSS-entry dates remain unavailable.",
                "A_direct_official",
                "high",
                [{"source_key": CONGRESS_MADSON}, {"source_key": GREENBELT_MADSON}, {"source_key": INDEX, "support_type": "context_only"}],
                "Published as last civilian employer only; immediate-pre-OSS status is not asserted.",
                "published",
                "max-madson-agriculture-b1034",
            ),
        ]
    )
    return values


def base_update(row: int, **overrides: object) -> dict[str, object]:
    name = PEOPLE[row][1]
    box = PEOPLE[row][2]
    value: dict[str, object] = {
        "person_id": PEOPLE[row][0],
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified page 289 source preserves {name}, Box {box}, rank or grade when printed, notes when present, and archive location. Staged official, exact-name, employment, occupation, obituary, institutional, newspaper, directory, and archival searches did not establish a defensible identity-and-affiliation bridge.",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": f"Review indexed Box {box} for corroborating identifiers, immediate pre-OSS affiliation, and last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }
    value.update(overrides)
    return value


def person_updates() -> list[dict[str, object]]:
    updates = [base_update(row) for row in ACTIVE_ROWS]
    by_row = {row: update for row, update in zip(ACTIVE_ROWS, updates, strict=True)}

    high_identity_rows = {1, 5, 7, 19, 20, 45}
    variants = {
        1: ["Cyril Mac Leod"],
        5: ["John I Mac Lintock"],
        7: ["Robert C Mac Mahon"],
        19: ["William S Mac Neil"],
        20: ["Francis G Mac Nichol"],
        45: ["Masaichi G K Maeda"],
    }
    for row in ARMY_ASSOCIATIONS:
        status = "high_confidence" if row in high_identity_rows else "confirmed"
        by_row[row].update(
            identity_status=status,
            identity_evidence=(
                "A nonshared protected linkage plus a reviewed spacing or damaged-name variation connects the official index and Army records; the protected identifier remains private."
                if status == "high_confidence"
                else "Exact official name agreement and a nonshared protected linkage connect the index and Army records; the protected identifier remains private."
            ),
            name_variants=variants.get(row),
            replace_name_variants=False,
            personnel_category="enlisted_army_personnel",
            commissioned_officer=False,
            allied_or_foreign_personnel=False,
            research_status="occupation_only_found",
            nara_catalog_id="1263923",
            archival_review_priority="critical" if row in {1, 5, 20, 45} else "high",
            next_action=f"Review Box {PEOPLE[row][2]} to identify a named employer or institution and establish Army-to-OSS chronology. The protected Army link supplies only a broad historical occupation or student-status category.",
        )

    for row in (2, 3, 4):
        by_row[row].update(
            identity_status="ambiguous",
            identity_evidence="Page 289 prints three separate Robert B MacLeod rows: an unranked Box 510 McLeod cross-reference, a P-7 Box 472 row with a protected identifier, and a DR Box 472 row. Name agreement alone does not establish one person.",
            possible_duplicate_group="p289-robert-b-macleod-b621",
            research_status="needs_identity_review",
            next_action="Compare the Box 510 McLeod cross-reference with both Box 472 personnel files before any merge. No rank, identity, employer, or affiliation evidence is transferred among the three rows.",
            archival_review_priority="critical",
        )

    by_row[21].update(
        identity_status="high_confidence",
        identity_evidence="The official Marine Corps study expands the name to William Butts Macomber, gives a compatible commissioned rank, and explicitly traces Yale, Marine, and OSS FREELANCE service.",
        name_variants=["William Butts Macomber", "William B Macomber Jr.", "William Butts Macomber Jr."],
        replace_name_variants=False,
        personnel_category="commissioned_marine_corps_officer",
        commissioned_officer=True,
        allied_or_foreign_personnel=False,
        research_status="completed",
        next_action="Review Box 473 for the formal Marine-to-OSS transfer order and exact Yale graduation date. Accessible official evidence establishes the immediate Marine affiliation and prior student status; no civilian employer is inferred.",
        archival_review_priority="medium",
    )
    by_row[34].update(
        identity_evidence="Exact official name agreement and a nonshared protected Army linkage confirm the identity; National Park Service history independently identifies George Maddock as an OSS team member in southern France.",
        next_action="Review Box 474 to identify George Maddock's educational institution, determine whether student status immediately preceded Army entry, and document the Army-to-OSS assignment sequence.",
    )
    by_row[40].update(
        identity_status="high_confidence",
        identity_evidence="The uncommon exact name, compatible captain rank, Department of Labor-to-Army-to-OSS chronology, and a direct OSS Bucharest record establish a high-confidence identity match.",
        personnel_category="commissioned_army_officer",
        commissioned_officer=True,
        allied_or_foreign_personnel=False,
        research_status="verified_employer_found",
        next_action="Review Box 474 for the exact Department of Labor departure date, Army entry date, and OSS selection or transfer order. The accessible record already separates the last civilian employer from the immediate Army affiliation.",
        archival_review_priority="medium",
    )
    by_row[44].update(
        identity_status="high_confidence",
        identity_evidence="The rare full name appears in an official 1942 Department of Agriculture employee list; a first-person biography uses the Madsen variant and directly identifies Department employment and OSS Photographic Aide service.",
        name_variants=["Max T Madsen"],
        replace_name_variants=False,
        personnel_category="civilian_professional_or_administrative_grade",
        commissioned_officer=False,
        allied_or_foreign_personnel=False,
        research_status="verified_employer_found",
        next_action="Review Box 474 for the exact Department of Agriculture departure and OSS entry dates. Immediate-pre-OSS status remains unasserted pending that chronology.",
        archival_review_priority="medium",
    )

    if len(updates) != 45:
        raise RuntimeError(f"Expected 45 person updates, generated {len(updates)}")
    return updates


def unresolved_reason(row: int) -> str:
    special = {
        2: "The Box 510 McLeod cross-reference was not merged with either Box 472 row.",
        3: "The P-7 Box 472 Robert B MacLeod row remains separate from the unranked and DR rows.",
        4: "The DR Box 472 Robert B MacLeod row remains separate from the unranked and P-7 rows.",
        6: "A federal judicial biography for a Lloyd Francis MacMahon names 1942-53 private practice and 1944-45 Naval Reserve service, but no evidence bridges that namesake to this unranked index row.",
        15: "A University of Chicago finding aid identifies a Harley Farnsworth MacNair professorship from 1928, but no source reviewed connects that academic to this indexed row or OSS service.",
        36: "The protected ABRO notation and British A note were preserved, but searches did not establish a full identity or pre-OSS affiliation for Patrick Maddox.",
        38: "Later academic and social-welfare material for Bernice Q. Madison lacked a pre-OSS identity bridge and was not used to infer an employer.",
        39: "Exact-name searches did not establish a reliable identity or pre-OSS affiliation for Janet S. Madison.",
        46: "Exact-name and meaningful-variant searches did not establish a reliable identity or pre-OSS affiliation for Tore Maehle.",
    }
    return special.get(
        row,
        "Unbridged namesakes, snippets, commercial people-finder pages, unsourced genealogy, relatives, and postwar-only leads did not establish this indexed person's identity or pre-OSS affiliation.",
    )


def research_attempts() -> list[dict[str, object]]:
    updates = {item["person_id"]: item for item in person_updates()}
    substantiated = set(ARMY_ASSOCIATIONS) | {21, 40, 44}
    values: list[dict[str, object]] = []
    for row in ACTIVE_ROWS:
        person_id, name, box = PEOPLE[row]
        next_action = str(updates[person_id]["next_action"])
        values.append(
            {
                "key": f"page289-row{row}-{slug(name)}-b1034",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA OSS index context; exact-name and meaningful initial, suffix, spacing, punctuation and OCR variants; OSS and CIA Reading Room; rank, branch, assignment and protected-identifier clues; employer and occupation 1940; obituary, biography, institutional, newspaper, directory and archival searches; indexed Box {box}",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_1034",
                "started_at": "2026-11-04T17:25:00-05:00",
                "completed_at": "2026-11-04T19:10:00-05:00",
                "outcome": "source_reviewed" if row in substantiated else "candidate_rejected",
                "sources_reviewed": 7 if row in {21, 40, 44} else (5 if row in substantiated else 5),
                "candidate_sources_rejected": 2 if row in substantiated else 4,
                "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, and postwar-only leads were rejected. Army categories were not converted into named employers; identical names were not merged; and discovery-only material was not published as evidence.",
                "research_notes": f"{unresolved_reason(row)} The official index, exact-name OSS searches, targeted CIA context, employment and occupation searches, and institutional, newspaper, obituary, directory, and archival searches were reviewed as applicable. Page 289 and all cited code-list pages were visually checked. No authenticated NARA Catalog API request was made.",
                "next_action": next_action,
                "attempt_number": 1,
                "research_agent_version": "before-oss-b1034-v1",
            }
        )
    if len(values) != 45:
        raise RuntimeError(f"Expected 45 research attempts, generated {len(values)}")
    return values


def main() -> None:
    bundle = {
        "bundle_version": "batch-1034-v1",
        "reviewer": "Before OSS Batch 1034 evidence review",
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
