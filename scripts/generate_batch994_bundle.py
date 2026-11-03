#!/usr/bin/env python3
"""Generate the reviewed Batch 994 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / (
    "research/evidence-page487-waite-to-walk-"
    "review_batch-994_2026-11-03.json"
)

INDEX = "nara-index-b994"
ARMY = "army-bulk-b994"
TECH = "army-tech-b994"
CODES = "army-codes-b994"
AWM = "awm-nancy-wake-b994"
YALE = "yale-eugene-waith-b994"
USNI = "usni-george-walbridge-b994"
GAGOSIAN = "gagosian-patrick-waldberg-b994"
MED = "med-dept-herbert-waldhorn-b994"
NYMM = "ny-military-maturin-waldo-b994"

ORG_YALE = "yale-university-b994"
ORG_ARMY = "us-army-b994"
ORG_HEARST = "hearst-newspapers-b994"
ORG_RESISTANCE = "french-resistance-b994"
ORG_SOE = "soe-b994"
ORG_NAVY = "us-navy-b994"
ORG_RCAF = "rcaf-b994"
ORG_OWI = "owi-b994"
ORG_FRENCH_ARMY = "french-army-b994"
ORG_74GH = "74th-general-hospital-b994"
ORG_101CAV = "101st-cavalry-b994"


PEOPLE = {
    24: ("30250cf6-d13f-56cc-b743-c639b9120535", "Wilma Isabel Waite"),
    25: ("0556f56a-4bdf-5b63-af67-4f0629913e00", "Eugene Merse Waith"),
    26: ("564b2773-158c-57e3-8e81-5895472d7d6d", "Henry S Wakabayashi"),
    27: ("b0e63804-da34-5d6e-a559-54e8bc27a9d3", "Nancy Wake"),
    28: ("a45a141e-4073-5be4-a732-a9e38728c831", "Richard P Wakefield"),
    29: ("dbec9a7e-ed97-59bb-af82-7a3034cbe822", "Arthur Francis Walber"),
    30: ("a8860eb7-afc7-5794-a905-342135ea2d22", "Charles R Walbert"),
    31: ("cf66a9eb-8b52-5e53-99d6-83f98ef83371", "George O Walbridge"),
    32: ("48a25f31-02b3-5b89-bb49-45eb86e6fb6d", "Albert R Walcott"),
    33: ("626accf6-7831-58fd-8cb0-0f6698ecdee8", "Patrick K.C. Waldberg"),
    34: ("589acaac-0166-569b-a562-cdf5874509d9", "Carl O Walden"),
    35: ("3ca1371b-4df5-5f7a-97b6-f5799089d618", "James E Walden"),
    36: ("aca20a31-be9d-514c-8971-7b753de5cc51", "Herbert F Waldhorn"),
    37: ("87af7bcc-1d6f-5870-96fa-87a2ab2778e2", "Robert G Waldman"),
    38: ("aa96ec67-10e8-5dfc-89bb-e8433076bf1d", "Maturin F Waldo"),
    39: ("cc40a1b0-633e-5130-8d49-07e45610864a", "Phyllis H Waldo"),
    40: ("64650a84-e326-5e9d-b3f8-c63c1a95202f", "Henry H Waldon"),
    41: ("502814b4-df38-5b53-ab06-c9ba62dcbc5f", "Arthur Leonard Waldo-Stefans"),
    42: ("ae88568f-37ac-58d6-9ab8-6db3262e3d81", "Howard T Waldron"),
    43: ("adc91fda-fcf0-528e-b9e7-03951e0a24e0", "James Waldron"),
    44: ("3b16058e-9339-533b-a096-14304185c887", "John Waldron"),
    45: ("9debd6e3-7228-5e20-8735-277c7704a997", "Thomas H Waldron"),
    46: ("6602744c-b6d8-5828-8a48-e3b5d695f6f7", "Everett G Walk"),
}

UNRESOLVED = {
    24: "Exact-name, OSS, employer, occupation, obituary, institutional, newspaper and archival searches produced no reliable identity bridge.",
    26: "A 1995 Congressional Record index names a Japanese-American Veterans Association representative, but it does not establish that he is the indexed wartime person or document pre-OSS work.",
    29: "The distinctive full name produced no source with an OSS, protected-identifier, employer or personnel-file bridge.",
    30: "Exact-name and spelling-variant searches produced no source with an OSS, protected-identifier, employer or personnel-file bridge.",
    32: "Common-name searches produced no source with the middle initial, indexed identifier or a direct OSS assignment bridge.",
    37: "The index note is incomplete, and common-name searches produced no source with the indexed identifier or a direct OSS bridge.",
    39: "Exact-name, OSS, occupation, obituary, institutional and archival searches produced no reliable result.",
    40: "Rank-aware and exact-name searches produced no source with the indexed identifier or a direct OSS assignment bridge.",
    41: "The visually verified hyphenated surname produced no source with an OSS, employer, occupation or personnel-file bridge.",
    42: "Common-name searches produced no source with the middle initial, indexed identifier or a direct OSS assignment bridge.",
    44: "Official records document an OSS historian named Dr. John Waldron, but the common indexed name has no middle name, rank or identifier linking that biography to this row.",
    45: "Common-name searches produced no source with the middle initial, indexed identifier or a direct OSS assignment bridge.",
    46: "Exact-name and initial-variant searches produced no source with an OSS, protected-identifier, employer or personnel-file bridge.",
}

ARMY_OCCUPATIONS = {
    28: ("1943-03-11", "002", "actors and actresses"),
    38: ("1941-03-29", "068", "semiprofessional occupations, n.e.c."),
    43: ("1945-03-07", "266", "policemen and detectives, public service"),
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 811-812 and 815",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 487, rows 24-46; checked against layout-preserving text and an original-detail page render",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. Protected identifiers remain private. PDF page 488 row 1, Richard D Walk, is outside this cohort and begins the next batch.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; three accepted protected-identifier comparisons; identifiers and record ordinals withheld",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "Three records were accepted after exact protected-identifier comparison. Carl O. Walden and James E. Walden share one indexed identifier, received no bulk match and remain separate conflicting rows.",
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
            "access_date": "2026-11-03",
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
            "locator": "Historical civilian-occupation categories 0-02, 0-68 and 2-66",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "Historical labels identify broad occupations, not named employers, agencies, productions, workplaces or exact OSS-transfer dates.",
        },
        {
            "key": AWM,
            "stable_url": "https://www.awm.gov.au/collection/P332",
            "archival_identifier": "Australian War Memorial person record P332",
            "title": "Nancy Grace Augusta Wake",
            "author_creator": "Australian War Memorial",
            "repository_publisher": "Australian War Memorial",
            "locator": "Description and timeline",
            "access_date": "2026-11-03",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Australian War Memorial People collection",
            "rights_notes": "The record documents Hearst journalism, French Resistance work and SOE service. It does not itself document OSS employment or assignment.",
        },
        {
            "key": YALE,
            "stable_url": "https://news.yale.edu/2007/11/08/memoriam-eugene-m-waith-professor-english-literature",
            "title": "In Memoriam: Eugene M. Waith, Professor of English Literature",
            "author_creator": "Yale News",
            "repository_publisher": "Yale University",
            "publication_record_date": "2007-11-08",
            "locator": "Biographical paragraphs 79-95",
            "access_date": "2026-11-03",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "Yale News In Memoriam",
            "rights_notes": "The institutional biography explicitly documents the full name, 1939 Yale appointment, 1943-1946 Army service, promotion to first lieutenant and OSS counterintelligence service.",
        },
        {
            "key": USNI,
            "stable_url": "https://www.usni.org/people/george-o-walbridge",
            "title": "George O. Walbridge",
            "author_creator": "U.S. Naval Institute",
            "repository_publisher": "U.S. Naval Institute",
            "locator": "Author biography",
            "access_date": "2026-11-03",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "U.S. Naval Institute author biographies",
            "rights_notes": "The biography directly states RCAF service, 1942 U.S. Navy commissioning, MTB Ron 7 and MTB Ron 2 service, and OSS service after Normandy D-Day.",
        },
        {
            "key": GAGOSIAN,
            "stable_url": "https://gagosian.com/quarterly/2020/09/09/isabelle-waldberg/",
            "title": "Isabelle Waldberg",
            "author_creator": "Jacquelynn Baas",
            "repository_publisher": "Gagosian Quarterly",
            "publication_record_date": "2020-09-09",
            "locator": "Patrick Waldberg wartime chronology",
            "access_date": "2026-11-03",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "Gagosian Quarterly, Spring 2020 issue",
            "rights_notes": "Used for Patrick Waldberg's French infantry and Office of War Information chronology. The article does not mention OSS or the K.C. initials.",
        },
        {
            "key": MED,
            "stable_url": "https://www.med-dept.com/unit-histories/74th-general-hospital/",
            "title": "74th General Hospital Unit History",
            "author_creator": "WW2 US Medical Research Centre",
            "repository_publisher": "WW2 US Medical Research Centre",
            "locator": "1945 Neuropsychiatric Section and transfer roster",
            "access_date": "2026-11-03",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "collection_name": "WW2 US Medical Research Centre unit histories",
            "rights_notes": "The unit history reproduces an exact officer identifier that matches the index privately; the identifier remains excluded from public evidence.",
        },
        {
            "key": NYMM,
            "stable_url": "https://museum.dmna.ny.gov/unit-history/conflict/world-war-2-1939-1945/27th-infantry-division-world-war-two/27th-infantry-division-world-war-two-men-who-were-federalized-1940/27th-infantry-division-world-war-two-men-who-were-federalized-1940-last-names-beginning-w",
            "title": "27th Infantry Division World War Two Men Who Were Federalized In 1940: Last Names Beginning With W",
            "author_creator": "New York State Military Museum and Veterans Research Center",
            "repository_publisher": "New York State Division of Military and Naval Affairs",
            "locator": "Waldo, Maturin roster entry",
            "access_date": "2026-11-03",
            "source_quality": "B_authoritative_institutional",
            "collection_name": "New York National Guard service records",
            "rights_notes": "The roster's protected identifier independently agrees with the index and Army record; the identifier remains private.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {"key": ORG_YALE, "organization_id": "918dedde-f9d1-5db1-8304-5c218a06b9b5", "canonical_name": "Yale University", "historical_name": "Yale University", "aliases": [], "organization_type": "university", "sector": "academia_and_research", "city": "New Haven", "state_or_region": "Connecticut", "country": "United States", "normalization_notes": "Existing canonical university reused; this claim is employment, not student status."},
        {"key": ORG_ARMY, "organization_id": "28a26f92-78af-5a1a-9c09-a843eb5975b4", "canonical_name": "United States Army", "historical_name": "United States Army", "aliases": ["U.S. Army", "Army of the United States"], "organization_type": "armed service", "sector": "military", "country": "United States", "normalization_notes": "Existing canonical military organization reused."},
        {"key": ORG_HEARST, "canonical_name": "Hearst newspapers", "historical_name": "Hearst group of newspapers", "aliases": ["Hearst group"], "organization_type": "newspaper group", "sector": "journalism_and_media", "country": "United States", "normalization_notes": "The source's collective historical wording is preserved; no individual newspaper is inferred."},
        {"key": ORG_RESISTANCE, "organization_id": "bfd3056a-78bb-5827-a68a-c0fd2144b1db", "canonical_name": "French Resistance", "historical_name": "French Resistance", "aliases": ["Resistance", "Maquis"], "organization_type": "resistance movement", "sector": "military", "country": "France", "normalization_notes": "Existing broad historical resistance organization reused; recorded as volunteer service, not employment."},
        {"key": ORG_SOE, "organization_id": "b917eced-da73-5c67-8579-3fdacb16a31a", "canonical_name": "Special Operations Executive", "historical_name": "Special Operations Executive", "aliases": ["SOE"], "organization_type": "British wartime government organization", "sector": "federal_government", "country": "United Kingdom", "active_dates": "1940-1946", "normalization_notes": "Existing canonical wartime organization reused; not conflated with OSS."},
        {"key": ORG_NAVY, "organization_id": "3960fa8e-a551-56cf-8305-b2b9e4961b9d", "canonical_name": "United States Navy", "historical_name": "United States Navy", "aliases": ["U.S. Navy", "U.S. Naval Reserve"], "organization_type": "armed service", "sector": "military", "country": "United States", "normalization_notes": "Existing canonical military organization reused."},
        {"key": ORG_RCAF, "canonical_name": "Royal Canadian Air Force", "historical_name": "Royal Canadian Air Force", "aliases": ["RCAF"], "organization_type": "armed service", "sector": "military", "country": "Canada", "normalization_notes": "Historical service name preserved."},
        {"key": ORG_OWI, "organization_id": "c48b74b9-1a67-5480-bb47-8dd73d10abf4", "canonical_name": "Office of War Information", "historical_name": "American Office of War Information", "aliases": ["OWI"], "organization_type": "federal agency", "sector": "federal_government", "country": "United States", "active_dates": "1942-1945", "normalization_notes": "Existing canonical wartime agency reused; government assignment is not labeled civilian private employment."},
        {"key": ORG_FRENCH_ARMY, "organization_id": "f61aed47-47ad-5e11-82be-3835d1bc4365", "canonical_name": "French Army", "historical_name": "French infantry", "aliases": ["French infantry"], "organization_type": "armed service", "sector": "military", "country": "France", "normalization_notes": "Existing canonical French military organization reused."},
        {"key": ORG_74GH, "canonical_name": "74th General Hospital", "historical_name": "74th General Hospital", "aliases": ["74th Gen Hosp"], "organization_type": "U.S. Army general hospital", "sector": "military", "country": "United States", "active_dates": "activated 1942", "normalization_notes": "Historical Army hospital unit kept distinct from modern institutions."},
        {"key": ORG_101CAV, "canonical_name": "101st Cavalry Regiment", "historical_name": "Troop E, 101st Cavalry", "aliases": ["101st Cavalry", "Troop E"], "organization_type": "National Guard cavalry regiment", "sector": "military", "state_or_region": "New York", "country": "United States", "normalization_notes": "The source's troop and regiment wording is preserved."},
    ]


def affiliation(key: str, row: int, relationship: str, temporal: str, identity: str, confidence: str, quality: str, publication: str, **kwargs: object) -> dict[str, object]:
    value: dict[str, object] = {
        "key": key,
        "person_id": PEOPLE[row][0],
        "relationship_type": relationship,
        "pre_oss_temporal_basis": temporal,
        "identity_confidence": identity,
        "claim_confidence": confidence,
        "source_quality": quality,
        "publication_status": publication,
    }
    value.update(kwargs)
    return value


def affiliations() -> list[dict[str, object]]:
    values = []
    for row, (date, code, occupation) in ARMY_OCCUPATIONS.items():
        values.append(affiliation(
            f"{slug(PEOPLE[row][1])}-army-occupation-b994", row, "employment", "strongly_date_bounded", "confirmed", "medium", "A_direct_official", "publish_qualified",
            occupation=occupation, end_date=date, date_precision=f"Historical civilian-occupation code {code} was recorded at Army entry on {date}; no named employer, agency, production or OSS-transfer date is supplied.", country="United States", immediate_pre_oss=False, last_civilian_pre_service=False, research_notes="Broad historical occupation category only; no named employer is inferred."
        ))
    values.extend([
        affiliation("eugene-waith-yale-b994", 25, "employment", "strongly_date_bounded", "high_confidence", "high", "B_authoritative_institutional", "published", organization_key=ORG_YALE, organization_name_as_found="Yale", role_title="Instructor in English", occupation="English literature scholar and teacher", start_date="1939", end_date="1943", date_precision="Yale appointed Waith in 1939 and says he interrupted teaching duties for Army service in 1943.", city="New Haven", state_or_region="Connecticut", country="United States", immediate_pre_oss=False, last_civilian_pre_service=True, research_notes="Explicit last civilian employment before Army service; not mislabeled as the immediate OSS institution."),
        affiliation("eugene-waith-army-b994", 25, "military_assignment", "strongly_date_bounded", "high_confidence", "high", "B_authoritative_institutional", "published", organization_key=ORG_ARMY, organization_name_as_found="United States Army", role_title="private; later first lieutenant and OSS counterintelligence officer", start_date="1943", end_date="1946", date_precision="Yale dates Army service to 1943-1946 and explicitly states promotion and OSS counterintelligence service in Europe.", country="United States", immediate_pre_oss=True, last_civilian_pre_service=False, research_notes="Military pathway into OSS; not a civilian employer."),
        affiliation("nancy-wake-hearst-b994", 27, "employment", "documented_prewar", "probable", "medium", "B_authoritative_institutional", "publish_qualified", organization_key=ORG_HEARST, organization_name_as_found="Hearst group of newspapers", role_title="journalist", occupation="journalist", end_date="1940", date_precision="The Australian War Memorial places Hearst journalism in Paris before Wake joined the Resistance after France's 1940 surrender; exact employment dates are not supplied.", city="Paris", country="France", immediate_pre_oss=False, last_civilian_pre_service=True, research_notes="Best-supported last civilian employer before Resistance and SOE service; identity remains probable because the source does not mention OSS."),
        affiliation("nancy-wake-resistance-b994", 27, "volunteer", "documented_prewar", "probable", "medium", "B_authoritative_institutional", "publish_qualified", organization_key=ORG_RESISTANCE, organization_name_as_found="Resistance", role_title="resistance organizer and courier", start_date="1940", end_date="1943-06", date_precision="The Memorial dates her Resistance work from France's 1940 surrender until escape to England in June 1943.", country="France", immediate_pre_oss=False, last_civilian_pre_service=False, research_notes="Volunteer resistance service, not employment."),
        affiliation("nancy-wake-soe-b994", 27, "government_assignment", "strongly_date_bounded", "probable", "medium", "B_authoritative_institutional", "publish_qualified", organization_key=ORG_SOE, organization_name_as_found="French Section of the Special Operations Executive", role_title="French Section operative; ensign in FANY", start_date="1943-06", end_date="1944-10", date_precision="The Memorial dates her arrival in England and SOE work to June 1943, France return to April 1944, and London headquarters return to October 1944.", country="United Kingdom and France", immediate_pre_oss=False, last_civilian_pre_service=False, research_notes="Documented British service. It is not silently converted into an OSS assignment or immediate OSS predecessor."),
        affiliation("george-walbridge-navy-b994", 31, "military_assignment", "strongly_date_bounded", "high_confidence", "high", "B_authoritative_institutional", "published", organization_key=ORG_NAVY, organization_name_as_found="U.S. Navy", role_title="ensign; MTB Ron 7 and MTB Ron 2 officer", start_date="1942", end_date="1944-06", date_precision="The Naval Institute dates commissioning to 1942 and states that OSS service followed Normandy D-Day.", country="United States", immediate_pre_oss=True, last_civilian_pre_service=False, research_notes="The Navy motor-torpedo-boat pathway is military service, not civilian employment."),
        affiliation("george-walbridge-rcaf-b994", 31, "military_assignment", "documented_prewar", "high_confidence", "high", "B_authoritative_institutional", "published", organization_key=ORG_RCAF, organization_name_as_found="Royal Canadian Air Force", role_title="service member", end_date="1942", date_precision="The Naval Institute says one year of RCAF service preceded his 1942 U.S. Navy commission.", country="Canada", immediate_pre_oss=False, last_civilian_pre_service=False, research_notes="Earlier Allied military service."),
        affiliation("patrick-waldberg-owi-b994", 33, "government_assignment", "temporal_relation_uncertain", "probable", "medium", "C_reputable_contemporary_or_scholarly", "publish_qualified", organization_key=ORG_OWI, organization_name_as_found="American Office of War Information", role_title="London assignment", start_date="1942-09", date_precision="The source dates marriage and departure for an OWI assignment to September 1942, then places work in London, North Africa and Paris.", city="London", country="United Kingdom", immediate_pre_oss=False, last_civilian_pre_service=False, research_notes="Documented wartime government assignment; the source does not establish its sequence relative to OSS or the indexed K.C. initials."),
        affiliation("patrick-waldberg-french-army-b994", 33, "military_assignment", "documented_prewar", "probable", "medium", "C_reputable_contemporary_or_scholarly", "publish_qualified", organization_key=ORG_FRENCH_ARMY, organization_name_as_found="French infantry", role_title="volunteer soldier", end_date="1940-08", date_precision="The source says Waldberg volunteered at war's onset, received the Croix de Guerre and was demobilized in August 1940.", country="France", immediate_pre_oss=False, last_civilian_pre_service=False, research_notes="Earlier military service, not employment."),
        affiliation("patrick-waldberg-writer-b994", 33, "self_employment", "documented_prewar", "probable", "medium", "C_reputable_contemporary_or_scholarly", "publish_qualified", occupation="writer and political activist", end_date="1939", date_precision="The source describes Patrick Waldberg as an American writer and political activist before the war without naming an employer.", city="Paris", country="France", immediate_pre_oss=False, last_civilian_pre_service=False, research_notes="Occupation only; self-employment form is qualified and no employer is invented."),
        affiliation("herbert-waldhorn-74gh-b994", 36, "military_assignment", "explicit_immediate", "confirmed", "confirmed", "C_reputable_contemporary_or_scholarly", "published", organization_key=ORG_74GH, organization_name_as_found="74th General Hospital", role_title="captain, Medical Corps; assistant chief of Neuropsychiatric Section", occupation="physician and neuropsychiatrist", start_date="1945-01", end_date="1945", date_precision="The unit history names him in the 1945 section and explicitly lists transfer to OSS headquarters; exact transfer day is not stated.", country="United Kingdom", immediate_pre_oss=True, last_civilian_pre_service=False, research_notes="Direct unit-to-OSS transfer. Protected officer identifier agrees privately and remains withheld."),
        affiliation("maturin-waldo-101cav-b994", 38, "military_assignment", "documented_prewar", "confirmed", "high", "B_authoritative_institutional", "published", organization_key=ORG_101CAV, organization_name_as_found="Troop E, 101st Cavalry", role_title="corporal", start_date="1938-03-29", end_date="1941-03-27", date_precision="The New York State roster explicitly gives the unit, rank and dates; Army entry followed two days later.", state_or_region="New York", country="United States", immediate_pre_oss=False, last_civilian_pre_service=False, research_notes="Earlier National Guard assignment; not claimed as the immediate OSS predecessor."),
    ])
    return values


def links(*keys: str) -> list[dict[str, str]]:
    return [{"source_key": key} for key in keys]


def claim(key: str, row: int, claim_type: str, text: str, paraphrase: str, identity: str, temporal: str, quality: str, confidence: str, publication: str, notes: str, source_links: list[dict[str, str]], affiliation_key: str | None = None) -> dict[str, object]:
    value: dict[str, object] = {"key": key, "person_id": PEOPLE[row][0], "claim_type": claim_type, "claim_text": text, "evidence_paraphrase": paraphrase, "identity_match_assessment": identity, "temporal_assessment": temporal, "source_quality": quality, "claim_confidence": confidence, "publication_status": publication, "match_notes": notes, "sources": source_links}
    if affiliation_key:
        value["affiliation_key"] = affiliation_key
    return value


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, (date, code, occupation) in ARMY_OCCUPATIONS.items():
        name = PEOPLE[row][1]
        identity_text = "The official index and Army bulk record agree in name and a nonshared protected identifier."
        if row == 43:
            identity_text = "The nonshared protected identifier links the index to the Army record, which supplies the middle initial A."
        values.extend([
            claim(f"identity-{slug(name)}-b994", row, "identity", f"Indexed {name} is confirmed as the reviewed official Army entry record.", identity_text, "Confirmed by direct protected-identifier agreement; the identifier and record ordinal remain private.", f"The Army record dates entry to {date} and supplies only historical civilian code {code}.", "A_direct_official", "confirmed", "published", "Identity only; no employer or exact OSS-transfer date is inferred.", links(INDEX, ARMY)),
            claim(f"occupation-{slug(name)}-b994", row, "occupation", f"At Army entry on {date}, {name} was recorded in the historical category {occupation}; no named employer is identified.", f"The accepted Army record carries civilian-occupation code {code}, decoded from NARA's official code list.", "The category belongs only to the confirmed protected-identifier match.", "Strongly date-bounded to Army entry; it does not establish a named employer or immediate OSS affiliation.", "A_direct_official", "medium", "publish_qualified", "Published with its limits and excluded from verified-employer analytics.", [{"source_key": ARMY, "locator_override": f"Army entry {date}; civilian occupation code {code}; protected identifier withheld"}, {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46"}, {"source_key": CODES, "locator_override": f"Historical category {code}", "excerpt_override": occupation.capitalize()}], f"{slug(name)}-army-occupation-b994"),
        ])

    values.extend([
        claim("identity-eugene-waith-b994", 25, "identity", "Indexed Eugene Merse Waith is a high-confidence match to Eugene Mersereau Waith, Yale instructor and OSS counterintelligence officer.", "Yale supplies the full distinctive name, compatible shortened index form, first-lieutenant chronology and direct OSS service.", "High confidence from the rare full name, matching indexed lieutenant note and explicit institutional OSS biography.", "Yale dates civilian teaching, Army entry and OSS service in sequence.", "B_authoritative_institutional", "high", "published", "The personnel file is still needed for an exact transfer date.", links(INDEX, YALE)),
        claim("last-civilian-eugene-waith-yale-b994", 25, "last_civilian_pre_service", "Yale University was Eugene Mersereau Waith's last documented civilian employer before Army and OSS service.", "Yale appointed him Instructor in English in 1939 and says he interrupted teaching duties for Army service in 1943.", "High-confidence identity from the rare name, lieutenant note and direct OSS biography.", "Strongly date-bounded from the 1939 appointment to the 1943 interruption for Army service.", "B_authoritative_institutional", "high", "published", "Employment is kept separate from the later Army pathway.", [{"source_key": YALE, "locator_override": "Biographical paragraphs 93-95", "excerpt_override": "upon completing his Ph.D. in English in 1939, he was appointed Instructor in English"}], "eugene-waith-yale-b994"),
        claim("army-eugene-waith-b994", 25, "immediate_pre_oss_affiliation", "The United States Army was Eugene Mersereau Waith's institutional pathway into OSS counterintelligence service.", "Yale says he enlisted as a private, became a first lieutenant and served in Europe as an OSS counterintelligence officer.", "High-confidence identity from the direct institutional biography and compatible index lieutenant note.", "Strong wartime pathway; the exact Army-to-OSS transfer date is not supplied.", "B_authoritative_institutional", "high", "published", "Military assignment, never mislabeled as a civilian employer.", [{"source_key": YALE, "locator_override": "Biographical paragraph 94", "excerpt_override": "served in Europe as a counterintelligence officer for the Office of Strategic Services"}], "eugene-waith-army-b994"),
        claim("identity-nancy-wake-b994", 27, "identity", "Indexed Nancy Wake probably refers to Nancy Grace Augusta Wake, the Australian journalist, Resistance member and SOE officer.", "The Australian War Memorial supplies the famous exact name and compatible Allied clandestine-service chronology but does not mention OSS or this personnel file.", "Probable, not settled: the distinctive name and chronology are strong, but famous-name assignment is not upgraded without a direct OSS or personnel-file bridge.", "The Memorial dates Hearst journalism, Resistance work and SOE service before and during the war.", "B_authoritative_institutional", "medium", "publish_qualified", "Box 811 review is required to establish why the OSS index contains this allied personnel record.", links(INDEX, AWM)),
        claim("hearst-nancy-wake-b994", 27, "last_civilian_pre_service", "Hearst's newspaper group is the best-supported last civilian employer before Nancy Wake's Resistance and SOE service.", "The Memorial says Wake worked in Paris for the Hearst group as a journalist before joining the Resistance after France's surrender.", "Probable identity from the distinctive name and compatible Allied wartime chronology.", "Documented prewar employment and best-supported last civilian role; not claimed as immediately before OSS.", "B_authoritative_institutional", "medium", "publish_qualified", "No individual Hearst newspaper or exact employment date is inferred.", [{"source_key": AWM, "locator_override": "Description paragraphs 76-78", "excerpt_override": "Wake settled in Paris, working for the Hearst group of newspapers as a journalist."}], "nancy-wake-hearst-b994"),
        claim("resistance-nancy-wake-b994", 27, "other_pre_oss_affiliation", "Nancy Wake joined the French Resistance after France's 1940 surrender.", "The Memorial documents escape-line work and later armed Resistance organization.", "Probable identity from the distinctive name and compatible Allied wartime chronology.", "Documented wartime service before SOE; no OSS sequence is established.", "B_authoritative_institutional", "medium", "publish_qualified", "Volunteer resistance work, not employment.", links(AWM), "nancy-wake-resistance-b994"),
        claim("soe-nancy-wake-b994", 27, "other_pre_oss_affiliation", "Nancy Wake began work in the French Section of the Special Operations Executive after reaching England in June 1943.", "The Memorial gives the month, organization, France return and later SOE headquarters movements.", "Probable identity from the distinctive name and compatible Allied wartime chronology.", "Strongly dated Allied service; not presented as OSS service or as a proven immediate predecessor.", "B_authoritative_institutional", "medium", "publish_qualified", "SOE remains distinct from OSS.", [{"source_key": AWM, "locator_override": "Description paragraph 78", "excerpt_override": "In June 1943 she reached England where she began working in the French Section of the Special Operations Executive"}], "nancy-wake-soe-b994"),
        claim("identity-george-walbridge-b994", 31, "identity", "Indexed George O Walbridge is a high-confidence match to the U.S. Navy officer who served in OSS after Normandy.", "The Naval Institute uses the exact distinctive name, supplies officer and unit chronology, and explicitly states OSS service.", "High confidence from the exact name, direct OSS statement and compatible military chronology.", "The biography places Navy service directly before OSS.", "B_authoritative_institutional", "high", "published", "The indexed personnel file can refine the exact transfer date.", links(INDEX, USNI)),
        claim("navy-george-walbridge-b994", 31, "immediate_pre_oss_affiliation", "The United States Navy, including MTB Ron 2, was George O. Walbridge's immediate documented pathway into OSS.", "The Naval Institute lists Navy commissioning and motor-torpedo squadrons before stating that OSS service followed Normandy D-Day.", "High-confidence exact-name direct OSS biography.", "Strongly date-bounded by the explicit after-D-Day transition; no exact day is given.", "B_authoritative_institutional", "high", "published", "Military assignment, not civilian employment.", [{"source_key": USNI, "locator_override": "Author biography", "excerpt_override": "After Normandy D-Day he served in the OSS."}], "george-walbridge-navy-b994"),
        claim("rcaf-george-walbridge-b994", 31, "other_pre_oss_affiliation", "George O. Walbridge served for one year in the Royal Canadian Air Force before his 1942 U.S. Navy commission.", "The Naval Institute explicitly supplies the service and sequence.", "High-confidence exact-name direct OSS biography.", "Documented earlier Allied military service, not immediate to OSS.", "B_authoritative_institutional", "high", "published", "Earlier military assignment.", links(USNI), "george-walbridge-rcaf-b994"),
        claim("identity-patrick-waldberg-b994", 33, "identity", "Indexed Patrick K.C. Waldberg is probably the American writer and wartime OWI assignee Patrick Waldberg.", "A scholarly profile supplies the unusual surname, American nationality and compatible France-to-U.S.-to-London wartime chronology.", "Probable only: the source omits K.C., OSS and the indexed personnel file.", "The source documents French military service and a 1942 OWI assignment but not their relation to OSS.", "C_reputable_contemporary_or_scholarly", "medium", "publish_qualified", "Box 811 review is required before upgrading identity or immediacy.", links(INDEX, GAGOSIAN)),
        claim("owi-patrick-waldberg-b994", 33, "other_pre_oss_affiliation", "Patrick Waldberg received an Office of War Information assignment to London in September 1942.", "The profile dates his departure and names the American Office of War Information.", "Probable identity from the unusual name and compatible wartime chronology.", "Documented wartime government assignment; the sequence relative to OSS is unknown.", "C_reputable_contemporary_or_scholarly", "medium", "publish_qualified", "Government assignment, not silently labeled a private employer.", [{"source_key": GAGOSIAN, "locator_override": "Patrick Waldberg wartime chronology", "excerpt_override": "he departed for London, where he had been assigned by the American Office of War Information"}], "patrick-waldberg-owi-b994"),
        claim("french-army-patrick-waldberg-b994", 33, "other_pre_oss_affiliation", "Patrick Waldberg volunteered in the French infantry and was demobilized in August 1940.", "The profile documents the volunteer service, Croix de Guerre and demobilization.", "Probable identity from the unusual name and compatible wartime chronology.", "Definitely earlier than the 1942 OWI assignment; not shown as immediately before OSS.", "C_reputable_contemporary_or_scholarly", "medium", "publish_qualified", "Earlier military service.", links(GAGOSIAN), "patrick-waldberg-french-army-b994"),
        claim("writer-patrick-waldberg-b994", 33, "occupation", "Patrick Waldberg was described as an American writer and political activist before the war; no employer is named.", "The profile identifies his work and Paris associations before wartime service.", "Probable identity from the unusual name and compatible chronology.", "Documented prewar occupation only; no immediate or last-employer claim is made.", "C_reputable_contemporary_or_scholarly", "medium", "publish_qualified", "No employer is invented from an occupation.", links(GAGOSIAN), "patrick-waldberg-writer-b994"),
        claim("conflict-carl-walden-b994", 34, "identity", "Carl O Walden remains separate from James E Walden despite a shared printed protected identifier.", "The visually verified adjacent rows print different names but the same protected identifier; the Army bulk comparison produced no resolving record.", "Conflicting source data: neither person receives the other's rank, history or identity.", "No temporal conclusion is possible until the personnel files are reviewed.", "A_direct_official", "conflicting", "conflicting", "The duplicate group is visible and requires critical archival review.", links(INDEX, ARMY)),
        claim("conflict-james-walden-b994", 35, "identity", "James E Walden remains separate from Carl O Walden despite a shared printed protected identifier.", "The visually verified adjacent rows print different names but the same protected identifier; the Army bulk comparison produced no resolving record.", "Conflicting source data: James retains his printed private rank, while no history is transferred between rows.", "No temporal conclusion is possible until the personnel files are reviewed.", "A_direct_official", "conflicting", "conflicting", "The duplicate group is visible and requires critical archival review.", links(INDEX, ARMY)),
        claim("identity-herbert-waldhorn-b994", 36, "identity", "Indexed Herbert F Waldhorn is confirmed as the 74th General Hospital Medical Corps captain transferred to OSS headquarters.", "The index and unit history agree in exact name and a protected officer identifier; the unit history explicitly names the OSS transfer.", "Confirmed by exact protected-identifier agreement and direct unit-to-OSS evidence; the identifier remains private.", "The 1945 hospital role directly precedes the listed OSS transfer.", "C_reputable_contemporary_or_scholarly", "confirmed", "published", "Direct military assignment evidence; no civilian employer is inferred.", links(INDEX, MED)),
        claim("hospital-herbert-waldhorn-b994", 36, "immediate_pre_oss_affiliation", "The 74th General Hospital was Herbert F. Waldhorn's explicit immediate assignment before transfer to OSS headquarters.", "The unit history identifies Waldhorn as an assistant neuropsychiatric service chief and lists his transfer destination as OSS headquarters.", "Confirmed by protected-identifier agreement and exact name.", "Explicit immediate transfer; the precise day is not stated.", "C_reputable_contemporary_or_scholarly", "confirmed", "published", "Military hospital assignment, not civilian employment.", [{"source_key": MED, "locator_override": "1945 transfer roster", "excerpt_override": "Capt. Herbert F. Waldhorn, MC ... HQ & HQ Office of Strategic Service"}], "herbert-waldhorn-74gh-b994"),
        claim("cavalry-maturin-waldo-b994", 38, "other_pre_oss_affiliation", "Maturin F. Waldo served as a corporal in Troop E, 101st Cavalry through 27 March 1941.", "The New York State roster supplies the exact name, private matching identifier, unit, rank and service dates.", "Confirmed by two official protected-identifier matches and exact name.", "Documented earlier military service ending two days before Army entry; not claimed as the immediate OSS predecessor.", "B_authoritative_institutional", "high", "published", "The two-day transition is preserved without inferring the later OSS pathway.", links(NYMM, INDEX, ARMY), "maturin-waldo-101cav-b994"),
    ])
    return values


def base_update(row: int, **overrides: object) -> dict[str, object]:
    value: dict[str, object] = {"person_id": PEOPLE[row][0], "manual_review_required": True, "personnel_file_digitized": False, "personnel_file_reviewed": False, "archival_review_priority": "high"}
    value.update(overrides)
    return value


def person_updates() -> list[dict[str, object]]:
    values = [base_update(row, identity_status="unresolved", identity_evidence=f"The visually verified page 487 row preserves {PEOPLE[row][1]} and its archival context. {reason}", research_status="requires_archival_review", next_action=f"Review the indexed personnel file for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}") for row, reason in UNRESOLVED.items()]
    values.extend([
        base_update(25, identity_status="high_confidence", identity_evidence="Yale documents Eugene Mersereau Waith's rare full name, 1939 appointment, promotion to first lieutenant and explicit OSS counterintelligence service; the index's Merse truncation and lieutenant note are compatible.", name_variants=["Eugene Mersereau Waith"], personnel_category="commissioned_army_officer", commissioned_officer=True, allied_or_foreign_personnel=False, research_status="verified_employer_found", next_action="Review Box 811 only to refine the exact Army-to-OSS transition date; Yale is the verified last civilian employer.", archival_review_priority="low"),
        base_update(27, identity_status="probable", identity_evidence="The Australian War Memorial documents the distinctive name and compatible Hearst-to-Resistance-to-SOE chronology but does not mention OSS or the indexed file.", name_variants=["Nancy Grace Augusta Wake"], personnel_category="foreign_or_allied_military_personnel", commissioned_officer=True, allied_or_foreign_personnel=True, research_status="documented_prewar_employer_found", next_action="Review Box 811 to establish why this Allied SOE officer appears in the OSS index and whether any OSS liaison followed SOE service; Hearst remains qualified last civilian employment."),
        base_update(28, identity_status="confirmed", identity_evidence="Exact name and a nonshared protected identifier connect the visually verified index row to the official Army record.", personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="occupation_only_found", next_action="Review Box 811 to identify any employer or production behind the broad actors and actresses category and establish the Army-to-OSS chronology.", nara_catalog_id="1263923"),
        base_update(31, identity_status="high_confidence", identity_evidence="The U.S. Naval Institute uses the exact distinctive name, documents the Navy units and explicitly states that Walbridge served in OSS after Normandy D-Day.", personnel_category="commissioned_naval_officer", commissioned_officer=True, allied_or_foreign_personnel=False, research_status="completed", next_action="No online research action is required. Review Box 811 only to refine the exact Navy-to-OSS transfer date.", archival_review_priority="low"),
        base_update(33, identity_status="probable", identity_evidence="A scholarly profile documents the unusual Patrick Waldberg name and compatible France-to-U.S.-to-London wartime chronology, but omits K.C., OSS and the personnel file.", name_variants=["Patrick Waldberg"], personnel_category="civilian_professional_or_administrative_grade", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="completed", next_action="Review Box 811 to confirm the K.C. identity and determine whether OWI preceded OSS; current affiliations remain qualified."),
        base_update(34, identity_status="conflicting", identity_evidence="Carl O Walden and adjacent James E Walden print different names but the same protected identifier. No Army bulk record resolves the conflict.", possible_duplicate_group="page487-walden-shared-identifier-b994", personnel_category="unknown_or_indeterminate", commissioned_officer=None, allied_or_foreign_personnel=False, research_status="conflicting_sources", next_action="Jointly review both Box 812 files before accepting any identifier, rank or pre-OSS history.", archival_review_priority="critical"),
        base_update(35, identity_status="conflicting", identity_evidence="James E Walden and adjacent Carl O Walden print different names but the same protected identifier. No Army bulk record resolves the conflict.", possible_duplicate_group="page487-walden-shared-identifier-b994", personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="conflicting_sources", next_action="Jointly review both Box 812 files before accepting any identifier or pre-OSS history; retain James's printed private rank only on this row.", archival_review_priority="critical"),
        base_update(36, identity_status="confirmed", identity_evidence="Exact name and a protected officer identifier privately connect the index row to the 74th General Hospital captain directly transferred to OSS headquarters.", personnel_category="commissioned_army_officer", commissioned_officer=True, allied_or_foreign_personnel=False, research_status="completed", next_action="No online research action is required. Review Box 812 only for a precise transfer date and any last civilian medical employer.", archival_review_priority="low"),
        base_update(38, identity_status="confirmed", identity_evidence="Exact name and nonshared protected identifier agree across the index, official Army bulk record and New York State Military Museum roster.", personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="completed", next_action="Review Box 812 to identify the Army-to-OSS pathway and any named civilian employer behind historical occupation code 068.", nara_catalog_id="1263923", archival_review_priority="medium"),
        base_update(43, identity_status="confirmed", identity_evidence="A nonshared protected identifier links the index to the official Army record, which supplies the middle initial A while the index omits it.", name_variants=["James A Waldron"], personnel_category="enlisted_army_personnel", commissioned_officer=False, allied_or_foreign_personnel=False, research_status="occupation_only_found", next_action="Review Box 812 to identify the public-service agency behind historical occupation code 266 and establish the Army-to-OSS chronology.", nara_catalog_id="1263923"),
    ])
    return values


def research_attempts() -> list[dict[str, object]]:
    sourced = {25, 27, 28, 31, 33, 36, 38, 43}
    rejected = {26, 37, 44}
    conflicts = {34, 35}
    detail = {
        25: "Yale directly documented the rare-name identity, verified last civilian employment and Army-to-OSS counterintelligence pathway.",
        27: "The Australian War Memorial supported a probable identity, Hearst employment and separate Resistance and SOE service; it did not establish OSS service.",
        28: "The accepted protected-identifier Army bridge confirmed identity and the qualified historical actors and actresses category.",
        31: "The Naval Institute directly documented RCAF and Navy service followed by OSS after Normandy.",
        33: "A scholarly institutional profile supported a probable identity and qualified French infantry, writer and OWI chronology.",
        34: "The shared protected identifier conflicts with the distinct adjacent Carl and James Walden names and produced no resolving Army record.",
        35: "The shared protected identifier conflicts with the distinct adjacent Carl and James Walden names and produced no resolving Army record.",
        36: "A protected-identifier match and unit history documented the 74th General Hospital role and direct transfer to OSS headquarters.",
        38: "Army and New York State protected-identifier matches confirmed identity, a qualified occupation category and earlier 101st Cavalry service.",
        43: "The protected-identifier Army match confirmed identity, middle initial A and a qualified historical police and detective category.",
    }
    attempts = []
    for row, (person_id, name) in PEOPLE.items():
        if row in sourced:
            outcome, reviewed, rejected_count = "source_reviewed", 8, 5
            note = detail[row]
        elif row in conflicts:
            outcome, reviewed, rejected_count = "candidate_rejected", 7, 6
            note = detail[row]
        elif row in rejected:
            outcome, reviewed, rejected_count = "candidate_rejected", 7, 7
            note = UNRESOLVED[row]
        else:
            outcome, reviewed, rejected_count = "no_result", 6, 6
            note = UNRESOLVED.get(row, "No reliable identity or pre-OSS affiliation bridge was found.")
        attempts.append({
            "key": f"page487-row{row}-{slug(name)}-b994", "person_id": person_id, "source_adapter": "manual_staged_protocol",
            "query_text": f"{name}; NARA OSS index context; CIA Reading Room exact-name domain check; Library of Congress exact-name collection check; exact-name and meaningful variants; OSS, rank, branch, identifier and assignment clues; employer and occupation 1940; obituary, institutional, newspaper, directory and archival searches; indexed Box 811, 812 or 815; protected identifiers used only in private official-record comparison",
            "query_variant_type": "staged_identity_employment_archival_protocol_batch_994", "started_at": "2026-11-03T15:00:00Z", "completed_at": "2026-11-03T16:20:00Z", "outcome": outcome, "sources_reviewed": reviewed, "candidate_sources_rejected": rejected_count,
            "rejection_reasons": "Unbridged namesakes, snippets, commercial people-finder pages, relatives, unsourced genealogy, postwar-only leads and sources without an OSS, protected-identifier, rank, unit or personnel-file bridge were rejected. The official Dr. John Waldron OSS history was not assigned to the common-name index row without another corroborating identifier. Henry S. Wakabayashi's 1995 veterans-association reference was not treated as a wartime identity bridge. Historical occupation codes and military service were not silently converted into named employers.",
            "research_notes": f"{note} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain and archival searches were checked as applicable. Grouped CIA Reading Room and Library of Congress discovery checks produced no additional publishable employer source for the cohort. The NARA index page was text-extracted, rendered and visually checked; official Army bulk data and code documentation were inspected locally. Final sources were opened in context. No search-result snippet was used as sole final evidence, no paywall or access control was bypassed, and no authenticated NARA Catalog API call was made.",
            "next_action": "Review the indexed personnel file for corroborating identifiers, the immediate pre-OSS affiliation and the last civilian employer before wartime service.", "attempt_number": 1, "research_agent_version": "before-oss-b994-v1",
        })
    return attempts


def main() -> None:
    bundle = {"bundle_version": "batch-994-v1", "reviewer": "Before OSS Batch 994 evidence review", "sources": sources(), "organizations": organizations(), "affiliations": affiliations(), "claims": claims(), "person_updates": person_updates(), "research_attempts": research_attempts()}
    EvidenceBundle.model_validate(bundle)
    OUTPUT.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
