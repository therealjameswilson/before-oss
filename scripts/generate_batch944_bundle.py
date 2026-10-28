#!/usr/bin/env python3
"""Generate the reviewed Batch 944 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page462-ivan-m-tchok-to-harry-m-templeton-"
    "review_batch-944_2026-10-28.json"
)

INDEX = "nara-index-b944"
ARMY = "army-bulk-b944"
TECH = "army-tech-b944"
CODES = "army-codes-b944"
TCHOK_BIO = "slovenska-biografija-tchok-b944"
STANFORD = "stanford-journalism-teilhet-b944"
TEILHET_BIO = "ebsco-teilhet-b944"
OSU_1938 = "ohio-state-trustees-telberg-1938-b944"
NZ_LISTENER = "nz-listener-telberg-1949-b944"

SELF_EMPLOYED_LEGAL = "self-employed-legal-practice-b944"
ZVEZA = "zveza-jugoslovanskih-emigrantov-b944"
STANFORD_ORG = "stanford-university-b944"
OHIO_STATE = "ohio-state-university-b944"


PEOPLE = {
    24: ("51bec465-c44d-5d74-b1d8-0b4fe2308f7e", "Ivan M Tchok"),
    25: ("ae99d4da-c423-5ce2-a09a-764c1a4d4dcd", "John Teague"),
    26: ("7322ca21-e1d6-5ca4-9142-8d1755af7ff7", "Clyde V Teasdale"),
    27: ("9a531f65-6e90-5bd1-b882-b43b45f6b9e6", "Leo Teboul"),
    28: ("8754b271-e59d-5411-ab7d-3584f0aa445c", "William J Techtmann"),
    29: ("6ec02784-6748-5597-bbad-a9135fd3b5c3", "Pete Tedeschi"),
    30: ("8aeb5ab3-cd07-51d1-90a4-0da6cea7597d", "William S Teeter"),
    31: ("d8f9765d-97f8-53ec-b3cf-180fcba62cf9", "Mary E Teichgraeber"),
    32: ("fb7f264c-9871-52d7-9c66-07428e4bd1e3", "Kate Teichner"),
    33: ("3d0678d9-f91e-5283-a68c-9ab560d7a8f4", "Gudrun I Teigen"),
    34: ("bbcb261e-2496-5956-8fe8-6ec811e96fe3", "Darwin L Teilhet"),
    35: ("94a92f6d-33ad-5793-82c6-5d3544f9d8a8", "Ina Telberg"),
    36: ("e8dfe679-56fe-5269-af7e-4e6e84481a6e", "Anastos Telemachus"),
    37: ("d7be1805-264b-5e86-9d34-d50717002b7f", "Ruby D Telesca"),
    38: ("2e4a2945-99fb-5abc-aaf5-781d85c3cf1c", "Aram H Tellalian"),
    39: ("3b8081c4-27ff-5382-b29e-5bf69bbd63e8", "Clarence R Teller"),
    40: ("b50fd8ff-b5d6-5ecf-bbca-e0fa69bf9bd6", "Rennie L Tellia"),
    41: ("685f819e-75d4-5aee-a4a2-65ca0b42b999", "Dominic L Telloni"),
    42: ("f3300ed3-b2fa-5d76-a9cc-e5441bb52d92", "Joseph G Temolo"),
    43: ("1edf6ee4-65f8-5e18-b87d-11d086ddaf85", "Fay W Temple"),
    44: ("d391a6b2-3902-57ba-a702-a5c8a8ae87cc", "George H Temple"),
    45: ("b2d1f2ba-8862-5b16-b620-3ffbbd9c67d6", "Lucille E Temple"),
    46: ("76095811-68ca-55e1-b76d-074dbd95b7b5", "Harry M Templeton"),
}


ARMY_OCCUPATIONS = [
    {
        "row": 26,
        "date": "1942-04-30",
        "code": "306",
        "occupation": "General farmers",
        "public_occupation": "general farmer",
        "locator": "PDF physical page 172; historical category 3-06",
    },
    {
        "row": 30,
        "date": "1943-03-17",
        "code": "992",
        "occupation": "Students",
        "public_occupation": "student",
        "locator": "PDF physical page 304; amended historical category 9-92",
        "relationship": "student",
    },
    {
        "row": 40,
        "date": "1942-07-08",
        "code": "736",
        "occupation": "Chauffeurs and drivers, bus, taxi, truck, and tractor",
        "public_occupation": "chauffeur or driver in the broad historical bus, taxi, truck and tractor category",
        "locator": "PDF physical page 174; historical category 7-36",
    },
    {
        "row": 41,
        "date": "1943-04-19",
        "code": "957",
        "occupation": "Occupations in laundering, cleaning, dyeing, and pressing apparel and other articles",
        "public_occupation": "laundering, cleaning, dyeing or pressing occupation in the broad historical category",
        "locator": "PDF physical page 174; historical category 9-57",
    },
    {
        "row": 42,
        "date": "1943-05-14",
        "code": "401",
        "occupation": "Bakers",
        "public_occupation": "baker",
        "locator": "PDF physical page 173; historical category 4-01",
    },
    {
        "row": 44,
        "date": "1943-06-09",
        "code": "992",
        "occupation": "Students",
        "public_occupation": "student",
        "locator": "PDF physical page 304; amended historical category 9-92",
        "relationship": "student",
    },
]


UNRESOLVED = {
    25: "The common name and absence of a rank, identifier or public assignment prevented a defensible match to an external John Teague biography.",
    29: "A postwar minor-league player is a namesake lead only; no OSS, Box 768 or wartime identifier connects him to the indexed row.",
    31: "Exact-name and middle-initial searches found no reliable OSS, employer, occupation, institutional or archival identity bridge.",
    32: "The printed six-digit value is preserved but is ineligible for the Army merged-file matcher and was not reinterpreted as a different identifier type.",
    33: "Exact-name and middle-initial searches found no reliable wartime identity, employer, occupation, institutional or OSS bridge.",
    37: "A same-name lifespan lead lacked the indexed middle initial, OSS context, employer evidence and a Box 768 bridge.",
    39: "Exact-name and middle-initial searches found no defensible OSS, employer, occupation or archival identity bridge.",
    43: "Exact-name and middle-initial searches found no defensible OSS, employer, occupation or archival identity bridge.",
    46: "Exact-name and middle-initial searches found no defensible OSS, employer, occupation or archival identity bridge.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 767-768",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 462, rows 24-46; checked against layout-preserving text and a 300 dpi page render",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. Full protected identifiers remain private. Kenneth S. Templeton on page 463 row 1 was checked as the next boundary.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; seven reviewed Batch 944 candidates; protected identifiers withheld",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "No raw bulk row or full protected identifier is retained in public assets. Six exact-name identities were accepted. The William J. Techtmann candidate conflicts with the Army name and transfers no fields.",
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
            "access_date": "2026-10-28",
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
            "locator": "PDF physical pages 172-174 and 304; reviewed historical categories 3-06, 4-01, 7-36, 9-57 and 9-92",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "The four relevant pages were rendered at 220 dpi and visually inspected. Historical occupation labels identify neither employers nor workplaces.",
        },
        {
            "key": TCHOK_BIO,
            "stable_url": "https://www.slovenska-biografija.si/oseba/sbi1006590/",
            "archival_identifier": "Slovenska biografija record sbi1006590",
            "title": "Čok, Ivan Marija (1886-1948)",
            "author_creator": "Jurij Perovšek; Boris Sancin; Albert Rejec",
            "repository_publisher": "Slovenska akademija znanosti in umetnosti and ZRC SAZU",
            "publication_record_date": "2018; last revised 2018-07-28",
            "locator": "Names and occupations; Novi Slovenski biografski leksikon; Primorski slovenski biografski leksikon",
            "access_date": "2026-10-28",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Slovenska biografija",
            "rights_notes": "The institutional record explicitly gives Ivan M. Tchok as a name form, documents his legal practice and emigrant-association leadership, and cites a scholarly article about his OSS employment.",
        },
        {
            "key": STANFORD,
            "stable_url": "https://journalism.stanford.edu/125-years-journalism/1940s-better-defining-journalism-studies",
            "title": "The 1940s: Better defining journalism studies",
            "author_creator": "Stanford Journalism Program",
            "repository_publisher": "Stanford University",
            "locator": "Teaching section, faculty who taught in the 1940s",
            "access_date": "2026-10-28",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "125 Years of Journalism",
            "rights_notes": "The institutional history lists Darwin L. Teilhet for 1941-1942 and the course Procedures in Advertising. It does not establish the date or mechanism of his transition into OSS.",
        },
        {
            "key": TEILHET_BIO,
            "stable_url": "https://www.ebsco.com/research-starters/history/darwin-l-teilhet",
            "title": "Darwin L. Teilhet",
            "repository_publisher": "EBSCO",
            "locator": "Biography section",
            "access_date": "2026-10-28",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "EBSCO Research Starters",
            "rights_notes": "The biography gives the full name Darwin LeOra Teilhet, documents his Stanford teaching and states that he served as a wartime intelligence officer. Stanford supplies the direct employment evidence.",
        },
        {
            "key": OSU_1938,
            "stable_url": "https://trustees.osu.edu/sites/default/files/documents/2018/12/1937-38.pdf",
            "archival_identifier": "Ohio State University Board of Trustees record of proceedings, 1937-1938",
            "title": "Record of Proceedings of the Board of Trustees of the Ohio State University, 1937-1938",
            "author_creator": "Board of Trustees of the Ohio State University",
            "repository_publisher": "The Ohio State University",
            "publication_record_date": "1938-01-21",
            "locator": "PDF page numbered 165; College of Commerce and Administration, Sociology",
            "access_date": "2026-10-28",
            "source_quality": "A_direct_official",
            "collection_name": "Ohio State University Board of Trustees records",
            "rights_notes": "The official record identifies Ina Telberg as a Sociology graduate assistant for the winter quarter. It is direct employment evidence but does not prove immediate pre-OSS chronology.",
        },
        {
            "key": NZ_LISTENER,
            "stable_url": "https://paperspast.natlib.govt.nz/periodicals/NZLIST19490909.2.13",
            "archival_identifier": "New Zealand Listener, 9 September 1949, item NZLIST19490909.2.13",
            "title": "They Don't Do It Our Way",
            "author_creator": "Ina Telberg",
            "repository_publisher": "New Zealand Listener; National Library of New Zealand Papers Past",
            "publication_record_date": "1949-09-09",
            "locator": "Author introduction preceding the article",
            "access_date": "2026-10-28",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Papers Past: New Zealand Listener",
            "rights_notes": "The contemporary introduction identifies Telberg as a former Ohio State sociology and anthropology instructor and states that she served with OSS in Washington and India.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": SELF_EMPLOYED_LEGAL,
            "organization_id": "b38d4d4f-f70c-5ab9-b3ac-59a5e9892f1f",
            "canonical_name": "Self-employed legal practice",
            "historical_name": "private law practice",
            "aliases": ["private practice", "self-employed attorney"],
            "organization_type": "self-employment",
            "sector": "self_employed",
            "normalization_notes": "Existing canonical organization reused. No law firm is named in the reviewed source.",
        },
        {
            "key": ZVEZA,
            "canonical_name": "Zveza jugoslovanskih emigrantov iz Julijske krajine",
            "historical_name": "Zveza jugoslovanskih emigrantov iz Julijske krajine",
            "aliases": [],
            "organization_type": "emigrant association",
            "sector": "labor_nonprofit_and_religion",
            "country": "Yugoslavia",
            "active_dates": "1931-1940 under Ivan M. Čok's documented presidency",
            "normalization_notes": "Historical Slovenian name retained; no modern successor or English legal name is substituted.",
        },
        {
            "key": STANFORD_ORG,
            "organization_id": "63b7b9f4-ee2a-51b3-b83a-d483901bdc38",
            "canonical_name": "Stanford University",
            "historical_name": "Stanford University",
            "aliases": [],
            "organization_type": "private university",
            "sector": "academia_and_research",
            "city": "Stanford",
            "state_or_region": "California",
            "country": "United States",
            "normalization_notes": "Existing canonical organization reused; the Journalism Program supplies the historical teaching record.",
        },
        {
            "key": OHIO_STATE,
            "organization_id": "de52c90c-62bc-532e-a99e-a7d9ca019c09",
            "canonical_name": "The Ohio State University",
            "historical_name": "Ohio State University",
            "aliases": ["Ohio State University"],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "Columbus",
            "state_or_region": "Ohio",
            "country": "United States",
            "normalization_notes": "Existing canonical organization reused; the historical source omits the initial article in the modern name.",
        },
    ]


def army_affiliation(item: dict[str, object]) -> dict[str, object]:
    row = int(item["row"])
    name = PEOPLE[row][1]
    return {
        "key": f"{slug(name)}-occupation-b944",
        "person_id": PEOPLE[row][0],
        "occupation": item["public_occupation"],
        "relationship_type": item.get("relationship", "employment"),
        "end_date": item["date"],
        "date_precision": f"Historical civilian-occupation code {item['code']} was recorded at Army entry on {item['date']}; no employer, school or OSS-transfer date is named.",
        "country": "United States",
        "immediate_pre_oss": False,
        "last_civilian_pre_service": False,
        "pre_oss_temporal_basis": "strongly_date_bounded",
        "identity_confidence": "high_confidence",
        "claim_confidence": "medium",
        "source_quality": "A_direct_official",
        "publication_status": "publish_qualified",
        "research_notes": "The historical category is not converted into a named employer, workplace, school, immediate affiliation or exact modern job title.",
    }


def affiliations() -> list[dict[str, object]]:
    values = [army_affiliation(item) for item in ARMY_OCCUPATIONS]
    values.extend(
        [
            {
                "key": "ivan-tchok-legal-practice-b944",
                "person_id": PEOPLE[24][0],
                "organization_key": SELF_EMPLOYED_LEGAL,
                "organization_name_as_found": "advokatura v Trstu",
                "role_title": "attorney in private practice",
                "occupation": "attorney",
                "relationship_type": "self_employment",
                "start_date": "1911",
                "end_date": "1928",
                "date_precision": "The biography says Tchok entered legal practice after his 1911 doctorate and could no longer practice after the 1928 prosecution; it does not name a firm.",
                "city": "Trieste",
                "country": "Italy",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "An earlier documented occupation and self-employment relationship, not the immediate predecessor to OSS.",
            },
            {
                "key": "ivan-tchok-zveza-b944",
                "person_id": PEOPLE[24][0],
                "organization_key": ZVEZA,
                "organization_name_as_found": "Zveza jugoslovanskih emigrantov iz Julijske krajine",
                "role_title": "president",
                "relationship_type": "professional_affiliation",
                "start_date": "1931",
                "end_date": "1940",
                "date_precision": "The institutional biography gives his presidency from the association's 1931 formation until its dissolution by the Yugoslav government in 1940.",
                "country": "Yugoslavia",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Documented political and emigrant-association leadership; it is not labeled employment or the immediate OSS predecessor.",
            },
            {
                "key": "darwin-teilhet-stanford-b944",
                "person_id": PEOPLE[34][0],
                "organization_key": STANFORD_ORG,
                "organization_name_as_found": "Stanford University",
                "role_title": "journalism instructor; Procedures in Advertising",
                "occupation": "teacher",
                "relationship_type": "employment",
                "start_date": "1941",
                "end_date": "1942",
                "date_precision": "Stanford's Journalism Program lists Darwin L. Teilhet among faculty who taught in 1941-1942 and associates him with Procedures in Advertising.",
                "city": "Stanford",
                "state_or_region": "California",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "B_authoritative_institutional",
                "publication_status": "published",
                "research_notes": "Close prewar teaching employment, but no reviewed source proves it was the final civilian role or explicitly links the end date to OSS entry.",
            },
            {
                "key": "ina-telberg-ohio-state-b944",
                "person_id": PEOPLE[35][0],
                "organization_key": OHIO_STATE,
                "organization_name_as_found": "Ohio State University",
                "role_title": "graduate assistant; later described as instructor in sociology and anthropology",
                "occupation": "sociology teaching and research",
                "relationship_type": "employment",
                "start_date": "1938",
                "end_date": "1938",
                "date_precision": "The trustees' record identifies a winter-quarter 1938 graduate assistant appointment; a 1949 contemporary introduction describes her as a former instructor.",
                "city": "Columbus",
                "state_or_region": "Ohio",
                "country": "United States",
                "immediate_pre_oss": False,
                "last_civilian_pre_service": False,
                "pre_oss_temporal_basis": "documented_prewar",
                "identity_confidence": "high_confidence",
                "claim_confidence": "high",
                "source_quality": "A_direct_official",
                "publication_status": "published",
                "research_notes": "Direct prewar university employment. The five-year gap before her reported 1943 OSS service prevents an immediate or last-employer designation.",
            },
        ]
    )
    return values


def claim(
    row: int,
    key: str,
    claim_type: str,
    text: str,
    paraphrase: str,
    identity: str,
    temporal: str,
    quality: str,
    confidence: str,
    source_links: list[dict[str, object]],
    notes: str,
    affiliation_key: str | None = None,
    publication_status: str | None = None,
) -> dict[str, object]:
    result: dict[str, object] = {
        "key": key,
        "person_id": PEOPLE[row][0],
        "claim_type": claim_type,
        "claim_text": text,
        "evidence_paraphrase": paraphrase,
        "identity_match_assessment": identity,
        "temporal_assessment": temporal,
        "source_quality": quality,
        "claim_confidence": confidence,
        "publication_status": publication_status
        or ("published" if confidence in {"confirmed", "high"} else "publish_qualified"),
        "match_notes": notes,
        "sources": source_links,
    }
    if affiliation_key:
        result["affiliation_key"] = affiliation_key
    return result


def army_claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for item in ARMY_OCCUPATIONS:
        row = int(item["row"])
        name = PEOPLE[row][1]
        values.append(
            claim(
                row,
                f"identity-{slug(name)}-b944",
                "identity",
                f"The indexed {name} row is a high-confidence match to the reviewed official Army record.",
                "A nonshared protected identifier connects the visually verified index row to the official Army record, and the full name agrees exactly.",
                "High confidence from the private protected-identifier bridge and exact full-name agreement.",
                "The record supports identity and a dated occupation or student-status category but does not establish the OSS transfer sequence.",
                "A_direct_official",
                "high",
                [
                    {"source_key": INDEX, "locator_override": f"PDF page 462 row {row}; protected identifier withheld"},
                    {"source_key": ARMY, "locator_override": "Accepted reviewed identity bridge; protected identifier withheld"},
                ],
                "No protected identifier is exposed, and no employer, workplace or school is inferred from the identity bridge.",
            )
        )
        values.append(
            claim(
                row,
                f"occupation-{slug(name)}-b944",
                "occupation",
                f"At Army entry on {item['date']}, {name} was recorded in the historical {str(item['public_occupation']).lower()} category; no employer or institution is identified.",
                f"The accepted Army record carries civilian-occupation code {item['code']}, decoded from NARA's official code list.",
                "The category belongs only to the reviewed protected-identifier match; the identifier itself is not public.",
                "Strongly date-bounded to Army entry; it does not establish the immediate pre-OSS affiliation or a named employer or school.",
                "A_direct_official",
                "medium",
                [
                    {"source_key": ARMY, "locator_override": f"Accepted reviewed identity record; civilian occupation code {item['code']}; protected identifier withheld"},
                    {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46; Army-entry-date and civilian-occupation fields"},
                    {"source_key": CODES, "locator_override": item["locator"], "excerpt_override": item["occupation"]},
                ],
                "The historical category remains a qualified occupation or status lead, not an employer, workplace, institution or exact modern title.",
                f"{slug(name)}-occupation-b944",
            )
        )
    return values


def substantive_claims() -> list[dict[str, object]]:
    return [
        claim(
            28,
            "conflict-william-j-techtmann-army-b944",
            "identity",
            "The indexed William J. Techtmann row is not assigned to the reviewed Robert J. Mertes Army record despite the private identifier collision.",
            "The protected identifier points to an Army record with a completely different surname and first name, so no Army field is transferred.",
            "Conflicting: the private identifier agrees but the full name materially disagrees.",
            "No Army occupation, grade or affiliation is transferred until the Box 768 file and source records resolve the collision.",
            "A_direct_official",
            "conflicting",
            [
                {"source_key": INDEX, "locator_override": "PDF page 462 row 28; protected identifier withheld"},
                {"source_key": ARMY, "support_type": "contradicts", "locator_override": "Reviewed candidate prints Robert J Mertes; protected identifier withheld"},
            ],
            "The conflict remains visible and is not silently corrected, rejected or used as biographical evidence.",
            publication_status="conflicting",
        ),
        claim(
            24,
            "identity-ivan-m-tchok-b944",
            "identity",
            "Indexed Ivan M. Tchok is a high-confidence match to Slovenian attorney and political organizer Ivan Marija Čok.",
            "The institutional biographical record explicitly gives Ivan M. Tchok as a name form and cites scholarship on his OSS employment.",
            "High confidence from the rare exact indexed name form, full-name expansion, matching wartime context and explicit OSS-employment bibliography.",
            "The biography documents prewar work and wartime movements but does not specify the precise OSS entry date.",
            "B_authoritative_institutional",
            "high",
            [
                {"source_key": INDEX, "locator_override": "PDF page 462 row 24"},
                {"source_key": TCHOK_BIO, "locator_override": "Names; bibliography", "excerpt_override": "Ivan M. Tchok"},
            ],
            "The original indexed spelling remains primary; Ivan Marija Čok and Miček are preserved as documented variants.",
        ),
        claim(
            24,
            "prewar-ivan-tchok-legal-b944",
            "other_pre_oss_affiliation",
            "Ivan Marija Čok practiced law privately in Trieste from after his 1911 doctorate until fascist repression prevented continued practice in 1928.",
            "The institutional biography states that he entered legal practice after completing his doctorate and later could no longer practice after the 1928 case.",
            "High-confidence identity from the exact Tchok name form and rare biographical alignment.",
            "Documented earlier prewar self-employment; not shown to be the immediate or last civilian role before OSS.",
            "B_authoritative_institutional",
            "high",
            [
                {"source_key": TCHOK_BIO, "locator_override": "Novi and Primorski biographical entries", "excerpt_override": "Po promociji se je posvetil advokaturi v Trstu"},
            ],
            "No firm is named, so the relationship is normalized only as self-employed legal practice.",
            "ivan-tchok-legal-practice-b944",
        ),
        claim(
            24,
            "prewar-ivan-tchok-zveza-b944",
            "other_pre_oss_affiliation",
            "Ivan Marija Čok led the Zveza jugoslovanskih emigrantov iz Julijske krajine from 1931 until its dissolution in 1940.",
            "The institutional biography documents his election as president at the association's formation and his continued leadership until 1940.",
            "High-confidence identity from the exact Tchok alias and detailed chronology.",
            "Documented prewar professional and political affiliation; not proven to be employment or the immediate predecessor to OSS.",
            "B_authoritative_institutional",
            "high",
            [
                {"source_key": TCHOK_BIO, "locator_override": "Summary and Primorski biographical entry", "excerpt_override": "V tridesetih letih 20. stoletja je vodil Zvezo jugoslovanskih emigrantov iz Julijske krajine."},
            ],
            "The historical Slovenian organization name is preserved without substituting a modern successor.",
            "ivan-tchok-zveza-b944",
        ),
        claim(
            34,
            "identity-darwin-l-teilhet-b944",
            "identity",
            "Indexed Darwin L. Teilhet is a high-confidence match to writer, Stanford instructor and wartime intelligence officer Darwin LeOra Teilhet.",
            "The distinctive exact indexed name is supported by Stanford's 1941-1942 teaching record and a scholarly biography documenting his wartime intelligence service.",
            "High confidence from the rare exact full name, matching prewar Stanford record and wartime intelligence chronology.",
            "The sources establish prewar teaching and wartime intelligence service but do not state the exact OSS entry date.",
            "B_authoritative_institutional",
            "high",
            [
                {"source_key": INDEX, "locator_override": "PDF page 462 row 34"},
                {"source_key": STANFORD, "locator_override": "Teaching section"},
                {"source_key": TEILHET_BIO, "locator_override": "Biography section"},
            ],
            "Darwin LeOra Teilhet is preserved as a documented full-name variant. No unverified military rank is assigned.",
        ),
        claim(
            34,
            "prewar-darwin-teilhet-stanford-b944",
            "other_pre_oss_affiliation",
            "Darwin L. Teilhet taught Procedures in Advertising at Stanford University during 1941-1942.",
            "Stanford's Journalism Program lists him among faculty who taught in the 1940s and supplies the dates and course title.",
            "High-confidence identity from the distinctive exact name and mutually reinforcing wartime biography.",
            "Documented close prewar employment; not proven to be the final civilian employer or immediate OSS predecessor.",
            "B_authoritative_institutional",
            "high",
            [
                {"source_key": STANFORD, "locator_override": "Teaching section", "excerpt_override": "Darwin L. Teilhet, 1941-1942, Procedures in Advertising"},
                {"source_key": TEILHET_BIO, "support_type": "context_only", "locator_override": "Biography section; wartime intelligence officer"},
            ],
            "Stanford is published as documented employment, while chronology beyond the stated academic years remains qualified.",
            "darwin-teilhet-stanford-b944",
        ),
        claim(
            35,
            "identity-ina-telberg-b944",
            "identity",
            "Indexed Ina Telberg is a high-confidence match to the Ohio State sociologist who served with OSS in Washington and India.",
            "A contemporary article introduction supplies the exact rare name, former Ohio State role and direct OSS service; the university trustees record corroborates the prewar appointment.",
            "High confidence from the rare exact name, direct contemporary OSS statement and independent official university employment record.",
            "The sources establish 1938 university work and wartime OSS service, but not an uninterrupted chronology or immediate predecessor.",
            "C_reputable_contemporary_or_scholarly",
            "high",
            [
                {"source_key": INDEX, "locator_override": "PDF page 462 row 35"},
                {"source_key": NZ_LISTENER, "locator_override": "Author introduction"},
                {"source_key": OSU_1938, "locator_override": "PDF page numbered 165"},
            ],
            "No postwar loyalty-investigation allegations or unrelated sensitive personal data are reproduced.",
        ),
        claim(
            35,
            "prewar-ina-telberg-ohio-state-b944",
            "other_pre_oss_affiliation",
            "Ina Telberg held a 1938 sociology graduate-assistant appointment at Ohio State University and was later described as a former sociology and anthropology instructor there.",
            "The trustees' appointment record and a contemporary biographical introduction independently document her university role.",
            "High-confidence identity from the rare exact name and explicit OSS service in the contemporary introduction.",
            "Documented prewar employment; the interval before reported 1943 OSS service prevents an immediate or last-employer designation.",
            "A_direct_official",
            "high",
            [
                {"source_key": OSU_1938, "locator_override": "PDF page numbered 165; Sociology", "excerpt_override": "Ina Telberg — Graduate Assistant — Wi. Qr. only"},
                {"source_key": NZ_LISTENER, "locator_override": "Author introduction", "excerpt_override": "formerly instructor in the Department of Sociology and Anthropology in the Ohio State University"},
            ],
            "The historical source wording is preserved; no specific later university position or continuous tenure is inferred.",
            "ina-telberg-ohio-state-b944",
        ),
    ]


def archival_update(row: int, reason: str) -> dict[str, object]:
    person_id, name = PEOPLE[row]
    return {
        "person_id": person_id,
        "identity_status": "unresolved",
        "identity_evidence": f"The visually verified index row supplies {name}, Box 768 and archive location 230/86/41/07. {reason}",
        "personnel_category": "unknown_or_indeterminate",
        "manual_review_required": True,
        "research_status": "requires_archival_review",
        "next_action": "Review Box 768 for corroborating identifiers and the last documented pre-OSS affiliation. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        "personnel_file_digitized": False,
        "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }


def person_updates() -> list[dict[str, object]]:
    updates = [archival_update(row, reason) for row, reason in UNRESOLVED.items()]
    army_rows = {int(item["row"]) for item in ARMY_OCCUPATIONS}
    for row in sorted(army_rows):
        updates.append(
            {
                "person_id": PEOPLE[row][0],
                "identity_status": "high_confidence",
                "identity_evidence": "A nonshared protected identifier connects the visually verified index row to the reviewed official Army record, and the full name agrees exactly.",
                "personnel_category": "enlisted_army_personnel",
                "commissioned_officer": False,
                "allied_or_foreign_personnel": False,
                "manual_review_required": True,
                "research_status": "occupation_only_found",
                "next_action": "Review Box 768 to establish the immediate pre-OSS affiliation and named last civilian employer; do not convert the Army occupation or student-status category into a workplace or institution.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            }
        )
    updates.extend(
        [
            {
                "person_id": PEOPLE[27][0],
                "identity_status": "ambiguous",
                "identity_evidence": "Léon Téboul, an industrialist and French resistance organizer, is a plausible spelling-variant lead, but no source connects that person to the indexed Leo Teboul, OSS, Box 768 or a shared identifier.",
                "personnel_category": "unknown_or_indeterminate",
                "manual_review_required": True,
                "research_status": "needs_identity_review",
                "next_action": "Review Box 768 for birth date, nationality, aliases and assignment before adopting the Léon Téboul resistance biography or its industrial occupation.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[28][0],
                "identity_status": "conflicting",
                "identity_evidence": "The index prints William J. Techtmann, while the reviewed Army row linked by the private identifier prints Robert J. Mertes. The collision is preserved and no Army fields are transferred.",
                "personnel_category": "unknown_or_indeterminate",
                "manual_review_required": True,
                "research_status": "conflicting_sources",
                "next_action": "Review the Box 768 personnel file and the original Army source together to resolve the identifier/name collision before assigning any occupation or affiliation.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[36][0],
                "identity_status": "ambiguous",
                "identity_evidence": "Telemachus George Anastos is a plausible transposed-name candidate who served in the U.S. Navy from 1942 to 1946, but the index prints surname Telemachus and first name Anastos and supplies no corroborating identifier.",
                "personnel_category": "unknown_or_indeterminate",
                "manual_review_required": True,
                "research_status": "needs_identity_review",
                "next_action": "Review Box 768 for name order, birth date and Navy identifiers before adopting the Telemachus George Anastos biography.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[38][0],
                "identity_status": "ambiguous",
                "identity_evidence": "A distinctive Aram H. Tellalian candidate ran for the Connecticut legislature in Bridgeport in 1936, but the election record provides no OSS, Box 768 or wartime identifier bridge to the indexed row.",
                "personnel_category": "unknown_or_indeterminate",
                "manual_review_required": True,
                "research_status": "needs_identity_review",
                "next_action": "Review Box 768 for suffix, birth date, hometown, profession and service identifiers before assigning the Connecticut political or legal biography.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "critical",
            },
            {
                "person_id": PEOPLE[24][0],
                "identity_status": "high_confidence",
                "identity_evidence": "The Slovenian Academy and ZRC SAZU biographical record explicitly gives Ivan M. Tchok as a name form for Ivan Marija Čok and cites scholarship on his OSS employment.",
                "name_variants": ["Ivan Marija Čok", "Ivan M. Čok", "Miček"],
                "personnel_category": "civilian_professional_or_administrative_grade",
                "commissioned_officer": False,
                "manual_review_required": True,
                "research_status": "documented_prewar_employer_found",
                "next_action": "Review Box 767 to establish the precise OSS entry chronology and determine whether his 1931-1940 association presidency or a later government role was the immediate predecessor.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[34][0],
                "identity_status": "high_confidence",
                "identity_evidence": "The distinctive exact name aligns across the index, Stanford's 1941-1942 faculty record and a scholarly biography describing Darwin LeOra Teilhet's wartime intelligence service.",
                "name_variants": ["Darwin LeOra Teilhet"],
                "personnel_category": "unknown_or_indeterminate",
                "manual_review_required": True,
                "research_status": "documented_prewar_employer_found",
                "next_action": "Review Box 768 for service status, OSS entry date and chronology needed to determine whether Stanford was his immediate or last civilian employer.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
            {
                "person_id": PEOPLE[35][0],
                "identity_status": "high_confidence",
                "identity_evidence": "A contemporary article identifies the rare exact-name Ina Telberg as a former Ohio State instructor who served with OSS in Washington and India; an official trustees record independently corroborates her 1938 appointment.",
                "name_variants": ["Ina Georgievna Telberg"],
                "personnel_category": "civilian_professional_or_administrative_grade",
                "commissioned_officer": False,
                "manual_review_required": True,
                "research_status": "documented_prewar_employer_found",
                "next_action": "Review Box 768 to establish her employment from 1939 through OSS entry and whether Ohio State or an intervening role was the last civilian employer.",
                "personnel_file_digitized": False,
                "personnel_file_reviewed": False,
                "archival_review_priority": "high",
            },
        ]
    )
    return updates


def research_attempts() -> list[dict[str, object]]:
    army_rows = {int(item["row"]) for item in ARMY_OCCUPATIONS}
    ambiguous_rows = {27, 36, 38}
    strong_rows = {24, 34, 35}
    attempts: list[dict[str, object]] = []
    for row in sorted(PEOPLE):
        if row == 45:
            continue
        person_id, name = PEOPLE[row]
        if row in UNRESOLVED:
            outcome, reviewed, rejected, detail = "no_result", 4, 4, UNRESOLVED[row]
        elif row in army_rows:
            outcome, reviewed, rejected, detail = "source_reviewed", 7, 4, "An accepted protected-identifier Army bridge supports identity and a dated historical occupation or student-status category, not an employer or institution."
        elif row == 28:
            outcome, reviewed, rejected, detail = "candidate_found", 7, 5, "The protected identifier points to Robert J. Mertes while the index prints William J. Techtmann; the conflict is preserved and no Army fields are transferred."
        elif row in ambiguous_rows:
            outcome, reviewed, rejected = "candidate_found", 6, 5
            if row == 27:
                detail = "The Léon Téboul industrialist and resistance biography lacks an OSS, spelling, identifier or Box 768 bridge to indexed Leo Teboul."
            elif row == 36:
                detail = "Telemachus George Anastos is a plausible transposed-name Navy candidate, but the index order and absence of a second identifier prevent assignment."
            else:
                detail = "The 1936 Connecticut candidate Aram H. Tellalian lacks a wartime or Box 768 bridge, so no political or legal affiliation is published."
        elif row in strong_rows:
            outcome, reviewed, rejected = "source_reviewed", 9, 4
            if row == 24:
                detail = "An authoritative Slovenian institutional biography supports the Ivan M. Tchok/Ivan Marija Čok identity, earlier private legal practice and 1931-1940 emigrant-association leadership."
            elif row == 34:
                detail = "Stanford directly documents 1941-1942 teaching employment; a scholarly biography and the rare exact name support identity, while immediate chronology remains unresolved."
            else:
                detail = "An official Ohio State appointment record and a contemporary article independently document Ina Telberg's prewar university work and direct OSS service."
        else:
            raise AssertionError(f"Missing Batch 944 outcome for row {row}")
        attempts.append(
            {
                "key": f"page462-row{row}-{slug(name)}-b944",
                "person_id": person_id,
                "source_adapter": "manual_staged_protocol",
                "query_text": f"{name}; NARA index and public Archives context; CIA Reading Room; exact-name and meaningful variants; OSS, rank and military clues; employer and occupation 1940; obituary, institutional, newspaper, directory, Library of Congress and archival searches; Boxes 767-768; protected identifiers used privately only when defensible",
                "query_variant_type": "staged_identity_employment_archival_protocol_batch_944",
                "started_at": "2026-10-28T21:00:00Z",
                "completed_at": "2026-10-29T00:15:00Z",
                "outcome": outcome,
                "sources_reviewed": reviewed,
                "candidate_sources_rejected": rejected,
                "rejection_reasons": "Unbridged namesakes, search snippets, family-tree assertions, modern people-finder pages, postwar-only leads and sources without an OSS, protected-identifier or Box-file bridge were not assigned.",
                "research_notes": f"{detail} The index page and admitted Army code-list pages were visually checked. No search-result snippet was used as sole final evidence, no access control was bypassed, and no authenticated NARA Catalog API call was made.",
                "next_action": "Review the indexed personnel file for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before wartime service.",
                "attempt_number": 1,
                "research_agent_version": "before-oss-b944-v1",
            }
        )
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-944-v1",
        "reviewer": "Before OSS Batch 944 evidence review",
        "sources": sources(),
        "organizations": organizations(),
        "affiliations": affiliations(),
        "claims": army_claims() + substantive_claims(),
        "person_updates": person_updates(),
        "research_attempts": research_attempts(),
    }
    EvidenceBundle.model_validate(bundle)
    OUTPUT.write_text(
        json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
