#!/usr/bin/env python3
"""Generate the reviewed Batch 999 evidence bundle from audited constants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oss_research.evidence import EvidenceBundle  # noqa: E402


OUTPUT = ROOT / "research/evidence-page490-walters-to-warburton-review_batch-999_2026-11-03.json"

INDEX = "nara-index-b999"
ARMY = "army-bulk-b999"
TECH = "army-tech-b999"
CODES = "army-codes-b999"
WAPLES_ARTICLE = "jaworski-waples-b999"
UCHICAGO_VP = "uchicago-vp-waples-b999"
UCHICAGO_GLS = "uchicago-gls-waples-b999"
WANVIG_ARMY = "army-order-battle-wanvig-b999"
WAMPLER_BOOK = "bartholomew-feis-wampler-b999"

PEOPLE = {
    1: ("11146615-3f52-5ae6-9119-ecc165802b78", "Robert E Walters"),
    2: ("74ab917d-f2ab-5d2f-bf4f-59055a55da57", "Thelma Walters"),
    3: ("1141d8de-a8d3-5aaf-b779-8b84ec4cf1b0", "Curt Waltheim"),
    4: ("9f35a8cd-f1b4-52c6-86b4-714c202bf405", "Alan T Walther"),
    5: ("996f75ec-4fac-55f6-b7bf-fa4f0ddb43a7", "John J Walthers"),
    6: ("35002c15-38b4-5f5e-8713-b0b226926dd0", "Daniel W Walton"),
    7: ("403d1c63-8193-5f2f-a549-5f71c37c1f71", "Gladys E Walton"),
    8: ("b23d9b76-1987-537d-b0bf-89c43d458860", "Lewis B Walton"),
    9: ("2bfe7baf-a5df-5c11-8fcd-d8f5a4146430", "Marion C Walton"),
    10: ("a74ca522-ca4d-5924-a8dc-ed3382ee190f", "Wilson W Waltz"),
    11: ("491e9892-9c66-5c7b-85a8-276ff02d464d", "Joseph A Walukinas"),
    12: ("e11cbc37-42b3-5a65-8657-cdf1ac337f83", "Leonard Walz"),
    13: ("fae415ae-efc6-5102-bd9c-b6abba49fa52", "Robert E Wampler"),
    14: ("38cb516e-118d-5644-b837-9d45de5ea917", "Kenneth Wanamaker"),
    15: ("9ab444b5-ff20-5e15-9848-43ddb04202cd", "Rafael Wand"),
    16: ("13428c39-15ea-5c58-bdb9-dfa9089a968e", "Edward W Wank"),
    17: ("53ff2ff5-0e2d-5e07-b144-6fa3393829ca", "Lucien H Wante"),
    18: ("140ae430-6d2f-51ee-9f80-9f223b4e6aa2", "John C Wantland"),
    19: ("da9f2b1c-e14b-507e-8a85-79946acc3477", "Newton R Wantland"),
    20: ("3dd93a91-632c-54b9-9dee-7171a731a6c7", "James Wanveer"),
    21: ("83703277-d84d-5429-88c6-e13b0ef7fdbd", "Harry F Wanvig"),
    22: ("5e7d4837-9102-5424-bdf0-90556c450648", "Douglas Waples"),
    23: ("c4243e64-49ca-5166-8354-37b415fea9cf", "John H Warburton"),
}

ARMY_OCCUPATIONS = {
    4: {"date": "1942-10-08", "code": "048", "occupation": "draftsman", "label": "Draftsmen", "locator": "PDF physical page 171; historical category 0-48"},
    6: {"date": "1942-09-06", "code": "306", "occupation": "general farmer", "label": "General farmers", "locator": "PDF physical page 172; historical category 3-06"},
    15: {"date": "1943-08-31", "code": "627", "occupation": "textile-products-fabrication occupation, not elsewhere classified", "label": "Occupations in fabrication of textile products, n.e.c.", "locator": "PDF physical page 174; historical category 6-27"},
    19: {"date": "1944-05-01", "code": "583", "occupation": "mechanic or repairman, not elsewhere classified", "label": "Mechanics and repairmen, not elsewhere classified", "locator": "PDF physical pages 175-176; historical category 5-83"},
    23: {"date": "1943-05-14", "code": "760", "occupation": "filling-station or parking-lot attendant", "label": "Attendants, filling stations and parking lots", "locator": "PDF physical page 174; historical category 7-60"},
}

ARMY_IDENTITY_ONLY = {
    10: "The residual civilian-occupation code 999 is not interpreted.",
    14: "The residual civilian-occupation code 999 is not interpreted.",
}

UNRESOLVED = {
    1: "Common-name results supplied no OSS assignment, protected-identifier, employer, occupation, or Box 815 personnel-file bridge.",
    2: "Exact-name and initial-variant searches supplied no reliable OSS, employment, institutional, or archival identity bridge.",
    3: "The printed spelling and a Kurt spelling variant produced no reliable OSS, employer, occupation, or personnel-file bridge; no correction is inferred from the truncated note.",
    5: "Exact-name and plural-surname variants produced no reliable OSS, employer, occupation, or personnel-file bridge.",
    7: "Exact-name, obituary, directory, institutional, newspaper, and archival searches yielded only unbridged namesakes.",
    8: "Common-name searches produced no source with an OSS assignment, protected identifier, employer chronology, or Box 815 bridge.",
    9: "Exact-name and meaningful-variant searches produced no source with an OSS assignment, protected identifier, employer chronology, or Box 815 bridge.",
    12: "Exact-name, occupation, obituary, institutional, directory, and archival searches produced no reliable identity bridge.",
    16: "Exact-name and initial-variant searches produced no reliable OSS, employer, occupation, or personnel-file bridge.",
    17: "Exact-name and meaningful-variant searches produced no reliable OSS, employer, occupation, or personnel-file bridge.",
    18: "A 1941 Dallas directory lead names a salesman with this name, but no OSS, protected-identifier, rank, location, or Box 815 evidence connects that namesake to the index row.",
    20: "The distinctive surname produced no reliable OSS assignment, employer, occupation, obituary, institutional, or archival identity bridge.",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def sources() -> list[dict[str, object]]:
    return [
        {
            "key": INDEX,
            "stable_url": "https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf",
            "archival_identifier": "RG 226, Entry A1-224, Boxes 814-815",
            "title": "OSS Personnel Files from Excel",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "2010-12-23",
            "locator": "PDF page 490, rows 1-23; checked against layout-preserving text and an original-detail page render",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "Records of the Office of Strategic Services, Record Group 226",
            "rights_notes": "All 23 printed rows remain separate. The Curt Waltheim note is preserved literally as printed. Protected identifiers remain private. Page 490 row 24 begins the next batch.",
        },
        {
            "key": ARMY,
            "stable_url": "https://catalog.archives.gov/id/1263923",
            "archival_identifier": "National Archives Identifier 1263923; parent series NAID 604357",
            "title": "Electronic Army Serial Number Merged File, ca. 1938-1946",
            "author_creator": "Adjutant General's Office; National Personnel Records Center; National Archives and Records Administration",
            "repository_publisher": "National Archives and Records Administration",
            "publication_record_date": "1938-1946; merged file created 2002",
            "locator": "Official unrestricted ASNEF.FIN.DAT; seven accepted and one conflicting protected-identifier comparison; identifiers and record ordinals withheld",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records",
            "document_number": "ASNEF.FIN.DAT",
            "rights_notes": "Five broad occupation categories and two identity-only bridges were accepted after private review. Joseph A Walukinas remains conflicting because the identifier is shared by materially different index names.",
        },
        {
            "key": TECH,
            "stable_url": "https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf",
            "archival_identifier": "NN3-064-03-008; National Archives Identifier 1263923",
            "title": "World War II Army Enlistment Records: Reference Copy of Technical Documentation",
            "author_creator": "National Archives and Records Administration",
            "repository_publisher": "National Archives at College Park - Electronic Records",
            "publication_record_date": "1994-2005; reference copy modified 2011",
            "locator": "PDF physical pages 44-46; name, Army-entry-date, grade, and civilian-occupation fields",
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
            "locator": "PDF physical pages 171, 172, 174, and 175-176; historical civilian-occupation categories 0-48, 3-06, 5-83, 6-27, and 7-60",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "collection_name": "World War II Army Enlistment Records technical documentation",
            "rights_notes": "The historical categories identify broad occupations, not named employers, workplaces, or exact OSS-transfer dates. Residual code 999 is not interpreted.",
        },
        {
            "key": WAPLES_ARTICLE,
            "stable_url": "https://doi.org/10.1002/symb.498",
            "archival_identifier": "DOI 10.1002/symb.498",
            "title": "Goffman's Interest in Spies and Espionage: The University of Chicago Context",
            "author_creator": "Gary D. Jaworski",
            "repository_publisher": "Symbolic Interaction; Wiley",
            "publication_record_date": "2020-07-09",
            "locator": "Volume 44, issue 2, pages 392-411; abstract and references to Waples's 1941 university records and RG 226 Box 815 personnel file",
            "access_date": "2026-11-03",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "rights_notes": "The scholarly article identifies Douglas Waples as a University of Chicago professor who served in a U.S. intelligence organization and cites his exact Box 815 personnel file.",
        },
        {
            "key": UCHICAGO_VP,
            "stable_url": "https://www.lib.uchicago.edu/e/scrc/findingaids/view.php?eadid=ICU.SPCL.OFCVP",
            "archival_identifier": "ICU.SPCL.OFCVP, Box 58, folders 13-15",
            "title": "Guide to the University of Chicago Office of the Vice-President Records, 1937-1946",
            "author_creator": "University of Chicago Library",
            "repository_publisher": "Hanna Holborn Gray Special Collections Research Center, University of Chicago Library",
            "publication_record_date": "2006",
            "locator": "Box 58, folders 13-15, Waples, Douglas, 1940-1943",
            "access_date": "2026-11-03",
            "source_quality": "B_authoritative_institutional",
        },
        {
            "key": UCHICAGO_GLS,
            "stable_url": "https://www.lib.uchicago.edu/e/scrc/findingaids/view.php?eadid=ICU.SPCL.GRADLIBRARY",
            "archival_identifier": "ICU.SPCL.GRADLIBRARY, Box 5, folder 3",
            "title": "Guide to the University of Chicago Graduate Library School Records, 1928-1979",
            "author_creator": "University of Chicago Library",
            "repository_publisher": "Hanna Holborn Gray Special Collections Research Center, University of Chicago Library",
            "publication_record_date": "2006",
            "locator": "Series I, Faculty Materials; Box 5, folder 3, Waples, Douglas",
            "access_date": "2026-11-03",
            "source_quality": "B_authoritative_institutional",
        },
        {
            "key": WANVIG_ARMY,
            "stable_url": "https://www.armyupress.army.mil/Portals/7/combat-studies-institute/csi-books/OrderofBattle2.pdf",
            "title": "U.S. Army Order of Battle, 1919-1941, Volume 2",
            "author_creator": "Steven E. Clay",
            "repository_publisher": "Combat Studies Institute Press; Army University Press",
            "publication_record_date": "2010",
            "locator": "309th Field Artillery Regiment entry; commanders table, PDF text lines 11554-11562",
            "access_date": "2026-11-03",
            "source_quality": "A_direct_official",
            "rights_notes": "The official unit history identifies Colonel Harry F. Wanvig as commander from 26 April 1926 to October 1940; it does not establish his later OSS sequence.",
        },
        {
            "key": WAMPLER_BOOK,
            "stable_url": "https://kansaspress.ku.edu/9780700616527/",
            "title": "The OSS and Ho Chi Minh: Unexpected Allies in the War against Japan",
            "author_creator": "Dixee R. Bartholomew-Feis",
            "repository_publisher": "University Press of Kansas",
            "publication_record_date": "2006-05",
            "locator": "Chapter 7, page 176; Major Robert E. Wampler identified with the OSS Special Operations Branch in Kunming",
            "access_date": "2026-11-03",
            "source_quality": "C_reputable_contemporary_or_scholarly",
            "rights_notes": "Used for identity and wartime assignment only. It supplies no pre-OSS employer or immediate predecessor affiliation.",
        },
    ]


def organizations() -> list[dict[str, object]]:
    return [
        {
            "key": "university-chicago-b999",
            "organization_id": "f2c878b0-ee44-573d-ab30-7e4282bc85e5",
            "canonical_name": "University of Chicago",
            "historical_name": "University of Chicago",
            "aliases": ["University of Chicago Graduate Library School"],
            "organization_type": "university",
            "sector": "academia_and_research",
            "city": "Chicago",
            "state_or_region": "Illinois",
            "country": "United States",
            "normalization_notes": "The employing university is canonicalized while the Graduate Library School unit is preserved in the role and name-as-found fields.",
        },
        {
            "key": "309-field-artillery-b999",
            "canonical_name": "309th Field Artillery Regiment",
            "historical_name": "309th Field Artillery Regiment",
            "aliases": ["309th F.A. Regiment"],
            "organization_type": "Army regiment",
            "sector": "military",
            "country": "United States",
            "active_dates": "1917-1959",
            "normalization_notes": "The interwar Organized Reserve regiment remains distinct from later successor units.",
        },
    ]


def affiliations() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, item in ARMY_OCCUPATIONS.items():
        values.append({
            "key": f"{slug(PEOPLE[row][1])}-army-occupation-b999",
            "person_id": PEOPLE[row][0],
            "occupation": item["occupation"],
            "relationship_type": "unknown",
            "end_date": item["date"],
            "date_precision": f"Historical civilian-occupation code {item['code']} was recorded at Army entry on {item['date']}; no named employer, workplace, or exact OSS-transfer date is supplied.",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "strongly_date_bounded",
            "identity_confidence": "confirmed",
            "claim_confidence": "medium",
            "source_quality": "A_direct_official",
            "publication_status": "publish_qualified",
            "research_notes": "Broad historical occupation category only; no named employer or workplace is inferred.",
        })
    values.extend([
        {
            "key": "douglas-waples-university-chicago-b999",
            "person_id": PEOPLE[22][0],
            "organization_key": "university-chicago-b999",
            "organization_name_as_found": "University of Chicago Graduate Library School",
            "role_title": "professor",
            "occupation": "professor and library-science researcher",
            "relationship_type": "employment",
            "date_precision": "University records document Waples in 1940-1943 faculty and vice-president files; the scholarly source cites his Box 815 personnel file beginning in 1942.",
            "city": "Chicago",
            "state_or_region": "Illinois",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "high_confidence",
            "claim_confidence": "high",
            "source_quality": "B_authoritative_institutional",
            "publication_status": "published",
            "research_notes": "The university employment is documented before and into the wartime period, but the accessible sources do not establish the exact transition to the indexed personnel file or exclude an intervening government assignment.",
        },
        {
            "key": "harry-wanvig-309-field-artillery-b999",
            "person_id": PEOPLE[21][0],
            "organization_key": "309-field-artillery-b999",
            "organization_name_as_found": "309th Field Artillery Regiment",
            "role_title": "colonel and regimental commander",
            "occupation": "Army officer",
            "relationship_type": "military_assignment",
            "start_date": "1926-04-26",
            "end_date": "1940-10",
            "date_precision": "The official Army unit history gives 26 April 1926 through October 1940; no later transfer chronology is supplied.",
            "country": "United States",
            "immediate_pre_oss": False,
            "last_civilian_pre_service": False,
            "pre_oss_temporal_basis": "documented_prewar",
            "identity_confidence": "probable",
            "claim_confidence": "medium",
            "source_quality": "A_direct_official",
            "publication_status": "publish_qualified",
            "research_notes": "The exact distinctive name and official rank support a probable match, but the Box 815 file is needed to bridge the interwar command to this index row.",
        },
    ])
    return values


def make_claim(*, key: str, row: int, claim_type: str, text: str, paraphrase: str,
               identity: str, temporal: str, quality: str, confidence: str,
               publication: str, notes: str, source_links: list[dict[str, str]],
               affiliation_key: str | None = None) -> dict[str, object]:
    value: dict[str, object] = {
        "key": key, "person_id": PEOPLE[row][0], "claim_type": claim_type,
        "claim_text": text, "evidence_paraphrase": paraphrase,
        "identity_match_assessment": identity, "temporal_assessment": temporal,
        "source_quality": quality, "claim_confidence": confidence,
        "publication_status": publication, "match_notes": notes,
        "sources": source_links,
    }
    if affiliation_key:
        value["affiliation_key"] = affiliation_key
    return value


def claims() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, item in ARMY_OCCUPATIONS.items():
        name = PEOPLE[row][1]
        values.extend([
            make_claim(
                key=f"identity-{slug(name)}-b999", row=row, claim_type="identity",
                text=f"Indexed {name} is confirmed as the reviewed official Army entry record.",
                paraphrase="The exact names agree, and a nonshared protected identifier connects the records.",
                identity="Confirmed by exact name and a nonshared protected-identifier agreement; the identifier and record ordinal remain private.",
                temporal=f"The Army record dates entry to {item['date']} and supplies only historical civilian code {item['code']}.",
                quality="A_direct_official", confidence="confirmed", publication="published",
                notes="Identity only; no named employer or exact OSS-transfer date is inferred.",
                source_links=[
                    {"source_key": INDEX, "locator_override": f"PDF page 490 row {row}; protected identifier withheld"},
                    {"source_key": ARMY, "locator_override": "Accepted reviewed identity bridge; protected identifier withheld"},
                ],
            ),
            make_claim(
                key=f"occupation-{slug(name)}-b999", row=row, claim_type="occupation",
                text=f"At Army entry on {item['date']}, {name} was recorded in the historical {item['occupation']} category; no named employer is identified.",
                paraphrase=f"The accepted Army record carries civilian-occupation code {item['code']}, decoded from NARA's official code list.",
                identity="The occupation category belongs only to the confirmed protected-identifier match; the identifier itself is not public.",
                temporal="Strongly date-bounded to Army entry; it does not establish the immediate pre-OSS affiliation or a named employer.",
                quality="A_direct_official", confidence="medium", publication="publish_qualified",
                notes="Published with its limits and excluded from verified-employer analytics.",
                source_links=[
                    {"source_key": ARMY, "locator_override": f"Army entry {item['date']}; civilian occupation code {item['code']}; protected identifier withheld"},
                    {"source_key": TECH, "support_type": "context_only", "locator_override": "PDF physical pages 44-46"},
                    {"source_key": CODES, "locator_override": item["locator"], "excerpt_override": item["label"]},
                ], affiliation_key=f"{slug(name)}-army-occupation-b999",
            ),
        ])
    for row, limitation in ARMY_IDENTITY_ONLY.items():
        name = PEOPLE[row][1]
        values.append(make_claim(
            key=f"identity-{slug(name)}-b999", row=row, claim_type="identity",
            text=f"Indexed {name} is confirmed as the reviewed official Army entry record.",
            paraphrase="The exact names agree, and a nonshared protected identifier connects the records.",
            identity="Confirmed by exact name and a nonshared protected-identifier agreement; the identifier and record ordinal remain private.",
            temporal=f"The Army entry supports identity only. {limitation}",
            quality="A_direct_official", confidence="confirmed", publication="published",
            notes="No occupation, employer, workplace, or exact OSS-transfer date is inferred.",
            source_links=[
                {"source_key": INDEX, "locator_override": f"PDF page 490 row {row}; protected identifier withheld"},
                {"source_key": ARMY, "locator_override": "Accepted reviewed identity bridge; protected identifier withheld"},
            ],
        ))
    values.extend([
        make_claim(
            key="conflict-joseph-walukinas-b999", row=11, claim_type="identity",
            text="Joseph A Walukinas's protected identifier is shared by a materially different index name, so the Army candidate remains conflicting.",
            paraphrase="The private comparison found surname-and-given-name agreement to one Army form but a material collision elsewhere in the index.",
            identity="Conflicting: the shared protected identifier cannot establish a unique person, and the Army form omits the indexed middle initial.",
            temporal="No chronology or occupation is transferred until the Box 815 files resolve the collision.",
            quality="A_direct_official", confidence="conflicting", publication="conflicting",
            notes="The conflict remains visible without exposing the protected identifier or unrelated index biography.",
            source_links=[
                {"source_key": INDEX, "locator_override": "PDF page 490 row 11; protected identifier withheld"},
                {"source_key": ARMY, "locator_override": "Conflicting reviewed identity bridge; protected identifier withheld"},
            ],
        ),
        make_claim(
            key="identity-robert-e-wampler-b999", row=13, claim_type="identity",
            text="The indexed Major Robert E Wampler is a high-confidence match to the OSS Special Operations Branch chief documented in Kunming.",
            paraphrase="The exact name, rank, OSS organization, and China assignment align with a scholarly history.",
            identity="High confidence from exact name and rank plus a specific OSS branch and wartime location; the Box 815 file remains the direct archival confirmation target.",
            temporal="The source documents a 1945 OSS assignment, not Wampler's pre-OSS employer or predecessor affiliation.",
            quality="C_reputable_contemporary_or_scholarly", confidence="high", publication="published",
            notes="Identity and OSS assignment only; no pre-OSS affiliation is inferred.",
            source_links=[
                {"source_key": INDEX, "locator_override": "PDF page 490 row 13; rank Major; Box 815"},
                {"source_key": WAMPLER_BOOK, "locator_override": "Chapter 7, page 176", "excerpt_override": "SO Branch of the OSS in Kunming"},
            ],
        ),
        make_claim(
            key="identity-harry-f-wanvig-b999", row=21, claim_type="identity",
            text="The indexed Harry F Wanvig is a probable match to Colonel Harry F. Wanvig in the official Army unit history.",
            paraphrase="The exact distinctive name aligns with an official interwar Army command record, but no direct OSS or Box 815 bridge was accessible online.",
            identity="Probable from the distinctive exact name and official colonel record; direct personnel-file confirmation is still required.",
            temporal="The Army command ended in October 1940 and is documented prewar, but its relation to the indexed service sequence remains unproven.",
            quality="A_direct_official", confidence="medium", publication="publish_qualified",
            notes="Published as a qualified identity and assignment lead, not a settled immediate pre-OSS affiliation.",
            source_links=[
                {"source_key": INDEX, "locator_override": "PDF page 490 row 21; Box 815"},
                {"source_key": WANVIG_ARMY, "locator_override": "309th Field Artillery Regiment commanders table"},
            ],
        ),
        make_claim(
            key="assignment-harry-f-wanvig-b999", row=21, claim_type="other_pre_oss_affiliation",
            text="A probable Harry F. Wanvig identity commanded the 309th Field Artillery Regiment from 26 April 1926 to October 1940.",
            paraphrase="The official Army order of battle names Colonel Harry F. Wanvig and dates his regimental command.",
            identity="Probable from the distinctive exact name; the indexed Box 815 personnel file is required for direct confirmation.",
            temporal="Explicitly dated prewar; not shown to be the immediate predecessor to indexed service.",
            quality="A_direct_official", confidence="medium", publication="publish_qualified",
            notes="Military assignment, not civilian employment; excluded from default verified analytics because identity remains probable.",
            source_links=[{"source_key": WANVIG_ARMY, "locator_override": "309th Field Artillery Regiment commanders table", "excerpt_override": "Col. Harry F. Wanvig | 26 April 1926-October 1940"}],
            affiliation_key="harry-wanvig-309-field-artillery-b999",
        ),
        make_claim(
            key="identity-douglas-waples-b999", row=22, claim_type="identity",
            text="The indexed Douglas Waples is a high-confidence match to the University of Chicago professor whose scholarly record cites the same NARA Box 815 personnel file.",
            paraphrase="A scholarly article identifies Douglas Waples as a University of Chicago professor in wartime intelligence and cites Entry A1-224, Box 815.",
            identity="High confidence from the exact name, exact NARA series and box, university records, and wartime-intelligence context.",
            temporal="University records run through 1942-1943 and the cited personnel file begins in 1942; the exact transition remains unclear.",
            quality="C_reputable_contemporary_or_scholarly", confidence="high", publication="published",
            notes="The direct personnel file has not been reviewed, so the exact agency sequence remains an archival task.",
            source_links=[
                {"source_key": INDEX, "locator_override": "PDF page 490 row 22; Box 815"},
                {"source_key": WAPLES_ARTICLE, "locator_override": "Abstract and references", "excerpt_override": "Douglas Waples, both of whom served in U.S. intelligence organizations during World War II"},
                {"source_key": UCHICAGO_VP, "support_type": "context_only", "locator_override": "Box 58, folders 13-15"},
            ],
        ),
        make_claim(
            key="employment-douglas-waples-uchicago-b999", row=22, claim_type="other_pre_oss_affiliation",
            text="Douglas Waples was a University of Chicago Graduate Library School professor before and into the wartime period.",
            paraphrase="University finding aids preserve Waples faculty and vice-president files through 1942-1943; the scholarly article identifies him as a professor and cites his Box 815 personnel file.",
            identity="High confidence from the exact Box 815 citation and matching institutional records.",
            temporal="Documented before the cited 1942 personnel-file span, but not proven to be the immediate predecessor or last civilian employer before service.",
            quality="B_authoritative_institutional", confidence="high", publication="published",
            notes="Published as documented pre-OSS employment; not labeled immediate and not used to infer an unproven transition date.",
            source_links=[
                {"source_key": WAPLES_ARTICLE, "locator_override": "Abstract and references"},
                {"source_key": UCHICAGO_VP, "locator_override": "Box 58, folders 13-15"},
                {"source_key": UCHICAGO_GLS, "locator_override": "Series I, Faculty Materials; Box 5, folder 3"},
            ],
            affiliation_key="douglas-waples-university-chicago-b999",
        ),
    ])
    return values


def base_update(row: int, **overrides: object) -> dict[str, object]:
    value: dict[str, object] = {
        "person_id": PEOPLE[row][0], "manual_review_required": True,
        "personnel_file_digitized": False, "personnel_file_reviewed": False,
        "archival_review_priority": "high",
    }
    value.update(overrides)
    return value


def person_updates() -> list[dict[str, object]]:
    values: list[dict[str, object]] = []
    for row, reason in UNRESOLVED.items():
        values.append(base_update(
            row, identity_status="unresolved",
            identity_evidence=f"The visually verified page 490 row preserves {PEOPLE[row][1]} and its archival context. {reason}",
            research_status="requires_archival_review",
            next_action=f"Review the indexed Box {'814' if row == 3 else '815'} personnel file for corroborating identifiers, the immediate pre-OSS affiliation, and the last civilian employer. No reliable pre-OSS employer has yet been identified in the accessible sources reviewed. {reason}",
        ))
    for row, item in ARMY_OCCUPATIONS.items():
        values.append(base_update(
            row, identity_status="confirmed",
            identity_evidence="The exact indexed name and a nonshared protected identifier connect the row to the reviewed official Army record.",
            personnel_category="enlisted_army_personnel", commissioned_officer=False,
            allied_or_foreign_personnel=False, research_status="occupation_only_found",
            next_action=f"Review the indexed Box 815 personnel file to identify any named employer behind the broad {item['occupation']} category and establish the Army-to-OSS chronology.",
            nara_catalog_id="1263923",
        ))
    for row, limitation in ARMY_IDENTITY_ONLY.items():
        values.append(base_update(
            row, identity_status="confirmed",
            identity_evidence="The exact indexed name and a nonshared protected identifier connect the row to the reviewed official Army record; no occupation is interpreted.",
            personnel_category="enlisted_army_personnel", commissioned_officer=False,
            allied_or_foreign_personnel=False, research_status="requires_archival_review",
            next_action=f"Review the indexed Box 815 personnel file for the immediate pre-OSS affiliation and last civilian employer. {limitation}",
            nara_catalog_id="1263923",
        ))
    values.extend([
        base_update(
            11, identity_status="conflicting",
            identity_evidence="The reviewed protected identifier is shared by materially different index names; the Army candidate omits the indexed middle initial and cannot be uniquely assigned.",
            research_status="conflicting_sources",
            next_action="Compare the indexed Box 815 personnel files for Joseph A Walukinas and the colliding name before transferring any Army identity or occupation evidence.",
        ),
        base_update(
            13, identity_status="high_confidence",
            identity_evidence="The exact name, printed Major rank, OSS Special Operations Branch, and Kunming assignment align with a scholarly history.",
            personnel_category="commissioned_army_officer", commissioned_officer=True,
            allied_or_foreign_personnel=False, research_status="requires_archival_review",
            next_action="Review the indexed Box 815 personnel file to establish Robert E Wampler's immediate pre-OSS military or civilian affiliation and last civilian employer; the accessible source documents only his wartime OSS assignment.",
        ),
        base_update(
            21, identity_status="probable",
            identity_evidence="The distinctive exact name aligns with Colonel Harry F. Wanvig in an official interwar Army unit history, but no direct OSS or Box 815 bridge was accessible online.",
            personnel_category="commissioned_army_officer", commissioned_officer=True,
            allied_or_foreign_personnel=False, research_status="requires_archival_review",
            next_action="Review the indexed Box 815 personnel file to confirm the probable identity and determine what followed the 309th Field Artillery Regiment command after October 1940.",
        ),
        base_update(
            22, identity_status="high_confidence",
            identity_evidence="A scholarly article identifies Douglas Waples as a University of Chicago professor in wartime intelligence and cites the same RG 226 Entry A1-224 Box 815 personnel file.",
            research_status="documented_prewar_employer_found",
            next_action="Review the indexed Box 815 personnel file to determine whether University of Chicago was the immediate predecessor or last civilian employer and to resolve the intervening wartime government sequence.",
        ),
    ])
    return values


def research_attempts() -> list[dict[str, object]]:
    attempts: list[dict[str, object]] = []
    for row, (person_id, name) in PEOPLE.items():
        if row in ARMY_OCCUPATIONS:
            outcome, reviewed, rejected = "source_reviewed", 9, 5
            note = f"A reviewed Army bridge supports identity and a qualified {ARMY_OCCUPATIONS[row]['occupation']} category at Army entry; no named employer or exact OSS-transfer date is supplied."
        elif row in ARMY_IDENTITY_ONLY:
            outcome, reviewed, rejected = "source_reviewed", 8, 5
            note = "A reviewed Army bridge supports identity only; residual civilian code 999 is not interpreted."
        elif row == 11:
            outcome, reviewed, rejected = "candidate_rejected", 9, 6
            note = "A shared protected identifier creates a material collision between different index names; Army identity and occupation evidence were withheld."
        elif row == 13:
            outcome, reviewed, rejected = "source_reviewed", 10, 6
            note = "A scholarly source supports the exact Major Robert E Wampler identity and OSS Special Operations Branch assignment in Kunming, but not a pre-OSS affiliation."
        elif row == 21:
            outcome, reviewed, rejected = "source_reviewed", 10, 6
            note = "An official Army source supports a probable exact-name identity and a dated 309th Field Artillery Regiment command; the later service sequence remains unbridged."
        elif row == 22:
            outcome, reviewed, rejected = "source_reviewed", 12, 5
            note = "A scholarly article cites the exact Box 815 personnel file, and University of Chicago finding aids support documented pre-OSS university employment."
        elif row == 18:
            outcome, reviewed, rejected = "candidate_rejected", 8, 7
            note = UNRESOLVED[row]
        else:
            outcome, reviewed, rejected = "no_result", 7, 7
            note = UNRESOLVED[row]
        attempts.append({
            "key": f"page490-row{row}-{slug(name)}-b999",
            "person_id": person_id,
            "source_adapter": "manual_staged_protocol",
            "query_text": f"{name}; NARA OSS index context; CIA Reading Room exact-name domain check; Library of Congress collection check; exact-name and meaningful variants; OSS, rank, branch, assignment and identifier clues; employer and occupation 1940; obituary, institutional, newspaper, directory and archival searches; indexed Box {'814' if row == 3 else '815'}; protected identifiers used only in private official-record comparison",
            "query_variant_type": "staged_identity_employment_archival_protocol_batch_999",
            "started_at": "2026-11-03T16:10:00Z",
            "completed_at": "2026-11-03T18:10:00Z",
            "outcome": outcome,
            "sources_reviewed": reviewed,
            "candidate_sources_rejected": rejected,
            "rejection_reasons": "Unbridged namesakes, search-result snippets, commercial people-finder pages, unsourced genealogy, relatives, modern or postwar-only leads, and sources without an OSS, protected-identifier, rank, unit, or personnel-file bridge were rejected. The John C Wantland directory salesman, unrelated Robert Wampler biographies, British John Warburton namesakes, and modern Waples results were not assigned. Historical occupation categories were not converted into named employers.",
            "research_notes": f"{note} Exact-name OSS, employer, occupation, obituary, institutional, newspaper, official-domain, and archival searches were checked as applicable. Direct CIA adapter access stopped at the site's robots restriction and was not bypassed; indexed official-domain results were checked instead. The LoC adapter timed out on its first request; no success is claimed, and alternate institutional and newspaper discovery checks were performed. The NARA index page was text-extracted, rendered, and visually checked; official Army bulk data, technical documentation, and code documentation were inspected locally. No authenticated NARA Catalog API call was made.",
            "next_action": f"Review the indexed Box {'814' if row == 3 else '815'} personnel file for corroborating identifiers, the immediate pre-OSS affiliation, and the last civilian employer before wartime service.",
            "attempt_number": 1,
            "research_agent_version": "before-oss-b999-v1",
        })
    return attempts


def main() -> None:
    bundle = {
        "bundle_version": "batch-999-v1",
        "reviewer": "Before OSS Batch 999 evidence review",
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
